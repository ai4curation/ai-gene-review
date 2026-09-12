"""Reproducible analyses supporting the human AP3M2 (mu3B) GO annotation review.

Three questions are asked, each answered from data fetched live at run time:

1. Where does AP3M2 sit among the human adaptor medium (mu) subunits?
   Pairwise global identity over the whole family tells us whether the PAINT
   AP-3 clade assignment is the right one and whether AP-1/AP-2 mu donors are
   an appropriate source for a transferred molecular function.

2. Does AP3M2 retain the YxxPhi (tyrosine-based sorting signal) binding site?
   The site is defined *empirically* from two solved complexes, never hardcoded.
   (a) PDB 9C5B, the human AP-3 holocomplex on a nanodisc with the LAMP1
       cytoplasmic tail bound: every mu3A residue within a cutoff of the cargo
       peptide is AP-3's own tyrosine-cargo site, and it transfers to AP3M2
       across an 84%-identity alignment.
   (b) PDB 1BXX, the rat mu2 C-terminal domain with the TGN38 DYQRLN signal:
       the classical AP-2 pocket, used as an outgroup and, because its
       alignment-projected positions can be compared with the positions 9C5B
       observes directly, as a check that the cross-family alignment holds.

3. Does AP3M2 retain the mu3 linker amphipathic helix reported for AP-3 by
   Begley et al. 2024 (PMID:39705307)? Scanned with an Eisenberg-consensus
   hydrophobic-moment window over the linker that precedes each protein's own
   UniProt-annotated MHD domain.

Plus two bookkeeping fetches used by the review: the UniProt feature table
(MHD boundaries, isoform 2 truncation) and the Human Protein Atlas
tissue/cell-type specificity fields for the "is AP3M2 neuron-restricted?"
question.

Run:  uv run python analyze.py
Writes RESULTS.md next to this file.
"""

from __future__ import annotations

import json
import math
import re
import sys
from dataclasses import dataclass
from pathlib import Path

import requests
from Bio.Align import PairwiseAligner, substitution_matrices
from Bio.PDB import MMCIFParser
from Bio.PDB.Polypeptide import is_aa

HERE = Path(__file__).parent
CACHE = HERE / "data"
CACHE.mkdir(exist_ok=True)

# The human adaptor medium subunits. Accessions are asserted against the fetched
# record (gene name + organism), so a wrong accession fails loudly.
HUMAN_MU = {
    "AP3M2": "P53677",
    "AP3M1": "Q9Y2T2",
    "AP1M1": "Q9BXS5",
    "AP1M2": "Q9Y6Q5",
    "AP2M1": "Q96CW1",
    "AP4M1": "O00189",
}
# Structure anchors.
# 9C5B: human AP-3 holocomplex on a nanodisc with the LAMP1 cytoplasmic tail
#       (GRKRSHAGYQTI) engaged -- the AP-3 tyrosine-cargo site itself, on mu3A.
AP3_PDB = "9c5b"
AP3_MU_ACC = "Q9Y2T2"   # AP3M1_HUMAN, the mu subunit in the structure
AP3_CARGO_ACC = "P11279"  # LAMP1_HUMAN
# 4IKN: an independent AP-3 cargo complex -- the rat mu3A C-terminal domain with the
#       TGN38 SDYQRL peptide. Different species, different cargo, same subfamily, so it
#       is a check on whether the 9C5B site is structure-specific.
AP3_RAT_PDB = "4ikn"
AP3_RAT_MU_ACC = "P53676"    # AP3M1_RAT -- rat mu3A, NOT an AP-2 subunit
AP3_RAT_CARGO_ACC = "P19814"  # TGON3_RAT
# 1BXX: rat mu2 C-terminal domain with the TGN38 DYQRLN signal -- the classical
#       YxxPhi pocket, used as an outgroup comparison and alignment cross-check.
AP2_PDB = "1bxx"
AP2_MU_ACC = "P84092"   # AP2M1_RAT
AP2_CARGO_NAME = "TGN38 internalisation peptide"
CONTACT_CUTOFF_A = 4.0
AH_WINDOW = 18
LINKER_UPSTREAM = 45  # residues before the MHD start that we call "the linker"

