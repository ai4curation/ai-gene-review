---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-23T20:43:22.109831'
end_time: '2026-01-23T21:00:49.310723'
duration_seconds: 1047.2
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: SOCS4
  gene_symbol: SOCS4
  uniprot_accession: Q8WXH5
  protein_description: 'RecName: Full=Suppressor of cytokine signaling 4; Short=SOCS-4;
    AltName: Full=Suppressor of cytokine signaling 7; Short=SOCS-7;'
  gene_info: Name=SOCS4; Synonyms=SOCS7;
  organism_full: Homo sapiens (Human).
  protein_family: Not specified in UniProt
  protein_domains: SH2. (IPR000980); SH2_dom_sf. (IPR036860); SOCS4/SOCS5_dom. (IPR022252);
    SOCS4_SH2. (IPR035864); SOCS4_SOCS. (IPR037342)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 16
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q8WXH5
- **Protein Description:** RecName: Full=Suppressor of cytokine signaling 4; Short=SOCS-4; AltName: Full=Suppressor of cytokine signaling 7; Short=SOCS-7;
- **Gene Information:** Name=SOCS4; Synonyms=SOCS7;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** SH2. (IPR000980); SH2_dom_sf. (IPR036860); SOCS4/SOCS5_dom. (IPR022252); SOCS4_SH2. (IPR035864); SOCS4_SOCS. (IPR037342)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "SOCS4" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'SOCS4' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **SOCS4** (gene ID: SOCS4, UniProt: Q8WXH5) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# SOCS4: Suppressor of Cytokine Signaling 4 - A Comprehensive Review

## Introduction

Suppressor of cytokine signaling 4 (SOCS4) is a member of the SOCS protein family, which comprises eight structurally related proteins (CIS/CISH, SOCS1-7) that function as negative regulators of signal transduction pathways [alexander-2002-socs-immune]. Among the SOCS family members, SOCS4 has historically been one of the least characterized, sometimes referred to as "the neglected SOCS" [trengove-2013-socs-development]. However, accumulating evidence over the past two decades has revealed that SOCS4 plays critical roles in regulating epidermal growth factor receptor (EGFR) signaling, modulating immune responses during viral infection, and functioning as a tumor suppressor in several malignancies.

The human SOCS4 gene is located on chromosome 14q22.3 (Gene ID: 122809) and encodes a 440 amino acid protein (UniProt: Q8WXH5). The protein contains the canonical SOCS architecture: a central SH2 (Src Homology 2) domain that mediates phosphotyrosine-dependent substrate recognition, and a C-terminal SOCS box that recruits E3 ubiquitin ligase machinery [croker-2008-socs-jak-stat]. SOCS4 is most closely related to SOCS5, with which it shares 92% amino acid identity within the SH2 domain, suggesting overlapping substrate specificity while maintaining distinct regulatory roles through their divergent N-terminal regions [bullock-2007-socs4-structure].

## Protein Structure and Domain Organization

The structural basis of SOCS4 function was elucidated through X-ray crystallography of the SOCS4-ElonginB/C complex at 2.5 Angstrom resolution [bullock-2007-socs4-structure]. This structural analysis revealed that SOCS4 represents a structurally distinct subfamily within the SOCS family. Unlike SOCS2, whose structure had been previously determined, SOCS4 exhibits an 80-degree rotation of the SH2 domain relative to the SOCS box interface. This distinct domain arrangement results from the SOCS4 Extended SH2 Subdomain (ESS) helix replacing the position occupied by the C-terminus in SOCS2, creating a fundamentally different architecture that can accommodate extended C-terminal regions.

The SH2 domain of SOCS4 is responsible for substrate recognition through binding to phosphorylated tyrosine residues on target proteins. Structural and biochemical analyses demonstrated that SOCS4 exhibits a strong preference for substrates with isoleucine, leucine, or valine at both the +1 and +3 positions relative to the phosphotyrosine [bullock-2007-socs4-structure]. This selectivity pattern underlies the specificity of SOCS4 for particular signaling molecules, most notably the EGFR at phosphotyrosine 1092 (pY1092).

