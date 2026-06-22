---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-21T21:00:27.250306'
end_time: '2026-06-21T21:11:54.314984'
duration_seconds: 687.06
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR24177
  interpro_name: CASKIN
  interpro_short_name: Not specified
  interpro_type: family
  interpro_integrated: None (top-level entry)
  member_databases: Not specified
  n_proteins: '12734'
  n_taxa: '977'
  n_subfamilies: '116'
  interpro2go_terms: None mapped (no InterPro2GO terms for this entry)
  interpro_description: Not specified in InterPro
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 18
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: PTHR24177-deep-research-falcon_artifacts/artifact-00.md
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
- **Accession:** PTHR24177
- **Name:** CASKIN
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** None (top-level entry)
- **Member database signatures:** Not specified
- **Scale:** 12734 proteins across 977 taxa, 116 subfamilies
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
**PTHR24177 (CASKIN)**, structured to support GO annotation review.

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
- **Accession:** PTHR24177
- **Name:** CASKIN
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** None (top-level entry)
- **Member database signatures:** Not specified
- **Scale:** 12734 proteins across 977 taxa, 116 subfamilies
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
**PTHR24177 (CASKIN)**, structured to support GO annotation review.

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


# InterPro Family Research Report: PTHR24177 (CASKIN)

## Executive Summary

InterPro entry PTHR24177 represents the CASKIN (CASK-Interacting Protein) family, a metazoan-specific family of multidomain scaffold proteins spanning 12,734 proteins across 977 taxa with 116 subfamilies. Currently, **no InterPro2GO terms are mapped to this entry**. This comprehensive review, based on recent structural, biochemical, and functional studies (2011-2024), identifies CASKIN proteins as protein-binding scaffolds rather than enzymes, with significant functional divergence between subfamilies that necessitates conservative family-level GO annotation.

