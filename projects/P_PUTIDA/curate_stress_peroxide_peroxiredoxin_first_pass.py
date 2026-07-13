#!/usr/bin/env python3
"""First-pass curate the PSEPK peroxide/peroxiredoxin stress-detox batch."""

from __future__ import annotations

import csv
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes" / "PSEPK"
BATCH_TSV = ROOT / "projects/P_PUTIDA/batches/module_stress_detoxification_peroxide_peroxiredoxin_detoxification.tsv"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


TERM = {
    "GO:0004130": {"id": "GO:0004130", "label": "cytochrome-c peroxidase activity"},
    "GO:0004601": {"id": "GO:0004601", "label": "peroxidase activity"},
    "GO:0005737": {"id": "GO:0005737", "label": "cytoplasm"},
    "GO:0005829": {"id": "GO:0005829", "label": "cytosol"},
    "GO:0008379": {"id": "GO:0008379", "label": "thioredoxin peroxidase activity"},
    "GO:0016691": {"id": "GO:0016691", "label": "chloride peroxidase activity"},
    "GO:0020037": {"id": "GO:0020037", "label": "heme binding"},
    "GO:0042597": {"id": "GO:0042597", "label": "periplasmic space"},
    "GO:0051920": {"id": "GO:0051920", "label": "peroxiredoxin activity"},
    "GO:0098869": {"id": "GO:0098869", "label": "cellular oxidant detoxification"},
    "GO:0140824": {"id": "GO:0140824", "label": "thioredoxin-dependent peroxiredoxin activity"},
}


