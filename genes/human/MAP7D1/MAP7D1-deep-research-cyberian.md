---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-22T22:03:47.899127'
end_time: '2026-01-22T22:17:26.956812'
duration_seconds: 819.06
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: MAP7D1
  gene_symbol: MAP7D1
  uniprot_accession: Q3KQU3
  protein_description: 'RecName: Full=MAP7 domain-containing protein 1; AltName: Full=Arginine/proline-rich
    coiled-coil domain-containing protein 1; AltName: Full=Proline/arginine-rich coiled-coil
    domain-containing protein 1;'
  gene_info: Name=MAP7D1; Synonyms=KIAA1187, PARCC1, RPRC1; ORFNames=PP2464;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the MAP7 family. .
  protein_domains: MAP7_domain-containing. (IPR051483); MAP7_fam. (IPR008604); MAP7
    (PF05672)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 9
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q3KQU3
- **Protein Description:** RecName: Full=MAP7 domain-containing protein 1; AltName: Full=Arginine/proline-rich coiled-coil domain-containing protein 1; AltName: Full=Proline/arginine-rich coiled-coil domain-containing protein 1;
- **Gene Information:** Name=MAP7D1; Synonyms=KIAA1187, PARCC1, RPRC1; ORFNames=PP2464;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the MAP7 family. .
- **Key Domains:** MAP7_domain-containing. (IPR051483); MAP7_fam. (IPR008604); MAP7 (PF05672)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "MAP7D1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'MAP7D1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **MAP7D1** (gene ID: MAP7D1, UniProt: Q3KQU3) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# MAP7D1 (MAP7 Domain-Containing Protein 1): Comprehensive Functional Analysis

## Introduction and Summary

MAP7D1 (MAP7 domain-containing protein 1; UniProt Q3KQU3) is a human protein encoded by the MAP7D1 gene located on chromosome 1p34.3. As a member of the MAP7 family of microtubule-associated proteins, MAP7D1 functions primarily as a microtubule-stabilizing protein with roles in cytoskeleton organization, intracellular transport, cell migration, neuronal development, and more recently discovered, DNA damage response [sun-2022-map7d1-map7d2-abstract][bensenor-2023-map7-ddr-abstract]. The protein consists of 846 amino acids in mouse (and similar length in human) and contains two coiled-coil domains: an N-terminal microtubule-binding domain and a C-terminal MAP7 domain that mediates interaction with kinesin-1 motor proteins [tymanskyj-2019-map7-kinesin-abstract].

## Protein Domain Architecture

The MAP7D1 protein exhibits the characteristic domain organization conserved across the MAP7 family. The N-terminal region contains an alpha-helical coiled-coil motif that constitutes the microtubule-binding domain (MTBD). This region is highly positively charged, with all MAP7 family members having isoelectric points (pI) above 10.0 in their N-terminal domains, facilitating electrostatic interactions with the negatively charged microtubule surface [montalvo-ortiz-2019-map7d2-axon-abstract]. The N-terminal domain of MAP7D1 is sufficient for microtubule binding, as demonstrated by truncation studies showing that all N-terminal containing constructs and chimeras retain microtubule binding activity.

The C-terminal region contains the conserved MAP7 domain, which mediates binding to the kinesin-1 motor protein KIF5B. Interestingly, the MAP7 domains across family members show variable isoelectric points: MAP7 has a pI of 7.6, MAP7D1 has a pI of 9.1, MAP7D2 has a pI of 5.8, and MAP7D3 has a pI of 9.9 [montalvo-ortiz-2019-map7d2-axon-abstract]. This variation may contribute to differential binding properties and functional specialization among family members. The C-terminal domains of both MAP7D1 and MAP7D2 show diffuse localization throughout neurons and accumulate at axon tips when expressed alone, suggesting the N-terminal microtubule-binding domain is required for proper subcellular targeting.

