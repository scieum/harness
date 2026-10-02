"""Lab_Stock 하네스 판정 스크립트 (읽기 전용 판정자).

사용:
  python harness/scripts/judge.py --gate {S1|S2|S3|S5} --run runs/{id}
  python harness/scripts/judge.py --hash

규칙 값은 harness/rules.json 에서만 읽는다.
결과: {run}/judge/gate-{X}.json
종료 코드: 0 통과 / 1 위반 있음 / 2 판정 불가
"""
import argparse
import fnmatch
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RULES_PATH = ROOT / "harness" / "rules.json"

D_RULES = ["D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D10", "C1", "C2"]
N_RULES = ["N1-a", "N1-b", "N1-c", "N1-d", "N2-a", "N2-b", "N2-c"]
GATES = {
    "S1": ["S1-a", "S1-b", "F1", "F2"],
    "S2": ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "C1", "N1-d", "N2-a", "N2-c", "F1", "F2"],
    "S3": D_RULES + N_RULES + ["F1", "F2"],
    "S5": D_RULES + ["D9"] + N_RULES + ["F1", "F2"],
}
FRAME_FILE = {"S3": "design/s3-keyscreens.json", "S5": "design/s4-frames.json"}


class CannotJudge(Exception):
    pass


def v(rule, where, actual, allowed):
    return {"rule": rule, "node": where, "actual": actual, "allowed": allowed}


# ---------- 입력 읽기 ----------

