---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-23T23:21:07.470288'
end_time: '2026-01-23T23:36:34.338310'
duration_seconds: 926.87
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: TMA16
  gene_symbol: TMA16
  uniprot_accession: Q96EY4
  protein_description: 'RecName: Full=Translation machinery-associated protein 16;'
  gene_info: Name=TMA16; Synonyms=C4orf43;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the TMA16 family. .
  protein_domains: Tma16. (IPR021346); Tma16_sf. (IPR038356); Tma16 (PF11176)
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
- **UniProt Accession:** Q96EY4
- **Protein Description:** RecName: Full=Translation machinery-associated protein 16;
- **Gene Information:** Name=TMA16; Synonyms=C4orf43;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the TMA16 family. .
- **Key Domains:** Tma16. (IPR021346); Tma16_sf. (IPR038356); Tma16 (PF11176)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "TMA16" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'TMA16' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **TMA16** (gene ID: TMA16, UniProt: Q96EY4) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# TMA16 (Translation Machinery-Associated Protein 16): A Comprehensive Review

## Introduction

TMA16 (Translation machinery-associated protein 16), also known by its former designation C4orf43, is a human nuclear protein that functions as an assembly factor in the biogenesis of the large (60S) ribosomal subunit. Encoded by the TMA16 gene located on chromosome 4, this 203-amino acid protein (UniProt: Q96EY4) has been structurally characterized as binding to pre-60S ribosomal particles during their late nuclear maturation stages, specifically occupying a strategic position between the rotated 5S ribonucleoprotein (5S RNP) complex and the P0 stalk [liang-2020-pre60S-summary]. Despite its recent structural characterization, TMA16 remains relatively understudied compared to other ribosome biogenesis factors, with the majority of functional insights derived from a single seminal cryo-electron microscopy study published in 2020.

The protein belongs to the conserved TMA16 family and contains the Tma16 domain (Pfam: PF11176, InterPro: IPR021346), which is found across eukaryotes from yeast to humans. Gene Ontology annotations based on direct experimental evidence indicate that TMA16 functions in preribosome binding and ribosomal large subunit biogenesis, with localization to the nucleus, nucleoplasm, and nucleolus [GO-annotations]. The primary function of TMA16 appears to be as a transient stabilizing factor that associates with pre-60S particles following the critical 5S RNP rotation event and dissociates before the particles undergo nuclear export and subsequent cytoplasmic maturation.

## Molecular Function and Structural Basis

