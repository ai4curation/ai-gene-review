---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-21T20:46:45.662304'
end_time: '2026-06-21T20:59:24.873799'
duration_seconds: 759.21
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR23192
  interpro_name: Olfactomedin-like domain-containing protein
  interpro_short_name: Olfactomedin-like_domain
  interpro_type: family
  interpro_integrated: IPR050605
  member_databases: Not specified
  n_proteins: '13283'
  n_taxa: '3881'
  n_subfamilies: '26'
  interpro2go_terms: None mapped (no InterPro2GO terms for this entry)
  interpro_description: This family of proteins includes secreted and membrane-associated
    factors with diverse biological functions, primarily related to cell signaling,
    development, and maintenance of cellular structures. Members are involved in processes
    such as cell adhesion, migration, cytoskeleton organization, and differentiation.
    They play roles in the formation and maintenance of the nodes of Ranvier in neurons,
    dorsoventral patterning during development, and may influence cell proliferation
    in cancer. Some family members are implicated in the regulation of smooth muscle
    cell phenotype, bone formation, myelination, muscle hypertrophy, and neurite outgrowth.
    They are characterized by the presence of an olfactomedin-like domain, which mediates
    protein-protein interactions and contributes to their diverse functions.
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 24
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: PTHR23192-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# InterPro Family Research for GO Annotation Review

## ⚠️ CRITICAL: Family Identification Context

**BEFORE YOU BEGIN RESEARCH:** You are researching an **InterPro entry** (a protein
family / domain / superfamily signature), not a single gene. The goal is to judge
whether the GO terms that InterPro2GO attaches to this signature are appropriate for
**every** protein the signature matches.

### Target InterPro Entry (from the InterPro API):
- **Accession:** PTHR23192
- **Name:** Olfactomedin-like domain-containing protein
- **Short name:** Olfactomedin-like_domain
- **Entry type:** family
- **Integrated into / parent:** IPR050605
- **Member database signatures:** Not specified
- **Scale:** 13283 proteins across 3881 taxa, 26 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** This family of proteins includes secreted and membrane-associated factors with diverse biological functions, primarily related to cell signaling, development, and maintenance of cellular structures. Members are involved in processes such as cell adhesion, migration, cytoskeleton organization, and differentiation. They play roles in the formation and maintenance of the nodes of Ranvier in neurons, dorsoventral patterning during development, and may influence cell proliferation in cancer. Some family members are implicated in the regulation of smooth muscle cell phenotype, bone formation, myelination, muscle hypertrophy, and neurite outgrowth. They are characterized by the presence of an olfactomedin-like domain, which mediates protein-protein interactions and contributes to their diverse functions.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR23192 (Olfactomedin-like domain-containing protein)**, structured to support GO annotation review.

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
- **Accession:** PTHR23192
- **Name:** Olfactomedin-like domain-containing protein
- **Short name:** Olfactomedin-like_domain
- **Entry type:** family
- **Integrated into / parent:** IPR050605
- **Member database signatures:** Not specified
- **Scale:** 13283 proteins across 3881 taxa, 26 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** This family of proteins includes secreted and membrane-associated factors with diverse biological functions, primarily related to cell signaling, development, and maintenance of cellular structures. Members are involved in processes such as cell adhesion, migration, cytoskeleton organization, and differentiation. They play roles in the formation and maintenance of the nodes of Ranvier in neurons, dorsoventral patterning during development, and may influence cell proliferation in cancer. Some family members are implicated in the regulation of smooth muscle cell phenotype, bone formation, myelination, muscle hypertrophy, and neurite outgrowth. They are characterized by the presence of an olfactomedin-like domain, which mediates protein-protein interactions and contributes to their diverse functions.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR23192 (Olfactomedin-like domain-containing protein)**, structured to support GO annotation review.

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


# InterPro Family Research Report: PTHR23192 (Olfactomedin-like domain-containing protein)

## Executive Summary

PTHR23192 represents a phylogenetically diverse **family** (not a domain-only entry) of olfactomedin-containing proteins spanning 13,283 proteins across 3,881 taxa with 26 subfamilies. The current InterPro2GO annotation status (no mapped GO terms) is **APPROPRIATE and should be maintained**. This family exhibits extreme functional divergence across subfamilies, making family-wide GO term assignment scientifically unsound. The recommendation is **ACCEPT** the current lack of GO mappings at this entry level.

---

## 1. Family Definition and Biochemistry

