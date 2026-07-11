#!/usr/bin/env python3
"""First-pass curation for tRNA modification, editing, and processing genes."""

from __future__ import annotations

import re
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes" / "PSEPK"
MODULE_PATH = ROOT / "modules" / "trna_modification_processing_boundary.yaml"
BATCH_TSV = "projects/P_PUTIDA/batches/module_translation_rna_processing_trna_modification_processing.tsv"
PRESERVE_EXISTING_REVIEWS = {"cca"}


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):  # type: ignore[override]
        return True


def term(go_id: str, label: str) -> dict[str, str]:
    return {"id": go_id, "label": label}


GENES = [
    "mnmG",
    "mnmE",
    "tsaC",
    "tsaD",
    "cca",
    "cmoM",
    "selU",
    "trmJ",
    "tadA",
    "cmoB",
    "trmD",
    "tsaB",
    "tilS",
    "truD",
    "yfiP",
    "ttcA",
    "rluA",
    "mnmC",
    "trhO",
    "dusC",
    "truA",
    "dusA",
    "trmK",
    "PP_4520",
    "trmA",
    "truB",
    "dusB",
    "miaA",
    "tsaE",
    "trmL",
]


SPEC = {
    "mnmG": {
        "description": "mnmG encodes the conserved MnmG/GidA flavoprotein component of the MnmEG tRNA wobble-uridine modification system, which helps install the carboxymethylaminomethyl group at U34 of selected tRNAs.",
        "role": "MnmEG wobble-uridine cmnm5/mnm5 side-chain formation factor.",
        "part": "wobble_uridine_cmnm5_mnm5_s2_cmo_pathway",
        "core": [
            {
                "description": "FAD-associated MnmG/GidA factor for tRNA wobble-uridine modification at U34.",
                "directly_involved_in": ["GO:0002098"],
                "locations": ["GO:0005737"],
            }
        ],
    },
    "mnmE": {
        "description": "mnmE encodes the MnmE/TrmE tRNA-modification GTPase that works with MnmG during formation of carboxymethylaminomethyl-modified wobble uridines in selected tRNAs.",
        "role": "MnmE GTPase for MnmEG-dependent wobble-uridine modification.",
        "part": "wobble_uridine_cmnm5_mnm5_s2_cmo_pathway",
        "core": [
            {
                "description": "GTPase activity coupled to MnmEG tRNA wobble-uridine modification.",
                "molecular_function": "GO:0003924",
                "directly_involved_in": ["GO:0002098"],
                "locations": ["GO:0005737"],
            }
        ],
    },
    "tsaC": {
        "description": "tsaC encodes threonylcarbamoyl-AMP synthase, the Sua5-family enzyme that makes the TC-AMP intermediate required for N6-threonylcarbamoyladenosine formation at position 37 of tRNAs.",
        "role": "TC-AMP synthase for t6A37 biosynthesis.",
        "part": "t6a37_biosynthesis",
        "core": [
            {
                "description": "L-threonylcarbamoyladenylate synthase activity that supplies TC-AMP for tRNA t6A37 formation.",
                "molecular_function": "GO:0061710",
                "directly_involved_in": ["GO:0002949"],
                "locations": ["GO:0005737"],
            }
        ],
    },
    "tsaD": {
        "description": "tsaD encodes the TsaD tRNA N6-adenosine threonylcarbamoyltransferase, the catalytic subunit that transfers the threonylcarbamoyl group to A37 during bacterial t6A biosynthesis.",
        "role": "TsaD catalytic subunit for tRNA t6A37 biosynthesis.",
        "part": "t6a37_biosynthesis",
        "core": [
            {
                "description": "tRNA N(6)-L-threonylcarbamoyladenine synthase activity for t6A37 formation.",
                "molecular_function": "GO:0061711",
                "directly_involved_in": ["GO:0002949"],
                "locations": ["GO:0005737"],
            }
        ],
    },
    "cca": {
        "description": "cca encodes the multifunctional bacterial CCA-adding enzyme that builds, repairs, and can tandemly extend the 3-prime CCA end of tRNAs.",
        "role": "template-independent tRNA CCA and CCACCA nucleotidyltransferase.",
        "part": "trna_cca_processing",
        "core": [
            {
                "description": "Template-independent CCA addition to tRNA 3-prime ends.",
                "molecular_function": "GO:0004810",
                "directly_involved_in": ["GO:0001680", "GO:0042780"],
            },
            {
                "description": "Tandem CCACCA addition used in tRNA quality control.",
                "molecular_function": "GO:0160016",
            },
        ],
    },
    "cmoM": {
        "description": "cmoM encodes a CmoM-family tRNA 5-carboxymethoxyuridine methyltransferase that methylates cmo5U34 to mcmo5U34 in tRNAs.",
        "role": "CmoM cmo5U34 methyltransferase in wobble-uridine modification.",
        "part": "wobble_uridine_cmnm5_mnm5_s2_cmo_pathway",
        "core": [
            {
                "description": "tRNA 5-carboxymethoxyuridine(34) 5-O-methyltransferase activity.",
                "molecular_function": "GO:0097697",
                "directly_involved_in": ["GO:0006400"],
            }
        ],
    },
    "selU": {
        "description": "selU encodes tRNA 2-selenouridine synthase, a SelU-family enzyme that converts 2-thiouridine-containing wobble uridines to 2-selenouridine derivatives in selected tRNAs.",
        "role": "SelU wobble-uridine 2-selenouridine synthase.",
        "part": "wobble_uridine_cmnm5_mnm5_s2_cmo_pathway",
        "core": [
            {
                "description": "tRNA 2-selenouridine synthase activity on U34 thiolated tRNA substrates.",
                "molecular_function": "GO:0043828",
                "directly_involved_in": ["GO:0002098"],
            }
        ],
    },
    "trmJ": {
        "description": "trmJ encodes a SPOUT-family TrmJ methyltransferase that forms 2-prime-O-methylcytidine and 2-prime-O-methyluridine at position 32 in tRNAs.",
        "role": "TrmJ tRNA C32/U32 2-prime-O-ribose methyltransferase.",
        "part": "trna_methyltransferases",
        "core": [
            {
                "description": "tRNA cytidine(32)/uridine(32) 2-prime-O-ribose methyltransferase activity.",
                "molecular_function": "GO:0160206",
                "directly_involved_in": ["GO:0002128"],
                "locations": ["GO:0005737"],
            }
        ],
        "extra_accept": {"GO:0106339"},
    },
    "tadA": {
        "description": "tadA encodes the tRNA-specific adenosine deaminase that edits adenosine-34 to inosine in bacterial tRNAs.",
        "role": "TadA tRNA adenosine-34 deaminase.",
        "part": "trna_deamination_lysidine_thiolation_and_other_base_mods",
        "core": [
            {
                "description": "tRNA-specific adenosine-34 deaminase activity converting wobble adenosine to inosine.",
                "molecular_function": "GO:0052717",
                "directly_involved_in": ["GO:0002100"],
            }
        ],
        "extra_accept": {"GO:0008251"},
    },
    "cmoB": {
        "description": "cmoB encodes tRNA U34 carboxymethyltransferase, which transfers a carboxymethyl group from carboxy-S-adenosyl-L-methionine to 5-hydroxyuridine at wobble position 34.",
        "role": "CmoB wobble-uridine U34 carboxymethyltransferase.",
        "part": "wobble_uridine_cmnm5_mnm5_s2_cmo_pathway",
        "core": [
            {
                "description": "Alkyl or aryl transferase activity for carboxymethylation in tRNA wobble-uridine modification.",
                "molecular_function": "GO:0016765",
                "directly_involved_in": ["GO:0002098"],
            }
        ],
    },
    "trmD": {
        "description": "trmD encodes the TrmD SPOUT methyltransferase that installs N1-methylguanosine at position 37 in tRNAs.",
        "role": "TrmD tRNA guanine-37 N1 methyltransferase.",
        "part": "trna_methyltransferases",
        "core": [
            {
                "description": "tRNA guanine(37) N1 methyltransferase activity.",
                "molecular_function": "GO:0052906",
                "directly_involved_in": ["GO:0002939"],
                "locations": ["GO:0005737"],
            }
        ],
    },
    "tsaB": {
        "description": "tsaB encodes the TsaB accessory subunit of the bacterial t6A biosynthesis system, which supports TsaD/TsaE-dependent transfer of the threonylcarbamoyl group to tRNA A37.",
        "role": "TsaB accessory factor in tRNA t6A37 biosynthesis.",
        "part": "t6a37_biosynthesis",
        "core": [
            {
                "description": "Accessory factor for tRNA threonylcarbamoyladenosine modification.",
                "directly_involved_in": ["GO:0002949"],
                "locations": ["GO:0005737"],
            }
        ],
    },
    "tilS": {
        "description": "tilS encodes tRNA(Ile)-lysidine synthase, which ligates lysine onto cytidine-34 in tRNA(Ile) to generate lysidine and ensure AUA codon decoding as isoleucine.",
        "role": "TilS tRNA(Ile) lysidine synthase.",
        "part": "trna_deamination_lysidine_thiolation_and_other_base_mods",
        "core": [
            {
                "description": "tRNA(Ile)-lysidine synthase activity at wobble cytidine-34.",
                "molecular_function": "GO:0032267",
                "directly_involved_in": ["GO:0006400"],
                "locations": ["GO:0005737"],
            }
        ],
    },
    "truD": {
        "description": "truD encodes tRNA pseudouridine synthase D, the enzyme responsible for converting uridine-13 to pseudouridine in tRNAs.",
        "role": "TruD tRNA pseudouridine(13) synthase.",
        "part": "trna_pseudouridine_synthases",
        "core": [
            {
                "description": "tRNA pseudouridine(13) synthase activity.",
                "molecular_function": "GO:0160150",
                "directly_involved_in": ["GO:0031119"],
                "locations": ["GO:0005829"],
            }
        ],
    },
    "yfiP": {
        "description": "yfiP encodes a DTW-domain tRNA-uridine aminocarboxypropyltransferase predicted to install aminocarboxypropyl modifications on tRNA uridines.",
        "role": "YfiP tRNA-uridine aminocarboxypropyltransferase.",
        "part": "trna_deamination_lysidine_thiolation_and_other_base_mods",
        "core": [
            {
                "description": "tRNA-uridine aminocarboxypropyltransferase activity.",
                "molecular_function": "GO:0016432",
                "directly_involved_in": ["GO:0006400"],
            }
        ],
    },
    "ttcA": {
        "description": "ttcA encodes the iron-sulfur enzyme TtcA, an ATP-dependent tRNA cytidine-32 2-sulfurtransferase involved in tRNA thio-modification.",
        "role": "TtcA tRNA C32 2-thiolation enzyme.",
        "part": "trna_deamination_lysidine_thiolation_and_other_base_mods",
        "core": [
            {
                "description": "Sulfurtransferase activity for tRNA cytidine-32 2-thio-modification.",
                "molecular_function": "GO:0016783",
                "directly_involved_in": ["GO:0034227"],
                "locations": ["GO:0005737"],
            }
        ],
    },
    "rluA": {
        "description": "rluA encodes an RluA-family dual-specificity pseudouridine synthase that modifies tRNA position 32 and 23S rRNA position 746.",
        "role": "RluA dual tRNA and 23S rRNA pseudouridine synthase.",
        "part": "trna_pseudouridine_synthases",
        "core": [
            {
                "description": "tRNA pseudouridine(32) synthase activity.",
                "molecular_function": "GO:0160151",
                "directly_involved_in": ["GO:0001522"],
            },
            {
                "description": "23S rRNA pseudouridine(746) synthase activity.",
                "molecular_function": "GO:0160142",
                "directly_involved_in": ["GO:0000455"],
            },
        ],
    },
    "mnmC": {
        "description": "mnmC encodes bifunctional MnmC, which oxidizes and methylates the wobble U34 side chain during conversion of cmnm5s2U to mnm5s2U in tRNAs.",
        "role": "Bifunctional MnmC oxidoreductase and methyltransferase for mnm5s2U34 formation.",
        "part": "wobble_uridine_cmnm5_mnm5_s2_cmo_pathway",
        "core": [
            {
                "description": "tRNA mnm5s2U34 methyltransferase activity.",
                "molecular_function": "GO:0004808",
                "directly_involved_in": ["GO:0002098"],
                "locations": ["GO:0005737"],
            },
            {
                "description": "FAD-dependent oxidoreductase step in mnm5s2U34 biosynthesis.",
                "molecular_function": "GO:0016645",
                "directly_involved_in": ["GO:0002098"],
                "locations": ["GO:0005737"],
            },
        ],
    },
    "trhO": {
        "description": "trhO encodes tRNA uridine-34 hydroxylase, an oxygen-dependent enzyme that forms 5-hydroxyuridine at the wobble position of selected tRNAs.",
        "role": "TrhO tRNA U34 hydroxylase.",
        "part": "wobble_uridine_cmnm5_mnm5_s2_cmo_pathway",
        "core": [
            {
                "description": "Oxidoreductase activity for tRNA uridine-34 hydroxylation.",
                "molecular_function": "GO:0016705",
                "directly_involved_in": ["GO:0006400"],
            }
        ],
    },
    "dusC": {
        "description": "dusC encodes the DusC tRNA-dihydrouridine synthase that reduces uridine-16 to dihydrouridine in tRNAs.",
        "role": "DusC tRNA dihydrouridine-16 synthase.",
        "part": "trna_dihydrouridine_synthases",
        "core": [
            {
                "description": "tRNA-dihydrouridine16 synthase activity.",
                "molecular_function": "GO:0102262",
                "directly_involved_in": ["GO:0002943"],
            }
        ],
    },
    "truA": {
        "description": "truA encodes tRNA pseudouridine synthase A, which forms pseudouridine at positions 38, 39 and 40 in the anticodon stem-loop region of tRNAs.",
        "role": "TruA tRNA pseudouridine(38-40) synthase.",
        "part": "trna_pseudouridine_synthases",
        "core": [
            {
                "description": "tRNA pseudouridine(38-40) synthase activity.",
                "molecular_function": "GO:0160147",
                "directly_involved_in": ["GO:0031119"],
            }
        ],
    },
    "dusA": {
        "description": "dusA encodes the DusA tRNA-dihydrouridine synthase that reduces uridine-20 and uridine-20a in tRNA D-loops.",
        "role": "DusA tRNA dihydrouridine-20/20a synthase.",
        "part": "trna_dihydrouridine_synthases",
        "core": [
            {
                "description": "tRNA-dihydrouridine20 synthase activity.",
                "molecular_function": "GO:0102264",
                "directly_involved_in": ["GO:0002943"],
            },
            {
                "description": "tRNA-dihydrouridine20a synthase activity.",
                "molecular_function": "GO:0102266",
                "directly_involved_in": ["GO:0002943"],
            },
        ],
    },
    "trmK": {
        "description": "trmK encodes a TrmK-family tRNA adenine-22 N1 methyltransferase candidate.",
        "role": "TrmK tRNA adenine-22 N1 methyltransferase.",
        "part": "trna_methyltransferases",
        "core": [
            {
                "description": "tRNA adenine(22) N1 methyltransferase activity.",
                "molecular_function": "GO:0160105",
            }
        ],
    },
    "PP_4520": {
        "description": "PP_4520 encodes a DTWD2/TAPT-family tRNA-uridine aminocarboxypropyltransferase candidate.",
        "role": "DTWD2-family tRNA-uridine aminocarboxypropyltransferase.",
        "part": "trna_deamination_lysidine_thiolation_and_other_base_mods",
        "core": [
            {
                "description": "tRNA-uridine aminocarboxypropyltransferase activity.",
                "molecular_function": "GO:0016432",
                "directly_involved_in": ["GO:0006400"],
            }
        ],
    },
    "trmA": {
        "description": "trmA encodes the TrmA/RumT tRNA and tmRNA uracil-C5 methyltransferase that forms m5U54 in tRNAs and the corresponding methyluridine in tmRNA.",
        "role": "TrmA tRNA/tmRNA uracil-C5 methyltransferase.",
        "part": "trna_methyltransferases",
        "core": [
            {
                "description": "tRNA uracil(54) C5 methyltransferase activity.",
                "molecular_function": "GO:0030697",
                "directly_involved_in": ["GO:0030488"],
                "locations": ["GO:0005829"],
            }
        ],
        "over": {"GO:0019843"},
    },
    "truB": {
        "description": "truB encodes tRNA pseudouridine synthase B, which forms pseudouridine-55 in the T-loop of tRNAs.",
        "role": "TruB tRNA pseudouridine(55) synthase.",
        "part": "trna_pseudouridine_synthases",
        "core": [
            {
                "description": "tRNA pseudouridine(55) synthase activity.",
                "molecular_function": "GO:0160148",
                "directly_involved_in": ["GO:0031119"],
            }
        ],
        "over": {"GO:1990481"},
    },
    "dusB": {
        "description": "dusB encodes the DusB tRNA-dihydrouridine synthase subfamily enzyme, an FMN-dependent oxidoreductase that reduces uridine residues to dihydrouridine in tRNAs.",
        "role": "DusB tRNA dihydrouridine synthase.",
        "part": "trna_dihydrouridine_synthases",
        "core": [
            {
                "description": "tRNA dihydrouridine synthase activity.",
                "molecular_function": "GO:0017150",
                "directly_involved_in": ["GO:0002943"],
            }
        ],
    },
    "miaA": {
        "description": "miaA encodes tRNA dimethylallyltransferase, which transfers a dimethylallyl group to adenosine-37 in tRNAs that read codons beginning with uridine.",
        "role": "MiaA tRNA adenosine-37 dimethylallyltransferase.",
        "part": "trna_deamination_lysidine_thiolation_and_other_base_mods",
        "core": [
            {
                "description": "tRNA dimethylallyltransferase activity at adenosine-37.",
                "molecular_function": "GO:0052381",
                "directly_involved_in": ["GO:0006400"],
            }
        ],
    },
    "tsaE": {
        "description": "tsaE encodes the TsaE ATPase-family factor of the bacterial t6A biosynthesis system, supporting TsaD/TsaB-dependent threonylcarbamoyl transfer to tRNA A37.",
        "role": "TsaE accessory factor in tRNA t6A37 biosynthesis.",
        "part": "t6a37_biosynthesis",
        "core": [
            {
                "description": "Accessory factor for tRNA threonylcarbamoyladenosine modification.",
                "directly_involved_in": ["GO:0002949"],
                "locations": ["GO:0005737"],
            }
        ],
    },
    "trmL": {
        "description": "trmL encodes a TrmL SPOUT methyltransferase that methylates the 2-prime-O-ribose of cytidine-34 and cmnm5U34 wobble nucleotides in leucine tRNAs.",
        "role": "TrmL wobble-position tRNA ribose methyltransferase.",
        "part": "trna_methyltransferases",
        "core": [
            {
                "description": "tRNA cytidine(34) 2-prime-O-ribose methyltransferase activity.",
                "molecular_function": "GO:0141098",
                "directly_involved_in": ["GO:0002130", "GO:0002131"],
                "locations": ["GO:0005737"],
            },
            {
                "description": "tRNA cmnm5U34 2-prime-O-ribose methyltransferase activity.",
                "molecular_function": "GO:0141102",
                "directly_involved_in": ["GO:0002130", "GO:0002132"],
                "locations": ["GO:0005737"],
            },
        ],
    },
}