> **InterPro entry under review:** PTHR24177, **CASKIN**, family-type entry; currently **no InterPro2GO terms are mapped**. Available evidence supports treating CASKIN as a **multidomain scaffold/adaptor family**, not an enzyme family. In vertebrate CASKIN proteins, the N-terminal half typically contains **six ankyrin repeats, one SH3 domain, and tandem SAM domains (SAM1-SAM2)**, followed by a **long proline-rich/disordered region** and a **conserved C-terminal region/LD motif**; CASKIN1 additionally contains a **CASK interaction domain (CID)** between SH3 and SAM1, whereas CASKIN2 lacks this CID. Primary structural and cell-biological studies consistently describe CASKIN proteins as scaffold proteins organizing multiprotein complexes rather than catalyzing chemical reactions (smirnova2016anewmode pages 1-2, stafford2011tandemsamdomain pages 1-2, wang2024caskin2isa pages 3-5).
>
> **1. Family definition and biochemistry.** CASKIN proteins are best understood as **protein-binding scaffolds** whose conserved biochemical core is mediated by modular interaction domains rather than catalytic residues. The tandem SAM domains are the best-characterized structural module. For **CASKIN1**, X-ray crystallography showed that SAM1 and SAM2 each adopt the canonical **five-helix SAM fold** and assemble into an **intramolecular head-to-tail arrangement** that extends into a **helical polymer/fibril** through conserved **mid-loop (ML)** and **end-helix (EH)** interfaces; polymerization is strongly influenced by electrostatic interactions, and mutations such as **G520E** and **G566K** disrupt polymerization. The adjacent CID allows assembly of **CASK** onto the CASKIN1 SAM polymer, further supporting a scaffold model (stafford2011tandemsamdomain pages 2-3, stafford2011tandemsamdomain pages 3-4, stafford2011tandemsamdomain pages 5-6). For **CASKIN2**, crystal/NMR work showed a distinct oligomerization mode: the tandem SAMs form a **domain-swapped dimer** rather than the linear CASKIN1 polymer, and isolated **SAM1 is partially disordered/less stably folded** whereas SAM2 is better folded, indicating domain-coupled stabilization and a different assembly logic from CASKIN1 (smirnova2016anewmode pages 1-2, clements2023thestructuraldynamics pages 4-6, clements2023thestructuraldynamics pages 6-8). Recent structural work further showed that the **C-terminal LD motif of CASKIN2** binds the **R8 domain of talin** in a helical conformation, effectively forming a five-helix bundle with talin; residues with major buried surface contribution include **L1183, F1190, L1197, and L1201**, and mutation of these residues abolishes talin binding (wang2024caskin2isa pages 3-5). Across the family, therefore, the strongest mechanistic claim that appears broadly true is **specific protein-binding/scaffold activity via conserved interaction modules**; there is no evidence that CASKIN proteins are catalytic enzymes or that the family is defined by conserved catalytic residues (smirnova2016anewmode pages 1-2, stafford2011tandemsamdomain pages 1-2, wang2024caskin2isa pages 3-5).
>
> **2. InterPro2GO mapping appropriateness.** Because **no GO terms are currently mapped**, the review question is whether family-level GO additions would be safe. The evidence argues for **caution**. A family-level mapping to broad **molecular function** terms such as **protein binding** or a scaffold-like binding role is defensible because all characterized members are multidomain adaptors whose conserved architecture mediates protein-protein interactions (smirnova2016anewmode pages 1-2, stafford2011tandemsamdomain pages 1-2, mehrabipour2023asystematiccompilation pages 11-13, wang2024caskin2isa pages 3-5). In contrast, **process terms** such as **axon guidance**, **cell migration**, **synapse organization**, or **component terms** such as **synapse**, **presynaptic active zone**, **focal adhesion**, or **cortical microtubule stabilization complex** would be over-broad at the PTHR24177 family level, because they are only demonstrated for subsets of the family: Drosophila Caskin is implicated in **Lar/LAR-RPTP-dependent motor axon guidance**; vertebrate CASKIN1 is linked to neuronal/presynaptic scaffolding; and vertebrate CASKIN2 is linked to **talin/Abi1/WAVE-associated cell adhesion and migration** (weng2011thecytoplasmicadaptor pages 1-2, weng2011thecytoplasmicadaptor pages 6-8, wang2024caskin2isa pages 3-5, wang2024caskin2isa pages 7-9). Thus, if any GO is added at this parent family, it should be restricted to **broad, non-process, non-compartment core molecular functions**. More specific neuronal, synaptic, adhesion, or migration GO terms should be reserved for **child entries/subfamilies** or manual gene-level annotation supported by direct evidence.
>
> **3. Functional divergence across the family.** The family is **not functionally homogeneous**. **CASKIN1** is strongly associated with neuronal scaffolding: it contains the **CID** that mediates direct interaction with the **CaMK domain of CASK**, and its tandem SAMs form **linear/helical oligomers** compatible with presynaptic scaffold assembly (stafford2011tandemsamdomain pages 1-2, stafford2011tandemsamdomain pages 5-6). **CASKIN2**, despite similar overall architecture, **lacks the CID** and therefore does **not bind CASK** in the same way; instead, it shows distinct SAM assembly behavior and, in recent experiments, directly binds **talin** through its C-terminal LD motif and **Abi1** through its proline-rich region, promoting **cell motility** and localizing near focal-adhesion/CMSC-associated structures (smirnova2016anewmode pages 1-2, wang2024caskin2isa pages 3-5, wang2024caskin2isa pages 7-9). A 2023 review on multi-SAM proteins summarizes this divergence as **linear fibril-like oligomers for CASKIN1** versus **branched oligomers of dimers for CASKIN2** (clements2023thestructuraldynamics pages 4-6, clements2023thestructuraldynamics pages 6-8). In **Drosophila**, a single Caskin homolog functions in **Lar receptor signaling during motor axon guidance** and physically binds Lar through its **N-terminal SAM domain**; vertebrate mouse Caskin2 SAM domains can also interact with LAR family receptors in yeast assays, suggesting conservation of an ancestral adaptor role with later vertebrate specialization (weng2011thecytoplasmicadaptor pages 1-2, weng2011thecytoplasmicadaptor pages 6-8). There is **no evidence of pseudo-enzyme evolution**, because the family is not enzyme-derived; the main divergence is in **binding partners, oligomer architecture, expression pattern, and cellular context**, not loss of catalysis.
>
> **4. Taxonomic scope.** Available evidence indicates that CASKIN is a **metazoan** scaffold family with lineage-specific expansion. A **single homolog** is present in **Drosophila** and was experimentally characterized in axon guidance, whereas **no homolog was observed in C. elegans** in the cited structural study background. Mammals possess at least **CASKIN1 and CASKIN2**, consistent with duplication and subfunctionalization/neofunctionalization in vertebrates (smirnova2016anewmode pages 1-2, weng2011thecytoplasmicadaptor pages 1-2). The InterPro summary supplied for this review reports **12,734 proteins across 977 taxa and 116 subfamilies**, implying a large and evolutionarily diversified animal family. That breadth reinforces the annotation risk: a conserved family-level claim may extend only to **multidomain protein-binding scaffold function**, whereas specific pathways or compartments are unlikely to hold across all taxa and subfamilies.
>
> **5. Over-annotation verdict and GO action pattern.** With **no current mappings**, the immediate risk is not over-annotation from existing InterPro2GO terms but rather **future over-broad annotation if specific terms are added at the parent family**. Recommended verdict: **family-level annotation should be conservative**. For broad molecular-function terms that are true of essentially all members, the action pattern would be **ACCEPT** or **KEEP_AS_NON_CORE**. For any proposed specific process/component terms related to **axon guidance, synaptic organization, presynapse, focal adhesion, cortical microtubule stabilization complexes, or cell migration**, the recommended action is **MODIFY-to-specific** at an appropriate child/subfamily entry or **do not map at the parent family level** (weng2011thecytoplasmicadaptor pages 1-2, wang2024caskin2isa pages 3-5, wang2024caskin2isa pages 7-9, weng2011thecytoplasmicadaptor pages 6-8). Overall verdict: **PTHR24177 is functionally diverse enough that parent-family GO should be limited to broad scaffold/protein-binding concepts; specialized neuronal or adhesion annotations belong below the family level.**


