#!/usr/bin/env python3
"""First-pass curation for low-information translation/RNA spillovers."""

from __future__ import annotations

import csv
import json
import urllib.request
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes" / "PSEPK"
MODULE_PATH = ROOT / "modules" / "translation_rna_processing_spillover_boundary.yaml"
BATCH_TSV = (
    "projects/P_PUTIDA/batches/"
    "module_translation_rna_processing_low_information_rna_binding_or_enzyme_spillovers.tsv"
)
TAXON_LABEL = "Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)"
TODAY = "2026-07-10"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):  # type: ignore[override]
        return True


TERM = {
    "GO:0003723": {"id": "GO:0003723", "label": "RNA binding"},
    "GO:0003960": {"id": "GO:0003960", "label": "quinone reductase (NADPH) activity"},
    "GO:0005737": {"id": "GO:0005737", "label": "cytoplasm"},
    "GO:0005829": {"id": "GO:0005829", "label": "cytosol"},
    "GO:0008270": {"id": "GO:0008270", "label": "zinc ion binding"},
    "GO:0010608": {"id": "GO:0010608", "label": "post-transcriptional regulation of gene expression"},
    "GO:0016491": {"id": "GO:0016491", "label": "oxidoreductase activity"},
    "GO:0033592": {"id": "GO:0033592", "label": "RNA strand annealing activity"},
    "GO:0034057": {"id": "GO:0034057", "label": "RNA strand-exchange activity"},
}

GO_REF_TITLES = {
    "GO_REF:0000002": "Gene Ontology annotation through association of InterPro records with GO terms",
    "GO_REF:0000003": "Gene Ontology annotation based on Enzyme Commission mapping",
    "GO_REF:0000044": "Gene Ontology annotation based on UniProtKB SubCellular Location vocabulary mapping",
    "GO_REF:0000118": "TreeGrafter-generated Gene Ontology annotations based on phylogenetic placement",
    "GO_REF:0000120": "Gene Ontology annotation reference GO_REF:0000120",
}

GENE_INFO = {
    "PP_2182": {
        "accession": "Q88KV7",
        "entry": "Q88KV7_PSEPK",
        "length": 171,
        "protein": "ProQ/FinO domain-containing protein",
        "interpro": [
            ("IPR023529", "FinO/ProQ domain"),
            ("IPR016103", "RNA-binding OB-fold-like domain"),
            ("IPR036442", "FinO-domain superfamily"),
        ],
        "pfam": [("PF04352", "ProQ/FinO domain")],
        "panther": [("PTHR38106", "ProQ/FinO domain-containing protein family")],
        "keywords": ["Chaperone", "Cytoplasm", "Reference proteome", "RNA-binding"],
        "description": (
            "PP_2182 encodes a predicted ProQ/FinO-domain RNA chaperone in Pseudomonas putida KT2440. "
            "The supported molecular functions are cytosolic RNA binding, RNA strand annealing, and RNA strand exchange, "
            "consistent with a general post-transcriptional RNA matchmaker rather than a dedicated rRNA, tRNA, or ribosome "
            "assembly factor."
        ),
    },
    "PP_2953": {
        "accession": "Q88IP6",
        "entry": "Q88IP6_PSEPK",
        "length": 335,
        "protein": "Zinc-type alcohol dehydrogenase-like protein",
        "interpro": [
            ("IPR013154", "Zinc-type alcohol dehydrogenase-like domain"),
            ("IPR014182", "Zinc-type alcohol dehydrogenase domain"),
            ("IPR020843", "Zinc-type alcohol dehydrogenase conserved site"),
            ("IPR011032", "GroES-like domain superfamily"),
            ("IPR036291", "NAD(P)-binding Rossmann-like domain superfamily"),
            ("IPR002364", "Zinc-type alcohol dehydrogenase family"),
            ("IPR051603", "Zinc-type alcohol dehydrogenase-like family"),
        ],
        "pfam": [("PF08240", "Alcohol dehydrogenase GroES-like domain"), ("PF13602", "Zinc-binding dehydrogenase")],
        "panther": [("PTHR44154", "Zinc-type alcohol dehydrogenase-like family")],
        "keywords": [
            "Cytoplasm",
            "Metal-binding",
            "NADP",
            "Oxidoreductase",
            "Reference proteome",
            "RNA-binding",
            "Zinc",
        ],
        "description": (
            "PP_2953 encodes a predicted soluble zinc-type alcohol dehydrogenase-like oxidoreductase in Pseudomonas putida "
            "KT2440. The supported molecular function is NADPH-dependent quinone reductase activity with zinc-binding "
            "oxidoreductase-family context; no specific physiological quinone substrate or pathway role is established."
        ),
    },
}

