# Snr1 (Snf5-related 1, BAP45; FBgn0011715; UniProtKB Q24090) review notes

## Scope and sources

- Fetched accession Q24090 (unreviewed TrEMBL entry carrying all 43 GOA rows). The
  UniProt record has no curated FUNCTION text; its domain features are the Pfam
  INI1 DNA-binding domain (PF21459) and SNF5 domain (PF04855).
- Deep research source: the FlyBase hand-written description
  (`Snr1-deep-research-flybase.md`). No Falcon or Perplexity report was run.
- PAINT node placement: `Snr1-bioinformatics/RESULTS.md`.
- Literature queries run (PubMed E-utilities, 2026-11-17): `Snr1 Drosophila` (20 hits
  screened), `SNR1 Drosophila brahma` (16 hits), `Snr1 tumor suppressor Drosophila
  imaginal`; web search for the Snr1 tumour suppressor and endosomal trafficking paper.
  Papers added to the cache for this review: PMID:27923836, PMID:37294080,
  PMID:22467207, PMID:16990270, PMID:15454538, PMID:12645932, PMID:17640523.

## Identity and complex membership

- Snr1 was identified as the fly SNF5 homolog and co-purifies with Brm in a >2 MDa
  complex [PMID:7579694 "The snr1 and brm proteins are present in a large (> 2 x 10(6) Da) complex, and they co-immunoprecipitate from Drosophila extracts."].
- Flies have two Brahma complexes, BAP (OSA) and PBAP (Polybromo, BAP170, SAYP), which
  share seven core subunits [PMID:15060132 "Biochemical analysis established that Drosophila contains two distinct BRM complexes"]
  [PMID:18299390 "Both complexes share seven core subunits, including the Brahma ATPase, but differ in a few signature subunits"].
  Snr1 is in the common core [PMID:33799739 "A common core complex includes Brahma"].
- The fly BRM complex lacks the subunit heterogeneity of the human complexes
  [PMID:9735357 "The BRM complex is even more highly related to the human BRG1 and hBRM complexes, but lacks the subunit heterogeneity characteristic of these complexes."].
- Snr1 is not required in every tissue that needs Brm: it was proposed to be an
  optional, targeting subunit [PMID:12645932 "Thus, SNR1 is essential for some, but not all Brm functions, and it likely serves as an optional subunit, directing Brm complex activity to specific gene loci or cellular processes."].

## Activation and repression

- Coactivator side: the purified BRM complex is essential for Zeste-directed activation
  on chromatin in vitro [PMID:10809665 "Reconstituted transcription reactions established that the Brahma (BRM) chromatin-remodeling complex is essential for Zeste-directed activation on nucleosomal templates."];
  Akirin recruits BAP to a subset of Relish target genes [PMID:25180232 "Akirin orchestrates NF-κB transcriptional selectivity through the recruitment of the Osa-containing-SWI/SNF-like Brahma complex (BAP)"]
  (the PMC full text reports that RNAi of snr-1, like that of the other BAP subunits,
  reduces the attacin-A reporter; the cached copy in this repository is abstract-only,
  so only the abstract is quoted); Snr1 knockdown lowers
  br and Eip93F expression in optic lobe neuroepithelium and neuroblasts and Snr1 is on
  their transcribed chromatin [PMID:37294080 "Thus, knockdown of Snr1 in either neuroepithelial cells or neuroblasts resulted in reduced expression of the Snr1 target genes br and Eip93F."].
- SNR1 binds the Trithorax SET domain [PMID:12482982 "SNR1 can establish direct contacts through the conserved repeat 2 region with the SET domain of the homeotic regulator Trithorax (TRX)"].
- Repressor side: in the wing, snr1 and brm have opposite phenotypes and SNR1 restricts
  complex activity, with HDAC and the vein repressor NET [PMID:15013794 "The SNR1-mediated repression is dependent on cooperation with histone deacetylases (HDAC) and physical associations with NET, a localized vein repressor."]
  [PMID:16990270 "Importantly, SNR1 mediates ATP-independent repression functions of the complex in cooperation with histone deacetylases and direct contacts with gene-specific repressors."].
  SNR1 restrains BRM-dependent remodeling downstream of promoters of ecdysone-regulated
  genes [PMID:22467207 "revealing that SNR1 functions to restrict BRM-dependent nucleosome remodeling activities downstream of the promoter region."].
  In type II neuroblast lineages Snr1 associates with the Fez-family zinc finger
  transcription factor Earmuff (Erm) in a Brm-HDAC3-Erm repressor complex that stops
  intermediate neural progenitors dedifferentiating [PMID:24618901 "Furthermore, Bap60 and Snr1, two other components of the Brm complex, also physically associate with Erm in a protein complex."]
  [PMID:24618901 "Thus, we conclude that brm and snr1 genetically interact with erm to prevent dedifferentiation of INPs to neuroblasts."].
