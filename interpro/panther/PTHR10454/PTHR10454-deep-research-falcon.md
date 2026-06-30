---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-28T19:55:53.682781'
end_time: '2026-06-28T20:17:27.043172'
duration_seconds: 1293.36
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR10454
  interpro_name: CASPASE
  interpro_short_name: Not specified
  interpro_type: family
  interpro_integrated: IPR002398
  member_databases: Not specified
  n_proteins: '8115'
  n_taxa: '5813'
  n_subfamilies: '24'
  interpro2go_terms: None mapped (no InterPro2GO terms for this entry)
  interpro_description: Not specified in InterPro
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 53
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PTHR10454-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR10454-deep-research-falcon_artifacts/artifact-01.md
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
- **Accession:** PTHR10454
- **Name:** CASPASE
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** IPR002398
- **Member database signatures:** Not specified
- **Scale:** 8115 proteins across 5813 taxa, 24 subfamilies
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
**PTHR10454 (CASPASE)**, structured to support GO annotation review.

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
- **Accession:** PTHR10454
- **Name:** CASPASE
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** IPR002398
- **Member database signatures:** Not specified
- **Scale:** 8115 proteins across 5813 taxa, 24 subfamilies
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
**PTHR10454 (CASPASE)**, structured to support GO annotation review.

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


# Comprehensive Research Report: InterPro Entry PTHR10454 (CASPASE) — GO Annotation Review

## 1. Family Definition and Biochemistry

### 1.1 Structural Fold and Clan Classification

The PTHR10454 CASPASE entry represents a broad protein family within clan CD of cysteine peptidases (MEROPS family C14). Clan CD is defined by a conserved structural fold comprising a central six-stranded β-sheet (five parallel and one antiparallel strand) surrounded by five conserved α-helices (Hα1–Hα5), termed the caspase–hemoglobinase fold (CHF) (mcluskey2015comparativestructuralanalysis pages 2-3, mcluskey2015comparativestructuralanalysis pages 10-11). This fold represents the minimal structural unit conserved across all clan CD members and serves as the archetype for the entire clan (mcluskey2015comparativestructuralanalysis pages 1-2).

### 1.2 Catalytic Mechanism and Conserved Residues

The catalytic mechanism employs a strictly conserved histidine/cysteine (His/Cys) dyad located at the C-terminal ends of β-strands 3 and 4 (mcluskey2015comparativestructuralanalysis pages 10-11, mcluskey2015comparativestructuralanalysis pages 2-3). In canonical caspases, His-237 functions as a general acid/base catalyst, while Cys-285 (in the conserved QACXG motif) acts as the nucleophilic residue that forms a covalent enzyme–substrate acyl intermediate (fuentesprior2004theproteinstructures pages 9-9). A conserved glycine adjacent to the catalytic histidine is structurally invariant across all clan CD families (mcluskey2015comparativestructuralanalysis pages 10-11). Additionally, a conserved aspartate residue positioned between strands β4 and β5 contributes to catalytic architecture (mcluskey2015comparativestructuralanalysis pages 2-3).

Substrate recognition involves a tetrapeptide motif (P4–P3–P2–P1) with an absolute requirement for aspartate (Asp) at the P1 cleavage site for canonical caspases (nicholson1999caspasestructureproteolytic pages 2-5, mcluskey2015comparativestructuralanalysis pages 1-2). The P1 Asp carboxylate is anchored through hydrogen bonds with three conserved residues: Arg-179, Gln-283, and Arg-341 (nicholson1999caspasestructureproteolytic pages 2-5). Substrate specificity is further shaped by the S4 binding pocket, which differs between caspase subclasses—inflammatory caspases have shallow hydrophobic S4 pockets accommodating aromatic residues, while apoptotic caspases have more constrained pockets preferring short branched aliphatic residues (fuentesprior2004theproteinstructures pages 9-9).

### 1.3 Activation Mechanisms

Caspases display two fundamentally distinct activation mechanisms. Initiator (apical) caspases must undergo dimerization at activation platforms—the DISC for caspase-8 or the apoptosome for caspase-9—through an induced proximity mechanism (salvesen2008caspasemechanisms. pages 4-6, biboverdugo2024evolutionofcaspases pages 3-5). Executioner caspases exist as pre-formed dimers and require proteolytic cleavage of an inter-subunit linker for activation (salvesen2008caspasemechanisms. pages 4-6, nadendla2025caspasesstructuraland pages 7-8). Active caspases form tetramers composed of two large (~17–20 kDa) and two small (~10–12 kDa) subunits arranged in a head-to-tail configuration with two catalytic sites per dimer (nicholson1999caspasestructureproteolytic pages 2-5, nadendla2025caspasesstructuraland pages 7-8).

## 2. InterPro2GO Mapping Appropriateness

The PTHR10454 entry currently has **no InterPro2GO mappings**, which is the correct annotation state given the extreme functional heterogeneity of this family. The following analysis evaluates candidate GO terms that might be considered and explains why each would constitute over-annotation if applied at the family level.

