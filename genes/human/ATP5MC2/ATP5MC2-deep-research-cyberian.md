---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-22T15:06:07.472370'
end_time: '2026-01-22T15:22:00.343985'
duration_seconds: 952.87
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: ATP5MC2
  gene_symbol: ATP5MC2
  uniprot_accession: Q06055
  protein_description: 'RecName: Full=ATP synthase F(0) complex subunit C2, mitochondrial
    {ECO:0000305}; AltName: Full=ATP synthase lipid-binding protein; AltName: Full=ATP
    synthase membrane subunit c locus 2 {ECO:0000312|HGNC:HGNC:842}; AltName: Full=ATP
    synthase proteolipid P2; AltName: Full=ATP synthase proton-transporting mitochondrial
    F(0) complex subunit C2; AltName: Full=ATPase protein 9; AltName: Full=ATPase
    subunit c; Flags: Precursor;'
  gene_info: Name=ATP5MC2 {ECO:0000312|HGNC:HGNC:842}; Synonyms=ATP5G2 {ECO:0000312|HGNC:HGNC:842};
    ORFNames=PSEC0033;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the ATPase C chain family. .
  protein_domains: ATP_synth_F0_csu. (IPR000454); ATP_synth_F0_csu_DDCD_BS. (IPR020537);
    ATP_synth_F0_csu_sf. (IPR038662); ATPase_proteolipid_c-like_dom. (IPR002379);
    F/V-ATP_Csub_sf. (IPR035921)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 13
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q06055
- **Protein Description:** RecName: Full=ATP synthase F(0) complex subunit C2, mitochondrial {ECO:0000305}; AltName: Full=ATP synthase lipid-binding protein; AltName: Full=ATP synthase membrane subunit c locus 2 {ECO:0000312|HGNC:HGNC:842}; AltName: Full=ATP synthase proteolipid P2; AltName: Full=ATP synthase proton-transporting mitochondrial F(0) complex subunit C2; AltName: Full=ATPase protein 9; AltName: Full=ATPase subunit c; Flags: Precursor;
- **Gene Information:** Name=ATP5MC2 {ECO:0000312|HGNC:HGNC:842}; Synonyms=ATP5G2 {ECO:0000312|HGNC:HGNC:842}; ORFNames=PSEC0033;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the ATPase C chain family. .
- **Key Domains:** ATP_synth_F0_csu. (IPR000454); ATP_synth_F0_csu_DDCD_BS. (IPR020537); ATP_synth_F0_csu_sf. (IPR038662); ATPase_proteolipid_c-like_dom. (IPR002379); F/V-ATP_Csub_sf. (IPR035921)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ATP5MC2" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ATP5MC2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ATP5MC2** (gene ID: ATP5MC2, UniProt: Q06055) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# ATP5MC2 (ATP Synthase F(0) Complex Subunit C2, Mitochondrial): A Comprehensive Functional Review

## Introduction and Summary

ATP5MC2 (previously designated ATP5G2) encodes one of the three nuclear-encoded isoforms of the c subunit of mitochondrial ATP synthase, the enzyme complex responsible for the majority of cellular ATP production in eukaryotes [jonckheere-2011-atpsynthase-abstract]. The gene is located on human chromosome 12q13.13 and produces a precursor protein of 141 amino acids, consisting of a 66-amino acid mitochondrial targeting sequence and a 75-amino acid mature protein that is identical to the mature forms produced by its paralogs ATP5MC1 and ATP5MC3 [dyer-1993-human-genes-abstract]. Despite this sequence identity, recent research has established that the three isoforms are functionally non-redundant, with their distinct mitochondrial targeting peptides serving specialized roles in respiratory chain assembly beyond mere protein import [vives-bauza-2010-isoforms-abstract].

The mature subunit c protein functions as a core component of the F0 (proton channel) sector of ATP synthase, where eight copies assemble into the c8-ring that forms the central element of the rotary mechanism driving ATP synthesis [zhou-2015-cryoem-abstract]. Each subunit c contributes a conserved glutamate residue that accepts and donates protons as the ring rotates through the membrane, coupling the proton-motive force generated by the electron transport chain to the mechanical rotation that drives conformational changes in the F1 catalytic domain [xu-2015-atpsynthase-review-abstract]. The proper function of subunit c is absolutely essential for oxidative phosphorylation, and defects in its degradation lead to the devastating neurodegenerative conditions known as the neuronal ceroid lipofuscinoses (Batten disease) [palmer-1992-ceroid-lipofuscinosis-abstract].