The molecular function of TMA16 was elucidated through cryo-electron microscopy structural analysis of human pre-60S ribosomal particles purified via the nuclear export factor NMD3 [liang-2020-pre60S-summary]. According to PubMed, Liang and colleagues ([DOI](https://doi.org/10.1038/s41467-020-17237-x)) determined four structures representing assembly stages immediately before and after nuclear export, revealing TMA16 as a previously uncharacterized factor positioned in the space between the rotated 5S RNP and the P0 stalk.

The structural analysis enabled construction of an atomic model for residues 17-166 of the full-length 203-residue protein [liang-2020-pre60S-summary]. The N-terminus of TMA16 contains a remarkably long alpha-helix spanning residues 19-60, extending approximately 60 angstroms toward the peptidyl transferase center (PTC). The N-terminal end of this helix docks onto the tip of helix 39 (H39) of the 28S ribosomal RNA, with two highly conserved residues, H18 and R22, forming direct interactions with nucleotides A1867 and G1864 of H39 respectively. This N-terminal helix also engages in extensive interactions with the 5S RNA, primarily through its basic residues.

The main body of TMA16 adopts a position sandwiched between rRNA helices H42 and H25ES7. One side of TMA16, comprising the loop between helices H1 and H2 and the C-terminal region, interacts with H25ES7, while the opposite side containing the loop between H2 and H3 specifically contacts H42 [liang-2020-pre60S-summary]. This strategic positioning suggests that TMA16 may function as a sensor for the rotational state of the 5S RNP, stabilizing the pre-60S particle in a conformation appropriate for nuclear export.

The interaction between TMA16 and H39 is further stabilized by the assembly factor GTPBP4 (known as Nog2 in yeast). Specifically, residue Y124 of the GTPBP4 N-terminal domain enhances the stacking interaction between H18 of TMA16 and A1867 of H39 [liang-2020-pre60S-summary]. This tripartite interaction network indicates that TMA16 function is integrated with the broader assembly factor machinery controlling pre-60S maturation.

TMA16 has also been annotated with the molecular function "protein-macromolecule adaptor activity" (GO:0030674) based on direct assay evidence from the Liang et al. study [GO-annotations]. This annotation reflects the structural role of TMA16 in bridging between the 5S RNP complex and the ribosomal RNA elements of the maturing 60S subunit. High-throughput interactome mapping studies have identified physical interactions between TMA16 and proteins including AP2M1, CASTOR1, HTT (huntingtin), KLHL2, KRTAP10-7, and TSPYL2, although the functional significance of these interactions remains to be determined [rolland-2014-interactome-abstract].

## Subcellular Localization

TMA16 localizes to the nucleus, consistent with its function in the nuclear stages of ribosome biogenesis. According to annotations from the Human Protein Atlas (HPA) based on direct assay evidence, TMA16 is found in both the nucleoplasm and nucleolus [GO-annotations]. This dual localization is consistent with the known pathway of 60S ribosome biogenesis, which initiates in the nucleolus and progresses through the nucleoplasm before particles are exported to the cytoplasm.

The nucleolar localization positions TMA16 appropriately for its role in pre-60S maturation, as this is where the majority of ribosomal RNA transcription and early processing occurs. The nucleoplasmic localization reflects the later maturation stages where TMA16 is structurally observed to associate with pre-60S particles that have completed 5S RNP rotation but have not yet undergone nuclear export [liang-2020-pre60S-summary].

Additional localization data from high-throughput studies supports nuclear localization of TMA16, with the protein detected in the human sperm nucleus proteome ([DOI](https://doi.org/10.1002/pmic.201000799), PMID: 21630459).

## Role in 60S Ribosome Biogenesis

Eukaryotic ribosome biogenesis is an extraordinarily complex process involving over 200 assembly factors and approximately 76 small nucleolar RNAs working in concert to fold, modify, and process ribosomal RNA while coordinating binding of ribosomal proteins [konikkat-2017-60S-review-abstract]. The large 60S ribosomal subunit assembly pathway proceeds through the nucleolus and nucleoplasm before particles undergo Crm1-dependent nuclear export and final cytoplasmic maturation.

A landmark discovery in understanding 60S biogenesis was the demonstration that the 5S RNP complex, consisting of 5S rRNA bound to ribosomal proteins L5 (uL18) and L11 (uL5), undergoes a dramatic ~180-degree rotation during maturation [leidig-2014-5SRNP-rotation-abstract]. According to PubMed, Leidig and colleagues ([DOI](https://doi.org/10.1038/ncomms4491)) showed using cryo-EM that the 5S RNP is initially positioned in a pre-rotation conformation that is nearly opposite its final mature position on the 60S subunit. This rotation is coordinated with remodeling of neighboring 25S rRNA helices and is stabilized by assembly factors including Rsa4 and Nog1.

TMA16 enters the pre-60S assembly pathway after the 5S RNP rotation has occurred. The structural analysis by Liang et al. shows that TMA16 binds in the space that opens up between the rotated 5S RNP and the P0 stalk [liang-2020-pre60S-summary]. Critically, TMA16 is present in the earlier maturation states (pre-A and A) but absent from the later states (B and C), indicating that its association with pre-60S particles is transient.

The timing of TMA16 action is constrained by incompatibilities with both earlier and later assembly factors. TMA16 binding is incompatible with factors that act earlier than NMD3, including Nug1 and Cgr1, which are present in nucleoplasmic Nog2-particles [liang-2020-pre60S-summary]. It also has a steric clash with the ribosomal protein uL16, which is incorporated at later stages. These observations define a relatively narrow time window for TMA16 function: after 5S RNP rotation and before the departure of GTPBP4.

The observation that TMA16 is absent from equivalent positions in yeast pre-60S structures at similar maturation stages suggests that TMA16 may be a transient binding factor whose association timing is strictly controlled [liang-2020-pre60S-summary]. This transient nature, combined with its strategic position sensing the 5S RNP rotation state, has led to the suggestion that TMA16 may function as a structural checkpoint or nuclear export adapter. In yeast, Tma16 has been found in pre-60S particles purified through Arx1 or Lsg1, and accumulates on pre-60S Lsg1-particles when Nog1 release is impaired, supporting a role in the export-proximate stages of assembly.

## Conservation and Evolutionary Context

TMA16 is conserved across eukaryotes, with identifiable homologs from yeast (Saccharomyces cerevisiae) to humans. The Tma16 domain (PF11176) that defines this protein family is found in all major eukaryotic lineages, indicating an ancient origin and fundamental importance in ribosome biogenesis.

Despite this conservation at the sequence level, there appear to be species-specific differences in the behavior of TMA16 family proteins. As noted above, human TMA16 was clearly resolved in cryo-EM structures of pre-60S particles, whereas the equivalent position appears empty in yeast structures at comparable maturation stages [liang-2020-pre60S-summary]. This may reflect differences in the kinetics of TMA16 association and dissociation between species, or could indicate that the protein is more stably associated with pre-60S particles in humans than in yeast.

A comprehensive proteomics study of yeast 60S ribosome biogenesis factors provided important insights into yeast Tma16 interactions. Sailer and colleagues ([DOI](https://doi.org/10.1016/j.celrep.2022.110353)) used cross-linking mass spectrometry to identify interactions between the N-terminal region of Tma16 and Rei1 (a cytoplasmic assembly factor), as well as between the C-terminal region of Tma16 and ribosomal protein uL18 [sailer-2022-60S-landscape-abstract]. Since uL18 and Rei1 are located distantly from each other on the pre-60S surface, this suggests that yeast Tma16 adopts an extended conformation bridging these sites. The abundance pattern of Tma16 in various pre-60S particle preparations was most similar to the Arx1/Alb1 complex, consistent with its role at cytoplasmic maturation stages. These data support classification of yeast Tma16 as a cytoplasmic ribosome biogenesis factor, somewhat later than the nuclear localization observed for human TMA16.

Phenotypic analysis of yeast TMA16 (YOR252W) deletion mutants from the Saccharomyces Genome Database reveals that TMA16 is not essential for viability [SGD-TMA16]. The null mutant phenotypes include altered competitive fitness, haploinsufficiency, decreased heat sensitivity, and abnormal vacuolar morphology. The SGD describes yeast TMA16 as a "protein of unknown function that associates with ribosomes." Interestingly, the yeast gene has 121 documented physical interactions across 104 unique genes, including numerous ribosomal proteins and biogenesis factors identified through affinity capture-mass spectrometry approaches. The transcription of yeast TMA16 is regulated by stress-responsive transcription factors Yap6p (heat response) and Sfp1p (stress response), consistent with coordination of its expression with ribosome biogenesis rates.

A recent comprehensive structural analysis comparing human and yeast ribosome biogenesis confirmed the high degree of conservation in the overall pathway. According to PubMed, Fiorentino and colleagues ([DOI](https://doi.org/10.1093/nar/gkaf255)) demonstrated that the interaction networks and conformational changes during 60S assembly are essentially identical between yeast and humans, supporting the evolutionary preservation of ribosomal assembly mechanisms.

## Regulation of TMA16 Expression

While relatively little is known about the transcriptional or post-transcriptional regulation of human TMA16, studies in yeast have revealed that TMA16 mRNA levels are regulated by P-body proteins during cellular stress. According to PubMed, Loll-Krippleber and Brown ([DOI](https://doi.org/10.1038/s41467-017-00632-2)) identified yeast TMA16 as one of six mRNAs (including HHT1, ACF4, ARL3, RRS1, and YOX1) whose abundance is controlled by the P-body protein Lsm1 during DNA replication stress induced by hydroxyurea treatment [loll-krippleber-2017-pbody-abstract].

P-bodies are cytoplasmic granules that form in response to various stresses and serve as sites for mRNA storage and degradation. The finding that Lsm1 controls TMA16 mRNA abundance to prevent its "toxic accumulation" during replication stress suggests that TMA16 overexpression may be detrimental under stress conditions. This could relate to the importance of precisely controlling ribosome biogenesis rates during cellular stress responses.

At the protein level, TMA16 has been found to undergo post-translational modifications including ADP-ribosylation at serine-9 and O-linked glycosylation. Three genetic variants have been documented in human populations: R12Q, Q65P, and I176T, though no disease associations have been established for these variants.

## Implications for Disease

TMA16 has not been directly implicated as a causative gene in any disease to date. However, given its role in ribosome biogenesis, it may be relevant to the class of disorders known as ribosomopathies, which result from defects in ribosome production or function. Ribosomopathies include Diamond-Blackfan anemia, Shwachman-Diamond syndrome, and others, typically caused by mutations in ribosomal proteins or core biogenesis factors.

TMA16 was identified as a differentially methylated gene in a study of Parkinson's disease biomarkers. According to PubMed, Zhu and colleagues ([DOI](https://doi.org/10.1016/j.clineuro.2025.109014)) found TMA16 among a small set of genes with altered methylation patterns in both cerebrospinal fluid and blood cell-free DNA of Parkinson's disease patients. The significance of this finding for disease pathophysiology remains to be determined.

Additionally, a genome-wide association study in Korean women identified TMA16 among genes associated with body mass index and basal metabolic rate ([DOI](https://doi.org/10.4162/nrp.2016.10.1.115), PMID: 26865924), though these associations require replication and functional validation.

## Open Questions

Despite significant advances in understanding TMA16 structure and localization, several important questions remain:

1. **Precise molecular function:** While TMA16 clearly associates with pre-60S particles at specific maturation stages, its exact biochemical function remains unclear. Does it actively promote structural transitions, or does it serve primarily as a passive stabilizer? The suggestion that it could function as a nuclear export adapter requires experimental validation.

2. **Mechanism of association and release:** What signals trigger TMA16 binding to pre-60S particles after 5S RNP rotation, and what causes its release? The dependence on GTPBP4 for stabilizing the TMA16-H39 interface suggests that GTPBP4 departure may trigger TMA16 release, but this has not been directly tested.

3. **Species-specific differences:** Why is TMA16 visible in human pre-60S structures but not in yeast structures at comparable stages? This could reflect genuine differences in TMA16 function between species or could be a technical artifact of particle isolation conditions.

4. **Functional significance of protein interactions:** The high-throughput identification of TMA16 interacting partners (AP2M1, CASTOR1, HTT, etc.) raises questions about potential functions beyond ribosome biogenesis. Are these interactions physiologically relevant?

5. **Consequences of TMA16 deficiency:** In yeast, TMA16 deletion mutants are viable, with phenotypes including altered competitive fitness, haploinsufficiency, decreased heat sensitivity, and abnormal vacuolar morphology [SGD-TMA16]. This suggests Tma16 is not essential for ribosome biogenesis in yeast. No detailed characterization of TMA16 knockout or knockdown phenotypes in mammalian cells has been published. Such studies would clarify whether human TMA16 has a more essential or modulatory role.

6. **Post-translational modifications:** The functional significance of ADP-ribosylation at serine-9 and O-linked glycosylation of TMA16 is unknown. Could these modifications regulate TMA16 localization or activity?

7. **Disease relevance:** Does TMA16 contribute to ribosomopathies or other diseases? The methylation changes observed in Parkinson's disease warrant further investigation.

## References

1. **liang-2020-pre60S**: Liang X, Zuo MQ, Zhang Y, Li N, Ma C, Dong MQ, Gao N. Structural snapshots of human pre-60S ribosomal particles before and after nuclear export. *Nature Communications*. 2020 Jul 15;11(1):3542. PMID: 32669547. PMCID: PMC7363849. [DOI: 10.1038/s41467-020-17237-x](https://doi.org/10.1038/s41467-020-17237-x)

2. **loll-krippleber-2017-pbody**: Loll-Krippleber R, Brown GW. P-body proteins regulate transcriptional rewiring to promote DNA replication stress resistance. *Nature Communications*. 2017 Sep 15;8(1):558. PMID: 28916784. PMCID: PMC5601920. [DOI: 10.1038/s41467-017-00632-2](https://doi.org/10.1038/s41467-017-00632-2)

3. **konikkat-2017-60S-review**: Konikkat S, Woolford JL Jr. Principles of 60S ribosomal subunit assembly emerging from recent studies in yeast. *Biochemical Journal*. 2017 Jan 15;474(2):195-214. PMID: 28062837. PMCID: PMC5555582. [DOI: 10.1042/BCJ20160516](https://doi.org/10.1042/BCJ20160516)

4. **leidig-2014-5SRNP-rotation**: Leidig C, Thoms M, Holdermann I, Bradatsch B, Berninghausen O, Bange G, Sinning I, Hurt E, Beckmann R. 60S ribosome biogenesis requires rotation of the 5S ribonucleoprotein particle. *Nature Communications*. 2014 Mar 24;5:3491. PMID: 24662372. [DOI: 10.1038/ncomms4491](https://doi.org/10.1038/ncomms4491)

5. **ma-2017-cytoplasmic-pre60S**: Ma C, Wu S, Li N, Chen Y, Yan K, Li Z, Zheng L, Lei J, Woolford JL, Gao N. Structural snapshot of cytoplasmic pre-60S ribosomal particles bound by Nmd3, Lsg1, Tif6 and Reh1. *Nature Structural & Molecular Biology*. 2017 Mar;24(3):214-220. PMID: 28112732. PMCID: PMC5555584. [DOI: 10.1038/nsmb.3364](https://doi.org/10.1038/nsmb.3364)

6. **vanden-broeck-2023-human-pre60S**: Vanden Broeck A, Klinge S. Principles of human pre-60S biogenesis. *Science*. 2023 Jul 7;381(6653):eadh3892. PMID: 37410842. [DOI: 10.1126/science.adh3892](https://doi.org/10.1126/science.adh3892)

7. **rolland-2014-interactome**: Rolland T, Taşan M, Charloteaux B, et al. A proteome-scale map of the human interactome network. *Cell*. 2014 Nov 20;159(5):1212-1226. PMID: 25416956. PMCID: PMC4266588. [DOI: 10.1016/j.cell.2014.10.050](https://doi.org/10.1016/j.cell.2014.10.050)

8. **luck-2020-HuRI-interactome**: Luck K, Kim DK, Lambourne L, et al. A reference map of the human binary protein interactome. *Nature*. 2020 Apr;580(7803):402-408. PMID: 32296183. PMCID: PMC7169983. [DOI: 10.1038/s41586-020-2188-x](https://doi.org/10.1038/s41586-020-2188-x)

9. **thoms-2018-5SRNP-cgr1**: Thoms M, Mitterer V, Kater L, Falquet L, Beckmann R, Kressler D, Hurt E. Suppressor mutations in Rpf2-Rrs1 or Rpl5 bypass the Cgr1 function for pre-ribosomal 5S RNP-rotation. *Nature Communications*. 2018 Oct 5;9(1):4094. PMID: 30291245. PMCID: PMC6173701. [DOI: 10.1038/s41467-018-06660-w](https://doi.org/10.1038/s41467-018-06660-w)

10. **thoms-2023-rixosome**: Thoms M, Lau B, Cheng J, et al. Structural insights into coordinating 5S RNP rotation with ITS2 pre-RNA processing during ribosome formation. *EMBO Reports*. 2023 Dec;24(12):e57984. PMID: 37921038. PMCID: PMC10702828. [DOI: 10.15252/embr.202357984](https://doi.org/10.15252/embr.202357984)

11. **fiorentino-2025-MDN1-NLE1**: Fiorentino F, Thoms M, Wild K, Denk T, Cheng J, Zeman J, Sinning I, Hurt E, Beckmann R. Highly conserved ribosome biogenesis pathways between human and yeast revealed by the MDN1-NLE1 interaction and NLE1 containing pre-60S subunits. *Nucleic Acids Research*. 2025 Apr 10;53(7). PMID: 40207627. PMCID: PMC11983104. [DOI: 10.1093/nar/gkaf255](https://doi.org/10.1093/nar/gkaf255)

12. **nerurkar-2015-ribosome-export-review**: Nerurkar P, Altvater M, Gerhardy S, Schütz S, Fischer U, Weirich C, Panse VG. Eukaryotic Ribosome Assembly and Nuclear Export. *International Review of Cell and Molecular Biology*. 2015;319:107-40. PMID: 26404467. [DOI: 10.1016/bs.ircmb.2015.07.002](https://doi.org/10.1016/bs.ircmb.2015.07.002)

13. **UniProt Q96EY4**: UniProt Consortium. UniProt entry Q96EY4 (TMA16_HUMAN). https://www.uniprot.org/uniprotkb/Q96EY4

14. **de-mateo-2011-sperm-nucleus**: de Mateo S, Castillo J, Estanyol JM, Ballescà JL, Oliva R. Proteomic characterization of the human sperm nucleus. *Proteomics*. 2011 Jun;11(13):2714-26. PMID: 21630459. [DOI: 10.1002/pmic.201000799](https://doi.org/10.1002/pmic.201000799)

15. **sailer-2022-60S-landscape**: Sailer C, Jansen J, Sekulski K, Cruz VE, Erzberger JP, Stengel F. A comprehensive landscape of 60S ribosome biogenesis factors. *Cell Reports*. 2022 Feb 8;38(6):110353. PMID: 35139378. PMCID: PMC8884084. [DOI: 10.1016/j.celrep.2022.110353](https://doi.org/10.1016/j.celrep.2022.110353)

16. **SGD-TMA16**: Saccharomyces Genome Database. TMA16/YOR252W Gene Entry. https://www.yeastgenome.org/locus/S000005778


## Citations

1. SGD-TMA16-entry.md
2. konikkat-2017-60S-review-abstract.md
3. leidig-2014-5SRNP-rotation-abstract.md
4. liang-2020-pre60S-abstract.md
5. liang-2020-pre60S-fulltext.txt
6. liang-2020-pre60S-summary.md
7. loll-krippleber-2017-pbody-abstract.md
8. loll-krippleber-2017-pbody-fulltext.txt
9. luck-2020-HuRI-abstract.md
10. ma-2017-cytoplasmic-pre60S-abstract.md
11. rolland-2014-interactome-abstract.md
12. sailer-2022-60S-landscape-abstract.md
13. thoms-2018-cgr1-abstract.md
14. vanden-broeck-2023-human-pre60S-abstract.md