| Candidate GO Term | GO ID (approximate) | GO Aspect (MF/BP/CC) | Would It Over-Annotate? (Yes/No) | Reason | Recommended Action |
|---|---|---|---|---|---|
| cysteine-type endopeptidase activity | GO:0004197 | MF | Yes | Broad PTHR10454 appears to encompass catalytically active canonical caspases, Arg-specific paracaspase/metacaspase relatives, and catalytically dead pseudo-caspase c-FLIP/CFLAR; therefore peptidase activity is not true for every matched protein (smyth2020flip(l)thepseudo‐caspase pages 1-2, smyth2020flip(l)thepseudo‐caspase pages 2-4, staal2011regulationofnfκb pages 10-11, hailfinger2014targetingbcelllymphomas pages 1-5, minina2017metacaspasesversuscaspases pages 2-3, mcluskey2015comparativestructuralanalysis pages 1-2) | REMOVE at this family level; if needed, move to catalytic child entries only |
| cysteine-type endopeptidase activity involved in apoptotic process | GO:0008635 | MF | Yes | Too narrow even for canonical caspases: inflammatory caspases function in cytokine maturation/pyroptosis, caspase-14 functions in epidermal differentiation, and MALT1 regulates NF-kB signaling rather than apoptosis; pseudo-caspases further invalidate universal mapping (nadendla2025caspasesstructuraland pages 5-6, fuentesprior2004theproteinstructures pages 2-3, biboverdugo2024evolutionofcaspases pages 5-7, staal2011regulationofnfκb pages 10-11, nadendla2025caspasesstructuraland pages 15-16) | REMOVE; map only to apoptotic catalytic child subfamilies if justified |
| aspartic-type endopeptidase activity | GO:0004190 | MF | Yes | Biochemically wrong for this family: caspases are cysteine-dependent proteases, not aspartic proteases; moreover some related family members are Arg-specific or inactive (mcluskey2015comparativestructuralanalysis pages 1-2, nicholson1999caspasestructureproteolytic pages 2-5, fuentesprior2004theproteinstructures pages 9-9, staal2011regulationofnfκb pages 10-11) | DO NOT MAP |
| proteolysis | GO:0006508 | BP | Yes | Although many active members cleave protein substrates, the family includes inactive pseudo-caspases and noncanonical signaling proteins; the term is also too generic to add much value and would still fail universality (smyth2020flip(l)thepseudo‐caspase pages 1-2, smyth2020flip(l)thepseudo‐caspase pages 2-4, staal2011regulationofnfκb pages 10-11, jaworski2016theparacaspasemalt1 pages 2-4) | KEEP UNMAPPED / KEEP_AS_NON_CORE only on narrower catalytic entries |
| apoptotic process | GO:0006915 | BP | Yes | False for inflammatory caspases, caspase-14, MALT1, and many divergent metazoan caspases with immune or differentiation roles; also leaks across taxa where specific apoptotic circuitry differs substantially (nadendla2025caspasesstructuraland pages 5-6, biboverdugo2024evolutionofcaspases pages 5-7, malireddi2025threedecadesof pages 16-17, krasovec2024intrinsicapoptosisis pages 5-6, nadendla2025caspasesstructuraland pages 15-16) | REMOVE; use only on apoptotic child groups |
| regulation of apoptotic process | GO:0042981 | BP | Yes | Some members regulate apoptosis, but others execute pyroptosis, promote NF-kB signaling, mediate epidermal differentiation, or act as pseudoenzymatic modulators; not universal across the family (smyth2020flip(l)thepseudo‐caspase pages 5-6, staal2011regulationofnfκb pages 9-10, staal2011regulationofnfκb pages 10-11, nadendla2025caspasesstructuraland pages 15-16) | REMOVE; use on specific regulatory subfamilies only |
| inflammatory response | GO:0006954 | BP | Yes | Applies mainly to inflammatory caspases and some caspase-8/PANoptosis contexts, but not broadly to executioner caspases, caspase-14, or apoptotic-only subgroups (staal2011regulationofnfκb pages 5-6, biboverdugo2024evolutionofcaspases pages 5-7, gao2024panoptosisbridgingapoptosis pages 2-4) | REMOVE; map to inflammatory caspase children only |
| pyroptosis | GO:0070269 | BP | Yes | Restricted to inflammatory caspases and some context-dependent cross-talk involving caspase-3 or caspase-8; clearly not a universal property of all PTHR10454 matches (biboverdugo2024evolutionofcaspases pages 5-7, gao2024panoptosisbridgingapoptosis pages 2-4) | REMOVE; map only to pyroptosis-driving subfamilies |
| programmed cell death | GO:0012501 | BP | Yes | Over-broad and still not universal: some family members have non-death roles in differentiation, barrier formation, immune signaling, or survival regulation; taxonomic breadth further weakens universality (nadendla2025caspasesstructuraland pages 5-6, malireddi2025threedecadesof pages 16-17, malireddi2025threedecadesof pages 4-6, nadendla2025caspasesstructuraland pages 15-16) | REMOVE |
| cytoplasm | GO:0005737 | CC | Yes | Localization is variable and context-dependent; many caspases are synthesized as cytosolic zymogens but are recruited to large signaling complexes or specialized compartments, and such a generic CC term adds little information (staal2011regulationofnfκb pages 4-5, fuentesprior2004theproteinstructures pages 2-3, nadendla2025caspasesstructuraland pages 10-11) | DO NOT MAP |
| Overall verdict for PTHR10454 | N/A | N/A | Yes | No current InterPro2GO mapping is the correct state. The family is too functionally heterogeneous for safe family-level GO transfer because it spans apoptotic, inflammatory, differentiation-associated, scaffold/paracaspase, and pseudo-caspase members with different catalytic status and substrate specificity (nadendla2025caspasesstructuraland pages 5-6, smyth2020flip(l)thepseudo‐caspase pages 1-2, staal2011regulationofnfκb pages 10-11, krasovec2024intrinsicapoptosisis pages 5-6, nadendla2025caspasesstructuraland pages 15-16) | ACCEPT current no-mapping state; only annotate more specific child entries/subfamilies |


*Table: This table evaluates plausible GO terms for the broad PTHR10454 caspase family and shows why family-level mapping would over-annotate. It is useful for justifying retention of the current no-mapping InterPro2GO state and for identifying which terms should instead be pushed down to narrower child entries.*

### 2.1 Molecular Function Terms

**Cysteine-type endopeptidase activity (GO:0004197)** would over-annotate because the family includes the catalytically dead pseudo-caspase c-FLIP/CFLAR, where the catalytic His and Cys residues are replaced by arginine (R315) and tyrosine (Y360), rendering the protein incapable of protease activity (smyth2020flip(l)thepseudo‐caspase pages 2-4). Furthermore, paracaspases such as MALT1 cleave after arginine residues rather than aspartate, representing a fundamentally different substrate specificity (staal2011regulationofnfκb pages 10-11, solsona2022theparacaspasemalt1 pages 2-4).

**Cysteine-type endopeptidase activity involved in apoptotic process (GO:0008635)** is too narrow even for catalytically active canonical caspases, as inflammatory caspases primarily function in cytokine maturation and pyroptosis rather than apoptosis (fuentesprior2004theproteinstructures pages 2-3, biboverdugo2024evolutionofcaspases pages 5-7), caspase-14 functions exclusively in epidermal differentiation (nadendla2025caspasesstructuraland pages 15-16), and caspase-8 has been shown to function in both apoptotic and non-apoptotic inflammatory pathways (nadendla2025caspasesstructuraland pages 5-6, staal2011regulationofnfκb pages 9-10).

### 2.2 Biological Process Terms

**Apoptotic process (GO:0006915)** would be false for inflammatory caspases, caspase-14, MALT1/paracaspases, and c-FLIP (nadendla2025caspasesstructuraland pages 5-6, staal2011regulationofnfκb pages 10-11, nadendla2025caspasesstructuraland pages 15-16). Similarly, **pyroptosis (GO:0070269)** applies only to inflammatory caspases and some caspase-8/caspase-3 cross-talk contexts (biboverdugo2024evolutionofcaspases pages 5-7, gao2024panoptosisbridgingapoptosis pages 2-4). Even **programmed cell death (GO:0012501)**, though broader, would be incorrect for members whose primary roles are in differentiation, immune signaling, or regulatory scaffolding (malireddi2025threedecadesof pages 16-17, malireddi2025threedecadesof pages 4-6, nadendla2025caspasesstructuraland pages 15-16).

### 2.3 Verdict on Current State

The absence of InterPro2GO terms on PTHR10454 is **appropriate** and should be maintained. Any molecular function, biological process, or cellular component GO term applied at this family level would systematically over-annotate a significant fraction of the 8,115 matched proteins.

## 3. Functional Divergence Across the Family

The PTHR10454 family encompasses extraordinary functional diversity, with members displaying divergent—and in some cases, opposing—biological activities.

