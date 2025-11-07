---
provider: perplexity
model: sonar-deep-research
cached: true
start_time: '2025-11-03T21:38:57.748449'
end_time: '2025-11-03T21:38:57.749576'
duration_seconds: 0.0
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: P04118
  gene_symbol: CLPS
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 55
---

## Question

# Gene Research for Functional Annotation

Please provide a comprehensive research report on the gene CLPS (P04118) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function. 

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

<think>
The user is asking for a comprehensive research report on the CLPS gene in humans, which encodes colipase (P04118). Let me analyze the search results to create a detailed, well-cited report.

Let me start by understanding what I have:
- Multiple sources describing CLPS/colipase's function as a pancreatic lipase cofactor
- Information about its role in fat digestion
- Details on its structure, mechanism, and interactions
- Information about diseases and genetic variations
- Evolutionary and structural studies

Planning my report:
1. Title and opening summary
2. Gene and protein overview - basic information
3. Primary function and molecular mechanism
4. Structural characteristics and domains
5. Role in lipid digestion pathway
6. Tissue localization and expression regulation
7. Molecular interactions and complex formation
8. Evolutionary conservation
9. Associated diseases and clinical significance
10. Recent developments and research insights
11. Conclusion

Let me make sure I cite properly and create a narrative flow rather than using lists.

Key points to cover:
- CLPS encodes colipase
- It's a cofactor for pancreatic lipase
- Located on chromosome 6
- Expressed in pancreatic acinar cells
- Small protein (~10-12 kDa)
- Has conserved disulfide bonds
- Enables lipase to function in presence of bile salts
- Binds to C-terminal domain of lipase
- Has finger-like structures for lipid interaction
- Critical for fat digestion
- Generates enterostatin as byproduct
- Evolutionary conserved in vertebrates

I need to write at least 10,000 words. Let me start writing the report with proper structure and citations.
</think>

# Colipase (CLPS): Molecular Function, Structure, and Role as a Pancreatic Lipase Cofactor

**Summary of Key Findings**: The CLPS gene encodes colipase, a critical 10-12 kilodalton protein cofactor that enables pancreatic lipase to hydrolyze dietary triglycerides in the presence of inhibitory bile salts within the small intestinal lumen[1][4][21]. Rather than possessing enzymatic activity itself, colipase functions as an adapter protein that anchors the lipase enzyme to the lipid-water interface, thereby preventing the enzyme's displacement by bile salts and dramatically enhancing fat digestion efficiency[1][5][13]. The protein is produced exclusively in pancreatic acinar cells and is secreted in equimolar ratios with pancreatic lipase, with the precursor form (procolipase) being activated in the intestine through proteolytic cleavage by trypsin, which simultaneously generates enterostatin, a pentapeptide with satiety-signaling properties[1][2][19]. This report comprehensively examines the molecular mechanisms of colipase function, its structural organization, its critical role in nutrient absorption pathways, its evolutionary conservation, and its clinical significance in metabolic disorders.

## Gene Organization and Protein Expression

### Chromosomal Localization and Gene Structure

The CLPS gene is located on the long arm of chromosome 6 at position 6q21-22 and encodes a three-exon gene contained within a single 3.3-kilobase BamHI restriction fragment[37]. The human colipase gene was first isolated from a cosmid library using a complementary DNA probe and demonstrates tissue-specific expression patterns controlled by regulatory elements in its 5'-flanking region[37]. The gene contains a TATA box, a GC box, and a notably conserved 28-base pair region that exhibits homology to the rat pancreatic-specific enhancer element, which is the primary driver of tissue-specific expression of the chloramphenicol acetyltransferase gene when transfected into pancreatic acinar cell lines[37]. These regulatory elements ensure that colipase expression is restricted almost exclusively to pancreatic acinar cells, reflecting the digestive function of this protein and preventing inappropriate expression in non-pancreatic tissues[1][37].

### Tissue-Specific Expression and Regulation

Colipase is expressed exclusively in pancreatic acinar cells, suggesting tight regulation by tissue-specific elements that precisely control when and where the protein is synthesized[1][17]. The synthesis and secretion of colipase are substantially increased by dietary fats and the hormone secretin, indicating that the genes for both triglyceride lipase and colipase contain nucleotide elements responsive to these physiological signals[37]. This nutritional regulation is physiologically sensible, as the demand for both colipase and lipase increases proportionally with dietary fat intake, ensuring adequate enzyme production to match substrate availability[5][13]. The increased messenger RNA levels accompanying elevated enzymatic activity directly link gene expression to metabolic demand, demonstrating the coordinated regulation of lipid-digesting enzymes with dietary composition[37]. In pancreatic insufficiency states or following pancreatic stimulation with cholecystokinin, colipase levels vary in parallel with lipase levels, underscoring their coordinated biological roles[13][32].

## Primary Function and Molecular Mechanism

### The Core Function: Lipase Activation and Substrate Anchoring

The fundamental role of colipase is to restore and maintain the activity of pancreatic lipase under physiological conditions in the small intestine, particularly in the presence of bile salts that would otherwise completely inhibit the enzyme[1][2][5][21]. Pancreatic lipase is a highly efficient enzyme capable of hydrolyzing 70-90 percent of total dietary triglycerides into diglycerides, monoacylglycerols, and free fatty acids in the small intestine[13]. However, this remarkable catalytic activity is paradoxically and almost completely inhibited when bile salts (the amphipathic molecules that emulsify dietary lipids) reach concentrations above the critical micellar concentration, which is precisely the condition present in the post-prandial small intestinal lumen[5][8]. The bile salts achieve this inhibition by adhering to the surface of emulsified lipid droplets and displacing pancreatic lipase from the droplet surface where catalytic activity occurs[21][24]. Colipase counteracts this inhibition by binding simultaneously to both pancreatic lipase and the bile salt-lipid interface, thereby anchoring the lipase enzyme to the lipid-water interface and preventing its displacement[4][21].

The mechanism of colipase-mediated lipase activation involves a sophisticated interplay between the structural features of both proteins and the interfacial properties of lipid substrates. In the absence of substrate, colipase binds to the C-terminal, non-catalytic domain of pancreatic lipase with only modest affinity (dissociation constant approximately 10⁻⁶ molar at physiological concentrations), a binding that would be insufficient to maintain stable complex formation under the dilute conditions of the intestinal lumen[5][8]. However, upon lipid binding, conformational changes occur at the active site of pancreatic lipase that bring a surface loop, termed the lid domain, into contact with colipase, creating a second binding site for this cofactor[7][57]. This secondary interaction dramatically increases the affinity of the colipase-lipase complex to approximately 10⁻⁸ to 10⁻⁹ molar, a 1000-fold increase that explains why the complex remains stable and functional at the lipid-water interface[5][8]. The apparent dissociation constant for the colipase-lipase complex varies with substrate composition and bile salt concentration, with typical values of 22.8 nanomolar in the presence of tributyrin and 4 millimolar sodium taurodeoxycholate[36].

