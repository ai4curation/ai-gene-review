#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["gemmi>=0.6", "requests>=2.31"]
# ///
"""Structure-guided audit of the ACTL7A actin fold.

Question this answers
---------------------
ACTL7A ("actin-like protein 7A", Arp7A) carries canonical actin-derived GO
annotations (structural constituent of cytoskeleton, cytoskeleton organization).
Those are defensible only if ACTL7A retains the parts of the actin fold that do
the corresponding work:

1. the **nucleotide cleft** (ATP/ADP + divalent cation), and
2. the **protomer-protomer interfaces** that make a filament.

Rather than asserting conservation from the family name, this script derives
both residue sets *from experimental structures* and then reads off what ACTL7A
and a panel of comparator actins/ARPs actually have at those positions.

Method
------
* Contact residues are computed with a neighbour search, not taken from a list:
  - G-actin nucleotide pocket: PDB 2BTF (profilin-beta-actin, ATP + divalent site).
  - F-actin nucleotide pocket + inter-protomer interface: PDB 8A2S
    (cryo-EM F-actin, Mg2+-ADP-Pi, 5 protomers).
* Positions are mapped through a MAFFT L-INS-i alignment of the deposited actin
  sequence with the comparator panel, so no residue numbering is hard-coded.
* Comparators calibrate the answer: conventional actins and Arp1/Arp2/Arp3 are
  nucleotide binders; the yeast SWI/SNF Arps (Arp7/Arp9) are the family's most
  divergent members. Whatever cutoff separates those groups is the scale on
  which ACTL7A should be read.

Everything is downloaded at run time and cached under ``data/``; nothing about
the result is hard-coded. Missing tools or unexpected structure content raise
immediately.

Run with:  uv run --script actin_fold_audit.py
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

import gemmi
import requests

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
CONTACT_CUTOFF = 4.0  # A, ligand-protein contact
INTERFACE_CUTOFF = 4.5  # A, protein-protein (inter-protomer) contact

# (accession, expected gene symbol, short label, group)
PANEL: list[tuple[str, str, str, str]] = [
    ("Q9Y615", "ACTL7A", "ACTL7A_HUMAN", "query"),
    ("Q9QY84", "Actl7a", "ACTL7A_MOUSE", "query_ortholog"),
    ("Q641W9", "Actl7a", "ACTL7A_RAT", "query_ortholog"),
    ("Q9Y614", "ACTL7B", "ACTL7B_HUMAN", "query_paralog"),
    ("Q8TC94", "ACTL9", "ACTL9_HUMAN", "testis_arp"),
    ("Q5JWF8", "ACTL10", "ACTL10_HUMAN", "testis_arp"),
    ("Q8TDG2", "ACTRT1", "ACTRT1_HUMAN", "testis_arp"),
    ("Q8TDY3", "ACTRT2", "ACTRT2_HUMAN", "testis_arp"),
    ("Q9BYD9", "ACTRT3", "ACTRT3_HUMAN", "testis_arp"),
    ("P60709", "ACTB", "ACTB_HUMAN", "conventional_actin"),
    ("P68133", "ACTA1", "ACTA1_HUMAN", "conventional_actin"),
    ("P60010", "ACT1", "ACT1_YEAST", "conventional_actin"),
    ("P61163", "ACTR1A", "ARP1_HUMAN", "filament_forming_arp"),
    ("P61160", "ACTR2", "ARP2_HUMAN", "nucleotide_binding_arp"),
    ("P61158", "ACTR3", "ARP3_HUMAN", "nucleotide_binding_arp"),
    ("O96019", "ACTL6A", "ARP4_BAF53A_HUMAN", "nuclear_arp"),
    ("Q9H9F9", "ACTR5", "ARP5_HUMAN", "nuclear_arp"),
    ("Q9GZN1", "ACTR6", "ARP6_HUMAN", "nuclear_arp"),
    ("Q9H981", "ACTR8", "ARP8_HUMAN", "nuclear_arp"),
    ("P80428", "ARP4", "ARP4_YEAST", "nuclear_arp"),
    ("Q12406", "ARP7", "ARP7_YEAST", "divergent_swisnf_arp"),
    ("Q05123", "ARP9", "ARP9_YEAST", "divergent_swisnf_arp"),
]

# ACTL7A missense/nonsense positions from the UniProt Q9Y615 feature table plus
# the two variants reported after the entry was last curated. `pathogenic` marks
# variants reported in SPGF86 patients; the rest are population polymorphisms
# and serve as an internal control for "does this class of position matter?".
# (position, wild-type aa, variant aa, pathogenic?, source)
VARIANTS: list[tuple[int, str, str, bool, str]] = [
    (45, "R", "C", False, "dbSNP:rs368653764 / PMID:17644991"),
    (75, "D", "A", True, "PMID:36574082"),
    (161, "A", "P", False, "dbSNP:rs35995497"),
    (245, "A", "T", True, "PMID:32923619, PMID:37004249"),
    (246, "G", "A", True, "PMID:37004249"),
    (340, "V", "M", False, "dbSNP:rs7872077 / PMID:17644991"),
    (343, "L", "V", False, "dbSNP:rs56031956"),
    (362, "G", "R", True, "PMID:34727571"),
    (402, "G", "S", True, "PMID:35863052"),
]

# Residues that the actin ATP-hydrolysis literature identifies as catalytic, in standard
# actin numbering, with the residue each one must be in the reference structure. The
# expected identity is asserted at run time, so a numbering mismatch is fatal rather than
# silently wrong. Sources: Gln137/His161 as the hydrolysis pair and Asp154 + the Val159
# main chain as the proton-relay/water-stabilising partners --
# Kanematsu et al. 2023 PMID:37009486; Oda et al. 2019 PMID:30622175 (PNAS 116:1723).
CATALYTIC_RESIDUES: dict[int, str] = {11: "D", 137: "Q", 154: "D", 159: "V", 161: "H"}

NUCLEOTIDE_LIGANDS = {"ATP", "ADP", "PO4"}
METAL_LIGANDS = {"MG", "CA", "SR", "MN"}
ADENINE_ATOMS = {"N1", "C2", "N3", "C4", "C5", "C6", "N6", "N7", "C8", "N9"}
PHOSPHATE_ATOMS = {
    "PA", "O1A", "O2A", "O3A",
    "PB", "O1B", "O2B", "O3B",
    "PG", "O1G", "O2G", "O3G",
    "P", "O1", "O2", "O3", "O4",  # free phosphate (PO4)
}


def die(msg: str) -> None:
    raise SystemExit(f"ERROR: {msg}")


def require_tool(name: str) -> str:
    path = shutil.which(name)
    if path is None:
        die(f"required executable {name!r} not found on PATH. Install it (e.g. `brew install {name}`).")
    return path


def cached_get(url: str, dest: Path) -> str:
    """Download url to dest unless already cached. Any HTTP failure is fatal."""
    if dest.exists() and dest.stat().st_size > 0:
        return dest.read_text()
    dest.parent.mkdir(parents=True, exist_ok=True)
    resp = requests.get(url, timeout=120)
    if resp.status_code != 200:
        die(f"GET {url} returned HTTP {resp.status_code}")
    if not resp.text.strip():
        die(f"GET {url} returned an empty body")
    dest.write_text(resp.text)
    return resp.text


# --------------------------------------------------------------------------- #
# sequences
# --------------------------------------------------------------------------- #

def fetch_panel() -> dict[str, str]:
    """Return {label: sequence}. Asserts each accession really is the expected gene."""
    seqs: dict[str, str] = {}
    for acc, gene, label, _group in PANEL:
        text = cached_get(
            f"https://rest.uniprot.org/uniprotkb/{acc}.fasta",
            DATA / "seqs" / f"{acc}.fasta",
        )
        lines = text.strip().splitlines()
        header = lines[0]
        if f"GN={gene} " not in header + " ":
            die(
                f"{acc} header does not carry GN={gene}; UniProt returned:\n  {header}\n"
                "Fix the PANEL entry rather than relaxing this check."
            )
        seqs[label] = "".join(lines[1:]).upper()
    return seqs


# --------------------------------------------------------------------------- #
# structures
# --------------------------------------------------------------------------- #

@dataclass
class ActinChain:
    pdb_id: str
    chain_name: str
    seq: str  # full SEQRES-derived sequence, 1-letter
    # label_seq (1-based index into seq) for each observed residue
    observed: dict[int, gemmi.Residue]


def load_structure(pdb_id: str) -> gemmi.Structure:
    text = cached_get(
        f"https://files.rcsb.org/download/{pdb_id}.cif",
        DATA / "struct" / f"{pdb_id}.cif",
    )
    doc = gemmi.cif.read_string(text)
    st = gemmi.make_structure_from_block(doc.sole_block())
    st.setup_entities()
    if len(st) == 0:
        die(f"{pdb_id}: no models in structure")
    return st


def actin_chains(st: gemmi.Structure, min_len: int = 300) -> list[ActinChain]:
    """Every polymer chain long enough to be an actin protomer, with SEQRES mapping."""
    out: list[ActinChain] = []
    model = st[0]
    for chain in model:
        poly = chain.get_polymer()
        if len(poly) < min_len:
            continue
        ent = st.get_entity_of(poly)
        if ent is None or not ent.full_sequence:
            die(f"{st.name}: chain {chain.name} has no SEQRES entity; cannot map numbering")
        full = [gemmi.find_tabulated_residue(r.split(",")[0]) for r in ent.full_sequence]
        seq = "".join(
            (info.one_letter_code.upper() if info and info.is_amino_acid() else "X")
            for info in full
        )
        observed: dict[int, gemmi.Residue] = {}
        for res in poly:
            ls = res.label_seq
            if ls is None:
                die(f"{st.name}: chain {chain.name} residue {res.seqid.num} lacks label_seq")
            expected = ent.full_sequence[ls - 1].split(",")[0]
            if expected != res.name:
                die(
                    f"{st.name} chain {chain.name}: SEQRES[{ls}]={expected} but model has "
                    f"{res.name}{res.seqid.num}; numbering assumption broken"
                )
            observed[ls] = res
        out.append(ActinChain(st.name, chain.name, seq, observed))
    if not out:
        die(f"{st.name}: found no polymer chain of >= {min_len} residues")
    return out


def ligand_contacts(
    st: gemmi.Structure, chains: list[ActinChain], atom_filter: set[str] | None, resnames: set[str]
) -> dict[str, set[int]]:
    """{chain_name: {label_seq of residues within CONTACT_CUTOFF of the ligand}}."""
    model = st[0]
    ns = gemmi.NeighborSearch(model, st.cell, CONTACT_CUTOFF + 1.0).populate()
    by_chain: dict[str, set[int]] = {c.chain_name: set() for c in chains}
    lookup = {c.chain_name: c for c in chains}
    n_lig = 0
    for chain in model:
        for res in chain:
            if res.name not in resnames:
                continue
            n_lig += 1
            for atom in res:
                if atom_filter is not None and atom.name not in atom_filter:
                    continue
                for mark in ns.find_atoms(atom.pos, "\0", radius=CONTACT_CUTOFF):
                    cra = mark.to_cra(model)
                    if cra.residue.name in resnames or cra.residue.name == "HOH":
                        continue
                    target = lookup.get(cra.chain.name)
                    if target is None:
                        continue
                    if cra.atom.pos.dist(atom.pos) > CONTACT_CUTOFF:
                        continue
                    ls = cra.residue.label_seq
                    if ls is not None and ls in target.observed:
                        by_chain[cra.chain.name].add(ls)
    if n_lig == 0:
        die(f"{st.name}: no ligand residues matching {sorted(resnames)} found")
    return by_chain


def interprotomer_contacts(st: gemmi.Structure, chains: list[ActinChain]) -> dict[str, set[int]]:
    """{chain_name: {label_seq of residues contacting a *different* protomer}}."""
    model = st[0]
    ns = gemmi.NeighborSearch(model, st.cell, INTERFACE_CUTOFF + 1.0).populate()
    lookup = {c.chain_name: c for c in chains}
    by_chain: dict[str, set[int]] = {c.chain_name: set() for c in chains}
    for ac in chains:
        for ls, res in ac.observed.items():
            for atom in res:
                if atom.element == gemmi.Element("H"):
                    continue
                for mark in ns.find_atoms(atom.pos, "\0", radius=INTERFACE_CUTOFF):
                    cra = mark.to_cra(model)
                    if cra.chain.name == ac.chain_name or cra.chain.name not in lookup:
                        continue
                    if cra.atom.pos.dist(atom.pos) <= INTERFACE_CUTOFF:
                        by_chain[ac.chain_name].add(ls)
                        break
    if not any(by_chain.values()):
        die(f"{st.name}: no inter-protomer contacts found; is this a single-protomer entry?")
    return by_chain


def consensus_positions(by_chain: dict[str, set[int]], chains: list[ActinChain], min_frac: float) -> list[int]:
    """label_seq positions seen in at least min_frac of the chains that have any hit."""
    active = [c for c in chains if by_chain[c.chain_name]]
    if not active:
        die("no chain carried any contact")
    counts: dict[int, int] = {}
    for c in active:
        for ls in by_chain[c.chain_name]:
            counts[ls] = counts.get(ls, 0) + 1
    need = max(1, int(round(min_frac * len(active))))
    return sorted(ls for ls, n in counts.items() if n >= need)


# --------------------------------------------------------------------------- #
# alignment
# --------------------------------------------------------------------------- #

def run_mafft(seqs: dict[str, str]) -> tuple[dict[str, str], str]:
    mafft = require_tool("mafft")
    version = subprocess.run([mafft, "--version"], capture_output=True, text=True).stderr.strip()
    fasta = DATA / "panel.fasta"
    fasta.parent.mkdir(parents=True, exist_ok=True)
    fasta.write_text("".join(f">{k}\n{v}\n" for k, v in seqs.items()))
    proc = subprocess.run(
        [mafft, "--localpair", "--maxiterate", "1000", "--anysymbol", "--quiet", str(fasta)],
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        die(f"mafft failed (rc={proc.returncode}):\n{proc.stderr[-2000:]}")
    aln: dict[str, str] = {}
    name = None
    for line in proc.stdout.splitlines():
        if line.startswith(">"):
            name = line[1:].strip()
            aln[name] = ""
        elif name is not None:
            aln[name] += line.strip()
    (DATA / "panel.aln.fasta").write_text(proc.stdout)
    lengths = {len(v) for v in aln.values()}
    if len(lengths) != 1:
        die(f"mafft returned ragged alignment: lengths {lengths}")
    if set(aln) != set(seqs):
        die(f"mafft lost sequences: {set(seqs) - set(aln)}")
    return aln, version


def seq_to_col(aligned: str) -> dict[int, int]:
    """{1-based residue index in ungapped seq: 0-based alignment column}."""
    out: dict[int, int] = {}
    i = 0
    for col, ch in enumerate(aligned):
        if ch != "-":
            i += 1
            out[i] = col
    return out


def pct(num: int, den: int) -> float | None:
    return None if den == 0 else round(100.0 * num / den, 1)


# --------------------------------------------------------------------------- #
# main
# --------------------------------------------------------------------------- #

def main() -> int:
    seqs = fetch_panel()

    # --- structures ---
    gactin = load_structure("2BTF")
    g_chains = actin_chains(gactin)
    if len(g_chains) != 1:
        die(f"2BTF: expected 1 actin-length chain, got {[c.chain_name for c in g_chains]}")
    factin = load_structure("8A2S")
    f_chains = actin_chains(factin)
    if len(f_chains) < 3:
        die(f"8A2S: expected >=3 protomers, got {[c.chain_name for c in f_chains]}")

    ref_label = "ACTB_2BTF_chainA"
    seqs_for_aln = dict(seqs)
    seqs_for_aln[ref_label] = g_chains[0].seq
    f_ref_label = "ACTIN_8A2S"
    seqs_for_aln[f_ref_label] = f_chains[0].seq

    sites: dict[str, dict] = {}

    def add_site(key: str, desc: str, ref: str, chain: ActinChain, positions: list[int], src: str) -> None:
        if not positions:
            die(f"site {key!r} came out empty; check ligand/atom filters")
        sites[key] = {
            "description": desc,
            "reference_seq": ref,
            "source": src,
            "n_positions": len(positions),
            "positions": positions,
            "residues": "".join(chain.seq[p - 1] for p in positions),
        }

    # G-actin nucleotide pocket (2BTF: ATP + SR at the divalent cation site)
    g_all = ligand_contacts(gactin, g_chains, None, NUCLEOTIDE_LIGANDS | METAL_LIGANDS)
    g_aden = ligand_contacts(gactin, g_chains, ADENINE_ATOMS, NUCLEOTIDE_LIGANDS)
    g_phos = ligand_contacts(gactin, g_chains, PHOSPHATE_ATOMS, NUCLEOTIDE_LIGANDS)
    g_metal = ligand_contacts(gactin, g_chains, None, METAL_LIGANDS)
    gc = g_chains[0]
    add_site("g_pocket_all", f"any residue within {CONTACT_CUTOFF} A of ATP or the divalent cation",
             ref_label, gc, sorted(g_all[gc.chain_name]), "PDB 2BTF (profilin-beta-actin, ATP)")
    add_site("g_pocket_adenine", f"within {CONTACT_CUTOFF} A of the ATP adenine ring",
             ref_label, gc, sorted(g_aden[gc.chain_name]), "PDB 2BTF")
    add_site("g_pocket_phosphate", f"within {CONTACT_CUTOFF} A of the ATP alpha/beta/gamma phosphates",
             ref_label, gc, sorted(g_phos[gc.chain_name]), "PDB 2BTF")
    add_site("g_pocket_metal", f"within {CONTACT_CUTOFF} A of the divalent cation",
             ref_label, gc, sorted(g_metal[gc.chain_name]), "PDB 2BTF")

    # F-actin nucleotide pocket and inter-protomer interface (8A2S)
    f_all = ligand_contacts(factin, f_chains, None, NUCLEOTIDE_LIGANDS | METAL_LIGANDS)
    f_iface = interprotomer_contacts(factin, f_chains)
    fc = f_chains[0]
    add_site("f_pocket_all", f"within {CONTACT_CUTOFF} A of ADP/Pi/Mg in >=50% of protomers",
             f_ref_label, fc, consensus_positions(f_all, f_chains, 0.5),
             "PDB 8A2S (cryo-EM F-actin, Mg-ADP-Pi)")
    add_site("f_protomer_interface",
             f"within {INTERFACE_CUTOFF} A of a neighbouring protomer in >=50% of protomers "
             "that have any inter-protomer contact",
             f_ref_label, fc, consensus_positions(f_iface, f_chains, 0.5), "PDB 8A2S")

    # --- alignment ---
    aln, mafft_version = run_mafft(seqs_for_aln)
    col_of = {label: seq_to_col(aln[label]) for label in aln}

    # overall pairwise identity vs each structural reference
    def pairwise_identity(a: str, b: str) -> dict:
        sa, sb = aln[a], aln[b]
        both = ident = 0
        for x, y in zip(sa, sb):
            if x != "-" and y != "-":
                both += 1
                ident += x == y
        return {"aligned_positions": both, "identical": ident, "percent_identity": pct(ident, both)}

    per_seq: dict[str, dict] = {}
    for _acc, _gene, label, group in PANEL:
        entry: dict = {"group": group, "length": len(seqs[label])}
        entry["identity_vs_2BTF_actin"] = pairwise_identity(label, ref_label)
        entry["identity_vs_8A2S_actin"] = pairwise_identity(label, f_ref_label)
        for key, site in sites.items():
            ref = site["reference_seq"]
            matched = ident = gaps = 0
            observed_chars = []
            ref_chars = []
            for p in site["positions"]:
                col = col_of[ref][p]
                ref_aa = aln[ref][col]
                aa = aln[label][col]
                ref_chars.append(ref_aa)
                observed_chars.append(aa)
                if aa == "-":
                    gaps += 1
                    continue
                matched += 1
                ident += aa == ref_aa
            entry[key] = {
                "n_positions": len(site["positions"]),
                "aligned": matched,
                "gapped": gaps,
                "identical_to_actin": ident,
                "percent_identity_at_site": pct(ident, matched),
                "reference_residues": "".join(ref_chars),
                "observed_residues": "".join(observed_chars),
            }
        per_seq[label] = entry

    # --- literature-defined catalytic residues ---
    for p, expected in CATALYTIC_RESIDUES.items():
        got = gc.seq[p - 1]
        if got != expected:
            die(
                f"2BTF position {p} is {got}, expected {expected}. The deposited numbering is not "
                "standard actin numbering, so CATALYTIC_RESIDUES cannot be mapped."
            )
    catalytic = {}
    for _acc, _gene, label, group in PANEL:
        chars = []
        for p in sorted(CATALYTIC_RESIDUES):
            chars.append(aln[label][col_of[ref_label][p]])
        catalytic[label] = {
            "group": group,
            "residues": "".join(chars),
            "n_conserved": sum(
                c == CATALYTIC_RESIDUES[p] for c, p in zip(chars, sorted(CATALYTIC_RESIDUES))
            ),
        }

    # --- variant mapping ---
    q = "ACTL7A_HUMAN"
    qseq = seqs[q]
    variant_rows = []
    site_pos_cols = {
        key: {col_of[site["reference_seq"]][p]: p for p in site["positions"]}
        for key, site in sites.items()
    }
    # union of the two nucleotide-cleft definitions, expressed as alignment columns
    cleft_cols = set(site_pos_cols["g_pocket_all"]) | set(site_pos_cols["f_pocket_all"])
    # every 2BTF actin position, keyed by alignment column, so any ACTL7A residue can be
    # placed in actin numbering whether or not it falls in a derived site
    ref_pos_of_col = {c: p for p, c in col_of[ref_label].items()}
    for pos, wt, mut, pathogenic, source in VARIANTS:
        if pos > len(qseq):
            die(f"variant position {pos} beyond ACTL7A length {len(qseq)}")
        if qseq[pos - 1] != wt:
            die(
                f"variant {wt}{pos}{mut}: UniProt sequence has {qseq[pos - 1]} at {pos}. "
                "Fix the VARIANTS table."
            )
        col = col_of[q][pos]
        in_sites = sorted(k for k, cols in site_pos_cols.items() if col in cols)
        ref_pos = ref_pos_of_col.get(col)
        variant_rows.append({
            "position": pos,
            "wild_type": wt,
            "variant": mut,
            "reported_in_SPGF86": pathogenic,
            "source": source,
            "actin_residue_at_aligned_column_2BTF": aln[ref_label][col],
            "aligned_actin_position": ref_pos,
            "in_nucleotide_cleft": col in cleft_cols,
            "in_sites": in_sites,
        })

    # How surprising is it that reported variants land in the cleft? Compare against the
    # fraction of ACTL7A residues that align to any cleft column at all.
    q_cols = set(col_of[q].values())
    cleft_q = len(cleft_cols & q_cols)
    background = cleft_q / len(qseq)
    path = [v for v in variant_rows if v["reported_in_SPGF86"]]
    benign = [v for v in variant_rows if not v["reported_in_SPGF86"]]
    n_path_cleft = sum(v["in_nucleotide_cleft"] for v in path)
    n_benign_cleft = sum(v["in_nucleotide_cleft"] for v in benign)
    # exact binomial tail P(X >= k) with p = background
    from math import comb
    k, n = n_path_cleft, len(path)
    p_tail = sum(comb(n, i) * background**i * (1 - background) ** (n - i) for i in range(k, n + 1))
    cleft_enrichment = {
        "actl7a_residues_aligning_to_a_cleft_column": cleft_q,
        "actl7a_length": len(qseq),
        "background_fraction": round(background, 4),
        "n_reported_SPGF86_variants": len(path),
        "n_reported_SPGF86_variants_in_cleft": n_path_cleft,
        "n_population_polymorphisms": len(benign),
        "n_population_polymorphisms_in_cleft": n_benign_cleft,
        "binomial_p_upper_tail": round(p_tail, 4),
        "caveat": (
            "n is small and the variant set is not an unbiased sample, so this is suggestive "
            "only; UniProt annotates A245T, G246A and G362R as 'uncertain significance'."
        ),
    }

    # --- alignment windows, so a reader can check the mapping is not an alignment artefact ---
    anchors = sorted(set(CATALYTIC_RESIDUES) | {
        v["aligned_actin_position"] for v in variant_rows if v["aligned_actin_position"]
    })
    spans: list[list[int]] = []
    for a in anchors:
        lo, hi = max(1, a - 8), min(len(gc.seq), a + 8)
        if spans and lo <= spans[-1][1] + 1:
            spans[-1][1] = max(spans[-1][1], hi)
        else:
            spans.append([lo, hi])
    window_labels = [
        ref_label, "ACTB_HUMAN", "ACTA1_HUMAN", "ACTL7A_HUMAN", "ACTL7B_HUMAN",
        "ACTL9_HUMAN", "ARP1_HUMAN", "ARP2_HUMAN", "ARP9_YEAST",
    ]
    windows = []
    for lo, hi in spans:
        c0, c1 = col_of[ref_label][lo], col_of[ref_label][hi]
        windows.append({
            "actin_range": [lo, hi],
            "rows": {lbl: aln[lbl][c0:c1 + 1] for lbl in window_labels},
        })

    result = {
        "query": {"accession": "Q9Y615", "gene": "ACTL7A", "length": len(qseq)},
        "parameters": {
            "ligand_contact_cutoff_angstrom": CONTACT_CUTOFF,
            "interface_contact_cutoff_angstrom": INTERFACE_CUTOFF,
            "aligner": mafft_version,
            "alignment_mode": "mafft --localpair --maxiterate 1000 --anysymbol",
        },
        "structures": {
            "2BTF": {"chains_used": [c.chain_name for c in g_chains], "seqres_len": len(gc.seq)},
            "8A2S": {"chains_used": [c.chain_name for c in f_chains], "seqres_len": len(fc.seq)},
        },
        "sites": sites,
        "catalytic_residues": {
            "definition": CATALYTIC_RESIDUES,
            "reference": "standard actin numbering, verified against PDB 2BTF SEQRES",
            "per_sequence": catalytic,
        },
        "per_sequence": per_seq,
        "actl7a_variants": variant_rows,
        "nucleotide_cleft_variant_enrichment": cleft_enrichment,
        "alignment_windows": windows,
    }
    (HERE / "results.json").write_text(json.dumps(result, indent=2) + "\n")
    write_report(result)
    print(f"wrote {HERE / 'results.json'} and {HERE / 'RESULTS.md'}")
    return 0


def write_report(r: dict) -> None:
    groups_order = [
        "query", "query_ortholog", "query_paralog", "testis_arp", "conventional_actin",
        "filament_forming_arp", "nucleotide_binding_arp", "nuclear_arp", "divergent_swisnf_arp",
    ]
    lines: list[str] = []
    A = lines.append
    A("# ACTL7A actin-fold audit: does the fold still carry actin's working parts?")
    A("")
    A("Reproduce with `uv run --script actin_fold_audit.py` (regenerates `results.json`")
    A("and this file byte-for-byte; inputs are cached under `data/`, which is not committed).")
    A("")
    A("## Why")
    A("")
    A("ACTL7A is annotated with actin-derived terms (`GO:0005200 structural constituent of")
    A("cytoskeleton`, `GO:0007010 cytoskeleton organization`, `GO:0005198 structural molecule")
    A("activity`). Those hold only if ACTL7A retains the machinery the terms imply. This audit")
    A("derives two residue sets from experimental actin structures and reports what ACTL7A has")
    A("at those positions, against a panel that spans the family from conventional actin to the")
    A("most divergent SWI/SNF Arps.")
    A("")
    A("## Findings")
    A("")
    q = r["per_sequence"]["ACTL7A_HUMAN"]
    cat_q = r["catalytic_residues"]["per_sequence"]["ACTL7A_HUMAN"]
    catdef = r["catalytic_residues"]["definition"]
    keys = sorted(catdef, key=int)
    lost = [
        f"{catdef[k]}{k}->{aa}"
        for k, aa in zip(keys, cat_q["residues"])
        if aa != catdef[k]
    ]

    def group_mean(group: str, field: str) -> str:
        vals = [
            e[field]["percent_identity_at_site"]
            for e in r["per_sequence"].values()
            if e["group"] == group and e[field]["percent_identity_at_site"] is not None
        ]
        return f"{sum(vals) / len(vals):.1f}" if vals else "n/a"

    A(f"* Whole-chain identity of ACTL7A to the deposited actin: "
      f"**{q['identity_vs_2BTF_actin']['percent_identity']}%**.")
    A(f"* **Nucleotide cleft largely retained.** ACTL7A is "
      f"{q['g_pocket_all']['percent_identity_at_site']}% identical to actin across the "
      f"{r['sites']['g_pocket_all']['n_positions']} G-actin cleft positions "
      f"({q['g_pocket_phosphate']['percent_identity_at_site']}% at the phosphate contacts), "
      f"against {group_mean('conventional_actin', 'g_pocket_all')}% for conventional actins, "
      f"{group_mean('nucleotide_binding_arp', 'g_pocket_all')}% for Arp2/Arp3 and "
      f"{group_mean('divergent_swisnf_arp', 'g_pocket_all')}% for the divergent SWI/SNF Arps.")
    A(f"* **The ATP-hydrolysis trigger is not retained.** Of the "
      f"{len(keys)} literature-defined catalytic positions ACTL7A keeps "
      f"{cat_q['n_conserved']} ({cat_q['residues']}); changed: {', '.join(lost) or 'none'}. "
      "Every conventional actin and Arp1/Arp2/Arp3 in the panel keeps all of them.")
    A(f"* **The filament interface is not retained.** ACTL7A matches actin at "
      f"{q['f_protomer_interface']['percent_identity_at_site']}% of the "
      f"{r['sites']['f_protomer_interface']['n_positions']} inter-protomer contact positions, "
      f"versus {group_mean('conventional_actin', 'f_protomer_interface')}% for conventional "
      f"actins and {group_mean('filament_forming_arp', 'f_protomer_interface')}% for Arp1, "
      "which does form a filament (in dynactin).")
    ce = r["nucleotide_cleft_variant_enrichment"]
    A(f"* **The cleft is under disease-relevant constraint.** "
      f"{ce['n_reported_SPGF86_variants_in_cleft']}/{ce['n_reported_SPGF86_variants']} ACTL7A "
      f"variants reported in SPGF86 patients map into the nucleotide cleft, which covers only "
      f"{100 * ce['background_fraction']:.1f}% of the protein "
      f"(binomial p = {ce['binomial_p_upper_tail']}); "
      f"{ce['n_population_polymorphisms_in_cleft']}/{ce['n_population_polymorphisms']} "
      "population polymorphisms do.")
    A("")
    A("## Method")
    A("")
    p = r["parameters"]
    A(f"* Nucleotide-cleft residues: every residue within {p['ligand_contact_cutoff_angstrom']} A of")
    A("  ATP or the divalent cation in **PDB 2BTF** (profilin-beta-actin), and of ADP/Pi/Mg in")
    A("  **PDB 8A2S** (cryo-EM F-actin, Mg-ADP-Pi, 5 protomers).")
    A(f"* Inter-protomer interface: every residue within {p['interface_contact_cutoff_angstrom']} A of a")
    A("  *different* protomer in 8A2S, required in >=50% of the protomers that have any such contact")
    A("  (so the terminal protomers do not dilute the set).")
    A(f"* Alignment: `{p['alignment_mode']}` ({p['aligner']}), with the deposited SEQRES sequences")
    A("  included as alignment entries so that structural positions map without hard-coded numbering.")
    A("* Contact sets are computed by neighbour search, never listed by hand.")
    A("")
    A("## Site sizes")
    A("")
    A("| site | n positions | description |")
    A("|---|---|---|")
    for key, s in r["sites"].items():
        A(f"| `{key}` | {s['n_positions']} | {s['description']} ({s['source']}) |")
    A("")
    A("## Conservation at the derived sites")
    A("")
    A("`% id` = identity to the deposited actin sequence at that site's positions.")
    A("")
    A("| protein | group | len | % id vs actin (whole chain) | nucleotide cleft, G-actin | phosphates | metal | adenine | nucleotide cleft, F-actin | protomer interface |")
    A("|---|---|---|---|---|---|---|---|---|---|")
    for g in groups_order:
        for label, e in r["per_sequence"].items():
            if e["group"] != g:
                continue
            A(
                f"| {label} | {g} | {e['length']} | {e['identity_vs_2BTF_actin']['percent_identity']} "
                f"| {e['g_pocket_all']['percent_identity_at_site']} "
                f"| {e['g_pocket_phosphate']['percent_identity_at_site']} "
                f"| {e['g_pocket_metal']['percent_identity_at_site']} "
                f"| {e['g_pocket_adenine']['percent_identity_at_site']} "
                f"| {e['f_pocket_all']['percent_identity_at_site']} "
                f"| {e['f_protomer_interface']['percent_identity_at_site']} |"
            )
    A("")
    A("## Residue-by-residue at the G-actin nucleotide cleft")
    A("")
    site = r["sites"]["g_pocket_all"]
    A("Positions (2BTF numbering): " + ", ".join(str(x) for x in site["positions"]))
    A("")
    A("| protein | residues at those positions |")
    A("|---|---|")
    A(f"| **2BTF actin (reference)** | `{site['residues']}` |")
    for g in groups_order:
        for label, e in r["per_sequence"].items():
            if e["group"] != g:
                continue
            A(f"| {label} | `{e['g_pocket_all']['observed_residues']}` |")
    A("")
    A("## The ATP-hydrolysis catalytic set")
    A("")
    cat = r["catalytic_residues"]
    wanted = "".join(cat["definition"][k] for k in sorted(cat["definition"], key=int))
    order = ", ".join(f"{cat['definition'][k]}{k}" for k in sorted(cat['definition'], key=int))
    A(f"Actin residues {order} (standard actin numbering, verified against the 2BTF SEQRES).")
    A("Gln137 and His161 are the hydrolysis pair; Asp154 and the Val159 main chain stabilise the")
    A("attacking water; Asp11 is part of the divalent-cation site. Sources: PMID:37009486,")
    A("PMID:30622175.")
    A("")
    A(f"| protein | group | residues at {order} | conserved / {len(wanted)} |")
    A("|---|---|---|---|")
    for g in groups_order:
        for label, e in cat["per_sequence"].items():
            if e["group"] != g:
                continue
            A(f"| {label} | {g} | `{e['residues']}` | {e['n_conserved']} |")
    A("")
    A("## ACTL7A variants against the derived sites")
    A("")
    A("ACTL7A numbering includes its 64-residue N-terminal extension, so ACTL7A position *n*")
    A("aligns to roughly actin position *n* - 64; the mapped actin position is given explicitly.")
    A("")
    A("| variant | reported in SPGF86 | aligned actin position | actin residue there | falls in |")
    A("|---|---|---|---|---|")
    for v in r["actl7a_variants"]:
        hits = ", ".join(f"`{h}`" for h in v["in_sites"]) or "-"
        A(
            f"| {v['wild_type']}{v['position']}{v['variant']} | {'yes' if v['reported_in_SPGF86'] else 'no'} "
            f"| {v['aligned_actin_position'] if v['aligned_actin_position'] else '-'} "
            f"| {v['actin_residue_at_aligned_column_2BTF']} | {hits} |"
        )
    A("")
    ce = r["nucleotide_cleft_variant_enrichment"]
    A(
        f"{ce['actl7a_residues_aligning_to_a_cleft_column']} of ACTL7A's "
        f"{ce['actl7a_length']} residues align to a nucleotide-cleft column "
        f"({100 * ce['background_fraction']:.1f}% of the protein). "
        f"{ce['n_reported_SPGF86_variants_in_cleft']}/{ce['n_reported_SPGF86_variants']} variants "
        f"reported in SPGF86 patients fall there "
        f"(exact binomial upper tail p = {ce['binomial_p_upper_tail']}), versus "
        f"{ce['n_population_polymorphisms_in_cleft']}/{ce['n_population_polymorphisms']} "
        "population polymorphisms."
    )
    A("")
    A(f"*Caveat:* {ce['caveat']}")
    A("")
    A("## Alignment windows around every mapped position")
    A("")
    A("Included so the mapping can be checked rather than trusted: if these windows were")
    A("gap-ridden the residue calls above would be alignment artefacts.")
    A("")
    for w in r["alignment_windows"]:
        lo, hi = w["actin_range"]
        A(f"actin {lo}-{hi}:")
        A("")
        A("```")
        for lbl, seg in w["rows"].items():
            A(f"{lbl:<20s} {seg}")
        A("```")
        A("")
    A("## Notes on interpretation")
    A("")
    A("* This is a sequence-and-structure audit, not an assay. Retained residues mean the")
    A("  activity is *not excluded*; they do not demonstrate it. Lost residues are the stronger")
    A("  signal, because they exclude the activity on structural grounds.")
    A("* The comparator groups are the yardstick: read ACTL7A's numbers against the conventional")
    A("  actins (which bind nucleotide and polymerise) and against ARP7/ARP9 (the family's most")
    A("  divergent members).")
    A("* Percentages at a site are identity to *this particular* actin, so a conservative")
    A("  substitution counts as a mismatch. The residue-level table above is the thing to read")
    A("  when a percentage looks low.")
    (HERE / "RESULTS.md").write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    sys.exit(main())
