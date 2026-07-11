#!/usr/bin/env python3
"""First-pass curate the PSEPK chaperone/foldase protein-turnover split."""

from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes" / "PSEPK"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


TERM = {
    "GO:0001671": {"id": "GO:0001671", "label": "ATPase activator activity"},
    "GO:0003676": {"id": "GO:0003676", "label": "nucleic acid binding"},
    "GO:0003681": {"id": "GO:0003681", "label": "bent DNA binding"},
    "GO:0003755": {"id": "GO:0003755", "label": "peptidyl-prolyl cis-trans isomerase activity"},
    "GO:0005524": {"id": "GO:0005524", "label": "ATP binding"},
    "GO:0005737": {"id": "GO:0005737", "label": "cytoplasm"},
    "GO:0005829": {"id": "GO:0005829", "label": "cytosol"},
    "GO:0006457": {"id": "GO:0006457", "label": "protein folding"},
    "GO:0009295": {"id": "GO:0009295", "label": "nucleoid"},
    "GO:0016226": {"id": "GO:0016226", "label": "iron-sulfur cluster assembly"},
    "GO:0016853": {"id": "GO:0016853", "label": "isomerase activity"},
    "GO:0016887": {"id": "GO:0016887", "label": "ATP hydrolysis activity"},
    "GO:0034605": {"id": "GO:0034605", "label": "cellular response to heat"},
    "GO:0042026": {"id": "GO:0042026", "label": "protein refolding"},
    "GO:0044183": {"id": "GO:0044183", "label": "protein folding chaperone"},
    "GO:0044571": {"id": "GO:0044571", "label": "[2Fe-2S] cluster assembly"},
    "GO:0051082": {"id": "GO:0051082", "label": "unfolded protein binding"},
    "GO:0051087": {"id": "GO:0051087", "label": "protein-folding chaperone binding"},
    "GO:0051259": {"id": "GO:0051259", "label": "protein complex oligomerization"},
    "GO:1990230": {"id": "GO:1990230", "label": "iron-sulfur cluster transfer complex"},
}


DESCRIPTIONS = {
    "hslO": (
        "HslO/Hsp33 is a cytoplasmic redox-regulated molecular chaperone of Pseudomonas putida KT2440. "
        "It protects thermally unfolding and oxidatively damaged proteins from irreversible aggregation and "
        "therefore functions as a stress-responsive holdase/refolding factor in bacterial proteostasis."
    ),
    "slyD": (
        "SlyD is a cytoplasmic FKBP-type peptidyl-prolyl cis-trans isomerase. It catalyzes cis-trans "
        "isomerization of peptidyl-prolyl bonds and is also annotated as a chaperone-like factor linked to "
        "protein refolding and hydrogenase metallocenter assembly; the first-pass core call is the conserved "
        "PPIase/foldase activity."
    ),
    "hscB": (
        "HscB is a J-domain co-chaperone for the HscA system. It interacts with HscA, stimulates HscA ATPase "
        "activity, and helps target iron-sulfur-cluster-containing proteins for maturation, tying its "
        "protein-folding/chaperone role to Fe-S cluster assembly."
    ),
    "hscA": (
        "HscA is an Hsp70-family ATP-dependent chaperone specialized for maturation of iron-sulfur "
        "cluster-containing proteins. Its conserved nucleotide-binding and substrate-binding domains support "
        "ATP binding, ATP hydrolysis, and client-protein binding during Fe-S cluster assembly."
    ),
    "PP_1548": (
        "PP_1548 is a small DjlA N-terminal/TerB-like domain-containing protein. Current first-pass metadata "
        "supports a possible chaperone-associated/domain-family context, but no GOA rows or specific molecular "
        "function are available for a confident core annotation."
    ),
    "cspA-II": (
        "cspA-II encodes a small cytosolic cold-shock-domain protein with a CspA-like OB-fold. Domain and GOA "
        "evidence support conservative nucleic-acid binding, but the specific RNA or DNA targets are unresolved."
    ),
    "PP_3316": (
        "PP_3316 is a cytoplasmic ClpA/ClpB-family AAA+ chaperone-associated ATPase candidate. The conserved "
        "AAA+ ATPase domains support ATP binding and ATP hydrolysis, while the specific partner complex and "
        "client substrates remain unresolved."
    ),
    "cbpM": (
        "CbpM is a CbpA-interacting chaperone modulatory protein. It inhibits both the DnaJ-like co-chaperone "
        "activity and DNA-binding activity of CbpA and, together with CbpA, modulates the DnaK chaperone system."
    ),
    "cbpA": (
        "CbpA is a cytoplasmic and nucleoid-associated curved-DNA-binding protein with DnaJ-like chaperone "
        "features. It preferentially recognizes curved DNA and can bind protein substrates for DnaK-mediated "
        "recognition, with its activity inhibited by CbpM."
    ),
}


