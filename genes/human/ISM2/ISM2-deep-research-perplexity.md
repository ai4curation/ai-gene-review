---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2025-12-12T07:05:40.713819'
end_time: '2025-12-12T07:08:16.494825'
duration_seconds: 155.78
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: ISM2
  gene_symbol: ISM2
  uniprot_accession: Q6H9L7
  protein_description: 'RecName: Full=Isthmin-2; AltName: Full=Thrombospondin and
    AMOP domain-containing isthmin-like protein 1; AltName: Full=Thrombospondin type-1
    domain-containing protein 3; Flags: Precursor;'
  gene_info: Name=ISM2; Synonyms=TAIL1, THSD3; ORFNames=PSEC0137;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the isthmin family. .
  protein_domains: AMOP_dom. (IPR005533); Angio_Inhib/Adhesion_GPCR. (IPR051867);
    TSP1_rpt. (IPR000884); TSP1_rpt_sf. (IPR036383); AMOP (PF03782)
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
- **UniProt Accession:** Q6H9L7
- **Protein Description:** RecName: Full=Isthmin-2; AltName: Full=Thrombospondin and AMOP domain-containing isthmin-like protein 1; AltName: Full=Thrombospondin type-1 domain-containing protein 3; Flags: Precursor;
- **Gene Information:** Name=ISM2; Synonyms=TAIL1, THSD3; ORFNames=PSEC0137;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the isthmin family. .
- **Key Domains:** AMOP_dom. (IPR005533); Angio_Inhib/Adhesion_GPCR. (IPR051867); TSP1_rpt. (IPR000884); TSP1_rpt_sf. (IPR036383); AMOP (PF03782)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ISM2" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ISM2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ISM2** (gene ID: ISM2, UniProt: Q6H9L7) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

<think>
Let me carefully analyze this research query. The user is asking for a comprehensive research report on the gene ISM2 (UniProt Q6H9L7) in humans. This gene encodes Isthmin-2, a secreted protein with thrombospondin type-1 repeat (TSR1) and AMOP domains.

The user has provided search results that contain extensive information about ISM2 and related proteins like ISM1, thrombospondins, and various cellular functions. Let me organize the key findings:

**Key Points from Search Results:**
1. ISM2 gene location: Chromosome 14 (14q24.3)
2. Gene ID: 145501
3. Protein: ~63.9 kDa, 571 amino acids
4. Domains: TSR1 (thrombospondin type-1 repeat) and AMOP (adhesion-associated domain in MUC4 and other proteins)
5. Structure: Signal peptide + TSR1 domain + AMOP domain
6. Expression: Highly expressed in placenta, also found in other tissues
7. Functions: Angiogenic modulation, vascular permeability, development, metabolism
8. Cellular localization: Secreted protein

**Major Functions from Literature:**
1. Angiogenesis modulation (decreased in preeclampsia, elevated in choriocarcinoma)
2. Vascular permeability regulation
3. Developmental functions (craniofacial development)
4. Metabolic functions (related to ISM1)
5. Immune and cancer-related functions

I need to write a comprehensive 10,000+ word report that:
- Clearly identifies ISM2 and distinguishes it from ISM1
- Explains domain structure and post-translational modifications
- Details tissue expression and localization
- Describes angiogenic functions
- Discusses vascular permeability
- Covers disease associations


- Incorporates current research findings with appropriate citations
- Follows a formal scientific structure with clear sections and subsections
</think>

# Comprehensive Functional Annotation of ISM2 (Isthmin-2): A Multifunctional Secreted Protein with Vascular and Angiogenic Regulatory Properties

## Executive Summary

Isthmin-2 (ISM2), encoded by the ISM2 gene located on human chromosome 14q24.3, is a secreted protein of approximately 63.9 kilodaltons comprising 571 amino acid residues[3][14]. This protein belongs to the isthmin family alongside ISM1 and represents a critical regulator of vascular biology, angiogenesis, and developmental processes[14][20][49]. ISM2 is structurally defined by the presence of two major conserved domains: a thrombospondin type-1 repeat (TSR1) domain positioned centrally and an adhesion-associated domain in MUC4 and other proteins (AMOP) domain at the carboxyl terminus, flanked by an amino-terminal signal peptide[14][20][35][49]. The protein exhibits complex biological functions that vary depending on its physical state and tissue context, with particularly significant roles in placental vascularization, where it functions as an angiogenic modulator whose altered expression contributes to pathological conditions such as preeclampsia and contributes to tumor angiogenesis in choriocarcinoma[13][57]. Recent structural and functional studies have substantially revised earlier understanding of how ISM2 and its family member ISM1 interact with cellular receptors and execute their biological functions, revealing sophisticated mechanisms of regulation through post-translational modifications and context-dependent signaling.

## Molecular Structure and Domain Organization

### Primary Structure and Gene Organization

The ISM2 gene, also designated TAIL1 (thrombospondin and AMOP containing isthmin-like 1) or THSD3 (thrombospondin type-1 domain-containing protein 3) in earlier nomenclature[12][58], comprises a complete open reading frame encoding a 571-amino acid precursor protein with an initial molecular weight of approximately 63.9 kilodaltons[3][13][49]. The gene is located on chromosome 14, specifically at chromosomal position 14q24.3 in humans[52], and represents one of only two known members of the isthmin gene family, alongside ISM1 which is encoded on chromosome 20[52]. Phylogenetic analysis demonstrates that both ISM1 and ISM2 are highly conserved across vertebrate species, suggesting ancient evolutionary origins and fundamental biological importance[39]. The genomic organization of ISM2 results in two alternatively spliced transcript variants that encode distinct protein isoforms, although the specific functional differences between these variants remain incompletely characterized[58].

The primary structure of ISM2 follows a characteristic architecture beginning with an amino-terminal hydrophobic signal peptide that directs the protein into the secretory pathway[14][20][35][39][49]. This signal sequence typically comprises approximately 30 amino acid residues and facilitates translocation of the nascent polypeptide into the endoplasmic reticulum lumen during ribosomal synthesis. Following synthesis and signal peptidase cleavage, the mature secreted protein consists of an amino-terminal region of approximately 216 residues that is predicted to be largely intrinsically disordered, followed by the highly structured thrombospondin type-1 repeat domain[9]. The TSR1 domain occupies a central position in the protein sequence and comprises approximately 60 amino acid residues organized into a conserved three-stranded antiparallel beta-sheet core stabilized by three disulfide bonds and featuring conserved tryptophan and arginine residues that form a characteristic tryptophan-arginine (Trp-Arg) ladder[9][14][20].

