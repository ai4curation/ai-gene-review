---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-23T21:16:39.085790'
end_time: '2026-01-23T21:36:23.439154'
duration_seconds: 1184.35
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: STOM
  gene_symbol: STOM
  uniprot_accession: P27105
  protein_description: 'RecName: Full=Stomatin {ECO:0000312|HGNC:HGNC:3383}; AltName:
    Full=Erythrocyte band 7 integral membrane protein {ECO:0000303|PubMed:1883838};
    AltName: Full=Erythrocyte membrane protein band 7.2 {ECO:0000312|HGNC:HGNC:3383};
    AltName: Full=Protein 7.2b {ECO:0000303|PubMed:8825639};'
  gene_info: Name=STOM {ECO:0000312|HGNC:HGNC:3383}; Synonyms=BND7 {ECO:0000312|HGNC:HGNC:3383},
    EPB72 {ECO:0000303|PubMed:8825639};
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the band 7/mec-2 family. .
  protein_domains: Band-7_stomatin-like. (IPR043202); Band_7. (IPR001107); Band_7/SPFH_dom_sf.
    (IPR036013); Band_7/stomatin-like_CS. (IPR018080); Stomatin_HflK_fam. (IPR001972)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 19
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P27105
- **Protein Description:** RecName: Full=Stomatin {ECO:0000312|HGNC:HGNC:3383}; AltName: Full=Erythrocyte band 7 integral membrane protein {ECO:0000303|PubMed:1883838}; AltName: Full=Erythrocyte membrane protein band 7.2 {ECO:0000312|HGNC:HGNC:3383}; AltName: Full=Protein 7.2b {ECO:0000303|PubMed:8825639};
- **Gene Information:** Name=STOM {ECO:0000312|HGNC:HGNC:3383}; Synonyms=BND7 {ECO:0000312|HGNC:HGNC:3383}, EPB72 {ECO:0000303|PubMed:8825639};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the band 7/mec-2 family. .
- **Key Domains:** Band-7_stomatin-like. (IPR043202); Band_7. (IPR001107); Band_7/SPFH_dom_sf. (IPR036013); Band_7/stomatin-like_CS. (IPR018080); Stomatin_HflK_fam. (IPR001972)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "STOM" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'STOM' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **STOM** (gene ID: STOM, UniProt: P27105) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Stomatin (STOM): A Comprehensive Research Report

## 1. Introduction

Stomatin (STOM), also known as erythrocyte band 7 integral membrane protein or protein 7.2b, is a 31.5 kDa monotopic membrane protein belonging to the evolutionarily ancient band 7/mec-2 family [hiebl-dirschmied-1991-cloning-abstract]. First identified as a major component of the human erythrocyte membrane, stomatin is characterized by the presence of a conserved SPFH (stomatin/prohibitin/flotillin/HflK/C) domain, also referred to as the band 7 or prohibitin homology (PHB) domain. The protein was named after hereditary stomatocytosis, a hemolytic anemia in which stomatin is notably absent from red blood cell membranes, though paradoxically no mutations in the STOM gene itself have been found in this condition [fricke-2005-ohst-trafficking-abstract].

Stomatin functions primarily as a membrane-organizing scaffolding protein that regulates the activity of multiple ion channels and membrane transporters through direct protein-protein interactions. The protein associates with cholesterol-rich lipid rafts, forms higher-order oligomeric structures, and recruits its target proteins to these specialized membrane domains [rungaldier-2017-stomatin-structure-function-abstract]. Beyond its well-established roles in transport regulation, recent research has revealed unexpected functions in cell division, lipid metabolism, and innate immunity. This review synthesizes current understanding of stomatin's molecular function, subcellular localization, structural features, and roles in physiological and pathological contexts, with particular emphasis on its conserved role in regulating mechanosensation through ion channel modulation.

## 2. Protein Structure and Membrane Topology

### 2.1 Domain Organization

Human stomatin is encoded by the STOM gene and consists of 287 amino acids. The protein contains several functionally important regions: an N-terminal membrane-anchoring domain, a central SPFH/band 7 domain (also called the stomatin domain), and a C-terminal coiled-coil domain essential for oligomerization [hiebl-dirschmied-1991-cloning-abstract]. The SPFH domain spans approximately residues 86-213 in mouse stomatin and adopts a mixed α/β-fold similar to other SPFH family members [brand-2012-stomatin-dimer-abstract].

### 2.2 Unique Hairpin-Loop Membrane Topology

