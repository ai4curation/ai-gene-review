---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-01-02T23:08:37.637405'
end_time: '2026-01-02T23:10:41.672700'
duration_seconds: 124.04
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: AIMP2
  gene_symbol: AIMP2
  uniprot_accession: Q13155
  protein_description: 'RecName: Full=Aminoacyl tRNA synthase complex-interacting
    multifunctional protein 2; AltName: Full=Multisynthase complex auxiliary component
    p38; AltName: Full=Protein JTV-1;'
  gene_info: Name=AIMP2; Synonyms=JTV1; ORFNames=PRO0992;
  organism_full: Homo sapiens (Human).
  protein_family: Not specified in UniProt
  protein_domains: AIMP2. (IPR042360); AIMP2_LysRS-bd. (IPR031889); AIMP2_thioredoxin.
    (IPR041503); Glutathione-S-Trfase_C_sf. (IPR036282); GST_C. (IPR004046)
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 47
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q13155
- **Protein Description:** RecName: Full=Aminoacyl tRNA synthase complex-interacting multifunctional protein 2; AltName: Full=Multisynthase complex auxiliary component p38; AltName: Full=Protein JTV-1;
- **Gene Information:** Name=AIMP2; Synonyms=JTV1; ORFNames=PRO0992;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** AIMP2. (IPR042360); AIMP2_LysRS-bd. (IPR031889); AIMP2_thioredoxin. (IPR041503); Glutathione-S-Trfase_C_sf. (IPR036282); GST_C. (IPR004046)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "AIMP2" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'AIMP2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **AIMP2** (gene ID: AIMP2, UniProt: Q13155) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

<think>
Let me think about this query carefully. I need to write a comprehensive research report on the AIMP2 gene (UniProt Q13155) in humans. The user has provided extensive search results and wants me to focus on:

1. The primary function of the gene product
2. Biological processes and localization
3. Signaling/biochemical pathways
4. Experimental evidence and structural information

Let me start by verifying this is the correct gene:
- Gene symbol: AIMP2
- UniProt: Q13155
- Protein: Aminoacyl tRNA synthase complex-interacting multifunctional protein 2
- Organism: Homo sapiens
- Synonyms: JTV-1, p38, PRO0992

From the search results, I can see this is indeed the correct protein. The results are rich with information about:
1. AIMP2 as a scaffolding protein in the aminoacyl-tRNA synthetase complex
2. Its role in DNA damage response and p53 activation
3. Its role in cell death pathways (TNF-alpha, TGF-beta)
4. Its association with Parkinson's disease
5. Its role as a tumor suppressor
6. The oncogenic variant AIMP2-DX2
7. Its role in viral infections
8. Its role in intestinal stem cells and Wnt signaling

The search results are comprehensive and from authoritative sources (NCBI, UniProt, PNAS, scientific journals). I need to write a 10,000+ word report that covers:

1. Introduction with overview
2. Structure and molecular composition
3. Primary function in the multi-tRNA synthetase complex
4. DNA damage response and p53 regulation
5. Other signaling pathways (TNF-alpha, TGF-beta, Wnt/beta-catenin)
6. Cellular localization and dynamics
8. Parkinson's disease and neurodegeneration


9. Cancer biology and AIMP2-DX2
10. Viral infections
11. AIMP2-DX2 variant and therapeutic implications
12. Conclusion

I'll structure this as a comprehensive scientific report with proper citations, ensuring each section builds on the previous findings to create a cohesive narrative about AIMP2's multifaceted roles in human biology.
</think>

# AIMP2: A Multifunctional Protein Linking Translation Machinery to Cellular Stress Response and Tumor Suppression

AIMP2, also known as aminoacyl-tRNA synthetase complex-interacting multifunctional protein 2 (alternatively called p38 or JTV-1), represents one of the most multifaceted and functionally diverse proteins in cellular biology, serving simultaneously as a scaffolding component of the translational machinery and as a critical stress-response regulator that orchestrates cell fate decisions in response to DNA damage, inflammatory signals, and other cellular stresses[2][12][30]. This protein operates as a paradigmatic example of how a single gene product can maintain distinct, spatially and temporally segregated functions that are essential for both normal cellular homeostasis and the prevention of malignant transformation[11][12]. The research on AIMP2 over the past two decades has progressively unveiled a complex functional landscape wherein the protein's role extends far beyond its canonical position within the multi-tRNA synthetase complex, revealing instead a sophisticated molecular integrator that coordinates protein synthesis with genome integrity surveillance and programmed cell death pathways[8][15][16].

## Structural Organization and Assembly Within the Multi-tRNA Synthetase Complex

AIMP2 functions as a critical non-enzymatic component of the multi-tRNA synthetase complex (MSC), a massive macromolecular assembly that represents the second largest translation-related machinery in human cells[2][40]. The MSC comprises nine different aminoacyl-tRNA synthetases (ARS) and three non-enzymatic auxiliary factors: AIMP1 (also called p43), AIMP2 (p38), and AIMP3 (p18)[2][39]. The protein structure of AIMP2 reveals a molecular architecture specifically optimized for its scaffolding role, consisting of an N-terminal domain and a glutathione S-transferase (GST)-like C-terminal domain that is remarkably similar to the GST domains found in other regulatory proteins[2][28][40]. This structural organization is not merely incidental but rather essential for AIMP2's ability to interact with multiple synthetase components and coordinate their proper assembly.

