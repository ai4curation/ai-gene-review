---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-11T22:29:24.984547'
end_time: '2026-01-11T22:43:43.879283'
duration_seconds: 858.89
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: WT1
  gene_symbol: WT1
  uniprot_accession: P19544
  protein_description: 'RecName: Full=Wilms tumor protein; AltName: Full=WT33;'
  gene_info: Name=WT1;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the EGR C2H2-type zinc-finger protein family.
  protein_domains: Wilms_tumour_N. (IPR000976); Znf_C2H2_sf. (IPR036236); Znf_C2H2_type.
    (IPR013087); WT1 (PF02165); zf-C2H2 (PF00096)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 15
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P19544
- **Protein Description:** RecName: Full=Wilms tumor protein; AltName: Full=WT33;
- **Gene Information:** Name=WT1;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the EGR C2H2-type zinc-finger protein family.
- **Key Domains:** Wilms_tumour_N. (IPR000976); Znf_C2H2_sf. (IPR036236); Znf_C2H2_type. (IPR013087); WT1 (PF02165); zf-C2H2 (PF00096)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "WT1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'WT1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **WT1** (gene ID: WT1, UniProt: P19544) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# WT1 (Wilms Tumor Protein): A Comprehensive Functional Annotation Report

## 1. Introduction and Overview

The Wilms tumor 1 gene (WT1) encodes a zinc finger transcription factor that plays essential roles in the development of the urogenital system and functions as both a tumor suppressor and oncogene depending on cellular context [toska-2014-wt1-review-abstract]. First identified in 1990 as a tumor suppressor gene associated with Wilms tumor (nephroblastoma), WT1 has since emerged as a remarkably complex master regulator of organogenesis, differentiation, and cellular homeostasis [rauscher-1993-wt1-tumor-suppressor-abstract]. The protein contains a proline- and glutamine-rich N-terminal domain and four C-terminal C2H2-type zinc fingers of the Krüppel class, which mediate both DNA and RNA binding [toska-2014-wt1-review-abstract]. WT1 is characterized by its capacity to function as either a transcriptional activator or repressor depending on the presence of specific cofactors, cellular context, and post-translational modifications.

WT1 belongs to the EGR (Early Growth Response) C2H2-type zinc-finger protein family and demonstrates high-affinity DNA binding to GC-rich sequences closely related to the EGR-1 consensus site [hamilton-1998-dna-binding-abstract]. The remarkable complexity of WT1 biology stems from the existence of at least 24 distinct protein isoforms generated through alternative splicing and alternate translation initiation sites, with the two most functionally significant splice variants differing by the presence or absence of three amino acids (lysine-threonine-serine, KTS) between zinc fingers 3 and 4 [laity-2000-kts-splicing-abstract]. This single modification dramatically alters the protein's DNA binding capacity and subcellular localization, enabling a single gene to serve multiple distinct cellular functions [larsson-1995-localization-abstract].

## 2. Protein Structure and DNA Binding Properties

The WT1 protein architecture comprises several functionally distinct domains. The N-terminus contains a proline- and glutamine-rich region capable of transcriptional regulation, with a defined repression domain (residues 71-180) and a separate activation domain (residues 180-250) [toska-2014-wt1-review-abstract]. The C-terminal region houses four canonical Cys2-His2 zinc fingers that constitute the nucleic acid binding domain.

Structural studies using X-ray crystallography and NMR spectroscopy have elucidated the molecular basis of WT1-DNA interaction [stoll-2007-wt1-structure-abstract]. The second, third, and fourth zinc finger domains insert deep into the major groove of DNA where they make base-specific contacts. Zinc fingers 2 and 3 are primarily responsible for most of the binding affinity and can function as a minimal DNA binding domain, while zinc finger 4 is indispensable for target specificity, pinpointing a particular position on the target sequence and preventing register promiscuity [stoll-2007-wt1-structure-abstract]. In contrast, zinc finger 1 functions primarily to anchor WT1 to the DNA by amplifying binding affinity, although it does not contribute significantly to sequence specificity.

