#!/usr/bin/env python3
"""First-pass curation for PSEPK DNA-bucket mobile-element recombination genes."""

from __future__ import annotations

import csv
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes" / "PSEPK"
MODULE_PATH = ROOT / "modules" / "mobile_genetic_elements_boundary.yaml"
MOBILE_TSV = ROOT / "projects/P_PUTIDA/batches/module_dna_replication_repair_recombination_mobile_integrase_recombinase_transposase.tsv"
RT_TSV = ROOT / "projects/P_PUTIDA/batches/module_dna_replication_repair_recombination_retroelement_reverse_transcriptase.tsv"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


TERM = {
    "GO:0000150": {"id": "GO:0000150", "label": "DNA strand exchange activity"},
    "GO:0003677": {"id": "GO:0003677", "label": "DNA binding"},
    "GO:0003723": {"id": "GO:0003723", "label": "RNA binding"},
    "GO:0003887": {"id": "GO:0003887", "label": "DNA-directed DNA polymerase activity"},
    "GO:0003964": {"id": "GO:0003964", "label": "RNA-directed DNA polymerase activity"},
    "GO:0004803": {"id": "GO:0004803", "label": "transposase activity"},
    "GO:0006278": {"id": "GO:0006278", "label": "RNA-templated DNA biosynthetic process"},
    "GO:0006310": {"id": "GO:0006310", "label": "DNA recombination"},
    "GO:0006313": {"id": "GO:0006313", "label": "DNA transposition"},
    "GO:0008907": {"id": "GO:0008907", "label": "integrase activity"},
    "GO:0009037": {"id": "GO:0009037", "label": "tyrosine-based site-specific recombinase activity"},
    "GO:0015074": {"id": "GO:0015074", "label": "DNA integration"},
    "GO:0016740": {"id": "GO:0016740", "label": "transferase activity"},
    "GO:0016779": {"id": "GO:0016779", "label": "nucleotidyltransferase activity"},
}


MOBILE_GENES = [
    "PP_1116",
    "PP_1118",
    "PP_1532",
    "PP_1533",
    "PP_1555",
    "PP_1865",
    "PP_1960",
    "PP_1962",
    "PP_2297",
    "PP_2495",
    "PP_2501",
    "PP_2937",
    "PP_2964",
    "PP_2971",
    "tnpS",
    "PP_3026",
    "PP_3181",
    "PP_3678",
    "PP_3791",
    "PP_3889",
    "PP_3920",
    "PP_3987",
    "PP_4409",
    "PP_4415",
    "PP_5490",
]

RT_GENES = ["PP_1250", "PP_1846"]
CONTEXT_ONLY_GENES = {"PP_2495"}


def read_tsv(path: Path) -> dict[str, dict[str, str]]:
    with path.open() as stream:
        return {row["gene"]: row for row in csv.DictReader(stream, delimiter="\t")}


BATCH_INFO = read_tsv(MOBILE_TSV) | read_tsv(RT_TSV)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def optional_first_line(path: Path, *needles: str) -> str | None:
    if not path.exists():
        return None
    for line in read_text(path).splitlines():
        if all(needle in line for needle in needles):
            return line
    return None


def prefixed_lines(path: Path, prefix: str, limit: int = 5) -> list[str]:
    if not path.exists():
        return []
    return [line for line in read_text(path).splitlines() if line.startswith(prefix)][:limit]


def support(reference_id: str, text: str | None) -> dict[str, str] | None:
    if not text:
        return None
    return {"reference_id": reference_id, "supporting_text": text}


def add_unique(items: list[dict[str, str]], item: dict[str, str] | None) -> None:
    if item and item not in items:
        items.append(item)


def file_id(gene: str, suffix: str) -> str:
    return f"file:PSEPK/{gene}/{gene}-{suffix}"


def product_line(gene: str) -> str | None:
    path = GENE_ROOT / gene / f"{gene}-uniprot.txt"
    return optional_first_line(path, "DE   RecName") or optional_first_line(path, "DE   SubName")


def goa_line(gene: str, term_id: str) -> str | None:
    return optional_first_line(GENE_ROOT / gene / f"{gene}-goa.tsv", term_id)


