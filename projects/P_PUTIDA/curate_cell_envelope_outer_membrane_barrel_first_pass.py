#!/usr/bin/env python3
"""First-pass curate PSEPK outer-membrane barrel/channel boundary candidates."""

from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes" / "PSEPK"


TERM = {
    "GO:0005509": {"id": "GO:0005509", "label": "calcium ion binding"},
    "GO:0009279": {"id": "GO:0009279", "label": "cell outer membrane"},
    "GO:0015288": {"id": "GO:0015288", "label": "porin activity"},
    "GO:0016020": {"id": "GO:0016020", "label": "membrane"},
    "GO:0019867": {"id": "GO:0019867", "label": "outer membrane"},
}


def read_lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8").splitlines()


def first_line(path: Path, *needles: str) -> str:
    for line in read_lines(path):
        if all(needle in line for needle in needles):
            return line
    raise ValueError(f"No line in {path} contains all needles: {needles}")


def file_id(gene: str, suffix: str) -> str:
    return f"file:PSEPK/{gene}/{gene}-{suffix}"


def support(reference_id: str, text: str) -> dict[str, str]:
    return {"reference_id": reference_id, "supporting_text": text}


def common_support(
    gene: str,
    *,
    go_term: str | None = None,
    domain: str | None = None,
    similarity: str | None = None,
) -> list[dict[str, str]]:
    uniprot = GENE_ROOT / gene / f"{gene}-uniprot.txt"
    asta = GENE_ROOT / gene / f"{gene}-deep-research-asta.md"
    goa = GENE_ROOT / gene / f"{gene}-goa.tsv"
    data: list[dict[str, str]] = []
    if go_term:
        goa_snippet = f"{go_term}\t{TERM[go_term]['label']}"
        if goa.exists() and goa_snippet in goa.read_text(encoding="utf-8"):
            data.append(support(file_id(gene, "goa.tsv"), goa_snippet))
    data.append(support(file_id(gene, "uniprot.txt"), first_line(uniprot, "DE   ")))
    if domain:
        data.append(support(file_id(gene, "uniprot.txt"), first_line(uniprot, domain)))
    if similarity:
        data.append(support(file_id(gene, "uniprot.txt"), first_line(uniprot, similarity)))
    data.append(support(file_id(gene, "deep-research-asta.md"), first_line(asta, "- **Protein Description:**")))
    return data


def reference_list(existing_refs: list[dict], gene: str, accession: str) -> list[dict]:
    refs: list[dict] = []
    seen = set()
    for ref in existing_refs:
        ref_id = ref["id"]
        seen.add(ref_id)
        refs.append(ref)
    for ref_id in (file_id(gene, "goa.tsv"), file_id(gene, "uniprot.txt"), file_id(gene, "deep-research-asta.md")):
        if ref_id in seen:
            continue
        title = {
            file_id(gene, "goa.tsv"): f"QuickGO GOA annotations for {gene} ({accession})",
            file_id(gene, "uniprot.txt"): f"UniProtKB entry for {gene} ({accession})",
            file_id(gene, "deep-research-asta.md"): f"Asta retrieval report for {gene} ({accession})",
        }[ref_id]
        refs.append({"id": ref_id, "title": title, "findings": []})
    return refs


def review(
    gene: str,
    term_id: str,
    summary: str,
    action: str,
    reason: str,
    *,
    support_go: str | None = None,
    support_domain: str | None = None,
    support_similarity: str | None = None,
    replacements: list[str] | None = None,
) -> dict:
    obj = {
        "summary": summary,
        "action": action,
        "reason": reason,
        "supported_by": common_support(
            gene,
            go_term=support_go or term_id,
            domain=support_domain,
            similarity=support_similarity,
        ),
    }
    if replacements:
        obj["proposed_replacement_terms"] = [TERM[replacement] for replacement in replacements]
    return obj


def new_annotation(
    gene: str,
    term_id: str,
    qualifier: str,
    summary: str,
    reason: str,
    *,
    support_domain: str | None = None,
    support_similarity: str | None = None,
) -> dict:
    return {
        "term": TERM[term_id],
        "evidence_type": "IEA",
        "original_reference_id": file_id(gene, "uniprot.txt"),
        "qualifier": qualifier,
        "review": {
            "summary": summary,
            "action": "NEW",
            "reason": reason,
            "supported_by": common_support(gene, domain=support_domain, similarity=support_similarity),
        },
    }