### 1.1 Structural Architecture

The olfactomedin (OLF) domain adopts a **five-bladed β-propeller fold** comprising approximately 250-300 amino acids (hill2015moleculardetailsof pages 1-2, hill2015moleculardetailsof pages 2-4). Crystal structures from multiple subfamily members (myocilin, gliomedin, noelin/OLFM1, latrophilin-3) reveal this conserved architecture but with significant biochemical variation (hill2015moleculardetailsof pages 1-2, hill2015moleculardetailsof pages 10-13).

**Core conserved features (subfamily-dependent):**
- **Molecular clasp**: Extensive hydrogen bonding between discontinuous outer strands of blade E (E-1-E-2 and E-21) stabilizes the closed propeller conformation (hill2015moleculardetailsof pages 1-2, hill2015moleculardetailsof pages 2-4)
- **Disulfide bond**: N- and C-terminal cysteines form an inter-blade disulfide in most OLFs (e.g., myocilin C245-C433, OLFM1), but this is **absent in gliomedin**, demonstrating subfamily-specific loss (hill2015moleculardetailsof pages 6-9, hill2015moleculardetailsof pages 10-13)
- **Central hydrophilic cavity**: Contains a sequestered Ca²⁺ ion coordinated by conserved Asp/Glu residues in myocilin and OLFM1 (hill2015moleculardetailsof pages 6-9, hill2015moleculardetailsof pages 9-10), but gliomedin binds Na⁺ instead and lacks the canonical Ca²⁺ site (hill2015moleculardetailsof pages 9-10, hill2015moleculardetailsof pages 10-13)
- **Top-face loop B-10/C-11**: Well-defined loop covering the cavity entrance; site of protein-protein interactions and numerous disease mutations in myocilin (hill2015moleculardetailsof pages 6-9, hill2015moleculardetailsof pages 9-10, hill2015moleculardetailsof pages 10-13)
- **Cation-π interaction**: Conserved Lys/Tyr pair (e.g., myocilin K423/Y371) stabilizes loop architecture in myocilin, OLFM1, and latrophilin-3, but is disrupted in gliomedin where Lys466 is solvent-exposed (hill2015moleculardetailsof pages 9-10, hill2015moleculardetailsof pages 10-13)

### 1.2 Mechanistic Function

The olfactomedin domain is **NOT an enzyme**. It functions as a **protein-protein interaction scaffold** mediating cell adhesion, extracellular matrix organization, and receptor-ligand recognition (cardenasleon2022matricellularproteinsin pages 1-2, hill2015moleculardetailsof pages 1-2, hill2015moleculardetailsof pages 2-4). No catalytic residues or enzymatic activity has been documented. Instead, the domain:
- Binds diverse protein partners through surface-exposed loops and electrostatic patches (hill2015moleculardetailsof pages 9-10, hill2015moleculardetailsof pages 10-13)
- Mediates cell-cell and cell-matrix adhesion in development and tissue homeostasis (cardenasleon2022matricellularproteinsin pages 1-2, morenosalinas2019latrophilinsaneurocentric pages 1-2)
- May interact with polynucleotides, glycosaminoglycans, and lipids in a subfamily-specific manner (hill2015moleculardetailsof pages 9-10)

---

## 2. InterPro2GO Mapping Appropriateness

**Current status**: No GO terms are mapped to PTHR23192.

**Assessment**: This is **CORRECT** and reflects sound curation practice.

### 2.1 Why NO GO terms should be assigned at this family level

This entry is classified as **entry type: family** with 26 subfamilies. The literature demonstrates that:

1. **Functional divergence is extreme**. Representative subfamilies exhibit wholly distinct, non-overlapping biological roles:
   - **Myocilin (Subfamily III)**: Toxic gain-of-function protein aggregation causing primary open-angle glaucoma; normal function unknown (ng2023evaluationofmyocilin pages 1-2, scelsi2023quantitativedifferentiationof pages 1-3)
   - **Gliomedin (Subfamily VI)**: Node of Ranvier assembly via neurofascin-186 binding and sodium channel recruitment (hill2015moleculardetailsof pages 1-2, hill2015moleculardetailsof pages 2-4)
   - **OLFM1/noelin (Subfamily I)**: Neurogenesis, synaptic plasticity, amyloid-β regulation, and cognitive function (wei2025correlationofperipheral pages 1-2)
   - **OLFM2 (Subfamily IV)**: Adipocyte differentiation, cell cycle control, and energy homeostasis (lluch2025defectiveolfactomedin2connects pages 1-2)
   - **OLFML3 (Subfamily VII)**: Macrophage mitochondrial function, IRG1 localization, immune regulation (yu2025olfml3promotesirg1 pages 1-2, yu2025olfml3promotesirg1 pages 2-3)
   - **OLFM4 (Subfamily IX)**: Intestinal stem cell marker, cancer stem-cell niche support, immune evasion (cardenasleon2022matricellularproteinsin pages 1-2)
   - **Latrophilins (Subfamily II)**: Adhesion GPCR-mediated neuronal wiring and synapse formation (morenosalinas2019latrophilinsaneurocentric pages 1-2)

