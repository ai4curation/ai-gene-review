---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-28T20:45:59.247847'
end_time: '2026-06-28T21:13:54.921367'
duration_seconds: 1675.67
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR14098
  interpro_name: Immunoreceptor signaling adapters
  interpro_short_name: Immunoreceptor_sig_adapters
  interpro_type: family
  interpro_integrated: IPR051751
  member_databases: Not specified
  n_proteins: '4117'
  n_taxa: '3321'
  n_subfamilies: '7'
  interpro2go_terms: None mapped (no InterPro2GO terms for this entry)
  interpro_description: This family of proteins includes adapters and linkers that
    play critical roles in immunoreceptor signaling pathways. They are involved in
    the regulation of signaling cascades downstream of various receptors such as T-cell
    antigen receptors, B-cell antigen receptors, and mast cell degranulation receptors.
    These proteins mediate interactions through SH2 domains and proline-rich regions,
    facilitating the activation of kinases, the mobilization of calcium, and the activation
    of transcription factors like NF-kappa-B and NFAT. They are essential for various
    cellular processes including cell development, activation, and apoptosis. Some
    members are also implicated in the negative regulation of natural killer cell-activating
    receptors and the production of interferon-gamma, as well as in promoting reactive
    oxidative species generation and necrosis.
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 41
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PTHR14098-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR14098-deep-research-falcon_artifacts/artifact-01.md
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
- **Accession:** PTHR14098
- **Name:** Immunoreceptor signaling adapters
- **Short name:** Immunoreceptor_sig_adapters
- **Entry type:** family
- **Integrated into / parent:** IPR051751
- **Member database signatures:** Not specified
- **Scale:** 4117 proteins across 3321 taxa, 7 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** This family of proteins includes adapters and linkers that play critical roles in immunoreceptor signaling pathways. They are involved in the regulation of signaling cascades downstream of various receptors such as T-cell antigen receptors, B-cell antigen receptors, and mast cell degranulation receptors. These proteins mediate interactions through SH2 domains and proline-rich regions, facilitating the activation of kinases, the mobilization of calcium, and the activation of transcription factors like NF-kappa-B and NFAT. They are essential for various cellular processes including cell development, activation, and apoptosis. Some members are also implicated in the negative regulation of natural killer cell-activating receptors and the production of interferon-gamma, as well as in promoting reactive oxidative species generation and necrosis.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR14098 (Immunoreceptor signaling adapters)**, structured to support GO annotation review.

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
- **Accession:** PTHR14098
- **Name:** Immunoreceptor signaling adapters
- **Short name:** Immunoreceptor_sig_adapters
- **Entry type:** family
- **Integrated into / parent:** IPR051751
- **Member database signatures:** Not specified
- **Scale:** 4117 proteins across 3321 taxa, 7 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** This family of proteins includes adapters and linkers that play critical roles in immunoreceptor signaling pathways. They are involved in the regulation of signaling cascades downstream of various receptors such as T-cell antigen receptors, B-cell antigen receptors, and mast cell degranulation receptors. These proteins mediate interactions through SH2 domains and proline-rich regions, facilitating the activation of kinases, the mobilization of calcium, and the activation of transcription factors like NF-kappa-B and NFAT. They are essential for various cellular processes including cell development, activation, and apoptosis. Some members are also implicated in the negative regulation of natural killer cell-activating receptors and the production of interferon-gamma, as well as in promoting reactive oxidative species generation and necrosis.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR14098 (Immunoreceptor signaling adapters)**, structured to support GO annotation review.

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


# Comprehensive Research Report: PTHR14098 — Immunoreceptor Signaling Adapters

## 1. Family Definition and Biochemistry

### 1.1 Overview

PTHR14098 (Immunoreceptor signaling adapters) is a PANTHER family-level entry encompassing a heterogeneous collection of adaptor and linker proteins that function as non-enzymatic scaffolds downstream of immunoreceptors. These proteins lack catalytic or transcriptional activity; instead, they organize multiprotein signaling complexes (signalosomes) by providing docking sites for SH2-domain-containing, SH3-domain-containing, and other interaction-module-containing proteins (rudd1999adaptorsandmolecular pages 1-2, borowicz2020adaptorproteinsflexible pages 6-9). The family spans 4,117 proteins across 3,321 taxa with 7 recognized subfamilies.

### 1.2 Structural Features

The family includes two structurally distinct classes of adaptors:

**Transmembrane adaptor proteins (TRAPs/pTRAPs):** These are integral membrane proteins with short extracellular domains, a single transmembrane helix, and relatively long cytoplasmic tails containing multiple tyrosine-based signaling motifs (TBSMs). TRAPs generally lack classical ITAMs and do not directly associate with immunoreceptors. Their primary function is to provide multiple docking sites for SH2-domain-containing cytosolic signaling molecules, thereby organizing membrane-proximal signaling assemblies (horejsi2004transmembraneadaptorproteins pages 1-2, simeoni2004adaptorsandlinkers pages 4-5). Key members include LAT, NTAL/LAB/LAT2, LAX, SIT, LIME, and TRIM.

**Cytosolic adaptor proteins:** These contain modular protein-protein interaction domains. SLP-76, for example, contains an N-terminal SAM (sterile alpha motif) domain, an acidic region with tyrosine motifs (YESP, YEPP), a proline-rich region, and a C-terminal SH2 domain (rudd1999adaptorsandmolecular pages 2-3, rudd1999adaptorsandmolecular pages 1-2). BLNK/SLP-65 is the B-cell functional counterpart with analogous domain architecture.

A defining characteristic of this family is that the cytoplasmic regions are largely **intrinsically disordered**. These disordered regions provide accessibility for binding domains since the motifs are continually exposed, enabling high specificity with low affinity interactions—ideal for reversible signaling hubs (borowicz2020adaptorproteinsflexible pages 9-12, borowicz2020adaptorproteinsflexible pages 12-14). LAT has been specifically described as a "TCR-proximal disordered adapter protein" whose cytoplasmic tail functions as a "protein fishing line" with multiple SH2- and PTB-binding motifs, providing a larger capture radius than compact folded proteins through a "fly-casting mechanism" (fernandezaguilar2023astoryof pages 9-11, borowicz2020adaptorproteinsflexible pages 12-14).

