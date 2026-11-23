# cgs2 (SPCC285.09c, P36599) notes

## Identity
- `just fetch-gene SCHPO cgs2` resolved directly (symbol `cgs2`; synonym `pde1`). UniProt P36599 PDE1_SCHPO,
  346 aa, ORF SPCC285.09c, class II cyclic-nucleotide PDE (Pfam PF02112, IPR000396, PANTHER PTHR28283:SF1).

## Deep research
- Ran `timeout 1300 just deep-research-falcon SCHPO cgs2 --fallback perplexity-lite`:
  2026-10-02: FAILED. Falcon timed out after 600 s; fallback perplexity-lite failed with
  "Provider 'perplexity' not available. Available: falcon, asta, openscientist" ("All providers failed").
  No deep-research file exists. Literature work was done manually with the PubMed MCP and cached
  papers (just fetch-gene-pmids + just fetch-pmid 16143612 15667320 7862141). Status left at DRAFT.

## Key literature (manual)
- Identification: cgs2 ("continues to grow in stationary") mutants cannot undergo meiosis, are sterile and
  fail to enter stationary phase; cgs2 mutant cells "have elevated levels of cAMP"
  [PMID:1657594 "biochemical studies demonstrate that cells containing a mutant allele of cgs2+ have elevated levels of cAMP"].
- pde1 isolated as a multicopy suppressor of high-cAMP sterility; disruption gives partial sterility
  [PMID:1318497 "this cAMP phosphodiesterase plays an important role in balancing the cAMP level in vivo"].
- Biochemistry: expressed in PDE-deficient S. cerevisiae
  [PMID:8392846 "Extracts from such cells that express the Sz. pombe Pde1 exhibit high levels of cAMP phosphodiesterase activity."].
- Genetic interaction with gpa2: [PMID:1340462 "The cAMP level reaches 20 times as high as the wild-type level if a cell carries both this type of gpa2 mutation and a null mutation in pde1"].
- Feedback limitation of glucose cAMP signal: cgs2-s1 (S24F) keeps normal basal cAMP but loses feedback
  [PMID:16143612 "cgs2-s1 cells maintain normal basal cAMP levels, but are severely defective in feedback regulation upon glucose detection"];
  [PMID:16143612 "the wild-type Cgs2 cAMP phosphodiesterase becomes activated almost immediately after adenylate cyclase activation to limit the cAMP response to glucose in fission yeast"].
- cGMP: reporter assay with exogenous nucleotides
  [PMID:21118717 "suggests that Cgs2 is more effective at hydrolysing cGMP than cAMP"].
- Transcriptional regulation by Spc1-Atf1-Pcr1 at M26 in cgs2 promoter [PMID:15448137].
- S. cerevisiae ortholog Pde1 specifically controls glucose/acidification-induced cAMP, PKA site conserved in
  S. pombe [PMID:9880329].

## GO-CAM consistency (gomodel:66187e4700003150)
- cgs2 enables GO:0004115, occurs_in cytosol (PMID:16823372), part_of GO:0110034 (PMID:24928510),
  has_input cAMP, has_output AMP; causal edges: atf1 and pcr1 activities -> (RO:0002407) cgs2 PDE
  (PMID:15448137); cgs2 PDE -> (RO:0002407) cgs1 cAMP-dependent protein kinase inhibitor activity (PMID:21118717).
- No direct pka1 -> cgs2 edge in the cached model (PKA feedback on Cgs2 is hypothesised, not modelled).
- Review core function (GO:0004115, GO:0110034, cytosol) is consistent with the model.

## Decisions
- MF cAMP PDE: ACCEPT (all). cGMP PDE: KEEP_AS_NON_CORE (exogenous cGMP only).
- nucleus HDA: KEEP_AS_NON_CORE; cytosol ACCEPT.
- negative regulation of meiotic cell cycle: KEEP_AS_NON_CORE (indirect via PKA; direction questionable,
  since cgs2 loss blocks meiosis).
- GPCR-pathway regulation terms: ACCEPT (all); GO:0110034 is_a GO:0106072 (checked via OLS).

## Update: falcon deep research completed late
The falcon job continued after the wrapper's 600 s timeout and wrote `cgs2-deep-research-falcon.md`. Points checked against the review:
- It states that no Cgs2-specific cGMP hydrolysis data were retrieved; this is superseded by the cached full text of PMID:21118717, which infers Cgs2 hydrolyses cGMP (exogenous-cGMP 5FOA assay). The GO:0047555 KEEP_AS_NON_CORE calls stand.
- It confirms loss of cgs2 elevates cAMP and impairs mating/meiosis, supporting the open question on the direction of GO:0051447 (negative regulation of meiotic cell cycle, IMP PMID:1657594).
- It agrees Cgs2 localisation has not been directly established beyond the genome-wide HDA survey (PMID:16823372).
- It adds Scr1 promoter binding/repression of cgs2 under glucose (Vassiliadis 2019) and a 2024 live-cell PKA-reporter study (Sakai et al.) as further support for Cgs2 restraining glucose/PKA signalling; these papers are not cached.
