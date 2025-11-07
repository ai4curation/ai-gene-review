---
provider: perplexity
model: sonar-deep-research
cached: true
start_time: '2025-11-03T21:37:43.718799'
end_time: '2025-11-03T21:37:43.723919'
duration_seconds: 0.01
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: P48201
  gene_symbol: ATP5MC3
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 43
---

## Question

# Gene Research for Functional Annotation

Please provide a comprehensive research report on the gene ATP5MC3 (P48201) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function. 

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

<think>
The user is asking for a comprehensive research report on the ATP5MC3 gene in humans. Let me break down what I need to cover:

1. The gene ATP5MC3 (encoding ATP synthase membrane subunit C locus 3, also known as P48201)
2. Its primary function - especially the biochemical reaction it catalyzes/substrate specificity
3. Its localization - where in the cell it functions
4. Biological processes and pathways it's involved in
5. Evidence from experimental, structural, evolutionary, or bioinformatic analysis

Let me plan my approach:

**Planning:**

1. **Introduction/Overview**: What is ATP5MC3? Basic identification, localization, disease associations
2. **Structural Properties**: The protein structure, hairpin formation, transmembrane helices
3. **Molecular Function**: The specific role in ATP synthase, proton translocation mechanism
4. **Biochemical Mechanism**: How the c-subunit participates in ATP synthesis, proton-coupled rotation
5. **Complex Assembly and Organization**: How ATP5MC3 assembles into the c-ring, stoichiometry
6. **Post-Translational Modifications**: Lysine methylation by FAM173B
7. **Clinical/Pathological Significance**: Disease associations, particularly dystonia and spastic paraplegia
8. **Evolutionary Context**: Conservation across organisms
9. **Broader Cellular Context**: Role in mitochondrial bioenergetics, oxidative phosphorylation
10. **Conclusion**: Summary and implications

Let me go through the search results and organize them:

**Key Information from Sources:**

From [1][8][16][27][32][53][56]: ATP5MC3 encodes a subunit of mitochondrial ATP synthase, specifically subunit c of the Fo complex. It catalyzes ATP synthesis using an electrochemical gradient of protons. One of three genes encoding this subunit with distinct import sequences but identical mature protein.


ATP5MC3 is located on chromosome 2 with NCBI Gene ID 518. The c subunit functions as the primary transmembrane component across V-type, A-type, and F-type ATP synthases, where it oligomerizes into a rotor ring containing a critical aspartate residue (in F-ATPases) or glutamate (in V-ATPases) that mediates proton transport. The c subunit exhibits amyloidogenic properties, capable of forming β-sheet structures and oligomers in calcium-dependent conditions.

The protein features a characteristic hairpin architecture composed of two transmembrane α-helices, with Asp61 in the second helix playing a crucial role in proton translocation. Post-translational methylation occurs at lysine-43. The c-ring rotates at speeds up to 150 Hz through interaction with the a-subunit, a mechanism recently elucidated via cryo-EM and molecular dynamics simulations that detail both the rotational dynamics and proton transfer pathways. Specific residues like Asp61 are essential for F0 sector function and proton movement across the membrane.

A pathogenic variant (c.318C>G, p.Asn106Lys) in ATP5MC3 has been identified in patients with dystonia and spastic paraplegia, resulting in diminished complex V activity. The c-subunits function cooperatively during rotation, enabling efficient energy coupling. FAM173B methyltransferase catalyzes trimethylation at Lys-43, while the c-ring itself can form a voltage-gated ion channel involved in mitochondrial permeability transition. The oligomeric c-ring structure, along with the broader F1Fo ATP synthase architecture, represents a sophisticated molecular motor system critical for oxidative phosphorylation and mitochondrial biogenesis.

Recent structural insights from cryo-EM have revealed rotary states and dimer configurations, showing how the c-oligomer undergoes hairpin folding with specific packing arrangements. Subunit coupling mechanisms drive γ-subunit rotation, while the OSCP hinge provides flexible coupling through rotary substates. ATP synthase dimers form ribbon-like structures that shape mitochondrial membranes and facilitate cristae formation, with c-ring stoichiometry adapting to meet cellular physiological demands. The F1-ATPase catalytic cycle proceeds through six distinct steps, operating via a 3×120° rotary mechanism that reflects the evolutionary refinement of ATP synthase across diverse organisms.
</think>

# ATP5MC3: Structural and Functional Characterization of a Critical Component of Mitochondrial ATP Synthase

