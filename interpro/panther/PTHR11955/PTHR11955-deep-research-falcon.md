---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-28T20:28:52.438632'
end_time: '2026-06-28T20:47:15.363808'
duration_seconds: 1102.93
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR11955
  interpro_name: FATTY ACID BINDING PROTEIN
  interpro_short_name: Not specified
  interpro_type: family
  interpro_integrated: IPR031259
  member_databases: Not specified
  n_proteins: '17946'
  n_taxa: '4599'
  n_subfamilies: '34'
  interpro2go_terms: None mapped (no InterPro2GO terms for this entry)
  interpro_description: Not specified in InterPro
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 27
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PTHR11955-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR11955-deep-research-falcon_artifacts/artifact-01.md
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
- **Accession:** PTHR11955
- **Name:** FATTY ACID BINDING PROTEIN
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** IPR031259
- **Member database signatures:** Not specified
- **Scale:** 17946 proteins across 4599 taxa, 34 subfamilies
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
**PTHR11955 (FATTY ACID BINDING PROTEIN)**, structured to support GO annotation review.

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
- **Accession:** PTHR11955
- **Name:** FATTY ACID BINDING PROTEIN
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** IPR031259
- **Member database signatures:** Not specified
- **Scale:** 17946 proteins across 4599 taxa, 34 subfamilies
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
**PTHR11955 (FATTY ACID BINDING PROTEIN)**, structured to support GO annotation review.

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


# InterPro Family Research Report: PTHR11955 — FATTY ACID BINDING PROTEIN

## 1. Family Definition and Biochemistry

### Structural Fold and Architecture

PTHR11955 (FATTY ACID BINDING PROTEIN) is a PANTHER family-level entry within the broader intracellular lipid-binding protein (iLBP) superfamily (parent: IPR031259). The FABP family is defined by a highly conserved tertiary structure consisting of a slightly elliptical β-barrel composed of ten anti-parallel β-strands arranged as two nearly orthogonal five-stranded β-sheets, surrounding a solvent-accessible ligand-binding cavity of approximately 500 Å³ (bodnariuc2021examinationofbrainfatty pages 16-20, storch2023themultifunctionalfamily pages 1-3). The barrel is capped at one end by a small helix-turn-helix motif consisting of two short α-helices (αI and αII), which forms a dynamic "portal region" that gates ligand entry and exit (agellon2024importanceoffatty pages 2-4, storch2023themultifunctionalfamily pages 1-3).

Despite low primary sequence identity across family members (20–70%), the tertiary fold is remarkably conserved across all FABP types (storch2023themultifunctionalfamily pages 1-3). FABPs are small proteins of 126–134 amino acid residues and belong to the calycin protein superfamily (storch2023themultifunctionalfamily pages 1-3, agellon2024importanceoffatty pages 1-2). The barrel's outer surface is lined with hydrophilic sidechains while the interior is lined with hydrophobic sidechains, both of which vary among different FABP types (agellon2024importanceoffatty pages 2-4).

### Conserved Binding Residues and Mechanism

The ligand-binding mechanism involves conformational changes in the portal region. In the unliganded (apo) state, the αII helix and turns between β-strands C–D and E–F are disordered and flexible, adopting an "open" configuration; upon fatty acid binding, these regions become stabilized in a "closed" configuration through transient local unfolding of the αII helix that creates a temporary opening permitting ligand passage (agellon2024importanceoffatty pages 2-4, storch2023themultifunctionalfamily pages 1-3, storch2023themultifunctionalfamily pages 3-4). Key conserved residues for fatty acid coordination include R126 and Y128 (numbered by FABP7), which form hydrogen bonds with the carboxylate head group of fatty acids within the binding cavity (bodnariuc2021examinationofbrainfatty pages 16-20). The binding cavity interior contains approximately 43 side chains arranged in three functional zones: a hydrophobic bottom section, a middle section enriched in hydrophilic and ionizable groups, and a mixed-residue region near the portal (ibanezshimabukuro2019structureandligand pages 8-9).

Most FABP types bind a single ligand molecule with 1:1 stoichiometry, but FABP1 and FABP6 possess larger cavities that accommodate two ligand molecules simultaneously (2:1 stoichiometry) (storch2023themultifunctionalfamily pages 3-4).

### Relationship to the iLBP Superfamily

