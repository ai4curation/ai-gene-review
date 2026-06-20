---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T19:52:54.280678'
end_time: '2026-06-18T20:02:51.845353'
duration_seconds: 597.56
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: JUGRE
  gene_id: A0A2I4G8T1
  gene_symbol: LOC109005703
  uniprot_accession: A0A2I4G8T1
  protein_description: 'RecName: Full=Glycosyltransferase {ECO:0000256|RuleBase:RU362057};
    EC=2.4.1.- {ECO:0000256|RuleBase:RU362057};'
  gene_info: Name=LOC109005703 {ECO:0000313|RefSeq:XP_018840292.1, ECO:0000313|RefSeq:XP_018840293.1,
    ECO:0000313|RefSeq:XP_018840295.1};
  organism_full: Juglans regia (English walnut).
  protein_family: Belongs to the UDP-glycosyltransferase family.
  protein_domains: Glyco_transf_N. (IPR058980); UDP_glucos_trans. (IPR002213); UDP_glycos_trans_CS.
    (IPR035595); Glyco_transf_N (PF26168); UDPGT (PF00201)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 14
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: A0A2I4G8T1-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A2I4G8T1
- **Protein Description:** RecName: Full=Glycosyltransferase {ECO:0000256|RuleBase:RU362057}; EC=2.4.1.- {ECO:0000256|RuleBase:RU362057};
- **Gene Information:** Name=LOC109005703 {ECO:0000313|RefSeq:XP_018840292.1, ECO:0000313|RefSeq:XP_018840293.1, ECO:0000313|RefSeq:XP_018840295.1};
- **Organism (full):** Juglans regia (English walnut).
- **Protein Family:** Belongs to the UDP-glycosyltransferase family.
- **Key Domains:** Glyco_transf_N. (IPR058980); UDP_glucos_trans. (IPR002213); UDP_glycos_trans_CS. (IPR035595); Glyco_transf_N (PF26168); UDPGT (PF00201)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "LOC109005703" matches the protein description above**
2. **Verify the organism is correct:** Juglans regia (English walnut).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'LOC109005703' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **LOC109005703** (gene ID: A0A2I4G8T1, UniProt: A0A2I4G8T1) in JUGRE.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A2I4G8T1
- **Protein Description:** RecName: Full=Glycosyltransferase {ECO:0000256|RuleBase:RU362057}; EC=2.4.1.- {ECO:0000256|RuleBase:RU362057};
- **Gene Information:** Name=LOC109005703 {ECO:0000313|RefSeq:XP_018840292.1, ECO:0000313|RefSeq:XP_018840293.1, ECO:0000313|RefSeq:XP_018840295.1};
- **Organism (full):** Juglans regia (English walnut).
- **Protein Family:** Belongs to the UDP-glycosyltransferase family.
- **Key Domains:** Glyco_transf_N. (IPR058980); UDP_glucos_trans. (IPR002213); UDP_glycos_trans_CS. (IPR035595); Glyco_transf_N (PF26168); UDPGT (PF00201)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "LOC109005703" matches the protein description above**
2. **Verify the organism is correct:** Juglans regia (English walnut).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'LOC109005703' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **LOC109005703** (gene ID: A0A2I4G8T1, UniProt: A0A2I4G8T1) in JUGRE.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Comprehensive Research Report: Functional Annotation of Gene LOC109005703 (A0A2I4G8T1) from *Juglans regia*

## Executive Summary

LOC109005703 encodes a glycosyltransferase belonging to the UDP-glycosyltransferase (UGT) superfamily in English walnut (*Juglans regia*). While no direct experimental studies on this specific gene were identified in the literature, comprehensive functional annotation can be inferred from its conserved domain architecture, family membership, and characterized homologs in walnut and related plant species. This report synthesizes current knowledge to provide a detailed functional annotation addressing catalytic mechanism, substrate specificity, pathway involvement, and subcellular localization.

## Gene and Protein Identity

The gene LOC109005703 (UniProt accession A0A2I4G8T1) from *Juglans regia* encodes a protein annotated as a glycosyltransferase with the enzyme classification EC 2.4.1.- (tahara2024elucidationandreconstitution pages 2-4). The protein belongs to the UDP-glycosyltransferase family, which represents the largest glycosyltransferase superfamily in plants (speeckaert2022ugt72amajor pages 1-2). In the model plant *Arabidopsis thaliana*, this family comprises 123 members, while in the tree species *Populus trichocarpa*, it has expanded to 281 members (speeckaert2022ugt72amajor pages 2-5). This expansion reflects the diversification of specialized metabolism in plants, particularly in long-lived woody species like walnut (speeckaert2022ugt72amajor pages 2-5).

