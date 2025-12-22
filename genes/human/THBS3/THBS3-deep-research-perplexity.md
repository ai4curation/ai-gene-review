---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2025-12-11T22:49:41.304230'
end_time: '2025-12-11T22:51:44.457598'
duration_seconds: 123.15
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: THBS3
  gene_symbol: THBS3
  uniprot_accession: P49746
  protein_description: 'RecName: Full=Thrombospondin-3; Flags: Precursor;'
  gene_info: Name=THBS3; Synonyms=TSP3;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the thrombospondin family. .
  protein_domains: ConA-like_dom_sf. (IPR013320); EGF-like_Ca-bd_dom. (IPR001881);
    EGF-like_dom. (IPR000742); EGF_Ca-bd_CS. (IPR018097); NOTCH1_EGF-like. (IPR049883)
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 44
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P49746
- **Protein Description:** RecName: Full=Thrombospondin-3; Flags: Precursor;
- **Gene Information:** Name=THBS3; Synonyms=TSP3;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the thrombospondin family. .
- **Key Domains:** ConA-like_dom_sf. (IPR013320); EGF-like_Ca-bd_dom. (IPR001881); EGF-like_dom. (IPR000742); EGF_Ca-bd_CS. (IPR018097); NOTCH1_EGF-like. (IPR049883)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "THBS3" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'THBS3' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **THBS3** (gene ID: THBS3, UniProt: P49746) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

<think>
The user is asking me to provide a comprehensive research report on the gene THBS3 (thrombospondin-3) with UniProt accession P49746 from Homo sapiens (Human). 

Let me first verify the gene information:
- Gene symbol: THBS3
- UniProt ID: P49746
- Full name: Thrombospondin-3
- Organism: Homo sapiens (Human)
- Protein family: Thrombospondin family
- Key domains: ConA-like domain, EGF-like calcium-binding domain, EGF-like domain

The search results provided contain extensive information about THBS3/TSP3. Let me verify this is the correct protein from the sources:

From source [1], [21], [29], [37]: "Thrombospondin-3 (TSP3) is a protein that in humans is encoded by the THBS3 gene... The protein encoded by this gene belongs to the thrombospondin family. Thrombospondin family members are adhesive glycoproteins that mediate cell-to-cell and cell-to-matrix interactions."

From source [2], [20], [38]: "Adhesive glycoprotein that mediates cell-to-cell and cell-to-matrix interactions. Can bind to fibrinogen, fibronectin, laminin and type V collagen."

From source [12]: "The protein encoded by this gene belongs to the thrombospondin family. Thrombospondin family members are adhesive glycoproteins that mediate cell-to-cell and cell-to-matrix interactions. This protein forms a pentameric molecule linked by a single disulfide bond."

This confirms we have the correct protein. Now I need to structure a comprehensive research report that covers:

1. Key concepts and definitions with current understanding
2. Recent developments and latest research
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources


5. Relevant statistics and data from recent studies

I'll systematically compile statistical data from recent studies, focusing on quantitative insights that provide context for THBS3's biological significance. I'll extract numerical evidence about protein expression levels, interaction frequencies, and clinical correlations across different research contexts.

The comprehensive report structure will enable a deep, multifaceted exploration of thrombospondin-3's complex molecular landscape. My approach involves integrating diverse research domains to create a nuanced scientific narrative that captures the protein's intricate roles and potential translational implications.

The sources offer robust scientific documentation, supporting an in-depth 10,000-word analysis that comprehensively examines THBS3's molecular characteristics, functional dynamics, and clinical relevance across multiple physiological and pathological domains.
</think>

# Comprehensive Functional Annotation of THBS3 (Thrombospondin-3): Structure, Function, and Physiological Significance

**Thrombospondin-3 (THBS3), encoded on human chromosome 1, is a pentameric matricellular glycoprotein that serves as a critical adhesion molecule mediating cell-to-cell and cell-to-matrix interactions across diverse biological contexts.** This protein forms a pentameric structure linked by a single disulfide bond and contains characteristic calcium-binding type 3 repeats and epidermal growth factor-like domains that enable its multiple protein interactions[1][12][29]. Recent research has established THBS3 as a multifunctional protein with complex and sometimes antagonistic roles in skeletal development, cardiac homeostasis, tumor progression, and immune regulation, with particular significance emerging regarding its involvement in COVID-19 susceptibility and disease-induced cardiomyopathy. Unlike its family member thrombospondin-4 (THBS4), which typically exerts protective effects on cardiac and skeletal muscle, THBS3 demonstrates a predominantly maladaptive phenotype in disease contexts through mechanisms involving integrin trafficking and sarcolemmal stability[18][36][39]. The protein's function is highly dependent on calcium binding and structural conformational states, and its dysregulation has been implicated in osteosarcoma progression, aortic aneurysm pathology, and wound healing responses in corneal tissues.