## Molecular Function: The Proton Translocation Mechanism

The primary molecular function of ATP synthase subunit c is to serve as the proton carrier in the rotary mechanism of ATP synthesis. Each c-subunit consists of two transmembrane α-helices connected by a short loop, with a critical glutamate or aspartate residue positioned near the center of the second helix [xu-2015-atpsynthase-review-abstract]. In mammalian systems, this corresponds to Glu-59 (using the bovine numbering), which is located within the hydrophobic core of the membrane and functions as the proton donor and acceptor in the translocation pathway [xu-2015-atpsynthase-review-abstract]. This residue is the target of the classical ATP synthase inhibitor N,N′-dicyclohexylcarbodiimide (DCCD), which reacts covalently with the protonated carboxylate and completely abolishes proton translocation [xu-2015-atpsynthase-review-abstract].

The mechanism of proton translocation proceeds through a well-characterized series of steps elucidated by high-resolution cryo-EM structures [klusch-2017-proton-translocation-abstract]. Protons enter from the intermembrane space (or cristae lumen) through a half-channel formed by the a-subunit of F0. This lumenal channel features a funnel-shaped entrance approximately 23 × 37 Å wide that narrows to 4 × 5 Å at its deepest point, directing protons toward the c-ring [klusch-2017-proton-translocation-abstract]. The protons bind to the essential glutamate residue on the c-subunit positioned at the interface with the a-subunit. Upon protonation, the negative charge of the glutamate is neutralized, allowing the side chain to adopt a buried conformation that partitions favorably into the hydrophobic lipid environment [klusch-2017-proton-translocation-abstract]. This protonation event drives the rotation of the c-ring relative to the stationary a-subunit.

A strictly conserved arginine residue (a-Arg239 in the algal structure) positioned between the entry and exit half-channels forms a positively charged "seal" that prevents direct proton leakage across the membrane [klusch-2017-proton-translocation-abstract]. As the c-ring rotates nearly 360 degrees, each protonated glutamate eventually reaches the matrix half-channel. The higher pH of the mitochondrial matrix (approximately 8.0 versus 7.2 in the intermembrane space) favors deprotonation, and the proton is released into the matrix. The now-negatively charged glutamate is electrostatically repelled from the hydrophobic membrane environment and attracted toward the aqueous matrix channel, generating the rotational torque that drives ATP synthesis [klusch-2017-proton-translocation-abstract].

Calculations based on structural data indicate that a membrane potential of 200 mV across the 6 Å distance between the two half-channels generates an electrostatic force capable of producing a torque of 40-60 pN nm on the deprotonated glutamate, values that align with experimental measurements of F1 rotation [klusch-2017-proton-translocation-abstract].

## Structure: The c8-Ring and ATP Synthesis Stoichiometry

Mammalian mitochondrial ATP synthase contains a c-ring composed of exactly eight copies of subunit c, referred to as the c8-ring [zhou-2015-cryoem-abstract][xu-2015-atpsynthase-review-abstract]. This stoichiometry has been confirmed by multiple independent cryo-EM studies of bovine and ovine ATP synthase and is consistently found across mammalian species [pinke-2020-mammalian-atpsynthase-abstract]. The c-ring stoichiometry varies considerably across species, ranging from 8 subunits in mammals to 10 in yeast and up to 15 in some bacteria, with significant implications for bioenergetic efficiency [xu-2015-atpsynthase-review-abstract].

The stoichiometry of the c-ring directly determines the ion-to-ATP ratio of the enzyme, calculated as the number of c-subunits divided by the three catalytic β-subunits in F1 [xu-2015-atpsynthase-review-abstract]. For mammalian mitochondria with a c8-ring, this yields an H+/ATP ratio of approximately 2.67 (8/3), meaning that the translocation of approximately 2.67 protons is required to synthesize one molecule of ATP [xu-2015-atpsynthase-review-abstract]. This relatively low ratio compared to organisms with larger c-rings reflects an evolutionary optimization for ATP synthesis efficiency under the stable metabolic conditions of mammalian mitochondria.