## Structural Organization and Key Domains

### Domain Architecture

LOC109005703 contains two critical functional domains characteristic of plant UGTs:

1. **UDPGT domain (PF00201)**: The C-terminal domain responsible for binding the UDP-sugar donor molecule (gharabli2024thesugardonor pages 1-3, speeckaert2020characterizationofthe pages 1-4). This domain contains the highly conserved Plant Secondary Product Glycosyltransferase (PSPG) box, a 44-amino acid motif essential for UDP-sugar recognition (gharabli2024thesugardonor pages 1-3, gharabli2024thesugardonor pages 3-4, speeckaert2022ugt72amajor pages 2-5).

2. **Glyco_transf_N domain (PF26168, IPR058980)**: The N-terminal domain that binds and recognizes the acceptor substrate molecule (gharabli2024thesugardonor pages 1-3, gharabli2024thesugardonor pages 3-4). This domain is more variable among UGT family members and largely determines substrate specificity (speeckaert2022ugt72amajor pages 2-5).

### Three-Dimensional Structure

Plant UGTs adopt a canonical GT-B fold consisting of two Rossmann-type domains connected by a linker region, forming a central catalytic cleft (gharabli2024thesugardonor pages 1-3, speeckaert2022ugt72amajor pages 2-5). The C-terminal domain containing the PSPG motif predominantly interacts with the UDP-sugar donor, while the N-terminal domain forms a more variable pocket that accommodates diverse acceptor molecules (gharabli2024thesugardonor pages 3-4, speeckaert2022ugt72amajor pages 2-5). Within the PSPG box, conserved residues at specific positions interact with the UDP moiety and sugar portion of the donor substrate, with the terminal glutamine (Gln) residue often playing a critical role in sugar donor specificity (gharabli2024thesugardonor pages 1-3, gharabli2024thesugardonor pages 3-4).

## Catalytic Function and Mechanism

### General Reaction

UGTs catalyze the transfer of a sugar moiety from a UDP-activated sugar donor to a wide variety of acceptor molecules through glycosylation reactions (gharabli2024thesugardonor pages 1-3). The enzyme performs regio- and stereoselective one-step glycosylation, making these enzymes valuable tools in both plant metabolism and biotechnological applications (gharabli2024thesugardonor pages 1-3).

### Catalytic Mechanism

The catalytic mechanism of plant family 1 UGTs involves a highly conserved catalytic dyad, typically comprising histidine (His) and aspartate (Asp) residues (gharabli2024thesugardonor pages 1-3). In O-glycosylation reactions, the His residue acts as a Brønsted base that deprotonates the hydroxyl group of the acceptor molecule, facilitating nucleophilic attack on the anomeric carbon of the UDP-sugar (gharabli2024thesugardonor pages 1-3, speeckaert2022ugt72amajor pages 2-5). This reaction proceeds via an SN2-like mechanism with inversion of the anomeric configuration (gharabli2024thesugardonor pages 1-3).

### Sugar Donor Specificity

Plant UGTs most commonly utilize UDP-glucose (UDP-Glc) as the sugar donor, though members of the superfamily can also accept UDP-galactose (UDP-Gal), UDP-glucuronic acid (UDP-GlcA), UDP-rhamnose (UDP-Rha), and UDP-xylose (UDP-Xyl) depending on subfamily-specific donor recognition determinants (gharabli2024thesugardonor pages 1-3, gharabli2024thesugardonor pages 3-4). The donor specificity is strongly influenced by residues within and near the PSPG motif, particularly at conserved positions that interact with the C4 and C6 hydroxyl groups of the sugar moiety (gharabli2024thesugardonor pages 1-3, gharabli2024thesugardonor pages 3-4). While the specific sugar donor preference of LOC109005703 cannot be determined without experimental characterization, UDP-glucose is the most likely primary substrate based on family-wide trends (gharabli2024thesugardonor pages 1-3).

## Substrate Specificity and Biochemical Reactions

### Predicted Acceptor Substrates

While the precise acceptor substrate for LOC109005703 remains unknown without direct experimental evidence, the protein is predicted to act on phenolic secondary metabolites based on family characteristics and the metabolic context of walnut. Plant UGTs broadly glycosylate specialized metabolites derived from the phenylpropanoid pathway, including:

1. **Flavonoids**: UGTs catalyze the glycosylation of various flavonoid classes including anthocyanins, flavonols (quercetin, kaempferol), and flavones (ren2022genomewideanalysisof pages 2-4, ren2022genomewideanalysisof pages 1-2, speeckaert2022ugt72amajor pages 1-2). In the related species *Morella rubra* (Chinese bayberry), characterized UGTs such as MrUFGT (MrUGT78A26) and MrUGT72B67 were identified as flavonoid 3-O-glucosyltransferases involved in the accumulation of cyanidin 3-O-glucoside and quercetin 3-O-glucoside (ren2022genomewideanalysisof pages 2-4, ren2022genomewideanalysisof pages 1-2). The importance of a conserved glutamine residue (Gln375 in MrUFGT and Gln391 in MrUGT72B67) for glucosyl transfer activity was demonstrated through site-directed mutagenesis (ren2022genomewideanalysisof pages 2-4, ren2022genomewideanalysisof pages 1-2).

2. **Gallic Acid and Hydroxybenzoic Acids**: Members of the UGT84A clade catalyze the formation of β-glucogallin (1-O-galloyl-β-D-glucose) from gallic acid and UDP-glucose, a critical step in hydrolyzable tannin biosynthesis (tahara2024elucidationandreconstitution pages 1-2, tahara2024elucidationandreconstitution pages 4-6). In walnut, two characterized enzymes, JrGGT1 (UGT84A73) and JrGGT2 (UGT84A74), have been identified as gallic acid glucosyltransferases (tahara2024elucidationandreconstitution pages 4-6). These enzymes exhibit substrate promiscuity, accepting both hydroxybenzoic acids (HBAs; C6-C1 compounds) and hydroxycinnamic acids (HCAs; C6-C3 compounds) (tahara2024elucidationandreconstitution pages 4-6).

3. **Monolignols**: The UGT72 family includes members that glycosylate monolignols (p-coumaryl alcohol, coniferyl alcohol, and sinapyl alcohol), producing monolignol glucosides such as coniferin and syringin (speeckaert2022ugt72amajor pages 2-5, speeckaert2022ugt72amajor pages 1-2, speeckaert2020characterizationofthe pages 1-4). In poplar (*Populus* spp.), UGT72 family members including UGT72AZ1, UGT72AZ2, UGT72B37, and UGT72B39 have been demonstrated to glycosylate monolignols in vitro (speeckaert2020characterizationofthe pages 1-4, speeckaert2020characterizationofthe pages 6-10).

## Biochemical Pathways and Biological Role

### Phenylpropanoid Pathway Context

LOC109005703 functions within the broader context of plant secondary metabolism, specifically the phenylpropanoid pathway (speeckaert2022ugt72amajor pages 2-5, speeckaert2022ugt72amajor pages 1-2). This pathway begins with the aromatic amino acids phenylalanine and tyrosine, which are products of the shikimate pathway (speeckaert2022ugt72amajor pages 2-5). Through a series of enzymatic steps involving phenylalanine ammonia-lyase (PAL), cinnamate 4-hydroxylase (C4H), and 4-coumarate:CoA ligase (4CL), the pathway generates p-coumaroyl-CoA, the last common precursor for the biosynthesis of monolignols, flavonoids, stilbenes, and other phenylpropanoid-derived compounds (speeckaert2022ugt72amajor pages 2-5).

### Hydrolyzable Tannin Biosynthesis

Walnut is known to accumulate hydrolyzable tannins (HTs), a class of polyphenols characteristic of core eudicot plants (tahara2024elucidationandreconstitution pages 2-4, tahara2024elucidationandreconstitution pages 1-2). The biosynthesis of HTs is initiated by the formation of gallic acid from 3-dehydroshikimic acid, catalyzed by bifunctional dehydroquinate dehydratase/shikimate dehydrogenases (DQD/SDHs) (tahara2024elucidationandreconstitution pages 1-2). A DQD/SDH from *Juglans regia* (JrSDH) has been described that catalyzes the oxidation of 3-dehydroshikimic acid to gallic acid (tahara2024elucidationandreconstitution pages 1-2).

In the second step of HT biosynthesis, UDP-glycosyltransferases esterify gallic acid with glucose to form β-glucogallin (1-O-galloyl-β-D-glucose) (tahara2024elucidationandreconstitution pages 1-2, tahara2024elucidationandreconstitution pages 4-6). This reaction is catalyzed by gallic acid UGTs belonging to the UGT84A clade (tahara2024elucidationandreconstitution pages 4-6). β-Glucogallin then serves as both an acyl acceptor and donor in subsequent galloylation steps, eventually leading to the formation of gallotannins and ellagitannins (tahara2024elucidationandreconstitution pages 1-2, tahara2024elucidationandreconstitution pages 4-6). While LOC109005703's specific role in this pathway cannot be confirmed without experimental data, its family membership and the presence of characterized walnut gallic acid UGTs (JrGGT1 and JrGGT2) suggest a potential involvement in phenolic acid or tannin-related metabolism (tahara2024elucidationandreconstitution pages 4-6).