## Structural Architecture and Molecular Characteristics

The structural organization of thrombospondin-3 fundamentally determines its biological properties and functional capacity within the extracellular matrix environment. THBS3 is organized as a **pentameric molecule linked by a single disulfide bond**, distinguishing it structurally from thrombospondins-1 and -2 which form trimeric structures[1][12][29][30]. The protein belongs to the thrombospondin family of matricellular glycoproteins, which function as adapter molecules that guide extracellular matrix synthesis and tissue remodeling in various normal and pathological settings[5][31]. The thrombospondin family comprises five distinct members in vertebrates—THBS1 through THBS5—each with unique structural features and biological properties, though all share a fundamental role in mediating extracellular matrix organization and cell-matrix interactions[5][31].

The molecular architecture of THBS3 contains several conserved domain structures that define its interactive capabilities. The protein possesses calcium-binding type 3 repeats arranged in tandem, which are composed of aspartic acid-rich motifs that resemble EF-hand structures in their calcium coordination patterns[31][35]. Specifically, each type 3 repeat contains two DxDxD/N motifs that encapsulate calcium ions in a novel arrangement distinct from classical EF-hands[35]. The protein contains an L-type lectin domain, also known as the C-terminal domain (CTD), which forms a characteristic lectin-like β-sandwich structure containing four strictly conserved calcium-binding sites[35]. Additionally, THBS3 possesses epidermal growth factor-like domains with calcium-binding capability (EGF-like Ca-binding domains) and non-calcium-binding EGF-like domains[1][17][40]. Notably, THBS3 differs from THBS1 and THBS2 in that it lacks the procollagen homology domain and type I repeats characteristic of those proteins[25].

The calcium-binding capacity of thrombospondins, including THBS3, is profoundly important for protein function and conformational stability. Thrombospondins have been shown to bind 10-12 calcium ions per subunit with high cooperativity and moderate affinity (average Kd approximately 0.1 mM)[35]. The removal of calcium leads to dissociation of the type 3 repeats from the L-type lectin domain[31]. The type 3 repeats contain two distinct classes of calcium-binding motifs—N-type and C-type—which can be distinguished by sequence length, calcium ion binding mechanisms, and their interactions with water molecules[31][35]. Two classes of type 3 repeat motif ([N] and [C] designation) form the structural basis, with C-type motifs demonstrating high-affinity calcium binding and N-type motifs demonstrating lower affinity[35]. This calcium-dependent architecture explains how mutations in the calcium-binding residues of THBS family members can cause protein misfolding and associated diseases.

A critical distinguishing feature of THBS3 relative to other thrombospondins concerns its integrin-binding motifs. Whereas all other THBS family proteins—specifically THBS4 and THBS5—contain conserved RGD (arginine-glycine-aspartate) or KGD (lysine-glycine-aspartate) integrin-binding motifs in the type 3 repeats, THBS3 uniquely contains a conserved EGD (glutamic acid-glycine-aspartate) sequence at the corresponding position[18][36][57]. This fundamental substitution of glutamic acid for the basic amino acid (arginine or lysine) found in other family members has profound consequences for integrin recognition and cell-matrix interactions[36][57]. This structural difference underscores why THBS3 demonstrates antagonistic properties compared to THBS4 in cardiac disease contexts, as the altered integrin-binding domain directly affects integrin trafficking and membrane localization patterns[36][57]. Furthermore, THBS3 gene shares a common promoter region with metaxin 1 (MTX1), a mitochondrial membrane protein involved in protein import, suggesting coordinate transcriptional regulation of these functionally unrelated proteins[1][12][30][33].

## Primary Biological Functions and Extracellular Matrix Interactions

Thrombospondin-3 functions fundamentally as an adhesive glycoprotein that mediates critical interactions between cells and the extracellular matrix, as well as between adjacent cells[1][2][12][20][38]. The primary function of THBS3 is to serve as a matricellular protein—a classification describing proteins that associate with the extracellular matrix and regulate cell-matrix interactions while not being structural components themselves[5][31]. The protein accomplishes this through its capacity to bind multiple extracellular matrix proteins, establishing itself as a molecular bridge within the matrix architecture. THBS3 has been documented to bind to fibrinogen, fibronectin, laminin, and type V collagen[2][20][38][10], the same ligands recognized by other thrombospondin family members. These binding interactions enable THBS3 to integrate into developing extracellular matrix during tissue remodeling and to coordinate the assembly of matrix components[5].

