#!/usr/bin/env python3
"""First-pass curation for ppu02040 flagellar export/assembly genes."""

from __future__ import annotations

from pathlib import Path

import yaml


SPECIES = "PSEPK"
ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes" / SPECIES


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


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
    "GO_REF:0000108": "Automatic transfer of experimentally-verified manual GO annotation data to orthologs using Ensembl Compara",
    "GO_REF:0000118": "TreeGrafter-generated GO annotations",
    "GO_REF:0000120": "Combined Automated Annotation using Multiple IEA Methods",
}


def term(term_id: str, label: str) -> dict[str, str]:
    return {"id": term_id, "label": label}


def support(reference_id: str, text: str) -> dict[str, str]:
    return {"reference_id": reference_id, "supporting_text": text}


def ref_id(gene: str, suffix: str) -> str:
    return f"file:{SPECIES}/{gene}/{gene}-{suffix}"


def find_line(path: Path, needle: str) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if needle in line:
            return line
    raise ValueError(f"{needle!r} not found in {path}")


def goa_line(gene: str, term_id: str) -> dict[str, str]:
    path = GENE_ROOT / gene / f"{gene}-goa.tsv"
    return support(ref_id(gene, "goa.tsv"), find_line(path, term_id))


def uniprot_line(gene: str, needle: str) -> dict[str, str]:
    path = GENE_ROOT / gene / f"{gene}-uniprot.txt"
    return support(ref_id(gene, "uniprot.txt"), find_line(path, needle))


def asta_line(gene: str, needle: str = "- **Protein Description:**") -> dict[str, str]:
    path = GENE_ROOT / gene / f"{gene}-deep-research-asta.md"
    return support(ref_id(gene, "deep-research-asta.md"), find_line(path, needle))


def uniq_support(items: list[dict[str, str]]) -> list[dict[str, str]]:
    seen: set[tuple[str, str]] = set()
    out = []
    for item in items:
        key = (item["reference_id"], item["supporting_text"])
        if key not in seen:
            out.append(item)
            seen.add(key)
    return out


def make_review(
    gene: str,
    term_id: str,
    label: str,
    action: str,
    reason: str,
    summary: str | None = None,
    extra_support: list[dict[str, str]] | None = None,
    replacements: list[dict[str, str]] | None = None,
) -> dict:
    if summary is None:
        summary = f"{label} was reviewed for {gene} in the ppu02040 flagellar export/assembly first pass."
    supported_by = [goa_line(gene, term_id), asta_line(gene)]
    if extra_support:
        supported_by.extend(extra_support)
    review = {
        "summary": summary,
        "action": action,
        "reason": reason,
        "supported_by": uniq_support(supported_by),
    }
    if replacements:
        review["proposed_replacement_terms"] = replacements
    return review


def file_reference(gene: str, suffix: str, title: str, statement: str) -> dict:
    path = GENE_ROOT / gene / f"{gene}-{suffix}"
    return {
        "id": ref_id(gene, suffix),
        "title": title,
        "findings": [{"statement": statement}],
    } if path.exists() else {}


def normalize_references(existing: list[dict], gene: str) -> list[dict]:
    refs: list[dict] = []
    seen: set[str] = set()
    for entry in existing or []:
        ref = dict(entry)
        ref_id_value = ref.get("id")
        if not ref_id_value or ref_id_value in seen:
            continue
        if ref_id_value in GO_REF_TITLES:
            ref = {"id": ref_id_value, "title": GO_REF_TITLES[ref_id_value], "findings": []}
        refs.append(ref)
        seen.add(ref_id_value)

    for ref in [
        file_reference(
            gene,
            "uniprot.txt",
            f"UniProtKB entry for {gene}",
            "UniProt protein names, family assignments, domains, subcellular-location lines, and GO cross-references used for first-pass curation.",
        ),
        file_reference(
            gene,
            "goa.tsv",
            f"QuickGO GOA annotations for {gene}",
            "Fetched GOA rows reviewed in this first-pass curation file.",
        ),
        file_reference(
            gene,
            "deep-research-asta.md",
            f"Asta retrieval report for {gene}",
            "Asta retrieval was used as fast gene-level metadata support; it was not used to introduce unsupported hypotheses.",
        ),
    ]:
        ref_id_value = ref.get("id")
        if ref_id_value and ref_id_value not in seen:
            refs.append(ref)
            seen.add(ref_id_value)
    return refs


