---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-23T18:14:34.897655'
end_time: '2026-01-23T18:29:40.412793'
duration_seconds: 905.52
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: RAB9B
  gene_symbol: RAB9B
  uniprot_accession: Q9NP90
  protein_description: 'RecName: Full=Ras-related protein Rab-9B; EC=3.6.5.2 {ECO:0000250|UniProtKB:P62820};
    AltName: Full=Rab-9-like protein; Short=Rab-9L;'
  gene_info: Name=RAB9B {ECO:0000312|HGNC:HGNC:14090}; Synonyms=RAB9L;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the small GTPase superfamily. Rab family.
  protein_domains: P-loop_NTPase. (IPR027417); Rab9. (IPR041824); Small_GTP-bd. (IPR005225);
    Small_GTPase. (IPR001806); Ras (PF00071)
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
- **UniProt Accession:** Q9NP90
- **Protein Description:** RecName: Full=Ras-related protein Rab-9B; EC=3.6.5.2 {ECO:0000250|UniProtKB:P62820}; AltName: Full=Rab-9-like protein; Short=Rab-9L;
- **Gene Information:** Name=RAB9B {ECO:0000312|HGNC:HGNC:14090}; Synonyms=RAB9L;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the small GTPase superfamily. Rab family.
- **Key Domains:** P-loop_NTPase. (IPR027417); Rab9. (IPR041824); Small_GTP-bd. (IPR005225); Small_GTPase. (IPR001806); Ras (PF00071)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "RAB9B" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'RAB9B' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **RAB9B** (gene ID: RAB9B, UniProt: Q9NP90) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# RAB9B: Comprehensive Functional Annotation Report

## Introduction

RAB9B (Ras-related protein Rab-9B, also known as Rab-9-like protein or Rab-9L) is a member of the Rab family of small GTPases in humans, encoded by the RAB9B gene located on the X chromosome (Xq22.2). The protein is characterized by UniProt accession Q9NP90 and functions as a molecular switch in membrane trafficking, cycling between an active GTP-bound state and an inactive GDP-bound state [uniprot-q9np90-rab9b]. As a Rab family GTPase with EC number 3.6.5.2, RAB9B catalyzes the hydrolysis of GTP to GDP, a reaction that is central to its regulatory function in vesicular transport.

RAB9B is one of two human Rab9 paralogs, the other being RAB9A, which arose from a gene duplication event that occurred prior to the divergence of jawed vertebrates. While most of the functional characterization in the literature has focused on RAB9A (commonly referred to simply as "Rab9"), the high sequence homology between the two proteins suggests that RAB9B performs similar functions in late endosome-to-trans-Golgi network (TGN) transport [wu-2014-rab9a-rutbc2-structure-abstract]. Indeed, biochemical data demonstrate that Rab9B can bind to the effector RUTBC2 in a manner similar to Rab9A, supporting functional equivalence in at least some pathways [shu-2012-rutbc2-abstract].

The primary function attributed to Rab9 proteins is the recycling of mannose 6-phosphate receptors (MPRs) from late endosomes back to the TGN, a critical step in lysosome biogenesis [stenmark-2001-lysosome-biogenesis-abstract]. This transport pathway ensures that MPRs, which deliver newly synthesized lysosomal hydrolases from the Golgi to endosomes, are efficiently recycled for additional rounds of enzyme delivery. Additionally, Rab9 has been implicated in non-canonical (Atg5/Atg7-independent) autophagy, where it mediates fusion of isolation membranes with vesicles derived from the trans-Golgi and late endosomes [nishida-2009-alternative-autophagy-abstract].

## Molecular Function and GTPase Activity

RAB9B functions as a small GTPase, belonging to the Ras superfamily of GTP-binding proteins. The protein contains the canonical structural features of this family, including a P-loop NTPase fold, characteristic switch regions (switch I and switch II), and a C-terminal prenylation motif that enables membrane association. The crystal structure of Rab9 has been determined at 1.25-Å resolution, revealing a nucleotide binding fold consisting of a six-stranded β-sheet surrounded by five α-helices with a tightly bound nucleotide in the active site [chen-2004-rab9-structure-abstract]. The structure for GppNHp-bound RAB9B has been deposited in the Protein Data Bank with identifier 2OCB.

