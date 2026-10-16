---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-26T20:24:39.903903'
end_time: '2026-09-26T20:31:54.303990'
duration_seconds: 434.4
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: yeast
  gene_id: CAC2
  gene_symbol: CAC2
  uniprot_accession: Q04199
  protein_description: 'RecName: Full=Chromatin assembly factor 1 subunit B {ECO:0000250|UniProtKB:Q13112};
    Short=CAF-1 subunit B {ECO:0000250|UniProtKB:Q13112}; AltName: Full=CAF-1 60 kDa
    subunit; AltName: Full=Chromatin assembly factor 1 subunit p60;'
  gene_info: Name=CAC2; OrderedLocusNames=YML102W;
  organism_full: Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
  protein_family: Belongs to the WD repeat HIR1 family. .
  protein_domains: Beta-prop_CAF1B_HIR1. (IPR055410); PTHR15271. (IPR045145); WD40/YVTN_repeat-like_dom_sf.
    (IPR015943); WD40_repeat_dom_sf. (IPR036322); WD40_rpt. (IPR001680)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 20
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: CAC2-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** Q04199
- **Protein Description:** RecName: Full=Chromatin assembly factor 1 subunit B {ECO:0000250|UniProtKB:Q13112}; Short=CAF-1 subunit B {ECO:0000250|UniProtKB:Q13112}; AltName: Full=CAF-1 60 kDa subunit; AltName: Full=Chromatin assembly factor 1 subunit p60;
- **Gene Information:** Name=CAC2; OrderedLocusNames=YML102W;
- **Organism (full):** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
- **Protein Family:** Belongs to the WD repeat HIR1 family. .
- **Key Domains:** Beta-prop_CAF1B_HIR1. (IPR055410); PTHR15271. (IPR045145); WD40/YVTN_repeat-like_dom_sf. (IPR015943); WD40_repeat_dom_sf. (IPR036322); WD40_rpt. (IPR001680)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "CAC2" matches the protein description above**
2. **Verify the organism is correct:** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'CAC2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **CAC2** (gene ID: CAC2, UniProt: Q04199) in yeast.

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
- **UniProt Accession:** Q04199
- **Protein Description:** RecName: Full=Chromatin assembly factor 1 subunit B {ECO:0000250|UniProtKB:Q13112}; Short=CAF-1 subunit B {ECO:0000250|UniProtKB:Q13112}; AltName: Full=CAF-1 60 kDa subunit; AltName: Full=Chromatin assembly factor 1 subunit p60;
- **Gene Information:** Name=CAC2; OrderedLocusNames=YML102W;
- **Organism (full):** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
- **Protein Family:** Belongs to the WD repeat HIR1 family. .
- **Key Domains:** Beta-prop_CAF1B_HIR1. (IPR055410); PTHR15271. (IPR045145); WD40/YVTN_repeat-like_dom_sf. (IPR015943); WD40_repeat_dom_sf. (IPR036322); WD40_rpt. (IPR001680)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "CAC2" matches the protein description above**
2. **Verify the organism is correct:** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'CAC2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **CAC2** (gene ID: CAC2, UniProt: Q04199) in yeast.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Research report: *Saccharomyces cerevisiae* **CAC2** (YML102W; UniProt Q04199)

## Executive conclusion

The identity is verified: **CAC2/YML102W in *Saccharomyces cerevisiae* S288c encodes Cac2, the conserved middle/p60-like subunit of chromatin assembly factor 1 (CAF-1)**. It is not an enzyme or transporter. Its primary molecular role is to act as a WD-repeat-containing structural and histone-chaperone subunit that enables CAF-1 to bind H3–H4 productively and deposit H3–H4 onto newly synthesized DNA. This supports replication- and repair-coupled nucleosome assembly, genome stability, and maintenance of repressive chromatin states. Cac2 acts principally as part of the nuclear Cac1–Cac2–Cac3 CAF-1 complex; isolated Cac2 has little histone-binding activity, whereas its incorporation into CAF-1 creates a high-affinity, assembly-competent histone-binding interface. (mattiroli2017thecac2subunit pages 1-2, mattiroli2017thecac2subunit pages 2-3, mattiroli2017thecac2subunit pages 5-6)

