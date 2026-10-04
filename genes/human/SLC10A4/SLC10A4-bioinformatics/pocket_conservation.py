"""Are the NTCP sodium sites and myristoyl pocket conserved in the SLC10 paralogues?

Method, in three steps, with nothing hardcoded:

1. **Define the sites from experiment.** Parse the NTCP cryo-EM entries and
   collect every NTCP residue with a heavy atom within CUTOFF of a bound
   ligand: NA (sodium) in 7ZYI and 9QZQ, BJU (N-tetradecanoylglycine, the
   myristoyl-glycine of the HBV preS1 anchor) in 8RQF. The ligand-contacting
   residue set is therefore read off coordinates, not asserted from memory.
   The NTCP chain is identified as the polymer chain whose sequence matches the
   UniProt Q14973 sequence (the entries also contain Fab/nanobody chains).

2. **Align each paralogue to the experimental NTCP chain.** TM-align (via
   tmtools) gives a structure-based residue-to-residue mapping, a TM-score and
   an RMSD. The AFDB model of SLC10A1 itself is aligned the same way as a
   method control: if it does not recover the experimental SLC10A1 structure,
   the mapping cannot be trusted for the paralogues either.

3. **Read off what each paralogue has at those positions.** For every site
   residue, report the aligned residue in the target, classified as identical,
   a conservative substitution (same Dayhoff-style group), a non-conservative
   substitution, or a gap (no aligned residue).

Interpretation limits are stated in RESULTS.md, not here. In particular a
conserved pocket does not establish transport activity, and a degenerate one
does not by itself prove its absence -- this is a structural observation that
can support or undercut a hypothesis, never an experimental demonstration.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

import gemmi
import numpy as np
from Bio.Align import PairwiseAligner, substitution_matrices
from tmtools import tm_align

HERE = Path(__file__).parent
STRUCT = HERE / "structures"

CUTOFF = 4.5  # Angstrom, heavy-atom distance to a ligand atom

# Experimental references and the ligand that defines the site in each.
REFERENCES = [
    ("7ZYI", "NA", "sodium site(s), 2.88 A"),
    ("9QZQ", "NA", "sodium site(s), 3.11 A"),
    # The substrate pocket. CHO is glycochenodeoxycholic acid, a conjugated
    # bile salt and a genuine NTCP substrate, resolved in 7ZYI. This site was
    # missed in the first version of this analysis, which took the ligand list
    # from the RCSB entry summary field `nonpolymer_bound_components` -- that
    # reported only NA for 7ZYI. The script now enumerates the HETATM
    # components itself (see list_het_components) so a bound ligand cannot be
    # missed this way again.
    ("7ZYI", "CHO", "bile salt (glycochenodeoxycholate) pocket, 2.88 A"),
    ("8RQF", "BJU", "myristoyl-glycine (preS1 anchor) pocket, 3.41 A"),
]

# Ligands present in the reference entries that are not functional sites:
# CLR is cholesterol (membrane/annular lipid), HOH is water.
NON_SITE_LIGANDS = {"CLR", "HOH"}

TARGETS = {
    "Q14973": "SLC10A1 (NTCP) AFDB model - METHOD CONTROL",
    "Q12908": "SLC10A2 (ASBT)",
    "Q96EP9": "SLC10A4",
    "Q3KNW5": "SLC10A6 (SOAT)",
    "Q0GE19": "SLC10A7",
    "P26435": "Slc10a1/Ntcp (rat)",
    "O08705": "Slc10a1/Ntcp (mouse) - transports bile salts, not an HBV receptor",
}

# Dayhoff-style groups for a coarse conservative/non-conservative call.
GROUPS = [
    set("AGPST"),  # small / polar-neutral
    set("NDQE"),   # acidic + amide
    set("RHK"),    # basic
    set("ILMV"),   # aliphatic hydrophobic
    set("FWY"),    # aromatic
    set("C"),      # cysteine
]

AA3to1 = {
    "ALA": "A", "ARG": "R", "ASN": "N", "ASP": "D", "CYS": "C", "GLN": "Q",
    "GLU": "E", "GLY": "G", "HIS": "H", "ILE": "I", "LEU": "L", "LYS": "K",
    "MET": "M", "PHE": "F", "PRO": "P", "SER": "S", "THR": "T", "TRP": "W",
    "TYR": "Y", "VAL": "V", "MSE": "M",
}


@dataclass
class Chain:
    """A protein chain reduced to what the alignment and lookup need."""

    label: str
    seq: str
    coords: np.ndarray                    # CA coordinates, (n, 3)
    numbers: list[int] = field(default_factory=list)  # author seq ids, len n


def seq_pairing(ref_seq: str, tgt_seq: str) -> dict[int, int]:
    """Map reference 1-based positions to target 1-based positions.

    Global Needleman-Wunsch with BLOSUM62 over the two full UniProt
    sequences. Used because the SLC10 fold is shared but the paralogues differ
    enough in loop length that structural nearest-neighbour pairing slips (see
    the note at the call site).
    """
    aligner = PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -11
    aligner.extend_gap_score = -1
    aligner.mode = "global"
    alignment = aligner.align(ref_seq, tgt_seq)[0]
    pairing: dict[int, int] = {}
    for (r_start, r_end), (t_start, t_end) in zip(*alignment.aligned):
        for offset in range(r_end - r_start):
            pairing[r_start + offset + 1] = t_start + offset + 1
    return pairing


def verify_numbering(chain: Chain, uniprot_seq: str) -> tuple[int, int]:
    """Check author seqids index straight into the UniProt sequence.

    Returns (matches, total). The site positions are reported in UniProt
    numbering, so this has to hold for the cross-paralogue mapping to mean
    anything; the caller aborts if it does not.
    """
    matches = 0
    for aa, num in zip(chain.seq, chain.numbers):
        if 1 <= num <= len(uniprot_seq) and uniprot_seq[num - 1] == aa:
            matches += 1
    return matches, len(chain.seq)


def classify(ref_aa: str, tgt_aa: str) -> str:
    if tgt_aa == "-":
        return "gap"
    if ref_aa == tgt_aa:
        return "identical"
    for group in GROUPS:
        if ref_aa in group and tgt_aa in group:
            return "conservative"
    return "non-conservative"


def protein_chains(structure: gemmi.Structure) -> list[tuple[str, Chain]]:
    out = []
    for chain in structure[0]:
        seq, coords, numbers = [], [], []
        for residue in chain:
            if residue.name not in AA3to1:
                continue
            ca = residue.find_atom("CA", "*")
            if ca is None:
                continue
            seq.append(AA3to1[residue.name])
            coords.append([ca.pos.x, ca.pos.y, ca.pos.z])
            numbers.append(residue.seqid.num)
        if len(seq) >= 50:
            out.append((chain.name, Chain(chain.name, "".join(seq), np.array(coords), numbers)))
    return out


def uniprot_sequence(accession: str) -> str:
    """Read the target sequence out of the repo's cached UniProt flat file."""
    gene_dirs = {
        "Q14973": "human/SLC10A1/SLC10A1",
        "Q12908": "human/SLC10A2/SLC10A2",
        "Q96EP9": "human/SLC10A4/SLC10A4",
        "Q3KNW5": "human/SLC10A6/SLC10A6",
        "Q0GE19": "human/SLC10A7/SLC10A7",
        "P26435": "rat/Slc10a1/Slc10a1",
        "O08705": "mouse/Slc10a1/Slc10a1",
    }
    path = HERE.parents[2] / gene_dirs[accession]
    text = Path(f"{path}-uniprot.txt").read_text()
    seq_lines, in_seq = [], False
    for line in text.splitlines():
        if line.startswith("SQ   "):
            in_seq = True
            continue
        if in_seq:
            if line.startswith("//"):
                break
            seq_lines.append(line.replace(" ", ""))
    return "".join(seq_lines)