| Subfamily/Member | Pro-domain Type | Catalytic Activity (Yes/No) | Substrate Specificity (P1 residue) | Primary Biological Function(s) | Taxonomic Distribution | Compatible with generic “caspase” GO terms? |
|---|---|---:|---|---|---|---|
| Apoptotic initiator caspases (caspase-2, -8, -9, -10) | Long pro-domains; CARD (caspase-2, -9) or DED (caspase-8, -10) | Yes | Asp | Initiate apoptotic signaling from activation platforms; caspase-8 also regulates NF-κB signaling, T-cell activation, inflammasome/PANoptosis crosstalk | Metazoa; caspase-2 broadly bilaterian, caspase-9 deuterostome-specific, caspase-8/-10 mainly vertebrate/deuterostome lineages | **Partly**: compatible only with broad catalytic terms for active Asp-specific caspases, but **not** with apoptosis-only GO terms across the whole family (staal2011regulationofnfκb pages 4-5, fuentesprior2004theproteinstructures pages 2-3, biboverdugo2024evolutionofcaspases pages 5-7, staal2011regulationofnfκb pages 9-10, krasovec2024intrinsicapoptosisis pages 5-6, krasovec2024intrinsicapoptosisis pages 9-10, nadendla2025caspasesstructuraland pages 5-6, nadendla2025caspasesstructuraland pages 10-11) |
| Apoptotic executioner caspases (caspase-3, -6, -7) | Short/no prodomain | Yes | Asp | Execute apoptosis by cleavage of many cellular substrates; additional non-apoptotic roles include pyroptosis cross-talk (caspase-3), axon pruning/PANoptosome functions (caspase-6), membrane repair and differentiation/osteogenesis roles (caspase-7) | Metazoa; diversified animal caspase clades | **Partly**: catalytic caspase terms may fit active members, but apoptosis process terms are too narrow for all functions even within this subgroup (biboverdugo2024evolutionofcaspases pages 3-5, biboverdugo2024evolutionofcaspases pages 5-7, malireddi2025threedecadesof pages 16-17, malireddi2025threedecadesof pages 4-6, gao2024panoptosisbridgingapoptosis pages 2-4) |
| Inflammatory caspases (caspase-1, -4, -5, -11) | Long pro-domains; CARD | Yes | Asp | Cytokine maturation (IL-1β, IL-18), inflammasome signaling, gasdermin cleavage, pyroptosis, innate immune defense | Mainly vertebrates; inflammatory caspases are vertebrate-restricted | **No** for generic apoptotic GO terms; only some inflammatory/pyroptotic catalytic terms would fit this subgroup, not the whole PTHR10454 family (fuentesprior2004theproteinstructures pages 2-3, staal2011regulationofnfκb pages 5-6, biboverdugo2024evolutionofcaspases pages 5-7, malireddi2025threedecadesof pages 3-4, krasovec2024intrinsicapoptosisis pages 5-6) |
| Caspase-14 | Short/no prodomain; atypical | Yes | Asp (caspase-family catalytic architecture) | Epidermal differentiation, stratum corneum formation, UVB protection, skin barrier and water-loss prevention; non-apoptotic | Vertebrates, especially terrestrial vertebrate epidermis | **No** for generic apoptosis or inflammatory GO terms; only highly specific epidermis/keratinization-related terms would be appropriate (nadendla2025caspasesstructuraland pages 5-6, fuentesprior2004theproteinstructures pages 3-4, nadendla2025caspasesstructuraland pages 15-16) |
| MALT1 paracaspase | N-terminal death domain + Ig-like domains + caspase-like domain | Yes | **Arg** (not Asp) | Scaffold + protease in CBM signaling; NF-κB/AP-1 activation, lymphocyte activation, immune homeostasis, mucosal healing; not a cell-death execution caspase | Animals; paracaspase lineage broader than canonical caspases in evolution, but MALT1 is metazoan immune signaling protein | **No**: not an Asp-specific caspase, not apoptotic by default; generic caspase GO terms would misannotate substrate specificity and biology (staal2011regulationofnfκb pages 10-11, hailfinger2014targetingbcelllymphomas pages 1-5, jaworski2016theparacaspasemalt1 pages 4-6, solsona2022theparacaspasemalt1 pages 2-4, jaworski2016theparacaspasemalt1 pages 2-4, yu2015malt1proteaseactivity pages 20-20) |
| c-FLIP/CFLAR pseudo-caspase | Two DEDs + caspase-like pseudo-domain | **No** | None as independent protease; pseudo-caspase domain is catalytically dead | Regulates caspase-8 complexes, apoptosis, necroptosis, autophagy, inflammasome signaling; scaffold/modulator rather than protease | Vertebrates | **No**: any peptidase activity term would be false; apoptosis terms are also not universally appropriate because it is primarily a regulator and inhibitor/modulator (smyth2020flip(l)thepseudo‐caspase pages 1-2, smyth2020flip(l)thepseudo‐caspase pages 5-6, smyth2020flip(l)thepseudo‐caspase pages 2-4, zhang2025biologicalfunctionsand pages 1-2, smyth2020flip(l)thepseudo‐caspase pages 6-8) |
| Metacaspases | Variable; Type I/II forms with diverse N-terminal regions, not canonical CARD/DED caspase pro-domains | Yes | **Arg/Lys** (not Asp) | Developmental and stress-related proteolysis, programmed cell death-like processes, diverse signaling roles; structurally related but biochemically distinct from caspases | Broadest distribution: plants, fungi, protozoa, bacteria, archaea; notably absent from animals | **No**: not true caspases in substrate specificity or taxonomic context; generic “caspase” GO terms would systematically over-annotate (mcluskey2015comparativestructuralanalysis pages 7-8, minina2017metacaspasesversuscaspases pages 2-3, mcluskey2015comparativestructuralanalysis pages 1-2, minina2017metacaspasesversuscaspases pages 1-2, minina2017metacaspasesversuscaspases pages 5-7, biboverdugo2024evolutionofcaspases pages 1-3, minina2017metacaspasesversuscaspases pages 3-5) |


*Table: This table summarizes major functional and biochemical differences among caspase-related subfamilies relevant to review of InterPro entry PTHR10454. It highlights why generic caspase GO annotation would be unsafe across a broad family that includes active Asp-specific caspases, Arg-specific paracaspases/metacaspases, and catalytically dead pseudo-caspases.*

### 3.1 Canonical Caspase Subgroups

Historically, caspases were classified into three functional groups: **inflammatory caspases** (caspase-1, -4, -5, -11) that process pro-inflammatory cytokines IL-1β and IL-18; **apoptotic initiator caspases** (caspase-2, -8, -9, -10) that initiate apoptotic signaling cascades; and **apoptotic executioner caspases** (caspase-3, -6, -7) that carry out the proteolytic dismantling of the cell (fuentesprior2004theproteinstructures pages 2-3, nadendla2025caspasesstructuraland pages 5-6). However, extensive recent evidence demonstrates that these boundaries are far more fluid than originally thought. Caspase-8 functions not only as an apoptotic initiator but also as an upstream regulator of inflammasome-dependent inflammatory responses and can process pro-inflammatory cytokines including IL-1β and IL-18 (nadendla2025caspasesstructuraland pages 5-6, malireddi2025threedecadesof pages 9-11). Caspase-3 can both activate and suppress pyroptosis through differential cleavage of gasdermin D at different sites (gao2024panoptosisbridgingapoptosis pages 2-4). Caspase-6 promotes ZBP1-PANoptosome formation and activates the NLRP3 inflammasome independent of its enzymatic activity (malireddi2025threedecadesof pages 4-6).

