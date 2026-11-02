---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-30T05:14:40.921207'
end_time: '2026-09-30T05:32:20.479231'
duration_seconds: 1059.56
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: DROME
  gene_id: P13098
  gene_symbol: E-spl-m8-HLH
  uniprot_accession: P13098
  protein_description: 'RecName: Full=Enhancer of split m8 protein; Short=E(spl)m8;'
  gene_info: Name=E(spl)m8-HLH {ECO:0000312|FlyBase:FBgn0000591}; Synonyms=E(spl)
    {ECO:0000303|PubMed:2540957}, m8 {ECO:0000312|FlyBase:FBgn0000591}; ORFNames=CG8365
    {ECO:0000312|FlyBase:FBgn0000591};
  organism_full: Drosophila melanogaster (Fruit fly).
  protein_family: Not specified in UniProt
  protein_domains: bHLH_dom. (IPR011598); HES_HEY. (IPR050370); HLH_DNA-bd_sf. (IPR036638);
    Orange_dom. (IPR003650); Hairy_orange (PF07527)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 65
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: E-spl-m8-HLH-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: E-spl-m8-HLH-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P13098
- **Protein Description:** RecName: Full=Enhancer of split m8 protein; Short=E(spl)m8;
- **Gene Information:** Name=E(spl)m8-HLH {ECO:0000312|FlyBase:FBgn0000591}; Synonyms=E(spl) {ECO:0000303|PubMed:2540957}, m8 {ECO:0000312|FlyBase:FBgn0000591}; ORFNames=CG8365 {ECO:0000312|FlyBase:FBgn0000591};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** bHLH_dom. (IPR011598); HES_HEY. (IPR050370); HLH_DNA-bd_sf. (IPR036638); Orange_dom. (IPR003650); Hairy_orange (PF07527)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "E-spl-m8-HLH" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'E-spl-m8-HLH' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **E-spl-m8-HLH** (gene ID: P13098, UniProt: P13098) in DROME.

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
- **UniProt Accession:** P13098
- **Protein Description:** RecName: Full=Enhancer of split m8 protein; Short=E(spl)m8;
- **Gene Information:** Name=E(spl)m8-HLH {ECO:0000312|FlyBase:FBgn0000591}; Synonyms=E(spl) {ECO:0000303|PubMed:2540957}, m8 {ECO:0000312|FlyBase:FBgn0000591}; ORFNames=CG8365 {ECO:0000312|FlyBase:FBgn0000591};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** bHLH_dom. (IPR011598); HES_HEY. (IPR050370); HLH_DNA-bd_sf. (IPR036638); Orange_dom. (IPR003650); Hairy_orange (PF07527)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "E-spl-m8-HLH" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'E-spl-m8-HLH' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **E-spl-m8-HLH** (gene ID: P13098, UniProt: P13098) in DROME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Comprehensive Research Report: E(spl)m8-HLH (P13098) in Drosophila melanogaster

### Gene Identity and Classification

E(spl)m8-HLH (Enhancer of split m8 protein, UniProt P13098) is a basic helix-loop-helix-Orange (bHLH-O) transcriptional repressor encoded within the Enhancer of split Complex [E(spl)-C] in *Drosophila melanogaster* (pinot2024spatiotemporalregulationof pages 2-4). The E(spl)-C locus encodes seven related bHLH repressor proteins that function as canonical downstream effectors of Notch signaling during development (couturier2019regulationofnotch pages 3-4, bahrampour2020thefivefaces pages 51-53). E(spl)m8 is a member of the Hairy/Enhancer of split (HES) family, characterized by conserved bHLH, Orange, and C-terminal WRPW domains (jennings2006molecularrecognitionof pages 1-2, fisher1998grouchoproteinstranscriptional pages 2-3).

### Molecular Function and Mechanism of Action

#### Primary Function as a Transcriptional Repressor

E(spl)m8 functions primarily as a sequence-specific transcriptional repressor, converting Notch pathway activation into suppression of proneural, differentiation, and cell-cycle gene programs (bandyopadhyay2016theconservedmapk pages 1-2, ronald2025rolesplayedby pages 1-4, bandyopadhyay2016theconservedmapk pages 4-5). The protein does not activate transcription; instead, it represses target genes by binding to regulatory DNA sequences and recruiting the Groucho (Gro) corepressor (bandyopadhyay2016theconservedmapk pages 1-2, fisher1998grouchoproteinstranscriptional pages 2-3).

#### DNA Binding Specificity

E(spl)m8 exhibits sequence-specific DNA binding through its basic region. Early studies identified N-box sequences (CACNAG consensus) as E(spl) binding sites (oellers1994bhlhproteinsencoded pages 4-5, oellers1994bhlhproteinsencoded pages 5-6, oellers1994bhlhproteinsencoded pages 2-3). However, systematic characterization of all seven E(spl) bHLH proteins revealed preferential binding to class B E-box/ESE-box sequences centered on the CACGTG core motif (jennings1999targetspecificitiesof pages 2-4, jennings1999targetspecificitiesof pages 7-9, jennings1999targetspecificitiesof pages 1-2). The optimal extended consensus sequence was determined to be 5′-TGGCACGTG[C/T][C/T]A-3′, demonstrating that flanking nucleotides contribute to recognition specificity (jennings1999targetspecificitiesof pages 2-4, jennings1999targetspecificitiesof pages 6-7). This indicates E(spl)m8 preferentially recognizes CACGTG-centered E-box elements, with lower-affinity or context-dependent recognition of N-box sequences.

#### Protein-Protein Interactions and Corepressor Recruitment

The C-terminal WRPW motif (Trp-Arg-Pro-Trp) is both necessary and sufficient for recruiting the Groucho corepressor (jennings2006molecularrecognitionof pages 1-2, fisher1996thewrpwmotif pages 3-4, fisher1996thewrpwmotif pages 4-5, fisher1996thewrpwmotif pages 5-6). This tetrapeptide binds directly to the WD-repeat beta-propeller domain of Groucho, forming specific hydrophobic and polar contacts (jennings2006molecularrecognitionof pages 4-5, jennings2006molecularrecognitionof pages 5-7, jennings2006molecularrecognitionof pages 7-9). The WRPW-Groucho interaction converts DNA-bound E(spl)m8 into an active transcriptional repressor, as Groucho itself functions as a corepressor when recruited to chromatin (fisher1998grouchoproteinstranscriptional pages 2-3, fisher1996thewrpwmotif pages 3-4).

#### Post-Translational Regulation by Phosphorylation

E(spl)m8 activity is tightly controlled through multisite phosphorylation, which regulates the timing and strength of repression (bandyopadhyay2016theconservedmapk pages 1-2, bandyopadhyay2016theconservedmapk pages 15-17, bandyopadhyay2016theconservedmapk pages 17-19). The protein contains two conserved phosphorylation sites in its C-terminal P-domain:

1. **CK2 site (Ser159)**: Casein kinase 2 (CK2) phosphorylates Ser159, and this modification is required for M8-mediated repression of the proneural factor Atonal during eye development (bandyopadhyay2016theconservedmapk pages 15-17, bandyopadhyay2016theconservedmapk pages 5-7, bandyopadhyay2016theconservedmapk pages 4-5).