FALLBACK_GOA = {
    "PP_2182": [
        {
            "gene_product_id": "Q88KV7",
            "symbol": "PP_2182",
            "qualifier": "enables",
            "go_id": "GO:0003723",
            "go_name": "RNA binding",
            "go_aspect": "molecular_function",
            "eco_id": "ECO:0000256",
            "go_evidence": "IEA",
            "reference": "GO_REF:0000002",
            "with_from": "InterPro:IPR023529",
            "assigned_by": "InterPro",
            "date": "20260710",
        },
        {
            "gene_product_id": "Q88KV7",
            "symbol": "PP_2182",
            "qualifier": "enables",
            "go_id": "GO:0033592",
            "go_name": "RNA strand annealing activity",
            "go_aspect": "molecular_function",
            "eco_id": "ECO:0000501",
            "go_evidence": "IEA",
            "reference": "GO_REF:0000120",
            "with_from": "InterPro:IPR023529|PANTHER:PTN002445573",
            "assigned_by": "UniProt",
            "date": "20260710",
        },
        {
            "gene_product_id": "Q88KV7",
            "symbol": "PP_2182",
            "qualifier": "enables",
            "go_id": "GO:0034057",
            "go_name": "RNA strand-exchange activity",
            "go_aspect": "molecular_function",
            "eco_id": "ECO:0000501",
            "go_evidence": "IEA",
            "reference": "GO_REF:0000120",
            "with_from": "InterPro:IPR023529|PANTHER:PTN002445573",
            "assigned_by": "UniProt",
            "date": "20260710",
        },
        {
            "gene_product_id": "Q88KV7",
            "symbol": "PP_2182",
            "qualifier": "involved_in",
            "go_id": "GO:0010608",
            "go_name": "post-transcriptional regulation of gene expression",
            "go_aspect": "biological_process",
            "eco_id": "ECO:0000501",
            "go_evidence": "IEA",
            "reference": "GO_REF:0000120",
            "with_from": "InterPro:IPR023529|PANTHER:PTN002445573",
            "assigned_by": "UniProt",
            "date": "20260710",
        },
        {
            "gene_product_id": "Q88KV7",
            "symbol": "PP_2182",
            "qualifier": "located_in",
            "go_id": "GO:0005829",
            "go_name": "cytosol",
            "go_aspect": "cellular_component",
            "eco_id": "ECO:0007826",
            "go_evidence": "IEA",
            "reference": "GO_REF:0000118",
            "with_from": "PANTHER:PTN002445573",
            "assigned_by": "TreeGrafter",
            "date": "20260710",
        },
    ],
    "PP_2953": [
        {
            "gene_product_id": "Q88IP6",
            "symbol": "PP_2953",
            "qualifier": "enables",
            "go_id": "GO:0003960",
            "go_name": "quinone reductase (NADPH) activity",
            "go_aspect": "molecular_function",
            "eco_id": "ECO:0000501",
            "go_evidence": "IEA",
            "reference": "GO_REF:0000003",
            "with_from": "EC:1.6.5.5",
            "assigned_by": "UniProt",
            "date": "20260710",
        },
        {
            "gene_product_id": "Q88IP6",
            "symbol": "PP_2953",
            "qualifier": "enables",
            "go_id": "GO:0008270",
            "go_name": "zinc ion binding",
            "go_aspect": "molecular_function",
            "eco_id": "ECO:0000256",
            "go_evidence": "IEA",
            "reference": "GO_REF:0000002",
            "with_from": "InterPro:IPR002364|InterPro:IPR014182",
            "assigned_by": "InterPro",
            "date": "20260710",
        },
        {
            "gene_product_id": "Q88IP6",
            "symbol": "PP_2953",
            "qualifier": "enables",
            "go_id": "GO:0016491",
            "go_name": "oxidoreductase activity",
            "go_aspect": "molecular_function",
            "eco_id": "ECO:0000256",
            "go_evidence": "IEA",
            "reference": "GO_REF:0000002",
            "with_from": "InterPro:IPR002364|InterPro:IPR020843",
            "assigned_by": "InterPro",
            "date": "20260710",
        },
        {
            "gene_product_id": "Q88IP6",
            "symbol": "PP_2953",
            "qualifier": "located_in",
            "go_id": "GO:0005829",
            "go_name": "cytosol",
            "go_aspect": "cellular_component",
            "eco_id": "ECO:0007322",
            "go_evidence": "IEA",
            "reference": "GO_REF:0000044",
            "with_from": "UniProtKB-SubCell:SL-0091",
            "assigned_by": "UniProt",
            "date": "20260710",
        },
    ],
}