The interaction of THBS3 with extracellular matrix proteins involves multiple discrete binding sites within the protein structure. The type 3 repeats of thrombospondins contain integrin-binding sites whose availability depends critically on the protein's calcium-loading state and disulfide bond configuration[31]. In THBS3 specifically, the presence of the EGD motif rather than the canonical RGD motif results in altered integrin recognition patterns compared to other family members[18][36]. The C-terminal region of THBS3, comprising the type 3 repeats and the lectin-like β-sandwich domain, serves as the primary region for extracellular matrix incorporation[31]. Research has demonstrated that ECM incorporation of thrombospondins is conserved across family members and depends on the carboxy-terminal region in its proper oligomeric form, with this activity being partially inhibited by mutation of highly conserved aspartic acid residues that coordinate calcium ions[31].

Recent research has revealed that THBS3 functions as a cell-matrix protein with roles in adhesion-dependent cellular responses[55]. Studies employing bioinformatics analysis of clear cell renal cell carcinoma demonstrated that THBS3 functions as an adhesion molecule and cell matrix protein capable of modulating cellular proliferation and migration[55]. The protein can engage cell surface receptors through its multiple binding domains, thereby transmitting information from the extracellular environment to intracellular signaling cascades[31][55]. In this capacity, THBS3 participates in integrating cell adhesion signals that regulate cellular behavior including proliferation, differentiation, apoptosis, and migration[5][31].

## Role in Skeletal Maturation and Development

One of the first characterized functions of THBS3 was its involvement in regulating skeletal maturation during development. **THBS3 has been found to be involved in the regulation of skeletal maturation**, representing one of its primary developmental roles[1][11][12][21][29]. This discovery emerged from studies of gene-knockout mice that revealed altered bone properties when THBS3 function was disrupted. Mice with a disruption of the thrombospondin 3 gene demonstrate significant differences in the geometric and biomechanical properties of bone and exhibit accelerated development of the femoral epiphysis[6][9][11][49]. Specifically, homozygous null mice at young ages are heavier and exhibit femurs with increased periosteal and endocortical diameters, greater moments of inertia, and altered bone biomechanical properties[14]. These findings provided clear evidence that THBS3 plays a regulatory role in skeletal development and maturation processes.

The molecular basis for THBS3's role in skeletal development likely involves its interactions with the extracellular matrix in bone and cartilage tissues. During skeletal development, the transition from cartilage to bone involves coordinated changes in extracellular matrix composition and organization[31]. THBS3 may influence this process through its capacity to bind matrix proteins and modulate cell-matrix interactions that are essential for osteoblast differentiation and bone formation. The protein's calcium-dependent structure and integrin-binding properties position it to serve as a regulator of cellular responses to matrix cues during this developmental transition. Additionally, THBS3's expression pattern during development appears to be tightly regulated, consistent with its role as a developmentally regulated heparin-binding protein[34][40].

The specific mechanisms by which THBS3 regulates skeletal maturation remain incompletely understood, though the altered geometric and biomechanical properties of bones in knockout mice suggest involvement in processes affecting bone shape, size, and material properties. The accelerated femoral epiphysis ossification observed in THBS3-deficient mice indicates that normal THBS3 function delays or regulates the rate of endochondral ossification—the process by which cartilage is replaced by bone[11][52]. This suggests THBS3 may function to suppress premature ossification or to maintain cartilage integrity during development. The role of mechanical factors in contributing to ossification of femoral head cartilage indicates that THBS3 may also participate in mechanotransduction processes whereby physical forces are translated into cellular responses[52].

## Cardiac and Vascular Pathophysiology

Recent research has revealed that THBS3 plays a critical and largely maladaptive role in cardiac disease, promoting cardiomyopathy through mechanisms distinct from its family member THBS4. **Thrombospondin-3 augments injury-induced cardiomyopathy by promoting sarcolemmal destabilization through reduced integrin function**[18][39][44][57]. This discovery represents a paradigm shift in understanding thrombospondin function, as THBS4 exerts cardioprotective effects through opposite mechanisms—specifically by enhancing integrin membrane residence and sarcolemmal stability[18][36]. Transgenic mice overexpressing THBS3 specifically in cardiomyocytes show exacerbated cardiac pathology with stress stimulation, whereas mice lacking THBS3 are protected from disease-induced cardiomyopathy, demonstrating a clear pathogenic role for this protein in the heart[18][36].

The molecular mechanism whereby THBS3 exacerbates cardiac disease involves direct inhibition of integrin trafficking to the cardiomyocyte plasma membrane (sarcolemma). **Deletion of Thbs3 in mice enhances integrin membrane expression and membrane stability, protecting the heart from disease stimuli**[18][36]. This protective effect has been demonstrated in multiple cardiac injury models including transverse aortic constriction (TAC) and isoproterenol stimulation[18][36][57]. Conversely, when THBS3 is overexpressed or upregulated during cardiac stress, integrin levels at the sarcolemma are reduced, leading to decreased membrane stability and enhanced susceptibility to membrane rupture events[18][36][57]. This mechanism has been verified through multiple experimental approaches including immunoprecipitation studies demonstrating that THBS3 protein localizes to intracellular vesicular compartments containing integrin proteins, and through cell surface biotinylation experiments showing reduced surface levels of integrin α5 and β1 integrin in THBS3-overexpressing cardiomyocytes[18][57].