The SOCS box domain consists of two functional subdomains: the BC box, which binds the Elongin B/C adaptor complex, and the Cullin box (Cul box), which recruits Cullin5 [babon-2009-socs-cullin5]. The assembled SOCS4-ElonginBC-Cullin5-Rbx2 complex functions as an E3 ubiquitin ligase that catalyzes polyubiquitination of substrates, targeting them for proteasomal degradation. Biochemical studies have demonstrated that SOCS4 binds Cullin5 with high affinity (dissociation constant approximately 10 nM), placing it in the same affinity class as SOCS2, SOCS5, SOCS6, SOCS7, and CIS [babon-2009-socs-cullin5]. This high-affinity binding suggests that SOCS4 functions primarily through the SOCS box-dependent degradation mechanism, in contrast to SOCS1 and SOCS3, which employ both SOCS box-dependent and kinase inhibitory region (KIR)-dependent mechanisms.

SOCS4 also possesses an extended N-terminal domain of approximately 270 amino acids, significantly longer than the N-terminal regions of SOCS1-3 [croker-2008-socs-jak-stat]. SOCS4 and SOCS5 share a distinctive N-terminal conserved region (NTCR) whose precise function remains to be fully elucidated. Recent evidence suggests this region may contain a JAK interaction region (JIR) analogous to that identified in SOCS5, potentially enabling direct regulation of JAK kinase activity [trengove-2013-socs-development].

## Molecular Function and Mechanism of Action

The primary molecular function of SOCS4 is to serve as a substrate-recognition component of a Cullin-RING E3 ubiquitin ligase (CRL) complex. Through its SH2 domain, SOCS4 recognizes and binds to phosphorylated tyrosine residues on target proteins, while the SOCS box recruits the Elongin B/C-Cullin5-Rbx2 ubiquitin ligase machinery to catalyze polyubiquitination and subsequent proteasomal degradation of the bound substrate [bullock-2007-socs4-structure].

The best-characterized substrate of SOCS4 is the epidermal growth factor receptor (EGFR). Isothermal titration calorimetry measurements revealed that SOCS4 binds to EGFR at phosphotyrosine 1092 with a dissociation constant of 0.5 micromolar [bullock-2007-socs4-structure]. This binding affinity is comparable to that of Grb2, a well-established physiological ligand of EGFR pY1092 (KD = 0.4-0.7 micromolar), indicating that SOCS4 can effectively compete with downstream signaling adaptors for receptor binding. Importantly, EGFR pY1092 is also a major docking site for STAT3, and SOCS4 binding at this position directly competes with STAT3 recruitment [bullock-2007-socs4-structure]. This competition underlies the observed reduction in STAT3 signaling following SOCS4 expression in cellular transfection studies.

The expression of SOCS4 is induced by EGF stimulation, consistent with its role as a negative feedback regulator of EGFR signaling [kario-2005-socs4-egfr]. Kinetic studies demonstrated that SOCS4 mRNA levels peak within 60 minutes of EGFR activation and subsequently decay, representing a typical inducible feedback inhibitor expression pattern. Upon induction, SOCS4 promotes EGFR degradation in a SOCS box-dependent manner. Critically, this degradation occurs independently of the canonical c-Cbl-mediated pathway that normally regulates EGFR turnover, representing an alternative mechanism for receptor downregulation [kario-2005-socs4-egfr].

Beyond EGFR, limited evidence suggests that SOCS4 may interact with other signaling molecules. Studies have reported low-affinity interactions between SOCS4 and JAK2, as well as c-KIT [trengove-2013-socs-development]. However, the physiological significance of these interactions remains to be established through additional experimental investigation.

## Subcellular Localization

Based on data from the Human Protein Atlas, SOCS4 localizes primarily to the nucleoplasm and cytosol [Human Protein Atlas, ENSG00000180008-SOCS4]. This dual localization pattern is consistent with the protein's function in regulating receptor signaling, which involves recognition of activated receptors at or near the plasma membrane followed by assembly of the ubiquitin ligase complex that can function in cytosolic compartments.

