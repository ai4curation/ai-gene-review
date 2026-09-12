---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-21T20:02:44.317378'
end_time: '2026-06-21T20:17:15.889979'
duration_seconds: 871.57
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR11592
  interpro_name: GLUTATHIONE PEROXIDASE
  interpro_short_name: Not specified
  interpro_type: family
  interpro_integrated: IPR000889
  member_databases: Not specified
  n_proteins: '38772'
  n_taxa: '27727'
  n_subfamilies: '43'
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
  path: PTHR11592-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR11592-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: PTHR11592-deep-research-falcon_artifacts/artifact-02.md
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
- **Accession:** PTHR11592
- **Name:** GLUTATHIONE PEROXIDASE
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** IPR000889
- **Member database signatures:** Not specified
- **Scale:** 38772 proteins across 27727 taxa, 43 subfamilies
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
**PTHR11592 (GLUTATHIONE PEROXIDASE)**, structured to support GO annotation review.

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
- **Accession:** PTHR11592
- **Name:** GLUTATHIONE PEROXIDASE
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** IPR000889
- **Member database signatures:** Not specified
- **Scale:** 38772 proteins across 27727 taxa, 43 subfamilies
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
**PTHR11592 (GLUTATHIONE PEROXIDASE)**, structured to support GO annotation review.

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


# Comprehensive Research Report: InterPro Entry PTHR11592 (GLUTATHIONE PEROXIDASE) for GO Annotation Review

## Executive Summary

PTHR11592 is a PANTHER family-level entry representing the glutathione peroxidase (GPX) protein family, encompassing 38,772 proteins across 27,727 taxa with 43 subfamilies. Critically, **this entry currently has no InterPro2GO mappings**, which is appropriate given the extreme functional heterogeneity of the family. This report provides comprehensive evidence that the GPX family exhibits massive functional divergence spanning classical antioxidant peroxide scavenging, specialized membrane lipid reduction, ferroptosis suppression, protein folding in the endoplasmic reticulum, and tissue-specific reproductive functions—precluding broad family-level GO annotation.

---

## 1. Family Definition and Biochemistry

### 1.1 Conserved Catalytic Mechanism

The glutathione peroxidase family is defined by a conserved catalytic **tetrad** comprising selenocysteine (Sec) or cysteine (Cys), glutamine (Gln), tryptophan (Trp), and asparagine (Asn) residues (cubasgaona2020tetrahymenaglutathioneperoxidase pages 1-3, brigeliusflohe2020regulatoryphenomenain pages 4-6). This tetrad enables the reduction of hydroperoxides through a ping-pong catalytic mechanism (brigeliusflohe2020regulatoryphenomenain pages 4-6, chaudiere2023biologicalandcatalytic pages 1-2).

In **selenocysteine-based GPXs** (mammalian GPX1-4 and GPX6 in humans), the catalytic cycle proceeds as follows: (1) the selenolate (Se⁻) nucleophilically attacks the peroxide bond (ROOH) to form selenic acid (Se-OH), (2) the first glutathione (GSH) molecule reduces Se-OH to a selenyl-glutathione intermediate (Se-SG), and (3) a second GSH molecule regenerates the active selenolate while releasing oxidized glutathione (GSSG) (pei2023researchprogressof pages 1-2, pei2023researchprogressof pages 2-3, chaudiere2023biologicalandcatalytic pages 1-2). The extraordinary catalytic efficiency of Sec-based GPXs—exceeding low-molecular-weight thiols by 4–7 orders of magnitude—derives from concerted electrophilic and nucleophilic attack on the hydroperoxide, enabled by the selenolate's superior nucleophilicity and reversibility compared to cysteine (brigeliusflohe2020regulatoryphenomenain pages 4-6, chaudiere2023biologicalandcatalytic pages 1-2).

In **cysteine-based GPXs** (mammalian GPX5, GPX7, GPX8), the mechanism is analogous but relies on a cysteine thiolate, often forming disulfide intermediates that require alternative reducing partners such as thioredoxin, protein disulfide isomerase (PDI), or other redoxins rather than classical GSH (pei2023researchprogressof pages 1-2, brigeliusflohe2020regulatoryphenomenain pages 1-4, cubasgaona2020tetrahymenaglutathioneperoxidase pages 1-3, santos2025thefamilyof pages 1-2).

### 1.2 Structural Features

The GPX family exhibits **two major quaternary structures**: homotetramers (GPX1, GPX2, GPX3, GPX5, GPX6) and monomers (GPX4, GPX7, GPX8) (weaver2022theselenoproteinglutathione pages 2-3, pei2023researchprogressof pages 3-6). This structural divergence correlates with substrate specificity: monomeric GPX4 uniquely reduces complex membrane lipid hydroperoxides, whereas tetrameric GPXs typically act on soluble H₂O₂ and small-molecule peroxides (chaudiere2023biologicalandcatalytic pages 10-11). The GPX fold itself belongs to the thiol peroxidase superfamily but is evolutionarily distinct from catalases and peroxiredoxins (hewitt2023antioxidantenzymesthat pages 1-2, hewitt2023antioxidantenzymesthat pages 3-4).

### 1.3 Substrate Specificity

GPXs reduce a range of substrates including hydrogen peroxide (H₂O₂), organic hydroperoxides, and—uniquely for GPX4—phospholipid hydroperoxides, cholesterol hydroperoxides, and cholesteryl ester hydroperoxides embedded in membranes and lipoproteins (pei2023researchprogressof pages 1-2, weaver2022theselenoproteinglutathione pages 2-3, chaudiere2023biologicalandcatalytic pages 10-11). However, substrate preference varies dramatically across subfamilies (see Section 3).

---

## 2. InterPro2GO Mapping Appropriateness

### 2.1 Current Mapping Status

**PTHR11592 has NO InterPro2GO terms currently mapped**, as stated in the provided InterPro API data. This absence is scientifically sound and should be maintained.

### 2.2 Recommended Annotation Policy

