---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-28T19:39:34.292994'
end_time: '2026-06-28T20:08:02.289357'
duration_seconds: 1708.0
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR10048
  interpro_name: PHOSPHATIDYLINOSITOL KINASE
  interpro_short_name: Not specified
  interpro_type: family
  interpro_integrated: IPR015433
  member_databases: Not specified
  n_proteins: '31999'
  n_taxa: '10051'
  n_subfamilies: '28'
  interpro2go_terms: None mapped (no InterPro2GO terms for this entry)
  interpro_description: Not specified in InterPro
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
  path: PTHR10048-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR10048-deep-research-falcon_artifacts/artifact-01.md
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
- **Accession:** PTHR10048
- **Name:** PHOSPHATIDYLINOSITOL KINASE
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** IPR015433
- **Member database signatures:** Not specified
- **Scale:** 31999 proteins across 10051 taxa, 28 subfamilies
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
**PTHR10048 (PHOSPHATIDYLINOSITOL KINASE)**, structured to support GO annotation review.

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
- **Accession:** PTHR10048
- **Name:** PHOSPHATIDYLINOSITOL KINASE
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** IPR015433
- **Member database signatures:** Not specified
- **Scale:** 31999 proteins across 10051 taxa, 28 subfamilies
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
**PTHR10048 (PHOSPHATIDYLINOSITOL KINASE)**, structured to support GO annotation review.

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


# Comprehensive GO Annotation Review Report: PTHR10048 (PHOSPHATIDYLINOSITOL KINASE)

## 1. Family Definition and Biochemistry

### 1.1 Scope of the PTHR10048 Family

PTHR10048 is a PANTHER family-level entry that encompasses the broad **phosphatidylinositol kinase superfamily**, matching 31,999 proteins across 10,051 taxa with 28 recognized subfamilies. This family is integrated into the InterPro parent entry IPR015433. Critically, despite its name suggesting lipid kinase function, this family encompasses proteins with fundamentally different enzymatic activities—and even catalytically dead members.

The phosphoinositide kinase superfamily comprises **19 human genes encoding phosphoinositide kinase catalytic subunits** organized into three major functional groups based on sequence conservation (burke2018structuralbasisfor pages 2-4, burke2018structuralbasisfor pages 2-2). Burke (2018) established three evolutionary groups: (1) all PI3K classes and type III PI4Ks; (2) type II PI4Ks; and (3) PIP kinases (burke2018structuralbasisfor pages 2-2). In addition, the family includes the **PIKK (phosphatidylinositol 3-kinase-related kinase) subfamily**, which despite sharing the PI3K-like kinase domain fold, functions exclusively as **protein serine/threonine kinases** rather than lipid kinases (eliasvillalobos2019newinsightsinto pages 1-6, tafur2020structuralinsightsinto pages 15-18).

### 1.2 Structural Fold and Catalytic Mechanism

Members of this superfamily share a conserved **PI3K-like kinase domain** with a bilobal architecture consisting of an N-lobe and a C-lobe (burke2018structuralbasisfor pages 4-5). The domain organization varies significantly across subfamilies. PI3K class I enzymes contain ABD (adaptor-binding domain), RBD (Ras-binding domain), C2, helical, and kinase (N-lobe + C-lobe) domains (burke2018structuralbasisfor pages 4-5). PIKK members share a characteristic architecture of N-terminal HEAT repeats (forming an α-solenoid superhelical structure with "Finger," "Ring," and "Clasp" domains), followed by a FAT domain, the PI3K-related kinase domain, and a C-terminal FATC motif (eliasvillalobos2019newinsightsinto pages 6-9).

### 1.3 Conserved Catalytic Residues

Three canonical catalytic motifs are conserved across active family members (eliasvillalobos2019newinsightsinto pages 12-17, eliasvillalobos2019newinsightsinto pages 6-9):
- **VAIK motif**: ATP-binding motif
- **HRD (or DRH) motif**: Catalytic loop residue essential for phosphotransfer
- **DFG motif**: Divalent cation (Mg²⁺)-binding motif

For type II PI4Ks specifically, conserved catalytic residues include **Lys-152** (nucleotide binding), **Asp-307** (catalytic base), **Asn-312** and **Asp-345** (Mg²⁺ binding), and **Glu-155, Pro-163, Asp-300** (class-conserved residues), along with the palmitoylation motif CCPC (kumar2024phosphatidylinositol4kinases pages 2-4).