The FABP family sits within the broader iLBP superfamily, which is classified into four subfamilies based on ligand-binding preferences: Subfamily I contains cellular retinol-binding proteins (CRBPs) and cellular retinoic acid-binding proteins (CRABPs); Subfamily II contains FABP1 and FABP6; Subfamily III contains FABP2 alone; and Subfamily IV, the largest, includes FABP3–5, FABP7–9, and FABP12 (kakouratos2025theroleof pages 2-4, kakouratos2025theroleof pages 4-6). This classification underscores that even within the FABP label, there are structurally and functionally distinct lineages.

---

## 2. InterPro2GO Mapping Appropriateness

### Current State

PTHR11955 currently has **no InterPro2GO mappings**. This absence is evaluated below against candidate GO terms to determine whether any should be added.

The following table assesses the appropriateness of plausible GO terms for family-level mapping:

| Candidate GO term | GO ID | GO aspect (MF/BP/CC) | Applies to all members? | Problem if mapped at family level | Recommendation |
|---|---|---|---|---|---|
| fatty acid binding | GO:0005504 | MF | No | Over-broad for the family: FABP6 preferentially binds bile acids rather than canonical fatty acids, and FABP8/PMP2 has divergent phosphoinositide-binding biology; family-wide mapping would misstate ligand specificity for substantial subgroups (storch2023themultifunctionalfamily pages 14-16, storch2023themultifunctionalfamily pages 3-4, storch2023themultifunctionalfamily pages 17-19, agellon2024importanceoffatty pages 2-4) | **DO NOT MAP** at family level |
| lipid binding | GO:0008289 | MF | Mostly yes | Likely broadly true across FABPs, but too generic to be very informative and obscures important divergence in ligand class (fatty acids, bile acids, phosphoinositides, heme, endocannabinoids) (storch2023themultifunctionalfamily pages 3-4, storch2023themultifunctionalfamily pages 17-19, agellon2024importanceoffatty pages 4-5, kakouratos2025theroleof pages 4-6) | **COULD MAP** but low information value; better kept off broad family and used only if no more specific child-level term is possible |
| lipid transport | GO:0006869 | BP | No | Not all members are best characterized as transporters: some act in signaling or membrane organization, FABP4 can function as a secreted adipokine/hormone, and FABP8 regulates sphingomyelin distribution rather than generic lipid transport (storch2023themultifunctionalfamily pages 17-19, agellon2024importanceoffatty pages 4-5, storch2023themultifunctionalfamily pages 16-17, storch2023themultifunctionalfamily pages 12-14) | **DO NOT MAP** |
| fatty acid metabolic process | GO:0006631 | BP | No | This is a process term that overreaches from binding/chaperoning proteins to pathway participation; FABP6 is specialized for bile acid handling, while other members have roles in neurobiology, signaling, or extracellular hormone-like activity rather than a universal fatty acid metabolic process (storch2023themultifunctionalfamily pages 14-16, agellon2024importanceoffatty pages 4-5, storch2023themultifunctionalfamily pages 1-3) | **DO NOT MAP** |
| cytoplasm | GO:0005737 | CC | Mostly yes | Many FABPs are abundant cytosolic proteins, but not all are confined there: FABP4 is secreted/exosomal, some FABPs translocate to the nucleus, and nematode FABPs include extracellular forms (xu2022thebiologicalfunctions pages 1-2, agellon2024importanceoffatty pages 4-5, storch2023themultifunctionalfamily pages 12-14, storch2023themultifunctionalfamily pages 1-3, ibanezshimabukuro2019structureandligand pages 8-9) | **DO NOT MAP** at family level |
| intracellular | GO:0005622 | CC | Mostly but not all | Too broad and still not universal: extracellular/secreted FABP4 and secreted nematode FABPs violate a universal intracellular assignment; additionally, this CC term is extremely generic (xu2022thebiologicalfunctions pages 1-2, storch2023themultifunctionalfamily pages 12-14, storch2023themultifunctionalfamily pages 1-3, ibanezshimabukuro2019structureandligand pages 8-9) | **DO NOT MAP** at family level |


*Table: This table evaluates plausible GO terms for the broad PTHR11955 fatty acid binding protein family and explains why most are unsafe at family level. It is useful for GO review because it distinguishes terms that are merely generic from those that would clearly over-annotate divergent FABP subfamilies.*

### Analysis