The GTPase cycle of RAB9B is regulated by guanine nucleotide exchange factors (GEFs) that promote GDP-to-GTP exchange, and GTPase-activating proteins (GAPs) that accelerate the intrinsic GTP hydrolysis rate. In its active GTP-bound state, RAB9B adopts a conformation that allows it to recruit specific effector proteins to membrane surfaces. The switch I and switch II regions undergo substantial conformational changes between the GDP- and GTP-bound states, enabling selective recognition by effector proteins [chen-2004-rab9-structure-abstract]. Notably, structure-based sequence alignment reveals that while Rab9 shares conserved active site residues with other Rab proteins (implying a common catalytic mechanism), it contains seven regions with significantly different conformations that may contribute to its specificity for particular effectors [chen-2004-rab9-structure-abstract].

The cycling of Rab proteins between membranes and cytosol is further regulated by GDP dissociation inhibitor (GDI), which extracts the GDP-bound form of the Rab from membranes and maintains it in a soluble cytosolic pool. Upon encountering the appropriate GEF at target membranes, GDI releases the Rab, allowing nucleotide exchange and stable membrane association.

A critical prerequisite for Rab membrane association is C-terminal prenylation. Like most Rab family members, RAB9B is modified by the attachment of geranylgeranyl groups to C-terminal cysteine residues. This reaction is catalyzed by Rab geranylgeranyltransferase (RabGGTase) in conjunction with Rab escort protein (REP). The majority of Rab proteins contain C-terminal motifs ending in CC, CxC, or CCxx, where both cysteines are geranylgeranylated. Dual prenylation is essential for proper membrane targeting; mono-prenylated Rab proteins are mistargeted to the endoplasmic reticulum and are non-functional. The geranylgeranyl groups are masked by GDI when Rabs are cytosolic, and exposed upon membrane insertion. The affinity of prenylated Rab9 for GDI is in the nanomolar range, indicating tight regulation of the cytosolic pool.

## Subcellular Localization and Membrane Trafficking

RAB9B, like its paralog RAB9A, localizes primarily to late endosomes, where it occupies a distinct membrane microdomain that is segregated from Rab7-containing regions [barbero-2002-rab9-visualization-abstract]. Videomicroscopy of living cells expressing fluorescently tagged Rab9 revealed that Rab9 and Rab7 domains exhibit only approximately 15% overlap on late endosomal membranes, suggesting compartmentalized functionality within these organelles. This "macaroon cookie" arrangement of distinct Rab domains supports the model that different Rab proteins organize functionally distinct regions of the same organelle [barbero-2002-rab9-visualization-abstract].

The Rab9 microdomain is enriched in mannose 6-phosphate receptors, with approximately 40% of Rab9-positive structures containing detectable CI-MPR compared to only 16% of Rab7-positive structures [barbero-2002-rab9-visualization-abstract]. This selective enrichment is consistent with Rab9's function in organizing cargo for retrograde transport to the TGN. Small Rab9-positive vesicles have been directly observed budding from late endosomes and fusing with TGN structures marked by galactosyltransferase, establishing vesicles rather than tubules as the primary transport carriers in this pathway [barbero-2002-rab9-visualization-abstract].

The transport of Rab9-bearing vesicles is microtubule-dependent, with vesicle velocities of approximately 0.75 μm/s under normal conditions. Treatment with nocodazole (a microtubule-depolymerizing agent) reduced vesicle velocity to approximately 0.2 μm/s, indicating that while microtubules enhance transport efficiency, the pathway remains viable even without intact microtubules [barbero-2002-rab9-visualization-abstract].

