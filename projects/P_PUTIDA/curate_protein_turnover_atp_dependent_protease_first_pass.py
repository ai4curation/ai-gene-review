#!/usr/bin/env python3
"""First-pass curate the PSEPK ATP-dependent protease/protein-turnover split."""

from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes" / "PSEPK"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


TERM = {
    "GO:0004176": {"id": "GO:0004176", "label": "ATP-dependent peptidase activity"},
    "GO:0004252": {"id": "GO:0004252", "label": "serine-type endopeptidase activity"},
    "GO:0004298": {"id": "GO:0004298", "label": "threonine-type endopeptidase activity"},
    "GO:0005524": {"id": "GO:0005524", "label": "ATP binding"},
    "GO:0005737": {"id": "GO:0005737", "label": "cytoplasm"},
    "GO:0005829": {"id": "GO:0005829", "label": "cytosol"},
    "GO:0005840": {"id": "GO:0005840", "label": "ribosome"},
    "GO:0006508": {"id": "GO:0006508", "label": "proteolysis"},
    "GO:0006515": {
        "id": "GO:0006515",
        "label": "protein quality control for misfolded or incompletely synthesized proteins",
    },
    "GO:0008233": {"id": "GO:0008233", "label": "peptidase activity"},
    "GO:0009368": {"id": "GO:0009368", "label": "endopeptidase Clp complex"},
    "GO:0009376": {"id": "GO:0009376", "label": "HslUV protease complex"},
    "GO:0010498": {"id": "GO:0010498", "label": "proteasomal protein catabolic process"},
    "GO:0016887": {"id": "GO:0016887", "label": "ATP hydrolysis activity"},
    "GO:0030163": {"id": "GO:0030163", "label": "protein catabolic process"},
    "GO:0034605": {"id": "GO:0034605", "label": "cellular response to heat"},
    "GO:0036402": {"id": "GO:0036402", "label": "proteasome-activating activity"},
    "GO:0043335": {"id": "GO:0043335", "label": "protein unfolding"},
    "GO:0043565": {"id": "GO:0043565", "label": "sequence-specific DNA binding"},
    "GO:0045732": {"id": "GO:0045732", "label": "positive regulation of protein catabolic process"},
    "GO:0051117": {"id": "GO:0051117", "label": "ATPase binding"},
    "GO:0061135": {"id": "GO:0061135", "label": "endopeptidase regulator activity"},
}


DESCRIPTIONS = {
    "PP_0680": (
        "PP_0680 is a predicted Lon/peptidase S16-family ATP-dependent endopeptidase in Pseudomonas putida KT2440. "
        "It contains Lon-family ATPase/proteolytic domain signatures and is annotated as endopeptidase La, supporting "
        "a conservative role in ATP-dependent proteolysis and protein catabolic process."
    ),
    "sspB": (
        "SspB is a predicted ClpXP protease specificity-enhancing factor. It is an SspB-family adaptor/regulator "
        "that promotes delivery of tagged protein substrates to the ClpXP degradation machinery rather than acting "
        "as a peptidase itself."
    ),
    "lon-I": (
        "lon-I encodes a cytoplasmic Lon/ATP-dependent protease La homolog. The full-length peptidase S16 protein "
        "contains AAA+ ATPase and Lon proteolytic domains and supports ATP-dependent degradation of abnormal, "
        "misfolded, or regulatory proteins during stress-linked protein quality control."
    ),
    "clpP": (
        "ClpP is a cytoplasmic Clp protease proteolytic subunit. It forms the ClpP proteolytic chamber and cleaves "
        "protein or peptide substrates in cooperation with ATPase partners, contributing to degradation of misfolded "
        "proteins and general protein turnover."
    ),
    "lon-II": (
        "lon-II encodes a second cytoplasmic Lon/ATP-dependent protease La homolog. Like lon-I, it contains AAA+ "
        "ATPase and Lon protease domains and is best curated as an ATP-dependent serine protease involved in protein "
        "quality control and stress-linked protein turnover."
    ),
    "PP_3045": (
        "PP_3045 is a ClpP-family proteolytic subunit candidate. Domain and GOA evidence support a Clp complex "
        "protease subunit that binds ATPase partners and participates in misfolded-protein quality control, although "
        "its exact partner specificity is unresolved."
    ),
    "PP_3267": (
        "PP_3267 is a short predicted ClpP/TepA-family protease-domain protein with no fetched GOA rows. The local "
        "UniProt record carries ClpP/TepA and CLP_protease domain evidence, supporting only a conservative generic "
        "peptidase/proteolysis call in this first pass."
    ),
    "clpA": (
        "ClpA is a ClpA/ClpB-family AAA+ ATPase and unfoldase component of ATP-dependent protein turnover systems. "
        "The supported first-pass role is ATP hydrolysis-driven unfolding or delivery of substrates, not intrinsic "
        "serine endopeptidase catalysis, which belongs to associated ClpP proteolytic subunits."
    ),
    "PP_4814": (
        "PP_4814 is a small Lon N-terminal-domain protein. Current metadata supports a Lon substrate-binding-domain "
        "context, but the protein lacks clear AAA+ ATPase and Lon proteolytic-domain evidence, so no peptidase or "
        "protein-catabolic core function is assigned in this first pass."
    ),
    "hslV": (
        "HslV is the catalytic protease subunit of the bacterial HslUV protease complex. It is a cytoplasmic "
        "proteasome-like threonine endopeptidase activated by HslU and participates in ATP-dependent protein "
        "catabolism."
    ),
    "hslU": (
        "HslU is the AAA+ ATPase/unfoldase and proteasome-activating subunit of the HslUV protease complex. It "
        "uses ATP binding and hydrolysis to recognize and unfold protein substrates before HslV-mediated hydrolysis; "
        "it is not the catalytic peptidase subunit."
    ),
}


