---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-23T18:45:01.265995'
end_time: '2026-01-23T19:00:58.716151'
duration_seconds: 957.45
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: RASA1
  gene_symbol: RASA1
  uniprot_accession: P20936
  protein_description: 'RecName: Full=Ras GTPase-activating protein 1; Short=GAP;
    Short=GTPase-activating protein; Short=RasGAP; AltName: Full=Ras p21 protein activator;
    AltName: Full=p120GAP;'
  gene_info: Name=RASA1; Synonyms=GAP, RASA;
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
citation_count: 11
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P20936
- **Protein Description:** RecName: Full=Ras GTPase-activating protein 1; Short=GAP; Short=GTPase-activating protein; Short=RasGAP; AltName: Full=Ras p21 protein activator; AltName: Full=p120GAP;
- **Gene Information:** Name=RASA1; Synonyms=GAP, RASA;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** C2_dom. (IPR000008); C2_domain_sf. (IPR035892); PH-like_dom_sf. (IPR011993); PH_domain. (IPR001849); Ras_GTPase. (IPR039360)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "RASA1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'RASA1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **RASA1** (gene ID: RASA1, UniProt: P20936) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# RASA1 (p120GAP): A Comprehensive Review of Ras GTPase-Activating Protein 1

## Introduction and Summary

RASA1 (Ras GTPase-activating protein 1), also known as p120GAP, RasGAP, or p120-RasGAP, is a 120 kDa cytoplasmic protein that serves as a critical negative regulator of Ras signaling. The protein was the first GTPase-activating protein discovered for the Ras family of small GTPases, with its identification by Trahey and McCormick in 1987 representing a fundamental advance in understanding how Ras signaling is controlled in cells [trahey-1987-gap-discovery-abstract]. RASA1 functions by dramatically accelerating the intrinsic GTPase activity of Ras proteins, converting them from the active GTP-bound state to the inactive GDP-bound state and thereby terminating Ras-mediated mitogenic signaling [scheffzek-2019-rasgap-review-summary].

The primary enzymatic function of RASA1 is to catalyze GTP hydrolysis on Ras proteins through a mechanism involving an "arginine finger" that stabilizes the transition state of the hydrolysis reaction [scheffzek-1997-ras-rasgap-complex-summary]. This catalytic activity enhances the rate of GTP hydrolysis by approximately 10^5-fold compared to the intrinsic rate, making it an extraordinarily efficient regulator of Ras activity [scheffzek-2019-rasgap-review-summary]. Beyond its catalytic function, RASA1 serves as a multifunctional scaffold protein that participates in signal transduction through its N-terminal protein-protein interaction domains, connecting receptor tyrosine kinase signaling to downstream effectors [pamonsinlapatham-2009-rasgap-multiinteracting-summary].

RASA1 is ubiquitously expressed and essential for embryonic development, as demonstrated by the embryonic lethality of Rasa1 knockout mice at embryonic day 10.5 due to severe vascular and neuronal defects [henkemeyer-1995-rasgap-knockout-abstract]. In humans, germline loss-of-function mutations in RASA1 cause capillary malformation-arteriovenous malformation syndrome (CM-AVM1), a vascular disorder characterized by multiple capillary malformations and, in some cases, fast-flow arteriovenous malformations [chen-2023-ephb4-rasa1-summary]. These genetic findings have provided crucial insights into the biological importance of RASA1-mediated Ras regulation in vascular development and maintenance.

## Domain Architecture and Protein Structure

RASA1 is a modular protein comprising multiple functional domains that enable both its catalytic and scaffolding functions. From the N-terminus to the C-terminus, the protein contains: two SH2 (Src homology 2) domains separated by a single SH3 (Src homology 3) domain, followed by a pleckstrin homology (PH) domain, a C2 domain, and finally the C-terminal GAP catalytic module [scheffzek-2019-rasgap-review-summary]. This domain organization positions RASA1 uniquely among the ten mammalian RasGAPs, as it is the only family member to contain SH2 domains [stiegler-2022-sh2-tandem-summary].

