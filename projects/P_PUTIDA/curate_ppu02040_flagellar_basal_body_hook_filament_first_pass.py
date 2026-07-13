#!/usr/bin/env python3
"""First-pass curation for ppu02040 flagellar basal-body/hook/filament genes."""

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
    "GO_REF:0000044": (
        "Gene Ontology annotation based on UniProtKB/Swiss-Prot Subcellular Location vocabulary mapping, "
        "accompanied by conservative changes to GO terms applied by UniProt"
    ),
    "GO_REF:0000104": (
        "Electronic Gene Ontology annotations created by transferring manual GO annotations between "
        "related proteins based on shared sequence features"
    ),
    "GO_REF:0000118": "TreeGrafter-generated GO annotations",
    "GO_REF:0000120": "Combined Automated Annotation using Multiple IEA Methods",
}


def term(term_id: str, label: str) -> dict[str, str]:
    return {"id": term_id, "label": label}


def ref_id(gene: str, suffix: str) -> str:
    return f"file:{SPECIES}/{gene}/{gene}-{suffix}"


def support(reference_id: str, text: str) -> dict[str, str]:
    return {"reference_id": reference_id, "supporting_text": text}


def find_line(path: Path, needle: str) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if needle in line:
            return line
    raise ValueError(f"{needle!r} not found in {path}")


def goa_line(gene: str, term_id: str) -> dict[str, str]:
    return support(ref_id(gene, "goa.tsv"), find_line(GENE_ROOT / gene / f"{gene}-goa.tsv", term_id))


def uniprot_line(gene: str, needle: str) -> dict[str, str]:
    return support(
        ref_id(gene, "uniprot.txt"),
        find_line(GENE_ROOT / gene / f"{gene}-uniprot.txt", needle),
    )


def asta_line(gene: str, needle: str = "- **Protein Description:**") -> dict[str, str]:
    return support(
        ref_id(gene, "deep-research-asta.md"),
        find_line(GENE_ROOT / gene / f"{gene}-deep-research-asta.md", needle),
    )


def uniq(items: list[dict[str, str]]) -> list[dict[str, str]]:
    seen: set[tuple[str, str]] = set()
    out: list[dict[str, str]] = []
    for item in items:
        key = (item["reference_id"], item["supporting_text"])
        if key not in seen:
            out.append(item)
            seen.add(key)
    return out


def support_from_spec(gene: str, specs: list[tuple[str, str]]) -> list[dict[str, str]]:
    out = []
    for source, needle in specs:
        if source == "uniprot":
            out.append(uniprot_line(gene, needle))
        elif source == "asta":
            out.append(asta_line(gene, needle))
        else:
            raise ValueError(f"Unknown support source {source}")
    return out


def review(
    gene: str,
    term_id: str,
    label: str,
    action: str,
    reason: str,
    extra_support: list[dict[str, str]] | None = None,
    replacements: list[dict[str, str]] | None = None,
) -> dict:
    data = {
        "summary": f"{label} was reviewed for {gene} in the ppu02040 basal-body/hook/filament first pass.",
        "action": action,
        "reason": reason,
        "supported_by": uniq([goa_line(gene, term_id), asta_line(gene)] + (extra_support or [])),
    }
    if replacements:
        data["proposed_replacement_terms"] = replacements
    return data


def file_ref(gene: str, suffix: str, title: str, statement: str) -> dict:
    path = GENE_ROOT / gene / f"{gene}-{suffix}"
    if not path.exists():
        return {}
    return {"id": ref_id(gene, suffix), "title": title, "findings": [{"statement": statement}]}