*Blockquote: This blockquote summarizes the evidence base for reviewing GO annotation of InterPro family PTHR24177 (CASKIN), emphasizing conserved scaffold features, subfamily divergence, taxonomic scope, and conservative family-level annotation recommendations.*

## Key Findings and Recommendations

### 1. Family Definition and Biochemistry

CASKIN proteins are **non-catalytic scaffold/adaptor proteins** characterized by a conserved multidomain architecture. The core domain organization includes: **six ankyrin repeats** (N-terminal), an **SH3 domain**, **tandem SAM domains (SAM1-SAM2)**, an extended **proline-rich region (PRR)**, and a **C-terminal domain containing an LD motif** (smirnova2016anewmode pages 1-2, wang2024caskin2isa pages 1-3, wang2024caskin2isa pages 3-5).

High-resolution structural studies have elucidated the molecular mechanisms of CASKIN scaffolding:

**CASKIN1 Structure and Oligomerization:** X-ray crystallography at 2.4 Å resolution revealed that the tandem SAM domains form an intramolecular head-to-tail arrangement, with SAM1 binding SAM2 through conserved mid-loop (ML) and end-helix (EH) interfaces. This tandem unit further oligomerizes into **helical fibrils** containing eight SAM domains per helical turn with an unusually long pitch. Key polymer interface residues include **G520, G566, Y567, and F572**; mutations G520E and G566K disrupt polymerization. The polymer formation is highly salt-dependent, with electrostatic interactions playing a crucial regulatory role (stafford2011tandemsamdomain pages 2-3, stafford2011tandemsamdomain pages 3-4, stafford2011tandemsamdomain pages 1-2, stafford2011tandemsamdomain pages 5-6).

