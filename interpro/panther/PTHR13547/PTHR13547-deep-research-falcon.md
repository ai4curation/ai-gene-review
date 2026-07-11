---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-21T20:32:19.310106'
end_time: '2026-06-21T20:43:29.476579'
duration_seconds: 670.17
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR13547
  interpro_name: Mitochondrial RNase P catalytic subunit-like
  interpro_short_name: Mt_RNase_P_catalytic-like
  interpro_type: family
  interpro_integrated: None (top-level entry)
  member_databases: Not specified
  n_proteins: '3673'
  n_taxa: '5053'
  n_subfamilies: '8'
  interpro2go_terms: None mapped (no InterPro2GO terms for this entry)
  interpro_description: This family of proteins includes catalytic subunits of ribonuclease
    P (RNase P) complexes, which are primarily involved in the 5'-end maturation of
    tRNA molecules. Members of this family are characterized by their association
    with other protein components, such as TRMT10C/MRPP1 and HSD17B10/MRPP2, to form
    a functional complex capable of cleaving pre-tRNA substrates. These proteins display
    a non-productive active site that becomes fully functional upon binding to their
    protein partners and the tRNA substrate. Some members are also implicated in the
    maturation of other RNA species, such as mRNA and small nucleolar RNA (snoRNA),
    highlighting a broader role in RNA processing.
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 26
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PTHR13547-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR13547-deep-research-falcon_artifacts/artifact-01.md
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
- **Accession:** PTHR13547
- **Name:** Mitochondrial RNase P catalytic subunit-like
- **Short name:** Mt_RNase_P_catalytic-like
- **Entry type:** family
- **Integrated into / parent:** None (top-level entry)
- **Member database signatures:** Not specified
- **Scale:** 3673 proteins across 5053 taxa, 8 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** This family of proteins includes catalytic subunits of ribonuclease P (RNase P) complexes, which are primarily involved in the 5'-end maturation of tRNA molecules. Members of this family are characterized by their association with other protein components, such as TRMT10C/MRPP1 and HSD17B10/MRPP2, to form a functional complex capable of cleaving pre-tRNA substrates. These proteins display a non-productive active site that becomes fully functional upon binding to their protein partners and the tRNA substrate. Some members are also implicated in the maturation of other RNA species, such as mRNA and small nucleolar RNA (snoRNA), highlighting a broader role in RNA processing.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR13547 (Mitochondrial RNase P catalytic subunit-like)**, structured to support GO annotation review.

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
- **Accession:** PTHR13547
- **Name:** Mitochondrial RNase P catalytic subunit-like
- **Short name:** Mt_RNase_P_catalytic-like
- **Entry type:** family
- **Integrated into / parent:** None (top-level entry)
- **Member database signatures:** Not specified
- **Scale:** 3673 proteins across 5053 taxa, 8 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** This family of proteins includes catalytic subunits of ribonuclease P (RNase P) complexes, which are primarily involved in the 5'-end maturation of tRNA molecules. Members of this family are characterized by their association with other protein components, such as TRMT10C/MRPP1 and HSD17B10/MRPP2, to form a functional complex capable of cleaving pre-tRNA substrates. These proteins display a non-productive active site that becomes fully functional upon binding to their protein partners and the tRNA substrate. Some members are also implicated in the maturation of other RNA species, such as mRNA and small nucleolar RNA (snoRNA), highlighting a broader role in RNA processing.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR13547 (Mitochondrial RNase P catalytic subunit-like)**, structured to support GO annotation review.

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


# InterPro Family Research Report: PTHR13547 (Mitochondrial RNase P catalytic subunit-like)

## Executive Summary

InterPro entry **PTHR13547** represents a protein family of RNase P catalytic subunits (also known as PRORP or MRPP3 in various organisms) that catalyze the 5' end maturation of precursor tRNAs. **Currently, this entry has no InterPro2GO mappings.** This report evaluates the appropriateness of potential GO annotations, based on comprehensive review of recent structural, biochemical, and evolutionary literature (2015-2024).

**Verdict:** InterPro2GO mappings for PTHR13547 should be **ADDED with subfamily-specific restrictions**. Core GO terms for tRNA processing and endoribonuclease activity are safe for the entire family. However, cellular component and some partner-related terms must be restricted to specific subfamilies to avoid systematic over-annotation.

---

## 1. Family Definition and Biochemistry

### 1.1 Structural Architecture

PTHR13547 family members share a conserved three-domain architecture consisting of (karasik2016nuclearproteinonlyribonuclease pages 1-3, reinhard2015structureofthe pages 1-2, klemm2016thediversityof pages 1-4, klemm2016thediversityof pages 5-8):

