#!/usr/bin/env python3
"""First-pass curation for new ppu01501 beta-lactam-resistance stubs."""

from __future__ import annotations

from pathlib import Path

import yaml


SPECIES = "PSEPK"
ROOT = Path("genes") / SPECIES


GENES = {
    "PP_0906": {
        "symbol": "PP_0906",
        "description": (
            "PP_0906 is a predicted inner-membrane RND multidrug efflux "
            "transporter in Pseudomonas putida KT2440. It is a multi-pass "
            "membrane protein with AcrB/acriflavine-resistance transporter "
            "domains and is best treated as the substrate-translocating "
            "component of a cell-envelope efflux system. In the beta-lactam "
            "resistance map it contributes generic xenobiotic/drug efflux "
            "capacity rather than a beta-lactam-specific enzymatic mechanism."
        ),
        "uniprot_support": "DE   SubName: Full=Multidrug efflux RND transporter {ECO:0000313|EMBL:AAN66531.1};",
        "asta_support": "- **Protein Description:** SubName: Full=Multidrug efflux RND transporter {ECO:0000313|EMBL:AAN66531.1};",
        "core": {
            "description": (
                "RND inner-membrane xenobiotic efflux transporter component "
                "that contributes to export of toxic compounds across the "
                "cell envelope."
            ),
            "molecular_function": {
                "id": "GO:0042910",
                "label": "xenobiotic transmembrane transporter activity",
            },
            "directly_involved_in": [
                {"id": "GO:0042908", "label": "xenobiotic transport"}
            ],
            "locations": [{"id": "GO:0005886", "label": "plasma membrane"}],
            "in_complex": {"id": "GO:1990281", "label": "efflux pump complex"},
        },
        "decisions": {
            "GO:0005886": ("ACCEPT", "inner membrane localization for a multi-pass RND transporter"),
            "GO:0016020": ("KEEP_AS_NON_CORE", "broad membrane location; plasma membrane is more informative"),
            "GO:0022857": ("KEEP_AS_NON_CORE", "correct broad parent of the xenobiotic efflux activity"),
            "GO:0042908": ("ACCEPT", "xenobiotic transport is the relevant resistance-boundary process"),
            "GO:0042910": ("ACCEPT", "core xenobiotic transmembrane transporter activity for an RND pump"),
            "GO:0055085": ("KEEP_AS_NON_CORE", "broad parent process of xenobiotic transport"),
        },
    },
    "PP_0907": {
        "symbol": "PP_0907",
        "description": (
            "PP_0907 is a predicted membrane-fusion/periplasmic adaptor "
            "component of an RND efflux system in Pseudomonas putida KT2440. "
            "It carries membrane-fusion-protein domains and is best curated as "
            "a cell-envelope efflux-pump component that contributes to, but "
            "does not independently enable, transporter activity."
        ),
        "uniprot_support": "DE   SubName: Full=RND efflux membrane fusion protein-related protein {ECO:0000313|EMBL:AAN66532.1};",
        "asta_support": "- **Protein Description:** SubName: Full=RND efflux membrane fusion protein-related protein {ECO:0000313|EMBL:AAN66532.1};",
        "core": {
            "description": (
                "Membrane-fusion/adaptor component of an RND efflux pump, "
                "supporting tripartite efflux across the cell envelope."
            ),
            "contributes_to_molecular_function": {
                "id": "GO:0015562",
                "label": "efflux transmembrane transporter activity",
            },
            "locations": [{"id": "GO:0030313", "label": "cell envelope"}],
            "in_complex": {"id": "GO:1990281", "label": "efflux pump complex"},
        },
        "decisions": {
            "GO:0015562": ("MARK_AS_OVER_ANNOTATED", "the adaptor contributes to complex-level efflux but is not itself the translocating subunit"),
            "GO:0016020": ("KEEP_AS_NON_CORE", "broad membrane context for a cell-envelope adaptor"),
            "GO:0022857": ("MARK_AS_OVER_ANNOTATED", "generic transporter activity is over-assigned to an adaptor component"),
            "GO:0030313": ("ACCEPT", "cell-envelope localization fits a tripartite efflux adaptor"),
            "GO:0055085": ("KEEP_AS_NON_CORE", "broad process for the complex-level transport role"),
            "GO:1990281": ("ACCEPT", "efflux pump complex membership is the best current annotation"),
        },
    },
    "PP_1263": {
        "symbol": "PP_1263",
        "description": (
            "PP_1263 is a predicted outer-membrane factor/lipoprotein of an "
            "efflux system in Pseudomonas putida KT2440, annotated as a "
            "fusaric-acid-resistance protein. Its strongest first-pass role is "
            "outer-membrane efflux-channel context for xenobiotic resistance, "
            "not a beta-lactam-specific catalytic activity."
        ),
        "uniprot_support": "DE   SubName: Full=Fusaric acid resistance protein {ECO:0000313|EMBL:AAN66887.1};",
        "asta_support": "- **Protein Description:** SubName: Full=Fusaric acid resistance protein {ECO:0000313|EMBL:AAN66887.1};",
        "core": {
            "description": (
                "Outer-membrane factor component contributing to efflux-mediated "
                "transport of toxic compounds."
            ),
            "contributes_to_molecular_function": {
                "id": "GO:0015562",
                "label": "efflux transmembrane transporter activity",
            },
            "locations": [{"id": "GO:0009279", "label": "cell outer membrane"}],
            "in_complex": {"id": "GO:1990281", "label": "efflux pump complex"},
        },
        "decisions": {
            "GO:0009279": ("ACCEPT", "outer-membrane factor family and signal/lipid-anchor features support outer membrane localization"),
            "GO:0015562": ("ACCEPT", "efflux transporter component context is supported by the OMF family"),
            "GO:0016020": ("KEEP_AS_NON_CORE", "broad membrane parent of the outer membrane location"),
            "GO:0022857": ("KEEP_AS_NON_CORE", "broad transporter parent of the efflux component role"),
            "GO:0055085": ("KEEP_AS_NON_CORE", "broad transport process for this efflux boundary component"),
        },
    },
    "ampG": {
        "symbol": "ampG",
        "aliases": ["PP_1355"],
        "description": (
            "ampG encodes a predicted multi-pass MFS-family muropeptide "
            "permease in Pseudomonas putida KT2440. AmpG-family transporters "
            "import cell-wall recycling muropeptides across the inner membrane, "
            "linking peptidoglycan turnover to inducible beta-lactamase systems "
            "in organisms that carry an AmpC/AmpR-type response. The current "
            "GOA terms support a conservative transmembrane transporter role."
        ),
        "uniprot_support": "DE   SubName: Full=Muropeptide permease AmpG {ECO:0000313|EMBL:AAN66978.1};",
        "asta_support": "- **Protein Description:** SubName: Full=Muropeptide permease AmpG {ECO:0000313|EMBL:AAN66978.1};",
        "core": {
            "description": "Multi-pass AmpG-family muropeptide permease in cell-wall recycling and beta-lactam-resistance boundary context.",
            "molecular_function": {
                "id": "GO:0022857",
                "label": "transmembrane transporter activity",
            },
            "directly_involved_in": [
                {"id": "GO:0055085", "label": "transmembrane transport"}
            ],
            "locations": [{"id": "GO:0005886", "label": "plasma membrane"}],
        },
        "decisions": {
            "GO:0005886": ("ACCEPT", "inner membrane localization is expected for multi-pass AmpG"),
            "GO:0016020": ("KEEP_AS_NON_CORE", "broad membrane parent of plasma membrane localization"),
            "GO:0022857": ("ACCEPT", "best current molecular-function term for the muropeptide permease"),
            "GO:0055085": ("ACCEPT", "broad but appropriate process for the current GOA set"),
        },
    },
    "PP_1798": {
        "symbol": "PP_1798",
        "description": (
            "PP_1798 is a predicted outer-membrane efflux protein in "
            "Pseudomonas putida KT2440. It belongs to the outer membrane "
            "factor/TolC-like family and is best treated as an efflux-channel "
            "component of a tripartite transporter, contributing to resistance "
            "or export boundary context rather than a dedicated beta-lactamase."
        ),
        "uniprot_support": "DE   SubName: Full=Outer membrane efflux protein {ECO:0000313|EMBL:AAN67417.1};",
        "asta_support": "- **Protein Description:** SubName: Full=Outer membrane efflux protein {ECO:0000313|EMBL:AAN67417.1};",
        "core": {
            "description": "Outer-membrane factor/channel component contributing to efflux pump transport.",
            "contributes_to_molecular_function": {
                "id": "GO:0015562",
                "label": "efflux transmembrane transporter activity",
            },
            "locations": [{"id": "GO:0009279", "label": "cell outer membrane"}],
            "in_complex": {"id": "GO:1990281", "label": "efflux pump complex"},
        },
        "decisions": {
            "GO:0009279": ("ACCEPT", "outer membrane localization is supported for an OMF/TolC-like efflux channel"),
            "GO:0015288": ("KEEP_AS_NON_CORE", "porin/channel context is plausible but less specific than efflux complex role"),
            "GO:0015562": ("ACCEPT", "efflux transporter component role is supported by the OMF family"),
            "GO:0019867": ("KEEP_AS_NON_CORE", "outer membrane is correct but redundant with cell outer membrane"),
            "GO:0055085": ("KEEP_AS_NON_CORE", "broad parent process for efflux transport"),
            "GO:1990281": ("ACCEPT", "efflux pump complex membership is appropriate for an OMF channel"),
        },
    },
    "PP_3455": {
        "symbol": "PP_3455",
        "description": (
            "PP_3455 is a predicted membrane-fusion protein component of a "
            "multidrug RND efflux system in Pseudomonas putida KT2440. Its "
            "role is most conservatively described as an adaptor component of "
            "an efflux pump associated with antibiotic and xenobiotic response "
            "context, not as an independently active transporter."
        ),
        "uniprot_support": "DE   SubName: Full=Multidrug efflux RND membrane fusion protein {ECO:0000313|EMBL:AAN69057.1};",
        "asta_support": "- **Protein Description:** SubName: Full=Multidrug efflux RND membrane fusion protein {ECO:0000313|EMBL:AAN69057.1};",
        "core": {
            "description": "Membrane-fusion/adaptor component contributing to RND multidrug efflux pump activity.",
            "contributes_to_molecular_function": {
                "id": "GO:0015562",
                "label": "efflux transmembrane transporter activity",
            },
            "in_complex": {"id": "GO:1990281", "label": "efflux pump complex"},
        },
        "decisions": {
            "GO:0005886": ("KEEP_AS_NON_CORE", "membrane-associated efflux adaptor context"),
            "GO:0016020": ("KEEP_AS_NON_CORE", "broad membrane context"),
            "GO:0022857": ("MARK_AS_OVER_ANNOTATED", "generic transporter activity is over-assigned to a membrane-fusion adaptor"),
            "GO:0046677": ("KEEP_AS_NON_CORE", "antibiotic response is plausible resistance context but not the molecular role"),
            "GO:0055085": ("KEEP_AS_NON_CORE", "broad transport process for the complex-level role"),
        },
    },
    "PP_3582": {
        "symbol": "PP_3582",
        "description": (
            "PP_3582 is a predicted outer-membrane factor of an RND efflux "
            "transporter in Pseudomonas putida KT2440. Its strongest "
            "first-pass assignment is an outer-membrane efflux-channel "
            "component contributing to cell-envelope export and resistance "
            "boundary context."
        ),
        "uniprot_support": "DE   SubName: Full=RND efflux transporter, outer membrane protein {ECO:0000313|EMBL:AAN69183.1};",
        "asta_support": "- **Protein Description:** SubName: Full=RND efflux transporter, outer membrane protein {ECO:0000313|EMBL:AAN69183.1};",
        "core": {
            "description": "Outer-membrane factor component contributing to RND efflux pump transport.",
            "contributes_to_molecular_function": {
                "id": "GO:0015562",
                "label": "efflux transmembrane transporter activity",
            },
            "locations": [{"id": "GO:0009279", "label": "cell outer membrane"}],
            "in_complex": {"id": "GO:1990281", "label": "efflux pump complex"},
        },
        "decisions": {
            "GO:0009279": ("ACCEPT", "outer membrane localization is supported by the OMF family assignment"),
            "GO:0015562": ("ACCEPT", "efflux transporter component role is supported by the OMF family"),
            "GO:0016020": ("KEEP_AS_NON_CORE", "broad membrane parent of outer membrane localization"),
            "GO:0022857": ("KEEP_AS_NON_CORE", "broad transporter parent of the efflux component role"),
            "GO:0055085": ("KEEP_AS_NON_CORE", "broad parent process for efflux transport"),
        },
    },
    "PP_4923": {
        "symbol": "PP_4923",
        "description": (
            "PP_4923 is a predicted outer-membrane efflux protein in "
            "Pseudomonas putida KT2440. It belongs to the outer membrane "
            "factor/TolC-like family and likely acts as an efflux-channel "
            "component of a tripartite transporter, providing resistance "
            "boundary context rather than beta-lactam-specific hydrolysis."
        ),
        "uniprot_support": "DE   SubName: Full=Outer membrane efflux protein {ECO:0000313|EMBL:AAN70490.1};",
        "asta_support": "- **Protein Description:** SubName: Full=Outer membrane efflux protein {ECO:0000313|EMBL:AAN70490.1};",
        "core": {
            "description": "Outer-membrane factor/channel component contributing to efflux pump transport.",
            "contributes_to_molecular_function": {
                "id": "GO:0015562",
                "label": "efflux transmembrane transporter activity",
            },
            "locations": [{"id": "GO:0009279", "label": "cell outer membrane"}],
            "in_complex": {"id": "GO:1990281", "label": "efflux pump complex"},
        },
        "decisions": {
            "GO:0009279": ("ACCEPT", "outer membrane localization is supported for an OMF/TolC-like efflux channel"),
            "GO:0015288": ("KEEP_AS_NON_CORE", "porin/channel context is plausible but less specific than efflux complex role"),
            "GO:0015562": ("ACCEPT", "efflux transporter component role is supported by the OMF family"),
            "GO:0019867": ("KEEP_AS_NON_CORE", "outer membrane is correct but redundant with cell outer membrane"),
            "GO:0055085": ("KEEP_AS_NON_CORE", "broad parent process for efflux transport"),
            "GO:1990281": ("ACCEPT", "efflux pump complex membership is appropriate for an OMF channel"),
        },
    },
}


