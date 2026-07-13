#!/usr/bin/env python3
"""First-pass curation for sigma, anti-sigma, and anti-anti-sigma regulators."""

from __future__ import annotations

import csv
import re
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes" / "PSEPK"
BATCH_DIR = ROOT / "projects" / "P_PUTIDA" / "batches"
BATCH_TSV = BATCH_DIR / "module_regulation_signal_transduction_sigma_anti_sigma_and_sigma_factors.tsv"
PARTITION_TSV = BATCH_DIR / "module_regulation_signal_transduction_partition.tsv"
MODULE_PATH = ROOT / "modules" / "sigma_anti_sigma_regulation_boundary.yaml"
TODAY = "2026-07-10"
PRESERVE_EXISTING_REVIEWS = {"rpoS", "pvdS", "rpoH"}


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):  # type: ignore[override]
        return True


def term(go_id: str, label: str) -> dict[str, str]:
    return {"id": go_id, "label": label}


TERM = {
    "GO:0003677": term("GO:0003677", "DNA binding"),
    "GO:0003700": term("GO:0003700", "DNA-binding transcription factor activity"),
    "GO:0005886": term("GO:0005886", "plasma membrane"),
    "GO:0006352": term("GO:0006352", "DNA-templated transcription initiation"),
    "GO:0006355": term("GO:0006355", "regulation of DNA-templated transcription"),
    "GO:0006417": term("GO:0006417", "regulation of translation"),
    "GO:0006950": term("GO:0006950", "response to stress"),
    "GO:0009408": term("GO:0009408", "response to heat"),
    "GO:0016020": term("GO:0016020", "membrane"),
    "GO:0016987": term("GO:0016987", "sigma factor activity"),
    "GO:0016989": term("GO:0016989", "sigma factor antagonist activity"),
    "GO:0030288": term("GO:0030288", "outer membrane-bounded periplasmic space"),
    "GO:0032885": term("GO:0032885", "regulation of polysaccharide biosynthetic process"),
    "GO:0042597": term("GO:0042597", "periplasmic space"),
    "GO:0043856": term("GO:0043856", "anti-sigma factor antagonist activity"),
    "GO:0045152": term("GO:0045152", "antisigma factor binding"),
    "GO:0045892": term("GO:0045892", "negative regulation of DNA-templated transcription"),
    "GO:0045893": term("GO:0045893", "positive regulation of DNA-templated transcription"),
    "GO:2000142": term("GO:2000142", "regulation of DNA-templated transcription initiation"),
}


SIGMA_GENES = {"PP_0865", "PP_0994", "PP_1008", "rpoE", "PP_2088", "PP_2888", "PP_3006", "PP_4208", "PP_4608"}
MUC_SIGMA_SYSTEM = {"rpoE", "mucA", "mucB"}
RSKA_SIGK_SYSTEM = {"PP_3005", "PP_3006"}


def batch_rows() -> dict[str, dict[str, str]]:
    with BATCH_TSV.open(encoding="utf-8") as handle:
        return {row["gene"]: row for row in csv.DictReader(handle, delimiter="\t")}


BATCH_ROWS = batch_rows()


def gene_path(gene: str, suffix: str) -> Path:
    return GENE_ROOT / gene / f"{gene}-{suffix}"


def file_id(gene: str, suffix: str) -> str:
    return f"file:PSEPK/{gene}/{gene}-{suffix}"


def read_lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8").splitlines()


def first_line(path: Path, contains: str) -> str | None:
    if not path.exists():
        return None
    for line in read_lines(path):
        if contains in line:
            return line.strip()
    return None


def support(reference_id: str, supporting_text: str) -> dict[str, str]:
    return {"reference_id": reference_id, "supporting_text": supporting_text}


def add_support(items: list[dict[str, str]], item: dict[str, str] | None) -> None:
    if item and item["supporting_text"] and item not in items:
        items.append(item)


def goa_rows(gene: str) -> dict[str, dict[str, str]]:
    with gene_path(gene, "goa.tsv").open(encoding="utf-8") as handle:
        return {row["GO TERM"]: row for row in csv.DictReader(handle, delimiter="\t")}


def goa_line(gene: str, go_id: str) -> str:
    rows = read_lines(gene_path(gene, "goa.tsv"))
    for line in rows[1:]:
        if f"\t{go_id}\t" in line:
            return line
    raise KeyError(f"No GOA row for {gene} {go_id}")