The GAP catalytic module itself consists of two structural domains: the central catalytic domain (GAPc) and an extra domain (GAPex). The minimal catalytic fragment, termed GAP-334 (residues 714-1047), was the first GTPase-activating protein to have its structure determined by X-ray crystallography [scheffzek-1996-gap334-structure-summary]. This structure revealed an elongated, exclusively helical protein representing a novel protein fold at the time of its discovery in 1996. The GAPex domain, while structurally conserved, is dispensable for catalytic activity, with all residues essential for GAP function residing within the GAPc domain [scheffzek-2019-rasgap-review-summary].

The N-terminal SH2-SH3-SH2 cassette enables RASA1 to interact with phosphotyrosine-containing proteins, including activated receptor tyrosine kinases such as PDGFR (platelet-derived growth factor receptor), EGFR (epidermal growth factor receptor), and EphB receptors [chen-2023-ephb4-rasa1-summary]. Structural studies have revealed that the two SH2 domains can engage dual phosphotyrosine residues in a single binding partner through a "bidentate" binding mode, achieving remarkably tight binding affinities of approximately 10 nM—a 15-30 fold enhancement compared to single SH2 domain engagement [stiegler-2022-sh2-tandem-summary]. Notably, the C-terminal SH2 domain employs an unusual "FLVR-unique" phosphotyrosine binding mechanism in which the conserved arginine residue makes an intramolecular salt bridge rather than directly coordinating the phosphotyrosine [stiegler-2022-sh2-tandem-summary].

The PH domain of RASA1 contributes to membrane localization through its ability to bind phosphoinositide lipids, particularly phosphatidylinositol 4,5-bisphosphate (PIP2). PH domains function by recruiting their host proteins to membranes enriched in specific phosphoinositides, thereby positioning RASA1 in proximity to membrane-bound Ras proteins. The C2 domain, located immediately proximal to the GAP catalytic module, was initially presumed to serve primarily as a calcium-dependent phospholipid-binding module for membrane targeting. However, recent research has revealed an unexpected direct role for the C2 domain in augmenting catalytic activity through interaction with the Ras allosteric lobe, with residue R707 at the center of an evolutionarily conserved surface critical for this function [scheffzek-2019-rasgap-review-summary].

## Enzymatic Mechanism and Catalysis

The primary biochemical function of RASA1 is to accelerate GTP hydrolysis by Ras proteins through a well-characterized mechanism involving transition state stabilization. The discovery of this activity by Trahey and McCormick in 1987 demonstrated that a cytoplasmic protein could stimulate the GTPase activity of normal N-Ras p21 by more than 200-fold in vitro [trahey-1987-gap-discovery-abstract]. Subsequent structural and biochemical studies have revealed that the rate enhancement achieved by RasGAPs can reach 10^5-fold, converting the slow intrinsic hydrolysis rate of Ras into a rapid switch mechanism suitable for controlling cellular signaling [scheffzek-2019-rasgap-review-summary].

The catalytic mechanism centers on the "arginine finger" provided by the GAP domain. In RASA1, this essential residue is Arg789, which inserts into the active site of Ras-GTP and contacts the β/γ phosphate region of the bound nucleotide [scheffzek-1997-ras-rasgap-complex-summary]. The importance of this residue is demonstrated by mutagenesis studies showing that even conservative substitution of arginine to lysine reduces GAP activity by three orders of magnitude [scheffzek-2019-rasgap-review-summary]. The arginine finger serves dual roles: it helps position the nucleophilic water molecule for attack on the γ-phosphate, and it stabilizes the developing negative charge during the transition state of phosphoryl transfer.

A seminal contribution to understanding this mechanism came from the crystal structure of the Ras-RasGAP complex in the presence of aluminum fluoride, which mimics the transition state of the GTP hydrolysis reaction [scheffzek-1997-ras-rasgap-complex-summary]. This structure, solved at 2.5 Å resolution, revealed that aluminum fluoride forms a pentagonal bipyramidal geometry with the fluorides forming the trigonal base and two apical oxygen ligands. The arginine finger from RASA1 contacts one of the fluorides, demonstrating how the GAP neutralizes developing charges on the γ-phosphate during the phosphoryl transfer reaction.

