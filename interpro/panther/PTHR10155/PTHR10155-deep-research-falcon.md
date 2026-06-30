---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-28T19:39:34.292994'
end_time: '2026-06-28T20:05:43.785281'
duration_seconds: 1569.49
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR10155
  interpro_name: PHOSPHATIDYLINOSITOL 3-KINASE REGULATORY SUBUNIT
  interpro_short_name: Not specified
  interpro_type: family
  interpro_integrated: None (top-level entry)
  member_databases: Not specified
  n_proteins: '16060'
  n_taxa: '4817'
  n_subfamilies: '21'
  interpro2go_terms: None mapped (no InterPro2GO terms for this entry)
  interpro_description: Not specified in InterPro
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 23
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: PTHR10155-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR10155-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: PTHR10155-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
---

## Question

# InterPro Family Research for GO Annotation Review

## ⚠️ CRITICAL: Family Identification Context

**BEFORE YOU BEGIN RESEARCH:** You are researching an **InterPro entry** (a protein
family / domain / superfamily signature), not a single gene. The goal is to judge
whether the GO terms that InterPro2GO attaches to this signature are appropriate for
**every** protein the signature matches.

### Target InterPro Entry (from the InterPro API):
- **Accession:** PTHR10155
- **Name:** PHOSPHATIDYLINOSITOL 3-KINASE REGULATORY SUBUNIT
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** None (top-level entry)
- **Member database signatures:** Not specified
- **Scale:** 16060 proteins across 4817 taxa, 21 subfamilies
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
**PTHR10155 (PHOSPHATIDYLINOSITOL 3-KINASE REGULATORY SUBUNIT)**, structured to support GO annotation review.

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
- **Accession:** PTHR10155
- **Name:** PHOSPHATIDYLINOSITOL 3-KINASE REGULATORY SUBUNIT
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** None (top-level entry)
- **Member database signatures:** Not specified
- **Scale:** 16060 proteins across 4817 taxa, 21 subfamilies
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
**PTHR10155 (PHOSPHATIDYLINOSITOL 3-KINASE REGULATORY SUBUNIT)**, structured to support GO annotation review.

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


# Comprehensive Research Report: InterPro Family PTHR10155 — PHOSPHATIDYLINOSITOL 3-KINASE REGULATORY SUBUNIT

## 1. Family Definition and Biochemistry

### 1.1 Overview

PTHR10155 is a PANTHER family-level entry that groups the non-catalytic (regulatory/adaptor) subunits of phosphatidylinositol 3-kinases (PI3Ks). The family spans 16,060 proteins across 4,817 taxa and encompasses 21 subfamilies. Critically, this family unites three structurally and functionally distinct classes of PI3K regulatory proteins:

**Class IA regulatory subunits** (PIK3R1/p85α, PIK3R2/p85β, PIK3R3/p55γ, and splice variants p55α and p50α) contain a characteristic modular domain architecture: an N-terminal SH3 domain, proline-rich sequences, a BH (Bcr Homology/RhoGAP-like) domain, followed by two SH2 domains (nSH2 and cSH2) separated by an inter-SH2 (iSH2) coiled-coil region (fox2020classiapi3k pages 1-3, kapeller1994phosphatidylinositol3‐kinase pages 2-3, kapeller1994phosphatidylinositol3‐kinase pages 3-5). The iSH2 domain is the primary binding site for class IA catalytic subunits (p110α, p110β, p110δ), while the nSH2 and cSH2 domains recognize phosphotyrosine motifs on activated receptor tyrosine kinases or adaptor proteins such as IRS-1 (kapeller1994phosphatidylinositol3‐kinase pages 3-5). The SH2 domains show a consensus binding preference for the motif Y-(MNIVE)-X-M (kapeller1994phosphatidylinositol3‐kinase pages 3-5). The shorter splice variants p55α, p50α, and p55γ lack the N-terminal SH3 and BH domains but retain the SH2-iSH2-SH2 core that is sufficient for p110 binding (karolina2012activationregulationand pages 19-22, fox2020classiapi3k pages 3-4). Between p85α and p85β, the SH3 and BH domains share only 37% sequence homology, and p85β possesses a unique C-terminal proline-rich region (kim2024divergentrolesof pages 3-4).

**Class IB regulatory subunits** (PIK3R5/p101 and PIK3R6/p84/p87PIKAP) associate exclusively with the p110γ catalytic subunit and lack identifiable SH2, SH3, or BH domains. They show no homology to class IA regulatory subunits or to other known protein families (karolina2012activationregulationand pages 19-22). Their N-terminal segment interacts directly with p110γ, while the C-terminal region binds Gβγ subunits released from activated G protein-coupled receptors (GPCRs), mediating membrane recruitment and activation in immune cells (li2024targetingpi3kfamily pages 2-5).

**Class III regulatory subunit** (PIK3R4/VPS15/p150) is structurally unrelated to either class I subgroup. VPS15 contains a kinase-like domain (likely pseudokinase, with only autophosphorylation demonstrated and no known substrates beyond itself), helical/HEAT-like domains, a linker, and WD40 repeats (karolina2012activationregulationand pages 19-22, ohashi2021activationmechanismsof pages 3-4). It is myristoylated for membrane attachment and serves as the backbone of VPS34 (PIK3C3) complexes, stabilizing VPS34 and regulating PI3P production for autophagy and endocytic trafficking (karolina2012activationregulationand pages 19-22, ohashi2021activationmechanismsof pages 3-4, li2024targetingpi3kfamily pages 2-5).

### 1.2 Mechanistic Functions

