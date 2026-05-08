# rdgBbeta (Drosophila melanogaster) - Research Notes

## Gene Identity

- **Gene symbol**: rdgBbeta (retinal degeneration B homolog beta)
- **UniProt**: Q9U9P7 (PITC1_DROME)
- **FlyBase**: FBgn0027872
- **CG number**: CG17818
- **Human ortholog**: PITPNC1 (Q9UKF7) -- cytoplasmic phosphatidylinositol transfer protein 1
- **273 amino acids**, 31.7 kDa, soluble cytoplasmic protein

## Protein Family and Domain Architecture

rdgBbeta belongs to the PtdIns transfer protein family, PI transfer class IIB subfamily.
It contains:
- IPR023393: START-like domain superfamily (residues 2-263)
- IPR055261: Phosphatidylinositol transfer protein, N-terminal domain (residues 2-244)
- IPR001666: Phosphatidylinositol transfer protein (family) (residues 3-254 and multiple sub-regions)

Key structural feature: rdgBbeta contains ONLY the PITP domain plus a short disordered C-terminal tail.
It lacks transmembrane domains and the conserved C-terminal domain found in other rdgB-family proteins
(rdgB/RdgBalpha, Nir2, Nir3). This makes it a soluble, cytoplasmic lipid transfer protein.

## Lipid Binding Specificity -- Key Distinction from Class I PITPs

The human ortholog PITPNC1 has been characterized biochemically [PMID:22822086]. Critical finding:
- PITPNC1/rdgBbeta binds and transfers **phosphatidylinositol (PI)** and **phosphatidic acid (PA)**
- It does **NOT** significantly bind phosphatidylcholine (PC)
- This distinguishes it from Class I PITPs (PITPalpha, PITPbeta/vibrator/giotto) which bind both PI and PC

[PMID:22822086 "the lipid binding properties of this protein are distinct to Class I PITPs because, besides phosphatidylinositol (PI), RdgBbeta binds and transfers phosphatidic acid (PA) but hardly binds phosphatidylcholine"]

PITPNC1/RdgBbeta is the first lipid-binding protein identified that can bind and transfer PA.
When purified from E. coli, it was preloaded with PA and phosphatidylglycerol.

## Protein Interactions (human ortholog)

[PMID:21728994] The C-terminus of RdgBbeta binds 14-3-3 proteins via two tandem phosphorylated sites
(Ser274 and Ser299 in human). The PITP domain interacts with ATRAP (angiotensin II type I 
receptor-associated protein), an integral membrane protein that recruits RdgBbeta to membranes.
14-3-3 shields PEST sequences; loss of 14-3-3 binding accelerates proteasomal degradation.

## Original Cloning (human ortholog)

[PMID:10531358 Fullwood et al. 1999] Cloned human rdgBbeta by EST database searching for rdgB homologs.
Key findings:
- 333 amino acids (human), N-terminal PITP-like domain + short C-terminal domain
- No transmembrane domains (unlike other rdgB family members)
- Cytoplasmic localization by immunofluorescence
- Ubiquitous expression (highest in heart, muscle, kidney, liver, leukocytes)
- In vitro PI transfer activity comparable to other PITP-like domains

## Drosophila-specific Data

### Expression
- Mass spectrometry detected rdgBbeta protein in adult head tissue, associated with membranes (FlyBase)
- Bgee: expressed in adult middle midgut class I enteroendocrine cell and 98 other cell types/tissues
- Weak testis specificity index (-0.19), indicating modest UNDER-representation in testis

### Mutant Phenotypes
- Two alleles (rdgBbeta^EP2360 and rdgBbeta^G8057) ameliorate ALS-like phenotype
  when modeled with Vap33^P58S mutations (FlyBase allele reports)
- This connects rdgBbeta to phosphoinositide metabolism in neurodegeneration

### Connection to ALS/neurodegeneration
[PMID:23492670] Drosophila ALS8 model: Vap33-P58S expression causes neurodegeneration through
increased phosphoinositide levels. Sac1 phosphatase is sequestered into aggregates.
While this paper does not mention rdgBbeta directly, the FlyBase genetic interaction data 
suggests rdgBbeta alleles modify this phenotype, consistent with its role in PI metabolism.

## Relationship to Other Drosophila PITPs

Important: rdgBbeta should NOT be confused with:
- **rdgB/RdgBalpha** (FBgn0003218): membrane-associated PITP with additional domains (FFAT, DDHD),
  essential for photoreceptor maintenance, required for phototransduction
- **vibrator** (vib): Class I PITP, required for cytokinesis (cleavage furrow ingression) [PMID:16684816]
- **giotto** (gio): Class I PITP, required for both mitotic and meiotic cytokinesis [PMID:16431372]

The cytokinesis, meiosis, and spermatocyte division phenotypes in Drosophila are associated with
vibrator and giotto mutants, NOT rdgBbeta.

## Cancer Biology (human PITPNC1)

[PMID:26977884] PITPNC1 is amplified in breast cancer and overexpressed in metastatic breast,
melanoma, and colon cancers. It promotes malignant secretion by binding Golgi-resident PI4P and
localizing RAB1B to the Golgi, driving secretion of pro-invasive and pro-angiogenic factors 
(HTRA1, MMP1, FAM3C, PDGFA, ADAM10).

## BioReason Prediction Assessment

The BioReason deep-research file makes several claims that need verification:

1. **GO:0008525 phosphatidylcholine transporter activity** -- INCORRECT. Literature shows rdgBbeta/PITPNC1
   "hardly binds phosphatidylcholine" [PMID:22822086]. This is a Class I PITP property, not Class IIB.

2. **Cytokinesis functions (GO:0007110, GO:0007111, GO:0007112, GO:0000916, GO:0036090, GO:0048137)** -- 
   NOT SUPPORTED for rdgBbeta. These functions are associated with vibrator and giotto (Class I PITPs),
   not rdgBbeta. No published evidence connects rdgBbeta to cytokinesis or meiotic division.

3. **GO:0000212 meiotic spindle organization** -- NOT SUPPORTED. No evidence for rdgBbeta.

4. **GO:0005794 Golgi apparatus** -- Partially supported for human PITPNC1 in cancer context [PMID:26977884],
   but not demonstrated for Drosophila rdgBbeta.

5. **GO:0032154 cleavage furrow** -- NOT SUPPORTED. Cleavage furrow association is for vibrator, not rdgBbeta.

6. **GO:0031965 nuclear membrane** -- NOT SUPPORTED. No evidence for rdgBbeta.

7. **PI transfer activity (GO:0008526)** -- CORRECT. Well-supported by ortholog data.

8. **Cytoplasmic localization (GO:0005737)** -- CORRECT. Supported by multiple lines of evidence.

The BioReason model appears to have conflated the functions of different PITP family members,
attributing Class I PITP functions (cytokinesis, PC binding) to this Class IIB PITP.