EXTRA_TERMS = {
    "GO:0000455": term("GO:0000455", "enzyme-directed rRNA pseudouridine synthesis"),
    "GO:0001522": term("GO:0001522", "pseudouridine synthesis"),
    "GO:0001680": term("GO:0001680", "tRNA 3'-terminal CCA addition"),
    "GO:0002100": term("GO:0002100", "tRNA wobble adenosine to inosine editing"),
    "GO:0002128": term("GO:0002128", "tRNA nucleoside ribose methylation"),
    "GO:0002130": term("GO:0002130", "wobble position ribose methylation"),
    "GO:0002131": term("GO:0002131", "wobble position cytosine ribose methylation"),
    "GO:0002132": term("GO:0002132", "wobble position uridine ribose methylation"),
    "GO:0002939": term("GO:0002939", "tRNA N1-guanine methylation"),
    "GO:0002943": term("GO:0002943", "tRNA dihydrouridine synthesis"),
    "GO:0002949": term("GO:0002949", "tRNA threonylcarbamoyladenosine modification"),
    "GO:0003924": term("GO:0003924", "GTPase activity"),
    "GO:0004808": term("GO:0004808", "tRNA (5-methylaminomethyl-2-thiouridylate)(34)-methyltransferase activity"),
    "GO:0004810": term("GO:0004810", "CCA tRNA nucleotidyltransferase activity"),
    "GO:0005737": term("GO:0005737", "cytoplasm"),
    "GO:0005829": term("GO:0005829", "cytosol"),
    "GO:0006400": term("GO:0006400", "tRNA modification"),
    "GO:0008033": term("GO:0008033", "tRNA processing"),
    "GO:0016432": term("GO:0016432", "tRNA-uridine aminocarboxypropyltransferase activity"),
    "GO:0016645": term("GO:0016645", "oxidoreductase activity, acting on the CH-NH group of donors"),
    "GO:0016705": term(
        "GO:0016705",
        "oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen",
    ),
    "GO:0016765": term("GO:0016765", "transferase activity, transferring alkyl or aryl (other than methyl) groups"),
    "GO:0016783": term("GO:0016783", "sulfurtransferase activity"),
    "GO:0017150": term("GO:0017150", "tRNA dihydrouridine synthase activity"),
    "GO:0030488": term("GO:0030488", "tRNA methylation"),
    "GO:0030697": term("GO:0030697", "tRNA (uracil(54)-C5)-methyltransferase activity, S-adenosyl methionine-dependent"),
    "GO:0031119": term("GO:0031119", "tRNA pseudouridine synthesis"),
    "GO:0032267": term("GO:0032267", "tRNA(Ile)-lysidine synthase activity"),
    "GO:0034227": term("GO:0034227", "tRNA thio-modification"),
    "GO:0042780": term("GO:0042780", "tRNA 3'-end processing"),
    "GO:0043828": term("GO:0043828", "tRNA 2-selenouridine synthase activity"),
    "GO:0052381": term("GO:0052381", "tRNA dimethylallyltransferase activity"),
    "GO:0052717": term("GO:0052717", "tRNA-specific adenosine-34 deaminase activity"),
    "GO:0052906": term("GO:0052906", "tRNA (guanine(37)-N1)-methyltransferase activity"),
    "GO:0061710": term("GO:0061710", "L-threonylcarbamoyladenylate synthase activity"),
    "GO:0061711": term("GO:0061711", "tRNA N(6)-L-threonylcarbamoyladenine synthase activity"),
    "GO:0097697": term("GO:0097697", "tRNA (5-carboxymethoxyuridine(34)-5-O)-methyltransferase activity"),
    "GO:0102262": term("GO:0102262", "tRNA-dihydrouridine16 synthase activity"),
    "GO:0102264": term("GO:0102264", "tRNA-dihydrouridine20 synthase activity"),
    "GO:0102266": term("GO:0102266", "tRNA-dihydrouridine20a synthase activity"),
    "GO:0106339": term("GO:0106339", "tRNA (cytidine(32)-2'-O-ribose)-methyltransferase activity"),
    "GO:0141098": term("GO:0141098", "tRNA (cytidine(34)-2'-O-ribose)-methyltransferase activity"),
    "GO:0141102": term("GO:0141102", "tRNA (5-carboxymethylaminomethyluridine(34)-2'-O-ribose)-methyltransferase activity"),
    "GO:0160016": term("GO:0160016", "CCACCA tRNA nucleotidyltransferase activity"),
    "GO:0160105": term("GO:0160105", "tRNA (adenine(22)-N1)-methyltransferase activity"),
    "GO:0160142": term("GO:0160142", "23S rRNA pseudouridine(746) synthase activity"),
    "GO:0160147": term("GO:0160147", "tRNA pseudouridine(38-40) synthase activity"),
    "GO:0160148": term("GO:0160148", "tRNA pseudouridine(55) synthase activity"),
    "GO:0160150": term("GO:0160150", "tRNA pseudouridine(13) synthase activity"),
    "GO:0160151": term("GO:0160151", "tRNA pseudouridine(32) synthase activity"),
    "GO:0160206": term("GO:0160206", "tRNA (cytidine(32)/uridine(32)-2'-O-ribose)-methyltransferase activity"),
}


