# GPAM: ProtNLM function-description review

Selected horse accession: [A0A9L0TTC1](https://www.uniprot.org/uniprotkb/A0A9L0TTC1/entry). Source: ProtNLM2 API snapshot 2026-09-08, frozen in [horse40-predictions.csv](../../../../projects/PROTNLM_EVALUATION/mammal-benchmark/horse40-predictions.csv).

## Exact model output

> Esterifies acyl-group from acyl-ACP to the sn-1 position of glycerol-3-phosphate, an essential step in glycerolipids biosynthesis such as triglycerides, phosphatidic acids and lysophosphatidic acids

## Claim-level assessment

### Acyl donor is acyl-ACP

**PLI.** The experimentally characterized mammalian mitochondrial GPAT1 reaction uses fatty acyl-CoA; the curated human reaction and structural substrate-binding information identify the CoA-linked donor. Acyl-ACP donor usage fits bacterial/other glycerolipid acyltransferase contexts and is not established for GPAM. Conserved horse GPAM architecture and 94.2% identity favor transfer of the mammalian substrate class, not the alternate donor. [PMID:36522428](https://pubmed.ncbi.nlm.nih.gov/36522428/); [DOI:10.1038/s41594-022-00884-7](https://doi.org/10.1038/s41594-022-00884-7).

### sn-1 glycerol-3-phosphate acylation and glycerolipid biosynthesis

**Supported family transfer with sequence caveat.** The chemical position and biosynthetic role fit GPAT1, whose product is lysophosphatidic acid and feeds phosphatidic acid and triacylglycerol biosynthesis. The horse sequence lacks human residues 370–407, so activity of this selected shortened model remains an inference; no assay on this sequence is supplied. [PMID:36522428](https://pubmed.ncbi.nlm.nih.gov/36522428/); [DOI:10.1038/s41594-022-00884-7](https://doi.org/10.1038/s41594-022-00884-7).

## Evidence scope and limits

[Human–horse sequence comparison](GPAM-bioinformatics/RESULTS.md) records coverage, gaps and architecture caveats. Human experimental results support transfer where the relevant features are conserved; ARBA assertions and generated gene-review prose are not used as biological evidence. The human reference sequence and current horse sequence are not known to be the exact prediction-time inputs. Claim assessments are kept separate because a partly correct paragraph should not receive an undifferentiated verdict.