A modern reclassification based on pro-domain architecture groups caspases into **CARD-containing** (caspase-1, -2, -4, -5, -9, -11, -12), **DED-containing** (caspase-8, -10), and **short/no pro-domain** (caspase-3, -6, -7, -14) categories, better reflecting the multi-dimensional roles of these proteases (nadendla2025caspasesstructuraland pages 5-6, nadendla2025caspasesstructuraland pages 10-11).

### 3.2 Caspase-14: Non-Apoptotic Differentiation Function

Caspase-14 represents a striking case of neo-functionalization. It is induced and processed during normal epidermal differentiation without triggering apoptosis, playing a protective role in skin barrier function by defending against UVB photodamage and preventing water loss (nadendla2025caspasesstructuraland pages 15-16). This function is entirely distinct from any cell death pathway and is specific to the stratum corneum of terrestrial vertebrate skin (nadendla2025caspasesstructuraland pages 5-6, fuentesprior2004theproteinstructures pages 3-4).

### 3.3 c-FLIP/CFLAR: The Pseudo-Caspase

c-FLIP (encoded by the CFLAR gene) represents the only identified human pseudo-caspase—a catalytically dead paralog of caspase-8 and caspase-10 (smyth2020flip(l)thepseudo‐caspase pages 1-2). Its caspase-like domain has substituted the catalytic His/Cys dyad with arginine and tyrosine residues, abolishing protease activity (smyth2020flip(l)thepseudo‐caspase pages 2-4). Despite lacking catalytic function, c-FLIP(L) modulates apoptosis, necroptosis, autophagy, and inflammasome signaling through regulatory scaffold interactions with procaspase-8 (smyth2020flip(l)thepseudo‐caspase pages 5-6, zhang2025biologicalfunctionsand pages 1-2). At high FLIP(L):procaspase-8 ratios, it inhibits apoptosis; at low ratios, it permits apoptotic signaling (smyth2020flip(l)thepseudo‐caspase pages 5-6). This pseudo-enzyme member would be falsely annotated by any peptidase activity GO term.

### 3.4 MALT1 Paracaspase: Arg-Specific Immune Signaling Protease

MALT1 is a paracaspase with a caspase-like catalytic domain containing conserved Cys (C464) and His (H415) residues, but it fundamentally differs from canonical caspases in substrate specificity, cleaving after arginine residues rather than aspartate (staal2011regulationofnfκb pages 10-11, solsona2022theparacaspasemalt1 pages 2-4, hailfinger2014targetingbcelllymphomas pages 5-8). MALT1 functions through dual scaffold and protease mechanisms within the CARMA-BCL10-MALT1 (CBM) signalosome to activate NF-κB and AP-1 signaling in lymphocytes (jaworski2016theparacaspasemalt1 pages 2-4, hailfinger2014targetingbcelllymphomas pages 1-5). Its substrates include NF-κB regulators A20 and CYLD, mRNA stability factors Regnase-1 and Roquin, and the transcription factor RelB (solsona2022theparacaspasemalt1 pages 2-4, hailfinger2014targetingbcelllymphomas pages 11-15). MALT1 does not induce cell death like apoptotic caspases—instead, it promotes lymphocyte activation, survival, and proliferation (staal2011regulationofnfκb pages 10-11).

### 3.5 Metacaspases: Plant/Fungal/Prokaryotic Relatives

Although metacaspases share the clan CD fold with caspases, they differ fundamentally in substrate specificity (cleaving after Arg/Lys rather than Asp), activation mechanisms, and taxonomic distribution (mcluskey2015comparativestructuralanalysis pages 7-8, minina2017metacaspasesversuscaspases pages 2-3). They are present in plants, fungi, protozoa, bacteria, and archaea but notably absent from animals (minina2017metacaspasesversuscaspases pages 2-3, mcluskey2015comparativestructuralanalysis pages 1-2). Structural analysis suggests metacaspases are sufficiently divergent from caspases and paracaspases to warrant classification as a separate family within clan CD (mcluskey2015comparativestructuralanalysis pages 7-8). If PTHR10454 encompasses metacaspase-like sequences (as its scale of 5,813 taxa suggests), any caspase-specific GO term would be deeply inappropriate for these members.

### 3.6 Non-Apoptotic Functions of Canonical Caspases

Even within "apoptotic" caspases, extensive non-death functions have been documented: caspase-8 is essential for T cell activation and IL-2-dependent proliferation through TCR-stimulated NF-κB signaling (staal2011regulationofnfκb pages 9-10, staal2011regulationofnfκb pages 4-5); caspase-1 activates NF-κB through its CARD domain independently of its catalytic activity (staal2011regulationofnfκb pages 5-6); caspase-2 protects against oxidative damage, prevents polyploidization, and performs non-canonical aspartate-independent substrate proteolysis (malireddi2025threedecadesof pages 3-4); caspase-6 functions in axon pruning during development (malireddi2025threedecadesof pages 4-6); and caspase-7 participates in differentiation of cells forming dental hard tissues and in membrane repair (malireddi2025threedecadesof pages 16-17).

## 4. Taxonomic Scope

### 4.1 Distribution of Canonical Caspases

Canonical caspases (subfamily C14A) are restricted to **Metazoa** (animals) and some viruses (mcluskey2015comparativestructuralanalysis pages 1-2, minina2017metacaspasesversuscaspases pages 2-3). Within animals, caspase diversity varies substantially: vertebrates possess up to 14 caspases (with one inactive, i.e., CFLAR/c-FLIP), arthropods have ~7 (Drosophila), and nematodes have ~4 (C. elegans) (koonin2002originandevolution pages 3-4). Non-bilaterian animals (cnidarians, ctenophores, placozoans) possess divergent caspase sequences positioned at the base of caspase phylogenetic clades (krasovec2024intrinsicapoptosisis pages 3-4, krasovec2024intrinsicapoptosisis pages 5-6).

### 4.2 Differential Distribution of Caspase Subtypes

Importantly, different caspase subtypes have markedly different taxonomic distributions. Caspase-2 is ancestral to bilaterians (present across deuterostomes, ecdysozoans, and lophotrochozoans), while caspase-9 is restricted to deuterostomes only (krasovec2024intrinsicapoptosisis pages 5-6, krasovec2024intrinsicapoptosisis pages 9-10). Inflammatory caspases are limited to vertebrates (krasovec2024intrinsicapoptosisis pages 5-6). The protostome-specific caspase-Y group is found in mollusks and annelids (krasovec2024intrinsicapoptosisis pages 2-3). This means that any GO term referring to a specific apoptotic pathway (e.g., intrinsic apoptosis via caspase-9) would systematically leak into taxa where that specific pathway component is absent.

### 4.3 Broader C14 Family Distribution

If PTHR10454 encompasses the broader C14 family—including metacaspases and paracaspases—its 5,813 taxa would span virtually all domains of life. Paracaspases are found in bacteria, archaea, slime molds, and metazoans (minina2017metacaspasesversuscaspases pages 2-3, mcluskey2015comparativestructuralanalysis pages 3-4). Metacaspases have the broadest distribution, occurring throughout bacteria, archaea, protozoa, fungi, and plants, while being notably absent from animals (minina2017metacaspasesversuscaspases pages 2-3, mcluskey2015comparativestructuralanalysis pages 1-2). This makes any animal-specific process term (apoptosis, pyroptosis, immune response) inappropriate for a large fraction of matched proteins.

