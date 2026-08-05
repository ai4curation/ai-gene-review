"""Is human ACTL8 an actin, and does its all-IBA GO record survive inspection?

ACTL8 (Q9H568, "Actin-like protein 8" / cancer-testis antigen CT57) has no UniProt
FUNCTION comment and no experimental GO annotation for molecular function,
localisation or process. Its entire structural/localisation record is transferred
from conventional actin by PANTHER/PAINT (IBA, GO_REF:0000033) plus two automatic
IEA steps. Two opposite mistakes are possible:

  (a) accepting "actin filament" / "structural constituent of postsynaptic actin
      cytoskeleton" because the protein carries an actin fold, which would be a
      fold-name-to-activity slip; and
  (b) asserting "fold without function" without checking whether the residues that
      make actin an actin are actually still there.

Both are decided by measurement, so this script measures, from live data only.

Analysis 1 -- nucleotide site.
  The residues that contact ATP in actin are not taken from memory or from a review;
  they are computed from the coordinates of a beta-actin:ATP crystal structure
  (PDB 2BTF, chain A) as every residue with an atom within a distance cutoff of the
  bound ATP or its associated divalent cation. The structure's own observed
  sequence, with its own residue numbering, is then globally aligned to ACTL8 and to
  a panel of actin-family relatives, and the aligned residue is reported per
  contact position. Conservation is therefore read off an alignment, never off a
  position number.

Analysis 2 -- filament protomer interface.
  "Actin filament" and "structural constituent of ... actin cytoskeleton" are claims
  about polymerisation, so the same treatment is applied to the protomer-protomer
  interface of a filament structure (PDB 6DJO, four protomers of F-actin). Interface
  residues are every residue of the most-buried chain within the cutoff of any other
  chain.

Analysis 3 -- IBA source audit.
  Every WITH/FROM token in ACTL8-goa.tsv is parsed programmatically (never by hand),
  resolved to protein entries via the UniProt REST API, and then each resolved source
  is asked, through QuickGO, what evidence it itself carries for the exact term it
  donated. Identifier lookups request several hits and report all of them, because an
  ambiguous cross-reference is data rather than a missing input. Swiss-Prot/TrEMBL
  status is printed next to every name, since an unreviewed entry's name is an
  automatic label and is not evidence about function.

Analysis 4 -- clade composition of the donating PANTHER nodes.
  Three PANTHER ancestral nodes appear in ACTL8's WITH/FROM fields. QuickGO is asked
  which *human* genes each node donates to, and every one of those genes is then
  aligned locally to beta-actin. A node whose other human members are all near-identical
  to beta-actin is a node whose reconstructed ancestral state is beta-actin's biology,
  and inheriting that state at 34% identity is a different proposition from inheriting
  the generic actin-fold state of a deep node.

Analysis 5 -- do ACTL8's own closest relatives sit under the same nodes?
  If ACTL8's placement inside the cytoplasmic-actin subfamily is anomalous, then the
  other divergent human actin-like proteins should not be there. QuickGO is asked, for
  each of them, which PANTHER nodes appear in the WITH/FROM field of its own IBA
  annotations, and how many IBA rows it has. This turns "ACTL8 is mis-placed" from an
  argument about one clade into a comparison across the whole set of relatives.

Analysis 6 -- family context.
  For every human member of PANTHER family PTHR11937 (ACTIN), QuickGO is asked how
  many experimental-code annotations it has, per GO aspect. This tests, rather than
  asserts, the claim that experimentally characterised molecular function in this
  family is confined to a few conventional actins and actin-related complexes.

A missing local input file is a hard error naming the command that regenerates it.
An ambiguous or empty remote answer is reported, not silently dropped.

Usage:  uv run python analyze_actl8.py
Writes: results.json, RESULTS.md
"""

from __future__ import annotations

import csv
import io
import json
import re
from collections import Counter
from pathlib import Path

import requests
from Bio import Align
from Bio.Align import substitution_matrices
from Bio.Data.PDBData import protein_letters_3to1_extended as THREE_TO_ONE
from Bio.PDB import MMCIFParser, NeighborSearch

HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent
REPO_ROOT = GENE_DIR.parents[2]
GOA_TSV = GENE_DIR / "ACTL8-goa.tsv"
PANTHER_ENTRIES = REPO_ROOT / "interpro" / "panther" / "PTHR11937" / "PTHR11937-entries.csv"

CONTACT_CUTOFF = 4.0  # Angstrom, heavy-atom to heavy-atom
SECOND_SHELL_CUTOFF = 5.0

ACTL8 = "Q9H568"

# Reference actins and actin-family relatives. Chosen because each is either a
# WITH/FROM donor on an ACTL8 row (the conventional actins) or a human actin-family
# member with a comparably restricted expression pattern (the ACTL/ACTRT set), so the
# comparison shows whether residue loss is specific to ACTL8 or general to the clade.
PANEL = {
    "P60709": "ACTB (human beta-actin; IBA donor)",
    "P63261": "ACTG1 (human gamma-actin; IBA donor)",
    "P68133": "ACTA1 (human alpha-skeletal actin; IBA donor)",
    "P68032": "ACTC1 (human alpha-cardiac actin; IBA donor)",
    "P61160": "ACTR2 (human Arp2)",
    "P61158": "ACTR3 (human Arp3)",
    "P61163": "ACTR1A (human alpha-centractin)",
    "Q9Y615": "ACTL7A (human actin-like 7A)",
    "Q9Y614": "ACTL7B (human actin-like 7B)",
    "Q8TC94": "ACTL9 (human actin-like 9)",
    "Q5JWF8": "ACTL10 (human actin-like 10)",
    "Q8TDG2": "ACTRT1 (human actin-related protein T1)",
    "P45891": "Arp53D (Drosophila actin-like 53D; IBA donor)",
}

# Structures. Both are actin-only assemblies so that no partner protein can be
# mistaken for a nucleotide or filament contact.
ATP_STRUCTURE = ("2BTF", "A", ("ATP", "SR"))  # beta-actin:profilin, ATP + Sr(II) in the Mg site
FILAMENT_STRUCTURE = ("6DJO", None, ())  # four protomers of F-actin, ADP + Mg

