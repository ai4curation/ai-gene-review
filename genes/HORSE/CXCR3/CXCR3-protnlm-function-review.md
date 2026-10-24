# CXCR3: ProtNLM function-description review

Selected horse accession: [A0A9L0T1D1](https://www.uniprot.org/uniprotkb/A0A9L0T1D1/entry). Source: ProtNLM2 API snapshot 2026-09-08, frozen in [horse40-predictions.csv](../../../../projects/PROTNLM_EVALUATION/mammal-benchmark/horse40-predictions.csv).

## Exact model output

> Receptor for a number of inflammatory CC-chemokines including CCL3/MIP-1-alpha, CCL4/MIP-1-beta and RANTES and subsequently transduces a signal by increasing the intracellular calcium ion level. May play a role in the control of granulocytic lineage proliferation or differentiation. Participates in T-lymphocyte migration to the infection site by acting as a chemotactic receptor

## Claim-level assessment

### CCL3, CCL4 and CCL5/RANTES receptor specificity

**PLI.** The human CXCR3-B study explicitly reports that these CC chemokines did not compete for radiolabeled CXCL10 binding. Its positive ligands were CXCL9/10/11 and CXCL4. The selected horse receptor is 90.8% identical across the full human CXCR3-A sequence with seven membrane helices retained. The stated ligand set is characteristic of a different chemokine-receptor specificity, not validated by the broad family label. [PMID:12782716](https://pubmed.ncbi.nlm.nih.gov/12782716/); [DOI:10.1084/jem.20021897](https://doi.org/10.1084/jem.20021897).

### Calcium signaling and T-lymphocyte chemotaxis

**Supported family transfer.** These broad properties fit CXCR3 ligand-induced signaling and activated-lymphocyte migration. They do not validate the incorrect ligand list in the preceding sentence. The horse model retains the full receptor architecture; this is inference from human receptor experiments, supplemented by horse expression evidence, rather than direct horse ligand-binding data. [PMID:12782716](https://pubmed.ncbi.nlm.nih.gov/12782716/); [DOI:10.1084/jem.20021897](https://doi.org/10.1084/jem.20021897).

### Granulocytic lineage proliferation/differentiation

**UNC.** The investigated receptor papers do not establish this specific function for the selected horse CXCR3 product. Endothelial growth effects of a human alternative isoform are a different claim. A lineage-specific assay or mechanistic evidence is needed. [PMID:12782716](https://pubmed.ncbi.nlm.nih.gov/12782716/); [DOI:10.1084/jem.20021897](https://doi.org/10.1084/jem.20021897).

## Evidence scope and limits

[Human–horse sequence comparison](CXCR3-bioinformatics/RESULTS.md) records coverage, gaps and architecture caveats. Human experimental results support transfer where the relevant features are conserved; ARBA assertions and generated gene-review prose are not used as biological evidence. The human reference sequence and current horse sequence are not known to be the exact prediction-time inputs. Claim assessments are kept separate because a partly correct paragraph should not receive an undifferentiated verdict.