Between the N-terminal and C-terminal domains lies an unstructured linker region that contributes to kinesin-1 activation through allosteric mechanisms. MAP7D1 shows the highest sequence conservation with MAP7 among the family members, consistent with their overlapping expression patterns and functional redundancy [koizumi-2017-dclk1-map7d1-abstract].

The MAP7 family in mammals comprises four paralogous proteins encoded by distinct genes: MAP7 (also known as ensconsin or E-MAP-115), MAP7D1, MAP7D2, and MAP7D3 [tymanskyj-2019-map7-kinesin-abstract]. These proteins share conserved domain architecture and exhibit functional redundancy in kinesin-1 activation, yet display distinct tissue expression patterns and specialized roles in specific cellular contexts. MAP7D1, along with MAP7, is broadly expressed across human tissues with particular enrichment in skeletal muscle (267.9 nTPM), heart muscle (91.0 nTPM), and spinal cord (87.4 nTPM), and localizes predominantly to the somatodendritic compartment in neurons, contrasting with the axon-localized MAP7D2 and MAP7D3 [montalvo-ortiz-2019-map7d2-axon-abstract].

## Molecular Function: Microtubule Stabilization

The primary molecular function of MAP7D1 is microtubule stabilization, though the mechanism by which it achieves this differs from its paralog MAP7D2. While MAP7D2 directly binds microtubules through its N-terminal region and stabilizes them through this direct interaction, MAP7D1 operates through an indirect mechanism centered on maintaining levels of acetylated tubulin [sun-2022-map7d1-map7d2-abstract]. Tubulin acetylation, specifically on lysine 40 of alpha-tubulin, is a post-translational modification enriched on stable, long-lived microtubules and serves as a marker of microtubule stability. The requirement for MAP7D1 in maintaining acetylated tubulin levels suggests it may regulate either the enzymes responsible for tubulin acetylation (such as alpha-tubulin acetyltransferase 1, ATAT1) or protect acetylated microtubules from deacetylation or depolymerization.

Studies using knockdown approaches in N1-E115 mouse neuronal cells demonstrated that loss of either MAP7D1 or MAP7D2 results in comparable reductions in overall microtubule stabilization without affecting EB1-decorated dynamic microtubule plus-ends [sun-2022-map7d1-map7d2-abstract]. However, MAP7D2 loss specifically decreased resistance to the microtubule-destabilizing agent nocodazole while leaving acetylated and detyrosinated stable microtubule populations intact, whereas MAP7D1 loss specifically reduced acetylated tubulin levels. This functional specialization within the MAP7 family demonstrates how related proteins have evolved distinct mechanisms to achieve similar cellular outcomes.

## Kinesin-1 Recruitment and Intracellular Transport

A critical function of MAP7D1, shared with other MAP7 family members, is the positive regulation of kinesin-1 motor proteins. Unlike most microtubule-associated proteins such as tau and MAP2 that inhibit kinesin-1-driven motility, MAP7 family proteins promote kinesin-1 binding to microtubules and enhance motor protein processivity [tymanskyj-2019-map7-kinesin-abstract][pan-2019-map7-organelle-abstract]. This makes the MAP7 family unique regulators of microtubule-based transport.

All four mammalian MAP7 family members bind kinesin-1, with MAP7, MAP7D1, and MAP7D3 acting redundantly in HeLa cells to enable kinesin-1-dependent transport [tymanskyj-2019-map7-kinesin-abstract]. The triple knockout of these three proteins is not viable, highlighting their essential role in cellular function. MAP7 proteins promote kinesin-1 binding through two complementary mechanisms: directly, through the N-terminal microtubule-binding domain and unstructured linker region, and indirectly, through an allosteric effect mediated by the C-terminal kinesin-binding domain [tymanskyj-2019-map7-kinesin-abstract].