### Flavonoid Metabolism

UGTs play essential roles in flavonoid biosynthesis by catalyzing the glycosylation of flavonoid aglycones, which enhances their solubility, stability, and biological activity (ren2022genomewideanalysisof pages 2-4, ren2022genomewideanalysisof pages 1-2, speeckaert2022ugt72amajor pages 1-2). In Chinese bayberry, UV-B treatment significantly induced the accumulation of cyanidin 3-O-glucoside and quercetin 3-O-glucoside in fruit, with corresponding increases in the expression of specific UGT genes (ren2022genomewideanalysisof pages 2-4, ren2022genomewideanalysisof pages 1-2). Given the nutritional and medical importance of flavonoid glycosides in walnut tissues, LOC109005703 may contribute to the diversification of these bioactive compounds.

### Monolignol Homeostasis

UGT72 family members are involved in monolignol homeostasis through the glycosylation of monolignols, producing storage or transport forms of these lignin precursors (speeckaert2022ugt72amajor pages 2-5, speeckaert2022ugt72amajor pages 1-2, speeckaert2020characterizationofthe pages 1-4). Monolignol glucosides such as coniferin and syringin accumulate in vascular tissues and can be incorporated into the lignin polymer (speeckaert2020characterizationofthe pages 1-4). Glycosylation renders monolignols less cytotoxic by reducing their reactivity and facilitates their storage in vacuoles or transport to the cell wall (speeckaert2020characterizationofthe pages 1-4, speeckaert2020characterizationofthe pages 6-10).

### Functional Significance of Glycosylation

Glycosylation serves multiple important functions in plant metabolism (speeckaert2022ugt72amajor pages 2-5, speeckaert2022ugt72amajor pages 1-2):

1. **Detoxification**: Reduces the toxicity of reactive phenolic compounds
2. **Solubility enhancement**: Increases the water solubility of hydrophobic metabolites
3. **Stability**: Protects compounds from degradation
4. **Storage**: Enables compartmentalization in vacuoles
5. **Transport**: Facilitates movement of metabolites within and between cells
6. **Regulation**: Modulates the biological activity of signaling molecules

## Subcellular Localization

### Predicted Localization

While subcellular localization data for LOC109005703 is not available, insights can be drawn from characterized UGT family members. Studies on poplar UGT72 proteins revealed diverse localization patterns depending on subfamily membership (speeckaert2020characterizationofthe pages 1-4, speeckaert2020characterizationofthe pages 6-10). UGT72 group 1 members (UGT72AZ1 and UGT72AZ2) and group 4 members (UGT72B37 and UGT72B39) were found to be associated with both the nucleus and the endoplasmic reticulum (ER) (speeckaert2020characterizationofthe pages 1-4). In contrast, UGT72A2 (group 2) localized to bodies associated with chloroplasts and possibly within chloroplasts themselves (speeckaert2020characterizationofthe pages 1-4).

Based on these observations and the general characteristics of UGTs involved in secondary metabolism, LOC109005703 is most likely localized to the **cytoplasm and/or endoplasmic reticulum** (speeckaert2020characterizationofthe pages 1-4, speeckaert2020characterizationofthe pages 6-10). This localization would be consistent with its predicted role in glycosylating phenolic secondary metabolites. Following glycosylation, the products are often transported to and stored in vacuoles, where they accumulate at high concentrations (speeckaert2020characterizationofthe pages 1-4, speeckaert2020characterizationofthe pages 6-10).

### Tissue-Specific Expression

Expression patterns of UGT genes in woody plants often show enrichment in vascular tissues, particularly in phloem, cambium, and developing xylem (speeckaert2020characterizationofthe pages 1-4, speeckaert2020characterizationofthe pages 6-10). Promoter analyses of poplar UGT72 genes revealed the presence of cis-regulatory elements associated with vascular tissue differentiation and secondary cell wall formation, including Secondary wall MYB-Responsive Elements (SMRE), Secondary wall NAC-Binding Elements (SNBE), and Tracheary-Element-Regulating cis-Elements (TERE) (speeckaert2020characterizationofthe pages 6-10). While tissue-specific expression data for LOC109005703 is not available, similar expression patterns would be expected given its family membership.

## Evidence Assessment and Limitations

### Available Evidence