| Structural domain/feature | Function | Conserved residues / motifs | Supporting evidence |
|---|---|---|---|
| N-terminal PPR domain | Major RNA-binding module for pre-tRNA recognition; engages the tRNA elbow and contributes to substrate positioning. In human mtRNase P, the PPR domain also contacts TRMT10C and helps recruit/position PRORP on substrate. | Tandem PPR motifs; plant PRORP1 contains ~5 PPR motifs, while truncated human MRPP3 structures retained only part of the PPR region. Conserved RNA-binding role across PRORPs rather than a single universal residue set. | PRORP proteins contain an N-terminal PPR domain linked to RNA recognition; Arabidopsis PRORP1 truncation of N-terminal PPR motifs reduces binding/cleavage; cryo-EM of human mtRNase P shows PRORP PPR domain contacting the tRNA elbow and TRMT10C (bhatta2021structuralbasisof pages 1-2, vilardo2023cleavagekineticsof pages 1-5, karasik2016nuclearproteinonlyribonuclease pages 1-3, reinhard2015structureofthe pages 1-2, klemm2016thediversityof pages 5-8) |
| Central Zn-binding domain | Structural hinge/scaffold connecting PPR and nuclease domains; supports the V-/L-shaped architecture needed to juxtapose substrate recognition and catalysis. | Conserved zinc-binding site in the central domain; exact coordinating residues are described as conserved in structural studies, but the core point for family review is the presence of a conserved Zn-binding structural module between PPR and NYN domains. | Arabidopsis PRORP1 and human MRPP3 both contain a central zinc-binding domain; crystal structures show this domain links the two arms of the enzyme and contributes to global fold (bhatta2021structuralbasisof pages 1-2, reinhard2015structureofthe pages 1-2, klemm2016thediversityof pages 5-8) |
| C-terminal NYN metallonuclease domain | Catalytic endonuclease domain that performs 5'-leader cleavage of pre-tRNAs via metal-dependent hydrolysis. | NYN (Nedd4-BP1, YacP nuclease) domain; conserved catalytic Asp set in plant PRORP1: D399, D474, D475, D493, with D497 contributing to metal coordination/outer-sphere interaction; corresponding human MRPP3 active-site residues include D409, D478, D479, D499. | Structural and biochemical work assigns catalysis to the NYN domain; conserved Asp residues are required for cleavage; PRORP enzymes use a two-metal-ion mechanism analogous to other phosphodiesterases (karasik2016nuclearproteinonlyribonuclease pages 1-3, reinhard2015structureofthe pages 1-2, klemm2016thediversityof pages 5-8, klemm2016thediversityof pages 10-12, klemm2016thediversityof pages 12-15) |
| Catalytic active site (metal-binding center) | Coordinates catalytic divalent metals and activates water for phosphodiester bond hydrolysis at the 5' end of pre-tRNA. | Plant PRORP1 active site: D399, D474, D475, D493, D497; human MRPP3 active-site region: D409, D478, D479, D499, with inactive/autoinhibited crystal conformations involving N412, R445, and R498 occluding productive metal binding in truncated structures. | Mn2+-bound PRORP1 structure supports a two-metal mechanism; mutating catalytic Asp residues severely impairs activity; human MRPP3 crystal structures showed a distorted/non-productive active site in truncated proteins, whereas cryo-EM of the full mtRNase P complex indicates an activated conformation in the assembled enzyme (bhatta2021structuralbasisof pages 1-2, reinhard2015structureofthe pages 1-2, reinhard2015structureofthe pages 4-5, klemm2016thediversityof pages 10-12, klemm2016thediversityof pages 12-15) |
| Overall PRORP/MRPP3 architecture | Integrates RNA recognition and catalysis in a single polypeptide; stand-alone in plants/protists but partner-dependent in metazoan mitochondria. | V-shaped/L-shaped architecture composed of PPR + central Zn-binding + NYN domains. | Arabidopsis PRORP1 and PRORP2 structures show the canonical tripartite architecture; human MRPP3 shares this domain organization but in animals requires TRMT10C-SDR5C1 for efficient and accurate cleavage of mitochondrial pre-tRNAs (bhatta2021structuralbasisof pages 1-2, vilardo2023cleavagekineticsof pages 1-5, karasik2016nuclearproteinonlyribonuclease pages 1-3, reinhard2015structureofthe pages 1-2, klemm2016thediversityof pages 5-8) |
| Human MRPP3 partner-dependent activation feature | In metazoan mitochondria, MRPP3 is the catalytic subunit but is strongly stimulated/positioned by TRMT10C-SDR5C1; accessory proteins enhance rate and fidelity and help process structurally degenerate mt-tRNAs. | Not a separate conserved motif, but a conserved functional feature of the metazoan mitochondrial branch of the family. | Human mtRNase P cryo-EM and kinetics show PRORP/MRPP3 alone can bind some substrates and weakly cleave some pre-tRNAs, but TRMT10C-SDR5C1 directs nuclease-domain positioning, increases cleavage rate/accuracy, and stabilizes processing of non-canonical mitochondrial tRNAs (bhatta2021structuralbasisof pages 1-2, vilardo2023cleavagekineticsof pages 1-5, bhatta2024structuralbasisof pages 1-6) |


*Table: This table summarizes the major structural modules and catalytic features of PRORP/MRPP3 proteins relevant to InterPro family review. It highlights which properties are broadly conserved across the family and which reflect the specialized metazoan mitochondrial RNase P branch.*

The **PPR domain** (pentatricopeptide repeat domain) comprises multiple tandem PPR motifs forming a right-handed superhelical structure that binds RNA substrates (bhatta2021structuralbasisof pages 1-2, karasik2016nuclearproteinonlyribonuclease pages 1-3). Crystal structures of *Arabidopsis thaliana* PRORP1 and PRORP2 revealed five PPR motifs in the N-terminal region, while human MRPP3 structures show a similar PPR organization (karasik2016nuclearproteinonlyribonuclease pages 1-3, reinhard2015structureofthe pages 1-2). Truncation of N-terminal PPR motifs in AtPRORP1 severely reduces both binding and cleavage activity, demonstrating the critical role of this domain in substrate recognition (reinhard2015structureofthe pages 1-2, klemm2016thediversityof pages 1-4).

The **central zinc-binding domain** serves as a structural scaffold connecting the PPR and metallonuclease domains, creating the characteristic V-shaped or L-shaped overall architecture essential for positioning the active site relative to the substrate (karasik2016nuclearproteinonlyribonuclease pages 1-3, reinhard2015structureofthe pages 1-2, reinhard2015structureofthe pages 4-5, klemm2016thediversityof pages 5-8).

The **NYN metallonuclease domain** (Nedd4-BP1, YacP nuclease family) contains the catalytic machinery for pre-tRNA 5' leader cleavage (karasik2016nuclearproteinonlyribonuclease pages 1-3, reinhard2015structureofthe pages 1-2, klemm2016thediversityof pages 1-4, klemm2016thediversityof pages 5-8). This domain represents the defining catalytic module of the family and houses the conserved active site residues.

### 1.2 Conserved Catalytic Residues and Mechanism