Structural studies of MAP7 have revealed a sophisticated regulatory mechanism. The microtubule-binding domain (MTBD) forms an extended alpha-helix of approximately 112 amino acids that binds between the protofilament ridge and the site of lateral contact on the microtubule lattice [siahaan-2022-map7-structure-abstract]. Intriguingly, this binding site partially overlaps with the kinesin-1 binding site, creating a competitive relationship. At low MAP7 concentrations, the projection domain tethers kinesin-1 to the microtubule, preventing motor dissociation and allowing it to rebind at neighboring sites through "tethered diffusion." However, at high MAP7 concentrations where microtubules become saturated, the overlap between MAP7 and kinesin-1 binding sites leads to motor inhibition [siahaan-2022-map7-structure-abstract]. This biphasic regulation provides a mechanism for fine-tuned control of kinesin-1-mediated transport.

The functional consequence of MAP7-mediated kinesin-1 activation is profound. MAP7 does not alter the force exerted by a single kinesin-1 motor but increases its microtubule binding rate [pan-2019-map7-organelle-abstract]. For cargoes transported by teams of motors, this increased binding rate means more motors are simultaneously engaged with the microtubule, resulting in enhanced processivity and force generation. This enables kinesin-1-mediated roles including intracellular organelle transport, oocyte polarization, nuclear positioning, and centrosome separation.

## Cellular Localization

MAP7D1 exhibits cytoplasmic localization with association to the microtubule cytoskeleton. In neuronal cells, MAP7D1 shows prominent localization to the centrosome and partial association with cytoplasmic microtubules, similar to MAP7D2 [sun-2022-map7d1-map7d2-abstract]. Importantly, within the polarized architecture of neurons, MAP7D1 (along with MAP7) localizes primarily to the somatodendritic compartment, in contrast to MAP7D2 and MAP7D3 which concentrate at the proximal axon near the axon initial segment [montalvo-ortiz-2019-map7d2-axon-abstract].

During cell division, MAP7D1 associates with the mitotic spindle, where it plays an essential role in proper spindle formation. Studies examining cells with MAP7D1 mutations revealed multipolar and unstable mitotic spindle structures, which could be rescued by wild-type but not mutant MAP7D1 protein expression. This indicates MAP7D1 is important for maintaining bipolar spindle integrity during mitosis, likely through its microtubule-stabilizing function.

Gene Ontology annotations predict MAP7D1 to be involved in microtubule cytoskeleton organization, located in the cytoplasm and spindle, and active in the microtubule cytoskeleton. Human Protein Atlas data confirms broad tissue distribution with cytoplasmic expression across multiple tissue types.

## Role in Wnt5a Signaling and Cell Migration

MAP7D1 participates in non-canonical Wnt signaling through a feedback loop with Dishevelled (DVL), a central mediator of Wnt signaling pathways [mori-2018-map7-dvl-wnt5a-abstract]. Wnt5a signaling promotes microtubule remodeling during cell-substrate adhesion, migration, and planar cell polarity formation through a beta-catenin-independent pathway. In this context, MAP7 and MAP7D1 bind directly to DVL, directing its cortical localization and facilitating the targeting of microtubule plus-ends to the cell cortex in response to Wnt5a.

The interaction forms a positive feedback loop: Wnt5a signaling activates DVL, which promotes MAP7/7D1 movement toward microtubule plus-ends via kinesin-1 (KIF5B). This movement stabilizes MAP7/7D1 and enhances DVL cortical accumulation, amplifying the signaling response [mori-2018-map7-dvl-wnt5a-abstract]. Depletion of KIF5B abolishes both MAP7/7D1 dynamics and DVL localization, demonstrating the kinesin-1 dependency of this system.

Functional consequences of MAP7/7D1 depletion include impaired cortical DVL accumulation, reduced microtubule plus-end targeting to the cell cortex, compromised filopodia formation, defective focal adhesion dynamics, and slowed cell adhesion and migration [mori-2018-map7-dvl-wnt5a-abstract]. This function is evolutionarily conserved: the Drosophila ortholog Ensconsin shows planar-polarized distribution in epithelial cells and is required for proper Dishevelled localization in fly tissues.

## Phosphorylation and Regulatory Mechanisms

