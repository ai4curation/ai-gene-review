---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-24T00:39:05.088701'
end_time: '2026-01-24T00:54:53.866610'
duration_seconds: 948.78
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: WIPF1
  gene_symbol: WIPF1
  uniprot_accession: O43516
  protein_description: 'RecName: Full=WAS/WASL-interacting protein family member 1;
    AltName: Full=Protein PRPL-2; AltName: Full=Wiskott-Aldrich syndrome protein-interacting
    protein; Short=WASP-interacting protein;'
  gene_info: Name=WIPF1; Synonyms=WASPIP, WIP;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the verprolin family. .
  protein_domains: PH-like_dom_sf. (IPR011993); WAS/WASL-interacting_domain. (IPR053099);
    WH2_dom. (IPR003124); WH2 (PF02205)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 29
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** O43516
- **Protein Description:** RecName: Full=WAS/WASL-interacting protein family member 1; AltName: Full=Protein PRPL-2; AltName: Full=Wiskott-Aldrich syndrome protein-interacting protein; Short=WASP-interacting protein;
- **Gene Information:** Name=WIPF1; Synonyms=WASPIP, WIP;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the verprolin family. .
- **Key Domains:** PH-like_dom_sf. (IPR011993); WAS/WASL-interacting_domain. (IPR053099); WH2_dom. (IPR003124); WH2 (PF02205)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "WIPF1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'WIPF1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **WIPF1** (gene ID: WIPF1, UniProt: O43516) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# WIPF1 (WAS/WASL-interacting protein family member 1): A Comprehensive Research Report

## Introduction

WIPF1 (WAS/WASL-interacting protein family member 1), also known as WIP (WASP-interacting protein), is a proline-rich scaffolding protein that serves as a critical regulator of actin cytoskeleton dynamics in hematopoietic cells. First identified in 1997 by Ramesh and colleagues through a yeast two-hybrid screen designed to find binding partners of the Wiskott-Aldrich syndrome protein (WASP), WIP has emerged as a multifunctional protein essential for proper immune cell function, actin polymerization, and cellular motility [ramesh-1997-wip-discovery-abstract]. The protein is encoded by the WIPF1 gene (with synonyms WASPIP and WIP) and belongs to the evolutionarily conserved verprolin protein family, with orthologs found in organisms ranging from yeast (Vrp1p) to humans [munn-2009-verprolin-review-abstract].

WIP functions primarily as a chaperone and stabilizer of WASP, protecting it from degradation while also acting as a regulator of its actin polymerization activity. Beyond its WASP-dependent roles, WIP exhibits autonomous functions in actin cytoskeleton remodeling and serves as a hub for multiple signaling pathways through its extensive proline-rich sequences. The protein is intrinsically disordered, consisting of consecutive small functional domains and motifs that mediate interactions with a diverse array of cellular partners [sokolik-2020-wip-structure-abstract]. This structural flexibility enables WIP to function as a versatile adapter that integrates multiple signaling inputs to regulate actin-dependent cellular processes, including immune synapse formation, cell migration, phagocytosis, and pathogen subversion.

## Domain Architecture and Structural Features

WIP is a 503-amino acid polypeptide characterized by its intrinsically disordered nature, with over 30% of its primary sequence consisting of proline residues [sokolik-2020-wip-structure-abstract]. The protein architecture can be divided into three major functional segments: an N-terminal actin-binding domain, a central proline-rich region that binds SH3 domain-containing proteins, and a C-terminal WASP-binding domain.

The N-terminal region contains actin-binding motifs (ABMs) that directly interact with actin monomers. Structural studies using NMR spectroscopy have revealed that this domain, while largely disordered in its unbound state, contains regions with transient helical and beta-strand character that become ordered upon actin binding [elazari-shalom-2015-abstract]. The actin-binding function is mediated primarily through WH2 (WASP Homology 2) domains, which are approximately 35-residue motifs that bind actin monomers with high affinity [paunola-2002-wh2-review-abstract]. Importantly, functional studies in yeast demonstrated that the WH2 domain is essential for WIP's ability to complement verprolin-deficient cells, underscoring its critical role in cytoskeletal function [vaduva-1999-wip-yeast-abstract].

The central region of WIP is dominated by proline-rich sequences that serve as binding sites for SH3 domain-containing proteins. Antón and colleagues identified that WIP binds to the adaptor protein Nck through its second SH3 domain, with the binding site localized to amino acids 321-415 of WIP [anton-1998-wip-nck-abstract]. This region is distinct from the WASP-binding site, allowing WIP to simultaneously engage both partners and potentially recruit Nck to sites of actin polymerization via the WASP-WIP complex.

