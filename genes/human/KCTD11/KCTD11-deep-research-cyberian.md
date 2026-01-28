---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-22T19:01:59.010350'
end_time: '2026-01-22T19:23:26.483717'
duration_seconds: 1287.47
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: KCTD11
  gene_symbol: KCTD11
  uniprot_accession: Q693B1
  protein_description: 'RecName: Full=BTB/POZ domain-containing protein KCTD11; AltName:
    Full=KCASH1 protein {ECO:0000303|PubMed:21472142}; AltName: Full=Potassium channel
    tetramerization domain-containing protein 11; AltName: Full=RING-type E3 ubiquitin
    transferase subunit KCTD11 {ECO:0000303|PubMed:20081843};'
  gene_info: Name=KCTD11; Synonyms=C17orf36, REN;
  organism_full: Homo sapiens (Human).
  protein_family: Not specified in UniProt
  protein_domains: KCTD11/21_C. (IPR045763); SKP1/BTB/POZ_sf. (IPR011333); T1-type_BTB.
    (IPR003131); BTB_2 (PF02214); KCTD11_21_C (PF19329)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 14
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q693B1
- **Protein Description:** RecName: Full=BTB/POZ domain-containing protein KCTD11; AltName: Full=KCASH1 protein {ECO:0000303|PubMed:21472142}; AltName: Full=Potassium channel tetramerization domain-containing protein 11; AltName: Full=RING-type E3 ubiquitin transferase subunit KCTD11 {ECO:0000303|PubMed:20081843};
- **Gene Information:** Name=KCTD11; Synonyms=C17orf36, REN;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** KCTD11/21_C. (IPR045763); SKP1/BTB/POZ_sf. (IPR011333); T1-type_BTB. (IPR003131); BTB_2 (PF02214); KCTD11_21_C (PF19329)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "KCTD11" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'KCTD11' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **KCTD11** (gene ID: KCTD11, UniProt: Q693B1) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# KCTD11 (KCASH1): A Comprehensive Review of Structure, Function, and Role in Disease

## Introduction and Summary

KCTD11, also known as REN (retinoic acid-, EGF-, and NGF-induced gene) or KCASH1 (KCTD Containing-Cullin3 Adaptor, Suppressor of Hedgehog), is a BTB/POZ domain-containing protein that functions as a substrate-specific adapter for the Cullin3-RING E3 ubiquitin ligase complex (CRL3). The gene maps to human chromosome 17p13.2 and encodes a protein of approximately 232 amino acids (26 kDa) that plays critical roles in neural development, cell cycle regulation, and tumor suppression [dimarcotullio-2004-hedgehog-suppressor-abstract].

The primary molecular function of KCTD11 is to serve as a substrate receptor that recruits specific proteins for ubiquitination and subsequent proteasomal degradation. Its best-characterized substrate is histone deacetylase 1 (HDAC1), whose degradation by CRL3-KCTD11 leads to hyperacetylation and inactivation of the Gli transcription factors, thereby suppressing Hedgehog signaling [canettieri-2010-gli-acetylation-abstract]. More recently, SALL4, a stemness regulator, has been identified as another CRL3-KCTD11 substrate [severini-2023-sall4-substrate-abstract]. Through these mechanisms, KCTD11 acts as a potent tumor suppressor whose expression is frequently reduced or lost in multiple cancer types, most notably medulloblastoma, prostate adenocarcinoma, hepatocellular carcinoma, and lung cancer.

## Discovery and Evolutionary Context

The gene encoding KCTD11 was originally identified in mouse as "REN," a developmentally regulated gene that promotes neural cell differentiation. Gallo and colleagues (2002) discovered that mouse Ren expression was upregulated by neurogenic signals including retinoic acid, epidermal growth factor (EGF), and nerve growth factor (NGF) in pluripotent embryonic stem cells and neural progenitor cell lines [gallo-2002-neural-differentiation-abstract]. The mouse protein consists of 232 amino acids with an N-terminal BTB/POZ domain and multiple predicted sites for post-translational modifications including myristoylation and phosphorylation. Northern blot analysis demonstrated peak expression at embryonic day 8.5, with localization in neural tissues including the neural tube and dorsal root ganglia [gallo-2002-neural-differentiation-abstract].