Notably, the PIKK family member **TRRAP** has completely lost all three catalytic motifs (VAIK, HRD, and DFG), rendering it a **pseudokinase** with no phosphotransfer activity (eliasvillalobos2019newinsightsinto pages 12-17, eliasvillalobos2019newinsightsinto pages 6-9).

---

## 2. InterPro2GO Mapping Appropriateness

**Current status: No InterPro2GO terms are mapped to PTHR10048.**

This absence is **entirely appropriate** and should be maintained. The following analysis explains why no GO term at any of the three ontology branches (Molecular Function, Biological Process, Cellular Component) can be correctly applied to all 31,999 proteins matched by this signature.

### 2.1 Molecular Function GO Terms

- **"Phosphatidylinositol kinase activity" (GO:0052813 or related)**: This would be incorrect for the PIKK protein kinase members (mTOR, ATM, ATR, DNA-PKcs, SMG1), which phosphorylate protein substrates on Ser/Thr residues rather than lipids (tafur2020structuralinsightsinto pages 15-18, huang2023inhibitorsofphosphoinositide pages 1-2). It would also be incorrect for TRRAP, which has no catalytic activity whatsoever (eliasvillalobos2019newinsightsinto pages 12-17).

- **"ATP binding" (GO:0005524)**: While most active members bind ATP, TRRAP has lost the ATP-binding VAIK motif and cannot bind ATP (eliasvillalobos2019newinsightsinto pages 12-17). Therefore, this term would systematically over-annotate TRRAP-containing proteins.

- **"Kinase activity" (GO:0016301)**: Incorrect for TRRAP, which is a pseudokinase (eliasvillalobos2019newinsightsinto pages 12-17, eliasvillalobos2019newinsightsinto pages 9-12).

- **"Protein serine/threonine kinase activity" (GO:0004674)**: Only applicable to PIKK members (mTOR, ATM, ATR, DNA-PKcs, SMG1), not to the lipid kinase subfamilies (tafur2020structuralinsightsinto pages 15-18).

### 2.2 Biological Process GO Terms

The biological processes spanned by this family are irreconcilably diverse:
- **PI3K class I**: Growth factor signaling, cell survival, proliferation (burke2018structuralbasisfor pages 5-6)
- **PI3K class III (VPS34)**: Autophagy, endomembrane trafficking (burke2018structuralbasisfor pages 8-10)
- **PI4Ks**: Vesicle trafficking, lipid transport, Golgi/PM phosphoinositide supply (kumar2024phosphatidylinositol4kinases pages 2-4, burke2018structuralbasisfor pages 2-2)
- **PIP kinases**: Plasma membrane signaling, actin dynamics (muftuoglu2016mechanismofsubstrate pages 1-2)
- **mTOR**: Growth control, metabolism, autophagy regulation (tafur2020structuralinsightsinto pages 15-18, huang2023inhibitorsofphosphoinositide pages 1-2)
- **ATM/ATR/DNA-PKcs**: DNA damage response, genome stability maintenance (huang2023inhibitorsofphosphoinositide pages 1-2)
- **SMG1**: Nonsense-mediated mRNA decay (huang2023inhibitorsofphosphoinositide pages 1-2)
- **TRRAP**: Transcriptional co-activation, chromatin modification via SAGA/NuA4 complexes (eliasvillalobos2019newinsightsinto pages 9-12, eliasvillalobos2019newinsightsinto pages 12-17)

No single biological process GO term encompasses all of these activities.

### 2.3 Cellular Component GO Terms

Members localize to plasma membrane, cytoplasm, nucleus, Golgi apparatus, endosomes, and chromatin-associated complexes. No common compartment unifies the family (burke2018structuralbasisfor pages 5-6, eliasvillalobos2019newinsightsinto pages 9-12).

---

## 3. Functional Divergence Across the Family

The following table details the extreme functional heterogeneity within PTHR10048:

| Subfamily | Substrate Type | Key Substrate/Product | Primary Biological Process | Catalytic? | Appropriate Specific GO Term (MF) |
|---|---|---|---|---|---|
| PI3K Class I (p110α, p110β, p110δ, p110γ) | Lipid | PI(4,5)P2 → PI(3,4,5)P3 | Growth, survival, receptor/GPCR signaling | Yes | phosphatidylinositol-4,5-bisphosphate 3-kinase activity (burke2018structuralbasisfor pages 5-6, burke2018structuralbasisfor pages 2-4) |
| PI3K Class II (PI3K-C2α, PI3K-C2β, PI3K-C2γ) | Lipid | PI → PI3P; PI4P → PI(3,4)P2 | Membrane trafficking, signaling | Yes | phosphatidylinositol kinase activity (class II PI3K-specific child term preferred if available) (burke2018structuralbasisfor pages 5-6) |
| PI3K Class III (VPS34) | Lipid | PI → PI3P | Autophagy, endomembrane trafficking | Yes | phosphatidylinositol 3-kinase activity (burke2018structuralbasisfor pages 8-10, burke2018structuralbasisfor pages 5-6) |
| PI4K Type II (PI4KIIα, PI4KIIβ) | Lipid | PI → PI4P | Vesicle trafficking, membrane organization | Yes | phosphatidylinositol 4-kinase activity (kumar2024phosphatidylinositol4kinases pages 2-4, burke2018structuralbasisfor pages 5-6) |
| PI4K Type III (PI4KA, PI4KB) | Lipid | PI → PI4P | Lipid transport, Golgi/PM phosphoinositide supply | Yes | phosphatidylinositol 4-kinase activity (burke2018structuralbasisfor pages 2-2, burke2018structuralbasisfor pages 5-6) |
| PIP Kinase Type I (PIP5Kα/β/γ) | Lipid | PI4P → PI(4,5)P2 | Plasma membrane signaling, actin/membrane regulation | Yes | phosphatidylinositol-4-phosphate 5-kinase activity (muftuoglu2016mechanismofsubstrate pages 1-2, burke2018structuralbasisfor pages 5-6) |
| PIP Kinase Type II (PIP4Kα/β/γ) | Lipid | PI5P → PI(4,5)P2 | Nuclear/cytoplasmic phosphoinositide regulation, signaling | Yes | phosphatidylinositol-5-phosphate 4-kinase activity (muftuoglu2016mechanismofsubstrate pages 1-2, burke2018structuralbasisfor pages 5-6) |
| PIP Kinase Type III / PIKfyve | Lipid | PI3P → PI(3,5)P2 | Endolysosomal homeostasis, trafficking | Yes | phosphatidylinositol-3-phosphate 5-kinase activity (burke2018structuralbasisfor pages 5-6) |
| mTOR (PIKK) | Protein | Protein Ser/Thr residues on substrates such as S6K/4E-BP family members | Growth control, metabolism, autophagy regulation | Yes | protein serine/threonine kinase activity (tafur2020structuralinsightsinto pages 15-18, huang2023inhibitorsofphosphoinositide pages 1-2) |
| ATM (PIKK) | Protein | Protein Ser/Thr residues on DNA damage response substrates | DNA damage response, genome stability | Yes | protein serine/threonine kinase activity (tafur2020structuralinsightsinto pages 15-18, huang2023inhibitorsofphosphoinositide pages 1-2) |
| ATR (PIKK) | Protein | Protein Ser/Thr residues on replication stress/DNA damage substrates | DNA damage response, replication stress signaling | Yes | protein serine/threonine kinase activity (tafur2020structuralinsightsinto pages 15-18, huang2023inhibitorsofphosphoinositide pages 1-2) |
| DNA-PKcs (PIKK) | Protein | Protein Ser/Thr residues on DNA repair substrates | Non-homologous end joining, double-strand break repair | Yes | protein serine/threonine kinase activity (tafur2020structuralinsightsinto pages 15-18, huang2023inhibitorsofphosphoinositide pages 1-2) |
| SMG1 (PIKK) | Protein | Protein Ser/Thr residues on NMD-associated substrates | Nonsense-mediated mRNA decay; also DNA repair-related functions reported | Yes | protein serine/threonine kinase activity (tafur2020structuralinsightsinto pages 15-18, huang2023inhibitorsofphosphoinositide pages 1-2) |
| TRRAP (PIKK) | Neither active lipid nor protein kinase; pseudokinase scaffold | No demonstrated catalytic phosphotransfer substrate; retains PI3K-like domain | Transcriptional co-activation, chromatin-associated scaffolding | No | no catalytic MF term appropriate; protein-containing complex scaffold activity may be more appropriate than kinase terms (eliasvillalobos2019newinsightsinto pages 12-17, eliasvillalobos2019newinsightsinto pages 9-12) |


