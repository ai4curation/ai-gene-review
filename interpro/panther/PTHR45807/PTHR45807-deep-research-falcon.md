---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-28T21:42:23.513091'
end_time: '2026-06-28T22:00:27.271853'
duration_seconds: 1083.76
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR45807
  interpro_name: Janus Kinase (JAK)
  interpro_short_name: JAK
  interpro_type: family
  interpro_integrated: IPR051286
  member_databases: Not specified
  n_proteins: '7018'
  n_taxa: '3925'
  n_subfamilies: '6'
  interpro2go_terms: None mapped (no InterPro2GO terms for this entry)
  interpro_description: The JAK family of non-receptor tyrosine kinases is pivotal
    in signal transduction for various cellular processes including growth, development,
    differentiation, and immune response. Members of the family associate with cytokine
    receptors, phosphorylating them upon ligand binding, which creates docking sites
    for STAT proteins. These STAT proteins are then phosphorylated, dimerize, and
    translocate to the nucleus to regulate gene transcription. The family plays roles
    in both innate and adaptive immunity, hematopoiesis, and cell cycle regulation.
    They are involved in signaling pathways for type I and type II receptors, mediating
    responses to growth factors, cytokines, and interferons. The JAK kinases also
    have regulatory domains that modulate their activity, with some acting as pseudokinases.
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 42
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: PTHR45807-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR45807-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: PTHR45807-deep-research-falcon_artifacts/artifact-02.md
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
- **Accession:** PTHR45807
- **Name:** Janus Kinase (JAK)
- **Short name:** JAK
- **Entry type:** family
- **Integrated into / parent:** IPR051286
- **Member database signatures:** Not specified
- **Scale:** 7018 proteins across 3925 taxa, 6 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** The JAK family of non-receptor tyrosine kinases is pivotal in signal transduction for various cellular processes including growth, development, differentiation, and immune response. Members of the family associate with cytokine receptors, phosphorylating them upon ligand binding, which creates docking sites for STAT proteins. These STAT proteins are then phosphorylated, dimerize, and translocate to the nucleus to regulate gene transcription. The family plays roles in both innate and adaptive immunity, hematopoiesis, and cell cycle regulation. They are involved in signaling pathways for type I and type II receptors, mediating responses to growth factors, cytokines, and interferons. The JAK kinases also have regulatory domains that modulate their activity, with some acting as pseudokinases.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR45807 (Janus Kinase (JAK))**, structured to support GO annotation review.

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
- **Accession:** PTHR45807
- **Name:** Janus Kinase (JAK)
- **Short name:** JAK
- **Entry type:** family
- **Integrated into / parent:** IPR051286
- **Member database signatures:** Not specified
- **Scale:** 7018 proteins across 3925 taxa, 6 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** The JAK family of non-receptor tyrosine kinases is pivotal in signal transduction for various cellular processes including growth, development, differentiation, and immune response. Members of the family associate with cytokine receptors, phosphorylating them upon ligand binding, which creates docking sites for STAT proteins. These STAT proteins are then phosphorylated, dimerize, and translocate to the nucleus to regulate gene transcription. The family plays roles in both innate and adaptive immunity, hematopoiesis, and cell cycle regulation. They are involved in signaling pathways for type I and type II receptors, mediating responses to growth factors, cytokines, and interferons. The JAK kinases also have regulatory domains that modulate their activity, with some acting as pseudokinases.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR45807 (Janus Kinase (JAK))**, structured to support GO annotation review.

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


# InterPro Family Research Report: PTHR45807 — Janus Kinase (JAK) Family

## 1. Family Definition and Biochemistry

### 1.1 Definition and Mechanistic Overview

PTHR45807 corresponds to the Janus Kinase (JAK) family, a group of non-receptor tyrosine kinases that are obligate transducers of cytokine receptor signaling via the JAK-STAT (Signal Transducer and Activator of Transcription) pathway. The JAK family is defined by a unique multi-domain architecture comprising seven JAK homology (JH) domains numbered from C-terminus to N-terminus (JH1–JH7), organized into four functional modules: the FERM domain (JH5–JH7), SH2-like domain (JH3–JH4), pseudokinase domain (JH2), and kinase domain (JH1) (lv2024thejakstatpathway pages 11-12, kwon2022moleculardissectionof pages 1-2). This entry type is **family**, matching 7,018 proteins across 3,925 taxa with 6 subfamilies.

### 1.2 Domain Architecture and Fold

JAK proteins contain an N-terminal FERM-SH2 holodomain and a C-terminal tandem kinase cassette. The FERM domain is a tri-lobed structure consisting of an F1 ubiquitin-like subdomain, an F2 acyl-CoA-binding protein-like subdomain, and an F3 pleckstrin homology domain-like subdomain. Together with the SH2-like domain, it forms the FERM-SH2 holodomain that is crucial for binding the intracellular Box1 and Box2 motifs of cytokine receptors (lv2024thejakstatpathway pages 12-15, glassman2022structureofa pages 3-4, glassman2022structureofa pages 13-19).

The JH1 kinase domain (~275 amino acids) adopts a canonical bilobed protein kinase fold with N-terminal and C-terminal lobes connected by a hinge region that forms the ATP-binding cleft. The JH2 pseudokinase domain is structurally similar but is catalytically inactive in most family members, serving instead as a critical regulatory module (lv2024thejakstatpathway pages 11-12, kwon2022moleculardissectionof pages 2-4, lv2024thejakstatpathway pages 12-15).