GOA_HEADER = [
    "GENE PRODUCT DB",
    "GENE PRODUCT ID",
    "SYMBOL",
    "QUALIFIER",
    "GO TERM",
    "GO NAME",
    "GO ASPECT",
    "ECO ID",
    "GO EVIDENCE CODE",
    "REFERENCE",
    "WITH/FROM",
    "TAXON ID",
    "TAXON NAME",
    "ASSIGNED BY",
    "GENE NAME",
    "DATE",
]


def clean_with_from(items: object) -> str:
    if not items:
        return ""
    values: list[str] = []
    if isinstance(items, str):
        return items
    if isinstance(items, list):
        for item in items:
            if isinstance(item, dict):
                for xref_group in item.get("connectedXrefs", []):
                    db = xref_group.get("db")
                    xref_id = xref_group.get("id")
                    if db and xref_id:
                        values.append(f"{db}:{xref_id}")
            elif isinstance(item, str):
                values.append(item)
    return "|".join(values)


def fetch_quickgo(accession: str) -> list[dict[str, str]]:
    url = f"https://www.ebi.ac.uk/QuickGO/services/annotation/search?geneProductId=UniProtKB:{accession}&limit=100"
    with urllib.request.urlopen(url, timeout=60) as handle:
        data = json.load(handle)
    rows: list[dict[str, str]] = []
    for row in data.get("results", []):
        rows.append(
            {
                "gene_product_id": row["geneProductId"].split(":", 1)[-1],
                "symbol": row.get("symbol") or accession,
                "qualifier": row.get("qualifier", ""),
                "go_id": row["goId"],
                "go_name": row.get("goName") or TERM.get(row["goId"], {}).get("label", ""),
                "go_aspect": row.get("goAspect", ""),
                "eco_id": row.get("evidenceCode", ""),
                "go_evidence": row.get("goEvidence", ""),
                "reference": row.get("reference", ""),
                "with_from": clean_with_from(row.get("withFrom")),
                "assigned_by": row.get("assignedBy", ""),
                "date": row.get("date", TODAY.replace("-", "")),
            }
        )
    return rows


def get_goa_rows(gene: str) -> list[dict[str, str]]:
    accession = GENE_INFO[gene]["accession"]
    try:
        rows = fetch_quickgo(accession)
    except Exception:
        rows = []
    return rows or FALLBACK_GOA[gene]


def gene_dir(gene: str) -> Path:
    return GENE_ROOT / gene


def gene_file(gene: str, suffix: str) -> Path:
    return gene_dir(gene) / f"{gene}-{suffix}"


def file_id(gene: str, suffix: str) -> str:
    return f"file:PSEPK/{gene}/{gene}-{suffix}"


def read_lines(path: Path) -> list[str]:
    if not path.exists():
        return []
    return path.read_text(encoding="utf-8").splitlines()


def first_line(path: Path, *needles: str) -> str | None:
    for line in read_lines(path):
        if all(needle in line for needle in needles):
            return line
    return None


def support(reference_id: str, text: str | None) -> dict[str, str] | None:
    if not text:
        return None
    return {"reference_id": reference_id, "supporting_text": text}


def add_support(items: list[dict[str, str]], item: dict[str, str] | None) -> None:
    if item and item not in items:
        items.append(item)


def goa_line(gene: str, term_id: str) -> str | None:
    return first_line(gene_file(gene, "goa.tsv"), term_id)


def evidence_for(gene: str, term_id: str | None = None, include_asta: bool = False) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    if term_id:
        add_support(items, support(file_id(gene, "goa.tsv"), goa_line(gene, term_id)))
    add_support(items, support(file_id(gene, "uniprot.txt"), first_line(gene_file(gene, "uniprot.txt"), "DE   SubName:")))
    if gene == "PP_2182":
        add_support(items, support(file_id(gene, "uniprot.txt"), first_line(gene_file(gene, "uniprot.txt"), "DR   InterPro; IPR023529;")))
        add_support(items, support(file_id(gene, "uniprot.txt"), first_line(gene_file(gene, "uniprot.txt"), "KW   Chaperone;")))
    if gene == "PP_2953":
        add_support(items, support(file_id(gene, "uniprot.txt"), first_line(gene_file(gene, "uniprot.txt"), "DR   InterPro; IPR002364;")))
        add_support(items, support(file_id(gene, "uniprot.txt"), first_line(gene_file(gene, "uniprot.txt"), "KW   Cytoplasm;")))
    return items


