# mtm-9 (Q965W9) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: first full review of C. elegans MTM-9 (synonym CUP-10, Y39H10A.3). ProtNLM2
outputs were not opened or used.

### Deep research
`just deep-research-falcon worm mtm-9 --fallback perplexity-lite` failed: falcon returned
`403 Forbidden` at authentication, and the perplexity fallback returned `401 insufficient_quota`.
No deep-research file exists; the review uses the cached primary literature and UniProt.

### Evolutionary placement
- PANTHER: PTHR10807:SF73 (LD06050P) [file:worm/mtm-9/mtm-9-uniprot.txt "DR   PANTHER; PTHR10807:SF73; LD06050P; 1."].
  Human MTMR9 (Q96QG7) is in SF56, a separate subfamily. MTM-9 is the only experimentally
  studied SF73 member.
- PAINT (interpro/panther/PTHR10807/PTHR10807-paint.tsv):
  - PTN008506586 (taxon 2759) IBD: PI3P phosphatase activity, PI(3,5)P2 phosphatase activity,
    phosphatidylinositol dephosphorylation (donors: active MTMR6/7/8 group, Arabidopsis MTMs, worm mtm-6 for MF).
  - PTN000086907 (taxon 33213): IRD NOT GO:0004438 and NOT GO:0106018. This is the curator
    marking catalytic loss on the inactive branch. MTM-9 thus receives the process
    (dephosphorylation) but not the catalytic MF terms.
  - PTN002246859 (taxon 6072): IBD protein phosphatase binding and negative regulation of
    autophagy, single donor human MTMR9. The node lies above both SF56 and SF73.
    PAINT did NOT propagate MTMR9's phosphatase activator activity (GO:0019211) or positive regulation
    of phosphatase activity. I treat that omission as deliberate and do not add a NEW activator term.
- Catalytic loop (mtm-9-bioinformatics/RESULTS.md): HGGDGLDS (G346 replaces the nucleophilic
  Cys, S replaces the Arg). Same pattern as human MTMR9 (HGTEGTDS). Worm MTM-6 control has HCSDGWDR (C335).

### Experimental findings in C. elegans
- Fares & Greenwald 2001 [PMID:11560892]: cup-10 identified in the coelomocyte uptake-defective screen (abstract only).
- Dang et al. 2004 [PMID:14565969, full text]: cup-10 = mtm-9; mutants disrupt PI(3)P
  localisation ("both genes are required for PI(3)P localization in vivo") and block
  fluid-phase BSA-Rhod uptake by coelomocytes ("no BSA-Rhod is seen in mtm-6(ar513 ) and
  mtm-9(ar479 ) coelomocytes by the 5-min and 60-min time point"). Co-IP of GFP-MTM-6A and
  Flg-MTM-9 in human 293 cells. MTM-9::GFP is "predominantly localized to the coelomocyte
  cytoplasm" with "some membrane association". MTM-6(C335S) increases MTM-9 membrane
  association. MTM-6(C335S) membrane association does not need MTM-9. MTM-9::GFP
  colocalises with ARF-6 (data not shown).
- Silhankova et al. 2010 [PMID:21076391, abstract only]: mtm-6/mtm-9 mutants have defects in
  Wnt-dependent processes. MTM-6 is required in Wnt-producing cells for MIG-14/Wls recycling.
  The cell-autonomy experiments are described for MTM-6. MTM-9 is inferred to act with it as the complex.
- Ericson et al. 2014 [PMID:25479419, full text]: mtm-9(ok3523) null reduces DA9 GFP::RAB-3
  puncta to the same extent as mtm-6. The double mutant is not more severe, so the two act in one pathway.
  The synapse phenotype is attributed partly to EGL-20 Wnt secretion from tail cells, so it is a downstream organismal readout.
- Maekawa et al. 2014 [PMID:24591580, abstract only]: mammalian MTMR6/MTMR9 needed for macropinocytosis.
  The worm pinocytosis IMP comes from this paper's use of the worm Cup mutants.

### Decisions summary
- Core: non-catalytic partner of MTM-6 (phosphatase binding, IPI) in the MTM-6/MTM-9
  PI-phosphate phosphatase complex. Acts in phosphatidylinositol dephosphorylation and
  fluid-phase endocytosis (pinocytosis) in coelomocytes.
- NOT PI3P phosphatase activity: accept (sequence + PAINT IRD).
- Endocytosis rows: MODIFY to pinocytosis (synonym "fluid-phase endocytosis"; the assays are fluid-phase uptake).
- Synapse assembly (NAS) and negative regulation of autophagy (IBA, human-only donor, SF56):
  marked over-annotated, as downstream readouts with no worm-level participation evidence.
- Regulation of cell migration (IMP): keep as non-core (indirect, via Wnt secretion).
- Apical plasma membrane IDA: UNDECIDED. No MTM-9 apical-membrane observation is in the
  cached text, and coelomocytes are not polarised epithelia. I defer to the curator rather than removing it.