def uniprot_evidence(gene: str, term_id: str | None = None, domain_needles: tuple[str, ...] = ()) -> list[dict[str, str]]:
    path = GENE_ROOT / gene / f"{gene}-uniprot.txt"
    items: list[dict[str, str]] = []
    add_unique(items, support(file_id(gene, "uniprot.txt"), product_line(gene)))
    if term_id:
        add_unique(items, support(file_id(gene, "uniprot.txt"), optional_first_line(path, f"DR   GO; {term_id};")))
    for needle in domain_needles:
        add_unique(items, support(file_id(gene, "uniprot.txt"), optional_first_line(path, needle)))
    for marker in ("CC   -!- FUNCTION:", "Belongs to", "DR   PANTHER;", "KW   DNA", "KW   Transposition"):
        add_unique(items, support(file_id(gene, "uniprot.txt"), optional_first_line(path, marker)))
    return items


def asta_evidence(gene: str) -> list[dict[str, str]]:
    path = GENE_ROOT / gene / f"{gene}-deep-research-asta.md"
    items: list[dict[str, str]] = []
    add_unique(items, support(file_id(gene, "deep-research-asta.md"), optional_first_line(path, "uniprot_accession:")))
    add_unique(items, support(file_id(gene, "deep-research-asta.md"), optional_first_line(path, "protein_description:")))
    add_unique(items, support(file_id(gene, "deep-research-asta.md"), optional_first_line(path, "protein_family:")))
    add_unique(items, support(file_id(gene, "deep-research-asta.md"), optional_first_line(path, "protein_domains:")))
    return items


def evidence_for(gene: str, term_id: str | None = None, domain_needles: tuple[str, ...] = ()) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    if term_id:
        add_unique(items, support(file_id(gene, "goa.tsv"), goa_line(gene, term_id)))
    for item in uniprot_evidence(gene, term_id, domain_needles):
        add_unique(items, item)
    for item in asta_evidence(gene):
        add_unique(items, item)
    return items


def term_ids(data: dict) -> set[str]:
    return {ann.get("term", {}).get("id") for ann in data.get("existing_annotations") or []}


def has_term(data: dict, term_id: str) -> bool:
    return term_id in term_ids(data)


def gene_class(gene: str, data: dict) -> str:
    ids = term_ids(data)
    product = product_line(gene) or ""
    if gene in RT_GENES:
        return "reverse_transcriptase"
    if "GO:0004803" in ids or "Transposase" in product:
        return "transposase"
    if gene == "PP_1533":
        return "excisionase"
    if gene in CONTEXT_ONLY_GENES:
        return "context_only"
    if "GO:0000150" in ids:
        return "resolvase"
    return "integrase"


def description_for(gene: str, data: dict) -> str:
    info = BATCH_INFO[gene]
    product = info["protein_name"]
    cls = gene_class(gene, data)
    if cls == "reverse_transcriptase":
        return (
            f"{gene} encodes a bacterial reverse transcriptase-family RNA-directed DNA polymerase with group II "
            "intron/maturase-family domain support. Its supported first-pass role is RNA-templated DNA synthesis in "
            "retroelement or group-II-intron mobile-element biology, not chromosomal DNA replication or a resolved "
            "antiviral-defense module."
        )
    if cls == "transposase":
        return (
            f"{gene} encodes a mobile-element transposase ({product}). UniProt, GOA, and domain evidence support "
            "transposase activity in DNA transposition, so it is routed to the mobile genetic element boundary rather "
            "than to chromosomal DNA repair."
        )
    if cls == "resolvase":
        return (
            f"{gene} encodes a site-specific recombinase/resolvase-family mobile-element protein ({product}). "
            "The supported role is DNA strand exchange in recombination and, where annotated, mobile-element DNA "
            "integration."
        )
    if cls == "excisionase":
        return (
            f"{gene} encodes an excisionase-like DNA-binding protein in a mobile-element recombination context. "
            "Current first-pass evidence supports DNA-binding/recombination context, but not an independent "
            "chromosomal DNA-repair role."
        )
    if cls == "context_only":
        return (
            f"{gene} encodes a YqaJ viral recombinase domain-containing protein. The local record has no GOA rows, "
            "so it is retained as an unresolved mobile-element recombinase-like boundary member without a synthetic "
            "core GO function call."
        )
    return (
        f"{gene} encodes a phage/integrative-element integrase or tyrosine recombinase-family protein ({product}). "
        "The supported role is site-specific recombination/integration in mobile-element biology rather than "
        "chromosomal DNA repair."
    )