Recent comprehensive mutagenesis by Rubin et al. (2024) identified functional regions spanning over 40% of the LAT amino acid sequence, with conserved sequence motifs for protein interactions alongside charge distribution as critical sequence features. Notably, total charge extent and distribution, rather than individual charged residues, proved functionally important (rubin2024latencodest pages 9-11, rubin2024latencodest pages 9-9).

### 1.3 Mechanistic Function

Upon immunoreceptor engagement, kinases such as ZAP-70 phosphorylate the tyrosine residues on LAT's cytoplasmic tail. Phosphorylated LAT then recruits PLC-γ1 (via its C-terminal SH2 domain at Tyr132), the Gads-SLP-76 complex (at Tyr171, Tyr191), and GRB2 (at Tyr171, Tyr191, Tyr226), forming the LAT signalosome (fernandezaguilar2023astoryof pages 9-11, samelson2002signaltransductionmediated pages 13-15). This signalosome drives calcium mobilization, Ras/MAPK activation, and transcription factor activation (NF-AT, NF-κB, AP-1) (rudd1999adaptorsandmolecular pages 1-2, rudd1999adaptorsandmolecular pages 2-3).

Recent work has revealed that LAT-based signaling complexes form **biomolecular condensates** through liquid-liquid phase separation. The multivalency of interactions between LAT, GRB2, SOS1, SLP-76, and PLC-γ1 drives the formation of higher-order signaling condensates at the plasma membrane (nicolas2022systemslevelconservationof pages 13-13, borowicz2020adaptorproteinsflexible pages 12-14).

The representative member proteins of the PTHR14098 family and their key features are summarized in the following table:

| Protein | Alternative names | Structural type | Primary cell types | Regulatory role | Key binding partners / distinguishing features |
|---|---|---|---|---|---|
| LAT | Linker for activation of T cells | Transmembrane adaptor (palmitoylated TRAP) | T cells; also NK cells, mast cells, platelets, pre-B cells | Mostly positive; can also recruit negative regulators in some contexts | Phosphorylated LAT recruits GRB2, GADS, PLC-γ1, and thereby nucleates LAT-SLP-76 signalosomes; essential hub for TCR signaling and also used in FcεRI/NK pathways (horejsi2004transmembraneadaptorproteins pages 12-13, horejsi2004transmembraneadaptorproteins pages 5-6, horejsi2004transmembraneadaptorproteins pages 4-5, curson2018ptrapstransmembraneadaptors pages 2-3, fernandezaguilar2023astoryof pages 9-11) |
| NTAL / LAB / LAT2 | Non-T cell activation linker; Linker for activation of B cells; LAT family member 2 | Transmembrane adaptor (palmitoylated TRAP) | B cells, NK cells, mast cells, monocytes/macrophages; induced in activated T cells | Dual: often negative in T and B cells, but cooperative/positive in mast cells or LAT-deficient settings | Associates with GRB2, GAB1, CBL; notably lacks PLC-γ/SLP binding seen for LAT; can partially complement LAT yet suppress TCR calcium/PLC-γ1 signaling in T cells (simeoni2004adaptorsandlinkers pages 5-6, stepanek2014palmitoylatedtransmembraneadaptor pages 2-3, narbonasanchez2023expressionofnont pages 1-2, narbonasanchez2023expressionofnont pages 8-10, horejsi2004transmembraneadaptorproteins pages 6-7) |
| LAX | Linker for activation of X cells | Transmembrane adaptor (non-raft TRAP) | T cells, B cells, other hematopoietic cells | Predominantly negative | Contains GRB2- and GADS-binding sites; thought to sequester these from LAT and limit MAPK/p38 activation rather than reconstitute LAT-like signaling (horejsi2004transmembraneadaptorproteins pages 11-12, horejsi2004transmembraneadaptorproteins pages 10-11) |
| SIT | SHP2-interacting transmembrane adaptor protein | Transmembrane adaptor (non-raft TRAP) | Mainly T cells / hematopoietic cells | Predominantly negative | Binds inhibitory factors including SHP2 and CSK; overexpression and knockout data support inhibitory control of TCR signaling (horejsi2004transmembraneadaptorproteins pages 11-12, horejsi2004transmembraneadaptorproteins pages 10-11) |
| LIME | Lck-interacting membrane protein | Transmembrane adaptor (palmitoylated TRAP) | Peripheral T cells; also reported in B cells | Positive to dual/modulatory | Associates with LCK/Src-family signaling; enhances Ca2+ flux, IL-2 transcription, adhesion, and synapse formation, but some studies also suggest inhibitory/modulatory effects in resting cells (simeoni2004adaptorsandlinkers pages 5-6, horejsi2004transmembraneadaptorproteins pages 10-11, stepanek2014palmitoylatedtransmembraneadaptor pages 2-3, stepanek2014palmitoylatedtransmembraneadaptor pages 5-6) |
| TRIM | TCR-interacting molecule | Transmembrane adaptor | T cells | Modulatory / incompletely resolved | Associates with TCR-CD3-ζ complex and regulates cell-surface TCR expression; less well characterized than LAT/LAX/SIT (horejsi2004transmembraneadaptorproteins pages 10-11) |
| SLP-76 | SH2 domain-containing leukocyte protein of 76 kDa; LCP2 | Cytosolic adaptor | T cells, NK-lineage and other hematopoietic cells | Positive | Modular adaptor with SAM domain, phosphotyrosine motifs, proline-rich region, and SH2 domain; binds GADS, VAV, NCK, PLC-γ1-linked complexes and is recruited to LAT signalosomes (rudd1999adaptorsandmolecular pages 1-2, rudd1999adaptorsandmolecular pages 2-3, nicolas2022systemslevelconservationof pages 13-13) |
| BLNK / SLP-65 | B-cell linker protein; SLP-65 | Cytosolic adaptor | B cells, especially pre-B and mature B cells | Positive in BCR signaling; also tumor-suppressive in pre-B development | Functional B-cell counterpart of SLP-76; organizes BCR signaling, calcium responses, and pre-B-cell transition; loss causes developmental defects and leukemogenic predisposition (horejsi2004transmembraneadaptorproteins pages 12-13, simeoni2004adaptorsandlinkers pages 4-5, simeoni2004adaptorsandlinkers pages 5-6, rudd1999adaptorsandmolecular pages 2-3) |
| CLNK / MIST | Cytokine-dependent hematopoietic cell linker; Mast cell immunoreceptor signal transducer | Cytosolic adaptor | Cytokine-stimulated hematopoietic cells, mast cells, some lymphoid contexts | Positive / context-dependent substitute for SLP-76 family signaling | SLP-76-family adaptor that can functionally substitute for SLP-76 in some immunoreceptor signaling settings; induced in hematopoietic contexts rather than being a universal T-cell adaptor (horejsi2004transmembraneadaptorproteins pages 12-13) |