The structure also explains why oncogenic Ras mutations at positions G12, G13, and Q61 are insensitive to GAP-mediated stimulation. Glutamine 61 is essential for proper positioning of the nucleophilic water molecule, and mutations at this position virtually eliminate GAP sensitivity [scheffzek-1997-ras-rasgap-complex-summary]. Glycine 12 is positioned near both the arginine finger and Gln61 in the active site; substitution of larger residues at this position sterically interferes with proper arginine finger insertion and prevents formation of the catalytically competent complex. This structural understanding explains the fundamental observation of Trahey and McCormick that the GAP activity does not affect oncogenic Ras mutants [trahey-1987-gap-discovery-abstract].

## Substrate Specificity

RASA1 functions as a GAP for classical Ras isoforms (H-Ras, K-Ras, and N-Ras) without significant preference among these three proteins. The catalytic domains of RASA1 and neurofibromin (NF1), the two best-characterized RasGAPs, interact with H-Ras, N-Ras, and K-Ras with similar efficiency [scheffzek-2019-rasgap-review-summary]. This broad specificity toward classical Ras proteins positions RASA1 as a general negative regulator of Ras signaling rather than an isoform-specific modulator.

Interestingly, RASA1 displays differential activity toward R-Ras compared to classical Ras proteins. Kinetic measurements have shown that RASA1 actually has higher affinity for R-Ras (EC50 ~3.9 nM) compared to H-Ras (EC50 ~23 nM), representing approximately 6-fold selectivity toward R-Ras [scheffzek-2019-rasgap-review-summary]. This contrasts with GAP1m, another RasGAP, which preferentially stimulates classical Ras GTPase activity over R-Ras. The biological significance of this selectivity pattern remains an area of ongoing investigation.

Comparison with neurofibromin reveals important differences in Ras binding properties despite similar catalytic mechanisms. The affinity of neurofibromin for Ras-GTP is 50- to 100-fold higher than that of RASA1, while the kinetics of association and dissociation are much faster for RASA1 [scheffzek-2019-rasgap-review-summary]. This suggests that neurofibromin may function as a more persistent Ras regulator once bound, while RASA1 rapidly cycles on and off Ras-GTP in a manner more suited to dynamic signaling regulation. Despite these kinetic differences, both proteins utilize the same fundamental arginine finger mechanism for catalysis.

## Subcellular Localization and Membrane Recruitment

RASA1 is predominantly a cytosolic protein that undergoes regulated recruitment to cellular membranes where it can access its substrate, membrane-bound Ras-GTP. Multiple mechanisms contribute to RASA1 membrane localization, reflecting the importance of spatial control for its function as a Ras regulator. According to the Human Protein Atlas, RASA1 shows primary localization to vesicles and the basal body, with additional presence in the cytosol [scheffzek-2019-rasgap-review-summary].

Growth factor stimulation triggers translocation of RASA1 from the cytoplasm to the plasma membrane. This recruitment is facilitated by the SH2 and SH3 protein interaction domains, which mediate binding to activated receptor tyrosine kinases and their associated signaling complexes [chen-2023-ephb4-rasa1-summary]. The SH2 domains recognize specific phosphotyrosine motifs on receptors such as PDGFR, EGFR, and EphB4. In the case of EphB4, RASA1 binds through SH2 domain recognition of a pair of autophosphorylated tyrosine residues in the receptor juxtamembrane region [chen-2023-ephb4-rasa1-summary].

Beyond receptor-mediated recruitment, RASA1 membrane targeting involves the adaptor protein Annexin A6. This calcium-dependent membrane-binding protein interacts constitutively with RASA1 in the cytosol and promotes its Ca2+-dependent recruitment to the plasma membrane upon stimulation [grewal-2005-annexin-a6-abstract]. Annexin A6 acts as a scaffold that assembles RASA1-Ras complexes at the membrane, thereby facilitating Ras inactivation. Expression of Annexin A6 reduces EGF-induced Ras and ERK activation, while suppression of Annexin A6 enhances Ras signaling, demonstrating the physiological importance of this mechanism [grewal-2005-annexin-a6-abstract].

