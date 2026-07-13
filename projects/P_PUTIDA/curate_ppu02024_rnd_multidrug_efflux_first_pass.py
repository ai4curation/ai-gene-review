#!/usr/bin/env python3
"""First-pass curation for the ppu02024 RND multidrug efflux pair."""

from __future__ import annotations

import csv
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes/PSEPK"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


GENES = {
    "PP_2064": {
        "accession": "Q88L71",
        "description": (
            "PP_2064 encodes a predicted membrane-fusion protein/adaptor component "
            "of a resistance-nodulation-division (RND) multidrug efflux pump in "
            "Pseudomonas putida KT2440. The protein is best modeled as part of an "
            "efflux pump complex that contributes to drug/xenobiotic efflux rather "
            "than as a standalone transmembrane transporter."
        ),
        "product_quote": "DE   SubName: Full=Multidrug efflux RND membrane fusion protein",
        "domain_quote": "DR   InterPro; IPR006143; RND_pump_MFP.",
        "asta_quote": "protein_description: 'SubName: Full=Multidrug efflux RND membrane fusion protein",
    },
    "PP_2065": {
        "accession": "Q88L70",
        "description": (
            "PP_2065 encodes a predicted inner-membrane RND multidrug/xenobiotic "
            "efflux transporter in Pseudomonas putida KT2440. It likely forms the "
            "transport component of a local efflux pump pair with the adjacent "
            "membrane-fusion protein PP_2064."
        ),
        "product_quote": "DE   SubName: Full=Multidrug efflux RND transporter",
        "domain_quote": "DR   InterPro; IPR001036; Acrflvin-R.",
        "asta_quote": "protein_description: 'SubName: Full=Multidrug efflux RND transporter",
    },
}


GO_REF_TITLES = {
    "GO_REF:0000002": "Gene Ontology annotation through association of InterPro records with GO terms",
    "GO_REF:0000108": "Automatic assignment of GO terms using logical inference, based on inter-ontology links",
    "GO_REF:0000118": "TreeGrafter-generated GO annotations",
    "GO_REF:0000120": "Combined Automated Annotation using Multiple IEA Methods",
}


def file_ref(gene: str, suffix: str) -> str:
    return f"file:PSEPK/{gene}/{gene}-{suffix}"


def ref(reference_id: str, text: str) -> dict[str, str]:
    return {"reference_id": reference_id, "supporting_text": text}


def review(summary: str, action: str, reason: str, supported_by: list[dict[str, str]]) -> dict:
    return {
        "summary": summary,
        "action": action,
        "reason": reason,
        "supported_by": supported_by,
    }


def goa_rows(gene: str) -> dict[str, dict[str, str]]:
    path = GENE_ROOT / gene / f"{gene}-goa.tsv"
    with path.open(encoding="utf-8") as handle:
        return {row["GO TERM"]: row for row in csv.DictReader(handle, delimiter="\t")}


def goa_quote(row: dict[str, str]) -> str:
    return f"{row['GO TERM']}\t{row['GO NAME']}"


def ensure_references(data: dict, gene: str, cfg: dict) -> None:
    refs = {entry["id"]: entry for entry in data.get("references", [])}
    for ref_id, title in GO_REF_TITLES.items():
        refs.setdefault(ref_id, {"id": ref_id, "title": title, "findings": []})

    refs[file_ref(gene, "goa.tsv")] = {
        "id": file_ref(gene, "goa.tsv"),
        "title": f"QuickGO/GOA annotation table for {gene} in Pseudomonas putida KT2440",
        "findings": [],
    }
    refs[file_ref(gene, "uniprot.txt")] = {
        "id": file_ref(gene, "uniprot.txt"),
        "title": f"UniProt record {cfg['accession']} for {gene} in Pseudomonas putida KT2440",
        "findings": [
            {
                "statement": "UniProt product naming supports the first-pass RND efflux assignment.",
                "supporting_text": cfg["product_quote"],
            },
            {
                "statement": "Conserved domain annotation supports RND efflux-pump context.",
                "supporting_text": cfg["domain_quote"],
            },
        ],
    }
    refs[file_ref(gene, "deep-research-asta.md")] = {
        "id": file_ref(gene, "deep-research-asta.md"),
        "title": f"Asta retrieval report for {gene} in Pseudomonas putida KT2440",
        "findings": [
            {
                "statement": "Asta retrieval was checked for this first pass and recapitulates the UniProt efflux-pump assignment.",
                "supporting_text": cfg["asta_quote"],
            }
        ],
    }
    data["references"] = list(refs.values())