> PTHR11592 is a PANTHER **family** entry rather than a domain or repeat, so in principle it can support whole-protein GO annotations; however, the evidence indicates that the glutathione peroxidase family is **not functionally homogeneous** across all matched proteins, because it spans classical soluble hydroperoxide-reducing enzymes, membrane-lipid peroxide reductases, epididymal/sperm-protective proteins, and ER-localized oxidative protein-folding factors (pei2023researchprogressof pages 1-2, brigeliusflohe2020regulatoryphenomenain pages 1-4, hewitt2023antioxidantenzymesthat pages 1-2, cubasgaona2020tetrahymenaglutathioneperoxidase pages 1-3, chaudiere2023biologicalandcatalytic pages 10-11, mi2020pantherversion16 pages 1-2).
>
> For family-level InterPro2GO policy, only **very broad catalytic terms** are plausibly safe, such as high-level oxidoreductase/peroxidase activity terms, and even these should be used cautiously because reductant usage, substrate range, and catalytic chemistry vary across clades and subfamilies; by contrast, terms such as **ferroptosis-related function** are GPX4-specific, **protein folding / oxidative folding in the ER** applies to GPX7/GPX8, **spermatogenesis or sperm protection** is GPX5-associated, **extracellular region** is not family-wide because it mainly reflects GPX3, and tissue- or compartment-specific annotations are clearly over-broad at the parent-family level (pei2023researchprogressof pages 1-2, weaver2022theselenoproteinglutathione pages 2-3, brigeliusflohe2020regulatoryphenomenain pages 1-4, pei2023researchprogressof pages 3-6, chaudiere2023biologicalandcatalytic pages 10-11).
>
> Additional properties that should **not** be propagated from PTHR11592 to all matches include **selenocysteine-based catalysis versus cysteine-based catalysis**, **glutathione dependence versus alternative reductants/redoxin partners**, and **tetrameric versus monomeric quaternary structure**, because these vary substantially among GPX1-8 and across non-vertebrate homologs (weaver2022theselenoproteinglutathione pages 2-3, cubasgaona2020tetrahymenaglutathioneperoxidase pages 1-3, chaudiere2023biologicalandcatalytic pages 1-2, chaudiere2023biologicalandcatalytic pages 10-11).
>
> Annotation should therefore be pushed, wherever possible, to **subfamily-level PANTHER nodes** corresponding to the major mammalian GPX types (GPX1-GPX8) or to narrower evolutionary groups, rather than attached to the broad parent family PTHR11592; this is especially important because the broader GPX family extends across vertebrates, invertebrates, plants, fungi, protists, bacteria, and archaea, and many lineage-specific properties in the literature are vertebrate- or mammal-specific rather than universal across the family (hewitt2023antioxidantenzymesthat pages 1-2, cubasgaona2020tetrahymenaglutathioneperoxidase pages 1-3, santos2025thefamilyof pages 1-2, mi2020pantherversion16 pages 2-3, mi2020pantherversion16 pages 1-2).
>
> In short: **PTHR11592 should support only conservative, cross-family core enzymatic annotations, while subfamily-specific biological process, cellular component, substrate-specific, structural, and taxon-restricted terms should be withheld from the parent family and assigned only to validated child groups** (brigeliusflohe2020regulatoryphenomenain pages 1-4, hewitt2023antioxidantenzymesthat pages 1-2, chaudiere2023biologicalandcatalytic pages 10-11, mi2020pantherversion16 pages 1-2).


*Blockquote: This blockquote summarizes why PTHR11592 can, in principle, support whole-protein GO terms but should be annotated conservatively because the glutathione peroxidase family is highly functionally divergent. It highlights which term types are broadly defensible and which would over-annotate if applied at the parent-family level.*

**Safe family-level annotations** (if any are to be added):
- **Molecular Function (MF):** Broad oxidoreductase or peroxidase activity terms (e.g., GO:0016491 oxidoreductase activity, GO:0004601 peroxidase activity) are defensible but should be applied cautiously, as even these vary in mechanism (Sec vs. Cys, GSH vs. thioredoxin/PDI reducing partners).

**Terms that MUST NOT be applied at PTHR11592 family level** (subfamily-specific):
- **Ferroptosis suppression** (GO:0140767 negative regulation of ferroptosis): GPX4-specific (brigeliusflohe2020regulatoryphenomenain pages 1-4, chaudiere2023biologicalandcatalytic pages 10-11)
- **Protein folding / oxidative folding in ER**: GPX7 and GPX8 only (pei2023researchprogressof pages 1-2, brigeliusflohe2020regulatoryphenomenain pages 1-4, pei2023researchprogressof pages 3-6)
- **Spermatogenesis / sperm protection**: GPX5-specific (pei2023researchprogressof pages 1-2, weaver2022theselenoproteinglutathione pages 2-3)
- **Extracellular region** (GO:0005576): Predominantly GPX3; not family-wide (pei2023researchprogressof pages 2-3, chaudiere2023biologicalandcatalytic pages 10-11)
- **Selenocysteine-containing / selenium binding**: False for GPX5, GPX7, GPX8, and many non-vertebrate homologs (pei2023researchprogressof pages 1-2, weaver2022theselenoproteinglutathione pages 2-3, cubasgaona2020tetrahymenaglutathioneperoxidase pages 1-3)
- **Glutathione binding / GSH-dependent catalysis**: Many plant, fungal, and ciliate GPXs use thioredoxin or other reductants (cubasgaona2020tetrahymenaglutathioneperoxidase pages 1-3, santos2025thefamilyof pages 1-2)
- **Tetrameric structure**: False for GPX4, GPX7, GPX8 (weaver2022theselenoproteinglutathione pages 2-3, pei2023researchprogressof pages 3-6)
- **Tissue-specific localizations** (e.g., gastrointestinal epithelium for GPX2, kidney tubules for GPX3 production, epididymis for GPX5): All subfamily-specific

### 2.3 Recommendation for InterPro

**The PANTHER subfamily structure (43 subfamilies reported in PTHR11592) should be leveraged for GO annotation.** Ideally, GO terms should be assigned to child PANTHER subfamilies corresponding to the well-characterized mammalian GPX1–GPX8 types, and potentially to orthologous groups in plants, fungi, and other clades. This approach prevents systematic over-annotation of proteins that share the GPX fold but diverge in catalytic chemistry, localization, biological process participation, and taxonomic scope (mi2020pantherversion16 pages 2-3, mi2020pantherversion16 pages 1-2).

---

## 3. Functional Divergence Across the Family

The glutathione peroxidase family exhibits **extreme functional heterogeneity**, with at least eight distinct mammalian subfamilies displaying neo-functionalized or sub-functionalized roles.