*Table: This table summarizes representative adaptor proteins captured within the PTHR14098 immunoreceptor signaling adapters family, highlighting their structural class, cell-type usage, regulatory direction, and binding logic. It is useful for GO review because it shows that the family spans both positive and negative regulators across distinct immune lineages.*

## 2. InterPro2GO Mapping Appropriateness

PTHR14098 currently has **no InterPro2GO terms mapped**. This analysis concludes that the absence of mapped GO terms is **appropriate and should be maintained**, given the extreme functional heterogeneity of this family. The following table evaluates candidate GO terms:

| Candidate GO term | Aspect | True for **all** PTHR14098 members? | Problem if applied at family level | Recommendation |
|---|---|---:|---|---|
| GO:0007166 cell surface receptor signaling pathway | BP | No | Too broad and still not universal: members act downstream of different receptors (TCR, BCR, FcεRI, NK receptors, platelet receptors), and some are negative regulators rather than generic pathway executors; would overgeneralize across distinct subfamilies and cell types (horejsi2004transmembraneadaptorproteins pages 5-6, horejsi2004transmembraneadaptorproteins pages 11-12, curson2018ptrapstransmembraneadaptors pages 2-3, horejsi2004transmembraneadaptorproteins pages 7-8) | DO NOT ADD |
| GO:0050851 antigen receptor-mediated signaling pathway | BP | No | Fits LAT/SLP-76/BLNK/CLNK lineages better than the whole family, but excludes or weakly fits some TRAPs with inhibitory/modulatory roles and members acting outside classic antigen receptor pathways; also not valid for all mast-cell/platelet-focused members (horejsi2004transmembraneadaptorproteins pages 12-13, stepanek2014palmitoylatedtransmembraneadaptor pages 2-3, horejsi2004transmembraneadaptorproteins pages 7-8) | ADD AT SUBFAMILY LEVEL |
| GO:0006468 protein phosphorylation | BP | No | Family members are mostly non-enzymatic adaptors/scaffolds that are **phosphorylated** and recruit kinases/phosphatases rather than catalyze phosphorylation; would misstate biochemical role (rudd1999adaptorsandmolecular pages 1-2, borowicz2020adaptorproteinsflexible pages 12-14, borowicz2020adaptorproteinsflexible pages 6-9) | DO NOT ADD |
| GO:0005829 cytosol | CC | No | Some family members are cytosolic (SLP-76, BLNK), but many are transmembrane adaptors localized at the plasma membrane or membrane microdomains; mixed localization makes this false at family level (horejsi2004transmembraneadaptorproteins pages 1-2, simeoni2004adaptorsandlinkers pages 4-5, rudd1999adaptorsandmolecular pages 1-2) | ADD AT SUBFAMILY LEVEL |
| GO:0005886 plasma membrane | CC | No | Correct for LAT/NTAL/LAX/SIT/LIME/TRIM-type transmembrane adaptors, but false for cytosolic members such as SLP-76 and BLNK; family spans both compartments (horejsi2004transmembraneadaptorproteins pages 1-2, simeoni2004adaptorsandlinkers pages 4-5, rudd1999adaptorsandmolecular pages 1-2) | ADD AT SUBFAMILY LEVEL |
| GO:0019901 protein kinase binding | MF | No | Many members recruit kinases or participate in kinase-containing complexes, but evidence is member-specific and not universal across all subfamilies; also too interaction-generic for a large heterogeneous family (rudd1999adaptorsandmolecular pages 1-2, borowicz2020adaptorproteinsflexible pages 14-17, borowicz2020adaptorproteinsflexible pages 6-9) | ADD AT SUBFAMILY LEVEL |
| GO:0042803 protein homodimerization activity | MF | No | Not a defining property of the family; signaling often depends on multivalent clustering/condensates rather than demonstrated homodimerization of every member, and evidence is not universal (borowicz2020adaptorproteinsflexible pages 14-17, nicolas2022systemslevelconservationof pages 13-13, rubin2024latencodest pages 16-18) | DO NOT ADD |
| GO:0035556 intracellular signal transduction | BP | No | Very plausible for many members, but still over-broad and not safely universal because the family contains both positive and negative regulators operating in distinct receptor contexts; adds little specificity and risks blanket propagation (borowicz2020adaptorproteinsflexible pages 12-14, borowicz2020adaptorproteinsflexible pages 14-17, borowicz2020adaptorproteinsflexible pages 6-9) | ACCEPTABLE IF GENERIC |
| GO:0042110 T cell activation | BP | No | Strongly false for B-cell, mast-cell, NK-cell, monocyte/macrophage, and platelet-associated members such as BLNK and NTAL/LAB; clear taxa/cell-type leakage (horejsi2004transmembraneadaptorproteins pages 5-6, stepanek2014palmitoylatedtransmembraneadaptor pages 2-3, curson2018ptrapstransmembraneadaptors pages 2-3, horejsi2004transmembraneadaptorproteins pages 7-8) | ADD AT SUBFAMILY LEVEL |
| GO:0050776 regulation of immune response | BP | No | Family includes both positive and negative regulators, and the regulated process varies widely by lineage and receptor system; too broad to be biologically useful and not demonstrably universal (horejsi2004transmembraneadaptorproteins pages 11-12, horejsi2004transmembraneadaptorproteins pages 10-11, narbonasanchez2023expressionofnont pages 1-2, narbonasanchez2023expressionofnont pages 8-10) | ACCEPTABLE IF GENERIC |
| GO:0005515 protein binding | MF | No | Trivially true for adaptors but too generic to be informative; not recommended for InterPro2GO family-level propagation because it adds minimal value and obscures mechanistic differences (borowicz2020adaptorproteinsflexible pages 12-14, borowicz2020adaptorproteinsflexible pages 6-9) | ACCEPTABLE IF GENERIC |


