# TLR9 (human, Q9NR96) review notes

## Deep research status

The Falcon report (`TLR9-deep-research-falcon.md`) arrived after the review was
written; see the cross-check section at the end. The review is built from the
UniProt record, the cached GOA-cited publications, and six additional primary
papers fetched into `publications/` (PMID:11564765, 17932028, 25686612,
18820679, 18931679, 20865800).

## Biology summary with provenance

- **Receptor for CpG DNA.** Mouse knockout: "Here we show that cellular response
  to CpG DNA is mediated by a Toll-like receptor, TLR9." [PMID:11130078]. Human
  TLR9 confers responsiveness: "Cells that are not responsive to CpG DNA become
  responsive when transfected with hTLR9." and "Cells expressing hTLR9 are
  stimulated by CpG motifs that are active in primates but not rodents"
  [PMID:11564765]. So ligand class (unmethylated CpG DNA) is conserved between
  mouse and human, with species differences in the optimal motif; this justifies
  keeping ortholog-transferred GO:0034162 rows.
- **Direct binding.** "We show that CpG DNA binds directly to TLR9 in
  ligand-binding studies." [PMID:14716310]. Structures: "Agonistic-CpG-DNA-bound
  TLR9 formed a symmetric TLR9-CpG-DNA complex with 2:2 stoichiometry, whereas
  iDNA-bound TLR9 was a monomer." [PMID:25686612] (abstract-only; species of the
  crystallized TLR9 not stated in the abstract).
- **Trafficking and location.** ER at rest: "We have found that TLR9 is
  localized to the endoplasmic reticulum (ER) of dendritic cells (DCs) and
  macrophages." [PMID:14716310]. Golgi transit and palmitoylation: "The
  palmitoylation cycle begins in the Golgi, where DHHC3 palmitoylates TLR9 and
  ends in lysosomes, where PPT1 depalmitoylates TLR9." [PMID:38169466].
  Endolysosomal cleavage is required: "The ectodomains of TLR9 and TLR7 are
  cleaved in the endolysosome, such that no full-length protein is detectable in
  the compartment where ligand is recognized." and "conditions that prevent
  receptor proteolysis, including forced TLR9 surface localization, render the
  receptor non-functional." [PMID:18820679]; "Here we show that TLR9 proteolytic
  cleavage is a prerequisite for TLR9 signaling." [PMID:18931679].
- **Surface TLR9 in some cells.** Polarized IECs: "TLR9 activation through
  apical and basolateral surface domains have distinct transcriptional
  responses" [PMID:17128265]; melanocytes express TLR9 protein [PMID:19740627].
  Decision: plasma membrane rows (IBA/IDA/IEA) kept as non-core, not removed.
- **Signalling.** MyD88 recruitment: "TLR9 redistributes from the ER to CpG
  DNA-containing structures, which also accumulate MyD88." [PMID:14716310];
  BTK: "Here we report the endogenous interaction between Brutons's tyrosine
  kinase (Btk) and human TLR8 and TLR9 in the monocytic cell line THP1."
  [PMID:17932028].
- **Outputs in humans.** "We show here that IFN-alpha/beta and -lambda induction
  via TLR-7, TLR-8, and TLR-9 was abolished in IRAK-4-deficient blood cells."
  and this is "paradoxically redundant for protective immunity to most viruses in
  humans." [PMID:16286015]. B cells: "As previously established [34], CpG could
  induce blood B lymphocytes to differentiate into antibody-secreting cells"
  [PMID:23857366].

## Key curation decisions

- Core MF: GO:0038187 pattern recognition receptor activity plus GO:0045322
  unmethylated CpG binding; core BP GO:0034162; core CC endolysosome membrane.
- GO:0032729 type II IFN IDA (PMID:16286015): paper measured IFN-alpha/beta and
  IFN-lambda (type III), not IFN-gamma, in response to TLR9 agonist -> MODIFY to
  GO:0034346 positive regulation of type III interferon production (OLS-verified).
- GO:0035197 siRNA binding IMP (PMID:15723075): abstract-only; abstract attributes
  siRNA sensing to TLR7 ("Immunostimulation by siRNA was absent in TLR7-deficient
  mice."). Left UNDECIDED per the rule on not overruling experimental
  annotations without full text; flagged as a suggested question.
- GO:0005576 extracellular region NAS: REMOVE (type I membrane protein, no
  secreted form; non-experimental).
- GO:0034165 positive regulation of TLR9 signaling (IEA from mouse): REMOVE; the
  receptor is the pathway participant, not a regulator of it.
- Rat-derived IEA oddities (male gonad development, cellular response to LPS,
  cellular response to metal ion): MARK_AS_OVER_ANNOTATED. LPS is the TLR4
  ligand, relevant to the project's ligand-specificity question.
- Downstream cytokine/B-cell/MAPK terms: KEEP_AS_NON_CORE.
- GO:1901895 (SERCA2 inhibition, PMID:24610369): experiments mainly in rat and
  mouse cardiomyocytes; kept as non-core, not overruled.
- No NEW annotations proposed.

## Deep-research cross-check (2026-09-30)

- **Agrees:** unmethylated CpG DNA sensing (core GO:0045322/GO:0038187/GO:0034162);
  CpG DNA as molecular glue for a 2:2 dimer (PMID:25686612); Z-loop cleavage required
  (PMID:18820679, PMID:18931679); ER synthesis, UNC93B1, Golgi transit and
  DHHC3/PPT1 palmitoylation cycle (PMID:38169466 - supports the accepted Golgi membrane
  rows); early-to-late endosome progression shaping NF-kappaB vs IRF7 output;
  MyD88-only signalling; cell-type-restricted surface TLR9 (consistent with keeping
  plasma membrane rows as non-core).
- **Adds (not used for decisions):** ligand-induced Y870/Y980 phosphorylation by
  Syk/EGFR (2025), UNC93B1 N272 glycosylation, surface TLR9 on neutrophils and
  erythrocytes, and a mouse hippocampal role of Tlr9 in memory formation. These are
  single-lab or mouse findings not in GOA and not verified here in a cached primary
  paper; no NEW terms proposed.
- **Conflicts:** none. The report does not address siRNA binding, type II IFN or the
  rat-derived IEA rows.
- **Changes:** no annotation decisions changed. Added the report to `references`
  and cited it as corroborating context on the `GO:0045322` row.

