---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-28T20:54:34.751278'
end_time: '2026-06-28T21:16:39.840536'
duration_seconds: 1325.09
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR23037
  interpro_name: Type I Cytokine Receptor
  interpro_short_name: Type_I_Cytokine_Rcpt
  interpro_type: family
  interpro_integrated: None (top-level entry)
  member_databases: Not specified
  n_proteins: '19493'
  n_taxa: '2954'
  n_subfamilies: '20'
  interpro2go_terms: None mapped (no InterPro2GO terms for this entry)
  interpro_description: The Type I Cytokine Receptor family includes receptors for
    various interleukins, growth hormone, erythropoietin, and thrombopoietin, among
    others. These receptors are characterized by the presence of conserved motifs
    such as the WSXWS motif, necessary for proper folding and transport, and the box
    1 motif, essential for JAK interaction and activation. Family members play crucial
    roles in immune response, hematopoiesis, and growth regulation. They mediate signaling
    pathways like JAK-STAT, influencing cell proliferation, differentiation, and survival.
    Some receptors also have soluble forms that modulate signaling by acting as inhibitors
    or reservoirs. The family is involved in Th2 differentiation, IgE production,
    allergic inflammation responses, and the regulation of postnatal body growth.
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 33
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PTHR23037-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR23037-deep-research-falcon_artifacts/artifact-01.md
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
- **Accession:** PTHR23037
- **Name:** Type I Cytokine Receptor
- **Short name:** Type_I_Cytokine_Rcpt
- **Entry type:** family
- **Integrated into / parent:** None (top-level entry)
- **Member database signatures:** Not specified
- **Scale:** 19493 proteins across 2954 taxa, 20 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** The Type I Cytokine Receptor family includes receptors for various interleukins, growth hormone, erythropoietin, and thrombopoietin, among others. These receptors are characterized by the presence of conserved motifs such as the WSXWS motif, necessary for proper folding and transport, and the box 1 motif, essential for JAK interaction and activation. Family members play crucial roles in immune response, hematopoiesis, and growth regulation. They mediate signaling pathways like JAK-STAT, influencing cell proliferation, differentiation, and survival. Some receptors also have soluble forms that modulate signaling by acting as inhibitors or reservoirs. The family is involved in Th2 differentiation, IgE production, allergic inflammation responses, and the regulation of postnatal body growth.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR23037 (Type I Cytokine Receptor)**, structured to support GO annotation review.

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
- **Accession:** PTHR23037
- **Name:** Type I Cytokine Receptor
- **Short name:** Type_I_Cytokine_Rcpt
- **Entry type:** family
- **Integrated into / parent:** None (top-level entry)
- **Member database signatures:** Not specified
- **Scale:** 19493 proteins across 2954 taxa, 20 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** The Type I Cytokine Receptor family includes receptors for various interleukins, growth hormone, erythropoietin, and thrombopoietin, among others. These receptors are characterized by the presence of conserved motifs such as the WSXWS motif, necessary for proper folding and transport, and the box 1 motif, essential for JAK interaction and activation. Family members play crucial roles in immune response, hematopoiesis, and growth regulation. They mediate signaling pathways like JAK-STAT, influencing cell proliferation, differentiation, and survival. Some receptors also have soluble forms that modulate signaling by acting as inhibitors or reservoirs. The family is involved in Th2 differentiation, IgE production, allergic inflammation responses, and the regulation of postnatal body growth.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR23037 (Type I Cytokine Receptor)**, structured to support GO annotation review.

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


# Comprehensive Research Report: PTHR23037 (Type I Cytokine Receptor) — InterPro Family for GO Annotation Review

## 1. Family Definition and Biochemistry

### 1.1 Structural Architecture

The Type I Cytokine Receptor family (also designated Class I cytokine receptors or hematopoietin receptors) represents the largest cytokine receptor family, comprising over 30 human members (lv2024thejakstatpathway pages 6-8). PTHR23037, as defined in InterPro, encompasses 19,493 proteins across 2,954 taxa with 20 recognized subfamilies.

The defining structural feature of the family is the **cytokine-binding homology region (CHR)**, a ~200-residue extracellular module consisting of two consecutive fibronectin type-III (FnIII) domains (~100 residues each), arranged in a β-sandwich structure with three- and four-stranded β-sheets (lv2024thejakstatpathway pages 6-8, wang2009structuralbiologyof pages 2-4). The original structural analysis by Bazan (1990) established that the individual receptor domains adopt an antiparallel β-sandwich topology similar to immunoglobulin constant domains, creating a "double-barrel" receptor design from domains distantly related to fibronectin type III structures (bazan1990structuraldesignand pages 1-2, bazan1990structuraldesignand pages 2-3).

### 1.2 Conserved Motifs

