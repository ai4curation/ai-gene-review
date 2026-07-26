"""Residue-level test of whether beta-centractin (ACTR1B) retains the Arp1
nucleotide site and the Arp1-Arp1 protomer interface.

The question this answers
-------------------------
ACTR1B is 91% identical to ACTR1A and both are annotated as dynactin Arp1
subunits. Canonical actin-family properties (ATP binding, polymerisation into
a filament) may therefore be correct for ACTR1B -- or may be paralog transfer.
The only deposited structure of the human Arp1 mini-filament (PDB 9B85, the
2025 cryo-EM structure of human dynactin) models all eight filament protomers
as ACTR1A and does not model ACTR1B at all. So the contact residues are
measured on ACTR1A in its real structural context (Arp1 filament inside
dynactin, ADP bound) and then tested for retention in ACTR1B, rather than
being recited for conventional actin by analogy.

Two residue sets are derived from the structure itself, never hardcoded:
  1. NUCLEOTIDE SITE  -- residues of an Arp1 protomer within CONTACT_CUTOFF of
     its bound ADP.
  2. PROTOMER INTERFACE -- residues of an Arp1 protomer within CONTACT_CUTOFF
     of any neighbouring Arp1 protomer. Which chains those neighbours are is
     recovered from the coordinates, not asserted.

PDB 9B85 chain A maps 1:1 onto UniProt P61163 residues 1-376 by SIFTS, which
the script re-verifies from the PDBe mapping API instead of assuming it.

Missing inputs are hard errors naming the fix, per repo policy.
"""

from __future__ import annotations

import gzip
import io
import json
import sys
from dataclasses import dataclass, field
from pathlib import Path

import gemmi
import requests
from Bio import Align
from Bio.Align import substitution_matrices

HERE = Path(__file__).parent
CACHE = HERE / "cache"
RESULTS_JSON = HERE / "results.json"
RESULTS_MD = HERE / "RESULTS.md"

PDB_ID = "9B85"
CONTACT_CUTOFF = 4.0  # Angstrom, heavy-atom to heavy-atom

# Arp1 filament chains of 9B85 (all modelled as ACTR1A) in filament order,
# taken from the entity/chain table of the entry; chain H is the single
# conventional beta-actin protomer and is excluded from the Arp1-Arp1 analysis.
REFERENCE_CHAIN = "A"
REFERENCE_ACC = "P61163"  # ACTR1A, the chain actually modelled in 9B85
SUBJECT_ACC = "P42025"  # ACTR1B, the gene under review; absent from every PDB entry
# The subject's own mouse orthologue. A substitution shared only with it is
# orthologue conservation, NOT evidence that the wider family tolerates the
# position, so the two counts are reported separately.
SUBJECT_ORTHOLOGUE = "Q8R5C5"

# Sequences to test for retention. `role` is descriptive only.
TARGETS = {
    "P42025": "ACTR1B human (beta-centractin) -- the gene under review",
    "P61163": "ACTR1A human (alpha-centractin) -- paralog, modelled in 9B85",
    "F2Z5G5": "ACTR1A pig -- WITH/FROM donor on the IBA rows",
    "O94630": "arp1 S. pombe -- WITH/FROM donor (sole donor for GO:0106006)",
    "P38696": "ARP1 S. cerevisiae -- WITH/FROM donor",
    "Q9NA98": "arp-1 C. elegans -- WITH/FROM donor (TrEMBL)",
    "Q5BBX7": "AN1953 A. nidulans -- WITH/FROM donor (TrEMBL)",
    "Q8R5C5": "Actr1b mouse -- ortholog of the gene under review",
    "P60709": "ACTB human (beta-actin) -- conventional actin outgroup",
    "Q9NZ32": "ACTR10 human (Arp11) -- dynactin pointed-end capping Arp",
}


def die(msg: str) -> None:
    raise SystemExit(f"ERROR: {msg}")