The absence of GO mappings at the PTHR11955 level is well-justified. The most ostensibly appropriate term, "fatty acid binding" (GO:0005504), is violated by FABP6, which preferentially binds bile acids (cholate and chenodeoxycholate) rather than fatty acids (storch2023themultifunctionalfamily pages 14-16), and by FABP8, which has diverged to bind phosphoinositides (PI(4,5)P2) and controls sphingomyelin transbilayer movement (storch2023themultifunctionalfamily pages 17-19, storch2023themultifunctionalfamily pages 16-17). A broader "lipid binding" (GO:0008289) term would be closer to universally correct, but it is so generic that its annotation value is minimal. Process terms such as "lipid transport" or "fatty acid metabolic process" are clearly subfamily-specific and would over-annotate the diverse functional repertoire. Cellular component terms such as "cytoplasm" are undermined by the well-documented secretion of FABP4 as a circulating adipokine/hormone (storch2023themultifunctionalfamily pages 12-14, storch2023themultifunctionalfamily pages 1-3) and the existence of extracellular nematode FABPs (nemFABPs) (ibanezshimabukuro2019structureandligand pages 8-9).

---

## 3. Functional Divergence Across the Family

### Overview of Subfamily Divergence

The FABP family exhibits extensive functional divergence, as summarized below:

| FABP type | Primary tissue expression | Primary ligands | Unique functional features | Subcellular localization |
|---|---|---|---|---|
| FABP1 | Liver; also small-intestinal enterocytes and renal proximal tubules | Long-chain fatty acids; bile acids; lysophospholipids; cholesterol; heme; monoacylglycerols; binds 2 ligands/protein | Largest binding cavity in family; unique 2:1 ligand stoichiometry; ligand-selective modulation of PPARα signaling; functionally distinct from FABP2 despite overlap in intestinal expression (storch2023themultifunctionalfamily pages 6-8, storch2023themultifunctionalfamily pages 3-4) | Predominantly cytosolic; can translocate to nucleus in a ligand-dependent manner; also associated with lipid transport vesicles (agellon2024importanceoffatty pages 4-5, storch2023themultifunctionalfamily pages 3-4) |
| FABP2 | Small intestine, especially jejunum | Saturated and other long-chain fatty acids; endocannabinoids | Nutrient absorption and lipid sensing; reduced weight gain and increased fecal loss in KO mice; functionally distinct from FABP1 in whole-body energy homeostasis (storch2023themultifunctionalfamily pages 6-8, storch2023themultifunctionalfamily pages 8-9, kakouratos2025theroleof pages 4-6) | Primarily cytosolic in enterocytes; targets ligands to intracellular destinations (storch2023themultifunctionalfamily pages 3-4) |
| FABP3 | Heart and skeletal muscle; lower expression in stomach, brain, lung, placenta, immune cells | Saturated and unsaturated long-chain fatty acids; oxygenated eicosanoids; endocannabinoids | Major cardiac cytosolic FABP; roles in cardiac metabolism, neurodegeneration-related α-synuclein biology, immune differentiation; reported growth inhibitor activity (storch2023themultifunctionalfamily pages 8-9, agellon2024importanceoffatty pages 4-5) | Cytosolic; also interacts with membrane transport machinery and other intracellular targets (agellon2024importanceoffatty pages 4-5, xu2022thebiologicalfunctions pages 1-2) |
| FABP4 | Adipocytes and macrophages; also endothelial contribution to circulating pool | Long-chain fatty acids | Secreted adipokine/hormone; links obesity, inflammation, insulin secretion, and cancer; stimulates cell proliferation; extracellular receptor-mediated signaling documented (agellon2024importanceoffatty pages 4-5, storch2023themultifunctionalfamily pages 12-14) | Cytosolic, exosomal, and extracellular/circulating (storch2023themultifunctionalfamily pages 12-14, storch2023themultifunctionalfamily pages 1-3) |
| FABP5 | Epidermis and widely distributed in multiple tissues | Long-chain fatty acids; retinoic acid-related ligands; endocannabinoids (AEA, 2-AG) | Ligand-dependent nuclear translocation to PPARs; roles in endocannabinoid signaling, hypoxia responses, cancer biology, and ER-to-Golgi trafficking (storch2023themultifunctionalfamily pages 14-16, agellon2024importanceoffatty pages 4-5, storch2023themultifunctionalfamily pages 12-14) | Cytosolic; nucleus; ER/Golgi-associated secretory pathway; extracellular/autocrine-paracrine contexts reported (xu2022thebiologicalfunctions pages 1-2, storch2023themultifunctionalfamily pages 12-14) |
| FABP6 | Distal small intestine/ileum; also ovary in some contexts | Bile acids, especially cholate and chenodeoxycholate; can bind 2 ligands | Clear functional divergence from canonical fatty-acid-binding role; key in enterohepatic bile acid circulation; contributes to bile-acid signaling via FXR/TGR5 (storch2023themultifunctionalfamily pages 14-16, storch2023themultifunctionalfamily pages 3-4) | Predominantly cytosolic; functionally coupled to bile salt transport systems (agellon2024importanceoffatty pages 4-5, agellon2024importanceoffatty pages 1-2) |
| FABP7 | Brain glial cells, especially astrocytes and microglia | Polyunsaturated fatty acids, especially DHA; also endocannabinoids | Roles in hippocampal neurogenesis, blood-brain barrier maintenance, sleep and pain regulation; interacts with α-synuclein and other signaling partners (storch2023themultifunctionalfamily pages 14-16, storch2023themultifunctionalfamily pages 16-17) | Cytosolic; can contribute to nuclear lipid signaling depending on ligand context (storch2023themultifunctionalfamily pages 14-16, storch2023themultifunctionalfamily pages 17-19) |
| FABP8 (PMP2) | Peripheral myelin/nervous tissue | Phosphoinositides, especially PI(4,5)P2 | Strongly divergent ligand preference; controls transbilayer movement of sphingomyelin; implicated in myelination defects (agellon2024importanceoffatty pages 2-4, storch2023themultifunctionalfamily pages 17-19, storch2023themultifunctionalfamily pages 16-17) | Myelin-associated; interacts with plasma membrane lipids rather than being only soluble cytosolic carrier (storch2023themultifunctionalfamily pages 16-17, storch2023themultifunctionalfamily pages 17-19) |
| FABP9 | Testicular germ cells during spermiogenesis | Lipid ligands not well resolved in gathered evidence | Highly tissue-restricted; specialized role in sperm development/spermiogenesis (storch2023themultifunctionalfamily pages 17-19) | Perforatorium and perinuclear theca in sperm cells (storch2023themultifunctionalfamily pages 17-19) |
| FABP10 | Mainly non-mammalian vertebrates (e.g., fish); not established as a mammalian FABP in gathered evidence | Fatty-acid-related ligands inferred from family membership, but no direct mammalian evidence gathered | Present in broader vertebrate FABP evolution but not part of the canonical mammalian set discussed in recent reviews; should not be generalized to human/mammalian annotations without lineage-specific evidence (zhang2020tracingtheevolution pages 9-10, zhang2020tracingtheevolution pages 3-4, zhang2020tracingtheevolution pages 2-3) | Not established for mammals in gathered evidence (zhang2020tracingtheevolution pages 9-10, zhang2020tracingtheevolution pages 3-4) |
| FABP11 | Teleost-specific in gathered evidence; not established as a mammalian FABP | Not established in gathered evidence | Evolutionarily present in teleosts; absent from canonical mammalian FABP complement in recent reviews (zhang2020tracingtheevolution pages 3-4, zhang2020tracingtheevolution pages 2-3) | Not established for mammals in gathered evidence (zhang2020tracingtheevolution pages 3-4, zhang2020tracingtheevolution pages 2-3) |
| FABP12 | Retina and testis | Lipid ligands not well resolved in gathered evidence | Recently discovered member; retina/testis expression suggests specialized roles distinct from other FABPs (agellon2024importanceoffatty pages 2-4, storch2023themultifunctionalfamily pages 17-19) | Likely intracellular, but specific subcellular localization not resolved in gathered evidence (storch2023themultifunctionalfamily pages 17-19, agellon2024importanceoffatty pages 1-2) |