## 5. Recent Developments (2024–2025)

### 5.1 PANoptosis and the PANoptosome

A major conceptual advance in caspase biology is the PANoptosis framework, which describes an innate immune cell death pathway integrating apoptosis, pyroptosis, and necroptosis through multiprotein PANoptosome complexes containing innate immune sensors, caspase-1/inflammasomes, caspase-8, and RIPKs (malireddi2025threedecadesof pages 9-11, malireddi2025threedecadesof pages 11-13). Multiple PANoptosome types have been identified, including ZBP1-, AIM2-, RIPK1-, and NLRP12-PANoptosomes (gao2024panoptosisbridgingapoptosis pages 2-4). This demonstrates that caspases operate through redundant and interconnected networks rather than linear cascades (malireddi2025threedecadesof pages 11-13), further undermining attempts to assign single pathway GO terms to individual caspases.

### 5.2 Reclassification of Caspases

Recent authoritative reviews (2025) propose reclassifying caspases based on pro-domain architecture rather than function alone, recognizing that traditional categories (apoptotic vs. inflammatory) are inadequate (nadendla2025caspasesstructuraland pages 5-6). This reflects the now-established finding that "apoptotic" caspases (e.g., caspase-3, -6, -7, -8) can also drive lytic inflammatory cell death downstream of innate immune sensing (nadendla2025caspasesstructuraland pages 5-6).

### 5.3 Non-Canonical Functions

Caspase-2 has been found to perform non-canonical, aspartate-independent substrate proteolysis at ubstressomes to remove neurotoxic damaged proteins (malireddi2025threedecadesof pages 3-4). Caspase-2 also protects against ferroptosis by interacting with heat shock proteins to limit GPX4 degradation (malireddi2025threedecadesof pages 4-6). These findings further expand the functional repertoire beyond classical caspase activities.

## 6. Over-Annotation Verdict and Recommendations

### 6.1 Summary Assessment

The PTHR10454 (CASPASE) entry currently has **no InterPro2GO mappings**, and this is the **correct and appropriate state**. The family is far too functionally heterogeneous for any safe family-level GO term transfer, based on the following evidence:

1. **Catalytic status is not universal**: The family includes catalytically dead pseudo-caspases (c-FLIP/CFLAR) alongside active proteases (smyth2020flip(l)thepseudo‐caspase pages 1-2, smyth2020flip(l)thepseudo‐caspase pages 2-4).

2. **Substrate specificity diverges fundamentally**: Canonical caspases cleave after Asp; paracaspases (MALT1) and metacaspases cleave after Arg/Lys (mcluskey2015comparativestructuralanalysis pages 7-8, staal2011regulationofnfκb pages 10-11).

3. **Biological processes are mutually exclusive across subfamilies**: Apoptosis (executioners), pyroptosis (inflammatory caspases), epidermal differentiation (caspase-14), NF-κB/immune signaling (MALT1), and regulatory scaffolding (c-FLIP) represent incompatible GO annotations (nadendla2025caspasesstructuraland pages 5-6, staal2011regulationofnfκb pages 10-11, nadendla2025caspasesstructuraland pages 15-16).

4. **Taxonomic range precludes pathway-specific terms**: With representation across potentially all domains of life (if metacaspases are included), animal-specific or vertebrate-specific pathway terms would leak inappropriately (minina2017metacaspasesversuscaspases pages 2-3, krasovec2024intrinsicapoptosisis pages 5-6).

### 6.2 Recommended GO Action Pattern

| Recommendation | Details |
|---|---|
| **Overall verdict** | **ACCEPT** the current no-mapping state |
| **Family-level GO terms** | Do NOT add any GO terms to PTHR10454 |
| **Subfamily-level recommendation** | Push GO annotations to narrower child entries/subfamilies where functional homogeneity can be established |
| **InterPro recommendation** | Consider whether PTHR10454 subfamilies are sufficiently delineated to receive subfamily-specific GO mappings (e.g., executioner caspase subfamily → GO:0006915 apoptotic process + GO:0004197 cysteine-type endopeptidase activity; inflammatory caspase subfamily → GO:0006954 inflammatory response + GO:0070269 pyroptosis) |
| **Specific caution** | Ensure no child entry that matches c-FLIP/CFLAR receives peptidase activity terms; ensure no entry matching MALT1 receives Asp-specific cleavage terms |

In summary, PTHR10454 represents a textbook case where family-level GO annotation would systematically over-annotate due to profound functional divergence, including neo-functionalization (caspase-14), loss of catalytic activity (c-FLIP), altered substrate specificity (MALT1, metacaspases), and pathway diversification (apoptosis vs. pyroptosis vs. immune signaling vs. differentiation). The current absence of InterPro2GO mappings is scientifically sound and should be maintained.

References

1. (mcluskey2015comparativestructuralanalysis pages 2-3): Karen McLuskey and Jeremy C. Mottram. Comparative structural analysis of the caspase family with other clan cd cysteine peptidases. Biochemical Journal, 466:219-232, Feb 2015. URL: https://doi.org/10.1042/bj20141324, doi:10.1042/bj20141324. This article has 101 citations and is from a domain leading peer-reviewed journal.

2. (mcluskey2015comparativestructuralanalysis pages 10-11): Karen McLuskey and Jeremy C. Mottram. Comparative structural analysis of the caspase family with other clan cd cysteine peptidases. Biochemical Journal, 466:219-232, Feb 2015. URL: https://doi.org/10.1042/bj20141324, doi:10.1042/bj20141324. This article has 101 citations and is from a domain leading peer-reviewed journal.

3. (mcluskey2015comparativestructuralanalysis pages 1-2): Karen McLuskey and Jeremy C. Mottram. Comparative structural analysis of the caspase family with other clan cd cysteine peptidases. Biochemical Journal, 466:219-232, Feb 2015. URL: https://doi.org/10.1042/bj20141324, doi:10.1042/bj20141324. This article has 101 citations and is from a domain leading peer-reviewed journal.

4. (fuentesprior2004theproteinstructures pages 9-9): Pablo FUENTES-PRIOR and Guy S. SALVESEN. The protein structures that shape caspase activity, specificity, activation and inhibition. The Biochemical journal, 384 Pt 2:201-32, Dec 2004. URL: https://doi.org/10.1042/bj20041142, doi:10.1042/bj20041142. This article has 1266 citations.

5. (nicholson1999caspasestructureproteolytic pages 2-5): DW Nicholson. Caspase structure, proteolytic substrates, and function during apoptotic cell death. Cell Death and Differentiation, 6:1028-1042, Nov 1999. URL: https://doi.org/10.1038/sj.cdd.4400598, doi:10.1038/sj.cdd.4400598. This article has 2235 citations and is from a domain leading peer-reviewed journal.

