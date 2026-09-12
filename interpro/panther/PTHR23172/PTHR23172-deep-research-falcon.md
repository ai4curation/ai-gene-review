---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-21T20:46:25.608758'
end_time: '2026-06-21T20:58:58.400978'
duration_seconds: 752.79
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR23172
  interpro_name: Clathrin-mediated endocytosis auxilin-like protein
  interpro_short_name: CME_auxilin-like
  interpro_type: family
  interpro_integrated: None (top-level entry)
  member_databases: Not specified
  n_proteins: '10009'
  n_taxa: '7490'
  n_subfamilies: '23'
  interpro2go_terms: None mapped (no InterPro2GO terms for this entry)
  interpro_description: This family of proteins is involved in the process of clathrin-mediated
    endocytosis and vesicular trafficking. Members of this family function primarily
    by recruiting HSPA8/HSC70 to clathrin-coated vesicles, promoting the uncoating
    process necessary for the fusion of vesicles with target membranes and the recycling
    of clathrin components. Some members are also implicated in the regulation of
    chloroplast movement in response to light and may contribute to resistance to
    environmental stressors such as aluminum. Additionally, certain members associate
    with cyclin G and CDK5, and their expression may vary throughout the cell cycle.
    The family includes proteins with J domains that interact with Hsp70-type chaperones,
    stimulating their ATPase activity to facilitate clathrin coat disassembly.
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 32
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PTHR23172-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR23172-deep-research-falcon_artifacts/artifact-01.md
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
- **Accession:** PTHR23172
- **Name:** Clathrin-mediated endocytosis auxilin-like protein
- **Short name:** CME_auxilin-like
- **Entry type:** family
- **Integrated into / parent:** None (top-level entry)
- **Member database signatures:** Not specified
- **Scale:** 10009 proteins across 7490 taxa, 23 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** This family of proteins is involved in the process of clathrin-mediated endocytosis and vesicular trafficking. Members of this family function primarily by recruiting HSPA8/HSC70 to clathrin-coated vesicles, promoting the uncoating process necessary for the fusion of vesicles with target membranes and the recycling of clathrin components. Some members are also implicated in the regulation of chloroplast movement in response to light and may contribute to resistance to environmental stressors such as aluminum. Additionally, certain members associate with cyclin G and CDK5, and their expression may vary throughout the cell cycle. The family includes proteins with J domains that interact with Hsp70-type chaperones, stimulating their ATPase activity to facilitate clathrin coat disassembly.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR23172 (Clathrin-mediated endocytosis auxilin-like protein)**, structured to support GO annotation review.

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
- **Accession:** PTHR23172
- **Name:** Clathrin-mediated endocytosis auxilin-like protein
- **Short name:** CME_auxilin-like
- **Entry type:** family
- **Integrated into / parent:** None (top-level entry)
- **Member database signatures:** Not specified
- **Scale:** 10009 proteins across 7490 taxa, 23 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** This family of proteins is involved in the process of clathrin-mediated endocytosis and vesicular trafficking. Members of this family function primarily by recruiting HSPA8/HSC70 to clathrin-coated vesicles, promoting the uncoating process necessary for the fusion of vesicles with target membranes and the recycling of clathrin components. Some members are also implicated in the regulation of chloroplast movement in response to light and may contribute to resistance to environmental stressors such as aluminum. Additionally, certain members associate with cyclin G and CDK5, and their expression may vary throughout the cell cycle. The family includes proteins with J domains that interact with Hsp70-type chaperones, stimulating their ATPase activity to facilitate clathrin coat disassembly.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR23172 (Clathrin-mediated endocytosis auxilin-like protein)**, structured to support GO annotation review.

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


# Comprehensive Research Report: InterPro Entry PTHR23172 (Clathrin-mediated endocytosis auxilin-like protein)

## Executive Summary

InterPro entry PTHR23172 represents a family of auxilin-like proteins spanning 10,009 proteins across 7,490 taxa with 23 subfamilies. **Critical finding: This is a functionally heterogeneous family** that cannot be assigned uniform whole-protein GO terms without substantial over-annotation. The entry currently has no InterPro2GO mappings, which is appropriate given the documented functional divergence. This report provides evidence-based recommendations for GO annotation strategy.

---

## 1. Family Definition and Biochemistry

### 1.1 Core Structural Architecture

The canonical animal auxilin architecture comprises three conserved domains (roosen2019dnajcproteinsand pages 3-7, park2015theclathrinbindingand pages 1-2):

**N-terminal PTEN-like domain:** This domain binds phosphatidylinositol phosphate head groups, particularly PI(4,5)P2, and facilitates membrane targeting to clathrin-coated vesicles (roosen2019dnajcproteinsand pages 3-7, he2020dynamicsofauxilin pages 1-2). Despite structural similarity to PTEN phosphatase, this domain lacks catalytic phosphatase activity and functions purely in membrane/lipid recognition (roosen2019dnajcproteinsand pages 3-7). The PTEN-like domain contributes to a proposed "lipid-switch" timing mechanism that distinguishes newly budded vesicles from assembling pits, as auxilins are absent from assembling pits and recruited only after dynamin-mediated scission (he2020dynamicsofauxilin pages 1-2).

**Clathrin-binding domain:** This central region contains multiple clathrin-binding boxes that directly engage the clathrin coat on coated vesicles (roosen2019dnajcproteinsand pages 3-7, joshi2020chaperonesandproteostasis pages 11-13). The clathrin-binding domain positions auxilin on the vesicle surface and is subject to regulatory phosphorylation; for example, auxilin S627 (in the clathrin-binding region) is phosphorylated by LRRK2, modulating clathrin association (nguyen2019synapticmitochondrialand pages 4-6).

**C-terminal J-domain:** The J-domain is the defining feature of the DNAJ protein family and contains the conserved HPD catalytic motif essential for recruiting Hsc70/HSPA8 and stimulating its ATPase activity (roosen2019dnajcproteinsand pages 3-7, joshi2020chaperonesandproteostasis pages 11-13, he2020dynamicsofauxilin pages 1-2). This is the **most universally conserved mechanistic feature** across the family. The J-domain-Hsc70 interaction couples ATP hydrolysis to conformational changes in clathrin, driving coat disassembly (roosen2019dnajcproteinsand pages 3-7, he2020dynamicsofauxilin pages 1-2).