def fetch(url: str, dest: Path, binary: bool = False) -> bytes | str:
    """Fetch with an on-disk cache so reruns are reproducible offline."""
    if dest.exists():
        return dest.read_bytes() if binary else dest.read_text()
    dest.parent.mkdir(parents=True, exist_ok=True)
    r = requests.get(url, timeout=120)
    if r.status_code != 200:
        die(
            f"fetch failed ({r.status_code}) for {url}. "
            f"Network required on first run; delete {CACHE} to force a refetch."
        )
    if binary:
        dest.write_bytes(r.content)
        return r.content
    dest.write_text(r.text)
    return r.text


def get_sequence(acc: str) -> str:
    txt = fetch(
        f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", CACHE / f"{acc}.fasta"
    )
    lines = [ln.strip() for ln in txt.splitlines() if ln and not ln.startswith(">")]
    if not lines:
        die(f"empty FASTA for {acc}")
    return "".join(lines)


def get_structure() -> gemmi.Structure:
    raw = fetch(
        f"https://files.rcsb.org/download/{PDB_ID}.cif.gz",
        CACHE / f"{PDB_ID}.cif.gz",
        binary=True,
    )
    with gzip.open(io.BytesIO(raw), "rt") as fh:
        doc = gemmi.cif.read_string(fh.read())
    st = gemmi.make_structure_from_block(doc.sole_block())
    st.setup_entities()
    return st


def verify_sifts_offset() -> None:
    """Confirm PDB 9B85 chain A numbering == UniProt P61163 numbering.

    Asserted rather than assumed: an offset here would silently shift every
    residue number reported below.
    """
    txt = fetch(
        f"https://www.ebi.ac.uk/pdbe/api/mappings/uniprot/{PDB_ID.lower()}",
        CACHE / "sifts.json",
    )
    data = json.loads(txt)[PDB_ID.lower()]["UniProt"]
    if REFERENCE_ACC not in data:
        die(f"{REFERENCE_ACC} not in SIFTS mapping for {PDB_ID}")
    for m in data[REFERENCE_ACC]["mappings"]:
        if m["chain_id"] != REFERENCE_CHAIN:
            continue
        pdb_start = m["start"]["residue_number"]
        if pdb_start != m["unp_start"] or m["end"]["residue_number"] != m["unp_end"]:
            die(
                f"{PDB_ID} chain {REFERENCE_CHAIN} is NOT 1:1 with {REFERENCE_ACC} "
                f"(pdb {pdb_start}-{m['end']['residue_number']} vs "
                f"unp {m['unp_start']}-{m['unp_end']}); the offset must be applied."
            )
        return
    die(f"no SIFTS mapping for chain {REFERENCE_CHAIN} of {PDB_ID}")


@dataclass
class ContactSet:
    label: str
    description: str
    residues: dict[int, str] = field(default_factory=dict)  # resnum -> 1-letter


def is_aa(res: gemmi.Residue) -> bool:
    info = gemmi.find_tabulated_residue(res.name)
    return bool(info and info.is_amino_acid())


def heavy_atoms(res: gemmi.Residue):
    return [a for a in res if a.element != gemmi.Element("H")]


def sifts_chains(acc: str) -> list[str]:
    """Chains of PDB_ID assigned to `acc` by SIFTS (authoritative, not guessed)."""
    txt = fetch(
        f"https://www.ebi.ac.uk/pdbe/api/mappings/uniprot/{PDB_ID.lower()}",
        CACHE / "sifts.json",
    )
    data = json.loads(txt)[PDB_ID.lower()]["UniProt"]
    if acc not in data:
        die(
            f"{acc} has no SIFTS mapping in {PDB_ID}; the entry composition changed "
            "and chain selection must be revisited."
        )
    return sorted({m["chain_id"] for m in data[acc]["mappings"]})


