"""judge.py 검증 (R8).

사용: python harness/tests/run_tests.py
- fixtures/pass  → 모든 게이트 exit 0, 위반 0
- fixtures/fail  → 게이트별 규칙 ID·건수 = fixtures/fail-expected.json
- N1·N2 규칙 7개가 fail에서 모두 잡혀야 함 (★)
- 빈 실행 폴더 → exit 2
샘플은 임시 폴더로 복사해서 돌린다 (fixtures 원본은 바뀌지 않음).
"""
import json
import shutil
import subprocess
import sys
import tempfile
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
JUDGE = HERE.parent / "scripts" / "judge.py"
GATES = ["S1", "S2", "S3", "S5"]
N_RULES = {"N1-a", "N1-b", "N1-c", "N1-d", "N2-a", "N2-b", "N2-c", "GM1", "GM2", "GM3", "GM4", "GM5"}
failures = []


def judge(*args):
    p = subprocess.run([sys.executable, str(JUDGE), *args], capture_output=True, text=True, encoding="utf-8")
    return p.returncode, p.stdout.strip()


def prepare(name, tmp, baseline):
    run = Path(tmp) / name
    shutil.copytree(HERE / "fixtures" / name, run)
    state = json.loads((run / "state.json").read_text(encoding="utf-8"))
    state["baseline_hash"] = baseline
    (run / "state.json").write_text(json.dumps(state), encoding="utf-8")
    return run


def check(cond, msg):
    print(("  ok   " if cond else "  FAIL ") + msg)
    if not cond:
        failures.append(msg)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    code, current = judge("--hash")
    check(code == 0 and len(current) == 64, "judge.py --hash")
    expected = json.loads((HERE / "fixtures" / "fail-expected.json").read_text(encoding="utf-8"))

    with tempfile.TemporaryDirectory() as tmp:
        print("[pass]")
        run = prepare("pass", tmp, current)
        for g in GATES:
            code, out = judge("--gate", g, "--run", str(run))
            res = json.loads((run / "judge" / f"gate-{g}.json").read_text(encoding="utf-8"))
            check(code == 0 and res["pass"], f"{g}: exit {code}, 위반 {len(res['violations'])}건 (기대 0)")
            for x in res["violations"]:
                print("        ", x)

        print("[fail]")
        run = prepare("fail", tmp, "0" * 64)
        caught = set()
        for g in GATES:
            code, out = judge("--gate", g, "--run", str(run))
            res = json.loads((run / "judge" / f"gate-{g}.json").read_text(encoding="utf-8"))
            got = dict(Counter(x["rule"] for x in res["violations"]))
            caught |= set(got)
            check(code == 1 and got == expected[g], f"{g}: exit {code}, 규칙 {len(got)}종 (기대 {len(expected[g])}종)")
            if got != expected[g]:
                print("         기대:", expected[g])
                print("         실제:", got)
        all_rules = {r for g in expected.values() for r in g}
        check(caught == all_rules, f"전체 규칙 {len(caught)}/{len(all_rules)}종 검출")
        check(N_RULES <= caught, f"★ N1·N2·GM 규칙 {len(N_RULES & caught)}/{len(N_RULES)} 검출")

        print("[split]")
        split = Path(tmp) / "split"
        shutil.copytree(HERE / "fixtures" / "pass", split)
        st = json.loads((split / "state.json").read_text(encoding="utf-8"))
        st["baseline_hash"] = current
        (split / "state.json").write_text(json.dumps(st), encoding="utf-8")
        for g, rel in (("S3", "s3-keyscreens"), ("S5", "s4-frames")):
            src = split / "design" / f"{rel}.json"
            doc = json.loads(src.read_text(encoding="utf-8"))
            (split / "design" / rel).mkdir()
            for f in doc["frames"]:
                part = {"figma_file": doc.get("figma_file"), "frames": [f]}
                (split / "design" / rel / f"{f['name']}.json").write_text(json.dumps(part, ensure_ascii=False), encoding="utf-8")
            code, out = judge("--gate", g, "--run", str(split))
            check(code == 2, f"{g}: 단일 파일 + 폴더 둘 다 → exit {code} (기대 2)")
            src.unlink()
            code, out = judge("--gate", g, "--run", str(split))
            check(code == 0, f"{g}: 프레임별 파일 {len(doc['frames'])}개 → exit {code} (기대 0)")

        print("[empty]")
        empty = Path(tmp) / "empty"
        empty.mkdir()
        for g in GATES:
            code, out = judge("--gate", g, "--run", str(empty))
            check(code == 2, f"{g}: exit {code} (기대 2)")

    print(f"\n{'PASS' if not failures else 'FAIL'} · 실패 {len(failures)}건")
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
