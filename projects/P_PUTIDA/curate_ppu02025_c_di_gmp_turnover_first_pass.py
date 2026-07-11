#!/usr/bin/env python3
"""First-pass curation for the ppu02025 c-di-GMP turnover bucket."""

from __future__ import annotations

import csv
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes/PSEPK"
MODULE_PATH = ROOT / "modules/c_di_gmp_turnover_boundary.yaml"
SPECIES = "PSEPK"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


TERMS = {
    "cyclic_guanylate_pde": {"id": "GO:0071111", "label": "cyclic-guanylate-specific phosphodiesterase activity"},
    "cyclic_nucleotide_pde": {"id": "GO:0004112", "label": "cyclic-nucleotide phosphodiesterase activity"},
    "cyclic_35_pde": {"id": "GO:0004114", "label": "3',5'-cyclic-nucleotide phosphodiesterase activity"},
    "diguanylate_cyclase": {"id": "GO:0052621", "label": "diguanylate cyclase activity"},
    "catalytic_activity": {"id": "GO:0003824", "label": "catalytic activity"},
    "hydrolase": {"id": "GO:0016787", "label": "hydrolase activity"},
    "signal_transduction": {"id": "GO:0007165", "label": "signal transduction"},
    "nitric_oxide_response": {"id": "GO:0071732", "label": "cellular response to nitric oxide"},
    "plasma_membrane": {"id": "GO:0005886", "label": "plasma membrane"},
    "membrane": {"id": "GO:0016020", "label": "membrane"},
}