*Table: This table summarizes the major functional subdivisions inside the broad PTHR10048 phosphatidylinositol kinase family. It is useful for GO review because it shows that the family spans multiple distinct catalytic specificities, biological processes, and even a catalytically inactive pseudokinase.*

### 3.1 Three Major Functional Classes

The family encompasses three fundamentally distinct functional categories (burke2018structuralbasisfor pages 5-6, burke2018structuralbasisfor pages 2-2):

1. **Lipid kinases** (PI3Ks, PI4Ks, PIP kinases): Phosphorylate the inositol head group of phosphatidylinositol lipids at different positions (3-, 4-, or 5-OH). Even within this group, substrate specificities and products differ dramatically. Notably, type II and type III PI4Ks produce the same product (PI4P) but are evolutionarily divergent, representing convergent evolution of catalytic function (burke2018structuralbasisfor pages 2-2).

2. **Protein kinases** (PIKK family: mTOR, ATM, ATR, DNA-PKcs, SMG1): Despite sharing the PI3K-like kinase domain fold, these function exclusively as serine/threonine protein kinases with no lipid kinase activity (eliasvillalobos2019newinsightsinto pages 1-6, tafur2020structuralinsightsinto pages 15-18). Their biological roles span from metabolic growth control (mTOR) to DNA damage sensing and repair (ATM, ATR, DNA-PKcs) to mRNA surveillance (SMG1) (huang2023inhibitorsofphosphoinositide pages 1-2).

3. **Pseudokinase** (TRRAP/Tra1): The sole catalytically inactive member of the PIKK family, TRRAP has completely lost all three canonical catalytic motifs (VAIK, HRD, DFG) yet retains the overall domain architecture (eliasvillalobos2019newinsightsinto pages 12-17, eliasvillalobos2019newinsightsinto pages 6-9). TRRAP functions as a scaffolding subunit of the SAGA and NuA4/TIP60 histone acetyltransferase complexes, recruiting these co-activator complexes to gene promoters upon transcription factor binding (eliasvillalobos2019newinsightsinto pages 9-12). Structurally, TRRAP shares the dedicated HSP90/TTT chaperone machinery with active PIKKs, suggesting evolutionary pressure to maintain the fold for complex assembly rather than catalysis (eliasvillalobos2019newinsightsinto pages 9-12, eliasvillalobos2019newinsightsinto pages 1-6).

### 3.2 Kinase-Independent Functions

Beyond TRRAP, other family members also display kinase-independent functions. PI3K p110β has been shown to possess scaffolding activities independent of its lipid kinase activity (hirsch2009twiceupona pages 3-4). PIP4Ks have been reported to have catalytic-independent roles in regulating PI(4,5)P2 levels. These examples further complicate any attempt to apply a uniform GO annotation.

---

## 4. Taxonomic Scope

PTHR10048 spans **10,051 taxa**, primarily across eukaryotes. The phylogenetic distribution of PIKK family members has been mapped across major eukaryotic lineages including Amorphea (metazoans and fungi), Archaeplastida (plants including tracheophytes, bryophytes, and chlorophytes), SAR (stramenopiles, alveolates), and Excavata (eliasvillalobos2019newinsightsinto pages 25-30). Different PIKK members show variable taxonomic distributions:

- **TOR and ATR**: Broadly conserved across most eukaryotic supergroups
- **ATM**: Present across most eukaryotic lineages
- **DNA-PK**: More restricted distribution (absent from some lineages including certain invertebrates and plants)
- **SMG1**: Variable presence across eukaryotic groups
- **TRRAP**: Conserved across eukaryotes from fungi to vertebrates (eliasvillalobos2019newinsightsinto pages 25-30, eliasvillalobos2019newinsightsinto pages 6-9)

The lipid kinase members (PI3Ks, PI4Ks) are found broadly across eukaryotes, with phosphoinositide metabolism being a fundamental eukaryotic feature (burke2018structuralbasisfor pages 2-4, burke2018structuralbasisfor pages 2-2). The enormous taxonomic breadth, combined with the functional heterogeneity described above, means that no biological process or cellular component GO term could hold across all matched organisms.

---

## 5. Over-Annotation Verdict and Recommendations