def read_json(path):
    if not path.exists():
        raise CannotJudge(f"파일 없음: {path.name}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        raise CannotJudge(f"JSON 형식 오류: {path.name} ({e})")


def read_text(path):
    if not path.exists():
        raise CannotJudge(f"파일 없음: {path.relative_to(path.parents[1])}")
    return path.read_text(encoding="utf-8")


def md_tables_by_section(text, section_re):
    """section_re에 맞는 '## ' 제목 아래 표들을 {제목그룹: [row dict]}로 돌려준다."""
    out, key, block = {}, None, []

    def flush():
        if key is not None and len(block) >= 2:
            header = [c.strip() for c in block[0].strip().strip("|").split("|")]
            for line in block[2:]:
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                cells += [""] * (len(header) - len(cells))
                out.setdefault(key, []).append(dict(zip(header, cells)))

    for line in text.splitlines():
        if line.startswith("## "):
            flush(); block = []
            m = re.match(section_re, line[3:].strip())
            key = m.group(1) if m else None
        elif line.strip().startswith("|"):
            block.append(line)
        else:
            flush(); block = []
    flush()
    return out


def frame_screen(name, rules):
    if not re.match(rules["frames"]["name_pattern"], name):
        return None
    return int(name.split("-")[0])


def iter_nodes(frames):
    for f in frames:
        for n in f.get("nodes", []):
            yield f, n


def texts(frames):
    return [(f, n, n["text"]["characters"]) for f, n in iter_nodes(frames) if n.get("text")]


def where(f, n):
    return "/".join(n.get("path") or [f["name"], n.get("name", "?")])


def load_inputs(gate, run):
    data = {"input": read_json(run / "input.json"), "state": read_json(run / "state.json")}
    if not isinstance(data["input"].get("screens"), list):
        raise CannotJudge("input.json에 screens 목록 없음")
    if gate == "S1":
        data["refs"] = md_tables_by_section(read_text(run / "research/s1-references.md"), r"화면\s*(\d+)")
        data["adopt"] = md_tables_by_section(read_text(run / "research/s1-adopt.md"), r"화면\s*(\d+)")
    if gate in ("S2", "S3", "S5"):
        data["spec"] = read_text(run / "spec/s2-spec.md")
    if gate == "S2":
        table = md_tables_by_section(data["spec"], r"(역할별 노출)").get("역할별 노출")
        if not table:
            raise CannotJudge("s2-spec.md에 '## 역할별 노출' 표 없음")
        roles = {}
        for row in table:
            comp = row.get("컴포넌트", "")
            try:
                roles[comp] = {k: int(val) for k, val in row.items() if k != "컴포넌트"}
            except ValueError:
                raise CannotJudge(f"역할별 노출 표의 숫자가 아님: {comp}")
        data["roles"] = roles
    if gate in FRAME_FILE:
        data["frames"] = load_frames(run, FRAME_FILE[gate])
    return data


def load_frames(run, rel):
    """단일 파일(design/s4-frames.json) 또는 프레임별 폴더(design/s4-frames/*.json) 중 하나."""
    single, folder = run / rel, run / rel[:-len(".json")]
    if single.exists() and folder.is_dir():
        raise CannotJudge(f"{rel}과 {folder.name}/ 가 둘 다 있음 — 하나만 둔다")
    if not folder.is_dir():
        doc = read_json(single)
        if not isinstance(doc.get("frames"), list):
            raise CannotJudge(f"{rel}에 frames 목록 없음")
        return doc["frames"]
    parts = sorted(folder.glob("*.json"))
    if not parts:
        raise CannotJudge(f"{folder.name}/ 에 프레임 파일 없음")
    frames = []
    for p in parts:
        doc = read_json(p)
        if not isinstance(doc.get("frames"), list):
            raise CannotJudge(f"{folder.name}/{p.name}에 frames 목록 없음")
        frames += doc["frames"]
    return frames


# ---------- S1 ----------

def check_S1a(d, r, run):
    lo, hi = r["s1"]["refs_per_screen"]
    out = []
    for s in d["input"]["screens"]:
        rows = d["refs"].get(str(s), [])
        n = sum(1 for row in rows if any(c.startswith("http") for c in row.values()))
        if not lo <= n <= hi:
            out.append(v("S1-a", f"화면 {s}", n, f"{lo}~{hi}"))
    return out


def check_S1b(d, r, run):
    out = []
    for s in d["input"]["screens"]:
        adopt = {row.get("ui_url", ""): row.get("가져올 것", "") for row in d["adopt"].get(str(s), [])}
        for row in d["refs"].get(str(s), []):
            url = row.get("ui_url", "")
            if url.startswith("http") and not adopt.get(url, "").strip():
                out.append(v("S1-b", f"화면 {s} {url}", "빈 칸", "가져올 것 1줄"))
    return out


# ---------- R (역할) ----------

def role_count(d, comp, role):
    return d["roles"].get(comp, {}).get(role, 0)


def check_roles(rule_id):
    def check(d, r, run):
        spec = r["roles"][rule_id]
        all_roles = r["roles"]["R4"]["roles"]
        out = []
        if "max" in spec:
            for comp in spec.get("components", [spec.get("component")]):
                n = role_count(d, comp, spec["role"])
                if n > spec["max"]:
                    out.append(v(rule_id, f"{spec['role']}/{comp}", n, f"≤ {spec['max']}"))
        if "only_roles" in spec:
            comp = spec["component"]
            for role in all_roles:
                n = role_count(d, comp, role)
                if role in spec["only_roles"] and n < 1:
                    out.append(v(rule_id, f"{role}/{comp}", n, "≥ 1"))
                if role not in spec["only_roles"] and n > 0:
                    out.append(v(rule_id, f"{role}/{comp}", n, "0"))
        if "min_per_role" in spec:
            comp = spec["component"]
            for role in spec["roles"]:
                n = role_count(d, comp, role)
                if n < spec["min_per_role"]:
                    out.append(v(rule_id, f"{role}/{comp}", n, f"≥ {spec['min_per_role']}"))
        return out
    return check


# ---------- D (디자인 가이드) ----------

def norm_color(c):
    return re.sub(r"\s+", "", str(c)).lower()


def check_D1(d, r, run):
    allowed = {norm_color(c) for c in r["colors"]["allowed"]}
    rgba = {norm_color(x["value"]): x["only_in"] for x in r["colors"]["allowed_rgba"]}
    out = []
    for f, n in iter_nodes(d["frames"]):
        for c in n.get("fills", []) + n.get("strokes", []):
            c = norm_color(c)
            if c in allowed:
                continue
            if c in rgba and rgba[c] in (n.get("path") or []):
                continue
            out.append(v("D1", where(f, n), c, "colors.allowed"))
    return out


def check_D2(d, r, run):
    out = []
    for key in ("accent", "accent_soft"):
        if key not in r["colors"]:
            continue
        acc = norm_color(r["colors"][key]["value"])
        ok = r["colors"][key]["only_within"]
        for f, n in iter_nodes(d["frames"]):
            colors = [norm_color(c) for c in n.get("fills", []) + n.get("strokes", [])]
            if acc in colors and not any(p in ok for p in (n.get("path") or [])):
                out.append(v("D2", where(f, n), acc, f"{ok} 안에서만"))
    return out


def check_D10(d, r, run):
    hl = r["colors"]["highlight"]
    vals = {norm_color(c) for c in hl["values"]}
    no_text = {norm_color(c) for c in hl["no_text"]}
    out = []
    for f, n in iter_nodes(d["frames"]):
        colors = {norm_color(c) for c in n.get("fills", []) + n.get("strokes", [])}
        used = sorted(colors & vals)
        if not used:
            continue
        inside = [p for p in (n.get("path") or []) if p in hl["forbidden_within"]]
        if inside:
            out.append(v("D10", where(f, n), used, f"{hl['forbidden_within']} 밖에서만"))
        if n.get("text") and colors & no_text:
            out.append(v("D10", where(f, n), sorted(colors & no_text), "하늘색 글자 금지 (#141414)"))
    return out


def radii(n):
    cr = n.get("cornerRadius")
    if cr is None:
        return []
    return cr if isinstance(cr, list) else [cr]


def check_D3(d, r, run):
    allowed = r["radius"]["allowed"]
    return [v("D3", where(f, n), x, allowed)
            for f, n in iter_nodes(d["frames"]) for x in radii(n) if x not in allowed]


def check_D4(d, r, run):
    t = r["typography"]
    out = []
    for f, n, _ in texts(d["frames"]):
        tx = n["text"]
        fams = [t["family"]] + ([t["figma_fallback_family"]] if t.get("figma_fallback_family") else [])
        if tx.get("fontFamily") not in fams:
            out.append(v("D4", where(f, n), tx.get("fontFamily"), fams))
        if tx.get("fontWeight") not in t["weights"]:
            out.append(v("D4", where(f, n), tx.get("fontWeight"), t["weights"]))
        if tx.get("fontSize") not in t["sizes"]:
            out.append(v("D4", where(f, n), tx.get("fontSize"), t["sizes"]))
    return out


def check_D5(d, r, run):
    t = r["typography"]
    out = []
    for f, n, _ in texts(d["frames"]):
        tx = n["text"]
        if tx.get("letterSpacing", 0) != t["letter_spacing"]:
            out.append(v("D5", where(f, n), tx.get("letterSpacing"), t["letter_spacing"]))
        if tx.get("textCase", "ORIGINAL") not in t["text_case"]:
            out.append(v("D5", where(f, n), tx.get("textCase"), t["text_case"]))
    return out


def check_D6(d, r, run):
    exc = r["effects"]["exceptions"]
    out = []
    for f, n in iter_nodes(d["frames"]):
        shadows = [e for e in n.get("effects", []) if e.get("type") == "DROP_SHADOW"]
        if len(shadows) > r["effects"]["drop_shadow_max"] and not any(p in exc for p in (n.get("path") or [])):
            out.append(v("D6", where(f, n), f"DROP_SHADOW {len(shadows)}", f"0 ({exc} 예외)"))
    return out


def check_D7(d, r, run):
    allowed = r["spacing"]["allowed"]
    out = []
    for f, n in iter_nodes(d["frames"]):
        vals = list(n.get("padding") or [])
        if n.get("gap") is not None:
            vals.append(n["gap"])
        out += [v("D7", where(f, n), x, allowed) for x in vals if x not in allowed]
    return out


def check_D8(d, r, run):
    b = r["button"]
    out = []
    for f, n in iter_nodes(d["frames"]):
        if not n.get("name", "").startswith(b["name_prefix"]):
            continue
        if any(x != r["radius"]["button"] for x in radii(n)) or not radii(n):
            out.append(v("D8", where(f, n), n.get("cornerRadius"), r["radius"]["button"]))
        if (n.get("height") or 0) < b["min_height"]:
            out.append(v("D8", where(f, n), n.get("height"), f"≥ {b['min_height']}"))
    return out


def check_D9(d, r, run):
    fr = r["frames"]
    expected = {f"{s}-{dev}" for s in d["input"]["screens"] for dev in ("mobile", "desktop")}
    out = []
    names = set()
    for f in d["frames"]:
        name = f.get("name", "")
        names.add(name)
        if not re.match(fr["name_pattern"], name):
            out.append(v("D9", name, "프레임 이름", fr["name_pattern"]))
            continue
        size = [f.get("width"), f.get("height")]
        want = fr[name.split("-")[1]]
        if size != want:
            out.append(v("D9", name, size, want))
    for name in sorted(expected - names):
        out.append(v("D9", name, "없음", "프레임 필요"))
    for name in sorted(names - expected):
        if re.match(fr["name_pattern"], name):
            out.append(v("D9", name, "대상 밖 프레임", sorted(expected)))
    return out


# ---------- N (어기면 안 되는 것) ----------

def check_N1a(d, r, run):
    n1 = r["never"]["N1"]
    school = d["input"].get("school_name")
    if not school:
        raise CannotJudge("input.json에 school_name 없음")
    out = []
    for f in d["frames"]:
        s = frame_screen(f.get("name", ""), r)
        if s in n1["screens_require_school_name"]:
            if not any(school in t for _, _, t in texts([f])):
                out.append(v("N1-a", f["name"], "학교명 없음", school))
    return out


def check_N1b(d, r, run):
    n1 = r["never"]["N1"]
    pat = re.compile(n1["school_name_pattern"])
    scope = [f for f in d["frames"] if frame_screen(f.get("name", ""), r) in n1["school_name_scope_screens"]]
    names = sorted({m.group(0) for _, _, t in texts(scope) for m in pat.finditer(t)})
    limit = n1["distinct_school_names"]
    return [] if len(names) <= limit else [v("N1-b", f"화면 {n1['school_name_scope_screens']}", names, f"{limit}종")]


def check_N1c(d, r, run):
    only = r["never"]["N1"]["school_select_only_on"]
    return [v("N1-c", where(f, n), "school-select", f"화면 {only}에만")
            for f, n in iter_nodes(d["frames"])
            if n.get("name", "").startswith("school-select") and frame_screen(f.get("name", ""), r) not in only]


def check_N1d(d, r, run):
    """학교 선택 3단계(시/도 → 지역 → 학교): S2는 설계서 해당 화면, S3·S5는 해당 화면 프레임."""
    levels = r["never"]["N1"]["school_select_levels"]
    sel = r["never"]["N1"].get("school_select_screen", 1)
    out = []
    if "frames" not in d:
        if sel not in d["input"]["screens"]:
            return []
        m = re.search(rf"^## 화면\s*{sel}\s*$(.*?)(?=^## |\Z)", d["spec"], re.M | re.S)
        body = m.group(1) if m else ""
        names = re.findall(r"^-\s*([\w-]+)\s*:", body, re.M)
        found = [n for n in names if n in levels]
        if found != levels:
            out.append(v("N1-d", f"spec/s2-spec.md 화면 {sel}", found, levels))
        return out
    for f in d["frames"]:
        if frame_screen(f.get("name", ""), r) != sel:
            continue
        found = [n["name"] for n in f.get("nodes", []) if n.get("name") in levels]
        if found != levels:
            out.append(v("N1-d", f["name"], found, levels))
    return out


def has_banned(text, terms):
    low = text.lower()
    return [t for t in terms if t.lower() in low]


def check_N2a(d, r, run):
    terms = r["never"]["N2"]["banned_terms"]
    out = []
    for i, line in enumerate(d["spec"].splitlines(), 1):
        hit = has_banned(line, terms)
        if hit:
            out.append(v("N2-a", f"spec/s2-spec.md:{i}", hit, "금지어 0"))
    for f, n, t in texts(d.get("frames", [])):
        hit = has_banned(t, terms)
        if hit:
            out.append(v("N2-a", where(f, n), hit, "금지어 0"))
    return out


def check_N2b(d, r, run):
    terms = r["never"]["N2"]["screen5_input_label_banned"]
    out = []
    for f, n, t in texts(d["frames"]):
        if frame_screen(f.get("name", ""), r) != 5:
            continue
        if any(p.startswith("text-input") for p in (n.get("path") or [])[:-1]):
            hit = has_banned(t, terms)
            if hit:
                out.append(v("N2-b", where(f, n), t, f"라벨에 {terms} 금지"))
    return out


def check_C1(d, r, run):
    """화면별 필수 컴포넌트: S2는 설계서의 '## 화면 N' 구성 요소, S3·S5는 그 화면 프레임 노드 이름."""
    req = {int(k): v for k, v in r.get("screens_required", {}).items() if k.isdigit()}
    out = []
    if "frames" not in d:
        for s, comps in req.items():
            m = re.search(rf"^## 화면\s*{s}\s*$(.*?)(?=^## |\Z)", d["spec"], re.M | re.S)
            if not m:
                continue
            names = set(re.findall(r"^-\s*([\w-]+)\s*:", m.group(1), re.M))
            missing = [c for c in comps if c not in names]
            if missing:
                out.append(v("C1", f"spec/s2-spec.md 화면 {s}", f"없음 {missing}", comps))
        return out
    for f in d["frames"]:
        s = frame_screen(f.get("name", ""), r)
        if s not in req:
            continue
        names = {n.get("name") for n in f.get("nodes", [])}
        missing = [c for c in req[s] if c not in names]
        if missing:
            out.append(v("C1", f["name"], f"없음 {missing}", req[s]))
    return out


def check_C2(d, r, run):
    """하단 탭바: 화면 2~13 mobile 프레임마다 tab-bar 1개 + 그 안 tab-item 4개, 그 밖 프레임은 tab-bar 0."""
    tb = r.get("tab_bar")
    if not tb:
        return []
    out = []
    for f in d["frames"]:
        name = f.get("name", "")
        s = frame_screen(name, r)
        if s is None:
            continue
        nodes = f.get("nodes", [])
        bars = [n for n in nodes if n.get("name") == tb["component"]]
        need = name.endswith("-mobile") and s in tb["mobile_screens"]
        if not need:
            if bars:
                out.append(v("C2", name, f"{tb['component']} {len(bars)}개", "0 (로그인·회원가입·desktop)"))
            continue
        if len(bars) != 1:
            out.append(v("C2", name, f"{tb['component']} {len(bars)}개", 1))
            continue
        if "radius" in tb and radii(bars[0]) and any(x != tb["radius"] for x in radii(bars[0])):
            out.append(v("C2", where(f, bars[0]), bars[0].get("cornerRadius"), f"radius {tb['radius']} (사각형)"))
        items = [n for n in nodes if n.get("name") == tb["item"] and tb["component"] in (n.get("path") or [])]
        if len(items) != tb["items"]:
            out.append(v("C2", name, f"{tb['item']} {len(items)}개", tb["items"]))
    return out


def check_N2c(d, r, run):
    pat = re.compile(r["never"]["N2"]["key_value_pattern"])
    out = []
    for i, line in enumerate(d["spec"].splitlines(), 1):
        if pat.search(line):
            out.append(v("N2-c", f"spec/s2-spec.md:{i}", "키 형식 문자열", "0"))
    for f, n, t in texts(d.get("frames", [])):
        if pat.search(t):
            out.append(v("N2-c", where(f, n), "키 형식 문자열", "0"))
    return out


# ---------- F (파일·해시) ----------

def tree_hash(r):
    hs = r["hash_scope"]
    h = hashlib.sha256()
    files = []
    for inc in hs["include"]:
        for p in (ROOT / inc).rglob("*"):
            rel = p.relative_to(ROOT).as_posix()
            if not p.is_file() or any(rel == e or rel.startswith(e + "/") for e in hs["exclude"]):
                continue
            if any(part in hs["exclude_names"] for part in p.parts):
                continue
            files.append((rel, p))
    for rel, p in sorted(files):
        h.update(rel.encode("utf-8") + b"\0" + p.read_bytes() + b"\0")
    return h.hexdigest()


def check_F1(d, r, run):
    allowed = set(r["files"]["allowed"])
    patterns = r["files"].get("allowed_patterns", [])

    def ok(rel):
        return rel in allowed or any(fnmatch.fnmatchcase(rel, pat) for pat in patterns)
    return [v("F1", p.relative_to(run).as_posix(), "허용 목록 밖 파일", "rules.json files.allowed")
            for p in sorted(run.rglob("*")) if p.is_file() and not ok(p.relative_to(run).as_posix())]


def check_F2(d, r, run):
    base = d["state"].get("baseline_hash")
    if not base:
        raise CannotJudge("state.json에 baseline_hash 없음")
    now = tree_hash(r)
    return [] if now == base else [v("F2", "docs/ + harness/", now[:12], base[:12])]


CHECKS = {
    "S1-a": check_S1a, "S1-b": check_S1b,
    "R1": check_roles("R1"), "R2": check_roles("R2"), "R3": check_roles("R3"), "R4": check_roles("R4"),
    "R5": check_roles("R5"), "R6": check_roles("R6"), "R7": check_roles("R7"), "C1": check_C1, "C2": check_C2,
    "D1": check_D1, "D2": check_D2, "D3": check_D3, "D4": check_D4, "D5": check_D5,
    "D6": check_D6, "D7": check_D7, "D8": check_D8, "D9": check_D9, "D10": check_D10,
    "N1-a": check_N1a, "N1-b": check_N1b, "N1-c": check_N1c, "N1-d": check_N1d,
    "N2-a": check_N2a, "N2-b": check_N2b, "N2-c": check_N2c,
    "F1": check_F1, "F2": check_F2,
}


# ---------- 실행 ----------

def write_result(run, gate, result):
    out = run / "judge" / f"gate-{gate}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    return out


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("--gate", choices=list(GATES))
    ap.add_argument("--run")
    ap.add_argument("--hash", action="store_true")
    a = ap.parse_args()

    rules = json.loads(RULES_PATH.read_text(encoding="utf-8"))
    if a.hash:
        print(tree_hash(rules))
        return 0
    if not (a.gate and a.run):
        ap.error("--gate 와 --run 이 필요하다")

    run = Path(a.run)
    if not run.is_dir():
        print(f"판정 불가: 실행 폴더 없음 {run}")
        return 2
    try:
        data = load_inputs(a.gate, run)
        violations = []
        for rule_id in GATES[a.gate]:
            violations += CHECKS[rule_id](data, rules, run)
    except CannotJudge as e:
        out = write_result(run, a.gate, {"gate": a.gate, "pass": False, "exit": 2, "reason": str(e), "violations": []})
        print(f"gate {a.gate}: 판정 불가 — {e}\n결과: {out}")
        return 2

    code = 0 if not violations else 1
    out = write_result(run, a.gate, {"gate": a.gate, "pass": code == 0, "exit": code, "violations": violations})
    print(f"gate {a.gate}: {'통과' if code == 0 else '실패'} · 위반 {len(violations)}건\n결과: {out}")
    return code


if __name__ == "__main__":
    sys.exit(main())
