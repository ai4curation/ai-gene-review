---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-23T21:36:31.938343'
end_time: '2026-01-23T21:48:05.480200'
duration_seconds: 693.54
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: STOML1
  gene_symbol: STOML1
  uniprot_accession: Q9UBI4
  protein_description: 'RecName: Full=Stomatin-like protein 1; Short=SLP-1; AltName:
    Full=EPB72-like protein 1; AltName: Full=Protein unc-24 homolog; AltName: Full=Stomatin-related
    protein; Short=STORP;'
  gene_info: Name=STOML1; Synonyms=SLP1, UNC24; ORFNames=MSTP019;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the band 7/mec-2 family. .
  protein_domains: Band-7_stomatin-like. (IPR043202); Band_7. (IPR001107); Band_7/SPFH_dom_sf.
    (IPR036013); SCP2_sterol-bd_dom. (IPR003033); SCP2_sterol-bd_dom_sf. (IPR036527)
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
- **UniProt Accession:** Q9UBI4
- **Protein Description:** RecName: Full=Stomatin-like protein 1; Short=SLP-1; AltName: Full=EPB72-like protein 1; AltName: Full=Protein unc-24 homolog; AltName: Full=Stomatin-related protein; Short=STORP;
- **Gene Information:** Name=STOML1; Synonyms=SLP1, UNC24; ORFNames=MSTP019;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the band 7/mec-2 family. .
- **Key Domains:** Band-7_stomatin-like. (IPR043202); Band_7. (IPR001107); Band_7/SPFH_dom_sf. (IPR036013); SCP2_sterol-bd_dom. (IPR003033); SCP2_sterol-bd_dom_sf. (IPR036527)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "STOML1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'STOML1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **STOML1** (gene ID: STOML1, UniProt: Q9UBI4) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# STOML1 (Stomatin-like Protein 1) Research Report

## Introduction

STOML1 (Stomatin-like protein 1), also known as SLP-1 (Stomatin-Like Protein-1), is a human gene encoding a membrane-associated protein that belongs to the band 7/mec-2 family. According to UniProt (Q9UBI4), STOML1 is a 394 amino acid protein with a distinctive bipartite structure that sets it apart from other mammalian stomatin family members. The protein was first cloned and characterized in 1998 from a human cerebral cortex cDNA library, where it was identified as a brain-specific protein similar to the Caenorhabditis elegans protein UNC-24[seidel-1998-hslp1-cloning-abstract].

The stomatin family of proteins is remarkably conserved across all three domains of life, with bacterial and human homologs sharing approximately 50% amino acid identity[green-2008-slipins-phylogeny-abstract]. In mammals, five stomatin family proteins have been identified: stomatin, podocin, STOML1, STOML2, and STOML3[lapatsina-2011-stomatin-domain-proteins-abstract]. While all these proteins share the characteristic stomatin domain (also called the SPFH domain, for stomatin/prohibitin/flotillin/HflK-HflC), STOML1 is unique among mammalian stomatins in containing a C-terminal sterol carrier protein-2 (SCP-2) domain in addition to the stomatin domain[seidel-1998-hslp1-cloning-abstract][edqvist-2006-scp2-evolution-abstract]. This bipartite architecture suggests a dual functional capacity that links membrane association with lipid transfer capabilities.

## Domain Structure and Molecular Architecture

The STOML1 protein contains two functionally distinct domains that define its molecular properties. The N-terminal portion contains the Band-7/stomatin-like domain (IPR043202, IPR001107), which is the defining characteristic of the stomatin protein family. According to structural studies on related stomatin proteins, this domain enables membrane association and can form oligomeric structures, typically dimers or trimers[lapatsina-2011-stomatin-domain-proteins-abstract]. The stomatin domain of related proteins has been shown to associate with detergent-resistant membrane domains (lipid rafts), which are membrane microdomains enriched in cholesterol and sphingolipids[sedensky-2004-unc1-lipid-rafts-abstract].

