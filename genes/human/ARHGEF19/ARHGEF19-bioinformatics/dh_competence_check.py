#!/usr/bin/env python3
"""Is the ARHGEF19 (WGEF / Ephexin-2) DH-PH module a competent Dbl-family GEF?

Run from this directory:  uv run python dh_competence_check.py

Nothing is hardcoded except identifiers and the two published residue claims that
this script exists to CHECK. Sequences come live from the UniProt REST API, the
Dbl-homology profile comes live from InterPro (Pfam PF00621), and the
GTPase-contact positions are computed live from the deposited coordinates of
PDB 1X86 (ARHGEF12/LARG DH-PH bound to RhoA) and 1LB1 (Dbs DH-PH bound to RhoA).

Design notes
------------
The point of the panel is that a DH-domain profile score, on its own, cannot tell
you whether a protein catalyses nucleotide exchange -- retained residues are not
evidence of activity, and divergence is not evidence of its absence. So the panel
carries BOTH directions:

  * positive comparators -- five Dbl-family GEFs that have BOTH a co-crystal
    structure with their Rho-family substrate AND measured exchange activity;
  * negative controls -- sequences that must NOT score as DH domains, including
    ARHGEF19's own isoform 2 (Q8IW93-2), whose 484-783 splice deletion removes
    the C-terminal third of the DH domain and all of PH and SH3.

A pass here is therefore only a statement about the *module*, and the review says
so: the question of whether ARHGEF19 actually exchanges nucleotide on RhoA is
settled by experiment (PMID:15485661, PMID:18256687, PMID:38714795), not by this
script.

Exit codes: 0 = every assertion held; 1 = a published residue claim or a control
expectation failed (that is a finding, not a crash); 2 = a fetched input was not
what was expected (tooling failure).
"""

from __future__ import annotations

import gzip
import io
import json
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path

import gemmi
import requests

HERE = Path(__file__).resolve().parent
CACHE = HERE / "cache"
UNIPROT = "https://rest.uniprot.org/uniprotkb/{acc}.fasta"
UNIPROT_ISOFORM = "https://rest.uniprot.org/uniprotkb/{acc}.fasta"
PFAM_HMM = "https://www.ebi.ac.uk/interpro/wwwapi//entry/pfam/{pfam}?annotation=hmm"
PDB_CIF = "https://files.rcsb.org/download/{pdb}.cif"

TARGET = "Q8IW93"  # ARHGEF19 / WGEF / Ephexin-2, human
TARGET_LEN = 802
# The DH-truncating splice isoform used as the internal negative control.
TRUNCATION_CONTROL = "Q8IW93-2"

# Published, load-bearing residue claims about the HUMAN protein that the review
# cites. Each is (position, expected residue, source, what it is).
RESIDUE_CLAIMS = [
    (
        295,
        "Y",
        "PMID:38714795",
        "conserved N-terminal inhibitory-domain tyrosine; "
        "hWGEF Y295E is reported autoinhibition-free "
        '("This particular tyrosine (Y353xWGEF/295hWGEF) of hWGEF is present in NID '
        'and locks the GEF by interacting with its DH domain")',
    ),
]

# The internal PDZ-binding motif (IPM) that Dvl2-PDZ engages, as published.
IPM_CLAIM = (349, 359, "GSTFSLWQDIP", "PMID:38714795")

# The 8YR7 construct fuses this WGEF peptide to the Dvl2 PDZ C-terminus; the
# deposited sequence ends with it. It must be a substring of the human protein.
PDB_8YR7_WGEF_PEPTIDE = "TFSLWQDIP"


@dataclass
class Member:
    acc: str
    label: str
    role: str  # target | paralog | positive | negative
    expect_dh: bool  # should Pfam PF00621 fire at the gathering threshold?
    expect_contacts: bool = True  # should it span the GTPase-contacting positions?
    note: str = ""
    seq: str = field(default="", repr=False)