MAP7D1 is subject to regulation by phosphorylation, with the best-characterized site being serine 315 (S315), which is phosphorylated by doublecortin-like kinase 1 (DCLK1) [koizumi-2017-dclk1-map7d1-abstract]. This phosphorylation event is functionally significant: mutation analysis revealed that phosphorylation at S315 is critical for MAP7D1's role in promoting axon elongation. While the precise mechanism by which S315 phosphorylation modulates MAP7D1 activity remains unknown, it may affect microtubule binding affinity, protein-protein interactions, or subcellular localization.

For comparison, the closely related MAP7 protein is also regulated by phosphorylation in a cell-cycle-dependent manner. During interphase, MAP7 is phosphorylated only on serine residues, while threonine phosphorylation occurs during mitosis. Studies have shown that the MARK kinase (microtubule affinity-regulating kinase) phosphorylates MAP7 at conserved residues Ser168 and Ser198, and this phosphorylation is required for proper MAP7 localization patterns without affecting its microtubule binding affinity. Given the high sequence conservation between MAP7 and MAP7D1, similar regulatory mechanisms may apply to MAP7D1, though this remains to be experimentally verified.

## Role in Neuronal Development and Axon Elongation

MAP7D1 plays a specific role in cortical neuron development, particularly in callosal axon elongation [koizumi-2017-dclk1-map7d1-abstract]. DCLK1 is a member of the doublecortin family that functions in multiple stages of neural development including radial migration and axon growth. Through proteomic analysis, MAP7D1 was identified as a novel DCLK1 kinase substrate.

Knockdown of MAP7D1 in layer 2/3 cortical neurons results in significant impairment of callosal axon elongation without affecting radial migration, demonstrating a selective role in axon growth [koizumi-2017-dclk1-map7d1-abstract]. Mutation analysis revealed that phosphorylation at S315 is critical for this function, and overexpression of a phosphomimetic MAP7D1 mutant (S315D) fully rescues axon elongation defects in DCLK1 knockdown neurons. This establishes a DCLK1-MAP7D1 signaling axis important for axon development. Interestingly, MAP7D1 is required specifically for axon elongation but not for radial migration, suggesting that different aspects of neuronal development have distinct requirements for microtubule-associated proteins.

## DNA Damage Response: A Novel Function

A surprising recent discovery revealed that MAP7 and MAP7D1 participate in the DNA damage response (DDR), particularly during the G1 phase of the cell cycle [bensenor-2023-map7-ddr-abstract]. Using quantitative proteomics, researchers identified interactions between MAP7/MAP7D1 and several DDR proteins including RAD50, BRCA1, 53BP1, MLH1, and XPC. These interactions are direct and depend on CK2-mediated phosphorylation of the DDR proteins at specific sites (RAD50 Thr690, BRCA1 Ser1336).

Notably, these interactions persist even when microtubules are disrupted by drugs, suggesting a cytoskeleton-independent scaffolding function [bensenor-2023-map7-ddr-abstract]. Knockdown of MAP7D1 leads to strong arrest in the G1 cell cycle phase, and when MAP7/MAP7D1 are depleted in G1-arrested cells, DNA repair capacity decreases significantly. This manifests as fewer 53BP1 foci following gamma-irradiation and impaired recruitment of RAD50 to chromatin.

This unexpected function positions MAP7D1 as a potential link between cytoskeletal organization and genome maintenance, though the precise molecular mechanisms and physiological significance remain to be fully characterized.

## Interaction Partners

Beyond its well-characterized interactions with kinesin-1 (KIF5B) and Dishevelled (DVL), MAP7D1 engages with several other protein partners that expand its functional repertoire. Large-scale proteomic studies have identified additional interaction partners including DNMBP (dynamin-binding protein), as documented in the BioGRID interaction database. DNMBP is involved in actin cytoskeleton organization and endocytosis, suggesting potential coordination between microtubule and actin networks through MAP7D1.

