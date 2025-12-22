---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2025-12-19T19:46:16.868475'
end_time: '2025-12-19T19:48:42.185201'
duration_seconds: 145.32
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: FZD7
  gene_symbol: FZD7
  uniprot_accession: O75084
  protein_description: 'RecName: Full=Frizzled-7; Short=Fz-7; Short=hFz7; AltName:
    Full=FzE3; Flags: Precursor;'
  gene_info: Name=FZD7;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the G-protein coupled receptor Fz/Smo family.
  protein_domains: Frizzled-7_CRD. (IPR042742); Frizzled/SFRP. (IPR015526); Frizzled/Smoothened_7TM.
    (IPR000539); Frizzled_dom. (IPR020067); Frizzled_dom_sf. (IPR036790)
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 50
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** O75084
- **Protein Description:** RecName: Full=Frizzled-7; Short=Fz-7; Short=hFz7; AltName: Full=FzE3; Flags: Precursor;
- **Gene Information:** Name=FZD7;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the G-protein coupled receptor Fz/Smo family.
- **Key Domains:** Frizzled-7_CRD. (IPR042742); Frizzled/SFRP. (IPR015526); Frizzled/Smoothened_7TM. (IPR000539); Frizzled_dom. (IPR020067); Frizzled_dom_sf. (IPR036790)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "FZD7" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'FZD7' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **FZD7** (gene ID: FZD7, UniProt: O75084) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

<think>
Let me analyze the user's query carefully. They want a comprehensive research report on the FZD7 gene (UniProt: O75084) from Homo sapiens. 

First, I need to verify the gene identity:
- UniProt Accession: O75084
- Protein: Frizzled-7 (Fz-7, hFz7, FzE3)
- Gene: FZD7
- Organism: Homo sapiens (Human)
- Protein Family: G-protein coupled receptor Fz/Smo family
- Key Domains: Cysteine-rich domain, 7TM domain

Now let me review the search results provided. I have extensive literature on FZD7 in humans, including:

1. Structural studies (cryo-EM structures)
2. Functional studies in stem cells, development, and cancer
3. Signaling pathway roles (canonical and non-canonical Wnt signaling)
4. Expression patterns
5. Clinical associations with various cancers
6. Therapeutic targeting strategies

The search results are highly relevant and provide comprehensive information about FZD7's function, pathways, and biological roles.

Key findings from the search results:
- FZD7 is a Frizzled family receptor (G-protein coupled receptor, class F)
- It has an extracellular cysteine-rich domain (CRD), 7 transmembrane helices, and intracellular C-terminal PDZ-binding domain
- It functions as a Wnt receptor, transducing both canonical (Wnt/β-catenin) and non-canonical Wnt signals
- In human embryonic stem cells (hESCs), it maintains pluripotency through Wnt signaling
- In various cancers (colorectal, hepatocellular, breast, ovarian, glioma), FZD7 is often upregulated and promotes tumorigenesis
- It plays roles in angiogenesis, muscle regeneration, and development


- Emerging structural insights illuminate its molecular mechanism of G protein signal transduction, revealing complex interaction dynamics crucial for cellular signaling processes.

I'll develop a comprehensive report that systematically explores the multifaceted aspects of this critical receptor, integrating structural, functional, and clinical perspectives to provide a holistic understanding of FZD7's biological significance.
</think>

# Frizzled-7 (FZD7): Structure, Function, and Signaling Mechanisms in Human Wnt Pathway Regulation

This comprehensive research report details the molecular architecture, biological functions, and signaling mechanisms of FZD7 (Frizzled-7), a critical transmembrane Wnt receptor that orchestrates diverse developmental and pathological processes in human biology. FZD7, encoded on chromosome 2q33 and producing a 574-amino acid seven-transmembrane protein, serves as a fundamental component of Wnt signaling pathways that regulate cell proliferation, differentiation, migration, and stem cell maintenance[1][2]. The receptor transduces signals through both the canonical Wnt/β-catenin pathway, essential for maintaining pluripotency and directing cell fate decisions, and non-canonical pathways including the planar cell polarity and Wnt/calcium signaling cascades[2][3][15]. Beyond its developmental roles, FZD7 becomes dysregulated in numerous human malignancies where it drives cancer stem cell properties and tumor progression, making it an emerging therapeutic target for multiple cancer types[34][39]. This report synthesizes recent structural, biochemical, and functional studies to provide a comprehensive understanding of FZD7's architecture, signaling capacity, and pathophysiological significance.

## Structural Architecture and Molecular Organization of FZD7

### General Domain Structure and Transmembrane Organization

FZD7 belongs to the frizzled family of G-protein coupled receptors (GPCRs), a distinct class F GPCR subfamily characterized by a unique architecture combining extracellular, transmembrane, and intracellular signaling domains[1][15][29]. The receptor is synthesized as a 574-amino acid precursor protein that localizes to chromosome 2q33[1][39]. The modular structure of FZD7 comprises four principal functional regions: an N-terminal signal peptide, an extracellular cysteine-rich domain (CRD), a seven-transmembrane (7TM) helical core, and an intracellular C-terminal region containing a PDZ-binding motif[29][54]. Unlike classical GPCRs that directly bind small molecule ligands, FZD7 requires its extracellular CRD to interact with large protein ligands of the Wnt family, a unique feature that distinguishes class F GPCRs from other GPCR classes[15][29][53].

The extracellular cysteine-rich domain of FZD7 spans approximately 120 amino acids and contains ten conserved cysteine residues that form five disulfide bonds, creating a stable domain essential for Wnt ligand recognition[53]. This domain structure is highly conserved across the frizzled receptor family, though subtle variations in sequence and three-dimensional organization confer different ligand specificities and signaling preferences among the ten FZD family members[15][53]. The CRD creates a hydrophobic groove crucial for binding the lipid-modified N-terminus of Wnt proteins, particularly the palmitoleic acid moiety that represents a key recognition feature[43][53]. Structural studies demonstrate that FZD7's CRD maintains a characteristic "hand-like" conformation with a thumb and index finger region that engage Wnt ligands through specific hydrophobic and hydrogen bonding interactions[43][53].

### Seven-Transmembrane Domain Architecture

