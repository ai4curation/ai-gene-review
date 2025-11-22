---
provider: cyberian
model: deep-research
cached: false
start_time: '2025-11-15T15:31:36.495541'
end_time: '2025-11-15T15:49:16.273452'
duration_seconds: 1059.78
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: METEA
  gene_id: mllA
  gene_symbol: mllA
  uniprot_accession: C5B1I4
  protein_description: 'SubName: Full=Siderophore synthetase component {ECO:0000313|EMBL:ACS41785.1};'
  gene_info: OrderedLocusNames=MexAM1_META1p4132 {ECO:0000313|EMBL:ACS41785.1};
  organism_full: Methylorubrum extorquens (strain ATCC 14718 / DSM 1338 / JCM 2805
    / NCIMB 9133 / AM1) (Methylobacterium extorquens).
  protein_family: Belongs to the IucA/IucC family.
  protein_domains: Aerobactin_biosyn_IucA/IucC_N. (IPR007310); IucA/IucC-like_C. (IPR022770);
    LucA/IucC-like. (IPR037455); FhuF (PF06276); IucA_IucC (PF04183)
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
- **UniProt Accession:** C5B1I4
- **Protein Description:** SubName: Full=Siderophore synthetase component {ECO:0000313|EMBL:ACS41785.1};
- **Gene Information:** OrderedLocusNames=MexAM1_META1p4132 {ECO:0000313|EMBL:ACS41785.1};
- **Organism (full):** Methylorubrum extorquens (strain ATCC 14718 / DSM 1338 / JCM 2805 / NCIMB 9133 / AM1) (Methylobacterium extorquens).
- **Protein Family:** Belongs to the IucA/IucC family.
- **Key Domains:** Aerobactin_biosyn_IucA/IucC_N. (IPR007310); IucA/IucC-like_C. (IPR022770); LucA/IucC-like. (IPR037455); FhuF (PF06276); IucA_IucC (PF04183)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "mllA" matches the protein description above**
2. **Verify the organism is correct:** Methylorubrum extorquens (strain ATCC 14718 / DSM 1338 / JCM 2805 / NCIMB 9133 / AM1) (Methylobacterium extorquens).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'mllA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **mllA** (gene ID: mllA, UniProt: C5B1I4) in METEA.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: mllA (META1p4132) in Methylorubrum extorquens AM1

**Gene:** mllA (OrderedLocusName: MexAM1_META1p4132)
**UniProt Accession:** C5B1I4
**Organism:** Methylorubrum extorquens (strain ATCC 14718 / DSM 1338 / JCM 2805 / NCIMB 9133 / AM1)
**Protein Family:** IucA/IucC family (NRPS-independent siderophore synthetases)

## Introduction

The mllA gene (META1p4132) in Methylorubrum extorquens AM1 encodes a critical component of the methylolanthanin biosynthetic pathway, representing the first characterized lanthanophore biosynthesis system in bacteria[zytnick-2024-methylolanthanin]. This protein belongs to the IucA/IucC family of nonribosomal peptide synthetase-independent (NIS) siderophore synthetases, enzymes that catalyze ATP-dependent condensation reactions to assemble metallophore molecules without requiring the large modular NRPS machinery[bailey-2018-aerobactin-biosynthesis]. MllA shares 50% sequence identity with AsbA from Bacillus subtilis, a well-characterized petrobactin biosynthesis enzyme, positioning it as a Type A NIS synthetase that utilizes citrate as its primary substrate[zytnick-2024-methylolanthanin]. The discovery and characterization of this enzyme has illuminated how methylotrophic bacteria acquire lanthanide cofactors essential for their metabolism, particularly for lanthanide-dependent methanol dehydrogenases that enable growth on single-carbon compounds.

## Protein Structure and Domain Architecture

MllA exhibits the characteristic domain organization of IucA/IucC family proteins, featuring multiple conserved domains that facilitate its catalytic function. The protein contains the Aerobactin_biosyn_IucA/IucC_N domain (IPR007310), which represents the N-terminal region characteristic of this enzyme family and is essential for substrate recognition and binding. Additionally, MllA possesses the IucA/IucC-like C-terminal domain (IPR022770), which contributes to the overall three-dimensional architecture and catalytic mechanism. The complete protein falls within the IucA/IucC-like superfamily (IPR037455), encompassing the full complement of structural features required for NIS synthetase activity.