2. **No shared molecular function** beyond "protein binding" exists across all members. Terms like GO:0005515 (protein binding) or GO:0005576 (extracellular region) would be trivially uninformative.

3. **Process and component terms leak across taxa**. For example:
   - Gliomedin's GO:0043005 (neuron projection) and GO:0033268 (node of Ranvier) would systematically mis-annotate OLFM4 (intestinal stem cells) or OLFM2 (adipocytes).
   - OLFM4's GO:0005634 (intestinal stem cell maintenance, inferred) would mis-annotate myocilin (ocular trabecular meshwork).

4. **Subfamily-specific neo-functionalization** is prevalent:
   - Myocilin variants cause disease via **protein misfolding**, not loss of a conserved enzymatic activity (scelsi2023quantitativedifferentiationof pages 1-3)
   - Gliomedin structurally diverged (no disulfide, no Ca²⁺) yet retained high thermostability, suggesting functional adaptation (hill2015moleculardetailsof pages 9-10, hill2015moleculardetailsof pages 10-13)
   - Latrophilins in invertebrates **lack the olfactomedin domain entirely**, indicating vertebrate-specific domain acquisition (krishnan2016classificationnomenclatureand pages 1-5, morenosalinas2019latrophilinsaneurocentric pages 1-2)

### 2.2 Recommendation for InterPro

**Action**: **ACCEPT** the current absence of InterPro2GO terms for PTHR23192.

**Rationale**: This is a **family-level signature** identifying a structurally related but functionally divergent protein set. GO annotation should occur at:
- **Child subfamily entries** (if InterPro creates subfamily-specific signatures under IPR050605 or as independent entries)
- **Individual gene/protein records** in species-specific databases (UniProtKB, model organism databases)

Assigning GO terms at PTHR23192 would constitute systematic over-annotation, propagating incorrect functional predictions to thousands of proteins where those functions are absent.

---

## 3. Functional Divergence Across the Family

The olfactomedin family comprises **nine phylogenetically distinct subfamilies** with radically different biological roles (yu2025olfml3promotesirg1 pages 1-2, hill2015moleculardetailsof pages 1-2, krishnan2016classificationnomenclatureand pages 1-5). Key subfamily distinctions are summarized below.