Detailed structure-function analysis of human stomatin has revealed several important features that likely apply to the stomatin domain of STOML1[salzer-2017-stomatin-structure-summary]. The stomatin domain contains an intramembrane region that enables monotopic membrane insertion, along with CRAC/CARC cholesterol recognition motifs that enable cholesterol binding. A coiled-coil region is essential for oligomerization, while the PHB/SPFH core domain forms a conserved ellipsoid structure. Mutational studies have definitively established that stomatin is a cholesterol-binding protein, with multiple binding sites working cooperatively[salzer-2017-stomatin-structure-summary]. These structural features help explain how the stomatin domain of STOML1 may anchor the protein to cholesterol-rich membrane microdomains while engaging in oligomeric assembly.

The C-terminal portion of STOML1 contains the SCP-2 sterol-binding domain (IPR003033, IPR036527). This domain, which functions as a non-specific lipid transfer protein (nsLTP), is found in several human proteins involved in lipid metabolism. The SCP-2 domain has been shown in vitro to enhance the transfer of lipids, including sterols, between membranes[edqvist-2006-scp2-evolution-abstract]. Barnes and colleagues first noted this unusual combination when cloning the C. elegans ortholog UNC-24, proposing that the SCP-2 domain provides lipid carrier function while being tethered to membranes by the stomatin-like domain[barnes-1996-unc24-cloning-abstract].

The combination of a membrane-anchoring stomatin domain with a lipid transfer SCP-2 domain suggests that STOML1 may function in intracellular lipid trafficking, potentially facilitating the movement of sterols or other lipids between closely apposed membrane compartments[barnes-1996-unc24-cloning-abstract][mairhofer-2009-slp1-late-endosomes-abstract].

## Subcellular Localization

Detailed investigation of STOML1 subcellular localization was conducted by Mairhofer and colleagues, who demonstrated that this protein primarily localizes to the late endosomal compartment[mairhofer-2009-slp1-late-endosomes-abstract]. This localization pattern distinguishes STOML1 from stomatin itself, which is found both at the plasma membrane and in late endosomes. The exclusive late endosomal targeting of STOML1 is mediated by a GYXXΦ (where Φ represents a bulky, hydrophobic amino acid) sorting signal located at the N-terminus of the protein. When this signal is mutated, STOML1 instead localizes to the plasma membrane, demonstrating that the late endosomal targeting is an active, signal-dependent process rather than a default localization[mairhofer-2009-slp1-late-endosomes-abstract].

In sensory neurons, studies examining the expression of stomatin family proteins have found that STOML1, along with stomatin (STOM) and STOML3, is expressed in dorsal root ganglion neurons[gonzalez-velandia-2022-olfactory-stomatins-abstract]. Using a STOML1 null mutant mouse with a β-galactosidase reporter driven from the STOML1 gene locus, Kozlenkov and colleagues determined that STOML1 is expressed in at least 50% of dorsal root ganglion neurons[kozlenkov-2013-stoml1-asic-abstract]. In cultured DRG neurons, STOML1 colocalizes with lysosomal markers (Lysotracker Red), consistent with its late endosomal/lysosomal localization. Additionally, STOML1 is found in punctate structures along neuronal processes that may represent specialized membrane microdomains[kozlenkov-2013-stoml1-asic-abstract].

STOML1 also associates with detergent-resistant membranes, suggesting localization to lipid raft domains within late endosomes. Co-immunoprecipitation experiments demonstrated that STOML1 directly interacts with stomatin, and overexpression of STOML1 leads to redistribution of stomatin from the plasma membrane to late endosomes[mairhofer-2009-slp1-late-endosomes-abstract].

## Primary Molecular Functions

### Cholesterol and Lipid Transfer