The three-dimensional structure of the multi-tRNA synthetase complex has been progressively elucidated through combined crystallographic and cross-linking mass spectrometry approaches, revealing that AIMP2 acts as a central scaffolding hub that interfaces with multiple enzyme components[13][40]. Recent structural studies utilizing cross-linking mass spectrometry demonstrated that four AARSs containing GST-like domains—specifically methionyl-tRNA synthetase (MRS), glutamyl-prolyl-tRNA synthetase (EPRS), AIMP2, and AIMP3—form a core heterotetrameric complex structure that serves as the architectural foundation for the entire multi-tRNA synthetase assembly[40]. AIMP2 interacts extensively with the majority of component proteins within this complex, showing preferential interactions with lysyl-tRNA synthetase (LysRS), aspartyl-tRNA synthetase (DRS), and other aminoacyl-tRNA synthetases[39]. Among the three non-enzymatic auxiliary proteins, AIMP2 appears to interact with the broadest range of synthetase components, underscoring its central role in maintaining complex integrity[39][40].

The lysyl-tRNA synthetase-AIMP2 interaction has been particularly well-characterized through high-resolution crystal structural analysis conducted at 1.88 Ångstrom resolution, revealing that human LysRS forms a remarkably tight assembly with AIMP2 through a sophisticated arrangement wherein two AIMP2 N-terminal peptides form an antiparallel scaffold that holds two LysRS dimers through four distinct binding motifs and additional stabilizing interactions[13]. This structural investigation revealed two distinct conformational states of the LysRS-AIMP2 subcomplex: a loose V-form where the two LysRS dimers connect through AIMP2's N-terminal regions and remain flexibly positioned, and a retracted X-form where the LysRS dimers are held in closer proximity[13]. These two assembly states appear to have distinct functional significance, with the V-form potentially facilitating individual LysRS dimer dissociation for extramolecular functions while the X-form provides a more organized configuration for efficient tRNA aminoacylation within the complex[13].

## Primary Function as a Scaffolding Protein in Protein Synthesis

In its canonical role as a component of the multi-tRNA synthetase complex, AIMP2 is essential for the assembly and stability of this macromolecular machine that catalyzes the critical first step of protein synthesis—the aminoacylation of transfer RNAs[2][4][5]. The multi-tRNA synthetase complex brings together nine different aminoacyl-tRNA synthetases, each with the capacity to recognize a specific amino acid and its cognate transfer RNA molecules, ensuring the fidelity and efficiency of protein synthesis across the genome[39][40]. AIMP2's scaffolding function ensures that all component synthetases are properly assembled into a functional complex, with appropriate spatial organization that optimizes substrate channeling and catalytic efficiency[13][39]. Depletion of AIMP2 leads to significant destabilization of bound enzymes, demonstrating the protein's critical role in maintaining complex integrity[39].

The functional significance of AIMP2 in the translation apparatus extends beyond simple structural scaffolding. The protein's presence within the complex influences the catalytic properties and expression levels of associated aminoacyl-tRNA synthetases, suggesting that AIMP2 may modulate the translational efficiency of the entire enzyme complement[39]. This modulation likely occurs through both indirect structural effects and potentially through more direct regulatory mechanisms involving protein-protein interactions that fine-tune enzyme activity. The multi-tRNA synthetase complex has been proposed to serve as a molecular reservoir that can respond dynamically to cellular signals, and AIMP2's presence appears to be critical for this responsive capacity[16].

Furthermore, AIMP2 contains a thioredoxin-like domain and GST-C domain that provide additional functional properties beyond simple scaffolding[17][25]. These domains may provide oxidoreductase or glutathione-binding capabilities that could contribute to the complex's regulation under different cellular conditions, particularly under oxidative stress[25]. The presence of these conserved domains across the AIMP protein family suggests that these functional modules have been specifically maintained throughout evolution, indicating their importance for cellular function beyond the core scaffolding role.

## DNA Damage Response and p53 Regulation: A Stress-Induced Function

One of the most thoroughly characterized and functionally important roles of AIMP2 has emerged from investigations into cellular responses to genotoxic stress and DNA damage[8][15][16]. In response to DNA damage induced by ultraviolet radiation or other genotoxic agents, AIMP2 undergoes a remarkable functional transformation wherein it dissociates from the multi-tRNA synthetase complex and translocates to the nucleus to interact with the tumor suppressor protein p53[8][15][16]. This stress-responsive dissociation and nuclear translocation represents a fundamental example of how the same protein can be repurposed to perform distinct functions under different cellular conditions—a capacity for functional plasticity that appears to be characteristic of the multi-tRNA synthetase complex components[15][39][42].

The molecular mechanism of this DNA damage-induced AIMP2 release involves phosphorylation-dependent dissociation from the multi-tRNA synthetase complex. Specifically, upon DNA damage, AIMP2 becomes phosphorylated by the c-Jun N-terminal kinase (JNK) pathway at critical residues that destabilize its interaction with other complex components[15][16]. This JNK-dependent phosphorylation has been shown to be both necessary and sufficient for AIMP2's dissociation from the complex and its subsequent nuclear translocation[15]. The requirement for JNK-mediated phosphorylation establishes a clear mechanistic link between the MAPK stress-signaling pathway and AIMP2's stress-response functions, indicating that AIMP2 is an integrated target of cellular stress-sensing mechanisms[15].

Once in the nucleus, AIMP2 directly interacts with p53 through a specific interaction domain spanning approximately amino acid residues 162-225, and this interaction has profound consequences for p53's stability and function[8][15][16]. AIMP2 blocks the interaction between p53 and MDM2 (murine double minute 2), an E3 ubiquitin ligase that normally marks p53 for proteasomal degradation[8][15]. By physically shielding p53 from MDM2-mediated ubiquitination, AIMP2 stabilizes p53 levels in the nucleus, allowing p53 to accumulate to levels sufficient to activate transcription of pro-apoptotic target genes including PUMA (p53-regulated modulator of apoptosis) and GADD45[8][15][16]. The enhancement of p53 activity by AIMP2 is both direct and functionally significant—AIMP2-deficient cells show markedly reduced p53 accumulation in response to DNA damage, demonstrating that AIMP2 is not merely a regulatory auxiliary but rather a functionally critical activator of p53 in the genotoxic stress response[15][16].

