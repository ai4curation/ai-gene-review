---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-22T16:36:19.050070'
end_time: '2026-01-22T16:51:24.258090'
duration_seconds: 905.21
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: CLPS
  gene_symbol: CLPS
  uniprot_accession: P04118
  protein_description: 'RecName: Full=Colipase {ECO:0000305}; Flags: Precursor;'
  gene_info: Name=CLPS {ECO:0000312|HGNC:HGNC:2085};
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the colipase family. {ECO:0000255|PROSITE-
  protein_domains: CLPS_chr. (IPR047576); Colipase. (IPR001981); Colipase_C. (IPR017914);
    Colipase_CS. (IPR017915); Colipase_N. (IPR017913)
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
- **UniProt Accession:** P04118
- **Protein Description:** RecName: Full=Colipase {ECO:0000305}; Flags: Precursor;
- **Gene Information:** Name=CLPS {ECO:0000312|HGNC:HGNC:2085};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the colipase family. {ECO:0000255|PROSITE-
- **Key Domains:** CLPS_chr. (IPR047576); Colipase. (IPR001981); Colipase_C. (IPR017914); Colipase_CS. (IPR017915); Colipase_N. (IPR017913)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "CLPS" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'CLPS' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **CLPS** (gene ID: CLPS, UniProt: P04118) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Human Colipase (CLPS): A Comprehensive Review

## Introduction and Summary

Colipase (gene symbol: CLPS; UniProt: P04118) is a small, essential protein cofactor that enables the efficient hydrolysis of dietary triglycerides by pancreatic lipase in the human duodenum. The protein is encoded by the CLPS gene located on chromosome 6p21.31 and is expressed exclusively in the pancreas [sims-1992-gene-structure-abstract]. Colipase belongs to a family of cysteine-rich proteins characterized by a distinctive structural fold stabilized by five disulfide bonds [egloff-1995-crystallographic-abstract].

The primary biological function of colipase is to counteract the inhibitory effect of bile salts on pancreatic triglyceride lipase (PTL), allowing the enzyme to remain anchored at the lipid-water interface where it catalyzes fat digestion [borgstrom-1975-interactions-abstract]. Without colipase, bile salts would wash lipase away from its substrate, effectively halting triglyceride hydrolysis in the physiological environment of the small intestine [chapus-1988-minireview-abstract]. The colipase-PTL system accounts for approximately 60% of dietary triglyceride hydrolysis in adult humans, making it essential for normal fat absorption and nutrition [lowe-1997-structure-function-abstract].

Colipase is secreted from pancreatic acinar cells as an inactive precursor, procolipase, which is activated in the intestinal lumen by trypsin-mediated cleavage. This activation releases a five-amino-acid N-terminal peptide called enterostatin, which has been shown to function as a satiety signal that specifically suppresses dietary fat intake [okada-1991-enterostatin-fat-intake-abstract]. Thus, the CLPS gene product has dual functions: the mature colipase enables fat digestion while the enterostatin peptide may provide feedback regulation of fat consumption.

## Biochemical Function and Mechanism

### The Problem: Bile Salt Inhibition of Lipase

Dietary fat digestion in the small intestine presents a unique biochemical challenge. Pancreatic lipase, the primary enzyme responsible for hydrolyzing triglycerides into absorbable monoglycerides and free fatty acids, must function at lipid-water interfaces in the presence of bile salts [lowe-1997-structure-function-abstract]. Bile salts, secreted from the liver and concentrated in the gallbladder, are amphipathic molecules essential for emulsifying dietary fats into micelles that increase the surface area available for enzymatic attack.

However, at concentrations above their critical micellar concentration (CMC), bile salts strongly inhibit pancreatic lipase activity [borgstrom-1975-interactions-abstract]. This inhibition occurs through a mechanism whereby bile salts displace lipase from hydrophobic substrate interfaces. The observation of this paradox—that bile salts are both necessary for fat digestion yet inhibitory to the key digestive enzyme—led to the discovery of colipase in 1963 by the laboratory of Professor Borgström in Lund, Sweden [chapus-1988-minireview-abstract].

### Colipase as a Cofactor

Colipase functions by providing a high-affinity binding site for lipase at the bile salt-covered lipid interface [borgstrom-1975-interactions-abstract]. The protein binds to the non-catalytic C-terminal domain of pancreatic lipase with a 1:1 stoichiometry, forming a stable complex [vantilbeurgh-1999-colipase-structure-abstract]. This interaction stabilizes lipase in an active conformation and considerably increases the overall hydrophobic binding site available for substrate interaction [egloff-1995-crystallographic-abstract].

The mechanism of colipase action involves multiple effects. First, colipase anchors the lipase to the substrate interface, counteracting the displacement effect of bile salts. Second, colipase stabilizes the "open" conformation of the lipase lid domain, a 23-amino-acid surface loop that must move away from the active site to allow substrate access [yang-2000-open-lid-abstract]. Third, colipase creates a more favorable microenvironment at the interface by packing more efficiently with substrates and products of lipolysis than with phosphatidylcholine, thereby concentrating reactants near the enzyme [vantilbeurgh-1999-colipase-structure-abstract].

At physiological pH (6-7), colipase fully restores lipase activity that would otherwise be completely inhibited by bile salts, and actually shifts the pH optimum of the enzyme from 8-9 (in the absence of bile salts) to 6-7 (the normal duodenal environment) [borgstrom-1975-interactions-abstract].

### Substrate Specificity

Colipase enables pancreatic lipase to efficiently hydrolyze dietary triglycerides of varying chain lengths. The lipase preferentially cleaves ester bonds at the sn-1 and sn-3 positions of triglycerides, producing 2-monoacylglycerol and free fatty acids as the primary products [lowe-1997-structure-function-abstract]. The colipase-lipase system operates on long-chain triglycerides (the predominant form in the diet), medium-chain triglycerides, and short-chain triglycerides, though the efficiency varies somewhat with chain length [dsilva-2007-polymorphism-abstract].

## Structural Biology

### Protein Structure

Colipase is a small protein of approximately 10 kDa (90 amino acids in mature form) with a distinctive three-dimensional structure that has been determined by both X-ray crystallography and NMR spectroscopy [egloff-1995-crystallographic-abstract][vantilbeurgh-1999-colipase-structure-abstract][breg-1995-procolipase-NMR-abstract]. The protein adopts a flat, finger-like shape with dimensions of approximately 25 × 30 × 35 Å. Secondary structure analysis reveals that colipase contains approximately 5% alpha-helix (residues 39-44), 25% beta-sheet organized into three separate regions (residues 7-11, 49-57, and 77-85), and eight beta-turns comprising approximately 32% of the polypeptide [breg-1995-procolipase-NMR-abstract]. Importantly, the solution structure determined by NMR is nearly identical to the crystal structure, confirming that the crystallographic conformation represents the native state of the protein [breg-1995-procolipase-NMR-abstract].

The structure is stabilized primarily by an extended network of five disulfide bonds connecting ten conserved cysteine residues at positions 34-45, 40-56, 44-78, 66-86, and 80-104 [egloff-1995-crystallographic-abstract]. This disulfide network runs throughout the molecule, reticulating four protruding finger-like loops. The surface of colipase is divided into a hydrophilic region that interacts with lipase and a more hydrophobic region formed by the tips of the finger loops that contacts lipid interfaces [egloff-1995-crystallographic-abstract].

### Lipase-Colipase Complex

The crystal structure of the pancreatic lipase-colipase complex has been solved at high resolution (2.46 Å), providing detailed insight into their interaction [egloff-1995-246A-structure-abstract]. Pancreatic lipase itself is a 50 kDa single-chain glycoprotein of 449 amino acids consisting of two structural domains: an N-terminal domain (336 residues) containing the catalytic site, and a C-terminal domain (113 residues) devoted to colipase binding [lowe-1997-structure-function-abstract].

The N-terminal catalytic domain has a typical alpha/beta hydrolase fold topology and contains the catalytic triad of Ser153, His264, and Asp177 [lowe-1997-structure-function-abstract]. The C-terminal domain has a beta-sheet sandwich topology and provides the primary binding site for colipase [vantilbeurgh-1999-colipase-structure-abstract].

The interaction between colipase and the C-terminal domain of lipase is stabilized by eight hydrogen bonds and approximately 80 van der Waals contacts [egloff-1995-crystallographic-abstract]. However, when lipase binds to a lipid interface and the lid domain opens, three additional hydrogen bonds and approximately 28 more van der Waals contacts are formed between colipase and the newly positioned lid [egloff-1995-crystallographic-abstract]. This explains the higher apparent affinity of the lipase-colipase complex observed in the presence of lipid/water interfaces.

### The Lid Domain and Interfacial Activation

A key structural feature of pancreatic lipase is the "lid domain," a 23-amino-acid surface loop that overlies the active site in the closed (inactive) conformation [yang-2000-open-lid-abstract]. Upon contact with lipid interfaces or amphiphilic molecules, this lid undergoes a dramatic conformational change, moving away from the active site to create access for substrate binding [lowe-1997-structure-function-abstract].

Colipase plays a critical role in stabilizing this open conformation. In the active complex, colipase is held in a grip between the N-terminal and C-terminal domains of lipase, with interactions extending to the repositioned lid [vantilbeurgh-1999-colipase-structure-abstract]. Studies using lid-swap chimeras between different lipases demonstrated that specific residues in the lid (particularly Arg257 and Asp258) are essential for proper colipase interaction and enzyme function [yang-2000-open-lid-abstract].

### Bile Salt Binding Site

High-resolution NMR studies have characterized the bile salt binding properties of colipase [wieloch-1979-NMR-bile-salt-abstract]. These experiments revealed that all three tyrosine residues and one histidine residue in porcine colipase are affected by taurodeoxycholate (bile salt) binding, indicating that the bile salt molecules bind near these residues in a hydrophobic region on the colipase surface [wieloch-1979-NMR-bile-salt-abstract]. This binding interaction is essential for colipase's ability to function at bile salt-covered lipid interfaces.

### Evolutionary Conservation and Structural Homology

The colipase fold is highly conserved and has been identified in a diverse range of proteins beyond pancreatic colipases [vantilbeurgh-1999-colipase-structure-abstract]. A particularly interesting structural analogy exists between colipase and a domain in the Dickkopf (Dkk) family of Wnt signaling antagonists. The C-terminal cysteine-rich domain of Dickkopf proteins shares the same disulfide-bonding pattern and overall fold as colipase, suggesting an ancient evolutionary relationship [vantilbeurgh-1999-colipase-structure-abstract]. Whether this structural similarity implies a conserved function in lipid interaction remains to be clarified.

The colipase fold has also been identified in several animal toxins, including mamba intestinal toxin 1 (MIT1) from the black mamba snake, which shows remarkably high structural homology with colipase (RMSD of 1.3 Å for more than 60 residues) despite limited sequence similarity [vantilbeurgh-1999-colipase-structure-abstract]. MIT1 and colipase share identical disulfide patterns and similar secondary structure motifs, representing a striking example of structural conservation across functionally diverse proteins. Additionally, related structural folds have been found in funnel web spider toxins.

## Cellular Localization and Secretion

### Gene Structure and Expression

The human CLPS gene is located on chromosome 6p21.31, spanning approximately 2.3 kb of genomic DNA organized into three exons [sims-1992-gene-structure-abstract][davis-1991-chromosome-mapping-abstract]. The 5'-flanking region contains characteristic regulatory elements including a TATA box, a GC box, and a 28-bp region with homology to the rat pancreatic-specific enhancer [sims-1992-gene-structure-abstract]. This enhancer region binds specific nuclear factors and directs tissue-specific expression exclusively in pancreatic acinar cells, as demonstrated by transfection experiments where the promoter was active in AR42-J rat pancreatic acinar cells but inactive in hepatic (HEPG2), muscle (C2C12), and kidney (COS-1) cell lines [sims-1992-gene-structure-abstract].

### Biosynthesis and Secretion

Colipase is synthesized in pancreatic acinar cells as a precursor protein (preprocolipase) of 112 amino acids [lowe-1997-structure-function-abstract]. The initial translation product includes a 17-residue signal peptide that directs the protein into the secretory pathway. Following signal peptide cleavage, the resulting procolipase (95 amino acids) is packaged into zymogen granules along with other digestive enzymes including pancreatic lipase, trypsinogen, and various proteases.

The ratio of procolipase to pancreatic lipase in pancreatic secretions is approximately 1:1, ensuring stoichiometric availability of the cofactor [lowe-1997-structure-function-abstract]. Upon stimulation by cholecystokinin (CCK)—released from intestinal I-cells in response to dietary fat—or by vagal acetylcholine release, pancreatic acinar cells undergo calcium-mediated exocytosis of zymogen granule contents into the pancreatic ductal system.

### Activation in the Intestinal Lumen

Procolipase remains in its inactive precursor form until reaching the duodenum, where it is activated by trypsin-catalyzed cleavage of a five-amino-acid N-terminal peptide (the activation peptide) [okada-1991-enterostatin-fat-intake-abstract]. This cleavage generates two products: the mature, active colipase (90 amino acids) and enterostatin.

Importantly, procolipase and mature colipase have similar abilities to interact with pancreatic lipase and restore its activity, suggesting that the primary purpose of the trypsin-catalyzed activation step is to release enterostatin rather than to regulate colipase function per se [dsilva-2007-polymorphism-abstract].

## Role in Lipid Digestion Pathway

### The Lipolytic Triad

Dietary fat digestion in the mammalian small intestine is accomplished by a highly efficient trio of factors: pancreatic lipase, colipase, and bile salts [chapus-1988-minireview-abstract]. These three components work synergistically to hydrolyze dietary triglycerides in an environment where other lipases would fail [lowe-1997-structure-function-abstract].

The process begins with the emulsification of dietary fat by bile salts and mechanical mixing in the duodenum, creating a bile salt-covered lipid-water interface. Colipase first adsorbs to this interface through its hydrophobic finger tips, then recruits and anchors pancreatic lipase [borgstrom-1975-interactions-abstract]. The resulting colipase-lipase complex efficiently catalyzes the stepwise hydrolysis of triglycerides to 2-monoacylglycerol and free fatty acids, which are then absorbed by enterocytes.

### Evidence from Knockout Studies

The essential role of colipase in fat digestion has been confirmed through studies of colipase-deficient (Clps-/-) mice. These animals exhibit decreased postnatal survival and weight gain, steatorrhea (fatty stools indicating fat malabsorption) on high-fat diets, and reduced body fat compared to wild-type littermates [dsilva-2007-polymorphism-abstract]. Interestingly, the fat malabsorption phenotype is more severe in colipase-deficient mice than in pancreatic lipase-deficient mice, likely because colipase also stimulates the activity of pancreatic lipase-related protein 2 (PLRP2), which contributes to triglyceride digestion especially in nursing pups.

### Enterostatin as a Satiety Signal

The activation peptide released from procolipase, enterostatin, has been demonstrated to function as a satiety signal that specifically reduces dietary fat intake [okada-1991-enterostatin-fat-intake-abstract]. In rats, intracerebroventricular injection of enterostatin (sequence VPDPR in most species, though APGPR in humans) selectively decreased consumption of high-fat diet by 45% while leaving low-fat diet intake unchanged [okada-1991-enterostatin-fat-intake-abstract].

Because procolipase secretion increases during high-fat feeding, enterostatin has been proposed as a feedback regulator connecting fat digestion to central appetite control [okada-1991-enterostatin-fat-intake-abstract]. However, studies in enterostatin-deficient mice (procolipase knockouts) suggest that enterostatin is not critically required for food intake regulation, as other compensatory pathways may exist. Nonetheless, enterostatin appears to have developmental effects on survival of newborns and alters cholesterol metabolism in mice.

## Clinical Significance

### Association with Type 2 Diabetes

A functional polymorphism in the CLPS gene (Arg109Cys in the preproprotein, corresponding to Arg92Cys in mature colipase) has been associated with increased risk of type 2 diabetes mellitus in two independent Caucasian populations [lindner-2005-diabetes-association-abstract]. In these studies, carriers of the Arg/Cys genotype (found in 2-3% of the population) had 3.75 to 4.86-fold increased odds of developing type 2 diabetes compared to non-carriers [lindner-2005-diabetes-association-abstract].

Functional characterization of this variant revealed that Cys92 colipase has decreased function specifically against long-chain triglycerides (only 50% of wild-type activity), while retaining full activity against short- and medium-chain triglycerides [dsilva-2007-polymorphism-abstract]. Furthermore, the variant protein is unstable and loses activity upon storage at 4°C due to oxidation of the extra cysteine residue, which disrupts the disulfide bond network essential for proper protein folding [dsilva-2007-polymorphism-abstract].

The mechanism linking impaired colipase function to diabetes risk is not fully established, but may involve altered fat absorption, changed postprandial lipid metabolism, or effects on enterostatin-mediated signaling. Additional genetic studies have shown that CLPS variability associates with altered insulin secretory function in non-diabetic humans, supporting a role for this gene in metabolic regulation beyond simple fat digestion [lindner-2005-diabetes-association-abstract].

### Pancreatic Insufficiency

Deficiency of pancreatic enzymes including lipase and colipase occurs in various conditions affecting the exocrine pancreas, including cystic fibrosis, chronic pancreatitis, and pancreatic cancer. In these conditions, enzyme replacement therapy is typically administered with meals to maintain fat absorption. The colipase-lipase complex provides the rationale for including both components in enzyme replacement preparations to maximize efficacy in the presence of endogenous bile salts.

## Open Questions

Several important questions remain regarding colipase biology and function:

1. **Enterostatin signaling mechanism**: The precise molecular pathway by which enterostatin suppresses fat intake—including its receptor, signaling cascade, and integration with other satiety signals—remains incompletely characterized. Understanding this pathway could have implications for obesity treatment.

2. **Dickkopf-colipase evolutionary relationship**: The functional significance of the structural homology between colipase and the Dickkopf family of Wnt antagonists remains unclear. Does the colipase fold in Dickkopf proteins serve a lipid-binding function, or has the structure been co-opted for different purposes?

3. **Therapeutic potential of colipase variants**: Could engineered colipase variants with enhanced stability or function be developed for improved enzyme replacement therapy in pancreatic insufficiency?

4. **Diabetes mechanism**: The molecular mechanism linking the Arg92Cys colipase polymorphism to type 2 diabetes risk warrants further investigation. Is the effect mediated through altered fat absorption, changes in enterostatin release, or other metabolic pathways?

5. **Regulation of expression**: The factors controlling CLPS gene expression during development and in response to dietary changes are not fully understood. How does the pancreas coordinate expression of lipase and colipase to maintain their 1:1 ratio?

6. **Colipase-like proteins**: The human genome contains a related gene, CLPSL1 (colipase-like 1), located on chromosome 6p21.31, encoding a protein with predicted enzyme activator activity and annotations suggesting roles in digestion and response to food. However, the precise function of CLPSL1 remains uncharacterized—it shows only ~30% sequence identity to orthologs in mouse and rat. Does this protein serve as a functional paralog of CLPS with tissue-specific or developmental roles in lipid metabolism?

7. **Computational advances**: Recent computational studies using AlphaFold and molecular dynamics simulations are revealing new details about lipase-colipase-fatty acid interactions, including the regulatory roles of calcium ions. How can these computational insights be translated into therapeutic applications for pancreatic diseases?

## References

- **borgstrom-1975-interactions-abstract**: Borgström B. On the interactions between pancreatic lipase and colipase and the substrate, and the importance of bile salts. J Lipid Res. 1975 Nov;16(6):411-7. PMID: 446.

- **chapus-1988-minireview-abstract**: Chapus C, Rovery M, Sarda L, Verger R. Minireview on pancreatic lipase and colipase. Biochimie. 1988 Sep;70(9):1223-34. PMID: 3147715. DOI: 10.1016/0300-9084(88)90188-5.

- **davis-1991-chromosome-mapping-abstract**: Davis RC, Xia YR, Mohandas T, Schotz MC, Lusis AJ. Assignment of the human pancreatic colipase gene to chromosome 6p21.1 to pter. Genomics. 1991 May;10(1):262-5. PMID: 2045105. DOI: 10.1016/0888-7543(91)90511-c.

- **dsilva-2007-polymorphism-abstract**: D'Silva S, Xiao X, Lowe ME. A polymorphism in the gene encoding procolipase produces a colipase, Arg92Cys, with decreased function against long-chain triglycerides. J Lipid Res. 2007 Nov;48(11):2478-84. PMID: 17715423. PMCID: PMC3684974. DOI: 10.1194/jlr.M700371-JLR200.

- **egloff-1995-crystallographic-abstract**: Egloff MP, Sarda L, Verger R, Cambillau C, van Tilbeurgh H. Crystallographic study of the structure of colipase and of the interaction with pancreatic lipase. Protein Sci. 1995 Jan;4(1):44-57. PMID: 7773176. DOI: 10.1002/pro.5560040107.

- **egloff-1995-246A-structure-abstract**: Egloff MP, Marguet F, Buono G, Verger R, Cambillau C, van Tilbeurgh H. The 2.46 A resolution structure of the pancreatic lipase-colipase complex inhibited by a C11 alkyl phosphonate. Biochemistry. 1995 Mar 7;34(9):2751-62. PMID: 7893686. DOI: 10.1021/bi00009a003. PDB: 1LPB.

- **lindner-2005-diabetes-association-abstract**: Lindner I, Helwig U, Rubin D, Li Y, Fisher E, Boeing H, Möhlig M, Spranger J, Pfeiffer A, Hampe J, Schreiber S, Döring F, Schrezenmeir J. Putative association between a new polymorphism in exon 3 (Arg109Cys) of the pancreatic colipase gene and type 2 diabetes mellitus in two independent Caucasian study populations. Mol Nutr Food Res. 2005 Oct;49(10):972-6. PMID: 16189801. DOI: 10.1002/mnfr.200500087.

- **lowe-1997-structure-function-abstract**: Lowe ME. Structure and function of pancreatic lipase and colipase. Annu Rev Nutr. 1997;17:141-58. PMID: 9240923. DOI: 10.1146/annurev.nutr.17.1.141.

- **okada-1991-enterostatin-fat-intake-abstract**: Okada S, York DA, Bray GA, Erlanson-Albertsson C. Enterostatin (Val-Pro-Asp-Pro-Arg), the activation peptide of procolipase, selectively reduces fat intake. Physiol Behav. 1991 Jun;49(6):1185-9. PMID: 1896500. DOI: 10.1016/0031-9384(91)90349-s.

- **sims-1992-gene-structure-abstract**: Sims HF, Lowe ME. The human colipase gene: isolation, chromosomal location, and tissue-specific expression. Biochemistry. 1992 Aug 11;31(31):7120-5. PMID: 1643046. DOI: 10.1021/bi00146a013.

- **vantilbeurgh-1999-colipase-structure-abstract**: van Tilbeurgh H, Bezzine S, Cambillau C, Verger R, Carrière F. Colipase: structure and interaction with pancreatic lipase. Biochim Biophys Acta. 1999 Nov 23;1441(2-3):173-84. PMID: 10570245. DOI: 10.1016/s1388-1981(99)00149-3.

- **wieloch-1979-NMR-bile-salt-abstract**: Wieloch T, Borgström B, Falk KE, Forsén S. High-resolution proton magnetic resonance study of porcine colipase and its interactions with taurodeoxycholate. Biochemistry. 1979 Apr 17;18(8):1622-8. PMID: 570855. DOI: 10.1021/bi00576a003.

- **breg-1995-procolipase-NMR-abstract**: Breg JN, et al. Solution Structure of Porcine Pancreatic Procolipase as Determined from 1H Homonuclear Two-Dimensional and Three-Dimensional NMR. Eur J Biochem. 1995;229:663-672. PDB: 1PCO.

- **yang-2000-open-lid-abstract**: Yang Y, Lowe ME. The open lid mediates pancreatic lipase function. J Lipid Res. 2000 Jan;41(1):48-57. PMID: 10627501.


## Citations

1. borgstrom-1975-interactions-abstract.md
2. breg-1995-procolipase-NMR-abstract.md
3. chapus-1988-minireview-abstract.md
4. davis-1991-chromosome-mapping-abstract.md
5. dsilva-2007-polymorphism-abstract.md
6. egloff-1995-246A-structure-abstract.md
7. egloff-1995-crystallographic-abstract.md
8. lindner-2005-diabetes-association-abstract.md
9. lowe-1997-structure-function-abstract.md
10. okada-1991-enterostatin-fat-intake-abstract.md
11. sims-1992-gene-structure-abstract.md
12. vantilbeurgh-1999-colipase-structure-abstract.md
13. wieloch-1979-NMR-bile-salt-abstract.md
14. yang-2000-open-lid-abstract.md