GENES = {
    "yiaD": {
        "accession": "Q88PS5",
        "symbol": "yiaD",
        "description": "yiaD (PP_0773) encodes an OmpA/MotB-domain outer-membrane protein in Pseudomonas putida KT2440. The protein is best treated as an envelope structural or anchoring candidate in this first pass; no specific molecular activity or pathway role is established from the available metadata.",
        "domain": "OmpA-like.",
        "reviews": {
            "GO:0009279": (
                "Cell outer membrane localization is the most specific supported cellular-component annotation.",
                "ACCEPT",
                "The UniProt subcellular-location mapping and OmpA-family domain composition support an outer-membrane assignment.",
                None,
                "OmpA-like.",
                None,
                None,
            ),
            "GO:0016020": (
                "Generic membrane localization is correct but less informative than the outer-membrane annotation already present.",
                "MODIFY",
                "The OmpA-family annotation and UniProt subcellular-location mapping support cell outer membrane as the more informative component term.",
                None,
                "OMP_bac.",
                None,
                ["GO:0009279"],
            ),
        },
        "core": [
            {
                "description": "OmpA/MotB-domain outer-membrane protein with unresolved envelope structural or anchoring role.",
                "locations": [TERM["GO:0009279"]],
            }
        ],
        "question": "Does yiaD affect outer-membrane integrity, motility-associated envelope mechanics, or another envelope phenotype in KT2440?",
        "experiment": "Compare wild-type and yiaD deletion strains for outer-membrane permeability, envelope-stress sensitivity, and motility phenotypes.",
    },
    "PP_1121": {
        "accession": "Q88NT3",
        "symbol": "PP_1121",
        "description": "PP_1121 encodes an OmpA-family outer-membrane protein in Pseudomonas putida KT2440. A TSP type-3 repeat supports a calcium-binding inference, but the main curated role at this stage is envelope-localized OmpA-family context rather than a defined transport or remodeling pathway.",
        "domain": "OmpA-like.",
        "reviews": {
            "GO:0005509": (
                "Calcium ion binding is plausible from the TSP type-3 repeat but is not the core pathway role.",
                "KEEP_AS_NON_CORE",
                "The annotation is an InterPro2GO inference from the TSP type-3 repeat; it may describe a domain property without establishing a biological pathway role.",
                None,
                "TSP_type-3_rpt.",
                None,
                None,
            ),
            "GO:0009279": (
                "Cell outer membrane localization is the most specific supported cellular-component annotation.",
                "ACCEPT",
                "UniProt subcellular-location mapping and OmpA-family domains support outer-membrane localization.",
                None,
                "OmpA-like.",
                None,
                None,
            ),
            "GO:0016020": (
                "Generic membrane localization is correct but less informative than the outer-membrane annotation already present.",
                "MODIFY",
                "The available evidence points to the cell outer membrane, so the broader membrane term should be replaced by that component for curation purposes.",
                None,
                "OMP_bac.",
                None,
                ["GO:0009279"],
            ),
        },
        "core": [
            {
                "description": "OmpA-family outer-membrane protein with unresolved envelope role; calcium binding is kept as a non-core domain property.",
                "locations": [TERM["GO:0009279"]],
            }
        ],
        "question": "Is PP_1121 a structural outer-membrane protein, an adhesin-like protein, or a condition-specific envelope factor?",
        "experiment": "Profile PP_1121 abundance and deletion phenotypes under envelope stress, surface-attachment, and biofilm growth conditions.",
    },
    "PP_1122": {
        "accession": "Q88NT2",
        "symbol": "PP_1122",
        "description": "PP_1122 encodes an OmpA-family outer-membrane protein in Pseudomonas putida KT2440. Domain evidence supports outer-membrane localization and a possible calcium-binding repeat property, but the specific envelope function remains unresolved.",
        "domain": "OmpA-like.",
        "reviews": {
            "GO:0005509": (
                "Calcium ion binding is plausible from the TSP type-3 repeat but is not the core pathway role.",
                "KEEP_AS_NON_CORE",
                "The annotation is an InterPro2GO inference from the TSP type-3 repeat; it may reflect a repeat/domain property rather than the principal biological function.",
                None,
                "TSP_type-3_rpt.",
                None,
                None,
            ),
            "GO:0009279": (
                "Cell outer membrane localization is supported and specific enough for the current review.",
                "ACCEPT",
                "InterPro OmpA-like signatures and the UniProt subcellular-location mapping support cell outer membrane localization.",
                None,
                "OmpA-like.",
                None,
                None,
            ),
            "GO:0016020": (
                "Generic membrane localization is correct but less informative than cell outer membrane.",
                "MODIFY",
                "The same domain evidence already supports a more specific cell outer membrane assignment.",
                None,
                "OMP_bac.",
                None,
                ["GO:0009279"],
            ),
        },
        "core": [
            {
                "description": "OmpA-family outer-membrane protein with unresolved envelope role; calcium binding is kept as a non-core domain property.",
                "locations": [TERM["GO:0009279"]],
            }
        ],
        "question": "Does PP_1122 have a phenotype distinct from PP_1121, or are these paralogous OmpA-family envelope candidates redundant?",
        "experiment": "Construct PP_1121, PP_1122, and double deletion strains and compare surface, envelope-stress, and biofilm phenotypes.",
    },
    "PP_1880": {
        "accession": "Q88LP9",
        "symbol": "PP_1880",
        "description": "PP_1880 encodes a predicted outer-membrane autotransporter in Pseudomonas putida KT2440. The protein has an autotransporter beta-barrel domain and passenger-associated domains, so it is curated as an outer-membrane type V secretion/autotransporter candidate with unresolved passenger function.",
        "domain": "OM_autotransptr_brl_dom.",
        "reviews": {
            "GO:0019867": (
                "Outer membrane localization is supported by the autotransporter beta-barrel domain.",
                "ACCEPT",
                "InterPro assigns an outer-membrane autotransporter barrel domain, matching the UniProt product name.",
                None,
                "OM_autotransptr_brl_dom.",
                None,
                None,
            ),
        },
        "core": [
            {
                "description": "Predicted outer-membrane autotransporter with unresolved passenger domain function.",
                "locations": [TERM["GO:0019867"]],
            }
        ],
        "question": "What passenger function, substrate interaction, or surface phenotype is associated with PP_1880?",
        "experiment": "Test PP_1880 surface exposure and deletion phenotypes in adhesion, biofilm, and envelope-stress assays; map passenger-domain processing if expressed.",
    },
    "PP_3069": {
        "accession": "Q88ID0",
        "symbol": "PP_3069",
        "description": "PP_3069 encodes a predicted outer-membrane autotransporter in Pseudomonas putida KT2440. The autotransporter beta-barrel supports outer-membrane localization, but the passenger function is not established from the current first-pass evidence.",
        "domain": "OM_autotransptr_brl_dom.",
        "reviews": {
            "GO:0019867": (
                "Outer membrane localization is supported by the autotransporter beta-barrel domain.",
                "ACCEPT",
                "InterPro assigns an outer-membrane autotransporter barrel domain, matching the UniProt product name.",
                None,
                "OM_autotransptr_brl_dom.",
                None,
                None,
            ),
        },
        "core": [
            {
                "description": "Predicted outer-membrane autotransporter with unresolved passenger domain function.",
                "locations": [TERM["GO:0019867"]],
            }
        ],
        "question": "Does PP_3069 act as a surface adhesin, extracellular enzyme carrier, or another type V secretion passenger in KT2440?",
        "experiment": "Assay PP_3069-dependent surface localization, extracellular protein processing, adhesion, and biofilm phenotypes.",
    },
    "PP_3449": {
        "accession": "Q88HB1",
        "symbol": "PP_3449",
        "description": "PP_3449 encodes a predicted bacteriophage N4 receptor outer-membrane subunit in Pseudomonas putida KT2440. Because the fetched GOA file has no annotations, this first pass adds only the conservative outer-membrane cellular-component inference and leaves receptor specificity unresolved.",
        "domain": "TPR-like_helical_dom_sf.",
        "reviews": {},
        "core": [
            {
                "description": "Predicted bacteriophage N4 receptor outer-membrane subunit with unresolved receptor specificity.",
                "locations": [TERM["GO:0019867"]],
            }
        ],
        "new_annotations": [
            (
                "GO:0019867",
                "located_in",
                "PP_3449 should be represented as an outer-membrane component candidate.",
                "UniProt names PP_3449 as a bacteriophage N4 receptor outer-membrane subunit; no GOA row was present in the downloaded file.",
                None,
                None,
            )
        ],
        "question": "Is PP_3449 a functional phage receptor component in KT2440, and if so what partner subunits or phage specificity does it have?",
        "experiment": "Test PP_3449 deletion and complementation for sensitivity to N4-like phage exposure and for outer-membrane localization of tagged protein.",
    },
    "PP_4291": {
        "accession": "Q88F09",
        "symbol": "PP_4291",
        "description": "PP_4291 encodes a Tsx-like nucleoside-specific outer-membrane channel protein in Pseudomonas putida KT2440. The current evidence supports a channel/porin molecular function at the outer membrane, while the physiological substrate scope and relation to nucleoside uptake remain to be tested.",
        "domain": "Channel_Tsx",
        "reviews": {
            "GO:0009279": (
                "Cell outer membrane localization is supported by Tsx-like channel domains.",
                "ACCEPT",
                "The protein is named as a nucleoside-specific outer-membrane channel and carries Tsx-like channel domains.",
                None,
                "Channel_Tsx",
                "nucleoside-specific channel-forming outer",
                None,
            ),
        },
        "core": [
            {
                "description": "Tsx-like outer-membrane channel/porin candidate for nucleoside passage.",
                "molecular_function": TERM["GO:0015288"],
                "locations": [TERM["GO:0009279"]],
            }
        ],
        "new_annotations": [
            (
                "GO:0015288",
                "enables",
                "PP_4291 should be represented with porin activity as a conservative channel-function annotation.",
                "The UniProt RecName and Tsx-like channel domains support channel-forming outer-membrane activity, but do not by themselves establish an in vivo nucleoside-transport process.",
                "Channel_Tsx",
                "nucleoside-specific channel-forming outer",
            )
        ],
        "question": "What nucleosides or related compounds pass through PP_4291 in vivo?",
        "experiment": "Measure uptake or growth rescue on defined nucleosides in PP_4291 deletion, PP_4293 deletion, and double deletion strains.",
    },
    "PP_4293": {
        "accession": "Q88F07",
        "symbol": "PP_4293",
        "description": "PP_4293 encodes a Tsx-like nucleoside-specific outer-membrane channel protein in Pseudomonas putida KT2440. It is provisionally curated as a porin/channel at the outer membrane, with physiological substrate specificity unresolved.",
        "domain": "Channel_Tsx",
        "reviews": {
            "GO:0009279": (
                "Cell outer membrane localization is supported by Tsx-like channel domains.",
                "ACCEPT",
                "The protein is named as a nucleoside-specific outer-membrane channel and carries Tsx-like channel domains.",
                None,
                "Channel_Tsx",
                "nucleoside-specific channel-forming outer",
                None,
            ),
        },
        "core": [
            {
                "description": "Tsx-like outer-membrane channel/porin candidate for nucleoside passage.",
                "molecular_function": TERM["GO:0015288"],
                "locations": [TERM["GO:0009279"]],
            }
        ],
        "new_annotations": [
            (
                "GO:0015288",
                "enables",
                "PP_4293 should be represented with porin activity as a conservative channel-function annotation.",
                "The UniProt RecName and Tsx-like channel domains support channel-forming outer-membrane activity, but do not by themselves establish an in vivo nucleoside-transport process.",
                "Channel_Tsx",
                "nucleoside-specific channel-forming outer",
            )
        ],
        "question": "Does PP_4293 have substrate specificity distinct from the adjacent Tsx-like PP_4291 protein?",
        "experiment": "Compare PP_4291, PP_4293, and double deletion strains for growth and uptake phenotypes on individual nucleosides and nucleoside analogs.",
    },
}