**Minimal functional module:** In vitro and in vivo rescue experiments demonstrate that the clathrin-binding domain plus J-domain are **necessary and sufficient** for Hsc70-mediated clathrin uncoating, whereas the PTEN-like domain enhances efficiency but is not absolutely required (park2015theclathrinbindingand pages 1-2).

### 1.2 Mechanistic Biochemistry of Clathrin Uncoating

The canonical mechanism in animal systems proceeds as follows (roosen2019dnajcproteinsand pages 3-7, he2020dynamicsofauxilin pages 1-2, ng2024dysfunctionofsynaptic pages 3-4):

1. Following dynamin-mediated vesicle scission, the newly formed clathrin-coated vesicle (CCV) displays altered phosphoinositide composition
2. Auxilin binds to the CCV through dual engagement: PTEN-like domain recognizes lipid heads, clathrin-binding domain engages the coat
3. The J-domain recruits Hsc70/HSPA8 to the CCV and stimulates Hsc70 ATPase activity
4. ATP hydrolysis by Hsc70 drives conformational changes in clathrin, inducing coat disassembly within seconds of vesicle release (he2020dynamicsofauxilin pages 1-2, abela2024neurodevelopmentalandsynaptic pages 1-2)
5. Hsc70 also chaperones dissociated clathrin to prevent cytosolic aggregation (roosen2019dnajcproteinsand pages 3-7)

Single-molecule imaging confirms that auxilin recruitment occurs in transient bursts immediately after scission, with even 4-6 molecules sufficient to mediate uncoating (he2020dynamicsofauxilin pages 1-2). Knockout or depletion of auxilin results in accumulation of clathrin-coated vesicles and empty clathrin cages at synapses, confirming its essential uncoating role (cheng2023impairedpresynapticplasticity pages 1-2, abela2024neurodevelopmentalandsynaptic pages 1-2, ng2024dysfunctionofsynaptic pages 3-4).

| Domain/Feature | Function | Conservation across family | Key references |
|---|---|---|---|
| N-terminal PTEN-like domain | Binds phosphoinositide head groups and helps recruit auxilin-family proteins to newly budded clathrin-coated vesicles; described as PTEN-like in fold but catalytically inactive as a phosphatase | Conserved in canonical auxilin/DNAJC6 and GAK/auxilin-2; broadly present in animal auxilin-like proteins involved in clathrin traffic. Not a reliable marker for all divergent family members because plant auxilin-like proteins associated with chloroplast movement are defined primarily by J-domain-based signaling roles rather than the canonical animal clathrin-uncoating architecture | (roosen2019dnajcproteinsand pages 3-7, park2015theclathrinbindingand pages 1-2, he2020dynamicsofauxilin pages 1-2) |
| PTEN-like domain lipid-recognition property | Recognizes phosphatidylinositol phosphate head groups, supporting timing of recruitment after vesicle scission; proposed to contribute to a lipid-switch mechanism that distinguishes coated vesicles from assembling pits | Well supported for mammalian Aux1 and GAK in clathrin-mediated traffic; should be treated as conserved mainly within the animal clathrin-uncoating branch, not assumed for all kingdom-wide matches | (he2020dynamicsofauxilin pages 1-2, roosen2019dnajcproteinsand pages 3-7) |
| Clathrin-binding domain / clathrin-binding boxes | Direct binding to clathrin coat on clathrin-coated vesicles; positions the protein on coated membranes and cooperates with the J-domain to support Hsc70-driven uncoating | Core conserved feature of animal auxilin-family members. Present in auxilin and GAK and sufficient together with the J-domain for uncoating support in vitro and in vivo rescue experiments. Divergent family members may not share the same vesicle-specific usage | (roosen2019dnajcproteinsand pages 3-7, park2015theclathrinbindingand pages 1-2, joshi2020chaperonesandproteostasis pages 11-13, ng2024dysfunctionofsynaptic pages 3-4) |
| Clathrin-binding domain residue-level regulatory feature | Includes regulatory phosphorylation sites that alter clathrin association; e.g., auxilin S627 in the clathrin-binding region modulates clathrin interaction downstream of LRRK2 signaling | Demonstrated for mammalian auxilin/DNAJC6; indicates functional conservation of clathrin engagement but also lineage-specific regulatory tuning | (nguyen2019synapticmitochondrialand pages 4-6) |
| C-terminal J-domain | Recruits Hsc70/HSPA8 and stimulates its ATPase activity, coupling ATP hydrolysis to clathrin coat disassembly | The most universally conserved defining feature across auxilin-like proteins in this family; central to both canonical clathrin uncoating and some divergent functions in other trafficking/autophagy contexts | (roosen2019dnajcproteinsand pages 3-7, joshi2020chaperonesandproteostasis pages 11-13, he2020dynamicsofauxilin pages 1-2, ng2024dysfunctionofsynaptic pages 3-4) |
| J-domain HPD catalytic motif / Hsp70-interaction module | Canonical J-domain co-chaperone element required for productive interaction with Hsp70-family chaperones and ATPase stimulation | Highly conserved across J-domain proteins and functionally central in auxilin-like proteins; strongest family-wide mechanistic feature for molecular function inference | (roosen2019dnajcproteinsand pages 3-7, he2020dynamicsofauxilin pages 1-2) |
| Minimal uncoating module: clathrin-binding domain + J-domain | Together are necessary and sufficient to support Hsc70-mediated clathrin basket uncoating; explains why the family’s core biochemical activity maps to these C-terminal regions | Conserved in animal auxilin/GAK branch; experimental rescue data show N-terminal regions are dispensable for basic uncoating activity but can improve efficiency or confer added regulation | (park2015theclathrinbindingand pages 1-2) |
| N-terminal Ser/Thr kinase domain (GAK only) | Additional catalytic module in GAK/DNAJC26; expands function beyond canonical auxilin by contributing to broader cellular regulation, including mitosis, autophagy/mitophagy, and tissue-specific trafficking requirements | Subfamily-specific, not family-wide. Present in GAK/auxilin-2 and some invertebrate homologs such as Drosophila auxilin-like proteins, but absent from neuronal auxilin/DNAJC6; therefore inappropriate as a pan-family feature | (park2015theclathrinbindingand pages 1-2, zhang2023cyclingassociatedkinasegakdaux pages 1-2, munson2021gakandprkcd pages 1-2, ng2024dysfunctionofsynaptic pages 3-4) |
| GAK uncoating domain with autophagy-linked interactions | In GAK/dAux, the uncoating-region/J-domain module also interacts with ULK1/Atg1 and regulates autophagy initiation, showing neo-functionalization layered onto the clathrin-uncoating scaffold | Restricted to GAK/dAux subfamily; evidence argues against assigning autophagy-initiation functions to the whole PTHR23172 family | (zhang2023cyclingassociatedkinasegakdaux pages 1-2, zhang2023cyclingassociatedkinasegakdaux pages 3-5) |
| Overall canonical animal architecture: PTEN-like + clathrin-binding + J-domain (± kinase in GAK) | Provides a modular mechanism for vesicle targeting, clathrin binding, and Hsc70 activation during rapid post-scission clathrin-coat disassembly | Strongly conserved in animal auxilin/DNAJC6 and GAK/DNAJC26. However, family-wide InterPro matches span many taxa and include divergent plant auxilin-like proteins with chloroplast-movement roles, so whole-family GO annotation should prioritize only the most universal mechanistic feature(s) | (roosen2019dnajcproteinsand pages 3-7, park2015theclathrinbindingand pages 1-2, he2020dynamicsofauxilin pages 1-2, suetsugu2016lightinducedmovementsof pages 1-2) |