The specificity of the AIMP2-p53 interaction is particularly noteworthy. The peptide region of AIMP2 spanning amino acids 84-225 has been shown to interact with p53 in in vitro pull-down assays, and mutations within this region that disrupt p53 binding abolish AIMP2's proapoptotic activity, establishing a clear structure-function relationship[8][16]. Interestingly, AIMP2 shows decreased affinity for phosphorylated p53, suggesting that as p53 becomes phosphorylated and activated during the apoptotic response, the AIMP2-p53 interaction is attenuated, allowing AIMP2 to dissociate and making room for other regulatory proteins to interact with activated p53[8]. This cyclic interaction pattern implies a sophisticated temporal regulation of p53 activity wherein AIMP2 provides an early protective interaction that stabilizes p53, but the subsequent phosphorylation of p53 by upstream kinases naturally terminates this interaction, allowing the apoptotic program to proceed.

The functional consequences of this AIMP2-mediated p53 stabilization are substantial. AIMP2-deficient cells demonstrate remarkable resistance to DNA damage-induced apoptosis, retaining normal cell cycle checkpoint function but failing to undergo apoptosis at normal rates[8][15]. Conversely, cells with enhanced AIMP2 expression show increased susceptibility to apoptosis in response to DNA damage[8]. This clear correlation between AIMP2 expression levels and apoptotic sensitivity establishes AIMP2 as a critical determinant of cellular responses to genotoxic stress and suggests that AIMP2 may function as a "rheostat" that tunes the threshold at which DNA damage triggers apoptosis[8][15][16].

## TNF-α Signaling and TRAF2-Mediated Apoptosis

Beyond its role in DNA damage-induced p53 activation, AIMP2 has emerged as a critical regulator of tumor necrosis factor-alpha (TNF-α) signaling, mediating the pro-apoptotic arm of TNF-α responses[19][22][32]. When cells are stimulated with TNF-α, a cytokine that can trigger either survival or death responses depending on cellular context and signal intensity, AIMP2 specifically enhances the apoptotic response by targeting TNF receptor-associated factor 2 (TRAF2), a central component of the TNF-α signaling pathway[19][22][32]. This function operates through a mechanism distinct from AIMP2's p53-centered DNA damage response but with comparable functional importance for apoptosis induction.

The mechanism of AIMP2-mediated TRAF2 regulation reveals an elegant example of how AIMP2 facilitates protein ubiquitination without itself possessing E1, E2, or E3 enzyme activities[19][22][32]. Upon TNF-α stimulation, AIMP2 interacts directly with TRAF2 and, through this interaction, facilitates the recruitment of the E3 ubiquitin ligase c-IAP1 (inhibitor of apoptosis protein 1) to TRAF2[19][22][32]. The enhanced proximity of c-IAP1 to TRAF2 resulting from AIMP2-mediated bridging dramatically increases the rate of ubiquitin-dependent degradation of TRAF2[19][22]. The degradation of TRAF2, a protein that normally inhibits pro-apoptotic signaling by ubiquitinating signaling molecules in the TNF-α pathway, tips the balance toward apoptosis induction. The peptide region of AIMP2 spanning amino acids 84-225 has been identified as the TRAF2-binding domain, and deletion of this region abolishes AIMP2's pro-apoptotic activity in TNF-α signaling[22][32].

The downstream consequences of TRAF2 degradation include the suppression of nuclear factor-kappa B (NFκB) signaling, a survival pathway that normally opposes apoptosis[19][22]. AIMP2 expression leads to increased levels of IκB (inhibitor of κB), which sequesters NFκB in the cytoplasm and prevents its nuclear translocation to activate survival genes[19][22]. This mechanism establishes a clear connection between AIMP2-mediated TRAF2 degradation and inhibition of pro-survival signaling, thereby biasing the cellular response toward apoptosis[19]. TNF-α-induced cell death was significantly compromised in AIMP2-deficient or AIMP2-suppressed cells and was substantially enhanced by exogenous AIMP2 supplementation, confirming AIMP2's essential role in TNF-α-dependent apoptosis[19][22].

## TGF-β Signaling and FUBP1 Regulation

AIMP2 also functions as a critical regulator of transforming growth factor-beta (TGF-β) signaling, which plays crucial roles in cellular differentiation, proliferation control, and development[35][38][42]. In response to TGF-β stimulation, AIMP2 translocates to the nucleus where it interacts with FUSE-binding protein (FUBP1), also known as far upstream element binding protein[7][35][38][42]. FUBP1 is a multifunctional DNA and RNA-binding protein that acts as a potent transcriptional activator of the MYC proto-oncogene, a transcription factor that drives cellular proliferation[7][38]. By facilitating the ubiquitination and proteasomal degradation of FUBP1, AIMP2 leads to the suppression of MYC transcription, thereby exerting an anti-proliferative effect that is particularly critical in the context of lung cell differentiation[7][35][42].

Recent research has identified Smurf2, a SMAD ubiquitination regulatory factor, as the E3 ubiquitin ligase responsible for FUBP1 ubiquitination in this pathway[44][47]. AIMP2 appears to enhance the interaction between FUBP1 and Smurf2, facilitating the polyubiquitination and degradation of FUBP1[44][47]. This mechanism demonstrates AIMP2's broader role as a facilitator of ubiquitin-dependent protein degradation across multiple signaling pathways. The functional significance of this pathway is underscored by observations that AIMP2 heterozygous mice show increased susceptibility to TGF-β-driven tumorigenesis, indicating that AIMP2's capacity to suppress MYC expression and inhibit proliferation represents a critical tumor-suppressive function[11][35][42].