The PH domain provides direct lipid-binding capacity through recognition of phosphoinositides such as PIP2. Additionally, the C2 domain may contribute to membrane association, although recent evidence suggests its primary role may be in direct catalytic enhancement rather than membrane targeting [scheffzek-2019-rasgap-review-summary]. An alternative model proposes that RASA1 is targeted to Ras-GTP through recognition of membrane lipids generated during EphB4 signaling rather than solely through direct protein-protein interaction [chen-2023-ephb4-rasa1-summary].

## Role in Ras-MAPK Signaling

RASA1 functions as a critical negative regulator of the Ras-MAPK (mitogen-activated protein kinase) signaling pathway, one of the most important signal transduction cascades controlling cell proliferation, differentiation, and survival. In this pathway, activated Ras-GTP binds to and activates the serine-threonine kinase RAF, which phosphorylates MEK1/2, which in turn phosphorylates and activates ERK (extracellular signal-regulated kinase) [chen-2023-ephb4-rasa1-summary]. By converting Ras-GTP to Ras-GDP, RASA1 terminates signaling through this entire cascade.

A particularly well-characterized context for RASA1 function is the EPHB4-RASA1 signaling axis in endothelial cells. The receptor tyrosine kinase EphB4 communicates with RASA1 to inhibit Ras activation in endothelial cells, with knockdown of RASA1 in human umbilical vein endothelial cells blocking EphB4's ability to inhibit the Ras-MAPK pathway [chen-2023-ephb4-rasa1-summary]. This functional relationship positions EPHB4 as an upstream regulator that dampens Ras-MAPK signaling through RASA1-dependent mechanisms, rather than activating downstream signaling like conventional growth factor receptors.

The importance of this regulatory relationship is demonstrated by the consequences of EPHB4 or RASA1 deficiency. Loss of either protein results in greatly augmented activation of ERK MAPK in endothelial cells during developmental angiogenesis [chen-2023-ephb4-rasa1-summary]. During lymphangiogenesis, EPHB4 and RASA1 cooperate to limit the duration of Ras-MAPK signaling induced by VEGF-C binding to VEGFR3. In the absence of either protein, prolonged Ras-MAPK signaling leads to lymphatic endothelial cell apoptosis [chen-2023-ephb4-rasa1-summary].

RASA1 also participates in crosstalk between Ras and Rho GTPase signaling pathways through its interaction with p190RhoGAP. The tandem SH2 domains of RASA1 engage dual phosphotyrosine residues on p190RhoGAP with high affinity, potentially coordinating the activities of these two major small GTPase families [stiegler-2022-sh2-tandem-summary]. This bidentate binding mechanism may function as a highly selective signaling gate, ensuring that Ras-Rho pathway coordination occurs only under specific phosphorylation conditions.

## Role in Apoptosis Regulation

Beyond its canonical function as a Ras-GTPase activating protein, RASA1 plays an unexpected role in regulating cell survival and apoptosis through a mechanism involving caspase-mediated cleavage. This function positions RASA1 as a stress sensor that can modulate cell fate decisions depending on the intensity of apoptotic stimuli.

During the early phases of apoptosis, RASA1 is proteolytically cleaved by caspase-3 at two distinct sites [wen-1998-rasgap-cleavage-abstract]. Initial cleavage at position 455 generates an N-terminal fragment (fragment N, amino acids 1-455) and a C-terminal fragment (fragment C, amino acids 456-1047). Under conditions of high caspase activity, fragment N is further cleaved at position 157, generating smaller fragments [yang-2001-caspase-rasgap-summary]. Remarkably, the biological outcomes of this cleavage depend critically on the extent of processing.

At low levels of caspase-3 activity, such as might occur during mild cellular stress, partial cleavage of RASA1 generates an antiapoptotic response [yang-2001-caspase-rasgap-summary]. Fragment N, produced by initial cleavage at position 455, activates the prosurvival Akt kinase in a Ras-dependent manner, preventing further amplification of caspase activity and allowing cells to recover from transient stress. This partial cleavage mechanism is essential for cell survival under stress conditions, as cells expressing an uncleavable RASA1 mutant cannot activate Akt, cannot prevent amplification of caspase-3 activity, and eventually undergo apoptosis even in response to mild stress [yang-2001-caspase-rasgap-summary].