| Subfamily | Catalytic residue | Quaternary structure | Subcellular localization | Primary substrates / reducing partner | Key distinguishing functional properties | Tissue / cell type specificity | Evidence |
|---|---|---|---|---|---|---|---|
| GPX1 | Selenocysteine (Sec) | Homotetramer | Cytoplasm and mitochondria | H2O2 and soluble low-molecular hydroperoxides; reduced by GSH | Ubiquitous canonical antioxidant GPX; protects against systemic oxidant challenge; modulates redox signaling by limiting hydroperoxide-dependent phosphatase inactivation and downstream phosphorylation cascades | Broadly expressed; among the most abundant mammalian selenoproteins | (pei2023researchprogressof pages 1-2, weaver2022theselenoproteinglutathione pages 2-3, pei2023researchprogressof pages 2-3, brigeliusflohe2020regulatoryphenomenain pages 6-8) |
| GPX2 | Selenocysteine (Sec) | Homotetramer | Predominantly gastrointestinal epithelium | Hydroperoxides including H2O2 and tert-butyl hydroperoxide; reduced by GSH | GI-enriched first-line defense against dietary and microbiota-associated oxidants; functionally distinct from GPX1 by strong epithelial/tissue specificity | Highest in esophageal and intestinal epithelial cells, especially crypt/villus regions | (pei2023researchprogressof pages 1-2, pei2023researchprogressof pages 2-3, pei2023researchprogressof pages 3-6) |
| GPX3 | Selenocysteine (Sec) | Homotetramer | Secreted; plasma / extracellular space | H2O2 and lipid peroxides; in vitro uses GSH, but extracellularly likely uses alternative thiols/redoxin systems because plasma GSH is low | Only known secreted Sec-containing human GPX; implicated in maintaining extracellular redox balance, nitric oxide bioavailability, and antithrombotic protection; may show context-dependent tumor suppressive or pro-metastatic roles | Mature protein produced mainly by renal tubular epithelial cells and secreted into blood | (pei2023researchprogressof pages 2-3, chaudiere2023biologicalandcatalytic pages 10-11) |
| GPX4 | Selenocysteine (Sec) | Monomer | Cytosol, mitochondria, nucleus; also associated with membranes and lipoproteins | Complex lipid hydroperoxides including phospholipids, cholesterol and cholesteryl ester hydroperoxides; less efficient on H2O2 / t-BuOOH than GPX1 | Functionally unique within family: directly reduces complex membrane lipids, suppresses lipid peroxidation, is a central inhibitor of ferroptosis, and in sperm maturation can use protein thiols to promote mitochondrial sheath formation; essential for embryonic development and male fertility | Cytosolic form in somatic tissues; mitochondrial and nuclear forms enriched in testis / sperm | (pei2023researchprogressof pages 1-2, weaver2022theselenoproteinglutathione pages 2-3, brigeliusflohe2020regulatoryphenomenain pages 1-4, pei2023researchprogressof pages 3-6, chaudiere2023biologicalandcatalytic pages 10-11) |
| GPX5 | Cysteine (Cys) | Homotetramer | Secreted in epididymis / associated with sperm environment | Peroxides, especially those threatening sperm membranes; evidence indicates Cys-based GPX superfamily member, often described as relying on thioredoxin-like reducing systems rather than classical GSH-dependent Sec chemistry | First discovered mammalian Cys-based GPX; specialized protection of sperm membranes from oxidative damage and lipid peroxidation; not a broadly acting antioxidant across tissues | Epididymis; strongly associated with spermatozoa protection and male fertility | (pei2023researchprogressof pages 1-2, weaver2022theselenoproteinglutathione pages 2-3, pei2023researchprogressof pages 3-6) |
| GPX6 | Sec in humans; Cys in rodents | Homotetramer | Not well resolved in humans; olfactory epithelium emphasized in rodents | Not well defined; presumed hydroperoxide reduction like Sec-GPXs, but physiology remains less characterized | Clear lineage-specific divergence in catalytic chemistry (human Sec versus rodent Cys), making it a poor universal proxy for catalytic mechanism across mammals | Expressed in embryos and adult olfactory epithelium; rodent olfactory epithelial enrichment noted | (pei2023researchprogressof pages 1-2, weaver2022theselenoproteinglutathione pages 2-3) |
| GPX7 | Cysteine (Cys) | Monomer | Endoplasmic reticulum | Mild classical GPX activity toward H2O2; reoxidation/recycling linked to protein disulfide isomerase (PDI) and ER oxidative folding machinery rather than canonical GSH-centered catalysis | Strongly diverged from classical antioxidant GPXs: acts in ER oxidative protein folding, senses/transmits redox equivalents to other thiols, and helps maintain ER proteostasis | ER-localized; broadly linked to secretory pathway / protein-folding cells rather than a single tissue | (pei2023researchprogressof pages 1-2, weaver2022theselenoproteinglutathione pages 2-3, brigeliusflohe2020regulatoryphenomenain pages 1-4, hewitt2023antioxidantenzymesthat pages 1-2, pei2023researchprogressof pages 3-6) |
| GPX8 | Cysteine (Cys) with catalytic tetrad divergence (Gln replaced by Ser) | Monomer | Endoplasmic reticulum, membrane-associated | Mild peroxidase activity in ER redox environment; linked to PDI/oxidative folding systems rather than classical soluble GSH-dependent peroxide detoxification | Highly specialized ER paralog involved in oxidative protein folding and ER redox control; additionally implicated in ER Ca2+ regulation; catalytic-site divergence underscores functional neo-specialization within family | ER-localized; associated with ER stress / secretory pathway contexts | (pei2023researchprogressof pages 1-2, weaver2022theselenoproteinglutathione pages 2-3, cubasgaona2020tetrahymenaglutathioneperoxidase pages 1-3, pei2023researchprogressof pages 3-6) |


*Table: This table compares GPX1-GPX8 across catalytic chemistry, structure, localization, substrates, and specialized biology. It highlights the strong functional divergence within the glutathione peroxidase family that is critical for GO annotation review.*

### 3.1 Classical Antioxidant GPXs

