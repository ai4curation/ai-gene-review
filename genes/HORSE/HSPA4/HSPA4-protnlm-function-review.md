# HSPA4: ProtNLM function-description review

Selected horse accession: [A0A9L0S5Z5](https://www.uniprot.org/uniprotkb/A0A9L0S5Z5/entry). Source: ProtNLM2 API snapshot 2026-09-08, frozen in [horse40-predictions.csv](../../../../projects/PROTNLM_EVALUATION/mammal-benchmark/horse40-predictions.csv).

## Exact model output

> Component of the ribosome-associated complex (RAC), a complex involved in folding or maintaining nascent polypeptides in a folding-competent state. In the RAC complex, binds to the nascent polypeptide chain, while DNAJC2 stimulates its ATPase activity

## Claim-level assessment

### Obligate RAC component whose ATPase is stimulated by DNAJC2

**PLI.** Primary work identifies the human RAC pair as Mpp11 and Hsp70L1, while Apg2/HSPA4 experiments establish nucleotide exchange on Hsc70 in a chaperone/disaggregase system. Generic Hsp70-family similarity does not place HSPA4 in RAC. The selected horse protein is a near-identical HSPA4 homolog with its ATPase region retained and an internal C-terminal-region deletion; it is not thereby the RAC Hsp70 paralog. [PMID:36604744](https://pubmed.ncbi.nlm.nih.gov/36604744/).

### Maintenance/refolding of client polypeptides

**Supported at broad level.** Apg2/HSPA4 supports Hsc70-dependent aggregate reactivation as a nucleotide-exchange factor. This validates broad chaperone biology, not the particular ribosome-bound mechanism or direct nascent-chain-binding role asserted by the paragraph. [PMID:30521813](https://pubmed.ncbi.nlm.nih.gov/30521813/); [DOI:10.1016/j.jmb.2018.11.026](https://doi.org/10.1016/j.jmb.2018.11.026).

## Evidence scope and limits

[Human–horse sequence comparison](HSPA4-bioinformatics/RESULTS.md) records coverage, gaps and architecture caveats. Human experimental results support transfer where the relevant features are conserved; ARBA assertions and generated gene-review prose are not used as biological evidence. The human reference sequence and current horse sequence are not known to be the exact prediction-time inputs. Claim assessments are kept separate because a partly correct paragraph should not receive an undifferentiated verdict.
