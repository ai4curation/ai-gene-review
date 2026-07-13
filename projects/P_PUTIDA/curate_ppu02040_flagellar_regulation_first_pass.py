#!/usr/bin/env python3
"""First-pass curation for the ppu02040 flagellar regulation gap gene atoC."""

from __future__ import annotations

from pathlib import Path

import yaml


SPECIES = "PSEPK"
GENE = "atoC"
ROOT = Path(__file__).resolve().parents[2]
GENE_DIR = ROOT / "genes" / SPECIES / GENE


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


GO_REF_TITLES = {
    "GO_REF:0000002": "Gene Ontology annotation through association of InterPro records with GO terms",
    "GO_REF:0000104": (
        "Electronic Gene Ontology annotations created by transferring manual GO annotations between "
        "related proteins based on shared sequence features"
    ),
    "GO_REF:0000120": "Combined Automated Annotation using Multiple IEA Methods",
}


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


def review(term_id: str, label: str, action: str, reason: str, extra: list[dict[str, str]] | None = None) -> dict:
    return {
        "summary": f"{label} was reviewed for atoC in the ppu02040 flagellar-regulation first pass.",
        "action": action,
        "reason": reason,
        "supported_by": uniq([goa_line(term_id), asta_line()] + (extra or [])),
    }


def file_ref(suffix: str, title: str, statement: str) -> dict:
    path = GENE_DIR / f"{GENE}-{suffix}"
    if not path.exists():
        return {}
    return {"id": ref_id(suffix), "title": title, "findings": [{"statement": statement}]}


def normalize_references(existing: list[dict]) -> list[dict]:
    refs: list[dict] = []
    seen: set[str] = set()
    for entry in existing or []:
        ref = dict(entry)
        rid = ref.get("id")
        if not rid or rid in seen:
            continue
        if rid in GO_REF_TITLES:
            ref = {"id": rid, "title": GO_REF_TITLES[rid], "findings": []}
        refs.append(ref)
        seen.add(rid)
    for ref in [
        file_ref("uniprot.txt", "UniProtKB entry for atoC", "UniProt protein names, domains, GO cross-references, and response-regulator/sigma-54 activator features used for first-pass curation."),
        file_ref("goa.tsv", "QuickGO GOA annotations for atoC", "Fetched GOA rows reviewed in this first-pass curation file."),
        file_ref("deep-research-asta.md", "Asta retrieval report for atoC", "Asta retrieval provided fast metadata confirmation but no usable organism-specific hypothesis beyond UniProt/GOA/domain context."),
    ]:
        rid = ref.get("id")
        if rid and rid not in seen:
            refs.append(ref)
            seen.add(rid)
    return refs


