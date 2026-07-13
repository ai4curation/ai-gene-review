#!/usr/bin/env python3
"""First-pass curate the PSEPK divisome/Z-ring/septation sub-batch."""

from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes/PSEPK"
TAXON = {
    "id": "NCBITaxon:160488",
    "label": "Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)",
}


GO_REF_TITLES = {
    "GO_REF:0000002": "Gene Ontology annotation through association of InterPro records with GO terms",
    "GO_REF:0000044": "Gene Ontology annotation based on UniProtKB/Swiss-Prot Subcellular Location vocabulary mapping, accompanied by conservative changes to GO terms applied by UniProt",
    "GO_REF:0000104": "Electronic Gene Ontology annotations created by transferring manual GO annotations between related proteins based on shared sequence features",
    "GO_REF:0000118": "TreeGrafter-generated GO annotations",
    "GO_REF:0000120": "Combined Automated Annotation using Multiple IEA Methods",
}


DATA = {
    "engB": {
        "id": "Q88RK5",
        "description": "engB encodes a probable cytosolic EngB-family GTP-binding protein required for normal bacterial septation. In this first pass it is retained as a septation-support factor in the divisome boundary rather than as a structural FtsZ-ring component.",
        "uniprot_support": [
            "DE   RecName: Full=Probable GTP-binding protein EngB",
            "Necessary for normal cell division and for the maintenance of",
            "normal septation.",
            "DR   InterPro; IPR030393; G_ENGB_dom.",
        ],
        "asta_support": "- **Protein Description:** RecName: Full=Probable GTP-binding protein EngB",
        "terms": {
            "GO:0005525": ("ACCEPT", "GTP binding is an appropriate core molecular-function annotation for this EngB-family P-loop GTPase.", "UniProt identifies EngB as a GTP-binding protein and records the GTP-binding/domain evidence."),
            "GO:0005829": ("ACCEPT", "Cytosol is the appropriate functional location for this soluble septation-associated GTP-binding protein.", "The GOA/UniProt records place EngB in the cytosol."),
            "GO:0090529": ("ACCEPT", "Cell septum assembly is the core process annotation for EngB in this first-pass divisome boundary.", "UniProt states that EngB is necessary for normal cell division and normal septation."),
        },
        "core_functions": [
            {
                "description": "Cytosolic EngB-family GTP-binding protein required for normal septation.",
                "molecular_function": {"id": "GO:0005525", "label": "GTP binding"},
                "directly_involved_in": [{"id": "GO:0090529", "label": "cell septum assembly"}],
                "locations": [{"id": "GO:0005829", "label": "cytosol"}],
            }
        ],
    },
    "PP_1309": {
        "id": "Q88NA3",
        "description": "PP_1309 encodes a predicted ZapG/YhcB-family inner-membrane Z-ring-associated cell division protein. The current local evidence supports membrane localization and cell-division/Z-ring context, but not a specific catalytic molecular function.",
        "uniprot_support": [
            "DE   RecName: Full=Z-ring associated protein G",
            "DE   AltName: Full=Cell division protein ZapG",
            "Cell inner membrane",
            "DR   GO; GO:0051301; P:cell division; IEA:UniProtKB-KW.",
            "DR   InterPro; IPR009386; ZapG-like.",
        ],
        "asta_support": "- **Protein Description:** RecName: Full=Z-ring associated protein G",
        "terms": {
            "GO:0005886": ("ACCEPT", "Plasma membrane localization is appropriate for this predicted single-pass inner-membrane ZapG/YhcB-family protein.", "UniProt records cell inner membrane localization and the GOA row assigns plasma membrane."),
        },
        "new_annotations": [
            {
                "id": "GO:0051301",
                "label": "cell division",
                "qualifier": "involved_in",
                "summary": "Cell division is a useful missing process annotation for PP_1309.",
                "reason": "The UniProt record names PP_1309 as Z-ring associated protein G / cell division protein ZapG and includes a cell-division GO cross-reference.",
                "support": ["DE   AltName: Full=Cell division protein ZapG", "DR   GO; GO:0051301; P:cell division; IEA:UniProtKB-KW."],
            }
        ],
        "core_functions": [
            {
                "description": "Predicted ZapG/YhcB-family inner-membrane cell-division protein with Z-ring-associated context.",
                "directly_involved_in": [{"id": "GO:0051301", "label": "cell division"}],
                "locations": [{"id": "GO:0005886", "label": "plasma membrane"}],
            }
        ],
    },
    "zapE": {
        "id": "Q88NA0",
        "description": "zapE encodes a cytoplasmic AFG1-family ATPase that interacts with FtsZ and reduces the stability of FtsZ polymers in the presence of ATP. It is retained as an ATP-hydrolyzing Z-ring-associated cell-division factor.",
        "uniprot_support": [
            "DE   RecName: Full=Cell division protein ZapE",
            "Reduces the stability of FtsZ polymers in the presence of",
            "ATP.",
            "SUBUNIT: Interacts with FtsZ.",
            "DR   GO; GO:0016887; F:ATP hydrolysis activity; IEA:UniProtKB-UniRule.",
        ],
        "asta_support": "- **Protein Description:** RecName: Full=Cell division protein ZapE",
        "terms": {
            "GO:0005524": ("KEEP_AS_NON_CORE", "ATP binding is correct but secondary to the more informative ATP hydrolysis annotation.", "ZapE is an AFG1-family ATPase with ATP binding and ATP hydrolysis annotations."),
            "GO:0005737": ("ACCEPT", "Cytoplasm localization is appropriate for ZapE.", "UniProt records ZapE as a cytoplasmic protein."),
            "GO:0016887": ("ACCEPT", "ATP hydrolysis activity is the core molecular activity for ZapE.", "UniProt and UniRule identify ZapE as an ATPase whose ATP-dependent action destabilizes FtsZ polymers."),
            "GO:0032153": ("ACCEPT", "Cell division site localization is appropriate for a Z-ring-associated FtsZ-interacting factor.", "ZapE interacts with FtsZ and is assigned to cell division site by TreeGrafter."),
            "GO:0051301": ("ACCEPT", "Cell division is the appropriate broad process annotation for ZapE.", "ZapE is a Z-ring-associated ATPase that modulates FtsZ polymer stability."),
        },
        "core_functions": [
            {
                "description": "ATP-hydrolyzing Z-ring-associated factor that interacts with FtsZ and reduces FtsZ-polymer stability.",
                "molecular_function": {"id": "GO:0016887", "label": "ATP hydrolysis activity"},
                "directly_involved_in": [{"id": "GO:0051301", "label": "cell division"}],
                "locations": [{"id": "GO:0005737", "label": "cytoplasm"}, {"id": "GO:0032153", "label": "cell division site"}],
            }
        ],
    },
    "ftsL": {
        "id": "Q88N83",
        "description": "ftsL encodes an essential single-pass inner-membrane cell division protein of the FtsB-FtsL-FtsQ divisome subcomplex. It localizes to the division septum and likely links upstream cytoplasmic division proteins to downstream periplasmic divisome proteins.",
        "uniprot_support": [
            "DE   RecName: Full=Cell division protein FtsL",
            "Essential cell division protein. May link together the",
            "Part of a complex composed of FtsB, FtsL and FtsQ.",
            "Note=Localizes to the division septum",
            "DR   GO; GO:0043093; P:FtsZ-dependent cytokinesis; IEA:UniProtKB-UniRule.",
        ],
        "asta_support": "- **Protein Description:** RecName: Full=Cell division protein FtsL",
        "terms": {
            "GO:0005886": ("ACCEPT", "Plasma membrane localization is appropriate for this inner-membrane divisome protein.", "UniProt records FtsL as a cell inner membrane protein."),
            "GO:0016020": ("KEEP_AS_NON_CORE", "Membrane is correct but less informative than plasma membrane and division-site localization.", "FtsL is a single-pass membrane protein."),
            "GO:0032153": ("ACCEPT", "Cell division site localization is core for FtsL.", "UniProt states that FtsL localizes to the division septum."),
            "GO:0043093": ("ACCEPT", "FtsZ-dependent cytokinesis is the core process for FtsL.", "FtsL is an essential divisome subcomplex component downstream of FtsZ-ring assembly."),
            "GO:0051301": ("KEEP_AS_NON_CORE", "Cell division is correct but broad relative to FtsZ-dependent cytokinesis.", "FtsL is an essential cell division protein."),
        },
        "core_functions": [
            {
                "description": "FtsB-FtsL-FtsQ divisome subcomplex member linking cytoplasmic and periplasmic division proteins during FtsZ-dependent cytokinesis.",
                "directly_involved_in": [{"id": "GO:0043093", "label": "FtsZ-dependent cytokinesis"}],
                "locations": [{"id": "GO:0005886", "label": "plasma membrane"}, {"id": "GO:0032153", "label": "cell division site"}],
            }
        ],
    },
    "ftsQ": {
        "id": "Q88N73",
        "description": "ftsQ encodes an essential single-pass inner-membrane FtsQ/DivIB-family divisome protein. It is part of the FtsB-FtsL-FtsQ subcomplex, localizes to the division septum, and may control correct divisome assembly.",
        "uniprot_support": [
            "DE   RecName: Full=Cell division protein FtsQ",
            "May control correct divisome assembly.",
            "Part of a complex composed of FtsB, FtsL and FtsQ.",
            "Note=Localizes to the division septum.",
            "DR   GO; GO:0043093; P:FtsZ-dependent cytokinesis; IEA:UniProtKB-UniRule.",
        ],
        "asta_support": "- **Protein Description:** RecName: Full=Cell division protein FtsQ",
        "terms": {
            "GO:0005886": ("ACCEPT", "Plasma membrane localization is appropriate for FtsQ.", "UniProt records FtsQ as a cell inner membrane protein."),
            "GO:0016020": ("KEEP_AS_NON_CORE", "Membrane is correct but less informative than plasma membrane and division-site localization.", "FtsQ is a single-pass membrane protein."),
            "GO:0032153": ("ACCEPT", "Cell division site localization is core for FtsQ.", "UniProt states that FtsQ localizes to the division septum."),
            "GO:0043093": ("ACCEPT", "FtsZ-dependent cytokinesis is a core process annotation for FtsQ.", "FtsQ is an essential divisome subcomplex member."),
            "GO:0090529": ("ACCEPT", "Cell septum assembly is appropriate for this septal divisome component.", "FtsQ localizes to the division septum and may control divisome assembly."),
        },
        "core_functions": [
            {
                "description": "FtsB-FtsL-FtsQ divisome subcomplex member that localizes to the division septum and supports correct divisome assembly during FtsZ-dependent cytokinesis.",
                "directly_involved_in": [{"id": "GO:0043093", "label": "FtsZ-dependent cytokinesis"}, {"id": "GO:0090529", "label": "cell septum assembly"}],
                "locations": [{"id": "GO:0005886", "label": "plasma membrane"}, {"id": "GO:0032153", "label": "cell division site"}],
            }
        ],
    },
    "ftsA": {
        "id": "Q88N72",
        "description": "ftsA encodes an FtsA/MreB-family peripheral inner-membrane protein that interacts with FtsZ and anchors or organizes the Z ring at the cytoplasmic side of the membrane during bacterial cytokinesis.",
        "uniprot_support": [
            "DE   RecName: Full=Cell division protein FtsA",
            "Cell division protein that is involved in the assembly of the",
            "May serve as a membrane anchor for the Z ring.",
            "Interacts with FtsZ.",
            "Cytoplasmic side",
            "DR   GO; GO:0043093; P:FtsZ-dependent cytokinesis; IEA:UniProtKB-UniRule.",
        ],
        "asta_support": "- **Protein Description:** RecName: Full=Cell division protein FtsA",
        "terms": {
            "GO:0005886": ("KEEP_AS_NON_CORE", "Plasma membrane localization is correct but less precise than cytoplasmic side of plasma membrane for FtsA.", "UniProt describes FtsA as a peripheral inner-membrane protein on the cytoplasmic side."),
            "GO:0009898": ("ACCEPT", "Cytoplasmic side of plasma membrane is the most informative location for FtsA.", "FtsA anchors the Z ring at the membrane through a conserved C-terminal amphipathic helix."),
            "GO:0032153": ("ACCEPT", "Cell division site localization is core for FtsA.", "UniProt states that FtsA localizes to the Z ring in an FtsZ-dependent manner."),
            "GO:0043093": ("ACCEPT", "FtsZ-dependent cytokinesis is the core process for FtsA.", "FtsA interacts with FtsZ and participates in Z-ring assembly."),
            "GO:0051301": ("KEEP_AS_NON_CORE", "Cell division is correct but broad relative to FtsZ-dependent cytokinesis.", "FtsA is a cell division protein involved in Z-ring assembly."),
        },
        "core_functions": [
            {
                "description": "Peripheral membrane FtsA/MreB-family Z-ring anchor that interacts with FtsZ during FtsZ-dependent cytokinesis.",
                "directly_involved_in": [{"id": "GO:0043093", "label": "FtsZ-dependent cytokinesis"}],
                "locations": [{"id": "GO:0009898", "label": "cytoplasmic side of plasma membrane"}, {"id": "GO:0032153", "label": "cell division site"}],
            }
        ],
    },
    "ftsB": {
        "id": "Q88MF8",
        "description": "ftsB encodes an essential single-pass inner-membrane cell division protein in the FtsB-FtsL-FtsQ divisome subcomplex. It localizes to the division septum and likely links upstream cytoplasmic division proteins to downstream periplasmic divisome proteins.",
        "uniprot_support": [
            "DE   RecName: Full=Cell division protein FtsB",
            "Essential cell division protein. May link together the",
            "Part of a complex composed of FtsB, FtsL and FtsQ.",
            "Note=Localizes to the division",
            "DR   GO; GO:0043093; P:FtsZ-dependent cytokinesis; IEA:UniProtKB-UniRule.",
        ],
        "asta_support": "- **Protein Description:** RecName: Full=Cell division protein FtsB",
        "terms": {
            "GO:0005886": ("ACCEPT", "Plasma membrane localization is appropriate for this inner-membrane divisome protein.", "UniProt records FtsB as a cell inner membrane single-pass protein."),
            "GO:0030428": ("ACCEPT", "Cell septum localization is appropriate for FtsB.", "UniProt states that FtsB localizes to the division septum."),
            "GO:0032153": ("ACCEPT", "Cell division site localization is core for FtsB.", "FtsB is a septal divisome subcomplex component."),
            "GO:0043093": ("ACCEPT", "FtsZ-dependent cytokinesis is the core process for FtsB.", "FtsB is an essential cell division protein in the FtsB-FtsL-FtsQ subcomplex."),
        },
        "core_functions": [
            {
                "description": "FtsB-FtsL-FtsQ divisome subcomplex member localizing to the septal division site during FtsZ-dependent cytokinesis.",
                "directly_involved_in": [{"id": "GO:0043093", "label": "FtsZ-dependent cytokinesis"}],
                "locations": [{"id": "GO:0005886", "label": "plasma membrane"}, {"id": "GO:0032153", "label": "cell division site"}, {"id": "GO:0030428", "label": "cell septum"}],
            }
        ],
    },
    "dedD": {
        "id": "Q88LD7",
        "description": "dedD encodes a predicted membrane-associated SPOR-domain cell division protein. The local evidence supports septal/division-site localization and peptidoglycan binding, consistent with a peptidoglycan-binding septal factor in cytokinesis.",
        "uniprot_support": [
            "DE   SubName: Full=Cell division protein",
            "DR   GO; GO:0042834; F:peptidoglycan binding; IEA:InterPro.",
            "DR   InterPro; IPR052521; Cell_div_SPOR-domain.",
            "DR   InterPro; IPR007730; SPOR-like_dom.",
            "DR   PANTHER; PTHR38687:SF1; CELL DIVISION PROTEIN DEDD; 1.",
        ],
        "asta_support": "- **Protein Description:** SubName: Full=Cell division protein",
        "terms": {
            "GO:0030428": ("ACCEPT", "Cell septum localization is appropriate for this SPOR-domain septal protein.", "TreeGrafter and family/domain context place DedD at the septum."),
            "GO:0032153": ("ACCEPT", "Cell division site localization is appropriate for DedD.", "The protein is a SPOR-domain cell division protein."),
            "GO:0032506": ("ACCEPT", "Cytokinetic process is the best available process annotation for DedD in this first pass.", "DedD is a cell division protein with septal localization and peptidoglycan-binding evidence."),
            "GO:0042834": ("ACCEPT", "Peptidoglycan binding is the core molecular function supported by SPOR-domain evidence.", "The GOA and InterPro records support peptidoglycan binding."),
        },
        "core_functions": [
            {
                "description": "SPOR-domain septal protein with peptidoglycan-binding activity in cytokinetic context.",
                "molecular_function": {"id": "GO:0042834", "label": "peptidoglycan binding"},
                "directly_involved_in": [{"id": "GO:0032506", "label": "cytokinetic process"}],
                "locations": [{"id": "GO:0032153", "label": "cell division site"}, {"id": "GO:0030428", "label": "cell septum"}],
            }
        ],
    },
    "zipA": {
        "id": "Q88F24",
        "description": "zipA encodes the essential inner-membrane Z-ring anchor ZipA. It binds FtsZ, stabilizes and cross-links FtsZ protofilaments, anchors the Z ring at the cytoplasmic membrane, and recruits downstream cell division proteins to the septal ring.",
        "uniprot_support": [
            "DE   RecName: Full=Cell division protein ZipA",
            "Essential cell division protein that stabilizes the FtsZ",
            "membrane anchor for the Z ring.",
            "Interacts with FtsZ via their C-terminal domains.",
            "DR   GO; GO:0043093; P:FtsZ-dependent cytokinesis; IEA:UniProtKB-UniRule.",
        ],
        "asta_support": "- **Protein Description:** RecName: Full=Cell division protein ZipA",
        "terms": {
            "GO:0000917": ("ACCEPT", "Division septum assembly is appropriate for ZipA.", "ZipA stabilizes FtsZ protofilaments and recruits downstream division proteins to the septal ring."),
            "GO:0005886": ("ACCEPT", "Plasma membrane localization is appropriate for this inner-membrane Z-ring anchor.", "UniProt records ZipA as a cell inner membrane single-pass protein."),
            "GO:0016020": ("KEEP_AS_NON_CORE", "Membrane is correct but less precise than plasma membrane and cell division site.", "ZipA is a single-pass inner-membrane protein."),
            "GO:0032153": ("ACCEPT", "Cell division site localization is core for ZipA.", "ZipA localizes to the Z ring in an FtsZ-dependent manner."),
            "GO:0043093": ("ACCEPT", "FtsZ-dependent cytokinesis is a core process annotation for ZipA.", "ZipA stabilizes and anchors the FtsZ ring."),
            "GO:0090529": ("ACCEPT", "Cell septum assembly is appropriate for ZipA.", "ZipA recruits downstream division proteins to the septal ring."),
        },
        "core_functions": [
            {
                "description": "Inner-membrane Z-ring anchor that stabilizes FtsZ protofilaments and recruits downstream septal division proteins.",
                "directly_involved_in": [{"id": "GO:0043093", "label": "FtsZ-dependent cytokinesis"}, {"id": "GO:0090529", "label": "cell septum assembly"}],
                "locations": [{"id": "GO:0005886", "label": "plasma membrane"}, {"id": "GO:0032153", "label": "cell division site"}],
            }
        ],
    },
    "PP_5090": {
        "id": "Q88CU0",
        "description": "PP_5090 encodes a predicted outer-membrane SPOR-domain/RlpA-family peptidoglycan-binding cell division protein. The current local evidence supports outer-membrane localization and peptidoglycan binding; the precise septal remodeling role remains unresolved.",
        "uniprot_support": [
            "DE   SubName: Full=Cell division protein",
            "DR   GO; GO:0009279; C:cell outer membrane; IEA:TreeGrafter.",
            "DR   GO; GO:0042834; F:peptidoglycan binding; IEA:InterPro.",
            "DR   GO; GO:0051301; P:cell division; IEA:UniProtKB-KW.",
            "DR   PANTHER; PTHR34183; ENDOLYTIC PEPTIDOGLYCAN TRANSGLYCOSYLASE RLPA; 1.",
        ],
        "asta_support": "- **Protein Description:** SubName: Full=Cell division protein",
        "terms": {
            "GO:0009279": ("ACCEPT", "Cell outer membrane localization is appropriate for this predicted membrane-associated RlpA/SPOR-domain protein.", "TreeGrafter and UniProt assign outer membrane localization."),
            "GO:0042834": ("ACCEPT", "Peptidoglycan binding is the core molecular-function annotation for PP_5090.", "The SPOR-domain/InterPro evidence supports peptidoglycan binding."),
        },
        "new_annotations": [
            {
                "id": "GO:0051301",
                "label": "cell division",
                "qualifier": "involved_in",
                "summary": "Cell division is a useful missing process annotation for PP_5090.",
                "reason": "The record is a cell division protein with SPOR-domain peptidoglycan-binding evidence and a UniProt cell-division GO cross-reference.",
                "support": ["DE   SubName: Full=Cell division protein", "DR   GO; GO:0051301; P:cell division; IEA:UniProtKB-KW."],
            }
        ],
        "core_functions": [
            {
                "description": "Outer-membrane SPOR/RlpA-family peptidoglycan-binding cell-division protein candidate.",
                "molecular_function": {"id": "GO:0042834", "label": "peptidoglycan binding"},
                "directly_involved_in": [{"id": "GO:0051301", "label": "cell division"}],
                "locations": [{"id": "GO:0009279", "label": "cell outer membrane"}],
            }
        ],
    },
    "PP_5202": {
        "id": "Q88CH9",
        "description": "PP_5202 encodes a predicted ZapA-family Z-ring-associated cell division protein. It promotes FtsZ filament bundling by inhibiting FtsZ GTPase activity, is recruited early to midcell, and is retained as a cytosolic/cell-division-site Z-ring assembly factor.",
        "uniprot_support": [
            "DE   RecName: Full=Cell division protein ZapA",
            "Activator of cell division through the inhibition of FtsZ",
            "promoting FtsZ assembly into bundles of",
            "protofilaments necessary for the formation of the division Z ring.",
            "Homodimer. Interacts with FtsZ.",
            "DR   GO; GO:0043093; P:FtsZ-dependent cytokinesis; IEA:TreeGrafter.",
        ],
        "asta_support": "- **Protein Description:** RecName: Full=Cell division protein ZapA",
        "terms": {
            "GO:0000917": ("ACCEPT", "Division septum assembly is appropriate for ZapA.", "ZapA promotes FtsZ bundling needed for division Z-ring formation."),
            "GO:0000921": ("REMOVE", "Septin ring assembly is not appropriate for bacterial ZapA.", "The local evidence supports bacterial FtsZ Z-ring assembly, not eukaryotic septin-ring assembly."),
            "GO:0005737": ("KEEP_AS_NON_CORE", "Cytoplasm is correct but less precise than cytosol and cell-division-site localization.", "ZapA is a soluble cytoplasmic Z-ring-associated factor."),
            "GO:0005829": ("ACCEPT", "Cytosol localization is appropriate for ZapA.", "TreeGrafter assigns cytosol and UniProt records cytoplasmic localization."),
            "GO:0030428": ("ACCEPT", "Cell septum localization is appropriate for ZapA.", "ZapA is recruited early at midcell and supports Z-ring formation."),
            "GO:0032153": ("ACCEPT", "Cell division site localization is core for ZapA.", "ZapA is a Z-ring-associated cell division protein recruited at midcell."),
            "GO:0043093": ("ACCEPT", "FtsZ-dependent cytokinesis is the core process annotation for ZapA.", "ZapA acts through FtsZ assembly into bundles of protofilaments."),
        },
        "core_functions": [
            {
                "description": "ZapA-family Z-ring-associated factor promoting FtsZ filament bundling during FtsZ-dependent cytokinesis.",
                "directly_involved_in": [{"id": "GO:0043093", "label": "FtsZ-dependent cytokinesis"}, {"id": "GO:0000917", "label": "division septum assembly"}],
                "locations": [{"id": "GO:0005829", "label": "cytosol"}, {"id": "GO:0032153", "label": "cell division site"}, {"id": "GO:0030428", "label": "cell septum"}],
            }
        ],
    },
}


