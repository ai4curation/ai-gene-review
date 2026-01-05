---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2025-12-27T16:20:38.820838'
end_time: '2025-12-27T16:22:41.082930'
duration_seconds: 122.26
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: AFAP1L1
  gene_symbol: AFAP1L1
  uniprot_accession: Q8TED9
  protein_description: 'RecName: Full=Actin filament-associated protein 1-like 1;
    Short=AFAP1-like protein 1;'
  gene_info: Name=AFAP1L1;
  organism_full: Homo sapiens (Human).
  protein_family: Not specified in UniProt
  protein_domains: AFAP. (IPR030113); PH-like_dom_sf. (IPR011993); PH_domain. (IPR001849);
    PH (PF00169)
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 36
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q8TED9
- **Protein Description:** RecName: Full=Actin filament-associated protein 1-like 1; Short=AFAP1-like protein 1;
- **Gene Information:** Name=AFAP1L1;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** AFAP. (IPR030113); PH-like_dom_sf. (IPR011993); PH_domain. (IPR001849); PH (PF00169)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "AFAP1L1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'AFAP1L1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **AFAP1L1** (gene ID: AFAP1L1, UniProt: Q8TED9) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

<think>
The user is asking me to write a comprehensive research report on the gene AFAP1L1 (UniProt: Q8TED9) in humans. They've provided extensive search results and specific instructions about how to structure the report. Let me verify the information first:

1. Check if gene symbol matches protein description:
   - UniProt says: "Actin filament-associated protein 1-like 1; AFAP1-like protein 1"
   - Gene name: AFAP1L1
   - This matches correctly

2. Verify organism:
   - UniProt says: Homo sapiens (Human)
   - This is correct

3. Protein family/domains:
   - AFAP domain (IPR030113)
   - PH-like domain (IPR011993)
   - PH domain (IPR001849)
   - PH domain (PF00169)
   - The search results confirm AFAP family membership and PH domains

The search results are extensive and directly relevant to AFAP1L1 in human. I have good quality literature including:
- 2014 study on AFAP1L1 in colorectal cancer (Takahashi et al.)
- 2011 study on AFAP1L1 as an adaptor protein (Snyder et al.)
- 2023 study on AFAP1L1 in gastric cancer (Sun et al.)
- Multiple studies on transcriptional regulation, protein interactions, disease associations

Now I need to plan my report structure:

Main themes to investigate:
1. Molecular structure and domain architecture
2. Protein interactions and binding partners
3. Cellular localization and subcellular structures
4. Primary biochemical and cellular functions
5. Role in cancer and disease
6. Transcriptional regulation
7. Evolutionary and comparative aspects
8. Therapeutic potential

I should write at least 10,000 words, organize by major themes with subsections, use narrative flow (no lists), cite thoroughly, and focus on functional aspects as requested.


I'll organize the report with an opening section establishing the protein's significance, followed by detailed exploration of its molecular architecture and structural features. Then I'll move through protein interaction networks and cellular localization patterns, particularly focusing on invadopodial and podosomal structures. The functional analysis will examine both normal cellular roles and pathological involvement in cancer, with dedicated sections on signaling cascades and transcriptional control mechanisms. I'll conclude with therapeutic implications and future research directions. This structure should provide comprehensive coverage while maintaining narrative coherence throughout the 10,000+ word target.
</think>

# AFAP1L1 (Actin Filament-Associated Protein 1-Like 1): Molecular Structure, Function, and Role in Cancer Progression

## Overview and Key Findings

**AFAP1L1** (actin filament-associated protein 1-like 1) is a multidomain adaptor protein encoded by the *AFAP1L1* gene on human chromosome 5q33.1[1], which encodes a protein of 768 amino acids with a molecular weight of approximately 115 kilodaltons[14][20]. This protein represents a member of the AFAP family of adaptor proteins, which also includes AFAP1 (also known as AFAP-110) and AFAP1L2 (also known as XB130)[14][20][42]. The AFAP1L1 protein has emerged in recent years as a significant prognostic marker and driver of cancer cell invasion, metastasis, and epithelial-to-mesenchymal transition across multiple malignancies, particularly colorectal cancer, gastric cancer, and sarcomas[7][10][12][21]. Unlike its family member AFAP1, which primarily binds to c-Src through its SH3 binding motif, AFAP1L1 exhibits a unique functional specialization through its preferential interaction with the adaptor protein cortactin rather than c-Src[13][14][20], enabling distinct roles in the formation and regulation of invadopodia—specialized cellular structures involved in extracellular matrix degradation and invasion[8][14]. The protein's ability to modulate actin cytoskeleton dynamics, control cell morphology transitions from mesenchymal to amoeboid states, and promote anoikis resistance positions it as a critical node in cancer cell progression and a promising therapeutic target[7][10][21].

## Molecular Architecture and Domain Structure

### Overall Protein Structure and Family Classification

AFAP1L1 belongs to the AFAP family of adaptor proteins, classified together by the Human Genome Project based on their shared modular domain structure and amino acid sequence conservation[14][20][42]. The AFAP family comprises three members—AFAP1, AFAP1L1, and AFAP1L2/XB130—that collectively share sequence similarities of approximately 44 to 71 percent identity depending on the specific domain analyzed[14][20]. The *afap1l1* gene is located on chromosome 5q33.1 and consists of 19 exons that encode 768 amino acids in the open reading frame, resulting in a protein with a predicted molecular weight of approximately 115 kilodaltons[14][20]. This multi-exon structure suggests complex post-transcriptional regulation, which has been observed in various cell types and cancer contexts[31][56].

