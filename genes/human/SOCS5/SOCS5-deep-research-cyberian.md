---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-23T21:00:56.374744'
end_time: '2026-01-23T21:16:32.117490'
duration_seconds: 935.74
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: SOCS5
  gene_symbol: SOCS5
  uniprot_accession: O75159
  protein_description: 'RecName: Full=Suppressor of cytokine signaling 5; Short=SOCS-5;
    AltName: Full=Cytokine-inducible SH2 protein 6; Short=CIS-6; AltName: Full=Cytokine-inducible
    SH2-containing protein 5;'
  gene_info: Name=SOCS5; Synonyms=CIS6, CISH5, CISH6, KIAA0671;
  organism_full: Homo sapiens (Human).
  protein_family: Not specified in UniProt
  protein_domains: SH2. (IPR000980); SH2_dom_sf. (IPR036860); SOCS4/SOCS5_dom. (IPR022252);
    SOCS5_SOCS. (IPR037343); SOCS_box. (IPR001496)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 11
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** O75159
- **Protein Description:** RecName: Full=Suppressor of cytokine signaling 5; Short=SOCS-5; AltName: Full=Cytokine-inducible SH2 protein 6; Short=CIS-6; AltName: Full=Cytokine-inducible SH2-containing protein 5;
- **Gene Information:** Name=SOCS5; Synonyms=CIS6, CISH5, CISH6, KIAA0671;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** SH2. (IPR000980); SH2_dom_sf. (IPR036860); SOCS4/SOCS5_dom. (IPR022252); SOCS5_SOCS. (IPR037343); SOCS_box. (IPR001496)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "SOCS5" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'SOCS5' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **SOCS5** (gene ID: SOCS5, UniProt: O75159) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Suppressor of Cytokine Signaling 5 (SOCS5): A Comprehensive Functional Review

## Introduction and Summary

Suppressor of Cytokine Signaling 5 (SOCS5) is a member of the SOCS family of intracellular proteins that function as negative regulators of cytokine and growth factor signaling. The human SOCS5 gene (UniProt: O75159, OMIM: 607094) encodes a 536-amino acid protein located on chromosome 2p21 [trengove-2013-socs-review-abstract]. Unlike other SOCS family members that predominantly regulate cytokine receptor signaling, SOCS5 has emerged as a key regulator of receptor tyrosine kinase (RTK) signaling, particularly through its ability to target the epidermal growth factor receptor (EGFR) for degradation [nicholson-2005-socs5-egfr-abstract]. SOCS5 functions through two mechanistically distinct pathways: first, as an E3 ubiquitin ligase adapter that facilitates proteasomal degradation of target receptors, and second, through direct inhibition of Janus kinases (JAK1 and JAK2) via a unique N-terminal region [linossi-2013-socs5-jak-shc1-abstract]. The protein is expressed ubiquitously with notably high expression in the brain and has been implicated in regulating T helper cell differentiation, anti-viral immunity, and cancer suppression.

## Domain Architecture and Structural Features

SOCS5 is characterized by three distinct structural domains that are conserved across the SOCS family. The central SH2 (Src Homology 2) domain enables recognition and binding to phosphorylated tyrosine residues on target proteins, while the C-terminal SOCS box (approximately 40 amino acids) functions as an adapter that recruits the E3 ubiquitin ligase machinery [sondergaard-2016-cullin5-review-abstract]. What distinguishes SOCS5 from other SOCS family members is its extended N-terminal region of approximately 369 residues, which it shares only with the closely related SOCS4 [linossi-2013-socs5-jak-shc1-abstract].

The N-terminal region of SOCS5 contains a unique JAK interaction region (JIR), spanning residues 175-244, which enables direct binding to the catalytic domains of JAK kinases with measured binding affinities around 0.5 μM for JAK1 [linossi-2013-socs5-jak-shc1-abstract]. This JIR is conserved between SOCS5 orthologs but is distinct from the kinase inhibitory region (KIR) found in SOCS1 and SOCS3, indicating that SOCS5 employs a fundamentally different mechanism for JAK inhibition. SOCS4 and SOCS5 share 92% amino acid identity within their SH2 domains and approximately 49% overall amino acid identity, suggesting they may have partially overlapping functions [trengove-2013-socs-review-abstract].

