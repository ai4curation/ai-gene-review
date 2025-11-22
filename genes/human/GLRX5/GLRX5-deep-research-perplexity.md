---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2025-11-15T16:13:18.370033'
end_time: '2025-11-15T16:15:55.723999'
duration_seconds: 157.35
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: GLRX5
  gene_symbol: GLRX5
  uniprot_accession: Q86SX6
  protein_description: 'RecName: Full=Glutaredoxin-related protein 5, mitochondrial;
    AltName: Full=Monothiol glutaredoxin-5; Flags: Precursor;'
  gene_info: Name=GLRX5; Synonyms=C14orf87;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the glutaredoxin family. Monothiol subfamily.
  protein_domains: Glutaredoxin. (IPR002109); GRX_PICOT-like. (IPR033658); Monothiol_GRX-rel.
    (IPR004480); Thioredoxin-like_sf. (IPR036249); Glutaredoxin (PF00462)
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 46
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q86SX6
- **Protein Description:** RecName: Full=Glutaredoxin-related protein 5, mitochondrial; AltName: Full=Monothiol glutaredoxin-5; Flags: Precursor;
- **Gene Information:** Name=GLRX5; Synonyms=C14orf87;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the glutaredoxin family. Monothiol subfamily.
- **Key Domains:** Glutaredoxin. (IPR002109); GRX_PICOT-like. (IPR033658); Monothiol_GRX-rel. (IPR004480); Thioredoxin-like_sf. (IPR036249); Glutaredoxin (PF00462)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "GLRX5" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'GLRX5' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **GLRX5** (gene ID: GLRX5, UniProt: Q86SX6) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

<think>
The user is asking me to write a comprehensive research report on GLRX5 (glutaredoxin-related protein 5, mitochondrial) with UniProt accession Q86SX6 in humans. Let me first verify from the search results that I have the correct gene/protein.

From the search results, I can confirm:
1. Source [1] (NCBI) - describes GLRX5 as "51218 - Gene Result GLRX5 glutaredoxin 5 [ (human)] - NCBI" - involves biogenesis of iron-sulfur clusters
2. Source [3] and [6] - Functional Analysis of GLRX5 Mutants - "Glutaredoxin 5 (GLRX5) is a 156 amino acid mitochondrial protein that plays an essential role in mitochondrial iron-sulfur cluster transfer"
3. Source [7] and [19] - Crystal structure paper - "Human GLRX5 (glutaredoxin 5) is an evolutionarily conserved thiol–disulfide oxidoreductase that has a direct role in the maintenance of normal cytosolic and mitochondrial iron homoeostasis"
4. Source [10] - "GLRX5 is a mitochondrial protein required for iron-sulfur cluster biogenesis"
5. Source [15] - GeneCards summary confirms the same
6. Source [18] - UniProt - "GLRX5 is a mitochondrial glutaredoxin involved in iron-sulfur cluster transfer"

So yes, I have the correct gene. GLRX5 is a 156 amino acid mitochondrial protein that is a monothiol glutaredoxin involved in iron-sulfur cluster biogenesis and transfer. Let me plan my comprehensive report.

## Planning my approach:

1. **Title & Summary paragraph** - Overview of GLRX5 and its central role in iron-sulfur cluster biogenesis


2. **Structural Characteristics and Domain Organization** - Crystal structure details, tetrameric assembly, and active site architecture
3. **Primary Biochemical Function** - Iron-sulfur cluster assembly and transfer mechanisms, cofactor interactions
4. **Subcellular Localization and Import** - Mitochondrial targeting sequences and compartmentalization
5. **Role in Iron-Sulfur Cluster Biogenesis Pathway** - Integration with ISC machinery and protein interactions
6. **Tissue-Specific Expression and Erythropoiesis** - Particular importance in erythroid differentiation and heme synthesis
7. **Clinical Significance** - Disease associations and pathological implications
8. **Mechanistic Insights from Recent Research** - Structural dynamics and conformational transitions during cluster transfer
9. **Integration with Cellular Iron Homeostasis** - Connections to iron regulatory networks and mitochondrial iron metabolism
10. **Conclusion and Future Perspectives** - Synthesis of findings and emerging research questions

I'm organizing this report to build from structural foundations through functional mechanisms, then connecting to broader cellular processes and clinical relevance. The framework moves from molecular details to systemic implications, establishing how this protein operates within multiple biological contexts before addressing disease states and future research directions.
</think>

# GLRX5: Mitochondrial Iron-Sulfur Cluster Transfer and Biogenesis

GLRX5 (glutaredoxin 5), also known as glutaredoxin-related protein 5 or monothiol glutaredoxin-5, is a 156 amino acid mitochondrial protein that occupies a critical position in the mammalian iron-sulfur (Fe-S) cluster assembly machinery[3][6][15]. This monothiol glutaredoxin functions as a key metallochaperone that receives [2Fe-2S] clusters from scaffold proteins and facilitates their transfer to downstream recipient proteins involved in fundamental cellular processes including electron transport, DNA metabolism, and heme biosynthesis[10][26][48]. As a conserved component of the mitochondrial iron-sulfur cluster (ISC) assembly system, GLRX5 directly maintains normal cytosolic and mitochondrial iron homeostasis while simultaneously affecting erythropoiesis and heme synthesis, particularly in erythroid cells where it is highly expressed[3][33][53]. Mutations in GLRX5 result in two distinct human disease phenotypes—autosomal recessive sideroblastic anemia and variant nonketotic hyperglycinemia—highlighting the clinical importance of proper Fe-S cluster biogenesis[6][13][32]. The recent determination of GLRX5's crystal structure bound to [2Fe-2S] clusters and detailed characterization of its molecular interactions have revealed novel mechanisms of cluster transfer and cellular redox regulation that distinguish this protein from other redox-active proteins in the cell.

## Structural Organization and Biochemical Characterization

### Crystal Structure and Tetrameric Assembly

The three-dimensional structure of human GLRX5 represents a significant breakthrough in understanding monothiol glutaredoxin function and iron-sulfur cluster coordination. Crystal structures of human GLRX5 bound to [2Fe-2S] clusters revealed a remarkable tetrameric organization with two [2Fe-2S] clusters completely buried in the interior of the protein complex[7][28][51]. This tetrameric architecture contrasts sharply with the monomeric organization of the metal-free apoprotein, indicating that cluster binding induces dramatic conformational reorganization and protein assembly[51]. Each [2Fe-2S] cluster is ligated by the N-terminal active-site cysteine residue (Cys67) from two protomers combined with two cysteine thiols from two molecules of reduced glutathione (GSH)[7][28][51]. This coordination geometry differs notably from that observed in iron-sulfur-bound human GLRX2, with GLRX5 displaying a more extended conformation in the two subunits coordinating the cluster and more extensive intersubunit interactions involving conserved residues among monothiol glutaredoxins[7][28].

