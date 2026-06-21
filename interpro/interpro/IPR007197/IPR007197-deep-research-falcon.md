---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-20T05:52:29.604652'
end_time: '2026-06-20T06:04:05.452928'
duration_seconds: 695.85
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: IPR007197
  interpro_name: Radical SAM
  interpro_short_name: rSAM
  interpro_type: domain
  interpro_integrated: None (top-level entry)
  member_databases: 'SFLDS00029 (sfld: Radical SAM); PS51918 (profile: Radical SAM
    core domain profile); PF04055 (pfam: Radical SAM superfamily)'
  n_proteins: '316821'
  n_taxa: '36891'
  n_subfamilies: '0'
  interpro2go_terms: GO:0003824 catalytic activity [F]; GO:0051536 iron-sulfur cluster
    binding [F]
  interpro_description: "The Radical SAM domain is organised in a fold related to\
    \ the \u03B2-barrel or TIM barrel, in which \u03B2-strands are arranged in a barrel-like\
    \ array, with peripheral helices intervening between \u03B2-strands. The [4Fe-4S]\
    \ clusters and substrates are bound within the barrels, as is typical of TIM barrel\
    \ enzymes [[cite:PUB00097557], [cite:PUB00097556]]. Radical SAM proteins are found\
    \ in all domains of life and share an unusual Fe-S cluster associated with generation\
    \ of a free radical by reductive cleavage of SAM and often provide an anaerobic\
    \ or oxygen-independent mechanism that is found as an aerobic reaction in other\
    \ proteins. Radical SAM proteins catalyse diverse reactions, including unusual\
    \ methylations, isomerisation, sulphur insertion, ring formation, anaerobic oxidation\
    \ and protein radical formation. These proteins function in DNA precursor, vitamin,\
    \ cofactor, antibiotic and herbicide biosynthesis and in biodegradation pathways\
    \ [[cite:PUB00010539], [cite:PUB00015124]]. Radical SAM proteins share several\
    \ common features, notably three strictly conserved cysteine residues generally\
    \ included in the CxxxCxxC motif. These critical cysteines coordinate the unusual\
    \ [4Fe-4S]2+/1+ cluster, while SAM serves as ligand for the fourth iron atom and\
    \ acts as a cofactor or a cosubstrate . The radical SAM enzymes biochemically\
    \ characterised to date have in common the cleavage of the [4Fe-4S]1+-SAM complex\
    \ to [4Fe-4S]2+-Met and the 5'-deoxyadenosyl radical, which abstracts a hydrogen\
    \ atom from the sub ..."
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 31
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: IPR007197-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: IPR007197-deep-research-falcon_artifacts/artifact-01.md
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
- **Accession:** IPR007197
- **Name:** Radical SAM
- **Short name:** rSAM
- **Entry type:** domain
- **Integrated into / parent:** None (top-level entry)
- **Member database signatures:** SFLDS00029 (sfld: Radical SAM); PS51918 (profile: Radical SAM core domain profile); PF04055 (pfam: Radical SAM superfamily)
- **Scale:** 316821 proteins across 36891 taxa, 0 subfamilies
- **Current InterPro2GO terms (the mappings under review):** GO:0003824 catalytic activity [F]; GO:0051536 iron-sulfur cluster binding [F]
- **InterPro description:** The Radical SAM domain is organised in a fold related to the β-barrel or TIM barrel, in which β-strands are arranged in a barrel-like array, with peripheral helices intervening between β-strands. The [4Fe-4S] clusters and substrates are bound within the barrels, as is typical of TIM barrel enzymes [[cite:PUB00097557], [cite:PUB00097556]]. Radical SAM proteins are found in all domains of life and share an unusual Fe-S cluster associated with generation of a free radical by reductive cleavage of SAM and often provide an anaerobic or oxygen-independent mechanism that is found as an aerobic reaction in other proteins. Radical SAM proteins catalyse diverse reactions, including unusual methylations, isomerisation, sulphur insertion, ring formation, anaerobic oxidation and protein radical formation. These proteins function in DNA precursor, vitamin, cofactor, antibiotic and herbicide biosynthesis and in biodegradation pathways [[cite:PUB00010539], [cite:PUB00015124]]. Radical SAM proteins share several common features, notably three strictly conserved cysteine residues generally included in the CxxxCxxC motif. These critical cysteines coordinate the unusual [4Fe-4S]2+/1+ cluster, while SAM serves as ligand for the fourth iron atom and acts as a cofactor or a cosubstrate . The radical SAM enzymes biochemically characterised to date have in common the cleavage of the [4Fe-4S]1+-SAM complex to [4Fe-4S]2+-Met and the 5'-deoxyadenosyl radical, which abstracts a hydrogen atom from the sub ...

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**IPR007197 (Radical SAM)**, structured to support GO annotation review.

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
- **Accession:** IPR007197
- **Name:** Radical SAM
- **Short name:** rSAM
- **Entry type:** domain
- **Integrated into / parent:** None (top-level entry)
- **Member database signatures:** SFLDS00029 (sfld: Radical SAM); PS51918 (profile: Radical SAM core domain profile); PF04055 (pfam: Radical SAM superfamily)
- **Scale:** 316821 proteins across 36891 taxa, 0 subfamilies
- **Current InterPro2GO terms (the mappings under review):** GO:0003824 catalytic activity [F]; GO:0051536 iron-sulfur cluster binding [F]
- **InterPro description:** The Radical SAM domain is organised in a fold related to the β-barrel or TIM barrel, in which β-strands are arranged in a barrel-like array, with peripheral helices intervening between β-strands. The [4Fe-4S] clusters and substrates are bound within the barrels, as is typical of TIM barrel enzymes [[cite:PUB00097557], [cite:PUB00097556]]. Radical SAM proteins are found in all domains of life and share an unusual Fe-S cluster associated with generation of a free radical by reductive cleavage of SAM and often provide an anaerobic or oxygen-independent mechanism that is found as an aerobic reaction in other proteins. Radical SAM proteins catalyse diverse reactions, including unusual methylations, isomerisation, sulphur insertion, ring formation, anaerobic oxidation and protein radical formation. These proteins function in DNA precursor, vitamin, cofactor, antibiotic and herbicide biosynthesis and in biodegradation pathways [[cite:PUB00010539], [cite:PUB00015124]]. Radical SAM proteins share several common features, notably three strictly conserved cysteine residues generally included in the CxxxCxxC motif. These critical cysteines coordinate the unusual [4Fe-4S]2+/1+ cluster, while SAM serves as ligand for the fourth iron atom and acts as a cofactor or a cosubstrate . The radical SAM enzymes biochemically characterised to date have in common the cleavage of the [4Fe-4S]1+-SAM complex to [4Fe-4S]2+-Met and the 5'-deoxyadenosyl radical, which abstracts a hydrogen atom from the sub ...

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**IPR007197 (Radical SAM)**, structured to support GO annotation review.

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


