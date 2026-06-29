---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-28T21:43:19.968608'
end_time: '2026-06-28T22:11:31.912134'
duration_seconds: 1691.94
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR46037
  interpro_name: PROTEIN ENHANCER OF SEVENLESS 2B
  interpro_short_name: Not specified
  interpro_type: family
  interpro_integrated: IPR043539
  member_databases: Not specified
  n_proteins: '7580'
  n_taxa: '4536'
  n_subfamilies: '6'
  interpro2go_terms: None mapped (no InterPro2GO terms for this entry)
  interpro_description: Not specified in InterPro
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
  path: PTHR46037-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR46037-deep-research-falcon_artifacts/artifact-01.md
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
- **Accession:** PTHR46037
- **Name:** PROTEIN ENHANCER OF SEVENLESS 2B
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** IPR043539
- **Member database signatures:** Not specified
- **Scale:** 7580 proteins across 4536 taxa, 6 subfamilies
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
**PTHR46037 (PROTEIN ENHANCER OF SEVENLESS 2B)**, structured to support GO annotation review.

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
- **Accession:** PTHR46037
- **Name:** PROTEIN ENHANCER OF SEVENLESS 2B
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** IPR043539
- **Member database signatures:** Not specified
- **Scale:** 7580 proteins across 4536 taxa, 6 subfamilies
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
**PTHR46037 (PROTEIN ENHANCER OF SEVENLESS 2B)**, structured to support GO annotation review.

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


# Comprehensive Research Report: PTHR46037 — PROTEIN ENHANCER OF SEVENLESS 2B

## InterPro Family Research for GO Annotation Review

---

## 1. Family Definition and Biochemistry

### 1.1 Historical Naming and Identification

The InterPro entry PTHR46037, named "PROTEIN ENHANCER OF SEVENLESS 2B," derives its name from *Drosophila* genetics. The designation E(sev)2B refers to an enhancer locus of the Sevenless receptor tyrosine kinase (RTK) pathway, identified through genetic screens for modifiers of Sevenless-mediated R7 photoreceptor cell fate specification in the developing *Drosophila* eye. The gene identified at the E(sev)2B locus is *drk* (downstream of receptor kinases), which encodes the *Drosophila* homolog of mammalian Growth Factor Receptor-Bound Protein 2 (GRB2) and *C. elegans* Sem-5 (yamamoto1994signalingmechanismsin pages 3-4).

### 1.2 Domain Architecture and Fold

All members of the GRB2/drk family share a conserved **SH3-SH2-SH3** modular domain architecture consisting of a central Src Homology 2 (SH2) domain flanked by two Src Homology 3 (SH3) domains (N-terminal and C-terminal) (malagrino2024grb2adynamic pages 2-3, wang2024theconfigurationof pages 1-2). Human GRB2 is a 25 kDa, 217-amino-acid non-enzymatic adaptor protein. The crystal structure has been solved at 3.1 Å resolution (PDB: 1GR1) (malagrino2024grb2adynamic pages 2-3). Key structural features include:

- **SH2 domain** (residues 60–152): A module composed of two alpha-helices flanking a central beta-sheet that recognizes phosphorylated tyrosine residues, particularly the consensus motif pYxNx on activated receptor tyrosine kinases (malagrino2024grb2adynamic pages 1-2, wang2024theconfigurationof pages 1-2).
- **N-terminal SH3 domain** (residues 156–215): A beta-sandwich module that binds proline-rich ligands (PxxP motifs) on downstream effectors, most notably Son of Sevenless (SOS) (wang2024theconfigurationof pages 2-4).
- **C-terminal SH3 domain** (residues 1–58): A second beta-sandwich module with distinct binding specificity from the N-terminal SH3 (wang2024theconfigurationof pages 15-17).

The protein can exist as a monomer (active signaling form) or homodimer (inactive form), with dimerization mediated by hydrogen bonds between SH2 Glu87 and c-SH3 Tyr160, and between c-SH3 Asn188 and Asn214 (wang2024theconfigurationof pages 5-7, wang2024theconfigurationof pages 7-9).

### 1.3 Mechanism of Action

GRB2/drk functions as a **non-enzymatic adaptor protein** that physically bridges activated receptor tyrosine kinases to downstream signaling effectors. The canonical mechanism involves:

1. The SH2 domain binding phosphorylated tyrosine residues (e.g., pY1068 or pY1086) on activated RTKs such as EGFR (wang2011dcblbindingto pages 4-6).
2. The N-terminal SH3 domain recruiting SOS (Son of Sevenless), a guanine nucleotide exchange factor, to the plasma membrane (wang2024theconfigurationof pages 2-4).
3. SOS then catalyzes the exchange of GDP for GTP on Ras, activating the Ras/MAPK/ERK signaling cascade that controls cell proliferation, differentiation, and survival (wang2024theconfigurationof pages 2-4, wang2024theconfigurationof pages 11-12).