def normalize_references(existing: list[dict], gene: str) -> list[dict]:
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
        file_ref(gene, "uniprot.txt", f"UniProtKB entry for {gene}", "UniProt protein names, family assignments, domains, subcellular-location lines, and GO cross-references used for first-pass curation."),
        file_ref(gene, "goa.tsv", f"QuickGO GOA annotations for {gene}", "Fetched GOA rows reviewed in this first-pass curation file."),
        file_ref(gene, "deep-research-asta.md", f"Asta retrieval report for {gene}", "Asta retrieval was used as fast gene-level metadata support; it was not used to introduce unsupported hypotheses."),
    ]:
        rid = ref.get("id")
        if rid and rid not in seen:
            refs.append(ref)
            seen.add(rid)
    return refs


SWARMING_REASON = (
    "Swarming is a specialized surface-associated behavior with regulators and physiology beyond the core structural role of this flagellar component; keep the broader flagellum-dependent motility context instead."
)
MOTOR_OVER_REASON = (
    "This protein is a structural basal-body/ring/rod component rather than a torque-generating motor or switch protein, so the cytoskeletal motor activity term is over-propagated for the first-pass core role."
)
BROAD_MOTILITY_REASON = (
    "The broader archaeal-or-bacterial flagellum-dependent motility term is true but less precise than bacterial-type flagellum-dependent cell motility for this KT2440 bacterial component."
)