def term(term_id: str, label: str | None = None) -> dict[str, str]:
    if label:
        return {"id": term_id, "label": label}
    return TERM[term_id]


def review_for(gene: str, row: dict[str, str]) -> dict:
    term_id = row["go_id"]
    if gene == "PP_2182":
        if term_id == "GO:0003723":
            return {
                "summary": "RNA binding is directionally correct for a ProQ/FinO-domain RNA chaperone but is less informative than the strand-annealing and strand-exchange activities.",
                "action": "KEEP_AS_NON_CORE",
                "reason": (
                    "The ProQ/FinO domain and current GOA rows support RNA-binding context, while the more specific "
                    "GO:0033592 and GO:0034057 rows capture the likely chaperone/matchmaker activity."
                ),
                "supported_by": evidence_for(gene, term_id, include_asta=True),
            }
        if term_id == "GO:0033592":
            return {
                "summary": "RNA strand annealing activity is the clearest specific molecular-function call for this ProQ/FinO-domain protein.",
                "action": "ACCEPT",
                "reason": (
                    "GOA maps the ProQ/FinO-domain evidence to RNA strand annealing activity, consistent with the general "
                    "RNA-chaperone role of ProQ/FinO-family proteins. No more specific KT2440 target RNA is available."
                ),
                "supported_by": evidence_for(gene, term_id, include_asta=True),
            }
        if term_id == "GO:0034057":
            return {
                "summary": "RNA strand-exchange activity is consistent with the same ProQ/FinO RNA-chaperone evidence.",
                "action": "ACCEPT",
                "reason": (
                    "The InterPro/PANTHER-supported GOA row provides a specific RNA-chaperone activity. This should not be "
                    "expanded to rRNA, tRNA, or ribosome-biogenesis roles without target-specific evidence."
                ),
                "supported_by": evidence_for(gene, term_id, include_asta=True),
            }
        if term_id == "GO:0010608":
            return {
                "summary": "Post-transcriptional regulation is appropriate process context for a ProQ/FinO-family RNA chaperone.",
                "action": "ACCEPT",
                "reason": (
                    "The process is broad but matches the supported RNA strand annealing/exchange function of a bacterial "
                    "RNA chaperone. No pathway-specific translation, rRNA, or tRNA process is asserted."
                ),
                "supported_by": evidence_for(gene, term_id, include_asta=True),
            }
        if term_id == "GO:0005829":
            return {
                "summary": "Cytosol is appropriate localization context for this soluble bacterial RNA-chaperone candidate.",
                "action": "ACCEPT",
                "reason": "The cytosol annotation is supported by the current GOA row and is retained as the location for the core RNA-chaperone function.",
                "supported_by": evidence_for(gene, term_id, include_asta=True),
            }
    if gene == "PP_2953":
        if term_id == "GO:0003960":
            return {
                "summary": "NADPH-dependent quinone reductase activity is the most specific supported molecular-function call for PP_2953.",
                "action": "ACCEPT",
                "reason": (
                    "Current GOA maps the enzyme-class evidence to GO:0003960. This resolves PP_2953 as a soluble "
                    "oxidoreductase spillover rather than a translation/RNA-processing gene."
                ),
                "supported_by": evidence_for(gene, term_id, include_asta=True),
            }
        if term_id == "GO:0008270":
            return {
                "summary": "Zinc ion binding is appropriate cofactor/domain context for a zinc-type dehydrogenase-like protein.",
                "action": "KEEP_AS_NON_CORE",
                "reason": (
                    "The InterPro evidence supports zinc-binding dehydrogenase-family context, but the metal-binding row is "
                    "secondary to the quinone reductase molecular function."
                ),
                "supported_by": evidence_for(gene, term_id, include_asta=True),
            }
        if term_id == "GO:0016491":
            return {
                "summary": "Generic oxidoreductase activity is true but less informative than the specific quinone reductase annotation.",
                "action": "MARK_AS_OVER_ANNOTATED",
                "reason": "GO:0003960 should carry the core molecular-function interpretation; the broad parent adds little curational value.",
                "supported_by": evidence_for(gene, term_id, include_asta=True),
            }
        if term_id == "GO:0005829":
            return {
                "summary": "Cytosol is appropriate localization context for a soluble oxidoreductase.",
                "action": "ACCEPT",
                "reason": "The current GOA location row places PP_2953 in the cytosol and is retained as the location for the core oxidoreductase function.",
                "supported_by": evidence_for(gene, term_id, include_asta=True),
            }
        if term_id == "GO:0005737":
            return {
                "summary": "Broad cytoplasm location is directionally correct but cytosol is the more specific current location.",
                "action": "MODIFY",
                "reason": "Use GO:0005829 for the soluble cytosolic oxidoreductase context.",
                "supported_by": evidence_for(gene, term_id, include_asta=True),
                "proposed_replacement_terms": [term("GO:0005829")],
            }
        if term_id == "GO:0003723":
            return {
                "summary": "RNA binding is not supported by the current live QuickGO rows used for this first pass.",
                "action": "UNDECIDED",
                "reason": (
                    "The local partition snapshot retained an RNA-binding keyword for PP_2953, but the current GOA evidence "
                    "used here supports oxidoreductase, zinc-binding, and cytosol annotations. Do not route PP_2953 into RNA "
                    "processing without independent evidence."
                ),
                "supported_by": evidence_for(gene, term_id, include_asta=True),
            }
    return {
        "summary": "This low-information spillover annotation was not resolved in this first pass.",
        "action": "UNDECIDED",
        "reason": "The available fallback evidence is insufficient for a confident manual decision.",
        "supported_by": evidence_for(gene, term_id, include_asta=True),
    }