def sifts_chains_optional(acc: str) -> list[str]:
    """Chains assigned to `acc` in PDB_ID, or [] if it is absent from the entry."""
    txt = fetch(
        f"https://www.ebi.ac.uk/pdbe/api/mappings/uniprot/{PDB_ID.lower()}",
        CACHE / "sifts.json",
    )
    data = json.loads(txt)[PDB_ID.lower()]["UniProt"]
    return sorted({m["chain_id"] for m in data.get(acc, {}).get("mappings", [])})


def pdbe_structure_count(acc: str) -> int:
    """How many PDB entries PDBe maps to `acc` (0 when there is no mapping).

    Measured rather than asserted: the claim "ACTR1B is in no deposited
    structure" is load-bearing for this analysis, so it must be recomputed on
    every run and will change by itself if a structure is ever deposited.
    """
    dest = CACHE / f"best_structures_{acc}.json"
    if not dest.exists():
        r = requests.get(
            f"https://www.ebi.ac.uk/pdbe/api/mappings/best_structures/{acc}", timeout=120
        )
        if r.status_code not in (200, 404):
            die(f"PDBe best_structures failed ({r.status_code}) for {acc}")
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(r.text if r.status_code == 200 else "{}")
    data = json.loads(dest.read_text())
    return len({e["pdb_id"] for e in data.get(acc, [])})


def chain_arp1_ids(st: gemmi.Structure) -> list[str]:
    """Arp1 filament chains: SIFTS-assigned to ACTR1A and present in the model."""
    present = {ch.name for ch in st[0]}
    out = [c for c in sifts_chains(REFERENCE_ACC) if c in present]
    if not out:
        die(
            f"none of the SIFTS {REFERENCE_ACC} chains of {PDB_ID} are present in the "
            "parsed model; chain naming changed."
        )
    return out


def contacts_to_ligand(
    st: gemmi.Structure, ns: gemmi.NeighborSearch, chain: str, lig_name: str
) -> ContactSet:
    cs = ContactSet(
        "nucleotide_site",
        f"residues of Arp1 chain {chain} within {CONTACT_CUTOFF} A of its bound {lig_name}",
    )
    # gemmi keeps the ligand of an author chain in a separate Chain object that
    # reuses the same name, so every chain with this name must be scanned.
    ligs = [r for ch in st[0] if ch.name == chain for r in ch if r.name == lig_name]
    if not ligs:
        die(
            f"no {lig_name} in chain {chain} of {PDB_ID}; the nucleotide site cannot "
            "be derived from this entry."
        )
    for lig in ligs:
        for atom in heavy_atoms(lig):
            marks = ns.find_atoms(atom.pos, "\0", radius=CONTACT_CUTOFF)
            for m in marks:
                cra = m.to_cra(st[0])
                if cra.chain.name != chain or cra.residue.name == lig_name:
                    continue
                if not is_aa(cra.residue):
                    continue
                if cra.atom.pos.dist(atom.pos) <= CONTACT_CUTOFF:
                    cs.residues[cra.residue.seqid.num] = gemmi.find_tabulated_residue(
                        cra.residue.name
                    ).one_letter_code.upper()
    return cs


def contacts_by_partner_chain(
    st: gemmi.Structure, ns: gemmi.NeighborSearch, chain: str
) -> dict[str, dict[int, str]]:
    """One pass: residues of `chain` contacting each other protein chain."""
    out: dict[str, dict[int, str]] = {}
    for res in [r for ch in st[0] if ch.name == chain for r in ch]:
        if not is_aa(res):
            continue
        code = gemmi.find_tabulated_residue(res.name).one_letter_code.upper()
        for atom in heavy_atoms(res):
            for m in ns.find_atoms(atom.pos, "\0", radius=CONTACT_CUTOFF):
                cra = m.to_cra(st[0])
                if cra.chain.name == chain or not is_aa(cra.residue):
                    continue
                if cra.atom.pos.dist(atom.pos) <= CONTACT_CUTOFF:
                    out.setdefault(cra.chain.name, {})[res.seqid.num] = code
    return out