2. **MAPK site (Ser151)**: A PXSP MAPK consensus motif centered on Ser151 links M8 regulation to EGFR/MAPK signaling (bandyopadhyay2016theconservedmapk pages 1-2, bandyopadhyay2016theconservedmapk pages 15-17, bandyopadhyay2016theconservedmapk pages 17-19).

These phosphorylation events function as a conformational switch that relieves C-terminal autoinhibition (bandyopadhyay2016theconservedmapk pages 19-21, jozwick2023proteinkinaseck2 pages 4-7). In the unphosphorylated state, the C-terminal domain interacts intramolecularly with the HLH/Orange regions, preventing repressor activity. Phosphorylation by CK2 and MAPK relieves this inhibition, exposing the functional domains and activating M8's repressor function (bandyopadhyay2016theconservedmapk pages 19-21, bandyopadhyay2016theconservedmapk pages 5-7). Protein phosphatase 2A (PP2A) opposes this activation by targeting the MAPK site, thereby limiting the amplitude or duration of M8 activity (bandyopadhyay2016theconservedmapk pages 15-17, bandyopadhyay2016theconservedmapk pages 17-19, bandyopadhyay2016theconservedmapk pages 19-21).

This phosphorylation-dependent regulation is particularly important in the developing eye, where it ensures that M8 represses Atonal only after proneural clusters have formed and reached the threshold for R8 photoreceptor specification (bandyopadhyay2016theconservedmapk pages 1-2, bandyopadhyay2016theconservedmapk pages 19-21). Premature or constitutive M8 activity causes excessive Atonal repression, resulting in R8 photoreceptor loss and reduced eye tissue (bandyopadhyay2016theconservedmapk pages 4-5).

### Structural Domains and Functional Organization

| Feature/Domain | Description | Function |
|---|---|---|
| Protein family | Drosophila Enhancer-of-split/HES-family basic helix–loop–helix–Orange (bHLH-O) protein and one of seven related bHLH repressors encoded by the **E(spl)-C** locus. It is a canonical downstream effector of Notch signaling. (pinot2024spatiotemporalregulationof pages 2-4, bandyopadhyay2016theconservedmapk pages 24-25) | Acts primarily as a developmentally regulated transcriptional repressor, converting Notch activation into inhibition of proneural, differentiation, and cell-cycle programs. |
| bHLH domain | Conserved basic helix–loop–helix region; the basic segment contacts DNA, while the HLH segment supports homo-/heterodimerization. An intact basic region is required for sequence-specific DNA binding. (jennings1999targetspecificitiesof pages 2-4, oellers1994bhlhproteinsencoded pages 4-5) | Directs binding to E-box-related regulatory sequences and supports formation of DNA-binding dimers, enabling repression at target enhancers and promoters. |
| Orange domain | Conserved domain characteristic of Hairy/E(spl)/HES repressors, located C-terminal to the bHLH domain. It contributes to partner selectivity and functional specificity; the M8 C-terminal region can interact intramolecularly with the HLH/Orange region. (bandyopadhyay2016theconservedmapk pages 19-21, jozwick2023proteinkinaseck2 pages 4-7) | Helps specify protein–protein interactions and participates in autoinhibitory control of M8. Phosphorylation-dependent relief of this inhibition is proposed to expose the Orange domain and activate repression. |
| WRPW motif | Strictly conserved C-terminal tetrapeptide **Trp–Arg–Pro–Trp**. It binds directly to the WD-repeat beta-propeller domain of the Groucho corepressor; the motif is sufficient to confer Groucho-dependent repression in tethering assays. (jennings2006molecularrecognitionof pages 1-2, fisher1996thewrpwmotif pages 3-4, jennings2006molecularrecognitionof pages 4-5) | Recruits Groucho to M8-bound regulatory DNA, converting sequence-specific DNA occupancy into active transcriptional repression. |
| CK2 phosphorylation site (S159) | Conserved casein kinase 2 recognition site centered on **Ser159** in the C-terminal P-domain. CK2 phosphorylation is supported biochemically, and S159 phosphomimetic variants increase M8 repressor activity in the developing eye. (bandyopadhyay2016theconservedmapk pages 15-17, bandyopadhyay2016theconservedmapk pages 5-7, bandyopadhyay2016theconservedmapk pages 4-5) | Helps relieve C-terminal autoinhibition and activate M8 at the appropriate stage of the morphogenetic furrow. Dysregulated activation causes excessive Atonal repression, R8 photoreceptor loss, and reduced eye tissue. |
| MAPK phosphorylation site (S151) | Conserved **PXSP** MAPK-consensus motif centered on **Ser151**. Genetic and phosphomimetic experiments connect this site to EGFR/MAPK-dependent regulation, although direct phosphorylation by a specific Drosophila MAPK was not biochemically established in the cited study. (bandyopadhyay2016theconservedmapk pages 1-2, bandyopadhyay2016theconservedmapk pages 15-17, bandyopadhyay2016theconservedmapk pages 17-19) | Couples EGFR/MAPK signaling to the spatial and temporal activation of M8 repression. Its regulation delays strong M8 activity until Atonal has reached the threshold required for R8 specification; PP2A is proposed to oppose this activation. |
| DNA-binding specificity | M8 can bind the historically defined N-box consensus **CACNAG**, but systematic analysis of all seven E(spl) bHLH proteins found higher affinity for a class-B E-box/ESE-box centered on **CACGTG**. The optimal extended consensus was reported as **5′-TGGCACGTG[C/T][C/T]A-3′**, showing that flanking bases contribute to recognition. (jennings1999targetspecificitiesof pages 2-4, jennings1999targetspecificitiesof pages 7-9, jennings1999targetspecificitiesof pages 1-2) | Provides sequence-selective occupancy of target regulatory DNA. The best-supported interpretation is preferential binding to CACGTG-centered ESE sites, with lower-affinity or context-dependent recognition of N-boxes. |
| Protein interactions | Groucho is recruited through the WRPW motif. M8 also participates in interactions involving proneural bHLH factors such as Atonal, and its C-terminal domain can autoinhibit interaction through the HLH/Orange region. CK2 is a direct regulatory kinase; functional evidence also links M8 to MAPK and opposing PP2A activity. (bandyopadhyay2016theconservedmapk pages 1-2, bandyopadhyay2016theconservedmapk pages 19-21, bandyopadhyay2016theconservedmapk pages 5-7) | Groucho mediates corepression; interactions with proneural factors can antagonize their activity; and kinase/phosphatase inputs tune M8’s conformation, stability, timing, and repressive strength. |


*Table: Structural domains, DNA-binding properties, interaction motifs, and regulatory phosphorylation sites of Drosophila E(spl)m8. The table links each feature to its mechanistic role in transcriptional repression.*

### Subcellular Localization

E(spl)m8 is a nuclear protein, consistent with its function as a transcription factor (pinot2024spatiotemporalregulationof pages 2-4, couturier2019regulationofnotch pages 6-8). Following Notch receptor activation by Delta ligand binding, the Notch intracellular domain (NICD) is released through proteolytic cleavage and translocates to the nucleus (pinot2024spatiotemporalregulationof pages 2-4, bahrampour2020thefivefaces pages 51-53). In the nucleus, NICD forms a transcriptional activation complex with Suppressor of Hairless [Su(H), the Drosophila CSL protein] and Mastermind, which activates E(spl)m8 transcription (pinot2024spatiotemporalregulationof pages 2-4, bivik2016controlofneural pages 16-17, bandyopadhyay2016theconservedmapk pages 1-2, bahrampour2020thefivefaces pages 51-53). E(spl)m8 protein then functions in the nucleus, where it binds to E-box/ESE-box regulatory sequences in target genes and recruits Groucho to effect transcriptional repression.

