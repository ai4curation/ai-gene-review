---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-11T03:29:14.815291'
end_time: '2026-05-11T03:47:29.811394'
duration_seconds: 1095.0
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 30
---

## Question

Research the human small nucleolar RNA gene SNORD116-1 (RNAcentral URS000075CFA5_9606), one copy in the SNORD116 cluster, for Gene Ontology functional annotation. This is a snoRNA/non-coding RNA, not a protein; do not infer protein domains or enzyme activity. Focus on its core RNA molecular function, nucleolar localization, RNA processing or RNA binding evidence, the strength and limits of evidence connecting the SNORD116 cluster to Prader-Willi syndrome and neurodevelopment, and which GO terms are directly supported for the individual SNORD116-1 gene versus the cluster. Distinguish direct function from locus-level phenotypes, and provide citations for each major claim.

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

Research the human small nucleolar RNA gene SNORD116-1 (RNAcentral URS000075CFA5_9606), one copy in the SNORD116 cluster, for Gene Ontology functional annotation. This is a snoRNA/non-coding RNA, not a protein; do not infer protein domains or enzyme activity. Focus on its core RNA molecular function, nucleolar localization, RNA processing or RNA binding evidence, the strength and limits of evidence connecting the SNORD116 cluster to Prader-Willi syndrome and neurodevelopment, and which GO terms are directly supported for the individual SNORD116-1 gene versus the cluster. Distinguish direct function from locus-level phenotypes, and provide citations for each major claim.

## Research report: GO-relevant functional annotation for human **SNORD116-1** (RNAcentral: **URS000075CFA5_9606**)

### Executive summary
SNORD116-1 is one paralogous copy within the paternally expressed **SNORD116 tandem repeat cluster** embedded in the imprinted **SNHG14 / SNURF–SNRPN** locus at 15q11–q13. The strongest Gene Ontology (GO)-relevant evidence for SNORD116-1 is *structural/class-based*: it is a **box C/D snoRNA** produced by **intron-derived snoRNA biogenesis** and is therefore expected to function within a **box C/D snoRNP** and reside in the **nucleolus**, but direct biochemical assays are generally **not copy-resolved**. By contrast, essentially all disease and neurodevelopmental data implicate **loss of the cluster/critical region**, not loss of a single copy such as SNORD116-1; therefore, Prader–Willi syndrome (PWS) and neurodevelopment phenotypes should be treated as **locus/cluster-level associations**, not direct per-gene functional evidence for SNORD116-1. (bortolincavaille2012thesnord115(hmbii52) pages 1-2, duker2010paternallyinheritedmicrodeletion pages 4-5, chung2020praderwillisyndromereflections pages 7-8)

### 1) Key concepts and definitions (current understanding)

#### 1.1 What SNORD116-1 is (and is not)
* **SNORD116-1 is a non-coding RNA gene** encoding a small nucleolar RNA (snoRNA) and should not be annotated with protein domains or enzymatic activities. The SNORD116 family is described as **box C/D snoRNAs** produced from an imprinted host transcript; box C/D snoRNAs assemble with core proteins (NOP56, NOP58, fibrillarin, and 15.5K/SNU13) to form snoRNPs. (chung2020praderwillisyndromereflections pages 6-7)

#### 1.2 Cluster organization and copy-specific terminology
* The SNORD116 cluster contains multiple paralogues (commonly described as ~30 copies). A widely used subgrouping partitions the cluster into **SNOG1 = SNORD116-1 to SNORD116-9**, SNOG2 = SNORD116-10 to -24, and SNOG3 = SNORD116-25 to -29, reflecting sequence/expression differences. (chung2020praderwillisyndromereflections pages 7-8)
* Copy-resolved expression analyses indicate **heterogeneous expression among individual paralogues** and dominance of group I/II expression in adult tissues (with some copies weak/absent), supporting the need to avoid “all-copies-equal” assumptions in per-copy GO annotation. (baldini2022phylogeneticandmolecular pages 3-5)

#### 1.3 Canonical box C/D snoRNA biology (relevant to GO)
* Canonical box C/D snoRNAs are processed from **excised and debranched introns** by exonucleolytic trimming and typically accumulate in **nucleoli** as snoRNPs. (chung2020praderwillisyndromereflections pages 6-7, bortolincavaille2012thesnord115(hmbii52) pages 1-2)
* Canonically, box C/D snoRNAs guide **2′-O-methylation** of target RNAs via antisense elements; however, multiple authoritative sources emphasize that **SNORD116 snoRNAs are “orphan”**: they show no clear complementarity to rRNA and **validated targets have been difficult to define**. (chung2020praderwillisyndromereflections pages 7-8, holmes2025footprintsinthe pages 2-3, cavaille2017boxcdsmall pages 1-3)

### 2) Molecular function and cellular component evidence for SNORD116-1 vs the cluster

#### 2.1 Evidence supporting “box C/D snoRNA / snoRNP component” for SNORD116
* Experimental mapping of SNORD116 termini and processing products supports that the **cluster generates canonical snoRNA-sized species** (e.g., ~92 nt dominant species in mouse) via intron-derived processing pathways; low-abundance truncated forms exist but their functional relevance is not established. (bortolincavaille2012thesnord115(hmbii52) pages 6-6)
* Reviews and primary studies support that SNORD116 family members behave as bona fide box C/D snoRNAs that assemble with core snoRNP proteins. In particular, fibrillarin RIP-seq enrichment over the **first third of the cluster** supports snoRNP association for that region, aligning with SNOG1 (which includes SNORD116-1). (chung2020praderwillisyndromereflections pages 7-8)