GENE_INFO = {
    "osmC": {
        "role": "OsmC/Ohr-family stress-induced peroxidase",
        "description": (
            "osmC encodes an OsmC/Ohr-family stress-induced peroxiredoxin/peroxidase in "
            "Pseudomonas putida KT2440. First-pass evidence supports peroxide or organic "
            "hydroperoxide detoxification and oxidative-stress response context, but not a "
            "resolved electron donor, localization, or pathway-specific substrate."
        ),
        "primary_function": TERM["GO:0004601"],
        "process": TERM["GO:0098869"],
        "locations": [],
        "new_terms": [],
    },
    "PP_0235": {
        "role": "Prx6-family peroxiredoxin",
        "description": (
            "PP_0235 encodes a Prx6-subfamily peroxiredoxin/peroxidase in Pseudomonas "
            "putida KT2440. Its UniProt family assignment and GOA support peroxiredoxin "
            "activity, cellular oxidant detoxification, and a soluble cytosolic role in "
            "redox stress protection."
        ),
        "primary_function": TERM["GO:0051920"],
        "process": TERM["GO:0098869"],
        "locations": [TERM["GO:0005829"]],
        "new_terms": [],
    },
    "tsaA": {
        "role": "AhpC/Prx1-family thioredoxin peroxidase",
        "description": (
            "tsaA encodes an AhpC/Prx1-family thioredoxin peroxidase in Pseudomonas "
            "putida KT2440. It is a soluble peroxiredoxin-family peroxide-detoxification "
            "enzyme linked to hydrogen peroxide catabolism, cellular oxidant detoxification, "
            "and oxidative-stress response."
        ),
        "primary_function": TERM["GO:0051920"],
        "process": TERM["GO:0098869"],
        "locations": [TERM["GO:0005737"]],
        "new_terms": [],
    },
    "PP_1235": {
        "role": "Bcp/PrxQ thioredoxin-dependent peroxiredoxin",
        "description": (
            "PP_1235 encodes a Bcp/PrxQ-family thioredoxin-dependent peroxiredoxin in "
            "Pseudomonas putida KT2440. The EC mapping, peroxiredoxin-family domains, and "
            "GOA support a cytoplasmic thioredoxin-dependent peroxide-detoxification role."
        ),
        "primary_function": TERM["GO:0140824"],
        "process": TERM["GO:0098869"],
        "locations": [TERM["GO:0005737"]],
        "new_terms": [],
    },
    "ohr": {
        "role": "OsmC/Ohr-family organic hydroperoxide resistance protein",
        "description": (
            "ohr encodes an OsmC/Ohr-family organic hydroperoxide resistance protein in "
            "Pseudomonas putida KT2440. The name, family assignment, and domain evidence "
            "support a peroxide-detoxification role in oxidative-stress defense, with the "
            "exact physiological hydroperoxide substrate still unresolved in this first pass."
        ),
        "primary_function": TERM["GO:0004601"],
        "process": TERM["GO:0098869"],
        "locations": [],
        "new_terms": ["GO:0004601", "GO:0098869"],
    },
    "PP_2943": {
        "role": "periplasmic cytochrome c551 peroxidase",
        "description": (
            "PP_2943 encodes a predicted periplasmic cytochrome c551 peroxidase in "
            "Pseudomonas putida KT2440. GOA and domain evidence support cytochrome-c "
            "peroxidase activity, heme-dependent electron-transfer chemistry, periplasmic "
            "localization, and cellular oxidant detoxification."
        ),
        "primary_function": TERM["GO:0004130"],
        "process": TERM["GO:0098869"],
        "locations": [TERM["GO:0042597"]],
        "new_terms": [],
    },
    "PP_3248": {
        "role": "DyP-type heme peroxidase",
        "description": (
            "PP_3248 encodes a DyP-type peroxidase-family protein in Pseudomonas putida "
            "KT2440. Its domain architecture and GOA support heme-associated peroxidase "
            "activity and cellular oxidant detoxification, while substrate specificity "
            "remains unresolved in this first-pass review."
        ),
        "primary_function": TERM["GO:0004601"],
        "process": TERM["GO:0098869"],
        "locations": [TERM["GO:0005829"]],
        "new_terms": [],
    },
    "tpx": {
        "role": "Tpx-family thioredoxin-dependent peroxiredoxin",
        "description": (
            "tpx encodes the Tpx-family thiol peroxidase/peroxiredoxin in Pseudomonas "
            "putida KT2440. HAMAP and GOA support thioredoxin-dependent peroxiredoxin "
            "activity, peroxide detoxification, and oxidative-stress response context."
        ),
        "primary_function": TERM["GO:0140824"],
        "process": TERM["GO:0098869"],
        "locations": [],
        "new_terms": [],
    },
    "cpo": {
        "role": "non-heme chloride peroxidase",
        "description": (
            "cpo encodes a bacterial non-heme chloroperoxidase/AB-hydrolase-family enzyme "
            "in Pseudomonas putida KT2440. Existing GOA supports chloride peroxidase "
            "activity and cellular oxidant detoxification; this first pass does not assign "
            "a narrower physiological substrate or pathway role."
        ),
        "primary_function": TERM["GO:0016691"],
        "process": TERM["GO:0098869"],
        "locations": [],
        "new_terms": [],
    },
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def read_lines(path: Path) -> list[str]:
    return read_text(path).splitlines()


def first_line(path: Path, *needles: str) -> str:
    for line in read_lines(path):
        if all(needle in line for needle in needles):
            return line
    raise ValueError(f"No line in {path} contains all needles: {needles}")


def optional_first_line(path: Path, *needles: str) -> str | None:
    for line in read_lines(path):
        if all(needle in line for needle in needles):
            return line
    return None


def file_id(gene: str, suffix: str) -> str:
    return f"file:PSEPK/{gene}/{gene}-{suffix}"


def support(reference_id: str, text: str) -> dict[str, str]:
    return {"reference_id": reference_id, "supporting_text": text}


def goa_support(gene: str, term_id: str) -> dict[str, str] | None:
    goa = GENE_ROOT / gene / f"{gene}-goa.tsv"
    line = optional_first_line(goa, term_id)
    if not line:
        return None
    return support(file_id(gene, "goa.tsv"), line)


def uniprot_evidence(gene: str) -> list[dict[str, str]]:
    uniprot = GENE_ROOT / gene / f"{gene}-uniprot.txt"
    data = [support(file_id(gene, "uniprot.txt"), first_line(uniprot, "DE   "))]
    for marker in (
        ("CC   -!- FUNCTION:",),
        ("CC   -!- SUBCELLULAR LOCATION:",),
        ("CC   -!- SIMILARITY:",),
        ("DR   InterPro;",),
        ("DR   Pfam;",),
        ("FT   ACT_SITE",),
        ("FT   BINDING",),
    ):
        line = optional_first_line(uniprot, *marker)
        if line and line not in {item["supporting_text"] for item in data}:
            data.append(support(file_id(gene, "uniprot.txt"), line))
    return data


def asta_evidence(gene: str) -> list[dict[str, str]]:
    asta = GENE_ROOT / gene / f"{gene}-deep-research-asta.md"
    data = [support(file_id(gene, "deep-research-asta.md"), first_line(asta, "  protein_description:"))]
    for marker in ("  protein_family:", "  protein_domains:"):
        line = optional_first_line(asta, marker)
        if line:
            data.append(support(file_id(gene, "deep-research-asta.md"), line))
    return data


def standard_support(gene: str, term_id: str | None = None) -> list[dict[str, str]]:
    data: list[dict[str, str]] = []
    if term_id:
        goa = goa_support(gene, term_id)
        if goa:
            data.append(goa)
    data.extend(uniprot_evidence(gene))
    data.extend(asta_evidence(gene))
    return data


def reference_list(existing_refs: list[dict], gene: str, accession: str) -> list[dict]:
    refs: list[dict] = []
    seen = set()
    for ref in existing_refs:
        ref_id = ref["id"]
        seen.add(ref_id)
        refs.append(ref)
    titles = {
        file_id(gene, "goa.tsv"): f"QuickGO GOA annotations for {gene} ({accession})",
        file_id(gene, "uniprot.txt"): f"UniProtKB entry for {gene} ({accession})",
        file_id(gene, "deep-research-asta.md"): f"Asta retrieval report for {gene} ({accession})",
    }
    for ref_id, title in titles.items():
        if ref_id not in seen:
            refs.append({"id": ref_id, "title": title, "findings": []})
    return refs


def replacement(term_id: str) -> list[dict[str, str]]:
    return [TERM[term_id]]


def accept_review(gene: str, term_id: str, summary: str, reason: str) -> dict:
    return {
        "summary": summary,
        "action": "ACCEPT",
        "reason": reason,
        "supported_by": standard_support(gene, term_id),
    }


def keep_review(gene: str, term_id: str, summary: str, reason: str) -> dict:
    return {
        "summary": summary,
        "action": "KEEP_AS_NON_CORE",
        "reason": reason,
        "supported_by": standard_support(gene, term_id),
    }


def modify_review(gene: str, term_id: str, replacement_term_id: str, summary: str, reason: str) -> dict:
    return {
        "summary": summary,
        "action": "MODIFY",
        "reason": reason,
        "proposed_replacement_terms": replacement(replacement_term_id),
        "supported_by": standard_support(gene, term_id),
    }


def review_for_annotation(gene: str, term_id: str) -> dict:
    info = GENE_INFO[gene]
    primary = info["primary_function"]["id"]
    primary_label = info["primary_function"]["label"]
    role = info["role"]

    if term_id == primary:
        return accept_review(
            gene,
            term_id,
            f"{primary_label} is the core molecular function supported for this {role}.",
            "The UniProt product/family context, domain evidence, Asta retrieval metadata, and GOA row converge on this catalytic role.",
        )

    if term_id == "GO:0004601":
        return modify_review(
            gene,
            term_id,
            primary,
            "The annotation is directionally correct but less specific than the supported peroxiredoxin-family function.",
            f"{gene} is resolved as a {role}; the more specific {primary_label} term captures the catalytic identity better than broad peroxidase activity.",
        )

    if term_id == "GO:0008379":
        if gene == "tsaA":
            return accept_review(
                gene,
                term_id,
                "Thioredoxin peroxidase activity is consistent with the TsaA product name and peroxiredoxin-family assignment.",
                "The annotation is a reasonable molecular-function statement for this thioredoxin-peroxidase-family protein.",
            )
        return modify_review(
            gene,
            term_id,
            primary,
            "The annotation is plausible but less specific than the thioredoxin-dependent peroxiredoxin term already present.",
            f"The EC/family evidence supports {primary_label} as the sharper molecular-function statement.",
        )

    if term_id in {"GO:0016491", "GO:0016684"}:
        return modify_review(
            gene,
            term_id,
            primary,
            "The oxidoreductase annotation is correct at a high level but too broad for this family-resolved peroxide-detoxification enzyme.",
            f"Use {primary_label} as the informative molecular-function term for this first-pass review.",
        )

    if term_id == "GO:0016209":
        return keep_review(
            gene,
            term_id,
            "Antioxidant activity is biologically consistent but broad compared with the catalytic peroxidase/peroxiredoxin annotation.",
            "Keep the row as secondary context, but do not treat the parent antioxidant term as the core function.",
        )

    if term_id == "GO:0098869":
        return accept_review(
            gene,
            term_id,
            "Cellular oxidant detoxification captures the direct biological-process role of this peroxide-detoxification enzyme.",
            "The protein family and GOA evidence support a direct role in enzymatic oxidant removal.",
        )

    if term_id in {"GO:0006979", "GO:0034599", "GO:0033554"}:
        return keep_review(
            gene,
            term_id,
            "The stress-response annotation is consistent with peroxide-detoxification biology but broader than the direct enzyme activity.",
            "The direct function is oxidant detoxification; response-to-stress terms are retained as secondary physiological context.",
        )

    if term_id == "GO:0042744":
        return accept_review(
            gene,
            term_id,
            "Hydrogen peroxide catabolic process is a supported process context for this peroxiredoxin-family enzyme.",
            "The family and GOA evidence support peroxide reduction; broader oxidant detoxification remains the preferred summary process.",
        )

    if term_id == "GO:0045454":
        return keep_review(
            gene,
            term_id,
            "Cell redox homeostasis is plausible context but broader than the direct peroxide-detoxification role.",
            "Keep as non-core because the enzyme acts through a specific peroxidase/peroxiredoxin activity.",
        )

    if term_id in {"GO:0005737", "GO:0005829", "GO:0042597"}:
        return accept_review(
            gene,
            term_id,
            "The localization row is compatible with the protein class and current GOA evidence.",
            "Use the existing localization as supporting context for the catalytic role; it is not by itself the pathway-defining function.",
        )

    if term_id == "GO:0020037":
        return keep_review(
            gene,
            term_id,
            "Heme binding is supported cofactor context for this peroxidase-family protein.",
            "Keep as non-core because the catalytic peroxidase activity is the primary functional statement.",
        )

    if term_id == "GO:0009055":
        return keep_review(
            gene,
            term_id,
            "Electron transfer activity is consistent with cytochrome-c peroxidase chemistry but is less informative than the specific peroxidase term.",
            "Keep as non-core cofactor/redox-cycle context for the cytochrome-c peroxidase.",
        )

    if term_id == "GO:0042802":
        return keep_review(
            gene,
            term_id,
            "The experimental identical-protein-binding annotation is retained as non-core oligomerization context.",
            "Do not overinterpret the IPI row as a pathway-level function; the catalytic peroxidase activity remains the core role.",
        )

    raise ValueError(f"No review rule for {gene} {term_id}")


def new_annotation(gene: str, term_id: str, qualifier: str) -> dict:
    info = GENE_INFO[gene]
    term = TERM[term_id]
    return {
        "term": term,
        "evidence_type": "IEA",
        "original_reference_id": file_id(gene, "uniprot.txt"),
        "qualifier": qualifier,
        "review": {
            "summary": f"First-pass evidence supports adding {term['label']} for this {info['role']}.",
            "action": "NEW",
            "reason": (
                "The current GOA rows understate the direct detoxification role; UniProt product/family evidence and "
                "Asta retrieval metadata support this conservative addition."
            ),
            "supported_by": standard_support(gene, None),
        },
    }


def core_for(gene: str) -> dict:
    info = GENE_INFO[gene]
    core = {
        "description": info["role"],
        "molecular_function": info["primary_function"],
        "directly_involved_in": [info["process"]],
        "supported_by": standard_support(gene, info["primary_function"]["id"]),
    }
    if info["locations"]:
        core["locations"] = info["locations"]
    return core


def apply_review(gene: str, accession: str) -> None:
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(read_text(path))
    data["gene_symbol"] = gene
    data["status"] = "DRAFT"
    data["description"] = GENE_INFO.get(gene, {}).get("description", data.get("description"))
    data["references"] = reference_list(data.get("references") or [], gene, accession)

    if gene == "ahpC":
        data["references"] = reference_list(data.get("references") or [], gene, accession)
        supported_by = data["core_functions"][0].setdefault("supported_by", [])
        for item in asta_evidence(gene):
            if item not in supported_by:
                supported_by.append(item)
    else:
        existing = data.get("existing_annotations") or []
        retained = []
        seen_new = {
            annotation.get("term", {}).get("id")
            for annotation in existing
            if annotation.get("review", {}).get("action") == "NEW"
        }
        for annotation in existing:
            if annotation.get("review", {}).get("action") == "NEW":
                retained.append(annotation)
                continue
            term_id = annotation["term"]["id"]
            annotation["review"] = review_for_annotation(gene, term_id)
            retained.append(annotation)
        for term_id in GENE_INFO[gene]["new_terms"]:
            if term_id in seen_new:
                continue
            qualifier = "enables" if term_id.startswith("GO:0004") else "involved_in"
            retained.append(new_annotation(gene, term_id, qualifier))
        data["existing_annotations"] = retained
        data["core_functions"] = [core_for(gene)]

    data["proposed_new_terms"] = []
    data["suggested_questions"] = [
        {
            "question": (
                f"What are the in vivo oxidant substrates, electron donor partners, and stress conditions that most strongly "
                f"depend on {gene} in Pseudomonas putida KT2440?"
            )
        }
    ]
    data["suggested_experiments"] = [
        {
            "description": (
                f"Purify {gene} and assay peroxide, organic hydroperoxide, and donor-coupled activity with candidate reductants "
                "or redox partners, then test a clean deletion strain under matched oxidative-stress conditions."
            ),
            "experiment_type": "enzyme kinetics and targeted oxidative-stress phenotyping",
        }
    ]
    path.write_text(yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, width=120), encoding="utf-8")


