#!/usr/bin/env python3
"""First-pass curation for PSEPK mobile-genetic-element GOA-supported transposases."""

from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes" / "PSEPK"
MODULE_PATH = ROOT / "modules" / "mobile_genetic_elements_boundary.yaml"
BATCH_TSV = ROOT / "projects/P_PUTIDA/batches/module_mobile_genetic_elements_transposase_goa_supported.tsv"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


TERM = {
    "GO:0003676": {"id": "GO:0003676", "label": "nucleic acid binding"},
    "GO:0003677": {"id": "GO:0003677", "label": "DNA binding"},
    "GO:0004518": {"id": "GO:0004518", "label": "nuclease activity"},
    "GO:0004519": {"id": "GO:0004519", "label": "endonuclease activity"},
    "GO:0004803": {"id": "GO:0004803", "label": "transposase activity"},
    "GO:0006310": {"id": "GO:0006310", "label": "DNA recombination"},
    "GO:0006313": {"id": "GO:0006313", "label": "DNA transposition"},
    "GO:0015074": {"id": "GO:0015074", "label": "DNA integration"},
    "GO:0016787": {"id": "GO:0016787", "label": "hydrolase activity"},
    "GO:0043565": {"id": "GO:0043565", "label": "sequence-specific DNA binding"},
}


GENES = [
    "PP_0014",
    "PP_0334",
    "PP_0526",
    "PP_0568",
    "PP_1133",
    "PP_1931",
    "PP_2570",
    "PP_2976",
    "tnpB",
    "PP_3498",
    "PP_3499",
    "PP_3966",
    "insN",
    "PP_4420",
    "PP_4441",
    "PP_4444",
    "PP_4445",
    "PP_5176",
]

IS3_RVE_GENES = {"PP_0014", "tnpB", "PP_4420", "PP_4445"}
IS200_GENES = {"PP_0568", "PP_5176"}
TRANSPOSASE8_GENES = {"PP_2976", "PP_3499", "PP_3966", "insN", "PP_4441", "PP_4444"}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def optional_first_line(path: Path, *needles: str) -> str | None:
    if not path.exists():
        return None
    for line in read_text(path).splitlines():
        if all(needle in line for needle in needles):
            return line
    return None


def support(reference_id: str, text: str | None) -> dict[str, str] | None:
    if not text:
        return None
    return {"reference_id": reference_id, "supporting_text": text}


def add_unique(items: list[dict[str, str]], item: dict[str, str] | None) -> None:
    if item and item not in items:
        items.append(item)


def file_id(gene: str, suffix: str) -> str:
    return f"file:PSEPK/{gene}/{gene}-{suffix}"


def gene_file(gene: str, suffix: str) -> Path:
    return GENE_ROOT / gene / f"{gene}-{suffix}"


def product_line(gene: str) -> str | None:
    path = gene_file(gene, "uniprot.txt")
    return optional_first_line(path, "DE   RecName") or optional_first_line(path, "DE   SubName")


def goa_line(gene: str, term_id: str) -> str | None:
    return optional_first_line(gene_file(gene, "goa.tsv"), term_id)


def uniprot_evidence(gene: str, term_id: str | None = None, domain_needles: tuple[str, ...] = ()) -> list[dict[str, str]]:
    path = gene_file(gene, "uniprot.txt")
    items: list[dict[str, str]] = []
    add_unique(items, support(file_id(gene, "uniprot.txt"), product_line(gene)))
    if term_id:
        add_unique(items, support(file_id(gene, "uniprot.txt"), optional_first_line(path, f"DR   GO; {term_id};")))
    for needle in domain_needles:
        add_unique(items, support(file_id(gene, "uniprot.txt"), optional_first_line(path, needle)))
    for marker in ("DR   InterPro;", "DR   Pfam;", "Belongs to the transposase", "KW   Transposition"):
        add_unique(items, support(file_id(gene, "uniprot.txt"), optional_first_line(path, marker)))
    return items