**WSXWS motif:** Located in the C-terminal FnIII domain of the CHR module, the Trp-Ser-X-Trp-Ser (WSXWS) motif is the hallmark signature of Class I cytokine receptors. It forms a "ladder" structure through cation-π interactions between tryptophan and arginine side chains (metcalfe2020structuralunderstandingof pages 1-2). The motif is critical for maintaining tertiary structure rather than directly participating in cytokine binding (lv2024thejakstatpathway pages 6-8); mutations render receptors non-functional (metcalfe2020structuralunderstandingof pages 2-4, metcalfe2020structuralunderstandingof pages 1-2). The WSxWS box lies on a loop between C-domain strands F' and G' and forms the floor of the ligand-binding crevice (bazan1990structuraldesignand pages 3-4).

**Conserved cysteines:** The N-terminal FnIII domain of the CHR contains four conserved cysteine residues forming interstrand disulfide bonds essential for structural integrity (wang2009structuralbiologyof pages 2-4, lv2024thejakstatpathway pages 6-8).

**Box1 and Box2 motifs:** In the intracellular domain, two conserved sequence motifs mediate JAK kinase recruitment. Box1 is a proline-rich motif positioned approximately 10 residues from the transmembrane domain, binding the F2 subdomain of JAK FERM domains. Box2 is a hydrophobic-rich motif located 10–50 residues downstream of Box1, interacting with the JAK SH2 domain (morris2018themoleculardetails pages 11-14, morris2018themoleculardetails pages 14-17, lv2024thejakstatpathway pages 11-12). Together, these motifs form an elongated epitope spanning approximately 85 Ångströms with extensive interactions burying over 1,000 Å² (lv2024thejakstatpathway pages 12-15). Membrane proximity is essential for JAK activation; relocating these motifs away from the membrane abolishes JAK binding (morris2018themoleculardetails pages 14-17).

**Disordered intracellular domains (ICDs):** Class 1 cytokine receptor ICDs are fully intrinsically disordered and rich in short linear motifs (SLiMs) that orchestrate complex signaling, including STAT-binding motifs located toward the C-terminus (seiffert2020orchestrationofsignaling pages 1-2). Despite lacking intrinsic kinase activity, these disordered ICDs constitute crucial scaffolds for JAK-STAT signal transduction (morris2018themoleculardetails pages 11-14, seiffert2020orchestrationofsignaling pages 1-2). Recent evidence also suggests that some ICD regions contain structured lipid interaction domains that stabilize JAK-receptor complexes at the membrane (meyer2024functionalcouplingof pages 85-88).

### 1.3 Cytokine Binding and Activation Mechanism

Cytokine binding occurs at the junction between the two FnIII domains of the CHR, with flexible variable loops from each domain contributing to binding specificity (lv2024thejakstatpathway pages 6-8). Helical cytokines dock into a V-shaped crevice formed between the linked FnIII domains (bazan1990structuraldesignand pages 3-4). Signaling is initiated when cytokine binding induces receptor dimerization or conformational changes in preformed dimers, bringing associated JAK kinases into proximity for trans-phosphorylation (morris2018themoleculardetails pages 11-14, morris2018themoleculardetails pages 14-17).

## 2. InterPro2GO Mapping Appropriateness

### 2.1 Current State

**PTHR23037 currently has no InterPro2GO terms mapped.** This is a notable and, as this analysis demonstrates, largely appropriate absence.

### 2.2 Assessment of Candidate GO Terms

The following table evaluates candidate GO terms that might be considered for this family-level entry, assessing their appropriateness for every member the signature matches:

| Candidate GO Term | GO ID (approximate) | Aspect (MF/BP/CC) | True for all members? | Problem if applied broadly | Recommendation |
|---|---|---|---|---|---|
| cytokine receptor activity | GO:0004896 | MF | No | Over-annotates non-signaling members: several family members are non-signaling alpha chains with short cytoplasmic tails, and soluble members such as CRLF1 are not membrane signaling receptors (crisponi2022crlf1andclcf1 pages 4-6, morris2018themoleculardetails pages 11-14, morris2018themoleculardetails pages 8-11) | KEEP_AS_NON_CORE or push to subfamilies |
| cytokine binding | GO:0019955 | MF | Mostly no at strict family-wide level | Over-annotates shared signaling chains because some shared chains do not bind cytokine independently and require partner receptor chains; binding specificity is subfamily/context dependent (wang2009structuralbiologyof pages 4-5, morris2018themoleculardetails pages 8-11) | Push to subfamilies |
| JAK-STAT cascade | GO:0007259 | BP | No | Over-annotates non-signaling members: alpha chains and soluble receptors do not themselves execute JAK-STAT signaling, even though many signaling-competent complexes do (crisponi2022crlf1andclcf1 pages 4-6, morris2018themoleculardetails pages 11-14, morris2018themoleculardetails pages 8-11) | Push to subfamilies |
| immune response | GO:0006955 | BP | No | Subfamily-specific; endocrine receptors such as GHR and PRLR are primarily involved in growth/reproduction rather than core immune functions (morris2018themoleculardetails pages 4-8, liongue2007evolutionofclass pages 1-2, lv2024thejakstatpathway pages 5-6) | Push to subfamilies |
| hematopoiesis | GO:0030097 | BP | No | Subfamily-specific; applies to receptors such as EPOR, TPOR, βc-family, and some gp130-family members, but not broadly across endocrine and other branches (morris2018themoleculardetails pages 4-8, lv2024thejakstatpathway pages 9-11, lv2024thejakstatpathway pages 5-6) | Push to subfamilies |
| plasma membrane | GO:0005886 | CC | No | Over-annotates soluble forms because family includes secreted/soluble receptor-like proteins such as CRLF1 and soluble receptor forms (crisponi2022crlf1andclcf1 pages 4-6, crisponi2022crlf1andclcf1 pages 2-4) | Push to subfamilies |
| extracellular region | GO:0005576 | CC | Partial only | Only true for soluble forms; most canonical family members are single-pass membrane proteins rather than exclusively extracellular proteins (lv2024thejakstatpathway pages 6-8, wang2009structuralbiologyof pages 2-4, crisponi2022crlf1andclcf1 pages 4-6) | Not appropriate at family level |
| cytokine-mediated signaling pathway | GO:0019221 | BP | No | Same problem as JAK-STAT-related process terms: over-annotates non-signaling alpha chains and soluble modulators, and masks strong functional divergence across immune, endocrine, and hematopoietic branches (morris2018themoleculardetails pages 4-8, crisponi2022crlf1andclcf1 pages 4-6, morris2018themoleculardetails pages 11-14, morris2018themoleculardetails pages 8-11) | Push to subfamilies |


*Table: This table evaluates candidate GO terms for the broad PTHR23037 Type I Cytokine Receptor family and shows why most terms are too broad for safe family-level annotation. It is useful for deciding which terms should remain absent from the top-level InterPro2GO mapping and instead be pushed to narrower subfamilies.*

**Key finding:** No single GO term from the Molecular Function, Biological Process, or Cellular Component ontologies can be safely applied to all proteins matched by this family signature. The family includes: (a) signaling-competent receptor chains with long ICDs and Box1/Box2 motifs; (b) non-signaling alpha chains with short cytoplasmic tails that function only in ligand capture and presentation (morris2018themoleculardetails pages 11-14, morris2018themoleculardetails pages 8-11); and (c) soluble receptor-like proteins such as CRLF1 that lack transmembrane domains and serve as extracellular modulators (crisponi2022crlf1andclcf1 pages 4-6, crisponi2022crlf1andclcf1 pages 2-4).

Even "cytokine receptor activity" (GO:0004896) — seemingly the most natural term — would over-annotate the non-signaling alpha chains (IL-2Rα, IL-15Rα, IL-6Rα, IL-11Rα, CNTFRα) that lack functional signaling capacity on their own (morris2018themoleculardetails pages 8-11), and soluble forms that modulate rather than transduce signals (crisponi2022crlf1andclcf1 pages 4-6).

## 3. Functional Divergence Across the Family

### 3.1 Major Subfamilies and Their Functions

The Type I cytokine receptor family exhibits extreme functional heterogeneity, with members spanning immune regulation, endocrine signaling, hematopoiesis, energy homeostasis, and neuronal survival (morris2018themoleculardetails pages 8-11, morris2018themoleculardetails pages 4-8, lv2024thejakstatpathway pages 5-6). The following table summarizes the major subfamilies:

| Subfamily | Shared chain | Representative members / receptors | Primary biological function | JAK association | Signaling status |
|---|---|---|---|---|---|
| gp130 / IL-6 family | gp130 (IL6ST) | IL-6Rα/gp130 complex, IL-11Rα/gp130, LIFR/gp130, OSMR/gp130, CNTFRα/LIFR/gp130, IL-27R-containing complexes | Hematopoiesis, acute-phase response, inflammation, cell survival/differentiation, neuronal and cardiovascular effects (morris2018themoleculardetails pages 8-11, wang2009structuralbiologyof pages 4-5, lv2024thejakstatpathway pages 9-11, lv2024thejakstatpathway pages 5-6) | Mainly JAK1, with JAK2 and TYK2 also used depending on chain/context (lv2024thejakstatpathway pages 9-11, metcalfe2020structuralunderstandingof pages 2-4, crisponi2022crlf1andclcf1 pages 2-4) | Mostly signaling-competent as full receptor complexes; cytokine-specific α chains are often non-signaling on their own and rely on gp130-family signaling chains (crisponi2022crlf1andclcf1 pages 2-4, morris2018themoleculardetails pages 8-11) |
| Common gamma chain / IL-2 family | γc (IL2RG) | IL-2R, IL-4R, IL-7R, IL-9R, IL-15R, IL-21R | Immune-cell proliferation, survival, differentiation, lymphocyte homeostasis, NK/T-cell biology (morris2018themoleculardetails pages 8-11, wang2009structuralbiologyof pages 1-2, lv2024thejakstatpathway pages 5-6) | JAK1 and JAK3 are the canonical pair for signaling complexes containing γc (morris2018themoleculardetails pages 8-11, lv2024thejakstatpathway pages 9-11) | Signaling-competent in β/γ or α/β/γ complexes; some α chains are ligand-binding/non-signaling accessories (morris2018themoleculardetails pages 8-11) |
| Common beta chain / IL-3 family | βc (CSF2RB) | IL-3R, IL-5R, GM-CSFR | Hematopoiesis, myeloid-cell development, inflammatory and immune responses (morris2018themoleculardetails pages 8-11, wang2009structuralbiologyof pages 1-2, lv2024thejakstatpathway pages 9-11, lv2024thejakstatpathway pages 5-6) | Predominantly JAK2 (metcalfe2020structuralunderstandingof pages 2-4) | Signaling-competent when α and βc chains assemble into the full receptor complex (morris2018themoleculardetails pages 8-11, wang2009structuralbiologyof pages 1-2) |
| Homodimeric receptors | None; two identical receptor chains | GHR, PRLR, EPOR, TPOR, LepR, G-CSFR | Endocrine growth control, lactation/reproduction, erythropoiesis, thrombopoiesis, energy homeostasis, granulopoiesis (morris2018themoleculardetails pages 4-8, liongue2007evolutionofclass pages 1-2, lv2024thejakstatpathway pages 5-6) | Commonly JAK2-associated (strongest evidence for EPOR/GHR/PRLR/TPOR and several related receptors) (metcalfe2020structuralunderstandingof pages 2-4, morris2018themoleculardetails pages 4-8) | Signaling-competent; typically activated as ligand-induced or preformed dimers (morris2018themoleculardetails pages 4-8) |
| IL-12 / IL-23 family | No single universal shared chain across the whole subgroup; IL12RB1 is shared between IL-12 and IL-23 receptor complexes | IL-12Rβ1/IL-12Rβ2, IL-12Rβ1/IL-23R | Th1 and Th17 differentiation, inflammatory host defense (morris2018themoleculardetails pages 8-11, lv2024thejakstatpathway pages 9-11, lv2024thejakstatpathway pages 5-6) | JAK2 and TYK2 (metcalfe2020structuralunderstandingof pages 2-4) | Signaling-competent heteromeric receptor complexes (morris2018themoleculardetails pages 8-11, lv2024thejakstatpathway pages 9-11) |
| Non-signaling alpha chains | Accessory α chains; no independent signaling chain | IL-2Rα, IL-15Rα, IL-6Rα, IL-11Rα, CNTFRα | Ligand capture, presentation, affinity enhancement, receptor assembly specificity (wang2009structuralbiologyof pages 4-5, morris2018themoleculardetails pages 8-11) | No direct JAK binding or only very short/non-functional cytoplasmic tails (morris2018themoleculardetails pages 11-14, morris2018themoleculardetails pages 8-11) | Non-signaling alone; require signaling partner chains such as gp130, γc, or other long-tailed receptor chains (morris2018themoleculardetails pages 11-14, morris2018themoleculardetails pages 8-11) |
| Soluble receptors / receptor-like modulators | None | CRLF1, sCNTFRα | Cytokine chaperoning, extracellular modulation, agonistic or antagonistic/decoy-like regulation depending on context (crisponi2022crlf1andclcf1 pages 4-6, crisponi2022crlf1andclcf1 pages 2-4) | No direct JAK binding (crisponi2022crlf1andclcf1 pages 4-6, crisponi2022crlf1andclcf1 pages 2-4) | Non-signaling as standalone soluble proteins; modulate signaling through membrane receptors (crisponi2022crlf1andclcf1 pages 4-6, crisponi2022crlf1andclcf1 pages 2-4) |


*Table: This table summarizes the major functional subfamilies encompassed by the broad Type I cytokine receptor family and highlights why family-wide GO annotation is difficult. It distinguishes signaling receptor complexes from accessory alpha chains and soluble receptor-like proteins that lack direct JAK signaling capacity.*

### 3.2 Key Points of Functional Divergence

**Immune vs. Endocrine receptors:** The family encompasses both immune-centric receptors (interleukin receptors, GM-CSF receptor) and purely endocrine receptors (growth hormone receptor, prolactin receptor). GHR regulates postnatal body growth, PRLR regulates lactation and reproduction, while the interleukin receptors regulate immune cell proliferation, differentiation, and inflammatory responses (morris2018themoleculardetails pages 4-8, liongue2007evolutionofclass pages 1-2, lv2024thejakstatpathway pages 5-6).

**Signaling vs. Non-signaling members:** Not all Type I cytokine receptor chains are signaling-competent. Many cytokine-specific alpha chains contain only short cytoplasmic regions with no known signaling function (morris2018themoleculardetails pages 11-14). The alpha receptors for IL-2 and IL-15 are described as non-signaling chains that consist of sushi domains rather than canonical CHR domains (morris2018themoleculardetails pages 8-11). Similarly, soluble receptors like CRLF1 function as cytokine chaperones (facilitating CLCF1 secretion) rather than as signal transducers (crisponi2022crlf1andclcf1 pages 4-6).