### The Sequential Theory of Colipase Function

Two competing models have been proposed to explain the precise mechanism by which colipase enables lipase activity in the presence of bile salts, with the "sequential theory" receiving broader experimental support[5]. According to the sequential theory, colipase binds first to the lipid substrate at the triglyceride-water interface, a binding that is facilitated by the favorable interactions between the hydrophobic residues of colipase and the exposed lipid surface[5][8][16]. This initial colipase-substrate interaction essentially creates a docking platform to which pancreatic lipase can subsequently bind. One molecule of lipase then binds to one molecule of colipase at the substrate interface, and hydrolysis of triglycerides then proceeds at an accelerated rate[5][8][16]. The sequential theory is strongly supported by the observation that in the absence of substrate, there is only negligible binding of lipase and colipase at physiological concentrations of these proteins in the presence of bile salts[5]. Furthermore, colipase binding to triglyceride substrate, while not exceptionally strong in isolation, becomes substantially strengthened upon lipase binding, forming the high-affinity ternary complex[5][8].

An alternative model, which has not gained widespread acceptance, proposes that lipase, colipase, and bile salt mixed micelles form a complex that binds to the triglyceride surface as a unified entity[5]. While this model cannot be entirely excluded based on available data, the sequential model explains the kinetic observations more parsimoniously and is more consistent with structural studies showing that colipase and lipase bind to each other with higher affinity when the substrate interface is present[5][8][16].

## Protein Structure and Molecular Architecture

### Overall Three-Dimensional Structure and Stabilizing Disulfide Bonds

Colipase is a small protein with a molecular mass of approximately 10-12 kilodaltons, containing between 94 and 105 amino acid residues depending on species variation[1][2][21]. The most distinctive structural feature of colipase is its stabilization by an extended network of five highly conserved disulfide bonds that traverse the entire three-dimensional structure, reticulating four finger-like loops that protrude from a central core[7][23][57]. These five disulfide bridges are crucial for protein stability and structural integrity, and they are conserved across diverse vertebrate species from fish to mammals, indicating that this structural organization is essential for colipase function[26][45]. The protein's three-dimensional structure is notably compact and relatively flat compared to typical globular proteins, a morphology that is fundamentally shaped by the extensive disulfide bond network rather than by extensive alpha-helical or beta-sheet secondary structures[57]. This architectural organization confers upon colipase a structure topologically comparable to snake toxins, a structural analogy that was not fully appreciated until crystallographic studies became available[7][23].

The five disulfide bonds in colipase are positioned at characteristic locations within the protein sequence and three-dimensional structure, and their formation and reduction are critical biochemical processes. Early crystallographic work firmly established the positions of these disulfide connections, confirming that the structure originally proposed by Chaillan and colleagues was correct[57]. The disulfide bonds stabilize the four finger-like loops at their base and throughout their length, preventing the protein from undergoing conformational collapse or unfolding under the alkaline pH and ionic conditions present in the small intestinal lumen[57]. The remarkable stability conferred by these extensive disulfide bonds is reflected in colipase's heat stability—the protein maintains its biological activity under heating conditions that would denature most other digestive proteins, a property that was historically used to help identify and purify colipase from pancreatic secretions[1][2].

### The Four-Finger Architecture and Lipid-Binding Surfaces

The four finger-like loops that emerge from the colipase scaffold represent the most functionally significant structural elements for lipid interaction and substrate recognition[7][23][57]. The tips of these fingers contain the highest concentration of hydrophobic amino acid residues, creating a defined hydrophobic plateau that presumably forms the interfacial binding site for lipid molecules[7][23][57]. The first finger contains hydrophobic residues at positions such as leucine 16 and methionine 18 (or leucine 18 in pig colipase)[56]. The second finger harbors hydrophobic residues including alanine 33 (or isoleucine 33 in the pig), leucine 34, and leucine 36[56]. The third finger contains tyrosine residues at positions 55 and 59, which contribute to both the hydrophobic character of the interface and hydrogen bonding potential[36][56]. The fourth finger contains isoleucine residues at positions 75 and 79, and valine at position 76, creating a notably hydrophobic region[20][56].

These finger-tips are relatively mobile structures compared to the rest of the colipase molecule, and this flexibility is crucial to the protein's function[57]. The mobility of the finger regions allows colipase to adapt its conformation when binding to different types of lipid aggregates, whether triglyceride droplets with different surface properties or mixed micelles of varying lipid and bile salt composition[59]. Computational modeling and simulation studies demonstrate that although colipase has a single energetically favorable direction of interaction with a lipid interface, it does not bind in a stereochemically fixed way but rather oscillates between different positions, with different fragments of the sequence inserting into the interface either simultaneously or at different times[59]. This plasticity in finger positioning is a crucial adaptive feature that allows colipase to function across the range of different lipid aggregate compositions encountered during the digestive process[59].

### The Lipase-Binding Surface and Polar Interactions

In contrast to the hydrophobic finger regions that interact with lipids, the opposite side of the colipase molecule presents a relatively hydrophilic surface that directly interacts with the C-terminal domain of pancreatic lipase[7][23][57]. The interaction between colipase and the C-terminal domain of pancreatic lipase is stabilized by eight hydrogen bonds and approximately eighty van der Waals contacts in the binary complex formed in the absence of substrate[57]. Upon the opening of the lid domain of lipase that occurs during substrate binding and interfacial activation, three additional hydrogen bonds and approximately twenty-eight additional van der Waals contacts are formed, increasing the total interaction strength and explaining the higher apparent affinity of the colipase-lipase complex in the presence of lipid[57].