BINDING_TERMS = {
    "GO:0000049",
    "GO:0003723",
    "GO:0003725",
    "GO:0019843",
    "GO:0042802",
}
COFACTOR_TERMS = {
    "GO:0000166",
    "GO:0000287",
    "GO:0005506",
    "GO:0005524",
    "GO:0005525",
    "GO:0008270",
    "GO:0010181",
    "GO:0050660",
    "GO:0051539",
}
BROAD_ACTIVITY_TERMS = {
    "GO:0008168",
    "GO:0008173",
    "GO:0008175",
    "GO:0008757",
    "GO:0009982",
    "GO:0016491",
    "GO:0016747",
    "GO:0016779",
    "GO:0016787",
    "GO:0016879",
    "GO:0140098",
}
BROAD_PROCESS_TERMS = {
    "GO:0002097",
    "GO:0006396",
    "GO:0006400",
    "GO:0006450",
    "GO:0008033",
    "GO:0009451",
    "GO:0010467",
}


def gene_file(gene: str, suffix: str) -> Path:
    return GENE_ROOT / gene / f"{gene}-{suffix}"


def file_id(gene: str, suffix: str) -> str:
    return f"file:PSEPK/{gene}/{gene}-{suffix}"


def load_gene_review(gene: str) -> dict:
    return yaml.safe_load(gene_file(gene, "ai-review.yaml").read_text(encoding="utf-8")) or {}


