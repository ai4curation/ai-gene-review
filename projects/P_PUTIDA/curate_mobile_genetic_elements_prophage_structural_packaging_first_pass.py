#!/usr/bin/env python3
"""First-pass curation for PSEPK prophage structural and packaging proteins."""

from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes" / "PSEPK"
MODULE_PATH = ROOT / "modules" / "phage_structural_packaging_boundary.yaml"
BATCH_ID = "module_mobile_genetic_elements_prophage_structural_packaging"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


TERM = {
    "GO:0004519": {"id": "GO:0004519", "label": "endonuclease activity"},
    "GO:0005198": {"id": "GO:0005198", "label": "structural molecule activity"},
    "GO:0019068": {"id": "GO:0019068", "label": "virion assembly"},
}

GENES = [
    "PP_1562",
    "PP_1563",
    "PP_1565",
    "PP_1569",
    "PP_1574",
    "PP_1577",
    "PP_2287",
    "PP_2288",
    "PP_3044",
    "PP_3058",
    "PP_3061",
    "PP_3064",
    "PP_3862",
    "PP_3863",
    "PP_3867",
    "PP_3869",
    "PP_3877",
    "PP_3879",
    "PP_3881",
    "PP_3882",
    "PP_4135",
]

TERMINASE_LARGE = {"PP_1563", "PP_3881"}
STRUCTURAL = {
    "PP_1565",
    "PP_1569",
    "PP_1574",
    "PP_1577",
    "PP_2288",
    "PP_3044",
    "PP_3064",
    "PP_3863",
    "PP_3867",
    "PP_3869",
    "PP_3877",
    "PP_3879",
    "PP_4135",
}
UNRESOLVED = set(GENES) - TERMINASE_LARGE - STRUCTURAL

DOMAIN_NEEDLES = {
    "PP_1563": ("P-loop_NTPase", "TerL_ATPase", "TerL_nuclease", "Terminase_largesu-like", "TerL_nuclease"),
    "PP_3881": ("P-loop_NTPase", "TerL_ATPase", "TerL_nuclease", "Terminase_largesu-like", "TerL_nuclease"),
    "PP_1565": ("Phage/GTA_portal", "Portal_HK97", "Phage_portal"),
    "PP_1569": ("Phage_HK97_gp6-like",),
    "PP_1574": ("Phage_TAC_12", "Phage_TAC_13"),
    "PP_1577": ("Phage_tape_meas_C", "Tape_meas_lam_C"),
    "PP_2287": ("Lysozyme-like_dom_sf", "Transglycosylase_SLT_dom_1", "SLT"),
    "PP_2288": ("Phage_T7_tail_fibre-like_N", "Phage_T7_tail"),
    "PP_3044": ("Phage_lambda_portal", "Phage_portal_2"),
    "PP_3061": ("Phage_tail_E/E", "Phage_TAC_7"),
    "PP_3064": ("GpX-like", "Phage_tail_X"),
    "PP_3862": ("GpV/Gp45", "Phage_Mu_Gp45"),
    "PP_3863": ("Baseplate-like_2-layer_sand", "Baseplate_GpP", "Gp44/GpP-like", "GpP-like"),
    "PP_3867": ("Phage_Mu_GpM_tail_tub", "Tail_tube"),
    "PP_3869": ("Phage_sheath_subtilisin", "Tail_sheath", "Phage_sheath_1"),
    "PP_3877": ("Phage_capsid", "Phage_capsid-like_C"),
    "PP_3879": ("Phage/GTA_portal", "Portal_HK97", "Phage_portal"),
    "PP_3882": ("Phage_term_ssu_P27", "Terminase_4"),
    "PP_4135": ("Phage_head_completion_GpL", "Phage_GPL"),
}


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


def add_unique(items: list[dict], item: dict | None) -> None:
    if item and item not in items:
        items.append(item)


def file_id(gene: str, suffix: str) -> str:
    return f"file:PSEPK/{gene}/{gene}-{suffix}"


def gene_file(gene: str, suffix: str) -> Path:
    return GENE_ROOT / gene / f"{gene}-{suffix}"


def product_line(gene: str) -> str | None:
    path = gene_file(gene, "uniprot.txt")
    return optional_first_line(path, "DE   RecName") or optional_first_line(path, "DE   SubName")


def product_text(gene: str) -> str:
    return (product_line(gene) or "DE   SubName: Full=prophage protein").removeprefix("DE   ").rstrip(".")


