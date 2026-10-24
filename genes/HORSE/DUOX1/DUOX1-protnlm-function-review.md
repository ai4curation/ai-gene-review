# DUOX1: ProtNLM function-description review

Selected horse accession: [A0A9L0SQG9](https://www.uniprot.org/uniprotkb/A0A9L0SQG9/entry). Source: ProtNLM2 API snapshot 2026-09-08, frozen in [horse40-predictions.csv](../../../../projects/PROTNLM_EVALUATION/mammal-benchmark/horse40-predictions.csv).

## Exact model output

> Generates hydrogen peroxide which is required for the activity of thyroid peroxidase/TPO and lactoperoxidase/LPO. Plays a role in thyroid hormones synthesis and lactoperoxidase-mediated antimicrobial defense at the surface of mucosa. May have its own peroxidase activity through its N-terminal peroxidase-like domain

## Claim-level assessment

### H2O2 generation supporting TPO/LPO chemistry

**UNC for this selected sequence.** Full-length human DUOX1–DUOXA1 complexes generate H2O2. The selected horse sequence retains the catalytic oxidase region but lacks human residues 775–873, including the first annotated EF-hand and much of the second. This undermines transfer of normal calcium-regulated activity. Thyroid hormone and mucosal antimicrobial participation additionally require the relevant tissue/partner context. [PMID:33420071](https://pubmed.ncbi.nlm.nih.gov/33420071/); [DOI:10.1038/s41467-020-20466-9](https://doi.org/10.1038/s41467-020-20466-9).

### Intrinsic peroxidase activity in the N-terminal domain

**NPI.** The isolated human DUOX1 N-terminal domain lacks intrinsic peroxidase activity despite peroxidase-fold homology; the homologous horse region is retained. The model hedges with “may”, but supplies no mechanism or evidence overcoming this direct negative result. Peroxidase-like fold should not be equated with peroxidase catalysis, and NOX-domain heme binding is a separate property. [PMID:19460756](https://pubmed.ncbi.nlm.nih.gov/19460756/); [DOI:10.1074/jbc.M109.013581](https://doi.org/10.1074/jbc.M109.013581).

## Evidence scope and limits

[Human–horse sequence comparison](DUOX1-bioinformatics/RESULTS.md) records coverage, gaps and architecture caveats. Human experimental results support transfer where the relevant features are conserved; ARBA assertions and generated gene-review prose are not used as biological evidence. The human reference sequence and current horse sequence are not known to be the exact prediction-time inputs. Claim assessments are kept separate because a partly correct paragraph should not receive an undifferentiated verdict.