PANEL: list[Member] = [
    Member(TARGET, "ARHGEF19 / WGEF / Ephexin-2 (human)", "target", True),
    # --- ephexin-family paralogues; the five UniProt accessions that GO_Central
    #     uses as IBA donors / co-members of PANTHER PTHR12845 ---
    Member("Q8N5V2", "NGEF / Ephexin-1 (human)", "paralog", True),
    Member("Q12774", "ARHGEF5 / Ephexin-3 / TIM (human)", "paralog", True),
    Member("Q5VV41", "ARHGEF16 / Ephexin-4 (human)", "paralog", True),
    Member("O94989", "ARHGEF15 / Ephexin-5 (human)", "paralog", True),
    Member("Q96DR7", "ARHGEF26 / SGEF (human)", "paralog", True),
    # --- positive comparators: co-crystal with substrate GTPase + measured
    #     exchange activity ---
    Member("Q9NZN5", "ARHGEF12 / LARG (human) [PDB 1X86 with RhoA]", "positive", True),
    Member("Q64096", "Dbs / Mcf2l (mouse) [PDB 1LB1 with RhoA]", "positive", True),
    Member("Q15811", "ITSN1 (human) [PDB 1KI1 with Cdc42]", "positive", True),
    Member("Q60610", "Tiam1 (mouse) [PDB 1FOE with Rac1]", "positive", True),
    Member("O75962", "TRIO (human) [PDB 2NZ8 with Rac1]", "positive", True),
    # --- negative controls ---
    Member(
        "Q8IW93-2",
        "ARHGEF19 isoform 2 (human) [484-783 deleted]",
        "negative",
        expect_dh=True,  # and that is the point -- see note
        expect_contacts=False,
        note="internal control. The splice deletion removes the C-terminal third "
        "of the DH domain plus all of PH and SH3, so this isoform cannot present "
        "an intact exchange surface -- yet PF00621 still fires on the surviving "
        "N-terminal half. The control is calibrating the PROFILE, not the protein: "
        "a DH hit is not evidence of exchange competence.",
    ),
    Member(
        "Q06187",
        "BTK (human)",
        "negative",
        expect_dh=False,
        expect_contacts=False,
        note="PH + SH3 + kinase, no DH domain: tests that the profile is not "
        "firing on PH/SH3 alone",
    ),
    Member(
        "P61586",
        "RHOA (human)",
        "negative",
        expect_dh=False,
        expect_contacts=False,
        note="the substrate, not a GEF",
    ),
]

# GEF-side contact positions are computed from these complexes at run time.
TEMPLATES = [
    # (pdb id, GEF accession, GEF auth chain, GTPase auth chain)
    ("1X86", "Q9NZN5", "A", "B"),
    ("1LB1", "Q64096", "A", "B"),
]
CONTACT_CUTOFF_A = 4.5


def fetch(url: str, name: str, binary: bool = False) -> bytes | str:
    CACHE.mkdir(exist_ok=True)
    path = CACHE / name
    if path.exists():
        return path.read_bytes() if binary else path.read_text()
    resp = requests.get(url, timeout=120, headers={"User-Agent": "aigr-arhgef19"})
    resp.raise_for_status()
    if binary:
        path.write_bytes(resp.content)
        return resp.content
    path.write_text(resp.text)
    return resp.text


def load_sequences() -> None:
    accs = [m.acc for m in PANEL]
    dupes = sorted({a for a in accs if accs.count(a) > 1})
    if dupes:
        fail_tooling(
            f"duplicate accession(s) in PANEL: {dupes}. FASTA names are the join "
            "key for hmmsearch and hmmalign, so a duplicate silently collapses "
            "two panel members into one row."
        )
    for m in PANEL:
        fasta = fetch(UNIPROT.format(acc=m.acc), f"{m.acc}.fasta")
        assert isinstance(fasta, str)
        lines = fasta.strip().splitlines()
        if not lines or not lines[0].startswith(">"):
            fail_tooling(f"UniProt returned no FASTA for {m.acc}")
        m.seq = "".join(lines[1:])
        if not m.seq:
            fail_tooling(f"empty sequence for {m.acc}")


def fail_tooling(msg: str) -> None:
    print(f"TOOLING FAILURE: {msg}", file=sys.stderr)
    sys.exit(2)


def get_hmm() -> Path:
    raw = fetch(PFAM_HMM.format(pfam="PF00621"), "PF00621.hmm.gz", binary=True)
    assert isinstance(raw, bytes)
    text = gzip.decompress(raw).decode()
    path = CACHE / "PF00621.hmm"
    path.write_text(text)
    return path


def run(cmd: list[str], stdin: str | None = None) -> str:
    proc = subprocess.run(
        cmd, input=stdin, capture_output=True, text=True, check=False
    )
    if proc.returncode != 0:
        fail_tooling(f"{cmd[0]} exited {proc.returncode}: {proc.stderr[:800]}")
    return proc.stdout


def panel_fasta() -> str:
    return "".join(f">{m.acc}\n{m.seq}\n" for m in PANEL)