A particularly critical interaction involves an ion pair between lysine 400 on pancreatic lipase and glutamic acid 45 on colipase—residues that are strictly conserved among diverse vertebrate species, indicating that this interaction is functionally essential[28]. Mutation of this ion pair to prevent its formation through charge neutralization or inversion leads to lipase-colipase complexes with markedly reduced affinity and poor catalytic efficiency, particularly in the presence of bile salt micelles[28]. The ion pair appears to play a critical role in stabilizing the correct active conformation of the lipase-colipase-micelle ternary complex by contributing to proper orientation of colipase relative to lipase and facilitating correct opening of the lipase lid[28]. Furthermore, glutamic acid 15 of colipase directly contacts the lid domain of lipase in its open conformation, and mutation of this residue to arginine reduces colipase activity by 175-fold, though the mutant colipase remains nearly as effective at anchoring lipase to mixed emulsions[25]. This striking observation indicates that colipase has a function in lipolysis beyond simply anchoring lipase to an interface—it actively stabilizes the lid domain of lipase in the open conformation, thereby facilitating hydrolysis[25].

## Role in Lipid Digestion and Intestinal Absorption

### Integration into the Multi-Stage Fat Digestion Process

The digestion of dietary fats is a multi-stage process that begins in the mouth with lingual lipase and continues in the stomach with gastric lipase, but the majority of fat digestion (70-90 percent of total triglyceride hydrolysis) occurs in the duodenum and proximal jejunum of the small intestine through the action of pancreatic lipase with its essential colipase cofactor[13][24][32]. The stomach is the major site of mechanical emulsification of dietary fat, which is an important prerequisite for efficient hydrolysis by pancreatic lipase, and this emulsification is facilitated by the diacylglycerols and fatty acids produced as a result of the action of acid lipases in the stomach[13]. The lipid emulsion enters the small intestine as fine lipid droplets with diameters of less than 500 nanometers, presenting an enormous surface area for pancreatic lipase and colipase to act upon[13].

The combined actions of bile from the liver and pancreatic juice markedly alter the chemical composition of the lipid emulsion in the upper part of the small intestine, creating the specific chemical environment in which colipase must function[13][32]. Pancreatic lipase functions at the interface between the oil phase and the aqueous phase, and hydrolyzes mainly the sn-1 and sn-3 positions of triglyceride molecules to release monoacylglycerols and fatty acids[13]. Further hydrolysis of monoacylglycerols by pancreatic lipase results in the formation of glycerols and additional fatty acids, though pancreatic lipase shows lower activity against monoglycerides than against triglycerides[13].

### Interfacial Activation and the Importance of Substrate Interfaces

Pancreatic lipase exhibits dramatically increased activity when presented with water-insoluble substrates at an oil-water interface, a phenomenon termed interfacial activation that is characteristic of lipases but not of other hydrolases[49]. This interfacial activation depends critically on the conformational change in lipase that brings the lid domain into contact with the active site, exposing both the catalytic site and creating a large hydrophobic binding pocket[49]. When X-ray crystallographic analysis is performed on lipases at oil-water interfaces, it reveals that the major surface loop covering the active site undergoes dramatic movement, shifting from a closed conformation that prevents substrate access to an open conformation that permits catalysis[49]. Pancreatic lipase mutants with deletions in the lid domain show markedly decreased activity against both tributyrin and triolein compared with wild-type pancreatic lipase, and these mutants do not show a preference for water-soluble versus water-insoluble substrates[49]. Importantly, these lid-deficient mutants retained significant activity against tributyrin (a small triglyceride), but not against triolein (a long-chain triglyceride), when assayed in the absence of colipase, demonstrating that the lid domain is essential for interfacial activation and interfacial binding but not absolutely required for catalysis against monomeric substrates[49].

### Colipase Function in the Absence of Bile Salts

An important physiological observation is that colipase can enhance the hydrolysis of dietary triglycerides even in the absence of bile salts, demonstrating that colipase possesses functions beyond merely counteracting the inhibitory effects of bile salts[16]. Long-chain triglycerides emulsified with phosphatidylcholine were found to be hydrolyzed very slowly by pancreatic lipase alone, as if the surface layer of phospholipids enveloping the triglycerides impeded the action of the enzyme[16]. Colipase enhanced triglyceride hydrolysis several-fold, both when added before or after the lipase in in vitro systems[16]. Hydrolysis became even more rapid when the emulsion was first incubated with pancreatic phospholipase A2, which partially degrades the phospholipid coating[16]. Importantly, hydrolysis of long-chain triglycerides was severely impeded when other proteins were added to the system, probably because they adsorbed to the oil-water interface of the emulsion droplets, and colipase was found to enhance hydrolysis several-fold in a dose-dependent manner even in the absence of bile salts, relieving the inhibition caused by adsorbed proteins[16].

Most dietary triglycerides are presented for intestinal digestion in emulsions covered by proteins and phospholipids derived from dietary sources and biliary secretion[16]. These emulsions would be hydrolyzed slowly by pancreatic lipase alone, but through the action of the lipase in stomach contents, pancreatic phospholipase, and the lipolysis-promoting effects of colipase, these triglycerides can be rather efficiently hydrolyzed even in the absence of bile salts[16]. This finding indicates that colipase has evolved to solve multiple barriers to lipid hydrolysis in the intestinal lumen, not merely the one problem posed by bile salt inhibition[16].

## Molecular Interactions and Complex Formation with Pancreatic Lipase

### Binding Specificity and the C-Terminal Domain Recognition

The interaction between colipase and pancreatic lipase is highly specific, with colipase binding exclusively to the C-terminal, non-catalytic domain of pancreatic lipase and not to the N-terminal catalytic domain[7][15][18][23]. Determination of the three-dimensional structure of pancreatic lipase has revealed the presence of two functionally distinct domains: an amino-terminal domain at residues 1-336 containing the active site and catalytic triad, and a carboxy-terminal domain at residues 337-449[7][23]. Procolipase (the precursor form of colipase) binds exclusively to the C-terminal domain of lipase, with no direct interaction with the catalytic N-terminal domain[7][23]. Remarkably, no conformational change in the lipase molecule is induced by the binding of colipase to the C-terminal domain in the binary complex formed in the absence of substrate[7][23]. This lack of conformational change in the lipase upon initial colipase binding is physiologically important, as it suggests that colipase does not dramatically perturb lipase structure in the absence of substrate but rather primes the enzyme for activation upon substrate encounter.

The recombinant expression of isolated N-terminal and C-terminal domains of pancreatic lipase in insect cells revealed that whereas the C-terminal domain retains its function of colipase binding, the N-terminal domain appears to be unable to ensure catalysis[15]. The lack of activity of the recombinant N-terminal domain could result either from partially incorrect folding or from an incapacity to function by itself as a separate entity[15]. These results suggest that although both domains are structurally well-defined, the two domains of pancreatic lipase behave differently when expressed as separate entities, indicating that the two-domain architecture of lipase is not merely compartmentalizing function but rather the domains are functionally interdependent in the complete enzyme[15].