The subcellular distribution of SOCS4 likely reflects the dynamic nature of its function as a signal transduction regulator. Following EGF stimulation, SOCS4 would be expected to translocate to sites of activated EGFR to mediate receptor ubiquitination and degradation. The observed cytoplasmic and nuclear localization may also indicate roles beyond receptor degradation, potentially including regulation of transcription factors or other nuclear signaling components, although such functions remain to be experimentally validated for SOCS4.

## Role in EGFR Signaling Pathway

SOCS4 functions as a critical negative feedback regulator of the EGF receptor signaling pathway. The EGFR is a receptor tyrosine kinase that, upon ligand binding, undergoes autophosphorylation at multiple tyrosine residues, creating docking sites for downstream signaling molecules including Grb2, Shc, STAT3, and PLCgamma. Uncontrolled EGFR signaling contributes to the pathogenesis of numerous cancers, making its tight regulation essential for normal cellular homeostasis.

SOCS4 participates in EGFR regulation through a classic negative feedback loop. EGF stimulation activates EGFR, which triggers downstream signaling cascades and simultaneously induces SOCS4 expression [kario-2005-socs4-egfr]. Once expressed, SOCS4 binds to the phosphorylated EGFR, recruits the ubiquitin ligase machinery, and targets the receptor for proteasomal degradation. This mechanism serves to attenuate and terminate the EGF signal, preventing excessive or prolonged receptor activation.

The functional importance of this regulatory mechanism is supported by studies in both Drosophila and mammalian systems. In Drosophila, SOCS36E, the ortholog of mammalian SOCS4 and SOCS5, suppresses EGF receptor signaling in the imaginal wing disc [callus-2002-socs36e-drosophila]. Genetic studies demonstrated that SOCS36E phenotypes were exacerbated in flies heterozygous for the EGF receptor gene, providing genetic evidence for functional interaction between SOCS and EGFR pathways. The high degree of sequence conservation between Drosophila SOCS36E and mammalian SOCS4/SOCS5 (72% identity within the SH2 domain) suggests evolutionary conservation of this regulatory relationship [bullock-2007-socs4-structure].

In mammalian cells, SOCS4 is recognized as one of four EGF receptor inducible feedback inhibitors (IFIs), along with LRIG1, RALT/MIG6/ERRFI1, and SOCS5 [kario-2005-socs4-egfr]. Among these, SOCS4 and SOCS5 are unique in utilizing the ubiquitin-proteasome system to promote receptor degradation, while LRIG1 and RALT employ distinct mechanisms. The redundancy among these feedback inhibitors likely ensures robust control of EGFR signaling under diverse physiological conditions.

## Role in Antiviral Immunity

One of the most significant advances in understanding SOCS4 biology came from studies of influenza infection in SOCS4-deficient mice [kedzierski-2014-socs4-influenza]. These experiments provided the first demonstration of a clear functional phenotype in animals lacking functional SOCS4 protein. Mice expressing a truncated SOCS4 mutant (R108X, which lacks the SH2 domain and SOCS box) rapidly succumbed to infection with pathogenic H1N1 influenza virus and showed hypersusceptibility to the less virulent H3N2 strain.

The phenotype of SOCS4-deficient mice during influenza infection revealed a complex and somewhat paradoxical role for this protein in immune regulation. SOCS4-deficient animals exhibited dysregulated proinflammatory cytokine and chemokine production in the lungs, with elevated levels of IL-1beta, IL-4, IL-5, IL-6, IL-12p40, IL-13, IFN-gamma, and chemokines including CXCL1, CXCL2, and CCL2 [kedzierski-2014-socs4-influenza]. This cytokine storm pattern is characteristic of severe influenza pathology and contributes to tissue damage and disease severity.

Concurrently, SOCS4-deficient mice showed delayed viral clearance and impaired trafficking of virus-specific CD8+ T cells to the site of infection. Rather than migrating to the infected lungs, these effector T cells accumulated in the spleen. This trafficking defect was linked to impaired T cell receptor (TCR) activation, as evidenced by reduced downregulation of CD62L expression on activated CD8+ T cells in draining lymph nodes [kedzierski-2014-socs4-influenza]. In vitro studies confirmed that SOCS4-deficient CD8+ T cells exhibited impaired proliferation following TCR stimulation.