According to the Human Protein Atlas, RAB9B shows membranous and cytoplasmic expression in most tissues, with the highest expression observed in intercalated discs of heart myocytes [human-protein-atlas-rab9b]. At the RNA level, heart muscle shows the highest expression (20.1 nTPM), followed by cerebellum (16.7 nTPM), basal ganglia (9.9 nTPM), and seminal vesicle (8.9 nTPM). In the brain, expression is relatively uniform across regions with the highest levels in the hypothalamus (21.7 nTPM). This tissue distribution pattern differs somewhat from RAB9A, which shows more ubiquitous expression with particular enrichment in glandular and lymphoid cells.

## Interacting Partners and Effector Proteins

The function of RAB9B in membrane trafficking is mediated through interactions with multiple effector proteins that carry out specific steps in vesicle formation, transport, and fusion. The best-characterized effectors are TIP47, p40, GCC185, and RUTBC2.

**TIP47 (Tail-Interacting Protein of 47 kDa):** TIP47 is a cytosolic adaptor protein essential for the transport of mannose 6-phosphate receptors from endosomes to the TGN. Rab9 recruits TIP47 from the cytosol to late endosome surfaces, where it binds to the cytoplasmic domains of MPRs with enhanced affinity [hanna-2002-tip47-rab9-abstract]. The affinity of TIP47 for Rab9-GTPγS is remarkably high (Kd = 95 nM), approximately 10-fold stronger than TIP47's intrinsic affinity for MPR cytoplasmic domains [ganley-2004-rab9-endosome-size-abstract]. This cooperative binding mechanism ensures efficient cargo selection during vesicle formation. Strikingly, TIP47 is also essential for Rab9 stability; depletion of TIP47 reduces Rab9 half-life fourfold (from 32 to 8 hours), representing the first evidence that an effector interaction is essential for Rab protein stability [ganley-2004-rab9-endosome-size-abstract].

**p40:** p40 is a 40-kDa protein that binds Rab9-GTP with approximately fourfold preference over Rab9-GDP [pfeffer-2009-multiple-routes-abstract]. Unlike TIP47, p40 does not interact with Rab7 or K-Ras, indicating selectivity for the Rab9 pathway. Anti-p40 antibodies inhibit MPR transport in vitro, confirming its functional importance. p40 and Rab9 show synergy in stimulating MPR transport, consistent with a model where they act together to drive transport vesicle docking [pfeffer-2009-multiple-routes-abstract].

**GCC185:** GCC185 is a TGN-localized golgin (coiled-coil tethering protein) that functions as a Rab9 effector required for MPR recycling [reddy-2006-gcc185-abstract]. GCC185 binds Rab9 with strong preference for its active, GTP-bound conformation. Depletion of GCC185 causes approximately 75% inhibition of MPR recycling and results in accumulation of MPRs in peripheral vesicular structures containing Rab9 [reddy-2006-gcc185-abstract]. GCC185 is proposed to participate in docking of late endosome-derived, Rab9-bearing transport vesicles at the TGN. Unlike other golgins, GCC185 binds poorly to Arl1 GTPase and instead uses direct Rab9 interaction for its tethering function.

**RUTBC2:** RUTBC2 is a TBC domain-containing protein that binds to both Rab9A and Rab9B in their GTP-bound states [shu-2012-rutbc2-abstract]. The crystal structure of the Rab9A-RUTBC2 complex reveals that RUTBC2 uses a pleckstrin homology domain fold to interact with the switch and interswitch regions of Rab9A [wu-2014-rab9a-rutbc2-structure-abstract]. Importantly, while RUTBC2 is a Rab9 effector, it is not a GAP for Rab9 itself; instead, it functions as a GAP for Rab36 and Rab34 [shu-2012-rutbc2-abstract]. This suggests a functional connection between Rab9-mediated receptor recycling pathways and Rab36-regulated lysosomal positioning, representing a potential coordination mechanism in membrane trafficking. RUTBC2 is highly enriched in brain tissue.

## Role in Lysosome Biogenesis and Autophagy