def goa_support(gene: str, go_id: str) -> dict[str, str]:
    return support(file_id(gene, "goa.tsv"), goa_line(gene, go_id))


def uniprot_support_lines(gene: str, gene_class: str) -> list[dict[str, str]]:
    path = gene_path(gene, "uniprot.txt")
    items: list[dict[str, str]] = []
    for needle in ("DE   RecName:", "DE   SubName:", "DE   AltName:", "GN   OrderedLocusNames="):
        line = first_line(path, needle)
        if line:
            add_support(items, support(file_id(gene, "uniprot.txt"), line))
            break
    if gene_class in {"sigma", "preserved_sigma"}:
        for needle in (
            "SIMILARITY: Belongs to the sigma-70 factor family",
            "DR   InterPro; IPR007627; RNA_pol_sigma70_r2.",
            "DR   InterPro; IPR013249; RNA_pol_sigma70_r4_t2.",
            "KW   Sigma factor",
        ):
            line = first_line(path, needle)
            if line:
                add_support(items, support(file_id(gene, "uniprot.txt"), line))
    elif gene_class == "mucA":
        for needle in ("SUBCELLULAR LOCATION: Cell membrane", "SIMILARITY: Belongs to the RseA family.", "Anti-sigma_E_RseA"):
            line = first_line(path, needle)
            if line:
                add_support(items, support(file_id(gene, "uniprot.txt"), line))
    elif gene_class == "mucB":
        for needle in ("SUBCELLULAR LOCATION: Periplasm", "SIMILARITY: Belongs to the RseB family.", "MucB_RseB"):
            line = first_line(path, needle)
            if line:
                add_support(items, support(file_id(gene, "uniprot.txt"), line))
    elif gene_class == "anti_anti":
        for needle in ("SubName: Full=Anti-anti-sigma factor", "DR   InterPro; IPR002645; STAS_dom."):
            line = first_line(path, needle)
            if line:
                add_support(items, support(file_id(gene, "uniprot.txt"), line))
    elif gene_class == "rskA":
        for needle in (
            "AltName: Full=Sigma-K anti-sigma factor RskA",
            "SUBCELLULAR LOCATION: Cell membrane",
            "DR   InterPro; IPR051474; Anti-sigma-K/W_factor.",
        ):
            line = first_line(path, needle)
            if line:
                add_support(items, support(file_id(gene, "uniprot.txt"), line))
    return items


def asta_support_lines(gene: str, gene_class: str) -> list[dict[str, str]]:
    path = gene_path(gene, "deep-research-asta.md")
    items: list[dict[str, str]] = []
    for needle in ("**Protein Description:**", "protein_description:"):
        line = first_line(path, needle)
        if line:
            add_support(items, support(file_id(gene, "deep-research-asta.md"), line))
            break
    if gene_class in {"sigma", "preserved_sigma"}:
        for needle in ("**Protein Family:** Belongs to the sigma-70 factor family", "**Key Domains:**"):
            line = first_line(path, needle)
            if line:
                add_support(items, support(file_id(gene, "deep-research-asta.md"), line))
    elif gene_class in {"mucA", "mucB", "rskA", "anti_anti"}:
        line = first_line(path, "**Key Domains:**")
        if line:
            add_support(items, support(file_id(gene, "deep-research-asta.md"), line))
    return items


def evidence_for(gene: str, go_id: str | None = None) -> list[dict[str, str]]:
    info = GENE_INFO[gene]
    items: list[dict[str, str]] = []
    if go_id:
        add_support(items, goa_support(gene, go_id))
    for item in uniprot_support_lines(gene, info["class"]):
        add_support(items, item)
    for item in asta_support_lines(gene, info["class"]):
        add_support(items, item)
    return items