The SH2 domain of SOCS5 contains an extended SH2 subdomain (ESS), an N-terminal alpha-helix that stabilizes the phosphotyrosine-binding loop and is characteristic of SOCS family proteins. Surface plasmon resonance studies have determined that the SOCS5 SH2 domain binds to phosphoTyr317 on Shc-1 with high affinity (Kd = 0.16 μM), which represents a 25-fold tighter interaction compared to Shc-1 pY239 and exceeds the affinity for EGFR pY1092 (Kd = 0.87 μM) [linossi-2013-socs5-jak-shc1-abstract]. The SOCS box consists of a BC box and a Cullin5 box that mediate interactions with Elongin B/C and Cullin5, respectively, forming the complete E3 ubiquitin ligase complex [sondergaard-2016-cullin5-review-abstract].

## Three-Dimensional Structure

Experimental structural information for SOCS5 is limited to the JAK interaction region within the N-terminal domain. The NMR solution structure of mouse SOCS5 residues 175-244 (PDB ID: 2N34) was determined by Chandrashekaran and colleagues [chandrashekaran-2015-socs5-jir-structure-abstract]. This structure revealed that the JIR, despite being within a largely disordered N-terminal region, contains preformed structural elements consisting of an alpha-helix spanning residues 224-233, preceded by a turn and an extended structure. The presence of these preformed elements within an otherwise disordered region suggests they may serve as recognition motifs for JAK binding, reducing the entropic cost of binding by providing a pre-organized interaction surface.

The structural study also identified a phosphorylation site at Ser211 and investigated its role in modulating JAK interactions [chandrashekaran-2015-socs5-jir-structure-abstract]. Post-translational modification at this site could potentially serve as a regulatory mechanism for SOCS5's interaction with JAK kinases, though the physiological significance of this phosphorylation event remains to be fully characterized.

No crystal or NMR structure is currently available for the full-length SOCS5 protein or for SOCS5 in complex with its binding partners (EGFR, Shc-1, or Elongin B/C-Cullin5). The highly conserved SH2 and SOCS box domains are likely to adopt structures similar to those determined for other SOCS family members, given the high sequence conservation within these regions.

## Evolutionary Conservation

SOCS5 is an evolutionarily ancient protein that was present in the common ancestor of animals. The polypeptide sequences of SOCS proteins are highly conserved among mammals; for example, human and porcine SOCS5 share 96.6% amino acid identity. This high degree of conservation suggests strong selective pressure to maintain SOCS5 function throughout vertebrate evolution.

The SOCS gene family in extant vertebrates evolved from ancestral SOCS1/SOCS2/SOCS3/CISH and SOCS4/SOCS5 intermediates through two rounds of whole genome duplications (WGDs). SOCS4 and SOCS5 form a distinct evolutionary clade, sharing significant sequence homology with each other while being more distantly related to other SOCS family members. This evolutionary relationship is consistent with the functional similarities observed between these two proteins, including their roles in regulating receptor tyrosine kinase signaling and their extended N-terminal domains.

In Drosophila melanogaster, the SOCS5 ortholog is Socs36E, which shares 64% identity with human SOCS5 in the conserved carboxy-terminal region (SH2 domain and SOCS box) [stec-2011-drosophila-socs-abstract]. Functional studies in Drosophila have demonstrated remarkable conservation of function across species. Like its mammalian counterpart, Socs36E is both a target gene and negative regulator of JAK/STAT signaling, operating through a classical negative feedback mechanism. Socs36E also weakly inhibits EGFR signaling, mirroring the function of mammalian SOCS5. Importantly, Socs36E has been identified as a tumor suppressor in Drosophila epithelial transformation models, behaving as a cooperating factor that limits EGFR-driven tumorigenesis [stec-2011-drosophila-socs-abstract]. Notably, Socs36E null mutant flies remain viable, similar to SOCS5 knockout mice, suggesting that functional redundancy in signal transduction regulation is a conserved feature across metazoan evolution.

## Molecular Function as an E3 Ubiquitin Ligase Adapter

The primary biochemical function of SOCS5 is to serve as a substrate recognition subunit within a Cullin-RING E3 ubiquitin ligase complex. Through its SOCS box domain, SOCS5 recruits Elongin B and Elongin C, which in turn associate with Cullin5 and the RING domain protein Rbx2 [sondergaard-2016-cullin5-review-abstract]. This multi-protein complex enables the transfer of ubiquitin to substrates bound by the SOCS5 SH2 domain, marking them for proteasomal degradation.