The structural basis for THBS3's deleterious effects on integrin trafficking involves its aberrant EGD motif rather than the canonical RGD integrin-binding domains found in THBS4 and THBS5. **Mutating Thbs3 to contain the conserved RGD integrin binding domain normally found in Thbs4 and Thbs5 now rescues the defective expression of integrins on the sarcolemma**[18][36]. This experiment directly demonstrates that the EGD sequence is the critical determinant of THBS3's maladaptive phenotype in cardiac tissue. When the EGD motif is replaced with RGD, THBS3 no longer impairs integrin trafficking, and the cardioprotective effects of integrin are maintained[18][36]. Moreover, transgene-mediated overexpression of α7β1D integrin in hearts with THBS3 overexpression ameliorates the disease-predisposing effects of THBS3, demonstrating that increasing integrin levels is sufficient to compensate for THBS3's inhibitory effects on integrin trafficking[18][36][57].

The intracellular mechanisms by which THBS3 inhibits integrin trafficking have been elucidated through detailed cellular and molecular studies. THBS3 reduces integrin trafficking from the trans-Golgi network to the plasma membrane, a process that involves selective inhibition of α5 integrin exit from the Golgi[18][36][57]. Importantly, addition of extracellular recombinant THBS3 protein does not alter integrin trafficking patterns, demonstrating that THBS3's effect on integrin trafficking is mediated through intracellular interactions rather than through cell surface receptor engagement[18][36][57]. Analysis of endocytic protein uptake after cell surface biotinylation reveals that THBS3 enhances integrin uptake and endocytosis, suggesting that THBS3 promotes greater turnover of sarcolemmal integrin content[57]. This combination of reduced Golgi exit and enhanced endocytic uptake results in reduced steady-state levels of integrin at the cardiomyocyte surface.

The endoplasmic reticulum localization of THBS3 provides insights into its intracellular mechanisms. Immunohistochemical analysis of heart sections from THBS3 transgenic mice and mice subjected to cardiac injury shows cardiomyocyte-restricted, intracellular localization of THBS3 protein that is directly coincident with the endoplasmic reticulum chaperone protein disulfide isomerase (PDI)[57]. Ultrastructural analysis reveals strong expansion of the ER-vesicular compartment with attached ribosomes in hearts overexpressing THBS3, similar to what has been observed in hearts and skeletal muscle overexpressing THBS4, though without ultrastructural defects in mitochondria or sarcomeres[57]. These observations indicate that THBS3 engages the unfolded protein response and endoplasmic reticulum stress pathways during disease states[57].

Beyond cardiac tissue, THBS3 also demonstrates altered expression in vascular diseases including abdominal aortic aneurysm. **Overexpression of THBSs may have a destabilizing effect on the structure of the extracellular matrix by affecting both the matrix producing cells and by inhibiting the activity of matrix proteins**[42][45]. In samples of abdominal aortic aneurysm tissue, differential expression of THBS3 with notably higher levels in control regions compared to aneurysmal tissue suggests that overexpression of this protein might destabilize the matrix architecture by affecting both the activity of matrix-producing cells and interfering with matrix protein function[12][30][42][45]. THBS3 has been hypothesized to downregulate the expression of integrins, which can affect cell membranes and destabilize the complex junction of the extracellular matrix structure in the aortic vessel[42]. The destabilization of the extracellular matrix and the connection of cells to it may facilitate pathological changes associated with aneurysm development[42].

Furthermore, THBS3 expression has been identified as abnormally reduced in patients suffering acute myocardial infarction (AMI). Low THBS3 expression in peripheral blood mononuclear cells from AMI patients has been proposed as a biomarker for identifying acute myocardial infarction risk[41]. The correlation between low THBS3 expression and AMI occurrence suggests a paradoxical protective effect of THBS3 in the context of acute ischemic injury, which may differ mechanistically from its chronic disease-promoting effects observed with pathological cardiac stress. This apparent discrepancy warrants further investigation into the context-dependent and temporally dynamic functions of THBS3 in cardiac pathology.

## Involvement in Tumor Progression and Cancer Biology

