#!/usr/bin/env python3
"""First-pass curation for the ppu04122 Tus/MnmA tRNA-thiolation bucket."""

from __future__ import annotations

import csv
from pathlib import Path

import yaml


SPECIES = "PSEPK"
ROOT = Path("genes") / SPECIES


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def term(go_id: str, label: str) -> dict[str, str]:
    return {"id": go_id, "label": label}


GO_REF_TITLES = {
    "GO_REF:0000002": "Gene Ontology annotation through association of InterPro records with GO terms",
    "GO_REF:0000044": (
        "Gene Ontology annotation based on UniProtKB/Swiss-Prot Subcellular Location vocabulary mapping, "
        "accompanied by conservative changes to GO terms applied by UniProt"
    ),
    "GO_REF:0000104": (
        "Electronic Gene Ontology annotations created by transferring manual GO annotations between "
        "related proteins based on shared sequence features"
    ),
    "GO_REF:0000118": "TreeGrafter-generated GO annotations",
    "GO_REF:0000120": "Combined Automated Annotation using Multiple IEA Methods",
}


GENES: dict[str, dict] = {
    "tusA-I": {
        "description": (
            "tusA-I encodes a TusA-family small sulfur carrier/sulfurtransferase-like protein. "
            "It is a paralogous TusA-like sulfur-relay candidate in the ppu04122 sulfur-relay "
            "boundary, but current first-pass evidence does not resolve whether it participates "
            "directly in the canonical TusBCD/TusE/MnmA tRNA-thiolation route."
        ),
        "core": [
            {
                "description": (
                    "Predicted TusA-family sulfur carrier/sulfurtransferase-like protein; exact "
                    "sulfur-relay recipient and pathway branch remain unresolved."
                ),
                "molecular_function": term("GO:0097163", "sulfur carrier activity"),
            }
        ],
        "questions": [
            "Does tusA-I supply sulfur to the canonical TusBCD/TusE/MnmA tRNA-thiolation pathway, or does it serve a different sulfur-relay client?"
        ],
    },
    "tusA": {
        "description": (
            "tusA encodes the canonical TusA sulfur carrier protein. In the Tus/MnmA sulfur-relay "
            "system, TusA-family sulfur carriers pass activated sulfur toward downstream TusBCD/TusE "
            "and MnmA components for wobble-position uridine thiolation of tRNA."
        ),
        "decisions": {
            "GO:0002143": ("ACCEPT", "tRNA wobble-position uridine thiolation is the pathway process supported by the TusA-family GOA assignment."),
            "GO:0005737": ("ACCEPT", "cytoplasm is appropriate for a soluble bacterial sulfur-relay/tRNA-modification protein."),
            "GO:0097163": ("ACCEPT", "sulfur carrier activity is the most informative molecular-function term in the fetched GOA set for TusA."),
        },
        "core": [
            {
                "description": "TusA sulfur carrier activity supporting tRNA wobble-uridine thiolation.",
                "molecular_function": term("GO:0097163", "sulfur carrier activity"),
                "directly_involved_in": [term("GO:0002143", "tRNA wobble position uridine thiolation")],
                "locations": [term("GO:0005737", "cytoplasm")],
            }
        ],
    },
    "tusD": {
        "description": (
            "tusD encodes a DsrE/TusD-family subunit of the TusBCD sulfurtransferase complex. "
            "This complex acts in the sulfur-relay branch that supplies sulfur for MnmA-dependent "
            "2-thiolation of wobble uridine in tRNA."
        ),
        "decisions": {
            "GO:0002143": ("ACCEPT", "tRNA wobble-position uridine thiolation is the specific biological process assigned by TreeGrafter for this TusD-family subunit."),
            "GO:0005737": ("ACCEPT", "cytoplasm is appropriate for the bacterial Tus sulfur-relay complex."),
            "GO:0005829": ("KEEP_AS_NON_CORE", "cytosol is a redundant imported location relative to the bacterial cytoplasm annotation."),
            "GO:0008033": ("KEEP_AS_NON_CORE", "tRNA processing is true but broader than the specific wobble-uridine thiolation process."),
            "GO:0016783": ("MARK_AS_OVER_ANNOTATED", "generic sulfurtransferase activity is less informative than the sulfur-carrier/complex role assigned to TusD."),
            "GO:0097163": ("ACCEPT", "sulfur carrier activity captures the TusD sulfur-relay role better than a generic transferase parent."),
            "GO:1990228": ("ACCEPT", "sulfurtransferase-complex membership matches the TusBCD complex assignment for TusD."),
        },
        "core": [
            {
                "description": "TusD subunit of the TusBCD sulfurtransferase complex for tRNA wobble-uridine thiolation.",
                "molecular_function": term("GO:0097163", "sulfur carrier activity"),
                "directly_involved_in": [term("GO:0002143", "tRNA wobble position uridine thiolation")],
                "locations": [term("GO:0005737", "cytoplasm")],
                "in_complex": term("GO:1990228", "sulfurtransferase complex"),
            }
        ],
    },
    "PP_3994": {
        "description": (
            "PP_3994 encodes a TusC/DsrF-like sulfur-relay protein adjacent to tusD, PP_3995/TusB, "
            "and tusE. UniProt names it a TusC-like tRNA 5-methylaminomethyl-2-thiouridine synthase "
            "component, supporting assignment as the TusC subunit of the TusBCD sulfurtransferase "
            "complex in the tRNA wobble-uridine thiolation pathway."
        ),
        "core": [
            {
                "description": "TusC-like subunit of the TusBCD sulfurtransferase complex for tRNA wobble-uridine thiolation.",
                "directly_involved_in": [term("GO:0002143", "tRNA wobble position uridine thiolation")],
                "in_complex": term("GO:1990228", "sulfurtransferase complex"),
            }
        ],
    },
    "PP_3995": {
        "description": (
            "PP_3995 encodes the TusB subunit of the TusBCD sulfurtransferase complex. "
            "Together with TusC/PP_3994 and TusD, it forms the sulfur-relay complex that feeds "
            "the MnmA tRNA-uridine 2-thiouridylase pathway."
        ),
        "decisions": {
            "GO:0002143": ("ACCEPT", "tRNA wobble-position uridine thiolation is the pathway process supported for the TusB subunit."),
            "GO:0005737": ("ACCEPT", "cytoplasm is appropriate for this bacterial sulfurtransferase-complex subunit."),
            "GO:1990228": ("ACCEPT", "sulfurtransferase-complex membership is the most specific GOA annotation for PP_3995/TusB."),
        },
        "core": [
            {
                "description": "TusB subunit of the TusBCD sulfurtransferase complex for tRNA wobble-uridine thiolation.",
                "directly_involved_in": [term("GO:0002143", "tRNA wobble position uridine thiolation")],
                "locations": [term("GO:0005737", "cytoplasm")],
                "in_complex": term("GO:1990228", "sulfurtransferase complex"),
            }
        ],
    },
    "tusE": {
        "description": (
            "tusE encodes a DsrC/TusE-family sulfurtransferase/sulfur-carrier protein. "
            "It functions as a downstream sulfur-relay factor in the MnmA-dependent pathway "
            "for tRNA wobble-position uridine thiolation."
        ),
        "decisions": {
            "GO:0002143": ("ACCEPT", "tRNA wobble-position uridine thiolation is the specific process assigned for TusE by TreeGrafter."),
            "GO:0005737": ("ACCEPT", "cytoplasm is appropriate for a soluble bacterial tRNA-thiolation sulfur-relay protein."),
            "GO:0097163": ("ACCEPT", "sulfur carrier activity is the specific MF currently assigned for TusE."),
        },
        "core": [
            {
                "description": "TusE sulfur-carrier activity in the sulfur relay to MnmA for tRNA wobble-uridine thiolation.",
                "molecular_function": term("GO:0097163", "sulfur carrier activity"),
                "directly_involved_in": [term("GO:0002143", "tRNA wobble position uridine thiolation")],
                "locations": [term("GO:0005737", "cytoplasm")],
            }
        ],
    },
    "mnmA": {
        "description": (
            "mnmA encodes tRNA-specific 2-thiouridylase MnmA/TrmU. It catalyzes ATP-dependent "
            "2-thiolation of wobble-position uridine in tRNA, using sulfur supplied through "
            "protein-bound sulfane sulfur from the upstream Tus sulfur-relay system."
        ),
        "decisions": {
            "GO:0002143": ("ACCEPT", "tRNA wobble-position uridine thiolation is the specific biological process for MnmA."),
            "GO:0005737": ("ACCEPT", "cytoplasm is appropriate for a bacterial tRNA-modification enzyme."),
            "GO:0006400": ("KEEP_AS_NON_CORE", "tRNA modification is correct but broader than wobble-position uridine thiolation."),
            "GO:0008033": ("KEEP_AS_NON_CORE", "tRNA processing is a broad parent process and not the most informative MnmA annotation."),
            "GO:0016740": ("MARK_AS_OVER_ANNOTATED", "generic transferase activity is over-broad when tRNA-uridine 2-sulfurtransferase activity is available."),
            "GO:0016783": ("MARK_AS_OVER_ANNOTATED", "generic sulfurtransferase activity is less precise than the Rhea/EC-backed tRNA-uridine 2-sulfurtransferase term."),
            "GO:0103016": ("ACCEPT", "tRNA-uridine 2-sulfurtransferase activity captures the direct MnmA catalytic function."),
        },
        "core": [
            {
                "description": "MnmA tRNA-uridine 2-sulfurtransferase activity forming wobble-position 2-thiouridine in tRNA.",
                "molecular_function": term("GO:0103016", "tRNA-uridine 2-sulfurtransferase activity"),
                "directly_involved_in": [term("GO:0002143", "tRNA wobble position uridine thiolation")],
                "locations": [term("GO:0005737", "cytoplasm")],
            }
        ],
    },
}