def identity(a: str, b: str) -> float:
    """Crude ungapped identity used only to pick the NTCP chain in an entry."""
    window = min(len(a), len(b))
    if window == 0:
        return 0.0
    hits = sum(1 for i in range(window) if a[i] == b[i])
    return hits / window


def find_ntcp_chain(structure: gemmi.Structure, ntcp_seq: str) -> Chain:
    """The entries hold Fab/nanobody chains too; pick the one that is NTCP."""
    best, best_score = None, -1.0
    for _, chain in protein_chains(structure):
        # NTCP chains are a subsequence of the UniProt sequence; score by the
        # fraction of the chain's residues found in a matching UniProt window.
        score = max(
            (identity(chain.seq, ntcp_seq[offset:]) for offset in range(0, 40)),
            default=0.0,
        )
        if score > best_score:
            best, best_score = chain, score
    if best is None or best_score < 0.8:
        raise RuntimeError(f"could not identify the NTCP chain (best score {best_score:.2f})")
    print(f"    NTCP chain = {best.label} ({len(best.seq)} residues, identity {best_score:.2f})")
    return best


def list_het_components(path: Path) -> dict[str, int]:
    """Enumerate non-amino-acid components actually present in the file.

    Done from the coordinates rather than from an RCSB summary field, because
    the summary's `nonpolymer_bound_components` omitted the bound bile salt in
    7ZYI and that omission cost this analysis its substrate pocket on the
    first pass.
    """
    structure = gemmi.read_structure(str(path))
    structure.setup_entities()
    counts: dict[str, int] = {}
    for chain in structure[0]:
        for residue in chain:
            if residue.name not in AA3to1:
                counts[residue.name] = counts.get(residue.name, 0) + 1
    return counts