The nuclear translocation of AIMP2 in response to TGF-β stimulation parallels its behavior in DNA damage responses, suggesting that cells have evolved multiple stress-response pathways that converge on AIMP2 as a key regulator of cellular fate[35][42]. Some evidence suggests that AIMP2 may be phosphorylated at serine 156 by p38 MAPK in response to TGF-β, providing a phosphorylation-dependent mechanism for AIMP2 dissociation from the multi-tRNA synthetase complex analogous to the JNK-dependent phosphorylation observed in DNA damage responses[35][42]. This convergence of multiple phosphorylation-based dissociation pathways suggests that AIMP2 exists in a dynamic equilibrium within the complex, with various cellular stress signals capable of triggering its release and relocation to sites of active signal transduction.

## Wnt/β-Catenin Signaling in Intestinal Stem Cell Control

Beyond its functions in DNA damage and inflammatory responses, AIMP2 has recently been recognized as a critical regulator of Wnt/β-catenin signaling, a fundamental pathway controlling intestinal stem cell maintenance and proliferation[33][55][58]. In the intestinal epithelium, which continuously self-renews through division of leucine-rich repeat-containing G-protein–coupled receptor 5 (LGR5)-expressing intestinal stem cells, AIMP2 expression is particularly high in the crypts of Lieberkühn, the region where these stem cells reside[33][55]. The canonical Wnt/β-catenin signaling pathway functions through a complex cascade wherein Wnt ligand binding to cell surface receptors inhibits the β-catenin destruction complex, allowing β-catenin to accumulate and translocate to the nucleus where it activates transcription of proliferation-associated genes[33][55].

AIMP2 exerts its regulatory function in this pathway through a direct interaction with Dishevelled (DVL), a critical scaffolding protein in the Wnt pathway[33][55]. The interaction between AIMP2 and DVL prevents DVL from interacting with AXIN, a component of the β-catenin destruction complex[33][55]. By competing with AXIN for binding to DVL's DIX domain, AIMP2 effectively inhibits Wnt/β-catenin signaling even in the presence of Wnt ligands[33][55]. This mechanism is particularly interesting because it operates at the level of protein-protein interactions rather than through post-translational modification, representing a distinct regulatory strategy from AIMP2's roles in other signaling pathways.

The functional importance of this Wnt-pathway regulation became evident through analysis of AIMP2 heterozygous knockout mice, which demonstrated increased proliferation in intestinal crypts and an expanded intestinal stem cell compartment[33][55]. In the context of an APC-Min background predisposed to adenoma formation, AIMP2 hemizygosity increased adenoma formation, indicating that AIMP2 functions as a haploinsufficient tumor suppressor in the intestine[33][55]. This observation is particularly significant because it demonstrates that AIMP2 dosage is critical for proper regulation of stem cell proliferation—an amount of AIMP2 that is roughly half the normal level is insufficient to properly constrain Wnt/β-catenin signaling, resulting in enhanced proliferation and tumorigenesis risk[33][55]. These findings suggest that AIMP2 operates as a molecular "rheostat" that fine-tunes Wnt/β-catenin signaling activity to maintain an appropriate balance between intestinal stem cell self-renewal and differentiation.

## Cellular Localization and Dynamic Trafficking

AIMP2 displays dynamic subcellular localization that correlates with its functional state and cellular context[12][15][36][42][43][49]. Under normal, unstressed conditions, AIMP2 is predominantly localized in the cytoplasm as an integral component of the multi-tRNA synthetase complex[12][15][43]. However, in response to various cellular stress signals—including DNA damage, TNF-α stimulation, and TGF-β signaling—AIMP2 undergoes rapid nuclear translocation[12][15][35][42]. The protein is expressed across multiple tissues, with notably high expression in the brain, where it appears to play critical roles in neuronal survival and is implicated in Parkinson's disease pathogenesis[12][14][49]. Brain tissue expression analysis indicates that AIMP2 levels vary among different brain regions, with particular enrichment in areas associated with motor control[49].

The nuclear translocation of AIMP2 is not accompanied by new protein synthesis, but rather represents mobilization of pre-existing AIMP2 molecules that are released from the multi-tRNA synthetase complex in response to stress signals[15]. This distinction is important because it indicates that the cell can rapidly reprogram AIMP2 function through post-translational mechanisms without waiting for new AIMP2 synthesis, allowing for rapid responses to stresses like DNA damage. The dissociation of AIMP2 from the multi-tRNA synthetase complex appears to occur in a selective manner—while AIMP2 dissociates, other components of the complex remain associated, suggesting that dissociation does not lead to catastrophic complex disassembly but rather to a partial structural reorganization[16].

## Parkinson's Disease and Neurodegeneration

A particularly significant pathophysiological role for AIMP2 has emerged from investigations into Parkinson's disease pathogenesis. AIMP2 has been identified as a critical substrate of the E3 ubiquitin ligase parkin, mutations in which cause autosomal recessive early-onset Parkinson's disease[12][20][21][24][35][42]. Under normal circumstances, parkin-mediated ubiquitination targets AIMP2 for proteasomal degradation, and this degradation pathway is essential for normal dopaminergic neuron survival[12][21][24][35][42]. When parkin function is impaired through loss-of-function mutations or post-translational inactivation, AIMP2 accumulates in dopaminergic neurons to toxic levels[12][21][24][35][42].