The ATP5MC3 gene encodes a subunit of the mitochondrial ATP synthase complex, specifically the membrane-embedded subunit c of the F₀ portion of the enzyme, also known as the oligomycin sensitivity-conferring protein (OSCP)-interacting proteolipid subunit. This 75-residue peptide plays a central mechanistic role in coupling the electrochemical proton gradient across the inner mitochondrial membrane to the synthesis of adenosine triphosphate (ATP), the universal energy currency of the cell. Recent investigations using cryo-electron microscopy, molecular dynamics simulations, and functional genomics have revealed that ATP5MC3-encoded subunit c participates in a sophisticated rotary mechanism that converts proton translocation into mechanical rotation, ultimately driving ATP synthesis with remarkable efficiency. This report synthesizes current understanding of ATP5MC3's molecular structure, biochemical function, cellular localization, assembly into higher-order complexes, post-translational modification, disease associations, and evolutionary conservation, drawing on both classical biochemical studies and contemporary structural biology approaches.

## Molecular Architecture and Structural Features of Subunit c

ATP5MC3 encodes a small, highly hydrophobic protein that functions as an integral membrane component of the F₀ complex of ATP synthase[1][8][16]. The mature protein, which is 75 residues in length, adopts a characteristic hairpin structure composed of two transmembrane α-helices connected by a small cytoplasmic loop[31]. This distinctive fold is highly conserved from bacteria through eukaryotes, indicating its ancient evolutionary origin and critical functional importance[31]. The structural organization places the first transmembrane helix toward the inner surface of the oligomeric assembly, while the second transmembrane helix orients toward the periphery, creating a specific geometric arrangement that is essential for function[34][54].

The critical functional residue in subunit c is aspartate at position 61 in the second transmembrane helix, which serves as the principal proton-binding site during the catalytic cycle[7][10]. This aspartate residue is positioned at the interface between two interacting c-subunits within the c-ring assembly, occupying a hydrophobic environment shielded from the lipid bilayer by the packing arrangement of the transmembrane helices[34][54][55]. The positioning of Asp61 is particularly significant, as it lies within the center of four transmembrane helices from two neighboring subunits, creating a microenvironment that is uniquely suited to facilitating proton transfer[34]. Structural studies using nuclear magnetic resonance spectroscopy on isolated subunit c have confirmed the hairpin conformation and validated predictions from genetic studies regarding the positioning of functionally important residues[31]. The conserved glycine motif with a GxGxGxG pattern in the transmembrane helices facilitates the tight packing of helices that is essential for maintaining the structural integrity of the c-ring and for allowing the proper presentation of the aspartate residue during catalysis[51].

Beyond the transmembrane helices, subunit c contains a small loop region connecting the two helices on the cytoplasmic side of the membrane. Notably, position 106 in this loop contains a highly conserved residue that serves as a point of contact between the F₀ and F₁ portions of ATP synthase[13][21][50]. This contact region is critical for transmitting the rotary motion generated by proton translocation in F₀ to the catalytic machinery of F₁. A naturally occurring mutation at this position—a change from lysine to asparagine (p.Asn106Lys)—has been identified as causing neurological disease, highlighting the functional importance of this structural feature[13][21].

## The Oligomeric c-Ring: Assembly, Stoichiometry, and Quaternary Structure

In the native ATP synthase complex, ATP5MC3-encoded subunit c proteins do not function as monomers but rather self-assemble into highly ordered oligomeric rings, termed c-rings[25][34][54][55]. The assembly of individual c-subunits into these rings occurs through specific interactions between the hydrophobic surfaces of adjacent monomers, with the "front face" of one subunit packing against the "back face" of the neighboring subunit[34][54]. This arrangement creates a compact hollow cylinder with an outer diameter of approximately 55-60 Ångströms and an inner cavity with a minimal diameter of 11-12 Ångströms[34][54]. Phospholipids are believed to pack within this inner space in the native membrane environment, suggesting that lipid molecules are integral to the structural integrity and potentially the functional properties of the c-ring[34].

The stoichiometry of the c-ring—that is, the number of c-subunit monomers comprising each ring—is species-dependent and varies between 8 and 17 subunits across different organisms[28][44][51]. In mammalian mitochondria, human ATP synthase c-rings typically contain approximately 10 c-subunits, though some evidence suggests variation between tissues and physiological states[25][51]. The stoichiometry of the c-ring is a critical determinant of ATP synthase efficiency, as it directly impacts the ion-to-ATP ratio, a fundamental parameter of cellular bioenergetics[51]. The number of c-subunits in the ring also determines the angular increment by which the rotor advances with each proton translocation event; for a c₁₀ ring, each proton translocation event advances the rotor by approximately 36 degrees, corresponding to a complete 360-degree rotation after ten sequential protonation-deprotonation cycles[38][51].

