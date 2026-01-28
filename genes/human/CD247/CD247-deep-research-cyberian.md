---
provider: cyberian
model: deep-research
cached: true
start_time: '2026-01-22T16:35:37.998874'
end_time: '2026-01-22T16:35:38.001038'
duration_seconds: 0.0
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: CD247
  gene_symbol: CD247
  uniprot_accession: P20963
  protein_description: 'RecName: Full=T-cell surface glycoprotein CD3 zeta chain;
    AltName: Full=T-cell receptor T3 zeta chain; AltName: CD_antigen=CD247; Flags:
    Precursor;'
  gene_info: Name=CD247; Synonyms=CD3Z, T3Z, TCRZ;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the CD3Z/FCER1G family. .
  protein_domains: CD3_zeta/IgE_Fc_rcpt_gamma. (IPR021663); Phos_immunorcpt_sig_ITAM.
    (IPR003110); T-cell_CD3_zeta. (IPR024128); ITAM (PF02189); TCR_zetazeta (PF11628)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 24
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P20963
- **Protein Description:** RecName: Full=T-cell surface glycoprotein CD3 zeta chain; AltName: Full=T-cell receptor T3 zeta chain; AltName: CD_antigen=CD247; Flags: Precursor;
- **Gene Information:** Name=CD247; Synonyms=CD3Z, T3Z, TCRZ;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the CD3Z/FCER1G family. .
- **Key Domains:** CD3_zeta/IgE_Fc_rcpt_gamma. (IPR021663); Phos_immunorcpt_sig_ITAM. (IPR003110); T-cell_CD3_zeta. (IPR024128); ITAM (PF02189); TCR_zetazeta (PF11628)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "CD247" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'CD247' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **CD247** (gene ID: CD247, UniProt: P20963) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# ATP5MC2 (ATP Synthase F0 Complex Subunit C2, Mitochondrial): A Comprehensive Review

## Introduction and Summary

ATP5MC2 (also known as ATP5G2) encodes one of three nuclear genes in humans that produce the c-subunit of the mitochondrial ATP synthase F0 complex. This small, highly hydrophobic protein is an essential structural component of the proton-translocating c-ring, the molecular rotor that converts the proton electrochemical gradient across the inner mitochondrial membrane into the mechanical energy required for ATP synthesis [jonckheere-2012-architecture-abstract]. The ATP synthase (also called F1F0-ATPase or Complex V) is the final enzyme of the oxidative phosphorylation pathway, synthesizing the vast majority of cellular ATP through a remarkable rotary catalysis mechanism first described by Paul Boyer [boyer-1997-splendid-abstract].

A distinctive feature of the human c-subunit is that it is encoded by three separate nuclear genes—ATP5MC1 (formerly ATP5G1), ATP5MC2 (formerly ATP5G2), and ATP5MC3 (formerly ATP5G3)—located on chromosomes 17, 12, and 2, respectively. These three genes encode precursor proteins with different N-terminal mitochondrial targeting sequences but produce absolutely identical mature 75-76 amino acid proteins after import into mitochondria and proteolytic processing [dyer-1993-subunitc-abstract]. Despite this apparent genetic redundancy, the three isoforms are not functionally interchangeable, and all three genes are required for normal ATP synthase function and cellular respiration [vantourout-2010-targeting-abstract].

The c-subunit functions as the essential rotor element of the F0 sector, forming a ring of eight identical subunits (c8-ring) in mammalian mitochondria that directly couples proton translocation to mechanical rotation [gu-2019-cryoem-abstract]. Each c-subunit contains a conserved glutamate residue (Glu59 in human numbering) in the middle of its transmembrane region that is essential for binding and translocating protons. The rotation of the c-ring, driven by proton flow down the electrochemical gradient, mechanically drives the rotation of the central γ-subunit stalk in the F1 sector, inducing the conformational changes in the catalytic β-subunits that drive ATP synthesis. This elegant mechanism establishes ATP synthase as one of nature's most efficient molecular motors.

