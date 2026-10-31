# PDC6 (YGR087C, P26263) notes

## Evidence journal
- Third PDC structural gene; weakly expressed on glucose; its deletion lowers Pdc activity in ethanol-grown cells [PMID:1744053 "However, in cells grown in ethanol medium the PDC6 deletion caused a reduction of pyruvate decarboxylase activity."].
- Low sulfur amino acid content, induced under sulfur limitation [PMID:22904058 "The third PDC isoenzyme, Pdc6, has a very low content of sulfur-containing amino acids and is highly expressed in sulfur-limited cultures"].
- Least efficient of the three isozymes [PMID:23423327 "ScPDC6 has the least decarboxylation efficiency of all three isozymes of S. cerevisiae."].
- Active on pyruvate, linear and branched-chain 2-oxo acids, but not phenylpyruvate, when expressed alone [PMID:22904058].
- GFP: cytoplasm only [UniProt:P26263 "SUBCELLULAR LOCATION: Cytoplasm"].

## Curation decisions
- No fermentation BP asserted as core: Pdc6p cannot sustain fermentation on its own; core = pyruvate decarboxylase + branched-chain 2-oxo acid decarboxylation (valine/isoleucine Ehrlich).
- Phenylpyruvate rows UNDECIDED (genetic vs biochemical conflict); bifid shunt removed.


## 2026-10-25 alcoholic-fermentation audit

The prior universal claim that PDC6 cannot sustain fermentation is superseded. PMID1807827 explicitly reports spontaneous PDC1-promoter/PDC6 fusion mutants restoring glucose fermentation, with partial complementation only. Standard native low expression still explains poor rescue in pdc1/pdc5 mutants. PMID1744053 documents Pdc activity in ethanol-grown cells, not ethanol oxidation. PMID22904058 full text verifies direct pyruvate activity of individually expressed PDC6. Fermentative capacity is therefore conditional, not absent. Nuclear localization remains a non-core phylogenetic inference, not independently demonstrated in the inspected target-specific evidence.

Workflow: fetched current gene data using `just fetch-gene`; existing original row fields were preserved (verified against the pre-edit JSON snapshot). All 52 rows were reassessed by term and source, including non-fermentation activities/localizations. Annotation-reviewer and core-function synthesis instructions were applied. `just deep-research-falcon yeast PDC6 --fallback perplexity-lite` ran concurrently with `just fetch-gene-pmids`: Falcon/Edison failed HTTP403 authentication; Perplexity failed HTTP401 insufficient_quota. No generated provider report was fabricated. Publication caching completed successfully. FEBA fitness is a prokaryote-only review requirement and does not apply to yeast.

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
- GO:0019658 bifid shunt: REMOVE.
- GO:0030976 thiamine pyrophosphate binding: ACCEPT.
- GO:0045151 acetoin biosynthetic process: KEEP_AS_NON_CORE.
- GO:0047433 branched-chain-2-oxoacid decarboxylase activity: ACCEPT.
- GO:0047434 indolepyruvate decarboxylase activity: KEEP_AS_NON_CORE.
- GO:0050177 phenylpyruvate decarboxylase activity: UNDECIDED.
- GO:0050546 4-hydroxyphenylpyruvate decarboxylase activity: UNDECIDED.
- GO:1902652 secondary alcohol metabolic process: MODIFY.