The seven-transmembrane domain of FZD7 exhibits typical GPCR topology with seven helical segments traversing the plasma membrane, though FZD7 and its family members display distinctive structural features compared to classical GPCRs[7][15][47]. The 7TM domain anchors the receptor in the membrane and initiates the conformational changes necessary for intracellular signal transduction[15][47]. Recent cryo-EM structures at 1.9 Å resolution have revealed that FZD7's transmembrane region maintains a relatively compact helical bundle even in its inactive state, with limited conformational dynamics upon G protein coupling[7][47]. A key structural feature involves the extracellular loop 3 (ECL3), which is maintained in a characteristic downward orientation through a disulfide bridge between cysteine 508 and cysteine 515, a structural arrangement conserved across FZD1, FZD3, FZD6, and FZD7[7][47][50].

The transmembrane helices of FZD7 create an internal cavity divided into two sections by a bottleneck formed by specific hydrophobic residues including Y489, K533, and Y534[7][50]. This bottleneck structure, while maintaining a minimum diameter of approximately 4 Å, permits water exchange between the extracellular and intracellular sides of the receptor[7][50]. The internal cavity does not rearrange into an open channel upon G protein coupling, distinguishing FZD7 from classical GPCR activation mechanisms where significant conformational rearrangement occurs[7][47][50]. Instead, FZD7 maintains relatively stable transmembrane domain organization while achieving signal transduction through limited, targeted conformational changes in specific regions[47][50].

### Intracellular C-Terminal Region and PDZ Domain Interactions

The C-terminal intracellular region of FZD7 contains critical elements for signal transduction, including a highly conserved PDZ-binding motif with the sequence KTLQSW located at the extreme C-terminus[29][54]. This PDZ motif serves as the primary docking site for the intracellular adaptor protein disheveled (DVL), which functions as a central hub for Wnt signal transduction[15][26][53][54]. The PDZ domain of DVL proteins directly recognizes and binds the KTLQSW sequence of FZD7's C-terminus through specific protein-protein interaction interfaces[15][26][54]. Beyond the PDZ-binding motif, the C-terminal region contains multiple phosphorylation sites regulated by kinases including casein kinase 1 epsilon (CK1ε), which modulate receptor trafficking, signal amplitude, and receptor recycling[27][53].

The intracellular loops connecting transmembrane helices provide additional contact points for signaling proteins and regulatory factors[7][47]. Intracellular loop 3 (ICL3), which connects transmembrane helices 5 and 6, contains residues D457 and K466 that directly interact with the α5-helix of heterotrimeric Gs proteins, mediating constitutive and ligand-induced G protein coupling[7][44]. The structural basis for G protein recognition involves hydrogen bonding and electrostatic interactions contributed from the C-terminal segment of the Gs α-subunit, with specific contacts between leucine residues L393 and L394 of the Gs α5-helix and FZD7 residues within the receptor core[44][47]. Recent investigations have identified conserved residues in the intracellular loops and transmembrane helices that form a "molecular switch" involving arginine 470 (R470 in position 6.32) and tryptophan 547 (W547 in position 7.55), which tightly regulates transmembrane helix 6 dynamics and receptor activation status[7][47][50].

### Cholesterol Binding and Allosteric Regulation

An emerging structural feature of FZD7 is a conserved cholesterol-binding site located within the transmembrane domain core[7][47][50]. Cryo-EM structural analysis revealed high-quality density consistent with cholesterol molecules bound at a specific allosteric site, with the primary cholesterol-binding site involving hydrophobic interactions with residues F345, H382, and W386[7][50]. This cholesterol-binding site appears to be highly conserved across the entire frizzled receptor family, suggesting functional importance beyond FZD7 alone[7][50]. Functional validation demonstrates that mutations disrupting cholesterol binding significantly impair the recruitment of DVL to FZD7, indicating that cholesterol association is critical for transducer protein interaction[7][50].

The precise mechanism by which cholesterol modulates FZD7 signaling involves allosteric effects on receptor conformation and protein-protein interactions. Molecular dynamics simulations indicate that cholesterol binding at this conserved site influences the local environment of the DVL-binding interface, enhancing the stability and affinity of DVL recruitment[7][50]. Interestingly, cholesterol binding is not required for constitutive G protein coupling activity, as FZD7 displays similar levels of Gs activation even when cholesterol-binding residues are mutated[7][50]. This distinction reveals a differential requirement for cholesterol in mediating canonical versus non-canonical signaling through FZD7, with implications for understanding how different signaling outcomes emerge from this single receptor.

## Canonical Wnt/β-Catenin Signaling Pathway

### Overview and Mechanism of Wnt/β-Catenin Pathway Activation

The canonical Wnt/β-catenin pathway represents the best-characterized Wnt signaling cascade and plays essential roles in regulating cell proliferation, survival, and gene expression programs controlling cell fate[15][18][25][28]. In the absence of Wnt ligand stimulation, the intracellular protein β-catenin is constitutively phosphorylated by a "destruction complex" composed of glycogen synthase kinase 3β (GSK3β), adenomatous polyposis coli (APC), casein kinase 1 (CK1), and axin[15][18][53][54]. The sequential phosphorylation of β-catenin by CK1 and GSK3β creates a phosphorylation pattern recognized by ubiquitin ligases, targeting β-catenin for proteasomal degradation[18][53]. This steady-state degradation maintains basal levels of β-catenin low, preventing the accumulation of this transcriptional coactivator in the nucleus[15][18][53].

When Wnt ligands are secreted and bind to FZD7's extracellular cysteine-rich domain, the receptor undergoes conformational changes that permit interaction with low-density lipoprotein receptor-related proteins 5 or 6 (LRP5/6)[15][18][25][28]. The formation of the functional Wnt receptor complex requires coordinated binding of Wnt proteins to both FZD7 and LRP5/6 co-receptors, leading to their clustering and oligomerization at the cell surface[28][34]. This multi-protein complex assembly at the plasma membrane serves as a nucleation site for the formation of the intracellular "signalosome," a dynamic assembly of signaling proteins that transduces the Wnt signal into intracellular responses[25][28][34]. The activation of the FZD7-LRP5/6 receptor complex triggers the recruitment of disheveled (DVL) proteins to the membrane through direct interactions between DVL's DEP domain and the C-terminal PDZ-binding motif of FZD7[15][26][34][53].

### DVL-Mediated Inhibition of the Destruction Complex

Once recruited to the activated FZD7-LRP5/6 complex at the membrane, DVL undergoes a conformational change and phosphorylation by multiple kinases including casein kinase 1 epsilon[15][53]. DVL functions as a critical scaffolding protein that mediates the inhibition of the β-catenin destruction complex through multiple mechanisms[15][53]. The disheveled/axin interaction domain of DVL (the DIX domain) exhibits self-polymerization properties, forming multimeric assemblies that recruit axin protein away from free β-catenin in the cytoplasm[15][25][53]. Axin represents a critical component of the destruction complex, and its sequestration by DVL oligomers reduces the local concentration of GSK3β and CK1 available to phosphorylate β-catenin[15][25][53].

