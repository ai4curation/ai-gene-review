---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-21T20:32:39.628438'
end_time: '2026-06-21T20:45:27.487428'
duration_seconds: 767.86
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR13976
  interpro_name: Epithelial Splicing Regulatory
  interpro_short_name: ESRP
  interpro_type: family
  interpro_integrated: IPR050666
  member_databases: Not specified
  n_proteins: '13338'
  n_taxa: '5963'
  n_subfamilies: '24'
  interpro2go_terms: None mapped (no InterPro2GO terms for this entry)
  interpro_description: The ESRP family is involved in the regulation of mRNA splicing,
    playing a crucial role in the formation of cell type-specific isoforms, particularly
    in epithelial cells. Family members are known to regulate the expression of FGFR2-IIIb,
    an epithelial-specific isoform of FGFR2, and are implicated in the splicing of
    various transcripts during the epithelial-to-mesenchymal transition (EMT). They
    act by directly binding to specific sequences in mRNAs, such as GU-rich motifs
    in regulatory regions. Some family members also participate in the regulation
    of alternative splicing in embryo development and are involved in processes like
    inner ear development and auditory hair cell differentiation. Additionally, hnRNP
    proteins within this family contribute to pre-mRNA processing events, forming
    complexes that are essential for the conversion of pre-mRNAs into functional,
    translatable mRNAs in the cytoplasm.
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 19
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: PTHR13976-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR13976-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: PTHR13976-deep-research-falcon_artifacts/artifact-02.md
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
- **Accession:** PTHR13976
- **Name:** Epithelial Splicing Regulatory
- **Short name:** ESRP
- **Entry type:** family
- **Integrated into / parent:** IPR050666
- **Member database signatures:** Not specified
- **Scale:** 13338 proteins across 5963 taxa, 24 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** The ESRP family is involved in the regulation of mRNA splicing, playing a crucial role in the formation of cell type-specific isoforms, particularly in epithelial cells. Family members are known to regulate the expression of FGFR2-IIIb, an epithelial-specific isoform of FGFR2, and are implicated in the splicing of various transcripts during the epithelial-to-mesenchymal transition (EMT). They act by directly binding to specific sequences in mRNAs, such as GU-rich motifs in regulatory regions. Some family members also participate in the regulation of alternative splicing in embryo development and are involved in processes like inner ear development and auditory hair cell differentiation. Additionally, hnRNP proteins within this family contribute to pre-mRNA processing events, forming complexes that are essential for the conversion of pre-mRNAs into functional, translatable mRNAs in the cytoplasm.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR13976 (Epithelial Splicing Regulatory)**, structured to support GO annotation review.

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
- **Accession:** PTHR13976
- **Name:** Epithelial Splicing Regulatory
- **Short name:** ESRP
- **Entry type:** family
- **Integrated into / parent:** IPR050666
- **Member database signatures:** Not specified
- **Scale:** 13338 proteins across 5963 taxa, 24 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** The ESRP family is involved in the regulation of mRNA splicing, playing a crucial role in the formation of cell type-specific isoforms, particularly in epithelial cells. Family members are known to regulate the expression of FGFR2-IIIb, an epithelial-specific isoform of FGFR2, and are implicated in the splicing of various transcripts during the epithelial-to-mesenchymal transition (EMT). They act by directly binding to specific sequences in mRNAs, such as GU-rich motifs in regulatory regions. Some family members also participate in the regulation of alternative splicing in embryo development and are involved in processes like inner ear development and auditory hair cell differentiation. Additionally, hnRNP proteins within this family contribute to pre-mRNA processing events, forming complexes that are essential for the conversion of pre-mRNAs into functional, translatable mRNAs in the cytoplasm.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR13976 (Epithelial Splicing Regulatory)**, structured to support GO annotation review.

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


# InterPro Family PTHR13976 (Epithelial Splicing Regulatory) — GO Annotation Review Research Report

## Executive Summary

InterPro entry PTHR13976 corresponds to the **Epithelial Splicing Regulatory Protein (ESRP) family**, a functionally coherent protein family of RNA-binding splicing regulators. The family is currently **under-annotated** in InterPro2GO, with zero GO terms mapped. Based on comprehensive literature review and structural/functional analysis, this report recommends **adding core GO terms** for RNA binding, mRNA splicing regulation, and alternative splicing, while **avoiding tissue-specific developmental/process terms** that are restricted to particular paralogs, taxa, or biological contexts.

---

## 1. Family Definition and Biochemistry

### Molecular Architecture and Conserved Domains

The ESRP family comprises epithelial-cell-type-specific RNA-binding proteins characterized by a conserved multi-domain architecture (derham2023thediscoveryfunction pages 3-4, derham2023thediscoveryfunction pages 1-3, wang2025theroleof pages 1-2). The defining structural features include:

- **Three tandem RNA Recognition Motifs (RRMs)**: ESRP1 and ESRP2 both contain three RRM domains (RRM1, RRM2, RRM3) with high sequence identity between paralogs (89%, 68%, and 76% respectively) (derham2023thediscoveryfunction pages 3-4, derham2023thediscoveryfunction pages 1-3). These RRM domains are the functional core for RNA recognition and binding.

- **N-terminal DNAQ-like exonuclease domain**: Both ESRP1 and ESRP2 contain this conserved domain, though its specific function in the ESRP context remains to be fully characterized (derham2023thediscoveryfunction pages 3-4).

- **Paralog-specific C-terminal domains**: ESRP1 contains a DAZAP2-like domain at the C-terminus, whereas ESRP2 contains a FAM70 domain, representing the major structural divergence between the two paralogs (derham2023thediscoveryfunction pages 3-4).

### RNA-Binding Specificity and Mechanistic Details

ESRPs recognize and bind **UGG-rich and GU-rich motifs** in target RNAs with high affinity (derham2023thediscoveryfunction pages 3-4, peart2022theglobalproteinrna pages 4-6). The most enriched binding motif identified through in vivo enhanced crosslinking immunoprecipitation (eCLIP) is **UGGUGG** (peart2022theglobalproteinrna pages 4-6, liu2024esrp1controlsbiogenesis pages 1-2). Structural studies using X-ray crystallography of the ESRP1 qRRM2 domain revealed that guanines are embedded in **clamp-like aromatic pockets** in the protein, providing direct molecular insight into sequence-specific RNA recognition (liu2024esrp1controlsbiogenesis pages 1-2).

