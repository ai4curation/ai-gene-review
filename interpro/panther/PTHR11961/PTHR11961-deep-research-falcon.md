---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-28T20:31:50.340719'
end_time: '2026-06-28T20:54:32.568459'
duration_seconds: 1362.23
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR11961
  interpro_name: CYTOCHROME C
  interpro_short_name: Not specified
  interpro_type: family
  interpro_integrated: IPR002327
  member_databases: Not specified
  n_proteins: '16207'
  n_taxa: '14406'
  n_subfamilies: '18'
  interpro2go_terms: None mapped (no InterPro2GO terms for this entry)
  interpro_description: Not specified in InterPro
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 36
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PTHR11961-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR11961-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# InterPro Family Research for GO Annotation Review

## ⚠️ CRITICAL: Family Identification Context

**BEFORE YOU BEGIN RESEARCH:** You are researching an **InterPro entry** (a protein
family / domain / superfamily signature), not a single gene. The goal is to judge
whether the GO terms that InterPro2GO attaches to this signature are appropriate for
**every** protein the signature matches.

### Target InterPro Entry (from the InterPro API):
- **Accession:** PTHR11961
- **Name:** CYTOCHROME C
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** IPR002327
- **Member database signatures:** Not specified
- **Scale:** 16207 proteins across 14406 taxa, 18 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** Not specified in InterPro

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR11961 (CYTOCHROME C)**, structured to support GO annotation review.

Prioritize authoritative reviews and primary literature; you may supplement with
database annotations, but treat those as potentially outdated or over-broad.

Address each of the following:

1. **Family definition and biochemistry.** What does this family/domain do
   mechanistically? What fold is it? What are the conserved catalytic or binding
   residues? Cite primary/structural literature for all claims.