def read_lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8").splitlines()


def optional_first_line(path: Path, *needles: str) -> str | None:
    for line in read_lines(path):
        if all(needle in line for needle in needles):
            return line
    return None


def first_line(path: Path, *needles: str) -> str:
    line = optional_first_line(path, *needles)
    if line is None:
        raise ValueError(f"No line in {path} contains all needles: {needles}")
    return line


def file_id(gene: str, suffix: str) -> str:
    return f"file:PSEPK/{gene}/{gene}-{suffix}"


def support(reference_id: str, text: str) -> dict[str, str]:
    return {"reference_id": reference_id, "supporting_text": text}


def add_unique(items: list[dict[str, str]], item: dict[str, str] | None) -> None:
    if not item:
        return
    key = (item["reference_id"], item["supporting_text"])
    if key not in {(existing["reference_id"], existing["supporting_text"]) for existing in items}:
        items.append(item)


def goa_support(gene: str, term_id: str) -> dict[str, str] | None:
    line = optional_first_line(GENE_ROOT / gene / f"{gene}-goa.tsv", term_id)
    if not line:
        return None
    return support(file_id(gene, "goa.tsv"), line)


def uniprot_support(gene: str, term_id: str | None = None) -> list[dict[str, str]]:
    path = GENE_ROOT / gene / f"{gene}-uniprot.txt"
    items: list[dict[str, str]] = []
    add_unique(items, support(file_id(gene, "uniprot.txt"), first_line(path, "DE   ")))
    if term_id:
        line = optional_first_line(path, f"DR   GO; {term_id};")
        if line:
            add_unique(items, support(file_id(gene, "uniprot.txt"), line))
    for needles in (
        ("CC   -!- FUNCTION:",),
        ("CC   -!- CATALYTIC ACTIVITY:",),
        ("CC   -!- SUBCELLULAR LOCATION:",),
        ("CC   -!- SUBUNIT:",),
        ("CC   -!- INDUCTION:",),
        ("CC   -!- SIMILARITY:",),
        ("DR   PANTHER;",),
        ("DR   Pfam;",),
        ("FT   DOMAIN",),
    ):
        line = optional_first_line(path, *needles)
        if line:
            add_unique(items, support(file_id(gene, "uniprot.txt"), line))
    for line in [line for line in read_lines(path) if line.startswith("DR   InterPro;")][:5]:
        add_unique(items, support(file_id(gene, "uniprot.txt"), line))
    return items


def asta_support(gene: str) -> list[dict[str, str]]:
    path = GENE_ROOT / gene / f"{gene}-deep-research-asta.md"
    items: list[dict[str, str]] = []
    for marker in ("  uniprot_accession:", "  protein_description:", "  protein_family:", "  protein_domains:"):
        line = optional_first_line(path, marker)
        if line:
            add_unique(items, support(file_id(gene, "deep-research-asta.md"), line))
    return items