def make_gene_info() -> dict[str, dict[str, object]]:
    out: dict[str, dict[str, object]] = {}
    for gene, row in BATCH_ROWS.items():
        product = row["protein_name"]
        accession = row["uniprot_accession"]
        if gene in PRESERVE_EXISTING_REVIEWS:
            out[gene] = {
                "class": "preserved_sigma",
                "accession": accession,
                "role": f"existing curated {product}",
                "description": f"Existing curated review preserved for {gene}.",
                "core_mf": "GO:0016987",
                "core_processes": ["GO:0006352", "GO:2000142"],
                "locations": [],
                "part": "global_stress_sigma_factors",
            }
        elif gene in SIGMA_GENES:
            out[gene] = {
                "class": "sigma",
                "accession": accession,
                "role": "ECF sigma factor controlling promoter selection and transcription initiation",
                "description": (
                    f"{gene} encodes a predicted ECF-subfamily sigma-70 factor in Pseudomonas putida KT2440. "
                    "The UniProt and Asta retrieval metadata support conserved sigma-70 region domains and sigma-factor "
                    "family membership, so the first-pass core function is sigma factor activity in transcription initiation; "
                    "the direct regulon and inducing signal remain unresolved."
                ),
                "core_mf": "GO:0016987",
                "core_processes": ["GO:0006352", "GO:2000142"],
                "locations": [],
                "part": "orphan_ecf_sigma_factors",
            }
        elif gene == "mucA":
            out[gene] = {
                "class": "mucA",
                "accession": accession,
                "role": "membrane anti-sigma factor for AlgU/RpoE-family transcription control",
                "description": (
                    "mucA encodes the membrane-associated negative regulatory protein for the AlgU/RpoE sigma-factor system. "
                    "RseA-like anti-sigma domains and cell-membrane localization support sigma factor antagonist activity that "
                    "negatively regulates DNA-templated transcription."
                ),
                "core_mf": "GO:0016989",
                "core_processes": ["GO:0045892"],
                "locations": ["GO:0005886"],
                "part": "muc_algU_sigma_anti_sigma_system",
            }
        elif gene == "mucB":
            out[gene] = {
                "class": "mucB",
                "accession": accession,
                "role": "periplasmic MucB/RseB anti-sigma partner that binds the anti-sigma factor",
                "description": (
                    "mucB encodes a periplasmic MucB/RseB-family regulator in the AlgU/RpoE sigma-factor control system. "
                    "The most direct supported molecular function is antisigma factor binding in the periplasm; polysaccharide "
                    "biosynthesis regulation is retained as pathway context rather than a standalone core function in this first pass."
                ),
                "core_mf": "GO:0045152",
                "core_processes": [],
                "locations": ["GO:0042597"],
                "part": "muc_algU_sigma_anti_sigma_system",
            }
        elif gene == "PP_2166":
            out[gene] = {
                "class": "anti_anti",
                "accession": accession,
                "role": "anti-anti-sigma factor that can positively regulate transcription by relieving anti-sigma inhibition",
                "description": (
                    "PP_2166 encodes a predicted STAS-domain anti-anti-sigma factor. The first-pass supported role is anti-sigma "
                    "factor antagonist activity, with positive regulation of DNA-templated transcription as the expected regulatory outcome."
                ),
                "core_mf": "GO:0043856",
                "core_processes": ["GO:0045893"],
                "locations": [],
                "part": "anti_anti_sigma_factor",
            }
        elif gene == "PP_3005":
            out[gene] = {
                "class": "rskA",
                "accession": accession,
                "role": "membrane sigma-K anti-sigma factor RskA candidate",
                "description": (
                    "PP_3005 encodes a predicted membrane anti-sigma factor annotated as regulator of SigK/RskA. "
                    "Anti-sigma-K/W-factor domain evidence supports sigma factor antagonist activity and negative regulation "
                    "of transcription, while the TreeGrafter regulation-of-translation row is not supported by the protein family context."
                ),
                "core_mf": "GO:0016989",
                "core_processes": ["GO:0045892"],
                "locations": ["GO:0005886", "GO:0016020"],
                "part": "rskA_sigK_sigma_anti_sigma_system",
            }
        else:
            raise KeyError(gene)
    return out


GENE_INFO = make_gene_info()


def replacement(go_id: str) -> list[dict[str, str]]:
    return [TERM[go_id]]


