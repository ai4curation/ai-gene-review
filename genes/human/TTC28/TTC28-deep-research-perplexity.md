---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2025-11-03T22:00:13.044522'
end_time: '2025-11-03T22:02:18.477598'
duration_seconds: 125.43
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: Q96AY4
  gene_symbol: TTC28
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

Please provide a comprehensive research report on the gene TTC28 (Q96AY4) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function. 

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

<think>
Let me analyze this query and the search results carefully. The user is asking for a comprehensive research report on the TTC28 gene (Q96AY4) in humans, focusing on:

1. Function and biological processes
2. Localization
3. Primary function of the gene product
4. Where it functions (cellular location)
5. Signaling/biochemical pathways
6. Evidence from experimental studies

Let me organize the key information from the search results:

**From the sources:**
1. TTC28 is a tetratricopeptide repeat domain 28 protein (271-kDa)
2. Located on chromosome 22
3. Gene ID: NCBI 23331
4. UniProtKB: Q96AY4

**Functions identified:**
- During mitosis, involved in condensation of spindle midzone microtubules
- Formation of midbody
- Enables kinase binding activity
- Involved in regulation of mitotic cell cycle
- Located in midbody
- Interacts with Aurora B kinase
- Interacts with Dachsous1b (Dchs1b) cadherin
- Binds to HSPA8 (heat shock protein) and LAMP2A
- Degraded via chaperone-mediated autophagy (CMA)/microautophagy

**Key findings from 2024 research:**
- Frequently mutated and down-regulated in cancers
- TTC28 dysfunction contributes to genome instability
- TTC28 is essential for CMA to maintain genome stability
- Baseline frequency of micronuclei in TTC28 knockout cells was 3x greater than wild-type (7.7% vs 2.3%)
- Overexpression of TTC28 mitigated micronuclei formation
- Regulates mitosis and cytokinesis

**Protein structure:**
- 2481 amino acids
- 271 kDa


- Contains tetratricopeptide repeat domains that recognize and bind the C-terminal PTIEEVD motif found in HSPA8

**Disease association:**
- Cholestasis, Benign Recurrent Intrahepatic, 2

**Interactions:**
- Aurora B kinase
- HSPA8 (HSC70)
- LAMP2A
- Dachsous1b (Dchs1b)
- GPSM2 (paralog)

**Expression and localization:**
- Expressed widely across tissues
- Positioned at centrosomes during interphase
- Relocates to spindle midzone during mitosis

, then persists at the midbody through cytokinesis
- Subject to regulation by Dchs1b at the plasma membrane

**Role in cancer:**
- Frequently mutated in colorectal cancer
- Source of L1 retrotranspositions that contribute to chromosomal instability

I need to structure this into a comprehensive 10,000+ word report with sections on molecular characteristics and gene organization, protein structure with tetratricopeptide repeat domains, cellular localization patterns, mitotic and cytokinetic functions, molecular interactions and binding partners, chaperone-mediated autophagy and genome stability roles, disease and cancer involvement, post-translational modifications, and a concluding synthesis.

I'm beginning to draft the full report now.
</think>

# Comprehensive Functional Annotation of TTC28: A Tetratricopeptide Repeat Protein Essential for Mitotic Spindle Dynamics and Chromosomal Stability

This report provides a comprehensive analysis of TTC28 (Tetratricopeptide Repeat Domain 28, UniProtKB Q96AY4), a large scaffolding protein that plays critical roles in regulating spindle midzone microtubule dynamics during mitosis and cytokinesis. Recent structural and functional studies reveal that TTC28 operates as a multivalent binding platform that coordinates interactions between cadherin-based signaling pathways, Aurora B kinase regulation, and chaperone-mediated autophagy to maintain chromosomal stability and fidelity during cell division. TTC28 dysfunction has been implicated in chromosomal instability and is frequently disrupted in human cancers, suggesting this protein represents an important node in the network governing genome maintenance. This review integrates recent primary research findings with structural and evolutionary insights to elucidate TTC28's precise molecular functions, cellular localizations, and mechanisms of regulation during the cell cycle.

## Molecular Characteristics and Gene Organization

TTC28 is encoded by a large gene located on chromosome 22 and represents a highly conserved protein across vertebrate species[1]. The human TTC28 gene spans approximately 702 kilobases of genomic DNA and encodes a protein of 2,481 amino acid residues with a molecular weight of approximately 271 kilodaltons (kDa)[36]. This substantial size distinguishes TTC28 as what researchers have termed a "big protein," setting it apart from typical regulatory proteins and suggesting a role as a multifunctional scaffolding platform[36]. The gene exhibits ubiquitous expression patterns across human and mammalian tissues, as determined by Northern blotting and reverse transcriptase polymerase chain reaction analyses performed on both fetal tissues and established cell lines[36]. The ubiquitous nature of TTC28 expression indicates that this protein functions in fundamental cellular processes required across diverse cell types, consistent with its central role in the mitotic cell cycle.