The human ortholog was subsequently cloned and characterized by Di Marcotullio and colleagues (2004), who demonstrated 91% amino acid identity with the mouse protein [dimarcotullio-2004-hedgehog-suppressor-abstract]. The human gene is intronless and maps to chromosome 17p13.2, a region frequently subject to loss of heterozygosity (LOH) in various cancers. The gene was named KCTD11 based on sequence similarity to the tetramerization domain of voltage-gated potassium channels, though KCTD11 does not function as a potassium channel. The KCASH1 designation was later adopted to reflect its function as a Cullin3 adaptor and suppressor of Hedgehog signaling [desmaele-2011-kcash-family-abstract].

KCTD11 belongs to a larger family of 26 KCTD proteins in humans. Phylogenetic analysis groups KCTD11 in the E-group along with KCTD21 (KCASH2) and KCTD6 (KCASH3), which share functional similarity as Hedgehog pathway suppressors [liu-2013-kctd-family-review-abstract]. These three proteins comprise the KCASH family, capable of forming homo- and hetero-oligomeric complexes that function coordinately to regulate HDAC1 degradation and Hedgehog signaling [desmaele-2011-kcash-family-abstract].

## Protein Structure and Molecular Organization

KCTD11 contains a conserved N-terminal BTB/POZ (Bric-a-brac, Tramtrack, Broad-complex/Poxvirus and Zinc finger) domain spanning approximately 95 amino acids. The core BTB fold comprises five alpha-helices organized into two sets of hairpins, capped at one end by three beta-strands [pinkas-2017-kctd-structural-abstract]. This domain mediates protein oligomerization and interaction with Cullin3. The C-terminal region of KCTD11 contains the KCTD11/21_C domain (Pfam: PF19329), which is involved in substrate recognition.

Two protein isoforms exist: a shorter form (sKCTD11, 232 amino acids) and a longer variant (lKCTD11) with an extended N-terminus of approximately 39 additional residues [liu-2013-kctd-family-review-abstract]. Only the lKCTD11 form has a complete BTB domain, yet remarkably, even the shorter variant retains Cullin3-binding activity [liu-2013-kctd-family-review-abstract].

The oligomeric state of KCTD11 has been the subject of investigation. Initial biophysical characterization using gel filtration and light scattering suggested that KCTD11 forms stable tetramers, in contrast to the pentameric assemblies observed for the related protein KCTD5 [correale-2011-kctd11-organization-abstract]. Homology-based modeling suggested a 4:4 stoichiometry for the KCTD11-Cullin3 complex [correale-2011-kctd11-organization-abstract]. However, subsequent electron microscopy studies revealed that the BTB domain can also adopt pentameric states, suggesting structural flexibility [angrisani-2021-kctd-cancer-review-abstract]. The binding interface with Cullin3 involves aromatic residues, particularly Phe102 and Tyr103, in the POZ/BTB domain [correale-2011-kctd11-organization-abstract].

Despite differences in oligomeric state, tetrameric KCTD11 and pentameric KCTD5 share a similar cavity at the subunit-subunit interface for Cullin3 binding [correale-2011-kctd11-organization-abstract]. This structural conservation enables both proteins to function as Cullin3 adaptors, though they recognize different substrates.

More recently, AlphaFold v2.0 has been used to predict the full-length pentameric structure of KCTD11 [esposito-2022-alphafold-kctd-abstract]. These predictions classify KCTD11 within Cluster 2, sub-Cluster 2B alongside KCTD21 based on structural similarities. The predicted pentamer forms a propeller-like assembly with a central cavity delimited by beta-strands. Molecular dynamics simulations spanning 200 nanoseconds validated the overall integrity of the pentameric BTB and CTD domains [esposito-2022-alphafold-kctd-abstract]. Structural comparison between AlphaFold-predicted KCTD11 and KCTD21 yielded an RMSD of 2.36 Angstroms with 579 Calpha atoms aligned, demonstrating substantial structural conservation despite sequence divergence (31.6% identity in CTD domains) [esposito-2022-alphafold-kctd-abstract].

