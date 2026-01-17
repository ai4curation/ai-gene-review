---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-15T17:25:54.757231'
end_time: '2026-01-15T17:41:05.033207'
duration_seconds: 910.28
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: ATP5MC1
  gene_symbol: ATP5MC1
  uniprot_accession: P05496
  protein_description: 'RecName: Full=ATP synthase F(0) complex subunit C1, mitochondrial
    {ECO:0000305}; AltName: Full=ATP synthase lipid-binding protein; AltName: Full=ATP
    synthase membrane subunit c locus 1 {ECO:0000312|HGNC:HGNC:841}; AltName: Full=ATP
    synthase proteolipid P1; AltName: Full=ATP synthase proton-transporting mitochondrial
    F(0) complex subunit C1; AltName: Full=ATPase protein 9; AltName: Full=ATPase
    subunit c; AltName: Full=Proton-conducting channel, ATP synthase F(0) complex
    subunit c {ECO:0000305}; Flags: Precursor;'
  gene_info: Name=ATP5MC1 {ECO:0000312|HGNC:HGNC:841}; Synonyms=ATP5G1 {ECO:0000312|HGNC:HGNC:841};
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
citation_count: 15
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P05496
- **Protein Description:** RecName: Full=ATP synthase F(0) complex subunit C1, mitochondrial {ECO:0000305}; AltName: Full=ATP synthase lipid-binding protein; AltName: Full=ATP synthase membrane subunit c locus 1 {ECO:0000312|HGNC:HGNC:841}; AltName: Full=ATP synthase proteolipid P1; AltName: Full=ATP synthase proton-transporting mitochondrial F(0) complex subunit C1; AltName: Full=ATPase protein 9; AltName: Full=ATPase subunit c; AltName: Full=Proton-conducting channel, ATP synthase F(0) complex subunit c {ECO:0000305}; Flags: Precursor;
- **Gene Information:** Name=ATP5MC1 {ECO:0000312|HGNC:HGNC:841}; Synonyms=ATP5G1 {ECO:0000312|HGNC:HGNC:841};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the ATPase C chain family. .
- **Key Domains:** ATP_synth_F0_csu. (IPR000454); ATP_synth_F0_csu_DDCD_BS. (IPR020537); ATP_synth_F0_csu_sf. (IPR038662); ATPase_proteolipid_c-like_dom. (IPR002379); F/V-ATP_Csub_sf. (IPR035921)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ATP5MC1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ATP5MC1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ATP5MC1** (gene ID: ATP5MC1, UniProt: P05496) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# ATP5MC1: ATP Synthase F(0) Complex Subunit C1

## Introduction and Summary

ATP5MC1 (also known as ATP5G1) encodes the c-subunit of the mitochondrial ATP synthase F(0) complex in humans. This protein is a critical component of the molecular machinery responsible for synthesizing adenosine triphosphate (ATP), the primary energy currency of eukaryotic cells. The ATP synthase complex, localized to the inner mitochondrial membrane, couples the electrochemical proton gradient generated by the electron transport chain to the phosphorylation of ADP, producing ATP through oxidative phosphorylation [boyer-1997-molecular-machine-abstract]. The c-subunit forms an oligomeric ring structure that serves as the rotor of this remarkable molecular machine, directly translocating protons across the membrane to drive rotational catalysis [zhou-2015-bovine-cryo-em-abstract].

Uniquely in mammals, the identical mature c-subunit protein is encoded by three different nuclear genes—ATP5MC1, ATP5MC2 (formerly ATP5G2), and ATP5MC3 (formerly ATP5G3)—located on chromosomes 17, 12, and 2, respectively. Each gene encodes a precursor protein with a distinct mitochondrial targeting presequence, but upon import and processing, all three yield an identical 75-amino acid mature protein that assembles into the functional c-ring [dyer-walker-1993-omim]. This genetic redundancy may reflect the essential nature of this protein for cellular energy production. Beyond its canonical role in ATP synthesis, the c-subunit ring has emerged as a central component in understanding the mitochondrial permeability transition pore (mPTP), a phenomenon implicated in cell death pathways and various degenerative diseases [mnatsakanyan-2020-cring-mpt-abstract].