The SOCS box is disordered in isolation and only becomes structured upon Elongin B/C association. The interaction depends upon the first 12 residues of the SOCS box domain, particularly a deeply buried, conserved leucine residue. Biochemical studies have determined that SOCS5 binds Cullin5 with high affinity (Kd approximately 10 nM), comparable to other SOCS family members, though this interaction requires prior recruitment of Elongin B/C [sondergaard-2016-cullin5-review-abstract]. The critical recognition motif in the Cullin5 box is defined by the sequence LPΦP (where Φ represents a hydrophobic residue), which mediates specific Cullin5 binding.

This E3 ligase activity is essential for SOCS5's ability to regulate EGFR signaling. When SOCS5 is overexpressed, it promotes enhanced downregulation of EGFR from the cell surface following EGF treatment, primarily through increased receptor degradation rather than altered internalization rates [nicholson-2005-socs5-egfr-abstract]. Importantly, the SOCS box is required for this function, as SOCS box-deleted mutants fail to promote EGFR degradation.

## Regulation of Epidermal Growth Factor Receptor Signaling

One of the best-characterized functions of SOCS5 is its role as a negative regulator of EGFR signaling. The initial demonstration of this function came from studies showing that SOCS5 associates with the EGFR complex in an EGF-independent manner and that the mitogenic response to EGF is dramatically inhibited in SOCS5-expressing cell lines compared to control lines [nicholson-2005-socs5-egfr-abstract]. This inhibition occurs through enhanced proteasomal degradation of the EGFR, dependent on SOCS box recruitment of E3 ubiquitin ligase activity.

Both the N-terminal region and the SH2 domain of SOCS5 contribute to EGFR binding. Uniquely, SOCS5 can associate with EGFR independently of receptor phosphorylation, which distinguishes it from many other SH2 domain-containing proteins that require phosphotyrosine recognition for binding [nicholson-2005-socs5-egfr-abstract]. This constitutive association may enable SOCS5 to function as a pre-positioned negative regulator, ready to dampen signaling upon receptor activation.

SOCS5's regulation of EGFR has important physiological consequences. Studies in COPD patients revealed that SOCS5 levels are diminished in respiratory epithelial cells, correlating with increased susceptibility to influenza virus infection [kedzierski-2017-socs5-influenza-abstract]. Using mouse models, researchers demonstrated that SOCS5-deficient animals exhibit heightened disease severity during influenza infection, with increased viral titers and weight loss. This phenotype can be attributed to dysregulated EGFR signaling, as EGFR activation promotes viral replication in epithelial cells. These findings suggest that therapeutic interventions targeting SOCS5 expression could represent a novel treatment strategy for respiratory viral infections.

Beyond EGFR, SOCS5 has also been shown to target other ErbB family members including ERBB2 (HER2) and ERBB4, while sparing other cell surface proteins, indicating substrate specificity within the receptor tyrosine kinase family [nicholson-2005-socs5-egfr-abstract].

## Regulation of JAK-STAT Signaling

In addition to its role in RTK signaling, SOCS5 functions as a regulator of the JAK-STAT pathway through a mechanistically distinct mechanism. Studies have demonstrated that SOCS5 can interact directly with JAK kinases via its unique N-terminal JIR, and co-expression of SOCS5 specifically reduces the autophosphorylation of JAK1 and JAK2 while having no effect on JAK3 or TYK2 [linossi-2013-socs5-jak-shc1-abstract]. This selectivity indicates that SOCS5 has evolved to regulate specific subsets of JAK-dependent signaling pathways.

The mechanism of JAK inhibition by SOCS5 appears distinct from that of SOCS1 and SOCS3, which employ a kinase inhibitory region (KIR) to directly block the JAK catalytic site. Mutation of the putative KIR region in SOCS5 (His360) had only a modest impact on JAK1 inhibition compared to deletion of the N-terminus, indicating that SOCS5 uses fundamentally different structural elements for kinase inhibition [linossi-2013-socs5-jak-shc1-abstract]. The JIR alone is unlikely to be a direct JAK inhibitor, suggesting it functions primarily as a binding mediator, with additional N-terminal residues contributing to the inhibitory mechanism.

An important target of SOCS5's JAK regulatory activity is the IL-4 signaling pathway. The initial characterization of SOCS5 function in T helper cell biology demonstrated that SOCS5 protein is preferentially expressed in committed Th1 cells and interacts with the cytoplasmic region of the IL-4 receptor alpha chain [seki-2002-socs5-il4-stat6-abstract]. This interaction is unconventional in that it occurs irrespective of receptor tyrosine phosphorylation, with SOCS5 binding to the box1 region of IL-4R and reducing JAK1 association with the receptor. The functional consequence is inhibition of IL-4-mediated STAT6 activation. Transgenic mice constitutively expressing SOCS5 showed five-fold less Th2 development compared to littermate controls, supporting a role for SOCS5 in promoting Th1-biased immune responses [seki-2002-socs5-il4-stat6-abstract].