## Primary Molecular Function: E3 Ubiquitin Ligase Adaptor Activity

The principal molecular function of KCTD11 is to act as a substrate-specific adapter for the BCR (BTB-CUL3-RBX1) E3 ubiquitin-protein ligase complex. In this capacity, KCTD11 bridges the Cullin3 scaffold protein to specific substrates, targeting them for polyubiquitination and subsequent proteasomal degradation [canettieri-2010-gli-acetylation-abstract].

### HDAC1 as a Substrate

The best-characterized substrate of CRL3-KCTD11 is histone deacetylase 1 (HDAC1). The landmark study by Canettieri and colleagues (2010) in Nature Cell Biology established that KCTD11, in complex with Cullin3, promotes the ubiquitination and degradation of HDAC1 [canettieri-2010-gli-acetylation-abstract]. This discovery was crucial for understanding how KCTD11 regulates Hedgehog signaling.

Both KCASH1 (KCTD11) and KCASH2 (KCTD21) can directly bind HDAC1, while KCASH3 (KCTD6) requires heterodimerization with KCASH1 to effectively target HDAC1 [desmaele-2011-kcash-family-abstract]. This hetero-oligomerization enables coordinate regulation of HDAC1 levels by the KCASH family.

### SALL4 as a Substrate

More recently, the stemness regulator SALL4 (Spalt-like transcriptional factor 4) was identified as another CRL3-KCTD11 substrate through proteomic analysis [severini-2023-sall4-substrate-abstract]. SALL4 interacts with KCTD11 through its zinc finger cluster 1 (ZFC1) domain. CRL3-KCTD11 induces polyubiquitylation and degradation of wild-type SALL4, but not a SALL4 mutant lacking the ZFC1 domain [severini-2023-sall4-substrate-abstract]. The identification of SALL4 as a substrate reveals additional mechanisms by which KCTD11 suppresses tumorigenesis.

### Protein Interaction Partners

According to the BioGRID database, KCTD11 has multiple confirmed interaction partners beyond its substrates. The key interactions include: (1) CUL3 (Cullin3), which forms the scaffold of the CRL3 complex via direct binding to the KCTD11 BTB domain; (2) KCTD6 (KCASH3) and KCTD21 (KCASH2), with which KCTD11 can form heteropentameric assemblies [desmaele-2011-kcash-family-abstract]; (3) CTNNB1 (beta-catenin), which binds directly to the BTB domain of KCTD11 [yang-2021-lung-cancer-wnt-hippo-abstract]; and (4) RBX1, the RING-box protein that completes the BCR E3 ligase complex. These interactions reflect the dual role of KCTD11 as both an E3 ligase adaptor and a direct regulator of signaling pathways.

## Signaling Pathway Regulation

### Hedgehog Pathway Suppression

The Hedgehog (Hh) signaling pathway is crucial for embryonic development and is frequently dysregulated in cancer, particularly medulloblastoma. The transcriptional output of Hedgehog signaling is mediated by the Gli family of transcription factors (Gli1, Gli2, Gli3). KCTD11 functions as a negative regulator of this pathway through multiple mechanisms.

The primary mechanism involves HDAC1 degradation and subsequent Gli acetylation. Gli1 and Gli2 are acetylated proteins, and their HDAC-mediated deacetylation promotes transcriptional activation [canettieri-2010-gli-acetylation-abstract]. Acetylation of Gli1 and Gli2, catalyzed by the histone acetyltransferase p300, inhibits their transcriptional activity by preventing recruitment to target promoters. HDAC1 and HDAC2 remove these acetyl groups, restoring Gli activity. Hedgehog signaling induces HDAC1 expression, creating a positive feedback loop that amplifies pathway activity [canettieri-2010-gli-acetylation-abstract].