## Molecular Function and Biochemistry

### Proton Translocation and the Rotary Mechanism

The ATP synthase c-subunit functions as the essential proton-translocating element of the F(0) sector. Each c-subunit contains a conserved glutamate residue (Glu-59 in bovine/human) located in the middle of the second transmembrane helix, positioned within the hydrophobic core of the lipid bilayer [jonckheere-2012-atp-synthase-review-summary]. This glutamate serves as the proton-binding site and is the key functional residue for proton translocation. In its protonated form, the glutamate can exist within the hydrophobic membrane environment; deprotonation requires access to aqueous half-channels formed primarily by the adjacent a-subunit [klusch-2017-proton-translocation-abstract].

The proton translocation mechanism operates as follows: protons from the intermembrane space enter through the luminal half-channel in the a-subunit and protonate the essential glutamate of an adjacent c-subunit. The protonated, electrically neutral glutamate can then partition into the hydrophobic membrane environment. Upon rotation of the c-ring by approximately 320°, the protonated glutamate encounters the matrix-facing half-channel, where the higher pH (~8) favors deprotonation and release of the proton into the mitochondrial matrix [klusch-2017-proton-translocation-abstract]. A strictly conserved arginine residue in the a-subunit (Arg-259 in humans) separates the two half-channels, preventing proton leakage and ensuring unidirectional flow. The electrostatic attraction between this positively charged arginine and the negatively charged deprotonated glutamate generates the force driving net directional rotation of the c-ring [klusch-2017-proton-translocation-abstract].

### The Binding Change Mechanism

The rotational movement of the c-ring is mechanically coupled to the F1 catalytic head through the central stalk (γ-subunit). Paul Boyer's Nobel Prize-winning "binding change mechanism" explains how this rotation drives ATP synthesis [boyer-1997-molecular-machine-abstract]. The three β-subunits of F1 exist in three distinct conformational states at any given moment: open (O), loose (L), and tight (T). Rotation of the γ-subunit, driven by the c-ring, causes sequential conformational changes in each β-subunit. In the tight state, ADP and inorganic phosphate are bound with high affinity and spontaneously condense to form ATP. The conformational change to the open state, driven by γ-rotation, dramatically reduces ATP binding affinity and promotes product release. Each 360° rotation of the c-ring drives one complete cycle through all three states in each β-subunit, producing three ATP molecules [boyer-1997-molecular-machine-abstract].

### Inhibition by Oligomycin

The c-subunit ring is the target of oligomycin, a classical macrolide antibiotic that potently inhibits mitochondrial ATP synthase. High-resolution crystal structures (1.9 Å) of oligomycin bound to the yeast c10-ring revealed that the drug binds to the surface of the ring at the interface between two neighboring c-subunits [symersky-2012-oligomycin-abstract]. The carboxyl side chain of the essential glutamate (Glu-59) forms a hydrogen bond with oligomycin via a bridging water molecule, while the remaining contacts are primarily hydrophobic. Oligomycin naturally partitions into the lipid-water interface and, once bound, becomes an integral component of the proton-coordinating network. As the c-ring rotates, the oligomycin-bound site eventually reaches the a-subunit interface and halts the rotary mechanism by blocking access to the essential carboxylate [symersky-2012-oligomycin-abstract]. The amino acid residues forming this oligomycin-binding site are 100% conserved between human and yeast but differ significantly from bacterial homologs, explaining the differential sensitivity to this inhibitor across species. Mutations in residues Leu53, Ala56, Leu57, and Phe64 of yeast subunit c confer oligomycin resistance by directly disrupting drug binding.

## Structure of the c-Ring

