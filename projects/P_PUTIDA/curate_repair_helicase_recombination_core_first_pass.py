#!/usr/bin/env python3
"""First-pass curation for the PSEPK repair-helicase/recombination split."""

from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes" / "PSEPK"
MODULE_PATH = ROOT / "modules" / "bacterial_homologous_recombination.yaml"
BATCH_TSV = "projects/P_PUTIDA/batches/module_dna_replication_repair_recombination_repair_helicase_recombination_core.tsv"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


TERM = {
    "GO:0000018": {"id": "GO:0000018", "label": "regulation of DNA recombination"},
    "GO:0000166": {"id": "GO:0000166", "label": "nucleotide binding"},
    "GO:0000725": {"id": "GO:0000725", "label": "recombinational repair"},
    "GO:0003676": {"id": "GO:0003676", "label": "nucleic acid binding"},
    "GO:0003677": {"id": "GO:0003677", "label": "DNA binding"},
    "GO:0003678": {"id": "GO:0003678", "label": "DNA helicase activity"},
    "GO:0003684": {"id": "GO:0003684", "label": "damaged DNA binding"},
    "GO:0003690": {"id": "GO:0003690", "label": "double-stranded DNA binding"},
    "GO:0004386": {"id": "GO:0004386", "label": "helicase activity"},
    "GO:0004519": {"id": "GO:0004519", "label": "endonuclease activity"},
    "GO:0004521": {"id": "GO:0004521", "label": "RNA endonuclease activity"},
    "GO:0005524": {"id": "GO:0005524", "label": "ATP binding"},
    "GO:0005737": {"id": "GO:0005737", "label": "cytoplasm"},
    "GO:0005829": {"id": "GO:0005829", "label": "cytosol"},
    "GO:0006259": {"id": "GO:0006259", "label": "DNA metabolic process"},
    "GO:0006260": {"id": "GO:0006260", "label": "DNA replication"},
    "GO:0006281": {"id": "GO:0006281", "label": "DNA repair"},
    "GO:0006302": {"id": "GO:0006302", "label": "double-strand break repair"},
    "GO:0006310": {"id": "GO:0006310", "label": "DNA recombination"},
    "GO:0008094": {"id": "GO:0008094", "label": "ATP-dependent activity, acting on DNA"},
    "GO:0008270": {"id": "GO:0008270", "label": "zinc ion binding"},
    "GO:0008408": {"id": "GO:0008408", "label": "3'-5' exonuclease activity"},
    "GO:0009295": {"id": "GO:0009295", "label": "nucleoid"},
    "GO:0009432": {"id": "GO:0009432", "label": "SOS response"},
    "GO:0016787": {"id": "GO:0016787", "label": "hydrolase activity"},
    "GO:0016818": {"id": "GO:0016818", "label": "hydrolase activity, acting on acid anhydrides, in phosphorus-containing anhydrides"},
    "GO:0016887": {"id": "GO:0016887", "label": "ATP hydrolysis activity"},
    "GO:0031297": {"id": "GO:0031297", "label": "replication fork processing"},
    "GO:0033677": {"id": "GO:0033677", "label": "DNA/RNA helicase activity"},
    "GO:0033679": {"id": "GO:0033679", "label": "3'-5' DNA/RNA helicase activity"},
    "GO:0043022": {"id": "GO:0043022", "label": "ribosome binding"},
    "GO:0043138": {"id": "GO:0043138", "label": "3'-5' DNA helicase activity"},
    "GO:0043139": {"id": "GO:0043139", "label": "5'-3' DNA helicase activity"},
    "GO:0043590": {"id": "GO:0043590", "label": "bacterial nucleoid"},
    "GO:0046872": {"id": "GO:0046872", "label": "metal ion binding"},
    "GO:0051539": {"id": "GO:0051539", "label": "4 iron, 4 sulfur cluster binding"},
    "GO:0140664": {"id": "GO:0140664", "label": "ATP-dependent DNA damage sensor activity"},
}


PUBS = {
    "PMID:30224353": "Characterization of Lhr-Core DNA helicase and manganese- dependent DNA nuclease components of a bacterial gene cluster encoding nucleic acid repair enzymes.",
}


