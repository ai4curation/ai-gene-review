# LRP12 literature notes

## Identity, isoforms, topology, and structure

Human LRP12 (UniProtKB Q9Y561) is a protein-coding LDL receptor-related family member. The foundational human cDNA paper describes a putative 859-residue transmembrane protein [PMID:9927190 "encodes a putative transmembrane protein composed of 859 amino acids: the 492"]. The reviewed UniProt entry models a signal peptide, an extracellular region (33-492), one transmembrane helix (493-513), and a long cytoplasmic tail (514-859) [UniProtKB:Q9Y561 "FT   TRANSMEM        493..513"]. This is a type-I topology model, not evidence that LRP12 is an autonomous enzyme.

UniProt curates two named human protein isoforms [UniProtKB:Q9Y561 "CC       Event=Alternative splicing; Named isoforms=2;"]. Isoform 1 is the displayed 859-residue sequence; isoform 2 carries VSP_040992, a deletion of residues 27-45 [UniProtKB:Q9Y561 "Missing (in isoform 2)"]. None of the functional papers reviewed here assigns α4-integrin regulation, neuronal phenotypes, trafficking, or cancer phenotypes uniquely to either isoform. Tested constructs should therefore be reported as tested isoforms/constructs, not as proof of isoform-specific biology.

The current UniProt record has an AlphaFoldDB cross-reference [UniProtKB:Q9Y561 "DR   AlphaFoldDB; Q9Y561; -."], but no experimental PDB cross-reference. There is consequently no reviewed full-length experimental structure; predicted structure must not be described as experimentally solved.

## Noncoding repeat-expansion diseases

Human genetic studies establish LRP12 as a repeat-expansion disease locus. A noncoding CGG expansion in LRP12 was identified in oculopharyngodistal myopathy [PMID:31332380 "oculopharyngodistal myopathy, in LOC642361/NUTM2B-AS1 and LRP12, respectively."]. UniProt records the pathogenic sequence as a heterozygous expansion in the 5-prime untranslated region [UniProtKB:Q9Y561 "expansion (CGG) in the 5-prime untranslated region of the gene"], usually greater than 100 repeats in OPDM1 [UniProtKB:Q9Y561 "patients is usually greater than 100 (PubMed:37339631)."].

Shorter pathogenic expansions also cause ALS28. The ALS study found 61-100 repeats in LRP12-ALS, compared with 100-200 in most LRP12-OPDM individuals [PMID:37339631 "ALS individuals (LRP12-ALS) have 61-100 repeats, which contrasts with most OPDM"], and reports repeat-length-dependent switching of phenotypes [PMID:37339631 "repeat length-dependent switching of phenotypes."]. RNA foci in muscle and induced motor neurons support repeat-mediated toxic gain-of-function disease biology [PMID:37339631 "RNA foci are more prominent in muscle and iPSMNs in LRP12-ALS"]. Because the causal variant is a noncoding 5-prime-UTR repeat expansion rather than a protein-coding change, these disease associations do not license a new molecular-function or biological-process annotation for the normal LRP12 protein.

## α4-integrin mechanism

The strongest direct molecular evidence identifies LRP12 as an α4-integrin inactivator. The cached abstract states that the LRP12 cytoplasmic domain binds the integrin α4 tail [PMID:37330909 "The LRP12 cytoplasmic domain directly binds to the"] and that it inhibits talin engagement, thereby maintaining inactive integrin [PMID:37330909 "keeping integrin inactive."]. LRP12-α4 interaction promotes leading-edge nascent-adhesion turnover, whereas LRP12 knockdown increases nascent adhesions and migration [PMID:37330909 "LRP12 leads to increased NAs and enhanced cell migration."].

The current human GO integrin-binding annotation is an Ensembl Compara IEA with mouse Lrp12 (UniProtKB Q8BUJ9/ENSMUSP00000022916) as the ordered source. Thus the mechanism is compelling exact-ortholog evidence, but it is not a direct human experimental GO assertion. The cached abstract is also abstract-only and does not expose all construct/species details. Human transfer should stay explicitly identified as orthology-based.