def build_term_map() -> dict[str, dict[str, str]]:
    terms = dict(EXTRA_TERMS)
    for gene in GENES:
        path = gene_file(gene, "ai-review.yaml")
        if not path.exists():
            continue
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        for ann in data.get("existing_annotations", []):
            item = ann.get("term") or {}
            if item.get("id") and item.get("label"):
                terms[item["id"]] = term(item["id"], item["label"])
    return terms


TERM = build_term_map()


def t(go_id: str) -> dict[str, str]:
    if go_id not in TERM:
        raise KeyError(f"Missing GO term label for {go_id}")
    return TERM[go_id]


def line_containing(path: Path, *needles: str) -> str | None:
    if not path.exists():
        return None
    for line in path.read_text(encoding="utf-8").splitlines():
        if all(needle in line for needle in needles):
            return line
    return None


def support(reference_id: str, text: str | None) -> dict[str, str] | None:
    if not text:
        return None
    return {"reference_id": reference_id, "supporting_text": text}


def add_support(items: list[dict[str, str]], item: dict[str, str] | None) -> None:
    if item and item not in items:
        items.append(item)


def goa_line(gene: str, term_id: str) -> str | None:
    return line_containing(gene_file(gene, "goa.tsv"), term_id)


def evidence_for(gene: str, term_id: str | None = None) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    if term_id:
        add_support(items, support(file_id(gene, "goa.tsv"), goa_line(gene, term_id)))
    uniprot = gene_file(gene, "uniprot.txt")
    for marker in (
        "DE   ",
        "CC   -!- FUNCTION:",
        "CC   -!- CATALYTIC ACTIVITY:",
        "CC   -!- COFACTOR:",
        "CC   -!- SIMILARITY:",
        "DR   GO;",
        "DR   InterPro;",
        "DR   Pfam;",
        "DR   PANTHER;",
        "KW   ",
    ):
        add_support(items, support(file_id(gene, "uniprot.txt"), line_containing(uniprot, marker)))
    return items