| Assessment Area | Finding | Recommendation |
|---|---|---|
| Family Functional Homogeneity | Extremely heterogeneous: includes lipid kinases (PI3K, PI4K, PIP kinases), protein kinases (mTOR, ATM, ATR, DNA-PKcs, SMG1), and pseudokinase (TRRAP) (burke2018structuralbasisfor pages 5-6, tafur2020structuralinsightsinto pages 15-18, eliasvillalobos2019newinsightsinto pages 12-17) | No family-level GO term can capture all members |
| Current InterPro2GO Status | No GO terms currently mapped | ACCEPT - this is correct; do not add any GO terms |
| Molecular Function GO Term Assessment | `phosphatidylinositol kinase activity` would be incorrect for PIKK protein kinases and TRRAP; `ATP binding` is incorrect for TRRAP; `kinase activity` is incorrect for TRRAP because it lacks catalytic motifs (eliasvillalobos2019newinsightsinto pages 1-6, tafur2020structuralinsightsinto pages 15-18, eliasvillalobos2019newinsightsinto pages 12-17) | Do NOT add any MF term at family level |
| Biological Process GO Term Assessment | Processes span lipid signaling, DNA damage response, mRNA decay, autophagy, and transcription, with no process shared by all members (burke2018structuralbasisfor pages 5-6, huang2023inhibitorsofphosphoinositide pages 1-2, eliasvillalobos2019newinsightsinto pages 9-12) | Do NOT add any BP term at family level |
| Cellular Component GO Term Assessment | Members act at plasma membrane, cytoplasm, nucleus, Golgi/endomembrane systems, and chromatin-associated complexes; no common compartment fits all members (burke2018structuralbasisfor pages 5-6, huang2023inhibitorsofphosphoinositide pages 1-2, eliasvillalobos2019newinsightsinto pages 9-12) | Do NOT add any CC term at family level |
| Pseudokinase Members | TRRAP completely lacks the canonical catalytic motifs required in other PIKKs (VAIK, HRD, DFG absent) and functions as a scaffold/pseudokinase (eliasvillalobos2019newinsightsinto pages 12-17, eliasvillalobos2019newinsightsinto pages 6-9) | Any kinase or ATP-binding term would be systematically incorrect for TRRAP |
| Overall Verdict | The absence of InterPro2GO mappings for PTHR10048 is correct and sound given the family's biochemical and biological diversity (burke2018structuralbasisfor pages 5-6, eliasvillalobos2019newinsightsinto pages 12-17, tafur2020structuralinsightsinto pages 15-18) | ACCEPT the current empty mapping |
| Recommendation for InterPro | GO annotations should be assigned, if at all, to the 28 PTHR10048 subfamilies rather than to the parent family, because function is resolved only at narrower clade levels (burke2018structuralbasisfor pages 5-6, eliasvillalobos2019newinsightsinto pages 25-30) | Consider adding subfamily-level InterPro2GO mappings instead |


*Table: This table summarizes the GO annotation review verdict for the broad PTHR10048 phosphatidylinositol kinase family. It is useful because it shows why the current absence of InterPro2GO mappings is appropriate and why any future GO annotation should be pushed down to subfamily level.*

### 5.1 Overall Assessment

The current InterPro2GO mapping status for PTHR10048—**no mapped GO terms**—is **CORRECT and SOUND**. This family is one of the most functionally heterogeneous entries in the PANTHER classification, spanning:
- Lipid kinases with at least 8 distinct substrate specificities
- Protein serine/threonine kinases involved in 4+ unrelated biological processes
- A catalytically dead pseudokinase functioning as a transcriptional scaffold

### 5.2 Recommended GO Action Pattern

**ACCEPT** — The current empty InterPro2GO mapping should be maintained.

Any addition of GO terms at this family level would result in systematic over-annotation of thousands of proteins. Specifically:
- Adding "phosphatidylinositol kinase activity" would incorrectly annotate all PIKK protein kinases and the TRRAP pseudokinase
- Adding "ATP binding" would incorrectly annotate TRRAP
- Adding any biological process term would incorrectly annotate the majority of family members not involved in that process
- Adding any cellular component term would be incorrect for members with different subcellular localizations

### 5.3 Recommendations for InterPro

1. **Push GO annotations to subfamily level**: The 28 PTHR10048 subfamilies likely resolve functional homogeneity to a degree where subfamily-specific GO terms can be applied. For example, a PI3K class I subfamily could correctly receive "phosphatidylinositol-4,5-bisphosphate 3-kinase activity" (GO:0046934), while an mTOR subfamily could receive "protein serine/threonine kinase activity" (GO:0004674).