RRM2 and RRM3 have been identified as essential for recognition and interaction with pre-mRNA targets, with point mutations in RRM2 reducing FGFR2 target binding (derham2023thediscoveryfunction pages 3-4). The specific role of RRM1 remains less well characterized, though combined RRM1/RRM2 mutations suppress binding to key ESRP targets including FGFR2 and ENAH (derham2023thediscoveryfunction pages 3-4).

### Position-Dependent Splicing Regulation

ESRPs function as master regulators of alternative splicing through a **position-dependent "RNA map" mechanism** (peart2022theglobalproteinrna pages 4-6, peart2022theglobalproteinrna pages 1-2). When ESRPs bind upstream of or within an exon, they induce **exon skipping**; when they bind in the downstream intron (typically 75-250 nucleotides downstream), they promote **exon inclusion** (derham2023thediscoveryfunction pages 3-4, peart2022theglobalproteinrna pages 4-6). This position-dependent activity has been validated genome-wide using rMAPS2 analysis combining eCLIP-seq binding data with RNA-seq splicing changes (peart2022theglobalproteinrna pages 4-6).

### Molecular Function Beyond Splicing

In addition to nuclear splicing regulation, ESRP1 exhibits **cytoplasmic localization** for certain isoforms, suggesting additional post-transcriptional roles (derham2023thediscoveryfunction pages 3-4, peart2022theglobalproteinrna pages 1-2). ESRP1 binds extensively within 3' and 5' untranslated regions (UTRs) of mRNAs, supporting roles in mRNA stability, translation, and alternative polyadenylation (derham2023thediscoveryfunction pages 3-4, peart2022theglobalproteinrna pages 1-2, peart2022theglobalproteinrna pages 4-6). ESRP1 also controls the biogenesis of large circular RNAs such as circDOCK1(2–27) by binding GGU-containing repeats in intron 1 and detaining its splicing (liu2024esrp1controlsbiogenesis pages 1-2).

| Protein | Gene location | Protein size | Domain structure | RNA-binding motif / sequence specificity | Key molecular functions | Tissue / cellular expression | Evolutionary conservation | Major knockout / loss-of-function phenotypes |
|---|---|---|---|---|---|---|---|---|
| ESRP1 | Human **8q22.1**; also called **RBM35A** (wang2025theroleof pages 1-2) | ~**681 aa**, estimated **~76 kDa** (wang2025theroleof pages 1-2) | **Three RRMs**; RRM1/RRM2/RRM3 are highly conserved with ESRP2; N-terminal **DNAQ-like exonuclease domain** reported in review literature; ESRP1 C-terminus contains a **DAZAP2-like domain**; ESRP1 also has alternatively spliced isoforms differing in a **putative nuclear localization sequence**, consistent with nuclear and cytoplasmic forms (derham2023thediscoveryfunction pages 3-4, wang2025theroleof pages 1-2) | High-affinity binding to **UGG-rich / GU-rich motifs**; in vivo eCLIP identified **UGGUGG** as the most enriched motif; HITS-CLIP/structural work showed binding to **GGU-containing** motifs; qRRM2 crystal structure showed guanines bound in **aromatic clamp-like pockets** (derham2023thediscoveryfunction pages 3-4, peart2022theglobalproteinrna pages 4-6, liu2024esrp1controlsbiogenesis pages 1-2) | Master regulator of **epithelial alternative splicing**; directly binds exons/introns to promote exon inclusion or skipping in a **position-dependent RNA map**; regulates classic epithelial targets including **FGFR2**, **CTNND1**, **ENAH**, **ARHGEF11**; also shows binding in **3' and 5' UTRs**, supporting post-transcriptional roles beyond splicing, including effects on translation/stability; promotes epithelial identity and contributes to circRNA biogenesis such as **circDOCK1(2–27)** (derham2023thediscoveryfunction pages 3-4, peart2022theglobalproteinrna pages 1-2, peart2022theglobalproteinrna pages 4-6, liu2024esrp1controlsbiogenesis pages 1-2, kwon2023roleofepithelial pages 1-2) | Predominantly **epithelial cell-type specific** and mainly **nuclear**, but detectable in the **cytoplasm**; broadly expressed across multiple epithelial organs/tissues; epithelial epidermis studies show a central role in epithelial transcriptome maintenance (peart2022theglobalproteinrna pages 1-2, wang2025theroleof pages 1-2, kwon2023roleofepithelial pages 1-2) | ESRP family is described as **highly conserved**, with orthologs in **flies (fusilli)**, **worms (sym-2)**, and **chicken**; strong conservation especially across the three RRMs, indicating conserved RNA-binding/splicing function (derham2023thediscoveryfunction pages 3-4) | **Esrp1 knockout mice** develop **cleft lip and palate**; combined loss with Esrp2 causes more severe widespread developmental defects and disrupted epithelial splicing programs; epidermal loss impairs **skin barrier** function; ESRP1 loss in epithelial systems shifts splicing toward mesenchymal patterns (bebee2015thesplicingregulators pages 1-2, bebee2015thesplicingregulators pages 2-3, peart2022theglobalproteinrna pages 1-2) |
| ESRP2 | Human **16q22.1**; also called **RBM35B** (wang2025theroleof pages 1-2) | ~**727 aa**, estimated **~78 kDa** (wang2025theroleof pages 1-2) | **Three RRMs** homologous to ESRP1; review literature reports an N-terminal **DNAQ-like exonuclease domain** and an ESRP2-specific C-terminal **FAM70 domain**; RRM2/RRM3 implicated in target recognition and splicing activity (derham2023thediscoveryfunction pages 3-4) | Shares the ESRP family preference for **UGG-rich** motifs; a point mutation in **RRM2** reduced binding to **FGFR2** pre-mRNA; family-level data support common UGG/GU-rich specificity with ESRP1 (derham2023thediscoveryfunction pages 3-4) | Paralogous epithelial splicing regulator with partial redundancy to ESRP1; controls epithelial splice isoforms and, in liver, directs a major **neonatal-to-adult hepatocyte splicing program** affecting ~**20%** of splice isoforms in mouse and human hepatocytes; helps maintain adult isoforms of Hippo-pathway-related genes during liver maturation/regeneration (peart2022theglobalproteinrna pages 1-2, bhate2015esrp2controlsan pages 1-2, derham2023thediscoveryfunction pages 6-7) | Epithelial-associated expression overall, but with a notable specialized role in **hepatocytes**, where ESRP2 is the **predominant/sole ESRP paralog expressed in liver** and rises during postnatal maturation (derham2023thediscoveryfunction pages 6-7, bhate2015esrp2controlsan pages 1-2) | Conserved paralog within the ESRP family; shares high sequence identity with ESRP1 in RRM regions and participates in conserved epithelial splicing control across vertebrates; family orthology noted across metazoans (derham2023thediscoveryfunction pages 3-4) | **Esrp2 single-knockout mice** reportedly show **no obvious abnormalities** in the developmental study, indicating weaker requirement than ESRP1 in many tissues; however, liver studies show Esrp2 loss disrupts adult hepatocyte splicing, causes persistence of fetal-like splicing patterns, and affects hepatocyte proliferation/maturation responses after injury (peart2022theglobalproteinrna pages 1-2, bhate2015esrp2controlsan pages 1-2, derham2023thediscoveryfunction pages 6-7) |