In contrast, at high levels of caspase activity, further cleavage at position 157 abolishes the antiapoptotic capacity of fragment N, and the resulting fragments become proapoptotic [yang-2001-caspase-rasgap-summary]. Fragment C expressed alone can induce apoptosis, although this effect is blocked when fragment N is co-expressed. This elegant "apoptostat" mechanism allows RASA1 to function as a sensor of caspase activity levels, promoting survival under mild stress but permitting apoptosis when cellular damage is severe.

Additional complexity in this pathway emerged from studies showing that fragment N also functions as an NF-κB inhibitor by promoting nuclear export of NF-κB. Cells unable to generate fragment N display increased NF-κB activation upon stress, and knock-in mice expressing uncleavable RASA1 show exaggerated NF-κB activation when their epidermis is treated with inflammatory stimuli. Thus, RASA1 cleavage serves to modulate multiple stress-responsive signaling pathways beyond its primary role in Ras regulation.

## Physiological Functions and Disease Associations

The essential role of RASA1 in mammalian development was established by gene targeting studies in mice. Homozygous deletion of Rasa1 results in embryonic lethality at approximately embryonic day 10.5, with affected embryos displaying severe defects in both yolk sac and embryonic vascular systems [henkemeyer-1995-rasgap-knockout-abstract]. The vascular abnormalities reflect impaired ability of endothelial cells to organize into properly structured vascular networks. In addition to vascular phenotypes, Rasa1 null embryos exhibit extensive neuronal apoptosis, indicating that RASA1-mediated Ras regulation is important for neuronal survival during development [henkemeyer-1995-rasgap-knockout-abstract].

Double mutant studies combining Rasa1 and Nf1 (neurofibromin) deficiency demonstrate amplified phenotypic abnormalities, indicating that these two RasGAPs act together to regulate Ras activity during embryonic development [henkemeyer-1995-rasgap-knockout-abstract]. This genetic interaction suggests that while there may be some functional redundancy between RasGAPs, each contributes uniquely to maintaining appropriate levels of Ras signaling in specific developmental contexts.

In humans, germline heterozygous loss-of-function mutations in RASA1 cause capillary malformation-arteriovenous malformation syndrome type 1 (CM-AVM1), which accounts for approximately 70% of CM-AVM cases [chen-2023-ephb4-rasa1-summary]. The remaining 30% (CM-AVM2) are caused by mutations in EPHB4, the upstream receptor that signals through RASA1. The clinical features are indistinguishable between these two genetic forms, consistent with their function in a shared signaling pathway. CM-AVM is characterized by multiple small capillary malformations, typically 1-2 cm in diameter and often surrounded by a pale halo, that appear on the face and limbs and increase in number with age. Some affected individuals also develop fast-flow arteriovenous malformations (AVMs) or arteriovenous fistulas in the skin, muscle, bone, spine, or brain.

Parkes Weber syndrome represents a related but more severe manifestation within the RASA1 mutation spectrum. This condition is characterized by multiple micro-arteriovenous fistulas associated with segmental overgrowth of soft tissue and skeletal components affecting a limb. Originally considered a sporadic, non-genetic condition, Parkes Weber syndrome is now recognized as part of the CM-AVM spectrum caused by RASA1 mutations. Germline inactivating variants in RASA1 are detected in 50-85% of individuals with Parkes Weber syndrome. The focal nature and variable expressivity of vascular lesions in these conditions supports a two-hit model, wherein complete loss of RASA1 function through biallelic inactivation (the inherited germline mutation plus a somatic "second hit") is required for lesion development. This model has been confirmed by identification of somatic RASA1 mutations in lesional tissue from affected patients. Notably, both germline and postzygotic (mosaic) RASA1 mutations can lead to CM-AVM and Parkes Weber syndrome phenotypes.

Most pathogenic RASA1 mutations are nonsense mutations, splice site substitutions, or frameshift mutations that result in premature stop codons and predicted loss of protein through nonsense-mediated RNA decay [chen-2023-ephb4-rasa1-summary]. The disease mechanism appears to involve haploinsufficiency, with a "second hit" model proposed for lesion development. According to this model, somatic mutation of the inherited wild-type RASA1 allele in endothelial cells during development creates RASA1-null cells that drive lesion formation [chen-2023-ephb4-rasa1-summary]. This model has been supported by identification of biallelic RASA1 inactivation in lesional tissue.