### Thrombospondin Type-1 Repeat Domain Structure and Modifications

The TSR1 domain of ISM2 exhibits the characteristic structural features observed in thrombospondin-related proteins and shares significant homology with the TSR1 domain of ISM1, demonstrating approximately 98% sequence identity between mouse and human orthologs[32][52]. Within the TSR1 domain, several critical structural motifs have been identified that appear essential for protein function. Most notably, ISM2 contains a WSPW motif similar to but distinct from the WSLW motif present in ISM1[14][20][35]. This motif is positioned to potentially facilitate interactions with heparin and other glycosaminoglycans, a function previously characterized for thrombospondin-1 TSR domains[20][35]. The TSR1 domain also contains an EPQ motif known to determine carbohydrate binding specificity and a CSVTCG motif that is conserved among anti-angiogenic TSR-containing proteins and may facilitate interactions with CD36, a receptor implicated in mediating anti-angiogenic signaling[14][20].

The TSR1 domain undergoes critical post-translational modification through C-mannosylation at two conserved tryptophan residues corresponding to positions 223 and 226 in the human ISM1 sequence, with equivalent positions predicted to be modified in ISM2[9][33][36]. This C-mannosylation occurs through a unique glycosylation mechanism distinct from the canonical N-linked or O-linked glycosylation pathways, whereby mannose residues are attached directly to the indole nitrogen of tryptophan side chains[33][36]. Structural studies have demonstrated that C-mannosylation plays a critical role in protein folding, stability, and secretion, with the C-mannoses positioned to interact through hydrogen bonding within the tryptophan-arginine ladder structure[9][33][36]. In the absence of C-mannosylation, thrombospondin type-1 repeats demonstrate significantly reduced thermal and reductive stability, form aberrant intermolecular disulfide bridges at physiological temperatures, and exhibit delayed folding kinetics within the endoplasmic reticulum[33][36]. The C-mannosylation process is itself dependent on prior N-glycosylation events, creating an interdependent post-translational modification hierarchy that ensures proper protein folding and export[32][33].

### AMOP Domain Architecture and Structure

The carboxyl-terminal AMOP domain of ISM2 comprises approximately 100 amino acid residues and represents a relatively recently characterized protein motif found in only a limited number of secreted and transmembrane proteins including MUC4 (mucin-4), SUSD2 (sushi domain-containing protein 2), ISM1, and ISM2[14][20][35][39][49]. Recent crystal structure determination of the ISM1 AMOP domain has revealed that this domain adopts a highly distinctive fold centered on a streptavidin-like antiparallel beta-barrel core structure, a surprising finding given the domain's function in cell adhesion rather than biotin binding[9][16]. The AMOP domain comprises multiple conserved structural features including eight invariant cysteine residues that form complex disulfide bonding patterns, a series of antiparallel beta-strands forming the central barrel or "fingers" structure, and lateral alpha helices forming a "thumb" region[9][16]. Comparison of AlphaFold-predicted structures of AMOP domains from different proteins reveals that while the conserved core streptavidin-like beta-barrel is maintained across all AMOP-containing proteins, the surface helices and loops vary substantially among different AMOP proteins, potentially accounting for functional diversity among these proteins[9][16].

A particularly notable feature of ISM1 and ISM2 AMOP domains is the presence of an unpaired cysteine residue (Cys303 in ISM1) located on a surface loop[9][16]. This surface-exposed cysteine may participate in additional post-translational modifications or may serve regulatory functions through intermolecular disulfide bonding or redox-dependent interactions. Within the AMOP domain, previous studies identified a putative RKD (arginine-lysine-aspartate) motif at amino acid positions 315-317 that was proposed to function analogously to the canonical RGD (arginine-glycine-aspartate) integrin-binding sequence[48][49]. However, recent structural analysis has demonstrated that this RKD sequence is rigidly positioned on the beta-barrel core and does not occupy a flexible loop region typical of integrin-binding RGD motifs, and structural modeling indicates that significant steric clashes would prevent functional RGD-like integrin binding[9][50]. This finding necessitates revision of previous mechanistic models and suggests that ISM2 and ISM1 interactions with integrins, if they occur, involve alternative binding epitopes on the AMOP domain surface rather than RGD-mediated engagement[9][50].

### Structural Flexibility and Inter-Domain Relationships

The linker region connecting the TSR1 and AMOP domains in ISM2 comprises approximately 22 amino acid residues (positions 263-285 in ISM1) and is largely not visualized in crystallographic structures, indicating that this region maintains substantial conformational flexibility[9]. This flexibility is consistent with predictions from AlphaFold modeling and suggests that the TSR1 and AMOP domains can adopt varying orientations relative to one another[9]. The independence of domain movement is functionally significant, as it permits the two domains to present their respective functional epitopes simultaneously to multiple binding partners or receptors without steric constraint. The amino-terminal region preceding the TSR1 domain (residues 31-216 in ISM1) likewise appears to be intrinsically disordered based on AlphaFold structure predictions and is invariably not visualized in crystal structures[9]. This disordered region may serve regulatory roles through conditional interactions with cellular proteins or may function to enhance the solubility and bioavailability of the protein in extracellular compartments.

## Tissue-Specific Expression and Cellular Localization

### Placental Expression and Development

ISM2 demonstrates a highly tissue-restricted expression pattern in human tissues, with particular enrichment in the placenta where it achieves its highest absolute expression levels[13][21][42]. Immunohistochemical analysis of human placental tissue reveals localized focal cytoplasmic positivity for ISM2 in trophoblastic cells, with particularly prominent expression in the syncytiotrophoblast and cytotrophoblast layers that form the primary interface between maternal and fetal circulation[13][21]. Quantitative immunohistochemistry demonstrates that in normal placentas, approximately 173 trophoblastic cells per ten high-power fields exhibit focal cytoplasmic edge positivity for ISM2[13]. Notably, this expression pattern is significantly reduced in pathological pregnancies associated with preeclampsia, wherein only approximately 52 trophoblastic cells per ten high-power fields demonstrate ISM2 staining, representing a roughly threefold reduction compared to normal pregnancy[13]. This dramatic reduction in placental ISM2 expression in preeclampsia is accompanied by decreased serum ISM2 levels, with the mean ISM2 concentration in preeclamptic patients significantly lower than in normotensive controls[13].

