#!/usr/bin/env python3
"""First-pass curation for ribosome assembly, maturation, and hibernation genes."""

from __future__ import annotations

import re
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes" / "PSEPK"
MODULE_PATH = ROOT / "modules" / "bacterial_ribosome_maturation_regulation_boundary.yaml"
BATCH_TSV = (
    "projects/P_PUTIDA/batches/"
    "module_translation_rna_processing_ribosome_assembly_maturation_hibernation.tsv"
)


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):  # type: ignore[override]
        return True


def term(go_id: str, label: str) -> dict[str, str]:
    return {"id": go_id, "label": label}


TERM = {
    "GO:0000027": term("GO:0000027", "ribosomal large subunit assembly"),
    "GO:0000028": term("GO:0000028", "ribosomal small subunit assembly"),
    "GO:0000166": term("GO:0000166", "nucleotide binding"),
    "GO:0000967": term("GO:0000967", "rRNA 5'-end processing"),
    "GO:0003676": term("GO:0003676", "nucleic acid binding"),
    "GO:0003723": term("GO:0003723", "RNA binding"),
    "GO:0003824": term("GO:0003824", "catalytic activity"),
    "GO:0003924": term("GO:0003924", "GTPase activity"),
    "GO:0004222": term("GO:0004222", "metalloendopeptidase activity"),
    "GO:0004518": term("GO:0004518", "nuclease activity"),
    "GO:0004521": term("GO:0004521", "RNA endonuclease activity"),
    "GO:0005524": term("GO:0005524", "ATP binding"),
    "GO:0005525": term("GO:0005525", "GTP binding"),
    "GO:0005737": term("GO:0005737", "cytoplasm"),
    "GO:0005829": term("GO:0005829", "cytosol"),
    "GO:0005840": term("GO:0005840", "ribosome"),
    "GO:0005886": term("GO:0005886", "plasma membrane"),
    "GO:0006364": term("GO:0006364", "rRNA processing"),
    "GO:0006400": term("GO:0006400", "tRNA modification"),
    "GO:0006412": term("GO:0006412", "translation"),
    "GO:0006417": term("GO:0006417", "regulation of translation"),
    "GO:0006446": term("GO:0006446", "regulation of translational initiation"),
    "GO:0008080": term("GO:0008080", "N-acetyltransferase activity"),
    "GO:0008168": term("GO:0008168", "methyltransferase activity"),
    "GO:0008270": term("GO:0008270", "zinc ion binding"),
    "GO:0008276": term("GO:0008276", "protein methyltransferase activity"),
    "GO:0008999": term("GO:0008999", "protein-N-terminal-alanine acetyltransferase activity"),
    "GO:0009409": term("GO:0009409", "response to cold"),
    "GO:0009432": term("GO:0009432", "SOS response"),
    "GO:0010467": term("GO:0010467", "gene expression"),
    "GO:0016279": term("GO:0016279", "protein-lysine N-methyltransferase activity"),
    "GO:0016407": term("GO:0016407", "acetyltransferase activity"),
    "GO:0016740": term("GO:0016740", "transferase activity"),
    "GO:0016747": term(
        "GO:0016747",
        "acyltransferase activity, transferring groups other than amino-acyl groups",
    ),
    "GO:0016788": term("GO:0016788", "hydrolase activity, acting on ester bonds"),
    "GO:0016879": term("GO:0016879", "ligase activity, forming carbon-nitrogen bonds"),
    "GO:0017111": term("GO:0017111", "ribonucleoside triphosphate phosphatase activity"),
    "GO:0017148": term("GO:0017148", "negative regulation of translation"),
    "GO:0018169": term("GO:0018169", "ribosomal S6-glutamic acid ligase activity"),
    "GO:0019843": term("GO:0019843", "rRNA binding"),
    "GO:0022627": term("GO:0022627", "cytosolic small ribosomal subunit"),
    "GO:0030490": term("GO:0030490", "maturation of SSU-rRNA"),
    "GO:0032259": term("GO:0032259", "methylation"),
    "GO:0032561": term("GO:0032561", "guanyl ribonucleotide binding"),
    "GO:0035596": term("GO:0035596", "methylthiotransferase activity"),
    "GO:0035599": term("GO:0035599", "aspartic acid methylthiotransferase activity"),
    "GO:0036009": term("GO:0036009", "protein-glutamine N-methyltransferase activity"),
    "GO:0042254": term("GO:0042254", "ribosome biogenesis"),
    "GO:0042256": term("GO:0042256", "cytosolic ribosome assembly"),
    "GO:0042274": term("GO:0042274", "ribosomal small subunit biogenesis"),
    "GO:0043022": term("GO:0043022", "ribosome binding"),
    "GO:0043023": term("GO:0043023", "ribosomal large subunit binding"),
    "GO:0043024": term("GO:0043024", "ribosomal small subunit binding"),
    "GO:0043168": term("GO:0043168", "anion binding"),
    "GO:0045900": term("GO:0045900", "negative regulation of translational elongation"),
    "GO:0046872": term("GO:0046872", "metal ion binding"),
    "GO:0051536": term("GO:0051536", "iron-sulfur cluster binding"),
    "GO:0051539": term("GO:0051539", "4 iron, 4 sulfur cluster binding"),
    "GO:0070181": term("GO:0070181", "small ribosomal subunit rRNA binding"),
    "GO:0090071": term("GO:0090071", "negative regulation of ribosome biogenesis"),
    "GO:0097216": term("GO:0097216", "guanosine tetraphosphate binding"),
    "GO:0103039": term("GO:0103039", "protein methylthiotransferase activity"),
    "GO:1902626": term("GO:1902626", "assembly of large subunit precursor of preribosome"),
    "GO:1990904": term("GO:1990904", "ribonucleoprotein complex"),
}