2. **InterPro2GO mapping appropriateness.** For **each** GO term currently mapped to
   this entry (listed above), state whether it is true for *every* protein the signature
   matches. Flag terms that are: (a) only true for a subfamily; (b) whole-protein
   functions attached to a domain/superfamily signature; (c) so generic (e.g. "ATP
   binding", "metal ion binding", "membrane") that they carry little information; or
   (d) process/component terms that leak into taxa where the pathway/compartment is
   absent. Where a more specific GO term would be correct, name it.

3. **Functional divergence across the family.** Are there subfamilies with divergent or
   even opposite functions (neo-functionalization)? Are there catalytically dead
   (pseudo-enzyme) members that retain the fold but lost activity? Identify the
   subfamilies and what distinguishes them.

4. **Taxonomic scope.** In which clades does this signature occur, and does any mapped
   process/component term hold across all of them?

5. **Over-annotation verdict.** Summarize whether InterPro2GO for this entry is sound,
   partially over-broad, or over-annotating, and give the recommended GO action pattern
   (ACCEPT / MODIFY-to-specific / KEEP_AS_NON_CORE / MARK_AS_OVER_ANNOTATED / REMOVE)
   for genes matching it. Note any recommendation for InterPro itself (e.g. demote a
   whole-protein term on a domain entry, or move it to a child entry).

Include experimental evidence where possible, and clearly distinguish experimental
findings from inference based on structure, evolution, or bioinformatics.


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

# InterPro Family Research for GO Annotation Review

## ⚠️ CRITICAL: Family Identification Context

**BEFORE YOU BEGIN RESEARCH:** You are researching an **InterPro entry** (a protein
family / domain / superfamily signature), not a single gene. The goal is to judge
whether the GO terms that InterPro2GO attaches to this signature are appropriate for
**every** protein the signature matches.

### Target InterPro Entry (from the InterPro API):
- **Accession:** PTHR11961
- **Name:** CYTOCHROME C
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** IPR002327
- **Member database signatures:** Not specified
- **Scale:** 16207 proteins across 14406 taxa, 18 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** Not specified in InterPro

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR11961 (CYTOCHROME C)**, structured to support GO annotation review.

Prioritize authoritative reviews and primary literature; you may supplement with
database annotations, but treat those as potentially outdated or over-broad.

Address each of the following:

1. **Family definition and biochemistry.** What does this family/domain do
   mechanistically? What fold is it? What are the conserved catalytic or binding
   residues? Cite primary/structural literature for all claims.

2. **InterPro2GO mapping appropriateness.** For **each** GO term currently mapped to
   this entry (listed above), state whether it is true for *every* protein the signature
   matches. Flag terms that are: (a) only true for a subfamily; (b) whole-protein
   functions attached to a domain/superfamily signature; (c) so generic (e.g. "ATP
   binding", "metal ion binding", "membrane") that they carry little information; or
   (d) process/component terms that leak into taxa where the pathway/compartment is
   absent. Where a more specific GO term would be correct, name it.

3. **Functional divergence across the family.** Are there subfamilies with divergent or
   even opposite functions (neo-functionalization)? Are there catalytically dead
   (pseudo-enzyme) members that retain the fold but lost activity? Identify the
   subfamilies and what distinguishes them.

4. **Taxonomic scope.** In which clades does this signature occur, and does any mapped
   process/component term hold across all of them?

5. **Over-annotation verdict.** Summarize whether InterPro2GO for this entry is sound,
   partially over-broad, or over-annotating, and give the recommended GO action pattern
   (ACCEPT / MODIFY-to-specific / KEEP_AS_NON_CORE / MARK_AS_OVER_ANNOTATED / REMOVE)
   for genes matching it. Note any recommendation for InterPro itself (e.g. demote a
   whole-protein term on a domain entry, or move it to a child entry).

Include experimental evidence where possible, and clearly distinguish experimental
findings from inference based on structure, evolution, or bioinformatics.


# InterPro Family Research Report: PTHR11961 (CYTOCHROME C)

## 1. Family Definition and Biochemistry

PTHR11961 is a PANTHER family-level entry for **cytochrome c**, integrated into the parent InterPro entry IPR002327. It encompasses 16,207 proteins across 14,406 taxa with 18 defined subfamilies, making it one of the most broadly distributed protein families in biology.

### Structural Features

Cytochrome c proteins share a characteristic **class I cytochrome c fold** consisting of five α-helices connected by extended omega (Ω) loops and a two-stranded antiparallel β-sheet (hannibal2016alternativeconformationsof pages 3-4, zhou2024diversefunctionsof pages 2-3). In the canonical eukaryotic somatic form, the protein is a small, highly conserved globular hemoprotein of 94–114 amino acids (104 in humans) (zhou2024diversefunctionsof pages 2-3, hannibal2016alternativeconformationsof pages 1-2).

### Conserved Residues and Heme Binding

The defining biochemical signature of the family is the **CXXCH motif**, which consists of Cys14, Cys17, and His18 (human numbering). The two cysteine residues form covalent thioether linkages to the heme c porphyrin ring, while His18 provides one axial ligand to the heme iron. Met80 serves as the second axial ligand, providing the redox potential appropriate for electron transfer (zhou2024diversefunctionsof pages 2-3, gideon2022mechanismofelectron pages 4-5). The heme moiety is largely buried within the protein structure, with only ~7.5% of its surface accessible to solvent (hannibal2016alternativeconformationsof pages 3-4). Fifteen amino acid residues are conserved throughout evolution, including Cys14, Cys17, His18, Gly29, Pro30, Gly41, Asn52, Trp59, Tyr67, Leu68, Pro71, Pro76, Thr78, Met80, and Phe82 (zhou2024diversefunctionsof pages 4-5). Surface lysine residues (Lys8, 13, 27, 72, 86, 87) facilitate electrostatic interactions with respiratory complexes (zhou2024diversefunctionsof pages 2-3, gideon2022mechanismofelectron pages 4-5).

### Primary Mechanism

In its canonical role, cytochrome c functions as a soluble one-electron carrier in the mitochondrial electron transport chain (ETC), shuttling electrons from complex III (cytochrome bc1) to complex IV (cytochrome c oxidase). The iron atom cycles between ferrous (Fe²⁺, reduced) and ferric (Fe³⁺, oxidized) states during this process (zhou2024diversefunctionsof pages 6-7). In cyanobacteria, the related cytochrome c6 performs an analogous but distinct function, transferring electrons between the cytochrome b6f complex and photosystem I (PSI) during photosynthesis, serving as a functional alternative to plastocyanin (zhang2025ahighresolutioncrystallographic pages 1-2, zhang2025ahighresolutioncrystallographic pages 10-11).

## 2. InterPro2GO Mapping Appropriateness

PTHR11961 currently has **no InterPro2GO terms mapped**. The following analysis evaluates whether any GO terms should be added at the family level and concludes that the absence of mappings is largely appropriate given the family's extreme functional heterogeneity.

The following table evaluates candidate GO terms that might theoretically be applied:

| Candidate GO Term | GO ID (approximate) | Aspect (MF/BP/CC) | True for All Members? | Risk of Over-annotation | Recommended Action |
|---|---|---|---|---|---|
| heme binding | GO:0020037 | MF | Broadly yes for bona fide c-type cytochromes in this family because covalent heme c attachment via the CXXCH motif is the defining biochemical feature, but still very generic and low-information (zhou2024diversefunctionsof pages 2-3, gideon2022mechanismofelectron pages 4-5) | Medium: chemically true but generic; may add little value if parent entry already captures heme-c chemistry | KEEP_AS_NON_CORE |
| electron carrier activity | GO:0009055 | MF | No, not safely for all members across 18 subfamilies and 14,406 taxa; many members are soluble carriers, but some lineages have diverged into specialized or unclear roles, and some multiheme forms mediate extracellular transfer in very different contexts (espinosanchez2023directtestsof pages 1-2, baquero2023extracellularcytochromenanowires pages 3-5, kletzin2015cytochromescin pages 10-11) | High: family spans mitochondrial ETC, photosynthetic transfer, archaeal/bacterial respiratory pathways, and extracellular nanowires | DO_NOT_ADD |
| electron transfer activity | GO:0009055 | MF | No, not as a single family-wide assertion for every match; electron transfer is common but mechanistically and biologically heterogeneous, and some paralogs have uncertain or noncanonical roles (espinosanchez2023directtestsof pages 1-2, espinosanchez2023directtestsof pages 8-9, baquero2023extracellularcytochromenanowires pages 3-5, zhang2025ahighresolutioncrystallographic pages 1-2) | High: likely true for many but still too broad for universal transfer to all matched proteins | DO_NOT_ADD |
| iron ion binding | GO:0005506 | MF | No as a precise annotation; these proteins bind heme iron through the prosthetic group rather than functioning as generic iron-binding proteins, so this is less specific than heme binding and can be misleading (zhou2024diversefunctionsof pages 2-3, hannibal2016alternativeconformationsof pages 1-2) | High: generic and less chemically informative than heme binding | DO_NOT_ADD |
| mitochondrial intermembrane space | GO:0005758 | CC | No; only a subset of eukaryotic mitochondrial cytochromes localize there, whereas bacterial, archaeal, plastid/photosynthetic, and extracellular cytochromes do not (zhou2024diversefunctionsof pages 6-7, kletzin2015cytochromescin pages 1-2, zhang2025ahighresolutioncrystallographic pages 1-2, baquero2023extracellularcytochromenanowires pages 3-5) | Very high: major taxonomic leakage outside mitochondria-bearing eukaryotes | DO_NOT_ADD |
| mitochondrial electron transport, cytochrome c to oxygen | GO:0006123 | BP | No; true for canonical mitochondrial cytochrome c in many eukaryotes, but false for cyanobacterial cytochrome c6, archaeal respiratory cytochromes, bacterial respiratory cytochromes, extracellular nanowires, and divergent Plasmodium cyt c-2 (zhou2024diversefunctionsof pages 2-3, espinosanchez2023directtestsof pages 8-9, kletzin2015cytochromescin pages 1-2, zhang2025ahighresolutioncrystallographic pages 1-2, baquero2023extracellularcytochromenanowires pages 3-5) | Very high: pathway/component term restricted to one functional subset | DO_NOT_ADD |
| apoptotic process | GO:0006915 | BP | No; apoptosis-related roles are animal/eukaryotic moonlighting functions and not shared across the family, especially not in bacteria/archaea/photosynthetic cytochromes (zhou2024diversefunctionsof pages 8-9, zhou2024diversefunctionsof pages 9-10, kletzin2015cytochromescin pages 1-2, zhang2025ahighresolutioncrystallographic pages 1-2) | Very high: strongly subfamily- and taxon-specific | DO_NOT_ADD |
| oxidation-reduction process | GO:0055114 | BP | Broadly yes in a very general sense for most cytochrome c proteins because they participate in redox chemistry, but it is too nonspecific and does not distinguish pathway or mechanism (zhou2024diversefunctionsof pages 2-3, baquero2023extracellularcytochromenanowires pages 3-5, kletzin2015cytochromescin pages 10-11, zhang2025ahighresolutioncrystallographic pages 1-2) | Medium-high: generic BP term with limited annotation value across a highly heterogeneous family | KEEP_AS_NON_CORE |


*Table: This table evaluates plausible GO terms for the broad PTHR11961 cytochrome c family and indicates whether any should be added at the family level. It is useful for showing that most biologically specific terms would over-annotate this highly diverse family, while only very generic chemistry-level terms are defensible.*

**Key reasoning:** The only GO terms that could defensibly be applied family-wide are extremely generic molecular function terms such as "heme binding" (GO:0020037), but these carry minimal informational value and are likely already covered by the parent entry IPR002327. Any biological process terms (mitochondrial electron transport, apoptosis, photosynthesis) or cellular component terms (mitochondrial intermembrane space) would systematically over-annotate large fractions of the 16,207 matched proteins (zhou2024diversefunctionsof pages 2-3, baquero2023extracellularcytochromenanowires pages 3-5, zhang2025ahighresolutioncrystallographic pages 1-2). Even "electron carrier activity" is not universally appropriate, given the existence of divergent paralogs with unclear or atypical function (espinosanchez2023directtestsof pages 1-2, espinosanchez2023directtestsof pages 8-9).

## 3. Functional Divergence Across the Family

The cytochrome c family exhibits profound functional divergence across its 18 subfamilies. The following table summarizes the major functional categories:

| Subfamily/Member Type | Taxonomic Distribution | Primary Function | Biological Process | Key Distinguishing Features | Heme binding GO appropriate? | Electron carrier activity GO appropriate? | Mitochondrial ETC GO appropriate? | Apoptosis GO appropriate? |
|---|---|---|---|---|---|---|---|---|
| Eukaryotic somatic cytochrome c | Animals, plants, fungi, many protists with mitochondria | Soluble monoheme electron carrier between complex III and complex IV; in many eukaryotes also moonlighting in apoptosis and other cell-death/stress pathways | Mitochondrial respiratory electron transport; in animals additionally apoptosome formation, cardiolipin peroxidation, nuclear stress functions | Canonical class I cytochrome c fold with 5 α-helices; conserved CXXCH motif and Met axial ligand; highly conserved lysine-rich interaction surface for respiratory complexes; in animals can translocate to cytosol and nucleus (zhou2024diversefunctionsof pages 2-3, zhou2024diversefunctionsof pages 4-5, hannibal2016alternativeconformationsof pages 3-4) | Yes, but generic (zhou2024diversefunctionsof pages 2-3) | Yes, core and informative (zhou2024diversefunctionsof pages 2-3, gideon2022mechanismofelectron pages 4-5) | Yes for this row only, not family-wide (zhou2024diversefunctionsof pages 2-3, zhou2024diversefunctionsof pages 6-7) | Only for animal/eukaryotic subgroups, not family-wide (zhou2024diversefunctionsof pages 8-9, zhou2024diversefunctionsof pages 9-10) |
| Divergent paralogs like *Plasmodium* cyt c-2 | Apicomplexan parasites; exemplified by *Plasmodium falciparum* cyt c-2 | Heme-binding cytochrome c paralog with unclear/divergent role; dispensable for blood-stage ETC function | Uncertain; likely lineage-specific or stage-specific role rather than canonical ETC carrier in blood stages | Retains heme-attachment motif and is hemylated, but has unusual open active site and atypical coordination/redox properties; dispensable in blood-stage parasites unlike canonical cyt c (espinosanchez2023directtestsof pages 1-2, espinosanchez2023directtestsof pages 9-10, espinosanchez2023directtestsof pages 8-9, garciaguerrero2024biogenesisofcytochromes pages 1-2) | Yes (espinosanchez2023directtestsof pages 1-2, garciaguerrero2024biogenesisofcytochromes pages 1-2) | Probably not safe family-wide for this subgroup without direct evidence for each member (espinosanchez2023directtestsof pages 1-2, espinosanchez2023directtestsof pages 8-9) | No; explicitly over-broad here (espinosanchez2023directtestsof pages 1-2, espinosanchez2023directtestsof pages 8-9) | No evidence; inappropriate (espinosanchez2023directtestsof pages 1-2, garciaguerrero2024biogenesisofcytochromes pages 1-2) |
| Cyanobacterial cytochrome c6 | Cyanobacteria; also algal plastid-associated systems under some conditions | Soluble photosynthetic electron carrier between cytochrome b6f and PSI | Photosynthetic electron transport, not mitochondrial respiration | Small monoheme c-type cytochrome with cytochrome c-like fold; functions as plastocyanin alternative; PSI docking and heme-centered electron transfer in photosynthesis (zhang2025ahighresolutioncrystallographic pages 1-2, zhang2025ahighresolutioncrystallographic pages 7-10, zhang2025ahighresolutioncrystallographic pages 2-5, zhang2025ahighresolutioncrystallographic pages 10-11) | Yes (zhang2025ahighresolutioncrystallographic pages 2-5, zhang2025ahighresolutioncrystallographic pages 10-11) | Yes (zhang2025ahighresolutioncrystallographic pages 1-2, zhang2025ahighresolutioncrystallographic pages 7-10) | No; wrong compartment/process (zhang2025ahighresolutioncrystallographic pages 1-2, zhang2025ahighresolutioncrystallographic pages 10-11) | No (zhang2025ahighresolutioncrystallographic pages 1-2, zhang2025ahighresolutioncrystallographic pages 10-11) |
| Bacterial c-type cytochromes (monoheme) | Broadly across Bacteria, including respiratory and phototrophic lineages | Periplasmic or soluble electron carriers in diverse redox chains | Respiratory electron transport, denitrification, sulfur/nitrogen metabolism, photosynthetic cyclic electron transfer in some taxa | Diverse monoheme c-type proteins sharing covalent heme c attachment but used in different pathways; examples include cytochrome c551 mediating cyclic electron transport in anoxygenic phototrophs (kletzin2015cytochromescin pages 1-2, kletzin2015cytochromescin pages 10-11) | Usually yes, but generic (kletzin2015cytochromescin pages 1-2, kletzin2015cytochromescin pages 10-11) | Often yes, but should be placed on narrower child groups when possible because pathway partners differ (kletzin2015cytochromescin pages 1-2, kletzin2015cytochromescin pages 10-11) | No, except for mitochondrion-derived eukaryotic members, so not suitable here (kletzin2015cytochromescin pages 1-2) | No (kletzin2015cytochromescin pages 1-2) |
| Prokaryotic multiheme cytochrome c / extracellular nanowires | Diverse bacteria and archaea, including metal reducers and anaerobic consortia | Long-range extracellular electron transfer via stacked hemes in filaments | Metal reduction, direct interspecies electron transfer, methane-linked and anoxic community metabolism | Multiheme architecture, filament/nanowire assembly, extracellular localization, conductive heme arrays; fundamentally different from soluble monoheme mitochondrial cytochrome c proteins (baquero2023extracellularcytochromenanowires pages 3-5, baquero2023extracellularcytochromenanowires pages 1-3, baquero2023extracellularcytochromenanowires pages 10-11, soares2024asurveyof pages 15-15) | Yes (heme c binding is central), but extremely generic (baquero2023extracellularcytochromenanowires pages 3-5, soares2024asurveyof pages 15-15) | Yes in broad sense, though often better as extracellular electron transfer-related annotations on narrower entries (baquero2023extracellularcytochromenanowires pages 3-5, baquero2023extracellularcytochromenanowires pages 1-3) | No (baquero2023extracellularcytochromenanowires pages 3-5, baquero2023extracellularcytochromenanowires pages 10-11) | No (baquero2023extracellularcytochromenanowires pages 3-5, baquero2023extracellularcytochromenanowires pages 1-3) |
| Archaeal cytochromes c | Present in several archaeal orders including Desulfurococcales, Thermoproteales, Archaeoglobales, Methanosarcinales, Halobacteriales, Thermoplasmatales; absent from some phyla such as Thaumarchaeota | Diverse electron transfer roles in archaeal energy metabolism | Nitrogen/sulfur cycling, thiosulfate oxidation, denitrification, nitrate ammonification, metal respiration, other lineage-specific bioenergetic processes | Mix of monoheme and multiheme forms; 258 predicted proteins in 54 similarity clusters across >300 archaeal proteomes, indicating strong diversification and patchy distribution (kletzin2015cytochromescin pages 1-2, kletzin2015cytochromescin pages 10-11) | Yes, but generic (kletzin2015cytochromescin pages 1-2) | Often yes at broad level, but exact pathway function varies greatly (kletzin2015cytochromescin pages 10-11) | No (kletzin2015cytochromescin pages 1-2, kletzin2015cytochromescin pages 10-11) | No (kletzin2015cytochromescin pages 1-2) |


*Table: This table summarizes major functionally distinct member types within the broad PTHR11961 cytochrome c family and evaluates whether common GO terms would be appropriate for each. It is useful for showing why family-wide GO transfer is risky despite shared heme-c binding chemistry.*

### Specific Examples of Divergence

**Eukaryotic moonlighting functions:** In animals, cytochrome c has acquired multiple non-respiratory roles. Upon release from mitochondria during apoptosis, it binds APAF1 to form the apoptosome and activate caspase-9 (zhou2024diversefunctionsof pages 8-9, zhou2024diversefunctionsof pages 9-10). It also participates in pyroptosis through pyroptosome assembly with APAF1 and CASP4/11 (zhou2024diversefunctionsof pages 9-10), exhibits peroxidase activity when interacting with cardiolipin (zhou2024diversefunctionsof pages 7-8), and translocates to the nucleus to regulate chromatin remodeling and histone chaperone SET/TAF-Iβ (zhou2024diversefunctionsof pages 8-9, zhou2024diversefunctionsof pages 3-4). These moonlighting functions are lineage-specific and absent from bacterial and archaeal members.

**Apicomplexan paralog divergence:** *Plasmodium falciparum* encodes two cytochrome c homologs: a conserved cyt c (PF3D7_1404100, ~64% identity with human) that is essential for ETC function in blood-stage parasites, and a highly divergent cyt c-2 (PF3D7_1311700, <32% identity with human) that is the most divergent eukaryotic cyt c known. While cyt c-2 retains heme binding capacity, it is fully dispensable for blood-stage growth and has an unusual open active site with penta-coordinate rather than hexa-coordinate heme iron (espinosanchez2023directtestsof pages 1-2, espinosanchez2023directtestsof pages 2-3, espinosanchez2023directtestsof pages 8-9, espinosanchez2023directtestsof pages 3-4). This cytochrome c duplication is conserved throughout Apicomplexa (espinosanchez2023directtestsof pages 9-10).

**Cyanobacterial cytochrome c6:** This ~12 kDa monoheme protein functions exclusively in photosynthetic electron transfer between the cytochrome b6f complex and PSI, not in mitochondrial respiration (zhang2025ahighresolutioncrystallographic pages 1-2, zhang2025ahighresolutioncrystallographic pages 7-10). In cyanobacteria, cyt c6 is the predominant electron carrier, while in green algae it serves as a copper-deficiency-induced alternative to plastocyanin (zhang2025ahighresolutioncrystallographic pages 1-2, zhang2025ahighresolutioncrystallographic pages 10-11).

**Extracellular cytochrome nanowires:** In bacteria (e.g., *Geobacter*) and archaea (e.g., *Pyrobaculum calidifontis*, *Archaeoglobus veneficus*), multiheme c-type cytochromes assemble into extracellular conductive filaments that mediate long-range electron transfer over micron-scale distances. These enable diverse metabolic processes including metal reduction, direct interspecies electron transfer (DIET), methane oxidation, and anaerobic photosynthesis — all fundamentally different from intracellular mitochondrial electron transfer (baquero2023extracellularcytochromenanowires pages 3-5, baquero2023extracellularcytochromenanowires pages 1-3, baquero2023extracellularcytochromenanowires pages 10-11, baquero2023extracellularcytochromenanowires pages 8-10).

**Archaeal diversity:** Analysis of >300 archaeal proteomes identified 258 predicted cytochrome c proteins organized into 54 similarity clusters, some unique to archaea. The highest diversity occurs in species with metal oxidation/reduction capabilities. Archaeal cytochromes c participate in sulfate respiration, denitrification, nitrate ammonification, thiosulfate oxidation, and anaerobic ammonium oxidation (kletzin2015cytochromescin pages 1-2, kletzin2015cytochromescin pages 10-11).

**No catalytically dead (pseudo-enzyme) members** have been specifically documented in the literature for this family, although the *Plasmodium* cyt c-2 with its atypical coordination and dispensability approaches this category functionally (espinosanchez2023directtestsof pages 1-2, espinosanchez2023directtestsof pages 8-9).

## 4. Taxonomic Scope

PTHR11961 spans all three domains of life:

- **Bacteria:** Widespread across diverse phyla, including *Pseudomonas*, *Paracoccus*, *Thermus*, *Shewanella*, *Geobacter*, and cyanobacteria. Both monoheme and multiheme forms are present. Functional roles range from periplasmic electron carriers to extracellular nanowire subunits (kletzin2015cytochromescin pages 1-2, baquero2023extracellularcytochromenanowires pages 3-5, zhang2025ahighresolutioncrystallographic pages 1-2).

- **Archaea:** Found in Desulfurococcales, Thermoproteales, Archaeoglobales, Methanosarcinales, Halobacteriales, and Thermoplasmatales (both Cren- and Euryarchaeota). Notably absent from Thaumarchaeota and other phyla (kletzin2015cytochromescin pages 1-2). Functions center on metal respiration and diverse bioenergetic pathways.

- **Eukaryotes:** Ubiquitous in mitochondria-containing organisms — animals, plants, fungi, and protists including *Plasmodium* (zhou2024diversefunctionsof pages 2-3). The human gene CYCS (cytochrome c, somatic) is essentially monomorphic, reflecting extreme sequence conservation (hannibal2016alternativeconformationsof pages 1-2). Mutations are associated with thrombocytopenia 4 and neurodegenerative disease (OpenTargets Search: -CYCS).

Given this taxonomic breadth, **no process or component term holds universally**: mitochondrial localization fails for all prokaryotes; apoptotic function fails for bacteria, archaea, plants, and fungi; photosynthetic electron transfer fails for non-cyanobacterial/non-algal lineages; and even generic "electron carrier activity" fails for divergent paralogs like *Plasmodium* cyt c-2.

## 5. Over-Annotation Verdict

### Current status: No InterPro2GO terms mapped — APPROPRIATE

The absence of InterPro2GO terms on PTHR11961 is the **correct annotation strategy** for this entry. The family is a PANTHER family-level classification encompassing 16,207 proteins across 14,406 taxa with 18 subfamilies. The functional heterogeneity is extreme, ranging from mitochondrial electron transfer to photosynthetic electron transfer to extracellular nanowire-mediated electron transfer to uncertain/divergent functions.

### Recommended GO Action Pattern

| Action | Recommendation |
|--------|---------------|
| **Overall family verdict** | **ACCEPT** current state (no InterPro2GO terms mapped) |
| Heme binding (GO:0020037) | KEEP_AS_NON_CORE if added, but better left to parent entry IPR002327 |
| Electron carrier activity (GO:0009055) | DO_NOT_ADD at family level; move to specific subfamilies |
| Mitochondrial electron transport (GO:0006123) | DO_NOT_ADD; would over-annotate prokaryotic and photosynthetic members |
| Apoptotic process (GO:0006915) | DO_NOT_ADD; lineage-specific moonlighting function |
| Mitochondrial IMS (GO:0005758) | DO_NOT_ADD; massive taxonomic leakage |

### Recommendation for InterPro

The current architecture — where PTHR11961 carries no GO terms and the parent domain entry IPR002327 may carry minimal generic annotations — is sound. GO annotations should be pushed to the **18 subfamily-level entries** where functional homogeneity is higher. For example, a subfamily containing only canonical eukaryotic somatic cytochromes c could safely receive "electron carrier activity," "mitochondrial intermembrane space," and "mitochondrial electron transport, cytochrome c to oxygen." Similarly, a cyanobacterial cyt c6 subfamily could receive "photosynthesis" and related terms. The family-level entry should remain free of process and component annotations to avoid systematic over-annotation of the >16,000 matched proteins.

References

1. (hannibal2016alternativeconformationsof pages 3-4): Luciana Hannibal, Florencia Tomasina, Daiana A. Capdevila, Verónica Demicheli, Verónica Tórtora, Damián Alvarez-Paggi, Ronald Jemmerson, Daniel H. Murgida, and Rafael Radi. Alternative conformations of cytochrome c: structure, function, and detection. Biochemistry, 55 3:407-28, Jan 2016. URL: https://doi.org/10.1021/acs.biochem.5b01385, doi:10.1021/acs.biochem.5b01385. This article has 165 citations and is from a peer-reviewed journal.

2. (zhou2024diversefunctionsof pages 2-3): Zhuan Zhou, Tasnim Arroum, Xu Luo, Rui Kang, Yong J. Lee, Daolin Tang, Maik Hüttemann, and Xinxin Song. Diverse functions of cytochrome c in cell death and disease. Cell death and differentiation, 31:387-404, Mar 2024. URL: https://doi.org/10.1038/s41418-024-01284-8, doi:10.1038/s41418-024-01284-8. This article has 185 citations and is from a domain leading peer-reviewed journal.

3. (hannibal2016alternativeconformationsof pages 1-2): Luciana Hannibal, Florencia Tomasina, Daiana A. Capdevila, Verónica Demicheli, Verónica Tórtora, Damián Alvarez-Paggi, Ronald Jemmerson, Daniel H. Murgida, and Rafael Radi. Alternative conformations of cytochrome c: structure, function, and detection. Biochemistry, 55 3:407-28, Jan 2016. URL: https://doi.org/10.1021/acs.biochem.5b01385, doi:10.1021/acs.biochem.5b01385. This article has 165 citations and is from a peer-reviewed journal.

4. (gideon2022mechanismofelectron pages 4-5): Daniel Andrew Gideon, Vijay Nirusimhan, Jesu Castin E, Karthik Sudarsha, and Kelath Murali Manoj. Mechanism of electron transfers mediated by cytochromes c and b 5 in mitochondria and endoplasmic reticulum: classical and murburn perspectives. Journal of Biomolecular Structure and Dynamics, 40:9235-9252, May 2022. URL: https://doi.org/10.1080/07391102.2021.1925154, doi:10.1080/07391102.2021.1925154. This article has 27 citations and is from a peer-reviewed journal.

5. (zhou2024diversefunctionsof pages 4-5): Zhuan Zhou, Tasnim Arroum, Xu Luo, Rui Kang, Yong J. Lee, Daolin Tang, Maik Hüttemann, and Xinxin Song. Diverse functions of cytochrome c in cell death and disease. Cell death and differentiation, 31:387-404, Mar 2024. URL: https://doi.org/10.1038/s41418-024-01284-8, doi:10.1038/s41418-024-01284-8. This article has 185 citations and is from a domain leading peer-reviewed journal.

6. (zhou2024diversefunctionsof pages 6-7): Zhuan Zhou, Tasnim Arroum, Xu Luo, Rui Kang, Yong J. Lee, Daolin Tang, Maik Hüttemann, and Xinxin Song. Diverse functions of cytochrome c in cell death and disease. Cell death and differentiation, 31:387-404, Mar 2024. URL: https://doi.org/10.1038/s41418-024-01284-8, doi:10.1038/s41418-024-01284-8. This article has 185 citations and is from a domain leading peer-reviewed journal.

7. (zhang2025ahighresolutioncrystallographic pages 1-2): Botao Zhang, Yuancong Xu, Shuwen Liu, Sixu Chen, Wencong Zhao, Zhaoyang Li, Junshuai Wang, Weijian Zhao, Heng Zhang, Yuhui Dong, Yong Gong, Wang Sheng, and Peng Cao. A high-resolution crystallographic study of cytochrome c6: structural basis for electron transfer in cyanobacterial photosynthesis. International Journal of Molecular Sciences, 26:824, Jan 2025. URL: https://doi.org/10.3390/ijms26020824, doi:10.3390/ijms26020824. This article has 6 citations.

8. (zhang2025ahighresolutioncrystallographic pages 10-11): Botao Zhang, Yuancong Xu, Shuwen Liu, Sixu Chen, Wencong Zhao, Zhaoyang Li, Junshuai Wang, Weijian Zhao, Heng Zhang, Yuhui Dong, Yong Gong, Wang Sheng, and Peng Cao. A high-resolution crystallographic study of cytochrome c6: structural basis for electron transfer in cyanobacterial photosynthesis. International Journal of Molecular Sciences, 26:824, Jan 2025. URL: https://doi.org/10.3390/ijms26020824, doi:10.3390/ijms26020824. This article has 6 citations.

9. (espinosanchez2023directtestsof pages 1-2): Tanya J. Espino-Sanchez, Henry Wienkers, Rebecca G. Marvin, Shai-anne Nalder, Aldo E. García-Guerrero, Peter E. VanNatta, Yasaman Jami-Alahmadi, Amanda Mixon Blackwell, Frank G. Whitby, James A. Wohlschlegel, Matthew T. Kieber-Emmons, Christopher P. Hill, and Paul A. Sigala. Direct tests of cytochrome c and c1 functions in the electron transport chain of malaria parasites. Proceedings of the National Academy of Sciences of the United States of America, May 2023. URL: https://doi.org/10.1073/pnas.2301047120, doi:10.1073/pnas.2301047120. This article has 20 citations and is from a highest quality peer-reviewed journal.

10. (baquero2023extracellularcytochromenanowires pages 3-5): Diana P. Baquero, Virginija Cvirkaite-Krupovic, Shengen Shawn Hu, Jessie Lynda Fields, Xing Liu, Christopher Rensing, Edward H. Egelman, Mart Krupovic, and Fengbin Wang. Extracellular cytochrome nanowires appear to be ubiquitous in prokaryotes. Cell, 186:2853-2864.e8, Jun 2023. URL: https://doi.org/10.1016/j.cell.2023.05.012, doi:10.1016/j.cell.2023.05.012. This article has 90 citations and is from a highest quality peer-reviewed journal.

11. (kletzin2015cytochromescin pages 10-11): Arnulf Kletzin, Thomas Heimerl, Jennifer Flechsler, Laura van Niftrik, Reinhard Rachel, and Andreas Klingl. Cytochromes c in archaea: distribution, maturation, cell architecture, and the special case of ignicoccus hospitalis. Frontiers in Microbiology, May 2015. URL: https://doi.org/10.3389/fmicb.2015.00439, doi:10.3389/fmicb.2015.00439. This article has 89 citations and is from a peer-reviewed journal.

12. (espinosanchez2023directtestsof pages 8-9): Tanya J. Espino-Sanchez, Henry Wienkers, Rebecca G. Marvin, Shai-anne Nalder, Aldo E. García-Guerrero, Peter E. VanNatta, Yasaman Jami-Alahmadi, Amanda Mixon Blackwell, Frank G. Whitby, James A. Wohlschlegel, Matthew T. Kieber-Emmons, Christopher P. Hill, and Paul A. Sigala. Direct tests of cytochrome c and c1 functions in the electron transport chain of malaria parasites. Proceedings of the National Academy of Sciences of the United States of America, May 2023. URL: https://doi.org/10.1073/pnas.2301047120, doi:10.1073/pnas.2301047120. This article has 20 citations and is from a highest quality peer-reviewed journal.

13. (kletzin2015cytochromescin pages 1-2): Arnulf Kletzin, Thomas Heimerl, Jennifer Flechsler, Laura van Niftrik, Reinhard Rachel, and Andreas Klingl. Cytochromes c in archaea: distribution, maturation, cell architecture, and the special case of ignicoccus hospitalis. Frontiers in Microbiology, May 2015. URL: https://doi.org/10.3389/fmicb.2015.00439, doi:10.3389/fmicb.2015.00439. This article has 89 citations and is from a peer-reviewed journal.

14. (zhou2024diversefunctionsof pages 8-9): Zhuan Zhou, Tasnim Arroum, Xu Luo, Rui Kang, Yong J. Lee, Daolin Tang, Maik Hüttemann, and Xinxin Song. Diverse functions of cytochrome c in cell death and disease. Cell death and differentiation, 31:387-404, Mar 2024. URL: https://doi.org/10.1038/s41418-024-01284-8, doi:10.1038/s41418-024-01284-8. This article has 185 citations and is from a domain leading peer-reviewed journal.

15. (zhou2024diversefunctionsof pages 9-10): Zhuan Zhou, Tasnim Arroum, Xu Luo, Rui Kang, Yong J. Lee, Daolin Tang, Maik Hüttemann, and Xinxin Song. Diverse functions of cytochrome c in cell death and disease. Cell death and differentiation, 31:387-404, Mar 2024. URL: https://doi.org/10.1038/s41418-024-01284-8, doi:10.1038/s41418-024-01284-8. This article has 185 citations and is from a domain leading peer-reviewed journal.

16. (espinosanchez2023directtestsof pages 9-10): Tanya J. Espino-Sanchez, Henry Wienkers, Rebecca G. Marvin, Shai-anne Nalder, Aldo E. García-Guerrero, Peter E. VanNatta, Yasaman Jami-Alahmadi, Amanda Mixon Blackwell, Frank G. Whitby, James A. Wohlschlegel, Matthew T. Kieber-Emmons, Christopher P. Hill, and Paul A. Sigala. Direct tests of cytochrome c and c1 functions in the electron transport chain of malaria parasites. Proceedings of the National Academy of Sciences of the United States of America, May 2023. URL: https://doi.org/10.1073/pnas.2301047120, doi:10.1073/pnas.2301047120. This article has 20 citations and is from a highest quality peer-reviewed journal.

17. (garciaguerrero2024biogenesisofcytochromes pages 1-2): Aldo E. García-Guerrero, Rebecca G. Marvin, Amanda Mixon Blackwell, and Paul A. Sigala. Biogenesis of cytochromes c and c1 in the electron transport chain of malaria parasites. ACS infectious diseases, Oct 2024. URL: https://doi.org/10.1021/acsinfecdis.4c00450, doi:10.1021/acsinfecdis.4c00450. This article has 10 citations and is from a peer-reviewed journal.

18. (zhang2025ahighresolutioncrystallographic pages 7-10): Botao Zhang, Yuancong Xu, Shuwen Liu, Sixu Chen, Wencong Zhao, Zhaoyang Li, Junshuai Wang, Weijian Zhao, Heng Zhang, Yuhui Dong, Yong Gong, Wang Sheng, and Peng Cao. A high-resolution crystallographic study of cytochrome c6: structural basis for electron transfer in cyanobacterial photosynthesis. International Journal of Molecular Sciences, 26:824, Jan 2025. URL: https://doi.org/10.3390/ijms26020824, doi:10.3390/ijms26020824. This article has 6 citations.

19. (zhang2025ahighresolutioncrystallographic pages 2-5): Botao Zhang, Yuancong Xu, Shuwen Liu, Sixu Chen, Wencong Zhao, Zhaoyang Li, Junshuai Wang, Weijian Zhao, Heng Zhang, Yuhui Dong, Yong Gong, Wang Sheng, and Peng Cao. A high-resolution crystallographic study of cytochrome c6: structural basis for electron transfer in cyanobacterial photosynthesis. International Journal of Molecular Sciences, 26:824, Jan 2025. URL: https://doi.org/10.3390/ijms26020824, doi:10.3390/ijms26020824. This article has 6 citations.

20. (baquero2023extracellularcytochromenanowires pages 1-3): Diana P. Baquero, Virginija Cvirkaite-Krupovic, Shengen Shawn Hu, Jessie Lynda Fields, Xing Liu, Christopher Rensing, Edward H. Egelman, Mart Krupovic, and Fengbin Wang. Extracellular cytochrome nanowires appear to be ubiquitous in prokaryotes. Cell, 186:2853-2864.e8, Jun 2023. URL: https://doi.org/10.1016/j.cell.2023.05.012, doi:10.1016/j.cell.2023.05.012. This article has 90 citations and is from a highest quality peer-reviewed journal.

21. (baquero2023extracellularcytochromenanowires pages 10-11): Diana P. Baquero, Virginija Cvirkaite-Krupovic, Shengen Shawn Hu, Jessie Lynda Fields, Xing Liu, Christopher Rensing, Edward H. Egelman, Mart Krupovic, and Fengbin Wang. Extracellular cytochrome nanowires appear to be ubiquitous in prokaryotes. Cell, 186:2853-2864.e8, Jun 2023. URL: https://doi.org/10.1016/j.cell.2023.05.012, doi:10.1016/j.cell.2023.05.012. This article has 90 citations and is from a highest quality peer-reviewed journal.

22. (soares2024asurveyof pages 15-15): Ricardo Soares, Bruno M. Fonseca, Benjamin W. Nash, Catarina M. Paquete, and Ricardo O. Louro. A survey of the desulfuromonadia “cytochromome” provides a glimpse of the unexplored diversity of multiheme cytochromes in nature. Oct 2024. URL: https://doi.org/10.1186/s12864-024-10872-4, doi:10.1186/s12864-024-10872-4. This article has 13 citations and is from a peer-reviewed journal.

23. (zhou2024diversefunctionsof pages 7-8): Zhuan Zhou, Tasnim Arroum, Xu Luo, Rui Kang, Yong J. Lee, Daolin Tang, Maik Hüttemann, and Xinxin Song. Diverse functions of cytochrome c in cell death and disease. Cell death and differentiation, 31:387-404, Mar 2024. URL: https://doi.org/10.1038/s41418-024-01284-8, doi:10.1038/s41418-024-01284-8. This article has 185 citations and is from a domain leading peer-reviewed journal.

24. (zhou2024diversefunctionsof pages 3-4): Zhuan Zhou, Tasnim Arroum, Xu Luo, Rui Kang, Yong J. Lee, Daolin Tang, Maik Hüttemann, and Xinxin Song. Diverse functions of cytochrome c in cell death and disease. Cell death and differentiation, 31:387-404, Mar 2024. URL: https://doi.org/10.1038/s41418-024-01284-8, doi:10.1038/s41418-024-01284-8. This article has 185 citations and is from a domain leading peer-reviewed journal.

25. (espinosanchez2023directtestsof pages 2-3): Tanya J. Espino-Sanchez, Henry Wienkers, Rebecca G. Marvin, Shai-anne Nalder, Aldo E. García-Guerrero, Peter E. VanNatta, Yasaman Jami-Alahmadi, Amanda Mixon Blackwell, Frank G. Whitby, James A. Wohlschlegel, Matthew T. Kieber-Emmons, Christopher P. Hill, and Paul A. Sigala. Direct tests of cytochrome c and c1 functions in the electron transport chain of malaria parasites. Proceedings of the National Academy of Sciences of the United States of America, May 2023. URL: https://doi.org/10.1073/pnas.2301047120, doi:10.1073/pnas.2301047120. This article has 20 citations and is from a highest quality peer-reviewed journal.

26. (espinosanchez2023directtestsof pages 3-4): Tanya J. Espino-Sanchez, Henry Wienkers, Rebecca G. Marvin, Shai-anne Nalder, Aldo E. García-Guerrero, Peter E. VanNatta, Yasaman Jami-Alahmadi, Amanda Mixon Blackwell, Frank G. Whitby, James A. Wohlschlegel, Matthew T. Kieber-Emmons, Christopher P. Hill, and Paul A. Sigala. Direct tests of cytochrome c and c1 functions in the electron transport chain of malaria parasites. Proceedings of the National Academy of Sciences of the United States of America, May 2023. URL: https://doi.org/10.1073/pnas.2301047120, doi:10.1073/pnas.2301047120. This article has 20 citations and is from a highest quality peer-reviewed journal.

27. (baquero2023extracellularcytochromenanowires pages 8-10): Diana P. Baquero, Virginija Cvirkaite-Krupovic, Shengen Shawn Hu, Jessie Lynda Fields, Xing Liu, Christopher Rensing, Edward H. Egelman, Mart Krupovic, and Fengbin Wang. Extracellular cytochrome nanowires appear to be ubiquitous in prokaryotes. Cell, 186:2853-2864.e8, Jun 2023. URL: https://doi.org/10.1016/j.cell.2023.05.012, doi:10.1016/j.cell.2023.05.012. This article has 90 citations and is from a highest quality peer-reviewed journal.

28. (OpenTargets Search: -CYCS): Open Targets Query (-CYCS, 31 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

## Artifacts

- [Edison artifact artifact-00](PTHR11961-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR11961-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. hannibal2016alternativeconformationsof pages 3-4
2. zhou2024diversefunctionsof pages 4-5
3. zhou2024diversefunctionsof pages 6-7
4. zhou2024diversefunctionsof pages 2-3
5. kletzin2015cytochromescin pages 1-2
6. kletzin2015cytochromescin pages 10-11
7. zhou2024diversefunctionsof pages 9-10
8. zhou2024diversefunctionsof pages 7-8
9. espinosanchez2023directtestsof pages 9-10
10. hannibal2016alternativeconformationsof pages 1-2
11. gideon2022mechanismofelectron pages 4-5
12. zhang2025ahighresolutioncrystallographic pages 1-2
13. zhang2025ahighresolutioncrystallographic pages 10-11
14. espinosanchez2023directtestsof pages 1-2
15. baquero2023extracellularcytochromenanowires pages 3-5
16. espinosanchez2023directtestsof pages 8-9
17. zhou2024diversefunctionsof pages 8-9
18. garciaguerrero2024biogenesisofcytochromes pages 1-2
19. zhang2025ahighresolutioncrystallographic pages 7-10
20. zhang2025ahighresolutioncrystallographic pages 2-5
21. baquero2023extracellularcytochromenanowires pages 1-3
22. baquero2023extracellularcytochromenanowires pages 10-11
23. soares2024asurveyof pages 15-15
24. zhou2024diversefunctionsof pages 3-4
25. espinosanchez2023directtestsof pages 2-3
26. espinosanchez2023directtestsof pages 3-4
27. baquero2023extracellularcytochromenanowires pages 8-10
28. https://doi.org/10.1021/acs.biochem.5b01385,
29. https://doi.org/10.1038/s41418-024-01284-8,
30. https://doi.org/10.1080/07391102.2021.1925154,
31. https://doi.org/10.3390/ijms26020824,
32. https://doi.org/10.1073/pnas.2301047120,
33. https://doi.org/10.1016/j.cell.2023.05.012,
34. https://doi.org/10.3389/fmicb.2015.00439,
35. https://doi.org/10.1021/acsinfecdis.4c00450,
36. https://doi.org/10.1186/s12864-024-10872-4,