def read_tsv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def goa_snippet(row: dict[str, str]) -> str:
    return f"{row['GO TERM']}\t{row['GO NAME']}"


def line_containing(path: Path, pattern: str) -> str:
    text = path.read_text(encoding="utf-8")
    for line in text.splitlines():
        if pattern in line:
            return line
    raise ValueError(f"Pattern not found in {path}: {pattern}")


def uniprot_identity_snippet(uniprot: Path) -> str:
    for pattern in ("CC   -!- FUNCTION:", "DE   RecName: Full=", "DE   SubName: Full="):
        try:
            return line_containing(uniprot, pattern)
        except ValueError:
            pass
    return uniprot.read_text(encoding="utf-8").splitlines()[0]


def uniprot_go_snippet(uniprot: Path, term_id: str) -> str | None:
    text = uniprot.read_text(encoding="utf-8")
    for line in text.splitlines():
        if f"GO; {term_id};" in line:
            return line
    return None


def asta_support(gene: str) -> dict[str, str]:
    path = ROOT / gene / f"{gene}-deep-research-asta.md"
    accession = yaml.safe_load((ROOT / gene / f"{gene}-ai-review.yaml").read_text(encoding="utf-8"))["id"]
    return {
        "reference_id": f"file:{SPECIES}/{gene}/{gene}-deep-research-asta.md",
        "supporting_text": f"uniprot_accession: {accession}",
    }