| Subfamily | Representative Members | Key Biological Functions | Conserved Structural Features | Taxonomic Distribution | Citations |
|---|---|---|---|---|---|
| I | OLFM1 / noelin / pancortin | Secreted neural glycoprotein linked to neurogenesis, neural crest formation, cortex development, synaptic structure/function, and APP/Aβ-related regulation; serum OLFM1 is reduced in Alzheimer’s disease cohorts and correlates with cognition in APOE ε4 carriers | OLF domain forms a five-bladed β-propeller; npoh-OLF retains the OLF molecular clasp, disulfide bond, and a sequestered Ca2+ in the central hydrophilic cavity; top-face loop architecture implicated in protein interactions | Vertebrates; strongly represented in nervous system tissues, especially brain | (hill2015moleculardetailsof pages 1-2, hill2015moleculardetailsof pages 2-4, hill2015moleculardetailsof pages 6-9, wei2025correlationofperipheral pages 1-2) |
| II | Latrophilins / ADGRL1-3 | Adhesion GPCRs involved in neuronal adhesion, synapse assembly, neuronal network formation, and selective ligand interactions with teneurins, FLRTs, and in some cases neurexins; variants implicated in neuropsychiatric phenotypes | OLF domain present in vertebrate latrophilins; overall OLF fold is a five-bladed β-propeller; lat3-OLF shares core OLF architecture but shows distinct loop/cavity features relative to myocilin and OLFM1 | Broad across animals for latrophilins, but the OLF domain in latrophilins is vertebrate-specific or acquired in early vertebrate evolution; invertebrate latrophilins can lack OLF | (hill2015moleculardetailsof pages 1-2, krishnan2016classificationnomenclatureand pages 1-5, morenosalinas2019latrophilinsaneurocentric pages 1-2, scholz2019revisitingtheclassification pages 1-2) |
| III | Myocilin (MYOC) | Best-established disease link is toxic gain-of-function misfolding/aggregation in primary open-angle glaucoma; normal physiological function remains unclear | Canonical OLF five-bladed β-propeller; conserved disulfide bond (C245-C433 in full-length MYOC), central Ca2+-binding site, top-face loop B-10/C-11, and cation-π interaction important for stability; many pathogenic variants destabilize the OLF domain | Vertebrates, prominently studied in mammals and ocular tissues | (hill2015moleculardetailsof pages 1-2, hill2015moleculardetailsof pages 6-9, ng2023evaluationofmyocilin pages 1-2, scelsi2023quantitativedifferentiationof pages 1-3) |
| IV | OLFM2 | Pleiotropic glycoprotein involved in development and energy homeostasis; recent evidence shows adipocyte-specific roles in adipogenesis, cell-cycle-linked adipocyte biology, and obesity-related metabolic dysfunction | Family membership indicates an OLF-containing secreted glycoprotein; direct structural evidence for OLFM2 OLF domain in the retrieved corpus is limited compared with MYOC/OLFM1, so only family-level OLF fold inference is justified | Vertebrates, with widespread expression but prominent neural and adipose-related roles in mammals | (lluch2025defectiveolfactomedin2connects pages 1-2, hill2015moleculardetailsof pages 1-2) |
| V | OLFM3 / OLFML3 | Functions vary by species and context: scaffold in BMP/chordin/BMP1-Tolloid signaling during Xenopus axial development; tumor angiogenesis/pericyte biology; antiviral/innate immune regulation; macrophage migration, phagocytosis, IRG1 mitochondrial localization, and protection from LPS-induced mitochondrial dysfunction | N-terminal coiled-coil region plus C-terminal OLF-like domain; belongs to one of nine phylogenetic OLF subfamilies; mechanistic data support protein–protein interaction/scaffold roles rather than catalysis | Present across diverse vertebrates; expression/function can differ substantially among species and tissues | (yu2025olfml3promotesirg1 pages 1-2, yu2025olfml3promotesirg1 pages 2-3) |
| VI | Gliomedin / COLM / CRG-L2 | Formation and maintenance of nodes of Ranvier via extracellular shedding, trimerization through collagen regions, and binding neurofascin-186 to recruit sodium channel complexes | OLF domain retains five-bladed β-propeller fold but is an outlier structurally: lacks the conserved disulfide bond and the sequestered Ca2+ seen in other solved OLFs; has altered cavity ions and distinctive loop/cation-π features; unusually high thermal stability | Vertebrates; phylogenetically closest among solved examples to primitive OLFs; functions characterized mainly in peripheral nervous system myelination | (hill2015moleculardetailsof pages 2-4, hill2015moleculardetailsof pages 1-2, hill2015moleculardetailsof pages 6-9, hill2015moleculardetailsof pages 10-13) |
| VII | OLFML-like proteins including OLFML3 | Subfamily-level functions are heterogeneous and include immune modulation, angiogenesis, development, and context-dependent roles in infection and cancer; OLFML3 specifically is assigned here by recent phylogenetic work | Members typically combine an N-terminal coiled-coil region with a C-terminal OLF-like domain; family-level OLF fold conserved, but biochemical properties likely diverge | Vertebrates; OLFML3 reported in human, mouse, chicken, and Xenopus, with broader OLF family presence from nematodes to humans | (yu2025olfml3promotesirg1 pages 1-2, hill2015moleculardetailsof pages 1-2) |
| VIII | OLFML2A / OLFML2B | OLFML2B is associated with tumor microenvironment, immune infiltration, prognosis, ECM/focal adhesion-related signatures, and drug-resistance correlations in pan-cancer analyses; ocular expression reported for OLFML2A/B | OLFML2B has a distinctive Ser/Thr-rich region preceding the OLF domain, supporting separation as an independent subfamily; direct catalytic residues not established | Primates and other vertebrates; human/baboon ocular expression documented; likely broader vertebrate distribution | (hu2022pancanceranalysisof pages 1-2, krishnan2016classificationnomenclatureand pages 1-5) |
| IX | OLFM4 | Functions are highly lineage/context specific: robust marker of intestinal stem-like cells in human intestine and colorectal cancer, supports tumor stem-cell niche interactions, and participates in inflammation/cancer progression | OLF family membership supports extracellular OLF-domain scaffold architecture; no universal catalytic activity established from available evidence | Vertebrates, especially mammals; prominent in intestinal epithelium, neutrophil subsets, and gastrointestinal cancers | (cardenasleon2022matricellularproteinsin pages 1-2, hill2015moleculardetailsof pages 1-2) |