6. (salvesen2008caspasemechanisms. pages 4-6): Guy S. Salvesen and Stefan J. Riedl. Caspase mechanisms. Advances in experimental medicine and biology, 615:13-23, Jan 2008. URL: https://doi.org/10.1007/978-1-4020-6554-5\_2, doi:10.1007/978-1-4020-6554-5\_2. This article has 353 citations and is from a peer-reviewed journal.

7. (biboverdugo2024evolutionofcaspases pages 3-5): Betsaida Bibo-Verdugo and Guy Salvesen. Evolution of caspases and the invention of pyroptosis. International Journal of Molecular Sciences, 25:5270, May 2024. URL: https://doi.org/10.3390/ijms25105270, doi:10.3390/ijms25105270. This article has 14 citations.

8. (nadendla2025caspasesstructuraland pages 7-8): Eswar Kumar Nadendla, Rebecca E. Tweedell, Gary Kasof, and Thirumala-Devi Kanneganti. Caspases: structural and molecular mechanisms and functions in cell death, innate immunity, and disease. Cell Discovery, May 2025. URL: https://doi.org/10.1038/s41421-025-00791-3, doi:10.1038/s41421-025-00791-3. This article has 67 citations and is from a peer-reviewed journal.

9. (smyth2020flip(l)thepseudo‐caspase pages 1-2): Peter Smyth, Tamas Sessler, Christopher J. Scott, and Daniel B. Longley. Flip(l): the pseudo‐caspase. The FEBS Journal, 287:4246-4260, Mar 2020. URL: https://doi.org/10.1111/febs.15260, doi:10.1111/febs.15260. This article has 58 citations.

10. (smyth2020flip(l)thepseudo‐caspase pages 2-4): Peter Smyth, Tamas Sessler, Christopher J. Scott, and Daniel B. Longley. Flip(l): the pseudo‐caspase. The FEBS Journal, 287:4246-4260, Mar 2020. URL: https://doi.org/10.1111/febs.15260, doi:10.1111/febs.15260. This article has 58 citations.

11. (staal2011regulationofnfκb pages 10-11): Jens Staal, Tine Bekaert, and Rudi Beyaert. Regulation of nf-κb signaling by caspases and malt1 paracaspase. Cell Research, 21:40-54, Nov 2011. URL: https://doi.org/10.1038/cr.2010.168, doi:10.1038/cr.2010.168. This article has 115 citations and is from a domain leading peer-reviewed journal.

12. (hailfinger2014targetingbcelllymphomas pages 1-5): Stephan Hailfinger, Georg Lenz, and Margot Thome. Targeting b-cell lymphomas with inhibitors of the malt1 paracaspase. Current opinion in chemical biology, 23:47-55, Dec 2014. URL: https://doi.org/10.1016/j.cbpa.2014.09.025, doi:10.1016/j.cbpa.2014.09.025. This article has 23 citations and is from a peer-reviewed journal.

13. (minina2017metacaspasesversuscaspases pages 2-3): E. Minina, Núria S Coll, Hannele Tuominen, and P. Bozhkov. Metacaspases versus caspases in development and cell fate regulation. Cell Death and Differentiation, 24:1314-1325, Feb 2017. URL: https://doi.org/10.1038/cdd.2017.18, doi:10.1038/cdd.2017.18. This article has 112 citations and is from a domain leading peer-reviewed journal.

14. (nadendla2025caspasesstructuraland pages 5-6): Eswar Kumar Nadendla, Rebecca E. Tweedell, Gary Kasof, and Thirumala-Devi Kanneganti. Caspases: structural and molecular mechanisms and functions in cell death, innate immunity, and disease. Cell Discovery, May 2025. URL: https://doi.org/10.1038/s41421-025-00791-3, doi:10.1038/s41421-025-00791-3. This article has 67 citations and is from a peer-reviewed journal.

15. (fuentesprior2004theproteinstructures pages 2-3): Pablo FUENTES-PRIOR and Guy S. SALVESEN. The protein structures that shape caspase activity, specificity, activation and inhibition. The Biochemical journal, 384 Pt 2:201-32, Dec 2004. URL: https://doi.org/10.1042/bj20041142, doi:10.1042/bj20041142. This article has 1266 citations.

16. (biboverdugo2024evolutionofcaspases pages 5-7): Betsaida Bibo-Verdugo and Guy Salvesen. Evolution of caspases and the invention of pyroptosis. International Journal of Molecular Sciences, 25:5270, May 2024. URL: https://doi.org/10.3390/ijms25105270, doi:10.3390/ijms25105270. This article has 14 citations.

17. (nadendla2025caspasesstructuraland pages 15-16): Eswar Kumar Nadendla, Rebecca E. Tweedell, Gary Kasof, and Thirumala-Devi Kanneganti. Caspases: structural and molecular mechanisms and functions in cell death, innate immunity, and disease. Cell Discovery, May 2025. URL: https://doi.org/10.1038/s41421-025-00791-3, doi:10.1038/s41421-025-00791-3. This article has 67 citations and is from a peer-reviewed journal.

18. (jaworski2016theparacaspasemalt1 pages 2-4): Maike Jaworski and Margot Thome. The paracaspase malt1: biological function and potential for therapeutic inhibition. Cellular and Molecular Life Sciences: CMLS, 73:459-473, Oct 2016. URL: https://doi.org/10.1007/s00018-015-2059-z, doi:10.1007/s00018-015-2059-z. This article has 132 citations.

19. (malireddi2025threedecadesof pages 16-17): RKS Malireddi and TD Kanneganti. Three decades of caspases and ripks in life and death. Human molecular genetics, Jul 2025. URL: https://doi.org/10.1093/hmg/ddaf106, doi:10.1093/hmg/ddaf106. This article has 4 citations and is from a domain leading peer-reviewed journal.

20. (krasovec2024intrinsicapoptosisis pages 5-6): Gabriel Krasovec, Helen R Horkan, Éric Quéinnec, and Jean-Philippe Chambon. Intrinsic apoptosis is evolutionarily divergent among metazoans. Evolution Letters, 8:267-282, Nov 2024. URL: https://doi.org/10.1093/evlett/qrad057, doi:10.1093/evlett/qrad057. This article has 21 citations and is from a domain leading peer-reviewed journal.

21. (smyth2020flip(l)thepseudo‐caspase pages 5-6): Peter Smyth, Tamas Sessler, Christopher J. Scott, and Daniel B. Longley. Flip(l): the pseudo‐caspase. The FEBS Journal, 287:4246-4260, Mar 2020. URL: https://doi.org/10.1111/febs.15260, doi:10.1111/febs.15260. This article has 58 citations.

22. (staal2011regulationofnfκb pages 9-10): Jens Staal, Tine Bekaert, and Rudi Beyaert. Regulation of nf-κb signaling by caspases and malt1 paracaspase. Cell Research, 21:40-54, Nov 2011. URL: https://doi.org/10.1038/cr.2010.168, doi:10.1038/cr.2010.168. This article has 115 citations and is from a domain leading peer-reviewed journal.

23. (staal2011regulationofnfκb pages 5-6): Jens Staal, Tine Bekaert, and Rudi Beyaert. Regulation of nf-κb signaling by caspases and malt1 paracaspase. Cell Research, 21:40-54, Nov 2011. URL: https://doi.org/10.1038/cr.2010.168, doi:10.1038/cr.2010.168. This article has 115 citations and is from a domain leading peer-reviewed journal.