Class IA p85 subunits serve a dual regulatory role: they stabilize p110 catalytic subunits (preventing their thermal degradation) while simultaneously inhibiting basal catalytic activity through inhibitory contacts between the nSH2/iSH2 domains and the p110 kinase domain (fox2020classiapi3k pages 1-3, li2024targetingpi3kfamily pages 2-5). Upon receptor activation, phosphotyrosine binding to the SH2 domains relieves this inhibition, allowing p110 to phosphorylate PtdIns(4,5)P₂ to PtdIns(3,4,5)P₃ at the membrane (kapeller1994phosphatidylinositol3‐kinase pages 3-5). Three critical inhibitory interfaces have been identified between p85 and p110: nSH2-C2/HD/KD, cSH2-KD, and iSH2-C2/KD (sheng2024molecularbasisof pages 29-31).

The following table summarizes the major subfamilies within PTHR10155 and their key characteristics:

| Gene Name | Protein Name | PI3K Class | Domain Architecture | Catalytic Partner | Upstream Signal | Key Functions | Taxonomic Distribution |
|---|---|---|---|---|---|---|---|
| **PIK3R1** | p85α; splice isoforms p55α and p50α | Class IA | p85α: SH3–proline-rich motif(s)–BH/RhoGAP-like–nSH2–iSH2–cSH2; shorter splice isoforms lack the N-terminal SH3/BH region and retain SH2/iSH2 core | p110α/PIK3CA, p110β/PIK3CB, p110δ/PIK3CD | Primarily receptor tyrosine kinases via phosphotyrosine docking proteins such as IRS/adaptors | Canonical class IA regulatory/adaptor subunit: stabilizes and inhibits p110 at rest, recruits holoenzyme to phosphotyrosine signals, mediates p110-independent scaffold functions including PTEN regulation, Rab/Cdc42-related trafficking/cytoskeletal control, ER-stress signaling, and JNK signaling; tumor-suppressive in many contexts (fox2020classiapi3k pages 1-3, fox2020classiapi3k pages 4-6, kapeller1994phosphatidylinositol3‐kinase pages 3-5, fox2020classiapi3k pages 15-16, fox2020classiapi3k pages 16-18, fox2020classiapi3k pages 13-15, fox2020classiapi3k pages 12-13, kim2024divergentrolesof pages 7-8, sheng2024molecularbasisof pages 20-23) | Metazoan class I branch; class I/class II PI3Ks arose in early metazoans, not the ancestral pan-eukaryotic PI3K system (brown2011phylogenomicsofphosphoinositide pages 7-8, brown2011phylogenomicsofphosphoinositide pages 8-9) |
| **PIK3R2** | p85β | Class IA | SH3–proline-rich motif(s)–BH/RhoGAP-like–nSH2–iSH2–cSH2; similar overall scaffold to p85α but divergent N-terminal sequence/function | p110α/PIK3CA, p110β/PIK3CB, p110δ/PIK3CD | Primarily receptor tyrosine kinases via phosphotyrosine docking proteins | Class IA regulatory subunit with non-redundant behavior versus p85α: regulates basal and stimulated PI3K signaling differently, has distinct roles in metabolism, T-cell biology, and cancer; often described as more pro-oncogenic than p85α; also shows p110-independent scaffold roles (kim2024divergentrolesof pages 7-8, kim2024divergentrolesof pages 1-2, kim2024divergentrolesof pages 3-4, kim2024divergentrolesof pages 4-5, kim2024divergentrolesof pages 6-7, fox2020classiapi3k pages 15-16, fox2020classiapi3k pages 16-18) | Metazoan class I branch; not part of the ancestral VPS34/VPS15 system (brown2011phylogenomicsofphosphoinositide pages 7-8, brown2011phylogenomicsofphosphoinositide pages 8-9) |
| **PIK3R3** | p55γ | Class IA | Shorter class IA regulatory subunit lacking the long N-terminal SH3/BH region; retains class IA SH2–iSH2–SH2 core for p110 binding and phosphotyrosine recognition | p110α/PIK3CA, p110β/PIK3CB, p110δ/PIK3CD | Primarily receptor tyrosine kinases/adaptor phosphotyrosine signals | Class IA adaptor/regulatory subunit with weaker or more selective interactions than major p85 isoforms in some signaling settings; lacks the full N-terminal scaffold/GTPase-regulatory apparatus of p85α/p85β, so it cannot be assumed to share all p110-independent functions (karolina2012activationregulationand pages 19-22, fox2020classiapi3k pages 1-3, fox2020classiapi3k pages 4-6, kim2024divergentrolesof pages 3-4) | Metazoan class I branch (brown2011phylogenomicsofphosphoinositide pages 7-8, brown2011phylogenomicsofphosphoinositide pages 8-9) |
| **PIK3R4** | VPS15 / p150 | Class III | Kinase-like/pseudokinase domain–helical/HEAT-like regions–linker–WD40 repeats; structurally unrelated to p85-family SH2 adaptors | VPS34 / PIK3C3 | Nutrient- and membrane-trafficking-associated VPS34 complex regulation rather than phosphotyrosine receptor docking | Core regulatory subunit/backbone of class III PI3K complexes; stabilizes VPS34, scaffolds VPS34 complexes I/II, helps membrane recruitment and regulation of PI3P production in autophagy and endocytic trafficking; mechanistically distinct from class IA/IB regulatory subunits (karolina2012activationregulationand pages 19-22, li2024targetingpi3kfamily pages 2-5, ohashi2021activationmechanismsof pages 3-4, ohashi2021activationmechanismsof pages 2-3, brown2011phylogenomicsofphosphoinositide pages 7-8) | Ancient and broadly conserved across eukaryotes; VPS34/VPS15 system is the ancestral PI3K branch present from yeast to metazoans (ohashi2021activationmechanismsof pages 2-3, brown2011phylogenomicsofphosphoinositide pages 7-8, brown2011phylogenomicsofphosphoinositide pages 8-9) |
| **PIK3R5** | p101 | Class IB | No classic p85-like SH2/SH3/BH architecture; specialized class IB adaptor with p110γ-interacting region and Gβγ-responsive region/domain organization distinct from class IA adaptors | p110γ / PIK3CG | GPCR signaling via Gβγ | Regulatory/adaptor subunit of PI3Kγ complex; promotes coupling of p110γ to GPCR inputs and biases responsiveness to Gβγ-driven signals in leukocytes and inflammatory cells; does not behave like class IA p85 proteins (karolina2012activationregulationand pages 19-22, li2024targetingpi3kfamily pages 2-5, sheng2024molecularbasisof pages 19-20) | Vertebrate/immune-associated class IB branch; evolutionarily later and much narrower than VPS15 (brown2011phylogenomicsofphosphoinositide pages 8-9) |
| **PIK3R6** | p84 / p87PIKAP | Class IB | No classic p85-like SH2/SH3/BH architecture; distinct class IB adaptor for PI3Kγ, structurally/functionally different from p101 and class IA p85 proteins | p110γ / PIK3CG | GPCR signaling, with direct and context-dependent Gβγ regulation | Alternative PI3Kγ regulatory subunit; forms p84/p110γ complexes with signaling properties distinct from p101/p110γ, helping tune neutrophil and immune-cell responses; another example of divergence within the broader “PI3K regulatory subunit” label (karolina2012activationregulationand pages 19-22, li2024targetingpi3kfamily pages 2-5, sheng2024molecularbasisof pages 19-20) | Vertebrate/immune-associated class IB branch; evolutionarily later than the ancestral class III system (brown2011phylogenomicsofphosphoinositide pages 8-9) |


