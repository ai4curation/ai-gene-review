#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.85", "requests", "pyyaml"]
# ///
"""Pairwise comparison of the Actinomortierella ambigua SUCLG2-type beta subunit
(UniProtKB A0A9P6TY68) with reference succinyl-CoA synthetase beta subunits.

Nothing is hard-coded except identifiers and the reference residue numbers being
looked up. Sequences, protein names, organisms and signature hits are fetched from
UniProt at run time; identities and residue correspondences are computed.

1. Inventory: every UniProt entry of the query organism (taxon read from the query
   entry) that carries a PANTHER PTHR11815 (beta) or PTHR11117 (alpha) cross-reference,
   with its PANTHER and HAMAP hits.
2. Pairwise global alignments (BLOSUM62, gap open -10, extend -0.5, end gaps free)
   of the query against each comparator. Identity is identical residues over the
   columns in which both sequences have a residue.
3. Residue correspondences: for named residues of reference proteins, the query
   residue in the same alignment column.
4. N-terminal extension: number of query residues before the residue aligned with
   Met1 of E. coli SucC.
5. N-terminal comparison with the closest ortholog models (NTERM_ORTHOLOGS): for each,
   the residues of query and ortholog that precede the residue aligned with Met1 of
   E. coli SucC, which query residues of the extension have an identical aligned
   ortholog residue, and the basic and acidic residue counts of the ortholog leader.

Usage: uv run --script scs_beta_comparison.py   (writes results.yaml next to the script)
"""
from __future__ import annotations

import datetime
import pathlib

import requests
import yaml
from Bio.Align import PairwiseAligner, substitution_matrices

QUERY = "A0A9P6TY68"
COMPARATORS = [
    "A0A197JV50",  # Linnemannia elongata, Gln20 gene placed in the LSC2 panel trees
    "A0A1Y2H5W1",  # Lobosporangium transversale, Gln20 gene placed in the LSC2 panel trees
    "A9UVA2",      # Monosiga brevicollis, leaf below PTN000929335
    "Q96I99",      # human SUCLG2
    "P53590",      # pig SUCLG2
    "Q869S7",      # Dictyostelium scsB (G-type)
    "Q9P2R7",      # human SUCLA2
    "B3FHP0",      # Blastocystis SCSb (Gln20, ATP-specific by assay)
    "P0A836",      # E. coli SucC
    "P53312",      # S. cerevisiae LSC2
]
# reference residues to map onto the query: (accession, position, why)
REFERENCE_RESIDUES = [
    ("P0A836", 20, "position 20 of the mature subunit (Pro in E. coli SucC)"),
    ("P53590", 58, "UniProt GTP binding site of pig SUCLG2 (Gln20 of the mature subunit)"),
    ("Q96I99", 57, "human SUCLG2 residue at position 20 of the mature subunit"),
    ("P0A836", 46, "HAMAP rule ATP site"),
    ("P0A836", 107, "HAMAP rule ATP site"),
    ("P0A836", 199, "HAMAP rule Mg site"),
    ("P0A836", 213, "HAMAP rule Mg site"),
    ("P0A836", 264, "HAMAP rule substrate site"),
    ("P0A836", 321, "HAMAP rule substrate motif, first residue"),
    ("P0A836", 322, "HAMAP rule substrate motif, second residue"),
    ("P0A836", 323, "HAMAP rule substrate motif, third residue"),
    ("P0A836", 1, "first residue of E. coli SucC"),
]
# closest ortholog gene models, compared at the N-terminus
NTERM_ORTHOLOGS = ["A0A197JV50", "A0A1Y2H5W1"]
API = "https://rest.uniprot.org/uniprotkb"


def fetch(acc: str) -> dict:
    r = requests.get(f"{API}/{acc}.json", timeout=60)
    r.raise_for_status()
    return r.json()


def summarise(e: dict) -> dict:
    xr = e.get("uniProtKBCrossReferences", [])
    desc = e.get("proteinDescription", {})
    name = (desc.get("recommendedName") or (desc.get("submissionNames") or [{}])[0]).get("fullName", {}).get("value")
    genes = e.get("genes", [])
    gene = None
    if genes:
        g = genes[0]
        gene = (g.get("geneName") or (g.get("orfNames") or g.get("orderedLocusNames") or [{}])[0]).get("value")
    return {
        "accession": e["primaryAccession"],
        "organism": e["organism"]["scientificName"],
        "gene": gene,
        "protein_name": name,
        "length": e["sequence"]["length"],
        "sequence_version": e["entryAudit"]["sequenceVersion"],
        "panther": [x["id"] for x in xr if x["database"] == "PANTHER"],
        "hamap": [x["id"] for x in xr if x["database"] == "HAMAP"],
    }


def aligner() -> PairwiseAligner:
    al = PairwiseAligner()
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score = -10
    al.extend_gap_score = -0.5
    al.mode = "global"
    al.end_gap_score = 0
    return al


def columns(al: PairwiseAligner, a: str, b: str) -> list[tuple[int | None, int | None]]:
    """Aligned columns as (1-based index in a or None, 1-based index in b or None)."""
    aln = al.align(a, b)[0]
    ra, rb = aln[0], aln[1]
    out, i, j = [], 0, 0
    for x, y in zip(ra, rb):
        ia = jb = None
        if x != "-":
            i += 1
            ia = i
        if y != "-":
            j += 1
            jb = j
        out.append((ia, jb))
    return out