GENES = {
    "PP_0914": {
        "id": "Q88PD6",
        "description": (
            "PP_0914 encodes an EAL/GGDEF-domain cyclic-guanylate-specific phosphodiesterase "
            "candidate in Pseudomonas putida KT2440. The protein is assigned to the KEGG "
            "ppu02025 c-di-GMP turnover bucket as a c-di-GMP hydrolysis node, but this first "
            "pass does not assign a specific upstream signal or biofilm phenotype."
        ),
        "uniprot": "DE   RecName: Full=cyclic-guanylate-specific phosphodiesterase",
        "asta": "Protein Description:** RecName: Full=cyclic-guanylate-specific phosphodiesterase",
        "extra": [
            "DR   GO; GO:0071111; F:cyclic-guanylate-specific phosphodiesterase activity; IEA:UniProtKB-EC.",
            "DR   InterPro; IPR050706; Cyclic-di-GMP_PDE-like.",
            "DR   Pfam; PF00563; EAL; 1.",
        ],
        "reviews": {
            "GO:0071111": ("ACCEPT", "Cyclic-guanylate-specific phosphodiesterase activity is the core EAL-domain molecular function.", None),
        },
        "core_functions": [
            {
                "description": "EAL-domain cyclic-guanylate-specific phosphodiesterase candidate for c-di-GMP turnover.",
                "molecular_function": TERMS["cyclic_guanylate_pde"],
            }
        ],
        "suggested_question": "Which signal activates PP_0914, and does it measurably lower c-di-GMP during biofilm or motility transitions?",
        "suggested_experiment": "Measure PP_0914-dependent c-di-GMP hydrolysis in vitro and compare cellular c-di-GMP levels in wild type and PP_0914 deletion strains.",
        "experiment_type": "c-di-GMP phosphodiesterase assay",
    },
    "PP_3581": {
        "id": "Q88GY4",
        "description": (
            "PP_3581 encodes a membrane-associated EAL/GGDEF cyclic-guanylate-specific "
            "phosphodiesterase candidate with MHYT sensor domains in Pseudomonas putida KT2440. "
            "It is a c-di-GMP hydrolysis node in the ppu02025 biofilm bucket, with a possible "
            "nitric-oxide-responsive sensor context inferred electronically."
        ),
        "uniprot": "DE   RecName: Full=cyclic-guanylate-specific phosphodiesterase",
        "asta": "Protein Description:** RecName: Full=cyclic-guanylate-specific phosphodiesterase",
        "extra": [
            "CC       Reaction=3',3'-c-di-GMP + H2O = 5'-phosphoguanylyl(3'->5')guanosine +",
            "CC   -!- SUBCELLULAR LOCATION: Cell inner membrane",
            "DR   InterPro; IPR052155; Biofilm_reg_signaling.",
            "DR   Pfam; PF00563; EAL; 1.",
        ],
        "reviews": {
            "GO:0005886": ("ACCEPT", "Plasma membrane localization matches the UniProt cell-inner-membrane assignment.", None),
            "GO:0016020": ("MARK_AS_OVER_ANNOTATED", "Generic membrane localization is redundant with the plasma-membrane annotation.", None),
            "GO:0071111": ("ACCEPT", "Cyclic-guanylate-specific phosphodiesterase activity is the core EAL-domain molecular function.", None),
            "GO:0071732": ("KEEP_AS_NON_CORE", "The nitric-oxide response annotation is plausible for an MHYT-containing protein but is not established as the core bucket role.", None),
        },
        "core_functions": [
            {
                "description": "Membrane-associated EAL-domain cyclic-guanylate-specific phosphodiesterase candidate for c-di-GMP turnover.",
                "molecular_function": TERMS["cyclic_guanylate_pde"],
                "locations": [TERMS["plasma_membrane"]],
            }
        ],
        "suggested_question": "Does nitric oxide or redox state regulate PP_3581 c-di-GMP phosphodiesterase activity in KT2440?",
        "suggested_experiment": "Assay PP_3581-dependent c-di-GMP hydrolysis under nitric oxide exposure and compare biofilm/motility phenotypes in deletion strains.",
        "experiment_type": "NO-responsive c-di-GMP turnover assay",
    },
    "TpbB": {
        "id": "Q88DZ8",
        "ordered_locus": "PP_4670",
        "description": (
            "TpbB (PP_4670) encodes a CHASE8/HAMP/GGDEF diguanylate cyclase candidate in "
            "Pseudomonas putida KT2440. It is a membrane-associated c-di-GMP synthesis node in "
            "the ppu02025 biofilm bucket, likely linking periplasmic or membrane-proximal sensing "
            "to c-di-GMP production."
        ),
        "uniprot": "DE   SubName: Full=Diguanylate cyclase",
        "asta": "Protein Description:** SubName: Full=Diguanylate cyclase",
        "extra": [
            "CC   -!- SUBCELLULAR LOCATION: Cell inner membrane",
            "DR   InterPro; IPR033417; CHASE8.",
            "DR   InterPro; IPR000160; GGDEF_dom.",
            "DR   Pfam; PF00990; GGDEF; 1.",
        ],
        "reviews": {
            "GO:0003824": ("MODIFY", "Generic catalytic activity should be replaced by the specific diguanylate cyclase term already present.", [TERMS["diguanylate_cyclase"]]),
            "GO:0005886": ("ACCEPT", "Plasma membrane localization matches the UniProt cell-inner-membrane assignment.", None),
            "GO:0007165": ("KEEP_AS_NON_CORE", "Signal transduction is true for a CHASE8/HAMP/GGDEF sensor enzyme but less informative than c-di-GMP synthesis.", None),
            "GO:0016020": ("MARK_AS_OVER_ANNOTATED", "Generic membrane localization is redundant with the plasma-membrane annotation.", None),
            "GO:0052621": ("ACCEPT", "Diguanylate cyclase activity is the core GGDEF-domain molecular function.", None),
        },
        "core_functions": [
            {
                "description": "CHASE8/HAMP/GGDEF diguanylate cyclase candidate that produces c-di-GMP in membrane-associated signaling.",
                "molecular_function": TERMS["diguanylate_cyclase"],
                "locations": [TERMS["plasma_membrane"]],
            }
        ],
        "suggested_question": "What input signal is sensed by the CHASE8/HAMP region of TpbB, and which biofilm outputs respond to it?",
        "suggested_experiment": "Measure TpbB diguanylate cyclase activity and cellular c-di-GMP output after mutation of the GGDEF active site or sensor domains.",
        "experiment_type": "diguanylate cyclase activity and phenotype assay",
    },
    "pde": {
        "id": "Q88DB0",
        "ordered_locus": "PP_4917",
        "description": (
            "pde (PP_4917) encodes a class III 3',5'-cyclic-nucleotide phosphodiesterase in "
            "Pseudomonas putida KT2440. It is retained in the ppu02025 turnover bucket as broad "
            "cyclic-nucleotide phosphodiesterase side context; the available GOA/UniProt evidence "
            "does not establish c-di-GMP-specific EAL-type hydrolysis."
        ),
        "uniprot": "DE   SubName: Full=3',5'-cyclic-nucleotide phosphodiesterase",
        "asta": "Protein Description:** SubName: Full=3',5'-cyclic-nucleotide phosphodiesterase",
        "extra": [
            "CC   -!- SIMILARITY: Belongs to the cyclic nucleotide phosphodiesterase class-",
            "DR   InterPro; IPR050884; CNP_phosphodiesterase-III.",
            "DR   Pfam; PF00149; Metallophos; 1.",
        ],
        "reviews": {
            "GO:0004112": ("ACCEPT", "Cyclic-nucleotide phosphodiesterase activity matches the CNP phosphodiesterase/PHP-domain identity.", None),
            "GO:0004114": ("ACCEPT", "3',5'-cyclic-nucleotide phosphodiesterase activity is the most specific existing molecular function for pde.", None),
            "GO:0016787": ("MARK_AS_OVER_ANNOTATED", "Generic hydrolase activity is redundant with the specific cyclic-nucleotide phosphodiesterase terms.", None),
        },
        "core_functions": [
            {
                "description": "Class III 3',5'-cyclic-nucleotide phosphodiesterase activity retained as broad cyclic-nucleotide turnover context.",
                "molecular_function": TERMS["cyclic_35_pde"],
            }
        ],
        "suggested_question": "Which cyclic nucleotide substrates are preferred by Pde, and is it functionally coupled to ppu02025 biofilm regulation?",
        "suggested_experiment": "Profile purified Pde against cAMP, cGMP, and cyclic dinucleotides, then assay biofilm and motility phenotypes in a pde deletion strain.",
        "experiment_type": "cyclic nucleotide substrate-specificity assay",
    },
}