GENES = [
    "yigZ",
    "rimI",
    "der",
    "darP",
    "hpf",
    "rimO",
    "era",
    "rimM",
    "prmB",
    "PP_1910",
    "PP_2956",
    "ycaO",
    "PP_3810",
    "rbfA",
    "rimP",
    "ybeY",
    "rsfS",
    "prmA",
    "PP_4885",
    "PP_4996",
    "typA",
    "rmf",
    "PP_5700",
    "PP_5726",
]


SPEC = {
    "yigZ": {
        "description": "yigZ encodes an IMPACT-family ribosome-binding factor candidate in the cytoplasm, with first-pass support for translation-initiation regulatory context but no resolved catalytic activity.",
        "role": "IMPACT/YigZ-family ribosome-binding translation-initiation regulatory candidate.",
        "part": "ribosome_maturation_gtpases_and_binding_factors",
        "core": [
            {
                "description": "IMPACT-family ribosome-binding factor candidate in translational initiation regulation.",
                "directly_involved_in": ["GO:0006446"],
                "locations": ["GO:0005737"],
            }
        ],
        "accept": {"GO:0006446"},
        "non_core": {"GO:0005737"},
        "over": {"GO:0017111", "GO:0032561", "GO:0043168"},
    },
    "rimI": {
        "description": "rimI encodes the cytoplasmic GNAT-family N-acetyltransferase that acetylates the N-terminal alanine of ribosomal protein bS18.",
        "role": "ribosomal protein bS18 N-terminal alanine acetyltransferase.",
        "part": "ribosomal_protein_modification",
        "core": [
            {
                "description": "N-terminal alanine acetyltransferase activity on ribosomal protein bS18.",
                "molecular_function": "GO:0008999",
                "locations": ["GO:0005737"],
            }
        ],
        "accept": {"GO:0008999"},
        "non_core": {"GO:0005737"},
        "over": {"GO:0008080", "GO:0016407", "GO:0016740", "GO:0016747"},
    },
    "der": {
        "description": "der encodes the conserved EngA/Der ribosome-associated GTPase, a late-stage ribosome biogenesis factor.",
        "role": "EngA/Der ribosome-associated GTPase in late ribosome biogenesis.",
        "part": "ribosome_maturation_gtpases_and_binding_factors",
        "core": [
            {
                "description": "Ribosome-associated GTPase activity during late ribosome biogenesis.",
                "molecular_function": "GO:0003924",
                "directly_involved_in": ["GO:0042254"],
            }
        ],
        "accept": {"GO:0043022"},
        "non_core": {"GO:0005525"},
        "core_support": "GTPase that plays an essential role in the late steps of",
    },
    "darP": {
        "description": "darP encodes a cytoplasmic DarP/YjgA-family factor that binds rRNA/ribosomes and participates in 50S large-subunit precursor assembly.",
        "role": "DarP large-subunit maturation factor with rRNA and ribosome binding.",
        "part": "large_subunit_maturation_factors",
        "core": [
            {
                "description": "rRNA/ribosome-binding factor for large-subunit precursor assembly.",
                "molecular_function": "GO:0019843",
                "directly_involved_in": ["GO:1902626"],
                "locations": ["GO:0005737"],
            }
        ],
        "accept": {"GO:0019843", "GO:0043022", "GO:1902626"},
        "non_core": {"GO:0005737", "GO:0005829"},
    },
    "hpf": {
        "description": "hpf encodes the ribosome hibernation-promoting factor HPF, which binds small ribosomal subunits and represses translational elongation during ribosome hibernation.",
        "role": "HPF ribosome hibernation factor that binds the small subunit and inhibits elongation.",
        "part": "hibernation_and_translation_silencing",
        "core": [
            {
                "description": "Small-subunit binding and negative regulation of translational elongation during ribosome hibernation.",
                "molecular_function": "GO:0043024",
                "directly_involved_in": ["GO:0045900"],
            }
        ],
        "accept": {"GO:0043024", "GO:0045900"},
        "over": {"GO:0022627"},
        "modify": {"GO:0022627": ["GO:0043024"]},
    },
    "rimO": {
        "description": "rimO encodes a radical-SAM, iron-sulfur-dependent methylthiotransferase that methylthiolates an aspartate residue in ribosomal protein uS12.",
        "role": "ribosomal protein uS12 aspartate methylthiotransferase.",
        "part": "ribosomal_protein_modification",
        "core": [
            {
                "description": "Aspartate methylthiotransferase activity on ribosomal protein uS12.",
                "molecular_function": "GO:0035599",
                "locations": ["GO:0005737"],
            }
        ],
        "accept": {"GO:0035599", "GO:0103039", "GO:0051536", "GO:0051539"},
        "non_core": {"GO:0005737", "GO:0005829"},
        "over": {"GO:0003824", "GO:0016740", "GO:0035596"},
        "remove": {"GO:0006400"},
    },
    "era": {
        "description": "era encodes an essential cytoplasmic and membrane-associated GTPase that binds 16S rRNA/30S subunits and functions in small-subunit assembly and biogenesis.",
        "role": "Era GTPase for 30S ribosomal small-subunit assembly.",
        "part": "small_subunit_maturation_factors",
        "core": [
            {
                "description": "GTPase activity coupled to 16S rRNA and small-subunit binding during 30S assembly.",
                "molecular_function": "GO:0003924",
                "directly_involved_in": ["GO:0000028", "GO:0042274"],
                "locations": ["GO:0005737", "GO:0005886"],
            }
        ],
        "accept": {"GO:0003924", "GO:0019843", "GO:0043024", "GO:0070181", "GO:0000028", "GO:0042274"},
        "non_core": {"GO:0005525", "GO:0005737", "GO:0005829", "GO:0005886"},
        "over": {"GO:0003723"},
    },
    "rimM": {
        "description": "rimM encodes a cytoplasmic ribosome maturation factor that binds immature 30S particles and assists late small-subunit biogenesis and rRNA processing.",
        "role": "RimM late 30S small-subunit maturation factor.",
        "part": "small_subunit_maturation_factors",
        "core": [
            {
                "description": "Ribosome binding during late small-subunit biogenesis.",
                "molecular_function": "GO:0043022",
                "directly_involved_in": ["GO:0042274"],
                "locations": ["GO:0005737"],
            }
        ],
        "accept": {"GO:0043022", "GO:0042274"},
        "non_core": {"GO:0005737", "GO:0005840", "GO:0006364"},
    },
    "prmB": {
        "description": "prmB encodes the ribosomal protein uL3 glutamine methyltransferase that methylates a conserved glutamine in large-subunit protein uL3.",
        "role": "ribosomal protein uL3 glutamine methyltransferase.",
        "part": "ribosomal_protein_modification",
        "core": [
            {
                "description": "Protein-glutamine N-methyltransferase activity on ribosomal protein uL3.",
                "molecular_function": "GO:0036009",
                "locations": ["GO:0005829"],
            }
        ],
        "accept": {"GO:0036009"},
        "non_core": {"GO:0005829"},
        "over": {"GO:0008168", "GO:0008276"},
        "remove": {"GO:0003676"},
    },
    "PP_1910": {
        "description": "PP_1910 encodes a YceD-family cytosolic factor implicated in 23S rRNA accumulation, stability, or large-subunit biogenesis.",
        "role": "YceD-family 23S rRNA accumulation and large-subunit biogenesis candidate.",
        "part": "large_subunit_maturation_factors",
        "core": [
            {
                "description": "YceD-family factor implicated in 23S rRNA accumulation and ribosome biogenesis.",
                "directly_involved_in": ["GO:0042254"],
                "locations": ["GO:0005829"],
            }
        ],
        "non_core": {"GO:0005829"},
        "core_support": "Plays a role in synthesis, processing and/or stability of 23S",
    },
    "PP_2956": {
        "description": "PP_2956 encodes a RimK-like ATP-grasp protein predicted to add glutamate residues to ribosomal protein S6.",
        "role": "RimK-like ribosomal protein S6 glutamic acid ligase.",
        "part": "ribosomal_protein_modification",
        "core": [
            {
                "description": "Ribosomal protein S6 glutamic acid ligase activity.",
                "molecular_function": "GO:0018169",
                "locations": ["GO:0005737"],
            }
        ],
        "accept": {"GO:0018169"},
        "non_core": {"GO:0000166", "GO:0005524", "GO:0005737", "GO:0046872"},
        "over": {"GO:0003824", "GO:0016879", "GO:0009432"},
    },
    "ycaO": {
        "description": "ycaO encodes a YcaO-domain protein with PANTHER/product support as a cofactor for beta-methylthiolation of ribosomal protein S12, but no current GOA rows.",
        "role": "YcaO-like accessory candidate for RimO-dependent ribosomal protein S12 methylthiolation.",
        "part": "ribosomal_protein_modification",
        "core": [],
    },
    "PP_3810": {
        "description": "PP_3810 is a low-information locus-tag protein with a protein-language-model ribosomal protein S3AE name but no GOA rows or resolved domain support in this pass.",
        "role": "low-information ribosomal-protein-like side node.",
        "part": "unresolved_ribosomal_interface_side_nodes",
        "core": [],
    },
    "rbfA": {
        "description": "rbfA encodes cytoplasmic ribosome-binding factor A, a late 30S assembly factor involved in small-subunit rRNA maturation.",
        "role": "RbfA late small-subunit rRNA maturation factor.",
        "part": "small_subunit_maturation_factors",
        "core": [
            {
                "description": "Small-subunit binding factor for SSU-rRNA maturation.",
                "molecular_function": "GO:0043024",
                "directly_involved_in": ["GO:0030490", "GO:0042254"],
                "locations": ["GO:0005737"],
            }
        ],
        "accept": {"GO:0043024", "GO:0030490", "GO:0042254"},
        "non_core": {"GO:0005737", "GO:0005829"},
        "modify": {"GO:0006364": ["GO:0030490"]},
    },
    "rimP": {
        "description": "rimP encodes a cytoplasmic ribosome maturation factor required for 30S small-subunit maturation.",
        "role": "RimP 30S small-subunit maturation factor.",
        "part": "small_subunit_maturation_factors",
        "core": [
            {
                "description": "RimP-dependent ribosomal small-subunit assembly and biogenesis.",
                "directly_involved_in": ["GO:0000028", "GO:0042274"],
                "locations": ["GO:0005737"],
            }
        ],
        "accept": {"GO:0000028", "GO:0042274"},
        "non_core": {"GO:0005737", "GO:0005829"},
        "over": {"GO:0006412"},
    },
    "ybeY": {
        "description": "ybeY encodes a cytoplasmic zinc-dependent single-strand RNA endonuclease involved in rRNA processing and ribosome biogenesis.",
        "role": "YbeY RNA endonuclease in rRNA processing and ribosome biogenesis.",
        "part": "small_subunit_maturation_factors",
        "core": [
            {
                "description": "RNA endonuclease activity in rRNA processing.",
                "molecular_function": "GO:0004521",
                "directly_involved_in": ["GO:0006364", "GO:0042254"],
                "locations": ["GO:0005737"],
            }
        ],
        "accept": {"GO:0004521", "GO:0006364", "GO:0042254"},
        "non_core": {"GO:0005737", "GO:0008270"},
        "modify": {"GO:0004222": ["GO:0004521"]},
    },
    "rsfS": {
        "description": "rsfS encodes a cytoplasmic ribosomal silencing factor that binds the large ribosomal subunit and negatively regulates translation/ribosome biogenesis.",
        "role": "RsfS large-subunit-binding ribosomal silencing factor.",
        "part": "hibernation_and_translation_silencing",
        "core": [
            {
                "description": "Large-subunit binding factor that negatively regulates translation and ribosome biogenesis.",
                "molecular_function": "GO:0043023",
                "directly_involved_in": ["GO:0017148", "GO:0090071"],
                "locations": ["GO:0005737"],
            }
        ],
        "accept": {"GO:0043023", "GO:0017148", "GO:0090071"},
        "non_core": {"GO:0005737"},
        "over": {"GO:0042256"},
    },
    "prmA": {
        "description": "prmA encodes the cytoplasmic ribosomal protein L11 lysine N-methyltransferase.",
        "role": "ribosomal protein L11 lysine N-methyltransferase.",
        "part": "ribosomal_protein_modification",
        "core": [
            {
                "description": "Protein-lysine N-methyltransferase activity on ribosomal protein L11.",
                "molecular_function": "GO:0016279",
                "locations": ["GO:0005737"],
            }
        ],
        "accept": {"GO:0016279"},
        "non_core": {"GO:0005737", "GO:0005829", "GO:0008276"},
    },
    "PP_4885": {
        "description": "PP_4885 is a low-information locus-tag protein with a protein-language-model SSU ribosomal protein S2p name but no GOA rows or resolved domain support in this pass.",
        "role": "low-information SSU ribosomal-protein-like side node.",
        "part": "unresolved_ribosomal_interface_side_nodes",
        "core": [],
    },
    "PP_4996": {
        "description": "PP_4996 encodes a YqgF/RuvX-family putative pre-16S rRNA nuclease implicated in rRNA 5-prime-end processing and ribosome biogenesis.",
        "role": "putative pre-16S rRNA nuclease for rRNA 5-prime-end processing.",
        "part": "small_subunit_maturation_factors",
        "core": [
            {
                "description": "Putative nuclease activity in pre-16S rRNA 5-prime-end processing.",
                "molecular_function": "GO:0004518",
                "directly_involved_in": ["GO:0000967"],
                "locations": ["GO:0005737"],
            }
        ],
        "accept": {"GO:0000967", "GO:0006364", "GO:0042254"},
        "non_core": {"GO:0005737", "GO:0005829"},
        "modify": {"GO:0016788": ["GO:0004518"]},
        "core_support": "Could be a nuclease involved in processing of the 5'-end of",
    },
    "typA": {
        "description": "typA encodes BipA/TypA, a cytoplasmic ribosome-associated GTPase involved in large-subunit assembly and stress-responsive ribosome biogenesis.",
        "role": "BipA/TypA ribosome-associated GTPase for large-subunit assembly.",
        "part": "ribosome_maturation_gtpases_and_binding_factors",
        "core": [
            {
                "description": "Ribosome-associated GTPase activity in large-subunit assembly.",
                "molecular_function": "GO:0003924",
                "directly_involved_in": ["GO:0000027", "GO:0042254"],
                "locations": ["GO:0005737"],
            }
        ],
        "accept": {"GO:0003924", "GO:0043022", "GO:0000027", "GO:0042254"},
        "non_core": {"GO:0005525", "GO:0005737", "GO:0005829", "GO:0009409", "GO:0010467", "GO:0097216", "GO:1990904"},
    },
    "rmf": {
        "description": "rmf encodes ribosome modulation factor, a stationary-phase hibernation factor that converts active 70S ribosomes into inactive dimers and regulates translation.",
        "role": "ribosome modulation factor in stationary-phase translation regulation.",
        "part": "hibernation_and_translation_silencing",
        "core": [
            {
                "description": "Ribosome modulation factor in regulation of translation.",
                "directly_involved_in": ["GO:0006417"],
                "locations": ["GO:0005737"],
            }
        ],
        "accept": {"GO:0006417"},
        "non_core": {"GO:0005737"},
    },
    "PP_5700": {
        "description": "PP_5700 encodes an RHF/RaiA-like ribosomal subunit interface protein candidate, but has no GOA rows and no resolved first-pass activity.",
        "role": "RHF/RaiA-like ribosomal subunit interface candidate.",
        "part": "hibernation_and_translation_silencing",
        "core": [],
    },
    "PP_5726": {
        "description": "PP_5726 is a low-information locus-tag protein with a protein-language-model SSU ribosomal protein S2p name but no GOA rows or resolved domain support in this pass.",
        "role": "low-information SSU ribosomal-protein-like side node.",
        "part": "unresolved_ribosomal_interface_side_nodes",
        "core": [],
    },
}