Based on structural studies of homologous enzymes, particularly IucA from the aerobactin biosynthetic pathway, MllA is predicted to adopt a three-domain architecture often described as a "cupped hand" structure, with thumb, fingers, and palm regions that create a substrate-binding pocket[bailey-2018-aerobactin-biosynthesis]. This architecture facilitates the ordered binding of multiple substrates and positions them appropriately for the condensation reaction. A particularly important structural feature likely present in MllA is the "550 loop," a flexible region that becomes ordered upon substrate binding and contains conserved asparagine residues critical for positioning the nucleophile substrate[bailey-2020-iuca-ordered-mechanism]. This loop region has been shown to be disordered in crystal structures of IucA, IucC, AcsD, AlcC, and DfoC, suggesting it is a conserved dynamic element across the NIS synthetase family[carroll-2018-nis-review][patel-2025-nis-review]. Comprehensive reviews of NIS synthetase structure and function confirm that these architectural features are conserved across the enzyme family, reflecting a common catalytic strategy for ATP-dependent amide bond formation between carboxylates and amine nucleophiles[patel-2025-nis-review].

## Enzymatic Function and Catalytic Mechanism

MllA functions as an NRPS-independent siderophore synthetase that catalyzes the initial condensation step in methylolanthanin biosynthesis[zytnick-2024-methylolanthanin]. As a Type A NIS synthetase, MllA utilizes citrate as one of its substrates, distinguishing it from Type B enzymes that react with α-ketoglutarate and Type C enzymes that use citrate or succinate derivatives[bailey-2020-iuca-ordered-mechanism][carroll-2018-nis-review]. The enzyme catalyzes an ATP-dependent two-step reaction analogous to that performed by IucA in aerobactin biosynthesis. NIS synthetases operate by adenylating a carboxylic acid substrate followed by nucleophilic attack by an amine or alcohol, forming amide or ester linkages without requiring the large modular NRPS machinery[patel-2025-nis-review].

The catalytic mechanism of MllA, inferred from detailed studies of its homolog IucA, likely proceeds through an ordered sequential mechanism[bailey-2020-iuca-ordered-mechanism]. In this mechanism, ATP binds first to the enzyme, followed by citrate, and finally the modified amino acid nucleophile. Only after formation of the complete quaternary complex (enzyme-ATP-citrate-nucleophile) does the chemical reaction proceed. The first partial reaction involves adenylation of citrate to form a citryl-AMP intermediate, activating one of citrate's carboxylate groups for nucleophilic attack. In the second partial reaction, this activated intermediate reacts with the α-amino group of a modified lysine derivative to form a new amide bond, creating the biosynthetic intermediate that carries the first arm of the metallophore scaffold.

Studies of IucA have revealed critical active site residues that are likely conserved in MllA. The citrate-binding site involves multiple residues that coordinate the substrate's three carboxylate groups, with particular importance placed on residues equivalent to His147, Thr284, Arg288, and His425 in IucA[bailey-2020-iuca-ordered-mechanism]. The nucleophile-binding site positions the incoming modified amino acid for attack on the citryl-AMP intermediate, with residues equivalent to Leu423, Tyr479, and Tyr483 playing structural roles. Perhaps most critically, the conserved Asn-Glu-Asn motif on the flexible 550 loop is essential for catalytic activity, with mutation of the asparagine residues abolishing enzyme function[bailey-2020-iuca-ordered-mechanism].

The ordered mechanism employed by MllA has important functional implications. By requiring ATP and citrate to bind before the nucleophile, the enzyme ensures proper positioning of all reactive groups and prevents wasteful hydrolysis of the citryl-AMP intermediate. This sequential binding also contributes to the enzyme's substrate specificity, as the binding pocket undergoes conformational changes with each substrate addition that prepare it for the next binding event. The stereoselectivity observed in IucA, which produces exclusively the 3S-citryl derivative through enantioselective desymmetrization of citrate, is likely also a feature of MllA, ensuring production of a single stereoisomer of the methylolanthanin intermediate[bailey-2018-aerobactin-biosynthesis].

## Role in Methylolanthanin Biosynthesis Pathway

MllA functions as part of a ten-gene biosynthetic cluster (META1p4129-4138, also designated mll/mlu) that produces methylolanthanin, the first structurally characterized lanthanophore[zytnick-2024-methylolanthanin]. This cluster exhibits homology to biosynthetic gene clusters responsible for transport, regulation, and biosynthesis of NRPS-independent siderophores containing citrate and aromatic moieties, including petrobactin, rhodopetrobactin, and roseobactin. The organization and predicted functions of the genes in this cluster reveal a sophisticated system for metallophore production and regulation.

