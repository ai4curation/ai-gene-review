---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-05T02:00:46.974404'
end_time: '2026-07-05T02:22:15.667775'
duration_seconds: 1288.69
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: yeast
  gene_id: GPM3
  gene_symbol: GPM3
  uniprot_accession: Q12326
  protein_description: 'RecName: Full=Phosphoglycerate mutase 3; Short=PGAM 3; EC=5.4.2.11;
    AltName: Full=BPG-dependent PGAM 3; AltName: Full=MPGM 3; AltName: Full=Phosphoglyceromutase
    3;'
  gene_info: Name=GPM3; OrderedLocusNames=YOL056W; ORFNames=O1236;
  organism_full: Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
  protein_family: Belongs to the phosphoglycerate mutase family. BPG-
  protein_domains: His_Pase_superF_clade-1. (IPR013078); His_PPase_superfam. (IPR029033);
    PG/BPGM_mutase_AS. (IPR001345); Phosphogly_mut1. (IPR005952); His_Phos_1 (PF00300)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 21
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: GPM3-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: GPM3-deep-research-falcon_artifacts/artifact-01.md
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
- **UniProt Accession:** Q12326
- **Protein Description:** RecName: Full=Phosphoglycerate mutase 3; Short=PGAM 3; EC=5.4.2.11; AltName: Full=BPG-dependent PGAM 3; AltName: Full=MPGM 3; AltName: Full=Phosphoglyceromutase 3;
- **Gene Information:** Name=GPM3; OrderedLocusNames=YOL056W; ORFNames=O1236;
- **Organism (full):** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
- **Protein Family:** Belongs to the phosphoglycerate mutase family. BPG-
- **Key Domains:** His_Pase_superF_clade-1. (IPR013078); His_PPase_superfam. (IPR029033); PG/BPGM_mutase_AS. (IPR001345); Phosphogly_mut1. (IPR005952); His_Phos_1 (PF00300)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "GPM3" matches the protein description above**
2. **Verify the organism is correct:** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'GPM3' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **GPM3** (gene ID: GPM3, UniProt: Q12326) in yeast.

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
- **UniProt Accession:** Q12326
- **Protein Description:** RecName: Full=Phosphoglycerate mutase 3; Short=PGAM 3; EC=5.4.2.11; AltName: Full=BPG-dependent PGAM 3; AltName: Full=MPGM 3; AltName: Full=Phosphoglyceromutase 3;
- **Gene Information:** Name=GPM3; OrderedLocusNames=YOL056W; ORFNames=O1236;
- **Organism (full):** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
- **Protein Family:** Belongs to the phosphoglycerate mutase family. BPG-
- **Key Domains:** His_Pase_superF_clade-1. (IPR013078); His_PPase_superfam. (IPR029033); PG/BPGM_mutase_AS. (IPR001345); Phosphogly_mut1. (IPR005952); His_Phos_1 (PF00300)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "GPM3" matches the protein description above**
2. **Verify the organism is correct:** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'GPM3' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **GPM3** (gene ID: GPM3, UniProt: Q12326) in yeast.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Comprehensive Research Report: GPM3 (YOL056W) — Phosphoglycerate Mutase 3 in *Saccharomyces cerevisiae*

## 1. Gene and Protein Identity

GPM3 (systematic name YOL056W; UniProt Q12326) is located on the left arm of chromosome XV in *Saccharomyces cerevisiae* (strain ATCC 204508 / S288c). It encodes Phosphoglycerate Mutase 3 (PGAM 3), a member of the 2,3-bisphosphoglycerate (BPG)-dependent phosphoglycerate mutase family (EC 5.4.2.11). The protein belongs to the histidine phosphatase superfamily and contains the His_Pase_superF_clade-1 domain (IPR013078), His_PPase_superfam domain (IPR029033), and the Phosphogly_mut1 domain (IPR005952), which are characteristic of cofactor-dependent phosphoglycerate mutases (dPGMs) (papini2010phosphoglyceratemutaseknock‐out pages 1-2, jedrzejas2001comparisonofthe pages 2-3).

The following summary encapsulates the key functional annotation findings for GPM3:

> GPM3 (YOL056W; UniProt Q12326) in *Saccharomyces cerevisiae* S288c is best annotated as a putative 2,3-bisphosphoglycerate-dependent phosphoglycerate mutase (EC 5.4.2.11) of the phosphoglycerate mutase family, consistent with its assignment to the histidine phosphatase superfamily and the His_Pase_superF_clade-1/PG-BPG mutase domain architecture. (papini2010phosphoglyceratemutaseknock‐out pages 1-2, jedrzejas2001comparisonofthe pages 2-3, bond2001highresolutionstructure pages 1-1)
>
> By family-level inference and paralog comparison, the expected catalytic role of Gpm3 is the reversible interconversion of 3-phosphoglycerate and 2-phosphoglycerate in lower glycolysis and gluconeogenesis, using the canonical cofactor-dependent phosphoglycerate mutase mechanism in which 2,3-bisphosphoglycerate primes an active-site phosphohistidine intermediate. (papini2010phosphoglyceratemutaseknock‐out pages 1-2, jedrzejas2001comparisonofthe pages 2-3, bond2001highresolutionstructure pages 1-1, bond2001highresolutionstructure pages 3-4)
>
> The strongest organism-specific evidence indicates that GPM3 is a high-homology duplicate of the major phosphoglycerate mutase gene GPM1, but at endogenous expression levels it behaves as a non-functional or physiologically negligible homolog: GPM3 is expressed too weakly to support significant glycolytic flux, and overexpression from its native promoter does not rescue a *gpm1Δ* strain. (papini2010phosphoglyceratemutaseknock‐out pages 1-2, papini2010phosphoglyceratemutaseknock‐out pages 6-8)
>
> However, GPM3 is not necessarily a completely dead enzyme: when expressed from the stronger *PFK2* promoter, GPM3 can partially complement the growth defect of *gpm1Δ* cells on glycerol/ethanol after prolonged incubation, implying residual catalytic competence despite poor native expression. (papini2010phosphoglyceratemutaseknock‐out pages 1-2)
>
> Functionally, GPM3 is therefore best viewed as a weakly expressed paralog of the main glycolytic/gluconeogenic phosphoglycerate mutase rather than the primary enzyme carrying this step in vivo; GPM1 remains the dominant physiological phosphoglycerate mutase in yeast. (papini2010phosphoglyceratemutaseknock‐out pages 1-2)
>
> Subcellularly, Gpm3 is expected to function in the cytoplasm, matching the usual localization of soluble glycolytic enzymes and available yeast localization resources; unlike Gpm1, there is no strong evidence for a characterized cell-wall moonlighting role for Gpm3. (papini2010phosphoglyceratemutaseknock‐out pages 1-2, rodicio2009sugarmetabolismby pages 8-9)
>
> Evolutionarily, GPM3 appears to have arisen through gene-duplication events that generated the GPM1/GPM2/GPM3 family; comparative analyses of glycolytic duplicates support broader retention of glycolytic paralogs in yeast evolution, although GPM2/GPM3 were treated separately from canonical retained whole-genome-duplication pairs in one comparative study. (papini2010phosphoglyceratemutaseknock‐out pages 1-2, conant2007increasedglycolyticflux pages 4-5, conant2007increasedglycolyticflux pages 3-4)


*Blockquote: This blockquote condenses the main functional annotation conclusions for yeast GPM3, integrating direct organism-specific evidence with enzyme-family mechanistic inference. It is useful as a concise evidence-backed summary of likely function, pathway role, localization, and evolutionary origin.*

## 2. Enzymatic Function and Catalytic Mechanism

### 2.1. Predicted Reaction

By sequence homology and domain architecture, GPM3 encodes a 2,3-bisphosphoglycerate-dependent phosphoglycerate mutase predicted to catalyze the reversible interconversion of 3-phosphoglycerate (3-PG) and 2-phosphoglycerate (2-PG), a step in the lower portion of the Embden-Meyerhof-Parnas glycolytic pathway and in gluconeogenesis (papini2010phosphoglyceratemutaseknock‐out pages 1-2).

### 2.2. Catalytic Mechanism of the dPGM Family