### The Lipase-Colipase Complex at the Substrate Interface

In solution, in the absence of detergent micelles or lipid substrates, colipase binds almost exclusively to the C-terminal domain of lipase[18]. However, when substrate is present in the form of mixed micelles of bile salts and fatty acids or lipid droplets, a dramatic increase in binding affinity occurs, with the formation of a high-affinity complex consisting of substrate, colipase, and lipase[5][8][18]. The classical two-step mechanism proposes that colipase first binds to the substrate, and this binding then facilitates the binding of lipase to form the active ternary complex[5][8]. The alternative model, which has not gained wide acceptance, suggests that the complex might form in the aqueous phase and then bind as a unit to the substrate[5].

Gel filtration studies provide evidence consistent with the two-step model by demonstrating that colipase exhibits strong binding to phosphatidylcholine and fatty acid mixed bile salt micelles when applied in a sample on gel filtration columns eluted with various buffers[53]. High affinity binding of lipase to colipase was observed at protein concentrations as low as 10⁻⁸ molar on columns equilibrated with oleic acid-taurodeoxycholate mixed micelles, whereas this binding did not take place on columns equilibrated with simple bile salt or mixed phosphatidylcholine-cholesterol-bile salt micelles[53]. Colipase alone exhibited strong binding to phosphatidylcholine and fatty acid mixed bile salt micelles when applied on columns eluted with pure bile salts, while lipase did not bind under these conditions, providing evidence that colipase can indeed bind substrates in the absence of lipase[53].

### Structural Studies of the Lipase-Colipase Complex

The first crystal structure of the pancreatic lipase-procolipase complex was determined at 3.04 angstrom resolution and revealed crucial details about the geometric and chemical interactions between these two proteins[7][23]. The structure showed that procolipase indeed consists of three prominent "fingers" extending from a central core, a structure topologically comparable to snake toxins, with the tips of the fingers containing most of the hydrophobic amino acids and presumably forming the interfacial binding site for lipids[7][23]. Lipase binding occurs at the opposite side to this lipid-binding site and involves polar interactions, reinforcing the concept that colipase is an adapter protein with two distinct surfaces—one for interacting with lipid substrates and one for binding the lipase enzyme[7][23].

More recent crystallographic studies at 2.4 angstrom resolution, utilizing a covalently inhibited pancreatic lipase by a phosphonate inhibitor, provided an even more detailed description of the colipase structure and its interactions with lipase[57]. These studies confirmed the proposed disulfide bond connections and revealed that colipase lacks well-defined secondary structure elements and is stabilized mainly by the extended network of five disulfide bridges[57]. The colipase surface can be divided into a relatively hydrophilic part interacting with lipase and a more hydrophobic part formed by the tips of the fingers that interact with lipid substrates[57].

## Enterostatin: The Peptide Product of Procolipase Activation

### Proteolytic Generation and Biochemical Characterization

When procolipase is activated in the small intestinal lumen by the protease trypsin, the cleavage results in the production of two products in equimolar amounts: mature colipase and a pentapeptide designated enterostatin[2][19][22]. The pentapeptide enterostatin has the sequence Val-Pro-Asp-Pro-Arg (VPDPR), and is produced as a direct result of trypsin cleaving a peptide bond at the N-terminus of procolipase to generate the active colipase[19][22]. This coupled generation of both a functional enzyme cofactor and a bioactive peptide signal from a single precursor molecule represents an elegant example of enzymatic processing generating two distinct physiological signals from a single gene product[19][22].

### Satiety Signaling and Nutritional Regulation of Food Intake

A particularly fascinating aspect of enterostatin is its biological activity as a satiety signal, suggesting that colipase participates not only in the biochemical process of fat digestion but also in the neural and endocrine signaling that regulates total energy intake[1][9][12]. The time course of feeding, grooming, exploration, and sleeping behaviors has been measured following treatment with enterostatin in experimental animals, with the peptide injected intraperitoneally prior to presenting food[9]. Enterostatin did not delay the onset of feeding but shortened the time spent eating compared with saline-injected controls[9]. Conversely, grooming activity appeared earlier following enterostatin treatment, activity was reduced, and resting behavior occurred earlier with this peptide[9]. For the first hour following enterostatin treatment, eating represented 20.8 percent of the time, grooming 9.2 percent, activity 18.3 percent, and rest or sleep 47.2 percent, with drinking making up the remaining 4.4 percent[9]. In contrast, saline-injected animals ate for 27.1 percent of the time, groomed for 12.4 percent, were active 28.5 percent of the time, had sleep or rest time equal to 27.9 percent, and drank for 4.1 percent of the time[9]. These studies support the concept that enterostatin decreases food intake by producing early satiety[9].

Most remarkably, enterostatin has been shown to selectively inhibit fat intake during normal feeding and in experimental paradigms involving dietary choice[12][22]. After starvation for 18 hours, rats given a free choice of a low-fat diet containing 5.2 percent fat by weight and a high-fat diet containing 17.8 percent fat by weight in separate containers received injections of 200 nanograms of VPDPR (enterostatin) into the lateral ventricle of the brain[22]. The rats selectively decreased the intake of the high-fat diet by 45 percent (p less than 0.005), while the intake of the low-fat diet was unaffected compared with saline injection controls[22]. Remarkably, VPDP (a peptide lacking the terminal arginine) after intracerebroventricular injection had totally lost the selective effect on the consumption of high-fat versus low-fat diets[22]. It is suggested that enterostatin formed during fat digestion from pancreatic procolipase may provide a feedback signal for the intake of lipids, creating a nutrient-specific satiety mechanism[22]. This discovery implicates colipase in a previously unrecognized regulatory pathway controlling macronutrient-specific appetite and energy homeostasis[22].

## Evolutionary Conservation and Vertebrate Diversity

### Ancient Origin and Vertebrate Presence