The structural data reveals that the [2Fe-2S] clusters are deeply shielded from solvent exposure through protection by the conserved β1-α2 loop and phenylalanine residue 69 along with the coordinating GSH molecules[7][28][51]. Mass spectrometry analyses demonstrated that in the absence of bound iron-sulfur clusters, GLRX5 undergoes glutathionylation at cysteine residues, a reversible modification that protects the catalytic thiols from unwanted oxidation and potentially facilitates cluster transfer and acceptance[7][28][55]. The apoprotein form of GLRX5 exhibits reduced glutathione mixed disulfide reduction activity at approximately 100-fold lower rates compared to GLRX2, yet retains activity as a glutathione-dependent electron donor for mammalian ribonucleotide reductase[7][28], demonstrating retained redox activity even in the absence of bound clusters.

### Protein Domains and Structural Motifs

GLRX5 belongs to the glutaredoxin family and specifically to the monothiol subfamily, characterized by the conserved CGFS active-site motif[53]. This sequence motif distinguishes monothiol glutaredoxins from dithiol glutaredoxins that contain CXXC domains[53]. Bioinformatic analysis reveals that GLRX5 contains multiple structural domains: the core glutaredoxin domain (IPR002109), the thioredoxin-like superfamily domain (IPR036249), and monothiol glutaredoxin-related sequences (IPR004480)[15][48]. Additionally, GLRX5 harbors a GRX_PICOT-like domain (IPR033658), linking it to related proteins containing PICOT domains that function in cellular signaling and protein-protein interactions[15][48]. The catalytic CGFS motif is positioned at the N-terminus following the mitochondrial targeting sequence, placing the active site in an optimal position for substrate recognition and catalysis[3][6].

Within the CGFS active site, Cys67 serves as the primary nucleophilic residue attacking disulfide bonds and coordinating iron-sulfur clusters, while the flanking glycine and phenylalanine residues contribute to substrate specificity and cluster binding[3][6]. The conserved serine residue following the CGFS motif participates in cluster ligation through its interaction with glutathione molecules[3][6]. Additional conserved residues critical for GLRX5 function include K59, T108, and D123, which form part of the glutathione binding site and are essential for efficient [Fe-S] assembly and cluster coordination[53]. Site-directed mutagenesis studies demonstrated that mutation of K59 to Q, C67 to S, or T108 to V abolished the characteristic absorption pattern of bound [2Fe-2S] clusters upon protein reconstitution, confirming the essential roles of these residues in cluster assembly[53].

## Subcellular Localization and Mitochondrial Targeting

### Import into Mitochondria

GLRX5 is synthesized as a precursor protein with an N-terminal mitochondrial targeting sequence that directs the protein to the mitochondrial matrix. Immunofluorescence staining in HeLa cells demonstrated that endogenous GLRX5 expression colocalizes with mitochondrial markers, and subcellular fractionation coupled with Western blotting confirmed GLRX5 localization predominantly in the mitochondrial fraction[10][33][53]. The mature, processed form of GLRX5 lacks approximately the first 29 amino acids of the translation product, corresponding to the cleaved N-terminal targeting presequence[8][50]. This processing occurs after the protein crosses the mitochondrial membranes via the translocon machinery and is processed by the mitochondrial processing peptidase (MPP) within the matrix[8][50].

Following mitochondrial subfractionation under hypotonic conditions that disrupt the outer membrane, GLRX5 entirely colocalizes with matrix proteins, specifically showing colocalization with lipoic acid-modified proteins including pyruvate dehydrogenase (PDH) and α-ketoglutarate dehydrogenase (α-KGDH)[8][50]. This colocalization with lipoylated proteins provides the first functional clue to GLRX5's role in the biogenesis of Fe-S proteins, as both PDH and α-KGDH require iron-sulfur clusters for assembly and function. The critical importance of the N-terminal targeting sequence for proper localization was demonstrated through deletion studies: whereas wild-type GLRX5 localizes to mitochondria, constructs lacking the first 8 or 23 amino acids remain exclusively in the cytoplasm and fail to complement the functional defects caused by GLRX5 absence[8][50]. This strict requirement for appropriate N-terminal targeting reflects the segregation of GLRX5 function to the mitochondrial compartment, where initial iron-sulfur cluster assembly occurs.

### Compartmentalization and Functional Implications

The mitochondrial localization of GLRX5 places this protein at the nexus of two critical cellular processes: initial iron-sulfur cluster assembly on scaffold proteins and the distribution of pre-formed clusters to recipient proteins throughout the cell. The ISC (iron-sulfur cluster) assembly machinery is concentrated in the mitochondrial matrix, and mature clusters assembled on the scaffold protein ISCU must be transferred to GLRX5 for subsequent delivery to target proteins[22][31][37]. This architectural arrangement allows the ISC system to operate in the specialized reducing environment of the mitochondrial matrix, where pyridoxal-5'-phosphate-dependent cysteine desulfurase (NFS1) and other biosynthetic enzymes function optimally. By maintaining GLRX5 exclusively in mitochondria, the cell ensures that this critical cluster transfer protein remains intimately connected with the upstream assembly machinery while still being positioned to interface with the chaperone systems that deliver clusters to mitochondrial and extramiochondrial recipients[31][37].

## Primary Biochemical Function: Iron-Sulfur Cluster Transfer

### Cluster Binding and Coordination Mechanism

The fundamental biochemical role of GLRX5 is the binding and transfer of [2Fe-2S] clusters synthesized on the ISCU scaffold protein to downstream recipient proteins that require iron-sulfur clusters for their catalytic activity or structural integrity. GLRX5 can homodimerize and assemble [2Fe-2S] clusters in vitro, enabling it to function as a functional iron-sulfur scaffold or sensor protein[10][33][53]. Reconstitution studies reveal that GLRX5 assembly of an [Fe-S] cluster requires the presence of reduced glutathione (GSH), which serves as a ligand coordinating the cluster along with cysteine residues from two GLRX5 monomers[10][33][53]. After protein reconstitution and purification, GLRX5 acquires a characteristic dark brown coloration and displays strong absorption peaks at 330 and 420 nanometers with a shoulder at 520 nanometers, an absorption pattern that is diagnostic of bound [2Fe-2S] clusters[53].