The cluster begins with regulatory and transport components (META1p4129-4131, designated mluARI) that encode an outer membrane TonB-dependent receptor, an anti-sigma factor, and a sigma factor for cell-surface signaling and transcriptional regulation. These components likely mediate feedback regulation in response to lanthanide availability, similar to systems observed in iron siderophore biosynthesis. The biosynthetic core of the cluster comprises META1p4132-4135, with MllA (META1p4132) serving as the initial synthetase. This is followed by META1p4133 (mllBC), a gene fusion encoding both an NRPS-like synthetase and an adenylation domain with 52% and 56% identity respectively to petrobactin pathway components. META1p4134 (mllDE) represents another fusion protein combining aryl carrier protein and ligase domains with 54% homology to asbD/asbE from the petrobactin pathway. META1p4135 (mllF) encodes a predicted 3,4-dihydroxybenzoate synthase homolog with 52% identity to known enzymes, though interestingly, the final methylolanthanin product contains 4-hydroxybenzoate rather than 3,4-dihydroxybenzoate moieties. META1p4137 (mllH) encodes a GNAT family acetyltransferase with 74% identity to enzymes in the rhodopetrobactin pathway, responsible for acetylating the homospermidine linkers in the final product.

The complete biosynthetic pathway produces methylolanthanin, a molecule consisting of a central citrate group linked to two 4-hydroxybenzoate (4-HB) moieties via homospermidine residues, each acetylated at the central amine[zytnick-2024-methylolanthanin]. This structure represents a unique metallophore scaffold not previously described, distinguished particularly by the presence of monohydroxybenzoate groups rather than the dihydroxybenzoate groups found in related siderophores like petrobactin. MllA initiates this biosynthetic sequence by catalyzing the first condensation reaction that links citrate to a modified precursor, establishing the central scaffold upon which subsequent enzymatic steps elaborate to build the complete metallophore structure.

## Cellular Localization and Secretion

While direct experimental evidence for MllA localization has not been reported, the enzyme is predicted to function in the cytoplasm based on the absence of signal sequences and the cytoplasmic location of other characterized NIS synthetases[bailey-2018-aerobactin-biosynthesis]. The biosynthesis of methylolanthanin likely occurs entirely within the cytoplasm, with the completed metallophore subsequently secreted to the extracellular environment where it can chelate lanthanides. The presence of a TonB-dependent receptor (encoded by mluA/META1p4129) in the biosynthetic cluster suggests that the lanthanide-loaded methylolanthanin complex is then recognized and transported back into the cell through the outer membrane, a mechanism analogous to classical siderophore uptake systems[zytnick-2024-methylolanthanin].

The cellular context of methylolanthanin function extends beyond simple biosynthesis and secretion. Studies of lanthanide homeostasis in M. extorquens AM1 have revealed that lanthanides are stored within the cell as cytoplasmic inclusions resembling polyphosphate granules[roszczenko-2020-lanthanide-homeostasis]. This storage mechanism suggests a sophisticated system for managing lanthanide availability, with MllA-produced methylolanthanin facilitating the initial acquisition of lanthanides from the environment, followed by intracellular storage and mobilization for incorporation into lanthanide-dependent enzymes.

## Regulation and Expression Patterns

The expression of mllA and the entire methylolanthanin biosynthetic cluster is highly responsive to lanthanide availability and solubility. Quantitative proteomics studies have demonstrated that the genes META1p4129 through META1p4138 are among the most strongly upregulated genes in M. extorquens AM1 when cells are grown with poorly soluble neodymium oxide (Nd2O3) compared to growth with soluble neodymium chloride (NdCl3), showing an average 32-fold increase in expression[zytnick-2024-methylolanthanin]. This dramatic upregulation indicates that the cell recognizes lanthanide limitation or poor bioavailability and responds by increasing production of the metallophore machinery needed to scavenge these essential metals from recalcitrant environmental sources.

The regulation of the mll cluster likely involves the sigma factor/anti-sigma factor pair encoded by META1p4130 and META1p4131, which would enable rapid transcriptional responses to changes in lanthanide-metallophore complexes detected at the outer membrane. This regulatory architecture is characteristic of metal acquisition systems in bacteria, where metal-loaded metallophores binding to outer membrane receptors trigger conformational changes that release sigma factors, which then activate transcription of biosynthetic and uptake genes. Such regulatory mechanisms ensure that metallophore production is coordinated with cellular metal requirements, preventing wasteful overproduction when metals are readily available while ensuring adequate synthesis when metals are limiting.

The physiological context for this regulation becomes clear when considering the dual methanol dehydrogenase systems in M. extorquens AM1. The organism encodes both calcium-dependent (MxaFI) and lanthanide-dependent (XoxF) methanol dehydrogenases[roszczenko-2020-lanthanide-homeostasis]. When lanthanides are abundant and bioavailable, cells preferentially express XoxF-type enzymes, which provide superior catalytic efficiency for methylotrophic growth. Under these conditions, the mll cluster expression remains at basal levels. However, when lanthanides are present but poorly soluble or complexed in forms that are difficult to access, the cell dramatically upregulates the mll cluster to produce the methylolanthanin needed to solubilize and acquire these metals, enabling continued use of the more efficient XoxF pathway.