def main() -> None:
    al = aligner()
    q = fetch(QUERY)
    qseq = q["sequence"]["value"]
    taxon = q["organism"]["taxonId"]

    # 1. inventory of SCS subunits in the query organism
    inv = []
    for fam in ("PTHR11815", "PTHR11117"):
        r = requests.get(
            f"{API}/search",
            params={"query": f"taxonomy_id:{taxon} AND xref:panther-{fam}", "format": "json", "size": 100},
            timeout=60,
        )
        r.raise_for_status()
        for e in r.json()["results"]:
            s = summarise(e)
            s["family"] = fam
            inv.append(s)
    paralogs = [s["accession"] for s in inv if s["family"] == "PTHR11815" and s["accession"] != QUERY]

    # 2 and 3. pairwise alignments
    entries = {QUERY: q}
    for acc in COMPARATORS + paralogs:
        entries[acc] = fetch(acc)
    pairs, colmaps = [], {}
    for acc in COMPARATORS + paralogs:
        seq = entries[acc]["sequence"]["value"]
        cols = columns(al, qseq, seq)
        colmaps[acc] = cols
        both = [(i, j) for i, j in cols if i and j]
        ident = sum(qseq[i - 1] == seq[j - 1] for i, j in both)
        s = summarise(entries[acc])
        pairs.append({
            "accession": acc,
            "organism": s["organism"],
            "gene": s["gene"],
            "length": s["length"],
            "aligned_columns": len(both),
            "identical": ident,
            "percent_identity": round(100 * ident / len(both), 1),
            "same_organism_paralog": acc in paralogs,
        })
    pairs.sort(key=lambda p: -p["percent_identity"])

    residues = []
    for acc, pos, why in REFERENCE_RESIDUES:
        seq = entries[acc]["sequence"]["value"]
        qpos = next((i for i, j in colmaps[acc] if j == pos), None)
        residues.append({
            "reference": acc,
            "reference_position": pos,
            "reference_residue": seq[pos - 1],
            "query_position": qpos,
            "query_residue": qseq[qpos - 1] if qpos else None,
            "note": why,
        })

    # 4. N-terminal extension relative to E. coli SucC Met1
    first = next((i for i, j in colmaps["P0A836"] if j == 1), None)
    nterm = None
    if first:
        ext = qseq[: first - 1]
        nterm = {
            "query_residue_aligned_with_ecoli_Met1": first,
            "extension_length": len(ext),
            "extension_sequence": ext,
            "arg_plus_lys": sum(ext.count(c) for c in "RK"),
            "asp_plus_glu": sum(ext.count(c) for c in "DE"),
        }

    # 5. N-terminus of the query against the closest ortholog models
    nterm_orthologs = []
    if first:
        for acc in NTERM_ORTHOLOGS:
            seq = entries[acc]["sequence"]["value"]
            cols = colmaps[acc]
            # ortholog residue aligned with the query residue that aligns with E. coli Met1
            opos = next((j for i, j in cols if i == first), None)
            if opos is None:
                # fall back to the first ortholog residue aligned at or after that query position
                opos = next((j for i, j in cols if i and i >= first and j), None)
            leader = seq[: opos - 1] if opos else None
            conserved = [i for i, j in cols if i and j and i < first and qseq[i - 1] == seq[j - 1]]
            unaligned = [i for i, j in cols if i and i < first and not j]
            mismatched = [i for i, j in cols if i and j and i < first and qseq[i - 1] != seq[j - 1]]
            nterm_orthologs.append({
                "accession": acc,
                "organism": entries[acc]["organism"]["scientificName"],
                "length": len(seq),
                "ortholog_residue_aligned_with_query_core_start": opos,
                "ortholog_leader_length": len(leader) if leader is not None else None,
                "ortholog_leader_sequence": leader,
                "ortholog_leader_arg_plus_lys": sum(leader.count(c) for c in "RK") if leader is not None else None,
                "ortholog_leader_asp_plus_glu": sum(leader.count(c) for c in "DE") if leader is not None else None,
                "query_extension_positions_identical_to_ortholog": conserved,
                "query_extension_positions_mismatched": mismatched,
                "query_extension_positions_without_ortholog_residue": unaligned,
            })

    out = {
        "retrieved": datetime.date.today().isoformat(),
        "query": summarise(q),
        "organism_scs_subunits": inv,
        "pairwise_identity": pairs,
        "residue_correspondences": residues,
        "n_terminal_extension": nterm,
        "n_terminal_comparison_with_orthologs": nterm_orthologs,
        "method": "Biopython PairwiseAligner, global, BLOSUM62, gap open -10, extend -0.5, end gaps free; "
                  "identity = identical residues over columns where both sequences have a residue",
    }
    path = pathlib.Path(__file__).with_name("results.yaml")
    path.write_text(yaml.safe_dump(out, sort_keys=False, allow_unicode=True, width=120))
    print(path.read_text())


if __name__ == "__main__":
    main()