def review_for(gene: str, data: dict, term_id: str) -> dict:
    cls = gene_class(gene, data)
    if term_id == "GO:0003677":
        dna_binding_is_core = cls == "excisionase" or (cls == "integrase" and not has_term(data, "GO:0009037"))
        action = "ACCEPT" if dna_binding_is_core else "KEEP_AS_NON_CORE"
        summary = "DNA binding is compatible with the mobile-element recombinase/transposase context."
        reason = (
            "The local UniProt and GOA records support DNA-binding domains or DNA-binding keyword propagation. For "
            "catalytic recombinases and transposases, the catalytic activity and mobile-element process terms are more "
            "informative, so DNA binding is retained as substrate/context rather than the main routing decision."
        )
        if dna_binding_is_core:
            reason = (
                "The fetched record supports a mobile-element recombinase/excisionase-family role but lacks a more "
                "specific catalytic GOA row. DNA binding is accepted as the current molecular-function evidence while "
                "the exact mobile-element partner, target site, and catalytic specificity remain unresolved."
            )
        supported = evidence_for(gene, term_id, ("DNA-bd", "DNA_bind", "Resolvase_HTH", "Excisionase"))
        return {"summary": summary, "action": action, "reason": reason, "supported_by": supported}

    if term_id == "GO:0000150":
        return {
            "summary": "DNA strand exchange activity is the supported catalytic role for this resolvase-family protein.",
            "action": "ACCEPT",
            "reason": "Resolvase/recombinase domains and InterPro-derived GOA support DNA strand exchange as the core mobile-element recombination activity.",
            "supported_by": evidence_for(gene, term_id, ("Resolv_N", "SSR_resolvase", "Recombinase_CS", "Resolvase")),
        }

    if term_id == "GO:0009037":
        return {
            "summary": "Tyrosine-based site-specific recombinase activity is supported for this integrase-family protein.",
            "action": "ACCEPT",
            "reason": "The UniProt product, phage/integrase-family domains, and GOA rows support a tyrosine recombinase/integrase role in mobile-element recombination.",
            "supported_by": evidence_for(gene, term_id, ("Integrase_catalytic", "Phage_integrase", "Tyrosine_recombinase", "Integrase_recombinase_N")),
        }

    if term_id == "GO:0008907":
        return {
            "summary": "Integrase activity is supported but is less specific than the tyrosine recombinase row present on this record.",
            "action": "KEEP_AS_NON_CORE",
            "reason": "The integrase-family assignment is correct, but the more specific tyrosine-based site-specific recombinase activity captures the core catalytic call where both terms are present.",
            "supported_by": evidence_for(gene, term_id, ("Integrase_catalytic", "Phage_integrase", "Integrase_recombinase_N")),
        }

    if term_id == "GO:0004803":
        return {
            "summary": "Transposase activity is supported by the product name and transposase-family domain evidence.",
            "action": "ACCEPT",
            "reason": "The fetched UniProt/GOA records identify a DDE/RNaseH-like transposase-family protein, making transposase activity the core molecular function.",
            "supported_by": evidence_for(gene, term_id, ("Transpos", "DDE_Tnp", "RNaseH-like")),
        }

    if term_id == "GO:0006313":
        return {
            "summary": "DNA transposition is the supported biological process for this transposase.",
            "action": "ACCEPT",
            "reason": "The transposase activity row and transposase-family domains support mobile-element DNA transposition.",
            "supported_by": evidence_for(gene, term_id, ("Transpos", "DDE_Tnp", "RNaseH-like")),
        }

    if term_id == "GO:0006310":
        return {
            "summary": "DNA recombination is retained as the broad mobile-element recombination process.",
            "action": "ACCEPT",
            "reason": "The product/domain evidence supports recombinase, integrase, or excisionase-family mobile-element recombination context. This does not imply chromosomal homologous recombination or DNA repair.",
            "supported_by": evidence_for(gene, term_id, ("Integrase", "Resolv", "Recombinase", "Excisionase")),
        }

    if term_id == "GO:0015074":
        return {
            "summary": "DNA integration is compatible with the integrase/resolvase-family mobile-element context.",
            "action": "ACCEPT",
            "reason": "The local GOA and UniProt records route this gene to mobile-element DNA integration. The term is retained as mobile genetic element biology rather than general genome-maintenance DNA repair.",
            "supported_by": evidence_for(gene, term_id, ("Integrase", "Resolv", "Recombinase", "Phage_integrase")),
        }

    if term_id == "GO:0003723":
        return {
            "summary": "RNA binding is retained as compatible group-II-intron/reverse-transcriptase context.",
            "action": "ACCEPT",
            "reason": "Group-II-intron/maturase-family reverse transcriptases are RNA-associated enzymes, and the InterPro-derived RNA-binding row is compatible with the RNA-directed DNA polymerase role.",
            "supported_by": evidence_for(gene, term_id, ("Group_II_RT_mat", "Mat_intron_G2", "RT_dom")),
        }

    if term_id == "GO:0003964":
        return {
            "summary": "RNA-directed DNA polymerase activity is the core reverse-transcriptase activity.",
            "action": "ACCEPT",
            "reason": "The UniProt record names RNA-directed DNA polymerase activity with EC 2.7.7.49 and reverse-transcriptase/group-II-intron domain support.",
            "supported_by": evidence_for(gene, term_id, ("Group_II_RT_mat", "RT_dom", "Reverse_transcriptase")),
        }

    if term_id == "GO:0003887":
        return {
            "summary": "DNA-directed DNA polymerase activity is not the right specific call for this reverse-transcriptase-family record.",
            "action": "MODIFY",
            "reason": "The product and UniProt GO cross-reference support RNA-directed DNA polymerase activity. The DNA-directed polymerase row is an automated over-propagation and should be replaced by the RT activity already present on the record.",
            "proposed_replacement_terms": [TERM["GO:0003964"]],
            "supported_by": evidence_for(gene, "GO:0003964", ("Group_II_RT_mat", "RT_dom", "Reverse_transcriptase")),
        }

    if term_id == "GO:0006278":
        return {
            "summary": "RNA-templated DNA biosynthetic process is compatible with the reverse-transcriptase activity.",
            "action": "ACCEPT",
            "reason": "The record supports RNA-directed DNA polymerase activity in a mobile/retroelement context. The broader process term is retained without asserting a resolved cognate intron, retron, or defense pathway.",
            "supported_by": evidence_for(gene, term_id, ("Group_II_RT_mat", "RT_dom", "Reverse_transcriptase")),
        }

    if term_id in {"GO:0016740", "GO:0016779"}:
        return {
            "summary": "This parent transferase/nucleotidyltransferase term is redundant with the specific reverse-transcriptase activity.",
            "action": "MARK_AS_OVER_ANNOTATED",
            "reason": "The more specific RNA-directed DNA polymerase activity captures the actual catalytic role. The parent term is technically related but adds little functional value for this review.",
            "supported_by": evidence_for(gene, term_id, ("RT_dom", "Reverse_transcriptase")),
        }

    raise ValueError(f"No review rule for {gene} {term_id}")


