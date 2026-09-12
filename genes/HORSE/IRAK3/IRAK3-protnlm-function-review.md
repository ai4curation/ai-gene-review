# IRAK3: ProtNLM function-description review

Selected horse accession: [A0A3Q2HDT6](https://www.uniprot.org/uniprotkb/A0A3Q2HDT6/entry). Source: ProtNLM2 API snapshot 2026-09-08, frozen in [horse40-predictions.csv](../../../../projects/PROTNLM_EVALUATION/mammal-benchmark/horse40-predictions.csv).

## Exact model output

> Binds to the IL-1 type I receptor following IL-1 engagement, triggering intracellular signaling cascades leading to transcriptional up-regulation and mRNA stabilization

## Claim-level assessment

### Participation in an IL-1 receptor signaling complex

**Plausible, UNC for exact selected sequence.** IRAK-M/IRAK3 can reconstitute IL-1 responses in an IRAK-deficient cell model, but is a signaling regulator rather than a conventional active receptor-associated kinase. The selected horse sequence lacks human residues 2–43, reaching the start of the death domain; intact receptor-complex assembly is therefore not established. The text also overstates direct receptor binding unless the receptor-associated complex is distinguished from a direct binary interaction. [PMID:10383454](https://pubmed.ncbi.nlm.nih.gov/10383454/); [DOI:10.1074/jbc.274.27.19403](https://doi.org/10.1074/jbc.274.27.19403).

### Unqualified activation of transcription and mRNA stabilization

**UNC.** The positive IL-1-response result and negative physiological feedback are both real contexts. IRAK-M prevents IRAK/IRAK4 dissociation from MyD88 and restrains cytokine induction in knockout experiments. The prediction does not specify an assay context or identify which mRNAs are stabilized; a generic IRAK activator description is inadequate to establish these exact effects for horse IRAK3. [PMID:12150927](https://pubmed.ncbi.nlm.nih.gov/12150927/); [DOI:10.1016/s0092-8674(02)00827-9](https://doi.org/10.1016/s0092-8674(02)00827-9).

## Evidence scope and limits

[Human–horse sequence comparison](IRAK3-bioinformatics/RESULTS.md) records coverage, gaps and architecture caveats. Human experimental results support transfer where the relevant features are conserved; ARBA assertions and generated gene-review prose are not used as biological evidence. The human reference sequence and current horse sequence are not known to be the exact prediction-time inputs. Claim assessments are kept separate because a partly correct paragraph should not receive an undifferentiated verdict.