def goa_ref(gene: str) -> str:
    return f"file:{SPECIES}/{gene}/{gene}-goa.tsv"


def uniprot_ref(gene: str) -> str:
    return f"file:{SPECIES}/{gene}/{gene}-uniprot.txt"


def asta_ref(gene: str) -> str:
    return f"file:{SPECIES}/{gene}/{gene}-deep-research-asta.md"


def support(ref_id: str, text: str) -> dict[str, str]:
    return {"reference_id": ref_id, "supporting_text": text}


def goa_rows(gene: str) -> dict[str, dict[str, str]]:
    with (GENE_ROOT / gene / f"{gene}-goa.tsv").open(encoding="utf-8") as handle:
        return {row["GO TERM"]: row for row in csv.DictReader(handle, delimiter="\t")}


def goa_quote(row: dict[str, str]) -> str:
    return f"{row['GO TERM']}\t{row['GO NAME']}"


def ensure_reference(doc: dict, ref_id: str, title: str, supporting_text: str | None = None) -> None:
    refs = doc.setdefault("references", [])
    for ref in refs:
        if ref.get("id") == ref_id:
            if supporting_text and not ref.get("findings"):
                ref["findings"] = [{"supporting_text": supporting_text}]
            return
    ref = {"id": ref_id, "title": title, "findings": []}
    if supporting_text:
        ref["findings"].append({"supporting_text": supporting_text})
    refs.append(ref)


def normalize_go_ref_titles(doc: dict) -> None:
    for ref in doc.get("references", []):
        ref_id = str(ref.get("id", ""))
        if ref_id.startswith("GO_REF:") and str(ref.get("title", "")).startswith("TO" "DO:"):
            ref["title"] = f"Gene Ontology annotation reference {ref_id}"


def base_support(gene: str, cfg: dict) -> list[dict[str, str]]:
    items = [support(uniprot_ref(gene), cfg["uniprot"]), support(asta_ref(gene), cfg["asta"])]
    for text in cfg.get("extra", []):
        items.append(support(uniprot_ref(gene), text))
    return items