def standard_support(gene: str, term_id: str | None = None) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    if term_id:
        add_unique(items, goa_support(gene, term_id))
    for item in uniprot_support(gene, term_id):
        add_unique(items, item)
    for item in asta_support(gene):
        add_unique(items, item)
    return items


def load(gene: str) -> dict:
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def write(gene: str, data: dict) -> None:
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    path.write_text(yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=False, width=120), encoding="utf-8")


def ensure_references(data: dict, gene: str, accession: str) -> None:
    refs = data.setdefault("references", [])
    seen = {ref["id"] for ref in refs}
    for ref_id, title in {
        file_id(gene, "goa.tsv"): f"QuickGO GOA annotations for {gene} ({accession})",
        file_id(gene, "uniprot.txt"): f"UniProtKB entry for {gene} ({accession})",
        file_id(gene, "deep-research-asta.md"): f"Asta retrieval report for {gene} ({accession})",
    }.items():
        if ref_id not in seen:
            refs.append({"id": ref_id, "title": title, "findings": []})
            seen.add(ref_id)


def accession(data: dict) -> str:
    return data.get("id", "")


def set_review(data: dict, gene: str, term_id: str, action: str, summary: str, reason: str | None = None) -> None:
    for ann in data.get("existing_annotations") or []:
        if ann.get("term", {}).get("id") == term_id:
            review = {
                "summary": summary,
                "action": action,
                "supported_by": standard_support(gene, term_id),
            }
            if reason:
                review["reason"] = reason
            ann["review"] = review
            return
    raise ValueError(f"{gene} has no existing annotation {term_id}")


def ensure_new_annotation(
    data: dict,
    gene: str,
    term_id: str,
    qualifier: str,
    summary: str,
    reason: str,
) -> None:
    annotations = data.setdefault("existing_annotations", [])
    if any(ann.get("term", {}).get("id") == term_id for ann in annotations):
        set_review(data, gene, term_id, "NEW", summary, reason)
        return
    annotations.append(
        {
            "term": TERM[term_id],
            "evidence_type": "IEA",
            "original_reference_id": file_id(gene, "uniprot.txt"),
            "qualifier": qualifier,
            "review": {
                "summary": summary,
                "action": "NEW",
                "reason": reason,
                "supported_by": standard_support(gene, term_id),
            },
        }
    )


def core(
    description: str,
    mf: str,
    processes: list[str] | None = None,
    locations: list[str] | None = None,
    in_complex: str | None = None,
    supported_by: list[dict[str, str]] | None = None,
) -> dict:
    item = {
        "description": description,
        "molecular_function": TERM[mf],
        "supported_by": supported_by or [],
    }
    if processes:
        item["directly_involved_in"] = [TERM[p] for p in processes]
    if locations:
        item["locations"] = [TERM[loc] for loc in locations]
    if in_complex:
        item["in_complex"] = TERM[in_complex]
    return item


def finish_common(data: dict, gene: str) -> None:
    data["status"] = "DRAFT"
    data["description"] = DESCRIPTIONS[gene]
    data["proposed_new_terms"] = data.get("proposed_new_terms") or []
    data["suggested_questions"] = data.get("suggested_questions") or []
    data["suggested_experiments"] = data.get("suggested_experiments") or []