The 3.6 Å cryo-EM structure of full-length murine JAK1 bound to the interferon λ receptor 1 (IFNλR1) intracellular domain, reported by Glassman et al. (2022), revealed that all seven domains form an extended structural unit. Dimerization is mediated by close-packing of the pseudokinase domains, and a two-step allosteric activation model was proposed: JAKs exist in an autoinhibited "closed" state with the TK domain folded back on the FERM-SH2 module; cytokine-mediated receptor dimerization shifts this equilibrium to an "open" state enabling JAK dimerization and transactivation (glassman2022structureofa pages 1-3, glassman2022structureofa pages 3-4, glassman2022structureofa pages 6-8).

### 1.3 Conserved Catalytic Residues

The conserved catalytic lysine in the JH1 AXK motif is K908 (JAK1), K882 (JAK2), K855 (JAK3), and K930 (TYK2). Activation loop tyrosines critical for kinase activation are Y1034 (JAK1), Y1007 (JAK2), Y980 (JAK3), and Y1054 (TYK2). The gatekeeper residue in the JH1 domain is a conserved methionine across all four mammalian JAKs (kwon2022moleculardissectionof pages 2-4, moncivais2023structuralanalysisof pages 1-3). The JH2 pseudokinase domains have divergent gatekeeper residues: Glu in JAK1, Gln in JAK2, and Thr in TYK2, which is pharmacologically important for selective inhibitor design (kwon2022moleculardissectionof pages 2-4).

The following table summarizes the JAK domain architecture and conserved residues:

| Domain | JH Designation | Approximate Size | Function | Key Conserved Residues |
|---|---|---:|---|---|
| FERM domain | JH5-JH7 | ~300 aa | Membrane-proximal receptor binding and membrane localization; forms part of the FERM-SH2 holodomain that recognizes cytokine receptor Box1/Box2 regions (lv2024thejakstatpathway pages 11-12, lv2024thejakstatpathway pages 12-15, glassman2022structureofa pages 3-4) | Conserved tri-lobed FERM organization with F1 ubiquitin-like, F2 acyl-CoA-binding protein-like, and F3 pleckstrin homology-like subdomains; no canonical catalytic residue assignment (lv2024thejakstatpathway pages 12-15) |
| SH2-like domain | JH3-JH4 | ~100 aa | Protein-protein interactions and receptor binding; packs against the FERM domain and contributes to cytokine receptor recognition (lv2024thejakstatpathway pages 11-12, moncivais2023structuralanalysisof pages 1-3, lv2024thejakstatpathway pages 12-15, glassman2022structureofa pages 3-4) | SH2-like fold; functions primarily in receptor engagement rather than catalysis, so no family-wide catalytic residue equivalent to JH1/JH2 is defined here (lv2024thejakstatpathway pages 12-15) |
| Pseudokinase domain | JH2 | ~300 aa | Regulatory/autoinhibitory domain that suppresses basal kinase activity yet is required for cytokine-inducible activation; central to JAK dimerization and allosteric control (kwon2022moleculardissectionof pages 2-4, lv2024thejakstatpathway pages 12-15, glassman2022structureofa pages 1-3, glassman2022structureofa pages 6-8) | JH2 gatekeeper residues differ across family members: Glu in JAK1, Gln in JAK2, Thr in TYK2; JH2 retains an ATP-binding cleft but lacks the canonical catalytic Asp found in active kinases; JAK2 JH2 can phosphorylate regulatory S523 and Y570 (lv2024thejakstatpathway pages 11-12, kwon2022moleculardissectionof pages 2-4, virtanen2023identificationofnovel pages 14-15) |
| Kinase domain | JH1 | ~275 aa | Catalytic tyrosine kinase domain responsible for trans-phosphorylation of JAKs, cytokine receptors, and STATs (lv2024thejakstatpathway pages 11-12, moncivais2023structuralanalysisof pages 1-3, glassman2022structureofa pages 1-3) | Conserved catalytic Lys: K908 (JAK1), K882 (JAK2), K855 (JAK3), K930 (TYK2); activation-loop Tyr: Y1034 (JAK1), Y1007 (JAK2), Y980 (JAK3), Y1054 (TYK2); gatekeeper residue is Met in all four JAKs (kwon2022moleculardissectionof pages 2-4, moncivais2023structuralanalysisof pages 1-3) |


*Table: This table summarizes the canonical JAK domain layout and the conserved residues most relevant for catalytic activity and regulation. It is useful for assessing which biochemical properties are likely to hold across the full PTHR45807 family.*

---

## 2. InterPro2GO Mapping Appropriateness

### 2.1 Current Status

**No InterPro2GO terms are currently mapped to PTHR45807.** Therefore, the review focuses on whether GO terms *should* be added and, if so, which ones are appropriate for the entire family.

### 2.2 Assessment of Candidate GO Terms

Given that PTHR45807 is a **family-type** entry (not a domain or superfamily), whole-protein function terms are in principle appropriate, provided the family is functionally homogeneous. All members of the JAK family are non-receptor tyrosine kinases that bind ATP, phosphorylate substrates, and participate in JAK-STAT signaling cascades downstream of cytokine receptors (wei2024insightintojanus pages 2-2, moncivais2023structuralanalysisof pages 1-3, jensen2023allosterictyk2inhibition pages 2-4, lv2024thejakstatpathway pages 11-12). These core biochemical and pathway-level functions are conserved from invertebrate orthologs (e.g., *Drosophila* Hopscotch) through vertebrate JAK1/JAK2/JAK3/TYK2 (maurya2021maheshvararegulatesjakstat pages 1-2, yu2022drosophilainnateimmunity pages 8-9).

However, more specific biological process terms (e.g., hematopoiesis, adaptive immune response, specific cytokine signaling pathways) are only applicable to subsets of the family. JAK3 is restricted to the common gamma chain and lymphocyte biology (garridotrigo2020molecularstructureand pages 16-18), JAK2 is the primary mediator of hormone-like receptor signaling and definitive hematopoiesis (garridotrigo2020molecularstructureand pages 10-12, castelosoccio2023proteinkinasesdrug pages 7-8), while invertebrate JAKs have distinct developmental and innate immune roles (yu2022drosophilainnateimmunity pages 8-9).

