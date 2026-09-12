# TRIM5 (TRIM5alpha) review notes

UniProt: Q9C035 (TRIM5_HUMAN), 493 aa. EC=2.3.2.27 (RING-type E3 ubiquitin transferase).
HGNC:16276. Chromosome 11.

## Domain architecture (RBCC/TRIM)
- RING-type zinc finger (15-59) -> E3 ubiquitin ligase activity [UniProt FT; PMID:21734049 RING NMR structure]
- B box-type zinc finger (90-132) -> higher-order multimerization
- Coiled-coil (130-241) -> dimerization/low-order multimerization
- B30.2/PRYSPRY (281-493) -> capsid recognition domain (species-specific restriction)
TRIM5alpha (isoform Alpha, Q9C035-1) is the full-length antiviral isoform; other splice isoforms lack the PRYSPRY domain and are non-restrictive (e.g. Iota is dominant-negative).

## Core functions (from UniProt FUNCTION + experimental papers)
1. Capsid-specific retroviral restriction factor. Blocks infection after entry, before reverse transcription. Recognizes the assembled retroviral capsid lattice via the B30.2/PRYSPRY domain. Restricts N-MLV, EIAV, SIVmac, FIV, BIV (human TRIM5a restricts these; weak vs HIV-1). [UniProt; PMID:17156811; PMID:22291694]
2. Pattern recognition receptor / innate immune sensor of the retroviral capsid lattice. Binding to capsid lattice triggers its RING E3 ligase activity; with UBE2V1-UBE2N (UBC13-UEV1A) it synthesizes unanchored K63-linked polyubiquitin chains that activate the TAK1 (MAP3K7)/TAB2/TAB3 kinase complex by autophosphorylation -> NF-kB and AP-1/MAPK inflammatory gene induction. [PMID:21512573 "TRIM5 is an innate immune sensor for the retrovirus capsid lattice"]
   - PMID:21512573 supports: GO:0038187 PRR activity (IDA), GO:0002218 activation of innate immune response (IDA), GO:0004842 ubiquitin-protein transferase activity (IDA), GO:0070534 protein K63-linked ubiquitination (IDA), GO:0043123 positive reg canonical NF-kB (IMP), GO:0043410 positive reg MAPK cascade (IMP), GO:0031664 regulation of LPS-mediated signaling (IMP).
3. E3 ubiquitin ligase: RING-dependent. Autoubiquitinated (RING/UBE2D2-dependent); monoubiquitinated by TRIM21. Generates K63 chains. EC 2.3.2.27. [UniProt; PMID:18312418]
4. Precision/selective autophagy. TRIM5a is a selective autophagy receptor: directly recognizes HIV-1 capsid protein p24 and delivers it for autophagic degradation; also acts as a platform/regulator assembling ULK1 and Beclin-1 (BECN1) in activated states, activating BECN1 by dissociating it from inhibitors BCL2 and TAB2. Interacts with ULK1, GABARAP/GABARAPL1/GABARAPL2, MAP1LC3A/C, BECN1, SQSTM1. [PMID:25127057 "TRIM5α acts as a selective autophagy receptor... delivered its cognate cytosolic target, a viral capsid protein, for autophagic degradation"]
   - Supports GO:0006914 autophagy (IDA), GO:1990462 omegasome (colocalizes), GO:0030674 protein-macromolecule adaptor activity (IPI), GO:0019901 protein kinase binding (IPI ULK1), GO:0032880 regulation of protein localization (IMP).

## Localization
- Cytoplasm; predominantly in cytoplasmic bodies. [UniProt; PMID:12878161; PMID:20357094; PMID:25127057]
- Colocalizes with proteasomal subunits and SQSTM1/p62 in cytoplasmic bodies. PSMC2 interaction. [PMID:22078707; PMID:20357094]
- Cytoplasmic ribonucleoprotein granule / P-body (GO:0036464 / GO:0000932) reported via SQSTM1 study. [PMID:20357094]
- Nucleus: only "By similarity" (UniProtKB:Q0PF16) - partial nuclear localization when coexpressed with TRIM22/TRIM27. Not a core localization for human TRIM5a.

## Notes on specific annotations
- GO:0003713 transcription coactivator activity (IDA, PMID:23077300, ARUK-UCL): PMID:23077300 is a TRIM-family screen for NF-kB/AP-1/IFN activation; TRIM5 activates TAK1 -> NF-kB. The "transcription coactivator activity" framing is an over-interpretation; TRIM5 acts upstream in signaling, not as a DNA-associated coactivator. MARK_AS_OVER_ANNOTATED.
- GO:0045893 positive regulation of DNA-templated transcription (IEA GO_REF:0000108, inter-ontology from coactivator): inherits from the coactivator over-annotation. MARK_AS_OVER_ANNOTATED.
- GO:0010468 regulation of gene expression (IBA): generic; downstream of NF-kB activation. KEEP_AS_NON_CORE.
- GO:0046596 regulation of viral entry into host cell (IBA): TRIM5 blocks post-entry (uncoating/RT), not entry per se; but family-level IBA. Restriction is better captured by host-mediated suppression of symbiont invasion / defense response to virus. KEEP_AS_NON_CORE / acceptable as restriction-related.
- GO:0044790 suppression of viral release by host (IDA, PMID:18248090): PMID:18248090 screened TRIM late-stage effects; for TRIM5 the dominant validated activity is early (post-entry) restriction. This late-stage "viral release" assignment is weak for TRIM5a. MARK_AS_OVER_ANNOTATED.
- GO:0046597 host-mediated suppression of symbiont invasion (IDA, PMID:18248090): captures the early restriction block. ACCEPT (core restriction).
- GO:0140374 antiviral innate immune response (IDA, PMID:18248090): core. ACCEPT.
- protein binding (GO:0005515) IPI: many are from CFTR interactome screens (PMID:26618866, PMID:35156780), SNAIL/FBXO11 study (PMID:25203322 - this is about SCF-FBXO11/SNAIL, TRIM5 appears as interactor in IntAct), E3-RING dimer screen (PMID:22493164), NOD2/TRIM27 (PMID:22829933). Bare protein binding -> KEEP_AS_NON_CORE (uninformative per guidelines).
- GO:0042802 identical protein binding / GO:0042803 homodimerization: TRIM5 forms homodimers/trimers; multimerization essential for restriction. ACCEPT homodimerization as it is functionally core; identical protein binding redundant -> KEEP_AS_NON_CORE / ACCEPT.
- GO:0008270 zinc ion binding (IEA): correct (RING + B-box coordinate Zn). KEEP_AS_NON_CORE (supports but generic).
- GO:0019901 protein kinase binding: TRIM5 binds TAK1/MAP3K7 and ULK1 (phosphorylated). Functionally meaningful but the informative function is the signaling activation. KEEP_AS_NON_CORE.

## GO IDs verified relevant
- GO:0038187 pattern recognition receptor activity (core MF)
- GO:0061630 ubiquitin protein ligase activity / GO:0004842 ubiquitin-protein transferase activity (core MF)
- GO:0070534 protein K63-linked ubiquitination
- GO:0002218 activation of innate immune response
- GO:0140374 antiviral innate immune response
- GO:0043123 positive regulation of canonical NF-kappaB signal transduction
- GO:0043410 positive regulation of MAPK cascade
- GO:0006914 autophagy
- GO:0042803 protein homodimerization activity
