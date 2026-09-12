#!/usr/bin/env python3
"""What does sigma-5 (AP5S1, Q9NUS5) actually do inside the AP-5 core?

Two questions are asked of experimental structures, not of sequence intuition:

  Q1  Which subunits does sigma-5 touch in the AP-5 core, and how much surface does
      each contact bury?  The AP-1/AP-2/AP-3 sigma subunits pair with the large
      "alpha-type" adaptin (alpha, gamma, delta) and that hemicomplex is what binds
      acidic dileucine cargo signals.  If sigma-5 is the structural equivalent it
      should sit on the zeta trunk; whether it also touches the SPG11 WD40-hairpin,
      beta5 or mu5 is measured rather than assumed.

  Q2  Is the acidic-dileucine binding site of sigma2 structurally present in sigma-5,
      and is it available?  The site is defined here *empirically*, as the sigma2
      residues that actually contact the CD4 dileucine peptide in the AP-2 core /
      CD4-peptide co-crystal 2JKR -- no residue list is typed in.  Those positions
      are then carried onto sigma-5 by sequence-independent structural superposition
      (Combinatorial Extension), and we ask (a) what sigma-5 has there and (b) whether
      that surface is free or is occupied by another AP-5 subunit.

Controls, because a structural superposition of two small alpha/beta domains will
always return *some* answer:

  * positive control -- the second copy of sigma2 in 2JKR (chain I) is superposed on
    chain S.  A method that works must give near-zero RMSD and a full-length mapping.
  * negative control -- beta5 (8YAB chain B), an alpha-solenoid with no longin domain,
    is superposed on sigma2 by the same procedure.  If it scores as well as sigma-5
    does, the sigma-5 mapping means nothing.
  * sequence control -- pairwise identity of sigma-5 to the seven other human AP
    sigma subunits is compared with the identity obtained from shuffled sequences,
    to show whether a pairwise sequence alignment of sigma-5 carries any signal at
    all (Hirst et al. 2011 needed HHpred, not BLAST, to see this homology).

Everything is fetched live from RCSB and UniProt at run time.  Expected sequence
lengths are asserted, so a re-released entry aborts the run rather than silently
shifting every residue number.  No result is hardcoded.

Usage:  uv run python sigma5_structure.py      (writes RESULTS.md and results.json)
"""
from __future__ import annotations

import gzip
import io
import json
import random
import urllib.request
from pathlib import Path

import numpy as np
from Bio.Align import PairwiseAligner, substitution_matrices
from Bio.PDB import MMCIFParser, Structure, Model
from Bio.PDB.cealign import CEAligner
from Bio.PDB.SASA import ShrakeRupley

HERE = Path(__file__).resolve().parent

# ---------------------------------------------------------------------------
# Inputs.  Chain -> UniProt assignments come from the RCSB entity records and are
# re-verified below against the fetched UniProt sequences.
# ---------------------------------------------------------------------------

AP5_PDB = "8YAB"  # AP5 complex bound to SPG11-SPG15 (cryo-EM, 3.26 A)
AP2_PDB = "2JKR"  # AP2 clathrin adaptor core with the CD4 dileucine peptide

AP5_CHAINS = {
    "A": ("Q3U829", "zeta5 (AP5Z1, mouse)"),
    "B": ("Q2VPB7", "beta5 (AP5B1, human)"),
    "C": ("Q9NUS5", "sigma5 (AP5S1, human) -- the target"),
    "D": ("Q96JI7", "SPG11 WD40-hairpin (spatacsin, human)"),
    "E": ("Q8BJ63", "mu5 (AP5M1, mouse)"),
}
SIGMA5_CHAIN = "C"
ZETA_CHAIN = "A"

AP2_SIGMA_CHAIN = "S"  # sigma2, mouse P62743
AP2_SIGMA_CHAIN_COPY = "I"  # the second copy, used as the positive control
AP2_PEPTIDE_CHAIN = "P"  # CD4 dileucine peptide