def core_function_for(gene: str, data: dict) -> list[dict]:
    cls = gene_class(gene, data)
    if cls == "context_only":
        return []
    if cls == "reverse_transcriptase":
        return [
            {
                "description": "Bacterial reverse-transcriptase-family RNA-directed DNA polymerase activity in RNA-templated DNA biosynthesis.",
                "supported_by": evidence_for(gene, "GO:0003964", ("Group_II_RT_mat", "RT_dom", "Reverse_transcriptase")),
                "molecular_function": TERM["GO:0003964"],
                "directly_involved_in": [TERM["GO:0006278"]],
            }
        ]
    if cls == "transposase":
        return [
            {
                "description": "Mobile-element transposase activity driving DNA transposition.",
                "supported_by": evidence_for(gene, "GO:0004803", ("Transpos", "DDE_Tnp", "RNaseH-like")),
                "molecular_function": TERM["GO:0004803"],
                "directly_involved_in": [TERM["GO:0006313"]],
            }
        ]
    if cls == "resolvase":
        processes = [TERM["GO:0006310"]]
        if has_term(data, "GO:0015074"):
            processes.append(TERM["GO:0015074"])
        return [
            {
                "description": "Resolvase/site-specific recombinase-family DNA strand exchange in mobile-element recombination.",
                "supported_by": evidence_for(gene, "GO:0000150", ("Resolv_N", "SSR_resolvase", "Recombinase_CS", "Resolvase")),
                "molecular_function": TERM["GO:0000150"],
                "directly_involved_in": processes,
            }
        ]
    if cls == "excisionase":
        return [
            {
                "description": "Excisionase-like DNA-binding role in mobile-element recombination context.",
                "supported_by": evidence_for(gene, "GO:0003677", ("Excisionase", "DNA-bd_dom")),
                "molecular_function": TERM["GO:0003677"],
                "directly_involved_in": [TERM["GO:0006310"]],
            }
        ]
    if has_term(data, "GO:0009037"):
        return [
            {
                "description": "Phage/integrative-element tyrosine recombinase activity in mobile-element DNA recombination and integration.",
                "supported_by": evidence_for(gene, "GO:0009037", ("Integrase_catalytic", "Phage_integrase", "Tyrosine_recombinase", "Integrase_recombinase_N")),
                "molecular_function": TERM["GO:0009037"],
                "directly_involved_in": [TERM["GO:0006310"], TERM["GO:0015074"]],
            }
        ]
    return [
        {
            "description": "Integrase-family DNA-binding/recombination candidate in mobile-element DNA integration context.",
            "supported_by": evidence_for(gene, "GO:0003677", ("Integrase", "Phage_integrase", "DNA_brk_join_enz")),
            "molecular_function": TERM["GO:0003677"],
            "directly_involved_in": [TERM["GO:0006310"], TERM["GO:0015074"]],
        }
    ]