In *Drosophila*, drk associates with the activated Sevenless receptor kinase through its SH2 domain and with the Sos protein through its SH3 domains, thereby coupling the Sevenless RTK to Ras activation during R7 photoreceptor induction (yamamoto1994signalingmechanismsin pages 4-5). GRB2/drk also plays dual roles in EGFR signaling—both positively (signal transduction via SOS/Ras) and negatively (promoting receptor internalization and degradation through cooperation with Cbl E3 ubiquitin ligases) (wang2011dcblbindingto pages 4-6, wang2011dcblbindingto pages 6-8, wang2011dcblbindingto pages 1-2).

The following table summarizes the key members of the GRB2/drk adaptor protein family encompassed by PTHR46037:

| Protein / ortholog | Typical size (aa) | Expression pattern | Domain architecture | Key binding partners / motifs | Knockout or loss-of-function phenotype | Primary signaling role | Evidence |
|---|---:|---|---|---|---|---|---|
| **GRB2** (vertebrates) | 217 aa | Ubiquitous | **SH3-SH2-SH3** adaptor; central SH2 binds phosphotyrosine motifs, flanking SH3 domains bind proline-rich motifs | RTKs such as EGFR and other phosphotyrosine-containing receptors/adaptors via SH2; **SOS1** and other proline-rich partners via SH3 | **Embryonic lethal** in mouse; strong developmental and T-cell signaling defects when absent | Canonical adaptor linking activated RTKs to **RAS/MAPK** signaling; also participates in receptor internalization and other signaling complexes | (bilal2015theroleof pages 46-51, malagrino2024grb2adynamic pages 2-3, wang2024theconfigurationof pages 1-2, bilal2015theroleof pages 33-37, malagrino2024grb2adynamic pages 1-2) |
| **GADS / GRAP2** (vertebrates) | 330 aa | Hematopoietic and neuroendocrine cell-restricted | **SH3-SH2-SH3** adaptor | Binds phosphorylated **LAT** and bridges to **SLP-76**-centered complexes; shares some ligand space with GRB2 family proteins | Knockout mice are **viable** with comparatively milder immune/thymic phenotypes than GRB2 deficiency | Specialized adaptor in **T-cell receptor / immune receptor signaling**, especially LAT-SLP76 signalosome assembly | (bilal2015theroleof pages 46-51, feller2006potentialdiseasetargets pages 18-18, ruminski2023mappingtheslp76 pages 6-7) |
| **GRAP** (vertebrates) | 217 aa | Hematopoietic; also reported in salivary glands and kidney tubules | **SH3-SH2-SH3** adaptor | Can bind phosphotyrosine sites and proline-rich ligands; overlaps partly with GRB2/GADS ligand usage | Knockout mice reported as **viable/healthy** with relatively subtle phenotypes; role remains less well defined | More restricted adaptor with partially overlapping but weaker/nonredundant roles in immune and growth-factor signaling | (bilal2015theroleof pages 46-51, bilal2015theroleof pages 33-37, ruminski2023mappingtheslp76 pages 6-7) |
| **drk / downstream of receptor kinases** (*Drosophila*; historical **E(sev)2B**) | ~one GRB2-like adaptor, size not specified in retrieved evidence | *Drosophila* developmental signaling contexts including eye development; also reported in Johnston's organ/hearing organ | **SH3-SH2-SH3** adaptor homologous to mammalian GRB2 and *C. elegans* Sem-5 | Activated **Sevenless/RTKs** via SH2; **Sos** via SH3; also interacts in EGFR pathway regulation | Loss of function disrupts **R7 photoreceptor specification**; additional defects in EGFR-dependent and sensory/hearing contexts | Core adaptor in **Sevenless / RTK-to-Ras signaling** during eye development; conserved RTK-Ras coupling factor | (yamamoto1994signalingmechanismsin pages 3-4, birge1996sh2andsh3‐containing pages 2-4, yamamoto1994signalingmechanismsin pages 4-5, wang2011dcblbindingto pages 4-6, wang2011dcblbindingto pages 6-8) |


*Table: This table summarizes major GRB2-family members and the Drosophila drk ortholog relevant to PTHR46037, highlighting conserved SH3-SH2-SH3 architecture alongside clear divergence in expression, partners, phenotypes, and signaling specialization.*

---

## 2. InterPro2GO Mapping Appropriateness

### 2.1 Current Status

**No InterPro2GO terms are currently mapped to PTHR46037.** This entry is integrated into the parent entry IPR043539. The InterPro system assigns GO terms to entries based on experimental evidence from characterized proteins and propagates them to all proteins matched by the entry (blum2021theinterproprotein pages 1-2).

### 2.2 Assessment of Candidate GO Terms

Given the well-characterized biochemistry of the GRB2/drk family, the absence of GO terms is notable. However, careful analysis reveals that this absence may be partially justified by the **functional divergence across the family's 6 subfamilies**. The following table evaluates candidate GO terms for their appropriateness:

| GO Term | GO Category (MF/BP/CC) | Appropriateness for all family members | Risk level | Recommendation | Notes |
|---|---|---|---|---|---|
| GO:0005515 protein binding | MF | Partial | Medium | REJECT | Broadly true for GRB2-family adaptors because they function through multiple protein-protein interactions via SH2/SH3 domains, but too generic to be informative and not ideal for InterPro2GO core mapping; better captured by more specific adaptor-related functions if supported. (giubellino2010grb2andother pages 91-93, malagrino2024grb2adynamic pages 1-2, feller2006potentialdiseasetargets pages 6-7) |
| GO:0005070 SH3/SH2 adaptor activity | MF | Yes | Low | ACCEPT | Best-supported conserved molecular function across the family: all canonical GRB2-family proteins share SH3-SH2-SH3 architecture and act as non-catalytic adaptors linking phosphotyrosine-containing partners to proline-rich ligands. This is the most family-defining term. (yamamoto1994signalingmechanismsin pages 3-4, malagrino2024grb2adynamic pages 2-3, sandouk2023sh2sh2mediateddomainswappeddimerization pages 10-14) |
| GO:0005068 transmembrane receptor protein tyrosine kinase adaptor activity | MF | Partial | Medium | MODIFY | Well supported for GRB2/drk and likely many family members that couple RTKs to SOS/Ras, but some paralogs such as GADS are more specialized for immune LAT/SLP-76 signaling rather than generic RTK coupling. Better placed on a child entry or restricted subfamily if available. (yamamoto1994signalingmechanismsin pages 3-4, bilal2015theroleof pages 33-37, ruminski2023mappingtheslp76 pages 6-7, malagrino2024grb2adynamic pages 2-3) |
| GO:0007165 signal transduction | BP | Partial | Medium | REJECT | Family members are clearly involved in signaling, but this term is extremely broad and adds little value. It also risks obscuring meaningful specialization among GRB2, GADS, and GRAP. (giubellino2010grb2andother pages 91-93, wang2024theconfigurationof pages 11-12, malagrino2024grb2adynamic pages 1-2) |
| GO:0007169 transmembrane receptor protein tyrosine kinase signaling pathway | BP | Partial | Medium | MODIFY | Appropriate for drk/GRB2-centered RTK signaling, especially Sevenless/EGFR-like contexts, but not equally specific for all members across all taxa because GADS has substantial specialization in antigen receptor/LAT signaling. Use on narrower descendant entries if possible. (yamamoto1994signalingmechanismsin pages 3-4, birge1996sh2andsh3‐containing pages 2-4, bilal2015theroleof pages 46-51, malagrino2024grb2adynamic pages 2-3) |
| GO:0046578 regulation of Ras protein signal transduction | BP | Partial | Medium | MODIFY | Strong for GRB2/drk proteins that recruit SOS and promote Ras activation, but less secure for all family members because GRAP is poorly characterized and GADS has partly divergent scaffolding roles. Safer on subfamilies centered on canonical Grb2/drk orthologs. (yamamoto1994signalingmechanismsin pages 3-4, wang2024theconfigurationof pages 2-4, bilal2015theroleof pages 33-37, bilal2015theroleof pages 164-168) |
| GO:0042501 serine phosphorylation of STAT protein | BP | No | High | REJECT | Not a core conserved process for the family and far too pathway-specific. No evidence from the reviewed family literature supports this as a universal property of PTHR46037 matches. (blum2021theinterproprotein pages 1-2) |
| GO:0045467 R7 cell fate commitment | BP | No | High | REJECT | This is Drosophila-specific developmental biology tied to Sevenless signaling in the eye and cannot be propagated to the full family spanning thousands of taxa. At most, it would apply to drk in a narrow lineage-specific context. (yamamoto1994signalingmechanismsin pages 3-4, birge1996sh2andsh3‐containing pages 2-4) |
| GO:0005829 cytosol | CC | Partial | Medium | REJECT | Many family members are cytosolic adaptors prior to receptor recruitment, but their function is dynamic and includes membrane-proximal signaling complexes; CC assignment at family level is not sufficiently specific and may not capture all states/contexts. (wang2024theconfigurationof pages 5-7, malagrino2024grb2adynamic pages 1-2, wang2024theconfigurationof pages 9-11) |


*Table: This table evaluates candidate GO terms that could be considered for InterPro2GO mapping of PTHR46037 and rates their suitability for all proteins in the family. It helps distinguish family-defining adaptor functions from overly broad, subfamily-specific, or lineage-specific terms that would risk over-annotation.*

### 2.3 Key Observations

The most defensible GO term for the entire family is **GO:0005070 (SH3/SH2 adaptor activity)**, which captures the core molecular function shared by all members: acting as a non-catalytic adaptor that bridges phosphotyrosine-containing proteins to proline-rich effectors via SH2 and SH3 domains (malagrino2024grb2adynamic pages 2-3, sandouk2023sh2sh2mediateddomainswappeddimerization pages 10-14). More specific process terms (e.g., Ras signaling, RTK signaling) are well-supported for the GRB2/drk subfamily but not universally applicable across all paralogs, particularly GADS and GRAP, which have specialized immune signaling roles (ruminski2023mappingtheslp76 pages 6-7).