Detailed spectroscopic characterization indicates that in the fully loaded tetrameric form with bound [2Fe-2S] clusters, GLRX5 exists as a homodimer bridged by a single [2Fe-2S]²⁺ cluster in solution, even though the crystal structure reveals a tetrameric arrangement[26]. This apparent discrepancy between solid-state crystal packing and solution oligomerization states suggests that GLRX5 undergoes dynamic conformational transitions depending on solution conditions and protein concentration[26]. The [2Fe-2S] cluster in solution GLRX5 is stably bound and is not released into the glutathione pool under physiological concentrations of GSH, indicating that GLRX5 functions as a protective metallochaperone that prevents inappropriate cluster release while maintaining substrate accessibility for transfer reactions[26].

### Cluster Transfer to Recipient Proteins

GLRX5 mediates the transfer of [2Fe-2S] clusters to a diverse set of recipient proteins, including iron-regulatory protein 1 (IRP1), mitochondrial aconitase (m-aconitase), ferrochelatase, succinate dehydrogenase subunit B, lipoic acid synthase, and [4Fe-4S] cluster assembly factors[3][6][14]. The cluster transfer process occurs through a specific protein-protein recognition mechanism involving the structural plasticity of GLRX5's dimeric state[26]. The transition between conformational states of holo-GLRX5 (cluster-bound form) drives the cluster transfer event by exposing the coordination interface to recipient proteins while maintaining cluster shielding from bulk solution[26]. This mechanism contrasts with simpler transfer pathways seen in some bacterial systems, instead representing a sophisticated metallochaperone function where protein-protein interactions control cluster availability.

The cluster transfer from GLRX5 to various recipient proteins proceeds through transient, cluster-mediated protein-protein intermediates[26]. For [2Fe-2S] apoproteins such as human ISCA1 and ISCA2, the transfer occurs rapidly within seconds in a spontaneous fashion, independent of chaperone assistance[31][37][43]. However, for the formation of [4Fe-4S] clusters from [2Fe-2S] donors, the process requires additional factors including ISCA1-ISCA2-IBA57 and electron transfer components[37][43]. Electrons from mitochondrial ferredoxin 2 (FDX2) catalyze a reductive [2Fe-2S] cluster fusion reaction on ISCA1-ISCA2 in an IBA57-dependent fashion, ultimately producing [4Fe-4S] clusters that are subsequently transferred to final recipient proteins[37][43].

### Mechanism of Monothiol Glutaredoxin Activity

The monothiol glutaredoxin activity of GLRX5 differs fundamentally from the dithiol mechanism employed by other glutaredoxins such as GLRX1 and GLRX2. Detailed kinetic and structural studies reveal that GLRX5-catalyzed redox reactions occur primarily through a monothiol mechanism involving only the N-terminal active-site cysteine (Cys67)[27][30]. In this mechanism, when GLRX5 becomes oxidized to form a mixed disulfide with glutathione (Grx-SSG intermediate), subsequent reduction by a second glutathione molecule regenerates the active enzyme[27][30]. The reduction rate constants for the individual redox reactions in GLRX5-catalyzed processes range from 10⁵ to 10⁶ M⁻¹s⁻¹, values typical of glutaredoxin-catalyzed redox chemistry[9].

Critical structural differences between GLRX5 and dithiol glutaredoxins determine their respective functions. The loop structure adjacent to the active site in monothiol glutaredoxins such as GLRX5 is distinct from that in dithiol glutaredoxins, and this loop serves as a key determinant of whether a glutaredoxin functions as an oxidoreductase or as an iron-sulfur cluster transferase[27]. Engineering studies in which a CGFS-type loop was introduced into a CxxC/S-type glutaredoxin switched its function from oxidoreductase to Fe-S transferase, while the reciprocal modification abolished Fe-S transferase activity and activated oxidoreductase function[27]. This demonstrates that the loop architecture is the primary molecular determinant distinguishing GLRX5's specialized Fe-S transfer function from the general redox chemistry catalyzed by other glutaredoxins.

## Role in the Iron-Sulfur Cluster Assembly Machinery

### Position in the ISC Pathway

GLRX5 occupies a central position in the three-phase mitochondrial iron-sulfur cluster assembly pathway that has been conserved throughout evolution. In the first phase, [2Fe-2S] clusters are synthesized de novo on the ISCU scaffold protein through the coordinated action of the cysteine desulfurase complex comprising NFS1, ISD11, and ACP (acyl carrier protein)[17][22]. NFS1 catalyzes the conversion of cysteine to alanine while generating a persulfide intermediate that transfers sulfane sulfur to a conserved cysteine residue (Cys138 in human ISCU)[17][22]. Frataxin (FXN) acts as an allosteric regulator of this initial assembly step, driving efficient sulfur transfer from the NFS1 cysteine loop to ISCU and facilitating conformational changes that complete the active site of the NFS1/ISD11/ACP homodimeric complex[17][22].

The second phase of the pathway involves transfer of the newly assembled [2Fe-2S] cluster from ISCU to GLRX5, mediated by a mitochondrial Hsp70 chaperone system comprised of HSPA9 and the dedicated J-type cochaperone HSC20[31][37][41][42]. Unlike prokaryotic systems where the Ssq1/Jac1 chaperone pair is essential for efficient cluster transfer to the monothiol glutaredoxin Grx5, the human chaperone system (HSPA9/HSC20) surprisingly exhibits an inhibitory rather than stimulatory role in cluster transfer from ISCU to GLRX5[31]. In the human system, chaperones instead promote the reverse transfer from GLRX5 back to ISCU, suggesting organism-specific control mechanisms that permit directional tuning of cluster redistribution[31]. This distinction between prokaryotic and eukaryotic mechanisms highlights the sophistication of cellular Fe-S chemistry regulation.