def preferred_mfs(gene: str) -> list[str]:
    out = []
    for entry in SPEC[gene]["core"]:
        if entry.get("molecular_function"):
            out.append(entry["molecular_function"])
    return out


def preferred_processes(gene: str) -> set[str]:
    out: set[str] = set()
    for entry in SPEC[gene]["core"]:
        out.update(entry.get("directly_involved_in", []))
    return out


def preferred_locations(gene: str) -> set[str]:
    out: set[str] = set()
    for entry in SPEC[gene]["core"]:
        out.update(entry.get("locations", []))
    return out


def make_review(
    summary: str,
    action: str,
    reason: str,
    gene: str,
    term_id: str,
    replacements: list[str] | None = None,
) -> dict:
    out = {
        "summary": summary,
        "action": action,
        "reason": reason,
        "supported_by": evidence_for(gene, term_id),
    }
    if replacements:
        out["proposed_replacement_terms"] = [t(go_id) for go_id in replacements]
    return out


def review_for(gene: str, term_id: str) -> dict:
    term_label = TERM.get(term_id, {"label": term_id})["label"]
    mfs = preferred_mfs(gene)
    processes = preferred_processes(gene)
    locations = preferred_locations(gene)
    spec = SPEC[gene]

    if term_id in spec.get("over", set()):
        return make_review(
            f"{term_label} is likely an off-substrate or over-propagated electronic annotation for {gene}.",
            "MARK_AS_OVER_ANNOTATED",
            f"The supported first-pass role is {spec['role']}; this term should not be treated as a core function for this protein.",
            gene,
            term_id,
        )

    if term_id in mfs or term_id in spec.get("extra_accept", set()):
        return make_review(
            f"{term_label} is a supported molecular function for {gene}.",
            "ACCEPT",
            f"The UniProt product/function context and GOA row match the first-pass role: {spec['role']}",
            gene,
            term_id,
        )

    if term_id in processes:
        return make_review(
            f"{term_label} is appropriate biological-process context for {gene}.",
            "ACCEPT",
            f"The process captures the tRNA modification, editing, or processing context for {spec['role']}",
            gene,
            term_id,
        )

    if term_id in locations:
        return make_review(
            f"{term_label} is appropriate bacterial cytoplasmic location context for {gene}.",
            "ACCEPT",
            "The annotation is compatible with the soluble bacterial tRNA modification or processing role recorded for this gene.",
            gene,
            term_id,
        )

    if term_id in COFACTOR_TERMS:
        return make_review(
            f"{term_label} is retained as cofactor, substrate, or nucleotide-binding context for {gene}.",
            "KEEP_AS_NON_CORE",
            "This row is compatible with the enzyme family, but the core annotation should be the tRNA modification reaction or pathway step.",
            gene,
            term_id,
        )

    if term_id in BINDING_TERMS:
        action = "MARK_AS_OVER_ANNOTATED" if term_id in {"GO:0003725", "GO:0019843"} else "KEEP_AS_NON_CORE"
        return make_review(
            f"{term_label} is substrate or family-context binding information for {gene}.",
            action,
            "Binding context is less informative than the supported catalytic tRNA modification or processing activity in this batch.",
            gene,
            term_id,
        )

    if term_id in BROAD_ACTIVITY_TERMS:
        replacements = [mfs[0]] if mfs else None
        if replacements and replacements[0] != term_id:
            return make_review(
                f"{term_label} is broad relative to the best-supported activity for {gene}.",
                "MODIFY",
                "The row is chemically compatible, but the site- or reaction-specific tRNA modification term is the preferred molecular-function representation.",
                gene,
                term_id,
                replacements,
            )
        return make_review(
            f"{term_label} is retained as the best available molecular-function term for {gene}.",
            "ACCEPT",
            f"No sharper current GOA molecular-function row is available, and the term matches the first-pass role: {spec['role']}",
            gene,
            term_id,
        )

    if term_id in BROAD_PROCESS_TERMS:
        action = "MARK_AS_OVER_ANNOTATED" if term_id in {"GO:0006396", "GO:0009451", "GO:0010467"} else "KEEP_AS_NON_CORE"
        return make_review(
            f"{term_label} is true but broad for {gene}.",
            action,
            f"The term is compatible with {spec['role']} but is less informative than the specific modification process or molecular function.",
            gene,
            term_id,
        )

    return make_review(
        f"{term_label} is retained conservatively for {gene}.",
        "KEEP_AS_NON_CORE",
        "The annotation is compatible with the available UniProt/GOA evidence but is not the most specific statement of the gene product's role.",
        gene,
        term_id,
    )


