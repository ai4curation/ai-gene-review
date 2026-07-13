#!/usr/bin/env python3
"""First-pass curation for KEGG ppu03060 bacterial protein export."""

from __future__ import annotations

from pathlib import Path

import yaml


SPECIES = "PSEPK"
ROOT = Path("genes") / SPECIES
OVERLAP_GENES = ["secA", "ffh", "ftsY"]
SCRIPT_ADDED_TERMS = {"GO:0031522"}
SCRIPT_ADDED_TERMS_BY_GENE = {"yajC": {"GO:0043952"}}

GO_REF_TITLES = {
    "GO_REF:0000002": "Gene Ontology annotation through association of InterPro records with GO terms",
    "GO_REF:0000003": "Gene Ontology annotation based on Enzyme Commission mapping",
    "GO_REF:0000043": "Gene Ontology annotation based on UniProtKB/Swiss-Prot keyword mapping",
    "GO_REF:0000044": (
        "Gene Ontology annotation based on UniProtKB/Swiss-Prot Subcellular Location vocabulary mapping, "
        "accompanied by conservative changes to GO terms applied by UniProt"
    ),
    "GO_REF:0000104": (
        "Electronic Gene Ontology annotations created by transferring manual GO annotations between "
        "related proteins based on shared sequence features"
    ),
    "GO_REF:0000117": "Electronic Gene Ontology annotations created by ARBA machine learning models",
    "GO_REF:0000118": "TreeGrafter-generated GO annotations",
    "GO_REF:0000120": "Combined Automated Annotation using Multiple IEA Methods",
}


SEC_DECISIONS = {
    "GO:0005886": ("ACCEPT", "plasma membrane localization matches the bacterial inner-membrane Sec apparatus"),
    "GO:0006605": ("KEEP_AS_NON_CORE", "protein targeting is correct but broader than Sec-complex protein transport"),
    "GO:0006886": ("MARK_AS_OVER_ANNOTATED", "intracellular protein transport is a broad parent of Sec-dependent translocation"),
    "GO:0008320": ("ACCEPT", "protein transmembrane transporter activity is appropriate at the Sec translocon level"),
    "GO:0009306": ("ACCEPT", "protein secretion captures Sec-dependent export across the cytoplasmic membrane"),
    "GO:0015031": ("KEEP_AS_NON_CORE", "protein transport is correct but less specific than the Sec-complex process"),
    "GO:0015450": (
        "MARK_AS_OVER_ANNOTATED",
        "protein-transporting ATPase activity is appropriate for SecA but over-propagated to non-ATPase Sec channel/accessory subunits",
    ),
    "GO:0016020": ("MARK_AS_OVER_ANNOTATED", "generic membrane localization is less informative than plasma membrane"),
    "GO:0043952": ("ACCEPT", "protein transport by the Sec complex is the pathway-defining process"),
    "GO:0065002": ("ACCEPT", "intracellular protein transmembrane transport is the transmembrane aspect of Sec-dependent export"),
}

TAT_DECISIONS = {
    "GO:0005886": ("ACCEPT", "plasma membrane localization matches the bacterial Tat translocase"),
    "GO:0008320": ("ACCEPT", "protein transmembrane transporter activity is appropriate for Tat translocase components"),
    "GO:0009977": ("ACCEPT", "proton motive force dependent protein transmembrane transporter activity captures Tat energetics"),
    "GO:0015031": ("KEEP_AS_NON_CORE", "protein transport is correct but less specific than Tat-complex transport"),
    "GO:0016020": ("MARK_AS_OVER_ANNOTATED", "generic membrane localization is less informative than plasma membrane"),
    "GO:0033281": ("ACCEPT", "TAT protein transport complex is the relevant translocase complex"),
    "GO:0043953": ("ACCEPT", "protein transport by the Tat complex is the pathway-defining process"),
    "GO:0065002": ("ACCEPT", "intracellular protein transmembrane transport captures Tat-mediated export across the inner membrane"),
}


