# samsn1a notes

## Provenance and setup

- Record: B3DH22 (TrEMBL, 621 aa), ZFIN ZDB-GENE-030131-8639, Ensembl ENSDARG00000054543 (chr15).
- Paralog: samsn1b (A0A8M2BH30). Pair drawn at random for DANRE_DUPLICATION batch 4
  (PANTHER `TGD_tree`, Ensembl Compara duplication node Osteoglossocephalai).
- Deep research was not available for this gene (Edison returned 402 Payment Required; the OpenAI
  key is invalid). Literature was searched by hand through Europe PMC (queries: `samsn1a OR samsn1b`;
  `(samsn1 OR HACS1 OR SASH2 OR NASH1) AND zebrafish`; title search for HACS1/SAMSN1/NASH1).
- No functional study of zebrafish samsn1a or samsn1b exists. Zebrafish mentions are marker-gene
  statements in single-cell RNA-seq papers.

## Mammalian SAMSN1 (HACS1, SLy2, NASH1)

- SH3-SAM adaptor, hematopoietic, human chr21q11.2
  [PMID:11536050 "HACS1 encodes a 441 amino acid protein that is differentially expressed in hematopoietic cells and has restricted expression in human tissues."]
  [PMID:11536050 "Immunostaining and cellular fractionation studies localized the HACS1 protein predominantly to the cytoplasm."]
- NASH1 identified in mast cells, nuclear
  [PMID:11594764 "In consistent with the presence of NLS, Nash1 was localized in the nucleus."]
- Up-regulated in B-cell activation; binds tyrosine-phosphorylated proteins and PIR-B
  [PMID:15381729 "HACS1 associates with tyrosine-phosphorylated proteins after B cell activation and binds in vitro to the inhibitory molecule paired Ig-like receptor B."]
  [PMID:15381729 "Hacs1 is expressed in the cytoplasm of most of the positive cells but is also present in nuclei of some cells (inset in spleen bottom panel)."]
- Mouse knockout: enhanced B-cell responses (source of the IBA for negative regulation of B cell
  activation, MGI:1914992)
  [PMID:19923443 "Purified splenic B cells from Hacs1(-/-) mice showed increased cell proliferation on BCR (B-cell receptor) stimulation."]
  [PMID:19923443 "This study suggests that Hacs1 is an immunoinhibitory adaptor that might be a useful target for immune suppression therapy."]
- SH3 domain binds a motif near ITIM3 of PIRB (NMR structure)
  [PMID:33188360 "Here, we describe the interaction between the HACS1 SH3 domain and a sequence near the third immunoreceptor tyrosine-based inhibition motif (ITIM3) of the paired immunoglobulin receptor B (PIRB)."]
- Family: SLy1/SASH3, SLy2/HACS1 (SAMSN1), SASH1/SLy3
  [PMID:33710696 "Despite their obvious homology, the three SLy/SASH1-members fundamentally differ with regard to their expression and function in intracellular signaling."]

## Zebrafish / teleost expression

- Retinal bipolar-cell marker in two independent zebrafish scRNA-seq studies:
  [PMID:37988404 "UMAP plots of vsx1 and samsn1a, known and novel markers of bipolar cells, respectively, showed high counts in cluster 15 (Figure 8E and F)."]
  [PMID:36047082 "samsn1a , vsx1 , neurod4 (BPs)"]
- Channel catfish spleen single-nucleus data place samsn1a in a myeloid cluster (catfish, an
  otophysan like zebrafish; not zebrafish data):
  [PMID:39325796 "Cluster 11 was defined by upregulated expression of myeloid-related genes such as dbn1 (drebrin 1), foxp4 (forkhead box P4), samsn1a (SAM domain, SH3 domain and nuclear localization signals 1), csf1rb (colony stimulating factor 1 receptor), mafba (MAF bZIP transcription factor B) and csf3r (colony stimulating factor 3 receptor)."]
- My analysis (file:DANRE/samsn1a/samsn1a-bioinformatics/RESULTS.md):
  - ZFIN curated in situ (Covassin et al. 2006, ZDB-PUB-060927-11): samsn1a in blood, macrophage and
    solid lens vesicle at prim-5. samsn1b: epiphysis (pineal) and retinal photoreceptor layer
    (Thisse et al. 2004 direct submission).
  - E-ERAD-475: samsn1a zygotic, rising from hatching to 28 TPM at day 5; samsn1b has a small
    gastrula peak (5 TPM) then silent until larval stages (10-17 TPM).
  - Bgee: both copies have RNA-seq calls in granulocyte, spleen, head kidney, retina, gill, intestine,
    liver; samsn1a has top scores in granulocyte/spleen/head kidney, samsn1b in retina.

## Protein

- samsn1a and samsn1b are only 37.8% identical over the full length, but SH3 domains are 82.3% and
  77.4% identical to human SAMSN1 SH3; both keep the 14-3-3 motif region. Both zebrafish proteins
  (621/676 aa) and the gar protein (690 aa) are much longer than human SAMSN1 (373 aa).
  No relative-rate asymmetry (gar outgroup).

## Annotation decisions

- Only two IBA process rows on each copy. Both accepted; the B-cell row is a phylogenetic inference
  from the mouse knockout, consistent with the hematopoietic expression of both copies. No NEW rows.