def apply_reviews(gene: str, cfg: dict) -> None:
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    data["gene_symbol"] = cfg["symbol"]
    data["status"] = "DRAFT"
    data["description"] = cfg["description"]
    data["references"] = reference_list(data.get("references") or [], gene, cfg["accession"])

    configured_new_terms = {term_id for term_id, *_ in cfg.get("new_annotations", [])}
    if configured_new_terms:
        data["existing_annotations"] = [
            annotation
            for annotation in (data.get("existing_annotations") or [])
            if not (
                annotation.get("term", {}).get("id") in configured_new_terms
                and annotation.get("review", {}).get("action") == "NEW"
            )
        ]

    seen_terms = set()
    for annotation in data.get("existing_annotations") or []:
        term_id = annotation["term"]["id"]
        seen_terms.add(term_id)
        if term_id not in cfg["reviews"]:
            raise ValueError(f"No review configured for {gene} {term_id}")
        summary, action, reason, support_go, support_domain, support_similarity, replacements = cfg["reviews"][term_id]
        annotation["review"] = review(
            gene,
            term_id,
            summary,
            action,
            reason,
            support_go=support_go,
            support_domain=support_domain,
            support_similarity=support_similarity,
            replacements=replacements,
        )

    missing_reviews = set(cfg["reviews"]) - seen_terms
    if missing_reviews:
        raise ValueError(f"Configured reviews not found in {gene}: {sorted(missing_reviews)}")

    for term_id, qualifier, summary, reason, support_domain, support_similarity in cfg.get("new_annotations", []):
        data.setdefault("existing_annotations", []).append(
            new_annotation(
                gene,
                term_id,
                qualifier,
                summary,
                reason,
                support_domain=support_domain,
                support_similarity=support_similarity,
            )
        )

    core_functions = []
    for core in cfg["core"]:
        core = dict(core)
        if "molecular_function" in core:
            support_go = core["molecular_function"]["id"]
        else:
            support_go = core.get("locations", [{}])[0].get("id")
        core["supported_by"] = common_support(
            gene,
            go_term=support_go,
            domain=cfg.get("domain"),
            similarity="nucleoside-specific channel-forming outer" if gene in {"PP_4291", "PP_4293"} else None,
        )
        core_functions.append(core)
    data["core_functions"] = core_functions
    data["proposed_new_terms"] = []
    data["suggested_questions"] = [{"question": cfg["question"]}]
    data["suggested_experiments"] = [
        {"description": cfg["experiment"], "experiment_type": "targeted envelope phenotype and localization assay"}
    ]

    path.write_text(yaml.safe_dump(data, sort_keys=False, width=120), encoding="utf-8")