*Table: This table summarizes the main domains and conserved mechanistic features reported for the auxilin-like protein family, highlighting which features are core to the animal clathrin-uncoating branch versus subfamily-specific specializations such as the GAK kinase domain.*

---

## 2. InterPro2GO Mapping Appropriateness

**Current status:** PTHR23172 has **zero InterPro2GO terms** mapped to it. This absence is appropriate and should be maintained given the evidence below.

### 2.1 Why Whole-Protein GO Terms Are Inappropriate for This Entry

**Major functional divergence across kingdoms:**
- **Animal branch:** Clathrin-mediated endocytosis, synaptic vesicle recycling, presynaptic function (roosen2019dnajcproteinsand pages 3-7, he2020dynamicsofauxilin pages 1-2, cheng2023impairedpresynapticplasticity pages 1-2, abela2024neurodevelopmentalandsynaptic pages 1-2, ng2024dysfunctionofsynaptic pages 3-4)
- **Plant branch:** Chloroplast photorelocation movement, epidermal chloroplast immune response—completely different biology (wada2016chloroplastandnuclear pages 1-3, irieda2022emergingrolesof pages 6-8, suetsugu2016lightinducedmovementsof pages 1-2, irieda2022emergingrolesof pages 1-2)

Plant auxilin-like proteins such as JAC1 regulate blue-light-induced chloroplast accumulation responses and chloroplast positioning via phototropin signaling and cp-actin filament reorganization (irieda2022emergingrolesof pages 6-8, suetsugu2016lightinducedmovementsof pages 1-2, irieda2022emergingrolesof pages 1-2). These proteins share the J-domain but lack the canonical animal PTEN-like/clathrin-binding architecture and function in a completely distinct cellular context (chloroplast movement, not endocytosis) (irieda2022emergingrolesof pages 6-8, suetsugu2016lightinducedmovementsof pages 1-2).

**Subfamily-specific functions that should not be generalized:**
- GAK/DNAJC26 has an additional N-terminal kinase domain and neo-functionalized roles in autophagy initiation via ULK1/Atg1 and PRKN-independent mitophagy (zhang2023cyclingassociatedkinasegakdaux pages 1-2, munson2021gakandprkcd pages 1-2, zhang2023cyclingassociatedkinasegakdaux pages 3-5)—these are **not** shared by neuronal auxilin/DNAJC6 (park2015theclathrinbindingand pages 1-2)
- Neuronal auxilin/DNAJC6 is specifically enriched in brain/presynaptic terminals and critical for synaptic vesicle recycling (roosen2019dnajcproteinsand pages 3-7, cheng2023impairedpresynapticplasticity pages 1-2, abela2024neurodevelopmentalandsynaptic pages 1-2)—inappropriate to assign "synaptic vesicle endocytosis" to ubiquitous GAK or plant homologs

### 2.2 Recommended GO Action Pattern

Given that PTHR23172 spans 7,490 taxa including both animal and plant kingdoms with documented functional divergence:

**ACCEPT current state (no InterPro2GO terms)** because:
- The family is heterogeneous at the whole-protein function level
- Mapping animal-specific endocytic terms would over-annotate plant proteins
- Mapping plant-specific chloroplast terms would over-annotate animal proteins
- Even within animals, GAK-specific autophagy functions should not be assigned to all members

**Recommended strategy for future curation:**
- **Promote subfamily-specific terms to child InterPro entries** if subfamilies are created (e.g., separate entries for animal auxilin/GAK vs. plant JAC1-like proteins)
- **Keep only the most mechanistically universal term at family level:** "unfolded protein binding" (GO:0051082) or "heat shock protein binding" (GO:0031072) reflecting the conserved J-domain co-chaperone function
- **Avoid:** "clathrin-mediated endocytosis" (GO:0072583), "synaptic vesicle endocytosis" (GO:0048488), "clathrin coat disassembly" (GO:1905665), or "chloroplast movement" at the family level—these are subfamily-specific