*Table: This table summarizes the major subfamilies grouped under PTHR10155 and highlights why they are not functionally homogeneous for GO annotation. It contrasts class IA SH2 adaptors, class IB GPCR-responsive PI3Kγ adaptors, and the ancient class III VPS15 scaffold.*

## 2. InterPro2GO Mapping Appropriateness

### 2.1 Current Status

No InterPro2GO terms are currently mapped to PTHR10155. This is the correct status given the radical functional and structural heterogeneity of the family.

### 2.2 Assessment of Candidate GO Terms

A systematic evaluation of candidate GO terms demonstrates that no single GO term could apply correctly across all members of this family. The following table presents this analysis:

| Candidate GO Term | GO ID (approximate) | Applicability to Class IA | Applicability to Class IB | Applicability to VPS15/Class III | Verdict (appropriate for whole family Y/N) | Recommendation |
|---|---|---|---|---|---|---|
| phosphatidylinositol 3-kinase complex | GO:0005942 | Yes: class IA p85 proteins are obligate regulatory subunits of class I PI3K heterodimers | Yes: p101/p84 are regulatory subunits of PI3Kγ heterodimers | No: VPS15 belongs to VPS34/class III complexes, not the canonical GO:0005942 class I PI3K complex | N | Move to child entries for class IA and possibly class IB only; do not map to PTHR10155 as a whole (karolina2012activationregulationand pages 19-22, li2024targetingpi3kfamily pages 2-5, ohashi2021activationmechanismsof pages 2-3) |
| phosphatidylinositol 3-kinase activity | GO:0035004 | No: regulatory subunits are not the lipid kinase catalytic subunits | No | No: VPS15 regulates VPS34 but is not itself the PI 3-kinase catalytic enzyme | N | REMOVE/never map at family level; this is a catalytic-subunit function (fox2020classiapi3k pages 1-3, karolina2012activationregulationand pages 19-22, ohashi2021activationmechanismsof pages 3-4) |
| phosphatidylinositol 3-kinase regulatory activity | GO:0016303 or similar approximate regulatory term | Yes in broad biochemical sense: p85 proteins regulate p110 catalytic activity | Yes: p101/p84 regulate p110γ | Yes in broad sense: VPS15 regulates VPS34 activity/stability | Borderline N | Even if broadly true, too heterogeneous mechanistically and not a stable GO concept across all branches; if used at all, restrict to child entries with explicit evidence (fox2020classiapi3k pages 1-3, karolina2012activationregulationand pages 19-22, li2024targetingpi3kfamily pages 2-5, ohashi2021activationmechanismsof pages 3-4) |
| protein binding | GO:0005515 | Yes | Yes | Yes | N | KEEP_AS_NON_CORE at most; too generic to be useful for InterPro2GO (fox2020classiapi3k pages 1-3, li2024targetingpi3kfamily pages 2-5, ohashi2021activationmechanismsof pages 3-4) |
| cytoplasm | GO:0005737 | Often yes, but not exclusive; many shuttle to membranes, nucleus, endomembrane sites | Often yes | Often yes, but VPS15 is strongly endomembrane-associated | N | Too generic and context-dependent; do not map (fox2020classiapi3k pages 15-16, fox2020classiapi3k pages 16-18, kim2024divergentrolesof pages 6-7, kim2024divergentrolesof pages 7-8) |
| membrane | GO:0016020 | Indirect/transient membrane recruitment upon receptor signaling | Indirect/transient membrane recruitment during GPCR signaling | Yes, strongly associated with intracellular membranes via VPS34 complexes | N | Over-broad and not universally true as a stable component term; avoid family-level mapping (karolina2012activationregulationand pages 19-22, ohashi2021activationmechanismsof pages 3-4, ohashi2021activationmechanismsof pages 2-3) |
| signal transduction | GO:0007165 | Yes: major role in RTK/insulin signaling and other pathways | Yes: major role in GPCR signaling in immune cells | Partly: VPS15 participates in nutrient/endocytic signaling but also constitutive trafficking/autophagy functions | N | Too broad and biologically heterogeneous; if used, only on more specific descendants (karolina2012activationregulationand pages 19-22, kim2024divergentrolesof pages 7-8, kim2024divergentrolesof pages 1-2, fox2020classiapi3k pages 15-16) |
| phosphatidylinositol-mediated signaling | GO:0048015 | Yes for class IA | Yes for class IB | Yes in a broad sense via VPS34-generated PI3P pathways | Borderline N | Although all branches connect to phosphoinositide signaling, the pathways differ too much (PIP3 RTK/GPCR signaling versus PI3P autophagy/endocytosis); do not map at top family (karolina2012activationregulationand pages 19-22, li2024targetingpi3kfamily pages 2-5, ohashi2021activationmechanismsof pages 2-3, brown2011phylogenomicsofphosphoinositide pages 7-8) |
| autophagy | GO:0006914 | Not a universal/core role for class IA regulatory subunits | Not a universal/core role for class IB regulatory subunits | Yes: VPS15/VPS34 complexes are core autophagy regulators | N | Move, if anywhere, to VPS15/class III child entry only; mapping to PTHR10155 would strongly over-annotate class I proteins (karolina2012activationregulationand pages 19-22, ohashi2021activationmechanismsof pages 3-4, ohashi2021activationmechanismsof pages 2-3) |
| insulin signaling pathway | GO:0008286 | Yes for major subset of class IA, especially PIK3R1/PIK3R2 and their splice isoforms | No: not core for class IB | No: not core for VPS15/class III | N | Move only to relevant class IA child entries, especially PIK3R1/PIK3R2; never to the top family (kim2024divergentrolesof pages 7-8, kim2024divergentrolesof pages 1-2, kim2024divergentrolesof pages 4-5, kim2024divergentrolesof pages 6-7) |
| receptor tyrosine kinase signaling pathway | GO:0007169 | Yes for class IA | No: class IB is GPCR-linked | No: VPS15/class III is not an RTK adaptor family | N | Restrict to class IA child entries only (fox2020classiapi3k pages 1-3, karolina2012activationregulationand pages 19-22, sheng2024molecularbasisof pages 29-31) |
| G protein-coupled receptor signaling pathway | GO:0007186 | No, not core | Yes: defining for PI3Kγ regulatory subunits p101/p84 | No | N | Restrict to class IB child entries only (karolina2012activationregulationand pages 19-22, li2024targetingpi3kfamily pages 2-5, sheng2024molecularbasisof pages 19-20) |
| endocytosis / endosomal trafficking | GO:0006897 / GO:0006898 | Sometimes yes through p110-independent Rab trafficking roles | Context-dependent in immune cells | Yes, strongly for VPS15/VPS34 complexes | N | Too uneven across subfamilies; possible only on narrower descendants with evidence (fox2020classiapi3k pages 15-16, fox2020classiapi3k pages 16-18, fox2020classiapi3k pages 13-15, ohashi2021activationmechanismsof pages 3-4) |
| phosphatidylinositol 3-kinase regulator activity, GTP-dependent GPCR branch | approximate | No | Yes | No | N | Suitable only for class IB child entries if a precise GO term exists; not for whole family (karolina2012activationregulationand pages 19-22, li2024targetingpi3kfamily pages 2-5, sheng2024molecularbasisof pages 19-20) |
| phosphatidylinositol 3-kinase regulator activity, RTK/IRS-associated branch | approximate | Yes | No | No | N | Suitable only for class IA child entries if supported by GO; not for top family (fox2020classiapi3k pages 1-3, kapeller1994phosphatidylinositol3‐kinase pages 3-5, kim2024divergentrolesof pages 7-8, kim2024divergentrolesof pages 4-5) |


