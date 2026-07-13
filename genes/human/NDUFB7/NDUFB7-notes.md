# NDUFB7 (B18) — review notes

UniProt: P17568 (NDUB7_HUMAN). HGNC:7702. Gene ID 4713. NCBI taxon 9606.

## Identity / naming
- NADH dehydrogenase [ubiquinone] 1 beta subcomplex subunit 7; aka Complex I-B18 / CI-B18,
  NADH-ubiquinone oxidoreductase B18 subunit, and (historically) "Cell adhesion protein SQM1"
  from an early cDNA-cloning report [PMID:2302251]. The "cell adhesion" naming is a legacy of the
  original cloning; the protein's established function is as a Complex I accessory subunit.
  [file:human/NDUFB7/NDUFB7-uniprot.txt "AltName: Full=Cell adhesion protein SQM1"]

## Core biology (all VERIFIED against UniProt)
- Accessory (supernumerary) subunit of mitochondrial respiratory chain Complex I
  (NADH:ubiquinone oxidoreductase), **not** involved in catalysis.
  [file:human/NDUFB7/NDUFB7-uniprot.txt "Accessory subunit of the mitochondrial membrane respiratory"
   ... "that is believed not to be" (involved in catalysis)]
- Complex I transfers electrons from NADH to ubiquinone; the immediate electron acceptor is ubiquinone.
  [file:human/NDUFB7/NDUFB7-uniprot.txt "Complex I functions in the transfer of electrons"]
- Complex I is composed of 45 different subunits.
  [file:human/NDUFB7/NDUFB7-uniprot.txt "Complex I is composed of 45 different subunits"]
- Subcellular location: Mitochondrion inner membrane (peripheral membrane protein);
  Mitochondrion intermembrane space.
  [file:human/NDUFB7/NDUFB7-uniprot.txt "Mitochondrion inner membrane" / "Mitochondrion intermembrane space"]
- Twin-CX9C: contains two C-X9-C motifs (residues 59-69 and 80-90) forming a helix-coil-helix (CHCH)
  domain (56-98) with two intramolecular disulfide bonds (Cys59-Cys90, Cys69-Cys80); imported/oxidatively
  folded via the MIA40 (CHCHD4) disulfide relay of the IMS.
  [file:human/NDUFB7/NDUFB7-uniprot.txt "Contains two C-X9-C motifs that are predicted to form a helix-"]
- N-terminal N-myristoyl glycine lipid modification at residue 2 (INIT_MET removed).
  [file:human/NDUFB7/NDUFB7-uniprot.txt "N-myristoyl glycine"]
- SIMILARITY: complex I NDUFB7 subunit family. Structures: 5XTC/5XTD/5XTH, 9CWT, 9I4I, 9TI4 (cryo-EM).

## Key experimental support
- **IMS-surface localization** — NDUFB7 and NDUFA8 localize to the intermembrane-space surface of
  Complex I; Cx9C subunits proposed to stabilize the membrane domain via intramolecular disulfides.
  [PMID:21310150 "NDUFB7 and NDUFA8 are located at the intermembrane surface of complex I"]
  (This paper's title/abstract is explicitly about NDUFB7 — HIGH relevance, VERIFIED.)
- **Complex membership (MS)** — identified as a subunit by immunopurification + MS of human Complex I.
  [PMID:12611891 "subunit composition of the human NADH dehydrogenase"]
- **Complex membership (structure)** — cryo-EM of human megacomplex I2III2IV2 assigns individual CI subunits.
  [PMID:28844695 "precise assignment of individual subunits of"]
- **Accessory-subunit importance** — systematic accessory-subunit KO/proteomics: accessory subunits are
  integral for assembly and function; loss destabilizes co-module subunits.
  [PMID:27626371 "Accessory subunits are integral for assembly and function of human mitochondrial"]
- **Disease (MC1DN39)** — biallelic intronic variant c.113-10C>G reduced NDUFB7 protein and reduced
  Complex I activity; WT-NDUFB7 complementation normalized CI function. Congenital lactic acidosis +
  hypertrophic cardiomyopathy, fatal.
  [PMID:33502047 "reduction of the NDUFB7 protein and reduced complex I activity"]
  This IMP demonstrates NDUFB7 is REQUIRED for holoenzyme activity — not that the subunit itself
  catalyzes NADH dehydrogenase activity.

## Curation decisions (rationale)
- **MF**: honest subunit-level MF is **GO:0005198 structural molecule activity**.
  The complex-level catalytic activity **GO:0008137 (NADH dehydrogenase (ubiquinone) activity)** is
  recorded via **contributes_to_molecular_function** (NOT direct enables).
  - Both direct `enables GO:0008137` annotations (IMP PMID:33502047; NAS PMID:9878551) →
    **MARK_AS_OVER_ANNOTATED** (non-catalytic accessory subunit; per policy IMP is not REMOVEd).
- **BP core**: GO:0006120 (electron transport, NADH→ubiquinone) ACCEPT; plus GO:0032981
  (mitochondrial respiratory chain complex I assembly) added to core_functions (assembly role).
  - GO:0009060 aerobic respiration (NAS) → KEEP_AS_NON_CORE (correct but general).
  - GO:0042776 ATP synthesis (NAS) and GO:1902600 proton transmembrane transport (IEA) →
    MARK_AS_OVER_ANNOTATED (downstream / core-membrane-subunit-driven, not this subunit).
- **CC**: part_of GO:0045271 (respiratory chain complex I) ACCEPT (IDA/IPI/IBA); captured as `in_complex`.
  GO:0005743 inner membrane and GO:0005758 IMS ACCEPT (experimental); captured in `locations`.
  GO:0005739 mitochondrion (IEA/HTP/HDA) and redundant Reactome-TAS inner-membrane rows → KEEP_AS_NON_CORE.
- **MF protein binding** (GO:0005515, IPI, PMID:32296183 HuRI + PMID:32814053 ND interactome):
  both are high-throughput Y2H against non-Complex-I partners → **MARK_AS_OVER_ANNOTATED**
  (uninformative bare "protein binding"; not REMOVEd per policy).

## Provenance notes
- All cited publications in publications/PMID_*.md are abstract-only (full_text_available: false)
  except PMID:32296183, PMID:20833797, PMID:34800366. All supporting_text quotes were grep-verified
  as verbatim single-line substrings of their source.
- No deep-research file generated (per instruction; falcon out of credits).