GENE_INFO = {
    "PP_0152": {
        "accession": "Q88RH7",
        "description": "PP_0152 is a low-information KT2440 protein assigned a ProtNLM-derived Holliday-junction-resolvasome/helicase-subunit name. The fetched record has no GOA rows and only CHP02448/DUF2388 plus a signal peptide, so this first pass does not promote a recombination or helicase GO function.",
        "core": [],
    },
    "PP_1061": {
        "accession": "Q88NZ2",
        "description": "PP_1061 is a large Lhr-like ATP-dependent helicase candidate in Pseudomonas putida KT2440. UniProt keyword and domain evidence support a DNA/nucleic-acid helicase ATPase, but no KT2440-specific biochemical assay was found in the first-pass Asta retrieval.",
        "core": [
            {"description": "Lhr-like ATP-dependent helicase candidate.", "molecular_function": TERM["GO:0004386"], "support_term": "GO:0004386"},
        ],
    },
    "PP_1103": {
        "accession": "Q88NV1",
        "description": "PP_1103 encodes the experimentally characterized P. putida Lhr-Core helicase. The protein is an ssDNA-dependent ATPase/dATPase and ATP-dependent 3'-to-5' helicase that unwinds DNA duplexes and RNA:DNA hybrids, and its locus context supports a probable DNA repair pathway role.",
        "core": [
            {"description": "Experimentally characterized ATP-dependent 3'-to-5' DNA helicase/translocase.", "molecular_function": TERM["GO:0043138"], "support_term": "GO:0043138"},
            {"description": "ssDNA-dependent ATP hydrolysis coupled to Lhr-Core translocation and unwinding.", "molecular_function": TERM["GO:0016887"], "support_term": "GO:0016887"},
        ],
        "pubs": ["PMID:30224353"],
    },
    "PP_1106": {
        "accession": "Q88NU8",
        "description": "PP_1106 is a DNA-ligase-associated metallo-beta-lactamase/Xnuc_lig-associated nuclease candidate near the Lhr-Core locus. Its only fetched GOA row is RNA endonuclease activity from TreeGrafter, but the local metadata support only a broad predicted nuclease context, so no precise core GO function is asserted in this first pass.",
        "core": [],
    },
    "dinG": {
        "accession": "Q88NS9",
        "description": "dinG encodes a DinG/Rad3-like ATP-dependent DNA helicase in Pseudomonas putida KT2440. HAMAP/UniProt evidence supports DNA-dependent ATPase and 5'-to-3' DNA helicase activity on D-loops, R-loops, forked DNA, and G-quadruplex DNA, with an iron-sulfur cluster.",
        "core": [
            {"description": "DinG-family 5'-to-3' DNA helicase.", "molecular_function": TERM["GO:0043139"], "directly_involved_in": [TERM["GO:0006281"]], "support_term": "GO:0043139"},
            {"description": "Fe-S cluster cofactor associated with DinG helicase function.", "molecular_function": TERM["GO:0051539"], "support_term": "GO:0051539"},
        ],
    },
    "PP_1410": {
        "accession": "Q88N08",
        "description": "PP_1410 is an unresolved KT2440 Cys-rich CWC-domain protein with a ProtNLM-derived generic helicase name but no GOA rows and no canonical helicase ATPase domain in the fetched metadata. No GO function is asserted in this first pass.",
        "core": [],
    },
    "rdgC": {
        "accession": "Q88M72",
        "description": "rdgC encodes a recombination-associated RdgC-family protein in Pseudomonas putida KT2440. HAMAP, InterPro, Pfam, and PANTHER support a bacterial RdgC protein that binds double-stranded DNA and participates in DNA recombination regulation in the cytoplasm/nucleoid context.",
        "core": [
            {"description": "RdgC-family double-stranded-DNA-binding recombination-associated protein.", "molecular_function": TERM["GO:0003690"], "directly_involved_in": [TERM["GO:0006310"], TERM["GO:0000018"]], "locations": [TERM["GO:0043590"], TERM["GO:0005737"]], "support_term": "GO:0003690"},
        ],
    },
    "PP_1937": {
        "accession": "Q88LJ4",
        "description": "PP_1937 is a SNF2-family helicase-like repair candidate in Pseudomonas putida KT2440. The fetched annotations support DNA repair and replication-fork-processing context, while UniProt/Asta domain evidence supports a conservative new helicase activity call.",
        "core": [
            {"description": "SNF2-like helicase-family repair candidate.", "molecular_function": TERM["GO:0004386"], "directly_involved_in": [TERM["GO:0006281"]], "support_term": "GO:0004386"},
        ],
        "new_terms": ["GO:0004386"],
    },
    "sbcC": {
        "accession": "Q88LB1",
        "description": "sbcC encodes the ATPase/SMC-like subunit of the SbcCD nuclease complex. UniProt describes SbcCD as opening DNA hairpins and processing DNA structures that arise during replication and recombination; fetched GOA supports ATP hydrolysis and double-strand-break repair context.",
        "core": [
            {"description": "SbcCD ATPase subunit contributing to double-strand-break/hairpin-DNA repair.", "molecular_function": TERM["GO:0016887"], "directly_involved_in": [TERM["GO:0006302"]], "support_term": "GO:0016887"},
        ],
    },
    "sbcD": {
        "accession": "Q88LB0",
        "description": "sbcD encodes the nuclease subunit of the SbcCD DNA-structure-processing complex in Pseudomonas putida KT2440. UniProt and GOA support endonuclease and 3'-to-5' exonuclease activities in DNA metabolic/recombination contexts.",
        "core": [
            {"description": "SbcCD nuclease subunit with endonuclease and 3'-to-5' exonuclease activities.", "molecular_function": TERM["GO:0008408"], "support_term": "GO:0008408"},
            {"description": "SbcCD-associated DNA endonuclease activity.", "molecular_function": TERM["GO:0004519"], "support_term": "GO:0004519"},
        ],
    },
    "uup": {
        "accession": "Q88L06",
        "description": "uup encodes an ABCF-family ATPase in Pseudomonas putida KT2440. HAMAP supports ATPase, DNA-binding, ribosome-binding, and cytoplasmic localization, with a probable role in ribosome function and possible involvement in resolving branched DNA intermediates from postreplication gaps.",
        "core": [
            {"description": "ABCF/Uup ATPase with ribosome-binding and possible branched-DNA-intermediate context.", "molecular_function": TERM["GO:0016887"], "locations": [TERM["GO:0005737"]], "support_term": "GO:0016887"},
            {"description": "Ribosome-associated Uup function retained as the best supported specific binding annotation.", "molecular_function": TERM["GO:0043022"], "locations": [TERM["GO:0005737"]], "support_term": "GO:0043022"},
        ],
    },
    "PP_2146": {
        "accession": "Q88KZ3",
        "description": "PP_2146 is a SNF2/RAD54-family helicase-like ATPase candidate in Pseudomonas putida KT2440. Current metadata support helicase-family activity plus zinc/SWIM-domain context, but do not resolve a specific DNA-repair substrate or pathway step.",
        "core": [
            {"description": "SNF2/RAD54-family helicase candidate.", "molecular_function": TERM["GO:0004386"], "support_term": "GO:0004386"},
        ],
        "new_terms": ["GO:0004386"],
    },
    "PP_2298": {
        "accession": "Q88KJ2",
        "description": "PP_2298 is an unresolved DUF6388 protein with a ProtNLM-derived DNA-repair-ATPase name but no GOA rows, no PANTHER family, and no specific catalytic domain in the fetched metadata. No GO function is asserted in this first pass.",
        "core": [],
    },
    "PP_2565": {
        "accession": "Q88JT2",
        "description": "PP_2565 is a UvrD/Rep-family DNA helicase candidate in Pseudomonas putida KT2440. UniProt/GOA evidence supports ATP-dependent 3'-to-5' DNA helicase activity, DNA binding, cytosolic localization, and recombinational-repair context.",
        "core": [
            {"description": "UvrD/Rep-family ATP-dependent 3'-to-5' DNA helicase.", "molecular_function": TERM["GO:0043138"], "directly_involved_in": [TERM["GO:0000725"]], "locations": [TERM["GO:0005829"]], "support_term": "GO:0043138"},
        ],
    },
    "PP_3681": {
        "accession": "Q88GN9",
        "description": "PP_3681 is a UvrD/Rep-family DNA 3'-to-5' helicase candidate in Pseudomonas putida KT2440. UniProt/GOA evidence supports ATP hydrolysis-coupled 3'-to-5' DNA helicase activity and recombinational-repair context.",
        "core": [
            {"description": "UvrD/Rep-family ATP-dependent 3'-to-5' DNA helicase.", "molecular_function": TERM["GO:0043138"], "directly_involved_in": [TERM["GO:0000725"]], "support_term": "GO:0043138"},
        ],
    },
    "PP_3691": {
        "accession": "Q88GN0",
        "description": "PP_3691 is a very large DNA2/NAM7-like helicase-related protein in Pseudomonas putida KT2440. The fetched GOA table supports only generic helicase activity, with additional DNA2/NAM7-like, AAA, and restriction-endonuclease-like domains but no resolved organism-specific repair step.",
        "core": [
            {"description": "DNA2/NAM7-like helicase-related protein.", "molecular_function": TERM["GO:0004386"], "support_term": "GO:0004386"},
        ],
    },
    "PP_4448": {
        "accession": "Q88EL4",
        "description": "PP_4448 is a HerA-like central-domain protein with P-loop NTPase domain evidence but no GOA rows. The first pass records it as a boundary candidate without asserting helicase or DNA-repair GO terms from the domain name alone.",
        "core": [],
    },
    "radA": {
        "accession": "Q88E24",
        "description": "radA encodes a RadA-family DNA repair protein in Pseudomonas putida KT2440. HAMAP, NCBIfam, InterPro, and GOA support an ATP-dependent DNA damage sensor/branched-DNA-processing protein involved in recombinational repair, with damaged-DNA binding and cytosolic context.",
        "core": [
            {"description": "ATP-dependent RadA DNA-damage sensor and recombinational-repair factor.", "molecular_function": TERM["GO:0140664"], "directly_involved_in": [TERM["GO:0000725"], TERM["GO:0006281"]], "locations": [TERM["GO:0005829"]], "support_term": "GO:0140664"},
            {"description": "Damaged-DNA binding associated with RadA repair activity.", "molecular_function": TERM["GO:0003684"], "directly_involved_in": [TERM["GO:0000725"]], "support_term": "GO:0003684"},
        ],
    },
    "recN": {
        "accession": "Q88DU0",
        "description": "recN encodes a RecN-family SMC-like DNA repair/recombination protein in Pseudomonas putida KT2440. UniProt/PANTHER evidence supports recombinational repair of damaged DNA and bacterial-nucleoid localization, while ATP binding is the only current molecular-function row.",
        "core": [
            {"description": "RecN-family DNA repair and recombination factor acting in bacterial nucleoid context.", "directly_involved_in": [TERM["GO:0006281"], TERM["GO:0006310"]], "locations": [TERM["GO:0043590"]], "support_term": "GO:0006310"},
        ],
    },
    "PP_5711": {
        "accession": "A0A140FWR4",
        "description": "PP_5711 is an unresolved GajA/Old/RecF-like AAA-domain protein. Current evidence is limited to a Pfam/InterPro AAA-family domain and a ProtNLM-derived product name, so no endonuclease, RecF, or repair GO function is asserted in this first pass.",
        "core": [],
    },
}