def write_notes(gene: str, cfg: dict) -> None:
    uniprot = GENE_ROOT / gene / f"{gene}-uniprot.txt"
    asta = GENE_ROOT / gene / f"{gene}-deep-research-asta.md"
    product_line = first_line(uniprot, "DE   ")
    domain_line = first_line(uniprot, cfg["domain"])
    asta_product = first_line(asta, "- **Protein Description:**")
    note = [
        f"# {gene} notes",
        "",
        "2026-07-10: First-pass outer-membrane barrel/channel/autotransporter boundary curation.",
        cfg["description"],
        "",
        f"Primary provenance: UniProt product/domain evidence [{file_id(gene, 'uniprot.txt')} \"{product_line}\"; "
        f"{file_id(gene, 'uniprot.txt')} \"{domain_line}\"]. Asta retrieval mainly confirmed the same metadata-level "
        f"identity [{file_id(gene, 'deep-research-asta.md')} \"{asta_product}\"].",
        "",
        "Decision: " + cfg["core"][0]["description"],
    ]
    if gene in {"PP_4291", "PP_4293"}:
        similarity_line = first_line(uniprot, "nucleoside-specific channel-forming outer")
        note.extend(
            [
                "",
                f"Tsx-specific note: added GO:0015288 porin activity from product/domain support, but did not add a nucleoside-transport process term because the available evidence does not establish the in vivo substrate or pathway role [{file_id(gene, 'uniprot.txt')} \"{similarity_line}\"].",
            ]
        )
    if gene == "PP_3449":
        note.extend(
            [
                "",
                "GOA note: the downloaded GOA file had no annotation rows, so this pass adds only the outer-membrane cellular-component candidate.",
            ]
        )
    (GENE_ROOT / gene / f"{gene}-notes.md").write_text("\n".join(note) + "\n", encoding="utf-8")


def main() -> None:
    for gene, cfg in GENES.items():
        apply_reviews(gene, cfg)
        write_notes(gene, cfg)
        print(f"Curated {gene}")


if __name__ == "__main__":
    main()