Quantitative binding studies have demonstrated that recombinant WT1 zinc fingers bind to the dodecamer DNA sequence GCG-TGG-GCG-TGT with high affinity, exhibiting a dissociation constant (Kd) of 1.14 × 10⁻⁹ M under physiological conditions [hamilton-1998-dna-binding-abstract]. The consensus DNA binding sequence for WT1 has been characterized as 5'-GCG(T/G)GGGCG-3', which is closely related to but distinct from the EGR-1 binding site [hamilton-1998-dna-binding-abstract]. Thermodynamic analysis revealed that WT1-DNA interaction is an entropy-driven process, distinguishing it from the related EGR1 protein whose DNA binding is favored by both enthalpy and entropy [hamilton-1998-dna-binding-abstract].

## 3. Alternative Splicing and Isoform-Specific Functions

Alternative splicing generates functionally distinct WT1 isoforms that perform remarkably different cellular roles. The two most critical splice variants involve exon 5 (which adds 17 amino acids in the central region) and an alternative splice donor site at exon 9 that inserts the three amino acids KTS (lysine-threonine-serine) between zinc fingers 3 and 4 [toska-2014-wt1-review-abstract]. The +KTS/-KTS splicing event has profound functional consequences.

The molecular basis for the functional differences between +KTS and -KTS isoforms was elucidated by NMR structural studies demonstrating that the KTS insertion increases the flexibility of the linker between fingers 3 and 4, abrogating the binding of the fourth zinc finger to its cognate site in the DNA major groove [laity-2000-kts-splicing-abstract]. Consequently, the -KTS isoform binds EGR-like recognition elements with high affinity and functions primarily as a transcription factor, while the +KTS isoform binds DNA weakly and is preferentially associated with the splicing machinery [laity-2000-kts-splicing-abstract].

The physiological importance of maintaining the correct ratio of +KTS to -KTS isoforms (normally approximately 2:1) is dramatically illustrated by Frasier syndrome, in which mutations disrupting the +KTS splice site alter this ratio to 1:2, resulting in severe abnormalities in kidney and gonad development despite the production of structurally normal WT1 protein [laity-2000-kts-splicing-abstract]. Mouse knockout studies ablating either the +KTS or -KTS isoform specifically have provided direct evidence that these splice variants perform distinct essential functions in embryonic development. Recent studies have demonstrated that the -KTS splice variant is essential for ovarian determination in mice, highlighting the isoform-specific roles in sex determination pathways.

## 4. Subcellular Localization and Nuclear Functions

The subnuclear localization of WT1 is splice form-dependent, providing additional insight into the distinct functions of the isoforms [larsson-1995-localization-abstract]. The +KTS isoforms preferentially colocalize with molecules implicated in mRNA splicing in characteristic nuclear speckles, while -KTS proteins colocalize predominantly with transcription factors [larsson-1995-localization-abstract]. Nuclear speckles are now recognized as storage sites from which splicing factors are recruited to new sites of transcription, where pre-mRNA splicing occurs cotranscriptionally.

The association of WT1 with the splicing machinery has been demonstrated through its interaction with U2AF65, an essential splice factor that binds to the polypyrimidine tract upstream of the 3' splice site and promotes U2 snRNA annealing to the branch point [davies-1998-u2af65-abstract]. WT1 associates specifically with U2AF65 in a manner enhanced by the KTS insertion, and WT1 can be incorporated directly into spliceosomes [davies-1998-u2af65-abstract]. Both the amino-terminal RS domain and linker region of U2AF65 are required for WT1 binding. Additionally, WT1 interacts with the splicing regulator RBM4, and overexpressed WT1(+KTS) can abrogate the effects of RBM4 on splice-site selection, providing evidence for a post-transcriptional regulatory role [davies-1998-u2af65-abstract].

Post-translational modifications also regulate WT1 subcellular distribution. Phosphorylation by PKA or PKC at serines 365 and 393 within the zinc finger domain inhibits DNA binding and results in cytoplasmic retention of WT1, effectively suppressing its transcriptional functions while leaving RNA-binding activity intact [toska-2014-wt1-review-abstract]. WT1 is also SUMOylated at lysine residues 73 and 177 within the repression domain, though the functional consequences of this modification remain unclear. The WT1-binding partner BASP1 is SUMOylated by SUMO-3, raising the potential for differential regulation of WT1 and its cofactors.

## 5. Transcriptional Activation and Repression Mechanisms

WT1 exhibits remarkable functional duality, acting as either a transcriptional activator or repressor depending on cellular context and cofactor availability [toska-2014-wt1-review-abstract]. This dichotomous behavior enables WT1 to orchestrate complex developmental programs and respond appropriately to different physiological signals.