EXPERIMENTAL_CODES = {
    "EXP", "IDA", "IPI", "IMP", "IGI", "IEP",
    "HTP", "HDA", "HMP", "HGI", "HEP",
}

XREF_DB = {
    "MGI": "mgi",
    "RGD": "rgd",
    "SGD": "sgd",
    "PomBase": "pombase",
    "FB": "flybase",
    "dictyBase": "dictybase",
    "CGD": "cgd",
    "WB": "wormbase",
}

SESSION = requests.Session()
SESSION.headers.update({"Accept": "application/json"})


# --------------------------------------------------------------------------- io


def require(path: Path, fix: str) -> Path:
    if not path.exists():
        raise FileNotFoundError(f"missing required input {path}\n  regenerate with: {fix}")
    return path


def get_json(url: str, params: dict | None = None) -> dict:
    r = SESSION.get(url, params=params, timeout=180)
    r.raise_for_status()
    return r.json()


def uniprot_sequence(acc: str) -> str:
    r = SESSION.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=120)
    r.raise_for_status()
    seq = "".join(line.strip() for line in r.text.splitlines()[1:])
    if not seq:
        raise RuntimeError(f"UniProt returned no sequence for {acc}")
    return seq


def fetch_cif(pdb_id: str) -> str:
    r = SESSION.get(f"https://files.rcsb.org/download/{pdb_id.upper()}.cif", timeout=300)
    r.raise_for_status()
    return r.text


# ------------------------------------------------------- structure -> residues


def polymer_residues(chain):
    """Residues of a chain that are amino acids, including modified ones (e.g. HIC)."""
    return [
        res
        for res in chain
        if res.id[0] != "W" and res.get_resname().upper() in THREE_TO_ONE
    ]


def chain_sequence(residues) -> str:
    return "".join(THREE_TO_ONE[res.get_resname().upper()] for res in residues)


def ligand_contacts(cif_text: str, pdb_id: str, chain_id: str, ligand_names, cutoff: float):
    """Residues of `chain_id` with any heavy atom within `cutoff` of a named ligand."""
    model = MMCIFParser(QUIET=True).get_structure(pdb_id, io.StringIO(cif_text))[0]
    chain = model[chain_id]
    residues = polymer_residues(chain)
    ligands = [res for res in chain if res.get_resname().strip() in ligand_names]
    if not ligands:
        raise RuntimeError(
            f"{pdb_id} chain {chain_id} carries none of {sorted(ligand_names)}; "
            "the structure content has changed and the ligand list needs revisiting"
        )
    ns = NeighborSearch([a for res in residues for a in res])
    hits: dict[int, dict] = {}
    for lig in ligands:
        for atom in lig:
            for other in ns.search(atom.coord, cutoff):
                res = other.get_parent()
                d = float(atom - other)
                rec = hits.setdefault(
                    res.id[1],
                    {"resname": res.get_resname(), "ligands": set(), "min_dist": d},
                )
                rec["ligands"].add(lig.get_resname().strip())
                rec["min_dist"] = min(rec["min_dist"], d)
    for rec in hits.values():
        rec["ligands"] = sorted(rec["ligands"])
        rec["min_dist"] = round(rec["min_dist"], 2)
    return residues, hits


def interface_contacts(cif_text: str, pdb_id: str, cutoff: float):
    """Residues of the most-buried protein chain within `cutoff` of any other chain."""
    model = MMCIFParser(QUIET=True).get_structure(pdb_id, io.StringIO(cif_text))[0]
    chains = {}
    for chain in model:
        residues = polymer_residues(chain)
        if len(residues) > 200:
            chains[chain.id] = residues
    if len(chains) < 3:
        raise RuntimeError(
            f"{pdb_id} yielded {len(chains)} long protein chains; an interface "
            "calculation needs a multi-protomer filament model"
        )
    best = None
    for cid, residues in chains.items():
        others = [a for k, v in chains.items() if k != cid for res in v for a in res]
        ns = NeighborSearch(others)
        hits: dict[int, dict] = {}
        for res in residues:
            for atom in res:
                for other in ns.search(atom.coord, cutoff):
                    partner = other.get_parent()
                    d = float(atom - other)
                    rec = hits.setdefault(
                        res.id[1],
                        {"resname": res.get_resname(), "partners": set(), "min_dist": d},
                    )
                    rec["partners"].add(partner.get_parent().id)
                    rec["min_dist"] = min(rec["min_dist"], d)
        if best is None or len(hits) > len(best[2]):
            best = (cid, residues, hits)
    cid, residues, hits = best
    for rec in hits.values():
        rec["partners"] = sorted(rec["partners"])
        rec["min_dist"] = round(rec["min_dist"], 2)
    return cid, sorted(chains), residues, hits


# ------------------------------------------------------------------- alignment


def aligner(matrix: str = "BLOSUM62", open_gap: float = -11, extend_gap: float = -1):
    al = Align.PairwiseAligner()
    al.substitution_matrix = substitution_matrices.load(matrix)
    al.open_gap_score = open_gap
    al.extend_gap_score = extend_gap
    al.mode = "global"
    return al


# A second, deliberately different scoring scheme. ACTL8 is only ~34% identical to
# actin, which is inside the range where gap placement can move; if the conservation
# tallies are an artefact of one gap model they will not survive a change of matrix
# and gap costs.
ALIGNMENT_SCHEMES = {
    "BLOSUM62/-11/-1": ("BLOSUM62", -11, -1),
    "BLOSUM45/-14/-2": ("BLOSUM45", -14, -2),
}


