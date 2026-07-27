#!/usr/bin/env python3
"""Assert every ancestry relation this review's argument leans on.

Rule from the campaign brief: FETCH the relation, never infer it from the label.
``regulates`` / ``positively_regulates`` do NOT subsume; only ``is_a`` / ``part_of``
do, so every check here restricts ``relations`` to those two.

Each entry in CLAIMS is (descendant, ancestor, expected_bool, why).
Exits non-zero if any claim is wrong.

Usage:
    uv run python genes/human/AFF3/AFF3-bioinformatics/term_relations.py
"""

from __future__ import annotations

import json
import urllib.parse
import urllib.request

UA = {"User-Agent": "ai-gene-review/AFF3 (cjmungall@lbl.gov)"}
ANC = "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/{ids}/ancestors?relations=is_a,part_of"

CLAIMS: list[tuple[str, str, bool, str]] = [
    ("GO:0006368", "GO:0006354", True,
     "MODIFY GO:0006354 -> GO:0006368 must be a DOWNWARD move (asserts strictly more)"),
    ("GO:0006355", "GO:0010468", True,
     "GO:0010468 is a redundant ancestor of the GO:0006355 IBA row"),
    ("GO:0007611", "GO:0050877", True,
     "both GO:0050877 donors' own experimental term is GO:0007611, i.e. BELOW the propagated term"),
    ("GO:0001764", "GO:0050877", False,
     "neuron migration is NOT a nervous system process: the GO:0050877 branch cannot carry AFF3's developmental role"),
    ("GO:0016607", "GO:0005654", True,
     "nuclear speck refines the existing nucleoplasm IDA rather than contradicting it"),
    ("GO:0045190", "GO:0002443", True,
     "isotype switching sits in the leukocyte-mediated immunity branch (sanity check on the CSR term)"),
    ("GO:0035116", "GO:0030326", True,
     "embryonic hindlimb morphogenesis is a child of embryonic limb morphogenesis"),
    ("GO:0003712", "GO:0140110", True,
     "transcription coregulator activity is a transcription regulator activity"),
    ("GO:0003700", "GO:0003712", False,
     "DNA-binding transcription factor activity and coregulator activity are SIBLINGS, not parent/child"),
    ("GO:0003712", "GO:0003700", False,
     "...and the converse also fails, so the two make different claims"),
    # MEASURED, and it refuted my first guess: GO:0030674's only ancestors are
    # GO:0003674 and GO:0060090. It is NOT under protein binding, so proposing it is
    # not "a more informative GO:0005515" -- it is a different branch (molecular
    # adaptor activity). Recorded because the wrong version of this claim was written
    # first and the guard is what caught it.
    ("GO:0030674", "GO:0005515", False,
     "protein-macromolecule adaptor activity is NOT under protein binding"),
    ("GO:0030674", "GO:0060090", True,
     "...it is under molecular adaptor activity, a separate branch of MF"),
    # RETRACTION, second one in this review. The GO:0006355 row's reason initially argued
    # that its donors "disagree in sign", reading GO:0032786 as belonging to the negative
    # branch by proximity to GO:0032785. It does not: GO:0032786 is POSITIVE regulation of
    # transcription elongation. So every signed donor on that row points the same way, and
    # the reason had to be rewritten to rest on the RECIPIENT's mixed output instead. The
    # claim is asserted here so the fact is machine-checked rather than eyeballed.
    ("GO:0032786", "GO:0045893", True,
     "GO:0032786 is in the POSITIVE branch: all signed donors on the GO:0006355 row agree"),
    ("GO:0032786", "GO:0045892", False,
     "...and it is NOT in the negative branch, which is what the retracted reason assumed"),
    ("GO:0045893", "GO:0006355", True,
     "the positive child is available and unused on this gene, so the unsigned parent must "
     "be justified by the recipient's own mixed output rather than by donor disagreement"),
    # Added after review round 1, which observed that the GO:0050877 reason cited AFF3's
    # human genetics as its grounding while the same review shows the developmental part of
    # that genetics is off-branch. Half right: the COGNITIVE part is on-branch. Checked so
    # the split can be stated precisely instead of lumped.
    ("GO:0050890", "GO:0050877", True,
     "cognition IS under nervous system process, so AFF3's intellectual-disability and "
     "language/education phenotypes are on-branch grounding"),
    ("GO:0007611", "GO:0050890", True,
     "...and the donors' learning-or-memory term sits under cognition, one step below it"),
    ("GO:0021795", "GO:0050877", False,
     "...whereas cerebral cortex cell migration is NOT, so the migration evidence is the "
     "off-branch half and belongs on the separate proposed row"),
    ("GO:0003711", "GO:0140110", True,
     "closes the sibling claim on the GO:0003711 NEW row: previously only the GO:0003712 "
     "leg was checked (reviewer point 4)"),
    # Round 2: the GO:0006355 reason said "GO:0045893, GO:0032786 and GO:0032968 were all
    # verified to sit under GO:0045893". GO:0032968 was not in this list at all, and
    # "GO:0045893 under GO:0045893" is vacuous. Both corrected: the third donor term is
    # checked here, and the prose now names only the two terms that are genuinely below.
    ("GO:0032968", "GO:0045893", True,
     "the third signed donor term is also POSITIVE, completing the claim the GO:0006355 "
     "reason makes"),
    # Round 3: the GO:0003711 NEW row's reason asserts that GO:0003711 and GO:0003712 are
    # SIBLINGS with neither ancestor closure containing the other. Only the shared-parent leg
    # was checked; the reciprocal non-containment pair was not, unlike the equivalent
    # GO:0003700/GO:0003712 pair above. Both directions now asserted.
    ("GO:0003711", "GO:0003712", False,
     "elongation factor activity is NOT under coregulator activity"),
    ("GO:0003712", "GO:0003711", False,
     "...nor the converse, so the two are genuinely siblings and the GO:0003711 NEW row adds "
     "a statement rather than refining the GO:0003712 IBA"),
]


def ancestors(term: str) -> set[str]:
    url = ANC.format(ids=urllib.parse.quote(term))
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as fh:
        d = json.load(fh)
    res = d["results"]
    if len(res) != 1:
        raise SystemExit(f"FATAL: expected 1 result for {term}, got {len(res)}")
    if res[0]["id"] != term:
        raise SystemExit(f"FATAL: asked for {term}, QuickGO returned {res[0]['id']}")
    return set(res[0].get("ancestors") or [])


def main() -> None:
    cache: dict[str, set[str]] = {}
    problems = []
    for desc, anc, expected, why in CLAIMS:
        if desc not in cache:
            cache[desc] = ancestors(desc)
        got = anc in cache[desc]
        ok = "OK " if got == expected else "FAIL"
        rel = "IS" if got else "is NOT"
        print(f"{ok}  {desc} {rel} a descendant of {anc}  (expected {expected})")
        print(f"      {why}")
        if got != expected:
            problems.append((desc, anc, expected, got))
    if problems:
        raise SystemExit(f"\n{len(problems)} ancestry claim(s) WRONG: {problems}")
    print(f"\nall {len(CLAIMS)} ancestry claims verified")


if __name__ == "__main__":
    main()