### Stoichiometry and Bioenergetic Implications

Cryo-electron microscopy studies have revealed that mammalian mitochondrial ATP synthases contain a c8-ring—eight c-subunits arranged in an oligomeric ring structure [zhou-2015-bovine-cryo-em-abstract][pinke-2020-mammalian-atp-synthase-abstract]. This stoichiometry differs from other organisms; yeast mitochondria contain c10-rings, and the c-ring stoichiometry varies from 8 to 17 subunits across different species [siebert-2013-stoichiometry-abstract]. The number of c-subunits directly determines the bioenergetic efficiency of the enzyme: since one complete rotation produces three ATP molecules (due to the three β-subunits), the ion-to-ATP ratio is calculated as n/3, where n is the number of c-subunits.

For mammalian ATP synthases with c8-rings, this yields an H+/ATP ratio of 2.67, meaning approximately 2.67 protons are required to synthesize one ATP molecule. This is among the most efficient ratios observed in nature, reflecting the high and relatively stable proton motive force in animal mitochondria, which is maintained primarily as membrane potential (Δψ ≈ 150 mV) rather than pH gradient [siebert-2013-stoichiometry-abstract]. The predicted P/O ratios based on this stoichiometry are approximately 2.7 for NADH-linked substrates and 1.6 for succinate, consistent with experimental measurements. The c-ring stoichiometry is genetically programmed and depends on the sequence of amino acids in the contact region between adjacent subunits, particularly a highly conserved glycine repeat motif (GxGxGxGxG) in the N-terminal α-helix [nirody-2020-evolution-abstract].

### Atomic Structure and Conformational States

High-resolution cryo-EM structures of both bovine and ovine ATP synthase have provided detailed views of the c-ring architecture [zhou-2015-bovine-cryo-em-abstract][pinke-2020-mammalian-atp-synthase-abstract]. Each c-subunit adopts a hairpin-like structure with two transmembrane α-helices connected by a short loop on the matrix side. The eight subunits pack together with their outer helices forming the external surface of the ring and inner helices lining a central pore. The essential glutamate residues are positioned on the outer helices, oriented toward the interface with the a-subunit where proton translocation occurs.

Analysis of bovine ATP synthase revealed seven distinct conformational states showing different modes of bending and twisting within the intact complex [zhou-2015-bovine-cryo-em-abstract]. These conformational fluctuations support a Brownian ratchet mechanism for proton-driven rotation, where thermal fluctuations allow the c-ring to sample multiple rotational positions, with proton binding and release biasing the direction of rotation. The ovine F1F(0) structure further revealed that subunit e anchors a "lipid plug" that caps the central pore of the c-ring under normal physiological conditions [pinke-2020-mammalian-atp-synthase-abstract].

## ATP Synthase Assembly and Biogenesis

The assembly of human mitochondrial ATP synthase is a complex, ordered process that has been elucidated through systematic gene knockout studies [he-2018-assembly-abstract]. The human ATP synthase comprises 29 proteins of 18 different types, with all but two components (ATP6 and ATP8) encoded in nuclear genes, synthesized on cytoplasmic ribosomes, and imported into mitochondria. Disruption of individual genes leads to the formation of characteristic intermediate vestigial complexes that have revealed the assembly pathway.

The key intermediate in human ATP synthase assembly is the F1-c8 complex, in which the fully assembled c8-ring is bound to the F1 catalytic domain and inhibited by the ATPase inhibitor protein IF1 [he-2018-assembly-abstract]. This intermediate is attached to the peripheral stalk with subunits e, f, and g associated with the membrane domain. This complex serves as the template for insertion of ATP6 and ATP8, which are synthesized on mitochondrial ribosomes. The association of ATP6 and ATP8 with the complex is stabilized by the 6.8 proteolipid (equivalent to the yeast j-subunit), which locks these mitochondrially encoded subunits into the membrane assembly. At this point, the complex becomes competent for ATP synthesis. The monomeric ATP synthase complexes subsequently dimerize via interactions between ATP6 subunits and between 6.8 proteolipids. A final nuclear-encoded protein then oligomerizes the dimers into rows along the cristae edges.

