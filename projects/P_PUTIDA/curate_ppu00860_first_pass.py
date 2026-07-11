#!/usr/bin/env python3
"""First-pass curation for the PSEPK ppu00860 porphyrin/tetrapyrrole batch."""

from __future__ import annotations

import csv
import re
from pathlib import Path

import yaml


BATCH = Path("projects/P_PUTIDA/batches/ppu00860_porphyrin_metabolism_boundary.tsv")


def term(go_id: str, label: str) -> dict[str, str]:
    return {"id": go_id, "label": label}


CONFIG: dict[str, dict] = {
    "hemF": {
        "description": "hemF encodes the oxygen-dependent coproporphyrinogen III oxidase of the heme/protoporphyrin IX biosynthetic pathway, oxidizing coproporphyrinogen III toward protoporphyrinogen IX under aerobic conditions.",
        "accept": {"GO:0004109", "GO:0006783"},
        "non_core": {"GO:0005737", "GO:0006779", "GO:0042803"},
        "core": [
            {
                "description": "Oxygen-dependent coproporphyrinogen III oxidation during heme biosynthesis.",
                "molecular_function": term("GO:0004109", "coproporphyrinogen oxidase activity"),
                "directly_involved_in": [term("GO:0006783", "heme biosynthetic process")],
            }
        ],
    },
    "hemC": {
        "description": "hemC encodes hydroxymethylbilane synthase/porphobilinogen deaminase, an early tetrapyrrole enzyme that polymerizes porphobilinogen to hydroxymethylbilane for heme and related porphyrin-containing cofactors.",
        "accept": {"GO:0004418", "GO:0006783"},
        "non_core": {"GO:0005737", "GO:0033014"},
        "core": [
            {
                "description": "Hydroxymethylbilane synthase activity in early heme/tetrapyrrole biosynthesis.",
                "molecular_function": term("GO:0004418", "hydroxymethylbilane synthase activity"),
                "directly_involved_in": [term("GO:0006783", "heme biosynthetic process")],
            }
        ],
    },
    "hemD": {
        "description": "hemD encodes uroporphyrinogen III synthase, converting hydroxymethylbilane to uroporphyrinogen III in the shared tetrapyrrole branch that supplies heme, siroheme, and corrinoid precursors.",
        "accept": {"GO:0004852", "GO:0006780"},
        "non_core": {"GO:0033014"},
        "core": [
            {
                "description": "Uroporphyrinogen III formation in the common tetrapyrrole biosynthetic pathway.",
                "molecular_function": term("GO:0004852", "uroporphyrinogen-III synthase activity"),
                "directly_involved_in": [term("GO:0006780", "uroporphyrinogen III biosynthetic process")],
            }
        ],
    },
    "PP_0188": {
        "description": "PP_0188 encodes a predicted HemX-family membrane protein annotated at the protein-name level as uroporphyrin-III C-methyltransferase, but the fetched GOA table currently has no GO annotations for this protein.",
        "core": [
            {
                "description": "Predicted HemX-family tetrapyrrole-associated membrane protein with unresolved catalytic role in this first-pass review.",
            }
        ],
        "questions": [
            "Is PP_0188 an active uroporphyrinogen/precorrin methyltransferase or a non-enzymatic HemX-family membrane factor in the PSEPK tetrapyrrole cluster?"
        ],
    },
    "PP_0431": {
        "description": "PP_0431 encodes a HemJ-family protoporphyrinogen IX oxidase, a membrane-associated late heme biosynthetic enzyme that oxidizes protoporphyrinogen IX.",
        "accept": {"GO:0070818"},
        "non_core": {"GO:0005886", "GO:0046872"},
        "core": [
            {
                "description": "Membrane-associated protoporphyrinogen IX oxidation in late heme biosynthesis.",
                "molecular_function": term("GO:0070818", "protoporphyrinogen oxidase activity"),
                "locations": [term("GO:0005886", "plasma membrane")],
            }
        ],
    },
    "bfr-I": {
        "description": "bfr-I encodes a bacterioferritin iron-storage protein with ferroxidase activity, heme cofactor binding, and a role in intracellular iron homeostasis rather than tetrapyrrole biosynthesis.",
        "accept": {"GO:0004322", "GO:0006879", "GO:0140315"},
        "non_core": {"GO:0005506", "GO:0005829", "GO:0006826", "GO:0008199", "GO:0020037"},
        "core": [
            {
                "description": "Bacterioferritin iron oxidation and sequestration for intracellular iron homeostasis.",
                "molecular_function": term("GO:0140315", "iron ion sequestering activity"),
                "directly_involved_in": [term("GO:0006879", "intracellular iron ion homeostasis")],
            }
        ],
    },
    "hemA": {
        "description": "hemA encodes glutamyl-tRNA reductase, the NADPH-dependent first enzyme of the C5 pathway to 5-aminolevulinate for bacterial tetrapyrrole and heme biosynthesis.",
        "accept": {"GO:0008883", "GO:0033014"},
        "non_core": {"GO:0050661"},
        "core": [
            {
                "description": "Glutamyl-tRNA reduction to glutamate-1-semialdehyde in 5-aminolevulinate/tetrapyrrole biosynthesis.",
                "molecular_function": term("GO:0008883", "glutamyl-tRNA reductase activity"),
                "directly_involved_in": [term("GO:0033014", "tetrapyrrole biosynthetic process")],
            }
        ],
    },
    "hemH": {
        "description": "hemH encodes ferrochelatase, the late heme biosynthetic enzyme that inserts ferrous iron into protoporphyrin IX to form protoheme.",
        "accept": {"GO:0004325", "GO:0006783"},
        "non_core": {"GO:0005737", "GO:0006779"},
        "core": [
            {
                "description": "Insertion of ferrous iron into protoporphyrin IX during heme biosynthesis.",
                "molecular_function": term("GO:0004325", "protoporphyrin ferrochelatase activity"),
                "directly_involved_in": [term("GO:0006783", "heme biosynthetic process")],
            }
        ],
    },
    "hemO": {
        "description": "hemO encodes a heme oxygenase that oxidatively cleaves heme, placing it in heme degradation or heme-iron utilization rather than heme biosynthesis.",
        "accept": {"GO:0004392", "GO:0006788"},
        "core": [
            {
                "description": "Heme oxygenase activity for oxidative heme cleavage.",
                "molecular_function": term("GO:0004392", "heme oxygenase (decyclizing) activity"),
                "directly_involved_in": [term("GO:0006788", "heme oxidation")],
            }
        ],
    },
    "bfr-II": {
        "description": "bfr-II encodes a second bacterioferritin iron-storage protein with ferroxidase activity and heme cofactor context, supporting iron homeostasis rather than committed porphyrin synthesis.",
        "accept": {"GO:0004322", "GO:0006879", "GO:0140315"},
        "non_core": {"GO:0005506", "GO:0005829", "GO:0006826", "GO:0008199", "GO:0020037"},
        "core": [
            {
                "description": "Bacterioferritin iron oxidation and sequestration for intracellular iron homeostasis.",
                "molecular_function": term("GO:0140315", "iron ion sequestering activity"),
                "directly_involved_in": [term("GO:0006879", "intracellular iron ion homeostasis")],
            }
        ],
    },
    "pduO": {
        "description": "pduO encodes a corrinoid adenosyltransferase that adenosylates cobinamide/cobalamin-family corrinoids for cobalamin metabolism and biosynthesis.",
        "accept": {"GO:0008817", "GO:0009235", "GO:0009236"},
        "non_core": {"GO:0005524", "GO:0016765"},
        "core": [
            {
                "description": "Corrinoid adenosyltransferase activity in cobalamin/cobamide metabolism.",
                "molecular_function": term("GO:0008817", "corrinoid adenosyltransferase activity"),
                "directly_involved_in": [term("GO:0009236", "cobalamin biosynthetic process")],
            }
        ],
    },
    "PP_1358": {
        "description": "PP_1358 encodes a predicted heme iron utilization/HugZ-like protein with cytoplasmic annotation and heme-utilization domain context, but its exact enzymatic role remains unresolved in this first-pass review.",
        "non_core": {"GO:0005737"},
        "core": [
            {
                "description": "Predicted heme iron utilization protein; exact molecular activity remains unresolved.",
            }
        ],
        "questions": [
            "Does PP_1358 function as a heme oxygenase-like heme iron utilization enzyme in PSEPK, and what substrate/product should be captured by GO?"
        ],
    },
    "cobO": {
        "description": "cobO encodes a corrinoid adenosyltransferase in adenosylcobalamin biosynthesis, adenosylating incomplete and complete corrinoid intermediates.",
        "accept": {"GO:0008817", "GO:0009236"},
        "non_core": {"GO:0005524", "GO:0005737"},
        "over": {"GO:0006779"},
        "core": [
            {
                "description": "Corrinoid adenosyltransferase activity in adenosylcobalamin biosynthesis.",
                "molecular_function": term("GO:0008817", "corrinoid adenosyltransferase activity"),
                "directly_involved_in": [term("GO:0009236", "cobalamin biosynthetic process")],
            }
        ],
    },
    "cobB__Q88MA1": {
        "description": "cobB__Q88MA1 encodes hydrogenobyrinate a,c-diamide synthase, a glutamine amidotransferase/ATP-dependent enzyme in corrinoid ring amidation during cobalamin biosynthesis.",
        "accept": {"GO:0009236", "GO:0042242", "GO:0043802"},
        "non_core": {"GO:0005524", "GO:0006541"},
        "over": {"GO:0003824"},
        "core": [
            {
                "description": "ATP-dependent hydrogenobyrinate a,c-diamide synthesis in cobalamin biosynthesis.",
                "molecular_function": term("GO:0043802", "hydrogenobyrinic acid a,c-diamide synthase (glutamine-hydrolysing) activity"),
                "directly_involved_in": [term("GO:0009236", "cobalamin biosynthetic process")],
            }
        ],
    },
    "cobD": {
        "description": "cobD encodes a CobD/CbiB-family cobalamin biosynthesis protein in the aminopropanol/lower-side-chain branch of cobamide assembly.",
        "accept": {"GO:0009236", "GO:0048472"},
        "non_core": {"GO:0005886", "GO:0016020"},
        "remove": {"GO:0015420", "GO:0015889"},
        "core": [
            {
                "description": "CobD-family cobalamin biosynthesis protein with threonine-phosphate decarboxylase-associated annotation.",
                "molecular_function": term("GO:0048472", "threonine-phosphate decarboxylase activity"),
                "directly_involved_in": [term("GO:0009236", "cobalamin biosynthetic process")],
            }
        ],
    },
    "cobC": {
        "description": "cobC encodes threonine-phosphate decarboxylase, a PLP-dependent aminopropanol-branch enzyme supporting cobalamin biosynthesis.",
        "accept": {"GO:0009236", "GO:0048472"},
        "non_core": {"GO:0030170"},
        "over": {"GO:0003824"},
        "core": [
            {
                "description": "Threonine-phosphate decarboxylase activity in cobalamin biosynthesis.",
                "molecular_function": term("GO:0048472", "threonine-phosphate decarboxylase activity"),
                "directly_involved_in": [term("GO:0009236", "cobalamin biosynthetic process")],
            }
        ],
    },
    "cobQ": {
        "description": "cobQ encodes cobyric acid synthase, a CobQ-family amidation enzyme in cobalamin biosynthesis; the current GOA process is useful but lacks a specific molecular-function term for the synthase activity.",
        "accept": {"GO:0009236"},
        "over": {"GO:0003824"},
        "remove": {"GO:0015420", "GO:0015889"},
        "core": [
            {
                "description": "Cobyric acid synthase/amidation step in cobalamin biosynthesis.",
                "directly_involved_in": [term("GO:0009236", "cobalamin biosynthetic process")],
            }
        ],
        "questions": [
            "Is there a current specific GO molecular-function term for CobQ/cobyric acid synthase activity that should replace generic catalytic activity?"
        ],
    },
    "cobP": {
        "description": "cobP encodes a bifunctional adenosylcobalamin biosynthesis enzyme with adenosylcobinamide kinase and cobinamide phosphate guanylyltransferase activities.",
        "accept": {"GO:0008820", "GO:0009236", "GO:0043752"},
        "non_core": {"GO:0000166", "GO:0005524", "GO:0005525"},
        "core": [
            {
                "description": "Adenosylcobinamide kinase activity in nucleotide-loop assembly for cobalamin biosynthesis.",
                "molecular_function": term("GO:0043752", "adenosylcobinamide kinase activity"),
                "directly_involved_in": [term("GO:0009236", "cobalamin biosynthetic process")],
            },
            {
                "description": "Cobinamide phosphate guanylyltransferase activity in cobalamin biosynthesis.",
                "molecular_function": term("GO:0008820", "cobinamide phosphate guanylyltransferase activity"),
                "directly_involved_in": [term("GO:0009236", "cobalamin biosynthetic process")],
            },
        ],
    },
    "PP_1680": {
        "description": "PP_1680 encodes an alpha-ribazole-5'-phosphate phosphatase, a lower-ligand processing enzyme for cobalamin nucleotide-loop assembly.",
        "accept": {"GO:0043755"},
        "non_core": {"GO:0005737"},
        "modify": {"GO:0016791": term("GO:0043755", "alpha-ribazole phosphatase activity")},
        "core": [
            {
                "description": "Alpha-ribazole phosphate dephosphorylation in cobalamin lower-ligand assembly.",
                "molecular_function": term("GO:0043755", "alpha-ribazole phosphatase activity"),
            }
        ],
    },
    "cobS": {
        "description": "cobS encodes adenosylcobinamide-GDP ribazoletransferase/cobalamin 5'-phosphate synthase, a membrane-associated enzyme that attaches the nucleotide-loop lower ligand during cobalamin biosynthesis.",
        "accept": {"GO:0008818", "GO:0009236", "GO:0051073"},
        "non_core": {"GO:0005886"},
        "core": [
            {
                "description": "Adenosylcobinamide-GDP ribazoletransferase activity in cobalamin nucleotide-loop assembly.",
                "molecular_function": term("GO:0051073", "adenosylcobinamide-GDP ribazoletransferase activity"),
                "directly_involved_in": [term("GO:0009236", "cobalamin biosynthetic process")],
                "locations": [term("GO:0005886", "plasma membrane")],
            }
        ],
    },
    "gltX": {
        "description": "gltX encodes glutamate--tRNA ligase, a translation enzyme that also supplies glutamyl-tRNA for HemA in C5-pathway tetrapyrrole precursor formation.",
        "accept": {"GO:0004818", "GO:0006418", "GO:0006424"},
        "non_core": {"GO:0000049", "GO:0000166", "GO:0005524", "GO:0005737", "GO:0005829", "GO:0008270", "GO:0043039"},
        "modify": {"GO:0004812": term("GO:0004818", "glutamate-tRNA ligase activity")},
        "core": [
            {
                "description": "Glutamate charging of tRNA(Glu) for protein translation and tetrapyrrole precursor supply.",
                "molecular_function": term("GO:0004818", "glutamate-tRNA ligase activity"),
                "directly_involved_in": [term("GO:0006424", "glutamyl-tRNA aminoacylation")],
            }
        ],
    },
    "cobA": {
        "description": "cobA encodes uroporphyrinogen III C-methyltransferase, producing precorrin-2/siroheme-branch intermediates at the branch point from uroporphyrinogen III.",
        "accept": {"GO:0004851", "GO:0019354"},
        "over": {"GO:0008168"},
        "core": [
            {
                "description": "Uroporphyrinogen III C-methylation at the siroheme/corrinoid branch point.",
                "molecular_function": term("GO:0004851", "uroporphyrin-III C-methyltransferase activity"),
                "directly_involved_in": [term("GO:0019354", "siroheme biosynthetic process")],
            }
        ],
    },
    "PP_2582": {
        "description": "PP_2582 encodes a second predicted heme oxygenase, supporting heme oxidation/heme-utilization chemistry rather than de novo porphyrin synthesis.",
        "accept": {"GO:0004392", "GO:0006788"},
        "core": [
            {
                "description": "Heme oxygenase activity for oxidative heme cleavage.",
                "molecular_function": term("GO:0004392", "heme oxygenase (decyclizing) activity"),
                "directly_involved_in": [term("GO:0006788", "heme oxidation")],
            }
        ],
    },
    "hemB": {
        "description": "hemB encodes porphobilinogen synthase/delta-aminolevulinic acid dehydratase, condensing 5-aminolevulinate to porphobilinogen in heme/tetrapyrrole biosynthesis.",
        "accept": {"GO:0004655", "GO:0006783"},
        "non_core": {"GO:0005829", "GO:0006779", "GO:0008270", "GO:0033014", "GO:0046872"},
        "core": [
            {
                "description": "Porphobilinogen synthesis from 5-aminolevulinate in heme biosynthesis.",
                "molecular_function": term("GO:0004655", "porphobilinogen synthase activity"),
                "directly_involved_in": [term("GO:0006783", "heme biosynthetic process")],
            }
        ],
    },
    "hemBB": {
        "description": "hemBB encodes a second porphobilinogen synthase/delta-aminolevulinic acid dehydratase paralog contributing to tetrapyrrole precursor formation.",
        "accept": {"GO:0004655", "GO:0006783"},
        "non_core": {"GO:0005829", "GO:0006779", "GO:0008270", "GO:0033014", "GO:0046872"},
        "core": [
            {
                "description": "Porphobilinogen synthesis from 5-aminolevulinate in heme/tetrapyrrole biosynthesis.",
                "molecular_function": term("GO:0004655", "porphobilinogen synthase activity"),
                "directly_involved_in": [term("GO:0006783", "heme biosynthetic process")],
            }
        ],
    },
    "PP_3409": {
        "description": "PP_3409 encodes a CobE/CbiG-family cobalamin biosynthesis protein in the corrinoid branch of the tetrapyrrole pathway.",
        "accept": {"GO:0009236"},
        "core": [
            {
                "description": "CobE/CbiG-family cobalamin biosynthesis protein with unresolved exact molecular activity.",
                "directly_involved_in": [term("GO:0009236", "cobalamin biosynthetic process")],
            }
        ],
        "questions": [
            "What exact molecular activity should be assigned to the PP_3409 CobE/CbiG-family cobalamin biosynthesis protein?"
        ],
    },
    "cobM": {
        "description": "cobM encodes precorrin-4 C11-methyltransferase, a SAM-dependent methyltransferase in corrinoid ring construction for cobalamin biosynthesis.",
        "accept": {"GO:0009236", "GO:0046026"},
        "over": {"GO:0008168"},
        "core": [
            {
                "description": "Precorrin-4 C11 methylation during cobalamin biosynthesis.",
                "molecular_function": term("GO:0046026", "precorrin-4 C11-methyltransferase activity"),
                "directly_involved_in": [term("GO:0009236", "cobalamin biosynthetic process")],
            }
        ],
    },
    "PP_3506": {
        "description": "PP_3506 encodes a ChlI/MoxR-like AAA ATPase annotated as a magnesium-chelatase-like subunit, likely representing a chelatase ATPase accessory component near cobN in the cobalamin branch.",
        "accept": {"GO:0016887"},
        "non_core": {"GO:0005524"},
        "core": [
            {
                "description": "Chelatase-associated AAA ATPase activity in the cobalamin/corrinoid gene neighborhood.",
                "molecular_function": term("GO:0016887", "ATP hydrolysis activity"),
            }
        ],
        "questions": [
            "Should PP_3506 be curated as a cobaltochelatase ATPase/accessory subunit rather than a magnesium-chelatase chlorophyll-pathway protein?"
        ],
    },
    "cobN": {
        "description": "cobN encodes the CobN cobaltochelatase subunit, inserting cobalt into the corrin precursor during aerobic cobalamin biosynthesis.",
        "accept": {"GO:0009236", "GO:0051116"},
        "core": [
            {
                "description": "Cobalt chelation of corrinoid precursors in cobalamin biosynthesis.",
                "molecular_function": term("GO:0051116", "cobaltochelatase activity"),
                "directly_involved_in": [term("GO:0009236", "cobalamin biosynthetic process")],
            }
        ],
    },
    "PP_3763": {
        "description": "PP_3763 encodes a CobF-family precorrin methyltransferase/deacetylating enzyme in the corrinoid branch of cobalamin biosynthesis.",
        "accept": {"GO:0009236", "GO:0043819"},
        "over": {"GO:0008168"},
        "core": [
            {
                "description": "Precorrin-6A synthase/deacetylating activity in cobalamin biosynthesis.",
                "molecular_function": term("GO:0043819", "precorrin-6A synthase (deacetylating) activity"),
                "directly_involved_in": [term("GO:0009236", "cobalamin biosynthetic process")],
            }
        ],
    },
    "cysG": {
        "description": "cysG encodes multifunctional siroheme synthase, combining uroporphyrinogen III methyltransferase, precorrin-2 dehydrogenase, and sirohydrochlorin ferrochelatase activities for siroheme biosynthesis.",
        "accept": {"GO:0004851", "GO:0006779", "GO:0019354", "GO:0043115", "GO:0051266"},
        "non_core": {"GO:0051287"},
        "over": {"GO:0008168", "GO:0009236"},
        "modify": {"GO:0004325": term("GO:0051266", "sirohydrochlorin ferrochelatase activity")},
        "core": [
            {
                "description": "Uroporphyrinogen III methylation to precorrin-2 in siroheme biosynthesis.",
                "molecular_function": term("GO:0004851", "uroporphyrin-III C-methyltransferase activity"),
                "directly_involved_in": [term("GO:0019354", "siroheme biosynthetic process")],
            },
            {
                "description": "Precorrin-2 dehydrogenase step of siroheme biosynthesis.",
                "molecular_function": term("GO:0043115", "precorrin-2 dehydrogenase activity"),
                "directly_involved_in": [term("GO:0019354", "siroheme biosynthetic process")],
            },
            {
                "description": "Sirohydrochlorin ferrochelatase activity completing siroheme biosynthesis.",
                "molecular_function": term("GO:0051266", "sirohydrochlorin ferrochelatase activity"),
                "directly_involved_in": [term("GO:0019354", "siroheme biosynthetic process")],
            },
        ],
    },
    "hemN": {
        "description": "hemN encodes the oxygen-independent radical-SAM coproporphyrinogen III oxidase/dehydrogenase used for heme biosynthesis under low-oxygen conditions.",
        "accept": {"GO:0006779", "GO:0051989"},
        "non_core": {"GO:0005737", "GO:0046872", "GO:0051536", "GO:0051539"},
        "over": {"GO:0003824"},
        "modify": {"GO:0004109": term("GO:0051989", "coproporphyrinogen dehydrogenase activity")},
        "core": [
            {
                "description": "Oxygen-independent coproporphyrinogen III dehydrogenase activity in heme/tetrapyrrole biosynthesis.",
                "molecular_function": term("GO:0051989", "coproporphyrinogen dehydrogenase activity"),
                "directly_involved_in": [term("GO:0006779", "porphyrin-containing compound biosynthetic process")],
            }
        ],
    },
    "hemL": {
        "description": "hemL encodes glutamate-1-semialdehyde 2,1-aminomutase, the PLP-dependent second enzyme of the bacterial C5 pathway to 5-aminolevulinate.",
        "accept": {"GO:0033014", "GO:0042286"},
        "non_core": {"GO:0005737", "GO:0030170"},
        "core": [
            {
                "description": "Glutamate-1-semialdehyde aminomutase activity in 5-aminolevulinate/tetrapyrrole biosynthesis.",
                "molecular_function": term("GO:0042286", "glutamate-1-semialdehyde 2,1-aminomutase activity"),
                "directly_involved_in": [term("GO:0033014", "tetrapyrrole biosynthetic process")],
            }
        ],
    },
    "cobJ": {
        "description": "cobJ encodes a precorrin-3B C17 methyltransferase-family enzyme in the corrinoid ring-construction branch of cobalamin biosynthesis.",
        "accept": {"GO:0009236"},
        "over": {"GO:0008168"},
        "core": [
            {
                "description": "Precorrin-3B C17 methyltransferase-family step in cobalamin biosynthesis; GOA currently lacks a specific MF term.",
                "directly_involved_in": [term("GO:0009236", "cobalamin biosynthetic process")],
            }
        ],
        "questions": [
            "Is there a current specific GO term for CobJ precorrin-3B C17-methyltransferase activity?"
        ],
    },
    "cobI": {
        "description": "cobI encodes precorrin-2 C20-methyltransferase, a SAM-dependent methyltransferase step in cobalamin biosynthesis.",
        "accept": {"GO:0009236", "GO:0030788"},
        "non_core": {"GO:0008757"},
        "over": {"GO:0008168"},
        "core": [
            {
                "description": "Precorrin-2 C20 methylation during cobalamin biosynthesis.",
                "molecular_function": term("GO:0030788", "precorrin-2 C20-methyltransferase activity"),
                "directly_involved_in": [term("GO:0009236", "cobalamin biosynthetic process")],
            }
        ],
    },
    "cobH": {
        "description": "cobH encodes precorrin-8X methylmutase, rearranging late corrinoid intermediates during cobalamin biosynthesis.",
        "accept": {"GO:0009236", "GO:0016993"},
        "core": [
            {
                "description": "Precorrin-8X methylmutase activity in cobalamin biosynthesis.",
                "molecular_function": term("GO:0016993", "precorrin-8X methylmutase activity"),
                "directly_involved_in": [term("GO:0009236", "cobalamin biosynthetic process")],
            }
        ],
    },
    "cobG": {
        "description": "cobG encodes precorrin-3B synthase, an iron-sulfur/heme-associated oxidase-like enzyme in aerobic cobalamin corrin-ring biosynthesis.",
        "accept": {"GO:0043818"},
        "non_core": {"GO:0016491", "GO:0020037", "GO:0051536"},
        "core": [
            {
                "description": "Precorrin-3B synthase activity in aerobic cobalamin biosynthesis.",
                "molecular_function": term("GO:0043818", "precorrin-3B synthase activity"),
            }
        ],
    },
    "cobL": {
        "description": "cobL encodes precorrin-6Y C5,15-methyltransferase, a decarboxylating methyltransferase step in cobalamin biosynthesis.",
        "accept": {"GO:0009236", "GO:0046025"},
        "over": {"GO:0008168"},
        "remove": {"GO:0008276"},
        "core": [
            {
                "description": "Precorrin-6Y C5,15 methylation/decarboxylation in cobalamin biosynthesis.",
                "molecular_function": term("GO:0046025", "precorrin-6Y C5,15-methyltransferase (decarboxylating) activity"),
                "directly_involved_in": [term("GO:0009236", "cobalamin biosynthetic process")],
            }
        ],
    },
    "cbiD": {
        "description": "cbiD encodes cobalt-precorrin-5B C1-methyltransferase/cobalt-precorrin-6A synthase, a corrinoid methylation step in cobalamin biosynthesis.",
        "accept": {"GO:0009236", "GO:0043780"},
        "over": {"GO:0008168"},
        "core": [
            {
                "description": "Cobalt-precorrin-5B C1 methylation during cobalamin biosynthesis.",
                "molecular_function": term("GO:0043780", "cobalt-precorrin-5B C1-methyltransferase activity"),
                "directly_involved_in": [term("GO:0009236", "cobalamin biosynthetic process")],
            }
        ],
    },
    "cobK": {
        "description": "cobK encodes precorrin-6x reductase, an oxidoreductase step in corrinoid ring modification during cobalamin biosynthesis.",
        "accept": {"GO:0009236", "GO:0016994"},
        "over": {"GO:0016491"},
        "remove": {"GO:0003690", "GO:0006265"},
        "core": [
            {
                "description": "Precorrin-6A/6x reductase activity in cobalamin biosynthesis.",
                "molecular_function": term("GO:0016994", "precorrin-6A reductase activity"),
                "directly_involved_in": [term("GO:0009236", "cobalamin biosynthetic process")],
            }
        ],
    },
    "PP_4856": {
        "description": "PP_4856 encodes a bacterioferritin-family ferroxidase/Dps-like iron-storage protein, supporting iron homeostasis rather than tetrapyrrole biosynthesis.",
        "accept": {"GO:0004322", "GO:0006879"},
        "non_core": {"GO:0005506", "GO:0005829", "GO:0006826", "GO:0008199", "GO:0020037"},
        "core": [
            {
                "description": "Bacterioferritin-family ferroxidase activity contributing to intracellular iron homeostasis.",
                "molecular_function": term("GO:0004322", "ferroxidase activity"),
                "directly_involved_in": [term("GO:0006879", "intracellular iron ion homeostasis")],
            }
        ],
    },
    "hemE": {
        "description": "hemE encodes uroporphyrinogen decarboxylase, converting uroporphyrinogen III toward coproporphyrinogen III in heme/tetrapyrrole biosynthesis.",
        "accept": {"GO:0004853", "GO:0006783"},
        "non_core": {"GO:0005737", "GO:0005829", "GO:0006778", "GO:0006779"},
        "core": [
            {
                "description": "Uroporphyrinogen decarboxylation in heme biosynthesis.",
                "molecular_function": term("GO:0004853", "uroporphyrinogen decarboxylase activity"),
                "directly_involved_in": [term("GO:0006783", "heme biosynthetic process")],
            }
        ],
    },
}


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def file_title(kind: str, gene: str) -> str:
    if kind == "uniprot":
        return f"UniProt entry for {gene}"
    if kind == "goa":
        return f"QuickGO GOA annotations for {gene}"
    if kind == "asta":
        return f"Asta retrieval report for {gene}"
    raise ValueError(kind)