The primary physiological function of Rab9 proteins is ensuring efficient lysosome biogenesis through proper sorting of lysosomal enzymes. Mannose 6-phosphate receptors bind newly synthesized lysosomal hydrolases in the Golgi complex and deliver them to endosomes. Following cargo release in the acidic endosomal environment, MPRs must recycle back to the TGN for additional rounds of enzyme delivery [stenmark-2001-lysosome-biogenesis-abstract]. Expression of dominant-negative Rab9 (S21N mutation) strongly inhibits MPR recycling, demonstrating the importance of Rab9 GTPase activity for this pathway.

Depletion of Rab9 from cells has multiple phenotypic consequences: late endosome diameter decreases by approximately 45% (from 0.76 to 0.42 μm), with concomitant reduction in the numbers of multilamellar and dense tubule-containing structures [ganley-2004-rab9-endosome-size-abstract]. The remaining late endosomes and lysosomes become more tightly clustered near the nucleus, implicating Rab9 in endosome positioning through motor protein recruitment. Importantly, multivesicular endosome numbers remain unchanged, and EGF receptor degradation rates are unaffected, indicating that Rab9 depletion specifically affects the retrograde transport pathway without globally disrupting endosome function [ganley-2004-rab9-endosome-size-abstract].

Beyond its role in constitutive MPR recycling, Rab9 has been implicated in non-canonical autophagy. The landmark discovery by Nishida and colleagues demonstrated that cells lacking ATG5 or ATG7 can still form autophagosomes and perform autophagic protein degradation under certain stress conditions through an alternative, Rab9-dependent mechanism [nishida-2009-alternative-autophagy-abstract]. In this Atg5/Atg7-independent pathway, autophagosomes are generated by Rab9-mediated fusion of isolation membranes (phagophores) with vesicles derived from the trans-Golgi and late endosomes. Unlike conventional autophagy, LC3 lipidation does not occur in this alternative pathway. This form of autophagy has physiological importance in specific contexts, including degradation of secretory proteins such as insulin granules and mitochondrial elimination in reticulocytes [nishida-2009-alternative-autophagy-abstract].

## Role in Cholesterol Homeostasis and Niemann-Pick Type C Disease

Beyond its well-established role in MPR recycling, Rab9 has been implicated in cholesterol trafficking and homeostasis within the endolysosomal system. This connection is particularly evident in Niemann-Pick type C (NPC) disease, an autosomal recessive neurodegenerative disorder characterized by massive accumulation of cholesterol and glycosphingolipids within late endosomes and lysosomes. Approximately 95% of NPC patients harbor mutations in the NPC1 gene, which encodes a large late endosomal protein with 13 transmembrane domains involved in cholesterol export.

Studies by Ganley and Pfeffer demonstrated that cholesterol accumulation directly affects Rab9 function in NPC1-deficient cells [ganley-2006-npc-cholesterol-abstract]. Endogenous Rab9 levels were elevated 1.8-fold in NPC cells compared to wild-type cells, and its half-life increased from 44 to 70 hours, indicating that Rab9 accumulation results from impaired protein turnover rather than increased synthesis. The underlying mechanism involves cholesterol-mediated stabilization of Rab9 on late endosome membranes. In normal cells, over 90% of Rab9 can be extracted from membranes by GDI, but in NPC cells, only 35% is extractable. This GDI resistance correlates directly with membrane cholesterol concentration, as demonstrated using artificial liposomes [ganley-2006-npc-cholesterol-abstract].

The functional consequence of Rab9 sequestration is disruption of the retrograde transport pathway. In NPC1-depleted cells, cation-dependent mannose 6-phosphate receptors are missorted to lysosomes for degradation, with CD-MPR levels dropping by approximately 70%. This creates a vicious cycle: impaired Rab9 function leads to defective MPR recycling, which compromises lysosomal enzyme delivery and further exacerbates the lysosomal storage phenotype.