GENES: dict[str, dict] = {
    "fliF": {
        "description": "fliF encodes the FliF MS/M-ring protein of the Pseudomonas putida KT2440 bacterial-type flagellum. It is a membrane-associated basal-body scaffold that forms the MS ring and supports flagellum-dependent motility by anchoring the export/motor architecture.",
        "core": {
            "description": "Membrane-associated FliF MS/M-ring scaffold of the flagellar basal body.",
            "directly_involved_in": [term("GO:0071973", "bacterial-type flagellum-dependent cell motility")],
            "locations": [term("GO:0009431", "bacterial-type flagellum basal body, MS ring"), term("GO:0005886", "plasma membrane")],
        },
        "extra": [("uniprot", "RecName: Full=Flagellar M-ring protein"), ("uniprot", "DR   Pfam; PF01514; YscJ_FliF; 1.")],
        "decisions": {
            "GO:0003774": ("MARK_AS_OVER_ANNOTATED", MOTOR_OVER_REASON, None),
            "GO:0005886": ("ACCEPT", "FliF is a membrane-associated basal-body MS-ring component.", None),
            "GO:0009425": ("KEEP_AS_NON_CORE", "Basal-body localization is correct but less precise than the MS-ring annotation.", None),
            "GO:0009431": ("ACCEPT", "The MS-ring term is the most specific cellular component for FliF.", None),
            "GO:0071973": ("ACCEPT", "FliF supports flagellum-dependent motility through basal-body/MS-ring assembly.", None),
        },
    },
    "fliE": {
        "description": "fliE encodes the FliE hook-basal body complex protein of the KT2440 bacterial-type flagellum. It is a small structural basal-body component that links the MS ring/rod region to the exported axial structure and supports flagellum-dependent motility.",
        "core": {
            "description": "FliE structural component of the hook-basal-body complex.",
            "molecular_function": term("GO:0005198", "structural molecule activity"),
            "directly_involved_in": [term("GO:0071973", "bacterial-type flagellum-dependent cell motility")],
            "locations": [term("GO:0009425", "bacterial-type flagellum basal body"), term("GO:0009288", "bacterial-type flagellum")],
        },
        "extra": [("uniprot", "RecName: Full=Flagellar hook-basal body complex protein FliE"), ("uniprot", "DR   Pfam; PF02049; FliE; 1.")],
        "decisions": {
            "GO:0003774": ("MARK_AS_OVER_ANNOTATED", MOTOR_OVER_REASON, None),
            "GO:0005198": ("ACCEPT", "Structural molecule activity is appropriate for FliE as a small hook-basal-body complex component.", None),
            "GO:0009288": ("ACCEPT", "FliE is part of the bacterial-type flagellum.", None),
            "GO:0009425": ("ACCEPT", "Basal-body localization matches FliE's hook-basal-body complex role.", None),
            "GO:0071973": ("ACCEPT", "FliE contributes to a flagellar structure required for flagellum-dependent motility.", None),
            "GO:0097588": ("KEEP_AS_NON_CORE", BROAD_MOTILITY_REASON, None),
        },
    },
    "fliD": {
        "description": "fliD encodes flagellar hook-associated protein 2, the FliD filament-cap protein. In KT2440 it is an exported flagellar cap component that supports filament elongation at the distal end of the bacterial-type flagellum.",
        "core": {
            "description": "FliD filament-cap protein that enables flagellar filament elongation.",
            "directly_involved_in": [term("GO:0071973", "bacterial-type flagellum-dependent cell motility")],
            "locations": [term("GO:0009421", "bacterial-type flagellum filament cap"), term("GO:0009288", "bacterial-type flagellum")],
        },
        "extra": [("uniprot", "AltName: Full=Flagellar cap protein"), ("uniprot", "DR   Pfam; PF02465; FliD_N; 1.")],
        "decisions": {
            "GO:0005576": ("KEEP_AS_NON_CORE", "Extracellular region is broadly true for an exported flagellar cap protein but less precise than the filament-cap location.", None),
            "GO:0007155": ("MARK_AS_OVER_ANNOTATED", "Cell adhesion is an over-broad InterPro transfer for FliD in this first pass; the supported role is filament cap/assembly.", None),
            "GO:0009288": ("ACCEPT", "FliD is a component of the bacterial-type flagellum.", None),
            "GO:0009421": ("ACCEPT", "The filament-cap term is the best cellular-component placement for FliD.", None),
            "GO:0009424": ("MODIFY", "FliD is hook-associated by name but the specific structural location is the filament cap rather than the hook proper.", [term("GO:0009421", "bacterial-type flagellum filament cap")]),
            "GO:0071973": ("ACCEPT", "A functional FliD cap supports flagellar filament assembly and flagellum-dependent motility.", None),
        },
    },
    "flgJ": {
        "description": "flgJ encodes a periplasmic flagellum-specific peptidoglycan hydrolase/muramidase. The protein combines FlgJ rod-associated context with glycosyl-hydrolase family 73 features, supporting local peptidoglycan remodeling during basal-body/rod assembly.",
        "core": {
            "description": "Periplasmic FlgJ muramidase that clears peptidoglycan for flagellar rod assembly.",
            "molecular_function": term("GO:0016798", "hydrolase activity, acting on glycosyl bonds"),
            "directly_involved_in": [term("GO:0044780", "bacterial-type flagellum assembly")],
            "locations": [term("GO:0042597", "periplasmic space")],
        },
        "extra": [("uniprot", "RecName: Full=Peptidoglycan hydrolase FlgJ"), ("uniprot", "DR   Pfam; PF01832; Glucosaminidase; 1.")],
        "decisions": {
            "GO:0004040": ("MODIFY", "FlgJ is described as a muramidase/glycosyl hydrolase rather than a specific amidase; the existing glycosyl-bond hydrolase term better captures the chemistry.", [term("GO:0016798", "hydrolase activity, acting on glycosyl bonds")]),
            "GO:0016798": ("ACCEPT", "Glycosyl-bond hydrolase activity matches the FlgJ muramidase/glycosyl hydrolase family evidence.", None),
            "GO:0042597": ("ACCEPT", "Periplasmic localization matches the location where peptidoglycan is remodeled for rod passage.", None),
            "GO:0044780": ("ACCEPT", "Flagellum assembly is the pathway role for FlgJ-mediated local peptidoglycan remodeling.", None),
            "GO:0071973": ("KEEP_AS_NON_CORE", "Motility is downstream of successful flagellar assembly; FlgJ's core role is assembly and peptidoglycan remodeling.", None),
        },
    },
    "flgI": {
        "description": "flgI encodes the periplasmic flagellar P-ring protein of the KT2440 basal body. As a precursor with a signal peptide, it assembles around the rod to form the P ring in the periplasm and supports flagellum-dependent motility.",
        "core": {
            "description": "Periplasmic P-ring structural protein of the flagellar basal body.",
            "molecular_function": term("GO:0005198", "structural molecule activity"),
            "directly_involved_in": [term("GO:0071973", "bacterial-type flagellum-dependent cell motility")],
            "locations": [term("GO:0009428", "bacterial-type flagellum basal body, distal rod, P ring"), term("GO:0042597", "periplasmic space")],
        },
        "extra": [("uniprot", "RecName: Full=Flagellar P-ring protein"), ("uniprot", "FT   SIGNAL")],
        "decisions": {
            "GO:0005198": ("ACCEPT", "Structural molecule activity is appropriate for the FlgI P-ring structural protein.", None),
            "GO:0009425": ("KEEP_AS_NON_CORE", "Basal-body localization is correct but less precise than the P-ring term.", None),
            "GO:0009428": ("ACCEPT", "The P-ring term is the specific cellular-component placement for FlgI.", None),
            "GO:0030288": ("ACCEPT", "Outer membrane-bounded periplasmic space is compatible with a periplasmic P-ring precursor.", None),
            "GO:0042597": ("ACCEPT", "Periplasmic space matches FlgI signal-peptide and location evidence.", None),
            "GO:0071973": ("ACCEPT", "The P ring is required for a flagellar basal body that supports motility.", None),
            "GO:0097588": ("KEEP_AS_NON_CORE", BROAD_MOTILITY_REASON, None),
        },
    },
    "flgH": {
        "description": "flgH encodes the flagellar L-ring protein of the KT2440 basal body. It is an outer-membrane-associated precursor that assembles around the distal rod to form the L ring and supports flagellum-dependent motility.",
        "core": {
            "description": "Outer-membrane L-ring structural protein of the flagellar basal body.",
            "directly_involved_in": [term("GO:0071973", "bacterial-type flagellum-dependent cell motility")],
            "locations": [term("GO:0009427", "bacterial-type flagellum basal body, distal rod, L ring"), term("GO:0009279", "cell outer membrane")],
        },
        "extra": [("uniprot", "RecName: Full=Flagellar L-ring protein"), ("uniprot", "FT   SIGNAL")],
        "decisions": {
            "GO:0003774": ("MARK_AS_OVER_ANNOTATED", MOTOR_OVER_REASON, None),
            "GO:0009279": ("ACCEPT", "Outer membrane localization matches the FlgH L-ring protein.", None),
            "GO:0009425": ("KEEP_AS_NON_CORE", "Basal-body localization is correct but less precise than the L-ring term.", None),
            "GO:0009427": ("ACCEPT", "The L-ring term is the specific cellular-component placement for FlgH.", None),
            "GO:0071973": ("ACCEPT", "The L ring is required for a flagellar basal body that supports motility.", None),
            "GO:0097588": ("KEEP_AS_NON_CORE", BROAD_MOTILITY_REASON, None),
        },
    },
    "flgG": {
        "description": "flgG encodes the distal rod protein of the KT2440 flagellar basal body. It is a flagellar basal-body rod-family structural protein that forms part of the distal rod and supports flagellum-dependent motility.",
        "core": {
            "description": "FlgG distal rod structural protein of the flagellar basal body.",
            "directly_involved_in": [term("GO:0071973", "bacterial-type flagellum-dependent cell motility")],
            "locations": [term("GO:0009426", "bacterial-type flagellum basal body, distal rod"), term("GO:0009288", "bacterial-type flagellum")],
        },
        "extra": [("uniprot", "AltName: Full=Distal rod protein"), ("uniprot", "DR   Pfam; PF00460; Flg_bb_rod; 1.")],
        "decisions": {
            "GO:0009288": ("ACCEPT", "FlgG is a component of the bacterial-type flagellum.", None),
            "GO:0009425": ("KEEP_AS_NON_CORE", "Basal-body localization is correct but less precise than the distal-rod term.", None),
            "GO:0009426": ("ACCEPT", "Distal rod is the specific structural location for FlgG.", None),
            "GO:0071973": ("ACCEPT", "A functional distal rod supports flagellum-dependent motility.", None),
            "GO:0071978": ("MARK_AS_OVER_ANNOTATED", SWARMING_REASON, None),
        },
    },
    "flgF": {
        "description": "flgF encodes a flagellar basal-body rod protein of the KT2440 bacterial-type flagellum. It is a rod-family structural protein that supports basal-body rod assembly and flagellum-dependent motility.",
        "core": {
            "description": "FlgF rod structural protein of the flagellar basal body.",
            "directly_involved_in": [term("GO:0071973", "bacterial-type flagellum-dependent cell motility")],
            "locations": [term("GO:0030694", "bacterial-type flagellum basal body, rod"), term("GO:0009288", "bacterial-type flagellum")],
        },
        "extra": [("uniprot", "RecName: Full=Flagellar basal-body rod protein FlgF"), ("uniprot", "DR   Pfam; PF00460; Flg_bb_rod; 1.")],
        "decisions": {
            "GO:0009288": ("ACCEPT", "FlgF is a component of the bacterial-type flagellum.", None),
            "GO:0009425": ("KEEP_AS_NON_CORE", "Basal-body localization is correct but less precise than the rod term.", None),
            "GO:0030694": ("ACCEPT", "The basal-body rod term captures the specific structural location for FlgF.", None),
            "GO:0071973": ("ACCEPT", "A functional rod supports flagellum-dependent motility.", None),
            "GO:0071978": ("MARK_AS_OVER_ANNOTATED", SWARMING_REASON, None),
        },
    },
    "flgD": {
        "description": "flgD encodes a FlgD-family basal-body rod modification and hook-formation factor. In KT2440 it is best treated as an assembly factor for bacterial-type flagellum organization rather than as a mature rod, hook, or filament structural subunit.",
        "core": {
            "description": "FlgD-family hook-formation/rod-modification factor for flagellar organization.",
            "directly_involved_in": [term("GO:0044781", "bacterial-type flagellum organization")],
        },
        "extra": [("uniprot", "RecName: Full=Basal-body rod modification protein FlgD"), ("uniprot", "Required for flagellar hook formation.")],
        "decisions": {
            "GO:0044781": ("ACCEPT", "Flagellum organization is the conservative process term for FlgD hook-formation/rod-modification context.", None),
        },
    },
    "flgC": {
        "description": "flgC encodes a flagellar basal-body rod protein of the KT2440 bacterial-type flagellum. It is a rod-family structural protein that forms part of the basal-body rod and supports flagellum-dependent motility.",
        "core": {
            "description": "FlgC rod structural protein of the flagellar basal body.",
            "directly_involved_in": [term("GO:0071973", "bacterial-type flagellum-dependent cell motility")],
            "locations": [term("GO:0030694", "bacterial-type flagellum basal body, rod"), term("GO:0009288", "bacterial-type flagellum")],
        },
        "extra": [("uniprot", "RecName: Full=Flagellar basal-body rod protein FlgC"), ("uniprot", "DR   Pfam; PF00460; Flg_bb_rod; 1.")],
        "decisions": {
            "GO:0009288": ("ACCEPT", "FlgC is a component of the bacterial-type flagellum.", None),
            "GO:0009425": ("KEEP_AS_NON_CORE", "Basal-body localization is correct but less precise than the rod term.", None),
            "GO:0030694": ("ACCEPT", "The basal-body rod term captures the specific structural location for FlgC.", None),
            "GO:0071973": ("ACCEPT", "A functional rod supports flagellum-dependent motility.", None),
            "GO:0071978": ("MARK_AS_OVER_ANNOTATED", SWARMING_REASON, None),
        },
    },
    "flgB": {
        "description": "flgB encodes a flagellar basal-body rod protein of the KT2440 bacterial-type flagellum. It is a rod-family structural component of the basal body and supports flagellum-dependent motility.",
        "core": {
            "description": "FlgB rod structural protein of the flagellar basal body.",
            "directly_involved_in": [term("GO:0071973", "bacterial-type flagellum-dependent cell motility")],
            "locations": [term("GO:0030694", "bacterial-type flagellum basal body, rod"), term("GO:0009288", "bacterial-type flagellum")],
        },
        "extra": [("uniprot", "RecName: Full=Flagellar basal body rod protein FlgB"), ("uniprot", "DR   Pfam; PF00460; Flg_bb_rod; 1.")],
        "decisions": {
            "GO:0009288": ("ACCEPT", "FlgB is a component of the bacterial-type flagellum.", None),
            "GO:0009425": ("KEEP_AS_NON_CORE", "Basal-body localization is correct but less precise than the rod term.", None),
            "GO:0030694": ("ACCEPT", "The basal-body rod term captures the specific structural location for FlgB.", None),
            "GO:0071973": ("ACCEPT", "A functional rod supports flagellum-dependent motility.", None),
            "GO:0071978": ("MARK_AS_OVER_ANNOTATED", SWARMING_REASON, None),
        },
    },
}