The C-terminal domain (approximately residues 416-503) mediates the critical interaction with WASP/N-WASP. NMR structural analysis of the N-WASP EVH1 domain-WIP complex revealed a novel recognition mechanism whereby a 25-residue WIP motif wraps around the EVH1 domain, contacting a narrow but extended surface [volkman-2002-evh1-wip-structure-abstract]. Zettl and Way further characterized the binding motif, identifying the sequence ESRFYFHPISD as the core WH1 binding motif in WIP, with the two conserved phenylalanine residues being critical for the interaction [zettl-2002-wh1-evh1-abstract]. The C-terminal domain of WIP also contains transient secondary structure, including propensity for helical conformation in residues 446-456 and an extended conformation followed by a short helix in residues 468-478 [haba-2013-abstract].

## Molecular Function: WASP Stabilization and Regulation

The primary molecular function of WIP is its role as a chaperone and stabilizer of WASP. Studies by Konno and colleagues definitively demonstrated that WASP expression depends on WIP co-expression; WASP gene transfer results in high WASP expression only when WIP is concomitantly present, and WIP-knockdown T cells show concordant reduction of WASP levels [konno-2007-wasp-wip-expression-abstract]. This stabilization function is essential because, in the absence of WIP, WASP is susceptible to degradation by both calpain-mediated proteolysis and the ubiquitin-proteasome pathway.

The relationship between WIP and WASP is complex and bidirectional. Using triple-color FRET technology, Fried and colleagues demonstrated that WIP and WASP interact through two distinct molecular interfaces [fried-2014-fret-wip-wasp-abstract]. The first interaction occurs between the WASP WH1 domain and the C-terminal domain of WIP, and this interaction depends on the phosphorylation status of WIP, which is phosphorylated by PKC-theta in response to T cell receptor activation. The second interaction occurs between the VCA domain of WASP and the N-terminal domain of WIP, and this interaction requires actin as it is inhibited by latrunculin A.

Importantly, WASP activation involves dissociation of the first (WH1-CTD) interaction while leaving the second (VCA-NTD) interaction intact. This conformational change exposes the ubiquitylation site on WASP, leading to its degradation [fried-2014-fret-wip-wasp-abstract]. This mechanism suggests that the activation and degradation of WASP are delicately balanced and depend on the phosphorylation state of WIP, providing an elegant regulatory mechanism for controlling the duration and intensity of WASP signaling.

Contrary to earlier models suggesting that WIP-WASP dissociation was required for WASP activation, Dong and colleagues demonstrated that the WIP-WASP complex mediates TCR-induced NFAT activation without dissociation [dong-2007-wip-wasp-nfat-abstract]. Their structure-function analysis revealed that the N-terminal region of WIP is highly inhibitory for TCR-mediated transcriptional activation, suggesting that WIP, like WASP, is subject to autoinhibition.

## Role in Actin Cytoskeleton Dynamics

WIP functions as a critical regulator of actin polymerization and cytoskeletal remodeling. In the original characterization of WIP, Ramesh and colleagues showed that expression of WIP in human B cells increased polymerized actin content and induced the appearance of actin-containing cerebriform projections on the cell surface [ramesh-1997-wip-discovery-abstract]. This effect required the N-terminal actin-binding motif, as truncation mutants lacking this region failed to induce actin polymerization.

The mechanism by which WIP regulates actin dynamics involves both WASP-dependent and WASP-independent pathways. WIP facilitates the localization of WASP to sites of actin polymerization, serving as a shuttle that brings WASP to areas of active cytoskeletal reorganization [anton-2007-wip-review-abstract]. In Dictyostelium studies, Myers and colleagues demonstrated that WIP (designated WIPa) localizes to sites of new pseudopod protrusion, colocalizes with WASP at the leading edge, and increases F-actin elongation in vivo in a WASP-dependent manner [myers-2006-abstract].

Studies in yeast have provided fundamental insights into WIP/verprolin function. Vaduva and colleagues showed that human WIP can functionally replace yeast verprolin, suppressing the growth defects of VRP1 mutations and restoring cytoskeletal organization and endocytosis [vaduva-1999-wip-yeast-abstract]. This complementation depends on both the WH2 actin-binding domain and a putative profilin-binding domain, highlighting the conservation of WIP function across evolution.

## Subcellular Localization and Actin-Rich Structures

WIP localizes to multiple actin-rich structures within cells, reflecting its role in diverse actin-dependent processes. These structures include the immune synapse, filopodia, lamellipodia, stress fibers, podosomes, and invadopodia [anton-2007-wip-review-abstract].