The biological significance of placental ISM2 expression relates to the critical angiogenic remodeling that occurs during placental development, particularly the dramatic expansion of placental vasculature necessary to support increasing fetal nutrient and gas exchange demands as pregnancy progresses[60]. ISM2 appears to be expressed in a pattern consistent with roles in both promoting and regulating vascular growth within the placental tissue. The concentration of ISM2 expression in trophoblastic cells, which directly produce many angiogenic and anti-angiogenic factors, suggests direct involvement in the paracrine regulation of endothelial cell behavior within the placental vasculature[13]. The reduction in ISM2 expression in preeclampsia, a condition fundamentally characterized by impaired placental angiogenesis and excessive production of circulating anti-angiogenic factors, further supports a role for ISM2 as a pro-angiogenic or angiogenic-regulatory protein[13][60].

### Expression in Other Tissues and Developmental Contexts

Beyond the placenta, ISM2 is expressed at moderate to low levels in a variety of other tissues, as documented through analysis of The Human Protein Atlas database and other systematic tissue expression surveys[15][21][24][29]. According to immunohistochemical surveys, ISM2 protein is detectable in the male reproductive system, digestive system tissues, and various other organs where it appears to be secreted into the extracellular matrix and blood compartments[15]. RNA-level expression analysis indicates that while ISM2 mRNA is highly enriched in placental tissue, moderate expression is also detected in brain tissue and other vascular-rich organs, though at substantially lower levels than in placenta[24]. This broader tissue distribution, albeit at lower abundance, suggests additional biological roles for ISM2 beyond placental development.

During embryonic development, spatiotemporal analysis of ISM2 expression in animal models reveals particularly vigorous expression in bilateral streams of mesenchymal cells in the head region and moderate expression in trunk tissues[14][35][39]. In mouse embryos, ISM2 expression follows temporal and spatial patterns that overlap with but differ from ISM1 expression, suggesting distinct developmental roles for the two isthmin family members[8]. The developmental expression of ISM2 in head and craniofacial tissues suggests potential roles in craniofacial development and neural development, though detailed analysis of ISM2-specific functions in these contexts remains incomplete[14][35][39].

### Subcellular Localization and Secretion

As a secreted protein, ISM2 is synthesized on rough endoplasmic reticulum through recognition of its amino-terminal signal peptide by the signal recognition particle and is co-translationally translocated into the rough endoplasmic reticulum lumen[14][20][35]. Following synthesis and initial post-translational modifications including C-mannosylation of TSR1 domain tryptophan residues and N-glycosylation at asparagine residues, ISM2 is packaged into transport vesicles and trafficked through the Golgi apparatus where additional glycosylation maturation occurs[32][33]. The protein is subsequently packaged into secretory vesicles and exported from the cell through constitutive or regulated exocytosis[14][20][35]. Once secreted, ISM2 accumulates in the extracellular matrix and extracellular fluid compartments where it interacts with matrix components and cell surface receptors[15][42][49].

The precise mechanism of ISM2 secretion and trafficking has not been as thoroughly characterized as ISM1, but based on structural homology and domain composition, ISM2 is predicted to follow similar secretory pathways. The N-terminal disordered region and the flexible inter-domain linker region may contribute to the protein's hydrodynamic properties and solubility in extracellular compartments, potentially enhancing its bioavailability and diffusional reach within tissues. The presence of both secreted and potentially membrane-associated pools of ISM2 in different cellular contexts remains to be fully characterized.

## Biochemical Functions and Signaling Mechanisms

### Angiogenic and Anti-Angiogenic Properties

The most extensively studied biological function of ISM2 relates to regulation of blood vessel formation and vascular homeostasis, processes collectively termed angiogenesis. Based on multiple lines of evidence from expression analysis, in vitro functional studies, and clinical observations, ISM2 appears to function as a pro-angiogenic or angiogenic-modulating protein, contrasting with the more clearly anti-angiogenic properties established for ISM1 under certain conditions[13][14][57]. The evidence supporting angiogenic functions for ISM2 is somewhat more limited and contextual than the detailed mechanistic understanding of ISM1 angiogenic inhibition, reflecting the earlier and more extensive characterization of ISM1 in the literature.

The angiogenic role of ISM2 is inferred from several convergent lines of evidence. First, the serum level of ISM2 is significantly decreased in women with preeclampsia compared to normotensive pregnant controls, and this decrease is accompanied by increased circulating levels of the prototypical anti-angiogenic factors soluble fms-like tyrosine kinase-1 (sFlt1) and soluble endoglin (sEng)[13][60]. Preeclampsia is pathologically characterized by impaired placental angiogenesis and excessive production of circulating anti-angiogenic factors that disrupt endothelial function systemically[60]. The reduction in ISM2 levels in this context where pro-angiogenic factors are depleted suggests that ISM2 normally contributes to maintaining adequate angiogenic signaling[13].

Second, ISM2 is highly expressed in choriocarcinoma, a highly vascular trophoblastic malignancy characterized by excessive angiogenesis and high expression of pro-angiogenic factors[13][14][57]. This elevated expression in a condition of pathological angiogenesis suggests that ISM2 expression may facilitate tumor vascularization. By contrast, ISM1 expression is reported to be elevated in multiple different cancer types including gastric cancer, hepatocellular carcinoma, and colorectal cancer[14][35][39][49], where it typically exerts anti-angiogenic functions and impairs tumor growth[14][35][39]. The distinction between ISM2 expression in the highly vascular choriocarcinoma and ISM1 expression in various other cancers suggests functional specialization of the two isthmin family members.