Recent molecular dynamics and crystallographic studies have revealed that the c-ring stoichiometry is not absolutely fixed but rather can adapt to cellular needs and evolutionary pressures[51]. In the alkaliphilic bacterium *Bacillus pseudofirmus*, whose ATP synthase must operate efficiently at extraordinarily high pH values (above 10), the c-ring contains thirteen subunits, which may confer advantages for functioning under conditions of very low proton-motive force[51]. The precise stoichiometry appears to be determined by subtle structural features in the GxGxGxG motif and surrounding residues that control the tightness of helix packing and the geometry of subunit-subunit interactions[51]. This adaptation of c-ring stoichiometry represents an elegant example of how evolutionary pressures shape the bioenergetic capabilities of organisms inhabiting extreme environments.

## Biochemical Function: The Proton-Translocation Mechanism

The primary biochemical function of ATP5MC3-encoded subunit c is to facilitate directional proton translocation across the inner mitochondrial membrane, coupled to the rotation of the c-ring relative to the stationary a-subunit[1][8][10]. This process is the direct result of the electrochemical proton gradient established by the electron transport chain, where complexes I, III, and IV pump protons from the mitochondrial matrix into the intermembrane space, generating both a concentration gradient and an electrical potential across the membrane[1][39].

The mechanism of proton translocation involves a precisely orchestrated cycle of proton binding and release involving Asp61 of the c-subunit and specific residues of the a-subunit, particularly the critical arginine 210[10][38][41]. Protons from the intermembrane space enter the F₀ complex through an entry half-channel formed at the interface between subunits a and c[38][41]. This entry pathway is composed of hydrophilic residues from both the a-subunit and two neighboring c-subunits, creating an aqueous environment that allows protons to reach the buried aspartate residue[38][41]. Once a proton reaches Asp61 on one of the c-subunits positioned at the a-subunit interface, it protonates the aspartate carboxyl group, converting it from a negatively charged deprotonated state to a neutral protonated form[7][10].

This protonation event triggers a profound conformational change in the c-subunit, particularly affecting the C-terminal transmembrane helix, which undergoes a substantial rotation relative to the N-terminal helix[7][38]. The structural change associated with Asp61 protonation has been quantified through nuclear magnetic resonance and cryo-electron microscopy studies, revealing a twist of approximately 140 degrees between the two helices[7][38]. This conformational change alters the electrochemical interactions between the c-subunit and the a-subunit, reducing the favorable electrostatic interactions and allowing the c-ring to rotate forward[9][38].

The rotational movement is driven by the favorable change in the electrostatic environment; as the protonated Asp61 moves away from the hydrophilic environment of the a-subunit into the hydrophobic lipid bilayer, the c-ring must rotate to bring a new, unprotonated aspartate residue from a neighboring c-subunit into the proton-binding site at the a-subunit interface[9][38]. This rotational movement has been termed the "power stroke" and represents the force that ultimately drives ATP synthesis[9]. As the c-ring rotates and the newly incoming aspartate prepares to be protonated, the previously protonated Asp61 moves to a region near the exit half-channel, also formed at the a/c interface[38][41]. Here, the hydrophilic environment facilitates deprotonation of the aspartate, releasing the proton into the matrix side of the membrane[38][41]. The exit half-channel is also composed of hydrophilic residues from the a-subunit and c-subunits, ensuring that the released proton can proceed toward the matrix[38][41].

Recent molecular dynamics simulations of complete rotary cycles have provided unprecedented atomic-level detail regarding this mechanism[9]. These simulations, performing multi-microsecond atomistic molecular dynamics calculations, have demonstrated that rotation proceeds through dynamic sliding of the ring over the a-subunit surface, with specific intermediates being stabilized by interactions with conserved polar residues[9]. Crucially, these simulations have identified ordered water chains that organize for Grotthuss-type proton transfer—a mechanism in which proton transfer occurs not through free diffusion but through sequential protonation and deprotonation of amino acid residues and water molecules, allowing rapid proton transport without bulk water movement[9].