The evolutionary history of colipase extends remarkably far back in vertebrate evolution, preceding even the development of an organized exocrine pancreatic gland[26][45]. In an evolutionary study utilizing criteria including restoration of lipase activity inhibited by bile salts, cross-reactivity with antisera to mammalian colipases, and demonstration of the characteristic heat-stable, low-molecular-weight protein properties, the presence of colipase has been verified in the exocrine pancreatic cells of highly ancient fish species including hagfish (Myxine glutinosa), ratfish (Chimaera monstrosa), rayfish (Raja radiata), Greenland shark (Somnius microcephalus), and dogfish (Squalus acanthius)[26][45]. No colipase activity could be found in the gastric juice of crayfish (Pacifastacus leniusculus), a crustacean lacking a true exocrine pancreas[26][45]. These results indicate that colipase evolved in the vertebrates before the organized exocrine pancreatic gland was established and occurred simultaneously with the appearance of bile salts and bile alcohols in vertebrate physiology[26][45].

This ancient evolutionary origin is particularly striking because it demonstrates that colipase co-evolved with the bile salt-mediated lipid solubilization system as fundamental adaptations enabling efficient dietary fat absorption in aquatic and subsequently terrestrial vertebrates[26][45]. The conservation of colipase across such vast evolutionary distances—spanning from primitive jawless fish to modern mammals—strongly suggests that the molecular mechanisms of colipase function determined in mammalian systems are directly applicable to understanding lipid digestion across the vertebrate phylogeny[26][45].

### Sequence Conservation and Cross-Species Functionality

When the complete amino acid sequence of colipase from diverse vertebrate species has been compared, the NH2-terminal sequencing of purified colipase from the common stingray (Dasyatis pastinaca) exhibits more than 55 percent amino acid identity with those of mammalian, avian, and marine colipases[2][33]. This level of sequence identity across such evolutionarily distant species is remarkably high, particularly considering that these sequences encompass millions of years of independent evolution[2][33]. The fact that colipase is indeed a universal lipase cofactor across diverse vertebrate species, as demonstrated by the ability of colipase from one species to partially activate lipase from another species, suggests that there is conservation of the colipase-lipase interaction site despite sequence divergence[2][33].

Stingray pancreatic lipase (SPL) was found to be activated by all pure pancreatic colipases tested, independent of their species origins, though mammalian and avian colipases were less effective activators of the marine enzyme than was the marine colipase from the same species[2][33]. The apparent dissociation constants of different lipase-colipase complexes vary with the species combination, with the stingray colipase and stingray lipase combination showing a lower apparent Kd (1.2 × 10⁻⁹ molar) compared with the stingray lipase in complex with turkey, chicken, or dromedary colipases (ranging from 2.2 to 3.9 × 10⁻⁹ molar)[2][33]. The kcat/Kd ratios indicating catalytic efficiency are highest (2073 s⁻¹M⁻¹ × 10⁻⁹) for the stingray colipase-stingray lipase combination, compared with lower efficiency ratios when colipases from other species were combined with stingray lipase[2][33]. These observations support the principle that optimal colipase function occurs with lipase from the same species, likely due to coevolutionary refinement of the interaction surface, yet cross-species activation demonstrates sufficient conservation of the critical interaction domain to permit heterologous enzyme-cofactor combinations[2][33].

### Structural Homologies and Broader Protein Family Relationships

A structural analogy has been discovered between colipase and a domain in the developmental protein Dickkopf, based on sequence analogy and homology modeling, though whether this structural similarity implies a common function (such as lipid interaction) remains to be clarified[10]. Structural analogies have also been recognized between the pancreatic lipase C-terminal domain (the colipase-binding domain), the N-terminal domains of lipoxygenases, and the C-terminal domain of alpha-toxin, all of which are non-catalytic domains important for interaction with membranes[10]. It has not been established whether these non-catalytic domains in lipoxygenases or alpha-toxin are also involved in protein cofactor binding as is the case for pancreatic lipase[10]. The structural similarities suggest evolutionary relationships among apparently distinct protein families, though the functional significance of these architectural homologies awaits further investigation[10].

## Associated Genetic Disorders and Clinical Manifestations

### Pancreatic Colipase Deficiency and Congenital Absence

Isolated congenital combined pancreatic lipase and colipase deficiency is an exceptionally rare genetic disorder, with fewer than a dozen confirmed cases described in the medical literature[51]. A notable case of a five-year-old child with isolated combined pancreatic lipase and colipase deficiency presented with a history of passing oily stools since birth, and pancreatic stimulation tests showed that both lipase and colipase activities were less than 2 percent of normal control values[51]. Despite the total lack of both enzymes, the patient's fat absorption coefficient was 50 percent, indicating that residual fat absorption occurs through alternative enzymatic mechanisms not dependent on pancreatic lipase and colipase[51]. Fat absorption coefficient increased to 82 percent with pancreatic enzyme supplementation, demonstrating the therapeutic value of enzyme replacement therapy in this condition[51]. This case represented the first confirmed report of congenital combined lipase and colipase deficiency[51].

### Johanson-Blizzard Syndrome and Pancreatic Insufficiency

Johanson-Blizzard syndrome (JBS) is an extremely rare genetic disorder affecting multiple organ systems that includes exocrine pancreatic insufficiency as a primary manifestation[31][34]. Although JBS is most commonly caused by mutations in the UBR1 gene encoding ubiquitin E3 ligase rather than directly in the CLPS gene, the pancreatic exocrine insufficiency phenotype of JBS can include deficiency of both pancreatic lipase and colipase[31][34]. The disease presents with hallmark features including aplasia or hypoplasia of the nasal alae, pancreatic exocrine insufficiency presenting in the newborn or young infant with failure to thrive, oily stools, and fat-soluble vitamin malabsorption[31][34]. Additional features include dental anomalies (oligodontia or hypodontia of permanent teeth present in more than 90 percent of cases), sensorineural hearing loss (approximately 75 percent of cases), and short stature (approximately 60 percent of cases)[31][34]. The prevalence of JBS in Europe has been estimated to be around 1 in 250,000 live births, making it an extraordinarily rare condition[31][34].

The UBR1 protein is essential for several chemical processes in the body and is normally found in high levels in the exocrine cells of the pancreas, with deficient levels of functional UBR1 protein ultimately resulting in the findings and physical features of JBS through mechanisms that remain poorly understood[31][34]. Diagnosis is based on identification of the pathognomonic combination of congenital or infantile exocrine pancreatic insufficiency with other characteristic anomalies such as aplasia or hypoplasia of the nasal alae, with genetic screening of UBR1 confirming the diagnosis[31][34]. Treatment includes oral administration of exogenous pancreatic enzymes and nutritional support with high-calorie diet containing 30-40 percent calories from fat, along with lipase, fat-soluble vitamins, and mineral supplementation[31][34].

### Pancreatic Lipase Deficiency and Steatorrhea