| Subfamily/Member | Taxonomic distribution | Key distinguishing features | Primary biological function | Evidence level |
|---|---|---|---|---|
| Neuronal auxilin / DNAJC6 (auxilin-1, PARK19) | Vertebrates; neuronal-enriched/brain-enriched animal branch | Canonical auxilin architecture with N-terminal PTEN-like domain, clathrin-binding region, and C-terminal J-domain; lacks the N-terminal kinase domain of GAK; expression is primarily neuronal/presynaptic; disease-associated human mutations cluster in splice/truncating alleles and the J-domain missense R927G, supporting a core neuronal clathrin-uncoating role (roosen2019dnajcproteinsand pages 3-7, abela2024neurodevelopmentalandsynaptic pages 1-2, ng2024dysfunctionofsynaptic pages 3-4) | Recruitment of Hsc70/HSPA8 to clathrin-coated vesicles for rapid post-scission clathrin uncoating in synaptic vesicle recycling; strong support for presynaptic clathrin-mediated endocytosis and synaptic vesicle homeostasis (roosen2019dnajcproteinsand pages 3-7, he2020dynamicsofauxilin pages 1-2, cheng2023impairedpresynapticplasticity pages 1-2, abela2024neurodevelopmentalandsynaptic pages 1-2) | **High** for clathrin uncoating/endocytosis in neurons (human genetics, mouse knockout, iPSC neurons, live-cell imaging); **not** evidence for plant-like or GAK-specific autophagy functions across this subfamily (he2020dynamicsofauxilin pages 1-2, cheng2023impairedpresynapticplasticity pages 1-2, abela2024neurodevelopmentalandsynaptic pages 1-2, ng2024dysfunctionofsynaptic pages 3-4) |
| Ubiquitous GAK / DNAJC26 (auxilin-2) | Broadly distributed in animals; ubiquitous/non-neuronal and neuronal tissues | Shares PTEN-like, clathrin-binding, and J-domains with auxilin, but has an extra N-terminal Ser/Thr kinase domain; this marks a clear neo-functionalized branch relative to neuronal auxilin; rescue experiments show clathrin-binding + J-domains are sufficient for basic uncoating, whereas the kinase/PTEN-like regions add regulatory or tissue-specific functions (park2015theclathrinbindingand pages 1-2, zhang2023cyclingassociatedkinasegakdaux pages 1-2, zhang2023cyclingassociatedkinasegakdaux pages 3-5) | Conserved role in clathrin coat uncoating/chaperoning with Hsc70, plus additional lineage-specific roles in autophagy initiation via ULK1/Atg1, glial biology, and PRKN-independent mitophagy; therefore broader than DNAJC6 and not functionally identical (park2015theclathrinbindingand pages 1-2, zhang2023cyclingassociatedkinasegakdaux pages 1-2, munson2021gakandprkcd pages 1-2, zhang2023cyclingassociatedkinasegakdaux pages 3-5) | **High** for clathrin-uncoating role; **moderate-to-high** for added autophagy/mitophagy functions, but those are subfamily-specific and should not be generalized to all PTHR23172 members (park2015theclathrinbindingand pages 1-2, zhang2023cyclingassociatedkinasegakdaux pages 1-2, munson2021gakandprkcd pages 1-2, zhang2023cyclingassociatedkinasegakdaux pages 3-5) |
| Plant auxilin-like proteins (JAC1 and related) | Land plants, including Arabidopsis and other plant lineages | Functionally divergent auxilin-like/J-domain proteins associated with chloroplast photorelocation and epidermal chloroplast immunity; evidence emphasizes J-domain signaling in light-regulated chloroplast movement rather than canonical synaptic/endocytic clathrin uncoating; these proteins highlight kingdom-level divergence within the broader family assignment (wada2016chloroplastandnuclear pages 1-3, irieda2022emergingrolesof pages 6-8, suetsugu2016lightinducedmovementsof pages 1-2, irieda2022emergingrolesof pages 1-2) | Regulation of chloroplast accumulation/avoidance responses and related epidermal chloroplast behaviors in light response and immunity; this is a divergent biological process compared with animal clathrin-coated vesicle uncoating (irieda2022emergingrolesof pages 6-8, suetsugu2016lightinducedmovementsof pages 1-2, irieda2022emergingrolesof pages 1-2) | **High** for chloroplast-movement role in plants; **low/insufficient** to claim canonical clathrin-uncoating as a universal function for this branch from the evidence assembled here (irieda2022emergingrolesof pages 6-8, suetsugu2016lightinducedmovementsof pages 1-2, irieda2022emergingrolesof pages 1-2) |
| Invertebrate homologs (e.g., Drosophila dAux, C. elegans / other metazoan auxilin-GAK-like proteins) | Invertebrate metazoans including flies, worms, and zebrafish-relevant animal models for related branches | Retain core clathrin-binding/J-domain machinery; some invertebrate homologs resemble GAK-like proteins with kinase-domain-containing architecture rather than vertebrate DNAJC6-only organization; functional studies show conservation of endocytic control, but also added roles in development, molting/trafficking networks, and glial autophagy in flies (park2015theclathrinbindingand pages 1-2, zhang2023cyclingassociatedkinasegakdaux pages 1-2, joseph2020controlofclathrinmediated pages 1-2) | Conserved clathrin-mediated endocytic trafficking/uncoating functions, with lineage-specific developmental and trafficking adaptations; Drosophila dAux also contributes to autophagy regulation, again arguing for partial conservation plus neo-functionalization rather than perfect family-wide uniformity (park2015theclathrinbindingand pages 1-2, zhang2023cyclingassociatedkinasegakdaux pages 1-2, joseph2020controlofclathrinmediated pages 1-2) | **Moderate-to-high** for conserved endocytic trafficking roles; **moderate** for additional lineage-specific functions, which vary by organism and architecture and therefore should not be promoted to universal GO terms for the whole family (park2015theclathrinbindingand pages 1-2, zhang2023cyclingassociatedkinasegakdaux pages 1-2, joseph2020controlofclathrinmediated pages 1-2) |


*Table: This table summarizes the main functional branches within PTHR23172 and shows that the family is not uniformly equivalent to neuronal auxilin. It is useful for GO review because it separates conserved clathrin-uncoating features from subfamily-specific innovations such as GAK kinase functions and plant chloroplast-movement roles.*

---

## 3. Functional Divergence Across the Family

### 3.1 Major Subfamilies and Their Distinguishing Features

**Neuronal auxilin / DNAJC6 / PARK19:**
- Tissue distribution: Brain-enriched, neuronal/presynaptic (roosen2019dnajcproteinsand pages 3-7, abela2024neurodevelopmentalandsynaptic pages 1-2)
- Architecture: PTEN-like + clathrin-binding + J-domain (lacks kinase) (roosen2019dnajcproteinsand pages 3-7)
- Function: Clathrin uncoating in synaptic vesicle recycling; knockout causes accumulation of CCVs and impaired synaptic vesicle homeostasis (cheng2023impairedpresynapticplasticity pages 1-2, abela2024neurodevelopmentalandsynaptic pages 1-2, ng2024dysfunctionofsynaptic pages 3-4)
- Human disease: Loss-of-function mutations cause juvenile-onset Parkinson's disease with epilepsy and cognitive impairment (ng2020dnajc6mutationsdisrupt pages 4-7, roosen2019dnajcproteinsand pages 3-7, abela2024neurodevelopmentalandsynaptic pages 1-2)