## Biological Significance and Physiological Context

The biological significance of MllA and the methylolanthanin system it helps produce extends far beyond simple metal acquisition, touching on fundamental aspects of bacterial methylotrophy and metal-dependent metabolism. Methylotrophy, the ability to grow on reduced single-carbon compounds like methanol, is a metabolic capability of major ecological importance in environments where plant-derived methanol is abundant. Pink-pigmented facultative methylotrophic bacteria of the genera Methylobacterium and Methylorubrum are ubiquitous plant symbionts that utilize methanol produced during pectin demethylation in plant cell walls[juma-2022-siderophore-methylobacterium]. The efficiency of this methylotrophic lifestyle depends critically on methanol dehydrogenase enzymes, and the lanthanide-dependent XoxF-type enzymes significantly outperform their calcium-dependent MxaFI counterparts in catalytic efficiency.

Experimental evidence demonstrates the functional importance of the mll cluster and MllA in lanthanide-dependent physiology. Deletion mutants lacking the methylolanthanin biosynthetic genes show an 1.8-fold decrease in neodymium bioaccumulation compared to wild-type cells, while overexpression of the cluster increases accumulation 3.5-fold[zytnick-2024-methylolanthanin]. These findings establish that methylolanthanin production is required for wild-type levels of lanthanide acquisition and accumulation. The consequences of this reduced lanthanide uptake would be decreased availability of lanthanide cofactors for incorporation into XoxF methanol dehydrogenases, potentially limiting methylotrophic growth under conditions where lanthanides are the available metal but are poorly soluble or complexed.

The discovery of methylolanthanin and characterization of MllA has revealed that bacteria employ siderophore-like metallophores not only for iron acquisition but also for acquiring rare earth elements. This finding has been reinforced by studies in related Methylobacterium species, where siderophores have been shown to have dual roles in both iron and lanthanide acquisition[juma-2022-siderophore-methylobacterium]. In Methylobacterium aquaticum strain 22A, the staphyloferrin B-like siderophore can solubilize insoluble lanthanide oxides and function as a lanthanophore, demonstrating that different Methylobacterium/Methylorubrum species have evolved distinct metallophore systems for lanthanide acquisition. Genomic analysis of 60 Methylobacterium genomes identified a total of 66 siderophore synthesis gene clusters distributed across 10 different structural types, suggesting remarkable diversity in metallophore chemistry across the genus[juma-2022-siderophore-methylobacterium].

## Evolutionary and Comparative Context

The evolutionary relationships among NIS synthetases provide important context for understanding MllA function. The IucA/IucC family represents a widespread solution to the challenge of assembling hydroxamate and carboxylate siderophores without the metabolic cost of maintaining large NRPS gene clusters. MllA's 50% sequence identity to AsbA from the petrobactin pathway in Bacillus subtilis suggests these enzymes diverged from a common ancestor, with subsequent specialization for different metallophore products and potentially different metal specificities (iron for petrobactin, lanthanides for methylolanthanin). The methylolanthanin biosynthetic cluster also shows homology to the rhodopetrobactin cluster from Rhodopseudomonas palustris TIE-1, suggesting that lanthanophore biosynthesis may be more widespread among bacteria than currently appreciated[zytnick-2024-methylolanthanin].

The structural uniqueness of methylolanthanin, particularly its incorporation of 4-hydroxybenzoate moieties instead of the 3,4-dihydroxybenzoate groups found in petrobactin and rhodopetrobactin, raises interesting questions about substrate specificity and product evolution. Despite encoding a predicted 3,4-dihydroxybenzoate synthase (MllF), the pathway produces 4-hydroxybenzoate-containing products, suggesting either that MllF has evolved altered specificity or that downstream modification steps remove one hydroxyl group[zytnick-2024-methylolanthanin]. This modification may be functionally significant, potentially tuning the metal-binding properties of methylolanthanin to favor lanthanides over iron, though this hypothesis awaits experimental validation.

## Relationship to Other Metal Acquisition Systems

The mllA-containing methylolanthanin biosynthetic cluster functions as part of a larger cellular system for lanthanide homeostasis in M. extorquens AM1. This system includes the lut (lanthanide utilization and transport) cluster (META1_1778-1787), which encodes a TonB-dependent receptor (LutH), ABC-type transporter components, multiple periplasmic binding proteins, and lanmodulin, a highly selective lanthanide-binding protein[roszczenko-2020-lanthanide-homeostasis]. The relationship between these systems suggests a division of labor: the mll cluster produces and secretes the metallophore for environmental scavenging, while the lut cluster handles the subsequent recognition, transport, and delivery of lanthanide-loaded metallophores to appropriate cellular destinations.