## ATP Synthase Dimerization and Cristae Formation

ATP synthase dimers play a fundamental role in shaping mitochondrial morphology by inducing the membrane curvature that generates cristae, the characteristic folds of the inner mitochondrial membrane [blum-2019-dimers-cristae-abstract]. Cryo-electron tomography has revealed that mammalian ATP synthase dimers self-assemble into long (~1 μm) rows positioned at the apex of cristae membranes, where they generate strong local membrane curvature with an outer radius of approximately 17 nm.

The ability of ATP synthase to induce membrane curvature depends critically on dimerization. Reconstitution studies have shown that monomeric ATP synthase in liposomes does not visibly bend membranes or form rows, while dimers spontaneously self-assemble into rows and bend the lipid bilayer [blum-2019-dimers-cristae-abstract]. Subunits e and g at the lateral dimer interface do not directly form dimer contacts but rather enable dimerization by inducing a strong membrane curvature of approximately 100° at the dimer interface. No specific lipids or proteins beyond the ATP synthase dimers themselves are required for row formation and membrane remodeling, though cardiolipin, which comprises approximately 20% of inner membrane lipids, promotes dimer row formation and is essential for proper cristae structure.

The physiological importance of ATP synthase dimerization is underscored by studies in mutants lacking dimers, which fail to develop normal lamellar cristae and instead form single or multiple balloon-shaped vesicles of the inner membrane. This demonstrates that ATP synthase dimers are not merely a consequence of cristae formation but are instead a prerequisite for generating normal mitochondrial architecture.

## Subcellular Localization

ATP5MC1 encodes a nuclear protein that is synthesized in the cytoplasm and subsequently imported into mitochondria. The precursor protein contains a 61-amino acid N-terminal mitochondrial targeting sequence that directs the protein to the mitochondrial matrix, where it is cleaved by matrix peptidases to yield the mature 75-amino acid protein [dyer-walker-1993-omim]. The mature c-subunit is then inserted into the inner mitochondrial membrane as part of the assembled F(0) complex.

The protein localizes specifically to the inner mitochondrial membrane, where it is embedded as part of the F(0) sector of ATP synthase. Multiple copies of subunit c (eight in mammals) assemble to form the c-ring, which spans the membrane and directly contacts the a-subunit to form the proton translocation machinery. The c-ring is positioned at the interface between the membrane-embedded F(0) and the matrix-protruding F1, mechanically coupling proton flow to the catalytic activity in F1 [jonckheere-2012-atp-synthase-review-summary]. Within the inner membrane, ATP synthase is enriched at the cristae ridges, where dimeric rows of the enzyme shape the membrane architecture.

## Post-Translational Modification

The c-subunit undergoes a critical post-translational modification: trimethylation of lysine-43 (Lys-43) by the mitochondrial methyltransferase ATPSCKMT (also known as FAM173B) [malecki-2019-methylation-abstract]. This modification is conserved across metazoans and is required for proper incorporation of the c-subunit into the ATP synthase complex and optimal mitochondrial respiration. Studies using CRISPR/Cas9 knockout of FAM173B demonstrated that loss of Lys-43 methylation results in aberrant assembly of the c-subunit into the ATP synthase complex, decreased ATP-generating capacity, and reduced mitochondrial respiration, including both ATP synthesis-linked and maximal respiration [malecki-2019-methylation-abstract]. This finding underscores that proper post-translational processing of the c-subunit is essential for the full functionality of the ATP synthase complex.

## Role in Mitochondrial Permeability Transition

### The c-Ring as a Pore-Forming Element