A key determinant of WT1's activator versus repressor function is its physical and functional interaction with the tumor suppressor p53. Coimmunoprecipitation experiments demonstrated that p53 and WT1 physically associate in cells, and this interaction profoundly modulates transcriptional output [maheswaran-1993-p53-interaction-abstract]. In the absence of p53, WT1 functions as a potent transcriptional activator of EGR1-like promoter sequences rather than as a repressor. Conversely, WT1 enhances p53's ability to transactivate target promoters such as the muscle creatine kinase promoter, indicating a cooperative relationship between these tumor suppressors [maheswaran-1993-p53-interaction-abstract]. Subsequent studies showed that WT1 expression can stabilize p53 protein, enhance its DNA binding to target sequences, and inhibit p53-mediated apoptosis while not affecting p53-mediated cell cycle arrest. This functional interaction may explain the elevated levels of wild-type p53 protein observed in Wilms' tumors.

The conversion of WT1 from a transcriptional activator to a repressor is also mediated through its interaction with the corepressor BASP1 (brain acid soluble protein 1) [toska-2012-basp1-hdac-abstract]. The N-terminal myristoylation of BASP1 is essential for eliciting transcriptional repression at WT1 target genes. Mechanistically, myristoylated BASP1 binds to nuclear phosphatidylinositol 4,5-bisphosphate (PIP2), which leads to the recruitment of PIP2 to the promoter regions of WT1-dependent target genes. This association with PIP2 is required for the interaction of BASP1 with histone deacetylase 1 (HDAC1), enabling chromatin deacetylation and gene silencing [toska-2012-basp1-hdac-abstract].

The transcriptional repression complex also includes prohibitin as an essential component [toska-2014-prohibitin-abstract]. Prohibitin interacts with BASP1, colocalizes with BASP1 in the nucleus, and is recruited to the promoter regions of WT1 target genes. Prohibitin and BASP1 cooperate to recruit the chromatin remodeling factor BRG1 (brahma-related gene 1) to WT1-responsive promoters, resulting in the dissociation of the histone acetyltransferase CBP from the promoter region and subsequent gene silencing [toska-2014-prohibitin-abstract].

The interplay between WT1 and BASP1 is dynamically regulated during cellular differentiation. In podocyte precursor cells, both WT1 and BASP1 occupy the promoters of genes including Bak, c-myc, and podocalyxin. During differentiation-dependent upregulation of podocalyxin expression, BASP1 occupancy of the podocalyxin promoter decreases while WT1 remains bound, allowing transcriptional activation. The regulation of BASP1 promoter occupancy involves sumoylation of BASP1, which can result in its redistribution within the nucleus from chromatin to the nuclear matrix [toska-2012-basp1-hdac-abstract].

## 6. Target Genes and Developmental Pathways

WT1 regulates a diverse array of target genes involved in development, differentiation, cell growth, and apoptosis. ChIP-chip analysis coupled with morpholino knockdown experiments in embryonic kidney explants has identified many WT1 targets in the context of kidney development [toska-2014-wt1-review-abstract].

In kidney development and podocyte function, WT1 is essential for the mesenchymal-to-epithelial transition (MET) of metanephric mesenchyme and subsequent nephron formation. WT1 controls metanephric mesenchyme self-renewal and proliferation by regulating FGF and BMP-pSMAD signaling pathways as well as Sall1 and Pax2. WT1 drives mesenchyme differentiation and MET by targeting Fgf8 and Wnt4, and defines podocyte identity by activation of podocyte-specific transcription factors including Mafb, Lmx1b, FoxC2, and Tcf21.

A critical direct target of WT1 in podocytes is nephrin (encoded by NPHS1), a transmembrane protein that is a constituent of the podocyte slit diaphragm and essential for the glomerular filtration barrier [wagner-2004-nephrin-abstract]. WT1 binds to a specific responsive element in the nephrin promoter and activates transcription more than 10-fold. Transgenic mouse analysis confirmed that this WT1 binding site is required for podocyte-specific nephrin expression in vivo [wagner-2004-nephrin-abstract]. Deletion of WT1 from adult kidneys results in severe podocyte injury, failure of the glomerular filtration barrier, and loss of expression of key podocyte genes.