The interactions with DNA damage response proteins represent another important class of MAP7D1 binding partners. Quantitative proteomics identified direct interactions with RAD50, BRCA1, 53BP1, MLH1, and XPC [bensenor-2023-map7-ddr-abstract]. These interactions are phospho-dependent, requiring CK2-mediated phosphorylation of the DDR proteins at specific residues (RAD50 Thr690, BRCA1 Ser1336). Importantly, these interactions persist even when microtubules are disrupted, indicating they represent a distinct functional mode independent of MAP7D1's cytoskeletal role.

Proteomic analysis of microtubule co-sedimented proteins from brain tissue identified MAP7, MAP7D1, and MAP7D2 (but not MAP7D3) as microtubule-associated proteins [sun-2022-map7d1-map7d2-abstract]. Notably, more MAP7D1 than MAP7D2 was recovered from brain lysates, consistent with MAP7D1's predominantly somatodendritic localization in neurons where it is more abundant than the axon-localized MAP7D2.

## Disease Associations

While MAP7D1 has not been extensively linked to human disease, one significant association has emerged. A novel mutation in MAP7D1 (c.601C>T, p.Arg201Trp) was identified in a patient with Shwachman-Diamond syndrome (SDS), a rare genetic disorder characterized by bone marrow failure, exocrine pancreatic insufficiency, and skeletal abnormalities. This mutation occurs in the microtubule-binding domain and disrupts the MAP7D1-microtubule interaction.

Cells carrying the R201W mutation exhibited multipolar and unstable mitotic spindles during cell division, with approximately 40% of cells showing abnormal division patterns. The mutation appears to have a loss-of-function effect, as wild-type MAP7D1 expression could rescue the phenotype while mutant expression could not. However, this finding is limited to a single patient, and further genetic screening in other SDS patients is needed to establish causality.

Given MAP7D1's interactions with DDR proteins including BRCA1, there may be relevance to cancer biology, though direct links to carcinogenesis have not been established. Human Protein Atlas data shows variable MAP7D1 expression across 20 different cancer types, warranting further investigation.

## Evolutionary Conservation and Family Context

The MAP7 family represents an evolutionarily conserved group of microtubule regulators. In Drosophila, a single homolog called Ensconsin (or E-MAP-115) performs functions analogous to the mammalian family members [mori-2018-map7-dvl-wnt5a-abstract]. Ensconsin is essential for myonuclear positioning and interacts with Khc (the Drosophila kinesin-1 heavy chain), demonstrating conservation of the MAP7-kinesin regulatory relationship across more than 500 million years of evolution.

The expansion to four paralogous genes in mammals (MAP7, MAP7D1, MAP7D2, MAP7D3) has enabled functional specialization. MAP7D1 shares overlapping functions with MAP7, including broad tissue expression, somatodendritic neuronal localization, kinesin-1 activation, and participation in Wnt5a signaling [mori-2018-map7-dvl-wnt5a-abstract][tymanskyj-2019-map7-kinesin-abstract]. Meanwhile, MAP7D2 and MAP7D3 have evolved specialized roles in axonal transport at the proximal axon [montalvo-ortiz-2019-map7d2-axon-abstract]. Despite this specialization, significant redundancy remains, as evidenced by the lethality of triple MAP7/MAP7D1/MAP7D3 knockout cells.

## Tissue Expression and Muscle Function

MAP7D1 shows broad expression across human tissues with notable enrichment in muscle and neural tissue. According to the Human Protein Atlas, the highest RNA expression occurs in skeletal muscle (267.9 nTPM), followed by heart muscle (91.0 nTPM) and spinal cord (87.4 nTPM). The protein shows cytoplasmic localization across multiple tissue types. In contrast, its paralog MAP7D2 has much more restricted expression, detected at the protein level only in brain and testis. This differential expression pattern likely reflects the specialized roles of different MAP7 family members in distinct physiological contexts.