The catalytic active site contains a cluster of conserved aspartate residues that coordinate two divalent metal ions (typically Mg²⁺ or Mn²⁺) in a two-metal-ion catalytic mechanism analogous to other nucleases and polymerases (reinhard2015structureofthe pages 1-2, klemm2016thediversityof pages 1-4, klemm2016thediversityof pages 5-8, klemm2016thediversityof pages 10-12, klemm2016thediversityof pages 12-15). In *Arabidopsis* PRORP1, these are **D399, D474, D475, D493**, with **D497** forming outer-sphere interactions with metal 2 (karasik2016nuclearproteinonlyribonuclease pages 1-3, klemm2016thediversityof pages 10-12, klemm2016thediversityof pages 12-15). The corresponding human MRPP3 active site residues include **D409, D478, D479, D499** (reinhard2015structureofthe pages 1-2, reinhard2015structureofthe pages 4-5, klemm2016thediversityof pages 10-12).

Mechanistically, PRORPs use a **concerted metal-dependent hydrolysis mechanism** in which metal 1 activates a hydroxide nucleophile and metal 2 stabilizes the transition state and protonates the leaving 3' oxyanion (klemm2016thediversityof pages 10-12, klemm2016thediversityof pages 12-15). Kinetic isotope effect studies demonstrated that PRORP1 employs a metal-bound hydroxide nucleophile rather than a general base mechanism, with a characteristic pH dependence showing a single ionization (Hill coefficient nH = 1) consistent with metal-hydroxide activation (klemm2016thediversityof pages 10-12, klemm2016thediversityof pages 12-15). Alanine substitutions of the conserved aspartates severely impair or abolish catalytic activity, confirming their essential roles (karasik2016nuclearproteinonlyribonuclease pages 1-3, klemm2016thediversityof pages 10-12).

Recent cryo-EM structures of the human mitochondrial RNase P complex bound to pre-tRNA reveal that in the active, substrate-bound state, PRORP/MRPP3 positions its nuclease domain precisely above the 5' cleavage site, with the active site aspartates coordinating metal ions for phosphodiester bond hydrolysis (bhatta2021structuralbasisof pages 1-2, bhatta2021structuralbasisof pages 2-3). Earlier crystal structures of truncated human MRPP3 showed a distorted, non-productive active site with residues N412, R445, and R498 occluding metal-binding positions, suggesting an autoinhibited conformation that becomes activated upon assembly with MRPP1/MRPP2 and substrate binding (reinhard2015structureofthe pages 1-2, reinhard2015structureofthe pages 4-5, klemm2016thediversityof pages 10-12).

### 1.3 Fold Classification

PTHR13547 members adopt a **protein-only RNase P (PRORP)** fold characterized by the tripartite PPR + central Zn-binding + NYN metallonuclease architecture (karasik2016nuclearproteinonlyribonuclease pages 1-3, klemm2016thediversityof pages 1-4, klemm2016thediversityof pages 5-8). The NYN domain specifically belongs to the NYN/PIN-like nuclease superfamily, a group of metallonucleases involved in RNA processing across diverse biological contexts (klemm2016thediversityof pages 1-4, klemm2016thediversityof pages 5-8). This fold is evolutionarily distinct from the ribonucleoprotein RNase P complexes found in bacteria, archaea, and some eukaryotic nuclei, representing an independent evolutionary solution to the tRNA 5'-end maturation problem (klemm2016thediversityof pages 1-4, klemm2016thediversityof pages 5-8).

---

## 2. InterPro2GO Mapping Appropriateness

**Current status:** PTHR13547 has **no GO terms mapped** in the provided InterPro2GO data. This section evaluates which GO terms would be appropriate for this family.

> Recommended core Molecular Function for the family: **GO:0004540 ribonuclease activity** and, more specifically, **GO:0008408 3'-5' exonuclease activity** should **not** be used; the literature supports an **RNase P-like endonucleolytic pre-tRNA 5'-leader cleavage activity** by PRORP/MRPP3 proteins, so the most appropriate MF is **GO:0004521 endoribonuclease activity** only if InterPro curators accept a broader parent term, because the family acts as a metal-dependent endonuclease on pre-tRNA rather than a generic RNase. **GO:0046872 metal ion binding** is mechanistically true but too generic to be very informative as an InterPro2GO family term. The catalytic NYN metallonuclease domain with conserved Asp residues and a two-metal mechanism is conserved across characterized PRORPs/MRPP3 proteins (bhatta2021structuralbasisof pages 1-2, karasik2016nuclearproteinonlyribonuclease pages 1-3, reinhard2015structureofthe pages 1-2, klemm2016thediversityof pages 5-8, klemm2016thediversityof pages 10-12, klemm2016thediversityof pages 12-15)
>
> Recommended core Biological Process for the family: **GO:0008033 tRNA processing** is well supported across characterized family members and is the safest broad process term. A more specific child such as **GO:0001682 tRNA 5'-leader removal** would be biologically closest to the demonstrated activity, if available/accepted in the GO version used for InterPro2GO. **GO:0006400 tRNA modification** should **not** be attached to this family, because methylation is carried out by partner proteins such as TRMT10C/MRPP1 rather than PRORP/MRPP3 itself. **GO:0006399 tRNA metabolic process** may be acceptable as a broader parent but is less specific than **tRNA processing** (karasik2019interplaybetweensubstrate pages 1-2, bhatta2021structuralbasisof pages 1-2, vilardo2023cleavagekineticsof pages 1-5, saoji2018mitochondrialrnasep pages 1-4, klemm2016thediversityof pages 5-8)
>
> Terms that are appropriate for essentially all family members studied: **pre-tRNA endonucleolytic processing / tRNA processing** and a **metal-dependent endoribonuclease activity**. These are shared by plant single-subunit PRORPs, trypanosome PRORPs, and metazoan MRPP3 orthologs, despite differences in partner dependence and localization (vilardo2023cleavagekineticsof pages 1-5, karasik2016nuclearproteinonlyribonuclease pages 1-3, klemm2016thediversityof pages 1-4, klemm2016thediversityof pages 5-8)
>
> Subfamily-specific Cellular Component terms: **GO:0005739 mitochondrion** is appropriate for the metazoan MRPP3 branch and for organellar PRORP1-type proteins that localize to mitochondria, but it is **not valid for the entire family**, because plant PRORP2/3 are nuclear and PRORP1 can also be chloroplast-targeted. Thus, mitochondrion should be restricted to appropriate child entries or sequence subsets. For plant organellar PRORP1-like proteins, a broader plastid/mitochondrion localization may apply, but again not across the whole family. No single CC term appears safe for all PTHR13547 members except very broad eukaryotic intracellular localization, which would add little value (karasik2016nuclearproteinonlyribonuclease pages 1-3, saoji2018mitochondrialrnasep pages 1-4, klemm2016thediversityof pages 5-8)
>
> Over-annotation warning: do **not** assign metazoan-specific terms such as **mitochondrial tRNA processing** or **mitochondrial RNase P complex** to the whole family, because the family includes nuclear PRORPs and plant/chloroplast/mitochondrial single-subunit PRORPs. Likewise, do **not** assign methyltransferase-related terms, dehydrogenase-related terms, or obligate-complex terms to MRPP3-like proteins generally, since those belong to partner subunits or only to the metazoan mitochondrial subfamily (karasik2019interplaybetweensubstrate pages 1-2, bhatta2021structuralbasisof pages 1-2, vilardo2023cleavagekineticsof pages 1-5, saoji2018mitochondrialrnasep pages 1-4, hochberg2021biallelicvariantsin pages 1-2, klemm2016thediversityof pages 5-8)
>
> Practical GO recommendation pattern for PTHR13547: keep or add a **core BP term around tRNA processing / pre-tRNA 5'-end maturation** and, if a sufficiently specific MF is available in the InterPro2GO vocabulary, a **core endoribonuclease activity** term; avoid generic **metal ion binding** unless needed as non-core, and move **mitochondrion** or other compartment terms to narrower child entries that correspond to metazoan mitochondrial MRPP3 or plant organellar PRORP clades (bhatta2021structuralbasisof pages 1-2, vilardo2023cleavagekineticsof pages 1-5, karasik2016nuclearproteinonlyribonuclease pages 1-3, klemm2016thediversityof pages 5-8)