**Structural diversity in receptor architecture:** Homodimeric receptors (GHR, EPOR, PRLR) have the simplest architecture with a single CHR per chain, while gp130, leptin receptor, and G-CSF receptor are "tall receptors" with additional FnIII domains creating legs that position the cytokine-binding region up to 120 Å from the cell surface (morris2018themoleculardetails pages 4-8).

**Soluble forms as modulators:** Soluble cytokine receptors are generated through protease cleavage, differential splicing, or exosome release and can function as either agonistic or antagonistic decoy receptors (crisponi2022crlf1andclcf1 pages 2-4). These represent a functionally distinct category from membrane-bound signaling receptors.

### 3.3 Neo-functionalization and Divergent Signaling

Different subfamilies activate distinct JAK-STAT combinations, resulting in divergent transcriptional programs. The γc chain exclusively recruits JAK3, while gp130 primarily recruits JAK1. Different STAT proteins (STAT1/2, STAT3, STAT5) are activated depending on the receptor complex composition, determining cell fate outcomes ranging from proliferation to apoptosis (metcalfe2020structuralunderstandingof pages 2-4, morris2018themoleculardetails pages 8-11).

## 4. Taxonomic Scope

### 4.1 Evolutionary Distribution

Class I cytokine receptors have an ancient evolutionary origin in bilaterian animals. The archetypal CytoR-JAK-STAT signaling module exists in extant protostomes such as insects (e.g., *Drosophila* Domeless/Dome receptor) (liongue2016evolutionofcytokine pages 1-2, liongue2016evolutionofcytokine pages 2-3). A single Class I receptor has been identified in the mosquito *Anopheles gambiae*, indicating an archetypal receptor existed at least 974 MYA when protostomes and deuterostomes diverged (liongue2007evolutionofclass pages 9-11).

**Urochordates:** The sea squirt (*Ciona intestinalis*) possesses only two Class I receptors — one homologous to gp130 and one related to the divergent orphan receptor CLF-3 (liongue2007evolutionofclass pages 1-2).

**Vertebrates:** Major diversification occurred between 794 MYA and 476 MYA, resulting in eight different receptor topologies among 27 core receptor chains by the last common ancestor of teleosts and mammals (liongue2007evolutionofclass pages 9-11, liongue2007evolutionofclass pages 1-2). Zebrafish possess 36 Class I cytokine receptors representing all five structural groups found in mammals (liongue2007evolutionofclass pages 1-2). This expansion was driven by two rounds of whole-genome duplication during early vertebrate evolution (liongue2016evolutionofcytokine pages 4-5). In mammals, the diversified system includes approximately 50 cytokine receptor molecules serviced by four JAK proteins and seven STAT proteins (liongue2016evolutionofcytokine pages 2-3).

### 4.2 Implications for GO Annotation

The broad taxonomic scope (19,493 proteins across 2,954 taxa) introduces additional challenges for family-wide GO annotation. Process terms like "immune response" or "Th2 cell differentiation" are clearly vertebrate-specific innovations that would be inappropriate for invertebrate orthologs matching this signature. Even "JAK-STAT cascade" — while the core pathway is conserved from insects to mammals (liongue2016evolutionofcytokine pages 1-2) — is not applicable to all family members (non-signaling alpha chains, soluble forms). The functional assignments of specific cytokine receptor subfamilies diverged substantially during vertebrate evolution, with limited lineage-specific diversification afterward (liongue2007evolutionofclass pages 1-2).

## 5. Over-Annotation Verdict

### 5.1 Summary Assessment

**The current absence of InterPro2GO mappings for PTHR23037 is appropriate and should be maintained.** This verdict is based on the following considerations:

1. **Family is functionally heterogeneous:** PTHR23037 encompasses receptors involved in immune regulation, endocrine signaling, hematopoiesis, energy homeostasis, neuronal survival, and cardiovascular function (lv2024thejakstatpathway pages 9-11, lv2024thejakstatpathway pages 5-6). No single biological process GO term applies universally.

2. **Family contains non-signaling members:** Alpha chains (IL-2Rα, IL-15Rα, IL-6Rα, IL-11Rα, CNTFRα) and soluble receptor-like proteins (CRLF1, sCNTFRα) lack functional signaling capacity, making even "cytokine receptor activity" over-broad for the complete family (morris2018themoleculardetails pages 11-14, morris2018themoleculardetails pages 8-11, crisponi2022crlf1andclcf1 pages 4-6).

3. **Taxonomic breadth introduces leakage:** With 2,954 taxa spanning invertebrates to mammals, vertebrate-specific processes (e.g., immune response, Th2 differentiation, IgE production) would inappropriately annotate invertebrate homologs (liongue2007evolutionofclass pages 9-11, liongue2016evolutionofcytokine pages 1-2).

