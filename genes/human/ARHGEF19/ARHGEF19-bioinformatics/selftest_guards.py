#!/usr/bin/env python3
"""Mutation tests for dh_competence_check.py.

Run from this directory:  uv run python selftest_guards.py

A check that never fails is not a check. Each case below breaks exactly one
thing and asserts the expected guard fires with the expected exit code; the
first case is a NEGATIVE CONTROL that must stay silent. Mutation is done by
rebinding a named module attribute, so every anchor matches exactly once by
construction -- there is no string-replacement that could match zero times
(silently passing) or twice (silently corrupting a second site).

Exit 0 = every guard behaved as specified.
"""

from __future__ import annotations

import contextlib
import copy
import io
import sys
from dataclasses import replace

import dh_competence_check as mod

FAIL_EXIT = 1  # a published claim or control expectation did not hold
TOOLING_EXIT = 2  # an input was not what the script requires


def run_main() -> int:
    """Run main(), returning its exit code whether returned or raised."""
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
            return mod.main()
    except SystemExit as exc:
        return int(exc.code or 0)
    finally:
        run_main.last_output = buf.getvalue()  # type: ignore[attr-defined]


def snapshot() -> dict:
    return {
        "RESIDUE_CLAIMS": copy.deepcopy(mod.RESIDUE_CLAIMS),
        "IPM_CLAIM": mod.IPM_CLAIM,
        "PDB_8YR7_WGEF_PEPTIDE": mod.PDB_8YR7_WGEF_PEPTIDE,
        "TARGET_LEN": mod.TARGET_LEN,
        "CONTACT_CUTOFF_A": mod.CONTACT_CUTOFF_A,
        "TEMPLATES": copy.deepcopy(mod.TEMPLATES),
        "PANEL": copy.deepcopy(mod.PANEL),
        "TRUNCATION_CONTROL": mod.TRUNCATION_CONTROL,
    }


def restore(snap: dict) -> None:
    for k, v in snap.items():
        setattr(mod, k, copy.deepcopy(v))


CASES: list[tuple[str, object, int, str]] = []


def case(name, mutate, expect_code, expect_text):
    CASES.append((name, mutate, expect_code, expect_text))


# --- negative control: nothing broken, nothing may fire ----------------------
case("negative control (unmutated)", lambda: None, 0, "All assertions held.")


# --- Test 1 guards -----------------------------------------------------------
def break_residue_claim():
    pos, _, src, what = mod.RESIDUE_CLAIMS[0]
    mod.RESIDUE_CLAIMS = [(pos, "W", src, what)]


case("wrong expected residue at Y295", break_residue_claim, FAIL_EXIT,
     "residue claim PMID:38714795 W295")


def break_ipm():
    lo, hi, _, src = mod.IPM_CLAIM
    mod.IPM_CLAIM = (lo, hi, "AAAAAAAAAAA", src)


case("wrong expected IPM sequence", break_ipm, FAIL_EXIT, "IPM 349-359")


def break_peptide():
    mod.PDB_8YR7_WGEF_PEPTIDE = "WWWWWWWWW"


case("8YR7 peptide absent from the protein", break_peptide, FAIL_EXIT,
     "8YR7 peptide not uniquely located")


def break_peptide_ambiguous():
    mod.PDB_8YR7_WGEF_PEPTIDE = "L"  # occurs many times


case("8YR7 peptide not unique", break_peptide_ambiguous, FAIL_EXIT,
     "8YR7 peptide not uniquely located")


# --- tooling guards ----------------------------------------------------------
def break_target_len():
    mod.TARGET_LEN = 803


case("UniProt sequence length changed", break_target_len, TOOLING_EXIT,
     "expected 803")


def break_cutoff():
    mod.CONTACT_CUTOFF_A = 0.5


case("contact cutoff too tight to find an interface", break_cutoff,
     TOOLING_EXIT, "no GEF-GTPase contacts found")


def break_chain():
    mod.TEMPLATES = [("1X86", "Q9NZN5", "Z", "B"), mod.TEMPLATES[1]]


case("template chain id wrong", break_chain, TOOLING_EXIT, "chain Z not present")


def break_numbering():
    # Point 1X86's GEF chain at the WRONG UniProt entry. The auth-numbering
    # cross-check must notice that the residue types do not agree.
    mod.TEMPLATES = [("1X86", "Q15811", "A", "B"), mod.TEMPLATES[1]]


case("template mapped to the wrong UniProt entry", break_numbering,
     TOOLING_EXIT, "auth numbering does not match")


# --- Test 2 / Test 4 control guards -----------------------------------------
def break_negative_control():
    mod.PANEL = [
        replace(m, expect_dh=True) if m.acc == "Q06187" else m for m in mod.PANEL
    ]


