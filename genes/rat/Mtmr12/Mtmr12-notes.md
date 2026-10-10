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

## Re-review 2026-10-04

**GOA changes.** None for this product: the refreshed GOA still carries only the two UniProt SubCell-mapping IEA rows (GO:0016529 sarcoplasmic reticulum, GO:0030017 sarcomere). No new rows, no retired rows.

**Row audit.** Both rows remain `UNDECIDED`. The sarcoplasmic-reticulum row now records a `reason`: the gene-level localization is well supported (mouse MTMR12, Q80TA6, carries an EXP annotation to GO:0016529 from PMID:23818870; the MTM1-MTMR12 complex "localizes to **triads**, partly overlapping RyR1-positive sarcoplasmic-reticulum structures but not α-actinin-positive Z-lines" in mouse muscle, per the Falcon report), but whether this alternative-N-terminus product with a predicted signal peptide (`SIGNAL 1..20`) is targeted the same way is untested. The sarcomere row stays UNDECIDED; the mouse data place the complex at triads rather than Z-lines, so sarcomere is at best a loose description.

**core_functions added.** One entry: MTM1-binding adaptor (GO:0019902 phosphatase binding) acting in GO:0050821 protein stabilization of MTM1. Rationale: the mechanism is well established at gene level [PMID:23818870 "binds to myotubularin in skeletal muscle"; "MTMR12 primarily regulates the function of myotubularin protein by affecting protein levels instead of modulating the enzymatic activity"], and this rat product retains reference residues 57-748 with 691/692 identity, including the entire myotubularin domain and the C-terminal region (Mtmr12-bioinformatics/RESULTS.md). The core-function description states that the rat product itself has not been assayed.

**Not added as NEW rows.** Comparator check (QuickGO, 2026-10-04): human MTMR12 (Q9C0I1), mouse (Q80TA6) and the rat reference product (Q5FVM6) carry no GO:0019902 or GO:0050821 annotations; human carries only GO:0005515 IPI rows with MTM1/MTMR2. Proposing NEW annotations on a non-reference TrEMBL product ahead of the reference orthologs is not justified, so the two validator warnings ("core function term not reflected in existing_annotations") are left deliberately.

**Open question.** Is the alternative N-terminus of A0A8I5ZMD5 a real transcript, and does it change trafficking or MTM1 binding?