The simulations have also revealed asymmetry in the free energy landscape that strongly favors forward rotation over backward rotation[9]. After a proton binds to an incoming c-subunit aspartate, a high free energy barrier is established that prevents backward rotation, while the overall free energy gradient strongly favors continued forward rotation[9]. This ratchet-like mechanism, sometimes termed a Brownian ratchet combined with a power stroke, ensures the thermodynamic irreversibility of the process and the directional rotation necessary for ATP synthesis to occur[9].

## Cellular Localization and Mitochondrial Targeting

ATP5MC3 encodes a protein that is synthesized on ribosomes in the cytoplasm and subsequently imported into mitochondria through a well-characterized targeting mechanism[1][6][26]. The mature, functional form of subunit c lacks an N-terminal targeting sequence; instead, it begins directly with the first transmembrane helix[6][26]. However, the nascent protein synthesized from the ATP5MC3 mRNA contains a mitochondrial targeting sequence (MTS) at its N-terminus that is recognized by the translocase of the outer mitochondrial membrane (TOM) complex and the translocase of the inner mitochondrial membrane (TIM) complex[6][26].

Notably, the ATP5MC3 gene is one of three genes—ATP5MC1, ATP5MC2, and ATP5MC3—that encode the identical mature c-subunit protein, each with a distinct mitochondrial import sequence[1][6][8][16][26][27]. After successful translocation across both mitochondrial membranes, the mitochondrial protease MPP (mitochondrial processing peptidase) cleaves the targeting sequence, releasing the mature 75-residue peptide[6][26]. This redundancy of genes encoding the same protein but with different targeting sequences represents an interesting evolutionary feature, possibly allowing fine-tuning of c-subunit import rates or spatial distribution within the mitochondrial compartments[6][26].

Once imported and processed, the mature ATP5MC3-encoded subunit c immediately associates with other c-subunit molecules—products of ATP5MC1 and ATP5MC2—to form the c-ring assembly in the inner mitochondrial membrane[1][6][25]. The c-ring then integrates into the complete F₀ complex through interaction with other subunits, particularly the a-subunit, which is encoded by the mtDNA gene ATP6 and is therefore translated directly on ribosomes localized to the inner mitochondrial membrane[25]. The physical location of c-ring assembly occurs directly at the inner mitochondrial membrane, where the nascent c-subunits can immediately participate in rotor formation.

## Integration into the ATP Synthase Complex and Supramolecular Organization

The ATP5MC3-encoded c-subunit, as a component of the c-ring, represents a crucial structural element of the larger F₀-F₁ ATP synthase complex[1][8][25][33]. This molecular machine consists of two functionally distinct domains: the F₁ catalytic head, which extends into the mitochondrial matrix and contains the catalytic sites for ATP synthesis, and the F₀ domain, which is embedded in the inner mitochondrial membrane and functions as a proton-translocating turbine[1][8][25][33]. The c-ring, of which ATP5MC3-encoded subunits are constituents, forms the core of the rotary element of the F₀ domain, interacting directly with the stationary a-subunit through which protons are channeled[25][33].

The central stalk of ATP synthase, which is composed of the γ, δ, and ε subunits of the F₁ domain, is firmly attached to the c-ring, such that rotation of the c-ring driven by proton translocation directly drives rotation of the γ-subunit within the F₁ catalytic core[8][25][33][44]. This mechanical coupling between F₀ and F₁ is absolute and remarkably efficient—the rotational motion generated by proton translocation is directly converted into conformational changes at the catalytic sites of the β-subunits, where ATP synthesis occurs[33][36][44].

Recent cryo-electron microscopy structures have revealed that the coupling between the F₀ and F₁ domains is not rigid but rather involves a degree of flexibility, particularly at the oligomycin sensitivity-conferring protein (OSCP) subunit, which contains an interdomain hinge[44][57]. This flexible coupling mechanism allows the F₁ head to rotate through approximately 30 degrees at the beginning of each 120-degree primary rotary step, facilitating the coordination between the stoichiometrically mismatched F₀ domain (with 10 c-subunits) and the F₁ domain (with threefold symmetry)[44][57].

In mammalian mitochondria, ATP synthases do not exist as isolated monomers but rather assemble into highly organized supramolecular structures. ATP synthase monomers dimerize through interactions mediated by subunits e, k, i/j, and others, forming stable dimers[22][43][46]. These dimers then organize into long, linear ribbons that are localized specifically at the apex of the cristae—the infoldings of the inner mitochondrial membrane that dramatically increase the surface area available for oxidative phosphorylation[43][46]. The organization of ATP synthases into these dimer ribbons is not an accidental feature but rather serves important functional purposes; the ribbons bend the lipid bilayer locally, with a radius of curvature of approximately 17 nanometers[43][46]. This local membrane curvature creates a "proton trap" effect, concentrating protons in the restricted volume of the cristae lumen and thereby significantly increasing the local pH gradient experienced by the ATP synthase[43][46]. This geometry-dependent enhancement of the local pH gradient is thought to be particularly important for ATP synthesis under conditions of limited proton availability or high energy demand.