### Signaling Pathways and Regulatory Networks

#### Integration with Notch Signaling

E(spl)m8 is a direct transcriptional target of canonical Notch signaling (pinot2024spatiotemporalregulationof pages 2-4, bivik2016controlofneural pages 16-17, bandyopadhyay2016theconservedmapk pages 1-2). Upon Delta-mediated Notch activation, NICD enters the nucleus and associates with Su(H) and Mastermind to form the Notch coactivator complex (pinot2024spatiotemporalregulationof pages 2-4, bahrampour2020thefivefaces pages 51-53). This complex binds to Su(H) paired sites (SPS) and monomeric CSL sites in the E(spl) complex enhancers, driving E(spl)m8 transcription (kuang2021enhancerswithcooperative pages 14-16, kuang2020enhancerarchitecturesensitizes pages 10-11, kuang2021enhancerswithcooperative pages 5-7). The E(spl)m5/m8 mesectoderm enhancer contains SPS elements along with flanking N-box motifs, which provide negative feedback regulation through E(spl) protein binding (kuang2020enhancerarchitecturesensitizes pages 10-11, kuang2021enhancerswithcooperative pages 14-16).

SPS-containing enhancers exhibit cooperative binding of Notch coactivator complexes and are more resistant to repression by the Hairless co-repressor compared to enhancers with monomeric CSL sites (kuang2021enhancerswithcooperative pages 14-16, kuang2021enhancerswithcooperative pages 5-7, kuang2021enhancerswithcooperative pages 10-11, kuang2021enhancerswithcooperative pages 13-14). This architecture ensures consistent E(spl)m8 activation in response to Notch signaling despite competition from co-repressor complexes.

#### Cross-talk with EGFR/MAPK Signaling

E(spl)m8 activity integrates Notch and EGFR/MAPK signaling inputs through the MAPK phosphorylation site (bandyopadhyay2016theconservedmapk pages 1-2, bandyopadhyay2016theconservedmapk pages 15-17, bandyopadhyay2016theconservedmapk pages 17-19). EGFR signaling, which activates MAPK at stages 2-3 of the morphogenetic furrow during eye development, controls the spatial and temporal activation of M8 repression (bandyopadhyay2016theconservedmapk pages 15-17, bandyopadhyay2016theconservedmapk pages 17-19). Reducing EGFR dosage weakens M8 repressor activity in an MAPK site-dependent manner, while MAPK phosphomimetic variants cause premature M8 activation (bandyopadhyay2016theconservedmapk pages 1-2, bandyopadhyay2016theconservedmapk pages 15-17). This coordination between Notch-dependent transcription and MAPK-dependent post-translational activation allows precise temporal control of repression during development.

### Biological Processes and Developmental Roles