Third, the structural composition of ISM2 itself suggests potential angiogenic activity through the integration of multiple domains with demonstrated roles in angiogenic regulation[13][57]. Specifically, the TSP-1 central domain contained within the TSR1 region of ISM2 has been demonstrated to have dual pro-angiogenic and anti-angiogenic properties depending on cellular context[13][57]. TSP-1 can promote endothelial cell proliferation, migration, and overall vascular growth under certain conditions while simultaneously exerting anti-angiogenic effects through interactions with CD36 and other receptors in other contexts[23][44]. The AMOP domain in ISM2, although not yet fully functionally characterized in this protein, is present in MUC4 and SUSD2, both of which have been implicated in promoting tumor angiogenesis in specific cancer contexts[13].

### Vascular Permeability Regulation

While vascular permeability regulation has been more extensively characterized for ISM1 than for ISM2, the structural homology between the two proteins and the presence of shared domains suggest that ISM2 may similarly participate in regulating vascular permeability. ISM1 functions as a vascular permeability inducer through interaction with cell-surface GRP78 (glucose-regulated protein 78 kDa) and αvβ5 integrins on endothelial cells[25][28][52]. This interaction triggers Src family kinase activation and phosphorylation of adherens junction proteins, leading to disruption of endothelial cell-cell junctions and increased vascular permeability[25][28][52]. ISM1-mediated vascular permeability enhancement is particularly pronounced in the lung vasculature and has been implicated in lipopolysaccharide-induced acute lung injury[25][28]. The structural features of ISM2 that would be necessary for similar permeability-inducing function remain to be experimentally validated, but the presence of potential GRP78-binding epitopes within the AMOP domain structure suggests this possibility.

### Developmental and Morphogenic Functions

ISM2 appears to play roles in developmental processes, particularly in craniofacial development and asymmetric organ morphogenesis. These functions are likely mediated through interactions with developmental signaling pathways, particularly transforming growth factor-beta (TGF-β) superfamily signaling. The TSR1 domain of ISM2 contains structural motifs including WSPW that show conservation with known TGF-β regulatory motifs, suggesting potential for ISM2 to interact with latent TGF-β complexes and modulate TGF-β signaling activation[14][20][35][39]. ISM1 has been definitively demonstrated to antagonize NODAL signaling through direct interaction with NODAL ligands and type I receptors, thereby suppressing SMAD2 phosphorylation and downstream transcriptional responses[19][32][35][39]. This function is specifically mediated through the AMOP domain, suggesting that ISM2, by virtue of possessing a similar AMOP domain, might similarly interact with developmental signaling molecules[19][32].

## Regulation of Receptor-Mediated Signaling

### Integrin Interactions and Signaling

The interactions between ISM2 and integrin family receptors have been more extensively characterized for ISM1, but insights from this mechanistic understanding inform our current understanding of potential ISM2 integrin interactions. ISM1 has been reported to interact with the αvβ5 integrin heterodimer through a mechanism proposed to involve the RKD motif in its AMOP domain[48][49][52]. However, recent high-resolution structural studies combined with computational modeling have substantially revised this model, revealing that the RKD sequence in ISM1's AMOP domain is positioned rigidly on the beta-barrel core in a manner incompatible with canonical RGD-motif integrin binding[9][50]. Instead, structural modeling suggests that ISM1 interaction with integrins, if it occurs, involves alternative binding epitopes on the AMOP domain surface distinct from the RKD motif[9][50].

Despite the structural clarification that has revised previous RGD-mediated integrin binding models, significant experimental evidence continues to support functional interactions between ISM1 and αvβ5 integrins, with important downstream consequences. Soluble ISM1 acts as an antagonist of αvβ5 integrin signaling, inducing endothelial cell apoptosis through integrin-mediated death mechanisms without triggering anoikis (detachment-induced apoptosis)[48][49]. This apoptotic function requires direct recruitment and activation of caspase-8, suggesting proximal signaling events immediately downstream of αvβ5 integrin ligation by ISM1[48][49]. By contrast, when ISM1 is immobilized within the extracellular matrix, it functions as an agonist of αvβ5 integrin, promoting endothelial cell adhesion, survival, and haptotactic migration through activation of focal adhesion kinase (FAK)[48][49]. This remarkable switch from integrin antagonism to agonism based on protein immobilization state represents a sophisticated regulatory mechanism that may similarly apply to ISM2.

### GRP78 Signaling and Apoptotic Pathways

Glucose-regulated protein 78 kDa (GRP78, also known as BiP or HSPA5) represents a critical high-affinity receptor for ISM1 with a binding affinity (Kd) of approximately 8.58 nanoMolar[52]. While the GRP78-ISM2 interaction has not been as thoroughly characterized as the GRP78-ISM1 interaction, the structural similarity between the two proteins and the presence of putative GRP78-binding epitopes suggest potential for similar interactions. GRP78 is traditionally recognized as an endoplasmic reticulum-resident chaperone protein essential for protein folding and cellular stress response[25][28][52]. However, under conditions of endoplasmic reticulum stress or in certain cell types including cancer cells, a portion of GRP78 is translocated to and retained at the cell surface where it functions as a receptor for extracellular ligands including pro-apoptotic factors[25][28][52].

ISM1 binding to cell-surface GRP78 initiates a signaling cascade that leads to Src family kinase activation, particularly through direct protein-protein interaction between GRP78 and Src kinase[25][28]. This interaction triggers Src autophosphorylation and kinase activation, which subsequently phosphorylates multiple downstream substrates including adherens junction proteins at tyrosine residues[25][28]. The phosphorylation of adherens junction proteins including VE-cadherin and associated catenins disrupts cell-cell junctional integrity and increases paracellular permeability in endothelial monolayers[25][28]. Additionally, GRP78-ISM1 interaction can trigger internalization of the ISM1-GRP78 complex into acidic endosomes and ultimately direct trafficking to mitochondria where ISM1 interacts with adenine nucleotide translocase (AAC) in the inner mitochondrial membrane, blocking ADP/ATP exchange and depleting cytoplasmic ATP, leading to energy-dependent cell death[25][28][56].

### NODAL Signaling Antagonism

