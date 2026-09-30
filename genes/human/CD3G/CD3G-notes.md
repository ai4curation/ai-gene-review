# CD3G (human, P09693) review notes

Context: ADAPTIVE_IMMUNITY project, T cell receptor trunk.

## Biology summary (with provenance)

- Invariant subunit of the TCR-CD3 complex; forms CD3 gamma-epsilon heterodimer.
  [PMID:9485181 "The TCR/CD3 complex is assembled after a series of pairwise interactions involving the formation of dimers of CD3 epsilon with either CD3 gamma or CD3 delta."]
  [PMID:31461748 "The octameric TCR-CD3 complex is assembled with 1:1:1:1 stoichiometry of TCRαβ:CD3γε:CD3δε:CD3ζζ."]
- EC Ig domain sites bind CD3E; TM acidic residue binds TCR beta.
  [PMID:8636209 "Site-directed mutagenesis of the acidic amino acid in the TM domain of CD3 gamma demonstrated that this residue is involved in TCR assembly probably by binding to Ti beta."]
- ITAM tyrosine-phosphorylated by LCK.
  [PMID:2470098 "members of the CD3 complex, including the gamma, delta, and epsilon chains, as well as a putative zeta subunit, can be phosphorylated at tyrosine residues by the CD4/CD8.p56lck complex."]
- PKC-phosphorylated S126 + di-leucine L131/L132 mediate clathrin-dependent TCR down-regulation.
  [PMID:8187769 "a membrane-proximal di-leucine motif (L131 and L132) in the cytoplasmic tail of CD3 gamma was required for PKC-mediated TCR down-regulation in addition to phosphorylation at S126."]
  [PMID:1535555 "A di-leucine- and a tyrosine-based motif are individually sufficient to induce both endocytosis and delivery to lysosomes of Tac."]
- Human CD3G-deficient T cells: reduced surface TCR, impaired ligand-induced endocytosis, no PMA-induced down-modulation.
  [PMID:12794121 "Kinetic confocal analysis indicated that early ligand-induced endocytosis was impaired."]
- gamma-delta TCRs contain CD3 gamma-epsilon but mostly lack CD3 delta.
  [PMID:30976362 "In fact, the CD3δ subunit is not even incorporated into the γδTCR complex and is not required for γδT cell development"]
- IMD17: CD3G deficiency milder than CD3D/CD3E deficiency.
  [PMID:17277165 "We propose a CD3delta >> CD3gamma hierarchy for the relative impact of their absence on the signaling for T cell production in humans."]

## Curation decisions

- 9 HuRI `protein binding` IPI rows: REMOVE (uninformative Y2H, mostly membrane-protein background partners).
- `protein transport` IMP (PMID:12794121): MODIFY -> GO:0031623 receptor internalization. CD3G supplies
  the sorting motif (structural participation), not merely cargo.
- Comparator check for internalization terms: CD3D (P04234), CD3E (P07766), CD79A (P11912), CD79B
  (P40259) carry none of GO:0031623 / GO:0036300 / GO:0006897 / GO:0038009 (QuickGO, 2026-09-30).
  So no NEW row was added; raised as a suggested question instead. The MODIFY refines an existing
  curated IMP assertion rather than manufacturing a new one.
- Knockout/deficiency phenotype process rows (cell polarity, regulation of lymphocyte apoptosis,
  positive thymic selection IBA): KEEP_AS_NON_CORE (necessity evidence, downstream of TCR signalling).
- `MHC class II receptor activity` contributes_to IDA (PMID:1323144, abstract-only): MARK_AS_OVER_ANNOTATED,
  consistent with CD247 review; class II specificity is a property of the clonotypic TCR.
- `identical protein binding` IDA (PMID:14967045): KEEP_AS_NON_CORE (in vitro oligomerization of disordered
  cytoplasmic fragment).
- `T cell receptor binding` NAS (PMID:11186279, case-report letter, no abstract): KEEP_AS_NON_CORE.
- Core MF: GO:0030159 signaling receptor complex adaptor activity, contributes_to GO:0004888.

## Deep research

Falcon deep research (`just deep-research-falcon human CD3G --fallback perplexity-lite`) was launched in
parallel with the review; see status below.

Status (2026-09-30): deep research FAILED. Falcon timed out/failed (600 s timeout). The
perplexity-lite fallback then failed with "Provider 'perplexity' not available. Available: falcon,
asta, openscientist", ending in "All providers failed". The review was written without a deep research
file, using the UniProt record, the cached GOA-cited publications, and five UniProt-cited papers
fetched with `just fetch-pmid` (PMID:2470098, 8187769, 1535555, 15136729, 17277165).