Unlike typical transmembrane proteins, stomatin adopts a distinctive monotopic membrane topology characterized by a hydrophobic hairpin-loop structure. In this configuration, a short hydrophobic stretch of approximately 29 residues near the N-terminus inserts into the membrane but does not traverse it completely, leaving both the N- and C-termini exposed to the cytoplasm [kadurin-2009-proline-topology-abstract]. This topology is critically dependent on a highly conserved proline residue (Pro-47) located in the middle of the hydrophobic domain. When this proline is mutated to serine, the entire stomatin pool adopts a single-pass transmembrane configuration and loses its ability to localize to detergent-resistant membrane domains (lipid rafts), demonstrating that the hairpin-loop formation is inefficient and requires this conserved proline residue [kadurin-2009-proline-topology-abstract].

### 2.3 Post-Translational Modifications

Stomatin undergoes palmitoylation at multiple cysteine residues, particularly Cys-30 and Cys-87. Palmitoylation of Cys-87 is essential for attachment of the SPFH domain to the plasma membrane, while Cys-30 resides within the intramembrane domain and provides additional membrane anchoring [rungaldier-2017-stomatin-structure-function-abstract]. These post-translational modifications, combined with the hydrophobic hairpin structure, result in a biochemical profile similar to caveolins and other integral scaffolding proteins.

### 2.4 Crystal Structure and Oligomerization

Crystallographic studies of the mouse stomatin SPFH domain revealed that the basic building block is a "banana-shaped dimer" formed through an intermolecular β-sheet at the C-terminus of the stomatin domain, burying approximately 600 Å² of surface area per molecule [brand-2012-stomatin-dimer-abstract]. This dimerization is functionally critical; disrupting the dimer interface through the V197P mutation abolishes stomatin's ability to modulate acid-sensing ion channels (ASICs). Beyond dimers, stomatin assembles into ring-like cylindrical oligomers with an outer diameter of approximately 8 nm, representing higher-order structures built from banana-shaped dimeric building blocks [brand-2012-stomatin-dimer-abstract]. The coiled-coil domain at the C-terminus is essential for this oligomerization, and association with cholesterol-rich membranes appears to be a prerequisite for oligomer formation [rungaldier-2017-stomatin-structure-function-abstract].

A crucial functional element identified in the crystal structure is a hydrophobic pocket at the concave face of the stomatin dimer, with a volume of approximately 350 Å³. This pocket can accommodate small hydrophobic peptides and exhibits dynamic open-closed behavior. Mutation of this pocket (T182W) eliminated stomatin's inhibitory function on ASIC3 and ASIC2a channels despite maintaining proper protein folding and localization, establishing the hydrophobic pocket as essential for ion channel regulation [brand-2012-stomatin-dimer-abstract].

## 3. Subcellular Localization

### 3.1 Lipid Raft Association

Stomatin is primarily localized to cholesterol-rich membrane microdomains known as lipid rafts. In erythrocytes, along with flotillin-1 and flotillin-2, stomatin is among the most abundant integral proteins of lipid raft fractions isolated by detergent resistance assays [mairhofer-2002-platelet-abstract]. Stomatin has been identified as a cholesterol-binding protein, with two domains important for cholesterol-rich membrane association: the CRAC/CARC domain (residues 55-68) and the ORA/CARC domain (residues 263-273). Both domains contribute equally to lipid raft localization [rungaldier-2017-stomatin-structure-function-abstract]. A highly conserved proline residue in the hydrophobic domain has also been proposed to directly bind cholesterol and is necessary for ion channel regulation [kadurin-2009-proline-topology-abstract].

### 3.2 Distribution Across Cell Types

While initially characterized in erythrocytes, stomatin is widely expressed across many tissues and cell types. Expression has been documented in visceral pleura, pericardium, vena cava, and over 200 other cell types and tissues. Beyond the plasma membrane, stomatin localizes to specific subcellular compartments depending on cell type. In platelets, stomatin is found predominantly at the α-granular membrane rather than the plasma membrane. Upon platelet activation by calcium ionophore or thrombin, stomatin translocates to the plasma membrane, undergoes calpain-mediated cleavage, and is sorted into released microvesicles, suggesting a role in α-granule organization and function [mairhofer-2002-platelet-abstract].

Stomatin-carrying endosomes have been observed to be highly dynamic and interact with lipid droplets, suggesting potential roles in intracellular lipid transport. In sensory neurons, stomatin and its homologs localize along neuronal processes, particularly in mechanosensory cells where they form complexes with ion channels [huang-1995-mec2-abstract].

## 4. Molecular Function: Ion Channel and Transporter Regulation

### 4.1 Modulation of Acid-Sensing Ion Channels (ASICs)