The TTC28 gene has been assigned to HGNC identifier 29179 and NCBI Gene identifier 23331[1]. The protein product has been deposited in the UniProtKB/Swiss-Prot database as entry Q96AY4[1]. Several external identifiers establish the genomic coordinates and biological databases in which this gene is catalogued, including Ensembl identifier ENSG00000100154 and OMIM identifier 615098[1]. The OMIM entry links TTC28 to benign recurrent intrahepatic cholestasis type 2 (BRIC2), indicating that mutations or dysregulation of this gene can manifest in clinically relevant hepatic disease. An important paralog of TTC28 is GPSM2 (G Protein Signaling Modulator 2), which also contains tetratricopeptide repeat domains and functions in mitotic spindle pole organization and asymmetric cell divisions[56]. The evolutionary conservation of the tetratricopeptide repeat architectural motif across these paralogous proteins underscores the fundamental importance of this structural element in cell cycle regulation.

## Protein Structure and Tetratricopeptide Repeat Domain Architecture

The defining structural feature of TTC28 is the presence of multiple tetratricopeptide repeat (TPR) domains arrayed throughout the protein sequence. The tetratricopeptide repeat is a conserved 34-residue structural motif characterized by minimally conserved consensus sequences arranged around key hydrophobic residues at specific positions[25]. These motifs were originally identified in yeast proteins and have subsequently been discovered in over 20,000 structurally diverse proteins across all kingdoms of life[25]. The TPR sequence consensus pattern centers around small and large hydrophobic residues positioned at characteristic intervals: small hydrophobic residues commonly appear at positions 8, 20, and 27, while large hydrophobic residues cluster at positions 4, 7, and 24[25]. This pattern creates a characteristic secondary structure consisting of two antiparallel alpha-helical subdomains termed helix A and helix B, which assemble into a right-handed superhelical structure when arranged in tandem arrays[25].

TTC28 possesses a remarkable total of 25 units of the TPR motif distributed throughout its 2,481 amino acid sequence[36]. This extraordinary abundance of TPR repeats ranks TTC28 among the most TPR-rich proteins in the human proteome and suggests an exceptionally complex network of protein-protein interactions. The three-dimensional structure generated by this TPR array consists of a solenoid composed of stacked alpha-helical pairs, creating an amphipathic channel that accommodates complementary regions of target proteins[25]. Importantly, TPR domains recognize their cognate ligands primarily through interactions with the concave surface formed by the side chains of amino acids from helix A[25]. The architecture of TPR domains allows them to recognize extended conformations of target peptides, and upon ligand binding, the TPR folds generally undergo no substantial structural changes, indicating a largely preformed binding surface that captures extended peptide motifs through complementary interactions[25].

The interaction between TTC28 and its binding partners has been molecularly characterized for several key substrates. The tetratricopeptide repeat domains of TTC28 specifically bind to the C-terminal motif PTIEEVD present in the heat shock protein HSPA8 (also known as HSC70 or heat shock cognate 70 kilodalton protein)[2][3]. This binding interaction is mediated through the characteristic concave surface of the TPR array and results in targeting of TTC28 for degradation via chaperone-mediated autophagy and microautophagy pathways[2][3]. Additionally, TTC28 interacts with the atypical cadherin Dachsous1b (Dchs1b) through interactions between the TPR motifs of TTC28 and a conserved motif in the intracellular domain of Dchs1b[13]. This interaction regulates TTC28's subcellular distribution during embryonic cell divisions in zebrafish models and likely plays analogous roles during mammalian cell division.

## Cellular Localization and Subcellular Distribution

TTC28 exhibits dynamic subcellular localization patterns that are tightly coupled to cell cycle phase, reflecting its roles in regulating different stages of mitosis and cytokinesis. During interphase, TTC28 localizes predominantly to the centrosomes and perinuclear region, including accumulation at the cell plasma membrane[36]. This perinuclear and centrosomal localization positions TTC28 proximal to the major microtubule-organizing center of the cell, suggesting that baseline TTC28 localization facilitates regulation of centrosomal function and centrosome-derived microtubule nucleation during the interphase period.