Interestingly, M. extorquens AM1 also possesses an exclusive TonB-dependent receptor for lanthanide uptake (LutH), suggesting that the organism may have multiple routes for lanthanide acquisition beyond the methylolanthanin system[juma-2022-siderophore-methylobacterium]. This redundancy likely reflects the critical importance of lanthanide acquisition for the organism's methylotrophic lifestyle. The integration of these various systems—metallophore biosynthesis and secretion, outer membrane recognition and transport, inner membrane transport, intracellular storage, and cofactor incorporation—represents a sophisticated cellular machinery comparable in complexity to well-studied iron homeostasis systems but adapted for the unique chemistry and biology of lanthanide metals.

## Mechanistic Insights from Structural Studies of Homologs

Although the three-dimensional structure of MllA itself has not been determined, extensive structural and mechanistic studies of its close homologs IucA and IucC from aerobactin biosynthesis provide detailed insights into how this family of enzymes functions[bailey-2018-aerobactin-biosynthesis][bailey-2020-iuca-ordered-mechanism]. These studies have revealed that NIS synthetases employ an elegant catalytic strategy that ensures substrate specificity and stereochemical control while avoiding the large protein scaffolds required by NRPS systems.

The crystal structure of IucA reveals a three-domain architecture with distinct substrate-binding pockets for ATP, citrate, and the nucleophile[bailey-2020-iuca-ordered-mechanism]. The ATP-binding site is positioned to facilitate adenylation of citrate, with the adenylated intermediate remaining bound while awaiting attack by the nucleophile. The citrate-binding site must accommodate the substrate's three carboxylate groups while specifically orienting one for adenylation and subsequent nucleophilic attack. Residues in this site not only bind the substrate but also contribute to stereochemical control—IucA produces exclusively the 3S-citryl derivative despite citrate being achiral, achieving this through asymmetric binding that exposes only one of citrate's two pro-chiral carboxylates for reaction.

The most intriguing structural feature is the 550 loop, a region of approximately 10 residues that is disordered in all crystal structures but is essential for catalysis[bailey-2020-iuca-ordered-mechanism]. This loop contains a conserved Asn-Glu-Asn motif, and mutation of either asparagine residue to alanine completely abolishes activity with the nucleophile substrate. The loop is proposed to become ordered upon nucleophile binding, positioning these asparagine residues to activate the nucleophile's α-amino group for attack on the citryl-AMP intermediate. This dynamic structural element thus plays a gating role, ensuring that the adenylated intermediate is only attacked when the correct nucleophile is present and properly positioned.

Kinetic studies of IucA have quantified the enzyme's catalytic parameters, revealing kcat values of 0.35-0.85 s⁻¹ depending on which substrate is varied, and KM values in the range of 0.05-0.79 mM[bailey-2020-iuca-ordered-mechanism]. While these values represent moderate catalytic efficiency by enzyme standards, they are appropriate for biosynthetic enzymes where reaction flux is often controlled by substrate availability rather than enzyme saturation. The complete aerobactin biosynthetic pathway, incorporating the activities of IucD, IucB, IucA, and IucC, operates with an overall turnover frequency of approximately 6 min⁻¹ under saturating conditions[bailey-2018-aerobactin-biosynthesis], suggesting that this pace of metallophore production is sufficient for cellular needs.

By analogy to these detailed studies of IucA and IucC, MllA is predicted to employ similar structural and mechanistic strategies. The enzyme likely adopts the characteristic three-domain architecture, utilizes an ordered binding mechanism to ensure proper substrate positioning and prevent wasteful side reactions, employs a flexible loop element for nucleophile activation, and achieves stereochemical control through asymmetric substrate binding. These conserved features reflect the fundamental chemical challenges of coupling citrate to modified amino acids in an ATP-dependent manner, challenges that the IucA/IucC family has solved through a common structural and mechanistic framework that can be adapted to produce diverse metallophore products.

## Substrate Specificity and Biosynthetic Flexibility

The substrate specificity of NIS synthetases like MllA determines both the fidelity of metallophore biosynthesis and the potential for producing variant structures. Studies of IucA have examined how the enzyme discriminates among potential substrates, revealing both strict requirements and some flexibility[bailey-2020-iuca-ordered-mechanism]. For the carboxylic acid substrate, IucA shows strong preference for citrate but can utilize tricarballylic acid, which lacks citrate's central hydroxyl group, albeit with reduced efficiency. However, the enzyme rejects glutarate and α-ketoglutarate, demonstrating that the three-carboxylate structure is essential for productive binding. This indicates that while the central hydroxyl contributes to binding affinity and catalytic efficiency, the tertiary carboxylate is absolutely required.