def core_support(gene: str, core: dict, extra_specs: list[tuple[str, str]]) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    for slot in ("molecular_function", "contributes_to_molecular_function", "in_complex"):
        value = core.get(slot)
        if isinstance(value, dict) and value.get("id"):
            try:
                items.append(goa_line(gene, value["id"]))
            except ValueError:
                pass
    for slot in ("directly_involved_in", "locations"):
        for value in core.get(slot, []) or []:
            try:
                items.append(goa_line(gene, value["id"]))
            except ValueError:
                try:
                    items.append(uniprot_line(gene, f"DR   GO; {value['id']};"))
                except ValueError:
                    pass
    items.extend(support_from_spec(gene, extra_specs))
    items.append(asta_line(gene))
    return uniq(items)


def curate_gene(gene: str, spec: dict) -> None:
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    data["status"] = "DRAFT"
    data["gene_symbol"] = gene
    data["description"] = spec["description"]
    data["references"] = normalize_references(data.get("references", []), gene)

    for annotation in data.get("existing_annotations", []) or []:
        tid = annotation["term"]["id"]
        label = annotation["term"]["label"]
        action, reason, replacements = spec["decisions"].get(
            tid,
            ("KEEP_AS_NON_CORE", "This annotation is compatible with flagellar structural context but is not the most specific first-pass interpretation.", None),
        )
        annotation["review"] = review(
            gene,
            tid,
            label,
            action,
            reason,
            extra_support=support_from_spec(gene, spec.get("extra", [])[:1]),
            replacements=replacements,
        )

    core = dict(spec["core"])
    core["supported_by"] = core_support(gene, core, spec.get("extra", []))
    data["core_functions"] = [core]
    data["proposed_new_terms"] = []
    data["suggested_questions"] = [
        {"question": "Does this structural or assembly factor have a condition-specific requirement in KT2440 swimming, surface motility, or biofilm-associated flagellar remodeling?"},
        {"question": "Can native-locus tagging resolve the precise assembly stage and substructure localization for this flagellar component in KT2440?"},
    ]
    data["suggested_experiments"] = [
        {"description": "Construct a clean deletion or depletion allele and compare swimming motility, flagellation, and basal-body/hook/filament morphology by microscopy."},
        {"description": "Complement the mutant and use native-locus epitope or fluorescent tagging to test assembly-stage localization under motility-inducing conditions."},
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