The activation of LRP5/6 represents another critical level of control in the canonical pathway. Phosphorylation of LRP5/6 on specific PPPSP motifs by GSK3β is required for pathway activation, an apparently paradoxical requirement since GSK3β normally promotes pathway inhibition through β-catenin phosphorylation[25][34]. This unique arrangement occurs because DVL-mediated recruitment of axin to phosphorylated LRP5/6 facilitates a conformational change in axin that inhibits its ability to activate GSK3β-mediated phosphorylation of β-catenin[15][25][34]. Additionally, the recruitment of axin to the membrane through interactions with phosphorylated LRP5/6 prevents its assembly into the cytoplasmic destruction complex, further reducing β-catenin phosphorylation[15][25][34].

### β-Catenin Stabilization and Nuclear Translocation

As the destruction complex activity decreases in response to Wnt-FZD7-LRP5/6 signaling, unphosphorylated β-catenin begins to accumulate in the cytoplasm[15][18][25]. The stabilized β-catenin enters the nucleus through nuclear transport mechanisms mediated by importin proteins[15][18][53]. Once in the nucleus, β-catenin serves as a transcriptional coactivator, binding to members of the T cell factor/lymphoid enhancer factor (TCF/LEF) family of transcription factors[15][18][38][53]. TCF/LEF proteins contain DNA-binding domains recognizing conserved E-box sequences in the regulatory regions of Wnt target genes[15][38][53]. In the basal state, without β-catenin, TCF/LEF proteins are bound to co-repressor proteins of the Gro/TLE family, which actively repress transcription of Wnt-responsive genes[38][53].

The binding of stabilized β-catenin to TCF/LEF proteins triggers a displacement or removal of the co-repressor Gro/TLE complex from chromatin[15][38][53]. This replacement of the repressor complex with an activator complex containing β-catenin and TCF/LEF permits the recruitment of chromatin-remodeling factors and transcriptional machinery to Wnt target gene promoters[15][38][53]. The resulting transcriptional activation of Wnt target genes drives the expression of genes controlling cell proliferation (cyclin D1, c-myc), survival (survivin, BCL family members), and cell fate determination[15][18][34][53]. Among the primary Wnt target genes regulated through β-catenin-TCF/LEF signaling are the SP5 transcription factor and other Wnt pathway components, establishing positive feedback loops that amplify and sustain the Wnt signal[2][35][46].

## Non-Canonical Wnt Signaling Pathways

### Planar Cell Polarity and Rho GTPase Activation

In addition to canonical Wnt/β-catenin signaling, FZD7 transduces non-canonical Wnt signals through the planar cell polarity (PCP) pathway, which regulates cell polarity, migration, and cytoskeletal organization[14][15][27][30][40][60]. In the PCP pathway, certain Wnt ligands such as Wnt7a and Wnt5a bind to FZD receptors and activate a distinct signaling cascade involving disheveled and downstream effectors that control the orientation of cell division and coordinated cell movements[14][15][30][40]. The canonical Wnt receptor co-receptors LRP5/6 are not required for non-canonical signaling through FZD7, allowing the PCP pathway to function independently of β-catenin pathway activation[14][15][30][40].

The FZD7-mediated PCP pathway employs small GTPases of the Rho family, particularly RhoA and Rac1, as critical downstream effectors that coordinate cytoskeletal rearrangements[14][15][27][30][37][40][60]. Upon Wnt binding to FZD7, the receptor recruits DVL proteins that activate the Formin-Homology-containing protein diacylglycerol (DAG)-associated kinase 1 (DAAM1), which in turn activates RhoA and promotes the recruitment and activation of downstream effectors including ROCK kinases[14][15][37][40][60]. Activated ROCK phosphorylates myosin light chain kinase and other cytoskeletal proteins, promoting the formation and contraction of actin stress fibers and the redistribution of cellular tension[14][27][30][37][40][60]. Simultaneously, the PCP pathway activates Rac1 through distinct mechanisms involving Dvl and other adaptor proteins, promoting the assembly of lamellipodia and the formation of adhesion complexes at cell-cell junctions[14][27][30][37][40][60].

The balance between RhoA and Rac1 activities critically determines cellular phenotypes regulated by FZD7, with RhoA activation promoting migration and invasive behavior, while Rac1 activation promotes cell polarity and epithelial properties[14][27][37][40]. Indeed, investigations in ovarian cancer cells demonstrated that FZD7 knockdown leads to reciprocal inhibition of RhoA activity and activation of Rac1, resulting in decreased cell migration and increased cadherin-based cell-cell adhesion characteristic of epithelial phenotypes[27][37]. The Vangl2 protein represents another critical component of the PCP pathway that associates with FZD7 to mediate symmetric cell division of satellite stem cells, where polarized distributions of Vangl2 at opposite poles of dividing cells instruct daughter cells to adopt symmetric rather than asymmetric fates[14][56][60].

### Wnt/Calcium Signaling Pathway

The Wnt/calcium (Ca2+) pathway represents another non-canonical signaling mechanism activated through FZD7 in response to certain Wnt ligands such as Wnt5a and Wnt11[15][18][30][34]. In this pathway, FZD7-mediated signaling through heterotrimeric G proteins triggers activation of phospholipase C (PLC), which cleaves phosphatidylinositol 4,5-bisphosphate (PIP2) into two second messengers: inositol 1,4,5-trisphosphate (IP3) and diacylglycerol (DAG)[15][18][30][34]. IP3 diffuses through the cytoplasm and binds to IP3 receptors on the endoplasmic reticulum membrane, triggering the release of calcium stores into the cytoplasm[15][18][30][34]. The elevation of intracellular calcium concentration subsequently activates calcium-dependent protein kinases including calmodulin-dependent kinase II (CaMKII) and protein kinase C (PKC), which phosphorylate downstream targets controlling gene expression and cellular behavior[15][18][30][34].

The Wnt/Ca2+ pathway typically opposes β-catenin signaling, as increased intracellular calcium activates the calcium/calmodulin-dependent phosphatase calcineurin, which dephosphorylates transcription factors such as NFAT that compete with β-catenin-TCF complexes for target gene regulation[15][30][34]. Additionally, calcium-activated kinases including PKC and CaMKII phosphorylate TCF/LEF transcription factors, promoting their phosphorylation-dependent sequestration and reducing their ability to activate canonical Wnt target genes[15][30][34]. This mutual antagonism between canonical and non-canonical Wnt pathways provides a regulatory mechanism ensuring that cells adopt distinct programs appropriate to Wnt ligand identity and developmental context[15][30][34].