**GO implication:** for SNORD116-1, the most defensible molecular-function annotation is a **box C/D snoRNA / snoRNP-associated RNA scaffold role**, but the direct experimental evidence is at subgroup/cluster resolution rather than SNORD116-1-specific pulldowns. (bortolincavaille2012thesnord115(hmbii52) pages 1-2, chung2020praderwillisyndromereflections pages 7-8)

#### 2.2 Nucleolar localization
* Box C/D snoRNAs are described as concentrating mainly in the **nucleolus**, and SNORD116 snoRNAs are described as **localizing to nucleoli** (processed snoRNAs), consistent with canonical snoRNA biology. (bortolincavaille2012thesnord115(hmbii52) pages 1-2, holmes2025footprintsinthe pages 10-12)

**GO implication:** a cellular-component assignment to **nucleolus** is supported strongly for the **processed SNORD116 snoRNAs collectively**, but not proven for SNORD116-1 specifically by copy-resolved imaging. (holmes2025footprintsinthe pages 10-12, bortolincavaille2012thesnord115(hmbii52) pages 1-2)

#### 2.3 Biogenesis: intron-derived processing from SNHG14/SNURF–SNRPN
* Multiple sources describe SNORD116 copies as embedded within, and processed from, repeated introns of the large imprinted host transcript (SNHG14/SNURF–SNRPN region), via splicing/debranching followed by exonucleolytic trimming. (chung2020praderwillisyndromereflections pages 6-7, bortolincavaille2012thesnord115(hmbii52) pages 1-2)
* In neuronal differentiation models, mature SNORD116 predominates over extended forms, consistent with efficient processing from the host. (helwak2024rolesofsnord115 pages 2-4)

**GO implication:** biological-process terms consistent with **snoRNA processing/biogenesis from introns** are well supported at the family/cluster level and can be cautiously extended to SNORD116-1 as a member of the intronic array. (bortolincavaille2012thesnord115(hmbii52) pages 1-2, helwak2024rolesofsnord115 pages 2-4)

#### 2.4 Guide activity for 2′-O-methylation: what is supported vs not
* Authoritative discussions repeatedly describe SNORD116 as an **orphan box C/D snoRNA family** with no validated rRNA targets and no established canonical 2′-O-methylation guide function for specific targets. (chung2020praderwillisyndromereflections pages 7-8, holmes2025footprintsinthe pages 2-3, cavaille2017boxcdsmall pages 1-3)

**GO implication:** it is not currently justified (from the cited evidence base) to assign SNORD116-1 a specific “**guide for 2′-O-methylation of RNA**” molecular function. (chung2020praderwillisyndromereflections pages 7-8, holmes2025footprintsinthe pages 2-3)

#### 2.5 RNA-binding / non-canonical regulatory roles: cluster-level evidence and limits
* Cluster-/locus-level studies report diverse downstream molecular effects and RNA interactions for Snord116/SNORD116, including locus-wide interaction mapping and altered signaling readouts in animal models, but these generally do not identify a single paralogue as causal. (holmes2025footprintsinthe pages 9-10, holmes2025footprintsinthe pages 10-12)
* A notable limitation for per-copy annotation is that the only explicit paralogue-specific functional example in the retrieved evidence concerns **SNORD116-3** (predicted interaction with *Nhlh2* and effects on mRNA decay under SNORD116 manipulation), and this should **not** be transferred to SNORD116-1 without direct evidence. (holmes2025footprintsinthe pages 9-10)

### 3) Evidence connecting the SNORD116 region to Prader–Willi syndrome and neurodevelopment

#### 3.1 Strength of evidence (human genetics)
* Human atypical **paternal microdeletions encompassing SNORD116** are repeatedly cited as sufficient to produce a PWS clinical picture. In a widely cited example, a paternally inherited ~236 kb deletion including SNORD116 showed **complete loss of SNORD116 expression** in blood while SNRPN and UBE3A were detected, supporting SNORD116-region causality. (duker2010paternallyinheritedmicrodeletion pages 3-4)
* Reported clinical features across SNORD116-region microdeletion patients include classic PWS findings (e.g., neonatal hypotonia, feeding problems/failure to thrive, later hyperphagia/obesity, developmental delay, behavioral problems, sleep disturbance, hypogonadism). (duker2010paternallyinheritedmicrodeletion pages 4-5)

**Interpretation:** these data strongly support that **loss of the SNORD116 critical region/cluster** is a key driver of PWS phenotypes in humans. (duker2010paternallyinheritedmicrodeletion pages 4-5, duker2010paternallyinheritedmicrodeletion pages 3-4)

#### 3.2 Limits of evidence (single-copy resolution and confounding)
* The deletions implicated in PWS remove **multiple tandem copies** (and sometimes neighboring noncoding elements), and thus do **not** establish that loss of any single repeat (including SNORD116-1) is sufficient for disease. (duker2010paternallyinheritedmicrodeletion pages 2-3)
* Minimal critical intervals cited in the literature can include additional noncoding genes (e.g., IPW and other snoRNAs), which complicates strict attribution to SNORD116 mature snoRNAs alone versus other locus-derived products. (burnett2017lossofthe pages 1-2)

