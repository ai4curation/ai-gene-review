# PDC1 (YLR044C, P06169) notes

## Evidence journal
- Major pyruvate decarboxylase isozyme (EC 4.1.1.1); TPP + Mg2+ cofactors; homotetramer; allosterically activated by pyruvate [UniProt:P06169].
- pdc1 deletants keep 60-70% (or 80%) of the activity because PDC5 is induced (autoregulation) [PMID:2404950 "pdc1(0) mutants were able to grow on glucose and still contained 60 to 70% of the wild-type PDC activity"]; the pdc1 pdc5 double mutant has no activity and cannot ferment glucose [PMID:2185016 "Deletion mutants lacking both PDC1 and PDC5 did not show any detectable pyruvate decarboxylase activity in vitro and were unable to ferment glucose."].
- PDC1 expressed in E. coli gives active enzyme [PMID:2404950 "This result shows that the PDC1-encoded subunit alone can form an active tetramer without yeast-specific processing steps."].
- Cytosolic [PMID:2665820 "The activity of the cytosolic enzyme pyruvate decarboxylase in S. cerevisiae"]; nuclear enrichment reported [PMID:16850348 "Interestingly, the enzymes Pdc1 and Pdc5 are enriched in the nucleus."].
- Ehrlich pathway: decarboxylates branched-chain 2-oxo acids [PMID:9546164 "both PDC1- and PDC5-encoded isoenzymes can decarboxylate branched-chain 2-oxo acids"; PMID:22904058 "Aro10, Pdc1, Pdc5, and Pdc6 exhibited activity with all branched-chain and sulfur-containing 2-oxo acids tested"]; valine: "any one of the isozymes of pyruvate decarboxylase will decarboxylate alpha-ketoisovalerate" [PMID:10753893].
- Aromatic substrates conflict: genetics says any Pdc can decarboxylate phenylpyruvate/indolepyruvate [PMID:12499363 "This decarboxylation can be effected by any of Pdc1p, Pdc5p, Pdc6p, or Ydr380wp"], but direct assay of individually expressed enzymes finds only Aro10 and Pdc5 active with phenylpyruvate [PMID:22904058 "Only Aro10 and Pdc5 catalyzed the decarboxylation of the aromatic substrate phenylpyruvate"]. Phenylpyruvate rows left UNDECIDED.
- Acetoin carboligation side reaction [UniProt:P06169 "Reaction=2 acetaldehyde = acetoin"].

## Curation decisions
- RCA "bifid shunt" (GLUCFERMEN-PWY) removed: wrong for yeast.
- RCA 4-hydroxyphenylpyruvate decarboxylase / tyrosine catabolism: no evidence for Pdc1p; YeastCyc attaches every family member.
- protein binding (Pdc1-Pdc5 co-purification) removed as uninformative; likely mixed tetramers.


## 2026-10-25 alcoholic-fermentation audit

Major glucose-fermentation pyruvate decarboxylase. PMID22904058 full text and PMID9546164 full text distinguish direct branched-chain catalysis from requirement for whole-cell fusel production. Pdc1 lacks measurable phenylpyruvate activity in the 2012 single-enzyme panel; older 2003 genetic aromatic catabolism remains relevant and specific MF stays UNDECIDED. No inference of 4-hydroxyphenylpyruvate absence from the phenylpyruvate result. Native pdc1/pdc5 phenotype is qualified by promoter-activated PDC6 rescue (PMID1807827).

Workflow: fetched current gene data using `just fetch-gene`; existing original row fields were preserved (verified against the pre-edit JSON snapshot). All 59 rows were reassessed by term and source, including non-fermentation activities/localizations. Annotation-reviewer and core-function synthesis instructions were applied. `just deep-research-falcon yeast PDC1 --fallback perplexity-lite` ran concurrently with `just fetch-gene-pmids`: Falcon/Edison failed HTTP403 authentication; Perplexity failed HTTP401 insufficient_quota. No generated provider report was fabricated. Publication caching completed successfully. FEBA fitness is a prokaryote-only review requirement and does not apply to yeast.

Family membership from the fetched record (official names independently checked in `interpro/panther/panther.obo`):

```text
DR   PANTHER; PTHR43452; PYRUVATE DECARBOXYLASE; 1.
DR   PANTHER; PTHR43452:SF30; PYRUVATE DECARBOXYLASE ISOZYME 1-RELATED; 1.
```

GO-CAM index lookup by the UniProt accession returned no entries in the current index; existing RCA/YeastPathways assertions were assessed from their explicit terms and underlying chemistry. No new process rows were manufactured.

Audit decisions by original term (duplicate evidence rows remain intact):

- GO:0000287 magnesium ion binding: ACCEPT.
- GO:0003824 catalytic activity: MODIFY.
- GO:0004737 pyruvate decarboxylase activity: ACCEPT.
- GO:0005515 protein binding: REMOVE.
- GO:0005634 nucleus: KEEP_AS_NON_CORE.
- GO:0005737 cytoplasm: MODIFY.
- GO:0005829 cytosol: ACCEPT.
- GO:0006067 ethanol metabolic process: MODIFY.
- GO:0006550 L-isoleucine catabolic process: ACCEPT.
- GO:0006559 L-phenylalanine catabolic process: KEEP_AS_NON_CORE.
- GO:0006569 L-tryptophan catabolic process: KEEP_AS_NON_CORE.
- GO:0006572 L-tyrosine catabolic process: UNDECIDED.
- GO:0006574 L-valine catabolic process: ACCEPT.
- GO:0016831 carboxy-lyase activity: MODIFY.
- GO:0019655 pyruvate fermentation to ethanol: ACCEPT.
- GO:0019658 bifid shunt: REMOVE.
- GO:0030976 thiamine pyrophosphate binding: ACCEPT.
- GO:0045151 acetoin biosynthetic process: KEEP_AS_NON_CORE.
- GO:0047433 branched-chain-2-oxoacid decarboxylase activity: ACCEPT.
- GO:0047434 indolepyruvate decarboxylase activity: KEEP_AS_NON_CORE.
- GO:0050177 phenylpyruvate decarboxylase activity: UNDECIDED.
- GO:0050546 4-hydroxyphenylpyruvate decarboxylase activity: UNDECIDED.
- GO:1902652 secondary alcohol metabolic process: MODIFY.
