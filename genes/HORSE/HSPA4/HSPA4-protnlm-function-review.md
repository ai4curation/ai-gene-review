# HSPA4: ProtNLM function-description review

Selected horse accession: [A0A9L0S5Z5](https://www.uniprot.org/uniprotkb/A0A9L0S5Z5/entry). Source: ProtNLM2 API snapshot 2026-09-08, frozen in [horse40-predictions.csv](../../../../projects/PROTNLM_EVALUATION/mammal-benchmark/horse40-predictions.csv).

## Exact model output

> Component of the ribosome-associated complex (RAC), a complex involved in folding or maintaining nascent polypeptides in a folding-competent state. In the RAC complex, binds to the nascent polypeptide chain, while DNAJC2 stimulates its ATPase activity

## Claim-level assessment

### Obligate RAC component whose ATPase is stimulated by DNAJC2

**PLI.** Primary work identifies the human RAC pair as Mpp11 and Hsp70L1, while Apg2/HSPA4 experiments establish nucleotide exchange on Hsc70 in a chaperone/disaggregase system. Generic Hsp70-family similarity does not place HSPA4 in RAC. The selected horse protein is a near-identical HSPA4 homolog with its ATPase region retained and an internal C-terminal-region deletion; it is not thereby the RAC Hsp70 paralog. [PMID:36604744](https://pubmed.ncbi.nlm.nih.gov/36604744/).

### Maintenance/refolding of client polypeptides

**UNC for this selected sequence.** Apg2/HSPA4 supports Hsc70-dependent aggregate reactivation as a nucleotide-exchange factor. This validates broad chaperone biology, not the particular ribosome-bound mechanism or direct nascent-chain-binding role asserted by the paragraph. At that broad level the claim is not novel for the horse gene: the full-length horse HSPA4 product F6YZJ4 already carries protein folding (GO:0006457) in GOA. A0A9L0S5Z5 is an exon-skipping isoform that lacks human residues 679–718 in the conserved alpha-helical C-terminal region, while retaining the nucleotide-binding domain [(gene-model comparison)](HSPA4-bioinformatics/RESULTS-rereview.md). HSPA4 takes part in refolding through its exchange activity on Hsc70, and the distinctive C-terminal extension of Apg2 interacts with the Hsc70 nucleotide-binding domain and tunes this activity. No study has tested whether a form lacking this segment keeps exchange activity, so the contribution of this exact sequence is unresolved. [PMID:30521813](https://pubmed.ncbi.nlm.nih.gov/30521813/); [DOI:10.1016/j.jmb.2018.11.026](https://doi.org/10.1016/j.jmb.2018.11.026); [PMID:36167183](https://pubmed.ncbi.nlm.nih.gov/36167183/).

## Evidence scope and limits

[Human–horse sequence comparison](HSPA4-bioinformatics/RESULTS.md) records coverage, gaps and architecture caveats. Human experimental results support transfer where the relevant features are conserved; ARBA assertions and generated gene-review prose are not used as biological evidence. The human reference sequence and current horse sequence are not known to be the exact prediction-time inputs. Claim assessments are kept separate because a partly correct paragraph should not receive an undifferentiated verdict.