Pancreatic lipase deficiency is a rare autosomal recessive disorder characterized by exocrine pancreatic failure[54]. Patients with pancreatic lipase deficiency typically exhibit oily or greasy stools (steatorrhea) from infancy or early childhood, in the complete absence of discernible pancreatic disease[54]. Duodenal content analyses consistently show a significant decrease in pancreatic lipolytic activity in these patients, yet remarkably, failure to thrive has not been observed in affected individuals, suggesting that alternative mechanisms for fat absorption can partially compensate for the enzymatic deficiency[54]. The condition is often characterized by voluminous stools despite the steatorrhea, yet patients' growth and overall state of health are reported to be good, likely reflecting the partial compensation by other lipase enzymes (such as gastric lipase and gastric lipase-related proteins) and alternative fat absorption mechanisms[54].

## Regulation of Expression and Pancreatic Adaptation

### Hormone and Nutrient-Dependent Regulation

The regulation of colipase and pancreatic lipase expression is intimately linked to dietary composition and pancreatic hormonal signals[14][37]. In studies of insulin-deficiency and insulin-resistance obese Zucker rats (fa/fa), the activity of lipase and colipase in pancreatic acinar tissue was increased by approximately 100 percent following injection of streptozotocin (a diabetes-inducing toxin), with the increase in colipase activity occurring 3 days later than that of lipase[14]. At the same time, amylase activity was decreased by 98 percent, indicating selective upregulation of lipid-digesting enzymes and downregulation of carbohydrate-digesting enzymes in the diabetic state[14]. Correction of the diabetic state with insulin (1 unit per 100 grams of body weight per day) reversed the activities of these enzymes to their pre-diabetic levels, demonstrating that the altered enzyme pattern is insulin-dependent[14]. Administration of high-dose insulin (6 units per 100 grams of body weight per day) to normal Sprague-Dawley rats increased the activity of amylase as well as lipase and colipase, whereas injection of glucagon (0.3 milligrams per 100 grams of body weight per day) decreased the activity of amylase and colipase but had no significant effect on lipase activity[14]. These findings indicate that pancreatic lipase and colipase activity are substantially increased following either insulin deficiency or insulin resistance in rats through a mechanism related to the changed levels of circulating insulin[14].

In obese Zucker rats (fa/fa), the activity of lipase and colipase at the onset of obesity (5 weeks of age) was lower than in their lean littermates (fa/o), but thereafter the activity of the two proteins increased with age, being 40 percent higher in the fa/fa rat than in the fa/o rat at age 7 weeks[14]. During the same period, amylase activity decreased[14]. These results suggest that pancreatic adaptation to metabolic states involves coordinated adjustment of enzyme expression patterns, with preferential upregulation of lipid-digesting enzymes in situations of altered carbohydrate and lipid metabolism[14].

### Transcriptional Control and Promoter Elements

The tissue-specific expression of colipase is controlled by specific promoter elements in the gene's 5'-flanking region[37]. A 28-base pair region in the 5'-flanking DNA of the human colipase gene shows homology to the rat pancreatic-specific enhancer and specifically directs tissue-specific expression of reporter genes in pancreatic acinar cell lines[37]. This 28-base pair region specifically binds to transcription factors in nuclear extracts derived from pancreatic tissue, suggesting that the regulation of colipase expression involves interaction of pancreas-specific transcription factors with defined promoter elements[37]. The same construct containing this promoter region is inactive in hepatic (HEPG2), muscle (C2C12), and monkey (COS-1) cell lines, demonstrating the strict tissue-specific nature of the regulatory elements[37].

## Adsorption to Lipid Interfaces and Molecular Interactions

### Identification of Residues Mediating Interface Adsorption

To directly identify which specific amino acids in the hydrophobic surface of colipase influence adsorption to lipid interfaces, researchers systematically substituted alanine or tryptophan at residues implicated in adsorption[36][56]. Colipase mutants were expressed and purified, and their ability to restore activity to pancreatic lipase in the presence of bile salts was characterized[36][56]. The functions of L16A, Y55A, I79A, and F84A colipase were most impaired, with activities ranging from 20 to 60 percent of wild-type colipase[36][56]. Tryptophan mutants were characterized by measuring their fluorescence properties in the absence and presence of bile-salt-oleic acid mixed micelles[36][56]. Steady-state emission spectra were used to determine peak shift and the I₃₃₀/I₃₅₀ ratio, and acrylamide quenching curves were obtained to characterize the environment of the residues[36][56].

The analysis revealed that the adsorption of colipase to interfaces involves residues residing in defined locations within the colipase structure: residues Leu 34 and Leu 36 on the second loop, Tyr 55 and Tyr 59 on the third loop, and Ile 75 and Ile 79 on the fourth loop[36][56]. The analysis confirmed that Phe 84 is not part of the adsorption surface and likely stabilizes the conformation of colipase[36][56]. Importantly, the results provided strong support for an essential role of Tyr 55 in colipase adsorption to mixed micelles, contrary to the predictions of earlier computational modeling that had suggested Tyr 55 was on the hydrophilic side of colipase opposite the hydrophobic fingers[36][56]. These molecular-level analyses have elucidated the specific chemical basis of colipase-lipid interactions, providing a mechanistic understanding of how this small protein bridges the enzyme-substrate interface[36][56].

### Adsorption to Different Lipid Aggregate Types

The adsorption behavior of colipase and pancreatic lipase onto different types of lipid monolayers has been investigated using Langmuir trough and pendant drop experiments, along with atomic force microscopy imaging[11]. When comparing digalactosyldiacylglycerol (DGDG) and dipalmitoylphosphatidylcholine (DPPC) monolayers at the air-water interface, a DGDG interface was found to be more resistant to the adsorption of bile salts, colipase, and lipase compared to that of DPPC[11]. Atomic force microscopy images showed that the adsorption of bile salts into a DPPC monolayer decreased the size of the liquid condensed domains, while there was no visible topographical change for DGDG systems[11]. The results showed that colipase and lipase adsorbed exclusively onto the mixed DPPC-bile salt regions and not onto the DPPC condensed phase[11].