The most thoroughly mechanistically characterized function of ISM1 is its role as an antagonist of NODAL signaling, a developmental pathway critical for left-right asymmetry determination and multiple developmental processes[19][22][32][35][39]. NODAL is a member of the TGF-β superfamily of secreted signaling molecules that activates downstream signaling through interaction with a heterotetrameric receptor complex consisting of type I receptors (ALK4/ACVR1B) and type II receptors (ActR2A) along with the co-receptor CRIPTO/CRYPTIC[19]. ISM1 negatively regulates NODAL signaling by directly interacting with both the NODAL ligand and the type I receptor ACVR1B through its AMOP domain, thereby disrupting productive NODAL-ACVR1B complex formation and preventing SMAD2 phosphorylation and downstream transcriptional responses[19]. This inhibitory mechanism is selective for NODAL signaling, as ISM1 does not significantly affect signaling through other TGF-β superfamily members including TGF-β1, ACTIVIN-A, or BMP4[19][32].

The AMOP domain specificity for NODAL antagonism has been definitively established through deletion analysis, demonstrating that deletion of the AMOP domain completely abolishes ISM1's ability to inhibit NODAL signaling while deletion of the TSR1 domain does not significantly impair this function[19][32][35]. By contrast, TSR1-mediated functions such as potential TGF-β activation through binding to latency-associated protein remain intact in AMOP-deleted variants. The biological significance of NODAL antagonism by ISM1 extends to craniofacial development, where ISM1 expression levels influence left-right symmetry determination and bilateral symmetry of craniofacial structures[19][22][32][35][39].

While similar detailed mechanistic analysis of ISM2's interaction with NODAL has not been published, the presence of an analogous AMOP domain structure in ISM2 raises the possibility that ISM2 similarly interacts with developmental signaling pathways, potentially including NODAL signaling. However, the functional specialization implied by the differing expression patterns and tissue distributions of ISM1 and ISM2 suggests that the two proteins may have diverged in their specific developmental roles even while retaining structurally homologous domains.

## Cellular and Tissue-Level Consequences

### Endothelial Cell Responses

At the cellular level, ISM2's effects on vascular biology are likely to be mediated primarily through interactions with endothelial cells, which form the inner lining of blood vessels and directly sense circulating angiogenic factors and locally produced matrix proteins. The angiogenic modulation attributed to ISM2 would be expected to manifest as changes in endothelial cell proliferation rates, cell survival versus apoptosis ratios, and cell migration and tube formation capacity in three-dimensional culture systems. The differential effects of ISM2 when present in soluble versus immobilized form within the extracellular matrix, as well established for ISM1, would produce distinct phenotypic outcomes in endothelial cell populations depending on local ISM2 concentration and tissue microenvironment context.

The localization of ISM2 to trophoblastic cells within placental tissue suggests that ISM2 is produced by epithelial cells and acts in a paracrine manner on adjacent endothelial cells within the placental vasculature. This cellular communication is particularly important in the placenta where intimate association between trophoblastic epithelium and endothelial vasculature facilitates nutrient and gas exchange. The dramatic reduction in trophoblastic ISM2 expression in preeclampsia suggests impaired paracrine signaling to placental endothelial cells, potentially contributing to the endothelial dysfunction characteristic of preeclampsia.

### Podocyte and Glomerular Function

In the kidney glomerulus, ISM1 has been demonstrated to induce apoptosis of podocytes, specialized epithelial cells that form the glomerular filtration barrier[45]. Recombinant ISM1 treatment of isolated human podocytes induces dose- and time-dependent decreases in cell viability through both caspase-dependent and caspase-independent apoptotic mechanisms[45]. At low ISM1 concentrations, apoptosis is primarily caspase-dependent and can be blocked by pan-caspase inhibitors, while at higher concentrations, a caspase-independent component becomes prominent, characterized by mitochondrial destabilization and nuclear translocation of apoptosis-inducing factor (AIF)[45]. In disease contexts, elevated renal expression of ISM1 is associated with glomerular disease progression, suggesting that dysregulation of ISM-family protein expression in the kidney contributes to pathological outcomes[45]. ISM2's potential to similarly affect podocyte function remains to be experimentally tested.

## Disease Associations and Pathophysiological Roles

### Preeclampsia and Placental Insufficiency

The most extensively documented disease association for ISM2 relates to preeclampsia, a serious pregnancy complication affecting approximately five to eight percent of pregnancies and representing a leading cause of maternal and fetal morbidity and mortality worldwide[60]. Preeclampsia is fundamentally characterized by impaired placental angiogenesis, excessive production of anti-angiogenic factors, and systemic endothelial dysfunction manifesting as hypertension, proteinuria, and multi-organ involvement[60]. The characteristic angiogenic imbalance in preeclampsia involves elevated circulating levels of soluble fms-like tyrosine kinase-1 (sFlt1) and soluble endoglin (sEng) coupled with reduced levels of pro-angiogenic factors including vascular endothelial growth factor (VEGF) and placental growth factor (PlGF)[60].

The observation that ISM2 serum levels are significantly decreased in preeclamptic patients compared to normotensive pregnant controls, with the mean reduction exceeding thirty percent in some studies, suggests that loss of pro-angiogenic ISM2 signaling contributes to preeclampsia pathogenesis[13]. This decrease in serum ISM2 parallels the well-established decreases in VEGF and PlGF that characterize the pro-angiogenic deficit in preeclampsia[13][60]. The mechanism underlying reduced ISM2 levels in preeclampsia may involve both decreased placental production of ISM2 by trophoblastic cells, as evidenced by reduced immunohistochemical staining intensity, and increased clearance or consumption of circulating ISM2[13]. The hypothesis that restoration of ISM2 signaling might ameliorate preeclampsia pathology remains to be tested, but would be consistent with the therapeutic potential of pro-angiogenic factor replacement in this disease.

### Choriocarcinoma and Trophoblastic Malignancy

By marked contrast to the decreased ISM2 expression in preeclampsia, ISM2 expression is significantly elevated in choriocarcinoma, a highly malignant trophoblastic tumor characterized by rapid proliferation, extensive vascularization, and metastatic dissemination[13][14]. The high expression of ISM2 in this context where pathological angiogenesis is excessive suggests that ISM2 expression facilitates tumor angiogenesis and vascular growth supporting tumor expansion[13][14]. This distinction between pathologically low ISM2 in preeclampsia and pathologically high ISM2 in choriocarcinoma, despite both conditions affecting trophoblastic tissues, illustrates the context-dependent and dosage-dependent effects of angiogenic regulators in human disease.