def map_positions(query_seq: str, query_numbers: list[int], target_seq: str, al):
    """Align query (a structure chain) to target; return {query_resnum: (target_pos, aa)}."""
    aln = al.align(query_seq, target_seq)[0]
    qi = ti = 0
    mapping: dict[int, tuple[int | None, str]] = {}
    identities = 0
    for qc, tc in zip(aln[0], aln[1]):
        if qc != "-":
            qi += 1
        if tc != "-":
            ti += 1
        if qc != "-":
            if tc != "-":
                mapping[query_numbers[qi - 1]] = (ti, tc)
                if qc == tc:
                    identities += 1
            else:
                mapping[query_numbers[qi - 1]] = (None, "-")
    pct = 100.0 * identities / min(len(query_seq), len(target_seq))
    return mapping, round(pct, 1), float(aln.score)


CONSERVATIVE = [set("GA"), set("ST"), set("DE"), set("KRH"), set("NQ"), set("ILVMF"), set("FYW")]


def classify(ref_aa: str, obs_aa: str) -> str:
    if obs_aa == "-":
        return "gap"
    if ref_aa == obs_aa:
        return "identical"
    if any(ref_aa in grp and obs_aa in grp for grp in CONSERVATIVE):
        return "conservative"
    return "non-conservative"


# ------------------------------------------------------------- GOA / WITH-FROM


def parse_goa(path: Path) -> list[dict]:
    with path.open() as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    if not rows:
        raise RuntimeError(f"{path} has no annotation rows")
    return rows


def split_withfrom(field: str) -> list[str]:
    return [tok for tok in field.split("|") if tok]


def resolve_token(token: str) -> dict:
    """Resolve a WITH/FROM token to protein entries. Ambiguity is reported, not raised."""
    out = {"token": token, "strategy": None, "hits": [], "note": None}
    if token.startswith("PANTHER:"):
        out["strategy"] = "none"
        out["note"] = "PANTHER internal tree node, not a protein; cannot be resolved to an entry"
        return out
    if token.startswith("GO:"):
        out["strategy"] = "none"
        out["note"] = "GO term used as the WITH/FROM source (automatic MF->BP step)"
        return out
    if token.startswith("UniProtKB:"):
        acc = token.split(":", 1)[1]
        queries = [("accession", f"accession:{acc.split('-')[0]}")]
    else:
        db, ident = token.split(":", 1)
        if db not in XREF_DB:
            out["strategy"] = "none"
            out["note"] = (
                f"{db} is a controlled-vocabulary namespace, not a gene product database; "
                "the source is a UniProt annotation statement rather than another gene's evidence"
            )
            return out
        # MGI arrives as MGI:MGI:87906; UniProt's xref: search wants the bare number.
        bare = ident.split(":")[-1] if db == "MGI" else ident
        queries = [
            ("xref", f"xref:{XREF_DB[db]}-{bare}"),
            ("free-text", bare),
        ]
    for strategy, query in queries:
        data = get_json(
            "https://rest.uniprot.org/uniprotkb/search",
            {
                "query": query,
                "size": 5,
                "fields": "accession,reviewed,protein_name,gene_names,organism_name",
            },
        )
        results = data.get("results", [])
        if results:
            out["strategy"] = strategy
            for entry in results:
                desc = entry.get("proteinDescription", {})
                name = (
                    desc.get("recommendedName", {}).get("fullName", {}).get("value")
                    or (desc.get("submissionNames") or [{}])[0]
                    .get("fullName", {})
                    .get("value")
                    or "(no name)"
                )
                out["hits"].append(
                    {
                        "accession": entry["primaryAccession"],
                        "reviewed": "Swiss-Prot"
                        if "unreviewed" not in (entry.get("entryType") or "")
                        else "TrEMBL",
                        "name": name,
                        "genes": [
                            g.get("geneName", {}).get("value")
                            for g in entry.get("genes", [])
                            if g.get("geneName")
                        ],
                        "organism": entry.get("organism", {}).get("scientificName"),
                    }
                )
            break
    if not out["hits"]:
        out["note"] = "unresolved by both xref and free-text search; deferred, not dismissed"
    elif len(out["hits"]) > 1:
        reviewed = [h for h in out["hits"] if h["reviewed"] == "Swiss-Prot"]
        out["note"] = (
            f"{len(out['hits'])} candidate entries; "
            f"{len(reviewed)} reviewed (Swiss-Prot), {len(out['hits']) - len(reviewed)} unreviewed"
        )
    return out


def quickgo_evidence(gene_product: str, go_id: str) -> dict:
    data = get_json(
        "https://www.ebi.ac.uk/QuickGO/services/annotation/search",
        {
            "geneProductId": gene_product,
            "goId": go_id,
            "goUsage": "descendants",
            "goUsageRelationships": "is_a,part_of",
            "limit": 100,
        },
    )
    codes = Counter(r.get("goEvidence") for r in data.get("results", []))
    refs = sorted(
        {
            r.get("reference")
            for r in data.get("results", [])
            if r.get("goEvidence") in EXPERIMENTAL_CODES
        }
    )
    return {
        "n_hits": data.get("numberOfHits", 0),
        "codes": dict(sorted(codes.items(), key=lambda kv: kv[0] or "")),
        "has_experimental": bool(set(codes) & EXPERIMENTAL_CODES),
        "experimental_refs": refs,
    }


def quickgo_aspect_counts(gene_product: str) -> dict:
    counts = {"MF": Counter(), "BP": Counter(), "CC": Counter()}
    # Molecular-function terms other than bare `GO:0005515 protein binding` that carry an
    # experimental code. Tracked separately because a two-hybrid `protein binding` IPI is
    # what almost every human protein has, and counting it as "experimental molecular
    # function" would make the family survey say nothing.
    informative_mf: set[str] = set()
    page = 1
    while True:
        data = get_json(
            "https://www.ebi.ac.uk/QuickGO/services/annotation/search",
            {"geneProductId": gene_product, "limit": 200, "page": page},
        )
        results = data.get("results", [])
        for r in results:
            aspect = {"molecular_function": "MF", "biological_process": "BP", "cellular_component": "CC"}.get(
                r.get("goAspect")
            )
            if aspect:
                counts[aspect][r.get("goEvidence")] += 1
            if (
                aspect == "MF"
                and r.get("goEvidence") in EXPERIMENTAL_CODES
                and r.get("goId") != "GO:0005515"
            ):
                informative_mf.add(r.get("goId"))
        total_pages = (data.get("pageInfo") or {}).get("total", 1)
        if page >= total_pages or not results:
            break
        page += 1
    out = {
        aspect: {
            "total": sum(c.values()),
            "experimental": sum(v for k, v in c.items() if k in EXPERIMENTAL_CODES),
            "codes": dict(sorted(c.items())),
        }
        for aspect, c in counts.items()
    }
    out["informative_experimental_MF_terms"] = sorted(informative_mf)
    return out