def curate_lon_like(gene: str) -> None:
    data = load(gene)
    ensure_references(data, gene, accession(data))
    finish_common(data, gene)
    set_review(data, gene, "GO:0004176", "ACCEPT", "Correct core call for a Lon/peptidase S16-family ATP-dependent protease.")
    set_review(data, gene, "GO:0004252", "KEEP_AS_NON_CORE", "Correct catalytic-class parent, but less informative than ATP-dependent peptidase activity for Lon-family proteases.")
    if any(ann.get("term", {}).get("id") == "GO:0005524" for ann in data.get("existing_annotations") or []):
        set_review(data, gene, "GO:0005524", "MARK_AS_OVER_ANNOTATED", "Correct but broad nucleotide-binding context; ATP-dependent peptidase activity and ATP hydrolysis are more informative where present.")
    if any(ann.get("term", {}).get("id") == "GO:0005737" for ann in data.get("existing_annotations") or []):
        set_review(data, gene, "GO:0005737", "ACCEPT", "Correct cytoplasmic localization for the soluble Lon-family protease.")
    for term_id in ("GO:0006508", "GO:0030163", "GO:0006515", "GO:0034605"):
        if any(ann.get("term", {}).get("id") == term_id for ann in data.get("existing_annotations") or []):
            set_review(data, gene, term_id, "ACCEPT", "Consistent with Lon-family ATP-dependent degradation of abnormal or stress-damaged proteins.")
    if any(ann.get("term", {}).get("id") == "GO:0016887" for ann in data.get("existing_annotations") or []):
        set_review(data, gene, "GO:0016887", "ACCEPT", "Correct ATP-hydrolysis activity for the AAA+ motor region of the Lon protease.")
    if any(ann.get("term", {}).get("id") == "GO:0043565" for ann in data.get("existing_annotations") or []):
        set_review(data, gene, "GO:0043565", "KEEP_AS_NON_CORE", "UniProt transfers a site-specific double-stranded DNA-binding property for Lon; this is retained as secondary context rather than the main protease function.")
    processes = ["GO:0030163"] if any(ann.get("term", {}).get("id") == "GO:0030163" for ann in data.get("existing_annotations") or []) else ["GO:0006508"]
    locations = ["GO:0005737"] if any(ann.get("term", {}).get("id") == "GO:0005737" for ann in data.get("existing_annotations") or []) else None
    data["core_functions"] = [
        core(
            "ATP-dependent proteolytic degradation of protein substrates by a Lon-family serine protease.",
            "GO:0004176",
            processes,
            locations,
            supported_by=standard_support(gene, "GO:0004176"),
        )
    ]
    if any(ann.get("term", {}).get("id") == "GO:0016887" for ann in data.get("existing_annotations") or []):
        data["core_functions"].append(
            core(
                "AAA+ ATP hydrolysis powers substrate processing by the Lon-family protease.",
                "GO:0016887",
                processes,
                locations,
                supported_by=standard_support(gene, "GO:0016887"),
            )
        )
    data["suggested_questions"] = [{"question": f"What substrates distinguish {gene} from the other Lon-family proteases encoded by KT2440?"}]
    write(gene, data)


def curate_sspB() -> None:
    gene = "sspB"
    data = load(gene)
    ensure_references(data, gene, accession(data))
    finish_common(data, gene)
    set_review(data, gene, "GO:0005829", "ACCEPT", "Cytosol is consistent with a soluble ClpXP substrate-adaptor/regulator.")
    set_review(data, gene, "GO:0005840", "KEEP_AS_NON_CORE", "Ribosome association is plausible as SspB participates in tmRNA/SsrA-linked protein quality control, but it is not the defining function.")
    set_review(data, gene, "GO:0045732", "ACCEPT", "SspB enhances ClpXP-dependent protein degradation and is appropriately curated as positive regulation of protein catabolic process.")
    ensure_new_annotation(
        data,
        gene,
        "GO:0061135",
        "enables",
        "SspB is a ClpXP specificity-enhancing factor, best captured as an endopeptidase-regulator/adaptor activity rather than generic protein binding or peptidase activity.",
        "The local UniProt product name and SspB domain evidence support a ClpXP regulator/adaptor role; no catalytic peptidase domain is present.",
    )
    data["core_functions"] = [
        core(
            "Regulates ClpXP endopeptidase substrate selection and promotes protein catabolic process as an SspB-family adaptor.",
            "GO:0061135",
            ["GO:0045732"],
            ["GO:0005829"],
            supported_by=standard_support(gene, "GO:0061135"),
        )
    ]
    data["suggested_questions"] = [{"question": "Which KT2440 SsrA-tagged or stress-regulated substrates are delivered to ClpXP by SspB?"}]
    write(gene, data)