*Table: This table summarizes the major olfactomedin protein subfamilies, representative proteins, experimentally supported functions, structural traits, and taxonomic scope. It is useful for GO review because it highlights strong functional divergence despite shared OLF-domain architecture.*

### 3.1 Evidence of Neo-Functionalization

- **Structural divergence**: Gliomedin (Subfamily VI) lacks the disulfide bond and Ca²⁺ binding seen in most other OLFs, yet exhibits exceptionally high thermal stability (Tm ~70°C vs. ~55°C for myocilin/OLFM1), suggesting adaptation to peripheral nervous system extracellular environment (hill2015moleculardetailsof pages 9-10, hill2015moleculardetailsof pages 10-13)
- **Pathogenic variants**: Myocilin mutations cause glaucoma via **toxic gain-of-function** protein aggregation, not loss of a shared enzymatic activity; benign polymorphisms can be distinguished by thermal stability cutoffs (Tm <47°C predicts pathogenicity) (scelsi2023quantitativedifferentiationof pages 1-3)
- **Tissue-specific expression switches**: OLFM2 is adipocyte-specific and suppressed by inflammation (lluch2025defectiveolfactomedin2connects pages 1-2), whereas OLFM4 is an intestinal stem cell/cancer marker (cardenasleon2022matricellularproteinsin pages 1-2); OLFM1 is predominantly neural (wei2025correlationofperipheral pages 1-2)

### 3.2 Absence of Pseudo-Enzymes

The olfactomedin domain is **not an enzyme**, so the concept of "catalytically dead" members does not apply. All members retain the β-propeller scaffold for protein interaction; loss of specific structural features (e.g., Ca²⁺ site in gliomedin) represents functional tuning rather than inactivation (hill2015moleculardetailsof pages 9-10, hill2015moleculardetailsof pages 10-13).

---

## 4. Taxonomic Scope

### 4.1 Distribution

Olfactomedin proteins are present across **diverse metazoan taxa** from Caenorhabditis elegans to Homo sapiens, with over 200 family members identified (yu2025olfml3promotesirg1 pages 1-2, hill2015moleculardetailsof pages 1-2). The PTHR23192 entry spans 13,283 proteins across 3,881 taxa.

**Key taxonomic observations**:
- **Invertebrates**: Primitive olfactomedin-like proteins exist in nematodes and arthropods; C. elegans and Drosophila express latrophilin orthologs, though invertebrate latrophilins often **lack the olfactomedin domain** (krishnan2016classificationnomenclatureand pages 1-5, morenosalinas2019latrophilinsaneurocentric pages 1-2)
- **Vertebrates**: All nine subfamilies are represented, with subfamily-specific expansions:
  - Latrophilins acquired the olfactomedin domain in early vertebrate evolution (krishnan2016classificationnomenclatureand pages 1-5)
  - Gliomedin is phylogenetically similar to ancestral/primitive OLFs (hill2015moleculardetailsof pages 1-2, hill2015moleculardetailsof pages 2-4)
  - OLFM1-4 and OLFML subfamilies show vertebrate-specific diversification (hill2015moleculardetailsof pages 1-2)

### 4.2 Conservation of Function Across Taxa

**No single biological process or cellular component holds across all taxa matching this signature.** Examples of taxon-restricted functions:
- **Nodes of Ranvier** (gliomedin function) exist only in vertebrates with myelinated axons (hill2015moleculardetailsof pages 1-2, hill2015moleculardetailsof pages 2-4)
- **Intestinal stem cell niches** (OLFM4 function) are mammalian-specific (cardenasleon2022matricellularproteinsin pages 1-2)
- **Trabecular meshwork** (myocilin expression site) is vertebrate eye-specific (ng2023evaluationofmyocilin pages 1-2, scelsi2023quantitativedifferentiationof pages 1-3)

Thus, any GO process or component term assigned at the family level would systematically over-annotate proteins in taxa where that structure/pathway is absent.