*Table: This table summarizes the structural, biochemical, expression, evolutionary, and phenotypic features of ESRP1 and ESRP2 from the key papers reviewed. It is useful for assessing how functionally coherent the ESRP family is for GO annotation review.*

---

## 2. InterPro2GO Mapping Appropriateness

### Current Status: Zero GO Terms Mapped

PTHR13976 currently has **no InterPro2GO terms** mapped. Given the extensive experimental characterization of the ESRP family, this represents **under-annotation** rather than appropriate caution.

### Recommended Core GO Terms (ACCEPT for Family-Level Annotation)

The following GO terms are supported by direct experimental evidence for ESRP1 and ESRP2 and are appropriate for universal family-level annotation:

**Molecular Function:**
- **RNA binding (GO:0003723)**: Core family property supported by three RRM domains and extensive eCLIP/HITS-CLIP data (derham2023thediscoveryfunction pages 3-4, liu2024esrp1controlsbiogenesis pages 1-2, peart2022theglobalproteinrna pages 4-6).
- **mRNA binding (GO:0003729)**: ESRPs bind pre-mRNAs and mRNA UTRs in vivo (peart2022theglobalproteinrna pages 1-2, peart2022theglobalproteinrna pages 4-6).
- **pre-mRNA binding (GO:0043022)**: Canonical ESRP function involves binding intronic and exonic cis-elements in pre-mRNAs (derham2023thediscoveryfunction pages 3-4, peart2022theglobalproteinrna pages 1-2, peart2022theglobalproteinrna pages 4-6).
- **mRNA splicing regulator activity (GO:0090330)**: Best concise family-level functional term; ESRPs promote or repress exon inclusion in a position-dependent manner (peart2022theglobalproteinrna pages 1-2, peart2022theglobalproteinrna pages 4-6, derham2023thediscoveryfunction pages 3-4).

**Biological Process:**
- **regulation of mRNA splicing, via spliceosome (GO:0048024)**: Strong family-level process term supported by direct splicing-regulatory roles (peart2022theglobalproteinrna pages 1-2, peart2022theglobalproteinrna pages 4-6, derham2023thediscoveryfunction pages 3-4).
- **alternative mRNA splicing, via spliceosome (GO:0000380)**: ESRPs are defined by control of alternative exon choice in canonical targets such as FGFR2, CTNND1, ENAH, ARHGEF11 (peart2022theglobalproteinrna pages 1-2, kwon2023roleofepithelial pages 1-2, peart2022theglobalproteinrna pages 4-6).

**Cellular Component:**
- **nucleus (GO:0005634)**: ESRP proteins function primarily as nuclear splicing regulators (derham2023thediscoveryfunction pages 3-4, wang2025theroleof pages 1-2).
- **nucleoplasm (GO:0005654)**: More specific localization consistent with pre-mRNA splicing function (derham2023thediscoveryfunction pages 3-4, peart2022theglobalproteinrna pages 1-2).

### GO Terms to REJECT (Overly Specific or Context-Limited)

The following terms are **not appropriate** for universal family-level annotation because they apply only to subsets of the family or are restricted to particular taxa, tissues, or biological contexts:

- **Epithelial to mesenchymal transition (GO:0001837)**: ESRPs influence EMT-associated splicing programs, but EMT regulation is not universal for every matched family member across taxa or tissues (li2023regulationofepithelialmesenchymal pages 1-2, kwon2023roleofepithelial pages 1-2, derham2023thediscoveryfunction pages 6-7).
- **Epithelial cell differentiation/development**: ESRP-dependent phenotypes in palate, skin, ear, and branching organs are real but not universal to all family members (bebee2015thesplicingregulators pages 1-2, carroll2020anirf6esrp12regulatory pages 1-4, derham2023thediscoveryfunction pages 6-7, bhate2015esrp2controlsan pages 1-2).
- **Craniofacial development/palate development**: Strong vertebrate developmental phenotypes but clearly subfamily/taxon/context-limited (bebee2015thesplicingregulators pages 1-2, carroll2020anirf6esrp12regulatory pages 1-4).
- **Liver development/liver regeneration**: ESRP2 specialization in hepatocyte maturation/regeneration is paralog- and tissue-restricted (derham2023thediscoveryfunction pages 6-7, bhate2015esrp2controlsan pages 1-2).
- **Spliceosomal complex (GO:0005681)**: ESRPs regulate splice-site choice but are not established core spliceosome components (peart2022theglobalproteinrna pages 1-2, derham2023thediscoveryfunction pages 3-4).

