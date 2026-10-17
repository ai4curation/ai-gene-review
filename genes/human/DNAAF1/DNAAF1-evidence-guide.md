# DNAAF1 evidence guide

DNAAF1 is reviewed as a cytoplasmic dynein-arm assembly factor. The two human arm classes are represented in one core. Ciliary, spindle-pole and developmental observations remain visible without turning each phenotype into another molecular function.

## Original experiments and access

| Source | Evidence used | Limits |
| --- | --- | --- |
| [van Rooijen et al., 2008](https://doi.org/10.1681/ASN.2007080917), Figures 3, 5–7 and Methods | Human BC024009 LRRC50-EGFP localization; human HK-2 knockdown; zebrafish mutant, rescue and ultrastructure | The human construct was expressed in human 293T and canine MDCK hosts. Zebrafish rescue used BC045963. Neither host identity nor a phenotype establishes a purified human dynein interface. |
| [Loges et al., 2009](https://pmc.ncbi.nlm.nih.gov/articles/PMC2795801/), patient Results and Figure 4 | Human respiratory cilia lack ODA components DNAH5, DNAH9 and DNAI2 and IDA component DNALI1 | Cytoplasmic DNALI1 retention supports assembly/targeting failure; this is not imaging of endogenous DNAAF1 or a binding assay. |
| [Duquesnoy et al., 2009](https://pmc.ncbi.nlm.nih.gov/articles/PMC2790569/), Table 1, Figures 2–3 and transgene/fractionation Methods | Human loss of both arms; conserved cytoplasmic preassembly support | Quantitative cell-body enrichment and L92 substitution/rescue are Chlamydomonas experiments; DNAI1 redistribution is from Trypanosoma. Their predominantly ODA defect is narrower than the human phenotype. |

The three original GOA-cited publication caches are genuinely abstract-only. Additional original text was read separately: the 2008 [author-deposited full text](https://www.researchgate.net/publication/5468104_LRRC50_a_Conserved_Ciliary_Protein_Implicated_in_Polycystic_Kidney_Disease), and indexed original PMC text for both 2009 articles. The inspected source sections are identified above; figure legends were read, but no figure-pixel analysis is claimed. Failed direct XML/HTML requests remain recorded separately and were not treated as successful recovery. Cache bytes and their access flags were preserved.

The three original short quotations in the YAML are exact excerpts from the protected abstracts: 5 words from the 2008 paper, 9 from Loges et al. and 5 from Duquesnoy et al. Each occurs once. Other support entries cite the same evidence without repeating text; the number of quotations is not the number of observations assessed.

## Annotation decisions

All 27 source annotation dictionaries are retained. The review has 5 ACCEPT, 17 KEEP_AS_NON_CORE, 3 MODIFY, 1 REMOVE and 1 UNDECIDED decisions; no NEW annotation is proposed.

The general axoneme and dynein-complex assembly assertions are refined to the existing outer- and inner-arm processes. Official QuickGO is_a/part_of ancestor closures place [GO:0036158](https://www.ebi.ac.uk/QuickGO/term/GO:0036158) and [GO:0036159](https://www.ebi.ac.uk/QuickGO/term/GO:0036159) under GO:0070286 and GO:0035082, but not GO:0044458. The supported motile-cilium assertion is therefore retained as ACCEPT and included in the assembly core. The separate renal primary-cilium phenotype retains its distinct scope.

The sole removal concerns electronic extracellular-region inference. The saved [GO_REF:0000108](https://geneontology.org/GO_REF/0000108) row derives from organizer-cilium movement. [GO:0005576](https://www.ebi.ac.uk/QuickGO/term/GO:0005576) denotes the space outside the cell, whereas the ciliary interior is membrane bounded. Inferring the assembly factor's location from the extracellular fluid movement conflates distinct roles. This does not reject the retained laterality process or assert that every possible extracellular pool has been excluded.

Lung development remains UNDECIDED: the inspected patient evidence establishes respiratory disease and defective cilia, but does not resolve lung morphogenesis. The experimental row is not removed on that basis. Other laterality and movement assertions are retained as developmental or physiological contexts.

The two dynein-binding annotations are retained as non-core. Positive Chlamydomonas Oda7 association with outer and I1 inner dyneins is explicitly cited in the original papers. The target/fish perturbation experiments do not map the human binding interface. No unsupported chaperone or adaptor activity is substituted.

## Phylogeny and products

The official [PANTHER PTHR45973 tree](https://www.pantherdb.org/services/oai/pantherdb/treeinfo?family=PTHR45973&format=json) places human leaf PTN000062877 below the actual IBD node PTN002915666. The node-level PAINT slice records axoneme, dynein-complex binding, laterality and axoneme-assembly assertions. The current human and zebrafish annotations supply experimental grounding; human self-inclusion is expected, not circular. No target-specific loss or erroneous node descent was identified. The normal PAINT slice was generated from exact previously downloaded official GAF inputs; it is not represented as a fresh release download.

The [official UniProt record](https://www.uniprot.org/uniprotkb/Q8NEP3/entry) and all three isoform FASTAs support sequence-defined products of 725, 489 and 418 residues. The 489-residue form lacks the six annotated LRRs; the 418-residue form retains them but loses the distal tail. Equivalent function is unestablished for both. The historical 637-residue prediction in the 2008 paper is not silently mapped to either current shorter product. Predicted transcripts are not evidence that three functional proteins were demonstrated.


## Additional mammalian interaction evidence

[PMID:29228333](https://pmc.ncbi.nlm.nih.gov/articles/PMC5886296/), Results/Figure 3, supplies human DNAAF1–IFT88 Y2H and HEK293 co-IP, plus SF-TAP/co-IP association with RUVBL1 and RUVBL2. Its Methods identify the human DNAAF1 construct and assay hosts. Basal-body localization and RUVBL1-dependent DNAAF1/IFT88 colocalization are in the subsequent Results/Figure 4 and immunofluorescence/siRNA Methods. The proposed R2TP-like delivery model is explicitly distinguished from those observations. Mutant protein abundance and stability limit interpretation of altered partner recovery. No unseen supplementary table, purified dynein-transfer assay or natural short-product function is claimed.

[PMID:29601588](https://pmc.ncbi.nlm.nih.gov/articles/PMC5895051/) provides Discussion context, with earlier DNAAF1 studies cited rather than newly performed. [PMID:29959317](https://pmc.ncbi.nlm.nih.gov/articles/PMC6026120/), Methods and Figure 5D–E, supplies corroborating murine Dnaaf1 associations; those constructs are not relabelled as human. Existing cached full texts were inspected without modifying their bytes. The new human-study excerpts occur once each in notes and core support, totalling 16 words; the three original abstract excerpts remain unchanged.