def goa_line(gene: str, term_id: str) -> str | None:
    return optional_first_line(gene_file(gene, "goa.tsv"), term_id)


def evidence_for(gene: str, term_id: str | None = None) -> list[dict[str, str]]:
    path = gene_file(gene, "uniprot.txt")
    items: list[dict[str, str]] = []
    if term_id:
        add_unique(items, support(file_id(gene, "goa.tsv"), goa_line(gene, term_id)))
    add_unique(items, support(file_id(gene, "uniprot.txt"), product_line(gene)))
    if term_id:
        add_unique(items, support(file_id(gene, "uniprot.txt"), optional_first_line(path, f"DR   GO; {term_id};")))
    for needle in DOMAIN_NEEDLES.get(gene, ()):
        add_unique(items, support(file_id(gene, "uniprot.txt"), optional_first_line(path, needle)))
    for marker in ("DR   PANTHER;", "DR   Pfam;", "CC       "):
        add_unique(items, support(file_id(gene, "uniprot.txt"), optional_first_line(path, marker)))
    asta = gene_file(gene, "deep-research-asta.md")
    add_unique(items, support(file_id(gene, "deep-research-asta.md"), optional_first_line(asta, "uniprot_accession:")))
    add_unique(items, support(file_id(gene, "deep-research-asta.md"), optional_first_line(asta, "protein_description:")))
    add_unique(items, support(file_id(gene, "deep-research-asta.md"), optional_first_line(asta, "protein_domains:")))
    return items


def description_for(gene: str) -> str:
    product = product_text(gene)
    if gene in TERMINASE_LARGE:
        return (
            f"{gene} encodes a phage terminase large subunit ({product}) with TerL ATPase and nuclease domain support. "
            "It is consistent with the catalytic DNA-cleavage component of prophage genome packaging during virion assembly."
        )
    if gene in {"PP_1562", "PP_3882"}:
        return (
            f"{gene} encodes a phage terminase small-subunit candidate ({product}). The record supports prophage genome "
            "packaging context, but no specific GO molecular function is resolved in this first pass."
        )
    if gene in {"PP_1565", "PP_3044", "PP_3879"}:
        return (
            f"{gene} encodes a phage portal protein ({product}) with portal-family domain support, consistent with a "
            "structural role in phage head assembly and genome packaging."
        )
    if gene == "PP_1569":
        return (
            f"{gene} encodes a phage gp6-like head-tail connector protein ({product}) with HK97 gp6-like domain support, "
            "consistent with a structural head-tail connector role."
        )
    if gene == "PP_2287":
        return (
            f"{gene} encodes a phage internal core protein ({product}) with lysozyme-like/Slt transglycosylase-family "
            "domain evidence. The record indicates phage structural or host-cell-wall-contact context, but the precise "
            "molecular role is unresolved."
        )
    if gene in {"PP_2288", "PP_1574", "PP_1577", "PP_3064", "PP_3863", "PP_3867", "PP_3869"}:
        return (
            f"{gene} encodes a phage tail, tail-fiber, tube, sheath, tape-measure, or baseplate-associated protein "
            f"({product}) with phage structural domain support, consistent with a structural role in virion assembly."
        )
    if gene in {"PP_3061", "PP_3862"}:
        return (
            f"{gene} encodes a phage assembly-associated protein ({product}). The record supports assembly context, but "
            "does not resolve whether the protein is a virion structural component or an assembly accessory factor."
        )
    if gene in {"PP_3877", "PP_4135"}:
        return (
            f"{gene} encodes a phage capsid/head-associated protein ({product}) with capsid or head-completion domain "
            "support, consistent with a structural role in virion assembly."
        )
    return (
        f"{gene} encodes a phage structural or packaging candidate ({product}). The current local record does not resolve "
        "a more specific molecular function."
    )


def ensure_references(data: dict, gene: str) -> None:
    refs = data.setdefault("references", [])
    by_id = {ref.get("id"): ref for ref in refs}
    local_refs = [
        (file_id(gene, "uniprot.txt"), f"UniProtKB entry for {gene}", product_line(gene)),
        (file_id(gene, "goa.tsv"), f"QuickGO GOA annotations for {gene}", None),
        (
            file_id(gene, "deep-research-asta.md"),
            f"Asta retrieval report for {gene}",
            optional_first_line(gene_file(gene, "deep-research-asta.md"), "uniprot_accession:"),
        ),
    ]
    for ref_id, title, quote in local_refs:
        if ref_id in by_id:
            continue
        finding = {"statement": "Local first-pass source used for prophage structural/packaging review."}
        if quote:
            finding["supporting_text"] = quote
        refs.append({"id": ref_id, "title": title, "findings": [finding]})