Importantly, Rab9 overexpression provides therapeutic benefit in NPC disease models. GFP-tagged Rab9 expression rescued CD-MPR degradation and relieved cholesterol accumulation in NPC cells. Furthermore, protein transduction of Rab9 reduced intracellular cholesterol in NPC2 fibroblasts and cultured mouse NPC1 neurons [ganley-2006-npc-cholesterol-abstract]. These findings suggest that enhancing Rab9-mediated vesicular export could provide a therapeutic bypass for cholesterol removal from late endosomes, representing a potential treatment strategy for NPC disease. The Rab9 pathway also mediates transport of lactosylceramide (LacCer) from the plasma membrane to the Golgi apparatus; overexpression of wild-type Rab9 corrects abnormal LacCer transport in several sphingolipid storage disease cell types, further supporting its therapeutic potential.

## Comparison with RAB9A

RAB9B and RAB9A arose from a gene duplication that occurred prior to the divergence of jawed vertebrates, and both proteins share high sequence homology. Phylogenetic analysis shows highly supported sister clades comprising Rab9a and Rab9b sequences from fish, amphibians, birds, and mammals. The functional redundancy of these paralogs is supported by biochemical data showing that RAB9B can bind to effector RUTBC2 in a manner similar to RAB9A [wu-2014-rab9a-rutbc2-structure-abstract].

However, the two paralogs show distinct tissue expression patterns. While RAB9A is ubiquitously expressed with enrichment in glandular and lymphoid cells, RAB9B shows enhanced expression in heart muscle and is also expressed in brain regions including cerebellum and basal ganglia [human-protein-atlas-rab9b]. In the nervous system, RAB9A is abundantly present in oligodendroglial lineage cells, whereas RAB9B does not exhibit a specific profile across brain cell types. This differential expression pattern suggests potential tissue-specific or context-dependent roles, though the functional significance remains to be fully elucidated.

Notably, patients with deletions encompassing the PLP1 gene (causing Pelizaeus-Merzbacher disease, a hypomyelinating leukodystrophy) often have concomitant deletion of RAB9B due to the antiparallel arrangement of these genes on chromosome Xq22. Analysis of a patient with a 73-kb deletion including both PLP1 and RAB9B suggests that "lack of RAB9B may not be deleterious in itself," possibly due to functional compensation by RAB9A [ohira-2012-plp1-rab9b-deletion-abstract].

## Disease Associations and Potential Therapeutic Relevance

RAB9B has been identified as one of several Rab proteins that serve as substrates for LRRK2 (Leucine-Rich Repeat Kinase 2), whose mutations comprise the predominant genetic cause of familial Parkinson's disease [steger-2016-lrrk2-rab-phosphoproteomics-abstract]. In vitro kinase assays demonstrated that LRRK2 phosphorylates RAB9B along with other Rab proteins including Rab1A/B, Rab3C, Rab8A/B, Rab10, Rab23, and Rab35. LRRK2 phosphorylates these substrates on an evolutionarily conserved residue in the switch II domain, and pathogenic LRRK2 mutations increase this phosphorylation, strongly decreasing Rab affinity for regulatory proteins including GDIs [steger-2016-lrrk2-rab-phosphoproteomics-abstract]. Dysregulated Rab phosphorylation by hyperactive LRRK2 has been shown to induce neurotoxicity in primary neurons and dopaminergic neuron degeneration in vivo. Two therapeutic approaches targeting LRRK2 (an antisense oligonucleotide and a kinase inhibitor) are currently in clinical trials for Parkinson's disease.

The role of Rab9 in viral replication also presents therapeutic opportunities. The crystal structure of Rab9 was characterized as part of a structure-based drug design program because Rab9 has been identified as a key cellular component for HIV-1, Ebola, Marburg, and measles virus replication [chen-2004-rab9-structure-abstract]. This suggests that small molecule inhibitors targeting Rab9 could potentially serve as broad-spectrum antiviral agents, though no such compounds have yet advanced to clinical development.