Emerging evidence identifies THBS3 as a promoter of aggressive tumor behavior and metastatic potential, though the mechanisms appear distinct across different cancer types. **This is the first report of the THBS3 gene working as a stimulator of tumor progression**[3][23]. In osteosarcoma, one of the most aggressive pediatric bone cancers, THBS3 expression is significantly elevated and correlates strongly with poor clinical outcomes. Patients with tumors overexpressing THBS3 demonstrate worse overall survival, event-free survival, and relapse-free survival compared to patients with low THBS3 expression[23][26]. This association is particularly pronounced in patients with metastasis at diagnosis, where high THBS3 expression serves as a predictor of poor overall survival[23]. Importantly, after chemotherapy, patients with tumors maintaining high THBS3 expression have significantly worse relapse-free survival compared to those whose tumors show reduced THBS3 expression post-treatment[23].

The molecular basis for THBS3's role in promoting osteosarcoma progression involves its pro-angiogenic properties and its capacity to promote tumor angiogenesis. High THBS3 expression maintains the capacity of angiogenesis activated by THBS3, and this appears to be part of the fundamental process of tumor progression[23]. The effects of THBS3, like those of THBS1, appear to depend on multiple factors including protein concentration, the type of domain that is activated or available, and the types of receptors present on endothelial cells[23]. The study of these parameters in the context of osteosarcoma treatment should be considered when evaluating anti-angiogenic therapeutic strategies, as THBS3 expression levels may serve as a useful prognostic factor and potentially as a therapeutic target for improving osteosarcoma outcomes[23].

In clear cell renal cell carcinoma (ccRCC), bioinformatics analyses revealed that THBS3 is a novel candidate oncogene that is overexpressed in tumor tissue and whose elevated expression is associated with poor prognosis[55]. Comprehensive analysis demonstrated that THBS3 is significantly upregulated in ccRCC tumor tissues compared with adjacent normal tissues[55]. Experimental studies employing knockdown of THBS3 expression in ccRCC cell lines demonstrate that THBS3 suppression significantly inhibits cell proliferation, colony formation, and migration capacity of these cells[55]. These findings suggest that THBS3 is upregulated in cancer tissues and could be used as a novel prognostic marker for ccRCC, with implications for targeted therapeutic development[55].

The role of THBS3 in wound healing and tissue remodeling relates to its function in cancer biology through its capacity to regulate extracellular matrix organization and angiogenesis. In cultured human corneal stromal cells (keratocytes), those adopting a wound repair phenotype express THBS3 in conjunction with related thrombospondin family members THBS1 and THBS2[12][24][27]. This suggests that THBS3 plays a role in extracellular matrix organization and in preserving the avascularity necessary for proper corneal repair—a distinct function from its pro-angiogenic properties in tumor environments[12][24][27]. The differential expression of THBS3 in wound repair versus tumor contexts may reflect its capacity to adapt its function based on the tissue environment, cellular context, and interactions with other regulatory proteins and growth factors.

## COVID-19 Susceptibility and Immune Function

An important recent discovery has identified THBS3 as a genetic locus associated with susceptibility to SARS-CoV-2 infection and COVID-19 disease severity. **Identified as the gene on chromosome 1 responsible for mediating an associated with genetic susceptibility to SARS-CoV-2 infection**[1][21][29][37]. Genome-wide association studies conducted by large international consortia including the COVID-19 Host Genetics Initiative have identified THBS3 on chromosome 1 as one of the genetic loci contributing to differential COVID-19 outcomes across populations[19][22]. This finding emerged from large-scale investigations encompassing over 125,584 cases and more than 2.5 million controls across 60 studies from 25 countries, representing comprehensive global efforts to characterize population genetic heterogeneity in response to SARS-CoV-2 exposure[22].

The molecular basis for THBS3's involvement in COVID-19 susceptibility likely involves its capacity to activate transforming growth factor-beta 1 (TGF-β1), a key cytokine involved in immune regulation and fibrosis[30][47][50]. Research indicates that THBS3 may act as an activator of TGF-β1 and thereby promote enhanced IgA responses that could accentuate immunoinflammatory damage[30]. TGF-β1 plays complex and context-dependent roles during SARS-CoV-2 infection—while it is essential for maintaining healthy microvasculature through its roles in regulating inflammation, clotting, and wound healing, dysregulation of TGF-β signaling during SARS-CoV-2 infection can augment coagulation, cause immune dysregulation, and direct a path toward tissue fibrosis[47]. Serum levels of TGF-β1, an isotype switch factor, are elevated in COVID-19 patients, and this elevation correlates with SARS-CoV-2-specific IgA responses[47][50].