## Post-Translational Modification and Regulatory Mechanisms

An important regulatory feature of ATP5MC3-encoded subunit c involves post-translational modification by lysine methylation. In cells, the mature c-subunit undergoes trimethylation at lysine 43, a modification catalyzed by the mitochondrial methyltransferase FAM173B[20][26]. Recent investigations have demonstrated that this lysine methylation is essential for optimal ATP synthase function and that disruption of the methyltransferase FAM173B results in failure of the c-subunit to incorporate properly into the ATP synthase complex[20].

In cells lacking functional FAM173B, c-subunits can still associate with other ATP synthase subunits and can form complex assemblies, but these complexes exhibit markedly reduced ATP-generating capacity[20]. Furthermore, cellular respiration is substantially impaired in the absence of proper c-subunit methylation, indicating that this post-translational modification has profound effects on mitochondrial bioenergetics[20]. The specific role of the Lys43 methylation appears to be promoting the proper folding of the c-subunit into its native α-helical hairpin conformation, as c-subunits lacking this modification are more prone to aggregation and misfolding[20][26].

Interestingly, under stress conditions characterized by elevated calcium and oxidative stress, unmethylated or unfolded c-subunits have been found to adopt alternative conformations, particularly β-sheet structures[6][26][29]. The c-subunit in β-sheet conformation is itself an amyloidogenic peptide capable of self-assembly into oligomers and fibrils, a process that is notably enhanced by elevated calcium concentrations[6][26][29]. These misfolded oligomers can form ion channels in artificial lipid bilayers, suggesting a potential role in stress-induced permeabilization of the inner mitochondrial membrane[6][28][29]. This apparent duality of function—normal ATP synthase participation versus stress-induced ion channel formation—represents an intriguing example of how the same polypeptide can adopt functionally distinct conformations depending on cellular conditions.

## Proton-Coupling Mechanism: Sequential Catalysis and Cooperative Function

The function of ATP5MC3-encoded subunit c within the larger ATP synthase must be understood not as the action of an isolated component but rather as cooperative participation in a coordinated rotary catalytic cycle. Early biochemical and genetic evidence suggested a model in which the essential Asp61 residue of subunit c works in concert with specific residues of the a-subunit, particularly the critical Arg210, to create a precisely positioned ion-binding site[7][10][17]. Suppressor mutation analysis provided early insights into this interaction; third-site suppressor mutations that restored function to otherwise defective ATP synthases were found to map to specific helices of both subunit c and subunit a, providing genetic evidence for direct physical interaction between these subunits[17].

More recent evidence suggests that the proton-coupling mechanism may be even more sophisticated than previously appreciated. Rather than a simple sequential model in which only one c-subunit participates in proton transfer at any given moment, contemporary molecular dynamics simulations and biochemical studies have revealed that multiple c-subunits contribute to the functional mechanism[9][14][49][52]. Specifically, multiple c-subunits positioned at different angles around the a-subunit interface appear to participate in a cooperative process, with the waiting times for proton uptake being effectively shared among several subunits[14][49][52].

This cooperative mechanism has been demonstrated through elegant experiments in which two different point mutations were introduced at different positions around the c-ring of reconstituted ATP synthase, and the activity of the enzyme was measured as a function of the distance between the two mutations[14][49][52]. The experiments revealed that ATP synthesis activity is highest when the two mutated c-subunits are positioned close to each other in the ring and decreases as the distance between them increases[14][49][52]. This distance-dependent effect provides unambiguous evidence that at least three neighboring c-subunits on the a/c interface cooperate during the c-ring rotation process[14][49][52].

## Genetic Defects and Human Neurological Disease

ATP5MC3 mutations have emerged as a significant cause of human genetic disease, particularly severe neurological conditions characterized by movement disorders. A pivotal discovery in this area was the identification of a novel missense variant (c.318C>G, resulting in p.Asn106Lys) in families with autosomal dominant dystonia and spastic paraplegia[13][21][37]. The variant was initially discovered in a large multigenerational family in which affected members showed an unusual clinical combination of either generalized dystonia with childhood onset or spastic paraplegia with adult onset[13][21][37].