CRL3-KCTD11 turns off this mechanism by degrading HDAC1, thereby preserving Gli acetylation and blocking transcriptional activity. Loss of KCTD11, as occurs in medulloblastoma, allows HDAC1 accumulation and consequent Gli1 deacetylation and activation [canettieri-2010-gli-acetylation-abstract].

Additionally, the original study by Di Marcotullio et al. (2004) demonstrated that KCTD11/REN retains Gli1 in the cytoplasm under conditions that would otherwise trigger its nuclear translocation [dimarcotullio-2004-hedgehog-suppressor-abstract]. This cytoplasmic retention prevents Gli1 from accessing nuclear target genes.

The SALL4 pathway adds another layer of Hedgehog regulation. SALL4, HDAC1, and GLI1 form a trimeric complex that promotes GLI1 deacetylation, enhancing pathway activation [severini-2023-sall4-substrate-abstract]. By degrading both HDAC1 and SALL4, CRL3-KCTD11 disrupts this oncogenic complex.

### Wnt/Beta-Catenin Pathway Regulation

Beyond Hedgehog signaling, KCTD11 has been shown to regulate the Wnt/beta-catenin pathway. In non-small cell lung cancer, Yang and colleagues (2021) demonstrated that KCTD11 binds to beta-catenin through its BTB domain [yang-2021-lung-cancer-wnt-hippo-abstract]. This interaction promotes beta-catenin phosphorylation and inhibits its nuclear translocation, thereby suppressing Wnt pathway transcriptional activity. Deletion of the BTB domain eliminated both beta-catenin binding and tumor-suppressive effects [yang-2021-lung-cancer-wnt-hippo-abstract].

### Hippo Pathway Activation

KCTD11 also regulates the Hippo signaling pathway, which controls organ size and has tumor-suppressive functions. Studies in hepatocellular carcinoma [tong-2017-hcc-hippo-abstract] and lung cancer [yang-2021-lung-cancer-wnt-hippo-abstract] demonstrated that KCTD11 promotes phosphorylation of YAP at Ser127, leading to YAP cytoplasmic retention and inactivation. This prevents YAP-driven transcription of proliferative and anti-apoptotic genes.

Interestingly, KCTD11 lost its stimulatory effect on the Hippo pathway upon beta-catenin knockdown, establishing beta-catenin as essential for Hippo pathway regulation by KCTD11 [yang-2021-lung-cancer-wnt-hippo-abstract]. This reveals crosstalk between the Wnt and Hippo pathways mediated by KCTD11.

The hepatocellular carcinoma study identified three distinct mechanisms by which KCTD11 activates p21, a key cell cycle inhibitor: (1) YAP inactivation, (2) p53 stabilization via LATS2, and (3) promotion of the MST1/GSK3beta/p21 signaling axis [tong-2017-hcc-hippo-abstract]. These mechanisms function independently of p53 status.

## Subcellular Localization and Tissue Expression

KCTD11 exhibits both cytoplasmic and nuclear localization, with the distribution varying between normal and tumor tissues. According to immunohistochemical studies, normal tissues show predominantly nuclear KCTD11 staining (40-78% positive), while matching tumor samples show dramatically reduced nuclear staining (0-18%) [mancarelli-2010-sp1-methylation-abstract]. This suggests that nuclear localization may be important for KCTD11's tumor-suppressive function.

Functionally, KCTD11 operates primarily in the cytoplasm where it can sequester Gli1 and prevent its nuclear translocation [dimarcotullio-2004-hedgehog-suppressor-abstract]. The protein also influences the nuclear-cytoplasmic shuttling of other signaling molecules, including beta-catenin and YAP [yang-2021-lung-cancer-wnt-hippo-abstract][tong-2017-hcc-hippo-abstract].

Regarding tissue distribution, KCTD11 is broadly expressed across human tissues according to the Human Protein Atlas, with particularly notable expression in the cerebellum and nervous system tissues. In adult cerebellum, KCTD11 shows higher expression compared to whole brain, while medulloblastoma samples show significantly reduced expression. Real-time PCR analysis demonstrated reduced KCTD11 expression relative to normal adult cerebellum in 70% (14 of 20) of medulloblastoma samples examined [dimarcotullio-2004-hedgehog-suppressor-abstract]. Interestingly, neural stem cells show even lower KCTD11 levels than medulloblastoma, consistent with the role of KCTD11 as a marker and regulator of neuronal differentiation [gallo-2002-neural-differentiation-abstract].