In dendritic cells, Chou and colleagues demonstrated that WIP is essential for podosome formation and architecture [chou-2006-wip-podosomes-abstract]. Podosomes are actin-rich adhesive structures that mediate cell-matrix interactions and local matrix degradation in migrating cells. WIP is required for the formation of actin cores containing WASP and cortactin and for the organization of integrin and integrin-associated proteins in circular arrays, which are specific characteristics of podosome structure. WIP exerts these functions by regulating calpain-mediated cleavage of WASP and by facilitating the localization of WASP to sites of actin polymerization at podosomes.

In cancer cells, WIP has been shown to localize to invadopodia, which are actin-rich membrane protrusions that mediate matrix degradation during tumor invasion. García and colleagues demonstrated that WIP interacts with N-WASP and cortactin and is essential for invadopodium assembly in breast cancer cells [garcia-2016-wip-invadopodia-abstract]. Their work established that WIP functions as a hub for signaling molecule recruitment during invadopodium generation and cancer progression.

## Role in T Cell Signaling and Immune Function

WIP plays critical roles in T cell receptor signaling and immune function. The protein is essential for proper T cell activation, chemotaxis, and responsiveness to cytokines. Studies using WIP-deficient mice have revealed both WASP-dependent and WASP-independent roles for WIP in immune cell function.

Janssen and colleagues identified a DOCK8-WIP-WASP complex that links T cell receptors to the actin cytoskeleton [janssen-2016-dock8-wip-wasp-abstract]. WIP bridges DOCK8 (dedicator of cytokinesis 8) to WASP and actin in T cells, and DOCK8's guanine nucleotide exchange factor activity is essential for TCR-driven WASP activation, F-actin assembly, and immune synapse formation. This discovery provided an explanation for the overlapping clinical phenotypes of Wiskott-Aldrich syndrome and DOCK8 deficiency.

Le Bras and colleagues investigated the WASP-independent functions of WIP by comparing WIP/WASP double knockout mice to WASP single knockout mice [lebras-2009-wip-il2-abstract]. They found that WIP is essential for IL-2 signaling and responsiveness in T cells. Double knockout T cells had defective response to IL-2, evidenced by failure to phosphorylate STAT5 and induce expression of STAT5-dependent genes. Importantly, these T cells had a disrupted subcortical actin cytoskeleton and impaired actin polymerization after TCR ligation, suggesting that WIP's role in maintaining cytoskeletal integrity underlies its function in IL-2 signaling.

Gallego and colleagues demonstrated that WASP and WIP play complementary roles in T cell homing and chemotaxis [gallego-2005-wip-wasp-chemotaxis-abstract]. T cell homing to spleen and lymph nodes was deficient in WASP-deficient and WIP-deficient mice and severely impaired in double knockout mice. Chemotaxis to SDF-1alpha was significantly impaired in WIP-deficient T cells and severely reduced in double knockout T cells. Their findings indicate that WASP and WIP function downstream of small GTPases and play partially redundant roles in T cell chemotaxis.

In mast cells, Kettner and colleagues demonstrated that WIP regulates signaling via the high-affinity receptor for IgE (FcepsilonRI) [kettner-2004-wip-mast-cells-abstract]. WIP-deficient mast cells showed impaired degranulation, diminished calcium mobilization, and reduced phosphorylation of Syk. WIP was found to associate with Syk after FcepsilonRI ligation and to inhibit Syk degradation, revealing a novel mechanism by which WIP regulates immune receptor signaling.

## Role in NK Cell Cytotoxicity

WIP plays an essential role in natural killer (NK) cell function and cytotoxic activity. Krzewski and colleagues identified a multiprotein complex of approximately 1.3 megadaltons consisting of WIP, WASP, actin, and myosin IIA that forms during NK cell activation [krzewski-2006-nk-cell-multiprotein-abstract]. This complex is critical for the cytoskeletal rearrangements required for NK cell-mediated cytolysis.

The assembly of this multiprotein complex is dynamically regulated. WIP and WASP form a constitutive core complex, while actin and myosin IIA are recruited upon NK cell activation. Importantly, inhibitory signaling through killer cell immunoglobulin-like receptors (KIRs) dramatically decreases the recruitment of actin and myosin IIA to the WIP-WASP complex, providing a mechanism by which inhibitory receptors can prevent cytotoxic function [krzewski-2006-nk-cell-multiprotein-abstract]. Notably, actin and myosin IIA can be recruited to WIP even in the absence of WASP, and this recruitment correlates with WIP phosphorylation mediated by PKC-theta.