def asta_evidence(gene: str) -> list[dict[str, str]]:
    path = gene_file(gene, "deep-research-asta.md")
    items: list[dict[str, str]] = []
    add_unique(items, support(file_id(gene, "deep-research-asta.md"), optional_first_line(path, "uniprot_accession:")))
    add_unique(items, support(file_id(gene, "deep-research-asta.md"), optional_first_line(path, "protein_description:")))
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


def has_term(data: dict, term_id: str) -> bool:
    return any(ann.get("term", {}).get("id") == term_id for ann in data.get("existing_annotations") or [])


def family_label(gene: str) -> str:
    if gene in IS3_RVE_GENES:
        return "IS3/rve-family integrase-core transposase"
    if gene in IS200_GENES:
        return "IS200-like Y1 transposase"
    if gene in TRANSPOSASE8_GENES:
        return "transposase-8-family insertion-sequence protein"
    if gene == "PP_1931":
        return "IS1182-family transposase"
    return "IS110-like transposase"


def description_for(gene: str, data: dict) -> str:
    product = (product_line(gene) or "mobile-element transposase").removeprefix("DE   ").rstrip(".")
    if gene in IS3_RVE_GENES:
        return (
            f"{gene} encodes an {family_label(gene)} ({product}) with RNaseH/rve-like integrase catalytic domain "
            "support. It is associated with mobile-element DNA transposition and integration, where the catalytic "
            "domain supports an endonuclease or strand-transfer role on nucleic-acid substrates."
        )
    return (
        f"{gene} encodes a mobile-element {family_label(gene)} ({product}). It carries transposase-family domain "
        "features and is associated with DNA transposition, with DNA binding reflecting substrate or target-site "
        "recognition during mobile-element movement."
    )


def review_for(gene: str, data: dict, term_id: str) -> dict:
    if term_id == "GO:0004803":
        return {
            "summary": "Transposase activity is the supported molecular function for this mobile-element protein.",
            "action": "ACCEPT",
            "reason": "The fetched GOA and UniProt/InterPro records identify a transposase-family protein, making transposase activity the core molecular-function call.",
            "supported_by": evidence_for(gene, term_id, ("Transpos", "DDE_Tnp", "Y1_Tnp", "HTH_Tnp", "DEDD_Tnp")),
        }

    if term_id == "GO:0006313":
        return {
            "summary": "DNA transposition is the supported biological process for this mobile-element protein.",
            "action": "ACCEPT",
            "reason": "Transposase-family domains, product names, and the GOA process row support DNA transposition. This is mobile-element biology, not chromosomal DNA repair.",
            "supported_by": evidence_for(gene, term_id, ("Transpos", "DDE_Tnp", "Y1_Tnp", "HTH_Tnp", "rve")),
        }

    if term_id == "GO:0015074":
        return {
            "summary": "DNA integration is compatible with the IS3/rve-family transposase context.",
            "action": "ACCEPT",
            "reason": "The GOA row is InterPro-derived from the integrase catalytic core, and the protein records support a mobile-element integration/transposition context.",
            "supported_by": evidence_for(gene, term_id, ("Integrase_cat-core", "RNaseH", "rve", "Transpos_IS3")),
        }

    if term_id == "GO:0004519":
        return {
            "summary": "Endonuclease activity is retained as the current catalytic molecular-function call for this IS3/rve-family record.",
            "action": "ACCEPT",
            "reason": "The UniRule and RNaseH/rve-like integrase catalytic domain evidence support an endonuclease-type catalytic role, while the exact transposase specificity is not asserted as a new annotation here.",
            "supported_by": evidence_for(gene, term_id, ("Integrase_cat-core", "RNaseH", "rve", "Transpos_IS3")),
        }

    if term_id == "GO:0003677":
        return {
            "summary": "DNA binding is compatible but less informative than transposase activity.",
            "action": "KEEP_AS_NON_CORE",
            "reason": "DNA binding is expected for transposases, but the more specific transposase activity and DNA transposition terms capture the core function.",
            "supported_by": evidence_for(gene, term_id, ("DNA-bd", "HTH", "Transpos")),
        }

    if term_id == "GO:0043565":
        return {
            "summary": "Sequence-specific DNA binding is compatible with IS200-like target-site recognition but is not the core catalytic call.",
            "action": "KEEP_AS_NON_CORE",
            "reason": "TreeGrafter supports a DNA-recognition role for the IS200-like protein, while transposase activity and DNA transposition are the main functional annotations.",
            "supported_by": evidence_for(gene, term_id, ("RAYT_transposase", "Transposase_17", "Y1_Tnp")),
        }

    if term_id == "GO:0003676":
        return {
            "summary": "Nucleic acid binding is retained as a broad substrate-binding annotation.",
            "action": "KEEP_AS_NON_CORE",
            "reason": "The term is compatible with the RNaseH/rve-like integrase core but is less informative than the endonuclease and mobile-element process annotations.",
            "supported_by": evidence_for(gene, term_id, ("Integrase_cat-core", "RNaseH", "rve", "Transpos_IS3")),
        }

    if term_id == "GO:0006310":
        return {
            "summary": "DNA recombination is compatible but broad relative to DNA transposition/integration.",
            "action": "KEEP_AS_NON_CORE",
            "reason": "The annotation reflects mobile-element recombination context. It is retained, but the more specific DNA transposition and/or integration process terms are used for the core function.",
            "supported_by": evidence_for(gene, term_id, ("Integrase_cat-core", "RNaseH", "rve", "Transpos")),
        }

    if term_id in {"GO:0004518", "GO:0016787"}:
        return {
            "summary": "This parent catalytic term is less informative than the endonuclease activity row.",
            "action": "MARK_AS_OVER_ANNOTATED",
            "reason": "The parent nuclease/hydrolase term is compatible with the catalytic domain but adds little once the more specific endonuclease activity is present.",
            "supported_by": evidence_for(gene, term_id, ("Integrase_cat-core", "RNaseH", "rve")),
        }

    raise ValueError(f"No review rule for {gene} {term_id}")


