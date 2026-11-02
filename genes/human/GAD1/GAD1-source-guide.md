# GAD1 sources and product scope

GAD67 is a PLP-dependent glutamate decarboxylase that supplies GABA. The active full-length enzyme, its inactive GAD25 splice product, engineered structures and interaction-screen clones must remain distinct. Current judgments and manual reference assessments are in [the review](GAD1-ai-review.yaml); literal annotation contexts and historical locators are in [the source archive](GAD1-source-evidence.yaml).

## Catalysis and products

The original GAD67/GAD25 comparison measures radiolabeled glutamate-to-CO2 activity using equimolar translation, PLP and controls. Full-length GAD67 is active and GAD25 inactive; the variant-focused title does not negate canonical activity ([PMID:10671565](https://pubmed.ncbi.nlm.nih.gov/10671565/)). Cloned human GAD67 is independently enzymatically active in bacterial expression ([PMID:1549570](https://pubmed.ncbi.nlm.nih.gov/1549570/)). The GAD1 structure and catalytic analysis distinguish sustained GAD67 activity from GAD65 regulation ([PMID:17384644](https://pubmed.ncbi.nlm.nih.gov/17384644/)).

Official [PDB 2OKJ](https://www.rcsb.org/structure/2OKJ) is human GAD1, with a homodimeric biological assembly. Its engineered entity is canonical residues 93–594 plus HH, 504 residues in total. It is not a natural splice product; 2OKK is the separate GAD2 structure. Complete subscription Methods were not independently obtained.

| Current product | Sequence scope | Functional interpretation |
|---|---|---|
| Q99259-1 / GAD67 | Displayed, 594 residues; direct FASTA exact | Characterized active full-length enzyme |
| Q99259-2 | UniProt says not described; no sequence recovered | No invented FASTA or activity assignment |
| Q99259-3 / GAD25 | 224 residues; direct FASTA exact | Original GAD25 evidence establishes inactivity |
| Q99259-4 | 425 residues; direct FASTA exact | Sequence verified; equivalent catalysis/targeting not assumed |

The isoform-interaction study’s GAD1_1 clone translates exactly to the current 594-residue reference. Study GAD1_2 and GAD1_3 are experimental clone names, not automatically current UniProt suffixes ([PMID:26871637](https://pubmed.ncbi.nlm.nih.gov/26871637/)).

## Interactions and location

The SH3 screen places the GAD1 peptide at residues 520–532 opposite NCK1 SH3 domains; GAD1 is the domain-binding partner, not the SH3-domain provider ([PMID:17474147](https://pubmed.ncbi.nlm.nih.gov/17474147/), original Table S2). The other positive binary screens remain documented with exact partners, suffixes and construct limits. Their generic protein-binding annotations are removed as functionally uninformative; removal does not deny the reported interactions, and no unsupported specific molecular function is substituted. HuRI explicitly tests Q99259-1; its array, pooling and validated records are related assay forms, not three independent physiological replications ([PMID:32296183](https://pubmed.ncbi.nlm.nih.gov/32296183/)). HAAO T42S/I37V belong to the partner in the variant screen, not to GAD1 ([PMID:31515488](https://pubmed.ncbi.nlm.nih.gov/31515488/), Supplementary Data 2 rows 476–477).

One source join remains unresolved: the complete 1,166-pair Table 2 of [PMID:21516116](https://pubmed.ncbi.nlm.nih.gov/21516116/) pairs GAD1/2571 with CMTM5/116173, while the incoming annotation names AGTRAP/57085. Other papers independently support GAD1–AGTRAP, so failure to recover this source-specific pair is not evidence that binding is false. Likewise, the selected GAD25-paper Discussion does not independently resolve its GAD1–GAD2 IPI assay.

Actual GAD67 antibody evidence supports cytoplasm and inhibitory presynaptic terminals ([PMID:15347806](https://pubmed.ncbi.nlm.nih.gov/15347806/), selected Results/Figure 2; [PMID:23258346](https://pubmed.ncbi.nlm.nih.gov/23258346/), antibody Methods/Figure 3; [PMID:24613359](https://pubmed.ncbi.nlm.nih.gov/24613359/), selected Results/Figures 1 and 4). This is distinguished from GFP-at-Gad1-locus cell identification in the accessible [PMID:21584649](https://pubmed.ncbi.nlm.nih.gov/21584649/) abstract. Its exact source assay remains uninspected. The source paper has no verified PMC identifier; an earlier citation-list extraction was corrected rather than treated as a retraction or remapping.

Actual PAINT PTHR45677 assertions and the exact 594-residue target alignment support all four incoming ancestral placements. The catalytic/GABA-synthesis node is PTN002903772, cytoplasm PTN000242648 and active zone PTN002903810. Current versus literal/main donor differences remain separately dated. The active-zone original panels in PMID:12074840 remain inaccessible; the annotation retains the actual curator/PAINT placement without invented antibody or ultrastructure details. Selected PMID:18165320 electron microscopy labels SLC4A10, not GAD67. Precise perinuclear and cell-cortex claims remain unresolved.

## Pathway participants

The official [GAD1 component R-HSA-888580](https://reactome.org/content/detail/R-HSA-888580) is human Q99259, chain 1–594, at the GABA transport-vesicle membrane. The [GAD1 synthesis reaction](https://reactome.org/content/detail/R-HSA-888572) includes its homodimer; the [GAD2-labelled reaction](https://reactome.org/content/detail/R-HSA-888577) includes a GAD1:GAD2 assembly. [Release](https://reactome.org/content/detail/R-HSA-888589) and [docking](https://reactome.org/content/detail/R-HSA-917744) contain the same target through vesicle assemblies. Thus pathway labels do not establish target absence. Conversely, event-level plasma-membrane compartments do not automatically locate every participant there. The specialized vesicle model is not a new demonstration of GAD1 fusion/docking activity or equal targeting of every product.

The GABA shunt explicitly starts with glutamate decarboxylation, so GAD1 does perform its entry step; downstream reactions and complete physiological flux are not thereby established. Chemical synaptic transmission specifically concerns release and postsynaptic activation. Supplying GABA alone does not resolve the separate source-specific transmission claim.

## Preserved history and source access

The inherited review contains 31 source rows and a separate cytosol NEW. Its complete immutable Git locator, all 37 quotation-association locators and the original journal prefix are retained in the archive. Two previously used excerpts remain active at claims they support; 35 associations remain historical only. The old cytosol NEW is not reasserted: the actual IBD is cytoplasm, and its family-membership quote does not establish the narrower compartment. No absence of biological cytosol localization is claimed.

Normal cached text and separately accessed originals are described distinctly in each reference assessment. Partial Introduction/Discussion caches, authentic selected indexed originals and inaccessible source-specific panels are not called complete Methods reads. Genuine native acquisition reconciled all 50 original contexts with the actual 16-column export and private native seed. All 46 source files and both inherited quotations were checked against their actual bytes; 21 main sources were reused unchanged and 25 missing sources were acquired. Cache full-text availability is recorded separately from the exact sections assessed. The inherited review and journal remained untouched throughout acquisition. No current decision is duplicated in the compact evidence archive.