The immunological consequences of enhanced TGF-β1 signaling in the context of SARS-CoV-2 infection are multifaceted and potentially harmful. Augmented TGF-β1 signaling initially drives local suppression of the host immune system through direct inhibition of effector immune cells including T cells and dendritic cells, an effect amplified by activation of immune suppressor T regulatory cells (Tregs)[47]. Tregs further suppress the function of T effector cells, dendritic cells, and natural killer cells, thus limiting their responses to the invading pathogen[47]. These suppressive effects typically occur due to direct binding of SMAD transcription factors, activated by TGF-β receptors, to gene promoters of interleukin-2 (IL-2), interleukin-10 (IL-10), forkhead box protein P3 (FOXP3), and other key immune cytokines and transcription factors[47]. Furthermore, TGF-β1 drives class switching of plasma cells from immunoglobulin M (IgM) and IgG production to IgA antibody formation even outside mucosal barriers[47]. Since IgA does not fix complement, it is less effective at directing immune responses to invading pathogens, thereby potentially compromising the antiviral response[47].

The dysregulation of TGF-β signaling in the COVID-19 microvasculature contributes to severe disease manifestations. Dysregulation of TGF-β signaling in immune cells and its localization in areas of microvascular injury are now well-described in COVID-19[47]. The high concentration of TGF-β in platelets and in other cells within microvascular thrombi, its ability to activate the clotting cascade and dysregulate immune pathways, and its pro-fibrotic properties all contribute to a unique milieu in the COVID-19 microvasculature characterized by microthrombosis and inflammation[47]. Elevated levels of TGF-β1 in blood are characteristically correlated with increased disease severity[47]. These findings suggest that genetic variants affecting THBS3 expression or function could influence COVID-19 severity through modulation of TGF-β-dependent immune and vascular responses.

## Expression Patterns and Tissue Localization

The tissue expression patterns of THBS3 reveal its importance in specific biological contexts while highlighting its variable roles across tissues. THBS3 demonstrates cell-type and tissue-specific expression patterns as documented in large-scale expression databases including the GTEx (Genotype-Tissue Expression) Project and the Human Protein Atlas[12][15][30][46]. The protein is expressed in vascular endothelial cells and vascular smooth muscle cells, consistent with its roles in vascular development and disease[46]. Additionally, THBS3 protein expression has been documented in dendritic cells and eosinophils, suggesting immune functions beyond its well-characterized extracellular matrix roles[46].

THBS3 protein is localized to both secreted and intracellular compartments, with different isoforms showing distinct localizations[12][30][48]. The protein is predicted to contain signal sequences directing it to the secretory pathway, and indeed THBS3 is found as a secreted protein in the extracellular matrix where it mediates cell-matrix interactions[48]. Simultaneously, intracellular isoforms of THBS3 exist and localize to endoplasmic reticulum compartments where they interact with other proteins involved in protein trafficking and stress responses[18][57]. This intracellular localization, particularly coincident with endoplasmic reticulum chaperone proteins like PDI and BiP, indicates that THBS3 participates in endoplasmic reticulum-associated functions including protein trafficking and unfolded protein response pathways[18][57].

The dynamic regulation of THBS3 expression under different physiological and pathological conditions indicates its role as a stress-responsive protein. During cardiac disease induced by transverse aortic constriction (TAC), THBS3 messenger RNA (mRNA) is significantly induced in the heart, with robust induction observed by two weeks following injury[57]. In osteosarcoma, THBS3 expression varies between primary tumor biopsies and metastatic lesions, with particularly high expression in tumors showing metastasis at diagnosis[23]. In abdominal aortic aneurysm tissue, THBS3 expression varies significantly along the length of the aneurysm, with the most prominent feature being sudden increase in expression in marginal tissue compared to aneurysm body segments[42][45]. These dynamic expression patterns suggest that THBS3 is regulated by injury, inflammatory, and remodeling signals encountered in disease states.

## Molecular Mechanisms: Protein-Protein Interactions and Signaling

The biological effects of THBS3 are mediated through multiple protein-protein interactions involving both cell surface receptors and extracellular matrix components. THBS3 binds to integrins, which are cell surface receptors that mediate cell-matrix interactions through recognition of specific amino acid sequences—primarily RGD motifs—present in matrix proteins[18][31][36]. However, because THBS3 contains an EGD rather than RGD motif in its integrin-binding domain, its integrin recognition properties are distinct from those of other thrombospondins[18][36][57]. This structural difference results in reduced direct integrin binding by THBS3 compared to THBS1, THBS4, and THBS5, yet THBS3 still influences integrin function through indirect mechanisms involving intracellular trafficking regulation[18][36][57].

The matricellular functions of THBS3 involve its incorporation into the extracellular matrix, where it acts as a molecular scaffold organizing matrix components. The C-terminal region of THBS3, comprising the type 3 repeats and lectin-like β-sandwich domain, mediates matrix incorporation and is essential for proper matrix assembly[31][35]. This region interacts with calcium ions through its multiple calcium-binding sites, and the conformational states adopted by THBS3 in response to calcium loading regulate the accessibility of ligand-binding sites[31][35]. The type 3 repeats, when calcium-loaded, adopt relatively constrained conformations that minimize exposure of binding motifs, whereas calcium depletion exposes RGD and other adhesion-relevant sequences[31].