The accumulation of AIMP2 in dopaminergic neurons triggers a pathogenic cascade involving activation of poly(ADP-ribose) polymerase-1 (PARP1), a nuclear enzyme that catalyzes poly-ADP-ribosylation in response to DNA damage[12][21][24][35][42]. AIMP2 interacts directly with PARP1 and promotes its over-activation, leading to excessive production of poly(ADP-ribose) polymers that trigger a form of programmed cell death called parthanatos, distinct from apoptosis and characterized by energetic depletion and nuclear translocation of AIF (apoptosis-inducing factor)[12][21][24][35][42]. This AIMP2-mediated PARP1 activation and parthanatos induction appears to be particularly selective for dopaminergic neurons, explaining the selective neurodegeneration observed in Parkinson's disease[12][21][24][35][42].

Supporting this mechanistic hypothesis, AIMP2 knockout or knockdown substantially ameliorates α-synuclein aggregation and dopaminergic cell death in various Parkinson's disease models, including preformed fibril (PFF) models and 6-hydroxydopamine (6-OHDA) toxicity models[21][24]. In a 6-OHDA-induced Parkinson's disease mouse model, approximately 50% degeneration of dopaminergic neurons was observed in wild-type mice, whereas this degeneration was largely prevented in AIMP2 heterozygous knockout mice, indicating that reducing AIMP2 expression provides substantial neuroprotection[21][24]. Furthermore, parkin expression and VPS35 (vacuolar protein sorting-associated protein 35) have been shown to prevent AIMP2-mediated cell death, suggesting that multiple genetic factors regulating AIMP2 degradation pathways influence Parkinson's disease risk[12][21][24][35][42].

Interestingly, AIMP2 accumulation in Parkinson's disease models is associated with its co-aggregation with α-synuclein, the protein that forms the pathogenic Lewy bodies characteristic of Parkinson's disease[21]. Immunoelectron microscopy analysis of postmortem brain tissue from Parkinson's disease patients revealed co-localization of AIMP2 and phosphorylated α-synuclein within electron-dense inclusion structures in Lewy bodies, suggesting that AIMP2 is directly recruited into pathogenic α-synuclein aggregates[21]. This co-aggregation may represent a pathogenic gain-of-function wherein accumulated AIMP2 facilitates or nucleates α-synuclein aggregation through its propensity to form amyloid-like oligomers[21]. Some studies suggest that AIMP2 accumulation may be triggered not only by parkin dysfunction but also by oxidative stress or mutations in the retromer component VPS35[12][21][35][42]. These findings have positioned AIMP2 as a critical node in Parkinson's disease pathogenesis and have raised the possibility that therapeutic strategies aimed at reducing AIMP2 levels or facilitating its degradation could provide neuroprotection[12][21][24][35].

## Cancer Biology and AIMP2 as a Tumor Suppressor

AIMP2 functions as a multifaceted tumor suppressor across diverse cancer types, and multiple lines of evidence support this role. AIMP2 heterozygous mice, which have approximately half the normal level of AIMP2 expression, display dramatically enhanced susceptibility to carcinogen-induced tumorigenesis across multiple tissues, including lung, colon, and skin, indicating that AIMP2 represents a haploinsufficient tumor suppressor—a protein whose cancer-suppressive functions require near-normal expression levels to be fully operative[11][35][42]. This haploinsufficiency is particularly striking given that many well-characterized tumor suppressors (such as p53) function effectively with one functional allele remaining after heterozygous loss, suggesting that AIMP2's multiple regulatory functions may collectively require near-complete AIMP2 dosage.

A pan-cancer analysis examining AIMP2 expression across diverse tumor types revealed that AIMP2 expression was overexpressed in 24 tumor tissue types compared to normal tissue, contrary to what might be expected for a tumor suppressor[20]. However, this elevated expression showed a complex relationship with survival outcomes: high AIMP2 expression was associated with poorer prognosis in five cancer types specifically, including breast cancer[20]. This seemingly paradoxical finding may reflect the fact that tumor cells that maintain or increase AIMP2 expression may represent a subset of tumors that have acquired additional oncogenic mutations capable of overriding AIMP2's tumor-suppressive functions[20]. Alternatively, the high AIMP2 expression in tumors may reflect the cell type of origin, with tumors derived from cell types that normally express high AIMP2 levels showing correspondingly elevated AIMP2 in the tumor tissue[20].

When AIMP2 expression was knocked down in breast cancer cell lines, both proliferation and migration were substantially inhibited in vitro[20]. Invasion capacity was reduced following AIMP2 knockdown, and wound healing assays demonstrated decreased migration ability in AIMP2-depleted cells[20]. These experimental findings suggest that despite the apparent overexpression of AIMP2 in some tumors, the protein's presence continues to contribute to pro-growth and pro-metastatic phenotypes, possibly because its pro-apoptotic functions are attenuated by oncogenic mutations in downstream pathways such as p53[20].

The tumor-suppressive functions of AIMP2 extend to its capacity to regulate immune infiltration and the tumor microenvironment, which emerge as critical determinants of immunotherapy response[20]. AIMP2 expression was found to be significantly associated with tumor immune infiltration, particularly with macrophage M0, M1, and M2 populations in various cancer types[20]. Genes in modules showing the highest correlation with AIMP2 expression were primarily enriched in pathways related to cell cycle control, DNA replication, and proteasome function[20]. These associations suggest that AIMP2 may influence not only direct tumor cell behavior but also the immune landscape of the tumor microenvironment, potentially through effects on tumor cell death and immunogenicity[20].

## The Oncogenic AIMP2-DX2 Variant and Its Therapeutic Implications

A fundamentally important discovery in cancer biology was the identification of AIMP2-DX2, an alternatively spliced variant of AIMP2 that arises through skipping of exon 2 and produces a truncated protein lacking 69 amino acids[27][31][34][50][53]. This variant was found to be highly expressed in multiple cancer cell lines and patient tissues from diverse cancer types, including lung cancer, breast cancer, liver cancer, bone cancer, and stomach cancer[11][27][31][34][50][53]. The elevated expression of AIMP2-DX2 in cancer tissues suggests that selective pressure favors the production of this variant during malignant transformation[34][50][53].