Further studies demonstrated that WIP is essential for lytic granule polarization and exocytosis in NK cells [krzewski-2008-nk-cell-cytotoxicity-abstract]. Disruption of WIP expression by RNA interference led to almost complete inhibition of cytotoxic activity, establishing WIP as a central regulator of NK cell effector function. The WIP-dependent complex is required for the proper positioning of lytic granules at the immunological synapse, a critical step in target cell killing.

These findings have clinical relevance for Wiskott-Aldrich syndrome, where NK cell dysfunction contributes to increased susceptibility to infections and malignancies. The essential role of WIP in forming the cytoskeletal scaffold required for effective cytotoxicity explains why WIP deficiency results in impaired NK cell function.

## Role in Phagocytosis and Macrophage Function

WIP is essential for phagocytosis and macrophage migration, two processes that are critically impaired in Wiskott-Aldrich syndrome. Tsuboi and Meerloo demonstrated that WASP and WIP form a complex at the phagocytic cup, the actin-based membrane structure that macrophages form to engulf foreign particles [tsuboi-2007-phagocytic-cup-abstract]. The WASP-WIP complex is essential for efficient phagocytic cup formation, with WASP phosphorylation on tyrosine 291 playing an important regulatory role. These findings explain the phagocytic defects and recurrent infections observed in WAS patients.

The role of WIP in macrophage chemotaxis was characterized by Tsuboi, who demonstrated that WASP and the mammalian verprolins (WIP, WICH/WIRE) form functional complexes essential for monocyte migration [tsuboi-2006-monocyte-chemotaxis-abstract]. Both WIP and WICH/WIRE are expressed in monocytes and are involved in chemotaxis. When WASP binding to verprolins was blocked, chemotactic migration was impaired in both cell lines and primary human monocytes. Importantly, blocking WASP-verprolin interaction impaired cell polarization but not actin polymerization, indicating that the complex is specifically required for directional migration rather than general cytoskeletal function.

Tsuboi and colleagues further identified formin-binding protein 17 (FBP17) as a critical upstream regulator that recruits WASP, WIP, and dynamin-2 to the plasma membrane [tsuboi-2009-fbp17-abstract]. This recruitment is necessary for the formation of both podosomes and phagocytic cups, representing a common molecular step in these actin-based membrane structures. FBP17 facilitates the simultaneous occurrence of membrane deformation (through its F-BAR domain) and actin polymerization (through WASP-WIP recruitment) at the same membrane sites.

These studies establish that WIP functions in macrophages as part of an integrated system linking membrane dynamics to actin polymerization, enabling the coordinated formation of specialized membrane structures required for immune function.

## Additional Protein Interactions: Src Family Kinases

WIP interacts with additional signaling molecules beyond WASP and its core partners. Scott and colleagues used mass spectrometry to identify binding partners for the SH3 domain of Hck, a Src family kinase, and found WIP and WASP among the major interacting proteins in monocytes [scott-2002-hck-wip-abstract]. Using purified proteins, they confirmed that WIP interacts directly with the SH3 domain of Hck. This interaction links WIP to Src family kinase signaling pathways and suggests that WIP may serve as a substrate or regulatory partner for these kinases. The interaction with Hck provides an additional mechanism by which WIP can integrate diverse signaling inputs to regulate actin cytoskeleton dynamics.

## Role in Disease: Immunodeficiency and Cancer

Mutations in WIPF1 cause a severe combined immunodeficiency syndrome that resembles Wiskott-Aldrich syndrome. WIP deficiency leads to severe early-onset immunodeficiency in humans and severe autoimmunity and shortened lifespan in mice [alonso-eiras-2024-wip-cancer-abstract]. The clinical phenotype includes features common to WAS, such as thrombocytopenia, recurrent infections, and immunodysregulation, reflecting the essential role of the WIP-WASP complex in hematopoietic cell function [schwinger-2018-abstract].

The importance of WIP in WAS pathology is highlighted by the observation that approximately 80% of identified WAS patients have mutations in the WIP-binding region of WASP, underscoring the clinical significance of the WIP-WASP interaction [chou-2006-wip-podosomes-abstract]. Stewart and colleagues demonstrated that point mutations causing WAS can impair the interaction between WASP and WIP, providing a mechanistic link between disrupted protein interactions and disease [stewart-1999-abstract].

Beyond immunodeficiency, WIP has been implicated in cancer progression. The relationship between WIP and cancer is complex and context-dependent. In solid tumors, overexpression of WIP has been associated with tumor initiation, progression, and dissemination through matrix degradation by invadopodia [alonso-eiras-2024-wip-cancer-abstract]. García and colleagues demonstrated that WIP is necessary for matrix invasion by breast cancer cells and that elevated WIP levels correlate with high invasiveness [garcia-2016-wip-invadopodia-abstract, garcia-2014-abstract].