Comparative structural analysis reveals that AFAP1L1 shares 44% identity and 71% amino acid similarity with AFAP1[14]. However, despite these overall similarities, there are critical differences in functional domains that distinguish AFAP1L1 from its family members, particularly regarding which protein binding partners it engages with and which cellular compartments it localizes to[14][20][42]. These structural distinctions have profound implications for the protein's biological roles, as they determine its integration into specific cellular signaling networks and its involvement in particular cellular processes.

### Characteristic Domains and Motifs

All AFAP family members, including AFAP1L1, contain at least one predicted N-terminal SH3 binding motif, at least one predicted N-terminal SH2 binding motif, two pleckstrin homology (PH) domains separated by a region rich in serine and threonine residues (termed the substrate domain, SD), and a C-terminal SH2 binding motif[14][20][42]. The PH domains are particularly highly conserved across the AFAP family, suggesting that they perform fundamental functions shared among family members[42][53]. PH domains are approximately 120 amino acids in length and form characteristic three-dimensional structures consisting of two perpendicular anti-parallel beta sheets followed by a C-terminal amphipathic helix[53]. While many PH domains bind to phosphatidylinositol lipids within biological membranes, including phosphatidylinositol (3,4,5)-trisphosphate and phosphatidylinositol (4,5)-bisphosphate, many PH domains in proteins like AFAP1L1 have limited direct lipid binding capacity and instead function as protein binding modules[53].

However, AFAP1L1 exhibits critical differences in its SH3 binding motif compared to AFAP1, which profoundly influences its binding selectivity[14][20]. Whereas AFAP1 contains two juxtaposed SH3 binding motifs beginning at amino acids 65 and 76 (PPQMPLPEIP and PPDSGPPPLP), AFAP1L1 contains only one predicted SH3 binding motif, DLPPPLPNKP[14][20]. This single SH3 binding motif in AFAP1L1 does not conform to the consensus c-Src SH3 binding motif but rather more closely resembles the binding site for the cortactin SH3 domain, which preferentially binds a +PPΨPXKPXWL motif where + represents a basic residue, Ψ represents an aliphatic residue, and X represents any amino acid[14][20]. This structural difference is functionally significant, as it renders AFAP1L1 capable of efficiently interacting with cortactin through its SH3 domain while being less efficient at binding to c-Src, in stark contrast to AFAP1's preferential c-Src binding[14][20][25].

Regarding tyrosine phosphorylation sites, AFAP1L1 shares 100 percent sequence identity with both AFAP1 and AFAP1L2/XB130 in its predicted N-terminal SH2 binding motif, YYEEA, and is highly similar in its C-terminal SH2 binding motif YDYV[32]. These sequences likely represent potential sites for tyrosine phosphorylation, which could enable the protein to serve as a phosphotyrosine-dependent recruiter of other signaling proteins containing SH2 domains. The serine and threonine-rich sequences flanking the PH domains in AFAP1L1 represent predicted sites for serine/threonine phosphorylation, similar to AFAP1 where serine 277 is a known target of phosphorylation by the protein kinase PKCα, which plays a role in the protein's ability to regulate podosome formation and lifespan[32]. While AFAP1L1 contains similar serine and threonine residues in the sequence flanked by its PH domains, including what may be a PKCα phosphorylation site similar to that of AFAP1, these sequences have not yet been confirmed to be phosphorylated by serine/threonine protein kinases[32].

### Actin-Binding Domain and Leucine Zipper Motif

AFAP1L1 possesses a putative actin binding domain at its carboxy terminus that is structurally similar to the known actin filament binding domain found in AFAP1[14][20]. Like AFAP1, which is known to bind actin filaments through its carboxy terminal actin filament-binding domain and multimerize through its leucine zipper to enable actin filament cross-linking[14][20][25], AFAP1L1 contains a similar sequence that may act as a leucine zipper or coiled-coil motif directly adjacent to the actin binding domain[14][20]. The leucine zipper motif is essential for intra-molecular regulation and interaction with other AFAP1L1 molecules, enabling the protein to form higher-order oligomeric complexes[14][20]. This structural feature suggests that AFAP1L1 shares with AFAP1 the capacity to directly interact with and potentially cross-link actin filaments, though the precise mechanisms and substrate specificity may differ between family members.

## Protein Interactions and Binding Partners

### Cortactin Interaction and Recruitment

AFAP1L1 was first comprehensively characterized as a novel adaptor protein that distinctly interacts with cortactin rather than c-Src, establishing a new functional specialization within the AFAP family[8][13][14][16]. In comparative binding studies using GST fusion proteins, AFAP1L1 was shown to be more efficiently precipitated by GST-SH3-cortactin than by GST-SH3-Src, with approximately a 9-fold increase in the ratio of AFAP1L1 pulled down by GST-cortactin SH3 compared to GST control, whereas AFAP1 showed a strong interaction with the Src SH3 domain with a 14-fold increase in binding and essentially undetectable precipitation by the cortactin SH3 domain[14][20][25]. This differential binding selectivity reflects the structural differences in their SH3 binding motifs and has major consequences for the proteins' cellular roles.

By fluorescence microscopy, AFAP1L1 was demonstrated to decorate actin filaments and move to punctate actin structures while colocalizing with cortactin, consistent with localization to invadosomes—the collective term for both podosomes and invadopodia[8][14][20]. Upon overexpression in smooth muscle A7r5 cells, AFAP1L1 had the ability to induce podosome formation and move to podosomes without stimulation, indicating that AFAP1L1 expression alone is sufficient to drive invadosome assembly in certain cell types[8][14][43]. The specificity of AFAP1L1 for cortactin appears to confer upon it the ability to forge unique protein interactions that may be less efficient with AFAP1, and these interactions potentially allow AFAP1L1 to affect invadosome formation through distinct mechanisms[8][14][43].