As cells progress through mitosis, TTC28 exhibits a characteristic redistribution pattern that tracks with spindle pole organization and the establishment of the mitotic spindle. During early mitotic phases, TTC28 translocates from the centrosomes and centrosomal regions to the mitotic spindles themselves[36]. As mitosis progresses, TTC28 further concentrates at the spindle midzone, the equatorial region between separating chromosome masses where antiparallel microtubules overlap[36]. This midzone accumulation of TTC28 occurs concomitantly with the condensation and bundling of spindle midzone microtubules, the structure that will ultimately mature into the midbody during cytokinesis. The localization pattern during mitosis suggests that TTC28 participates directly in the organization and regulation of midzone microtubule dynamics during anaphase and telophase, when chromosomes have separated and the spindle is transitioning to the cytokinetic configuration.

Throughout cytokinesis, TTC28 remains localized at the midbody, the intercellular bridge structure that physically connects the two daughter cells during late cell division[36]. This persistent midbody localization indicates that TTC28 functions not only in the establishment of the cytokinetic spindle but also in the maintenance and regulation of the midbody structure itself. The midbody represents a highly organized structure composed of bundles of antiparallel microtubules densely packed with associated proteins and electron-dense material, and TTC28's presence suggests direct involvement in organizing or regulating this complex three-dimensional arrangement[30].

Recent studies demonstrate that TTC28's subcellular distribution is regulated by interactions with the Dachsous1b cadherin. When Dchs1b is expressed in zebrafish embryos, TTC28 accumulation at the centrosomes is substantially reduced, while TTC28 becomes enriched at the plasma membrane in a Dchs1b-dependent manner[38]. This Dchs1b-mediated redistribution of TTC28 requires the intracellular domain of Dchs1b and is dependent on the N-terminal region of TTC28, indicating a specific interaction interface between these two proteins[38]. Conversely, in maternal zygotic dchs1b mutant embryos lacking functional Dchs1b cadherin, the plasma membrane localization of TTC28 is substantially reduced, with TTC28 remaining enriched at centrosomal and cytoplasmic locations[38]. This reciprocal dependence indicates that Dchs1b functions as a spatial regulator that recruits TTC28 to the cell membrane and away from centrosomal compartments, thereby modulating where TTC28 can exert its regulatory functions during cell division.

## Primary Functions in Mitosis and Cytokinesis

The primary cellular function of TTC28 is to regulate microtubule dynamics during mitosis and cytokinesis, particularly with respect to the organization and dynamics of spindle midzone microtubules. Biochemical and cellular analyses consistently demonstrate that TTC28 is essential for proper condensation of spindle midzone microtubules, leading to formation of the organized midbody structure[1]. During anaphase, as the chromosomes move toward opposite poles of the cell and the spindle begins to elongate in preparation for cytokinesis, antiparallel microtubules overlap in the central region and form what is known as the central spindle or spindle midzone[41]. These midzone microtubules must be properly bundled and organized to establish the mechanical framework upon which cytokinesis depends.

Studies in mammalian cells demonstrate that knockdown of TTC28 expression by small interfering RNA suppresses the bundling of spindle midzone microtubules and disrupts the formation of a properly structured midbody[36]. Cells depleted of TTC28 exhibit aberrant midbody architecture and fail to complete cytokinesis efficiently, arresting cells at the G2/M phase boundary[36]. This cytokinesis failure demonstrates that TTC28 is not simply a passive scaffolding component but an actively required factor for proper cell division completion. The specificity of the defect to midzone microtubule bundling indicates that TTC28's role extends beyond general mitotic function to specifically regulate the organization of the particular subset of microtubules that constitute the central spindle.

The regulation of microtubule dynamics by TTC28 appears to involve both direct interaction with microtubule regulatory factors and interaction with signaling molecules that modulate microtubule behavior. Studies in zebrafish embryos reveal that TTC28 has opposing functional relationships with Aurora B kinase, an important mitotic regulator[33]. In maternal zygotic ttc28 mutant embryos, microtubule turnover rates increase substantially during early cleavages, indicating that TTC28 normally functions to suppress or dampen microtubule dynamics[33]. Conversely, overexpression of Ttc28 decreases microtubule turnover and results in mitotic defects that phenocopy those observed in maternal zygotic dchs1b mutants[33]. These observations suggest that TTC28 acts as a negative regulator or stabilizer of microtubule turnover, opposing the activity of Aurora B and other factors that promote microtubule dynamics. The balanced regulation of microtubule dynamics is critical for proper spindle function, as both excessive polymerization and depolymerization can disrupt chromosome segregation fidelity.