def hmmsearch_domains(hmm: Path) -> dict[str, list[tuple[int, int, float, float]]]:
    """Return acc -> list of (ali_from, ali_to, bitscore, i-Evalue) using Pfam GA."""
    with tempfile.NamedTemporaryFile("w", suffix=".fa", delete=False) as fh:
        fh.write(panel_fasta())
        fa = fh.name
    out = run(["hmmsearch", "--cut_ga", "--domtblout", "/dev/stdout", "-o", "/dev/null", str(hmm), fa])
    hits: dict[str, list[tuple[int, int, float, float]]] = {}
    for line in out.splitlines():
        if line.startswith("#") or not line.strip():
            continue
        f = line.split()
        acc, ievalue, score = f[0], float(f[12]), float(f[13])
        ali_from, ali_to = int(f[17]), int(f[18])
        hits.setdefault(acc, []).append((ali_from, ali_to, score, ievalue))
    return hits


def is_aa(res: gemmi.Residue) -> bool:
    info = gemmi.find_tabulated_residue(res.name)
    return bool(info and info.is_amino_acid())


def read_cif(pdb: str) -> gemmi.Structure:
    raw = fetch(PDB_CIF.format(pdb=pdb), f"{pdb}.cif")
    assert isinstance(raw, str)
    st = gemmi.read_structure_string(raw, format=gemmi.CoorFormat.Mmcif)
    st.remove_alternative_conformations()
    st.remove_hydrogens()
    st.remove_waters()
    st.remove_ligands_and_waters()
    st.setup_entities()
    return st


def structural_contacts(pdb: str, gef_chain: str, gtpase_chain: str) -> set[int]:
    """auth_seq_id of GEF residues with a heavy atom within CONTACT_CUTOFF_A of the GTPase."""
    st = read_cif(pdb)
    model = st[0]
    names = [ch.name for ch in model]
    for want in (gef_chain, gtpase_chain):
        if want not in names:
            fail_tooling(f"{pdb}: chain {want} not present (chains: {names})")
    gtp_positions = [
        a.pos for r in model[gtpase_chain] if is_aa(r) for a in r
    ]
    if not gtp_positions:
        fail_tooling(f"{pdb}: no GTPase residues in chain {gtpase_chain}")
    contacts: set[int] = set()
    for res in model[gef_chain]:
        if not is_aa(res):
            continue
        for atom in res:
            if any(atom.pos.dist(p) <= CONTACT_CUTOFF_A for p in gtp_positions):
                contacts.add(res.seqid.num)
                break
    if not contacts:
        fail_tooling(f"{pdb}: no GEF-GTPase contacts found; check chain ids")
    return contacts


def check_auth_numbering(pdb: str, chain: str, acc: str, positions: set[int]) -> int:
    """Confirm the structure's auth numbering equals UniProt numbering.

    Returns the number of positions checked. Exits 2 if the residue types do not
    agree -- that would mean every mapped position downstream is meaningless.
    """
    seq = next(m.seq for m in PANEL if m.acc == acc)
    st = read_cif(pdb)
    ch = st[0][chain]
    checked = 0
    for res in ch:
        if not is_aa(res):
            continue
        n = res.seqid.num
        if n not in positions:
            continue
        if not 1 <= n <= len(seq):
            fail_tooling(f"{pdb}:{chain} residue {n} outside {acc} (len {len(seq)})")
        one = gemmi.find_tabulated_residue(res.name).one_letter_code.upper()
        if one != seq[n - 1]:
            fail_tooling(
                f"{pdb}:{chain} auth numbering does not match {acc}: "
                f"position {n} is {one} in the structure but {seq[n - 1]} in UniProt"
            )
        checked += 1
    if checked == 0:
        fail_tooling(f"{pdb}:{chain} matched none of the contact positions")
    return checked