### Vinculin Interaction and Focal Adhesion Regulation

AFAP1L1 was identified as a novel associating partner of vinculin through immunoprecipitation assays in colorectal cancer cells[7][10][21]. Vinculin is an adaptor protein that localizes to integrin-mediated cell-matrix adhesions such as focal adhesions and invadopodia[7][10][21]. Vinculin functions to stabilize focal adhesions and has been described as a suppressor of cellular migration[7][10][21]. The interaction of AFAP1L1 with vinculin is particularly interesting because it occurs in the ringed structure of invadopodia, where both proteins colocalize[7][10][21].

The ectopic overexpression of AFAP1L1 induces the detachment of vinculin from focal adhesions in both colorectal cancer RKO cells and osteosarcoma SaOS2 cells, an effect that probably reflects the disassembly of focal adhesion structures[7][21][55]. The disassembly of focal adhesions can lead to alterations in both cell shape and motility, presumably as a consequence of reduced cell-matrix contacts, and this disassembly generally coincides with the dynamic formation of podosomes and invadopodia[7][21][55]. The hypothesis has been proposed that the AFAP1L1-induced alterations in cell shape and motility are mediated through its interactions with vinculin[7][10][21]. The mechanism by which AFAP1L1 regulates the function of vinculin remains incompletely understood, but it appears to involve sequestration or competitive displacement of vinculin from its typical focal adhesion localization.

### Nck2 Interaction and Actin Nucleation

More recent evidence has demonstrated that AFAP1L1 interacts with Nck2, an adaptor protein containing three SH3 domains that link receptor tyrosine kinases to effectors modulating actin polymerization[48][49]. In sarcoma cells, Nck2 binds to phosphorylated AFAP1L1 to enhance formation of invadopodia[48]. This interaction is particularly interesting because Nck proteins link activated receptor tyrosine kinases and cytosolic substrates to the Arp2/3 complex through N-WASP or related actin nucleation-promoting factors[49]. The N-WASP–Arp2/3 complex is a major driver of branched actin polymerization and is essential for invadopodial structure formation[49]. The interaction between AFAP1L1 and Nck2 thus provides a mechanism through which AFAP1L1 can recruit actin nucleation machinery to sites of invadopodia, amplifying the local concentration of factors necessary for actin polymerization and invadopodial growth.

### Rho GTPase Pathway Interactions

Recent research has uncovered that AFAP1L1 interacts with VAV2 (VAV guanine nucleotide exchange factor 2) to activate the Rho family GTPase CDC42[12][19][36][51][57]. In gastric cancer cells, this VAV2-CDC42 axis represents a critical downstream mechanism through which AFAP1L1 promotes cancer cell progression. The interaction between AFAP1L1 and VAV2 ultimately leads to activation of CDC42, a small GTPase of the Rho subfamily, which promotes the expression and activation of integrin subunit alpha 5 (ITGA5) and subsequent integrin signaling pathway activation[12][19][36][51][57]. This VAV2-CDC42-ITGA5 signaling cascade is particularly critical for epithelial-to-mesenchymal transition (EMT) induction, a fundamental process driving cancer cell invasion and metastasis[12][19][36][51][57].

## Cellular Localization and Subcellular Structures

### Tissue Expression Patterns

AFAP1L1 is expressed in breast, colon, and brain tissues, and in all three tissues it is expressed in the microvasculature at the protein level[17][30][38]. In the breast, AFAP1L1 is found in the contractile myoepithelial cell layer which surrounds the breast ducts and in the microvasculature, localization patterns similar to but distinct from AFAP1[25][38]. In the colon, AFAP1L1 is present in the epithelial mucous membrane, including in the colonic crypts which aid in mucous production and generation of new epithelial cells for the intestinal surface[25][38].

Human brain tissue shows particularly differential expression patterns between AFAP1 and AFAP1L1[25][38]. While AFAP1 is found in the microvasculature of the brain, in the molecular layer and meningeal vessels and to a slight level around the granule cells of the granular layer, AFAP1L1 is found in low levels in the microvasculature but is distinctly localized around Purkinje neurons and the granule cells of the granular layer[25][38]. This AFAP1L1 immunolabeling is not inside the Purkinje neurons or granule cell bodies but instead extends away from the cell body[25][38]. Outside the cerebellar cortex, both AFAP1 and AFAP1L1 are found in glial cells, but they display differential expression patterns in the dentate nucleus, one of four deep cerebellar nuclei responsible for voluntary movements of the extremities[25][38]. The unique localization of AFAP1L1 in the dentate nucleus and its expression appearing to occur along neuronal processes suggests AFAP1L1 has a unique role in the innervation of this nucleus[38][42], potentially related to neuronal process dynamics or axonal guidance.

### Podosomes and Invadopodia Localization

AFAP1L1 specifically localizes to podosomes and invadopodia, which are specialized actin-rich adhesion structures formed on the ventral membrane of cells[7][10][14][21]. Podosomes are found primarily on the ventral membrane of cells and contain an F-actin-rich core[14][25][38][43]. Invadopodia, or invadosomes as they are collectively termed with podosomes, are highly dynamic protrusions at the substrate-contacting side of the cell involved in the degradation of the extracellular matrix[7][21][55]. These structures display proteolytic activity induced mainly by the recruitment of matrix metalloproteinases, especially membrane type 1 matrix metalloprotease (MT1-MMP), MMP-2, and/or MMP-9[7][21][37].