*Table: This table summarizes functional divergence across the FABP family, highlighting differences in tissue expression, ligand preference, specialized biology, and localization. It is useful for assessing why broad family-level GO annotation is risky and why many functions are only valid for specific FABP subtypes.*

### Key Examples of Neo-functionalization

**FABP6 (ileal bile acid-binding protein):** This member has functionally diverged from canonical fatty acid binding to specialize in bile acid transport, showing high affinity and selectivity for cholate and chenodeoxycholate, and functioning in enterohepatic circulation via interactions with bile salt transporters, FXR, and TGR5 receptors (storch2023themultifunctionalfamily pages 14-16).

**FABP8 (peripheral myelin protein 2, PMP2):** This member has diverged to bind phosphoinositides, specifically PI(4,5)P2, and controls sphingomyelin transbilayer movement in the plasma membrane. The I43N mutant increases PI(4,5)P2 affinity and is associated with myelination defects, representing a unique membrane-organizing function not shared by other FABPs (storch2023themultifunctionalfamily pages 17-19, storch2023themultifunctionalfamily pages 16-17).

**FABP4 as a secreted hormone:** Although traditionally considered an intracellular chaperone, FABP4 is now established as a bona fide secreted adipokine/hormone. Endothelial cells contribute ~75% of basal circulating FABP4, while adipocytes contribute during lipolysis. Extracellular FABP4 signals through desmoglein 2 receptors to promote cancer cell proliferation and regulate insulin secretion (storch2023themultifunctionalfamily pages 12-14, storch2023themultifunctionalfamily pages 1-3).