The structure of the c8-ring is stabilized by specific lipid interactions, particularly with cardiolipin, the signature phospholipid of the inner mitochondrial membrane [pinke-2020-mammalian-atpsynthase-abstract]. Recent cryo-EM studies have revealed a previously unknown lipid plug that anchors accessory subunit e to the c-ring, contributing to the structural integrity of the F0 complex [pinke-2020-mammalian-atpsynthase-abstract]. The c-ring is attached to the central stalk (composed of subunits γ, δ, and ε), and as this asymmetric rotor rotates within the α3β3 hexamer of F1, it drives the conformational changes at the three catalytic sites that synthesize ATP through the binding change mechanism [jonckheere-2011-atpsynthase-abstract].

## ATP Synthase Assembly and c-Ring Formation

The assembly of human mitochondrial ATP synthase follows a carefully orchestrated pathway in which the c-ring plays a foundational role [he-2018-assembly-abstract]. Studies using gene-edited human cells have revealed that the c8-ring serves as an essential scaffolding structure upon which the rest of the membrane domain assembles. The assembly process begins with the import of nuclear-encoded c-subunits (from ATP5MC1, ATP5MC2, and ATP5MC3) into mitochondria, where they assemble into the ring structure. This c8-ring then associates with the F1 catalytic domain, forming an F1-c8 intermediate complex that is stabilized by binding of the ATPase inhibitor protein IF1 [he-2018-assembly-abstract].

The F1-c8 complex subsequently binds to the peripheral stalk, creating a larger intermediate that provides the template for the insertion of the mitochondrially-encoded subunits ATP6 (subunit a) and ATP8. This ordering is critical: the nuclear-encoded c-ring must be assembled before the mitochondrial-encoded proton channel subunits can be incorporated [he-2018-assembly-abstract]. Following ATP6/ATP8 insertion, the supernumerary subunits (including 6.8PL and DAPIT) associate to stabilize the complete complex and establish the functional proton channel between ATP6 and the c-ring.

Importantly, removal of the c-ring eliminates downstream assembly of other membrane components, underscoring its foundational importance in the assembly sequence [he-2018-assembly-abstract]. In cells where all three ATP5MC genes are disrupted, a vestigial ATP synthase complex can still form containing the F1 catalytic domain, peripheral stalk, and supernumerary subunits, but it lacks the membrane proteins ATP6 and ATP8 and is therefore non-functional for ATP synthesis [he-2017-mptp-persists-abstract].

## Subcellular Localization

ATP5MC2 and its protein product are localized exclusively to mitochondria. The precursor protein contains a 66-amino acid N-terminal mitochondrial targeting sequence that directs import through the TOM/TIM complexes of the outer and inner mitochondrial membranes [dyer-1993-human-genes-abstract]. Upon import into the mitochondrial matrix, the targeting peptide is cleaved by mitochondrial processing peptidases, generating the mature 75-amino acid subunit c that is subsequently inserted into the inner mitochondrial membrane as part of the c-ring assembly process.

The mature subunit c is an integral membrane protein of the inner mitochondrial membrane, specifically within the F0 sector of ATP synthase. ATP synthase complexes are not uniformly distributed in the inner membrane but are highly concentrated at the curved edges of cristae, where they form dimeric and oligomeric rows that are believed to contribute to cristae morphology [jonckheere-2011-atpsynthase-abstract]. The dimeric organization of ATP synthase, with the two F0 domains angled relative to each other, appears to be important for inducing the membrane curvature characteristic of cristae [pinke-2020-mammalian-atpsynthase-abstract].

## Post-Translational Modification: Lysine-43 Trimethylation

A remarkable post-translational modification conserved across all metazoans is the complete trimethylation of lysine-43 (corresponding to Lys-109 in the human precursor sequence) in the c-subunit [walpole-2015-lysine-trimethylation-abstract]. Mass spectrometric analysis of ATP synthase from 29 metazoan species spanning mammals, reptiles, birds, amphibians, fish, and invertebrates from six phyla revealed that this trimethylation is quantitative—no unmethylated or partially methylated species were detected [walpole-2015-lysine-trimethylation-abstract]. This lysine residue is absolutely conserved throughout metazoa and is likely trimethylated in all of the more than two million extant metazoan species.