| GO category | GO term name and ID | Applies to all PTHR13976 family members? | Evidence strength | Appropriateness for family-level annotation | Recommended action | Rationale / notes |
|---|---|---|---|---|---|---|
| MF | RNA binding (GO:0003723) | Probably yes | Experimental for ESRP1/2; inferred across family | APPROPRIATE | ACCEPT | Core family property: ESRP proteins are RNA-binding proteins with three RRMs; ESRP1/2 bind UGG/GU-rich motifs, and ESRP1 qRRM2 structure directly supports sequence-specific RNA recognition (derham2023thediscoveryfunction pages 3-4, liu2024esrp1controlsbiogenesis pages 1-2, peart2022theglobalproteinrna pages 4-6) |
| MF | mRNA binding (GO:0003729) | Probably yes | Experimental for ESRP1/2; inferred across family | APPROPRIATE | ACCEPT | ESRPs bind pre-mRNAs and mRNA UTRs in vivo; ESRP1 eCLIP showed extensive binding in introns, exons, and 3'/5' UTRs of protein-coding transcripts (peart2022theglobalproteinrna pages 1-2, peart2022theglobalproteinrna pages 4-6) |
| MF | single-stranded RNA binding (GO:0003727) | Likely yes | Inferred from RRM family biochemistry plus direct motif-binding studies | APPROPRIATE | ACCEPT | ESRP motifs are short UGG/GU-rich elements in transcripts; direct motif-binding and structural work are consistent with ssRNA recognition by RRM domains (derham2023thediscoveryfunction pages 3-4, liu2024esrp1controlsbiogenesis pages 1-2, peart2022theglobalproteinrna pages 4-6) |
| MF | pre-mRNA binding (GO:0043022) | Likely yes | Experimental for canonical members; inferred across family | APPROPRIATE | ACCEPT | ESRPs regulate splice-site choice by binding intronic/exonic cis-elements in pre-mRNAs, classically FGFR2 and many additional targets (derham2023thediscoveryfunction pages 3-4, peart2022theglobalproteinrna pages 1-2, peart2022theglobalproteinrna pages 4-6) |
| MF | mRNA splicing regulator activity (GO:0090330) | Likely yes | Experimental for ESRP1/2; inferred across family | APPROPRIATE | ACCEPT | Best concise family-level functional term: ESRPs are dedicated epithelial splicing regulators that promote or repress exon inclusion in a position-dependent manner (peart2022theglobalproteinrna pages 1-2, peart2022theglobalproteinrna pages 4-6, derham2023thediscoveryfunction pages 3-4) |
| MF | catalytic activity, acting on RNA | No | Contradicted by current understanding | TOO_SPECIFIC | REJECT | ESRPs are regulatory RNA-binding proteins, not spliceosomal catalytic factors or RNA enzymes; no catalytic residues/activity established (derham2023thediscoveryfunction pages 3-4, peart2022theglobalproteinrna pages 1-2) |
| BP | regulation of mRNA splicing, via spliceosome (GO:0048024) | Likely yes | Experimental for ESRP1/2; inferred across family | APPROPRIATE | ACCEPT | Strong family-level process term supported by direct splicing-regulatory roles across many targets and tissues (peart2022theglobalproteinrna pages 1-2, peart2022theglobalproteinrna pages 4-6, derham2023thediscoveryfunction pages 3-4) |
| BP | alternative mRNA splicing, via spliceosome (GO:0000380) | Likely yes | Experimental for ESRP1/2; inferred across family | APPROPRIATE | ACCEPT | ESRPs are defined by control of alternative exon choice, including FGFR2, CTNND1, ENAH, ARHGEF11 and many others (peart2022theglobalproteinrna pages 1-2, kwon2023roleofepithelial pages 1-2, peart2022theglobalproteinrna pages 4-6) |
| BP | RNA processing (GO:0006396) | Likely yes | Experimental/inferred | TOO_GENERIC | MODIFY | True but too broad; if a GO mapping is added, the splicing-specific BP terms above are more informative (peart2022theglobalproteinrna pages 1-2, derham2023thediscoveryfunction pages 3-4) |
| BP | mRNA processing (GO:0006397) | Likely yes | Experimental/inferred | TOO_GENERIC | MODIFY | Supported, especially because ESRP1 also binds UTRs and can affect post-transcriptional outputs, but still broader than the family-defining splicing role (peart2022theglobalproteinrna pages 1-2, peart2022theglobalproteinrna pages 4-6) |
| BP | regulation of alternative mRNA splicing, via spliceosome | Likely yes | Experimental for ESRP1/2; inferred across family | APPROPRIATE | ACCEPT | Even more specific summary of the defining ESRP function; suitable if available in GO and preferred over broader RNA-processing terms (peart2022theglobalproteinrna pages 1-2, peart2022theglobalproteinrna pages 4-6, derham2023thediscoveryfunction pages 3-4) |
| BP | epithelial to mesenchymal transition (GO:0001837) | No | Experimental, but context-specific and downstream | TOO_SPECIFIC | REJECT | ESRPs influence EMT-associated splicing programs, but EMT regulation is not universal for every matched family member across taxa or tissues; this is a systems-level consequence, not safe core family annotation (li2023regulationofepithelialmesenchymal pages 1-2, kwon2023roleofepithelial pages 1-2, derham2023thediscoveryfunction pages 6-7) |
| BP | epithelial cell differentiation / development | No | Experimental, but lineage- and organism-specific | TOO_SPECIFIC | REJECT | ESRP-dependent phenotypes in palate, skin, ear, branching organs, and liver are real, but not universal to all family members and not portable across all metazoan taxa matched by the signature (bebee2015thesplicingregulators pages 1-2, carroll2020anirf6esrp12regulatory pages 1-4, derham2023thediscoveryfunction pages 6-7, bhate2015esrp2controlsan pages 1-2) |
| BP | craniofacial development / palate development | No | Experimental for vertebrate subsets | TOO_SPECIFIC | REJECT | Strong vertebrate developmental phenotypes, but clearly subfamily/taxon/context-limited and unsuitable for universal family annotation (bebee2015thesplicingregulators pages 1-2, carroll2020anirf6esrp12regulatory pages 1-4) |
| BP | liver development / liver regeneration | No | Experimental mainly for ESRP2 in vertebrates | TOO_SPECIFIC | REJECT | ESRP2 specialization in hepatocyte maturation/regeneration is paralog- and tissue-restricted, not valid for all ESRP-family proteins (derham2023thediscoveryfunction pages 6-7, bhate2015esrp2controlsan pages 1-2) |
| CC | nucleus (GO:0005634) | Probably yes for major functional pool | Experimental for ESRP1/2; inferred across family | APPROPRIATE | ACCEPT | ESRP proteins function primarily as nuclear splicing regulators; ESRP1 is predominantly nuclear though some isoforms are cytoplasmic (derham2023thediscoveryfunction pages 3-4, wang2025theroleof pages 1-2) |
| CC | nucleoplasm (GO:0005654) | Likely yes | Inferred from nuclear splicing role | APPROPRIATE | ACCEPT | More specific than nucleus and consistent with pre-mRNA splicing function, though direct component-level localization evidence is less emphasized than for generic nucleus (derham2023thediscoveryfunction pages 3-4, peart2022theglobalproteinrna pages 1-2) |
| CC | spliceosomal complex (GO:0005681) | No / uncertain | Weak | TOO_SPECIFIC | REJECT | ESRPs regulate splice-site choice but are not established core spliceosome components; evidence supports regulator status rather than obligate stable spliceosomal-complex membership (peart2022theglobalproteinrna pages 1-2, derham2023thediscoveryfunction pages 3-4) |
| CC | cytoplasm (GO:0005737) | No / mixed | Experimental for some ESRP1 isoforms | TOO_SPECIFIC | MODIFY | Cytoplasmic ESRP1 isoforms and UTR-binding roles exist, but this is not clearly universal across the whole family; keep as non-core at most, not a default InterPro2GO family term (derham2023thediscoveryfunction pages 3-4, peart2022theglobalproteinrna pages 1-2, peart2022theglobalproteinrna pages 4-6) |
| CC | ribonucleoprotein complex | No / uncertain | Weak | TOO_GENERIC | REJECT | Too broad and not directly evidenced as a stable defining component annotation for the whole family (peart2022theglobalproteinrna pages 1-2) |