def hmmalign_map(hmm: Path) -> dict[str, dict[int, tuple[int, str]]]:
    """Align the panel to PF00621; return acc -> {match_state: (seq_pos, residue)}.

    hmmalign emits Stockholm with match states as UPPERCASE / '-' columns and
    insert states as lowercase / '.'. Match-state index is therefore the running
    count of non-insert columns.
    """
    with tempfile.NamedTemporaryFile("w", suffix=".fa", delete=False) as fh:
        fh.write(panel_fasta())
        fa = fh.name
    sto = run(["hmmalign", "--amino", "--outformat", "Stockholm", str(hmm), fa])

    rows: dict[str, str] = {}
    for line in sto.splitlines():
        if not line or line.startswith("#") or line.startswith("//"):
            continue
        parts = line.split()
        if len(parts) != 2:
            continue
        rows.setdefault(parts[0], "")
        rows[parts[0]] += parts[1]

    if not rows:
        fail_tooling("hmmalign produced no aligned rows")

    width = {len(v) for v in rows.values()}
    if len(width) != 1:
        fail_tooling(f"ragged alignment: column counts {sorted(width)}")

    # A column is a match column iff it is not an insert column. hmmalign marks
    # inserts as lowercase letters or '.'; match/delete as uppercase or '-'.
    ncols = width.pop()
    is_match_col = []
    for c in range(ncols):
        col = [rows[k][c] for k in rows]
        insert = all(ch == "." or ch.islower() for ch in col)
        is_match_col.append(not insert)

    out: dict[str, dict[int, tuple[int, str]]] = {}
    for acc, row in rows.items():
        seq_pos = 0
        match_state = 0
        mapping: dict[int, tuple[int, str]] = {}
        for c, ch in enumerate(row):
            if ch not in ".-":
                seq_pos += 1
            if is_match_col[c]:
                match_state += 1
                if ch not in ".-":
                    mapping[match_state] = (seq_pos, ch.upper())
        out[acc] = mapping
    return out