The enzyme responsible for this modification was identified as FAM173B, now renamed ATPSCKMT (ATP Synthase C Subunit Lysine N-Methyltransferase) [malecki-2018-methylation-abstract]. CRISPR/Cas9-mediated knockout of FAM173B in mammalian cells completely abolished trimethylation of lysine-43. Importantly, loss of this modification had significant functional consequences: knockout cells displayed aberrant c-ring assembly with accumulation of low-molecular-weight intermediates, approximately 50% reduction in ATP synthesis capacity, and decreased mitochondrial respiration [malecki-2018-methylation-abstract]. The evolutionary conservation of both the modification and its functional importance was demonstrated by the ability of the C. elegans FAM173B ortholog to restore methylation and function in human knockout cells [malecki-2018-methylation-abstract].

Structurally, lysine-43 is located in the loop region near the boundary between the lipid bilayer and the aqueous matrix phase [walpole-2015-lysine-trimethylation-abstract]. Several functions have been proposed for this trimethylation: it may provide a specific binding site for cardiolipin, enhance ring stability during the mechanical stress of rotation, participate in the proton exit pathway, or contribute to the unique stoichiometry of metazoan c-rings [walpole-2015-lysine-trimethylation-abstract]. Notably, unicellular eukaryotes and prokaryotes, which have variable c-ring stoichiometries of 9-15 subunits, lack this trimethylation even when the lysine residue is conserved, suggesting a possible role in determining or stabilizing the c8 stoichiometry characteristic of metazoa [walpole-2015-lysine-trimethylation-abstract].

## The Three Human Isoforms: Non-Redundancy Despite Identical Mature Proteins

Perhaps the most intriguing aspect of subunit c biology is the existence of three nuclear genes—ATP5MC1 (chromosome 17), ATP5MC2 (chromosome 12), and ATP5MC3 (chromosome 2)—that encode identical mature proteins but with different mitochondrial targeting peptides [dyer-1993-human-genes-abstract]. The targeting peptide lengths vary: P1 (ATP5MC1) is 61 amino acids, P2 (ATP5MC2) is 66 amino acids (or 82/123 amino acids in alternatively spliced variants), and P3 (ATP5MC3) is 67 amino acids [vives-bauza-2010-isoforms-abstract].

A landmark study by Vives-Bauza and colleagues (2010) demonstrated that despite encoding identical mature proteins, these three isoforms are functionally non-redundant and cannot substitute for one another [vives-bauza-2010-isoforms-abstract]. Using siRNA knockdown in HeLa cells, the researchers found that silencing each isoform individually produced distinct phenotypes:

- **P1 (ATP5MC1) silencing** resulted in 41% reduction in ATP synthesis, impaired mitochondrial membrane potential, and mitochondrial clustering
- **P2 (ATP5MC2) silencing** caused 48% reduction in ATP synthesis, selective defects in Complex IV (cytochrome c oxidase) assembly with 40% reduction in COX-I levels, respiration impairment, and mitochondrial fragmentation
- **P3 (ATP5MC3) silencing** produced a more modest 20% reduction in ATP synthesis with minimal structural effects

Critically, cross-complementation experiments showed that P1 and P2 were not interchangeable—exogenous P1 rescued P1 knockdown but not P2 knockdown, and vice versa [vives-bauza-2010-isoforms-abstract]. This demonstrates that the functional specificity resides in the targeting peptides themselves. In an elegant experiment, the researchers showed that fusion proteins consisting of just the P1 or P2 targeting peptides attached to fluorescent proteins could rescue the mitochondrial dysfunction in silenced cells, establishing that the targeting peptides have functions beyond protein import [vives-bauza-2010-isoforms-abstract].

The unexpected connection between P2 (ATP5MC2) and Complex IV assembly suggests that the P2 targeting peptide may function as a soluble assembly factor for the respiratory chain, potentially providing chaperone activity for cytochrome c oxidase biogenesis [vives-bauza-2010-isoforms-abstract]. This represents the first documented example of mitochondrial targeting peptides evolving distinct regulatory functions through subfunctionalization, challenging the conventional view of targeting sequences as merely import signals.

In terms of expression patterns, P2 and P3 are equally expressed and approximately four-fold more abundant than P1 at the mRNA level in HeLa cells [vives-bauza-2010-isoforms-abstract]. Studies in other mammalian tissues suggest that ATP5G1 expression is actively regulated in response to physiological stimuli such as developmental stage and cold acclimation, while ATP5G2 and ATP5G3 maintain basal levels of subunit c [vives-bauza-2010-isoforms-abstract].

## Role in the Mitochondrial Permeability Transition Pore