Beyond its canonical role in ATP synthesis, the c-subunit ring has been identified as a key structural component of the mitochondrial permeability transition pore (mPTP), a large-conductance channel whose opening leads to mitochondrial dysfunction and cell death [alavian-2014-mptp-pnas-abstract][mnatsakanyan-2020-cring-mpt-abstract]. The mPTP plays critical roles in pathological conditions including stroke, myocardial infarction, and neurodegenerative diseases.

Landmark studies by Alavian et al. demonstrated that the purified c-subunit ring forms a voltage-sensitive channel in reconstituted membrane systems [alavian-2014-mptp-pnas-abstract]. Under normal conditions, the c-ring central pore is occluded by the F1 complex from the matrix side and by a lipid plug and associated proteins (including subunit e and the 6.8PL protein) from the intermembrane space side. However, elevated calcium concentrations promote enlargement of the c-ring and its dissociation from regulatory proteins, enabling pore opening and uncontrolled depolarization of the inner mitochondrial membrane [alavian-2014-mptp-pnas-abstract].

### Structural Basis of mPTP Opening

Cryo-EM studies of calcium-exposed ATP synthase have provided structural insights into mPTP formation [pinke-2020-mammalian-atp-synthase-abstract]. Upon calcium treatment, subunit e retracts from its normal position, potentially "pulling" the lipid plug out of the c-ring central pore. This conformational change, combined with dissociation of F1 from the F(0) complex, would expose the c-ring pore from both sides, creating a large non-selective channel. The "bent-pull" model proposes that the C-terminal helices of subunit e interact with the 6.8PL protein occupying the c-ring central pore; calcium-induced conformational changes in subunit e displace this plug to open the channel [mnatsakanyan-2020-cring-mpt-abstract].

Studies in c-subunit knockout cells have shown that while a cyclosporine A-sensitive channel activity persists, the classic large-conductance (approximately 1.5 nS) mPTP is absent, supporting the c-ring as the primary pore-forming element [mnatsakanyan-2020-cring-mpt-abstract]. Depletion of c-subunits prevents calcium-induced cell death, while overexpression of c-subunits sensitizes cells to death stimuli [alavian-2014-mptp-pnas-abstract].

## Evolutionary Conservation

The ATP synthase complex, including its c-subunit, represents one of the most ancient and highly conserved molecular machines in biology. Phylogenetic analyses indicate that the ATP synthase originated before the Last Universal Common Ancestor (LUCA), with the divergence of F-type and A/V-type ATP synthases occurring more than 4 billion years ago, potentially predating the diversification of Archaea [nirody-2020-evolution-abstract]. Due to the conservation of basic structure and function across all domains of life, ATP synthases provide an important framework for studying major events in the evolution of bioenergetics.

Recent phylogenetic studies have suggested that the c-subunit may represent a distinct evolutionary module, separate from the remainder of the F(0) complex [nirody-2020-evolution-abstract]. The evolutionary story of F-type ATP synthases is complex, and several analyses have assigned a central role to the c-subunit, postulating that the complete F1F(0) ATP synthase evolved from at least four independent modules: the α/β subunits, the c-ring, and the remainder of the F1 and F(0) components separately.

The c-ring stoichiometry varies across species (from 8 to 17 subunits) but is fixed within each species, determined by the genetically encoded sequence of amino acids at the subunit interface. This stoichiometry determines the H+/ATP ratio and thus the bioenergetic efficiency of the enzyme. Interestingly, phylogenetic analysis of c-ring stoichiometry shows no clustering by bioenergetic mode or metabolic lifestyle, suggesting that the F-type ATP synthase is remarkably robust and able to function efficiently as part of diverse electron transport chains and cell types with minimal specific modifications [nirody-2020-evolution-abstract].

## Disease Associations

### Neuronal Ceroid Lipofuscinoses (Batten Disease)

