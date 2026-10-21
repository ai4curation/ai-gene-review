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

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

This entry was written during a re-review that deliberately ignored the ProtNLM2 predictions; the earlier sections above, including the ProtNLM2 claim assessments, are retained unchanged.

The predicted name is a correct domain description and does not assert phosphatase catalysis. The main uncertainty is localization of the exact product: its altered N-terminus carries a computational signal-peptide call, while the characterized MTMR12-MTM1 mechanism acts in the cytoplasm and at muscle membranes.

### Input identity and functional boundary

A0A8I5ZMD5 and Q5FVM6 are same-gene rat Mtmr12 products. Selected residues 41–732 align to reference 57–748 with 691/692 identities; the entire 439-residue myotubularin phosphatase domain is identical. The first 40 selected residues differ from the reference N-terminus. SignalP annotates residues 1–20 as a signal peptide, but this is a prediction rather than demonstrated ER import.

### Biological evidence

- [PMID:23818870 — Loss of catalytically inactive lipid phosphatase myotubularin-related protein 12 impairs myotubularin stability and promotes centronuclear myopathy in zebrafish.](https://pubmed.ncbi.nlm.nih.gov/23818870/): Cell and animal experiments distinguish inactive MTMR12 from its catalytically active MTM1 partner and support a protein-stability mechanism.

> MTMR12 primarily regulates the function of myotubularin protein by affecting protein levels instead of modulating the enzymatic activity


> the catalytically inactive MTMR12 only partially but significantly rescues myotubularin function

### Exact non-GO claims

The complete emitted record is preserved in [Mtmr12-protnlm-source.json](Mtmr12-protnlm-source.json). Assessments below address the selected protein product; evidence on longer products is identified explicitly.

#### Protein name

> Myotubularin phosphatase domain-containing protein

CNN (CS 2). The complete myotubularin phosphatase domain is retained, including identity across the reference domain. The wording “domain-containing” does not claim autonomous phosphatase activity and should not be scored as pseudoenzyme overannotation. [Sequence comparison](Mtmr12-bioinformatics/RESULTS.md).

#### Location

> Membrane

UNC (CS 1). Membrane association is plausible through the normal MTM1 complex and independently through a possible altered trafficking route, but neither demonstrates stable membrane association of this product. A cleavable signal-peptide prediction also does not by itself establish that the mature protein remains membrane bound. [PMID:23818870](https://pubmed.ncbi.nlm.nih.gov/23818870/); [exact record](Mtmr12-uniprot.txt).

### Emitted GO claims

All 1 emitted GO claims are individually assessed in [Mtmr12-protnlm-predictions-review.yaml](Mtmr12-protnlm-predictions-review.yaml).

### Family integration

The myotubularin family includes active phosphatases and inactive binding partners. MTMR12 belongs to the latter functional class; the full domain’s preservation does not reinstate MTM1-like catalysis. The sequence distinction here concerns the N-terminus and potentially trafficking, not loss of the phosphatase fold.

### Evidence limits

The primary report has full text and assays zebrafish, mammalian cells and muscle, rather than this alternative rat protein product. The genuine Falcon report provides a useful family and MTM1-interaction synthesis, but its broad localization transfer needs the exact N-terminal caveat. A signal-peptide predictor is insufficient to overturn the established gene-level mechanism or to declare a secreted isoform.

Exact sequence mapping: [Mtmr12-bioinformatics/RESULTS.md](Mtmr12-bioinformatics/RESULTS.md). Global alignments can place nonhomologous alternative tails opposite gaps or distant residues; only conserved segments and explicitly retained feature intervals support functional transfer.

### Re-review 2026-10-04

**GOA changes.** None for this product: the refreshed GOA still carries only the two UniProt SubCell-mapping IEA rows (GO:0016529 sarcoplasmic reticulum, GO:0030017 sarcomere). No new rows, no retired rows.

**Row audit.** Both rows remain `UNDECIDED`. The sarcoplasmic-reticulum row now records a `reason`: the gene-level localization is well supported (mouse MTMR12, Q80TA6, carries an EXP annotation to GO:0016529 from PMID:23818870; the MTM1-MTMR12 complex "localizes to **triads**, partly overlapping RyR1-positive sarcoplasmic-reticulum structures but not α-actinin-positive Z-lines" in mouse muscle, per the Falcon report), but whether this alternative-N-terminus product with a predicted signal peptide (`SIGNAL 1..20`) is targeted the same way is untested. The sarcomere row stays UNDECIDED; the mouse data place the complex at triads rather than Z-lines, so sarcomere is at best a loose description.

**core_functions added.** One entry: MTM1-binding adaptor (GO:0019902 phosphatase binding) acting in GO:0050821 protein stabilization of MTM1. Rationale: the mechanism is well established at gene level [PMID:23818870 "binds to myotubularin in skeletal muscle"; "MTMR12 primarily regulates the function of myotubularin protein by affecting protein levels instead of modulating the enzymatic activity"], and this rat product retains reference residues 57-748 with 691/692 identity, including the entire myotubularin domain and the C-terminal region (Mtmr12-bioinformatics/RESULTS.md). The core-function description states that the rat product itself has not been assayed.

**Not added as NEW rows.** Comparator check (QuickGO, 2026-10-04): human MTMR12 (Q9C0I1), mouse (Q80TA6) and the rat reference product (Q5FVM6) carry no GO:0019902 or GO:0050821 annotations; human carries only GO:0005515 IPI rows with MTM1/MTMR2. Proposing NEW annotations on a non-reference TrEMBL product ahead of the reference orthologs is not justified, so the two validator warnings ("core function term not reflected in existing_annotations") are left deliberately.

**Open question.** Is the alternative N-terminus of A0A8I5ZMD5 a real transcript, and does it change trafficking or MTM1 binding?

### Full re-review 2026-10-20 (independent of ProtNLM output)

**Independence.** This pass does not use any ProtNLM output. The earlier sections above ("Exact non-GO claims", "Emitted GO claims") describe a separate prediction assessment and are not evidence for the gene review. `compare_sequences.py` previously took the target sequence from the ProtNLM source JSON. It now reads the sequence from `Mtmr12-uniprot.txt`, and it also aligns the target to human MTMR12 (Q9C0I1) and human MTM1 (Q13496, fetched from UniProt REST into the bioinformatics folder). The `file:` reference to the ProtNLM source JSON has been dropped from the review.

**Identity of A0A8I5ZMD5.** This is an unreviewed Ensembl gene-model product (ENSRNOP00000078948.1, 732 aa) of rat Mtmr12 (RGD:1307902). It is 16 aa shorter than the reviewed rat protein Q5FVM6 (748 aa). Residues 41-732 are 691/692 identical to Q5FVM6 57-748, and they cover the whole myotubularin phosphatase-like domain (439/439 identical). The first 40 residues (`MVVSWVIRKFLCFCCKVCFPFPGYPSFLSFPKPWRISLLP`) are hydrophobic, rich in Cys and Pro, and unrelated to the conserved N-terminus shared by Q5FVM6 and human Q9C0I1. This is an alternative or likely spurious first exon. SignalP calls residues 1-20 as a signal peptide, but because the segment is not conserved I treat that call as a gene-model artefact and not as evidence of secretion. No domain is missing. The MTM1 catalytic CX5R loop (C375...R381) aligns to E376...L382 in the target, so both catalytic positions are replaced, as expected for an inactive member (Mtmr12-bioinformatics/RESULTS.md).

**Evolutionary grounding.** UniProt places the protein in PANTHER PTHR10807:SF37 (MYOTUBULARIN-RELATED PROTEIN 12), the same subfamily as human MTMR12 Q9C0I1 and mouse Q80TA6. The family review interpro/panther/PTHR10807/PTHR10807-review.yaml uses the same SF37 placement, so there is no disagreement. In PAINT, human Q9C0I1 is a seed of the cytoplasm IBD node PTN000743854 (GO:0005737), but this TrEMBL product received no IBA rows. I do not add cytoplasm as NEW because it is an ancestor of the sarcoplasmic reticulum term, which is accepted. The closest characterised relatives are the orthologs: human MTMR12/3-PAP, the original MTM1 adapter [PMID:12847286 "3-PAP functions as an \"adapter\" for myotubularin"], and mouse and zebrafish MTMR12 [PMID:23818870].

**Row changes.**
- GO:0016529 sarcoplasmic reticulum: UNDECIDED changed to ACCEPT. The mouse ortholog was shown experimentally to colocalize at triads with partial RyR1 overlap [PMID:23818870 "partial co-localization of MTMR12 was observed with ryanodine receptors, a sarcoplasmic reticulum marker"]. The signal-peptide caveat applies to a non-conserved exon only.
- GO:0030017 sarcomere: UNDECIDED changed to KEEP_AS_NON_CORE. The location is a loose positional description (triads recur within each sarcomere, with no Z-line overlap). UniProt's curated ortholog text uses "co-localizes with MTM1 in the sarcomere".

**Core function.** Unchanged in substance: GO:0019902 phosphatase binding and GO:0050821 protein stabilization of MTM1, with location sarcoplasmic reticulum. I still do not propose NEW rows for these terms because the reference orthologs (Q9C0I1, Q80TA6, Q5FVM6) do not carry them either; the reasoning is in the 2026-10-04 entry.

**Modules.** No module under modules/ mentions MTMR12 or MTM1 (grep, 2026-10-20).