GENERIC_REVIEWS = {
    "GO:0000166": ("MARK_AS_OVER_ANNOTATED", "Nucleotide binding is a broad parent term.", "A more informative ATPase/helicase or repair factor annotation is available where function is supported."),
    "GO:0003676": ("MARK_AS_OVER_ANNOTATED", "Nucleic acid binding is too broad.", "The available evidence supports DNA binding or helicase/recombination context where a specific nucleic-acid role is known."),
    "GO:0003677": ("KEEP_AS_NON_CORE", "DNA binding is retained as supporting context.", "DNA binding is expected for DNA repair/helicase proteins but is less informative than the specific ATPase, helicase, nuclease, or repair process."),
    "GO:0004386": ("ACCEPT", "Helicase activity is supported by UniProt/domain metadata.", "The protein has helicase product, keyword, InterPro/Pfam, or PANTHER support; more directional terms are preferred where present."),
    "GO:0005524": ("KEEP_AS_NON_CORE", "ATP binding is retained as non-core cofactor/substrate binding.", "ATP binding supports the ATPase/helicase machinery but is less informative than ATP hydrolysis or DNA-acting activity."),
    "GO:0005737": ("ACCEPT", "Cytoplasm localization is plausible for bacterial DNA repair proteins.", "Bacterial chromosomal DNA repair/recombination factors act in the cytoplasm/nucleoid context."),
    "GO:0005829": ("ACCEPT", "Cytosol localization is retained as broad bacterial cytosolic context.", "The annotation is compatible with soluble DNA repair/recombination factors."),
    "GO:0006259": ("MARK_AS_OVER_ANNOTATED", "DNA metabolic process is too broad.", "The reviewed evidence supports more specific nuclease, helicase, repair, or recombination context."),
    "GO:0006260": ("KEEP_AS_NON_CORE", "DNA replication is retained as shared repair/replication context.", "Several proteins process replication-associated DNA structures, but the split is not primary replisome curation."),
    "GO:0006281": ("ACCEPT", "DNA repair is supported for this repair/recombination candidate.", "The protein's family or UniProt keyword evidence places it in DNA repair context."),
    "GO:0009432": ("KEEP_AS_NON_CORE", "SOS response is retained as non-core damage-response context.", "SOS induction or association does not by itself define the direct molecular function."),
    "GO:0016787": ("MARK_AS_OVER_ANNOTATED", "Hydrolase activity is too broad.", "Specific ATPase, helicase, or nuclease terms are more informative where supported."),
    "GO:0016818": ("MARK_AS_OVER_ANNOTATED", "Acid-anhydride hydrolase activity is a broad parent.", "Specific ATP hydrolysis or helicase function is more informative."),
    "GO:0016887": ("KEEP_AS_NON_CORE", "ATP hydrolysis activity is retained as ATPase context.", "ATP hydrolysis supports helicase/ATPase machinery but may be less informative than directional DNA helicase terms."),
    "GO:0046872": ("KEEP_AS_NON_CORE", "Metal ion binding is retained as cofactor context.", "The metal-binding annotation supports cofactor use but is not the primary repair function."),
    "GO:0008270": ("KEEP_AS_NON_CORE", "Zinc ion binding is retained as domain/cofactor context.", "Zinc/SWIM or zinc-ribbon context supports the protein family but does not define the repair function."),
}