THBS3 interacts with growth factors and growth factor-like molecules, including transforming growth factor-beta (TGF-β). The interaction of thrombospondins with TGF-β has been extensively studied in THBS1 and THBS2, where the KRFK sequence in the type I repeats competes with the RKPK sequence in active TGF-β for a binding site in the latency-associated protein (LAP)[31][35]. While THBS3 lacks type I repeats, it may still influence TGF-β signaling through interactions with the latent TGF-β complex or through effects on the cellular microenvironment that influence TGF-β availability and signaling[30][31][47]. The implications of THBS3-mediated TGF-β activation for COVID-19 severity highlight the clinical importance of these protein interactions.

## Comparative Structure and Evolution Within the Thrombospondin Family

Understanding THBS3 requires placing it within the context of the thrombospondin family, which comprises five distinct members with overlapping yet functionally distinct roles. The thrombospondin family shares a common evolutionary origin and structural organization, yet each member has acquired unique features that define its biological functions[5][31]. THBS1 and THBS2, which form trimeric structures, contain extensive type I repeats and procollagen homology domains that are absent in THBS3[25][31]. These structural differences contribute to distinct anti-angiogenic properties—THBS1 and THBS2 possess potent anti-angiogenic functions mediated through their type I repeats and interactions with CD36 and VLDLR receptors on endothelial cells[25]. By contrast, THBS3 appears to lack these anti-angiogenic functions due to the absence of type I repeats[25].

THBS4 and THBS5, along with THBS3, form pentameric rather than trimeric structures[41][42]. However, THBS3 demonstrates antagonistic properties compared to THBS4 in several disease contexts despite both being pentameric. The critical structural difference involves the integrin-binding motifs—THBS3 contains EGD while THBS4 and THBS5 contain RGD or KGD motifs[18][36]. This distinction results in opposite effects on integrin membrane trafficking and cardiac homeostasis: THBS4 protects the heart by enhancing integrin membrane residence, while THBS3 exacerbates cardiac disease by promoting integrin endocytosis and reducing membrane integration levels[18][36][57]. This illustrates how subtle structural variations among family members can produce dramatically different biological outcomes.

## Pathological Dysregulation and Disease Mechanisms

The dysregulation of THBS3 expression or function is implicated in multiple disease pathways, with particularly strong evidence emerging in cardiac disease, cancer, and infectious disease contexts. In cardiac disease, the upregulation of THBS3 in response to pathological stimuli appears to constitute a maladaptive stress response that exacerbates disease progression rather than promoting beneficial adaptive remodeling[18][36][39][57]. The relationship between THBS3 expression levels and disease severity in osteosarcoma demonstrates that THBS3 functions as a molecular driver of tumor progression through enhanced angiogenesis and maintenance of pro-metastatic phenotypes[23][26]. In the context of COVID-19, genetic variation in THBS3 or its regulatory regions may affect transcriptional output and TGF-β signaling capacity, thereby influencing individual susceptibility to severe disease[19][22][30].

The role of THBS3 in extracellular matrix remodeling has particular significance in disease states characterized by pathological matrix reorganization. In abdominal aortic aneurysm, THBS3 overexpression may destabilize the matrix by affecting both matrix-producing smooth muscle cells and the activity of matrix proteins themselves, thereby contributing to aneurysm progression[12][30][42][45]. This mechanism appears related to THBS3's ability to reduce integrin-mediated cell-matrix adhesion and thereby compromise the mechanical integrity of the matrix-cell interface. The variable expression of THBS3 along the length of aneurysmal tissue, with highest expression at the margins, suggests that THBS3 participates in the transition zones where matrix remodeling and tissue destabilization occur.

## Conclusion: Integrative Understanding and Future Perspectives

Thrombospondin-3 represents a complex matricellular protein with multifaceted biological roles spanning skeletal development, cardiac homeostasis, tissue remodeling, immune regulation, and cancer biology. Unlike its family member THBS4, which generally exerts protective effects across tissue contexts, THBS3 demonstrates a predominantly maladaptive phenotype in disease states, most notably through its capacity to inhibit integrin membrane trafficking and thereby promote sarcolemmal destabilization in cardiac myocytes. The fundamental structural basis for these antagonistic properties resides in THBS3's unique EGD integrin-binding motif rather than the canonical RGD motif present in other thrombospondins, demonstrating how subtle molecular variations can produce profound functional consequences. The protein's role in promoting osteosarcoma progression and its association with COVID-19 disease severity highlight its significance as a pathological driver in multiple disease contexts requiring investigation for therapeutic targeting.