def write_notes(gene: str, accession: str) -> None:
    info = GENE_INFO.get(gene)
    if gene == "ahpC":
        summary = (
            "Backfilled Asta retrieval for the pre-existing ahpC review and retained the prior deeper curation. "
            "ahpC remains the AhpCF-system peroxiredoxin component, with donor-specific NADH dependence treated as "
            "system-level AhpCF context rather than a single-subunit molecular function."
        )
    else:
        summary = info["description"]
    evidence = standard_support(gene, info["primary_function"]["id"] if info else None)
    lines = [
        f"# {gene} notes",
        "",
        "2026-07-10: First-pass peroxide/peroxiredoxin stress-detoxification curation.",
        summary,
        "",
        "Primary provenance:",
    ]
    for item in evidence[:5]:
        lines.append(f"- [{item['reference_id']} \"{item['supporting_text']}\"]")
    lines.extend(
        [
            "",
            "Decision: represent this gene in the oxidative-stress/peroxide-detoxification boundary. Keep broad stress-response, "
            "redox-homeostasis, antioxidant, electron-transfer, and cofactor-binding rows as non-core context when they are not "
            "the most informative functional statement.",
        ]
    )
    (GENE_ROOT / gene / f"{gene}-notes.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    with BATCH_TSV.open(encoding="utf-8") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            gene = row["gene"]
            accession = row["uniprot_accession"]
            apply_review(gene, accession)
            write_notes(gene, accession)
            print(f"Curated {gene}")


if __name__ == "__main__":
    main()
