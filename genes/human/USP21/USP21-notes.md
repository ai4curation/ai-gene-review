# USP21 (Q9UK80, UBP21_HUMAN) review notes

NOTE: This is the CORRECT USP21 (UniProt Q9UK80). An earlier batch-6 fetch under the symbol
"USP21" mis-resolved (UniProt synonym collision) to USP25 and was relabeled; this review is
freshly fetched for Q9UK80.

## Identity / overview
- Ubiquitin carboxyl-terminal hydrolase 21 (USP21), a deubiquitinating enzyme (DUB) of the
  peptidase C19 / USP family. EC 3.4.19.12. 565 aa. Gene on chr 1q21. HGNC:12620.
  [file:human/USP21/USP21-uniprot.txt "Belongs to the peptidase C19 family. USP21 subfamily."]
- Catalytic USP domain spans residues 212-558; catalytic nucleophile Cys-221 (mutating to A/S
  abolishes activity); proton-acceptor His-518; a structural Zn(2+) site (C384/C387/C437/C440).
  [file:human/USP21/USP21-uniprot.txt "MUTAGEN 221 ... C->A,S: Abolishes ubiquitin thioesterase activity."]
- Dual subcellular localization: cytoplasm and nucleus; has a CRM1-dependent nuclear export
  signal (motif 134-152). [PMID:21888622 — "A global survey of CRM1-dependent nuclear export
  sequences in the human deubiquitinase family"]

## Core molecular function: cysteine-type deubiquitinase (GO:0004843)
- Originally identified as an isopeptidase with DUAL specificity, removing ubiquitin from
  ubiquitinated proteins AND NEDD8 from NEDD8 conjugates (but NOT SUMO/Sentrin-1). Cys-221
  required. [PMID:10799498 "USP21 is capable of removing ubiquitin from ubiquitinated proteins
  as expected. Furthermore, USP21 is capable of removing NEDD8 from NEDD8 conjugates but has no
  effect on Sentrin-1 conjugates."] -> supports both GO:0004843 (deubiquitinase) and GO:0019784
  (deNEDDylase activity), both IDA.
- Catalytic activity re-confirmed with active-site mapping and Cys-221 mutagenesis.
  [PMID:32011234 — active site, mutagenesis of Cys-221]
- USP21 USP domain crystallized in complex with ubiquitin (PDB 3I3T/2Y5B/3MTN); structural Zn
  site. [PMID:21399617 "Polyubiquitin binding and cross-reactivity in the USP domain
  deubiquitinase USP21."]

## Substrate / process contexts (BP)
1. **Ribosome-associated quality control (RQC), negative regulator.** USP21 (with OTUD3)
   deubiquitinates 40S ribosomal proteins eS10/RPS10 and uS10/RPS20, antagonizing
   ZNF598-mediated 40S ubiquitylation and limiting RQC activation.
   [PMID:32011234 "we identify OTUD3 and USP21 as deubiquitylating enzymes that antagonize
   ZNF598-mediated 40S ubiquitylation and can limit RQC activation"]
   [PMID:32011234 "cells lacking USP21 or OTUD3 have altered RQC activity and delayed eS10
   deubiquitylation indicating a functional role for deubiquitylating enzymes within the RQC
   pathway"]
   This is the IDA-supported BP behind GO:0016579 protein deubiquitination (PMID:32011234).
2. **rDNA silencing / NoRC stabilization.** USP21 deubiquitinates and stabilizes BAZ2A/TIP5
   (a NoRC component), acting with BEND3 to repress rRNA gene transcription.
   [PMID:26100909 "USP21 can interact with and deubiquitinate Tip5, thereby stabilizing the
   total levels of Tip5."] Supports GO:0016579 (IMP/IPI; substrate BAZ2A/TIP5).
3. **Histone H2A deubiquitination / transcription coactivation.** UniProt (By similarity, from
   mouse Q9QZL6) describes deubiquitination of histone H2A relieving repression, acting as a
   transcriptional coactivator and regulating transcription initiation. This underlies the
   ISS terms GO:0003713 (transcription coactivator activity), GO:0045815 (transcription
   initiation-coupled chromatin remodeling) and the GOC IEA GO:0045893 (positive regulation of
   DNA-templated transcription). These are ortholog-transferred (mouse) / inferred, not direct
   human experimental evidence.
   [file:human/USP21/USP21-uniprot.txt "Deubiquitinates histone H2A ... thereby acting as a
   coactivator (By similarity)."]
4. Reported but not in this GOA set: deubiquitination of RIPK1/RIP1 (TNF/NF-kB signaling),
   RIG-I, GATA3, MARK3, ACLY, microtubule/centrosome regulation. Mentioned as prior work in
   PMID:26100909 ("regulate the deubiquitination of several other substrates including RIG-1,
   RIP1, and GATA-3"). These broaden the substrate range but the specific GO BP terms for them
   are not in the seeded GOA.

## Interactions (IPI protein binding annotations)
- All bare GO:0005515 protein binding annotations from high-throughput interactome screens:
  - PMID:19615732 (Sowa et al. DUB interaction landscape) WITH UCHL1 (P09936)
  - PMID:25416956 (HuRI/CCSB Y2H) WITH KRT40 (Q6A162)
  - PMID:32296183 (binary interactome HuRI) WITH EFEMP2/O95967, CPSF6/Q16630-2,
    ADAMTSL4/Q6UY14-3, KCTD9/Q7L273, HOXC10/Q9NYD6
  - PMID:32814053 (neurodegeneration interactome) WITH UCHL1 (P09936)
  - PMID:26100909 IPI WITH BEND3 (Q5T5X7) and BAZ2A (Q9UIF9) — these two are functionally
    meaningful (BEND3 = interactor; BAZ2A/TIP5 = substrate), unlike the generic screen hits.
- Per curation guidelines, bare "protein binding" is uninformative and should not be elevated to
  core. The BEND3/BAZ2A interactions (PMID:26100909) are biologically meaningful but are still
  recorded as bare GO:0005515; they are best captured via the deubiquitination BP context.

## Localization annotations
- Cytoplasm + nucleus, both experimentally supported (PMID:21888622, EXP). HPA IDA: cytosol
  (GO:0005829) and nucleoplasm (GO:0005654). IBA cytoplasm. These are consistent.
- Centrosome (CD-CODE Centrosome cross-ref in UniProt) consistent with reported
  microtubule/centrosome role, but no centrosome GO term is in the seeded GOA.

## Reactome TAS
- Reactome annotations (R-HSA-5688426, -5690157, -5690159, -6783177) place USP21 DUB activity in
  Ub-specific processing protease and TNFR1 signaling pathways (consistent with RIPK1
  deubiquitination role). These are TAS general DUB-activity / localization terms — acceptable as
  curated but non-specific.

## Curation decisions summary
- Core MF: cysteine-type deubiquitinase activity (GO:0004843) — strong IDA/IMP human evidence.
- Secondary MF: deNEDDylase activity (GO:0019784) — IDA, accept (genuine dual specificity).
- BP: protein deubiquitination (GO:0016579) — accept as core process (multiple direct
  substrates: 40S RPs, BAZ2A).
- GO:0008234 cysteine-type peptidase activity — parent of GO:0004843; KEEP_AS_NON_CORE (less
  precise).
- Transcription-related terms (GO:0003713, GO:0045815, GO:0045893) — mouse ISS / inferred;
  KEEP_AS_NON_CORE (real but ortholog-transferred / indirect, not the primary human-demonstrated
  function).
- protein binding (GO:0005515) IPI — KEEP_AS_NON_CORE (records real interactions) or
  MARK_AS_OVER_ANNOTATED for generic screen hits unrelated to function; never core.
- Localizations — ACCEPT (cytosol, nucleoplasm, nucleus, cytoplasm all supported).
</content>
</invoke>