**Ubiquitous GAK / DNAJC26 (auxilin-2):**
- Tissue distribution: Ubiquitous, expressed in all cell types (roosen2019dnajcproteinsand pages 3-7, park2015theclathrinbindingand pages 1-2)
- Architecture: **Additional N-terminal Ser/Thr kinase domain** + PTEN-like + clathrin-binding + J-domain (park2015theclathrinbindingand pages 1-2, zhang2023cyclingassociatedkinasegakdaux pages 1-2)
- Function: Canonical clathrin uncoating **plus** neo-functionalized roles in (1) autophagy initiation via direct ULK1/Atg1 interaction through the uncoating domain (zhang2023cyclingassociatedkinasegakdaux pages 1-2, zhang2023cyclingassociatedkinasegakdaux pages 3-5), and (2) PRKN-independent mitophagy as a positive regulator requiring its kinase activity (munson2021gakandprkcd pages 1-2, munson2021gakandprkcd pages 3-4)
- Evidence: GAK knockout/knockdown in glia, microglia, and cultured cells increases autophagosome number/size and upregulates autophagy initiation markers (zhang2023cyclingassociatedkinasegakdaux pages 1-2, zhang2023cyclingassociatedkinasegakdaux pages 3-5)

**Plant auxilin-like proteins (JAC1 and related):**
- Taxonomic distribution: Land plants including Arabidopsis (wada2016chloroplastandnuclear pages 1-3, irieda2022emergingrolesof pages 6-8, suetsugu2016lightinducedmovementsof pages 1-2)
- Architecture: J-domain-containing proteins; divergent from animal architecture (irieda2022emergingrolesof pages 6-8, suetsugu2016lightinducedmovementsof pages 1-2)
- Function: **Completely different biology**—regulation of chloroplast accumulation/avoidance responses to light via phototropin signaling and cp-actin filament reorganization (irieda2022emergingrolesof pages 6-8, suetsugu2016lightinducedmovementsof pages 1-2); also involved in epidermal chloroplast immune response against fungal/oomycete pathogens (irieda2022emergingrolesof pages 6-8, irieda2022emergingrolesof pages 1-2)
- Mechanism: JAC1 is essential for blue-light-induced reorganization of cp-actin filaments during chloroplast photorelocation movement, coordinating with CHUP1, KAC proteins, and PMI proteins (irieda2022emergingrolesof pages 6-8, suetsugu2016lightinducedmovementsof pages 1-2)

**Invertebrate homologs:**
- Distribution: Drosophila (dAux), C. elegans, zebrafish (zhang2023cyclingassociatedkinasegakdaux pages 1-2, joseph2020controlofclathrinmediated pages 1-2)
- Function: Conserved endocytic/clathrin-uncoating role with lineage-specific adaptations; Drosophila dAux also regulates glial autophagy (zhang2023cyclingassociatedkinasegakdaux pages 1-2), and C. elegans homologs control molting via clathrin-mediated trafficking (joseph2020controlofclathrinmediated pages 1-2)

### 3.2 Neo-functionalization Summary

This family exhibits **clear neo-functionalization**:
1. **GAK subfamily** has evolved kinase-dependent autophagy/mitophagy functions layered onto the ancestral clathrin-uncoating scaffold (zhang2023cyclingassociatedkinasegakdaux pages 1-2, munson2021gakandprkcd pages 1-2, zhang2023cyclingassociatedkinasegakdaux pages 3-5)
2. **Plant lineage** has repurposed J-domain signaling machinery for chloroplast-movement regulation, abandoning the animal-specific endocytic role (irieda2022emergingrolesof pages 6-8, suetsugu2016lightinducedmovementsof pages 1-2, irieda2022emergingrolesof pages 1-2)
3. **No evidence for catalytically dead/pseudo-enzyme members**, but there is structural/regulatory diversity

---

## 4. Taxonomic Scope

### 4.1 Clade Distribution

InterPro metadata indicates PTHR23172 spans **7,490 taxa**. Literature evidence documents:

**Animals (Metazoa):**
- Mammals (human, mouse, rat) with both DNAJC6 and DNAJC26 (roosen2019dnajcproteinsand pages 3-7, park2015theclathrinbindingand pages 1-2, cheng2023impairedpresynapticplasticity pages 1-2, abela2024neurodevelopmentalandsynaptic pages 1-2)
- Invertebrates: Drosophila, C. elegans, zebrafish (park2015theclathrinbindingand pages 1-2, zhang2023cyclingassociatedkinasegakdaux pages 1-2, joseph2020controlofclathrinmediated pages 1-2)
- Conserved function: clathrin-mediated endocytosis/uncoating

**Plants (Viridiplantae):**
- Land plants including Arabidopsis thaliana, Nicotiana benthamiana, rice, and other angiosperms (wada2016chloroplastandnuclear pages 1-3, irieda2022emergingrolesof pages 6-8, suetsugu2016lightinducedmovementsof pages 1-2, irieda2022emergingrolesof pages 1-2)
- Divergent function: chloroplast photorelocation, light response, epidermal immunity

### 4.2 Cross-Kingdom GO Term Applicability

**Terms that hold across animals but NOT plants:**
- "clathrin-mediated endocytosis" (GO:0072583)—**animal-specific** (roosen2019dnajcproteinsand pages 3-7, he2020dynamicsofauxilin pages 1-2, ng2024dysfunctionofsynaptic pages 3-4)
- "clathrin coat disassembly" (GO:1905665)—**animal-specific** (roosen2019dnajcproteinsand pages 3-7, he2020dynamicsofauxilin pages 1-2)
- "synaptic vesicle endocytosis" (GO:0048488)—**neuronal subset only** (cheng2023impairedpresynapticplasticity pages 1-2, abela2024neurodevelopmentalandsynaptic pages 1-2)

