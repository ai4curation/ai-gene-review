# Sk1 (Drosophila melanogaster, CG1747, FBgn0030300; UniProt Q9VYY8) - manual literature research

No deep-research provider was run for this gene (no API keys in this environment). This file
records literature work done by hand from the cached publications and PubMed searches.

## Search

PubMed query `Drosophila sphingosine kinase (Sk1 OR Sk2 OR "sphingosine kinase 1")` (run
2026-10-28) returned 7 records. Only two are primary studies of the Sk1 protein itself:

- PMID:14722126 (Herr et al. 2004, J Biol Chem) - abstract only in cache.
- PMID:21321100 (Yonamine et al. 2011, J Cell Biol) - full text in cache (PMC3044112).

The remaining hits concern Sk2 (PMID:42230987 obesity/exercise; PMID:37669862 glial Sk2 and
synaptic homeostasis; PMID:30476102 FXTAS modifier screen), the human SPHK1 interactor
RPS6KC1 (PMID:41130203) or a human cancer study (PMID:37433364), or the desaturase ifc
(PMID:32641420). None assays Sk1 directly.

## Enzymatic activity

Herr et al. cloned the two fly sphingosine kinases and showed both are active enzymes:
[PMID:14722126 "Both genes functionally and biochemically complement a yeast sphingosine kinase
mutant, express predominantly cytosolic activities, and are capable of phosphorylating a range of
endogenous and non-endogenous sphingoid base substrates."]

Yonamine et al. confirm the substrate range in vivo:
[PMID:21321100 "Sk1 and Sk2 use both sphingosine and DHS as substrates and generate S1P and DHS1P."]

## Sequence features

UniProt Q9VYY8 (TrEMBL, 641 aa) carries a DAGKc catalytic domain (PROSITE PS50146, residues
186-334; Pfam PF00781 DAGK_cat plus PF19279 YegS_C) with PROSITE-ProRule ATP-binding positions,
and it is classified in PANTHER PTHR12358 (sphingosine kinase). There is no predicted
transmembrane segment; the N-terminal ~120 residues contain predicted disordered regions.

## Localization

- Cell fractionation: activity is "predominantly cytosolic" (PMID:14722126 abstract).
- Immunostaining of S2 cells stably expressing Sk1 from an inducible metallothionein vector:
  [PMID:21321100 "In addition to cytosolic staining, Sk1 localizes to the plasma membrane, as seen by
  its colocalization with cadherin, a plasma membrane marker"]. Sk2, in contrast, colocalized with
  Lamp1-GFP (lysosomes/late endosomes).
- No fly data place Sk1 in mitochondria. The GOA mitochondrial inner membrane row is an ISS from
  mouse Sphk2 (Q9JIA7).

## Genetics and physiology

- Sk1-null alleles were made by ends-out targeting: [PMID:21321100 "Sk1 mutant flies are viable
  and fertile at room temperature with no external morphological defects."]
- Lipid profiling of the null: [PMID:21321100 "both sk1 and sk2 accumulate sphingosine and DHS"]
  and [PMID:21321100 "The ratio of DHS1P to S1P is increased in the Sk1 mutant because of the
  reduction in S1P level as compared with Sk2 mutant and control flies."]
- Redundancy: [PMID:21321100 "Sk1 and Sk2 double mutants are lethal (unpublished data)"].
- Photoreceptors: [PMID:21321100 "Quantification of Rh1 and TRP shows that Rh1 is decreased to 30%
  and TRP to 40% in sk1 mutants compared with control cn.bw flies."] The authors interpret this as
  altered endolysosomal trafficking secondary to the shifted DHS1P/S1P ratio; it is a downstream
  consequence of the enzyme's product balance, not evidence that Sk1 is a trafficking component.
- Overexpression: GMR-driven Sk1 has only mild effects on rhabdomeres (80% intact vs 4% for Sk2).
- Herr et al. found that Sk1 and Sk2 have overlapping but distinct embryonic expression and are
  not redundant in biological function (PMID:14722126 abstract).