The following table provides a detailed assessment of candidate GO terms:

| GO Term | GO ID | Aspect (MF/BP/CC) | Appropriate for entire family? | Rationale | Recommendation |
|---|---|---|---|---|---|
| Non-receptor protein tyrosine kinase activity | GO:PLACEHOLDER | MF | Yes | The catalytic JH1 domain is conserved across JAK family members and mediates tyrosine phosphorylation of receptors, JAKs, and STATs; this is the core family-defining molecular function across vertebrate JAKs and invertebrate orthologs such as Hopscotch (lv2024thejakstatpathway pages 11-12, glassman2022structureofa pages 1-3, wei2024insightintojanus pages 2-2, garridotrigo2020molecularstructureand pages 4-5) | RECOMMEND ADDITION |
| ATP binding | GO:0005524 | MF | Yes | All JAKs bind ATP in the catalytic JH1 cleft, and JH2 pseudokinase domains also retain nucleotide binding; however, this term is generic and lower-information than the kinase activity term (kwon2022moleculardissectionof pages 2-4, moncivais2023structuralanalysisof pages 1-3) | RECOMMEND ADDITION (generic/low information) |
| Protein phosphorylation | GO:0006468 | BP | Yes | Protein phosphorylation is the central biochemical output of JAK proteins, including trans-phosphorylation of receptor tails, JAK activation loops, and STAT substrates (glassman2022structureofa pages 1-3, wei2024insightintojanus pages 2-2, moncivais2023structuralanalysisof pages 1-3, jensen2023allosterictyk2inhibition pages 2-4, garridotrigo2020molecularstructureand pages 8-9) | RECOMMEND ADDITION |
| JAK-STAT cascade | GO:0007259 | BP | Yes | Participation in the JAK-STAT signaling cascade is the defining pathway-level role of the family across animals, including vertebrate JAK1/JAK2/JAK3/TYK2 and the single Drosophila JAK Hopscotch (maurya2021maheshvararegulatesjakstat pages 1-2, yu2022drosophilainnateimmunity pages 8-9, wei2024insightintojanus pages 2-2, jensen2023allosterictyk2inhibition pages 2-4, lv2024thejakstatpathway pages 11-12) | RECOMMEND ADDITION |
| Cytokine-mediated signaling pathway | GO:0019221 | BP | Yes | Broadly appropriate because JAKs are receptor-associated kinases for cytokine signaling, but only the general term is safe at family level since precise receptor/cytokine usage differs strongly among JAK1, JAK2, JAK3, TYK2, and invertebrate homologs (wei2024insightintojanus pages 2-2, garridotrigo2020molecularstructureand pages 8-9, garridotrigo2020molecularstructureand pages 16-18, wei2024insightintojanus pages 2-3) | RECOMMEND ADDITION (general term only) |
| Cytoplasm | GO:0005737 | CC | Yes | JAKs are non-receptor tyrosine kinases that localize on the cytoplasmic side of cytokine receptors rather than being transmembrane kinases; this is broadly true across the family (moncivais2023structuralanalysisof pages 1-3, wei2024insightintojanus pages 2-2, lv2024thejakstatpathway pages 11-12, garridotrigo2020molecularstructureand pages 4-5) | RECOMMEND ADDITION |
| Hematopoiesis | GO:0030097 | BP | No | Hematopoietic functions are especially prominent for vertebrate JAK2 and some JAK1/JAK3 contexts, but they are not universal across the family and are not applicable to invertebrate members such as Hopscotch (garridotrigo2020molecularstructureand pages 10-12, garridotrigo2020molecularstructureand pages 8-9, garridotrigo2020molecularstructureand pages 27-28, yu2022drosophilainnateimmunity pages 8-9, castelosoccio2023proteinkinasesdrug pages 7-8) | DO NOT MAP at family level |
| Adaptive immune response | GO:0002250 | BP | No | This term excludes many invertebrate family members and overstates the role of some vertebrate JAKs; JAKs also act in innate immunity, development, proliferation, and antiviral responses, so adaptive immunity is not a universal family property (garridotrigo2020molecularstructureand pages 16-18, xie2023molecularcharacterizationand pages 9-12, yu2022drosophilainnateimmunity pages 8-9, garridotrigo2020molecularstructureand pages 18-19) | DO NOT MAP at family level |


*Table: This table summarizes which GO terms are appropriate to consider for InterPro entry PTHR45807 at the family level, and which would over-annotate the family. It is useful for deciding whether to add broad core terms while avoiding lineage- or subfamily-specific biological process annotations.*

---

## 3. Functional Divergence Across the Family

### 3.1 Four Mammalian Subfamilies

The mammalian JAK family comprises four members with significant functional divergence:

- **JAK1**: Broadly expressed, participates in signaling through gp130-family receptors, type I/II/III interferon receptors, and many heterodimeric cytokine receptor complexes. Knockout is perinatal lethal in mice, demonstrating its nonredundant essential role (garridotrigo2020molecularstructureand pages 10-12, garridotrigo2020molecularstructureand pages 27-28).

- **JAK2**: Broadly expressed, uniquely mediates signaling through homodimeric hormone-like receptors (EPO, TPO, GH, PRL, G-CSF) and is the sole JAK required for definitive hematopoiesis. JAK2 knockout is embryonic lethal. The V617F gain-of-function mutation in the pseudokinase domain drives myeloproliferative neoplasms (perner2025malignantjaksignalingat pages 4-5, perner2025malignantjaksignalingat pages 6-7, castelosoccio2023proteinkinasesdrug pages 7-8).