def load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text()) or {}


def dump_yaml(path: Path, data: dict) -> None:
    path.write_text(
        yaml.dump(
            data,
            Dumper=NoAliasDumper,
            sort_keys=False,
            allow_unicode=False,
            width=120,
        )
    )


def goa_support(gene: str, go_id: str, label: str) -> dict[str, str]:
    return {
        "reference_id": f"file:PSEPK/{gene}/{gene}-goa.tsv",
        "supporting_text": f"{go_id}\t{label}",
    }


def asta_reference(gene: str, accession: str | None) -> dict:
    findings = []
    if accession:
        findings.append(
            {
                "statement": "Asta retrieval was generated for this first-pass review and retained as lightweight identity context.",
                "supporting_text": f"uniprot_accession: {accession}",
            }
        )
    return {
        "id": f"file:PSEPK/{gene}/{gene}-deep-research-asta.md",
        "title": f"{gene} Asta gene-level retrieval report",
        "findings": findings,
    }


def file_reference(gene: str, suffix: str, title: str) -> dict:
    return {"id": f"file:PSEPK/{gene}/{gene}-{suffix}", "title": title, "findings": []}


def accession_from_uniprot(gene: str) -> str | None:
    path = GENE_ROOT / gene / f"{gene}-uniprot.txt"
    if not path.exists():
        return None
    match = re.search(r"^AC   ([A-Z0-9]+);", path.read_text(), re.MULTILINE)
    return match.group(1) if match else None