## FZD7 in Stem Cell Biology and Maintenance of Pluripotency

### Essential Role in Human Embryonic Stem Cell Self-Renewal

FZD7 occupies a uniquely important position in regulating the undifferentiated state of human embryonic stem cells (hESCs), where it maintains the expression of pluripotency-associated transcription factors including octamer-binding transcription factor 4 (OCT4, also known as POU5F1) and NANOG[2][35][39][46]. Gene expression profiling studies revealed that FZD7 mRNA levels in undifferentiated hESCs are approximately 200-fold higher than in differentiated cell types, indicating high-level expression specifically in the pluripotent state[39]. Functional studies using both RNA interference-mediated knockdown and FZD7-specific blocking antibodies (Fab fragments) demonstrated that disruption of FZD7 function leads to rapid loss of pluripotency markers, morphological changes in ESC colony organization, and differentiation into various germ layers[2][35][39][46].

The pluripotency-maintaining function of FZD7 depends on an endogenous Wnt signaling loop operating within hESC populations[2][35][46]. Treatment of hESCs with FZD7-blocking antibodies leads to down-regulation of FZD7 protein levels through receptor internalization and subsequent degradation, preventing Wnt ligand engagement and disrupting baseline Wnt/β-catenin signaling[2][35][46]. The endogenous ligand for FZD7 in hESCs appears to be Wnt3 or a closely related canonical Wnt protein, as FZD7-blocking antibodies specifically inhibit signaling by Wnt3a in this context while leaving other Wnt-dependent signaling pathways intact[2][35][46]. The basal level of Wnt/β-catenin signaling through FZD7 appears to be relatively low compared to the high-level signaling triggered by exogenous Wnt3a application, suggesting that a carefully titrated, constitutive Wnt signal maintains pluripotency genes without triggering differentiation[2][35][46].

Cell surface sorting studies using fluorescence-activated cell sorting (FACS) revealed that hESC populations naturally segregate into FZD7-high and FZD7-low cell populations, with the FZD7-high population substantially enriched for expression of pluripotency markers including NANOG, OCT4, and the pluripotency-associated long non-coding RNA linc-ROR[35][46]. This heterogeneity within hESC populations suggests that FZD7 expression level correlates with and may actively promote the undifferentiated pluripotent state, with FZD7-high cells occupying a position at the top of a potential hierarchy of pluripotency states[35][46]. The functional requirement for FZD7 in this context is selective, as other Wnt receptors including FZD2, FZD3, and FZD5 are also expressed in hESCs but appear to mediate distinct functions, with FZD5 and FZD3 potentially transducing mesendodermal differentiation signals rather than pluripotency maintenance[2][35][46].

### Selective FZD7 Activation Promotes Mesendodermal Differentiation

Despite FZD7's critical role in pluripotency maintenance, the receptor also functions to promote cell fate transitions when activated at higher ligand concentrations or through selective signaling mechanisms[3][32][41][55]. The development of FZD7-selective agonist molecules, particularly the bispecific antibody F7L6 that exclusively engages FZD7 and LRP6 without activating other frizzled receptors, permitted precise dissection of FZD7's role in directed differentiation of hESCs[3][32][55]. Treatment of hESCs with selective FZD7 agonists initiates transcriptional programs analogous to those occurring during primitive streak formation and mesendoderm specification in early embryonic development[3][32][55]. The selectivity of F7L6 for FZD7 contrasts with the native Wnt3a ligand, which can engage multiple frizzled receptors and LRP5/6 co-receptors, permitting clearer understanding of FZD7's specific role in mesodermal and endodermal specification[3][32][55].

Single-cell RNA-sequencing and bulk transcriptomic analyses revealed that FZD7 activation through F7L6 triggers a distinct transcriptional cascade compared to activation of other frizzled receptors including FZD2[41][55]. FZD7 stimulation specifically upregulates genes associated with lateral mesoderm and cardiac mesoderm lineages, including HAND1, ISL1, NKX2.5, and importantly, bone morphogenetic protein 4 (BMP4)[41][55]. The induction of BMP4 expression represents a key mechanistic distinction between FZD7 and FZD2 activation, as BMP4 signaling independently promotes lateral mesoderm specification through Smad1/5/8 phosphorylation and gene expression programs distinct from β-catenin-mediated transcription[41][55]. These findings establish that while FZD7 operates through the canonical Wnt/β-catenin pathway in both pluripotency maintenance and mesendodermal specification, the intensity and kinetics of β-catenin signaling, combined with receptor-selective effects on non-canonical pathways, determine distinct cellular outcomes[41][55].

### FZD7 in Skeletal Muscle Stem Cell Biology

Beyond its roles in embryonic stem cells, FZD7 functions as a critical regulator of skeletal muscle satellite stem cells, a population of quiescent progenitor cells residing between the myocyte and the basal lamina[14][56][59][60]. Satellite stem cells express markedly elevated levels of FZD7 compared to committed myogenic progenitors, with FZD7 specifically enriched in the Pax7+/YFP− quiescent satellite stem cell population rather than the Pax7+/YFP+ population of differentiating satellite myogenic cells[14][56][59][60]. The Wnt7a ligand, produced during muscle regeneration and injury, serves as a natural activator of FZD7 signaling in satellite cells, triggering a non-canonical Wnt pathway through the planar cell polarity components Vangl2 and Rac1[14][56][59][60].

Wnt7a-FZD7 signaling in satellite cells operates through the planar cell polarity pathway to control the symmetry of satellite cell divisions, promoting symmetric division that expands the satellite stem cell pool rather than asymmetric division that generates differentiated progeny[14][56][59][60]. In response to Wnt7a stimulation, Vangl2 becomes polarized to opposite poles of dividing satellite cells, coordinating symmetric cell division and the retention of both daughter cells within the quiescent stem cell niche[14][56][59][60]. Parallel to PCP pathway activation, Wnt7a-FZD7 signaling directly activates the AKT/mammalian target of rapamycin (mTOR) pathway in myofibers, inducing myofiber hypertrophy through anabolic processes independent of satellite cell expansion[59][60]. The net result of Wnt7a-FZD7 signaling is a coordinated program of regenerative myogenesis in which satellite stem cells expand through symmetric division while muscle fibers undergo hypertrophic growth, substantially accelerating muscle regeneration following injury[59][60].