- **JAK3**: Uniquely restricted to hematopoietic cells and exclusively associates with the common gamma chain (γc/IL-2RG). Loss-of-function mutations cause severe combined immunodeficiency (SCID) with absent T and NK lymphocytes (garridotrigo2020molecularstructureand pages 16-18, garridotrigo2020molecularstructureand pages 18-19).

- **TYK2**: Broadly expressed but plays a more restricted role, primarily in type I interferon and IL-12/IL-23 signaling. TYK2 deficiency is viable in humans and mice but impairs antiviral and IL-12-dependent immune responses. TYK2 is the target of the first-in-class allosteric pseudokinase inhibitor deucravacitinib (garridotrigo2020molecularstructureand pages 10-12, jensen2023allosterictyk2inhibition pages 2-4).

### 3.2 Invertebrate Orthologs

In *Drosophila melanogaster*, the single JAK ortholog Hopscotch (Hop) is constitutively associated with the Domeless receptor and is activated by Unpaired ligands (Upd, Upd2, Upd3). Hopscotch regulates developmental patterning, innate immunity, hemocyte proliferation, and stress responses (maurya2021maheshvararegulatesjakstat pages 1-2, yu2022drosophilainnateimmunity pages 8-9). Teleost fish such as golden pompano (*Trachinotus ovatus*) possess all four JAK orthologs (JAK1, JAK2a, JAK3, TYK2) with conserved domain architecture and roles in immune defense (xie2023molecularcharacterizationand pages 9-12).

### 3.3 Pseudokinase Domain as a Pseudo-enzyme Module

The JH2 pseudokinase domain is a signature feature of the JAK family that distinguishes it from other tyrosine kinases. Although classified as catalytically inactive, JAK2's JH2 domain retains dual-specificity kinase activity capable of phosphorylating S523 and Y570, which serves an autoinhibitory function (lv2024thejakstatpathway pages 11-12, virtanen2023identificationofnovel pages 14-15). Deletion of the JH2 domain increases basal kinase activity but abolishes cytokine-inducible activation, demonstrating its essential regulatory role (lv2024thejakstatpathway pages 12-15, moncivais2023structuralanalysisof pages 16-17). This represents pseudo-enzyme biology: the JH2 domain retains the kinase fold but has been repurposed for regulation rather than canonical substrate phosphorylation.

The following table summarizes the functional divergence across JAK family members:

| Protein | Taxonomic scope | Expression pattern | Principal receptor/cytokine specificity | Key biological roles | Loss-of-function / knockout phenotype | Representative disease associations | Evidence |
|---|---|---|---|---|---|---|---|
| JAK1 | Vertebrates / mammals | Broadly expressed / near-ubiquitous | Partners in gp130-family signaling; type I, II, and III interferon receptor pathways; also many heterodimeric cytokine receptor complexes | Core cytokine signal transduction, immune regulation, development, hematopoietic and inflammatory signaling | Knockout is perinatal or embryonic lethal; nonredundant requirement for multiple cytokine responses | Activating variants in inflammatory syndromes and rare leukemias; loss impairs cytokine signaling | (wei2024insightintojanus pages 2-2, garridotrigo2020molecularstructureand pages 8-9, garridotrigo2020molecularstructureand pages 27-28, garridotrigo2020molecularstructureand pages 9-10, perner2025malignantjaksignalingat pages 4-5) |
| JAK2 | Vertebrates / mammals | Broadly expressed / near-ubiquitous | Homodimeric signaling downstream of EPO, TPO, GH, PRL, G-CSF and related hormone-like receptors; also IFNγ and other cytokine pathways | Definitive hematopoiesis, erythropoiesis, myeloid signaling, cytokine receptor phosphorylation and STAT activation | Knockout is embryonic lethal with failure of definitive hematopoiesis | JAK2 V617F and related activating mutations drive myeloproliferative neoplasms (PV, ET, PMF); therapeutic target of ruxolitinib | (garridotrigo2020molecularstructureand pages 10-12, garridotrigo2020molecularstructureand pages 8-9, perner2025malignantjaksignalingat pages 4-5, perner2025malignantjaksignalingat pages 6-7, castelosoccio2023proteinkinasesdrug pages 7-8) |
| JAK3 | Vertebrates / mammals | Predominantly hematopoietic-restricted | Exclusively associates with the common gamma chain (γc/IL2RG) in IL-2, IL-4, IL-7, IL-9, IL-15, IL-21 receptor signaling, typically with JAK1 | Lymphocyte maturation, survival, activation, differentiation; adaptive immune development | Loss causes severe combined immunodeficiency (SCID), classically T−/NK− with preserved but functionally impaired B cells | Inactivating variants cause JAK3-SCID; activating variants can contribute to leukemias | (wei2024insightintojanus pages 2-2, garridotrigo2020molecularstructureand pages 16-18, castelosoccio2023proteinkinasesdrug pages 7-8, garridotrigo2020molecularstructureand pages 18-19) |
| TYK2 | Vertebrates / mammals | Broadly expressed / near-ubiquitous | Type I interferon receptors; IL-12 and IL-23 family signaling; also contributes to type III IFN and selected IL-10 family receptor complexes | Antiviral defense, IL-12/IL-23 signaling, innate/adaptive immune coordination | Viable deficiency/knockout with impaired type I IFN and IL-12 responses; less severe than JAK1/JAK2 loss | TYK2 deficiency causes susceptibility to infection/immune dysregulation; TYK2 is targeted by allosteric inhibitors such as deucravacitinib | (garridotrigo2020molecularstructureand pages 10-12, garridotrigo2020molecularstructureand pages 8-9, garridotrigo2020molecularstructureand pages 9-10, jensen2023allosterictyk2inhibition pages 2-4) |
| Hopscotch (Hop) | Insects / Drosophila | Broadly expressed; sole Drosophila JAK | Domeless receptor pathway activated by Unpaired ligands (Upd/Upd2/Upd3) | Developmental patterning, innate immunity, hemocyte proliferation, epithelial repair, stress and wound responses | Loss disrupts JAK/STAT-dependent development and immunity; pathway is simpler than vertebrates with one JAK and one major STAT | Hyperactive hop alleles drive overproliferation/tumor-like phenotypes in flies; model for conserved JAK-STAT biology | (maurya2021maheshvararegulatesjakstat pages 1-2, yu2022drosophilainnateimmunity pages 8-9) |


