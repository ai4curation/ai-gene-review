---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-23T19:01:06.489725'
end_time: '2026-01-23T19:18:02.514656'
duration_seconds: 1016.03
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: RASA2
  gene_symbol: RASA2
  uniprot_accession: Q15283
  protein_description: 'RecName: Full=Ras GTPase-activating protein 2; AltName: Full=GTPase-activating
    protein 1m; Short=GAP1m;'
  gene_info: Name=RASA2; Synonyms=GAP1M, RASGAP;
  organism_full: Homo sapiens (Human).
  protein_family: Not specified in UniProt
  protein_domains: C2_dom. (IPR000008); C2_domain_sf. (IPR035892); PH-like_dom_sf.
    (IPR011993); PH_domain. (IPR001849); Ras_GTPase. (IPR039360)
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
- **UniProt Accession:** Q15283
- **Protein Description:** RecName: Full=Ras GTPase-activating protein 2; AltName: Full=GTPase-activating protein 1m; Short=GAP1m;
- **Gene Information:** Name=RASA2; Synonyms=GAP1M, RASGAP;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** C2_dom. (IPR000008); C2_domain_sf. (IPR035892); PH-like_dom_sf. (IPR011993); PH_domain. (IPR001849); Ras_GTPase. (IPR039360)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "RASA2" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'RASA2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **RASA2** (gene ID: RASA2, UniProt: Q15283) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# RASA2 (Ras GTPase-Activating Protein 2): A Comprehensive Review

## Introduction

RASA2 (RAS p21 protein activator 2), also known as GAP1m (GTPase-activating protein 1m), is a member of the GAP1 family of RasGAPs that functions as a negative regulator of RAS signaling. The protein stimulates the intrinsic GTPase activity of RAS proteins, converting them from the active GTP-bound state to the inactive GDP-bound form, thereby serving as a critical brake on RAS-mediated mitogenic signaling [maekawa-1994-gap1m-abstract]. Located on human chromosome 3q23, RASA2 encodes an 853-amino acid protein with a characteristic modular architecture comprising two N-terminal C2 domains, a central RasGAP catalytic domain, and a C-terminal pleckstrin homology (PH) domain with a Bruton's tyrosine kinase (BTK) motif [li-1996-human-gap1m-abstract]. RASA2 was identified based on its strong sequence similarity to Drosophila Gap1, a known suppressor of RAS function in fruit flies, establishing it as the mammalian counterpart of this evolutionarily conserved signaling regulator [maekawa-1994-gap1m-abstract].

Recent research has revealed RASA2 as a critical signaling checkpoint in T cell biology and a tumor suppressor in melanoma, highlighting its importance in both normal immune function and cancer development [carnevale-2022-tcells-abstract][arafeh-2015-melanoma-abstract]. Loss-of-function mutations in RASA2 have been associated with developmental syndromes including Noonan syndrome, underscoring the protein's essential role in proper RAS pathway regulation during development [chen-2014-noonan-abstract].

## Molecular Function and Catalytic Mechanism

RASA2 functions as a GTPase-activating protein that accelerates the hydrolysis of GTP bound to RAS proteins. RAS proteins possess weak intrinsic GTPase activity (approximately 4.7 × 10⁻⁴ s⁻¹ at 37°C), but RasGAPs like RASA2 can enhance this rate approximately 100,000-fold [sondermann-2019-rasgap-review-abstract]. This dramatic acceleration is achieved through a transition state stabilization mechanism that depends on the conserved "arginine finger" motif present in the GAP catalytic domain.

The catalytic mechanism involves the insertion of a critical arginine residue into the nucleotide-binding pocket of RAS. This arginine finger (corresponding to Arg789 in p120GAP/RASA1) performs dual functions: it stabilizes the position of the catalytic glutamine residue (Gln61) of RAS and neutralizes developing negative charges on the phosphate groups during the hydrolysis reaction [sondermann-2019-rasgap-review-abstract]. The carbonyl oxygen on the arginine finger backbone interacts with a water molecule that forms a bridge between the NH₂ group of Gln61 and the γ-phosphate of GTP, helping to generate and position the nucleophilic water molecule for attack on the phosphate bond. Importantly, RASA2 stimulates the GTPase activity of wild-type RAS but not oncogenic RAS variants harboring mutations at key catalytic residues such as valine substitution at position 12 [maekawa-1994-gap1m-abstract].

