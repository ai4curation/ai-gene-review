#!/usr/bin/env python3
"""First-pass curate the PSEPK miscellaneous stress/detoxification spillover split."""

from __future__ import annotations

import csv
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes" / "PSEPK"
BATCH_DIR = ROOT / "projects" / "P_PUTIDA" / "batches"
BATCH_TSV = BATCH_DIR / "module_stress_detoxification_stress_regulatory_or_misc_spillovers.tsv"
PARTITION_TSV = BATCH_DIR / "module_stress_detoxification_partition.tsv"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


TERM = {
    "GO:0000287": {"id": "GO:0000287", "label": "magnesium ion binding"},
    "GO:0003677": {"id": "GO:0003677", "label": "DNA binding"},
    "GO:0004322": {"id": "GO:0004322", "label": "ferroxidase activity"},
    "GO:0004674": {"id": "GO:0004674", "label": "protein serine/threonine kinase activity"},
    "GO:0005524": {"id": "GO:0005524", "label": "ATP binding"},
    "GO:0005737": {"id": "GO:0005737", "label": "cytoplasm"},
    "GO:0008199": {"id": "GO:0008199", "label": "ferric iron binding"},
    "GO:0010124": {"id": "GO:0010124", "label": "phenylacetate catabolic process"},
    "GO:0016289": {"id": "GO:0016289", "label": "acyl-CoA hydrolase activity"},
    "GO:0016722": {"id": "GO:0016722", "label": "oxidoreductase activity, acting on metal ions"},
    "GO:0046677": {"id": "GO:0046677", "label": "response to antibiotic"},
    "GO:0098869": {"id": "GO:0098869", "label": "cellular oxidant detoxification"},
    "GO:0106310": {"id": "GO:0106310", "label": "protein serine kinase activity"},
    "GO:1904975": {"id": "GO:1904975", "label": "response to bleomycin"},
}