The ATP synthase c-subunit is the major protein component of the storage material that accumulates in lysosomes of patients with neuronal ceroid lipofuscinoses (NCLs), a group of inherited neurodegenerative lysosomal storage disorders collectively known as Batten disease [kominami-1992-ncl-storage-abstract]. This accumulation is observed in the late infantile and juvenile forms of NCL, but not in the infantile form. The stored material consists specifically of subunit c, while other mitochondrial proteins do not accumulate, indicating a selective failure in the degradation of this particular protein.

Studies using pulse-chase analysis demonstrated that the biosynthetic rate of subunit c is normal in affected patients, and various lysosomal protease activities are not substantially altered [ezaki-1995-delayed-degradation-abstract]. Instead, there is a specific delay in the degradation of subunit c after its normal incorporation into mitochondria. The undegraded protein is subsequently transferred to lysosomes through autophagic processes, where it accumulates due to impaired catabolism. This accumulation has been linked to multiple NCL genetic variants, including those affecting CLN2, CLN3, CLN5, and CLN6 genes, suggesting that the degradation pathway for subunit c is particularly vulnerable to lysosomal dysfunction [ezaki-1995-delayed-degradation-abstract].

### Cardiovascular Disease

A naturally occurring variant in ATP5MC1 has been associated with increased susceptibility to damage following hypoxia/reoxygenation injury in patients with ST-elevation myocardial infarction (STEMI) [ncbi-gene-516]. The protein has also been implicated in coronary artery disease susceptibility. These associations likely reflect the central role of ATP synthase in maintaining cellular energy homeostasis during ischemic stress, as well as the potential involvement of the c-ring in mPTP-mediated cell death during ischemia-reperfusion injury.

### Neurodegenerative Diseases

The ATP synthase c-subunit and mPTP have been implicated in the pathophysiology of neurodegenerative diseases including Alzheimer's disease and Huntington's disease [ncbi-gene-516]. In these conditions, mitochondrial dysfunction and dysregulated calcium homeostasis may promote mPTP opening through the c-subunit ring, contributing to neuronal death. The identification of the c-ring as a key component of the mPTP provides potential therapeutic targets for neuroprotection.

## Gene Family and Redundancy

The human genome contains three genes encoding ATP synthase c-subunit: ATP5MC1 (chromosome 17q21.32), ATP5MC2 (chromosome 12p13.3), and ATP5MC3 (chromosome 2q31.1). The original cloning and characterization by Dyer and Walker in 1993 identified ATP5G1 and ATP5G2 and showed that while their mitochondrial import presequences differ, their mature proteins are identical [dyer-walker-1993-omim]. The ATP5MC1 precursor is 136 amino acids with a 61-residue presequence, while ATP5MC2 precursor is 141 amino acids with a 66-residue presequence. Subsequent work by Yan et al. (1994) confirmed that all three genes encode identical 75-amino acid mature proteins.

This genetic redundancy is unusual and may reflect the absolute requirement for c-subunit expression in all mitochondria-containing cells. The different presequences might provide for tissue-specific or condition-specific regulation of import efficiency, or may represent evolutionary vestiges. Phylogenetic analysis suggests that the evolution of nuclear c-subunit genes has involved at least two independent transfers from the mitochondrial genome to the nucleus, followed by several independent episodes of gene loss [nirody-2020-evolution-abstract]. Expression analysis shows ubiquitous expression of ATP5MC1 across human tissues, with highest levels in metabolically active tissues including heart and skeletal muscle [ncbi-gene-516].

## Open Questions

Several important questions remain regarding ATP5MC1 and the c-subunit ring:

1. **Functional significance of three genes**: Why do mammals maintain three genes encoding identical mature proteins? Do the different presequences confer tissue-specific or physiological condition-specific regulation of c-subunit biogenesis?

2. **Precise mPTP molecular mechanism**: While the c-ring has been implicated in mPTP formation, the exact molecular transitions that convert the ATP synthase from an efficient coupling machine to a lethal pore remain incompletely understood. How do the interactions between c-ring, subunit e, 6.8PL, and F1 precisely regulate pore opening?