AFAP1L1 was specifically reported to be localized to the invadopodia along with cortactin in breast cancer cells[7][21][15], and this localization has been confirmed in multiple other cancer cell types[7][10][21]. In colorectal cancer cells, AFAP1L1 was clustered in the ringed structure of the invadopodia, with detailed immunofluorescence analysis revealing that AFAP1L1 aggregates at the ring-like structure and colocalizes with cortactin, which localizes to the core of the invadopodium[7][21]. The cortactin-rich core of invadopodia contains actin polymerization machinery including the Arp2/3 complex, while the ring is enriched in molecules like paxillin, which regulates adhesion dynamics[7][21].

Upon cSrc binding and activation, AFAP1 and cSrc move to these podosomes, structures which secrete proteases that enable cells to degrade the extracellular matrix, cross tissue barriers, and invade[14][25]. AFAP1L1, while not activating cSrc to the same extent as AFAP1, localizes to these structures through its cortactin interaction, serving distinct functions in invadopodial regulation and formation[8][14][20][43].

### Stress Fiber Localization

Beyond its localization to invadosomes, AFAP1L1 decorates actin stress fibers throughout the cell[8][14][20][25][38][43]. AFAP1L1 was shown by fluorescence microscopy to decorate actin filaments and move to punctate actin structures and colocalize with cortactin[8][14][20]. This broader actin cytoskeleton localization suggests that AFAP1L1 serves roles in actin filament remodeling and integrity throughout the cell, not just at invadosomal structures, though its effects on cellular morphology and motility appear to be most pronounced through its actions at invadopodia.

## Primary Cellular Functions

### Regulation of Cell Morphology and Motility

One of the most striking and well-characterized functions of AFAP1L1 is its ability to profoundly regulate cell morphology through modulation of the actin cytoskeleton. When AFAP1L1 is overexpressed in colorectal cancer RKO cells, which normally exhibit either a predominantly flattened or elongated shape, the cellular morphology becomes drastically altered to a rounded shape[7][10][21][55]. This morphological transition from a mesenchymal-like flattened morphology to a rounded morphology is characteristic of cells undergoing transition toward an amoeboid migration mode, where cells lack mature focal adhesions and stress fibers and instead move through space using their rounded cellular shape[10][21].

This morphological change is not dependent on fibronectin coating of the substrate, as equivalent experiments conducted without fibronectin coating showed similar results[10][21][55]. To confirm that the morphological effect is specifically attributable to AFAP1L1, cells were treated with small interfering RNA (siRNA) against AFAP1L1, which led to reversion to a flattened morphology[10][21][55], demonstrating the sufficiency and necessity of AFAP1L1 expression for maintaining the rounded morphology. Notably, this morphological transition is accompanied by disassembly of focal adhesion structures, as evidenced by the loss of paxillin and vinculin at focal adhesion sites and the disorganization of actin stress fibers[7][10][21][55].

Beyond morphological changes, AFAP1L1 overexpression leads to increased cell motility on planar substrates[7][10][21][55]. When gastric cancer cells with AFAP1L1 overexpression were compared to control cells in Transwell migration and invasion assays, AFAP1L1 downregulation significantly decreased migratory (fold changes = 0.81) and invasive (fold changes = 0.74) capacity of gastric cancer AGS cells, while AFAP1L1 overexpression significantly increased migration (fold changes = 1.26) and invasion (fold changes = 1.33) of MKN74 cells[12][19][36][51]. This enhanced motility likely reflects both the morphological changes enabling amoeboid migration and the disruption of adhesive structures that would otherwise constrain cell movement.

### Promotion of Anoikis Resistance

A particularly important function of AFAP1L1 identified through in vitro and in vivo studies is its role in promoting resistance to anoikis, a form of programmed cell death triggered by loss of cell-matrix attachment[7][10][21]. Anoikis represents a critical barrier to cell survival during the early stages of metastatic dissemination, when detached cells are particularly vulnerable to death[7][21][37]. AFAP1L1-transduced colorectal cancer cells exhibited significant resistance to anoikis in vitro[7][10][21]. This anoikis resistance was further confirmed by a decrease in the TUNEL-positive rates (measuring apoptotic cells) in AFAP1L1-expressing cells[7][21]. The resistance to anoikis likely results from the ability of AFAP1L1 to disassemble focal adhesions and reduce cell-matrix contacts, paradoxically protecting cells from the death signals normally triggered by loss of adhesion[7][21][37].

The in vivo significance of this anoikis resistance became apparent when cells were injected as a suspension into mice for xenograft formation[7][21][37]. Subcutaneous injections of cell suspensions in phosphate-buffered saline (PBS) are highly likely to evoke significant increases in anoikis-related signaling cascades. However, AFAP1L1-expressing cells, due to their acquired resistance to anoikis, survive this critical early step of xenograft formation and consequently grow faster in vivo than control cells[7][21][37]. This demonstrates that the adverse impact of upregulated AFAP1L1 expression on treatment outcomes in colorectal cancer may be attributable to enhanced cell motility and increased anoikis resistance, rather than to enhanced invasion capability through degradation of the surrounding matrix[7][21][37].

### Invadopodium Formation and Maintenance