However, a suppressive function for WIP has been shown in certain hematological cancers. Wang and colleagues identified FLI1 as a direct transcriptional regulator of WIP and showed that depletion of WIP accelerated cell proliferation in leukemia cells, suggesting a tumor suppressor function in this context [wang-2021-abstract]. These data highlight the need for further research to fully understand WIP's diverse functions in different cancer contexts.

## Protein-Protein Interactions

WIP serves as a hub for multiple protein-protein interactions, facilitated by its extensive proline-rich sequences and multiple functional domains. Beyond WASP, WIP interacts with numerous signaling proteins including:

**Nck adaptor proteins:** WIP binds Nck through its second SH3 domain, linking WIP to receptor tyrosine kinase signaling pathways. The presence of profilin in Nck precipitates suggests that Nck may couple extracellular signals to the cytoskeleton via its interaction with WIP and profilin [anton-1998-wip-nck-abstract].

**Cortactin:** WIP interacts with cortactin, a protein that stabilizes branched actin networks. This interaction is important for invadopodium formation and function [garcia-2016-wip-invadopodia-abstract].

**Profilin:** WIP contains profilin-binding motifs that link it to actin dynamics, as profilin is a key regulator of actin polymerization [ramesh-1997-wip-discovery-abstract].

**Syk kinase:** In mast cells, WIP associates with Syk following FcepsilonRI ligation and protects Syk from degradation [kettner-2004-wip-mast-cells-abstract].

**DOCK8:** WIP bridges DOCK8 to WASP, forming a complex essential for TCR-driven actin assembly [janssen-2016-dock8-wip-wasp-abstract].

**Myosin IIA:** In NK cells, myosin IIA is recruited to the WIP-WASP complex upon activation. This recruitment is mediated by WIP phosphorylation and is essential for cytotoxic function [krzewski-2006-nk-cell-multiprotein-abstract].

**FBP17 (Formin-binding protein 17):** FBP17 recruits WIP, WASP, and dynamin-2 to the plasma membrane during podosome and phagocytic cup formation [tsuboi-2009-fbp17-abstract].

**Hck kinase:** WIP interacts directly with the SH3 domain of Hck, linking WIP to Src family kinase signaling in monocytes [scott-2002-hck-wip-abstract].

**Dynamin-2:** WIP is recruited together with dynamin-2 by FBP17 to sites of membrane remodeling, connecting WIP to membrane fission machinery [tsuboi-2009-fbp17-abstract].

## Evolutionary Conservation and the Verprolin Family

WIP belongs to the verprolin family of proteins, which is evolutionarily conserved from yeast to humans. The yeast ortholog, verprolin (Vrp1p), is an actin- and myosin-interacting protein required for polarized morphogenesis, endocytosis, and cytokinesis [munn-2009-verprolin-review-abstract]. Human WIP can functionally replace verprolin in yeast, demonstrating conservation of function across evolution [vaduva-1999-wip-yeast-abstract].

In mammals, the verprolin family includes three members: WIP (WIPF1), WICH (also known as WIRE; WIPF2), and CR16 (WIPF3). These proteins share conserved actin-binding and WASP-binding domains but have distinct tissue expression patterns and functions. WICH/WIRE interacts preferentially with N-WASP and plays distinct roles in invadopodium maturation compared to WIP [garcia-2016-wip-invadopodia-abstract, kato-2002-abstract].

## Open Questions

Several important questions remain regarding WIP function:

1. **Regulation of WIP activity:** While the regulation of WASP by WIP is well characterized, less is known about how WIP itself is regulated. The autoinhibitory properties of the WIP N-terminus suggest regulatory mechanisms that remain to be fully elucidated.

2. **WASP-independent functions:** Many studies have focused on WIP's role as a WASP regulator, but WIP clearly has WASP-independent functions. The full scope of these functions and their mechanisms require further investigation.

3. **Tissue-specific roles:** WIP is expressed in multiple tissues, but most studies have focused on hematopoietic cells. The functions of WIP in other cell types, including neurons and epithelial cells, are less well understood.

4. **Cancer context dependency:** The opposing roles of WIP in solid tumors versus hematological malignancies require explanation. Understanding the molecular basis for these context-dependent functions could have therapeutic implications.

5. **Structural dynamics:** As an intrinsically disordered protein, WIP likely undergoes conformational changes upon binding partners. High-resolution structural studies of WIP in complex with its various partners would provide mechanistic insights.

