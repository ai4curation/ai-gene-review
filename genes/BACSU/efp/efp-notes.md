# efp (Bacillus subtilis 168, UniProtKB:P49778) - curation notes

## Deep research provenance

- Provider deep research (`just deep-research*`) was **not run**: no provider API keys are
  available in this environment. No `efp-deep-research-*.md` file exists for this gene.
- `just mod-description-deep-research BACSU efp` was run and reported
  `efp skipped: no MOD provider configured for organism 'BACSU'` (no SubtiWiki provider),
  so there is no MOD description file either.
- Literature search: local `publications/` cache searched for "EF-P", "elongation factor P",
  "aminopentan", "ymfI"; web search used to identify the Hummels & Kearns 2019 PLoS Genet paper
  (PMID:31237868), which was then cached with `just fetch-gene-pmids BACSU efp` together with the
  UniProt-cited sporulation paper (PMID:14586115). The Kearns et al. 2004 swarming screen
  (Mol Microbiol 52:357-369) that first identified efp as a swarming gene could not be resolved
  to a verified PMID here and is cited only via later papers.

## Identity and family

- 185 aa, Swiss-Prot reviewed; "Belongs to the elongation factor P family" (UniProt CC:SIMILARITY);
  HAMAP MF_00141 EF_P, TIGR00038 efp, PANTHER PTHR30053. Three-domain KOW + two OB/S1-like
  domains, tRNA-mimic shape. UniProt function text is "By similarity" (ECO:0000250) to E. coli.

## Function in B. subtilis (with provenance)

- EF-P relieves ribosome pausing at polyproline motifs in B. subtilis in vivo (ribosome profiling):
  [PMID:31237868 "Bacillus subtilis EF-P also alleviates ribosome pausing at sequences encoding tandem prolines"].
- Unlike most bacteria, efp is dispensable for growth in B. subtilis:
  [PMID:28787546 "Bacillus subtilis where EF-P is not required for growth and is instead specifically required for swarming motility"];
  [PMID:31237868 "growth defects in Bacillus subtilis efp mutants are negligible, even under conditions of high translation"].
- Swarming defect arises from impaired flagellar biosynthesis; a pause at an SPP motif in FliY is
  a key target: [PMID:31237868 "The B. subtilis efp mutant is instead impaired for flagellar biosynthesis"];
  [PMID:31237868 "One mutation abolished a translational pause site within the flagellar C-ring component FliY"].
  Swarming is therefore a downstream, indirect consequence of the translation-factor activity;
  no swarming-motility BP term is proposed (EF-P does no work of flagellar motility itself).
- Sporulation: efp disruption abolishes sporulation without affecting growth
  [PMID:14586115 "The effect was especially pronounced in the efp mutant, sporulation of which was entirely abolished without affecting growth"].
  Also indirect (translation of sporulation proteins); not annotated.

## Post-translational modification (5-aminopentanol on Lys32)

- Discovery: [PMID:27002156 "We identified a 5-aminopentanol moiety attached to Lys(32) of B. subtilis EF-P that is required for swarming motility"].
- YmfI reduces the 5-aminopentanone intermediate:
  [PMID:28787546 "Here we determine that the protein YmfI catalyzes the reduction of EF-P-5 aminopentanone to EF-P-5 aminopentanol"].
  Without YmfI the aminopentanone form accumulates and is inhibitory to swarming; an unmodifiable
  EF-P K32R allele bypasses YmfI: [PMID:28787546 "B. subtilis encodes the first EF-P ortholog that retains function in the absence of modification"].
- Pathway genes: [PMID:29615499 "ynbB, gsaB, and ymfI are required for modification and that yaaO, yfkA, and ywlG influence the level of modification"];
  the moiety is apparently built directly on EF-P
  [PMID:29615499 "5-aminopentanol is likely directly assembled on EF-P through a novel modification pathway"].
- Nuance: modification is not strictly required. PTM mutants show polyproline-reporter defects that
  are milder than efp deletion and condition/context-dependent
  [PMID:29615499 "this defect was not as significant as the defect seen in an efp mutant"].

## GO annotation decisions (summary)

- MF translation elongation factor activity (IBA, IEA): ACCEPT, core.
- CC cytoplasm (IBA, IEA), cytosol (IEA ARBA): ACCEPT, consistent with E. coli and P. putida EF-P reviews.
  No B. subtilis-specific localization experiment found; UniProt location is By similarity.
- BP translational elongation, rescue of stalled cytosolic ribosome: ACCEPT, core (B. subtilis ribosome
  profiling, PMID:31237868).
- BP peptide biosynthetic process: KEEP_AS_NON_CORE (matches ECOLI and PSEPK efp reviews; translation is
  no longer an is_a descendant of GO:0043043 so MODIFY would be lateral).
- BP regulation of gene expression (ARBA): MODIFY to regulation of translation (GO:0006417), the
  term the sibling reviews keep as non-core.