**FABP7 in neuronal biology:** FABP7 binds polyunsaturated fatty acids (especially DHA), interacts with α-synuclein to modulate its aggregation, interacts with ATP-citrate lyase and sortilin, and plays roles in hippocampal neurogenesis, blood-brain barrier maintenance, sleep regulation, and pain perception—functions highly specific to neural contexts (storch2023themultifunctionalfamily pages 14-16, storch2023themultifunctionalfamily pages 16-17).

**Opposing growth effects:** FABP3 acts as a growth inhibitor while FABP4 stimulates cell proliferation, representing opposite biological effects within the same protein family (agellon2024importanceoffatty pages 4-5).

### Pseudo-enzyme Considerations

FABPs are not enzymes (they are ligand-binding chaperones), so the concept of "catalytically dead" members does not directly apply. However, the radical divergence in ligand specificity (from fatty acids to bile acids to phosphoinositides) and the acquisition of extracellular signaling functions represent analogous neo-functionalization phenomena. Storch and Corsico (2023) explicitly note that "different FABP members lack apparent common functions and mechanisms of action," indicating that the family is functionally heterogeneous by expert consensus (storch2023themultifunctionalfamily pages 17-19).

---

## 4. Taxonomic Scope

### Distribution Across Animal Clades

FABPs are animal-specific proteins that evolved approximately 1 billion years ago, after the divergence of animals from plants and fungi (storch2023themultifunctionalfamily pages 1-3). The family is not found in plants, fungi, or bacteria. FABP genes are present across both invertebrate and vertebrate Metazoa:

- **Mammals:** 10 FABP types (FABP1–9, FABP12) (storch2023themultifunctionalfamily pages 1-3)
- **Birds (chicken):** 9 types (zhang2020tracingtheevolution pages 9-10)
- **Amphibians (Xenopus):** 8 types (zhang2020tracingtheevolution pages 9-10)
- **Reptiles (anole lizard):** 8 types (zhang2020tracingtheevolution pages 9-10)
- **Teleost fish:** 7 types, plus fish-specific types (FABP10, FABP11) arising from whole-genome duplication (zhang2020tracingtheevolution pages 9-10, zhang2020tracingtheevolution pages 3-4)
- **Cartilaginous fish (shark):** 5 types (zhang2020tracingtheevolution pages 9-10)
- **Tunicates (Ciona):** 5 FABP genes (zhang2020tracingtheevolution pages 3-4, zhang2020tracingtheevolution pages 2-3)
- **Nematodes (C. elegans):** 5 types, including secreted extracellular forms (nemFABPs) (zhang2020tracingtheevolution pages 9-10, ibanezshimabukuro2019structureandligand pages 8-9)
- **Insects (Drosophila):** 1 type (zhang2020tracingtheevolution pages 9-10)
- **Helminths/parasitic flatworms:** Multiple FABP family members documented in tapeworms and flukes (ibanezshimabukuro2019structureandligand pages 8-9)
- **Placozoans:** FABP orthologs present, representing the most basally branching animals with these proteins (agellon2024importanceoffatty pages 2-4, agellon2024importanceoffatty pages 1-2)

No single organism possesses all 12 FABP types (zhang2020tracingtheevolution pages 1-2). Phylogenetic analysis reveals two major clades—one containing FABP1/FABP6/FABP10 and another containing FABP2/FABP3/FABP4/FABP5/FABP7/FABP8/FABP9/FABP11/FABP12—suggesting that the primary divergence predates the vertebrate/invertebrate split (zhang2020tracingtheevolution pages 9-10).

### Implications for GO Annotation

The 17,946 proteins and 4,599 taxa matched by PTHR11955 span an enormous taxonomic range from placozoans to humans, encompassing both intracellular and extracellular members, fatty acid binders and bile acid binders, cytoplasmic chaperones and secreted hormones. No single GO Biological Process or Cellular Component term holds universally across this range.

---

## 5. Over-Annotation Verdict

### Summary Assessment

The current state of PTHR11955—having **no InterPro2GO mappings**—is **appropriate and sound** for a family of this functional heterogeneity and taxonomic breadth. The family is of entry type "family" (not domain or superfamily), which in principle could support whole-protein function annotations; however, the FABP family is emphatically *not* functionally homogeneous.