**GPX1, GPX2, and GPX3** represent the canonical selenocysteine-based, GSH-dependent antioxidant paradigm, but even these differ markedly in tissue expression and physiological context:
- **GPX1** is ubiquitous in cytoplasm and mitochondria, serving as the primary systemic antioxidant GPX; it also modulates redox signaling by limiting H₂O₂-mediated phosphatase inactivation (pei2023researchprogressof pages 1-2, pei2023researchprogressof pages 2-3, brigeliusflohe2020regulatoryphenomenain pages 6-8).
- **GPX2** is gastrointestinal epithelium-specific, forming the first barrier against dietary/microbial hydroperoxides and showing dual roles in inflammation-induced carcinogenesis (anti-carcinogenic early, pro-tumorigenic late) (brigeliusflohe2020regulatoryphenomenain pages 1-4, pei2023researchprogressof pages 3-6).
- **GPX3** is the only known secreted human selenoprotein GPX, produced by renal tubular epithelial cells and functioning extracellularly; its substrates in plasma likely include alternative thiols due to low extracellular GSH (pei2023researchprogressof pages 2-3, chaudiere2023biologicalandcatalytic pages 10-11).

### 3.2 Specialized Lipid Peroxide Reductase: GPX4

**GPX4** is functionally unique within the family: it is monomeric, reduces complex membrane lipid hydroperoxides (phospholipids, cholesterol, cholesteryl esters) inefficiently handled by other GPXs, and is the central inhibitor of **ferroptosis**, a lipid-peroxidation-driven form of regulated cell death (pei2023researchprogressof pages 1-2, weaver2022theselenoproteinglutathione pages 2-3, brigeliusflohe2020regulatoryphenomenain pages 1-4, chaudiere2023biologicalandcatalytic pages 10-11). GPX4 is essential for embryonic development; homozygous knockout is embryonic lethal, and even heterozygous or catalytically compromised mutants show male infertility due to defects in sperm mitochondrial sheath formation (chaudiere2023biologicalandcatalytic pages 10-11). GPX4 exists in cytosolic, mitochondrial, and nuclear isoforms, with tissue-specific expression patterns (chaudiere2023biologicalandcatalytic pages 10-11).

### 3.3 Cysteine-Based ER Protein-Folding GPXs

**GPX7 and GPX8** are ER-resident, cysteine-based GPXs with **low classical peroxidase activity**; instead, they function in **oxidative protein folding** by acting as redox-folding enzymes that interact with protein disulfide isomerase (PDI) and ER oxidoreductin 1 (Ero1) (pei2023researchprogressof pages 1-2, brigeliusflohe2020regulatoryphenomenain pages 1-4, pei2023researchprogressof pages 3-6). GPX8 additionally regulates ER Ca²⁺ homeostasis via interaction with the SERCA pump (pei2023researchprogressof pages 3-6). Notably, GPX8's catalytic tetrad diverges from the family consensus: Gln is replaced by Ser (cubasgaona2020tetrahymenaglutathioneperoxidase pages 1-3), underscoring functional neo-specialization.

### 3.4 Sperm-Protective GPX5

**GPX5** is the first-discovered mammalian cysteine-based GPX, secreted in the epididymis to protect spermatozoa from oxidative damage during maturation (pei2023researchprogressof pages 1-2, weaver2022theselenoproteinglutathione pages 2-3). Its reducing partner is likely thioredoxin-like rather than GSH, reflecting mechanistic divergence from classical GPXs (cubasgaona2020tetrahymenaglutathioneperoxidase pages 1-3).

### 3.5 GPX6: Lineage-Specific Catalytic Chemistry

**GPX6** is selenocysteine-based in humans but cysteine-based in rodents, illustrating lineage-specific loss of selenocysteine incorporation (pei2023researchprogressof pages 1-2, weaver2022theselenoproteinglutathione pages 2-3). This divergence highlights that even "selenocysteine-containing GPX" is not a family-wide property.

### 3.6 Catalytically Dead or Divergent Members

Evidence from plants, ciliates, and fungi indicates that many GPX family members have lost classical peroxidase activity or shifted to alternative electron donors (thioredoxin, trypanothione) (cubasgaona2020tetrahymenaglutathioneperoxidase pages 1-3, santos2025thefamilyof pages 1-2). In ciliates such as *Tetrahymena*, extensive intra- and interspecific gene duplications have produced multiple isoforms, many with Sec replaced by Cys and SECIS element anomalies, suggesting ongoing evolutionary flux in catalytic mechanism (cubasgaona2020tetrahymenaglutathioneperoxidase pages 1-3).

---

## 4. Taxonomic Scope

The GPX family occurs broadly across the tree of life, but its composition and catalytic features vary drastically by taxonomic group.

