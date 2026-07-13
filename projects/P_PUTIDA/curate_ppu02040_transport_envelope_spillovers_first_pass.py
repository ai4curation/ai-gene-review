#!/usr/bin/env python3
"""First-pass curation for ppu02040 transport/envelope spillover gene PP_1087."""

from __future__ import annotations

from pathlib import Path

import yaml


SPECIES = "PSEPK"
GENE = "PP_1087"
ROOT = Path(__file__).resolve().parents[2]
GENE_DIR = ROOT / "genes" / SPECIES / GENE


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def term(term_id: str, label: str) -> dict[str, str]:
    return {"id": term_id, "label": label}


def ref_id(suffix: str) -> str:
    return f"file:{SPECIES}/{GENE}/{GENE}-{suffix}"


def support(reference_id: str, text: str) -> dict[str, str]:
    return {"reference_id": reference_id, "supporting_text": text}


def find_line(path: Path, needle: str) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if needle in line:
            return line
    raise ValueError(f"{needle!r} not found in {path}")


def goa_line(term_id: str) -> dict[str, str]:
    return support(ref_id("goa.tsv"), find_line(GENE_DIR / f"{GENE}-goa.tsv", term_id))


def uniprot_line(needle: str) -> dict[str, str]:
    return support(ref_id("uniprot.txt"), find_line(GENE_DIR / f"{GENE}-uniprot.txt", needle))


def asta_line(needle: str = "- **Protein Description:**") -> dict[str, str]:
    return support(ref_id("deep-research-asta.md"), find_line(GENE_DIR / f"{GENE}-deep-research-asta.md", needle))


def uniq(items: list[dict[str, str]]) -> list[dict[str, str]]:
    seen: set[tuple[str, str]] = set()
    out: list[dict[str, str]] = []
    for item in items:
        key = (item["reference_id"], item["supporting_text"])
        if key not in seen:
            out.append(item)
            seen.add(key)
    return out


def file_ref(suffix: str, title: str, statement: str) -> dict:
    path = GENE_DIR / f"{GENE}-{suffix}"
    if not path.exists():
        return {}
    return {"id": ref_id(suffix), "title": title, "findings": [{"statement": statement}]}


def main() -> None:
    path = GENE_DIR / f"{GENE}-ai-review.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    data["status"] = "DRAFT"
    data["gene_symbol"] = GENE
    data["description"] = (
        "PP_1087 encodes a predicted signal-peptide-bearing OmpA-family outer-membrane/envelope "
        "protein in Pseudomonas putida KT2440. It appears in the broad ppu02040 flagellar-assembly "
        "map as an envelope side entry, but current first-pass evidence supports only membrane/envelope "
        "localization rather than a direct flagellar apparatus role."
    )
    data["references"] = [
        {
            "id": "GO_REF:0000104",
            "title": (
                "Electronic Gene Ontology annotations created by transferring manual GO annotations between "
                "related proteins based on shared sequence features"
            ),
            "findings": [],
        },
        file_ref("uniprot.txt", "UniProtKB entry for PP_1087", "UniProt protein name, OmpA/MotY_N-family domains, signal peptide, and GO cross-reference used for first-pass curation."),
        file_ref("goa.tsv", "QuickGO GOA annotations for PP_1087", "Single fetched GOA membrane row reviewed in this first-pass curation file."),
        file_ref("deep-research-asta.md", "Asta retrieval report for PP_1087", "Asta retrieval provided fast metadata confirmation but no usable organism-specific literature beyond UniProt/GOA/domain context."),
    ]

    extra = [
        uniprot_line("SubName: Full=Outer membrane protein, OmpA family"),
        uniprot_line("DR   InterPro; IPR006665; OmpA-like."),
        uniprot_line("DR   Pfam; PF00691; OmpA; 1."),
        uniprot_line("FT   SIGNAL"),
        asta_line(),
    ]
    data["existing_annotations"][0]["review"] = {
        "summary": "The generic membrane annotation was reviewed for PP_1087 in the ppu02040 spillover first pass.",
        "action": "MODIFY",
        "reason": "Membrane localization is supported, but the protein name, signal peptide, and OmpA-family domain evidence point more specifically to an outer-membrane/cell-envelope protein; no direct flagellar apparatus role is supported.",
        "proposed_replacement_terms": [term("GO:0009279", "cell outer membrane")],
        "supported_by": uniq([goa_line("GO:0016020")] + extra),
    }
    data["core_functions"] = [
        {
            "description": "Predicted OmpA-family outer-membrane/envelope protein retained as a nonflagellar ppu02040 spillover.",
            "locations": [term("GO:0009279", "cell outer membrane")],
            "supported_by": uniq(
                [
                    goa_line("GO:0016020"),
                    uniprot_line("SubName: Full=Outer membrane protein, OmpA family"),
                    uniprot_line("DR   InterPro; IPR006665; OmpA-like."),
                    uniprot_line("DR   Pfam; PF00691; OmpA; 1."),
                    uniprot_line("FT   SIGNAL"),
                    asta_line(),
                ]
            ),
        }
    ]
    data["proposed_new_terms"] = []
    data["suggested_questions"] = [
        {"question": "Does PP_1087 have any experimentally detectable role in envelope stability, cell-surface interactions, or motility-associated envelope remodeling?"},
        {"question": "Is PP_1087 physically or genetically linked to flagellar function, or is its ppu02040 membership an automated map spillover from OmpA/MotY-like family context?"},
    ]
    data["suggested_experiments"] = [
        {"description": "Test a PP_1087 deletion for outer-membrane integrity, envelope stress sensitivity, and swimming/swarming phenotypes under matched growth conditions."},
        {"description": "Localize tagged PP_1087 and compare its abundance in planktonic versus surface-associated states to determine whether it is a general envelope protein or conditionally motility-associated."},
    ]
    path.write_text(
        yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=False, width=100),
        encoding="utf-8",
    )
    print(f"Curated {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