Recombinant protein studies have confirmed that the isolated GAP-related domain of RASA2 is sufficient for catalytic activity. Expression of this domain in Saccharomyces cerevisiae suppressed the ira2⁻ phenotype, providing functional evidence that RASA2 acts as a bona fide RAS-specific GAP [maekawa-1994-gap1m-abstract]. However, surrounding domains, particularly the C2 domains, appear to augment full catalytic activity, consistent with findings from related dual-specificity GAPs [sondermann-2019-rasgap-review-abstract].

## Substrate Specificity

Among the GAP1 family members, RASA2 shows preferential activity toward RAS over RAP1, distinguishing it from closely related family members such as RASA3 (GAP1IP4BP), RASA4 (CAPRI), and RASAL1, which demonstrate dual RAS/RAP1 specificity [johansen-2023-mindthegap-abstract]. Studies in T cells have shown that CRISPR-Cas9-mediated targeting of RASA2 leads to increased GTP-bound RAS levels and enhanced phosphorylation of downstream effectors ERK and S6, confirming its role as a RAS-specific GAP in physiological contexts [johansen-2023-mindthegap-abstract].

Particularly noteworthy is the apparent isoform selectivity of RASA2 for NRAS over other RAS family members. Work by Arafeh and colleagues demonstrated that RNAi-mediated suppression of RASA2 in melanoma cells led to activation of NRAS-GTP, but not HRAS or KRAS [arafeh-2019-nf1-rasa2-abstract]. Conversely, overexpression of wild-type RASA2 substantially suppressed NRAS-GTP levels. This finding has significant implications for understanding melanoma biology, where NRAS is frequently mutated, and suggests that RASA2 and NF1 (which preferentially targets KRAS and HRAS) may have complementary functions in regulating different RAS isoforms [arafeh-2019-nf1-rasa2-abstract].

## Domain Architecture and Regulatory Features

### C2 Domains

RASA2 contains two tandem C2 domains (C2A and C2B) at its N-terminus. C2 domains are approximately 130-residue modules arranged as eight β antiparallel strands forming a β sandwich structure. While C2 domains are classically associated with calcium-dependent phospholipid binding, not all C2 domains exhibit these properties. The C2 domains of RasGAPs, including RASA2, are positioned immediately N-terminal to the GAP domain—a configuration conserved in nine of ten RAS-specific GAPs (with neurofibromin being the exception) [sondermann-2019-rasgap-review-abstract].

The C2 domains appear to contribute to full catalytic activity. Studies on related GAPs such as SynGAP have shown that the presence of the C2 domain augments catalytic activity against both RAS and the related GTPase RAP. Similarly, in dual-specificity RasGAPs including RASA2, RASA3, and RASAL1, the C2 domain confers a catalytic advantage compared to the GAP domain alone [sondermann-2019-rasgap-review-abstract]. The precise mechanism of this enhancement remains under investigation, but may involve intramolecular interactions that optimize GAP domain positioning or interactions with partner proteins.

### Pleckstrin Homology Domain and BTK Motif

The C-terminal region of RASA2 contains a pleckstrin homology (PH) domain connected to a Bruton's tyrosine kinase (BTK) motif. The PH domain of RASA2 binds phosphatidylinositol (3,4,5)-trisphosphate (PIP3), enabling membrane recruitment in response to PI3K activation [johansen-2023-mindthegap-abstract][shen-2017-nonredundant-rasgaps-abstract]. This PIP3-dependent recruitment creates a negative feedback loop: activation of PI3K (which can be promoted by RAS) generates PIP3, which recruits RASA2 to the membrane where it can inactivate RAS.