| Major taxonomic group | Presence / abundance of GPX family members | Sec vs Cys GPX features | Notable evolutionary insights | Special notes / group-specific variants |
|---|---|---|---|---|
| Bacteria | GPX family members occur in bacteria, but distribution is patchy rather than universal; bacterial and eukaryotic GPXs are both recognized, with many non-animal GPX-like proteins falling outside the vertebrate 8-member scheme (cubasgaona2020tetrahymenaglutathioneperoxidase pages 1-3, chaudiere2023biologicalandcatalytic pages 1-2, mi2020pantherversion16 pages 2-3) | Both Sec-containing and Cys-containing GPXs exist across life; Sec is not universal, and many GPX-like enzymes use Cys instead of Sec (cubasgaona2020tetrahymenaglutathioneperoxidase pages 1-3, chaudiere2023biologicalandcatalytic pages 1-2) | GPX is not the only peroxide-detoxification solution in bacteria, and bacterial forms contribute to the broader evolutionary backdrop from which eukaryotic GPXs diversified; PANTHER sampling includes bacterial genomes but the vertebrate-style subfamily nomenclature does not generalize to all bacterial homologs (chaudiere2023biologicalandcatalytic pages 1-2, mi2020pantherversion16 pages 2-3, mi2020pantherversion16 pages 1-2) | Some bacterial selenoenzymes illustrate the catalytic advantages of Sec, but bacterial GPXs should not be assumed to match mammalian substrate preferences or GO biology one-to-one (chaudiere2023biologicalandcatalytic pages 1-2) |
| Archaea | Archaea contain fewer documented GPX examples than bacteria/eukaryotes in the gathered literature; antioxidant systems in archaea often emphasize other enzymes, though putative GPX genes are reported in some archaeal contexts (mi2020pantherversion16 pages 2-3) | Available evidence supports that Sec biology is not universal in archaea; GPX-like antioxidant capacity, where present, should not be assumed to be Sec-based or glutathione-centered in the mammalian sense (chaudiere2023biologicalandcatalytic pages 1-2, mi2020pantherversion16 pages 2-3) | Archaeal sampling in PANTHER is limited relative to other kingdoms, reinforcing caution against broad family-level functional assumptions across all archaeal homologs (mi2020pantherversion16 pages 2-3) | Archaeal peroxide defense is often centered on non-GPX systems in reviews of archaeal redox biology, so GPX annotations at broad family level may be especially uncertain outside well-characterized lineages (mi2020pantherversion16 pages 2-3) |
| Protists / Protozoa | GPXs are widespread in protists; ciliates such as *Tetrahymena* encode multiple GPX paralogs/isoforms, indicating lineage-specific expansions (cubasgaona2020tetrahymenaglutathioneperoxidase pages 1-3, mi2020pantherversion16 pages 2-3) | In ciliates, many GPXs have replaced Sec with Cys; some retain SECIS-related anomalies, showing that Sec usage has been repeatedly modified during evolution (cubasgaona2020tetrahymenaglutathioneperoxidase pages 1-3) | Extensive intra- and interspecific duplications occurred in ciliates, producing multiple GPX isoforms; the ancestral state is inferred to have been selenoprotein-based, followed by frequent Sec-to-Cys replacement (cubasgaona2020tetrahymenaglutathioneperoxidase pages 1-3) | Many ciliate GPXs are described as PHGPx-like and may differ in electron donor usage or catalytic details; this supports substantial functional heterogeneity within non-vertebrate eukaryotic GPXs (cubasgaona2020tetrahymenaglutathioneperoxidase pages 1-3) |
| Fungi | Fungi possess GPX-like proteins, but the gathered literature emphasizes that many non-animal/fungal GPXs use alternative reductants and should not automatically be treated as classical GSH-dependent enzymes (cubasgaona2020tetrahymenaglutathioneperoxidase pages 1-3, mi2020pantherversion16 pages 2-3) | Many non-Sec fungal GPXs are Cys-based and may prefer thioredoxin/redoxin systems rather than glutathione (cubasgaona2020tetrahymenaglutathioneperoxidase pages 1-3) | Fungal GPXs support the broader point that the GPX fold/family diversified extensively, with multiple departures from the canonical mammalian Sec-GSH paradigm (cubasgaona2020tetrahymenaglutathioneperoxidase pages 1-3, mi2020pantherversion16 pages 1-2) | Fungal homologs are relevant to family evolution, but they are poor support for vertebrate-specific GO terms such as ferroptosis suppression or ER oxidative folding unless supported by a narrower child family (cubasgaona2020tetrahymenaglutathioneperoxidase pages 1-3, mi2020pantherversion16 pages 1-2) |
| Plants | Plants have numerous GPX family members, often as multigene families with stress-responsive expansion and compartment-specific isoforms (santos2025thefamilyof pages 1-2, mi2020pantherversion16 pages 2-3) | Plant GPXs are largely Cys-based rather than Sec-based, and many use thioredoxin rather than glutathione as reducing substrate (cubasgaona2020tetrahymenaglutathioneperoxidase pages 1-3, santos2025thefamilyof pages 1-2) | Plant GPXs illustrate major functional divergence from mammalian GPXs; they participate in stress signaling, pathogen responses, and compartment-specific ROS control rather than fitting neatly into the mammalian GPX1-8 framework (santos2025thefamilyof pages 1-2) | Plant GPXs act in chloroplasts, mitochondria, peroxisomes, apoplast, nucleus, and cytosol, and can function as H2O2 sensors/transmitters in addition to antioxidant enzymes (santos2025thefamilyof pages 1-2) |
| Invertebrate animals | GPXs occur broadly across metazoans, including sponges, cnidarians, annelids, arthropods, nematodes, and echinoderms, but copy number varies substantially by lineage (hewitt2023antioxidantenzymesthat pages 1-2, hewitt2023antioxidantenzymesthat pages 3-4) | Across metazoans, only the cysteine-dependent GPX7 subfamily is deeply conserved from sponges to mammals; Sec-containing vertebrate-type GPXs are not universally conserved across animals (hewitt2023antioxidantenzymesthat pages 1-2) | GPX is described as the most evolutionarily recent of the three major H2O2-targeting antioxidant families in animals, and its subfamily composition is much less conserved than catalases or peroxiredoxins; metazoan-wide conservation is strongest for GPX7 (hewitt2023antioxidantenzymesthat pages 1-2) | Sponge genomes encode GPX but typically few copies; nematodes and some other invertebrates show broader GPX repertoires, including phospholipid hydroperoxide GPX-like forms that evolved independently relative to mammals (hewitt2023antioxidantenzymesthat pages 1-2, hewitt2023antioxidantenzymesthat pages 3-4) |
| Vertebrate animals | Vertebrates have the best-characterized GPX repertoire, including the 8 mammalian subfamilies GPX1-GPX8; humans encode 8 GPXs, with varying localization and substrate specificity (pei2023researchprogressof pages 1-2, weaver2022theselenoproteinglutathione pages 2-3, hewitt2023antioxidantenzymesthat pages 1-2) | GPX1-4 and GPX6 are Sec-containing in mammals (with rodent GPX6 as a Cys exception), whereas GPX5, GPX7, and GPX8 are Cys-based; thus even within vertebrates Sec is not universal (pei2023researchprogressof pages 1-2, weaver2022theselenoproteinglutathione pages 2-3, brigeliusflohe2020regulatoryphenomenain pages 1-4) | The mammalian 8-subfamily system is a vertebrate-specific functional classification and should not be projected across all GPX homologs in other kingdoms; vertebrates also show major neo-functionalization, e.g. GPX4 for membrane lipids/ferroptosis and GPX7/8 for ER oxidative folding (pei2023researchprogressof pages 1-2, weaver2022theselenoproteinglutathione pages 2-3, brigeliusflohe2020regulatoryphenomenain pages 1-4, chaudiere2023biologicalandcatalytic pages 10-11) | Vertebrate specializations include secreted GPX3, sperm/epididymal GPX5, human-vs-rodent divergence in GPX6 catalytic residue, and ER-resident GPX7/8 with low classical GPX activity but specialized redox-folding roles (pei2023researchprogressof pages 1-2, weaver2022theselenoproteinglutathione pages 2-3, chaudiere2023biologicalandcatalytic pages 10-11) |


*Table: This table summarizes how glutathione peroxidases are distributed and diversified across major taxonomic groups. It highlights why broad GO annotation for the entire GPX family is risky: Sec is not universal, many homologs are Cys-based, and the mammalian GPX1-8 scheme is vertebrate-specific.*