The proband of the primary family presented with unilateral upper limb onset dystonia at age 2 years, which progressively generalized to involve the trunk and all limbs, resulting in loss of ambulation by adolescence[13][21][37]. The same proband subsequently showed benefit from bilateral pallidal deep brain stimulation, a surgical intervention typically effective for primary generalized dystonia[13][21][37]. Other family members, including the proband's father and grandfather, presented with progressive spastic paraplegia characterized by lower extremity weakness and spasticity, with onset after age 20 years[13][21][37]. The incomplete penetrance and variable expression of the phenotype within the same family, together with the unusual combination of dystonia and spastic paraplegia, represented a novel clinical entity[13][21][37].

Functional studies of patient-derived fibroblasts from affected family members demonstrated significantly reduced complex V activity compared to control cells, along with impaired ATP generation and decreased oxygen consumption, indicating compromised mitochondrial oxidative phosphorylation capacity[13][21][37]. Transgenic *Drosophila* models carrying the orthologous mutation also exhibited impaired mitochondrial function and significantly reduced mobility in standard geotaxis assays, providing independent animal model evidence for the pathogenicity of the variant[13][21][37].

The mechanistic basis for the p.Asn106Lys variant has been elucidated through structural and comparative analysis. The substitution occurs in a conserved loop region of subunit c that serves as the critical point of contact between the F₀ and F₁ domains of ATP synthase[13][21][37]. This loop region shows complete amino acid homology from humans through *Drosophila*, underscoring its functional importance[13][21][37]. Notably, a naturally occurring mutation at the equivalent position in the *Escherichia coli* ATP synthase ortholog (*atpE* gene)—the p.N102E substitution—has been previously shown to uncouple ATP hydrolysis from proton translocation while preserving proton translocation capacity[13][21][37]. The presence of the mutant allele is hypothesized to interfere with the normal F₁-F₀ interaction through a dominant-negative mechanism, rather than simple haploinsufficiency[13][21][37]. Supporting this model, overexpression of the mutant form in *Drosophila* resulted in statistically significant impairment of mobility, whereas overexpression of wildtype protein did not[13][21][37].

The pathological findings in these patients suggest that the reduced ATP synthase activity leads to insufficient ATP production and accumulation of reactive oxygen species, which in turn damages the nervous system, particularly neurons in the basal ganglia and spinal cord that have extremely high energy demands[13][21][37]. The differential presentation of dystonia versus spastic paraplegia within the same family may reflect variable penetrance, epigenetic factors, or sex-specific effects, though these mechanisms remain to be fully elucidated.

## Role in Oxidative Phosphorylation and Mitochondrial Biogenesis

The broader biological significance of ATP5MC3 lies in its essential role in oxidative phosphorylation, the aerobic process by which cells generate ATP from substrates in the presence of oxygen[1][15][18][39]. Approximately 90-95 percent of the ATP generated by eukaryotic cells under aerobic conditions is produced through oxidative phosphorylation in mitochondria, making this process absolutely critical for cellular function and survival[1][15][18][39]. The ATP5MC3-encoded subunit c is not merely an incidental component of this system but rather represents a critical catalytic element without which proton-coupled ATP synthesis cannot occur.

The efficiency of ATP synthesis is determined in part by the stoichiometry of protons to ATP, a relationship that is directly influenced by the number of c-subunits in the c-ring[51]. Each complete rotation of the c-ring, driven by proton translocation across the membrane, results in a defined number of ATP molecules being synthesized at the F₁ catalytic sites, determined by the matching of c-ring stoichiometry to the geometry of the F₁ catalytic sites[51]. This optimization represents an elegant solution to the bioenergetic requirements of different cell types and organisms; tissues with high ATP demand, such as cardiac muscle and brain, contain mitochondria packed with numerous cristae, dramatically increasing the surface area available for ATP synthesis[43][46].

The expression of ATP5MC3 is coordinately regulated with other genes encoding OXPHOS complex components through transcriptional programs that are activated in response to cellular energy demands[15][18]. The nuclear respiratory factors 1 and 2 (NRF1 and NRF2), which are transcriptional regulators that act on nuclear genes coding for OXPHOS subunits, play central roles in this regulation[18]. Additionally, mitochondrial transcription factor A (Tfam), which regulates transcription of genes encoded on the mitochondrial genome (including ATP6, encoding the critical a-subunit), is also transcriptionally regulated in response to cellular energy demands[18]. This integrated regulation ensures that the stoichiometric balance of nuclear-encoded and mitochondrially-encoded OXPHOS subunits is maintained, facilitating efficient assembly of functional ATP synthase complexes.

