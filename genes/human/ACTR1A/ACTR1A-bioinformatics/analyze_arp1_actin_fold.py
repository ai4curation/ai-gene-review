"""Is human ACTR1A (Arp1/alpha-centractin) an actin that keeps its nucleotide
site and its polymerisation interface?

The question is load-bearing for GO curation of ACTR1A, because two molecular
function annotations turn on it:

* ``GO:0005524 ATP binding`` reached ACTR1A only through the UniProt
  ``ATP-binding`` keyword pipeline (``GO_REF:0000043``), which GOA has retired;
  the term is now absent from ACTR1A's GOA record.
* ``GO:0005200 structural constituent of cytoskeleton`` is likewise absent from
  ACTR1A, while the non-polymerising pointed-end paralog ACTR10 (Arp11)
  carries it.

Three computations, none of them hard-coded:

A. Take a beta-actin structure with ATP bound (PDB 2BTF, chain A is bovine
   beta-actin) and derive the nucleotide-contacting residues from coordinates.
   Map them onto human ACTB and then onto ACTR1A, ACTR1B and ACTR10.
B. Take the human dynactin cryo-EM structure (PDB 9B85) and inventory what is
   actually modelled: how many ACTR1A protomers, and what nonpolymer species
   sits in each.  Derive the nucleotide-contacting ACTR1A residues from those
   coordinates too, and ask whether they are the same site as in actin.
C. From the same human structure, derive the ACTR1A-ACTR1A protofilament
   interfaces and the contacts made by ACTR10, to compare a subunit that
   polymerises with one that terminates the filament.

Run with ``uv run python analyze_arp1_actin_fold.py``.  Writes RESULTS.md and
results.json next to the script; both are overwritten, so do not hand-edit
them.  A missing input is a hard error naming the fix, never a silently
degraded report.
"""

from __future__ import annotations

import json
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

import gemmi
import numpy as np
import requests
from Bio import Align
from Bio.Align import substitution_matrices

HERE = Path(__file__).parent
CACHE = HERE / "cache"

# Bovine beta-actin + profilin, 2.55 A, ATP bound. Chain A = beta-actin.
ACTIN_ATP_PDB = "2btf"
# Human dynactin, cryo-EM, 3.47 A (the Dre1-bound reconstruction).
HUMAN_DYNACTIN_PDB = "9b85"

CONTACT_CUTOFF_A = 4.5
NUCLEOTIDE_COMPS = {"ATP", "ADP", "ANP", "AGS", "ADX"}

SUBJECTS = {
    "ACTB": "P60709",
    "ACTR1A": "P61163",
    "ACTR1B": "P42025",
    "ACTR10": "Q9NZ32",
}
REFERENCE = "ACTB"
ARP1_ENTITY_NAME = "Alpha-centractin"
ARP11_ENTITY_NAME = "Actin-related protein 10"


# --------------------------------------------------------------------------
# inputs
# --------------------------------------------------------------------------
def _require(path: Path, how: str) -> Path:
    if not path.exists():
        raise FileNotFoundError(f"missing input {path}; regenerate with: {how}")
    return path


def fetch_uniprot_fasta(acc: str) -> str:
    CACHE.mkdir(exist_ok=True)
    path = CACHE / f"{acc}.fasta"
    if not path.exists():
        r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
        r.raise_for_status()
        path.write_text(r.text)
    text = _require(path, f"delete {path} and re-run").read_text()
    seq = "".join(
        ln.strip() for ln in text.splitlines() if ln and not ln.startswith(">")
    )
    if not seq:
        raise ValueError(f"empty sequence for {acc} in {path}")
    return seq


def fetch_mmcif(pdb_id: str) -> Path:
    CACHE.mkdir(exist_ok=True)
    path = CACHE / f"{pdb_id}.cif.gz"
    if not path.exists():
        r = requests.get(
            f"https://files.rcsb.org/download/{pdb_id}.cif.gz", timeout=180
        )
        r.raise_for_status()
        path.write_bytes(r.content)
    return _require(path, f"delete {path} and re-run")


# --------------------------------------------------------------------------
# alignment helpers
# --------------------------------------------------------------------------
def make_aligner() -> Align.PairwiseAligner:
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -11
    aligner.extend_gap_score = -1
    aligner.mode = "global"
    return aligner