One of the best-characterized functions of stomatin is its modulation of acid-sensing ion channels (ASICs), proton-gated sodium channels involved in sensory neuron function. Stomatin co-immunoprecipitates and co-localizes with ASIC proteins in heterologous cells, and functionally alters their gating properties [price-2004-stomatin-asic-abstract].

The effects of stomatin differ depending on the ASIC subtype. For ASIC3, stomatin potently reduces acid-evoked currents without affecting steady-state protein levels or surface expression, indicating a direct effect on channel gating or conductance. For ASIC2a and heteromeric ASICs, stomatin accelerates the desensitization rate without affecting current amplitude. Detailed mechanistic studies identified that regulation requires two distinct sites on ASIC3: the distal C-terminus (containing a di-leucine motif at positions 488-489) that is critical for formation of the stomatin-ASIC3 complex, and the first transmembrane domain (TM1) that is required only for the regulatory effect [price-2004-stomatin-asic-abstract, brand-2012-stomatin-dimer-abstract].

### 4.2 Regulation of Glucose Transporter GLUT1

Stomatin directly associates with and modulates the glucose transporter GLUT1, one of the most abundant proteins in human erythrocytes. Co-immunoprecipitation experiments demonstrated that stomatin specifically interacts with GLUT1 through its C-terminal 42-amino acid segment, while neither band 3 (the most abundant erythrocyte membrane protein) nor actin showed similar interaction patterns, indicating specificity [zhang-1999-stomatin-glut1-association-abstract].

Functionally, overexpression of stomatin results in a 35-50% reduction in the basal rate of glucose transport, without affecting GLUT1 protein levels or surface expression. This indicates that stomatin decreases the "intrinsic" transport activity of GLUT1 through protein-protein interaction [zhang-2001-stomatin-glut1-abstract].

Notably, stomatin acts as a molecular switch that partly converts GLUT1 from a glucose transporter into a transporter for L-dehydroascorbic acid (DHA), an oxidized form of ascorbic acid. During human erythropoiesis, glucose transport decreases despite a more than 1000-fold increase in GLUT1 transcripts, while GLUT1-mediated DHA transport is dramatically enhanced. Stomatin expression inversely regulates the relative transport of glucose versus DHA by GLUT1. This functional switch appears unique to mammals unable to synthesize vitamin C (humans, apes, guinea pigs), providing a compensatory mechanism for ascorbic acid uptake in species that lack de novo synthesis capability [montel-hagen-2008-dha-uptake-abstract].

### 4.3 Modulation of Anion Exchanger 1 (AE1/Band 3)

Stomatin also modulates the activity of anion exchanger 1 (AE1, also known as band 3 or SLC4A1), the major erythrocyte membrane protein responsible for Cl⁻/HCO₃⁻ exchange. Proximity ligation assays confirmed direct interaction between stomatin and AE1 in both recombinant cells and erythrocytes [genetet-2017-ae1-modulation-abstract].

Functional studies revealed that stomatin-deficient red blood cells from patients with overhydrated hereditary stomatocytosis exhibit 47% decreased permeability to bicarbonate and 42% decreased chloride efflux compared to normal erythrocytes. Conversely, cells overexpressing stomatin showed 30% elevated AE1 activity compared to cells with only endogenous stomatin expression. Thus, stomatin positively regulates AE1 transport activity through direct protein-protein interaction [genetet-2017-ae1-modulation-abstract].

### 4.4 Interaction with Aquaporin-1 and Other Transporters

Comprehensive proteomic analysis using chemical cross-linking and mass spectrometry identified additional stomatin interaction partners in erythrocyte membranes. Major partners include GLUT1, AE1 (band 3), and the water channel aquaporin-1 (AQP1). Minor interacting proteins include ferroportin-1, urea transporters, nucleoside transporters, the plasma membrane calcium pump, CD47, and flotillins [rungaldier-2013-stomatin-interactions-abstract].

These findings support a model in which stomatin functions as a membrane-bound scaffolding protein within cholesterol-rich domains, organizing and modulating multiple transport proteins. Immunopurified stomatin complexes analyzed by blue native PAGE revealed major complexes of >500 kDa, approximately 300 kDa, and 130 kDa, all containing stomatin, band 3, and GLUT1 as major components [rungaldier-2013-stomatin-interactions-abstract].

### 4.5 Modulation of NTCP Bile Salt Transporter in Hepatocytes