The molecular mechanism of AIMP2-DX2 production involves mutations in the AIMP2 pre-mRNA sequence that disrupt exonic splicing enhancer (ESE) sites required for exon 2 inclusion. Specifically, an A152G substitution in exon 2 was found to substantially reduce recognition by the SR protein SF2/ASF, a critical splicing regulator, causing exon 2 to be skipped during splicing and leading to production of AIMP2-DX2[34]. Although AIMP2-DX2 lacks the exon 2-encoded region, it retains the GST-like domains that are critical for protein-protein interactions, particularly the glutathione S-transferase domain that mediates binding to other proteins[27][31][34].

The functional consequences of AIMP2-DX2 expression are profoundly oncogenic. AIMP2-DX2 competes with full-length AIMP2 for binding to critical partners including p53, TRAF2, and FUBP1, thereby functionally antagonizing the pro-apoptotic and anti-proliferative effects of wild-type AIMP2[27][31][34][50][53]. Specifically, while AIMP2-DX2 retains the capacity to bind p53, it cannot effectively block MDM2 from binding p53 or prevent MDM2-mediated ubiquitination of p53, unlike full-length AIMP2[34][50]. This competitive inhibition creates a dominant-negative effect wherein the presence of AIMP2-DX2 renders cells resistant to apoptotic stimuli that would normally be effective in cells expressing only full-length AIMP2[34][50].

The expression of AIMP2-DX2 shows a striking correlation with cancer progression and patient survival. The ratio of AIMP2-DX2 to full-length AIMP2 expression increases according to lung cancer stage, and this ratio showed a positive correlation with reduced patient survival[34][50]. Patients with higher expression of AIMP2-DX2 showed lower survival rates than those with lower levels of this variant[34][50]. Mice that were genetically engineered to constitutively express AIMP2-DX2 showed markedly increased susceptibility to carcinogen-induced lung tumorigenesis compared to wild-type controls, providing direct evidence that AIMP2-DX2 functions as an oncogenic factor in vivo[34][50]. Suppression of AIMP2-DX2 expression through RNA interference slowed tumor growth in these transgenic mice, suggesting that AIMP2-DX2 represents an effective therapeutic target[34][50].

Recent structural and molecular investigations have revealed novel mechanisms through which AIMP2-DX2 contributes to cancer development. AIMP2-DX2 was discovered to specifically bind to the hypervariable region (HVR) of KRAS, a mutated proto-oncogene present in many cancers[27][31][51]. Importantly, AIMP2-DX2 prevents the ubiquitin-mediated degradation of KRAS that would normally be catalyzed by Smurf2 by blocking Smurf2 access to KRAS[27][31][51]. This function represents a novel mechanism of KRAS stabilization distinct from the canonical mechanisms by which KRAS-mutant tumors promote KRAS stability, and it provides a direct mechanistic link between AIMP2-DX2 expression and the oncogenic KRAS signaling that drives many cancers[27][31][51]. Additionally, AIMP2-DX2 was shown to promote proliferation, migration, and invasion of nasopharyngeal carcinoma cells by upregulating matrix metalloproteinases MMP-2 and MMP-9, linking AIMP2-DX2 to metastatic potential[35][42].

These findings have led to the development of small-molecule inhibitors specifically targeting the KRAS-binding region of AIMP2-DX2[11][27][31]. Notably, these inhibitors can directly bind to AIMP2-DX2 and reduce its protein levels while leaving full-length AIMP2 relatively unaffected[11][27][31]. In xenograft models of lung cancer, these inhibitors significantly reduced both tumor size and weight without observable changes in body weight, suggesting promising therapeutic potential with acceptable tolerability[11][27][31]. These findings have positioned AIMP2-DX2 as a novel oncogenic variant that represents a promising therapeutic target for multiple cancer types.

## AIMP2-DX2 and Chemoresistance in Ovarian Cancer

AIMP2-DX2 has been specifically implicated in chemoresistance development in ovarian cancer, a particularly aggressive malignancy in which acquired resistance to platinum-based chemotherapy represents a major clinical challenge[53]. Expression analysis of platinum-sensitive and chemoresistant ovarian cancer cell lines revealed substantially higher AIMP2-DX2 levels in chemoresistant cells compared to chemotherapy-sensitive cells[53]. The presence of elevated AIMP2-DX2 in chemoresistant cells suggests that this variant confers survival advantages in the context of cytotoxic drug exposure[53].

The mechanism of chemoresistance conferred by AIMP2-DX2 appears to involve suppression of both p53-dependent and TNF-α-dependent pro-apoptotic pathways. Because many ovarian cancer cells harbor inactivating mutations in p53, the capacity of AIMP2-DX2 to antagonize p53-mediated apoptosis may be particularly relevant in these tumors[53]. Furthermore, AIMP2-DX2's capacity to antagonize TRAF2-dependent TNF-α signaling provides an alternative route to apoptosis suppression in p53-mutant cells, suggesting that AIMP2-DX2 effectively neutralizes multiple independent pathways through which chemotherapy drugs induce apoptosis[53]. Notably, suppression of AIMP2-DX2 through RNA interference in chemoresistant ovarian cancer cells was able to restore or enhance sensitivity to platinum-based chemotherapy both in vitro and in in vivo xenograft models[53]. This finding directly demonstrates that AIMP2-DX2 functionally contributes to chemoresistance and suggests that AIMP2-DX2 inhibition could represent an effective adjunctive therapy to overcome chemoresistance in ovarian cancer[53].

## AIMP2 in Viral Infection: Influenza A Virus