# Comprehensive Research Report on InterPro Entry IPR007197 (Radical SAM Domain)

## Executive Summary

This report evaluates the Gene Ontology (GO) annotations for InterPro entry IPR007197, the Radical SAM domain, to determine whether current InterPro2GO mappings are appropriate for a domain-level signature that matches 316,821 proteins across 36,891 taxa. Based on comprehensive analysis of recent literature (2018-2024), both current GO terms—**GO:0003824 (catalytic activity)** and **GO:0051536 (iron-sulfur cluster binding)**—are **APPROPRIATE** and should be **ACCEPTED**. These terms accurately describe conserved biochemical properties of the Radical SAM domain itself rather than whole-protein functions, making them valid domain-level annotations that avoid over-annotation.

---

## 1. Family Definition and Biochemistry

### 1.1 Structural Architecture

The Radical SAM domain adopts a **TIM barrel-related fold**, with structural diversity ranging from full (β/α)₈ barrels to pruned variants including (β/α)₆ and other partial barrel architectures (holliday2018atlasofthe pages 8-12, holliday2018atlasofthe pages 5-8). The canonical superfamily is defined by the **[4Fe-4S] cluster-binding motif**, which organizes β-strands into a barrel-like array with peripheral helices intervening between β-strands (holliday2018atlasofthe pages 1-5). The [4Fe-4S] clusters and substrates are bound within the barrels, consistent with typical TIM barrel enzyme architecture (holliday2018atlasofthe pages 1-5).

Structural characterization across multiple Radical SAM enzymes reveals considerable topological variation, from full TIM barrels (e.g., biotin synthase, PDB: 1R30) to three-quarter barrels (coproporphyrinogen-III oxidase, PDB: 1OLT) and further pruned variants such as (β₆/α₃) in 7-carboxy-7-deazaguanine synthase and (β₅/α₄) in 2-deoxy-scillo-inosamine dehydrogenase (holliday2018atlasofthe pages 8-12).

### 1.2 Conserved Catalytic Residues and Binding Motif

The defining structural feature of the Radical SAM superfamily is the **canonical CxxxCxxC motif** (where x represents any amino acid), which coordinates a [4Fe-4S] cluster (holliday2018atlasofthe pages 1-5, wang2018cobalamindependentradicalsadenosyllmethionine pages 1-3, boswinkle2022highlightingtheunique pages 1-3). More than 90% of Radical SAM proteins contain this canonical motif, while the remainder exhibit variations where cysteine pairs are separated by 2-3 residues or where spacing ranges from 3 to 22 residues (holliday2018atlasofthe pages 1-5). 

The three cysteine residues coordinate three iron atoms of the [4Fe-4S] cluster, leaving the **apical (fourth) iron atom free** to coordinate S-adenosylmethionine (SAM) in a bidentate manner through its amino and carboxylate groups (holliday2018atlasofthe pages 1-5, wang2018cobalamindependentradicalsadenosyllmethionine pages 1-3, boswinkle2022highlightingtheunique pages 1-3). This unique iron-SAM interaction is mechanistically critical and highly conserved across characterized Radical SAM structures (wang2018cobalamindependentradicalsadenosyllmethionine pages 1-3).

### 1.3 Mechanistic Biochemistry

The Radical SAM superfamily was originally defined by Sofia et al. (2001) based on three minimal characteristics that define canonical members (holliday2018atlasofthe pages 1-5):

1. **The unique three-cysteine [4Fe-4S] cluster-binding motif** described above
2. **A common activation step** involving formation of the 5'-deoxyadenosyl (5'-dA•) radical and methionine
3. **Requirement for an external electron donor** to catalyze initial reduction of the [4Fe-4S] cluster from the resting [4Fe-4S]²⁺ state to the active [4Fe-4S]¹⁺ state

The **conserved catalytic mechanism** proceeds as follows: Upon reduction to the +1 state, the [4Fe-4S]¹⁺ cluster donates an electron to the sulfonium group of SAM bound to the fourth iron, resulting in **reductive homolytic cleavage** of the C5'-S bond of SAM to generate methionine and the highly reactive **5'-deoxyadenosyl radical (5'-dA•)** (holliday2018atlasofthe pages 1-5, ruszczycky2024initiationpropagationand pages 1-3, boswinkle2022highlightingtheunique pages 1-3, benjdia2021radicalsamenzymes pages 3-5). This 5'-dA• radical then abstracts a hydrogen atom from an otherwise unreactive substrate site, generating 5'-deoxyadenosine (5'-dAdoH) and a substrate radical that undergoes further transformations (boswinkle2022highlightingtheunique pages 1-3, benjdia2021radicalsamenzymes pages 3-5).

This radical initiation chemistry is a **universally conserved feature** of the Radical SAM domain, with only rare exceptions such as the tryptophan methyltransferase TsrM, which does not catalyze formation of the 5'-dA• radical despite being clearly homologous to canonical Radical SAM sequences (holliday2018atlasofthe pages 5-8).

The mechanism has been described as proceeding through **three phases**—initiation, propagation, and termination—with radical SAM enzymes being defined by their common initiation mechanism coupling reduction of SAM by the [4Fe-4S]¹⁺ cluster to generation of the initial substrate radical (ruszczycky2024initiationpropagationand pages 1-3).

### 1.4 Cofactors and Prosthetic Groups

The [4Fe-4S] cluster is the **second most common cofactor/prosthetic group** in proteins tracing to the Last Universal Common Ancestor (LUCA), behind only ATP, reflecting the ancient and fundamental nature of iron-sulfur cluster biochemistry (weiss2016thephysiologyand pages 1-2). Radical SAM proteins are characterized as **metalloenzymes** that employ the [4Fe-4S]²⁺/¹⁺ cluster along with SAM to generate the 5'-dA• radical capable of initiating catalysis on otherwise unreactive substrates (boswinkle2022highlightingtheunique pages 1-3).

Beyond the obligate [4Fe-4S] cluster and SAM, many Radical SAM enzymes—particularly those in the **SPASM/twitch domain-containing subfamily**—possess **one or two additional auxiliary iron-sulfur clusters** in their C-terminal regions (barr2018xrayandepr pages 1-3, benjdia2021radicalsamenzymes pages 3-5). The functions of these auxiliary clusters remain incompletely understood but likely include roles in electron transfer during substrate radical termination, substrate positioning, and in some cases unusual ligand coordination (e.g., tyrosyl ligation in cyclopropyl synthases) (barr2018xrayandepr pages 1-3, lien2024structuralbiochemicaland pages 1-2).