---

## 3. Functional Divergence Across the Family

### 3.1 Vertebrate Paralogs: GRB2, GADS, and GRAP

The vertebrate GRB2 family consists of three paralogs that have undergone significant **neo-functionalization** despite retaining conserved domain architecture (bilal2015theroleof pages 46-51):

- **GRB2** (217 aa, ubiquitous expression): The canonical, essential adaptor protein. GRB2-null mice exhibit embryonic lethality, and conditional T cell-specific deletion causes severe developmental arrest and impaired negative selection. GRB2 is the primary mediator of RTK-to-Ras signaling and is overexpressed in multiple cancer types (bilal2015theroleof pages 33-37, bilal2015theroleof pages 46-51).

- **GADS/GRAP2** (330 aa, hematopoietic-restricted): Despite sharing ~50% overall sequence homology with GRB2, GADS has specialized for immune receptor signaling, particularly bridging LAT (Linker for Activation of T cells) to SLP-76 in the TCR signaling pathway. GADS-deficient mice are viable but show impaired positive and negative T cell selection (bilal2015theroleof pages 46-51). GADS also regulates mast cell activation via FcεRI signaling.

- **GRAP** (217 aa, hematopoietic/kidney/salivary gland expression): Shares ~60% overall homology with GRB2 but remains the least characterized family member. GRAP-deficient mice are viable and healthy with minimal phenotypes. Recent evidence shows that GRAP-deficient T cells display normal CD69 induction and IL-2 secretion, suggesting a more subtle or redundant role (bilal2015theroleof pages 33-37, ruminski2023mappingtheslp76 pages 6-7).

### 3.2 Competitive and Overlapping Signaling

Despite their functional specialization, all three vertebrate paralogs bind identical tyrosine residues on LAT (Y171 and Y191) and compete for the same binding sites, while also sharing overlapping SH3 domain ligand specificity (e.g., SOS1) (bilal2015theroleof pages 164-168). This suggests a model where different adaptors of the same structural type are expressed to **fine-tune signaling** from multiple receptor systems including TCR, costimulatory receptors, and cytokine receptors (bilal2015theroleof pages 164-168).

### 3.3 Invertebrate Orthologs

In *Drosophila*, a single drk gene fulfills the combined functions of the vertebrate paralogs, coupling Sevenless, EGFR, and other RTKs to Ras signaling (yamamoto1994signalingmechanismsin pages 3-4, birge1996sh2andsh3‐containing pages 2-4). Drk has also been shown to localize to synaptic terminals in Johnston's organ (the fly hearing organ), and its loss causes scolopidium abnormalities—a function not traditionally associated with RTK-Ras signaling (bilal2015theroleof pages 33-37). In *C. elegans*, the ortholog Sem-5 performs analogous adaptor functions in developmental signaling. Human GRB2 and *Drosophila* drk can functionally substitute for *C. elegans* Sem-5, demonstrating deep conservation of the core adaptor mechanism (sandouk2023sh2sh2mediateddomainswappeddimerization pages 10-14).

### 3.4 No Known Catalytically Dead or Pseudo-enzyme Members

Unlike some enzyme families, the GRB2/drk family members are inherently **non-enzymatic adaptors**, so the concept of "catalytically dead" members does not directly apply. All characterized family members retain functional SH2 and SH3 domains capable of mediating protein-protein interactions. No pseudo-adaptor members (i.e., proteins with degenerate SH2/SH3 domains that have lost binding capacity) have been reported in the literature.

---

## 4. Taxonomic Scope

### 4.1 Distribution

PTHR46037 matches 7,580 proteins across 4,536 taxa with 6 subfamilies. Based on the evolutionary biology of SH2 domains and phosphotyrosine signaling:

- **SH2 domain proteins** are ancient and found across all major eukaryotic divisions, including unicellular organisms (yeast has one SH2 protein, Spt6) (liu2012evolutionofsh2 pages 5-6, liu2011thesh2domain–containing pages 2-4).
- **The GRB2-type SH3-SH2-SH3 adaptor architecture** is a **metazoan innovation** that emerged early in eumetazoans, before the radiata-bilateria split, coinciding with the expansion of receptor tyrosine kinases (liu2011thesh2domain–containing pages 7-9).
- The choanoflagellate *Monosiga brevicollis* possesses 19 conserved SH2 families and a functional phosphotyrosine signaling network, but whether a true GRB2-type adaptor is present is not definitively established from the evidence reviewed (liu2012evolutionofsh2 pages 6-8).
- The complete phosphotyrosine signaling circuitry (SH2 domains, PTKs, PTPs) emerged approximately 900 million years ago at the premetazoan boundary, with the GRB2 family appearing among the first wave of metazoan SH2 innovations (liu2011thesh2domain–containing pages 1-2, liu2011thesh2domain–containing pages 7-9).