**Terms that hold in plants but NOT animals:**
- "chloroplast movement" (GO:0009902)—**plant-specific** (irieda2022emergingrolesof pages 6-8, suetsugu2016lightinducedmovementsof pages 1-2)
- "chloroplast organization" (GO:0009658)—**plant-specific** (irieda2022emergingrolesof pages 6-8, suetsugu2016lightinducedmovementsof pages 1-2, irieda2022emergingrolesof pages 1-2)

**Most conserved mechanistic term (potentially family-wide):**
- "heat shock protein binding" (GO:0031072) or "unfolded protein binding" (GO:0051082)—reflects the universal J-domain co-chaperone function with Hsp70-family proteins (roosen2019dnajcproteinsand pages 3-7, joshi2020chaperonesandproteostasis pages 11-13, he2020dynamicsofauxilin pages 1-2)

---

## 5. Over-Annotation Verdict and GO Recommendations

### 5.1 Current State Assessment

**Verdict:** The current absence of InterPro2GO terms for PTHR23172 is **appropriate and should be maintained**. This entry represents a functionally heterogeneous family where whole-protein process/component terms would systematically over-annotate.

### 5.2 Specific Problems if Common GO Terms Were Applied

**If "clathrin-mediated endocytosis" were mapped:**
- Would **over-annotate** all 10,009 proteins, including plant JAC1 proteins that regulate chloroplast movement, not endocytosis (irieda2022emergingrolesof pages 6-8, suetsugu2016lightinducedmovementsof pages 1-2, irieda2022emergingrolesof pages 1-2)

**If "synaptic vesicle endocytosis" were mapped:**
- Would **over-annotate** ubiquitous GAK in non-neuronal tissues and all plant homologs (roosen2019dnajcproteinsand pages 3-7, park2015theclathrinbindingand pages 1-2)

**If "autophagy" or "mitophagy" were mapped:**
- Would **over-annotate** neuronal auxilin/DNAJC6, which lacks evidence for these GAK-specific functions (park2015theclathrinbindingand pages 1-2, zhang2023cyclingassociatedkinasegakdaux pages 1-2, zhang2023cyclingassociatedkinasegakdaux pages 3-5)

**If "chloroplast movement" were mapped:**
- Would **over-annotate** all animal auxilin/GAK proteins, which function in endocytosis, not chloroplast biology (roosen2019dnajcproteinsand pages 3-7, irieda2022emergingrolesof pages 6-8)

### 5.3 Recommended GO Action Pattern

**For PTHR23172 (family level):**
- **ACCEPT** current no-mapping state
- If any term is added, limit to the most mechanistically universal: "heat shock protein binding" (GO:0031072) or "Hsp70 protein binding" (GO:0030544)
- **AVOID** process terms ("clathrin-mediated endocytosis," "chloroplast movement," "autophagy," "synaptic vesicle endocytosis") at family level

**Recommendation for InterPro curation:**
- **Create child entries** to segregate: (1) Animal auxilin/GAK branch (clathrin uncoating), (2) Plant JAC1-like branch (chloroplast movement)
- **Demote whole-protein process/component terms** to child entries only
- **Mark subfamily-specific functions** (e.g., GAK kinase/autophagy, neuronal synaptic vesicle recycling) as annotations that should go to more specific child signatures, not the parent family

**Action classification:** **MARK_AS_OVER_ANNOTATED** if endocytosis/synaptic terms are applied to this family-level entry; **KEEP_AS_NON_CORE** for the conserved Hsp70-binding molecular function.

### 5.4 Summary Table of GO Term Suitability

| GO Term | Appropriate for Family? | Rationale |
|---------|-------------------------|-----------|
| Heat shock protein binding (GO:0031072) | **YES** (mechanistic core) | Universal J-domain function conserved across all branches (roosen2019dnajcproteinsand pages 3-7, joshi2020chaperonesandproteostasis pages 11-13, he2020dynamicsofauxilin pages 1-2) |
| Clathrin-mediated endocytosis (GO:0072583) | **NO** (subfamily-only) | True for animal branch, false for plant JAC1 proteins (irieda2022emergingrolesof pages 6-8, suetsugu2016lightinducedmovementsof pages 1-2) |
| Clathrin coat disassembly (GO:1905665) | **NO** (subfamily-only) | Animal-specific; plants use these proteins for chloroplast positioning (irieda2022emergingrolesof pages 6-8) |
| Synaptic vesicle endocytosis (GO:0048488) | **NO** (sub-subfamily) | Neuronal auxilin-specific; inappropriate for GAK or plants (cheng2023impairedpresynapticplasticity pages 1-2, abela2024neurodevelopmentalandsynaptic pages 1-2) |
| Autophagy (GO:0006914) | **NO** (subfamily-only) | GAK-specific neo-function; not shared by DNAJC6 (zhang2023cyclingassociatedkinasegakdaux pages 1-2, zhang2023cyclingassociatedkinasegakdaux pages 3-5) |
| Chloroplast movement (GO:0009902) | **NO** (plant-only) | Plant JAC1 function; would over-annotate all animal proteins (irieda2022emergingrolesof pages 6-8, suetsugu2016lightinducedmovementsof pages 1-2) |

---

## Conclusion

PTHR23172 is a **family-level entry** encompassing functionally divergent proteins across kingdoms. The defining mechanistic feature is the **J-domain co-chaperone function** with Hsp70-family proteins. Beyond this conserved molecular mechanism, the family exhibits major functional divergence: animal members mediate clathrin-coat disassembly in endocytosis (with subfamily specialization between neuronal auxilin and ubiquitous GAK), whereas plant members regulate chloroplast photorelocation and immunity. **No whole-protein biological process or cellular component GO terms should be assigned at the family level.** The current absence of InterPro2GO mappings is appropriate. Subfamily-specific GO terms should be demoted to child InterPro entries if created. This represents a textbook case where a broad sequence-based family assignment must not be conflated with functional homogeneity for GO annotation purposes.

---

**Sources cited:** (ng2020dnajc6mutationsdisrupt pages 4-7, roosen2019dnajcproteinsand pages 3-7, park2015theclathrinbindingand pages 1-2, joshi2020chaperonesandproteostasis pages 11-13, nguyen2019synapticmitochondrialand pages 4-6, he2020dynamicsofauxilin pages 1-2, zhang2023cyclingassociatedkinasegakdaux pages 1-2, cheng2023impairedpresynapticplasticity pages 1-2, abela2024neurodevelopmentalandsynaptic pages 1-2, munson2021gakandprkcd pages 1-2, joseph2020controlofclathrinmediated pages 1-2, wada2016chloroplastandnuclear pages 1-3, irieda2022emergingrolesof pages 6-8, suetsugu2016lightinducedmovementsof pages 1-2, munson2021gakandprkcd pages 3-4, zhang2023cyclingassociatedkinasegakdaux pages 3-5, ng2024dysfunctionofsynaptic pages 3-4, irieda2022emergingrolesof pages 1-2)