## Role in Development

KCTD11 plays important roles in neural development. The original discovery of the gene revealed its induction by neurogenic signals (retinoic acid, EGF, NGF) and its ability to promote neuronal differentiation while inducing growth arrest [gallo-2002-neural-differentiation-abstract]. Overexpression of REN/KCTD11 induced neuronal differentiation and p27(KIP1) expression in neural progenitor cell lines, while inhibition impaired the induction of proneural genes neurogenin-1 and NeuroD [gallo-2002-neural-differentiation-abstract].

In cerebellar development, KCTD11 is expressed in differentiating rather than proliferating granule cell progenitors (GCPs). The Hedgehog pathway normally drives GCP proliferation, and KCTD11 antagonizes this by suppressing Hedgehog signaling, thereby promoting the transition from proliferation to differentiation [dimarcotullio-2004-hedgehog-suppressor-abstract]. Loss of KCTD11 disrupts this developmental checkpoint, contributing to medulloblastoma formation.

## Role in Cancer and Tumor Suppression

KCTD11 functions as a tumor suppressor gene, and its expression is reduced or lost in multiple cancer types.

### Medulloblastoma

Medulloblastoma, the most common malignant childhood brain tumor, is the cancer type most strongly associated with KCTD11 loss. Approximately 30% of medulloblastomas belong to the Sonic Hedgehog (SHH) molecular subgroup, characterized by constitutive pathway activation. Loss of heterozygosity on chromosome 17p13 occurs in up to 50% of medulloblastomas, and KCTD11 at 17p13.2 is a key gene affected by this deletion [dimarcotullio-2004-hedgehog-suppressor-abstract].

Studies have shown that KCTD11 deletion occurs in approximately 35-39% of primary medulloblastoma samples, with hemizygous tumors displaying 5-fold lower mRNA levels compared to normal cerebellum [dimarcotullio-2004-hedgehog-suppressor-abstract]. All three KCASH family members show reduced expression in medulloblastoma compared to normal cerebellum [desmaele-2011-kcash-family-abstract].

### Prostate Cancer

KCTD11 loss of heterozygosity is a common genetic lesion in human prostate adenocarcinoma. Nuclear KCTD11 protein expression is strongly reduced in primary prostate cancer, correlating with overexpression of Hedgehog pathway proteins [angrisani-2021-kctd-cancer-review-abstract].

### Hepatocellular Carcinoma

KCTD11 is lower expressed in hepatocellular carcinoma tumor tissues than peritumoral tissues, and patients with low KCTD11 expression show shorter survival rates [tong-2017-hcc-hippo-abstract]. The protein suppresses HCC growth through Hippo pathway activation and inhibits metastasis through suppression of MMPs and EMT [tong-2017-hcc-hippo-abstract].

### Lung Cancer

KCTD11 is under-expressed in lung cancer tissues and negatively correlates with tumor differentiation, TNM stage, and lymph node metastasis [yang-2021-lung-cancer-wnt-hippo-abstract]. Kaplan-Meier analysis demonstrates that KCTD11-positive patients have significantly better survival outcomes.

### Other Cancers

Reduced KCTD11 expression has been documented in cancers of the larynx, esophagus, stomach, colon-rectum, urinary bladder, breast, gallbladder, endometrium, and ovary [angrisani-2021-kctd-cancer-review-abstract][mancarelli-2010-sp1-methylation-abstract].

## Role in Peripheral Neuropathy: Charcot-Marie-Tooth Disease