def review_decision(gene: str, go_id: str) -> tuple[str, str, list[dict[str, str]] | None]:
    gene_class = GENE_INFO[gene]["class"]
    if gene_class == "sigma":
        if go_id == "GO:0003677":
            return (
                "MARK_AS_OVER_ANNOTATED",
                "Generic DNA binding is plausible for promoter-recognition domains but too broad for a sigma factor; sigma factor activity is the informative molecular function.",
                replacement("GO:0016987"),
            )
        if go_id == "GO:0003700":
            return (
                "MODIFY",
                "The annotation captures transcription control, but bacterial sigma factors are more specifically represented by sigma factor activity.",
                replacement("GO:0016987"),
            )
        if go_id == "GO:0006352":
            return ("ACCEPT", "Sigma factors direct RNA polymerase promoter recognition during transcription initiation.", None)
        if go_id == "GO:0006355":
            return (
                "MODIFY",
                "Broad transcription regulation is correct context, but regulation of transcription initiation better matches sigma-factor mechanism.",
                replacement("GO:2000142"),
            )
        if go_id == "GO:0006950":
            return (
                "KEEP_AS_NON_CORE",
                "The RpoE/ECF-sigma family context supports stress-response regulation, but this generic stress-response row is less direct than sigma factor activity and transcription-initiation control.",
                None,
            )
        if go_id == "GO:0016987":
            return ("ACCEPT", "Sigma factor activity is the core molecular function supported by sigma-70-family domain evidence.", None)
        if go_id == "GO:2000142":
            return ("ACCEPT", "Sigma factor activity regulates transcription initiation by changing promoter selection.", None)
    if gene_class == "mucA":
        if go_id == "GO:0005886":
            return ("ACCEPT", "UniProt places this RseA-like anti-sigma protein at the cell membrane.", None)
        if go_id == "GO:0016989":
            return ("ACCEPT", "RseA-like anti-sigma domains support sigma factor antagonist activity as the core molecular function.", None)
        if go_id == "GO:0045892":
            return ("ACCEPT", "Anti-sigma activity directly restrains sigma-dependent transcription, supporting negative regulation of transcription.", None)
    if gene_class == "mucB":
        if go_id == "GO:0030288":
            return ("ACCEPT", "MucB/RseB-family evidence supports a periplasmic anti-sigma-system partner, consistent with this specific periplasmic-space annotation.", None)
        if go_id == "GO:0032885":
            return (
                "KEEP_AS_NON_CORE",
                "AlgU/Muc regulation is plausibly connected to polysaccharide biology, but the direct first-pass molecular role for MucB is antisigma factor binding.",
                None,
            )
        if go_id == "GO:0042597":
            return ("ACCEPT", "UniProt places MucB in the periplasm, supporting periplasmic-space localization.", None)
        if go_id == "GO:0045152":
            return ("ACCEPT", "MucB/RseB-family domain evidence supports antisigma factor binding as the most direct molecular function.", None)
    if gene_class == "anti_anti":
        if go_id == "GO:0043856":
            return ("ACCEPT", "The product name and STAS-domain context support anti-sigma factor antagonist activity.", None)
        if go_id == "GO:0045893":
            return ("ACCEPT", "An anti-anti-sigma factor can positively regulate transcription by relieving anti-sigma inhibition.", None)
    if gene_class == "rskA":
        if go_id == "GO:0005886":
            return ("ACCEPT", "UniProt places the predicted RskA anti-sigma factor at the cell membrane.", None)
        if go_id == "GO:0006417":
            return (
                "REMOVE",
                "The protein is a predicted anti-sigma factor for transcriptional control; the current evidence does not support regulation of translation.",
                None,
            )
        if go_id == "GO:0016020":
            return ("ACCEPT", "Membrane localization is supported by UniProt membrane and transmembrane annotations.", None)
        if go_id == "GO:0016989":
            return ("ACCEPT", "Anti-sigma-K/W-factor domain evidence supports sigma factor antagonist activity.", None)
        if go_id == "GO:0045892":
            return ("ACCEPT", "Sigma-factor antagonism is a direct mechanism for negative regulation of DNA-templated transcription.", None)
    raise KeyError(f"Unhandled annotation {gene} {go_id}")


def review_for(gene: str, go_id: str) -> dict[str, object]:
    action, reason, replacements = review_decision(gene, go_id)
    out: dict[str, object] = {
        "summary": reason,
        "action": action,
        "reason": reason,
        "supported_by": evidence_for(gene, go_id),
    }
    if replacements:
        out["proposed_replacement_terms"] = replacements
    return out


def normalize_go_ref_titles(doc: dict[str, object]) -> None:
    for ref in doc.get("references", []):
        if isinstance(ref, dict) and str(ref.get("id", "")).startswith("GO_REF:") and str(ref.get("title", "")).startswith("TODO:"):
            ref["title"] = f"Gene Ontology annotation reference {ref['id']}"