def review_for(gene: str, term_id: str) -> dict:
    if gene in TERMINASE_LARGE and term_id == "GO:0004519":
        return {
            "summary": "Endonuclease activity is supported for the phage terminase large subunit.",
            "action": "ACCEPT",
            "reason": "The GOA row is supported by the TerL nuclease domain; the ATPase domain is noted as packaging context, but no separate ATPase activity is asserted here.",
            "supported_by": evidence_for(gene, term_id),
        }
    if gene in TERMINASE_LARGE and term_id == "GO:0019068":
        return {
            "summary": "Virion assembly is added as the process context for terminase-mediated genome packaging.",
            "action": "NEW",
            "reason": "Phage terminase large subunits cleave and package viral DNA as part of virion assembly; the TerL ATPase/nuclease domain architecture supports this process context.",
            "supported_by": evidence_for(gene, None),
        }
    if gene in STRUCTURAL and term_id == "GO:0005198":
        return {
            "summary": "Structural molecule activity is supported for this phage structural component.",
            "action": "ACCEPT" if gene == "PP_3044" else "NEW",
            "reason": "The product name and phage structural domains support a structural virion-component role. No enzymatic function is asserted.",
            "supported_by": evidence_for(gene, term_id if gene == "PP_3044" else None),
        }
    if gene in STRUCTURAL and term_id == "GO:0019068":
        return {
            "summary": "Virion assembly is the supported biological-process context.",
            "action": "ACCEPT" if gene == "PP_3044" else "NEW",
            "reason": "Portal, tail, baseplate, sheath, capsid, and head proteins act as structural components assembled into phage particles.",
            "supported_by": evidence_for(gene, term_id if gene == "PP_3044" else None),
        }
    raise ValueError(f"No review rule for {gene} {term_id}")


def ensure_new_rows(data: dict, gene: str) -> None:
    rows = data.setdefault("existing_annotations", [])
    if gene in TERMINASE_LARGE and not any(row.get("term", {}).get("id") == "GO:0019068" for row in rows):
        rows.append(
            {
                "term": TERM["GO:0019068"],
                "evidence_type": "IEA",
                "original_reference_id": file_id(gene, "uniprot.txt"),
                "qualifier": "involved_in",
                "review": review_for(gene, "GO:0019068"),
            }
        )
    if gene in STRUCTURAL and not any(row.get("term", {}).get("id") == "GO:0005198" for row in rows):
        rows.append(
            {
                "term": TERM["GO:0005198"],
                "evidence_type": "IEA",
                "original_reference_id": file_id(gene, "uniprot.txt"),
                "qualifier": "enables",
                "review": review_for(gene, "GO:0005198"),
            }
        )
    if gene in STRUCTURAL and not any(row.get("term", {}).get("id") == "GO:0019068" for row in rows):
        rows.append(
            {
                "term": TERM["GO:0019068"],
                "evidence_type": "IEA",
                "original_reference_id": file_id(gene, "uniprot.txt"),
                "qualifier": "involved_in",
                "review": review_for(gene, "GO:0019068"),
            }
        )


def core_functions_for(gene: str) -> list[dict]:
    if gene in TERMINASE_LARGE:
        return [
            {
                "description": "Phage terminase large-subunit endonuclease activity in virion assembly.",
                "supported_by": evidence_for(gene, "GO:0004519"),
                "molecular_function": TERM["GO:0004519"],
                "directly_involved_in": [TERM["GO:0019068"]],
            }
        ]
    if gene in STRUCTURAL:
        return [
            {
                "description": "Phage structural molecule activity in virion assembly.",
                "supported_by": evidence_for(gene, "GO:0005198" if gene == "PP_3044" else None),
                "molecular_function": TERM["GO:0005198"],
                "directly_involved_in": [TERM["GO:0019068"]],
            }
        ]
    return []


def questions_for(gene: str) -> list[dict[str, str]]:
    if gene in STRUCTURAL:
        text = f"Is {gene} part of an intact prophage virion assembly locus, or a remnant structural gene?"
    elif gene in TERMINASE_LARGE:
        text = f"Does {gene} retain the full catalytic and ATPase machinery expected for an active phage terminase large subunit?"
    else:
        text = f"Does {gene} encode a functional prophage packaging/assembly component, or is it a low-confidence remnant?"
    return [{"question": text}]