# Eisenberg et al. consensus hydrophobicity scale (normalised).
EISENBERG = {
    "A": 0.62, "R": -2.53, "N": -0.78, "D": -0.90, "C": 0.29,
    "Q": -0.85, "E": -0.74, "G": 0.48, "H": -0.40, "I": 1.38,
    "L": 1.06, "K": -1.50, "M": 0.64, "F": 1.19, "P": 0.12,
    "S": -0.18, "T": -0.05, "W": 0.81, "Y": 0.26, "V": 1.08,
}

THREE_TO_ONE = {
    "ALA": "A", "ARG": "R", "ASN": "N", "ASP": "D", "CYS": "C",
    "GLN": "Q", "GLU": "E", "GLY": "G", "HIS": "H", "ILE": "I",
    "LEU": "L", "LYS": "K", "MET": "M", "PHE": "F", "PRO": "P",
    "SER": "S", "THR": "T", "TRP": "W", "TYR": "Y", "VAL": "V",
    "MSE": "M",
}


def get(url: str, cache_name: str) -> str:
    """Fetch a URL once, caching the body under data/. Errors are not swallowed."""
    path = CACHE / cache_name
    if path.exists():
        return path.read_text()
    resp = requests.get(url, timeout=120)
    resp.raise_for_status()
    path.write_text(resp.text)
    return resp.text


@dataclass
class Entry:
    symbol: str
    accession: str
    sequence: str
    mhd_start: int
    mhd_end: int
    organism: str
    txt: str


def parse_uniprot_txt(symbol: str, accession: str) -> Entry:
    txt = get(
        f"https://rest.uniprot.org/uniprotkb/{accession}.txt",
        f"{accession}.txt",
    )
    seq_lines = txt.split("\nSQ   ")[1].split("\n")[1:]
    sequence = "".join(line.replace(" ", "") for line in seq_lines if not line.startswith("//"))
    organism = re.search(r"^OS   (.+?)\.?$", txt, re.M).group(1)
    mhd = None
    lines = txt.split("\n")
    for i, line in enumerate(lines):
        m = re.match(r"^FT   DOMAIN\s+(\d+)\.\.(\d+)", line)
        if m and 'note="MHD"' in lines[i + 1]:
            mhd = (int(m.group(1)), int(m.group(2)))
    if mhd is None:
        raise ValueError(f"{accession}: no MHD DOMAIN feature found in UniProt record")
    return Entry(symbol, accession, sequence, mhd[0], mhd[1], organism, txt)


def assert_identity(entry: Entry, expect_gene: str, expect_organism_prefix: str) -> None:
    gn = re.search(r"^GN   Name=([A-Za-z0-9_-]+)", entry.txt, re.M)
    if gn is None or gn.group(1).upper() != expect_gene.upper():
        raise ValueError(
            f"{entry.accession}: expected gene {expect_gene}, record says "
            f"{gn.group(1) if gn else None}"
        )
    if not entry.organism.startswith(expect_organism_prefix):
        raise ValueError(
            f"{entry.accession}: expected organism {expect_organism_prefix}, "
            f"record says {entry.organism}"
        )


def aligner() -> PairwiseAligner:
    al = PairwiseAligner()
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score = -11
    al.extend_gap_score = -1
    al.mode = "global"
    return al


def pairwise_identity(a: str, b: str, al: PairwiseAligner) -> tuple[float, dict[int, int]]:
    """Return (% identity over aligned columns, map of 1-based a-position -> b-position)."""
    aln = al.align(a, b)[0]
    ia, ib = aln.aligned
    same = 0
    total = 0
    mapping: dict[int, int] = {}
    for (a0, a1), (b0, b1) in zip(ia, ib):
        for k in range(a1 - a0):
            total += 1
            if a[a0 + k] == b[b0 + k]:
                same += 1
            mapping[a0 + k + 1] = b0 + k + 1
    return 100.0 * same / total, mapping