Once GLRX5 receives the cluster from ISCU, the third phase involves redistribution of [2Fe-2S] clusters to diverse recipient proteins. For [2Fe-2S] apoproteins such as those found in ISCA proteins, transfer occurs spontaneously and rapidly, but for [4Fe-4S] cluster formation, additional ISC factors must participate[31][37]. Specifically, ISCA1-ISCA2-IBA57 function together in [4Fe-4S] cluster assembly through a reductive conversion mechanism wherein two [2Fe-2S] clusters are fused into a single [4Fe-4S] cluster under the action of electrons provided by the ferredoxin FDX2[37][43][46]. This late-acting machinery specifically catalyzes the electron-dependent fusion of GLRX5-bound [2Fe-2S]²⁺ clusters into [4Fe-4S]²⁺ clusters required for proteins such as aconitase, succinate dehydrogenase, and radical S-adenosylmethionine enzymes[37][43][46].

### Interaction with Upstream Scaffold Proteins

GLRX5 physically interacts with the main scaffold protein ISCU2 to facilitate cluster transfer from the initial assembly site to GLRX5 for further processing[31][34][37]. Kinetic studies measuring cluster exchange reactivity reveal that in the absence of HSPA9 and HSC20 chaperones, human ISCU transfers its [2Fe-2S] cluster to apo-GLRX5 with rapid kinetics[31]. The apparent rate constant for this transfer in certain conditions reaches approximately 100 M⁻¹min⁻¹ or faster, indicating highly favorable thermodynamics and kinetics for this particular transfer step[31]. Computational modeling and structural studies suggest that the interaction between GLRX5 and ISCU involves recognition of GLRX5 as a physiological target protein for ISCU-bound clusters[31].

Recent proteomic and biochemical analyses have identified direct interactions between GLRX5 and multiple components of the Fe-S assembly machinery[25][31]. GLRX5 has been shown to physically interact with the cysteine desulfurase NFS1 and other members of the ISC complex, suggesting intimate functional coupling between cluster synthesis on ISCU and transfer to GLRX5[25][31]. Additionally, GLRX5 interacts with the iron-sulfur cluster carrier protein NFU1, which itself can function as a secondary carrier for [4Fe-4S] clusters[31][34][38]. The interaction between GLRX5 and NFU1 reveals bidirectional cluster transfer with specific rate constants depending on transfer direction, and surprisingly, NFU1 appears to be a more physiologically relevant donor of [2Fe-2S] clusters to human GLRX5 compared to ISCU in certain cellular contexts[31][34].

### Downstream Target Recognition and Cluster Delivery

GLRX5 receives [2Fe-2S] clusters from ISCU and mediates their transfer to a diverse array of recipient proteins throughout the mitochondria and beyond. One of the most extensively characterized recipients is iron regulatory protein 1 (IRP1), a bifunctional protein that functions as either cytosolic aconitase when containing its [4Fe-4S] cluster or as an iron-responsive element (IRE)-binding protein when lacking the cluster[3][6][10][33]. The assembly of the [4Fe-4S] cluster in IRP1 depends critically on GLRX5, as IRP1-deficient cells exhibit reduced IRP1 Fe-S cluster content and loss of the IRE-binding regulatory function[10][33]. This functional connection between GLRX5 and IRP1 establishes GLRX5 as a key regulator of cellular iron homeostasis through its control of IRP1 activity.

Mitochondrial aconitase (m-aconitase, encoded by ACO2) represents another major target of GLRX5-mediated cluster transfer. This [4Fe-4S]-containing enzyme catalyzes the isomerization of citrate to isocitrate within the tricarboxylic acid cycle and requires its iron-sulfur cluster for catalytic activity[10][33][37]. GLRX5 deficiency results in decreased m-aconitase activity and impaired citric acid cycle flux, contributing to the mitochondrial dysfunction observed in GLRX5-deficient cells[10][33][37]. Additionally, GLRX5 participates in the maturation of ferrochelatase, the terminal enzyme in heme biosynthesis that catalyzes the insertion of iron into protoporphyrin IX to form heme[3][13][14][16]. The availability of iron-sulfur clusters from GLRX5 directly influences ferrochelatase protein levels and activity, linking GLRX5 to heme synthesis and erythropoiesis[3][13].

## Tissue-Specific Expression and Role in Erythropoiesis

### Erythroid-Specific Expression Pattern

Quantitative reverse-transcription polymerase chain reaction (qRT-PCR) analysis of sorted cells from mouse bone marrow revealed that GLRX5 mRNA levels are at least 100-fold higher in erythroblast cells compared to macrophages and other bone marrow cell populations[53]. This dramatic tissue-specific enrichment in erythroid cells provides a critical clue to GLRX5's specialized role in red blood cell development. Bioinformatic analysis of human GLRX5 gene expression across tissues confirmed that while GLRX5 is minimally expressed in most cell types, it achieves notably high expression in CD71⁺ early erythroid cells from bone marrow, matching the expression patterns of ALAS2 (5-aminolevulinic acid synthase 2, the erythroid-specific form of the first enzyme in heme biosynthesis) and FECH (ferrochelatase, the terminal enzyme in heme synthesis)[53]. This coordinate expression of GLRX5 with rate-limiting heme biosynthetic enzymes suggests that GLRX5 has been selectively retained and amplified in erythroid cells due to specialized requirements for iron-sulfur cluster delivery in the context of massive hemoglobin production.

The high expression level of GLRX5 in erythroid cells indicates that proper Fe-S cluster biogenesis is particularly rate-limiting or critical during erythropoiesis, the differentiation of hematopoietic progenitor cells into mature red blood cells. During terminal erythroid differentiation, cells must synthesize enormous amounts of hemoglobin to fill the cytoplasm before nucleus extrusion, with hemoglobin comprising approximately 95% of total protein mass in mature red blood cells. This extraordinary biosynthetic demand places exceptional requirements on the cellular Fe-S cluster assembly machinery to support heme synthesis and iron metabolism.

### GLRX5 and Heme Biosynthesis

The functional connection between GLRX5 and heme biosynthesis manifests through multiple molecular mechanisms. GLRX5 is required for normal regulation of hemoglobin synthesis through its control of the iron-sulfur protein ACO1 (aconitase 1), the cytosolic form of aconitase that also functions as iron regulatory protein 1[15][33][48]. As a bifunctional protein, IRP1 responds to changes in cellular iron status: when iron-sulfur clusters are available, IRP1 incorporates its [4Fe-4S] cluster and functions as cytosolic aconitase, catalyzing the interconversion of citrate and isocitrate; when iron becomes limiting or clusters become unavailable, the cluster is lost and IRP1 switches to its IRE-binding mode, reducing translation of ALAS2 mRNA and ferroportin mRNA while increasing transferrin receptor expression[10][33].