Beyond its essential role in ATP synthesis, subunit c has been implicated as a critical component of the mitochondrial permeability transition pore (mPTP), a large conductance channel that opens in the inner membrane under conditions of calcium overload and oxidative stress [bonora-2013-mpt-abstract]. Opening of the mPTP causes collapse of the mitochondrial membrane potential, mitochondrial swelling, and can trigger cell death through apoptosis or necrosis.

Bonora and colleagues (2013) demonstrated that depletion of subunit c using siRNA inhibited mitochondrial permeability transition, mitochondrial fragmentation, and cell death induced by cytosolic calcium overload and oxidative stress in both HeLa cells and primary rat cortical neurons [bonora-2013-mpt-abstract]. Conversely, overexpression of subunit c accelerated the kinetics of permeability transition. In neurons, subunit c knockdown reduced glutamate-induced neuronal death by approximately 50% [bonora-2013-mpt-abstract].

More recent structural studies have suggested a mechanism for mPTP formation involving the c-ring [pinke-2020-mammalian-atpsynthase-abstract]. Cryo-EM imaging of ATP synthase exposed to calcium showed retraction of subunit e from the c-ring and apparent c-ring disassembly. The authors proposed that calcium triggers extraction of a lipid plug that normally seals the c-ring, potentially converting the c-ring into a large non-specific pore [pinke-2020-mammalian-atpsynthase-abstract].

However, this model has been directly challenged by a landmark study from the Walker laboratory. He and colleagues (2017) generated HAP1-A12 cells in which all three c-subunit genes (ATP5G1, ATP5G2, and ATP5G3) were disrupted using CRISPR-Cas9, completely eliminating subunit c expression [he-2017-mptp-persists-abstract]. Remarkably, these cells retained characteristic mPTP properties: permeability transition could still be triggered by calcium elevation, thapsigargin, or ferutinin, and was still inhibited by cyclosporine A. The authors concluded that "the c-subunit does not provide the PTP," directly contradicting the c-ring hypothesis [he-2017-mptp-persists-abstract].

Current models suggest that multiple proteins may contribute to mPTP formation through functional redundancy. The adenine nucleotide translocase (ANT) has re-emerged as a candidate, with recent studies suggesting a cooperative model in which both ATP synthase components and ANT interact to form the pore. When both protein complexes are fully assembled, ATP synthase may constitute the permeable portion; in the absence of the c-ring, ANT may assume this role. The molecular identity of the mPTP thus remains an active area of investigation with significant implications for understanding cell death mechanisms and potential therapeutic interventions.

## Disease Associations: Neuronal Ceroid Lipofuscinoses

The most significant disease association for ATP synthase subunit c is with the neuronal ceroid lipofuscinoses (NCLs), a group of inherited neurodegenerative storage disorders collectively known as Batten disease [palmer-1992-ceroid-lipofuscinosis-abstract]. These devastating diseases, typically manifesting in childhood, are characterized by progressive loss of vision, seizures, cognitive and motor decline, and premature death.

The seminal work of Palmer and colleagues (1992) established that subunit c of mitochondrial ATP synthase is the major component of the storage material that accumulates in cells of affected patients and animals [palmer-1992-ceroid-lipofuscinosis-abstract]. In the ovine form of the disease and in human late infantile and juvenile NCL, subunit c constitutes more than 50% of the accumulated storage material in lysosomes. Importantly, subunit c does not accumulate in the infantile form of NCL (CLN1), which instead shows accumulation of sphingolipid activator proteins (saposins A and D) [palmer-1992-ceroid-lipofuscinosis-abstract].

The mechanism of subunit c accumulation appears to involve a specific failure in lysosomal degradation rather than increased synthesis [palmer-1992-ceroid-lipofuscinosis-abstract]. Metabolic studies showed that the rate of subunit c synthesis was normal in patient fibroblasts, but degradation was severely impaired, leading to progressive lysosomal accumulation. Normally, subunit c turns over as part of mitochondrial protein quality control and is degraded by lysosomal proteases after mitophagy. The genes mutated in the various forms of NCL (CLN3, CLN6, etc.) encode proteins involved in lysosomal function, and their loss leads to the specific failure to degrade the highly hydrophobic and protease-resistant subunit c.

The storage of subunit c in NCL has important diagnostic implications, as immunohistochemical detection of subunit c accumulation can aid in the diagnosis and classification of these disorders [palmer-1992-ceroid-lipofuscinosis-abstract].