## FZD7 in Vascular Development and Angiogenesis

### Role in Endothelial Cell Function and Retinal Vascular Formation

FZD7 expressed by endothelial cells plays a critical and specific role in postnatal angiogenesis, particularly in the development of the retinal vascular network[13][16][33][36]. Studies utilizing transgenic mice with conditional deletion of FZD7 specifically in endothelial cells (fzd7^ECKO^ mice) demonstrated that FZD7 is essential for proper postnatal vascular formation, with FZD7-deficient endothelial cells exhibiting impaired tip cell phenotype and reduced stalk cell proliferation[13][16][33][36]. Retinal vascular plexus formation was delayed in FZD7-deficient endothelial cells, with reduced vessel density and altered vascular patterning compared to wild-type controls[13][16][33][36]. The tip cells, which are the leading migratory cells extending nascent vascular sprouts during angiogenesis, demonstrated reduced motility and migratory capacity in the absence of FZD7, while supporting stalk cells showed decreased proliferation and participation in new vessel formation[13][16][33][36].

The mechanism by which FZD7 promotes angiogenesis operates through canonical Wnt/β-catenin signaling in endothelial cells, with FZD7 functioning upstream of the Notch signaling pathway[13][16][33][36]. Genetic and pharmacological rescue strategies using lithium chloride treatment, which activates Wnt/β-catenin signaling downstream of FZD7, restored impaired tip and stalk cell phenotypes in FZD7-deficient endothelial cells, demonstrating that β-catenin activation is necessary for FZD7-mediated angiogenesis[13][16][33][36]. Furthermore, deletion of disheveled proteins (Dvl1/3) in endothelial cells produced a vascular phenotype identical to that observed in FZD7-deficient mice, confirming that DVL-mediated signal transduction is required for FZD7-dependent angiogenesis[13][16][33][36].

FZD7-mediated Wnt/β-catenin signaling in endothelial cells controls the expression of Notch pathway ligands including Delta-like ligand 4 (Dll4) and Jagged1, which are essential for proper arterial-venous differentiation and vascular patterning[13][16][33][36]. The Notch pathway operates downstream of β-catenin signaling to regulate the lateral inhibition of tip cell fate, ensuring that not all endothelial cells simultaneously adopt the migratory tip cell phenotype[13][16][33][36]. β-catenin-dependent transcription of Notch pathway components provides the mechanistic link between FZD7 signaling and the subsequent Notch-mediated specification of vascular cell fates[13][16][33][36]. This hierarchical arrangement of signaling pathways, with FZD7-Wnt-β-catenin upstream of Notch signaling, ensures coordinated control of endothelial cell behavior during angiogenesis and vascular development.

## FZD7 Dysregulation in Human Malignancies

### Overexpression and Activation in Colorectal Cancer

FZD7 represents the most frequently overexpressed frizzled receptor in colorectal cancer (CRC), identified as being upregulated in the epithelial tissues of colonic crypts where CRC initiates[34][39][42][43][54]. The predominantly expressed member of the frizzled family in colon epithelium, FZD7 becomes further amplified in colorectal cancer cells, particularly those harboring APC or CTNNB1 (β-catenin) gene mutations[31][34][39][54]. The canonical Wnt signaling pathway is constitutively active in the vast majority of human colorectal cancers, with approximately 80% of CRCs harboring loss-of-function mutations in the APC tumor suppressor gene that normally limits Wnt signaling[31][34][39][54]. Despite this genetic basis for pathway activation, FZD7 is frequently overexpressed in APC-mutant CRC cells, and genetic studies demonstrated that FZD7 remains critical for efficient Wnt/β-catenin pathway activation even in the presence of APC mutations[31][34][39][54].

The functional importance of FZD7 in CRC progression is demonstrated through studies employing FZD7-specific RNA interference knockdown in colorectal cancer cell lines. FZD7 knockdown in HCT-116 cells (which harbor CTNNB1 mutations) and in multiple other CRC cell lines with APC mutations reduced TCF transcriptional activity to 20-80% of control levels, demonstrating a substantial dependence on FZD7 for β-catenin-mediated transcription despite constitutive pathway activation from APC loss[31][34][39][54]. Moreover, FZD7 knockdown significantly decreased cell viability and in vitro invasion activity in CRC cells, with liver metastasis of FZD7-knockdown cells reduced to 40-50% relative to control cells in SCID mouse models[31][34][39][54]. These findings establish that even CRC cells with constitutively activated Wnt signaling from genetic mutations retain a substantial functional dependence on FZD7, making FZD7 an attractive therapeutic target in this disease[31][34][39][54].

### FZD7 in Hepatocellular Carcinoma and HCC Stem Cells

FZD7 expression becomes elevated in hepatocellular carcinoma (HCC), with 60-90% of human HCC cells and mouse HCC models displaying upregulation of FZD7 along with increased expression of Wnt ligands, particularly Wnt3[34][39][54]. The functional interaction between Wnt3 and FZD7 in HCC cells activates canonical Wnt/β-catenin signaling, with co-immunoprecipitation experiments demonstrating direct physical association between Wnt3 and FZD7[5][34][39][54]. FZD7-mediated Wnt3 signaling correlates with increased cytosolic and nuclear accumulation of β-catenin and enhanced cell migration in HCC cells, establishing a functional link between FZD7 expression and HCC progression[34][39][54]. Notably, hepatitis B and C virus infection, major risk factors for HCC development, induce upregulation of both Wnt ligands and FZD7 expression, suggesting that viral transformation processes activate FZD7-mediated Wnt signaling as part of the carcinogenic cascade[34][39][54].

FZD7 expression marks populations of cancer stem cells within HCC that display enhanced tumor-initiating capacity and therapeutic resistance[19][34][39]. HCC cells with high FZD7 expression demonstrate increased clonogenicity, enhanced sphere-forming capacity, and enhanced ability to generate heterogeneous tumors in orthotopic transplantation assays[6][19][34][39]. The enrichment of FZD7 expression in cancer stem cells of multiple tumor types suggests that FZD7 drives or maintains stem cell properties through mechanisms involving Wnt signaling-dependent control of self-renewal versus differentiation decisions[6][19][34][39]. Pharmacological inhibition of FZD7 with small interfering peptides that disrupt the interaction between FZD7 and DVL (the KTLQSW motif-containing peptides) displayed anti-tumor effects in HCC models, reducing cell viability through both β-catenin degradation and activation of the PKCδ kinase[34][39][54].

### FZD7 in Triple-Negative Breast Cancer and Other Malignancies