def ensure_references(data: dict, gene: str) -> None:
    refs = data.setdefault("references", [])
    by_id = {ref.get("id"): ref for ref in refs}
    local_refs = [
        (
            file_id(gene, "uniprot.txt"),
            f"UniProtKB entry for {gene}",
            product_line(gene),
            "UniProt provides product, GO cross-reference, family, and domain context used in this first-pass review.",
        ),
        (
            file_id(gene, "goa.tsv"),
            f"QuickGO GOA annotations for {gene}",
            None,
            "The fetched GOA table contains the machine-sourced annotations reviewed for this gene.",
        ),
        (
            file_id(gene, "deep-research-asta.md"),
            f"Asta retrieval report for {gene}",
            optional_first_line(GENE_ROOT / gene / f"{gene}-deep-research-asta.md", "uniprot_accession:"),
            "Asta retrieval was generated for this first-pass review and used as lightweight identity/retrieval context.",
        ),
    ]
    for ref_id, title, quote, statement in local_refs:
        if ref_id in by_id:
            continue
        finding = {"statement": statement}
        if quote:
            finding["supporting_text"] = quote
        refs.append({"id": ref_id, "title": title, "findings": [finding]})


def suggested_questions_for(gene: str, data: dict) -> list[dict[str, str]]:
    cls = gene_class(gene, data)
    if cls == "reverse_transcriptase":
        question = f"What cognate RNA element and genomic target, if any, define the mobile-element role of {gene}?"
    elif cls == "context_only":
        question = f"Does {gene} have measurable YqaJ-like recombinase or nuclease activity, and what mobile element encodes it?"
    else:
        question = f"What mobile element and target-site context define the recombination or transposition activity of {gene}?"
    return [{"question": question}]