*Table: This table reviews candidate GO terms that might be considered for InterPro entry PTHR14098 and assesses whether they are safe to propagate to all matched proteins. It is useful for deciding which terms should remain unmapped at family level versus being restricted to narrower subfamilies.*

**Key reasons no GO terms should be applied at the family level:**

- **Opposing regulatory directions:** LAT and SLP-76 are positive regulators of immunoreceptor signaling, while LAX and SIT are primarily negative regulators that suppress TCR signaling by sequestering GRB2/GADS or recruiting inhibitory phosphatases SHP2 and CSK (horejsi2004transmembraneadaptorproteins pages 11-12, horejsi2004transmembraneadaptorproteins pages 10-11). NTAL/LAT2 exhibits dual regulatory character, acting as a negative regulator in T cells but cooperating with LAT positively in mast cell FcεRI signaling (stepanek2014palmitoylatedtransmembraneadaptor pages 2-3, narbonasanchez2023expressionofnont pages 1-2, narbonasanchez2023expressionofnont pages 8-10).

- **Distinct cell-type expression:** LAT operates in T cells, NK cells, mast cells, and platelets; BLNK/SLP-65 is B-cell-specific; NTAL is expressed in B cells, NK cells, mast cells, and monocytes but not resting T cells (horejsi2004transmembraneadaptorproteins pages 5-6, stepanek2014palmitoylatedtransmembraneadaptor pages 2-3). Mapping a term like "T cell activation" (GO:0042110) would be categorically false for BLNK and other B-cell/mast-cell-specific members.

- **Mixed compartmentalization:** The family includes both transmembrane (LAT, NTAL, LAX, SIT) and cytosolic (SLP-76, BLNK) members, making cellular component terms inapplicable at the family level (horejsi2004transmembraneadaptorproteins pages 1-2, simeoni2004adaptorsandlinkers pages 4-5).

## 3. Functional Divergence Across the Family

### 3.1 Positive vs. Negative Regulators (Neo-functionalization)

The most striking functional divergence within the family is between activating and inhibitory members:

- **LAT** is a master positive switch for T-cell activation—LAT-deficient T cells are completely unable to signal through the TCR (stepanek2014palmitoylatedtransmembraneadaptor pages 2-3, horejsi2004transmembraneadaptorproteins pages 11-12). LAT also positively regulates FcεRI signaling in mast cells and NK cell cytotoxicity (curson2018ptrapstransmembraneadaptors pages 2-3, horejsi2004transmembraneadaptorproteins pages 4-5).

- **NTAL/LAT2** exemplifies context-dependent neo-functionalization. Despite being structurally homologous to LAT, NTAL acts primarily as a **negative regulator** of TCR signaling in T cells, reducing calcium flux and PLC-γ1 activation. NTAL-knockout mice develop autoimmune pathology with splenomegaly and autoantibodies, confirming its suppressive role (narbonasanchez2023expressionofnont pages 1-2, narbonasanchez2023expressionofnont pages 8-10). However, in mast cells, NTAL cooperates with LAT for FcεRI-mediated degranulation, and in LAT-deficient mast cells, NTAL can partially compensate as a positive regulator (horejsi2004transmembraneadaptorproteins pages 7-8). This dual character arises because NTAL lacks the PLC-γ1 binding site present on LAT (horejsi2004transmembraneadaptorproteins pages 6-7).

- **LAX** functions as an inhibitory adaptor by sequestering GRB2 and GADS away from LAT, thereby limiting MAPK pathway activation. LAX fails to reconstitute TCR-mediated signaling in LAT-deficient cells and instead suppresses p38 MAPK activation (horejsi2004transmembraneadaptorproteins pages 11-12, horejsi2004transmembraneadaptorproteins pages 10-11).

- **SIT** binds inhibitory signaling molecules SHP2 and CSK, and SIT-deficient mice confirm its role as a negative regulator of T-cell activation (horejsi2004transmembraneadaptorproteins pages 11-12).

### 3.2 Cell-type Specialization

**SLP-76** and **BLNK/SLP-65** represent a clear case of lineage-specific specialization. SLP-76 is the essential cytosolic adaptor for T-cell TCR signaling, while BLNK serves the equivalent function downstream of the BCR in B cells. CLNK/MIST can functionally substitute for SLP-76 in some immunoreceptor signaling contexts (horejsi2004transmembraneadaptorproteins pages 12-13, simeoni2004adaptorsandlinkers pages 4-5). The B-cell adaptor BLNK additionally functions as a **tumor suppressor** in pre-B cell development, with BLNK loss predisposing to pre-B cell leukemia—a function entirely distinct from its signaling scaffold role (rudd1999adaptorsandmolecular pages 2-3).

### 3.3 Fine-tuning Through Weak Interactions

Yamane et al. (2025) demonstrated that the weak SLP-76–PLC-γ1 interaction (Kd ~2.4 µM) within the LAT signalosome is a conserved checkpoint for fine-tuning TCR signal strength. Enhancing this interaction increased PLC-γ1 activity and altered thymocyte development and peripheral T-cell responses, indicating that the weak affinity is functionally optimized (yamane2025weakslp76plcγ1interaction pages 1-5, yamane2025weakslp76plcγ1interaction pages 13-17).

### 3.4 Recent Applications

In a clinically relevant development, Rotiroti et al. (2025) engineered a **membrane-tethered version of SLP-76 (MT-SLP-76)** to amplify CAR-T cell signaling, overcoming antigen-low resistance in cancer therapy by enhancing recruitment of ITK and PLCγ1. This highlights the therapeutic exploitation of adaptor protein biology (yamane2025weakslp76plcγ1interaction pages 1-5).