A recent breakthrough discovery (2025) has identified KCTD11 as a novel gene responsible for autosomal recessive intermediate Charcot-Marie-Tooth disease (RI-CMTE), expanding the disease associations of KCTD11 beyond cancer [gadacha-2025-cmt-neuropathy-abstract]. Genetic studies in ten patients from five unrelated families identified five distinct bi-allelic loss-of-function KCTD11 variants. The patients present with middle-to-late onset (typically ages 25-40) slowly progressive neuropathy characterized by distal motor weakness, foot deformities, hand weakness, and intermediate nerve conduction velocities (25-45 m/s at the median nerve) [gadacha-2025-cmt-neuropathy-abstract].

Mechanistic studies revealed that KCTD11 plays a critical role in peripheral nerve myelination and maintenance. In Kctd11-/- mice, progressive myelin abnormalities including abnormal myelin infoldings and increased g-ratio (indicating thinner myelin) develop with age, most pronounced in distal nerves [gadacha-2025-cmt-neuropathy-abstract]. In vitro studies using dorsal root ganglion neuron/Schwann cell co-cultures demonstrated that KCTD11 ablation impairs myelination. The pathogenic mechanism involves dysregulation of the same signaling pathways controlled by KCTD11 in cancer contexts: HDAC1, Wnt/beta-catenin (increased beta-catenin indicating pathway activation), Sonic Hedgehog (upregulation of Gli2), and Hippo/YAP (increased CTGF/CCN2 indicating pathway inhibition) [gadacha-2025-cmt-neuropathy-abstract]. These findings demonstrate that KCTD11 functions as a key regulator of peripheral nerve physiology, particularly in myelin maintenance through coordinated regulation of these signaling pathways in Schwann cells.

## Gene Regulation and Epigenetic Silencing

KCTD11 expression is regulated by both transcriptional and epigenetic mechanisms. The gene promoter contains a CpG island of 623 bp spanning 72 CpG dinucleotides, and six putative binding sites for the Sp1 transcription factor [mancarelli-2010-sp1-methylation-abstract].

Sp1 strongly activates the TATA-less KCTD11 promoter, particularly through binding sites (Sp1-E and Sp1-F) positioned near the transcription start site [mancarelli-2010-sp1-methylation-abstract]. Treatment with the demethylating agent 5'-aza-2'-deoxycytidine significantly increased KCTD11 mRNA levels in colon cancer cell lines, demonstrating that promoter hypermethylation contributes to gene silencing in cancer [mancarelli-2010-sp1-methylation-abstract].

The balance between DNA methylation and Sp1 binding may represent a mechanism regulating tissue-specific KCTD11 expression. In cancer, promoter hypermethylation shifts this balance toward gene silencing, contributing to tumor suppressor inactivation.

## Therapeutic Implications

The role of KCTD11 in suppressing Hedgehog signaling has therapeutic implications. KCASH proteins represent a potential class of endogenous agents through which Hedgehog pathway-addicted tumors might be targeted [desmaele-2011-kcash-family-abstract]. Strategies to reactivate or increase KCASH1/KCTD11 expression could suppress Hedgehog signaling in tumors.

The identification of SALL4 as a CRL3-KCTD11 substrate provides another therapeutic avenue. Inhibition of SALL4 suppresses SHH medulloblastoma growth in both murine and patient-derived xenograft models [severini-2023-sall4-substrate-abstract]. Thalidomide treatment, which redirects SALL4 to CRL4-CRBN-mediated degradation, impaired PDX cell proliferation [severini-2023-sall4-substrate-abstract].

Given the epigenetic silencing of KCTD11 in many cancers, demethylating agents represent another potential therapeutic approach to restore KCTD11 expression and tumor-suppressive function.

## Open Questions

Several important questions remain regarding KCTD11 biology:

1. **Complete substrate repertoire:** While HDAC1 and SALL4 are established substrates, the full range of proteins targeted by CRL3-KCTD11 for degradation remains unknown. Systematic proteomics approaches may identify additional substrates relevant to development and cancer.

2. **Tissue-specific functions:** KCTD11 is expressed in multiple tissues, but its functions outside the nervous system are less well characterized. Understanding tissue-specific roles could reveal new therapeutic opportunities.