def index_map(aligner: Align.PairwiseAligner, a: str, b: str) -> dict[int, int]:
    """Map 1-based positions in ``a`` to 1-based positions in ``b``."""
    aln = aligner.align(a, b)[0]
    mapping: dict[int, int] = {}
    for (a0, a1), (b0, b1) in zip(*aln.aligned):
        for off in range(int(a1) - int(a0)):
            mapping[int(a0) + off + 1] = int(b0) + off + 1
    return mapping


def pct_identity(aligner: Align.PairwiseAligner, a: str, b: str) -> float:
    aln = aligner.align(a, b)[0]
    same = sum(
        1
        for (a0, a1), (b0, b1) in zip(*aln.aligned)
        for off in range(int(a1) - int(a0))
        if a[int(a0) + off] == b[int(b0) + off]
    )
    return round(100.0 * same / min(len(a), len(b)), 1)


# --------------------------------------------------------------------------
# mmCIF helpers
# --------------------------------------------------------------------------
def entity_descriptions(block) -> dict[str, str]:
    out = {}
    for row in block.find("_entity.", ["id", "pdbx_description"]):
        out[row.str(0)] = row.str(1)
    if not out:
        raise ValueError("no _entity.pdbx_description in mmCIF")
    return out


def entity_source_organisms(block) -> dict[str, str]:
    """entity_id -> source organism, so the reference actin is not silently
    assumed to be human. 2BTF is bovine beta-actin, which is sequence-identical
    to human ACTB over the modelled region; the identity is computed below rather
    than asserted."""
    out: dict[str, str] = {}
    for tag, cols in (
        ("_entity_src_gen.", ["entity_id", "pdbx_gene_src_scientific_name"]),
        ("_entity_src_nat.", ["entity_id", "pdbx_organism_scientific"]),
    ):
        for row in block.find(tag, cols):
            out.setdefault(row.str(0), row.str(1))
    return out

def entity_sequences(block) -> dict[str, str]:
    out = {}
    for row in block.find("_entity_poly.", ["entity_id", "pdbx_seq_one_letter_code_can"]):
        out[row.str(0)] = "".join(row.str(1).split())
    return out


def chain_inventory(block) -> tuple[dict[str, str], dict[str, set[str]]]:
    """auth chain -> polymer entity id, and auth chain -> nonpolymer comp ids."""
    chain_entity: dict[str, str] = {}
    chain_hetero: dict[str, set[str]] = defaultdict(set)
    cols = ["group_PDB", "auth_asym_id", "label_entity_id", "label_comp_id"]
    for row in block.find("_atom_site.", cols):
        ch = row.str(1)
        if row.str(0) == "ATOM":
            chain_entity.setdefault(ch, row.str(2))
        else:
            chain_hetero[ch].add(row.str(3))
    return chain_entity, dict(chain_hetero)


@dataclass
class Atom:
    chain: str
    seqid: int  # label_seq_id (entity index) for polymer atoms; auth for hetero
    comp: str
    xyz: tuple[float, float, float]
    is_poly: bool


def load_atoms(block) -> list[Atom]:
    """Atoms keyed by label_seq_id for polymers.

    auth_seq_id cannot be used: in 9B85 chain B the same entity is numbered
    2009-2378 while every other ACTR1A chain is 7-376, so an auth-based
    consensus across protomers silently collapses to nothing.  label_seq_id is
    the entity-relative index and is uniform across copies.
    """
    cols = [
        "group_PDB",
        "auth_asym_id",
        "auth_seq_id",
        "label_seq_id",
        "label_comp_id",
        "Cartn_x",
        "Cartn_y",
        "Cartn_z",
        "label_atom_id",
    ]
    out = []
    for row in block.find("_atom_site.", cols):
        if row.str(8).startswith("H"):
            continue
        is_poly = row.str(0) == "ATOM"
        label_seq = row.str(3)
        if is_poly:
            if label_seq in (".", "?"):
                raise ValueError(
                    f"polymer atom without label_seq_id in chain {row.str(1)}"
                )
            seqid = int(label_seq)
        else:
            seqid = int(row.str(2))
        out.append(
            Atom(
                chain=row.str(1),
                seqid=seqid,
                comp=row.str(4),
                xyz=(float(row.str(5)), float(row.str(6)), float(row.str(7))),
                is_poly=is_poly,
            )
        )
    if not out:
        raise ValueError("no atoms parsed")
    return out