24. (gao2024panoptosisbridgingapoptosis pages 2-4): Jie Gao, Anying Xiong, Jiliu Liu, Xiaolan Li, Junyi Wang, Lei Zhang, Yao Liu, Ying Xiong, Guoping Li, and Xiang He. Panoptosis: bridging apoptosis, pyroptosis, and necroptosis in cancer progression and treatment. Cancer Gene Therapy, 31:970-983, Mar 2024. URL: https://doi.org/10.1038/s41417-024-00765-9, doi:10.1038/s41417-024-00765-9. This article has 150 citations and is from a peer-reviewed journal.

25. (malireddi2025threedecadesof pages 4-6): RKS Malireddi and TD Kanneganti. Three decades of caspases and ripks in life and death. Human molecular genetics, Jul 2025. URL: https://doi.org/10.1093/hmg/ddaf106, doi:10.1093/hmg/ddaf106. This article has 4 citations and is from a domain leading peer-reviewed journal.

26. (staal2011regulationofnfκb pages 4-5): Jens Staal, Tine Bekaert, and Rudi Beyaert. Regulation of nf-κb signaling by caspases and malt1 paracaspase. Cell Research, 21:40-54, Nov 2011. URL: https://doi.org/10.1038/cr.2010.168, doi:10.1038/cr.2010.168. This article has 115 citations and is from a domain leading peer-reviewed journal.

27. (nadendla2025caspasesstructuraland pages 10-11): Eswar Kumar Nadendla, Rebecca E. Tweedell, Gary Kasof, and Thirumala-Devi Kanneganti. Caspases: structural and molecular mechanisms and functions in cell death, innate immunity, and disease. Cell Discovery, May 2025. URL: https://doi.org/10.1038/s41421-025-00791-3, doi:10.1038/s41421-025-00791-3. This article has 67 citations and is from a peer-reviewed journal.

28. (solsona2022theparacaspasemalt1 pages 2-4): Beatriz Gomez Solsona, Anja Schmitt, Klaus Schulze-Osthoff, and Stephan Hailfinger. The paracaspase malt1 in cancer. Biomedicines, 10:344, Feb 2022. URL: https://doi.org/10.3390/biomedicines10020344, doi:10.3390/biomedicines10020344. This article has 34 citations.

29. (krasovec2024intrinsicapoptosisis pages 9-10): Gabriel Krasovec, Helen R Horkan, Éric Quéinnec, and Jean-Philippe Chambon. Intrinsic apoptosis is evolutionarily divergent among metazoans. Evolution Letters, 8:267-282, Nov 2024. URL: https://doi.org/10.1093/evlett/qrad057, doi:10.1093/evlett/qrad057. This article has 21 citations and is from a domain leading peer-reviewed journal.

30. (malireddi2025threedecadesof pages 3-4): RKS Malireddi and TD Kanneganti. Three decades of caspases and ripks in life and death. Human molecular genetics, Jul 2025. URL: https://doi.org/10.1093/hmg/ddaf106, doi:10.1093/hmg/ddaf106. This article has 4 citations and is from a domain leading peer-reviewed journal.

31. (fuentesprior2004theproteinstructures pages 3-4): Pablo FUENTES-PRIOR and Guy S. SALVESEN. The protein structures that shape caspase activity, specificity, activation and inhibition. The Biochemical journal, 384 Pt 2:201-32, Dec 2004. URL: https://doi.org/10.1042/bj20041142, doi:10.1042/bj20041142. This article has 1266 citations.

32. (jaworski2016theparacaspasemalt1 pages 4-6): Maike Jaworski and Margot Thome. The paracaspase malt1: biological function and potential for therapeutic inhibition. Cellular and Molecular Life Sciences: CMLS, 73:459-473, Oct 2016. URL: https://doi.org/10.1007/s00018-015-2059-z, doi:10.1007/s00018-015-2059-z. This article has 132 citations.

33. (yu2015malt1proteaseactivity pages 20-20): Jong W. Yu, Sandy Hoffman, Allison M. Beal, Angela Dykon, Michael A. Ringenberg, Anna C. Hughes, Lauren Dare, Amber D. Anderson, Joshua Finger, Viera Kasparcova, David Rickard, Scott B. Berger, Joshi Ramanjulu, John G. Emery, Peter J. Gough, John Bertin, and Kevin P. Foley. Malt1 protease activity is required for innate and adaptive immune responses. PLoS ONE, 10:e0127083, May 2015. URL: https://doi.org/10.1371/journal.pone.0127083, doi:10.1371/journal.pone.0127083. This article has 106 citations and is from a peer-reviewed journal.

34. (zhang2025biologicalfunctionsand pages 1-2): Haiyang Zhang, Xin Li, and Liangkang Lin. Biological functions and clinical implications of cflar: from cell death mechanisms to therapeutic targeting in immune regulation. Journal of Inflammation Research, 18:4911-4928, Apr 2025. URL: https://doi.org/10.2147/jir.s519885, doi:10.2147/jir.s519885. This article has 12 citations and is from a peer-reviewed journal.

35. (smyth2020flip(l)thepseudo‐caspase pages 6-8): Peter Smyth, Tamas Sessler, Christopher J. Scott, and Daniel B. Longley. Flip(l): the pseudo‐caspase. The FEBS Journal, 287:4246-4260, Mar 2020. URL: https://doi.org/10.1111/febs.15260, doi:10.1111/febs.15260. This article has 58 citations.

36. (mcluskey2015comparativestructuralanalysis pages 7-8): Karen McLuskey and Jeremy C. Mottram. Comparative structural analysis of the caspase family with other clan cd cysteine peptidases. Biochemical Journal, 466:219-232, Feb 2015. URL: https://doi.org/10.1042/bj20141324, doi:10.1042/bj20141324. This article has 101 citations and is from a domain leading peer-reviewed journal.

37. (minina2017metacaspasesversuscaspases pages 1-2): E. Minina, Núria S Coll, Hannele Tuominen, and P. Bozhkov. Metacaspases versus caspases in development and cell fate regulation. Cell Death and Differentiation, 24:1314-1325, Feb 2017. URL: https://doi.org/10.1038/cdd.2017.18, doi:10.1038/cdd.2017.18. This article has 112 citations and is from a domain leading peer-reviewed journal.

38. (minina2017metacaspasesversuscaspases pages 5-7): E. Minina, Núria S Coll, Hannele Tuominen, and P. Bozhkov. Metacaspases versus caspases in development and cell fate regulation. Cell Death and Differentiation, 24:1314-1325, Feb 2017. URL: https://doi.org/10.1038/cdd.2017.18, doi:10.1038/cdd.2017.18. This article has 112 citations and is from a domain leading peer-reviewed journal.

39. (biboverdugo2024evolutionofcaspases pages 1-3): Betsaida Bibo-Verdugo and Guy Salvesen. Evolution of caspases and the invention of pyroptosis. International Journal of Molecular Sciences, 25:5270, May 2024. URL: https://doi.org/10.3390/ijms25105270, doi:10.3390/ijms25105270. This article has 14 citations.