**CASKIN2 Structure and Oligomerization:** Distinct from CASKIN1, CASKIN2 SAM domains adopt a **domain-swapped dimer** architecture. NMR and crystal structure analysis showed that **SAM1 is partially disordered** when expressed alone but is stabilized upon interaction with SAM2. The minimal repeating unit is a dimer rather than a monomer, leading to **branched oligomeric structures** rather than the linear fibrils of CASKIN1 (smirnova2016anewmode pages 1-2, clements2023thestructuraldynamics pages 4-6, clements2023thestructuraldynamics pages 6-8).

**Binding Interfaces:** Recent crystallographic work (2024) determined the structure of CASKIN2's C-terminal LD motif bound to talin R8 domain at 2.7 Å resolution. The LD peptide forms a helical structure that packs against talin R8, creating a five-helix bundle. Critical binding residues include **L1183, F1190, L1197, and L1201**, with mutation of these residues abolishing talin interaction (wang2024caskin2isa pages 3-5, wang2024caskin2isa pages 1-3).

**No Catalytic Function:** Across all characterized family members, there is no evidence of enzymatic activity or conserved catalytic residues. CASKIN proteins function exclusively through **protein-protein interaction-mediated scaffolding** (smirnova2016anewmode pages 1-2, stafford2011tandemsamdomain pages 1-2, mehrabipour2023asystematiccompilation pages 11-13).

### 2. InterPro2GO Mapping Appropriateness

Given that **no GO terms are currently mapped** to PTHR24177, the critical question is what terms would be appropriate at the family level.

**Safe Family-Level Annotations:**
- Broad **molecular function** terms such as **protein binding** (GO:0005515) or **scaffold protein binding** are defensible because all characterized members mediate protein-protein interactions through their conserved modular domains (smirnova2016anewmode pages 1-2, stafford2011tandemsamdomain pages 1-2, mehrabipour2023asystematiccompilation pages 11-13, wang2024caskin2isa pages 3-5).

**Terms That Should NOT Be Mapped at Family Level:**
The following would constitute over-annotation because they apply only to specific subfamilies:

1. **Process terms** such as:
   - Axon guidance (specific to Drosophila Caskin and potentially vertebrate CASKIN1)
   - Cell migration (specific to CASKIN2)
   - Synapse organization/assembly (CASKIN1-specific)
   
2. **Component terms** such as:
   - Synapse/presynaptic active zone (CASKIN1 in neurons)
   - Focal adhesion (CASKIN2)
   - Cortical microtubule stabilization complex (CASKIN2)

These specific annotations should be reserved for **subfamily-level entries** or applied through manual curation with direct experimental evidence (weng2011thecytoplasmicadaptor pages 1-2, wang2024caskin2isa pages 3-5, wang2024caskin2isa pages 7-9, weng2011thecytoplasmicadaptor pages 6-8).

### 3. Functional Divergence Across the Family

The CASKIN family exhibits **substantial functional heterogeneity** across subfamilies:

**CASKIN1 Subfamily:**
- Contains a **CASK Interaction Domain (CID)** between the SH3 and SAM1 domains
- Binds the CaMK domain of CASK, a MAGUK scaffolding protein
- Predominantly **brain-specific** expression
- Functions in **neuronal/presynaptic scaffolding**
- Forms **linear helical SAM oligomers** that can be decorated by CASK
- Implicated in synaptic vesicle organization and neurotransmitter release
- Associated with neurodevelopmental functions
(stafford2011tandemsamdomain pages 2-3, stafford2011tandemsamdomain pages 3-4, stafford2011tandemsamdomain pages 1-2, stafford2011tandemsamdomain pages 5-6)

**CASKIN2 Subfamily:**
- **Lacks the CID domain** and therefore does not bind CASK
- **Broadly expressed** in non-neuronal tissues (Human Protein Atlas)
- Binds **talin** through C-terminal LD motif (Kd ~2.7 μM)
- Binds **Abi1** through proline-rich region (PxxPxR motif at residues 870-875)
- Recruits WAVE Regulatory Complex components (Wasf1/2, Cyfip1/2, Nckap1)
- **Promotes cell motility** (~45% increase in migration speed)
- Localizes to **focal adhesions** and **cortical microtubule stabilization complexes (CMSCs)**
- Interaction with Abi1 is **regulated by phosphorylation** at S878 (growth factor-induced via EGFR/MEK pathway)
- Forms **branched SAM dimers** rather than linear fibrils
(smirnova2016anewmode pages 1-2, wang2024caskin2isa pages 1-3, wang2024caskin2isa pages 3-5, wang2024caskin2isa pages 7-9)

