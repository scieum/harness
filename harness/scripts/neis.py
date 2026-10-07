"""NEIS 학교기본정보 → 화면 14(회원가입 학교 선택) 시안용 실제 데이터.

사용:
  python harness/scripts/neis.py --run runs/{id}

- 인증키: 환경변수 NEIS_API_KEY 또는 프로젝트 루트 .env (git 제외). 결과 파일에 키를 쓰지 않는다.
- 설정 값: harness/rules.json `neis` (exclude_sido에 든 시/도는 뺀다)
- 시/도·지역: input.json school_sido·school_region (없으면 rules.json 기본값)
- 학교급: rules.json neis.school_kinds (초·중·고), 시안용 고른 학교급 = input.json school_kind (없으면 neis.default_kind)
- 결과: {run}/neis.json = {sido_list, sido, region_list, region, kind_list, kind, school_list, school_count_by_kind}
종료 코드: 0 성공 / 2 실패(키 없음·API 오류)
"""
import argparse
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RULES_PATH = ROOT / "harness" / "rules.json"
PAGE = 1000


def read_key(cfg):
    key = os.environ.get(cfg["key_env"])
    env = ROOT / cfg["key_file"]
    if not key and env.exists():
        for line in env.read_text(encoding="utf-8").splitlines():
            name, _, val = line.partition("=")
            if name.strip() == cfg["key_env"]:
                key = val.strip()
    if not key:
        raise RuntimeError(f"{cfg['key_env']} 없음 (환경변수 또는 {cfg['key_file']})")
    return key


def fetch_all(cfg, key):
    rows = []
    for kind in cfg["school_kinds"]:
        rows += fetch_kind(cfg, key, kind)
    return rows


def fetch_kind(cfg, key, kind):
    rows, page = [], 1
    while True:
        q = urllib.parse.urlencode({"KEY": key, "Type": "json", "pIndex": page, "pSize": PAGE,
                                    "SCHUL_KND_SC_NM": kind})
        with urllib.request.urlopen(f"{cfg['endpoint']}?{q}", timeout=30) as res:
            data = json.load(res)
        if data.get("RESULT", {}).get("CODE") == "INFO-200":  # 해당 데이터 없음
            return rows
        if "schoolInfo" not in data:
            raise RuntimeError(f"NEIS 응답 오류: {data.get('RESULT', data)}")
        head, body = data["schoolInfo"]
        rows += body["row"]
        if len(rows) >= head["head"][0]["list_total_count"]:
            return rows
        page += 1


def region_of(row, sido_field):
    parts = (row.get("ORG_RDNMA") or "").split()
    if len(parts) > 1 and re.search(r"(시|군|구)$", parts[1]):
        return parts[1]
    return row[sido_field]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    a = ap.parse_args()

    cfg = json.loads(RULES_PATH.read_text(encoding="utf-8"))["neis"]
    SIDO = cfg["sido_field"]
    run = Path(a.run)
    inp = json.loads((run / "input.json").read_text(encoding="utf-8"))
    sido = inp.get("school_sido") or cfg["default_sido"]
    region = inp.get("school_region") or cfg["default_region"]
    kind = inp.get("school_kind") or cfg["default_kind"]
    if kind not in cfg["school_kinds"]:
        print(f"neis: 실패 — 학교급 '{kind}' 없음 (가능: {cfg['school_kinds']})")
        return 2

    try:
        rows = fetch_all(cfg, read_key(cfg))
        rows = [r for r in rows if r[SIDO] not in cfg.get("exclude_sido", [])]
    except Exception as e:  # 네트워크·키·응답 오류 모두 판정 불가로 본다
        print(f"neis: 실패 — {e}")
        return 2

    in_sido = [r for r in rows if r[SIDO] == sido]
    if not in_sido:
        print(f"neis: 실패 — 시/도 '{sido}' 학교 0개")
        return 2
    regions = sorted({region_of(r, SIDO) for r in in_sido})
    if region not in regions:
        print(f"neis: 실패 — '{sido}'에 지역 '{region}' 없음 (가능: {regions})")
        return 2
    in_region = [r for r in in_sido if region_of(r, SIDO) == region]
    out = {
        "source": cfg["endpoint"],
        "kind_list": cfg["school_kinds"],
        "kind": kind,
        "sido_list": sorted({r[SIDO] for r in rows}),
        "sido": sido,
        "region_list": regions,
        "region": region,
        "school_list": sorted(r["SCHUL_NM"] for r in in_region if r["SCHUL_KND_SC_NM"] == kind),
        "school_count_by_kind": {k: sum(r["SCHUL_KND_SC_NM"] == k for r in in_region) for k in cfg["school_kinds"]},
    }
    path = run / cfg["output"]
    path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"neis: 시/도 {len(out['sido_list'])} · {sido} 지역 {len(regions)} · {region} {kind} {len(out['school_list'])} (학교급별 {out['school_count_by_kind']})\n결과: {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