def read_lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8").splitlines()


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
    items = [support(file_id(gene, "uniprot.txt"), first_line(path, "DE   "))]
    if term_id:
        add_unique(items, support(file_id(gene, "uniprot.txt"), optional_first_line(path, f"DR   GO; {term_id};") or ""))
        if not items[-1]["supporting_text"]:
            items.pop()
    for needles in (
        ("CC   -!- FUNCTION:",),
        ("CC   -!- CATALYTIC ACTIVITY:",),
        ("CC   -!- SUBCELLULAR LOCATION:",),
        ("CC   -!- SUBUNIT:",),
        ("DR   PANTHER;",),
        ("DR   Pfam;",),
        ("FT   DOMAIN",),
    ):
        line = optional_first_line(path, *needles)
        if line:
            add_unique(items, support(file_id(gene, "uniprot.txt"), line))
    for line in [line for line in read_lines(path) if line.startswith("DR   InterPro;")][:4]:
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


def set_review(data: dict, term_id: str, review: dict) -> None:
    for ann in data.get("existing_annotations") or []:
        if ann.get("term", {}).get("id") == term_id:
            ann["review"] = review
            return
    raise ValueError(f"{data['gene_symbol']} has no existing annotation {term_id}")


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


def accept(gene: str, term_id: str, summary: str, reason: str) -> dict:
    return {
        "summary": summary,
        "action": "ACCEPT",
        "reason": reason,
        "supported_by": standard_support(gene, term_id),
    }


def keep_non_core(gene: str, term_id: str, summary: str, reason: str) -> dict:
    return {
        "summary": summary,
        "action": "KEEP_AS_NON_CORE",
        "reason": reason,
        "supported_by": standard_support(gene, term_id),
    }


def over_annotated(gene: str, term_id: str, summary: str, reason: str) -> dict:
    return {
        "summary": summary,
        "action": "MARK_AS_OVER_ANNOTATED",
        "reason": reason,
        "supported_by": standard_support(gene, term_id),
    }


def save_gene(gene: str, data: dict) -> None:
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    data["status"] = "DRAFT"
    data["description"] = DESCRIPTIONS[gene]
    if "proposed_new_terms" not in data:
        data["proposed_new_terms"] = []
    if "suggested_questions" not in data:
        data["suggested_questions"] = []
    if "suggested_experiments" not in data:
        data["suggested_experiments"] = []
    path.write_text(
        yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=False, width=120),
        encoding="utf-8",
    )