A substantial subset of Radical SAM enzymes also incorporate **cobalamin (vitamin B₁₂)** as an additional cofactor, requiring a fused B₁₂-binding domain (wang2018cobalamindependentradicalsadenosyllmethionine pages 1-3, holliday2018atlasofthe pages 8-12). This B₁₂-dependent Radical SAM group represents a major modular expansion of the superfamily.

---

## 2. InterPro2GO Mapping Appropriateness

### 2.1 Analysis Framework

IPR007197 is a **domain-level signature**, not a family-level annotation. The critical distinction is that domain annotations should describe **conserved properties intrinsic to the domain module itself**, not whole-protein functions that vary across the diverse contexts in which the domain is embedded. Whole-protein activities (e.g., "biotin synthase activity" or "lipoyl synthase activity") would constitute over-annotation when applied to a domain signature, because multi-domain proteins containing the Radical SAM domain perform vastly different overall catalytic functions depending on their accessory domains and biological contexts.

### 2.2 GO:0003824 (Catalytic Activity) — Molecular Function

**Assessment: ACCEPT**

Catalytic activity is a **defining, universally conserved property** of the canonical Radical SAM superfamily. The superfamily was originally defined as "a homologous group of enzymes united by their utilization of SAM in a radical mechanism" (holliday2018atlasofthe pages 1-5). All members are metalloenzymes that catalyze radical-based chemical transformations (benjdia2021radicalsamenzymes pages 3-5).

Although GO:0003824 is extremely generic and provides minimal biological information, it is **not incorrect** for a domain-level annotation. The term accurately reflects that the Radical SAM domain itself provides catalytic function—specifically, the ability to generate reactive radical intermediates from SAM—rather than serving a purely structural, regulatory, or transport role. This catalytic capability is intrinsic to the domain fold and cluster-binding motif, not conferred by accessory domains.

**Potential concerns:**
- **Generic/low-information:** GO:0003824 is the root molecular function term for all enzymes. More specific catalytic terms (e.g., "oxidoreductase activity" or "transferase activity") would be informative but would fail to capture the full mechanistic diversity of Radical SAM subfamilies, which span multiple EC classes (holliday2018atlasofthe pages 1-5, holliday2018atlasofthe pages 12-15).
- **Reaction diversity:** The superfamily catalyzes a "dizzying array of disparate" reactions including methylation, isomerization, sulfur insertion, ring formation, C-C bond formation, C-S bond formation, epimerization, and cofactor biosynthesis (holliday2018atlasofthe pages 1-5, holliday2018atlasofthe pages 5-8, benjdia2021radicalsamenzymes pages 3-5). Reaction types "fail to track well with sequence similarity-based subgroupings," meaning specific catalytic terms would over-specify and misrepresent the domain's versatility (holliday2018atlasofthe pages 1-5).

**Recommendation:** ACCEPT and retain GO:0003824. While generic, this term correctly identifies the Radical SAM domain as catalytic without overstating mechanistic uniformity. If InterPro prefers higher-information annotations, this term could optionally be flagged as **non-core** (lower-confidence/generic) rather than replaced with a narrower, potentially misleading term.

### 2.3 GO:0051536 (Iron-Sulfur Cluster Binding) — Molecular Function

**Assessment: ACCEPT**

Iron-sulfur cluster binding is an **absolutely conserved, mechanistically essential property** of the Radical SAM domain. More than 90% of superfamily members contain the canonical CxxxCxxC motif coordinating the [4Fe-4S] cluster (holliday2018atlasofthe pages 1-5). The [4Fe-4S] cluster is not merely a structural component but is central to the **mechanistic definition** of the superfamily: the cluster in its reduced [4Fe-4S]¹⁺ form is required for reductive cleavage of SAM and radical initiation (holliday2018atlasofthe pages 1-5, boswinkle2022highlightingtheunique pages 1-3, benjdia2021radicalsamenzymes pages 3-5).

All comprehensive reviews and structural studies describe the Radical SAM domain as an **Fe-S-binding metalloenzyme** (holliday2018atlasofthe pages 1-5, wang2018cobalamindependentradicalsadenosyllmethionine pages 1-3, boswinkle2022highlightingtheunique pages 1-3, benjdia2021radicalsamenzymes pages 3-5). The presence and proper coordination of the [4Fe-4S] cluster by the conserved cysteine motif is a **prerequisite for function** across the entire superfamily, including diverse subfamilies and multi-domain architectures.

**Why this term is appropriate:**
- **Universality:** The [4Fe-4S] cluster binding property applies to >90% of members and is conserved across all major subfamilies (holliday2018atlasofthe pages 1-5).
- **Domain-intrinsic:** The cluster is coordinated by residues within the Radical SAM domain core fold itself, not by accessory domains.
- **Mechanistically critical:** The cluster is not merely bound but actively participates in catalysis through electron transfer and SAM activation.
- **Specificity:** GO:0051536 is more informative than generic "metal ion binding" terms and accurately specifies the type of prosthetic group.

**Potential alternative considerations:**
- **[4Fe-4S] cluster binding:** A more specific child term of GO:0051536 exists (GO:0051539) but would not add substantial value given that the canonical [4Fe-4S] cluster is already the predominant Fe-S cluster type in this superfamily.

**Recommendation:** ACCEPT and retain GO:0051536. This term captures a universally conserved, mechanistically essential biochemical property of the Radical SAM domain and is appropriately specific without being overly narrow.

### 2.4 Summary Table of Current Mappings