---

## 5. Over-Annotation Verdict

### 5.1 Summary Assessment

**InterPro2GO status for PTHR23192: SOUND**

The absence of GO terms at this family-level entry correctly reflects the extreme functional heterogeneity documented across olfactomedin subfamilies. This entry identifies a **structural domain family** where the shared β-propeller fold mediates protein interactions, but the specific binding partners, tissue contexts, and biological outcomes are **subfamily-specific and often mutually exclusive**.

### 5.2 GO Action Pattern Recommendation

**For PTHR23192 (family level)**: **ACCEPT** — maintain zero InterPro2GO mappings

**For genes matching PTHR23192**:
- **Do NOT propagate** family-level GO terms (none exist, and none should be added)
- **Annotate** based on:
  1. **Subfamily membership** (if InterPro creates subfamily-specific child entries with appropriate scope)
  2. **Experimental evidence** from species-specific databases (UniProtKB, MGI, ZFIN, etc.)
  3. **Homology to well-characterized orthologs** within the same phylogenetic subfamily, with taxon-appropriate validation

### 5.3 Recommendations for InterPro

1. **Maintain current annotation**: The decision to not map GO terms to this family is exemplary curation practice and should serve as a model for other functionally heterogeneous domain families.

2. **Consider subfamily-specific entries**: If InterPro has or creates child entries corresponding to phylogenetic subfamilies (e.g., separate signatures for myocilin orthologs, gliomedin orthologs, OLFM4 orthologs), those could receive **narrowly scoped** GO terms reflecting subfamily-specific functions. However, each would require careful literature curation to ensure the function holds across all proteins matching that child signature.

3. **Document rationale**: Add a note to the PTHR23192 InterPro entry explicitly stating that this is a **structurally defined family** with extreme functional divergence, and that functional annotation should occur at the individual protein or subfamily level.

---

## Conclusion

PTHR23192 represents a well-defined **protein family** unified by a shared olfactomedin domain fold (five-bladed β-propeller) but exhibiting radical functional divergence across nine phylogenetic subfamilies. The domain acts as a scaffold for protein-protein interactions mediating cell adhesion, developmental signaling, and tissue-specific processes, **not as an enzyme**. Experimentally validated functions span glaucoma pathogenesis (myocilin), myelination (gliomedin), neurogenesis (OLFM1), adipogenesis (OLFM2), immune regulation (OLFML3), stem cell maintenance (OLFM4), and neuronal wiring (latrophilins), with no functional overlap.

The **absence of InterPro2GO terms** for this entry is scientifically correct. Assigning whole-protein GO terms at the family level would systematically over-annotate proteins across 3,881 taxa and 26 subfamilies, propagating incorrect functional predictions. The recommended action is **ACCEPT** the current annotation status, with GO terms assigned at subfamily-specific child entries or individual gene records where experimental or orthology-based evidence supports narrower functional scope.

---

**Prepared**: 2026  
**Sources**: Primary literature (2015-2025), structural biology databases (PDB), phylogenetic analyses  
**Entry Type Reminder**: PTHR23192 is a **family**, not a domain-only signature. GO terms describing whole-protein activities attached to domain families systematically over-annotate every protein containing that domain.

References

1. (hill2015moleculardetailsof pages 1-2): Shannon E. Hill, Rebecca K. Donegan, Elaine Nguyen, Tanay M. Desai, and Raquel L. Lieberman. Molecular details of olfactomedin domains provide pathway to structure-function studies. PLoS ONE, 10:e0130888, Jun 2015. URL: https://doi.org/10.1371/journal.pone.0130888, doi:10.1371/journal.pone.0130888. This article has 25 citations and is from a peer-reviewed journal.

2. (hill2015moleculardetailsof pages 2-4): Shannon E. Hill, Rebecca K. Donegan, Elaine Nguyen, Tanay M. Desai, and Raquel L. Lieberman. Molecular details of olfactomedin domains provide pathway to structure-function studies. PLoS ONE, 10:e0130888, Jun 2015. URL: https://doi.org/10.1371/journal.pone.0130888, doi:10.1371/journal.pone.0130888. This article has 25 citations and is from a peer-reviewed journal.

3. (hill2015moleculardetailsof pages 10-13): Shannon E. Hill, Rebecca K. Donegan, Elaine Nguyen, Tanay M. Desai, and Raquel L. Lieberman. Molecular details of olfactomedin domains provide pathway to structure-function studies. PLoS ONE, 10:e0130888, Jun 2015. URL: https://doi.org/10.1371/journal.pone.0130888, doi:10.1371/journal.pone.0130888. This article has 25 citations and is from a peer-reviewed journal.