def references_for(gene: str, existing: list[dict] | None) -> list[dict]:
    refs = list(existing or [])
    seen = {ref.get("id") for ref in refs}
    additions = [
        file_reference(gene, "uniprot.txt", f"{gene} UniProt record"),
        file_reference(gene, "goa.tsv", f"{gene} GOA annotations"),
        asta_reference(gene, accession_from_uniprot(gene)),
    ]
    for ref in additions:
        if ref["id"] not in seen:
            refs.append(ref)
            seen.add(ref["id"])
    return refs


def make_review(gene: str, ann: dict) -> dict:
    spec = SPEC[gene]
    term_obj = ann.get("term") or {}
    go_id = term_obj.get("id")
    label = term_obj.get("label")
    replacements = (spec.get("modify") or {}).get(go_id)
    if replacements:
        action = "MODIFY"
    elif go_id in spec.get("remove", set()):
        action = "REMOVE"
    elif go_id in spec.get("over", set()):
        action = "MARK_AS_OVER_ANNOTATED"
    elif go_id in spec.get("accept", set()):
        action = "ACCEPT"
    else:
        action = "KEEP_AS_NON_CORE"

    if action == "ACCEPT":
        summary = f"{label} fits the first-pass role of {gene}."
        reason = f"The fetched UniProt/GOA context supports {spec['role']} This term is retained as a core or direct module-context annotation."
    elif action == "KEEP_AS_NON_CORE":
        summary = f"{label} is retained as accurate supporting context for {gene}."
        reason = f"The term is compatible with {spec['role']} but is not the most informative statement of the gene product's core role in this batch."
    elif action == "MARK_AS_OVER_ANNOTATED":
        summary = f"{label} is a broad parent term, peripheral consequence, or low-specificity electronic carryover for {gene}."
        reason = f"The first-pass role is {spec['role']} A sharper term is already present or the term is too broad to represent the core function."
    elif action == "REMOVE":
        summary = f"{label} does not match the supported ribosome-maturation role for {gene}."
        reason = f"The annotation appears to be an over-propagated electronic inference. The first-pass role is {spec['role']}"
    else:
        replacement_labels = ", ".join(TERM[t]["label"] for t in replacements)
        summary = f"{label} is in the right functional area but should be represented by {replacement_labels}."
        reason = f"The annotation points to the same biological context as {spec['role']}, but the proposed replacement term is more specific or better matched to the substrate."

    review = {
        "summary": summary,
        "action": action,
        "reason": reason,
        "supported_by": [goa_support(gene, go_id, label)],
    }
    if replacements:
        review["proposed_replacement_terms"] = [TERM[t] for t in replacements]
    return review