| GO term ID and name | Term type | Appropriateness assessment | Rationale based on evidence | Universality across all proteins with the domain | Recommendation |
|---|---|---|---|---|---|
| GO:0003824 catalytic activity | MF | ACCEPT | The canonical Radical SAM superfamily is defined as a homologous group of enzymes that use SAM in radical chemistry; Holliday et al. state that to be considered a member, proteins share a common activation step for forming the 5'-deoxyadenosyl radical and require an external electron donor, while Benjdia & Berteau describe Radical SAM enzymes as metalloenzymes catalyzing diverse radical-based reactions. Although the exact reaction differs greatly among subfamilies, catalytic function is a conserved property of the Radical SAM domain itself rather than a pathway-specific whole-protein process. This term is very generic and low-information, but not incorrect for a domain entry (holliday2018atlasofthe pages 1-5, holliday2018atlasofthe pages 5-8, benjdia2021radicalsamenzymes pages 3-5). | Yes | KEEP/ACCEPT as a broad non-specific MF term; if InterPro prefers higher-information mappings, this could be kept as non-core rather than replaced with a narrower catalytic GO term that would overstate mechanistic uniformity. |
| GO:0051536 iron-sulfur cluster binding | MF | ACCEPT | Iron-sulfur cluster binding is a core, mechanistically defining property of the Radical SAM domain. The canonical superfamily is defined by a three-cysteine motif, usually CxxxCxxC, that coordinates a [4Fe-4S] cluster, leaving the fourth iron to bind SAM; >90% of members contain this motif, and the [4Fe-4S] cluster is central to SAM reductive cleavage and radical initiation. Reviews and structural work consistently describe the Radical SAM core as an Fe-S-binding metalloenzyme domain, including in diverse subfamilies and architectures (holliday2018atlasofthe pages 1-5, wang2018cobalamindependentradicalsadenosyllmethionine pages 1-3, boswinkle2022highlightingtheunique pages 1-3, benjdia2021radicalsamenzymes pages 3-5). | Yes | ACCEPT and retain. This term captures a universally conserved biochemical property of the domain itself and is more specific and informative than generic metal-ion-binding terms. |


*Table: This table evaluates the two current InterPro2GO mappings for the Radical SAM domain against evidence about conserved domain-level properties. It is useful for deciding whether the mappings should be retained, modified, or removed during GO annotation review.*

---

## 3. Functional Divergence Across the Family

### 3.1 Superfamily-Scale Diversity

The Radical SAM superfamily exhibits **extraordinary functional diversity** despite conservation of the core domain structure and radical-initiation mechanism. As of 2018, the superfamily contained over 113,000 non-redundant sequences organized into **more than 100 distinct functional families** (holliday2018atlasofthe pages 1-5, holliday2018atlasofthe pages 12-15). By 2024, estimates exceeded 500,000 members across ~100 distinct families (benjdia2021radicalsamenzymes pages 3-5), making it one of the largest and most diverse enzyme superfamilies known.

Holliday et al. (2018) classified the superfamily into **20 Level 1 subgroups with at least one known function**, plus **22 additional uncharacterized subgroups** composed entirely of sequences of unknown function (holliday2018atlasofthe pages 1-5, holliday2018atlasofthe pages 54-57, holliday2018atlasofthe pages 12-15). Even within characterized subgroups, "reaction types fail to track well with sequence similarity-based subgroupings, raising major challenges for function prediction" (holliday2018atlasofthe pages 1-5).

### 3.2 Major Subfamilies and Their Divergent Functions

| Subfamily / Level 1 subgroup | Representative reactions / functions | Key structural features / additional domains | Example enzymes | Evidence |
|---|---|---|---|---|
| SPASM/twitch domain-containing | Broad RiPP and cofactor chemistry; peptide C–C and C–S bond formation, oxidative transformations, and other substrate-radical reactions; includes highly diverse sublineages and many uncharacterized members | Radical SAM core plus C-terminal SPASM/twitch domain carrying one or two auxiliary Fe–S clusters; often additional peptide-recognition elements in RiPP enzymes | PqqE, AlbA, SkfB, MftC, SuiB, TigE | (holliday2018atlasofthe pages 54-57, benjdia2021radicalsamenzymes pages 3-5, lien2024structuralbiochemicaland pages 1-2) |
| B12-binding domain-containing | Cobalamin-assisted radical SAM chemistry, especially unusual methylations and other natural-product tailoring reactions | Radical SAM core fused to a cobalamin-binding domain; exemplifies modular domain accretion around the RS core | Fom3, BcpD, Fms7, TsrM-related enzymes | (wang2018cobalamindependentradicalsadenosyllmethionine pages 1-3, holliday2018atlasofthe pages 8-12, holliday2018atlasofthe pages 54-57) |
| Methylthiotransferase | tRNA/protein methylthiolation; C–H to C–S bond conversion in nucleic-acid and protein modification | N-terminal methylthiotransferase region, central radical-generating core, and C-terminal TRAM RNA-binding domain in many members | MiaB, RimO, CDK5RAP1, MtaB | (holliday2018atlasofthe pages 54-57) |
| Methyltransferase (Class A) | Radical-mediated methylation of chemically difficult centers; broad substrate scope across natural products and other metabolites | Radical SAM core with subgroup-specific sequence features; may include accessory domains depending on family | Diverse class A methyltransferases cataloged in RSS atlas | (holliday2018atlasofthe pages 54-57, holliday2018atlasofthe pages 12-15) |
| Methyltransferase (Class D) | Distinct radical SAM methyltransferase clade with divergent substrate specificities | Radical SAM core with subgroup-specific motif variations and family-dependent accessory modules | Diverse class D methyltransferases in the RSS atlas | (holliday2018atlasofthe pages 54-57, holliday2018atlasofthe pages 12-15) |
| Lipoyl synthase-like | Sulfur insertion in lipoate biosynthesis and related sulfur-incorporation reactions | Canonical radical SAM core; some evolutionary variants split function across multiple proteins | LipA, LipS1, LipS2 | (holliday2018atlasofthe pages 5-8, tanabe2023identificationofa pages 1-2) |
| Organic radical-activating enzymes | Activation of glycyl or other protein-centered radicals used by partner enzymes; initiates anaerobic metabolism pathways | Typically single RS core domain without extensive tailoring domains in prototypic members | PFL-AE, NrdG | (holliday2018atlasofthe pages 1-5, holliday2018atlasofthe pages 54-57) |
| 7-Carboxy-7-deazaguanine synthase-like | Cofactor and modified-base biosynthesis in 7-deazapurine pathways | RS core embedded in subgroup-specific architectures; distinct from RiPP-focused SPASM enzymes | 7-carboxy-7-deazaguanine synthase family enzymes | (holliday2018atlasofthe pages 8-12, holliday2018atlasofthe pages 54-57) |
| Anaerobic coproporphyrinogen-III oxidase-like | Heme biosynthesis under anaerobic conditions | Often relatively compact RS enzymes built around pruned TIM-barrel-like RS core | HemN / anaerobic coproporphyrinogen-III oxidase | (holliday2018atlasofthe pages 8-12, holliday2018atlasofthe pages 54-57) |
| F420 / menaquinone cofactor biosynthesis | Cofactor biosynthesis, including steps in F420 and menaquinone formation | RS core with family-specific accessory features; broad metabolic roles rather than a single chemistry | MqnE-pathway and F420-pathway radical SAM enzymes | (holliday2018atlasofthe pages 54-57) |
| FeMo cofactor biosynthesis protein | Metallocofactor assembly for nitrogenase-related systems | RS core adapted for complex metallocluster biogenesis | NifB-like proteins | (holliday2018atlasofthe pages 5-8, holliday2018atlasofthe pages 54-57) |
| PLP-dependent | Reactions coupling RS chemistry with pyridoxal phosphate-dependent transformations | Radical SAM domain combined with PLP-dependent catalytic framework | L-lysine 2,3-aminomutase and related enzymes | (holliday2018atlasofthe pages 1-5, holliday2018atlasofthe pages 54-57) |
| Spore photoproduct lyase-like | Direct DNA repair of spore photoproduct lesions | RS core with DNA-repair specialization; generally no SPASM tail required | Spore photoproduct lyase (SPL) | (holliday2018atlasofthe pages 5-8, benjdia2021radicalsamenzymes pages 3-5) |
| tRNA wybutosine-synthesizing | Complex tRNA base modification in wybutosine biosynthesis | RS core with family-specific RNA-recognition and tailoring features | TYW1 and related wybutosine-pathway enzymes | (holliday2018atlasofthe pages 5-8, holliday2018atlasofthe pages 54-57) |
| BATS domain-containing | Diverse and incompletely characterized chemistry; large subgroup indicating major functional expansion beyond well-studied families | Radical SAM core plus BATS-like accessory domain | BATS-domain RS enzymes from the RSS atlas | (holliday2018atlasofthe pages 54-57, holliday2018atlasofthe pages 8-12) |
| Antiviral proteins | Defense-associated radical SAM activities; exact chemistry unresolved for many members | RS core in defense-related architectures; substantial sequence divergence | Antiviral protein subgroup members in RSS atlas | (holliday2018atlasofthe pages 54-57) |
| Elongator protein-like | Eukaryotic and archaeal tRNA-modification-associated radical SAM chemistry | RS core in Elongator-associated architecture; concentrated in fewer eukaryotic subgroups | Elp3-like radical SAM proteins | (holliday2018atlasofthe pages 54-57) |
| Overall superfamily trend | The Radical SAM superfamily catalyzes an exceptionally broad range of reactions including methylation, isomerization, sulfur insertion, ring formation, peptide crosslinking, carbon–carbon bond formation, radical activation, and cofactor biosynthesis; reaction type does not map cleanly onto the whole superfamily | Conserved RS “plug-and-play” core domain, usually a TIM-barrel-related fold with a CxxxCxxC motif binding a [4Fe-4S] cluster, combined with many accessory domains and multidomain architectures | BioB, LipA, PFL-AE, NrdG, PqqE, TsrM, TigE and many others | (holliday2018atlasofthe pages 1-5, holliday2018atlasofthe pages 8-12, holliday2018atlasofthe pages 5-8, holliday2018atlasofthe pages 12-15, benjdia2021radicalsamenzymes pages 3-5) |