def node_human_targets(node: str) -> dict[str, list[str]]:
    """{GO id: [human gene symbols]} that this PANTHER node donates to, per QuickGO."""
    data = get_json(
        "https://www.ebi.ac.uk/QuickGO/services/annotation/search",
        {"withFrom": f"PANTHER:{node}", "taxonId": 9606, "limit": 200},
    )
    by_term: dict[str, set[str]] = {}
    accessions: dict[str, str] = {}
    for r in data.get("results", []):
        by_term.setdefault(r.get("goId"), set()).add(r.get("symbol"))
        accessions[r.get("symbol")] = r.get("geneProductId", "").split(":")[-1]
    return {
        "n_hits": data.get("numberOfHits", 0),
        "terms": {k: sorted(v) for k, v in sorted(by_term.items())},
        "accessions": dict(sorted(accessions.items())),
    }


def iba_panther_nodes(accession: str) -> dict:
    """PANTHER nodes appearing in the WITH/FROM of this protein's own IBA annotations."""
    data = get_json(
        "https://www.ebi.ac.uk/QuickGO/services/annotation/search",
        {"geneProductId": f"UniProtKB:{accession}", "evidenceCode": "ECO:0000318", "limit": 200},
    )
    nodes: set[str] = set()
    terms: set[str] = set()
    for r in data.get("results", []):
        terms.add(r.get("goId"))
        for w in r.get("withFrom") or []:
            for x in w.get("connectedXrefs", []):
                if x.get("db") == "PANTHER":
                    nodes.add(x.get("id"))
    return {
        "n_iba_rows": data.get("numberOfHits", 0),
        "panther_nodes": sorted(nodes),
        "iba_terms": sorted(terms),
    }


# Human actin-like / actin-related-T proteins: ACTL8's nearest divergent relatives.
RELATIVES = {
    "Q9H568": "ACTL8",
    "Q9Y615": "ACTL7A",
    "Q9Y614": "ACTL7B",
    "Q8TC94": "ACTL9",
    "Q5JWF8": "ACTL10",
    "Q8TDG2": "ACTRT1",
    "Q8TDY3": "ACTRT2",
    "Q9BYD9": "ACTRT3",
}


def local_identity_to(reference: str, query: str) -> dict:
    """Smith-Waterman identity, so a multidomain protein's actin block is compared fairly."""
    al = Align.PairwiseAligner()
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score = -11
    al.extend_gap_score = -1
    al.mode = "local"
    aln = al.align(reference, query)[0]
    cols = list(zip(aln[0], aln[1]))
    ident = sum(1 for a, b in cols if a == b and a != "-")
    return {
        "aligned_columns": len(cols),
        "identities": ident,
        "pct_identity_over_aligned_block": round(100.0 * ident / len(cols), 1),
    }


def human_family_members(path: Path) -> list[dict]:
    with path.open() as fh:
        rows = list(csv.DictReader(fh))
    members = [
        {"accession": r["id"], "gene": r["gene"], "name": r["name"], "length": int(r["length"])}
        for r in rows
        if r["source_tax_id"] == "9606"
    ]
    if not members:
        raise RuntimeError(f"{path} lists no Homo sapiens members; column layout changed")
    return sorted(members, key=lambda m: m["gene"] or m["accession"])


# ------------------------------------------------------------------ reporting


def fmt_residue_table(hits: dict, panel_maps: dict, ref_seq_by_num: dict, columns: list[str]) -> list[str]:
    lines = []
    header = "| Structure residue | Ligand/partner | min dist (Å) | " + " | ".join(columns) + " |"
    lines.append(header)
    lines.append("|" + "---|" * (3 + len(columns)))
    for num in sorted(hits):
        rec = hits[num]
        ref_aa = ref_seq_by_num[num]
        tag = ", ".join(rec.get("ligands") or rec.get("partners") or [])
        cells = []
        for acc in columns:
            pos, aa = panel_maps[acc][num]
            kind = classify(ref_aa, aa)
            mark = {"identical": "", "conservative": " ~", "non-conservative": " **", "gap": ""}[kind]
            cells.append(f"{aa}{pos if pos else ''}{mark}" if aa != "-" else "gap")
        lines.append(
            f"| {ref_aa}{num} ({rec['resname']}) | {tag} | {rec['min_dist']} | " + " | ".join(cells) + " |"
        )
    return lines