*Table: This table evaluates candidate GO terms that might be considered for InterPro family PTHR10155 and shows why most are too broad or branch-specific. It is useful for deciding that no top-level InterPro2GO mapping should be added to this highly heterogeneous family.*

As shown, every specific GO term that could be considered—from molecular function terms like "phosphatidylinositol 3-kinase complex" (GO:0005942) to biological process terms like "autophagy" (GO:0006914) or "insulin signaling pathway" (GO:0008286)—applies only to a subset of family members and would systematically over-annotate the others.

## 3. Functional Divergence Across the Family

### 3.1 Class IA Internal Divergence: p85α vs. p85β

Even within the most closely related subfamily pair, functional divergence is profound. A comprehensive 2024 review by Kim et al. documented that p85α (PIK3R1) and p85β (PIK3R2) exhibit opposing roles in multiple contexts (kim2024divergentrolesof pages 7-8, kim2024divergentrolesof pages 1-2):

- **Cancer:** p85α acts as a tumor suppressor, with decreased expression in prostate, lung, ovarian, bladder, breast, and liver cancers. p85β, conversely, is oncogenic, with increased expression driving tumor progression in breast, endometrial, colon, ovarian, and lung cancers (kim2024divergentrolesof pages 7-8, kim2024divergentrolesof pages 1-2). PIK3R1 mutations occur in approximately 2.4% of cancers, with ~70% being driver mutations; they are particularly prevalent in endometrial cancer (~30% of cases) (sheng2024molecularbasisof pages 20-23).