GATE_REASON = (
    "The UniProt family/domain calls place this protein in the conserved flagellar/type-III-like export apparatus. "
    "In this first pass the pathway-defining interpretation is bacterial-type flagellum assembly/export, not a separate generic secretion pathway."
)
GENERIC_MEMBRANE_REASON = (
    "Generic membrane localization is true for this membrane-associated flagellar export component, but it is less informative than the plasma-membrane or basal-body location already present."
)


GENES: dict[str, dict] = {
    "flhA": {
        "description": (
            "flhA encodes a multi-pass membrane FlhA/FHIPEP-family component of the flagellar export apparatus in Pseudomonas putida KT2440. "
            "It acts in the type-III-like flagellar export gate used for rod and filament assembly, providing membrane export-apparatus context rather than a standalone secreted protein function."
        ),
        "core": {
            "description": "Multi-pass FlhA/FHIPEP-family membrane export-gate component required for flagellar rod/filament assembly.",
            "directly_involved_in": [term("GO:0044780", "bacterial-type flagellum assembly")],
            "locations": [term("GO:0005886", "plasma membrane")],
        },
        "extra_core_support": [
            ("uniprot", "-!- FUNCTION: Required for formation of the rod structure of the flagellar"),
            ("uniprot", "apparatus. Together with FliI and FliH, may constitute the export"),
            ("uniprot", "DR   Pfam; PF00771; FHIPEP; 1."),
        ],
        "decisions": {
            "GO:0005886": ("ACCEPT", "Plasma membrane localization matches the multi-pass FlhA export-gate subunit.", None),
            "GO:0009306": ("KEEP_AS_NON_CORE", GATE_REASON, None),
            "GO:0016020": ("MARK_AS_OVER_ANNOTATED", GENERIC_MEMBRANE_REASON, None),
            "GO:0044780": ("ACCEPT", "Flagellum assembly is the pathway-defining FlhA role supported by UniProt function and FlhA/FHIPEP domain evidence.", None),
        },
    },
    "flhB": {
        "description": (
            "flhB encodes a multi-pass membrane FlhB/type-III secretion exporter-family component of the KT2440 flagellar export apparatus. "
            "It supports rod and basal-body formation and flagellin export together with the FliI/FliH cytosolic ATPase/regulator pair."
        ),
        "core": {
            "description": "FlhB/type-III secretion exporter-family membrane component of the flagellar export apparatus.",
            "directly_involved_in": [term("GO:0044780", "bacterial-type flagellum assembly")],
            "locations": [term("GO:0005886", "plasma membrane")],
        },
        "extra_core_support": [
            ("uniprot", "-!- FUNCTION: Required for formation of the rod structure in the basal body"),
            ("uniprot", "the export apparatus of flagellin."),
            ("uniprot", "DR   Pfam; PF01312; Bac_export_2; 1."),
        ],
        "decisions": {
            "GO:0005886": ("ACCEPT", "Plasma membrane localization matches the multi-pass FlhB export-gate subunit.", None),
            "GO:0009306": ("KEEP_AS_NON_CORE", GATE_REASON, None),
            "GO:0015031": ("KEEP_AS_NON_CORE", "Protein transport is compatible with the flagellar export apparatus but less specific than flagellar assembly/export.", None),
            "GO:0016020": ("MARK_AS_OVER_ANNOTATED", GENERIC_MEMBRANE_REASON, None),
            "GO:0044780": ("ACCEPT", "Flagellum assembly is the pathway-defining FlhB role supported by UniProt function and FlhB/exporter-family evidence.", None),
        },
    },
    "fliR": {
        "description": (
            "fliR encodes a multi-pass FliR/MopE/SpaR-family membrane component of the flagellar export gate. "
            "The protein is associated with the plasma membrane and basal body and contributes to flagellar biosynthesis in the KT2440 flagellar cluster."
        ),
        "core": {
            "description": "FliR-family membrane export-gate component for flagellar biosynthesis.",
            "directly_involved_in": [term("GO:0044780", "bacterial-type flagellum assembly")],
            "locations": [term("GO:0005886", "plasma membrane"), term("GO:0009425", "bacterial-type flagellum basal body")],
        },
        "extra_core_support": [
            ("uniprot", "-!- FUNCTION: Role in flagellar biosynthesis."),
            ("uniprot", "DR   Pfam; PF01311; Bac_export_1; 1."),
        ],
        "decisions": {
            "GO:0005886": ("ACCEPT", "Plasma membrane localization matches the multi-pass FliR export-gate subunit.", None),
            "GO:0006605": (
                "MARK_AS_OVER_ANNOTATED",
                "Protein targeting is a broad automated inference; the specific biological context is flagellar export/assembly.",
                [term("GO:0044780", "bacterial-type flagellum assembly")],
            ),
            "GO:0009425": ("ACCEPT", "Basal-body localization is consistent with FliR being a flagellar export-gate component.", None),
            "GO:0016020": ("MARK_AS_OVER_ANNOTATED", GENERIC_MEMBRANE_REASON, None),
            "GO:0044780": ("ACCEPT", "Flagellum assembly is the specific FliR role supported by UniProt function and export-gate domains.", None),
        },
    },
    "fliQ": {
        "description": (
            "fliQ encodes a small multi-pass FliQ/MopD/SpaQ-family component of the flagellar export gate. "
            "It localizes to the membrane/basal-body context and supports bacterial-type flagellum assembly through the flagellum-specific export apparatus."
        ),
        "core": {
            "description": "FliQ-family small membrane export-gate component for flagellar assembly.",
            "directly_involved_in": [term("GO:0044780", "bacterial-type flagellum assembly")],
            "locations": [term("GO:0005886", "plasma membrane"), term("GO:0009425", "bacterial-type flagellum basal body")],
        },
        "extra_core_support": [
            ("uniprot", "-!- FUNCTION: Role in flagellar biosynthesis."),
            ("uniprot", "DR   Pfam; PF01313; Bac_export_3; 1."),
        ],
        "decisions": {
            "GO:0005886": ("ACCEPT", "Plasma membrane localization matches the multi-pass FliQ export-gate subunit.", None),
            "GO:0009306": ("KEEP_AS_NON_CORE", GATE_REASON, None),
            "GO:0009425": ("ACCEPT", "Basal-body localization is consistent with FliQ being a flagellar export-gate component.", None),
            "GO:0016020": ("MARK_AS_OVER_ANNOTATED", GENERIC_MEMBRANE_REASON, None),
            "GO:0044780": ("ACCEPT", "Flagellum assembly is the specific FliQ role supported by UniProt function and FliQ/export-gate domains.", None),
        },
    },
    "fliP": {
        "description": (
            "fliP encodes a multi-pass FliP/MopC/SpaP-family component of the flagellum-specific transport/export system. "
            "In KT2440 it is best treated as a membrane/basal-body export-gate protein required for flagellar organization and assembly."
        ),
        "core": {
            "description": "FliP-family membrane component of the flagellum-specific export system.",
            "directly_involved_in": [term("GO:0044781", "bacterial-type flagellum organization")],
            "locations": [term("GO:0005886", "plasma membrane"), term("GO:0009425", "bacterial-type flagellum basal body")],
        },
        "extra_core_support": [
            ("uniprot", "Plays a role in the flagellum-specific transport system."),
            ("uniprot", "DR   Pfam; PF00813; FliP; 1."),
        ],
        "decisions": {
            "GO:0005886": ("ACCEPT", "Plasma membrane localization matches the multi-pass FliP export-gate subunit.", None),
            "GO:0009306": ("KEEP_AS_NON_CORE", GATE_REASON, None),
            "GO:0009425": ("ACCEPT", "Basal-body localization is consistent with FliP being a flagellar export-gate component.", None),
            "GO:0016020": ("MARK_AS_OVER_ANNOTATED", GENERIC_MEMBRANE_REASON, None),
            "GO:0044781": ("ACCEPT", "Flagellum organization captures FliP's role in the flagellum-specific transport system.", None),
        },
    },
    "fliO": {
        "description": (
            "fliO encodes a single-pass FliO/MopB-family membrane protein in the flagellar export region. "
            "It is associated with the plasma membrane and basal body and is treated here as an accessory factor for bacterial-type flagellum organization."
        ),
        "core": {
            "description": "FliO/MopB-family accessory membrane protein associated with the flagellar export/basal-body region.",
            "directly_involved_in": [term("GO:0044781", "bacterial-type flagellum organization")],
            "locations": [term("GO:0005886", "plasma membrane"), term("GO:0009425", "bacterial-type flagellum basal body")],
        },
        "extra_core_support": [
            ("uniprot", "Belongs to the FliO/MopB family."),
            ("uniprot", "DR   Pfam; PF04347; FliO; 1."),
        ],
        "decisions": {
            "GO:0005886": ("ACCEPT", "Plasma membrane localization matches the FliO membrane protein.", None),
            "GO:0009425": ("ACCEPT", "Basal-body localization is consistent with the FliO flagellar export-region context.", None),
            "GO:0016020": ("MARK_AS_OVER_ANNOTATED", GENERIC_MEMBRANE_REASON, None),
            "GO:0044781": ("ACCEPT", "Flagellum organization captures the conservative FliO/MopB-family role.", None),
        },
    },
    "fliK": {
        "description": (
            "fliK encodes a FliK-family flagellar hook-length control protein. "
            "The KT2440 GOA table is empty, but UniProt and Asta domain metadata support a conservative first-pass role in flagellar hook length control during bacterial-type flagellum assembly."
        ),
        "core": {
            "description": "FliK-family hook-length control factor for flagellar assembly.",
            "directly_involved_in": [term("GO:0044780", "bacterial-type flagellum assembly")],
        },
        "extra_core_support": [
            ("uniprot", "SubName: Full=Flagellar hook-length control protein FliK"),
            ("uniprot", "DR   PANTHER; PTHR37533; FLAGELLAR HOOK-LENGTH CONTROL PROTEIN; 1."),
            ("asta", "- **Key Domains:** Flagellar_hook_control-like_C."),
        ],
        "decisions": {},
    },
    "fliJ": {
        "description": (
            "fliJ encodes a FliJ-family cytoplasmic-side/peripheral membrane component of the flagellar export apparatus. "
            "It is treated as an export-apparatus factor for flagellar organization/protein transport rather than a flagellar motor protein."
        ),
        "core": {
            "description": "FliJ-family cytoplasmic-side export-apparatus component supporting flagellar organization and protein transport.",
            "directly_involved_in": [term("GO:0044781", "bacterial-type flagellum organization")],
            "locations": [term("GO:0005886", "plasma membrane")],
        },
        "extra_core_support": [
            ("uniprot", "Belongs to the FliJ family."),
            ("uniprot", "DR   Pfam; PF02050; FliJ; 1."),
            ("uniprot", "DR   GO; GO:0015031; P:protein transport; IEA:UniProtKB-KW."),
        ],
        "decisions": {
            "GO:0003774": ("REMOVE", "FliJ is an export-apparatus component, not the torque-generating flagellar motor/switch component; this InterPro-derived motor term is over-propagated.", None),
            "GO:0005886": ("ACCEPT", "Plasma-membrane/peripheral membrane localization matches the cytoplasmic-side export-apparatus placement.", None),
            "GO:0006935": ("MARK_AS_OVER_ANNOTATED", "Chemotaxis is an indirect phenotype-level consequence of flagellar function, not the specific FliJ export-apparatus role.", None),
            "GO:0009288": ("KEEP_AS_NON_CORE", "The broad bacterial flagellum component term is plausible but less informative than FliJ export-apparatus context.", None),
            "GO:0016020": ("MARK_AS_OVER_ANNOTATED", "Generic membrane localization is less informative than cytoplasmic-side/peripheral membrane placement.", None),
            "GO:0071973": ("KEEP_AS_NON_CORE", "Flagellum-dependent motility is a downstream process supported by flagellar export, but the core role is assembly/export.", None),
        },
    },
    "fliI": {
        "description": (
            "fliI encodes the ATPase of the flagellar type-III-like export apparatus. "
            "It hydrolyzes ATP for protein export through the flagellar secretion system and supports bacterial-type flagellum assembly; ATP-synthase-like annotations from broader family similarity are not treated as its biological role."
        ),
        "core": {
            "description": "Flagellar export ATPase that powers type-III-like protein secretion during flagellum assembly.",
            "molecular_function": term("GO:0008564", "protein-exporting ATPase activity"),
            "directly_involved_in": [term("GO:0030254", "protein secretion by the type III secretion system"), term("GO:0044780", "bacterial-type flagellum assembly")],
            "locations": [term("GO:0005737", "cytoplasm")],
            "in_complex": term("GO:0030257", "type III protein secretion system complex"),
        },
        "extra_core_support": [
            ("uniprot", "DR   GO; GO:0008564; F:protein-exporting ATPase activity;"),
            ("uniprot", "DR   GO; GO:0030254; P:protein secretion by the type III secretion system;"),
            ("uniprot", "DR   Pfam; PF18269; T3SS_ATPase_C; 1."),
        ],
        "decisions": {
            "GO:0005524": ("KEEP_AS_NON_CORE", "ATP binding is true for FliI but less informative than protein-exporting ATPase activity.", None),
            "GO:0005737": ("ACCEPT", "Cytoplasmic localization matches the soluble ATPase component of the export apparatus.", None),
            "GO:0008564": ("ACCEPT", "Protein-exporting ATPase activity is the specific molecular function of FliI.", None),
            "GO:0015986": ("REMOVE", "FliI is a flagellar export ATPase, not a proton motive force-driven ATP synthase; this is an ATP-synthase-family over-propagation.", None),
            "GO:0016887": ("ACCEPT", "ATP hydrolysis is the catalytic activity underlying FliI protein-exporting ATPase function.", None),
            "GO:0030254": ("ACCEPT", "Type-III secretion-system protein secretion captures the flagellar export apparatus context.", None),
            "GO:0030257": ("ACCEPT", "The type-III secretion-system complex term captures the flagellar export-apparatus complex context.", None),
            "GO:0044780": ("ACCEPT", "Bacterial-type flagellum assembly is the pathway-level role of FliI-powered export.", None),
            "GO:0046933": ("REMOVE", "FliI is not a rotary ATP synthase; this TreeGrafter inference is an ATP-synthase-family overcall.", None),
            "GO:0071973": ("KEEP_AS_NON_CORE", "Flagellum-dependent motility is downstream of successful assembly, but FliI's core role is export/assembly.", None),
        },
    },
    "fliH": {
        "description": (
            "fliH encodes a FliH-family cytosolic regulator/accessory component of the flagellar export ATPase apparatus. "
            "It is linked to flagellar regrowth and assembly and is best treated as part of the FliI/FliH/FliJ export-energy module."
        ),
        "core": {
            "description": "Cytosolic FliH-family accessory regulator of the FliI-powered flagellar export apparatus.",
            "directly_involved_in": [term("GO:0044781", "bacterial-type flagellum organization")],
            "locations": [term("GO:0005829", "cytosol")],
        },
        "extra_core_support": [
            ("uniprot", "-!- FUNCTION: Needed for flagellar regrowth and assembly."),
            ("uniprot", "DR   GO; GO:0044781; P:bacterial-type flagellum organization; IEA:UniProtKB-KW."),
            ("uniprot", "DR   Pfam; PF02108; FliH; 1."),
        ],
        "decisions": {
            "GO:0005829": ("ACCEPT", "Cytosol localization matches FliH as a cytosolic flagellar export accessory component.", None),
        },
    },
    "fliT": {
        "description": (
            "fliT encodes a small cytosolic FliT-family flagellar protein. "
            "In this first pass it is treated conservatively as a cytosolic flagellar organization/assembly-support factor rather than assigned a more specific unverified regulatory mechanism."
        ),
        "core": {
            "description": "Cytosolic FliT-family flagellar organization factor.",
            "directly_involved_in": [term("GO:0044781", "bacterial-type flagellum organization")],
            "locations": [term("GO:0005829", "cytosol")],
        },
        "extra_core_support": [
            ("uniprot", "DR   GO; GO:0044781; P:bacterial-type flagellum organization; IEA:UniProtKB-KW."),
            ("uniprot", "DR   Pfam; PF05400; FliT; 1."),
        ],
        "decisions": {
            "GO:0005829": ("ACCEPT", "Cytosol localization matches UniProt subcellular-location evidence for FliT.", None),
        },
    },
    "fliS": {
        "description": (
            "fliS encodes the FliS flagellar secretion chaperone. "
            "It is a cytosolic FliS-family factor that supports flagellin/filament assembly through the flagellar export pathway."
        ),
        "core": {
            "description": "Cytosolic FliS-family flagellar secretion chaperone supporting flagellum assembly.",
            "directly_involved_in": [term("GO:0044780", "bacterial-type flagellum assembly"), term("GO:0044781", "bacterial-type flagellum organization")],
            "locations": [term("GO:0005829", "cytosol")],
        },
        "extra_core_support": [
            ("uniprot", "RecName: Full=Flagellar secretion chaperone FliS"),
            ("uniprot", "DR   Pfam; PF02561; FliS; 1."),
        ],
        "decisions": {
            "GO:0005829": ("ACCEPT", "Cytosol localization matches the soluble flagellar chaperone role of FliS.", None),
            "GO:0044780": ("ACCEPT", "Flagellum assembly is the pathway-defining role for the FliS secretion chaperone.", None),
            "GO:0044781": ("ACCEPT", "Flagellum organization is consistent with FliS-supported assembly/export.", None),
            "GO:0071973": ("KEEP_AS_NON_CORE", "Flagellum-dependent motility is downstream of flagellar assembly, while FliS's core role is chaperone-supported assembly.", None),
        },
    },
    "flgA": {
        "description": (
            "flgA encodes a periplasmic FlgA-family factor required for flagellar P-ring formation. "
            "It supports basal-body/P-ring assembly in the periplasm rather than acting as a structural filament or motor component."
        ),
        "core": {
            "description": "Periplasmic FlgA-family factor for flagellar P-ring formation during basal-body assembly.",
            "directly_involved_in": [term("GO:0044780", "bacterial-type flagellum assembly")],
            "locations": [term("GO:0042597", "periplasmic space")],
        },
        "extra_core_support": [
            ("uniprot", "-!- FUNCTION: Involved in the assembly process of the P-ring formation."),
            ("uniprot", "DR   Pfam; PF13144; ChapFlgA; 1."),
        ],
        "decisions": {
            "GO:0042597": ("ACCEPT", "Periplasmic localization matches FlgA's P-ring assembly role.", None),
            "GO:0044780": ("ACCEPT", "Bacterial-type flagellum assembly captures the FlgA P-ring formation role.", None),
        },
    },
    "PP_4396": {
        "aliases": ["flgN"],
        "description": (
            "PP_4396 encodes a FlgN-family flagellar biosynthesis protein, likely the KT2440 FlgN-like assembly chaperone. "
            "UniProt describes it as required for efficient initiation of filament assembly, so this first pass retains it as a flagellar assembly-support factor under the locus-tag review name."
        ),
        "core": {
            "description": "FlgN-family flagellar biosynthesis factor required for efficient initiation of filament assembly.",
            "directly_involved_in": [term("GO:0044780", "bacterial-type flagellum assembly")],
        },
        "extra_core_support": [
            ("uniprot", "-!- FUNCTION: Required for the efficient initiation of filament assembly."),
            ("uniprot", "DR   Pfam; PF05130; FlgN; 1."),
        ],
        "decisions": {
            "GO:0044780": ("ACCEPT", "Bacterial-type flagellum assembly captures the FlgN-family role in initiating filament assembly.", None),
        },
    },
}