AIMP2 has emerged as an important host factor in viral pathogenesis, particularly in the context of influenza A virus (IAV) infection[9][35][42][45][48][56]. During IAV infection, the viral non-structural protein NS2 (also known as nuclear export protein, NEP) physically interacts with host AIMP2 and protects AIMP2 from ubiquitin-mediated degradation that would normally occur through parkin-mediated pathways[9][45][48][56]. This viral manipulation of host AIMP2 degradation represents a sophisticated viral strategy to exploit host cell machinery for viral benefit[9][45][48][56].

The functional consequence of this AIMP2 protection is particularly clever: accumulated AIMP2 facilitates a critical step in the viral life cycle by promoting the switch from ubiquitination to SUMOylation of the viral matrix protein M1 (matrix protein 1)[9][45][48][56]. Ubiquitination and SUMOylation compete for the same lysine residue (K242) on M1, suggesting that AIMP2 promotes the recruitment of SUMOylation machinery while simultaneously preventing ubiquitin ligase access[9][45][48][56]. The SUMOylation of M1 is functionally important because it permits M1-mediated nuclear export of viral ribonucleoproteins (vRNPs), a critical step in the viral replication cycle that transfers newly synthesized viral genome copies from the nucleus to the cytoplasm for packaging into progeny virions[9][45][48][56]. AIMP2 overexpression enhances IAV replication, whereas AIMP2 knockdown reduces viral replication efficiency, directly demonstrating the virus's dependence on this host factor[9][45][48][56].

This discovery highlights how viruses have evolved mechanisms to hijack host cell proteins that normally function in cell-autonomous surveillance and apoptosis pathways. By protecting AIMP2 from degradation during viral infection, IAV cleverly repurposes a host tumor suppressor protein to facilitate its own replication. This finding also has practical implications for potential antiviral therapies targeting AIMP2-dependent steps of the viral life cycle.

## Leukodystrophy and AIMP2 Genetic Mutations

AIMP2 dysfunction has been associated with leukodystrophy, hypomyelinating, 17 (HLD17), a rare genetic neurological disorder characterized by defective myelination of the central nervous system[2][26][29]. Homozygous mutations in the AIMP2 gene located on chromosome 7p22 have been identified as the genetic cause of this disease[26][29]. Leukodystrophies are progressive neurological disorders affecting the white matter of the brain and spinal cord, and the identification of AIMP2 mutations as a cause of HLD17 underscores the critical importance of AIMP2 in neural development and myelin formation[26][29].

The molecular consequences of pathogenic AIMP2 mutations in HLD17 patients likely involve disruption of either the scaffolding functions of AIMP2 within the multi-tRNA synthetase complex or its stress-response functions, either of which could impair the survival and maturation of oligodendrocytes, the cells responsible for producing myelin[26][29]. The presence of rare genetic mutations in AIMP2 associated with monogenic neurological disease establishes AIMP2 as a protein whose normal function is essential for human health and whose dysfunction contributes to disease pathogenesis.

## Broader Regulatory Networks and Intertissue Signaling

Beyond the specific pathways discussed above, AIMP2 appears to be integrated into broader networks of cellular regulation through multiple additional mechanisms. AIMP2 has been identified as a substrate and modulator of heat shock protein 70 (HSP70), a molecular chaperone implicated in protein quality control and stress responses[27][31][35][42]. The N-terminal flexible region of AIMP2-DX2, spanning residues 24-34, binds to the substrate-binding domain of HSP70, and this interaction influences AIMP2-DX2 stability and function[27][31]. HSP70 binding can stabilize AIMP2-DX2 levels by interfering with degradation pathways, suggesting an additional layer of post-translational regulation that coordinates AIMP2 protein levels with cellular proteostasis status[27][31].

AIMP2 also appears to participate in cellular glucose metabolism and bioenergetic regulation through its association with glycolytic enzymes and its capacity to modulate metabolic flux[35][42]. The tight coordination between AIMP2's functions in protein synthesis (through the multi-tRNA synthetase complex) and its stress-response functions suggests that AIMP2 may serve as an integrator of information about the cell's biosynthetic and bioenergetic status. When biosynthetic demands are high and the cell requires efficient protein synthesis, AIMP2 remains stably associated with the multi-tRNA synthetase complex; when cellular stresses compromise biosynthetic capacity or threaten genome integrity, AIMP2 dissociates to activate stress-response pathways.

## Conclusion: AIMP2 as a Molecular Integrator of Cellular Stress and Protein Synthesis

AIMP2 represents one of the most comprehensively characterized examples of a multifunctional protein that coordinates distinct cellular processes through context-dependent subcellular localization and posttranslational modification[2][8][11][12][15][16][20][21][24][27][35][42]. In its canonical role as a component of the multi-tRNA synthetase complex, AIMP2 serves as a critical scaffolding protein essential for assembly and stability of the translational machinery[2][4][5][39][40]. This function is essential for efficient protein synthesis under normal cellular conditions when biosynthetic resources should be directed toward cell growth and proliferation[2][39][40].

However, in response to multiple forms of cellular stress—including DNA damage, inflammatory cytokines, and growth factor signaling—AIMP2 undergoes phosphorylation-dependent dissociation from the multi-tRNA synthetase complex and translocates to the nucleus or other cellular compartments to activate stress-response programs[8][12][15][16][19][22][32][35][42]. Through interactions with p53, TRAF2, FUBP1, and other signaling proteins, AIMP2 orchestrates pro-apoptotic and anti-proliferative responses that protect the organism from tumorigenesis and excessive cellular proliferation[8][11][15][16][19][22][32][35][42]. This functional duality—essentially serving as both a "housekeeping" component of the translation machinery under normal conditions and a "stress responder" capable of promoting cell death under adverse conditions—exemplifies how cells achieve regulatory sophistication through the multifunctionality of individual proteins[8][12][15][42].

