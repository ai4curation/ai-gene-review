#!/usr/bin/env python3
"""First-pass curation for the PSEPK ppu01040 unsaturated-fatty-acid batch."""

from __future__ import annotations

from pathlib import Path

import yaml


def term(go_id: str, label: str) -> dict[str, str]:
    return {"id": go_id, "label": label}


def support(reference_id: str, supporting_text: str) -> dict[str, str]:
    return {"reference_id": reference_id, "supporting_text": supporting_text}


CONFIG: dict[str, dict] = {
    "tesA": {
        "id": "Q88KH2",
        "symbol": "tesA",
        "description": (
            "tesA encodes a predicted SGNH/GDSL hydrolase annotated as acyl-CoA "
            "thioesterase I/protease I/lysophospholipase L1. The best "
            "first-pass interpretation is a secreted or periplasmic lipid "
            "ester/thioester hydrolase with fatty acyl-ACP hydrolase and "
            "lysophospholipase/lipase activity, not a core unsaturated fatty "
            "acid biosynthesis enzyme."
        ),
        "reviews": {
            "GO:0004622": {
                "summary": "The lysophospholipase A1 annotation is plausible for the SGNH/GDSL hydrolase named as lysophospholipase L1, but the exact lipid substrate has not been experimentally resolved for KT2440 TesA.",
                "action": "KEEP_AS_NON_CORE",
                "reason": "Retain as lipid-hydrolase context while treating the fatty acyl-ACP hydrolase annotation as the clearer pathway-relevant molecular function.",
                "supported_by": [
                    support("file:PSEPK/tesA/tesA-uniprot.txt", "Full=Acyl-CoA thioesterase I/protease I/lysophospholipase L1"),
                    support("file:PSEPK/tesA/tesA-uniprot.txt", "DR   GO; GO:0004622; F:phosphatidylcholine lysophospholipase A1 activity; IEA:UniProtKB-EC."),
                    support("file:PSEPK/tesA/tesA-deep-research-asta.md", "- **Protein Description:** SubName: Full=Acyl-CoA thioesterase I/protease I/lysophospholipase L1 {ECO:0000313|EMBL:AAN67931.1}; EC=3.1.1.5 {ECO:0000313|EMBL:AAN67931.1}; EC=3.1.2.14 {ECO:0000313|EMBL:AAN67931.1}; EC=3.1.2.2 {ECO:0000313|EMBL:AAN67931.1};"),
                    support("file:PSEPK/tesA/tesA-goa.tsv", "GO:0004622\tphosphatidylcholine lysophospholipase A1 activity"),
                ],
            },
            "GO:0006629": {
                "summary": "Lipid metabolic process is a broad but reasonable biological-process context for a predicted lipase/thioesterase.",
                "action": "KEEP_AS_NON_CORE",
                "reason": "The term is broad process context and does not define a specific unsaturated fatty-acid biosynthesis step.",
                "supported_by": [
                    support("file:PSEPK/tesA/tesA-uniprot.txt", "DR   GO; GO:0006629; P:lipid metabolic process; IEA:InterPro."),
                    support("file:PSEPK/tesA/tesA-goa.tsv", "GO:0006629\tlipid metabolic process"),
                ],
            },
            "GO:0016297": {
                "summary": "Fatty acyl-[ACP] hydrolase activity is the most specific reviewed molecular-function assignment for TesA in this first pass.",
                "action": "ACCEPT",
                "reason": "UniProt EC mapping and the submitted product name support a fatty acyl-thioester hydrolase role, although no direct KT2440 biochemical assay was found.",
                "supported_by": [
                    support("file:PSEPK/tesA/tesA-uniprot.txt", "DR   GO; GO:0016297; F:fatty acyl-[ACP] hydrolase activity; IEA:UniProtKB-EC."),
                    support("file:PSEPK/tesA/tesA-uniprot.txt", "FT   DOMAIN          26..183"),
                    support("file:PSEPK/tesA/tesA-deep-research-asta.md", "- **Key Domains:** Ester_Hydrolysis_Enzymes. (IPR051532); Lipase_GDSL_AS. (IPR008265); SGNH_hydro. (IPR013830); SGNH_hydro_sf. (IPR036514); Lipase_GDSL_2 (PF13472)"),
                    support("file:PSEPK/tesA/tesA-goa.tsv", "GO:0016297\tfatty acyl-[ACP] hydrolase activity"),
                ],
            },
            "GO:0016298": {
                "summary": "Lipase activity is consistent with the GDSL/SGNH hydrolase domain but is less informative than the fatty acyl-ACP hydrolase assignment.",
                "action": "KEEP_AS_NON_CORE",
                "reason": "Retain as broad hydrolase/lipase context.",
                "supported_by": [
                    support("file:PSEPK/tesA/tesA-uniprot.txt", "DR   InterPro; IPR008265; Lipase_GDSL_AS."),
                    support("file:PSEPK/tesA/tesA-goa.tsv", "GO:0016298\tlipase activity"),
                ],
            },
            "GO:0016788": {
                "summary": "Hydrolase activity acting on ester bonds is true but too broad for this SGNH/GDSL hydrolase.",
                "action": "MARK_AS_OVER_ANNOTATED",
                "reason": "The more specific lipase/fatty acyl-thioester hydrolase terms are more useful for curation.",
                "supported_by": [
                    support("file:PSEPK/tesA/tesA-uniprot.txt", "DR   InterPro; IPR013830; SGNH_hydro."),
                    support("file:PSEPK/tesA/tesA-goa.tsv", "GO:0016788\thydrolase activity, acting on ester bonds"),
                ],
            },
        },
        "references": [
            ("file:PSEPK/tesA/tesA-uniprot.txt", "UniProtKB entry for tesA (Q88KH2)", "Full=Acyl-CoA thioesterase I/protease I/lysophospholipase L1"),
            ("file:PSEPK/tesA/tesA-goa.tsv", "QuickGO GOA annotations for tesA", "GO:0016297\tfatty acyl-[ACP] hydrolase activity"),
            ("file:PSEPK/tesA/tesA-deep-research-asta.md", "Asta retrieval report for tesA (Q88KH2)", "uniprot_accession: Q88KH2"),
        ],
        "core": [
            {
                "description": "Predicted SGNH/GDSL lipid thioester/ester hydrolase, best captured as fatty acyl-[ACP] hydrolase activity in this first pass.",
                "molecular_function": term("GO:0016297", "fatty acyl-[ACP] hydrolase activity"),
                "supported_by": [
                    support("file:PSEPK/tesA/tesA-uniprot.txt", "DR   GO; GO:0016297; F:fatty acyl-[ACP] hydrolase activity; IEA:UniProtKB-EC."),
                    support("file:PSEPK/tesA/tesA-uniprot.txt", "DR   InterPro; IPR008265; Lipase_GDSL_AS."),
                    support("file:PSEPK/tesA/tesA-deep-research-asta.md", "- **Key Domains:** Ester_Hydrolysis_Enzymes. (IPR051532); Lipase_GDSL_AS. (IPR008265); SGNH_hydro. (IPR013830); SGNH_hydro_sf. (IPR036514); Lipase_GDSL_2 (PF13472)"),
                ],
            }
        ],
        "questions": [
            "What are the physiological TesA substrates in KT2440: acyl-ACP, acyl-CoA, lysophospholipids, or multiple lipid ester/thioester pools?",
            "Is TesA exported to the periplasm or outer-membrane environment as predicted by the signal peptide?",
        ],
        "experiments": [
            {
                "description": "Purify mature TesA and compare hydrolysis of acyl-ACP, acyl-CoA, and lysophospholipid substrates.",
                "experiment_type": "biochemical enzyme assay",
            }
        ],
    },
    "tesB": {
        "id": "Q88DR1",
        "symbol": "tesB",
        "description": (
            "tesB encodes a predicted cytosolic Acyl-CoA thioesterase 2 "
            "with double-HotDog/C-M-P thioester hydrolase domains. Its core "
            "first-pass function is fatty acyl-CoA hydrolysis in acyl-CoA and "
            "fatty-acid turnover, not the ACP-based FabA/FabB unsaturated "
            "fatty-acid biosynthesis branch."
        ),
        "reviews": {
            "GO:0005829": {
                "summary": "Cytosol is consistent with the soluble acyl-CoA thioesterase 2 annotation.",
                "action": "KEEP_AS_NON_CORE",
                "reason": "Localization supports the enzyme assignment but is not the core molecular function.",
                "supported_by": [
                    support("file:PSEPK/tesB/tesB-uniprot.txt", "DR   GO; GO:0005829; C:cytosol; IEA:TreeGrafter."),
                    support("file:PSEPK/tesB/tesB-goa.tsv", "GO:0005829\tcytosol"),
                ],
            },
            "GO:0006637": {
                "summary": "Acyl-CoA metabolic process is appropriate for an acyl-CoA thioesterase.",
                "action": "ACCEPT",
                "reason": "TesB hydrolyzes fatty acyl-CoA to fatty acid and CoA, directly placing it in acyl-CoA metabolism.",
                "supported_by": [
                    support("file:PSEPK/tesB/tesB-uniprot.txt", "Reaction=a fatty acyl-CoA + H2O = a fatty acid + CoA + H(+);"),
                    support("file:PSEPK/tesB/tesB-uniprot.txt", "DR   GO; GO:0006637; P:acyl-CoA metabolic process; IEA:InterPro."),
                    support("file:PSEPK/tesB/tesB-goa.tsv", "GO:0006637\tacyl-CoA metabolic process"),
                ],
            },
            "GO:0009062": {
                "summary": "Fatty acid catabolic process is plausible broader context for a fatty acyl-CoA hydrolase but should not be read as a route-defining beta-oxidation assignment.",
                "action": "KEEP_AS_NON_CORE",
                "reason": "Retain as broad catabolic context while keeping the molecular function as the core annotation.",
                "supported_by": [
                    support("file:PSEPK/tesB/tesB-uniprot.txt", "DR   GO; GO:0009062; P:fatty acid catabolic process; IEA:TreeGrafter."),
                    support("file:PSEPK/tesB/tesB-goa.tsv", "GO:0009062\tfatty acid catabolic process"),
                ],
            },
            "GO:0047617": {
                "summary": "Fatty acyl-CoA hydrolase activity is the core molecular function for TesB.",
                "action": "ACCEPT",
                "reason": "The UniProt catalytic reaction, EC 3.1.2.20, InterPro domains, and GOA EC mapping all support fatty acyl-CoA thioester hydrolysis.",
                "supported_by": [
                    support("file:PSEPK/tesB/tesB-uniprot.txt", "RecName: Full=Acyl-CoA thioesterase 2"),
                    support("file:PSEPK/tesB/tesB-uniprot.txt", "DR   GO; GO:0047617; F:fatty acyl-CoA hydrolase activity; IEA:UniProtKB-EC."),
                    support("file:PSEPK/tesB/tesB-deep-research-asta.md", "- **Protein Description:** RecName: Full=Acyl-CoA thioesterase 2 {ECO:0000256|ARBA:ARBA00071120}; EC=3.1.2.20 {ECO:0000256|ARBA:ARBA00038894}; AltName: Full=Thioesterase II {ECO:0000256|ARBA:ARBA00079653};"),
                    support("file:PSEPK/tesB/tesB-goa.tsv", "GO:0047617\tfatty acyl-CoA hydrolase activity"),
                ],
            },
        },
        "references": [
            ("file:PSEPK/tesB/tesB-uniprot.txt", "UniProtKB entry for tesB (Q88DR1)", "RecName: Full=Acyl-CoA thioesterase 2"),
            ("file:PSEPK/tesB/tesB-goa.tsv", "QuickGO GOA annotations for tesB", "GO:0047617\tfatty acyl-CoA hydrolase activity"),
            ("file:PSEPK/tesB/tesB-deep-research-asta.md", "Asta retrieval report for tesB (Q88DR1)", "uniprot_accession: Q88DR1"),
        ],
        "core": [
            {
                "description": "Cytosolic fatty acyl-CoA thioester hydrolase activity in acyl-CoA turnover.",
                "molecular_function": term("GO:0047617", "fatty acyl-CoA hydrolase activity"),
                "directly_involved_in": [term("GO:0006637", "acyl-CoA metabolic process")],
                "supported_by": [
                    support("file:PSEPK/tesB/tesB-uniprot.txt", "Reaction=a fatty acyl-CoA + H2O = a fatty acid + CoA + H(+);"),
                    support("file:PSEPK/tesB/tesB-uniprot.txt", "DR   GO; GO:0047617; F:fatty acyl-CoA hydrolase activity; IEA:UniProtKB-EC."),
                    support("file:PSEPK/tesB/tesB-deep-research-asta.md", "- **Key Domains:** Acyl-CoA_hotdog. (IPR042171); Acyl_CoA_thio. (IPR003703); HotDog_dom_sf. (IPR029069); TesB_ACOT8-like_N. (IPR049449); TesB_C. (IPR025652)"),
                ],
            }
        ],
        "questions": [
            "Which fatty acyl-CoA chain lengths are preferred by KT2440 TesB, and does it act mainly in acyl-CoA pool regulation or fatty-acid catabolism?",
        ],
        "experiments": [
            {
                "description": "Measure TesB hydrolysis kinetics across short-, medium-, and long-chain acyl-CoA substrates.",
                "experiment_type": "biochemical enzyme assay",
            }
        ],
    },
    "PP_5331": {
        "id": "Q88C52",
        "symbol": "PP_5331",
        "description": (
            "PP_5331 encodes a predicted HotDog-family long-chain acyl-CoA "
            "thioester hydrolase. The first-pass function is long-chain "
            "fatty acyl-CoA hydrolysis in acyl-CoA and fatty-acid turnover; "
            "the exact substrate range and pathway context remain inferred."
        ),
        "reviews": {
            "GO:0005737": {
                "summary": "Cytoplasm is broad localization context for a predicted soluble HotDog thioesterase.",
                "action": "KEEP_AS_NON_CORE",
                "reason": "Retain as non-core localization context; cytosol is the more specific duplicated localization annotation.",
                "supported_by": [
                    support("file:PSEPK/PP_5331/PP_5331-goa.tsv", "GO:0005737\tcytoplasm"),
                ],
            },
            "GO:0005829": {
                "summary": "Cytosol is consistent with the soluble HotDog ACOT domain assignment.",
                "action": "KEEP_AS_NON_CORE",
                "reason": "Localization supports but does not define the core function.",
                "supported_by": [
                    support("file:PSEPK/PP_5331/PP_5331-uniprot.txt", "DR   GO; GO:0005829; C:cytosol; IEA:TreeGrafter."),
                    support("file:PSEPK/PP_5331/PP_5331-goa.tsv", "GO:0005829\tcytosol"),
                ],
            },
            "GO:0006637": {
                "summary": "Acyl-CoA metabolic process is appropriate for a predicted long-chain acyl-CoA thioester hydrolase.",
                "action": "ACCEPT",
                "reason": "The product name, HotDog ACOT domain, and GOA process annotation support acyl-CoA turnover.",
                "supported_by": [
                    support("file:PSEPK/PP_5331/PP_5331-uniprot.txt", "SubName: Full=Long-chain acyl-CoA thioester hydrolase"),
                    support("file:PSEPK/PP_5331/PP_5331-uniprot.txt", "DR   GO; GO:0006637; P:acyl-CoA metabolic process; IEA:TreeGrafter."),
                    support("file:PSEPK/PP_5331/PP_5331-goa.tsv", "GO:0006637\tacyl-CoA metabolic process"),
                ],
            },
            "GO:0009062": {
                "summary": "Fatty acid catabolic process is plausible broader context for long-chain acyl-CoA hydrolysis.",
                "action": "KEEP_AS_NON_CORE",
                "reason": "Retain as broad process context; no direct beta-oxidation route role is established.",
                "supported_by": [
                    support("file:PSEPK/PP_5331/PP_5331-uniprot.txt", "DR   GO; GO:0009062; P:fatty acid catabolic process; IEA:TreeGrafter."),
                    support("file:PSEPK/PP_5331/PP_5331-goa.tsv", "GO:0009062\tfatty acid catabolic process"),
                ],
            },
            "GO:0016790": {
                "summary": "Thiolester hydrolase activity is correct family-level chemistry but less specific than long-chain fatty acyl-CoA hydrolase activity.",
                "action": "MARK_AS_OVER_ANNOTATED",
                "reason": "Use the more specific long-chain fatty acyl-CoA hydrolase term as the core function.",
                "supported_by": [
                    support("file:PSEPK/PP_5331/PP_5331-uniprot.txt", "DR   InterPro; IPR033120; HOTDOG_ACOT."),
                    support("file:PSEPK/PP_5331/PP_5331-goa.tsv", "GO:0016790\tthiolester hydrolase activity"),
                ],
            },
            "GO:0052816": {
                "summary": "Long-chain fatty acyl-CoA hydrolase activity is the best-supported molecular function for PP_5331.",
                "action": "ACCEPT",
                "reason": "The product name and PANTHER/TreeGrafter GOA support a long-chain acyl-CoA thioester hydrolase role.",
                "supported_by": [
                    support("file:PSEPK/PP_5331/PP_5331-uniprot.txt", "SubName: Full=Long-chain acyl-CoA thioester hydrolase"),
                    support("file:PSEPK/PP_5331/PP_5331-uniprot.txt", "DR   GO; GO:0052816; F:long-chain fatty acyl-CoA hydrolase activity; IEA:TreeGrafter."),
                    support("file:PSEPK/PP_5331/PP_5331-deep-research-asta.md", "- **Protein Description:** SubName: Full=Long-chain acyl-CoA thioester hydrolase {ECO:0000313|EMBL:AAN70896.1};"),
                    support("file:PSEPK/PP_5331/PP_5331-goa.tsv", "GO:0052816\tlong-chain fatty acyl-CoA hydrolase activity"),
                ],
            },
        },
        "references": [
            ("file:PSEPK/PP_5331/PP_5331-uniprot.txt", "UniProtKB entry for PP_5331 (Q88C52)", "SubName: Full=Long-chain acyl-CoA thioester hydrolase"),
            ("file:PSEPK/PP_5331/PP_5331-goa.tsv", "QuickGO GOA annotations for PP_5331", "GO:0052816\tlong-chain fatty acyl-CoA hydrolase activity"),
            ("file:PSEPK/PP_5331/PP_5331-deep-research-asta.md", "Asta retrieval report for PP_5331 (Q88C52)", "uniprot_accession: Q88C52"),
        ],
        "core": [
            {
                "description": "Predicted long-chain fatty acyl-CoA thioester hydrolase activity in acyl-CoA turnover.",
                "molecular_function": term("GO:0052816", "long-chain fatty acyl-CoA hydrolase activity"),
                "directly_involved_in": [term("GO:0006637", "acyl-CoA metabolic process")],
                "supported_by": [
                    support("file:PSEPK/PP_5331/PP_5331-uniprot.txt", "SubName: Full=Long-chain acyl-CoA thioester hydrolase"),
                    support("file:PSEPK/PP_5331/PP_5331-uniprot.txt", "DR   GO; GO:0052816; F:long-chain fatty acyl-CoA hydrolase activity; IEA:TreeGrafter."),
                    support("file:PSEPK/PP_5331/PP_5331-deep-research-asta.md", "- **Key Domains:** Cytosol_ACT. (IPR040170); HOTDOG_ACOT. (IPR033120); HotDog_dom_sf. (IPR029069); Thioestr_dom. (IPR006683); 4HBT (PF03061)"),
                ],
            }
        ],
        "questions": [
            "Which long-chain fatty acyl-CoA substrates are preferred by PP_5331 in KT2440?",
        ],
        "experiments": [
            {
                "description": "Assay purified PP_5331 against a chain-length panel of acyl-CoA substrates and measure CoA release.",
                "experiment_type": "biochemical enzyme assay",
            }
        ],
    },
}