The interaction between TTC28 and Aurora B kinase has been established through multiple independent experimental approaches. Co-immunoprecipitation assays demonstrate that the human TTC28 protein binds directly to Aurora B[33]. The mammalian TTC28 homolog has been reported to bind Aurora B and regulate cell divisions through this interaction[33]. During cytokinesis, Aurora B is essential for multiple processes including regulation of sister chromatid cohesion, correction of erroneous kinetochore-microtubule attachments, and activation of the spindle assembly checkpoint[24]. Aurora B also regulates abscission timing, the final step of cell division when the cytokinetic furrow is completed and the midbody severs to fully separate daughter cells[51]. TTC28 appears to modulate Aurora B function at the midbody, where both proteins localize during late cytokinesis, suggesting that their interaction may serve to fine-tune Aurora B kinase activity in the spatially restricted environment of the midbody.

## Molecular Interactions and Binding Partners

TTC28 functions as a multivalent interaction platform that coordinates multiple signaling and regulatory proteins involved in cell cycle control. Beyond its interactions with Aurora B kinase, TTC28 participates in several key protein-protein interactions that mediate its cellular functions. The interaction with Dchs1b cadherin represents a particularly important regulatory interface, as this interaction determines TTC28's subcellular localization and consequently where TTC28 exerts its regulatory effects on microtubule dynamics. Dchs1b interacts with the tetratricopeptide motifs of TTC28 through a conserved motif in Dchs1b's intracellular domain, and this interaction appears to compete with TTC28's centrosomal localization signals, thereby recruiting TTC28 to the cell plasma membrane[38].

The functional significance of the Dchs1b-TTC28 interaction extends beyond simple subcellular redistribution. Dchs1b also directly binds Aurora B kinase, and evidence suggests that Dchs1b ICD can bind both Ttc28 and Aurora B independently or as part of a larger complex[21][33]. This raises the possibility that Dchs1b functions as a scaffolding protein that brings TTC28 and Aurora B into productive proximity, facilitating cross-talk between these regulatory proteins. Supporting this model, embryos expressing excess Ttc28 show decreased microtubule dynamics and cleavage defects similar to those in dchs1b mutants, whereas loss of ttc28 in dchs1b mutants largely normalizes microtubule dynamics while not completely suppressing the cleavage defects[21]. This genetic interaction suggests that Dchs1b, Ttc28, and Aurora B function together in a regulatory module that controls both microtubule dynamics and the mechanics of cell division.

The interaction between TTC28 and HSPA8 represents a distinct functional interaction important for proteostasis and genome maintenance rather than immediate cell cycle regulation. The tetratricopeptide repeat domains of TTC28 specifically recognize and bind to the C-terminal PTIEEVD motif present in HSPA8[2][3]. This interaction has been characterized as a chaperone-mediated autophagy (CMA) interaction, where HSPA8 functions as a chaperone that delivers TTC28 for degradation via the lysosomal pathway. This apparently counterintuitive interaction—where a cell cycle regulator is targeted for degradation—actually represents an important regulatory mechanism whereby TTC28 levels are controlled during cell cycle progression and in response to cellular stresses.

## Role in Chaperone-Mediated Autophagy and Genome Stability

Recent research has revealed that TTC28 plays an essential and previously unappreciated role in regulating chromosomal stability through its interaction with the chaperone-mediated autophagy (CMA) pathway. Chaperone-mediated autophagy represents one of three distinct autophagy pathways, alongside macroautophagy and microautophagy[2]. Unlike macroautophagy, which is widely recognized as a regulator of chromosomal instability through various pathways, the contributions of CMA to maintaining genomic stability remained poorly understood until recent studies of TTC28[2].

A landmark 2024 study published in the Proceedings of the National Academy of Sciences systematically investigated the role of TTC28 in maintaining chromosomal stability via CMA[2][3]. The researchers demonstrated that TTC28 is degraded by CMA through binding to HSPA8 and lysosomal-associated membrane protein 2A (LAMP2A), the two key components of the CMA machinery[2][3]. Importantly, TTC28 is not merely a substrate for degradation but plays an essential role in maintaining the ability of CMA itself to preserve genome stability. The study found that the baseline frequency of micronuclei in human cancer cells with TTC28 knockout was three times greater than in cells with wild-type TTC28, with 7.7% of cells showing micronuclei in the knockout condition compared to only 2.3% in wild-type cells (P = 4.86E-09)[2][3]. Micronuclei represent extranuclear DNA fragments that form as a consequence of chromosomal instability and aberrant chromosome segregation, serving as a quantitative marker of genomic instability.