*Table: This table compares the major JAK family members and Drosophila Hopscotch across expression, receptor usage, biological roles, knockout phenotypes, and disease relevance. It is useful for assessing how much functional homogeneity exists across the InterPro JAK family for GO annotation review.*

---

## 4. Taxonomic Scope

### 4.1 Distribution

The PTHR45807 signature matches 7,018 proteins across 3,925 taxa with 6 subfamilies. The JAK-STAT pathway is an evolutionarily conserved signaling mechanism that is present across Metazoa. Key observations on taxonomic distribution include:

- **Insects**: *Drosophila* possesses a single JAK (Hopscotch) and a single STAT (Stat92E), with JAK-STAT playing roles in innate immunity, development, and tissue homeostasis (maurya2021maheshvararegulatesjakstat pages 1-2, yu2022drosophilainnateimmunity pages 8-9). Other insects, including planthoppers and beetles, also utilize JAK-STAT for antiviral responses.

- **Crustaceans**: Decapod crustaceans express JAK-STAT pathway components, and this pathway functions in immune defense and potentially other physiological processes (xie2023molecularcharacterizationand pages 9-12).

- **Teleost fish**: Bony fish possess all four JAK orthologs (JAK1, JAK2, JAK3, TYK2) with conserved domain organization. Sequence identity with mammalian orthologs ranges from 66–92%, with higher conservation among fish species (xie2023molecularcharacterizationand pages 9-12).

- **Mammals/Vertebrates**: The full complement of JAK1, JAK2, JAK3, and TYK2 is present, with the expansion of cytokine receptor families and the JAK-STAT pathway supporting both innate and adaptive immunity (wei2024insightintojanus pages 2-2).

- **Pre-metazoan origins**: The choanoflagellate *Monosiga brevicollis* possesses a tyrosine kinase signaling network more elaborate than any known metazoan, suggesting that the ancestral kinase signaling machinery predates multicellularity (yeung2021evolutionoffunctional pages 13-14, yeung2021evolutionoffunctional pages 14-15). However, the canonical JAK-STAT pathway with its characteristic domain architecture appears to be a metazoan innovation.

### 4.2 Functional Conservation Across Taxa

The core biochemical properties of the family — non-receptor tyrosine kinase activity, ATP binding, protein phosphorylation, and participation in JAK-STAT signaling cascades — are broadly conserved across all taxa in which the signature is found. However, the specific cytokine receptor partnerships, biological process contexts (e.g., hematopoiesis, adaptive immunity), and the number of paralogous JAK genes vary substantially among clades. In invertebrates, JAK-STAT signaling predominantly mediates innate immune responses, developmental patterning, and stress responses, whereas in jawed vertebrates, it additionally supports adaptive immune cell development and function (xie2023molecularcharacterizationand pages 9-12, yu2022drosophilainnateimmunity pages 8-9).

---

## 5. Over-Annotation Verdict

### 5.1 Assessment Summary

Since **no InterPro2GO terms are currently mapped** to PTHR45807, the question of over-annotation does not arise in the conventional sense. Instead, the entry represents an **under-annotated** family for which carefully selected GO terms could be added.

### 5.2 Functional Homogeneity of the Family

Despite significant functional divergence among subfamilies (particularly in receptor specificity, expression patterns, and biological process involvement), all members of the JAK family share a set of core properties:

1. **All are non-receptor tyrosine kinases** with an active JH1 kinase domain.
2. **All bind ATP** in the catalytic cleft.
3. **All phosphorylate protein substrates**, including cytokine receptors and STAT transcription factors.
4. **All participate in JAK-STAT signaling cascades** downstream of cytokine receptors.
5. **All are cytoplasmic proteins** associated with the intracellular domains of transmembrane receptors.

These properties are conserved from invertebrate orthologs (e.g., *Drosophila* Hopscotch) through all four mammalian JAKs (maurya2021maheshvararegulatesjakstat pages 1-2, yu2022drosophilainnateimmunity pages 8-9, wei2024insightintojanus pages 2-2, lv2024thejakstatpathway pages 11-12).

### 5.3 Recommendations

**Recommended GO action pattern: ACCEPT for core terms / DO NOT MAP for subfamily-specific terms**

| Action | Details |
|--------|---------|
| **ADD (Recommended)** | Non-receptor protein tyrosine kinase activity (MF); ATP binding (MF); protein phosphorylation (BP); JAK-STAT cascade (BP); cytokine-mediated signaling pathway (BP, general term); cytoplasm (CC) |
| **DO NOT MAP at family level** | Hematopoiesis, adaptive immune response, specific cytokine signaling (e.g., interferon signaling), or immune cell differentiation terms — these should be placed on subfamily-specific child entries if available |

**Rationale**: The PTHR45807 family is a well-defined, functionally coherent protein family whose members share a defining set of biochemical activities and pathway involvement. The absence of any InterPro2GO mappings represents a missed opportunity for broad, accurate annotation. The recommended terms are safe for application across the entire 7,018-protein, 3,925-taxon family because they describe the conserved molecular function and core pathway participation that define what it means to be a JAK family member. More specific biological process terms (e.g., hematopoiesis, lymphocyte development, interferon signaling) should be restricted to the 6 recognized subfamilies or to individual gene-level annotations, as these functions are not universal across all members.