## 4. Taxonomic Scope

The PTHR14098 family encompasses 4,117 proteins across 3,321 taxa, indicating broad representation across jawed vertebrates (Gnathostomata). Key evidence for taxonomic distribution includes:

- **Conservation across jawed vertebrates:** The SLP-76–PLC-γ1 binding sites are highly conserved from cartilaginous fish to placental mammals. Yamane et al. (2025) examined nineteen orthologs across jawed vertebrates and confirmed conservation of this interaction (yamane2025weakslp76plcγ1interaction pages 1-5, yamane2025weakslp76plcγ1interaction pages 61-63). Sequence alignments show conservation of SLP-76 proline-rich regions across human, monkey, mouse, rabbit, cow, bat, and shrew (yamane2025weakslp76plcγ1interaction pages 52-54).

- **Systems-level conservation between mice and humans:** Nicolas et al. (2022) demonstrated that 13 of 17 SLP-76-prey interactions and 9 of 10 LAT-prey interactions found in human CD4+ T cells were conserved in mouse CD4+ T cells, with a strong correlation in interaction stoichiometries (Pearson r = 0.83) (nicolas2022systemslevelconservationof pages 10-11, nicolas2022systemslevelconservationof pages 9-10).

- **Presence in teleost fish:** SLP-76 orthologs have been identified in fish species such as common carp, and TCR signaling components including LAT and ZAP-70 have been characterized in zebrafish and other ray-finned fish, consistent with the emergence of adaptive immunity in early gnathostomes.

The broad vertebrate distribution is consistent with the family matching proteins in organisms that possess adaptive immune systems. However, the immunoreceptor signaling context (TCR, BCR, FcR pathways) is restricted to jawed vertebrates. GO terms referencing specific immune processes would be valid across this taxonomic range, but the extreme functional heterogeneity among subfamilies remains the primary barrier to family-level annotation, not taxonomic scope.

## 5. Over-Annotation Verdict

### Summary Assessment

The current state of PTHR14098's InterPro2GO mapping—**no GO terms mapped**—is **sound and appropriate**. This family exhibits extreme functional heterogeneity that precludes safe propagation of any biologically meaningful GO term to all 4,117 matched proteins.

### Specific Justifications

1. **Regulatory polarity divergence:** The family contains both strong positive regulators (LAT, SLP-76) and dedicated negative regulators (LAX, SIT, NTAL in T cells) of immunoreceptor signaling. Any process term implying "positive regulation" or even neutral "regulation" of a specific pathway would be false for a substantial fraction of family members (horejsi2004transmembraneadaptorproteins pages 11-12, narbonasanchez2023expressionofnont pages 1-2).

2. **Cell-type restriction:** Members are specialized for different immune cell lineages—SLP-76 for T cells, BLNK for B cells, and various TRAPs for mast cells, NK cells, and platelets. No immune-process term applies uniformly (horejsi2004transmembraneadaptorproteins pages 5-6, stepanek2014palmitoylatedtransmembraneadaptor pages 2-3).

3. **Mixed structural classes:** The family includes both transmembrane and cytosolic proteins, rendering cellular component terms inapplicable at this level (horejsi2004transmembraneadaptorproteins pages 1-2).

4. **Generic terms add no value:** While "protein binding" (GO:0005515) or "intracellular signal transduction" (GO:0035556) might be technically defensible, they are too uninformative for meaningful annotation and are generally avoided in InterPro2GO curation (borowicz2020adaptorproteinsflexible pages 6-9).

### Recommended GO Action Pattern

| Action | Detail |
|---|---|
| **For the family entry (PTHR14098):** | **ACCEPT** the current status of no InterPro2GO mappings. |
| **For subfamily entries:** | GO terms should be assigned at the **7 subfamilies level**, where functional homogeneity allows accurate annotation. For example, a LAT subfamily could receive GO:0050851 (antigen receptor-mediated signaling pathway), GO:0005886 (plasma membrane); an SLP-76 subfamily could receive GO:0050851, GO:0005829 (cytosol); BLNK could receive GO:0050853 (B cell receptor signaling pathway). |
| **InterPro structural recommendation:** | Consider whether the 7 subfamilies adequately capture the major functional splits. The positive-regulator TRAPs (LAT, LIME), negative-regulator TRAPs (LAX, SIT), dual-character TRAPs (NTAL), and cytosolic adaptors (SLP-76 family, BLNK) should ideally correspond to distinct child entries with subfamily-specific GO mappings. |

### Conclusion

PTHR14098 represents a textbook case where a protein family defined by sequence homology and shared evolutionary origin encompasses functionally divergent—and in some cases functionally opposing—members. The absence of InterPro2GO terms reflects appropriate curation restraint. Any future GO annotation efforts should focus exclusively on well-defined subfamilies where functional homogeneity has been experimentally validated.

References

1. (rudd1999adaptorsandmolecular pages 1-2): Christopher E. Rudd. Adaptors and molecular scaffolds in immune cell signaling. Cell, 96:5-8, Jan 1999. URL: https://doi.org/10.1016/s0092-8674(00)80953-8, doi:10.1016/s0092-8674(00)80953-8. This article has 286 citations and is from a highest quality peer-reviewed journal.

2. (borowicz2020adaptorproteinsflexible pages 6-9): Paweł Borowicz, Hanna Chan, Anette Hauge, and Anne Spurkland. Adaptor proteins: flexible and dynamic modulators of immune cell signalling. Scandinavian Journal of Immunology, Oct 2020. URL: https://doi.org/10.1111/sji.12951, doi:10.1111/sji.12951. This article has 39 citations and is from a peer-reviewed journal.

3. (horejsi2004transmembraneadaptorproteins pages 1-2): Václav Hořejší, Weiguo Zhang, and Burkhart Schraven. Transmembrane adaptor proteins: organizers of immunoreceptor signalling. Nature Reviews Immunology, 4:603-616, Aug 2004. URL: https://doi.org/10.1038/nri1414, doi:10.1038/nri1414. This article has 305 citations and is from a highest quality peer-reviewed journal.