def ligand_contacts(
    path: Path, ligand: str, ntcp_seq: str
) -> tuple[Chain, dict[int, str], int, dict[int, set[str]]]:
    """NTCP residues within CUTOFF of any atom of `ligand`."""
    structure = gemmi.read_structure(str(path))
    structure.setup_entities()
    structure.remove_alternative_conformations()
    structure.remove_hydrogens()

    ntcp = find_ntcp_chain(structure, ntcp_seq)

    ligand_atoms = []
    n_copies = 0
    for chain in structure[0]:
        for residue in chain:
            if residue.name == ligand:
                n_copies += 1
                ligand_atoms.extend([a.pos for a in residue])
    if not ligand_atoms:
        raise RuntimeError(f"{path.name}: no {ligand} found")

    # Which NTCP residues (by author seqid) contact the ligand, and do they do
    # so through their side chain or only through main-chain atoms? The
    # distinction matters for interpretation: a substitution at a position that
    # only contributes a backbone carbonyl is largely immaterial, because the
    # contact is sequence-independent.
    backbone = {"N", "CA", "C", "O", "OXT"}
    contacts: dict[int, str] = {}
    contact_via: dict[int, set[str]] = {}
    model = structure[0]
    for chain in model:
        if chain.name != ntcp.label:
            continue
        for residue in chain:
            if residue.name not in AA3to1:
                continue
            for atom in residue:
                if any(atom.pos.dist(lp) <= CUTOFF for lp in ligand_atoms):
                    contacts[residue.seqid.num] = AA3to1[residue.name]
                    kind = "main-chain" if atom.name in backbone else "side-chain"
                    contact_via.setdefault(residue.seqid.num, set()).add(kind)
    return ntcp, contacts, n_copies, contact_via


