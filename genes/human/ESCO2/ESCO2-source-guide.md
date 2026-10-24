# ESCO2 direct-source evidence

The inspected studies support human ESCO2 protein acetylation, chromatin association and promotion of replication-fork progression. The source-described 601-residue Q56NI9-1 and 239-residue Q56NI9-2 remain distinct. None of these readings establishes the short product's localization, activity or interaction repertoire. Artificial deletion constructs are not equated with natural splice products.

## Direct biochemistry and localization: PMID15958495

[Hou and Zou, 2005](https://doi.org/10.1091/mbc.e04-12-1063), available as the [original PMC article](https://pmc.ncbi.nlm.nih.gov/articles/PMC1182326/), provides actual Methods, Results and captions. Figure 1B, whose image was inspected, identifies full EFO2 as 601 residues and the EFO2-C2 construct as residues 215–601. The protein was expressed in *E. coli*, purified through metal-affinity and HiTrap Q chromatography, and assayed with radiolabeled acetyl-CoA. Figure 2A pixels and the accompanying Results show ESCO2-fragment autoacetylation and a negative BSA control. The 2005 paper does not identify the modified residue; the catalytic-mutant series in Figure 2B belongs to ESCO1. It therefore establishes ESCO2 acetyl-transfer capacity directly but is not a purified full-length ESCO2–SMC3 substrate assay.

Methods on cellular fractionation and immunofluorescence, and Results/Figures 5–6, establish association with the chromosome fraction in human HeLa and 293T cells. Tagged human EFO2 is nuclear during interphase, excluded from metaphase chromosomes, and reassociates in telophase. Tagged imaging was used because native-protein antibodies cross-reacted. The authors report little soluble nucleoplasmic ESCO2; the soluble pool was predominantly cytoplasmic. Broad nucleus is retained, and chromosome is refined to chromatin with the independent S-phase fractionation below. Figure 5/6 pixels were not inspected. The original main is accessible despite the immutable normal cache's abstract-only flag.

## Replication kinetics and chromatin: PMID19907496

[Terret et al., 2009](https://doi.org/10.1038/nature08550), [PMC original](https://pmc.ncbi.nlm.nih.gov/articles/PMC2777716/), was read for the operative Results, Methods Summary and figure captions. Figure 3d detects ESCO2 in the chromatin fraction of S-phase human cells. The RPE-derived DCC1 experiment is distinct from ESCO2 RNAi in HeLa cells and from the two Roberts syndrome patient-cell assays. Figures 3e and 4e directly measure fork slowing in ESCO2-deficient conditions; WAPL or PDS5A depletion reverses the HeLa slowing. Non-acetylatable SMC3 links the regulatory effect to cohesin acetylation. ESCO2 thus performs regulatory acetylation work; this does not make it a DNA polymerase or prove the proposed physical geometry of fork obstruction.

The positive direction supports GO:0045740, a current is_a descendant of the imported DNA-replication regulation term. Attempts to retrieve the listed supplementary DOC/PDF returned HTML challenges, so detailed online Methods and supplementary figures remain unread. No figure-pixel inspection is claimed for this paper.

## Cellular SMC3 acetylation: PMID21111234

[Nishiyama et al., 2010](https://doi.org/10.1016/j.cell.2010.10.031) is available in an [author-institution copy of the original](https://publications.mpi-cbg.de/Nishiyama_2010_4332.pdf). Printed pp. 741–742, Figure 3A–F (including its image), and the main Experimental Procedures on pp. 748–749 were inspected. The human experiment compares single ESCO1, single ESCO2 and combined RNAi in S-phase HeLa cells. Only combined depletion substantially reduces chromatin-associated SMC3 K105/K106 acetylation in this assay. The presence of an ESCO2 experiment is established directly, despite the Sororin-focused title.

The purified-enzyme experiment in Figure 3F uses ESCO1 with *Xenopus* chromatin. It is not a recombinant ESCO2 assay. Together with ESCO2's independent autoacetylation, the human perturbation supports protein-lysine acetylation while retaining redundancy and assay limits. Detailed supplemental human-cell Methods and Figure S3 were not recovered or read; the publisher route returned HTTP 403. No cache flag was changed.

## Exact interaction pairs: PMID32296183

[Luck et al., 2020](https://doi.org/10.1038/s41586-020-2188-x), Generation and characterization of HuRI and Discussion, describe nine screens, quadruplicate pairwise retesting and sequence confirmation. The [public PSI table](https://interactome-atlas.org/data/HuRI.psi) contains ESCO2 clone **100014712**, mapped to **Q56NI9-1**, with all four imported partners. Each pair has three method records: screening, array and validated two-hybrid. These are human protein reagents tested in yeast, not evidence of endogenous association in a particular human tissue.

| Imported partner | Verified gene | Partner ORF | Validated PSI line | Recorded screens |
| --- | --- | --- | --- | --- |
| P51114-2 | FXR1 | 100002625 | 153434 | 1, 3 |
| Q08379 | GOLGA2 | 14862 | 144815 | 1 |
| Q15276 | RABEP1 | 11256 | 50813 | 3 |
| Q9NRD5 | PICK1 | 100000407 | 64560 | 3 |

The FXR1 isoform suffix is retained. RABEP1 and PICK1 are mapped to their `-1` products in the table, while imported unsuffixed partner identifiers stay unchanged. GOLGA2 appears in the original as **ENSP00000476265.1**, linked to **ENSG00000167110.17**; [current official Q08379](https://www.uniprot.org/uniprotkb/Q08379/entry) independently links the same stable gene ENSG00000167110. That is a gene-level identity bridge, not an exact sequence-equivalence claim for the archived clone. Current official records likewise verify [FXR1](https://www.uniprot.org/uniprotkb/P51114/entry), [RABEP1](https://www.uniprot.org/uniprotkb/Q15276/entry) and [PICK1](https://www.uniprot.org/uniprotkb/Q9NRD5/entry).

Exact clone sequences, pair-specific orthogonal-assay results and physiological coupling were not established. None of these pairs alone supplies a more specific molecular activity; each supported binding annotation is retained as non-core under the campaign instruction. Detailed supplementary Methods and figure pixels were not inspected.

## Ontology and access boundaries

Current official QuickGO definitions and typed ancestry were captured for all imported direct terms and the three replacements. Chromatin is **part_of**, not **is_a**, chromosome; both the direct parent relation and separate is_a closure were checked. Protein-lysine-acetyltransferase activity specifies acetyl-CoA and a protein lysyl acceptor. Nucleoplasm excludes chromosomes, which matters for interpreting the 2005 fractionation. Imported grouping terms are preserved rather than rewritten mechanically; no new annotation is proposed.

All support entries are reference-only. The source papers' identities and fetched titles remain unchanged. Four manual reference assessments distinguish actual original access from normal-cache availability and partial supplemental access. No new publication quotation, core synthesis or whole-gene completion claim is included.


# ESCO2 database-source evidence

This assessment covers 18 database-origin annotations. The displayed human product Q56NI9-1 has 601 residues; the distinct Q56NI9-2 product has 239. Neither an artificial catalytic fragment nor a mouse localization result establishes functional equivalence of those products. All source records and original normal caches are preserved, and no publication quotations are added.

## Catalytic chemistry and actual reaction role

Current [GO:0004468](https://www.ebi.ac.uk/QuickGO/term/GO:0004468) describes acetyl phosphate acting on free L-lysine. The source mouse IMP from PMID:22101327 instead measures Smc3 protein K105/K106 acetylation after Esco2 deletion. The appropriate supported reaction is [GO:0061733](https://www.ebi.ac.uk/QuickGO/term/GO:0061733), using acetyl-CoA and a protein lysyl acceptor. The human target UniProt record links this chemistry to [RHEA:45948](https://www.rhea-db.org/rhea/45948). Official RHEA SPARQL independently returns the approved protein-lysine reaction and a direct GO:0061733 cross-reference. Several ordinary RHEA HTTP routes failed with 403; the successful SPARQL response, not those failures, supplies the reaction evidence.

Both [chromosomal-arm SMC3 acetylation](https://reactome.org/content/detail/R-HSA-2468039) and [centromeric SMC3 acetylation](https://reactome.org/content/detail/R-HSA-2473152) reach catalyst 2468053 → physical set 2468046 → member 2466400. The last entity is human Q56NI9, residues 1–601. ESCO1 is an alternative member, not an ESCO2 isoform. Both reactions use two acetyl-CoA inputs and produce CoA while converting SMC3 to its K105/K106-acetylated form. Actual input/output component paths reach unmodified SMC3 entity 163009 and acetylated entity 2468050. The [cohesion-establishment pathway](https://reactome.org/content/detail/R-HSA-2468052) includes these catalytic steps, so ESCO2 does chemical work in the process rather than being its substrate.

The ESCO2 participant itself has a nucleoplasm compartment. Its GOA location is therefore traceable to the target, not merely the event. The modeled substrates are chromatin associated; no claim is made that chromatin is an ontology part of nucleoplasm or that a freely soluble enzyme pool was directly demonstrated. HPA supplies separate positive imaging-defined nucleoplasmic evidence. The chromosome annotation is refined to chromatin using the actual human fractionation studies. Broad nucleus is retained across the documented nuclear compartments and conditions.

## Phylogeny and ortholog provenance

The official PTHR45884 tree places human leaf PTN002476323 under ancestral node PTN000118027. The ungapped target alignment equals the 601-residue source sequence. Current IBD rows at this node assert chromatin, nucleus, mitotic sister-chromatid cohesion and protein-lysine acetyltransferase activity; no NOT row interrupts the target path. The family label and target subfamily are read from the official tree. The inference is evaluated as a curated ancestral placement, not by donor count. Human target and ESCO1 experiments are independent selected descendant evidence for localization and chemistry; mouse experiments additionally support cohesion and chromatin context. This review does not claim to have read every yeast, plant or fly donor paper.

Mouse Q8CIB9 is linked by its official Ensembl cross-reference to the imported ENSMUSP00000022613 identifier. Its specific GO records trace XY-body localization to PMID:22699483, pericentric heterochromatin/chromocenter and the chemistry assertion to PMID:22101327, and double-strand-break-site localization to PMID:22614755 and PMID:22699483. Source extensions, including the protein-substrate extension on the IMP and the pericentric-location temporal context, remain literal. No ordinary relationship qualifier is used as biological evidence. The chromosome-architecture and germ-cell differences between species limit extrapolation but do not erase positive ortholog evidence.

## HPA location and product boundaries

[HPA ESCO2](https://www.proteinatlas.org/ENSG00000171320-ESCO2/subcellular) reports supported nucleoplasm localization and additional cell-dependent Golgi/cell-junction staining. HPA027243 and HPA053679 have 83-residue antigens matching canonical residues 313–395 and 4–86. Actual U2OS images for both antibodies were inspected and show nuclear green signal; no quantitative image analysis or new extra-compartment annotation is claimed. The first antigen overlaps part of the sequence retained in the short product, while the second lies in its missing N-terminal region. These sequence facts are not an empirical demonstration of short-product antibody recognition or localization. Original fractionation and microscopy have different operational resolutions; neither establishes universal exclusion from the other compartment.

## Operative original access

### PMID:15958495

[Original article](https://pmc.ncbi.nlm.nih.gov/articles/PMC1182326/); [DOI](https://doi.org/10.1091/mbc.e04-12-1063). Actual Methods blocks 14,18; Results/captions 25,28–29,37,41–42,44,46–48 (Figures 2,5–6).

Human ESCO2 fragment autoacetylation with acetyl-CoA and human chromosomal/nuclear localization support catalytic capacity and location. EFO2-C2 is an engineered fragment; its assay is not a purified full-length ESCO2–SMC3 reaction. The catalytic-mutant controls in Figure 2B are ESCO1. No figure pixels or supplementary material independently inspected in this database lane. Little soluble nucleoplasmic protein under the original fractionation conditions does not negate all other imaging contexts.

### PMID:19907496

[Original article](https://pmc.ncbi.nlm.nih.gov/articles/PMC2777716/); [DOI](https://doi.org/10.1038/nature08550). Actual main blocks 15–26, including Figure 3d, Figure 4 captions and Methods Summary.

S-phase human chromatin fractions contain ESCO2; human ESCO2 depletion and patient-cell fork phenotypes have distinct cellular contexts. Chromatin targeting and the regulatory role are not DNA polymerase catalysis. No figure pixels or detailed online/supplemental Methods independently read. Fork obstruction geometry remains a model.

### PMID:21111234

[Original article](https://publications.mpi-cbg.de/Nishiyama_2010_4332.pdf); [DOI](https://doi.org/10.1016/j.cell.2010.10.031). Author-original text lines 216–285, printed pp. 741–742 Results and Figure 3A–D caption; main Experimental Procedures lines 718–765, p. 748.

Human S-phase HeLa combined ESCO1/ESCO2 RNAi reduces SMC3 K105/K106 acetylation and Sororin association. The source does contain ESCO2 experiments, but its separate recombinant-enzyme experiment is ESCO1 with Xenopus chromatin. No independent figure-pixel inspection, no detailed supplemental human-cell Methods or Figure S3 read. Single-depletion redundancy is retained.

### PMID:22101327

[Original article](https://pmc.ncbi.nlm.nih.gov/articles/PMC3252581/); [DOI](https://doi.org/10.1038/emboj.2011.381). Actual main paragraphs 0–47, including Results 14–16,25–27 and Methods 40–47; actual Figure 3/4/7 captions separately read.

Mouse Esco2 is enriched at pericentric heterochromatin/chromocenter cores; loss reduces Smc3 K105/K106 acetylation and Sororin recruitment. This is protein acetylation evidence, not acetyl-phosphate/free-lysine chemistry. No figure pixels or supplementary Methods inspected. Human short-product compensation in Discussion 32 is explicitly a hypothesis, not observed activity. Mouse and limited human HeLa supplemental statements remain distinct.

### PMID:22699483

[Original article](https://pmc.ncbi.nlm.nih.gov/articles/PMC3463413/); [DOI](https://doi.org/10.1095/biolreprod.112.099978). Actual article blocks 17–88: Methods 21–36, Results 39/45/51 and Figures 1–8 captions, Discussion 81–88.

Mouse pachytene spermatocytes show XY-body ESCO2/H2AFX colocalization, and E18.5 oocytes show H2AFX-associated clumps beside synaptonemal complexes. Antibody A301-689A, 65-kDa immunoblot and negative staining controls are stated. No figure pixels inspected. Break-associated location is measured by imaging, not direct lesion mapping, binding to exposed DNA ends, or a purified repair reaction. RA-induced expression is not an extra core activity.

### PMID:22614755

[Original article](https://doi.org/10.4161/nucl.20440); [DOI](https://doi.org/10.4161/nucl.20440). Verified identifier/metadata and bounded failed publisher access only; no operative original body.

The mouse donor carries this reference for break-site localization. Independent original PMID:22699483 supplies the positive localization evidence used here. Full original unavailable; no negative or wrong-gene conclusion is inferred.

## Core evidence and assay boundaries

The one catalytic unit uses [GO:0061733 protein-lysine-acetyltransferase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0061733), with [mitotic sister-chromatid cohesion](https://www.ebi.ac.uk/QuickGO/term/GO:0007064) and [positive regulation of DNA replication](https://www.ebi.ac.uk/QuickGO/term/GO:0045740). The two processes are not ancestor/descendant duplicates. Their broader parent processes and a generic protein-acetylation process are not added as extra core coverage. [Chromatin](https://www.ebi.ac.uk/QuickGO/term/GO:0000785) belongs to the cellular anatomical entity branch in the current ontology; no stable membership in cohesin is inferred from being its acetyltransferase.

The [2005 human original](https://doi.org/10.1091/mbc.e04-12-1063), Methods and Results/Figures 2–3 and 5–6, distinguishes purified ESCO2-fragment autoacetylation from human-cell cohesion and localization. The synthesis additionally read the source's single and double depletion results and metaphase-spread caption (main blocks 30–36); these are positive human cohesion data. The [2010 original](https://doi.org/10.1016/j.cell.2010.10.031), printed pp. 741–742/Figure 3, requires combined ESCO1/ESCO2 depletion to strongly lower the measured human SMC3 acetylation endpoint. Its purified ESCO1/Xenopus experiment is separate. The [mouse Esco2 study](https://doi.org/10.1038/emboj.2011.381), Results and Figure 7, shows a stage-dependent SMC3 K105/K106 and Sororin phenotype following Esco2 loss. Together these support the conserved catalytic mechanism without treating any one assay as a purified full-length human ESCO2–SMC3 reaction.

Positive replication regulation has gene-specific human evidence in the [2009 original](https://doi.org/10.1038/nature08550): Results on replication dynamics and Figure 4e describe fork slowing in ESCO2-depleted HeLa cells and rescue by WAPL or PDS5A depletion. The non-acetylatable SMC3 experiment and Roberts syndrome cells are complementary tests, not the same perturbation. Methods Summary describes RNAi and sequential nucleotide-label DNA-fiber measurements. The proposed physical obstruction geometry remains a model, and ESCO2 is not assigned DNA polymerase activity. The core synthesis re-read these actual main sections/captions and the corresponding 2005, 2010 and mouse sections. It did not inspect additional paper figure pixels or supplements; the integrated reference assessments retain the direct review's earlier, explicitly recorded figure access.

Neither the engineered ESCO2 catalytic fragment nor mouse localization establishes function of the 239-residue natural product. Specialized mouse meiotic localization remains outside the core. No histone-acetyltransferase activity or additional process annotation is inferred.