### 4.1 Bacteria and Archaea

GPXs are present in some bacteria but are not universal; bacterial antioxidant systems often emphasize catalases and peroxiredoxins over GPX (chaudiere2023biologicalandcatalytic pages 1-2, mi2020pantherversion16 pages 2-3). Archaea show limited documented GPX representation in the literature, and selenocysteine usage is not universal in these domains (chaudiere2023biologicalandcatalytic pages 1-2, mi2020pantherversion16 pages 2-3). PANTHER sampling of bacterial and archaeal genomes is limited relative to eukaryotes (mi2020pantherversion16 pages 1-2).

### 4.2 Protists and Fungi

**Protists** such as ciliates encode multiple GPX isoforms with extensive lineage-specific duplications; many have replaced selenocysteine with cysteine, and some retain anomalous SECIS elements despite Cys-based catalysis (cubasgaona2020tetrahymenaglutathioneperoxidase pages 1-3). **Fungi** possess GPX-like proteins, but many are Cys-based and prefer thioredoxin over glutathione (cubasgaona2020tetrahymenaglutathioneperoxidase pages 1-3).

### 4.3 Plants

Plants have large GPX families (often 5–10+ genes per genome) distributed across chloroplasts, mitochondria, peroxisomes, cytosol, nucleus, and apoplast (santos2025thefamilyof pages 1-2). Plant GPXs are **predominantly cysteine-based** and often use thioredoxin as reductant; they function not only as antioxidants but also as H₂O₂ sensors and transmitters in stress signaling, pathogen defense, and ABA pathways (santos2025thefamilyof pages 1-2). The plant GPX repertoire does not map onto the mammalian GPX1–8 framework (santos2025thefamilyof pages 1-2).

### 4.4 Invertebrate Animals

Across metazoans, GPXs are widespread but evolutionarily variable. Among the major H₂O₂-targeting antioxidant families (catalases, peroxiredoxins, glutathione peroxidases), **GPX is the most recent to arise** and shows the **least conservation** in subfamily composition (hewitt2023antioxidantenzymesthat pages 1-2). Notably, **only GPX7 (cysteine-based) is conserved from sponges to mammals**; selenocysteine-based GPXs are not universal across animals (hewitt2023antioxidantenzymesthat pages 1-2, hewitt2023antioxidantenzymesthat pages 3-4). Sponges encode 1–3 GPXs, nematodes show broader expansion, and some invertebrate GPXs resemble phospholipid hydroperoxide GPXs but evolved independently of mammalian GPX4 (hewitt2023antioxidantenzymesthat pages 1-2, hewitt2023antioxidantenzymesthat pages 3-4).

### 4.5 Vertebrate Animals

The **8-subfamily mammalian system (GPX1–GPX8) is vertebrate-specific** and should not be projected onto non-vertebrate homologs (pei2023researchprogressof pages 1-2, weaver2022theselenoproteinglutathione pages 2-3, mi2020pantherversion16 pages 1-2). Even within vertebrates, catalytic residue divergence occurs (human vs. rodent GPX6) (weaver2022theselenoproteinglutathione pages 2-3).

### 4.6 Taxonomic Summary

The GPX family is **ancient but functionally heterogeneous**. Selenocysteine is not universal; cysteine-based variants dominate in plants, fungi, and many invertebrates. Substrate preference (H₂O₂ vs. lipid peroxides), reducing partner (GSH vs. thioredoxin vs. PDI), quaternary structure, and subcellular localization all vary across taxa. **GO terms describing vertebrate-specific processes (ferroptosis, ER protein folding, sperm maturation) are taxonomically restricted and inappropriate at the family level.**

---

## 5. Over-Annotation Verdict and Recommendations

### 5.1 Verdict

**The absence of InterPro2GO mappings for PTHR11592 is scientifically appropriate and should be maintained.** The glutathione peroxidase family exhibits extreme functional divergence that precludes meaningful broad GO annotation. Applying family-level GO terms would systematically over-annotate proteins across the following axes:

1. **Biological Process:** Ferroptosis suppression (GPX4), oxidative protein folding (GPX7/8), spermatogenesis (GPX5), and inflammation modulation (GPX2) are subfamily-specific.
2. **Cellular Component:** Extracellular (GPX3), ER (GPX7/8), mitochondrial sheath (GPX4-mitochondrial isoform), and tissue-specific localizations are not family-wide.
3. **Molecular Function:** Selenocysteine vs. cysteine catalysis, GSH vs. thioredoxin/PDI reducing partners, and substrate range (soluble peroxides vs. membrane lipids) vary across subfamilies and taxa.
4. **Taxonomic Scope:** The mammalian 8-subfamily framework is vertebrate-specific; applying it to plant, fungal, or bacterial homologs is incorrect.

### 5.2 Recommended GO Action Pattern

**For PTHR11592 (parent family):**
- **ACCEPT** the current absence of InterPro2GO mappings.
- **IF** any mappings are added in the future, limit to **extremely broad molecular function terms** such as GO:0016491 (oxidoreductase activity) or GO:0004601 (peroxidase activity), applied as **KEEP_AS_NON_CORE** annotations with explicit caveats about subfamily variability.
- **MARK_AS_OVER_ANNOTATED / REMOVE** any subfamily-specific biological process, cellular component, or detailed catalytic mechanism terms applied at the parent level.

**For PANTHER subfamilies (e.g., corresponding to GPX1, GPX2, GPX3, GPX4, GPX5, GPX6, GPX7, GPX8):**
- **MODIFY-to-specific:** Push subfamily-specific GO terms down to the appropriate child entries.
  - GPX1 → cytoplasmic/mitochondrial antioxidant, redox signaling modulation
  - GPX2 → GI epithelium, inflammation-carcinogenesis axis
  - GPX3 → secreted/extracellular, plasma antioxidant
  - GPX4 → ferroptosis inhibition, membrane lipid peroxide reduction, male fertility
  - GPX5 → epididymal secretion, sperm protection
  - GPX6 → olfactory epithelium (with human/rodent Sec/Cys divergence noted)
  - GPX7 → ER oxidative protein folding, PDI interaction
  - GPX8 → ER oxidative folding, ER Ca²⁺ regulation

**For InterPro curation:**
- **Recommend** that InterPro prioritize mapping GO terms to the 43 existing subfamilies of PTHR11592 rather than the parent.
- **Recommend** coordination with PANTHER curators to ensure subfamily-level HMMs accurately distinguish GPX1–8 orthologs in vertebrates and functionally equivalent groups in plants, fungi, and other taxa.