def support(gene: str, source: str, text: str) -> dict[str, str]:
    return {
        "reference_id": f"file:{SPECIES}/{gene}/{gene}-{source}",
        "supporting_text": text,
    }


def ensure_reference(refs: list[dict], ref_id: str, title: str, finding_text: str | None = None) -> None:
    if any(ref.get("id") == ref_id for ref in refs):
        return
    ref = {"id": ref_id, "title": title, "findings": []}
    if finding_text:
        ref["findings"].append(
            {
                "statement": "Used as lightweight first-pass identity and functional context.",
                "supporting_text": finding_text,
            }
        )
    refs.append(ref)


def curate_gene(gene: str, cfg: dict) -> None:
    path = ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    data["gene_symbol"] = cfg["symbol"]
    if cfg.get("aliases"):
        data["aliases"] = cfg["aliases"]
    elif cfg["symbol"] != gene:
        data["aliases"] = [gene]
    data["status"] = "DRAFT"
    data["description"] = cfg["description"]

    refs = data.setdefault("references", [])
    ensure_reference(refs, f"file:{SPECIES}/{gene}/{gene}-uniprot.txt", f"UniProt record for {gene}", cfg["uniprot_support"])
    ensure_reference(refs, f"file:{SPECIES}/{gene}/{gene}-goa.tsv", f"QuickGO GOA annotations for {gene}")
    ensure_reference(refs, f"file:{SPECIES}/{gene}/{gene}-deep-research-asta.md", f"Asta retrieval report for {gene}", cfg["asta_support"])

    first = True
    for annotation in data.get("existing_annotations", []):
        term = annotation["term"]
        term_id = term["id"]
        label = term["label"]
        action, rationale = cfg["decisions"][term_id]
        by = [support(gene, "goa.tsv", f"{term_id}\t{label}")]
        if first:
            by.append(support(gene, "deep-research-asta.md", cfg["asta_support"]))
            first = False
        annotation["review"] = {
            "summary": f"{label} is reviewed in the ppu01501 beta-lactam-resistance boundary context.",
            "action": action,
            "reason": (
                f"{rationale}. The fetched GOA term, UniProt protein identity, "
                "and Asta target context support this first-pass decision."
            ),
            "supported_by": by,
        }

    existing_ids = {annotation["term"]["id"] for annotation in data.get("existing_annotations", [])}
    if cfg["core"].get("in_complex", {}).get("id") == "GO:1990281" and "GO:1990281" not in existing_ids:
        data.setdefault("existing_annotations", []).append(
            {
                "term": {"id": "GO:1990281", "label": "efflux pump complex"},
                "evidence_type": "IEA",
                "original_reference_id": f"file:{SPECIES}/{gene}/{gene}-uniprot.txt",
                "qualifier": "part_of",
                "review": {
                    "summary": "Efflux pump complex membership is added to represent the component role of this beta-lactam-resistance boundary protein.",
                    "action": "NEW",
                    "reason": (
                        "The protein identity and domain/family context support "
                        "membership in an RND or outer-membrane-factor efflux "
                        "assembly. This captures component status more accurately "
                        "than assigning the complete transporter activity to every "
                        "subunit."
                    ),
                    "supported_by": [
                        support(gene, "uniprot.txt", cfg["uniprot_support"]),
                        support(gene, "deep-research-asta.md", cfg["asta_support"]),
                    ],
                },
            }
        )

    core = dict(cfg["core"])
    core["supported_by"] = [
        support(gene, "uniprot.txt", cfg["uniprot_support"]),
        support(gene, "deep-research-asta.md", cfg["asta_support"]),
    ]
    data["core_functions"] = [core]
    data["proposed_new_terms"] = []
    data["suggested_questions"] = [
        {
            "question": (
                f"What is the physiological pump partner or beta-lactam-resistance "
                f"contribution of {cfg['symbol']} in KT2440 under antibiotic stress?"
            )
        }
    ]
    data["suggested_experiments"] = [
        {
            "description": (
                f"Construct a {cfg['symbol']} deletion and complementation strain "
                "and measure susceptibility to representative beta-lactams and "
                "non-beta-lactam efflux substrates."
            )
        }
    ]

    path.write_text(yaml.safe_dump(data, sort_keys=False, width=100), encoding="utf-8")


def main() -> None:
    for gene, cfg in GENES.items():
        curate_gene(gene, cfg)
        print(f"curated {gene}")


if __name__ == "__main__":
    main()