AFAP1L1 plays a direct role in the formation and maintenance of invadopodia, specialized cellular protrusions involved in extracellular matrix degradation and invasion[8][14][20][43]. When AFAP1L1 is overexpressed in A7r5 cells, it has the ability to induce podosome formation and move to podosomes without stimulation[8][14][43]. Similarly, osteosarcoma SaOS2 cells transiently expressing AFAP1L1 develop several podosome-like actin-rich dots, structures which are seldom observed in mock-transfected cells[7][21][55]. In most cells expressing AFAP1L1, focal adhesion structures are disassembled, and actin stress fibers are disorganized[7][21][55]. This transition from stress fiber-dominated actin organization to podosome/invadopodia-dominated organization represents a fundamental shift in cellular architecture that facilitates the invasion phenotype.

The molecular mechanism through which AFAP1L1 drives invadopodia formation appears to involve its interaction with cortactin, which recruits the Arp2/3 complex, a central driver of branched actin polymerization[8][14][20][43]. Additionally, AFAP1L1's interaction with Nck2, which links to N-WASP and the Arp2/3 complex, provides another pathway for recruitment of actin nucleation machinery to sites of invadopodia formation[48][49]. The disruption of focal adhesions through AFAP1L1's interaction with vinculin removes a structural barrier to invadopodia assembly, as focal adhesions and invadopodia occupy distinct cellular niches and represent competing actin-based cellular architectures.

### Epithelial-to-Mesenchymal Transition (EMT) Promotion

A critical function of AFAP1L1 in cancer cells is its role in promoting epithelial-to-mesenchymal transition (EMT), a fundamental cellular process driving cancer cell invasion and metastasis[12][19][36][51][57]. EMT is often accompanied by reorganization of the cytoskeleton, which is necessary to destroy cell-cell attachment and strengthen cell-matrix adhesions[12]. AFAP1L1 could regulate cytoskeleton rearrangement and thereby facilitate EMT.

In gastric cancer cells, AFAP1L1 downregulation promotes expression of epithelial markers E-cadherin and EPCAM while inhibiting mesenchymal markers vimentin and N-cadherin[12][19][36][51]. Conversely, AFAP1L1 overexpression reduces the expression of epithelial markers and increases the expression of mesenchymal markers in gastric cancer cells[12][19][36][51]. The molecular mechanism underlying AFAP1L1-driven EMT in gastric cancer involves its interaction with VAV2 to activate CDC42, which promotes expression of integrin subunit alpha 5 (ITGA5) and activation of integrin signaling pathways[12][19][36][51][57]. Integrin signaling, particularly through ITGA5, is well-established to promote EMT and enhance cell invasion, providing a mechanistic link between AFAP1L1 expression and the acquisition of invasive capabilities[12][19][36][51].

The occurrence of EMT is often accompanied by reorganization of the cytoskeleton that is necessary to destroy cell-cell attachment and strengthen cell-matrix adhesions[12]. Because AFAP1L1 regulates cytoskeleton rearrangement, its role in facilitating EMT is well-integrated with its other functions in modulating actin dynamics and promoting cell motility. Through these coordinated effects on cellular morphology, adhesion structures, and cytoskeletal organization, AFAP1L1 orchestrates the cellular transformations necessary for epithelial cancer cells to acquire invasive and metastatic capabilities.

## Role in Cancer Progression and Metastasis

### Colorectal Cancer

AFAP1L1 was initially identified as a metastasis-predicting marker for spindle cell sarcomas through gene expression profiling, but its role in cancer progression was subsequently discovered to extend far beyond sarcomas to affect multiple epithelial malignancies including colorectal cancer[7][10][21][24][31][56]. A marked elevation of AFAP1L1 gene expression was found in colorectal cancer (CRC) tissues compared to adjacent normal mucosa[7][10][21][40][54]. Multivariate analysis revealed that AFAP1L1 expression was an independent and significant factor for the recurrence of rectal cancers[7][10][21][40][54]. Furthermore, the addition of the AFAP1L1 expression level to the lymph node metastasis status provided more predictive information regarding postoperative recurrence in rectal cancers than lymph node status alone[7][10][21][40][54].

In vivo, AFAP1L1-transduced colorectal cancer cells showed accelerated tumor growth, presumably reflecting the anoikis resistance of these AFAP1L1-expressing cells[7][10][21][37][40][54]. Furthermore, the local administration of siRNA against AFAP1L1 significantly suppressed the in vivo tumor growth of xenografts[7][10][21][37][40][54], providing direct experimental evidence that AFAP1L1 represents a viable therapeutic target for colorectal cancers. These results suggest that AFAP1L1 plays a role in the progression of colorectal cancers by modulating cell shape and motility and by inhibiting anoikis, presumably through interactions with vinculin-containing protein complexes[7][10][21][40][54].

### Gastric Cancer

More recent comprehensive analysis has revealed that AFAP1L1 functions as a critical oncogenic driver in gastric cancer, representing the only member of the AFAP family to be significantly upregulated in gastric cancer compared with normal gastric tissues[12][19][36][51][57]. Only AFAP1L1 was associated with poor prognosis and was identified as an independent risk factor for overall survival in gastric cancer patients[12][19][36][51][57]. In vitro and in vivo experiments demonstrated that AFAP1L1 promoted gastric cancer cell proliferation, invasion, and metastasis by inducing epithelial-to-mesenchymal transition[12][19][36][51][57].

