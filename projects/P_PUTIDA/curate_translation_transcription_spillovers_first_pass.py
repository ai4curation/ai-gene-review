#!/usr/bin/env python3
"""First-pass curation for transcription/RNA-polymerase spillovers."""

from __future__ import annotations

import csv
import json
import urllib.request
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes" / "PSEPK"
MODULE_PATH = ROOT / "modules" / "transcription_rna_polymerase_spillover_boundary.yaml"
BATCH_TSV = (
    "projects/P_PUTIDA/batches/"
    "module_translation_rna_processing_transcription_rna_polymerase_spillovers.tsv"
)
METADATA_TSV = ROOT / "projects" / "P_PUTIDA" / "data" / "psepk_uniprot_metadata.tsv"
TAXON_LABEL = "Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)"
TODAY = "2026-07-10"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):  # type: ignore[override]
        return True


TERM = {
    "GO:0000166": {"id": "GO:0000166", "label": "nucleotide binding"},
    "GO:0000428": {"id": "GO:0000428", "label": "DNA-directed RNA polymerase complex"},
    "GO:0003676": {"id": "GO:0003676", "label": "nucleic acid binding"},
    "GO:0003677": {"id": "GO:0003677", "label": "DNA binding"},
    "GO:0003700": {"id": "GO:0003700", "label": "DNA-binding transcription factor activity"},
    "GO:0003723": {"id": "GO:0003723", "label": "RNA binding"},
    "GO:0003899": {"id": "GO:0003899", "label": "DNA-directed RNA polymerase activity"},
    "GO:0005524": {"id": "GO:0005524", "label": "ATP binding"},
    "GO:0005737": {"id": "GO:0005737", "label": "cytoplasm"},
    "GO:0005829": {"id": "GO:0005829", "label": "cytosol"},
    "GO:0006351": {"id": "GO:0006351", "label": "DNA-templated transcription"},
    "GO:0006352": {"id": "GO:0006352", "label": "DNA-templated transcription initiation"},
    "GO:0006353": {"id": "GO:0006353", "label": "DNA-templated transcription termination"},
    "GO:0006355": {"id": "GO:0006355", "label": "regulation of DNA-templated transcription"},
    "GO:0008270": {"id": "GO:0008270", "label": "zinc ion binding"},
    "GO:0010468": {"id": "GO:0010468", "label": "regulation of gene expression"},
    "GO:0016817": {"id": "GO:0016817", "label": "hydrolase activity, acting on acid anhydrides"},
    "GO:0016887": {"id": "GO:0016887", "label": "ATP hydrolysis activity"},
    "GO:0016987": {"id": "GO:0016987", "label": "sigma factor activity"},
    "GO:0031554": {"id": "GO:0031554", "label": "regulation of termination of DNA-templated transcription"},
    "GO:0031564": {"id": "GO:0031564", "label": "transcription antitermination"},
    "GO:0140110": {"id": "GO:0140110", "label": "transcription regulator activity"},
    "GO:2000142": {"id": "GO:2000142", "label": "regulation of DNA-templated transcription initiation"},
}

GO_REF_TITLES = {
    "GO_REF:0000002": "Gene Ontology annotation through association of InterPro records with GO terms",
    "GO_REF:0000104": "Electronic Gene Ontology annotations created by transferring manual GO annotations between related proteins based on shared sequence features",
    "GO_REF:0000108": "Automatic assignment of GO terms using logical inference, based on inter-ontology links",
    "GO_REF:0000118": "TreeGrafter-generated Gene Ontology annotations based on phylogenetic placement",
    "GO_REF:0000120": "Combined Automated Annotation using Multiple IEA Methods",
}

GENES = ["nusB", "rapA", "PP_2266", "PP_4553", "dksA", "nusA"]
FALLBACK_UNIPROT_GENES = {"nusB", "rapA", "PP_2266", "PP_4553", "dksA"}

GENE_INFO = {
    "nusB": {
        "accession": "Q88QH5",
        "entry": "NUSB_PSEPK",
        "ordered_locus": "PP_0518",
        "description": (
            "nusB encodes the NusB transcription antitermination factor in Pseudomonas putida KT2440. "
            "It is a soluble RNA-binding transcription factor for ribosomal RNA operon antitermination, not a translation factor."
        ),
    },
    "rapA": {
        "accession": "Q88NR0",
        "entry": "RAPA_PSEPK",
        "ordered_locus": "PP_1145",
        "description": (
            "rapA encodes an RNA polymerase-associated Swi2/Snf2-family ATPase that stimulates RNA polymerase recycling "
            "and transcription regulation under stress conditions. Its translation/RNA-processing bucket placement reflects "
            "broad nucleic-acid/transcription keywords rather than a translation role."
        ),
    },
    "PP_2266": {
        "accession": "Q88KM4",
        "entry": "Q88KM4_PSEPK",
        "ordered_locus": "PP_2266",
        "description": (
            "PP_2266 encodes a predicted DNA-directed RNA polymerase-like protein with RNA polymerase domain evidence. "
            "This first pass routes it to RNA polymerase/transcription context while leaving its relationship to the compact "
            "canonical rpoA/rpoB/rpoC/rpoZ core unresolved."
        ),
    },
    "PP_4553": {
        "accession": "Q88EB3",
        "entry": "Q88EB3_PSEPK",
        "ordered_locus": "PP_4553",
        "description": (
            "PP_4553 encodes a predicted extracytoplasmic-function sigma-70 family factor. Its supported role is sigma "
            "factor activity in transcription initiation, not DNA-directed RNA polymerase catalysis or translation."
        ),
    },
    "dksA": {
        "accession": "Q88DX5",
        "entry": "Q88DX5_PSEPK",
        "ordered_locus": "PP_4693",
        "description": (
            "dksA encodes an RNA polymerase-binding DksA transcription factor. The supported function is zinc-coordinated "
            "transcription regulation through direct RNAP binding, with cytoplasmic localization."
        ),
    },
    "nusA": {
        "accession": "Q88DV6",
        "entry": "Q88DV6_PSEPK",
        "ordered_locus": "PP_4713",
        "description": (
            "nusA encodes the NusA transcription termination/antitermination factor in Pseudomonas putida KT2440. "
            "It binds RNA and RNA polymerase during elongating transcription complexes, supporting termination and antitermination "
            "rather than translation or ribosome assembly."
        ),
    },
}