*Table: This table evaluates plausible GO terms for InterPro family PTHR13976 and distinguishes safe family-level annotations from terms that are too broad, too specific, or taxon/paralog restricted. It is intended to guide whether new InterPro2GO mappings should be added despite the current absence of mappings.*

---

## 3. Functional Divergence Across the Family

### Two-Paralog Structure with Subfunctionalization

The vertebrate ESRP family comprises two paralogs, **ESRP1** and **ESRP2**, which exhibit **subfunctionalization** rather than neo-functionalization (derham2023thediscoveryfunction pages 3-4, peart2022theglobalproteinrna pages 1-2, derham2023thediscoveryfunction pages 6-7, bhate2015esrp2controlsan pages 1-2). Both paralogs retain the core molecular activity of RNA binding and alternative splicing regulation but have diverged in their tissue expression patterns and developmental importance.

### ESRP1: Dominant Developmental Regulator

ESRP1 is broadly epithelial-cell-type-specific and serves as the predominant regulator in epidermis and many developing epithelial tissues (derham2023thediscoveryfunction pages 3-4, peart2022theglobalproteinrna pages 1-2, wang2025theroleof pages 1-2). Mouse knockout studies demonstrate that **Esrp1 knockout mice develop cleft lip and palate**, with epidermal loss disrupting skin barrier function and epithelial splicing programs (peart2022theglobalproteinrna pages 1-2, bebee2015thesplicingregulators pages 2-3, bebee2015thesplicingregulators pages 1-2, carroll2020anirf6esrp12regulatory pages 1-4). ESRP1 is the more essential paralog for whole-animal development: **Esrp2 single-knockout mice show no obvious developmental abnormalities**, whereas Esrp1 knockout is clearly pathological (peart2022theglobalproteinrna pages 1-2, bebee2015thesplicingregulators pages 2-3, bebee2015thesplicingregulators pages 1-2).

### ESRP2: Hepatocyte-Specialized Regulator

ESRP2 exhibits strong evidence for tissue-program specialization in **liver**, where it is the sole or predominant ESRP paralog expressed and rises postnatally during hepatocyte maturation (derham2023thediscoveryfunction pages 6-7, bhate2015esrp2controlsan pages 1-2). ESRP2 controls the neonatal-to-adult hepatocyte splicing program, affecting approximately **20% of splice isoforms** in mouse and human hepatocytes (derham2023thediscoveryfunction pages 6-7, bhate2015esrp2controlsan pages 1-2). Liver-focused studies show that Esrp2 loss disrupts adult splicing of Hippo-pathway-related factors (Nf2, Csnk1d, Yap1, Tead1) and affects liver regeneration-associated splicing control (derham2023thediscoveryfunction pages 6-7, bhate2015esrp2controlsan pages 1-2).

### Partial Redundancy and Compensation

The two paralogs exhibit **partial functional redundancy**, with ESRP2 able to compensate for ESRP1 in some contexts, though compensation is insufficient to prevent clefting and other Esrp1-associated developmental defects (peart2022theglobalproteinrna pages 1-2, derham2023thediscoveryfunction pages 6-7). Double-knockout mice (Esrp1/Esrp2) exhibit much more severe developmental defects than Esrp1 single knockout, including failure to form lungs and salivary glands, demonstrating overlapping but non-interchangeable functions (peart2022theglobalproteinrna pages 1-2, bebee2015thesplicingregulators pages 2-3, bebee2015thesplicingregulators pages 1-2).

### No Evidence for Neo-Functionalization or Catalytically Dead Members

There is **no evidence** for neo-functionalization in the sense of opposite biochemical activities or for catalytically dead (pseudo-enzyme) members of the family (derham2023thediscoveryfunction pages 3-4, peart2022theglobalproteinrna pages 1-2, derham2023thediscoveryfunction pages 6-7, bhate2015esrp2controlsan pages 1-2). Both ESRP1 and ESRP2 retain core RNA-binding and splicing-regulatory activity. The functional divergence represents **tissue-program specialization** after paralog divergence rather than loss or gain of fundamentally new molecular activities.