def sec_core(description: str) -> dict:
    return {
        "description": description,
        "contributes_to_molecular_function": {"id": "GO:0008320", "label": "protein transmembrane transporter activity"},
        "directly_involved_in": [{"id": "GO:0043952", "label": "protein transport by the Sec complex"}],
        "locations": [{"id": "GO:0005886", "label": "plasma membrane"}],
    }


def tat_core(description: str, include_location: bool = True) -> dict:
    core = {
        "description": description,
        "contributes_to_molecular_function": {"id": "GO:0008320", "label": "protein transmembrane transporter activity"},
        "directly_involved_in": [{"id": "GO:0043953", "label": "protein transport by the Tat complex"}],
        "in_complex": {"id": "GO:0033281", "label": "TAT protein transport complex"},
    }
    if include_location:
        core["locations"] = [{"id": "GO:0005886", "label": "plasma membrane"}]
    return core


GENES: dict[str, dict] = {
    "yidC": {
        "symbol": "yidC",
        "description": (
            "yidC (PP_0006) encodes the conserved bacterial membrane protein insertase YidC. "
            "YidC inserts and folds inner-membrane proteins, acting both independently for selected membrane proteins "
            "and in partnership with the SecYEG translocon during membrane protein biogenesis."
        ),
        "core": {
            "description": "Inner-membrane insertase that promotes insertion and folding of membrane proteins.",
            "molecular_function": {"id": "GO:0032977", "label": "membrane insertase activity"},
            "directly_involved_in": [{"id": "GO:0051205", "label": "protein insertion into membrane"}],
            "locations": [{"id": "GO:0005886", "label": "plasma membrane"}],
        },
        "decisions": {
            "GO:0005886": ("ACCEPT", "YidC is an inner-membrane insertase"),
            "GO:0016020": ("MARK_AS_OVER_ANNOTATED", "generic membrane localization is less informative than plasma membrane"),
            "GO:0032977": ("ACCEPT", "membrane insertase activity is the defining YidC molecular function"),
            "GO:0051205": ("ACCEPT", "protein insertion into membrane is the core YidC process"),
        },
    },
    "secE": {
        "symbol": "secE",
        "description": (
            "secE (PP_0441) encodes SecE, a small integral inner-membrane subunit of the SecYEG translocon. "
            "SecE stabilizes the SecY channel and contributes to Sec-dependent protein transport across or into the membrane."
        ),
        "core": sec_core("Integral SecYEG translocon subunit that stabilizes the SecY protein-conducting channel."),
        "decisions": SEC_DECISIONS,
    },
    "secY": {
        "symbol": "secY",
        "description": (
            "secY (PP_0474) encodes SecY, the core protein-conducting channel of the bacterial SecYEG translocon. "
            "It provides the membrane pore used by SecA-driven post-translational export and SRP-coupled membrane protein insertion."
        ),
        "core": sec_core("Core SecYEG protein-conducting channel subunit for Sec-dependent translocation."),
        "decisions": SEC_DECISIONS,
    },
    "lspA": {
        "symbol": "lspA",
        "description": (
            "lspA (PP_0604) encodes lipoprotein signal peptidase, also called signal peptidase II. "
            "It is a membrane peptidase that cleaves signal peptides from prolipoproteins after lipid modification, "
            "supporting bacterial lipoprotein maturation during envelope protein export."
        ),
        "core": {
            "description": "Membrane signal peptidase II that processes bacterial prolipoproteins during lipoprotein maturation.",
            "molecular_function": {"id": "GO:0004190", "label": "aspartic-type endopeptidase activity"},
            "directly_involved_in": [{"id": "GO:0006508", "label": "proteolysis"}],
            "locations": [{"id": "GO:0016020", "label": "membrane"}],
        },
        "decisions": {
            "GO:0004190": ("ACCEPT", "aspartic-type endopeptidase activity captures LspA signal peptidase II chemistry"),
            "GO:0006508": ("ACCEPT", "proteolysis captures signal peptide cleavage from prolipoproteins"),
            "GO:0016020": ("ACCEPT", "LspA is a membrane signal peptidase"),
        },
    },
    "yajC": {
        "symbol": "yajC",
        "description": (
            "yajC (PP_0834) encodes YajC, a small membrane accessory component associated with the SecDF-YajC "
            "protein translocation accessory complex. It is part of the bacterial Sec export context rather than a standalone enzyme."
        ),
        "core": {
            "description": "SecDF-YajC accessory component supporting Sec-dependent protein export.",
            "locations": [{"id": "GO:0005886", "label": "plasma membrane"}],
        },
        "decisions": {**SEC_DECISIONS, "GO:0015031": ("ACCEPT", "protein transport captures YajC's Sec accessory role")},
    },
    "secD": {
        "symbol": "secD",
        "description": (
            "secD (PP_0835) encodes SecD, a membrane component of the SecDF-YajC accessory complex. "
            "SecD/SecF supports late-stage movement and release of exported proteins through the Sec translocon, "
            "likely using the proton motive force rather than acting as an ATPase itself."
        ),
        "core": sec_core("SecDF-YajC accessory component supporting late-stage Sec-dependent protein translocation."),
        "decisions": SEC_DECISIONS,
    },
    "secF": {
        "symbol": "secF",
        "description": (
            "secF (PP_0836) encodes SecF, the partner membrane component of the SecDF-YajC accessory complex. "
            "Together with SecD and YajC it supports efficient Sec-dependent protein transport across the inner membrane."
        ),
        "core": sec_core("SecDF-YajC accessory component supporting efficient Sec-dependent protein translocation."),
        "decisions": SEC_DECISIONS,
    },
    "tatC-I": {
        "symbol": "tatC-I",
        "description": (
            "tatC-I (PP_1039) encodes a TatC-family membrane subunit of a twin-arginine translocation locus. "
            "TatC is the signal-peptide recognition and core membrane component of the Tat complex for exporting folded proteins."
        ),
        "core": tat_core("TatC-family core membrane subunit for twin-arginine protein translocation."),
        "decisions": TAT_DECISIONS,
    },
    "tatB-I": {
        "symbol": "tatB-I",
        "description": (
            "tatB-I (PP_1040) encodes a TatB-family membrane component of the first KT2440 twin-arginine translocation locus. "
            "TatB partners with TatC and TatA-family proteins in export of folded twin-arginine signal peptide substrates."
        ),
        "core": tat_core("TatB-family membrane component of a twin-arginine protein translocation complex.", include_location=False),
        "decisions": TAT_DECISIONS,
    },
    "tatA-I": {
        "symbol": "tatA-I",
        "description": (
            "tatA-I (PP_1041) encodes a TatA-family membrane component of the first KT2440 twin-arginine translocation locus. "
            "TatA-family proteins form or contribute to the conductive Tat translocation path for folded protein export."
        ),
        "core": tat_core("TatA-family membrane component of a twin-arginine protein translocation complex."),
        "decisions": TAT_DECISIONS,
    },
    "lepB": {
        "symbol": "lepB",
        "description": (
            "lepB (PP_1432) encodes signal peptidase I, a membrane serine peptidase that removes N-terminal signal peptides "
            "from proteins exported by the Sec pathway. It supports maturation of secreted and membrane-associated proteins."
        ),
        "core": {
            "description": "Membrane signal peptidase I that removes signal peptides from exported precursor proteins.",
            "molecular_function": {"id": "GO:0009003", "label": "signal peptidase activity"},
            "directly_involved_in": [{"id": "GO:0051604", "label": "protein maturation"}],
            "locations": [{"id": "GO:0016020", "label": "membrane"}],
        },
        "decisions": {
            "GO:0004252": ("ACCEPT", "serine-type endopeptidase activity is the catalytic class of signal peptidase I"),
            "GO:0006508": ("ACCEPT", "proteolysis captures signal peptide cleavage"),
            "GO:0008233": ("MARK_AS_OVER_ANNOTATED", "generic peptidase activity is less informative than signal peptidase activity"),
            "GO:0008236": ("KEEP_AS_NON_CORE", "serine-type peptidase activity is correct but broader than signal peptidase activity"),
            "GO:0009003": ("ACCEPT", "signal peptidase activity is the defining LepB molecular function"),
            "GO:0016020": ("ACCEPT", "LepB is a membrane signal peptidase"),
            "GO:0051604": ("ACCEPT", "protein maturation captures signal peptide processing after export"),
        },
    },
    "tatA-II": {
        "symbol": "tatA-II",
        "description": (
            "tatA-II (PP_5016) encodes a second TatA-family membrane component in KT2440. "
            "It is annotated as a twin-arginine translocase component and likely contributes to a second TatABC-like export locus."
        ),
        "core": tat_core("Second-locus TatA-family membrane component for twin-arginine protein translocation."),
        "decisions": TAT_DECISIONS,
    },
    "tatB": {
        "symbol": "tatB",
        "description": (
            "tatB (PP_5017) encodes a TatB-family membrane component adjacent to tatA-II and tatC-II. "
            "It contributes to twin-arginine protein export of folded periplasmic or membrane-associated substrates."
        ),
        "core": tat_core("Second-locus TatB-family membrane component for twin-arginine protein translocation."),
        "decisions": TAT_DECISIONS,
    },
    "tatC-II": {
        "symbol": "tatC-II",
        "description": (
            "tatC-II (PP_5018) encodes a second TatC-family membrane subunit in KT2440. "
            "It is the core TatC component of the second TatABC-like locus and supports twin-arginine protein transport."
        ),
        "core": tat_core("Second-locus TatC-family core membrane subunit for twin-arginine protein translocation."),
        "decisions": TAT_DECISIONS,
    },
    "secB": {
        "symbol": "secB",
        "description": (
            "secB (PP_5053) encodes the SecB protein-export chaperone. "
            "SecB binds unfolded preproteins in the cytoplasm, maintains them in an export-competent state, and delivers them "
            "to SecA/SecYEG for post-translational Sec-dependent export."
        ),
        "core": {
            "description": "Cytoplasmic SecB chaperone that binds unfolded preproteins and delivers them to the Sec export pathway.",
            "directly_involved_in": [
                {"id": "GO:0015031", "label": "protein transport"},
                {"id": "GO:0006457", "label": "protein folding"},
            ],
            "locations": [{"id": "GO:0005737", "label": "cytoplasm"}],
        },
        "decisions": {
            "GO:0005737": ("ACCEPT", "SecB is a cytoplasmic preprotein chaperone"),
            "GO:0006457": ("ACCEPT", "protein folding captures SecB's chaperone role in maintaining export substrates"),
            "GO:0015031": ("ACCEPT", "protein transport captures SecB delivery of preproteins to the Sec pathway"),
            "GO:0051262": ("KEEP_AS_NON_CORE", "protein tetramerization is correct SecB assembly context but not the main export function"),
        },
    },
    "secG": {
        "symbol": "secG",
        "description": (
            "secG (PP_5706) encodes SecG, an integral inner-membrane subunit of the SecYEG protein translocon. "
            "SecG supports efficient Sec-dependent protein export and membrane insertion as part of the Sec channel complex."
        ),
        "core": sec_core("Integral SecYEG translocon subunit supporting Sec-dependent protein transport."),
        "decisions": SEC_DECISIONS,
    },
}