Despite its high expression in skeletal muscle, studies in mammalian myotubes have revealed that MAP7 (rather than MAP7D1) is the critical family member for myonuclear positioning [metzger-2012-map7-muscle-abstract]. Skeletal muscle cells contain hundreds of myonuclei that must be evenly distributed along the periphery of the muscle fiber, and mispositioned nuclei are associated with muscle dysfunction and diseases such as centronuclear myopathies. Metzger and colleagues demonstrated that MAP7 and kinesin-1 (KIF5B) physically interact and are essential regulators of myonuclear positioning in both Drosophila and mammalian systems [metzger-2012-map7-muscle-abstract]. Importantly, depletion of MAP7D1, MAP7D2, or MAP7D3 individually did not affect nuclear positioning in myotubes, whereas MAP7 depletion caused significant nuclear aggregation defects. This indicates that despite high MAP7D1 expression in muscle tissue, it cannot compensate for MAP7 in this specific function, revealing an important distinction in their activities.

The MAP7-kinesin-1 complex facilitates nuclear spacing by enabling kinesin to slide antiparallel microtubules emanating from neighboring nuclei, thereby spreading and maintaining proper inter-nuclear distances. Expression of a fusion protein containing the KIF5B motor domain and the MAP7 microtubule-binding domain was sufficient to rescue nuclear positioning defects in MAP7-depleted cells, demonstrating that MAP7's role is to link kinesin-1 to microtubules for this function [metzger-2012-map7-muscle-abstract]. The inability of MAP7D1 to substitute for MAP7 in this context, despite their structural similarity and overlapping expression, suggests subtle but functionally important differences in how these paralogs interact with kinesin-1 or microtubules in the specialized environment of multinucleated muscle fibers.

## Open Questions

Several important questions remain for future investigation:

1. **Mechanism of acetylated tubulin maintenance**: How exactly does MAP7D1 maintain acetylated tubulin levels? Does it regulate acetyltransferases, inhibit deacetylases, or protect acetylated microtubules from depolymerization?

2. **DDR function mechanism**: What is the precise molecular mechanism by which MAP7D1 participates in DNA damage response? How do cytoplasmic MAP proteins interact with nuclear DDR machinery, and is nuclear translocation involved?

3. **Relationship between cytoskeletal and DDR functions**: Are the microtubule-related and DDR functions of MAP7D1 independent, or do they represent an integrated response to cellular stress?

4. **Disease relevance**: Beyond the single Shwachman-Diamond syndrome case, what is the broader relevance of MAP7D1 to human disease? Given interactions with BRCA1, is there a role in cancer susceptibility or progression?

5. **Regulatory mechanisms**: What kinases beyond DCLK1 regulate MAP7D1 function? Are there phosphatases or other post-translational modifications that modulate its activity?

6. **Neuronal specificity**: Why does MAP7D1 specifically affect callosal axon elongation but not radial migration? What determines this functional specificity in neuronal development?

7. **Redundancy with MAP7**: To what extent are MAP7 and MAP7D1 interchangeable, and what conditions reveal their distinct functions?

## References

1. **[sun-2022-map7d1-map7d2-abstract]** Sun X, et al. (2022). Map7D2 and Map7D1 facilitate microtubule stabilization through distinct mechanisms in neuronal cells. *Life Science Alliance* 5(8):e202201390. PMID: 35470240. PMCID: PMC9039348. DOI: 10.26508/lsa.202201390. https://pmc.ncbi.nlm.nih.gov/articles/PMC9039348/

2. **[koizumi-2017-dclk1-map7d1-abstract]** Koizumi H, Fujioka H, Togashi K, Thompson J, Yates JR III, Gleeson JG, Emoto K. (2017). DCLK1 phosphorylates the microtubule-associated protein MAP7D1 to promote axon elongation in cortical neurons. *Developmental Neurobiology* 77(4):493-510. PMID: 27503845. DOI: 10.1002/dneu.22428. https://pubmed.ncbi.nlm.nih.gov/27503845/