4. (hill2015moleculardetailsof pages 6-9): Shannon E. Hill, Rebecca K. Donegan, Elaine Nguyen, Tanay M. Desai, and Raquel L. Lieberman. Molecular details of olfactomedin domains provide pathway to structure-function studies. PLoS ONE, 10:e0130888, Jun 2015. URL: https://doi.org/10.1371/journal.pone.0130888, doi:10.1371/journal.pone.0130888. This article has 25 citations and is from a peer-reviewed journal.

5. (hill2015moleculardetailsof pages 9-10): Shannon E. Hill, Rebecca K. Donegan, Elaine Nguyen, Tanay M. Desai, and Raquel L. Lieberman. Molecular details of olfactomedin domains provide pathway to structure-function studies. PLoS ONE, 10:e0130888, Jun 2015. URL: https://doi.org/10.1371/journal.pone.0130888, doi:10.1371/journal.pone.0130888. This article has 25 citations and is from a peer-reviewed journal.

6. (cardenasleon2022matricellularproteinsin pages 1-2): Claudia Griselda Cárdenas-León, Kristina Mäemets-Allas, Mariliis Klaas, Heli Lagus, Esko Kankuri, and Viljar Jaks. Matricellular proteins in cutaneous wound healing. Frontiers in Cell and Developmental Biology, Nov 2022. URL: https://doi.org/10.3389/fcell.2022.1073320, doi:10.3389/fcell.2022.1073320. This article has 29 citations.

7. (morenosalinas2019latrophilinsaneurocentric pages 1-2): Ana L. Moreno-Salinas, Monserrat Avila-Zozaya, Paul Ugalde-Silva, David A. Hernández-Guzmán, Fanis Missirlis, and Antony A. Boucard. Latrophilins: a neuro-centric view of an evolutionary conserved adhesion g protein-coupled receptor subfamily. Frontiers in Neuroscience, Jul 2019. URL: https://doi.org/10.3389/fnins.2019.00700, doi:10.3389/fnins.2019.00700. This article has 73 citations and is from a peer-reviewed journal.

8. (ng2023evaluationofmyocilin pages 1-2): Tsz Kin Ng, Jie Ji, Qingping Liu, Yao Yao, Wen-Ying Wang, Yingjie Cao, Chong-Bo Chen, Jian-Wei Lin, Geng Dong, Ling-Ping Cen, Chukai Huang, and Mingzhi Zhang. Evaluation of myocilin variant protein structures modeled by alphafold2. Biomolecules, 14:14, Dec 2023. URL: https://doi.org/10.3390/biom14010014, doi:10.3390/biom14010014. This article has 1 citations.

9. (scelsi2023quantitativedifferentiationof pages 1-3): Hailee F. Scelsi, Kamisha R. Hill, Brett M. Barlow, Mackenzie D. Martin, and Raquel L. Lieberman. Quantitative differentiation of benign and misfolded glaucoma-causing myocilin variants on the basis of protein thermal stability. Jan 2023. URL: https://doi.org/10.1242/dmm.049816, doi:10.1242/dmm.049816. This article has 11 citations and is from a domain leading peer-reviewed journal.

10. (wei2025correlationofperipheral pages 1-2): Chunxiao Wei, Guimei Zhang, Xiaoshu Fu, Meng Zhao, Weijie Zhai, Yanxin Shen, and Li Sun. Correlation of peripheral olfactomedin 1 with alzheimer’s disease and cognitive functions. Translational Psychiatry, Apr 2025. URL: https://doi.org/10.1038/s41398-025-03373-9, doi:10.1038/s41398-025-03373-9. This article has 6 citations and is from a peer-reviewed journal.

11. (lluch2025defectiveolfactomedin2connects pages 1-2): A. Lluch, J. Latorre, Isabel Espadas, Núria Oliveras-Cañellas, J. Moreno-Navarrete, Estefanía Caballano-Infantes, G. Sarker, Nicolás F Malvido, P. Garrido-Gil, J. Labandeira-García, Naoki Nakaya, Silvia Mora, Eduardo Chicano, Jaime López-Alcalá, María M. Malagón, Alejandro Martín-Montalvo, Birong Zhang, You Zhou, Ana I. Domingos, Miguel López, Johanna Pörschke, M. Gómez-Serrano, Witold Szymański, J. Graumann, Stanislav I Tomarev, I. González-García, J. Fernández-Real, and Francisco J Ortega. Defective olfactomedin-2 connects adipocyte dysfunction to obesity. Nature Communications, Aug 2025. URL: https://doi.org/10.1038/s41467-025-62430-5, doi:10.1038/s41467-025-62430-5. This article has 2 citations and is from a highest quality peer-reviewed journal.