def curate_hslO() -> None:
    gene = "hslO"
    data = yaml.safe_load((GENE_ROOT / gene / f"{gene}-ai-review.yaml").read_text())
    ensure_references(data, gene, data["id"])
    set_review(data, "GO:0005737", accept(gene, "GO:0005737", "Hsp33/HslO is a cytoplasmic bacterial chaperone.", "The UniProt subcellular-location rule and GOA row place this soluble stress chaperone in the cytoplasm."))
    set_review(data, "GO:0006457", accept(gene, "GO:0006457", "HslO protects non-native proteins from aggregation and participates in protein folding/refolding under stress.", "Protein folding is a correct process annotation for this redox-regulated Hsp33-family chaperone."))
    set_review(data, "GO:0042026", accept(gene, "GO:0042026", "HslO participates in refolding or recovery of thermally and oxidatively damaged proteins.", "Protein refolding is appropriate for a stress-activated Hsp33-family holdase/refolding chaperone."))
    set_review(data, "GO:0044183", accept(gene, "GO:0044183", "HslO is a redox-regulated protein folding chaperone.", "This captures the direct molecular chaperone role supported by Hsp33 family membership."))
    ensure_new_annotation(
        data,
        gene,
        "GO:0051082",
        "enables",
        "UniProt also maps HslO/Hsp33 to unfolded protein binding, which is the direct holdase/client-binding activity of this chaperone.",
        "Unfolded protein binding is the most informative molecular function for the Hsp33 holdase activity and complements the existing protein folding/refolding process annotations.",
    )
    data["core_functions"] = [
        {
            "description": "Redox-regulated Hsp33-family holdase chaperone that binds non-native or oxidatively damaged proteins and protects them from irreversible aggregation during stress recovery.",
            "molecular_function": TERM["GO:0051082"],
            "directly_involved_in": [TERM["GO:0042026"], TERM["GO:0006457"]],
            "locations": [TERM["GO:0005737"]],
            "supported_by": standard_support(gene, "GO:0051082"),
        }
    ]
    save_gene(gene, data)


def curate_slyD() -> None:
    gene = "slyD"
    data = yaml.safe_load((GENE_ROOT / gene / f"{gene}-ai-review.yaml").read_text())
    ensure_references(data, gene, data["id"])
    set_review(data, "GO:0003755", accept(gene, "GO:0003755", "SlyD is an FKBP-type peptidyl-prolyl cis-trans isomerase with EC 5.2.1.8.", "The PPIase catalytic activity is the specific, direct enzyme function supported by UniProt, Rhea, EC, and FKBP-family domain evidence."))
    set_review(data, "GO:0005737", accept(gene, "GO:0005737", "SlyD is annotated as cytoplasmic.", "The cytoplasm localization is consistent with UniProt subcellular-location mapping for this soluble FKBP-type foldase."))
    set_review(data, "GO:0016853", over_annotated(gene, "GO:0016853", "Generic isomerase activity is true but less informative than the specific peptidyl-prolyl cis-trans isomerase term.", "The specific PPIase term GO:0003755 is present and should be used as the core molecular function rather than the broad parent isomerase term."))
    set_review(data, "GO:0042026", accept(gene, "GO:0042026", "SlyD has chaperone/foldase context and is associated with protein refolding.", "Protein refolding is consistent with the FKBP-type foldase/chaperone-family context; the core catalytic term remains PPIase activity."))
    data["core_functions"] = [
        {
            "description": "FKBP-type peptidyl-prolyl cis-trans isomerase that catalyzes cis-trans isomerization of peptidyl-prolyl bonds in the cytoplasm.",
            "molecular_function": TERM["GO:0003755"],
            "directly_involved_in": [TERM["GO:0042026"]],
            "locations": [TERM["GO:0005737"]],
            "supported_by": standard_support(gene, "GO:0003755"),
        }
    ]
    save_gene(gene, data)