- **Metabolism:** Whole-body or liver-specific deletion of PIK3R1 increases insulin sensitivity, while muscle-specific deletion has no effect. p85β deletion improves insulin sensitivity without affecting glucose tolerance. Double knockout of both genes in liver reduces insulin sensitivity (kim2024divergentrolesof pages 1-2, kim2024divergentrolesof pages 4-5). p85α primarily mediates insulin-stimulated PI3K activity, whereas p85β influences basal PI3K activity levels (kim2024divergentrolesof pages 4-5).

- **Immune function:** p85α facilitates B cell development (its knockout causes lethality from B cell defects), while p85β regulates T cell differentiation and maturation (kim2024divergentrolesof pages 7-8, kim2024divergentrolesof pages 1-2).

### 3.2 p110-Independent Functions

Class IA regulatory subunits, particularly p85α, perform extensive functions independent of PI3K catalytic activity (fox2020classiapi3k pages 1-3). These include:

- **GAP activity:** The BH domain shows GAP activity toward Rab4 and Rab5 GTPases, regulating receptor endocytosis and down-regulation (fox2020classiapi3k pages 13-15).
- **Cytoskeletal regulation:** p85 binds and activates Cdc42, triggering filopodia formation, stress fiber disassembly, and cytokinesis. p85 acts as a scaffold recruiting Cdc42 and septin 2 to the cleavage furrow (fox2020classiapi3k pages 15-16).
- **PTEN stabilization:** Dimeric p85 positively regulates PTEN stability through BH domain interactions (fox2020classiapi3k pages 16-18, fox2020classiapi3k pages 12-13).
- **Stress signaling:** p85α is required for JNK activation through the Cdc42/MKK4 pathway and mediates nuclear translocation of XBP-1 during ER stress (kim2024divergentrolesof pages 6-7, fox2020classiapi3k pages 12-13, kim2024divergentrolesof pages 7-8).
- **p53-mediated senescence:** Free p85 forms complexes with p300 to enhance p53 acetylation (fox2020classiapi3k pages 10-12).

These p110-independent functions require the N-terminal SH3 and BH domains found only in full-length p85α and p85β, not in the shorter splice variants (fox2020classiapi3k pages 12-13).

### 3.3 Class IB vs. Class IA Divergence

Class IB regulatory subunits (p101, p84) do not influence p110γ stability or basal activity, unlike their class IA counterparts which both stabilize and inhibit p110 (sheng2024molecularbasisof pages 19-20). Instead, they serve primarily as membrane-recruitment adaptors responding to Gβγ subunits from GPCR activation. The two class IB subunits themselves show distinct signaling properties: p101/p110γ and p84/p110γ complexes bias PI3Kγ activation toward different GPCR agonists and control distinct neutrophil responses (li2024targetingpi3kfamily pages 2-5).

### 3.4 Class III VPS15: A Fundamentally Different Protein

VPS15/PIK3R4 is mechanistically unrelated to class I regulatory subunits. It functions as the constitutive regulatory backbone of class III PI3K complexes (Complex I for autophagy: VPS34–VPS15–Beclin 1–ATG14L; Complex II for endocytosis: VPS34–VPS15–Beclin 1–UVRAG) (ohashi2021activationmechanismsof pages 3-4, ohashi2021activationmechanismsof pages 2-3). VPS15 autoinhibits VPS34 kinase activity and is essential for VPS34 complex stability and membrane attachment (ohashi2021activationmechanismsof pages 3-4). It generates PI3P (not PIP₃), serving autophagy, endosomal trafficking, and lysosomal function rather than growth factor signaling (karolina2012activationregulationand pages 19-22).

### 3.5 Recent Developments (2023–2024)

Recent cryo-EM and HDX-MS studies have revealed new structural details of PI3K complexes, including the identification of allosteric inhibition modes in oncogenic PI3Kα(H1047R) mutants (sheng2024molecularbasisof pages 37-38). A 2024 structural analysis by Dsouza et al. identified a shared mechanism linking pathogenic PIK3R1 variants across cancer, undergrowth syndromes (SHORT syndrome), and overgrowth syndromes (sheng2024molecularbasisof pages 37-38). Xie et al. (2025) further documented that PIK3R1 functions both as a PI3K regulatory subunit and as a scaffold for p110-independent JAK2/STAT3 signaling, confirming its multi-functional nature beyond canonical PI3K regulation (sheng2024molecularbasisof pages 20-23). Nine ongoing clinical trials are investigating compounds targeting mutated PI3K proteins (sheng2024molecularbasisof pages 29-31).

## 4. Taxonomic Scope

Phylogenomic analysis reveals two waves of PI3K diversification (brown2011phylogenomicsofphosphoinositide pages 8-9, brown2011phylogenomicsofphosphoinositide pages 1-3):

- **Class III PI3K (VPS34/VPS15)** is the most ancient PI3K branch, universally conserved across all eukaryotes including yeast, protists, plants, fungi, and animals (brown2011phylogenomicsofphosphoinositide pages 7-8, ohashi2021activationmechanismsof pages 2-3). PIK3C3/VPS34 is the likely ancestral PI3K kinase, with single orthologs in all eukaryotic genomes examined (brown2011phylogenomicsofphosphoinositide pages 7-8).

- **Class I and Class II PI3Ks** are metazoan innovations, arising through gene duplications in early metazoans (brown2011phylogenomicsofphosphoinositide pages 8-9). Class IA regulatory subunits (p85-family) are therefore metazoan-specific, absent from fungi, plants, and most protists.

- **Class IB regulatory subunits** (p101, p84) appear to be even more phylogenetically restricted, predominantly found in vertebrate immune-associated contexts (brown2011phylogenomicsofphosphoinositide pages 8-9).