The mechanism through which AFAP1L1 drives gastric cancer progression involves its interaction with VAV2 to activate CDC42, which promotes expression of integrin subunit alpha 5 (ITGA5) and activation of integrin signaling[12][19][36][51][57]. AFAP1L1 knockdown in AGS gastric cancer cells significantly inhibited their proliferation, while overexpression of AFAP1L1 in MKN74 cells significantly promoted proliferative capacity[12][19][36][51][57]. Transwell migration and invasion assays demonstrated that AFAP1L1 downregulation significantly decreased migratory (fold changes = 0.81) and invasive (fold changes = 0.74) capacity, while AFAP1L1 overexpression significantly increased migration (fold changes = 1.26) and invasion (fold changes = 1.33)[12][19][36][51][57]. In vivo subcutaneous mouse models showed that AFAP1L1 downregulation inhibited growth of subcutaneous tumors, while AFAP1L1 overexpression promoted tumor growth[12][19][36][51][57]. In vivo metastatic experiments showed that knockdown of AFAP1L1 in gastric cancer cells significantly inhibited formation of pulmonary and liver metastasis foci, with MKN74 cells with AFAP1L1 overexpression metastasizing more easily to lung and liver compared to control cells[12][19][36][51][57].

### Sarcomas and Other Malignancies

AFAP1L1 was originally identified as a metastasis-predicting marker for spindle cell sarcomas, including osteosarcoma, liposarcoma, and leiomyosarcoma[7][10][24][31][45][56]. In univariate and multivariate analyses, higher expression of AFAP1L1 was found to contribute to the occurrence of distant metastases in sarcomas, along with patient age and tumor grade[24][31][56]. Knockdown of the AFAP1L1 gene in sarcoma cells reduced cell invasiveness, while forced expression of AFAP1L1 in immortalized human mesenchymal stem cells increased anchorage-independent cell growth as well as cell invasiveness[24][31][56]. Gelatin zymography demonstrated increased MMP-9 secretion in AFAP1L1-overexpressed cells, suggesting that AFAP1L1 also promotes the secretion of proteolytic enzymes involved in extracellular matrix degradation[7][10][21][24][31][37].

AFAP1L1 has also been documented to promote cell proliferation, cell cycle progression and inhibit cell apoptosis in non-small cell lung cancer[36][51][57]. The emerging pattern across multiple cancer types suggests that AFAP1L1 functions as a general driver of cancer progression through its ability to modify cellular morphology, promote motility and invasion, facilitate EMT, and enhance anoikis resistance.

## Signaling Pathways and Molecular Mechanisms

### The VAV2-CDC42-ITGA5 Signaling Axis

Recent mechanistic studies have revealed that AFAP1L1 functions as a critical upstream regulator of the VAV2-CDC42-ITGA5 signaling axis in gastric cancer[12][19][36][51][57]. AFAP1L1 interacts with VAV2, a guanine nucleotide exchange factor for Rho family GTPases[12][19][36][51][57]. This interaction allows VAV2 to catalyze the nucleotide exchange on CDC42, converting it from its inactive GDP-bound state to its active GTP-bound state[12][19][36][51][57]. Once activated, CDC42, a small GTPase of the Rho subfamily, promotes the expression and activation of integrin subunit alpha 5 (ITGA5) and downstream integrin signaling[12][19][36][51][57].

Integrin signaling, particularly through ITGA5 (α5β1 integrin), is well-established to promote cell-matrix adhesion, cell migration, invasion, and epithelial-to-mesenchymal transition[12][19][36][51][57]. The ITGA5 integrin interacts with extracellular matrix proteins containing Arg-Gly-Asp (RGD) sequences, including fibronectin, and transmits signals into the cell that promote motility and survival. Through this signaling pathway, AFAP1L1 expression drives gastric cancer cell proliferation, migration, invasion, and metastasis[12][19][36][51][57].

### Cytoskeleton Remodeling and Focal Adhesion Dynamics

AFAP1L1 regulates cytoskeleton remodeling through multiple mechanisms that collectively drive the transition from stress fiber-dominated actin organization to invadopodia-dominated organization[7][10][12][21][55]. The protein's direct binding to actin filaments through its carboxy-terminal actin binding domain enables it to influence actin polymer dynamics[14][20]. Its interaction with cortactin, which recruits the Arp2/3 complex, allows AFAP1L1 to nucleate branched actin polymerization at sites of invadopodia[8][14][20][43][48]. Its interaction with Nck2 provides an additional link to actin nucleation machinery through the N-WASP pathway[48][49].

Perhaps equally important is AFAP1L1's ability to promote focal adhesion disassembly through its interaction with vinculin[7][10][21]. The detachment of vinculin from focal adhesions, induced by AFAP1L1 overexpression, reflects the disassembly of these structures and leads to alterations in cell shape and motility as a consequence of reduced cell-matrix contacts[7][21][55]. This reduction in focal adhesion-mediated cell-matrix adhesion removes a barrier to cell motility and enables the transition to amoeboid migration. Furthermore, focal adhesion disassembly and invadopodia assembly are alternative cellular states—both involve actin reorganization but toward different structural ends—and AFAP1L1 simultaneously promotes both the disassembly of focal adhesions and the assembly of invadopodia, coordinating these complementary processes.

### Rho GTPase Regulation

The Rho family of small GTPases, including RhoA, Rac1, and CDC42, play critical roles in the regulation of the actin cytoskeleton, including cell shape and migration[10][21]. It is well-established that Rho-GTPases definitely play a critical role in the regulation of the actin cytoskeleton, including cell shape and migration[10][21]. AFAP1L1 integrates into Rho-GTPase signaling primarily through its interaction with VAV2 and activation of CDC42, though additional interactions with other regulators of Rho GTPases may also occur. CDC42 activation by the VAV2-AFAP1L1 complex promotes actin polymerization through N-WASP and the Arp2/3 complex, driving the formation of branched actin networks characteristic of invadopodia and contributing to cell motility[12][19][36][51][57].

## Transcriptional Regulation of AFAP1L1

