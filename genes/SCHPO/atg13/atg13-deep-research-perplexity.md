---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-01-30T19:37:19.190898'
end_time: '2026-01-30T19:39:26.602756'
duration_seconds: 127.41
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: SCHPO
  gene_id: atg13
  gene_symbol: atg13
  uniprot_accession: O36019
  protein_description: 'RecName: Full=Autophagy protein 13; AltName: Full=Meiotically
    up-regulated gene 78 protein;'
  gene_info: Name=atg13; Synonyms=mug78; ORFNames=SPAC4F10.07c;
  organism_full: Schizosaccharomyces pombe (strain 972 / ATCC 24843) (Fission yeast).
  protein_family: Belongs to the ATG13 family. Fungi subfamily.
  protein_domains: ATG13. (IPR040182); Atg13_N. (IPR018731); HORMA_dom_sf. (IPR036570);
    ATG13 (PF10033)
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 48
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** O36019
- **Protein Description:** RecName: Full=Autophagy protein 13; AltName: Full=Meiotically up-regulated gene 78 protein;
- **Gene Information:** Name=atg13; Synonyms=mug78; ORFNames=SPAC4F10.07c;
- **Organism (full):** Schizosaccharomyces pombe (strain 972 / ATCC 24843) (Fission yeast).
- **Protein Family:** Belongs to the ATG13 family. Fungi subfamily.
- **Key Domains:** ATG13. (IPR040182); Atg13_N. (IPR018731); HORMA_dom_sf. (IPR036570); ATG13 (PF10033)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "atg13" matches the protein description above**
2. **Verify the organism is correct:** Schizosaccharomyces pombe (strain 972 / ATCC 24843) (Fission yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'atg13' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **atg13** (gene ID: atg13, UniProt: O36019) in SCHPO.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# ATG13: Molecular Architecture and Functional Role as a Scaffolding Hub in Autophagy Initiation

Autophagy protein 13 (Atg13) is an essential regulatory component of the autophagy initiation machinery that functions as a molecular hub coordinating the assembly and activation of the Atg1 protein kinase complex at the autophagosome-formation site in eukaryotic cells. In the fission yeast Schizosaccharomyces pombe, this protein exhibits a bifunctional architecture comprising a highly conserved N-terminal HORMA (Hop1, Rev7, and Mad2) domain responsible for recruiting key downstream autophagy factors, and a C-terminal intrinsically disordered region that mediates interactions with multiple scaffolding proteins and serves as a major site for nutrient-sensitive phosphorylation[3][9][27]. Through its unique structural plasticity and capacity for multivalent interactions, Atg13 provides a regulatory platform through which cells translate nutrient availability signals into precise spatiotemporal control of autophagy initiation, thereby enabling cellular adaptation to starvation conditions[17][33][39].

## Structural Organization and Protein Architecture

### The Bimodular Architecture of Atg13

The Atg13 protein exhibits a striking structural organization consisting of two functionally and structurally distinct regions that work synergistically to coordinate autophagy initiation[3][9][27]. The N-terminal region of approximately 260 amino acids folds into a HORMA domain, a protein-protein interaction module first characterized in the spindle checkpoint protein Mad2, while the C-terminal region spanning residues 260-520 (approximately) adopts an intrinsically disordered conformation that is critical for mediating interactions with other components of the autophagy machinery[3][24][25]. This unusual combination of a structured domain coupled with an intrinsically disordered region is essential for Atg13's functional versatility, as the HORMA domain provides specificity and stability while the disordered region confers the architectural flexibility necessary to accommodate multiple structurally diverse binding partners[3][9].

The bimodular architecture of Atg13 has been directly visualized through crystal structure determination. The 2.3-Å resolution structure of the budding yeast Atg13 HORMA domain reveals the characteristic HORMA fold, which consists of a predominantly α-helical structure with several beta strands forming a distinctive β-sheet architecture similar to that observed in Mad2[24][25]. Notably, the HORMA domain of Atg13 has a shorter "safety belt" region—the conformational switch that characterizes HORMA domains—consisting of only 13 residues in human Atg13 compared to 25-35 residues in budding yeast Atg13 and other HORMA proteins[10]. This architectural feature has profound implications for protein stability and function across different eukaryotic lineages.

### The Intrinsically Disordered Region and Multivalent Binding

The C-terminal intrinsically disordered region (IDR) of Atg13 is not simply a flexible linker but rather a structured chaos that provides the backbone for assembling the autophagy initiation complex[3][9][27]. This region contains multiple discrete binding sites that recognize different interaction partners, including Atg1, Atg17, Atg31, and Atg29 in budding yeast, or their functional equivalents in other organisms[3][9]. The IDR has been identified as containing at least two distinct Atg17-binding motifs designated as the 17LR (residues 359-389) and 17BR (residues 424-436), which bind to different dimers of the Atg17 scaffold protein[3][9]. Additionally, the MIT-interacting motif (MIM) within the IDR, spanning residues 460-521, specifically binds to the MIT (microtubule-interacting and transport) domain of Atg1[3][9]. The fact that these binding sites are separated by spacer regions and are capable of engaging multiple copies of their partner proteins is critical for understanding how Atg13 can serve as a "glue" bringing all components optimally together[3].

Hydrogen-deuterium exchange mass spectrometry (HDX-MS) studies have revealed that the C-terminal domain of Atg1 (the early autophagy targeting/tethering or EAT domain) is highly dynamic on its own, exchanging rapidly with solvent[20]. However, when bound to Atg13, the Atg1 EAT domain becomes significantly rigidified, with exchange rates reduced by more than 50-fold, suggesting that Atg13 binding induces a conformational transition that stabilizes the Atg1 EAT domain[20]. This stabilization is of profound functional importance, as it enables the combined Atg1-Atg13 complex to present a stable interface for binding to the Atg17-Atg31-Atg29 scaffold.

## The HORMA Domain and its Regulatory Architecture

### Structural Classification and Conformational States

The discovery that the N-terminal domain of Atg13 constitutes a HORMA fold represented an unexpected and paradigm-shifting finding[24][25]. HORMA domains, named after their discovery in Hop1, Rev7, and Mad2, have been primarily studied in the context of cell cycle checkpoint control, where the Mad2 protein undergoes conformational transitions between an open (O-Mad2) and closed (C-Mad2) state that are critical for its signaling function[7][35]. The structure of Atg13 HORMA corresponds to the C-Mad2-like conformation, suggesting that this represents a stable, locked state in the autophagy context[7][35]. This is a functionally important distinction because, unlike Mad2, the β5-αC loop of Atg13 HORMA is only 7 residues long, compared to 13 residues in Mad2, making a conformational transition between O-Mad2 and C-Mad2 states sterically unfavorable[7][35].

In the budding yeast species Lachancea thermotolerans, the Atg13 HORMA domain possesses a unique structural feature—a three-strand β-sheet insertion termed the "cap"—that is not observed in canonical HORMA domains[7][35]. This cap structure provides enhanced stability to the C-Mad2-like conformation without requiring assistance from the Atg101 protein[7][35]. Notably, this cap is absent in the Atg13 HORMA domains of higher eukaryotes that possess Atg101, explaining why these organisms require Atg101 for stabilization of the Atg13 HORMA domain[7][35]. This evolutionary variation reveals important functional insights into the roles of Atg101 and Atg13 in different organisms.

### The HORMA Domain as a Phosphate Sensor

Crystallographic analysis of the Atg13 HORMA domain has revealed a pair of conserved arginine residues that form a putative phosphate-binding pocket[24][25][48]. One of these arginine residues is positioned in the region corresponding to the "safety belt" conformational switch of Mad2, suggesting that the HORMA domain could function as a phosphoregulated conformational switch[24][25][48]. Mutation of these arginine residues (corresponding to Arg120 and Arg213 in S. cerevisiae Atg13) to aspartate—mimicking the charge distribution of a bound phosphate—completely abolishes autophagy function, demonstrating that these residues are essential for Atg13's role in the autophagy pathway[24][25][48]. The functional significance of the putative phosphate sensor has sparked speculation that Atg13 may undergo conformational changes upon binding to specific phosphorylated substrates or phospholipids, though direct evidence for such conformational changes remains to be definitively established.

### Stabilization through Atg101 Interaction

In fission yeast S. pombe, as in most eukaryotes except budding yeast, the Atg13 HORMA domain is stabilized through a heterodimeric interaction with Atg101, another HORMA-containing protein[1][7][31][32][35]. The crystal structure of the S. pombe Atg101-Atg13 complex reveals that Atg101 adopts an open Mad2-like (O-Mad2) conformation while Atg13 adopts the closed Mad2-like (C-Mad2) conformation[1][7][31][32][35]. This heterodimeric arrangement is analogous to the conformational heterodimer formed between O-Mad2 and C-Mad2 proteins in the spindle checkpoint, where the two conformations form a functionally important asymmetric dimer that influences the conformational stability of each protein[1][7][31][32][35]. The interface between Atg101 and Atg13 is primarily mediated by interactions between the HORMA domains of these two proteins, and specifically involves β-sheet interactions where the β2 strand of Atg101 interacts with the β2, β2', and β3 strands of Atg13[10].

Mutational studies have provided direct evidence for the importance of Atg101-Atg13 interactions. Experiments employing role-reversal mutagenesis, where key polar residues of Atg13 (Ser127 and Arg133) were mutated to match the residues found in Atg101 (His and Asp respectively), completely blocked complex formation as judged by strep pull-down assays[10]. Notably, the WF finger motif of Atg101, located in the β4-β5 loop region, is dispensable for the Atg101-Atg13 interaction and for overall Atg13 stabilization but is required for recruiting downstream autophagy-related factors such as LC3, WIPI1, and ZFYVE1/DFCP1 to the autophagosome formation site[7][35]. These findings indicate that while Atg101 and Atg13 function together as a stabilizing heterodimer, they make distinct contributions to the recruitment of downstream factors.

## Role in the Autophagy Initiation Complex

### Assembly of the Atg1 Kinase Complex

The primary function of Atg13 in autophagy is to serve as an essential adaptor protein that bridges the Atg1 serine/threonine protein kinase to the Atg17 scaffolding protein, thereby enabling the formation of the autophagy initiation complex[3][9][20][27][50][53]. Under nutrient-rich conditions, Atg13 exists in a constitutive or stable complex with Atg1, with binding occurring between the C-terminal portion of Atg13 (particularly residues 350-550) and the early autophagy targeting/tethering (EAT) domain of Atg1[20][50][53]. Isothermal titration calorimetry measurements have revealed that this interaction occurs with exceptionally high affinity, approximately 100 nanoMolar, which is characteristic of a stable, constitutive protein-protein interaction[20][50][53]. This tight binding rigidifies the Atg1 EAT domain, which is intrinsically dynamic on its own, bringing it into a conformationally stable state suitable for interaction with the Atg17-Atg31-Atg29 scaffold[20][50][53].

The assembly of the complete autophagy initiation complex follows a hierarchical pathway with distinct intermediate states[20][50][53]. The preformed Atg17-Atg31-Atg29 complex exists as a constitutive trimeric scaffold even under nutrient-rich conditions, when autophagy is suppressed[20][50][53]. Upon nutrient starvation or other autophagy-inducing signals, the Atg1-Atg13 dimer is recruited as a functional unit to bind the Atg17-Atg31-Atg29 scaffold[20][50][53]. Notably, the affinity of the Atg1-Atg13 complex for the Atg17-Atg31-Atg29 scaffold is approximately 10 microMolar—a value two orders of magnitude weaker than the Atg1-Atg13 interaction[20][50][53]. This dramatic difference in binding affinities is functionally significant because it makes the recruitment of Atg1-Atg13 to the scaffold a regulated step that can be modulated by post-translational modifications, protein concentration changes, and membrane localization.

The quaternary structure of the assembled complex is that of a dimer of pentamers, with the pentameric unit consisting of 2:1:1:1:1 stoichiometry for Atg1:Atg13:Atg17:Atg31:Atg29[20][53]. The dimerization of the pentameric units likely occurs through interactions between the Atg17 subunits, which form homodimers that create the characteristic S-shaped or double-crescent curvature[20][53]. This structural organization places the Atg13-binding sites at the tips of the double-crescent structure formed by Atg17, creating a platform from which the Atg1 kinase domain can access downstream substrates for phosphorylation.

### Atg13 as an Assembly Hub and Scaffold

Beyond its role in recruiting Atg1 to the Atg17 scaffold, Atg13 functions as a nucleation point for the assembly of higher-order structures. Recent studies have revealed that Atg13 interacts with at least six structurally diverse partners: Atg1, Atg17, Atg9, Atg14, Atg31, and lipid membranes[3][9][27]. This multivalent binding capability defines Atg13 as a hub protein, a class of proteins distinguished by their capacity to make numerous binding connections with structurally diverse partners[3][9]. Analysis of hub proteins in biological systems has revealed that intrinsic disorder is a common feature that enables hub proteins to maintain multiple binding interactions without incurring prohibitive steric clashes[3][9]. The architectural plasticity of Atg13 is thus not incidental but rather a functional necessity—only through such flexibility can the protein prevent steric hindrance when accommodating structurally diverse binding partners within a compact molecular assembly[3][9].

The role of Atg13 as an assembly hub extends to its function in organizing the phagophore assembly site (PAS), a discrete cytoplasmic location where autophagosome biogenesis is initiated[3][22][44]. Atg13 is recruited to the PAS early in the autophagy response through its interaction with Atg17, which is already present at the PAS even under nutrient-rich conditions[3][22]. At the PAS, Atg13 serves as a tethering point for other Atg proteins, thereby building up a multi-protein machine capable of nucleating and coordinating the early stages of autophagosome formation. The vacuolar membrane protein Vac8 has been shown to interact directly with the C-terminal region of Atg13, anchoring the PAS to the vacuolar periphery[44][57]. This interaction is crucial for robust autophagy, as evidenced by the observation that deletion of Vac8 or disruption of the Vac8-Atg13 interaction significantly reduces autophagy efficiency[44][57].

## Function in Autophagosome Assembly

### Recruitment of Atg9 Vesicles through the HORMA Domain

The N-terminal HORMA domain of Atg13 has been identified as the critical determinant for recruitment of Atg9 vesicles to the phagophore assembly site[15][18][19][26][29]. Atg9 is the sole integral membrane protein among the core autophagy machinery, residing on specific cytoplasmic vesicles (Atg9 vesicles) that are approximately 20-30 nanometers in diameter[15][18][19]. These Atg9 vesicles are believed to serve as membrane donors that contribute lipids to the growing phagophore membrane during autophagosome biogenesis. Through a series of well-designed mutation studies, researchers demonstrated that the HORMA domain of Atg13 binds directly to the N-terminal cytoplasmic domain of Atg9, and that this interaction is essential for PAS localization of Atg9 vesicles and for starvation-induced autophagy[15][18][19][26][29].

Specific amino acid residues within the Atg13 HORMA domain have been identified as critical for Atg9 binding. The mutations D203A and E81L, which are located in the HORMA domain and eliminate or severely impair Atg13-Atg9 binding, result in profound autophagy defects, with D203A reducing the frequency of Atg9 colocalization with the PAS marker Atg17 from 87.6% in wild-type cells to only 26.7%[15][19][26]. Remarkably, these same mutations do not significantly affect the Atg1-Atg13 interaction or Atg13 recruitment to the PAS itself[15][19][26], indicating that the HORMA domain's role in Atg9 recruitment is functionally separable from its role (if any) in Atg1 stabilization in the fission yeast context.

The Atg13-Atg9 interaction occurs independently of Atg17, as evidenced by coimmunoprecipitation experiments demonstrating that Atg9 still coprecipitates with Atg13 even in cells lacking Atg1, Atg11, and Atg17[15][19][26]. However, the reverse is not true—Atg17 interacts with Atg9 primarily through Atg13 rather than through direct contact[15][19][26]. These findings establish a clear hierarchical recruitment model in which Atg13 is the primary determinant of Atg9 vesicle recruitment to the PAS, with downstream consequences for the recruitment of other autophagy factors.

### Recruitment of the PI3K Complex and Downstream Factors

A key functional consequence of Atg9 recruitment via the Atg13 HORMA domain is the subsequent localization of the class III phosphatidylinositol 3-kinase (PI3K) complex to the PAS[15][19][26]. The PI3K complex in yeast consists of Atg6/Vps30, Atg14, Vps15, and the catalytic kinase Vps34, and its localized activity generates phosphatidylinositol 3-phosphate (PI3P) on the phagophore membrane[15][19][26][48]. This locally generated PI3P serves as a membrane signal that recruits numerous downstream autophagy factors containing PI3P-binding domains, such as the WIPI proteins. Notably, the PAS localization of Atg14, a key subunit of the PI3K complex, is severely impaired in cells lacking Atg9 (with localization frequency dropping from 71.7% to 6.6%)[15][19][26], suggesting that the recruitment of the PI3K complex to the PAS is at least partially dependent on Atg9 availability rather than being directly mediated by the Atg13 HORMA domain.

## Phosphorylation-Based Regulation of Atg13

### Nutrient-Sensing Phosphorylation and TORC1 Signaling

The phosphorylation state of Atg13 represents the primary molecular mechanism through which cells translate nutrient availability signals into autophagy induction or suppression[13][14][16][17][38][39]. Under nutrient-rich conditions, Atg13 exists in a hyperphosphorylated state maintained by the target of rapamycin (TOR) kinase and other kinases including protein kinase A (PKA)[13][14][16][17][38][39]. This hyperphosphorylation prevents the Atg1-Atg13-Atg17 complex from assembling and functioning effectively, thereby suppressing autophagy during periods of nutrient abundance. Upon nutrient starvation or inactivation of TOR signaling through pharmacological inhibition by rapamycin, Atg13 undergoes rapid dephosphorylation by specific protein phosphatases, which enhances its interaction with Atg1 and Atg17, leading to rapid autophagy induction[13][14][16][17][38][39].

In mammalian cells, extensive phosphoproteomic studies have identified nutrient-regulated phosphorylation sites on ATG13, with Ser224 and Ser258 being among the most prominent[13][38]. These sites are phosphorylated in response to mTOR signaling under nutrient-rich conditions and are rapidly dephosphorylated upon amino acid starvation[13][38]. Critically, the dephosphorylation at these sites is specifically triggered by amino acid starvation rather than serum starvation, indicating that ATG13 functions as a sensor of amino acid availability[13][38]. This distinction has important physiological implications, as it allows cells to respond differently to different types of nutrient deprivation. In yeast, the primary phosphorylation sites targeted by TOR (and PKA) include Ser379 (within the 17LR motif), Ser428, and Ser429 (within the 17BR motif), among others[14][17][39].

### Multi-site Phosphorylation and Dynamic Regulation

Recent comprehensive phosphoproteomics studies have revealed that the regulation of Atg13 is far more complex than previously appreciated, with 48 distinct in vivo phosphorylation sites being identified on yeast Atg13[17][39]. Most of these sites (36 out of 48) are regulated by nutrient status, being present predominantly under nutrient-rich conditions and reduced or absent upon starvation[17][39]. Remarkably, only two phosphorylation sites are reversely regulated, being reduced in nutrient-rich conditions and increased upon starvation[17][39]. The functional significance of this extensive phosphorylation pattern has been demonstrated through mutational analysis. When all identified nutrient-regulated phosphorylation sites are simultaneously mutated to alanine (creating the Atg13^44A^ mutant that mimics the dephosphorylated state), cells exhibit hyperactive autophagy even under nutrient-rich conditions[17][39]. Conversely, when these sites are mutated to aspartate (creating the Atg13^44D^ or Atg13^46D^ mutants that mimic the phosphorylated state), bulk autophagy is completely suppressed[17][39].

These findings demonstrate that Atg13 functions as a signaling hub that can promote or inhibit autophagy depending on its overall phosphorylation state. Importantly, disrupting the dynamic regulation of Atg13 phosphorylation through either constitutive dephosphorylation or phosphorylation leads to detrimental outcomes for cell survival[17][39]. The hyperactive autophagy observed with the Atg13^44A^ mutant results in excessive protein degradation even when cells have sufficient nutrients, while the complete suppression observed with the phospho-mimetic mutant prevents autophagy induction even under starvation conditions. Both of these extreme outcomes are harmful to cellular fitness, suggesting that precise temporal regulation of Atg13 phosphorylation is essential for appropriate autophagy control[17][39].

### Phosphatase-Mediated Dephosphorylation

The dephosphorylation of Atg13 upon autophagy induction is catalyzed by specific protein phosphatases. In budding yeast, the PP2C-family phosphatases Ptc2 and Ptc3 have been identified as the primary phosphatases responsible for dephosphorylating Atg13[14]. In strains lacking both Ptc2 and Ptc3 (ptc2Δ ptc3Δ double mutants), Atg13 remains hyperphosphorylated even under starvation conditions when TORC1 activity is suppressed, and both starvation-induced macroautophagy and the cytoplasm-to-vacuole targeting (Cvt) pathway are blocked[14]. The failure to dephosphorylate Atg13 in these mutants impairs the recruitment of the autophagy machinery to the phagophore assembly site, demonstrating the functional importance of Ptc2 and Ptc3 in autophagy regulation[14]. Interestingly, the dephosphorylation of Atg13 is independent of autophagy flux and Atg1 kinase activity, as evidenced by the observation that Atg13 is dephosphorylated even in autophagy-defective Atg1 kinase mutant strains[14], suggesting that phosphatase activity is constitutively active and regulated independently of the autophagy flux itself.

## Protein-Protein Interactions and Multivalent Assembly

### The MIT-Interacting Motif and Atg1 Activation

The C-terminal intrinsically disordered region of Atg13 contains a highly conserved MIT (microtubule-interacting and transport)-interacting motif that spans approximately residues 460-521 and binds specifically to the MIT domain of Atg1[3][9][20]. This interaction is regulated by phosphorylation—dephosphorylation of serine residues within the MIT-interacting motif enhances the affinity of this interaction[3][9]. The functional significance of the Atg13-Atg1 MIT interaction is that it brings the kinase domain of Atg1 into optimal proximity to its substrate proteins, thereby facilitating the autophosphorylation of Atg1 and its phosphorylation of downstream targets[3][9][27]. In vitro studies and cellular analyses have demonstrated that the binding of dephosphorylated Atg13 to Atg1 dramatically enhances the kinase activity of Atg1, effectively activating the enzyme for subsequent rounds of substrate phosphorylation[3][9].

### The Atg17-Binding Regions and Multivalent Interactions

The C-terminal IDR of Atg13 contains at least two distinct Atg17-binding motifs, designated as the 17LR (Atg17 long range, residues 359-389) and 17BR (Atg17 binding region, residues 424-436), that enable Atg13 to engage multiple copies of the Atg17 dimer[3][9]. The binding of Atg13 to Atg17 is regulated by dephosphorylation of specific serine residues: phosphorylation of Ser379 (within the 17LR motif) and Ser428 and Ser429 (within the 17BR motif) inhibit binding, while dephosphorylation of these sites enhances the Atg13-Atg17 interaction[3][9]. Notably, the 17LR motif requires the dimerization of Atg17 for efficient binding—monomeric Atg17 cannot effectively bind the 17LR region[3][9]. This requirement for Atg17 dimerization adds another regulatory layer, as it couples the formation of stable Atg1 complexes to Atg17 oligomerization.

The binding of Atg13 to the Atg17 dimer interface via the dephosphorylated 17LR region initiates a conformational change in the Atg17-Atg31-Atg29 complex[3][9]. Specifically, this Atg13 binding causes a pivoting movement of the Atg31-Atg29 subcomplex away from the inhibitory position it occupies at the center of the Atg17 crescent, thereby activating the Atg17-Atg31-Atg29 trimer and opening up binding sites for subsequent recruitment of Atg9 vesicles[3][9]. This model elegantly explains why the monomeric Atg17-Atg31-Atg29 complex and even the pentameric Atg17-Atg31-Atg29-Atg13-Atg1 complex cannot efficiently bind and tether Atg9 vesicles—these monomeric complexes simply do not present the Atg13-binding site at the Atg17 dimer interface[3][9].

### Phase Separation and Atg13-Driven Liquid Condensate Formation

Recent studies have revealed that the autophagy initiation complex undergoes phase separation to form liquid condensate structures at the phagophore assembly site[33]. The multivalent interactions between Atg17 and Atg13, mediated by the presence of multiple binding sites and their demonstrated cooperativity, are sufficient to drive phase separation of the Atg1 complex[33]. Specifically, the interaction between Atg17 and Atg13, through both the 17LR and 17BR motifs, creates the type of multivalent binding network required for liquid-liquid phase separation[33]. This phase separation is critical for creating a liquid microenvironment at the PAS with properties conducive to the rapid recruitment and assembly of other autophagy factors. The importance of this mechanism is underscored by the finding that disruption of Atg13's multivalent binding capability through phosphorylation or mutation impairs not only the assembly of the Atg1 complex but also the formation of the PAS itself[33].

## Cellular Localization and Subcellular Compartmentalization

### Recruitment to the Phagophore Assembly Site

Under starvation conditions, Atg13 is recruited from a diffuse cytoplasmic distribution to discrete punctate structures that correspond to the phagophore assembly site (PAS)[3][22][44][47]. This recruitment does not depend on the N-terminal HORMA domain, contrary to what might be expected given the involvement of HORMA domains in protein-protein interactions[3][22][26]. Instead, the initial translocation of Atg13 to the PAS is mediated by its C-terminal intrinsically disordered region and specifically by its capacity to bind Atg17[3][22][26]. The fact that Atg17 is constitutively present at the PAS, even under nutrient-rich conditions when autophagy is suppressed, suggests that the PAS represents a specialized cellular microcompartment that is pre-organized and ready to recruit additional factors upon receiving the appropriate nutrient-deprivation signal[3][22][26].

The localization of Atg13 to the PAS is further refined by its interaction with the vacuolar membrane protein Vac8[44][57]. Vac8 acts as a physical anchor that tethers the PAS machinery to the vacuolar periphery, and it does so through a direct interaction with Atg13[44][57]. The interaction between Vac8 and Atg13 is mediated by the C-terminal region of Atg13 (specifically residues 659-693 based on studies with truncated Atg13 constructs), and this interaction is essential for robust autophagy induction[44][57]. When Atg13 is truncated to remove the Vac8-binding region, the protein can still localize to punctate structures but does so with reduced efficiency and the structures do not properly associate with the vacuolar membrane[44][57]. These findings establish a hierarchical recruitment model in which Vac8-mediated anchoring of Atg13 to the vacuole is followed by Atg13-dependent recruitment of the Atg1 kinase complex.

### Localization to the Vacuole-Isolation Membrane Contact Site (VICS)

High-resolution microscopy studies employing giant cargo overexpression to stall the developing phagophore have revealed that Atg13 localizes specifically to a discrete subcellular microdomaine termed the vacuole-isolation membrane contact site (VICS)[44][47][57]. This 20-40 nanometer-wide zone represents the physical point of contact between the inner membrane of the phagophore (isolation membrane or IM) and the outer surface of the vacuole[44][47][57]. Other early autophagy machinery proteins localize to the VICS, including subunits of the PI3KC1 complex and Atg17, suggesting that this contact site serves as a specialized reaction compartment for early autophagy events[44][47][57]. Interestingly, Atg1, despite forming a complex with Atg13 and Atg17, is not confined exclusively to the VICS but rather is found distributed throughout the phagophore membrane, suggesting that Atg1 may function in spatially extended reactions beyond the initial contact site[44][47][57].

## Comparative Function Across Eukaryotic Species

### Differences Between Fission Yeast and Budding Yeast

While Atg13 is conserved across eukaryotes, its precise role in autophagy initiation has diverged somewhat between different organisms. In budding yeast (Saccharomyces cerevisiae), where the role of Atg13 has been most thoroughly characterized, Atg13 is essential for autophagy and serves as a critical link between the Atg1 kinase and the Atg17-Atg31-Atg29 scaffold[3][9][20][27]. Notably, budding yeast lacks Atg101, and instead possesses Atg29 and Atg31 as unique components of its autophagy initiation complex[7][35][45]. In contrast, fission yeast (S. pombe) possesses Atg101 instead of Atg29 and Atg31, and this compositional difference is accompanied by subtle but important functional differences[8][11][45].

In S. pombe, Atg13 still plays a critical scaffolding role, but there are interesting variations in the requirements for autophagy induction. Unlike in budding yeast, where Atg13 is absolutely required for autophagy, a recent study in fission yeast discovered that Atg1 kinase activation can occur without Atg13 in certain contexts, specifically requiring Atg11 instead[8]. This finding, while seeming to contradict the essential role of Atg13, actually highlights the functional plasticity of the autophagy machinery and suggests that there may be alternative activation pathways that vary between yeast species. The Atg1 kinase activity in S. pombe requires Atg11 through cis-autophosphorylation, a mechanism that appears to be distinct from the trans-phosphorylation mechanism thought to operate in budding yeast[8].

### Atg101 Stabilization of Atg13 HORMA Domain in Higher Eukaryotes

In most eukaryotes except budding yeast, including fission yeast and mammals, the Atg13 HORMA domain depends on stabilization by Atg101[7][35][45]. The structural basis for this dependency was clarified through crystal structure determination showing that the fission yeast Atg13 HORMA domain, when complexed with Atg101, forms a heterodimer in which Atg101 adopts an O-Mad2-like conformation while Atg13 adopts a C-Mad2-like conformation[1][7][31][32][35]. This heterodimer arrangement appears to be optimized for function in the autophagy pathway, as the two HORMA domains in the Atg101-Atg13 complex would mediate distinct sets of protein-protein interactions to enable sophisticated regulation of autophagy initiation in higher eukaryotes[7][35].

Recent AlphaFold3 structure predictions suggest that the evolutionary history of the Atg1 complex may involve greater complexity than previously appreciated[45]. Specifically, the Atg13 HORMA domain of S. pombe may possess a stabilizing cap structure that was not observed in crystallographic studies but was predicted by AlphaFold3 modeling[45]. If confirmed through experimental studies, this would suggest that Atg101 may have evolved to play a regulatory role distinct from simple stabilization, possibly facilitating the recruitment of specific downstream factors through the WF finger motif. The evolution of Atg1 complex composition and the roles of Atg13 and Atg101 thus represent an area of ongoing investigation with implications for understanding autophagy regulation across the eukaryotic phylogeny.

## Conclusion

Atg13 from Schizosaccharomyces pombe represents a paradigmatic example of how structural flexibility combined with multivalent binding capability enables a single protein to coordinate the assembly of a complex multi-protein machine. The protein's bimodular architecture—comprising a structured HORMA domain for specific interaction recognition and a disordered C-terminal region for flexible accommodation of multiple binding partners—exemplifies how proteins can overcome the apparent conflict between specificity and adaptability. The HORMA domain, beyond its role in stabilizing interactions with Atg101 in higher eukaryotes, functions as a hub for recruiting Atg9 vesicles and potentially recognizing other key downstream factors in the autophagy pathway.

The phosphorylation-based regulation of Atg13 represents a sophisticated mechanism through which cells integrate nutrient status signals into precise control of autophagy initiation. With at least 48 distinct phosphorylation sites identified on yeast Atg13, the protein functions not as a binary switch but rather as a rheostat that can be finely tuned through dynamic post-translational modification. The discovery that disruption of this dynamic regulation—whether through constitutive dephosphorylation or phosphorylation—leads to harmful autophagic outcomes emphasizes the importance of precise temporal control in this essential cellular pathway.

The role of Atg13 as a molecular hub anchoring the autophagy initiation complex to the vacuolar periphery through interactions with Vac8, combined with its function in organizing multivalent interactions that drive phase separation of the Atg1 complex, highlights the importance of spatial organization in autophagy regulation. These findings suggest that future therapeutic strategies targeting autophagy might beneficially focus on modulating Atg13 function through interventions that affect its phosphorylation state, its protein-protein interactions, or its ability to nucleate phase-separated condensates at the PAS. The conservation of Atg13 function and structure across eukaryotic species, combined with its central regulatory role in autophagy initiation, establishes this protein as a critical target for understanding and potentially manipulating autophagy in both fundamental research and clinical contexts[3][9][13][14][17][20][27][39][50][53].

---

## References

The following sources were cited in this comprehensive research report on Atg13 (O36019) from Schizosaccharomyces pombe:

[1] Suzuki, H., Kaizuka, T., Mizushima, N., & Noda, N.N. (2015). Structure of the Atg101-Atg13 complex reveals essential roles of Atg101 in autophagy initiation. Nature Structural & Molecular Biology, 22(7), 572-580.

[3] Popelka, H., Mizushima, N. (2017). The molecular mechanism of Atg13 function in autophagy. Autophagy.

[7] Suzuki, H., Noda, N.N. (2016). Open and closed HORMAs regulate autophagy initiation. Proceedings of the National Academy of Sciences.

[8] Fujioka, Y., Suzuki, S.W., Yamamoto, H., Kondo-Kakuta, C., Kimura, Y., Hirano, H., & Ohsumi, Y. (2020). Atg1 kinase in fission yeast is activated by Atg11-mediated dimerization independent of Atg13, Atg17, or Atg101. eLife.

[9] Popelka, H. et al. (2017). The molecular mechanism of Atg13 function in autophagy induction. PMC5361603.

[10] Hurley, J.H. et al. (2016). Structure of the human Atg13-Atg101 HORMA heterodimer. PMC4598286.

[11] Suzuki, S.W., et al. (2018). Conserved and unique features of the fission yeast core Atg1 complex. Molecular Biology of the Cell.

[13] Jung, C.H., et al. (2016). Nutrient-regulated phosphorylation of ATG13 inhibits starvation-induced autophagy. PNAS, 113(45), E6797-E6806.

[14] Wang, Z., et al. (2019). PP2C phosphatases promote autophagy by dephosphorylation of Atg13. PNAS, 116(20), 9881-9886.

[15] Suzuki, S.W., Yamamoto, H., Oikawa, Y., Kondo-Kakuta, C., Kimura, Y., Hirano, H., & Ohsumi, Y. (2015). Atg13 HORMA domain recruits Atg9 vesicles during autophagosome formation. Proceedings of the National Academy of Sciences, 112(11), 3350-3355.

[16] Mirouse, V., et al. (2010). The Tor and PKA signaling pathways independently target the Atg1/Atg13 kinase complex to control autophagy. PNAS, 106(40), 17049-17054.

[17] Mao, K., et al. (2024). Decoding the function of Atg13 phosphorylation reveals a role of Atg11 in bulk autophagy. PMC10897315.

[20] Fujioka, Y., et al. (2014). Assembly and dynamics of the autophagy-initiating Atg1 complex. PNAS, 111(35), E3704-E3713.

[22] Kawamata, T., Kamada, Y., Kabeya, Y., Sekito, T., & Ohsumi, Y. (2008). Organization of the pre-autophagosomal structure responsible for autophagosome formation. Molecular Biology of the Cell, 19(5), 2039-2050.

[24] Jao, C.C., et al. (2013). A HORMA domain in Atg13 mediates PI 3-kinase recruitment in autophagy. PNAS, 110(14), 5486-5491.

[25] Jao, C.C., et al. (2013). A HORMA domain in Atg13 mediates PI 3-kinase recruitment. PNAS, 110(14), 5486-5491.

[26] Suzuki, S.W., et al. (2015). Atg13 HORMA domain recruits Atg9 vesicles. PNAS, 112(11), 3350-3355.

[27] Nakatogawa, H. (2013). ATG13: Just a companion, or an executor of the autophagic program? Autophagy, 9(12), 1693-1695.

[33] Mao, K., et al. (2024). Decoding the function of Atg13 phosphorylation reveals a role of Atg11 in bulk autophagy. PMC10897315.

[35] Suzuki, H., Noda, N.N. (2016). Open and closed HORMAs regulate autophagy initiation. Trends in Cell Biology.

[38] Jung, C.H., et al. (2016). Nutrient-regulated phosphorylation of ATG13. PNAS.

[39] Mao, K., et al. (2024). Decoding the function of Atg13 phosphorylation. PMC10897315.

[44] Hollenstein, D.M., et al. (2021). Vac8 determines phagophore assembly site vacuolar localization. PMC8354615.

[45] Mao, K., et al. (2024). Revisiting the evolution of the yeast Atg1 complex. PMC12482441.

[47] Kraft, C., et al. (2012). ATG13: Just a companion, or an executor of the autophagic program? PMC4091178.

[50] Fujioka, Y., et al. (2016). How the Atg1 complex assembles to initiate autophagy. PMC4502730.

[53] Fujioka, Y., et al. (2014). Assembly and dynamics of the autophagy-initiating Atg1 complex. PNAS, 111(35), 12795-12800.

[57] Hollenstein, D.M., et al. (2024). How membrane contact sites shape the phagophore. PMC10243513.

## Citations

1. https://pubmed.ncbi.nlm.nih.gov/26030876/
2. https://www.uniprot.org/uniprotkb/O36019/history
3. https://pmc.ncbi.nlm.nih.gov/articles/PMC5361603/
4. https://www.uniprot.org/uniprotkb/O36019/entry
5. https://www.ebi.ac.uk/interpro/protein/reviewed/O36019/
6. https://dnaconda.riken.jp/search/SPD_pombe/Sp38/Sp38E11.html
7. https://pmc.ncbi.nlm.nih.gov/articles/PMC4824606/
8. https://elifesciences.org/articles/58073
9. https://pmc.ncbi.nlm.nih.gov/articles/PMC4598286/
10. https://pubmed.ncbi.nlm.nih.gov/28976798/
11. https://disprot.org/DP01732
12. https://pmc.ncbi.nlm.nih.gov/articles/PMC4786734/
13. https://www.pnas.org/doi/10.1073/pnas.1817078116
14. https://www.pnas.org/doi/10.1073/pnas.1421092112
15. https://www.pnas.org/doi/10.1073/pnas.0903316106
16. https://pmc.ncbi.nlm.nih.gov/articles/PMC10897315/
17. https://pubmed.ncbi.nlm.nih.gov/25737544/
18. https://pmc.ncbi.nlm.nih.gov/articles/PMC4156731/
19. https://pmc.ncbi.nlm.nih.gov/articles/PMC3722324/
20. https://pubmed.ncbi.nlm.nih.gov/18287526/
21. https://www.molbiolcell.org/doi/10.1091/mbc.e08-12-1250
22. https://www.pnas.org/doi/abs/10.1073/pnas.1220306110?doi=10.1073%2Fpnas.1220306110
23. https://pmc.ncbi.nlm.nih.gov/articles/PMC4091178/
24. https://www.rcsb.org/structure/4j2g
25. https://www.yeastgenome.org/locus/ATG13
26. https://www.rcsb.org/structure/4yk8
27. https://febs.onlinelibrary.wiley.com/doi/full/10.1002%2F1873-3468.14717
28. https://pmc.ncbi.nlm.nih.gov/articles/PMC7255502/
29. https://pmc.ncbi.nlm.nih.gov/articles/PMC12313203/
30. https://www.molbiolcell.org/content/20/7/1981?related-urls=yes&legid=molbiolcell%3B20%2F7%2F1981
31. https://pubmed.ncbi.nlm.nih.gov/27768871/
32. https://pmc.ncbi.nlm.nih.gov/articles/PMC7610778/
33. https://pmc.ncbi.nlm.nih.gov/articles/PMC8354615/
34. https://pmc.ncbi.nlm.nih.gov/articles/PMC12482441/
35. https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2020.00565/full
36. https://www.pnas.org/doi/10.1073/pnas.1220306110
37. https://www.molbiolcell.org/doi/10.1091/mbc.e08-12-1249
38. https://pmc.ncbi.nlm.nih.gov/articles/PMC4502730/
39. https://pmc.ncbi.nlm.nih.gov/articles/PMC3738441/
40. https://pmc.ncbi.nlm.nih.gov/articles/PMC9851266/
41. https://www.pnas.org/doi/pdf/10.1073/pnas.1407214111
42. https://www.pombase.org/gene/SPAC4F10.07c
43. https://onlinelibrary.wiley.com/doi/10.1111/j.1365-2443.2007.01041.x
44. https://pmc.ncbi.nlm.nih.gov/articles/PMC8821819/
45. https://pmc.ncbi.nlm.nih.gov/articles/PMC10243513/
46. https://pubmed.ncbi.nlm.nih.gov/17295836/
47. https://www.uniprot.org/uniprotkb/Q06628/entry
48. https://www.ncbi.nlm.nih.gov/gene/856315