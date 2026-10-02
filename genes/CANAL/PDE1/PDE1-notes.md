# PDE1 (Candida albicans, Q5AGE4, orf19.11710 / C5_02290W_A) — curation notes

## Identity
- Low-affinity class II cyclic nucleotide phosphodiesterase (Pfam PF02112 PDEase_II; PROSITE PS00607; PANTHER PTHR28283:SF1).
- Orthologs: S. cerevisiae PDE1 (SGD:S000003217), S. pombe cgs2/pde1 (SPCC285.09c), Dictyostelium PdsA.
- Paralog-in-function: PDE2 (high-affinity class I PDE, distinct family).

## Biochemistry
- Cloned by complementation of a S. cerevisiae PDEase-deficient mutant [PMID:8075796 "We have cloned a Candida albicans gene, which encodes a cyclic nucleotide phosphodiesterase (PDEase), by complementation in a Saccharomyces cerevisiae PDEase-deficient mutant."]
- Hydrolyses cAMP and cGMP [PMID:8075796 "it hydrolyses both cAMP (Km = 0.49 mM) and cGMP (Km = 0.25 mM)"]; no divalent cation requirement, poorly inhibited by standard PDE inhibitors.

## Physiology
- Pde1 (not Pde2) terminates glucose- and acidification-induced cAMP signalling [PMID:20558315 "Pde1, but not Pde2, is responsible for down-regulation of cAMP signalling induced by glucose addition or intracellular acidification"]. Same division of labour as S. cerevisiae [PMID:9880329 "We show that deletion of PDE1, but not PDE2, results in a much higher cAMP accumulation upon addition of glucose or upon intracellular acidification."]
- Morphogenesis/stress phenotypes are mainly synthetic with GPA2 [PMID:20558315 "the genetic interactions of PDE1 and in some cases PDE2, with GPA2 caused synthetic defects in growth, morphogenesis and responses to some stresses"].
- Virulence: secondary to PDE2; pde1 pde2 double mutant avirulent [PMID:20558315].
- Not required for farnesol repression of hyphae [PMID:18078440 "Neither Pde1 nor Pde2 was necessary for the repression of hyphal growth by farnesol or dodecanol."]
- S. cerevisiae Pde1 PKA site (Ser252) conserved in C. albicans Pde1 [PMID:9880329].

## Review decisions
- MF: cAMP PDE (core), cGMP PDE (accept; physiological relevance unclear), general PDE terms accepted.
- BP: negative regulation of cAMP/PKA signalling and of glucose-activated GPCR pathway accepted (Pde1 directly destroys the second messenger); cAMP catabolism accepted.
- Filamentous growth IMPs kept as non-core (indirect, largely synthetic with gpa2; full text not cached).
- CC: no localisation data; ND accepted.
- Full text of PMID:20558315 and PMID:8075796 not available in cache (abstract only).

## Deep research status (2026-10-02)
- `just deep-research-falcon CANAL PDE1 --fallback perplexity-lite` failed: falcon timed out after 600 s and the perplexity provider is not configured in this environment. No deep-research file was produced.
- Literature was instead gathered manually via PubMed search ("Candida albicans PDE1 phosphodiesterase" returned 5 hits: PMID:30299574, 20558315, 18078440, 9880329, 8075796), plus PMID:14523128 (PDE2). All cached publications are abstract-only.