### 4.2 Implications for GO Term Propagation

The broad taxonomic distribution (4,536 taxa) means that any GO term assigned to PTHR46037 would be propagated across a wide range of animal lineages. Process-specific terms such as "R7 cell fate commitment" or "T cell receptor signaling pathway" would be clearly inappropriate, as these are lineage-specific biological processes (yamamoto1994signalingmechanismsin pages 3-4). The core adaptor function (SH3/SH2 adaptor activity) is the most taxonomically robust annotation, as all family members across all taxa share this fundamental domain architecture and binding mode.

---

## 5. Over-Annotation Verdict

### 5.1 Current State Assessment

The current status of PTHR46037 is that **no InterPro2GO terms are mapped**. This is a reasonable conservative position given the family's functional heterogeneity, but it may represent an **under-annotation** of a well-characterized protein family. The family entry type is **"family"** (not domain or superfamily), which means it identifies whole proteins and is more appropriate for whole-protein function terms than domain-level entries.

### 5.2 Verdict: **PARTIALLY UNDER-ANNOTATED**

The absence of any GO terms means that 7,580 proteins across 4,536 taxa receive no functional annotation from this InterPro entry. Given the strong evidence for conserved adaptor function, this represents a missed opportunity for information transfer. However, the functional divergence across the 6 subfamilies (GRB2 vs. GADS vs. GRAP and their invertebrate orthologs) justifies caution with specific process terms.

### 5.3 Recommended GO Action Pattern

| Action | Term | Rationale |
|--------|------|-----------|
| **ACCEPT** (recommended addition) | GO:0005070 — SH3/SH2 adaptor activity (MF) | Universally true for all family members; the defining molecular function of the family |
| **KEEP_AS_NON_CORE** | GO:0007169 — transmembrane RTK signaling pathway (BP) | True for the major subfamily (GRB2/drk orthologs) but not all paralogs (GADS primarily signals via immune receptors). Better assigned to subfamilies |
| **KEEP_AS_NON_CORE** | GO:0046578 — regulation of Ras protein signal transduction (BP) | True for GRB2/drk subfamily but not universally demonstrated for all family members |
| **MARK_AS_OVER_ANNOTATED** (if ever added) | GO:0045467 — R7 cell fate commitment | Drosophila-specific; would massively over-annotate |
| **MARK_AS_OVER_ANNOTATED** (if ever added) | GO:0042110 — T cell activation | Vertebrate immune-specific; only relevant for GADS/GRAP subfamily members |

### 5.4 Recommendations for InterPro

1. **Consider adding GO:0005070 (SH3/SH2 adaptor activity)** to PTHR46037 at the family level, as this is the defining molecular function shared by all members.
2. **Move process-specific GO terms to subfamily entries** if InterPro structure permits. The 6 subfamilies likely correspond to GRB2-proper, GADS, GRAP, and invertebrate orthologs, each with distinct process annotations.
3. **Do not assign broad terms** such as "protein binding" (GO:0005515) or "signal transduction" (GO:0007165) as these carry insufficient information and add noise.
4. **The Drosophila-derived name "PROTEIN ENHANCER OF SEVENLESS 2B"** could be misleading for non-*Drosophila* contexts; this is a naming issue rather than an annotation issue, but users should be aware that the family corresponds to the broadly conserved GRB2/Sem-5/drk family of SH3-SH2-SH3 signaling adaptors.

---

## Summary

PTHR46037 encompasses the GRB2/drk/Sem-5 family of non-enzymatic SH3-SH2-SH3 adaptor proteins that function as critical nodes linking activated receptor tyrosine kinases to downstream Ras/MAPK signaling cascades (malagrino2024grb2adynamic pages 2-3, wang2024theconfigurationof pages 2-4, sandouk2023sh2sh2mediateddomainswappeddimerization pages 10-14). Originally identified as the Enhancer of Sevenless 2B locus (*drk*) in *Drosophila* R7 photoreceptor development screens (yamamoto1994signalingmechanismsin pages 3-4), the family has undergone significant neo-functionalization in vertebrates, giving rise to three paralogs (GRB2, GADS, GRAP) with distinct expression patterns, binding partner specificities, and phenotypic consequences of loss (bilal2015theroleof pages 46-51, bilal2015theroleof pages 33-37, ruminski2023mappingtheslp76 pages 6-7). The current absence of InterPro2GO terms represents a conservative but defensible position; however, the addition of **GO:0005070 (SH3/SH2 adaptor activity)** is strongly recommended as a family-wide molecular function term, while more specific process terms should be reserved for subfamily-level annotation to avoid over-annotation across the 7,580 proteins matched by this signature (blum2021theinterproprotein pages 1-2).

References