4. **20 subfamilies reflect genuine functional partitioning:** The family's 20 subfamilies represent the appropriate level for GO annotation, as functional homogeneity exists primarily within these narrower groupings rather than across the entire family.

### 5.2 Recommended GO Action Pattern

| Scope | Recommendation | Rationale |
|-------|----------------|-----------|
| **PTHR23037 (family level)** | **ACCEPT current state (no mappings)** | Family too heterogeneous for any universal GO term; current absence of InterPro2GO terms is correct |
| **Subfamilies (20 children)** | **MODIFY-to-specific** | GO terms should be applied at the subfamily level where functional homogeneity allows confident annotation (e.g., EPOR subfamily → "erythropoietin receptor activity"; gp130 subfamily → "cytokine-mediated signaling pathway") |
| **If terms are ever proposed at family level** | **MARK_AS_OVER_ANNOTATED** | Any process or function term at this level would systematically over-annotate significant subsets of the 19,493 matched proteins |

### 5.3 Recommendations for InterPro

- The PTHR23037 entry should remain a top-level organizing family without GO terms.
- GO annotations should be pushed to the 20 subfamilies, where terms can be tailored to specific receptor functions (immune, endocrine, hematopoietic, etc.).
- If structural or molecular function annotations are desired at the family level, only extremely generic terms might be considered (e.g., "protein binding" GO:0005515), but these carry little informational value and are generally discouraged in InterPro2GO practice.
- Special attention should be given to non-signaling alpha chain subfamilies and soluble receptor-like members, which require distinct GO annotation profiles from the signaling-competent receptor chains.

References

1. (lv2024thejakstatpathway pages 6-8): You Lv, Jianxun Qi, Jeff J. Babon, Longxing Cao, Guohuang Fan, Jiajia Lang, Jin Zhang, Pengbing Mi, B. Kobe, and Faming Wang. The jak-stat pathway: from structural biology to cytokine engineering. Signal Transduction and Targeted Therapy, Aug 2024. URL: https://doi.org/10.1038/s41392-024-01934-w, doi:10.1038/s41392-024-01934-w. This article has 137 citations and is from a peer-reviewed journal.

2. (wang2009structuralbiologyof pages 2-4): Xinquan Wang, Patrick Lupardus, Sherry L. LaPorte, and K. Christopher Garcia. Structural biology of shared cytokine receptors. Apr 2009. URL: https://doi.org/10.1146/annurev.immunol.24.021605.090616, doi:10.1146/annurev.immunol.24.021605.090616. This article has 539 citations and is from a highest quality peer-reviewed journal.

3. (bazan1990structuraldesignand pages 1-2): J F Bazan. Structural design and molecular evolution of a cytokine receptor superfamily. Proceedings of the National Academy of Sciences of the United States of America, 87:6934-6938, Sep 1990. URL: https://doi.org/10.1073/pnas.87.18.6934, doi:10.1073/pnas.87.18.6934. This article has 3087 citations and is from a highest quality peer-reviewed journal.

4. (bazan1990structuraldesignand pages 2-3): J F Bazan. Structural design and molecular evolution of a cytokine receptor superfamily. Proceedings of the National Academy of Sciences of the United States of America, 87:6934-6938, Sep 1990. URL: https://doi.org/10.1073/pnas.87.18.6934, doi:10.1073/pnas.87.18.6934. This article has 3087 citations and is from a highest quality peer-reviewed journal.

5. (metcalfe2020structuralunderstandingof pages 1-2): Riley D. Metcalfe, Tracy L. Putoczki, and Michael D. W. Griffin. Structural understanding of interleukin 6 family cytokine signaling and targeted therapies: focus on interleukin 11. Frontiers in Immunology, Jul 2020. URL: https://doi.org/10.3389/fimmu.2020.01424, doi:10.3389/fimmu.2020.01424. This article has 140 citations and is from a peer-reviewed journal.

6. (metcalfe2020structuralunderstandingof pages 2-4): Riley D. Metcalfe, Tracy L. Putoczki, and Michael D. W. Griffin. Structural understanding of interleukin 6 family cytokine signaling and targeted therapies: focus on interleukin 11. Frontiers in Immunology, Jul 2020. URL: https://doi.org/10.3389/fimmu.2020.01424, doi:10.3389/fimmu.2020.01424. This article has 140 citations and is from a peer-reviewed journal.

7. (bazan1990structuraldesignand pages 3-4): J F Bazan. Structural design and molecular evolution of a cytokine receptor superfamily. Proceedings of the National Academy of Sciences of the United States of America, 87:6934-6938, Sep 1990. URL: https://doi.org/10.1073/pnas.87.18.6934, doi:10.1073/pnas.87.18.6934. This article has 3087 citations and is from a highest quality peer-reviewed journal.