| Developmental Context | Role/Function | Target Genes Repressed | Key References |
|---|---|---|---|
| Lateral inhibition in neurogenesis | Acts downstream of Delta–Notch signaling as a nuclear bHLH-Orange repressor. Together with Groucho, M8 suppresses proneural activity in Notch-activated neighboring cells, limiting neural-fate acquisition and helping separate neural precursors. Functional overlap with other E(spl)-HLH paralogues is substantial. | **atonal (ato)** is the best-supported proneural target in the eye; more broadly, E(spl)-dependent repression antagonizes proneural bHLH programs. | Bandyopadhyay et al. (2016), [DOI](https://doi.org/10.1371/journal.pone.0159508) (bandyopadhyay2016theconservedmapk pages 1-2) |
| R8 photoreceptor specification | Delta–Notch induces E(spl)-M8 at morphogenetic-furrow stages 2–3. M8 restricts Atonal activity to one future R8 cell per proneural cluster. CK2- and EGFR/MAPK-linked phosphorylation regulates when repression begins; premature or excessive activity causes loss of R8 cells and eye tissue. | **atonal (ato)**. Reduced **senseless (sens)** expression is a downstream consequence of impaired Atonal-dependent R8 specification, but sens is not established here as a direct M8 target. | Bandyopadhyay et al. (2016), [DOI](https://doi.org/10.1371/journal.pone.0159508) (bandyopadhyay2016theconservedmapk pages 19-21, bandyopadhyay2016theconservedmapk pages 4-5, bandyopadhyay2016theconservedmapk pages 1-2) |
| R7 photoreceptor fate determination | E(spl)m8 is expressed in the R7 precursor and can mediate Notch-dependent repression separating R7 fate from R1/6 and cone-cell programs. Ectopic M8 suppresses relevant reporters, but the mild single-gene loss phenotype demonstrates strong paralogue redundancy. | **phyllopod (phyl)** and **seven-up (svp)**. Repression of phyl affects photoreceptor-versus-cone-cell specification, whereas repression of svp prevents an R1/6-like fate. Evidence is stronger for collective E(spl)-complex repression than for unique endogenous control by M8. | Ronald, Mavromatakis, and Tomlinson (2025 preprint), [DOI](https://doi.org/10.1101/2025.01.30.635716) (ronald2025rolesplayedby pages 19-31, ronald2025rolesplayedby pages 4-7, ronald2025rolesplayedby pages 1-4) |
| Neuroblast proliferation control: Type I-to-Type 0 switch | Notch-responsive M8 contributes to the developmental switch in which neuroblast daughters cease an additional division. Stabilized or ectopic M8 can promote a premature switch, particularly with temporal and Hox factors such as Castor and Antennapedia. Its contribution is lineage-dependent and partly redundant. | Chromatin-association and functional evidence implicate **Cyclin E (CycE)**, **dacapo (dap)**, and **string (stg)**, although occupancy is better established than direct M8-mediated repression of every gene in every lineage. | Bivik et al. (2016) (bivik2016controlofneural pages 11-13, bivik2016controlofneural pages 16-17, bivik2016controlofneurala pages 16-17) |
| Sensory bristle patterning | E(spl)-HLH factors convert Notch-mediated lateral inhibition into suppression of proneural activity, enabling correct spacing and selection of sensory-organ precursors. M8 contributes within a partially redundant seven-member repressor set whose paralogue-specific expression and cross-repression shape Notch-output dynamics. | Proneural programs involving **achaete–scute** factors and **senseless** are antagonized at the E(spl)-complex level; a direct, M8-specific target in this context has not been firmly established. | Couturier et al. (2019), [DOI](https://doi.org/10.1038/s41467-019-11477-2) (couturier2019regulationofnotch pages 3-4, couturier2019regulationofnotch pages 6-8); Bandyopadhyay et al. (2016) (bandyopadhyay2016theconservedmapk pages 19-21) |


*Table: This table summarizes the principal developmental contexts in which Drosophila E(spl)m8 functions, its proposed regulatory targets, and the strength or limitations of the supporting evidence.*

#### Lateral Inhibition During Neurogenesis

E(spl)m8 mediates lateral inhibition, a fundamental mechanism by which equivalent cells adopt different fates through Delta-Notch signaling (bandyopadhyay2016theconservedmapk pages 1-2). In Notch-activated cells, E(spl)m8 represses proneural bHLH activators, preventing these cells from adopting neural fates and ensuring proper spacing of neural precursors (bandyopadhyay2016theconservedmapk pages 1-2, bandyopadhyay2016theconservedmapk pages 23-24, bandyopadhyay2016theconservedmapk pages 4-5). This function is conserved across multiple developmental contexts, including the central nervous system, sensory organ development, and eye development.

#### R8 Photoreceptor Specification in Eye Development

During compound eye development, E(spl)m8 plays a critical role in R8 photoreceptor specification through regulation of the proneural factor Atonal (bandyopadhyay2016theconservedmapk pages 1-2). At morphogenetic furrow stage 1, low Notch activity induces initial Atonal expression. Atonal autoactivation then raises expression levels in proneural clusters (bandyopadhyay2016theconservedmapk pages 1-2). At stages 2-3, Delta-Notch signaling induces E(spl) repressors including M8, which act with Groucho to restrict Atonal activity to one cell per cluster—the future R8 photoreceptor (bandyopadhyay2016theconservedmapk pages 1-2, bandyopadhyay2016theconservedmapk pages 4-5).

The CK2 and MAPK phosphorylation sites ensure M8 becomes active only after Atonal has reached the threshold required for R8 specification (bandyopadhyay2016theconservedmapk pages 1-2, bandyopadhyay2016theconservedmapk pages 15-17, bandyopadhyay2016theconservedmapk pages 19-21). Premature or excessive M8 repression prevents Atonal upregulation, blocks R8 fate acquisition, and causes severe eye-tissue loss (bandyopadhyay2016theconservedmapk pages 4-5). This phosphorylation-dependent timing mechanism reconciles Notch's dual roles in early proneural induction and subsequent lateral inhibition (bandyopadhyay2016theconservedmapk pages 19-21).

#### R7 Photoreceptor Fate Determination

E(spl)m8 is expressed in R7 photoreceptor precursors and contributes to Notch-dependent fate decisions separating R7 from R1/6 and cone-cell programs (ronald2025rolesplayedby pages 10-13, ronald2025rolesplayedby pages 7-10, ronald2025rolesplayedby pages 1-4, ronald2025rolesplayedby pages 19-31, ronald2025rolesplayedby pages 4-7). Recent studies (2025) demonstrate that E(spl) complex activity represses phyllopod (phyl) and seven-up (svp) transcription during R7 specification (ronald2025rolesplayedby pages 10-13, ronald2025rolesplayedby pages 19-31, ronald2025rolesplayedby pages 7-10, ronald2025rolesplayedby pages 1-4). Repression of phyl affects photoreceptor-versus-cone-cell specification by controlling Tramtrack (Ttk) repressor degradation, while repression of svp prevents adoption of the R1/6 photoreceptor fate (ronald2025rolesplayedby pages 10-13, ronald2025rolesplayedby pages 19-31, ronald2025rolesplayedby pages 7-10).

Ectopic E(spl)m8 expression suppresses phyl and svp reporters and can transform R1/6 precursors toward R7 or cone-cell fates (ronald2025rolesplayedby pages 19-31, ronald2025rolesplayedby pages 4-7). However, the mild phenotype of E(spl)m8 single-gene mutants reveals strong functional redundancy among E(spl) paralogs (ronald2025rolesplayedby pages 10-13, ronald2025rolesplayedby pages 4-7).

#### Neuroblast Proliferation Control

E(spl)m8 contributes to regulating the Type I-to-Type 0 proliferation switch in neuroblast lineages (bivik2016controlofneural pages 16-17, bivik2016controlofneural pages 11-13, bivik2016controlofneurala pages 16-17). This developmental transition determines whether neuroblast daughter cells undergo an additional division (Type I) or differentiate immediately (Type 0). Notch signaling activates E(spl)m8 expression in neuroblasts, and stabilized or ectopic M8 can promote premature switching, particularly when combined with temporal factors such as Castor and Hox factor Antennapedia (bivik2016controlofneural pages 11-13, bivik2016controlofneurala pages 11-13).

Chromatin immunoprecipitation (ChIP) and DNA adenine methyltransferase identification (DamID) experiments demonstrate that E(spl)m8 associates with regulatory regions of cell-cycle genes including Cyclin E (CycE), dacapo (dap), and string (stg) (bivik2016controlofneurala pages 16-17, bivik2016controlofneural pages 16-17, bivik2016controlofneural pages 11-13). M8 binding overlaps with Su(H) occupancy at known central nervous system enhancers, particularly at dap regulatory elements (bivik2016controlofneural pages 11-13, bivik2016controlofneurala pages 11-13). Misexpression of M8 reduces Dap and Stg levels and affects CycE expression, supporting direct regulation of cell-cycle progression (bivik2016controlofneural pages 11-13, bivik2016controlofneurala pages 11-13).

E(spl)m8 function in this context is lineage-specific and partially redundant with other E(spl) paralogs (bivik2016controlofneurala pages 16-17, bivik2016controlofneural pages 16-17). Genetic analysis indicates that multiple E(spl)-HLH genes cooperate with Groucho to regulate the proliferation switch (bivik2016controlofneurala pages 19-20, bivik2016controlofneural pages 19-20).

#### Sensory Bristle Patterning

E(spl)m8 participates in sensory organ precursor (SOP) selection and bristle patterning on the adult notum (couturier2019regulationofnotch pages 3-4, bandyopadhyay2016theconservedmapk pages 19-21, bandyopadhyay2016theconservedmapk pages 24-25, couturier2019regulationofnotch pages 6-8). Notch signaling establishes proneural stripes and singles out SOPs through lateral inhibition, with E(spl)-HLH factors mediating transcriptional repression of proneural genes (couturier2019regulationofnotch pages 3-4). Although all seven E(spl) paralogs contribute, recent work (2019) using live imaging revealed temporal dynamics and partial functional specialization (couturier2019regulationofnotch pages 3-4, couturier2019regulationofnotch pages 6-8). Different E(spl) factors show distinct expression patterns, with some (m3, mβ) delimiting early proneural stripes and others (mδ, m7, m8) acting during SOP selection (couturier2019regulationofnotch pages 3-4).

Removal of the entire E(spl)-C causes excessive proneural gene expression, overproduction of SOPs and neurons, and severe bristle loss, demonstrating the complex's essential role in Notch-mediated patterning (couturier2019regulationofnotch pages 3-4). Cross-repression among E(spl) paralogs contributes to regulating Notch output dynamics (couturier2019regulationofnotch pages 3-4).

### Target Gene Regulation

E(spl)m8 represses multiple classes of target genes:

1. **Proneural genes**: Atonal (ato) is the best-characterized direct target, particularly in eye development (bandyopadhyay2016theconservedmapk pages 1-2, bandyopadhyay2016theconservedmapk pages 4-5).

2. **Cell-fate determinants**: phyllopod (phyl) and seven-up (svp) during photoreceptor specification (ronald2025rolesplayedby pages 10-13, ronald2025rolesplayedby pages 19-31, ronald2025rolesplayedby pages 7-10, ronald2025rolesplayedby pages 1-4).

3. **Cell-cycle regulators**: Cyclin E (CycE), dacapo (dap), and string (stg) in neuroblast lineages (bivik2016controlofneural pages 11-13, bivik2016controlofneural pages 16-17, bivik2016controlofneurala pages 16-17).

ChIP and DamID data support direct chromatin association at these loci, although binding profiles can vary between assays and developmental contexts (bivik2016controlofneurala pages 16-17, bivik2016controlofneural pages 16-17, bivik2016controlofneural pages 11-13).

### Functional Redundancy and Evolutionary Conservation

E(spl)m8 functions within a partially redundant seven-member repressor family in the E(spl)-C (couturier2019regulationofnotch pages 3-4, voutyraki2022repressionofdifferentiation pages 3-4). Single-gene mutants often show mild or no phenotype, whereas combinations reveal stronger requirements (ronald2025rolesplayedby pages 10-13, voutyraki2022repressionofdifferentiation pages 3-4, bivik2016controlofneurala pages 19-20). This redundancy likely reflects shared biochemical properties—all seven E(spl) bHLH proteins bind similar DNA sequences, recruit Groucho through WRPW motifs, and respond to Notch signaling (couturier2019regulationofnotch pages 3-4, jennings1999targetspecificitiesof pages 2-4).

The E(spl) complex arose in the common ancestor of insects and crustaceans and has been maintained throughout arthropod evolution, suggesting selective pressure to preserve coordinate regulation and functional dosage (reviewed in recent literature on E(spl) evolution). In mammals, HES proteins serve analogous roles as Notch effectors, demonstrating deep evolutionary conservation of this regulatory logic.

### Recent Developments (2023-2025)

Recent studies continue to reveal new aspects of E(spl)m8 function:

- A 2025 preprint identified E(spl)m8's roles in R7 photoreceptor specification and demonstrated repression of phyllopod and seven-up (ronald2025rolesplayedby pages 10-13, ronald2025rolesplayedby pages 19-31, ronald2025rolesplayedby pages 4-7).

- 2024 work examined Hey gene regulation by paired Notch-responsive enhancers, providing broader context for Notch target gene architecture (relevant for understanding E(spl)m8 regulation).

- 2023 research confirmed CK2 phosphorylation of conserved motifs in E(spl) family members, extending understanding of post-translational control (jozwick2023proteinkinaseck2 pages 4-7, jozwick2023proteinkinaseck2 pages 10-17).

- 2022-2023 studies explored E(spl) function in neural stem cell tumors and differentiation control, revealing roles in maintaining undifferentiated states (voutyraki2022repressionofdifferentiation pages 3-4).

### Summary

E(spl)m8-HLH is a nuclear bHLH-Orange transcriptional repressor that functions as a key downstream effector of Notch signaling in *Drosophila* development. The protein binds E-box/ESE-box DNA sequences (CACGTG core) through its basic region and recruits the Groucho corepressor via its C-terminal WRPW motif to repress transcription. Post-translational regulation through CK2 and MAPK phosphorylation controls the timing and strength of repression by relieving autoinhibition. E(spl)m8 plays essential roles in lateral inhibition during neurogenesis, photoreceptor specification in eye development, neuroblast proliferation control, and sensory organ patterning. Target genes include proneural factors (atonal), cell-fate determinants (phyllopod, seven-up), and cell-cycle regulators (CycE, dap, stg). The protein functions redundantly with six other E(spl) paralogs, collectively mediating Notch-dependent developmental decisions across multiple tissues and developmental stages.

References

1. (pinot2024spatiotemporalregulationof pages 2-4): Mathieu Pinot and Roland Le Borgne. Spatio-temporal regulation of notch activation in asymmetrically dividing sensory organ precursor cells in drosophila melanogaster epithelium. Cells, 13:1133, Jun 2024. URL: https://doi.org/10.3390/cells13131133, doi:10.3390/cells13131133. This article has 3 citations.

2. (couturier2019regulationofnotch pages 3-4): Lydie Couturier, Khalil Mazouni, Francis Corson, and François Schweisguth. Regulation of notch output dynamics via specific e(spl)-hlh factors during bristle patterning in drosophila. Nature Communications, Aug 2019. URL: https://doi.org/10.1038/s41467-019-11477-2, doi:10.1038/s41467-019-11477-2. This article has 34 citations and is from a highest quality peer-reviewed journal.

3. (bahrampour2020thefivefaces pages 51-53): Shahrzad Bahrampour and Stefan Thor. The five faces of notch signalling during drosophila melanogaster embryonic cns development. Advances in experimental medicine and biology, 1218:39-58, Jan 2020. URL: https://doi.org/10.1007/978-3-030-34436-8\_3, doi:10.1007/978-3-030-34436-8\_3. This article has 14 citations and is from a peer-reviewed journal.

4. (jennings2006molecularrecognitionof pages 1-2): Barbara H. Jennings, Laura M. Pickles, S. Mark Wainwright, S. Mark Roe, Laurence H. Pearl, and David Ish-Horowicz. Molecular recognition of transcriptional repressor motifs by the wd domain of the groucho/tle corepressor. Molecular cell, 22 5:645-55, Jun 2006. URL: https://doi.org/10.1016/j.molcel.2006.04.024, doi:10.1016/j.molcel.2006.04.024. This article has 179 citations and is from a highest quality peer-reviewed journal.

5. (fisher1998grouchoproteinstranscriptional pages 2-3): Alfred L. Fisher and Michael Caudy. Groucho proteins: transcriptional corepressors for specific subsets of dna-binding transcription factors in vertebrates and invertebrates. Genes & development, 12 13:1931-40, Jul 1998. URL: https://doi.org/10.1101/gad.12.13.1931, doi:10.1101/gad.12.13.1931. This article has 400 citations and is from a highest quality peer-reviewed journal.

6. (bandyopadhyay2016theconservedmapk pages 1-2): Mohna Bandyopadhyay, Clifton P. Bishop, and Ashok P. Bidwai. The conserved mapk site in e(spl)-m8, an effector of drosophila notch signaling, controls repressor activity during eye development. PLOS ONE, 11:e0159508, Jul 2016. URL: https://doi.org/10.1371/journal.pone.0159508, doi:10.1371/journal.pone.0159508. This article has 13 citations and is from a peer-reviewed journal.

7. (ronald2025rolesplayedby pages 1-4): A. Arias Ronald, E. Mavromatakis Yannis, and Andrew Tomlinson. Roles played by enhancer of split transcription factors in drosophila r7 photoreceptor specification. bioRxiv, Jan 2025. URL: https://doi.org/10.1101/2025.01.30.635716, doi:10.1101/2025.01.30.635716. This article has 0 citations.

8. (bandyopadhyay2016theconservedmapk pages 4-5): Mohna Bandyopadhyay, Clifton P. Bishop, and Ashok P. Bidwai. The conserved mapk site in e(spl)-m8, an effector of drosophila notch signaling, controls repressor activity during eye development. PLOS ONE, 11:e0159508, Jul 2016. URL: https://doi.org/10.1371/journal.pone.0159508, doi:10.1371/journal.pone.0159508. This article has 13 citations and is from a peer-reviewed journal.

9. (oellers1994bhlhproteinsencoded pages 4-5): Nadja Oellers, Michaela Dehio, and Elisabeth Knust. Bhlh proteins encoded by theenhancer of split complex ofdrosophila negatively interfere with transcriptional activation mediated by proneural genes. Molecular and General Genetics MGG, 244:465-473, Sep 1994. URL: https://doi.org/10.1007/bf00583897, doi:10.1007/bf00583897. This article has 168 citations.

10. (oellers1994bhlhproteinsencoded pages 5-6): Nadja Oellers, Michaela Dehio, and Elisabeth Knust. Bhlh proteins encoded by theenhancer of split complex ofdrosophila negatively interfere with transcriptional activation mediated by proneural genes. Molecular and General Genetics MGG, 244:465-473, Sep 1994. URL: https://doi.org/10.1007/bf00583897, doi:10.1007/bf00583897. This article has 168 citations.

11. (oellers1994bhlhproteinsencoded pages 2-3): Nadja Oellers, Michaela Dehio, and Elisabeth Knust. Bhlh proteins encoded by theenhancer of split complex ofdrosophila negatively interfere with transcriptional activation mediated by proneural genes. Molecular and General Genetics MGG, 244:465-473, Sep 1994. URL: https://doi.org/10.1007/bf00583897, doi:10.1007/bf00583897. This article has 168 citations.

12. (jennings1999targetspecificitiesof pages 2-4): Barbara H. Jennings, David M. Tyler, and Sarah J. Bray. Target specificities of drosophilaenhancer of split basic helix-loop-helix proteins. Molecular and Cellular Biology, 19:4600-4610, Jul 1999. URL: https://doi.org/10.1128/mcb.19.7.4600, doi:10.1128/mcb.19.7.4600. This article has 102 citations and is from a domain leading peer-reviewed journal.

13. (jennings1999targetspecificitiesof pages 7-9): Barbara H. Jennings, David M. Tyler, and Sarah J. Bray. Target specificities of drosophilaenhancer of split basic helix-loop-helix proteins. Molecular and Cellular Biology, 19:4600-4610, Jul 1999. URL: https://doi.org/10.1128/mcb.19.7.4600, doi:10.1128/mcb.19.7.4600. This article has 102 citations and is from a domain leading peer-reviewed journal.

14. (jennings1999targetspecificitiesof pages 1-2): Barbara H. Jennings, David M. Tyler, and Sarah J. Bray. Target specificities of drosophilaenhancer of split basic helix-loop-helix proteins. Molecular and Cellular Biology, 19:4600-4610, Jul 1999. URL: https://doi.org/10.1128/mcb.19.7.4600, doi:10.1128/mcb.19.7.4600. This article has 102 citations and is from a domain leading peer-reviewed journal.

15. (jennings1999targetspecificitiesof pages 6-7): Barbara H. Jennings, David M. Tyler, and Sarah J. Bray. Target specificities of drosophilaenhancer of split basic helix-loop-helix proteins. Molecular and Cellular Biology, 19:4600-4610, Jul 1999. URL: https://doi.org/10.1128/mcb.19.7.4600, doi:10.1128/mcb.19.7.4600. This article has 102 citations and is from a domain leading peer-reviewed journal.

16. (fisher1996thewrpwmotif pages 3-4): Alfred L. Fisher, Shunji Ohsako, and Michael Caudy. The wrpw motif of the hairy-related basic helix-loop-helix repressor proteins acts as a 4-amino-acid transcription repression and protein-protein interaction domain. Molecular and Cellular Biology, 16:2670-2677, Jun 1996. URL: https://doi.org/10.1128/mcb.16.6.2670, doi:10.1128/mcb.16.6.2670. This article has 472 citations and is from a domain leading peer-reviewed journal.

17. (fisher1996thewrpwmotif pages 4-5): Alfred L. Fisher, Shunji Ohsako, and Michael Caudy. The wrpw motif of the hairy-related basic helix-loop-helix repressor proteins acts as a 4-amino-acid transcription repression and protein-protein interaction domain. Molecular and Cellular Biology, 16:2670-2677, Jun 1996. URL: https://doi.org/10.1128/mcb.16.6.2670, doi:10.1128/mcb.16.6.2670. This article has 472 citations and is from a domain leading peer-reviewed journal.

18. (fisher1996thewrpwmotif pages 5-6): Alfred L. Fisher, Shunji Ohsako, and Michael Caudy. The wrpw motif of the hairy-related basic helix-loop-helix repressor proteins acts as a 4-amino-acid transcription repression and protein-protein interaction domain. Molecular and Cellular Biology, 16:2670-2677, Jun 1996. URL: https://doi.org/10.1128/mcb.16.6.2670, doi:10.1128/mcb.16.6.2670. This article has 472 citations and is from a domain leading peer-reviewed journal.

19. (jennings2006molecularrecognitionof pages 4-5): Barbara H. Jennings, Laura M. Pickles, S. Mark Wainwright, S. Mark Roe, Laurence H. Pearl, and David Ish-Horowicz. Molecular recognition of transcriptional repressor motifs by the wd domain of the groucho/tle corepressor. Molecular cell, 22 5:645-55, Jun 2006. URL: https://doi.org/10.1016/j.molcel.2006.04.024, doi:10.1016/j.molcel.2006.04.024. This article has 179 citations and is from a highest quality peer-reviewed journal.

20. (jennings2006molecularrecognitionof pages 5-7): Barbara H. Jennings, Laura M. Pickles, S. Mark Wainwright, S. Mark Roe, Laurence H. Pearl, and David Ish-Horowicz. Molecular recognition of transcriptional repressor motifs by the wd domain of the groucho/tle corepressor. Molecular cell, 22 5:645-55, Jun 2006. URL: https://doi.org/10.1016/j.molcel.2006.04.024, doi:10.1016/j.molcel.2006.04.024. This article has 179 citations and is from a highest quality peer-reviewed journal.

21. (jennings2006molecularrecognitionof pages 7-9): Barbara H. Jennings, Laura M. Pickles, S. Mark Wainwright, S. Mark Roe, Laurence H. Pearl, and David Ish-Horowicz. Molecular recognition of transcriptional repressor motifs by the wd domain of the groucho/tle corepressor. Molecular cell, 22 5:645-55, Jun 2006. URL: https://doi.org/10.1016/j.molcel.2006.04.024, doi:10.1016/j.molcel.2006.04.024. This article has 179 citations and is from a highest quality peer-reviewed journal.

22. (bandyopadhyay2016theconservedmapk pages 15-17): Mohna Bandyopadhyay, Clifton P. Bishop, and Ashok P. Bidwai. The conserved mapk site in e(spl)-m8, an effector of drosophila notch signaling, controls repressor activity during eye development. PLOS ONE, 11:e0159508, Jul 2016. URL: https://doi.org/10.1371/journal.pone.0159508, doi:10.1371/journal.pone.0159508. This article has 13 citations and is from a peer-reviewed journal.

23. (bandyopadhyay2016theconservedmapk pages 17-19): Mohna Bandyopadhyay, Clifton P. Bishop, and Ashok P. Bidwai. The conserved mapk site in e(spl)-m8, an effector of drosophila notch signaling, controls repressor activity during eye development. PLOS ONE, 11:e0159508, Jul 2016. URL: https://doi.org/10.1371/journal.pone.0159508, doi:10.1371/journal.pone.0159508. This article has 13 citations and is from a peer-reviewed journal.

24. (bandyopadhyay2016theconservedmapk pages 5-7): Mohna Bandyopadhyay, Clifton P. Bishop, and Ashok P. Bidwai. The conserved mapk site in e(spl)-m8, an effector of drosophila notch signaling, controls repressor activity during eye development. PLOS ONE, 11:e0159508, Jul 2016. URL: https://doi.org/10.1371/journal.pone.0159508, doi:10.1371/journal.pone.0159508. This article has 13 citations and is from a peer-reviewed journal.

25. (bandyopadhyay2016theconservedmapk pages 19-21): Mohna Bandyopadhyay, Clifton P. Bishop, and Ashok P. Bidwai. The conserved mapk site in e(spl)-m8, an effector of drosophila notch signaling, controls repressor activity during eye development. PLOS ONE, 11:e0159508, Jul 2016. URL: https://doi.org/10.1371/journal.pone.0159508, doi:10.1371/journal.pone.0159508. This article has 13 citations and is from a peer-reviewed journal.

26. (jozwick2023proteinkinaseck2 pages 4-7): Lucas M. Jozwick and Ashok P. Bidwai. Protein kinase ck2 phosphorylates a conserved motif in the notch effector e(spl)-mγ. Sep 2023. URL: https://doi.org/10.1007/s11010-022-04539-5, doi:10.1007/s11010-022-04539-5. This article has 0 citations and is from a peer-reviewed journal.

27. (bandyopadhyay2016theconservedmapk pages 24-25): Mohna Bandyopadhyay, Clifton P. Bishop, and Ashok P. Bidwai. The conserved mapk site in e(spl)-m8, an effector of drosophila notch signaling, controls repressor activity during eye development. PLOS ONE, 11:e0159508, Jul 2016. URL: https://doi.org/10.1371/journal.pone.0159508, doi:10.1371/journal.pone.0159508. This article has 13 citations and is from a peer-reviewed journal.

28. (couturier2019regulationofnotch pages 6-8): Lydie Couturier, Khalil Mazouni, Francis Corson, and François Schweisguth. Regulation of notch output dynamics via specific e(spl)-hlh factors during bristle patterning in drosophila. Nature Communications, Aug 2019. URL: https://doi.org/10.1038/s41467-019-11477-2, doi:10.1038/s41467-019-11477-2. This article has 34 citations and is from a highest quality peer-reviewed journal.

29. (bivik2016controlofneural pages 16-17): C Bivik, RB MacDonald, E Gunnar, and K Mazouni. Control of neural daughter cell proliferation by multi-level notch/su (h)/e (spl)-hlh signaling. Unknown journal, 2016.

30. (kuang2021enhancerswithcooperative pages 14-16): Yi Kuang, Anna Pyo, Natanel Eafergan, Brittany Cain, Lisa M. Gutzwiller, Ofri Axelrod, Ellen K. Gagliani, Matthew T. Weirauch, Raphael Kopan, Rhett A. Kovall, David Sprinzak, and Brian Gebelein. Enhancers with cooperative notch binding sites are more resistant to regulation by the hairless co-repressor. PLOS Genetics, 17:e1009039, Sep 2021. URL: https://doi.org/10.1371/journal.pgen.1009039, doi:10.1371/journal.pgen.1009039. This article has 13 citations and is from a domain leading peer-reviewed journal.

31. (kuang2020enhancerarchitecturesensitizes pages 10-11): Yi Kuang, Ohad Golan, Kristina Preusse, Brittany Cain, Collin J Christensen, Joseph Salomone, Ian Campbell, FearGod V Okwubido-Williams, Matthew R Hass, Zhenyu Yuan, Nathanel Eafergan, Kenneth H Moberg, Rhett A Kovall, Raphael Kopan, David Sprinzak, and Brian Gebelein. Enhancer architecture sensitizes cell specific responses to notch gene dose via a bind and discard mechanism. Apr 2020. URL: https://doi.org/10.7554/elife.53659, doi:10.7554/elife.53659. This article has 23 citations and is from a domain leading peer-reviewed journal.

32. (kuang2021enhancerswithcooperative pages 5-7): Yi Kuang, Anna Pyo, Natanel Eafergan, Brittany Cain, Lisa M. Gutzwiller, Ofri Axelrod, Ellen K. Gagliani, Matthew T. Weirauch, Raphael Kopan, Rhett A. Kovall, David Sprinzak, and Brian Gebelein. Enhancers with cooperative notch binding sites are more resistant to regulation by the hairless co-repressor. PLOS Genetics, 17:e1009039, Sep 2021. URL: https://doi.org/10.1371/journal.pgen.1009039, doi:10.1371/journal.pgen.1009039. This article has 13 citations and is from a domain leading peer-reviewed journal.

33. (kuang2021enhancerswithcooperative pages 10-11): Yi Kuang, Anna Pyo, Natanel Eafergan, Brittany Cain, Lisa M. Gutzwiller, Ofri Axelrod, Ellen K. Gagliani, Matthew T. Weirauch, Raphael Kopan, Rhett A. Kovall, David Sprinzak, and Brian Gebelein. Enhancers with cooperative notch binding sites are more resistant to regulation by the hairless co-repressor. PLOS Genetics, 17:e1009039, Sep 2021. URL: https://doi.org/10.1371/journal.pgen.1009039, doi:10.1371/journal.pgen.1009039. This article has 13 citations and is from a domain leading peer-reviewed journal.

34. (kuang2021enhancerswithcooperative pages 13-14): Yi Kuang, Anna Pyo, Natanel Eafergan, Brittany Cain, Lisa M. Gutzwiller, Ofri Axelrod, Ellen K. Gagliani, Matthew T. Weirauch, Raphael Kopan, Rhett A. Kovall, David Sprinzak, and Brian Gebelein. Enhancers with cooperative notch binding sites are more resistant to regulation by the hairless co-repressor. PLOS Genetics, 17:e1009039, Sep 2021. URL: https://doi.org/10.1371/journal.pgen.1009039, doi:10.1371/journal.pgen.1009039. This article has 13 citations and is from a domain leading peer-reviewed journal.

35. (ronald2025rolesplayedby pages 19-31): A. Arias Ronald, E. Mavromatakis Yannis, and Andrew Tomlinson. Roles played by enhancer of split transcription factors in drosophila r7 photoreceptor specification. bioRxiv, Jan 2025. URL: https://doi.org/10.1101/2025.01.30.635716, doi:10.1101/2025.01.30.635716. This article has 0 citations.

36. (ronald2025rolesplayedby pages 4-7): A. Arias Ronald, E. Mavromatakis Yannis, and Andrew Tomlinson. Roles played by enhancer of split transcription factors in drosophila r7 photoreceptor specification. bioRxiv, Jan 2025. URL: https://doi.org/10.1101/2025.01.30.635716, doi:10.1101/2025.01.30.635716. This article has 0 citations.

37. (bivik2016controlofneural pages 11-13): C Bivik, RB MacDonald, E Gunnar, and K Mazouni. Control of neural daughter cell proliferation by multi-level notch/su (h)/e (spl)-hlh signaling. Unknown journal, 2016.

38. (bivik2016controlofneurala pages 16-17): C Bivik, RB MacDonald, E Gunnar, and K Mazouni. Control of neural daughter cell proliferation by multi-level notch/su (h)/e (spl)-hlh signaling. Unknown journal, 2016.

39. (bandyopadhyay2016theconservedmapk pages 23-24): Mohna Bandyopadhyay, Clifton P. Bishop, and Ashok P. Bidwai. The conserved mapk site in e(spl)-m8, an effector of drosophila notch signaling, controls repressor activity during eye development. PLOS ONE, 11:e0159508, Jul 2016. URL: https://doi.org/10.1371/journal.pone.0159508, doi:10.1371/journal.pone.0159508. This article has 13 citations and is from a peer-reviewed journal.

40. (ronald2025rolesplayedby pages 10-13): A. Arias Ronald, E. Mavromatakis Yannis, and Andrew Tomlinson. Roles played by enhancer of split transcription factors in drosophila r7 photoreceptor specification. bioRxiv, Jan 2025. URL: https://doi.org/10.1101/2025.01.30.635716, doi:10.1101/2025.01.30.635716. This article has 0 citations.

41. (ronald2025rolesplayedby pages 7-10): A. Arias Ronald, E. Mavromatakis Yannis, and Andrew Tomlinson. Roles played by enhancer of split transcription factors in drosophila r7 photoreceptor specification. bioRxiv, Jan 2025. URL: https://doi.org/10.1101/2025.01.30.635716, doi:10.1101/2025.01.30.635716. This article has 0 citations.

42. (bivik2016controlofneurala pages 11-13): C Bivik, RB MacDonald, E Gunnar, and K Mazouni. Control of neural daughter cell proliferation by multi-level notch/su (h)/e (spl)-hlh signaling. Unknown journal, 2016.

43. (bivik2016controlofneurala pages 19-20): C Bivik, RB MacDonald, E Gunnar, and K Mazouni. Control of neural daughter cell proliferation by multi-level notch/su (h)/e (spl)-hlh signaling. Unknown journal, 2016.

44. (bivik2016controlofneural pages 19-20): C Bivik, RB MacDonald, E Gunnar, and K Mazouni. Control of neural daughter cell proliferation by multi-level notch/su (h)/e (spl)-hlh signaling. Unknown journal, 2016.

45. (voutyraki2022repressionofdifferentiation pages 3-4): Chrysanthi Voutyraki, Alexandros Choromidis, Vasiliki Theodorou, Christina Efraimoglou, Gerasimos Anagnostopoulos, Srivathsa S. Magadi, Sofia Grammenoudi, Evanthia Zacharioudaki, and Christos Delidakis. Repression of differentiation genes by hes transcription factors fuels neural tumour growth in <i>drosophila</i>. The International Journal of Developmental Biology, 66(1-2-3):211-222, Jan 2022. URL: https://doi.org/10.1387/ijdb.210187cd, doi:10.1387/ijdb.210187cd. This article has 6 citations.

46. (jozwick2023proteinkinaseck2 pages 10-17): Lucas M. Jozwick and Ashok P. Bidwai. Protein kinase ck2 phosphorylates a conserved motif in the notch effector e(spl)-mγ. Sep 2023. URL: https://doi.org/10.1007/s11010-022-04539-5, doi:10.1007/s11010-022-04539-5. This article has 0 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](E-spl-m8-HLH-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](E-spl-m8-HLH-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. pinot2024spatiotemporalregulationof pages 2-4
2. bandyopadhyay2016theconservedmapk pages 4-5
3. bandyopadhyay2016theconservedmapk pages 1-2
4. bandyopadhyay2016theconservedmapk pages 19-21
5. couturier2019regulationofnotch pages 3-4
6. voutyraki2022repressionofdifferentiation pages 3-4
7. bahrampour2020thefivefaces pages 51-53
8. jennings2006molecularrecognitionof pages 1-2
9. fisher1998grouchoproteinstranscriptional pages 2-3
10. ronald2025rolesplayedby pages 1-4
11. oellers1994bhlhproteinsencoded pages 4-5
12. oellers1994bhlhproteinsencoded pages 5-6
13. oellers1994bhlhproteinsencoded pages 2-3
14. jennings1999targetspecificitiesof pages 2-4
15. jennings1999targetspecificitiesof pages 7-9
16. jennings1999targetspecificitiesof pages 1-2
17. jennings1999targetspecificitiesof pages 6-7
18. fisher1996thewrpwmotif pages 3-4
19. fisher1996thewrpwmotif pages 4-5
20. fisher1996thewrpwmotif pages 5-6
21. jennings2006molecularrecognitionof pages 4-5
22. jennings2006molecularrecognitionof pages 5-7
23. jennings2006molecularrecognitionof pages 7-9
24. bandyopadhyay2016theconservedmapk pages 15-17
25. bandyopadhyay2016theconservedmapk pages 17-19
26. bandyopadhyay2016theconservedmapk pages 5-7
27. bandyopadhyay2016theconservedmapk pages 24-25
28. couturier2019regulationofnotch pages 6-8
29. bivik2016controlofneural pages 16-17
30. kuang2021enhancerswithcooperative pages 14-16
31. kuang2020enhancerarchitecturesensitizes pages 10-11
32. kuang2021enhancerswithcooperative pages 5-7
33. kuang2021enhancerswithcooperative pages 10-11
34. kuang2021enhancerswithcooperative pages 13-14
35. ronald2025rolesplayedby pages 19-31
36. ronald2025rolesplayedby pages 4-7
37. bivik2016controlofneural pages 11-13
38. bivik2016controlofneurala pages 16-17
39. bandyopadhyay2016theconservedmapk pages 23-24
40. ronald2025rolesplayedby pages 10-13
41. ronald2025rolesplayedby pages 7-10
42. bivik2016controlofneurala pages 11-13
43. bivik2016controlofneurala pages 19-20
44. bivik2016controlofneural pages 19-20
45. E(spl)-C
46. C/T
47. Su(H), the Drosophila CSL protein
48. DOI
49. https://doi.org/10.1371/journal.pone.0159508
50. https://doi.org/10.1101/2025.01.30.635716
51. https://doi.org/10.1038/s41467-019-11477-2
52. https://doi.org/10.3390/cells13131133,
53. https://doi.org/10.1038/s41467-019-11477-2,
54. https://doi.org/10.1007/978-3-030-34436-8\_3,
55. https://doi.org/10.1016/j.molcel.2006.04.024,
56. https://doi.org/10.1101/gad.12.13.1931,
57. https://doi.org/10.1371/journal.pone.0159508,
58. https://doi.org/10.1101/2025.01.30.635716,
59. https://doi.org/10.1007/bf00583897,
60. https://doi.org/10.1128/mcb.19.7.4600,
61. https://doi.org/10.1128/mcb.16.6.2670,
62. https://doi.org/10.1007/s11010-022-04539-5,
63. https://doi.org/10.1371/journal.pgen.1009039,
64. https://doi.org/10.7554/elife.53659,
65. https://doi.org/10.1387/ijdb.210187cd,