6. **Therapeutic potential:** Given WIP's role in cancer invasion and immune dysfunction, understanding whether WIP can be targeted therapeutically is of significant interest.

## References

- **ramesh-1997-wip-discovery-abstract**: Ramesh N, Antón IM, Hartwig JH, Geha RS. WIP, a protein associated with Wiskott-Aldrich syndrome protein, induces actin polymerization and redistribution in lymphoid cells. Proc Natl Acad Sci U S A. 1997;94(26):14671-6. DOI: https://doi.org/10.1073/pnas.94.26.14671 PMID: 9405671

- **anton-2007-wip-review-abstract**: Antón IM, Jones GE, Wandosell F, Geha R, Ramesh N. WASP-interacting protein (WIP): working in polymerisation and much more. Trends Cell Biol. 2007;17(11):555-62. DOI: https://doi.org/10.1016/j.tcb.2007.08.005 PMID: 17949983

- **sokolik-2020-wip-structure-abstract**: Sokolik CG, Qassem N, Chill JH. The Disordered Cellular Multi-Tasker WIP and Its Protein-Protein Interactions: A Structural View. Biomolecules. 2020;10(7):1084. DOI: https://doi.org/10.3390/biom10071084 PMID: 32708183

- **munn-2009-verprolin-review-abstract**: Munn AL, Thanabalu T. Verprolin: a cool set of actin-binding sites and some very HOT prolines. IUBMB Life. 2009;61(7):707-12. DOI: https://doi.org/10.1002/iub.195 PMID: 19507265

- **volkman-2002-evh1-wip-structure-abstract**: Volkman BF, Prehoda KE, Scott JA, Peterson FC, Lim WA. Structure of the N-WASP EVH1 domain-WIP complex: insight into the molecular basis of Wiskott-Aldrich Syndrome. Cell. 2002;111(4):565-76. DOI: https://doi.org/10.1016/s0092-8674(02)01076-0 PMID: 12437929

- **zettl-2002-wh1-evh1-abstract**: Zettl M, Way M. The WH1 and EVH1 domains of WASP and Ena/VASP family members bind distinct sequence motifs. Curr Biol. 2002;12(18):1617-22. DOI: https://doi.org/10.1016/s0960-9822(02)01112-0 PMID: 12372256

- **konno-2007-wasp-wip-expression-abstract**: Konno A, Kirby M, Anderson SA, Schwartzberg PL, Candotti F. The expression of WASP is dependent on WIP. Int Immunol. 2007;19(2):185-92. DOI: https://doi.org/10.1093/intimm/dxl135 PMID: 17205972

- **fried-2014-fret-wip-wasp-abstract**: Fried S, Reicher B, Pauker MH, et al. Triple-color FRET analysis reveals conformational changes in the WIP-WASp actin-regulating complex. Sci Signal. 2014;7(331):ra60. DOI: https://doi.org/10.1126/scisignal.2005198 PMID: 24962707

- **dong-2007-wip-wasp-nfat-abstract**: Dong X, Patino-Lopez G, Candotti F, Shaw S. Structure-function analysis of the WIP role in TCR-stimulated NFAT activation. J Biol Chem. 2007;282(41):30303-10. DOI: https://doi.org/10.1074/jbc.M704972200 PMID: 17711847

- **janssen-2016-dock8-wip-wasp-abstract**: Janssen E, Tohme M, Hedayat M, et al. A DOCK8-WIP-WASp complex links T cell receptors to the actin cytoskeleton. J Clin Invest. 2016;126(10):3837-3851. DOI: https://doi.org/10.1172/JCI85774 PMID: 27599296

- **lebras-2009-wip-il2-abstract**: Le Bras S, Massaad M, Koduru S, Kumar L, Oyoshi MK, Hartwig J, Geha RS. WIP is critical for T cell responsiveness to IL-2. Proc Natl Acad Sci U S A. 2009;106(18):7519-24. DOI: https://doi.org/10.1073/pnas.0806410106 PMID: 19359486

- **gallego-2005-wip-wasp-chemotaxis-abstract**: Gallego MD, de la Fuente MA, Anton IM, Snapper S, Fuhlbrigge R, Geha RS. WIP and WASP play complementary roles in T cell homing and chemotaxis to SDF-1alpha. Int Immunol. 2005;18(2):221-32. DOI: https://doi.org/10.1093/intimm/dxh310 PMID: 16141245

- **kettner-2004-wip-mast-cells-abstract**: Kettner A, Kumar L, Antón IM, et al. WIP regulates signaling via the high affinity receptor for immunoglobulin E in mast cells. J Exp Med. 2004;199(3):357-68. DOI: https://doi.org/10.1084/jem.20030652 PMID: 14757742

