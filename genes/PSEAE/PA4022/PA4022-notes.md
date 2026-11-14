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


## 2026-11-06 comparative re-audit

PMID22267508 full text identifies native PAO1 HdhA as PA4022 by peptide mass fingerprinting and distinguishing peptides; recombinant His-tagged HdhA directly oxidizes acetaldehyde with NAD+ at pH 9.0 ("We found here that purified rHdhA and rExaC both oxidize acetaldehyde."). Hydrazone chemistry is NAD(P)-dependent oxidative hydrolysis yielding hydrazides and acids, not simple hydrolysis. The 2012 single/double disruptions and 2016 PA4022 deletion/complementation invalidate earlier blanket statements that the enzyme and mutants were never tested. The 2016 growth study did not reproduce hydrazone-supported growth under its conditions; this limits physiological generalization without negating the purified reaction. Broad parent MFs now MODIFY to the measured specific activities. A hydrazone MF NTR represents the ontology gap after QuickGO name/definition checks; no invented GO ID or new BP row. The PR5970-authored GO0140087 ISS/PMID10075429 row is retained as NEW and refined to IDA/PMID22267508; its exact old row and current payload are archived in PA4022-source-analysis/authored-proposal-evidence-history.yaml. All three upstream payloads are unchanged. The extra specificity row is now redundant with broad-row refinements but preserved for provenance. Direct core biological-process participation rests on measured oxidation plus native pathway genetics, not a growth phenotype alone.

A normal Falcon research attempt failed with HTTP 403 authentication/access error; no provider report was fabricated. Review evidence comes from the primary sources, frozen UniProt/domain records and explicitly identified comparative inference. Original GOA/UniProt files and upstream row payloads are preserved. Source refreshes used only the normal publication fetch command; separately acquired full articles remain ignored, with small exact excerpts and provenance retained beside the reviews.