**Invertebrate Caskin (Drosophila):**
- Single homolog (Ckn)
- Mediates **LAR receptor protein tyrosine phosphatase** signaling
- Required for **motor axon pathfinding** during embryonic development
- Binds LAR through **N-terminal SAM domain** (D2 phosphatase domain of LAR)
- Also binds Dock (SH2/SH3 adaptor)
- Overlapping roles with Dock in CNS axon outgrowth
- Mouse Caskin2 SAM domains can interact with vertebrate LAR family members, suggesting evolutionary conservation of receptor binding
(weng2011thecytoplasmicadaptor pages 1-2, weng2011thecytoplasmicadaptor pages 6-8, weng2011thecytoplasmicadaptor pages 2-3)

**No Pseudo-enzyme Members:** CASKIN proteins are scaffolds, not derived from enzymes, so there are no catalytically inactive "pseudo-enzyme" variants. The divergence is in **binding partner specificity**, **oligomerization architecture**, **tissue expression**, and **cellular localization**, not loss of catalytic activity (smirnova2016anewmode pages 1-2, clements2023thestructuraldynamics pages 6-8).

### 4. Taxonomic Scope

The CASKIN family exhibits a **metazoan-specific distribution** with lineage-dependent gene copy number:

- **Invertebrates:** Single Caskin gene in Drosophila melanogaster; **absent in C. elegans**
- **Vertebrates:** Gene duplication yielding CASKIN1 and CASKIN2 with subfunctionalization
- **Breadth:** 12,734 proteins across 977 taxa with 116 subfamilies (InterPro data)

This taxonomic distribution indicates an **ancient metazoan scaffold function** with the core scaffolding mechanism (SAM-mediated oligomerization, multidomain protein binding) conserved across the family. However, **specific binding partners and cellular contexts diversified** following vertebrate duplication:
- CASKIN1 evolved neuronal specialization with CASK binding
- CASKIN2 evolved adhesion/migration functions with talin/integrin pathway integration
- Invertebrate Caskin maintained receptor tyrosine phosphatase signaling functions

The broad taxonomic scope (977 taxa) means that **any GO term mapped at the family level must be true across invertebrates and vertebrates, neuronal and non-neuronal contexts** (smirnova2016anewmode pages 1-2, weng2011thecytoplasmicadaptor pages 1-2, weng2011thecytoplasmicadaptor pages 6-8).

### 5. Over-annotation Verdict and Recommended GO Action Patterns

**Current Status:** No InterPro2GO terms are mapped to PTHR24177.

**Assessment:** This is a **family-type entry** that could theoretically support whole-protein function terms, but only if the family is functionally homogeneous. The evidence clearly demonstrates **functional divergence across 116 subfamilies**, with distinct binding partners, cellular localizations, and biological processes.

**Verdict: CONSERVATIVE FAMILY-LEVEL ANNOTATION REQUIRED**

**Recommended Action Patterns:**

1. **For broad molecular function terms** (e.g., protein binding, scaffolding activity) applicable to all members:
   - **Action: ACCEPT** or **KEEP_AS_NON_CORE**
   - Rationale: All CASKIN proteins mediate protein-protein interactions through conserved domains

2. **For subfamily-specific process terms** (axon guidance, cell migration, synapse organization, integrin-mediated adhesion):
   - **Action: MODIFY-to-specific** (move to appropriate subfamily entry) or **DO NOT MAP at parent level**
   - Rationale: These processes are restricted to specific subfamilies and would over-annotate the entire family