## Regulation of Growth Factor Adaptor Protein Shc-1

Beyond receptor targeting, SOCS5 has been identified as a potential regulator of downstream signaling adaptor proteins. The identification of phosphoTyr317 on Shc-1 as a high-affinity binding site for the SOCS5 SH2 domain (Kd = 0.16 μM) suggests that SOCS5 may negatively regulate EGF and growth factor-driven Shc-1 signaling [linossi-2013-socs5-jak-shc1-abstract]. Shc-1 is an important adaptor protein that links receptor tyrosine kinases to the Ras-MAPK signaling cascade through recruitment of Grb2. By binding to phosphorylated Shc-1, SOCS5 may compete with Grb2 recruitment and thereby attenuate mitogenic signaling.

This finding positions SOCS5 as a potential regulator of multiple points in growth factor signaling pathways, both at the level of receptor stability (through EGFR degradation) and at the level of downstream signal transduction (through Shc-1 binding). Such multi-layered regulation would be consistent with SOCS5's proposed role as a tumor suppressor.

## Subcellular Localization

SOCS5 is primarily a cytoplasmic protein, consistent with its function in regulating cytoplasmic signaling pathways. The Human Protein Atlas indicates ubiquitous cytoplasmic expression across human tissues [trengove-2013-socs-review-abstract]. This localization enables SOCS5 to interact with activated receptor tyrosine kinases at the plasma membrane and with cytoplasmic JAK kinases associated with cytokine receptors.

The predominantly cytoplasmic localization of SOCS5 is consistent with its function as an E3 ligase adapter. By remaining in the cytoplasm, SOCS5 is positioned to encounter activated receptors that have been internalized from the plasma membrane, as well as to associate with receptor complexes at the cell surface. The EGFR, for example, is internalized upon ligand binding and traffics through endosomal compartments where SOCS5-mediated ubiquitination could target it for lysosomal degradation rather than recycling to the plasma membrane.

## Tissue Expression and Physiological Roles

Northern blot analysis reveals wide expression of SOCS5 transcripts across human tissues, with a 4.2 kb transcript detected in most tissues tested, though expression is notably weaker in pancreas and spleen [trengove-2013-socs-review-abstract]. SOCS5 was initially identified through screening for cDNAs encoding proteins expressed in brain, and the protein shows notably high expression in multiple brain regions including the cortex, hippocampus, cerebellum, and substantia nigra.

Despite high expression in the brain, SOCS5-deficient mice show no obvious neurological phenotype under normal conditions [brender-2004-socs5-lymphocyte-abstract]. However, when challenged with neurotropic viral infection, the importance of SOCS5 in the central nervous system becomes apparent. Studies using Semliki Forest virus infection in SOCS5-deficient mice revealed that lack of SOCS5 results in more severe neuroinflammation, with increased infiltration of CD11b+ cells, neutrophils, and inflammatory monocytes into the brain [kedzierski-2022-socs5-alphavirus-abstract]. SOCS5-deficient animals also displayed marked vacuolation of grey and white matter with multifocal parenchymal necrosis. These findings indicate that SOCS5 is a vital regulator of anti-viral immunity that mediates the critical balance between immunopathology and virus persistence in the CNS.

The generation of SOCS5 knockout mice by Brender and colleagues revealed that SOCS5-deficient animals are viable, fertile, and show no overt pathological changes [brender-2004-socs5-lymphocyte-abstract]. B and T cell development proceeds normally, and cytokine and antigen-induced proliferative responses remain intact. Notably, the predicted role of SOCS5 in Th1/Th2 differentiation based on overexpression studies was not confirmed in knockout animals, with CD4+ T cells showing normal Th1/Th2 responses both in vitro and in vivo. This discrepancy may be explained by functional redundancy with SOCS4, which shares significant sequence homology with SOCS5. Studies of SOCS4/SOCS5 double knockout mice would be required to fully address this question.

## Role in Cancer and Tumor Suppression

Growing evidence supports a role for SOCS5 as a tumor suppressor, primarily through its negative regulation of EGFR and JAK-STAT signaling pathways. Epigenetic silencing of SOCS5 through DNA hypermethylation has been reported in multiple cancer types, including hepatocellular carcinoma, cervical cancer, and thyroid tumors [sharma-2019-socs5-tall-abstract].