For the nucleophile substrate, IucA is specific for N6-acetyl-N6-hydroxylysine in the aerobactin pathway, but related enzymes in the family accept different modified amino acids or polyamines. AsbA from the petrobactin pathway uses spermidine rather than a modified lysine, while enzymes in the desferrioxamine pathway utilize other substrates. This substrate flexibility across the family suggests that MllA has evolved specificity for homospermidine or a modified derivative thereof, consistent with the structure of methylolanthanin which contains homospermidine linkers connecting citrate to the aromatic groups. The acetylation of these homospermidine moieties is performed by MllH, the GNAT family acetyltransferase, either before or after MllA-catalyzed condensation, though the exact order of these modifications remains to be experimentally determined.

The biosynthetic flexibility of the pathway is also evident in the production of the aromatic moieties. While the cluster encodes a predicted 3,4-dihydroxybenzoate synthase (MllF), the final product contains 4-hydroxybenzoate groups. This discrepancy could arise through several mechanisms: MllF might have evolved altered regiospecificity to produce 4-hydroxybenzoate directly, or a downstream enzyme might remove one hydroxyl group from an initially produced 3,4-dihydroxybenzoate intermediate. Understanding the resolution of this apparent inconsistency will require biochemical reconstitution of the pathway in vitro or detailed analysis of pathway intermediates in vivo.

## Comparative Analysis with Siderophore Systems

The evolution of MllA and the methylolanthanin system provides a fascinating example of how bacteria have repurposed iron-scavenging machinery for acquiring rare earth elements. Classical siderophores are small-molecule iron chelators that bacteria secrete to solubilize and acquire iron from their environment, a strategy necessitated by iron's extremely low solubility at neutral pH under aerobic conditions. The structural and mechanistic parallels between siderophore biosynthesis and lanthanophore biosynthesis are striking: both employ similar enzymatic machinery (NIS synthetases), similar transport systems (TonB-dependent receptors and ABC transporters), and similar regulatory logic (metal-responsive transcription)[roszczenko-2020-lanthanide-homeostasis].

However, lanthanides and iron differ substantially in their chemistry and biological roles. Iron is a transition metal that undergoes redox cycling between Fe²⁺ and Fe³⁺ states, a property essential for its function in enzymes like cytochromes and iron-sulfur proteins but also responsible for its participation in potentially harmful Fenton chemistry. Lanthanides, in contrast, are redox-inert under biological conditions, existing exclusively in the 3+ oxidation state. This redox inertness makes them unsuitable for electron transfer reactions but ideal for Lewis acid catalysis, where their role is to activate substrates through coordination rather than electron transfer. In XoxF-type methanol dehydrogenases, the lanthanide cofactor serves precisely this role, activating the alcohol substrate for hydride transfer without undergoing redox changes itself.

The chelating groups used in siderophores versus lanthanophores reflect these chemical differences. Many iron siderophores employ hydroxamate groups, which bind Fe³⁺ very tightly through bidentate coordination of the hydroxamate oxygen atoms. Methylolanthanin, in contrast, employs a combination of carboxylate groups from citrate and hydroxyl groups from 4-hydroxybenzoate, along with amine nitrogens from the homospermidine linkers. This mixed-ligand system likely provides the appropriate binding affinity and selectivity for lanthanides while also allowing for metal release upon reduction of the chelator or changes in pH within the cell. Understanding the exact coordination chemistry of methylolanthanin with different lanthanides remains an important area for future investigation.

Studies in Methylobacterium aquaticum strain 22A have demonstrated that even within the Methylobacterium/Methylorubrum genus, different species employ structurally distinct metallophores for lanthanide acquisition[juma-2022-siderophore-methylobacterium]. Strain 22A produces a staphyloferrin B-like siderophore that can function as both a siderophore for iron and a lanthanophore for rare earths, depending on environmental conditions. This dual functionality is particularly elegant, allowing the bacterium to use a single metallophore system to acquire whichever metal is limiting. The IucA/IucC family genes sbnC and sbnF in the staphyloferrin B cluster play analogous roles to mllA in methylolanthanin biosynthesis, catalyzing the ATP-dependent condensation reactions that build the metallophore scaffold. The diversity of metallophore systems across Methylobacterium species suggests that acquisition of lanthanides has been a significant selective pressure in the evolution of this bacterial group, driving innovation in metal-chelating chemistry.

## Integration with Lanthanide-Dependent Methylotrophy

The ultimate functional context for MllA and methylolanthanin is their enabling role in lanthanide-dependent methylotrophy. Methylotrophy is not merely an alternative metabolic pathway but rather a lifestyle that has allowed Methylobacterium and Methylorubrum species to occupy the phyllosphere niche in association with plants. Plants produce copious amounts of methanol during pectin demethylation reactions involved in cell wall synthesis, creating a carbon source that is abundant in the phyllosphere but toxic to many organisms and challenging to metabolize efficiently. Methylotrophic bacteria solve this challenge through specialized methanol dehydrogenase enzymes that oxidize methanol to formaldehyde, which then enters central metabolism through specialized pathways.