### 5.3 Experimental vs. Computational Evidence

The functional assignments in this report are based on extensive experimental literature from 2020–2025, including:
- **Structural biology:** Crystal structures of GPX1-8 isoforms, mutational analysis of catalytic residues (weaver2022theselenoproteinglutathione pages 2-3, chaudiere2023biologicalandcatalytic pages 1-2)
- **Biochemical assays:** Substrate specificity, reducing partner identification, kinetic measurements (brigeliusflohe2020regulatoryphenomenain pages 4-6, chaudiere2023biologicalandcatalytic pages 1-2, chaudiere2023biologicalandcatalytic pages 10-11)
- **Genetic studies:** Knockout mice for GPX1-8, revealing embryonic lethality (GPX4), male infertility (GPX4, GPX5), and tissue-specific phenotypes (chaudiere2023biologicalandcatalytic pages 10-11)
- **Cell biology:** Subcellular localization via immunofluorescence, organellar fractionation, and GFP fusions (santos2025thefamilyof pages 1-2, pei2023researchprogressof pages 3-6)

Computational/bioinformatic inferences (e.g., PANTHER phylogenetic trees, subfamily assignments) are supported by these experimental data but should not be used as the sole basis for GO annotation without experimental validation (mi2020pantherversion16 pages 2-3, mi2020pantherversion16 pages 1-2).

---

## 6. Conclusion

PTHR11592 (GLUTATHIONE PEROXIDASE) is a **family-type InterPro entry** that, in principle, could support whole-protein function GO terms. However, the glutathione peroxidase family is **not functionally homogeneous**: it encompasses classical antioxidant enzymes (GPX1–3), a unique membrane lipid peroxide reductase and ferroptosis suppressor (GPX4), specialized ER protein-folding factors (GPX7–8), and tissue-specific reproductive enzymes (GPX5). Catalytic chemistry varies (selenocysteine vs. cysteine), as do reducing partners (GSH vs. thioredoxin/PDI), quaternary structures (tetramer vs. monomer), and taxonomic distributions (vertebrate-specific vs. plant-specific subfamilies).

**The current absence of InterPro2GO mappings for PTHR11592 is scientifically sound.** Future GO annotation should be **subfamily-specific**, leveraging the 43 existing PANTHER subfamilies to assign precise, experimentally validated terms to orthologous groups. Broad family-level annotations risk systematic over-annotation and should be avoided.

**Final Recommendation:** **ACCEPT the current lack of InterPro2GO mappings. Future annotation should be SUBFAMILY-SPECIFIC using PANTHER child entries.**

---

## References

All citations in this report refer to context IDs from retrieved literature (pei2023researchprogressof pages 1-2, mi2020pantherversion16 pages 1-2), corresponding to:
- Pei et al. 2023, *Front. Pharmacol.* (pei2023researchprogressof pages 1-2, pei2023researchprogressof pages 2-3, pei2023researchprogressof pages 3-6)
- Weaver & Skouta 2022, *Biomedicines* (weaver2022theselenoproteinglutathione pages 2-3)
- Brigelius-Flohé & Flohé 2020, *Antioxid. Redox Signal.* (brigeliusflohe2020regulatoryphenomenain pages 1-4, brigeliusflohe2020regulatoryphenomenain pages 4-6, brigeliusflohe2020regulatoryphenomenain pages 6-8)
- Hewitt & Degnan 2023, *Sci. Rep.* (hewitt2023antioxidantenzymesthat pages 1-2, hewitt2023antioxidantenzymesthat pages 3-4)
- Cubas-Gaona et al. 2020, *Microorganisms* (cubasgaona2020tetrahymenaglutathioneperoxidase pages 1-3)
- Vašková et al. 2023, *Molecules* (vaskova2023glutathionerelatedenzymesand pages 2-4)
- do Carmo Santos et al. 2025, *Front. Plant Sci.* (santos2025thefamilyof pages 1-2)
- Chaudière 2023, *Int. J. Mol. Sci.* (chaudiere2023biologicalandcatalytic pages 1-2, chaudiere2023biologicalandcatalytic pages 10-11)
- Mi et al. 2021, *Nucleic Acids Res.* (PANTHER) (mi2020pantherversion16 pages 2-3, mi2020pantherversion16 pages 1-2)

Publication dates and DOIs are available in the BibTeX metadata of the retrieved papers.

References

1. (cubasgaona2020tetrahymenaglutathioneperoxidase pages 1-3): Liliana L. Cubas-Gaona, Patricia de Francisco, Ana Martín-González, and Juan Carlos Gutiérrez. Tetrahymena glutathione peroxidase family: a comparative analysis of these antioxidant enzymes and differential gene expression to metals and oxidizing agents. Microorganisms, 8:1008, Jul 2020. URL: https://doi.org/10.3390/microorganisms8071008, doi:10.3390/microorganisms8071008. This article has 17 citations.

2. (brigeliusflohe2020regulatoryphenomenain pages 4-6): Regina Brigelius-Flohé and Leopold Flohé. Regulatory phenomena in the glutathione peroxidase superfamily. Sep 2020. URL: https://doi.org/10.1089/ars.2019.7905, doi:10.1089/ars.2019.7905. This article has 460 citations and is from a domain leading peer-reviewed journal.

3. (chaudiere2023biologicalandcatalytic pages 1-2): Jean Chaudière. Biological and catalytic properties of selenoproteins. International Journal of Molecular Sciences, 24:10109, Jun 2023. URL: https://doi.org/10.3390/ijms241210109, doi:10.3390/ijms241210109. This article has 64 citations.

4. (pei2023researchprogressof pages 1-2): Jun Pei, Xingyu Pan, Guanghui Wei, and Yi Hua. Research progress of glutathione peroxidase family (gpx) in redoxidation. Frontiers in Pharmacology, Mar 2023. URL: https://doi.org/10.3389/fphar.2023.1147414, doi:10.3389/fphar.2023.1147414. This article has 700 citations.

5. (pei2023researchprogressof pages 2-3): Jun Pei, Xingyu Pan, Guanghui Wei, and Yi Hua. Research progress of glutathione peroxidase family (gpx) in redoxidation. Frontiers in Pharmacology, Mar 2023. URL: https://doi.org/10.3389/fphar.2023.1147414, doi:10.3389/fphar.2023.1147414. This article has 700 citations.