3. **[mori-2018-map7-dvl-wnt5a-abstract]** Mori H, et al. (2018). Map7/7D1 and Dvl form a feedback loop that facilitates microtubule remodeling and Wnt5a signaling. *EMBO Reports* 19(7):e45471. PMID: 29880710. PMCID: PMC6030700. DOI: 10.15252/embr.201745471. https://pmc.ncbi.nlm.nih.gov/articles/PMC6030700/

4. **[tymanskyj-2019-map7-kinesin-abstract]** Tymanskyj SR, et al. (2019). MAP7 family proteins regulate kinesin-1 recruitment and activation. *Journal of Cell Biology* 218(4):1298-1318. PMID: 30770434. PMCID: PMC6446838. DOI: 10.1083/jcb.201808065. https://pmc.ncbi.nlm.nih.gov/articles/PMC6446838/

5. **[bensenor-2023-map7-ddr-abstract]** Bensenor LB, et al. (2023). Microtubule-associated proteins MAP7 and MAP7D1 promote DNA double-strand break repair in the G1 cell cycle phase. *iScience* 26(3):106107. PMID: 36818290. PMCID: PMC9958362. DOI: 10.1016/j.isci.2023.106107. https://pmc.ncbi.nlm.nih.gov/articles/PMC9958362/

6. **[siahaan-2022-map7-structure-abstract]** Siahaan V, et al. (2022). Structural and functional insight into the regulation of kinesin-1 by microtubule-associated protein MAP7. *Science* 376(6590):eabf6154. PMID: 35389798. PMCID: PMC8985661. DOI: 10.1126/science.abf6154. https://pmc.ncbi.nlm.nih.gov/articles/PMC8985661/

7. **[montalvo-ortiz-2019-map7d2-axon-abstract]** Montalvo-Ortiz BL, et al. (2019). MAP7D2 Localizes to the Proximal Axon and Locally Promotes Kinesin-1-Mediated Cargo Transport into the Axon. *Cell Reports* 26(7):1988-1999.e6. PMID: 30759405. PMCID: PMC6381606. DOI: 10.1016/j.celrep.2019.01.084. https://pmc.ncbi.nlm.nih.gov/articles/PMC6381606/

8. **[pan-2019-map7-organelle-abstract]** Pan X, et al. (2019). MAP7 regulates organelle transport by recruiting kinesin-1 to microtubules. *Journal of Biological Chemistry* 294(25):10160-10172. PMID: 31085585. PMCID: PMC6664170. DOI: 10.1074/jbc.RA119.008052. https://pmc.ncbi.nlm.nih.gov/articles/PMC6664170/

9. **[metzger-2012-map7-muscle-abstract]** Metzger T, Gache V, Xu M, Cadot B, Folber ES, Richardson BE, et al. (2012). MAP and kinesin-dependent nuclear positioning is required for skeletal muscle function. *Nature* 484(7392):120-124. PMID: 22425998. PMCID: PMC3321085. DOI: 10.1038/nature10914. https://pmc.ncbi.nlm.nih.gov/articles/PMC3321085/

10. **UniProt Entry Q3KQU3**: https://www.uniprot.org/uniprotkb/Q3KQU3/entry

11. **OMIM Entry 621363**: https://www.omim.org/entry/621363

12. **Human Protein Atlas - MAP7D1**: https://www.proteinatlas.org/ENSG00000116871-MAP7D1

13. **BioGRID - MAP7D1 Interactions**: https://thebiogrid.org/


## Citations

1. bensenor-2023-map7-ddr-abstract.md
2. koizumi-2017-dclk1-map7d1-abstract.md
3. metzger-2012-map7-muscle-abstract.md
4. montalvo-ortiz-2019-map7d2-axon-abstract.md
5. mori-2018-map7-dvl-wnt5a-abstract.md
6. pan-2019-map7-organelle-abstract.md
7. siahaan-2022-map7-structure-abstract.md
8. sun-2022-map7d1-map7d2-abstract.md
9. tymanskyj-2019-map7-kinesin-abstract.md