3. **Oligomeric state regulation:** The apparent flexibility between tetrameric and pentameric states raises questions about whether oligomeric state is dynamically regulated and functionally significant.

4. **KCASH family coordination:** The three KCASH proteins can form hetero-oligomers, but the precise circumstances under which homo- versus hetero-oligomers form, and their differential substrate specificities, require further investigation.

5. **Post-translational modifications:** The KCTD11 protein contains predicted sites for myristoylation and phosphorylation, but the functional significance of these modifications is unexplored.

6. **Relationship to potassium channels:** Despite sequence similarity to potassium channel tetramerization domains, KCTD11 does not appear to function in potassium conductance. The evolutionary relationship and any functional connection to ion channels remains unclear.

7. **Therapeutic development:** Whether KCTD11 expression can be therapeutically restored in tumors with epigenetic silencing, or whether its downstream effects can be mimicked pharmacologically, remains to be determined.

8. **Structural details of substrate recognition:** High-resolution structures of KCTD11 in complex with its substrates (HDAC1, SALL4) would provide insights into the molecular basis of substrate recognition and potential strategies for therapeutic intervention.

9. **Peripheral nervous system function:** The recent discovery that KCTD11 mutations cause Charcot-Marie-Tooth disease reveals a previously unappreciated role in peripheral nerve myelination and Schwann cell function. The precise mechanisms by which KCTD11 regulates myelin maintenance, and whether this involves the same substrate repertoire as in the CNS and cancer contexts, require further investigation.

## References

1. **gallo-2002-neural-differentiation:** Gallo R, Zazzeroni F, Alesse E, et al. REN: a novel, developmentally regulated gene that promotes neural cell differentiation. *J Cell Biol.* 2002;158(4):731-740. PMID: 12186855. DOI: 10.1083/jcb.200206024

2. **dimarcotullio-2004-hedgehog-suppressor:** Di Marcotullio L, Ferretti E, De Smaele E, et al. REN(KCTD11) is a suppressor of Hedgehog signaling and is deleted in human medulloblastoma. *Proc Natl Acad Sci USA.* 2004;101(29):10833-10838. PMID: 15249678. DOI: 10.1073/pnas.0400690101. PMC: PMC490020. URL: https://www.pnas.org/doi/10.1073/pnas.0400690101

3. **canettieri-2010-gli-acetylation:** Canettieri G, Di Marcotullio L, Greco A, et al. Histone deacetylase and Cullin3-REN(KCTD11) ubiquitin ligase interplay regulates Hedgehog signalling through Gli acetylation. *Nat Cell Biol.* 2010;12(2):132-142. PMID: 20081843. DOI: 10.1038/ncb2013. URL: https://www.nature.com/articles/ncb2013

4. **mancarelli-2010-sp1-methylation:** Mancarelli MM, Zazzeroni F, Ciccocioppo L, et al. The tumor suppressor gene KCTD11 REN is regulated by Sp1 and methylation and its expression is reduced in tumors. *Mol Cancer.* 2010;9:172. PMID: 20591193. DOI: 10.1186/1476-4598-9-172. PMC: PMC2913982. URL: https://molecular-cancer.biomedcentral.com/articles/10.1186/1476-4598-9-172

5. **desmaele-2011-kcash-family:** De Smaele E, Di Marcotullio L, Moretti M, et al. Identification and Characterization of KCASH2 and KCASH3, 2 Novel Cullin3 Adaptors Suppressing Histone Deacetylase and Hedgehog Activity in Medulloblastoma. *Neoplasia.* 2011;13(4):374-385. PMID: 21472142. DOI: 10.1593/neo.101630. PMC: PMC3071086. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC3071086/

6. **correale-2011-kctd11-organization:** Correale S, Pirone L, Di Marcotullio L, et al. Molecular organization of the cullin E3 ligase adaptor KCTD11. *Biochimie.* 2011;93(4):715-724. PMID: 21237243. DOI: 10.1016/j.biochi.2010.12.014