def references_for(gene: str, data: dict) -> list[dict]:
    seen = set()
    refs: list[dict] = []
    for ref in data.get("references", []):
        ref_id = ref.get("id")
        if ref_id not in seen:
            refs.append(ref)
            seen.add(ref_id)
    for suffix, title in [
        ("uniprot.txt", f"{gene} UniProt flat-file record"),
        ("goa.tsv", f"{gene} GOA/QuickGO annotation rows"),
        ("deep-research-asta.md", f"{gene} Asta gene-level retrieval report"),
    ]:
        ref_id = file_id(gene, suffix)
        if ref_id not in seen and gene_file(gene, suffix).exists():
            ref = {"id": ref_id, "title": title, "findings": []}
            if suffix == "deep-research-asta.md":
                accession = line_containing(gene_file(gene, suffix), "uniprot_accession:")
                if accession:
                    ref["findings"].append(
                        {
                            "statement": "Asta retrieval was generated for this first-pass review and retained as lightweight identity context.",
                            "supporting_text": accession.strip(),
                        }
                    )
            refs.append(ref)
            seen.add(ref_id)
    return refs


def core_function(gene: str, core: dict) -> dict:
    out = {"description": core["description"]}
    support_items: list[dict[str, str]] = []
    if core.get("molecular_function"):
        mf = core["molecular_function"]
        out["molecular_function"] = t(mf)
        support_items.extend(evidence_for(gene, mf))
    else:
        support_items.extend(evidence_for(gene))
    if core.get("directly_involved_in"):
        out["directly_involved_in"] = [t(x) for x in core["directly_involved_in"]]
        for process_id in core["directly_involved_in"]:
            add_support(support_items, support(file_id(gene, "goa.tsv"), goa_line(gene, process_id)))
    if core.get("locations"):
        out["locations"] = [t(x) for x in core["locations"]]
        for location_id in core["locations"]:
            add_support(support_items, support(file_id(gene, "goa.tsv"), goa_line(gene, location_id)))
    if support_items:
        out["supported_by"] = support_items
    return out