The catalytic mechanism of dPGMs is well characterized through structural and biochemical studies of the related yeast Gpm1 enzyme and the *E. coli* dPGM. The enzyme requires the cofactor 2,3-bisphosphoglycerate (2,3-BPG) for activation. The native (unactivated) protein must first be phosphorylated by 2,3-BPG at a conserved nucleophilic histidine residue (His10 in the *E. coli* numbering, His8 in the yeast enzyme), generating a phosphoenzyme intermediate and releasing either 2-PG or 3-PG (jedrzejas2001comparisonofthe pages 2-3, bond2001highresolutionstructure pages 1-1, bond2001highresolutionstructure pages 1-2). The catalytic mechanism involves a pair of histidine residues: one histidine accepts the phosphoryl group from the cofactor (nucleophilic histidine), while a second histidine (His183 in *E. coli*) serves as a proton source during catalysis (jedrzejas2001comparisonofthe pages 2-3, bond2001highresolutionstructure pages 3-4). Notably, no metal ions are required for dPGM catalysis, distinguishing it from the cofactor-independent phosphoglycerate mutases (iPGMs) (jedrzejas2001comparisonofthe pages 2-3).

Beyond its mutase activity, the dPGM family possesses two additional catalytic activities: a phosphatase activity that converts 2,3-bisphosphoglycerate to monophosphoglycerate plus phosphate, and a synthase activity that converts 1,3-bisphosphoglycerate to 2,3-bisphosphoglycerate (bond2001highresolutionstructure pages 1-1).

### 2.3. Structural Basis

The crystal structure of the yeast dPGM (Gpm1) was first solved in 1974 (PDB: 3PGM), with multiple subsequent structures determined at increasing resolution (PDB entries 4PGM, 5PGM, 1BQ3, 1BQ4, 1QHF) (bond2001highresolutionstructure pages 1-1). The monomer adopts an α/β fold featuring a six-stranded β-sheet (C-B-D-A-E-F, with all but E parallel) flanked by six α-helices. The active site is located at the C-terminal edge of the β-sheet and is cup-shaped, approximately 16 Å deep and 10 × 8 Å wide with a volume of ~1200 Å³ (bond2001highresolutionstructure pages 1-2, bond2001highresolutionstructure pages 3-4). Key conserved active-site residues include His10 (nucleophilic), His183, Glu88, Arg61, Asn16, and Ser57, which are conserved across *E. coli*, *S. cerevisiae*, *S. pombe*, and human dPGM enzymes (bond2001highresolutionstructure pages 3-4). The yeast Gpm1 forms a tetramer, distinguishing it from the *E. coli* enzyme which is dimeric (bond2001highresolutionstructure pages 1-1, bond2001highresolutionstructure pages 1-2). Given the high sequence homology between GPM3 and GPM1, Gpm3 is predicted to share this overall fold and domain architecture.

## 3. Relationship to the Phosphoglycerate Mutase Gene Family in Yeast

*S. cerevisiae* harbors three genes encoding putative phosphoglycerate mutases: GPM1 (YKL152C), GPM2 (YDL021W), and GPM3 (YOL056W). The following table summarizes their comparative properties:

| Gene | Systematic name | Chromosomal location | Expression level | Functional status | Ability to complement **gpm1Δ** | Key evidence/references |
|---|---|---|---|---|---|---|
| **GPM1** | **YKL152C** | Right arm of chromosome VIII | High/constitutive; major expressed phosphoglycerate mutase isoform | Major functional phosphoglycerate mutase for glycolysis and gluconeogenesis; enzyme catalyzes 3-phosphoglycerate ↔ 2-phosphoglycerate | Native functional gene; deletion causes severe growth defect and inability to grow on glucose alone | Papini et al. 2010; Rodicio & Heinisch 2009 (papini2010phosphoglyceratemutaseknock‐out pages 1-2, rodicio2009sugarmetabolismby pages 8-9) |
| **GPM2** | **YDL021W** | Left arm of chromosome IV | Very low endogenous expression | Non-functional/weakly functional homolog of **GPM1** formed by duplication; does not contribute significantly to glycolytic flux at native expression | **No** complementation under own promoter; **partial** complementation only when overexpressed from **PFK2** promoter on glycerol/ethanol after prolonged incubation | Papini et al. 2010 (summarizing Heinisch et al.) (papini2010phosphoglyceratemutaseknock‐out pages 1-2) |
| **GPM3** | **YOL056W** | Left arm of chromosome XV | Very low endogenous expression | Non-functional/weakly functional homolog of **GPM1**; likely retains residual catalytic capacity but is not expressed enough to support significant flux | **No** complementation under own promoter; **partial** complementation only when overexpressed from **PFK2** promoter on glycerol/ethanol after prolonged incubation | Papini et al. 2010; targeted proteomics shows low expression and close regulatory clustering with Gpm1/Gpm3 family behavior (papini2010phosphoglyceratemutaseknock‐out pages 1-2, papini2010phosphoglyceratemutaseknock‐out pages 6-8, costenoble2011comprehensivequantitativeanalysis pages 6-8) |