FZD7 is upregulated in triple-negative breast cancer (TNBC), a subtype lacking expression of estrogen receptor, progesterone receptor, and HER2, representing approximately 15-20% of all breast cancers with particularly aggressive clinical behavior[34][39][54]. FZD7 modulates TNBC cell tumorigenesis through canonical Wnt signaling pathway activation, with shRNA knockdown of FZD7 significantly decreasing TNBC Wnt/β-catenin signaling and subsequent cell proliferation, migration in vitro, and tumor growth in vivo[34][39][54]. The sustained activation of non-canonical Wnt/Ca2+ signaling in TNBC cells promotes tumor cell migration and invasion through mechanisms involving prolonged receptor internalization and recycling that maintain Wnt/Ca2+ activity in these highly invasive cells[15][34][39][54].

FZD7 also becomes elevated in ovarian cancer, particularly in the Stem-A molecular subgroup characterized by high expression of stemness-related genes and poor clinical prognosis[17][27][37]. FZD7 knockdown in Stem-A ovarian cancer cell lines reduced cell proliferation through G0/G1 cell cycle arrest, altered actin cytoskeletal organization, and decreased directional cell migration through coordinated effects on RhoA and Rac1 small GTPases[27][37]. In glioblastoma multiforme (GBM), the most aggressive primary brain tumor, high FZD7 expression correlates with advanced tumor stage and poor overall survival[42][57][60]. FZD7 overexpression in glioma cells promotes proliferation through upregulation of the TAZ (transcriptional coactivator with PDZ-binding motif), a Hippo pathway effector that drives transcription of proliferation and survival genes[57][60]. Additionally, Wnt/PCP signaling components including FZD7 and Vangl1 form a complex at the leading edge of migratory GBM cells, promoting cellular migration, invasiveness, and the acquisition of mesenchymal phenotypes[60].

## Therapeutic Targeting of FZD7

### Small Molecule Inhibitor Development

Recent advances in structure-based drug discovery have enabled the identification of small molecule ligands targeting the transmembrane domain of FZD7, providing alternatives to antibody-based therapeutic approaches[8][9][10][11]. Rather than targeting the extracellular cysteine-rich domain where Wnt proteins bind, these small molecule inhibitors bind deep within the transmembrane domain core, acting as negative allosteric modulators (NAMs) that prevent Wnt-induced conformational dynamics and signal transduction[8][9][10][11]. Computational docking screens of large chemical libraries against the FZD7 transmembrane domain identified compound C45, which displaced tracer ligands with a pIC50 of 4.58 ± 0.09, and the more potent compound C407 with improved binding characteristics (pIC50 = 4.86 ± 0.04)[8][9].

Structural studies and molecular dynamics simulations revealed that C407 binds deep within the transmembrane domain at a specific allosteric site predicted through docking calculations, with mutations in key binding site residues including Y489 completely abrogating the compound's effects on Wnt-3A-induced signaling[8][9]. The identification of this transmembrane allosteric binding site reveals a previously untapped region for FZD7 modulation, distinct from the extracellular CRD-targeting antibodies and soluble receptor ectodomains[8][9]. Importantly, most FZD7 transmembrane domain binding site residues are highly conserved across the frizzled receptor family, suggesting that compounds derived from C407 may also target other FZD receptors, potentially providing either multi-target activity or selectivity through fine-tuning[8][9][10][11].

Earlier structure-guided drug discovery efforts identified compound F7H as an FZD7 antagonist with an IC50 of 1.25 ± 0.38 μM through screening of large chemical libraries against homology-modeled FZD7-transmembrane domain structures[9][11]. Computational studies including molecular docking, molecular dynamics simulations, and free energy perturbation calculations delineated the binding pocket formed by residues from transmembrane helices I, III, VI, and VII, along with contributions from extracellular loops, creating hydrophobic cores at both the top and bottom regions of the binding site[10][11]. The identification of conserved residues forming this binding site across the frizzled family suggests that targeting FZD-TMD may represent a generalizable approach to inhibiting multiple frizzled receptors across different cancer types[10][11].

### Antibody-Based Therapeutic Approaches

Monoclonal antibodies and engineered antibody fragments targeting FZD7 have been developed for therapeutic evaluation in multiple cancer settings[29][31][34][39][54]. The FZD7-specific blocking antibody vantictumab demonstrated anti-tumor activity in gastric cancer models, with genetic deletion of FZD7 or vantictumab treatment sufficient to inhibit tumor growth[42]. FZD7-blocking antibodies function through multiple mechanisms including direct blockade of Wnt ligand binding, although most antibodies do not directly compete with Wnt for FZD7 binding but rather induce FZD7 internalization and subsequent degradation through lysosomal or proteasomal pathways[2][29][34][39][46][54]. This internalization-mediated mechanism of action represents a distinct advantage in some contexts, as it removes FZD7 from the cell surface and prevents re-activation of signaling even if antibodies temporarily dissociate from receptors[2][34][46].

A clinical challenge associated with FZD7 antibody therapy involves development of potential resistance mechanisms if internalized FZD7 is recycled back to the cell surface after antibody clearance[29][34][39][54]. To address this limitation, combination strategies pairing FZD7-blocking antibodies with other chemotherapeutic agents have shown promise, combining immediate anti-proliferative effects of traditional chemotherapy with sustained blockade of Wnt signaling provided by FZD7 inhibition[34][39][54]. In Wilms tumor, a pediatric renal malignancy in which FZD7 marks stem cell populations, FZD7-blocking antibodies abrogated sphere-formation and clonogenic capacity of tumor cells sensitive to FZD7 inhibition, though some tumors retained FZD7-resistance phenotypes characterized by diminished FZD7 expression and heightened dependence on alternative Wnt receptors or signaling pathways[34][39][54].

### Disruption of Protein-Protein Interactions

An alternative therapeutic approach targets the critical PDZ domain-mediated interaction between FZD7 and DVL, rather than blocking ligand binding or inducing receptor internalization[29][34][39][54]. Membrane-permeable small interfering peptides containing the KTLQSW PDZ-binding motif of FZD7 compete with endogenous FZD7 for DVL binding, disrupting the formation of the FZD7-DVL signaling complex[29][34][39][54]. These peptides effectively inhibited Wnt/β-catenin signaling in HCC cells and displayed in vivo anti-tumor effects in transgenic HCC mouse models[29][34][39][54]. Similarly, the small molecule compound FJ9 disrupts the PDZ domain interaction between FZD7 and DVL, displaying β-catenin-dependent anti-cancer activities including induction of apoptosis in melanoma and lung cancer cell lines and attenuation of tumor growth in xenograft models[29][34][39][54].