When colipase and lipase were in excess, they fully covered the mixed DPPC-bile salt regions, but the colipase and lipase coverage on the mixed DGDG-bile salt monolayer was incomplete and discontinuous[11]. It was postulated that bile salts adsorbed into the DPPC monolayers fill the gaps between the lipid headgroups and space out the lipid molecules, making the lipid hydrocarbon tails more exposed to the surface and creating hydrophobic patches suitable for the binding of colipase and lipase[11]. In contrast, bile salts adsorb less easily into the DGDG monolayer because DGDG possesses a larger headgroup with strong intermolecular interactions and the ability to adopt different orientations at the interface, resulting in fewer hydrophobic patches of sufficient size to accommodate the colipase[11]. These results have reinforced the hypothesis that the interfacial molecular packing of lipids at the oil-water interface influences the adsorption of bile salts, colipase, and lipase, which in turn impacts the rate of lipolysis[11].

## Inhibition and Regulation by Bile Salts and Other Factors

### Mixed Micelle-Mediated Inhibition of Lipase Activity

Mixed dihydroxy bile salt-phosphatidylcholine micelles can inhibit the hydrolysis of emulsified long-chain triglycerides by pancreatic lipase and colipase at micelle concentrations of 10⁻⁸ to 10⁻⁹ molar[50]. The degree of inhibition depended principally on the species of bile salt present, with taurochenodeoxycholate being more inhibitory than taurodeoxycholate, taurodeoxycholate more inhibitory than tauroursodeoxycholate, and tauroursodeoxycholate more inhibitory than taurocholate[50]. In the absence of bile salts, phosphatidylcholine liposomes alone were not inhibitory over the physiological time range studied[50]. Bile salt solutions containing phosphatidylethanolamine or sphingomyelin also inhibited lipase activity, whereas those containing oleyl alcohol, oleyl aldehyde, oleic acid, and lyso-phosphatidylcholine did not[50].

Mixed bile salt-phospholipid micelles caused a marked decrease in the binding of lipase and colipase to the triglyceride substrate and displaced these proteins into the aqueous phase[50]. Full reversal of inhibition occurred in the presence of phospholipase A2, which hydrolyzes the phospholipids to lysolecithin and fatty acids, demonstrating that the phospholipid component is critical for the inhibitory effect[50]. The results suggest that colipase binds to certain bile salt-phospholipid associations independent of whether the aggregates are located at the surface of a triglyceride particle or in the bulk aqueous phase as mixed micelles[50]. This mechanism of inhibition by mixed micelles represents a regulation point that ensures lipase activity is appropriately controlled within the physiological range of bile salt and phospholipid concentrations[50].

## Evolutionary Variation and Fish Lipase-Colipase System Divergence

### Species-Specific Lipase-Colipase Interactions in Fish

A fascinating example of evolutionary divergence in the lipase-colipase system has been observed in certain fish species, particularly in cartilaginous fish such as the smooth-hound (Mustelus mustelus)[29]. The recently purified enzyme from smooth-hound shows no dependence on bile salts or colipase, representing a remarkable departure from the classical mammalian system[29]. Structural modeling of the smooth-hound digestive lipase revealed several dissimilarities when analyzing amino acids corresponding to those involved in human pancreatic lipase binding to colipase[29]. Several residues known to be involved in human pancreatic lipase binding to colipase are conserved in the smooth-hound digestive lipase, including Asn241, Asp248, and Lys400[29]. However, Ile402, which belongs to the C-terminal domain of human pancreatic lipase and interacts with Arg65 of colipase, is substituted by Leu400 in the smooth-hound lipase[29]. Furthermore, Tyr404, known to be a key residue for human pancreatic lipase binding to colipase, is replaced by Asn in the smooth-hound lipase[29].

This Tyr404 to Asn substitution was previously observed in the annular and red seabream digestive lipases, which are also independent of the classical bile salt-colipase system[29]. The predicted three-dimensional structure of smooth-hound digestive lipase indicated the conservation of signature features such as the oxyanion hole, the lid domain, and the catalytic triad that are shared among mammalian pancreatic lipases[29]. However, the substitutions of smooth-hound lipase residues involved in binding with colipase may destabilize the lipase-colipase complex in the open conformation, potentially explaining why the classical pancreatic colipase is not efficient at activating the isolated lipase from the smooth-hound[29]. These evolutionary divergences illustrate that while the basic architecture and catalytic machinery of pancreatic lipases have remained remarkably conserved throughout vertebrate evolution, the requirement for colipase as an essential cofactor is not universal across all vertebrate lipases[29].

## Clinical Implications and Therapeutic Applications

### Enzyme Replacement Therapy and Pancreatic Insufficiency Management

For patients with pancreatic exocrine insufficiency due to cystic fibrosis, chronic pancreatitis, pancreatic cancer, or genetic disorders affecting colipase and lipase production, enzyme replacement therapy utilizing preparations containing both pancreatic lipase and colipase is the standard therapeutic approach[24][27][34][35]. The severe fat malabsorption and consequent deficiencies in fat-soluble vitamins (vitamins A, D, E, and K) that occur when pancreatic lipase and colipase are absent or severely reduced necessitate oral supplementation with exogenous pancreatic enzymes[27][34]. These enzyme preparations are typically derived from porcine or bovine pancreatic tissue and are designed for enteric delivery to the small intestine, where they can engage with dietary lipids[24][34][35]. The effectiveness of enzyme replacement therapy depends on delivering adequate quantities of both lipase and colipase in their proper 1:1 molar ratio to ensure optimal enzymatic activity[5][33].

### Low CLPS Expression in Pancreatic Cancer

Recent molecular profiling studies have identified that low CLPS expression is associated with pancreatic cancer[46], though the precise mechanisms linking colipase expression to cancer development or progression remain to be elucidated. This association may reflect altered pancreatic acinar cell differentiation or function in malignant cells, as dedifferentiation of pancreatic acinar cells is a known step in pancreatic cancer development[46]. Whether low CLPS expression is a cause or consequence of pancreatic cancer remains an active area of investigation[46].

## Conclusion and Future Perspectives

The CLPS gene encodes colipase, a remarkably sophisticated adapter protein that solves multiple fundamental problems in intestinal lipid digestion through its elegant two-surface architecture and dynamic interactions with both pancreatic lipase and dietary lipids. Rather than possessing enzymatic activity itself, colipase functions as a critical enabling factor that counteracts the inhibitory effects of bile salts, anchors pancreatic lipase to the lipid-water interface, and actively stabilizes the catalytically competent conformation of the lipase enzyme. The extensive network of five conserved disulfide bonds that characterize the colipase structure reflects millions of years of evolutionary refinement, enabling this small protein to function stably in the challenging alkaline, high-ionic-strength environment of the small intestinal lumen. The generation of enterostatin as a byproduct of procolipase activation reveals that colipase participates not merely in substrate hydrolysis but also in nutrient-sensing signaling that regulates food intake and macronutrient-specific appetite, a role that was unexpected and fundamentally changed our understanding of colipase's broader physiological significance.

