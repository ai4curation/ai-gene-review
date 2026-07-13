#!/usr/bin/env python3
"""First-pass curation for KEGG ppu03430 mismatch-repair stubs."""

from __future__ import annotations

from pathlib import Path

import yaml


SPECIES = "PSEPK"
ROOT = Path("genes") / SPECIES


GO_REF_TITLES = {
    "GO_REF:0000002": "Gene Ontology annotation through association of InterPro records with GO terms",
    "GO_REF:0000104": "Electronic Gene Ontology annotations created by transferring manual GO annotations between related proteins based on shared sequence features",
    "GO_REF:0000108": "Automatic assignment of GO terms using logical inference, based on on inter-ontology links",
    "GO_REF:0000117": "Electronic Gene Ontology annotations created by ARBA machine learning models",
    "GO_REF:0000118": "TreeGrafter-generated GO annotations",
    "GO_REF:0000120": "Combined Automated Annotation using Multiple IEA Methods",
}


GENES: dict[str, dict] = {
    "dnaN": {
        "symbol": "dnaN",
        "description": (
            "dnaN (PP_0011) encodes the DNA polymerase III beta sliding clamp, "
            "a ring-shaped processivity factor that encircles DNA and tethers "
            "replicative polymerase and repair factors to the template during "
            "chromosomal DNA synthesis and post-replicative repair."
        ),
        "core": {
            "description": (
                "Beta sliding clamp subunit of the DNA polymerase III complex, "
                "supporting processive DNA synthesis during replication and "
                "providing a platform for repair proteins."
            ),
            "contributes_to_molecular_function": {
                "id": "GO:0003887",
                "label": "DNA-directed DNA polymerase activity",
            },
            "directly_involved_in": [
                {"id": "GO:0006260", "label": "DNA replication"},
                {
                    "id": "GO:0006271",
                    "label": "DNA strand elongation involved in DNA replication",
                },
            ],
            "locations": [{"id": "GO:0005737", "label": "cytoplasm"}],
            "in_complex": {"id": "GO:0009360", "label": "DNA polymerase III complex"},
        },
        "decisions": {
            "GO:0003677": ("KEEP_AS_NON_CORE", "DNA binding is expected for the beta clamp but less specific than its processivity-factor role"),
            "GO:0003887": ("MARK_AS_OVER_ANNOTATED", "the beta clamp contributes to polymerase activity but is not the catalytic polymerase subunit"),
            "GO:0005737": ("ACCEPT", "cytoplasmic location is appropriate for a bacterial replisome protein"),
            "GO:0006260": ("ACCEPT", "DNA replication is the core process for the sliding clamp"),
            "GO:0006271": ("ACCEPT", "the beta clamp supports processive strand elongation during DNA replication"),
            "GO:0008408": ("MARK_AS_OVER_ANNOTATED", "3'-5' exonuclease proofreading belongs to DnaQ-like exonuclease subunits rather than the beta clamp"),
            "GO:0009360": ("ACCEPT", "DnaN is the beta subunit of the DNA polymerase III complex"),
            "GO:0042802": ("KEEP_AS_NON_CORE", "the clamp is multimeric, but identical protein binding is not the informative pathway role"),
            "GO:0071897": ("KEEP_AS_NON_CORE", "DNA biosynthesis is a broad parent of DNA replication"),
        },
    },
    "PP_0353": {
        "symbol": "PP_0353",
        "description": (
            "PP_0353 encodes an RNase H/DnaQ-like predicted exonuclease in "
            "Pseudomonas putida KT2440. The current metadata support a "
            "conservative 3'-5' exonuclease assignment, but the physiological "
            "DNA-repair or replication substrate remains unresolved."
        ),
        "core": {
            "description": "Predicted DnaQ/RNase H-like 3'-5' exonuclease of unresolved pathway specificity.",
            "molecular_function": {"id": "GO:0008408", "label": "3'-5' exonuclease activity"},
            "locations": [{"id": "GO:0005829", "label": "cytosol"}],
        },
        "decisions": {
            "GO:0003676": ("KEEP_AS_NON_CORE", "nucleic acid binding is generic context for a nuclease-domain protein"),
            "GO:0004527": ("KEEP_AS_NON_CORE", "generic exonuclease activity is less specific than the 3'-5' exonuclease term"),
            "GO:0005829": ("KEEP_AS_NON_CORE", "cytosol is plausible but not pathway-defining"),
            "GO:0008408": ("ACCEPT", "DnaQ/RNase H-like domain and GOA support the 3'-5' exonuclease assignment"),
        },
    },
    "ssb": {
        "symbol": "ssb",
        "description": (
            "ssb (PP_0485) encodes the bacterial single-stranded DNA-binding "
            "protein, which coats ssDNA intermediates during replication, "
            "repair, and recombination to protect DNA and organize processing "
            "enzymes at the nucleoid."
        ),
        "core": {
            "description": "Single-stranded DNA-binding protein supporting DNA replication, repair, and recombination intermediates.",
            "molecular_function": {"id": "GO:0003697", "label": "single-stranded DNA binding"},
            "directly_involved_in": [
                {"id": "GO:0006260", "label": "DNA replication"},
                {"id": "GO:0006281", "label": "DNA repair"},
                {"id": "GO:0006310", "label": "DNA recombination"},
            ],
            "locations": [{"id": "GO:0009295", "label": "nucleoid"}],
        },
        "decisions": {
            "GO:0003697": ("ACCEPT", "single-stranded DNA binding is the defining SSB molecular function"),
            "GO:0006260": ("ACCEPT", "SSB is a core replication accessory protein"),
            "GO:0006281": ("ACCEPT", "SSB acts on repair ssDNA intermediates"),
            "GO:0006310": ("ACCEPT", "SSB acts on recombination ssDNA intermediates"),
            "GO:0009295": ("ACCEPT", "nucleoid localization is appropriate for a bacterial DNA-binding protein"),
        },
    },
    "xseB": {
        "symbol": "xseB",
        "description": (
            "xseB (PP_0529) encodes the small subunit of exodeoxyribonuclease "
            "VII. Together with XseA it forms the exonuclease VII complex, a "
            "single-stranded DNA exonuclease that contributes to DNA end "
            "processing and DNA catabolism in repair/recombination contexts."
        ),
        "core": {
            "description": "Small subunit of exodeoxyribonuclease VII, contributing to complex-level single-stranded DNA exonuclease activity.",
            "contributes_to_molecular_function": {
                "id": "GO:0008855",
                "label": "exodeoxyribonuclease VII activity",
            },
            "directly_involved_in": [{"id": "GO:0006308", "label": "DNA catabolic process"}],
            "locations": [{"id": "GO:0005829", "label": "cytosol"}],
            "in_complex": {"id": "GO:0009318", "label": "exodeoxyribonuclease VII complex"},
        },
        "decisions": {
            "GO:0005737": ("KEEP_AS_NON_CORE", "cytoplasm is plausible but less specific than cytosol in the current GOA set"),
            "GO:0005829": ("KEEP_AS_NON_CORE", "cytosol is plausible but not pathway-defining"),
            "GO:0006308": ("ACCEPT", "exonuclease VII participates in DNA catabolic processing"),
            "GO:0008855": ("ACCEPT", "XseB is the small subunit of the exodeoxyribonuclease VII enzyme"),
            "GO:0009318": ("ACCEPT", "XseB is a component of the exodeoxyribonuclease VII complex"),
        },
    },
    "holC": {
        "symbol": "holC",
        "description": (
            "holC (PP_0979) encodes DNA polymerase III subunit chi, an "
            "accessory clamp-loader subunit that links the replisome to "
            "single-stranded DNA-binding protein and supports DNA replication "
            "rather than catalyzing DNA synthesis itself."
        ),
        "core": {
            "description": "DNA polymerase III chi accessory subunit contributing to replisome function and DNA replication.",
            "contributes_to_molecular_function": {
                "id": "GO:0003887",
                "label": "DNA-directed DNA polymerase activity",
            },
            "directly_involved_in": [{"id": "GO:0006260", "label": "DNA replication"}],
        },
        "decisions": {
            "GO:0003677": ("KEEP_AS_NON_CORE", "DNA binding is plausible accessory context"),
            "GO:0003887": ("MARK_AS_OVER_ANNOTATED", "HolC contributes to DNA polymerase III function but is not the catalytic polymerase subunit"),
            "GO:0006260": ("ACCEPT", "HolC is a DNA replication accessory protein"),
            "GO:0032298": ("KEEP_AS_NON_CORE", "replication-initiation regulation is less direct than the core clamp-loader accessory role"),
            "GO:0071897": ("KEEP_AS_NON_CORE", "DNA biosynthesis is a broad parent of DNA replication"),
        },
    },
    "xseA": {
        "symbol": "xseA",
        "description": (
            "xseA (PP_1027) encodes the large catalytic subunit of "
            "exodeoxyribonuclease VII. With XseB it forms a bacterial "
            "single-stranded DNA exonuclease complex involved in DNA end "
            "processing and DNA catabolism."
        ),
        "core": {
            "description": "Large catalytic subunit of exodeoxyribonuclease VII for single-stranded DNA exonucleolytic processing.",
            "molecular_function": {
                "id": "GO:0008855",
                "label": "exodeoxyribonuclease VII activity",
            },
            "directly_involved_in": [{"id": "GO:0006308", "label": "DNA catabolic process"}],
            "locations": [{"id": "GO:0005737", "label": "cytoplasm"}],
            "in_complex": {"id": "GO:0009318", "label": "exodeoxyribonuclease VII complex"},
        },
        "decisions": {
            "GO:0003676": ("KEEP_AS_NON_CORE", "nucleic acid binding is generic for the nuclease"),
            "GO:0005737": ("KEEP_AS_NON_CORE", "cytoplasm is plausible but not pathway-defining"),
            "GO:0006308": ("ACCEPT", "exonuclease VII participates in DNA catabolic processing"),
            "GO:0008855": ("ACCEPT", "XseA is the large catalytic subunit of exodeoxyribonuclease VII"),
            "GO:0009318": ("ACCEPT", "XseA is a component of the exodeoxyribonuclease VII complex"),
        },
    },
    "sbcB": {
        "symbol": "sbcB",
        "description": (
            "sbcB (PP_1365) encodes exodeoxyribonuclease I, a 3'-to-5' "
            "single-stranded DNA exonuclease involved in DNA repair and "
            "recombination-associated DNA end processing."
        ),
        "core": {
            "description": "Single-stranded DNA 3'-5' exonuclease involved in DNA repair and DNA-end processing.",
            "molecular_function": {
                "id": "GO:0008310",
                "label": "single-stranded DNA 3'-5' DNA exonuclease activity",
            },
            "directly_involved_in": [{"id": "GO:0006281", "label": "DNA repair"}],
        },
        "decisions": {
            "GO:0000175": ("MODIFY", "RNA exonuclease activity is less appropriate for SbcB than the DNA-specific exonuclease term", [{"id": "GO:0008310", "label": "single-stranded DNA 3'-5' DNA exonuclease activity"}]),
            "GO:0003676": ("KEEP_AS_NON_CORE", "nucleic acid binding is generic for a DNA exonuclease"),
            "GO:0004527": ("KEEP_AS_NON_CORE", "generic exonuclease activity is less informative than DNA exonuclease activity"),
            "GO:0004529": ("ACCEPT", "DNA exonuclease activity fits exodeoxyribonuclease I"),
            "GO:0006281": ("ACCEPT", "SbcB-family exonucleases participate in DNA repair/recombination processing"),
            "GO:0008310": ("ACCEPT", "single-stranded DNA 3'-5' exonuclease activity is the most specific current function"),
        },
    },
    "recJ": {
        "symbol": "recJ",
        "description": (
            "recJ (PP_1477) encodes a single-stranded-DNA-specific 5'-to-3' "
            "exonuclease that processes DNA ends during repair and homologous "
            "recombination."
        ),
        "core": {
            "description": "Single-stranded-DNA-specific 5'-3' exonuclease for DNA repair and recombination processing.",
            "molecular_function": {"id": "GO:0008409", "label": "5'-3' exonuclease activity"},
            "directly_involved_in": [
                {"id": "GO:0006281", "label": "DNA repair"},
                {"id": "GO:0006310", "label": "DNA recombination"},
            ],
        },
        "decisions": {
            "GO:0003676": ("KEEP_AS_NON_CORE", "nucleic acid binding is generic for RecJ"),
            "GO:0006281": ("ACCEPT", "RecJ is a conserved DNA-repair exonuclease"),
            "GO:0006310": ("ACCEPT", "RecJ contributes to recombination-associated DNA end processing"),
            "GO:0008409": ("ACCEPT", "5'-3' exonuclease activity is the core RecJ molecular function"),
        },
    },
    "dnaEA": {
        "symbol": "dnaEA",
        "description": (
            "dnaEA (PP_1606) encodes the DNA polymerase III alpha subunit, the "
            "replicative DNA polymerase catalytic subunit that extends DNA "
            "strands during chromosomal replication."
        ),
        "core": {
            "description": "DNA polymerase III alpha catalytic subunit for DNA-templated DNA synthesis during replication.",
            "molecular_function": {
                "id": "GO:0003887",
                "label": "DNA-directed DNA polymerase activity",
            },
            "directly_involved_in": [{"id": "GO:0006260", "label": "DNA replication"}],
            "locations": [{"id": "GO:0005737", "label": "cytoplasm"}],
        },
        "decisions": {
            "GO:0003676": ("KEEP_AS_NON_CORE", "nucleic acid binding is generic for a DNA polymerase"),
            "GO:0003824": ("MARK_AS_OVER_ANNOTATED", "generic catalytic activity is uninformative when DNA polymerase activity is present"),
            "GO:0003887": ("ACCEPT", "DnaE alpha is the catalytic DNA polymerase III subunit"),
            "GO:0005737": ("KEEP_AS_NON_CORE", "cytoplasm is plausible but not pathway-defining"),
            "GO:0006260": ("ACCEPT", "DnaE alpha is a core DNA replication enzyme"),
            "GO:0008408": ("MARK_AS_OVER_ANNOTATED", "proofreading exonuclease activity is better assigned to DnaQ/epsilon in this batch"),
            "GO:0034061": ("KEEP_AS_NON_CORE", "DNA polymerase activity is a broad parent of DNA-directed DNA polymerase activity"),
            "GO:0071897": ("KEEP_AS_NON_CORE", "DNA biosynthesis is a broad parent of DNA replication"),
        },
    },
    "holB": {
        "symbol": "holB",
        "description": (
            "holB (PP_1966) encodes DNA polymerase III subunit delta', an "
            "accessory subunit of the clamp-loader complex that supports "
            "loading the beta clamp during DNA replication."
        ),
        "core": {
            "description": "Delta' clamp-loader subunit of DNA polymerase III supporting beta-clamp loading during DNA replication.",
            "contributes_to_molecular_function": {
                "id": "GO:0003887",
                "label": "DNA-directed DNA polymerase activity",
            },
            "directly_involved_in": [
                {"id": "GO:0006260", "label": "DNA replication"},
                {"id": "GO:0006261", "label": "DNA-templated DNA replication"},
            ],
            "in_complex": {"id": "GO:0009360", "label": "DNA polymerase III complex"},
        },
        "decisions": {
            "GO:0003677": ("KEEP_AS_NON_CORE", "DNA binding is accessory context"),
            "GO:0003887": ("MARK_AS_OVER_ANNOTATED", "HolB contributes to polymerase complex function but is not the catalytic polymerase"),
            "GO:0006260": ("ACCEPT", "HolB is a DNA replication clamp-loader subunit"),
            "GO:0006261": ("ACCEPT", "DNA-templated DNA replication is appropriate process context"),
            "GO:0008408": ("MARK_AS_OVER_ANNOTATED", "3'-5' exonuclease activity is not the expected role of the delta' clamp-loader subunit"),
            "GO:0009360": ("ACCEPT", "HolB is part of DNA polymerase III/clamp-loader machinery"),
            "GO:0034061": ("MARK_AS_OVER_ANNOTATED", "generic DNA polymerase activity is over-assigned to an accessory subunit"),
            "GO:0071897": ("KEEP_AS_NON_CORE", "DNA biosynthesis is a broad parent of DNA replication"),
        },
    },
    "dnaQ": {
        "symbol": "dnaQ",
        "description": (
            "dnaQ (PP_4141) encodes the DNA polymerase III epsilon "
            "proofreading subunit, a DnaQ-family 3'-to-5' exonuclease that "
            "edits misincorporated nucleotides during DNA replication."
        ),
        "core": {
            "description": "DNA polymerase III epsilon proofreading exonuclease for correction of misincorporated nucleotides during replication.",
            "molecular_function": {"id": "GO:0008408", "label": "3'-5' exonuclease activity"},
            "directly_involved_in": [
                {"id": "GO:0045004", "label": "DNA replication proofreading"},
                {"id": "GO:0006260", "label": "DNA replication"},
            ],
            "locations": [{"id": "GO:0005829", "label": "cytosol"}],
        },
        "decisions": {
            "GO:0003676": ("KEEP_AS_NON_CORE", "nucleic acid binding is generic for the exonuclease"),
            "GO:0003677": ("KEEP_AS_NON_CORE", "DNA binding is expected but less specific than proofreading exonuclease activity"),
            "GO:0003887": ("MARK_AS_OVER_ANNOTATED", "DnaQ is the proofreading exonuclease subunit rather than the polymerase catalytic subunit"),
            "GO:0004527": ("KEEP_AS_NON_CORE", "generic exonuclease activity is less specific than 3'-5' exonuclease activity"),
            "GO:0005829": ("KEEP_AS_NON_CORE", "cytosol is plausible but not pathway-defining"),
            "GO:0006260": ("ACCEPT", "DnaQ functions during DNA replication"),
            "GO:0008408": ("ACCEPT", "3'-5' exonuclease activity is the core DnaQ proofreading function"),
            "GO:0034061": ("MARK_AS_OVER_ANNOTATED", "DNA polymerase activity is over-assigned to a proofreading exonuclease subunit"),
            "GO:0045004": ("ACCEPT", "DNA replication proofreading is the core biological process"),
            "GO:0071897": ("KEEP_AS_NON_CORE", "DNA biosynthesis is a broad parent of DNA replication"),
        },
    },
    "dnaX": {
        "symbol": "dnaX",
        "description": (
            "dnaX (PP_4269) encodes the DNA polymerase III gamma/tau "
            "clamp-loader subunit, an ATP-binding replisome component that "
            "coordinates beta-clamp loading and polymerase assembly during "
            "DNA replication."
        ),
        "core": {
            "description": "ATP-binding gamma/tau clamp-loader subunit of DNA polymerase III supporting replisome assembly and beta-clamp loading.",
            "molecular_function": {"id": "GO:0005524", "label": "ATP binding"},
            "directly_involved_in": [
                {"id": "GO:0006260", "label": "DNA replication"},
                {"id": "GO:0006261", "label": "DNA-templated DNA replication"},
            ],
            "in_complex": {"id": "GO:0009360", "label": "DNA polymerase III complex"},
        },
        "decisions": {
            "GO:0003677": ("KEEP_AS_NON_CORE", "DNA binding is accessory context"),
            "GO:0003887": ("MARK_AS_OVER_ANNOTATED", "DnaX contributes to polymerase complex function but is not the catalytic polymerase"),
            "GO:0005524": ("ACCEPT", "DnaX is an ATP-binding clamp-loader ATPase-family subunit"),
            "GO:0006260": ("ACCEPT", "DnaX is a core DNA replication clamp-loader subunit"),
            "GO:0006261": ("ACCEPT", "DNA-templated replication is appropriate process context"),
            "GO:0009360": ("ACCEPT", "DnaX is part of DNA polymerase III/clamp-loader machinery"),
            "GO:0034061": ("MARK_AS_OVER_ANNOTATED", "generic DNA polymerase activity is over-assigned to an accessory subunit"),
            "GO:0071897": ("KEEP_AS_NON_CORE", "DNA biosynthesis is a broad parent of DNA replication"),
        },
    },
    "ligA": {
        "symbol": "ligA",
        "description": (
            "ligA (PP_4274) encodes the essential NAD-dependent DNA ligase "
            "that seals DNA nicks during replication and repair by forming "
            "phosphodiester bonds in duplex DNA."
        ),
        "core": {
            "description": "NAD-dependent DNA ligase sealing DNA nicks during replication and repair.",
            "molecular_function": {"id": "GO:0003911", "label": "DNA ligase (NAD+) activity"},
            "directly_involved_in": [
                {"id": "GO:0006260", "label": "DNA replication"},
                {"id": "GO:0006281", "label": "DNA repair"},
            ],
            "locations": [{"id": "GO:0005829", "label": "cytosol"}],
        },
        "decisions": {
            "GO:0003677": ("KEEP_AS_NON_CORE", "DNA binding is expected for DNA ligase but not the catalytic activity"),
            "GO:0003911": ("ACCEPT", "NAD-dependent DNA ligase activity is the core molecular function"),
            "GO:0005829": ("KEEP_AS_NON_CORE", "cytosol is plausible but not pathway-defining"),
            "GO:0006259": ("KEEP_AS_NON_CORE", "DNA metabolic process is broad parent context"),
            "GO:0006260": ("ACCEPT", "LigA seals Okazaki-fragment and replication-associated DNA nicks"),
            "GO:0006281": ("ACCEPT", "DNA ligase participates in DNA repair nick sealing"),
        },
    },
    "PP_4768": {
        "symbol": "PP_4768",
        "description": (
            "PP_4768 encodes a predicted RNase H/DnaQ-like exonuclease in "
            "Pseudomonas putida KT2440. The current automated evidence supports "
            "3'-5' exonuclease activity and DNA replication proofreading context, "
            "but the exact physiological substrate remains unresolved."
        ),
        "core": {
            "description": "Predicted DnaQ/RNase H-like 3'-5' exonuclease with DNA replication proofreading context.",
            "molecular_function": {"id": "GO:0008408", "label": "3'-5' exonuclease activity"},
            "directly_involved_in": [{"id": "GO:0045004", "label": "DNA replication proofreading"}],
            "locations": [{"id": "GO:0005829", "label": "cytosol"}],
        },
        "decisions": {
            "GO:0003676": ("KEEP_AS_NON_CORE", "nucleic acid binding is generic for a nuclease-domain protein"),
            "GO:0004527": ("KEEP_AS_NON_CORE", "generic exonuclease activity is less specific than 3'-5' exonuclease activity"),
            "GO:0005829": ("KEEP_AS_NON_CORE", "cytosol is plausible but not pathway-defining"),
            "GO:0008408": ("ACCEPT", "DnaQ/RNase H-like domain and GOA support 3'-5' exonuclease activity"),
            "GO:0045004": ("ACCEPT", "GOA places this DnaQ-like exonuclease in DNA replication proofreading context"),
        },
    },
    "holA": {
        "symbol": "holA",
        "description": (
            "holA (PP_4796) encodes DNA polymerase III subunit delta, a "
            "clamp-loader component that helps load the beta sliding clamp "
            "during DNA replication."
        ),
        "core": {
            "description": "Delta clamp-loader subunit of DNA polymerase III supporting beta-clamp loading during DNA replication.",
            "contributes_to_molecular_function": {
                "id": "GO:0003887",
                "label": "DNA-directed DNA polymerase activity",
            },
            "directly_involved_in": [
                {"id": "GO:0006260", "label": "DNA replication"},
                {"id": "GO:0006261", "label": "DNA-templated DNA replication"},
            ],
            "in_complex": {"id": "GO:0009360", "label": "DNA polymerase III complex"},
        },
        "decisions": {
            "GO:0003677": ("KEEP_AS_NON_CORE", "DNA binding is accessory context"),
            "GO:0003887": ("MARK_AS_OVER_ANNOTATED", "HolA contributes to DNA polymerase III function but is not the catalytic polymerase"),
            "GO:0006260": ("ACCEPT", "HolA is a DNA replication clamp-loader subunit"),
            "GO:0006261": ("ACCEPT", "DNA-templated DNA replication is appropriate process context"),
            "GO:0009360": ("ACCEPT", "HolA is part of DNA polymerase III/clamp-loader machinery"),
            "GO:0071897": ("KEEP_AS_NON_CORE", "DNA biosynthesis is a broad parent of DNA replication"),
        },
    },
    "ligB": {
        "symbol": "ligB",
        "description": (
            "ligB (PP_4968) encodes NAD-dependent DNA ligase B, a bacterial "
            "DNA ligase paralog associated with DNA repair and nick sealing "
            "rather than the primary essential replication ligase role of LigA."
        ),
        "core": {
            "description": "NAD-dependent DNA ligase B supporting DNA repair-associated nick sealing.",
            "molecular_function": {"id": "GO:0003911", "label": "DNA ligase (NAD+) activity"},
            "directly_involved_in": [{"id": "GO:0006281", "label": "DNA repair"}],
        },
        "decisions": {
            "GO:0003911": ("ACCEPT", "NAD-dependent DNA ligase activity is the core molecular function"),
            "GO:0006259": ("KEEP_AS_NON_CORE", "DNA metabolic process is broad parent context"),
            "GO:0006260": ("KEEP_AS_NON_CORE", "replication context is plausible but LigB is better treated as a repair ligase paralog"),
            "GO:0006281": ("ACCEPT", "LigB fits DNA repair-associated nick sealing context"),
        },
    },
    "uvrD": {
        "symbol": "uvrD",
        "description": (
            "uvrD (PP_5352) encodes DNA helicase II, a UvrD-family 3'-to-5' "
            "ATP-dependent DNA helicase that unwinds DNA during nucleotide "
            "excision repair, mismatch repair, and recombination-associated "
            "DNA repair contexts."
        ),
        "core": {
            "description": "ATP-dependent 3'-5' DNA helicase acting in bacterial DNA repair pathways.",
            "molecular_function": {"id": "GO:0043138", "label": "3'-5' DNA helicase activity"},
            "directly_involved_in": [{"id": "GO:0000725", "label": "recombinational repair"}],
            "locations": [{"id": "GO:0005829", "label": "cytosol"}],
        },
        "decisions": {
            "GO:0000166": ("KEEP_AS_NON_CORE", "nucleotide binding is generic for an ATP-dependent helicase"),
            "GO:0000725": ("ACCEPT", "UvrD-family helicases function in DNA repair and recombination-associated repair contexts"),
            "GO:0003677": ("KEEP_AS_NON_CORE", "DNA binding is expected but generic"),
            "GO:0003678": ("ACCEPT", "DNA helicase activity is supported by the UvrD-family identity"),
            "GO:0004386": ("KEEP_AS_NON_CORE", "helicase activity is a broad parent of DNA helicase activity"),
            "GO:0005524": ("ACCEPT", "ATP binding is required for UvrD helicase activity"),
            "GO:0005829": ("KEEP_AS_NON_CORE", "cytosol is plausible but not pathway-defining"),
            "GO:0016787": ("MARK_AS_OVER_ANNOTATED", "generic hydrolase activity is uninformative for an ATP-dependent DNA helicase"),
            "GO:0016887": ("ACCEPT", "ATP hydrolysis powers UvrD helicase activity"),
            "GO:0033202": ("KEEP_AS_NON_CORE", "DNA helicase complex context is plausible but less informative than UvrD activity"),
            "GO:0042802": ("KEEP_AS_NON_CORE", "identical protein binding is not pathway-defining"),
            "GO:0043138": ("ACCEPT", "3'-5' DNA helicase activity is the most specific current molecular function"),
        },
    },
}