3. **Therapeutic targeting**: Can the c-subunit ring be specifically targeted to prevent mPTP opening without disrupting normal ATP synthesis? This could have significant implications for treating ischemia-reperfusion injury and neurodegenerative diseases.

4. **Mechanisms of c-subunit accumulation in NCL**: The pathway by which c-subunit is normally degraded and how this is disrupted in various NCL subtypes remains unclear. Understanding this could lead to therapeutic approaches for Batten disease.

5. **Role of trimethylation**: While ATPSCKMT-mediated trimethylation of Lys-43 is required for optimal function, the precise mechanistic role of this modification in c-ring assembly and function is not fully elucidated.

6. **Species variation in c-ring stoichiometry**: What determines the c-ring stoichiometry in different organisms? Why did mammals evolve to use the smaller c8-ring compared to the c10-rings found in fungi?

7. **Dynamic regulation**: Is there dynamic regulation of ATP synthase activity through post-translational modifications of the c-subunit beyond methylation? How might this be affected in disease states?

8. **Dimerization and disease**: What is the relationship between ATP synthase dimerization defects and human disease? Could targeting dimer formation have therapeutic value in disorders of mitochondrial morphology?

## References

- [boyer-1997-molecular-machine-abstract] Boyer PD. The ATP synthase--a splendid molecular machine. Annu Rev Biochem. 1997;66:717-49. PMID: 9242922. DOI: 10.1146/annurev.biochem.66.1.717

- [zhou-2015-bovine-cryo-em-abstract] Zhou A, Rohou A, Schep DG, Bason JV, Montgomery MG, Walker JE, Grigorieff N, Rubinstein JL. Structure and conformational states of the bovine mitochondrial ATP synthase by cryo-EM. eLife. 2015;4:e10180. PMID: 26439008. DOI: 10.7554/eLife.10180

- [klusch-2017-proton-translocation-abstract] Klusch N, Murphy BJ, Mills DJ, Yildiz Ö, Kühlbrandt W. Structural basis of proton translocation and force generation in mitochondrial ATP synthase. eLife. 2017;6:e33274. DOI: 10.7554/eLife.33274

- [pinke-2020-mammalian-atp-synthase-abstract] Pinke G, Zhou L, Sazanov LA. Cryo-EM structure of the entire mammalian F-type ATP synthase. Nat Struct Mol Biol. 2020;27(11):1077-1085. PMID: 32929284. DOI: 10.1038/s41594-020-0503-8

- [mnatsakanyan-2020-cring-mpt-abstract] Mnatsakanyan N, Jonas EA. ATP synthase c-subunit ring as the channel of mitochondrial permeability transition: Regulator of metabolism in development and degeneration. J Mol Cell Cardiol. 2020;144:109-118. PMID: 32461058. DOI: 10.1016/j.yjmcc.2020.05.013

- [alavian-2014-mptp-pnas-abstract] Alavian KN, Beutner G, Lazrove E, et al. An uncoupling channel within the c-subunit ring of the F1FO ATP synthase is the mitochondrial permeability transition pore. Proc Natl Acad Sci USA. 2014;111(29):10580-5. PMID: 24979777. DOI: 10.1073/pnas.1401591111

- [malecki-2019-methylation-abstract] Małecki JM, Willemen HLDM, Pinto R, et al. Lysine methylation by the mitochondrial methyltransferase FAM173B optimizes the function of mitochondrial ATP synthase. J Biol Chem. 2019;294(4):1128-1141. PMID: 30530489. DOI: 10.1074/jbc.RA118.005473