- **vaduva-1999-wip-yeast-abstract**: Vaduva G, Martinez-Quiles N, Anton IM, et al. The human WASP-interacting protein, WIP, activates the cell polarity pathway in yeast. J Biol Chem. 1999;274(24):17103-8. DOI: https://doi.org/10.1074/jbc.274.24.17103 PMID: 10358064

- **chou-2006-wip-podosomes-abstract**: Chou HC, Antón IM, Holt MR, et al. WIP regulates the stability and localization of WASP to podosomes in migrating dendritic cells. Curr Biol. 2006;16(23):2337-44. DOI: https://doi.org/10.1016/j.cub.2006.10.037 PMID: 17141616

- **garcia-2016-wip-invadopodia-abstract**: García E, Ragazzini C, Yu X, et al. WIP and WICH/WIRE co-ordinately control invadopodium formation and maturation in human breast cancer cell invasion. Sci Rep. 2016;6:23590. DOI: https://doi.org/10.1038/srep23590 PMID: 27009365

- **alonso-eiras-2024-wip-cancer-abstract**: Alonso-Eiras J, Anton IM. Multifaceted role of the actin-binding protein WIP: Promotor and inhibitor of tumor progression and dissemination. Cytoskeleton (Hoboken). 2024;82(3):186-196. DOI: https://doi.org/10.1002/cm.21935 PMID: 39329352

- **paunola-2002-wh2-review-abstract**: Paunola E, Mattila PK, Lappalainen P. WH2 domain: a small, versatile adapter for actin monomers. FEBS Lett. 2002;513(1):92-7. DOI: https://doi.org/10.1016/s0014-5793(01)03242-2 PMID: 11911886

- **anton-1998-wip-nck-abstract**: Antón IM, Lu W, Mayer BJ, Ramesh N, Geha RS. The WIP binds to the adaptor protein Nck. J Biol Chem. 1998;273(33):20992-5. DOI: https://doi.org/10.1074/jbc.273.33.20992 PMID: 9694849

- **noy-2012-wip-review-abstract**: Noy E, Fried S, Matalon O, Barda-Saad M. WIP remodeling actin behind the scenes: how WIP reshapes immune and other functions. Int J Mol Sci. 2012;13(6):7629-7647. DOI: https://doi.org/10.3390/ijms13067629 PMID: 22837718

- **garcia-2014-abstract**: García E, Machesky LM, Jones GE, Antón IM. WIP is necessary for matrix invasion by breast cancer cells. Eur J Cell Biol. 2014;93(10-12):413-23. DOI: https://doi.org/10.1016/j.ejcb.2014.07.008 PMID: 25169059

- **ramesh-2009-wasp-wip-advances-abstract**: Ramesh N, Geha R. Recent advances in the biology of WASP and WIP. Immunol Res. 2009;44(1-3):99-111. DOI: https://doi.org/10.1007/s12026-008-8086-1 PMID: 19018480

- **schwinger-2018-abstract**: Schwinger W, Urban C, Ulreich R, et al. The Phenotype and Treatment of WIP Deficiency: Literature Synopsis and Review of a Patient. Front Immunol. 2018;9:2554. DOI: https://doi.org/10.3389/fimmu.2018.02554 PMID: 30450104

- **wang-2021-abstract**: Wang C, Sample KM, Gajendran B, et al. FLI1 Induces Megakaryopoiesis Gene Expression Through WAS/WIP-Dependent and Independent Mechanisms. Front Immunol. 2021;12:607836. DOI: https://doi.org/10.3389/fimmu.2021.607836 PMID: 33717090

- **stewart-1999-abstract**: Stewart DM, Tian L, Nelson DL. Mutations that cause the Wiskott-Aldrich syndrome impair the interaction of WASP with WIP. J Immunol. 1999;162(8):5019-24. PMID: 10202051

- **haba-2013-abstract**: Haba NY, Gross R, Novacek J, et al. NMR determines transient structure and dynamics in the disordered C-terminal domain of WIP. Biophys J. 2013;105(2):481-93. DOI: https://doi.org/10.1016/j.bpj.2013.05.046 PMID: 23870269

- **elazari-shalom-2015-abstract**: Elazari-Shalom H, Shaked H, Esteban-Martin S, Salvatella X, Barda-Saad M, Chill JH. New insights into the role of the disordered WIP N-terminal domain. FEBS J. 2015;282(4):700-14. DOI: https://doi.org/10.1111/febs.13174 PMID: 25495558