GENE_REVIEWS = {
    "PP_1061": {
        "GO:0008094": ("KEEP_AS_NON_CORE", "ATP-dependent activity acting on DNA is compatible but broad.", "Lhr-like helicase activity is the more informative functional call."),
    },
    "PP_1103": {
        "GO:0004386": ("KEEP_AS_NON_CORE", "Generic helicase activity is correct but less precise.", "The experimentally supported terms are ATP hydrolysis, 3'-5' DNA helicase activity, and 3'-5' DNA/RNA helicase activity."),
        "GO:0008094": ("KEEP_AS_NON_CORE", "ATP-dependent activity acting on DNA is correct but broad.", "The Lhr-Core biochemical paper supports a more precise 3'-to-5' helicase/translocase function."),
        "GO:0016887": ("ACCEPT", "ATP hydrolysis activity is experimentally supported.", "The Lhr-Core paper reports ssDNA-dependent ATPase/dATPase activity."),
        "GO:0033679": ("ACCEPT", "3'-5' DNA/RNA helicase activity is experimentally supported.", "Lhr-Core unwinds DNA duplexes and RNA:DNA hybrids with 3'-ssDNA loading tails."),
        "GO:0043138": ("ACCEPT", "3'-5' DNA helicase activity is experimentally supported.", "The Lhr-Core paper directly reports ATP-dependent 3'-to-5' helicase activity."),
    },
    "PP_1106": {
        "GO:0004521": ("MARK_AS_OVER_ANNOTATED", "RNA endonuclease activity is not well supported for this protein.", "The local metadata support a metallo-beta-lactamase/Xnuc_lig-associated predicted nuclease context, not a resolved RNA endonuclease function."),
    },
    "dinG": {
        "GO:0003678": ("KEEP_AS_NON_CORE", "DNA helicase activity is correct but less precise.", "The HAMAP-supported directional term is 5'-3' DNA helicase activity."),
        "GO:0033677": ("KEEP_AS_NON_CORE", "DNA/RNA helicase activity is retained as family context.", "DinG-family proteins can act on R-loops, but the core KT2440 call is the supported 5'-3' DNA helicase activity."),
        "GO:0043139": ("ACCEPT", "5'-3' DNA helicase activity is supported.", "HAMAP/UniProt describes DinG as a DNA-dependent ATPase and 5'-3' DNA helicase."),
        "GO:0051539": ("ACCEPT", "4Fe-4S cluster binding is supported.", "HAMAP/UniProt records an Fe-S cluster for DinG."),
    },
    "rdgC": {
        "GO:0000018": ("ACCEPT", "Regulation of DNA recombination is supported by RdgC-family evidence.", "RdgC is a recombination-associated DNA-binding protein and this process captures its regulatory context."),
        "GO:0003690": ("ACCEPT", "Double-stranded DNA binding is supported.", "TreeGrafter/HAMAP/domain evidence identifies RdgC as a dsDNA-binding recombination-associated protein."),
        "GO:0006310": ("ACCEPT", "DNA recombination is supported.", "RdgC-family evidence places this protein in recombination context."),
        "GO:0009295": ("KEEP_AS_NON_CORE", "Nucleoid is retained as localization context.", "Bacterial nucleoid/cytoplasm localization is plausible but secondary to the dsDNA-binding recombination role."),
        "GO:0043590": ("ACCEPT", "Bacterial nucleoid localization is retained.", "The protein acts on chromosomal DNA substrates in the bacterial nucleoid context."),
    },
    "PP_1937": {
        "GO:0006281": ("ACCEPT", "DNA repair is supported as the process context.", "SNF2-family helicase metadata and GOA place this protein in DNA repair context."),
        "GO:0031297": ("KEEP_AS_NON_CORE", "Replication fork processing is retained as non-core family context.", "The term is plausible for an SNF2-like repair protein but is more specific than current KT2440 evidence resolves."),
        "GO:0004386": ("NEW", "Helicase activity is added from local domain/product metadata.", "UniProt/Asta support a SNF2-like helicase-family protein, while the fetched GOA table lacks a specific helicase MF row."),
    },
    "sbcC": {
        "GO:0006302": ("ACCEPT", "Double-strand break repair is supported for SbcCD.", "SbcCD processes hairpin and double-stranded DNA structures in repair/recombination contexts."),
        "GO:0016887": ("ACCEPT", "ATP hydrolysis activity is the SbcC ATPase function.", "SbcC is the ATPase/SMC-like subunit of SbcCD."),
    },
    "sbcD": {
        "GO:0004519": ("ACCEPT", "Endonuclease activity is supported.", "SbcD is the nuclease subunit of the SbcCD DNA-structure-processing complex."),
        "GO:0008408": ("ACCEPT", "3'-5' exonuclease activity is supported.", "SbcCD has 3'-to-5' exonuclease activity on DNA structures."),
    },
    "uup": {
        "GO:0016887": ("ACCEPT", "ATP hydrolysis activity is supported for Uup.", "HAMAP/UniProt supports Uup as an ABCF-family ATPase."),
        "GO:0003677": ("KEEP_AS_NON_CORE", "DNA binding is retained as secondary context.", "HAMAP supports DNA binding but the protein also has ribosome-binding context and an unresolved primary process."),
        "GO:0006281": ("KEEP_AS_NON_CORE", "DNA repair is retained as possible postreplication-gap context.", "Uup may resolve branched DNA intermediates, but the record also foregrounds ribosome assembly/function."),
        "GO:0043022": ("ACCEPT", "Ribosome binding is supported.", "HAMAP states that Uup associates with ribosomes, making this a specific supported binding annotation."),
    },
    "PP_2146": {
        "GO:0004386": ("NEW", "Helicase activity is added from local UniProt metadata.", "SNF2/RAD54-family domains and product metadata support a helicase-family activity, while the fetched GOA block lacks a helicase MF row."),
    },
    "PP_2565": {
        "GO:0003678": ("KEEP_AS_NON_CORE", "DNA helicase activity is correct but less precise.", "The directional 3'-5' DNA helicase term is more informative."),
        "GO:0004386": ("KEEP_AS_NON_CORE", "Generic helicase activity is correct but less precise.", "The directional 3'-5' DNA helicase term is more informative."),
        "GO:0000725": ("ACCEPT", "Recombinational repair is supported as process context.", "TreeGrafter and UvrD/Rep-family context support recombinational repair involvement."),
        "GO:0043138": ("ACCEPT", "3'-5' DNA helicase activity is supported.", "UniProt EC/GO and UvrD/Rep domains support this directional helicase activity."),
    },
    "PP_3681": {
        "GO:0003678": ("KEEP_AS_NON_CORE", "DNA helicase activity is correct but less precise.", "The directional 3'-5' DNA helicase term is more informative."),
        "GO:0004386": ("KEEP_AS_NON_CORE", "Generic helicase activity is correct but less precise.", "The directional 3'-5' DNA helicase term is more informative."),
        "GO:0000725": ("ACCEPT", "Recombinational repair is supported as process context.", "TreeGrafter and UvrD/Rep-family context support recombinational repair involvement."),
        "GO:0043138": ("ACCEPT", "3'-5' DNA helicase activity is supported.", "UniProt EC/GO and UvrD/Rep domains support this directional helicase activity."),
    },
    "PP_3691": {
        "GO:0004386": ("ACCEPT", "Helicase activity is retained.", "DNA2/NAM7-like helicase-family domains support a conservative generic helicase call."),
    },
    "radA": {
        "GO:0000725": ("ACCEPT", "Recombinational repair is supported.", "RadA-family evidence supports repair of recombination intermediates and DNA breaks."),
        "GO:0003677": ("KEEP_AS_NON_CORE", "DNA binding is retained as broad binding context.", "Damaged-DNA binding and ATP-dependent DNA damage sensor activity are more informative."),
        "GO:0003684": ("ACCEPT", "Damaged DNA binding is supported.", "InterPro/GOA and RadA-family context support damaged-DNA binding."),
        "GO:0006281": ("ACCEPT", "DNA repair is supported.", "RadA is a DNA repair protein involved in damaged DNA and recombination intermediates."),
        "GO:0140664": ("ACCEPT", "ATP-dependent DNA damage sensor activity is supported.", "InterPro/GOA and RadA-family evidence support this specific molecular function."),
    },
    "recN": {
        "GO:0005524": ("KEEP_AS_NON_CORE", "ATP binding is retained as non-core RecN ATPase-family context.", "The process annotations better describe the RecN repair/recombination role."),
        "GO:0006281": ("ACCEPT", "DNA repair is supported.", "RecN-family evidence places this protein in DNA repair."),
        "GO:0006310": ("ACCEPT", "DNA recombination is supported.", "RecN is a recombination protein and the InterPro GOA row supports DNA recombination."),
        "GO:0009432": ("KEEP_AS_NON_CORE", "SOS response is retained as non-core regulatory context.", "SOS association is plausible but does not define RecN's direct function."),
        "GO:0043590": ("ACCEPT", "Bacterial nucleoid localization is retained.", "RecN acts on chromosomal DNA repair/recombination substrates."),
    },
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def optional_first_line(path: Path, *needles: str) -> str | None:
    if not path.exists():
        return None
    for line in read_text(path).splitlines():
        if all(needle in line for needle in needles):
            return line
    return None


def prefixed_lines(path: Path, prefix: str, limit: int = 4) -> list[str]:
    if not path.exists():
        return []
    return [line for line in read_text(path).splitlines() if line.startswith(prefix)][:limit]


def support(reference_id: str, text: str | None) -> dict[str, str] | None:
    if not text:
        return None
    return {"reference_id": reference_id, "supporting_text": text}


def add_unique(items: list[dict[str, str]], item: dict[str, str] | None) -> None:
    if item and item not in items:
        items.append(item)


def file_id(gene: str, suffix: str) -> str:
    return f"file:PSEPK/{gene}/{gene}-{suffix}"


def goa_support(gene: str, term_id: str | None) -> dict[str, str] | None:
    if not term_id:
        return None
    return support(file_id(gene, "goa.tsv"), optional_first_line(GENE_ROOT / gene / f"{gene}-goa.tsv", term_id))


def pub_support(pmid: str, *needles: str) -> dict[str, str] | None:
    path = ROOT / "publications" / f"{pmid.replace(':', '_')}.md"
    return support(pmid, optional_first_line(path, *needles))


def uniprot_evidence(gene: str, term_id: str | None = None) -> list[dict[str, str]]:
    path = GENE_ROOT / gene / f"{gene}-uniprot.txt"
    items: list[dict[str, str]] = []
    add_unique(items, support(file_id(gene, "uniprot.txt"), optional_first_line(path, "DE   RecName")))
    add_unique(items, support(file_id(gene, "uniprot.txt"), optional_first_line(path, "DE   SubName")))
    if term_id:
        add_unique(items, support(file_id(gene, "uniprot.txt"), optional_first_line(path, f"DR   GO; {term_id};")))
    for marker in (
        "CC   -!- FUNCTION:",
        "CC   -!- CATALYTIC ACTIVITY:",
        "CC   -!- COFACTOR:",
        "CC   -!- SUBCELLULAR LOCATION:",
        "CC   -!- SIMILARITY:",
        "DR   PANTHER;",
        "DR   Pfam;",
        "KW   ",
        "FT   DOMAIN",
    ):
        line = optional_first_line(path, marker)
        if line and "Reference proteome" not in line:
            add_unique(items, support(file_id(gene, "uniprot.txt"), line))
    for line in prefixed_lines(path, "DR   InterPro;", 6):
        add_unique(items, support(file_id(gene, "uniprot.txt"), line))
    return items


def asta_evidence(gene: str) -> list[dict[str, str]]:
    path = GENE_ROOT / gene / f"{gene}-deep-research-asta.md"
    items: list[dict[str, str]] = []
    if not path.exists():
        return items
    for marker in ("  uniprot_accession:", "  protein_description:", "  protein_family:", "  protein_domains:"):
        line = optional_first_line(path, marker)
        if line and "Not specified in UniProt" not in line:
            add_unique(items, support(file_id(gene, "deep-research-asta.md"), line))
    return items


def standard_support(gene: str, term_id: str | None = None) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    add_unique(items, goa_support(gene, term_id))
    for item in uniprot_evidence(gene, term_id):
        add_unique(items, item)
    for item in asta_evidence(gene):
        add_unique(items, item)
    if gene == "PP_1103":
        add_unique(items, pub_support("PMID:30224353", "P. putida Lhr-Core is an ssDNA-dependent ATPase"))
        add_unique(items, pub_support("PMID:30224353", "ATP-dependent 3'-to-5' helicase"))
    return items


def reference_list(existing_refs: list[dict] | None, gene: str, accession: str) -> list[dict]:
    refs: list[dict] = []
    seen = set()
    for ref in existing_refs or []:
        seen.add(ref["id"])
        refs.append(ref)
    for ref_id, title in {
        file_id(gene, "goa.tsv"): f"QuickGO GOA annotations for {gene} ({accession})",
        file_id(gene, "uniprot.txt"): f"UniProtKB entry for {gene} ({accession})",
        file_id(gene, "deep-research-asta.md"): f"Asta retrieval report for {gene} ({accession})",
    }.items():
        if ref_id not in seen and (GENE_ROOT / gene / ref_id.split("/")[-1]).exists():
            refs.append({"id": ref_id, "title": title, "findings": []})
            seen.add(ref_id)
    for pub_id in GENE_INFO[gene].get("pubs", []):
        if pub_id not in seen:
            refs.append({"id": pub_id, "title": PUBS[pub_id], "findings": []})
    return refs


def review_for_annotation(gene: str, term_id: str) -> dict:
    action, summary, reason = GENE_REVIEWS.get(gene, {}).get(term_id) or GENERIC_REVIEWS[term_id]
    return {
        "summary": summary,
        "action": action,
        "reason": reason,
        "supported_by": standard_support(gene, term_id),
    }


def new_annotation(gene: str, term_id: str) -> dict:
    return {
        "term": TERM[term_id],
        "evidence_type": "IEA",
        "original_reference_id": file_id(gene, "uniprot.txt"),
        "qualifier": "enables",
        "review": review_for_annotation(gene, term_id),
    }


def core_functions(gene: str) -> list[dict]:
    cores = []
    for item in GENE_INFO[gene]["core"]:
        core = {"description": item["description"], "supported_by": standard_support(gene, item.get("support_term"))}
        for key in ("molecular_function", "directly_involved_in", "locations"):
            if key in item:
                core[key] = item[key]
        cores.append(core)
    return cores


def apply_review(gene: str) -> None:
    info = GENE_INFO[gene]
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(read_text(path))
    data["gene_symbol"] = gene
    data["status"] = "DRAFT"
    data["description"] = info["description"]
    data["references"] = reference_list(data.get("references"), gene, info["accession"])
    existing = data.get("existing_annotations") or []
    for annotation in existing:
        annotation["review"] = review_for_annotation(gene, annotation["term"]["id"])
    for term_id in info.get("new_terms", []):
        if term_id not in {annotation["term"]["id"] for annotation in existing}:
            existing.append(new_annotation(gene, term_id))
    data["existing_annotations"] = existing
    data["core_functions"] = core_functions(gene)
    data["proposed_new_terms"] = []
    data["suggested_questions"] = suggested_questions(gene)
    data["suggested_experiments"] = suggested_experiments(gene)
    path.write_text(yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, width=120), encoding="utf-8")