The functional annotation of LOC109005703 presented in this report is based on:

1. **Domain architecture analysis**: The protein contains conserved UDPGT (PF00201) and Glyco_transf_N (PF26168) domains characteristic of plant UGTs (gharabli2024thesugardonor pages 1-3, gharabli2024thesugardonor pages 3-4, speeckaert2022ugt72amajor pages 2-5)
2. **Family-level functional studies**: Extensive characterization of plant UGT families, including substrate specificity, catalytic mechanism, and pathway involvement (gharabli2024thesugardonor pages 1-3, gharabli2024thesugardonor pages 3-4, speeckaert2022ugt72amajor pages 2-5, speeckaert2022ugt72amajor pages 1-2)
3. **Homology to characterized enzymes**: Identified walnut UGTs (JrGGT1 and JrGGT2) and related species UGTs provide functional context (tahara2024elucidationandreconstitution pages 4-6)
4. **Structural and mechanistic insights**: Crystal structures and biochemical studies of UGT family members elucidate the conserved catalytic mechanism (gharabli2024thesugardonor pages 1-3, gharabli2024thesugardonor pages 3-4)

### Limitations and Confidence Level

**Important limitation**: No direct experimental functional characterization or gene expression data for LOC109005703 was identified in the accessible scientific literature. Several recent publications specifically on walnut UGT gene family members and their roles in anthocyanin, polyphenol, and hydrolyzable tannin biosynthesis could not be retrieved, including genome-wide UGT family analyses by Shi et al. (2024) and transcriptomic studies by Zhao et al. (2023) and Wang et al. (2021).

The functional annotation provided represents **inference-based predictions** derived from:
- Conserved domain structure and family membership
- Characterized homologs in walnut and closely related plant species
- General biochemical properties of the UGT superfamily

**Confidence assessment**: The prediction that LOC109005703 functions as a glycosyltransferase catalyzing the transfer of a sugar from UDP-sugar to a small-molecule acceptor is **highly confident** based on domain structure. The prediction that it acts on phenolic secondary metabolites (flavonoids, phenolic acids, or monolignols) in the phenylpropanoid pathway is **moderately confident** based on family characteristics and walnut metabolism. The specific substrate identity, exact biochemical pathway, tissue expression pattern, and subcellular localization remain **uncertain** without direct experimental validation.

## Comprehensive Summary Table