- [kominami-1992-ncl-storage-abstract] Kominami E, Ezaki J, Muno D, Ishido K, Ueno T, Wolfe LS. Specific storage of subunit c of mitochondrial ATP synthase in lysosomes of neuronal ceroid lipofuscinosis (Batten's disease). J Biochem. 1992;111(2):278-82. PMID: 1533218. DOI: 10.1093/oxfordjournals.jbchem.a123749

- [ezaki-1995-delayed-degradation-abstract] Ezaki J, Wolfe LS, Higuti T, Ishidoh K, Kominami E. Specific delay of degradation of mitochondrial ATP synthase subunit c in late infantile neuronal ceroid lipofuscinosis (Batten disease). J Neurochem. 1995;64(2):733-41. PMID: 7830067. DOI: 10.1046/j.1471-4159.1995.64020733.x

- [jonckheere-2012-atp-synthase-review-summary] Jonckheere AI, Smeitink JAM, Rodenburg RJT. Understanding structure, function, and mutations in the mitochondrial ATP synthase. Microb Cell. 2012. PMCID: PMC4415626. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC4415626/

- [siebert-2013-stoichiometry-abstract] Watt IN, Montgomery MG, Runswick MJ, Leslie AGW, Walker JE. ATP synthase: From sequence to ring size to the P/O ratio. Proc Natl Acad Sci USA. 2010. PMCID: PMC2947903. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC2947903/

- [dyer-walker-1993-omim] Dyer MR, Walker JE. Sequences of members of the human gene family for the c subunit of mitochondrial ATP synthase. Biochem J. 1993;293:51-64. Referenced via OMIM entry 603192.

- [symersky-2012-oligomycin-abstract] Symersky J, Osowski D, Walters DE, Mueller DM. Oligomycin frames a common drug-binding site in the ATP synthase. Proc Natl Acad Sci USA. 2012;109(35):13961-5. PMID: 22869738. DOI: 10.1073/pnas.1207912109

- [he-2018-assembly-abstract] He J, Ford HC, Carroll J, Douglas C, Gonzales E, Ding S, Fearnley IM, Walker JE. Assembly of the membrane domain of ATP synthase in human mitochondria. Proc Natl Acad Sci USA. 2018;115(12):2988-2993. PMID: 29440398. DOI: 10.1073/pnas.1722086115

- [nirody-2020-evolution-abstract] Nirody JA, Budin I, Rangamani P. ATP synthase: Evolution, energetics, and membrane interactions. J Gen Physiol. 2020;152(11):e201912475. PMID: 32966553. DOI: 10.1085/jgp.201912475

- [blum-2019-dimers-cristae-abstract] Blum TB, Hahn A, Meier T, Davies KM, Kühlbrandt W. Dimers of mitochondrial ATP synthase induce membrane curvature and self-assemble into rows. Proc Natl Acad Sci USA. 2019;116(10):4250-4255. PMID: 30760595. DOI: 10.1073/pnas.1816556116

- [ncbi-gene-516] NCBI Gene database entry for ATP5MC1 (Gene ID: 516). URL: https://www.ncbi.nlm.nih.gov/gene/516

- Nobel Prize in Chemistry 1997 for Boyer and Walker: https://www.nobelprize.org/prizes/chemistry/1997/boyer/25946-the-binding-change-mechanism/


## Citations

1. alavian-2014-mptp-pnas-abstract.md
2. blum-2019-dimers-cristae-abstract.md
3. boyer-1997-molecular-machine-abstract.md
4. ezaki-1995-delayed-degradation-abstract.md
5. he-2018-assembly-abstract.md
6. jonckheere-2012-atp-synthase-review-summary.md
7. klusch-2017-proton-translocation-abstract.md
8. kominami-1992-ncl-storage-abstract.md
9. malecki-2019-methylation-abstract.md
10. mnatsakanyan-2020-cring-mpt-abstract.md
11. nirody-2020-evolution-abstract.md
12. pinke-2020-mammalian-atp-synthase-abstract.md
13. siebert-2013-stoichiometry-abstract.md
14. symersky-2012-oligomycin-abstract.md
15. zhou-2015-bovine-cryo-em-abstract.md