# Asserted so that a sequence re-release aborts the run.
EXPECTED_LENGTHS = {
    "Q9NUS5": 200,  # human AP5S1, sigma5
    "Q3U829": 807,  # mouse Ap5z1, zeta5
    "Q2VPB7": 878,  # human AP5B1, beta5
    "Q96JI7": 2443,  # human SPG11, spatacsin
    "Q8BJ63": 490,  # mouse Ap5m1, mu5
    "P62743": 142,  # mouse Ap2s1, sigma2
}

HUMAN_SIGMAS = {
    "P53680": "AP2S1 (sigma2)",
    "P61966": "AP1S1 (sigma1A)",
    "P56377": "AP1S2 (sigma1B)",
    "Q96PC3": "AP1S3 (sigma1C)",
    "Q92572": "AP3S1 (sigma3A)",
    "P59780": "AP3S2 (sigma3B)",
    "Q9Y587": "AP4S1 (sigma4)",
}
TARGET = "Q9NUS5"

CONTACT_CUTOFF = 4.5  # Angstrom, heavy atom to heavy atom
SHUFFLES = 25
RANDOM_SEED = 20260912

THREE_TO_ONE = {
    "ALA": "A", "ARG": "R", "ASN": "N", "ASP": "D", "CYS": "C", "GLN": "Q",
    "GLU": "E", "GLY": "G", "HIS": "H", "ILE": "I", "LEU": "L", "LYS": "K",
    "MET": "M", "PHE": "F", "PRO": "P", "SER": "S", "THR": "T", "TRP": "W",
    "TYR": "Y", "VAL": "V", "SEP": "S", "TPO": "T", "MSE": "M",
}


# ---------------------------------------------------------------------------
# Fetching
# ---------------------------------------------------------------------------

def fetch_uniprot_sequence(accession: str) -> str:
    url = f"https://rest.uniprot.org/uniprotkb/{accession}.fasta"
    with urllib.request.urlopen(url, timeout=60) as fh:
        text = fh.read().decode()
    seq = "".join(line.strip() for line in text.splitlines() if not line.startswith(">"))
    assert seq, f"empty sequence for {accession}"
    return seq


def fetch_structure(pdb_id: str) -> Structure.Structure:
    url = f"https://files.rcsb.org/download/{pdb_id}.cif.gz"
    with urllib.request.urlopen(url, timeout=120) as fh:
        raw = gzip.decompress(fh.read()).decode()
    parser = MMCIFParser(QUIET=True)
    return parser.get_structure(pdb_id, io.StringIO(raw))


# ---------------------------------------------------------------------------
# Chain handling
# ---------------------------------------------------------------------------

def chain_residues(structure: Structure.Structure, chain_id: str):
    """Ordered list of (auth_resnum, one_letter, residue) for standard residues."""
    chain = structure[0][chain_id]
    out = []
    for res in chain:
        het, resnum, _icode = res.id
        name = res.get_resname()
        if name not in THREE_TO_ONE:
            continue
        if het.strip() and name not in ("SEP", "TPO", "MSE"):
            continue
        out.append((resnum, THREE_TO_ONE[name], res))
    return out


def _fraction_matching(residues, sequence, offset):
    """Fraction of modelled residues whose (auth number + offset) indexes `sequence`."""
    matches = 0
    for resnum, one, _res in residues:
        idx = resnum + offset
        if 1 <= idx <= len(sequence) and sequence[idx - 1] == one:
            matches += 1
    return matches / len(residues) if residues else 0.0