4. (simeoni2004adaptorsandlinkers pages 4-5): Luca Simeoni, Stefanie Kliche, Jonathan Lindquist, and Burkhart Schraven. Adaptors and linkers in t and b cells. Current opinion in immunology, 16 3:304-13, Jun 2004. URL: https://doi.org/10.1016/j.coi.2004.03.001, doi:10.1016/j.coi.2004.03.001. This article has 87 citations and is from a peer-reviewed journal.

5. (rudd1999adaptorsandmolecular pages 2-3): Christopher E. Rudd. Adaptors and molecular scaffolds in immune cell signaling. Cell, 96:5-8, Jan 1999. URL: https://doi.org/10.1016/s0092-8674(00)80953-8, doi:10.1016/s0092-8674(00)80953-8. This article has 286 citations and is from a highest quality peer-reviewed journal.

6. (borowicz2020adaptorproteinsflexible pages 9-12): Paweł Borowicz, Hanna Chan, Anette Hauge, and Anne Spurkland. Adaptor proteins: flexible and dynamic modulators of immune cell signalling. Scandinavian Journal of Immunology, Oct 2020. URL: https://doi.org/10.1111/sji.12951, doi:10.1111/sji.12951. This article has 39 citations and is from a peer-reviewed journal.

7. (borowicz2020adaptorproteinsflexible pages 12-14): Paweł Borowicz, Hanna Chan, Anette Hauge, and Anne Spurkland. Adaptor proteins: flexible and dynamic modulators of immune cell signalling. Scandinavian Journal of Immunology, Oct 2020. URL: https://doi.org/10.1111/sji.12951, doi:10.1111/sji.12951. This article has 39 citations and is from a peer-reviewed journal.

8. (fernandezaguilar2023astoryof pages 9-11): Luis M. Fernández-Aguilar, Inmaculada Vico-Barranco, Mikel M. Arbulo-Echevarria, and Enrique Aguado. A story of kinases and adaptors: the role of lck, zap-70 and lat in switch panel governing t-cell development and activation. Biology, 12:1163, Aug 2023. URL: https://doi.org/10.3390/biology12091163, doi:10.3390/biology12091163. This article has 54 citations.

9. (rubin2024latencodest pages 9-11): Adam J. Rubin, Tyler T. Dao, Amelia V. Schueppert, Aviv Regev, and Alex K. Shalek. Lat encodes t cell activation pathway balance. bioRxiv, Aug 2024. URL: https://doi.org/10.1101/2024.08.26.609683, doi:10.1101/2024.08.26.609683. This article has 3 citations.

10. (rubin2024latencodest pages 9-9): Adam J. Rubin, Tyler T. Dao, Amelia V. Schueppert, Aviv Regev, and Alex K. Shalek. Lat encodes t cell activation pathway balance. bioRxiv, Aug 2024. URL: https://doi.org/10.1101/2024.08.26.609683, doi:10.1101/2024.08.26.609683. This article has 3 citations.

11. (samelson2002signaltransductionmediated pages 13-15): Lawrence E. Samelson. Signal transduction mediated by the t cell antigen receptor: the role of adapter proteins. Annual review of immunology, 20:371-94, Apr 2002. URL: https://doi.org/10.1146/annurev.immunol.20.092601.111357, doi:10.1146/annurev.immunol.20.092601.111357. This article has 784 citations and is from a highest quality peer-reviewed journal.

12. (nicolas2022systemslevelconservationof pages 13-13): Philippe Nicolas, Jocelyn Ollier, Daiki Mori, Guillaume Voisinne, Javier Celis-Gutierrez, Claude Gregoire, Jeanne Perroteau, Régine Vivien, Mylène Camus, Odile Burlet-Schiltz, Anne Gonzalez de Peredo, Béatrice Clémenceau, Romain Roncagalli, Henri Vié, and Bernard Malissen. Systems-level conservation of the proximal tcr signaling network of mice and humans. The Journal of Experimental Medicine, Jan 2022. URL: https://doi.org/10.1084/jem.20211295, doi:10.1084/jem.20211295. This article has 15 citations.

13. (horejsi2004transmembraneadaptorproteins pages 12-13): Václav Hořejší, Weiguo Zhang, and Burkhart Schraven. Transmembrane adaptor proteins: organizers of immunoreceptor signalling. Nature Reviews Immunology, 4:603-616, Aug 2004. URL: https://doi.org/10.1038/nri1414, doi:10.1038/nri1414. This article has 305 citations and is from a highest quality peer-reviewed journal.

14. (horejsi2004transmembraneadaptorproteins pages 5-6): Václav Hořejší, Weiguo Zhang, and Burkhart Schraven. Transmembrane adaptor proteins: organizers of immunoreceptor signalling. Nature Reviews Immunology, 4:603-616, Aug 2004. URL: https://doi.org/10.1038/nri1414, doi:10.1038/nri1414. This article has 305 citations and is from a highest quality peer-reviewed journal.

15. (horejsi2004transmembraneadaptorproteins pages 4-5): Václav Hořejší, Weiguo Zhang, and Burkhart Schraven. Transmembrane adaptor proteins: organizers of immunoreceptor signalling. Nature Reviews Immunology, 4:603-616, Aug 2004. URL: https://doi.org/10.1038/nri1414, doi:10.1038/nri1414. This article has 305 citations and is from a highest quality peer-reviewed journal.

16. (curson2018ptrapstransmembraneadaptors pages 2-3): James E B Curson, Lin Luo, Matthew J Sweet, and Jennifer L Stow. Ptraps: transmembrane adaptors in innate immune signaling. Journal of Leukocyte Biology, 103:1011-1019, Mar 2018. URL: https://doi.org/10.1002/jlb.2ri1117-474r, doi:10.1002/jlb.2ri1117-474r. This article has 15 citations and is from a peer-reviewed journal.

17. (simeoni2004adaptorsandlinkers pages 5-6): Luca Simeoni, Stefanie Kliche, Jonathan Lindquist, and Burkhart Schraven. Adaptors and linkers in t and b cells. Current opinion in immunology, 16 3:304-13, Jun 2004. URL: https://doi.org/10.1016/j.coi.2004.03.001, doi:10.1016/j.coi.2004.03.001. This article has 87 citations and is from a peer-reviewed journal.