1. (yamamoto1994signalingmechanismsin pages 3-4): Daisuke Yamamoto. Signaling mechanisms in induction of the r7 photoreceptor in the developing drosophila retina. BioEssays, 16:237-244, Apr 1994. URL: https://doi.org/10.1002/bies.950160406, doi:10.1002/bies.950160406. This article has 22 citations and is from a peer-reviewed journal.

2. (malagrino2024grb2adynamic pages 2-3): Francesca Malagrinò, Elena Puglisi, Livia Pagano, Carlo Travaglini-Allocatelli, and Angelo Toto. Grb2: a dynamic adaptor protein orchestrating cellular signaling in health and disease. Sep 2024. URL: https://doi.org/10.1016/j.bbrep.2024.101803, doi:10.1016/j.bbrep.2024.101803. This article has 23 citations and is from a peer-reviewed journal.

3. (wang2024theconfigurationof pages 1-2): Dingyi Wang, Guoxia Liu, Yuxin Meng, Hongjie Chen, Zu Ye, and Ji Jing. The configuration of grb2 in protein interaction and signal transduction. Biomolecules, 14:259, Feb 2024. URL: https://doi.org/10.3390/biom14030259, doi:10.3390/biom14030259. This article has 55 citations.

4. (malagrino2024grb2adynamic pages 1-2): Francesca Malagrinò, Elena Puglisi, Livia Pagano, Carlo Travaglini-Allocatelli, and Angelo Toto. Grb2: a dynamic adaptor protein orchestrating cellular signaling in health and disease. Sep 2024. URL: https://doi.org/10.1016/j.bbrep.2024.101803, doi:10.1016/j.bbrep.2024.101803. This article has 23 citations and is from a peer-reviewed journal.

5. (wang2024theconfigurationof pages 2-4): Dingyi Wang, Guoxia Liu, Yuxin Meng, Hongjie Chen, Zu Ye, and Ji Jing. The configuration of grb2 in protein interaction and signal transduction. Biomolecules, 14:259, Feb 2024. URL: https://doi.org/10.3390/biom14030259, doi:10.3390/biom14030259. This article has 55 citations.

6. (wang2024theconfigurationof pages 15-17): Dingyi Wang, Guoxia Liu, Yuxin Meng, Hongjie Chen, Zu Ye, and Ji Jing. The configuration of grb2 in protein interaction and signal transduction. Biomolecules, 14:259, Feb 2024. URL: https://doi.org/10.3390/biom14030259, doi:10.3390/biom14030259. This article has 55 citations.

7. (wang2024theconfigurationof pages 5-7): Dingyi Wang, Guoxia Liu, Yuxin Meng, Hongjie Chen, Zu Ye, and Ji Jing. The configuration of grb2 in protein interaction and signal transduction. Biomolecules, 14:259, Feb 2024. URL: https://doi.org/10.3390/biom14030259, doi:10.3390/biom14030259. This article has 55 citations.

8. (wang2024theconfigurationof pages 7-9): Dingyi Wang, Guoxia Liu, Yuxin Meng, Hongjie Chen, Zu Ye, and Ji Jing. The configuration of grb2 in protein interaction and signal transduction. Biomolecules, 14:259, Feb 2024. URL: https://doi.org/10.3390/biom14030259, doi:10.3390/biom14030259. This article has 55 citations.

9. (wang2011dcblbindingto pages 4-6): Pei-Yu Wang and Li-Mei Pai. D-cbl binding to drk leads to dose-dependent down-regulation of egfr signaling and increases receptor-ligand endocytosis. PLoS ONE, 6:e17097, Feb 2011. URL: https://doi.org/10.1371/journal.pone.0017097, doi:10.1371/journal.pone.0017097. This article has 14 citations and is from a peer-reviewed journal.

10. (wang2024theconfigurationof pages 11-12): Dingyi Wang, Guoxia Liu, Yuxin Meng, Hongjie Chen, Zu Ye, and Ji Jing. The configuration of grb2 in protein interaction and signal transduction. Biomolecules, 14:259, Feb 2024. URL: https://doi.org/10.3390/biom14030259, doi:10.3390/biom14030259. This article has 55 citations.

11. (yamamoto1994signalingmechanismsin pages 4-5): Daisuke Yamamoto. Signaling mechanisms in induction of the r7 photoreceptor in the developing drosophila retina. BioEssays, 16:237-244, Apr 1994. URL: https://doi.org/10.1002/bies.950160406, doi:10.1002/bies.950160406. This article has 22 citations and is from a peer-reviewed journal.

12. (wang2011dcblbindingto pages 6-8): Pei-Yu Wang and Li-Mei Pai. D-cbl binding to drk leads to dose-dependent down-regulation of egfr signaling and increases receptor-ligand endocytosis. PLoS ONE, 6:e17097, Feb 2011. URL: https://doi.org/10.1371/journal.pone.0017097, doi:10.1371/journal.pone.0017097. This article has 14 citations and is from a peer-reviewed journal.

