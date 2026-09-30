# CAPSL: ProtNLM function-text review

**NPI (score 0): the venom-gland context is incompatible with horse CAPSL.**

## Original prediction

Source: [ProtNLM A0A3Q2I3U9](https://www.uniprot.org/uniprotkb/A0A3Q2I3U9/entry#prot-nlm), frozen API snapshot 2026-09-08, retained in the benchmark raw data. No ontology term is implied by this free-text output.

> May be involved in the cellular control mechanism of the secretion of toxins from the gland into the venom

## Claim and evidence

The claim is participation in secretion of toxins from a venom gland. Horses do not have a venom delivery system; a generic role in cellular secretion would not validate this specific organismal claim. A0A3Q2I3U9 is identified as CAPSL by VGNC:16048, has calcyphosin-like EF-hand architecture, and aligns at 97.1% identity across the complete 208-residue human CAPSL sequence (92.4% of the 225-residue horse protein). [Sequence comparison](CAPSL-bioinformatics/RESULTS.md).

Human CAPSL studies instead establish intracellular localization and cell-regulatory phenotypes: “CAPSL is localized in both the cytoplasm and the nucleus of cells” ([PMID:39264149](https://pubmed.ncbi.nlm.nih.gov/39264149/), DOI [10.7554/eLife.96907](https://doi.org/10.7554/eLife.96907)). Human endothelial depletion and mouse endothelial knockout support angiogenic functions, while [PMID:31186450](https://pubmed.ncbi.nlm.nih.gov/31186450/) studies adipogenesis. These experiments ground the intracellular family interpretation; they are not direct horse experiments.

The weak modal “may” does not rescue the incompatible venom-gland context. **Error type: TAXON_CONSTRAINT_VIOLATION** in the biological sense of an organism-inappropriate process; this is not a claim that a formal GO taxon rule has been checked. The model's donor protein or training example is not established, so paralog confusion is not assigned.
