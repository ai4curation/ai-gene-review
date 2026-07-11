#!/usr/bin/env python3
"""First-pass curation for stress-resistance membrane transport spillovers."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes/PSEPK"
BATCH_PATH = ROOT / "projects/P_PUTIDA/batches/module_transport_membrane_efflux_stress_resistance_membrane_spillovers.tsv"
MODULE_PATH = ROOT / "modules/stress_detoxification_spillover_boundary.yaml"

GO_REF_TITLES = {
    "GO_REF:0000002": "Gene Ontology annotation through association of InterPro records with GO terms",
    "GO_REF:0000044": "Gene Ontology annotation based on UniProtKB/Swiss-Prot Subcellular Location vocabulary mapping, accompanied by conservative changes to GO terms applied by UniProt",
    "GO_REF:0000120": "Combined Automated Annotation using Multiple IEA Methods",
}

TERMS = {
    "GO:0005886": "plasma membrane",
    "GO:0006855": "xenobiotic transmembrane transport",
    "GO:0009636": "response to toxic substance",
    "GO:0016020": "membrane",
    "GO:0016787": "hydrolase activity",
    "GO:0019068": "virion assembly",
    "GO:0019076": "viral release from host cell",
    "GO:0022857": "transmembrane transporter activity",
    "GO:0042910": "xenobiotic transmembrane transporter activity",
    "GO:0055085": "transmembrane transport",
    "GO:1901562": "response to paraquat",
}

PQI_GENES = {"PP_0598", "PP_0599", "PP_2577", "PP_5745"}
HOLIN_GENES = {"PP_1559", "PP_3040", "PP_3884"}
VASX_TOXIN_GENES = {"PP_2076", "PP_2612", "PP_3388", "PP_3616"}
NO_GOA_MEMBRANE_GENES = {
    "PP_1425",
    "PP_1487",
    "PP_1559",
    "PP_1576",
    "PP_2076",
    "PP_2612",
    "PP_3040",
    "PP_3388",
    "nfrB",
    "PP_3616",
    "PP_3865",
    "PP_3884",
    "PP_5065",
}

PROFILES: dict[str, dict[str, Any]] = {
    "PP_0598": {
        "group": "PqiA-family paraquat-inducible membrane protein",
        "description": "PP_0598 is a predicted inner-membrane PqiA-family paraquat-inducible protein in the PqiA/PqiB intermembrane transport family.",
        "primary": None,
        "processes": ["GO:1901562"],
        "locations": ["GO:0005886"],
        "new": [("GO:1901562", "involved_in")],
    },
    "PP_0599": {
        "group": "PqiB-family paraquat-inducible membrane protein",
        "description": "PP_0599 is a predicted inner-membrane PqiB/MlaD-family paraquat-inducible protein in the PqiA/PqiB intermembrane transport family.",
        "primary": None,
        "processes": ["GO:1901562"],
        "locations": ["GO:0005886"],
        "new": [("GO:1901562", "involved_in")],
    },
    "PP_1264": {
        "group": "FUSC/ArAE-family fusaric-acid or xenobiotic exporter",
        "description": "PP_1264 is a FUSC/ArAE-family membrane exporter associated with fusaric-acid and xenobiotic resistance.",
        "primary": "GO:0042910",
        "processes": ["GO:0006855"],
        "locations": ["GO:0005886"],
        "new": [("GO:0042910", "enables"), ("GO:0006855", "involved_in")],
    },
    "PP_1425": {
        "group": "CptA/YgfX toxin-domain membrane protein",
        "description": "PP_1425 is a membrane CptA/YgfX-family toxin-domain protein whose physiological target is unresolved.",
        "primary": None,
        "processes": [],
        "locations": ["GO:0016020"],
        "new": [("GO:0016020", "located_in")],
    },
    "PP_1487": {
        "group": "TerB/YebE tellurite-resistance family protein",
        "description": "PP_1487 is a TerB/YebE-family membrane protein associated with tellurite or toxic-stress resistance.",
        "primary": None,
        "processes": ["GO:0009636"],
        "locations": ["GO:0016020"],
        "new": [("GO:0016020", "located_in"), ("GO:0009636", "involved_in")],
    },
    "PP_1559": {
        "group": "Lambda-family phage holin",
        "description": "PP_1559 is a predicted lambda-family phage holin membrane protein associated with prophage lysis or release.",
        "primary": None,
        "processes": ["GO:0019076"],
        "locations": ["GO:0016020"],
        "new": [("GO:0016020", "located_in"), ("GO:0019076", "involved_in")],
    },
    "PP_1576": {
        "group": "Phage superinfection-immunity protein",
        "description": "PP_1576 is a membrane phage-immunity/superinfection-immunity protein whose specific immunity mechanism is unresolved.",
        "primary": None,
        "processes": [],
        "locations": ["GO:0016020"],
        "new": [("GO:0016020", "located_in")],
    },
    "PP_2076": {
        "group": "VasX-family toxin-domain membrane protein",
        "description": "PP_2076 is a membrane-associated VasX N-terminal toxin-domain protein with an unresolved effector target.",
        "primary": None,
        "processes": [],
        "locations": ["GO:0016020"],
        "new": [("GO:0016020", "located_in")],
    },
    "PP_2577": {
        "group": "PqiB-family paraquat-inducible membrane protein",
        "description": "PP_2577 is a predicted inner-membrane PqiB/MlaD-family paraquat-inducible protein in the PqiA/PqiB intermembrane transport family.",
        "primary": None,
        "processes": ["GO:1901562"],
        "locations": ["GO:0005886"],
        "new": [("GO:1901562", "involved_in")],
    },
    "PP_2612": {
        "group": "VasX-family toxin-domain membrane protein",
        "description": "PP_2612 is a membrane-associated VasX N-terminal toxin-domain protein with an unresolved effector target.",
        "primary": None,
        "processes": [],
        "locations": ["GO:0016020"],
        "new": [("GO:0016020", "located_in")],
    },
    "PP_3040": {
        "group": "Pyocin R2 holin",
        "description": "PP_3040 is a predicted Pyocin R2 holin membrane protein associated with prophage or pyocin release.",
        "primary": None,
        "processes": ["GO:0019076"],
        "locations": ["GO:0016020"],
        "new": [("GO:0016020", "located_in"), ("GO:0019076", "involved_in")],
    },
    "PP_3388": {
        "group": "VasX-family toxin-domain membrane protein",
        "description": "PP_3388 is a membrane-associated VasX N-terminal toxin-domain protein with an unresolved effector target.",
        "primary": None,
        "processes": [],
        "locations": ["GO:0016020"],
        "new": [("GO:0016020", "located_in")],
    },
    "nfrB": {
        "group": "Bacteriophage N4 receptor inner-membrane subunit",
        "description": "NfrB is a predicted bacteriophage N4 receptor inner-membrane subunit with GT2/T2SS-like domains and unresolved receptor mechanism.",
        "primary": None,
        "processes": [],
        "locations": ["GO:0016020"],
        "new": [("GO:0016020", "located_in")],
    },
    "PP_3616": {
        "group": "VasX-family toxin-domain membrane protein",
        "description": "PP_3616 is a membrane-associated VasX N-terminal toxin-domain protein with an unresolved effector target.",
        "primary": None,
        "processes": [],
        "locations": ["GO:0016020"],
        "new": [("GO:0016020", "located_in")],
    },
    "PP_3865": {
        "group": "Phage tail/tape-measure protein",
        "description": "PP_3865 is a phage tail/tape-measure-family protein likely connected to prophage structural assembly.",
        "primary": None,
        "processes": ["GO:0019068"],
        "locations": ["GO:0016020"],
        "new": [("GO:0016020", "located_in"), ("GO:0019068", "involved_in")],
    },
    "PP_3884": {
        "group": "Lambda-family phage holin",
        "description": "PP_3884 is a predicted lambda-family phage holin membrane protein associated with prophage lysis or release.",
        "primary": None,
        "processes": ["GO:0019076"],
        "locations": ["GO:0016020"],
        "new": [("GO:0016020", "located_in"), ("GO:0019076", "involved_in")],
    },
    "cidB": {
        "group": "CidB/LrgB anti-holin regulator",
        "description": "CidB is a CidB/LrgB-family membrane anti-holin regulator paired with CidA-like murein hydrolase regulation.",
        "primary": None,
        "processes": [],
        "locations": ["GO:0016020"],
        "new": [],
    },
    "cidA": {
        "group": "CidA/LrgA holin-like murein hydrolase regulator",
        "description": "CidA is a CidA/LrgA-family holin-like membrane regulator of murein hydrolase activity.",
        "primary": None,
        "processes": [],
        "locations": ["GO:0005886"],
        "new": [],
    },
    "PP_5065": {
        "group": "Dermonecrotic-toxin-domain membrane protein",
        "description": "PP_5065 is a membrane-associated dermonecrotic-toxin N-terminal domain protein whose effector target is unresolved.",
        "primary": None,
        "processes": [],
        "locations": ["GO:0016020"],
        "new": [("GO:0016020", "located_in")],
    },
    "PP_5745": {
        "group": "PqiA-family paraquat-inducible membrane protein",
        "description": "PP_5745 is a predicted inner-membrane PqiA-family paraquat-inducible protein in the PqiA/PqiB intermembrane transport family.",
        "primary": None,
        "processes": ["GO:1901562"],
        "locations": ["GO:0005886"],
        "new": [("GO:1901562", "involved_in")],
    },
}


class GeneInfo(dict[str, Any]):
    pass


def load_rows() -> list[dict[str, str]]:
    with BATCH_PATH.open() as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def term(go_id: str) -> dict[str, str]:
    return {"id": go_id, "label": TERMS[go_id]}


def descriptor(go_id: str, description: str | None = None) -> dict[str, Any]:
    item: dict[str, Any] = {"preferred_term": TERMS[go_id], "term": term(go_id)}
    if description:
        item["description"] = description
    return item


def ref_file(gene: str, suffix: str) -> str:
    return f"file:PSEPK/{gene}/{gene}-{suffix}"


def support(reference_id: str, text: str) -> dict[str, str]:
    return {"reference_id": reference_id, "supporting_text": text}


def dedupe(items: list[dict[str, str]]) -> list[dict[str, str]]:
    seen: set[tuple[str, str]] = set()
    out: list[dict[str, str]] = []
    for item in items:
        key = (item["reference_id"], item["supporting_text"])
        if key in seen:
            continue
        seen.add(key)
        out.append(item)
    return out


def first_line(lines: list[str], needle: str, optional: bool = False) -> str | None:
    for line in lines:
        if needle in line:
            return line
    if optional:
        return None
    raise ValueError(f"Could not find {needle!r}")


def first_de_line(lines: list[str]) -> str:
    for line in lines:
        if line.startswith("DE   RecName") or line.startswith("DE   SubName"):
            return line
    for line in lines:
        if line.startswith("DE   "):
            return line
    raise ValueError("No UniProt DE line found")


def goa_rows(gene: str) -> list[dict[str, str]]:
    path = GENE_ROOT / gene / f"{gene}-goa.tsv"
    with path.open() as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def load_info(row: dict[str, str]) -> GeneInfo:
    gene = row["gene"]
    profile = PROFILES[gene]
    uniprot_lines = (GENE_ROOT / gene / f"{gene}-uniprot.txt").read_text(encoding="utf-8").splitlines()
    asta_lines = (GENE_ROOT / gene / f"{gene}-deep-research-asta.md").read_text(encoding="utf-8").splitlines()
    review_doc = yaml.safe_load((GENE_ROOT / gene / f"{gene}-ai-review.yaml").read_text(encoding="utf-8"))
    info = GeneInfo(
        gene=gene,
        accession=row["uniprot_accession"],
        product=row["protein_name"],
        profile=profile,
        existing_refs={ref["id"]: ref for ref in review_doc.get("references", []) if "id" in ref},
    )
    info["de"] = first_de_line(uniprot_lines)
    info["asta_product"] = first_line(asta_lines, "- **Protein Description:**")
    info["asta_domains"] = first_line(asta_lines, "- **Key Domains:**")
    info["location_line"] = first_line(uniprot_lines, "SUBCELLULAR LOCATION", optional=True)
    info["membrane_keyword"] = first_line(uniprot_lines, "KW   Membrane", optional=True)
    info["transmembrane_feature"] = first_line(uniprot_lines, "FT   TRANSMEM", optional=True)
    return info


def base_support(info: GeneInfo) -> list[dict[str, str]]:
    gene = info["gene"]
    items = [
        support(ref_file(gene, "uniprot.txt"), info["de"]),
        support(ref_file(gene, "deep-research-asta.md"), info["asta_product"]),
        support(ref_file(gene, "deep-research-asta.md"), info["asta_domains"]),
    ]
    for optional_key in ("location_line", "membrane_keyword", "transmembrane_feature"):
        if info.get(optional_key):
            items.append(support(ref_file(gene, "uniprot.txt"), info[optional_key]))
    return dedupe(items)


def goa_support(info: GeneInfo, go_id: str, label: str) -> dict[str, str]:
    return support(ref_file(info["gene"], "goa.tsv"), f"{go_id}\t{label}")


def review(info: GeneInfo, summary: str, action: str, reason: str, replacement_ids: list[str] | None = None) -> dict[str, Any]:
    item: dict[str, Any] = {
        "summary": summary,
        "action": action,
        "reason": reason,
        "supported_by": base_support(info),
    }
    if replacement_ids:
        item["proposed_replacement_terms"] = [term(go_id) for go_id in replacement_ids]
    return item


def location_review(info: GeneInfo, go_id: str) -> dict[str, Any]:
    if go_id == "GO:0005886":
        return review(info, "Plasma membrane localization is appropriate for this bacterial inner-membrane protein.", "ACCEPT", "The UniProt subcellular-location or membrane-domain context supports bacterial plasma/inner-membrane localization.")
    if go_id == "GO:0016020":
        action = "ACCEPT" if "GO:0005886" not in info["profile"].get("locations", []) else "KEEP_AS_NON_CORE"
        reason = "The broad membrane term is appropriate for this membrane protein." if action == "ACCEPT" else "The broad membrane row is true but less specific than the plasma-membrane localization row."
        return review(info, "Membrane localization is appropriate.", action, reason)
    raise ValueError(go_id)


def existing_review(info: GeneInfo, ann: dict[str, Any]) -> dict[str, Any]:
    gene = info["gene"]
    go_id = ann["term"]["id"]
    if go_id in {"GO:0005886", "GO:0016020"}:
        return location_review(info, go_id)
    if gene == "PP_1264":
        if go_id == "GO:0022857":
            return review(info, "Generic transmembrane transporter activity is supported but can be made more informative.", "MODIFY", "The FUSC/ArAE/fusaric-acid-resistance context supports xenobiotic efflux transporter activity rather than an unspecified transporter role.", ["GO:0042910"])
        if go_id == "GO:0055085":
            return review(info, "Generic transmembrane transport is supported but less informative than xenobiotic transport.", "MODIFY", "The product and FUSC domain evidence support xenobiotic transmembrane transport/resistance context.", ["GO:0006855"])
    if gene == "cidA" and go_id == "GO:0016787":
        return review(info, "Hydrolase activity is not supported for CidA itself.", "REMOVE", "CidA is described as a holin-like regulator of murein hydrolases, not as the murein hydrolase enzyme.")
    raise ValueError(f"No review rule for {gene} {go_id} {ann['term']['label']}")


def new_annotation(info: GeneInfo, go_id: str, qualifier: str) -> dict[str, Any]:
    gene = info["gene"]
    label = TERMS[go_id]
    return {
        "term": term(go_id),
        "evidence_type": "IEA",
        "original_reference_id": ref_file(gene, "uniprot.txt"),
        "qualifier": qualifier,
        "review": {
            "summary": f"Adds conservative {label} context for this stress/membrane spillover profile.",
            "action": "NEW",
            "reason": "The UniProt product, domain metadata, and Asta retrieval support this first-pass term, while exact substrates, targets, or partners remain unresolved unless directly named.",
            "supported_by": base_support(info),
        },
    }


def suggested_new_annotations(info: GeneInfo) -> list[dict[str, Any]]:
    existing_ids = set(info["go_ids"])
    out: list[dict[str, Any]] = []
    for go_id, qualifier in info["profile"].get("new", []):
        if go_id not in existing_ids:
            out.append(new_annotation(info, go_id, qualifier))
    return out


def references(info: GeneInfo) -> list[dict[str, Any]]:
    refs: dict[str, dict[str, Any]] = {}
    for ref_id, ref in info["existing_refs"].items():
        refs[ref_id] = ref
    for ref_id, title in GO_REF_TITLES.items():
        if ref_id in refs:
            refs[ref_id]["title"] = title
    gene = info["gene"]
    refs[ref_file(gene, "goa.tsv")] = {"id": ref_file(gene, "goa.tsv"), "title": f"QuickGO GOA annotations for {gene}", "findings": []}
    refs[ref_file(gene, "uniprot.txt")] = {
        "id": ref_file(gene, "uniprot.txt"),
        "title": f"UniProtKB entry for {gene} ({info['accession']})",
        "findings": [{"supporting_text": info["de"]}],
    }
    refs[ref_file(gene, "deep-research-asta.md")] = {
        "id": ref_file(gene, "deep-research-asta.md"),
        "title": f"Asta retrieval report for {gene} ({info['accession']})",
        "findings": [{"supporting_text": info["asta_product"]}, {"supporting_text": info["asta_domains"]}],
    }
    return list(refs.values())


def core_function(info: GeneInfo) -> dict[str, Any]:
    profile = info["profile"]
    core: dict[str, Any] = {"description": profile["description"], "supported_by": base_support(info)}
    if profile.get("primary"):
        core["molecular_function"] = term(profile["primary"])
    if profile.get("processes"):
        core["directly_involved_in"] = [term(go_id) for go_id in profile["processes"]]
    if profile.get("locations"):
        core["locations"] = [term(go_id) for go_id in profile["locations"]]
    return core


def curate_gene(row: dict[str, str]) -> GeneInfo:
    info = load_info(row)
    gene = info["gene"]
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    goa_ids = {row["GO TERM"] for row in goa_rows(gene)}
    goa_annotations = [ann for ann in doc.get("existing_annotations", []) if ann["term"]["id"] in goa_ids]
    info["go_ids"] = [ann["term"]["id"] for ann in goa_annotations]
    for ann in goa_annotations:
        ann["review"] = existing_review(info, ann)
        ann["review"]["supported_by"].insert(0, goa_support(info, ann["term"]["id"], ann["term"]["label"]))
        ann["review"]["supported_by"] = dedupe(ann["review"]["supported_by"])
    doc["existing_annotations"] = goa_annotations + suggested_new_annotations(info)
    doc["description"] = info["profile"]["description"]
    doc["status"] = "COMPLETE"
    doc["references"] = references(info)

    reflected_ids = {
        ann["term"]["id"]
        for ann in doc["existing_annotations"]
        if (ann.get("review") or {}).get("action") in {"ACCEPT", "NEW"}
    }
    core = core_function(info)
    if "molecular_function" in core and core["molecular_function"]["id"] not in reflected_ids:
        core.pop("molecular_function")
    for slot in ("directly_involved_in", "locations"):
        if slot in core:
            core[slot] = [item for item in core[slot] if item["id"] in reflected_ids]
            if not core[slot]:
                core.pop(slot)
    doc["core_functions"] = [core]
    doc["proposed_new_terms"] = []
    doc["suggested_questions"] = [{"question": "What direct substrate, target, partner, or stress phenotype is supported for this membrane stress-spillover protein in KT2440?"}]
    doc["suggested_experiments"] = [
        {
            "description": "Test stress survival, membrane localization, partner dependence, and toxin/holin or efflux phenotypes using knockout/complement strains, tagged proteins, and targeted challenge assays.",
            "experiment_type": "stress phenotype, localization, and partner-dependence assay",
        }
    ]
    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=120), encoding="utf-8")
    return info


def module_annoton(info: GeneInfo) -> dict[str, Any]:
    gene = info["gene"]
    profile = info["profile"]
    annoton: dict[str, Any] = {
        "id": f"{gene}_transport_bucket_stress_membrane_context",
        "label": f"{gene}: {info['product']}",
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "role_description": f"{gene}: {profile['group']}",
    }
    if profile.get("primary"):
        annoton["function"] = descriptor(profile["primary"])
    if profile.get("processes"):
        annoton["processes"] = [descriptor(go_id) for go_id in profile["processes"]]
    if profile.get("locations"):
        annoton["locations"] = [descriptor(go_id) for go_id in profile["locations"]]
    return annoton


def extend_module(infos: list[GeneInfo]) -> None:
    by_gene = {info["gene"]: info for info in infos}
    doc = yaml.safe_load(MODULE_PATH.read_text(encoding="utf-8"))
    evidence = doc.setdefault("evidence", [])
    source_id = f"file:{BATCH_PATH.relative_to(ROOT)}"
    if not any(item.get("source_id") == source_id for item in evidence):
        evidence.append(
            {
                "source_id": source_id,
                "title": "PSEPK transport stress-resistance membrane spillover batch",
                "statement": "The transport partition routes 20 paraquat-inducible, fusaric-acid-resistance, TerB, holin/immunity, phage, Cid, and toxin-domain membrane proteins to the existing stress/detoxification spillover boundary.",
            }
        )

    notes = doc.get("notes", "")
    add_note = (
        " The transport-bucket stress-resistance membrane extension adds Pqi paraquat-response proteins, "
        "PP_1264 xenobiotic-efflux context, TerB toxic-stress context, holin/phage release side nodes, "
        "CidA/CidB holin-regulator context, and unresolved VasX/CptA/ToxA toxin-domain membrane side nodes."
    )
    if "transport-bucket stress-resistance membrane extension" not in notes:
        doc["notes"] = (notes.rstrip() + add_note).strip()

    module = doc.setdefault("module", {})
    concepts = module.setdefault("concepts", [])
    concept_ids = {(item.get("term") or {}).get("id") for item in concepts if isinstance(item, dict)}
    for go_id in [
        "GO:1901562",
        "GO:0042910",
        "GO:0006855",
        "GO:0009636",
        "GO:0019076",
        "GO:0019068",
        "GO:0005886",
        "GO:0016020",
    ]:
        if go_id not in concept_ids:
            concepts.append(descriptor(go_id, "Concept used for transport-bucket stress-resistance membrane spillover curation."))

    parts = module.setdefault("parts", [])
    parts[:] = [
        part
        for part in parts
        if (part.get("node") or {}).get("id") != "transport_bucket_stress_resistance_membrane_spillovers"
    ]
    next_order = max((part.get("order", 0) or 0 for part in parts), default=0) + 1
    parts.append(
        {
            "order": next_order,
            "role": "Transport-bucket stress-resistance membrane spillovers",
            "node": {
                "id": "transport_bucket_stress_resistance_membrane_spillovers",
                "label": "Transport-bucket stress-resistance membrane spillovers",
                "module_type": "BIOLOGICAL_PROCESS",
                "description": "Transport/membrane/efflux partition extension for paraquat-inducible, fusaric-acid-resistance, TerB, holin/immunity, phage, Cid, and toxin-domain membrane side nodes.",
                "annotons": [
                    *(module_annoton(by_gene[gene]) for gene in ["PP_0598", "PP_0599", "PP_2577", "PP_5745"]),
                    module_annoton(by_gene["PP_1264"]),
                    module_annoton(by_gene["PP_1487"]),
                    *(module_annoton(by_gene[gene]) for gene in ["PP_1559", "PP_3040", "PP_3884", "cidA", "cidB"]),
                    *(module_annoton(by_gene[gene]) for gene in ["PP_1425", "PP_1576", "PP_2076", "PP_2612", "PP_3388", "PP_3616", "PP_5065"]),
                    module_annoton(by_gene["nfrB"]),
                    module_annoton(by_gene["PP_3865"]),
                ],
            },
        }
    )
    MODULE_PATH.write_text(yaml.safe_dump(doc, sort_keys=False, width=120), encoding="utf-8")


def main() -> None:
    rows = load_rows()
    infos = [curate_gene(row) for row in rows]
    extend_module(infos)
    print(f"Curated {len(infos)} genes")
    print(f"Extended {MODULE_PATH}")


if __name__ == "__main__":
    main()
