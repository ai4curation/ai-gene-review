"""Bioinformatics audit supporting the GO review of human ACTL7B (Q9Y614).

Two independent analyses, each with its own JSON output under ``results/``:

``propagation``
    Rebuilds, **from the GOA TSV itself**, the WITH/FROM set of every IBA/ISS/IEA row,
    resolves each token to UniProt (reporting Swiss-Prot vs TrEMBL status, and *every*
    hit when a cross-reference is ambiguous rather than silently taking the first), and
    asks QuickGO what evidence each source carries for the *propagated* term. It also
    reads the cached PANTHER PAINT table for the family so that the ancestral-node
    annotations behind each IBA -- including PAINT's own ``IRD`` (negated) calls -- are
    reported rather than guessed.

``residues``
    Asks whether ACTL7B retains the residues conventional actin uses to bind nucleotide
    and to polymerise. The residue sets are **computed from deposited structures**, not
    hardcoded: nucleotide contacts from a G-actin/ATP crystal structure and from an
    F-actin cryo-EM structure, and protomer-protomer interface residues from the
    inter-chain contacts of the F-actin structure. Each set is then scored across a panel
    of actin-family proteins (conventional actins, cytoplasmic ARPs, nuclear ARPs, and
    the ACTL7 clade) by global pairwise alignment, so ACTL7B is placed on a scale rather
    than judged in isolation.

``report``
    Renders RESULTS.md from the two JSON files. RESULTS.md is deterministic: fetch
    timestamps live in the JSON only, so a fresh run reproduces the committed file byte
    for byte unless an upstream database has changed.

Missing *inputs* are hard errors that name the fix. Ambiguous *data* (a cross-reference
with several hits, a source with no annotation to the propagated term) is reported, not
raised: an ambiguous cross-reference is a finding.
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

import requests
import typer
from Bio.Align import PairwiseAligner, substitution_matrices
from Bio.PDB import MMCIFParser, NeighborSearch
from Bio.PDB.MMCIF2Dict import MMCIF2Dict
from Bio.PDB.Polypeptide import is_aa

HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent
REPO_ROOT = GENE_DIR.parents[2]
GOA_TSV = GENE_DIR / "ACTL7B-goa.tsv"
PAINT_TSV = REPO_ROOT / "interpro" / "panther" / "PTHR11937" / "PTHR11937-paint.tsv"
CACHE = HERE / "data"
RESULTS = HERE / "results"

QUERY_ACC = "Q9Y614"

# Experimental evidence codes per the GO consortium.
EXPERIMENTAL_CODES = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP", "HTP", "HDA", "HMP", "HGI", "HEP"}

# Panel members are labelled only with the role we are testing; every *identity* claim
# (name, gene symbol, organism, review status) is fetched from UniProt at run time.
PANEL: list[tuple[str, str]] = [
    ("Q9Y614", "query (human ACTL7B)"),
    ("Q9QY83", "ACTL7 clade: mouse ortholog"),
    ("Q9Y615", "ACTL7 clade: human paralog"),
    ("Q9QY84", "ACTL7 clade: mouse paralog"),
    ("P60709", "conventional actin"),
    ("P68133", "conventional actin"),
    ("P60010", "conventional actin (yeast)"),
    ("P61160", "cytoplasmic ARP (Arp2/3 complex)"),
    ("P61158", "cytoplasmic ARP (Arp2/3 complex)"),
    ("O96019", "nuclear ARP (SWI/SNF-family)"),
    ("Q9H9F9", "nuclear ARP (INO80 complex)"),
    ("Q9H981", "nuclear ARP (INO80 complex)"),
    ("Q05123", "nuclear ARP (yeast RSC/SWI-SNF)"),
    ("Q12406", "nuclear ARP (yeast RSC/SWI-SNF)"),
]

# Structures used to derive residue sets. Chain selection is computed, not assumed.
STRUCTURES = {
    "1ATN": {
        "role": "G-actin monomer with ATP (X-ray)",
        "nucleotide_hetero": ["ATP", "CA", "MG"],
        "filament": False,
    },
    "8A2S": {
        "role": "F-actin filament, Mg-ADP-Pi state (cryo-EM)",
        "nucleotide_hetero": ["ADP", "PO4", "MG"],
        "filament": True,
    },
}

CONTACT_CUTOFF = 4.0  # Angstrom, heavy atoms
INTERFACE_CUTOFF = 4.5  # Angstrom, heavy atoms, between protomers

THREE_TO_ONE = {
    "ALA": "A", "ARG": "R", "ASN": "N", "ASP": "D", "CYS": "C", "GLN": "Q", "GLU": "E",
    "GLY": "G", "HIS": "H", "ILE": "I", "LEU": "L", "LYS": "K", "MET": "M", "PHE": "F",
    "PRO": "P", "SER": "S", "THR": "T", "TRP": "W", "TYR": "Y", "VAL": "V",
    "MSE": "M", "HIC": "H",
}

app = typer.Typer(add_completion=False, help=__doc__)


def _die(message: str) -> None:
    """Abort loudly. Used only for missing inputs, never for ambiguous data."""
    raise SystemExit(f"FATAL: {message}")


def _get(url: str, **kwargs) -> requests.Response:
    response = requests.get(url, timeout=120, **kwargs)
    if response.status_code != 200:
        _die(f"HTTP {response.status_code} for {url}\n{response.text[:400]}")
    return response


def _cached(name: str, url: str, **kwargs) -> str:
    CACHE.mkdir(parents=True, exist_ok=True)
    path = CACHE / name
    if path.exists():
        return path.read_text()
    text = _get(url, **kwargs).text
    path.write_text(text)
    return text


# ---------------------------------------------------------------------------
# Part 1: propagation audit
# ---------------------------------------------------------------------------


@dataclass
class GoaRow:
    index: int
    go_id: str
    go_name: str
    aspect: str
    evidence: str
    reference: str
    qualifier: str
    with_from: list[str] = field(default_factory=list)


def read_goa() -> list[GoaRow]:
    if not GOA_TSV.exists():
        _die(f"{GOA_TSV} is missing. Run: just fetch-gene human ACTL7B")
    lines = GOA_TSV.read_text().strip().split("\n")
    header = lines[0].split("\t")
    col = {name: i for i, name in enumerate(header)}
    required = ["GO TERM", "GO NAME", "GO ASPECT", "GO EVIDENCE CODE", "REFERENCE", "WITH/FROM", "QUALIFIER"]
    missing = [c for c in required if c not in col]
    if missing:
        _die(f"{GOA_TSV} lacks expected columns {missing}; header was {header}")
    rows = []
    for i, line in enumerate(lines[1:], start=1):
        f = line.split("\t")
        raw = f[col["WITH/FROM"]].strip()
        tokens = [t for t in raw.split("|") if t]
        rows.append(
            GoaRow(
                index=i,
                go_id=f[col["GO TERM"]],
                go_name=f[col["GO NAME"]],
                aspect=f[col["GO ASPECT"]],
                evidence=f[col["GO EVIDENCE CODE"]],
                reference=f[col["REFERENCE"]],
                qualifier=f[col["QUALIFIER"]],
                with_from=tokens,
            )
        )
    return rows


XREF_DB = {
    "MGI": "mgi",
    "SGD": "sgd",
    "RGD": "rgd",
    "CGD": "cgd",
    "FB": "flybase",
    "WB": "wormbase",
    "ZFIN": "zfin",
    "PomBase": "pombase",
    "dictyBase": "dictybase",
}


def _uniprot_summary(entry: dict) -> dict:
    desc = entry.get("proteinDescription", {})
    name = desc.get("recommendedName", {}).get("fullName", {}).get("value")
    if not name:
        alt = [s.get("fullName", {}).get("value") for s in desc.get("submissionNames", [])]
        name = alt[0] if alt else None
    return {
        "accession": entry.get("primaryAccession"),
        "uniprot_id": entry.get("uniProtkbId"),
        "review_status": "Swiss-Prot" if entry.get("entryType", "").endswith("(Swiss-Prot)") else "TrEMBL",
        "organism": entry.get("organism", {}).get("scientificName"),
        "protein_name": name,
        "gene": [g.get("geneName", {}).get("value") for g in entry.get("genes", [])],
    }


def resolve_token(token: str) -> dict:
    """Resolve one WITH/FROM token. Multi-hit is reported, never collapsed."""
    out: dict = {"token": token, "kind": None, "hits": [], "note": None}
    if token.startswith("PANTHER:PTN"):
        out["kind"] = "panther_tree_node"
        out["note"] = "internal PANTHER tree node, not a protein"
        return out
    if token.startswith("UniProtKB-SubCell:"):
        out["kind"] = "subcell_keyword"
        out["note"] = "UniProt controlled-vocabulary subcellular-location term, not a protein"
        return out
    if token.startswith("GO:"):
        out["kind"] = "go_term"
        out["note"] = "inter-ontology logical inference from another GO term, not a protein"
        return out
    if token.startswith("UniProtKB:"):
        acc = token.split(":", 1)[1]
        base = acc.split("-")[0]
        data = json.loads(
            _cached(
                f"uniprot_{base}.json",
                f"https://rest.uniprot.org/uniprotkb/{base}.json",
                params={"fields": "accession,id,protein_name,gene_names,organism_name,reviewed"},
            )
        )
        out["kind"] = "uniprot"
        out["hits"] = [_uniprot_summary(data)]
        if acc != base:
            out["note"] = f"isoform-level accession {acc}"
        return out
    db, _, local = token.partition(":")
    if db in XREF_DB:
        ident = local
        if ident.startswith(db + ":"):  # MGI tokens arrive as MGI:MGI:1343051
            ident = ident.split(":", 1)[1]
        payload = json.loads(
            _cached(
                f"xref_{XREF_DB[db]}_{ident}.json",
                "https://rest.uniprot.org/uniprotkb/search",
                params={
                    "query": f"xref:{XREF_DB[db]}-{ident}",
                    "size": 5,
                    "fields": "accession,id,protein_name,gene_names,organism_name,reviewed",
                },
            )
        )
        hits = [_uniprot_summary(h) for h in payload.get("results", [])]
        out["kind"] = "model_organism_db"
        out["hits"] = hits
        if len(hits) == 0:
            out["note"] = "no UniProt entry cross-referenced to this identifier"
        elif len(hits) > 1:
            out["note"] = f"AMBIGUOUS: {len(hits)} UniProt entries share this cross-reference"
        return out
    out["kind"] = "unrecognised"
    out["note"] = "token format not recognised by this resolver"
    return out


def quickgo_evidence(accession: str, go_id: str) -> dict:
    payload = json.loads(
        _cached(
            f"quickgo_{accession}_{go_id.replace(':', '')}.json",
            "https://www.ebi.ac.uk/QuickGO/services/annotation/search",
            params={
                "geneProductId": f"UniProtKB:{accession}",
                "goId": go_id,
                "goUsage": "descendants",
                "goUsageRelationships": "is_a,part_of",
                "limit": 100,
            },
            headers={"Accept": "application/json"},
        )
    )
    if payload.get("messages"):
        return {"queried": True, "error": payload["messages"], "annotations": []}
    anns = [
        {
            "go_id": r["goId"],
            "evidence": r["goEvidence"],
            "reference": r["reference"],
            "qualifier": r.get("qualifier"),
        }
        for r in payload.get("results", [])
    ]
    codes = sorted({a["evidence"] for a in anns})
    return {
        "queried": True,
        "n_annotations": len(anns),
        "evidence_codes": codes,
        "has_own_experimental": bool(EXPERIMENTAL_CODES & set(codes)),
        "annotations": anns,
    }


def read_paint(nodes: set[str]) -> dict[str, list[dict]]:
    if not PAINT_TSV.exists():
        _die(f"{PAINT_TSV} is missing. Run: just fetch-gene human ACTL7B")
    lines = PAINT_TSV.read_text().strip().split("\n")
    header = lines[0].split("\t")
    col = {n: i for i, n in enumerate(header)}
    out: dict[str, list[dict]] = {n: [] for n in nodes}
    for line in lines[1:]:
        f = line.split("\t")
        node = f[col["node"]]
        if node not in nodes:
            continue
        out[node].append(
            {
                "go_id": f[col["go_id"]],
                "aspect": f[col["aspect"]],
                "evidence": f[col["evidence"]],
                "negated": f[col["negated"]] == "true",
                "seeds": [s for s in f[col["seeds"]].split("|") if s],
                "taxon": f[col["taxon"]],
                "date": f[col["date"]],
            }
        )
    return out


@app.command()
def propagation() -> None:
    """Resolve every WITH/FROM token and query the evidence each source carries."""
    rows = read_goa()
    total_tokens = sum(len(r.with_from) for r in rows)
    resolved: dict[str, dict] = {}
    per_row = []
    panther_nodes: set[str] = set()

    for row in rows:
        entry = {
            "goa_row": row.index,
            "go_id": row.go_id,
            "go_name": row.go_name,
            "aspect": row.aspect,
            "qualifier": row.qualifier,
            "evidence": row.evidence,
            "reference": row.reference,
            "with_from": row.with_from,
            "sources": [],
        }
        for token in row.with_from:
            if token not in resolved:
                resolved[token] = resolve_token(token)
            info = dict(resolved[token])
            if info["kind"] == "panther_tree_node":
                panther_nodes.add(token.split(":", 1)[1])
            source_ev = []
            for hit in info["hits"]:
                source_ev.append(
                    {
                        **hit,
                        "evidence_for_propagated_term": quickgo_evidence(hit["accession"], row.go_id),
                    }
                )
            info["hits"] = source_ev
            entry["sources"].append(info)
        # Counts must match GOA by construction.
        assert len(entry["sources"]) == len(row.with_from), (
            f"row {row.index}: built {len(entry['sources'])} sources for "
            f"{len(row.with_from)} WITH/FROM tokens"
        )
        per_row.append(entry)

    assert sum(len(e["sources"]) for e in per_row) == total_tokens, "token count drifted from GOA"

    paint = read_paint(panther_nodes)
    # Seeds of the ancestral nodes are themselves worth resolving: they are the ultimate
    # origin of an IBA that lists only tree nodes in WITH/FROM.
    seed_resolution: dict[str, dict] = {}
    for node, annotations in paint.items():
        for ann in annotations:
            for seed in ann["seeds"]:
                if seed not in seed_resolution:
                    seed_resolution[seed] = resolve_token(seed)

    out = {
        "fetched": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "gene": "ACTL7B",
        "accession": QUERY_ACC,
        "goa_rows": len(rows),
        "with_from_tokens": total_tokens,
        "rows": per_row,
        "panther_nodes": paint,
        "panther_seed_identities": seed_resolution,
    }
    RESULTS.mkdir(parents=True, exist_ok=True)
    (RESULTS / "propagation_audit.json").write_text(json.dumps(out, indent=2) + "\n")
    print(f"wrote {RESULTS / 'propagation_audit.json'} ({len(rows)} rows, {total_tokens} tokens)")


# ---------------------------------------------------------------------------
# Part 2: actin residue audit
# ---------------------------------------------------------------------------


def fetch_fasta(acc: str) -> str:
    text = _cached(f"seq_{acc}.fasta", f"https://rest.uniprot.org/uniprotkb/{acc}.fasta")
    return "".join(line.strip() for line in text.split("\n") if line and not line.startswith(">"))


def fetch_entry(acc: str) -> dict:
    return json.loads(
        _cached(
            f"uniprot_{acc}.json",
            f"https://rest.uniprot.org/uniprotkb/{acc}.json",
            params={"fields": "accession,id,protein_name,gene_names,organism_name,reviewed"},
        )
    )


def _as_list(value) -> list[str]:
    if isinstance(value, list):
        return value
    return [value]


def load_structure(pdb_id: str) -> dict:
    """Return SEQRES sequences per auth chain, an auth->seq_id map, and the model."""
    path = CACHE / f"{pdb_id}.cif"
    if not path.exists():
        CACHE.mkdir(parents=True, exist_ok=True)
        path.write_text(_get(f"https://files.rcsb.org/download/{pdb_id}.cif").text)
    mmcif = MMCIF2Dict(str(path))
    if "_entity_poly.entity_id" not in mmcif:
        _die(f"{path} has no _entity_poly block; re-download it")
    entity_seq = dict(
        zip(
            _as_list(mmcif["_entity_poly.entity_id"]),
            [s.replace("\n", "").replace(";", "") for s in _as_list(mmcif["_entity_poly.pdbx_seq_one_letter_code_can"])],
        )
    )
    scheme_keys = [
        "_pdbx_poly_seq_scheme.entity_id",
        "_pdbx_poly_seq_scheme.seq_id",
        "_pdbx_poly_seq_scheme.pdb_strand_id",
        "_pdbx_poly_seq_scheme.pdb_seq_num",
    ]
    for key in scheme_keys:
        if key not in mmcif:
            _die(f"{path} lacks {key}; cannot map auth numbering to SEQRES")
    chain_entity: dict[str, str] = {}
    auth_to_seqid: dict[tuple[str, int], int] = {}
    for ent, seq_id, strand, pdb_num in zip(*[_as_list(mmcif[k]) for k in scheme_keys]):
        chain_entity[strand] = ent
        if pdb_num in (".", "?"):
            continue
        auth_to_seqid[(strand, int(pdb_num))] = int(seq_id)
    structure = MMCIFParser(QUIET=True).get_structure(pdb_id, str(path))
    model = next(structure.get_models())
    return {
        "pdb_id": pdb_id,
        "model": model,
        "chain_seq": {c: entity_seq[e] for c, e in chain_entity.items() if e in entity_seq},
        "auth_to_seqid": auth_to_seqid,
    }


def make_aligner() -> PairwiseAligner:
    aligner = PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -11
    aligner.extend_gap_score = -1
    aligner.mode = "global"
    return aligner


def align_map(aligner: PairwiseAligner, ref: str, target: str) -> tuple[dict[int, int], float]:
    """Map 1-based ref positions to 1-based target positions; also return % identity."""
    alignment = aligner.align(ref, target)[0]
    mapping: dict[int, int] = {}
    identities = 0
    aligned_cols = 0
    for (r0, r1), (t0, t1) in zip(*alignment.aligned):
        r0, r1, t0 = int(r0), int(r1), int(t0)
        for offset in range(r1 - r0):
            mapping[r0 + offset + 1] = t0 + offset + 1
            aligned_cols += 1
            if ref[r0 + offset] == target[t0 + offset]:
                identities += 1
    pct = 100.0 * identities / min(len(ref), len(target))
    return mapping, round(pct, 1)


def identify_actin_chains(struct: dict, actin_seq: str, aligner: PairwiseAligner) -> list[str]:
    """Chains whose SEQRES aligns to conventional actin above 50% identity."""
    chains = []
    for chain, seq in struct["chain_seq"].items():
        if len(seq) < 100:
            continue
        _, pct = align_map(aligner, actin_seq, seq)
        if pct >= 50.0:
            chains.append((chain, pct))
    return [c for c, _ in sorted(chains, key=lambda x: -x[1])]


def ligand_contacts(struct: dict, chain_id: str, hetero: list[str], cutoff: float) -> dict[int, list[str]]:
    """SEQRES positions of chain_id contacting any listed hetero group."""
    model = struct["model"]
    ligand_atoms = [
        atom
        for residue in model.get_residues()
        if residue.get_resname().strip() in hetero
        for atom in residue
        if atom.element != "H"
    ]
    if not ligand_atoms:
        _die(f"{struct['pdb_id']}: none of the hetero groups {hetero} were found in the model")
    protein_atoms = [
        atom
        for residue in model[chain_id]
        if is_aa(residue, standard=False)
        for atom in residue
        if atom.element != "H"
    ]
    search = NeighborSearch(ligand_atoms)
    hits: dict[int, list[str]] = {}
    for atom in protein_atoms:
        if not search.search(atom.coord, cutoff):
            continue
        residue = atom.get_parent()
        auth = residue.id[1]
        seq_id = struct["auth_to_seqid"].get((chain_id, auth))
        if seq_id is None:
            continue
        hits.setdefault(seq_id, []).append(residue.get_resname())
    return {k: sorted(set(v)) for k, v in sorted(hits.items())}


def interface_contacts(struct: dict, chain_id: str, other_chains: list[str], cutoff: float) -> dict[int, list[str]]:
    """SEQRES positions of chain_id within cutoff of a different actin protomer."""
    model = struct["model"]
    other_atoms = [
        atom
        for other in other_chains
        for residue in model[other]
        if is_aa(residue, standard=False)
        for atom in residue
        if atom.element != "H"
    ]
    if not other_atoms:
        _die(f"{struct['pdb_id']}: no atoms found in partner chains {other_chains}")
    search = NeighborSearch(other_atoms)
    hits: dict[int, list[str]] = {}
    for residue in model[chain_id]:
        if not is_aa(residue, standard=False):
            continue
        seq_id = struct["auth_to_seqid"].get((chain_id, residue.id[1]))
        if seq_id is None:
            continue
        for atom in residue:
            if atom.element == "H":
                continue
            if search.search(atom.coord, cutoff):
                hits.setdefault(seq_id, []).append(residue.get_resname())
                break
    return {k: sorted(set(v)) for k, v in sorted(hits.items())}


def score_set(
    aligner: PairwiseAligner,
    ref_seq: str,
    positions: list[int],
    panel_seqs: dict[str, str],
) -> dict:
    matrix = substitution_matrices.load("BLOSUM62")
    out: dict = {"n_positions": len(positions), "per_protein": {}}
    for acc, seq in panel_seqs.items():
        mapping, pct_id = align_map(aligner, ref_seq, seq)
        identical = similar = different = gaps = 0
        detail = []
        for pos in positions:
            ref_aa = ref_seq[pos - 1]
            tgt_pos = mapping.get(pos)
            if tgt_pos is None:
                gaps += 1
                detail.append({"ref_pos": pos, "ref_aa": ref_aa, "aa": "-", "class": "gap"})
                continue
            tgt_aa = seq[tgt_pos - 1]
            if tgt_aa == ref_aa:
                identical += 1
                cls = "identical"
            elif matrix[ref_aa, tgt_aa] > 0:
                similar += 1
                cls = "similar"
            else:
                different += 1
                cls = "different"
            detail.append({"ref_pos": pos, "ref_aa": ref_aa, "target_pos": tgt_pos, "aa": tgt_aa, "class": cls})
        out["per_protein"][acc] = {
            "global_pct_identity_to_structure_seq": pct_id,
            "identical": identical,
            "similar": similar,
            "different": different,
            "gap": gaps,
            "pct_identical": round(100.0 * identical / len(positions), 1),
            "pct_identical_or_similar": round(100.0 * (identical + similar) / len(positions), 1),
            "detail": detail,
        }
    return out


@app.command()
def residues() -> None:
    """Score ACTL7B against structure-derived actin nucleotide and interface residues."""
    aligner = make_aligner()
    panel_meta = {}
    panel_seqs = {}
    for acc, role in PANEL:
        entry = fetch_entry(acc)
        panel_meta[acc] = {**_uniprot_summary(entry), "panel_role": role}
        panel_seqs[acc] = fetch_fasta(acc)

    actb = panel_seqs["P60709"]
    sets_out = {}
    for pdb_id, spec in STRUCTURES.items():
        struct = load_structure(pdb_id)
        actin_chains = identify_actin_chains(struct, actb, aligner)
        if not actin_chains:
            _die(f"{pdb_id}: no chain aligned to conventional actin above 50% identity")
        if spec["filament"]:
            # Use the protomer with the most inter-chain contacts (avoids filament ends).
            counts = {
                c: len(interface_contacts(struct, c, [o for o in actin_chains if o != c], INTERFACE_CUTOFF))
                for c in actin_chains
            }
            chain = max(counts, key=lambda c: counts[c])
        else:
            chain = actin_chains[0]
        ref_seq = struct["chain_seq"][chain]
        nuc = ligand_contacts(struct, chain, spec["nucleotide_hetero"], CONTACT_CUTOFF)
        record = {
            "pdb_id": pdb_id,
            "role": spec["role"],
            "actin_chains": actin_chains,
            "chain_analysed": chain,
            "seqres_length": len(ref_seq),
            "nucleotide_hetero_groups": spec["nucleotide_hetero"],
            "nucleotide_contact_positions": sorted(nuc),
            "nucleotide_contacts": score_set(aligner, ref_seq, sorted(nuc), panel_seqs),
        }
        if spec["filament"]:
            others = [c for c in actin_chains if c != chain]
            iface = interface_contacts(struct, chain, others, INTERFACE_CUTOFF)
            record["interface_partner_chains"] = others
            record["interface_contact_positions"] = sorted(iface)
            record["interface_contacts"] = score_set(aligner, ref_seq, sorted(iface), panel_seqs)
        sets_out[pdb_id] = record

    # Whole-protein pairwise identity matrix, ACTL7B against the panel.
    query = panel_seqs[QUERY_ACC]
    matrix_rows = {}
    for acc, seq in panel_seqs.items():
        _, pct = align_map(aligner, query, seq)
        matrix_rows[acc] = pct

    out = {
        "fetched": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "contact_cutoff_angstrom": CONTACT_CUTOFF,
        "interface_cutoff_angstrom": INTERFACE_CUTOFF,
        "panel": panel_meta,
        "panel_lengths": {a: len(s) for a, s in panel_seqs.items()},
        "identity_to_ACTL7B_pct": matrix_rows,
        "structures": sets_out,
    }
    RESULTS.mkdir(parents=True, exist_ok=True)
    (RESULTS / "residue_audit.json").write_text(json.dumps(out, indent=2) + "\n")
    print(f"wrote {RESULTS / 'residue_audit.json'}")


# ---------------------------------------------------------------------------
# Part 3: report
# ---------------------------------------------------------------------------


def _label(meta: dict) -> str:
    genes = [g for g in meta.get("gene", []) if g]
    gene = genes[0] if genes else "?"
    org = (meta.get("organism") or "").split(" (")[0]
    return f"{gene} ({org})"


def contact_segments(positions: list[int], max_gap: int = 2) -> list[list[int]]:
    """Group contact positions into contiguous structural segments (data-derived)."""
    segments: list[list[int]] = []
    for pos in positions:
        if segments and pos - segments[-1][-1] <= max_gap:
            segments[-1].append(pos)
        else:
            segments.append([pos])
    return segments


def _md_table(header: list[str], rows: list[list[str]]) -> str:
    out = ["| " + " | ".join(header) + " |", "|" + "|".join(["---"] * len(header)) + "|"]
    for row in rows:
        out.append("| " + " | ".join(row) + " |")
    return "\n".join(out)


@app.command()
def report() -> None:
    """Render RESULTS.md from the JSON outputs (deterministic; no timestamps)."""
    prop_path = RESULTS / "propagation_audit.json"
    res_path = RESULTS / "residue_audit.json"
    for path, cmd in [(prop_path, "propagation"), (res_path, "residues")]:
        if not path.exists():
            _die(f"{path} is missing. Run: python analyze.py {cmd}")
    prop = json.loads(prop_path.read_text())
    res = json.loads(res_path.read_text())

    lines: list[str] = []
    lines.append("# ACTL7B bioinformatics audit")
    lines.append("")
    lines.append(
        "Generated by `analyze.py` (`propagation`, `residues`, `report`). Regenerate with "
        "`uv run --project . python analyze.py all` from this directory; fetch timestamps are "
        "in `results/*.json` so this file is byte-reproducible."
    )
    lines.append("")
    lines.append("## 1. Where every ACTL7B annotation comes from")
    lines.append("")
    lines.append(
        f"All {prop['goa_rows']} rows of `ACTL7B-goa.tsv` and all {prop['with_from_tokens']} "
        "WITH/FROM tokens were parsed from the TSV and resolved. For every token that resolves "
        "to a protein, QuickGO was asked what evidence *that protein* carries for the term being "
        "propagated (term plus `is_a`/`part_of` descendants)."
    )
    lines.append("")
    rows = []
    for row in prop["rows"]:
        for src in row["sources"]:
            if not src["hits"]:
                rows.append(
                    [
                        str(row["goa_row"]),
                        f"{row['go_id']} {row['go_name']}",
                        row["evidence"],
                        f"`{src['token']}`",
                        "-",
                        "-",
                        src["note"] or "",
                    ]
                )
                continue
            for hit in src["hits"]:
                ev = hit["evidence_for_propagated_term"]
                codes = ",".join(ev.get("evidence_codes") or []) or "none"
                own = "yes" if ev.get("has_own_experimental") else "no"
                rows.append(
                    [
                        str(row["goa_row"]),
                        f"{row['go_id']} {row['go_name']}",
                        row["evidence"],
                        f"`{src['token']}`",
                        f"{_label(hit)} {hit['accession']} [{hit['review_status']}]",
                        f"{codes} (own experimental: {own})",
                        src["note"] or "",
                    ]
                )
    lines.append(
        _md_table(
            ["GOA row", "term", "code", "WITH/FROM token", "resolves to", "source's evidence for this term", "note"],
            rows,
        )
    )
    lines.append("")
    lines.append("### Ancestral PANTHER nodes cited by the IBA rows")
    lines.append("")
    lines.append(
        "Read from the cached PAINT table `interpro/panther/PTHR11937/PTHR11937-paint.tsv`. "
        "`IRD` rows with `negated=true` are PAINT's own explicit *rejections* of a term for that "
        "clade."
    )
    lines.append("")
    node_rows = []
    for node, anns in sorted(prop["panther_nodes"].items()):
        for ann in anns:
            seed_labels = []
            for seed in ann["seeds"]:
                info = prop["panther_seed_identities"].get(seed, {})
                hits = info.get("hits") or []
                seed_labels.append(_label(hits[0]) if hits else seed)
            node_rows.append(
                [
                    node,
                    ann["go_id"],
                    ann["aspect"],
                    ann["evidence"] + (" (NEGATED)" if ann["negated"] else ""),
                    ", ".join(seed_labels) or "-",
                ]
            )
    lines.append(_md_table(["node", "term", "aspect", "PAINT evidence", "seeds"], node_rows))
    lines.append("")

    lines.append("## 2. Does ACTL7B retain actin's nucleotide and polymerisation residues?")
    lines.append("")
    lines.append(
        "Residue sets are computed from deposited structures, then scored across an actin-family "
        "panel by global BLOSUM62 alignment. Contact cutoffs: "
        f"{res['contact_cutoff_angstrom']} A to nucleotide/ion heavy atoms, "
        f"{res['interface_cutoff_angstrom']} A between protomers."
    )
    lines.append("")
    lines.append("### Panel")
    lines.append("")
    panel_rows = []
    for acc, meta in res["panel"].items():
        panel_rows.append(
            [
                acc,
                _label(meta),
                meta["protein_name"] or "?",
                meta["review_status"],
                str(res["panel_lengths"][acc]),
                meta["panel_role"],
                f"{res['identity_to_ACTL7B_pct'][acc]}",
            ]
        )
    lines.append(
        _md_table(
            ["accession", "gene", "UniProt name", "status", "length", "role in this panel", "% id to ACTL7B"],
            panel_rows,
        )
    )
    lines.append("")
    for pdb_id, rec in res["structures"].items():
        lines.append(f"### {pdb_id} - {rec['role']}")
        lines.append("")
        lines.append(
            f"Actin chains detected: {', '.join(rec['actin_chains'])}; chain analysed: "
            f"{rec['chain_analysed']} ({rec['seqres_length']} SEQRES residues). "
            f"Nucleotide/ion groups: {', '.join(rec['nucleotide_hetero_groups'])}."
        )
        lines.append("")
        blocks = [("nucleotide contacts", rec["nucleotide_contacts"], rec["nucleotide_contact_positions"])]
        if "interface_contacts" in rec:
            blocks.append(
                ("protomer-protomer interface", rec["interface_contacts"], rec["interface_contact_positions"])
            )
        for title, block, positions in blocks:
            lines.append(f"**{title}** - {block['n_positions']} positions: {positions}")
            lines.append("")
            score_rows = []
            for acc, meta in res["panel"].items():
                s = block["per_protein"][acc]
                score_rows.append(
                    [
                        _label(res["panel"][acc]),
                        meta["panel_role"],
                        f"{s['global_pct_identity_to_structure_seq']}",
                        f"{s['identical']}",
                        f"{s['similar']}",
                        f"{s['different']}",
                        f"{s['gap']}",
                        f"{s['pct_identical']}",
                        f"{s['pct_identical_or_similar']}",
                    ]
                )
            lines.append(
                _md_table(
                    [
                        "protein",
                        "role",
                        "% id to whole structure seq",
                        "identical",
                        "similar",
                        "different",
                        "gap",
                        "% identical",
                        "% id+sim",
                    ],
                    score_rows,
                )
            )
            lines.append("")
        query_detail = rec["nucleotide_contacts"]["per_protein"][QUERY_ACC]["detail"]
        lines.append(
            f"Per-position nucleotide contacts in ACTL7B ({pdb_id} numbering -> ACTL7B): "
            + ", ".join(
                f"{d['ref_aa']}{d['ref_pos']}->{d['aa']}"
                + (str(d.get("target_pos")) if d.get("target_pos") else "")
                for d in query_detail
            )
        )
        lines.append("")
        if "interface_contacts" in rec:
            lines.append(
                "Interface contacts broken into contiguous segments (segments are derived from the "
                "contact positions themselves, not from named literature regions):"
            )
            lines.append("")
            seg_rows = []
            detail_by_pos = {
                acc: {d["ref_pos"]: d for d in rec["interface_contacts"]["per_protein"][acc]["detail"]}
                for acc in (QUERY_ACC, "Q9Y615", "P60709")
            }
            for seg in contact_segments(rec["interface_contact_positions"]):
                def summarise(acc: str) -> str:
                    ds = [detail_by_pos[acc][p] for p in seg]
                    n_id = sum(1 for d in ds if d["class"] == "identical")
                    return f"{n_id}/{len(seg)}"

                seg_rows.append(
                    [
                        f"{seg[0]}-{seg[-1]}" if len(seg) > 1 else str(seg[0]),
                        str(len(seg)),
                        "".join(detail_by_pos[QUERY_ACC][p]["ref_aa"] for p in seg),
                        "".join(detail_by_pos[QUERY_ACC][p]["aa"] for p in seg),
                        summarise(QUERY_ACC),
                        summarise("Q9Y615"),
                        summarise("P60709"),
                    ]
                )
            lines.append(
                _md_table(
                    [
                        "segment",
                        "n",
                        "actin residues",
                        "ACTL7B residues",
                        "identical ACTL7B",
                        "identical ACTL7A",
                        "identical ACTB",
                    ],
                    seg_rows,
                )
            )
            lines.append("")

    (HERE / "RESULTS.md").write_text("\n".join(lines) + "\n")
    print(f"wrote {HERE / 'RESULTS.md'}")


@app.command("all")
def run_all() -> None:
    """Run propagation, residues, report."""
    propagation()
    residues()
    report()


if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.argv.append("all")
    app()