## Neuronal-development evidence is mouse-bounded

The direct developmental loss-of-function evidence is from mouse primary neurons and embryonic cortex. Lrp12 knockdown impaired arborization [PMID:26639854 "knockdown of LRP12 in primary neurons results in impaired neuronal arborization."] and in utero silencing produced upper-layer neuron malpositioning [PMID:26639854 "upper cortical layer neurons."]. These results support neuron projection development and migration as conserved, non-core outcomes, not as direct human assays or autonomous molecular activities.

An earlier reporter study identified a mouse Lrp12/Mig13a-positive preplate population [PMID:20439316 "expressed in a subpopulation of preplate neurons that undergo ventrally directed"] whose polarity pattern is disrupted in reeler mice [PMID:20439316 "neuronal polarity do not occur in reeler mutant mice"]. This maps expression and cell behavior; it does not show that Lrp12 is a Reelin receptor or directly transduces Reelin. C. elegans MIG-13 homology likewise provides evolutionary context, not automatic transfer of worm migration mechanisms to human LRP12.

## LDLR-family and trafficking boundaries

PMID:12809483 establishes LDL receptor-related family membership [PMID:12809483 "These results strongly suggested that ST7 was"] and reports cytoplasmic motifs implicated in endocytosis/signaling [PMID:12809483 "implicated in endocytosis and signal transduction."]. Its yeast two-hybrid data support tail interactions with RACK1, NMRK2/MIBP, and ZFYVE9/SARA [PMID:12809483 "revealed that this domain interacts with three proteins involved in signal"].

The accessible abstract does not report binding of an LDL particle, a defined lipoprotein ligand, cargo internalization, or quantified endocytic flux. UniProt's probable internalization language and coated-pit localization are curated from the same study, whose cached record is abstract-only. GO:0005905 (clathrin-coated pit) is not proposed as a new location because the accessible record does not expose the localization experiment needed to assess that more specific assertion. LDL receptor activity, receptor-mediated LDL uptake, and broad vesicle trafficking therefore must not be inferred from family architecture, motifs, or coated-pit annotation alone.

## Cancer and screening evidence

The 1999 human study began with a differential-expression screen and described LRP12/ST7 as a putative receptor whose expression was lower in some transformed lines [PMID:9927190 "expression is downregulated in some malignantly transformed cells, and which may"]. The authors explicitly framed this as an initial characterization [PMID:9927190 "are a first step in characterizing a novel putative receptor protein, whose"]. That paper does not directly establish tumor suppression or general growth regulation.

Later NSCLC work identified LRP12 promoter methylation as a carboplatin-response biomarker [PMID:30029672 "LRP12 methylation status is predictive for therapeutic response of NSCLC"]. This is a patient/PDX epigenetic association and response screen, not a direct assay of normal LRP12 receptor activity.

A 2025 gastric-cancer study did add disease-context perturbation evidence: LRP12 overexpression/knockdown altered proliferation and invasion [PMID:41276539 "both overexpression and knockdown showed that LRP12 promotes GC cell"] and overexpression increased AKT/mTOR phosphorylation [PMID:41276539 "AKT/mTOR pathway, reflected by increased phosphorylation of AKT and mTOR."]. These results are relevant to gastric-cancer cells and mouse xenografts, but should not be generalized into a universal normal-cell growth function or used retrospectively to make PMID:9927190 support an experiment it did not perform.

## Working synthesis boundary

The best-supported molecular model is a single-pass surface protein whose cytoplasmic tail binds α4 integrin and restrains its activation/adhesion dynamics. Neuronal migration and arborization are well-supported mouse developmental outcomes. Cytoplasmic-tail interactors and disease-context AKT/mTOR effects are informative but do not yet define a universal signaling pathway. Ligand identity for the extracellular LDLR-like region, species- and construct-resolved α4-integrin evidence, cargo uptake, isoform-resolved functions, and an experimental full-length structure remain open.