case("BTK expected to contain a DH domain", break_negative_control, FAIL_EXIT,
     "PF00621 expectation failed for Q06187")


def break_truncation_control():
    # Point the truncation-control checks at the full-length protein instead. It
    # then trivially spans as much of the exchange surface as itself, and the
    # "must span fewer" guard has to fire.
    mod.TRUNCATION_CONTROL = mod.TARGET


case("truncation control aimed at the full-length protein",
     break_truncation_control, FAIL_EXIT, "truncation control spans fewer")


def break_panel_uniqueness():
    mod.PANEL = [
        replace(m, acc=mod.TARGET) if m.acc == "Q8IW93-2" else m for m in mod.PANEL
    ]


case("duplicate accession in the panel", break_panel_uniqueness, TOOLING_EXIT,
     "duplicate accession(s) in PANEL")


def quote_checker_cases() -> int:
    """Mutation-test verify_quotes.py on a throwaway copy of the review.

    Kept separate from the CASES table because it drives a different script:
    verify_quotes reads the review YAML from disk, so each case writes a
    deliberately corrupted copy to a temp file and asserts the checker notices.
    Case 1 is the negative control -- the unmodified review must pass.
    """
    import copy as _copy
    import tempfile

    import yaml

    import verify_quotes as vq

    doc = yaml.safe_load(vq.REVIEW.read_text(encoding="utf-8"))
    failures = 0

    def run(mutated, expect_code, expect_text, name):
        nonlocal failures
        with tempfile.NamedTemporaryFile(
            "w", suffix="-ai-review.yaml", delete=False, encoding="utf-8"
        ) as fh:
            yaml.safe_dump(mutated, fh, allow_unicode=True, sort_keys=False)
            tmp = fh.name
        buf = io.StringIO()
        try:
            with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
                code = vq.main(__import__("pathlib").Path(tmp))
        except SystemExit as exc:
            code = int(exc.code or 0)
        out = buf.getvalue()
        ok = code == expect_code and expect_text in out
        print(f"[{'PASS' if ok else 'FAIL'}] {name}  exit={code} (want {expect_code})"
              f"  message {'found' if expect_text in out else 'NOT FOUND'}: "
              f"{expect_text!r}")
        if not ok:
            failures += 1

    run(doc, 0, "Every quote is a verbatim substring", "quote checker: unmutated review")

    # A PMID quote reworded by one word must fail.
    m = _copy.deepcopy(doc)
    m["references"][3]["findings"][0]["supporting_text"] = (
        "Expression of hWGEF and XWGEF DECREASED the level of active RhoA"
    )
    run(m, 1, "quote not found in PMID_18256687.md",
        "quote checker: reworded PMID quote")

    # A file: quote -- the class CI never checks -- reworded must also fail.
    m = _copy.deepcopy(doc)
    m["references"][25]["findings"][0]["supporting_text"] = (
        "25 of the 25 RhoA-contacting positions are present"
    )
    run(m, 1, "quote not found in RESULTS.md",
        "quote checker: reworded file: quote")

    # A Reactome quote reworded must fail.
    m = _copy.deepcopy(doc)
    m["references"][21]["findings"][0]["supporting_text"] = (
        "Following NGF binding, p75NTR inactivates the RAC GTPase."
    )
    run(m, 1, "quote not found in R-HSA-205039.md",
        "quote checker: reworded Reactome quote")

    # A reference pointing at a file that does not exist must fail.
    m = _copy.deepcopy(doc)
    m["references"][25]["id"] = "file:human/ARHGEF19/ARHGEF19-bioinformatics/NOPE.md"
    run(m, 1, "does not exist", "quote checker: missing source file")

    return failures


def main() -> int:
    snap = snapshot()
    width = max(len(n) for n, *_ in CASES)
    failures = 0
    for name, mutate, expect_code, expect_text in CASES:
        restore(snap)
        mutate()
        code = run_main()
        out = run_main.last_output  # type: ignore[attr-defined]
        code_ok = code == expect_code
        text_ok = expect_text in out
        ok = code_ok and text_ok
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] {name.ljust(width)}  exit={code} (want {expect_code})"
              f"  message {'found' if text_ok else 'NOT FOUND'}: {expect_text!r}")
        if not ok:
            failures += 1
            if not text_ok:
                print("        ---- captured output ----")
                for line in out.splitlines()[-25:]:
                    print(f"        {line}")
    restore(snap)
    print()
    failures += quote_checker_cases()
    print()
    total = len(CASES) + 5
    if failures:
        print(f"{failures}/{total} guard(s) did not behave as specified.")
        return 1
    print(f"All {total} guards behaved as specified "
          "(including the two negative controls, which stayed silent).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