These findings revealed a dual regulatory role for SOCS4 in antiviral immunity: classical negative regulation of proinflammatory cytokine production (consistent with its function as a SOCS protein), combined with a previously unsuspected positive regulatory role in TCR signaling that promotes appropriate T cell activation and effector function. The loss of SOCS4 therefore results in both excessive inflammation and inadequate adaptive immune responses, a combination that is particularly detrimental during viral infection.

Complementary studies on SOCS5 in influenza infection have extended these findings [kedzierski-2017-socs5-influenza]. SOCS5-deficient mice also exhibited increased susceptibility to influenza, but the mechanism involved direct effects on EGFR signaling in airway epithelium, where SOCS5 restricts viral entry by inhibiting EGFR activity. The distinct but complementary roles of SOCS4 and SOCS5 in antiviral immunity highlight the importance of this SOCS subfamily in host defense.

## Role in Autoimmune Disease

The identification of a disease-causing SOCS4 mutation in a family with inherited autoimmunity provided the first direct link between SOCS4 dysfunction and human disease [arts-2015-socs4-mutation]. Whole-exome sequencing of affected family members identified a heterozygous missense mutation (T266M) in SOCS4 that cosegregated with autoimmune manifestations including hypothyroidism, vitiligo, and alopecia across multiple generations.

Functional studies demonstrated that the T266M mutation impairs SOCS4 function, resulting in insufficient modulation of EGFR signaling and defective inhibition of STAT3 [arts-2015-socs4-mutation]. The consequence of this impaired regulation is excessive IL-6 production following EGF stimulation. Given that IL-6 is a key proinflammatory cytokine implicated in autoimmune pathogenesis, the dysregulated IL-6 production likely underlies the autoimmune phenotype in this family. This mechanistic understanding led to the suggestion that anti-IL-6 blockade with tocilizumab might be a viable therapeutic strategy for SOCS4-related autoimmunity.

The findings from this human genetic study are consistent with the mouse influenza studies, which also demonstrated elevated IL-6 and other proinflammatory cytokines in SOCS4-deficient animals [kedzierski-2014-socs4-influenza]. Together, these observations establish SOCS4 as a critical regulator of inflammatory cytokine production and highlight the consequences of its dysfunction for immune homeostasis.

## Role as a Tumor Suppressor

Evidence from multiple cancer types supports a tumor suppressor role for SOCS4. In gastric cancer, expression profiling combined with chromosomal analysis identified SOCS4 as having significantly attenuated expression in tumor tissue compared to normal tissue [kobayashi-2012-socs4-gastric]. Investigation of the mechanism revealed that SOCS4 silencing occurs through promoter hypermethylation rather than chromosomal deletion. Analysis of surgically resected specimens demonstrated that 80% (40 of 50) of gastric tumors exhibited hypermethylation of the SOCS4 promoter region, and this methylation correlated with significantly reduced SOCS4 mRNA expression. Importantly, SOCS4 hypermethylation was associated with poor patient prognosis, suggesting prognostic utility as a biomarker [kobayashi-2012-socs4-gastric].

The tumor suppressor function of SOCS4 is mechanistically linked to its role as a negative regulator of EGF signaling. EGFR is frequently overexpressed or hyperactivated in epithelial cancers, where it promotes cell proliferation, survival, and invasion. By promoting EGFR degradation, SOCS4 counteracts the oncogenic potential of this receptor. Consistent with this model, an inverse relationship between EGFR expression and SOCS4/SOCS5 expression has been observed in aggressive hepatocellular carcinoma [croker-2008-socs-jak-stat].

Studies in breast cancer have also identified SOCS4 as having tumor suppressor properties. Higher expression levels of SOCS4 (along with SOCS1, SOCS3, and SOCS7) are associated with earlier tumor stage and better clinical outcome [trengove-2013-socs-development]. Conversely, reduced SOCS4 expression is observed in advanced disease, suggesting that loss of SOCS4-mediated growth control contributes to tumor progression.

The evolutionary conservation of SOCS4/SOCS5 tumor suppressor function is supported by studies in Drosophila. While SOCS36E has only modest effects on growth on its own, it functions as a potent tumor suppressor in combination with EGFR/RAS pathway activation, and the human ortholog SOCS5 behaves similarly in cellular transformation assays [callus-2002-socs36e-drosophila].