3. **For subfamily-specific component terms** (synapse, presynaptic active zone, focal adhesion, CMSC):
   - **Action: MODIFY-to-specific** (move to appropriate subfamily entry) or **DO NOT MAP at parent level**
   - Rationale: Cellular localizations vary between CASKIN1 (neuronal/synaptic) and CASKIN2 (adhesion sites)

4. **For terms that leak across taxa** (specific synaptic processes absent in invertebrates):
   - **Action: REMOVE** from family level or **MARK_AS_OVER_ANNOTATED**
   - Rationale: Not valid across the 977 taxa represented

**Overall Recommendation:** PTHR24177 should receive **minimal, conservative family-level GO annotation** limited to core molecular functions (protein binding/scaffolding). Specialized neuronal, synaptic, adhesion, and migration annotations should be delegated to **subfamily-specific entries** (e.g., separate entries for CASKIN1 vs. CASKIN2 subfamilies) or applied through manual gene-level curation with direct experimental support.

**InterPro Recommendation:** Consider creating or annotating **child subfamily entries** within PTHR24177 to enable more specific GO term mapping that reflects the functional diversification between CASKIN1-like and CASKIN2-like proteins.

## Recent Research Developments (2023-2024)

Recent authoritative studies continue to refine understanding of CASKIN structure-function relationships:

1. **Wang et al. (2024), Journal of Cell Science** - First crystal structure of CASKIN2-talin complex, revealing mechanism of integrin adhesion regulation and identification of phosphorylation-dependent Abi1 binding (doi:10.1242/jcs.262116) (wang2024caskin2isa pages 1-3, wang2024caskin2isa pages 3-5, wang2024caskin2isa pages 7-9)

2. **Mehrabipour et al. (2023), Cells** - Systematic compilation of human SH3 domain proteins identifying CASKIN1/2 as representative scaffold proteins enabling multiprotein complex organization (doi:10.3390/cells12162054) (mehrabipour2023asystematiccompilation pages 11-13)

3. **Clements et al. (2023), Cancers** - Comprehensive review of multi-SAM containing proteins documenting distinct oligomerization modes and structural dynamics of CASKIN1 vs. CASKIN2, including characterization of intrinsic disorder in CASKIN2 SAM1 (doi:10.3390/cancers15113019) (clements2023thestructuraldynamics pages 4-6, clements2023thestructuraldynamics pages 6-8, clements2023thestructuraldynamics pages 8-9)

These studies employed advanced techniques including X-ray crystallography, NMR spectroscopy, analytical ultracentrifugation, AlphaFold2 modeling, and mass spectrometry-based proteomics.

## Conclusion

The CASKIN family (PTHR24177) represents a functionally diverse set of metazoan scaffold proteins united by conserved multidomain architecture but divergent in binding partners, oligomerization modes, and biological contexts. The absence of current InterPro2GO mappings provides an opportunity for **conservative, evidence-based annotation** that avoids over-annotation pitfalls. Family-level GO terms should be restricted to broad molecular functions universally true across all 12,734 proteins in 977 taxa. Specific process and component annotations should be delegated to subfamily-level entries to accurately reflect the functional specialization of CASKIN1 (neuronal scaffolding), CASKIN2 (adhesion/migration), and invertebrate Caskin (receptor signaling) subfamilies.

References

1. (smirnova2016anewmode pages 1-2): Ekaterina Smirnova, Jamie J. Kwan, Ryan Siu, Xin Gao, Georg Zoidl, Borries Demeler, Vivian Saridakis, and Logan W. Donaldson. A new mode of sam domain mediated oligomerization observed in the caskin2 neuronal scaffolding protein. Cell Communication and Signaling, Aug 2016. URL: https://doi.org/10.1186/s12964-016-0140-3, doi:10.1186/s12964-016-0140-3. This article has 20 citations and is from a peer-reviewed journal.

2. (stafford2011tandemsamdomain pages 1-2): Ryan L. Stafford, Elizabeth Hinde, Mary Jane Knight, Mario A. Pennella, Jason Ear, Michelle A. Digman, Enrico Gratton, and James U. Bowie. Tandem sam domain structure of human caskin1: a presynaptic, self-assembling scaffold for cask. Structure, 19 12:1826-36, Dec 2011. URL: https://doi.org/10.1016/j.str.2011.09.018, doi:10.1016/j.str.2011.09.018. This article has 36 citations and is from a domain leading peer-reviewed journal.

