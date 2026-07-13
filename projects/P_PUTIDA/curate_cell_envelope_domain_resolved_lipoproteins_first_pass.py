#!/usr/bin/env python3
"""First-pass curate PSEPK domain-resolved lipoprotein spillovers."""

from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes" / "PSEPK"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


TERM = {
    "GO:0005886": {"id": "GO:0005886", "label": "plasma membrane"},
    "GO:0006508": {"id": "GO:0006508", "label": "proteolysis"},
    "GO:0008233": {"id": "GO:0008233", "label": "peptidase activity"},
    "GO:0009269": {"id": "GO:0009269", "label": "response to desiccation"},
    "GO:0016020": {"id": "GO:0016020", "label": "membrane"},
    "GO:0019867": {"id": "GO:0019867", "label": "outer membrane"},
    "GO:0020037": {"id": "GO:0020037", "label": "heme binding"},
    "GO:0030414": {"id": "GO:0030414", "label": "peptidase inhibitor activity"},
    "GO:0043448": {"id": "GO:0043448", "label": "alkane catabolic process"},
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


def common_support(gene: str, *, go_term: str | None = None, markers: tuple[str, ...] = ()) -> list[dict[str, str]]:
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
    data.append(support(file_id(gene, "deep-research-asta.md"), first_line(asta, "- **Protein Description:")))
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
        refs.append(
            {
                "id": ref_id,
                "title": {
                    file_id(gene, "goa.tsv"): f"QuickGO GOA annotations for {gene} ({accession})",
                    file_id(gene, "uniprot.txt"): f"UniProtKB entry for {gene} ({accession})",
                    file_id(gene, "deep-research-asta.md"): f"Asta retrieval report for {gene} ({accession})",
                }[ref_id],
                "findings": [],
            }
        )
    return refs


def make_review(
    gene: str,
    term_id: str,
    summary: str,
    action: str,
    reason: str,
    *,
    markers: tuple[str, ...],
) -> dict:
    return {
        "summary": summary,
        "action": action,
        "reason": reason,
        "supported_by": common_support(gene, go_term=term_id, markers=markers),
    }


def new_annotation(
    gene: str,
    term_id: str,
    qualifier: str,
    summary: str,
    reason: str,
    *,
    markers: tuple[str, ...],
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
    "PP_0116": ("Q88RL3", "PA5502-like_lipo.", "PA5502-like lipoprotein candidate"),
    "PP_0139": ("Q88RJ0", "ABC_trans_aux.", "ABC-transporter auxiliary lipoprotein candidate"),
    "PP_0512": ("Q88QI1", "Pilotin.", "pilotin/YscW-like lipoprotein candidate"),
    "PP_0549": ("Q88QE5", "DUF1375.", "DUF1375 lipoprotein candidate"),
    "PP_0576": ("Q88QB8", "DUF4136.", "DUF4136 lipoprotein candidate"),
    "PP_0753": ("Q88PU5", "Uncharacterised_YajG.", "YajG-like lipoprotein candidate"),
    "PP_1115": ("Q88NT9", "WHy-dom.", "LEA/WHy-domain desiccation-response lipoprotein candidate"),
    "PP_1146": ("Q88NQ9", "M949_RS01915-like_dom.", "M949_RS01915-like lipoprotein candidate"),
    "PP_1153": ("Q88NQ2", "PA1123-like_domain.", "PA1123-like lipoprotein candidate"),
    "PP_1161": ("Q88NP6", "YgfB-like.", "YgfB-like lipoprotein candidate"),
    "PP_1238": ("Q88NH1", "BamC-like.", "BamC-like envelope lipoprotein candidate"),
    "PP_1322": ("Q88N90", "Lipoprotein_DolP.", "DolP/BON-domain outer-membrane lipoprotein candidate"),
    "PP_1500": ("Q88MR9", "Peptidase_S33.", "peptidase S33 alpha/beta-hydrolase lipoprotein candidate"),
    "PP_1519": ("Q88MQ1", "Lipoprotein_YbaY-like.", "YbaY/pilotin-like lipoprotein candidate"),
    "PP_1970": ("Q88LG3", "DUF4823.", "DUF4823 lipoprotein candidate"),
    "PP_2003": ("Q88LD2", "DUF2242.", "DUF2242 lipoprotein candidate"),
    "PP_2020": ("Q88LB5", "DUF5629.", "DUF5629 lipoprotein candidate"),
    "PP_2121": ("Q88L16", "YgdI/YgdR-like.", "YgdI/YgdR-like POT-family-associated membrane lipoprotein candidate"),
    "PP_2191": ("Q88KU8", "WHy-dom.", "LEA/WHy-domain desiccation-response lipoprotein candidate"),
    "PP_2462": ("Q88K30", "Prot_inh_I78.", "peptidase inhibitor I78-family lipoprotein candidate"),
    "PP_2730": ("Q88JB9", "DUF3833.", "DUF3833 lipoprotein candidate"),
    "PP_3520": ("Q88H45", "CHP02001.", "CHP02001/Gcw lipoprotein candidate"),
    "PP_4199": ("Q88F99", "DUF4398.", "DUF4398 coiled-coil lipoprotein candidate"),
    "PP_4564": ("Q88EA2", "UCP028200.", "UCP028200/DUF6279 lipoprotein candidate"),
    "PP_4686": ("Q88DY2", "Cofac_haem-bd_dom.", "heme-binding envelope lipoprotein candidate"),
    "PP_4920": ("Q88DA7", "PdaC/RsiV-like_sf.", "PdaC/RsiV-like lipoprotein candidate"),
    "PP_4961": ("Q88D66", "MliC.", "MliC-family membrane lipoprotein candidate"),
    "PP_5319": ("Q88C64", "Lipoprotein_repeat.", "lipoprotein-repeat envelope candidate"),
    "PP_5333": ("Q88C50", "DUF3299.", "DUF3299 lipoprotein candidate"),
    "PP_5639": ("A0A140FWJ2", "DUF1375.", "YceK/YidQ-family DUF1375 lipoprotein candidate"),
}


def location_term(gene: str) -> str:
    if gene == "PP_1322":
        return "GO:0019867"
    if gene == "PP_2121":
        return "GO:0005886"
    return "GO:0016020"


def description_for(gene: str, role: str) -> str:
    return (
        f"{gene} encodes a {role} in Pseudomonas putida KT2440. "
        "The first-pass evidence is dominated by UniProt product, lipoprotein, and domain metadata; "
        "specific pathway placement is left unresolved unless a GOA/domain annotation supports it."
    )


def configured_reviews(gene: str, marker: str) -> dict[str, tuple[str, str, str, tuple[str, ...]]]:
    if gene in {"PP_1115", "PP_2191"}:
        return {
            "GO:0009269": (
                "Response to desiccation is plausible LEA/WHy-domain process context.",
                "ACCEPT",
                "The GOA row is an InterPro2GO inference from the WHy domain, matching the LEA/WHy-domain architecture.",
                (marker,),
            )
        }
    if gene == "PP_1500":
        return {
            "GO:0006508": (
                "Proteolysis is appropriate process context for the peptidase S33 lipoprotein.",
                "ACCEPT",
                "The peptidase S33 and alpha/beta-hydrolase-family evidence supports proteolytic process context.",
                (marker, "SIMILARITY: Belongs to the peptidase S33 family"),
            ),
            "GO:0008233": (
                "Peptidase activity is the supported molecular function.",
                "ACCEPT",
                "The GOA row and UniProt family/domain evidence support peptidase activity while not resolving a narrower substrate.",
                (marker, "SIMILARITY: Belongs to the peptidase S33 family"),
            ),
        }
    if gene == "PP_5319":
        return {
            "GO:0043448": (
                "Alkane catabolic process is likely over-propagated from a broad PANTHER family.",
                "MARK_AS_OVER_ANNOTATED",
                "The local UniProt evidence describes a lipoprotein-repeat protein and does not provide alkane-catabolic enzyme, transporter, or pathway evidence.",
                (marker,),
            )
        }
    return {}


def extra_new_annotations(gene: str, marker: str) -> list[tuple[str, str, str, str, tuple[str, ...]]]:
    rows = [
        (
            location_term(gene),
            "located_in",
            f"{gene} should be represented with conservative membrane/envelope localization.",
            "The product name and lipoprotein/domain metadata support membrane-associated envelope context, but not a specific pathway role.",
            (marker,),
        )
    ]
    if gene == "PP_2462":
        rows.append(
            (
                "GO:0030414",
                "enables",
                "PP_2462 should be represented as a peptidase inhibitor-family candidate.",
                "The I78 peptidase-inhibitor family/domain evidence supports peptidase inhibitor activity as a candidate molecular function.",
                (marker,),
            )
        )
    if gene == "PP_4686":
        rows.append(
            (
                "GO:0020037",
                "enables",
                "PP_4686 should be represented as a candidate heme-binding lipoprotein.",
                "The cofactor heme-binding domain evidence supports heme binding while leaving ferric-uptake pathway involvement unresolved.",
                (marker, "Cofac_haem_bdg"),
            )
        )
    return rows


def core_for(gene: str, role: str, marker: str) -> dict:
    core = {"description": role}
    if gene in {"PP_1115", "PP_2191"}:
        core["directly_involved_in"] = [TERM["GO:0009269"]]
    if gene == "PP_1500":
        core["molecular_function"] = TERM["GO:0008233"]
        core["directly_involved_in"] = [TERM["GO:0006508"]]
    if gene == "PP_2462":
        core["molecular_function"] = TERM["GO:0030414"]
    if gene == "PP_4686":
        core["molecular_function"] = TERM["GO:0020037"]
    if gene != "PP_5319" or "molecular_function" not in core:
        core["locations"] = [TERM[location_term(gene)]]
    core["supported_by"] = common_support(gene, markers=(marker,))
    return core


def apply_reviews(gene: str, accession: str, marker: str, role: str) -> None:
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    data["gene_symbol"] = gene
    data["status"] = "DRAFT"
    data["description"] = description_for(gene, role)
    data["references"] = reference_list(data.get("references") or [], gene, accession)

    new_terms = {term_id for term_id, *_ in extra_new_annotations(gene, marker)}
    data["existing_annotations"] = [
        annotation
        for annotation in (data.get("existing_annotations") or [])
        if not (
            annotation.get("term", {}).get("id") in new_terms
            and annotation.get("review", {}).get("action") == "NEW"
        )
    ]

    reviews = configured_reviews(gene, marker)
    seen_terms = set()
    for annotation in data.get("existing_annotations") or []:
        term_id = annotation["term"]["id"]
        seen_terms.add(term_id)
        if term_id not in reviews:
            raise ValueError(f"No review configured for {gene} {term_id}")
        summary, action, reason, markers = reviews[term_id]
        annotation["review"] = make_review(gene, term_id, summary, action, reason, markers=markers)

    missing = set(reviews) - seen_terms
    if missing:
        raise ValueError(f"Configured reviews not found in {gene}: {sorted(missing)}")

    for term_id, qualifier, summary, reason, markers in extra_new_annotations(gene, marker):
        data.setdefault("existing_annotations", []).append(
            new_annotation(gene, term_id, qualifier, summary, reason, markers=markers)
        )

    data["core_functions"] = [core_for(gene, role, marker)]
    data["proposed_new_terms"] = []
    data["suggested_questions"] = [
        {
            "question": (
                f"What is the envelope localization, partner set, and condition-specific phenotype of {gene} "
                f"as a {role}?"
            )
        }
    ]
    data["suggested_experiments"] = [
        {
            "description": (
                f"Localize tagged {gene} and compare deletion/complemented strains under outer-membrane, "
                "osmotic, desiccation, and envelope-stress conditions; add biochemical assays if a specific "
                "domain-predicted activity is testable."
            ),
            "experiment_type": "targeted envelope localization, stress phenotype, and biochemical assay",
        }
    ]
    path.write_text(yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, width=120), encoding="utf-8")


