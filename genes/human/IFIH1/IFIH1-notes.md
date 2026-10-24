# IFIH1 (MDA5) review notes

## Why this gene was selected

MDA5 is annotated in GOA with `GO:0038187 pattern recognition receptor activity` (IDA x2), a term
whose GO definition is "Combining with a pathogen-associated molecular pattern (PAMP), a structure
conserved among microbial species to initiate an innate immune response." A 2026 Nature Immunology
paper reports that during actual virus infection MDA5 is bound not to viral RNA but to host RNA. The
curation question is whether the PAMP-based molecular function term still fits.

## The new result (PMID:42581186, Sampaio et al., Nat Immunol 27:1815-1828, 2026)

Verified on PubMed; DOI 10.1038/s41590-026-02614-3; full text cached.

The authors open by conceding that the ligand has never been pinned down:
[PMID:42581186 "MDA5's RNA agonists are not well defined."]

iCLIP of *endogenous* MDA5 (new monoclonal antibodies) in THP1 and Calu-3 cells infected with EMCV or
SARS-CoV-2:
[PMID:42581186 "upon infection with SARS-CoV-2 or encephalomyocarditis virus, MDA5 bound
overwhelmingly to cellular RNAs"], and more starkly
[PMID:42581186 "We did not detect MDA5 binding sites in viral RNA; instead, MDA5 bound only host
RNA."] Approximately 10% of input reads in SARS-CoV-2-infected cells mapped to the viral genome, yet
there was no enrichment of viral RNA in the MDA5 IP.

The binding sites were intronic and repeat-proximal, and the trigger was removable by fixing splicing:
[PMID:42581186 "overexpression of the splicing factor SRSF3 reduced aberrant transcription and
abrogated MDA5 activation"].

Proposed reframing:
[PMID:42581186 "we propose that MDA5 surveys RNA processing fidelity and can detect infections by
sensing perturbations of post-transcriptional events such as splicing."] and, in the discussion,
[PMID:42581186 "rather than exclusively detecting viral RNA as a PAMP, as is the case with other PRRs,
we propose that MDA5 can also function as a sensor of cellular RNA homeostasis"].

They describe MDA5's status in the field as unresolved:
[PMID:42581186 "the PAMP detected by MDA5 during infection has remained obscure and controversial"].

Crucially, this is a reframing and not a head-to-head rebuttal. The authors say so themselves:
[PMID:42581186 "We cannot exclude the possibility that MDA5 detects viral dsRNAs in different
settings"]. Two cell types, two viruses, one lab.

## What the GOA annotations actually rest on

- `GO:0038187` IDA #1 = PMID:21217758 (Zuest et al., Nat Immunol 2011, verified). Coronaviruses lacking
  2'-O-methyltransferase induce more interferon, and
  [PMID:21217758 "the induction of type I interferon by viruses deficient in 2'-O-methyltransferase
  was dependent on the cytoplasmic RNA sensor Mda5"]. Note the logic: this is discrimination by
  *absence of a host mark*, i.e. missing-self, not detection of a microbe-specific structure.
- `GO:0038187` IDA #2 = PMID:23273991 (Wu et al., Cell 2013, verified; cached entry is abstract-only).
  [PMID:23273991 "MDA5 recognizes the internal duplex structure, whereas RIG-I recognizes the terminus
  of dsRNA"]. Long duplex RNA is a classic PAMP, so this one does support the term as written.
- `GO:0003725` dsRNA binding: IBA + IDA (PMID:19656871) + TAS. Uncontested.

## Independent evidence that MDA5 senses self RNA

- IFIH1 gain-of-function alleles cause sterile interferonopathy:
  [PMID:24686847 "heterozygous mutations in the cytosolic double-stranded RNA receptor gene IFIH1
  (also called MDA5) cause a spectrum of neuroimmunological features consistently associated with an
  enhanced interferon state"], with the mechanism
  [PMID:24686847 "these mutations confer gain of function such that mutant IFIH1 binds RNA more avidly,
  leading to increased baseline and ligand-induced interferon signaling"].
- ADAR1 A-to-I editing exists in part to stop MDA5 responding to endogenous duplexes:
  [PMID:26275108 "embryonic death and phenotypes of Adar1(E861A/E861A) were rescued by concurrent
  deletion of the cytosolic sensor of dsRNA, MDA5"].
- The 2026 paper ties these together:
  [PMID:42581186 "In the absence of ADAR1, which catalyzes the deamination of adenosines to inosines in
  dsRNA to break base-pairing, MDA5 detects cellular dsRNA species"].

## Curation position taken

- `GO:0003725` dsRNA binding -> **ACCEPT**, core. Not in dispute under either model; the host ligands
  identified (inverted Alu repeats, structured introns) are themselves duplexes.
- `GO:0038187` pattern recognition receptor activity -> **ACCEPT**, core, with the dispute recorded in
  full in `reason`. Not REMOVE (two IDAs whose full text I have not read, and the Wu 2013 duplex result
  genuinely is PAMP-like), not MODIFY (no existing MF term describes a receptor for aberrantly
  processed self RNA). The mismatch is with the *wording of the GO term*, not with this gene, so it is
  raised as a `proposed_new_terms` entry ("aberrant cellular RNA sensor activity") and a
  `suggested_questions` item rather than being settled by an edit here.
- `GO:0003677` **DNA binding (IEA) -> REMOVE.** Traced to source: GO_REF:0000002 is InterPro2GO, and
  the InterPro API confirms IPR006935 (Helicase/UvrB, N-terminal; Pfam PF04851 ResIII) maps to
  GO:0003677, GO:0005524 and GO:0016787. That domain family is dominated by DNA-acting enzymes (UvrB,
  type III restriction endonucleases). MDA5 is a cytosolic RNA sensor with no reported direct DNA
  binding; activation by DNA viruses is accepted to be indirect, via RNA. This is exactly the case the
  project rules allow REMOVE for: an electronic inference arguable against on biological grounds.
- `GO:0016787` hydrolase activity (same InterPro source) -> **MODIFY** to GO:0016887.
- `GO:0003724` RNA helicase activity -> **MODIFY** to GO:0008186 (ATP-dependent activity, acting on
  RNA). The GO definition asserts ATP-driven unwinding of an RNA helix. The IMP behind it
  (PMID:19211564) measured ATP hydrolysis and signalling, and reported
  [PMID:19211564 "type I interferon production mediated by full-length MDA5 and RIG-I is independent of
  the helicase domain catalytic activity"]. The ATPase drives filament proofreading, not processive
  unwinding. GO:0016887, which the gene already carries with EXP/IMP evidence, states what was measured.
- `GO:0009597` detection of virus -> **KEEP_AS_NON_CORE**. The BP term most exposed to the iCLIP result.
- `GO:0005634` nucleus (IEA from the UniProt location vocabulary) -> **MARK_AS_OVER_ANNOTATED**.
  UniProt's own nucleus call for IFIH1 is ECO:0000305 and reads "May be found in the nucleus, during
  apoptosis".
- `GO:0016925` protein sumoylation (involved_in) -> **MARK_AS_OVER_ANNOTATED**; MDA5 is the substrate,
  not a component of the conjugation machinery.
- `GO:0005739` mitochondrion -> **KEEP_AS_NON_CORE**; conditional, post-activation relocalisation to
  engage MAVS, not a resident location.
- Bare `GO:0005515` protein binding and `GO:0019904` protein domain specific binding ->
  **MARK_AS_OVER_ANNOTATED**. `GO:0042802` identical protein binding kept as **ACCEPT**, because
  homotypic filament/CARD oligomerisation is mechanistically load-bearing for this protein rather than
  an incidental interaction.

## What I could not resolve

Whether the iCLIP result and the in vitro viral-ligand results are in conflict at all. Purified MDA5
demonstrably binds long viral duplexes; iCLIP reports what MDA5 is crosslinked to inside an infected
cell, where viral RNA may be shielded in replication organelles. The authors themselves argue this is
the resolution rather than a contradiction. I did not find a 2025-26 paper that tests the two models
against each other directly.