def goa_support(gene: str, term: dict[str, str]) -> dict[str, str]:
    return {
        "reference_id": f"file:PSEPK/{gene}/{gene}-goa.tsv",
        "supporting_text": f"{term['id']}\t{term['label']}",
    }


def file_support(gene: str, text: str) -> dict[str, str]:
    return {"reference_id": f"file:PSEPK/{gene}/{gene}-uniprot.txt", "supporting_text": text}


def asta_support(gene: str, text: str) -> dict[str, str]:
    return {"reference_id": f"file:PSEPK/{gene}/{gene}-deep-research-asta.md", "supporting_text": text}


def curate_gene(gene: str, info: dict) -> None:
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    doc["id"] = info["id"]
    doc["gene_symbol"] = gene
    doc["product_type"] = "PROTEIN"
    doc["status"] = "COMPLETE"
    doc["taxon"] = TAXON
    doc["description"] = info["description"]

    term_decisions = info["terms"]
    for annotation in doc["existing_annotations"]:
        term = annotation["term"]
        action, summary, reason = term_decisions[term["id"]]
        supported_by = [goa_support(gene, term)]
        for text in info["uniprot_support"][:3]:
            supported_by.append(file_support(gene, text))
        supported_by.append(asta_support(gene, info["asta_support"]))
        annotation["review"] = {
            "summary": summary,
            "action": action,
            "reason": reason,
            "supported_by": supported_by,
        }

    for new in info.get("new_annotations", []):
        doc["existing_annotations"].append(
            {
                "term": {"id": new["id"], "label": new["label"]},
                "evidence_type": "IEA",
                "original_reference_id": f"file:PSEPK/{gene}/{gene}-uniprot.txt",
                "qualifier": new["qualifier"],
                "review": {
                    "summary": new["summary"],
                    "action": "NEW",
                    "reason": new["reason"],
                    "supported_by": [file_support(gene, text) for text in new["support"]],
                },
            }
        )

    references = []
    seen = set()
    for annotation in doc["existing_annotations"]:
        ref = annotation.get("original_reference_id")
        if ref in GO_REF_TITLES and ref not in seen:
            references.append({"id": ref, "title": GO_REF_TITLES[ref], "findings": []})
            seen.add(ref)
    for ref_id, title in [
        (f"file:PSEPK/{gene}/{gene}-goa.tsv", f"QuickGO GOA annotations for {gene}"),
        (f"file:PSEPK/{gene}/{gene}-uniprot.txt", f"UniProtKB entry for {gene} ({info['id']})"),
        (f"file:PSEPK/{gene}/{gene}-deep-research-asta.md", f"Asta retrieval report for {gene} ({info['id']})"),
    ]:
        references.append({"id": ref_id, "title": title, "findings": []})
    doc["references"] = references

    core_functions = info["core_functions"]
    for core in core_functions:
        supported_by = []
        if "molecular_function" in core:
            supported_by.append(file_support(gene, info["uniprot_support"][0]))
        for process in core.get("directly_involved_in", []):
            term_id = process["id"]
            for annotation in doc["existing_annotations"]:
                if annotation["term"]["id"] == term_id:
                    if annotation["original_reference_id"].startswith("GO_REF"):
                        supported_by.append(goa_support(gene, annotation["term"]))
                    break
        for location in core.get("locations", []):
            term_id = location["id"]
            for annotation in doc["existing_annotations"]:
                if annotation["term"]["id"] == term_id and annotation["original_reference_id"].startswith("GO_REF"):
                    supported_by.append(goa_support(gene, annotation["term"]))
                    break
        for text in info["uniprot_support"]:
            supported_by.append(file_support(gene, text))
        supported_by.append(asta_support(gene, info["asta_support"]))
        core["supported_by"] = supported_by
    doc["core_functions"] = core_functions
    doc["proposed_new_terms"] = []
    doc["suggested_questions"] = [
        {
            "question": f"What is the precise P. putida KT2440 divisome role, interaction partner set, and essentiality of {gene} under standard and stress growth conditions?"
        }
    ]
    doc["suggested_experiments"] = [
        {
            "description": f"Use native-locus fluorescent tagging or depletion of {gene} to test septal localization, FtsZ-ring effects, and cell-division phenotypes.",
            "experiment_type": "cell-division localization and depletion assay",
        }
    ]

    path.write_text(yaml.safe_dump(doc, sort_keys=False, allow_unicode=False, width=1000), encoding="utf-8")


def main() -> None:
    for gene, info in DATA.items():
        curate_gene(gene, info)
        print(f"Curated {gene}")


if __name__ == "__main__":
    main()