12. (yu2025olfml3promotesirg1 pages 1-2): Qijun Yu, Hong Mei, Qian Gu, Ran Zeng, Yanan Li, Junjie Zhang, Chenxu Gao, Hai Fang, Jieming Qu, and Jia Liu. Olfml3 promotes irg1 mitochondrial localization and modulates mitochondrial function in macrophages. International Journal of Biological Sciences, 21:2275-2295, Feb 2025. URL: https://doi.org/10.7150/ijbs.103859, doi:10.7150/ijbs.103859. This article has 9 citations and is from a peer-reviewed journal.

13. (yu2025olfml3promotesirg1 pages 2-3): Qijun Yu, Hong Mei, Qian Gu, Ran Zeng, Yanan Li, Junjie Zhang, Chenxu Gao, Hai Fang, Jieming Qu, and Jia Liu. Olfml3 promotes irg1 mitochondrial localization and modulates mitochondrial function in macrophages. International Journal of Biological Sciences, 21:2275-2295, Feb 2025. URL: https://doi.org/10.7150/ijbs.103859, doi:10.7150/ijbs.103859. This article has 9 citations and is from a peer-reviewed journal.

14. (krishnan2016classificationnomenclatureand pages 1-5): Arunkumar Krishnan, Saskia Nijmeijer, Chris de Graaf, and Helgi B. Schiöth. Classification, nomenclature, and structural aspects of adhesion gpcrs. Handbook of experimental pharmacology, 234:15-41, Jan 2016. URL: https://doi.org/10.1007/978-3-319-41523-9\_2, doi:10.1007/978-3-319-41523-9\_2. This article has 61 citations and is from a peer-reviewed journal.

15. (scholz2019revisitingtheclassification pages 1-2): Nicole Scholz, Tobias Langenhan, and Torsten Schöneberg. Revisiting the classification of adhesion gpcrs. Annals of the New York Academy of Sciences, 1456:80-95, Jul 2019. URL: https://doi.org/10.1111/nyas.14192, doi:10.1111/nyas.14192. This article has 58 citations and is from a peer-reviewed journal.

16. (hu2022pancanceranalysisof pages 1-2): Pengbo Hu, Xiuyuan Zhang, Yiming Li, Liang Xu, and Hong Qiu. Pan-cancer analysis of olfml2b expression and its association with prognosis and immune infiltration. Frontiers in Genetics, Jul 2022. URL: https://doi.org/10.3389/fgene.2022.882794, doi:10.3389/fgene.2022.882794. This article has 8 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PTHR23192-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. hill2015moleculardetailsof pages 9-10
2. wei2025correlationofperipheral pages 1-2
3. cardenasleon2022matricellularproteinsin pages 1-2
4. morenosalinas2019latrophilinsaneurocentric pages 1-2
5. scelsi2023quantitativedifferentiationof pages 1-3
6. krishnan2016classificationnomenclatureand pages 1-5
7. hill2015moleculardetailsof pages 1-2
8. hill2015moleculardetailsof pages 2-4
9. hill2015moleculardetailsof pages 10-13
10. hill2015moleculardetailsof pages 6-9
11. ng2023evaluationofmyocilin pages 1-2
12. scholz2019revisitingtheclassification pages 1-2
13. hu2022pancanceranalysisof pages 1-2
14. https://doi.org/10.1371/journal.pone.0130888,
15. https://doi.org/10.3389/fcell.2022.1073320,
16. https://doi.org/10.3389/fnins.2019.00700,
17. https://doi.org/10.3390/biom14010014,
18. https://doi.org/10.1242/dmm.049816,
19. https://doi.org/10.1038/s41398-025-03373-9,
20. https://doi.org/10.1038/s41467-025-62430-5,
21. https://doi.org/10.7150/ijbs.103859,
22. https://doi.org/10.1007/978-3-319-41523-9\_2,
23. https://doi.org/10.1111/nyas.14192,
24. https://doi.org/10.3389/fgene.2022.882794,