#### 3.3 Model systems: what they support
* Mouse models with targeted Snord116-cluster deletions reproduce subsets of PWS-relevant phenotypes (e.g., growth retardation, hypotonia/activity changes, neurobehavioral phenotypes), but may fail to recapitulate others (notably obesity/infertility in some lines), indicating species/strain differences and incomplete model capture. (duker2010paternallyinheritedmicrodeletion pages 4-5)
* Developmental phenotyping of Snord116p/m+ mice revealed neuronal and endocrine pancreatic developmental changes (e.g., reduced neuronal cell body size with decreased nucleolar size; islet cellular composition changes), further supporting a cluster-level developmental role. (burnett2017lossofthe pages 1-2)

### 4) Recent developments (prioritizing 2023–2024)

#### 4.1 2024 Nature Communications: SNORD116 cluster roles during neuronal differentiation (LUHMES)
* Helwak et al. (Nature Communications; **published Nov 2024**; https://doi.org/10.1038/s41467-024-54573-8) created cell lines lacking the expressed paternal SNORD116 cluster and showed SNORD116 abundance increases during differentiation (~**5-fold** from day 0 to day 15 by RT-PCR) and plateaus between days 6–10, interpreted as stabilization. (helwak2024rolesofsnord115 pages 1-2, helwak2024rolesofsnord115 pages 2-4)
* Functional consequences of SNORD116-cluster deletion included acceleration toward more mature neuronal transcriptomic states and measurable transcriptome/proteome changes; the study reports limited bona fide alternative splicing changes (e.g., **95 events** in H116) and compiled a curated list of **24 high-confidence SNORD116-specific dysregulated RNAs**, plus proteome-level shifts (including altered protein/mRNA ratio changes). (helwak2024rolesofsnord115 pages 8-9)
* The paper provides a locus schematic and expression evidence across differentiation timepoints (days 0, 6, 10, 15), useful for grounding GO cellular context and biogenesis claims. (helwak2024rolesofsnord115 media 1ebb8c3a, helwak2024rolesofsnord115 media f44777c4)

#### 4.2 2024 Nucleic Acids Research: isogenic hESC neuronal deletion models and predicted targets
* Gilmore et al. (Nucleic Acids Research; **published Nov 2024**; https://doi.org/10.1093/nar/gkae1129) engineered isogenic hESC lines with deletions affecting the SNORD116 region, differentiated them into neurons, and identified **42 consistently dysregulated genes** across deletions; these genes were enriched for predicted SNORD116 targeting and were linked to validated changes in **FGF13 protein** levels. (gilmore2024identifyingkeyunderlying pages 1-2)

#### 4.3 2023 Human Molecular Genetics: SNHG14-derived sno-lncRNAs/SPA-lncRNAs regulate transcriptional programs
* Sledziowska et al. (Human Molecular Genetics; **published Sep 2023**; https://doi.org/10.1093/hmg/ddac228) depleted SNHG14-derived sno-lncRNAs and SPA-lncRNAs using antisense GapmeRs in iPSCs and used chromatin-associated RNA-seq to capture transcriptional effects. Combined knockdown (up to **80%**, 65% average) yielded **205 downregulated and 87 upregulated** transcripts (24 h), with top downregulated neuronal genes including **FAT3, NRXN1, NLGN1**, and GO/pathway enrichment for neuronal development and synaptic/cell-adhesion functions. (sledziowska2023noncodingrnasassociated pages 4-6, sledziowska2023noncodingrnasassociated pages 1-2)

**GO relevance:** these 2023–2024 studies strengthen the case that the *locus* (including processed snoRNAs and extended intronic RNAs) influences neuronal transcriptional programs, but they largely do **not** establish a direct, single-paralogue molecular function for SNORD116-1. (gilmore2024identifyingkeyunderlying pages 1-2, sledziowska2023noncodingrnasassociated pages 4-6)

### 5) Current applications and real-world implementations

#### 5.1 Diagnostics and genotype–phenotype interpretation
* High-resolution microarray (array CGH), breakpoint mapping, parent-of-origin genotyping, and RT-PCR expression assays have been used clinically/research-wise to identify atypical **SNORD116-region microdeletions** associated with PWS phenotypes, supporting real-world utility for genetic diagnosis beyond classic large deletions/UPD. (duker2010paternallyinheritedmicrodeletion pages 1-2, duker2010paternallyinheritedmicrodeletion pages 2-3)

#### 5.2 Therapeutic strategies (conceptual; locus-level)
* A recurring translational theme is **reactivation of the normally silent maternal allele** of PWS-locus genes (including SNORD116) via epigenetic modulation, although this is a locus-level approach and not a SNORD116-1-specific intervention. (gilmore2024identifyingkeyunderlying pages 1-2)

### 6) Expert opinions and authoritative synthesis
* Expert reviews emphasize two points: (i) SNORD116 is likely central to PWS pathogenesis because atypical deletions limited to the SNORD116 region can yield core phenotypes; (ii) the **mechanism of action remains unresolved**, in part because SNORD116 lacks clear canonical rRNA complementarity and targets are unknown, making it difficult to assign classic methylation-guide GO functions. (chung2020praderwillisyndromereflections pages 7-8, cavaille2017boxcdsmall pages 1-3)

### 7) Key statistics and quantitative findings (recent studies)
* SNORD116 genomic organization in SNHG14: **~29 tandem introns** generate SNORD116 in the human host gene SNHG14 (reported in 2024 LUHMES study). (helwak2024rolesofsnord115 pages 1-2)
* SNORD116 induction during neuronal differentiation: **~5× increase** from day 0 to day 15 (LUHMES). (helwak2024rolesofsnord115 pages 1-2, helwak2024rolesofsnord115 media f44777c4)
* Transcriptome effects (cluster deletion): **42 consistently dysregulated genes** across two isogenic hESC neuron deletion models. (gilmore2024identifyingkeyunderlying pages 1-2)
* Transcriptional response to SNHG14-derived lncRNA depletion (iPSC, 24 h): knockdown up to **80%**, and **205 down / 87 up** transcripts with combined SPA/sno-lncRNA depletion. (sledziowska2023noncodingrnasassociated pages 4-6)
* PWS genetics epidemiology (reviewed): SNORD116-only microdeletions are described as rare (**<1%** of PWS cases) relative to large deletions and UPD, underscoring limited patient numbers for genotype refinement. (mendiola2024characterizingtherolea pages 16-21)

---

### GO-term support overview (SNORD116-1 vs cluster)
The following table consolidates GO-relevant evidence and explicitly separates what is directly supportable for **SNORD116-1** from what is only supportable at **cluster/locus level**.

| Entity | GO aspect | Candidate GO term label | Direct evidence summary | Key limitations for per-copy assignment | Primary citations |
|---|---|---|---|---|---|
| SNORD116-1 (single copy; SNOG1/group I) | MF | box C/D snoRNA / snoRNP scaffold activity | SNORD116 family members are bona fide box C/D snoRNAs with conserved C/D features and are processed as canonical snoRNAs; SNOG1 includes SNORD116-1 to -9, and the first third of the cluster shows fibrillarin RIP enrichment, consistent with snoRNP assembly in this subgroup. | Evidence is subgroup- or cluster-level, not a direct biochemical assay on SNORD116-1 alone; no copy-specific fibrillarin/NOP58 pulldown for SNORD116-1 was shown. | (bortolincavaille2012thesnord115(hmbii52) pages 1-2, chung2020praderwillisyndromereflections pages 7-8, baldini2022phylogeneticandmolecular pages 3-5) |
| SNORD116 cluster / locus products | MF | box C/D snoRNA / snoRNP scaffold activity | SNORD116 cluster products were recommended to be considered bona fide box C/D snoRNAs; canonical box C/D snoRNP association is supported by fibrillarin RIP-seq over the first third of the cluster and by reports that Snord116 associates with FBL and NOP58 in brain extracts. | Still largely inferred at the cluster/family level; exact stoichiometry and whether all paralogues assemble equivalently are unresolved. | (chung2020praderwillisyndromereflections pages 7-8, holmes2025footprintsinthe pages 10-12, bortolincavaille2012thesnord115(hmbii52) pages 1-2, cavaille2017boxcdsmall pages 1-3) |
| SNORD116-1 | CC | nucleolus | General box C/D snoRNAs concentrate in nucleoli, and SNOG1 subgroup members are the most highly expressed in hypothalamus with fibrillarin enrichment over the first third of the cluster, making nucleolar residence plausible for SNORD116-1. | No direct imaging/localization experiment was reported for SNORD116-1 individually. | (bortolincavaille2012thesnord115(hmbii52) pages 1-2, chung2020praderwillisyndromereflections pages 7-8) |
| SNORD116 cluster / locus products | CC | nucleolus / nucleolar snoRNP | Processed Snord116 snoRNAs localize to nucleoli; SNORD116 snoRNAs are described as able to localize to the nucleolus, consistent with canonical box C/D snoRNA behavior. | Localization evidence is for processed snoRNAs collectively, not each human paralogue; 116HG host RNA has different localization (retained at transcription site), so locus products are heterogeneous. | (holmes2025footprintsinthe pages 10-12, bortolincavaille2012thesnord115(hmbii52) pages 1-2) |
| SNORD116-1 | BP | snoRNA processing from intron of SNHG14/SNURF-SNRPN transcript | SNORD116 genes are embedded within repeated introns of the long SNHG14/SNURF-SNRPN transcript and mature SNORD116 RNAs arise by splicing/debranching and exonucleolytic trimming; SNORD116-1 belongs to this intronic repeat set. | Processing was demonstrated for SNORD116 family/cluster, not mapped specifically to SNORD116-1 in the cited evidence. | (bortolincavaille2012thesnord115(hmbii52) pages 6-6, bortolincavaille2012thesnord115(hmbii52) pages 1-2, helwak2024rolesofsnord115 pages 2-4) |
| SNORD116 cluster / locus products | BP | intron-derived snoRNA processing from SNHG14/SNURF-SNRPN | Strong evidence supports intron-derived biogenesis: box C/D snoRNAs are processed from excised/debranched introns; full-length SNORD116 termini were mapped; mature SNORD116 predominates over extended forms during neuronal differentiation. The same locus also yields 116HG, sno-lncRNAs, and SPA-lncRNAs. | Biogenesis differs among locus products, so one GO statement cannot cover all products equally; sno-lncRNAs/SPA-lncRNAs are distinct noncanonical derivatives. | (bortolincavaille2012thesnord115(hmbii52) pages 6-6, bortolincavaille2012thesnord115(hmbii52) pages 1-2, sledziowska2023noncodingrnasassociated pages 1-2, helwak2024rolesofsnord115 pages 2-4) |
| SNORD116-1 | MF | guide for 2'-O-methylation of RNA | Not directly supported. SNORD116 is repeatedly described as an orphan box C/D snoRNA family with no validated rRNA targets and no established direct methylation target for SNORD116-1. | Canonical guide activity cannot be assigned to SNORD116-1 from current direct evidence; family-level potential does not equal demonstrated targeting by this copy. | (chung2020praderwillisyndromereflections pages 7-8, holmes2025footprintsinthe pages 2-3, cavaille2017boxcdsmall pages 1-3) |
| SNORD116 cluster / locus products | MF | guide for 2'-O-methylation of RNA | Not directly supported for the cluster either: although box C/D snoRNAs usually guide 2'-O-methylation, SNORD116 lacks clear rRNA complementarity and remains classified as orphan; no validated SNORD116 methylation target was established in the cited peer-reviewed 2023-2024 studies. | Candidate methylation interactions are computational/predicted; direct target validation remains lacking in the cited evidence base. | (chung2020praderwillisyndromereflections pages 7-8, holmes2025footprintsinthe pages 2-3, cavaille2017boxcdsmall pages 1-3, helwak2024rolesofsnord115 pages 9-10) |
| SNORD116-1 | MF/BP | RNA binding / post-transcriptional regulation of mRNA stability | No direct evidence for SNORD116-1 specifically. Copy-resolved functional evidence cited instead concerns SNORD116-3, for which a predicted 20-bp interaction with Nhlh2 mRNA was linked to altered mRNA decay/stability after SNORD116 manipulation. | The only copy-specific functional example in the cited set is SNORD116-3, not SNORD116-1; therefore this should not be transferred to SNORD116-1. | (holmes2025footprintsinthe pages 9-10) |
| SNORD116 cluster / locus products | MF/BP | RNA binding / regulation of mRNA stability or transcript abundance | Cluster-level studies reported ChIRP-seq and snoKARR-seq interactions, 32 RNA interactions in mouse cortex, and human neuronal deletion models with 42 consistently dysregulated genes enriched for predicted SNORD116 targets; FGF13 protein changes were validated. SNORD116 overexpression also altered Nhlh2 mRNA stability. | These findings are mostly cluster-level, often from mouse or engineered deletion/overexpression systems, and do not resolve which individual paralogue is responsible. | (holmes2025footprintsinthe pages 9-10, gilmore2024identifyingkeyunderlying pages 1-2) |
| SNORD116-1 | BP | regulation of neuronal differentiation / neurodevelopment | Not directly supported for the single gene. SNOG1/SNORD116-1 is in the highly expressed subgroup, but no single-copy perturbation study linked SNORD116-1 to neuronal differentiation timing or transcriptome change. | All cited neurodevelopmental effects come from cluster deletions or locus-level ncRNA depletion, not SNORD116-1-specific loss-of-function. | (chung2020praderwillisyndromereflections pages 7-8, helwak2024rolesofsnord115 pages 1-2) |
| SNORD116 cluster / locus products | BP | modulation of neuronal differentiation timing / neurodevelopmental transcriptome | 2024 neuronal models showed that SNORD116 cluster deletion accelerates aspects of neuronal maturation, alters RNA stability and protein synthesis, and changes defined transcript/protein sets; a curated set of 24 high-confidence SNORD116-specific dysregulated RNAs was reported, and 42 consistently dysregulated genes were found across isogenic hESC-neuron models. | These are downstream phenotypes from deleting the cluster/locus and do not prove a direct biochemical activity for any one snoRNA copy; some effects may involve other locus-derived RNAs. | (gilmore2024identifyingkeyunderlying pages 1-2, helwak2024rolesofsnord115 pages 9-10, helwak2024rolesofsnord115 pages 1-2, helwak2024rolesofsnord115 pages 8-9, sledziowska2023noncodingrnasassociated pages 4-6) |
| SNORD116-1 | BP/phenotype context | Prader-Willi syndrome / neurodevelopmental disorder involvement | No direct evidence shows that loss of SNORD116-1 alone causes PWS or neurodevelopmental phenotypes. Human data implicate paternal microdeletions encompassing the SNORD116 cluster/minimal region, not a single repeat. | Disease causality is locus/cluster-level; assigning disease-related GO process terms to SNORD116-1 would overstate the evidence. | (duker2010paternallyinheritedmicrodeletion pages 4-5, duker2010paternallyinheritedmicrodeletion pages 3-4, duker2010paternallyinheritedmicrodeletion pages 1-2, burnett2017lossofthe pages 1-2) |
| SNORD116 cluster / locus products | BP/phenotype context | contribution to PWS-related neurodevelopmental phenotypes | Rare paternal microdeletions removing the SNORD116 critical region are sufficient to produce many core PWS features, and mouse Snord116-cluster deletions recapitulate subsets of metabolic, developmental, neuronal, and endocrine phenotypes. | Minimal critical intervals can include other noncoding elements (e.g., IPW, SNORD109A, host-locus products), and most studies do not separate mature SNORD116 snoRNAs from 116HG/sno-lncRNAs/SPA-lncRNAs. | (duker2010paternallyinheritedmicrodeletion pages 4-5, duker2010paternallyinheritedmicrodeletion pages 3-4, mendiola2024characterizingtherole pages 16-21, burnett2017lossofthe pages 1-2, mendiola2024characterizingtherolea pages 16-21) |


*Table: This table contrasts what is directly supportable for the individual snoRNA gene SNORD116-1 versus the broader SNORD116 cluster/locus and its derived noncoding RNAs. It is designed to help separate core RNA function/localization evidence from cluster-level disease and neurodevelopmental phenotypes.*

### Recommended evidence-based GO annotation stance for SNORD116-1 (conservative)
Based on the retrieved evidence, SNORD116-1 is best annotated with **structural/biogenesis/localization** GO concepts typical of box C/D snoRNAs (snoRNP association; nucleolus; intron-derived snoRNA processing), while **not** being annotated (yet) with specific RNA modification targets or disease-process terms, because:
1) SNORD116 is repeatedly described as an **orphan** family lacking validated canonical targets (limiting MF assignment to “2′-O-methylation guide”). (chung2020praderwillisyndromereflections pages 7-8, holmes2025footprintsinthe pages 2-3)
2) PWS and neurodevelopmental effects are supported for the **cluster/critical region**, not for loss of an individual paralogue like SNORD116-1. (duker2010paternallyinheritedmicrodeletion pages 4-5, duker2010paternallyinheritedmicrodeletion pages 3-4, duker2010paternallyinheritedmicrodeletion pages 2-3)
3) Even when subgroup/copy differences are observed (e.g., SNOG1 enrichment and fibrillarin RIP enrichment over the first third), this is **not** equivalent to a direct SNORD116-1-specific functional assay. (chung2020praderwillisyndromereflections pages 7-8)