*Blockquote: This blockquote summarizes GO term recommendations for the PRORP/MRPP3 family, distinguishing family-wide terms from lineage-specific ones. It is useful for deciding which InterPro2GO mappings are safe to apply broadly and which should be restricted to subfamilies.*

### 2.1 Molecular Function (MF)

**Recommended core MF term:** The most appropriate molecular function for the entire family is an **endoribonuclease activity** term that reflects metal-dependent endonucleolytic cleavage of pre-tRNA 5' leaders. While the precise GO term "ribonuclease P activity" may exist in GO, curators should verify that any applied MF term accurately captures the endonucleolytic (rather than exonucleolytic) nature of the reaction and the metal dependence (karasik2019interplaybetweensubstrate pages 1-2, bhatta2021structuralbasisof pages 1-2, vilardo2023cleavagekineticsof pages 1-5, karasik2016nuclearproteinonlyribonuclease pages 1-3, klemm2016thediversityof pages 5-8, klemm2016thediversityof pages 10-12, klemm2016thediversityof pages 12-15).

**Generic metal ion binding (GO:0046872)** is mechanistically true for all family members given the two-metal-ion catalytic mechanism, but this term is too generic and uninformative to serve as a useful family-level annotation. It may be included as a non-core annotation if InterPro policy permits, but it should not be the primary MF (karasik2016nuclearproteinonlyribonuclease pages 1-3, klemm2016thediversityof pages 5-8, klemm2016thediversityof pages 10-12, klemm2016thediversityof pages 12-15).

**Terms to avoid:** Any methyltransferase activity, dehydrogenase activity, or S-adenosylmethionine-dependent activity terms should **not** be applied to PTHR13547, as these activities belong to the partner proteins TRMT10C/MRPP1 and SDR5C1/MRPP2 in metazoan mitochondria, not to PRORP/MRPP3 itself (karasik2019interplaybetweensubstrate pages 1-2, bhatta2021structuralbasisof pages 1-2, vilardo2023cleavagekineticsof pages 1-5, bhatta2024structuralbasisof pages 1-6).

### 2.2 Biological Process (BP)

**Recommended core BP term:** **GO:0008033 (tRNA processing)** is well-supported across all characterized family members and is the safest broad process term for the entire family (karasik2019interplaybetweensubstrate pages 1-2, bhatta2021structuralbasisof pages 1-2, vilardo2023cleavagekineticsof pages 1-5, karasik2016nuclearproteinonlyribonuclease pages 1-3, saoji2018mitochondrialrnasep pages 1-4, klemm2016thediversityof pages 5-8). A more specific child term such as **"tRNA 5'-leader removal"** or **"tRNA 5'-end maturation"** would be biologically more precise if available in the GO version used for InterPro2GO annotation.

**Terms to avoid:** tRNA methylation or tRNA modification terms should **not** be attached to this family entry, because the N1-methylation of purine-9 in mitochondrial tRNAs is catalyzed by the partner TRMT10C/MRPP1 subunit, not by PRORP/MRPP3 (karasik2019interplaybetweensubstrate pages 1-2, bhatta2021structuralbasisof pages 1-2, vilardo2023cleavagekineticsof pages 1-5, bhatta2024structuralbasisof pages 1-6). Similarly, avoid applying process terms that imply obligate complex formation, such as "mitochondrial RNase P complex assembly," as single-subunit PRORPs in plants and protists do not require additional protein partners (vilardo2023cleavagekineticsof pages 1-5, karasik2016nuclearproteinonlyribonuclease pages 1-3, klemm2016thediversityof pages 1-4, klemm2016thediversityof pages 5-8).

### 2.3 Cellular Component (CC)

**WARNING - No single CC term is safe for the entire family.** Cellular localization varies substantially across subfamilies:

