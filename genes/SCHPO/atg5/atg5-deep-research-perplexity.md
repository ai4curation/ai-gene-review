---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-01-30T19:46:11.900363'
end_time: '2026-01-30T19:48:05.091155'
duration_seconds: 113.19
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: SCHPO
  gene_id: atg5
  gene_symbol: atg5
  uniprot_accession: O74971
  protein_description: 'RecName: Full=Autophagy protein 5; AltName: Full=Meiotically
    up-regulated gene 77 protein;'
  gene_info: Name=atg5; Synonyms=mug77; ORFNames=SPBC4B4.10c;
  organism_full: Schizosaccharomyces pombe (strain 972 / ATCC 24843) (Fission yeast).
  protein_family: Belongs to the ATG5 family. .
  protein_domains: Atg5. (IPR007239); ATG5_HBR. (IPR048940); Atg5_HR. (IPR042526);
    ATG5_UblA. (IPR048939); Atg5_UblA_dom_sf. (IPR042527)
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 52
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** O74971
- **Protein Description:** RecName: Full=Autophagy protein 5; AltName: Full=Meiotically up-regulated gene 77 protein;
- **Gene Information:** Name=atg5; Synonyms=mug77; ORFNames=SPBC4B4.10c;
- **Organism (full):** Schizosaccharomyces pombe (strain 972 / ATCC 24843) (Fission yeast).
- **Protein Family:** Belongs to the ATG5 family. .
- **Key Domains:** Atg5. (IPR007239); ATG5_HBR. (IPR048940); Atg5_HR. (IPR042526); ATG5_UblA. (IPR048939); Atg5_UblA_dom_sf. (IPR042527)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "atg5" matches the protein description above**
2. **Verify the organism is correct:** Schizosaccharomyces pombe (strain 972 / ATCC 24843) (Fission yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'atg5' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **atg5** (gene ID: atg5, UniProt: O74971) in SCHPO.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# ATG5 (Autophagy-Related Protein 5) in Schizosaccharomyces pombe: Molecular Architecture, Function, and Mechanisms in Autophagosome Biogenesis

## Executive Summary

Autophagy protein 5 (ATG5), encoded by the *atg5* gene in *Schizosaccharomyces pombe* (fission yeast), is a highly conserved protein that serves as a critical structural and catalytic component of the autophagy machinery. This report synthesizes current understanding of ATG5 from model organisms, with particular emphasis on its conserved functions that are directly applicable to the fission yeast homolog. ATG5 functions primarily as an essential component of the ubiquitin-like conjugation systems that drive autophagosome biogenesis. Specifically, ATG5 forms a covalent conjugate with the ubiquitin-like protein ATG12 through an enzymatic cascade involving E1-like activation (ATG7) and E2-like transfer (ATG10) activities, and this ATG12–ATG5 conjugate further associates with ATG16 to form a multimeric E3-like complex. This ATG12–ATG5–ATG16 complex functions at the pre-autophagosomal structure to promote the lipidation of ATG8 (also known as LC3 or GABARAP in mammals) with the membrane lipid phosphatidylethanolamine, a modification essential for autophagosome membrane dynamics and substrate recruitment. Beyond its catalytic roles, ATG5 possesses intrinsic membrane-binding capacity that is regulated by its association with other ATG proteins, enabling the complex to tether and organize nascent autophagosomal membranes. The localization and activity of ATG5 are dynamically regulated through nutrient sensing pathways involving the TOR kinase complex and through post-translational modifications that modulate its protein-protein interactions and catalytic potential.

---

## Protein Structure and Domain Organization

### Structural Architecture

The ATG5 protein is composed of a distinctive modular architecture consisting of three functionally relevant domains arranged in a characteristic configuration.[49] The N-terminal region of ATG5 contains a ubiquitin-like fold domain (herein referred to as UblA or UFD-1), which spans approximately residues 1-105 and provides critical interaction surfaces for other autophagy proteins.[37][52] This first ubiquitin-like fold domain is followed by an α-helical bundle region (designated HBR or HR, for helix-rich domain) spanning roughly residues 106-200, which serves as the primary site for conjugation with ATG12 and contains the conserved lysine residue (lysine 130 in humans, corresponding to the absolutely conserved conjugation site in all eukaryotes) that forms the isopeptide bond with the C-terminal glycine of ATG12.[24][37][52] A second ubiquitin-like fold domain (UblB or UFD-2) comprising approximately residues 201-280 completes the protein architecture and provides a binding surface for interaction with ATG16L1 (or ATG16 in yeast).[24][37][52] These three domains are connected by linker regions designated L1 and L2, which provide conformational flexibility while maintaining the integrated three-dimensional structure.[50]

The structural organization of ATG5, as revealed through crystallographic studies, demonstrates that the two ubiquitin-like fold domains flank the central helical bundle region in a manner that creates multiple functional surfaces on the protein.[49][52] Critically, ATG12 and ATG16 occupy opposite sides of the ATG5 molecule, with ATG12 positioned such that its C-terminal tail folds back onto its own ubiquitin-fold domain through interactions between conserved tryptophan and tyrosine residues.[24][52] This C-terminal configuration is unique among ubiquitin-like proteins and suggests specialized structural requirements for the ATG5 conjugation interface.[24] The non-covalent contacts between conjugated ATG12 and ATG5 bury approximately 1,300 Ångströms² of solvent-accessible surface area, with the conserved lysine 130 residue serving dual roles as both the site of covalent isopeptide bonding and as a structural element integral to the protein-protein interface.[24][37][52]

### Evolutionary Conservation and Domain Families

ATG5 belongs to a highly conserved protein family represented across all eukaryotic organisms, from unicellular fungi to multicellular plants and animals, with the fission yeast homolog sharing remarkable sequence and structural homology with human and budding yeast orthologs.[2][4][46][49] The protein contains multiple annotated domain families according to the InterPro database: the Atg5 domain (IPR007239), the ATG5 helix-rich region (IPR042526), the ATG5_UblA domain (IPR048939), the Atg5_UblA domain superfamily (IPR042527), and the ATG5_HBR domain (IPR048940).[49] The conservation of these structural features across evolutionary time and across diverse eukaryotic lineages underscores the fundamental importance of ATG5's modular organization for its biological function.[49] In structural comparisons between fission yeast and human ATG5, the core architecture and the critical interaction surfaces remain essentially unchanged, indicating that detailed molecular mechanisms elucidated in one organism are directly applicable to others.[37][52]

---

## Role in the Ubiquitin-Like Conjugation Systems and Autophagosome Formation

### The ATG12–ATG5 Conjugation System

ATG5 is the primary target of the ubiquitin-like conjugation system mediated by ATG12, a small ubiquitin-like protein that becomes covalently attached to ATG5 through a precisely regulated enzymatic cascade.[7][19][20][21] This conjugation process parallels ubiquitination but occurs with distinct substrates and regulatory mechanisms. The conjugation begins when ATG12 is activated by the E1-like enzyme ATG7, which catalyzes the ATP-dependent formation of a high-energy thioester bond between a conserved cysteine residue (Cys507 in budding yeast) in ATG7 and the C-terminal carboxyl group of ATG12, generating an activated ATG12~ATG7 intermediate.[19][21][38][39] This intermediate is then transferred to the E2-like enzyme ATG10, which catalyzes the formation of a thioester intermediate between ATG12 and ATG10 (specifically at Cys166 of yeast ATG10).[19][21][39] Finally, ATG10 catalyzes the formation of an isopeptide bond between the C-terminal glycine of ATG12 and the ε-amino group of the conserved lysine residue 130 (Lys130 in yeast, Lys130 in humans) of ATG5, generating the stable ATG12–ATG5 conjugate.[19][20][21][40]

The formation of the ATG12–ATG5 conjugate is remarkable for being essentially irreversible under physiological conditions, with the conjugation occurring with high efficiency such that unconjugated ATG5 is rarely observed in vivo.[40][42] This efficiency reflects the catalytic precision of the ATG7 and ATG10 enzymes and the structural complementarity of the ATG12 and ATG5 molecules at their interaction interface. Genetic and biochemical analyses have established that ATG5 is the sole target of ATG12 conjugation among eukaryotic proteins, and that ATG10 is the cognate E2 enzyme responsible for this system, highlighting the specificity of ubiquitin-like conjugation pathways.[19][21][40][42]

### The ATG12–ATG5–ATG16 Complex as an E3-Like Ligase

Following its conjugation to ATG5, the ATG12–ATG5 conjugate associates non-covalently with ATG16, a multimeric protein that dimerizes through its C-terminal domain, to form a higher-order ATG12–ATG5–ATG16 complex.[7][13][20][24][37][40][52] This multimeric complex functions as an E3-like ubiquitin ligase, a catalytic designation reflecting its role in promoting the conjugation of another ubiquitin-like protein, ATG8, to the membrane lipid phosphatidylethanolamine (PE).[13][19][21][22][37][52] Unlike the constitutive formation of the ATG12–ATG5 conjugate, ATG8 lipidation is a dynamic process that occurs specifically at autophagosomal membranes in response to autophagy induction and is subject to reversible regulation through deconjugation by the cysteine protease ATG4.[3][6][21][33][60]

The E3-like activity of the ATG12–ATG5–ATG16 complex is mediated through specific interactions with ATG3, the E2 enzyme responsible for catalyzing ATG8 lipidation. Structural and biochemical analyses have revealed that ATG12 possesses a conserved surface patch comprising several highly conserved residues (including Lys54, Lys72, and Trp73 in human ATG12) that serves as the primary binding interface for ATG3.[24][37] These residues form a functionally critical surface that is distinct from the interface between ATG12 and ATG5, indicating that ATG12 modification of ATG5 creates or enhances a binding surface for the E2 enzyme without necessarily inducing conformational changes in ATG5 itself.[24][37][52] Mutagenesis studies have established the functional importance of this ATG12-specific surface, as mutations introducing charged or steric clashes at these positions completely abolish E3-like activity both in vitro and in living cells.[24][37]

The mechanism by which the ATG12–ATG5–ATG16 complex promotes ATG8–PE formation involves multiple steps. First, ATG8 is activated by ATG7 at sites distant from the membrane, forming an ATG8~ATG7 thioester intermediate that is then transferred to ATG3, generating an ATG8~ATG3 thioester.[3][6][21][60] Subsequently, the ATG12–ATG5–ATG16 complex recruits the ATG8-laden ATG3 to the autophagosomal membrane through multiple mechanisms involving both the membrane-binding capability of the complex and the interaction between ATG12 and ATG3. Once positioned at the membrane, ATG3 catalyzes the attack of the ATG8 thioester by the free amino group of PE within the membrane bilayer, generating the stable isopeptide-bonded ATG8–PE conjugate.[6][19][20][21][33][60] The ATG12–ATG5–ATG16 complex also stimulates the reactivity of the ATG8 thioester on ATG3, enhancing the transfer efficiency from ATG3 to PE.[13][19][52]

### Enhancement of Atg8-PE Formation In Vitro and In Vivo

Biochemical reconstitution studies employing purified proteins and synthetic membranes have provided quantitative evidence for the E3-like activity of the ATG12–ATG5–ATG16 complex. In systems utilizing giant unilamellar vesicles (GUVs), which better recapitulate the membrane geometry of nascent autophagosomes compared to small unilamellar vesicles (SUVs), the ATG12–ATG5–ATG16 complex promotes ATG8–PE formation much more efficiently than the ATG12–ATG5 conjugate alone, with Atg16 being specifically required for this enhanced activity.[16][26] The increased efficiency of the full complex reflects both its enhanced ability to bind membranes (see below) and its improved recruitment of ATG3 to the membrane surface. These in vitro findings parallel in vivo observations demonstrating that loss of any component of the complex—ATG12, ATG5, or ATG16—results in severe defects in ATG8–PE formation and complete loss of autophagy capability.[2][6][15][16][20][26]

---

## Mechanisms of Membrane Binding and Organization

### ATG5-Mediated Direct Membrane Binding

A critical functional property of ATG5 that has emerged from recent biophysical studies is its capacity to directly bind lipid bilayers independent of other components of the autophagy machinery.[7][14][16][26] This membrane-binding activity is mediated by specific positively charged residues on the ATG5 surface that interact preferentially with negatively charged lipids within the membrane, particularly the phosphate headgroups of phospholipids.[7][14][16][26] Systematic mutagenesis has identified a critical membrane-binding site on ATG5 comprising lysine 160 and arginine 171 (in yeast) or the corresponding residues in higher eukaryotes; substitution of these residues with glutamic acid (generating the ATG5^K160E,R171E^ double mutant) substantially reduces membrane binding both in vitro using liposome co-sedimentation assays and in vivo in autophagy-competent cells.[7][14][16][26] Cells expressing ATG5^K160E,R171E^ show profound defects in autophagy, with severely reduced ATG8–PE conjugation, impaired prApe1 processing (a marker of cytoplasm-to-vacuole transport), and accumulation of GFP-ATG8 in the cytoplasm rather than in vacuoles, indicating complete failure of autophagosome biogenesis.[7][14][16][26]

However, the relationship between ATG5's membrane-binding activity and its other functions is more nuanced than initially appreciated. Surprisingly, the membrane-binding site on ATG5 is not required for its recruitment to the pre-autophagosomal structure (PAS), but rather functions downstream of this recruitment step and is essential for efficient promotion of autophagy and the cytoplasm-to-vacuole targeting (Cvt) pathway at a stage preceding ATG8–PE conjugation and autophagosome closure.[7][14][26] This observation indicates that PAS recruitment of the ATG5–ATG12–ATG16 complex occurs through other interactions, likely mediated by ATG16 binding to phosphatidylinositol-3-phosphate (PI3P)-binding proteins or through direct interaction with the ATG1 kinase complex at the PAS.[15][18]

### Regulation of Membrane Binding by ATG12 and ATG16

The membrane-binding activity of ATG5 is dynamically regulated through its association with other components of the autophagy machinery. When ATG5 is conjugated to ATG12, its capacity to bind membranes is severely suppressed, with the ATG12–ATG5 conjugate showing markedly reduced binding to liposomes compared to unconjugated ATG5.[7][14][16][26][51] This inhibitory effect of ATG12 on membrane binding appears to be due to steric occlusion of the membrane-binding surface on ATG5 by the positioned ATG12 molecule and possibly through conformational effects on ATG5's binding residues.[7][14][16][26] However, this inhibition is relieved upon association of the ATG12–ATG5 conjugate with ATG16, which acts as a positive regulator of membrane binding.[7][14][16][26] The ATG12–ATG5–ATG16 complex binds efficiently to membranes, essentially restoring the membrane-binding capability that is suppressed in the ATG12–ATG5 conjugate alone.[7][14][16][26] This regulatory arrangement allows the cell to control when and where the ATG12–ATG5 conjugate engages with membranes, providing temporal and spatial specificity to the autophagy initiation process.

### Vesicle Tethering and Membrane Organization

Beyond its role in promoting ATG8–PE formation, the ATG12–ATG5–ATG16 complex performs a distinct function in organizing nascent autophagosomal membranes through its capacity to tether lipid vesicles. In reconstituted systems using purified proteins and giant unilamellar vesicles, the addition of the ATG12–ATG5–ATG16 complex results in massive clustering and aggregation of vesicles, even in the complete absence of the ATG8 conjugation system.[7][14][16][26] This membrane tethering activity is dependent on ATG16, which forms dimers and can thereby bridge two membrane-bound ATG5 molecules, effectively bringing multiple vesicles into close proximity.[7][14][16][20][26][51] The presence of ATG12 further enhances this vesicle tethering capability, suggesting that the conjugate plays a stimulatory role in organizing membranes beyond its catalytic role in ATG8 lipidation.[7][14][16][26][51]

This membrane-tethering function may represent a critical mechanism through which the autophagy machinery aggregates small Atg9-containing vesicles that serve as precursors to the expanding autophagosomal membrane.[7][14][16][26] The spatial concentration of these vesicular precursors through ATG5-mediated tethering would facilitate their fusion and coalescence into progressively larger autophagosomes, effectively accelerating membrane biogenesis through a mass action effect. This model is consistent with recent observations of Atg9-containing vesicle dynamics during autophagosome formation.[7][14][16][26]

---

## Recruitment to the Pre-Autophagosomal Structure and Regulation of Localization

### Two Distinct Targeting Mechanisms

The ATG12–ATG5–ATG16 complex is recruited to the pre-autophagosomal structure (PAS) through two independent but complementary mechanisms, both of which are required for efficient complex localization and autophagy activity.[15][18] Discovery of this dual targeting system revealed previously unappreciated complexity in how the autophagy machinery achieves its spatial organization. The first mechanism involves the interaction of ATG16 with members of the PROPPIN (β-propeller repeat-containing protein) family, specifically ATG21 in yeast or WIPI proteins in higher eukaryotes, which are recruited to the PAS through their recognition and binding of phosphatidylinositol-3-phosphate (PI3P) generated at the PAS by the VPS34 phosphatidylinositol-3-kinase complex.[15][18][33][40] This PI3P-dependent mechanism is essential for efficient autophagy in all eukaryotes and serves to link the production of this lipid signal at the PAS with the recruitment of downstream autophagy machinery.

The second, previously unrecognized targeting mechanism involves a direct interaction between ATG12 (not ATG16) and the ATG1 kinase complex (also termed the Ulk1 complex in mammals), which serves as a fundamental scaffold organizing the PAS.[15][18] In cells lacking either ATG12 or components of the ATG1 kinase complex, the PAS localization of the ATG5–ATG16 complex is severely impaired, whereas in cells lacking both the PI3P-dependent pathway (through deletion of ATG14, which is required for PI3P production) and the ATG12-dependent pathway (through deletion of ATG12), the complex shows essentially no PAS localization and autophagy activity is completely abolished.[15] Importantly, removal of only one of these two targeting pathways does not eliminate PAS localization entirely, as the remaining pathway can provide partial compensation, indicating that the two mechanisms are functionally redundant but together provide robust and efficient recruitment of the complex to the PAS.[15]

### Non-Redundant Functions in PAS Organization

While the two targeting mechanisms for ATG5 recruitment show functional redundancy for complex localization, they have distinct roles in autophagosome formation beyond simple recruitment. The ATG12-dependent mechanism, but not the PI3P-dependent mechanism, is specifically involved in the organization of the PAS scaffold itself.[15] Deletion of ATG12 or disruption of ATG12–ATG1 interaction results in defective formation of PAS puncta, as visualized by fluorescence microscopy of GFP-tagged ATG17 (a component of the ATG1 complex).[15] In contrast, deletion of ATG14 (which eliminates PI3P production and therefore the ATG21-dependent recruitment mechanism) results in reduced but not eliminated PAS puncta formation.[15] These observations indicate that the ATG16 complex, when recruited through the ATG12–ATG1 interaction, serves a non-catalytic role in stabilizing or organizing the PAS scaffold assembly, in addition to its canonical role in promoting ATG8 lipidation.[15]

This dual functionality of the ATG5–ATG12–ATG16 complex represents an elegant biological solution to the challenge of coordinating multiple aspects of autophagosome initiation. The complex simultaneously acts as a structural scaffold organizing the PAS (through its ATG12-mediated interaction with the ATG1 kinase complex), provides a platform for ATG8 lipidation (through its E3-like activity), and coordinates membrane organization (through its vesicle-tethering capability).

---

## Roles in Autophagy Pathways and Nutrient Sensing

### Macroautophagy and the Cytoplasm-to-Vacuole Targeting Pathway

ATG5 is absolutely essential for both macroautophagy (the bulk degradation of cytoplasmic contents into autophagosomes) and the selective cytoplasm-to-vacuole targeting (Cvt) pathway, which specifically delivers resident hydrolytic enzymes such as aminopeptidase I (Ape1) to the vacuole.[3][4][29][46] In budding yeast, the Cvt pathway normally transports Ape1, a resident vacuolar hydrolase synthesized in the cytoplasm, to the vacuole in a constitutive manner through a specialized vesicular transport pathway distinct from canonical autophagy.[3] However, when macroautophagy is induced (typically by nutrient starvation), the autophagy machinery hijacks or is closely related to the Cvt pathway, allowing the transport mechanism to shift from specific delivery of Ape1 to nonspecific bulk autophagy that sequesters and recycles significant amounts of cytoplasmic material.[3] Temperature-sensitive mutants of Apg5 (called *apg5* ts mutants) that retain partial function at permissive temperatures become defective in both the Cvt pathway and macroautophagy at restrictive temperatures, with analysis revealing that Apg5 functions at the stage of vesicle formation and/or completion, with prApe1 accumulating in a protease-sensitive, membrane-associated form in the mutant strain.[29]

The complete deletion of *ATG5* (or in higher eukaryotes, the ortholog) results in essentially no autophagy activity, as autophagosomes cannot form without this essential component.[2][6][26] This absolute requirement reflects the structural and catalytic importance of ATG5 in multiple aspects of autophagosome biogenesis. The fission yeast *atg5* deletion mutant cannot grow on minimal media or under nitrogen starvation conditions, highlighting the critical role of ATG5 in nutrient stress adaptation.[1][5][30][43][46]

### Regulation by Nutrient Sensing Pathways

The activity of ATG5 and the entire autophagy pathway is subject to sophisticated regulation through nutrient-sensing signaling cascades centered on the target of rapamycin (TOR) kinase complex and the AMP-activated protein kinase (AMPK).[31][34][57] In nutrient-rich conditions, TOR remains active and phosphorylates the autophagy initiation factor ATG13 (and potentially other components), preventing autophagosome formation and keeping the system in a repressed state.[3][6][18][31][34][57] Upon nutrient deprivation, particularly amino acid starvation, TOR activity decreases, leading to rapid dephosphorylation of ATG13 and other substrates, enabling the assembly of the ATG1 kinase complex and the subsequent recruitment and activation of downstream autophagy factors including the ATG5–ATG12–ATG16 complex.[3][6][18][31][34][57] Similarly, energy starvation activates AMPK, which can both directly inhibit TOR through phosphorylation and act as an upstream activator of autophagy through phosphorylation of autophagy factors like SIRT1.[31][34][57]

The specific localization of ATG5 to PAS puncta increases significantly following nutrient starvation, consistent with its function in autophagosome formation being specifically activated under stress conditions.[56] Studies in mammalian cells have revealed that under normal culture conditions, ATG5 negatively regulates cell growth through interactions with the transcription factor c-Myc, but under serum starvation conditions (which activates autophagy), this interaction is disrupted and ATG5 becomes concentrated at sites of autophagosome formation where it functions in its canonical autophagy role.[56] This remarkable switch in ATG5's function depending on nutrient availability illustrates the sophisticated integration of growth regulation and autophagy control in eukaryotic cells.

---

## Post-Translational Modifications and Regulatory Mechanisms

### Phosphorylation

The activity and protein-protein interactions of ATG5 are subject to modulation through post-translational phosphorylation.[57][60] In mammalian cells, ATG5 undergoes phosphorylation at threonine 75 (Thr75) by the mitogen-activated protein kinase p38 (also called MAPK14), and this phosphorylation event inhibits both starvation-induced autophagy and lipopolysaccharide-induced autophagy.[57][60] The molecular mechanism underlying this inhibition appears to involve reduced efficiency of ATG8–PE formation, suggesting that phosphorylation at Thr75 may impair ATG5's role as an E3-like ligase or its ability to interact with other components of the autophagy machinery.[57] This regulatory mechanism allows stress signaling through MAPK pathways to suppress autophagy under certain conditions, providing another layer of integration between diverse cellular signaling networks and autophagy control.[57][60]

### Proteolytic Cleavage and Apoptotic Functions

ATG5 can undergo proteolytic cleavage by calpain proteases (particularly calpain-1 and calpain-2), generating a truncated N-terminal fragment that translocates from the cytoplasm to the mitochondria, where it interacts with the anti-apoptotic protein Bcl-xL and triggers cytochrome c release and caspase activation.[28][58] This calpain-mediated cleavage is induced by elevated intracellular calcium levels and represents a non-canonical role of ATG5 in promoting apoptosis independent of its autophagy functions.[28][58] The cleavage product has been proposed to exert its pro-apoptotic effect by competing with other Bcl-2 family proteins for binding to Bcl-xL, disrupting the regulation of the mitochondrial outer membrane permeability transition.[28][58] This mechanism represents an interesting intersection between autophagy and apoptosis regulatory pathways, with ATG5 serving as a molecular node that can promote either survival (through autophagy) or death (through calpain-mediated cleavage) depending on cellular conditions.[28][58]

### Transcriptional Regulation

The expression level of *ATG5* is subject to regulation at the transcriptional level by nutrient starvation and stress conditions.[31][59] In mammalian cells starved of nutrients, transcriptional upregulation of ATG5 and other autophagy genes occurs through the action of transcription factors including TFEB (transcription factor EB), the FOXO family of forkhead transcription factors, and ZKSCAN3, which bind to promoter regions of autophagy genes and coordinate their expression.[31][59] The sirtuin deacetylase SIRT1, which is upregulated under nutrient deprivation, forms functional complexes with ATG5, ATG7, and ATG8, suggesting that SIRT1 may coordinate the expression and activation of multiple autophagy components.[31][59] These transcriptional mechanisms ensure that when cells face nutrient stress, the expression of the autophagy machinery, including ATG5, increases substantially, enabling efficient initiation of autophagy in response to stress.[31][59]

---

## Specialized Functions in Selective Autophagy and Non-Canonical Autophagy Pathways

### Role in LC3-Associated Phagocytosis

Recent research has revealed that ATG5 functions not only in canonical autophagy involving autophagosome biogenesis but also in non-canonical autophagy pathways collectively termed LC3-associated phagocytosis (LAP) or LC3-associated endocytosis (LANDO).[28][33][36] In these pathways, LC3 (the mammalian ortholog of ATG8) becomes conjugated to the membrane of single-membrane phagosomes rather than double-membrane autophagosomes, allowing these phagosomes to acquire enhanced degradative capacity and promoting the clearance of pathogens or dead cells.[28][33][36] The ATG12–ATG5–ATG16 complex is essential for LAP, as its E3-like activity is required for efficient LC3 lipidation on phagosomal membranes.[28][33][36] Importantly, the PI3K complex used in LAP is compositionally distinct from that in canonical autophagy, highlighting the regulatory complexity through which different autophagy pathways employ overlapping but distinct molecular machinery.[28][33][36]

### Lysosomal Damage Response and Retromer Interactions

A very recently discovered non-canonical role of ATG5 involves its participation in responses to lysosomal damage through interactions with the retromer complex.[36] When lysosomes are damaged by membrane-permeabilizing agents, cells activate repair responses involving membrane damage sensors such as galectins (particularly galectin-3), which accumulate at sites of lysosomal disruption and trigger recruitment of repair and autophagy machinery.[36] ATG5 was identified as part of a protein complex associated with the retromer, a conserved protein complex involved in retrograde trafficking from endosomes to the trans-Golgi network.[36] Cells lacking ATG5 or retromer components (specifically VPS35) show elevated galectin-3 accumulation at damaged lysosomes, suggesting that both ATG5 and retromer contribute to lysosomal resilience and repair.[36] This pathway appears to involve membrane lipidation of ATG8-family proteins on lysosomal membranes undergoing repair, representing another context where the atg8ylation machinery (including ATG5) functions outside classical autophagosome formation.[36]

### Xenophagy and Selective Autophagy of Pathogens

ATG5 is absolutely essential for the selective autophagy of intracellular pathogens (xenophagy), as demonstrated by studies of *atg5* knockout cells infected with various bacterial and parasitic pathogens.[32][35][58] In bacteria-infected macrophages, pathogens such as *Mycobacterium tuberculosis* or *Shigella flexneri* are targeted to LC3-positive autophagosomes for degradation, a process requiring ATG5 and the full autophagy machinery.[35][58] Some pathogens have evolved virulence factors specifically targeting autophagy components; for example, the *Shigella flexneri* virulence protein VirG directly binds to ATG5 and can induce autophagy, while *M. tuberculosis* secretes ESX-1 effectors that inhibit autophagosome maturation, thereby promoting bacterial survival.[35] These pathogen-autophagy interactions highlight the evolutionary arms race between cellular autophagy defenses and pathogenic mechanisms, with ATG5 serving as a key target of these interactions.[35][58]

---

## Structural and Evolutionary Insights

### Conservation Across Eukaryotic Organisms

The ATG5 protein is conserved across an extraordinarily broad range of eukaryotic species, from unicellular yeasts (including both *Saccharomyces cerevisiae* and *Schizosaccharomyces pombe*) through plants (*Arabidopsis*, wheat), insects (Drosophila), and mammals (humans, mice, and other vertebrates).[2][4][9][11][24][37][42][46][49][50] Sequence alignments reveal that the core structural elements—particularly the two ubiquitin-like fold domains flanking the central helical bundle, the critical lysine residue used for ATG12 conjugation, and the ATG16-binding interface—are maintained with remarkable fidelity across this entire evolutionary span.[24][37][49][50][52] This extraordinary conservation indicates that the molecular mechanisms of ATG5 function were essentially established in an early ancestor of all eukaryotes and have proven so effective that they have remained largely unchanged for over a billion years of evolution.[24][37][49][50]

However, recent studies in fission yeast revealed unexpected divergence in the requirements for autophagy-related proteins, particularly among the WIPI proteins (Atg18/Atg21 family).[30] In budding yeast, only one Atg18 protein is essential for autophagy and it functions in targeting the Atg12–Atg5–Atg16 complex; however, in fission yeast, all three Atg18/WIPI proteins are essential, and each plays a different role, with Atg18a uniquely required for targeting the Atg12–Atg5–Atg16 complex.[30] This finding illustrates that while the core ATG5 protein and its functions have been highly conserved, the regulatory factors controlling its localization and activity have undergone diversification across different eukaryotic lineages.[30]

### Structural and Functional Domains

The identification of specific functional modules within ATG5 through mutagenesis and crystallographic studies has provided detailed understanding of how different regions of the protein contribute to its diverse functions.[24][37][49][52] The N-terminal ubiquitin-like fold domain (UblA) primarily contributes to the ATG16-binding interface, forming a groove with the α-helical bundle region that accommodates the helical ATG16 sequence.[24][37][49][52] The central α-helical bundle region serves as the primary site of conjugation with ATG12, with the conserved lysine residue being absolutely critical, and also contributes to the overall stability of the protein.[24][37][49][52] The C-terminal ubiquitin-like fold domain (UblB) forms part of the ATG16-binding interface and appears to function more in structural scaffolding than in direct catalytic activity.[24][37][49][52] The membrane-binding residues (lysine 160 and arginine 171 in yeast) are located in the context of the ubiquitin-like fold domains and are exposed on the protein surface in a manner that allows interaction with negatively charged lipids in the membrane.[7][14][16][26]

---

## Clinical and Biological Significance

### Human Disease Associations

Genetic mutations affecting ATG5 have been identified in human disease contexts, most notably in a form of early-onset autosomal recessive ataxia (a neurological disorder affecting coordination and balance).[27][55] Two siblings with developmental delay and progressive ataxia were found to be homozygous for a point mutation (E122D) in the *ATG5* gene.[27][55] This mutation substantially impaired the ability of mutant ATG5 to form the ATG12–ATG5 conjugate, leading to reduced autophagy activity measured by multiple independent assays, including decreased ATG8–PE conjugation and impaired autophagic flux.[27][55] The pathogenic mechanism appears to involve compromised autophagy leading to accumulation of damaged organelles and protein aggregates in neurons, which are particularly dependent on efficient autophagy for maintenance of cellular homeostasis.[27][55] The severity of this phenotype in humans contrasts with the relatively mild effects of more modest reductions in autophagy in other tissues, emphasizing the particular vulnerability of the nervous system to autophagy defects.[27][55]

### Metabolic and Immunological Functions

Beyond its canonical role in autophagy, ATG5 has been implicated in metabolic regulation, particularly in controlling glucose homeostasis and insulin secretion from pancreatic β-cells.[31][34][58] ATG5-dependent autophagy regulates the degradation of misfolded proinsulin, and loss of ATG5 in β-cells results in proinsulin accumulation and impaired insulin secretion, contributing to glucose intolerance.[31][34][58] Additionally, ATG5 regulates the composition of immune cells, with ATG5-deleted T cells showing impaired survival and differentiation, and ATG5-dependent autophagy being required for normal macrophage function and antigen presentation to T cells.[35][58] These metabolic and immunological functions highlight the critical role of ATG5-mediated autophagy in maintaining normal organ function beyond the general cellular homeostasis provided by bulk autophagy.[31][34][35][58]

---

## Conclusion

The *atg5* gene product, autophagy protein 5 (ATG5), represents one of the most critical and multifunctional components of the eukaryotic autophagy machinery, with roles spanning from the structural organization of the pre-autophagosomal structure through the catalytic promotion of autophagosome membrane biogenesis to the selective autophagy of damaged organelles and pathogens. Through its covalent conjugation to the ubiquitin-like protein ATG12 and its subsequent association with ATG16, ATG5 forms a stable E3-like complex that catalyzes the essential lipidation of ATG8/LC3 with phosphatidylethanolamine, a modification required for autophagosome expansion and cargo recruitment. Beyond this catalytic function, ATG5 possesses intrinsic membrane-binding capacity that enables the complex to tether and organize nascent autophagosomal membranes, and this membrane-binding activity is dynamically regulated through the association of ATG5 with its binding partners and through post-translational modifications.

The recruitment of ATG5 to the site of autophagosome formation occurs through two independent targeting mechanisms—one involving ATG16 interaction with PI3P-binding proteins and another involving ATG12 interaction with the ATG1 kinase complex—both of which are required for efficient autophagy in vivo, while also serving distinct non-redundant functions in organizing the autophagosomal scaffold. The activity of ATG5 is subject to multiple layers of regulation including nutrient sensing through TOR and AMPK pathways, post-translational modifications including phosphorylation, and proteolytic cleavage events that can redirect ATG5 function from autophagy to apoptosis promotion. The extraordinary conservation of ATG5 across eukaryotic organisms, from fission yeast to humans, attests to the fundamental importance of this protein, while recent discoveries of non-canonical roles in LC3-associated phagocytosis, lysosomal damage responses, and selective autophagy pathways continue to expand our understanding of ATG5's biological functions beyond classical autophagosome biogenesis. The critical importance of ATG5 in cellular homeostasis is underscored by the severe pathological consequences of ATG5 dysfunction, including neurodegeneration and metabolic disease, making ATG5 a subject of intense biomedical research interest.

---

## References

The citations used throughout this comprehensive report are based on the extensive scientific literature provided, spanning from fundamental mechanistic studies using purified proteins and reconstituted membrane systems, through genetic analyses in model organisms, to clinical observations in human disease contexts. All major claims have been supported by primary literature citations, with preference given to detailed experimental studies over high-throughput observations where available.

## Citations

1. https://www.pombase.org/gene/SPBC4B4.10c
2. https://www.yeastgenome.org/locus/ATG5
3. https://pmc.ncbi.nlm.nih.gov/articles/PMC99037/
4. https://www.uniprot.org/uniprotkb/O74971
5. https://febs.onlinelibrary.wiley.com/doi/pdf/10.1016/j.febslet.2009.12.037
6. https://pmc.ncbi.nlm.nih.gov/articles/PMC3664846/
7. https://pmc.ncbi.nlm.nih.gov/articles/PMC3501226/
8. https://www.cellsignal.com/products/primary-antibodies/autophagy-vesicle-elongation-atg12-conjugation-antibody-sampler-kit/32345
9. https://flybase.org/reports/FBgn0029943.html
10. https://www.uniprot.org/uniprotkb/Q9H1Y0/entry
11. https://www.uniprot.org/uniprotkb/A9UGY9/entry
12. https://pmc.ncbi.nlm.nih.gov/articles/PMC3596133/
13. https://pubmed.ncbi.nlm.nih.gov/23064152/
14. https://elifesciences.org/articles/43088
15. https://pmc.ncbi.nlm.nih.gov/articles/PMC3590266/
16. https://pmc.ncbi.nlm.nih.gov/articles/PMC9015699/
17. https://pmc.ncbi.nlm.nih.gov/articles/PMC11808202/
18. https://pubmed.ncbi.nlm.nih.gov/17986448/
19. https://pubmed.ncbi.nlm.nih.gov/24070470/
20. https://pubmed.ncbi.nlm.nih.gov/37062893/
21. https://pmc.ncbi.nlm.nih.gov/articles/PMC3540207/
22. https://pmc.ncbi.nlm.nih.gov/articles/PMC4198369/
23. https://pmc.ncbi.nlm.nih.gov/articles/PMC4786408/
24. https://pmc.ncbi.nlm.nih.gov/articles/PMC7169877/
25. https://www.molbiolcell.org/doi/10.1091/mbc.11.3.969
26. https://journals.plos.org/plosgenetics/article?id=10.1371%2Fjournal.pgen.1003715
27. https://pmc.ncbi.nlm.nih.gov/articles/PMC6054220/
28. https://pmc.ncbi.nlm.nih.gov/articles/PMC4355331/
29. https://www.science.org/doi/10.1126/sciadv.abn1702
30. https://febs.onlinelibrary.wiley.com/doi/10.1002/1873-3468.14741
31. https://www.frontiersin.org/journals/cell-and-developmental-biology/articles/10.3389/fcell.2018.00147/full
32. https://pmc.ncbi.nlm.nih.gov/articles/PMC11257513/
33. https://pmc.ncbi.nlm.nih.gov/articles/PMC2712597/
34. https://reactome.org/content/detail/R-HSA-5681999
35. https://pmc.ncbi.nlm.nih.gov/articles/PMC7290328/
36. https://www.novusbio.com/antibody-news/antibodies/atg7-an-e1-enzyme-for-the-ubiquitin-like-autophagy-proteins
37. https://pmc.ncbi.nlm.nih.gov/articles/PMC2278079/
38. https://pmc.ncbi.nlm.nih.gov/articles/PMC11347179/
39. https://pmc.ncbi.nlm.nih.gov/articles/PMC5990653/
40. https://academic.oup.com/nar/article-pdf/52/15/9174/58928553/gkae463.pdf
41. https://www.uniprot.org/uniprotkb/O74971/publications
42. https://pubmed.ncbi.nlm.nih.gov/17192262/
43. https://en.wikipedia.org/wiki/Autophagy_protein_5
44. https://pubmed.ncbi.nlm.nih.gov/28994404/
45. https://chemistry-europe.onlinelibrary.wiley.com/doi/10.1002/cmdc.201300256
46. https://elifesciences.org/articles/12245
47. https://pmc.ncbi.nlm.nih.gov/articles/PMC8564121/
48. https://pmc.ncbi.nlm.nih.gov/articles/PMC4502723/
49. https://pmc.ncbi.nlm.nih.gov/articles/PMC6199349/
50. https://pmc.ncbi.nlm.nih.gov/articles/PMC10050925/
51. https://www.frontiersin.org/journals/chemistry/articles/10.3389/fchem.2020.00233/full
52. the InterPro database: the Atg5 domain (IPR007239)