40. (minina2017metacaspasesversuscaspases pages 3-5): E. Minina, Núria S Coll, Hannele Tuominen, and P. Bozhkov. Metacaspases versus caspases in development and cell fate regulation. Cell Death and Differentiation, 24:1314-1325, Feb 2017. URL: https://doi.org/10.1038/cdd.2017.18, doi:10.1038/cdd.2017.18. This article has 112 citations and is from a domain leading peer-reviewed journal.

41. (malireddi2025threedecadesof pages 9-11): RKS Malireddi and TD Kanneganti. Three decades of caspases and ripks in life and death. Human molecular genetics, Jul 2025. URL: https://doi.org/10.1093/hmg/ddaf106, doi:10.1093/hmg/ddaf106. This article has 4 citations and is from a domain leading peer-reviewed journal.

42. (hailfinger2014targetingbcelllymphomas pages 5-8): Stephan Hailfinger, Georg Lenz, and Margot Thome. Targeting b-cell lymphomas with inhibitors of the malt1 paracaspase. Current opinion in chemical biology, 23:47-55, Dec 2014. URL: https://doi.org/10.1016/j.cbpa.2014.09.025, doi:10.1016/j.cbpa.2014.09.025. This article has 23 citations and is from a peer-reviewed journal.

43. (hailfinger2014targetingbcelllymphomas pages 11-15): Stephan Hailfinger, Georg Lenz, and Margot Thome. Targeting b-cell lymphomas with inhibitors of the malt1 paracaspase. Current opinion in chemical biology, 23:47-55, Dec 2014. URL: https://doi.org/10.1016/j.cbpa.2014.09.025, doi:10.1016/j.cbpa.2014.09.025. This article has 23 citations and is from a peer-reviewed journal.

44. (koonin2002originandevolution pages 3-4): E V Koonin and L Aravind. Origin and evolution of eukaryotic apoptosis: the bacterial connection. Cell Death and Differentiation, 9:394-404, Apr 2002. URL: https://doi.org/10.1038/sj.cdd.4400991, doi:10.1038/sj.cdd.4400991. This article has 546 citations and is from a domain leading peer-reviewed journal.

45. (krasovec2024intrinsicapoptosisis pages 3-4): Gabriel Krasovec, Helen R Horkan, Éric Quéinnec, and Jean-Philippe Chambon. Intrinsic apoptosis is evolutionarily divergent among metazoans. Evolution Letters, 8:267-282, Nov 2024. URL: https://doi.org/10.1093/evlett/qrad057, doi:10.1093/evlett/qrad057. This article has 21 citations and is from a domain leading peer-reviewed journal.

46. (krasovec2024intrinsicapoptosisis pages 2-3): Gabriel Krasovec, Helen R Horkan, Éric Quéinnec, and Jean-Philippe Chambon. Intrinsic apoptosis is evolutionarily divergent among metazoans. Evolution Letters, 8:267-282, Nov 2024. URL: https://doi.org/10.1093/evlett/qrad057, doi:10.1093/evlett/qrad057. This article has 21 citations and is from a domain leading peer-reviewed journal.

47. (mcluskey2015comparativestructuralanalysis pages 3-4): Karen McLuskey and Jeremy C. Mottram. Comparative structural analysis of the caspase family with other clan cd cysteine peptidases. Biochemical Journal, 466:219-232, Feb 2015. URL: https://doi.org/10.1042/bj20141324, doi:10.1042/bj20141324. This article has 101 citations and is from a domain leading peer-reviewed journal.

48. (malireddi2025threedecadesof pages 11-13): RKS Malireddi and TD Kanneganti. Three decades of caspases and ripks in life and death. Human molecular genetics, Jul 2025. URL: https://doi.org/10.1093/hmg/ddaf106, doi:10.1093/hmg/ddaf106. This article has 4 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PTHR10454-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR10454-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. mcluskey2015comparativestructuralanalysis pages 1-2
2. fuentesprior2004theproteinstructures pages 9-9
3. mcluskey2015comparativestructuralanalysis pages 10-11
4. mcluskey2015comparativestructuralanalysis pages 2-3
5. nicholson1999caspasestructureproteolytic pages 2-5
6. nadendla2025caspasesstructuraland pages 15-16
7. gao2024panoptosisbridgingapoptosis pages 2-4
8. malireddi2025threedecadesof pages 4-6
9. mcluskey2015comparativestructuralanalysis pages 7-8
10. malireddi2025threedecadesof pages 3-4
11. malireddi2025threedecadesof pages 16-17
12. koonin2002originandevolution pages 3-4
13. krasovec2024intrinsicapoptosisis pages 5-6
14. krasovec2024intrinsicapoptosisis pages 2-3
15. malireddi2025threedecadesof pages 11-13
16. nadendla2025caspasesstructuraland pages 5-6
17. biboverdugo2024evolutionofcaspases pages 3-5
18. nadendla2025caspasesstructuraland pages 7-8
19. hailfinger2014targetingbcelllymphomas pages 1-5
20. minina2017metacaspasesversuscaspases pages 2-3
21. fuentesprior2004theproteinstructures pages 2-3
22. biboverdugo2024evolutionofcaspases pages 5-7
23. nadendla2025caspasesstructuraland pages 10-11
24. krasovec2024intrinsicapoptosisis pages 9-10
25. fuentesprior2004theproteinstructures pages 3-4
26. zhang2025biologicalfunctionsand pages 1-2
27. minina2017metacaspasesversuscaspases pages 1-2
28. minina2017metacaspasesversuscaspases pages 5-7
29. biboverdugo2024evolutionofcaspases pages 1-3
30. minina2017metacaspasesversuscaspases pages 3-5
31. malireddi2025threedecadesof pages 9-11
32. hailfinger2014targetingbcelllymphomas pages 5-8
33. hailfinger2014targetingbcelllymphomas pages 11-15
34. krasovec2024intrinsicapoptosisis pages 3-4
35. mcluskey2015comparativestructuralanalysis pages 3-4
36. https://doi.org/10.1042/bj20141324,
37. https://doi.org/10.1042/bj20041142,
38. https://doi.org/10.1038/sj.cdd.4400598,
39. https://doi.org/10.1007/978-1-4020-6554-5\_2,
40. https://doi.org/10.3390/ijms25105270,
41. https://doi.org/10.1038/s41421-025-00791-3,
42. https://doi.org/10.1111/febs.15260,
43. https://doi.org/10.1038/cr.2010.168,
44. https://doi.org/10.1016/j.cbpa.2014.09.025,
45. https://doi.org/10.1038/cdd.2017.18,
46. https://doi.org/10.1007/s00018-015-2059-z,
47. https://doi.org/10.1093/hmg/ddaf106,
48. https://doi.org/10.1093/evlett/qrad057,
49. https://doi.org/10.1038/s41417-024-00765-9,
50. https://doi.org/10.3390/biomedicines10020344,
51. https://doi.org/10.1371/journal.pone.0127083,
52. https://doi.org/10.2147/jir.s519885,
53. https://doi.org/10.1038/sj.cdd.4400991,