- **myers-2006-abstract**: Myers SA, Leeper LR, Chung CY. WASP-interacting protein is important for actin filament elongation and prompt pseudopod formation in response to a dynamic chemoattractant gradient. Mol Biol Cell. 2006;17(10):4564-75. DOI: https://doi.org/10.1091/mbc.e05-10-0994 PMID: 16899512

- **kato-2002-abstract**: Kato M, Miki H, Kurita S, et al. WICH, a novel verprolin homology domain-containing protein that functions cooperatively with N-WASP in actin-microspike formation. Biochem Biophys Res Commun. 2002;291(1):41-7. DOI: https://doi.org/10.1006/bbrc.2002.6406 PMID: 11829459

- **krzewski-2006-nk-cell-multiprotein-abstract**: Krzewski K, Chen X, Orange JS, Strominger JL. Formation of a WIP-, WASp-, actin-, and myosin IIA-containing multiprotein complex in activated NK cells and its alteration by KIR inhibitory signaling. J Cell Biol. 2006;173(1):121-32. DOI: https://doi.org/10.1083/jcb.200509076 PMID: 16606694

- **krzewski-2008-nk-cell-cytotoxicity-abstract**: Krzewski K, Chen X, Bhardwaj N, et al. WIP is essential for lytic granule polarization and NK cell cytotoxicity. J Immunol. 2008;180(12):8312-9. DOI: https://doi.org/10.4049/jimmunol.180.12.8312 PMID: 18523299

- **tsuboi-2006-monocyte-chemotaxis-abstract**: Tsuboi S. A complex of Wiskott-Aldrich syndrome protein with mammalian verprolins plays an important role in monocyte chemotaxis. J Immunol. 2006;176(11):6576-85. DOI: https://doi.org/10.4049/jimmunol.176.11.6576 PMID: 16709815

- **tsuboi-2007-phagocytic-cup-abstract**: Tsuboi S, Meerloo J. Wiskott-Aldrich syndrome protein is a key regulator of the phagocytic cup formation in macrophages. J Biol Chem. 2007;282(47):34194-203. DOI: https://doi.org/10.1074/jbc.M705999200 PMID: 17890224

- **tsuboi-2009-fbp17-abstract**: Tsuboi S, Takada H, Hara T, et al. FBP17 Mediates a Common Molecular Step in the Formation of Podosomes and Phagocytic Cups in Macrophages. J Biol Chem. 2009;284(13):8548-56. DOI: https://doi.org/10.1074/jbc.M805638200 PMID: 19155218

- **scott-2002-hck-wip-abstract**: Scott MP, Zappacosta F, Kim EY, Annan RS, Miller WT. Identification of novel SH3 domain ligands for the Src family kinase Hck. J Biol Chem. 2002;277(31):28238-46. DOI: https://doi.org/10.1074/jbc.M202783200 PMID: 12029088


## Citations

1. alonso-eiras-2024-wip-cancer-abstract.md
2. anton-1998-wip-nck-abstract.md
3. anton-2007-wip-review-abstract.md
4. chou-2006-wip-podosomes-abstract.md
5. dong-2007-wip-wasp-nfat-abstract.md
6. fried-2014-fret-wip-wasp-abstract.md
7. gallego-2005-wip-wasp-chemotaxis-abstract.md
8. garcia-2016-wip-invadopodia-abstract.md
9. janssen-2016-dock8-wip-wasp-abstract.md
10. kettner-2004-wip-mast-cells-abstract.md
11. konno-2007-wasp-wip-expression-abstract.md
12. krzewski-2006-nk-cell-multiprotein-abstract.md
13. krzewski-2008-nk-cell-cytotoxicity-abstract.md
14. lebras-2009-wip-il2-abstract.md
15. munn-2009-verprolin-review-abstract.md
16. noy-2012-wip-review-abstract.md
17. paunola-2002-wh2-review-abstract.md
18. ramesh-1997-wip-discovery-abstract.md
19. ramesh-2009-wasp-wip-advances-abstract.md
20. schwinger-2018-wip-deficiency-abstract.md
21. scott-2002-hck-wip-abstract.md
22. sokolik-2020-wip-structure-abstract.md
23. stewart-1999-wasp-wip-mutations-abstract.md
24. tsuboi-2006-monocyte-chemotaxis-abstract.md
25. tsuboi-2007-phagocytic-cup-abstract.md
26. tsuboi-2009-fbp17-abstract.md
27. vaduva-1999-wip-yeast-abstract.md
28. volkman-2002-evh1-wip-structure-abstract.md
29. zettl-2002-wh1-evh1-abstract.md