References

1. (roosen2019dnajcproteinsand pages 3-7): Dorien A. Roosen, Cornelis Blauwendraat, Mark R. Cookson, and Patrick A. Lewis. Dnajc proteins and pathways to parkinsonism. The FEBS Journal, 286:3080-3094, Aug 2019. URL: https://doi.org/10.1111/febs.14936, doi:10.1111/febs.14936. This article has 87 citations.

2. (park2015theclathrinbindingand pages 1-2): Bum-Chan Park, Yang-In Yim, Xiaohong Zhao, Maciej B. Olszewski, Evan Eisenberg, and Lois E. Greene. The clathrin-binding and j-domains of gak support the uncoating and chaperoning of clathrin by hsc70 in the brain. Journal of Cell Science, 128:3811-3821, Oct 2015. URL: https://doi.org/10.1242/jcs.171058, doi:10.1242/jcs.171058. This article has 36 citations and is from a domain leading peer-reviewed journal.

3. (he2020dynamicsofauxilin pages 1-2): Kangmin He, Eli Song, Srigokul Upadhyayula, Song Dang, Raphael Gaudin, Wesley Skillern, Kevin Bu, Benjamin R. Capraro, Iris Rapoport, Ilja Kusters, Minghe Ma, and Tom Kirchhausen. Dynamics of auxilin 1 and gak in clathrin-mediated traffic. The Journal of Cell Biology, Jan 2020. URL: https://doi.org/10.1083/jcb.201908142, doi:10.1083/jcb.201908142. This article has 70 citations.

4. (joshi2020chaperonesandproteostasis pages 11-13): Neha Joshi, Atchaya Raveendran, and Shirisha Nagotu. Chaperones and proteostasis: role in parkinson’s disease. Diseases, 8:24, Jun 2020. URL: https://doi.org/10.3390/diseases8020024, doi:10.3390/diseases8020024. This article has 22 citations.

5. (nguyen2019synapticmitochondrialand pages 4-6): Maria Nguyen, Yvette C. Wong, Daniel Ysselstein, Alex Severino, and Dimitri Krainc. Synaptic, mitochondrial, and lysosomal dysfunction in parkinson’s disease. Trends in Neurosciences, 42(2):140-149, Feb 2019. URL: https://doi.org/10.1016/j.tins.2018.11.001, doi:10.1016/j.tins.2018.11.001. This article has 369 citations and is from a highest quality peer-reviewed journal.

6. (ng2024dysfunctionofsynaptic pages 3-4): Xin Yi Ng and Mian Cao. Dysfunction of synaptic endocytic trafficking in parkinson’s disease. Neural Regeneration Research, 19(12):2649-2660, Mar 2024. URL: https://doi.org/10.4103/nrr.nrr-d-23-01624, doi:10.4103/nrr.nrr-d-23-01624. This article has 36 citations and is from a peer-reviewed journal.

7. (abela2024neurodevelopmentalandsynaptic pages 1-2): Lucia Abela, Lorita Gianfrancesco, Erica Tagliatti, Giada Rossignoli, Katy Barwick, Clara Zourray, Kimberley M Reid, Dimitri Budinger, Joanne Ng, John Counsell, Arlo Simpson, Toni S Pearson, Simon Edvardson, Orly Elpeleg, Frances M Brodsky, Gabriele Lignani, Serena Barral, and Manju A Kurian. Neurodevelopmental and synaptic defects in dnajc6 parkinsonism, amenable to gene therapy. Brain, 147:2023-2037, Jan 2024. URL: https://doi.org/10.1093/brain/awae020, doi:10.1093/brain/awae020. This article has 27 citations and is from a highest quality peer-reviewed journal.

8. (cheng2023impairedpresynapticplasticity pages 1-2): Xi Cheng, Yu Tang, D.J. Vidyadhara, Ben-Zheng Li, Michael Zimmerman, Alexandr Pak, Sanghamitra Nareddula, Paige Alyssa Edens, Sreeganga S. Chandra, and Alexander A. Chubykin. Impaired pre-synaptic plasticity and visual responses in auxilin-knockout mice. Oct 2023. URL: https://doi.org/10.1016/j.isci.2023.107842, doi:10.1016/j.isci.2023.107842. This article has 8 citations and is from a peer-reviewed journal.

9. (zhang2023cyclingassociatedkinasegakdaux pages 1-2): Shiping Zhang, Linfang Wang, Shuanglong Yi, Shuhua Li, Honglei Wang, Li Song, Jiayao Ou, M. Zhang, Mengxiao Wang, Yucheng Zheng, Ruiqi Wang, Kai Yang, Tong Liu, Wei Yan, Chang Liu, and M. Ho. Cyclin-g-associated kinase gak/daux regulates autophagy initiation via ulk1/atg1 in glia. Proceedings of the National Academy of Sciences, Jul 2023. URL: https://doi.org/10.1073/pnas.2301002120, doi:10.1073/pnas.2301002120. This article has 17 citations and is from a highest quality peer-reviewed journal.

10. (munson2021gakandprkcd pages 1-2): Michael J. Munson, Benan J. Mathai, Matthew Yoke Wui Ng, Laura Trachsel-Moncho, Laura R. de la Ballina, Sebastian W. Schultz, Yahyah Aman, Alf H. Lystad, Sakshi Singh, Sachin Singh, Jørgen Wesche, Evandro F. Fang, and Anne Simonsen. Gak and prkcd are positive regulators of prkn-independent mitophagy. Nature Communications, Oct 2021. URL: https://doi.org/10.1038/s41467-021-26331-7, doi:10.1038/s41467-021-26331-7. This article has 82 citations and is from a highest quality peer-reviewed journal.