Beyond erythrocyte transporters, stomatin regulates bile salt transport in hepatocytes through interaction with the sodium taurocholate cotransporting polypeptide (NTCP/SLC10A1). NTCP is expressed at the basolateral membrane of hepatocytes where it mediates uptake of conjugated bile acids and serves as the hepatocyte entry receptor for hepatitis B and D viruses [appelman-2020-ntcp-bile-abstract].

Proteomic screening identified stomatin as an NTCP-interacting protein, and this interaction was validated in human liver samples, demonstrating physiological relevance. Both stomatin and NTCP localize to lipid rafts at the plasma membrane. Functionally, both stomatin overexpression and knockdown increased NTCP-mediated taurocholate uptake, though the mechanisms differ: in stomatin-depleted cells, NTCP abundance at the plasma membrane increased, while overexpression modulated NTCP function without affecting surface expression [appelman-2020-ntcp-bile-abstract]. This complex regulatory relationship suggests stomatin fine-tunes bile salt uptake through multiple mechanisms, potentially influencing hepatic bile acid homeostasis and viral entry.

## 5. Role in Cell Division and Lipid Metabolism

### 5.1 Stomatin in Cytokinesis

Recent research has uncovered an unexpected role for stomatin in cell division. Time-lapse microscopy of stomatin-depleted HeLa cells revealed that the predominant defect is late-stage cytokinesis failure, with a smaller percentage of cells displaying chromosome segregation defects during mitosis [dona-2022-cytokinesis-lipid-abstract]. Proteomic studies have identified stomatin in midbodies, the site of final cleavage between dividing cells, suggesting that stomatin's primary role is during late stages of cytokinesis.

Importantly, key cytokinesis proteins including microtubules, actin, the septin SEPT9, the abscission protein CHMP2A (a member of the ESCRT-III complex), and the cytokinetic regulator RACGAP1 do not mislocalize in stomatin-depleted cells. This indicates that stomatin's effects on cell division are not mediated through gross mislocalization of canonical cytokinesis machinery, but rather through other mechanisms, possibly involving membrane dynamics or lipid organization at the cleavage furrow.

### 5.2 Stomatin and Lipidome Remodeling

Although stomatin is not a lipid biosynthetic enzyme, its depletion causes significant changes to cellular lipidomes. Specifically, stomatin depletion reduces ether lipids and phosphatidylcholines (PCs) while altering the balance of phosphatidylethanolamine (PE) species [dona-2022-cytokinesis-lipid-abstract]. The overall abundance of PC species decreased, while PE levels showed a net increase.

Remarkably, addition of exogenous phosphatidylcholines rescues stomatin-induced cytokinesis defects, providing direct evidence that stomatin interfaces with lipid metabolism. During cell division, stomatin's mobility on the plasma membrane changes, supporting the requirement for highly regulated physical interactions between membrane lipids and this cell division protein [dona-2022-cytokinesis-lipid-abstract]. These findings connect stomatin's established role as a lipid raft-associated scaffolding protein with new functions in regulating membrane lipid composition during critical cellular processes.

## 6. Evolutionary Conservation: Lessons from the C. elegans Homolog MEC-2

### 6.1 MEC-2 in Touch Sensation

The significance of stomatin in mechanosensation was first established through studies of its nematode homolog MEC-2 in *Caenorhabditis elegans*. The mec-2 gene is required for the function of six touch receptor neurons; mutants are touch-insensitive despite morphologically normal touch cells. The central region of MEC-2 shows high similarity to human stomatin, suggesting conserved function [huang-1995-mec2-abstract].

MEC-2-LacZ fusion proteins localize along the processes of touch receptor neurons, with this localization requiring an N-terminal signal disrupted by mutations in mec-12 (α-tubulin). This led to the hypothesis that MEC-2 links the mechanosensory channel to the microtubule cytoskeleton, enabling mechanotransduction through microtubule displacement-triggered channel activation [huang-1995-mec2-abstract].

### 6.2 MEC-2 Regulation of DEG/ENaC Channels

Electrophysiological studies demonstrated that MEC-2 dramatically enhances the activity of the mechanosensory channel complex formed by MEC-4 and MEC-10 (members of the DEG/ENaC family). When co-expressed in *Xenopus* oocytes, MEC-2 increased channel activity approximately 40-fold and allowed currents to be detected with wild-type MEC-4/MEC-10 that were undetectable without MEC-2 [goodman-2002-mec2-degenac-abstract].

Interestingly, while stomatin typically inhibits channel currents (as with ASIC3), MEC-2 potentiates MEC-4/MEC-10 activity. This suggests that stomatin-domain proteins can either enhance or suppress ion channel activity depending on the specific channel and cellular context. The conserved presence of stomatin-like proteins and DEG/ENaC family channels across vertebrates and invertebrates implies that this regulatory relationship has ancient evolutionary origins and may have important implications for mammalian mechanosensation and nociception [goodman-2002-mec2-degenac-abstract, price-2004-stomatin-asic-abstract].