def curate_clpP_like(gene: str, stronger: bool = True) -> None:
    data = load(gene)
    ensure_references(data, gene, accession(data))
    finish_common(data, gene)
    if stronger:
        set_review(data, gene, "GO:0004176", "ACCEPT", "Correct for a ClpP-family proteolytic subunit whose proteolysis occurs in an ATP-dependent Clp system.")
        set_review(data, gene, "GO:0004252", "KEEP_AS_NON_CORE", "Correct serine-peptidase class but less informative than the Clp-system ATP-dependent peptidase annotation.")
        set_review(data, gene, "GO:0006508", "ACCEPT", "Consistent with ClpP-family proteolytic turnover.")
        set_review(data, gene, "GO:0006515", "ACCEPT", "Consistent with ClpP-family degradation of misfolded or incompletely synthesized proteins.")
        set_review(data, gene, "GO:0009368", "ACCEPT", "Correct complex membership for a ClpP-family proteolytic subunit.")
        set_review(data, gene, "GO:0051117", "ACCEPT", "Correct because ClpP-family proteolytic subunits bind AAA+ ATPase partners.")
        if any(ann.get("term", {}).get("id") == "GO:0005737" for ann in data.get("existing_annotations") or []):
            set_review(data, gene, "GO:0005737", "ACCEPT", "Correct cytoplasmic localization for the soluble ClpP protease subunit.")
        data["core_functions"] = [
            core(
                "ClpP-family proteolytic subunit activity in ATP-dependent degradation of protein substrates.",
                "GO:0004176",
                ["GO:0006515"],
                ["GO:0005737"] if any(ann.get("term", {}).get("id") == "GO:0005737" for ann in data.get("existing_annotations") or []) else None,
                "GO:0009368",
                standard_support(gene, "GO:0004176"),
            ),
            core(
                "Binding of partner AAA+ ATPase subunits that deliver and unfold substrates for the ClpP proteolytic chamber.",
                "GO:0051117",
                ["GO:0006515"],
                ["GO:0005737"] if any(ann.get("term", {}).get("id") == "GO:0005737" for ann in data.get("existing_annotations") or []) else None,
                "GO:0009368",
                standard_support(gene, "GO:0051117"),
            ),
        ]
    else:
        ensure_new_annotation(
            data,
            gene,
            "GO:0008233",
            "enables",
            "PP_3267 has ClpP/TepA and CLP_protease domain evidence but no fetched GOA rows, so only generic peptidase activity is proposed in this first pass.",
            "The available local evidence is domain-level rather than an experimentally resolved ClpP catalytic assignment.",
        )
        ensure_new_annotation(
            data,
            gene,
            "GO:0006508",
            "involved_in",
            "Generic proteolysis is proposed as the matching process for the ClpP/TepA-domain peptidase candidate.",
            "The available local evidence supports only a conservative protease-domain call.",
        )
        data["core_functions"] = [
            core(
                "Conservative ClpP/TepA-domain peptidase candidate activity.",
                "GO:0008233",
                ["GO:0006508"],
                supported_by=standard_support(gene, "GO:0008233"),
            )
        ]
        data["suggested_questions"] = [{"question": "Does PP_3267 retain the catalytic residues and oligomeric assembly expected for an active ClpP-like peptidase?"}]
    write(gene, data)


def curate_clpA() -> None:
    gene = "clpA"
    data = load(gene)
    ensure_references(data, gene, accession(data))
    finish_common(data, gene)
    set_review(data, gene, "GO:0004252", "REMOVE", "This EC-derived peptidase annotation is likely over-propagated from the product name; ClpA is the AAA+ ATPase/unfoldase partner, not the ClpP proteolytic catalytic subunit.")
    set_review(data, gene, "GO:0005524", "MARK_AS_OVER_ANNOTATED", "Correct ATP-binding context but less informative than ATP hydrolysis activity for the ClpA AAA+ motor.")
    set_review(data, gene, "GO:0005737", "ACCEPT", "Correct cytoplasmic localization for a soluble ClpA-family ATPase.")
    set_review(data, gene, "GO:0016887", "ACCEPT", "Correct ATP hydrolysis activity for the ClpA AAA+ unfoldase motor.")
    set_review(data, gene, "GO:0034605", "KEEP_AS_NON_CORE", "Heat-response context is plausible for Clp-family protein quality control but is broader than the core ATPase/unfoldase function.")
    set_review(data, gene, "GO:0043335", "ACCEPT", "Correct process for a ClpA-family AAA+ unfoldase that remodels protein substrates.")
    data["core_functions"] = [
        core(
            "ATP hydrolysis-driven unfolding/remodeling of protein substrates by a ClpA-family AAA+ unfoldase.",
            "GO:0016887",
            ["GO:0043335"],
            ["GO:0005737"],
            supported_by=standard_support(gene, "GO:0016887"),
        )
    ]
    data["suggested_questions"] = [{"question": "Which ClpP paralog or proteolytic chamber partners with ClpA in KT2440?"}]
    write(gene, data)