def references_for(gene: str, data: dict[str, object]) -> list[dict[str, object]]:
    refs = list(data.get("references", []))
    seen = {ref.get("id") for ref in refs if isinstance(ref, dict)}
    additions: list[dict[str, object]] = [
        {
            "id": file_id(gene, "goa.tsv"),
            "title": f"QuickGO GOA annotations for {gene}",
            "findings": [{"supporting_text": goa_line(gene, go_id)} for go_id in goa_rows(gene)],
        },
        {
            "id": file_id(gene, "uniprot.txt"),
            "title": f"UniProtKB entry for {gene} ({GENE_INFO[gene]['accession']})",
            "findings": [{"supporting_text": item["supporting_text"]} for item in uniprot_support_lines(gene, str(GENE_INFO[gene]["class"]))],
        },
        {
            "id": file_id(gene, "deep-research-asta.md"),
            "title": f"Asta retrieval report for {gene} ({GENE_INFO[gene]['accession']})",
            "findings": [{"supporting_text": item["supporting_text"]} for item in asta_support_lines(gene, str(GENE_INFO[gene]["class"]))],
        },
    ]
    for ref in additions:
        if ref["id"] not in seen:
            refs.append(ref)
            seen.add(ref["id"])
    return refs


def core_function(gene: str) -> dict[str, object]:
    info = GENE_INFO[gene]
    core: dict[str, object] = {
        "description": info["role"],
        "molecular_function": TERM[str(info["core_mf"])],
        "supported_by": evidence_for(gene, str(info["core_mf"])),
    }
    processes = [TERM[x] for x in info["core_processes"]]
    if processes:
        core["directly_involved_in"] = processes
        for go_id in info["core_processes"]:
            add_support(core["supported_by"], goa_support(gene, str(go_id)))  # type: ignore[arg-type]
    locations = [TERM[x] for x in info["locations"]]
    if locations:
        core["locations"] = locations
        for go_id in info["locations"]:
            add_support(core["supported_by"], goa_support(gene, str(go_id)))  # type: ignore[arg-type]
    return core


def suggested_questions(gene: str) -> list[dict[str, object]]:
    info = GENE_INFO[gene]
    if info["class"] == "sigma":
        question = f"Which promoters, inducing cues, and anti-sigma partners define the direct regulon of {gene}?"
    elif info["class"] == "mucB":
        question = "Which anti-sigma partner and envelope cues place MucB in the KT2440 AlgU/RpoE regulatory circuit?"
    elif info["class"] == "anti_anti":
        question = "Which anti-sigma factor is antagonized by PP_2166, and under which environmental signal?"
    else:
        question = f"What direct sigma partner, signal, and regulon are controlled by {gene}?"
    return [{"question": question, "experts": []}]


def suggested_experiments(gene: str) -> list[dict[str, str]]:
    info = GENE_INFO[gene]
    if info["class"] == "sigma":
        description = (
            f"Map the {gene} regulon using perturbation RNA-seq, promoter motif enrichment, and sigma-dependent promoter-reporter assays."
        )
    else:
        description = (
            f"Test {gene}-dependent sigma-factor regulation using deletion/complementation, reporter assays, and partner-interaction assays."
        )
    return [{"experiment_type": "regulatory network mapping", "description": description}]


def write_notes(gene: str) -> None:
    info = GENE_INFO[gene]
    path = gene_path(gene, "notes.md")
    heading = f"## {TODAY} sigma/anti-sigma first pass"
    lines = [
        heading,
        "",
        f"- Batch: `{BATCH_TSV.relative_to(ROOT)}`.",
        f"- Main conclusion: {info['role']}.",
    ]
    if gene in PRESERVE_EXISTING_REVIEWS:
        lines.append("- Existing curated YAML decisions were preserved; Asta retrieval is available for future follow-up but was not used to rewrite this review.")
    else:
        lines.append("- This is a light first pass anchored to GOA, UniProt, and Asta retrieval metadata; direct regulons and inducing signals remain unresolved unless already curated.")
    lines.extend(["", "Primary provenance:"])
    for item in evidence_for(gene, str(info["core_mf"]))[:6]:
        lines.append(f"- [{item['reference_id']} \"{item['supporting_text']}\"]")
    lines.append("")
    block = "\n".join(lines)
    if path.exists():
        existing = path.read_text(encoding="utf-8")
        if heading not in existing:
            path.write_text(existing.rstrip() + "\n\n" + block, encoding="utf-8")
    else:
        path.write_text(f"# {gene} notes\n\n{block}", encoding="utf-8")