def main() -> None:
    path = GENE_DIR / f"{GENE}-ai-review.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    data["status"] = "DRAFT"
    data["gene_symbol"] = GENE
    data["description"] = (
        "atoC encodes a predicted two-component response-regulator transcriptional activator in the "
        "Pseudomonas putida KT2440 flagellar regulatory region. The protein combines a receiver domain, "
        "sigma-54-interaction/AAA+ ATPase module, and Fis-family helix-turn-helix DNA-binding domain, "
        "supporting a conserved role as a phosphorylation-responsive regulator of transcription rather "
        "than a structural flagellar apparatus component."
    )
    data["references"] = normalize_references(data.get("references", []))

    extra_common = [
        uniprot_line("SubName: Full=Two component system AtoC DNA-binding transcriptional activator"),
        uniprot_line('FT                   /note="Response regulatory"'),
        uniprot_line('FT                   /note="Sigma-54 factor interaction"'),
        uniprot_line("DR   Pfam; PF00158; Sigma54_activat; 1."),
        uniprot_line("DR   Pfam; PF02954; HTH_8; 1."),
    ]
    decisions = {
        "GO:0000160": (
            "ACCEPT",
            "A receiver domain and predicted aspartyl-phosphate site support two-component phosphorelay context for atoC.",
            [uniprot_line('FT                   /note="4-aspartylphosphate"'), uniprot_line("DR   PROSITE; PS50110; RESPONSE_REGULATORY; 1.")],
        ),
        "GO:0000166": (
            "KEEP_AS_NON_CORE",
            "Nucleotide binding is broadly compatible with the AAA+/sigma-54-interaction module but is less informative than ATP binding and transcriptional regulation.",
            [uniprot_line("DR   InterPro; IPR003593; AAA+_ATPase.")],
        ),
        "GO:0005524": (
            "ACCEPT",
            "ATP binding is consistent with the sigma-54-interacting AAA+ module typical of bacterial enhancer-binding response regulators.",
            [uniprot_line("DR   InterPro; IPR003593; AAA+_ATPase."), uniprot_line("KW   ATP-binding")],
        ),
        "GO:0006351": (
            "KEEP_AS_NON_CORE",
            "DNA-templated transcription is directionally correct but too broad for atoC; the reviewed core role is regulation/activation of transcription.",
            [uniprot_line("KW   Transcription")],
        ),
        "GO:0006355": (
            "ACCEPT",
            "Regulation of DNA-templated transcription captures the main process role supported by the DNA-binding transcriptional activator description and HTH/sigma-54 activator domains.",
            [uniprot_line("KW   Transcription regulation")],
        ),
        "GO:0043565": (
            "ACCEPT",
            "Sequence-specific DNA binding is supported by the HTH/Fis-family DNA-binding domain in this predicted transcriptional activator.",
            [uniprot_line("DR   InterPro; IPR002197; HTH_Fis."), uniprot_line("KW   DNA-binding")],
        ),
    }
    for annotation in data.get("existing_annotations", []) or []:
        tid = annotation["term"]["id"]
        action, reason, extra = decisions[tid]
        annotation["review"] = review(tid, annotation["term"]["label"], action, reason, extra_common + extra)

    data["existing_annotations"].append(
        {
            "term": term("GO:0001216", "DNA-binding transcription activator activity"),
            "evidence_type": "ISS",
            "original_reference_id": ref_id("uniprot.txt"),
            "qualifier": "enables",
            "review": {
                "summary": "atoC is a predicted DNA-binding transcription activator with receiver, sigma-54-interaction/AAA+, and HTH domains.",
                "action": "NEW",
                "reason": "The seeded GOA captures DNA binding and generic transcription regulation but misses the more specific transcription activator molecular function implied by the product name and domain architecture.",
                "supported_by": uniq(
                    [
                        uniprot_line("SubName: Full=Two component system AtoC DNA-binding transcriptional activator"),
                        uniprot_line("DR   Pfam; PF00158; Sigma54_activat; 1."),
                        uniprot_line("DR   Pfam; PF02954; HTH_8; 1."),
                        asta_line(),
                    ]
                ),
            },
        }
    )

    data["core_functions"] = [
        {
            "description": "Predicted phosphorylation-responsive sigma-54-associated DNA-binding transcription activator in the flagellar regulatory region.",
            "molecular_function": term("GO:0001216", "DNA-binding transcription activator activity"),
            "directly_involved_in": [
                term("GO:0000160", "phosphorelay signal transduction system"),
                term("GO:0006355", "regulation of DNA-templated transcription"),
            ],
            "supported_by": uniq(
                [
                    goa_line("GO:0000160"),
                    goa_line("GO:0006355"),
                    goa_line("GO:0043565"),
                    uniprot_line("SubName: Full=Two component system AtoC DNA-binding transcriptional activator"),
                    uniprot_line('FT                   /note="Response regulatory"'),
                    uniprot_line('FT                   /note="Sigma-54 factor interaction"'),
                    uniprot_line("DR   Pfam; PF00158; Sigma54_activat; 1."),
                    uniprot_line("DR   Pfam; PF02954; HTH_8; 1."),
                    asta_line(),
                ]
            ),
        }
    ]
    data["proposed_new_terms"] = []
    data["suggested_questions"] = [
        {
            "question": "Is PP_4371/atoC the KT2440 FleR-like response regulator for a specific flagellar sigma-54 promoter tier, or does it regulate a different local target set?"
        },
        {
            "question": "What sensor kinase phosphorylates AtoC in KT2440, and under which motility or surface-growth conditions is this regulator active?"
        },
    ]
    data["suggested_experiments"] = [
        {
            "description": "Construct an atoC deletion and test swimming motility, flagellar gene expression, and complementation under low- and high-c-di-GMP conditions."
        },
        {
            "description": "Map AtoC-bound promoters by ChIP-seq or targeted EMSA and test phosphorylation-dependent activation of candidate sigma-54 promoters in reporter assays."
        },
    ]
    path.write_text(
        yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=False, width=100),
        encoding="utf-8",
    )
    print(f"Curated {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