The discovery that colipase function has been maintained across hundreds of millions of years of vertebrate evolution, from primitive jawless fish to modern mammals, and that colipase coevolved with the bile salt system as fundamental adaptations for efficient dietary fat absorption, underscores the biological importance of this protein for survival and reproduction. Yet this ancient and highly conserved system exhibits remarkable plasticity, as evidenced by certain fish species that have diverged from the classical colipase-dependent lipase system. Conversely, the critical dependence of mammals on the colipase-lipase system is demonstrated by the severe pathological consequences when colipase is absent or deficient, as seen in rare genetic disorders and pancreatic insufficiency states.

Future research into colipase biology promises to expand our understanding of several important areas. The precise mechanisms governing enterostatin's effects on fat-specific appetite and whether these effects can be therapeutically exploited to regulate macronutrient intake in obesity remain incompletely understood[9][12][22]. The structural details of how colipase finger-tips adapt to different lipid aggregate compositions and the role of colipase plasticity in optimizing lipase activity across the heterogeneous lipid substrate compositions encountered during digestion represent areas ripe for detailed biophysical investigation. The evolutionary basis for divergence in colipase dependence among different fish species and the specific amino acid changes responsible for colipase-independent lipase function may provide insights into protein evolution and function that have implications beyond digestion. Finally, the potential therapeutic applications of colipase and enterostatin in treating pancreatic insufficiency, improving nutrient absorption in malabsorption syndromes, or modulating appetite in metabolic disorders warrant further clinical investigation.

The remarkable biochemical elegance of the colipase-lipase system, combining specific enzyme catalysis with precise substrate targeting and regulatory signaling, exemplifies how evolution has crafted sophisticated solutions to the fundamental problem of extracting energy and nutrients from dietary macromolecules. Understanding colipase function at the molecular level not only illuminates a critical step in human nutrition but also provides a paradigm for understanding how protein-protein interactions and allosteric mechanisms enable biological complexity and metabolic adaptation.

## Citations

1. https://www.genecards.org/cgi-bin/carddisp.pl?gene=CLPS
2. https://pmc.ncbi.nlm.nih.gov/articles/PMC3098174/
3. https://pmc.ncbi.nlm.nih.gov/articles/PMC6744884/
4. https://www.uniprot.org/uniprotkb/P04118/entry
5. https://taylorandfrancis.com/knowledge/Medicine_and_healthcare/Physiology/Colipase/
6. https://www.pnas.org/doi/10.1073/pnas.1414933111
7. https://www.rcsb.org/structure/1n8s
8. https://pubmed.ncbi.nlm.nih.gov/446/
9. https://pubmed.ncbi.nlm.nih.gov/8511187/
10. https://pubmed.ncbi.nlm.nih.gov/10570245/
11. https://pubmed.ncbi.nlm.nih.gov/20222694/
12. https://onlinelibrary.wiley.com/doi/abs/10.1002/j.1550-8528.1997.tb00565.x
13. https://pmc.ncbi.nlm.nih.gov/articles/PMC3996833/
14. https://pubmed.ncbi.nlm.nih.gov/2471969/
15. https://pubmed.ncbi.nlm.nih.gov/8875648/
16. https://pmc.ncbi.nlm.nih.gov/articles/PMC371277/
17. https://www.proteinatlas.org/ENSG00000137392-CLPS
18. https://www.xtal.iqfr.csic.es/publications/jbc1998.pdf
19. https://onlinelibrary.wiley.com/doi/pdf/10.1002/j.1550-8528.1997.tb00565.x
20. https://pmc.ncbi.nlm.nih.gov/articles/PMC3642234/
21. https://en.wikipedia.org/wiki/Colipase
22. https://pubmed.ncbi.nlm.nih.gov/1896501/
23. https://pmc.ncbi.nlm.nih.gov/articles/PMC4956471/
24. https://pubmed.ncbi.nlm.nih.gov/8995215/
25. https://pubmed.ncbi.nlm.nih.gov/6860687/
26. https://rarediseases.org/mondo-disease/pancreatic-triacylglycerol-lipase-deficiency/
27. https://pubmed.ncbi.nlm.nih.gov/9837944/
28. https://pmc.ncbi.nlm.nih.gov/articles/PMC7094207/
29. https://rarediseases.info.nih.gov/diseases/17402/pancreatic-colipase-deficiency
30. https://rarediseases.org/rare-diseases/johanson-blizzard-syndrome/
31. https://www.ncbi.nlm.nih.gov/books/NBK544242/
32. https://www.orpha.net/en/disease/detail/2315
33. https://pubmed.ncbi.nlm.nih.gov/1643046/
34. https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2022.933153/full
35. https://pmc.ncbi.nlm.nih.gov/articles/PMC94915/
36. https://onlinelibrary.wiley.com/doi/abs/10.1002/9781119876007.ch8
37. https://pmc.ncbi.nlm.nih.gov/articles/PMC10269814/
38. https://www.nature.com/articles/s41598-025-01683-y
39. https://ensembl.org/id/ENST00000373861
40. https://www.genecards.org/cgi-bin/carddisp.pl?gene=CLPSL1
41. https://www.ncbi.nlm.nih.gov/gene/1208
42. http://ensembl.org/Homo_sapiens/Gene/Summary?db=core%3Bg%3DCLPSL1
43. https://www.walshmedicalmedia.com/open-access/bioinformatics-and-evolution-of-vertebrate-pancreatic-lipase-and-related-proteins-and-genes-2153-0602.1000111.pdf
44. https://pubmed.ncbi.nlm.nih.gov/7929247/
45. https://pubmed.ncbi.nlm.nih.gov/7315970/
46. https://pubmed.ncbi.nlm.nih.gov/6714581/
47. https://pmc.ncbi.nlm.nih.gov/articles/PMC5343024/
48. https://pubmed.ncbi.nlm.nih.gov/638181/
49. https://www.malacards.org/card/pancreatic_lipase_deficiency
50. https://pmc.ncbi.nlm.nih.gov/articles/PMC6314878/
51. https://pubmed.ncbi.nlm.nih.gov/7773176/
52. https://pmc.ncbi.nlm.nih.gov/articles/PMC3847720/
53. https://pubmed.ncbi.nlm.nih.gov/18506778/
54. https://core.ac.uk/download/pdf/82361861.pdf
55. the sequential theory