*Table: This table compares the three phosphoglycerate mutase genes in Saccharomyces cerevisiae, highlighting that GPM1 is the major functional isoform, whereas GPM2 and GPM3 are very weakly expressed homologs with only partial rescue capacity when strongly overexpressed. It is useful for distinguishing primary enzyme function from paralog redundancy.*

GPM1 is the major glycolytic and gluconeogenic phosphoglycerate mutase in yeast. It encodes a constitutively expressed enzyme that forms a tetramer of four identical subunits, each approximately 28 kDa (papini2010phosphoglyceratemutaseknock‐out pages 1-2). Deletion of GPM1 renders cells unable to grow on glucose as a sole carbon source; growth is only possible when glycerol and ethanol are provided together, with glycerol feeding gluconeogenesis and ethanol providing energy through respiration (papini2010phosphoglyceratemutaseknock‐out pages 1-2).

GPM2 and GPM3 were identified through genome sequencing as genes with high sequence homology to GPM1. However, Heinisch and colleagues demonstrated that both are effectively non-functional homologs under physiological conditions: overexpression of GPM2 or GPM3 on multicopy vectors under the control of their own promoters does not complement a *gpm1* deletion mutant when grown on complex media containing glucose or a mixture of glycerol/ethanol (papini2010phosphoglyceratemutaseknock‐out pages 1-2). Further analysis of the GPM2 and GPM3 promoters indicated that these genes are expressed at levels too low to contribute to a significant glycolytic flux (papini2010phosphoglyceratemutaseknock‐out pages 1-2). Transcriptome analysis of a Δ*gpm1* mutant confirmed that GPM2 and GPM3 display very low expression levels even when the primary phosphoglycerate mutase is absent (papini2010phosphoglyceratemutaseknock‐out pages 6-8).

Critically, GPM3 retains some residual catalytic capacity: when GPM2 or GPM3 are overexpressed under the control of the stronger PFK2 promoter, they can partially complement the growth defect of the *gpm1* deletion strain on synthetic and complex media containing glycerol and ethanol, but only after prolonged incubation (papini2010phosphoglyceratemutaseknock‐out pages 1-2). This indicates that the Gpm3 protein likely retains enzymatic function, but its physiological insignificance is primarily due to insufficient endogenous expression rather than complete loss of catalytic competence.

Targeted proteomics studies using selected reaction monitoring (SRM) mass spectrometry have corroborated these findings. Costenoble et al. (2011) detected both Gpm1 and Gpm3 across multiple metabolic steady states and found that the Gpm1/Gpm3 pair clustered in proximate branches in hierarchical clustering analysis, suggesting similar regulatory patterns across growth conditions (costenoble2011comprehensivequantitativeanalysis pages 6-8). This proximity in expression regulation, combined with the partial complementation data, is consistent with Gpm3 being a weakly expressed but functionally related paralog of Gpm1.

## 4. Subcellular Localization

Gpm3 is predicted to localize to the cytoplasm, consistent with its role as a soluble glycolytic enzyme. This localization matches that assigned to Gpm3 in the global yeast GFP-tagged protein localization study (Huh et al. 2003, *Nature* 425:686–691). By contrast, the major paralog Gpm1 is primarily cytoplasmic but has also been found in significant amounts in the yeast cell wall, where it retains enzymatic activity when released by alkaline treatment, although the specific role of Gpm1 in the cell wall remains largely unknown (papini2010phosphoglyceratemutaseknock‐out pages 1-2). There is no experimental evidence indicating that Gpm3 has a similar cell wall–associated moonlighting function.

## 5. Pathway Context: Glycolysis and Gluconeogenesis

The phosphoglycerate mutase reaction occupies a critical position in lower glycolysis, connecting the output of phosphoglycerate kinase (which produces 3-PG) to the input of enolase (which consumes 2-PG to produce phosphoenolpyruvate). In the gluconeogenic direction, the same reaction runs in reverse to convert 2-PG to 3-PG. Deletion of GPM1, the primary enzyme catalyzing this step, leads to a severely impaired growth phenotype: the Δ*gpm1* mutant shows increased transcript levels of genes involved in the pentose phosphate pathway and the glyoxylate shunt, indicating an attempt to compensate for the energy imbalance caused by the deletion of this glycolytic/gluconeogenic gene (papini2010phosphoglyceratemutaseknock‐out pages 1-2). The inability of GPM2 and GPM3 to rescue this phenotype under normal expression conditions underscores the dominance of GPM1 in this metabolic step.