11. (zhang2023cyclingassociatedkinasegakdaux pages 3-5): Shiping Zhang, Linfang Wang, Shuanglong Yi, Shuhua Li, Honglei Wang, Li Song, Jiayao Ou, M. Zhang, Mengxiao Wang, Yucheng Zheng, Ruiqi Wang, Kai Yang, Tong Liu, Wei Yan, Chang Liu, and M. Ho. Cyclin-g-associated kinase gak/daux regulates autophagy initiation via ulk1/atg1 in glia. Proceedings of the National Academy of Sciences, Jul 2023. URL: https://doi.org/10.1073/pnas.2301002120, doi:10.1073/pnas.2301002120. This article has 17 citations and is from a highest quality peer-reviewed journal.

12. (suetsugu2016lightinducedmovementsof pages 1-2): Noriyuki Suetsugu, Takeshi Higa, Eiji Gotoh, and Masamitsu Wada. Light-induced movements of chloroplasts and nuclei are regulated in both cp-actin-filament-dependent and -independent manners in arabidopsis thaliana. PLoS ONE, 11:e0157429, Jun 2016. URL: https://doi.org/10.1371/journal.pone.0157429, doi:10.1371/journal.pone.0157429. This article has 54 citations and is from a peer-reviewed journal.

13. (wada2016chloroplastandnuclear pages 1-3): Masamitsu WADA. Chloroplast and nuclear photorelocation movements. Proceedings of the Japan Academy. Series B, Physical and Biological Sciences, 92:387-411, Nov 2016. URL: https://doi.org/10.2183/pjab.92.387, doi:10.2183/pjab.92.387. This article has 56 citations.

14. (irieda2022emergingrolesof pages 6-8): Hiroki Irieda. Emerging roles of motile epidermal chloroplasts in plant immunity. International Journal of Molecular Sciences, 23:4043, Apr 2022. URL: https://doi.org/10.3390/ijms23074043, doi:10.3390/ijms23074043. This article has 17 citations.

15. (irieda2022emergingrolesof pages 1-2): Hiroki Irieda. Emerging roles of motile epidermal chloroplasts in plant immunity. International Journal of Molecular Sciences, 23:4043, Apr 2022. URL: https://doi.org/10.3390/ijms23074043, doi:10.3390/ijms23074043. This article has 17 citations.

16. (joseph2020controlofclathrinmediated pages 1-2): Braveen B. Joseph, Yu Wang, Phil Edeen, Vladimir Lažetić, Barth D. Grant, and David S. Fay. Control of clathrin-mediated endocytosis by nima family kinases. PLOS Genetics, 16:e1008633, Feb 2020. URL: https://doi.org/10.1371/journal.pgen.1008633, doi:10.1371/journal.pgen.1008633. This article has 50 citations and is from a domain leading peer-reviewed journal.

17. (ng2020dnajc6mutationsdisrupt pages 4-7): Joanne Ng, Elisenda Cortès‐Saladelafont, Lucia Abela, Pichet Termsarasab, Kshitij Mankad, Sniya Sudhakar, Kathleen M. Gorman, Simon J.R. Heales, Simon Pope, Lorenzo Biassoni, Barbara Csányi, John Cain, Karl Rakshi, Helen Coutts, Sandeep Jayawant, Rosalind Jefferson, Deborah Hughes, Àngels García‐Cazorla, Detelina Grozeva, F. Lucy Raymond, Belén Pérez‐Dueñas, Christian De Goede, Toni S. Pearson, Esther Meyer, and Manju A. Kurian. Dnajc6 mutations disrupt dopamine homeostasis in juvenile parkinsonism‐dystonia. Movement Disorders, 35:1357-1368, May 2020. URL: https://doi.org/10.1002/mds.28063, doi:10.1002/mds.28063. This article has 49 citations and is from a highest quality peer-reviewed journal.

18. (munson2021gakandprkcd pages 3-4): Michael J. Munson, Benan J. Mathai, Matthew Yoke Wui Ng, Laura Trachsel-Moncho, Laura R. de la Ballina, Sebastian W. Schultz, Yahyah Aman, Alf H. Lystad, Sakshi Singh, Sachin Singh, Jørgen Wesche, Evandro F. Fang, and Anne Simonsen. Gak and prkcd are positive regulators of prkn-independent mitophagy. Nature Communications, Oct 2021. URL: https://doi.org/10.1038/s41467-021-26331-7, doi:10.1038/s41467-021-26331-7. This article has 82 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PTHR23172-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR23172-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. roosen2019dnajcproteinsand pages 3-7
2. he2020dynamicsofauxilin pages 1-2
3. nguyen2019synapticmitochondrialand pages 4-6
4. park2015theclathrinbindingand pages 1-2
5. zhang2023cyclingassociatedkinasegakdaux pages 1-2
6. joseph2020controlofclathrinmediated pages 1-2
7. irieda2022emergingrolesof pages 6-8
8. joshi2020chaperonesandproteostasis pages 11-13
9. ng2024dysfunctionofsynaptic pages 3-4
10. abela2024neurodevelopmentalandsynaptic pages 1-2
11. cheng2023impairedpresynapticplasticity pages 1-2
12. munson2021gakandprkcd pages 1-2
13. zhang2023cyclingassociatedkinasegakdaux pages 3-5
14. suetsugu2016lightinducedmovementsof pages 1-2
15. wada2016chloroplastandnuclear pages 1-3
16. irieda2022emergingrolesof pages 1-2
17. munson2021gakandprkcd pages 3-4
18. https://doi.org/10.1111/febs.14936,
19. https://doi.org/10.1242/jcs.171058,
20. https://doi.org/10.1083/jcb.201908142,
21. https://doi.org/10.3390/diseases8020024,
22. https://doi.org/10.1016/j.tins.2018.11.001,
23. https://doi.org/10.4103/nrr.nrr-d-23-01624,
24. https://doi.org/10.1093/brain/awae020,
25. https://doi.org/10.1016/j.isci.2023.107842,
26. https://doi.org/10.1073/pnas.2301002120,
27. https://doi.org/10.1038/s41467-021-26331-7,
28. https://doi.org/10.1371/journal.pone.0157429,
29. https://doi.org/10.2183/pjab.92.387,
30. https://doi.org/10.3390/ijms23074043,
31. https://doi.org/10.1371/journal.pgen.1008633,
32. https://doi.org/10.1002/mds.28063,