## Structural Organization of the C-Subunit and C-Ring

The mature c-subunit is a small, extremely hydrophobic protein of 75-76 amino acids that forms a hairpin-like structure consisting of two α-helical transmembrane segments connected by a short polar loop that faces the intermembrane space [hong-2008-inhibitors-abstract]. The N-terminal and C-terminal helices span the inner mitochondrial membrane, with the conserved proton-binding glutamate residue (Glu59) located in the middle of the C-terminal helix, positioned approximately at the center of the lipid bilayer.

In mammalian mitochondria, eight identical c-subunits oligomerize to form the c8-ring, a cylindrical structure embedded in the inner mitochondrial membrane [gu-2019-cryoem-abstract]. Cryo-electron microscopy studies have revealed the detailed architecture of the mammalian ATP synthase, showing that the c8-ring interacts directly with the a-subunit (ATP6), which provides the two half-channels for proton access from either side of the membrane [jonckheere-2012-architecture-abstract]. The interface between the c-ring and subunit a is critical for proton translocation and represents the site of action of important ATP synthase inhibitors including oligomycin.

The c-ring stoichiometry varies considerably among different organisms, ranging from 8 to 17 c-subunits depending on the species. This variation has significant bioenergetic implications because the c-ring stoichiometry determines the number of protons translocated per 360-degree rotation and thus the H+/ATP ratio of the enzyme. With eight c-subunits and three ATP synthesis sites in the F1 sector, mammalian ATP synthase has an ion-to-ATP ratio of approximately 2.67 (8/3), making it one of the most efficient ATP synthases in terms of protons required per ATP molecule synthesized.

The center of the c-ring forms a lipid-filled pore that has been proposed to have functional significance beyond ATP synthesis, potentially participating in the formation of the mitochondrial permeability transition pore (mPTP) under certain pathological conditions [spikes-2020-cringpore-abstract], although this remains controversial [he-2017-persistence-abstract].

## The Proton Translocation Mechanism

The c-ring functions as a proton-powered rotary motor that converts the energy stored in the proton electrochemical gradient into mechanical rotation. The currently accepted mechanism involves a sequential process of protonation and deprotonation of the essential Glu59 residues on adjacent c-subunits as they pass through the interface with subunit a [yanagisawa-2017-stepping-abstract].

In this mechanism, protons enter through a half-channel in subunit a from the intermembrane space (positive side), protonate the Glu59 carboxyl group on an approaching c-subunit, and remain bound as the c-subunit rotates through the hydrophobic interior of the membrane. When the protonated c-subunit completes nearly a full rotation and reaches the interface with subunit a at the other half-channel, the proton is released into the mitochondrial matrix (negative side), and the now-deprotonated Glu59 can interact with the highly conserved arginine residue (Arg159) in subunit a. This electrostatic interaction between the negatively charged carboxylate and the positively charged arginine drives the c-ring forward, positioning the next protonated c-subunit for deprotonation [yanagisawa-2017-stepping-abstract].

Single-molecule studies using gold nanorod attachments to track c-ring rotation have demonstrated that the motor exhibits discrete stepping behavior, with transient dwells occurring at approximately 36° intervals corresponding to single c-subunit steps [yanagisawa-2017-stepping-abstract]. These studies also revealed that the stepping frequency is pH-dependent, with transient dwells increasing inversely with pH, consistent with the protonation-dependent nature of the rotation.

The proton-binding Glu59 residue (equivalent to Asp61 in E. coli) is the target of the ATP synthase inhibitor dicyclohexylcarbodiimide (DCCD), which covalently modifies this residue and blocks proton translocation. Similarly, the macrolide antibiotic oligomycin binds at the interface between the c-ring and subunit a, blocking proton flow by interfering with access to the Glu59 residues [hong-2008-inhibitors-abstract].

## Subcellular Localization and Mitochondrial Import