def curate_hscB() -> None:
    gene = "hscB"
    data = yaml.safe_load((GENE_ROOT / gene / f"{gene}-ai-review.yaml").read_text())
    ensure_references(data, gene, data["id"])
    set_review(data, "GO:0001671", accept(gene, "GO:0001671", "HscB stimulates the ATPase activity of HscA.", "ATPase activator activity is the direct J-domain co-chaperone function of HscB."))
    set_review(data, "GO:0006457", accept(gene, "GO:0006457", "HscB participates in chaperone-mediated maturation/folding of Fe-S cluster-containing proteins.", "Protein folding is appropriate as process context for the HscA/HscB chaperone system."))
    set_review(data, "GO:0044571", accept(gene, "GO:0044571", "HscB is involved in maturation of [2Fe-2S]/Fe-S cluster-containing proteins.", "The HscB family is specifically linked to iron-sulfur protein maturation and [2Fe-2S] cluster assembly."))
    set_review(data, "GO:0051087", accept(gene, "GO:0051087", "HscB binds the HscA protein-folding chaperone.", "HscB directly interacts with HscA, and this chaperone binding is central to its ATPase-activating co-chaperone role."))
    set_review(data, "GO:0051259", keep_non_core(gene, "GO:0051259", "Protein complex oligomerization is plausible from HscB-family domain architecture but is secondary to HscA binding and Fe-S maturation.", "Retain as non-core process context rather than making oligomerization a defining function."))
    set_review(data, "GO:1990230", accept(gene, "GO:1990230", "HscB is part of the iron-sulfur cluster transfer/chaperone machinery.", "The complex annotation is consistent with HscA/HscB involvement in Fe-S protein maturation."))
    data["core_functions"] = [
        {
            "description": "J-domain co-chaperone that binds HscA and stimulates its ATPase activity during maturation of iron-sulfur-cluster-containing proteins.",
            "molecular_function": TERM["GO:0001671"],
            "directly_involved_in": [TERM["GO:0044571"], TERM["GO:0006457"]],
            "in_complex": TERM["GO:1990230"],
            "supported_by": standard_support(gene, "GO:0001671"),
        },
        {
            "description": "Binding to the HscA protein-folding chaperone as part of the Fe-S cluster transfer/folding machinery.",
            "molecular_function": TERM["GO:0051087"],
            "directly_involved_in": [TERM["GO:0044571"]],
            "in_complex": TERM["GO:1990230"],
            "supported_by": standard_support(gene, "GO:0051087"),
        },
    ]
    save_gene(gene, data)


def curate_hscA() -> None:
    gene = "hscA"
    data = yaml.safe_load((GENE_ROOT / gene / f"{gene}-ai-review.yaml").read_text())
    ensure_references(data, gene, data["id"])
    set_review(data, "GO:0005524", accept(gene, "GO:0005524", "HscA is an Hsp70-family nucleotide-binding chaperone.", "ATP binding is supported by the conserved Hsp70 nucleotide-binding domain."))
    set_review(data, "GO:0006457", accept(gene, "GO:0006457", "HscA chaperones folding/maturation of Fe-S cluster-containing proteins.", "Protein folding is correct process context for this specialized Hsp70-family chaperone."))
    set_review(data, "GO:0016226", accept(gene, "GO:0016226", "HscA participates in iron-sulfur cluster assembly.", "The HscA family is specifically involved in maturation of iron-sulfur-cluster-containing proteins."))
    set_review(data, "GO:0016887", accept(gene, "GO:0016887", "HscA hydrolyzes ATP, with activity stimulated by HscB.", "ATP hydrolysis is a direct molecular function of the Hsp70-family chaperone cycle."))
    ensure_new_annotation(
        data,
        gene,
        "GO:0051082",
        "enables",
        "UniProt maps HscA to unfolded protein binding through Hsp70 substrate-binding-domain evidence.",
        "Client binding is the direct chaperone molecular function paired with ATP hydrolysis in HscA-mediated Fe-S protein maturation.",
    )
    data["core_functions"] = [
        {
            "description": "ATP-dependent Hsp70-family chaperone activity supporting maturation of iron-sulfur-cluster-containing proteins.",
            "molecular_function": TERM["GO:0016887"],
            "directly_involved_in": [TERM["GO:0016226"], TERM["GO:0006457"]],
            "supported_by": standard_support(gene, "GO:0016887"),
        },
        {
            "description": "Binding of non-native or client proteins by the Hsp70 substrate-binding domain during Fe-S protein maturation.",
            "molecular_function": TERM["GO:0051082"],
            "directly_involved_in": [TERM["GO:0016226"], TERM["GO:0006457"]],
            "supported_by": standard_support(gene, "GO:0051082"),
        },
    ]
    save_gene(gene, data)