Post-transcriptional regulation of SOCS4 may also contribute to its tumor suppressor activity. MicroRNAs miR-98 and let-7 have been shown to suppress SOCS4 translation by targeting the 3' untranslated region [trengove-2013-socs-development]. Dysregulation of these microRNAs in cancer contexts could therefore contribute to reduced SOCS4 expression and consequent loss of tumor suppressor function.

A separate mechanism for SOCS4 inactivation in cancer involves transcriptional repression by the oncogenic transcription factor RUNX1/AML1 [scheitz-2012-runx1-socs4]. Studies using genetic lineage tracing demonstrated that RUNX1 directly represses SOCS4 and SOCS3 transcription, thereby enhancing STAT3 signaling and promoting cancer cell growth. Importantly, knockdown of SOCS4 rescued the growth defect caused by RUNX1 loss, providing functional evidence that SOCS4 repression is essential for the oncogenic activity of RUNX1. This mechanism was demonstrated in oral, skin, and ovarian epithelial cancers, suggesting broad relevance across epithelial malignancies [scheitz-2012-runx1-socs4]. The Runx1/SOCS4/Stat3 signaling axis represents a potential therapeutic target for cancer prevention and treatment.

## Role in Hematopoietic Cell Differentiation

Recent work has revealed an unexpected role for SOCS4 in hematopoietic cell fate decisions. A 2024 study demonstrated that SOCS4 influences the lineage bias of megakaryocyte-erythroid progenitor cells (MEPs), with SOCS4 promoting erythroid differentiation while inhibiting megakaryocytic differentiation [yuan-2024-socs4-differentiation]. This finding extends SOCS4 function beyond its established role in cytokine and growth factor signaling to include developmental cell fate determination.

The study identified SOCS4 as a direct target of the microRNA miR-1915-3p. Endogenous SOCS4 expression changes dynamically during megakaryocytic and erythroid differentiation, suggesting physiological relevance. Knockdown of SOCS4 reduced erythroid surface marker expression while enhancing megakaryocytic differentiation, mirroring the effects of miR-1915-3p overexpression. Conversely, SOCS4 overexpression promoted erythroid and suppressed megakaryocytic lineage commitment [yuan-2024-socs4-differentiation].

This function may be mechanistically linked to SOCS4's regulation of receptor tyrosine kinase signaling, as both erythropoietin receptor (EpoR) and thrombopoietin receptor (MPL) signaling pathways utilize JAK/STAT components that could be modulated by SOCS4. However, the precise molecular mechanism by which SOCS4 influences lineage choice remains to be fully elucidated. These findings have potential clinical implications for understanding thrombocytopenia and anemia, as well as for ex vivo production of platelets and red blood cells.

## Tissue Expression and Gene Regulation

SOCS4 exhibits broad tissue distribution with low tissue specificity, consistent with a general role in regulating cellular signaling [Human Protein Atlas]. Expression is notably elevated in lymphoid tissues, particularly lymph node (8.3 nTPM), thymus (7.5 nTPM), and appendix (7.4 nTPM), consistent with the immune regulatory functions revealed by studies in SOCS4-deficient mice. The brain shows moderate expression with highest levels in the hypothalamus (20.4 nTPM). At the single-cell level, high expression is observed in specialized cell types including fallopian tube ciliated cells and various endocrine cells.

SOCS4 expression is induced by EGF stimulation, consistent with its function as a negative feedback regulator of EGFR signaling [kario-2005-socs4-egfr]. This induction occurs through transcriptional mechanisms that remain to be fully characterized. In the context of immune cells, SOCS4 expression is likely also regulated by cytokine signaling, although specific inducers beyond EGF have not been extensively documented.

Post-transcriptional regulation of SOCS4 occurs through multiple mechanisms. As mentioned, microRNAs miR-98 and let-7 target the SOCS4 3'UTR to suppress translation [trengove-2013-socs-development]. This regulatory mechanism may be particularly important in pathological contexts where these microRNAs are dysregulated.

## Evolutionary Conservation