**Recommendations for InterPro itself**: If the 6 subfamilies correspond to the known mammalian JAK1, JAK2, JAK3, and TYK2 orthologs (plus invertebrate lineages), more specific GO terms describing receptor partnerships and biological processes should be mapped at those child-entry levels rather than at the parent PTHR45807 family level. This hierarchical approach would provide informative annotation without over-annotation risk.

References

1. (lv2024thejakstatpathway pages 11-12): You Lv, Jianxun Qi, Jeff J. Babon, Longxing Cao, Guohuang Fan, Jiajia Lang, Jin Zhang, Pengbing Mi, B. Kobe, and Faming Wang. The jak-stat pathway: from structural biology to cytokine engineering. Signal Transduction and Targeted Therapy, Aug 2024. URL: https://doi.org/10.1038/s41392-024-01934-w, doi:10.1038/s41392-024-01934-w. This article has 137 citations and is from a peer-reviewed journal.

2. (kwon2022moleculardissectionof pages 1-2): Sunghark Kwon. Molecular dissection of janus kinases as drug targets for inflammatory diseases. Frontiers in Immunology, Dec 2022. URL: https://doi.org/10.3389/fimmu.2022.1075192, doi:10.3389/fimmu.2022.1075192. This article has 29 citations and is from a peer-reviewed journal.

3. (lv2024thejakstatpathway pages 12-15): You Lv, Jianxun Qi, Jeff J. Babon, Longxing Cao, Guohuang Fan, Jiajia Lang, Jin Zhang, Pengbing Mi, B. Kobe, and Faming Wang. The jak-stat pathway: from structural biology to cytokine engineering. Signal Transduction and Targeted Therapy, Aug 2024. URL: https://doi.org/10.1038/s41392-024-01934-w, doi:10.1038/s41392-024-01934-w. This article has 137 citations and is from a peer-reviewed journal.

4. (glassman2022structureofa pages 3-4): Caleb R. Glassman, Naotaka Tsutsumi, Robert A. Saxton, Patrick J. Lupardus, Kevin M. Jude, and K. Christopher Garcia. Structure of a janus kinase cytokine receptor complex reveals the basis for dimeric activation. Apr 2022. URL: https://doi.org/10.1126/science.abn8933, doi:10.1126/science.abn8933. This article has 185 citations and is from a highest quality peer-reviewed journal.

5. (glassman2022structureofa pages 13-19): Caleb R. Glassman, Naotaka Tsutsumi, Robert A. Saxton, Patrick J. Lupardus, Kevin M. Jude, and K. Christopher Garcia. Structure of a janus kinase cytokine receptor complex reveals the basis for dimeric activation. Apr 2022. URL: https://doi.org/10.1126/science.abn8933, doi:10.1126/science.abn8933. This article has 185 citations and is from a highest quality peer-reviewed journal.

6. (kwon2022moleculardissectionof pages 2-4): Sunghark Kwon. Molecular dissection of janus kinases as drug targets for inflammatory diseases. Frontiers in Immunology, Dec 2022. URL: https://doi.org/10.3389/fimmu.2022.1075192, doi:10.3389/fimmu.2022.1075192. This article has 29 citations and is from a peer-reviewed journal.

7. (glassman2022structureofa pages 1-3): Caleb R. Glassman, Naotaka Tsutsumi, Robert A. Saxton, Patrick J. Lupardus, Kevin M. Jude, and K. Christopher Garcia. Structure of a janus kinase cytokine receptor complex reveals the basis for dimeric activation. Apr 2022. URL: https://doi.org/10.1126/science.abn8933, doi:10.1126/science.abn8933. This article has 185 citations and is from a highest quality peer-reviewed journal.

8. (glassman2022structureofa pages 6-8): Caleb R. Glassman, Naotaka Tsutsumi, Robert A. Saxton, Patrick J. Lupardus, Kevin M. Jude, and K. Christopher Garcia. Structure of a janus kinase cytokine receptor complex reveals the basis for dimeric activation. Apr 2022. URL: https://doi.org/10.1126/science.abn8933, doi:10.1126/science.abn8933. This article has 185 citations and is from a highest quality peer-reviewed journal.

9. (moncivais2023structuralanalysisof pages 1-3): Omar J. Rodriguez Moncivais, Stephanie A. Chavez, Victor H. Estrada Jimenez, Shengjie Sun, Lin Li, Robert A. Kirken, and Georgialina Rodriguez. Structural analysis of janus tyrosine kinase variants in hematological malignancies: implications for drug development and opportunities for novel therapeutic strategies. International Journal of Molecular Sciences, 24:14573, Sep 2023. URL: https://doi.org/10.3390/ijms241914573, doi:10.3390/ijms241914573. This article has 8 citations.

10. (virtanen2023identificationofnovel pages 14-15): Anniina T. Virtanen, Teemu Haikarainen, Parthasarathy Sampathkumar, Maaria Palmroth, Sanna Liukkonen, Jianping Liu, Natalia Nekhotiaeva, Stevan R. Hubbard, and Olli Silvennoinen. Identification of novel small molecule ligands for jak2 pseudokinase domain. Pharmaceuticals, 16:75, Jan 2023. URL: https://doi.org/10.3390/ph16010075, doi:10.3390/ph16010075. This article has 20 citations.

11. (wei2024insightintojanus pages 2-2): Tian‐Hua Wei, Meng‐Yi Lu, Si‐Hui Yao, Yu‐Qi Hong, Jin Yang, Meng‐Yuan Zhang, Yu‐Qi Yin, Yu‐Jie Han, Qing‐Qing Li, Zi‐Xuan Wang, Yi‐Bo Wang, Zhen‐Jiang Tong, Yun Zhou, Wei‐Chen Dai, Yan‐Cheng Yu, Shan‐Liang Sun, Ye Yang, Nian‐Guang Li, and Zhi‐Hao Shi. Insight into janus kinases specificity: from molecular architecture to cancer therapeutics. MedComm – Oncology, Mar 2024. URL: https://doi.org/10.1002/mog2.69, doi:10.1002/mog2.69. This article has 20 citations.