2. **Flag TRRAP subfamily**: Any subfamily containing TRRAP/Tra1 members should explicitly exclude kinase activity and ATP-binding terms, as this is a validated pseudokinase (eliasvillalobos2019newinsightsinto pages 12-17, eliasvillalobos2019newinsightsinto pages 1-6).

3. **Consider split annotation for type II vs. type III PI4Ks**: Although both produce PI4P, they are evolutionarily divergent and differ in structural features and subcellular localization (burke2018structuralbasisfor pages 2-2, kumar2024phosphatidylinositol4kinases pages 2-4), warranting distinct GO annotations at the subfamily level.

### 5.4 Summary

PTHR10048 represents a case where the PANTHER family classification correctly groups proteins by shared evolutionary origin (the PI3K-like kinase domain fold), but the functional divergence across the family is so extreme that no single GO term—at any ontology branch—can be safely applied to all matched proteins. The current absence of InterPro2GO mappings reflects appropriate curation judgment and should be preserved.


References

1. (burke2018structuralbasisfor pages 2-4): John E. Burke. Structural basis for regulation of phosphoinositide kinases and their involvement in human disease. Molecular cell, 71 5:653-673, Sep 2018. URL: https://doi.org/10.1016/j.molcel.2018.08.005, doi:10.1016/j.molcel.2018.08.005. This article has 304 citations and is from a highest quality peer-reviewed journal.

2. (burke2018structuralbasisfor pages 2-2): John E. Burke. Structural basis for regulation of phosphoinositide kinases and their involvement in human disease. Molecular cell, 71 5:653-673, Sep 2018. URL: https://doi.org/10.1016/j.molcel.2018.08.005, doi:10.1016/j.molcel.2018.08.005. This article has 304 citations and is from a highest quality peer-reviewed journal.

3. (eliasvillalobos2019newinsightsinto pages 1-6): Alberto Elías-Villalobos, Philippe Fort, and Dominique Helmlinger. New insights into the evolutionary conservation of the sole pikk pseudokinase tra1/trrap. Biochemical Society transactions, 47:1597-1608, Nov 2019. URL: https://doi.org/10.1042/bst20180496, doi:10.1042/bst20180496. This article has 38 citations and is from a peer-reviewed journal.

4. (tafur2020structuralinsightsinto pages 15-18): Lucas Tafur, Jennifer Kefauver, and Robbie Loewith. Structural insights into tor signaling. Genes, 11:885, Aug 2020. URL: https://doi.org/10.3390/genes11080885, doi:10.3390/genes11080885. This article has 54 citations.

5. (burke2018structuralbasisfor pages 4-5): John E. Burke. Structural basis for regulation of phosphoinositide kinases and their involvement in human disease. Molecular cell, 71 5:653-673, Sep 2018. URL: https://doi.org/10.1016/j.molcel.2018.08.005, doi:10.1016/j.molcel.2018.08.005. This article has 304 citations and is from a highest quality peer-reviewed journal.

6. (eliasvillalobos2019newinsightsinto pages 6-9): Alberto Elías-Villalobos, Philippe Fort, and Dominique Helmlinger. New insights into the evolutionary conservation of the sole pikk pseudokinase tra1/trrap. Biochemical Society transactions, 47:1597-1608, Nov 2019. URL: https://doi.org/10.1042/bst20180496, doi:10.1042/bst20180496. This article has 38 citations and is from a peer-reviewed journal.

7. (eliasvillalobos2019newinsightsinto pages 12-17): Alberto Elías-Villalobos, Philippe Fort, and Dominique Helmlinger. New insights into the evolutionary conservation of the sole pikk pseudokinase tra1/trrap. Biochemical Society transactions, 47:1597-1608, Nov 2019. URL: https://doi.org/10.1042/bst20180496, doi:10.1042/bst20180496. This article has 38 citations and is from a peer-reviewed journal.

8. (kumar2024phosphatidylinositol4kinases pages 2-4): Ravinder Kumar and Piyush Kumar. Phosphatidyl inositol 4-kinases. Encyclopedia, 4:1062-1072, Jun 2024. URL: https://doi.org/10.3390/encyclopedia4030068, doi:10.3390/encyclopedia4030068. This article has 1 citations.

