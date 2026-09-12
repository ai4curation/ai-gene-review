#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["requests"]
# ///
"""Domain-architecture audit of the WITH/FROM source genes behind ACAP3's IBA annotations.

Every IBA row in ``ACAP3-goa.tsv`` names, in its WITH/FROM column, the model-organism
genes whose experimental annotations supported the PANTHER ancestral-node call that was
then propagated to human ACAP3. A propagated annotation is only as safe as the
architectural equivalence between those source genes and ACAP3.

This script asks one question, per source gene: does it carry the ACAP module set?

    IPR045258  ACAP1/2/3-like        (the subfamily signature)
    IPR001164  ArfGAP domain         (the catalytic/GAP module)
    IPR004148  BAR domain            (membrane curvature / dimerisation module)
    IPR001849  PH domain             (phosphoinositide-binding module)
    IPR002110  Ankyrin repeat        (C-terminal ANK repeats)

Domain content is read from the InterPro cross-references of each source protein's
UniProt entry (UniProtKB REST). Nothing is hardcoded: if UniProt/InterPro change,
the table changes.

The gene-identifier -> UniProt accession step cannot be done by a single generic query
(the GOA WITH/FROM column mixes MGI/RGD/WB/FB/SGD/dictyBase/PomBase/AGI namespaces, and
some source genes have no Swiss-Prot entry at all). The resolution query actually used
for each identifier is recorded alongside it in SOURCES below so the mapping is
auditable and re-runnable.

Usage:
    uv run check_iba_source_architecture.py            # print table
    uv run check_iba_source_architecture.py --markdown # emit RESULTS.md body
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass

import requests

UNIPROT = "https://rest.uniprot.org/uniprotkb"

ACAP_MODULES: dict[str, str] = {
    "IPR045258": "ACAP1/2/3-like",
    "IPR001164": "ArfGAP",
    "IPR004148": "BAR",
    "IPR001849": "PH",
    "IPR002110": "ANK repeat",
}


@dataclass(frozen=True)
class Source:
    """A WITH/FROM source gene from ACAP3-goa.tsv."""

    withfrom_id: str  # exactly as it appears in the GOA WITH/FROM column
    label: str
    organism: str
    accession: str
    resolution_query: str  # the UniProtKB search query used to obtain `accession`
    iba_terms: tuple[str, ...]  # ACAP3 IBA terms this source appears under


SOURCES: tuple[Source, ...] = (
    Source(
        "MGI:MGI:2153589",
        "Acap3",
        "Mus musculus",
        "Q6NXL5",
        "MGI:2153589 AND organism_id:10090  (no Swiss-Prot entry; TrEMBL only)",
        ("GO:0005096", "GO:0001764", "GO:0010975"),
    ),
    Source(
        "UniProtKB:Q15057",
        "ACAP2",
        "Homo sapiens",
        "Q15057",
        "direct accession",
        ("GO:0005096", "GO:0005886"),
    ),
    Source(
        "RGD:1562939",
        "Acap2",
        "Rattus norvegicus",
        "Q5FVC7",
        "xref:rgd-1562939 AND reviewed:true",
        ("GO:0010008",),
    ),
    Source(
        "WB:WBGene00000565",
        "cnt-1",
        "Caenorhabditis elegans",
        "Q9XXH8",
        "WBGene00000565 AND organism_id:6239 AND reviewed:true",
        ("GO:0005886", "GO:0010008"),
    ),
    Source(
        "PomBase:SPBC17G9.08c",
        "cnt5",
        "Schizosaccharomyces pombe",
        "Q9UUE2",
        "xref:pombase-SPBC17G9.08c AND reviewed:true",
        ("GO:0005886",),
    ),
    Source(
        "dictyBase:DDB_G0279649",
        "DDB_G0279649",
        "Dictyostelium discoideum",
        "Q54WI0",
        "xref:dictybase-DDB_G0279649",
        ("GO:0005096", "GO:0005886", "GO:0030036"),
    ),
    Source(
        "dictyBase:DDB_G0276395",
        "DDB_G0276395",
        "Dictyostelium discoideum",
        "Q551Q8",
        "xref:dictybase-DDB_G0276395",
        ("GO:0030036",),
    ),
    Source(
        "SGD:S000002932",
        "AGE1",
        "Saccharomyces cerevisiae",
        "Q04412",
        "xref:sgd-S000002932 AND reviewed:true",
        ("GO:0005096",),
    ),
    Source(
        "AGI_LocusCode:AT5G13300",
        "AGD3",
        "Arabidopsis thaliana",
        "Q5W7F2",
        "xref:araport-AT5G13300 AND reviewed:true",
        ("GO:0005096", "GO:0005886"),
    ),
    Source(
        "AGI_LocusCode:AT5G61980",
        "AGD1",
        "Arabidopsis thaliana",
        "Q9FIT8",
        "gene:AGD1 AND organism_id:3702 AND reviewed:true",
        ("GO:0005886",),
    ),
    Source(
        "FB:FBgn0004133",
        "blow (blown fuse)",
        "Drosophila melanogaster",
        "P91678",
        "xref:flybase-FBgn0004133  (no Swiss-Prot entry; TrEMBL only, 4 isoforms, "
        "all with identical InterPro content)",
        ("GO:0030036",),
    ),
)

TARGET = Source(
    "-", "ACAP3 (target)", "Homo sapiens", "Q96P50", "direct accession", ()
)


def interpro_ids(accession: str, session: requests.Session) -> set[str]:
    """Return the set of InterPro accessions cross-referenced by a UniProt entry."""
    resp = session.get(
        f"{UNIPROT}/{accession}.json", params={"fields": "xref_interpro"}, timeout=60
    )
    resp.raise_for_status()
    return {
        x["id"]
        for x in resp.json().get("uniProtKBCrossReferences", [])
        if x["database"] == "InterPro"
    }


def audit() -> list[tuple[Source, set[str]]]:
    with requests.Session() as session:
        return [(s, interpro_ids(s.accession, session)) for s in (TARGET, *SOURCES)]


def render(rows: list[tuple[Source, set[str]]], markdown: bool) -> str:
    modules = list(ACAP_MODULES)
    head = ["source (WITH/FROM)", "gene", "organism", "acc", *ACAP_MODULES.values()]
    body = [
        [
            s.withfrom_id,
            s.label,
            s.organism,
            s.accession,
            *["yes" if m in found else "**NO**" if markdown else "NO" for m in modules],
        ]
        for s, found in rows
    ]
    if markdown:
        out = ["| " + " | ".join(head) + " |", "|" + "---|" * len(head)]
        out += ["| " + " | ".join(r) + " |" for r in body]
        return "\n".join(out)
    widths = [max(len(r[i]) for r in [head, *body]) for i in range(len(head))]
    return "\n".join(
        "  ".join(c.ljust(w) for c, w in zip(r, widths)) for r in [head, *body]
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--markdown", action="store_true", help="emit a markdown table")
    args = parser.parse_args()

    rows = audit()
    print(render(rows, args.markdown))
    print()

    target_modules = rows[0][1]
    missing_signature = [
        s.label
        for s, found in rows[1:]
        if not {"IPR045258", "IPR001164"} <= found
    ]
    print(
        "ACAP3 carries all five ACAP modules: "
        f"{ {'IPR045258','IPR001164','IPR004148','IPR001849','IPR002110'} <= target_modules }"
    )
    if missing_signature:
        print(
            "Source genes LACKING the ACAP1/2/3-like signature or the ArfGAP domain: "
            + ", ".join(missing_signature)
        )
    else:
        print("All WITH/FROM source genes carry the ACAP signature and an ArfGAP domain.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