In T-cell acute lymphoblastic leukemia (T-ALL), SOCS5 expression is epigenetically regulated by DNA methyltransferase-3A-mediated DNA methylation and methyl CpG binding protein-2-mediated histone deacetylation [sharma-2019-socs5-tall-abstract]. Forced SOCS5 expression in leukemic cells inhibits proliferation and cell cycle progression, while SOCS5 inactivation accelerates leukemia engraftment in mouse models. Interestingly, SOCS5 silencing leads to increased expression of IL-7 and IL-4 receptors and enhanced JAK-STAT pathway activation, consistent with loss of SOCS5's negative regulatory function.

Additional evidence for tumor suppressive function comes from studies showing that microRNA-9, which is elevated in some tumors, directly targets SOCS5 mRNA for degradation, resulting in enhanced JAK1/2 and STAT1/3 phosphorylation in endothelial cells [trengove-2013-socs-review-abstract]. By positioning SOCS5 as a regulator of multiple oncogenic signaling pathways, these studies suggest that restoration of SOCS5 expression could represent a therapeutic strategy in cancers characterized by SOCS5 silencing.

## Open Questions

Several important questions regarding SOCS5 function remain to be addressed:

1. **Mechanism of JAK inhibition**: While SOCS5 clearly inhibits JAK1 and JAK2, the precise molecular mechanism remains unclear. Unlike SOCS1 and SOCS3, SOCS5 lacks a canonical KIR domain, and the contribution of different N-terminal regions to JAK selectivity has not been fully characterized.

2. **SOCS4/SOCS5 functional redundancy**: The lack of an overt phenotype in SOCS5 knockout mice may reflect compensation by SOCS4. Generation and characterization of SOCS4/SOCS5 double knockout mice would be essential to understand the true physiological requirements for these proteins.

3. **Structural characterization**: While one NMR structure of SOCS5 domains exists in the Protein Data Bank, full-length structural analysis and characterization of SOCS5 in complex with its targets (JAK, EGFR, Shc-1) would provide important mechanistic insights.

4. **Substrate selectivity**: The full range of SOCS5 substrates beyond EGFR, Shc-1, and IL-4R remains to be determined. Proteomics approaches could identify additional binding partners and substrates for ubiquitination.

5. **Tissue-specific functions**: The high expression of SOCS5 in brain suggests potential neural-specific functions that have not been fully explored. The role of SOCS5 in regulating neuroinflammation during viral infection suggests it may be important in other neurological conditions.

6. **Therapeutic targeting**: Given the tumor suppressive function of SOCS5, strategies to restore or enhance SOCS5 expression in cancer may have therapeutic value. Conversely, understanding whether SOCS5 inhibition could enhance anti-viral or anti-tumor immune responses requires further investigation.

7. **Regulation of SOCS5 expression**: While epigenetic silencing has been documented, the physiological signals that regulate SOCS5 expression levels remain poorly characterized compared to other SOCS family members.

## References

1. **[linossi-2013-socs5-jak-shc1]** Linossi EM, Chandrashekaran IR, Kolesnik TB, Murphy JM, Webb AI, Willson TA, Kedzierski L, Bullock AN, Babon JJ, Norton RS, Nicola NA, Nicholson SE. Suppressor of Cytokine Signaling (SOCS) 5 Utilises Distinct Domains for Regulation of JAK1 and Interaction with the Adaptor Protein Shc-1. PLoS One. 2013 Aug 26;8(8):e70536. PMID: 23990909; PMCID: PMC3749136; DOI: 10.1371/journal.pone.0070536. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC3749136/

2. **[nicholson-2005-socs5-egfr]** Nicholson SE, Metcalf D, Sprigg NS, Columbus R, Walker F, Silva A, Cary D, Willson TA, Zhang JG, Hilton DJ, Alexander WS, Nicola NA. Suppressor of cytokine signaling (SOCS)-5 is a potential negative regulator of epidermal growth factor signaling. Proc Natl Acad Sci USA. 2005 Feb 15;102(7):2328-33. PMID: 15695332; PMCID: PMC549009; DOI: 10.1073/pnas.0409675102. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC549009/