13. (wang2011dcblbindingto pages 1-2): Pei-Yu Wang and Li-Mei Pai. D-cbl binding to drk leads to dose-dependent down-regulation of egfr signaling and increases receptor-ligand endocytosis. PLoS ONE, 6:e17097, Feb 2011. URL: https://doi.org/10.1371/journal.pone.0017097, doi:10.1371/journal.pone.0017097. This article has 14 citations and is from a peer-reviewed journal.

14. (bilal2015theroleof pages 46-51): Mahmood Bilal. The role of the grb2 family of adaptor proteins in t cell receptor-mediated signaling. ArXiv, 2015. URL: https://doi.org/10.17077/etd.idezeqlf, doi:10.17077/etd.idezeqlf. This article has 0 citations.

15. (bilal2015theroleof pages 33-37): Mahmood Bilal. The role of the grb2 family of adaptor proteins in t cell receptor-mediated signaling. ArXiv, 2015. URL: https://doi.org/10.17077/etd.idezeqlf, doi:10.17077/etd.idezeqlf. This article has 0 citations.

16. (feller2006potentialdiseasetargets pages 18-18): Stephan Feller and Marc Lewitzky. Potential disease targets for drugs that disrupt protein - protein interactions of grb2 and crk family adaptors. Feb 2006. URL: https://doi.org/10.2174/138161206775474369, doi:10.2174/138161206775474369. This article has 58 citations and is from a peer-reviewed journal.

17. (ruminski2023mappingtheslp76 pages 6-7): Kilian Ruminski, Javier Celis-Gutierrez, Nicolas Jarmuzynski, Emilie Maturin, Stephane Audebert, Marie Malissen, Luc Camoin, Guillaume Voisinne, Bernard Malissen, and Romain Roncagalli. Mapping the slp76 interactome in t cells lacking each of the grb2-family adaptors reveals molecular plasticity of the tcr signaling pathway. Frontiers in Immunology, Mar 2023. URL: https://doi.org/10.3389/fimmu.2023.1139123, doi:10.3389/fimmu.2023.1139123. This article has 5 citations and is from a peer-reviewed journal.

18. (birge1996sh2andsh3‐containing pages 2-4): Raymond B. Birge, Beatrice S. Knudsen, Daniel Besser, and Hidesaburo Hanafusa. Sh2 and sh3‐containing adaptor proteins: redundant or independent mediators of intracellular signal transduction. Genes to Cells, 1:595-613, Jul 1996. URL: https://doi.org/10.1046/j.1365-2443.1996.00258.x, doi:10.1046/j.1365-2443.1996.00258.x. This article has 172 citations and is from a peer-reviewed journal.

19. (blum2021theinterproprotein pages 1-2): Matthias Blum, Hsin-Yu Chang, Sara Chuguransky, Tiago Grego, Swaathi Kandasaamy, Alex Mitchell, Gift Nuka, Typhaine Paysan-Lafosse, Matloob Qureshi, Shriya Raj, Lorna Richardson, Gustavo A Salazar, Lowri Williams, Peer Bork, Alan Bridge, Julian Gough, Daniel H Haft, Ivica Letunic, Aron Marchler-Bauer, Huaiyu Mi, Darren A Natale, Marco Necci, Christine A Orengo, Arun P Pandurangan, Catherine Rivoire, Christian J A Sigrist, Ian Sillitoe, Narmada Thanki, Paul D Thomas, Silvio C E Tosatto, Cathy H Wu, Alex Bateman, and Robert D Finn. The interpro protein families and domains database: 20 years on. Nucleic Acids Research, 49:D344-D354, Nov 2021. URL: https://doi.org/10.1093/nar/gkaa977, doi:10.1093/nar/gkaa977. This article has 2541 citations and is from a highest quality peer-reviewed journal.

20. (giubellino2010grb2andother pages 91-93): Alessio Giubellino and Praveen R. Arany. Grb2 and other adaptor proteins in tumor metastasis. ArXiv, pages 77-102, Jan 2010. URL: https://doi.org/10.1007/978-90-481-9522-0\_5, doi:10.1007/978-90-481-9522-0\_5. This article has 1 citations.

21. (feller2006potentialdiseasetargets pages 6-7): Stephan Feller and Marc Lewitzky. Potential disease targets for drugs that disrupt protein - protein interactions of grb2 and crk family adaptors. Feb 2006. URL: https://doi.org/10.2174/138161206775474369, doi:10.2174/138161206775474369. This article has 58 citations and is from a peer-reviewed journal.

22. (sandouk2023sh2sh2mediateddomainswappeddimerization pages 10-14): Aline Sandouk. Sh2/sh2-mediated domain-swapped dimerization of grb2 and its implications for grb2 function. Text, Jan 2023. URL: https://doi.org/10.25820/etd.006997, doi:10.25820/etd.006997. This article has 0 citations and is from a peer-reviewed journal.