def suggested_experiments_for(gene: str, data: dict) -> list[dict[str, str]]:
    cls = gene_class(gene, data)
    if cls == "reverse_transcriptase":
        return [
            {
                "experiment_type": "RNA association and polymerase assay",
                "description": f"Identify RNAs associated with {gene} and test purified protein for RNA-directed DNA polymerase activity.",
                "hypothesis": f"{gene} functions as a mobile-element reverse transcriptase with a specific cognate RNA.",
            }
        ]
    if cls == "transposase":
        return [
            {
                "experiment_type": "transposition reporter assay",
                "description": f"Use a marked insertion-sequence or transposon reporter to test whether {gene} catalyzes DNA transposition.",
                "hypothesis": f"{gene} is an active mobile-element transposase.",
            }
        ]
    return [
        {
            "experiment_type": "site-specific recombination assay",
            "description": f"Test {gene} with candidate attachment or recombination-site substrates from its genomic neighborhood.",
            "hypothesis": f"{gene} catalyzes mobile-element site-specific recombination or integration at defined DNA sites.",
        }
    ]


def curate_gene(gene: str) -> None:
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(path.read_text())
    data["status"] = "DRAFT"
    data["description"] = description_for(gene, data)
    ensure_references(data, gene)
    for ann in data.get("existing_annotations") or []:
        ann["review"] = review_for(gene, data, ann["term"]["id"])
    data["core_functions"] = core_function_for(gene, data)
    data["proposed_new_terms"] = []
    data["suggested_questions"] = suggested_questions_for(gene, data)
    data["suggested_experiments"] = suggested_experiments_for(gene, data)
    path.write_text(yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=False, width=120), encoding="utf-8")


def descriptor(term_id: str, description: str | None = None) -> dict:
    item = {"preferred_term": TERM[term_id]["label"], "term": TERM[term_id]}
    if description:
        item["description"] = description
    return item


def participant(gene: str) -> dict:
    return {"selector_type": "GENE", "gene": {"preferred_term": gene}}


def annoton(gene: str, term_id: str | None, processes: list[str], label: str, role: str, notes: str | None = None) -> dict:
    item = {"id": f"{gene.lower().replace('-', '_')}_{label}", "label": f"{gene}: {role}", "participant": participant(gene), "role_description": role}
    if term_id:
        item["function"] = descriptor(term_id)
    if processes:
        item["processes"] = [descriptor(process_id) for process_id in processes]
    if notes:
        item["notes"] = notes
    return item