def experiments_for(gene: str) -> list[dict[str, str]]:
    return [
        {
            "experiment_type": "prophage locus inspection",
            "description": f"Inspect the genomic neighborhood of {gene} for synteny with terminase, portal, head, tail, and lysis modules.",
            "hypothesis": f"{gene} is part of a coherent prophage structural or packaging locus.",
        },
        {
            "experiment_type": "comparative sequence analysis",
            "description": f"Compare {gene} against curated phage structural and packaging proteins to assess domain completeness and conserved motifs.",
            "hypothesis": f"{gene} retains the expected sequence features for its prophage structural/packaging role.",
        },
    ]


def curate_gene(gene: str) -> None:
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(read_text(path))
    data["status"] = "DRAFT"
    data["description"] = description_for(gene)
    ensure_references(data, gene)
    for row in data.get("existing_annotations") or []:
        term_id = row.get("term", {}).get("id")
        row["review"] = review_for(gene, term_id)
    ensure_new_rows(data, gene)
    data["core_functions"] = core_functions_for(gene)
    data["proposed_new_terms"] = []
    data["suggested_questions"] = questions_for(gene)
    data["suggested_experiments"] = experiments_for(gene)
    path.write_text(yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, width=120), encoding="utf-8")


def descriptor(term_id: str, description: str | None = None) -> dict:
    obj = {"preferred_term": TERM[term_id]["label"], "term": TERM[term_id]}
    if description:
        obj["description"] = description
    return obj


def annoton(gene: str) -> dict:
    if gene in TERMINASE_LARGE:
        role = "phage terminase large-subunit endonuclease activity in virion assembly"
        function = descriptor("GO:0004519")
    else:
        role = "phage structural molecule activity in virion assembly"
        function = descriptor("GO:0005198")
    return {
        "id": f"{gene.lower()}_phage_structural_packaging",
        "label": f"{gene}: {role}",
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "role_description": role,
        "function": function,
        "processes": [descriptor("GO:0019068")],
    }


def write_module() -> None:
    annotons = [annoton(gene) for gene in sorted(TERMINASE_LARGE | STRUCTURAL)]
    unresolved_notes = ", ".join(sorted(UNRESOLVED))
    data = {
        "id": "MODULE:phage_structural_packaging_boundary",
        "title": "Prophage structural and genome-packaging boundary",
        "description": "Boundary module for PSEPK prophage terminase, portal, head, capsid, tail, sheath, tube, fiber, and assembly proteins that resolve to virion structural or packaging context rather than metabolic pathways.",
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": f"file:projects/P_PUTIDA/batches/{BATCH_ID}.tsv",
                "title": "PSEPK mobile-genetic-elements prophage structural/packaging split table",
                "statement": "The split table routes 21 broad mobile-genetic-elements genes to terminase, portal, head-tail connector, tail, fiber, tube, sheath, capsid/head, or unresolved assembly contexts.",
            }
        ],
        "notes": (
            "First-pass boundary. Large terminases are represented by endonuclease activity in virion assembly. "
            "Domain-supported portal, tail, baseplate, sheath, capsid, and head proteins are represented as structural "
            "molecule activity in virion assembly. Product-only small terminases, assembly/accessory proteins, and the "
            f"ambiguous internal-core/Slt-domain member are retained as no-core unresolved context in their gene reviews: {unresolved_notes}."
        ),
        "module": {
            "id": "phage_structural_packaging_boundary",
            "label": "Prophage structural and genome-packaging boundary",
            "module_type": "BIOLOGICAL_PROCESS",
            "concepts": [
                descriptor("GO:0004519", "Terminase large-subunit nuclease activity for genome packaging."),
                descriptor("GO:0005198", "Structural molecule activity for phage virion components."),
                descriptor("GO:0019068", "Virion assembly process context."),
            ],
            "parts": [
                {
                    "order": 1,
                    "role": "Terminase, portal, head, tail, and capsid structural/packaging proteins",
                    "node": {
                        "id": "phage_structural_packaging_components",
                        "label": "Prophage structural and packaging components",
                        "module_type": "BIOLOGICAL_PROCESS",
                        "annotons": annotons,
                    },
                }
            ],
        },
    }
    MODULE_PATH.write_text(yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, width=120), encoding="utf-8")


def main() -> None:
    for gene in GENES:
        curate_gene(gene)
    write_module()
    print(f"Curated {len(GENES)} gene reviews")
    print(f"Wrote {MODULE_PATH}")


if __name__ == "__main__":
    main()