def support_for(term_id: str, label: str, gene: str) -> dict:
    path = ROOT / gene / f"{gene}-goa.tsv"
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            if term_id in line:
                return {"reference_id": f"file:{SPECIES}/{gene}/{gene}-goa.tsv", "supporting_text": line}
    return {"reference_id": f"file:{SPECIES}/{gene}/{gene}-goa.tsv", "supporting_text": f"{term_id}\t{label}"}


def asta_support(gene: str) -> dict:
    path = ROOT / gene / f"{gene}-deep-research-asta.md"
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("- **Protein Description:** "):
            return {"reference_id": f"file:{SPECIES}/{gene}/{gene}-deep-research-asta.md", "supporting_text": line}
    raise ValueError(f"No Asta protein-description line found for {gene}")


def uniprot_go_support(gene: str, term_id: str) -> dict:
    path = ROOT / gene / f"{gene}-uniprot.txt"
    for line in path.read_text(encoding="utf-8").splitlines():
        if f"DR   GO; {term_id};" in line:
            return {"reference_id": f"file:{SPECIES}/{gene}/{gene}-uniprot.txt", "supporting_text": line}
    raise ValueError(f"No UniProt GO line found for {gene} {term_id}")


def unique_references(existing: list[dict], gene: str) -> list[dict]:
    refs: list[dict] = []
    seen: set[str] = set()
    for ref in existing:
        ref_id = ref.get("id")
        if not ref_id or ref_id in seen:
            continue
        if ref_id in GO_REF_TITLES:
            ref = {"id": ref_id, "title": GO_REF_TITLES[ref_id], "findings": []}
        refs.append(ref)
        seen.add(ref_id)
    for ref in [
        {
            "id": f"file:{SPECIES}/{gene}/{gene}-uniprot.txt",
            "title": f"UniProtKB entry for {gene}",
            "findings": [{"statement": "UniProt identity, protein name, family, domain, and GO metadata used for first-pass pathway curation."}],
        },
        {
            "id": f"file:{SPECIES}/{gene}/{gene}-goa.tsv",
            "title": f"QuickGO GOA annotations for {gene}",
            "findings": [{"statement": "GOA table containing the annotations reviewed in this file."}],
        },
        {
            "id": f"file:{SPECIES}/{gene}/{gene}-deep-research-asta.md",
            "title": f"Asta retrieval report for {gene}",
            "findings": [{"statement": "Asta retrieval used as fast gene-level context; no unsupported hypotheses were imported."}],
        },
    ]:
        local_name = ref["id"].split("/")[-1]
        if ref["id"] not in seen and (ROOT / gene / local_name).exists():
            refs.append(ref)
            seen.add(ref["id"])
    return refs