### 6.3 Phase Transitions in Mechanotransduction

Recent work has revealed that MEC-2 undergoes liquid-to-solid phase transitions that are functionally important. In a liquid-like state, MEC-2 condensates facilitate transport along neurites with varying caliber. Upon reaching their cellular target, MEC-2 condensates transition to a solid-like state capable of sustaining mechanical stress over long timescales during body wall touch, providing a focus for force transmission to the ion channel.

## 7. The Stomatin Family: STOML1, STOML2, STOML3, and Podocin

### 7.1 Overview of Family Members

The human genome encodes five stomatin-related genes: STOM (stomatin), STOML1, STOML2, STOML3, and NPHS2 (podocin). All share a conserved stomatin/SPFH domain and the capacity for membrane association, though they differ in expression patterns and specific functions.

STOML1 is highly expressed in brain and at lower levels in heart, skeletal muscle, and dorsal root ganglion sensory neurons where, like stomatin, it modulates ASIC channel activity. STOML2 localizes to mitochondria where it binds cardiolipin, stabilizing the inner mitochondrial membrane and creating scaffolds for supramolecular respiratory complexes. STOML2 lacks the typical N-terminal hydrophobic membrane anchor of other family members.

### 7.2 STOML3 in Piezo Channel Sensitization

STOML3 has emerged as particularly important for mechanosensation in sensory neurons. In mouse skin mechanoreceptors, molecular-scale displacements of approximately 13 nm are sufficient to gate mechanosensitive currents. Remarkably, in the absence of STOML3, displacement thresholds increase by one order of magnitude. STOML3 brings the activation threshold for Piezo1 and Piezo2 channels down to approximately 10 nm, enabling detection of molecular-scale stimuli relevant for fine touch [poole-2014-piezo-tuning-abstract].

STOML3 achieves this sensitization by controlling membrane mechanics through cholesterol binding. STOML3 localizes to cholesterol-rich lipid rafts, and in sensory neurons, cholesterol depletion and STOML3 deficiency similarly attenuate mechanosensitivity while modulating membrane mechanics [qi-2015-stoml3-membrane-stiffening-abstract]. This mechanism has therapeutic implications: small-molecule inhibitors of STOML3 oligomerization have been developed that effectively silence touch receptors and reverse touch-evoked pain associated with nerve injury or diabetic neuropathy, suggesting the STOML3-cholesterol interaction as a potential target for chronic pain management.

### 7.3 Podocin in Kidney Function

Podocin (NPHS2) is specifically localized to the slit diaphragm of podocytes, specialized epithelial cells covering kidney glomerular capillaries. Sharing approximately 44% homology with stomatin through its conserved PHB domain, podocin interacts with nephrin, NEPH1, and the TRPC6 calcium channel. Podocin acts as a molecular switch determining the preferred mode of TRPC6 activation: it reduces sensitivity to mechanical stimuli while facilitating activation by diacylglycerol analogs.

Mutations in NPHS2 cause autosomal recessive steroid-resistant nephrotic syndrome (SRNS), accounting for approximately 18% of SRNS cases. More than 100 different NPHS2 mutations have been identified. Loss of podocin function would result in profound hyperactivation of TRPC6 channels in foot processes, potentially leading to calcium overload as a shared pathogenic mechanism in glomerular diseases caused by mutations in either NPHS2 or TRPC6 genes.

## 8. Role in Innate Immunity

### 8.1 Stomatin in Macrophage Antifungal Defense

Recent studies have revealed an important role for stomatin in innate immune function, particularly in macrophage responses to fungal pathogens. Using CRISPR/Cas9-generated stomatin-deficient macrophage cell lines, researchers demonstrated that stomatin is required for optimal phagocytosis of *Aspergillus fumigatus* conidia, a major human fungal pathogen [goldmann-2023-dectin1-macrophage-abstract].

Mechanistically, stomatin is involved in the recruitment of the β-glucan receptor dectin-1 to both the plasma membrane and the phagosomal membrane. In stomatin knockout macrophages, only 30% of cells were dectin-1 positive after 24 hours of culture, compared to 70% of wild-type cells. Furthermore, stomatin promotes phagosome maturation by fostering fusion of phagosomes with lysosomes. In stomatin-deficient cells infected with pigmentless conidia, phagosome-lysosome fusion was reduced, vATPase recruitment to phagosomes was impaired, and tumor necrosis factor alpha (TNF-α) production was diminished [goldmann-2023-dectin1-macrophage-abstract]. These findings establish stomatin as a lipid raft component that facilitates pathogen recognition receptor localization and phagosomal maturation during antifungal immunity.