3. **[seki-2002-socs5-il4-stat6]** Seki Y, Hayashi K, Matsumoto A, Seki N, Tsukada J, Ransom J, Naka T, Kishimoto T, Yoshimura A, Kubo M. Expression of the suppressor of cytokine signaling-5 (SOCS5) negatively regulates IL-4-dependent STAT6 activation and Th2 differentiation. Proc Natl Acad Sci USA. 2002 Sep 17;99(20):13003-8. PMID: 12242343; PMCID: PMC130576; DOI: 10.1073/pnas.202477099. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC130576/

4. **[kedzierski-2017-socs5-influenza]** Kedzierski L, Tate MD, Hsu AC, Kolesnik TB, Linossi EM, Dagley L, Dong Z, Freeman S, Infusini G, Starkey MR, Bird NL, Chatfield SM, Babon JJ, Huntington N, Belz G, Webb A, Wark PAB, Nicola NA, Xu J, Kedzierska K, Hansbro PM, Nicholson SE. Suppressor of cytokine signaling (SOCS)5 ameliorates influenza infection via inhibition of EGFR signaling. eLife. 2017 Jan 6;6:e20444. DOI: 10.7554/eLife.20444. URL: https://elifesciences.org/articles/20444

5. **[brender-2004-socs5-lymphocyte]** Brender C, Columbus R, Metcalf D, Handman E, Starr R, Huntington N, Tarlinton D, Ødum N, Nicholson SE, Nicola NA, Hilton DJ, Alexander WS. SOCS5 Is Expressed in Primary B and T Lymphoid Cells but Is Dispensable for Lymphocyte Production and Function. Mol Cell Biol. 2004 Jul;24(13):6094-103. PMID: 15199163; PMCID: PMC480873; DOI: 10.1128/MCB.24.13.6094-6103.2004. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC480873/

6. **[kedzierski-2022-socs5-alphavirus]** Kedzierski L, Tan AEQI, Foo IJH, Nicholson SE, Fazakerley JK. Suppressor of Cytokine Signalling 5 (SOCS5) Modulates Inflammatory Responses during Alphavirus Infection. Viruses. 2022 Nov 9;14(11):2476. PMID: 36366574; PMCID: PMC9692489; DOI: 10.3390/v14112476. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC9692489/

7. **[trengove-2013-socs-review]** Trengove MC, Ward AC. SOCS proteins in development and disease. Am J Clin Exp Immunol. 2013 Feb 27;2(1):1-29. PMID: 23885323; PMCID: PMC3714205. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC3714205/

8. **[sharma-2019-socs5-tall]** Sharma ND, Nickl CK, Kang H, et al. Epigenetic silencing of SOCS5 potentiates JAK-STAT signaling and progression of T-cell acute lymphoblastic leukemia. Cancer Sci. 2019 Jun;110(6):1931-1946. PMID: 30974024; PMCID: PMC6549933; DOI: 10.1111/cas.14021. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC6549933/

9. **[sondergaard-2016-cullin5-review]** Sondergaard JN, et al. The role of cullin 5-containing ubiquitin ligases. Cell Div. 2016 Mar 29;11:5. PMID: 27030794; PMCID: PMC4812663; DOI: 10.1186/s13008-016-0016-3. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC4812663/

10. **[chandrashekaran-2015-socs5-jir-structure]** Chandrashekaran IR, Mohanty B, Linossi EM, Nicholson SE, Babon JJ, Norton RS, Dagley LF, Leung EWW, Murphy JM. NMR assignments and solution structure of the JAK interaction region of SOCS5. Biochemistry. 2015 Jul 21;54(28):4672-82. PMID: 26173083; DOI: 10.1021/acs.biochem.5b00619. PDB: 2N34. URL: https://www.rcsb.org/structure/2n34

11. **[stec-2011-drosophila-socs]** Stec WJ, Zeidler MP. Drosophila SOCS Proteins. J Signal Transduct. 2011;2011:894510. PMCID: PMC3238392; DOI: 10.1155/2011/894510. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC3238392/


## Citations

1. brender-2004-socs5-lymphocyte-abstract.md
2. chandrashekaran-2015-socs5-jir-structure-abstract.md
3. kedzierski-2017-socs5-influenza-abstract.md
4. kedzierski-2022-socs5-alphavirus-abstract.md
5. linossi-2013-socs5-jak-shc1-abstract.md
6. nicholson-2005-socs5-egfr-abstract.md
7. seki-2002-socs5-il4-stat6-abstract.md
8. sharma-2019-socs5-tall-abstract.md
9. sondergaard-2016-cullin5-review-abstract.md
10. stec-2011-drosophila-socs-abstract.md
11. trengove-2013-socs-review-abstract.md