| Category | Annotation for LOC109005703 / A0A2I4G8T1 | Evidence / Basis |
|---|---|---|
| Gene / protein identity | **Gene:** LOC109005703; **UniProt accession:** A0A2I4G8T1; **Organism:** *Juglans regia* (English walnut); **Protein family:** UDP-glycosyltransferase family | UniProt-provided identity in the prompt; plant UGTs are a major GT1 family defined by UDP-sugar-dependent glycosylation and a conserved PSPG motif (gharabli2024thesugardonor pages 1-3, speeckaert2022ugt72amajor pages 2-5, speeckaert2022ugt72amajor pages 1-2) |
| Catalytic function | **Enzyme class:** Glycosyltransferase, EC 2.4.1.-; **Predicted reaction:** transfer of a sugar from a UDP-sugar donor to a small-molecule acceptor; **Likely bond type:** most likely O-glycosylation/ester-forming or O-glucosylation activity typical of plant family 1 UGTs | Plant family 1 UGTs transfer sugars from UDP-activated donors to diverse acceptors in a regio- and stereoselective one-step reaction (gharabli2024thesugardonor pages 1-3); related plant UGTs glycosylate phenylpropanoids, flavonoids, and hydroxybenzoic acids (speeckaert2022ugt72amajor pages 2-5, tahara2024elucidationandreconstitution pages 4-6, speeckaert2020characterizationofthe pages 1-4) |
| Catalytic mechanism | **Mechanism:** conserved catalytic dyad, typically **His-Asp**; His acts as catalytic base to deprotonate the acceptor, enabling **SN2-like nucleophilic attack** on the anomeric carbon of the UDP-sugar with inversion of configuration | Explicitly described for plant family 1 UGTs in structural/mechanistic review literature (gharabli2024thesugardonor pages 1-3); UGT72 structural discussion also places catalytic His near acceptor and conserved C-terminal residues near donor sugar (speeckaert2022ugt72amajor pages 2-5) |
| Sugar donor(s) | **Most likely primary donor:** UDP-glucose; **Possible alternative donors in broader UGT family:** UDP-galactose, UDP-rhamnose, UDP-glucuronic acid, UDP-xylose depending on subfamily-specific donor recognition | UDP-glucose is the most common donor for plant UGTs; donor specificity is strongly influenced by the PSPG motif and nearby residues (gharabli2024thesugardonor pages 1-3, gharabli2024thesugardonor pages 3-4) |
| Predicted acceptor substrates | **Predicted acceptors:** phenolic small molecules, especially **flavonoids, hydroxybenzoic/hydroxycinnamic acids, gallic acid, and/or monolignols**; exact substrate for LOC109005703 is **unknown** | Plant UGTs broadly glycosylate specialized metabolites (speeckaert2022ugt72amajor pages 1-2, speeckaert2020characterizationofthe pages 1-4); UGT84A enzymes can glycosylate gallic acid and related phenolic acids (tahara2024elucidationandreconstitution pages 4-6); UGT72 members often glycosylate monolignols and some flavonoids (speeckaert2022ugt72amajor pages 2-5, speeckaert2020characterizationofthe pages 1-4) |
| Key domains | **Glyco_transf_N / PF26168:** N-terminal acceptor-binding region; **UDPGT / PF00201:** C-terminal donor-binding domain; **UDP_glycos_trans_CS / PSPG box:** conserved plant secondary product glycosyltransferase motif important for UDP-sugar binding | The N-terminal domain is more variable and largely shapes acceptor recognition, whereas the conserved C-terminal PSPG-containing domain binds the UDP-sugar donor (gharabli2024thesugardonor pages 3-4, speeckaert2022ugt72amajor pages 2-5, speeckaert2020characterizationofthe pages 1-4) |
| Overall structure | **Predicted fold:** canonical **GT-B fold** with two Rossmann-like domains connected by a linker, forming a central catalytic cleft | Described for plant UGTs generally and for UGT72 family members specifically (gharabli2024thesugardonor pages 3-4, speeckaert2022ugt72amajor pages 2-5) |
| Biochemical pathways | **Primary pathway context:** phenylpropanoid / specialized secondary metabolism; **Likely pathway interfaces:** flavonoid glycosylation, hydroxybenzoic acid conjugation, monolignol homeostasis, and potentially hydrolyzable tannin-related metabolism | UGTs act extensively in phenylpropanoid and specialized metabolism (speeckaert2022ugt72amajor pages 2-5, speeckaert2022ugt72amajor pages 1-2); walnut and other core eudicots use UGTs in pathways connected to phenolics and tannins (tahara2024elucidationandreconstitution pages 2-4, tahara2024elucidationandreconstitution pages 4-6) |
| Potential role in walnut metabolism | **Most plausible functional niche:** modification of walnut phenolic metabolites to alter solubility, stability, storage, transport, and detoxification; could contribute to accumulation/homeostasis of flavonoid glycosides, tannin intermediates, or monolignol glucosides, but this remains unverified for this specific locus | Glycosylation generally decreases toxicity and increases solubility/stability of specialized metabolites (speeckaert2022ugt72amajor pages 1-2); walnut is rich in polyphenol-related metabolism and known walnut UGTs include hydrolyzable tannin-associated UGT84A73/JrGGT1 and UGT84A74/JrGGT2 (tahara2024elucidationandreconstitution pages 4-6) |
| Hydrolyzable tannin connection | **Possible but unproven:** walnut has characterized UGT84A family members involved in forming **β-glucogallin** from gallic acid + UDP-glucose, a key hydrolyzable tannin intermediate; whether LOC109005703 belongs to this exact functional clade is **not established** | β-Glucogallin formation is a key HT biosynthetic step catalyzed by gallic acid UGTs; walnut proteins JrGGT1/2 (UGT84A73/74) are cited as such enzymes (tahara2024elucidationandreconstitution pages 4-6) |
| Subcellular localization | **Predicted localization:** likely **cytosol and/or endoplasmic reticulum-associated**, as is common for many soluble plant UGTs involved in specialized metabolism; products may subsequently be trafficked to the vacuole | Related poplar UGT72 proteins localize to nucleus/ER or chloroplast-associated compartments depending on subgroup, illustrating family diversity; many glycosylated products are stored in vacuoles (speeckaert2020characterizationofthe pages 1-4, speeckaert2020characterizationofthe pages 6-10) |
| Confidence / evidence type | **Evidence level for LOC109005703:** low-to-moderate, based on **domain architecture, family assignment, and homology-based inference**; **no direct experimental functional or localization data were identified for this specific walnut gene** | No direct literature for LOC109005703 was retrieved; annotation rests on conserved UGT features and characterized homologs from walnut and other plants (gharabli2024thesugardonor pages 1-3, speeckaert2022ugt72amajor pages 2-5, tahara2024elucidationandreconstitution pages 4-6, speeckaert2020characterizationofthe pages 1-4) |