def support(gene: str, cfg: dict, rows: dict[str, dict[str, str]], go_id: str) -> list[dict[str, str]]:
    return [
        ref(file_ref(gene, "goa.tsv"), goa_quote(rows[go_id])),
        ref(file_ref(gene, "uniprot.txt"), cfg["product_quote"]),
        ref(file_ref(gene, "uniprot.txt"), cfg["domain_quote"]),
        ref(file_ref(gene, "deep-research-asta.md"), cfg["asta_quote"]),
    ]


def review_pp2064(gene: str, cfg: dict, rows: dict[str, dict[str, str]], go_id: str) -> dict:
    if go_id == "GO:0015562":
        return review(
            "Efflux transporter activity reflects the pump function, but PP_2064 is the membrane-fusion/adaptor component rather than the standalone transporter.",
            "MARK_AS_OVER_ANNOTATED",
            "The TreeGrafter call is biologically close at complex level, but an MFP/adaptor subunit should be modeled as contributing to efflux pump activity as part of the complex.",
            support(gene, cfg, rows, go_id),
        )
    if go_id == "GO:0016020":
        return review(
            "Membrane localization is appropriate broad context for the RND membrane-fusion/adaptor protein.",
            "ACCEPT",
            "The InterPro RND pump MFP annotation supports membrane-associated efflux-pump context, although GOA does not resolve a more specific bacterial compartment.",
            support(gene, cfg, rows, go_id),
        )
    if go_id == "GO:0022857":
        return review(
            "Generic transmembrane transporter activity is too broad and too direct for an MFP/adaptor subunit.",
            "MARK_AS_OVER_ANNOTATED",
            "PP_2064 is predicted as the membrane-fusion component of an RND pump. Transporter activity should be attributed to the efflux pump or transporter component rather than to the adaptor alone.",
            support(gene, cfg, rows, go_id),
        )
    if go_id == "GO:0055085":
        return review(
            "Transmembrane transport is appropriate process context for the RND efflux pump pair.",
            "ACCEPT",
            "PP_2064 is an RND membrane-fusion protein/adaptor and therefore contributes to pump-mediated transport even though it is not modeled as the standalone transporter.",
            support(gene, cfg, rows, go_id),
        )
    if go_id == "GO:1990281":
        return review(
            "Efflux pump complex membership is the best core annotation for the membrane-fusion/adaptor component.",
            "ACCEPT",
            "The predicted MFP/RND-pump domain architecture supports modeling PP_2064 as part of an efflux pump complex.",
            support(gene, cfg, rows, go_id),
        )
    raise KeyError(go_id)


def review_pp2065(gene: str, cfg: dict, rows: dict[str, dict[str, str]], go_id: str) -> dict:
    if go_id == "GO:0005886":
        return review(
            "Plasma membrane localization is appropriate for the inner-membrane RND transporter.",
            "ACCEPT",
            "UniProt subcellular-location annotation and multiple transmembrane segments support inner/cell membrane localization, captured as GO:0005886 for bacteria.",
            [
                ref(file_ref(gene, "goa.tsv"), goa_quote(rows[go_id])),
                ref(file_ref(gene, "uniprot.txt"), "SUBCELLULAR LOCATION: Cell inner membrane"),
                ref(file_ref(gene, "uniprot.txt"), "FT   TRANSMEM"),
            ],
        )
    if go_id == "GO:0016020":
        return review(
            "Generic membrane localization is supported but less informative than plasma membrane.",
            "MARK_AS_OVER_ANNOTATED",
            "GOA already contains GO:0005886 plasma membrane, which better captures the bacterial inner-membrane transporter location.",
            [
                ref(file_ref(gene, "goa.tsv"), goa_quote(rows[go_id])),
                ref(file_ref(gene, "goa.tsv"), goa_quote(rows["GO:0005886"])),
            ],
        )
    if go_id == "GO:0022857":
        return review(
            "Generic transmembrane transporter activity is true but less informative than the xenobiotic transporter activity.",
            "KEEP_AS_NON_CORE",
            "The RND transporter is a transmembrane transporter, but the xenobiotic/multidrug efflux term is more informative for the core function.",
            support(gene, cfg, rows, go_id),
        )
    if go_id == "GO:0042908":
        return review(
            "Xenobiotic transport is appropriate for the predicted RND multidrug efflux transporter.",
            "ACCEPT",
            "The RND/AcrB-family domain architecture and TreeGrafter xenobiotic transporter annotation support xenobiotic efflux as the core biological process.",
            support(gene, cfg, rows, go_id),
        )
    if go_id == "GO:0042910":
        return review(
            "Xenobiotic transmembrane transporter activity is the best available core molecular-function term for PP_2065.",
            "ACCEPT",
            "PP_2065 is the predicted inner-membrane RND transporter component of the local efflux pair, with AcrB-family domain support.",
            support(gene, cfg, rows, go_id),
        )
    if go_id == "GO:0055085":
        return review(
            "Transmembrane transport is correct but less specific than xenobiotic transport.",
            "KEEP_AS_NON_CORE",
            "The term describes the general transport process, while GO:0042908 captures the likely xenobiotic/multidrug efflux context.",
            support(gene, cfg, rows, go_id),
        )
    raise KeyError(go_id)


