"""Test the marker check by breaking it.

A self-test that reports "ok" is only meaningful if it can report "not ok" for the
right reason. Two deliberate breakages:

1. Point a marker at a string no guard emits -> that mutation must FAIL, and only
   that one.
2. Disable one guard entirely -> the mutation exercising it must FAIL, and the
   failure must name that mutation rather than some other.

Both are applied to a COPY; the real file is never modified.
"""

import pathlib
import re
import shutil
import subprocess
import tempfile

BIO = pathlib.Path(__file__).parent


def run(src: str) -> tuple[int, str]:
    with tempfile.TemporaryDirectory() as td:
        tmp = pathlib.Path(td) / "audit_claims.py"
        tmp.write_text(src)
        # Run in place of the real module so relative paths still resolve.
        real = BIO / "audit_claims.py"
        backup = real.read_text()
        try:
            real.write_text(src)
            r = subprocess.run(
                ["uv", "run", "python", "audit_claims.py", "--self-test"],
                cwd=BIO, capture_output=True, text=True,
            )
            return r.returncode, r.stdout + r.stderr
        finally:
            real.write_text(backup)


orig = (BIO / "audit_claims.py").read_text()

print("=== breakage 1: a marker pointing at a string no guard emits ===")
b1 = orig.replace(
    "'an allele frequency presented as a carrier frequency':\n"
    "            'a gnomAD ALLELE frequency used as a carrier frequency',",
    "'an allele frequency presented as a carrier frequency':\n"
    "            'THIS STRING IS EMITTED BY NO GUARD',",
    1,
)
assert b1 != orig, "breakage 1 changed nothing"
rc, out = run(b1)
fails = [ln for ln in out.splitlines() if "SELF-TEST FAILED" in ln]
print(f"  exit={rc}  failures={len(fails)}")
for f in fails:
    print("   ", f[:150])
ok1 = rc != 0 and len(fails) == 1 and "allele frequency" in fails[0]
print(f"  -> {'PASS' if ok1 else 'DID NOT BEHAVE AS REQUIRED'}: exactly the mutated "
      "label fails, and only it")

print()
print("=== breakage 2: disable one guard entirely ===")
b2 = re.sub(
    r'    _require\(problems, results, "\*\*6/8 strict\.\*\*", "RESULTS\.md", '
    r'"the FHA 6/8 headline"\)',
    "    pass  # guard deliberately disabled for the breakage test",
    orig,
)
assert b2 != orig, "breakage 2 changed nothing"
rc, out = run(b2)
fails = [ln for ln in out.splitlines() if "SELF-TEST FAILED" in ln]
print(f"  exit={rc}  failures={len(fails)}")
for f in fails:
    print("   ", f[:150])
ok2 = rc != 0 and len(fails) == 1 and "FHA headline" in fails[0]
print(f"  -> {'PASS' if ok2 else 'DID NOT BEHAVE AS REQUIRED'}: the disabled guard's "
      "own mutation fails, and only it")

print()
print("=== control: unmodified file ===")
rc, out = run(orig)
print(f"  exit={rc}  -> {'PASS' if rc == 0 else 'FAIL'}")
assert (BIO / "audit_claims.py").read_text() == orig, "real file was left modified!"
print("  real audit_claims.py restored byte-for-byte")
raise SystemExit(0 if (ok1 and ok2 and rc == 0) else 1)