In gonad development, WT1 functions upstream of SF1 (steroidogenic factor 1) and is essential for early gonadogenesis. The -KTS isoform of WT1, but not the +KTS form, directly binds to and transactivates the Sf1 promoter through four identified binding sites [wilhelm-2002-gonad-sf1-abstract]. WT1 also directly regulates the sex-determining gene SRY by activating its expression via proximal EGR-1-like DNA-binding sequences in the core promoter [hossain-2001-sry-abstract]. Mutant WT1 proteins found in Denys-Drash syndrome patients fail to activate the SRY promoter, providing a molecular explanation for the gonadal abnormalities in these patients [hossain-2001-sry-abstract]. The transcriptional co-factor CITED2 acts with WT1 and SF1 to increase SRY expression to levels sufficient for efficient testis development initiation.

Additional categories of WT1 target genes include growth factor receptors (IGF1R, EGFR, PDGF-A), signaling molecules (amphiregulin, sprouty, Wnt4, CSF-1), cell cycle regulators (p21, c-Myc, cyclin D2), apoptosis regulators (BCL2, A1/BFL1, BAK), and epigenetic factors (DNMT3A, histone modifiers Jmjd1a, Myst2, Rest) [toska-2014-wt1-review-abstract].

Beyond the urogenital system, WT1 plays an essential role in cardiac development, specifically in the epicardium, the epithelial tissue lining the heart surface. WT1 is expressed in the proepicardium and developing epicardium, where it is required for epithelial-to-mesenchymal transition (EMT) that generates cardiovascular progenitor cells [vongise-2011-epicardial-emt-abstract]. Genetic knockout studies demonstrated that Wt1-null epicardium fails to undergo EMT, resulting in diminished myocardial proliferation and impaired coronary plexus formation. WT1 regulates epicardial EMT through multiple signaling pathways including canonical Wnt/β-catenin signaling (via reduced Lef1 and Ctnnb1 expression in knockouts), non-canonical Wnt5a signaling, and retinoic acid signaling through direct regulation of Raldh2 expression [vongise-2011-epicardial-emt-abstract]. Notably, while WT1 drives mesenchymal-to-epithelial transition (MET) in the developing kidney, it promotes the reverse process (EMT) in the epicardium, demonstrating that WT1's effects on epithelial-mesenchymal transitions are highly context-dependent. The epicardial EMT generates cardiac fibroblasts, vascular smooth muscle cells, and a subset of coronary endothelial cells. Intriguingly, WT1 is reactivated in adult epicardium following myocardial infarction, suggesting a role in cardiac repair responses.

## 7. Role in Disease: Wilms Tumor and Associated Syndromes

WT1 was originally identified as a tumor suppressor gene mutated in Wilms tumor, a pediatric kidney cancer. However, the relationship between WT1 and cancer is complex, as WT1 can function as either a tumor suppressor or oncogene depending on cellular context [toska-2014-wt1-review-abstract].

Denys-Drash syndrome (DDS) is caused by dominant-negative mutations in WT1 and is characterized by the triad of congenital nephropathy (diffuse mesangial sclerosis), Wilms tumor susceptibility, and disorders of sexual development [rauscher-1993-wt1-tumor-suppressor-abstract]. The majority of DDS patients harbor point mutations in one WT1 allele, frequently missense mutations affecting the zinc finger DNA-binding domains. Structural studies have categorized these mutations as either destabilizing zinc finger structures or replacing critical base-contact residues [stoll-2007-wt1-structure-abstract]. Interestingly, some DDS mutations enhance WT1 binding to U2AF65, suggesting a potential gain-of-function mechanism contributing to disease pathogenesis [davies-1998-u2af65-abstract].

Frasier syndrome is caused by mutations in intron 9 of the WT1 gene that prevent production of the +KTS isoform, thereby altering the normal +KTS/-KTS ratio from 2:1 to 1:2. Unlike DDS, Frasier syndrome patients produce structurally normal WT1 proteins but with an imbalanced isoform ratio [laity-2000-kts-splicing-abstract]. Frasier syndrome is characterized by focal segmental glomerulosclerosis (rather than the diffuse mesangial sclerosis of DDS), male pseudohermaphroditism, and gonadoblastoma susceptibility, but no increased risk of Wilms tumor because the -KTS isoform retains tumor suppressor function.