12. (jensen2023allosterictyk2inhibition pages 2-4): Lise Torp Jensen, Kathrine E. Attfield, Marc Feldmann, and Lars Fugger. Allosteric tyk2 inhibition: redefining autoimmune disease therapy beyond jak1-3 inhibitors. Nov 2023. URL: https://doi.org/10.1016/j.ebiom.2023.104840, doi:10.1016/j.ebiom.2023.104840. This article has 70 citations and is from a peer-reviewed journal.

13. (maurya2021maheshvararegulatesjakstat pages 1-2): Bhawana Maurya, Satya Surabhi, Rituparna Das, Pranjali Pandey, Ashim Mukherjee, and Mousumi Mutsuddi. Maheshvara regulates jak/stat signaling by interacting and stabilizing hopscotch transcripts which leads to apoptosis in drosophila melanogaster. Cell Death &amp; Disease, Apr 2021. URL: https://doi.org/10.1038/s41419-021-03649-0, doi:10.1038/s41419-021-03649-0. This article has 7 citations and is from a peer-reviewed journal.

14. (yu2022drosophilainnateimmunity pages 8-9): Shichao Yu, Fangzhou Luo, Yongyi Xu, Yan Zhang, and Li Hua Jin. Drosophila innate immunity involves multiple signaling pathways and coordinated communication between different tissues. Frontiers in Immunology, Jul 2022. URL: https://doi.org/10.3389/fimmu.2022.905370, doi:10.3389/fimmu.2022.905370. This article has 209 citations and is from a peer-reviewed journal.

15. (garridotrigo2020molecularstructureand pages 16-18): Alba Garrido-Trigo and Azucena Salas. Molecular structure and function of janus kinases: implications for the development of inhibitors. Journal of Crohn's & Colitis, 14:S713-S724, Dec 2020. URL: https://doi.org/10.1093/ecco-jcc/jjz206, doi:10.1093/ecco-jcc/jjz206. This article has 80 citations.

16. (garridotrigo2020molecularstructureand pages 10-12): Alba Garrido-Trigo and Azucena Salas. Molecular structure and function of janus kinases: implications for the development of inhibitors. Journal of Crohn's & Colitis, 14:S713-S724, Dec 2020. URL: https://doi.org/10.1093/ecco-jcc/jjz206, doi:10.1093/ecco-jcc/jjz206. This article has 80 citations.

17. (castelosoccio2023proteinkinasesdrug pages 7-8): Leslie Castelo-Soccio, Hanna Kim, Massimo Gadina, Pamela L. Schwartzberg, Arian Laurence, and John J. O’Shea. Protein kinases: drug targets for immunological disorders. Nature Reviews. Immunology, 23:1-20, May 2023. URL: https://doi.org/10.1038/s41577-023-00877-7, doi:10.1038/s41577-023-00877-7. This article has 134 citations.

18. (garridotrigo2020molecularstructureand pages 4-5): Alba Garrido-Trigo and Azucena Salas. Molecular structure and function of janus kinases: implications for the development of inhibitors. Journal of Crohn's & Colitis, 14:S713-S724, Dec 2020. URL: https://doi.org/10.1093/ecco-jcc/jjz206, doi:10.1093/ecco-jcc/jjz206. This article has 80 citations.

19. (garridotrigo2020molecularstructureand pages 8-9): Alba Garrido-Trigo and Azucena Salas. Molecular structure and function of janus kinases: implications for the development of inhibitors. Journal of Crohn's & Colitis, 14:S713-S724, Dec 2020. URL: https://doi.org/10.1093/ecco-jcc/jjz206, doi:10.1093/ecco-jcc/jjz206. This article has 80 citations.

20. (wei2024insightintojanus pages 2-3): Tian‐Hua Wei, Meng‐Yi Lu, Si‐Hui Yao, Yu‐Qi Hong, Jin Yang, Meng‐Yuan Zhang, Yu‐Qi Yin, Yu‐Jie Han, Qing‐Qing Li, Zi‐Xuan Wang, Yi‐Bo Wang, Zhen‐Jiang Tong, Yun Zhou, Wei‐Chen Dai, Yan‐Cheng Yu, Shan‐Liang Sun, Ye Yang, Nian‐Guang Li, and Zhi‐Hao Shi. Insight into janus kinases specificity: from molecular architecture to cancer therapeutics. MedComm – Oncology, Mar 2024. URL: https://doi.org/10.1002/mog2.69, doi:10.1002/mog2.69. This article has 20 citations.

21. (garridotrigo2020molecularstructureand pages 27-28): Alba Garrido-Trigo and Azucena Salas. Molecular structure and function of janus kinases: implications for the development of inhibitors. Journal of Crohn's & Colitis, 14:S713-S724, Dec 2020. URL: https://doi.org/10.1093/ecco-jcc/jjz206, doi:10.1093/ecco-jcc/jjz206. This article has 80 citations.

22. (xie2023molecularcharacterizationand pages 9-12): Yushuai Xie, Mingqu Chen, Pengfu Han, Xiang Liang, Meng Yang, Zhuanling Lu, and Youchuan Wei. Molecular characterization and expression analysis of four janus kinases (jak1, jak2a, jak3 and tyk2) from golden pompano (trachinotus ovatus). Fishes, 8:245, May 2023. URL: https://doi.org/10.3390/fishes8050245, doi:10.3390/fishes8050245. This article has 7 citations.