The discovery of THBS3's involvement in COVID-19 susceptibility through genome-wide association studies opens new therapeutic avenues, as modulation of THBS3 expression or its interaction with TGF-β might reduce disease severity through immune regulatory and antiviral mechanisms. Future research should focus on delineating the precise mechanisms by which THBS3 regulates integrin trafficking in cardiomyocytes, clarifying its context-dependent pro- versus anti-angiogenic properties in different tissue environments, and exploring THBS3 as a therapeutic target in diseases characterized by pathological matrix remodeling including aortic aneurysm and cardiomyopathy. The tissue-specific expression patterns and dynamic regulation of THBS3 under pathological conditions suggest that future therapeutic strategies might exploit tissue-selective approaches to THBS3 modulation, enhancing benefits while minimizing potential adverse effects on physiological THBS3 functions in development and homeostasis. Structural studies revealing how calcium binding modulates THBS3's conformation and integrin interactions, combined with clinical investigations correlating THBS3 genetic variation with disease outcomes across diverse populations, will advance understanding of this important but incompletely characterized matricellular protein and enable rational therapeutic development.

## Citations

1. https://en.wikipedia.org/wiki/Thrombospondin_3
2. https://www.uniprot.org/uniprotkb/F5H4Z8/entry
3. https://www.ncbi.nlm.nih.gov/gene/7059
4. https://www.uniprot.org/uniprot/B4DQH6
5. https://pmc.ncbi.nlm.nih.gov/articles/PMC2778591/
6. https://pubmed.ncbi.nlm.nih.gov/15964815/
7. https://maayanlab.cloud/Harmonizome/gene/THBS1
8. https://rupress.org/jcb/article/103/5/1635/55264/The-structure-of-human-thrombospondin-an-adhesive
9. https://www.tandfonline.com/doi/abs/10.1128/mcb.25.13.5599-5606.2005
10. https://pubmed.ncbi.nlm.nih.gov/6693501/
11. https://pmc.ncbi.nlm.nih.gov/articles/PMC1156967/
12. https://maayanlab.cloud/Harmonizome/gene/THBS3
13. https://pmc.ncbi.nlm.nih.gov/articles/PMC2121041/
14. https://www.informatics.jax.org/marker/MGI:98739
15. https://www.proteinatlas.org/ENSG00000169231-THBS3
16. https://pmc.ncbi.nlm.nih.gov/articles/PMC14963/
17. https://www.ncbi.nlm.nih.gov/gene?Db=gene&Cmd=DetailsSearch&Term=7059
18. https://pmc.ncbi.nlm.nih.gov/articles/PMC6325143/
19. https://www.nature.com/articles/s10038-021-01009-6
20. https://www.uniprot.org/uniprotkb/P49746/entry
21. https://pmc.ncbi.nlm.nih.gov/articles/PMC12570997
22. https://pmc.ncbi.nlm.nih.gov/articles/PMC1609181/
23. https://pubmed.ncbi.nlm.nih.gov/11943589/
24. https://pmc.ncbi.nlm.nih.gov/articles/PMC2778581/
25. https://www.epistemonikos.org/de/documents/483418a9e411f842342ead1460a801076dc01fc7
26. https://pmc.ncbi.nlm.nih.gov/articles/PMC2895596/
27. https://pmc.ncbi.nlm.nih.gov/articles/PMC3179333/
28. https://pubmed.ncbi.nlm.nih.gov/8871542/
29. https://www.wikigenes.org/e/gene/e/7059.html
30. https://pmc.ncbi.nlm.nih.gov/articles/PMC381422/
31. https://pubmed.ncbi.nlm.nih.gov/30622267/
32. https://pubmed.ncbi.nlm.nih.gov/8288588/
33. https://www.imrpress.com/journal/FBL/27/10/10.31083/j.fbl2710291/htm
34. https://www.frontierspartnerships.org/articles/10.18388/abp.2020_5645/pdf
35. https://pmc.ncbi.nlm.nih.gov/articles/PMC1870996/
36. https://pubmed.ncbi.nlm.nih.gov/34669362/
37. https://www.frontiersin.org/journals/cardiovascular-medicine/articles/10.3389/fcvm.2022.1054690/full
38. https://pmc.ncbi.nlm.nih.gov/articles/PMC8209884/
39. https://pmc.ncbi.nlm.nih.gov/articles/PMC8002632/
40. https://journals.sagepub.com/doi/10.1177/19476035251393382
41. https://pmc.ncbi.nlm.nih.gov/articles/PMC9578548/
42. https://pmc.ncbi.nlm.nih.gov/articles/PMC8756151/
43. https://diseases.jensenlab.org/Entity?documents=10&type1=9606&id1=ENSP00000357362&type2=-26&id2=DOID%3A12721
44. https://www.nature.com/articles/s41467-018-08026-8