*Table: This table summarizes the major Radical SAM subgroups and illustrates how a conserved radical-SAM core is combined with different accessory domains to support widely divergent chemistries. It is useful for GO review because it shows why domain-level annotations should stay close to universally conserved properties rather than subgroup-specific whole-protein functions.*

Key observations from the functional diversity analysis:

1. **SPASM/Twitch domain-containing enzymes** (the largest subgroup with >18,000 sequences) catalyze diverse RiPP modifications, cofactor biosynthesis, and other radical-based transformations, with many members catalyzing chemically unrelated reactions despite sharing the SPASM domain architecture (holliday2018atlasofthe pages 54-57, benjdia2021radicalsamenzymes pages 3-5).

2. **B12-binding domain-containing enzymes** represent a major evolutionary innovation coupling radical SAM chemistry with cobalamin-assisted methylations and other tailoring reactions in natural product biosynthesis (wang2018cobalamindependentradicalsadenosyllmethionine pages 1-3, holliday2018atlasofthe pages 8-12, holliday2018atlasofthe pages 54-57).

3. **Methylthiotransferases** catalyze tRNA and protein methylthiolation (C-H to C-S bond conversion), a biochemically distinct reaction from most other Radical SAM subfamilies (holliday2018atlasofthe pages 54-57).

4. **Lipoyl synthase-like enzymes** insert sulfur atoms into fatty acid precursors, a specialized chemistry not generalizable to other subfamilies (holliday2018atlasofthe pages 5-8, holliday2018atlasofthe pages 54-57, tanabe2023identificationofa pages 1-2).

5. **Organic radical-activating enzymes** (e.g., pyruvate formate-lyase activating enzyme, PFL-AE) generate protein-centered radicals for partner enzymes rather than directly transforming small-molecule substrates (holliday2018atlasofthe pages 1-5, holliday2018atlasofthe pages 54-57).

### 3.3 Are There Catalytically Inactive (Pseudo-Enzyme) Members?

**No evidence for catalytically dead Radical SAM pseudo-enzymes** was found in the literature reviewed. However, one notable exception to the canonical mechanism exists: **TsrM**, a tryptophan methyltransferase involved in thiostrepton biosynthesis, is clearly homologous to canonical Radical SAM sequences but **does not catalyze formation of the 5'-dA• radical**, instead using a distinct methylation mechanism (holliday2018atlasofthe pages 5-8). This represents mechanistic innovation within the superfamily fold rather than catalytic inactivation.

The absence of widespread pseudo-enzymes is consistent with the mechanistic centrality of the [4Fe-4S] cluster and SAM: loss of cluster binding or SAM reactivity would likely eliminate selective pressure to maintain the domain fold. The superfamily's defining biochemical activities—iron-sulfur cluster binding and catalytic function—thus remain universally relevant.

### 3.4 Implications for GO Annotation

The extreme functional divergence documented above **supports the appropriateness of generic domain-level GO terms** (catalytic activity, iron-sulfur cluster binding) while **arguing strongly against subfamily-specific whole-protein function terms**. For example:

- Annotating IPR007197 with "biotin synthase activity" would incorrectly propagate that term to >316,000 proteins, the vast majority of which are not biotin synthases.
- Annotating with "methyltransferase activity" would similarly over-annotate proteins in non-methylating subfamilies.
- Even relatively broad terms like "oxidoreductase activity" would misrepresent subfamilies performing isomerizations, radical activations, or C-C bond formations without net redox changes.

The current GO mappings correctly avoid this over-annotation pitfall by restricting annotations to universally conserved domain properties.

---

## 4. Taxonomic Scope

### 4.1 Distribution Across Domains of Life

Radical SAM proteins are found in **all three domains of life**—Bacteria, Archaea, and Eukaryotes—with an ancient origin predating the divergence of Bacteria and Archaea (holliday2018atlasofthe pages 1-5, holliday2018atlasofthe pages 54-57, weiss2016thephysiologyand pages 1-2). The superfamily's ubiquity across the biosphere provides strong evidence for its presence in the **Last Universal Common Ancestor (LUCA)** (holliday2018atlasofthe pages 54-57, weiss2016thephysiologyand pages 1-2).