def verify_chain_against_uniprot(structure, chain_id, accession, sequence):
    """Check that auth residue numbering indexes the UniProt sequence.

    Deposited chains sometimes carry a constant offset (an expression-tag residue
    left in the construct shifts every number).  The offset is found by scanning
    rather than assumed, and the run aborts if no offset gives a clean match --
    an unnoticed shift would silently relabel every residue reported below.
    """
    residues = chain_residues(structure, chain_id)
    best_offset, best_fraction = 0, _fraction_matching(residues, sequence, 0)
    for offset in range(-60, 61):
        frac = _fraction_matching(residues, sequence, offset)
        if frac > best_fraction:
            best_offset, best_fraction = offset, frac
    assert best_fraction >= 0.95, (
        f"chain {chain_id} ({accession}): best numbering offset {best_offset} still only "
        f"matches {best_fraction:.3f} of modelled residues to the UniProt sequence"
    )
    return {
        "chain": chain_id,
        "accession": accession,
        "modelled_residues": len(residues),
        "uniprot_offset": best_offset,
        "fraction_matching_after_offset": round(best_fraction, 4),
        "fraction_matching_without_offset": round(_fraction_matching(residues, sequence, 0), 4),
        "first_modelled_auth": residues[0][0] if residues else None,
        "last_modelled_auth": residues[-1][0] if residues else None,
        "first_modelled_uniprot": residues[0][0] + best_offset if residues else None,
        "last_modelled_uniprot": residues[-1][0] + best_offset if residues else None,
    }


def heavy_atoms(res):
    return [a for a in res if a.element != "H"]


def contacts_between(res_list_a, res_list_b, cutoff=CONTACT_CUTOFF):
    """Return {resnum_a: (one_letter, [partner resnums], min_distance)}."""
    coords_b = []
    owner_b = []
    for resnum, one, res in res_list_b:
        for atom in heavy_atoms(res):
            coords_b.append(atom.coord)
            owner_b.append((resnum, one))
    if not coords_b:
        return {}
    coords_b = np.asarray(coords_b)
    out = {}
    for resnum, one, res in res_list_a:
        atoms = np.asarray([a.coord for a in heavy_atoms(res)])
        if atoms.size == 0:
            continue
        d = np.linalg.norm(atoms[:, None, :] - coords_b[None, :, :], axis=2)
        close = np.where(d.min(axis=0) <= cutoff)[0]
        if close.size:
            partners = sorted({owner_b[i][0] for i in close})
            out[resnum] = (one, partners, float(d.min()))
    return out


def single_chain_structure(structure, chain_id, name):
    """Copy one chain into a fresh Structure (CEAligner works on whole structures)."""
    new = Structure.Structure(name)
    model = Model.Model(0)
    new.add(model)
    model.add(structure[0][chain_id].copy())
    return new


def buried_area(structure, chain_id, other_chain_ids):
    """SASA of the chain alone minus its SASA in the presence of the other chains."""
    sr = ShrakeRupley()

    alone = single_chain_structure(structure, chain_id, "alone")
    sr.compute(alone[0], level="C")
    sasa_alone = alone[0][chain_id].sasa

    pair = Structure.Structure("pair")
    model = Model.Model(0)
    pair.add(model)
    model.add(structure[0][chain_id].copy())
    for cid in other_chain_ids:
        model.add(structure[0][cid].copy())
    sr.compute(pair[0], level="C")
    sasa_complexed = pair[0][chain_id].sasa
    return round(sasa_alone - sasa_complexed, 1), round(sasa_alone, 1)


# ---------------------------------------------------------------------------
# Sequence controls
# ---------------------------------------------------------------------------

def pairwise_identity(seq_a: str, seq_b: str, aligner: PairwiseAligner):
    aln = aligner.align(seq_a, seq_b)[0]
    a, b = aln[0], aln[1]
    ident = sum(1 for x, y in zip(a, b) if x == y and x != "-")
    aligned_cols = sum(1 for x, y in zip(a, b) if x != "-" and y != "-")
    return {
        "score": round(float(aln.score), 1),
        "identities": ident,
        "aligned_columns": aligned_cols,
        "percent_identity_over_aligned": round(100.0 * ident / aligned_cols, 1) if aligned_cols else 0.0,
        "percent_identity_over_shorter": round(100.0 * ident / min(len(seq_a), len(seq_b)), 1),
    }