- **Metazoan MRPP3** localizes to **mitochondria** (karasik2019interplaybetweensubstrate pages 1-2, bhatta2021structuralbasisof pages 1-2, saoji2018mitochondrialrnasep pages 1-4, hochberg2021biallelicvariantsin pages 1-2, klemm2016thediversityof pages 5-8)
- **Plant PRORP1** localizes to **mitochondria and chloroplasts** (organellar) (karasik2016nuclearproteinonlyribonuclease pages 1-3, klemm2016thediversityof pages 1-4, klemm2016thediversityof pages 5-8)
- **Plant PRORP2/PRORP3** localize to the **nucleus** (karasik2016nuclearproteinonlyribonuclease pages 1-3, klemm2016thediversityof pages 1-4, klemm2016thediversityof pages 5-8)
- **Trypanosome PRORP1** localizes to the **nucleus**, while **PRORP2** is **mitochondrial** (klemm2016thediversityof pages 1-4, klemm2016thediversityof pages 5-8)

Applying **GO:0005739 (mitochondrion)** to the entire PTHR13547 family would **systematically over-annotate** all nuclear PRORP proteins from plants and trypanosomes. InterPro curators should either:
1. **Avoid CC terms at the family level**, or
2. **Create subfamily-specific child InterPro entries** that restrict mitochondrion, chloroplast, or nucleus localization to the appropriate sequence clades.

---

## 3. Functional Divergence Across the Family

PTHR13547 exhibits significant **functional stratification** based on subcellular localization and partner-protein dependence, but all characterized members retain the core tRNA 5'-end processing activity (vilardo2023cleavagekineticsof pages 1-5, karasik2016nuclearproteinonlyribonuclease pages 1-3, klemm2016thediversityof pages 1-4, klemm2016thediversityof pages 5-8).

### 3.1 Single-Subunit vs. Partner-Dependent PRORPs

The most important functional subdivision is between:

**Single-subunit PRORPs** (plants, algae, trypanosomes): These enzymes are catalytically competent as standalone proteins. *Arabidopsis* PRORP1, PRORP2, and PRORP3 process pre-tRNA substrates efficiently in vitro without requiring accessory factors (vilardo2023cleavagekineticsof pages 1-5, karasik2016nuclearproteinonlyribonuclease pages 1-3, klemm2016thediversityof pages 1-4, klemm2016thediversityof pages 5-8). The green alga *Ostreococcus tauri* encodes a single PRORP that also functions independently (klemm2016thediversityof pages 5-8). *Trypanosoma brucei* has two PRORP paralogs (TbPRORP1 and TbPRORP2) that are differentially localized but both process pre-tRNAs as monomers (klemm2016thediversityof pages 1-4, klemm2016thediversityof pages 5-8).

**Partner-dependent PRORPs (metazoan MRPP3)**: In animals, the PRORP ortholog (termed MRPP3 or PRORP in human and *Drosophila*) requires two additional protein subunits, TRMT10C/MRPP1 (a methyltransferase) and SDR5C1/MRPP2 (a dehydrogenase), for efficient and accurate pre-tRNA cleavage in mitochondria (karasik2019interplaybetweensubstrate pages 1-2, bhatta2021structuralbasisof pages 1-2, vilardo2023cleavagekineticsof pages 1-5, bhatta2024structuralbasisof pages 1-6, reinhard2015structureofthe pages 2-3, saoji2018mitochondrialrnasep pages 1-4, hochberg2021biallelicvariantsin pages 1-2, klemm2016thediversityof pages 5-8). Human MRPP3 alone binds pre-tRNAs with nanomolar affinity and can weakly cleave some substrates, but the MRPP1/2 subcomplex dramatically enhances cleavage rate, accuracy, and substrate range (vilardo2023cleavagekineticsof pages 1-5, bhatta2024structuralbasisof pages 1-6). The TRMT10C-SDR5C1 subcomplex binds conserved tRNA structural elements (including the anticodon loop) and positions MRPP3's nuclease domain for precise cleavage (bhatta2021structuralbasisof pages 1-2, bhatta2021structuralbasisof pages 2-3, vilardo2023cleavagekineticsof pages 1-5).

This functional divergence does **not** represent neo-functionalization with opposite activities, but rather an evolutionary shift in the mode of substrate recognition and enzyme activation. The core catalytic mechanism—metal-dependent hydrolytic cleavage of the pre-tRNA 5' leader—is conserved across all PRORPs (vilardo2023cleavagekineticsof pages 1-5, klemm2016thediversityof pages 5-8, klemm2016thediversityof pages 10-12, klemm2016thediversityof pages 12-15).

### 3.2 Subcellular Localization Subfamilies

Within plants, PRORP paralogs have diverged in localization:

- **PRORP1-type (organellar):** Localize to mitochondria and/or chloroplasts. In *Arabidopsis*, PRORP1 is essential for organellar tRNA processing and cannot be complemented by nuclear PRORPs (karasik2016nuclearproteinonlyribonuclease pages 1-3, klemm2016thediversityof pages 5-8).
- **PRORP2/3-type (nuclear):** Localize to the nucleus. AtPRORP2 and AtPRORP3 have overlapping substrate specificity, and deletion of both is required to eliminate nuclear RNase P activity, indicating functional redundancy (karasik2016nuclearproteinonlyribonuclease pages 1-3, klemm2016thediversityof pages 5-8).

In trypanosomes, TbPRORP1 is nuclear and TbPRORP2 is mitochondrial, representing a different paralog-based compartmentalization strategy (klemm2016thediversityof pages 1-4, klemm2016thediversityof pages 5-8).

### 3.3 Absence of Catalytically Dead Pseudoenzymes

**No evidence** exists in the reviewed literature for catalytically inactive or pseudoenzyme members of PTHR13547. All structurally characterized PRORPs retain the conserved active site aspartates, and biochemically studied orthologs demonstrate endonucleolytic activity (bhatta2021structuralbasisof pages 1-2, vilardo2023cleavagekineticsof pages 1-5, karasik2016nuclearproteinonlyribonuclease pages 1-3, reinhard2015structureofthe pages 1-2, klemm2016thediversityof pages 5-8, klemm2016thediversityof pages 10-12). Human MRPP3 truncation mutants that showed distorted active sites in crystal structures (reinhard2015structureofthe pages 1-2, reinhard2015structureofthe pages 4-5) were artifacts of the N-terminal deletions and do not represent naturally occurring inactive forms. Full-length MRPP3 in the cryo-EM structure of the mitochondrial RNase P complex shows a productive, substrate-engaged active site (bhatta2021structuralbasisof pages 1-2, bhatta2021structuralbasisof pages 2-3).

