# Mtmr12 (A0A8I5ZMD5): evidence and exact-input prediction review

The predicted name is a correct domain description and does not assert phosphatase catalysis. The main uncertainty is localization of the exact product: its altered N-terminus carries a computational signal-peptide call, while the characterized MTMR12-MTM1 mechanism acts in the cytoplasm and at muscle membranes.

## Input identity and functional boundary

A0A8I5ZMD5 and Q5FVM6 are same-gene rat Mtmr12 products. Selected residues 41–732 align to reference 57–748 with 691/692 identities; the entire 439-residue myotubularin phosphatase domain is identical. The first 40 selected residues differ from the reference N-terminus. SignalP annotates residues 1–20 as a signal peptide, but this is a prediction rather than demonstrated ER import.

## Biological evidence

- [PMID:23818870 — Loss of catalytically inactive lipid phosphatase myotubularin-related protein 12 impairs myotubularin stability and promotes centronuclear myopathy in zebrafish.](https://pubmed.ncbi.nlm.nih.gov/23818870/): Cell and animal experiments distinguish inactive MTMR12 from its catalytically active MTM1 partner and support a protein-stability mechanism.

> MTMR12 primarily regulates the function of myotubularin protein by affecting protein levels instead of modulating the enzymatic activity


> the catalytically inactive MTMR12 only partially but significantly rescues myotubularin function

## Exact non-GO claims

The complete emitted record is preserved in [Mtmr12-protnlm-source.json](Mtmr12-protnlm-source.json). Assessments below address the selected protein product; evidence on longer products is identified explicitly.

### Protein name

> Myotubularin phosphatase domain-containing protein

CNN (CS 2). The complete myotubularin phosphatase domain is retained, including identity across the reference domain. The wording “domain-containing” does not claim autonomous phosphatase activity and should not be scored as pseudoenzyme overannotation. [Sequence comparison](Mtmr12-bioinformatics/RESULTS.md).

### Location

> Membrane

UNC (CS 1). Membrane association is plausible through the normal MTM1 complex and independently through a possible altered trafficking route, but neither demonstrates stable membrane association of this product. A cleavable signal-peptide prediction also does not by itself establish that the mature protein remains membrane bound. [PMID:23818870](https://pubmed.ncbi.nlm.nih.gov/23818870/); [exact record](Mtmr12-uniprot.txt).

## Emitted GO claims

All 1 emitted GO claims are individually assessed in [Mtmr12-protnlm-predictions-review.yaml](Mtmr12-protnlm-predictions-review.yaml).

## Family integration

The myotubularin family includes active phosphatases and inactive binding partners. MTMR12 belongs to the latter functional class; the full domain’s preservation does not reinstate MTM1-like catalysis. The sequence distinction here concerns the N-terminus and potentially trafficking, not loss of the phosphatase fold.

## Evidence limits

The primary report has full text and assays zebrafish, mammalian cells and muscle, rather than this alternative rat protein product. The genuine Falcon report provides a useful family and MTM1-interaction synthesis, but its broad localization transfer needs the exact N-terminal caveat. A signal-peptide predictor is insufficient to overturn the established gene-level mechanism or to declare a secreted isoform.

Exact sequence mapping: [Mtmr12-bioinformatics/RESULTS.md](Mtmr12-bioinformatics/RESULTS.md). Global alignments can place nonhomologous alternative tails opposite gaps or distant residues; only conserved segments and explicitly retained feature intervals support functional transfer.