## Expression in Cancer and Metabolic Reprogramming

The expression of ATP synthase subunits, including ATP5MC2, has been examined in the context of cancer metabolism and the Warburg effect. Cancer cells often exhibit altered mitochondrial function, with many tumors showing downregulation of oxidative phosphorylation components in favor of aerobic glycolysis. Studies of clear cell renal cell carcinoma (ccRCC) have found significant downregulation of ATP synthase subunits, with ATP5G2 among the genes showing reduced expression in tumor tissue compared to normal renal tissue. This pattern is consistent with the metabolic reprogramming characteristic of many solid tumors.

Interestingly, not all cancer types show uniform downregulation of c-subunit genes. In HER2-driven mammary tumors, despite consistent downregulation of electron transport chain subunits (Complexes I-IV), a subset of Complex V genes including ATP5G1 and ATP5G2 were maintained at normal levels. This selective preservation of c-ring subunits, which increases the ratio of ATP synthase to electron transport chain components, may represent an adaptive mechanism to maintain oxidative phosphorylation capacity under conditions of reduced electron transport chain content. The functional significance of this differential regulation remains an active area of investigation in cancer metabolism research.

## Open Questions

Several important questions remain regarding ATP5MC2 and subunit c biology:

1. **Mechanism of isoform-specific functions:** While the Vives-Bauza study demonstrated that P2 targeting peptides have unique functions in Complex IV assembly, the precise molecular mechanism remains unknown. How does a cleaved targeting peptide influence cytochrome c oxidase biogenesis? Are there specific binding partners or chaperone functions involved?

2. **Regulation of isoform expression:** What determines the tissue-specific and developmental regulation of the three isoforms? Given their non-redundant functions, understanding their regulation may have implications for metabolic diseases.

3. **Role of lysine trimethylation:** While the importance of lysine-43 trimethylation for c-ring assembly is established, the precise structural and mechanistic basis for this requirement remains unclear. Does the trimethyl group directly contact cardiolipin? Does it influence c-ring stoichiometry?

4. **mPTP controversy:** The role of the c-ring in the mitochondrial permeability transition pore remains debated. Some studies suggest it is essential, while others report mPTP activity in cells lacking subunit c. Resolution of this controversy has important implications for understanding cell death and potential therapeutic interventions.

5. **Therapeutic implications for NCL:** Understanding why subunit c specifically accumulates in NCL and developing strategies to enhance its degradation could lead to treatments for these currently incurable diseases.

6. **Species-specific c-ring stoichiometry:** Why do metazoans universally have c8-rings while other organisms have variable stoichiometries? Is the trimethylation of lysine-43 causally related to the c8 stoichiometry?

## References

1. **jonckheere-2011-atpsynthase-abstract:** Jonckheere AI, Smeitink JAM, Rodenburg RJT. Mitochondrial ATP synthase: architecture, function and pathology. *Journal of Inherited Metabolic Disease*. 2011;35(2):211–225. PMID: 21874297. DOI: 10.1007/s10545-011-9382-9. https://pmc.ncbi.nlm.nih.gov/articles/PMC3278611/

2. **xu-2015-atpsynthase-review-abstract:** Xu T, Pagadala V, Mueller DM. Understanding structure, function, and mutations in the mitochondrial ATP synthase. *Microbial Cell*. 2015;2(4):105–125. PMID: 25938092. DOI: 10.15698/mic2015.04.197. https://pmc.ncbi.nlm.nih.gov/articles/PMC4415626/

3. **bonora-2013-mpt-abstract:** Bonora M, Bononi A, De Marchi E, et al. Role of the c subunit of the FO ATP synthase in mitochondrial permeability transition. *Cell Cycle*. 2013;12(4):674–683. PMID: 23343770. DOI: 10.4161/cc.23599. https://pmc.ncbi.nlm.nih.gov/articles/PMC3594268/

4. **zhou-2015-cryoem-abstract:** Zhou A, Rohou A, Schep DG, et al. Structure and conformational states of the bovine mitochondrial ATP synthase by cryo-EM. *eLife*. 2015;4:e10180. PMID: 26439008. DOI: 10.7554/eLife.10180. https://pubmed.ncbi.nlm.nih.gov/26439008/