### Notes on URLs and publication dates
Primary URLs and publication months/years are embedded above for the principal 2023–2024 sources: Helwak et al. (Nov 2024; https://doi.org/10.1038/s41467-024-54573-8), Gilmore et al. (Nov 2024; https://doi.org/10.1093/nar/gkae1129), and Sledziowska et al. (Sep 2023; https://doi.org/10.1093/hmg/ddac228). (gilmore2024identifyingkeyunderlying pages 1-2, helwak2024rolesofsnord115 pages 1-2, sledziowska2023noncodingrnasassociated pages 4-6)

### Evidence gaps relevant to future GO refinement for SNORD116-1
Key experiments that would enable more specific, per-copy GO terms for SNORD116-1 include: paralogue-resolved CLASH/eCLIP-style RNA–RNA chimera detection; paralogue-specific snoRNP IP (fibrillarin/NOP58) followed by long-read mapping; and direct 2′-O-methylation site assignment linked to specific SNORD116 paralogues. Current evidence remains strongest at the SNORD116 **cluster/subgroup** level rather than at the SNORD116-1 gene level. (gilmore2024identifyingkeyunderlying pages 1-2, chung2020praderwillisyndromereflections pages 7-8, baldini2022phylogeneticandmolecular pages 3-5)

References

1. (bortolincavaille2012thesnord115(hmbii52) pages 1-2): Marie-Line Bortolin-Cavaillé and J. Cavaillé. The snord115 (h/mbii-52) and snord116 (h/mbii-85) gene clusters at the imprinted prader-willi locus generate canonical box c/d snornas. Nucleic Acids Research, 40:6800-6807, Apr 2012. URL: https://doi.org/10.1093/nar/gks321, doi:10.1093/nar/gks321. This article has 108 citations and is from a highest quality peer-reviewed journal.

2. (duker2010paternallyinheritedmicrodeletion pages 4-5): Angela L Duker, Blake C Ballif, Erawati V Bawle, Richard E Person, Sangeetha Mahadevan, Sarah Alliman, Regina Thompson, Ryan Traylor, Bassem A Bejjani, Lisa G Shaffer, Jill A Rosenfeld, Allen N Lamb, and Trilochan Sahoo. Paternally inherited microdeletion at 15q11.2 confirms a significant role for the snord116 c/d box snorna cluster in prader–willi syndrome. European Journal of Human Genetics, 18:1196-1201, Jun 2010. URL: https://doi.org/10.1038/ejhg.2010.102, doi:10.1038/ejhg.2010.102. This article has 384 citations and is from a domain leading peer-reviewed journal.

3. (chung2020praderwillisyndromereflections pages 7-8): Michael S. Chung, Maéva Langouët, Stormy J. Chamberlain, and Gordon G. Carmichael. Prader-willi syndrome: reflections on seminal studies and future therapies. Open Biology, Sep 2020. URL: https://doi.org/10.1098/rsob.200195, doi:10.1098/rsob.200195. This article has 51 citations and is from a peer-reviewed journal.

4. (chung2020praderwillisyndromereflections pages 6-7): Michael S. Chung, Maéva Langouët, Stormy J. Chamberlain, and Gordon G. Carmichael. Prader-willi syndrome: reflections on seminal studies and future therapies. Open Biology, Sep 2020. URL: https://doi.org/10.1098/rsob.200195, doi:10.1098/rsob.200195. This article has 51 citations and is from a peer-reviewed journal.

5. (baldini2022phylogeneticandmolecular pages 3-5): Laeya Baldini, Anne Robert, Bruno Charpentier, and Stéphane Labialle. Phylogenetic and molecular analyses identify snord116 targets involved in the prader–willi syndrome. Molecular Biology and Evolution, Dec 2022. URL: https://doi.org/10.1093/molbev/msab348, doi:10.1093/molbev/msab348. This article has 35 citations and is from a highest quality peer-reviewed journal.

6. (holmes2025footprintsinthe pages 2-3): Terri L. Holmes, Alzbeta Chabronova, Chris Denning, Victoria James, Mandy J. Peffers, and James G. W. Smith. Footprints in the sno: investigating the cellular and molecular mechanisms of snord116. Open Biology, Mar 2025. URL: https://doi.org/10.1098/rsob.240371, doi:10.1098/rsob.240371. This article has 3 citations and is from a peer-reviewed journal.

7. (cavaille2017boxcdsmall pages 1-3): Jérôme Cavaillé. Box c/d small nucleolar rna genes and the prader‐willi syndrome: a complex interplay. Wiley Interdisciplinary Reviews: RNA, Jul 2017. URL: https://doi.org/10.1002/wrna.1417, doi:10.1002/wrna.1417. This article has 109 citations.

8. (bortolincavaille2012thesnord115(hmbii52) pages 6-6): Marie-Line Bortolin-Cavaillé and J. Cavaillé. The snord115 (h/mbii-52) and snord116 (h/mbii-85) gene clusters at the imprinted prader-willi locus generate canonical box c/d snornas. Nucleic Acids Research, 40:6800-6807, Apr 2012. URL: https://doi.org/10.1093/nar/gks321, doi:10.1093/nar/gks321. This article has 108 citations and is from a highest quality peer-reviewed journal.

9. (holmes2025footprintsinthe pages 10-12): Terri L. Holmes, Alzbeta Chabronova, Chris Denning, Victoria James, Mandy J. Peffers, and James G. W. Smith. Footprints in the sno: investigating the cellular and molecular mechanisms of snord116. Open Biology, Mar 2025. URL: https://doi.org/10.1098/rsob.240371, doi:10.1098/rsob.240371. This article has 3 citations and is from a peer-reviewed journal.

10. (helwak2024rolesofsnord115 pages 2-4): Aleksandra Helwak, Tomasz Turowski, Christos Spanos, and David Tollervey. Roles of snord115 and snord116 ncrna clusters during neuronal differentiation. Nature Communications, Nov 2024. URL: https://doi.org/10.1038/s41467-024-54573-8, doi:10.1038/s41467-024-54573-8. This article has 11 citations and is from a highest quality peer-reviewed journal.

11. (holmes2025footprintsinthe pages 9-10): Terri L. Holmes, Alzbeta Chabronova, Chris Denning, Victoria James, Mandy J. Peffers, and James G. W. Smith. Footprints in the sno: investigating the cellular and molecular mechanisms of snord116. Open Biology, Mar 2025. URL: https://doi.org/10.1098/rsob.240371, doi:10.1098/rsob.240371. This article has 3 citations and is from a peer-reviewed journal.

12. (duker2010paternallyinheritedmicrodeletion pages 3-4): Angela L Duker, Blake C Ballif, Erawati V Bawle, Richard E Person, Sangeetha Mahadevan, Sarah Alliman, Regina Thompson, Ryan Traylor, Bassem A Bejjani, Lisa G Shaffer, Jill A Rosenfeld, Allen N Lamb, and Trilochan Sahoo. Paternally inherited microdeletion at 15q11.2 confirms a significant role for the snord116 c/d box snorna cluster in prader–willi syndrome. European Journal of Human Genetics, 18:1196-1201, Jun 2010. URL: https://doi.org/10.1038/ejhg.2010.102, doi:10.1038/ejhg.2010.102. This article has 384 citations and is from a domain leading peer-reviewed journal.

13. (duker2010paternallyinheritedmicrodeletion pages 2-3): Angela L Duker, Blake C Ballif, Erawati V Bawle, Richard E Person, Sangeetha Mahadevan, Sarah Alliman, Regina Thompson, Ryan Traylor, Bassem A Bejjani, Lisa G Shaffer, Jill A Rosenfeld, Allen N Lamb, and Trilochan Sahoo. Paternally inherited microdeletion at 15q11.2 confirms a significant role for the snord116 c/d box snorna cluster in prader–willi syndrome. European Journal of Human Genetics, 18:1196-1201, Jun 2010. URL: https://doi.org/10.1038/ejhg.2010.102, doi:10.1038/ejhg.2010.102. This article has 384 citations and is from a domain leading peer-reviewed journal.

14. (burnett2017lossofthe pages 1-2): Lisa Cole Burnett, Gabriela Hubner, Charles A LeDuc, Michael V Morabito, Jayne F Martin Carli, and Rudolph L Leibel. Loss of the imprinted, non-coding snord116 gene cluster in the interval deleted in the prader willi syndrome results in murine neuronal and endocrine pancreatic developmental phenotypes. Human Molecular Genetics, 26:4606–4616, Dec 2017. URL: https://doi.org/10.1093/hmg/ddx342, doi:10.1093/hmg/ddx342. This article has 38 citations and is from a domain leading peer-reviewed journal.

15. (helwak2024rolesofsnord115 pages 1-2): Aleksandra Helwak, Tomasz Turowski, Christos Spanos, and David Tollervey. Roles of snord115 and snord116 ncrna clusters during neuronal differentiation. Nature Communications, Nov 2024. URL: https://doi.org/10.1038/s41467-024-54573-8, doi:10.1038/s41467-024-54573-8. This article has 11 citations and is from a highest quality peer-reviewed journal.

16. (helwak2024rolesofsnord115 pages 8-9): Aleksandra Helwak, Tomasz Turowski, Christos Spanos, and David Tollervey. Roles of snord115 and snord116 ncrna clusters during neuronal differentiation. Nature Communications, Nov 2024. URL: https://doi.org/10.1038/s41467-024-54573-8, doi:10.1038/s41467-024-54573-8. This article has 11 citations and is from a highest quality peer-reviewed journal.

17. (helwak2024rolesofsnord115 media 1ebb8c3a): Aleksandra Helwak, Tomasz Turowski, Christos Spanos, and David Tollervey. Roles of snord115 and snord116 ncrna clusters during neuronal differentiation. Nature Communications, Nov 2024. URL: https://doi.org/10.1038/s41467-024-54573-8, doi:10.1038/s41467-024-54573-8. This article has 11 citations and is from a highest quality peer-reviewed journal.

18. (helwak2024rolesofsnord115 media f44777c4): Aleksandra Helwak, Tomasz Turowski, Christos Spanos, and David Tollervey. Roles of snord115 and snord116 ncrna clusters during neuronal differentiation. Nature Communications, Nov 2024. URL: https://doi.org/10.1038/s41467-024-54573-8, doi:10.1038/s41467-024-54573-8. This article has 11 citations and is from a highest quality peer-reviewed journal.

19. (gilmore2024identifyingkeyunderlying pages 1-2): Rachel B Gilmore, Yaling Liu, Christopher E Stoddard, Michael S Chung, Gordon G Carmichael, and Justin Cotney. Identifying key underlying regulatory networks and predicting targets of orphan c/d box snord116 snornas in prader–willi syndrome. Nucleic Acids Research, 52:13757-13774, Nov 2024. URL: https://doi.org/10.1093/nar/gkae1129, doi:10.1093/nar/gkae1129. This article has 13 citations and is from a highest quality peer-reviewed journal.

20. (sledziowska2023noncodingrnasassociated pages 4-6): Monika Sledziowska, Kinga Winczura, Matt Jones, Ruba Almaghrabi, Hannah Mischo, Daniel Hebenstreit, Paloma Garcia, and Pawel Grzechnik. Non-coding rnas associated with prader–willi syndrome regulate transcription of neurodevelopmental genes in human induced pluripotent stem cells. Human Molecular Genetics, 32:608-620, Sep 2023. URL: https://doi.org/10.1093/hmg/ddac228, doi:10.1093/hmg/ddac228. This article has 24 citations and is from a domain leading peer-reviewed journal.

21. (sledziowska2023noncodingrnasassociated pages 1-2): Monika Sledziowska, Kinga Winczura, Matt Jones, Ruba Almaghrabi, Hannah Mischo, Daniel Hebenstreit, Paloma Garcia, and Pawel Grzechnik. Non-coding rnas associated with prader–willi syndrome regulate transcription of neurodevelopmental genes in human induced pluripotent stem cells. Human Molecular Genetics, 32:608-620, Sep 2023. URL: https://doi.org/10.1093/hmg/ddac228, doi:10.1093/hmg/ddac228. This article has 24 citations and is from a domain leading peer-reviewed journal.

22. (duker2010paternallyinheritedmicrodeletion pages 1-2): Angela L Duker, Blake C Ballif, Erawati V Bawle, Richard E Person, Sangeetha Mahadevan, Sarah Alliman, Regina Thompson, Ryan Traylor, Bassem A Bejjani, Lisa G Shaffer, Jill A Rosenfeld, Allen N Lamb, and Trilochan Sahoo. Paternally inherited microdeletion at 15q11.2 confirms a significant role for the snord116 c/d box snorna cluster in prader–willi syndrome. European Journal of Human Genetics, 18:1196-1201, Jun 2010. URL: https://doi.org/10.1038/ejhg.2010.102, doi:10.1038/ejhg.2010.102. This article has 384 citations and is from a domain leading peer-reviewed journal.

23. (mendiola2024characterizingtherolea pages 16-21): AJP Mendiola. Characterizing the role of snord116 in coordinating circadian entrainment of behavior, metabolism, and gene expression in prader-willi syndrome. Unknown journal, 2024.

24. (helwak2024rolesofsnord115 pages 9-10): Aleksandra Helwak, Tomasz Turowski, Christos Spanos, and David Tollervey. Roles of snord115 and snord116 ncrna clusters during neuronal differentiation. Nature Communications, Nov 2024. URL: https://doi.org/10.1038/s41467-024-54573-8, doi:10.1038/s41467-024-54573-8. This article has 11 citations and is from a highest quality peer-reviewed journal.

25. (mendiola2024characterizingtherole pages 16-21): AJP Mendiola. Characterizing the role of snord116 in coordinating circadian entrainment of behavior, metabolism, and gene expression in prader-willi syndrome. Unknown journal, 2024.

## Citations

1. chung2020praderwillisyndromereflections pages 6-7
2. chung2020praderwillisyndromereflections pages 7-8
3. baldini2022phylogeneticandmolecular pages 3-5
4. holmes2025footprintsinthe pages 9-10
5. duker2010paternallyinheritedmicrodeletion pages 3-4
6. duker2010paternallyinheritedmicrodeletion pages 4-5
7. duker2010paternallyinheritedmicrodeletion pages 2-3
8. burnett2017lossofthe pages 1-2
9. gilmore2024identifyingkeyunderlying pages 1-2
10. sledziowska2023noncodingrnasassociated pages 4-6
11. mendiola2024characterizingtherolea pages 16-21
12. holmes2025footprintsinthe pages 2-3
13. cavaille2017boxcdsmall pages 1-3
14. holmes2025footprintsinthe pages 10-12
15. sledziowska2023noncodingrnasassociated pages 1-2
16. duker2010paternallyinheritedmicrodeletion pages 1-2
17. mendiola2024characterizingtherole pages 16-21
18. https://doi.org/10.1038/s41467-024-54573-8
19. https://doi.org/10.1093/nar/gkae1129
20. https://doi.org/10.1093/hmg/ddac228
21. https://doi.org/10.1093/nar/gks321,
22. https://doi.org/10.1038/ejhg.2010.102,
23. https://doi.org/10.1098/rsob.200195,
24. https://doi.org/10.1093/molbev/msab348,
25. https://doi.org/10.1098/rsob.240371,
26. https://doi.org/10.1002/wrna.1417,
27. https://doi.org/10.1038/s41467-024-54573-8,
28. https://doi.org/10.1093/hmg/ddx342,
29. https://doi.org/10.1093/nar/gkae1129,
30. https://doi.org/10.1093/hmg/ddac228,