The presence of the SCP-2 sterol-binding domain strongly suggests a role for STOML1 in intracellular lipid transport. Functional studies by Mairhofer and colleagues provided experimental evidence for this function. Under conditions where cholesterol efflux from late endosomes is blocked (using drugs like U18666A), STOML1 overexpression induces the formation of enlarged, cholesterol-filled, acidic vesicles in the perinuclear region. Importantly, this cholesterol accumulation phenotype requires an intact SCP-2 domain; expression of truncated STOML1 lacking the SCP-2 domain does not produce this effect[mairhofer-2009-slp1-late-endosomes-abstract]. These findings support a model in which STOML1 facilitates cholesterol transfer to late endosomes, potentially as part of the cellular machinery that regulates cholesterol homeostasis through the endosomal/lysosomal system.

### Ion Channel Modulation

A major functional theme emerging from studies of stomatin family proteins is their ability to modulate ion channel activity. STOML1 has been shown to profoundly inhibit acid-sensing ion channel 1a (ASIC1a), one of the proton-gated cation channels that plays important roles in pain sensation, synaptic plasticity, and ischemic cell death[kozlenkov-2013-stoml1-asic-abstract]. This inhibition is specific to the ASIC1a splice variant; STOML1 has no effect on the closely related ASIC1b. Additionally, STOML1 accelerates the inactivation kinetics of ASIC3[kozlenkov-2013-stoml1-asic-abstract].

The functional importance of this ASIC modulation was demonstrated in STOML1 knockout mice, where patch clamp recordings from DRG neurons revealed a trend toward larger proton-gated currents compared to wild-type controls. This effect was observed for both transient and sustained currents at different pH levels, consistent with an endogenous inhibitory function for STOML1 on proton-gated channels[kozlenkov-2013-stoml1-asic-abstract]. The SCP-2 domain appears to be important for this ion channel modulatory function, as truncated STOML1 lacking this domain showed altered effects[kozlenkov-2013-stoml1-asic-abstract].

This ion channel modulatory function is consistent with the broader role of stomatin family proteins in sensory transduction. Related proteins such as STOML3 modulate mechanosensitive channels including Piezo proteins, and the C. elegans stomatin MEC-2 is an essential component of the mechanotransduction complex in touch receptor neurons[lapatsina-2011-stomatin-domain-proteins-abstract][gonzalez-velandia-2022-olfactory-stomatins-abstract].

### Protein-Protein Interactions and Cell Cycle Regulation

Beyond its roles in lipid transfer and ion channel modulation, STOML1 has been identified as an interaction partner for several proteins involved in cell cycle regulation. A yeast two-hybrid screen identified STOML1 as a binding partner for Fbw7-γ, an F-box protein that functions as a specificity factor for the SCF ubiquitin ligase complex[zhang-2012-slp1-fbw7-abstract]. The SCF^Fbw7 complex targets several proteins required for cellular proliferation for ubiquitin-mediated destruction, including c-Myc, cyclin E, and other oncogenic substrates.

STOML1 binds to the unique N-terminal domain of Fbw7-γ. Overexpression of STOML1 inhibits the proteasome-dependent degradation of Fbw7-γ, leading to increased Fbw7-γ protein levels and consequently decreased c-Myc protein abundance. Interestingly, Cdk2 also binds both STOML1 and Fbw7-γ, and co-expression of Cdk2 with STOML1 prevents the stabilization of Fbw7-γ, suggesting that these proteins may have opposing regulatory functions[zhang-2012-slp1-fbw7-abstract]. The physiological significance of the STOML1-Fbw7-γ interaction remains to be fully elucidated, but it suggests a potential role for STOML1 in regulating cell proliferation through effects on the ubiquitin-proteasome system.

## Tissue Expression and Distribution

Northern blot and RNA dot blot analyses from the original cloning study revealed that STOML1 is predominantly expressed in the brain, with the highest levels detected in the frontal lobe, cerebral cortex, caudate nucleus, amygdala, temporal lobe, putamen, substantia nigra, and hippocampus[seidel-1998-hslp1-cloning-abstract]. This pattern of high expression in the basal ganglia reflects the evolutionary relationship to the C. elegans UNC-24 protein, which is required for normal locomotion.