18. (stepanek2014palmitoylatedtransmembraneadaptor pages 2-3): Ondrej Stepanek, Peter Draber, and Vaclav Horejsi. Palmitoylated transmembrane adaptor proteins in leukocyte signaling. Cellular signalling, 26 5:895-902, May 2014. URL: https://doi.org/10.1016/j.cellsig.2014.01.007, doi:10.1016/j.cellsig.2014.01.007. This article has 52 citations and is from a peer-reviewed journal.

19. (narbonasanchez2023expressionofnont pages 1-2): Isaac Narbona-Sánchez, Alba Pérez-Linaza, Isabel Serrano-García, Inmaculada Vico-Barranco, Luis M. Fernández-Aguilar, José L. Poveda-Díaz, María J. Sánchez del Pino, Fermín Medina-Varo, Mikel M. Arbulo-Echevarria, and Enrique Aguado. Expression of non-t cell activation linker (ntal) in jurkat cells negatively regulates tcr signaling: potential role in rheumatoid arthritis. International Journal of Molecular Sciences, 24:4574, Feb 2023. URL: https://doi.org/10.3390/ijms24054574, doi:10.3390/ijms24054574. This article has 4 citations.

20. (narbonasanchez2023expressionofnont pages 8-10): Isaac Narbona-Sánchez, Alba Pérez-Linaza, Isabel Serrano-García, Inmaculada Vico-Barranco, Luis M. Fernández-Aguilar, José L. Poveda-Díaz, María J. Sánchez del Pino, Fermín Medina-Varo, Mikel M. Arbulo-Echevarria, and Enrique Aguado. Expression of non-t cell activation linker (ntal) in jurkat cells negatively regulates tcr signaling: potential role in rheumatoid arthritis. International Journal of Molecular Sciences, 24:4574, Feb 2023. URL: https://doi.org/10.3390/ijms24054574, doi:10.3390/ijms24054574. This article has 4 citations.

21. (horejsi2004transmembraneadaptorproteins pages 6-7): Václav Hořejší, Weiguo Zhang, and Burkhart Schraven. Transmembrane adaptor proteins: organizers of immunoreceptor signalling. Nature Reviews Immunology, 4:603-616, Aug 2004. URL: https://doi.org/10.1038/nri1414, doi:10.1038/nri1414. This article has 305 citations and is from a highest quality peer-reviewed journal.

22. (horejsi2004transmembraneadaptorproteins pages 11-12): Václav Hořejší, Weiguo Zhang, and Burkhart Schraven. Transmembrane adaptor proteins: organizers of immunoreceptor signalling. Nature Reviews Immunology, 4:603-616, Aug 2004. URL: https://doi.org/10.1038/nri1414, doi:10.1038/nri1414. This article has 305 citations and is from a highest quality peer-reviewed journal.

23. (horejsi2004transmembraneadaptorproteins pages 10-11): Václav Hořejší, Weiguo Zhang, and Burkhart Schraven. Transmembrane adaptor proteins: organizers of immunoreceptor signalling. Nature Reviews Immunology, 4:603-616, Aug 2004. URL: https://doi.org/10.1038/nri1414, doi:10.1038/nri1414. This article has 305 citations and is from a highest quality peer-reviewed journal.

24. (stepanek2014palmitoylatedtransmembraneadaptor pages 5-6): Ondrej Stepanek, Peter Draber, and Vaclav Horejsi. Palmitoylated transmembrane adaptor proteins in leukocyte signaling. Cellular signalling, 26 5:895-902, May 2014. URL: https://doi.org/10.1016/j.cellsig.2014.01.007, doi:10.1016/j.cellsig.2014.01.007. This article has 52 citations and is from a peer-reviewed journal.

25. (horejsi2004transmembraneadaptorproteins pages 7-8): Václav Hořejší, Weiguo Zhang, and Burkhart Schraven. Transmembrane adaptor proteins: organizers of immunoreceptor signalling. Nature Reviews Immunology, 4:603-616, Aug 2004. URL: https://doi.org/10.1038/nri1414, doi:10.1038/nri1414. This article has 305 citations and is from a highest quality peer-reviewed journal.

26. (borowicz2020adaptorproteinsflexible pages 14-17): Paweł Borowicz, Hanna Chan, Anette Hauge, and Anne Spurkland. Adaptor proteins: flexible and dynamic modulators of immune cell signalling. Scandinavian Journal of Immunology, Oct 2020. URL: https://doi.org/10.1111/sji.12951, doi:10.1111/sji.12951. This article has 39 citations and is from a peer-reviewed journal.

27. (rubin2024latencodest pages 16-18): Adam J. Rubin, Tyler T. Dao, Amelia V. Schueppert, Aviv Regev, and Alex K. Shalek. Lat encodes t cell activation pathway balance. bioRxiv, Aug 2024. URL: https://doi.org/10.1101/2024.08.26.609683, doi:10.1101/2024.08.26.609683. This article has 3 citations.

28. (yamane2025weakslp76plcγ1interaction pages 1-5): Hidehiro Yamane, Junya Wada, Elizabeth N. Stassenko, Natalie D. Convertino, Mariah E. Lee, Melanie S. Vacchio, Wenmei Li, Udumbara M. Rathnayake, Lakshmi Balagopalan, Raj Chari, Herbert Hagenau, Parirokh Awasthi, Dorian B. McGavern, Remy Bosselut, and Lawrence E. Samelson. Weak slp-76-plc-γ1 interaction in the lat-nucleated multi-protein complex fine-tunes tcr signal strength to optimize t cell responsiveness. BioRxiv, Sep 2025. URL: https://doi.org/10.1101/2025.09.11.675682, doi:10.1101/2025.09.11.675682. This article has 0 citations.

