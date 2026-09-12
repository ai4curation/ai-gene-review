# PIGK (GPI8_HUMAN, Q92643) review notes

## Identity
- HGNC:8965; synonym GPI8. UniProt RecName "GPI-anchor transamidase", AltName "component PIGK, catalytic subunit"; EC 2.6.1.- (transferase).
- 395 aa precursor; signal peptide 1-27 (cleaved after Ala-27); chain 28-395. Single-pass type I ER membrane protein: lumenal 28-368, TM 369-385, cytoplasmic 386-395.
- Peptidase C13 family (legumain-like cysteine protease); MEROPS C13.005; Pfam PF01650 Peptidase_C13; InterPro IPR028361 (GPI_transamidase), IPR001096 (Peptidase_C13).

## Core function (well established)
- Catalytic subunit of the GPI-anchor transamidase (GPI-T) complex, an ER-membrane heteropentamer of PIGK, GPAA1, PIGT, PIGS, PIGU [PMID:35165458 "The GPIT complex is known to be composed of five subunits: PIGK, PIGU, PIGT, PIGS and GPAA1."; PMID:11483512; PMID:12802054].
- GPI-T removes the C-terminal GPI attachment signal peptide (CSP) of nascent proproteins and attaches a preassembled GPI anchor via transamidation, in the ER [PMID:10793132 abstract; PMID:35551457 "The removal of a hydrophobic signal peptide and covalent attachment of GPI at the new carboxyl terminus are catalyzed by an endoplasmic reticulum membrane GPI transamidase complex (GPI-T)"].
- PIGK is the catalytic component; conserved Cys/His residues of a cysteine-protease family generate the carbonyl (acyl-enzyme thioester) intermediate [PMID:10793132 "cysteine and histidine residues of Gpi8p, which are conserved in members of a cysteine protease family, are essential for generation of a carbonyl intermediate... Gpi8p is a catalytic component that cleaves the GPI attachment signal peptide"].
- Catalytic dyad/triad: Cys206 (nucleophile), His164 (proton donor); Asn58 completes a C206-H164-N58 triad [PMID:35165458 "The PIGK subunit functions as the catalytic component, in which we identified a C206-H164-N58 triad that is critical for the transamination reaction."]. C206A and H164A abolish activity (UniProt MUTAGEN, PMID:10793132/35165458/35551457).
- Caspase/legumain-like two-phase mechanism; autoinhibitory loop (231-236) gates activity until proprotein binding [PMID:37684232 full text].
- Disulfide bond Cys92(PIGK)-Cys182(PIGT) is important (not essential) for full activity [PMID:12582175].

## Localization
- ER membrane [PMID:11483512 EXP; UniProt SUBCELLULAR LOCATION SL-0097]. Also detected generically in membrane fraction proteomics (NK-cell membrane proteome, PMID:19946888, HDA GO:0016020).

## Disease
- Bi-allelic PIGK variants cause NEDHCAS (neurodevelopmental disorder with hypotonia and cerebellar atrophy, with or without seizures), MIM:618879, autosomal recessive [PMID:32220290]. An inherited GPI-deficiency disorder (GPIBD).

## Annotation review decisions (summary)
- MF GPI-anchor transamidase activity (GO:0003923): the correct, current GOA MF term. Multiple IDA (PMID:35551457, 37684232), IMP (PMID:10793132), IBA, IEA, TAS -> ACCEPT (core).
- BP attachment of GPI anchor to protein (GO:0016255) and GPI anchored protein biosynthesis (GO:0180046) and GPI anchor biosynthetic process (GO:0006506): ACCEPT (core BP). GO:0180046 is the newer specific BP; keep both.
- CC GPI-anchor transamidase complex (GO:0042765): ACCEPT (part_of complex; multiple IDA). ER membrane (GO:0005789): ACCEPT.
- CC membrane (GO:0016020) HDA: MARK_AS_OVER_ANNOTATED (too general, superseded by ER membrane).
- MF proteolysis (GO:0006508) / peptidase activity (GO:0008233) IEA from Peptidase_C13 domain: KEEP_AS_NON_CORE. PIGK IS a cysteine-protease-like enzyme that cleaves the CSP, so these are not wrong, but they capture only half the transamidation reaction; GPI-anchor transamidase activity is the informative core term.
- MF protein binding (GO:0005515) IPI (many, GPAA1/PIGT/PIGS): MARK_AS_OVER_ANNOTATED per policy (bare protein binding uninformative; captures GPI-T subunit interactions already covered by complex membership).
- MF GPI anchor binding (GO:0034235) contributes_to TAS PMID:10793132: ACCEPT/KEEP_AS_NON_CORE — GPI-T binds the GPI lipid substrate; supported by structure (composite GPI cavity).