GLRX5 deficiency results in impaired [Fe-S] cluster biosynthesis, which prevents IRP1 from assembling its [4Fe-4S] cluster and causes constitutive activation of IRP1's IRE-binding function[10][33]. This persistent activation of IRP1 in GLRX5-deficient erythroid cells represses ALAS2 translation through IRE-mediated mechanisms, dramatically reducing the protein levels and activity of this rate-limiting heme biosynthetic enzyme[10][13][33][36]. The consequences extend further: decreased ALAS2 activity reduces the production of succinyl-CoA-derived intermediates for heme synthesis, while simultaneously GLRX5 deficiency impairs the assembly of the [Fe-S] cluster required by lipoic acid synthase, an enzyme essential for lipoylation of the pyruvate dehydrogenase complex and α-ketoglutarate dehydrogenase complex—both of which are required for generating the energy and metabolic intermediates needed for heme synthesis[13][20][23].

Additionally, ferrochelatase, the final enzyme in the heme biosynthetic pathway, requires an iron-sulfur cluster for both its structural stability and catalytic activity[16]. In GLRX5-deficient erythroid cells, ferrochelatase protein levels become markedly reduced, and the residual enzyme exhibits dramatically decreased activity despite remaining protein being present[13]. This specific impairment of ferrochelatase activity without accumulation of porphyrin precursors (in contrast to erythropoietic protoporphyria, where ferrochelatase deficiency alone causes porphyrin accumulation) indicates that GLRX5 deficiency reduces ferrochelatase activity through multiple mechanisms including reduced cluster assembly, altered protein stability, and dysregulated enzyme localization[13].

## Clinical Manifestations and Genetic Disease

### Sideroblastic Anemia

Sideroblastic anemia represents one of the primary clinical manifestations of GLRX5 mutations, characterized by the pathological accumulation of iron in erythroblast mitochondria (producing "ringed sideroblasts" when examined histologically)[3][4][10][33]. This condition demonstrates the critical importance of GLRX5 in iron homeostasis within developing red blood cells. The first documented human GLRX5 mutation associated with sideroblastic anemia was identified in an Italian patient who carried a mutation (A294G) in the last nucleotide of exon 1, which impeded normal intron 1 splicing and dramatically reduced GLRX5 mRNA levels[10][33][36]. This patient did not develop clinical symptoms until midlife, when he presented with microcytic hypochromic anemia accompanied by type 2 diabetes, cirrhosis, and liver iron overload[10][33][36]. The late onset of symptoms despite the presence of a GLRX5 mutation throughout life suggests that compensatory mechanisms maintain Fe-S cluster biogenesis at marginal but functional levels until additional physiological stresses overwhelm residual capacity.

A second well-characterized case involved a Chinese patient with congenital sideroblastic anemia who carried two compound heterozygous missense mutations in GLRX5 (c.301A>C causing K101Q and c.443T>C causing L148S)[3][6][14]. The K101Q mutation was found to prevent binding of the [Fe-S] cluster to GLRX5 protein, while the L148S mutation interfered with [Fe-S] transfer from GLRX5 to iron regulatory protein 1, mitochondrial aconitase, and ferrochelatase[3][6][14]. The biochemical consequences of these mutations differed substantially: the K101Q mutation blocked cluster assembly onto GLRX5, while L148S permitted cluster assembly but prevented subsequent transfer to recipient proteins, demonstrating that different point mutations in GLRX5 produce distinct biochemical defects[3][6][14].

The pathophysiology of GLRX5-associated sideroblastic anemia involves a dual mechanism of iron dysregulation: mitochondrial iron accumulates due to impaired iron-sulfur cluster biogenesis (and therefore impaired synthesis of iron-sulfur-containing proteins that normally participate in iron storage and metabolism), while simultaneously, cytosolic iron becomes depleted due to activation of iron regulatory proteins[10][33]. In patient fibroblasts and lymphoblasts derived from the Italian GLRX5 patient, GLRX5 protein was completely undetectable[10][33]. These GLRX5-deficient patient cells exhibited a slow-growth phenotype that could be rescued by transfection with wild-type GLRX5 or viral transduction of the GLRX5 gene[10][33]. Rescue reversed the mitochondrial iron overload phenotype and increased the activities of both cytosolic and mitochondrial aconitase, demonstrating functional recovery of the Fe-S cluster assembly pathway[10][33].

### Variant Nonketotic Hyperglycinemia

A distinct clinical phenotype associated with GLRX5 mutations manifests as variant nonketotic hyperglycinemia (variant NKH), a neurological disease characterized by elevated glycine levels, developmental delay, spasticity, and progressive neurodegeneration[32][35][45]. Variant NKH patients with GLRX5 mutations display normal development initially, followed by childhood-onset spastic paraplegia, spinal cord involvement, and optic atrophy[32][35][45]. The biochemical basis for this neurological phenotype involves GLRX5's role in lipoate synthesis through its participation in iron-sulfur cluster biogenesis for lipoic acid synthase (LIAS), an enzyme absolutely required for converting octanoyl groups into lipoyl moieties[13][20][23][35].

Lipoate serves as an essential cofactor for five key redox-active enzymes in humans: pyruvate dehydrogenase complex, α-ketoglutarate dehydrogenase complex, branched-chain ketoacid dehydrogenase complex, 2-oxoadipate dehydrogenase complex, and the glycine cleavage system (GCS)[20][23][35]. The glycine cleavage system, comprising glycine decarboxylase (GLDC), glycine cleavage H protein (GCSH), T protein, and L protein, catalyzes the oxidative decarboxylation of glycine and is localized to the inner mitochondrial membrane where it generates one-carbon units for biosynthesis while removing excess glycine[20][23][35]. When GLRX5 mutations impair lipoate synthesis through failure of iron-sulfur cluster assembly on LIAS, the glycine cleavage system becomes deficient, leading to glycine accumulation in body fluids and characteristic elevated cerebrospinal fluid glycine levels[32][35][45].

One reported case of variant NKH with GLRX5 mutations involved a Chinese girl who carried genetic lesions in GLRX5 and presented with developmental regression, spasticity, and developmental delay beginning around six months of age[32]. Her clinical presentation included spastic paralysis of all extremities with reduced muscle strength, hyperactive tendon reflexes, clonus, and positive Babinski sign—findings consistent with upper motor neuron disease and central nervous system involvement[32]. Brain MRI revealed bilateral cavitating leukoencephalopathy with long tract-like lesions affecting the spinal cord, indicating demyelination and axonal damage in major white matter tracts[32]. Interestingly, this patient also developed hypochromic microcytic anemia detected on blood tests, suggesting that the GLRX5 mutations affected both heme synthesis (leading to the anemia) and lipoate synthesis (leading to the neurological disease)[32]. Tandem mass spectrometry analysis revealed markedly elevated glycine levels (812 μM versus normal range of 20-760 μM), confirming the glycine cleavage system dysfunction[32].