The discovery of oncogenic AIMP2-DX2 variants and their selective expression in multiple cancer types highlights the clinical importance of maintaining proper AIMP2 function and appropriate AIMP2 dosage for tumor suppression[11][27][31][34][50][53]. The therapeutic potential of selectively inhibiting AIMP2-DX2 while sparing wild-type AIMP2 has been demonstrated in preclinical models, suggesting that targeting the balance between full-length and variant forms of AIMP2 may represent a promising therapeutic strategy for multiple cancers[11][27][31][34][50][53]. Similarly, the pathogenic accumulation of AIMP2 in Parkinson's disease and the potential neuroprotection afforded by reducing AIMP2 levels suggest that strategies to enhance AIMP2 degradation or reduce its pathogenic accumulation could represent novel therapeutic approaches for neurodegenerative diseases[12][21][24][35][42].

The fundamental mechanisms by which AIMP2 coordinates multiple signaling pathways through a relatively modest protein (approximately 35 kDa) remain incompletely understood, suggesting that continued investigation into AIMP2's structure, interactions, and regulation will yield further insights into how cells integrate information about biosynthetic capacity, genomic integrity, and stress status to make appropriate cell fate decisions. The multifaceted nature of AIMP2 function—encompassing roles in translation, tumor suppression, neuronal survival, immune regulation, and viral defense—establishes this protein as a central node in cellular homeostasis and disease pathogenesis whose full complexity has only recently begun to be appreciated.

## Citations

1. https://www.ncbi.nlm.nih.gov/gene?Db=gene&Cmd=DetailsSearch&Term=7965
2. https://www.genecards.org/cgi-bin/carddisp.pl?gene=AIMP2
3. https://www.uniprot.org/uniprotkb/Q13155/genomic-coordinates
4. https://www.uniprot.org/uniprotkb/Q13155/entry
5. https://www.ncbi.nlm.nih.gov/gene/7965
6. https://functionome.geneontology.org/gene/UniProtKB:Q13155
7. https://pmc.ncbi.nlm.nih.gov/articles/PMC11105487/
8. https://www.pnas.org/doi/10.1073/pnas.0800297105
9. https://pmc.ncbi.nlm.nih.gov/articles/PMC4301113/
10. https://www.uniprot.org/uniprotkb/Q8R010/entry
11. https://pmc.ncbi.nlm.nih.gov/articles/PMC11289502/
12. https://maayanlab.cloud/Harmonizome/gene/AIMP2
13. https://pmc.ncbi.nlm.nih.gov/articles/PMC6442029/
14. https://pmc.ncbi.nlm.nih.gov/articles/PMC2516205/
15. https://www.uniprot.org/uniprotkb/A0A287CX52/entry
16. https://aacrjournals.org/cancerres/article/76/11/3422/607891/Oncogenic-Mutation-of-AIMP2-p38-Inhibits-Its-Tumor
17. https://pubmed.ncbi.nlm.nih.gov/19584093/
18. https://pmc.ncbi.nlm.nih.gov/articles/PMC10790333/
19. https://pmc.ncbi.nlm.nih.gov/articles/PMC8082540/
20. https://journals.biologists.com/jcs/article/122/15/2710/20298/AIMP2-promotes-TNF-dependent-apoptosis-via
21. https://www.bmbreports.org/journal/view.html?doi=10.5483%2FBMBRep.2024-0053
22. https://pubmed.ncbi.nlm.nih.gov/23974709/
23. https://pmc.ncbi.nlm.nih.gov/articles/PMC10452860/
24. https://www.malacards.org/card/leukodystrophy_hypomyelinating_17
25. https://www.ncbi.nlm.nih.gov/Structure/cdd/cddsrv.cgi?uid=198309
26. https://www.ncbi.nlm.nih.gov/gtr/conditions/C4693912/
27. https://aacrjournals.org/cancerres/article/76/15/4559/613953/AIMP2-Controls-Intestinal-Stem-Cell-Compartments
28. https://pmc.ncbi.nlm.nih.gov/articles/PMC3069106/
29. https://pmc.ncbi.nlm.nih.gov/articles/PMC7382500/
30. https://www.ncbi.nlm.nih.gov/IEB/Research/Acembly/av.cgi?db=36a&c=geneid&q=7965
31. https://pmc.ncbi.nlm.nih.gov/articles/PMC6760448/
32. http://zymedi.com/wp-content/uploads/2023/02/AIMPs-for-homeostasis.pdf
33. https://academic.oup.com/nar/article/48/15/8740/5869352
34. https://www.proteinatlas.org/ENSG00000106305-AIMP2/subcellular
35. https://aacrjournals.org/cancerres/article-pdf/doi/10.1158/0008-5472.CAN-15-3255/2827165/0008-5472_can-15-3255v1.pdf
36. https://www.proteinatlas.org/ENSG00000106305-AIMP2
37. https://pubmed.ncbi.nlm.nih.gov/27197155/
38. https://journals.asm.org/doi/abs/10.1128/jvi.02170-14?doi=10.1128%2Fjvi.02170-14
39. https://v22.proteinatlas.org/ENSG00000106305-AIMP2/brain
40. https://journals.plos.org/plosgenetics/article?id=10.1371%2Fjournal.pgen.1001351
41. https://pmc.ncbi.nlm.nih.gov/articles/PMC9095880/
42. https://academic.oup.com/jmcb/article/4/3/164/914189
43. https://www.bmbreports.org/journal/view.html?uid=2027&vmd=Full
44. https://pmc.ncbi.nlm.nih.gov/articles/PMC10251411/
45. https://pubmed.ncbi.nlm.nih.gov/27262173/
46. https://febs.onlinelibrary.wiley.com/doi/pdf/10.1111/febs.16557
47. lung cancer stage