Analysis of 355 protein families tracing to LUCA by phylogenetic criteria identified multiple Radical SAM enzymes among LUCA's core metabolic machinery, including members involved in cofactor biosynthesis, tRNA modification, and other fundamental processes (weiss2016thephysiologyand pages 1-2). Radical SAM enzymes in LUCA were characterized by FeS clusters, radical reaction mechanisms, dependence on transition metals and SAM-dependent methylations (weiss2016thephysiologyand pages 1-2).

### 4.2 Quantitative Taxonomic Distribution

- **Bacteria** contain the largest proportion of Radical SAM sequences, with the vast majority of superfamily members encoded in bacterial genomes (boswinkle2022highlightingtheunique pages 1-3, holliday2018atlasofthe pages 54-57).
- **Archaea** represent the second-largest proportion, with Radical SAM proteins globally distributed across archaeal lineages (holliday2018atlasofthe pages 54-57). Methanogenic archaea are particularly enriched in Radical SAM enzymes, with unique functions in methanogenesis-specific pathways (boswinkle2022highlightingtheunique pages 1-3).
- **Eukaryotes** have the fewest Radical SAM superfamily members, with these sequences concentrated in a small number of subgroups (boswinkle2022highlightingtheunique pages 1-3, holliday2018atlasofthe pages 54-57). Human genomes encode only eight Radical SAM enzymes, all with established functions, primarily in mitochondrial metabolism (boswinkle2022highlightingtheunique pages 1-3).

Sequence similarity network analysis by Holliday et al. (2018) visualized the taxonomic distribution, showing bacterial sequences (gray) dominating the network, archaeal sequences (red) globally distributed across subgroups, and eukaryotic sequences (blue, yellow, green for vertebrates, invertebrates, and plants) forming discrete clusters within specific subgroups (holliday2018atlasofthe pages 54-57).

### 4.3 Implications for GO Term Universality

The universal distribution of Radical SAM proteins across all domains of life, coupled with their ancient origin in LUCA, confirms that the conserved biochemical properties described by GO:0003824 and GO:0051536 are **taxonomically unrestricted**. Both terms apply equally to:

- Bacterial Radical SAM proteins in primary and secondary metabolism
- Archaeal Radical SAM proteins in methanogenesis and extremophile adaptations (e.g., tetraether lipid biosynthesis) (li2024biosynthesisofgmgt pages 1-2)
- Eukaryotic Radical SAM proteins in mitochondrial and chloroplast metabolism

No evidence suggests that the [4Fe-4S] cluster-binding mechanism or catalytic function varies systematically by taxonomic lineage. The current GO mappings are therefore appropriate across the full taxonomic scope of IPR007197.

---

## 5. Over-Annotation Verdict and Recommendations

### 5.1 Summary Assessment

**VERDICT: Both current InterPro2GO mappings for IPR007197 (Radical SAM domain) are APPROPRIATE and should be ACCEPTED without modification.**

The two GO terms—**GO:0003824 (catalytic activity)** and **GO:0051536 (iron-sulfur cluster binding)**—accurately describe **conserved biochemical properties intrinsic to the Radical SAM domain** rather than whole-protein functions that vary across subfamilies. Both terms apply universally (>90% of members) across all subfamilies and taxonomic groups.

Critically, the current mappings **correctly avoid over-annotation** by not assigning subfamily-specific or pathway-specific molecular function terms (e.g., "biotin synthase activity," "methyltransferase activity," "lipoyl synthase activity") that would systematically misannotate the >316,000 proteins containing this domain. Because IPR007197 is a **domain signature** (entry type: domain), not a family signature, the GO terms should describe domain-level properties, which the current mappings do appropriately.

### 5.2 Detailed Recommendations

#### For GO:0003824 (Catalytic Activity)
- **Action:** ACCEPT / KEEP
- **Rationale:** All canonical Radical SAM proteins are enzymes. Catalytic function is a defining characteristic of the superfamily and is intrinsic to the domain fold and [4Fe-4S]-SAM chemistry.
- **Caveat:** This is a very generic term providing minimal biological specificity. If InterPro curators prefer higher-information annotations, GO:0003824 could be flagged as **KEEP_AS_NON_CORE** (retained but marked as low-specificity) rather than removed entirely. However, attempting to replace it with a more specific catalytic term (e.g., "oxidoreductase activity") would be inappropriate given the mechanistic diversity of the superfamily.

#### For GO:0051536 (Iron-Sulfur Cluster Binding)
- **Action:** ACCEPT / KEEP
- **Rationale:** The [4Fe-4S] cluster coordinated by the CxxxCxxC motif is absolutely conserved and mechanistically essential. This term is both universally applicable and appropriately specific for a domain annotation.
- **Strength:** GO:0051536 is substantially more informative than generic "metal ion binding" while remaining accurate across all subfamilies.

### 5.3 Recommendations for InterPro Entry Curation

While the current GO mappings are sound, the following actions could enhance the clarity and utility of IPR007197:

1. **Confirm entry type as "domain":** The InterPro API correctly identifies IPR007197 as entry type "domain." This classification should be explicitly maintained to ensure downstream tools understand that GO annotations apply to the domain module, not whole-protein activities.

2. **Consider subfamily-specific child entries:** The extreme functional diversity within the Radical SAM superfamily (>100 families with divergent reactions) suggests that InterPro might benefit from creating **child signatures** for major functionally homogeneous subfamilies (e.g., "Biotin synthase family," "Lipoyl synthase family," "SPASM/Twitch RiPP-modifying enzymes"). These child entries could carry more specific GO annotations (e.g., "biotin synthase activity" → biotin synthase family signature) while the parent domain entry (IPR007197) retains only the broad catalytic activity and Fe-S cluster binding terms. This hierarchical approach would prevent over-annotation at the domain level while enabling precise annotation at the family level.

3. **No process or component terms recommended:** Current mappings include no Biological Process (BP) or Cellular Component (CC) terms, which is appropriate. Radical SAM proteins participate in diverse processes (DNA repair, cofactor biosynthesis, natural product biosynthesis, etc.) that are subfamily- and organism-specific, not domain-level properties. Similarly, cellular localization varies (cytoplasm, mitochondria, chloroplasts, etc.) depending on full-protein architecture and organism. Adding generic BP/CC terms would add little value; adding specific terms would over-annotate.

### 5.4 Final GO Action Pattern