### Extracellular Domain Targeting and Soluble Receptors

The extracellular cysteine-rich domain of FZD7 has been developed as a therapeutic agent through expression of soluble FZD7 ectodomains (sFZD7) that compete with membrane-anchored FZD7 for Wnt ligand binding[29][34][39][54]. The soluble FZD7-CRD potently inhibits Wnt/β-catenin signaling through competitive binding with Wnt3, effectively sequestering Wnt ligands and preventing their engagement with full-length FZD7 receptors[29][34][39][54]. Transfection of plasmids expressing the FZD7 extracellular domain induced morphological changes and attenuated tumor growth in colon cancer cell lines, and the FZD7 extracellular domain has shown potent inhibitory effects on APC-mutant CRC tumor cell growth in mouse xenograft models[30][31][34][39][54]. This approach leverages the natural Wnt-binding properties of the FZD7-CRD without requiring generation of modified antibodies or small molecules, though systemic administration of soluble FZD7-CRD may be complicated by rapid turnover and potential immune reactions to the protein.

## Recent Structural and Mechanistic Insights

### Cryo-EM Structures Revealing FZD7 Activation Mechanism

High-resolution cryo-electron microscopy structures of FZD7 in both inactive and G protein-coupled active conformations have provided unprecedented mechanistic insights into FZD7 activation and signal transduction[7][44][47][50]. The cryo-EM structure of inactive FZD7, determined at 1.9 Å resolution without stabilizing mutations, reveals a compact transmembrane bundle with limited conformational flexibility compared to classical GPCRs[7][47][50]. The inactive FZD7 structure shows that the transmembrane core maintains a relatively stable conformation even in the apo state, with a narrow bottleneck between internal cavities permitting water exchange but not large-scale ligand-induced rearrangements typical of many other GPCR classes[7][47][50]. This structural organization differs notably from GPCRs such as the β-adrenergic receptors, which undergo substantial transmembrane helix displacement upon activation and G protein coupling[7][44][47].

Comparison of inactive FZD7 with the FZD7-mGs protein-coupled complex reveals limited conformational rearrangements during G protein coupling, with the most significant changes occurring at intracellular loops 1 and 3 that directly contact the Gs α-subunit[7][44][47][50]. The molecular switch formed by R470 (position 6.32) and W547 (position 7.55) exhibits only an 11° rotation in transmembrane helix 6, substantially less than the transmembrane helix movements observed during activation of other GPCR classes[7][47][50]. This limited TM6 dynamics in FZD7 represents a fundamental distinction from classical GPCRs and may explain the relatively poor G protein coupling efficiency of frizzled receptors compared to other GPCR classes, with DVL functioning as the preferred intracellular transducer[7][47][50].

### Allosteric Regulation Through Cholesterol and Lipid Interactions

Cryo-EM structures captured cholesterol molecules bound at a highly conserved allosteric site within the FZD7 transmembrane domain, providing structural basis for understanding lipid-mediated regulation of FZD signaling[7][47][50]. The primary cholesterol-binding site involves specific hydrophobic interactions with residues F345, H382, and W386, with the bound cholesterol positioned to influence the conformation of the DVL-binding interface at the intracellular surface[7][50]. Mutagenesis studies demonstrated that disruption of this cholesterol-binding site through F345A-H382A or F345A-W386A double mutations completely ablated FZD7-mediated recruitment of the DEP domain of DVL, a critical early step in signal transduction through the canonical pathway[7][50].

Notably, the same cholesterol-binding mutations did not impair constitutive G protein coupling activity, indicating differential requirements for cholesterol in mediating canonical versus non-canonical signaling[7][50]. This distinction reveals that while cholesterol is essential for DVL recruitment and canonical β-catenin pathway activation, constitutive Gs activation by FZD7 can proceed independently of cholesterol binding[7][50]. The conservation of the cholesterol-binding site across all frizzled family members suggests that lipid-mediated allosteric regulation represents a general mechanism for controlling FZD signaling, potentially linking cellular lipid composition and membrane organization to Wnt pathway activity[7][47][50].

### Wnt Ligand Specificity and Binding Preferences

Structure-based computational approaches combined with quantitative binding measurements have revealed selective binding preferences among different FZD receptors for various Wnt ligands[43][53]. FZD7 displays relatively selective binding affinity for specific Wnt ligands compared to other FZD family members with broad ligand affinity[43]. Homology modeling of Wnt-FZD cysteine-rich domain interactions and structure-activity relationship studies predicted that FZD7 exhibits high affinity for Wnt10a and selective binding to a subset of Wnt ligands rather than promiscuous engagement of all Wnt family members[43][53]. The structural basis for this selectivity involves variations in the hydrophobic pocket and hydrogen bonding networks within individual FZD-CRDs that preferentially stabilize binding of certain Wnt proteins over others[43][53].

The ligand specificity of FZD7 has important functional implications, as the identity of Wnt ligands engaging FZD7 can determine whether canonical or non-canonical signaling pathways are preferentially activated[43][53][55]. For example, Wnt3 signaling through FZD7 activates canonical β-catenin signaling supporting pluripotency maintenance in hESCs[2][35][46], while Wnt7a signaling through FZD7 activates non-canonical PCP pathway signaling controlling satellite stem cell expansion in muscle[14][56][59][60]. The molecular basis for this selectivity may involve not only the initial Wnt-FZD7-CRD interaction but also subsequent recruitment of distinct LRP5/6 co-receptors and intracellular adaptor proteins that determine pathway utilization[43][53][55].

## Conclusion

FZD7 stands as a central mediator of Wnt signal transduction whose diverse roles encompass stem cell biology, developmental morphogenesis, tissue homeostasis, and malignant transformation. The structural architecture of FZD7, combining an extracellular cysteine-rich domain for Wnt ligand recognition with a seven-transmembrane helical core capable of transducing both canonical and non-canonical Wnt signals, provides a sophisticated platform for integrating diverse cellular inputs into coordinated biological responses. The discovery of conserved allosteric binding sites for cholesterol and the identification of specific molecular switches controlling transmembrane helix dynamics have revealed previously unappreciated regulatory mechanisms governing FZD7 activation and signal transduction. FZD7's critical role in maintaining human embryonic stem cell pluripotency through baseline Wnt/β-catenin signaling, while simultaneously promoting directed mesendodermal differentiation when activated at elevated ligand concentrations, exemplifies how a single receptor can generate distinct biological outputs through quantitative and kinetic modulation of signaling intensity. The selective activation of FZD7 to promote lateral mesoderm specification, compared to FZD2 activation promoting paraxial mesoderm, reveals functional specialization among frizzled receptors despite sharing the canonical Wnt signaling pathway[41].