def build_core_function(gene: str, core: dict, goa_terms: set[str]) -> dict:
    entry = {"description": core["description"]}
    if "molecular_function" in core:
        entry["molecular_function"] = TERM[core["molecular_function"]]
    if core.get("directly_involved_in"):
        entry["directly_involved_in"] = [TERM[t] for t in core["directly_involved_in"]]
    if core.get("locations"):
        entry["locations"] = [TERM[t] for t in core["locations"]]
    supported_by = []
    for go_id in [core.get("molecular_function"), *(core.get("directly_involved_in") or [])]:
        if go_id and go_id in goa_terms:
            supported_by.append(goa_support(gene, go_id, TERM[go_id]["label"]))
    if not supported_by and SPEC[gene].get("core_support"):
        supported_by.append(
            {
                "reference_id": f"file:PSEPK/{gene}/{gene}-uniprot.txt",
                "supporting_text": SPEC[gene]["core_support"],
            }
        )
    if supported_by:
        entry["supported_by"] = supported_by
    return entry


def curate_gene(gene: str) -> None:
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    data = load_yaml(path)
    spec = SPEC[gene]
    data["status"] = "DRAFT"
    data["description"] = spec["description"]
    for ann in data.get("existing_annotations") or []:
        ann["review"] = make_review(gene, ann)
    goa_terms = {(ann.get("term") or {}).get("id") for ann in data.get("existing_annotations") or []}
    data["references"] = references_for(gene, data.get("references"))
    data["core_functions"] = [build_core_function(gene, core, goa_terms) for core in spec.get("core", [])]
    data["proposed_new_terms"] = []
    data["suggested_questions"] = [
        {"question": f"What is the direct KT2440 phenotype of deleting or depleting {gene} under ribosome assembly, hibernation, or translation-stress conditions?"}
    ]
    if not data["core_functions"]:
        data["suggested_questions"].append(
            {"question": f"Does {gene} encode a bona fide ribosome-associated factor in KT2440, or is the current product name a low-confidence protein-language-model assignment?"}
        )
    data["suggested_experiments"] = [
        {
            "description": f"Measure ribosome profiles and growth or translation phenotypes for a {gene} perturbation under standard, stationary-phase, cold-stress, and recovery conditions.",
            "experiment_type": "ribosome profiling and stress-phenotype assay",
        }
    ]
    dump_yaml(path, data)
    write_notes(gene)