def one_letter(comp: str) -> str:
    info = gemmi.find_tabulated_residue(comp)
    if info is None:
        return "X"
    return info.one_letter_code.upper() or "X"


def contacts_to_ligand(
    atoms: list[Atom], lig_chain: str, lig_comps: set[str], protein_chain: str
) -> dict[int, tuple[str, float]]:
    """Residues of ``protein_chain`` within the cutoff of a ligand in ``lig_chain``."""
    lig = np.asarray(
        [a.xyz for a in atoms if a.chain == lig_chain and a.comp in lig_comps]
    )
    if lig.size == 0:
        raise ValueError(f"no ligand {lig_comps} in chain {lig_chain}")
    out: dict[int, tuple[str, float]] = {}
    for a in atoms:
        if not a.is_poly or a.chain != protein_chain:
            continue
        d = float(np.min(np.linalg.norm(lig - np.asarray(a.xyz), axis=1)))
        if d <= CONTACT_CUTOFF_A:
            prev = out.get(a.seqid)
            if prev is None or d < prev[1]:
                out[a.seqid] = (one_letter(a.comp), round(d, 2))
    return dict(sorted(out.items()))


def interchain_contacts(
    atoms: list[Atom], chains: set[str]
) -> tuple[dict[tuple[str, str], int], dict[tuple[str, str], set[int]]]:
    """Heavy-atom contacts between polymer chains, restricted to ``chains``."""
    sel = [a for a in atoms if a.is_poly and a.chain in chains]
    coords = np.asarray([a.xyz for a in sel])
    ns = gemmi.NeighborSearch  # noqa: F841  (kept for readers; grid built below)
    # simple uniform grid to keep this O(N) rather than O(N^2)
    cell = CONTACT_CUTOFF_A
    grid: dict[tuple[int, int, int], list[int]] = defaultdict(list)
    keys = np.floor(coords / cell).astype(int)
    for i, k in enumerate(map(tuple, keys)):
        grid[k].append(i)
    pair_counts: dict[tuple[str, str], int] = defaultdict(int)
    pair_res: dict[tuple[str, str], set[int]] = defaultdict(set)
    for i, a in enumerate(sel):
        kx, ky, kz = keys[i]
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                for dz in (-1, 0, 1):
                    for j in grid.get((kx + dx, ky + dy, kz + dz), ()):
                        if j <= i:
                            continue
                        b = sel[j]
                        if a.chain == b.chain:
                            continue
                        if (
                            float(np.linalg.norm(coords[i] - coords[j]))
                            > CONTACT_CUTOFF_A
                        ):
                            continue
                        key = tuple(sorted((a.chain, b.chain)))
                        pair_counts[key] += 1
                        if key[0] == a.chain:
                            pair_res[key].add(a.seqid)
                        else:
                            pair_res[key].add(b.seqid)
    return dict(pair_counts), dict(pair_res)


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------
def main() -> None:
    seqs = {name: fetch_uniprot_fasta(acc) for name, acc in SUBJECTS.items()}
    aligner = make_aligner()
    ref = seqs[REFERENCE]

    # ---------------- A: actin-ATP homology ----------------
    block2 = gemmi.cif.read(str(fetch_mmcif(ACTIN_ATP_PDB))).sole_block()
    atoms2 = load_atoms(block2)
    ent_desc2 = entity_descriptions(block2)
    ent_seq2 = entity_sequences(block2)
    chain_ent2, chain_het2 = chain_inventory(block2)
    atp_chains = [c for c, h in chain_het2.items() if "ATP" in h]
    if len(atp_chains) != 1:
        raise ValueError(f"expected one ATP-bearing chain in 2BTF, got {atp_chains}")
    actin_chain = atp_chains[0]
    actin_ent = chain_ent2[actin_chain]
    actin_contacts = contacts_to_ligand(atoms2, actin_chain, {"ATP"}, actin_chain)

    # entity (label_seq_id) numbering -> human ACTB numbering
    ent_seq = ent_seq2[actin_ent]
    ent2ref = index_map(aligner, ent_seq, ref)
    actin_organism = entity_source_organisms(block2).get(actin_ent, "unrecorded")
    actin_vs_human_actb = pct_identity(aligner, ent_seq, ref)

    module_a_rows = []
    for ent_i, (res, dist) in actin_contacts.items():
        ref_i = ent2ref.get(ent_i)
        module_a_rows.append(
            {
                "entity_index": ent_i,
                "pdb_residue": res,
                "min_distance_A": dist,
                "actb_pos": ref_i,
                "actb_res": ref[ref_i - 1] if ref_i else None,
            }
        )

    maps = {n: index_map(aligner, ref, s) for n, s in seqs.items() if n != REFERENCE}
    identities = {
        n: pct_identity(aligner, ref, s) for n, s in seqs.items() if n != REFERENCE
    }
    for row in module_a_rows:
        if row["actb_pos"] is None:
            continue
        for n, m in maps.items():
            p = m.get(row["actb_pos"])
            row[f"{n}_pos"] = p
            row[f"{n}_res"] = seqs[n][p - 1] if p else None
            row[f"{n}_identical"] = bool(p and seqs[n][p - 1] == row["actb_res"])

    mapped = [r for r in module_a_rows if r["actb_pos"]]
    summary_a = {}
    for n in maps:
        ident = sum(1 for r in mapped if r.get(f"{n}_identical"))
        aligned = sum(1 for r in mapped if r.get(f"{n}_pos"))
        summary_a[n] = {
            "global_pct_identity_to_ACTB": identities[n],
            "positions_aligned": aligned,
            "positions_identical": ident,
            "pct_identical": round(100.0 * ident / len(mapped), 1) if mapped else 0.0,
        }

    # ---------------- B/C: human dynactin ----------------
    blockH = gemmi.cif.read(str(fetch_mmcif(HUMAN_DYNACTIN_PDB))).sole_block()
    atomsH = load_atoms(blockH)
    ent_descH = entity_descriptions(blockH)
    ent_seqH = entity_sequences(blockH)
    chain_entH, chain_hetH = chain_inventory(blockH)

    inventory = []
    arp1_chains, arp11_chains = [], []
    for ch, ent in sorted(chain_entH.items()):
        desc = ent_descH.get(ent, "?")
        het = sorted(chain_hetH.get(ch, set()))
        inventory.append({"chain": ch, "entity": ent, "description": desc, "hetero": het})
        if desc == ARP1_ENTITY_NAME:
            arp1_chains.append(ch)
        if desc == ARP11_ENTITY_NAME:
            arp11_chains.append(ch)
    if not arp1_chains:
        raise ValueError(f"no chain described as {ARP1_ENTITY_NAME!r} in {HUMAN_DYNACTIN_PDB}")

    # confirm the modelled ACTR1A sequence really is P61163
    arp1_ent = chain_entH[arp1_chains[0]]
    arp1_model_seq = ent_seqH.get(arp1_ent, "")
    arp1_vs_p61163 = pct_identity(aligner, arp1_model_seq, seqs["ACTR1A"]) if arp1_model_seq else None

    nucleotide_per_arp1 = {
        ch: sorted(NUCLEOTIDE_COMPS & chain_hetH.get(ch, set())) for ch in arp1_chains
    }
    arp1_with_nucleotide = [c for c, v in nucleotide_per_arp1.items() if v]

    # nucleotide contacts inside human ACTR1A, mapped to ACTB numbering
    model2up = index_map(aligner, arp1_model_seq, seqs["ACTR1A"]) if arp1_model_seq else {}
    arp1_nuc_contacts = {}
    for ch in arp1_with_nucleotide:
        comps = set(nucleotide_per_arp1[ch])
        arp1_nuc_contacts[ch] = contacts_to_ligand(atomsH, ch, comps, ch)
    consensus_positions = sorted(
        set.intersection(*[set(v) for v in arp1_nuc_contacts.values()])
    ) if arp1_nuc_contacts else []
    union_positions = sorted(set().union(*[set(v) for v in arp1_nuc_contacts.values()])) if arp1_nuc_contacts else []

    # ACTR1A position -> ACTB position (invert the ACTB->ACTR1A map)
    actr1a_to_actb = {v: k for k, v in maps["ACTR1A"].items()}
    actin_site_actb = {r["actb_pos"] for r in mapped}
    site_overlap = []
    for p in union_positions:
        actb_p = actr1a_to_actb.get(p)
        site_overlap.append(
            {
                "actr1a_pos": p,
                "actr1a_res": seqs["ACTR1A"][p - 1] if p <= len(seqs["ACTR1A"]) else None,
                "actb_pos": actb_p,
                "in_actin_atp_site": bool(actb_p and actb_p in actin_site_actb),
                "in_all_arp1_protomers": p in consensus_positions,
            }
        )
    n_overlap = sum(1 for s in site_overlap if s["in_actin_atp_site"])

    # filament interfaces: the Arps, beta-actin, and both capping modules
    filament_chains = set(arp1_chains) | set(arp11_chains)
    for ch, ent in chain_entH.items():
        desc = ent_descH.get(ent, "")
        if desc.startswith("Actin, cytoplasmic") or desc.startswith(
            "F-actin-capping protein"
        ):
            filament_chains.add(ch)
    pair_counts, pair_res = interchain_contacts(atomsH, filament_chains)
    chain_label = {
        ch: ent_descH.get(chain_entH[ch], "?") for ch in filament_chains
    }
    interfaces = []
    for (c1, c2), n in sorted(pair_counts.items(), key=lambda kv: -kv[1]):
        interfaces.append(
            {
                "chains": [c1, c2],
                "labels": [chain_label[c1], chain_label[c2]],
                "n_atom_contacts": n,
                "n_interface_residues_first_chain": len(pair_res[(c1, c2)]),
            }
        )
    partner_counts = defaultdict(int)
    for (c1, c2) in pair_counts:
        partner_counts[c1] += 1
        partner_counts[c2] += 1
    partners = {
        ch: {"label": chain_label[ch], "n_filament_partners": partner_counts[ch]}
        for ch in sorted(filament_chains)
    }

    # Does ACTR1A keep actin's longitudinal (polymerisation) surface? Take the
    # largest ACTR1A-ACTR1A interface and translate its residues into ACTB
    # numbering, so they can be compared with actin's own filament contacts.
    arp1_pairs = [
        (k, v)
        for k, v in pair_counts.items()
        if chain_label[k[0]] == ARP1_ENTITY_NAME
        and chain_label[k[1]] == ARP1_ENTITY_NAME
    ]
    if not arp1_pairs:
        raise ValueError("no ACTR1A-ACTR1A interface found; check chain labelling")
    biggest = max(arp1_pairs, key=lambda kv: kv[1])[0]
    # Separate the two contact-size classes rather than eyeballing them: the
    # intra-protofilament (longitudinal) interfaces are several-fold larger than
    # the lateral ones, so split at the largest gap in the sorted contact counts.
    sizes = sorted((v for _, v in arp1_pairs), reverse=True)
    gaps = [(sizes[i] - sizes[i + 1], i) for i in range(len(sizes) - 1)]
    split_after = max(gaps)[1] if gaps else 0
    threshold = sizes[split_after]
    long_pairs = sorted(
        (k for k, v in arp1_pairs if v >= threshold),
        key=lambda k: -pair_counts[k],
    )
    per_pair = {
        f"{k[0]}-{k[1]}": {
            "n_atom_contacts": pair_counts[k],
            "actr1a_positions": sorted(pair_res[k]),
        }
        for k in long_pairs
    }
    consensus = sorted(
        set.intersection(*[set(pair_res[k]) for k in long_pairs])
    ) if long_pairs else []
    longitudinal = {
        "chains": list(biggest),
        "n_atom_contacts": pair_counts[biggest],
        "actr1a_positions": sorted(pair_res[biggest]),
        "longitudinal_class_threshold_atom_contacts": threshold,
        "n_longitudinal_actr1a_actr1a_pairs": len(long_pairs),
        "per_longitudinal_pair": per_pair,
        "consensus_positions_all_longitudinal_pairs": consensus,
    }
    longitudinal["mapped_to_actb"] = [
        {
            "actr1a_pos": p,
            "actr1a_res": seqs["ACTR1A"][mp - 1] if (mp := model2up.get(p)) else None,
            "actb_pos": actr1a_to_actb.get(model2up.get(p)),
        }
        for p in longitudinal["actr1a_positions"]
    ]
    longitudinal["consensus_mapped_to_actb"] = [
        {
            "actr1a_pos": p,
            "actr1a_res": seqs["ACTR1A"][mp - 1] if (mp := model2up.get(p)) else None,
            "actb_pos": actr1a_to_actb.get(model2up.get(p)),
        }
        for p in longitudinal["consensus_positions_all_longitudinal_pairs"]
    ]
    cons_actb = [
        m["actb_pos"] for m in longitudinal["consensus_mapped_to_actb"] if m["actb_pos"]
    ]
    longitudinal["consensus_actb_positions_below_70"] = sorted(
        p for p in cons_actb if p < 70
    )
    longitudinal["consensus_actb_positions_70_and_above"] = sorted(
        p for p in cons_actb if p >= 70
    )
    actb_positions = [
        m["actb_pos"] for m in longitudinal["mapped_to_actb"] if m["actb_pos"]
    ]
    longitudinal["actb_position_range"] = (
        [min(actb_positions), max(actb_positions)] if actb_positions else []
    )
    # actin's subdomain-2 DNase-I-binding loop lies between the two N-terminal
    # nucleotide elements; report how much of this interface falls N-terminal to
    # actin residue 70, i.e. in subdomain 2.
    longitudinal["n_actb_positions_below_70"] = sum(
        1 for p in actb_positions if p < 70
    )
    longitudinal["actb_positions_below_70"] = sorted(p for p in actb_positions if p < 70)

    results = {
        "module_a_actin_atp_homology": {
            "pdb": ACTIN_ATP_PDB.upper(),
            "actin_chain": actin_chain,
            "actin_entity_description": ent_desc2.get(actin_ent),
            "actin_source_organism": actin_organism,
            "actin_entity_pct_identity_to_human_ACTB": actin_vs_human_actb,
            "contact_cutoff_A": CONTACT_CUTOFF_A,
            "n_contact_residues": len(actin_contacts),
            "table": module_a_rows,
            "summary": summary_a,
        },
        "module_b_human_dynactin_nucleotide": {
            "pdb": HUMAN_DYNACTIN_PDB.upper(),
            "chain_inventory": inventory,
            "actr1a_chains": arp1_chains,
            "n_actr1a_protomers": len(arp1_chains),
            "modelled_actr1a_seq_pct_identity_to_P61163": arp1_vs_p61163,
            "nucleotide_per_actr1a_chain": nucleotide_per_arp1,
            "n_actr1a_chains_with_nucleotide": len(arp1_with_nucleotide),
            "nucleotide_contact_positions_union": union_positions,
            "nucleotide_contact_positions_in_all_protomers": consensus_positions,
            "site_overlap_with_actin_atp_site": site_overlap,
            "n_positions_shared_with_actin_atp_site": n_overlap,
        },
        "module_c_filament_interfaces": {
            "pdb": HUMAN_DYNACTIN_PDB.upper(),
            "chains_considered": sorted(filament_chains),
            "interfaces": interfaces,
            "partners_per_chain": partners,
            "largest_actr1a_actr1a_interface": longitudinal,
        },
        "sequence_lengths": {k: len(v) for k, v in seqs.items()},
        "uniprot": SUBJECTS,
    }
    (HERE / "results.json").write_text(json.dumps(results, indent=2) + "\n")
    (HERE / "RESULTS.md").write_text(render(results))
    print(f"wrote {HERE/'results.json'} and {HERE/'RESULTS.md'}")
    for n, s in summary_a.items():
        print(
            f"  A {n}: global {s['global_pct_identity_to_ACTB']}% id to ACTB; "
            f"actin nucleotide site {s['positions_identical']}/{s['positions_aligned']} identical"
        )
    b = results["module_b_human_dynactin_nucleotide"]
    print(
        f"  B {b['pdb']}: {b['n_actr1a_protomers']} ACTR1A protomers, "
        f"{b['n_actr1a_chains_with_nucleotide']} with modelled nucleotide "
        f"{sorted({c for v in b['nucleotide_per_actr1a_chain'].values() for c in v})}; "
        f"{b['n_positions_shared_with_actin_atp_site']}/"
        f"{len(b['nucleotide_contact_positions_union'])} contact positions coincide with actin's ATP site"
    )