def add_file_references(data: dict, cfg: dict) -> None:
    refs = list(data.get("references") or [])
    seen = {ref.get("id") for ref in refs}
    for ref_id, title, supporting_text in cfg["references"]:
        if ref_id in seen:
            continue
        refs.append(
            {
                "id": ref_id,
                "title": title,
                "findings": [
                    {
                        "statement": "Local file evidence used for this first-pass ppu01040 review.",
                        "supporting_text": supporting_text,
                    }
                ],
            }
        )
        seen.add(ref_id)
    data["references"] = refs


def curate_gene(gene: str, cfg: dict) -> None:
    path = Path("genes/PSEPK") / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    data["gene_symbol"] = cfg["symbol"]
    data["status"] = "DRAFT"
    data["description"] = cfg["description"]
    for annotation in data.get("existing_annotations", []):
        go_id = annotation["term"]["id"]
        review = cfg["reviews"].get(go_id)
        if review is None:
            raise KeyError(f"No review configured for {gene} {go_id}")
        annotation["review"] = review
    add_file_references(data, cfg)
    data["core_functions"] = cfg["core"]
    data["proposed_new_terms"] = []
    data["suggested_questions"] = [{"question": question} for question in cfg.get("questions", [])]
    data["suggested_experiments"] = cfg.get("experiments", [])
    path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=100), encoding="utf-8")


def main() -> None:
    for gene, cfg in CONFIG.items():
        curate_gene(gene, cfg)
        print(f"Curated {gene}")


if __name__ == "__main__":
    main()