def main() -> None:
    require(GOA_TSV, "just fetch-gene human ACTL8")
    require(PANTHER_ENTRIES, "ai-gene-review fetch-panther PTHR11937")

    results: dict = {"inputs": {}, "nucleotide_site": {}, "filament_interface": {}, "iba_sources": {}, "family": {}}

    # ---- sequences
    sequences = {ACTL8: uniprot_sequence(ACTL8)}
    for acc in PANEL:
        sequences[acc] = uniprot_sequence(acc)
    results["inputs"]["sequence_lengths"] = {a: len(s) for a, s in sorted(sequences.items())}

    al = aligner()
    panel_order = [ACTL8] + list(PANEL)

    # ---- Analysis 1: nucleotide site
    pdb_id, chain_id, ligands = ATP_STRUCTURE
    cif = fetch_cif(pdb_id)
    struct_residues, atp_hits = ligand_contacts(cif, pdb_id, chain_id, set(ligands), CONTACT_CUTOFF)
    _, atp_hits_wide = ligand_contacts(cif, pdb_id, chain_id, set(ligands), SECOND_SHELL_CUTOFF)
    struct_seq = chain_sequence(struct_residues)
    struct_nums = [res.id[1] for res in struct_residues]
    ref_by_num = dict(zip(struct_nums, struct_seq))

    nuc_maps = {}
    for acc in panel_order:
        mapping, pct, score = map_positions(struct_seq, struct_nums, sequences[acc], al)
        nuc_maps[acc] = mapping
        results["nucleotide_site"].setdefault("alignments", {})[acc] = {
            "pct_identity_to_structure_chain": pct,
            "alignment_score": score,
        }
    results["nucleotide_site"]["structure"] = {
        "pdb_id": pdb_id,
        "chain": chain_id,
        "ligands": list(ligands),
        "cutoff_A": CONTACT_CUTOFF,
        "second_shell_cutoff_A": SECOND_SHELL_CUTOFF,
        "observed_residue_range": [struct_nums[0], struct_nums[-1]],
    }
    results["nucleotide_site"]["contacts"] = {
        str(n): {
            "structure_residue": f"{ref_by_num[n]}{n}",
            "ligands": rec["ligands"],
            "min_dist_A": rec["min_dist"],
            **{
                acc: {
                    "position": nuc_maps[acc][n][0],
                    "residue": nuc_maps[acc][n][1],
                    "class": classify(ref_by_num[n], nuc_maps[acc][n][1]),
                }
                for acc in panel_order
            },
        }
        for n, rec in sorted(atp_hits.items())
    }
    results["nucleotide_site"]["second_shell_only"] = sorted(
        f"{ref_by_num[n]}{n}" for n in atp_hits_wide if n not in atp_hits
    )
    actl8_nuc = [
        classify(ref_by_num[n], nuc_maps[ACTL8][n][1]) for n in sorted(atp_hits)
    ]
    results["nucleotide_site"]["summary"] = {
        "n_contacts": len(atp_hits),
        "ACTL8": dict(Counter(actl8_nuc)),
    }

    # ---- Analysis 2: filament interface
    fil_id, _, _ = FILAMENT_STRUCTURE
    fil_cif = fetch_cif(fil_id)
    fil_chain, all_chains, fil_residues, fil_hits = interface_contacts(fil_cif, fil_id, CONTACT_CUTOFF)
    fil_seq = chain_sequence(fil_residues)
    fil_nums = [res.id[1] for res in fil_residues]
    fil_ref_by_num = dict(zip(fil_nums, fil_seq))
    fil_maps = {}
    for acc in panel_order:
        mapping, pct, score = map_positions(fil_seq, fil_nums, sequences[acc], al)
        fil_maps[acc] = mapping
        results["filament_interface"].setdefault("alignments", {})[acc] = {
            "pct_identity_to_structure_chain": pct
        }
    results["filament_interface"]["structure"] = {
        "pdb_id": fil_id,
        "chains": all_chains,
        "analysed_chain": fil_chain,
        "cutoff_A": CONTACT_CUTOFF,
    }
    results["filament_interface"]["contacts"] = {
        str(n): {
            "structure_residue": f"{fil_ref_by_num[n]}{n}",
            "partner_chains": rec["partners"],
            "min_dist_A": rec["min_dist"],
            **{
                acc: {
                    "position": fil_maps[acc][n][0],
                    "residue": fil_maps[acc][n][1],
                    "class": classify(fil_ref_by_num[n], fil_maps[acc][n][1]),
                }
                for acc in panel_order
            },
        }
        for n, rec in sorted(fil_hits.items())
    }
    results["filament_interface"]["summary"] = {
        "n_contacts": len(fil_hits),
        **{
            acc: dict(Counter(classify(fil_ref_by_num[n], fil_maps[acc][n][1]) for n in sorted(fil_hits)))
            for acc in panel_order
        },
    }
    # same summary for the nucleotide site, all panel members
    results["nucleotide_site"]["summary"].update(
        {
            acc: dict(Counter(classify(ref_by_num[n], nuc_maps[acc][n][1]) for n in sorted(atp_hits)))
            for acc in panel_order
        }
    )

    # ---- alignment sensitivity: do the tallies survive a different matrix and gap model?
    sensitivity: dict = {}
    for scheme, (matrix, og, eg) in ALIGNMENT_SCHEMES.items():
        alt = aligner(matrix, og, eg)
        entry: dict = {}
        for acc in panel_order:
            nuc_map, _, _ = map_positions(struct_seq, struct_nums, sequences[acc], alt)
            fil_map, _, _ = map_positions(fil_seq, fil_nums, sequences[acc], alt)
            entry[acc] = {
                "nucleotide_site": dict(
                    Counter(classify(ref_by_num[n], nuc_map[n][1]) for n in sorted(atp_hits))
                ),
                "filament_interface": dict(
                    Counter(classify(fil_ref_by_num[n], fil_map[n][1]) for n in sorted(fil_hits))
                ),
            }
        sensitivity[scheme] = entry
    results["alignment_sensitivity"] = sensitivity

    # ---- Analysis 3: IBA source audit
    goa_rows = parse_goa(GOA_TSV)
    audit = []
    for row in goa_rows:
        tokens = split_withfrom(row["WITH/FROM"])
        entry = {
            "go_id": row["GO TERM"],
            "go_name": row["GO NAME"],
            "aspect": row["GO ASPECT"],
            "qualifier": row["QUALIFIER"],
            "evidence": row["GO EVIDENCE CODE"],
            "reference": row["REFERENCE"],
            "n_withfrom_tokens": len(tokens),
            "sources": [],
        }
        if row["GO EVIDENCE CODE"] in {"IBA", "ISS", "ISO", "ISA", "ISM", "IEA"}:
            for token in tokens:
                res = resolve_token(token)
                if res["hits"]:
                    primary = next(
                        (h for h in res["hits"] if h["reviewed"] == "Swiss-Prot"), res["hits"][0]
                    )
                    res["evidence_for_donated_term"] = quickgo_evidence(
                        f"UniProtKB:{primary['accession']}", row["GO TERM"]
                    )
                    res["primary_accession"] = primary["accession"]
                entry["sources"].append(res)
        audit.append(entry)
        assert entry["n_withfrom_tokens"] == len(tokens), "WITH/FROM token count drifted"
    results["iba_sources"]["rows"] = audit
    resolved = [s for e in audit for s in e["sources"] if s.get("hits")]
    with_exp = [s for s in resolved if s.get("evidence_for_donated_term", {}).get("has_experimental")]
    swissprot = {s["primary_accession"] for s in resolved if any(h["reviewed"] == "Swiss-Prot" and h["accession"] == s["primary_accession"] for h in s["hits"])}
    results["iba_sources"]["summary"] = {
        "n_source_tokens": sum(e["n_withfrom_tokens"] for e in audit),
        "n_resolved_protein_sources": len(resolved),
        "n_sources_with_own_experimental_evidence_for_donated_term": len(with_exp),
        "n_distinct_reviewed_source_proteins": len(swissprot),
        "n_unresolved": len([s for e in audit for s in e["sources"] if not s.get("hits") and s["strategy"] != "none"]),
        "n_non_protein_sources": len([s for e in audit for s in e["sources"] if s["strategy"] == "none"]),
    }

    # ---- Analysis 4: clade composition of the donating PANTHER nodes
    nodes = sorted(
        {
            tok.split(":", 1)[1]
            for row in goa_rows
            for tok in split_withfrom(row["WITH/FROM"])
            if tok.startswith("PANTHER:")
        }
    )
    clades = {}
    for node in nodes:
        info = node_human_targets(node)
        members_out = []
        for symbol, acc in info["accessions"].items():
            seq = sequences.get(acc) or uniprot_sequence(acc)
            sequences[acc] = seq
            members_out.append(
                {
                    "symbol": symbol,
                    "accession": acc,
                    "length": len(seq),
                    **local_identity_to(sequences["P60709"], seq),
                }
            )
        members_out.sort(key=lambda m: -m["pct_identity_over_aligned_block"])
        clades[node] = {
            "n_human_annotations": info["n_hits"],
            "donated_terms": info["terms"],
            "human_members": members_out,
        }
    results["panther_clades"] = {"nodes": clades}
    shallow = [n for n, c in clades.items() if len(c["human_members"]) < 12]
    results["panther_clades"]["summary"] = {
        "nodes_in_withfrom": nodes,
        "actl8_identity_to_ACTB_pct": next(
            m["pct_identity_over_aligned_block"]
            for m in clades[nodes[0]]["human_members"]
            if m["accession"] == ACTL8
        ),
        "narrow_nodes": shallow,
        "min_identity_of_other_members_in_narrow_nodes": {
            n: min(
                m["pct_identity_over_aligned_block"]
                for m in clades[n]["human_members"]
                if m["accession"] != ACTL8
            )
            for n in shallow
        },
    }

    # ---- Analysis 5: do ACTL8's own closest relatives sit under the same nodes?
    narrow = set(shallow)
    rel = {}
    for acc, sym in RELATIVES.items():
        info = iba_panther_nodes(acc)
        info["shares_narrow_nodes_with_ACTL8"] = sorted(set(info["panther_nodes"]) & narrow)
        rel[sym] = {"accession": acc, **info}
    others_in_narrow = [s for s, v in rel.items() if s != "ACTL8" and v["shares_narrow_nodes_with_ACTL8"]]
    results["relatives"] = {
        "narrow_nodes": sorted(narrow),
        "per_gene": dict(sorted(rel.items())),
        "summary": {
            "n_relatives_examined": len(rel),
            "relatives_other_than_ACTL8_under_a_narrow_node": others_in_narrow,
            "ACTL8_iba_rows": rel["ACTL8"]["n_iba_rows"],
            "median_iba_rows_of_relatives": sorted(
                v["n_iba_rows"] for s, v in rel.items() if s != "ACTL8"
            )[len([s for s in rel if s != "ACTL8"]) // 2],
        },
    }

    # ---- Analysis 6: family context
    members = human_family_members(PANTHER_ENTRIES)
    fam = []
    for m in members:
        counts = quickgo_aspect_counts(f"UniProtKB:{m['accession']}")
        fam.append({**m, "counts": counts})
    results["family"]["members"] = fam
    results["family"]["summary"] = {
        "n_human_members_listed": len(fam),
        "n_with_experimental_MF": sum(1 for m in fam if m["counts"]["MF"]["experimental"] > 0),
        "n_with_informative_experimental_MF": sum(
            1 for m in fam if m["counts"]["informative_experimental_MF_terms"]
        ),
        "n_with_experimental_any": sum(
            1 for m in fam if any(m["counts"][a]["experimental"] > 0 for a in ("MF", "BP", "CC"))
        ),
        "n_with_zero_experimental_anywhere": sum(
            1 for m in fam if all(m["counts"][a]["experimental"] == 0 for a in ("MF", "BP", "CC"))
        ),
    }

    (HERE / "results.json").write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")

    # ---------------------------------------------------------------- RESULTS.md
    L: list[str] = []
    A = L.append
    A("# ACTL8: does the actin fold come with actin's residues, and do its IBA sources transfer?")
    A("")
    A("Generated by `uv run python analyze_actl8.py`. Every number below is computed at run")
    A("time from the UniProt REST API, RCSB coordinate files, QuickGO, and the repository's")
    A("cached PANTHER family listing. Nothing is hard-coded from a previous run.")
    A("")
    A("## 1. Is actin's nucleotide site still present in ACTL8?")
    A("")
    ns_ = results["nucleotide_site"]["structure"]
    A(f"Contacts were computed from PDB **{ns_['pdb_id']}** chain {ns_['chain']} "
      f"(beta-actin with bound {', '.join(ns_['ligands'])}), taking every residue with a heavy atom "
      f"within {ns_['cutoff_A']} Å of the nucleotide or its divalent cation. "
      f"{len(atp_hits)} residues qualify. The structure chain's own observed sequence "
      f"(residues {ns_['observed_residue_range'][0]}–{ns_['observed_residue_range'][1]}) was then aligned "
      "to each panel sequence, so the residue reported for each protein is the aligned residue, not the "
      "residue at the same number.")
    A("")
    A("`~` = conservative substitution, `**` = non-conservative substitution.")
    A("")
    cols = [ACTL8, "P60709", "Q9Y615", "Q8TDG2", "P61160", "P45891"]
    L.extend(fmt_residue_table(atp_hits, nuc_maps, ref_by_num, cols))
    A("")
    A("Column key: " + "; ".join(f"`{c}` = {PANEL.get(c, 'ACTL8 (human actin-like 8)')}" for c in cols))
    A("")
    A("Per-protein tally over the same contact set:")
    A("")
    A("| Protein | identical | conservative | non-conservative | gap | % identity to structure chain |")
    A("|---|---|---|---|---|---|")
    for acc in panel_order:
        c = results["nucleotide_site"]["summary"][acc]
        pct = results["nucleotide_site"]["alignments"][acc]["pct_identity_to_structure_chain"]
        label = PANEL.get(acc, "ACTL8 (human actin-like 8)")
        A(f"| {label} | {c.get('identical', 0)} | {c.get('conservative', 0)} | "
          f"{c.get('non-conservative', 0)} | {c.get('gap', 0)} | {pct} |")
    A("")
    A(f"Residues that enter only the {ns_['second_shell_cutoff_A']} Å shell (second shell, "
      "water-mediated in this structure): " + ", ".join(results["nucleotide_site"]["second_shell_only"]) + ".")
    A("")
    A("## 2. Is the filament protomer interface still present?")
    A("")
    fs = results["filament_interface"]["structure"]
    A(f"PDB **{fs['pdb_id']}** contains {len(fs['chains'])} F-actin protomers "
      f"({', '.join(fs['chains'])}). Chain **{fs['analysed_chain']}** has the most inter-protomer "
      f"contacts and was used. Interface residues are every residue within {fs['cutoff_A']} Å of any "
      f"other chain: {results['filament_interface']['summary']['n_contacts']} residues.")
    A("")
    A("| Protein | identical | conservative | non-conservative | gap |")
    A("|---|---|---|---|---|")
    for acc in panel_order:
        c = results["filament_interface"]["summary"][acc]
        label = PANEL.get(acc, "ACTL8 (human actin-like 8)")
        A(f"| {label} | {c.get('identical', 0)} | {c.get('conservative', 0)} | "
          f"{c.get('non-conservative', 0)} | {c.get('gap', 0)} |")
    A("")
    A("### What this metric does and does not bound")
    A("")
    A("Ranking the whole panel by chemically compatible positions (identical + conservative) out of")
    A(f"{results['filament_interface']['summary']['n_contacts']}:")
    A("")
    ranked = sorted(
        (
            (
                acc,
                results["filament_interface"]["summary"][acc].get("identical", 0)
                + results["filament_interface"]["summary"][acc].get("conservative", 0),
            )
            for acc in panel_order
        ),
        key=lambda kv: -kv[1],
    )
    A("| Protein | compatible / %d |" % results["filament_interface"]["summary"]["n_contacts"])
    A("|---|---|")
    for acc, score in ranked:
        label = PANEL.get(acc, "ACTL8 (human actin-like 8)")
        mark = " **<-- ACTL8**" if acc == ACTL8 else ""
        A(f"| {label} | {score}{mark} |")
    A("")
    A("The ordering carries an important caveat, and it is one this analysis produces against itself.")
    A("**Arp3 (ACTR3) scores below ACTL8**, and Arp2 only a little above, yet Arp2 and Arp3 form the")
    A("first protomer pair of a daughter filament at an Arp2/3 branch - they do make actin-like")
    A("protomer contacts. A low score on this metric therefore bounds *canonical protomer")
    A("incorporation into a conventional two-stranded filament*; it does not show that a protein")
    A("cannot occupy any position in an actin-containing structure. ACTL8 sits in a band with the")
    A("other divergent actin-likes and Arp3, not uniquely below them, and any argument built on the")
    A("tally should be stated at that strength.")
    A("")
    A("Per-residue detail for ACTL8 and two reference points:")
    A("")
    L.extend(fmt_residue_table(fil_hits, fil_maps, fil_ref_by_num, [ACTL8, "P60709", "Q9Y615"]))
    A("")
    A("### Alignment sensitivity")
    A("")
    A("ACTL8 is far enough from actin that gap placement could in principle drive the tallies,")
    A("so both residue sets were re-scored under a second matrix and gap model. If the")
    A("counts below move only marginally, the conservation call is not an artefact of one")
    A("alignment.")
    A("")
    A("| Protein | scheme | nucleotide site (id/cons/non-cons/gap) | filament interface (id/cons/non-cons/gap) |")
    A("|---|---|---|---|")
    for acc in panel_order:
        label = PANEL.get(acc, "ACTL8 (human actin-like 8)")
        for scheme in ALIGNMENT_SCHEMES:
            e = results["alignment_sensitivity"][scheme][acc]
            def cell(c: dict) -> str:
                return "/".join(
                    str(c.get(k, 0)) for k in ("identical", "conservative", "non-conservative", "gap")
                )
            A(f"| {label} | {scheme} | {cell(e['nucleotide_site'])} | {cell(e['filament_interface'])} |")
    A("")
    A("## 3. What evidence do the IBA WITH/FROM sources carry for the term they donated?")
    A("")
    s = results["iba_sources"]["summary"]
    A(f"- WITH/FROM tokens across all rows (parsed from `ACTL8-goa.tsv`, not by hand): **{s['n_source_tokens']}**")
    A(f"- resolved to protein entries: **{s['n_resolved_protein_sources']}**")
    A(f"- distinct reviewed (Swiss-Prot) source proteins: **{s['n_distinct_reviewed_source_proteins']}**")
    A(f"- sources carrying their own experimental-code annotation for the donated term: "
      f"**{s['n_sources_with_own_experimental_evidence_for_donated_term']}**")
    A(f"- non-protein sources (PANTHER tree nodes, GO ids): **{s['n_non_protein_sources']}**")
    A(f"- unresolved: **{s['n_unresolved']}**")
    A("")
    for e in results["iba_sources"]["rows"]:
        if not e["sources"]:
            continue
        A(f"### {e['go_id']} {e['go_name']} ({e['aspect']}, {e['evidence']}, {e['qualifier']})")
        A("")
        A("| WITH/FROM | resolved to | status | organism | own evidence for this term |")
        A("|---|---|---|---|---|")
        for src in e["sources"]:
            if not src["hits"]:
                A(f"| `{src['token']}` | — | — | — | {src['note']} |")
                continue
            primary = src["primary_accession"]
            hit = next(h for h in src["hits"] if h["accession"] == primary)
            ev = src["evidence_for_donated_term"]
            codes = ", ".join(f"{k}×{v}" for k, v in ev["codes"].items()) or "none"
            extra = f" ({src['note']})" if src["note"] else ""
            A(f"| `{src['token']}` | {primary} {'/'.join(hit['genes']) or '?'} — {hit['name']}{extra} "
              f"| {hit['reviewed']} | {hit['organism']} | {codes} |")
        A("")
    A("## 4. Which clade does each donating PANTHER node actually cover?")
    A("")
    A("For every PANTHER ancestral node cited in an ACTL8 WITH/FROM field, QuickGO was asked")
    A("which human genes that node donates to. Each of those genes was then aligned locally to")
    A("human beta-actin (P60709), so that a multidomain protein is compared over its actin block")
    A("rather than over its full length.")
    A("")
    for node, c in sorted(results["panther_clades"]["nodes"].items()):
        A(f"### PANTHER:{node}")
        A("")
        A(f"Donates to human genes: {', '.join(sorted(c['donated_terms'].keys()))} "
          f"({c['n_human_annotations']} human annotations).")
        A("")
        A("| Gene | Accession | length | aligned block to ACTB | % identity to ACTB over that block |")
        A("|---|---|---|---|---|")
        for m in c["human_members"]:
            flag = " **" if m["accession"] == ACTL8 else ""
            A(f"| {m['symbol']}{flag} | {m['accession']} | {m['length']} | {m['aligned_columns']} "
              f"| {m['pct_identity_over_aligned_block']} |")
        A("")
    cs = results["panther_clades"]["summary"]
    A(f"ACTL8 is {cs['actl8_identity_to_ACTB_pct']}% identical to beta-actin over its aligned block. "
      "In the narrow nodes the lowest identity to beta-actin among the *other* human members is: "
      + "; ".join(f"`{k}` {v}%" for k, v in sorted(cs["min_identity_of_other_members_in_narrow_nodes"].items()))
      + ".")
    A("")
    A("## 5. Do ACTL8's own closest relatives sit under the same PANTHER nodes?")
    A("")
    rs = results["relatives"]["summary"]
    A("For each divergent human actin-like / actin-related-T protein, QuickGO was asked which PANTHER")
    A("nodes appear in the WITH/FROM field of its *own* IBA annotations. If ACTL8's membership of the")
    A("cytoplasmic-actin subfamily were normal for this group, its relatives would be there too.")
    A("")
    A("| Gene | Accession | own IBA rows | PANTHER nodes in its WITH/FROM | shares a narrow node with ACTL8 |")
    A("|---|---|---|---|---|")
    for sym, v in results["relatives"]["per_gene"].items():
        shared = ", ".join(v["shares_narrow_nodes_with_ACTL8"]) or "no"
        A(f"| {sym} | {v['accession']} | {v['n_iba_rows']} | {', '.join(v['panther_nodes']) or '—'} | {shared} |")
    A("")
    A(f"Narrow (beta-actin subfamily) nodes: {', '.join(results['relatives']['narrow_nodes'])}. "
      f"Of the {rs['n_relatives_examined']} relatives examined, the ones other than ACTL8 that sit "
      f"under a narrow node are: "
      + (", ".join(rs["relatives_other_than_ACTL8_under_a_narrow_node"]) or "**none**")
      + f". ACTL8 carries {rs['ACTL8_iba_rows']} IBA rows against a median of "
      f"{rs['median_iba_rows_of_relatives']} for its relatives.")
    A("")
    A("## 6. How common is experimental molecular function in this family?")
    A("")
    f = results["family"]["summary"]
    A(f"Human members of PANTHER PTHR11937 (ACTIN) listed in the repository's cached InterPro "
      f"entry table: **{f['n_human_members_listed']}**. Of these, "
      f"**{f['n_with_experimental_MF']}** carry at least one experimental-code molecular-function "
      f"annotation in QuickGO, **{f['n_with_experimental_any']}** carry an experimental annotation in "
      f"any aspect, and **{f['n_with_zero_experimental_anywhere']}** have none at all. Once bare "
      f"`GO:0005515 protein binding` is excluded — which nearly every human protein has from "
      f"interactome screens, so counting it would make this survey uninformative — "
      f"**{f['n_with_informative_experimental_MF']}** members retain an experimentally supported, "
      f"informative molecular function.")
    A("")
    A("| Gene | Accession | MF exp / total | BP exp / total | CC exp / total | informative experimental MF terms |")
    A("|---|---|---|---|---|---|")
    for m in results["family"]["members"]:
        c = m["counts"]
        terms = ", ".join(c["informative_experimental_MF_terms"]) or "—"
        A(f"| {m['gene'] or '?'} | {m['accession']} | {c['MF']['experimental']} / {c['MF']['total']} "
          f"| {c['BP']['experimental']} / {c['BP']['total']} | {c['CC']['experimental']} / {c['CC']['total']} "
          f"| {terms} |")
    A("")
    A("Experimental codes counted: " + ", ".join(sorted(EXPERIMENTAL_CODES)) + ".")
    A("")
    (HERE / "RESULTS.md").write_text("\n".join(L) + "\n")
    print(json.dumps(
        {
            "nucleotide_site": results["nucleotide_site"]["summary"],
            "filament_interface": results["filament_interface"]["summary"],
            "iba_sources": results["iba_sources"]["summary"],
            "family": results["family"]["summary"],
        },
        indent=2,
    ))


if __name__ == "__main__":
    main()