Beyond Wilms tumor, WT1 is overexpressed in various adult malignancies including acute myeloid leukemia (AML), where it serves as a prognostic marker and therapeutic target. In AML, WT1 is mutated in a mutually exclusive manner with TET2, IDH1, and IDH2. WT1 is also aberrantly expressed in solid tumors derived from tissues that normally lack WT1 expression, including colon, breast, desmoid tumors, and brain tumors [toska-2014-wt1-review-abstract]. In these contexts, WT1 appears to function as an oncogene rather than a tumor suppressor.

## 8. RNA Binding and Post-Transcriptional Functions

In addition to its well-characterized role as a transcription factor, WT1 binds RNA and participates in post-transcriptional gene regulation. The zinc finger domain of WT1 can bind both DNA and RNA, with different subsets of zinc fingers contributing to each interaction [caricasole-1996-rna-binding-abstract]. While zinc fingers 2, 3, and 4 are required for high-affinity DNA binding, zinc finger 1—which is dispensable for DNA binding—is more important for RNA binding. Consequently, the KTS insertion, which disrupts zinc finger 4 function, has minimal effect on RNA affinity, explaining why both +KTS and -KTS isoforms bind RNA with similar affinity despite their dramatically different DNA binding properties.

Structural studies have revealed that WT1 zinc fingers 1-3 bind in a widened major groove of RNA stem-loop structures, with a bulge nucleotide facilitating groove widening [caricasole-1996-rna-binding-abstract]. Zinc fingers 2 and 3 make specific contacts with nucleobases in a conserved AUGG sequence within the RNA helical stem. The +KTS isoform has been shown to associate with actively translating polysomes in the cytoplasm and can shuttle between nucleus and cytoplasm, suggesting roles in mRNA transport and translation regulation.

The WT1(+KTS) isoform functions with a constitutive transport element (CTE) to enhance translation from unspliced RNA with a retained intron, demonstrating a specific post-transcriptional regulatory function distinct from the transcriptional roles of the -KTS isoform. The identification of specific mRNA targets including IGF2 mRNA suggests that WT1 may coordinate transcriptional and post-transcriptional regulation of key developmental genes.

## 9. Open Questions

Despite decades of research, several fundamental questions about WT1 biology remain unresolved:

1. **Isoform-specific target genes**: While it is clear that +KTS and -KTS isoforms have distinct functions, a comprehensive genome-wide identification of isoform-specific target genes and RNAs is lacking. What is the full repertoire of genes regulated transcriptionally by -KTS versus post-transcriptionally by +KTS?

2. **Context-dependent activation vs. repression**: What determines whether WT1 activates or represses a given target gene in a specific cellular context? The role of BASP1 is established, but other factors likely contribute to this decision.

3. **SUMOylation function**: The functional consequences of WT1 SUMOylation remain unclear. Does this modification affect DNA binding, protein interactions, or subcellular localization?

4. **RNA targets and mechanisms**: While WT1 RNA binding has been demonstrated, the identity and functional consequences of most RNA targets remain unknown. How does WT1 coordinate transcriptional and post-transcriptional regulation?

5. **Adult tissue functions**: WT1 expression persists in adult podocytes, Sertoli cells, and granulosa cells. What are its functions in tissue homeostasis beyond development, and how does its dysregulation contribute to adult-onset diseases?

6. **Oncogenic mechanisms**: How does WT1 switch from tumor suppressor to oncogene in different cancers? What target genes mediate its oncogenic effects?

7. **Therapeutic targeting**: Can WT1 be effectively targeted for cancer therapy? WT1 peptide vaccines and T cell therapies are in clinical trials, but optimal approaches remain to be defined.

## References

- [caricasole-1996-rna-binding-abstract]: Caricasole A, et al. RNA binding by the Wilms tumor suppressor zinc finger proteins. PNAS. 1996;93(15):7562-6. PMID: 8755511

- [maheswaran-1993-p53-interaction-abstract]: Maheswaran S, et al. Physical and functional interaction between WT1 and p53 proteins. PNAS. 1993;90(11):5100-4. PMID: 8389468. DOI: 10.1073/pnas.90.11.5100

- [davies-1998-u2af65-abstract]: Davies RC, et al. WT1 interacts with the splicing factor U2AF65 in an isoform-dependent manner and can be incorporated into spliceosomes. Genes & Development. 1998;12(20):3217-25. PMID: 9784496. DOI: 10.1101/gad.12.20.3217