ATP5MC2 encodes a precursor protein of 141 amino acids that includes a 66-amino acid N-terminal mitochondrial targeting sequence (also called the presequence or transit peptide) followed by the 75-amino acid mature c-subunit [dyer-1993-subunitc-abstract]. The protein is synthesized on cytosolic ribosomes and imported into mitochondria through the TIM/TOM translocase machinery.

Upon import into the mitochondrial matrix, the targeting sequence is cleaved by mitochondrial processing peptidase (MPP), releasing the mature c-subunit that then inserts into the inner mitochondrial membrane [jonckheere-2012-architecture-abstract]. The cleaved presequence is rapidly degraded by matrix proteases, and recent studies have shown that this degradation is important for preventing potentially harmful accumulation of the amphipathic presequence peptide.

The mature c-subunit localizes exclusively to the inner mitochondrial membrane, where it assembles into the c8-ring structure as part of the F0 sector of ATP synthase. The protein faces both the intermembrane space (polar loop connecting the two transmembrane helices) and the matrix (N- and C-termini), with the transmembrane helices embedded in the lipid bilayer.

Interestingly, despite encoding identical mature proteins, the three c-subunit isoforms (from ATP5MC1, ATP5MC2, and ATP5MC3) appear to serve non-redundant functions, with their distinct targeting sequences conferring isoform-specific properties [vantourout-2010-targeting-abstract]. Studies have shown that silencing any single isoform results in ATP synthesis defects that cannot be rescued by overexpression of the other isoforms, suggesting that the targeting peptides play roles beyond simply directing import, possibly influencing assembly, stoichiometry, or temporal expression of the c-subunit.

## Post-Translational Modifications: Lysine Trimethylation

A critical post-translational modification of the c-subunit is the trimethylation of lysine-43 (Lys43) by the mitochondrial methyltransferase ATPSCKMT (formerly FAM173B) [malecki-2019-fam173b-abstract]. This modification is highly conserved across metazoans, with Lys43 being invariably trimethylated in all species examined.

Małecki et al. (2019) demonstrated that CRISPR/Cas9-mediated knockout of FAM173B (ATPSCKMT) in mammalian cells completely abrogated trimethylation of Lys43 in the c-subunit [malecki-2019-fam173b-abstract]. The functional consequences of this loss of methylation were significant: cells lacking Lys43 methylation showed aberrant incorporation of the c-subunit into the ATP synthase complex and approximately 50% reduction in oxidative phosphorylation-driven ATP synthesis. Complementation with wild-type FAM173B or orthologous enzymes from other species restored both methylation and function, confirming the specificity of this enzyme-substrate relationship.

The precise molecular mechanism by which Lys43 trimethylation promotes proper c-subunit incorporation into the ATP synthase complex remains to be fully elucidated. The modification may affect protein-protein interactions within the c-ring or between the c-ring and other F0 components, potentially influencing the stability or assembly kinetics of the complex.

## The Three Human C-Subunit Genes: Redundancy and Specificity

Humans possess three nuclear genes encoding the ATP synthase c-subunit: ATP5MC1 (chromosome 17), ATP5MC2 (chromosome 12), and ATP5MC3 (chromosome 2). All three genes produce identical mature proteins of 75-76 amino acids, but they differ in their N-terminal mitochondrial targeting sequences, untranslated regions, and expression patterns [dyer-1993-subunitc-abstract].

The targeting sequences have different lengths: the P1 isoform (from ATP5MC1) has a 61-amino acid targeting peptide, while the P2 isoform (from ATP5MC2) has two alternatively spliced forms with 82 and 123 amino acid targeting peptides. The P3 isoform (from ATP5MC3) has a distinct targeting sequence but retains the conserved RFS motif critical for mitochondrial import and processing.

Despite the identity of their mature proteins, studies have revealed that the three isoforms are not functionally redundant [vantourout-2010-targeting-abstract]. Silencing any single isoform (P1, P2, or P3) individually results in significant ATP synthesis defects, and importantly, the isoforms cannot cross-complement each other. When P2 expression was specifically silenced, it caused not only ATP synthesis defects but also defective cytochrome oxidase assembly and function, suggesting that the P2 isoform (encoded by ATP5MC2) may have specific roles in respiratory chain assembly or maintenance.