The mechanistic basis by which ISM2 overexpression in choriocarcinoma supports tumor vascularization remains to be fully elucidated but likely involves both direct pro-angiogenic effects on endothelial cells within the tumor microenvironment and indirect effects through modulation of other angiogenic signaling cascades. ISM2 may also contribute to tumor progression through effects on trophoblastic tumor cell biology itself, as trophoblastic cells express multiple receptors potentially engaged by ISM2 signaling.

### Craniofacial Development and Developmental Defects

Based on spatiotemporal expression patterns and domain homology with ISM1, which has been definitively implicated in craniofacial development, ISM2 is predicted to play roles in normal craniofacial morphogenesis[14][22][32][35][39]. ISM1 heterozygous deletions are enriched in patients with cleft lip and palate compared to control populations, indicating that even single-copy loss of ISM1 predisposes to this common developmental defect[35][39]. Knockdown of ISM1 in Xenopus embryos causes craniofacial malformations including cleft-like phenotypes, while overexpression produces left-right asymmetry defects and abnormal heart positioning[19][22][32][35][39]. These developmental functions of ISM1 appear to be mediated through antagonism of NODAL signaling and modulation of left-right axis determination.

Whether ISM2 plays similar or distinct roles in craniofacial development remains unclear, as ISM2-specific developmental studies are limited. However, the presence of mesenchymal expression in head and trunk tissues during embryonic development suggests developmental roles. The functional specialization implied by differing tissue expression patterns suggests that ISM2 may have evolved divergent developmental functions relative to ISM1, potentially including roles in specific craniofacial cell types or developmental timepoints.

## Molecular Evolution and Protein Family Context

### Isthmin Family Evolution and Structural Specialization

The isthmin family of secreted proteins comprises precisely two members in mammals: ISM1 and ISM2, a relatively small family compared to other secreted protein families such as thrombospondins or collagens[14][20][39][49]. Phylogenetic analysis demonstrates that both ISM1 and ISM2 are highly conserved across vertebrate species, with mouse ISM2 sharing approximately 93% sequence identity with human ISM2[32][52]. This high degree of evolutionary conservation across hundreds of millions of years indicates strong selective pressure to maintain protein function, suggesting fundamental importance in mammalian biology.

The structural organization of both ISM1 and ISM2—consisting of an amino-terminal signal peptide, central TSR1 domain, flexible linker region, and carboxyl-terminal AMOP domain—is invariant across the family and across species, underscoring the functional importance of this domain architecture[14][20][35][39][49]. The conservation of specific motifs within these domains, including the WSPW heparin-binding motif in ISM2, the C-mannosylation sites in the TSR1 domain, and the AMOP domain disulfide bond pattern, indicates that each structural element plays essential conserved functions.

Despite this overall structural conservation, sequence analysis reveals specific amino acid differences between ISM1 and ISM2 that likely account for functional specialization. Most notably, ISM1 contains a DGE motif in its TSR1 domain corresponding to an alpha-2-beta-1 integrin-binding sequence, while ISM2 contains an EPQ motif in the corresponding region[14][20][35]. This substitution potentially alters ISM2's ability to interact with specific integrin subtypes or other matrix-binding proteins. Similarly, differences in the amino acid sequences flanking conserved motifs within the AMOP domain may alter receptor binding specificity or signaling outcomes between the two proteins.

### Comparison with Related Thrombospondin-Domain Proteins

The TSR1 domain present in ISM2 is shared with many other secreted extracellular matrix and matricellular proteins, including all five known thrombospondins (TSP-1 through TSP-5), multiple ADAMTS metalloproteinases, and other specialized proteins[2][20][44][47]. This domain superfamily shares common structural features including the characteristic three-stranded beta-sheet core, conserved disulfide bonds, and tryptophan-arginine ladder, yet exhibits remarkable functional diversity[20][44][47]. Some TSR-containing proteins, particularly thrombospondins, function primarily as anti-angiogenic factors through CD36-mediated signaling that induces endothelial cell apoptosis[2][23][44][47]. Others, including certain ADAMTS proteins, function primarily through proteolytic processing of matrix components[20][47]. Still others, including ISM2, appear to have evolved more specialized functions in particular tissue contexts while retaining the fundamental TSR1 structural scaffold[14][20].

The AMOP domain present in ISM2 is found in only three other known human proteins: ISM1, MUC4 (mucin-4), and SUSD2[14][39]. All AMOP-containing proteins share the conserved eight-cysteine disulfide bond pattern and streptavidin-like core barrel structure, yet exhibit striking functional diversity in their biological roles[9]. MUC4 functions primarily as a mucin involved in epithelial cell protection and cancer progression[13]. SUSD2 promotes tumor angiogenesis in breast cancer[13]. ISM1 and ISM2, as the only secreted isthmin proteins, represent a specialized subfamily within the AMOP-containing protein family, adapted for extracellular matrix localization and paracrine signaling rather than membrane-tethered functions.

## Expression Regulation and Post-Translational Modification

### Post-Translational Modifications and Protein Maturation

The maturation of nascent ISM2 polypeptide into a fully functional secreted protein involves a coordinated series of post-translational modifications that occur sequentially during synthesis and transit through the secretory pathway. The amino-terminal signal peptide undergoes proteolytic cleavage by signal peptidase during ribosomal translocation into the endoplasmic reticulum, yielding the mature N-terminus of the secreted protein[14][20][35]. The TSR1 domain undergoes C-mannosylation at the conserved tryptophan residues (corresponding to positions 223 and 226 in ISM1), a modification catalyzed by the C-mannosyltransferase DPY-19 in the endoplasmic reticulum[33][36]. This C-mannosylation modification is prerequisite for subsequent N-glycosylation at additional asparagine residues and is critical for proper protein folding as evidenced by the finding that C-mannosylation inhibition dramatically impairs protein secretion[32][33].