3. (wang2024caskin2isa pages 3-5): Wei Wang, Paul Atherton, Maaike Kreft, Lisa te Molder, Sabine van der Poel, Liesbeth Hoekman, Patrick Celie, Robbie P. Joosten, Reinhard Fässler, Anastassis Perrakis, and Arnoud Sonnenberg. Caskin2 is a novel talin- and abi1-binding protein that promotes cell motility. Journal of Cell Science, May 2024. URL: https://doi.org/10.1242/jcs.262116, doi:10.1242/jcs.262116. This article has 6 citations and is from a domain leading peer-reviewed journal.

4. (stafford2011tandemsamdomain pages 2-3): Ryan L. Stafford, Elizabeth Hinde, Mary Jane Knight, Mario A. Pennella, Jason Ear, Michelle A. Digman, Enrico Gratton, and James U. Bowie. Tandem sam domain structure of human caskin1: a presynaptic, self-assembling scaffold for cask. Structure, 19 12:1826-36, Dec 2011. URL: https://doi.org/10.1016/j.str.2011.09.018, doi:10.1016/j.str.2011.09.018. This article has 36 citations and is from a domain leading peer-reviewed journal.

5. (stafford2011tandemsamdomain pages 3-4): Ryan L. Stafford, Elizabeth Hinde, Mary Jane Knight, Mario A. Pennella, Jason Ear, Michelle A. Digman, Enrico Gratton, and James U. Bowie. Tandem sam domain structure of human caskin1: a presynaptic, self-assembling scaffold for cask. Structure, 19 12:1826-36, Dec 2011. URL: https://doi.org/10.1016/j.str.2011.09.018, doi:10.1016/j.str.2011.09.018. This article has 36 citations and is from a domain leading peer-reviewed journal.

6. (stafford2011tandemsamdomain pages 5-6): Ryan L. Stafford, Elizabeth Hinde, Mary Jane Knight, Mario A. Pennella, Jason Ear, Michelle A. Digman, Enrico Gratton, and James U. Bowie. Tandem sam domain structure of human caskin1: a presynaptic, self-assembling scaffold for cask. Structure, 19 12:1826-36, Dec 2011. URL: https://doi.org/10.1016/j.str.2011.09.018, doi:10.1016/j.str.2011.09.018. This article has 36 citations and is from a domain leading peer-reviewed journal.

7. (clements2023thestructuraldynamics pages 4-6): Christopher M. Clements, Morkos A. Henen, Beat Vögeli, and Yiqun G. Shellman. The structural dynamics, complexity of interactions, and functions in cancer of multi-sam containing proteins. Cancers, 15:3019, Jun 2023. URL: https://doi.org/10.3390/cancers15113019, doi:10.3390/cancers15113019. This article has 10 citations.

8. (clements2023thestructuraldynamics pages 6-8): Christopher M. Clements, Morkos A. Henen, Beat Vögeli, and Yiqun G. Shellman. The structural dynamics, complexity of interactions, and functions in cancer of multi-sam containing proteins. Cancers, 15:3019, Jun 2023. URL: https://doi.org/10.3390/cancers15113019, doi:10.3390/cancers15113019. This article has 10 citations.

9. (mehrabipour2023asystematiccompilation pages 11-13): Mehrnaz Mehrabipour, Neda S. Kazemein Jasemi, Radovan Dvorsky, and Mohammad R. Ahmadian. A systematic compilation of human sh3 domains: a versatile superfamily in cellular signaling. Cells, 12:2054, Aug 2023. URL: https://doi.org/10.3390/cells12162054, doi:10.3390/cells12162054. This article has 50 citations.