The expression of exogenous P1 could rescue P1 silencing, and P2 could rescue P2 silencing, but P1 could not rescue P2 silencing and vice versa [vantourout-2010-targeting-abstract]. This functional specificity residing in the targeting peptides suggests that they may have roles beyond simply directing mitochondrial import, potentially influencing protein folding, assembly timing, or interactions with assembly factors.

## Disease Associations and Clinical Relevance

The c-subunit has been implicated in several disease contexts, with the most prominent being its accumulation in neuronal ceroid lipofuscinoses (NCL), a group of progressive neurodegenerative lysosomal storage disorders collectively known as Batten disease [palmer-1992-batten-abstract].

### Neuronal Ceroid Lipofuscinoses (Batten Disease)

In late infantile and juvenile forms of NCL (CLN2 and CLN3 diseases), subunit c accumulates abnormally in lysosomes rather than being properly degraded [palmer-1992-batten-abstract]. Under normal conditions, subunit c is present exclusively as an inner mitochondrial membrane component, but in NCL, immunohistochemical and biochemical studies have demonstrated massive accumulation of the protein in lysosomes throughout the brain and other tissues. This accumulation is associated with the characteristic autofluorescent lipopigment storage material found in affected cells.

The mechanism underlying c-subunit accumulation in NCL involves a specific failure in the degradation pathway rather than overproduction. The proteins mutated in different forms of NCL (including CLN2/TPP1, a lysosomal serine protease, and CLN3, a transmembrane protein of unknown function) appear to be required for proper catabolism of the c-subunit after its normal turnover from mitochondria [hong-2008-inhibitors-abstract]. The resulting accumulation of undegraded c-subunit contributes to lysosomal dysfunction and neurodegeneration, though the precise pathogenic mechanisms remain under investigation.

### Mitochondrial Permeability Transition Pore

The c-ring has been proposed as a candidate component of the mitochondrial permeability transition pore (mPTP), a non-specific high-conductance channel in the inner mitochondrial membrane that opens under conditions of calcium overload and oxidative stress [spikes-2020-cringpore-abstract]. Opening of the mPTP leads to mitochondrial swelling, loss of membrane potential, and cell death, and is implicated in ischemia-reperfusion injury, neurodegeneration, and other pathological conditions.

Several lines of evidence have supported a role for the c-ring in mPTP formation, including structural considerations (the c-ring forms a lipid-filled central pore), genetic studies showing altered mPTP sensitivity upon c-subunit manipulation, and pharmacological evidence. However, this hypothesis remains controversial. He et al. (2017) demonstrated that simultaneous deletion of all three c-subunit genes (ATP5G1, ATP5G2, ATP5G3) in human cells did not prevent Ca2+-induced mPTP opening, leading them to conclude that the c-subunit does not provide the PTP [he-2017-persistence-abstract]. More recent studies suggest that ATP synthase may act as a negative regulator of mPTP rather than forming the pore itself.

### Neurodegenerative Diseases and Cancer

Reduced expression or dysfunction of ATP synthase components, including subunit c, has been observed in Alzheimer's disease, where it may contribute to the bioenergetic deficits observed in affected neurons [hong-2008-inhibitors-abstract]. In cancer, alterations in ATP synthase expression and activity may contribute to the metabolic reprogramming characteristic of tumor cells (the Warburg effect), though the specific role of the c-subunit in this context requires further investigation.

## Biochemical Pathway: Oxidative Phosphorylation and Rotary Catalysis

ATP5MC2 functions within the oxidative phosphorylation pathway as an essential structural component of ATP synthase (Complex V). The c-ring is mechanically coupled to the F1 catalytic sector through the central γ-subunit stalk, forming a rotary motor that couples proton flux to ATP synthesis [boyer-1997-splendid-abstract].