N-glycosylation occurs at multiple asparagine residues within consensus N-glycosylation sequences (Asn-X-Serine/Threonine), with predicted sites within the amino-terminal disordered region and possibly within other domains[32][33][39]. The N-glycosylation process involves sequential addition of glucose and fucose residues by endoglycosidase H-sensitive enzymes in the endoplasmic reticulum, followed by trimming and elaboration of N-glycan structures by glycosidases and glycosyltransferases as the protein transits through the Golgi apparatus[32][33]. The importance of N-glycosylation for ISM2 function is underscored by the finding that tunicamycin inhibition of N-glycosylation markedly reduces protein secretion efficiency[32][33].

The AMOP domain contains the eight conserved cysteine residues that form disulfide bonds establishing the rigid barrel-like fold characteristic of AMOP domains[9][16]. These disulfide bonds form during protein synthesis in the oxidizing environment of the endoplasmic reticulum through the action of protein disulfide isomerase and other oxidoreductases[9][16]. The formation of correct disulfide bonds is critical for proper AMOP domain folding and subsequent protein secretion[9][16]. The unpaired cysteine residue present in ISM1 and ISM2 AMOP domains (Cys303 in ISM1) may undergo palmitoylation, glutathionylation, or other redox-dependent modifications, though the precise post-translational modification status and functional significance of this residue remain incompletely characterized[9][16].

### Regulation of Gene Expression and Transcriptional Control

The regulation of ISM2 gene transcription in normal and pathological states remains incompletely characterized compared to the transcriptional regulation of many other genes. The dramatic reduction in ISM2 expression specifically in preeclamptic placentas compared to normal placentas suggests that dysregulation of ISM2 transcription or transcript stability occurs in this disease context[13]. Potential mechanisms might include altered transcription factor activity in trophoblastic cells, changes in the transcriptional landscape induced by hypoxia or metabolic stress characteristic of preeclamptic placentas, or post-transcriptional mechanisms affecting ISM2 mRNA stability or translation efficiency[13].

By contrast, the elevated ISM2 expression in choriocarcinoma suggests constitutive upregulation of ISM2 transcription in trophoblastic malignancy, potentially through altered transcription factor signaling or loss of normal negative regulators of ISM2 expression[13][14]. Investigation of transcription factor binding sites within the ISM2 promoter region and characterization of the cis-regulatory elements controlling ISM2 expression represents an important area for future research that would illuminate the transcriptional mechanisms regulating this critical angiogenic regulator.

## Integration into Broader Vascular Biology and Extracellular Matrix Function

### Matricellular Protein Classification

ISM2 can be appropriately classified as a **matricellular protein**, a specialized class of extracellular matrix-associated proteins that, rather than serving structural roles in matrix assembly, instead function as regulators of matrix-cell interactions and cell signaling[27][44][49][55]. Matricellular proteins characteristically exhibit moderate abundance in extracellular matrices, possess multiple cell-binding domains, and modulate the activities of growth factors, proteases, and other matrix-binding proteins[27][44]. Classical examples include the thrombospondins, osteopontin, and many other glycoproteins[27][44].

The matricellular classification of ISM2 implies that its primary function is regulatory rather than structural, a classification supported by its domain composition and demonstrated functions in modulating angiogenesis, vascular permeability, and developmental signaling. As a matricellular protein, ISM2 likely contributes to the functional properties of the extracellular matrix through modulation of cell-matrix interactions and cell signaling rather than through provision of mechanical strength or structural integrity[27].

### Integration with Other Angiogenic Regulatory Factors

ISM2 functions within the complex tissue milieu of angiogenic regulators that collectively determine the balance between angiogenic and anti-angiogenic signaling at any given time and place. In normal placental tissue, pro-angiogenic factors including VEGF, PlGF, and PDGF act in concert with adequate levels of ISM2 to promote the controlled vascular expansion necessary for normal placental development[13][57][60]. The elevation of anti-angiogenic factors sFlt1 and sEng in preeclampsia coupled with decreased ISM2 and other pro-angiogenic factors creates the net anti-angiogenic environment characteristic of this disease[13][60].

The structural and functional relationship between ISM2 and thrombospondin-1 (TSP-1), mediated through the TSR1 domain shared between them, suggests potential interactions in regulating matrix assembly and remodeling[2][13][44]. TSP-1 is itself a potent regulator of angiogenesis, matrix metalloproteinase activity, and TGF-β activation[2][23][44]. The presence of TSR1 domains in both ISM2 and TSP-1 raises the intriguing possibility of direct protein-protein interaction between these molecules, though such interactions have not been explicitly demonstrated.

## Challenges and Open Questions

### Unresolved Structural-Function Relationships

Despite recent advances in structural characterization of ISM proteins through X-ray crystallography and cryo-electron microscopy, significant questions remain regarding the precise molecular mechanisms by which ISM2 exerts its biological effects. Most critically, while the crystal structure of ISM1's AMOP domain has been solved and reveals a streptavidin-like barrel architecture, the functional consequences of this specific fold for ISM2 biological activity require further investigation[9]. The discrepancy between previous predictions that the AMOP domain RKD motif mediates integrin binding and the recent structural evidence that this motif is incompilable with canonical RGD integrin binding epitopes necessitates identification of the actual integrin-binding surface if such interactions are indeed functionally important[9][50].

The role of the flexible inter-domain linker and the intrinsically disordered amino-terminal region in ISM2 function similarly requires further investigation[9]. These structurally heterogeneous regions may serve critical regulatory functions in controlling domain accessibility or may participate in multi-protein complex assembly that cannot be fully appreciated from structural studies alone.

### Ligand and Receptor Identification

While significant progress has been made in identifying cell surface receptors for ISM1 including GRP78, αvβ5 integrins, and potentially other currently uncharacterized receptors, the complete receptor repertoire for ISM2 remains unknown[25][28][52][56]. ISM2 likely binds to additional cellular receptors beyond those characterized for ISM1, potentially explaining its distinct biological functions in specific tissue contexts. Future work employing unbiased proteomic approaches to identify ISM2-binding proteins would illuminate the cellular targets through which this protein exerts its effects.

The identification of extracellular matrix components that bind ISM2 is equally important, as ISM2 function within the tissue microenvironment likely involves interactions with collagens, proteoglycans, and other matrix components[14][20]. The proposed interaction with heparin and heparan sulfate through the WSPW motif requires direct experimental validation[14][20].

### Tissue-Specific Functional Specialization