---

## 4. Taxonomic Scope

PTHR13547 (PRORP/MRPP3) proteins are found **exclusively in Eukaryotes**, with broad but not universal distribution (klemm2016thediversityof pages 1-4, shaukat2021thedynamicnetwork pages 1-2, klemm2016thediversityof pages 5-8):

### 4.1 Confirmed Clades

- **Land plants** (Viridiplantae): *Arabidopsis thaliana* (3 paralogs: PRORP1, PRORP2, PRORP3), *Physcomitrella patens* (moss; 3 paralogs), and likely other land plants (karasik2016nuclearproteinonlyribonuclease pages 1-3, klemm2016thediversityof pages 1-4, klemm2016thediversityof pages 5-8)
- **Algae** (Chlorophyta): *Ostreococcus tauri* (1 PRORP) and potentially other green algae (klemm2016thediversityof pages 1-4, klemm2016thediversityof pages 5-8)
- **Excavata** (protists): *Trypanosoma brucei* (2 paralogs: TbPRORP1, TbPRORP2) and likely other kinetoplastids (klemm2016thediversityof pages 1-4, klemm2016thediversityof pages 5-8)
- **Metazoa** (animals): Humans, *Drosophila melanogaster*, and other animals encode MRPP3 orthologs localized to mitochondria (karasik2019interplaybetweensubstrate pages 1-2, bhatta2021structuralbasisof pages 1-2, saoji2018mitochondrialrnasep pages 1-4, hochberg2021biallelicvariantsin pages 1-2, klemm2016thediversityof pages 5-8)

According to the InterPro API data provided, PTHR13547 spans **3673 proteins across 5053 taxa**, with **8 subfamilies** annotated. The broad taxonomic range is consistent with a eukaryote-wide but lineage-specific distribution.

### 4.2 Absent Clades

**Bacteria and Archaea** lack PRORP proteins and instead use ribonucleoprotein RNase P complexes with a catalytic RNA subunit (klemm2016thediversityof pages 1-4, shaukat2021thedynamicnetwork pages 1-2, klemm2016thediversityof pages 5-8). Some eukaryotic lineages also appear to lack identifiable PRORP sequences, including certain clades in Jacobida (Excavata), Cyanidiophyceae (red algae/Archaeplastida), and Nuclearia (Opisthokonta), though this may reflect incomplete genome sequencing or highly divergent sequences (klemm2016thediversityof pages 1-4, klemm2016thediversityof pages 5-8).

### 4.3 Implications for GO Annotation Across Taxa

Because PRORPs are restricted to eukaryotes and show lineage-specific localization (mitochondrial in metazoa, nuclear and/or organellar in plants, mixed in protists), **cellular component GO terms must be clade-restricted**. Process and function terms related to tRNA 5'-end processing are valid across all taxa where PRORPs occur. However, terms implying "mitochondrial" localization or "mitochondrial tRNA processing" would incorrectly annotate plant nuclear PRORPs and trypanosome TbPRORP1.

---

## 5. Over-Annotation Verdict and Recommended GO Action

### 5.1 Current Status

PTHR13547 currently has **no InterPro2GO mappings**. This is a significant gap, as the family represents a well-characterized set of enzymes with a conserved core function.

### 5.2 Recommended GO Action Pattern

**RECOMMENDATION: ADD core GO terms with subfamily-specific restrictions**

**Core terms safe for the entire family:**
- **Biological Process:** GO:0008033 (tRNA processing) or a more specific child term for tRNA 5'-leader removal / tRNA 5'-end maturation
- **Molecular Function:** GO:0004521 (endoribonuclease activity) or a specialized RNase P activity term, if available

**Subfamily-specific terms requiring restriction:**
- **Cellular Component - Mitochondrion (GO:0005739):** Should be applied **only to metazoan MRPP3 orthologs and plant/protist organellar PRORP1-type proteins**. Create a child InterPro entry or annotation rule to exclude nuclear PRORPs.
- **Cellular Component - Nucleus:** Should be applied **only to plant PRORP2/3-type orthologs and trypanosome TbPRORP1-type proteins**.
- **Cellular Component - Chloroplast/Plastid:** Should be applied **only to plant organellar PRORP1-type proteins** known to have dual mitochondrial/chloroplast targeting.

**Terms to explicitly avoid at the family level:**
- Any methyltransferase or SAM-dependent activity (these belong to MRPP1/TRMT10C partners, not PRORP/MRPP3)
- Any dehydrogenase or NADH-dependent activity (these belong to MRPP2/SDR5C1 partners)
- Generic "metal ion binding" as the primary function (too uninformative)
- Process terms implying obligate complex formation (not true for single-subunit PRORPs)

### 5.3 InterPro Curation Recommendations

1. **Consider subdividing PTHR13547 into child entries** corresponding to:
   - Metazoan mitochondrial MRPP3 (partner-dependent)
   - Plant organellar PRORP1-type (single-subunit, mitochondrial/chloroplast)
   - Plant nuclear PRORP2/3-type (single-subunit, nuclear)
   - Protist PRORP orthologs

   This would allow safer application of cellular component and context-specific process terms.

2. **If subdivision is impractical**, use annotation rules or conditional mappings to apply CC terms only to the appropriate sequence subsets.

3. **Document the functional heterogeneity** in the InterPro entry description to alert users that not all family members share identical localization or partner dependence.

4. **Verify that applied GO MF and BP terms** reflect the endonucleolytic mechanism and tRNA-specific substrate, not generic ribonuclease or RNA-binding activities.

### 5.4 Summary Verdict