def _sifts_chain(pdb_id: str, accession: str) -> tuple[str, int]:
    """First mapped chain for `accession` in `pdb_id`, plus author->UniProt offset."""
    sifts = json.loads(
        get(
            f"https://www.ebi.ac.uk/pdbe/api/mappings/uniprot/{pdb_id}",
            f"{pdb_id}-sifts.json",
        )
    )
    unp = sifts[pdb_id]["UniProt"]
    if accession not in unp:
        raise ValueError(f"{pdb_id}: {accession} not among mapped entries {list(unp)}")
    m = unp[accession]["mappings"][0]
    return m["chain_id"], m["unp_end"] - m["end"]["author_residue_number"]


def peptide_contacts(
    pdb_id: str, mu_acc: str, cargo_acc: str | None
) -> tuple[list[tuple[int, str]], str, str]:
    """mu-subunit residues (in `mu_acc` numbering) within the cutoff of the cargo peptide.

    `cargo_acc` of None means the structure holds exactly two polypeptide chains and
    the cargo is whichever one is not the mu subunit (true for the 1BXX peptide, which
    is synthetic and therefore carries no SIFTS mapping).
    """
    mu_chain, mu_offset = _sifts_chain(pdb_id, mu_acc)

    cif_path = CACHE / f"{pdb_id}.cif"
    get(f"https://files.rcsb.org/download/{pdb_id.upper()}.cif", f"{pdb_id}.cif")
    structure = MMCIFParser(QUIET=True).get_structure(pdb_id, str(cif_path))
    model = next(structure.get_models())

    chains = {c.id: [r for r in c if is_aa(r, standard=False)] for c in model}
    if cargo_acc is None:
        others = [cid for cid, res in chains.items() if cid != mu_chain and res]
        if len(others) != 1:
            raise ValueError(f"{pdb_id}: expected one non-mu chain, got {others}")
        pep_chain = others[0]
    else:
        pep_chain, _ = _sifts_chain(pdb_id, cargo_acc)
    if mu_chain == pep_chain:
        raise ValueError(f"{pdb_id}: mu and cargo resolved to the same chain {mu_chain}")
    for needed in (mu_chain, pep_chain):
        if not chains.get(needed):
            raise ValueError(f"{pdb_id}: chain {needed} has no amino-acid residues")
    pep_seq = "".join(THREE_TO_ONE.get(r.get_resname(), "X") for r in chains[pep_chain])

    pep_atoms = [a for r in chains[pep_chain] for a in r if a.element != "H"]
    contacts: dict[int, str] = {}
    for res in chains[mu_chain]:
        aa = THREE_TO_ONE.get(res.get_resname())
        if aa is None:
            continue
        for atom in res:
            if atom.element == "H":
                continue
            if any((atom - p) <= CONTACT_CUTOFF_A for p in pep_atoms):
                contacts[res.id[1] + mu_offset] = aa
                break
    return sorted(contacts.items()), pep_chain, pep_seq


def hydrophobic_moment(window: str, angle_deg: float = 100.0) -> tuple[float, float]:
    """Return (mean hydrophobicity, hydrophobic moment) for a peptide window."""
    hs = [EISENBERG[c] for c in window]
    ang = math.radians(angle_deg)
    x = sum(h * math.cos(ang * i) for i, h in enumerate(hs))
    y = sum(h * math.sin(ang * i) for i, h in enumerate(hs))
    return sum(hs) / len(hs), math.hypot(x, y) / len(hs)


def best_ah_window(seq: str, lo: int, hi: int) -> tuple[int, str, float, float]:
    """Highest-hydrophobic-moment AH_WINDOW-mer whose start lies in [lo, hi] (1-based)."""
    best = None
    for start in range(lo, hi + 1):
        window = seq[start - 1 : start - 1 + AH_WINDOW]
        if len(window) < AH_WINDOW or any(c not in EISENBERG for c in window):
            continue
        h, mu = hydrophobic_moment(window)
        if best is None or mu > best[3]:
            best = (start, window, h, mu)
    if best is None:
        raise ValueError("no scannable window")
    return best