| Paralog | Tissue-specific expression patterns | Unique knockout / loss-of-function phenotypes | Degree of functional redundancy | Compensation mechanisms | Specialized splicing targets / programs with strongest evidence | Evidence for or against neo-functionalization / subfunctionalization |
|---|---|---|---|---|---|---|
| ESRP1 | Broadly epithelial-cell-type-specific; predominant regulator in epidermis and many developing epithelial tissues; mainly nuclear but with cytoplasmic isoforms, supporting both splicing and additional post-transcriptional roles (derham2023thediscoveryfunction pages 3-4, peart2022theglobalproteinrna pages 1-2, wang2025theroleof pages 1-2) | Esrp1 knockout mice develop cleft lip/palate; epidermal Esrp loss disrupts skin barrier and epithelial splicing programs; Esrp1 is the more essential paralog in whole-animal development, because Esrp2 single KO has no obvious phenotype while Esrp1 KO is clearly abnormal (peart2022theglobalproteinrna pages 1-2, bebee2015thesplicingregulators pages 2-3, bebee2015thesplicingregulators pages 1-2, carroll2020anirf6esrp12regulatory pages 1-4) | Partial redundancy with ESRP2, but not fully interchangeable in vivo; double loss is much more severe than Esrp1 loss alone, showing overlap, while the Esrp1 single-KO phenotype shows ESRP1 has stronger nonredundant developmental importance (peart2022theglobalproteinrna pages 1-2, bebee2015thesplicingregulators pages 2-3, bebee2015thesplicingregulators pages 1-2) | ESRP2 can compensate partly in some tissues; review notes ESRP2 compensates for ESRP1 in some contexts, but compensation is insufficient to prevent clefting and other Esrp1-associated defects (peart2022theglobalproteinrna pages 1-2, derham2023thediscoveryfunction pages 6-7) | Canonical epithelial splicing network including FGFR2-IIIb/IIIc control; strong direct evidence for ESRP1 regulation of epidermal epithelial targets such as ARHGEF11 and broader epithelial cell-function transcripts; additional ESRP1-specific evidence exists for cytoplasmic/post-transcriptional regulation and circRNA biogenesis such as circDOCK1(2–27) (derham2023thediscoveryfunction pages 3-4, peart2022theglobalproteinrna pages 1-2, peart2022theglobalproteinrna pages 4-6, liu2024esrp1controlsbiogenesis pages 1-2) | Supports subfunctionalization more than full neo-functionalization: ESRP1 retains ancestral shared epithelial splicing activity but appears specialized as the dominant paralog in many non-hepatic epithelial developmental contexts and may have expanded cytoplasmic/post-transcriptional functions through isoform-specific localization; no evidence that it is a pseudo-enzyme or has opposite molecular function to ESRP2 (derham2023thediscoveryfunction pages 3-4, peart2022theglobalproteinrna pages 1-2, derham2023thediscoveryfunction pages 6-7) |
| ESRP2 | Also epithelial-associated, but with especially strong evidence for a specialized hepatocyte role; in liver ESRP2 is reported as the sole or predominant ESRP paralog expressed and rises postnatally during hepatocyte maturation (derham2023thediscoveryfunction pages 6-7, bhate2015esrp2controlsan pages 1-2) | Esrp2 single-knockout mice show no obvious abnormalities in the developmental mouse study, contrasting with Esrp1 KO; however, liver-focused studies show Esrp2 loss disrupts the neonatal-to-adult hepatocyte splicing program and affects regeneration-associated splicing control (peart2022theglobalproteinrna pages 1-2, bhate2015esrp2controlsan pages 1-2, derham2023thediscoveryfunction pages 6-7) | Partial redundancy with ESRP1 in many epithelial tissues, but weaker global developmental requirement; redundancy is asymmetric because ESRP1 can be indispensable where ESRP2 is dispensable, whereas ESRP2 appears to dominate in liver where ESRP1 is absent or minimal (peart2022theglobalproteinrna pages 1-2, derham2023thediscoveryfunction pages 6-7, bhate2015esrp2controlsan pages 1-2) | Compensation by ESRP1 appears limited in liver because ESRP2 is the principal hepatic paralog; outside liver, overlap with ESRP1 likely buffers phenotype, explaining the mild Esrp2 single-KO phenotype (peart2022theglobalproteinrna pages 1-2, derham2023thediscoveryfunction pages 6-7, bhate2015esrp2controlsan pages 1-2) | Strongest specialized program is the postnatal hepatocyte splicing network, including adult isoforms in Hippo-pathway-related factors such as Nf2, Csnk1d, Yap1, and Tead1, and a broad fetal-to-adult liver splicing switch affecting ~20% of splice isoforms in mouse and human hepatocytes (derham2023thediscoveryfunction pages 6-7, bhate2015esrp2controlsan pages 1-2) | Strong evidence for subfunctionalization: ESRP2 appears to have retained core epithelial splicing activity but become preferentially deployed in liver maturation/regeneration. Evidence does not support opposite biochemical function or loss of RNA-binding activity. Rather than neo-functionalization in the sense of a new molecular activity, current data fit tissue-program specialization after paralog divergence (derham2023thediscoveryfunction pages 3-4, derham2023thediscoveryfunction pages 6-7, bhate2015esrp2controlsan pages 1-2) |


*Table: This table compares ESRP1 and ESRP2 for expression, knockout phenotypes, redundancy, and tissue-program specialization. It is useful for judging whether family-level GO terms are safe across the whole InterPro family or should instead be restricted to paralog- or tissue-specific subsets.*

---

## 4. Taxonomic Scope

### Broad Metazoan Conservation

The ESRP family is **highly conserved across metazoans** with identified orthologs in:
- **Flies** (fusilli)
- **Worms** (sym-2)
- **Chicken** (esrp1)
- **Mammals** (ESRP1 and ESRP2)

The high degree of evolutionary conservation, particularly within the three RNA recognition motifs (RRMs), indicates a critical physiological function maintained across animal evolution (derham2023thediscoveryfunction pages 3-4, derham2023thediscoveryfunction pages 1-3).

### InterPro Family Scale

According to the InterPro API data, PTHR13976 matches **13,338 proteins across 5,963 taxa** with **24 subfamilies**. This broad taxonomic distribution is consistent with an ancient splicing-regulatory function present across animal clades.

### Vertebrate-Centric Function