8. (morris2018themoleculardetails pages 11-14): Rhiannon Morris, Nadia J. Kershaw, and Jeffrey J. Babon. The molecular details of cytokine signaling via the jak/stat pathway. Protein Science, 27:1984-2009, Nov 2018. URL: https://doi.org/10.1002/pro.3519, doi:10.1002/pro.3519. This article has 1112 citations and is from a peer-reviewed journal.

9. (morris2018themoleculardetails pages 14-17): Rhiannon Morris, Nadia J. Kershaw, and Jeffrey J. Babon. The molecular details of cytokine signaling via the jak/stat pathway. Protein Science, 27:1984-2009, Nov 2018. URL: https://doi.org/10.1002/pro.3519, doi:10.1002/pro.3519. This article has 1112 citations and is from a peer-reviewed journal.

10. (lv2024thejakstatpathway pages 11-12): You Lv, Jianxun Qi, Jeff J. Babon, Longxing Cao, Guohuang Fan, Jiajia Lang, Jin Zhang, Pengbing Mi, B. Kobe, and Faming Wang. The jak-stat pathway: from structural biology to cytokine engineering. Signal Transduction and Targeted Therapy, Aug 2024. URL: https://doi.org/10.1038/s41392-024-01934-w, doi:10.1038/s41392-024-01934-w. This article has 137 citations and is from a peer-reviewed journal.

11. (lv2024thejakstatpathway pages 12-15): You Lv, Jianxun Qi, Jeff J. Babon, Longxing Cao, Guohuang Fan, Jiajia Lang, Jin Zhang, Pengbing Mi, B. Kobe, and Faming Wang. The jak-stat pathway: from structural biology to cytokine engineering. Signal Transduction and Targeted Therapy, Aug 2024. URL: https://doi.org/10.1038/s41392-024-01934-w, doi:10.1038/s41392-024-01934-w. This article has 137 citations and is from a peer-reviewed journal.

12. (seiffert2020orchestrationofsignaling pages 1-2): Pernille Seiffert, Katrine Bugge, Mads Nygaard, Gitte W. Haxholm, Jacob H. Martinsen, Martin N. Pedersen, Lise Arleth, Wouter Boomsma, and Birthe B. Kragelund. Orchestration of signaling by structural disorder in class 1 cytokine receptors. Cell Communication and Signaling, Aug 2020. URL: https://doi.org/10.1186/s12964-020-00626-6, doi:10.1186/s12964-020-00626-6. This article has 28 citations and is from a peer-reviewed journal.

13. (meyer2024functionalcouplingof pages 85-88): Functional Coupling of Janus Kinases with Cytokine Receptors at the Plasma Membrane This article has 0 citations.

14. (crisponi2022crlf1andclcf1 pages 4-6): Laura Crisponi, Insa Buers, and Frank Rutsch. Crlf1 and clcf1 in development, health and disease. International Journal of Molecular Sciences, 23:992, Jan 2022. URL: https://doi.org/10.3390/ijms23020992, doi:10.3390/ijms23020992. This article has 53 citations.

15. (morris2018themoleculardetails pages 8-11): Rhiannon Morris, Nadia J. Kershaw, and Jeffrey J. Babon. The molecular details of cytokine signaling via the jak/stat pathway. Protein Science, 27:1984-2009, Nov 2018. URL: https://doi.org/10.1002/pro.3519, doi:10.1002/pro.3519. This article has 1112 citations and is from a peer-reviewed journal.

16. (wang2009structuralbiologyof pages 4-5): Xinquan Wang, Patrick Lupardus, Sherry L. LaPorte, and K. Christopher Garcia. Structural biology of shared cytokine receptors. Apr 2009. URL: https://doi.org/10.1146/annurev.immunol.24.021605.090616, doi:10.1146/annurev.immunol.24.021605.090616. This article has 539 citations and is from a highest quality peer-reviewed journal.

17. (morris2018themoleculardetails pages 4-8): Rhiannon Morris, Nadia J. Kershaw, and Jeffrey J. Babon. The molecular details of cytokine signaling via the jak/stat pathway. Protein Science, 27:1984-2009, Nov 2018. URL: https://doi.org/10.1002/pro.3519, doi:10.1002/pro.3519. This article has 1112 citations and is from a peer-reviewed journal.

18. (liongue2007evolutionofclass pages 1-2): Clifford Liongue and Alister C Ward. Evolution of class i cytokine receptors. BMC Evolutionary Biology, 7:120-120, Jul 2007. URL: https://doi.org/10.1186/1471-2148-7-120, doi:10.1186/1471-2148-7-120. This article has 183 citations and is from a domain leading peer-reviewed journal.

19. (lv2024thejakstatpathway pages 5-6): You Lv, Jianxun Qi, Jeff J. Babon, Longxing Cao, Guohuang Fan, Jiajia Lang, Jin Zhang, Pengbing Mi, B. Kobe, and Faming Wang. The jak-stat pathway: from structural biology to cytokine engineering. Signal Transduction and Targeted Therapy, Aug 2024. URL: https://doi.org/10.1038/s41392-024-01934-w, doi:10.1038/s41392-024-01934-w. This article has 137 citations and is from a peer-reviewed journal.