def suggested_questions(gene: str) -> list[dict[str, str]]:
    if gene in {"yfiP", "PP_4520"}:
        return [{"question": f"What exact tRNA substrate and uridine position does {gene} modify in P. putida KT2440?"}]
    if gene in {"tsaB", "tsaE"}:
        return [{"question": f"What is the direct biochemical contribution of {gene} to the bacterial TsaBDE t6A37 transfer complex in KT2440?"}]
    return [
        {
            "question": f"Which tRNA species and growth conditions most depend on the {gene}-dependent modification in P. putida KT2440?"
        }
    ]


def suggested_experiments(gene: str) -> list[dict[str, str]]:
    return [
        {
            "description": f"Compare wild-type and {gene} perturbation strains by tRNA modification mapping, growth phenotyping, and translation-fidelity or stress-response assays.",
            "experiment_type": "tRNA modification mapping and translation phenotype assay",
        }
    ]


def write_notes(gene: str) -> None:
    notes_path = gene_file(gene, "notes.md")
    heading = "## 2026-07-10 first-pass translation/RNA-processing tRNA-modification split"
    block = "\n".join(
        [
            heading,
            "",
            f"- Batch: `{BATCH_TSV}`.",
            f"- Asta retrieval report: `{file_id(gene, 'deep-research-asta.md')}`. The report is retained as provenance; annotation decisions are supported primarily by local UniProt and GOA rows.",
            f"- Main conclusion: {SPEC[gene]['role']}",
            "",
        ]
    )
    if gene in PRESERVE_EXISTING_REVIEWS and notes_path.exists():
        existing = notes_path.read_text(encoding="utf-8")
        if heading not in existing:
            notes_path.write_text(existing.rstrip() + "\n\n" + block, encoding="utf-8")
        return
    notes_path.write_text(f"# {gene} tRNA-modification first-pass notes\n\n{block}", encoding="utf-8")


def curate_gene(gene: str) -> None:
    data = load_gene_review(gene)
    data["status"] = "DRAFT"
    if gene not in PRESERVE_EXISTING_REVIEWS:
        data["description"] = SPEC[gene]["description"]
        for ann in data.get("existing_annotations", []):
            ann["review"] = review_for(gene, ann["term"]["id"])
        data["core_functions"] = [core_function(gene, core) for core in SPEC[gene]["core"]]
        data["proposed_new_terms"] = []
        data["suggested_questions"] = suggested_questions(gene)
        data["suggested_experiments"] = suggested_experiments(gene)
    data["references"] = references_for(gene, data)
    gene_file(gene, "ai-review.yaml").write_text(
        yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, width=120, allow_unicode=True),
        encoding="utf-8",
    )
    write_notes(gene)


def clean_id(text: str) -> str:
    out = re.sub(r"[^A-Za-z0-9_]+", "_", text.lower())
    out = re.sub(r"_+", "_", out).strip("_")
    return out