def main() -> int:
    failures: list[str] = []

    print("# ARHGEF19 DH-PH competence check")
    print()
    load_sequences()

    target = next(m for m in PANEL if m.acc == TARGET)
    if len(target.seq) != TARGET_LEN:
        fail_tooling(
            f"{TARGET} is {len(target.seq)} aa, expected {TARGET_LEN}; "
            "UniProt sequence has changed, re-check every position below"
        )

    # ---- Test 1: published residue claims about the human protein -------------
    print("## Test 1 - published residue claims about human ARHGEF19 (Q8IW93)")
    print()
    for pos, expected, src, what in RESIDUE_CLAIMS:
        got = target.seq[pos - 1]
        ok = got == expected
        print(f"- {src}: position {pos} expected {expected}, found {got} -> "
              f"{'MATCH' if ok else 'MISMATCH'}  ({what})")
        if not ok:
            failures.append(f"residue claim {src} {expected}{pos} -> found {got}")

    lo, hi, expected_ipm, src = IPM_CLAIM
    got_ipm = target.seq[lo - 1 : hi]
    ok = got_ipm == expected_ipm
    print(f"- {src}: internal PDZ-binding motif {lo}-{hi} expected {expected_ipm}, "
          f"found {got_ipm} -> {'MATCH' if ok else 'MISMATCH'}")
    if not ok:
        failures.append(f"IPM {lo}-{hi} -> {got_ipm}")

    idx = target.seq.find(PDB_8YR7_WGEF_PEPTIDE)
    print(f"- PDB 8YR7 fused WGEF peptide {PDB_8YR7_WGEF_PEPTIDE!r} occurs at "
          f"{idx + 1 if idx >= 0 else 'NOT FOUND'} "
          f"({'unique' if target.seq.count(PDB_8YR7_WGEF_PEPTIDE) == 1 else 'NOT UNIQUE'})")
    if idx < 0 or target.seq.count(PDB_8YR7_WGEF_PEPTIDE) != 1:
        failures.append("8YR7 peptide not uniquely located in Q8IW93")
    print()

    # ---- Test 2: does each panel member carry a DH domain? --------------------
    hmm = get_hmm()
    hits = hmmsearch_domains(hmm)
    print("## Test 2 - Pfam PF00621 (RhoGEF / Dbl homology) at the gathering threshold")
    print()
    print("| role | protein | DH domain (envelope) | bitscore | expected | result |")
    print("|---|---|---|---|---|---|")
    for m in PANEL:
        got = hits.get(m.acc, [])
        best = max(got, key=lambda t: t[2]) if got else None
        span = f"{best[0]}-{best[1]}" if best else "none"
        score = f"{best[2]:.1f}" if best else "-"
        has_dh = best is not None
        ok = has_dh == m.expect_dh
        print(f"| {m.role} | {m.label} | {span} | {score} | "
              f"{'DH' if m.expect_dh else 'no DH'} | {'OK' if ok else 'UNEXPECTED'} |")
        if not ok:
            failures.append(f"PF00621 expectation failed for {m.acc} ({m.label})")
    print()

    # ---- Test 3: GTPase-contacting DH positions, mapped onto the panel --------
    print("## Test 3 - DH residues that contact the GTPase in solved complexes")
    print()
    mapping = hmmalign_map(hmm)

    template_states: dict[str, list[int]] = {}
    for pdb, acc, gef_chain, gtp_chain in TEMPLATES:
        contacts = structural_contacts(pdb, gef_chain, gtp_chain)
        checked = check_auth_numbering(pdb, gef_chain, acc, contacts)
        dh_span = max(hits[acc], key=lambda t: t[2])
        in_dh = {p for p in contacts if dh_span[0] <= p <= dh_span[1]}
        rev = {pos: st for st, (pos, _) in mapping[acc].items()}
        states = sorted({rev[p] for p in in_dh if p in rev})
        template_states[pdb] = states
        print(f"- {pdb} ({acc}, chain {gef_chain} vs {gtp_chain}): "
              f"{len(contacts)} contact residues within {CONTACT_CUTOFF_A} A, "
              f"{len(in_dh)} inside the DH envelope {dh_span[0]}-{dh_span[1]}, "
              f"{len(states)} map to PF00621 match states "
              f"(auth numbering verified against {acc} at {checked} positions)")
    print()

    shared = sorted(set(template_states["1X86"]) & set(template_states["1LB1"]))
    print(f"Match states contacting RhoA in BOTH RhoA complexes: {len(shared)}")
    print()
    if len(shared) < 5:
        fail_tooling(
            f"only {len(shared)} shared contact states; the two templates should "
            "agree on far more than that"
        )

    scored = [m for m in PANEL if m.acc in hits]
    larg = mapping["Q9NZN5"]
    identical_to_larg: dict[str, int] = {m.acc: 0 for m in scored}
    present: dict[str, int] = {m.acc: 0 for m in scored}

    print("| match state | " + " | ".join(m.acc for m in scored) + " |")
    print("|" + "---|" * (1 + len(scored)))
    for st in shared:
        cells = []
        for m in scored:
            got = mapping[m.acc].get(st)
            if got is None:
                cells.append("-")
                continue
            present[m.acc] += 1
            cells.append(f"{got[1]}{got[0]}")
            if larg.get(st) and got[1] == larg[st][1]:
                identical_to_larg[m.acc] += 1
        print(f"| {st} | " + " | ".join(cells) + " |")
    print()

    print(f"| role | protein | contact positions spanned / {len(shared)} | "
          "identical to LARG | % identical |")
    print("|---|---|---|---|---|")
    for m in scored:
        pct = 100.0 * identical_to_larg[m.acc] / len(shared)
        print(f"| {m.role} | {m.label} | {present[m.acc]}/{len(shared)} | "
              f"{identical_to_larg[m.acc]} | {pct:.0f}% |")
    print()

    # ---- Test 4: the target has to behave like the verified-active panel, and
    #      the truncation control has to behave like a truncation ---------------
    print("## Test 4 - control expectations on contact-position coverage")
    print()
    positives = [m for m in scored if m.role == "positive"]
    floor = min(present[m.acc] for m in positives)
    print(f"Threshold is taken from the data, not chosen: the weakest of the "
          f"{len(positives)} verified-active comparators spans {floor}/{len(shared)} "
          "contact positions.")
    if floor < 0.8 * len(shared):
        fail_tooling(
            f"the verified-active comparators only reach {floor}/{len(shared)}; "
            "the comparator panel or the alignment is broken, so no conclusion "
            "about the target can be drawn from it"
        )
    checks = [
        (
            "target spans at least as many contact positions as the weakest "
            "verified-active comparator",
            present[TARGET] >= floor,
            f"ARHGEF19 {present[TARGET]}/{len(shared)} vs floor {floor}",
        ),
        (
            "truncation control spans fewer than that floor",
            present[TRUNCATION_CONTROL] < floor,
            f"{TRUNCATION_CONTROL} {present[TRUNCATION_CONTROL]}/{len(shared)} "
            f"vs floor {floor}",
        ),
        (
            "truncation control spans fewer than full-length ARHGEF19",
            present[TRUNCATION_CONTROL] < present[TARGET],
            f"{present[TRUNCATION_CONTROL]} vs {present[TARGET]}",
        ),
    ]
    for desc, ok, detail in checks:
        print(f"- [{'OK' if ok else 'UNEXPECTED'}] {desc} ({detail})")
        if not ok:
            failures.append(f"{desc} -- {detail}")
    print()
    print("Every DH-containing panel member and its coverage, for the record:")
    for m in scored:
        print(f"- {m.role}: {m.label} -- {present[m.acc]}/{len(shared)}")
    print()

    if failures:
        print("## FAILURES")
        for f in failures:
            print(f"- {f}")
        return 1
    print("All assertions held.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