In the peripheral nervous system, STOML1 is expressed in dorsal root ganglion neurons, where it has been implicated in modulating sensory neuron responses to acid stimulation[kozlenkov-2013-stoml1-asic-abstract]. Studies of the olfactory system found that STOML1 is expressed in olfactory sensory neurons, though at lower levels compared to stomatin and STOML3[gonzalez-velandia-2022-olfactory-stomatins-abstract].

## Evolutionary Conservation and the C. elegans UNC-24 Connection

STOML1 is the human ortholog of the C. elegans protein UNC-24, which was first identified in genetic screens for mutants affecting locomotion and anesthetic sensitivity[barnes-1996-unc24-cloning-abstract]. The conservation between these proteins extends beyond sequence similarity to include functional roles. In C. elegans, mutations in unc-24 cause uncoordinated locomotion and alter responses to volatile anesthetics[barnes-1996-unc24-cloning-abstract][sedensky-2004-unc1-lipid-rafts-abstract].

The role of UNC-24 in C. elegans has been extensively characterized as part of a genetic network controlling anesthetic sensitivity[morgan-2007-wormbook-anesthetics-summary]. This network includes three ion channel genes (unc-8, nca-1, nca-2), two stomatin-like genes (unc-1, unc-24), two gap junction genes (unc-7, unc-9), and one novel protein gene (unc-79). Within this network, UNC-24 controls the distribution of the UNC-1 stomatin protein, and UNC-1 localizes almost entirely within lipid rafts where it physically interacts with UNC-8, a degenerin channel protein. This suggests that anesthetic targets cluster in specialized membrane microdomains where multiple proteins work together to regulate neuronal responses to volatile anesthetics[morgan-2007-wormbook-anesthetics-summary]. The UNC-24 mutations suppress the hypersensitivity phenotypes of certain other mutations in this pathway, indicating that UNC-24 participates in modulating channel activity through its effects on protein localization.

Phylogenetic analysis has shown that STOML1/UNC-24-type proteins (containing both stomatin and SCP-2 domains) are present in nematodes and more advanced animals, suggesting that this fusion occurred early in animal evolution[green-2008-slipins-phylogeny-abstract][edqvist-2006-scp2-evolution-abstract]. The stomatin family as a whole arose from an ancient duplication event early in prokaryotic evolution, with subsequent diversification producing the multiple subfamilies found in mammals[green-2008-slipins-phylogeny-abstract].

Studies in C. elegans have demonstrated that UNC-24 localizes to lipid rafts in the nervous system and regulates the distribution of the related stomatin protein UNC-1[sedensky-2004-unc1-lipid-rafts-abstract]. In the absence of UNC-24, immunostaining of the nerve ring by anti-UNC-1 is abolished despite normal transcriptional levels of unc-1 mRNA, suggesting that UNC-24 affects the stability of UNC-1 protein rather than its expression[sedensky-2004-unc1-lipid-rafts-abstract]. This observation parallels the finding in mammalian cells that STOML1 overexpression leads to redistribution of stomatin from the plasma membrane to late endosomes, suggesting a conserved regulatory relationship between these stomatin family members.

## Disease Associations and Biomarker Potential

While no Mendelian disease has been directly attributed to STOML1 mutations, several studies have implicated STOML1 expression changes in cancer and other pathological conditions. Gene expression profiling studies have identified STOML1 among differentially expressed genes in various cancers including oral squamous cell carcinoma and colorectal cancer.

In nasopharyngeal carcinoma, high STOML1 protein expression was found to be significantly associated with improved overall survival and disease-free survival. Multivariate Cox analysis demonstrated that STOML1 expression is an independent prognostic factor, and combining STOML1 expression with TNM staging improved predictive accuracy for 5-year overall survival compared to either factor alone.

In oral squamous cell carcinoma, both STOML1 and STOML2 were found to be significantly overexpressed in tumor tissues compared to normal oral tissue, with both proteins positively associated with pathologic tumor stages. Immunohistochemistry showed that STOML1 was localized to the cell membrane, cytoplasm, and nucleus in these tumors.