def curate_pp4814() -> None:
    gene = "PP_4814"
    data = load(gene)
    ensure_references(data, gene, accession(data))
    finish_common(data, gene)
    data["existing_annotations"] = []
    data["core_functions"] = []
    data["proposed_new_terms"] = []
    data["suggested_questions"] = [
        {"question": "Is PP_4814 an autonomous functional Lon-related adaptor/substrate-binding protein, or a non-catalytic fragment/pseudogene-like remnant?"}
    ]
    write(gene, data)


def curate_hslV() -> None:
    gene = "hslV"
    data = load(gene)
    ensure_references(data, gene, accession(data))
    finish_common(data, gene)
    set_review(data, gene, "GO:0004298", "ACCEPT", "Correct core threonine-type endopeptidase activity for the HslV protease subunit.")
    set_review(data, gene, "GO:0005737", "ACCEPT", "Correct cytoplasmic localization.")
    set_review(data, gene, "GO:0005839", "KEEP_AS_NON_CORE", "HslV is proteasome-like, but the HslUV protease complex term is the more specific bacterial complex annotation.")
    set_review(data, gene, "GO:0006508", "ACCEPT", "Correct proteolysis process for the HslV catalytic subunit.")
    set_review(data, gene, "GO:0008233", "MARK_AS_OVER_ANNOTATED", "Correct broad parent, but threonine-type endopeptidase activity is the informative molecular-function term.")
    set_review(data, gene, "GO:0009376", "ACCEPT", "Correct HslUV protease complex membership.")
    set_review(data, gene, "GO:0030163", "ACCEPT", "Correct protein catabolic process for HslUV protease activity.")
    data["core_functions"] = [
        core(
            "Threonine-type proteolytic subunit activity in the HslUV protease complex.",
            "GO:0004298",
            ["GO:0030163"],
            ["GO:0005737"],
            "GO:0009376",
            standard_support(gene, "GO:0004298"),
        )
    ]
    data["suggested_questions"] = [{"question": "Which stress conditions and protein substrates are preferentially handled by HslUV in KT2440?"}]
    write(gene, data)


def curate_hslU() -> None:
    gene = "hslU"
    data = load(gene)
    ensure_references(data, gene, accession(data))
    finish_common(data, gene)
    set_review(data, gene, "GO:0005524", "MARK_AS_OVER_ANNOTATED", "Correct ATP-binding context but less informative than ATP hydrolysis and proteasome-activating activity.")
    set_review(data, gene, "GO:0005737", "ACCEPT", "Correct cytoplasmic localization.")
    set_review(data, gene, "GO:0008233", "REMOVE", "HslU is the ATPase/unfoldase activator of HslV, not the catalytic peptidase subunit.")
    set_review(data, gene, "GO:0009376", "ACCEPT", "Correct HslUV protease complex membership.")
    set_review(data, gene, "GO:0010498", "ACCEPT", "Correct proteasome-like protein catabolic process for the HslUV system.")
    set_review(data, gene, "GO:0016887", "ACCEPT", "Correct ATP hydrolysis activity for the HslU AAA+ motor.")
    set_review(data, gene, "GO:0036402", "ACCEPT", "Correct proteasome-activating activity: HslU activates HslV and delivers unfolded substrates.")
    set_review(data, gene, "GO:0043335", "ACCEPT", "Correct protein-unfolding process for the HslU ATPase/unfoldase.")
    data["core_functions"] = [
        core(
            "ATP hydrolysis-driven substrate unfolding by the HslU AAA+ motor.",
            "GO:0016887",
            ["GO:0043335", "GO:0010498"],
            ["GO:0005737"],
            "GO:0009376",
            standard_support(gene, "GO:0016887"),
        ),
        core(
            "Activation of the HslV protease chamber in the HslUV complex.",
            "GO:0036402",
            ["GO:0010498"],
            ["GO:0005737"],
            "GO:0009376",
            standard_support(gene, "GO:0036402"),
        ),
    ]
    data["suggested_questions"] = [{"question": "Which KT2440 substrates require HslU-mediated unfolding before HslV proteolysis?"}]
    write(gene, data)


def main() -> None:
    curate_lon_like("PP_0680")
    curate_sspB()
    curate_lon_like("lon-I")
    curate_clpP_like("clpP")
    curate_lon_like("lon-II")
    curate_clpP_like("PP_3045")
    curate_clpP_like("PP_3267", stronger=False)
    curate_clpA()
    curate_pp4814()
    curate_hslV()
    curate_hslU()
    print("Curated ATP-dependent protease/protein-turnover split")


if __name__ == "__main__":
    main()