### Genotype-Phenotype Correlation

The specific location and nature of GLRX5 mutations appear to influence the clinical phenotype observed. Mutations at different positions within the GLRX5 sequence produce distinct biochemical consequences. For example, mutations affecting the iron-sulfur cluster coordination site (such as those involving Cys67, which directly ligates the cluster) produce severe defects in cluster assembly and tend to manifest as sideroblastic anemia with prominent iron dysregulation and relatively less severe neurological involvement[3][6][13]. In contrast, mutations affecting residues involved in cluster transfer to recipient proteins (such as those producing the L148S substitution) preferentially impair transfer to specific targets while permitting cluster assembly onto GLRX5 itself, producing more constellation of biochemical defects affecting different downstream pathways[3][6][14].

Additional insight into GLRX5 function comes from mutations at different positions within the Cys67 coordination site. A patient carrying compound heterozygous mutations p.Cys67Tyr and p.Met128Lys presented with congenital sideroblastic anemia combined with mitochondrial dysfunction[13]. Three-dimensional structural analysis confirmed that Cys67 coordinates the [2Fe-2S] cluster directly, and the Cys67Tyr substitution would eliminate this critical coordination function[13]. Met128 resides distant from the cluster-binding site but is involved in putative partner protein interactions, suggesting that this residue facilitates recognition and binding of recipient proteins[13]. Analysis of the patient's lymphoblastoid and CD34⁺ cells revealed increased ferrochelatase protein levels but drastically decreased ferrochelatase activity, indicating that GLRX5 mutations can produce complex, multimodal effects on enzyme function beyond simple loss of Fe-S cluster delivery[13].

A particularly revealing case involved a patient harboring a p.K51del mutation in GLRX5, identified through genetic analysis in a variant nonketotic hyperglycinemia case[45]. This deletion variant produced a distinct neurological phenotype with myelopathy, variable leukoencephalopathy, seizures, optic atrophy, and peripheral neuropathy—a constellation of findings reminiscent of other multiple mitochondrial dysfunction syndromes caused by late-acting ISC protein defects[45]. However, despite the early-acting position of GLRX5 in the ISC pathway, the K51del variant produced primarily neurological manifestations with minimal secondary effects on iron metabolism, suggesting that the location and structural context of mutations influences their specific biochemical consequences and resulting clinical phenotypes[45].

## Recent Structural and Mechanistic Insights

### Conformational Plasticity in Cluster Transfer

Recent solution nuclear magnetic resonance (NMR) spectroscopy and structural studies have revealed that GLRX5 undergoes dynamic conformational transitions during the cluster transfer process. Although the crystal structure of GLRX5 displays a tetrameric arrangement with buried clusters, solution studies indicate that the holo form (cluster-bound form) exists predominantly as a symmetric dimer bridged by a single [2Fe-2S]²⁺ cluster under physiological solution conditions[26]. This dimer is coordinated by Cys67 and a GSH molecule per subunit, with cluster-binding sites that are not directly accessible to potential recipient proteins when in the fully symmetric dimeric state[26].

The structural plasticity of holo-GLRX5 serves as the crucial factor permitting efficient cluster transfer to partner proteins through a specific and cluster-mediated protein-protein recognition mechanism[26]. The protein undergoes transitions between different conformational states in solution, with two sets of signals being detected for Cys67 and Ser70 by two-dimensional heteronuclear single quantum coherence (HSQC-AP) NMR experiments, indicating coexistence of multiple conformational isomers in dynamic equilibrium[26]. This conformational heterogeneity appears to create transient exposure of the cluster-binding interface, allowing specific recognition and approach of recipient proteins such as ISCA1 and ISCA2[26]. Once recognition occurs through the cluster-mediated intermediate, the cluster is transferred from GLRX5 to the recipient protein through an associative mechanism involving direct protein-protein interactions rather than release of the cluster into the free glutathione pool[26].

This mechanism represents a sophisticated regulatory strategy whereby cluster transfer occurs through controlled exposure of the reactive cluster interface only upon recognition of appropriate recipient proteins, rather than through promiscuous cluster release that could lead to cellular damage through free cluster species. The interaction between GLRX5 and its two physiological [2Fe-2S] receptor proteins (ISCA1 and ISCA2) shares common structural recognition determinants, as both proteins interact at similar interfaces on GLRX5, suggesting that the mechanism of cluster transfer can be generalized to diverse target proteins[26]. The data are consistent with the cluster transfer occurring via an associative process involving specific protein-protein interactions rather than cluster dissociation in solution[26].

### Role of Glutathione Coordination

Glutathione coordination plays multiple critical roles in GLRX5 function beyond simple redox chemistry. The crystal structure reveals that the [2Fe-2S] cluster is ligated not only by cysteine residues from GLRX5 monomers but also by cysteine thiols from two glutathione molecules, creating a mixed coordination sphere[7][28][51]. This glutathione involvement in direct cluster coordination represents a notable distinction from many other iron-sulfur proteins, where GSH serves primarily as a reductant rather than as a direct ligand. The presence of glutathione bound directly to the cluster serves multiple functions: first, it contributes to cluster stabilization and coordination geometry; second, it creates an extended binding surface that facilitates protein-protein interactions with recipient proteins; and third, the glutathione ligands can undergo reversible modifications that regulate cluster accessibility[7][28][55].

Mass spectrometry analysis of GLRX5 revealed that under oxidative conditions or in the absence of bound clusters, the free cysteine residues of apo-GLRX5 undergo glutathionylation—the formation of mixed disulfides between GLRX5 cysteine residues and glutathione molecules[7][28][55]. This glutathionylation reaction protects the catalytic cysteine thiol groups from further oxidation and oxidative inactivation[7][28][55]. Additionally, glutathionylation may facilitate the process of cluster transfer or acceptance, as the reversible S-glutathionylation modification could serve to modulate the reactivity and accessibility of the cysteine coordination sites[7][28][55]. The reversible nature of glutathionylation (glutaredoxins like GLRX1 catalyze its removal) provides a mechanism for cellular regulation of GLRX5 reactivity in response to oxidative stress or changes in the redox environment.