**Key reasons the absence of GO mappings is correct:**

1. **Ligand specificity is not uniform:** FABP6 binds bile acids, FABP8 binds phosphoinositides, FABP1 binds heme/cholesterol/bile salts in addition to fatty acids—"fatty acid binding" would over-annotate (agellon2024importanceoffatty pages 2-4, storch2023themultifunctionalfamily pages 14-16, storch2023themultifunctionalfamily pages 3-4, storch2023themultifunctionalfamily pages 17-19).
2. **Subcellular localization varies:** Most FABPs are cytosolic, but FABP4 is a secreted circulating hormone, nematode FABPs include extracellular forms, and multiple FABPs undergo ligand-dependent nuclear translocation—"cytoplasm" would over-annotate (xu2022thebiologicalfunctions pages 1-2, agellon2024importanceoffatty pages 4-5, storch2023themultifunctionalfamily pages 12-14, ibanezshimabukuro2019structureandligand pages 8-9).
3. **Biological processes diverge radically:** From cardiac metabolism (FABP3) to bile acid enterohepatic circulation (FABP6) to neurogenesis and sleep regulation (FABP7) to sphingomyelin membrane organization (FABP8) to adipokine signaling (FABP4)—no single process term applies universally (storch2023themultifunctionalfamily pages 17-19, storch2023themultifunctionalfamily pages 14-16, storch2023themultifunctionalfamily pages 8-9, agellon2024importanceoffatty pages 4-5).
4. **The 34 subfamilies represent genuine functional partitions:** GO terms should be applied at the PTHR11955 child/subfamily level rather than the family level.

### Recommended GO Action Pattern

| Aspect | Recommendation | Rationale |
|--------|---------------|-----------|
| Current no-mapping state | **ACCEPT** | The absence of GO terms at this family level is the correct outcome given functional heterogeneity |
| "lipid binding" (GO:0008289) | **KEEP_AS_NON_CORE** | Could theoretically be added but carries minimal information value; better delegated to subfamilies |
| "fatty acid binding" (GO:0005504) | **DO NOT ADD** | Would over-annotate FABP6 (bile acid) and FABP8 (phosphoinositide) members |
| Process/Component terms | **DO NOT ADD** | All candidate terms are subfamily-specific |
| Recommendation for InterPro | **Move specific GO terms to child entries** corresponding to individual FABP subtypes (e.g., FABP1, FABP6, FABP7 subfamilies), where ligand and function are well-defined |

In conclusion, PTHR11955 is a structurally coherent but functionally heterogeneous family. The current absence of InterPro2GO mappings correctly reflects the impossibility of assigning any single molecular function, biological process, or cellular component term that would be accurate for all 17,946 matched proteins across 34 subfamilies and 4,599 taxa. GO annotation should be pushed down to the subfamily level where specific FABP types share demonstrably conserved functions.

References

1. (bodnariuc2021examinationofbrainfatty pages 16-20): Iulia Bodnariuc. Examination of brain-fatty acid binding protein interaction with hydrophobic ligands and micelles. ArXiv, May 2021. URL: https://doi.org/10.11575/prism/38871, doi:10.11575/prism/38871. This article has 0 citations.

2. (storch2023themultifunctionalfamily pages 1-3): Judith Storch and Betina Corsico. The multifunctional family of mammalian fatty acid–binding proteins. Annual Review of Nutrition, 43:25-54, Aug 2023. URL: https://doi.org/10.1146/annurev-nutr-062220-112240, doi:10.1146/annurev-nutr-062220-112240. This article has 73 citations and is from a highest quality peer-reviewed journal.

3. (agellon2024importanceoffatty pages 2-4): Luis B. Agellon. Importance of fatty acid binding proteins in cellular function and organismal metabolism. Journal of Cellular and Molecular Medicine, Mar 2024. URL: https://doi.org/10.1111/jcmm.17703, doi:10.1111/jcmm.17703. This article has 30 citations and is from a peer-reviewed journal.

4. (agellon2024importanceoffatty pages 1-2): Luis B. Agellon. Importance of fatty acid binding proteins in cellular function and organismal metabolism. Journal of Cellular and Molecular Medicine, Mar 2024. URL: https://doi.org/10.1111/jcmm.17703, doi:10.1111/jcmm.17703. This article has 30 citations and is from a peer-reviewed journal.