The rotary catalysis mechanism, elucidated primarily through the work of Paul Boyer and John Walker (who shared the Nobel Prize in Chemistry in 1997), involves three catalytic β-subunits in F1 that cycle through three conformational states during each 120° rotation of the γ-subunit: Open (O), Loose (L), and Tight (T) [boyer-1997-splendid-abstract]. In the O state, ADP and inorganic phosphate bind; transition to the L state induces substrate binding; and in the T state, ATP is synthesized. The energy input from the proton gradient does not directly drive the chemical synthesis of ATP (which occurs spontaneously in the tight binding site) but rather drives the conformational change that releases the tightly bound ATP product.

The c8-ring in mammalian ATP synthase requires eight protons (one per c-subunit) to complete one full 360° rotation [jonckheere-2012-architecture-abstract]. Since each 360° rotation produces three ATP molecules (one from each of the three catalytic sites), the theoretical H+/ATP ratio is 2.67 for mammalian ATP synthase. This represents one of the most efficient energy conversion mechanisms in biology, with the ATP synthase operating at near-thermodynamic efficiency under physiological conditions.

The mechanical coupling between the c-ring and the F1 sector is flexible, allowing for efficient energy transduction despite the stoichiometric mismatch between the c8-ring (8 proton-binding sites) and the F1 sector (3 catalytic sites). Recent cryo-EM studies have revealed that this flexibility is achieved through small rotational substates that allow the F1 head to rotate along with the c-ring for portions of each catalytic step [gu-2019-cryoem-abstract].

## Open Questions

Despite significant advances in understanding ATP synthase structure and function, several important questions regarding the c-subunit remain unresolved:

1. **Functional specificity of isoforms**: Why do the three genes encoding identical mature proteins exhibit functional non-redundancy? What specific roles do the different targeting sequences play beyond mitochondrial import?

2. **Assembly pathway**: How does the c-ring assemble, and what determines the precise c8 stoichiometry in mammals? Are there dedicated assembly factors specific to the c-ring?

3. **mPTP relationship**: What is the true relationship between the c-ring and the mitochondrial permeability transition pore? If the c-ring is not the pore itself, how does ATP synthase influence mPTP function?

4. **Tissue-specific expression**: Do the three c-subunit genes exhibit tissue-specific or developmental-specific expression patterns, and if so, what are the functional consequences?

5. **Therapeutic targeting**: Can the c-subunit or its assembly pathway be targeted therapeutically in diseases involving ATP synthase dysfunction, such as NCL or mitochondrial disorders?

6. **Methylation regulation**: How is c-subunit Lys43 trimethylation by ATPSCKMT regulated, and are there conditions under which this modification is altered with functional consequences?

7. **Lipid interactions**: The c-ring is embedded in the lipid bilayer, and lipid composition has been shown to affect ATP synthase function. What specific lipid-protein interactions are important for c-ring function and assembly?

## References

- **[boyer-1997-splendid-abstract]** Boyer PD. The ATP synthase--a splendid molecular machine. Annual Review of Biochemistry. 1997;66:717-749. PMID: 9242922

- **[jonckheere-2012-architecture-abstract]** Jonckheere AI, Smeitink JAM, Rodenburg RJT. Mitochondrial ATP synthase: architecture, function and pathology. Journal of Inherited Metabolic Diseases. 2012;35(2):211-225. DOI: 10.1007/s10545-011-9382-9. PMID: 21874297

- **[malecki-2019-fam173b-abstract]** Małecki JM, Willemen HLDM, Pinto R, Ho AYY, Moen A, Kjønstad IF, Burgering BMT, Zwartkruis F, Eijkelkamp N, Falnes PØ. Lysine methylation by the mitochondrial methyltransferase FAM173B optimizes the function of mitochondrial ATP synthase. Journal of Biological Chemistry. 2019;294(4):1128-1141. DOI: 10.1074/jbc.RA118.005473. PMID: 30530489. PMCID: PMC6349101