## Cellular Iron Homeostasis and Redox Regulation

### Impact on Iron Regulatory Proteins

GLRX5 exerts profound effects on cellular iron homeostasis through its role in maintaining the iron-sulfur cluster status of iron regulatory protein 1 (IRP1), the master regulator of cellular iron metabolism. When [Fe-S] cluster biosynthesis is intact, GLRX5-mediated delivery of [4Fe-4S] clusters to apo-IRP1 generates holo-IRP1 (the cluster-containing form), which functions as cytosolic aconitase and does not bind to iron-responsive elements[10][33]. This functional state permits normal translation of transferrin receptor 1 mRNA and normal synthesis of ferritin proteins, maintaining balanced iron uptake and storage[10][33].

In contrast, GLRX5 deficiency impairs [Fe-S] cluster biosynthesis, preventing adequate cluster delivery to IRP1[10][33]. Apo-IRP1 (lacking its cluster) binds to iron-responsive elements (IREs) in the 5' untranslated regions of ALAS2 and other mRNAs, repressing their translation[10][33][36]. Additionally, GLRX5-deficient cells exhibit increased levels of IRP2, the second iron regulatory protein, which similarly binds IREs and represses translation of target mRNAs[10][33]. The coordinate activation of both IRP1 and IRP2 IRE-binding activities reflects the cell's response to apparent iron depletion consequent to impaired Fe-S cluster biogenesis[10][33].

The practical consequences of IRP activation in GLRX5-deficient cells include dramatic reductions in ALAS2 protein levels due to translational repression of ALAS2 mRNA[10][33][36]. Furthermore, increases in ferroportin expression (the cellular iron exporter) occur in response to IRP-mediated mRNA destabilization and translational repression[10][33]. The net effect is that GLRX5-deficient erythroid cells exhibit marked reduction in heme biosynthesis capacity (due to ALAS2 repression and ferrochelatase dysfunction) combined with active iron export and reduced iron uptake, creating a state of relative cytosolic iron depletion despite absolute mitochondrial iron overload[10][33][36].

### Mitochondrial Iron Accumulation and Dysfunction

GLRX5 deficiency results in mitochondrial iron accumulation, a hallmark pathological feature of sideroblastic anemia[10][33][53]. The mechanisms underlying this mitochondrial iron overload are multifaceted. First, impaired Fe-S cluster biogenesis reduces the synthesis of iron-sulfur-containing proteins involved in iron storage and metabolism within mitochondria[10][33]. Second, the repression of ALAS2 and other iron metabolism genes through IRE-binding by activated IRP proteins paradoxically reduces the export of iron from mitochondria to the cytosol, leading to iron sequestration in the mitochondrial compartment[10][33]. Third, the reduced synthesis of heme biosynthetic enzymes means that less iron is being incorporated into heme, further promoting mitochondrial iron accumulation[10][33].

Measurements of iron distribution in GLRX5-deficient cells revealed that mitochondrial iron content increased 2.3-fold over control levels, whereas cytosolic iron levels remained unchanged, demonstrating the selective mitochondrial sequestration of excess iron[10][33][53]. Rescue experiments using patient-derived fibroblasts demonstrated that transfection with wild-type GLRX5 reversed this mitochondrial iron overload[10][33]. The accumulation of iron within mitochondria creates a microenvironment susceptible to free radical formation through Fenton chemistry, wherein ferrous iron (Fe²⁺) reacts with hydrogen peroxide and other reactive oxygen species to generate highly reactive hydroxyl radicals that damage lipids, proteins, and nucleic acids[10][13][33].

Consistent with oxidative stress from accumulated iron, GLRX5-deficient cells exhibit markers of oxidative damage. In patient-derived cells, reduced glutathione content decreased while markers of oxidative stress including decreased aconitase activity and increased MnSOD (manganese superoxide dismutase) protein expression were observed[13]. The oxidative damage extends to mitochondrial DNA (mtDNA), with decreased mtDNA copy number and impaired mtDNA integrity detected in GLRX5-deficient cells[13]. This mitochondrial DNA damage contributes to reduced complex I and IV activities and consequent depletion of ATP content, further compromising cellular energy metabolism[13].

## Future Research Directions and Therapeutic Implications

Despite substantial progress in understanding GLRX5 biochemistry and cellular functions, significant questions remain regarding the precise regulation of cluster transfer directionality, the complete roster of GLRX5-dependent recipient proteins, and organism-specific variations in GLRX5 function between prokaryotes, fungi, plants, and mammals. The demonstration that the mitochondrial chaperone HSPA9/HSC20 system exhibits inhibitory rather than stimulatory effects on ISCU-to-GLRX5 cluster transfer—contrary to the stimulatory role of Ssq1/Jac1 in yeast—suggests that mammalian cells employ distinct regulatory mechanisms for controlling cluster distribution. Future research should elucidate the molecular basis for these organism-specific differences and their implications for cellular adaptation to changing metabolic demands and stress conditions.

The identification of additional genetic variants in GLRX5 through expanded genomic screening of patients with unexplained sideroblastic anemia, neurological disease, or other multisystem mitochondrial disorders will continue to refine understanding of structure-function relationships within the protein. Structure-guided design of mutations combined with rigorous biochemical characterization of the resulting protein variants will establish how specific amino acid residues contribute to cluster coordination, recipient protein recognition, and conformational transitions critical for function. Determination of cryo-electron microscopy structures of GLRX5 in complex with its various interaction partners will reveal the molecular details of protein recognition interfaces and cluster transfer mechanisms.

Therapeutic development targeting GLRX5 should address the fundamental question of whether residual GLRX5 activity can be enhanced pharmacologically to improve outcomes in patients with GLRX5 mutations. Chemical genetic approaches might identify compounds that stabilize GLRX5 protein or enhance its expression levels. Additionally, understanding how cells adapt to chronic GLRX5 deficiency through upregulation of parallel pathways or changes in metabolic capacity may reveal therapeutic targets for partially compensating for impaired Fe-S cluster biogenesis. Lipoate supplementation trials in patients with variant nonketotic hyperglycinemia due to GLRX5 mutations have shown limited efficacy to date, suggesting that direct supplementation bypassing the Fe-S-dependent assembly step may be insufficient to restore full enzymatic function. Future therapeutic strategies might involve gene therapy approaches to restore GLRX5 expression or, alternatively, enhancement of residual GLRX5 function through adjunctive approaches targeting the redox environment or metabolic demand.