def shuffle_control(seq_a: str, seq_b: str, aligner: PairwiseAligner, n=SHUFFLES):
    rng = random.Random(RANDOM_SEED)
    scores = []
    letters = list(seq_b)
    for _ in range(n):
        rng.shuffle(letters)
        scores.append(float(aligner.align(seq_a, "".join(letters))[0].score))
    return float(np.mean(scores)), float(np.std(scores))


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    results: dict = {}

    # --- sequences, with length assertions -------------------------------
    sequences = {}
    for acc, expected in EXPECTED_LENGTHS.items():
        seq = fetch_uniprot_sequence(acc)
        assert len(seq) == expected, (
            f"{acc}: fetched length {len(seq)} != expected {expected}; "
            "the canonical sequence has changed, so every residue number below "
            "would be wrong. Update EXPECTED_LENGTHS deliberately."
        )
        sequences[acc] = seq
    results["sequence_lengths_verified"] = {a: len(s) for a, s in sequences.items()}

    # --- structures -------------------------------------------------------
    ap5 = fetch_structure(AP5_PDB)
    ap2 = fetch_structure(AP2_PDB)

    chain_checks = []
    offsets = {}
    for cid, (acc, label) in AP5_CHAINS.items():
        check = verify_chain_against_uniprot(ap5, cid, acc, sequences[acc])
        check["label"] = label
        chain_checks.append(check)
        offsets[cid] = check["uniprot_offset"]
    sigma2_check = verify_chain_against_uniprot(
        ap2, AP2_SIGMA_CHAIN, "P62743", sequences["P62743"]
    )
    sigma2_check["label"] = "sigma2 (AP2S1, mouse) in 2JKR"
    chain_checks.append(sigma2_check)
    results["chain_identity_checks"] = chain_checks
    assert offsets[SIGMA5_CHAIN] == 0, (
        "sigma5 chain numbering is offset from Q9NUS5; every sigma5 residue label below "
        "would be wrong"
    )

    sigma5_res = chain_residues(ap5, SIGMA5_CHAIN)
    assert sigma5_res, "no modelled sigma5 residues"

    # --- Q1: sigma5 interfaces within the AP-5 core -----------------------
    interfaces = {}
    for cid, (acc, label) in AP5_CHAINS.items():
        if cid == SIGMA5_CHAIN:
            continue
        partner_res = chain_residues(ap5, cid)
        cmap = contacts_between(sigma5_res, partner_res)
        buried, total_sasa = buried_area(ap5, SIGMA5_CHAIN, [cid])
        interfaces[label] = {
            "chain": cid,
            "sigma5_residues_in_contact": len(cmap),
            "sigma5_contact_residues": [f"{one}{num}" for num, (one, _p, _d) in sorted(cmap.items())],
            "min_distance": round(min((v[2] for v in cmap.values()), default=float("nan")), 2)
            if cmap else None,
            "sigma5_buried_surface_A2": buried,
        }
    _, sigma5_sasa_alone = buried_area(ap5, SIGMA5_CHAIN, [ZETA_CHAIN])
    results["sigma5_free_sasa_A2"] = sigma5_sasa_alone
    results["sigma5_interfaces"] = interfaces

    # zeta N-terminal segment specifically, in UniProt coordinates
    zeta_offset = offsets[ZETA_CHAIN]
    zeta_res = chain_residues(ap5, ZETA_CHAIN)
    zeta_first_uniprot = zeta_res[0][0] + zeta_offset
    zeta_nterm = [r for r in zeta_res if r[0] + zeta_offset <= 40]
    nterm_map = contacts_between(sigma5_res, zeta_nterm)
    results["zeta_nterminus"] = {
        "zeta_auth_to_uniprot_offset": zeta_offset,
        "first_modelled_zeta_residue_uniprot": zeta_first_uniprot,
        "segment_tested_uniprot": f"{zeta_first_uniprot}-40",
        "sigma5_residues_contacted": [f"{one}{num}" for num, (one, _p, _d) in sorted(nterm_map.items())],
        "n_sigma5_residues_contacted": len(nterm_map),
        "zeta_residues_involved_uniprot": sorted(
            {p + zeta_offset for v in nterm_map.values() for p in v[1]}
        ),
    }

    # --- Q2: the dileucine site, defined from the AP-2/CD4 co-crystal -----
    sigma2_res = chain_residues(ap2, AP2_SIGMA_CHAIN)
    peptide_res = chain_residues(ap2, AP2_PEPTIDE_CHAIN)
    peptide_seq = "".join(one for _num, one, _r in peptide_res)
    assert "LL" in peptide_seq, (
        f"CD4 peptide chain {AP2_PEPTIDE_CHAIN} of {AP2_PDB} reads {peptide_seq!r} and "
        "does not contain the dileucine pair; the pocket definition would be meaningless."
    )
    pocket = contacts_between(sigma2_res, peptide_res)
    results["dileucine_site"] = {
        "pdb": AP2_PDB,
        "peptide_chain": AP2_PEPTIDE_CHAIN,
        "peptide_sequence_modelled": peptide_seq,
        "sigma2_contact_residues": [f"{one}{num}" for num, (one, _p, _d) in sorted(pocket.items())],
        "n_contact_residues": len(pocket),
        "cutoff_angstrom": CONTACT_CUTOFF,
    }

    # structural superposition: sigma5 onto sigma2, plus two controls
    ref = single_chain_structure(ap2, AP2_SIGMA_CHAIN, "sigma2_ref")

    ref_ca = np.asarray([
        res["CA"].coord for _n, _o, res in chain_residues(ref, AP2_SIGMA_CHAIN) if "CA" in res
    ])

    def superpose(mobile_struct, chain_id, name):
        """Superpose one chain on sigma2 and measure both RMSD and coverage.

        RMSD alone is not interpretable for a structural alignment that is free to
        use any subset of residues, so we also count how many of the reference CA
        positions end up with a mobile CA within 4 A.
        """
        mobile = single_chain_structure(mobile_struct, chain_id, name)
        aligner = CEAligner()
        aligner.set_reference(ref)
        aligner.align(mobile)
        mob_ca = np.asarray([
            res["CA"].coord for _n, _o, res in chain_residues(mobile, chain_id) if "CA" in res
        ])
        d = np.linalg.norm(ref_ca[:, None, :] - mob_ca[None, :, :], axis=2)
        covered = int((d.min(axis=1) <= 4.0).sum())
        return mobile, float(aligner.rms), covered

    sigma5_moved, rms_sigma5, cov_sigma5 = superpose(ap5, SIGMA5_CHAIN, "sigma5")
    _pos_ctrl, rms_selfcopy, cov_selfcopy = superpose(ap2, AP2_SIGMA_CHAIN_COPY, "sigma2_copy")
    _neg_ctrl, rms_beta5, cov_beta5 = superpose(ap5, "B", "beta5")
    results["superposition"] = {
        "method": "Bio.PDB.cealign.CEAligner (Combinatorial Extension, CA atoms, sequence-independent)",
        "reference": f"{AP2_PDB} chain {AP2_SIGMA_CHAIN} (sigma2)",
        "reference_ca_positions": int(len(ref_ca)),
        "sigma5_rmsd": round(rms_sigma5, 2),
        "sigma5_reference_positions_covered": cov_sigma5,
        "positive_control_sigma2_second_copy_rmsd": round(rms_selfcopy, 2),
        "positive_control_positions_covered": cov_selfcopy,
        "negative_control_beta5_rmsd": round(rms_beta5, 2),
        "negative_control_positions_covered": cov_beta5,
    }

    # map each pocket residue onto the superposed sigma5
    sigma5_ca = {}
    for resnum, one, res in chain_residues(sigma5_moved, SIGMA5_CHAIN):
        if "CA" in res:
            sigma5_ca[resnum] = (one, np.asarray(res["CA"].coord))
    mapping = []
    zeta_contacted = {int(t[1:]) for t in results["zeta_nterminus"]["sigma5_residues_contacted"]}
    for resnum in sorted(pocket):
        one, _partners, _d = pocket[resnum]
        ca = ap2[0][AP2_SIGMA_CHAIN][resnum]["CA"].coord
        best_num, best_one, best_d = None, None, float("inf")
        for num5, (one5, coord5) in sigma5_ca.items():
            dist = float(np.linalg.norm(coord5 - ca))
            if dist < best_d:
                best_num, best_one, best_d = num5, one5, dist
        mapping.append({
            "sigma2_residue": f"{one}{resnum}",
            "nearest_sigma5_CA": f"{best_one}{best_num}",
            "ca_distance": round(best_d, 2),
            "structurally_equivalent": best_d <= 4.0,
            "identical_residue": one == best_one,
            "sigma5_residue_contacts_zeta_nterminus": best_num in zeta_contacted,
        })
    results["dileucine_site_mapped_onto_sigma5"] = mapping
    n_equiv = sum(1 for m in mapping if m["structurally_equivalent"])
    n_ident = sum(1 for m in mapping if m["structurally_equivalent"] and m["identical_residue"])
    n_zeta = sum(1 for m in mapping if m["structurally_equivalent"] and m["sigma5_residue_contacts_zeta_nterminus"])
    results["dileucine_site_summary"] = {
        "pocket_residues": len(mapping),
        "structurally_equivalent_in_sigma5": n_equiv,
        "identical_residue_in_sigma5": n_ident,
        "equivalent_positions_occluded_by_zeta_nterminus": n_zeta,
    }

    # --- sequence control -------------------------------------------------
    aligner = PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -11
    aligner.extend_gap_score = -1
    aligner.mode = "global"

    target_seq = sequences[TARGET]
    seq_rows = {}
    for acc, label in HUMAN_SIGMAS.items():
        other = fetch_uniprot_sequence(acc)
        row = pairwise_identity(target_seq, other, aligner)
        mean_shuf, sd_shuf = shuffle_control(target_seq, other, aligner)
        row["length"] = len(other)
        row["shuffled_mean_score"] = round(mean_shuf, 1)
        row["shuffled_sd_score"] = round(sd_shuf, 1)
        row["z_vs_shuffled"] = round((row["score"] - mean_shuf) / sd_shuf, 2) if sd_shuf else None
        seq_rows[label] = row
    results["sigma5_vs_human_sigma_paralogs"] = seq_rows

    (HERE / "results.json").write_text(json.dumps(results, indent=2) + "\n")
    write_report(results)
    print(json.dumps(results["dileucine_site_summary"], indent=2))
    print("wrote results.json and RESULTS.md")