def module_yaml() -> dict:
    resolvases = ["PP_1116", "PP_1118", "PP_3026", "PP_5490"]
    integrases = [
        "PP_1532",
        "PP_1555",
        "PP_1960",
        "PP_1962",
        "PP_2297",
        "PP_2501",
        "PP_2937",
        "tnpS",
        "PP_3181",
        "PP_3678",
        "PP_3791",
        "PP_3889",
        "PP_3920",
        "PP_3987",
        "PP_4409",
        "PP_4415",
    ]
    transposases = ["PP_1865", "PP_2964", "PP_2971"]
    rts = ["PP_0635", "PP_1250", "PP_1846"]
    return {
        "id": "MODULE:mobile_genetic_elements_boundary",
        "title": "Mobile genetic element recombination, transposition, and retroelement boundary",
        "description": (
            "Boundary module for PSEPK DNA-bucket members that resolve to mobile-element integrase, resolvase, "
            "transposase, excisionase, YqaJ-like recombinase, or reverse-transcriptase context rather than chromosome "
            "replication, homologous recombination, or DNA repair."
        ),
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": "file:projects/P_PUTIDA/batches/module_dna_replication_repair_recombination_mobile_integrase_recombinase_transposase.tsv",
                "title": "PSEPK mobile integrase/recombinase/transposase split table",
                "statement": "The split table routes 25 DNA-bucket genes to mobile-element recombinase, integrase, transposase, excisionase, or YqaJ-like context.",
            },
            {
                "source_id": "file:projects/P_PUTIDA/batches/module_dna_replication_repair_recombination_retroelement_reverse_transcriptase.tsv",
                "title": "PSEPK retroelement reverse-transcriptase split table",
                "statement": "The split table routes three DNA-bucket genes to reverse-transcriptase/retroelement context.",
            },
        ],
        "notes": (
            "First-pass boundary. PP_2495 is retained as an unresolved YqaJ viral recombinase-domain member with no "
            "GOA rows and no synthetic core GO function in its gene review. PP_0635 was already curated before this "
            "batch and is reused here with newly generated Asta provider coverage."
        ),
        "module": {
            "id": "mobile_genetic_elements_boundary",
            "label": "Mobile genetic element recombination/transposition boundary",
            "module_type": "BIOLOGICAL_PROCESS",
            "concepts": [
                descriptor("GO:0000150", "DNA strand exchange by resolvase/site-specific recombinase-family proteins."),
                descriptor("GO:0009037", "Tyrosine recombinase/integrase activity for phage or integrative elements."),
                descriptor("GO:0004803", "Transposase activity for insertion-sequence or Tn-family elements."),
                descriptor("GO:0003964", "RNA-directed DNA polymerase activity for reverse-transcriptase-family mobile elements."),
                descriptor("GO:0015074", "Mobile-element DNA integration process context."),
                descriptor("GO:0006313", "DNA transposition process context."),
            ],
            "parts": [
                {
                    "order": 1,
                    "role": "Resolvase and strand-exchange recombinases",
                    "node": {
                        "id": "resolvase_strand_exchange_recombinases",
                        "label": "Resolvase/strand-exchange recombinases",
                        "module_type": "MOLECULAR_FUNCTION",
                        "annotons": [
                            annoton(g, "GO:0000150", ["GO:0006310"] + (["GO:0015074"] if g != "PP_3026" else []), "dna_strand_exchange", "resolvase-family DNA strand exchange activity")
                            for g in resolvases
                        ],
                    },
                },
                {
                    "order": 2,
                    "role": "Phage and integrative-element recombinases",
                    "node": {
                        "id": "phage_integrase_tyrosine_recombinases",
                        "label": "Phage/integrative-element recombinases",
                        "module_type": "BIOLOGICAL_PROCESS",
                        "annotons": [
                            annoton(g, "GO:0009037" if g not in {"PP_2937", "PP_4415"} else "GO:0003677", ["GO:0006310", "GO:0015074"], "site_specific_recombination", "phage or integrative-element recombination/integration context")
                            for g in integrases
                        ],
                    },
                },
                {
                    "order": 3,
                    "role": "Excisionase and unresolved recombinase-like context",
                    "node": {
                        "id": "excisionase_yqaj_recombinase_boundary",
                        "label": "Excisionase/YqaJ recombinase boundary",
                        "module_type": "BIOLOGICAL_PROCESS",
                        "annotons": [
                            annoton("PP_1533", "GO:0003677", ["GO:0006310"], "excisionase_dna_binding", "excisionase-like DNA-binding recombination context"),
                            annoton(
                                "PP_2495",
                                None,
                                [],
                                "unresolved_yqaj_context",
                                "YqaJ viral recombinase-domain context; no GOA/core GO function asserted",
                                "No fetched GOA rows; retained as a bounded mobile-element recombinase-like knowledge gap.",
                            ),
                        ],
                    },
                },
                {
                    "order": 4,
                    "role": "Transposases",
                    "node": {
                        "id": "mobile_element_transposases",
                        "label": "Mobile-element transposases",
                        "module_type": "BIOLOGICAL_PROCESS",
                        "annotons": [
                            annoton(g, "GO:0004803", ["GO:0006313"], "transposase", "transposase activity in DNA transposition")
                            for g in transposases
                        ],
                    },
                },
                {
                    "order": 5,
                    "role": "Retroelement/group-II-intron reverse transcriptases",
                    "node": {
                        "id": "retroelement_reverse_transcriptases",
                        "label": "Retroelement reverse transcriptases",
                        "module_type": "BIOLOGICAL_PROCESS",
                        "annotons": [
                            annoton(g, "GO:0003964", ["GO:0006278"], "rna_directed_dna_polymerase", "reverse-transcriptase-family RNA-directed DNA polymerase activity")
                            for g in rts
                        ],
                    },
                },
            ],
        },
    }


def main() -> None:
    for gene in MOBILE_GENES + RT_GENES:
        curate_gene(gene)
    MODULE_PATH.write_text(
        yaml.dump(module_yaml(), Dumper=NoAliasDumper, sort_keys=False, allow_unicode=False, width=120),
        encoding="utf-8",
    )
    print(f"Curated {len(MOBILE_GENES) + len(RT_GENES)} gene reviews")
    print(f"Wrote {MODULE_PATH}")


if __name__ == "__main__":
    main()