def file_ref(kind: str, gene: str, gene_dir: Path) -> dict | None:
    if kind == "uniprot":
        path = gene_dir / f"{gene}-uniprot.txt"
        if not path.exists():
            return None
        return {
            "id": f"file:{SPECIES}/{gene}/{gene}-uniprot.txt",
            "title": f"UniProtKB entry for {gene}",
            "findings": [
                {
                    "statement": "UniProt provides protein identity, domain/family context, and GO cross-references used in this first-pass review.",
                    "supporting_text": uniprot_identity_snippet(path),
                }
            ],
        }
    if kind == "goa":
        path = gene_dir / f"{gene}-goa.tsv"
        if not path.exists():
            return None
        return {
            "id": f"file:{SPECIES}/{gene}/{gene}-goa.tsv",
            "title": f"QuickGO GOA annotations for {gene}",
            "findings": [
                {
                    "statement": "The fetched GOA table contains the annotations reviewed for this gene."
                }
            ],
        }
    if kind == "asta":
        path = gene_dir / f"{gene}-deep-research-asta.md"
        if not path.exists():
            return None
        return {
            "id": f"file:{SPECIES}/{gene}/{gene}-deep-research-asta.md",
            "title": f"Asta retrieval report for {gene}",
            "findings": [
                {
                    "statement": "Asta retrieval was generated for this first-pass review and used as lightweight identity/retrieval context.",
                    "supporting_text": asta_support(gene)["supporting_text"],
                }
            ],
        }
    raise ValueError(kind)


def ensure_references(data: dict, gene: str, gene_dir: Path) -> None:
    references = []
    seen: set[str] = set()
    for ref in data.get("references") or []:
        ref_id = ref.get("id")
        if not ref_id or ref_id in seen:
            continue
        if ref_id in GO_REF_TITLES:
            ref = {"id": ref_id, "title": GO_REF_TITLES[ref_id], "findings": []}
        references.append(ref)
        seen.add(ref_id)

    for kind in ("uniprot", "goa", "asta"):
        ref = file_ref(kind, gene, gene_dir)
        if ref and ref["id"] not in seen:
            references.append(ref)
            seen.add(ref["id"])
    data["references"] = references


def action_summary(action: str, gene: str, label: str) -> str:
    if action == "ACCEPT":
        return f"{label} is accepted for {gene} in the Tus/MnmA tRNA-thiolation first-pass review."
    if action == "KEEP_AS_NON_CORE":
        return f"{label} is retained for {gene} as supporting but non-core context."
    if action == "MARK_AS_OVER_ANNOTATED":
        return f"{label} is broader than the most informative Tus/MnmA pathway role for {gene}."
    if action == "UNDECIDED":
        return f"{label} remains unresolved for {gene} in this first-pass review."
    return f"{label} was reviewed for {gene}."