def curate_pp1548() -> None:
    gene = "PP_1548"
    data = yaml.safe_load((GENE_ROOT / gene / f"{gene}-ai-review.yaml").read_text())
    ensure_references(data, gene, data["id"])
    data["core_functions"] = []
    data["suggested_questions"] = [
        {"question": "Does PP_1548 function as a real DjlA-like co-chaperone in KT2440, or is the DjlA_N/TerB-like domain assignment only a weak family-level signal?"}
    ]
    save_gene(gene, data)


def curate_cspAII() -> None:
    gene = "cspA-II"
    data = yaml.safe_load((GENE_ROOT / gene / f"{gene}-ai-review.yaml").read_text())
    ensure_references(data, gene, data["id"])
    set_review(data, "GO:0003676", accept(gene, "GO:0003676", "The cold-shock/OB-fold domain evidence supports a conservative nucleic-acid-binding annotation.", "The evidence does not resolve a specific RNA or DNA target, so nucleic acid binding is the right first-pass level of specificity."))
    set_review(data, "GO:0005737", accept(gene, "GO:0005737", "Cytoplasmic localization is compatible with a small soluble cold-shock-domain protein.", "The UniProt subcellular-location mapping supports cytoplasm."))
    set_review(data, "GO:0005829", accept(gene, "GO:0005829", "Cytosolic localization is compatible with the same soluble cold-shock-domain context.", "The cytosol row is reasonable and slightly more specific than cytoplasm for this protein."))
    data["core_functions"] = [
        {
            "description": "Cold-shock-domain nucleic-acid-binding protein with unresolved RNA versus DNA target specificity.",
            "molecular_function": TERM["GO:0003676"],
            "locations": [TERM["GO:0005829"]],
            "supported_by": standard_support(gene, "GO:0003676"),
        }
    ]
    data["suggested_questions"] = [
        {"question": "Which RNA or single-stranded DNA targets, if any, define the physiological role of cspA-II in KT2440 stress adaptation?"}
    ]
    save_gene(gene, data)


def curate_pp3316() -> None:
    gene = "PP_3316"
    data = yaml.safe_load((GENE_ROOT / gene / f"{gene}-ai-review.yaml").read_text())
    ensure_references(data, gene, data["id"])
    set_review(data, "GO:0005524", accept(gene, "GO:0005524", "PP_3316 has conserved ClpA/ClpB-family AAA+ ATPase domains.", "ATP binding is supported by the conserved P-loop/AAA+ nucleotide-binding domain architecture."))
    set_review(data, "GO:0005737", accept(gene, "GO:0005737", "A cytoplasmic location is plausible for this soluble ClpA/ClpB-family ATPase candidate.", "The TreeGrafter cytoplasm annotation is consistent with a bacterial chaperone-associated ATPase."))
    set_review(data, "GO:0016887", accept(gene, "GO:0016887", "PP_3316 has conserved AAA+ ATPase domains and a ClpA/ClpB-family assignment.", "ATP hydrolysis is the direct, supportable molecular function for this chaperone-associated ATPase candidate."))
    set_review(data, "GO:0034605", keep_non_core(gene, "GO:0034605", "Cellular response to heat is plausible from ClpA/ClpB-family propagation but the exact KT2440 stress role is unresolved.", "Retain as non-core context; the reliable first-pass core is ATPase activity, not a specific heat-response phenotype."))
    data["core_functions"] = [
        {
            "description": "ClpA/ClpB-family AAA+ ATPase candidate with conserved ATP-binding and ATP-hydrolysis machinery; partner complex and client substrates remain unresolved.",
            "molecular_function": TERM["GO:0016887"],
            "locations": [TERM["GO:0005737"]],
            "supported_by": standard_support(gene, "GO:0016887"),
        }
    ]
    data["suggested_questions"] = [
        {"question": "Which Clp-like complex, if any, does PP_3316 join, and is its role protein disaggregation, protease adaptation, or another AAA+ chaperone-associated process?"}
    ]
    save_gene(gene, data)