- **Further diversification** of class I PI3K occurred in the early deuterostome lineage, prior to the emergence of mammals (brown2011phylogenomicsofphosphoinositide pages 8-9).

The wide taxonomic span of PTHR10155 (4,817 taxa) is explained by the inclusion of VPS15, which is pan-eukaryotic. Any GO term specific to class I PI3K biology (e.g., RTK signaling, insulin pathway, immune receptor signaling) would systematically over-annotate the substantial VPS15-containing portion of the family in yeast, plants, and other non-metazoan organisms.

## 5. Over-Annotation Verdict

> Current status: **no InterPro2GO terms are mapped to PTHR10155**, and the available evidence indicates that this absence is appropriate rather than missing annotation. The family is too heterogeneous to support a safe top-level GO mapping across all matched proteins (fox2020classiapi3k pages 1-3, karolina2012activationregulationand pages 19-22, brown2011phylogenomicsofphosphoinositide pages 7-8).
>
> PTHR10155 is **not functionally homogeneous**: it groups class IA PI3K regulatory subunits (p85-family SH2/SH3/BH adaptors that regulate p110α/β/δ in phosphotyrosine/RTK signaling), class IB regulatory subunits (p101/p84 adaptors for p110γ in GPCR/Gβγ signaling), and class III VPS15/PIK3R4 proteins (kinase-like/WD40 scaffolds for VPS34 complexes in autophagy and endomembrane trafficking). These branches differ in domain architecture, activation mechanism, pathway context, and evolutionary distribution; VPS15 is ancient and pan-eukaryotic, whereas class I regulatory subunits are metazoan innovations (fox2020classiapi3k pages 1-3, karolina2012activationregulationand pages 19-22, li2024targetingpi3kfamily pages 2-5, ohashi2021activationmechanismsof pages 3-4, ohashi2021activationmechanismsof pages 2-3, brown2011phylogenomicsofphosphoinositide pages 7-8, brown2011phylogenomicsofphosphoinositide pages 8-9).
>
> Even within class IA, **functional divergence is substantial**: p85α/PIK3R1 is widely described as tumor-suppressive and has distinctive roles in PTEN regulation, ER-stress signaling, and insulin sensitivity, whereas p85β/PIK3R2 is more often associated with pro-oncogenic activity and has distinct metabolic and immune functions. Thus, even a class-IA-wide biological-process mapping would risk overgeneralization (kim2024divergentrolesof pages 7-8, kim2024divergentrolesof pages 1-2, kim2024divergentrolesof pages 3-4, kim2024divergentrolesof pages 4-5, kim2024divergentrolesof pages 6-7, sheng2024molecularbasisof pages 20-23).
>
> **Recommended GO action:** **ACCEPT** the current absence of InterPro2GO mappings for PTHR10155. Any future GO annotation should be attached only to **narrower subfamily-level entries** (for example, class IA-specific, class IB-specific, or VPS15/class III-specific children), not to this top-level family (karolina2012activationregulationand pages 19-22, brown2011phylogenomicsofphosphoinositide pages 7-8, brown2011phylogenomicsofphosphoinositide pages 8-9).
>
> **Recommendation for InterPro:** review whether the current family definition is overly broad for annotation purposes, because it unites proteins with no shared domain architecture or universal biological role—SH2-containing class IA adaptors, structurally distinct class IB adaptors, and VPS15-like WD40/kinase-like class III regulators. If retained as a broad evolutionary family, it should remain unmapped in InterPro2GO and any functional GO terms should be pushed down to child entries (fox2020classiapi3k pages 1-3, karolina2012activationregulationand pages 19-22, ohashi2021activationmechanismsof pages 3-4, brown2011phylogenomicsofphosphoinositide pages 7-8).


*Blockquote: This blockquote summarizes the over-annotation assessment for PTHR10155 and gives the recommended GO-review action. It is useful as a concise decision record showing why the current lack of InterPro2GO mappings should be preserved.*

### Summary Recommendation

| Aspect | Assessment |
|--------|-----------|
| **Current InterPro2GO status** | No GO terms mapped — **correct** |
| **Family functional homogeneity** | **Extremely heterogeneous** — three structurally distinct classes with different domain architectures, upstream signals, pathways, and taxonomic distributions |
| **Within-class divergence** | **Significant** — even p85α vs. p85β show opposing roles (tumor suppressor vs. oncogene; B cell vs. T cell regulation) |
| **Pseudo-enzyme members** | VPS15 contains a kinase-like domain with no confirmed substrates beyond autophosphorylation, likely functioning as a pseudokinase (karolina2012activationregulationand pages 19-22, ohashi2021activationmechanismsof pages 3-4) |
| **GO action for PTHR10155** | **ACCEPT** current absence of InterPro2GO mappings |
| **Recommendation for GO terms** | All GO annotations should be pushed to subfamily-level child entries (e.g., class IA-specific, class IB-specific, VPS15/class III-specific) |
| **Recommendation for InterPro** | Review whether this top-level family grouping is appropriate for annotation purposes; if retained as an evolutionary family, maintain it as unmapped and ensure functional GO terms reside only on child entries |

The absence of InterPro2GO mappings for PTHR10155 is well-justified and should be preserved. This family exemplifies a case where evolutionary relatedness does not imply functional homogeneity, and where any top-level GO annotation would constitute systematic over-annotation across thousands of proteins with fundamentally different biological roles.

References

1. (fox2020classiapi3k pages 1-3): Millie Fox, Helen R. Mott, and Darerca Owen. Class ia pi3k regulatory subunits: p110-independent roles and structures. Biochemical Society Transactions, 48:1397-1417, Jul 2020. URL: https://doi.org/10.1042/bst20190845, doi:10.1042/bst20190845. This article has 103 citations and is from a peer-reviewed journal.