23. (bilal2015theroleof pages 164-168): Mahmood Bilal. The role of the grb2 family of adaptor proteins in t cell receptor-mediated signaling. ArXiv, 2015. URL: https://doi.org/10.17077/etd.idezeqlf, doi:10.17077/etd.idezeqlf. This article has 0 citations.

24. (wang2024theconfigurationof pages 9-11): Dingyi Wang, Guoxia Liu, Yuxin Meng, Hongjie Chen, Zu Ye, and Ji Jing. The configuration of grb2 in protein interaction and signal transduction. Biomolecules, 14:259, Feb 2024. URL: https://doi.org/10.3390/biom14030259, doi:10.3390/biom14030259. This article has 55 citations.

25. (liu2012evolutionofsh2 pages 5-6): Bernard A. Liu and Piers D. Nash. Evolution of sh2 domains and phosphotyrosine signalling networks. Philosophical Transactions of the Royal Society B: Biological Sciences, 367:2556-2573, Sep 2012. URL: https://doi.org/10.1098/rstb.2012.0107, doi:10.1098/rstb.2012.0107. This article has 106 citations and is from a domain leading peer-reviewed journal.

26. (liu2011thesh2domain–containing pages 2-4): Bernard A. Liu, Eshana E. Shah, K. Jablonowski, Andrew B Stergachis, Brett W. Engelmann, and Piers Nash. The sh2 domain–containing proteins in 21 species establish the provenance and scope of phosphotyrosine signaling in eukaryotes. Science Signaling, 4:ra83-ra83, Dec 2011. URL: https://doi.org/10.1126/scisignal.2002105, doi:10.1126/scisignal.2002105. This article has 130 citations and is from a domain leading peer-reviewed journal.

27. (liu2011thesh2domain–containing pages 7-9): Bernard A. Liu, Eshana E. Shah, K. Jablonowski, Andrew B Stergachis, Brett W. Engelmann, and Piers Nash. The sh2 domain–containing proteins in 21 species establish the provenance and scope of phosphotyrosine signaling in eukaryotes. Science Signaling, 4:ra83-ra83, Dec 2011. URL: https://doi.org/10.1126/scisignal.2002105, doi:10.1126/scisignal.2002105. This article has 130 citations and is from a domain leading peer-reviewed journal.

28. (liu2012evolutionofsh2 pages 6-8): Bernard A. Liu and Piers D. Nash. Evolution of sh2 domains and phosphotyrosine signalling networks. Philosophical Transactions of the Royal Society B: Biological Sciences, 367:2556-2573, Sep 2012. URL: https://doi.org/10.1098/rstb.2012.0107, doi:10.1098/rstb.2012.0107. This article has 106 citations and is from a domain leading peer-reviewed journal.

29. (liu2011thesh2domain–containing pages 1-2): Bernard A. Liu, Eshana E. Shah, K. Jablonowski, Andrew B Stergachis, Brett W. Engelmann, and Piers Nash. The sh2 domain–containing proteins in 21 species establish the provenance and scope of phosphotyrosine signaling in eukaryotes. Science Signaling, 4:ra83-ra83, Dec 2011. URL: https://doi.org/10.1126/scisignal.2002105, doi:10.1126/scisignal.2002105. This article has 130 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PTHR46037-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR46037-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. yamamoto1994signalingmechanismsin pages 3-4
2. wang2024theconfigurationof pages 2-4
3. wang2024theconfigurationof pages 15-17
4. wang2011dcblbindingto pages 4-6
5. yamamoto1994signalingmechanismsin pages 4-5
6. blum2021theinterproprotein pages 1-2
7. bilal2015theroleof pages 46-51
8. bilal2015theroleof pages 164-168
9. bilal2015theroleof pages 33-37
10. wang2024theconfigurationof pages 1-2
11. wang2024theconfigurationof pages 5-7
12. wang2024theconfigurationof pages 7-9
13. wang2024theconfigurationof pages 11-12
14. wang2011dcblbindingto pages 6-8
15. wang2011dcblbindingto pages 1-2
16. feller2006potentialdiseasetargets pages 18-18
17. feller2006potentialdiseasetargets pages 6-7
18. wang2024theconfigurationof pages 9-11
19. https://doi.org/10.1002/bies.950160406,
20. https://doi.org/10.1016/j.bbrep.2024.101803,
21. https://doi.org/10.3390/biom14030259,
22. https://doi.org/10.1371/journal.pone.0017097,
23. https://doi.org/10.17077/etd.idezeqlf,
24. https://doi.org/10.2174/138161206775474369,
25. https://doi.org/10.3389/fimmu.2023.1139123,
26. https://doi.org/10.1046/j.1365-2443.1996.00258.x,
27. https://doi.org/10.1093/nar/gkaa977,
28. https://doi.org/10.1007/978-90-481-9522-0\_5,
29. https://doi.org/10.25820/etd.006997,
30. https://doi.org/10.1098/rstb.2012.0107,
31. https://doi.org/10.1126/scisignal.2002105,