def curate_cbpM() -> None:
    gene = "cbpM"
    data = yaml.safe_load((GENE_ROOT / gene / f"{gene}-ai-review.yaml").read_text())
    ensure_references(data, gene, data["id"])
    ensure_new_annotation(
        data,
        gene,
        "GO:0051087",
        "enables",
        "CbpM interacts with CbpA, a DnaJ-like protein-folding chaperone analog, and inhibits CbpA co-chaperone activity.",
        "Protein-folding chaperone binding is the most informative available GO molecular-function term for the direct CbpM-CbpA interaction; avoid generic protein binding.",
    )
    data["core_functions"] = [
        {
            "description": "CbpA-binding modulatory protein that inhibits CbpA DnaJ-like co-chaperone and DNA-binding activities, thereby modulating the DnaK chaperone system.",
            "molecular_function": TERM["GO:0051087"],
            "supported_by": standard_support(gene, "GO:0051087"),
        }
    ]
    data["suggested_questions"] = [
        {"question": "Is KT2440 CbpM an active inhibitor of CbpA under a defined stress condition, and what signal controls the CbpA/CbpM module?"}
    ]
    save_gene(gene, data)


def curate_cbpA() -> None:
    gene = "cbpA"
    data = yaml.safe_load((GENE_ROOT / gene / f"{gene}-ai-review.yaml").read_text())
    ensure_references(data, gene, data["id"])
    set_review(data, "GO:0003681", accept(gene, "GO:0003681", "CbpA preferentially recognizes curved DNA.", "Bent/curved DNA binding is directly supported by the HAMAP/UniRule functional annotation and nucleoid localization."))
    set_review(data, "GO:0005737", accept(gene, "GO:0005737", "CbpA is cytoplasmic.", "Cytoplasm is compatible with its bacterial DnaJ-like and DNA-binding roles."))
    set_review(data, "GO:0006457", accept(gene, "GO:0006457", "CbpA has DnaJ-like co-chaperone context and participates in protein folding.", "The DnaJ-domain/HSP40 evidence supports protein-folding process context."))
    set_review(data, "GO:0009295", accept(gene, "GO:0009295", "CbpA is nucleoid-associated.", "Nucleoid localization is consistent with its curved-DNA-binding activity."))
    set_review(data, "GO:0042026", accept(gene, "GO:0042026", "CbpA has DnaJ-like chaperone/refolding context, although its activity differs from autonomous DnaJ.", "Protein refolding is appropriate family-level process context for this DnaJ-like CbpA protein."))
    ensure_new_annotation(
        data,
        gene,
        "GO:0051082",
        "enables",
        "UniProt maps CbpA to unfolded protein binding through DnaJ/HSP40 domain evidence.",
        "Unfolded/client protein binding captures the direct chaperone-like substrate-binding aspect of CbpA better than generic protein binding.",
    )
    data["core_functions"] = [
        {
            "description": "Curved/bent DNA-binding activity at the bacterial nucleoid.",
            "molecular_function": TERM["GO:0003681"],
            "locations": [TERM["GO:0009295"]],
            "supported_by": standard_support(gene, "GO:0003681"),
        },
        {
            "description": "DnaJ-like client-protein binding that targets substrates for recognition by DnaK, with activity modulated by CbpM.",
            "molecular_function": TERM["GO:0051082"],
            "directly_involved_in": [TERM["GO:0006457"], TERM["GO:0042026"]],
            "locations": [TERM["GO:0005737"]],
            "supported_by": standard_support(gene, "GO:0051082"),
        },
    ]
    save_gene(gene, data)


def main() -> None:
    for func in (
        curate_hslO,
        curate_slyD,
        curate_hscB,
        curate_hscA,
        curate_pp1548,
        curate_cspAII,
        curate_pp3316,
        curate_cbpM,
        curate_cbpA,
    ):
        func()
    print("Curated chaperone/foldase split")


if __name__ == "__main__":
    main()