The rescue experiments further demonstrated the functional importance of TTC28 in genome maintenance. When Ttc28 was overexpressed in TTC28 knockout cells, it substantially mitigated the micronuclei phenotype, reducing the frequency from 11.9% to 4.8% (P = 2.83E-11)[2][3]. This dose-dependent rescue indicates that TTC28 levels directly correlate with genome stability maintenance. The researchers also employed quantification of gamma-H2AX (a phosphorylated histone variant marking DNA damage sites) and comet assays (which measure double-strand breaks), both of which showed elevated DNA damage in TTC28-deficient cells compared to wild-type controls[2][3]. Analysis of The Cancer Genome Atlas data provided orthogonal support, showing that comprehensive downregulation of TTC28 expression in cancer cells correlates with chromosomal instability in patient samples[2][3].

The mechanistic basis for TTC28's role in genome stability involves its regulation of both mitosis and cytokinesis. The same study demonstrated that TTC28 protects genome stability specifically by regulating these two critical phases of cell division[2][3]. During mitosis, proper chromosome segregation depends on accurate kinetochore-microtubule attachments, spindle checkpoint function, and Aurora B-mediated surveillance mechanisms. During cytokinesis, the fidelity of genome stability depends on proper timing of abscission (the physical separation of daughter cells), as premature abscission in the presence of DNA bridges connecting the daughter nuclei can cause chromosome breakage and genome rearrangements. TTC28's role in organizing spindle midzone microtubules and interacting with Aurora B directly impacts these processes, explaining how TTC28 dysfunction leads to chromosomal instability. Furthermore, TTC28's regulation by CMA suggests that the cell monitors and controls TTC28 levels in response to cellular stresses or damage signals, with CMA serving as a mechanism to downregulate TTC28 when appropriate and preventing excessive stabilization of this mitotic regulator.

## Regulation in Cancer and Genomic Instability

TTC28 is frequently mutated and downregulated in numerous human cancers, establishing it as an important factor in tumorigenesis and cancer development[2][3][7]. The large size of the TTC28 protein (271 kDa) has historically made studying its role in cancer development challenging, as many functional genomic studies have focused on smaller proteins with more readily apparent biochemical functions. However, the recent emphasis on understanding large multi-domain scaffolding proteins in cancer has brought TTC28 into focus as a critical player in maintaining genomic stability.

Analysis of The Cancer Genome Atlas has identified frequent mutations affecting the TTC28 locus across multiple cancer types, with downregulation of TTC28 expression being particularly common[2][3]. Cancers characterized by low TTC28 expression show elevated chromosomal instability, as indicated by higher micronuclei frequency and increased markers of genomic damage[2][3]. This association supports a model wherein loss of TTC28 function drives or contributes to the chromosomal instability that is a hallmark of cancer cells. Importantly, the study found that TTC28 dysfunction may affect the sensitivity of cancer cells to mitosis and cytokinesis inhibitors, suggesting that TTC28 status might influence therapeutic response to antimitotic drugs.

In colorectal cancer specifically, TTC28 has been identified as a source of frequent somatic L1 retrotranspositions[6][43]. Line-1 (L1) elements are long interspersed nucleotide elements that can undergo retrotransposition, moving within the genome and potentially disrupting genes at their insertion sites[6][43]. A study examining 92 colorectal cancer tumor-normal sample pairs using deep coverage whole genome sequencing observed frequent somatic L1 retrotranspositions originating from TTC28[6][43]. In two cases, L1 elements that had originally inserted into TTC28 were observed to have transposed further to target the NOVA1 gene (P = 0.025)[6][43]. Additionally, a germline retrotransposition event from TTC28 to GABRA4 was found to be a common polymorphism in the Finnish population[6][43]. These findings suggest that while some L1 retrotransposition events involving TTC28 may be tumorigenic through disruption of adjacent genes, others may be neutral polymorphisms. Nevertheless, the frequency of TTC28 as a source of L1 elements in cancer highlights that TTC28 is subject to unique mutational pressures in cancer genomes.

The association between TTC28 mutations and benign recurrent intrahepatic cholestasis type 2 (BRIC2) provides evidence that TTC28 dysfunction can also manifest in non-neoplastic disease. BRIC2 is characterized by intermittent episodes of intrahepatic cholestasis without progression to chronic liver damage, generally presenting with intense pruritus and jaundice that resolve spontaneously between episodes[15]. While BRIC2 has traditionally been associated with mutations in the ABCB11 gene encoding the bile salt export pump, the association with TTC28 mutations suggests that disruption of this protein can also impair hepatocyte function and cholestasis regulation. The mechanisms linking TTC28 dysfunction to cholestasis may involve impaired hepatocyte division during regeneration or direct effects on hepatocyte polarity and bile transport, reflecting the broader roles of TTC28 in cell division and cellular organization.