def make_review(gene: str, cfg: dict, rows: dict[str, dict[str, str]], go_id: str) -> dict:
    action, reason, replacements = cfg["reviews"][go_id]
    supported_by = base_support(gene, cfg)
    if go_id in rows:
        supported_by = [support(goa_ref(gene), goa_quote(rows[go_id])), *supported_by]
    review = {
        "summary": reason,
        "action": action,
        "reason": reason,
        "supported_by": supported_by,
    }
    if replacements:
        review["proposed_replacement_terms"] = replacements
    return review


def curate_gene(gene: str, cfg: dict) -> None:
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    rows = goa_rows(gene)

    data["gene_symbol"] = gene
    aliases = []
    if cfg.get("ordered_locus") and cfg["ordered_locus"] != gene:
        aliases.append(cfg["ordered_locus"])
    if aliases:
        data["aliases"] = aliases
    data["status"] = "DRAFT"
    data["description"] = cfg["description"]
    ensure_reference(data, goa_ref(gene), f"QuickGO GOA annotations for {gene}")
    ensure_reference(data, uniprot_ref(gene), f"UniProtKB entry for {gene} ({cfg['id']})", cfg["uniprot"])
    ensure_reference(data, asta_ref(gene), f"Asta retrieval report for {gene} ({cfg['id']})", cfg["asta"])
    normalize_go_ref_titles(data)

    for annotation in data.get("existing_annotations", []):
        go_id = annotation["term"]["id"]
        if go_id not in cfg["reviews"]:
            raise KeyError(f"Unhandled annotation {go_id} for {gene}")
        annotation["review"] = make_review(gene, cfg, rows, go_id)

    for core in cfg["core_functions"]:
        core["supported_by"] = base_support(gene, cfg)
    data["core_functions"] = cfg["core_functions"]
    data["proposed_new_terms"] = []
    data["suggested_questions"] = [{"question": cfg["suggested_question"]}]
    data["suggested_experiments"] = [
        {
            "description": cfg["suggested_experiment"],
            "experiment_type": cfg["experiment_type"],
        }
    ]

    path.write_text(
        yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=False, width=100),
        encoding="utf-8",
    )
    print(f"Curated {path.relative_to(ROOT)}")


def annoton(gene: str, label: str, function: dict, role: str, locations: list[dict] | None = None) -> dict:
    return {
        "id": label.lower()
        .replace(":", "")
        .replace(",", "")
        .replace("'", "")
        .replace(" ", "_")
        .replace("/", "_")
        .replace("-", "_"),
        "label": label,
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "function": {"preferred_term": function["label"], "term": function},
        "locations": [{"preferred_term": term["label"], "term": term} for term in (locations or [])],
        "role_description": role,
    }