def support_from_spec(gene: str, support_specs: list[tuple[str, str]]) -> list[dict[str, str]]:
    out = []
    for source, needle in support_specs:
        if source == "uniprot":
            out.append(uniprot_line(gene, needle))
        elif source == "asta":
            out.append(asta_line(gene, needle))
        else:
            raise ValueError(f"Unknown support source {source}")
    return out


def core_support(gene: str, core: dict, extra_support_specs: list[tuple[str, str]]) -> list[dict[str, str]]:
    support_items: list[dict[str, str]] = []
    for slot in ("molecular_function", "contributes_to_molecular_function", "in_complex"):
        value = core.get(slot)
        if isinstance(value, dict) and value.get("id"):
            try:
                support_items.append(goa_line(gene, value["id"]))
            except ValueError:
                try:
                    support_items.append(uniprot_line(gene, f"DR   GO; {value['id']};"))
                except ValueError:
                    pass
    for slot in ("directly_involved_in", "locations"):
        for value in core.get(slot, []) or []:
            try:
                support_items.append(goa_line(gene, value["id"]))
            except ValueError:
                try:
                    support_items.append(uniprot_line(gene, f"DR   GO; {value['id']};"))
                except ValueError:
                    pass
    support_items.extend(support_from_spec(gene, extra_support_specs))
    support_items.append(asta_line(gene))
    return uniq_support(support_items)