2. (kapeller1994phosphatidylinositol3‐kinase pages 2-3): Rosana Kapeller and Lewis C. Cantley. Phosphatidylinositol 3‐kinase. BioEssays, 16:565-576, Aug 1994. URL: https://doi.org/10.1002/bies.950160810, doi:10.1002/bies.950160810. This article has 829 citations and is from a peer-reviewed journal.

3. (kapeller1994phosphatidylinositol3‐kinase pages 3-5): Rosana Kapeller and Lewis C. Cantley. Phosphatidylinositol 3‐kinase. BioEssays, 16:565-576, Aug 1994. URL: https://doi.org/10.1002/bies.950160810, doi:10.1002/bies.950160810. This article has 829 citations and is from a peer-reviewed journal.

4. (karolina2012activationregulationand pages 19-22): Karolina Błajecka. Activation, regulation and functional characterization of class ii pi3kc2b. ArXiv, 2012. URL: https://doi.org/10.5167/uzh-164197, doi:10.5167/uzh-164197. This article has 0 citations.

5. (fox2020classiapi3k pages 3-4): Millie Fox, Helen R. Mott, and Darerca Owen. Class ia pi3k regulatory subunits: p110-independent roles and structures. Biochemical Society Transactions, 48:1397-1417, Jul 2020. URL: https://doi.org/10.1042/bst20190845, doi:10.1042/bst20190845. This article has 103 citations and is from a peer-reviewed journal.

6. (kim2024divergentrolesof pages 3-4): Cho-Won Kim, Junsik M. Lee, and Sang Won Park. Divergent roles of the regulatory subunits of class ia pi3k. Frontiers in Endocrinology, Jan 2024. URL: https://doi.org/10.3389/fendo.2023.1152579, doi:10.3389/fendo.2023.1152579. This article has 18 citations.

7. (li2024targetingpi3kfamily pages 2-5): Hongyao Li, Xiang Wen, Yueting Ren, Zhichao Fan, Jin Zhang, Gu He, and Leilei Fu. Targeting pi3k family with small-molecule inhibitors in cancer therapy: current clinical status and future directions. Molecular Cancer, Aug 2024. URL: https://doi.org/10.1186/s12943-024-02072-1, doi:10.1186/s12943-024-02072-1. This article has 113 citations and is from a highest quality peer-reviewed journal.

8. (ohashi2021activationmechanismsof pages 3-4): Yohei Ohashi. Activation mechanisms of the vps34 complexes. JournalArticle, Nov 2021. URL: https://doi.org/10.17863/cam.78227, doi:10.17863/cam.78227. This article has 63 citations.

9. (sheng2024molecularbasisof pages 29-31): Zhi Sheng, Patrick Beck, Maegan Gabby, Semhar Habte-Mariam, and Katherine Mitkos. Molecular basis of oncogenic pi3k proteins. Cancers, 17:77, Dec 2024. URL: https://doi.org/10.3390/cancers17010077, doi:10.3390/cancers17010077. This article has 6 citations.

10. (fox2020classiapi3k pages 4-6): Millie Fox, Helen R. Mott, and Darerca Owen. Class ia pi3k regulatory subunits: p110-independent roles and structures. Biochemical Society Transactions, 48:1397-1417, Jul 2020. URL: https://doi.org/10.1042/bst20190845, doi:10.1042/bst20190845. This article has 103 citations and is from a peer-reviewed journal.

11. (fox2020classiapi3k pages 15-16): Millie Fox, Helen R. Mott, and Darerca Owen. Class ia pi3k regulatory subunits: p110-independent roles and structures. Biochemical Society Transactions, 48:1397-1417, Jul 2020. URL: https://doi.org/10.1042/bst20190845, doi:10.1042/bst20190845. This article has 103 citations and is from a peer-reviewed journal.

12. (fox2020classiapi3k pages 16-18): Millie Fox, Helen R. Mott, and Darerca Owen. Class ia pi3k regulatory subunits: p110-independent roles and structures. Biochemical Society Transactions, 48:1397-1417, Jul 2020. URL: https://doi.org/10.1042/bst20190845, doi:10.1042/bst20190845. This article has 103 citations and is from a peer-reviewed journal.

13. (fox2020classiapi3k pages 13-15): Millie Fox, Helen R. Mott, and Darerca Owen. Class ia pi3k regulatory subunits: p110-independent roles and structures. Biochemical Society Transactions, 48:1397-1417, Jul 2020. URL: https://doi.org/10.1042/bst20190845, doi:10.1042/bst20190845. This article has 103 citations and is from a peer-reviewed journal.

14. (fox2020classiapi3k pages 12-13): Millie Fox, Helen R. Mott, and Darerca Owen. Class ia pi3k regulatory subunits: p110-independent roles and structures. Biochemical Society Transactions, 48:1397-1417, Jul 2020. URL: https://doi.org/10.1042/bst20190845, doi:10.1042/bst20190845. This article has 103 citations and is from a peer-reviewed journal.

15. (kim2024divergentrolesof pages 7-8): Cho-Won Kim, Junsik M. Lee, and Sang Won Park. Divergent roles of the regulatory subunits of class ia pi3k. Frontiers in Endocrinology, Jan 2024. URL: https://doi.org/10.3389/fendo.2023.1152579, doi:10.3389/fendo.2023.1152579. This article has 18 citations.