### 8.2 Stomatin in Neutrophil Function

Stomatin also plays a role in neutrophil biology, with particular relevance to inflammatory conditions. Stomatin expression is upregulated in neutrophils following severe burn injury, where it promotes neutrophil degranulation and contributes to vascular leakage and lung damage during the early inflammatory response. Mechanistically, stomatin enhances the binding of primary granules to the cytoskeletal protein F-actin, facilitating granule mobilization and content release.

Importantly, genetic knockout of stomatin in mice partially inhibited excessive neutrophil degranulation following burn injury, potentially by reducing primary granule production and weakening granule-cytoskeleton interactions. Stomatin-deficient mice showed significantly reduced lung injury and vascular leakage compared to wild-type animals. These findings suggest that stomatin may represent a therapeutic target for controlling excessive inflammation in conditions characterized by neutrophil hyperactivation.

## 9. Disease Associations

### 9.1 Overhydrated Hereditary Stomatocytosis (OHSt)

Stomatin is notably absent from erythrocyte membranes in overhydrated hereditary stomatocytosis (OHSt), a variably compensated macrocytic hemolytic anemia characterized by red cells with slit-like lucencies (stomata), markedly increased cation permeability, and erythrocyte overhydration. Paradoxically, no mutations in the STOM gene have been identified in OHSt patients; stomatin protein production appears normal, suggesting that loss of stomatin is a secondary change [fricke-2005-ohst-trafficking-abstract].

Studies of erythroid cell cultures from OHSt patients revealed that stomatin immunoreactivity is present in progenitor cells but remains restricted to multivesicular complexes and the nuclear area during development, never reaching the plasma membrane. This suggests stomatin is "an innocent passenger in a more fundamental trafficking abnormality" [fricke-2005-ohst-trafficking-abstract].

OHSt is actually caused by heterozygous mutations in the RHAG gene (encoding Rh-associated glycoprotein), with the F65S mutation representing a hotspot. The RHAG mutations occur in predicted transmembrane regions and are thought to widen the pore, allowing cation passage. The mechanism by which RHAG mutations lead to stomatin mistrafficking remains incompletely understood.

Functionally, stomatin-deficient erythrocytes from OHSt patients exhibit approximately 50% reduction in Cl⁻/HCO₃⁻ exchange activity, while glucose uptake is increased and DHA transport is decreased. The absence of stomatin thus has measurable consequences for erythrocyte transport function [genetet-2017-ae1-modulation-abstract, montel-hagen-2008-dha-uptake-abstract].

### 9.2 Cancer Associations

Altered stomatin expression has been reported in various cancers. Decreased stomatin expression predicts poor prognosis in HER2-positive breast cancer. Stomatin's ability to control neutrophil degranulation, modulate transporter protein activity, and influence membrane organization may contribute to its roles in cancer progression and metastasis. The mechanisms underlying these associations remain areas of active investigation.

## 10. Open Questions

Several important questions about stomatin biology remain unresolved:

1. **Mechanism of OHSt pathogenesis**: Why do RHAG mutations lead to stomatin mistrafficking? What is the functional relationship between RhAG and stomatin that causes secondary stomatin loss?

2. **Selectivity of ion channel modulation**: Why does stomatin inhibit some channels (ASIC3) while its homolog MEC-2 potentiates others (MEC-4/MEC-10)? What determines whether a stomatin-domain protein will enhance or suppress channel activity?

3. **Dynamics of oligomer assembly**: How is stomatin oligomerization regulated in cells? What signals control the assembly and disassembly of stomatin ring structures, and how does this relate to functional states?

4. **Coordination with other scaffolding proteins**: How do stomatin, flotillins, and prohibitins cooperate or compete in organizing membrane domains? Do they form higher-order hetero-oligomeric complexes?

5. **Cell division mechanisms**: How does stomatin influence lipid metabolism and membrane dynamics during cytokinesis? Does stomatin interact directly with cytokinesis machinery or act indirectly through lipid organization?

6. **Immune function specificity**: What determines stomatin's differential effects on macrophage versus neutrophil function? Are these tissue-specific adaptations of a common scaffolding mechanism?

7. **Therapeutic potential**: Can stomatin-targeting compounds be developed for chronic pain management, inflammatory disorders, or cancer? The success of STOML3 oligomerization blockers in pain models provides proof-of-concept but stomatin-specific therapeutics remain unexplored.