def suggested_questions(gene: str) -> list[dict[str, object]]:
    text = {
        "PP_0152": "Is PP_0152 a genuine Holliday-junction-associated factor or an unrelated DUF2388/signal-peptide protein?",
        "PP_1061": "Does full-length PP_1061 Lhr have the same DNA-repair substrate profile as characterized Lhr/Lhr-Core helicases?",
        "PP_1103": "Which KT2440 genes function with Lhr-Core in the proposed DNA repair cluster?",
        "PP_1106": "Is PP_1106 a DNA exonuclease, an RNA endonuclease, or a noncanonical metallo-beta-lactamase-family nuclease?",
        "dinG": "Which DNA secondary structures require DinG in KT2440 stress or replication-restart conditions?",
        "PP_1410": "Does PP_1410 have any ATPase/helicase activity despite lacking a canonical helicase domain in the fetched metadata?",
        "rdgC": "What recombination intermediates or nucleoid sites are bound by KT2440 RdgC?",
        "PP_1937": "Does PP_1937 act as a SNF2-like DNA repair ATPase at stalled replication forks?",
        "sbcC": "Which DNA hairpin or double-strand-break substrates are processed by the KT2440 SbcCD complex?",
        "sbcD": "Does KT2440 SbcD provide both the endonuclease and 3'-5' exonuclease activities inferred from family evidence?",
        "uup": "Is KT2440 Uup primarily ribosome-associated, branched-DNA-associated, or bifunctional?",
        "PP_2146": "Which substrate or chromosomal context recruits the PP_2146 SNF2/RAD54-family protein?",
        "PP_2298": "Does PP_2298 have ATPase activity or any DNA-repair phenotype despite only DUF6388 support?",
        "PP_2565": "Is PP_2565 a UvrD/Rep-family recombinational-repair helicase or a plasmid/mobile-element helicase?",
        "PP_3681": "Is PP_3681 a UvrD/Rep-family recombinational-repair helicase or a pathway-specific backup helicase?",
        "PP_3691": "What substrate specificity is associated with the large DNA2/NAM7-like PP_3691 helicase-related protein?",
        "PP_4448": "Does PP_4448 form a HerA-like ATPase/helicase complex in KT2440?",
        "radA": "Which RadA-dependent branched-DNA or double-strand-break repair phenotypes are visible in KT2440?",
        "recN": "How does RecN contribute to KT2440 double-strand-break repair and SOS recovery?",
        "PP_5711": "Is PP_5711 a functional GajA/Old/RecF-like nuclease/ATPase or only a remote AAA-domain protein?",
    }[gene]
    return [{"question": text, "experts": []}]


