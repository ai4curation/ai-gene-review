---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-01-30T19:35:01.160793'
end_time: '2026-01-30T19:37:14.810892'
duration_seconds: 133.65
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: SCHPO
  gene_id: atg101
  gene_symbol: atg101
  uniprot_accession: O13978
  protein_description: 'RecName: Full=Autophagy-related protein 101 {ECO:0000303|PubMed:23950735};
    AltName: Full=Meiotically up-regulated gene protein 66 {ECO:0000303|PubMed:16303567};'
  gene_info: Name=atg101 {ECO:0000303|PubMed:23950735}; Synonyms=mug66 {ECO:0000303|PubMed:16303567};
    ORFNames=SPAC25H1.03;
  organism_full: Schizosaccharomyces pombe (strain 972 / ATCC 24843) (Fission yeast).
  protein_family: Belongs to the ATG101 family. .
  protein_domains: ATG101. (IPR012445); ATG101 (PF07855)
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 44
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** O13978
- **Protein Description:** RecName: Full=Autophagy-related protein 101 {ECO:0000303|PubMed:23950735}; AltName: Full=Meiotically up-regulated gene protein 66 {ECO:0000303|PubMed:16303567};
- **Gene Information:** Name=atg101 {ECO:0000303|PubMed:23950735}; Synonyms=mug66 {ECO:0000303|PubMed:16303567}; ORFNames=SPAC25H1.03;
- **Organism (full):** Schizosaccharomyces pombe (strain 972 / ATCC 24843) (Fission yeast).
- **Protein Family:** Belongs to the ATG101 family. .
- **Key Domains:** ATG101. (IPR012445); ATG101 (PF07855)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "atg101" matches the protein description above**
2. **Verify the organism is correct:** Schizosaccharomyces pombe (strain 972 / ATCC 24843) (Fission yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'atg101' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **atg101** (gene ID: atg101, UniProt: O13978) in SCHPO.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of Autophagy-Related Protein 101 (Atg101) in Schizosaccharomyces pombe: Structural Role in Autophagy Initiation Complex Assembly and Stabilization of Atg13

Autophagy-related protein 101 (Atg101) represents a critical yet distinct component of the autophagy initiation machinery in eukaryotes, serving as an essential stabilizing factor and architectural hub within the Atg1 kinase complex in fission yeast Schizosaccharomyces pombe. Unlike its absence in the evolutionarily divergent budding yeast Saccharomyces cerevisiae, Atg101 is present across higher eukaryotes and serves a conserved role in stabilizing the intrinsically unstable HORMA domain of Atg13, thereby enabling the formation of a functional autophagy-initiating complex that responds to nutrient starvation and other cellular stress signals. This report provides a comprehensive analysis of Atg101's molecular structure, protein interactions, cellular localization, mechanistic role in autophagy initiation, and evolutionary significance, grounded in structural biology, biochemical analysis, and genetic evidence from multiple model organisms.

## Protein Structure and Molecular Architecture of Atg101

### HORMA Domain Architecture and Conformational Properties

Atg101 is uniquely structured as a protein composed entirely of a single Hop1, Rev7, and Mad2 (HORMA) domain, an architectural feature that distinguishes it from most other autophagy-related proteins[1][7][8]. The crystal structure of the fission yeast Atg101-Atg13 complex, determined at 3.0 Ångström resolution, reveals that Atg101 adopts an open conformation that structurally resembles O-Mad2 (open-Mad2), the open conformer of the mitotic checkpoint protein Mad2[1]. This is particularly notable because unlike prototypical HORMA domain proteins such as Mad2, which can interconvert between open and closed conformations, Atg101 appears locked in the open state, unable to undergo the conformational transition that characterizes the canonical Mad2 protein architecture[8][47].

The structural determinants underlying Atg101's locked open conformation include key differences in the C-terminal region compared to Mad2[8]. While Mad2 possesses a C-terminal safety belt comprising two β-strands that can traverse and occlude the β-sheet through a conformational rearrangement, Atg101's C-terminus is substantially shorter and forms only a single antiparallel β-strand[8]. The mathematical constraint imposed by this shortened C-terminal region renders the traversal mechanism geometrically impossible, effectively trapping Atg101 in its open state even when bound to its physiological partner, Atg13[8][47]. This structural "locking" represents an important functional adaptation from the ancestral Mad2-like architecture, as the stabilized open conformation appears optimized for maintaining heteromeric interactions with Atg13 rather than undergoing dynamic conformational switching.

### Structural Insertions and Functional Domains

Beyond the core HORMA domain scaffold, Atg101 contains three substantial insertions relative to the canonical Mad2 fold, all positioned at a single pole of the molecule[8]. The first insertion (ext1) results in the formation of an extended finger-like structure containing two short β-strands positioned between α-helix A (αA) and β-strand 2 (β2), while the second insertion (ext2) extends the β4-β5 hairpin through additional strand segments β4' and β5'[8]. These extended regions project outward from the core HORMA domain and have been identified as functional interaction surfaces with unknown binding partners, likely representing an adaptation of the canonical HORMA fold to fulfill novel functions unique to autophagy[8][47]. A third insertion, termed ext3, is located between αC and β6 and contains an irregular helix and a capping loop structure that appears to shield the hydrophobic core of the protein, functionally substituting for structural elements present in Mad2[8].

Most significantly, Atg101 contains a conserved WF finger motif—composed of tryptophan and phenylalanine residues—that has been identified as essential for its autophagy function[1][7][19][22]. Structural analysis reveals that this WF finger exists in conformationally distinct states depending on the protein's interaction context[19][22]. In some structural contexts, such as free Atg101, the WF finger projects outward from the protein core and appears accessible for protein-protein interactions[19]. However, in the human Atg13-Atg101 HORMA heterodimer complex, the WF finger motif is sequestered within a hydrophobic pocket formed at the interface with Atg13, suggesting that the accessibility of this functional motif is dynamically regulated[19][31]. This regulated sequestration mechanism implies that the WF finger's interaction partners are not engaged when Atg101 is bound in the heterodimer state, and that conformational rearrangement or dissociation may be required to expose this motif for downstream interactions[19][22].

## Protein-Protein Interactions and Complex Assembly

### The Atg101-Atg13 Heterodimer: Conservation of Mad2-Like Architecture

The defining molecular function of Atg101 involves its direct, constitutive interaction with Atg13 through their respective HORMA domains[1][2][14]. The Atg101-Atg13 heterodimer forms the structural basis for autophagy initiation complex assembly across higher eukaryotes, and structural analysis of this complex from both fission yeast and human cells reveals a mode of assembly remarkably conserved with the O-Mad2-C-Mad2 conformational heterodimer that forms during mitotic checkpoint control[1][19][31]. In this architectural arrangement, Atg101 adopts the conformational role of O-Mad2 (open conformer), while Atg13 adopts the conformational role of C-Mad2 (closed conformer), creating a stable heteromeric HORMA pair that is distinct from homodimeric assemblies[1][31].

The Atg101-Atg13 interaction interface is extensive and involves both hydrophobic and polar interactions critical for complex stability[27][31][47]. The interface encompasses a large buried surface area with prominent polar residues on the Atg13 side, particularly Ser127 and Arg133, which interact with corresponding residues on Atg101 through a network of hydrogen bonds and electrostatic interactions[27][31]. On the Atg101 side, a central hydrophobic cluster involving residues I152, I153, and V156 forms the core of the interaction interface and is absolutely essential for complex formation[27]. Mutational studies in human cells demonstrate that disruption of these interface residues through substitutions such as I152D/I153D/V156D completely abolishes complex formation and destabilizes both Atg13 and Atg101, preventing their proper cellular function[27]. The robust nature of this interaction—maintained through multiple complementary interaction modes—underscores the fundamental importance of the heterodimer for autophagy regulation.

Critically, Atg13 cannot be stably expressed in isolation without Atg101[27][31]. This structural interdependence means that Atg101 functions as an obligate stabilizer of Atg13's inherently unstable HORMA domain fold[1][2][14]. In the absence of Atg101, Atg13 likely undergoes proteasomal degradation, as the HORMA domain of Atg13 possesses an inherently unstable fold that requires stabilization by the structural scaffolding provided by Atg101[1][2][14]. This stabilization mechanism appears to involve the locked-open conformation of Atg101 providing a rigid structural platform that supports the Atg13 HORMA domain, preventing misfolding and degradation through a process analogous to how O-Mad2 stabilizes C-Mad2 in the mitotic checkpoint system[1].

### Interactions with Other Atg1 Complex Components

In the context of the fission yeast Atg1 complex, Atg101 maintains selective protein-protein interactions with particular subunits while excluding others[2][14]. Biochemical analysis demonstrates that Atg101 directly interacts with Atg13 but does not bind to other core subunits such as Atg1, Atg17, or the mammalian FIP200 ortholog Atg11[2][14]. This selective interaction pattern is conserved across species and suggests that Atg101's primary role within the complex is as a stabilizing factor for Atg13 specifically, rather than as a general scaffold or organizing hub[2][14]. The absence of direct Atg101-Atg17 interaction in fission yeast contrasts with the yeast Atg17-Atg29-Atg31 complex seen in budding yeast, indicating that the Atg1 complex has diverged structurally in different lineages while maintaining its core autophagy-initiating function[2][14].

Atg11, the fission yeast ortholog of mammalian FIP200, interacts strongly with Atg1 and weakly with Atg13 but does not directly interact with Atg101[2]. However, Atg11 is required for Atg1 activation in fission yeast, and the role of Atg11 in mediating Atg1 kinase activation through dimerization represents a conserved mechanism that is independent of Atg101 stabilization of Atg13[37]. This functional separation suggests that while Atg101 and Atg13 form a stable subcomplex essential for complex integrity, the activation of the Atg1 kinase itself is coordinated through parallel interactions involving Atg11 and involves distinct regulatory mechanisms[37].

### Interaction with Phosphatidylinositol 3-Kinase Complex Components

Recent biochemical evidence reveals that Atg101 extends its interaction network beyond the Atg1 complex subunits to contact components of the phosphatidylinositol 3-kinase (PI3K) complex, which is recruited downstream of Atg1 complex activation during autophagy[13][22][39]. The C-terminal region of Atg101, distinct from the HORMA domain and the WF finger motif, has been identified as responsible for mediating interactions with PtdIns3K complex components, including Atg14, Beclin1 (Atg6), and Vps34[13][22][39]. This bridging function between the ULK1 (mammalian ortholog of Atg1) complex and the PtdIns3K complex represents a critical architectural role, as it connects the initial autophagy-initiating kinase complex with the nucleation machinery responsible for generating phosphatidylinositol 3-phosphate (PtdIns3P) at phagophore assembly sites[13].

The interaction between Atg101's C-terminal region and Atg14 has been demonstrated through co-immunoprecipitation and biochemical binding assays[13]. This interaction does not require the WF finger motif, as mutants affecting the WF finger (such as triple alanine substitutions of W110, P111, and F112) do not disrupt binding to the PtdIns3K complex[13][22]. Conversely, C-terminal deletion mutants of Atg101 (designated ATG101ΔC) show significantly decreased interaction with Atg14 while maintaining normal interaction with Atg13[13][22]. This functional compartmentalization suggests that Atg101 contains distinct, non-overlapping domains that mediate different phases of the autophagy initiation process: the HORMA domain stabilizes Atg13, the WF finger recruits unknown downstream factors, and the C-terminal region coordinates with the PtdIns3K nucleation machinery[13].

## Cellular Localization and Dynamic Recruitment to Autophagy Sites

### Pre-autophagosomal Structure Localization

Atg101 is dynamically recruited to punctate structures called the pre-autophagosomal structure (PAS) or phagophore assembly site (PAS) during autophagy induction in fission yeast[2][5][51]. Under nutrient-rich, non-starvation conditions, Atg101 is not visibly concentrated at discrete intracellular structures and is distributed diffusely throughout the cytoplasm[2][5]. However, upon nutrient deprivation through nitrogen starvation, Atg101 rapidly translocates to punctate cytoplasmic structures that co-localize with Atg8, the autophagy-specific ubiquitin-like protein conjugate that serves as a marker for autophagosome formation sites[2][5]. This dynamic translocation is dependent on the presence of functional Atg13, as disruption of the Atg101-Atg13 interaction prevents both Atg13 and Atg101 from efficiently recruiting to the PAS[5][51].

The localization of Atg101 to the PAS depends on upstream signaling events that inactivate the target of rapamycin complex 1 (TORC1) kinase[2]. TORC1 is a master regulator of autophagy that, under nutrient-rich conditions, phosphorylates Atg13 and maintains it in a hypophosphorylated state that reduces its affinity for Atg1 and Atg17, thereby preventing PAS assembly[2][40]. Upon nutrient starvation, TORC1 activity is inhibited (in fission yeast through combined treatment with rapamycin and caffeine, as fission yeast is relatively insensitive to rapamycin monotherapy), leading to rapid dephosphorylation of Atg13[2]. This dephosphorylation promotes Atg13's interaction with Atg1 and Atg17, and this complex then recruits Atg101 as part of the heteromeric Atg13-Atg101 unit[2].

Live-cell imaging studies in mammalian cells expressing fluorescently-tagged Atg101 demonstrate that Atg101 puncta are transient structures with average lifespans of approximately 200 seconds under autophagy-inducing conditions[51]. The formation of Atg101-positive puncta requires phosphatidylinositol 3-phosphate (PtdIns3P) synthesis, as inhibition of PI3K activity with wortmannin substantially reduces both the size of Atg101 puncta and their duration, indicating that sustained PtdIns3P generation at omegasomes (PtdIns3P-rich membrane compartments) is necessary for maintaining Atg101 recruitment[51]. Atg101 puncta emerge nearly simultaneously with omegasomes in most cases, though temporal precedence can vary between individual autophagy induction events[51]. Notably, Atg101 disappears from punctate structures well before the budding step during which nascent autophagosomes are released from the expanding membrane, suggesting that Atg101's function is predominantly during the early nucleation and initial expansion phases of autophagosome biogenesis[51].

### Subcellular Membrane Associations

In addition to its recruitment to the cytoplasmic PAS, Atg101 exists in association with endosomal and vacuolar membranes[2][5]. In non-starved vegetatively growing fission yeast cells, Atg1, Atg11, and Atg18a are observed on the vacuole membrane, providing a membrane-associated pool from which these proteins can be rapidly mobilized upon autophagy induction[2][5]. This membrane association appears to serve as a pre-formed platform that facilitates the rapid assembly of autophagy machinery when nutrient deprivation signals are received. The precise molecular mechanisms governing this membrane association and the identity of membrane-binding motifs on Atg101 remain incompletely characterized, though the palmitoylation site present on the third amino acid (a cysteine residue) of Atg101 may contribute to membrane targeting[26].

## Molecular Mechanisms of Autophagy Initiation

### Role in TORC1-Regulated Autophagy Induction

Atg101 functions within a hierarchical autophagy pathway in which nutrient sensing through the TORC1 kinase represents the primary control node[2][40]. Under nutrient-rich conditions, active TORC1 maintains autophagy in a suppressed state by phosphorylating Atg13, reducing its affinity for Atg1 and preventing assembly of the catalytically active Atg1 kinase complex[2][40]. The Atg101-Atg13 heterodimer, even when formed, cannot efficiently interact with Atg1 and Atg17 when Atg13 is hyperphosphorylated, as the phosphorylation-induced conformational changes reduce the accessibility of Atg1-binding surfaces on Atg13[2][40]. Upon nutrient deprivation, TORC1 activity is rapidly attenuated, triggering dephosphorylation of Atg13 by protein phosphatases[2][40]. This dephosphorylation event is critical for autophagy induction and represents a key regulatory step at which Atg101 plays an essential supporting role.

The dephosphorylated form of Atg13 exhibits increased affinity for both Atg1 and Atg17, and the presence of Atg101 stabilizing Atg13's HORMA domain facilitates this interaction[2]. By maintaining Atg13 in a properly folded, interaction-competent state, Atg101 ensures that dephosphorylated Atg13 can efficiently engage Atg1 and participate in the assembly of the catalytically active complex[2][14]. Notably, the stabilization function of Atg101 is constitutive—Atg101 does not itself respond directly to TORC1 phosphorylation—and rather serves as a structural buffer that enables Atg13 to respond appropriately to dephosphorylation signals[14]. This indirect regulatory mechanism represents an elegant division of labor in which Atg101 acts as a structural determinant while TORC1 provides the upstream signal that initiates autophagy through Atg13 dephosphorylation.

### Atg1 Kinase Activation and Autophosphorylation

Once the Atg1 complex is assembled at the PAS through TORC1 inactivation and Atg13 dephosphorylation, the next critical step involves activation of the Atg1 serine/threonine protein kinase through autophosphorylation[2][37]. In fission yeast, genetic and biochemical evidence demonstrates that Atg11 is the essential activator of Atg1 kinase, and this activation occurs through Atg11-mediated dimerization of Atg1, enabling trans-autophosphorylation between Atg1 molecules[37]. Interestingly, while Atg13 is required for complex assembly and PAS localization, neither Atg13, Atg17, nor Atg101 is individually necessary for Atg1 kinase activation in fission yeast[37]. However, the stabilization of Atg13 by Atg101 is critical for maintaining the overall complex integrity, and deletion of atg101 results in defective assembly of the entire Atg1 complex at the PAS[2][5].

Once activated through Atg11-mediated dimerization, the Atg1 kinase proceeds to phosphorylate multiple downstream substrates at the PAS[2][40][42]. These phosphorylation targets include the class III PI3K complex component Vps34, which undergoes Atg1-dependent phosphorylation at multiple serine/threonine residues[42]. This phosphorylation, while not strictly required for PAS recruitment of Vps34 complex I, is necessary for robust autophagy activity, suggesting that Atg1-dependent phosphorylation enhances PI3K catalytic activity[42]. Additionally, Atg1 phosphorylates ATG9 and other membrane trafficking machinery, and regulates the recruitment and activity of downstream autophagy factors[40][42].

## The WF Finger Motif and Recruitment of Downstream Effectors

### Structural Organization and Regulatory Accessibility

The WF finger motif of Atg101 has emerged as a critical functional domain essential for autophagy, yet its precise molecular targets and mechanisms of activation remain incompletely understood[1][7][19][22]. Structural studies reveal that the WF finger (composed of tryptophan at position 110 and phenylalanine at position 112 in human Atg101) exists in distinct conformational states depending on the protein's interaction context[19][22]. In the isolated structure of human Atg101 determined without Atg13, the WF finger projects prominently outward from the HORMA domain, suggesting an "out" or exposed conformation capable of engaging binding partners[19][31]. However, in the human Atg13-Atg101 HORMA heterodimer complex, the WF finger is folded back onto the Atg101 HORMA domain and sequestered within a hydrophobic pocket formed at the interface with Atg13[19][31]. This sequestration suggests that the WF finger's interaction partners are not engaged when Atg101 is in the stable heterodimer state, and implies a regulatory mechanism whereby the WF finger must undergo conformational rearrangement to access its functional targets.

Mutational analysis targeting the WF finger reveals its functional importance for autophagy[1][7][22]. Triple alanine mutations of the WF finger motif (designated APA mutants or AAA mutants in different studies) result in severe defects in autophagosome formation, impaired LC3 (Atg8 in yeast) turnover, and accumulation of the autophagy adaptor protein p62 (SQSTM1)[13][22]. These defects occur without significantly affecting Atg101's interaction with Atg13 or its C-terminal interaction with PtdIns3K complex components[13][22]. This functional separation indicates that the WF finger mediates recruitment of distinct downstream factors separate from both the Atg13-stabilization function and the PtdIns3K-bridging function of Atg101's C-terminal region[13][22].

### Recruitment of WIPI Family Proteins

The WF finger of Atg101 has been proposed to mediate interaction with WD repeat domain, phosphoinositide interacting protein 1 (WIPI1) and potentially related WIPI proteins[22]. The WIPI proteins are PtdIns3P-binding proteins that contain seven-bladed β-propeller folds and are recruited to omegasomes and expanding phagophores through their capacity to recognize and bind PtdIns3P[2][28]. While the direct binding interaction between Atg101's WF finger and WIPI1 has not been conclusively demonstrated biochemically, the mutational data showing that WF finger mutations prevent autophagosome formation while sparing PtdIns3K complex interaction strongly suggests that the WF finger mediates recruitment of factors necessary for membrane expansion and LC3 conjugation[22].

In fission yeast, three WIPI homologues exist (Atg18a, Atg18b, and Atg18c), and unlike budding yeast where only Atg18 is essential, all three fission yeast WIPI proteins are required for autophagy and play distinct roles[2][5]. Atg18a uniquely serves as a binding platform for recruiting the Atg12-Atg5-Atg16 complex to the PAS, while Atg18b and Atg18c have additional functions in phagophore expansion and maturation[2][5]. The potential recruitment of WIPI proteins by the Atg101 WF finger would position Atg101 as a key orchestrator of the transition from autophagy initiation (Atg1 complex assembly and Atg13 stabilization) to the membrane conjugation systems (Atg12 and LC3 lipidation) necessary for autophagosome formation[22].

## Evolutionary Conservation and Functional Divergence

### Atg101 Distribution Across Eukaryotic Lineages

Atg101 exhibits a remarkable evolutionary distribution pattern that has only recently been fully characterized through systematic bioinformatic analysis[32][50]. Atg101 is absent from the model budding yeast Saccharomyces cerevisiae but is present in multiple fission yeast species, particularly within the Schizosaccharomycetes class[32][50]. Unexpectedly, recent systematic database searches and structural modeling studies reveal that Atg101 is far more broadly distributed among budding yeast species than previously recognized, being present in at least 79 budding yeast species within the Saccharomycetes class, including species phylogenetically related to S. cerevisiae[32][50]. This broader distribution indicates that the loss of Atg101 in S. cerevisiae represents a derived, lineage-specific change rather than a fundamental feature of the budding yeast lineage.

Significantly, Atg101 is generally mutually exclusive with the Atg29-Atg31 subunit pair, which are specific components of the S. cerevisiae Atg1 complex absent in higher eukaryotes and fission yeast[32][50]. This suggests a functional relationship in which Atg101 and the Atg29-Atg31 pair have evolved to fulfill analogous structural roles—stabilizing Atg13 and organizing the Atg1 complex architecture—through different molecular mechanisms. Notably, a small number of budding yeast species have been identified that encode both Atg101 and Atg29-Atg31, suggesting that these may represent transitional evolutionary states or that the two subunit pairs can co-exist in certain organisms[32][50]. The correlation between Atg101 presence and a rod-shaped (rather than S-shaped) Atg17 scaffold architecture suggests that Atg101 stabilizes a particular Atg17 conformer distinct from that stabilized by Atg29-Atg31[32][50].

In higher eukaryotes including mammals, plants, and invertebrates, Atg101 is universally present and appears to have become a core, non-replaceable component of the ULK1 (mammalian ortholog of Atg1) complex[15][56]. In Drosophila, genetic loss of Atg101 results in developmental lethality in approximately 30-50% of animals, with the surviving animals showing severe defects in both developmental autophagy during metamorphosis and starvation-induced autophagy[15]. This requirement for Atg101 in multiple biological processes—developmental autophagy, nutrient-deprivation autophagy, and lifespan regulation—underscores its fundamental importance in maintaining cellular homeostasis throughout eukaryotic evolution[15].

### Evolutionary Origins and Structural Adaptations

The evolutionary origin of Atg101 from a Mad2-like HORMA ancestor represents a fascinating example of functional divergence from a cell cycle regulatory function to metabolic regulation[1][31][47]. The last eukaryotic common ancestor (LECA) likely possessed both Mad2-like proteins involved in mitotic checkpoint control and HORMA domain proteins involved in autophagy regulation, and the Atg101-Atg13 pair appears to have diverged from an ancestral Mad2-like heterodimer that subsequently became locked in the conformational geometry necessary for autophagy function[31][47]. The acquisition of the three extended insertion regions (ext1, ext2, and ext3) in Atg101 relative to canonical Mad2 likely represents adaptations to provide additional protein-protein interaction surfaces specific to autophagy regulation, particularly the WF finger and the C-terminal bridging function[8][47].

Comparative structural analysis between S. pombe and human Atg101-Atg13 complexes reveals a high degree of structural conservation at the interface—with 21% sequence identity between species for Atg13 and 25% for Atg101—despite the substantial evolutionary distance between unicellular fission yeast and mammals[1][31]. The conservation of critical interface residues, the HORMA domain fold, and the WF finger motif across this evolutionary distance indicates strong purifying selection and functional constraint, suggesting that the Atg101-Atg13 interaction represents an ancient and fundamental autophagy mechanism[1][31]. Furthermore, the human Atg101-Atg13 structure at 1.6 Ångström resolution reveals previously unidentified animal-specific hydrophobic pockets at the subunit junction that are absent in the S. pombe complex, indicating that while the core function is conserved, higher eukaryotes have accumulated additional regulatory features[31].

## Biochemical and Biophysical Properties

### Protein Stability and Degradation

Atg101 is subject to post-translational modification through ubiquitination, which regulates its stability and function in mammalian cells[55]. The E3 ubiquitin ligase HUWE1 mediates K48-linked polyubiquitination of Atg101, targeting it for proteasomal degradation[55]. Significantly, this ubiquitination occurs primarily through the C-terminal region of Atg101, the same domain responsible for interacting with the PtdIns3K complex[55]. This suggests that ubiquitination may provide a regulatory mechanism for controlling the interaction between the ULK1 and PtdIns3K complexes, and that Atg101 stability is subject to cellular conditions and regulatory signals[55]. Under nutrient starvation conditions, Atg101 levels are maintained at levels necessary for autophagy induction, but under normal growth conditions, basal levels of HUWE1-mediated ubiquitination may serve to attenuate autophagy signaling[55]. In pancreatic cancer cells, loss of ATG101 through CRISPR-mediated knockout results in severe growth retardation and decreased survival under nutrient starvation, highlighting its critical role in metabolic stress responses[55].

### Conformational Metamorphosis and Rate-Limiting Assembly

Recent in vitro biochemical reconstitution of human autophagy initiation complexes has revealed an unexpected dynamic property of Atg101: both Atg101 and Atg13 undergo an obligatory and rate-limiting conformational metamorphosis prior to binding ATG9A, the integral membrane protein that serves as a platform for initiation complex assembly on membrane systems[54]. This metamorphosis process—reminiscent of the slow spontaneous conformational changes observed in other HORMA domain proteins—acts as a regulatory switch that controls the assembly rate of the initiation super-complex. In the absence of the heteromerization interaction, ATG13 and ATG101 default to an inactive, non-ATG9A-binding state, and metamorphosis takes 18–24 hours for spontaneous conversion[54]. However, the dimerization of ATG13 and ATG101 dramatically accelerates this metamorphosis to approximately 30 minutes, indicating that complex formation provides a cooperative acceleration of conformational rearrangement[54].

Mutants lacking specific metamorphic elements—including ATG13ΔSeatbelt (lacking the C-terminal safety belt region) and ATG101ΔN (lacking the N-terminal region)—fail to rescue autophagy flux in ATG13 and ATG101 knockout cells, despite maintaining normal interactions with other complex components[54]. This finding indicates that the metamorphic process itself is functionally essential, not merely the complex formation, and suggests that proper conformational transition of Atg101 and Atg13 is required for productive interaction with ATG9A and downstream autophagy machinery. This metamorphic regulation may serve as a temporal control mechanism ensuring that autophagy initiation complexes assemble in a regulated manner, preventing inappropriate autophagy activation through premature complex formation[54].

## Biological Processes and Phenotypic Consequences

### Essential Requirement for Autophagy in Fission Yeast

Genetic analysis of fission yeast atg101 deletion mutants (atg101Δ) demonstrates that Atg101 is absolutely essential for autophagy[2][5][53]. The processing of CFP-Atg8, a well-established assay for autophagy flux, is completely blocked in atg101Δ cells, indicating that autophagosome formation cannot occur without Atg101[5][53]. This contrasts with certain other Atg proteins whose deletion results in impaired but residual autophagy activity, suggesting that while some Atg proteins have partially redundant functions or can be partially compensated, Atg101's role is strictly essential. The Atg8 puncta formation assay, which monitors the recruitment and localization of the autophagy-specific ubiquitin-like protein, reveals that atg101Δ cells show markedly reduced and delayed Atg8 puncta formation compared to wild-type cells[5][53]. The puncta that do form are dimmer than wild-type, indicating that the assembly of the PAS is fundamentally compromised in the absence of Atg101[5].

The cellular consequences of atg101 deletion extend to cell growth and survival under nutrient-deprived conditions[5][53]. Wild-type fission yeast cells transferred to nitrogen-free medium activate autophagy and can survive for extended periods through recycling of cellular components, whereas atg101Δ cells show severe growth defects under nitrogen starvation and exhibit reduced cell viability[5][53]. This demonstrates that Atg101 is critical not only for initiating the autophagy machinery but also for ensuring that cells can mount a sufficient autophagy response to maintain homeostasis during nutrient stress.

### Developmental Roles in Drosophila

In Drosophila melanogaster, Atg101 serves essential functions beyond nutrient-deprivation autophagy, playing critical roles in developmental autophagy during metamorphosis and in larval development[15]. Homozygous and hemizygous Atg101⁶ʰ mutant flies (containing a 13-nucleotide frameshift deletion in the atg101 coding region) show semi-lethality, with only 50-70% of mutant animals surviving to adulthood[15]. During the vulnerable larval stages, Atg101 mutant animals display defective developmental autophagy in larval fat bodies in response to nutrient sensing during the transition to pupation[15]. Morphological analysis of larval midguts reveals a delay in midgut cell death during metamorphosis in Atg101 mutants, as the gastric caeca (larval midgut structures) persist longer than normal at 4 hours after puparium formation, indicating that inhibition of developmental autophagy extends the persistence of larval tissues[15].

The adult flies that survive atg101 loss of function display significant reductions in lifespan, with most animals experiencing mortality within the first 10-15 days of adulthood compared to age-matched wild-type controls[15]. Additionally, Atg101 mutant adult flies exhibit mobility defects assessed through climbing assays, with 70-80% of day-2 mutant flies showing impaired climbing ability that progresses to 100% of flies by day 10, indicating a progressive neuromuscular or metabolic decline[15]. These mobility defects are associated with impaired autophagy in neural tissues, as evidenced by increased accumulation of Ref(2)p (the Drosophila ortholog of mammalian p62) in the fly head, indicating impaired autophagic flux in the central nervous system[15]. These phenotypes suggest that Atg101's role extends beyond nutrient sensing to include constitutive autophagy necessary for maintaining cellular homeostasis in metabolically active tissues, particularly the nervous system.

## Integration with the Broader Autophagy Pathway

### Hierarchical Recruitment of Autophagy Components

Atg101's role within the autophagy pathway must be understood in the context of the hierarchical recruitment of autophagy machinery to the PAS. The Atg1 complex, of which Atg101 is a component, represents the first functional unit recruited to the PAS upon autophagy induction[2][40]. This recruitment is dependent on TORC1 inactivation and subsequent Atg13 dephosphorylation, followed by Atg1 kinase activation through Atg11-mediated dimerization. Once the Atg1 complex is assembled and activated, its downstream targets include the class III PI3K complex, which is recruited to the PAS and generates phosphatidylinositol 3-phosphate[2][40][42]. This localized PtdIns3P synthesis creates an "omegasome" platform that recruits PtdIns3P-binding proteins including the WIPI family proteins[2][40]. The ATG12-Atg5-Atg16 complex is subsequently recruited through interactions with WIPI proteins, and finally, the LC3 lipidation system conjugates LC3 to phosphatidylethanolamine on the expanding membrane, creating the mature autophagosome[2][40].

Atg101's positioning at the apex of this hierarchy—as a stabilizer of Atg13 in the primary assembly complex and as a bridge between the Atg1 and PI3K complexes through its C-terminal region—places it in a strategic position to coordinate the initiation and nucleation phases of autophagosome biogenesis. By maintaining Atg13 stability and enabling its interaction with Atg1, Atg101 ensures that the kinase complex can form. By simultaneously bridging to the PI3K complex through its C-terminal domain, Atg101 coordinates the immediate recruitment and activation of the nucleation machinery, creating a coupled system in which initiation and nucleation occur sequentially as components of a coordinated process.

### Coordination with Membrane Systems and Lipid Sources

The role of Atg101 in autophagy extends to coordination with membrane trafficking systems and lipid supply pathways. The ATG9 trafficking system, which involves cycling of the ATG9 integral membrane protein between non-PAS and PAS compartments, provides membrane material for initial autophagosome formation[2][28]. The Atg1 complex, including Atg101, is positioned to regulate ATG9 recruitment and dynamics through kinase-dependent phosphorylation. Additionally, the Atg2-Atg18 complex, which functions as a lipid transfer protein complex that shuttles phospholipids from the endoplasmic reticulum to the expanding phagophore, is recruited downstream of the Atg1 complex activity[28][33][45]. Recent evidence indicates that ATG2A activity is enhanced cooperatively by interaction with the ATG9A-ATG13-ATG101 complex and WIPI4, suggesting that Atg101 contributes to coordinating the activities of multiple membrane-associated complexes[54].

## Structural Determinants of Atg101 Function

### The C-Terminal Region and Functional Compartmentalization

Detailed analysis of the human Atg101 structure in complex with Atg13 reveals that Atg101 possesses functionally distinct regions that mediate different aspects of autophagy initiation[13]. The C-terminal region, composed of approximately the final 30-50 residues of Atg101 and extending beyond the core HORMA domain fold, adopts a β-strand conformation in the free protein but can transition to α-helix or random coil conformations when in complex with Atg13[13]. This flexible C-terminal region protrudes from the HORMA domain core and interacts with downstream molecules, particularly the class III PI3K complex components[13]. The structural plasticity of this region suggests that it serves as a dynamic interface adapted to engage multiple diverse protein partners that are part of the PtdIns3K complex machinery.

The C-terminal region has been identified as a critical target for ubiquitination by HUWE1 and other E3 ligases, indicating that this domain is subject to post-translational regulatory modification[13][55]. Furthermore, C-terminal truncation mutants of Atg101 show significant defects in autophagosome formation despite maintaining normal Atg13 interaction, demonstrating that this region is functionally essential beyond its structural role in complex formation[13]. These observations collectively indicate that the C-terminal region functions as an independent interaction module responsible for recruiting and coordinating with the downstream PtdIns3K nucleation machinery, separate from the HORMA domain's role in Atg13 stabilization[13].

### Extended Insertion Regions and Potential Regulatory Interfaces

The three extended insertion regions (ext1, ext2, and ext3) of Atg101 represent structural features that have been added during evolution through insertion mutations and represent adaptations of the canonical HORMA fold[8][47]. The extended insertion regions form protruding structures at a single pole of the Atg101 molecule, creating interaction surfaces that are absent in canonical Mad2 and likely represent Atg101-specific interaction surfaces[8][47]. While the precise targets of these extended regions remain incompletely characterized, they are likely to represent sites of interaction with autophagy-specific proteins or regulatory factors not present in the mitotic checkpoint system from which the HORMA fold was ancestrally derived[8][47].

The capping loop located within ext3 appears to shield the hydrophobic core of the Atg101 HORMA domain, functionally substituting for the β7-β8 loop present in Mad2[8][47]. This structural adaptation suggests that Atg101 has evolved a mechanism for protecting its hydrophobic interior that differs from Mad2's reliance on conformational switching, consistent with Atg101's locked-open conformation[8][47]. The precise biological significance of these structural modifications remains an important area for future investigation, as they likely encode regulatory features essential for autophagy-specific functions not shared with the mitotic checkpoint system.

## Conclusions and Outstanding Questions

Atg101 represents a remarkable example of functional divergence and evolutionary adaptation, in which a HORMA domain protein has evolved from a role in mitotic checkpoint control to become an essential component of the autophagy initiation machinery. Through its constitutive interaction with Atg13, Atg101 stabilizes an intrinsically unstable HORMA domain, enabling Atg13 to participate in the assembly of a catalytically active Atg1 kinase complex in response to nutrient deprivation signals. Beyond this stabilization function, Atg101 serves as an architectural hub coordinating multiple phases of autophagy initiation through its WF finger motif and C-terminal region, bridging the upstream Atg1 kinase complex with the downstream class III PI3K nucleation machinery. The conformational plasticity and metamorphic properties of Atg101 and Atg13 appear to provide rate-limiting regulatory mechanisms controlling the assembly kinetics of the autophagy initiation super-complex, ensuring that autophagy is initiated in a controlled, temporally regulated manner rather than through uncontrolled spontaneous assembly.

Despite substantial recent progress in understanding Atg101's structure and molecular interactions, critical questions remain unanswered. The precise protein targets of the WF finger motif remain incompletely characterized, though WIPI family proteins represent likely candidates. The molecular mechanisms underlying the metamorphic conformational transitions of Atg101 and Atg13, and the regulatory factors that might accelerate or inhibit these transitions in vivo, require further investigation. The biological significance of the extended insertion regions (ext1, ext2, and ext3) and their interaction partners remain unknown. The post-translational modification of Atg101 through ubiquitination and potentially other modifications, and how these modifications integrate with autophagy signaling networks, deserve deeper investigation. Finally, while the core stabilization and bridging functions of Atg101 appear conserved from fission yeast to mammals, the evolutionary and functional significance of animal-specific features such as the hydrophobic pockets identified in human Atg101 remain to be elucidated.

The study of Atg101 exemplifies how detailed structural and biochemical analysis of individual autophagy components can illuminate both the mechanistic details of cellular homeostatic pathways and the evolutionary processes through which proteins acquire new functions. As autophagy emerges as an increasingly important target for therapeutic intervention in diseases including cancer, neurodegeneration, and metabolic disorders, a complete understanding of its initiation machinery—including the specific roles and regulatory mechanisms of Atg101—becomes increasingly essential for rational drug development and mechanistic understanding of autophagy-associated pathologies.

## Citations

1. https://pubmed.ncbi.nlm.nih.gov/26030876/
2. https://pmc.ncbi.nlm.nih.gov/articles/PMC8997447/
3. https://www.uniprot.org
4. https://www.uniprot.org/uniprotkb/O13978/entry
5. https://journals.plos.org/plosgenetics/article?id=10.1371%2Fjournal.pgen.1003715
6. https://evolution.lichtargelab.org/cgi-bin/report_maker_ls/uniprotTraceServerResults.pl?identifier=O13978
7. https://pmc.ncbi.nlm.nih.gov/articles/PMC4835198/
8. https://www.rcsb.org/structure/4yk8
9. https://febs.onlinelibrary.wiley.com/doi/full/10.1002%2F1873-3468.14717
10. https://febs.onlinelibrary.wiley.com/doi/10.1002/1873-3468.14717
11. https://pmc.ncbi.nlm.nih.gov/articles/PMC6984762/
12. https://pubmed.ncbi.nlm.nih.gov/28976798/
13. https://pmc.ncbi.nlm.nih.gov/articles/PMC6462509/
14. https://www.ncc-gcsp.ac.kr/n_alumni/data/Thesis_Jiyea%20Kim_2019Jan.pdf
15. https://pmc.ncbi.nlm.nih.gov/articles/PMC4598286/
16. https://pubmed.ncbi.nlm.nih.gov/12161753/
17. https://pubmed.ncbi.nlm.nih.gov/24895579/
18. https://www.pombase.org/gene/SPAC25H1.03
19. https://journals.plos.org/plosbiology/article?id=10.1371%2Fjournal.pbio.3000219
20. https://en.wikipedia.org/wiki/Autophagy-related_protein_101
21. https://www.ncbi.nlm.nih.gov/gene?Db=gene&Cmd=DetailsSearch&Term=60673
22. https://maayanlab.cloud/Harmonizome/gene/ATG101
23. https://pmc.ncbi.nlm.nih.gov/articles/PMC12482441/
24. https://pmc.ncbi.nlm.nih.gov/articles/PMC6511744/
25. https://royalsocietypublishing.org/doi/10.1098/rstb.2023.0368
26. https://febs.onlinelibrary.wiley.com/doi/10.1002/1873-3468.14742
27. https://elifesciences.org/articles/58073
28. https://pmc.ncbi.nlm.nih.gov/articles/PMC9266641/
29. https://www.biomolther.org/journal/view.html?doi=10.4062%2Fbiomolther.2024.094
30. https://pmc.ncbi.nlm.nih.gov/articles/PMC8868404/
31. https://pmc.ncbi.nlm.nih.gov/articles/PMC10392759/
32. https://pmc.ncbi.nlm.nih.gov/articles/PMC7337493/
33. https://pmc.ncbi.nlm.nih.gov/articles/PMC7265318/
34. https://febs.onlinelibrary.wiley.com/doi/10.1111/febs.15334
35. https://pmc.ncbi.nlm.nih.gov/articles/PMC4142721/
36. https://journals.biologists.com/jcs/article/126/22/5224/53891/Dynamic-association-of-the-ULK1-complex-with
37. https://www.uniprot.org/citations/16303567
38. https://pmc.ncbi.nlm.nih.gov/articles/PMC11062386/
39. https://pmc.ncbi.nlm.nih.gov/articles/PMC8430637/
40. https://pmc.ncbi.nlm.nih.gov/articles/PMC5869855/
41. https://pmc.ncbi.nlm.nih.gov/articles/PMC6028034/
42. https://www.ncc-gcsp.ac.kr/n_alumni/data/Jae-Yung%20LEE.pdf
43. https://pmc.ncbi.nlm.nih.gov/articles/PMC6975070/
44. https://www.ijbs.com/v20p0751.htm