While the family is broadly distributed across metazoans, the strongest experimental characterization comes from **vertebrate systems**, particularly mouse and human studies. The two-paralog structure (ESRP1 and ESRP2) appears to be a vertebrate innovation, with invertebrates typically having single orthologs (derham2023thediscoveryfunction pages 3-4, derham2023thediscoveryfunction pages 1-3).

### Universal Core Function Across Taxa

The core molecular function of **RNA binding** and **alternative splicing regulation** through UGG/GU-rich motif recognition appears to be conserved across the taxonomic range of the family (derham2023thediscoveryfunction pages 3-4, derham2023thediscoveryfunction pages 1-3). In contrast, specific developmental processes (craniofacial development, liver maturation) are vertebrate- or mammal-specific and should not be applied as universal family annotations.

---

## 5. Over-Annotation Verdict and Recommendations

### Summary Verdict: UNDER-ANNOTATED

InterPro2GO for PTHR13976 is currently **under-annotated** with zero GO terms mapped. The ESRP family is functionally coherent for core RNA-binding and alternative-splicing-regulatory activities that are conserved across all characterized family members.

### Recommended GO Annotation Action Pattern

**PRIMARY RECOMMENDATION: ADD CORE TERMS**

The following GO terms should be **added** to PTHR13976 as they reflect universal family properties:

**Molecular Function:**
- RNA binding (GO:0003723)
- mRNA binding (GO:0003729)
- pre-mRNA binding (GO:0043022)
- mRNA splicing regulator activity (GO:0090330)

**Biological Process:**
- regulation of mRNA splicing, via spliceosome (GO:0048024)
- alternative mRNA splicing, via spliceosome (GO:0000380)

**Cellular Component:**
- nucleus (GO:0005634)
- nucleoplasm (GO:0005654)

**SECONDARY RECOMMENDATION: AVOID TISSUE/DEVELOPMENTAL TERMS**

The following types of terms should **NOT** be added at the family level:
- Epithelial-mesenchymal transition (paralog- and context-specific)
- Craniofacial/palate development (vertebrate-specific, ESRP1-dominant)
- Liver development/regeneration (ESRP2-specific, mammalian)
- Cell-type-specific developmental processes (not universal across taxa)

### Recommendation for InterPro Itself

No structural changes to the InterPro entry itself are recommended. PTHR13976 is correctly classified as a **family** (not a domain or superfamily), making whole-protein function annotations appropriate. The entry type is suitable for the core MF/BP terms recommended above.

If finer-grained annotation is desired in the future, InterPro could consider:
1. Creating **child entries** for vertebrate ESRP1 and ESRP2 paralogs to enable paralog-specific GO annotations for liver-specific (ESRP2) or craniofacial-specific (ESRP1) processes.
2. Distinguishing between **nuclear splicing-regulatory** and **cytoplasmic post-transcriptional** ESRP1 isoforms if structural signatures can reliably separate these functional variants.

### Experimental vs. Inferred Distinction

The recommended core GO terms are supported by **extensive experimental evidence** from:
- Structural studies (X-ray crystallography of qRRM2) (liu2024esrp1controlsbiogenesis pages 1-2)
- Genome-wide binding studies (eCLIP, HITS-CLIP) (peart2022theglobalproteinrna pages 4-6, liu2024esrp1controlsbiogenesis pages 1-2)
- Knockout mouse phenotypes (bebee2015thesplicingregulators pages 2-3, bebee2015thesplicingregulators pages 1-2, carroll2020anirf6esrp12regulatory pages 1-4)
- RNA-seq splicing analysis (peart2022theglobalproteinrna pages 1-2, peart2022theglobalproteinrna pages 4-6, bhate2015esrp2controlsan pages 1-2)

Extension of these findings from ESRP1/2 to the entire PTHR13976 family is based on **strong sequence conservation** across RRM domains and the conserved family architecture, which is a reasonable inference for core molecular function (derham2023thediscoveryfunction pages 3-4, derham2023thediscoveryfunction pages 1-3).

---

## Conclusion

PTHR13976 (Epithelial Splicing Regulatory family) represents a functionally coherent protein family with a well-defined core biochemical activity: **RNA binding and position-dependent alternative splicing regulation**. The current absence of InterPro2GO mappings is inappropriate under-annotation. Core GO terms for RNA binding, mRNA splicing regulator activity, regulation of alternative splicing, and nuclear localization should be added. Tissue-specific developmental process terms (EMT, craniofacial development, liver regeneration) should be avoided as they are restricted to particular paralogs, taxa, or biological contexts and would systematically over-annotate proteins across the family's broad taxonomic range.

References

1. (derham2023thediscoveryfunction pages 3-4): Jessica M. Derham and Auinash Kalsotra. The discovery, function, and regulation of epithelial splicing regulatory proteins (esrp) 1 and 2. Biochemical Society transactions, 51:1097-1109, Jun 2023. URL: https://doi.org/10.1042/bst20221124, doi:10.1042/bst20221124. This article has 18 citations and is from a peer-reviewed journal.

2. (derham2023thediscoveryfunction pages 1-3): Jessica M. Derham and Auinash Kalsotra. The discovery, function, and regulation of epithelial splicing regulatory proteins (esrp) 1 and 2. Biochemical Society transactions, 51:1097-1109, Jun 2023. URL: https://doi.org/10.1042/bst20221124, doi:10.1042/bst20221124. This article has 18 citations and is from a peer-reviewed journal.

3. (wang2025theroleof pages 1-2): Lili Wang, Min Zhang, Kelei Zhao, Xiaohan Yuan, Houyu Zhao, Yanting Liu, Yinghua Ji, and Ping Lu. The role of esrp1 in solid tumor development through the regulation of cd44 splicing and emt processes. Frontiers in Oncology, Feb 2025. URL: https://doi.org/10.3389/fonc.2025.1451130, doi:10.3389/fonc.2025.1451130. This article has 6 citations.

4. (peart2022theglobalproteinrna pages 4-6): Natoya J. Peart, Jae Yeon Hwang, Mathieu Quesnel-Vallières, Matthew J. Sears, Yuequin Yang, Peter Stoilov, Yoseph Barash, Juw Won Park, Kristen W. Lynch, and Russ P. Carstens. The global protein-rna interaction map of esrp1 defines a post-transcriptional program that is essential for epithelial cell function. Oct 2022. URL: https://doi.org/10.1016/j.isci.2022.105205, doi:10.1016/j.isci.2022.105205. This article has 14 citations and is from a peer-reviewed journal.