16. (sheng2024molecularbasisof pages 20-23): Zhi Sheng, Patrick Beck, Maegan Gabby, Semhar Habte-Mariam, and Katherine Mitkos. Molecular basis of oncogenic pi3k proteins. Cancers, 17:77, Dec 2024. URL: https://doi.org/10.3390/cancers17010077, doi:10.3390/cancers17010077. This article has 6 citations.

17. (brown2011phylogenomicsofphosphoinositide pages 7-8): James R Brown and Kurt R Auger. Phylogenomics of phosphoinositide lipid kinases: perspectives on the evolution of second messenger signaling and drug discovery. BMC Evolutionary Biology, 11:4-4, Jan 2011. URL: https://doi.org/10.1186/1471-2148-11-4, doi:10.1186/1471-2148-11-4. This article has 132 citations and is from a domain leading peer-reviewed journal.

18. (brown2011phylogenomicsofphosphoinositide pages 8-9): James R Brown and Kurt R Auger. Phylogenomics of phosphoinositide lipid kinases: perspectives on the evolution of second messenger signaling and drug discovery. BMC Evolutionary Biology, 11:4-4, Jan 2011. URL: https://doi.org/10.1186/1471-2148-11-4, doi:10.1186/1471-2148-11-4. This article has 132 citations and is from a domain leading peer-reviewed journal.

19. (kim2024divergentrolesof pages 1-2): Cho-Won Kim, Junsik M. Lee, and Sang Won Park. Divergent roles of the regulatory subunits of class ia pi3k. Frontiers in Endocrinology, Jan 2024. URL: https://doi.org/10.3389/fendo.2023.1152579, doi:10.3389/fendo.2023.1152579. This article has 18 citations.

20. (kim2024divergentrolesof pages 4-5): Cho-Won Kim, Junsik M. Lee, and Sang Won Park. Divergent roles of the regulatory subunits of class ia pi3k. Frontiers in Endocrinology, Jan 2024. URL: https://doi.org/10.3389/fendo.2023.1152579, doi:10.3389/fendo.2023.1152579. This article has 18 citations.

21. (kim2024divergentrolesof pages 6-7): Cho-Won Kim, Junsik M. Lee, and Sang Won Park. Divergent roles of the regulatory subunits of class ia pi3k. Frontiers in Endocrinology, Jan 2024. URL: https://doi.org/10.3389/fendo.2023.1152579, doi:10.3389/fendo.2023.1152579. This article has 18 citations.

22. (ohashi2021activationmechanismsof pages 2-3): Yohei Ohashi. Activation mechanisms of the vps34 complexes. JournalArticle, Nov 2021. URL: https://doi.org/10.17863/cam.78227, doi:10.17863/cam.78227. This article has 63 citations.

23. (sheng2024molecularbasisof pages 19-20): Zhi Sheng, Patrick Beck, Maegan Gabby, Semhar Habte-Mariam, and Katherine Mitkos. Molecular basis of oncogenic pi3k proteins. Cancers, 17:77, Dec 2024. URL: https://doi.org/10.3390/cancers17010077, doi:10.3390/cancers17010077. This article has 6 citations.

24. (fox2020classiapi3k pages 10-12): Millie Fox, Helen R. Mott, and Darerca Owen. Class ia pi3k regulatory subunits: p110-independent roles and structures. Biochemical Society Transactions, 48:1397-1417, Jul 2020. URL: https://doi.org/10.1042/bst20190845, doi:10.1042/bst20190845. This article has 103 citations and is from a peer-reviewed journal.

25. (sheng2024molecularbasisof pages 37-38): Zhi Sheng, Patrick Beck, Maegan Gabby, Semhar Habte-Mariam, and Katherine Mitkos. Molecular basis of oncogenic pi3k proteins. Cancers, 17:77, Dec 2024. URL: https://doi.org/10.3390/cancers17010077, doi:10.3390/cancers17010077. This article has 6 citations.

26. (brown2011phylogenomicsofphosphoinositide pages 1-3): James R Brown and Kurt R Auger. Phylogenomics of phosphoinositide lipid kinases: perspectives on the evolution of second messenger signaling and drug discovery. BMC Evolutionary Biology, 11:4-4, Jan 2011. URL: https://doi.org/10.1186/1471-2148-11-4, doi:10.1186/1471-2148-11-4. This article has 132 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PTHR10155-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR10155-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](PTHR10155-deep-research-falcon_artifacts/artifact-02.md)

## Citations

1. kim2024divergentrolesof pages 3-4
2. karolina2012activationregulationand pages 19-22
3. sheng2024molecularbasisof pages 29-31
4. brown2011phylogenomicsofphosphoinositide pages 8-9
5. sheng2024molecularbasisof pages 20-23
6. kim2024divergentrolesof pages 4-5
7. sheng2024molecularbasisof pages 19-20
8. ohashi2021activationmechanismsof pages 3-4
9. sheng2024molecularbasisof pages 37-38
10. brown2011phylogenomicsofphosphoinositide pages 7-8
11. kim2024divergentrolesof pages 7-8
12. kim2024divergentrolesof pages 1-2
13. kim2024divergentrolesof pages 6-7
14. ohashi2021activationmechanismsof pages 2-3
15. brown2011phylogenomicsofphosphoinositide pages 1-3
16. https://doi.org/10.1042/bst20190845,
17. https://doi.org/10.1002/bies.950160810,
18. https://doi.org/10.5167/uzh-164197,
19. https://doi.org/10.3389/fendo.2023.1152579,
20. https://doi.org/10.1186/s12943-024-02072-1,
21. https://doi.org/10.17863/cam.78227,
22. https://doi.org/10.3390/cancers17010077,
23. https://doi.org/10.1186/1471-2148-11-4,