5. **pinke-2020-mammalian-atpsynthase-abstract:** Pinke G, Zhou L, Sazanov LA. Cryo-EM structure of the entire mammalian F-type ATP synthase. *Nature Structural & Molecular Biology*. 2020;27(11):1077-1085. PMID: 32929284. DOI: 10.1038/s41594-020-0503-8. https://pubmed.ncbi.nlm.nih.gov/32929284/

6. **malecki-2018-methylation-abstract:** Małecki JM, Willemen HLDM, Pinto R, et al. Lysine methylation by the mitochondrial methyltransferase FAM173B optimizes the function of mitochondrial ATP synthase. *Journal of Biological Chemistry*. 2018;294(4):1128–1141. PMID: 30530489. DOI: 10.1074/jbc.RA118.005473. https://pmc.ncbi.nlm.nih.gov/articles/PMC6349101/

7. **walpole-2015-lysine-trimethylation-abstract:** Walpole TB, Palmer DN, Jiang H, et al. Conservation of Complete Trimethylation of Lysine-43 in the Rotor Ring of c-Subunits of Metazoan Adenosine Triphosphate (ATP) Synthases. *Molecular & Cellular Proteomics*. 2015;14(4):828–840. PMID: 25608518. DOI: 10.1074/mcp.M114.047456. https://pmc.ncbi.nlm.nih.gov/articles/PMC4390263/

8. **vives-bauza-2010-isoforms-abstract:** Vives-Bauza C, Magrané J, Andreu AL, Manfredi G. Novel Role of ATPase Subunit C Targeting Peptides Beyond Mitochondrial Protein Import. *Molecular Biology of the Cell*. 2010;21(1):131–139. PMID: 19889836. DOI: 10.1091/mbc.E09-06-0483. https://pmc.ncbi.nlm.nih.gov/articles/PMC2801706/

9. **klusch-2017-proton-translocation-abstract:** Klusch N, Murphy BJ, Mills DJ, Yildiz Ö, Kühlbrandt W. Structural basis of proton translocation and force generation in mitochondrial ATP synthase. *eLife*. 2017;6:e33274. DOI: 10.7554/eLife.33274. https://elifesciences.org/articles/33274

10. **dyer-1993-human-genes-abstract:** Dyer MR, Walker JE. Sequences of members of the human gene family for the c subunit of mitochondrial ATP synthase. *Biochemical Journal*. 1993;293(1):51–64. PMID: 8328972. https://portlandpress.com/biochemj/article-abstract/293/1/51/30300/

11. **palmer-1992-ceroid-lipofuscinosis-abstract:** Palmer DN, Fearnley IM, Walker JE, et al. Mitochondrial ATP synthase subunit c storage in the ceroid-lipofuscinoses (Batten disease). *American Journal of Medical Genetics*. 1992;42(4):561–567. PMID: 1535179. https://pubmed.ncbi.nlm.nih.gov/1535179/

12. **he-2018-assembly-abstract:** He J, Ford HC, Carroll J, et al. Assembly of the membrane domain of ATP synthase in human mitochondria. *Proceedings of the National Academy of Sciences*. 2018;115(12):2988–2993. PMID: 29440398. DOI: 10.1073/pnas.1722086115. https://pmc.ncbi.nlm.nih.gov/articles/PMC5866602/

13. **he-2017-mptp-persists-abstract:** He J, Ford HC, Carroll J, et al. Persistence of the mitochondrial permeability transition in the absence of subunit c of human ATP synthase. *Proceedings of the National Academy of Sciences*. 2017;114(13):3409–3414. PMID: 28289229. DOI: 10.1073/pnas.1702357114. https://pmc.ncbi.nlm.nih.gov/articles/PMC5380099/


## Citations

1. bonora-2013-mpt-abstract.md
2. dyer-1993-human-genes-abstract.md
3. he-2017-mptp-persists-abstract.md
4. he-2018-assembly-abstract.md
5. jonckheere-2011-atpsynthase-abstract.md
6. klusch-2017-proton-translocation-abstract.md
7. malecki-2018-methylation-abstract.md
8. palmer-1992-ceroid-lipofuscinosis-abstract.md
9. pinke-2020-mammalian-atpsynthase-abstract.md
10. vives-bauza-2010-isoforms-abstract.md
11. walpole-2015-lysine-trimethylation-abstract.md
12. xu-2015-atpsynthase-review-abstract.md
13. zhou-2015-cryoem-abstract.md