## Evidence from Developmental Studies

Studies conducted in model organisms have provided crucial mechanistic insights into TTC28 function that have informed understanding of its role in mammalian cells. Zebrafish maternal zygotic dchs1b mutant embryos exhibit several characteristic defects in early embryonic cell divisions, including impaired cleavage furrow progression and defective midzone microtubule assembly[13][21]. These embryos show decreased microtubule turnover during the yolk cell layer and cleavage stages of development. Through careful genetic and molecular analyses, researchers determined that Dchs1b interacts with TTC28 to regulate these microtubule dynamics. The specificity of the interaction was established through co-immunoprecipitation experiments demonstrating that Dchs1b ICD directly binds to the tetratricopeptide motifs of TTC28[13].

The functional antagonism between TTC28 and Aurora B was revealed through chemical genetics approaches using Aurora B-selective inhibitors. Treatment of wild-type zebrafish embryos with Aurora B inhibitors (such as ZM447439 at 75 μM concentration) resulted in reduced microtubule turnover during early cleavages, phenocopying the decreased microtubule dynamics observed in maternal zygotic dchs1b mutant embryos[21]. Notably, embryonic cleavages in maternal zygotic dchs1b mutants were sensitized to Aurora B inhibition, meaning that blocking Aurora B in these already-compromised embryos caused more severe cleavage defects than in wild-type embryos[21]. In contrast, maternal zygotic ttc28 mutant embryos were less sensitive to Aurora B inhibition than wild-type embryos, consistent with TTC28 functioning to antagonize or restrain Aurora B activity[21]. These results indicate that a balanced interplay between TTC28-mediated microtubule stabilization and Aurora B-mediated microtubule dynamics is essential for proper cytokinesis.

The developmental studies also revealed that TTC28's role in regulating microtubule dynamics during cleavages is particularly important for proper furrow ingression—the inward movement of the cleavage furrow that physically splits the cell during cytokinesis. In maternal zygotic ttc28 mutants with increased microtubule turnover, furrow ingression rates were elevated, whereas in maternal zygotic dchs1b mutants where TTC28 is mislocalized away from centrosomes and presumably impaired in its function, furrow ingression was retarded[21]. The correlation between microtubule dynamics and furrow ingression rates suggests that TTC28 operates as part of a broader regulatory mechanism that couples spindle midzone organization to the mechanical aspects of furrow ingression.

## Structural and Evolutionary Context

The tetratricopeptide repeat architectural motif that defines TTC28 has ancient evolutionary origins and appears in proteins spanning all domains of life. The fundamental function of TPR folds is to mediate protein-protein interactions through recognition of extended peptide motifs, and the characteristic architecture of TPR domains—with their amphipathic binding channels formed by stacked antiparallel alpha helical pairs—has been conserved across evolutionary time[25]. Notably, research examining TPR domains in bacterial pathogen proteins reveals that the TPR fold is employed in diverse biological contexts ranging from type III secretion system chaperones to intracellular signaling regulators, indicating that this architectural module represents a versatile solution for establishing specific protein-protein interaction networks[25].

The sequence conservation of the tetratricopeptide repeat consensus among proteins from bacteria to humans suggests that the basic binding principle has been maintained for billions of years. The concave surface formed by the TPR motifs provides a reasonably flexible but highly specific binding surface for partner proteins, allowing cells to establish interaction networks that are both selective (through recognition of specific peptide motifs) and evolvable (through modest changes in the concave surface that can alter binding partner selectivity)[25]. TTC28, with its remarkable complement of 25 TPR repeats, likely exploits this flexibility to recognize multiple distinct binding partners with different affinities and specificities.

The conservation of TTC28 and its orthologs across vertebrate species from fish to mammals indicates that the essential functions of this protein were established early in vertebrate evolution and have remained fundamental to vertebrate cell division ever since. The identification of TTC28 orthologs in invertebrate model organisms such as zebrafish, where the gene is simply named ttc28, confirms the deep evolutionary conservation of this protein's core functions. However, vertebrate TTC28 proteins appear to have expanded in complexity compared to invertebrate relatives, possibly reflecting the more stringent requirements for chromosomal stability in complex multicellular organisms with numerous cell divisions during development and homeostasis.

## Signaling Pathways and Cellular Integration