def write_notes(gene: str) -> None:
    spec = SPEC[gene]
    notes = GENE_ROOT / gene / f"{gene}-notes.md"
    notes.write_text(
        "\n".join(
            [
                f"# {gene} notes",
                "",
                "## 2026-07-10 first-pass translation/RNA-processing ribosome-maturation split",
                "",
                f"- Role: {spec['role']}",
                f"- Primary evidence: fetched UniProt record, fetched GOA rows, and Asta retrieval report `genes/PSEPK/{gene}/{gene}-deep-research-asta.md`.",
                "- Curation policy: retain sharp ribosome-assembly, hibernation, or ribosomal-protein-modification terms; mark broad catalytic/binding parents as non-core or over-annotated; avoid adding a GO-level activity where the fetched data only supports a low-information product name.",
                "",
            ]
        )
    )


def annoton_id(gene: str, text: str) -> str:
    safe = re.sub(r"[^A-Za-z0-9]+", "_", f"{gene}_{text}".strip()).strip("_")
    return safe[:120]


PARTS = [
    (
        "ribosome_maturation_gtpases_and_binding_factors",
        "Ribosome maturation GTPases and binding factors",
        "Der/EngA, Era/BipA-like GTPase or IMPACT-family factors that couple nucleotide/binding state to ribosome biogenesis.",
    ),
    (
        "small_subunit_maturation_factors",
        "30S small-subunit maturation factors",
        "Factors for 16S rRNA processing, SSU-rRNA maturation, and late 30S assembly.",
    ),
    (
        "large_subunit_maturation_factors",
        "50S large-subunit maturation factors",
        "Factors for 23S rRNA accumulation and large-subunit precursor assembly.",
    ),
    (
        "ribosomal_protein_modification",
        "Ribosomal-protein modification enzymes and cofactors",
        "Enzymes and accessory candidates modifying ribosomal proteins bS18, uS12, uL3, L11, or S6.",
    ),
    (
        "hibernation_and_translation_silencing",
        "Ribosome hibernation and translation silencing",
        "HPF/RMF/RsfS/RHF-like factors that reduce translation or stabilize inactive ribosome states.",
    ),
    (
        "unresolved_ribosomal_interface_side_nodes",
        "Unresolved ribosomal interface and S2p-like side nodes",
        "Low-information locus-tag proteins with ribosomal-interface or S2p-like names but insufficient evidence for a GO-level activity.",
    ),
]