7. **liu-2013-kctd-family-review:** Liu Z, Xiang Y, Sun G. The KCTD family of proteins: structure, function, disease relevance. *Cell Biosci.* 2013;3(1):45. PMID: 24268103. DOI: 10.1186/2045-3701-3-45. PMC: PMC3882106. URL: https://cellandbioscience.biomedcentral.com/articles/10.1186/2045-3701-3-45

8. **tong-2017-hcc-hippo:** Tong R, Yang B, Xiao H, et al. KCTD11 inhibits growth and metastasis of hepatocellular carcinoma through activating Hippo signaling. *Oncotarget.* 2017;8(23):37717-37729. DOI: 10.18632/oncotarget.17145. URL: https://www.oncotarget.com/article/17145/text/

9. **pinkas-2017-kctd-structural:** Pinkas DM, Sanvitale CE, Bufton JC, et al. Structural complexity in the KCTD family of Cullin3-dependent E3 ubiquitin ligases. *Biochem J.* 2017;474(22):3747-3761. PMID: 28963344. DOI: 10.1042/BCJ20170527. PMC: PMC5664961. URL: https://portlandpress.com/biochemj/article/474/22/3747/49544/

10. **angrisani-2021-kctd-cancer-review:** Angrisani A, Di Fiore A, De Smaele E, Moretti M. The emerging role of the KCTD proteins in cancer. *Cell Commun Signal.* 2021;19:56. PMID: 34001146. DOI: 10.1186/s12964-021-00737-8. PMC: PMC8127222. URL: https://biosignaling.biomedcentral.com/articles/10.1186/s12964-021-00737-8

11. **yang-2021-lung-cancer-wnt-hippo:** Yang M, Han Y, Han Q, et al. KCTD11 inhibits progression of lung cancer by binding to beta-catenin to regulate the activity of the Wnt and Hippo pathways. *J Cell Mol Med.* 2021;25(19):9411-9426. PMID: 34453479. DOI: 10.1111/jcmm.16883. PMC: PMC8500973. URL: https://onlinelibrary.wiley.com/doi/10.1111/jcmm.16883

12. **severini-2023-sall4-substrate:** Lospinoso Severini L, Loricchio E, Navacci S, et al. SALL4 is a CRL3REN/KCTD11 substrate that drives Sonic Hedgehog-dependent medulloblastoma. *Cell Death Differ.* 2024;31(2):170-187. PMID: 38062245. DOI: 10.1038/s41418-023-01246-6. PMC: PMC10850099. URL: https://www.nature.com/articles/s41418-023-01246-6

13. **esposito-2022-alphafold-kctd:** Esposito L, Balasco N, Vitagliano L. AlphaFold Predictions Provide Insights into the Structural Features of the Functional Oligomers of All Members of the KCTD Family. *Int J Mol Sci.* 2022;23(21):13346. PMID: 36362127. DOI: 10.3390/ijms232113346. PMC: PMC9658877. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC9658877/

14. **gadacha-2025-cmt-neuropathy:** Gadacha W, et al. Bi-allelic mutations in KCTD11 cause a new form of autosomal recessive intermediate Charcot-Marie-Tooth disease. *bioRxiv* (preprint). 2025. DOI: 10.1101/2025.06.30.661538. URL: https://www.biorxiv.org/content/10.1101/2025.06.30.661538v1


## Citations

1. angrisani-2021-kctd-cancer-review-abstract.md
2. canettieri-2010-gli-acetylation-abstract.md
3. correale-2011-kctd11-organization-abstract.md
4. desmaele-2011-kcash-family-abstract.md
5. dimarcotullio-2004-hedgehog-suppressor-abstract.md
6. esposito-2022-alphafold-kctd-abstract.md
7. gadacha-2025-cmt-neuropathy-abstract.md
8. gallo-2002-neural-differentiation-abstract.md
9. liu-2013-kctd-family-review-abstract.md
10. mancarelli-2010-sp1-methylation-abstract.md
11. pinkas-2017-kctd-structural-abstract.md
12. severini-2023-sall4-substrate-abstract.md
13. tong-2017-hcc-hippo-abstract.md
14. yang-2021-lung-cancer-wnt-hippo-abstract.md