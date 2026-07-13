#!/usr/bin/env python3
"""First-pass curate PSEPK named outer-membrane/lipoprotein-family candidates."""

from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes" / "PSEPK"


TERM = {
    "GO:0006950": {"id": "GO:0006950", "label": "response to stress"},
    "GO:0008253": {"id": "GO:0008253", "label": "5'-nucleotidase activity"},
    "GO:0008289": {"id": "GO:0008289", "label": "lipid binding"},
    "GO:0009166": {"id": "GO:0009166", "label": "nucleotide catabolic process"},
    "GO:0009279": {"id": "GO:0009279", "label": "cell outer membrane"},
    "GO:0016020": {"id": "GO:0016020", "label": "membrane"},
    "GO:0016787": {"id": "GO:0016787", "label": "hydrolase activity"},
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
    markers: tuple[str, ...] = (),
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
    for marker in markers:
        data.append(support(file_id(gene, "uniprot.txt"), first_line(uniprot, marker)))
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
    markers: tuple[str, ...] = (),
    replacements: list[str] | None = None,
) -> dict:
    obj = {
        "summary": summary,
        "action": action,
        "reason": reason,
        "supported_by": common_support(gene, go_term=term_id, markers=markers),
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
    markers: tuple[str, ...] = (),
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
            "supported_by": common_support(gene, markers=markers),
        },
    }