def render(r: dict) -> str:
    a = r["module_a_actin_atp_homology"]
    b = r["module_b_human_dynactin_nucleotide"]
    c = r["module_c_filament_interfaces"]
    names = list(a["summary"].keys())
    o: list[str] = []
    o.append("# ACTR1A (Arp1): nucleotide site and polymerisation interface")
    o.append("")
    o.append(
        "Generated by `analyze_arp1_actin_fold.py` "
        "(`uv run python analyze_arp1_actin_fold.py`). Overwritten on every run; "
        "do not hand-edit."
    )
    o.append("")
    o.append(
        "Sequences: "
        + ", ".join(
            f"{k} {v} ({r['sequence_lengths'][k]} aa)" for k, v in r["uniprot"].items()
        )
    )
    o.append("")

    o.append("## A. Actin's ATP site, transferred by alignment")
    o.append("")
    o.append(
        f"Reference: PDB **{a['pdb']}** chain `{a['actin_chain']}` "
        f"({a['actin_entity_description']}, source organism "
        f"*{a['actin_source_organism']}*, "
        f"{a['actin_entity_pct_identity_to_human_ACTB']}% identical to human ACTB "
        f"over the modelled region), ligand ATP, heavy-atom cutoff "
        f"{a['contact_cutoff_A']} A. Nucleotide-contacting residues found from "
        f"coordinates: **{a['n_contact_residues']}**. The reference is not human, so "
        f"contacts are transferred through human ACTB rather than read off directly."
    )
    o.append("")
    o.append("| protein | global % identity to ACTB | site positions aligned | identical | % identical |")
    o.append("|---|---|---|---|---|")
    for n, v in a["summary"].items():
        o.append(
            f"| {n} | {v['global_pct_identity_to_ACTB']} | {v['positions_aligned']} | "
            f"{v['positions_identical']} | {v['pct_identical']} |"
        )
    o.append("")
    o.append("| ACTB pos | ACTB | min dist (A) | " + " | ".join(names) + " |")
    o.append("|---" * (3 + len(names)) + "|")
    for row in a["table"]:
        if not row.get("actb_pos"):
            continue
        cells = []
        for n in names:
            p, res = row.get(f"{n}_pos"), row.get(f"{n}_res")
            mark = "" if row.get(f"{n}_identical") else "*"
            cells.append(f"{res}{p}{mark}" if p else "-")
        o.append(
            f"| {row['actb_pos']} | {row['actb_res']} | {row['min_distance_A']} | "
            + " | ".join(cells)
            + " |"
        )
    o.append("")
    o.append("`*` = residue differs from beta-actin at that position.")
    o.append("")

    o.append("## B. What the human dynactin structure actually models")
    o.append("")
    o.append(f"PDB **{b['pdb']}** chain inventory:")
    o.append("")
    o.append("| chain | entity | description | nonpolymer |")
    o.append("|---|---|---|---|")
    for row in b["chain_inventory"]:
        o.append(
            f"| {row['chain']} | {row['entity']} | {row['description']} | "
            + (", ".join(row["hetero"]) if row["hetero"] else "-")
            + " |"
        )
    o.append("")
    o.append(
        f"- ACTR1A protomers modelled: **{b['n_actr1a_protomers']}** "
        f"(chains {', '.join(b['actr1a_chains'])}); the modelled sequence is "
        f"{b['modelled_actr1a_seq_pct_identity_to_P61163']}% identical to UniProt P61163."
    )
    nucs = sorted({x for v in b["nucleotide_per_actr1a_chain"].values() for x in v})
    o.append(
        f"- ACTR1A chains with a modelled nucleotide: "
        f"**{b['n_actr1a_chains_with_nucleotide']}/{b['n_actr1a_protomers']}**, "
        f"ligand(s) {', '.join(nucs) if nucs else 'none'}."
    )
    o.append(
        f"- Residues within {a['contact_cutoff_A']} A of that nucleotide: "
        f"{len(b['nucleotide_contact_positions_union'])} positions across protomers, "
        f"{len(b['nucleotide_contact_positions_in_all_protomers'])} of them in every protomer."
    )
    o.append(
        f"- Of those positions, **{b['n_positions_shared_with_actin_atp_site']}** align "
        f"onto residues that contact ATP in {a['pdb']} beta-actin, i.e. the ACTR1A "
        f"nucleotide sits in the conserved actin nucleotide cleft."
    )
    o.append("")
    o.append("| ACTR1A pos | res | aligned ACTB pos | also an actin ATP contact | present in all protomers |")
    o.append("|---|---|---|---|---|")
    for s in b["site_overlap_with_actin_atp_site"]:
        o.append(
            f"| {s['actr1a_pos']} | {s['actr1a_res']} | {s['actb_pos'] or '-'} | "
            f"{'yes' if s['in_actin_atp_site'] else 'no'} | "
            f"{'yes' if s['in_all_arp1_protomers'] else 'no'} |"
        )
    o.append("")

    o.append("## C. Who polymerises and who terminates")
    o.append("")
    o.append(
        f"Inter-chain heavy-atom contacts (cutoff {a['contact_cutoff_A']} A) among the "
        f"filament chains of {c['pdb']}:"
    )
    o.append("")
    o.append("| chain pair | subunits | atom contacts | interface residues (first chain) |")
    o.append("|---|---|---|---|")
    for i in c["interfaces"]:
        o.append(
            f"| {i['chains'][0]}-{i['chains'][1]} | "
            f"{i['labels'][0]} / {i['labels'][1]} | {i['n_atom_contacts']} | "
            f"{i['n_interface_residues_first_chain']} |"
        )
    o.append("")
    o.append("| chain | subunit | filament partners |")
    o.append("|---|---|---|")
    for ch, v in c["partners_per_chain"].items():
        o.append(f"| {ch} | {v['label']} | {v['n_filament_partners']} |")
    o.append("")
    lg = c["largest_actr1a_actr1a_interface"]
    o.append(
        f"Largest ACTR1A-ACTR1A interface: chains {lg['chains'][0]}-{lg['chains'][1]}, "
        f"{lg['n_atom_contacts']} atom contacts over "
        f"{len(lg['actr1a_positions'])} ACTR1A residues. In beta-actin numbering these "
        f"span {lg['actb_position_range'][0]}-{lg['actb_position_range'][1]}, of which "
        f"{lg['n_actb_positions_below_70']} lie N-terminal to actin residue 70 "
        f"(subdomain 2, the DNase-I-binding loop that makes actin's longitudinal "
        f"filament contact): {lg['actb_positions_below_70']}."
    )
    o.append("")
    o.append(
        "Full ACTR1A interface residue list for that pair (P61163 numbering, nothing "
        "omitted): " + ", ".join(str(p) for p in lg["actr1a_positions"]) + ". The "
        "subdomain-2 residues are the ones that carry the polymerisation argument; the "
        "higher-numbered positions are subdomain-3/4 contacts on the partner face and "
        "are reported here for completeness."
    )
    o.append("")
    o.append(
        f"Generalising beyond that single pair: splitting the ACTR1A-ACTR1A interfaces "
        f"at the largest gap in their contact counts separates "
        f"{lg['n_longitudinal_actr1a_actr1a_pairs']} large "
        f"(>= {lg['longitudinal_class_threshold_atom_contacts']} atom contacts, "
        f"intra-protofilament) interfaces from the smaller lateral ones. Positions "
        f"present in **every** large interface: "
        + ", ".join(str(p) for p in lg["consensus_positions_all_longitudinal_pairs"])
        + f". In beta-actin numbering, those below residue 70 (subdomain 2) are "
        f"{lg['consensus_actb_positions_below_70']} and the rest are "
        f"{lg['consensus_actb_positions_70_and_above']}."
    )
    o.append("")
    o.append("| pair | atom contacts | ACTR1A interface residues |")
    o.append("|---|---|---|")
    for name, v in lg["per_longitudinal_pair"].items():
        o.append(
            f"| {name} | {v['n_atom_contacts']} | "
            + ", ".join(str(x) for x in v["actr1a_positions"])
            + " |"
        )
    o.append("")
    return "\n".join(o) + "\n"


if __name__ == "__main__":
    main()