def core_functions(gene: str, cfg: dict) -> list[dict]:
    if gene == "PP_2064":
        return [
            {
                "description": "Membrane-fusion/adaptor component that contributes to RND efflux pump activity.",
                "contributes_to_molecular_function": {
                    "id": "GO:0015562",
                    "label": "efflux transmembrane transporter activity",
                },
                "directly_involved_in": [{"id": "GO:0055085", "label": "transmembrane transport"}],
                "locations": [{"id": "GO:0016020", "label": "membrane"}],
                "in_complex": {"id": "GO:1990281", "label": "efflux pump complex"},
                "supported_by": [
                    ref(file_ref(gene, "uniprot.txt"), cfg["product_quote"]),
                    ref(file_ref(gene, "uniprot.txt"), cfg["domain_quote"]),
                    ref(file_ref(gene, "deep-research-asta.md"), cfg["asta_quote"]),
                ],
            }
        ]
    return [
        {
            "description": "Inner-membrane RND multidrug/xenobiotic efflux transporter.",
            "molecular_function": {
                "id": "GO:0042910",
                "label": "xenobiotic transmembrane transporter activity",
            },
            "directly_involved_in": [{"id": "GO:0042908", "label": "xenobiotic transport"}],
            "locations": [{"id": "GO:0005886", "label": "plasma membrane"}],
            "supported_by": [
                ref(file_ref(gene, "uniprot.txt"), cfg["product_quote"]),
                ref(file_ref(gene, "uniprot.txt"), cfg["domain_quote"]),
                ref(file_ref(gene, "deep-research-asta.md"), cfg["asta_quote"]),
            ],
        }
    ]


def curate_gene(gene: str, cfg: dict) -> None:
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    rows = goa_rows(gene)
    data["status"] = "DRAFT"
    data["gene_symbol"] = gene
    data["description"] = cfg["description"]
    ensure_references(data, gene, cfg)

    reviewer = review_pp2064 if gene == "PP_2064" else review_pp2065
    for annotation in data["existing_annotations"]:
        annotation["review"] = reviewer(gene, cfg, rows, annotation["term"]["id"])

    data["core_functions"] = core_functions(gene, cfg)
    data["proposed_new_terms"] = []
    data["suggested_questions"] = [
        {
            "question": (
                "What substrates are exported by the PP_2064-PP_2065 RND efflux pair under KT2440 growth, stress, or community-interaction conditions?"
            )
        }
    ]
    data["suggested_experiments"] = [
        {
            "description": (
                "Construct single and paired PP_2064/PP_2065 deletion strains, test antibiotic/xenobiotic susceptibility and efflux assays, and verify whether both proteins are required for the same pump activity."
            ),
            "experiment_type": "efflux phenotype and susceptibility assay",
        }
    ]

    path.write_text(
        yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=False, width=100),
        encoding="utf-8",
    )
    print(f"Curated {path.relative_to(ROOT)}")


def main() -> None:
    for gene, cfg in GENES.items():
        curate_gene(gene, cfg)


if __name__ == "__main__":
    main()