def support_for(term_id: str, label: str, gene: str) -> dict:
    return {
        "reference_id": f"file:{SPECIES}/{gene}/{gene}-goa.tsv",
        "supporting_text": f"{term_id}\t{label}",
    }


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
            "findings": [
                {
                    "statement": "UniProt identity and protein-name metadata used for first-pass pathway curation."
                }
            ],
        },
        {
            "id": f"file:{SPECIES}/{gene}/{gene}-goa.tsv",
            "title": f"QuickGO GOA annotations for {gene}",
            "findings": [
                {"statement": "GOA table containing the annotations reviewed in this file."}
            ],
        },
        {
            "id": f"file:{SPECIES}/{gene}/{gene}-deep-research-asta.md",
            "title": f"Asta retrieval report for {gene}",
            "findings": [
                {
                    "statement": "Asta retrieval used as fast gene-level literature context; no unsupported hypotheses were imported."
                }
            ],
        },
    ]:
        if ref["id"] not in seen:
            refs.append(ref)
            seen.add(ref["id"])
    return refs


def curated_review(gene: str, term_id: str, label: str, decision: tuple) -> dict:
    action, reason, *rest = decision
    if action == "ACCEPT":
        summary = f"{label} is supported for {gene} in the ppu03430 first-pass curation."
    elif action == "KEEP_AS_NON_CORE":
        summary = f"{label} is plausible for {gene} but is not the main pathway-defining function."
    elif action == "MARK_AS_OVER_ANNOTATED":
        summary = f"{label} is too broad or over-propagated for the main function of {gene}."
    elif action == "MODIFY":
        summary = f"{label} should be replaced by a more specific or biologically appropriate term for {gene}."
    else:
        summary = f"{label} was reviewed for {gene}."
    review = {
        "summary": summary,
        "action": action,
        "reason": reason,
        "supported_by": [support_for(term_id, label, gene)],
    }
    if rest:
        review["proposed_replacement_terms"] = rest[0]
    return review