*Table: This table summarizes the current evidence-based functional annotation for the walnut gene LOC109005703 (A0A2I4G8T1). It distinguishes direct identity information from homology-based inferences about catalytic mechanism, substrate scope, pathway context, and localization.*

## Conclusions

LOC109005703 from *Juglans regia* encodes a member of the UDP-glycosyltransferase superfamily predicted to catalyze the glycosylation of phenolic secondary metabolites. The protein possesses the conserved structural features characteristic of plant UGTs, including the PSPG motif-containing C-terminal domain for UDP-sugar binding and a variable N-terminal domain for acceptor recognition. Based on characterized walnut UGTs and related family members, LOC109005703 most likely functions in the phenylpropanoid pathway, potentially contributing to flavonoid glycosylation, hydrolyzable tannin biosynthesis, or monolignol homeostasis. The enzyme is predicted to localize to the cytoplasm and/or endoplasmic reticulum, consistent with other UGTs involved in specialized metabolism.

While this functional annotation provides a comprehensive framework based on the best available evidence, experimental validation through heterologous expression, enzyme assays with candidate substrates, and expression analysis in different walnut tissues and developmental stages would be required to definitively determine the biological role of LOC109005703 in walnut metabolism.

## References

All evidence and citations are derived from the following sources cited in the text:
- pqac-00000000: Tahara et al. (2024) - Hydrolyzable tannin biosynthesis review
- pqac-00000001: Tahara et al. (2024) - Gallic acid formation and β-glucogallin synthesis
- pqac-00000002: Ren et al. (2022) - UGT gene family in Chinese bayberry, substrate specificity
- pqac-00000003: Ren et al. (2022) - Flavonoid glucosyltransferases
- pqac-00000004: Gharabli & Welner (2024) - Sugar donor specificity and catalytic mechanism
- pqac-00000005: Gharabli & Welner (2024) - PSPG motif structure and function
- pqac-00000006: Speeckaert et al. (2022) - UGT72 family review, phenylpropanoid pathway
- pqac-00000007: Speeckaert et al. (2022) - UGT evolutionary expansion and functions
- pqac-00000008: Tahara et al. (2024) - Walnut gallic acid UGTs and UGT84A family
- pqac-00000009: Speeckaert et al. (2020) - Poplar UGT72 characterization and localization
- pqac-00000010: Speeckaert et al. (2020) - UGT tissue expression and subcellular localization

References

1. (tahara2024elucidationandreconstitution pages 2-4): Ko Tahara, Carsten Milkowski, and Chihiro Oda-Yamamizo. Elucidation and reconstitution of hydrolyzable tannin biosynthesis. Plant Biotechnology, 41:203-212, Sep 2024. URL: https://doi.org/10.5511/plantbiotechnology.24.0601a, doi:10.5511/plantbiotechnology.24.0601a. This article has 11 citations and is from a peer-reviewed journal.

2. (speeckaert2022ugt72amajor pages 1-2): Nathanaël Speeckaert, Mondher El Jaziri, Marie Baucher, and Marc Behr. Ugt72, a major glycosyltransferase family for flavonoid and monolignol homeostasis in plants. Biology, 11:441, Mar 2022. URL: https://doi.org/10.3390/biology11030441, doi:10.3390/biology11030441. This article has 44 citations.

3. (speeckaert2022ugt72amajor pages 2-5): Nathanaël Speeckaert, Mondher El Jaziri, Marie Baucher, and Marc Behr. Ugt72, a major glycosyltransferase family for flavonoid and monolignol homeostasis in plants. Biology, 11:441, Mar 2022. URL: https://doi.org/10.3390/biology11030441, doi:10.3390/biology11030441. This article has 44 citations.

4. (gharabli2024thesugardonor pages 1-3): Hani Gharabli and Ditte Hededam Welner. The sugar donor specificity of plant family 1 glycosyltransferases. Frontiers in Bioengineering and Biotechnology, May 2024. URL: https://doi.org/10.3389/fbioe.2024.1396268, doi:10.3389/fbioe.2024.1396268. This article has 22 citations.