| GO Term | Current Status | Recommended Action |
|---------|---------------|-------------------|
| GO:0003824 (catalytic activity) | Mapped to IPR007197 | **ACCEPT** (or optionally **KEEP_AS_NON_CORE** if InterPro flags low-specificity terms) |
| GO:0051536 (iron-sulfur cluster binding) | Mapped to IPR007197 | **ACCEPT** |

**No modifications, additions, or removals recommended for the current GO mappings.**

---

## 6. Conclusion

The InterPro2GO mappings for IPR007197 (Radical SAM domain) exemplify **appropriate domain-level GO annotation**. Both terms—catalytic activity and iron-sulfur cluster binding—describe conserved biochemical properties of the domain module itself, apply universally across subfamilies and taxa, and correctly avoid the pitfall of assigning subfamily-specific whole-protein functions to a domain signature that matches >316,000 structurally and functionally diverse proteins.

The Radical SAM domain is a quintessential example of a **"plug and play" modular domain** (holliday2018atlasofthe pages 12-15) that provides a conserved catalytic core (Fe-S cluster-based radical generation from SAM) embedded in vastly different multi-domain architectures and biological contexts. GO annotation at the domain level must therefore focus on the invariant properties of the "plug" (the domain itself) rather than the variable properties of the whole "device" (the full-length protein with accessory domains). The current mappings achieve this goal.

This analysis supports **retaining both current GO terms without modification** and recommends that InterPro continue its conservative approach to domain-level GO annotation for other similarly diverse superfamily domains.

---

## References

All claims are supported by citations to peer-reviewed literature from 2016-2024, with particular reliance on:

- Holliday et al. (2018) "Atlas of the Radical SAM Superfamily" (Methods in Enzymology) — comprehensive superfamily classification and functional diversity analysis (holliday2018atlasofthe pages 1-5, holliday2018atlasofthe pages 8-12, holliday2018atlasofthe pages 5-8, holliday2018atlasofthe pages 54-57, holliday2018atlasofthe pages 12-15)
- Ruszczycky & Liu (2024) "Initiation, Propagation, and Termination in the Chemistry of Radical SAM Enzymes" (Biochemistry) — mechanistic review (ruszczycky2024initiationpropagationand pages 1-3)
- Benjdia & Berteau (2021) "Radical SAM Enzymes and Ribosomally-Synthesized and Post-translationally Modified Peptides" (Frontiers in Chemistry) — RiPP-modifying subfamily review (benjdia2021radicalsamenzymes pages 1-3, benjdia2021radicalsamenzymes pages 3-5)
- Boswinkle et al. (2022) "Highlighting the Unique Roles of Radical S-Adenosylmethionine Enzymes in Methanogenic Archaea" (Journal of Bacteriology) — archaeal Radical SAM distribution (boswinkle2022highlightingtheunique pages 1-3)
- Weiss et al. (2016) "The physiology and habitat of the last universal common ancestor" (Nature Microbiology) — LUCA reconstruction identifying ancient Radical SAM proteins (weiss2016thephysiologyand pages 1-2)

Additional structural, biochemical, and taxonomic evidence from Barr et al. (2018), Wang (2018), Lien et al. (2024), Li et al. (2024), Tanabe et al. (2023), and others provides corroborating support for conserved domain properties (barr2018xrayandepr pages 1-3, wang2018cobalamindependentradicalsadenosyllmethionine pages 1-3, lien2024structuralbiochemicaland pages 1-2, li2024biosynthesisofgmgt pages 1-2, tanabe2023identificationofa pages 1-2).

References

1. (holliday2018atlasofthe pages 8-12): Gemma L. Holliday, Eyal Akiva, Elaine C. Meng, Shoshana D. Brown, Sara Calhoun, Ursula Pieper, Andrej Sali, Squire J. Booker, and Patricia C. Babbitt. Atlas of the radical sam superfamily: divergent evolution of function using a "plug and play" domain. Methods in enzymology, 606:1-71, Jan 2018. URL: https://doi.org/10.1016/bs.mie.2018.06.004, doi:10.1016/bs.mie.2018.06.004. This article has 155 citations and is from a peer-reviewed journal.

2. (holliday2018atlasofthe pages 5-8): Gemma L. Holliday, Eyal Akiva, Elaine C. Meng, Shoshana D. Brown, Sara Calhoun, Ursula Pieper, Andrej Sali, Squire J. Booker, and Patricia C. Babbitt. Atlas of the radical sam superfamily: divergent evolution of function using a "plug and play" domain. Methods in enzymology, 606:1-71, Jan 2018. URL: https://doi.org/10.1016/bs.mie.2018.06.004, doi:10.1016/bs.mie.2018.06.004. This article has 155 citations and is from a peer-reviewed journal.

3. (holliday2018atlasofthe pages 1-5): Gemma L. Holliday, Eyal Akiva, Elaine C. Meng, Shoshana D. Brown, Sara Calhoun, Ursula Pieper, Andrej Sali, Squire J. Booker, and Patricia C. Babbitt. Atlas of the radical sam superfamily: divergent evolution of function using a "plug and play" domain. Methods in enzymology, 606:1-71, Jan 2018. URL: https://doi.org/10.1016/bs.mie.2018.06.004, doi:10.1016/bs.mie.2018.06.004. This article has 155 citations and is from a peer-reviewed journal.

4. (wang2018cobalamindependentradicalsadenosyllmethionine pages 1-3): Susan C. Wang. Cobalamin-dependent radical s-adenosyl-l-methionine enzymes in natural product biosynthesis. Natural product reports, 35 8:707-720, Aug 2018. URL: https://doi.org/10.1039/c7np00059f, doi:10.1039/c7np00059f. This article has 49 citations and is from a peer-reviewed journal.

5. (boswinkle2022highlightingtheunique pages 1-3): Kaleb Boswinkle, Justin McKinney, and Kylie D. Allen. Highlighting the unique roles of radical <i>s</i> -adenosylmethionine enzymes in methanogenic archaea. Aug 2022. URL: https://doi.org/10.1128/jb.00197-22, doi:10.1128/jb.00197-22. This article has 11 citations and is from a peer-reviewed journal.

6. (ruszczycky2024initiationpropagationand pages 1-3): Mark W. Ruszczycky and Hung-wen Liu. Initiation, propagation, and termination in the chemistry of radical sam enzymes. Biochemistry, 63:3161-3183, Dec 2024. URL: https://doi.org/10.1021/acs.biochem.4c00518, doi:10.1021/acs.biochem.4c00518. This article has 10 citations and is from a peer-reviewed journal.