def build_annoton(gene: str, core: dict | None) -> dict:
    spec = SPEC[gene]
    label_text = core["description"] if core else spec["role"]
    annoton = {
        "id": annoton_id(gene, label_text),
        "label": f"{gene}: {label_text}",
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "role_description": label_text,
    }
    if core and core.get("molecular_function"):
        go_id = core["molecular_function"]
        annoton["function"] = {"preferred_term": TERM[go_id]["label"], "term": TERM[go_id]}
    if core and core.get("directly_involved_in"):
        annoton["processes"] = [{"preferred_term": TERM[t]["label"], "term": TERM[t]} for t in core["directly_involved_in"]]
    if core and core.get("locations"):
        annoton["locations"] = [{"preferred_term": TERM[t]["label"], "term": TERM[t]} for t in core["locations"]]
    return annoton


def build_module() -> dict:
    evidence = [
        {
            "source_id": f"file:{BATCH_TSV}",
            "title": "PSEPK translation/RNA ribosome assembly and hibernation split",
            "statement": "The batch records ribosome biogenesis GTPases, maturation factors, hibernation/silencing factors, ribosomal-protein modifiers, and low-information ribosomal-interface side nodes.",
        }
    ]
    for gene in GENES:
        evidence.append(
            {
                "source_id": f"file:PSEPK/{gene}/{gene}-ai-review.yaml",
                "title": f"Curated {gene} review",
                "statement": SPEC[gene]["description"],
            }
        )
    parts = []
    for order, (part_id, label, description) in enumerate(PARTS, start=1):
        genes = [gene for gene in GENES if SPEC[gene]["part"] == part_id]
        annotons = []
        for gene in genes:
            cores = SPEC[gene].get("core") or []
            if cores:
                annotons.extend(build_annoton(gene, core) for core in cores)
            else:
                annotons.append(build_annoton(gene, None))
        parts.append(
            {
                "order": order,
                "role": label,
                "node": {
                    "id": part_id,
                    "label": label,
                    "module_type": "BIOLOGICAL_PROCESS",
                    "description": description,
                    "annotons": annotons,
                },
            }
        )
    return {
        "id": "MODULE:bacterial_ribosome_maturation_regulation_boundary",
        "title": "Bacterial ribosome maturation, hibernation, and ribosomal-protein modification boundary",
        "description": "Boundary module for PSEPK ribosome assembly and maturation factors, hibernation/silencing factors, ribosomal-protein modification enzymes, and unresolved ribosomal-interface side nodes. Structural ribosomal proteins and rRNA modification enzymes are kept in separate modules.",
        "status": "DRAFT",
        "evidence": evidence,
        "module": {
            "id": "bacterial_ribosome_maturation_regulation_boundary",
            "label": "Bacterial ribosome maturation, hibernation, and ribosomal-protein modification boundary",
            "module_type": "BIOLOGICAL_PROCESS",
            "concepts": [
                {"preferred_term": TERM[t]["label"], "term": TERM[t]}
                for t in [
                    "GO:0042254",
                    "GO:0042274",
                    "GO:0000028",
                    "GO:0000027",
                    "GO:0030490",
                    "GO:0000967",
                    "GO:0006417",
                    "GO:0017148",
                    "GO:0090071",
                    "GO:0018169",
                ]
            ],
            "parts": parts,
        },
    }


def main() -> None:
    for gene in GENES:
        curate_gene(gene)
    dump_yaml(MODULE_PATH, build_module())


if __name__ == "__main__":
    main()
