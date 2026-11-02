# GPAM: ProtNLM function-description review

Selected horse accession: [A0A9L0TTC1](https://www.uniprot.org/uniprotkb/A0A9L0TTC1/entry). Source: ProtNLM2 API snapshot 2026-09-08, frozen in [horse40-predictions.csv](../../../../projects/PROTNLM_EVALUATION/mammal-benchmark/horse40-predictions.csv).

## Exact model output

> Esterifies acyl-group from acyl-ACP to the sn-1 position of glycerol-3-phosphate, an essential step in glycerolipids biosynthesis such as triglycerides, phosphatidic acids and lysophosphatidic acids

## Claim-level assessment

### Acyl donor is acyl-ACP

**PLI.** The experimentally characterized mammalian mitochondrial GPAT1 reaction uses fatty acyl-CoA; the curated human reaction and structural substrate-binding information identify the CoA-linked donor. Acyl-ACP donor usage fits bacterial/other glycerolipid acyltransferase contexts and is not established for GPAM. Conserved horse GPAM architecture and 94.2% identity favor transfer of the mammalian substrate class, not the alternate donor. [PMID:36522428](https://pubmed.ncbi.nlm.nih.gov/36522428/); [DOI:10.1038/s41594-022-00884-7](https://doi.org/10.1038/s41594-022-00884-7).

### sn-1 glycerol-3-phosphate acylation and glycerolipid biosynthesis

**UNC for this selected sequence.** The chemical position and biosynthetic role fit GPAT1, whose product is lysophosphatidic acid and feeds phosphatidic acid and triacylglycerol biosynthesis. These claims are not novel for the horse gene: GOA already carries glycerol-3-phosphate O-acyltransferase activity (GO:0004366) and phospholipid biosynthetic process (GO:0008654) for horse GPAM, and the canonical product A0A9L0TCA8 also carries triglyceride biosynthetic process (GO:0019432). A0A9L0TTC1 is an alternative isoform that lacks human residues 370–407 [(gene-model comparison)](GPAM-bioinformatics/RESULTS-rereview.md). The segment is conserved in human, mouse, rat and the canonical horse product, and forms resolved helices and a strand in the catalytic domain of the human cryo-EM structure. The HXXXXD catalytic motif and the six CoA-binding residues are retained, so no known catalytic residue is missing. Whether the shortened protein folds and acylates glycerol-3-phosphate has not been tested, so activity of this exact sequence, and its contribution to glycerolipid biosynthesis, are unresolved. [PMID:36522428](https://pubmed.ncbi.nlm.nih.gov/36522428/); [DOI:10.1038/s41594-022-00884-7](https://doi.org/10.1038/s41594-022-00884-7).

## Evidence scope and limits

[Human–horse sequence comparison](GPAM-bioinformatics/RESULTS.md) records coverage, gaps and architecture caveats. Human experimental results support transfer where the relevant features are conserved; ARBA assertions and generated gene-review prose are not used as biological evidence. The human reference sequence and current horse sequence are not known to be the exact prediction-time inputs. Claim assessments are kept separate because a partly correct paragraph should not receive an undifferentiated verdict.