def uniprot_snippet(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    for line in text.splitlines():
        if "Full=" in line:
            snippet = line.split("Full=", 1)[1].split("{", 1)[0].strip().rstrip(";")
            return f"Full={snippet}"
    match = re.search(r"AC\s+([A-Z0-9]+);", text)
    if match:
        return f"AC   {match.group(1)};"
    return text.splitlines()[0]


def goa_snippet(annotation: dict[str, str]) -> str:
    return f"{annotation['GO TERM']}\t{annotation['GO NAME']}"


def ensure_file_references(data: dict, gene: str, accession: str, gene_dir: Path) -> None:
    references = list(data.get("references") or [])
    by_id = {ref.get("id"): ref for ref in references}
    additions: list[dict] = []

    uniprot = gene_dir / f"{gene}-uniprot.txt"
    if uniprot.exists():
        ref_id = f"file:PSEPK/{gene}/{gene}-uniprot.txt"
        if ref_id not in by_id:
            additions.append(
                {
                    "id": ref_id,
                    "title": file_title("uniprot", gene),
                    "findings": [
                        {
                            "statement": "UniProt provides the protein identity and first-pass functional context used for this review.",
                            "supporting_text": uniprot_snippet(uniprot),
                        }
                    ],
                }
            )

    goa = gene_dir / f"{gene}-goa.tsv"
    if goa.exists():
        ref_id = f"file:PSEPK/{gene}/{gene}-goa.tsv"
        if ref_id not in by_id:
            additions.append(
                {
                    "id": ref_id,
                    "title": file_title("goa", gene),
                    "findings": [
                        {
                            "statement": "The fetched GOA table contains the annotations reviewed for this gene.",
                        }
                    ],
                }
            )

    asta = gene_dir / f"{gene}-deep-research-asta.md"
    if asta.exists():
        ref_id = f"file:PSEPK/{gene}/{gene}-deep-research-asta.md"
        if ref_id not in by_id:
            additions.append(
                {
                    "id": ref_id,
                    "title": file_title("asta", gene),
                    "findings": [
                        {
                            "statement": "Asta retrieval was generated for this first-pass review and used as lightweight identity/literature context.",
                            "supporting_text": f"uniprot_accession: {accession}",
                        }
                    ],
                }
            )

    data["references"] = references + additions


def action_label(action: str) -> str:
    return {
        "ACCEPT": "Accepted",
        "KEEP_AS_NON_CORE": "Retained as non-core",
        "MARK_AS_OVER_ANNOTATED": "Marked as over-annotated",
        "MODIFY": "Modified",
        "REMOVE": "Removed",
    }[action]


def classify(gene: str, annotation: dict[str, str], cfg: dict) -> tuple[str, dict | None]:
    go_id = annotation["GO TERM"]
    if go_id in cfg.get("accept", set()):
        return "ACCEPT", None
    if go_id in cfg.get("non_core", set()):
        return "KEEP_AS_NON_CORE", None
    if go_id in cfg.get("over", set()):
        return "MARK_AS_OVER_ANNOTATED", None
    if go_id in cfg.get("remove", set()):
        return "REMOVE", None
    if go_id in cfg.get("modify", {}):
        return "MODIFY", cfg["modify"][go_id]
    if annotation["GO ASPECT"] == "cellular_component":
        return "KEEP_AS_NON_CORE", None
    if "binding" in annotation["GO NAME"]:
        return "KEEP_AS_NON_CORE", None
    if annotation["GO NAME"] in {
        "catalytic activity",
        "methyltransferase activity",
        "oxidoreductase activity",
        "transferase activity, transferring alkyl or aryl (other than methyl) groups",
        "phosphatase activity",
    }:
        return "MARK_AS_OVER_ANNOTATED", None
    return "KEEP_AS_NON_CORE", None


def reason_for(action: str, annotation: dict[str, str], cfg: dict, replacement: dict | None) -> str:
    label = annotation["GO NAME"]
    if action == "ACCEPT":
        return (
            f"{label} matches the fetched GOA/UniProt identity for this ppu00860 first-pass review "
            "and is consistent with the pathway role recorded for this gene."
        )
    if action == "KEEP_AS_NON_CORE":
        return (
            f"{label} is plausible context for this protein, but it is a location, cofactor, "
            "binding, structural, or broader side-process annotation rather than the most informative core activity."
        )
    if action == "MARK_AS_OVER_ANNOTATED":
        return (
            f"{label} is not necessarily false, but it is broader than the specific enzyme or pathway "
            "assignment supported by UniProt/GOA in this batch."
        )
    if action == "MODIFY" and replacement:
        return (
            f"The annotation captures the right general area but should be represented by the more specific "
            f"{replacement['label']} term for this protein."
        )
    if action == "REMOVE":
        if label in {"ABC-type vitamin B12 transporter activity", "cobalamin transport"}:
            return (
                "This transporter annotation appears to be an electronic over-propagation onto a biosynthetic "
                "Cob enzyme; the fetched UniProt/GOA identity supports cobalamin biosynthesis rather than transport."
            )
        if label in {"double-stranded DNA binding", "DNA topological change"}:
            return (
                "This DNA-related annotation is inconsistent with the CobK precorrin reductase identity and is "
                "likely a domain/family electronic over-propagation."
            )
        if label == "protein methyltransferase activity":
            return (
                "CobL is a small-molecule precorrin methyltransferase, not a protein methyltransferase; the "
                "protein-substrate parent term should not be retained."
            )
        return "This annotation is inconsistent with the fetched protein identity and pathway context."
    raise AssertionError(action)


def review_annotation(
    gene: str,
    annotation: dict,
    goa_by_id_label: dict[tuple[str, str], dict[str, str]],
    cfg: dict,
) -> None:
    term_data = annotation["term"]
    go_id = term_data["id"]
    label = term_data["label"]
    goa_row = goa_by_id_label.get((go_id, label))
    if goa_row is None:
        # Fallback for duplicate/label drift; GOA ids are trusted from the fetched table.
        goa_row = next((row for (gid, _), row in goa_by_id_label.items() if gid == go_id), None)
    action, replacement = classify(gene, goa_row or {"GO TERM": go_id, "GO NAME": label, "GO ASPECT": ""}, cfg)
    review = {
        "summary": f"{action_label(action)}: {label} for {gene} in the ppu00860 porphyrin/tetrapyrrole first-pass review.",
        "action": action,
        "reason": reason_for(action, goa_row or {"GO NAME": label}, cfg, replacement),
    }
    if replacement is not None:
        review["proposed_replacement_terms"] = [replacement]
    if goa_row is not None:
        review["supported_by"] = [
            {
                "reference_id": f"file:PSEPK/{gene}/{gene}-goa.tsv",
                "supporting_text": goa_snippet(goa_row),
            }
        ]
    annotation["review"] = review


def support_for_core(gene: str, core: dict, goa_rows: list[dict[str, str]], uniprot: Path) -> list[dict[str, str]]:
    support: list[dict[str, str]] = []
    term_ids: set[str] = set()
    for slot in ("molecular_function", "contributes_to_molecular_function"):
        if slot in core:
            term_ids.add(core[slot]["id"])
    for item in core.get("directly_involved_in", []) or []:
        term_ids.add(item["id"])
    for item in core.get("locations", []) or []:
        term_ids.add(item["id"])
    for row in goa_rows:
        if row["GO TERM"] in term_ids:
            support.append(
                {
                    "reference_id": f"file:PSEPK/{gene}/{gene}-goa.tsv",
                    "supporting_text": goa_snippet(row),
                }
            )
    if uniprot.exists():
        support.append(
            {
                "reference_id": f"file:PSEPK/{gene}/{gene}-uniprot.txt",
                "supporting_text": uniprot_snippet(uniprot),
            }
        )
    return support


def suggested_questions(cfg: dict) -> list[dict[str, str]]:
    return [{"question": question} for question in cfg.get("questions", [])]


def curate(row: dict[str, str]) -> None:
    gene = row["suggested_review_name"]
    if gene not in CONFIG:
        return
    cfg = CONFIG[gene]
    review_path = Path(row["review_file"])
    gene_dir = review_path.parent
    goa_path = gene_dir / f"{gene}-goa.tsv"
    uniprot_path = gene_dir / f"{gene}-uniprot.txt"
    data = yaml.safe_load(review_path.read_text(encoding="utf-8")) or {}
    goa_rows = read_tsv(goa_path) if goa_path.exists() else []
    goa_by_id_label = {(row["GO TERM"], row["GO NAME"]): row for row in goa_rows}

    data["gene_symbol"] = gene
    data["status"] = "DRAFT"
    data["description"] = cfg["description"]
    ensure_file_references(data, gene, row["uniprot_accession"], gene_dir)

    for annotation in data.get("existing_annotations") or []:
        review_annotation(gene, annotation, goa_by_id_label, cfg)

    core_functions: list[dict] = []
    for core in cfg.get("core", []):
        core_entry = dict(core)
        core_entry["supported_by"] = support_for_core(gene, core_entry, goa_rows, uniprot_path)
        core_functions.append(core_entry)
    data["core_functions"] = core_functions
    data["proposed_new_terms"] = []
    data["suggested_questions"] = suggested_questions(cfg)
    data["suggested_experiments"] = []

    review_path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=False), encoding="utf-8")


def main() -> None:
    rows = read_tsv(BATCH)
    for row in rows:
        curate(row)


if __name__ == "__main__":
    main()