def curate_gene(gene: str) -> None:
    if gene in PRESERVE_EXISTING_REVIEWS:
        write_notes(gene)
        print(f"Preserved existing curated review for {gene}")
        return
    path = gene_path(gene, "ai-review.yaml")
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    data["status"] = "DRAFT"
    data["description"] = GENE_INFO[gene]["description"]
    data["references"] = references_for(gene, data)
    normalize_go_ref_titles(data)
    for annotation in data.get("existing_annotations", []):
        annotation["review"] = review_for(gene, annotation["term"]["id"])
    data["core_functions"] = [core_function(gene)]
    data["proposed_new_terms"] = []
    data["suggested_questions"] = suggested_questions(gene)
    data["suggested_experiments"] = suggested_experiments(gene)
    path.write_text(
        yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, width=120, allow_unicode=False),
        encoding="utf-8",
    )
    write_notes(gene)
    print(f"Curated {path.relative_to(ROOT)}")


def clean_id(value: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9_]+", "_", value.lower())
    return re.sub(r"_+", "_", cleaned).strip("_")


def module_term(go_id: str, description: str | None = None) -> dict[str, object]:
    out: dict[str, object] = {"preferred_term": TERM[go_id]["label"], "term": TERM[go_id]}
    if description:
        out["description"] = description
    return out


def annoton(gene: str, role: str | None = None, processes: list[str] | None = None, locations: list[str] | None = None) -> dict[str, object]:
    info = GENE_INFO[gene]
    process_ids = processes if processes is not None else list(info["core_processes"])
    location_ids = locations if locations is not None else list(info["locations"])
    out: dict[str, object] = {
        "id": f"{clean_id(gene)}_{clean_id(str(info['role']))}",
        "label": f"{gene}: {info['role']}",
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "role_description": role or str(info["role"]),
        "function": {"preferred_term": TERM[str(info["core_mf"])]["label"], "term": TERM[str(info["core_mf"])]},
    }
    if process_ids:
        out["processes"] = [{"preferred_term": TERM[x]["label"], "term": TERM[x]} for x in process_ids]
    if location_ids:
        out["locations"] = [{"preferred_term": TERM[x]["label"], "term": TERM[x]} for x in location_ids]
    return out


def part(order: int, part_id: str, label: str, description: str, genes: list[str], connections: list[dict[str, str]] | None = None) -> dict[str, object]:
    node: dict[str, object] = {
        "id": part_id,
        "label": label,
        "module_type": "REGULATORY_STEP",
        "description": description,
        "annotons": [annoton(gene) for gene in genes],
    }
    if connections:
        node["connections"] = connections
    return {"order": order, "role": label, "node": node}