**PTHR13547 is suitable for InterPro2GO annotation with appropriate caveats.** The family is functionally homogeneous at the core biochemical level (all members catalyze tRNA 5'-leader cleavage via a conserved metal-dependent mechanism), making BP and MF annotations safe for the entire family. However, significant heterogeneity in subcellular localization and partner-protein dependence means that CC annotations must be subfamily-specific to avoid systematic over-annotation.

**Action pattern:** **MODIFY-to-specific** for cellular component terms; **ACCEPT** for core tRNA processing and endoribonuclease activity terms.

**Rationale:** This is a **type "family"** entry representing full-protein functions that are indeed conserved across the family (tRNA 5'-end processing). The conserved tripartite domain architecture and catalytic mechanism support family-wide functional annotations. The challenge is not whole-protein vs. module annotation (as with domain entries), but rather **lineage-specific context** (subcellular localization) that varies within a functionally conserved family. Proper curation requires either child entries or conditional GO mappings to reflect this biological reality.

---

## References

All citations in this report refer to context IDs from the evidence-gathering process. Key structural studies include the 2021 cryo-EM structure of human mitochondrial RNase P (bhatta2021structuralbasisof pages 1-2, bhatta2021structuralbasisof pages 2-3), the 2015-2016 crystal structures of plant PRORP and human MRPP3 (karasik2016nuclearproteinonlyribonuclease pages 1-3, reinhard2015structureofthe pages 1-2, reinhard2015structureofthe pages 4-5), and comprehensive reviews of RNase P diversity and mechanism (klemm2016thediversityof pages 1-4, klemm2016thediversityof pages 5-8, klemm2016thediversityof pages 10-12, klemm2016thediversityof pages 12-15). Biochemical characterization and partner-dependence studies are documented in (karasik2019interplaybetweensubstrate pages 1-2, vilardo2023cleavagekineticsof pages 1-5, bhatta2024structuralbasisof pages 1-6, reinhard2015structureofthe pages 2-3). Disease-associated variants and human genetics studies are cited from (hochberg2021biallelicvariantsin pages 1-2). Evolutionary distribution and taxonomy are supported by (klemm2016thediversityof pages 1-4, shaukat2021thedynamicnetwork pages 1-2, klemm2016thediversityof pages 5-8).

---

**Report prepared:** 2026  
**InterPro entry reviewed:** PTHR13547  
**Current InterPro2GO mappings:** None (0 GO terms)  
**Recommended action:** ADD core GO terms; RESTRICT cellular component terms to subfamilies

References

1. (karasik2016nuclearproteinonlyribonuclease pages 1-3): Agnes Karasik, Aranganathan Shanmuganathan, Michael J. Howard, Carol A. Fierke, and Markos Koutmos. Nuclear protein-only ribonuclease p2 structure and biochemical characterization provide insight into the conserved properties of trna 5' end processing enzymes. Journal of molecular biology, 428 1:26-40, Jan 2016. URL: https://doi.org/10.1016/j.jmb.2015.11.025, doi:10.1016/j.jmb.2015.11.025. This article has 43 citations and is from a domain leading peer-reviewed journal.

2. (reinhard2015structureofthe pages 1-2): L. Reinhard, S. Sridhara, and B. Martin Hällberg. Structure of the nuclease subunit of human mitochondrial rnase p. Nucleic Acids Research, 43:5664-5672, May 2015. URL: https://doi.org/10.1093/nar/gkv481, doi:10.1093/nar/gkv481. This article has 78 citations and is from a highest quality peer-reviewed journal.

3. (klemm2016thediversityof pages 1-4): Bradley Klemm, Nancy Wu, Yu Chen, Xin Liu, Kipchumba Kaitany, Michael Howard, and Carol Fierke. The diversity of ribonuclease p: protein and rna catalysts with analogous biological functions. Biomolecules, 6:27, May 2016. URL: https://doi.org/10.3390/biom6020027, doi:10.3390/biom6020027. This article has 92 citations.

4. (klemm2016thediversityof pages 5-8): Bradley Klemm, Nancy Wu, Yu Chen, Xin Liu, Kipchumba Kaitany, Michael Howard, and Carol Fierke. The diversity of ribonuclease p: protein and rna catalysts with analogous biological functions. Biomolecules, 6:27, May 2016. URL: https://doi.org/10.3390/biom6020027, doi:10.3390/biom6020027. This article has 92 citations.

5. (bhatta2021structuralbasisof pages 1-2): Arjun Bhatta, Christian Dienemann, Patrick Cramer, and Hauke S. Hillen. Structural basis of rna processing by human mitochondrial rnase p. Nature Structural & Molecular Biology, 28:713-723, Sep 2021. URL: https://doi.org/10.1038/s41594-021-00637-y, doi:10.1038/s41594-021-00637-y. This article has 107 citations and is from a highest quality peer-reviewed journal.

6. (vilardo2023cleavagekineticsof pages 1-5): Elisa Vilardo, Ursula Toth, Enxhi Hazisllari, and Walter Rossmanith. Cleavage kinetics of human mitochondrial rnase p and contribution of its non-nuclease subunits. Nucleic Acids Research, 51:10536-10550, Mar 2023. URL: https://doi.org/10.1101/2023.03.27.534089, doi:10.1101/2023.03.27.534089. This article has 19 citations and is from a highest quality peer-reviewed journal.

7. (klemm2016thediversityof pages 10-12): Bradley Klemm, Nancy Wu, Yu Chen, Xin Liu, Kipchumba Kaitany, Michael Howard, and Carol Fierke. The diversity of ribonuclease p: protein and rna catalysts with analogous biological functions. Biomolecules, 6:27, May 2016. URL: https://doi.org/10.3390/biom6020027, doi:10.3390/biom6020027. This article has 92 citations.

8. (klemm2016thediversityof pages 12-15): Bradley Klemm, Nancy Wu, Yu Chen, Xin Liu, Kipchumba Kaitany, Michael Howard, and Carol Fierke. The diversity of ribonuclease p: protein and rna catalysts with analogous biological functions. Biomolecules, 6:27, May 2016. URL: https://doi.org/10.3390/biom6020027, doi:10.3390/biom6020027. This article has 92 citations.

9. (reinhard2015structureofthe pages 4-5): L. Reinhard, S. Sridhara, and B. Martin Hällberg. Structure of the nuclease subunit of human mitochondrial rnase p. Nucleic Acids Research, 43:5664-5672, May 2015. URL: https://doi.org/10.1093/nar/gkv481, doi:10.1093/nar/gkv481. This article has 78 citations and is from a highest quality peer-reviewed journal.

10. (bhatta2024structuralbasisof pages 1-6): Arjun Bhatta. Structural basis of human mitochondrial rna processing. ArXiv, 2024. URL: https://doi.org/10.53846/goediss-10923, doi:10.53846/goediss-10923. This article has 0 citations.

11. (bhatta2021structuralbasisof pages 2-3): Arjun Bhatta, Christian Dienemann, Patrick Cramer, and Hauke S. Hillen. Structural basis of rna processing by human mitochondrial rnase p. Nature Structural & Molecular Biology, 28:713-723, Sep 2021. URL: https://doi.org/10.1038/s41594-021-00637-y, doi:10.1038/s41594-021-00637-y. This article has 107 citations and is from a highest quality peer-reviewed journal.

12. (karasik2019interplaybetweensubstrate pages 1-2): Agnes Karasik, Carol A. Fierke, and Markos Koutmos. Interplay between substrate recognition, 5′ end trna processing and methylation activity of human mitochondrial rnase p. RNA, 25:1646-1660, Aug 2019. URL: https://doi.org/10.1261/rna.069310.118, doi:10.1261/rna.069310.118. This article has 29 citations and is from a domain leading peer-reviewed journal.

13. (saoji2018mitochondrialrnasep pages 1-4): Maithili Saoji and Rachel T. Cox. Mitochondrial rnase p complex in animals: mitochondrial trna processing and links to disease. ArXiv, pages 47-71, Jan 2018. URL: https://doi.org/10.1007/978-3-319-78190-7\_3, doi:10.1007/978-3-319-78190-7\_3. This article has 5 citations.

14. (hochberg2021biallelicvariantsin pages 1-2): Irit Hochberg, Leigh A.M. Demain, Julie Richer, Kyle Thompson, Jill E. Urquhart, Alessandro Rea, Waheeda Pagarkar, Agustí Rodríguez-Palmero, Agatha Schlüter, Edgard Verdura, Aurora Pujol, Pilar Quijada-Fraile, Albert Amberger, Andrea J. Deutschmann, Sandra Demetz, Meredith Gillespie, Inna A. Belyantseva, Hugh J. McMillan, Melanie Barzik, Glenda M. Beaman, Reeya Motha, Kah Ying Ng, James O’Sullivan, Simon G. Williams, Sanjeev S. Bhaskar, Isabella R. Lawrence, Emma M. Jenkinson, Jessica L. Zambonin, Zeev Blumenfeld, Sergey Yalonetsky, Stephanie Oerum, Walter Rossmanith, Wyatt W. Yue, Johannes Zschocke, Kevin J. Munro, Brendan J. Battersby, Thomas B. Friedman, Robert W. Taylor, Raymond T. O’Keefe, and William G. Newman. Bi-allelic variants in the mitochondrial rnase p subunit prorp cause mitochondrial trna processing defects and pleiotropic multisystem presentations. The American Journal of Human Genetics, 108:2195-2204, Nov 2021. URL: https://doi.org/10.1016/j.ajhg.2021.10.002, doi:10.1016/j.ajhg.2021.10.002. This article has 53 citations.

15. (reinhard2015structureofthe pages 2-3): L. Reinhard, S. Sridhara, and B. Martin Hällberg. Structure of the nuclease subunit of human mitochondrial rnase p. Nucleic Acids Research, 43:5664-5672, May 2015. URL: https://doi.org/10.1093/nar/gkv481, doi:10.1093/nar/gkv481. This article has 78 citations and is from a highest quality peer-reviewed journal.

16. (shaukat2021thedynamicnetwork pages 1-2): Athanasios-Nasir Shaukat, Eleni G. Kaliatsi, Ilias Skeparnias, and Constantinos Stathopoulos. The dynamic network of rnp rnase p subunits. International Journal of Molecular Sciences, 22:10307, Sep 2021. URL: https://doi.org/10.3390/ijms221910307, doi:10.3390/ijms221910307. This article has 16 citations.

## Artifacts

- [Edison artifact artifact-00](PTHR13547-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR13547-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. klemm2016thediversityof pages 5-8
2. hochberg2021biallelicvariantsin pages 1-2
3. karasik2016nuclearproteinonlyribonuclease pages 1-3
4. reinhard2015structureofthe pages 1-2
5. klemm2016thediversityof pages 1-4
6. bhatta2021structuralbasisof pages 1-2
7. vilardo2023cleavagekineticsof pages 1-5
8. klemm2016thediversityof pages 10-12
9. klemm2016thediversityof pages 12-15
10. reinhard2015structureofthe pages 4-5
11. bhatta2024structuralbasisof pages 1-6
12. bhatta2021structuralbasisof pages 2-3
13. karasik2019interplaybetweensubstrate pages 1-2
14. saoji2018mitochondrialrnasep pages 1-4
15. reinhard2015structureofthe pages 2-3
16. shaukat2021thedynamicnetwork pages 1-2
17. https://doi.org/10.1016/j.jmb.2015.11.025,
18. https://doi.org/10.1093/nar/gkv481,
19. https://doi.org/10.3390/biom6020027,
20. https://doi.org/10.1038/s41594-021-00637-y,
21. https://doi.org/10.1101/2023.03.27.534089,
22. https://doi.org/10.53846/goediss-10923,
23. https://doi.org/10.1261/rna.069310.118,
24. https://doi.org/10.1007/978-3-319-78190-7\_3,
25. https://doi.org/10.1016/j.ajhg.2021.10.002,
26. https://doi.org/10.3390/ijms221910307,