The discovery that lanthanide-dependent XoxF-type methanol dehydrogenases significantly outperform calcium-dependent MxaFI enzymes has reframed our understanding of methylotrophy. Under conditions where lanthanides are available, bacteria preferentially express XoxF enzymes, suggesting these provide a selective advantage. However, lanthanides exist in the environment primarily as insoluble oxides and minerals, creating a bioavailability problem analogous to that faced with iron. The evolution of methylolanthanin biosynthesis, with MllA as a key biosynthetic enzyme, represents the bacterial solution to this bioavailability problem. By producing a lanthanide-specific metallophore capable of solubilizing poorly accessible lanthanide sources, M. extorquens AM1 can access the superior catalytic efficiency of XoxF enzymes even when lanthanides are present in recalcitrant forms.

The 32-fold upregulation of the mll cluster when cells are grown with poorly soluble Nd2O3 versus soluble NdCl3 demonstrates that bacteria actively sense lanthanide bioavailability and respond by increasing metallophore production[zytnick-2024-methylolanthanin]. This regulatory logic ensures that cells invest in metallophore biosynthesis only when needed—when lanthanides are present but difficult to access. Under conditions where lanthanides are readily bioavailable or completely absent, the cell can maintain low basal expression of the mll cluster, avoiding the metabolic cost of unnecessary metallophore production. This regulated response integrates with the broader lanthanide homeostasis machinery, including the lut transport cluster and lanmodulin-mediated intracellular lanthanide handling, to create a comprehensive system for managing these essential but sometimes scarce metal cofactors.

## Open Questions

Despite significant recent progress in understanding MllA and methylolanthanin biosynthesis, numerous important questions remain unanswered. The precise order of biosynthetic steps in the pathway has not been fully elucidated—specifically, whether homospermidine acetylation by MllH occurs before or after MllA-catalyzed condensation with citrate, and how the aromatic moieties are synthesized and attached to the growing metallophore. Biochemical reconstitution of the pathway in vitro would resolve these questions and enable detailed kinetic and mechanistic studies of each step.

The three-dimensional structure of MllA itself remains undetermined. While homology modeling based on IucA and AsbA structures can provide predictions, experimental structure determination through X-ray crystallography or cryo-electron microscopy would reveal the specific substrate-binding pockets, conformational states, and structural adaptations that tune MllA for its specific substrates and products. Structures of MllA in complex with substrates, products, and intermediate states would be particularly valuable for understanding the catalytic mechanism and stereochemical control.

The exact coordination chemistry of methylolanthanin with different lanthanide ions requires detailed investigation. While the study by Zytnick et al. demonstrated that methylolanthanin can form complexes with lanthanum, neodymium, and lutetium, representing light, middle, and heavy rare earths respectively, the detailed coordination geometry, stoichiometry, and thermodynamic stability constants remain to be determined[zytnick-2024-methylolanthanin]. Recent comparative binding studies (2024) of methylolanthanin and the structurally related rhodopetrobactin B have revealed unexpected complexity: both metallophores appear to precipitate lanthanides under biologically relevant pH and concentration conditions, raising questions about the mechanism of lanthanide delivery to cells. Understanding whether methylolanthanin shows selectivity among different lanthanides, how precipitation relates to biological function, and whether this selectivity matches the lanthanide preferences of XoxF methanol dehydrogenases, would illuminate the chemical logic of the system.

The biosynthetic discrepancy between the predicted 3,4-dihydroxybenzoate synthase activity of MllF and the 4-hydroxybenzoate groups actually present in methylolanthanin requires resolution. Does MllF produce 4-hydroxybenzoate directly, suggesting annotation error or evolved specificity change? Or does an unidentified enzyme remove one hydroxyl group from an initially produced 3,4-dihydroxybenzoate intermediate? Answering this question will require either in vitro characterization of MllF or analysis of pathway intermediates.

The question of how widespread lanthanophore biosynthesis is among bacteria represents a broader area for investigation. The identification of rhodopetrobactin from Rhodopseudomonas palustris as a related system suggests that lanthanophore production may occur in diverse bacterial lineages[zytnick-2024-methylolanthanin]. Genome mining approaches searching for mll-like clusters could reveal the distribution of these systems and potentially identify novel lanthanophore structures. Given that many bacteria encode lanthanide-dependent enzymes, it seems likely that lanthanophore biosynthesis is more widespread than currently appreciated, but most systems may produce molecules structurally distinct from methylolanthanin.