def curate_gene(gene: str, spec: dict) -> None:
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    data["status"] = "DRAFT"
    data["gene_symbol"] = gene
    if spec.get("aliases"):
        data["aliases"] = spec["aliases"]
    data["description"] = spec["description"]
    data["references"] = normalize_references(data.get("references", []), gene)

    decisions = spec.get("decisions", {})
    for annotation in data.get("existing_annotations", []) or []:
        term_id = annotation["term"]["id"]
        label = annotation["term"]["label"]
        action, reason, replacements = decisions.get(
            term_id,
            (
                "KEEP_AS_NON_CORE",
                "This annotation is compatible with the flagellar export/assembly context but is not the most specific first-pass interpretation.",
                None,
            ),
        )
        annotation["review"] = make_review(
            gene,
            term_id,
            label,
            action,
            reason,
            extra_support=support_from_spec(gene, spec.get("extra_core_support", [])[:1]),
            replacements=replacements,
        )

    core = dict(spec["core"])
    core["supported_by"] = core_support(gene, core, spec.get("extra_core_support", []))
    data["core_functions"] = [core]
    data["proposed_new_terms"] = []
    data["suggested_questions"] = [
        {"question": "Is the KT2440-specific requirement for this export/assembly factor condition-dependent across swimming, surface-associated motility, and biofilm growth?"},
        {"question": "Do direct interaction or localization data distinguish this protein's role within the flagellar export gate, ATPase/regulator module, or late assembly-chaperone module?"},
    ]
    data["suggested_experiments"] = [
        {"description": "Construct a clean deletion or depletion allele and assay flagellation, swimming motility, and assembly-stage defects by microscopy."},
        {"description": "Tag the protein at the native locus and test co-localization or interaction with export-gate and basal-body markers under motility-inducing conditions."},
    ]
    path.write_text(
        yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=False, width=100),
        encoding="utf-8",
    )
    print(f"Curated {path.relative_to(ROOT)}")


def main() -> None:
    for gene, spec in GENES.items():
        curate_gene(gene, spec)


if __name__ == "__main__":
    main()