## Evolutionary Conservation and Origin of ATP Synthases

The ATP synthase complex represents one of the most ancient and conserved molecular machines known to biology, likely predating the divergence of Archaea and Bacteria and possibly even the Last Universal Common Ancestor (LUCA) of all life[45]. The subunit c proteins, encoded in humans by ATP5MC3 and its paralogs, represent remarkably conserved molecules with clear orthologs identifiable in virtually all organisms from bacteria through archaea, plants, and animals[45]. Comparative sequence analysis reveals that the core structural features—including the hairpin fold with two transmembrane helices and the critical Asp61 proton-binding residue—are conserved across these vastly different organisms.

Phylogenetic analyses of ATP synthase genes, combined with phylogenetic analysis of the subunit c and other ATP synthase components, suggest that the divergence of ATP synthase into the F-type lineage (found in bacteria, plant chloroplasts, and animal mitochondria) and the A/V-type lineage (found in archaea and vacuoles) occurred very early in cellular evolution, dating to more than four billion years ago[45]. The retention of nearly identical catalytic mechanisms across all organisms suggests intense purifying selection, indicating that the precise details of the proton-translocation mechanism have been optimized by evolution and cannot be substantially altered without loss of function[45].

In eukaryotes, the mitochondrial ATP synthase represents an endosymbiotic inheritance from the alpha-proteobacterial ancestor that was engulfed to form mitochondria[45]. The ATP5MC3 gene in humans represents a nuclear copy of what was originally a bacterial ATP synthase gene, a transfer event that occurred at the time of endosymbiosis and presumably involved intron insertion and acquisition of a mitochondrial targeting sequence[45]. The existence of three separate genes (ATP5MC1, ATP5MC2, and ATP5MC3) encoding the identical mature c-subunit protein represents a more recent duplication event within eukaryotic evolution, possibly reflecting the increased demand for ATP synthase in multicellular organisms or providing redundancy that buffers against deleterious mutations.

## Therapeutic Implications and Future Directions

The identification of ATP5MC3 mutations as causative of human neurological disease opens new avenues for therapeutic intervention and diagnosis of mitochondrial disorders. Patients with unexplained dystonia or spastic paraplegia of unknown etiology might benefit from genetic screening for ATP5MC3 variants, particularly when accompanied by evidence of mitochondrial dysfunction such as elevated lactate or reduced ATP production. Furthermore, understanding the molecular basis of disease-associated ATP5MC3 variants could inform therapeutic strategies aimed at enhancing ATP synthase function or compensating for impaired energy production in affected neurons.

The observation that ATP5MC3-encoded subunit c can undergo conformational transitions to form amyloidogenic β-sheet structures under stress conditions[6][26][29] also raises intriguing questions about potential links to neurodegenerative diseases characterized by protein aggregation. While α-synuclein and amyloid-β are well-established contributors to Parkinson's disease and Alzheimer's disease respectively, the possibility of c-subunit aggregation contributing to neurotoxicity in specific contexts warrants further investigation[6][26][29].

The development of cryo-electron microscopy techniques has enabled the determination of high-resolution structures of ATP synthase in multiple rotatory states, providing unprecedented detail regarding the dynamic conformational changes that occur during catalysis[19][22][44][57]. Continued structural investigations, potentially including time-resolved crystallography or cryo-EM of ATP synthase trapped in specific catalytic intermediates, may further illuminate the mechanism and suggest new targets for pharmaceutical intervention or bioengineering approaches aimed at enhancing ATP production in cells with compromised mitochondrial function.

## Conclusion

The ATP5MC3 gene encodes a small but functionally critical component of the mitochondrial ATP synthase complex, the molecular machine responsible for generating the vast majority of cellular ATP under aerobic conditions. The product of ATP5MC3, the membrane-spanning subunit c of the F₀ domain, represents a remarkable example of evolutionary conservation, with its hairpin structure and precise catalytic mechanism preserved across billions of years of evolution. Through a sophisticated proton-coupling mechanism involving the sequential protonation and deprotonation of Asp61 and cooperative interactions among multiple c-subunits in the c-ring, the ATP5MC3 gene product converts the electrochemical proton gradient into mechanical rotation that ultimately drives ATP synthesis.