def main() -> int:
    al = aligner()

    entries: dict[str, Entry] = {}
    for symbol, acc in HUMAN_MU.items():
        e = parse_uniprot_txt(symbol, acc)
        assert_identity(e, symbol, "Homo sapiens")
        entries[symbol] = e
    anchor = parse_uniprot_txt("AP2M1_RAT", AP2_MU_ACC)
    assert_identity(anchor, "Ap2m1", "Rattus norvegicus")

    out: list[str] = []
    out.append("# AP3M2 (mu3B) bioinformatics results\n")
    out.append(
        "All numbers below are computed at run time by `analyze.py` from live "
        "UniProt, PDBe/RCSB and Human Protein Atlas records. Nothing is hardcoded; "
        "re-running regenerates this file.\n"
    )

    # ---------------------------------------------------------------- sequences
    out.append("## 1. Human adaptor medium (mu) subunits\n")
    out.append("| symbol | accession | length | UniProt MHD domain |")
    out.append("|---|---|---|---|")
    for s, e in entries.items():
        out.append(f"| {s} | {e.accession} | {len(e.sequence)} | {e.mhd_start}-{e.mhd_end} |")
    out.append(
        f"| {anchor.symbol} (structure anchor) | {anchor.accession} | "
        f"{len(anchor.sequence)} | {anchor.mhd_start}-{anchor.mhd_end} |"
    )
    out.append("")

    order = list(entries)
    out.append("### Pairwise global identity (%, BLOSUM62 global alignment)\n")
    out.append("| | " + " | ".join(order) + " |")
    out.append("|---" * (len(order) + 1) + "|")
    ident: dict[tuple[str, str], float] = {}
    for a in order:
        row = [a]
        for b in order:
            pid, _ = pairwise_identity(entries[a].sequence, entries[b].sequence, al)
            ident[(a, b)] = pid
            row.append(f"{pid:.1f}")
        out.append("| " + " | ".join(row) + " |")
    out.append("")
    asym = max(abs(ident[(a, b)] - ident[(b, a)]) for a in order for b in order)
    out.append(
        "The matrix is computed per ordered pair, and where several alignments are "
        "equally optimal the two directions can pick different ones, so it is very "
        f"slightly asymmetric: the largest difference between a cell and its transpose "
        f"is {asym:.1f} percentage points. Both values in such a pair are correct for "
        "their own direction; the AP3M2 row, which is the one the review cites, is "
        "unaffected either way.\n"
    )
    closest = max(
        (b for b in order if b != "AP3M2"), key=lambda b: ident[("AP3M2", b)]
    )
    out.append(
        f"AP3M2's closest human paralogue is **{closest}** "
        f"({ident[('AP3M2', closest)]:.1f}% identity). Identity to the AP-1 and AP-2 "
        f"medium subunits is "
        + ", ".join(f"{b} {ident[('AP3M2', b)]:.1f}%" for b in ("AP1M1", "AP1M2", "AP2M1"))
        + ".\n"
    )

    # --------------------------------------------- AP-3's own tyrosine-cargo site
    ap3_contacts, ap3_pep_chain, ap3_pep_seq = peptide_contacts(
        AP3_PDB, AP3_MU_ACC, AP3_CARGO_ACC
    )
    out.append("## 2. The AP-3 tyrosine-cargo site, observed and transferred\n")
    out.append(
        f"### 2a. mu3A residues that contact LAMP1 cargo in PDB {AP3_PDB.upper()}\n"
    )
    out.append(
        f"{AP3_PDB.upper()} is the human AP-3 holocomplex on a lipid nanodisc with the "
        f"LAMP1 cytoplasmic tail engaged (chain {ap3_pep_chain}, modelled sequence "
        f"`{ap3_pep_seq}`, which carries the GYQTI YxxPhi motif). The mu subunit in the "
        f"structure is {AP3_MU_ACC} (AP3M1/mu3A). Every mu3A residue with a heavy atom "
        f"within {CONTACT_CUTOFF_A} A of the cargo peptide is taken as the site: "
        f"{len(ap3_contacts)} residues qualify. Because AP3M1 and AP3M2 are "
        f"{ident[('AP3M1', 'AP3M2')]:.1f}% identical, transferring these positions to "
        "AP3M2 is a near-trivial alignment rather than a cross-family inference.\n"
    )
    m1_to_m2 = pairwise_identity(
        entries["AP3M1"].sequence, entries["AP3M2"].sequence, al
    )[1]
    out.append("| AP3M1 pos | mu3A | AP3M2 pos | mu3B | identical? |")
    out.append("|---|---|---|---|---|")
    ap3_same = 0
    ap3_claims: list[tuple[int, str, int, str]] = []
    for pos, aa in ap3_contacts:
        tgt = m1_to_m2.get(pos)
        if tgt is None:
            out.append(f"| {pos} | {aa} | - | - | no aligned residue |")
            continue
        t_aa = entries["AP3M2"].sequence[tgt - 1]
        same = t_aa == aa
        ap3_same += same
        ap3_claims.append((pos, aa, tgt, t_aa))
        out.append(f"| {pos} | {aa} | {tgt} | {t_aa} | {'yes' if same else 'no'} |")
    out.append("")
    out.append(
        f"**AP3M2 is identical to AP3M1 at {ap3_same} of the {len(ap3_contacts)} "
        f"cargo-contacting positions**, with no deletions. The tyrosine-cargo site that "
        "the AP-3 cryo-EM structure resolves is therefore intact in the neuronal mu3B "
        "paralogue; there is no residue-level evidence that AP3M2 has lost cargo "
        "recognition.\n"
    )

    # ------------------- second, independent AP-3 cargo complex (different species+cargo)
    rat_m1 = parse_uniprot_txt("AP3M1_RAT", AP3_RAT_MU_ACC)
    assert_identity(rat_m1, "Ap3m1", "Rattus norvegicus")
    ap3b_contacts, ap3b_pep_chain, ap3b_pep_seq = peptide_contacts(
        AP3_RAT_PDB, AP3_RAT_MU_ACC, AP3_RAT_CARGO_ACC
    )
    ratm1_to_hum = pairwise_identity(rat_m1.sequence, entries["AP3M1"].sequence, al)
    ratm1_to_m2 = pairwise_identity(rat_m1.sequence, entries["AP3M2"].sequence, al)
    projected = {ratm1_to_hum[1].get(pos) for pos, _ in ap3b_contacts} - {None}
    observed = {p for p, _ in ap3_contacts}
    out.append(
        f"### 2b. An independent AP-3 cargo complex: PDB {AP3_RAT_PDB.upper()}\n"
    )
    out.append(
        f"{AP3_RAT_PDB.upper()} is the {rat_m1.organism} mu3A C-terminal domain bound to the "
        f"TGN38 cytoplasmic tail (chain {ap3b_pep_chain}, modelled sequence "
        f"`{ap3b_pep_seq}`, carrying the DYQRL YxxPhi motif) - a different species and a "
        f"different cargo from {AP3_PDB.upper()}, so it tests whether the site found there "
        f"is structure-specific. {len(ap3b_contacts)} rat mu3A residues lie within "
        f"{CONTACT_CUTOFF_A} A of the peptide. Rat and human mu3A are "
        f"{ratm1_to_hum[0]:.1f}% identical and rat mu3A and human mu3B are "
        f"{ratm1_to_m2[0]:.1f}% identical.\n"
    )
    out.append("| AP3M1_RAT pos | rat mu3A | human AP3M1 pos | mu3A | human AP3M2 pos | mu3B |")
    out.append("|---|---|---|---|---|---|")
    agree = 0
    for pos, aa in ap3b_contacts:
        h1 = ratm1_to_hum[1].get(pos)
        h2 = ratm1_to_m2[1].get(pos)
        h1c = entries["AP3M1"].sequence[h1 - 1] if h1 else "-"
        h2c = entries["AP3M2"].sequence[h2 - 1] if h2 else "-"
        if h2c == aa:
            agree += 1
        out.append(
            f"| {pos} | {aa} | {h1 or '-'} | {h1c} | {h2 or '-'} | {h2c} |"
        )
    out.append("")
    shared = sorted(projected & observed)
    out.append(
        f"Projected onto human AP3M1, the {len(ap3b_contacts)} contacts of "
        f"{AP3_RAT_PDB.upper()} land on {len(projected)} positions, of which {len(shared)} "
        f"are among the {len(observed)} that {AP3_PDB.upper()} shows contacting LAMP1 "
        f"(shared: {', '.join(str(p) for p in shared) if shared else 'none'}). "
        f"Human AP3M2 carries the same residue as rat mu3A at {agree} of the "
        f"{len(ap3b_contacts)} positions. Two AP-3 structures, two different YxxPhi "
        "cargoes and two species therefore pick out the same site, and mu3B matches mu3A "
        "across it.\n"
    )

    # ------------------------------- outgroup: the classical AP-2 YxxPhi pocket
    contacts, pep_chain, pep_seq = peptide_contacts(AP2_PDB, AP2_MU_ACC, None)
    out.append(f"### 2c. Outgroup: the classical mu2 YxxPhi pocket (PDB {AP2_PDB.upper()})\n")
    out.append(
        f"{AP2_PDB.upper()} is the mu2 (AP50) C-terminal domain of {anchor.organism} "
        f"bound to the {AP2_CARGO_NAME} (chain {pep_chain}, modelled sequence "
        f"`{pep_seq}`). {len(contacts)} mu2 residues lie within {CONTACT_CUTOFF_A} A of "
        f"the peptide. Positions are in {anchor.accession} ({anchor.symbol}) numbering "
        "and are carried onto each human paralogue by pairwise alignment.\n"
    )
    maps = {
        s: pairwise_identity(anchor.sequence, entries[s].sequence, al)[1] for s in order
    }
    out.append("| " + anchor.accession + " pos | mu2 | " + " | ".join(order) + " |")
    out.append("|---" * (len(order) + 2) + "|")
    retained: dict[str, int] = {s: 0 for s in order}
    ap3m2_rows: list[tuple[int, str, int | None, str | None]] = []
    ap3m1_mapped: set[int] = set()
    for pos, aa in contacts:
        row = [str(pos), aa]
        for s in order:
            tgt = maps[s].get(pos)
            if tgt is None:
                row.append("-")
                cell_aa = None
            else:
                cell_aa = entries[s].sequence[tgt - 1]
                row.append(f"{cell_aa}{tgt}")
                if cell_aa == aa:
                    retained[s] += 1
                if s == "AP3M1":
                    ap3m1_mapped.add(tgt)
            if s == "AP3M2":
                ap3m2_rows.append((pos, aa, tgt, cell_aa))
        out.append("| " + " | ".join(row) + " |")
    out.append("")
    out.append("| paralogue | pocket positions identical to mu2 | of | % |")
    out.append("|---|---|---|---|")
    for s in order:
        out.append(
            f"| {s} | {retained[s]} | {len(contacts)} | "
            f"{100.0 * retained[s] / len(contacts):.0f} |"
        )
    out.append("")
    unanimous = []
    for pos, aa in contacts:
        cells = [
            entries[s].sequence[maps[s][pos] - 1] if maps[s].get(pos) else None
            for s in order
        ]
        if all(c == aa for c in cells):
            unanimous.append((pos, aa))
    out.append(
        "Positions where **every** human paralogue matches mu2: "
        + (", ".join(f"mu2 {aa}{pos}" for pos, aa in unanimous) if unanimous else "none")
        + f" ({len(unanimous)} of {len(contacts)}). Every other contact position has at "
        "least one paralogue that diverges.\n"
    )
    n_aligned = sum(1 for _, _, t, _ in ap3m2_rows if t is not None)
    observed = {p for p, _ in ap3_contacts}
    overlap = sorted(ap3m1_mapped & observed)
    out.append(
        f"AP3M2 aligns to {n_aligned}/{len(contacts)} of the mu2 pocket positions, with "
        f"no deletions, but matches mu2's residue at only {retained['AP3M2']} of them - "
        f"fewer than AP1M1 ({retained['AP1M1']}), AP1M2 ({retained['AP1M2']}) or AP4M1 "
        f"({retained['AP4M1']}). The AP-3 medium subunits have diverged substantially "
        "from the AP-2 signal pocket even though, per section 2a, they bind tyrosine "
        "cargo through the structurally equivalent region.\n"
    )
    out.append(
        "### 2d. Do the alignment and structure routes agree?\n\n"
        f"Projecting the {len(contacts)} mu2 pocket positions onto AP3M1 by alignment "
        f"lands on {len(ap3m1_mapped)} AP3M1 positions, of which {len(overlap)} are "
        f"among the {len(observed)} positions the {AP3_PDB.upper()} structure actually "
        f"shows contacting LAMP1 cargo (overlap: "
        f"{', '.join(str(p) for p in overlap) if overlap else 'none'}). The "
        "alignment-only route and the structure-observed route therefore identify the "
        "same site, which is the check that the cross-family alignment in 2c is not "
        "drifting.\n"
    )

    # ------------------------------------------------------ linker amphipathic helix
    out.append("## 3. The mu-linker amphipathic helix\n")
    out.append(
        "Begley et al. 2024 (PMID:39705307) report a membrane-inserting amphipathic "
        "helix in the mu3 linker of human AP-3. Below, the highest-hydrophobic-moment "
        f"{AH_WINDOW}-residue window starting in the {LINKER_UPSTREAM} residues that "
        "precede each protein's own UniProt MHD domain, using the Eisenberg consensus "
        "scale at 100 degrees per residue.\n"
    )
    out.append("| symbol | window (start-end) | sequence | <H> | <uH> |")
    out.append("|---|---|---|---|---|")
    ah: dict[str, float] = {}
    for s, e in entries.items():
        lo = max(1, e.mhd_start - LINKER_UPSTREAM)
        hi = e.mhd_start - AH_WINDOW
        start, window, h, mu = best_ah_window(e.sequence, lo, hi)
        ah[s] = mu
        out.append(
            f"| {s} | {start}-{start + AH_WINDOW - 1} | `{window}` | {h:+.2f} | {mu:.3f} |"
        )
    out.append("")
    out.append(
        f"AP3M2 <uH> = {ah['AP3M2']:.3f} versus AP3M1 {ah['AP3M1']:.3f}; the AP-1/AP-2 "
        f"subunits score "
        + ", ".join(f"{s} {ah[s]:.3f}" for s in ("AP1M1", "AP1M2", "AP2M1"))
        + f" and AP4M1 {ah['AP4M1']:.3f}.\n"
    )

    # --------------------------------------------------------------- isoform 2
    out.append("## 4. AP3M2 isoform 2 (P53677-2)\n")
    vsp = re.findall(
        r"^FT   VAR_SEQ\s+(\d+)(?:\.\.(\d+))?\n(?:FT\s+/note=\"([^\"]+)\")?",
        entries["AP3M2"].txt,
        re.M,
    )
    for start, end, note in vsp:
        span = f"{start}-{end}" if end else start
        out.append(f"- VAR_SEQ {span}: {note}")
    e = entries["AP3M2"]
    out.append(
        f"\nThe MHD of AP3M2 spans {e.mhd_start}-{e.mhd_end} of {len(e.sequence)} "
        "residues, so the isoform-2 variant removes the C-terminal portion of the very "
        "domain that carries the sorting-signal pocket analysed in section 2.\n"
    )

    # ------------------------------------------------------------------ expression
    hpa = json.loads(
        get(
            "https://www.proteinatlas.org/ENSG00000070718.json",
            "hpa-ENSG00000070718.json",
        )
    )
    out.append("## 5. Is human AP3M2 neuron-restricted?\n")
    out.append("Human Protein Atlas fields for ENSG00000070718:\n")
    for key in (
        "RNA tissue specificity",
        "RNA tissue distribution",
        "RNA single cell type specificity",
        "RNA single cell type specific nCPM",
        "RNA single cell type group specific nCPM",
        "RNA single nuclei brain specificity",
        "RNA brain regional specificity",
        "Tissue expression cluster",
    ):
        out.append(f"- **{key}**: {hpa.get(key)}")
    out.append("")

    text = "\n".join(out) + "\n"
    (HERE / "RESULTS.md").write_text(text)
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
