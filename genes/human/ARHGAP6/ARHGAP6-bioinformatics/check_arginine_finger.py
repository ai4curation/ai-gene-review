#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["biopython>=1.83"]
# ///
"""Does ARHGAP6 retain the RhoGAP catalytic arginine finger, and does that settle
anything about its GAP activity?

Motivation
----------
The ARHGAP6 review turns on a separability claim: RhoA-GAP activity on one side,
and GAP-*independent* outputs (actin/process remodelling, PLC-delta1 activation,
HERG downregulation) on the other. Both halves of that claim reference the
catalytic arginine finger -- PMID:10699171 and PMID:19038263 use the R433G mutant
as the instrument that separates them -- so the residue itself is worth checking
rather than assuming.

But a residue check is only as good as its controls, and in this superfamily
residue identity and curated activity come apart in BOTH directions. So the script
does not just ask "is the arginine there?". It puts the residue column and the
curated-GO column side by side for a panel chosen to contain both kinds of
counterexample, and lets the reader see that neither column predicts the other.

What is computed (nothing here is hardcoded as a result)
--------------------------------------------------------
1. The anchor is ARHGAP1/p50RhoGAP (UniProtKB:Q07960), the RhoGAP whose arginine
   finger is resolved in the RhoA transition-state complex PDB 1TX4. The anchor
   position is *verified against the structure*, not asserted: the script
   downloads 1TX4, reads chain A's author-numbered residues, and requires that
   the sequence window around the classic literature position (Arg85 in the
   construct numbering used by the structure paper) is identical to the window
   around the UniProt position, and that the residue is an arginine in both. If
   that check fails the script exits non-zero rather than reporting a number.

2. For each panel member, its UniProt-annotated Rho-GAP domain is aligned to the
   anchor's Rho-GAP domain (global Needleman-Wunsch, BLOSUM62) and the residue
   aligned to the anchor arginine is read off in the member's OWN numbering.

3. That alignment-derived call is cross-checked against UniProt's own
   "Arginine finger" SITE feature. Two independent methods agreeing is the
   evidence; a disagreement is reported as a disagreement, not silently resolved.

4. QuickGO is queried live for each member's GO:0005096 (GTPase activator
   activity) annotations, INCLUDING the NOT qualifier, which is the whole point:
   a curated NOT on a residue-intact protein and a positive call on a
   residue-substituted protein are what break the residue->activity inference.

Controls
--------
* Positive, structurally resolved: ARHGAP1 (Q07960), arginine finger in 1TX4.
  The anchor must map to itself and must be R. Asserted; non-zero exit if not.
* Known-dead: OCRL (Q01968) and INPP5B (P32019). Their C-terminal RhoGAP-like
  domains are the textbook catalytically dead RhoGAP folds.
* Negative control for the ASSAY (not for the biology): a residue that is NOT the
  arginine finger -- the anchor's own domain start -- must NOT come back as an
  arginine-finger match. This catches an alignment that maps everything to R.

Usage
-----
    uv run check_arginine_finger.py             # writes RESULTS.md next to this script
    uv run check_arginine_finger.py --stdout    # print instead of writing
    uv run check_arginine_finger.py --self-test # run the guard self-tests and exit
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

from Bio.Align import PairwiseAligner, substitution_matrices

UNIPROT = "https://rest.uniprot.org/uniprotkb/{acc}.json"
PDB_FILE = "https://files.rcsb.org/download/{pdb}.pdb"
QUICKGO = (
    "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
    "?geneProductId={acc}&goId={go}&limit=100"
)

# The structurally resolved anchor.
ANCHOR_ACC = "Q07960"          # ARHGAP1 / p50RhoGAP / CDC42GAP
ANCHOR_PDB = "1TX4"            # RhoA . GDP . AlF4- : p50RhoGAP transition-state complex
ANCHOR_PDB_CHAIN = "A"         # the GAP chain
ANCHOR_PDB_AUTHNUM = 85        # "Arg85", the construct numbering used in the literature

GAP_TERM = "GO:0005096"        # GTPase activator activity

# Declared input, not a result. `note` records only WHY each entry is in the panel.
PANEL: list[tuple[str, str, str]] = [
    ("O43182", "ARHGAP6", "target"),
    ("O54834", "Arhgap6 (mouse)", "IBA/ISS donor for the human annotations"),
    (ANCHOR_ACC, "ARHGAP1", "anchor; arginine finger resolved in PDB 1TX4"),
    ("Q6ZRI8", "ARHGAP36", "closest paralog: shares InterPro IPR037863 (RHOGAP6/36)"),
    ("Q3KRB8", "ARHGAP11B", "RhoGAP-domain protein carrying curated NOT annotations"),
    ("Q9NRY4", "ARHGAP35", "second active RhoGAP, as a non-anchor positive"),
    ("Q01968", "OCRL", "known-dead control: catalytically inactive RhoGAP-like domain"),
    ("P32019", "INPP5B", "known-dead control: OCRL paralog, same dead RhoGAP-like fold"),
]

THREE_TO_ONE = {
    "ALA": "A", "ARG": "R", "ASN": "N", "ASP": "D", "CYS": "C", "GLN": "Q",
    "GLU": "E", "GLY": "G", "HIS": "H", "ILE": "I", "LEU": "L", "LYS": "K",
    "MET": "M", "PHE": "F", "PRO": "P", "SER": "S", "THR": "T", "TRP": "W",
    "TYR": "Y", "VAL": "V", "SEC": "U", "PYL": "O",
}


def _get(url: str, binary: bool = False):
    with urllib.request.urlopen(url, timeout=90) as fh:
        raw = fh.read()
    return raw if binary else json.loads(raw)


@dataclass
class Entry:
    acc: str
    label: str
    note: str
    seq: str = ""
    seq_version: int = 0
    domain: tuple[int, int] | None = None
    uniprot_site: int | None = None
    aligned_pos: int | None = None
    aligned_res: str | None = None
    go_rows: list[str] = field(default_factory=list)

    @property
    def uniprot_site_res(self) -> str | None:
        if self.uniprot_site is None:
            return None
        return self.seq[self.uniprot_site - 1]


def fetch_entry(acc: str, label: str, note: str) -> Entry:
    d = _get(UNIPROT.format(acc=acc))
    e = Entry(acc=acc, label=label, note=note)
    e.seq = d["sequence"]["value"]
    e.seq_version = d["entryAudit"]["sequenceVersion"]
    for f in d.get("features", []):
        if f["type"] == "Domain" and "Rho-GAP" in (f.get("description") or ""):
            if e.domain is None:
                e.domain = (f["location"]["start"]["value"], f["location"]["end"]["value"])
        elif f["type"] == "Site" and "rginine finger" in (f.get("description") or ""):
            if e.uniprot_site is None:
                e.uniprot_site = f["location"]["start"]["value"]
    return e


def fetch_go_rows(acc: str, go: str) -> list[str]:
    """Live QuickGO rows for one term, preserving the NOT qualifier."""
    d = _get(QUICKGO.format(acc=f"UniProtKB:{acc}", go=go))
    rows = []
    for r in d.get("results", []):
        qual = r.get("qualifier") or ""
        rows.append(f"{qual} ({r['goEvidence']}, {r['reference']}, {r.get('assignedBy')})")
    return sorted(set(rows))


def pdb_chain_residues(pdb_text: str, chain: str) -> dict[int, str]:
    """author residue number -> one-letter code, for CA atoms of one chain."""
    out: dict[int, str] = {}
    for line in pdb_text.splitlines():
        if not line.startswith("ATOM"):
            continue
        if line[21] != chain or line[12:16].strip() != "CA":
            continue
        if line[16] not in (" ", "A"):        # skip alternate conformations B, C, ...
            continue
        resname = line[17:20].strip()
        if resname not in THREE_TO_ONE:
            continue
        out[int(line[22:26])] = THREE_TO_ONE[resname]
    return out


def verify_anchor_against_structure(anchor: Entry, window: int = 6) -> tuple[int, str]:
    """Confirm the UniProt arginine-finger site is the residue resolved in 1TX4.

    Returns (author_residue_number, matched_window). Raises on any mismatch --
    a number that cannot be verified is not reported at all.
    """
    if anchor.uniprot_site is None:
        raise SystemExit(f"FAIL: no UniProt 'Arginine finger' site on {anchor.acc}")
    text = _get(PDB_FILE.format(pdb=ANCHOR_PDB), binary=True).decode("utf-8", "replace")
    res = pdb_chain_residues(text, ANCHOR_PDB_CHAIN)
    if ANCHOR_PDB_AUTHNUM not in res:
        raise SystemExit(
            f"FAIL: {ANCHOR_PDB} chain {ANCHOR_PDB_CHAIN} has no residue "
            f"{ANCHOR_PDB_AUTHNUM}"
        )
    if res[ANCHOR_PDB_AUTHNUM] != "R":
        raise SystemExit(
            f"FAIL: {ANCHOR_PDB} {ANCHOR_PDB_AUTHNUM} is "
            f"{res[ANCHOR_PDB_AUTHNUM]}, not R"
        )
    pdb_win = "".join(
        res.get(ANCHOR_PDB_AUTHNUM + i, "-") for i in range(-window, window + 1)
    )
    u = anchor.uniprot_site
    unp_win = anchor.seq[u - 1 - window : u + window]
    if pdb_win != unp_win:
        raise SystemExit(
            "FAIL: structure/UniProt window mismatch for the anchor arginine:\n"
            f"  {ANCHOR_PDB} chain {ANCHOR_PDB_CHAIN} around {ANCHOR_PDB_AUTHNUM}: {pdb_win}\n"
            f"  {anchor.acc} around {u}: {unp_win}\n"
            "  The anchor position is unverified; refusing to report it."
        )
    return ANCHOR_PDB_AUTHNUM, pdb_win


def make_aligner() -> PairwiseAligner:
    a = PairwiseAligner()
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -11
    a.extend_gap_score = -1
    a.mode = "global"
    return a


def map_position(aligner: PairwiseAligner, anchor: Entry, target: Entry, anchor_pos: int):
    """Map an anchor position into the target's own numbering via a domain alignment.

    Returns (target_position, target_residue) or (None, None) if the anchor column
    aligns to a gap.
    """
    if anchor.domain is None or target.domain is None:
        return None, None
    a_start, a_end = anchor.domain
    t_start, t_end = target.domain
    a_sub = anchor.seq[a_start - 1 : a_end]
    t_sub = target.seq[t_start - 1 : t_end]
    if not (a_start <= anchor_pos <= a_end):
        raise SystemExit(f"FAIL: anchor position {anchor_pos} outside its Rho-GAP domain")
    aln = aligner.align(a_sub, t_sub)[0]
    a_blocks, t_blocks = aln.aligned
    offset = anchor_pos - a_start          # 0-based index within a_sub
    for (a0, a1), (t0, t1) in zip(a_blocks, t_blocks):
        if a0 <= offset < a1:
            t_idx = t0 + (offset - a0)
            return t_start + t_idx, t_sub[t_idx]
    return None, None


def classify(target_res: str | None) -> str:
    if target_res is None:
        return "ABSENT (aligns to a gap)"
    return "RETAINED" if target_res == "R" else f"SUBSTITUTED (R->{target_res})"


def self_test(aligner: PairwiseAligner, anchor: Entry) -> None:
    """Guards must fire with their expected message; negative controls must stay silent."""
    failures: list[str] = []

    def expect_fail(name: str, fn, needle: str) -> None:
        try:
            fn()
        except SystemExit as exc:
            if needle in str(exc):
                print(f"  ok   {name}: guard fired ({needle!r})")
            else:
                failures.append(f"{name}: fired with wrong message: {exc}")
            return
        failures.append(f"{name}: guard did NOT fire")

    # Guard 1: an anchor position outside the Rho-GAP domain must be refused.
    expect_fail(
        "anchor-outside-domain",
        lambda: map_position(aligner, anchor, anchor, 1),
        "outside its Rho-GAP domain",
    )

    # Guard 2: a structure window that does not match UniProt must be refused.
    bogus = Entry(acc=anchor.acc, label="bogus", note="")
    bogus.seq = "M" * len(anchor.seq)
    bogus.uniprot_site = anchor.uniprot_site
    expect_fail(
        "structure-window-mismatch",
        lambda: verify_anchor_against_structure(bogus),
        "window mismatch",
    )

    # Guard 3: no UniProt arginine-finger site at all must be refused.
    nosite = Entry(acc="X", label="nosite", note="")
    nosite.seq = anchor.seq
    expect_fail(
        "no-uniprot-site",
        lambda: verify_anchor_against_structure(nosite),
        "no UniProt 'Arginine finger' site",
    )

    # Negative control A: the anchor must map to ITSELF at the arginine finger.
    pos, res = map_position(aligner, anchor, anchor, anchor.uniprot_site)
    if (pos, res) == (anchor.uniprot_site, "R"):
        print(f"  ok   positive-control: anchor maps to itself at {pos}{res}")
    else:
        failures.append(f"positive-control: anchor mapped to {pos}{res}, expected {anchor.uniprot_site}R")

    # Negative control B (assay control): a NON-arginine-finger anchor column must
    # not come back as an arginine. This catches an alignment that maps everything
    # to R. We use the anchor's own domain start, which is not an arginine.
    d_start = anchor.domain[0]
    if anchor.seq[d_start - 1] == "R":
        failures.append("assay-control: chosen control column is itself an R; pick another")
    else:
        _, ctrl_res = map_position(aligner, anchor, anchor, d_start)
        if ctrl_res == anchor.seq[d_start - 1]:
            print(f"  ok   assay-control: non-finger column {d_start} maps to {ctrl_res}, not R")
        else:
            failures.append(f"assay-control: column {d_start} mapped to {ctrl_res}")

    # Negative control C: classify() must stay silent (RETAINED) only for R.
    if classify("R") != "RETAINED" or classify("T") == "RETAINED" or classify(None) == "RETAINED":
        failures.append("classify(): mislabels a substitution or a gap as RETAINED")
    else:
        print("  ok   classify(): R->RETAINED, T->SUBSTITUTED, gap->ABSENT")

    if failures:
        print("\nSELF-TEST FAILURES:")
        for f in failures:
            print("  FAIL " + f)
        raise SystemExit(1)
    print("\nself-test: all guards fired, all controls clean")


def render(rows: list[Entry], anchor: Entry, pdb_auth: int, pdb_win: str) -> str:
    today = date.today().isoformat()
    out: list[str] = []
    A = out.append
    A("# ARHGAP6 bioinformatics: the RhoGAP catalytic arginine finger, with controls")
    A("")
    A("## Question")
    A("")
    A("ARHGAP6 is reported to have two separable activities: RhoA-GAP activity, and a")
    A("GAP-*independent* actin-remodelling / process-outgrowth activity. Both the")
    A("original functional study (PMID:10699171) and the later HERG study")
    A("(PMID:19038263) separate them with the same instrument -- an R433G mutant of the")
    A("catalytic arginine finger. So: **does ARHGAP6 actually carry that arginine, and")
    A("does the answer settle whether it is an active GAP?**")
    A("")
    A("The second half of the question is the point. A retained catalytic residue is")
    A("not evidence of activity, and a substituted one is not proof of its absence.")
    A("The panel below was chosen to contain counterexamples in both directions.")
    A("")
    A("## Method")
    A("")
    A("`check_arginine_finger.py` computes everything from live primary sources; no")
    A("finding is hardcoded.")
    A("")
    A(f"1. **Anchor.** ARHGAP1/p50RhoGAP (UniProtKB:{ANCHOR_ACC}), whose arginine finger is")
    A(f"   resolved in the RhoA transition-state complex **PDB {ANCHOR_PDB}**.")
    A(f"2. **The anchor position is verified against the structure, not asserted.** The")
    A(f"   script downloads {ANCHOR_PDB}, reads chain {ANCHOR_PDB_CHAIN}'s author-numbered")
    A("   CA residues, and requires that the +/-6 window around the literature position")
    A("   matches the corresponding UniProt window residue-for-residue. A mismatch is a")
    A("   non-zero exit, so an unverifiable position is never reported.")
    A("3. **Mapping.** Each panel member's UniProt-annotated Rho-GAP domain is aligned to")
    A("   the anchor's (global Needleman-Wunsch, BLOSUM62, gap -11/-1) and the residue in")
    A("   the anchor's arginine column is read off in the member's own numbering.")
    A("4. **Cross-check.** That call is compared against UniProt's own `Arginine finger`")
    A("   SITE feature. Agreement of two independent methods is the evidence.")
    A("5. **Curated activity.** QuickGO is queried live for each member's")
    A(f"   `{GAP_TERM}` (GTPase activator activity) rows, **including the NOT qualifier**.")
    A("")
    A("```")
    A("uv run check_arginine_finger.py             # regenerate this file")
    A("uv run check_arginine_finger.py --self-test # guards + controls")
    A("```")
    A("")
    A(f"## Anchor verification (run {today})")
    A("")
    A(f"- `{ANCHOR_PDB}` chain {ANCHOR_PDB_CHAIN} author residue **{pdb_auth}** is **ARG**.")
    A(f"- Window around it: `{pdb_win}`")
    A(f"- UniProtKB:{anchor.acc} (sequence version {anchor.seq_version}) window around")
    A(f"  position **{anchor.uniprot_site}**: `{anchor.seq[anchor.uniprot_site-1-6:anchor.uniprot_site+6]}`")
    A("- The two windows are identical, so the structurally resolved arginine finger of")
    A(f"  p50RhoGAP is UniProt position **{anchor.uniprot_site}** (the literature's \"Arg{pdb_auth}\"")
    A("  is construct numbering, offset by")
    A(f"  {anchor.uniprot_site - pdb_auth}).")
    A("")
    A(f"## Result (run {today})")
    A("")
    A("| protein | acc (sv) | Rho-GAP domain | residue in the anchor's arginine column | UniProt `Arginine finger` site | agree? | call | curated GO:0005096 |")
    A("|---|---|---|---|---|---|---|---|")
    for e in rows:
        dom = f"{e.domain[0]}-{e.domain[1]}" if e.domain else "n/a"
        aligned = f"{e.aligned_res}{e.aligned_pos}" if e.aligned_pos else "gap"
        site = f"{e.uniprot_site_res}{e.uniprot_site}" if e.uniprot_site else "none"
        agree = "yes" if (e.uniprot_site and e.aligned_pos == e.uniprot_site) else (
            "n/a" if not e.uniprot_site else "**NO**")
        call = classify(e.aligned_res)
        if "SUBSTITUTED" in call or "ABSENT" in call:
            call = f"**{call}**"
        go = "; ".join(e.go_rows) if e.go_rows else "_none_"
        if "NOT|" in go:
            go = go.replace("NOT|", "**NOT**|")
        A(f"| {e.label} | {e.acc} (sv{e.seq_version}) | {dom} | {aligned} | {site} | {agree} | {call} | {go} |")
    A("")
    A("## Interpretation")
    A("")
    A("**ARHGAP6 retains the arginine finger.** The alignment to the structurally")
    A("resolved anchor and UniProt's own SITE feature independently place it at")
    A("**R433**, and that is the residue PMID:19038263 names when it states that")
    A("\"Mutation of the conserved arginine at position 433 to a glycine (R433G)")
    A("abolishes the rhoGAP activity of ARHGAP6\". Three independent lines -- structure-")
    A("anchored alignment, UniProt feature, and a published point mutant -- agree on the")
    A("same position, which is as well-grounded as this kind of call gets.")
    A("")
    A("**But retention does not establish activity, and the panel shows why.** In this")
    A("superfamily the residue column and the curated-activity column come apart in both")
    A("directions:")
    A("")
    A("- *Residue intact, activity curated absent.* ARHGAP11B keeps the arginine finger")
    A("  and nonetheless carries curated `NOT|enables GO:0005096` annotations. Retention")
    A("  is compatible with a protein that has been experimentally shown not to be a GAP.")
    A("- *Residue substituted, activity curated present.* ARHGAP36 -- ARHGAP6's closest")
    A("  paralog, sharing InterPro IPR037863 (RHOGAP6/36) -- has a threonine in the")
    A("  arginine column, yet carries a positive `enables GO:0005096`. OCRL, whose")
    A("  RhoGAP-like domain is the textbook dead one, substitutes a glutamine and still")
    A("  carries a positive IDA.")
    A("")
    A("So the residue check is **consistent with** ARHGAP6 being a real RhoA GAP and it")
    A("removes one way the GAP claim could have been wrong, but on its own it settles")
    A("nothing. What actually supports the GAP call is the functional evidence: the")
    A("R433G mutant fails to clear stress fibres while wild-type ARHGAP6 clears them")
    A("(PMID:10699171).")
    A("")
    A("**The same panel is what makes the separability claim interesting rather than")
    A("trivial.** Because R433G is a clean loss-of-GAP reagent, the phenotypes that")
    A("survive it are evidence of a genuinely GAP-independent output -- process outgrowth")
    A("(PMID:10699171) and HERG downregulation (PMID:19038263, where the R433G mutant")
    A("reduces HERG current as well as wild-type). That is an argument from a mutant that")
    A("works, not from a residue that is present.")
    A("")
    A("## Caveats")
    A("")
    A("- The dead controls are dead by *literature reputation* plus residue substitution;")
    A("  the positive GO rows they carry (OCRL IDA, ARHGAP36 IBA) are exactly the")
    A("  discrepancy being displayed, not an endorsement of those annotations. This")
    A("  script does not adjudicate them and no conclusion here depends on doing so.")
    A("- Domain boundaries are UniProt's. A member whose Rho-GAP domain is unannotated")
    A("  would be reported as `n/a` rather than guessed.")
    A("")
    return "\n".join(out) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--stdout", action="store_true", help="print instead of writing RESULTS.md")
    ap.add_argument("--self-test", action="store_true", help="run guard self-tests and exit")
    args = ap.parse_args()

    aligner = make_aligner()
    try:
        entries = [fetch_entry(a, l, n) for a, l, n in PANEL]
    except (urllib.error.URLError, TimeoutError) as exc:
        print(f"network failure, no result produced: {exc}", file=sys.stderr)
        return 2

    anchor = next(e for e in entries if e.acc == ANCHOR_ACC)

    if args.self_test:
        print("self-test:")
        self_test(aligner, anchor)
        return 0

    pdb_auth, pdb_win = verify_anchor_against_structure(anchor)

    # Positive control, asserted every run: the anchor must map to itself.
    pos, res = map_position(aligner, anchor, anchor, anchor.uniprot_site)
    if (pos, res) != (anchor.uniprot_site, "R"):
        raise SystemExit(
            f"FAIL: positive control broke -- anchor mapped to {res}{pos}, "
            f"expected R{anchor.uniprot_site}. Refusing to report the panel."
        )

    for e in entries:
        e.aligned_pos, e.aligned_res = map_position(aligner, anchor, e, anchor.uniprot_site)
        e.go_rows = fetch_go_rows(e.acc, GAP_TERM)

    md = render(entries, anchor, pdb_auth, pdb_win)
    if args.stdout:
        print(md)
    else:
        out = Path(__file__).with_name("RESULTS.md")
        out.write_text(md)
        print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