def annoton(gene: str, core: dict, index: int = 1) -> dict:
    label = core["description"]
    if len(SPEC[gene]["core"]) > 1:
        label = f"{label} ({index})"
    out = {
        "id": f"{clean_id(gene)}_{clean_id(label)}",
        "label": f"{gene}: {label}",
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "role_description": core["description"],
    }
    if core.get("molecular_function"):
        mf = core["molecular_function"]
        out["function"] = {"preferred_term": TERM[mf]["label"], "term": t(mf)}
    if core.get("directly_involved_in"):
        out["processes"] = [{"preferred_term": TERM[x]["label"], "term": t(x)} for x in core["directly_involved_in"]]
    if core.get("locations"):
        out["locations"] = [{"preferred_term": TERM[x]["label"], "term": t(x)} for x in core["locations"]]
    return out


def annotons_for(genes: list[str]) -> list[dict]:
    out = []
    for gene in genes:
        for index, core in enumerate(SPEC[gene]["core"], start=1):
            out.append(annoton(gene, core, index))
    return out


PARTS = [
    (
        "wobble_uridine_cmnm5_mnm5_s2_cmo_pathway",
        "Wobble-uridine U34 side-chain modification",
        "MnmEG/MnmC, CmoB/CmoM, SelU and TrhO factors modifying wobble uridine side chains.",
        ["mnmG", "mnmE", "cmoM", "cmoB", "selU", "mnmC", "trhO"],
    ),
    (
        "t6a37_biosynthesis",
        "t6A37 threonylcarbamoyladenosine biosynthesis",
        "TsaC/TsaB/TsaD/TsaE factors for N6-threonylcarbamoyladenosine formation at tRNA position 37.",
        ["tsaC", "tsaD", "tsaB", "tsaE"],
    ),
    (
        "trna_methyltransferases",
        "tRNA methyltransferases",
        "Trm enzymes installing base or ribose methyl marks at defined tRNA positions.",
        ["trmJ", "trmD", "trmK", "trmA", "trmL"],
    ),
    (
        "trna_pseudouridine_synthases",
        "tRNA pseudouridine synthases",
        "Tru/Rlu pseudouridine synthases acting on tRNA uridines, with RluA retaining its dual rRNA activity.",
        ["truD", "rluA", "truA", "truB"],
    ),
    (
        "trna_deamination_lysidine_thiolation_and_other_base_mods",
        "tRNA deamination, lysidine, thiolation, prenylation, and aminocarboxypropylation",
        "TadA, TilS, TtcA, MiaA and DTW-domain enzymes for non-methyl, non-pseudouridine tRNA base modifications.",
        ["tadA", "tilS", "yfiP", "ttcA", "PP_4520", "miaA"],
    ),
    (
        "trna_dihydrouridine_synthases",
        "tRNA dihydrouridine synthases",
        "Dus-family enzymes reducing specific tRNA uridines to dihydrouridines.",
        ["dusC", "dusA", "dusB"],
    ),
    (
        "trna_cca_processing",
        "tRNA CCA-end processing and quality control",
        "CCA-adding and CCACCA-adding activity for mature tRNA 3-prime ends and tRNA surveillance.",
        ["cca"],
    ),
]


def write_module() -> None:
    module_parts = []
    for order, (part_id, label, description, genes) in enumerate(PARTS, start=1):
        module_parts.append(
            {
                "order": order,
                "role": label,
                "node": {
                    "id": part_id,
                    "label": label,
                    "module_type": "BIOLOGICAL_PROCESS",
                    "description": description,
                    "annotons": annotons_for(genes),
                },
            }
        )
    module = {
        "id": "MODULE:trna_modification_processing_boundary",
        "title": "tRNA modification, editing, and processing boundary",
        "description": (
            "Boundary module for PSEPK tRNA modification and processing genes from the translation/RNA-processing umbrella. "
            "It covers wobble-uridine side-chain chemistry, t6A37 formation, tRNA methylation, pseudouridylation, deamination, "
            "lysidine formation, thiolation, dihydrouridine synthesis, aminocarboxypropylation, prenylation, and CCA-end processing."
        ),
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": f"file:{BATCH_TSV}",
                "title": "PSEPK translation/RNA tRNA modification split",
                "statement": "The batch records tRNA modification, editing, and CCA-end processing enzymes curated in the final translation/RNA-processing split.",
            }
        ]
        + [
            {
                "source_id": file_id(gene, "ai-review.yaml"),
                "title": f"Curated {gene} review",
                "statement": SPEC[gene]["description"],
            }
            for gene in GENES
        ],
        "module": {
            "id": "trna_modification_processing_boundary",
            "label": "tRNA modification, editing, and processing boundary",
            "module_type": "BIOLOGICAL_PROCESS",
            "concepts": [
                {"preferred_term": TERM[x]["label"], "term": t(x)}
                for x in [
                    "GO:0006400",
                    "GO:0002098",
                    "GO:0002949",
                    "GO:0030488",
                    "GO:0031119",
                    "GO:0002943",
                    "GO:0002100",
                    "GO:0034227",
                    "GO:0001680",
                    "GO:0042780",
                ]
            ],
            "parts": module_parts,
        },
    }
    MODULE_PATH.write_text(
        yaml.dump(module, Dumper=NoAliasDumper, sort_keys=False, width=120, allow_unicode=True),
        encoding="utf-8",
    )


def main() -> None:
    for gene in GENES:
        curate_gene(gene)
    write_module()


if __name__ == "__main__":
    main()