23. (garridotrigo2020molecularstructureand pages 18-19): Alba Garrido-Trigo and Azucena Salas. Molecular structure and function of janus kinases: implications for the development of inhibitors. Journal of Crohn's & Colitis, 14:S713-S724, Dec 2020. URL: https://doi.org/10.1093/ecco-jcc/jjz206, doi:10.1093/ecco-jcc/jjz206. This article has 80 citations.

24. (perner2025malignantjaksignalingat pages 4-5): Florian Perner, Heike L. Pahl, Robert Zeiser, and Florian H. Heidel. Malignant jak-signaling: at the interface of inflammation and malignant transformation. Leukemia, 39:1011-1030, Mar 2025. URL: https://doi.org/10.1038/s41375-025-02569-8, doi:10.1038/s41375-025-02569-8. This article has 56 citations and is from a highest quality peer-reviewed journal.

25. (perner2025malignantjaksignalingat pages 6-7): Florian Perner, Heike L. Pahl, Robert Zeiser, and Florian H. Heidel. Malignant jak-signaling: at the interface of inflammation and malignant transformation. Leukemia, 39:1011-1030, Mar 2025. URL: https://doi.org/10.1038/s41375-025-02569-8, doi:10.1038/s41375-025-02569-8. This article has 56 citations and is from a highest quality peer-reviewed journal.

26. (moncivais2023structuralanalysisof pages 16-17): Omar J. Rodriguez Moncivais, Stephanie A. Chavez, Victor H. Estrada Jimenez, Shengjie Sun, Lin Li, Robert A. Kirken, and Georgialina Rodriguez. Structural analysis of janus tyrosine kinase variants in hematological malignancies: implications for drug development and opportunities for novel therapeutic strategies. International Journal of Molecular Sciences, 24:14573, Sep 2023. URL: https://doi.org/10.3390/ijms241914573, doi:10.3390/ijms241914573. This article has 8 citations.

27. (garridotrigo2020molecularstructureand pages 9-10): Alba Garrido-Trigo and Azucena Salas. Molecular structure and function of janus kinases: implications for the development of inhibitors. Journal of Crohn's & Colitis, 14:S713-S724, Dec 2020. URL: https://doi.org/10.1093/ecco-jcc/jjz206, doi:10.1093/ecco-jcc/jjz206. This article has 80 citations.

28. (yeung2021evolutionoffunctional pages 13-14): Wayland Yeung, Annie Kwon, Rahil Taujale, Claire Bunn, Aarya Venkat, and Natarajan Kannan. Evolution of functional diversity in the holozoan tyrosine kinome. Molecular Biology and Evolution, 38:5625-5639, Aug 2021. URL: https://doi.org/10.1093/molbev/msab272, doi:10.1093/molbev/msab272. This article has 21 citations and is from a highest quality peer-reviewed journal.

29. (yeung2021evolutionoffunctional pages 14-15): Wayland Yeung, Annie Kwon, Rahil Taujale, Claire Bunn, Aarya Venkat, and Natarajan Kannan. Evolution of functional diversity in the holozoan tyrosine kinome. Molecular Biology and Evolution, 38:5625-5639, Aug 2021. URL: https://doi.org/10.1093/molbev/msab272, doi:10.1093/molbev/msab272. This article has 21 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PTHR45807-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR45807-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](PTHR45807-deep-research-falcon_artifacts/artifact-02.md)

## Citations

1. kwon2022moleculardissectionof pages 2-4
2. lv2024thejakstatpathway pages 12-15
3. garridotrigo2020molecularstructureand pages 16-18
4. yu2022drosophilainnateimmunity pages 8-9
5. xie2023molecularcharacterizationand pages 9-12
6. wei2024insightintojanus pages 2-2
7. lv2024thejakstatpathway pages 11-12
8. kwon2022moleculardissectionof pages 1-2
9. glassman2022structureofa pages 3-4
10. glassman2022structureofa pages 13-19
11. glassman2022structureofa pages 1-3
12. glassman2022structureofa pages 6-8
13. moncivais2023structuralanalysisof pages 1-3
14. virtanen2023identificationofnovel pages 14-15
15. maurya2021maheshvararegulatesjakstat pages 1-2
16. garridotrigo2020molecularstructureand pages 10-12
17. castelosoccio2023proteinkinasesdrug pages 7-8
18. garridotrigo2020molecularstructureand pages 4-5
19. garridotrigo2020molecularstructureand pages 8-9
20. wei2024insightintojanus pages 2-3
21. garridotrigo2020molecularstructureand pages 27-28
22. garridotrigo2020molecularstructureand pages 18-19
23. perner2025malignantjaksignalingat pages 4-5
24. perner2025malignantjaksignalingat pages 6-7
25. moncivais2023structuralanalysisof pages 16-17
26. garridotrigo2020molecularstructureand pages 9-10
27. yeung2021evolutionoffunctional pages 13-14
28. yeung2021evolutionoffunctional pages 14-15
29. https://doi.org/10.1038/s41392-024-01934-w,
30. https://doi.org/10.3389/fimmu.2022.1075192,
31. https://doi.org/10.1126/science.abn8933,
32. https://doi.org/10.3390/ijms241914573,
33. https://doi.org/10.3390/ph16010075,
34. https://doi.org/10.1002/mog2.69,
35. https://doi.org/10.1016/j.ebiom.2023.104840,
36. https://doi.org/10.1038/s41419-021-03649-0,
37. https://doi.org/10.3389/fimmu.2022.905370,
38. https://doi.org/10.1093/ecco-jcc/jjz206,
39. https://doi.org/10.1038/s41577-023-00877-7,
40. https://doi.org/10.3390/fishes8050245,
41. https://doi.org/10.1038/s41375-025-02569-8,
42. https://doi.org/10.1093/molbev/msab272,