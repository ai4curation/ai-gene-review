"""Survey the Korarchaeum cryptofilum OPF8 proteome (taxon 374847) for
methanogenesis marker proteins, coenzyme M / coenzyme B biosynthesis proteins
and Hdr / Mvh-like subunits, using live UniProt REST queries.

Nothing is hardcoded: every count and hit printed below comes from the API at
run time. InterPro accessions used as queries were looked up in the InterPro
API (names printed at run time so the identity of each query is auditable).

Usage:
    uv run python survey_com_cob_genes.py > survey_output.txt
"""

from __future__ import annotations

import datetime as dt
import sys

import requests

TAXON = "374847"
UNIPROT = "https://rest.uniprot.org/uniprotkb/search"
INTERPRO = "https://www.ebi.ac.uk/interpro/api/entry/interpro/{}"

# InterPro family/domain signatures, grouped by the pathway they mark.
INTERPRO_QUERIES = {
    "methyl-coenzyme M reductase (methanogenesis/ANME marker)": [
        "IPR003183",  # MCR alpha N-terminal domain
        "IPR003179",  # MCR beta subunit family
        "IPR003178",  # MCR gamma subunit family
    ],
    "coenzyme M biosynthesis (ComA, ComB, ComDE)": [
        "IPR003830",  # (2R)-phospho-3-sulpholactate synthase, ComA family
        "IPR005238",  # ComB-like family
        "IPR022502",  # sulfopyruvate decarboxylase alpha (ComD)
        "IPR022494",  # sulfopyruvate decarboxylase beta (ComE)
    ],
    "heterodisulfide reductase subunits": [
        "IPR039650",  # HdrA-like family
        "IPR017678",  # HdrB family
        "IPR053646",  # HdrC family
    ],
}

# Free-text name queries (UniProt protein_name field) for steps that have no
# specific InterPro family, notably coenzyme B synthesis and ComC.
NAME_QUERIES = [
    "methyl-coenzyme M reductase",
    "coenzyme M",
    "coenzyme B",
    "sulfolactate",
    "sulfopyruvate",
    "phosphosulfolactate",
    "7-mercaptoheptanoyl",
    "homocitrate synthase",
    "heterodisulfide",
    "methyl-viologen",
    "F420",
    "hydrogenase",
]

# Genes neighbouring the two HdrA-like loci, to show local context.
LOCUS_TAGS = [f"Kcr_{n:04d}" for n in list(range(760, 772)) + list(range(1112, 1122))]

FIELDS = "accession,gene_oln,protein_name,xref_interpro,length"


def interpro_name(acc: str) -> str:
    try:
        r = requests.get(INTERPRO.format(acc), timeout=60)
        r.raise_for_status()
        return r.json()["metadata"]["name"]["name"]
    except Exception as exc:  # report, never invent
        return f"<lookup failed: {exc}>"


def uniprot(query: str) -> list[dict]:
    r = requests.get(
        UNIPROT,
        params={"query": query, "fields": FIELDS, "format": "tsv", "size": 500},
        timeout=120,
    )
    r.raise_for_status()
    lines = r.text.strip().splitlines()
    if len(lines) <= 1:
        return []
    header = lines[0].split("\t")
    return [dict(zip(header, ln.split("\t"))) for ln in lines[1:]]


def taxon_total() -> str:
    r = requests.get(
        UNIPROT,
        params={"query": f"taxonomy_id:{TAXON}", "fields": "accession", "format": "tsv", "size": 1},
        timeout=120,
    )
    r.raise_for_status()
    return r.headers.get("x-total-results", "<header missing>")


def show(rows: list[dict]) -> None:
    for row in rows:
        print(
            "    {acc}\t{oln}\t{name}".format(
                acc=row.get("Entry", ""),
                oln=row.get("Gene Names (ordered locus)", ""),
                name=row.get("Protein names", ""),
            )
        )


def main() -> int:
    print(f"# Run date (UTC): {dt.datetime.now(dt.timezone.utc).isoformat()}")
    print(f"# Taxon: NCBITaxon:{TAXON}")
    print(f"# UniProtKB entries for taxon: {taxon_total()}")
    print()
    print("## InterPro signature queries")
    for group, accs in INTERPRO_QUERIES.items():
        print(f"### {group}")
        for acc in accs:
            q = f"taxonomy_id:{TAXON} AND xref:interpro-{acc}"
            rows = uniprot(q)
            print(f"  {acc} ({interpro_name(acc)}): query='{q}' hits={len(rows)}")
            show(rows)
    print()
    print("## Protein-name queries")
    for term in NAME_QUERIES:
        q = f'taxonomy_id:{TAXON} AND protein_name:"{term}"'
        rows = uniprot(q)
        print(f"  query='{q}' hits={len(rows)}")
        show(rows)
    print()
    print("## Neighbourhood of the HdrA-like loci (ordered locus names)")
    for tag in LOCUS_TAGS:
        rows = uniprot(f"taxonomy_id:{TAXON} AND gene:{tag}")
        if not rows:
            print(f"  {tag}: no entry")
        for row in rows:
            print(
                f"  {tag}\t{row.get('Entry','')}\t{row.get('Protein names','')}"
                f"\tInterPro={row.get('InterPro','')}"
            )
    print()
    print("## Names of InterPro entries seen in the neighbourhood")
    seen: set[str] = set()
    for tag in LOCUS_TAGS:
        for row in uniprot(f"taxonomy_id:{TAXON} AND gene:{tag}"):
            for acc in filter(None, row.get("InterPro", "").split(";")):
                seen.add(acc)
    for acc in sorted(seen):
        print(f"  {acc}\t{interpro_name(acc)}")
    print()
    print("## QuickGO: all IBA rows for GO:0051912 and their with/from")
    r = requests.get(
        "https://www.ebi.ac.uk/QuickGO/services/annotation/search",
        params={"goId": "GO:0051912", "evidenceCode": "ECO:0000318", "limit": 100},
        headers={"Accept": "application/json"},
        timeout=120,
    )
    r.raise_for_status()
    data = r.json()
    print(f"  hits={data.get('numberOfHits')}")
    for row in data.get("results", []):
        wf = ";".join(
            f"{x['db']}:{x['id']}" for w in row.get("withFrom") or [] for x in w["connectedXrefs"]
        )
        print(f"  {row['geneProductId']}\t{row.get('symbol')}\ttaxon={row.get('taxonId')}\twith={wf}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