5. (storch2023themultifunctionalfamily pages 3-4): Judith Storch and Betina Corsico. The multifunctional family of mammalian fatty acid–binding proteins. Annual Review of Nutrition, 43:25-54, Aug 2023. URL: https://doi.org/10.1146/annurev-nutr-062220-112240, doi:10.1146/annurev-nutr-062220-112240. This article has 73 citations and is from a highest quality peer-reviewed journal.

6. (ibanezshimabukuro2019structureandligand pages 8-9): Marina Ibáñez-Shimabukuro, M. Florencia Rey-Burusco, Mads Gabrielsen, Gisela R. Franchini, Alan Riboldi-Tunnicliffe, Andrew J. Roe, Kate Griffiths, Alan Cooper, Betina Córsico, Malcolm W. Kennedy, and Brian O. Smith. Structure and ligand binding of as-p18, an extracellular fatty acid binding protein from the eggs of a parasitic nematode. Bioscience Reports, Jul 2019. URL: https://doi.org/10.1042/bsr20191292, doi:10.1042/bsr20191292. This article has 14 citations and is from a peer-reviewed journal.

7. (kakouratos2025theroleof pages 2-4): Christos Kakouratos, Adriana Fernandez Garcia, Pramod Darvin, and Hemant M. Kocher. The role of intracellular lipid-binding proteins in digestive system neoplasms. Current Oncology, 32:531, Sep 2025. URL: https://doi.org/10.3390/curroncol32100531, doi:10.3390/curroncol32100531. This article has 0 citations.

8. (kakouratos2025theroleof pages 4-6): Christos Kakouratos, Adriana Fernandez Garcia, Pramod Darvin, and Hemant M. Kocher. The role of intracellular lipid-binding proteins in digestive system neoplasms. Current Oncology, 32:531, Sep 2025. URL: https://doi.org/10.3390/curroncol32100531, doi:10.3390/curroncol32100531. This article has 0 citations.

9. (storch2023themultifunctionalfamily pages 14-16): Judith Storch and Betina Corsico. The multifunctional family of mammalian fatty acid–binding proteins. Annual Review of Nutrition, 43:25-54, Aug 2023. URL: https://doi.org/10.1146/annurev-nutr-062220-112240, doi:10.1146/annurev-nutr-062220-112240. This article has 73 citations and is from a highest quality peer-reviewed journal.

10. (storch2023themultifunctionalfamily pages 17-19): Judith Storch and Betina Corsico. The multifunctional family of mammalian fatty acid–binding proteins. Annual Review of Nutrition, 43:25-54, Aug 2023. URL: https://doi.org/10.1146/annurev-nutr-062220-112240, doi:10.1146/annurev-nutr-062220-112240. This article has 73 citations and is from a highest quality peer-reviewed journal.

11. (agellon2024importanceoffatty pages 4-5): Luis B. Agellon. Importance of fatty acid binding proteins in cellular function and organismal metabolism. Journal of Cellular and Molecular Medicine, Mar 2024. URL: https://doi.org/10.1111/jcmm.17703, doi:10.1111/jcmm.17703. This article has 30 citations and is from a peer-reviewed journal.

12. (storch2023themultifunctionalfamily pages 16-17): Judith Storch and Betina Corsico. The multifunctional family of mammalian fatty acid–binding proteins. Annual Review of Nutrition, 43:25-54, Aug 2023. URL: https://doi.org/10.1146/annurev-nutr-062220-112240, doi:10.1146/annurev-nutr-062220-112240. This article has 73 citations and is from a highest quality peer-reviewed journal.

13. (storch2023themultifunctionalfamily pages 12-14): Judith Storch and Betina Corsico. The multifunctional family of mammalian fatty acid–binding proteins. Annual Review of Nutrition, 43:25-54, Aug 2023. URL: https://doi.org/10.1146/annurev-nutr-062220-112240, doi:10.1146/annurev-nutr-062220-112240. This article has 73 citations and is from a highest quality peer-reviewed journal.

14. (xu2022thebiologicalfunctions pages 1-2): Binyue Xu, Lu Chen, Yu Zhan, Karl Nelson S. Marquez, Lvjia Zhuo, Shasha Qi, Jinyu Zhu, Ying He, Xudong Chen, Hao Zhang, Yingying Shen, Gongxing Chen, Jianzhong Gu, Yong Guo, Shuiping Liu, and Tian Xie. The biological functions and regulatory mechanisms of fatty acid binding protein 5 in various diseases. Frontiers in Cell and Developmental Biology, Apr 2022. URL: https://doi.org/10.3389/fcell.2022.857919, doi:10.3389/fcell.2022.857919. This article has 108 citations.