def support_for_existing(gene: str, term_id: str, label: str, row: dict[str, str] | None) -> list[dict[str, str]]:
    support: list[dict[str, str]] = []
    if row is not None:
        support.append(
            {
                "reference_id": f"file:{SPECIES}/{gene}/{gene}-goa.tsv",
                "supporting_text": goa_snippet(row),
            }
        )
    uniprot = ROOT / gene / f"{gene}-uniprot.txt"
    if uniprot.exists():
        go_line = uniprot_go_snippet(uniprot, term_id)
        if go_line:
            support.append(
                {
                    "reference_id": f"file:{SPECIES}/{gene}/{gene}-uniprot.txt",
                    "supporting_text": go_line,
                }
            )
    asta = ROOT / gene / f"{gene}-deep-research-asta.md"
    if asta.exists():
        support.append(asta_support(gene))
    return support


def review_existing_annotation(gene: str, annotation: dict, goa_rows: list[dict[str, str]], decisions: dict[str, tuple[str, str]]) -> None:
    term_data = annotation["term"]
    term_id = term_data["id"]
    label = term_data["label"]
    row = next((item for item in goa_rows if item["GO TERM"] == term_id and item["GO NAME"] == label), None)
    action, reason = decisions.get(
        term_id,
        ("KEEP_AS_NON_CORE", "This annotation is plausible context but is not the main curated Tus/MnmA first-pass role."),
    )
    annotation["review"] = {
        "summary": action_summary(action, gene, label),
        "action": action,
        "reason": reason,
        "supported_by": support_for_existing(gene, term_id, label, row),
    }


def core_support(gene: str, core: dict, annotations: list[dict], goa_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    support: list[dict[str, str]] = []
    term_ids: set[str] = set()
    for slot in ("molecular_function", "contributes_to_molecular_function", "in_complex"):
        if isinstance(core.get(slot), dict):
            term_ids.add(core[slot]["id"])
    for slot in ("directly_involved_in", "locations"):
        for item in core.get(slot, []) or []:
            term_ids.add(item["id"])

    for row in goa_rows:
        if row["GO TERM"] in term_ids:
            support.append(
                {
                    "reference_id": f"file:{SPECIES}/{gene}/{gene}-goa.tsv",
                    "supporting_text": goa_snippet(row),
                }
            )

    for annotation in annotations:
        term_id = annotation.get("term", {}).get("id")
        if term_id not in term_ids:
            continue
        for item in annotation.get("review", {}).get("supported_by") or []:
            support.append(item)

    uniprot = ROOT / gene / f"{gene}-uniprot.txt"
    if uniprot.exists():
        support.append(
            {
                "reference_id": f"file:{SPECIES}/{gene}/{gene}-uniprot.txt",
                "supporting_text": uniprot_identity_snippet(uniprot),
            }
        )
    if (ROOT / gene / f"{gene}-deep-research-asta.md").exists():
        support.append(asta_support(gene))

    deduped: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()
    for item in support:
        key = (item["reference_id"], item["supporting_text"])
        if key not in seen:
            deduped.append(item)
            seen.add(key)
    return deduped


def curate_gene(gene: str, cfg: dict) -> None:
    gene_dir = ROOT / gene
    review_path = gene_dir / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(review_path.read_text(encoding="utf-8")) or {}
    goa_rows = read_tsv(gene_dir / f"{gene}-goa.tsv")

    data["gene_symbol"] = gene
    data["status"] = "DRAFT"
    data["description"] = cfg["description"]
    ensure_references(data, gene, gene_dir)

    goa_keys = {(row["GO TERM"], row["GO NAME"]) for row in goa_rows}
    data["existing_annotations"] = [
        annotation
        for annotation in data.get("existing_annotations") or []
        if (annotation.get("term", {}).get("id"), annotation.get("term", {}).get("label")) in goa_keys
    ]

    for annotation in data.get("existing_annotations") or []:
        review_existing_annotation(gene, annotation, goa_rows, cfg.get("decisions", {}))

    core_functions: list[dict] = []
    for core_spec in cfg.get("core", []):
        core = dict(core_spec)
        core["supported_by"] = core_support(gene, core, data.get("existing_annotations") or [], goa_rows)
        core_functions.append(core)
    data["core_functions"] = core_functions
    data["proposed_new_terms"] = []
    data["suggested_questions"] = [
        {"question": question}
        for question in cfg.get(
            "questions",
            [f"What is the precise in vivo contribution of {gene} to P. putida KT2440 tRNA wobble-uridine thiolation?"],
        )
    ]
    data["suggested_experiments"] = [
        {
            "description": (
                f"Perturb {gene} and assay wobble-position 2-thiouridine-containing tRNAs by LC-MS or targeted tRNA modification profiling."
            ),
            "experiment_type": "gene perturbation and tRNA modification profiling",
        }
    ]

    review_path.write_text(
        yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=False, width=120),
        encoding="utf-8",
    )


def main() -> None:
    for gene, cfg in GENES.items():
        curate_gene(gene, cfg)


if __name__ == "__main__":
    main()