The SOCS family can be divided into evolutionarily distinct groups. SOCS4-7 represent the ancestral SOCS proteins, while CIS and SOCS1-3 are vertebrate-specific additions that arose later in evolution [callus-2002-socs36e-drosophila]. This evolutionary perspective is supported by the observation that Drosophila possesses only three SOCS proteins (SOCS16D, SOCS44A, and SOCS36E), of which SOCS36E is the clear ortholog of mammalian SOCS4 and SOCS5.

The high degree of sequence conservation between SOCS4 and SOCS5 (92% identity in the SH2 domain), and between these mammalian proteins and Drosophila SOCS36E (72% SH2 domain identity), indicates strong selective pressure to maintain the EGFR-regulatory function of this SOCS subfamily [bullock-2007-socs4-structure]. Functional studies in Drosophila demonstrate that SOCS36E suppresses both JAK/STAT and EGF receptor signaling, phenotypes that require intact SH2 and SOCS box domains [callus-2002-socs36e-drosophila]. This conservation extends to tumor suppressor function, as SOCS36E cooperates with EGFR/RAS pathway activation to suppress transformation.

## Open Questions

Despite significant progress in understanding SOCS4 function, several important questions remain unresolved:

**Substrate Specificity Beyond EGFR:** While EGFR pY1092 has been established as a high-affinity substrate, the full repertoire of SOCS4 targets remains to be defined. Low-affinity interactions with JAK2 and c-KIT have been reported, but their physiological significance is unclear. A systematic analysis of SOCS4 interactors and substrates would provide a more complete picture of its regulatory scope.

**N-Terminal Domain Function:** The extended N-terminal region of SOCS4, including the NTCR shared with SOCS5, remains poorly characterized. By analogy with SOCS5, this region may contain a JAK interaction region enabling direct kinase regulation, but this has not been experimentally confirmed for SOCS4.

**TCR Signaling Mechanism:** The observation that SOCS4 positively regulates TCR activation is mechanistically unexpected for a SOCS protein and requires further investigation. The molecular targets through which SOCS4 promotes T cell activation remain unidentified.

**Tissue-Specific Functions:** Given the broad tissue distribution of SOCS4, tissue-specific conditional knockout studies would be valuable for understanding its roles in specific organ systems beyond the immune compartment.

**Redundancy with SOCS5:** The high degree of sequence similarity between SOCS4 and SOCS5 SH2 domains suggests potential functional redundancy. Compound knockout studies would help clarify the extent of overlapping versus distinct functions.

**Therapeutic Potential:** Given its tumor suppressor function and role in immune regulation, strategies to restore or enhance SOCS4 activity could have therapeutic applications in cancer and autoimmune disease. However, the feasibility of such approaches remains to be explored.

## References

- [alexander-2002-socs-immune] Alexander WS. Suppressors of cytokine signalling (SOCS) in the immune system. Nat Rev Immunol. 2002 Jun;2(6):410-6. DOI: 10.1038/nri818. PMID: 12093007.

- [arts-2015-socs4-mutation] Arts P, Plantinga TS, van den Berg JM, et al. A missense mutation underlies defective SOCS4 function in a family with autoimmunity. J Intern Med. 2015 Aug;278(2):203-10. DOI: 10.1111/joim.12351. PMID: 25639832.

- [babon-2009-socs-cullin5] Babon JJ, Sabo JK, Zhang JG, Nicola NA, Norton RS. The SOCS box encodes a hierarchy of affinities for Cullin5: implications for ubiquitin ligase formation and cytokine signalling suppression. J Mol Biol. 2009 Apr 3;387(1):162-74. DOI: 10.1016/j.jmb.2009.01.024. PMID: 19385048. PMCID: PMC2720833.

- [bullock-2007-socs4-structure] Bullock AN, Rodriguez MC, Debreczeni JE, Songyang Z, Knapp S. Structure of the SOCS4-ElonginB/C complex reveals a distinct SOCS box interface and the molecular basis for SOCS-dependent EGFR degradation. Structure. 2007 Nov;15(11):1493-504. DOI: 10.1016/j.str.2007.09.016. PMID: 17997974. PMCID: PMC2225448.