The quaternary assembly of ATP5MC3-encoded subunits into the c-ring, integration into the larger ATP synthase complex, and oligomerization into higher-order supramolecular structures represent additional levels of biological organization that contribute to the efficiency and regulation of cellular energy production. Post-translational modification through lysine methylation by FAM173B represents an important regulatory mechanism ensuring proper folding and functional incorporation of the c-subunit. The identification of disease-associated mutations in ATP5MC3 has revealed the severe neurological consequences of compromised ATP synthase function, with implications for understanding dystonia, spastic paraplegia, and potentially other neurodegenerative conditions.

Future investigations should continue to employ contemporary structural biology approaches, functional genomics, and animal models to elucidate the remaining mechanistic questions regarding ATP synthase function and regulation. The therapeutic potential of enhancing ATP synthase activity or correcting the effects of pathogenic variants presents an important frontier in mitochondrial medicine, with potential benefits extending far beyond the rare genetic disorders directly caused by ATP5MC3 mutations to potentially including more common mitochondrial dysfunction-associated conditions.

## Citations

1. https://www.genecards.org/cgi-bin/carddisp.pl?gene=ATP5MC3
2. https://www.ncbi.nlm.nih.gov/gene/518
3. https://en.wikipedia.org/wiki/ATP_synthase_subunit_C
4. https://www.uniprot.org/uniprotkb/P48201/entry
5. https://www.uniprot.org/uniprotkb/Q3ZC75/entry
6. https://www.nature.com/articles/s41598-021-88157-z
7. https://pubmed.ncbi.nlm.nih.gov/10580496/
8. https://pmc.ncbi.nlm.nih.gov/articles/PMC10945847/
9. https://pubmed.ncbi.nlm.nih.gov/1331039/
10. https://www.embopress.org/doi/10.1038/sj.embor.7400646
11. https://pmc.ncbi.nlm.nih.gov/articles/PMC8840961/
12. https://elifesciences.org/articles/69096
13. https://pmc.ncbi.nlm.nih.gov/articles/PMC6523352/
14. https://pubmed.ncbi.nlm.nih.gov/8300584/
15. https://pmc.ncbi.nlm.nih.gov/articles/PMC3211033/
16. https://www.annualreviews.org/content/journals/10.1146/annurev-biophys-060724-110838
17. https://pubmed.ncbi.nlm.nih.gov/30530489/
18. https://pmc.ncbi.nlm.nih.gov/articles/PMC9244403/
19. https://pubmed.ncbi.nlm.nih.gov/31213526/
20. https://movementdisorders.onlinelibrary.wiley.com/doi/abs/10.1002/mds.28821
21. https://pmc.ncbi.nlm.nih.gov/articles/PMC3278611/
22. https://www.nature.com/articles/s41418-022-00972-7
23. https://pubmed.ncbi.nlm.nih.gov/33888826/
24. https://www.ncbi.nlm.nih.gov/gene?Db=gene&Cmd=DetailsSearch&Term=518
25. https://pubmed.ncbi.nlm.nih.gov/8218294/
26. https://pmc.ncbi.nlm.nih.gov/articles/PMC9447477/
27. https://www.pnas.org/doi/10.1073/pnas.96.14.7785
28. https://www.pnas.org/doi/10.1073/pnas.0708746105
29. https://earth.callutheran.edu/Academic_Programs/Departments/BioDev/omm/jsmolnew/atp_synthase/atp_synthase.html
30. https://jackwestin.com/resources/mcat-content/oxidative-phosphorylation/atp-synthase-chemiosmotic-coupling
31. https://pmc.ncbi.nlm.nih.gov/articles/PMC6056720/
32. https://pmc.ncbi.nlm.nih.gov/articles/PMC2442323/
33. https://pubmed.ncbi.nlm.nih.gov/18323778/
34. https://www.science.org/doi/10.1126/science.aaw9128
35. https://pmc.ncbi.nlm.nih.gov/articles/PMC10656485/
36. https://www.pnas.org/doi/10.1073/pnas.1816556116
37. https://pmc.ncbi.nlm.nih.gov/articles/PMC2222616/
38. https://pmc.ncbi.nlm.nih.gov/articles/PMC3651500/
39. https://pmc.ncbi.nlm.nih.gov/articles/PMC8809890/
40. https://pmc.ncbi.nlm.nih.gov/articles/PMC22139/
41. https://www.nature.com/articles/s41467-021-25029-0
42. https://febs.onlinelibrary.wiley.com/doi/10.1016/S0014-5793(03)01101-3
43. https://pmc.ncbi.nlm.nih.gov/articles/PMC7703542/