20. (lv2024thejakstatpathway pages 9-11): You Lv, Jianxun Qi, Jeff J. Babon, Longxing Cao, Guohuang Fan, Jiajia Lang, Jin Zhang, Pengbing Mi, B. Kobe, and Faming Wang. The jak-stat pathway: from structural biology to cytokine engineering. Signal Transduction and Targeted Therapy, Aug 2024. URL: https://doi.org/10.1038/s41392-024-01934-w, doi:10.1038/s41392-024-01934-w. This article has 137 citations and is from a peer-reviewed journal.

21. (crisponi2022crlf1andclcf1 pages 2-4): Laura Crisponi, Insa Buers, and Frank Rutsch. Crlf1 and clcf1 in development, health and disease. International Journal of Molecular Sciences, 23:992, Jan 2022. URL: https://doi.org/10.3390/ijms23020992, doi:10.3390/ijms23020992. This article has 53 citations.

22. (wang2009structuralbiologyof pages 1-2): Xinquan Wang, Patrick Lupardus, Sherry L. LaPorte, and K. Christopher Garcia. Structural biology of shared cytokine receptors. Apr 2009. URL: https://doi.org/10.1146/annurev.immunol.24.021605.090616, doi:10.1146/annurev.immunol.24.021605.090616. This article has 539 citations and is from a highest quality peer-reviewed journal.

23. (liongue2016evolutionofcytokine pages 1-2): Clifford Liongue, Robert Sertori, and Alister C. Ward. Evolution of cytokine receptor signaling. The Journal of Immunology, 197:11-18, Jul 2016. URL: https://doi.org/10.4049/jimmunol.1600372, doi:10.4049/jimmunol.1600372. This article has 135 citations.

24. (liongue2016evolutionofcytokine pages 2-3): Clifford Liongue, Robert Sertori, and Alister C. Ward. Evolution of cytokine receptor signaling. The Journal of Immunology, 197:11-18, Jul 2016. URL: https://doi.org/10.4049/jimmunol.1600372, doi:10.4049/jimmunol.1600372. This article has 135 citations.

25. (liongue2007evolutionofclass pages 9-11): Clifford Liongue and Alister C Ward. Evolution of class i cytokine receptors. BMC Evolutionary Biology, 7:120-120, Jul 2007. URL: https://doi.org/10.1186/1471-2148-7-120, doi:10.1186/1471-2148-7-120. This article has 183 citations and is from a domain leading peer-reviewed journal.

26. (liongue2016evolutionofcytokine pages 4-5): Clifford Liongue, Robert Sertori, and Alister C. Ward. Evolution of cytokine receptor signaling. The Journal of Immunology, 197:11-18, Jul 2016. URL: https://doi.org/10.4049/jimmunol.1600372, doi:10.4049/jimmunol.1600372. This article has 135 citations.

## Artifacts

- [Edison artifact artifact-00](PTHR23037-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR23037-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. lv2024thejakstatpathway pages 6-8
2. metcalfe2020structuralunderstandingof pages 1-2
3. bazan1990structuraldesignand pages 3-4
4. lv2024thejakstatpathway pages 12-15
5. morris2018themoleculardetails pages 14-17
6. seiffert2020orchestrationofsignaling pages 1-2
7. meyer2024functionalcouplingof pages 85-88
8. morris2018themoleculardetails pages 8-11
9. metcalfe2020structuralunderstandingof pages 2-4
10. morris2018themoleculardetails pages 4-8
11. morris2018themoleculardetails pages 11-14
12. liongue2007evolutionofclass pages 9-11
13. liongue2007evolutionofclass pages 1-2
14. liongue2016evolutionofcytokine pages 4-5
15. liongue2016evolutionofcytokine pages 2-3
16. liongue2016evolutionofcytokine pages 1-2
17. wang2009structuralbiologyof pages 2-4
18. bazan1990structuraldesignand pages 1-2
19. bazan1990structuraldesignand pages 2-3
20. lv2024thejakstatpathway pages 11-12
21. wang2009structuralbiologyof pages 4-5
22. lv2024thejakstatpathway pages 5-6
23. lv2024thejakstatpathway pages 9-11
24. wang2009structuralbiologyof pages 1-2
25. https://doi.org/10.1038/s41392-024-01934-w,
26. https://doi.org/10.1146/annurev.immunol.24.021605.090616,
27. https://doi.org/10.1073/pnas.87.18.6934,
28. https://doi.org/10.3389/fimmu.2020.01424,
29. https://doi.org/10.1002/pro.3519,
30. https://doi.org/10.1186/s12964-020-00626-6,
31. https://doi.org/10.3390/ijms23020992,
32. https://doi.org/10.1186/1471-2148-7-120,
33. https://doi.org/10.4049/jimmunol.1600372,