Importantly, the PH domain of RASA2 also binds inositol 1,3,4,5-tetrakisphosphate (IP4) with high affinity and specificity [fukuda-1996-ip4-binding-abstract]. Structure-function studies have demonstrated that while the PH domain is the central IP4-binding domain, optimal binding requires an adjacent GAP-related domain and carboxyl terminus. A mutation replacing arginine with cysteine at position 628 in the PH domain (corresponding to the mutation in Bruton's tyrosine kinase observed in X-linked immunodeficiency mice) dramatically reduces both IP4 and phospholipid binding capacity [fukuda-1996-ip4-binding-abstract]. These findings indicate that the PH domain functions as a modulatory domain of GAP activity through its ability to bind both IP4 and phospholipids.

This regulatory mechanism distinguishes RASA2 from RASA3, whose PH domain additionally recognizes phosphatidylinositol (4,5)-bisphosphate (PIP2), allowing for constitutive membrane association. The consequence is that RASA2 is recruited to membranes upon PI3K activation, while RASA3 is found constitutively at membranes [johansen-2023-mindthegap-abstract]. The BTK motif, related to sequences found in Bruton's tyrosine kinase, participates in additional regulatory interactions including IP4 binding.

## Subcellular Localization

RASA2 is primarily localized to the cytoplasm and cytosol, with characteristic enrichment in the perinuclear region [shen-2017-nonredundant-rasgaps-abstract][lockyer-1997-localization-abstract]. This perinuclear localization distinguishes RASA2 from its close relative RASA3 (GAP1IP4BP), which localizes constitutively to the plasma membrane. Expression studies in COS-7 and HeLa cells demonstrated that while RASA3 is located solely at the plasma membrane, RASA2 maintains a distinct perinuclear distribution [lockyer-1997-localization-abstract]. Mutational analysis has established that this difference in subcellular distribution is determined by the respective PH domains of these proteins, highlighting the functional specialization within the GAP1 family.

Upon PI3K activation and PIP3 generation at the plasma membrane, RASA2 can translocate to the membrane where it encounters its RAS substrates. This dynamic localization allows RASA2 to function as a signal-responsive brake on RAS activity, being recruited specifically when and where PI3K signaling is active. The membrane targeting capacity of RASA2 is critical for its biological function, bringing it into proximity with membrane-associated RAS proteins that cycle between the plasma membrane and endomembranes. The requirement for PI3K-dependent membrane recruitment suggests that RASA2 primarily functions during active signaling states rather than providing constitutive suppression of RAS activity, in contrast to the constitutively membrane-localized RASA3.

## Role in RAS-MAPK Signaling Pathway

RASA2 functions as a negative regulator within the RAS-RAF-MEK-ERK (MAPK) signaling cascade, one of the most fundamental pathways controlling cell proliferation, differentiation, and survival. In this pathway, growth factors binding to receptor tyrosine kinases (RTKs) such as EGFR or PDGFR trigger receptor autophosphorylation and recruitment of adaptor proteins including GRB2. GRB2 in turn recruits guanine nucleotide exchange factors (GEFs) such as SOS1/2 and RASGRP1 that activate RAS by promoting GDP-to-GTP exchange. Active GTP-bound RAS then initiates the RAF-MEK-ERK kinase cascade, ultimately leading to activation of transcription factors and changes in gene expression [johansen-2023-mindthegap-abstract].

RASA2 counteracts this activation by accelerating GTP hydrolysis on RAS, returning it to the inactive GDP-bound state. Studies in T cells have demonstrated that RASA2 ablation enhances MAPK signaling, as evidenced by increased phosphorylation of ERK and downstream targets like S6 [carnevale-2022-tcells-abstract]. RASA2-deficient T cells show increased activation, cytokine production, and metabolic activity compared to control cells, reflecting the enhanced RAS-MAPK signaling in these cells [carnevale-2022-tcells-abstract].

An important aspect of RASA2 regulation is its expression-level control during signaling. Both RASA2 and RASA3 are markedly repressed upon T cell receptor (TCR) stimulation in both mouse and human T cells [johansen-2023-mindthegap-abstract]. This downregulation releases the brake on RAS (and RAP1) signaling, allowing full T cell activation. In contrast, RASA2 levels increase gradually with chronic antigen exposure, potentially contributing to T cell exhaustion in contexts of persistent stimulation [carnevale-2022-tcells-abstract].

## Role in T Cell Biology

Recent genome-wide CRISPR knockout screens have identified RASA2 as a critical signaling checkpoint in human T cells [carnevale-2022-tcells-abstract]. These screens, performed under immunosuppressive conditions designed to identify genes whose loss prevents T cell dysfunction, converged on RASA2 as a key regulatory target. The findings have significant implications for cancer immunotherapy, as RASA2 ablation can enhance both the sensitivity and persistence of anti-tumor T cell responses.

RASA2 ablation in T cells results in enhanced MAPK signaling and increased cytolytic activity in response to target antigens. Repeated tumor antigen stimulations in vitro revealed that RASA2-deficient T cells maintain increased activation, cytokine production, and metabolic activity compared with control cells [carnevale-2022-tcells-abstract]. Importantly, RASA2-deficient T cells show a marked advantage in persistent cancer cell killing, suggesting that RASA2 normally limits the long-term anti-tumor efficacy of T cells.

In preclinical models, RASA2-knockout chimeric antigen receptor (CAR) T cells demonstrated a competitive fitness advantage over control cells in the bone marrow in mouse models of leukemia. Ablation of RASA2 in multiple preclinical models of both T cell receptor (TCR) and CAR T cell therapies prolonged survival in mice bearing liquid or solid tumors [carnevale-2022-tcells-abstract]. These findings highlight RASA2 as a promising genetic target for enhancing both persistence and effector function in T cell therapies for cancer treatment.

The mechanism by which RASA2 limits T cell function appears to be activation-dependent. In the absence of TCR stimulation, RASA2 ablation does not result in unregulated MAPK signaling or altered T cell activation, proliferation, or viability [johansen-2023-mindthegap-abstract]. This suggests that RASA2 functions as a context-specific brake that engages primarily during active signaling states, consistent with its PI3K-dependent membrane recruitment.

## Role as a Tumor Suppressor

Analysis of 501 melanoma exomes identified RASA2 as a tumor suppressor gene mutated in approximately 5% of melanomas [arafeh-2015-melanoma-abstract]. The mutations include both nonsense mutations (such as p.Arg310*) and missense mutations affecting the RAS-GAP domain (such as p.Ser400Phe). Functional characterization demonstrated that these mutations represent loss-of-function alleles: while wild-type RASA2 substantially suppressed RAS-GTP levels in reconstitution experiments, mutant RASA2 proteins failed to suppress RAS-GTP [arafeh-2015-melanoma-abstract].

The biological consequences of RASA2 loss are consistent with its tumor suppressor function. RASA2 knockdown in NIH3T3 cells resulted in RAS activation leading to increased cell growth on plastic and in soft agar. Cells expressing mutant RASA2 showed significantly higher colony formation in soft agar compared to wild-type RASA2 and failed to suppress migration [arafeh-2015-melanoma-abstract].

Clinical analysis revealed that RASA2 expression was lost in at least 30% of human melanomas examined by immunohistochemistry. Loss of RASA2 expression was significantly associated with poorer patient survival (HR=0.42, log rank p=0.0043), underscoring its clinical relevance as a prognostic marker [arafeh-2015-melanoma-abstract].

The relationship between RASA2 and NF1 in melanoma is particularly informative. Both proteins function as RasGAPs, but they show distinct substrate preferences: RASA2 preferentially targets NRAS, while NF1 targets KRAS and HRAS [arafeh-2019-nf1-rasa2-abstract]. Mutations in RASA2 and NF1 co-occur significantly in melanoma (p=0.000011, Fisher's Exact Test), particularly in BRAF and NRAS wild-type tumors. Conversely, RASA2 and NRAS mutations are mutually exclusive, consistent with RASA2's role in suppressing NRAS activity. These observations suggest that combined loss of RASA2 and NF1 may be functionally equivalent to oncogenic RAS mutation, as it would result in constitutive activation of all RAS isoforms [arafeh-2019-nf1-rasa2-abstract].

## Disease Associations

### Noonan Syndrome

Loss-of-function mutations in RASA2 have been identified in patients with Noonan syndrome (NS), a developmental disorder characterized by distinctive facial features, short stature, congenital heart defects, and variable developmental delay [chen-2014-noonan-abstract]. Noonan syndrome and related disorders (collectively termed "RASopathies") are caused by germline mutations that increase RAS-MAPK pathway signaling.

Next-generation sequencing of 27 NS patients lacking mutations in previously known causative genes identified three patients with missense mutations in RASA2 affecting two residues: Y326C, Y326N (affecting the same codon), and R511C [chen-2014-noonan-abstract]. All mutations affect highly conserved amino acids within the GAP domain. Structural modeling based on the p120GAP structure predicts that R511 is a direct contact site for RAS, and MAPP analysis indicates that all three NS-associated mutations damage RASA2 function.

Expression of mutant RASA2 alleles in heterologous cells increased RAS-ERK pathway activation, supporting a causative role in NS pathogenesis [chen-2014-noonan-abstract]. All patients were heterozygous for their RASA2 allele, suggesting haploinsufficiency as the disease mechanism—a previously unreported mechanism of NS pathogenesis that is distinct from the gain-of-function mutations in RAS pathway components typically associated with RASopathies. However, the R511C variant appears to have dominant negative effects [chen-2014-noonan-abstract].

### Melanoma

As detailed above, RASA2 functions as a tumor suppressor in melanoma, with loss-of-function mutations or expression loss occurring in a substantial fraction of cases and correlating with worse patient outcomes [arafeh-2015-melanoma-abstract].

### Other Cancers

Examination of publicly available databases has revealed that RASA2 is mutated in several tumor types beyond melanoma. RASA2 loss-of-function mutations have been implicated in multiple myeloma, as well as cervical and head and neck cancers, where early-termination mutations similar to those found in melanoma have been identified [arafeh-2015-melanoma-abstract]. In relapsed refractory multiple myeloma (RRMM), RASA2 truncating mutations have been identified as part of the genetic alterations affecting the RAS/MAPK pathway, which is altered in 45-65% of these cases. However, RASA2 is typically co-mutated with other tumor suppressors such as NF1, suggesting reduced transformation potential as a single mutation and implying that RASA2 loss cooperates with other genetic hits to drive tumorigenesis.

## Tissue Expression and Distribution

RASA2 shows relatively broad tissue distribution, consistent with its classification among the ubiquitously distributed RasGAPs alongside RASA1, NF1, DAB2ip, and RASAL2 [shen-2017-nonredundant-rasgaps-abstract]. Original characterization of the rat homolog (Gap1m) revealed relatively high expression in brain, placenta, and kidney, with lower expression in other tissues [maekawa-1994-gap1m-abstract]. The human ortholog shows a similar pattern.

In the immune system, RASA2 is expressed in both CD4+ and CD8+ T cells [johansen-2023-mindthegap-abstract]. Expression is dynamically regulated: RASA2 is rapidly downregulated upon TCR stimulation but can increase gradually with chronic antigen exposure, as observed in exhausted T cells during chronic infection. Gene expression databases indicate highest RPKM values in lymph node and appendix, consistent with significant expression in lymphoid tissues.

## Evolutionary Conservation

RASA2 belongs to the GAP1 family of RasGAPs, which was identified based on homology to Drosophila Gap1. The amino acid sequence of RASA2 shows high similarity to the entire sequence of Drosophila Gap1, with the highest similarity observed in the catalytic domain when compared to Gap1, p120GAP, and neurofibromin [maekawa-1994-gap1m-abstract]. The human RASA2 protein (853 amino acids) is 89.4% identical to its rat ortholog, indicating strong conservation across mammals [li-1996-human-gap1m-abstract].

In Drosophila, Gap1 terminates RAS1 signaling downstream of receptor tyrosine kinases and the GEF Son-of-sevenless (Sos), playing critical roles in eye development and adult appendage patterning. Flies bearing mutations in both Gap1 and NF1 appear to be inviable, suggesting partial functional redundancy between these GAPs [shen-2017-nonredundant-rasgaps-abstract]. This evolutionary conservation underscores the fundamental importance of GAP1 family proteins in RAS pathway regulation.

## Open Questions

Despite significant advances in understanding RASA2 function, several important questions remain unresolved:

1. **Detailed biochemical characterization**: Comprehensive kinetic analysis of RASA2's catalytic activity toward different RAS isoforms and under varying conditions has not been reported. Understanding the quantitative parameters of RASA2 catalysis would help explain its apparent selectivity for NRAS.

2. **Structural basis of isoform selectivity**: The molecular basis for RASA2's preferential activity toward NRAS over HRAS and KRAS remains unclear. Crystal structures of RASA2 in complex with different RAS isoforms would be valuable.

3. **Regulation by post-translational modifications**: Whether RASA2 activity is regulated by phosphorylation or other post-translational modifications is not well characterized. Understanding such regulation could reveal additional layers of control.

4. **Functions beyond catalytic activity**: Whether RASA2 has scaffolding or other non-catalytic functions, as reported for some other RasGAPs, has not been explored in detail.

5. **Tissue-specific physiological roles**: Despite broad expression, the specific tissues and contexts where RASA2 is physiologically essential remain unclear. Conditional knockout studies would help address this question.

6. **Therapeutic targeting**: While RASA2 ablation enhances T cell anti-tumor activity, the potential consequences of systemic RASA2 inhibition (e.g., in non-immune cells) require careful consideration for therapeutic applications.

7. **Relationship with other RasGAPs**: How RASA2 cooperates or competes with other RasGAPs in physiological contexts is incompletely understood.

## References

- [maekawa-1994-gap1m-abstract]: Maekawa M, Li S, Iwamatsu A, Morishita T, Yokota K, Imai Y, Kohsaka S, Nakamura S, Hattori S. A novel mammalian Ras GTPase-activating protein which has phospholipid-binding and Btk homology regions. Mol Cell Biol. 1994 Oct;14(10):6879-85. PMID: 7935405. PMCID: PMC359218. DOI: 10.1128/mcb.14.10.6879-6885.1994. https://pubmed.ncbi.nlm.nih.gov/7935405/

- [li-1996-human-gap1m-abstract]: Li S, Satoh H, Watanabe T, Nakamura S, Hattori S. cDNA cloning and chromosomal mapping of a novel human GAP (GAP1M), a GTPase-activating protein of Ras. Genomics. 1996 Aug 1;35(3):625-7. PMID: 8812506. DOI: 10.1006/geno.1996.0412. https://pubmed.ncbi.nlm.nih.gov/8812506/

- [arafeh-2015-melanoma-abstract]: Arafeh R, Qutob N, Emmanuel R, Keren-Paz A, et al. Recurrent inactivating RASA2 mutations in melanoma. Nat Genet. 2015 Dec;47(12):1408-10. PMID: 26502337. PMCID: PMC4954601. DOI: 10.1038/ng.3427. https://pubmed.ncbi.nlm.nih.gov/26502337/

- [carnevale-2022-tcells-abstract]: Carnevale J, Shifrut E, et al. RASA2 ablation in T cells boosts antigen sensitivity and long-term function. Nature. 2022 Sep;609(7925):174-182. PMID: 36002574. PMCID: PMC9433322. DOI: 10.1038/s41586-022-05126-w. https://pubmed.ncbi.nlm.nih.gov/36002574/

- [johansen-2023-mindthegap-abstract]: Johansen KH, Golec DP, Okkenhaug K, Schwartzberg PL. Mind the GAP: RASA2 and RASA3 GTPase-activating proteins as gatekeepers of T cell activation and adhesion. Trends Immunol. 2023 Nov;44(11):917-931. PMID: 37858490. DOI: 10.1016/j.it.2023.09.002. https://pubmed.ncbi.nlm.nih.gov/37858490/

- [chen-2014-noonan-abstract]: Chen PC, Yin J, Yu HW, Yuan T, Fernandez M, et al. Next-generation sequencing identifies rare variants associated with Noonan syndrome. Proc Natl Acad Sci U S A. 2014 Aug 5;111(31):11473-8. PMID: 25049390. PMCID: PMC4128129. DOI: 10.1073/pnas.1324128111. https://pubmed.ncbi.nlm.nih.gov/25049390/

- [sondermann-2019-rasgap-review-abstract]: Sondermann H, Grundke C, Smerdon SJ. Ras-Specific GTPase-Activating Proteins—Structures, Mechanisms, and Interactions. Cold Spring Harb Perspect Med. 2019 Mar;9(3):a031500. PMCID: PMC6396337. DOI: 10.1101/cshperspect.a031500. https://pmc.ncbi.nlm.nih.gov/articles/PMC6396337/

- [arafeh-2019-nf1-rasa2-abstract]: Arafeh R, Di Pizio A, Elkahloun AG, Dym O, Niv MY, Samuels Y. RASA2 and NF1; two-negative regulators of Ras with complementary functions in melanoma. Oncogene. 2019 Mar;38(13):2432-2434. PMID: 30478445. DOI: 10.1038/s41388-018-0578-4. https://pubmed.ncbi.nlm.nih.gov/30478445/

- [shen-2017-nonredundant-rasgaps-abstract]: Shen MH, et al. Nonredundant Functions for Ras GTPase-Activating Proteins in Tissue Homeostasis. Sci Signal. 2017 Jun. PMCID: PMC5483993. https://pmc.ncbi.nlm.nih.gov/articles/PMC5483993/

- [fukuda-1996-ip4-binding-abstract]: Fukuda M, Mikoshiba K. Structure-function relationships of the mouse Gap1m. Determination of the inositol 1,3,4,5-tetrakisphosphate-binding domain. J Biol Chem. 1996 Aug 2;271(31):18838-42. PMID: 8702543. DOI: 10.1074/jbc.271.31.18838. https://pubmed.ncbi.nlm.nih.gov/8702543/

- [lockyer-1997-localization-abstract]: Lockyer PJ, Bottomley JR, Reynolds JS, McNulty TJ, Venkateswarlu K, Potter BV, Dempsey CE, Cullen PJ. Distinct subcellular localisations of the putative inositol 1,3,4,5-tetrakisphosphate receptors GAP1IP4BP and GAP1m result from the GAP1IP4BP PH domain directing plasma membrane targeting. Curr Biol. 1997 Dec 1;7(12):1007-10. PMID: 9382842. DOI: 10.1016/s0960-9822(06)00423-4. https://pubmed.ncbi.nlm.nih.gov/9382842/

- OMIM Entry 601589: RAS p21 PROTEIN ACTIVATOR 2; RASA2. https://omim.org/entry/601589

- NCBI Gene ID 5922: RASA2 RAS p21 protein activator 2 [Homo sapiens (human)]. https://www.ncbi.nlm.nih.gov/gene/5922


## Citations

1. arafeh-2015-melanoma-abstract.md
2. arafeh-2015-melanoma-summary.md
3. arafeh-2019-nf1-rasa2-abstract.md
4. carnevale-2022-tcells-abstract.md
5. carnevale-2022-tcells-summary.md
6. chen-2014-noonan-abstract.md
7. fukuda-1996-ip4-binding-abstract.md
8. johansen-2023-mindthegap-abstract.md
9. li-1996-human-gap1m-abstract.md
10. lockyer-1997-localization-abstract.md
11. maekawa-1994-gap1m-abstract.md
12. maekawa-1994-gap1m-summary.md
13. shen-2017-nonredundant-rasgaps-abstract.md
14. sondermann-2019-rasgap-review-abstract.md