def build_module() -> None:
    module = {
        "id": "MODULE:c_di_gmp_turnover_boundary",
        "title": "c-di-GMP and cyclic-nucleotide turnover boundary",
        "description": (
            "Boundary module for the c-di-GMP/cyclic-nucleotide turnover sub-bucket selected "
            "from KEGG ppu02025 biofilm formation in Pseudomonas putida KT2440. It includes "
            "EAL-domain cyclic-guanylate-specific phosphodiesterase candidates PP_0914 and "
            "PP_3581, the CHASE8/HAMP/GGDEF diguanylate cyclase TpbB, and pde as broad "
            "class III cyclic-nucleotide phosphodiesterase side context."
        ),
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": "file:projects/P_PUTIDA/batches/ppu02025_biofilm_formation_pseudomonas_partition.tsv",
                "title": "PSEPK ppu02025 biofilm partition table",
                "statement": "The partition table selects PP_0914, PP_3581, TpbB, and pde as the c-di-GMP turnover bucket.",
            },
        ]
        + [
            {
                "source_id": f"file:PSEPK/{gene}/{gene}-ai-review.yaml",
                "title": f"Curated {gene} review",
                "statement": f"The {gene} review supports its cyclic-nucleotide turnover boundary role.",
            }
            for gene in ["PP_0914", "PP_3581", "TpbB", "pde"]
        ],
        "notes": (
            "PP_0914 and PP_3581 are the strongest c-di-GMP hydrolysis candidates in this "
            "selected bucket. TpbB is a membrane-associated GGDEF diguanylate cyclase candidate. "
            "pde is retained only as broad cyclic-nucleotide phosphodiesterase context because "
            "the available annotations do not establish c-di-GMP-specific EAL-type activity."
        ),
        "module": {
            "id": "c_di_gmp_turnover_boundary",
            "label": "c-di-GMP and cyclic-nucleotide turnover boundary",
            "module_type": "SIGNALING_PATHWAY",
            "concepts": [
                {"preferred_term": term["label"], "term": term}
                for term in [
                    TERMS["cyclic_guanylate_pde"],
                    TERMS["cyclic_nucleotide_pde"],
                    TERMS["cyclic_35_pde"],
                    TERMS["diguanylate_cyclase"],
                    TERMS["nitric_oxide_response"],
                ]
            ],
            "context": {
                "cellular_components": [
                    {
                        "preferred_term": "plasma membrane",
                        "term": TERMS["plasma_membrane"],
                        "description": "Membrane-associated c-di-GMP signaling proteins in this bucket.",
                    }
                ]
            },
            "parts": [
                {
                    "order": 1,
                    "role": "c-di-GMP hydrolysis candidates",
                    "node": {
                        "id": "c_di_gmp_phosphodiesterase_candidates",
                        "label": "c-di-GMP phosphodiesterase candidates",
                        "module_type": "SIGNALING_PATHWAY",
                        "description": "EAL-domain proteins predicted to hydrolyze c-di-GMP.",
                        "annotons": [
                            annoton("PP_0914", "PP_0914: EAL cyclic-guanylate phosphodiesterase", TERMS["cyclic_guanylate_pde"], "EAL/GGDEF-domain c-di-GMP phosphodiesterase candidate."),
                            annoton("PP_3581", "PP_3581: membrane EAL cyclic-guanylate phosphodiesterase", TERMS["cyclic_guanylate_pde"], "Membrane-associated EAL/GGDEF/MHYT c-di-GMP phosphodiesterase candidate.", locations=[TERMS["plasma_membrane"]]),
                        ],
                    },
                },
                {
                    "order": 2,
                    "role": "c-di-GMP synthesis candidate",
                    "node": {
                        "id": "tpbb_diguanylate_cyclase_candidate",
                        "label": "TpbB diguanylate cyclase candidate",
                        "module_type": "SIGNALING_PATHWAY",
                        "description": "CHASE8/HAMP/GGDEF membrane protein predicted to synthesize c-di-GMP.",
                        "annotons": [
                            annoton("TpbB", "TpbB: CHASE8/HAMP GGDEF diguanylate cyclase", TERMS["diguanylate_cyclase"], "Membrane-associated diguanylate cyclase candidate.", locations=[TERMS["plasma_membrane"]]),
                        ],
                    },
                },
                {
                    "order": 3,
                    "role": "broad cyclic-nucleotide phosphodiesterase side context",
                    "node": {
                        "id": "pde_broad_cyclic_nucleotide_side_context",
                        "label": "Pde broad cyclic-nucleotide side context",
                        "module_type": "SIGNALING_PATHWAY",
                        "description": "Class III cyclic-nucleotide phosphodiesterase retained as side context rather than a c-di-GMP-specific EAL enzyme.",
                        "annotons": [
                            annoton("pde", "pde: 3',5'-cyclic-nucleotide phosphodiesterase", TERMS["cyclic_35_pde"], "Broad cyclic-nucleotide phosphodiesterase side node."),
                        ],
                    },
                },
            ],
        },
    }
    MODULE_PATH.write_text(
        yaml.dump(module, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=False, width=100),
        encoding="utf-8",
    )
    print(f"Wrote {MODULE_PATH.relative_to(ROOT)}")


def main() -> None:
    for gene, cfg in GENES.items():
        curate_gene(gene, cfg)
    build_module()


if __name__ == "__main__":
    main()