7. (benjdia2021radicalsamenzymes pages 3-5): Alhosna Benjdia and Olivier Berteau. Radical sam enzymes and ribosomally‐synthesized and post‐translationally modified peptides: a growing importance in the microbiomes. Frontiers in Chemistry, Jul 2021. URL: https://doi.org/10.3389/fchem.2021.678068, doi:10.3389/fchem.2021.678068. This article has 41 citations.

8. (weiss2016thephysiologyand pages 1-2): Madeline C. Weiss, Filipa L. Sousa, Natalia Mrnjavac, Sinje Neukirchen, Mayo Roettger, Shijulal Nelson-Sathi, and William F. Martin. The physiology and habitat of the last universal common ancestor. Nature Microbiology, Jul 2016. URL: https://doi.org/10.1038/nmicrobiol.2016.116, doi:10.1038/nmicrobiol.2016.116. This article has 1324 citations and is from a highest quality peer-reviewed journal.

9. (barr2018xrayandepr pages 1-3): Ian Barr, Troy A. Stich, Anthony S. Gizzi, Tyler L. Grove, Jeffrey B. Bonanno, John A. Latham, Tyler Chung, Carrie M. Wilmot, R. David Britt, Steven C. Almo, and Judith P. Klinman. X-ray and epr characterization of the auxiliary fe-s clusters in the radical sam enzyme pqqe. Biochemistry, 57 8:1306-1315, Feb 2018. URL: https://doi.org/10.1021/acs.biochem.7b01097, doi:10.1021/acs.biochem.7b01097. This article has 49 citations and is from a peer-reviewed journal.

10. (lien2024structuralbiochemicaland pages 1-2): Yi Lien, Jake C. Lachowicz, Aigera Mendauletova, Cynthia Zizola, Thacien Ngendahimana, Anastasiia Kostenko, Sandra S. Eaton, John A. Latham, and Tyler L. Grove. Structural, biochemical, and bioinformatic basis for identifying radical sam cyclopropyl synthases. ACS Chemical Biology, 19:370-379, Jan 2024. URL: https://doi.org/10.1021/acschembio.3c00583, doi:10.1021/acschembio.3c00583. This article has 12 citations and is from a domain leading peer-reviewed journal.

11. (holliday2018atlasofthe pages 12-15): Gemma L. Holliday, Eyal Akiva, Elaine C. Meng, Shoshana D. Brown, Sara Calhoun, Ursula Pieper, Andrej Sali, Squire J. Booker, and Patricia C. Babbitt. Atlas of the radical sam superfamily: divergent evolution of function using a "plug and play" domain. Methods in enzymology, 606:1-71, Jan 2018. URL: https://doi.org/10.1016/bs.mie.2018.06.004, doi:10.1016/bs.mie.2018.06.004. This article has 155 citations and is from a peer-reviewed journal.

12. (holliday2018atlasofthe pages 54-57): Gemma L. Holliday, Eyal Akiva, Elaine C. Meng, Shoshana D. Brown, Sara Calhoun, Ursula Pieper, Andrej Sali, Squire J. Booker, and Patricia C. Babbitt. Atlas of the radical sam superfamily: divergent evolution of function using a "plug and play" domain. Methods in enzymology, 606:1-71, Jan 2018. URL: https://doi.org/10.1016/bs.mie.2018.06.004, doi:10.1016/bs.mie.2018.06.004. This article has 155 citations and is from a peer-reviewed journal.

13. (tanabe2023identificationofa pages 1-2): Tomohisa Sebastian Tanabe, Martina Grosser, Lea Hahn, Carolin Kümpel, Hanna Hartenfels, Evelyn Vtulkin, Wanda Flegler, and Christiane Dahl. Identification of a novel lipoic acid biosynthesis pathway reveals the complex evolution of lipoate assembly in prokaryotes. PLOS Biology, 21:e3002177, Jun 2023. URL: https://doi.org/10.1371/journal.pbio.3002177, doi:10.1371/journal.pbio.3002177. This article has 12 citations and is from a highest quality peer-reviewed journal.

14. (li2024biosynthesisofgmgt pages 1-2): Yanan Li, Ting Yu, Xi Feng, Bo Zhao, Huahui Chen, Huan Yang, Xing Chen, Xiao-Hua Zhang, Hayden R. Anderson, Noah Z. Burns, Fuxing Zeng, Lizhi Tao, and Zhirui Zeng. Biosynthesis of gmgt lipids by a radical sam enzyme associated with anaerobic archaea and oxygen-deficient environments. Nature Communications, Jun 2024. URL: https://doi.org/10.1038/s41467-024-49650-x, doi:10.1038/s41467-024-49650-x. This article has 21 citations and is from a highest quality peer-reviewed journal.

15. (benjdia2021radicalsamenzymes pages 1-3): Alhosna Benjdia and Olivier Berteau. Radical sam enzymes and ribosomally‐synthesized and post‐translationally modified peptides: a growing importance in the microbiomes. Frontiers in Chemistry, Jul 2021. URL: https://doi.org/10.3389/fchem.2021.678068, doi:10.3389/fchem.2021.678068. This article has 41 citations.

## Artifacts

- [Edison artifact artifact-00](IPR007197-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](IPR007197-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. holliday2018atlasofthe pages 1-5
2. holliday2018atlasofthe pages 8-12
3. wang2018cobalamindependentradicalsadenosyllmethionine pages 1-3
4. holliday2018atlasofthe pages 5-8
5. ruszczycky2024initiationpropagationand pages 1-3
6. weiss2016thephysiologyand pages 1-2
7. boswinkle2022highlightingtheunique pages 1-3
8. benjdia2021radicalsamenzymes pages 3-5
9. holliday2018atlasofthe pages 54-57
10. li2024biosynthesisofgmgt pages 1-2
11. holliday2018atlasofthe pages 12-15
12. barr2018xrayandepr pages 1-3
13. lien2024structuralbiochemicaland pages 1-2
14. tanabe2023identificationofa pages 1-2
15. benjdia2021radicalsamenzymes pages 1-3
16. F
17. 4Fe-4S
18. [cite:PUB00097557
19. cite:PUB00097556
20. [cite:PUB00010539
21. cite:PUB00015124
22. https://doi.org/10.1016/bs.mie.2018.06.004,
23. https://doi.org/10.1039/c7np00059f,
24. https://doi.org/10.1128/jb.00197-22,
25. https://doi.org/10.1021/acs.biochem.4c00518,
26. https://doi.org/10.3389/fchem.2021.678068,
27. https://doi.org/10.1038/nmicrobiol.2016.116,
28. https://doi.org/10.1021/acs.biochem.7b01097,
29. https://doi.org/10.1021/acschembio.3c00583,
30. https://doi.org/10.1371/journal.pbio.3002177,
31. https://doi.org/10.1038/s41467-024-49650-x,