### Sp3 Transcription Factor Control

The expression of AFAP1L1 is tightly controlled at the transcriptional level through the action of the transcription factor Sp3 (specificity protein 3)[31][56][59]. Overexpression of Sp1 and Sp3 proteins transactivated the proximal AFAP1L1 promoter construct, and electrophoretic mobility shift assays showed that both Sp1 and Sp3 were able to bind to the promoter region in vitro[31][56][59]. Chromatin immunoprecipitation experiments, however, revealed that Sp3 is the major factor binding to the proximal promoter region of the AFAP1L1 gene in AFAP1L1-positive cells[31][56][59].

Treatment with mithramycin A, an inhibitor of proteins binding to GC-rich regions, prevented Sp3 from binding to the proximal promoter region of AFAP1L1 and decreased its expression in a dose-dependent manner[31][56][59]. Importantly, knocking down Sp3 using small inhibitory RNA significantly reduced AFAP1L1 expression, which was partially restored by expressing siRNA-resistant Sp3[31][56][59]. These findings indicate a direct and dominant role for Sp3 in driving AFAP1L1 expression in sarcomas and other cell types.

The Sp3 transcription factor is a member of the specificity protein family that binds to GC-rich promoter regions and regulates the transcription of genes involved in various cellular processes, including differentiation, proliferation, and apoptosis[31][56][59]. Sp3 is distinguished from other family members by its particular role in cell differentiation and its sensitivity to certain cellular signals and stresses. The identification of Sp3 as the key transcriptional regulator of AFAP1L1 suggests that signaling pathways that regulate Sp3 activity or expression—including stress responses, growth factor signaling, and differentiation signals—may control AFAP1L1 expression levels in cancer cells and contribute to the transition to an invasive phenotype.

### Ets Transcription Factor Involvement

In addition to Sp3, the Ets family of transcription factors also appears to participate in the transcriptional regulation of AFAP1L1[31][56][59]. Luciferase assays suggested the involvement of the Ets protein family in the regulation of AFAP1L1 transcription, and transfection of a dominant-negative Ets vector significantly reduced AFAP1L1 promoter activity[31][56][59]. This suggests that Ets proteins cooperate with Sp3 to drive AFAP1L1 transcription, though Sp3 appears to be the dominant factor. Interestingly, transfection of ELK1, another member of the Ets family, actually reduced AFAP1L1 promoter activity, suggesting that different Ets family members may have distinct, and sometimes opposing, roles in regulating AFAP1L1 transcription[31][56][59].

The involvement of both Sp and Ets transcription factors suggests that AFAP1L1 expression is regulated by signaling pathways that activate these transcription factors, including both basal growth signaling and stress-responsive signaling cascades. This regulatory architecture positions AFAP1L1 as a gene whose expression responds to cellular stress and growth factor signals, consistent with its role as a driver of cancer cell phenotypes under stress conditions such as matrix detachment.

## Associated Diseases and Genetic Pathology

### Coffin-Siris Syndrome 8

In addition to cancer, mutations in the *AFAP1L1* gene have been associated with Coffin-Siris Syndrome 8 (CSS8), a congenital disorder characterized by impaired intellectual development, speech impairment, hypotonia (low muscle tone), feeding difficulties, and behavioral abnormalities[1][26][29]. Dysmorphic features such as hypertrichosis (excessive body hair), thick eyebrows, thin upper lip vermilion, and an upturned nose may be present[26][29]. Additional features include coarse facial features, malformations of various organ systems, and absent or hypoplastic fifth digit nails or phalanges[26][29]. Patients often experience sucking and feeding difficulties, poor growth, ophthalmologic abnormalities, hearing impairment, and spinal anomalies[26][29].

The precise mechanisms through which AFAP1L1 mutations cause Coffin-Siris Syndrome 8 remain to be fully elucidated, but the phenotype suggests that AFAP1L1 is essential for normal neurological development, potentially through its roles in regulating cytoskeletal dynamics in developing neurons. The brain expression of AFAP1L1, particularly in Purkinje cells and around granule cells of the cerebellar granular layer, suggests involvement in cerebellar development and function, which may explain some of the neurological manifestations of CSS8.

### Spindle Cell Sarcoma

As noted above, AFAP1L1 is strongly associated with spindle cell sarcomas, including osteosarcoma, liposarcoma, and leiomyosarcoma[1][45]. These associations suggest that AFAP1L1 dysregulation contributes to the malignant transformation and progression of these sarcomas.

## Therapeutic Implications and Future Directions

### AFAP1L1 as a Therapeutic Target

The evidence that AFAP1L1 promotes cancer progression across multiple cancer types, combined with the finding that local administration of siRNA against AFAP1L1 significantly suppresses in vivo tumor growth, suggests that AFAP1L1 represents a promising therapeutic target for cancer treatment[7][10][21][37][40][54]. The fact that AFAP1L1 expression is an independent prognostic factor for cancer recurrence and poor survival further supports its development as a therapeutic target.

Several strategies could be pursued to target AFAP1L1 in cancer therapy. Direct knockdown using antisense oligonucleotides or siRNA could reduce AFAP1L1 expression in cancer cells. Small molecule inhibitors targeting the protein-protein interactions through which AFAP1L1 exerts its effects—such as its interactions with cortactin, vinculin, VAV2, Nck2, or actin—could potentially disrupt AFAP1L1 function without completely eliminating the protein. Transcriptional inhibition of AFAP1L1 expression through Sp3 inhibitors or other approaches targeting Sp3-AFAP1L1 promoter interactions could prevent upregulation of AFAP1L1 in cancer cells.