Beyond CM-AVM, RASA1 mutations have been associated with vein of Galen arteriovenous malformation (VGAM), lymphatic-related hydrops fetalis, central conducting lymphatic anomaly, and lymphedema [chen-2023-ephb4-rasa1-summary]. RASA1 and EPHB4 are required for the development of all three types of vascular valves—lymphatic vessel valves, lymphovenous valves, and venous valves—and maintenance of lymphatic vessel valves in adults depends upon continued RASA1 catalytic activity.

The mechanism by which RASA1 deficiency causes vascular malformations has been partially elucidated. Dysregulated Ras-MAPK activation in RASA1-deficient endothelial cells impairs secretion of collagen IV, a critical extracellular matrix component. Excessive MAPK signaling leads to increased collagen proline and lysine hydroxylation, which impairs proper collagen folding and cellular export [chen-2023-ephb4-rasa1-summary]. Retention of misfolded collagen in the endoplasmic reticulum triggers the unfolded protein response and subsequent endothelial cell apoptosis. This mechanistic understanding has identified potential therapeutic targets, including MAPK pathway inhibitors, collagen modification inhibitors, and ER chaperone agonists.

## Open Questions

Despite extensive research on RASA1 spanning more than three decades since its discovery, several important questions remain unresolved:

1. **Context-dependent signaling outcomes**: EphB4-RASA1 signaling inhibits the Ras-MAPK pathway in endothelial cells but activates this pathway in other cell types such as hepatic stellate cells [chen-2023-ephb4-rasa1-summary]. The molecular basis for these opposite outcomes in different cellular contexts remains unclear.

2. **C2 domain catalytic contribution**: While recent work has demonstrated that the C2 domain directly augments GAP catalytic activity through interaction with Ras, the precise structural mechanism and the physiological importance of this enhancement require further investigation.

3. **Tissue-specific phenotypes**: Some families with RASA1 mutations present with lymphatic-only phenotypes despite the two-hit model predicting vascular involvement [chen-2023-ephb4-rasa1-summary]. The basis for this phenotypic variability is not understood.

4. **Therapeutic window for established lesions**: It remains unclear whether vascular malformations that have already formed maintain dysregulated Ras-MAPK signaling, which would be necessary for pathway-targeted therapies to be effective [chen-2023-ephb4-rasa1-summary].

5. **Functional specificity among RasGAPs**: Ten RasGAPs exist in mammals, yet RASA1 deficiency produces specific phenotypes despite the presence of other family members. Understanding how specificity is achieved, and whether compensation occurs, remains an open area of investigation.

6. **Integration of catalytic and scaffolding functions**: RASA1 serves both as an enzyme and as a multidomain scaffold for signaling complexes. How these two functions are coordinated, and whether they can be separated therapeutically, warrants further study.

## References

1. **[trahey-1987-gap-discovery-abstract]** Trahey M, McCormick F. A cytoplasmic protein stimulates normal N-ras p21 GTPase, but does not affect oncogenic mutants. *Science*. 1987 Oct 23;238(4826):542-5. PMID: 2821624. DOI: 10.1126/science.2821624

2. **[scheffzek-1996-gap334-structure-summary]** Scheffzek K, Lautwein A, Kabsch W, Ahmadian MR, Wittinghofer A. Crystal structure of the GTPase-activating domain of human p120GAP and implications for the interaction with Ras. *Nature*. 1996 Dec 12;384(6609):591-6. PMID: 8955277. DOI: 10.1038/384591a0

3. **[scheffzek-1997-ras-rasgap-complex-summary]** Scheffzek K, Ahmadian MR, Kabsch W, Wiesmuller L, Lautwein A, Schmitz F, Wittinghofer A. The Ras-RasGAP complex: structural basis for GTPase activation and its loss in oncogenic Ras mutants. *Science*. 1997 Jul 18;277(5324):333-8. PMID: 9219684. DOI: 10.1126/science.277.5324.333. PDB: 1WQ1