8. **NTCP regulation and viral entry**: Does stomatin's modulation of NTCP affect hepatitis B/D virus entry into hepatocytes? Could targeting this interaction have antiviral therapeutic applications?

## 11. References

1. **[appelman-2020-ntcp-bile-abstract]** Appelman MD, Robin MJD, Vogels EWM, Wolzak C, Vos WG, Vos HR, Van Es RM, Burgering BMT, Van de Graaf SFJ. The Lipid Raft Component Stomatin Interacts with the Na+ Taurocholate Cotransporting Polypeptide (NTCP) and Modulates Bile Salt Uptake. Cells. 2020 Apr 16;9(4):986. PMID: 32316189. DOI: 10.3390/cells9040986

2. **[brand-2012-stomatin-dimer-abstract]** Brand J, Smith ES, Schwefel D, Lapatsina L, Poole K, Omerbašić D, Kozlenkov A, Behlke J, Lewin GR, Daumke O. A stomatin dimer modulates the activity of acid-sensing ion channels. EMBO J. 2012 Sep 5;31(17):3635-46. PMID: 22850675. DOI: 10.1038/emboj.2012.203

3. **[dona-2022-cytokinesis-lipid-abstract]** Donà F, Özbalci C, Paquola A, Ferrentino F, Terry SJ, Storck EM, Wang G, Eggert US. Removal of Stomatin, a Membrane-Associated Cell Division Protein, Results in Specific Cellular Lipid Changes. J Am Chem Soc. 2022 Oct 5;144(39):18069-18074. PMID: 36136763. DOI: 10.1021/jacs.2c07907

4. **[fricke-2005-ohst-trafficking-abstract]** Fricke B, Parsons SF, Knöpfle G, von Düring M, Stewart GW. Stomatin is mis-trafficked in the erythrocytes of overhydrated hereditary stomatocytosis, and is absent from normal primitive yolk sac-derived erythrocytes. Br J Haematol. 2005 Oct;131(2):265-77. PMID: 16197460. DOI: 10.1111/j.1365-2141.2005.05742.x

5. **[genetet-2017-ae1-modulation-abstract]** Genetet S, Desrames A, Chouali Y, Ripoche P, Lopez C, Mouro-Chanteloup I. Stomatin modulates the activity of the Anion Exchanger 1 (AE1, SLC4A1). Sci Rep. 2017 Apr 7;7:46170. PMID: 28387307. DOI: 10.1038/srep46170

6. **[goldmann-2023-dectin1-macrophage-abstract]** Goldmann M, Schmidt F, Cseresnyés Z, Jaeger E, Hoefgen M, Svensson CM, Albrecht J, Grunert O, Hafner S, Figge MT, Vylkova T, Hillmann F, Brakhage AA. The Lipid Raft-Associated Protein Stomatin Is Required for Accumulation of Dectin-1 in the Phagosomal Membrane and for Full Activity of Macrophages against Aspergillus fumigatus. mSphere. 2023 Feb 21;8(1):e0052322. PMID: 36719247. DOI: 10.1128/msphere.00523-22

7. **[goodman-2002-mec2-degenac-abstract]** Goodman MB, Ernstrom GG, Chelur DS, O'Hagan R, Yao CA, Chalfie M. MEC-2 regulates C. elegans DEG/ENaC channels needed for mechanosensation. Nature. 2002 Feb 28;415(6875):1039-42. PMID: 11875573. DOI: 10.1038/4151039a

8. **[hiebl-dirschmied-1991-cloning-abstract]** Hiebl-Dirschmied CM, Entler B, Glotzmann C, Maurer-Fogy I, Stratowa C, Prohaska R. Cloning and nucleotide sequence of cDNA encoding human erythrocyte band 7 integral membrane protein. Biochim Biophys Acta. 1991 Aug 27;1090(1):123-124. PMID: 1883838. DOI: 10.1016/0167-4781(91)90047-p

9. **[huang-1995-mec2-abstract]** Huang M, Gu G, Ferguson EL, Chalfie M. A stomatin-like protein necessary for mechanosensation in C. elegans. Nature. 1995 Nov 16;378(6554):292-5. PMID: 7477350. DOI: 10.1038/378292a0

10. **[kadurin-2009-proline-topology-abstract]** Kadurin I, Huber S, Gründer S. A single conserved proline residue determines the membrane topology of stomatin. Biochem J. 2009 Mar 15;418(3):587-94. PMID: 19032151. DOI: 10.1042/BJ20081662