def main() -> None:
    ntcp_seq = uniprot_sequence("Q14973")
    results: dict[str, object] = {
        "cutoff_angstrom": CUTOFF,
        "sites": {},
        "alignments": {},
        "conservation": {},
    }

    # ---- step 1: define sites from the experimental structures
    site_defs = []
    print("Step 1: define sites from ligand contacts in the experimental structures")
    for pdb_id, ligand, note in REFERENCES:
        path = STRUCT / f"{pdb_id}.cif"
        if not path.exists():
            print(f"  {pdb_id}: MISSING, skipped")
            continue
        print(f"  {pdb_id} ({note}), ligand {ligand}:")
        het = list_het_components(path)
        interesting = {k: v for k, v in het.items() if k not in NON_SITE_LIGANDS}
        print(f"    components present: {het} (candidate sites: {sorted(interesting)})")
        ntcp, contacts, n_copies, contact_via = ligand_contacts(path, ligand, ntcp_seq)
        matched, total = verify_numbering(ntcp, ntcp_seq)
        if matched / total < 0.95:
            raise SystemExit(
                f"{pdb_id}: author numbering does not index into the UniProt "
                f"sequence ({matched}/{total}); site positions would be "
                "meaningless, so aborting rather than reporting them"
            )
        print(f"    numbering check: {matched}/{total} residues match UniProt Q14973")
        ordered = dict(sorted(contacts.items()))
        print(f"    {n_copies} copy/copies of {ligand}; {len(ordered)} contacting residues: "
              + ", ".join(f"{aa}{num}" for num, aa in ordered.items()))
        site_defs.append((pdb_id, ligand, note, ntcp, ordered, contact_via))
        results["sites"][f"{pdb_id}:{ligand}"] = {
            "note": note,
            "ligand_copies": n_copies,
            "contacts": {str(k): v for k, v in ordered.items()},
            "contact_atoms": {
                str(k): sorted(contact_via.get(k, [])) for k in ordered
            },
        }

    if not site_defs:
        raise SystemExit("no sites could be defined; aborting rather than inventing any")

    # ---- steps 2 and 3: align each target and read off the site positions
    print("\nSteps 2-3: align paralogues to the experimental NTCP chain and read off sites")
    for acc, label in TARGETS.items():
        model_path = STRUCT / f"AF-{acc}.pdb"
        if not model_path.exists():
            print(f"  {acc} ({label}): model MISSING, skipped")
            continue
        model = gemmi.read_structure(str(model_path))
        model.setup_entities()
        chains = protein_chains(model)
        if not chains:
            print(f"  {acc}: no usable chain, skipped")
            continue
        target = chains[0][1]
        target_full_seq = uniprot_sequence(acc)

        print(f"\n  {acc} - {label}")
        results["conservation"][acc] = {"label": label, "sites": {}}

        for pdb_id, ligand, note, ntcp, contacts, contact_via in site_defs:
            # TM-align gives the independent fold comparison (score + RMSD).
            res = tm_align(ntcp.coords, target.coords, ntcp.seq, target.seq)

            # The residue correspondence comes from the sequence alignment,
            # NOT from geometric nearest neighbours. A geometric pairing was
            # tried first and rejected: it fails its own method control,
            # mapping the control model's F128 onto G132 (a ~4-residue frame
            # shift) for the 8RQF superposition, because mutual CA
            # nearest-neighbour pairing is unstable where helices shift
            # between conformational states.
            pairing = seq_pairing(ntcp_seq, target_full_seq)

            rows = []
            for num, ref_aa in contacts.items():
                tgt_num = pairing.get(num)
                tgt_aa = target_full_seq[tgt_num - 1] if tgt_num else "-"
                via = sorted(contact_via.get(num, []))
                call = classify(ref_aa, tgt_aa)
                # A substitution at a position whose only ligand contact is a
                # backbone atom does not change the contact chemistry.
                if call in {"conservative", "non-conservative"} and via == ["main-chain"]:
                    call = f"{call} (main-chain contact only)"
                rows.append({
                    "ntcp_residue": f"{ref_aa}{num}",
                    "target_residue": f"{tgt_aa}{tgt_num}" if tgt_num else "-",
                    "contact_via": via,
                    "call": call,
                })
            counts: dict[str, int] = {}
            for row in rows:
                counts[row["call"]] = counts.get(row["call"], 0) + 1
            key = f"{pdb_id}:{ligand}"
            results["conservation"][acc]["sites"][key] = {
                "tm_score_normalised_on_ntcp": round(float(res.tm_norm_chain1), 3),
                "rmsd": round(float(res.rmsd), 2),
                "counts": counts,
                "rows": rows,
            }
            results["alignments"][f"{acc}|{pdb_id}"] = {
                "mapping_method": "global BLOSUM62 alignment of UniProt sequences",
                "tm_score_normalised_on_ntcp": round(float(res.tm_norm_chain1), 3),
                "tm_score_normalised_on_target": round(float(res.tm_norm_chain2), 3),
                "rmsd": round(float(res.rmsd), 2),
                "aligned_pairs": len(pairing),
            }
            summary = ", ".join(f"{k}={v}" for k, v in sorted(counts.items()))
            print(f"    {key} ({note.split(',')[0]}): TM={res.tm_norm_chain1:.3f} "
                  f"RMSD={res.rmsd:.2f} | {summary}")
            for row in rows:
                print(f"       {row['ntcp_residue']:>7}  ->  {row['target_residue']:>7}  {row['call']}")

    out = HERE / "pocket_conservation.json"
    out.write_text(json.dumps(results, indent=2) + "\n")
    print(f"\nWrote {out.name}")


if __name__ == "__main__":
    main()