## 1. Mandatory identity verification

Kaufman, Kobayashi, and Stillman explicitly identified **CAC2 as chromosome XIII ORF YML102W encoding the yeast CAF-1 p60 subunit**. Later literature consistently identifies Cac2 as the middle subunit of the heterotrimeric budding-yeast CAF-1 complex, alongside large subunit Cac1 and small subunit Cac3; its human orthologous counterpart is CHAF1B/p60. Thus, the supplied gene symbol, locus, organism, and protein description are mutually consistent. [Kaufman et al., February 1997, DOI](https://doi.org/10.1101/gad.11.3.345); [Mattiroli et al., April 2017, DOI](https://doi.org/10.1038/srep46274). (kaufman1997ultravioletradiationsensitivity pages 5-6, mattiroli2017thecac2subunit pages 1-2, hall2026caf1inreplication pages 5-7)

Cac2 contains multiple WD40 repeats and a conserved C-terminal B-domain associated with ASF1 binding. The predicted WD40 fold agrees with the supplied InterPro annotations—WD40 repeat/superfamily and Beta-prop_CAF1B_HIR1—and with assignment to the WD-repeat HIR1 family. The literature therefore supports, rather than contradicts, the UniProt Q04199 domain annotation. The detailed isolated Cac2 structure has not been established to the same resolution as its biochemical role, so the beta-propeller assignment remains substantially sequence- and homology-supported. (nair2021regulationofreplication pages 35-40, mattiroli2017thecac2subunit pages 2-3)

| Topic | Best-supported finding | Evidence type / quantitative detail | Attribution level | Source with year and DOI URL |
|---|---|---|---|---|
| Target identity | *S. cerevisiae* **CAC2** is chromosome XIII ORF **YML102W** and encodes the yeast CAF-1 p60 subunit, matching UniProt Q04199. | Locus identification, sequence comparison, and targeted gene disruption. | **Direct Cac2** | Kaufman et al. (1997), [10.1101/gad.11.3.345](https://doi.org/10.1101/gad.11.3.345) (kaufman1997ultravioletradiationsensitivity pages 5-6) |
| Domain architecture | Cac2 is a WD-repeat protein with a predicted WD40 fold and a conserved C-terminal **B domain** that binds the histone chaperone Asf1. This agrees with the supplied WD-repeat/HIR1-family annotation. | Comparative sequence/domain analysis; the detailed fold was predicted rather than experimentally solved for isolated Cac2. | **Direct Cac2**, partly evolutionary/bioinformatic inference | Nair (2021) (nair2021regulationofreplication pages 35-40); Mattiroli et al. (2017), [10.1038/srep46274](https://doi.org/10.1038/srep46274) (mattiroli2017thecac2subunit pages 2-3) |
| CAF-1 composition | Budding-yeast CAF-1 is a heterotrimer of Cac1, Cac2, and Cac3; Cac1 organizes the complex and bridges Cac2 and Cac3, which do not directly interact. | Recombinant complex analysis demonstrated **1:1:1 stoichiometry**. | **Direct complex placement of Cac2** | Mattiroli et al. (2017), [10.1038/srep46274](https://doi.org/10.1038/srep46274) (mattiroli2017thecac2subunit pages 1-2, mattiroli2017thecac2subunit pages 6-8) |
| H3–H4 recognition | Cac2 contributes to a composite histone-binding surface formed with the acidic and Cac2-binding regions of Cac1; isolated Cac2 binds H3–H4 only very weakly or not detectably. | Isolated Cac2: **Kd >1 μM**; full-length CAF-1: **Kd ≈0.3 nM**; truncated active CAF-1: **Kd ≈0.5 nM**; minimal Cac1–Cac2 module: **Kd ≈2 nM**. | **Direct Cac2 requirement within CAF-1**; high-affinity values describe complexes, not isolated Cac2 | Mattiroli et al. (2017), [10.1038/srep46274](https://doi.org/10.1038/srep46274) (mattiroli2017thecac2subunit pages 2-3, mattiroli2017thecac2subunit pages 5-6) |
| Nucleosome assembly | Cac2 is indispensable for productive histone engagement and H3–H4 deposition: removing Cac2 permits residual, nonproductive histone association but abolishes detectable tetrasome and nucleosome assembly. | Hydrogen–deuterium exchange MS plus tetrasome and nucleosome-assembly assays; **no detectable assembly** by the Cac2-deficient complex. | **Direct Cac2 requirement within reconstituted CAF-1** | Mattiroli et al. (2017), [10.1038/srep46274](https://doi.org/10.1038/srep46274) (mattiroli2017thecac2subunit pages 6-8, mattiroli2017thecac2subunit pages 5-6) |
| UV resistance and telomeric silencing | **cac2Δ**, like deletion of either other CAF-1 subunit, causes UV hypersensitivity and reduced telomeric silencing without a normal-growth defect; combined CAF-1 mutations were not additive. | Individual null-mutant genetics; telomere-adjacent **URA3/5-FOA** assay. Rare fully grown 5-FOA-resistant colonies occurred at about **1 in 10⁴**, with most resistant colonies being microcolonies; no increased γ-irradiation sensitivity was observed. | **Direct cac2Δ phenotype**, interpreted as loss of the CAF-1 complex | Kaufman et al. (1997), [10.1101/gad.11.3.345](https://doi.org/10.1101/gad.11.3.345) (kaufman1997ultravioletradiationsensitivity pages 6-7) |
| Meiotic DSB localization | Epitope-tagged Cac2 is recruited to engineered VDE breaks and Spo11-dependent meiotic DSB hotspots, including in **dmc1Δ** cells; recruitment therefore precedes or does not require strand invasion. | ChIP during meiotic time courses; recruitment at DSB loci versus negative-control loci. **cac2Δ** caused only a slight meiotic delay and retained wild-type spore viability and crossover behavior. | **Direct Cac2 localization and mutant evidence** | Brachet et al. (2015), [10.1371/journal.pone.0125965](https://doi.org/10.1371/journal.pone.0125965) (brachet2015thecaf1and pages 5-8, brachet2015thecaf1and pages 10-11) |
| 2023 genome-stability development | Deleting **CAC2** strongly aggravates growth of **ctf4Δ** cells, supporting a need for intact CAF-1-mediated chromatin assembly when replisome coupling is impaired; the cac3Δ interaction was less severe than cac1Δ or cac2Δ. | Comparative genetic interaction/growth assays. | **Direct cac2Δ genetic interaction** | Ghaddar et al. (2023), [10.15698/cst2023.09.289](https://doi.org/10.15698/cst2023.09.289) (ghaddar2023chromatinassemblyfactor1 pages 4-6) |
| 2023 cohesion mechanism—attribution caveat | CAF-1 was proposed to promote sister-chromatid cohesion, cohesin function, Eco1-dependent Smc3 acetylation, and genome stability in **ctf4Δ** cells. However, the detailed cohesion, Scc1 occupancy, DNA-damage-focus, checkpoint, and Smc3-acetylation experiments chiefly used **cac1Δ**, so they should not be reported as Cac2-specific mechanisms. | Cohesion assays counted **>100 cells across five experiments**; Smc3-acetylation quantification used **six experiments**. Loss of CAC1 increased chromatin-associated Scc1 yet worsened cohesion in ctf4Δ cells. | **CAF-1-level conclusion based mainly on Cac1 proxy; not direct Cac2 evidence** | Ghaddar et al. (2023), [10.15698/cst2023.09.289](https://doi.org/10.15698/cst2023.09.289) (ghaddar2023chromatinassemblyfactor1 pages 10-12, ghaddar2023chromatinassemblyfactor1 pages 12-13, ghaddar2023chromatinassemblyfactor1 pages 9-10) |


*Table: Compact evidence map for the verified budding-yeast CAC2/YML102W protein, separating direct Cac2 results from whole-CAF-1 and Cac1-proxy evidence. Quantitative biochemical and genetic findings are included with attribution caveats.*

## 2. Primary molecular function

### 2.1 A non-catalytic histone-chaperone component

Cac2 does not catalyze a chemical reaction. CAF-1 is a histone chaperone: it binds H3–H4, shields these basic histones from inappropriate interactions, and deposits them on DNA during chromatin restoration. Recombinant yeast CAF-1 contains Cac1, Cac2, and Cac3 in **1:1:1 stoichiometry**. Cac1 provides the main scaffold and independently binds Cac2 and Cac3; Cac2 and Cac3 do not substantially contact one another. (mattiroli2017thecac2subunit pages 1-2, mattiroli2017thecac2subunit pages 6-8)

Cac2’s decisive role is to convert histone association into a productive deposition intermediate. Isolated Cac2 binds H3–H4 only very weakly, with a reported **Kd greater than 1 μM**, whereas full-length CAF-1 binds at approximately **0.3 nM** and an active truncated CAF-1 complex at approximately **0.5 nM**. A minimal composite module containing Cac2 and the relevant Cac1 regions binds at approximately **2 nM**. These differences show that Cac2 is not an autonomous high-affinity histone receptor; it helps construct a composite interface with the acidic and Cac2-binding regions of Cac1. (mattiroli2017thecac2subunit pages 2-3, mattiroli2017thecac2subunit pages 5-6)

Hydrogen–deuterium exchange mass spectrometry and reconstituted assembly assays provide the strongest direct functional evidence. Removing Cac2 altered the histone protection pattern, particularly around the H3 α3 region involved in H3–H4 tetramerization. Although some residual histone association remained, the Cac2-deficient complex produced **no detectable tetrasome or nucleosome assembly**. Cac2 is therefore indispensable for productive H3–H4 configuration and deposition, rather than merely increasing binding affinity. Whether Cac2 directly contacts every relevant histone surface or allosterically organizes Cac1 remains incompletely resolved. [Mattiroli et al., April 2017, DOI](https://doi.org/10.1038/srep46274). (mattiroli2017thecac2subunit pages 6-8, mattiroli2017thecac2subunit pages 5-6)

### 2.2 Substrate specificity and deposition mechanism

The relevant molecular cargo is newly synthesized **histone H3–H4**, normally handled as H3–H4 dimers before assembly of an (H3–H4)₂ tetramer on DNA. At the whole-complex level, yeast CAF-1 binds one H3–H4 dimer in solution; two histone-loaded CAF-1 complexes can associate on sufficiently long DNA and promote tetramer deposition. Cac2 enables the productive histone-binding state, while major PCNA- and DNA-binding elements reside predominantly in Cac1. Accordingly, recruitment through PCNA or DNA should not be misassigned as an intrinsic Cac2 activity. (mattiroli2017thecac2subunit pages 6-8, hall2026caf1inreplication pages 3-5, hall2026caf1inreplication pages 5-7)

Cac2’s conserved B-domain also provides a mechanistic link to ASF1, the upstream H3–H4 chaperone. The accepted model is that ASF1 carries an H3–H4 dimer and transfers it to CAF-1 through an interaction involving the CAF-1 middle subunit. This places Cac2 at the histone-supply interface as well as within the final deposition machinery. Direct transfer kinetics for isolated budding-yeast Cac2 remain less well defined than the complete CAF-1 assembly reaction. (mattiroli2017thecac2subunit pages 1-2, nair2021regulationofreplication pages 35-40)

## 3. Cellular localization

Cac2 functions in the **nucleus**, at chromatin undergoing DNA synthesis or repair. This conclusion follows from its obligatory role in CAF-1 and from direct chromatin immunoprecipitation of tagged Cac2 at meiotic DNA double-strand breaks. Cac2-3HA was recruited to an engineered VDE break and to Spo11-dependent hotspots, including GAT1. Recruitment persisted in **dmc1Δ** cells, which fail in strand invasion and accumulate resected breaks, indicating that Cac2/CAF-1 reaches damage sites before, or independently of, successful strand invasion. [Brachet et al., May 2015, DOI](https://doi.org/10.1371/journal.pone.0125965). (brachet2015thecaf1and pages 5-8, brachet2015thecaf1and pages 10-11)

This meiotic recruitment was not equivalent to an indispensable recombination function. Deleting CAC2 caused only a slight meiotic delay, with wild-type spore viability and essentially normal crossover outcomes in the assays reported. The best interpretation is that CAF-1 is mobilized to damaged chromatin and may assist restoration, but redundant histone-assembly pathways can preserve meiotic recombination outcomes. (brachet2015thecaf1and pages 5-8, brachet2015thecaf1and pages 11-13)

## 4. Biological processes and pathways

### Replication-coupled chromatin assembly

CAF-1 restores chromatin behind replication forks by depositing new H3–H4 on nascent DNA. Cac2 is essential to the productive histone-binding/deposition step, whereas Cac1 supplies principal PCNA- and DNA-binding functions. CAC2 deletion is viable under standard laboratory conditions, showing that alternative histone chaperones can support basal proliferation, but deletion compromises chromatin-state inheritance and stress resistance. (mattiroli2017thecac2subunit pages 1-2, mattiroli2017thecac2subunit pages 2-3, kaufman1997ultravioletradiationsensitivity pages 6-7)

### DNA-repair-coupled chromatin restoration

CAF-1 is coupled to synthesis-dependent DNA repair through PCNA and reassembles nucleosomes after repair synthesis. Direct Cac2 recruitment to meiotic DSBs supports a repair-site role, while classical genetics showed that **cac2Δ**, like loss of the other CAF-1 subunits, causes UV hypersensitivity. The mutants were not comparably hypersensitive to γ irradiation in the original assay, indicating damage-context specificity rather than a universal inability to repair all DNA lesions. (kaufman1997ultravioletradiationsensitivity pages 6-7, brachet2015thecaf1and pages 5-8)

### Transcriptional silencing and epigenetic maintenance

Individual CAC1, CAC2, and MSI1/CAC3 null mutations reduced silencing of a telomere-adjacent URA3 reporter. Rare fully grown 5-FOA-resistant colonies occurred at approximately **1 in 10⁴**, while most resistant mutant colonies were microcolonies. Combining CAF-1 mutations did not produce additive UV or silencing defects, supporting the interpretation that Cac2 acts through the shared complex. The original study did not find equally dramatic derepression at HML/HMR, and subsequent work indicates that CAF-1 contributes more to maintenance than de novo establishment of some silent states. [Kaufman et al., February 1997, DOI](https://doi.org/10.1101/gad.11.3.345). (kaufman1997ultravioletradiationsensitivity pages 6-7)

### Sister-chromatid cohesion and replication-fork robustness

A 2023 study found strong synthetic sickness between **cac2Δ and ctf4Δ**; cac3Δ ctf4Δ was less severe than cac2Δ ctf4Δ or cac1Δ ctf4Δ. This directly shows that Cac2-containing CAF-1 becomes particularly important when Ctf4-dependent replisome organization is impaired. [Ghaddar et al., September 2023, DOI](https://doi.org/10.15698/cst2023.09.289). (ghaddar2023chromatinassemblyfactor1 pages 4-6)

The same study proposed that CAF-1-generated chromatin promotes sister-chromatid cohesion and genome stability. However, the detailed cohesion, Scc1 occupancy, DNA-damage-focus, checkpoint, and Smc3-acetylation experiments primarily used **cac1Δ**, not cac2Δ. Those experiments included cohesion scoring of more than 100 cells across five experiments and Smc3-acetylation measurements across six experiments. They support a CAF-1-level model but do not prove that Cac2 has an independent cohesion activity. (ghaddar2023chromatinassemblyfactor1 pages 10-12, ghaddar2023chromatinassemblyfactor1 pages 12-13, ghaddar2023chromatinassemblyfactor1 pages 9-10)

## 5. Recent developments, 2023–2024

The most relevant direct 2023 advance is the CAC2–CTF4 genetic interaction described above. It extends the annotation from general chromatin assembly to a defined condition in which CAF-1-dependent deposition is needed for replisome robustness and indirectly for cohesion. The rigorous conclusion is that Cac2 is required as part of intact CAF-1; the available evidence does not establish a separate Cac2–cohesin interaction. (ghaddar2023chromatinassemblyfactor1 pages 10-12, ghaddar2023chromatinassemblyfactor1 pages 4-6)

A 2024 structural/biophysical study of CAF-1 from *Schizosaccharomyces pombe* showed how disordered acidic regions and folded modules cooperate in histone deposition and PCNA-associated synthesis-coupled assembly. This supports evolutionary conservation of CAF-1’s modular architecture, but it studies fission yeast and must not be treated as direct evidence about Q04199 from budding yeast. Likewise, 2024 work on the structurally related HIR chaperone informs the broader WD-repeat histone-chaperone family but does not alter the direct CAC2 annotation.

Overall, relatively little 2023–2024 work isolates budding-yeast Cac2 biochemically. The mechanistic foundation still rests on the 2015 localization and 2017 reconstitution studies, supplemented by the 2023 genetic analysis. This is a meaningful limitation rather than evidence that the established annotation is obsolete.

## 6. Current applications and real-world relevance

Cac2 currently has no clinical or industrial application comparable to a drug target, enzyme, or engineered transporter. Its practical importance is as an **experimental model component** for:

1. reconstituting replication-coupled nucleosome assembly;
2. testing histone handoff from ASF1 to CAF-1;
3. dissecting PCNA-coupled chromatin restoration after replication or repair;
4. measuring epigenetic silencing with telomeric reporter systems;
5. probing replication stress and synthetic genetic interactions such as **cac2Δ ctf4Δ**; and
6. distinguishing chromatin restoration from DNA recombination itself at programmed meiotic DSBs.

Because CAF-1 and the p60/CHAF1B subunit are conserved, yeast Cac2 supplies a tractable mechanistic framework for understanding replication-coupled chromatin assembly in higher eukaryotes. Cross-species translation should nevertheless be made at the level of conserved CAF-1 principles, not by assuming that every mammalian CHAF1B phenotype occurs in budding yeast.

## 7. Evidence-weighted functional annotation

**Recommended primary annotation:** Cac2 is the WD-repeat middle subunit of nuclear CAF-1. In complex with Cac1, it creates a productive H3–H4-binding interface required to deposit newly synthesized H3–H4 onto nascent or repaired DNA and thereby restore nucleosomes.

**Secondary processes supported experimentally:** replication-coupled chromatin assembly, repair-associated chromatin restoration, UV-damage resistance, telomeric silencing, recruitment to meiotic DSBs, and maintenance of genome stability when Ctf4-dependent replication functions are compromised. (mattiroli2017thecac2subunit pages 5-6, kaufman1997ultravioletradiationsensitivity pages 6-7, brachet2015thecaf1and pages 5-8, ghaddar2023chromatinassemblyfactor1 pages 4-6)

**Important boundaries:** Cac2 is not itself a catalytic enzyme; PCNA recognition and major DNA-binding activities are largely properties of Cac1; isolated Cac2 is not an efficient histone chaperone; and recent cohesion mechanisms are supported mainly by Cac1 perturbation and should be assigned to CAF-1 rather than uniquely to Cac2. (mattiroli2017thecac2subunit pages 2-3, hall2026caf1inreplication pages 3-5, ghaddar2023chromatinassemblyfactor1 pages 10-12)

## Key references

- Kaufman P, Kobayashi R, Stillman B. “Ultraviolet radiation sensitivity and reduction of telomeric silencing in *Saccharomyces cerevisiae* cells lacking chromatin assembly factor-I.” *Genes & Development*. Published February 1997. https://doi.org/10.1101/gad.11.3.345 (kaufman1997ultravioletradiationsensitivity pages 6-7, kaufman1997ultravioletradiationsensitivity pages 5-6)
- Brachet E, Béneut C, Serrentino M-E, Borde V. “The CAF-1 and Hir Histone Chaperones Associate with Sites of Meiotic Double-Strand Breaks in Budding Yeast.” *PLoS ONE*. Published May 2015. https://doi.org/10.1371/journal.pone.0125965 (brachet2015thecaf1and pages 5-8, brachet2015thecaf1and pages 10-11)
- Mattiroli F, Gu Y, Balsbaugh JL, Ahn NG, Luger K. “The Cac2 subunit is essential for productive histone binding and nucleosome assembly in CAF-1.” *Scientific Reports*. Published April 2017. https://doi.org/10.1038/srep46274 (mattiroli2017thecac2subunit pages 1-2, mattiroli2017thecac2subunit pages 2-3, mattiroli2017thecac2subunit pages 5-6)
- Ghaddar N, Luciano P, Géli V, Corda Y. “Chromatin assembly factor-1 preserves genome stability in ctf4∆ cells by promoting sister chromatid cohesion.” *Cell Stress*. Published September 2023. https://doi.org/10.15698/cst2023.09.289 (ghaddar2023chromatinassemblyfactor1 pages 10-12, ghaddar2023chromatinassemblyfactor1 pages 4-6)

References

1. (mattiroli2017thecac2subunit pages 1-2): Francesca Mattiroli, Yajie Gu, Jeremy L. Balsbaugh, Natalie G. Ahn, and Karolin Luger. The cac2 subunit is essential for productive histone binding and nucleosome assembly in caf-1. Scientific Reports, Apr 2017. URL: https://doi.org/10.1038/srep46274, doi:10.1038/srep46274. This article has 34 citations and is from a peer-reviewed journal.

2. (mattiroli2017thecac2subunit pages 2-3): Francesca Mattiroli, Yajie Gu, Jeremy L. Balsbaugh, Natalie G. Ahn, and Karolin Luger. The cac2 subunit is essential for productive histone binding and nucleosome assembly in caf-1. Scientific Reports, Apr 2017. URL: https://doi.org/10.1038/srep46274, doi:10.1038/srep46274. This article has 34 citations and is from a peer-reviewed journal.

3. (mattiroli2017thecac2subunit pages 5-6): Francesca Mattiroli, Yajie Gu, Jeremy L. Balsbaugh, Natalie G. Ahn, and Karolin Luger. The cac2 subunit is essential for productive histone binding and nucleosome assembly in caf-1. Scientific Reports, Apr 2017. URL: https://doi.org/10.1038/srep46274, doi:10.1038/srep46274. This article has 34 citations and is from a peer-reviewed journal.

4. (kaufman1997ultravioletradiationsensitivity pages 5-6): P. Kaufman, R. Kobayashi, and B. Stillman. Ultraviolet radiation sensitivity and reduction of telomeric silencing in saccharomyces cerevisiae cells lacking chromatin assembly factor-i. Genes & development, 11 3:345-57, Feb 1997. URL: https://doi.org/10.1101/gad.11.3.345, doi:10.1101/gad.11.3.345. This article has 473 citations and is from a highest quality peer-reviewed journal.

5. (hall2026caf1inreplication pages 5-7): Ian P. Hall, Carly A. Nowoj, and Lynne M. Dieckman. Caf-1 in replication and repair: a critical genetic mediator of synthesis-coupled nucleosome assembly. Sep 2026. URL: https://doi.org/10.3390/biom16091277, doi:10.3390/biom16091277. This article has 0 citations.

6. (nair2021regulationofreplication pages 35-40): A Gopinathan Nair. Regulation of replication dependent nucleosome assembly. Unknown journal, 2021.

7. (mattiroli2017thecac2subunit pages 6-8): Francesca Mattiroli, Yajie Gu, Jeremy L. Balsbaugh, Natalie G. Ahn, and Karolin Luger. The cac2 subunit is essential for productive histone binding and nucleosome assembly in caf-1. Scientific Reports, Apr 2017. URL: https://doi.org/10.1038/srep46274, doi:10.1038/srep46274. This article has 34 citations and is from a peer-reviewed journal.

8. (kaufman1997ultravioletradiationsensitivity pages 6-7): P. Kaufman, R. Kobayashi, and B. Stillman. Ultraviolet radiation sensitivity and reduction of telomeric silencing in saccharomyces cerevisiae cells lacking chromatin assembly factor-i. Genes & development, 11 3:345-57, Feb 1997. URL: https://doi.org/10.1101/gad.11.3.345, doi:10.1101/gad.11.3.345. This article has 473 citations and is from a highest quality peer-reviewed journal.

9. (brachet2015thecaf1and pages 5-8): Elsa Brachet, Claire Béneut, Maria-Elisabetta Serrentino, and Valérie Borde. The caf-1 and hir histone chaperones associate with sites of meiotic double-strand breaks in budding yeast. PLoS ONE, 10:e0125965, May 2015. URL: https://doi.org/10.1371/journal.pone.0125965, doi:10.1371/journal.pone.0125965. This article has 16 citations and is from a peer-reviewed journal.

10. (brachet2015thecaf1and pages 10-11): Elsa Brachet, Claire Béneut, Maria-Elisabetta Serrentino, and Valérie Borde. The caf-1 and hir histone chaperones associate with sites of meiotic double-strand breaks in budding yeast. PLoS ONE, 10:e0125965, May 2015. URL: https://doi.org/10.1371/journal.pone.0125965, doi:10.1371/journal.pone.0125965. This article has 16 citations and is from a peer-reviewed journal.

11. (ghaddar2023chromatinassemblyfactor1 pages 4-6): Nagham Ghaddar, Pierre Luciano, Vincent Géli, and Yves Corda. Chromatin assembly factor-1 preserves genome stability in ctf4∆ cells by promoting sister chromatid cohesion. Cell Stress, 7:69-89, Sep 2023. URL: https://doi.org/10.15698/cst2023.09.289, doi:10.15698/cst2023.09.289. This article has 5 citations.

12. (ghaddar2023chromatinassemblyfactor1 pages 10-12): Nagham Ghaddar, Pierre Luciano, Vincent Géli, and Yves Corda. Chromatin assembly factor-1 preserves genome stability in ctf4∆ cells by promoting sister chromatid cohesion. Cell Stress, 7:69-89, Sep 2023. URL: https://doi.org/10.15698/cst2023.09.289, doi:10.15698/cst2023.09.289. This article has 5 citations.

13. (ghaddar2023chromatinassemblyfactor1 pages 12-13): Nagham Ghaddar, Pierre Luciano, Vincent Géli, and Yves Corda. Chromatin assembly factor-1 preserves genome stability in ctf4∆ cells by promoting sister chromatid cohesion. Cell Stress, 7:69-89, Sep 2023. URL: https://doi.org/10.15698/cst2023.09.289, doi:10.15698/cst2023.09.289. This article has 5 citations.

14. (ghaddar2023chromatinassemblyfactor1 pages 9-10): Nagham Ghaddar, Pierre Luciano, Vincent Géli, and Yves Corda. Chromatin assembly factor-1 preserves genome stability in ctf4∆ cells by promoting sister chromatid cohesion. Cell Stress, 7:69-89, Sep 2023. URL: https://doi.org/10.15698/cst2023.09.289, doi:10.15698/cst2023.09.289. This article has 5 citations.

15. (hall2026caf1inreplication pages 3-5): Ian P. Hall, Carly A. Nowoj, and Lynne M. Dieckman. Caf-1 in replication and repair: a critical genetic mediator of synthesis-coupled nucleosome assembly. Sep 2026. URL: https://doi.org/10.3390/biom16091277, doi:10.3390/biom16091277. This article has 0 citations.

16. (brachet2015thecaf1and pages 11-13): Elsa Brachet, Claire Béneut, Maria-Elisabetta Serrentino, and Valérie Borde. The caf-1 and hir histone chaperones associate with sites of meiotic double-strand breaks in budding yeast. PLoS ONE, 10:e0125965, May 2015. URL: https://doi.org/10.1371/journal.pone.0125965, doi:10.1371/journal.pone.0125965. This article has 16 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](CAC2-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. kaufman1997ultravioletradiationsensitivity pages 5-6
2. nair2021regulationofreplication pages 35-40
3. kaufman1997ultravioletradiationsensitivity pages 6-7
4. Kaufman et al., February 1997, DOI
5. Mattiroli et al., April 2017, DOI
6. 10.1101/gad.11.3.345
7. 10.1038/srep46274
8. 10.1371/journal.pone.0125965
9. 10.15698/cst2023.09.289
10. Brachet et al., May 2015, DOI
11. Ghaddar et al., September 2023, DOI
12. https://doi.org/10.1101/gad.11.3.345
13. https://doi.org/10.1038/srep46274
14. https://doi.org/10.1371/journal.pone.0125965
15. https://doi.org/10.15698/cst2023.09.289
16. https://doi.org/10.1038/srep46274,
17. https://doi.org/10.1101/gad.11.3.345,
18. https://doi.org/10.3390/biom16091277,
19. https://doi.org/10.1371/journal.pone.0125965,
20. https://doi.org/10.15698/cst2023.09.289,