29. (yamane2025weakslp76plcγ1interaction pages 13-17): Hidehiro Yamane, Junya Wada, Elizabeth N. Stassenko, Natalie D. Convertino, Mariah E. Lee, Melanie S. Vacchio, Wenmei Li, Udumbara M. Rathnayake, Lakshmi Balagopalan, Raj Chari, Herbert Hagenau, Parirokh Awasthi, Dorian B. McGavern, Remy Bosselut, and Lawrence E. Samelson. Weak slp-76-plc-γ1 interaction in the lat-nucleated multi-protein complex fine-tunes tcr signal strength to optimize t cell responsiveness. BioRxiv, Sep 2025. URL: https://doi.org/10.1101/2025.09.11.675682, doi:10.1101/2025.09.11.675682. This article has 0 citations.

30. (yamane2025weakslp76plcγ1interaction pages 61-63): Hidehiro Yamane, Junya Wada, Elizabeth N. Stassenko, Natalie D. Convertino, Mariah E. Lee, Melanie S. Vacchio, Wenmei Li, Udumbara M. Rathnayake, Lakshmi Balagopalan, Raj Chari, Herbert Hagenau, Parirokh Awasthi, Dorian B. McGavern, Remy Bosselut, and Lawrence E. Samelson. Weak slp-76-plc-γ1 interaction in the lat-nucleated multi-protein complex fine-tunes tcr signal strength to optimize t cell responsiveness. BioRxiv, Sep 2025. URL: https://doi.org/10.1101/2025.09.11.675682, doi:10.1101/2025.09.11.675682. This article has 0 citations.

31. (yamane2025weakslp76plcγ1interaction pages 52-54): Hidehiro Yamane, Junya Wada, Elizabeth N. Stassenko, Natalie D. Convertino, Mariah E. Lee, Melanie S. Vacchio, Wenmei Li, Udumbara M. Rathnayake, Lakshmi Balagopalan, Raj Chari, Herbert Hagenau, Parirokh Awasthi, Dorian B. McGavern, Remy Bosselut, and Lawrence E. Samelson. Weak slp-76-plc-γ1 interaction in the lat-nucleated multi-protein complex fine-tunes tcr signal strength to optimize t cell responsiveness. BioRxiv, Sep 2025. URL: https://doi.org/10.1101/2025.09.11.675682, doi:10.1101/2025.09.11.675682. This article has 0 citations.

32. (nicolas2022systemslevelconservationof pages 10-11): Philippe Nicolas, Jocelyn Ollier, Daiki Mori, Guillaume Voisinne, Javier Celis-Gutierrez, Claude Gregoire, Jeanne Perroteau, Régine Vivien, Mylène Camus, Odile Burlet-Schiltz, Anne Gonzalez de Peredo, Béatrice Clémenceau, Romain Roncagalli, Henri Vié, and Bernard Malissen. Systems-level conservation of the proximal tcr signaling network of mice and humans. The Journal of Experimental Medicine, Jan 2022. URL: https://doi.org/10.1084/jem.20211295, doi:10.1084/jem.20211295. This article has 15 citations.

33. (nicolas2022systemslevelconservationof pages 9-10): Philippe Nicolas, Jocelyn Ollier, Daiki Mori, Guillaume Voisinne, Javier Celis-Gutierrez, Claude Gregoire, Jeanne Perroteau, Régine Vivien, Mylène Camus, Odile Burlet-Schiltz, Anne Gonzalez de Peredo, Béatrice Clémenceau, Romain Roncagalli, Henri Vié, and Bernard Malissen. Systems-level conservation of the proximal tcr signaling network of mice and humans. The Journal of Experimental Medicine, Jan 2022. URL: https://doi.org/10.1084/jem.20211295, doi:10.1084/jem.20211295. This article has 15 citations.

## Artifacts

- [Edison artifact artifact-00](PTHR14098-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR14098-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. horejsi2004transmembraneadaptorproteins pages 10-11
2. horejsi2004transmembraneadaptorproteins pages 12-13
3. horejsi2004transmembraneadaptorproteins pages 7-8
4. horejsi2004transmembraneadaptorproteins pages 6-7
5. horejsi2004transmembraneadaptorproteins pages 11-12
6. rudd1999adaptorsandmolecular pages 2-3
7. horejsi2004transmembraneadaptorproteins pages 1-2
8. borowicz2020adaptorproteinsflexible pages 6-9
9. rudd1999adaptorsandmolecular pages 1-2
10. simeoni2004adaptorsandlinkers pages 4-5
11. borowicz2020adaptorproteinsflexible pages 9-12
12. borowicz2020adaptorproteinsflexible pages 12-14
13. fernandezaguilar2023astoryof pages 9-11
14. rubin2024latencodest pages 9-11
15. rubin2024latencodest pages 9-9
16. samelson2002signaltransductionmediated pages 13-15
17. nicolas2022systemslevelconservationof pages 13-13
18. horejsi2004transmembraneadaptorproteins pages 5-6
19. horejsi2004transmembraneadaptorproteins pages 4-5
20. curson2018ptrapstransmembraneadaptors pages 2-3
21. simeoni2004adaptorsandlinkers pages 5-6
22. stepanek2014palmitoylatedtransmembraneadaptor pages 2-3
23. narbonasanchez2023expressionofnont pages 1-2
24. narbonasanchez2023expressionofnont pages 8-10
25. stepanek2014palmitoylatedtransmembraneadaptor pages 5-6
26. borowicz2020adaptorproteinsflexible pages 14-17
27. rubin2024latencodest pages 16-18
28. nicolas2022systemslevelconservationof pages 10-11
29. nicolas2022systemslevelconservationof pages 9-10
30. https://doi.org/10.1016/s0092-8674(00
31. https://doi.org/10.1111/sji.12951,
32. https://doi.org/10.1038/nri1414,
33. https://doi.org/10.1016/j.coi.2004.03.001,
34. https://doi.org/10.3390/biology12091163,
35. https://doi.org/10.1101/2024.08.26.609683,
36. https://doi.org/10.1146/annurev.immunol.20.092601.111357,
37. https://doi.org/10.1084/jem.20211295,
38. https://doi.org/10.1002/jlb.2ri1117-474r,
39. https://doi.org/10.1016/j.cellsig.2014.01.007,
40. https://doi.org/10.3390/ijms24054574,
41. https://doi.org/10.1101/2025.09.11.675682,