def suggested_experiments(gene: str) -> list[dict[str, str]]:
    return [
        {
            "experiment_type": "genetic and biochemical validation",
            "description": f"Test a {gene} deletion strain for DNA-damage sensitivity and, where a catalytic activity is predicted, assay purified protein on defined DNA or nucleic-acid substrates.",
        }
    ]


def write_notes(gene: str) -> None:
    info = GENE_INFO[gene]
    path = GENE_ROOT / gene / f"{gene}-notes.md"
    support_term = info["core"][0].get("support_term") if info["core"] else None
    evidence = standard_support(gene, support_term)
    lines = [
        f"# {gene} notes",
        "",
        "2026-07-10: First-pass repair-helicase/recombination split curation.",
        info["description"],
        "",
        "Primary provenance:",
    ]
    seen = set()
    for item in evidence:
        key = (item["reference_id"], item["supporting_text"])
        if key in seen:
            continue
        seen.add(key)
        lines.append(f"- [{item['reference_id']} \"{item['supporting_text']}\"]")
        if len(seen) >= 10:
            break
    lines.extend(["", "Decision: curate conservatively inside the repair-helicase/recombination boundary; do not promote ProtNLM-only names to GO functions.", ""])
    path.write_text("\n".join(lines), encoding="utf-8")