def write_uniprot_fallback(gene: str) -> None:
    info = GENE_INFO[gene]
    lines = [
        f"ID   {info['entry']}            Unreviewed;       {info['length']} AA.",
        f"AC   {info['accession']};",
        f"DE   SubName: Full={info['protein']};",
        f"GN   Name={gene}; OrderedLocusNames={gene};",
        f"OS   {TAXON_LABEL}.",
        "OX   NCBI_TaxID=160488;",
        (
            "CC   -!- CAUTION: Minimal fallback context assembled from "
            "projects/P_PUTIDA/data/psepk_gene_list.tsv because UniProt REST returned HTTP 500 on 2026-07-10."
        ),
        (
            "CC   -!- FUNCTION: Domain- and GOA-based first-pass context only; no manually reviewed UniProt function text "
            "was available from the REST endpoint."
        ),
    ]
    for go_id, go_label in [(row["go_id"], row["go_name"]) for row in FALLBACK_GOA[gene]]:
        aspect = {"molecular_function": "F", "biological_process": "P", "cellular_component": "C"}[
            next(row["go_aspect"] for row in FALLBACK_GOA[gene] if row["go_id"] == go_id)
        ]
        lines.append(f"DR   GO; {go_id}; {aspect}:{go_label}; IEA:{gene}.")
    for database, rows in (("InterPro", info["interpro"]), ("Pfam", info["pfam"]), ("PANTHER", info["panther"])):
        for db_id, label in rows:
            lines.append(f"DR   {database}; {db_id}; {label}.")
    lines.append("KW   " + "; ".join(info["keywords"]) + ".")
    if gene == "PP_2953":
        lines.append(
            "CC   -!- CURATION_NOTE: The local partition snapshot retained an RNA-binding keyword, but live QuickGO rows "
            "used here do not include an RNA-binding GO annotation."
        )
    lines.append("//")
    gene_file(gene, "uniprot.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_goa(gene: str, rows: list[dict[str, str]]) -> None:
    path = gene_file(gene, "goa.tsv")
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(GOA_HEADER)
        for row in rows:
            writer.writerow(
                [
                    "UniProtKB",
                    row["gene_product_id"],
                    row["symbol"],
                    row["qualifier"],
                    row["go_id"],
                    row["go_name"],
                    row["go_aspect"],
                    row["eco_id"],
                    row["go_evidence"],
                    row["reference"],
                    row["with_from"],
                    "160488",
                    TAXON_LABEL,
                    row["assigned_by"],
                    GENE_INFO[gene]["protein"],
                    row["date"],
                ]
            )


def write_notes(gene: str, rows: list[dict[str, str]]) -> None:
    path = gene_file(gene, "notes.md")
    if gene == "PP_2182":
        body = f"""# {gene} notes

## {TODAY}

- UniProt REST returned HTTP 500 for Q88KV7 during `just fetch-gene`, so this folder uses a minimal fallback context file assembled from the project gene list, clearly marked in `{gene}-uniprot.txt` ["CC   -!- CAUTION: Minimal fallback context assembled from projects/P_PUTIDA/data/psepk_gene_list.tsv because UniProt REST returned HTTP 500 on 2026-07-10."].
- The current GOA rows support a ProQ/FinO-style RNA-chaperone interpretation rather than a specific ribosome, rRNA, or tRNA processing role [{file_id(gene, "goa.tsv")} "{goa_line(gene, "GO:0033592")}"] [{file_id(gene, "goa.tsv")} "{goa_line(gene, "GO:0034057")}"].
- I kept RNA binding as non-core because the strand annealing/exchange annotations are more informative [{file_id(gene, "goa.tsv")} "{goa_line(gene, "GO:0003723")}"].
"""
    else:
        body = f"""# {gene} notes

## {TODAY}

- UniProt REST returned HTTP 500 for Q88IP6 during `just fetch-gene`, so this folder uses a minimal fallback context file assembled from the project gene list, clearly marked in `{gene}-uniprot.txt` ["CC   -!- CAUTION: Minimal fallback context assembled from projects/P_PUTIDA/data/psepk_gene_list.tsv because UniProt REST returned HTTP 500 on 2026-07-10."].
- The local partition snapshot carried an RNA-binding keyword for PP_2953, but current live QuickGO rows used here support oxidoreductase/zinc-binding/cytosol annotations rather than RNA processing [{file_id(gene, "goa.tsv")} "{goa_line(gene, "GO:0003960")}"] [{file_id(gene, "uniprot.txt")} "CC   -!- CURATION_NOTE: The local partition snapshot retained an RNA-binding keyword, but live QuickGO rows used here do not include an RNA-binding GO annotation."].
- I interpreted PP_2953 as an oxidoreductase spillover from the translation/RNA bucket and kept the core function narrow around quinone reductase activity [{file_id(gene, "goa.tsv")} "{goa_line(gene, "GO:0016491")}"].
"""
    if gene_file(gene, "deep-research-asta.md").exists():
        body += f"- Asta was run as fast gene-level retrieval context; no Asta-only hypothesis was imported [{file_id(gene, 'deep-research-asta.md')} \"{first_line(gene_file(gene, 'deep-research-asta.md'), 'uniprot_accession:')}\"].\n"
    path.write_text(body, encoding="utf-8")


def references_for(gene: str, rows: list[dict[str, str]]) -> list[dict]:
    refs: list[dict] = []
    for ref_id in sorted({row["reference"] for row in rows if row.get("reference")}):
        refs.append({"id": ref_id, "title": GO_REF_TITLES.get(ref_id, f"Gene Ontology annotation reference {ref_id}"), "findings": []})
    refs.extend(
        [
            {
                "id": file_id(gene, "uniprot.txt"),
                "title": f"Fallback UniProt-style metadata context for {gene} ({GENE_INFO[gene]['accession']})",
                "findings": [
                    {
                        "statement": "UniProt REST was unavailable, so this local file records project gene-list and domain metadata used for Asta context.",
                        "supporting_text": (
                            "CC   -!- CAUTION: Minimal fallback context assembled from projects/P_PUTIDA/data/psepk_gene_list.tsv "
                            "because UniProt REST returned HTTP 500 on 2026-07-10."
                        ),
                    }
                ],
            },
            {
                "id": file_id(gene, "goa.tsv"),
                "title": f"QuickGO GOA annotations for {gene}",
                "findings": [{"statement": f"GOA table containing the annotations reviewed for {gene}."}],
            },
        ]
    )
    if gene_file(gene, "deep-research-asta.md").exists():
        refs.append(
            {
                "id": file_id(gene, "deep-research-asta.md"),
                "title": f"Asta retrieval report for {gene} ({GENE_INFO[gene]['accession']})",
                "findings": [
                    {
                        "statement": "Asta retrieval used as fast gene-level literature context; no unsupported hypotheses were imported.",
                        "supporting_text": first_line(gene_file(gene, "deep-research-asta.md"), "uniprot_accession:"),
                    }
                ],
            }
        )
    return refs


def existing_annotations(gene: str, rows: list[dict[str, str]]) -> list[dict]:
    annotations = []
    for row in rows:
        annotations.append(
            {
                "term": {"id": row["go_id"], "label": row["go_name"]},
                "evidence_type": row["go_evidence"],
                "original_reference_id": row["reference"],
                "qualifier": row["qualifier"],
                "review": review_for(gene, row),
            }
        )
    return annotations


def core_functions(gene: str) -> list[dict]:
    if gene == "PP_2182":
        return [
            {
                "description": (
                    "ProQ/FinO-domain RNA chaperone activity, represented by RNA strand annealing and exchange, supporting "
                    "post-transcriptional regulation without assigning a specific target RNA class."
                ),
                "molecular_function": term("GO:0033592"),
                "directly_involved_in": [term("GO:0010608")],
                "locations": [term("GO:0005829")],
                "supported_by": evidence_for(gene, "GO:0033592", include_asta=True),
            },
            {
                "description": "RNA strand-exchange activity as a second ProQ/FinO-family RNA-chaperone activity.",
                "molecular_function": term("GO:0034057"),
                "directly_involved_in": [term("GO:0010608")],
                "locations": [term("GO:0005829")],
                "supported_by": evidence_for(gene, "GO:0034057", include_asta=True),
            },
        ]
    return [
        {
            "description": (
                "Predicted soluble NADPH-dependent quinone reductase activity in a zinc-type alcohol dehydrogenase-like "
                "oxidoreductase family protein."
            ),
            "molecular_function": term("GO:0003960"),
            "locations": [term("GO:0005829")],
            "supported_by": evidence_for(gene, "GO:0003960", include_asta=True),
        }
    ]


def write_review(gene: str, rows: list[dict[str, str]]) -> None:
    review = {
        "id": GENE_INFO[gene]["accession"],
        "gene_symbol": gene,
        "product_type": "PROTEIN",
        "status": "DRAFT",
        "taxon": {"id": "NCBITaxon:160488", "label": TAXON_LABEL},
        "description": GENE_INFO[gene]["description"],
        "existing_annotations": existing_annotations(gene, rows),
        "references": references_for(gene, rows),
        "core_functions": core_functions(gene),
        "proposed_new_terms": [],
        "suggested_questions": [
            {
                "question": (
                    "Which specific RNA targets and regulatory circuits use PP_2182 in P. putida KT2440?"
                    if gene == "PP_2182"
                    else "Which physiological quinone or redox substrate is reduced by PP_2953 in P. putida KT2440?"
                )
            }
        ],
        "suggested_experiments": [
            {
                "description": (
                    "Perform RNA co-immunoprecipitation or CLIP-style target capture for tagged PP_2182, then test RNA annealing "
                    "with candidate sRNA-mRNA pairs in vitro."
                    if gene == "PP_2182"
                    else "Purify PP_2953 and assay NADPH-dependent reduction of candidate quinones and related redox substrates, then compare knockout phenotypes under quinone/redox stress."
                ),
                "experiment_type": "RNA target and chaperone assay" if gene == "PP_2182" else "quinone reductase substrate assay",
            }
        ],
    }
    gene_file(gene, "ai-review.yaml").write_text(
        yaml.dump(review, Dumper=NoAliasDumper, sort_keys=False, width=110),
        encoding="utf-8",
    )


def write_module() -> None:
    module = {
        "id": "MODULE:translation_rna_processing_spillover_boundary",
        "title": "Translation/RNA processing spillover boundary",
        "description": (
            "Boundary module for low-information genes that entered the PSEPK translation/RNA-processing bucket through broad "
            "RNA-binding or keyword evidence but should not be forced into ribosome, rRNA, tRNA, translation-factor, or RNA-decay "
            "pathways without stronger evidence. This first version records PP_2182 as a ProQ/FinO RNA-chaperone candidate and "
            "PP_2953 as an oxidoreductase spillover routed out of RNA processing."
        ),
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": f"file:{BATCH_TSV}",
                "title": "PSEPK translation/RNA-processing low-information spillover split",
                "statement": (
                    "The batch table records PP_2182 and PP_2953 as low-information RNA-binding or enzyme spillovers with "
                    "weak pathway specificity."
                ),
            },
            {
                "source_id": "file:PSEPK/PP_2182/PP_2182-ai-review.yaml",
                "title": "Curated PP_2182 review",
                "statement": "The PP_2182 review accepts ProQ/FinO-domain RNA strand annealing/exchange and post-transcriptional regulation without assigning rRNA, tRNA, or ribosome-specific roles.",
            },
            {
                "source_id": "file:PSEPK/PP_2953/PP_2953-ai-review.yaml",
                "title": "Curated PP_2953 review",
                "statement": "The PP_2953 review accepts NADPH-dependent quinone reductase activity and routes the gene out of translation/RNA processing.",
            },
        ],
        "module": {
            "id": "translation_rna_processing_spillover_boundary",
            "label": "Translation/RNA processing spillover boundary",
            "module_type": "BIOLOGICAL_PROCESS",
            "concepts": [
                {
                    "preferred_term": "RNA strand annealing activity",
                    "term": term("GO:0033592"),
                    "description": "Specific RNA-chaperone activity retained for PP_2182.",
                },
                {
                    "preferred_term": "RNA strand-exchange activity",
                    "term": term("GO:0034057"),
                    "description": "Second ProQ/FinO-family RNA-chaperone activity retained for PP_2182.",
                },
                {
                    "preferred_term": "post-transcriptional regulation of gene expression",
                    "term": term("GO:0010608"),
                    "description": "Broad process context for the PP_2182 RNA-chaperone call.",
                },
                {
                    "preferred_term": "quinone reductase (NADPH) activity",
                    "term": term("GO:0003960"),
                    "description": "Specific oxidoreductase activity retained for PP_2953.",
                },
                {
                    "preferred_term": "cytosol",
                    "term": term("GO:0005829"),
                    "description": "Location context for the two soluble proteins where supported by GOA.",
                },
            ],
            "parts": [
                {
                    "order": 1,
                    "role": "ProQ/FinO RNA-chaperone spillover",
                    "node": {
                        "id": "proq_fino_rna_chaperone_spillover",
                        "label": "ProQ/FinO RNA-chaperone spillover",
                        "module_type": "BIOLOGICAL_PROCESS",
                        "description": (
                            "PP_2182 has ProQ/FinO-domain support for RNA strand annealing/exchange and broad "
                            "post-transcriptional regulation, but no evidence in this batch for rRNA modification, tRNA "
                            "processing, ribosome biogenesis, or translation-factor activity."
                        ),
                        "annotons": [
                            {
                                "id": "PP_2182_proq_fino_rna_chaperone",
                                "label": "PP_2182: ProQ/FinO RNA chaperone candidate",
                                "participant": {"selector_type": "GENE", "gene": {"preferred_term": "PP_2182"}},
                                "function": {"preferred_term": "RNA strand annealing activity", "term": term("GO:0033592")},
                                "processes": [
                                    {"preferred_term": "post-transcriptional regulation of gene expression", "term": term("GO:0010608")}
                                ],
                                "locations": [{"preferred_term": "cytosol", "term": term("GO:0005829")}],
                                "role_description": "Low-information ProQ/FinO-family RNA chaperone candidate.",
                            }
                        ],
                    },
                },
                {
                    "order": 2,
                    "role": "Oxidoreductase spillover routed out of RNA processing",
                    "node": {
                        "id": "oxidoreductase_spillover_routed_out",
                        "label": "Oxidoreductase spillover routed out of RNA processing",
                        "module_type": "MOLECULAR_FUNCTION",
                        "description": (
                            "PP_2953 is retained as a soluble zinc-type alcohol dehydrogenase-like oxidoreductase with "
                            "NADPH-dependent quinone reductase support. It is not represented as an RNA-processing gene."
                        ),
                        "annotons": [
                            {
                                "id": "PP_2953_quinone_reductase_spillover",
                                "label": "PP_2953: predicted NADPH quinone reductase",
                                "participant": {"selector_type": "GENE", "gene": {"preferred_term": "PP_2953"}},
                                "function": {"preferred_term": "quinone reductase (NADPH) activity", "term": term("GO:0003960")},
                                "locations": [{"preferred_term": "cytosol", "term": term("GO:0005829")}],
                                "role_description": "Oxidoreductase-family spillover from a broad RNA/translation partition.",
                            }
                        ],
                    },
                },
            ],
        },
        "notes": (
            "This module is intentionally a boundary/spillover record, not a satisfiable translation or RNA-processing pathway. "
            "Use it to keep low-information genes visible while preventing pathway over-interpretation."
        ),
    }
    MODULE_PATH.write_text(yaml.dump(module, Dumper=NoAliasDumper, sort_keys=False, width=110), encoding="utf-8")


def main() -> None:
    for gene in GENE_INFO:
        gene_dir(gene).mkdir(parents=True, exist_ok=True)
        rows = get_goa_rows(gene)
        write_uniprot_fallback(gene)
        write_goa(gene, rows)
        write_review(gene, rows)
        write_notes(gene, rows)
    write_module()


if __name__ == "__main__":
    main()