def core_supported_by(core: dict, annotations: list[dict], gene: str) -> list[dict]:
    support: list[dict] = []
    term_index = {
        ann["term"]["id"]: ann["term"]["label"]
        for ann in annotations
        if ann.get("term", {}).get("id")
    }
    for slot in ("molecular_function", "contributes_to_molecular_function", "in_complex"):
        term = core.get(slot)
        if isinstance(term, dict) and term.get("id") in term_index:
            support.append(support_for(term["id"], term_index[term["id"]], gene))
    for slot in ("directly_involved_in", "locations"):
        for term in core.get(slot, []) or []:
            if term.get("id") in term_index:
                support.append(support_for(term["id"], term_index[term["id"]], gene))
    if support:
        return support
    return [
        {
            "reference_id": f"file:{SPECIES}/{gene}/{gene}-uniprot.txt",
            "supporting_text": "Reference proteome",
        }
    ]


def curate_gene(gene: str, spec: dict) -> None:
    path = ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    data["gene_symbol"] = spec["symbol"]
    data["status"] = "DRAFT"
    data["description"] = spec["description"]

    decisions = spec["decisions"]
    for ann in data.get("existing_annotations", []):
        term = ann["term"]
        decision = decisions.get(term["id"], ("KEEP_AS_NON_CORE", "not part of the primary ppu03430 first-pass interpretation"))
        ann["review"] = curated_review(gene, term["id"], term["label"], decision)

    core = dict(spec["core"])
    core["supported_by"] = core_supported_by(core, data.get("existing_annotations", []), gene)
    data["core_functions"] = [core]
    data["proposed_new_terms"] = []
    data["suggested_questions"] = [
        {
            "question": (
                f"What is the precise physiological contribution of {spec['symbol']} "
                "to mismatch repair versus neighboring replication, excision-repair, "
                "or recombination pathways in P. putida KT2440?"
            )
        }
    ]
    data["suggested_experiments"] = [
        {
            "description": (
                f"Measure mutation rate, mismatch-repair reporter activity, and DNA-damage "
                f"sensitivity in a targeted {spec['symbol']} perturbation under matched "
                "growth conditions."
            ),
            "experiment_type": "gene perturbation and DNA repair phenotype assay",
        }
    ]
    data["references"] = unique_references(data.get("references", []), gene)

    path.write_text(yaml.safe_dump(data, sort_keys=False, width=120), encoding="utf-8")


def add_asta_reference(gene: str) -> None:
    path = ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    data["references"] = unique_references(data.get("references", []), gene)
    path.write_text(yaml.safe_dump(data, sort_keys=False, width=120), encoding="utf-8")


def main() -> None:
    for gene, spec in GENES.items():
        curate_gene(gene, spec)
    for gene in ["mutS", "mutL"]:
        add_asta_reference(gene)


if __name__ == "__main__":
    main()