GENES = {
    "uxpA": {
        "accession": "Q88P09",
        "symbol": "uxpA",
        "description": "uxpA (PP_1044) encodes a lipoprotein with 5'-nucleotidase C-terminal and metallo-dependent phosphatase-like domains in Pseudomonas putida KT2440. The available evidence supports a nucleotide-catabolic hydrolase context, best represented as candidate 5'-nucleotidase activity, while envelope localization remains unresolved beyond lipoprotein metadata.",
        "markers": ("5'-Nucleotdase_C_sf.", "Metallo-depent_PP-like."),
        "reviews": {
            "GO:0009166": (
                "Nucleotide catabolic process is appropriate broad process context for a UxpA/5'-nucleotidase-family lipoprotein.",
                "ACCEPT",
                "The InterPro 5'-nucleotidase C-terminal signature supports nucleotide catabolism as a first-pass process annotation.",
                ("5'-Nucleotdase_C_sf.",),
                None,
            ),
            "GO:0016787": (
                "Hydrolase activity is correct but too broad for the available domain evidence.",
                "MODIFY",
                "The more informative supported molecular function is 5'-nucleotidase activity.",
                ("5'-Nucleotdase_C_sf.", "Metallo-depent_PP-like."),
                ["GO:0008253"],
            ),
        },
        "core": [
            {
                "description": "Candidate lipoprotein 5'-nucleotidase/nucleotide-catabolic hydrolase.",
                "molecular_function": TERM["GO:0008253"],
                "directly_involved_in": [TERM["GO:0009166"]],
            }
        ],
        "new_annotations": [
            (
                "GO:0008253",
                "enables",
                "uxpA should be represented with 5'-nucleotidase activity rather than only broad hydrolase activity.",
                "The UxpA product name and 5'-nucleotidase/metallo-phosphatase domain architecture support a specific nucleotidase-family molecular function.",
                ("5'-Nucleotdase_C_sf.", "Metallo-depent_PP-like."),
            )
        ],
        "question": "What nucleotide substrates does UxpA hydrolyze in the KT2440 envelope or periplasmic space?",
        "experiment": "Assay purified UxpA against 5'-nucleotides and compare extracellular/periplasmic nucleotide utilization phenotypes in a uxpA deletion strain.",
    },
    "slyB": {
        "accession": "Q88NS3",
        "symbol": "slyB",
        "description": "slyB (PP_1131) encodes a SlyB-family outer-membrane lipoprotein in Pseudomonas putida KT2440. Current evidence supports outer-membrane localization and surface-antigen/lipoprotein family context, but not a specific pathway-level molecular function.",
        "markers": ("Bact_OM_lipoprot/Surf_antigen.", "SUBCELLULAR LOCATION"),
        "reviews": {
            "GO:0009279": (
                "Cell outer membrane localization is directly supported.",
                "ACCEPT",
                "UniProt subcellular-location mapping and SlyB/surface-antigen-family domains support cell outer membrane localization.",
                ("Bact_OM_lipoprot/Surf_antigen.",),
                None,
            ),
            "GO:0019867": (
                "Outer membrane localization is also supported by the glycine-zipper/two-transmembrane-domain inference.",
                "ACCEPT",
                "The InterPro-derived outer-membrane annotation agrees with the specific UniProt cell outer membrane localization.",
                ("Gly_zipper_2TM_dom.",),
                None,
            ),
        },
        "core": [
            {
                "description": "SlyB-family outer-membrane lipoprotein with unresolved surface/envelope function.",
                "locations": [TERM["GO:0009279"]],
            }
        ],
        "question": "Does SlyB contribute to outer-membrane integrity, surface antigenicity, or stress adaptation in KT2440?",
        "experiment": "Assay slyB deletion strains for outer-membrane permeability, envelope-stress sensitivity, and surface protein profile changes.",
    },
    "oprI": {
        "accession": "Q88KG8",
        "symbol": "oprI",
        "description": "oprI (PP_2322) encodes a major OprI-family outer-membrane lipoprotein in Pseudomonas putida KT2440. The current first pass supports outer-membrane lipoprotein context but does not assign a specific molecular activity.",
        "markers": ("Oprl.", "KW   Lipoprotein"),
        "reviews": {},
        "core": [
            {
                "description": "Major OprI-family outer-membrane lipoprotein with unresolved molecular function.",
                "locations": [TERM["GO:0009279"]],
            }
        ],
        "new_annotations": [
            (
                "GO:0009279",
                "located_in",
                "oprI should be represented as a cell outer membrane lipoprotein candidate.",
                "The UniProt product name identifies oprI as a major outer membrane lipoprotein and the entry carries OprI-family/domain evidence.",
                ("Oprl.", "KW   Lipoprotein"),
            )
        ],
        "question": "What envelope phenotype or surface-structure role is associated with the major OprI-family lipoprotein in KT2440?",
        "experiment": "Compare outer-membrane protein profiles and envelope-stress phenotypes in oprI deletion and complemented strains.",
    },
    "PP_3236": {
        "accession": "Q88HW7",
        "symbol": "PP_3236",
        "description": "PP_3236 encodes an OprI-named lipoprotein paralog in Pseudomonas putida KT2440. Because the fetched GOA file has no annotations and UniProt lacks domain signatures beyond lipoprotein/coiled-coil metadata, this pass records only conservative membrane lipoprotein context.",
        "markers": ("KW   Lipoprotein", "KW   Signal"),
        "reviews": {},
        "core": [
            {
                "description": "OprI-named membrane lipoprotein paralog with unresolved localization specificity and function.",
                "locations": [TERM["GO:0016020"]],
            }
        ],
        "new_annotations": [
            (
                "GO:0016020",
                "located_in",
                "PP_3236 should be represented as a membrane lipoprotein candidate.",
                "The UniProt product name and lipoprotein/signal metadata support membrane association, but not a sharper outer-membrane claim in this first pass.",
                ("KW   Lipoprotein", "KW   Signal"),
            )
        ],
        "question": "Is PP_3236 an outer-membrane OprI-like lipoprotein, and is it redundant with oprI/PP_2322?",
        "experiment": "Localize tagged PP_3236 and compare single and double OprI-paralog mutants for outer-membrane protein profiles and envelope phenotypes.",
    },
    "yaiW": {
        "accession": "Q88GB9",
        "symbol": "yaiW",
        "description": "yaiW (PP_3805) encodes a DUF1615 lipoprotein annotated as required for swarming in Pseudomonas putida KT2440. The current metadata supports a membrane lipoprotein and swarming-associated candidate, but does not establish the molecular mechanism or a GO biological-process annotation for motility.",
        "markers": ("DUF1615.", "KW   Lipoprotein"),
        "reviews": {},
        "core": [
            {
                "description": "DUF1615 membrane lipoprotein candidate associated by product name with swarming.",
                "locations": [TERM["GO:0016020"]],
            }
        ],
        "new_annotations": [
            (
                "GO:0016020",
                "located_in",
                "yaiW should be represented as a membrane lipoprotein candidate.",
                "The UniProt product name and lipoprotein keyword support membrane association, but the swarming product name is not enough to assign a process-level motility GO term.",
                ("DUF1615.", "KW   Lipoprotein"),
            )
        ],
        "question": "Does yaiW affect swarming in KT2440, and if so through envelope mechanics, surface wetting, or another mechanism?",
        "experiment": "Compare swarming, swimming, biofilm, and envelope-stress phenotypes for yaiW deletion and complemented strains.",
    },
    "PP_4032": {
        "accession": "Q88FQ5",
        "symbol": "PP_4032",
        "description": "PP_4032 encodes an outer-membrane lipoprotein Blc/lipocalin-family protein in Pseudomonas putida KT2440. The UniProt/PIRNR evidence supports lipid binding, likely lysophospholipid preference, and cell outer membrane localization, while the broad stress-response annotation is retained as non-core context.",
        "markers": ("Lipocalin_Blc-like_dom.", "KW   Lipid-binding"),
        "reviews": {
            "GO:0006950": (
                "Response to stress is plausible family-level context but is not the core annotation.",
                "KEEP_AS_NON_CORE",
                "The Blc family text links lipid storage or transport to membrane maintenance under stressful conditions, but the actionable molecular function is lipid binding.",
                ("FUNCTION: Involved", "Lipocalin_Blc-like_dom."),
                None,
            ),
            "GO:0008289": (
                "Lipid binding is the core supported molecular function.",
                "ACCEPT",
                "The Blc/lipocalin family assignment and UniProt lipid-binding keyword support lipid binding.",
                ("KW   Lipid-binding", "Lipocalin_Blc-like_dom."),
                None,
            ),
            "GO:0009279": (
                "Cell outer membrane localization is supported.",
                "ACCEPT",
                "UniProt places this Blc lipoprotein at the cell outer membrane.",
                ("SUBCELLULAR LOCATION", "Lipocalin_Blc-like_dom."),
                None,
            ),
        },
        "core": [
            {
                "description": "Outer-membrane Blc/lipocalin-family lipoprotein inferred to bind lipids.",
                "molecular_function": TERM["GO:0008289"],
                "locations": [TERM["GO:0009279"]],
            }
        ],
        "question": "Which lysophospholipids or other lipids does PP_4032 bind in KT2440, and under which envelope-stress conditions is it relevant?",
        "experiment": "Measure ligand binding for purified PP_4032 and test deletion phenotypes under osmotic and membrane-stress conditions.",
    },
    "PP_4855": {
        "accession": "Q88DH0",
        "symbol": "PP_4855",
        "description": "PP_4855 encodes an OsmE/BamE-domain lipoprotein in Pseudomonas putida KT2440. The first-pass evidence supports outer-membrane localization and osmotic/envelope lipoprotein context, but not a defined Bam-complex role or molecular activity.",
        "markers": ("BamE_dom.", "KW   Lipoprotein"),
        "reviews": {
            "GO:0019867": (
                "Outer membrane localization is supported by the BamE-domain InterPro inference.",
                "ACCEPT",
                "The GOA row is based on InterPro IPR007450, and UniProt records BamE-like/BamE-domain signatures.",
                ("BamE_dom.",),
                None,
            ),
        },
        "core": [
            {
                "description": "OsmE/BamE-domain outer-membrane lipoprotein candidate with unresolved specific envelope role.",
                "locations": [TERM["GO:0019867"]],
            }
        ],
        "question": "Is PP_4855 a BamE-like outer-membrane assembly factor, an osmotic-stress lipoprotein, or both in KT2440?",
        "experiment": "Localize PP_4855 and test deletion effects on outer-membrane protein assembly and osmotic-stress fitness.",
    },
    "PP_5037": {
        "accession": "Q88CZ2",
        "symbol": "PP_5037",
        "description": "PP_5037 encodes an outer-membrane lipoprotein Blc/lipocalin-family protein in Pseudomonas putida KT2440. As for PP_4032, the strongest current annotation is lipid binding at the cell outer membrane; stress response is kept as non-core family context.",
        "markers": ("Lipocalin_Blc-like_dom.", "KW   Lipid-binding"),
        "reviews": {
            "GO:0006950": (
                "Response to stress is plausible family-level context but is not the core annotation.",
                "KEEP_AS_NON_CORE",
                "The Blc family text links lipid storage or transport to membrane maintenance under stressful conditions, but the actionable molecular function is lipid binding.",
                ("FUNCTION: Involved", "Lipocalin_Blc-like_dom."),
                None,
            ),
            "GO:0008289": (
                "Lipid binding is the core supported molecular function.",
                "ACCEPT",
                "The Blc/lipocalin family assignment and UniProt lipid-binding keyword support lipid binding.",
                ("KW   Lipid-binding", "Lipocalin_Blc-like_dom."),
                None,
            ),
            "GO:0009279": (
                "Cell outer membrane localization is supported.",
                "ACCEPT",
                "UniProt places this Blc lipoprotein at the cell outer membrane.",
                ("SUBCELLULAR LOCATION", "Lipocalin_Blc-like_dom."),
                None,
            ),
        },
        "core": [
            {
                "description": "Outer-membrane Blc/lipocalin-family lipoprotein inferred to bind lipids.",
                "molecular_function": TERM["GO:0008289"],
                "locations": [TERM["GO:0009279"]],
            }
        ],
        "question": "Does PP_5037 bind the same lipid ligands as PP_4032, or has the Blc paralog pair diverged in substrate or condition specificity?",
        "experiment": "Compare ligand binding and stress phenotypes for PP_4032, PP_5037, and double deletion strains.",
    },
    "PP_5226": {
        "accession": "Q88CF5",
        "symbol": "PP_5226",
        "description": "PP_5226 encodes an Lppl/LptM-conserved-family lipoprotein in Pseudomonas putida KT2440. The available evidence supports cell outer membrane localization, while the specific envelope function remains unresolved.",
        "markers": ("LptM_cons.", "SUBCELLULAR LOCATION"),
        "reviews": {
            "GO:0009279": (
                "Cell outer membrane localization is supported.",
                "ACCEPT",
                "UniProt subcellular-location mapping and the LptM-conserved-family domain support cell outer membrane localization.",
                ("LptM_cons.",),
                None,
            ),
        },
        "core": [
            {
                "description": "LptM-conserved-family outer-membrane lipoprotein with unresolved specific envelope function.",
                "locations": [TERM["GO:0009279"]],
            }
        ],
        "question": "What envelope pathway or partner proteins involve PP_5226/LptM-family lipoprotein in KT2440?",
        "experiment": "Localize PP_5226 and test deletion phenotypes for LPS transport stress, outer-membrane integrity, and growth under envelope stress.",
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
        summary, action, reason, markers, replacements = cfg["reviews"][term_id]
        annotation["review"] = review(
            gene,
            term_id,
            summary,
            action,
            reason,
            markers=markers,
            replacements=replacements,
        )

    missing_reviews = set(cfg["reviews"]) - seen_terms
    if missing_reviews:
        raise ValueError(f"Configured reviews not found in {gene}: {sorted(missing_reviews)}")

    for term_id, qualifier, summary, reason, markers in cfg.get("new_annotations", []):
        data.setdefault("existing_annotations", []).append(
            new_annotation(gene, term_id, qualifier, summary, reason, markers=markers)
        )

    core_functions = []
    for core in cfg["core"]:
        core = dict(core)
        if "molecular_function" in core:
            support_go = core["molecular_function"]["id"]
        elif "locations" in core:
            support_go = core["locations"][0]["id"]
        else:
            support_go = None
        core["supported_by"] = common_support(gene, go_term=support_go, markers=cfg["markers"])
        core_functions.append(core)
    data["core_functions"] = core_functions
    data["proposed_new_terms"] = []
    data["suggested_questions"] = [{"question": cfg["question"]}]
    data["suggested_experiments"] = [
        {"description": cfg["experiment"], "experiment_type": "targeted envelope phenotype, localization, and biochemical assay"}
    ]

    path.write_text(yaml.safe_dump(data, sort_keys=False, width=120), encoding="utf-8")


def write_notes(gene: str, cfg: dict) -> None:
    uniprot = GENE_ROOT / gene / f"{gene}-uniprot.txt"
    asta = GENE_ROOT / gene / f"{gene}-deep-research-asta.md"
    product_line = first_line(uniprot, "DE   ")
    marker_lines = [first_line(uniprot, marker) for marker in cfg["markers"][:2]]
    asta_product = first_line(asta, "- **Protein Description:**")
    provenance = "; ".join(f'{file_id(gene, "uniprot.txt")} "{line}"' for line in [product_line, *marker_lines])
    note = [
        f"# {gene} notes",
        "",
        "2026-07-10: First-pass named lipoprotein-family curation.",
        cfg["description"],
        "",
        f"Primary provenance: UniProt product/domain/keyword evidence [{provenance}]. Asta retrieval mainly confirmed the same metadata-level identity [{file_id(gene, 'deep-research-asta.md')} \"{asta_product}\"].",
        "",
        "Decision: " + cfg["core"][0]["description"],
    ]
    if gene in {"PP_4032", "PP_5037"}:
        note.extend(
            [
                "",
                "Blc note: lipid binding is treated as core; response to stress is retained as non-core family context because the evidence describes membrane maintenance under stressful conditions rather than a specific stress-response pathway.",
            ]
        )
    if gene in {"PP_3236", "yaiW"}:
        note.extend(
            [
                "",
                "Localization caution: this pass adds only broad membrane context, not a cell-outer-membrane annotation, because the local evidence is lipoprotein metadata without a direct subcellular-location line.",
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