GENE_INFO = {
    "srkA": {
        "accession": "Q88QX5",
        "role": "stress-response Ser/Thr protein kinase",
        "description": (
            "srkA (PP_0359) encodes Stress response kinase A, a soluble cytoplasmic "
            "SrkA/RdoA-family protein kinase in Pseudomonas putida KT2440. UniRule, "
            "Rhea, and family/domain evidence support ATP- and magnesium-dependent "
            "phosphorylation of serine/threonine protein substrates, but this first pass "
            "does not resolve the physiological substrates or the precise stress-signaling "
            "pathway controlled by the kinase."
        ),
        "core": [
            {
                "description": "Cytoplasmic ATP- and magnesium-dependent Ser/Thr protein kinase candidate",
                "molecular_function": TERM["GO:0004674"],
                "locations": [TERM["GO:0005737"]],
                "support_term": "GO:0004674",
            }
        ],
        "new_terms": [],
    },
    "dps": {
        "accession": "Q88NJ7",
        "role": "Dps-family DNA-binding ferroxidase stress protein",
        "description": (
            "dps (PP_1210) encodes a Dps/ferritin-like stress protein in Pseudomonas "
            "putida KT2440. The protein has a ferritin/Dps domain, EC-derived "
            "ferroxidase activity, ferric-iron-binding annotation, and UniProt/domain "
            "support for DNA binding. In this first pass it is curated as a Dps-family "
            "iron-sequestration and DNA-binding stress protein rather than as a fully "
            "experimentally characterized KT2440 DNA-protection factor."
        ),
        "core": [
            {
                "description": "Dps-family ferritin-like ferroxidase/iron-binding stress protein",
                "molecular_function": TERM["GO:0004322"],
                "support_term": "GO:0004322",
            },
            {
                "description": "Dps-family DNA-binding activity inferred from protein name, keyword, and Dps domain evidence",
                "molecular_function": TERM["GO:0003677"],
                "support_term": "GO:0003677",
            },
        ],
        "new_terms": ["GO:0003677"],
    },
    "PP_3269": {
        "accession": "Q88HT4",
        "role": "low-information KGG-repeat stress-induced protein",
        "description": (
            "PP_3269 encodes a small predicted stress-induced KGG-repeat protein in "
            "Pseudomonas putida KT2440. The current fetched metadata gives only the "
            "Stress-induced_KGG_rpt/PF10685 family signature and no GOA molecular "
            "function, process, or localization. The first-pass curation therefore leaves "
            "the gene without a proposed GO function pending family- or organism-specific "
            "evidence."
        ),
        "core": [],
        "new_terms": [],
    },
    "paaY": {
        "accession": "Q88HR8",
        "role": "phenylacetate-pathway detoxifying thioesterase candidate",
        "description": (
            "paaY (PP_3285) encodes a predicted detoxifying thioesterase associated with "
            "the phenylacetate degradation pathway in Pseudomonas putida KT2440. The "
            "protein is assigned to PaaY/hexapeptide-repeat/LpxA-like families. Because "
            "the current GOA block is empty, the first pass proposes a conservative "
            "acyl-CoA hydrolase molecular function and phenylacetate-catabolism process "
            "context rather than a more specific experimentally unresolved substrate call."
        ),
        "core": [
            {
                "description": "Predicted PaaY-family acyl-CoA/thioester hydrolase in phenylacetate catabolism",
                "molecular_function": TERM["GO:0016289"],
                "directly_involved_in": [TERM["GO:0010124"]],
                "support_term": None,
            }
        ],
        "new_terms": ["GO:0016289", "GO:0010124"],
    },
    "PP_3509": {
        "accession": "Q88H56",
        "role": "bleomycin-resistance-family antibiotic-response protein",
        "description": (
            "PP_3509 encodes a small VOC-domain bleomycin-resistance-family protein in "
            "Pseudomonas putida KT2440. UniProt/InterPro metadata supports antibiotic "
            "response context through the Bleomycin-R family and antibiotic-resistance "
            "keyword, but no precise molecular function is resolved in the fetched data. "
            "The first pass retains the broad response-to-antibiotic annotation and "
            "suggests the more specific response-to-bleomycin process as a conservative "
            "family-based refinement."
        ),
        "core": [
            {
                "description": "Bleomycin-resistance-family protein associated with antibiotic/bleomycin response",
                "directly_involved_in": [TERM["GO:1904975"]],
                "support_term": "GO:0046677",
            }
        ],
        "new_terms": ["GO:1904975"],
    },
    "PP_3963": {
        "accession": "Q88FW4",
        "role": "low-information KGG-repeat stress-induced protein",
        "description": (
            "PP_3963 encodes a predicted stress-induced KGG-repeat protein in Pseudomonas "
            "putida KT2440. The current metadata supports only the Stress-induced_KGG_rpt/"
            "PF10685 family signature, with no fetched GOA rows and no specific function. "
            "The first-pass curation records it as an unresolved stress-induced protein "
            "rather than adding unsupported GO terms."
        ),
        "core": [],
        "new_terms": [],
    },
    "PP_5593": {
        "accession": "A0A140FWE1",
        "role": "low-information KGG-repeat stress-induced protein",
        "description": (
            "PP_5593 encodes a small predicted stress-induced KGG-repeat protein in "
            "Pseudomonas putida KT2440. Available metadata is limited to the "
            "Stress-induced_KGG_rpt/PF10685 family signature and no GOA rows, so this "
            "first pass leaves molecular function and process unresolved."
        ),
        "core": [],
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


def first_prefixed_lines(path: Path, prefix: str, limit: int = 4) -> list[str]:
    return [line for line in read_lines(path) if line.startswith(prefix)][:limit]


def file_id(gene: str, suffix: str) -> str:
    return f"file:PSEPK/{gene}/{gene}-{suffix}"


def support(reference_id: str, text: str) -> dict[str, str]:
    return {"reference_id": reference_id, "supporting_text": text}


def add_unique(items: list[dict[str, str]], item: dict[str, str] | None) -> None:
    if item and item["supporting_text"] not in {existing["supporting_text"] for existing in items}:
        items.append(item)


def goa_support(gene: str, term_id: str) -> dict[str, str] | None:
    line = optional_first_line(GENE_ROOT / gene / f"{gene}-goa.tsv", term_id)
    if not line:
        return None
    return support(file_id(gene, "goa.tsv"), line)


def uniprot_evidence(gene: str, term_id: str | None = None) -> list[dict[str, str]]:
    uniprot = GENE_ROOT / gene / f"{gene}-uniprot.txt"
    data = [support(file_id(gene, "uniprot.txt"), first_line(uniprot, "DE   "))]
    if term_id:
        line = optional_first_line(uniprot, f"DR   GO; {term_id};")
        if line:
            add_unique(data, support(file_id(gene, "uniprot.txt"), line))
    for marker in (
        ("CC   -!- FUNCTION:",),
        ("CC   -!- SUBCELLULAR LOCATION:",),
        ("CC   -!- SIMILARITY:",),
        ("DR   CDD;",),
        ("DR   NCBIfam;",),
        ("DR   PANTHER;",),
        ("DR   Pfam;",),
        ("KW   ",),
        ("FT   DOMAIN",),
    ):
        if gene == "paaY" and marker == ("DR   PANTHER;",):
            continue
        line = optional_first_line(uniprot, *marker)
        if line and line.startswith("KW   ") and "Reference proteome" in line:
            continue
        if line:
            add_unique(data, support(file_id(gene, "uniprot.txt"), line))
    for line in first_prefixed_lines(uniprot, "DR   InterPro;", 5):
        add_unique(data, support(file_id(gene, "uniprot.txt"), line))
    return data


def asta_evidence(gene: str) -> list[dict[str, str]]:
    asta = GENE_ROOT / gene / f"{gene}-deep-research-asta.md"
    data = [support(file_id(gene, "deep-research-asta.md"), first_line(asta, "  uniprot_accession:"))]
    for marker in ("  protein_description:", "  protein_family:", "  protein_domains:"):
        line = optional_first_line(asta, marker)
        if line and "Not specified in UniProt" in line:
            continue
        if line:
            add_unique(data, support(file_id(gene, "deep-research-asta.md"), line))
    return data


def standard_support(gene: str, term_id: str | None = None) -> list[dict[str, str]]:
    data: list[dict[str, str]] = []
    if term_id:
        add_unique(data, goa_support(gene, term_id))
    for item in uniprot_evidence(gene, term_id):
        add_unique(data, item)
    for item in asta_evidence(gene):
        add_unique(data, item)
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


def review_for_annotation(gene: str, term_id: str) -> dict:
    if gene == "srkA":
        summaries = {
            "GO:0000287": "Magnesium binding is a cofactor annotation consistent with the UniRule SrkA kinase model.",
            "GO:0004674": "Protein serine/threonine kinase activity is the defining SrkA/RdoA-family molecular function.",
            "GO:0005524": "ATP binding is required for the kinase reaction and is supported by the UniRule kinase model.",
            "GO:0005737": "Cytoplasmic localization is consistent with the UniProt subcellular-location annotation.",
            "GO:0106310": "Protein serine kinase activity is a Rhea-derived kinase-reaction annotation compatible with SrkA function.",
        }
        return {
            "summary": summaries[term_id],
            "action": "ACCEPT",
            "reason": (
                "The GOA row matches the UniProt/HAMAP SrkA/RdoA-family kinase annotation and supporting "
                "domain/family evidence. The first pass accepts the activity/cofactor/localization terms "
                "without asserting specific physiological substrates."
            ),
            "supported_by": standard_support(gene, term_id),
        }
    if gene == "dps":
        if term_id == "GO:0016722":
            return {
                "summary": "This broad oxidoreductase parent is compatible with Dps ferroxidase activity but less informative.",
                "action": "MARK_AS_OVER_ANNOTATED",
                "reason": (
                    "The row is not biologically contradictory, but GO:0004322 ferroxidase activity is already present "
                    "and captures the direct Dps-family redox activity more specifically."
                ),
                "supported_by": standard_support(gene, term_id),
            }
        summaries = {
            "GO:0004322": "Ferroxidase activity is supported by the EC 1.16.3.1 annotation and ferritin/Dps domain context.",
            "GO:0008199": "Ferric iron binding is consistent with the ferritin/Dps domain assignment.",
        }
        return {
            "summary": summaries[term_id],
            "action": "ACCEPT",
            "reason": (
                "The term matches the Dps/ferritin-like protein identity and the fetched UniProt/InterPro evidence. "
                "It is retained as part of the Dps-family iron-handling stress function."
            ),
            "supported_by": standard_support(gene, term_id),
        }
    if gene == "PP_3509" and term_id == "GO:0046677":
        return {
            "summary": "Response to antibiotic is appropriate broad process context for a bleomycin-resistance-family protein.",
            "action": "ACCEPT",
            "reason": (
                "The InterPro/UniProt evidence supports the Bleomycin-R family and antibiotic-resistance keyword. "
                "The row is broad but reasonable; a more specific response-to-bleomycin recommendation is added separately."
            ),
            "supported_by": standard_support(gene, term_id),
        }
    raise ValueError(f"No review rule for {gene} {term_id}")


def new_annotation(gene: str, term_id: str) -> dict:
    term = TERM[term_id]
    qualifier = "enables" if term_id in {"GO:0003677", "GO:0016289"} else "involved_in"
    if gene == "dps":
        reason = (
            "The GOA fetch omitted DNA binding, but UniProt lists a DNA-binding GO cross-reference and keyword, and "
            "the protein is a Dps-family DNA-binding stress protein with DPS_DNA-bd/DPS consensus signatures."
        )
    elif gene == "paaY":
        reason = (
            "The GOA fetch is empty, but the UniProt protein name identifies PaaY as a detoxifying thioesterase of the "
            "phenylacetate degradation pathway and the family/domain block includes PaaY/hexapeptide-repeat evidence. "
            "GO:0016289 and GO:0010124 are conservative, broad recommendations that avoid over-specifying the exact "
            "phenylacetate-pathway CoA thioester substrate."
        )
    elif gene == "PP_3509":
        reason = (
            "The existing GOA row gives the parent response-to-antibiotic term. The UniProt/InterPro evidence names a "
            "bleomycin-resistance protein/family, so response to bleomycin is a reasonable more specific process "
            "recommendation pending direct KT2440 testing."
        )
    else:
        raise ValueError(f"No NEW annotation rule for {gene} {term_id}")
    return {
        "term": term,
        "evidence_type": "IEA",
        "original_reference_id": file_id(gene, "uniprot.txt"),
        "qualifier": qualifier,
        "review": {
            "summary": f"First-pass evidence supports adding {term['label']} for this {GENE_INFO[gene]['role']}.",
            "action": "NEW",
            "reason": reason,
            "supported_by": standard_support(gene, term_id),
        },
    }


def core_functions(gene: str) -> list[dict]:
    cores = []
    for item in GENE_INFO[gene]["core"]:
        core = {
            "description": item["description"],
            "supported_by": standard_support(gene, item.get("support_term")),
        }
        for key in ("molecular_function", "directly_involved_in", "locations"):
            if key in item:
                core[key] = item[key]
        cores.append(core)
    return cores


def apply_review(gene: str) -> None:
    info = GENE_INFO[gene]
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(read_text(path))
    data["gene_symbol"] = gene
    data["status"] = "DRAFT"
    data["description"] = info["description"]
    data["references"] = reference_list(data.get("references") or [], gene, info["accession"])
    existing = data.get("existing_annotations") or []
    for annotation in existing:
        term_id = annotation["term"]["id"]
        if term_id in info["new_terms"]:
            annotation.update(new_annotation(gene, term_id))
        else:
            annotation["review"] = review_for_annotation(gene, term_id)
    for term_id in info["new_terms"]:
        if term_id not in {annotation["term"]["id"] for annotation in existing}:
            existing.append(new_annotation(gene, term_id))
    data["existing_annotations"] = existing
    data["core_functions"] = core_functions(gene)
    data["proposed_new_terms"] = []
    data["suggested_questions"] = suggested_questions(gene)
    data["suggested_experiments"] = suggested_experiments(gene)
    path.write_text(yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, width=120), encoding="utf-8")


def suggested_questions(gene: str) -> list[dict[str, object]]:
    if gene == "srkA":
        text = "What are the direct SrkA substrates and stress inputs in KT2440?"
    elif gene == "dps":
        text = "Under which stresses does KT2440 Dps bind/protect DNA in vivo, and how much protection depends on ferroxidase activity?"
    elif gene == "paaY":
        text = "Which phenylacetate-pathway CoA thioesters are hydrolyzed by KT2440 PaaY in vivo?"
    elif gene == "PP_3509":
        text = "Does PP_3509 confer bleomycin resistance in KT2440, and is the mechanism ligand sequestration or another VOC-domain activity?"
    else:
        text = f"What is the biochemical or cellular role of the KGG-repeat stress-induced protein {gene}?"
    return [{"question": text, "experts": []}]


def suggested_experiments(gene: str) -> list[dict[str, str]]:
    if gene == "srkA":
        return [
            {
                "experiment_type": "phosphoproteomics",
                "description": "Compare wild-type and srkA deletion/kinase-dead strains under stress conditions to identify direct or proximal phosphorylation targets.",
            }
        ]
    if gene == "dps":
        return [
            {
                "experiment_type": "oxidative-stress and DNA-binding assays",
                "description": "Assay purified Dps for ferroxidase activity and DNA binding, and compare wild-type and dps deletion strains under peroxide and iron stress.",
            }
        ]
    if gene == "paaY":
        return [
            {
                "experiment_type": "thioesterase substrate panel",
                "description": "Purify PaaY and test hydrolysis of phenylacetate-pathway acyl-CoA intermediates, then measure phenylacetate growth and intermediate accumulation in a paaY mutant.",
            }
        ]
    if gene == "PP_3509":
        return [
            {
                "experiment_type": "antibiotic-resistance assay",
                "description": "Compare bleomycin susceptibility of wild-type, PP_3509 deletion, and complemented strains and test bleomycin binding by purified PP_3509.",
            }
        ]
    return []


def write_notes(gene: str) -> None:
    path = GENE_ROOT / gene / f"{gene}-notes.md"
    info = GENE_INFO[gene]
    evidence = standard_support(gene, None)
    if gene == "dps":
        evidence = standard_support(gene, "GO:0004322") + standard_support(gene, "GO:0003677")
    elif gene == "srkA":
        evidence = standard_support(gene, "GO:0004674")
    elif gene == "PP_3509":
        evidence = standard_support(gene, "GO:0046677")
    lines = [
        f"# {gene} notes",
        "",
        "2026-07-10: First-pass miscellaneous stress/detoxification spillover curation.",
        info["description"],
        "",
        "Primary provenance:",
    ]
    seen = set()
    for item in evidence:
        key = (item["reference_id"], item["supporting_text"])
        if key in seen or not item["supporting_text"]:
            continue
        seen.add(key)
        lines.append(f"- [{item['reference_id']} \"{item['supporting_text']}\"]")
        if len(seen) >= 10:
            break
    lines.extend(["", f"Decision: {decision_text(gene)}", ""])
    path.write_text("\n".join(lines), encoding="utf-8")


def decision_text(gene: str) -> str:
    if gene == "srkA":
        return "accept kinase, ATP, magnesium, and cytoplasm annotations; do not assert substrates or a specific stress pathway yet."
    if gene == "dps":
        return "accept Dps ferroxidase/iron-binding evidence, mark the broad oxidoreductase parent as over-annotated, and add DNA binding."
    if gene == "paaY":
        return "add conservative acyl-CoA hydrolase and phenylacetate catabolic process recommendations from PaaY/thioesterase context."
    if gene == "PP_3509":
        return "accept response to antibiotic and add a more specific response-to-bleomycin recommendation; no molecular function is asserted."
    return "record as a low-information KGG-repeat stress-induced protein with no proposed GO function in this first pass."


def update_partition() -> None:
    rows = list(csv.DictReader(PARTITION_TSV.open(), delimiter="\t"))
    for row in rows:
        if row["partition_bucket"] == "stress_regulatory_or_misc_spillovers":
            row["recommended_action"] = "COMPLETED_SUBMODULE"
            row["bucket_status"] = "CURATED"
            gene = row["gene"]
            review = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
            asta = GENE_ROOT / gene / f"{gene}-deep-research-asta.md"
            row["review_status"] = "CURATED" if review.exists() else "MISSING"
            row["curation_status"] = "CURATED" if review.exists() else "MISSING"
            row["asta_research_status"] = "PRESENT" if asta.exists() else "MISSING"
    with PARTITION_TSV.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys(), delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    for gene in GENE_INFO:
        apply_review(gene)
        write_notes(gene)
    update_partition()


if __name__ == "__main__":
    main()