### Biomarker Development

AFAP1L1 expression levels show promise as a prognostic biomarker for cancer recurrence and poor survival across multiple cancer types[7][10][12][19][21][36][40][51][54][57]. The addition of AFAP1L1 expression to standard clinicopathologic factors such as lymph node metastasis status provides more predictive information regarding cancer recurrence and overall survival than these factors alone[7][10][21][40][54]. Development of standardized methods for AFAP1L1 assessment (such as immunohistochemistry scoring systems or qPCR assays) and validation in large clinical cohorts could establish AFAP1L1 as a clinical biomarker that guides treatment decisions and prognostic counseling.

## Conclusion

AFAP1L1 has emerged as a critical regulator of cancer cell invasion, metastasis, and epithelial-to-mesenchymal transition through its multiple roles in modulating actin cytoskeleton dynamics, controlling cell-matrix adhesion, and regulating fundamental processes like anoikis resistance and cell motility. As a multidomain adaptor protein, AFAP1L1 integrates signals from multiple upstream pathways—including growth factor signaling through receptor tyrosine kinases, integrin signaling, and Rho GTPase cascades—and translates these signals into coordinated changes in cellular morphology and migration capacity. The protein's specific interactions with cortactin, rather than c-Src as seen with its family member AFAP1, provide a specialized niche within the adaptor protein family that positions AFAP1L1 as a coordinator of invadopodia formation and podosome assembly, key structures driving invasion and metastasis[7][10][12][14][20][21][36][51].

The discovery of the VAV2-CDC42-ITGA5 signaling axis downstream of AFAP1L1 provides a molecular framework for understanding how AFAP1L1 promotes epithelial-to-mesenchymal transition and the acquisition of invasive capabilities in epithelial cancers[12][19][36][51][57]. The identification of Sp3 as the major transcriptional regulator of AFAP1L1 offers potential strategies for controlling AFAP1L1 expression through targeting Sp3 or its upstream regulators. The robust evidence that AFAP1L1 knockdown suppresses tumor growth in vivo and that AFAP1L1 expression independently predicts cancer recurrence and poor survival establish this protein as a promising therapeutic target and biomarker for multiple cancer types. Future research should focus on developing specific inhibitors of AFAP1L1 function, understanding the upstream signaling pathways that regulate AFAP1L1 expression in cancer contexts, validating AFAP1L1 as a clinical biomarker in prospective trials, and exploring combination therapeutic strategies that target AFAP1L1 together with other cancer drivers. Through these efforts, AFAP1L1 may become both a key biomarker guiding cancer patient stratification and a crucial target for developing new therapies to suppress cancer invasion and metastasis.

## Citations

1. https://www.genecards.org/cgi-bin/carddisp.pl?gene=AFAP1L1
2. https://maayanlab.cloud/Harmonizome/gene_set/Actin+filament-associated+protein+1-like+1/InterPro+Predicted+Protein+Domain+Annotations
3. https://functionome.geneontology.org/gene/UniProtKB:Q8TED9
4. https://www.proteinatlas.org/ENSG00000157510-AFAP1L1
5. https://www.informatics.jax.org/marker/MGI:2147199
6. https://www.uniprot.org/locations/SL-0501
7. https://onlinelibrary.wiley.com/doi/full/10.1002/cam4.237
8. https://pubmed.ncbi.nlm.nih.gov/21333378/
9. https://diseases.jensenlab.org/Entity?documents=10&type1=9606&id1=ENSP00000296721&type2=-26&id2=DOID%3A4235
10. https://pmc.ncbi.nlm.nih.gov/articles/PMC4303145/
11. https://www.uniprot.org/uniprotkb/Q8TED9/entry
12. https://pmc.ncbi.nlm.nih.gov/articles/PMC9835296/
13. https://pmc.ncbi.nlm.nih.gov/articles/PMC3085893/
14. https://researchrepository.wvu.edu/etd/3379/
15. https://www.ncbi.nlm.nih.gov/gene/998
16. https://geneglobe.qiagen.com/us/knowledge/gene/ENSMUSG00000033032
17. https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0049709
18. https://www.malacards.org/card/coffin_siris_syndrome_8
19. https://maayanlab.cloud/Harmonizome/gene/AFAP1L1
20. https://www.datacommons.org/browser/bio/DOID_0112367
21. https://pmc.ncbi.nlm.nih.gov/articles/PMC3541374/
22. https://pubmed.ncbi.nlm.nih.gov/25301070/
23. https://mhlw-grants.niph.go.jp/system/files/2013/133041/201313047B/201313047B0007.pdf
24. https://stacks.cdc.gov/view/cdc/192171/cdc_192171_DS1.pdf
25. https://pubmed.ncbi.nlm.nih.gov/36631800/
26. https://pmc.ncbi.nlm.nih.gov/articles/PMC4774376/
27. https://www.spandidos-publications.com/10.3892/br.2016.588
28. https://pmc.ncbi.nlm.nih.gov/articles/PMC7737098/
29. https://f1000research.com/posters/1089915
30. https://www.molbiolcell.org/doi/abs/10.1091/mbc.e06-01-0088?etoc=
31. https://pubmed.ncbi.nlm.nih.gov/26212012/
32. https://pmc.ncbi.nlm.nih.gov/articles/PMC10999758/
33. https://pmc.ncbi.nlm.nih.gov/articles/PMC1933402/
34. https://w.string-db.org/overview/overview.59729.html
35. https://en.wikipedia.org/wiki/Pleckstrin_homology_domain
36. https://pubmed.ncbi.nlm.nih.gov/23326307/