9. (huang2023inhibitorsofphosphoinositide pages 1-2): Xueqin Huang, Li You, Eugenie Nepovimova, Miroslav Psotka, David Malinak, Marian Valko, Ladislav Sivak, Jan Korabecny, Zbynek Heger, Vojtech Adam, Qinghua Wu, and Kamil Kuca. Inhibitors of phosphoinositide 3-kinase (pi3k) and phosphoinositide 3-kinase-related protein kinase family (pikk). Journal of Enzyme Inhibition and Medicinal Chemistry, Jul 2023. URL: https://doi.org/10.1080/14756366.2023.2237209, doi:10.1080/14756366.2023.2237209. This article has 44 citations and is from a peer-reviewed journal.

10. (eliasvillalobos2019newinsightsinto pages 9-12): Alberto Elías-Villalobos, Philippe Fort, and Dominique Helmlinger. New insights into the evolutionary conservation of the sole pikk pseudokinase tra1/trrap. Biochemical Society transactions, 47:1597-1608, Nov 2019. URL: https://doi.org/10.1042/bst20180496, doi:10.1042/bst20180496. This article has 38 citations and is from a peer-reviewed journal.

11. (burke2018structuralbasisfor pages 5-6): John E. Burke. Structural basis for regulation of phosphoinositide kinases and their involvement in human disease. Molecular cell, 71 5:653-673, Sep 2018. URL: https://doi.org/10.1016/j.molcel.2018.08.005, doi:10.1016/j.molcel.2018.08.005. This article has 304 citations and is from a highest quality peer-reviewed journal.

12. (burke2018structuralbasisfor pages 8-10): John E. Burke. Structural basis for regulation of phosphoinositide kinases and their involvement in human disease. Molecular cell, 71 5:653-673, Sep 2018. URL: https://doi.org/10.1016/j.molcel.2018.08.005, doi:10.1016/j.molcel.2018.08.005. This article has 304 citations and is from a highest quality peer-reviewed journal.

13. (muftuoglu2016mechanismofsubstrate pages 1-2): Yagmur Muftuoglu, Yi Xue, Xiang Gao, Dianqing Wu, and Ya Ha. Mechanism of substrate specificity of phosphatidylinositol phosphate kinases. Proceedings of the National Academy of Sciences, 113:8711-8716, Jul 2016. URL: https://doi.org/10.1073/pnas.1522112113, doi:10.1073/pnas.1522112113. This article has 49 citations and is from a highest quality peer-reviewed journal.

14. (hirsch2009twiceupona pages 3-4): Emilio Hirsch, Laura Braccini, Elisa Ciraolo, Fulvio Morello, and Alessia Perino. Twice upon a time: pi3k's secret double life exposed. Trends in biochemical sciences, 34 5:244-8, May 2009. URL: https://doi.org/10.1016/j.tibs.2009.02.003, doi:10.1016/j.tibs.2009.02.003. This article has 90 citations and is from a domain leading peer-reviewed journal.

15. (eliasvillalobos2019newinsightsinto pages 25-30): Alberto Elías-Villalobos, Philippe Fort, and Dominique Helmlinger. New insights into the evolutionary conservation of the sole pikk pseudokinase tra1/trrap. Biochemical Society transactions, 47:1597-1608, Nov 2019. URL: https://doi.org/10.1042/bst20180496, doi:10.1042/bst20180496. This article has 38 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PTHR10048-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR10048-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. burke2018structuralbasisfor pages 2-2
2. burke2018structuralbasisfor pages 4-5
3. eliasvillalobos2019newinsightsinto pages 6-9
4. eliasvillalobos2019newinsightsinto pages 12-17
5. tafur2020structuralinsightsinto pages 15-18
6. burke2018structuralbasisfor pages 5-6
7. burke2018structuralbasisfor pages 8-10
8. muftuoglu2016mechanismofsubstrate pages 1-2
9. huang2023inhibitorsofphosphoinositide pages 1-2
10. eliasvillalobos2019newinsightsinto pages 9-12
11. hirsch2009twiceupona pages 3-4
12. eliasvillalobos2019newinsightsinto pages 25-30
13. burke2018structuralbasisfor pages 2-4
14. eliasvillalobos2019newinsightsinto pages 1-6
15. https://doi.org/10.1016/j.molcel.2018.08.005,
16. https://doi.org/10.1042/bst20180496,
17. https://doi.org/10.3390/genes11080885,
18. https://doi.org/10.3390/encyclopedia4030068,
19. https://doi.org/10.1080/14756366.2023.2237209,
20. https://doi.org/10.1073/pnas.1522112113,
21. https://doi.org/10.1016/j.tibs.2009.02.003,