In the context of glycolysis humanization, Boonekamp et al. (2021) replaced yeast glycolytic enzymes with human orthologs and found that human phosphoglycerate mutase 2 (HsPGAM2) showed significantly lower activity than the yeast enzyme and required adaptive laboratory evolution to achieve adequate flux, further highlighting the importance of this enzymatic step to glycolytic throughput (boonekamp2021ayeastwith pages 10-12, boonekamp2021ayeastwith pages 12-15, boonekamp2021ayeastwith pages 15-19).

## 6. Moonlighting Functions of the Phosphoglycerate Mutase Family

While GPM3 itself has no characterized moonlighting roles, the broader phosphoglycerate mutase family in yeasts has well-documented moonlighting functions. In *Candida albicans*, Gpm1 localizes to the cell surface, particularly at hyphal tips, where it binds plasminogen through lysine-binding domains and enables its activation to plasmin by urokinase-type plasminogen activator, facilitating fibrinolysis and extracellular matrix degradation for cell invasion (gancedo2016theexpandinglandscape pages 6-7). Additionally, cell-surface Gpm1 in *C. albicans* binds complement regulators FH and FHL-1, helping the pathogen evade complement-mediated immune responses (gancedo2016theexpandinglandscape pages 7-8). In *S. cerevisiae*, Gpm1 is present and enzymatically active in the cell wall, though its specific functional role there remains unclear (papini2010phosphoglyceratemutaseknock‐out pages 1-2). Given GPM3's very low expression, it is unlikely to contribute meaningfully to any such moonlighting role.

## 7. Evolutionary Context