5. (speeckaert2020characterizationofthe pages 1-4): Nathanael Speeckaert, Nassirou Mahamadou Adamou, Hadjara Amadou Hassane, Fabien Baldacci-Cresp, Adeline Mol, Geert Goeminne, Wout Boerjan, Pierre Duez, Simon Hawkins, Godfrey Neutelings, Thomas Hoffmann, Wilfried Schwab, Mondher El Jaziri, Marc Behr, and Marie Baucher. Characterization of the udp-glycosyltransferase ugt72 family in poplar and identification of genes involved in the glycosylation of monolignols. International Journal of Molecular Sciences, 21:5018, Jul 2020. URL: https://doi.org/10.3390/ijms21145018, doi:10.3390/ijms21145018. This article has 52 citations.

6. (gharabli2024thesugardonor pages 3-4): Hani Gharabli and Ditte Hededam Welner. The sugar donor specificity of plant family 1 glycosyltransferases. Frontiers in Bioengineering and Biotechnology, May 2024. URL: https://doi.org/10.3389/fbioe.2024.1396268, doi:10.3389/fbioe.2024.1396268. This article has 22 citations.

7. (ren2022genomewideanalysisof pages 2-4): Chuanhong Ren, Yunlin Cao, Mengyun Xing, Yan Guo, Jiajia Li, Lei Xue, Chongde Sun, Changjie Xu, Kunsong Chen, and Xian Li. Genome-wide analysis of udp-glycosyltransferase gene family and identification of members involved in flavonoid glucosylation in chinese bayberry (morella rubra). Frontiers in Plant Science, Sep 2022. URL: https://doi.org/10.3389/fpls.2022.998985, doi:10.3389/fpls.2022.998985. This article has 38 citations.

8. (ren2022genomewideanalysisof pages 1-2): Chuanhong Ren, Yunlin Cao, Mengyun Xing, Yan Guo, Jiajia Li, Lei Xue, Chongde Sun, Changjie Xu, Kunsong Chen, and Xian Li. Genome-wide analysis of udp-glycosyltransferase gene family and identification of members involved in flavonoid glucosylation in chinese bayberry (morella rubra). Frontiers in Plant Science, Sep 2022. URL: https://doi.org/10.3389/fpls.2022.998985, doi:10.3389/fpls.2022.998985. This article has 38 citations.

9. (tahara2024elucidationandreconstitution pages 1-2): Ko Tahara, Carsten Milkowski, and Chihiro Oda-Yamamizo. Elucidation and reconstitution of hydrolyzable tannin biosynthesis. Plant Biotechnology, 41:203-212, Sep 2024. URL: https://doi.org/10.5511/plantbiotechnology.24.0601a, doi:10.5511/plantbiotechnology.24.0601a. This article has 11 citations and is from a peer-reviewed journal.

10. (tahara2024elucidationandreconstitution pages 4-6): Ko Tahara, Carsten Milkowski, and Chihiro Oda-Yamamizo. Elucidation and reconstitution of hydrolyzable tannin biosynthesis. Plant Biotechnology, 41:203-212, Sep 2024. URL: https://doi.org/10.5511/plantbiotechnology.24.0601a, doi:10.5511/plantbiotechnology.24.0601a. This article has 11 citations and is from a peer-reviewed journal.

11. (speeckaert2020characterizationofthe pages 6-10): Nathanael Speeckaert, Nassirou Mahamadou Adamou, Hadjara Amadou Hassane, Fabien Baldacci-Cresp, Adeline Mol, Geert Goeminne, Wout Boerjan, Pierre Duez, Simon Hawkins, Godfrey Neutelings, Thomas Hoffmann, Wilfried Schwab, Mondher El Jaziri, Marc Behr, and Marie Baucher. Characterization of the udp-glycosyltransferase ugt72 family in poplar and identification of genes involved in the glycosylation of monolignols. International Journal of Molecular Sciences, 21:5018, Jul 2020. URL: https://doi.org/10.3390/ijms21145018, doi:10.3390/ijms21145018. This article has 52 citations.

## Artifacts

- [Edison artifact artifact-00](A0A2I4G8T1-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. tahara2024elucidationandreconstitution pages 2-4
2. gharabli2024thesugardonor pages 1-3
3. tahara2024elucidationandreconstitution pages 4-6
4. tahara2024elucidationandreconstitution pages 1-2
5. speeckaert2020characterizationofthe pages 1-4
6. speeckaert2020characterizationofthe pages 6-10
7. gharabli2024thesugardonor pages 3-4
8. ren2022genomewideanalysisof pages 2-4
9. ren2022genomewideanalysisof pages 1-2
10. https://doi.org/10.5511/plantbiotechnology.24.0601a,
11. https://doi.org/10.3390/biology11030441,
12. https://doi.org/10.3389/fbioe.2024.1396268,
13. https://doi.org/10.3390/ijms21145018,
14. https://doi.org/10.3389/fpls.2022.998985,