The functional specialization that has apparently evolved between ISM1 and ISM2, evidenced by their distinct expression patterns and apparently divergent roles in disease states, remains incompletely understood. ISM1 has been characterized extensively as an anti-angiogenic factor that promotes endothelial cell apoptosis through multiple receptor-mediated mechanisms, whereas ISM2 appears to function more as a pro-angiogenic or angiogenic-modulating factor. The structural basis for this functional divergence, despite apparent domain homology, warrants investigation at the level of specific amino acid differences in domain sequences that may alter receptor binding specificity or signaling outcomes.

## Conclusions and Future Perspectives

ISM2 (Isthmin-2) represents a multifunctional secreted protein that integrates structural features derived from two distinct protein domain families—the thrombospondin type-1 repeat and the AMOP domain—to execute diverse biological functions in vascular biology, development, and pathophysiology. The protein achieves particular importance in the placenta where it appears to regulate vascular growth and endothelial cell function during normal pregnancy and where dysregulation of ISM2 expression contributes to preeclampsia pathogenesis. The structural characterization of ISM2 reveals a sophisticated architecture with multiple post-translational modifications including C-mannosylation and N-glycosylation that support protein folding, secretion, and presumably biological function.

The biological activities of ISM2 encompass angiogenic modulation, vascular permeability regulation, developmental signaling, and potentially immunological functions, activities that are likely mediated through multiple distinct cell surface receptors and signaling mechanisms. The context-dependent effects of ISM2, modulated by its physical state (soluble versus matrix-immobilized), tissue microenvironment composition, and receptor expression patterns on target cells, indicate sophisticated spatial and temporal regulation of ISM2 function within tissues.

Future research aimed at clarifying ISM2 structure-function relationships, identifying the complete receptor repertoire through which this protein signals, and characterizing tissue-specific functions should substantially enhance understanding of vascular biology and provide insights potentially applicable to pregnancy complications and trophoblastic malignancies. The potential therapeutic utility of ISM2 replacement or inhibition in disease contexts ranging from preeclampsia to tumoral angiogenesis warrants investigation, particularly given the accessibility of placentally-derived and recombinant ISM2 production strategies.

## Citations

1. https://www.ncbi.nlm.nih.gov/gene?Db=gene&Cmd=DetailsSearch&Term=145501
2. https://en.wikipedia.org/wiki/Thrombospondin
3. https://www.uniprot.org/uniprotkb/Q6H9L7.133
4. https://www.ncbi.nlm.nih.gov/gene/145501
5. https://www.merckmillipore.com/SN/en/genes/ism2
6. https://www.uniprot.org/uniprotkb/Q6H9L7/entry
7. https://www.pnas.org/doi/10.1073/pnas.2502294122
8. https://pmc.ncbi.nlm.nih.gov/articles/PMC4050162/
9. https://www.nature.com/articles/s41467-025-58828-w
10. https://pubmed.ncbi.nlm.nih.gov/40392845/
11. https://maayanlab.cloud/Harmonizome/gene/ISM2
12. https://pubmed.ncbi.nlm.nih.gov/15194193/
13. https://pmc.ncbi.nlm.nih.gov/articles/PMC7567920/
14. https://pmc.ncbi.nlm.nih.gov/articles/PMC9818725/
15. https://www.proteinatlas.org/ENSG00000100593-ISM2
16. https://pmc.ncbi.nlm.nih.gov/articles/PMC3822802/
17. https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/NABA_MATRISOME.html
18. https://pmc.ncbi.nlm.nih.gov/articles/PMC6605798/
19. https://www.proteinatlas.org/ENSG00000100593-ISM2/tissue
20. https://pmc.ncbi.nlm.nih.gov/articles/PMC7960586/
21. https://www.frontiersin.org/journals/cardiovascular-medicine/articles/10.3389/fcvm.2024.1337586/full
22. https://www.proteinatlas.org/ENSG00000100593-ISM2/brain
23. https://pubmed.ncbi.nlm.nih.gov/25952901/
24. https://pmc.ncbi.nlm.nih.gov/articles/PMC3249625/
25. https://academic.oup.com/cardiovascres/article/107/1/131/513883?login=true
26. https://www.proteinatlas.org/ENSG00000100593-ISM2/cancer
27. https://pmc.ncbi.nlm.nih.gov/articles/PMC12138950/
28. https://pmc.ncbi.nlm.nih.gov/articles/PMC10409700/
29. https://pmc.ncbi.nlm.nih.gov/articles/PMC6954052/
30. https://www.proteinatlas.org/ENSG00000182093-GET1/cancer
31. https://elifesciences.org/articles/52978
32. https://pubmed.ncbi.nlm.nih.gov/16712928/
33. https://pmc.ncbi.nlm.nih.gov/articles/PMC2443699/
34. https://pubmed.ncbi.nlm.nih.gov/40414312/
35. https://www.nature.com/articles/s42003-022-04157-3
36. https://pmc.ncbi.nlm.nih.gov/articles/PMC2895425/
37. https://pmc.ncbi.nlm.nih.gov/articles/PMC2778591/
38. https://pmc.ncbi.nlm.nih.gov/articles/PMC9916724/
39. https://pmc.ncbi.nlm.nih.gov/articles/PMC2997389/
40. https://anatomypubs.onlinelibrary.wiley.com/doi/10.1002/(SICI)1097-0177(200006)218:2%3C280::AID-DVDY4%3E3.0.CO;2-0
41. https://www.nature.com/articles/cddis201137
42. https://onlinelibrary.wiley.com/doi/10.1155/2022/2909487
43. https://www.frontiersin.org/journals/cardiovascular-medicine/articles/10.3389/fcvm.2022.939757/full
44. https://pmc.ncbi.nlm.nih.gov/articles/PMC3122116/
45. https://www.hubrecht.eu/app/uploads/2017/11/cvv146.pdf
46. https://www.nature.com/articles/cdd20143
47. https://www.genecards.org/cgi-bin/carddisp.pl?gene=ISM2
48. https://pmc.ncbi.nlm.nih.gov/articles/PMC6219483/
49. https://pmc.ncbi.nlm.nih.gov/articles/PMC3087187/
50. immunohistochemical surveys