Finally, the ecological and evolutionary context for lanthanophore biosynthesis remains largely unexplored. Do environmental lanthanide concentrations and bioavailability vary sufficiently to impose selective pressure for metallophore-based acquisition? How do bacteria compete for lanthanides in mixed communities, and do different species' metallophores show differential selectivity that partitions lanthanide resources? In plant-associated environments where Methylorubrum species thrive, what is the relative importance of lanthanide-dependent versus calcium-dependent methylotrophy, and how does metallophore production influence the competitive fitness of these bacteria? Addressing these ecological questions will require field studies, microbial community analyses, and experimental evolution approaches that go beyond the biochemistry and cell biology that have dominated lanthanide biology research to date.

## References

**bailey-2018-aerobactin-biosynthesis**: Bailey DC, Alexander E, Rice MR, Drake EJ, Mydy LS, Aldrich CC, Gulick AM. Structural and functional delineation of aerobactin biosynthesis in hypervirulent Klebsiella pneumoniae. J Biol Chem. 2018 May 18;293(20):7841-7852. doi: 10.1074/jbc.RA118.002798. PMID: 29618511; PMCID: PMC5961048.

**bailey-2020-iuca-ordered-mechanism**: Mydy LS, Bailey DC, Patel KD, Rice MR, Gulick AM. The Siderophore Synthetase IucA of the Aerobactin Biosynthetic Pathway Uses an Ordered Mechanism. Biochemistry. 2020 Jun 16;59(23):2143-2153. doi: 10.1021/acs.biochem.0c00250. PMID: 32432457; PMCID: PMC7325057.

**carroll-2018-nis-review**: Carroll CS, Moore MM. Ironing out siderophore biosynthesis: a review of non-ribosomal peptide synthetase (NRPS)-independent siderophore synthetases. Crit Rev Biochem Mol Biol. 2018 Aug;53(4):356-381. doi: 10.1080/10409238.2018.1476449. PMID: 29863423.

**juma-2022-siderophore-methylobacterium**: Juma PO, Fujitani Y, Alessa O, Oyama T, Yurimoto H, Sakai Y, Tani A. Siderophore for Lanthanide and Iron Uptake for Methylotrophy and Plant Growth Promotion in Methylobacterium aquaticum Strain 22A. Front Microbiol. 2022 Jul 7;13:921635. doi: 10.3389/fmicb.2022.921635. PMID: 35875576; PMCID: PMC9301485.

**patel-2025-nis-review**: Patel KD, Fisk MB, Gulick AM. Discovery, functional characterization, and structural studies of the NRPS-independent siderophore synthetases. Crit Rev Biochem Mol Biol. 2024 Dec;59(6):447-471. doi: 10.1080/10409238.2025.2476476. Epub 2025 Mar 14. PMID: 40085133.

**roszczenko-2020-lanthanide-homeostasis**: Roszczenko-Jasińska P, Vu HN, Subuyuj GA, Creasor R, Buzzard CL, Lichtarge TJ, Good NM, Sousa EHS, Martinez-Gomez NC. Gene products and processes contributing to lanthanide homeostasis and methanol metabolism in Methylorubrum extorquens AM1. Sci Rep. 2020 Jul 29;10(1):12663. doi: 10.1038/s41598-020-69401-4. PMID: 32728125; PMCID: PMC7391723.

**zytnick-2024-methylolanthanin**: Zytnick AM, Gutenthaler-Tietze SM, Aron AT, Reitz ZL, Phi MT, Good NM, Petras D, Daumann LJ, Martinez-Gomez NC. Identification and characterization of a small-molecule metallophore involved in lanthanide metabolism. Proc Natl Acad Sci USA. 2024 Aug 6;121(32):e2322096121. doi: 10.1073/pnas.2322096121. PMID: 39078674; PMCID: PMC11317620.


## Citations

1. bailey-2018-aerobactin-biosynthesis-abstract.md
2. bailey-2018-aerobactin-biosynthesis-summary.md
3. bailey-2020-iuca-ordered-mechanism-abstract.md
4. bailey-2020-iuca-ordered-mechanism-summary.md
5. carroll-2018-nis-review-abstract.md
6. carroll-2018-nis-review-summary.md
7. juma-2022-siderophore-methylobacterium-abstract.md
8. juma-2022-siderophore-methylobacterium-summary.md
9. patel-2025-nis-review-abstract.md
10. patel-2025-nis-review-summary.md
11. roszczenko-2020-lanthanide-homeostasis-abstract.md
12. roszczenko-2020-lanthanide-homeostasis-summary.md
13. zytnick-2024-methylolanthanin-abstract.md
14. zytnick-2024-methylolanthanin-summary.md