5. (liu2024esrp1controlsbiogenesis pages 1-2): Dawei Liu, B Kate Dredge, Andrew G Bert, Katherine A Pillman, John Toubia, Wenting Guo, Boris J A Dyakov, Melodie M Migault, Vanessa M Conn, Simon J Conn, Philip A Gregory, Anne-Claude Gingras, Dinshaw Patel, Baixing Wu, and Gregory J Goodall. Esrp1 controls biogenesis and function of a large abundant multiexon circrna. Nucleic Acids Research, 52:1387-1403, Nov 2024. URL: https://doi.org/10.1093/nar/gkad1138, doi:10.1093/nar/gkad1138. This article has 31 citations and is from a highest quality peer-reviewed journal.

6. (peart2022theglobalproteinrna pages 1-2): Natoya J. Peart, Jae Yeon Hwang, Mathieu Quesnel-Vallières, Matthew J. Sears, Yuequin Yang, Peter Stoilov, Yoseph Barash, Juw Won Park, Kristen W. Lynch, and Russ P. Carstens. The global protein-rna interaction map of esrp1 defines a post-transcriptional program that is essential for epithelial cell function. Oct 2022. URL: https://doi.org/10.1016/j.isci.2022.105205, doi:10.1016/j.isci.2022.105205. This article has 14 citations and is from a peer-reviewed journal.

7. (kwon2023roleofepithelial pages 1-2): Mi Jeong Kwon. Role of epithelial splicing regulatory protein 1 in cancer progression. Cancer Cell International, Dec 2023. URL: https://doi.org/10.1186/s12935-023-03180-6, doi:10.1186/s12935-023-03180-6. This article has 19 citations and is from a peer-reviewed journal.

8. (bebee2015thesplicingregulators pages 1-2): Thomas W Bebee, Juw Won Park, Katherine I Sheridan, Claude C Warzecha, Benjamin W Cieply, Alex M Rohacek, Yi Xing, and Russ P Carstens. The splicing regulators esrp1 and esrp2 direct an epithelial splicing program essential for mammalian development. eLife, Sep 2015. URL: https://doi.org/10.7554/elife.08954, doi:10.7554/elife.08954. This article has 173 citations and is from a domain leading peer-reviewed journal.

9. (bebee2015thesplicingregulators pages 2-3): Thomas W Bebee, Juw Won Park, Katherine I Sheridan, Claude C Warzecha, Benjamin W Cieply, Alex M Rohacek, Yi Xing, and Russ P Carstens. The splicing regulators esrp1 and esrp2 direct an epithelial splicing program essential for mammalian development. eLife, Sep 2015. URL: https://doi.org/10.7554/elife.08954, doi:10.7554/elife.08954. This article has 173 citations and is from a domain leading peer-reviewed journal.

10. (bhate2015esrp2controlsan pages 1-2): Amruta Bhate, Darren J. Parker, Thomas W. Bebee, Jaegyoon Ahn, Waqar Arif, Edrees H. Rashan, Sandip Chorghade, Anthony Chau, Jae-Hyung Lee, Sayeepriyadarshini Anakk, Russ P. Carstens, Xinshu Xiao, and Auinash Kalsotra. Esrp2 controls an adult splicing programme in hepatocytes to support postnatal liver maturation. Nature Communications, Nov 2015. URL: https://doi.org/10.1038/ncomms9768, doi:10.1038/ncomms9768. This article has 117 citations and is from a highest quality peer-reviewed journal.

11. (derham2023thediscoveryfunction pages 6-7): Jessica M. Derham and Auinash Kalsotra. The discovery, function, and regulation of epithelial splicing regulatory proteins (esrp) 1 and 2. Biochemical Society transactions, 51:1097-1109, Jun 2023. URL: https://doi.org/10.1042/bst20221124, doi:10.1042/bst20221124. This article has 18 citations and is from a peer-reviewed journal.

12. (li2023regulationofepithelialmesenchymal pages 1-2): Ling Li, Jinxia Zheng, and Sebastian Oltean. Regulation of epithelial-mesenchymal transitions by alternative splicing: potential new area for cancer therapeutics. Genes, 14:2001, Oct 2023. URL: https://doi.org/10.3390/genes14112001, doi:10.3390/genes14112001. This article has 8 citations.

13. (carroll2020anirf6esrp12regulatory pages 1-4): Shannon H. Carroll, Claudio Macias Trevino, Edward B. Li, Kenta Kawasaki, Nikita Myers, Shawn A. Hallett, Nora Alhazmi, Justin Cotney, Russ P. Carstens, and Eric C. Liao. An irf6-esrp1/2 regulatory axis controls midface morphogenesis in vertebrates. Development (Cambridge, England), Jan 2020. URL: https://doi.org/10.1242/dev.194498, doi:10.1242/dev.194498. This article has 32 citations.

## Artifacts

- [Edison artifact artifact-00](PTHR13976-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR13976-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](PTHR13976-deep-research-falcon_artifacts/artifact-02.md)

## Citations

1. derham2023thediscoveryfunction pages 3-4
2. peart2022theglobalproteinrna pages 4-6
3. wang2025theroleof pages 1-2
4. peart2022theglobalproteinrna pages 1-2
5. derham2023thediscoveryfunction pages 1-3
6. kwon2023roleofepithelial pages 1-2
7. bebee2015thesplicingregulators pages 1-2
8. bebee2015thesplicingregulators pages 2-3
9. derham2023thediscoveryfunction pages 6-7
10. li2023regulationofepithelialmesenchymal pages 1-2
11. https://doi.org/10.1042/bst20221124,
12. https://doi.org/10.3389/fonc.2025.1451130,
13. https://doi.org/10.1016/j.isci.2022.105205,
14. https://doi.org/10.1093/nar/gkad1138,
15. https://doi.org/10.1186/s12935-023-03180-6,
16. https://doi.org/10.7554/elife.08954,
17. https://doi.org/10.1038/ncomms9768,
18. https://doi.org/10.3390/genes14112001,
19. https://doi.org/10.1242/dev.194498,