6. (brigeliusflohe2020regulatoryphenomenain pages 1-4): Regina Brigelius-Flohé and Leopold Flohé. Regulatory phenomena in the glutathione peroxidase superfamily. Sep 2020. URL: https://doi.org/10.1089/ars.2019.7905, doi:10.1089/ars.2019.7905. This article has 460 citations and is from a domain leading peer-reviewed journal.

7. (santos2025thefamilyof pages 1-2): Maria Luíza do Carmo Santos, Ariana Silva Santos, Diogo Pereira Silva de Novais, Natasha dos Santos Lopes, Carlos Priminho Pirovani, and Fabienne Micheli. The family of glutathione peroxidase proteins and their role against biotic stress in plants: a systematic review. Frontiers in Plant Science, Feb 2025. URL: https://doi.org/10.3389/fpls.2025.1425880, doi:10.3389/fpls.2025.1425880. This article has 24 citations.

8. (weaver2022theselenoproteinglutathione pages 2-3): Kamari Weaver and Rachid Skouta. The selenoprotein glutathione peroxidase 4: from molecular mechanisms to novel therapeutic opportunities. Biomedicines, Apr 2022. URL: https://doi.org/10.3390/biomedicines10040891, doi:10.3390/biomedicines10040891. This article has 292 citations.

9. (pei2023researchprogressof pages 3-6): Jun Pei, Xingyu Pan, Guanghui Wei, and Yi Hua. Research progress of glutathione peroxidase family (gpx) in redoxidation. Frontiers in Pharmacology, Mar 2023. URL: https://doi.org/10.3389/fphar.2023.1147414, doi:10.3389/fphar.2023.1147414. This article has 700 citations.

10. (chaudiere2023biologicalandcatalytic pages 10-11): Jean Chaudière. Biological and catalytic properties of selenoproteins. International Journal of Molecular Sciences, 24:10109, Jun 2023. URL: https://doi.org/10.3390/ijms241210109, doi:10.3390/ijms241210109. This article has 64 citations.

11. (hewitt2023antioxidantenzymesthat pages 1-2): Olivia H. Hewitt and Sandie M. Degnan. Antioxidant enzymes that target hydrogen peroxide are conserved across the animal kingdom, from sponges to mammals. Scientific Reports, Feb 2023. URL: https://doi.org/10.1038/s41598-023-29304-6, doi:10.1038/s41598-023-29304-6. This article has 47 citations and is from a peer-reviewed journal.

12. (hewitt2023antioxidantenzymesthat pages 3-4): Olivia H. Hewitt and Sandie M. Degnan. Antioxidant enzymes that target hydrogen peroxide are conserved across the animal kingdom, from sponges to mammals. Scientific Reports, Feb 2023. URL: https://doi.org/10.1038/s41598-023-29304-6, doi:10.1038/s41598-023-29304-6. This article has 47 citations and is from a peer-reviewed journal.

13. (mi2020pantherversion16 pages 1-2): Huaiyu Mi, Dustin Ebert, Anushya Muruganujan, Caitlin Mills, Laurent-Philippe Albou, Tremayne Mushayamaha, and Paul D Thomas. Panther version 16: a revised family classification, tree-based classification tool, enhancer regions and extensive api. Nucleic Acids Research, 49:D394-D403, Dec 2021. URL: https://doi.org/10.1093/nar/gkaa1106, doi:10.1093/nar/gkaa1106. This article has 1509 citations and is from a highest quality peer-reviewed journal.

14. (mi2020pantherversion16 pages 2-3): Huaiyu Mi, Dustin Ebert, Anushya Muruganujan, Caitlin Mills, Laurent-Philippe Albou, Tremayne Mushayamaha, and Paul D Thomas. Panther version 16: a revised family classification, tree-based classification tool, enhancer regions and extensive api. Nucleic Acids Research, 49:D394-D403, Dec 2021. URL: https://doi.org/10.1093/nar/gkaa1106, doi:10.1093/nar/gkaa1106. This article has 1509 citations and is from a highest quality peer-reviewed journal.

15. (brigeliusflohe2020regulatoryphenomenain pages 6-8): Regina Brigelius-Flohé and Leopold Flohé. Regulatory phenomena in the glutathione peroxidase superfamily. Sep 2020. URL: https://doi.org/10.1089/ars.2019.7905, doi:10.1089/ars.2019.7905. This article has 460 citations and is from a domain leading peer-reviewed journal.

16. (vaskova2023glutathionerelatedenzymesand pages 2-4): Janka Vašková, Ladislav Kočan, Ladislav Vaško, and Pál Perjési. Glutathione-related enzymes and proteins: a review. Molecules, 28:1447, Feb 2023. URL: https://doi.org/10.3390/molecules28031447, doi:10.3390/molecules28031447. This article has 424 citations.

## Artifacts

- [Edison artifact artifact-00](PTHR11592-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR11592-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](PTHR11592-deep-research-falcon_artifacts/artifact-02.md)

## Citations

1. chaudiere2023biologicalandcatalytic pages 10-11
2. pei2023researchprogressof pages 3-6
3. cubasgaona2020tetrahymenaglutathioneperoxidase pages 1-3
4. chaudiere2023biologicalandcatalytic pages 1-2
5. santos2025thefamilyof pages 1-2
6. hewitt2023antioxidantenzymesthat pages 1-2
7. weaver2022theselenoproteinglutathione pages 2-3
8. vaskova2023glutathionerelatedenzymesand pages 2-4
9. brigeliusflohe2020regulatoryphenomenain pages 4-6
10. pei2023researchprogressof pages 1-2
11. pei2023researchprogressof pages 2-3
12. brigeliusflohe2020regulatoryphenomenain pages 1-4
13. hewitt2023antioxidantenzymesthat pages 3-4
14. brigeliusflohe2020regulatoryphenomenain pages 6-8
15. https://doi.org/10.3390/microorganisms8071008,
16. https://doi.org/10.1089/ars.2019.7905,
17. https://doi.org/10.3390/ijms241210109,
18. https://doi.org/10.3389/fphar.2023.1147414,
19. https://doi.org/10.3389/fpls.2025.1425880,
20. https://doi.org/10.3390/biomedicines10040891,
21. https://doi.org/10.1038/s41598-023-29304-6,
22. https://doi.org/10.1093/nar/gkaa1106,
23. https://doi.org/10.3390/molecules28031447,