In regenerative medicine and tissue biology, FZD7 emerges as a critical therapeutic target whose modulation can enhance skeletal muscle regeneration through coordinated expansion of satellite stem cells and myofiber hypertrophy. The Wnt7a-FZD7-planar cell polarity signaling axis controlling symmetric satellite cell expansion represents a paradigm for leveraging developmental signaling pathways to potentiate tissue regeneration, with demonstrated efficacy in improving outcomes of myogenic cell transplantation therapy for dystrophic muscles. In vascular biology, FZD7 expressed by endothelial cells drives postnatal angiogenesis through β-catenin-mediated control of Notch pathway signaling, establishing hierarchical pathway relationships essential for proper vessel formation. The dysregulation of FZD7 in multiple human malignancies—including colorectal cancer, hepatocellular carcinoma, triple-negative breast cancer, ovarian cancer, and glioblastoma—identifies FZD7 as a nearly universal component of cancer stem cell programs and malignant transformation[34][39][42][54]. The functional dependence of even genetically mutated cancer cells (APC-mutant colorectal cancers and CTNNB1-mutant cancers) on FZD7 for efficient pathway activation establishes this receptor as a critical nodal point in Wnt signaling potentially amenable to therapeutic intervention[31][34][39][54].

Recent therapeutic developments targeting FZD7 through small molecule transmembrane domain inhibitors, blocking antibodies, protein-protein interaction disruptors, and soluble receptor ectodomains provide multiple complementary approaches to inhibiting FZD7-dependent pathways in disease contexts[8][9][10][11][29][34][39][54]. The identification of negative allosteric modulator sites deep within the FZD7 transmembrane domain opens new opportunities for selective modulation of FZD7 signaling without the complete receptor blockade that might impair developmentally essential functions. Future therapeutic development should prioritize understanding of how individual Wnt ligands differentially engage FZD7 to activate distinct downstream pathways, enabling selective inhibition of pathological (non-canonical) signaling while preserving beneficial canonical pathway functions in normal tissues. The structural insights revealing cholesterol-binding sites essential for DVL recruitment but dispensable for G protein coupling suggest opportunities for selective modulation of different FZD7 signaling outputs. As research continues to clarify FZD7's roles in normal physiology and disease pathogenesis, this transmembrane Wnt receptor will likely become an increasingly important therapeutic target in cancer, regenerative medicine, and developmental diseases.

## Citations

1. https://www.ncbi.nlm.nih.gov/gene/8324
2. https://www.pnas.org/doi/10.1073/pnas.1323697111
3. https://pmc.ncbi.nlm.nih.gov/articles/PMC7759383/
4. https://www.uniprot.org/uniprotkb/O75084/entry
5. https://pmc.ncbi.nlm.nih.gov/articles/PMC2390890/
6. https://www.pnas.org/doi/10.1073/pnas.2522465122
7. https://www.nature.com/articles/s41467-024-51664-4
8. https://www.nature.com/articles/s41467-025-67147-z
9. https://pubs.acs.org/doi/10.1021/acs.jmedchem.2c01795
10. https://pmc.ncbi.nlm.nih.gov/articles/PMC5710937/
11. https://pubmed.ncbi.nlm.nih.gov/37669317/
12. https://www.uniprot.org/uniprotkb/Q9PUK8/entry
13. https://pubmed.ncbi.nlm.nih.gov/27758766/
14. https://pmc.ncbi.nlm.nih.gov/articles/PMC2743383/
15. https://pmc.ncbi.nlm.nih.gov/articles/PMC12078226/
16. https://www.ahajournals.org/doi/10.1161/ATVBAHA.116.307926?doi=10.1161%2FATVBAHA.116.307926
17. https://pubmed.ncbi.nlm.nih.gov/25032869/
18. https://www.nature.com/articles/s41392-025-02142-w
19. https://pmc.ncbi.nlm.nih.gov/articles/PMC12503320/
20. https://pmc.ncbi.nlm.nih.gov/articles/PMC4748333/
21. https://www.proteinatlas.org/ENSG00000155760-FZD7
22. https://www.proteinatlas.org/ENSG00000155760-FZD7/subcellular
23. https://portlandpress.com/bioscirep/article/36/1/e00296/56517/Sorting-nexin-27-interacts-with-Fzd7-and-mediates
24. https://pubmed.ncbi.nlm.nih.gov/11287199/
25. https://pmc.ncbi.nlm.nih.gov/articles/PMC8134664/
26. https://reactome.org/content/detail/R-HSA-1504188
27. https://pmc.ncbi.nlm.nih.gov/articles/PMC4123093/
28. https://www.nature.com/articles/s41467-025-60096-7
29. https://pmc.ncbi.nlm.nih.gov/articles/PMC3268941/
30. https://pmc.ncbi.nlm.nih.gov/articles/PMC4880867/
31. https://pmc.ncbi.nlm.nih.gov/articles/PMC2435005/
32. https://elifesciences.org/articles/63060
33. https://pmc.ncbi.nlm.nih.gov/articles/PMC3910637/
34. https://www.nature.com/articles/cddis2014302
35. https://www.nature.com/articles/ncomms6368
36. https://genesdev.cshlp.org/content/17/2/295.long
37. https://pmc.ncbi.nlm.nih.gov/articles/PMC11864152/
38. https://pmc.ncbi.nlm.nih.gov/articles/PMC5500790/
39. https://www.nature.com/articles/s41422-021-00525-6
40. https://pmc.ncbi.nlm.nih.gov/articles/PMC7905944/
41. https://pmc.ncbi.nlm.nih.gov/articles/PMC11358414/
42. https://www.nature.com/articles/s41467-025-64129-z
43. https://www.science.org/doi/10.1126/scisignal.adv1529
44. https://www.cellomicstech.com/product/6519/fzd7-full-length-orf-human-gene-rfp-lentivirus
45. https://pubmed.ncbi.nlm.nih.gov/41086253/
46. https://pmc.ncbi.nlm.nih.gov/articles/PMC3987134/
47. https://pmc.ncbi.nlm.nih.gov/articles/PMC5349891/
48. https://pubmed.ncbi.nlm.nih.gov/33331818/
49. https://www.pnas.org/doi/10.1073/pnas.1215765109
50. https://pmc.ncbi.nlm.nih.gov/articles/PMC10582999/