- Conclusion: Snr1 is a coregulator subunit with both activating and repressive outputs.
  The coactivator activity of the complex is real in flies; the repressive role is
  cell-type and target specific. Neither is the whole story.

## Tumour suppression, cytoplasmic Snr1 and endosomal trafficking

- Snr1 knockdown, unlike knockdown of other SWI/SNF subunits, causes neoplastic
  overgrowth of imaginal epithelia, with endosomal trafficking defects and deregulated
  Notch, JNK and JAK/STAT [PMID:27923836 "Snr1, the conserved homolog of human SMARCB1/hSNF5, prevents tumorigenesis by maintaining normal endosomal trafficking-mediated signaling cascades."].
- Endogenous Snr1 is in both nucleus and cytoplasm, and an NES-deleted Snr1 fails to
  suppress overgrowth [PMID:27923836 "Unlike other components of the SWI/SNF complex that were detected only in the nucleus, Snr1 was observed in both the nucleus and the cytoplasm."]
  [PMID:27923836 "These data suggest that the cytoplasmic function of Snr1 is required for its tumor-suppressing role in Drosophila imaginal disc."].
  The molecular role of cytoplasmic Snr1 in trafficking is unknown (the authors point to
  the human SMARCB1-Dynamin-2 interaction). This is a necessity result: no step of
  endosomal transport is assigned to Snr1, so no process term is proposed.

## Neural development

- Snr1 controls the neuroepithelium-to-neuroblast transition and neuroblast
  differentiation in the optic lobe [PMID:37294080 "Loss of Snr1 in neuroepithelial cells leads to premature neural stem cell formation."].
- Snr1 mutant projection neurons mistarget dendrites like brm mutants
  [PMID:21284845 "In PNs, Snr1 mutants displayed similar phenotypes to brm mutants."].

## npBAF and nBAF (vertebrate assemblies)

- In mammals, neural progenitor BAF complexes contain BAF45a and BAF53a, which are
  replaced in post-mitotic neurons [PMID:17640523 "As neural progenitors exit the cell cycle, these subunits are replaced by the homologous BAF45b, BAF45c, and BAF53b."].
- Flies have one BAF53 (Bap55); human BAF53a and BAF53b both rescue it, and the split
  of roles arose after the vertebrate/insect divergence [PMID:21284845 "These data suggest that the functions for BAF53a and b (in neural precursors and postmitotic neurons, respectively) diverge after the evolutionary split between vertebrates and insects."].
- The npBAF and nBAF IBDs sit on the Bilateria node PTN000001220, seeded only by mouse
  Smarcb1 (`Snr1-bioinformatics/RESULTS.md`). The fly neural Brahma complexes are
  already captured by GO:0035060 brahma complex. Verdict: REMOVE both IBA rows; the
  IBDs should be moved to a vertebrate node.

## Row-level notes

- GO:0030957 Tat protein binding (IPI, PMID:24618901, UniProt-GOA, WITH Erm Q9VQ56):
  Tat protein binding means binding to the HIV Tat transactivator. The paper shows Snr1
  binding to Erm, a fly transcription factor. MODIFY to GO:0140297 DNA-binding
  transcription factor binding (the term FlyBase uses for the matching Brm-TF rows) and
  record a WRONG_TERM defect.
- GO:0043697 cell dedifferentiation (IGI, PMID:24618901, UniProt-GOA): Snr1 prevents
  dedifferentiation; GO has no generic negative regulation term (only vascular smooth
  muscle cell). The same row was made for brm, HDAC3 and erm from this paper on the
  same day. MODIFY to a proposed new term.
- GO:0097150 neuronal stem cell population maintenance (IMP, PMID:28350987): the cached
  abstract is about the super elongation complex and does not mention Snr1; full text
  not available. UNDECIDED.
- Bare protein binding rows: REMOVE, except the cyclin E row, MODIFY to cyclin binding
  (PMID:12093739, PMID:15454538).

## Other accession

UniProt has a second, unreviewed Snr1 entry, Q7K0F9 (GH08712p, 370 aa), with three GOA
rows, all IEA: GO:0006338 chromatin remodeling and GO:0000228 nuclear chromosome
(InterPro IPR006939) and GO:0005634 nucleus (ARBA). Q24090 carries the same three rows.
This review covers only the fetched accession Q24090.