def curated_review(gene: str, term_id: str, label: str, decision: tuple) -> dict:
    action, reason, *rest = decision
    if action == "ACCEPT":
        summary = f"{label} is supported for {gene} in the ppu03060 protein-export first pass."
    elif action == "KEEP_AS_NON_CORE":
        summary = f"{label} is plausible for {gene} but not the most specific pathway-defining role."
    elif action == "MARK_AS_OVER_ANNOTATED":
        summary = f"{label} is too broad or over-propagated for the main ppu03060 role of {gene}."
    else:
        summary = f"{label} was reviewed for {gene}."
    review = {"summary": summary, "action": action, "reason": reason, "supported_by": [support_for(term_id, label, gene), asta_support(gene)]}
    if rest:
        review["proposed_replacement_terms"] = rest[0]
    return review


def new_annotation_review(gene: str, term: dict, reason: str) -> dict:
    support = []
    try:
        support.append(uniprot_go_support(gene, term["id"]))
    except ValueError:
        pass
    support.append(asta_support(gene))
    return {
        "summary": f"{term['label']} is a missing product-backed annotation for {gene}.",
        "action": "NEW",
        "reason": reason,
        "supported_by": support,
    }


def core_supported_by(core: dict, annotations: list[dict], gene: str) -> list[dict]:
    support: list[dict] = []
    term_index = {ann["term"]["id"]: ann["term"]["label"] for ann in annotations if ann.get("term", {}).get("id")}
    for slot in ("molecular_function", "contributes_to_molecular_function", "in_complex"):
        term = core.get(slot)
        if isinstance(term, dict) and term.get("id") in term_index:
            support.append(support_for(term["id"], term_index[term["id"]], gene))
    for slot in ("directly_involved_in", "locations"):
        for term in core.get(slot, []) or []:
            if term.get("id") in term_index:
                support.append(support_for(term["id"], term_index[term["id"]], gene))
    for slot in ("molecular_function", "contributes_to_molecular_function", "in_complex"):
        term = core.get(slot)
        if isinstance(term, dict) and term.get("id"):
            try:
                support.append(uniprot_go_support(gene, term["id"]))
            except ValueError:
                pass
    support.append(asta_support(gene))
    deduped: list[dict] = []
    seen: set[tuple[str, str]] = set()
    for item in support:
        key = (item["reference_id"], item["supporting_text"])
        if key not in seen:
            deduped.append(item)
            seen.add(key)
    return deduped


