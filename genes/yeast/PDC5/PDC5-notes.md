# PDC5 (YLR134W, P16467) notes

## Evidence journal
- Second pyruvate decarboxylase structural gene, 88% identical to PDC1; expressed mainly in pdc1 mutants [PMID:2185016 "PDC5 is only expressed in pdc1 deletion mutants."]; Km 8 mM vs 5 mM for Pdc1 [PMID:2185016 "The PDC5 isoenzyme showed a slightly higher Km value for its substrate pyruvate than the PDC1 product"].
- pdc1 pdc5 double mutant: no activity, no fermentation [PMID:2185016].
- Recombinant isozyme comparison [PMID:23423327 "ScPDC5 has comparable decarboxylation efficiency to that of ScPDC1"].
- Induced by thiamine limitation and nitrogen limitation; requires Pdc2 [PMID:22904058 "PDC5 exhibits tight transcriptional control"].
- Only Pdc isozyme with phenylpyruvate activity in individual-expression assays [PMID:22904058 "Only Aro10 and Pdc5 catalyzed the decarboxylation of the aromatic substrate phenylpyruvate"]; also branched-chain/sulfur 2-oxo acids [PMID:22904058].
- Nuclear enrichment [PMID:16850348].

## Curation decisions
- Phenylpyruvate decarboxylase and phenylalanine catabolism accepted for PDC5 (unlike PDC1/PDC6).
- 4-hydroxyphenylpyruvate / tyrosine RCA rows UNDECIDED: plausible given phenylpyruvate activity, untested.
- bifid shunt RCA removed; protein binding removed.


## 2026-10-25 alcoholic-fermentation audit

Compensatory pyruvate decarboxylase, induced when PDC1 is absent; also has direct phenylpyruvate activity (PMID22904058), unlike Pdc1/Pdc6 in that panel. Pyruvate and branched-chain functions remain core. Do not generalize phenylpyruvate kinetics to the untested 4-hydroxyphenylpyruvate substrate. Native pdc1/pdc5 phenotype is qualified by promoter-activated PDC6 rescue (PMID1807827).

Workflow: fetched current gene data using `just fetch-gene`; existing original row fields were preserved (verified against the pre-edit JSON snapshot). All 60 rows were reassessed by term and source, including non-fermentation activities/localizations. Annotation-reviewer and core-function synthesis instructions were applied. `just deep-research-falcon yeast PDC5 --fallback perplexity-lite` ran concurrently with `just fetch-gene-pmids`: Falcon/Edison failed HTTP403 authentication; Perplexity failed HTTP401 insufficient_quota. No generated provider report was fabricated. Publication caching completed successfully. FEBA fitness is a prokaryote-only review requirement and does not apply to yeast.

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
- GO:0006559 L-phenylalanine catabolic process: ACCEPT.
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
- GO:0050177 phenylpyruvate decarboxylase activity: ACCEPT.
- GO:0050546 4-hydroxyphenylpyruvate decarboxylase activity: UNDECIDED.
- GO:1902652 secondary alcohol metabolic process: MODIFY.