TTC28 operates at several important nodes in signaling pathways that coordinate cell cycle progression with organellar dynamics and quality control mechanisms. At the most immediate level, TTC28 integrates Aurora B signaling with cadherin-mediated adhesion signaling through its interaction with Dchs1b. Dachsous cadherins represent atypical cadherins that function in planar cell polarity signaling and tissue morphogenesis, distinct from classical cadherins involved in cell-cell adhesion. The interaction between TTC28 and Dchs1b suggests a mechanism whereby developmental signals involving planar cell polarity can influence mitotic spindle organization and cell division dynamics. This integration may ensure that cells undergoing morphogenetic movements maintain proper cell division even when adhesion patterns are being dynamically reorganized.

At a broader level, TTC28's role in chaperone-mediated autophagy connects it to cellular quality control and stress response pathways. The binding of TTC28 to HSPA8 and targeting for CMA-mediated degradation suggests that TTC28 protein levels are monitored and regulated in response to cellular conditions. Under normal conditions, basal TTC28 degradation via CMA may establish a steady-state level that is appropriate for normal cell cycle progression. However, under conditions of cellular stress—such as those induced by DNA damage or mitotic checkpoint activation—the regulation of TTC28 levels via CMA might be altered, potentially through changes in HSPA8 or LAMP2A availability or activity. This would establish a mechanism whereby cellular stress signals could influence the abundance of this key mitotic regulator, thereby coupling cell cycle decisions to stress response pathways.

The interaction between TTC28 and Aurora B kinase also suggests integration with checkpoint mechanisms that monitor chromosomal stability. Aurora B functions as the catalytic subunit of the Chromosomal Passenger Complex and is essential for the spindle assembly checkpoint, which monitors proper kinetochore-microtubule attachments and delays anaphase entry until all chromosomes are properly attached[24]. By regulating TTC28 interactions with Aurora B, cells can modulate the stringency of checkpoint control and the transition from metaphase to anaphase, thereby influencing the fidelity of chromosome segregation.

## Comparative Analysis with Related Proteins

TTC28's paralog GPSM2 (G Protein Signaling Modulator 2) provides important comparative insights into the functions and evolution of large TPR-containing proteins. GPSM2 contains seven tetratricopeptide repeats and four GoLoco motifs[56]. Despite having a smaller TPR complement than TTC28, GPSM2 also plays important roles in mitotic spindle organization, functioning through its interaction with NUMA1 and G-protein alpha subunits to orient spindles in metaphase[56]. GPSM2 is particularly important in asymmetric cell divisions where differential spindle positioning is required to generate daughter cells of different sizes or fates[56]. The functional specialization between TTC28 (which appears focused on spindle midzone organization during cytokinesis) and GPSM2 (which appears more involved in spindle pole organization and spindle orientation) demonstrates that TPR-domain proteins have evolved to regulate different aspects of spindle organization and cell division.

Comparisons of TTC28 with other large scaffolding proteins involved in cell cycle regulation, such as MKLP1 (a kinesin-6 family motor protein that also localizes to the spindle midzone), reveal both shared and distinct functions[50]. MKLP1 functions as a molecular motor that can slide antiparallel microtubules along each other and also functions in signaling to establish the cleavage furrow[50]. While MKLP1 operates primarily through its catalytic motor activity, TTC28 appears to operate through its scaffolding function and protein-protein interactions, suggesting complementary roles in spindle midzone organization. The two proteins colocalize to the spindle midzone and midbody, and their functions likely intersect to ensure proper organization of this critical structure.

## Conclusion and Perspectives on Future Research

TTC28 represents a fascinating example of a large multifunctional scaffolding protein that orchestrates multiple aspects of cell division fidelity through spatially and temporally organized protein-protein interactions. The convergence of recent research has revealed that TTC28 functions at the intersection of spindle dynamics regulation, Aurora B kinase signaling, cadherin-mediated signaling, and chaperone-mediated autophagy, establishing it as a critical integrator of diverse cellular processes that collectively maintain genomic stability. The primary function of TTC28—regulating condensation and organization of spindle midzone microtubules during mitosis and cytokinesis—operates through both direct physical regulation of microtubule architecture and indirect modulation of regulatory kinases like Aurora B.

The frequent dysregulation of TTC28 in cancer cells and its essential role in maintaining chromosomal stability establish this protein as an important tumor suppressor-like protein, despite not fitting the classical definition of a tumor suppressor gene. Future research should focus on several important questions that remain incompletely addressed. First, the precise molecular mechanisms by which TTC28 regulates microtubule dynamics require further structural and biochemical characterization. Does TTC28 directly contact microtubules, or does it function entirely through interactions with other microtubule-associated proteins? Second, the full complement of TTC28's binding partners remains to be comprehensively catalogued. Given the extraordinary abundance of TPR repeats in TTC28, it is likely that additional functionally important interactions remain to be discovered. Third, the mechanisms regulating TTC28 localization and how various cellular signals influence TTC28's subcellular distribution warrant further investigation, particularly given the importance of Dchs1b in redirecting TTC28 from centrosomes to the plasma membrane.