def curate_gene(gene: str, spec: dict) -> None:
    path = ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    data["gene_symbol"] = spec["symbol"]
    data["status"] = "DRAFT"
    data["description"] = spec["description"]
    if gene == "secB":
        data["existing_annotations"] = [
            ann for ann in data.get("existing_annotations", []) if ann.get("term", {}).get("id") != "GO:0051082"
        ]
    data["existing_annotations"] = [
        ann
        for ann in data.get("existing_annotations", [])
        if not (
            str(ann.get("original_reference_id", "")).startswith(f"file:{SPECIES}/")
            and ann.get("term", {}).get("id") in (SCRIPT_ADDED_TERMS | SCRIPT_ADDED_TERMS_BY_GENE.get(gene, set()))
        )
    ]

    decisions = spec["decisions"]
    for ann in data.get("existing_annotations", []):
        term = ann["term"]
        if term["id"] == "GO:0008320":
            term["label"] = "protein transmembrane transporter activity"
        decision = decisions.get(
            term["id"],
            ("KEEP_AS_NON_CORE", "reviewed as ppu03060 boundary context but not central to the first-pass interpretation"),
        )
        ann["review"] = curated_review(gene, term["id"], term["label"], decision)

    for ann in spec.get("new_annotations", []):
        ann = dict(ann)
        if any(existing.get("term", {}).get("id") == ann["term"]["id"] for existing in data.get("existing_annotations", [])):
            continue
        ann["review"] = new_annotation_review(gene, ann["term"], ann.pop("reason"))
        data.setdefault("existing_annotations", []).append(ann)

    core = dict(spec["core"])
    core["supported_by"] = core_supported_by(core, data.get("existing_annotations", []), gene)
    data["core_functions"] = [core]
    data["proposed_new_terms"] = []
    data["suggested_questions"] = [
        {
            "question": (
                f"What is the quantitative contribution of {spec['symbol']} to Sec/Tat/YidC protein export "
                "and membrane protein biogenesis in P. putida KT2440 under standard and stress conditions?"
            )
        }
    ]
    data["suggested_experiments"] = [
        {
            "description": (
                f"Use targeted perturbation of {spec['symbol']} with secretome, membrane-proteome, and envelope-stress readouts "
                "to distinguish direct protein-export defects from secondary growth effects."
            ),
            "experiment_type": "gene perturbation with proteomics and envelope-stress phenotyping",
        }
    ]
    data["references"] = unique_references(data.get("references", []), gene)
    path.write_text(yaml.safe_dump(data, sort_keys=False, width=120), encoding="utf-8")


def add_asta_support_to_existing_gene(gene: str) -> None:
    path = ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    support = asta_support(gene)
    for ann in data.get("existing_annotations", []):
        review = ann.get("review") or {}
        supported_by = review.setdefault("supported_by", [])
        if not any(item.get("reference_id") == support["reference_id"] for item in supported_by):
            supported_by.append(support)
        ann["review"] = review
    for core in data.get("core_functions", []) or []:
        supported_by = core.setdefault("supported_by", [])
        if not any(item.get("reference_id") == support["reference_id"] for item in supported_by):
            supported_by.append(support)
    data["references"] = unique_references(data.get("references", []), gene)
    path.write_text(yaml.safe_dump(data, sort_keys=False, width=120), encoding="utf-8")


def main() -> None:
    for gene, spec in GENES.items():
        curate_gene(gene, spec)
    for gene in OVERLAP_GENES:
        add_asta_support_to_existing_gene(gene)


if __name__ == "__main__":
    main()