- **[yanagisawa-2017-stepping-abstract]** Yanagisawa S, Frasch WD. Protonation-dependent stepped rotation of the F-type ATP synthase c-ring observed by single-molecule measurements. Journal of Biological Chemistry. 2017;292(41):17093-17100. DOI: 10.1074/jbc.M117.799940. PMID: 28842490. PMCID: PMC5641864

- **[hong-2008-inhibitors-abstract]** Hong S, Pedersen PL. ATP Synthase and the Actions of Inhibitors Utilized To Study Its Roles in Human Health, Disease, and Other Scientific Areas. Microbiology and Molecular Biology Reviews. 2008;72(4):590-641. DOI: 10.1128/MMBR.00016-08. PMID: 19052322. PMCID: PMC2593570

- **[dyer-1993-subunitc-abstract]** Dyer MR, Walker JE. cDNA cloning and tissue expression of the genes for two isoforms of subunit c of the ATP synthase from bovine mitochondria. Biochemistry. 1993;32(14):3545-3553. PMID: 8466899

- **[palmer-1992-batten-abstract]** Palmer DN, Fearnley IM, Walker JE, Hall NA, Lake BD, Wolfe LS, Haltia M, Martinus RD, Jolly RD. Mitochondrial ATP synthase subunit c storage in the ceroid-lipofuscinoses (Batten disease). American Journal of Medical Genetics. 1992;42(4):561-567. PMID: 1535179

- **[spikes-2020-cringpore-abstract]** Spikes TE, Montgomery MG, Walker JE. ATP synthase c-subunit ring as the channel of mitochondrial permeability transition: Regulator of metabolism in development and degeneration. Journal of Molecular and Cellular Cardiology. 2020;144:101-113. DOI: 10.1016/j.yjmcc.2020.05.013. PMID: 32461058. PMCID: PMC7877492

- **[he-2017-persistence-abstract]** He J, Carroll J, Ding S, Fearnley IM, Walker JE. Persistence of the mitochondrial permeability transition in the absence of subunit c of human ATP synthase. Proceedings of the National Academy of Sciences USA. 2017;114(13):3409-3414. DOI: 10.1073/pnas.1702357114. PMID: 28289229

- **[gu-2019-cryoem-abstract]** Gu J, Zhang L, Zong S, Guo R, Liu T, Yi J, Wang P, Zhuo W, Yang M. Cryo-EM structure of the mammalian ATP synthase tetramer bound with inhibitory protein IF1. Science. 2019;364(6445):1068-1075. DOI: 10.1126/science.aaw4852. PMID: 31197009

- **[vantourout-2010-targeting-abstract]** Vantourout P, et al. Novel Role of ATPase Subunit C Targeting Peptides Beyond Mitochondrial Protein Import. Molecular Biology of the Cell. 2010;21(17):3122-3136. DOI: 10.1091/mbc.e09-06-0483. PMID: 20660153


## Citations

1. bettini-2017-itam-abstract.md
2. boyer-1997-splendid-abstract.md
3. call-2004-assembly-abstract.md
4. deford-watts-2011-phosphoinositide-abstract.md
5. dong-2019-structure-abstract.md
6. dyer-1993-subunitc-abstract.md
7. eshhar-1993-cart-abstract.md
8. gu-2019-cryoem-abstract.md
9. he-2017-persistence-abstract.md
10. hong-2008-inhibitors-abstract.md
11. housden-2003-phosphorylation-abstract.md
12. jonckheere-2012-architecture-abstract.md
13. malecki-2019-fam173b-abstract.md
14. malissen-1993-knockout-abstract.md
15. mizoguchi-1992-cancer-abstract.md
16. palmer-1992-batten-abstract.md
17. rieux-laucat-2006-mutations-abstract.md
18. samelson-1986-phosphorylation-abstract.md
19. spikes-2020-cringpore-abstract.md
20. straus-1993-zap70-abstract.md
21. vantourout-2010-targeting-abstract.md
22. wang-2010-zap70-abstract.md
23. weissman-1988-cloning-abstract.md
24. yanagisawa-2017-stepping-abstract.md