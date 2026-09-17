"""Break akap12_audit.py deliberately and confirm each guard fires.

A self-test proves only the guards you thought of fire; it cannot tell you which guard you
failed to write. So each mutation here ASSERTS its target string is present before
replacing it - a mutation whose anchor has drifted otherwise "passes" by changing nothing.

Mutants are written to a TEMPFILE and the audit is pointed at it. An earlier version wrote
each mutant over the curated review file and restored it afterwards, which meant an
interrupted run (Ctrl-C, crash, killed shell) could leave deliberately corrupted YAML in the
working tree. A test must not be able to damage the artifact it is testing.
"""
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = None
for cand in [Path.cwd(), *Path.cwd().parents]:
    if (cand / "src").is_dir() and (cand / "publications").is_dir():
        ROOT = cand
        break
if ROOT is None:
    raise SystemExit("could not derive repo root")

AUDIT = Path(__file__).with_name("akap12_audit.py")
REL = "genes/human/AKAP12/AKAP12-ai-review.yaml"

MUTATIONS = [
    (
        "duplicate YAML key",
        "  evidence_type: IDA\n  original_reference_id: PMID:9000000\n",
        "  evidence_type: IDA\n  evidence_type: IPI\n  original_reference_id: PMID:9000000\n",
        "duplicate YAML key",
    ),
    (
        "dropped supporting_entities (row coverage)",
        "  supporting_entities:\n  - UniProtKB-SubCell:SL-0162\n",
        "",
        "row coverage mismatch",
    ),
    (
        "deleted a source_entity",
        "      - source_id: ZFIN:ZDB-GENE-030131-9753\n",
        "      - source_id: ZFIN:ZDB-GENE-030131-9753-DELETED\n",
        "source_entities != GOA WITH/FROM",
    ),
    (
        "harmless prose edit",
        "    action: MARK_AS_OVER_ANNOTATED\n    reason: >-\n      The donor annotation is IEP from PMID:23925424, whose entire content is expression",
        "    action: MARK_AS_OVER_ANNOTATED\n    reason: >-\n      MUTATED. The donor annotation is IEP from PMID:23925424, whose entire content is expression",
        None,  # control: a harmless prose edit must NOT trip anything
    ),
    (
        # exercises the root_cause-vs-action coherence guard: an over-annotation row whose
        # propagation_review simultaneously claims nothing went wrong.
        "root_cause contradicts action",
        "        regeneration or formation of liver fibrosis after various injuries.\n    propagation_review:\n      root_cause: SOURCE_WEAK_OR_INFERRED\n",
        "        regeneration or formation of liver fibrosis after various injuries.\n    propagation_review:\n      root_cause: NO_FAILURE_CORE\n",
        "asserts no failure",
    ),
    (
        "undeclared reference",
        "    - reference_id: PMID:11814414\n",
        "    - reference_id: PMID:99999999\n",
        "cited but not declared",
    ),
    (
        "retracted phrasing reintroduced in core_functions (NOT in description)",
        "    Anchors the type II regulatory subunit dimer of protein kinase A through a C-terminal\n    anchoring region",
        "    Anchors the type II regulatory subunit dimer of protein kinase A through a C-terminal\n    amphipathic helix",
        "retracted phrasing",
    ),
    (
        "required claim partially deleted",
        "    proposed_replacement_terms:\n    - id: GO:0034237\n      label: protein kinase A regulatory subunit binding\n",
        "    proposed_replacement_terms:\n    - id: GO:0005515\n      label: protein binding\n",
        "MODIFY rows targeting GO:0034237",
    ),
    (
        "is_invalid flag removed from the retracted paper",
        "  is_invalid: true\n",
        "",
        "is not flagged is_invalid",
    ),
    (
        "experimental code with no species stated",
        "the ability to resensitise the beta2-adrenergic\n      receptor, while suppressing AKAP5 in the same cells does not",
        "the ability to resensitise the beta2-adrenergic\n      receptor, while suppressing AKAP5 in the same cells does not [SPECIES-WORD-REMOVED]",
        None,  # control: the word "human" still appears elsewhere in that reason
    ),
]


def run_audit(target=None):
    """Run the audit, optionally against a mutated copy rather than the curated file."""
    cmd = ["uv", "run", "--quiet", "python", str(AUDIT)]
    if target is not None:
        cmd.append(str(target))
    return subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)


failures = []

base = run_audit()
if base.returncode != 0:
    raise SystemExit(
        f"BASELINE ALREADY FAILING - fix the document first:\n{base.stdout}{base.stderr}"
    )
print("baseline: audit passes\n")

original = (ROOT / REL).read_text()

with tempfile.TemporaryDirectory() as td:
    mutant_path = Path(td) / "AKAP12-ai-review.yaml"
    for name, old, new, expect in MUTATIONS:
        if old not in original:
            failures.append(f"{name}: ANCHOR NOT FOUND - mutation would have been a silent no-op")
            continue
        mutated = original.replace(old, new, 1)
        assert mutated != original, f"{name}: mutation produced no change"
        mutant_path.write_text(mutated)
        res = run_audit(mutant_path)
        out = res.stdout + res.stderr
        if expect is None:
            if res.returncode != 0:
                failures.append(f"{name}: CONTROL mutation tripped the audit:\n{out}")
            else:
                print(f"  control OK   : {name} (audit correctly stayed silent)")
        else:
            if res.returncode == 0:
                failures.append(f"{name}: audit PASSED a broken document")
            elif expect not in out:
                failures.append(
                    f"{name}: audit failed but not for the expected reason "
                    f"(wanted {expect!r})\n{out}"
                )
            else:
                print(f"  guard fires  : {name}")

# The curated file is never written by this script; assert that rather than assume it.
assert (ROOT / REL).read_text() == original, "the self-test modified the curated review file"
print("\ncurated file untouched (never written)")

if failures:
    print()
    for f in failures:
        print(f"SELF-TEST FAILURE: {f}")
    sys.exit(1)
print("self-test passed")