4. **[henkemeyer-1995-rasgap-knockout-abstract]** Henkemeyer M, Rossi DJ, Holmyard DP, Puri MC, Mbamalu G, Harpal K, Shih TS, Jacks T, Pawson T. Vascular system defects and neuronal apoptosis in mice lacking ras GTPase-activating protein. *Nature*. 1995 Oct 26;377(6551):695-701. PMID: 7477259. DOI: 10.1038/377695a0

5. **[grewal-2005-annexin-a6-abstract]** Grewal T, Evans R, Rentero C, Tebar F, Cubells L, de Diego I, Kirchhoff MF, Hughes WE, Heeren J, Rye KA, Rinninger F, Daly RJ, Pol A, Enrich C. Annexin A6 stimulates the membrane recruitment of p120GAP to modulate Ras and Raf-1 activity. *Oncogene*. 2005 Sep 1;24(38):5809-20. PMID: 15940262. DOI: 10.1038/sj.onc.1208743

6. **[pamonsinlapatham-2009-rasgap-multiinteracting-summary]** Pamonsinlapatham P, Hadj-Slimane R, Lepelletier Y, Allain B, Toccafondi M, Garbay C, Raynaud F. p120-Ras GTPase activating protein (RasGAP): a multi-interacting protein in downstream signaling. *Biochimie*. 2009 Mar;91(3):320-8. PMID: 19022332. DOI: 10.1016/j.biochi.2008.10.010

7. **[scheffzek-2019-rasgap-review-summary]** Scheffzek K, Shivalingaiah G. Ras-Specific GTPase-Activating Proteins-Structures, Mechanisms, and Interactions. *Cold Spring Harb Perspect Med*. 2019 Mar 1;9(3):a031500. PMID: 29610147. PMCID: PMC6396337. DOI: 10.1101/cshperspect.a031500

8. **[stiegler-2022-sh2-tandem-summary]** Stiegler AL, Vish KJ, Boggon TJ. Tandem engagement of phosphotyrosines by the dual SH2 domains of p120RasGAP. *Structure*. 2022 Dec 1;30(12):1603-1614.e5. PMID: 36323259. PMCID: PMC9722645. DOI: 10.1016/j.str.2022.10.009. PDB: 8DGQ

9. **[chen-2023-ephb4-rasa1-summary]** Chen D, Van der Ent MA, Lartey NL, King PD. EPHB4-RASA1-Mediated Negative Regulation of Ras-MAPK Signaling in the Vasculature: Implications for the Treatment of EPHB4- and RASA1-Related Vascular Anomalies in Humans. *Pharmaceuticals (Basel)*. 2023 Jan 23;16(2):165. PMID: 37259315. PMCID: PMC9959185. DOI: 10.3390/ph16020165

10. **[wen-1998-rasgap-cleavage-abstract]** Wen LP, Madani K, Martin GA, Rosen GD. Proteolytic cleavage of ras GTPase-activating protein during apoptosis. *Cell Death Differ*. 1998 Sep;5(9):729-34. PMID: 10200531. DOI: 10.1038/sj.cdd.4400409

11. **[yang-2001-caspase-rasgap-summary]** Yang JY, Widmann C. Antiapoptotic Signaling Generated by Caspase-Induced Cleavage of RasGAP. *Mol Cell Biol*. 2001 Aug;21(16):5346-58. PMID: 11463818. PMCID: PMC87258. DOI: 10.1128/MCB.21.16.5346-5358.2001


## Citations

1. chen-2023-ephb4-rasa1-summary.md
2. grewal-2005-annexin-a6-abstract.md
3. henkemeyer-1995-rasgap-knockout-abstract.md
4. pamonsinlapatham-2009-rasgap-multiinteracting-summary.md
5. scheffzek-1996-gap334-structure-summary.md
6. scheffzek-1997-ras-rasgap-complex-summary.md
7. scheffzek-2019-rasgap-review-summary.md
8. stiegler-2022-sh2-tandem-summary.md
9. trahey-1987-gap-discovery-abstract.md
10. wen-1998-rasgap-cleavage-abstract.md
11. yang-2001-caspase-rasgap-summary.md