RAB9B is associated through chromosomal deletion with Pelizaeus-Merzbacher Disease and Spastic Paraplegia 2, X-Linked, though the primary causative gene in these disorders is PLP1 rather than RAB9B itself [ohira-2012-plp1-rab9b-deletion-abstract]. The functional consequences of RAB9B loss in these patients remain unclear due to potential compensation by RAB9A.

## Open Questions

Despite substantial progress in understanding Rab9 biology, several important questions remain regarding RAB9B specifically:

1. **Functional specificity versus redundancy:** While RAB9B and RAB9A share effector interactions and presumably similar functions, are there contexts where RAB9B performs unique or specialized roles? The distinct tissue expression patterns (cardiac enrichment for RAB9B) suggest possible tissue-specific functions that remain to be characterized.

2. **GEF and GAP identification:** The specific GEF(s) responsible for activating RAB9B have not been definitively identified. Similarly, while RUTBC2 binds Rab9 as an effector, the GAP(s) that inactivate Rab9 proteins remain incompletely characterized.

3. **LRRK2 phosphorylation consequences:** While RAB9B is phosphorylated by LRRK2, the specific functional consequences of this modification for RAB9B activity and localization have not been extensively studied. Understanding this relationship may provide insights into Parkinson's disease pathogenesis.

4. **Relative contributions to autophagy:** The role of Rab9 in non-canonical autophagy has been established, but whether RAB9A and RAB9B contribute differentially to this pathway remains unknown.

5. **Cardiac function:** Given the enhanced expression of RAB9B in cardiac tissue, particularly in intercalated discs of heart myocytes, does RAB9B play specific roles in cardiac physiology or pathology?

6. **Consequences of RAB9B loss:** Patients with deletions of both PLP1 and RAB9B exist, but isolating the contribution of RAB9B loss from the dominant PLP1 phenotype is challenging. Generation of RAB9B-specific knockout models would help clarify the physiological requirements for this gene.

7. **Neural cell-type specific roles:** While RAB9A is enriched in oligodendrocytes, RAB9B shows a mixed neuronal expression pattern. The functional significance of this differential distribution in the nervous system warrants investigation.

## References

1. **[chen-2004-rab9-structure-abstract]** Chen L, DiGiammarino E, Zhou XE, Wang Y, Toh D, Hodge TW, Meehan EJ. High resolution crystal structure of human Rab9 GTPase: a novel antiviral drug target. J Biol Chem. 2004 Sep 17;279(38):40204-8. PMID: 15263003. DOI: 10.1074/jbc.M407114200. PDB: 1WMS.

2. **[barbero-2002-rab9-visualization-abstract]** Barbero P, Bittova L, Bhattacharya S (Pfeffer lab). Visualization of Rab9-mediated vesicle transport from endosomes to the trans-Golgi in living cells. J Cell Biol. 2002;156(3):511-8. PMID: 11827983. PMCID: PMC2173336.

3. **[ganley-2004-rab9-endosome-size-abstract]** Ganley IG, Carroll K, Hanna L (Pfeffer lab). Rab9 GTPase Regulates Late Endosome Size and Requires Effector Interaction for Its Stability. Mol Biol Cell. 2004;15(12):5420-30. PMID: 15456905. PMCID: PMC532021. DOI: 10.1091/mbc.e04-08-0747.

4. **[reddy-2006-gcc185-abstract]** Reddy JV et al. A Functional Role for the GCC185 Golgin in Mannose 6-Phosphate Receptor Recycling. Mol Biol Cell. 2006;17(10):4353-63. PMID: 16885419. PMCID: PMC1635343. DOI: 10.1091/mbc.e06-02-0153.

5. **[shu-2012-rutbc2-abstract]** Shu DL, Lu P et al. RUTBC2 Protein, a Rab9A Effector and GTPase-activating Protein for Rab36. J Biol Chem. 2012;287(26):22333-40. PMID: 22637480. PMCID: PMC3391118. DOI: 10.1074/jbc.M112.358127.

