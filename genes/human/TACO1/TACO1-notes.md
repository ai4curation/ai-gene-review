# TACO1 (Q9BSH4) review notes

## Identity
- TACO1 = Translational Activator of Cytochrome c Oxidase 1 (mitochondrially-encoded COX I / MT-CO1).
- Synonym CCDC44 (coiled-coil domain-containing 44); ORFName PRO0477. HGNC:24316. Gene MIM 612958; disease MIM 619052 (MC4DN8).
- 297 aa; member of the TACO1 / YebC-like family (HAMAP MF_00693; InterPro IPR002876 Transcrip_reg_TACO1-like, IPR029072 YebC-like). Predicted RNA-binding fold. Coiled-coil 191-227; N-terminal disordered region 20-45 (basic/acidic, consistent with a mitochondrial targeting presequence).

## Function (verified biology)
- Mitochondrial-matrix RNA-binding translational activator originally described as binding the MT-CO1 (COX1) mitochondrial mRNA and activating its translation, thereby required for synthesis of the MT-CO1 catalytic core subunit and hence Complex IV (cytochrome c oxidase) assembly [PMID:19503089, UniProt FUNCTION "Acts as a translational activator of mitochondrially-encoded cytochrome c oxidase 1"].
- Refined mechanism (Brischigliaro et al. 2024): TACO1 is the mitochondrial functional counterpart of bacterial EF-P / eukaryotic-archaeal eIF5A/aIF5A. It binds the mitoribosome (mtLSU) and alleviates mitoribosome stalling at polyproline stretches, being required for rapid synthesis of the polyproline-rich COX1 and COX3 subunits [PMID:39036954, "TACO1 binds to the mitoribosome and positively regulates mitochondrial protein synthesis by alleviating polyproline-induced mitoribosome stalling."]. TACO1 cooperates with the N-terminal extension of large-subunit protein bL27m to stabilize the peptidyl-transferase center during elongation.
- So the experimentally-supported MF present in GOA is GO:0097177 mitochondrial ribosome binding (IDA, PMID:39036954). GO:0003729 mRNA binding is present only in the UniProt DR (IEA:Ensembl), consistent with the S4-domain/YebC-like RNA-binding fold and the classical COX1-mRNA-binding model, but is not in the GOA TSV.
- Core BP: positive regulation of mitochondrial translation (GO:0070131, IDA PMID:39036954) and, upstream/context, mitochondrial translation (GO:0032543) and cytochrome c oxidase (Complex IV) assembly (GO:0033617). Reactome R-HSA-9864848 Complex IV assembly.

## Localization
- Mitochondrion (UniProt SUBCELLULAR LOCATION, PMID:19503089); HPA IDA GO:0005739; HTP mito proteome PMID:34800366. As an mRNA-binding matrix translational activator acting on the mitoribosome (matrix face of inner membrane), anatomical location = GO:0005759 mitochondrial matrix. The GOA CC annotations use the broader GO:0005739 mitochondrion; core_functions locates it to the matrix (GO:0005759).

## Disease
- Biallelic TACO1 variants cause Mitochondrial complex IV deficiency, nuclear type 8 (MC4DN8), a late-onset (juvenile) Leigh-syndrome-like neurodegeneration with cytochrome c oxidase deficiency [PMID:19503089 "Mutation in TACO1 ... results in cytochrome c oxidase deficiency and late-onset Leigh syndrome"].

## Existing annotation assessment summary
- BP positive regulation of mitochondrial translation (GO:0070131): IBA + IDA(PMID:39036954) -> ACCEPT (core).
- BP regulation of mitochondrial translation (GO:0070129, IEA/ARBA): parent of the above; ACCEPT (redundant broader, not wrong).
- MF mitochondrial ribosome binding (GO:0097177): IDA(PMID:39036954) experimental -> ACCEPT (core MF); IEA/ARBA duplicate -> ACCEPT.
- CC mitochondrion (GO:0005739): IBA(is_active_in), IEA, IDA(HPA), HTP(PMID:34800366) -> ACCEPT all; matrix (GO:0005759) captured in core_functions.
- MF protein binding (GO:0005515) IPI x many (IntAct interactome/HT screens: PMID:16189514, PMID:32296183, PMID:32814053): bare "protein binding", uninformative; interactors (SAT1, keratins, CALCOCO2, DR1, TRIM23/27, GTF3C3, etc.) are not mitochondrial-matrix partners and reflect Y2H/AP-MS network mapping, not the physiological mitoribosome interaction. Per policy do NOT REMOVE experimental IPIs -> MARK_AS_OVER_ANNOTATED.

## References used
- PMID:19503089 (not cached locally; grounded via UniProt FUNCTION/DISEASE text) — original TACO1 disease/function paper.
- PMID:39036954 (cached, full text) — mechanistic paper; supplies verbatim quotes.
- file:human/TACO1/TACO1-uniprot.txt — UniProt FUNCTION/SUBCELLULAR/DISEASE.
</content>