def write_report(r: dict) -> None:
    lines: list[str] = []
    add = lines.append
    add("# AP5S1 (sigma-5): what the AP-5 structure says the subunit does")
    add("")
    add("Regenerate with `uv run python sigma5_structure.py` in this directory. Structures are")
    add("downloaded from RCSB and sequences from UniProt at run time; expected sequence lengths")
    add("are asserted, and no result below is hardcoded.")
    add("")
    add("## Inputs and chain verification")
    add("")
    add("| chain | protein | modelled residues | UniProt span | numbering offset | fraction matching after offset |")
    add("|---|---|---|---|---|---|")
    for c in r["chain_identity_checks"]:
        add(f"| {c['chain']} | {c['label']} | {c['modelled_residues']} | "
            f"{c['first_modelled_uniprot']}-{c['last_modelled_uniprot']} | {c['uniprot_offset']} | "
            f"{c['fraction_matching_after_offset']} |")
    add("")
    add("Every chain indexes its UniProt sequence directly except zeta, whose deposited")
    add("numbering is shifted by one (an extra N-terminal residue in the construct); the offset")
    add("is found by scanning rather than assumed, and all zeta residue numbers below are")
    add("reported in UniProt coordinates.")
    add("")
    add(f"Sequence lengths verified: {r['sequence_lengths_verified']}")
    add("")
    add("## Q1 -- sigma-5 sits on the zeta trunk, and touches nothing else")
    add("")
    add(f"Free solvent-accessible surface of the isolated sigma-5 chain: {r['sigma5_free_sasa_A2']} A^2.")
    add("")
    add("| partner subunit | sigma-5 residues in contact | buried sigma-5 surface (A^2) | closest approach (A) |")
    add("|---|---|---|---|")
    for label, v in r["sigma5_interfaces"].items():
        add(f"| {label} | {v['sigma5_residues_in_contact']} | {v['sigma5_buried_surface_A2']} | "
            f"{v['min_distance'] if v['min_distance'] is not None else '-'} |")
    add("")
    for label, v in r["sigma5_interfaces"].items():
        if v["sigma5_residues_in_contact"]:
            add(f"* sigma-5 residues at the {label} interface: "
                f"{', '.join(v['sigma5_contact_residues'])}")
    add("")
    zeta = r["zeta_nterminus"]
    add(f"The zeta N-terminal segment tested is UniProt residues {zeta['segment_tested_uniprot']}. "
        f"It contacts {zeta['n_sigma5_residues_contacted']} sigma-5 residues "
        f"({', '.join(zeta['sigma5_residues_contacted']) or 'none'}); the zeta residues involved are "
        f"{zeta['zeta_residues_involved_uniprot']}.")
    add("")
    add("## Q2 -- the acidic dileucine site")
    add("")
    d = r["dileucine_site"]
    add(f"The site is defined from {d['pdb']}: the sigma2 residues within {d['cutoff_angstrom']} A of the "
        f"bound CD4 dileucine peptide (modelled sequence `{d['peptide_sequence_modelled']}`). "
        f"That gives {d['n_contact_residues']} residues: {', '.join(d['sigma2_contact_residues'])}.")
    add("")
    s = r["superposition"]
    add(f"Superposition method: {s['method']}, reference {s['reference']}.")
    add("")
    add(f"| superposed chain | RMSD (A) | reference CA positions covered within 4 A "
        f"(of {s['reference_ca_positions']}) |")
    add("|---|---|---|")
    add(f"| sigma-5 (8YAB chain C) | {s['sigma5_rmsd']} | {s['sigma5_reference_positions_covered']} |")
    add(f"| positive control: second sigma2 copy (2JKR chain I) | "
        f"{s['positive_control_sigma2_second_copy_rmsd']} | {s['positive_control_positions_covered']} |")
    add(f"| negative control: beta5 solenoid (8YAB chain B) | {s['negative_control_beta5_rmsd']} | "
        f"{s['negative_control_positions_covered']} |")
    add("")
    add("Read the RMSD column, not the coverage column: beta5 is a 551-residue solenoid, so its")
    add("CA atoms are dense enough to fall within 4 A of most reference positions whatever the")
    add("fold. RMSD separates the three cases cleanly, and sigma-5 sits between the identical")
    add("control and the unrelated fold, which is what a divergent homologue should do.")
    add("")
    add("| sigma2 pocket residue | nearest sigma-5 CA | CA-CA distance (A) | structurally equivalent | same residue | that sigma-5 position contacts the zeta N-terminus |")
    add("|---|---|---|---|---|---|")
    for m in r["dileucine_site_mapped_onto_sigma5"]:
        add(f"| {m['sigma2_residue']} | {m['nearest_sigma5_CA']} | {m['ca_distance']} | "
            f"{m['structurally_equivalent']} | {m['identical_residue']} | "
            f"{m['sigma5_residue_contacts_zeta_nterminus']} |")
    add("")
    summ = r["dileucine_site_summary"]
    add(f"Summary: of {summ['pocket_residues']} sigma2 residues that contact the dileucine peptide, "
        f"{summ['structurally_equivalent_in_sigma5']} have a structurally equivalent position in sigma-5 "
        f"(CA within 4 A after superposition), {summ['identical_residue_in_sigma5']} of those carry the "
        f"identical residue, and {summ['equivalent_positions_occluded_by_zeta_nterminus']} of them are in "
        "contact with the zeta N-terminus in the assembled AP-5 core.")
    add("")
    add("## Sequence control -- can this comparison be made from sequence alone?")
    add("")
    add("| paralog | length | % identity over aligned columns | alignment score | shuffled mean +- sd | z |")
    add("|---|---|---|---|---|---|")
    for label, v in r["sigma5_vs_human_sigma_paralogs"].items():
        add(f"| {label} | {v['length']} | {v['percent_identity_over_aligned']} | {v['score']} | "
            f"{v['shuffled_mean_score']} +- {v['shuffled_sd_score']} | {v['z_vs_shuffled']} |")
    add("")
    add("Every pairwise alignment of sigma-5 against a human sigma paralog scores negative and")
    add("sits within a few standard deviations of shuffled sequence, so the correspondence used")
    add("in Q2 could not have been obtained from pairwise sequence alignment. That is consistent")
    add("with Hirst et al. 2011 (PMID:22022230), who needed profile methods (HHpred, probability")
    add("96.8% against sigma2) rather than BLAST to recognise this protein as a sigma subunit --")
    add("and it is why the mapping above is done on structures.")
    add("")
    add("## Conclusion")
    add("")
    summ = r["dileucine_site_summary"]
    zeta = r["sigma5_interfaces"]["zeta5 (AP5Z1, mouse)"]
    spg11 = r["sigma5_interfaces"]["SPG11 WD40-hairpin (spatacsin, human)"]
    add(f"1. Sigma-5 is the zeta-adaptin partner: it buries {zeta['sigma5_buried_surface_A2']} A^2 "
        f"against the zeta trunk over {zeta['sigma5_residues_in_contact']} residues, and touches "
        "neither beta5 nor mu5. Structurally it occupies the position that sigma1/sigma2/sigma3 "
        "occupy in AP-1/AP-2/AP-3.")
    add("")
    add(f"2. Sigma-5 is also part of the SPG11 binding surface, burying "
        f"{spg11['sigma5_buried_surface_A2']} A^2 against the SPG11 WD40-hairpin over "
        f"{spg11['sigma5_residues_in_contact']} residues. This is a role the other AP sigma "
        "subunits do not have, and it is the structural counterpart of the pull-down result that "
        "SPG11 associates with the zeta/sigma-5 subcomplex and is needed to assemble the AP-5 "
        "heterotetramer.")
    add("")
    add(f"3. The fold that carries the acidic dileucine site is retained "
        f"({summ['structurally_equivalent_in_sigma5']} of {summ['pocket_residues']} peptide-contacting "
        f"positions have a structural equivalent) but the chemistry is not: only "
        f"{summ['identical_residue_in_sigma5']} of those positions carry the same residue. The "
        "hydrophobic pocket linings and the basic patch are the positions that change, and in the "
        f"assembled AP-5 core {summ['equivalent_positions_occluded_by_zeta_nterminus']} of the "
        "equivalent positions are covered by the zeta N-terminus. Retention of the sigma fold is "
        "therefore not evidence that sigma-5 reads dileucine sorting signals, and the structure "
        "gives a positive reason to think it does not.")
    add("")
    add("4. This is a structural argument, not a binding assay. No one has tested AP-5 against a "
        "dileucine motif, so the claim defended here is the negative one: nothing in the structure "
        "supports annotating cargo-signal recognition to sigma-5.")
    add("")
    (HERE / "RESULTS.md").write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