11. **[mairhofer-2002-platelet-abstract]** Mairhofer M, Steiner M, Mosgoeller W, Prohaska R, Salzer U. Stomatin is a major lipid-raft component of platelet alpha granules. Blood. 2002 Aug 1;100(3):897-904. PMID: 12130500. DOI: 10.1182/blood.v100.3.897

12. **[montel-hagen-2008-dha-uptake-abstract]** Montel-Hagen A, Kinet S, Manel N, Mongellaz C, Prohaska R, Battini JL, Delaunay J, Sitbon M, Taylor N. Erythrocyte Glut1 triggers dehydroascorbic acid uptake in mammals unable to synthesize vitamin C. Cell. 2008 Mar 21;132(6):1039-48. PMID: 18358815. DOI: 10.1016/j.cell.2008.01.042

13. **[poole-2014-piezo-tuning-abstract]** Poole K, Herget R, Lapatsina L, Ngo HD, Lewin GR. Tuning Piezo ion channels to detect molecular-scale movements relevant for fine touch. Nat Commun. 2014 Mar 24;5:3520. PMID: 24662763. DOI: 10.1038/ncomms4520

14. **[price-2004-stomatin-asic-abstract]** Price MP, Thompson RJ, Eshcol JO, Wemmie JA, Benson CJ. Stomatin modulates gating of acid-sensing ion channels. J Biol Chem. 2004 Dec 17;279(51):53886-91. PMID: 15471860. DOI: 10.1074/jbc.M407708200

15. **[qi-2015-stoml3-membrane-stiffening-abstract]** Qi Y, Andolfi L, Frattini F, Mayer F, Lazzarino M, Hu J. Membrane stiffening by STOML3 facilitates mechanosensation in sensory neurons. Nat Commun. 2015 Oct 7;6:8512. PMID: 26443885. DOI: 10.1038/ncomms9512

16. **[rungaldier-2013-stomatin-interactions-abstract]** Rungaldier S, Oberwagner W, Salzer U, Csaszar E, Prohaska R. Stomatin interacts with GLUT1/SLC2A1, band 3/SLC4A1, and aquaporin-1 in human erythrocyte membrane domains. Biochim Biophys Acta. 2013 Mar;1828(3):956-66. PMID: 23219802. DOI: 10.1016/j.bbamem.2012.11.030

17. **[rungaldier-2017-stomatin-structure-function-abstract]** Rungaldier S, Umlauf E, Mairhofer M, Salzer U, Thiele C, Prohaska R. Structure-function analysis of human stomatin: A mutation study. PLoS One. 2017 Jun 2;12(6):e0178646. PMID: 28575093. DOI: 10.1371/journal.pone.0178646

18. **[zhang-1999-stomatin-glut1-association-abstract]** Zhang JZ, Hayashi H, Ebina Y, Prohaska R, Ismail-Beigi F. Association of stomatin (band 7.2b) with Glut1 glucose transporter. Arch Biochem Biophys. 1999 Dec 1;372(1):173-8. PMID: 10562431. DOI: 10.1006/abbi.1999.1489

19. **[zhang-2001-stomatin-glut1-abstract]** Zhang JZ, Abbud W, Prohaska R, Ismail-Beigi F. Overexpression of stomatin depresses GLUT-1 glucose transporter activity. Am J Physiol Cell Physiol. 2001 May;280(5):C1277-83. PMID: 11287341. DOI: 10.1152/ajpcell.2001.280.5.C1277


## Citations

1. appelman-2020-ntcp-bile-abstract.md
2. brand-2012-stomatin-dimer-abstract.md
3. dona-2022-cytokinesis-lipid-abstract.md
4. fricke-2005-ohst-trafficking-abstract.md
5. genetet-2017-ae1-modulation-abstract.md
6. goldmann-2023-dectin1-macrophage-abstract.md
7. goodman-2002-mec2-degenac-abstract.md
8. hiebl-dirschmied-1991-cloning-abstract.md
9. huang-1995-mec2-abstract.md
10. kadurin-2009-proline-topology-abstract.md
11. mairhofer-2002-platelet-abstract.md
12. montel-hagen-2008-dha-uptake-abstract.md
13. poole-2014-piezo-tuning-abstract.md
14. price-2004-stomatin-asic-abstract.md
15. qi-2015-stoml3-membrane-stiffening-abstract.md
16. rungaldier-2013-stomatin-interactions-abstract.md
17. rungaldier-2017-stomatin-structure-function-abstract.md
18. zhang-1999-stomatin-glut1-association-abstract.md
19. zhang-2001-stomatin-glut1-abstract.md