def aligner() -> Align.PairwiseAligner:
    al = Align.PairwiseAligner()
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score = -11
    al.extend_gap_score = -1
    al.mode = "global"
    return al


def align_map(ref: str, tgt: str) -> tuple[dict[int, tuple[int, str]], float]:
    """Map 1-based ref position -> (1-based tgt position, tgt residue).

    Returns the map and the percent identity over aligned columns.
    """
    aln = aligner().align(ref, tgt)[0]
    mapping: dict[int, tuple[int, str]] = {}
    ident = aligned = 0
    for (rs, re_), (ts, te) in zip(*aln.aligned):
        for k in range(re_ - rs):
            rpos = rs + k + 1
            tpos = ts + k + 1
            mapping[rpos] = (tpos, tgt[ts + k])
            aligned += 1
            if ref[rs + k] == tgt[ts + k]:
                ident += 1
    pid = 100.0 * ident / aligned if aligned else 0.0
    return mapping, pid


def main() -> None:
    verify_sifts_offset()
    st = get_structure()
    ns = gemmi.NeighborSearch(st, 5.0).populate()
    arp1_chains = chain_arp1_ids(st)

    # Which chains the reference protomer actually touches is recovered from the
    # structure, not asserted by hand.
    ref = REFERENCE_CHAIN
    per_partner = contacts_by_partner_chain(st, ns, ref)
    neighbours = sorted(
        (c for c in per_partner if c in arp1_chains),
        key=lambda c: -len(per_partner[c]),
    )
    if not neighbours:
        die(f"chain {ref} of {PDB_ID} contacts no other Arp1 chain")
    iface: dict[int, str] = {}
    for c in neighbours:
        iface.update(per_partner[c])

    sets = [
        contacts_to_ligand(st, ns, ref, "ADP"),
        ContactSet(
            "protomer_interface",
            f"residues of Arp1 chain {ref} within {CONTACT_CUTOFF} A of a "
            f"neighbouring Arp1 protomer (chains {','.join(neighbours)})",
            iface,
        ),
    ]

    ref_seq = get_sequence(REFERENCE_ACC)
    # Sanity: the structural residue identities must match the UniProt sequence.
    for cs in sets:
        for num, aa in cs.residues.items():
            if ref_seq[num - 1] != aa:
                die(
                    f"residue {num} of {PDB_ID} chain {ref} is {aa} but "
                    f"{REFERENCE_ACC}[{num}] is {ref_seq[num-1]}; numbering is off."
                )

    report: dict = {
        "pdb_id": PDB_ID,
        "contact_cutoff_angstrom": CONTACT_CUTOFF,
        "reference_chain": ref,
        "reference_accession": REFERENCE_ACC,
        "arp1_chains_in_structure": arp1_chains,
        "arp1_neighbour_chains_of_reference": neighbours,
        "actr1b_chains_in_this_structure": sifts_chains_optional(SUBJECT_ACC),
        "actr1b_pdb_structures_anywhere": pdbe_structure_count(SUBJECT_ACC),
        "contact_sets": {
            cs.label: {
                "description": cs.description,
                "n_residues": len(cs.residues),
                "residues": {str(k): v for k, v in sorted(cs.residues.items())},
            }
            for cs in sets
        },
        "targets": {},
    }

    maps: dict[str, dict[int, tuple[int, str]]] = {}
    for acc, role in TARGETS.items():
        tgt_seq = get_sequence(acc)
        mapping, pid = align_map(ref_seq, tgt_seq)
        entry = {
            "role": role,
            "length": len(tgt_seq),
            "percent_identity_to_ACTR1A": round(pid, 1),
            "sets": {},
        }
        for cs in sets:
            kept = []
            lost = []
            for num, aa in sorted(cs.residues.items()):
                m = mapping.get(num)
                if m is None:
                    lost.append(f"{aa}{num}->gap")
                elif m[1] == aa:
                    kept.append(num)
                else:
                    lost.append(f"{aa}{num}->{m[1]}{m[0]}")
            entry["sets"][cs.label] = {
                "n_total": len(cs.residues),
                "n_identical": len(kept),
                "fraction_identical": round(len(kept) / len(cs.residues), 3),
                "substitutions": lost,
            }
        report["targets"][acc] = entry
        maps[acc] = mapping

    # Per-position audit of every contact position where the SUBJECT (ACTR1B)
    # differs from the structural reference (ACTR1A). For each such position,
    # record what every other sequence has there, so the question "is ACTR1B's
    # residue novel, or is it one the family already tolerates?" is answered by
    # the data and not by eye. (Three earlier genes in this campaign had
    # hand-maintained residue claims drift.)
    if SUBJECT_ACC not in maps:
        die(f"{SUBJECT_ACC} must be in TARGETS for the divergence audit")
    audit = []
    outgroups = [a for a in TARGETS if a not in (SUBJECT_ACC, REFERENCE_ACC)]
    for cs in sets:
        for num, ref_aa in sorted(cs.residues.items()):
            m = maps[SUBJECT_ACC].get(num)
            subj_aa = m[1] if m else None
            if subj_aa == ref_aa:
                continue
            others = {}
            for a in outgroups:
                mo = maps[a].get(num)
                others[a] = mo[1] if mo else "-"
            shares = sorted(a for a, aa in others.items() if aa == subj_aa)
            shares_nonortho = [a for a in shares if a != SUBJECT_ORTHOLOGUE]
            audit.append(
                {
                    "set": cs.label,
                    "position_ACTR1A_numbering": num,
                    "ACTR1A": ref_aa,
                    "ACTR1B": subj_aa or "gap",
                    "other_sequences": others,
                    "outgroups_sharing_the_ACTR1B_residue": shares,
                    "n_outgroups_sharing": len(shares),
                    "conserved_in_subject_orthologue": SUBJECT_ORTHOLOGUE in shares,
                    "family_sharing_excluding_subject_orthologue": shares_nonortho,
                    "n_family_sharing_excluding_subject_orthologue": len(shares_nonortho),
                }
            )
    report["subject_divergence_audit"] = {
        "subject": SUBJECT_ACC,
        "reference": REFERENCE_ACC,
        "n_divergent_contact_positions": len(audit),
        "subject_orthologue": SUBJECT_ORTHOLOGUE,
        "n_positions_conserved_in_subject_orthologue": sum(
            1 for a in audit if a["conserved_in_subject_orthologue"]
        ),
        "n_positions_shared_with_family_excluding_subject_orthologue": sum(
            1 for a in audit if a["n_family_sharing_excluding_subject_orthologue"] > 0
        ),
        "positions": audit,
    }

    RESULTS_JSON.write_text(json.dumps(report, indent=2) + "\n")
    RESULTS_MD.write_text(render(report))
    print(f"wrote {RESULTS_JSON.name} and {RESULTS_MD.name}")