15. (storch2023themultifunctionalfamily pages 6-8): Judith Storch and Betina Corsico. The multifunctional family of mammalian fatty acid–binding proteins. Annual Review of Nutrition, 43:25-54, Aug 2023. URL: https://doi.org/10.1146/annurev-nutr-062220-112240, doi:10.1146/annurev-nutr-062220-112240. This article has 73 citations and is from a highest quality peer-reviewed journal.

16. (storch2023themultifunctionalfamily pages 8-9): Judith Storch and Betina Corsico. The multifunctional family of mammalian fatty acid–binding proteins. Annual Review of Nutrition, 43:25-54, Aug 2023. URL: https://doi.org/10.1146/annurev-nutr-062220-112240, doi:10.1146/annurev-nutr-062220-112240. This article has 73 citations and is from a highest quality peer-reviewed journal.

17. (zhang2020tracingtheevolution pages 9-10): Yuru Zhang, Junmei Zhang, Yanhua Ren, Ronghua Lu, Liping Yang, and Guoxing Nie. Tracing the evolution of fatty acid‐binding proteins (fabps) in organisms with a heterogeneous fat distribution. FEBS Open Bio, 10:861-872, Mar 2020. URL: https://doi.org/10.1002/2211-5463.12840, doi:10.1002/2211-5463.12840. This article has 36 citations and is from a peer-reviewed journal.

18. (zhang2020tracingtheevolution pages 3-4): Yuru Zhang, Junmei Zhang, Yanhua Ren, Ronghua Lu, Liping Yang, and Guoxing Nie. Tracing the evolution of fatty acid‐binding proteins (fabps) in organisms with a heterogeneous fat distribution. FEBS Open Bio, 10:861-872, Mar 2020. URL: https://doi.org/10.1002/2211-5463.12840, doi:10.1002/2211-5463.12840. This article has 36 citations and is from a peer-reviewed journal.

19. (zhang2020tracingtheevolution pages 2-3): Yuru Zhang, Junmei Zhang, Yanhua Ren, Ronghua Lu, Liping Yang, and Guoxing Nie. Tracing the evolution of fatty acid‐binding proteins (fabps) in organisms with a heterogeneous fat distribution. FEBS Open Bio, 10:861-872, Mar 2020. URL: https://doi.org/10.1002/2211-5463.12840, doi:10.1002/2211-5463.12840. This article has 36 citations and is from a peer-reviewed journal.

20. (zhang2020tracingtheevolution pages 1-2): Yuru Zhang, Junmei Zhang, Yanhua Ren, Ronghua Lu, Liping Yang, and Guoxing Nie. Tracing the evolution of fatty acid‐binding proteins (fabps) in organisms with a heterogeneous fat distribution. FEBS Open Bio, 10:861-872, Mar 2020. URL: https://doi.org/10.1002/2211-5463.12840, doi:10.1002/2211-5463.12840. This article has 36 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PTHR11955-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR11955-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. storch2023themultifunctionalfamily pages 1-3
2. agellon2024importanceoffatty pages 2-4
3. bodnariuc2021examinationofbrainfatty pages 16-20
4. ibanezshimabukuro2019structureandligand pages 8-9
5. storch2023themultifunctionalfamily pages 3-4
6. storch2023themultifunctionalfamily pages 14-16
7. storch2023themultifunctionalfamily pages 17-19
8. agellon2024importanceoffatty pages 4-5
9. zhang2020tracingtheevolution pages 9-10
10. zhang2020tracingtheevolution pages 1-2
11. agellon2024importanceoffatty pages 1-2
12. kakouratos2025theroleof pages 2-4
13. kakouratos2025theroleof pages 4-6
14. storch2023themultifunctionalfamily pages 16-17
15. storch2023themultifunctionalfamily pages 12-14
16. xu2022thebiologicalfunctions pages 1-2
17. storch2023themultifunctionalfamily pages 6-8
18. storch2023themultifunctionalfamily pages 8-9
19. zhang2020tracingtheevolution pages 3-4
20. zhang2020tracingtheevolution pages 2-3
21. https://doi.org/10.11575/prism/38871,
22. https://doi.org/10.1146/annurev-nutr-062220-112240,
23. https://doi.org/10.1111/jcmm.17703,
24. https://doi.org/10.1042/bsr20191292,
25. https://doi.org/10.3390/curroncol32100531,
26. https://doi.org/10.3389/fcell.2022.857919,
27. https://doi.org/10.1002/2211-5463.12840,