def core_function_for(gene: str, data: dict) -> list[dict]:
    if gene in IS3_RVE_GENES:
        return [
            {
                "description": "IS3/rve-family endonuclease activity in mobile-element DNA transposition and integration.",
                "supported_by": evidence_for(gene, "GO:0004519", ("Integrase_cat-core", "RNaseH", "rve", "Transpos_IS3")),
                "molecular_function": TERM["GO:0004519"],
                "directly_involved_in": [TERM["GO:0006313"], TERM["GO:0015074"]],
            }
        ]

    return [
        {
            "description": "Mobile-element transposase activity driving DNA transposition.",
            "supported_by": evidence_for(gene, "GO:0004803", ("Transpos", "DDE_Tnp", "Y1_Tnp", "HTH_Tnp")),
            "molecular_function": TERM["GO:0004803"],
            "directly_involved_in": [TERM["GO:0006313"]],
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
            optional_first_line(gene_file(gene, "deep-research-asta.md"), "uniprot_accession:"),
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


def suggested_questions_for(gene: str) -> list[dict[str, str]]:
    if gene in IS3_RVE_GENES:
        question = f"Which Tn4652/IS3-family element boundary and target-site chemistry define the in vivo role of {gene}?"
    else:
        question = f"What insertion-sequence or transposon copy does {gene} act on in P. putida KT2440?"
    return [{"question": question}]


def suggested_experiments_for(gene: str) -> list[dict[str, str]]:
    if gene in IS3_RVE_GENES:
        return [
            {
                "experiment_type": "integration or strand-transfer assay",
                "description": f"Test purified {gene} or a reconstructed mobile-element system with candidate terminal-repeat DNA substrates.",
                "hypothesis": f"{gene} contributes endonuclease/strand-transfer activity to mobile-element DNA integration or transposition.",
            }
        ]
    return [
        {
            "experiment_type": "transposition reporter assay",
            "description": f"Use a marked insertion-sequence or transposon reporter to test whether {gene} catalyzes DNA transposition.",
            "hypothesis": f"{gene} is an active mobile-element transposase.",
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
    data["suggested_questions"] = suggested_questions_for(gene)
    data["suggested_experiments"] = suggested_experiments_for(gene)
    path.write_text(yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=False, width=120), encoding="utf-8")


def descriptor(term_id: str, description: str | None = None) -> dict:
    item = {"preferred_term": TERM[term_id]["label"], "term": TERM[term_id]}
    if description:
        item["description"] = description
    return item


def participant(gene: str) -> dict:
    return {"selector_type": "GENE", "gene": {"preferred_term": gene}}


def annoton(gene: str) -> dict:
    if gene in IS3_RVE_GENES:
        function_id = "GO:0004519"
        processes = ["GO:0006313", "GO:0015074"]
        role = "IS3/rve-family endonuclease activity in DNA transposition/integration"
        label = "is3_rve_endonuclease"
    else:
        function_id = "GO:0004803"
        processes = ["GO:0006313"]
        role = "transposase activity in DNA transposition"
        label = "mobile_bucket_transposase"
    return {
        "id": f"{gene.lower().replace('-', '_')}_{label}",
        "label": f"{gene}: {role}",
        "participant": participant(gene),
        "role_description": role,
        "function": descriptor(function_id),
        "processes": [descriptor(process_id) for process_id in processes],
    }


def ensure_concept(module: dict, term_id: str, description: str) -> None:
    concepts = module["module"].setdefault("concepts", [])
    if any(c.get("term", {}).get("id") == term_id for c in concepts):
        return
    concepts.append(descriptor(term_id, description))


def add_or_replace_module_part() -> None:
    data = yaml.safe_load(MODULE_PATH.read_text())
    evidence = data.setdefault("evidence", [])
    source_id = "file:projects/P_PUTIDA/batches/module_mobile_genetic_elements_transposase_goa_supported.tsv"
    if not any(item.get("source_id") == source_id for item in evidence):
        evidence.append(
            {
                "source_id": source_id,
                "title": "PSEPK mobile-genetic-elements GOA-supported transposase split table",
                "statement": "The split table routes 18 broad mobile-genetic-elements genes to GOA-supported transposase or IS3/rve integration/transposition context.",
            }
        )

    data["description"] = (
        "Boundary module for PSEPK DNA-bucket and broad mobile-genetic-elements members that resolve to mobile-element "
        "integrase, resolvase, transposase, excisionase, YqaJ-like recombinase, reverse-transcriptase, or "
        "integration/transposition context rather than chromosome replication, homologous recombination, or DNA repair."
    )
    note = (
        "The module:mobile_genetic_elements transposase_goa_supported sub-batch adds 18 broad-bucket genes; four "
        "IS3/rve-family records are kept as endonuclease/integration/transposition calls without synthetic "
        "transposase-activity rows."
    )
    current_notes = data.get("notes", "").replace(note, "").strip()
    data["notes"] = f"{current_notes} {note}".strip()

    ensure_concept(data, "GO:0004519", "Endonuclease activity for IS3/rve-family integrase-core transposition proteins.")
    parts = data["module"].setdefault("parts", [])
    parts[:] = [
        part
        for part in parts
        if part.get("node", {}).get("id") != "mobile_bucket_goa_supported_transposases"
    ]
    parts.append(
        {
            "order": max([part.get("order", 0) for part in parts] or [0]) + 1,
            "role": "GOA-supported transposases from broad mobile-genetic-elements bucket",
            "node": {
                "id": "mobile_bucket_goa_supported_transposases",
                "label": "Broad-bucket GOA-supported transposases",
                "module_type": "BIOLOGICAL_PROCESS",
                "annotons": [annoton(gene) for gene in GENES],
            },
        }
    )
    MODULE_PATH.write_text(yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=False, width=120), encoding="utf-8")


def main() -> None:
    if not BATCH_TSV.exists():
        raise FileNotFoundError(BATCH_TSV)
    for gene in GENES:
        curate_gene(gene)
    add_or_replace_module_part()
    print(f"Curated {len(GENES)} gene reviews")
    print(f"Updated {MODULE_PATH}")


if __name__ == "__main__":
    main()