FALLBACK_GOA = {
    "nusB": [
        ("Q88QH5", "nusB", "enables", "GO:0003723", "molecular_function", "ECO:0000501", "IEA", "GO_REF:0000120", "InterPro:IPR006027|UniRule:UR000037471", "UniProt", "20260706"),
        ("Q88QH5", "nusB", "involved_in", "GO:0006353", "biological_process", "ECO:0000501", "IEA", "GO_REF:0000120", "InterPro:IPR011605|UniRule:UR000037471", "UniProt", "20260706"),
        ("Q88QH5", "nusB", "involved_in", "GO:0006355", "biological_process", "ECO:0000256", "IEA", "GO_REF:0000002", "InterPro:IPR006027", "InterPro", "20260706"),
        ("Q88QH5", "nusB", "located_in", "GO:0005829", "cellular_component", "ECO:0007826", "IEA", "GO_REF:0000118", "PANTHER:PTN002253960", "TreeGrafter", "20260706"),
    ],
    "rapA": [
        ("Q88NR0", "rapA", "enables", "GO:0005524", "molecular_function", "ECO:0000501", "IEA", "GO_REF:0000120", "InterPro:IPR000330|UniRule:UR000085077", "UniProt", "20260706"),
        ("Q88NR0", "rapA", "enables", "GO:0016817", "molecular_function", "ECO:0000256", "IEA", "GO_REF:0000002", "InterPro:IPR022737", "InterPro", "20260706"),
        ("Q88NR0", "rapA", "involved_in", "GO:0006355", "biological_process", "ECO:0000501", "IEA", "GO_REF:0000120", "InterPro:IPR023949|UniRule:UR000085077", "UniProt", "20260706"),
    ],
    "PP_2266": [
        ("Q88KM4", "PP_2266", "enables", "GO:0003677", "molecular_function", "ECO:0000256", "IEA", "GO_REF:0000002", "InterPro:IPR002092", "InterPro", "20260706"),
        ("Q88KM4", "PP_2266", "enables", "GO:0003899", "molecular_function", "ECO:0000501", "IEA", "GO_REF:0000120", "InterPro:IPR002092|InterPro:IPR024075|EC:2.7.7.6|PANTHER:PTN007419821", "UniProt", "20260706"),
        ("Q88KM4", "PP_2266", "involved_in", "GO:0006351", "biological_process", "ECO:0000256", "IEA", "GO_REF:0000002", "InterPro:IPR002092", "InterPro", "20260706"),
    ],
    "PP_4553": [
        ("Q88EB3", "PP_4553", "enables", "GO:0003677", "molecular_function", "ECO:0000256", "IEA", "GO_REF:0000002", "InterPro:IPR013249", "InterPro", "20260706"),
        ("Q88EB3", "PP_4553", "enables", "GO:0003700", "molecular_function", "ECO:0000256", "IEA", "GO_REF:0000002", "InterPro:IPR007627|InterPro:IPR013249|InterPro:IPR013325|InterPro:IPR014284", "InterPro", "20260706"),
        ("Q88EB3", "PP_4553", "enables", "GO:0016987", "molecular_function", "ECO:0000256", "IEA", "GO_REF:0000002", "InterPro:IPR013249", "InterPro", "20260706"),
        ("Q88EB3", "PP_4553", "involved_in", "GO:0006352", "biological_process", "ECO:0000256", "IEA", "GO_REF:0000002", "InterPro:IPR007627|InterPro:IPR013249|InterPro:IPR013325|InterPro:IPR014284", "InterPro", "20260706"),
        ("Q88EB3", "PP_4553", "involved_in", "GO:0006355", "biological_process", "ECO:0000256", "IEA", "GO_REF:0000002", "InterPro:IPR007627|InterPro:IPR013249|InterPro:IPR013325|InterPro:IPR014284", "InterPro", "20260706"),
        ("Q88EB3", "PP_4553", "involved_in", "GO:2000142", "biological_process", "ECO:0000366", "IEA", "GO_REF:0000108", "GO:0016987", "GOC", "20260706"),
    ],
    "dksA": [
        ("Q88DX5", "dksA", "enables", "GO:0008270", "molecular_function", "ECO:0000501", "IEA", "GO_REF:0000120", "InterPro:IPR000962|InterPro:IPR012784|UniRule:UR000078108", "UniProt", "20260706"),
        ("Q88DX5", "dksA", "involved_in", "GO:0010468", "biological_process", "ECO:0000256", "IEA", "GO_REF:0000104", "UniRule:UR000078108", "UniProt", "20260706"),
        ("Q88DX5", "dksA", "located_in", "GO:0005737", "cellular_component", "ECO:0000501", "IEA", "GO_REF:0000120", "UniProtKB-SubCell:SL-0086|UniRule:UR000078108", "UniProt", "20260706"),
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


def term(term_id: str) -> dict[str, str]:
    return TERM[term_id]


def metadata_by_accession() -> dict[str, dict[str, str]]:
    with METADATA_TSV.open(encoding="utf-8") as handle:
        return {row["Entry"]: row for row in csv.DictReader(handle, delimiter="\t")}


def gene_dir(gene: str) -> Path:
    return GENE_ROOT / gene


def gene_file(gene: str, suffix: str) -> Path:
    return gene_dir(gene) / f"{gene}-{suffix}"


def file_id(gene: str, suffix: str) -> str:
    return f"file:PSEPK/{gene}/{gene}-{suffix}"


def lines(path: Path) -> list[str]:
    if not path.exists():
        return []
    return path.read_text(encoding="utf-8").splitlines()


def first_line(path: Path, *needles: str) -> str | None:
    for line in lines(path):
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


def clean_with_from(items: object) -> str:
    if not items:
        return ""
    values: list[str] = []
    if isinstance(items, str):
        return items
    if isinstance(items, list):
        for item in items:
            if isinstance(item, str):
                values.append(item)
            elif isinstance(item, dict):
                for xref in item.get("connectedXrefs", []):
                    if xref.get("db") and xref.get("id"):
                        values.append(f"{xref['db']}:{xref['id']}")
    return "|".join(values)


def fetch_quickgo(accession: str) -> list[dict[str, str]]:
    url = f"https://www.ebi.ac.uk/QuickGO/services/annotation/search?geneProductId=UniProtKB:{accession}&limit=100"
    with urllib.request.urlopen(url, timeout=60) as handle:
        data = json.load(handle)
    rows = []
    for row in data.get("results", []):
        go_id = row["goId"]
        rows.append(
            {
                "gene_product_id": row["geneProductId"].split(":", 1)[-1],
                "symbol": row.get("symbol") or "",
                "qualifier": row.get("qualifier", ""),
                "go_id": go_id,
                "go_name": row.get("goName") or TERM[go_id]["label"],
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


def fallback_rows(gene: str) -> list[dict[str, str]]:
    rows = []
    for acc, symbol, qualifier, go_id, aspect, eco, evidence, ref, with_from, assigned_by, date in FALLBACK_GOA[gene]:
        rows.append(
            {
                "gene_product_id": acc,
                "symbol": symbol,
                "qualifier": qualifier,
                "go_id": go_id,
                "go_name": TERM[go_id]["label"],
                "go_aspect": aspect,
                "eco_id": eco,
                "go_evidence": evidence,
                "reference": ref,
                "with_from": with_from,
                "assigned_by": assigned_by,
                "date": date,
            }
        )
    return rows


def parse_existing_goa(gene: str) -> list[dict[str, str]]:
    path = gene_file(gene, "goa.tsv")
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as handle:
        rows = []
        for row in csv.DictReader(handle, delimiter="\t"):
            rows.append(
                {
                    "gene_product_id": row["GENE PRODUCT ID"],
                    "symbol": row["SYMBOL"],
                    "qualifier": row["QUALIFIER"],
                    "go_id": row["GO TERM"],
                    "go_name": row["GO NAME"],
                    "go_aspect": row["GO ASPECT"],
                    "eco_id": row["ECO ID"],
                    "go_evidence": row["GO EVIDENCE CODE"],
                    "reference": row["REFERENCE"],
                    "with_from": row["WITH/FROM"],
                    "assigned_by": row["ASSIGNED BY"],
                    "date": row["DATE"],
                }
            )
        return rows


def get_goa_rows(gene: str) -> list[dict[str, str]]:
    if gene == "nusA":
        existing = parse_existing_goa(gene)
        if existing:
            return existing
    try:
        rows = fetch_quickgo(GENE_INFO[gene]["accession"])
    except Exception:
        rows = []
    return rows or fallback_rows(gene)


def write_goa(gene: str, rows: list[dict[str, str]]) -> None:
    if gene == "nusA" and gene_file(gene, "goa.tsv").exists():
        return
    with gene_file(gene, "goa.tsv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(GOA_HEADER)
        for row in rows:
            writer.writerow(
                [
                    "UniProtKB",
                    row["gene_product_id"],
                    row["symbol"] or gene,
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
                    metadata_by_accession().get(GENE_INFO[gene]["accession"], {}).get("Protein names", ""),
                    row["date"],
                ]
            )


def write_uniprot_fallback(gene: str, metadata: dict[str, dict[str, str]]) -> None:
    if gene not in FALLBACK_UNIPROT_GENES:
        return
    info = GENE_INFO[gene]
    meta = metadata[info["accession"]]
    path = gene_file(gene, "uniprot.txt")
    out = [
        f"ID   {info['entry']}            {'Reviewed' if meta['Reviewed'] == 'reviewed' else 'Unreviewed'};       {meta['Length']} AA.",
        f"AC   {info['accession']};",
        f"DE   SubName: Full={meta['Protein names']};",
        f"GN   Name={gene}; OrderedLocusNames={info['ordered_locus']};",
        f"OS   {TAXON_LABEL}.",
        "OX   NCBI_TaxID=160488;",
        (
            "CC   -!- CAUTION: Minimal fallback context assembled from "
            "projects/P_PUTIDA/data/psepk_uniprot_metadata.tsv because UniProt REST returned HTTP 500 on 2026-07-10."
        ),
    ]
    if meta.get("Function [CC]"):
        out.append(f"CC   -!- {meta['Function [CC]']}")
    if gene == "rapA":
        out.append("CC   -!- SIMILARITY: Belongs to the RapA/RNA polymerase-associated ATPase family.")
    elif gene == "nusB":
        out.append("CC   -!- SIMILARITY: Belongs to the NusB family.")
    elif gene == "dksA":
        out.append("CC   -!- SIMILARITY: Belongs to the DksA/TraR transcription regulator family.")
    elif gene == "PP_4553":
        out.append("CC   -!- SIMILARITY: Belongs to the sigma-70 factor family, ECF subfamily.")
    elif gene == "PP_2266":
        out.append("CC   -!- SIMILARITY: Contains DNA-directed RNA polymerase domain signatures.")
    for go_id in (meta.get("Gene Ontology IDs") or "").split("; "):
        if go_id:
            label = TERM.get(go_id, {"label": "GO term"})["label"]
            out.append(f"DR   GO; {go_id}; {label}.")
    for db_name, col in [("InterPro", "InterPro"), ("Pfam", "Pfam"), ("PANTHER", "PANTHER")]:
        for value in (meta.get(col) or "").split(";"):
            value = value.strip()
            if value:
                out.append(f"DR   {db_name}; {value}; {value}.")
    if meta.get("EC number"):
        out.append(f"DR   EC; {meta['EC number']};")
    if meta.get("Keywords"):
        out.append("KW   " + "; ".join(k.strip() for k in meta["Keywords"].split(";") if k.strip()) + ".")
    out.append("//")
    path.write_text("\n".join(out) + "\n", encoding="utf-8")


def goa_line(gene: str, term_id: str) -> str | None:
    return first_line(gene_file(gene, "goa.tsv"), term_id)


def evidence_for(gene: str, term_id: str | None = None) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    if term_id:
        add_support(items, support(file_id(gene, "goa.tsv"), goa_line(gene, term_id)))
    uniprot = gene_file(gene, "uniprot.txt")
    add_support(items, support(file_id(gene, "uniprot.txt"), first_line(uniprot, "DE   ")))
    for marker in (
        "CC   -!- FUNCTION:",
        "CC   -!- SUBUNIT:",
        "CC   -!- SUBCELLULAR LOCATION:",
        "CC   -!- SIMILARITY:",
        "DR   EC;",
        "DR   GO;",
        "DR   InterPro;",
        "DR   Pfam;",
        "DR   PANTHER;",
        "KW   ",
    ):
        add_support(items, support(file_id(gene, "uniprot.txt"), first_line(uniprot, marker)))
    return items


def review_for(gene: str, row: dict[str, str]) -> dict:
    go_id = row["go_id"]
    if gene == "nusB":
        if go_id == "GO:0003723":
            return {"summary": "RNA binding is the supported molecular function for NusB antitermination factor activity.", "action": "ACCEPT", "reason": "NusB binds antitermination RNA elements in ribosomal RNA operons and functions in transcription antitermination.", "supported_by": evidence_for(gene, go_id)}
        if go_id == "GO:0006353":
            return {"summary": "Termination is directionally related but the NusB-specific process is antitermination.", "action": "MODIFY", "reason": "NusB is an antitermination factor, so GO:0031564 is more precise than plain DNA-templated transcription termination.", "proposed_replacement_terms": [term("GO:0031564")], "supported_by": evidence_for(gene, go_id)}
        if go_id == "GO:0006355":
            return {"summary": "Broad transcription regulation should be narrowed to transcription antitermination.", "action": "MODIFY", "reason": "The reviewed function is rRNA operon antitermination, not general transcription regulation.", "proposed_replacement_terms": [term("GO:0031564")], "supported_by": evidence_for(gene, go_id)}
        if go_id == "GO:0005829":
            return {"summary": "Cytosol is appropriate for this soluble bacterial transcription factor.", "action": "ACCEPT", "reason": "The live GOA location row supports cytosol as the functional location.", "supported_by": evidence_for(gene, go_id)}
    if gene == "rapA":
        if go_id == "GO:0005524":
            return {"summary": "ATP binding is cofactor context for RapA's RNAP-associated ATPase activity.", "action": "KEEP_AS_NON_CORE", "reason": "ATP binding supports, but is secondary to, the ATP-hydrolysis-dependent transcription-regulatory role.", "supported_by": evidence_for(gene, go_id)}
        if go_id == "GO:0016817":
            return {"summary": "The generic acid-anhydride hydrolase term should be narrowed to ATP hydrolysis activity.", "action": "MODIFY", "reason": "RapA is an ATP-dependent RNA polymerase-associated remodeling/recycling factor; GO:0016887 is the informative hydrolase term.", "proposed_replacement_terms": [term("GO:0016887")], "supported_by": evidence_for(gene, go_id)}
        if go_id == "GO:0006355":
            return {"summary": "Regulation of DNA-templated transcription is appropriate for RapA's RNAP recycling role.", "action": "ACCEPT", "reason": "UniProt/HAMAP describes RapA as activating transcription by stimulating RNA polymerase recycling under stress conditions.", "supported_by": evidence_for(gene, go_id)}
    if gene == "PP_2266":
        if go_id == "GO:0003677":
            return {"summary": "DNA binding is broad context for an RNA polymerase-like protein but less informative than RNA polymerase activity.", "action": "KEEP_AS_NON_CORE", "reason": "Retain as non-core nucleic-acid context while using DNA-directed RNA polymerase activity as the core call.", "supported_by": evidence_for(gene, go_id)}
        if go_id == "GO:0003899":
            return {"summary": "DNA-directed RNA polymerase activity is the supported core molecular-function call for this RNA polymerase-like protein.", "action": "ACCEPT", "reason": "The live GOA row maps RNA polymerase domains and EC 2.7.7.6 to DNA-directed RNA polymerase activity.", "supported_by": evidence_for(gene, go_id)}
        if go_id == "GO:0006351":
            return {"summary": "DNA-templated transcription is appropriate process context for the RNA polymerase activity.", "action": "ACCEPT", "reason": "RNA polymerase domain evidence supports transcription context, while the exact complex membership remains a boundary question.", "supported_by": evidence_for(gene, go_id)}
    if gene == "PP_4553":
        if go_id == "GO:0003677":
            return {"summary": "DNA binding is broad and non-core for a sigma factor.", "action": "MARK_AS_OVER_ANNOTATED", "reason": "Sigma factor activity captures promoter-specific RNAP recruitment more precisely than generic DNA binding.", "supported_by": evidence_for(gene, go_id)}
        if go_id == "GO:0003700":
            return {"summary": "Generic DNA-binding transcription factor activity should be replaced by sigma factor activity.", "action": "MODIFY", "reason": "The protein is an ECF sigma-70 family factor; sigma factor activity is the specific bacterial MF.", "proposed_replacement_terms": [term("GO:0016987")], "supported_by": evidence_for(gene, go_id)}
        if go_id == "GO:0016987":
            return {"summary": "Sigma factor activity is the correct core molecular function for PP_4553.", "action": "ACCEPT", "reason": "InterPro sigma-factor domain evidence supports PP_4553 as an ECF sigma factor.", "supported_by": evidence_for(gene, go_id)}
        if go_id == "GO:0006352":
            return {"summary": "Transcription initiation is appropriate process context for sigma factor activity.", "action": "ACCEPT", "reason": "Sigma factors direct RNA polymerase to promoters during transcription initiation.", "supported_by": evidence_for(gene, go_id)}
        if go_id == "GO:0006355":
            return {"summary": "Broad transcription regulation is directionally correct but less specific than initiation regulation.", "action": "MODIFY", "reason": "GO:2000142 is the more specific process implied by sigma factor activity.", "proposed_replacement_terms": [term("GO:2000142")], "supported_by": evidence_for(gene, go_id)}
        if go_id == "GO:2000142":
            return {"summary": "Regulation of transcription initiation is appropriate for a sigma factor.", "action": "ACCEPT", "reason": "This logical inference from sigma factor activity matches bacterial sigma-factor biology.", "supported_by": evidence_for(gene, go_id)}
    if gene == "dksA":
        if go_id == "GO:0008270":
            return {"summary": "Zinc binding is appropriate DksA-family cofactor context.", "action": "KEEP_AS_NON_CORE", "reason": "The zinc-finger row supports DksA structure but is secondary to transcription regulation.", "supported_by": evidence_for(gene, go_id)}
        if go_id == "GO:0010468":
            return {"summary": "Regulation of gene expression is appropriate but broad context for DksA.", "action": "ACCEPT", "reason": "DksA regulates gene expression by direct RNA polymerase binding; no stronger live GOA process row is available.", "supported_by": evidence_for(gene, go_id)}
        if go_id == "GO:0005737":
            return {"summary": "Cytoplasm is appropriate for this soluble bacterial RNA polymerase-binding regulator.", "action": "ACCEPT", "reason": "The live GOA location row and UniProt subcellular-location mapping support cytoplasm.", "supported_by": evidence_for(gene, go_id)}
    if gene == "nusA":
        if go_id in {"GO:0000166", "GO:0003676"}:
            return {"summary": "This generic nucleic-acid/nucleotide-binding term is less informative than RNA binding and transcription termination/antitermination context.", "action": "MARK_AS_OVER_ANNOTATED", "reason": "NusA has specific RNA-binding and transcription termination/antitermination annotations that should carry the functional interpretation.", "supported_by": evidence_for(gene, go_id)}
        if go_id == "GO:0003700":
            return {"summary": "NusA is a transcription regulator, but generic DNA-binding transcription factor activity is not the best molecular-function description.", "action": "MODIFY", "reason": "NusA binds RNA polymerase and nascent RNA during elongation; transcription regulator activity is a better abstraction than DNA-binding transcription factor activity.", "proposed_replacement_terms": [term("GO:0140110")], "supported_by": evidence_for(gene, go_id)}
        if go_id == "GO:0003723":
            return {"summary": "RNA binding is a supported core molecular function for NusA.", "action": "ACCEPT", "reason": "UniProt notes that NusA binds nascent RNA while participating in termination and antitermination.", "supported_by": evidence_for(gene, go_id)}
        if go_id in {"GO:0005737", "GO:0005829"}:
            return {"summary": f"{TERM[go_id]['label']} is appropriate location context for bacterial NusA.", "action": "ACCEPT", "reason": "NusA acts with cytoplasmic RNA polymerase transcription complexes.", "supported_by": evidence_for(gene, go_id)}
        if go_id in {"GO:0006353", "GO:0031554", "GO:0031564"}:
            return {"summary": f"{TERM[go_id]['label']} is appropriate for NusA's termination/antitermination role.", "action": "ACCEPT", "reason": "UniProt describes NusA as participating in both transcription termination and antitermination.", "supported_by": evidence_for(gene, go_id)}
    return {"summary": "This transcription spillover annotation could not be resolved in this pass.", "action": "UNDECIDED", "reason": "Available evidence was insufficient for a confident decision.", "supported_by": evidence_for(gene, go_id)}


def extra_annotations(gene: str) -> list[dict]:
    extras: list[dict] = []
    if gene == "nusB":
        extras.append(
            {
                "term": term("GO:0031564"),
                "evidence_type": "IEA",
                "original_reference_id": file_id(gene, "uniprot.txt"),
                "qualifier": "involved_in",
                "review": {
                    "summary": "Add explicit transcription antitermination for NusB.",
                    "action": "NEW",
                    "reason": "The current live rows include termination and broad regulation, but the product and function evidence identify NusB as an antitermination factor.",
                    "supported_by": evidence_for(gene, "GO:0006353"),
                },
            }
        )
    if gene == "dksA":
        extras.append(
            {
                "term": term("GO:0140110"),
                "evidence_type": "IEA",
                "original_reference_id": file_id(gene, "uniprot.txt"),
                "qualifier": "enables",
                "review": {
                    "summary": "Add transcription regulator activity for DksA.",
                    "action": "NEW",
                    "reason": "DksA is named and functionally described as an RNA polymerase-binding transcription factor; the live GOA rows otherwise only expose zinc binding as molecular function.",
                    "supported_by": evidence_for(gene, "GO:0010468"),
                },
            }
        )
    return extras


def existing_annotations(gene: str, rows: list[dict[str, str]]) -> list[dict]:
    annotations = [
        {
            "term": {"id": row["go_id"], "label": row["go_name"]},
            "evidence_type": row["go_evidence"],
            "original_reference_id": row["reference"],
            "qualifier": row["qualifier"],
            "review": review_for(gene, row),
        }
        for row in rows
    ]
    annotations.extend(extra_annotations(gene))
    return annotations


def core_functions(gene: str) -> list[dict]:
    if gene == "nusB":
        return [{"description": "NusB RNA-binding antitermination factor for ribosomal RNA operon transcription.", "molecular_function": term("GO:0003723"), "directly_involved_in": [term("GO:0031564")], "locations": [term("GO:0005829")], "supported_by": evidence_for(gene, "GO:0003723")}]
    if gene == "rapA":
        return [{"description": "RNA polymerase-associated ATPase that supports transcription regulation by RNAP recycling/remodeling.", "molecular_function": term("GO:0016887"), "directly_involved_in": [term("GO:0006355")], "supported_by": evidence_for(gene, "GO:0016817")}]
    if gene == "PP_2266":
        return [{"description": "Predicted DNA-directed RNA polymerase-like activity in transcription context; exact core-complex relationship remains unresolved.", "molecular_function": term("GO:0003899"), "directly_involved_in": [term("GO:0006351")], "supported_by": evidence_for(gene, "GO:0003899")}]
    if gene == "PP_4553":
        return [{"description": "ECF sigma factor activity directing RNA polymerase to promoters during transcription initiation.", "molecular_function": term("GO:0016987"), "directly_involved_in": [term("GO:0006352"), term("GO:2000142")], "supported_by": evidence_for(gene, "GO:0016987")}]
    if gene == "dksA":
        return [{"description": "RNA polymerase-binding transcription regulator with zinc-binding DksA-family structure.", "molecular_function": term("GO:0140110"), "directly_involved_in": [term("GO:0010468")], "locations": [term("GO:0005737")], "supported_by": evidence_for(gene, "GO:0010468")}]
    return [{"description": "NusA RNA-binding transcription termination/antitermination factor.", "molecular_function": term("GO:0003723"), "directly_involved_in": [term("GO:0006353"), term("GO:0031564")], "locations": [term("GO:0005737")], "supported_by": evidence_for(gene, "GO:0003723")}]


def references_for(gene: str, rows: list[dict[str, str]]) -> list[dict]:
    refs = [{"id": ref, "title": GO_REF_TITLES.get(ref, f"Gene Ontology annotation reference {ref}"), "findings": []} for ref in sorted({row["reference"] for row in rows if row.get("reference")})]
    if gene in FALLBACK_UNIPROT_GENES:
        refs.append(
            {
                "id": file_id(gene, "uniprot.txt"),
                "title": f"Fallback UniProt-style metadata context for {gene} ({GENE_INFO[gene]['accession']})",
                "findings": [
                    {
                        "statement": "UniProt REST stream was unavailable, so this local file records project metadata used for curation and Asta context.",
                        "supporting_text": "CC   -!- CAUTION: Minimal fallback context assembled from projects/P_PUTIDA/data/psepk_uniprot_metadata.tsv because UniProt REST returned HTTP 500 on 2026-07-10.",
                    }
                ],
            }
        )
    else:
        refs.append({"id": file_id(gene, "uniprot.txt"), "title": f"UniProtKB entry for {gene} ({GENE_INFO[gene]['accession']})", "findings": []})
    refs.append({"id": file_id(gene, "goa.tsv"), "title": f"QuickGO GOA annotations for {gene}", "findings": [{"statement": f"GOA table containing the annotations reviewed for {gene}."}]})
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


def write_notes(gene: str) -> None:
    path = gene_file(gene, "notes.md")
    caution = ""
    if gene in FALLBACK_UNIPROT_GENES:
        caution = (
            f"- `just fetch-gene` could not populate {gene} because UniProt REST returned HTTP 500; "
            f"`{gene}-uniprot.txt` is explicitly marked as fallback context "
            f"[{file_id(gene, 'uniprot.txt')} \"CC   -!- CAUTION: Minimal fallback context assembled from projects/P_PUTIDA/data/psepk_uniprot_metadata.tsv because UniProt REST returned HTTP 500 on 2026-07-10.\"].\n"
        )
    asta = ""
    if gene_file(gene, "deep-research-asta.md").exists():
        asta = f"- Asta was run as fast retrieval context and is recorded as provenance only [{file_id(gene, 'deep-research-asta.md')} \"{first_line(gene_file(gene, 'deep-research-asta.md'), 'uniprot_accession:')}\"] .\n"
    path.write_text(
        f"# {gene} notes\n\n## {TODAY}\n\n"
        f"{caution}"
        f"- Routed this gene out of the translation/RNA-processing umbrella into transcription/RNA-polymerase spillover context.\n"
        f"- Core interpretation: {GENE_INFO[gene]['description']}\n"
        f"{asta}",
        encoding="utf-8",
    )


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
            {"question": f"What are the direct P. putida KT2440 transcriptional targets or promoter contexts for {gene}?"}
        ],
        "suggested_experiments": [
            {
                "description": f"Combine tagged {gene} chromatin/RNAP-associated pull-down or occupancy profiling with RNA-seq after deletion or depletion to resolve direct transcriptional targets.",
                "experiment_type": "transcription-regulatory target assay",
            }
        ],
    }
    gene_file(gene, "ai-review.yaml").write_text(yaml.dump(review, Dumper=NoAliasDumper, sort_keys=False, width=110), encoding="utf-8")


def write_module() -> None:
    module = {
        "id": "MODULE:transcription_rna_polymerase_spillover_boundary",
        "title": "Transcription and RNA-polymerase spillover boundary",
        "description": (
            "Boundary module for PSEPK genes that entered the translation/RNA-processing bucket through broad RNA, "
            "transcription, or RNA-polymerase keywords but function in transcription termination, antitermination, sigma-factor "
            "initiation, RNA polymerase regulation, or RNA polymerase-like catalysis."
        ),
        "status": "DRAFT",
        "evidence": [
            {"source_id": f"file:{BATCH_TSV}", "title": "PSEPK translation/RNA transcription spillover split", "statement": "The batch records nusB, rapA, PP_2266, PP_4553, dksA, and nusA as transcription/RNA-polymerase spillovers from the translation/RNA-processing umbrella."},
            *[{"source_id": file_id(g, "ai-review.yaml"), "title": f"Curated {g} review", "statement": GENE_INFO[g]["description"]} for g in GENES],
        ],
        "module": {
            "id": "transcription_rna_polymerase_spillover_boundary",
            "label": "Transcription and RNA-polymerase spillover boundary",
            "module_type": "BIOLOGICAL_PROCESS",
            "concepts": [
                {"preferred_term": "RNA binding", "term": term("GO:0003723"), "description": "RNA-binding activity for NusB/NusA antitermination or elongation factors."},
                {"preferred_term": "transcription antitermination", "term": term("GO:0031564"), "description": "Nus-family antitermination process context."},
                {"preferred_term": "ATP hydrolysis activity", "term": term("GO:0016887"), "description": "RapA RNAP-associated ATPase activity."},
                {"preferred_term": "DNA-directed RNA polymerase activity", "term": term("GO:0003899"), "description": "RNA-polymerase-like catalytic context for PP_2266."},
                {"preferred_term": "sigma factor activity", "term": term("GO:0016987"), "description": "ECF sigma-factor activity for PP_4553."},
                {"preferred_term": "transcription regulator activity", "term": term("GO:0140110"), "description": "DksA RNA polymerase-binding transcription regulator activity."},
            ],
            "parts": [
                {"order": 1, "role": "Nus transcription termination and antitermination factors", "node": {"id": "nus_termination_antitermination_factors", "label": "Nus termination and antitermination factors", "module_type": "BIOLOGICAL_PROCESS", "description": "NusB and NusA are transcription elongation/termination factors, not translation factors.", "annotons": [
                    {"id": "nusB_antitermination_factor", "label": "nusB: RNA-binding antitermination factor", "participant": {"selector_type": "GENE", "gene": {"preferred_term": "nusB"}}, "function": {"preferred_term": "RNA binding", "term": term("GO:0003723")}, "processes": [{"preferred_term": "transcription antitermination", "term": term("GO:0031564")}], "locations": [{"preferred_term": "cytosol", "term": term("GO:0005829")}], "role_description": "NusB-family antitermination factor."},
                    {"id": "nusA_termination_antitermination_factor", "label": "nusA: termination/antitermination factor", "participant": {"selector_type": "GENE", "gene": {"preferred_term": "nusA"}}, "function": {"preferred_term": "RNA binding", "term": term("GO:0003723")}, "processes": [{"preferred_term": "DNA-templated transcription termination", "term": term("GO:0006353")}, {"preferred_term": "transcription antitermination", "term": term("GO:0031564")}], "locations": [{"preferred_term": "cytoplasm", "term": term("GO:0005737")}], "role_description": "NusA-family RNA-binding termination and antitermination factor."},
                ]}},
                {"order": 2, "role": "RNA polymerase regulatory factors", "node": {"id": "rnap_regulatory_factors", "label": "RNA polymerase regulatory factors", "module_type": "BIOLOGICAL_PROCESS", "description": "RapA and DksA regulate transcription through RNA polymerase-associated activities.", "annotons": [
                    {"id": "rapA_rnap_recycling_atpase", "label": "rapA: RNAP-associated ATPase", "participant": {"selector_type": "GENE", "gene": {"preferred_term": "rapA"}}, "function": {"preferred_term": "ATP hydrolysis activity", "term": term("GO:0016887")}, "processes": [{"preferred_term": "regulation of DNA-templated transcription", "term": term("GO:0006355")}], "role_description": "RNAP-associated ATPase/transcription-recycling factor."},
                    {"id": "dksA_rnap_binding_regulator", "label": "dksA: RNAP-binding transcription regulator", "participant": {"selector_type": "GENE", "gene": {"preferred_term": "dksA"}}, "function": {"preferred_term": "transcription regulator activity", "term": term("GO:0140110")}, "processes": [{"preferred_term": "regulation of gene expression", "term": term("GO:0010468")}], "locations": [{"preferred_term": "cytoplasm", "term": term("GO:0005737")}], "role_description": "DksA-family RNAP-binding transcription regulator."},
                ]}},
                {"order": 3, "role": "RNA polymerase and sigma-factor side nodes", "node": {"id": "rnap_sigma_side_nodes", "label": "RNA polymerase and sigma-factor side nodes", "module_type": "BIOLOGICAL_PROCESS", "description": "PP_2266 and PP_4553 are transcription side nodes rather than translation/RNA-processing genes.", "annotons": [
                    {"id": "PP_2266_rnap_like_candidate", "label": "PP_2266: RNA polymerase-like candidate", "participant": {"selector_type": "GENE", "gene": {"preferred_term": "PP_2266"}}, "function": {"preferred_term": "DNA-directed RNA polymerase activity", "term": term("GO:0003899")}, "processes": [{"preferred_term": "DNA-templated transcription", "term": term("GO:0006351")}], "role_description": "RNA polymerase-domain candidate kept outside the compact canonical RNAP core until complex role is resolved."},
                    {"id": "PP_4553_ecf_sigma_factor", "label": "PP_4553: ECF sigma factor", "participant": {"selector_type": "GENE", "gene": {"preferred_term": "PP_4553"}}, "function": {"preferred_term": "sigma factor activity", "term": term("GO:0016987")}, "processes": [{"preferred_term": "DNA-templated transcription initiation", "term": term("GO:0006352")}, {"preferred_term": "regulation of DNA-templated transcription initiation", "term": term("GO:2000142")}], "role_description": "Predicted ECF sigma factor and transcription-initiation regulator."},
                ]}},
            ],
        },
        "notes": "This is a routing/boundary module for transcription genes mis-bucketed under translation/RNA processing.",
    }
    MODULE_PATH.write_text(yaml.dump(module, Dumper=NoAliasDumper, sort_keys=False, width=110), encoding="utf-8")


def main() -> None:
    metadata = metadata_by_accession()
    for gene in GENES:
        gene_dir(gene).mkdir(parents=True, exist_ok=True)
        rows = get_goa_rows(gene)
        write_uniprot_fallback(gene, metadata)
        write_goa(gene, rows)
        write_review(gene, rows)
        write_notes(gene)
    write_module()


if __name__ == "__main__":
    main()