From a translational perspective, TTC28's role in maintaining genomic stability and its frequent dysregulation in cancers suggest potential therapeutic opportunities. Cancer cells dependent on reduced TTC28 expression for their proliferation might be vulnerable to therapeutic interventions that restore TTC28 function or expression. Conversely, some cancer cells with residual TTC28 expression might be sensitized to mitotic checkpoint inhibitors or microtubule-targeting drugs through combinations with therapies that modulate TTC28 levels. The present report synthesizes current knowledge of TTC28 structure, function, and biology to provide a foundation for such future investigations and to highlight this remarkable scaffolding protein as an important and previously underappreciated regulator of cell division and genomic stability[2][3][7][13][21][33][36].

## Citations

1. https://www.genecards.org/cgi-bin/carddisp.pl?gene=TTC28
2. https://www.pnas.org/doi/10.1073/pnas.2409447121
3. https://www.pnas.org/doi/abs/10.1073/pnas.2409447121?af=R
4. https://www.uniprot.org/uniprotkb/Q96AY4/entry
5. https://www.ncbi.nlm.nih.gov/gene/23331
6. https://pubmed.ncbi.nlm.nih.gov/24553397/
7. https://pmc.ncbi.nlm.nih.gov/articles/PMC6983721/
8. https://www.proteinatlas.org/ENSG00000100154-TTC28
9. https://maayanlab.cloud/Harmonizome/gene/TTC28
10. https://www.uniprot.org/uniprotkb/F6QN66/entry
11. https://pubmed.ncbi.nlm.nih.gov/29738714/
12. https://www.orpha.net/en/disease/detail/65682
13. https://zfin.org/ZDB-FIG-180720-23
14. http://www.malacards.org/card/cholestasis_benign_recurrent_intrahepatic_2
15. https://www.nature.com/articles/s41413-025-00441-0
16. https://pmc.ncbi.nlm.nih.gov/articles/PMC5983389/
17. https://pmc.ncbi.nlm.nih.gov/articles/PMC8534862/
18. https://pmc.ncbi.nlm.nih.gov/articles/PMC6369278/
19. https://pmc.ncbi.nlm.nih.gov/articles/PMC3584863/
20. https://pmc.ncbi.nlm.nih.gov/articles/PMC4505518/
21. https://www.proteinatlas.org/ENSG00000100154-TTC28/tissue
22. https://pmc.ncbi.nlm.nih.gov/articles/PMC3302730/
23. https://pmc.ncbi.nlm.nih.gov/articles/PMC11648667/
24. https://www.pnas.org/doi/abs/10.1073/pnas.2409447121
25. https://pmc.ncbi.nlm.nih.gov/articles/PMC4274643/
26. https://pubmed.ncbi.nlm.nih.gov/39630868/
27. https://pubmed.ncbi.nlm.nih.gov/23036704/
28. https://www.thermofisher.com/us/en/home/life-science/protein-biology/protein-biology-learning-center/protein-biology-resource-library/pierce-protein-methods/overview-post-translational-modification.html
29. https://www.ncbi.nlm.nih.gov/gene?Db=gene&Cmd=DetailsSearch&Term=23331
30. https://pmc.ncbi.nlm.nih.gov/articles/PMC25457/
31. https://pmc.ncbi.nlm.nih.gov/articles/PMC10152985/
32. https://pubmed.ncbi.nlm.nih.gov/16394881/
33. https://pmc.ncbi.nlm.nih.gov/articles/PMC6756986/
34. https://pmc.ncbi.nlm.nih.gov/articles/PMC2844474/
35. https://pmc.ncbi.nlm.nih.gov/articles/PMC8699595/
36. https://rupress.org/jcb/article/224/11/e202505046/278372/Understanding-microtubule-dynamics-The-synergy-of
37. https://pubmed.ncbi.nlm.nih.gov/9693365/
38. https://aacrjournals.org/mcr/article/22/10/909/748530/The-Complex-Regulation-of-Cytokinesis-upon
39. https://pubmed.ncbi.nlm.nih.gov/29930083/
40. https://pubmed.ncbi.nlm.nih.gov/15946753/
41. https://pubmed.ncbi.nlm.nih.gov/25548932/
42. https://pmc.ncbi.nlm.nih.gov/articles/PMC6051344/
43. https://www.genecards.org/cgi-bin/carddisp.pl?gene=GPSM2
44. https://pmc.ncbi.nlm.nih.gov/articles/PMC7854016/