- [callus-2002-socs36e-drosophila] Callus BA, Mathey-Prevot B. SOCS36E, a novel Drosophila SOCS protein, suppresses JAK/STAT and EGF-R signalling in the imaginal wing disc. Oncogene. 2002 Jul 18;21(31):4812-21. DOI: 10.1038/sj.onc.1205618. PMID: 12101419.

- [croker-2008-socs-jak-stat] Croker BA, Kiu H, Nicholson SE. SOCS regulation of the JAK/STAT signalling pathway. Semin Cell Dev Biol. 2008 Aug;19(4):414-22. DOI: 10.1016/j.semcdb.2008.07.010. PMID: 18708154. PMCID: PMC2597703.

- [kario-2005-socs4-egfr] Kario E, Marmor MD, Adamsky K, et al. Suppressors of cytokine signaling 4 and 5 regulate epidermal growth factor receptor signaling. J Biol Chem. 2005 Feb 25;280(8):7038-48. DOI: 10.1074/jbc.M408575200. PMID: 15590694.

- [kedzierski-2014-socs4-influenza] Kedzierski L, Linossi EM, Kolesnik TB, et al. Suppressor of Cytokine Signaling 4 (SOCS4) Protects against Severe Cytokine Storm and Enhances Viral Clearance during Influenza Infection. PLoS Pathog. 2014 May 8;10(5):e1004134. DOI: 10.1371/journal.ppat.1004134. PMID: 24809749. PMCID: PMC4014316.

- [kedzierski-2017-socs5-influenza] Kedzierski L, et al. Suppressor of cytokine signaling (SOCS)5 ameliorates influenza infection via inhibition of EGFR signaling. eLife. 2017 Feb 14;6:e20444. DOI: 10.7554/eLife.20444.

- [kobayashi-2012-socs4-gastric] Kobayashi D, Nomoto S, Kodera Y, et al. Suppressor of cytokine signaling 4 detected as a novel gastric cancer suppressor gene using double combination array analysis. World J Surg. 2012 Feb;36(2):362-72. DOI: 10.1007/s00268-011-1358-2. PMID: 22127425.

- [scheitz-2012-runx1-socs4] Scheitz CJ, Lee TS, McDermitt DJ, Tumbar T. Defining a tissue stem cell-driven Runx1/Stat3 signalling axis in epithelial cancer. EMBO J. 2012 Nov 5;31(21):4124-39. DOI: 10.1038/emboj.2012.270. PMID: 23034403.

- [trengove-2013-socs-development] Trengove MC, Ward AC. SOCS proteins in development and disease. Am J Clin Exp Immunol. 2013;2(1):1-29. PMID: 23885323. PMCID: PMC3714205.

- [yuan-2024-socs4-differentiation] Yuan X, Liu P, Xu L, et al. miR-1915-3p regulates megakaryocytic and erythroid differentiation by targeting SOCS4. Thromb J. 2024 Aug 9;22(1):74. DOI: 10.1186/s12959-024-00615-6.

- Human Protein Atlas. SOCS4 protein expression summary. https://www.proteinatlas.org/ENSG00000180008-SOCS4

- NCBI Gene. SOCS4 suppressor of cytokine signaling 4 [Homo sapiens (human)]. Gene ID: 122809. https://www.ncbi.nlm.nih.gov/gene/122809


## Citations

1. alexander-2002-socs-immune-abstract.md
2. arts-2015-socs4-mutation-abstract.md
3. arts-2015-socs4-mutation-summary.md
4. babon-2009-socs-cullin5-abstract.md
5. bullock-2007-socs4-structure-abstract.md
6. bullock-2007-socs4-structure-summary.md
7. callus-2002-socs36e-drosophila-abstract.md
8. croker-2008-socs-jak-stat-abstract.md
9. kario-2005-socs4-egfr-abstract.md
10. kedzierski-2014-socs4-influenza-abstract.md
11. kedzierski-2014-socs4-influenza-summary.md
12. kedzierski-2017-socs5-influenza-abstract.md
13. kobayashi-2012-socs4-gastric-abstract.md
14. scheitz-2012-runx1-socs4-abstract.md
15. trengove-2013-socs-development-abstract.md
16. yuan-2024-socs4-differentiation-abstract.md