6. **[wu-2014-rab9a-rutbc2-structure-abstract]** Wu M, Gan Y et al. Crystal Structure of the Rab9A-RUTBC2 RBD Complex Reveals the Molecular Basis for the Binding Specificity of Rab9A with RUTBC2. Structure. 2014;22(10):1408-20. PMID: 25220469. DOI: 10.1016/j.str.2014.08.005.

7. **[steger-2016-lrrk2-rab-phosphoproteomics-abstract]** Steger M, Tonelli F, Ito G et al. Phosphoproteomics reveals that Parkinson's disease kinase LRRK2 regulates a subset of Rab GTPases. eLife. 2016;5:e12813. PMID: 26824392. PMCID: PMC4769169. DOI: 10.7554/eLife.12813.

8. **[nishida-2009-alternative-autophagy-abstract]** Nishida Y, Arakawa S, Fujitani K et al. Discovery of Atg5/Atg7-independent alternative macroautophagy. Nature. 2009;461(7264):654-8. PMID: 19794493. DOI: 10.1038/nature08455.

9. **[stenmark-2001-lysosome-biogenesis-abstract]** Riederer MA, Lehner PJ et al. Lysosome biogenesis requires Rab9 function and receptor recycling from endosomes to the trans-Golgi network. J Cell Biol. 1994;125(3):573-82. PMID: 7909812. DOI: 10.1083/jcb.125.3.573.

10. **[hanna-2002-tip47-rab9-abstract]** Hanna L, Carroll K (Pfeffer lab). Purification and Analysis of TIP47 Function in Rab9-Dependent Mannose 6-Phosphate Receptor Trafficking. Methods Enzymol. 2006;403:191-205. PMID: 16473602. DOI: 10.1016/S0076-6879(05)03016-2.

11. **[pfeffer-2009-multiple-routes-abstract]** Pfeffer SR. Multiple routes of protein transport from endosomes to the trans Golgi network. FEBS Lett. 2009;583(23):3811-6. PMID: 19879873. PMCID: PMC2787657. DOI: 10.1016/j.febslet.2009.10.075.

12. **[ohira-2012-plp1-rab9b-deletion-abstract]** Ohira M, Nagata Y et al. Clinical and genetic characterization of a 2-year-old boy with complete PLP1 deletion. Brain Dev. 2012;34(10):853-7. DOI: 10.1016/j.braindev.2012.01.013.

13. **[ganley-2006-npc-cholesterol-abstract]** Ganley IG, Pfeffer SR. Cholesterol accumulation sequesters Rab9 and disrupts late endosome function in NPC1-deficient cells. J Biol Chem. 2006;281(26):17890-9. PMID: 16644737. PMCID: PMC3650718. DOI: 10.1074/jbc.M601679200.

14. **[uniprot-q9np90-rab9b]** UniProt Consortium. UniProtKB entry Q9NP90 - RAB9B. https://www.uniprot.org/uniprotkb/Q9NP90/entry

15. **[human-protein-atlas-rab9b]** Human Protein Atlas. RAB9B protein expression summary. https://www.proteinatlas.org/ENSG00000123570-RAB9B


## Citations

1. barbero-2002-rab9-visualization-abstract.md
2. chen-2004-rab9-structure-abstract.md
3. ganley-2004-rab9-endosome-size-abstract.md
4. ganley-2006-npc-cholesterol-abstract.md
5. hanna-2002-tip47-rab9-abstract.md
6. human-protein-atlas-rab9b.md
7. nishida-2009-alternative-autophagy-abstract.md
8. ohira-2012-plp1-rab9b-deletion-abstract.md
9. pfeffer-2009-multiple-routes-abstract.md
10. reddy-2006-gcc185-abstract.md
11. shu-2012-rutbc2-abstract.md
12. steger-2016-lrrk2-rab-phosphoproteomics-abstract.md
13. stenmark-2001-lysosome-biogenesis-abstract.md
14. uniprot-q9np90-rab9b.md
15. wu-2014-rab9a-rutbc2-structure-abstract.md