## Conclusion

GLRX5 represents a paradigmatic example of how specialized subcellular localization of a single polypeptide, despite its modest size of 156 amino acids and straightforward CGFS active-site motif, enables profound control over fundamental cellular processes including energy metabolism, biosynthesis, and iron homeostasis. As a monothiol glutaredoxin functioning as a metallochaperone in mitochondrial iron-sulfur cluster biogenesis, GLRX5 occupies a critical hub position in the iron-sulfur cluster assembly pathway, serving as the intermediate carrier that receives newly synthesized [2Fe-2S] clusters from the scaffold protein ISCU and facilitates their transfer to an diverse set of recipient proteins spanning cytosolic iron-regulatory proteins, mitochondrial metabolic enzymes, respiratory chain complexes, and biosynthetic machinery. The structural plasticity of GLRX5, revealed through crystallographic studies in its tetrameric cluster-bound state and through solution NMR spectroscopy demonstrating dynamic dimeric conformations in solution, provides a molecular mechanism for specific recognition and directional cluster transfer to appropriate target proteins while preventing inappropriate cluster release that could trigger cellular damage through free radical formation.

The tissue-specific amplification of GLRX5 expression in erythroid cells reflects the specialized demands of erythropoiesis, wherein the extraordinary biosynthetic capacity required for hemoglobin production places exceptional demands on the Fe-S cluster assembly machinery. This tissue specificity, combined with GLRX5's role in both heme synthesis (through ferrochelatase and ALAS2 regulation) and iron homeostasis (through IRP1 control), explains why GLRX5 mutations preferentially manifest as sideroblastic anemia in which pathological iron accumulates in the mitochondria of erythroid precursor cells. The variant nonketotic hyperglycinemia phenotype caused by different GLRX5 mutations illustrates how impairment of upstream Fe-S cluster synthesis by GLRX5 deficiency cascades through the lipoate synthesis pathway to compromise the glycine cleavage system and energy metabolism enzymes, producing neurological disease.

Recent structural and kinetic studies have fundamentally advanced our understanding of how GLRX5 mediates cluster transfer through conformational transitions and specific protein-protein recognition, establishing a sophisticated metallochaperone mechanism that extends well beyond the simpler redox chemistry catalyzed by other glutaredoxins. These discoveries position GLRX5 as a central node in cellular Fe-S cluster homeostasis, warranting continued investigation of its regulation, interaction networks, and potential targeting for therapeutic intervention in diseases of Fe-S cluster biogenesis. The conservation of GLRX5 function across eukaryotic cells and organisms, combined with its critical role in both housekeeping metabolic pathways and specialized biosynthetic processes, ensures that GLRX5 will remain a paradigm for understanding how specialized redox-active proteins integrate into complex cellular signaling networks to maintain metabolic homeostasis.

## Citations

1. https://www.ncbi.nlm.nih.gov/gene/51218
2. https://predictomes.org/hp?pid=2440
3. https://onlinelibrary.wiley.com/doi/10.1002/jcb.25267
4. https://www.uniprot.org/uniprotkb/Q86SX6/entry
5. https://www.ebi.ac.uk/interpro/protein/UniProt/Q86SX6/sequence/
6. https://pubmed.ncbi.nlm.nih.gov/26100117/
7. https://portlandpress.com/biochemj/article/433/2/303/45147/The-crystal-structure-of-human-GLRX5-iron-sulfur
8. https://www.molbiolcell.org/doi/10.1091/mbc.01-10-0517
9. https://pmc.ncbi.nlm.nih.gov/articles/PMC10897161/
10. https://pmc.ncbi.nlm.nih.gov/articles/PMC2860907/
11. https://pmc.ncbi.nlm.nih.gov/articles/PMC6928294/
12. https://pmc.ncbi.nlm.nih.gov/articles/PMC7047114/
13. https://pubmed.ncbi.nlm.nih.gov/30660387/
14. https://www.genecards.org/cgi-bin/carddisp.pl?gene=GLRX5
15. https://pmc.ncbi.nlm.nih.gov/articles/PMC9958551/
16. https://pmc.ncbi.nlm.nih.gov/articles/PMC8349188/
17. https://pubmed.ncbi.nlm.nih.gov/24777537/
18. https://zfin.org/ZDB-GENE-040426-1957
19. https://pmc.ncbi.nlm.nih.gov/articles/PMC7237328/
20. https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2020.00510/full
21. https://pmc.ncbi.nlm.nih.gov/articles/PMC9927405/
22. https://www.pnas.org/doi/10.1073/pnas.1400102111
23. https://pmc.ncbi.nlm.nih.gov/articles/PMC7351949/
24. https://pubmed.ncbi.nlm.nih.gov/21029046/
25. https://journals.sagepub.com/doi/full/10.1089/ars.2012.5007
26. https://pmc.ncbi.nlm.nih.gov/articles/PMC5964037/
27. https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2021.605778/full
28. https://www.jci.org/articles/view/40372
29. https://febs.onlinelibrary.wiley.com/doi/10.1111/febs.14353
30. https://pubmed.ncbi.nlm.nih.gov/24334290/
31. https://pubmed.ncbi.nlm.nih.gov/20364084/
32. https://pmc.ncbi.nlm.nih.gov/articles/PMC7456137/
33. https://elifesciences.org/articles/15991v1.pdf
34. https://pmc.ncbi.nlm.nih.gov/articles/PMC6006200/
35. https://pubs.acs.org/doi/abs/10.1021/jacs.6b09567
36. https://pmc.ncbi.nlm.nih.gov/articles/PMC3188835/
37. https://iubmb.onlinelibrary.wiley.com/doi/am-pdf/10.1002/iub.2597
38. https://www.pnas.org/doi/10.1073/pnas.2003982117
39. https://pmc.ncbi.nlm.nih.gov/articles/PMC8565018/
40. https://pubmed.ncbi.nlm.nih.gov/32817474/
41. https://pmc.ncbi.nlm.nih.gov/articles/PMC8614886/
42. https://pmc.ncbi.nlm.nih.gov/articles/PMC4585086/
43. https://services.healthtech.dtu.dk/services/TargetP-2.0/
44. https://pmc.ncbi.nlm.nih.gov/articles/PMC6709626/
45. https://pmc.ncbi.nlm.nih.gov/articles/PMC4098818/
46. https://pmc.ncbi.nlm.nih.gov/articles/PMC9529593/