GPM2 and GPM3 arose through gene duplication events in the *S. cerevisiae* lineage (papini2010phosphoglyceratemutaseknock‐out pages 1-2). Conant and Wolfe (2007) demonstrated that glycolytic gene duplicates retained after the ancient whole-genome duplication (WGD) in the *Saccharomyces* lineage were preferentially preserved relative to the genome-wide average (Fisher's exact test, P = 0.0014), suggesting selective advantage through increased enzymatic dosage and glycolytic flux (conant2007increasedglycolyticflux pages 4-5, conant2007increasedglycolyticflux pages 3-4). However, the GPM2/GPM3 pair was specifically excluded from their main statistical analysis of WGD-retained duplicates, suggesting these paralogs may have arisen through a different duplication mechanism or may have diverged to the point of near non-functionality, unlike the retained WGD duplicates that maintained high expression and contributed to increased glycolytic capacity (conant2007increasedglycolyticflux pages 4-5). Rodicio and Heinisch (2009) listed Gpm1, Gpm2, and Gpm3 as homodimeric phosphoglycerate mutases in their review of yeast sugar metabolism, noting them as putative isoenzymes (rodicio2009sugarmetabolismby pages 8-9).

## 8. Summary

GPM3 (YOL056W) in *Saccharomyces cerevisiae* encodes a putative 2,3-bisphosphoglycerate-dependent phosphoglycerate mutase (EC 5.4.2.11) that is a high-homology paralog of the major glycolytic enzyme GPM1. By domain architecture and family membership, Gpm3 is predicted to catalyze the reversible interconversion of 3-phosphoglycerate and 2-phosphoglycerate using a phosphohistidine intermediate mechanism requiring 2,3-BPG as cofactor. The protein localizes to the cytoplasm. However, under physiological conditions, GPM3 is expressed at negligibly low levels and does not contribute significantly to glycolytic or gluconeogenic flux. Overexpression experiments demonstrate that Gpm3 retains some residual catalytic capacity, as it can partially complement a *gpm1Δ* deletion when driven by a strong heterologous promoter, but only on non-fermentable carbon sources and after extended incubation. GPM3 is therefore best characterized as a weakly expressed, largely non-functional paralog of GPM1 that arose through gene duplication, with the primary functional constraint being transcriptional silencing rather than complete loss of enzymatic activity.

References

1. (papini2010phosphoglyceratemutaseknock‐out pages 1-2): Marta Papini, Intawat Nookaew, Gionata Scalcinati, Verena Siewers, and Jens Nielsen. Phosphoglycerate mutase knock‐out mutant saccharomyces cerevisiae: physiological investigation and transcriptome analysis. Biotechnology Journal, 5:1016-1027, Oct 2010. URL: https://doi.org/10.1002/biot.201000199, doi:10.1002/biot.201000199. This article has 15 citations and is from a peer-reviewed journal.

2. (jedrzejas2001comparisonofthe pages 2-3): Mark J. Jedrzejas and Peter Setlow. Comparison of the binuclear metalloenzymes diphosphoglycerate-independent phosphoglycerate mutase and alkaline phosphatase: their mechanism of catalysis via a phosphoserine intermediate. Chemical Reviews, 101:607-618, Feb 2001. URL: https://doi.org/10.1021/cr000253a, doi:10.1021/cr000253a. This article has 156 citations and is from a highest quality peer-reviewed journal.

3. (bond2001highresolutionstructure pages 1-1): Charles S. Bond, Malcolm F. White, and William N. Hunter. High resolution structure of the phosphohistidine-activated form of escherichia coli cofactor-dependent phosphoglycerate mutase*. The Journal of Biological Chemistry, 276:3247-3253, Feb 2001. URL: https://doi.org/10.1074/jbc.m007318200, doi:10.1074/jbc.m007318200. This article has 83 citations.

4. (bond2001highresolutionstructure pages 3-4): Charles S. Bond, Malcolm F. White, and William N. Hunter. High resolution structure of the phosphohistidine-activated form of escherichia coli cofactor-dependent phosphoglycerate mutase*. The Journal of Biological Chemistry, 276:3247-3253, Feb 2001. URL: https://doi.org/10.1074/jbc.m007318200, doi:10.1074/jbc.m007318200. This article has 83 citations.

5. (papini2010phosphoglyceratemutaseknock‐out pages 6-8): Marta Papini, Intawat Nookaew, Gionata Scalcinati, Verena Siewers, and Jens Nielsen. Phosphoglycerate mutase knock‐out mutant saccharomyces cerevisiae: physiological investigation and transcriptome analysis. Biotechnology Journal, 5:1016-1027, Oct 2010. URL: https://doi.org/10.1002/biot.201000199, doi:10.1002/biot.201000199. This article has 15 citations and is from a peer-reviewed journal.

6. (rodicio2009sugarmetabolismby pages 8-9): Rosaura Rodicio and Jürgen J. Heinisch. Sugar metabolism by saccharomyces and non-saccharomyces yeasts. ArXiv, pages 113-134, 2009. URL: https://doi.org/10.1007/978-3-540-85463-0\_6, doi:10.1007/978-3-540-85463-0\_6. This article has 40 citations.

7. (conant2007increasedglycolyticflux pages 4-5): Gavin C Conant and Kenneth H Wolfe. Increased glycolytic flux as an outcome of whole-genome duplication in yeast. Molecular Systems Biology, Jul 2007. URL: https://doi.org/10.1038/msb4100170, doi:10.1038/msb4100170. This article has 312 citations and is from a highest quality peer-reviewed journal.

8. (conant2007increasedglycolyticflux pages 3-4): Gavin C Conant and Kenneth H Wolfe. Increased glycolytic flux as an outcome of whole-genome duplication in yeast. Molecular Systems Biology, Jul 2007. URL: https://doi.org/10.1038/msb4100170, doi:10.1038/msb4100170. This article has 312 citations and is from a highest quality peer-reviewed journal.

9. (bond2001highresolutionstructure pages 1-2): Charles S. Bond, Malcolm F. White, and William N. Hunter. High resolution structure of the phosphohistidine-activated form of escherichia coli cofactor-dependent phosphoglycerate mutase*. The Journal of Biological Chemistry, 276:3247-3253, Feb 2001. URL: https://doi.org/10.1074/jbc.m007318200, doi:10.1074/jbc.m007318200. This article has 83 citations.

10. (costenoble2011comprehensivequantitativeanalysis pages 6-8): Roeland Costenoble, Paola Picotti, Lukas Reiter, Robert Stallmach, Matthias Heinemann, Uwe Sauer, and Ruedi Aebersold. Comprehensive quantitative analysis of central carbon and amino-acid metabolism in saccharomyces cerevisiae under multiple conditions by targeted proteomics. Molecular Systems Biology, 7:464-464, Feb 2011. URL: https://doi.org/10.1038/msb.2010.122, doi:10.1038/msb.2010.122. This article has 144 citations and is from a highest quality peer-reviewed journal.

11. (boonekamp2021ayeastwith pages 10-12): Francine J. Boonekamp, Ewout Knibbe, Marcel A. Vieira-Lara, Melanie Wijsman, Marijke A.H. Luttik, Karen van Eunen, Maxime den Ridder, Reinier Bron, Ana Maria Almonacid Suarez, Patrick van Rijn, Justina C. Wolters, Martin Pabst, Jean-Marc Daran, Barbara Bakker, and Pascale Daran-Lapujade. A yeast with muscle doesn’t run faster: full humanization of the glycolytic pathway in saccharomyces cerevisiae. bioRxiv, Sep 2021. URL: https://doi.org/10.1101/2021.09.28.462164, doi:10.1101/2021.09.28.462164. This article has 3 citations.

12. (boonekamp2021ayeastwith pages 12-15): Francine J. Boonekamp, Ewout Knibbe, Marcel A. Vieira-Lara, Melanie Wijsman, Marijke A.H. Luttik, Karen van Eunen, Maxime den Ridder, Reinier Bron, Ana Maria Almonacid Suarez, Patrick van Rijn, Justina C. Wolters, Martin Pabst, Jean-Marc Daran, Barbara Bakker, and Pascale Daran-Lapujade. A yeast with muscle doesn’t run faster: full humanization of the glycolytic pathway in saccharomyces cerevisiae. bioRxiv, Sep 2021. URL: https://doi.org/10.1101/2021.09.28.462164, doi:10.1101/2021.09.28.462164. This article has 3 citations.

13. (boonekamp2021ayeastwith pages 15-19): Francine J. Boonekamp, Ewout Knibbe, Marcel A. Vieira-Lara, Melanie Wijsman, Marijke A.H. Luttik, Karen van Eunen, Maxime den Ridder, Reinier Bron, Ana Maria Almonacid Suarez, Patrick van Rijn, Justina C. Wolters, Martin Pabst, Jean-Marc Daran, Barbara Bakker, and Pascale Daran-Lapujade. A yeast with muscle doesn’t run faster: full humanization of the glycolytic pathway in saccharomyces cerevisiae. bioRxiv, Sep 2021. URL: https://doi.org/10.1101/2021.09.28.462164, doi:10.1101/2021.09.28.462164. This article has 3 citations.

14. (gancedo2016theexpandinglandscape pages 6-7): Carlos Gancedo, Carmen-Lisset Flores, and Juana M. Gancedo. The expanding landscape of moonlighting proteins in yeasts. Microbiology and Molecular Biology Reviews, 80:765-777, Sep 2016. URL: https://doi.org/10.1128/mmbr.00012-16, doi:10.1128/mmbr.00012-16. This article has 82 citations and is from a domain leading peer-reviewed journal.

15. (gancedo2016theexpandinglandscape pages 7-8): Carlos Gancedo, Carmen-Lisset Flores, and Juana M. Gancedo. The expanding landscape of moonlighting proteins in yeasts. Microbiology and Molecular Biology Reviews, 80:765-777, Sep 2016. URL: https://doi.org/10.1128/mmbr.00012-16, doi:10.1128/mmbr.00012-16. This article has 82 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](GPM3-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](GPM3-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. jedrzejas2001comparisonofthe pages 2-3
2. bond2001highresolutionstructure pages 1-1
3. bond2001highresolutionstructure pages 3-4
4. costenoble2011comprehensivequantitativeanalysis pages 6-8
5. gancedo2016theexpandinglandscape pages 6-7
6. gancedo2016theexpandinglandscape pages 7-8
7. conant2007increasedglycolyticflux pages 4-5
8. rodicio2009sugarmetabolismby pages 8-9
9. conant2007increasedglycolyticflux pages 3-4
10. bond2001highresolutionstructure pages 1-2
11. boonekamp2021ayeastwith pages 10-12
12. boonekamp2021ayeastwith pages 12-15
13. boonekamp2021ayeastwith pages 15-19
14. https://doi.org/10.1002/biot.201000199,
15. https://doi.org/10.1021/cr000253a,
16. https://doi.org/10.1074/jbc.m007318200,
17. https://doi.org/10.1007/978-3-540-85463-0\_6,
18. https://doi.org/10.1038/msb4100170,
19. https://doi.org/10.1038/msb.2010.122,
20. https://doi.org/10.1101/2021.09.28.462164,
21. https://doi.org/10.1128/mmbr.00012-16,