Neuroimaging genetics studies in Alzheimer's disease have identified associations between STOML1 genetic variants (rs734854) and morphometric changes in brain structures including the hippocampus and insular cortex in normal control subjects.

## Open Questions

Several important questions about STOML1 function remain to be addressed:

1. **Substrate specificity of the SCP-2 domain:** While the SCP-2 domain can transfer sterols in vitro, the precise physiological substrates of STOML1-mediated lipid transfer in vivo remain unclear. Does STOML1 transfer cholesterol, other sterols, or additional lipid species?

2. **Mechanism of ion channel modulation:** How does STOML1 inhibit ASIC1a? Is this through direct binding to the channel, through effects on channel localization or trafficking, or through modulation of the local lipid environment? Why does the SCP-2 domain contribute to ion channel modulation?

3. **Relationship between lipid transfer and ion channel functions:** Are the lipid transfer and ion channel modulatory functions of STOML1 mechanistically connected, or are they independent activities of different protein domains?

4. **Physiological significance of stomatin interaction:** What is the functional consequence of STOML1-stomatin interaction? Does STOML1 regulate stomatin localization or activity, analogous to the UNC-24/UNC-1 relationship in C. elegans?

5. **Role in sensory transduction:** Given its expression in DRG neurons and effects on ASICs, does STOML1 play a role in pain sensation or other sensory modalities? STOML1 knockout mice have been generated but have not shown overt neurological phenotypes; more detailed sensory testing may reveal subtle deficits.

6. **Function in lipid homeostasis disorders:** The ability of STOML1 to induce cholesterol accumulation in late endosomes suggests potential relevance to diseases of cholesterol metabolism such as Niemann-Pick type C disease. Is STOML1 involved in normal cholesterol trafficking through late endosomes?

7. **Cancer biology implications:** What is the mechanistic basis for the prognostic significance of STOML1 expression in cancers? Is this related to its interaction with Fbw7-γ and potential effects on c-Myc levels?

8. **Anesthetic sensitivity:** Given the role of UNC-24 in anesthetic sensitivity in C. elegans, does STOML1 influence responses to volatile anesthetics in mammals? This could have clinical relevance.

## References

* **seidel-1998-hslp1-cloning:** Seidel G, Prohaska R. Molecular cloning of hSLP-1, a novel human brain-specific member of the band 7/MEC-2 family similar to Caenorhabditis elegans UNC-24. Gene. 1998 Dec 28;225(1-2):23-9. PMID: 9931417. DOI: https://doi.org/10.1016/s0378-1119(98)00532-0

* **mairhofer-2009-slp1-late-endosomes:** Mairhofer M, Steiner M, Salzer U, Prohaska R. Stomatin-like protein-1 interacts with stomatin and is targeted to late endosomes. J Biol Chem. 2009 Oct 16;284(42):29218-29. PMID: 19696025. PMCID: PMC2781465. DOI: https://doi.org/10.1074/jbc.M109.014993

* **kozlenkov-2013-stoml1-asic:** Kozlenkov A, Lapatsina L, Lewin GR, Smith ES. Subunit-specific inhibition of acid sensing ion channels by stomatin-like protein 1. J Physiol. 2014 Feb 15;592(4):557-69. PMID: 24247984. PMCID: PMC3934701. DOI: https://doi.org/10.1113/jphysiol.2013.258657

* **barnes-1996-unc24-cloning:** Barnes TM, Jin Y, Horvitz HR, Ruvkun G, Hekimi S. The Caenorhabditis elegans behavioral gene unc-24 encodes a novel bipartite protein similar to both erythrocyte band 7.2 (stomatin) and nonspecific lipid transfer protein. J Neurochem. 1996 Jul;67(1):46-57. PMID: 8667025. DOI: https://doi.org/10.1046/j.1471-4159.1996.67010046.x