10. (weng2011thecytoplasmicadaptor pages 1-2): Yi-Lan Weng, Nan Liu, Aaron DiAntonio, and Heather T. Broihier. The cytoplasmic adaptor protein caskin mediates lar signal transduction during drosophila motor axon guidance. The Journal of Neuroscience, 31:4421-4433, Mar 2011. URL: https://doi.org/10.1523/jneurosci.5230-10.2011, doi:10.1523/jneurosci.5230-10.2011. This article has 44 citations.

11. (weng2011thecytoplasmicadaptor pages 6-8): Yi-Lan Weng, Nan Liu, Aaron DiAntonio, and Heather T. Broihier. The cytoplasmic adaptor protein caskin mediates lar signal transduction during drosophila motor axon guidance. The Journal of Neuroscience, 31:4421-4433, Mar 2011. URL: https://doi.org/10.1523/jneurosci.5230-10.2011, doi:10.1523/jneurosci.5230-10.2011. This article has 44 citations.

12. (wang2024caskin2isa pages 7-9): Wei Wang, Paul Atherton, Maaike Kreft, Lisa te Molder, Sabine van der Poel, Liesbeth Hoekman, Patrick Celie, Robbie P. Joosten, Reinhard Fässler, Anastassis Perrakis, and Arnoud Sonnenberg. Caskin2 is a novel talin- and abi1-binding protein that promotes cell motility. Journal of Cell Science, May 2024. URL: https://doi.org/10.1242/jcs.262116, doi:10.1242/jcs.262116. This article has 6 citations and is from a domain leading peer-reviewed journal.

13. (wang2024caskin2isa pages 1-3): Wei Wang, Paul Atherton, Maaike Kreft, Lisa te Molder, Sabine van der Poel, Liesbeth Hoekman, Patrick Celie, Robbie P. Joosten, Reinhard Fässler, Anastassis Perrakis, and Arnoud Sonnenberg. Caskin2 is a novel talin- and abi1-binding protein that promotes cell motility. Journal of Cell Science, May 2024. URL: https://doi.org/10.1242/jcs.262116, doi:10.1242/jcs.262116. This article has 6 citations and is from a domain leading peer-reviewed journal.

14. (weng2011thecytoplasmicadaptor pages 2-3): Yi-Lan Weng, Nan Liu, Aaron DiAntonio, and Heather T. Broihier. The cytoplasmic adaptor protein caskin mediates lar signal transduction during drosophila motor axon guidance. The Journal of Neuroscience, 31:4421-4433, Mar 2011. URL: https://doi.org/10.1523/jneurosci.5230-10.2011, doi:10.1523/jneurosci.5230-10.2011. This article has 44 citations.

15. (clements2023thestructuraldynamics pages 8-9): Christopher M. Clements, Morkos A. Henen, Beat Vögeli, and Yiqun G. Shellman. The structural dynamics, complexity of interactions, and functions in cancer of multi-sam containing proteins. Cancers, 15:3019, Jun 2023. URL: https://doi.org/10.3390/cancers15113019, doi:10.3390/cancers15113019. This article has 10 citations.

## Artifacts

- [Edison artifact artifact-00](PTHR24177-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. mehrabipour2023asystematiccompilation pages 11-13
2. smirnova2016anewmode pages 1-2
3. stafford2011tandemsamdomain pages 1-2
4. stafford2011tandemsamdomain pages 2-3
5. stafford2011tandemsamdomain pages 3-4
6. stafford2011tandemsamdomain pages 5-6
7. clements2023thestructuraldynamics pages 4-6
8. clements2023thestructuraldynamics pages 6-8
9. weng2011thecytoplasmicadaptor pages 1-2
10. weng2011thecytoplasmicadaptor pages 6-8
11. weng2011thecytoplasmicadaptor pages 2-3
12. clements2023thestructuraldynamics pages 8-9
13. https://doi.org/10.1186/s12964-016-0140-3,
14. https://doi.org/10.1016/j.str.2011.09.018,
15. https://doi.org/10.1242/jcs.262116,
16. https://doi.org/10.3390/cancers15113019,
17. https://doi.org/10.3390/cells12162054,
18. https://doi.org/10.1523/jneurosci.5230-10.2011,