def write_notes(gene: str, accession: str, marker: str, role: str) -> None:
    uniprot = GENE_ROOT / gene / f"{gene}-uniprot.txt"
    asta = GENE_ROOT / gene / f"{gene}-deep-research-asta.md"
    product_line = first_line(uniprot, "DE   ")
    marker_line = first_line(uniprot, marker)
    asta_product = first_line(asta, "- **Protein Description:")
    note = [
        f"# {gene} notes",
        "",
        "2026-07-10: First-pass domain-resolved lipoprotein spillover curation.",
        description_for(gene, role),
        "",
        f"Primary provenance: UniProt product/domain evidence [{file_id(gene, 'uniprot.txt')} \"{product_line}\"; "
        f"{file_id(gene, 'uniprot.txt')} \"{marker_line}\"]. Asta retrieval mainly confirmed the same metadata-level "
        f"identity [{file_id(gene, 'deep-research-asta.md')} \"{asta_product}\"].",
        "",
        "Decision: " + role,
    ]
    if gene == "PP_5319":
        note.extend(
            [
                "",
                "Caution: the TreeGrafter/PANTHER alkane-catabolism annotation is treated as over-annotation because this pass found only lipoprotein-repeat evidence, not alkane-catabolic enzyme or pathway evidence.",
            ]
        )
    (GENE_ROOT / gene / f"{gene}-notes.md").write_text("\n".join(note) + "\n", encoding="utf-8")


def main() -> None:
    for gene, (accession, marker, role) in GENES.items():
        apply_reviews(gene, accession, marker, role)
        write_notes(gene, accession, marker, role)
        print(f"Curated {gene}")


if __name__ == "__main__":
    main()