def annoton(annoton_id: str, gene: str, term_id: str, role: str, processes: list[str] | None = None) -> dict:
    data = {
        "id": annoton_id,
        "label": f"{gene}: {TERM[term_id]['label']}",
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "function": {"preferred_term": TERM[term_id]["label"], "term": TERM[term_id]},
        "role_description": role,
    }
    if processes:
        data["processes"] = [{"preferred_term": TERM[p]["label"], "term": TERM[p]} for p in processes]
    return data


def write_module_extension() -> None:
    data = yaml.safe_load(read_text(MODULE_PATH))
    evidence = data.setdefault("evidence", [])
    source_id = f"file:{BATCH_TSV}"
    if not any(item.get("source_id") == source_id for item in evidence):
        evidence.append(
            {
                "source_id": source_id,
                "title": "PSEPK repair-helicase/recombination-core split table",
                "statement": "The split table records the 20 broad DNA-repair/recombination candidates reviewed as supplemental boundary context for the homologous-recombination module.",
            }
        )
    notes = data.get("notes", "")
    addition = " The 2026-07-10 repair-helicase/recombination split adds supplemental Lhr/DinG/UvrD-like helicases, SbcCD, RdgC, RadA, RecN, Uup, and unresolved low-evidence boundary candidates; ProtNLM-only names are not promoted to module functions."
    if "repair-helicase/recombination split" not in notes:
        data["notes"] = (notes + addition).strip()

    parts = data["module"].setdefault("parts", [])
    parts[:] = [part for part in parts if part.get("node", {}).get("id") != "supplemental_repair_helicase_recombination_candidates"]
    parts.append(
        {
            "order": 5,
            "role": "Supplemental repair helicases, SbcCD, and recombination boundary candidates",
            "node": {
                "id": "supplemental_repair_helicase_recombination_candidates",
                "label": "Supplemental repair-helicase and recombination candidates",
                "module_type": "BIOLOGICAL_PROCESS",
                "annotons": [
                    annoton("pp1103_lhr_core_helicase", "PP_1103", "GO:0043138", "Experimentally characterized Lhr-Core 3'-to-5' DNA/RNA:DNA helicase.", ["GO:0006281"]),
                    annoton("ding_5_3_helicase", "dinG", "GO:0043139", "DinG-family 5'-to-3' DNA helicase for repair/restart substrates.", ["GO:0006281"]),
                    annoton("pp1061_lhr_like_helicase", "PP_1061", "GO:0004386", "Full-length Lhr-like helicase candidate.", ["GO:0006281"]),
                    annoton("pp2565_uvrd_rep_helicase", "PP_2565", "GO:0043138", "UvrD/Rep-family 3'-to-5' DNA helicase candidate.", ["GO:0000725"]),
                    annoton("pp3681_uvrd_rep_helicase", "PP_3681", "GO:0043138", "Second UvrD/Rep-family 3'-to-5' DNA helicase candidate.", ["GO:0000725"]),
                    annoton("pp1937_snf2_like_helicase", "PP_1937", "GO:0004386", "SNF2-like helicase-family repair candidate.", ["GO:0006281"]),
                    annoton("pp2146_snf2_rad54_helicase", "PP_2146", "GO:0004386", "SNF2/RAD54-family helicase candidate."),
                    annoton("pp3691_dna2_nam7_helicase", "PP_3691", "GO:0004386", "DNA2/NAM7-like helicase-related protein."),
                    annoton("sbcc_sbccd_atpase", "sbcC", "GO:0016887", "SbcCD ATPase/SMC-like subunit.", ["GO:0006302"]),
                    annoton("sbcd_sbccd_nuclease", "sbcD", "GO:0008408", "SbcCD nuclease subunit.", ["GO:0006310"]),
                    annoton("rdgc_recombination_dna_binding", "rdgC", "GO:0003690", "RdgC double-stranded-DNA-binding recombination-associated protein.", ["GO:0006310"]),
                    annoton("rada_damage_sensor", "radA", "GO:0140664", "RadA ATP-dependent DNA damage sensor/recombination factor.", ["GO:0000725", "GO:0006281"]),
                    annoton("recn_recombination_repair", "recN", "GO:0006310", "RecN SMC-like recombination and repair factor.", ["GO:0006281"]),
                    annoton("uup_abcf_atpase_boundary", "uup", "GO:0016887", "Uup ABCF ATPase with possible branched-DNA and ribosome-associated context.", ["GO:0006281"]),
                ],
            },
        }
    )
    MODULE_PATH.write_text(yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, width=120), encoding="utf-8")


def main() -> None:
    for gene in GENE_INFO:
        apply_review(gene)
        write_notes(gene)
    write_module_extension()


if __name__ == "__main__":
    main()