def write_module() -> None:
    evidence: list[dict[str, str]] = [
        {
            "source_id": f"file:{BATCH_TSV.relative_to(ROOT)}",
            "title": "PSEPK regulation/signal-transduction sigma/anti-sigma split",
            "statement": "The batch table records 16 sigma, anti-sigma, and anti-anti-sigma regulators handled in this first pass.",
        },
        {
            "source_id": f"file:{PARTITION_TSV.relative_to(ROOT)}",
            "title": "PSEPK regulation/signal-transduction partition table",
            "statement": "The regulation umbrella was partitioned into family-scale regulator splits; this module covers the sigma/anti-sigma split.",
        },
    ]
    for gene in BATCH_ROWS:
        evidence.append(
            {
                "source_id": file_id(gene, "ai-review.yaml"),
                "title": f"Curated {gene} review",
                "statement": str(GENE_INFO[gene]["role"]),
            }
        )

    orphan_sigma = ["PP_0865", "PP_0994", "PP_1008", "PP_2088", "PP_2888", "PP_4208", "pvdS", "PP_4608"]
    module = {
        "id": "MODULE:sigma_anti_sigma_regulation_boundary",
        "title": "Sigma and anti-sigma regulation boundary",
        "description": (
            "Boundary module for the PSEPK regulation/signal-transduction sigma split. It groups ECF sigma factors, "
            "global stress sigma factors, and anti-sigma or anti-anti-sigma regulators while leaving direct regulons "
            "and inducing cues unresolved unless supported by an existing curated review."
        ),
        "status": "DRAFT",
        "evidence": evidence,
        "notes": (
            "This module is broader than the ppu02020 ECF sigma/anti-sigma boundary. It is a genome-curation work unit, "
            "not a single linear pathway."
        ),
        "module": {
            "id": "sigma_anti_sigma_regulation_boundary",
            "label": "Sigma and anti-sigma regulation boundary",
            "module_type": "SIGNALING_PATHWAY",
            "concepts": [
                module_term("GO:0016987", "Core sigma-factor molecular function for ECF, RpoS, RpoH, and PvdS entries."),
                module_term("GO:0016989", "Anti-sigma molecular function for membrane anti-sigma regulators."),
                module_term("GO:0045152", "MucB/RseB anti-sigma-partner binding activity."),
                module_term("GO:0043856", "Anti-anti-sigma molecular function for STAS-domain regulators."),
                module_term("GO:0006352", "Direct process for sigma-dependent promoter recognition."),
                module_term("GO:2000142", "Specific transcription-initiation regulation process preferred over broad transcription regulation."),
                module_term("GO:0045892", "Process output for anti-sigma-dependent repression of transcription."),
                module_term("GO:0045893", "Process output for anti-anti-sigma relief of anti-sigma inhibition."),
            ],
            "context": {
                "cellular_components": [
                    module_term("GO:0005886"),
                    module_term("GO:0016020"),
                    module_term("GO:0042597"),
                    module_term("GO:0030288"),
                ]
            },
            "parts": [
                part(
                    1,
                    "orphan_and_contextual_ecf_sigma_factors",
                    "Orphan and contextual ECF sigma factors",
                    "ECF sigma factors whose direct regulons or anti-sigma partners are unresolved in this first pass.",
                    orphan_sigma,
                ),
                part(
                    2,
                    "muc_algU_sigma_anti_sigma_system",
                    "Muc/AlgU sigma anti-sigma system",
                    "rpoE/AlgU-family sigma factor with adjacent MucA anti-sigma and MucB/RseB periplasmic partner.",
                    ["rpoE", "mucA", "mucB"],
                    [
                        {
                            "source": clean_id("mucA_" + str(GENE_INFO["mucA"]["role"])),
                            "target": clean_id("rpoE_" + str(GENE_INFO["rpoE"]["role"])),
                            "connection_type": "NEGATIVELY_REGULATES",
                            "description": "MucA is the predicted membrane anti-sigma regulator for the AlgU/RpoE-family sigma factor.",
                        },
                        {
                            "source": clean_id("mucB_" + str(GENE_INFO["mucB"]["role"])),
                            "target": clean_id("mucA_" + str(GENE_INFO["mucA"]["role"])),
                            "connection_type": "PART_OF",
                            "description": "MucB/RseB-family proteins bind anti-sigma factors in the periplasmic arm of the AlgU/RpoE system.",
                        },
                    ],
                ),
                part(
                    3,
                    "rskA_sigK_sigma_anti_sigma_system",
                    "RskA/SigK sigma anti-sigma system",
                    "PP_3005 is a membrane RskA-like anti-sigma candidate adjacent to the PP_3006 ECF sigma factor.",
                    ["PP_3005", "PP_3006"],
                    [
                        {
                            "source": clean_id("PP_3005_" + str(GENE_INFO["PP_3005"]["role"])),
                            "target": clean_id("PP_3006_" + str(GENE_INFO["PP_3006"]["role"])),
                            "connection_type": "NEGATIVELY_REGULATES",
                            "description": "PP_3005 is the predicted RskA-like anti-sigma regulator for the adjacent PP_3006 ECF sigma factor.",
                        }
                    ],
                ),
                part(
                    4,
                    "anti_anti_sigma_factor",
                    "Anti-anti-sigma factor",
                    "PP_2166 is retained as a STAS-domain anti-anti-sigma regulatory node with unknown direct partner.",
                    ["PP_2166"],
                ),
                part(
                    5,
                    "global_stress_sigma_factors",
                    "Global stress and heat-shock sigma factors",
                    "Existing curated RpoS and RpoH reviews are preserved as non-ECF sigma-factor context in the same regulation split.",
                    ["rpoS", "rpoH"],
                ),
            ],
        },
    }
    MODULE_PATH.write_text(
        yaml.dump(module, Dumper=NoAliasDumper, sort_keys=False, width=120, allow_unicode=False),
        encoding="utf-8",
    )
    print(f"Wrote {MODULE_PATH.relative_to(ROOT)}")


def main() -> None:
    for gene in BATCH_ROWS:
        curate_gene(gene)
    write_module()


if __name__ == "__main__":
    main()