* **lapatsina-2011-stomatin-domain-proteins:** Lapatsina L, Brand J, Poole K, Daumke O, Lewin GR. Stomatin-domain proteins. Eur J Cell Biol. 2011 Jun-Jul;91(6-7):240-5. PMID: 21501885. DOI: https://doi.org/10.1016/j.ejcb.2011.01.018

* **zhang-2012-slp1-fbw7:** Zhang W, MacDonald EM, Koepp DM. The stomatin-like protein SLP-1 and Cdk2 interact with the F-Box protein Fbw7-γ. PLoS One. 2012;7(10):e47736. PMID: 23082202. PMCID: PMC3474722. DOI: https://doi.org/10.1371/journal.pone.0047736

* **green-2008-slipins-phylogeny:** Green JB, Young JP. Slipins: ancient origin, duplication and diversification of the stomatin protein family. BMC Evol Biol. 2008 Feb 11;8:44. PMID: 18267007. PMCID: PMC2258279. DOI: https://doi.org/10.1186/1471-2148-8-44

* **sedensky-2004-unc1-lipid-rafts:** Sedensky MM, Siefker JM, Koh JY, Miller DM 3rd, Morgan PG. A stomatin and a degenerin interact in lipid rafts of the nervous system of Caenorhabditis elegans. Am J Physiol Cell Physiol. 2004 Aug;287(2):C468-74. PMID: 15102610. DOI: https://doi.org/10.1152/ajpcell.00182.2003

* **gonzalez-velandia-2022-olfactory-stomatins:** Gonzalez-Velandia KY, Hernandez-Clavijo A, Menini A, Dibattista M, Pifferi S. Expression pattern of Stomatin-domain proteins in the peripheral olfactory system. Sci Rep. 2022 Jul 6;12(1):11447. PMID: 35794236. PMCID: PMC9259621. DOI: https://doi.org/10.1038/s41598-022-15572-1

* **edqvist-2006-scp2-evolution:** Edqvist J, Blomqvist K. Fusion and fission, the evolution of sterol carrier protein-2. J Mol Evol. 2006 Mar;62(3):292-306. PMID: 16501878. DOI: https://doi.org/10.1007/s00239-005-0086-3

* **cullinan-2021-asic-regulation:** Cullinan MM, Klipp RC, Bankston JR. Regulation of acid-sensing ion channels by protein binding partners. Channels (Austin). 2021 Dec;15(1):635-647. PMID: 34704535. PMCID: PMC8555555. DOI: https://doi.org/10.1080/19336950.2021.1976946

* **salzer-2017-stomatin-structure:** Salzer U, Mairhofer M, Prohaska R. Structure-function analysis of human stomatin: A mutation study. PLoS One. 2017;12(6):e0178646. DOI: https://doi.org/10.1371/journal.pone.0178646

* **morgan-2007-wormbook-anesthetics:** Morgan PG, Bhambra S. C. elegans and volatile anesthetics. WormBook. 2007 Jan 31:1-10. URL: https://www.ncbi.nlm.nih.gov/books/NBK19697/


## Citations

1. barnes-1996-unc24-cloning-abstract.md
2. barnes-1996-unc24-cloning-summary.md
3. cullinan-2021-asic-regulation-abstract.md
4. edqvist-2006-scp2-evolution-abstract.md
5. gonzalez-velandia-2022-olfactory-stomatins-abstract.md
6. green-2008-slipins-phylogeny-abstract.md
7. kozlenkov-2013-stoml1-asic-abstract.md
8. kozlenkov-2013-stoml1-asic-summary.md
9. lapatsina-2011-stomatin-domain-proteins-abstract.md
10. mairhofer-2009-slp1-late-endosomes-abstract.md
11. mairhofer-2009-slp1-late-endosomes-summary.md
12. morgan-2007-wormbook-anesthetics-summary.md
13. salzer-2017-stomatin-structure-summary.md
14. sedensky-2004-unc1-lipid-rafts-abstract.md
15. seidel-1998-hslp1-cloning-abstract.md
16. zhang-2012-slp1-fbw7-abstract.md