- [hamilton-1998-dna-binding-abstract]: Hamilton TB, et al. Comparison of the DNA binding characteristics of the related zinc finger proteins WT1 and EGR1. Biochemistry. 1998;37(7):2051-8. PMID: 9485332. DOI: 10.1021/bi9717993

- [hossain-2001-sry-abstract]: Hossain A, Saunders GF. The human sex-determining gene SRY is a direct target of WT1. J Biol Chem. 2001;276(20):16817-23. PMID: 11278460. DOI: 10.1074/jbc.M009056200

- [laity-2000-kts-splicing-abstract]: Laity JH, et al. Molecular basis for modulation of biological function by alternate splicing of the Wilms' tumor suppressor protein. PNAS. 2000;97(22):11932-5. PMID: 11050227. DOI: 10.1073/pnas.97.22.11932

- [larsson-1995-localization-abstract]: Larsson SH, et al. Subnuclear localization of WT1 in splicing or transcription factor domains is regulated by alternative splicing. Cell. 1995;81(3):391-401. PMID: 7736591. DOI: 10.1016/0092-8674(95)90392-5

- [rauscher-1993-wt1-tumor-suppressor-abstract]: Rauscher FJ 3rd. The WT1 Wilms tumor gene product: a developmentally regulated transcription factor in the kidney that functions as a tumor suppressor. FASEB J. 1993;7(10):896-903. PMID: 8393820

- [stoll-2007-wt1-structure-abstract]: Stoll R, et al. Structure of the Wilms tumor suppressor protein zinc finger domain bound to DNA. J Mol Biol. 2007;372(5):1227-45. PMID: 17716689. DOI: 10.1016/j.jmb.2007.07.017

- [toska-2012-basp1-hdac-abstract]: Toska E, et al. Repression of transcription by WT1-BASP1 requires the myristoylation of BASP1 and the PIP2-dependent recruitment of histone deacetylase. Cell Reports. 2012;2(3):462-9. PMID: 22939983. DOI: 10.1016/j.celrep.2012.08.005

- [toska-2014-prohibitin-abstract]: Toska E, et al. Prohibitin is required for transcriptional repression by the WT1-BASP1 complex. Oncogene. 2014;33(43):5100-8. PMID: 24166496. DOI: 10.1038/onc.2013.447

- [toska-2014-wt1-review-abstract]: Toska E, Roberts SGE. Mechanisms of transcriptional regulation by WT1 (Wilms' tumour 1). Biochem J. 2014;461(1):15-32. PMID: 24927120. DOI: 10.1042/BJ20131587

- [vongise-2011-epicardial-emt-abstract]: von Gise A, et al. WT1 regulates epicardial epithelial to mesenchymal transition through β-catenin and retinoic acid signaling pathways. Dev Biol. 2011;356(2):421-31. PMID: 21663736. DOI: 10.1016/j.ydbio.2011.05.668

- [wagner-2004-nephrin-abstract]: Wagner N, et al. The major podocyte protein nephrin is transcriptionally activated by the Wilms' tumor suppressor WT1. J Am Soc Nephrol. 2004;15(12):3044-51. PMID: 15579507. DOI: 10.1097/01.ASN.0000146687.99058.25

- [wilhelm-2002-gonad-sf1-abstract]: Wilhelm D, Englert C. The Wilms tumor suppressor WT1 regulates early gonad development by activation of Sf1. Genes & Development. 2002;16(14):1839-51. DOI: 10.1101/gad.220102


## Citations

1. caricasole-1996-rna-binding-abstract.md
2. davies-1998-u2af65-abstract.md
3. hamilton-1998-dna-binding-abstract.md
4. hossain-2001-sry-abstract.md
5. laity-2000-kts-splicing-abstract.md
6. larsson-1995-localization-abstract.md
7. maheswaran-1993-p53-interaction-abstract.md
8. rauscher-1993-wt1-tumor-suppressor-abstract.md
9. stoll-2007-wt1-structure-abstract.md
10. toska-2012-basp1-hdac-abstract.md
11. toska-2014-prohibitin-abstract.md
12. toska-2014-wt1-review-abstract.md
13. vongise-2011-epicardial-emt-abstract.md
14. wagner-2004-nephrin-abstract.md
15. wilhelm-2002-gonad-sf1-abstract.md