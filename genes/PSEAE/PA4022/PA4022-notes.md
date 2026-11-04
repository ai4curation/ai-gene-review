# PA4022 (Q9HX05) curation notes

- Added as the ethanolamine-specific representative of the non-acylating acetaldehyde
  dehydrogenase route in `modules/bacterial_ethanolamine_uptake_catabolism.yaml`
  (PR #5970 review round).
- Deep research was not generated (no provider API keys in this environment). Sources
  used: UniProt Q9HX05, PMID:27325678 (Lundgren et al. 2016, abstract only), PMID:10075429
  (ExaC), and the pairwise analysis in `PA4022-bioinformatics/`.
- Literature: PMID:27325678 assigns PA4022 the acetaldehyde dehydrogenase step of the
  PA4022-eat-eutBC operon [PMID:27325678 "This pathway is encoded by the PA4022-eat-eutBC
  operon and consists of a transport protein (Eat), an ethanolamine-ammonia lyase (EutBC),
  and an acetaldehyde dehydrogenase (PA4022)."]. No enzyme assay of PA4022 was found.
- Bioinformatics (`PA4022-bioinformatics/pairwise_exac.py`, results in RESULTS.md):
  PA4022 is 98.2% identical to ExaC Q9ZAA1 (strain ATCC 17933) and 98.4% to PAO1 exaC
  PA1984 (Q9I2C4); Q9ZAA1 is the strain-ATCC 17933 ortholog of PA1984 (99.4%). Catalytic
  Glu262 and Cys301 are conserved. PA4022 is therefore a recent near-identical paralog of
  exaC in PAO1.
- Decisions: the three electronic rows (generic ALDH and oxidoreductase) are TOO_GENERAL;
  GO:0140087 is proposed as NEW (ISS from ExaC). No process term is proposed: the
  ethanolamine-catabolic role rests on operon placement and the authors' assignment, and no
  PA4022 mutant phenotype is available; it is recorded as a knowledge gap.
- PANTHER: PTHR43111:SF1 (UniProt DR and PANTHER 19.0 Pseudomonas classification agree).