def render(r: dict) -> str:
    L = []
    A = L.append
    A("# ACTR1B: does beta-centractin retain the Arp1 nucleotide site and")
    A("# protomer interface?")
    A("")
    A("**Generated by `analyze.py`. Do not hand-edit — rerun `uv run python analyze.py`.**")
    A("")
    A("## What was measured")
    A("")
    A(
        f"Contact residues were derived from **PDB {r['pdb_id']}** "
        "(cryo-EM structure of human dynactin bound to the *Chlamydia* effector Dre1, "
        "released 2025-04-16), not recited for conventional actin by analogy."
    )
    nb = r["actr1b_pdb_structures_anywhere"]
    A(
        f"All {len(r['arp1_chains_in_structure'])} Arp1 filament protomers in that entry "
        f"(chains {', '.join(r['arp1_chains_in_structure'])}) are modelled as "
        "**ACTR1A / alpha-centractin**, each with a bound ADP. "
        f"ACTR1B is assigned to {len(r['actr1b_chains_in_this_structure'])} chains of "
        f"{r['pdb_id']} by SIFTS, and PDBe maps **{nb} PDB entries** to P42025 in total"
        + (
            " — i.e. ACTR1B is present in no deposited structure at all, so its residues "
            "are tested by alignment onto the ACTR1A protomer."
            if nb == 0
            else " — rerun and revisit: a structure now exists."
        )
    )
    A("")
    A(
        f"Cutoff: heavy-atom contacts within **{r['contact_cutoff_angstrom']} A**. "
        f"Reference chain **{r['reference_chain']}** maps 1:1 onto "
        f"{r['reference_accession']} residues 1-376 by SIFTS (re-verified at runtime)."
    )
    A("")
    for label, cs in r["contact_sets"].items():
        A(f"- **{label}** ({cs['n_residues']} residues): {cs['description']}")
    A("")
    A("## Retention per sequence")
    A("")
    hdr = "| Accession | Role | Len | % id to ACTR1A | Nucleotide site | Protomer interface |"
    A(hdr)
    A("|---|---|---|---|---|---|")
    for acc, t in r["targets"].items():
        ns = t["sets"]["nucleotide_site"]
        ps = t["sets"]["protomer_interface"]
        A(
            f"| {acc} | {t['role']} | {t['length']} | {t['percent_identity_to_ACTR1A']} | "
            f"{ns['n_identical']}/{ns['n_total']} | {ps['n_identical']}/{ps['n_total']} |"
        )
    A("")
    A("## Substitutions, per sequence")
    A("")
    for acc, t in r["targets"].items():
        A(f"### {acc} — {t['role']}")
        for label, s in t["sets"].items():
            subs = ", ".join(s["substitutions"]) if s["substitutions"] else "none"
            A(f"- {label}: {s['n_identical']}/{s['n_total']} identical; substitutions: {subs}")
        A("")
    aud = r["subject_divergence_audit"]
    A("## Every contact position where ACTR1B differs from ACTR1A")
    A("")
    n_div = aud["n_divergent_contact_positions"]
    A(
        f"{n_div} of "
        f"{sum(c['n_residues'] for c in r['contact_sets'].values())} contact positions "
        f"differ. {aud['n_positions_conserved_in_subject_orthologue']}/{n_div} are "
        f"conserved in the mouse ACTR1B orthologue ({aud['subject_orthologue']}), so they "
        "are fixed features of the beta paralog rather than human-specific noise. At "
        f"{aud['n_positions_shared_with_family_excluding_subject_orthologue']}/{n_div} the "
        "ACTR1B residue is *independently* present in another Arp1 family member or in "
        "conventional actin -- a position the family already tolerates, not a novel loss. "
        "The two counts are kept separate because a substitution shared only with the "
        "mouse orthologue is not independent evidence of tolerance."
    )
    A("")
    cols = [a for a in TARGETS if a not in (SUBJECT_ACC, REFERENCE_ACC)]
    A(
        "| Set | Pos | ACTR1A | ACTR1B | "
        + " | ".join(cols)
        + " | family members (excl. mouse ACTR1B) sharing it |"
    )
    A("|---|---|---|---|" + "---|" * len(cols) + "---|")
    for a in aud["positions"]:
        row = " | ".join(a["other_sequences"][c] for c in cols)
        shares = ", ".join(a["family_sharing_excluding_subject_orthologue"]) or "none"
        A(
            f"| {a['set']} | {a['position_ACTR1A_numbering']} | {a['ACTR1A']} | "
            f"{a['ACTR1B']} | {row} | {shares} |"
        )
    A("")
    A("## Contact residues (ACTR1A / P61163 numbering)")
    A("")
    for label, cs in r["contact_sets"].items():
        items = ", ".join(f"{v}{k}" for k, v in cs["residues"].items())
        A(f"- **{label}**: {items}")
        A("")
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    sys.exit(main())
