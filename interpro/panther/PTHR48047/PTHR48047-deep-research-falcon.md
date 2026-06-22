---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-21T22:24:29.822670'
end_time: '2026-06-21T22:37:10.710955'
duration_seconds: 760.89
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR48047
  interpro_name: UDP-glycosyltransferase
  interpro_short_name: UDP-glycosyltransferase
  interpro_type: family
  interpro_integrated: None (top-level entry)
  member_databases: Not specified
  n_proteins: '16213'
  n_taxa: '1627'
  n_subfamilies: '133'
  interpro2go_terms: None mapped (no InterPro2GO terms for this entry)
  interpro_description: The UDP-glycosyltransferase family is involved in the modification
    of a wide range of substrates through the transfer of sugar moieties from activated
    nucleotide sugars to acceptor molecules, which include flavonoids, hormones, and
    various secondary metabolites. Members of the family exhibit specificity for different
    substrates and positions on those substrates, contributing to the diversity of
    glycosylated products. These modifications often alter the solubility, stability,
    and biological activity of the compounds, playing crucial roles in plant metabolism,
    including defense mechanisms, stress responses, and developmental processes. Some
    members are also implicated in the detoxification of xenobiotics and the biosynthesis
    of bioactive compounds with medicinal properties.
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 14
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: PTHR48047-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR48047-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: PTHR48047-deep-research-falcon_artifacts/artifact-02.md
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
- **Accession:** PTHR48047
- **Name:** UDP-glycosyltransferase
- **Short name:** UDP-glycosyltransferase
- **Entry type:** family
- **Integrated into / parent:** None (top-level entry)
- **Member database signatures:** Not specified
- **Scale:** 16213 proteins across 1627 taxa, 133 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** The UDP-glycosyltransferase family is involved in the modification of a wide range of substrates through the transfer of sugar moieties from activated nucleotide sugars to acceptor molecules, which include flavonoids, hormones, and various secondary metabolites. Members of the family exhibit specificity for different substrates and positions on those substrates, contributing to the diversity of glycosylated products. These modifications often alter the solubility, stability, and biological activity of the compounds, playing crucial roles in plant metabolism, including defense mechanisms, stress responses, and developmental processes. Some members are also implicated in the detoxification of xenobiotics and the biosynthesis of bioactive compounds with medicinal properties.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR48047 (UDP-glycosyltransferase)**, structured to support GO annotation review.

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
- **Accession:** PTHR48047
- **Name:** UDP-glycosyltransferase
- **Short name:** UDP-glycosyltransferase
- **Entry type:** family
- **Integrated into / parent:** None (top-level entry)
- **Member database signatures:** Not specified
- **Scale:** 16213 proteins across 1627 taxa, 133 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** The UDP-glycosyltransferase family is involved in the modification of a wide range of substrates through the transfer of sugar moieties from activated nucleotide sugars to acceptor molecules, which include flavonoids, hormones, and various secondary metabolites. Members of the family exhibit specificity for different substrates and positions on those substrates, contributing to the diversity of glycosylated products. These modifications often alter the solubility, stability, and biological activity of the compounds, playing crucial roles in plant metabolism, including defense mechanisms, stress responses, and developmental processes. Some members are also implicated in the detoxification of xenobiotics and the biosynthesis of bioactive compounds with medicinal properties.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR48047 (UDP-glycosyltransferase)**, structured to support GO annotation review.

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


# Comprehensive Research Report: InterPro Entry PTHR48047 (UDP-glycosyltransferase Family) for GO Annotation Review

## Executive Summary

InterPro entry **PTHR48047** represents a large, ancient, and highly divergent family of UDP-glycosyltransferases (UGTs) spanning 16,213 proteins across 1,627 taxa and 133 subfamilies. This report evaluates the appropriateness of Gene Ontology (GO) term mappings for this family-level signature. The evidence demonstrates that while the family shares conserved structural features (GT-B fold, PSPG motif, catalytic machinery), it exhibits **extreme functional divergence** in donor sugar specificity, acceptor substrate range, regiospecificity, and biological processes. The current absence of InterPro2GO mappings is **correct and should be maintained**, as any specific molecular function or biological process term would systematically over-annotate proteins bearing this signature.

---

## 1. Family Definition and Biochemistry

### 1.1 Structural Architecture

UDP-glycosyltransferases in the PTHR48047 family adopt a canonical **GT-B fold** comprising two Rossmann-like domains connected by a linker and forming a central cleft (gharabli2024thesugardonor pages 3-4, lethe2024similaritiesinstructure pages 1-4, speeckaert2022ugt72amajor pages 2-5). The N-terminal domain primarily recognizes the acceptor substrate, while the C-terminal domain binds the UDP-sugar donor (gharabli2024thesugardonor pages 3-4, speeckaert2022ugt72amajor pages 2-5). Plant members are typically soluble cytoplasmic enzymes, whereas animal homologs (e.g., human UGT1A and UGT2B families) are membrane-bound endoplasmic reticulum proteins (lethe2024similaritiesinstructure pages 4-5).

| Feature category | Family-level summary for PTHR48047 (UDP-glycosyltransferase) | Evidence / notes | Citation |
|---|---|---|---|
| Overall enzyme class | UDP-glycosyltransferases transfer a sugar moiety from an activated UDP-sugar donor to a chemically diverse acceptor molecule, producing glycosides. | Family members glycosylate low-molecular-weight compounds including flavonoids, triterpenes, phenolics, hormones, steroids, and xenobiotics, but exact substrates vary strongly by subfamily and taxon. | (gharabli2024thesugardonor pages 1-3, lethe2024similaritiesinstructure pages 1-4, lethe2024similaritiesinstructure pages 5-7) |
| Structural fold | Canonical **GT-B fold** with **two Rossmann-like domains** connected by a linker and forming a central cleft. | The N-terminal domain is primarily associated with acceptor recognition; the C-terminal domain is primarily associated with donor (UDP-sugar) recognition. | (gharabli2024thesugardonor pages 3-4, lethe2024similaritiesinstructure pages 1-4, speeckaert2022ugt72amajor pages 2-5) |
| Conserved donor-binding motif | Plant members contain the **PSPG (Plant Secondary Product Glycosyltransferase) motif**, a highly conserved **44-residue** signature in the C-terminal domain. | The motif is widely used to identify plant UGTs; it is a major determinant of UDP-sugar binding, especially the UDP moiety. | (gharabli2024thesugardonor pages 3-4, lethe2024similaritiesinstructure pages 1-4, speeckaert2022ugt72amajor pages 2-5) |
| PSPG motif architecture | The PSPG motif typically begins with **Trp** and ends with an **acidic residue followed by Gln/His/Asn**; several positions are strongly conserved. | Conserved positions reported include 4, 8, 19, 21, 24, 27, and 39; most contact the UDP portion, whereas positions near the motif end can influence sugar specificity. | (gharabli2024thesugardonor pages 3-4) |
| Donor recognition determinants | Donor binding is centered in the C-terminal domain and depends on the PSPG motif plus additional residues outside the motif. | Residues outside the PSPG motif, including N-terminal loop residues, can strongly alter specificity for UDP-Glc, UDP-Gal, UDP-Rha, UDP-Xyl, or UDP-GlcA. | (gharabli2024thesugardonor pages 3-4, lethe2024similaritiesinstructure pages 4-5, gharabli2024thesugardonor pages 4-6) |
| Acceptor-binding region | The acceptor-binding site is more variable than the donor-binding site and is mainly formed by N-terminal residues. | This region explains the family’s broad acceptor diversity and poor prediction of exact substrate specificity from sequence alone. | (speeckaert2022ugt72amajor pages 2-5, lethe2024similaritiesinstructure pages 5-7) |
| Conserved catalytic residues | A **His-Asp catalytic dyad** is the common mechanistic core in many family 1 UGTs. | The catalytic histidine acts as a general base; the aspartate helps stabilize/organize the active site and supports catalysis. Example residues discussed include His-22/Asp-121 in UGT71G1 and analogous positions in other UGTs. | (gharabli2024thesugardonor pages 1-3, lethe2024similaritiesinstructure pages 4-5, speeckaert2022ugt72amajor pages 2-5) |
| Core catalytic mechanism | Glycosyl transfer generally proceeds by an **SN2-like inverting mechanism**. | In O-glycosylation, the catalytic His-Asp system deprotonates the acceptor hydroxyl, enabling nucleophilic attack on the anomeric carbon of the UDP-sugar with inversion of configuration. | (gharabli2024thesugardonor pages 1-3) |
| Reaction chemistry diversity | Family members can catalyze **O-, N-, S-, and in some cases C-glycosylation**. | Despite shared fold/mechanistic logic, bond type and regiospecificity vary across subfamilies. | (gharabli2024thesugardonor pages 1-3, lethe2024similaritiesinstructure pages 1-4) |
| Distinguishing biochemical hallmark | Combination of **GT-B fold + C-terminal UDP-sugar-recognition motif + catalytic His-centered inverting chemistry** distinguishes this family from many other GTs. | The family is unified structurally and mechanistically, but not by a single substrate or biological process. | (gharabli2024thesugardonor pages 3-4, speeckaert2022ugt72amajor pages 2-5, lethe2024similaritiesinstructure pages 5-7) |
| Family-level limitation for annotation | Structural conservation does **not** imply functional uniformity at the substrate level. | Closely related UGTs can differ in donor sugar, acceptor substrate, and glycosylation position; single substitutions can switch specificity. | (gharabli2024thesugardonor pages 3-4, speeckaert2022ugt72amajor pages 2-5, gharabli2024thesugardonor pages 4-6, speeckaert2022ugt72amajor pages 8-9) |


*Table: This table summarizes the core structural and biochemical properties of the PTHR48047 UDP-glycosyltransferase family. It highlights the conserved GT-B fold, PSPG donor-binding motif, catalytic His-Asp dyad, and inverting SN2-like mechanism while noting the family’s major substrate-level diversity.*

### 1.2 The PSPG Motif

A hallmark of plant UGTs is the **Plant Secondary Product Glycosyltransferase (PSPG) motif**, a highly conserved 44-residue signature in the C-terminal domain (gharabli2024thesugardonor pages 3-4, lethe2024similaritiesinstructure pages 1-4, speeckaert2022ugt72amajor pages 2-5). The PSPG motif begins with tryptophan and ends with an acidic residue followed by Gln/His/Asn, with conserved positions at residues 4, 8, 19, 21, 24, 27, and 39 (gharabli2024thesugardonor pages 3-4). Most conserved positions interact with the UDP moiety; terminal residues influence sugar specificity (gharabli2024thesugardonor pages 3-4).

Despite its conservation, the PSPG motif alone does not dictate donor sugar preference. Studies show that residues **outside** the PSPG motif—including N-terminal loop positions—can switch donor specificity between UDP-Glc, UDP-Gal, UDP-Rha, UDP-Xyl, and UDP-GlcA through single amino acid substitutions (gharabli2024thesugardonor pages 3-4, lethe2024similaritiesinstructure pages 4-5, gharabli2024thesugardonor pages 4-6). For example, loop positions LP1 and LP2 near the donor sugar C6 region determine rhamnosyltransferase versus glucosyltransferase activity, and reciprocal mutations between related enzymes from *Viola tricolor* (VtCGTa and VtCGTc) switch donor preference (gharabli2024thesugardonor pages 4-6).

### 1.3 Catalytic Mechanism and Conserved Residues

The catalytic core consists of a **His-Asp dyad** (gharabli2024thesugardonor pages 1-3, lethe2024similaritiesinstructure pages 4-5, speeckaert2022ugt72amajor pages 2-5). The histidine residue (e.g., His-22 in UGT71G1; His-39 in human UGT1A1) acts as a general base, deprotonating the acceptor hydroxyl group; the aspartate (e.g., Asp-121 in UGT71G1) stabilizes the active site (lethe2024similaritiesinstructure pages 4-5). Glycosyl transfer proceeds via an **SN2-like inverting mechanism**: the deprotonated acceptor nucleophile attacks the anomeric carbon (C1′) of the UDP-sugar from the opposite face, inverting the stereochemistry of the glycosidic bond (gharabli2024thesugardonor pages 1-3). Family members can catalyze O-, N-, S-, and in some cases C-glycosylation, though O-glycosylation is most common (gharabli2024thesugardonor pages 1-3, lethe2024similaritiesinstructure pages 1-4).

**Key experimental evidence:** X-ray crystal structures of plant UGTs (UGT71G1, PDB 2ACW; UGT72B1; UGT89C1; and others in Table 1 of Gharabli & Welner 2024) confirm UDP-sugar binding modes and catalytic geometry (gharabli2024thesugardonor pages 1-3, gharabli2024thesugardonor pages 3-4). Mutagenesis of the catalytic histidine or conserved donor-recognition residues abolishes or severely impairs activity, confirming their mechanistic centrality (gharabli2024thesugardonor pages 3-4, lethe2024similaritiesinstructure pages 4-5).

---

## 2. InterPro2GO Mapping Appropriateness

### 2.1 Current Mapping Status

InterPro entry **PTHR48047** currently has **no GO terms mapped** via InterPro2GO. This section evaluates whether specific GO terms would be appropriate for the family.

### 2.2 Potential Molecular Function Terms

Candidate GO terms that might be considered include:

- **GO:0016757** (*transferase activity, transferring glycosyl groups*): This is the only term mechanistically true for all family members. However, it is **too generic** to be informative and would add no value beyond what is already evident from the family name.
  
- **Specific donor-based terms** (e.g., *UDP-glucose:acceptor glucosyltransferase activity*, GO:0035251; *UDP-glucuronosyltransferase activity*, GO:0015020): These terms are **not universally applicable** because the family includes enzymes preferring UDP-Glc (most plant UGTs), UDP-GlcA (most animal UGTs), UDP-Gal, UDP-Rha, UDP-Xyl, and combinations thereof (gharabli2024thesugardonor pages 3-4, lethe2024similaritiesinstructure pages 4-5, lethe2024similaritiesinstructure pages 7-9, gharabli2024thesugardonor pages 4-6).

- **Acceptor-based terms** (e.g., *quercetin 3-O-glucosyltransferase activity*, GO:0080043; *flavonoid 7-O-glucosyltransferase activity*, GO:0047893; *steroid glucosyltransferase activity*, GO:0035252): These are subfamily-specific. UGT72 members glycosylate flavonoids and monolignols; human UGT1A1 glycosylates bilirubin and steroids; bacterial UGTs participate in cell-wall biosynthesis (majeed2024glycosyltransferasesunravelingmolecular pages 1-2, majeed2024glycosyltransferasesunravelingmolecular pages 2-4, lethe2024similaritiesinstructure pages 7-9, lethe2024similaritiesinstructure pages 9-11, speeckaert2022ugt72amajor pages 8-9). Mapping any acceptor-specific term to the whole family would **massively over-annotate** unrelated subfamilies.

**Verdict:** No donor- or acceptor-specific molecular function term is appropriate for this family-level entry.

### 2.3 Potential Biological Process Terms

Candidate process terms might include:

- **Generic terms** (e.g., *metabolic process*, GO:0008152): These are too broad to be useful.
  
- **Specialized metabolism terms** (e.g., *flavonoid biosynthetic process*, GO:0009813; *lignin biosynthetic process*, GO:0009809; *xenobiotic metabolic process*, GO:0006805; *steroid metabolic process*, GO:0008202): Each is true for only a **subset** of the family. Plant UGT72 members participate in monolignol glycosylation related to lignification and flavonoid homeostasis (speeckaert2022ugt72amajor pages 2-5, speeckaert2022ugt72amajor pages 1-2, speeckaert2022ugt72amajor pages 8-9). Human UGT1A/2B members detoxify xenobiotics and regulate steroid levels (lethe2024similaritiesinstructure pages 7-9, lethe2024similaritiesinstructure pages 9-11). Bacterial UGTs contribute to cell-wall biosynthesis and virulence (majeed2024glycosyltransferasesunravelingmolecular pages 1-2, majeed2024glycosyltransferasesunravelingmolecular pages 2-4). Mapping any of these process terms to the entire family would leak into taxa or subfamilies where the pathway is absent or irrelevant.

**Verdict:** No specific biological process term is appropriate for this family-level entry.

### 2.4 Cellular Component Terms

Plant UGTs are cytosolic; animal UGTs are ER-membrane-bound (lethe2024similaritiesinstructure pages 1-4, lethe2024similaritiesinstructure pages 4-5). Bacterial and archaeal homologs have yet other localizations (majeed2024glycosyltransferasesunravelingmolecular pages 1-2). No single component term holds across 1,627 taxa.

**Verdict:** No cellular component term is appropriate.

---

## 3. Functional Divergence Across the Family

The UDP-glycosyltransferase family exhibits **profound functional diversification** that precludes uniform GO annotation.

| Example UGT / group | Taxon / context | UDP-sugar donor(s) reported | Acceptor substrate class(es) | Regiospecificity / bond pattern | Evidence for divergence or specificity switching | Citation |
|---|---|---|---|---|---|---|
| UGT71G1 | Plant (Medicago truncatula) | UDP-Glc preferred | Flavonoids; triterpenes (medicagenic acid) | Produces multiple quercetin glycosides, with quercetin-3-O-glucoside the major product; also glycosylates triterpene aglycones | Same enzyme can act on chemically distinct acceptors; illustrates broad acceptor promiscuity within one subfamily member | (lethe2024similaritiesinstructure pages 1-4, lethe2024similaritiesinstructure pages 7-9) |
| UGT72 family | Plants | Mostly UDP-Glc; some members/subfamily examples also use UDP-Gal or UDP-Xyl | Monolignols, monolignol precursors/derivatives, flavonoids, xenobiotics | Monolignols often glycosylated at C4; flavonoid glycosylation varies by enzyme: 3-O, 7-O, 3'-O, or multisite 3/7/4' | Strong subfamily divergence despite family relationship; sequence does not reliably predict exact substrate class or regioselectivity | (speeckaert2022ugt72amajor pages 2-5, speeckaert2022ugt72amajor pages 8-9) |
| UGT72B1 | Plant (Arabidopsis thaliana) | UDP-Glc; also reported with UDP-5-thioglucose | Monolignols, phenolics, xenobiotics | Glycosylates diverse acceptors including coniferyl alcohol, p-coumaryl alcohol, vanillin, chlorophenols/anilines | Demonstrates expansion from endogenous phenylpropanoids to xenobiotic detoxification within one family branch | (speeckaert2022ugt72amajor pages 8-9) |
| UGT72B3 | Plant (Arabidopsis thaliana) | UDP-Glc, UDP-Gal, UDP-Xyl | Flavonoids; aldehyde phenylpropanoids; xenobiotics | Glycosylates quercetin, fisetin, kaempferol, coniferaldehyde, sinapaldehyde | Same enzyme lineage can differ from nearby homologs in both donor usage and acceptor class, arguing against one family-wide GO function | (speeckaert2022ugt72amajor pages 8-9) |
| UGT72E1 / UGT72E2 / UGT72E3 | Plant (Arabidopsis thaliana) | UDP-Glc | Hydroxycinnamates, aldehydes, monolignol alcohols | 4-O glycosylation reported for coniferaldehyde and related monolignol-pathway substrates | Closely related enzymes split substrate ranges across coniferaldehyde, sinapaldehyde, ferulic acid, sinapic acid, caffeic acid, coniferyl alcohol, sinapyl alcohol | (speeckaert2022ugt72amajor pages 8-9) |
| UGT89C1 | Plant rhamnosyltransferase | UDP-Rha | Flavonoid-type acceptors in cited donor-specificity studies | Donor specificity linked to loop residues near donor C6 region | LP1/LP2 substitutions toward glucosyltransferase-like residues abolish or reduce rhamnosyltransferase activity, showing single-residue control of donor preference | (gharabli2024thesugardonor pages 3-4, gharabli2024thesugardonor pages 4-6) |
| VtCGTa vs VtCGTc | Plant (Viola tricolor) | VtCGTa: UDP-Glc/UDP-Xyl/UDP-Gal; VtCGTc: UDP-Glc/UDP-Xyl/UDP-Rha/UDP-Ara | Flavonoids / CGT acceptors in donor-specificity study | Different donor usage despite related enzymes | LP1 mutation in VtCGTa (Thr→Pro/Val-like states) can enable UDP-Rha activity; reciprocal mutation in VtCGTc (Val→Thr) reduces UDP-Rha and establishes UDP-Glc activity | (gharabli2024thesugardonor pages 4-6) |
| UGT89A2 allelic variants / Ib3GGT / At3GGT / CsGT2 / UGT74AN3 / UGT73F4 / UGT73F2 / UGT78W1 / UGT76D1 / AsAAT1 | Multiple plant lineages | Different examples across UDP-Glc, UDP-Xyl, UDP-Gal, UDP-Ara, UDP-Rha | Various specialized metabolites | Donor preference can change without changing general GT-B scaffold | Tabled mutagenesis evidence shows single or few amino-acid substitutions switch donor preference among UDP-Glc, UDP-Xyl, UDP-Gal, UDP-Rha, or mixed specificity | (gharabli2024thesugardonor pages 4-6) |
| UGT71G1 donor-site residues | Plant | UDP-Glc | Flavonoids / triterpenes | Donor selectivity influenced by consensus-sequence residues such as terminal Gln and other donor-contacting positions | Residues Asn-361, Trp-360, Glu-381, Gln-382 recognize glucose moiety; changing analogous positions in related enzymes alters donor preference | (lethe2024similaritiesinstructure pages 4-5, gharabli2024thesugardonor pages 3-4) |
| UGT73P12-like glucuronosyltransferase logic | Plant structural comparison | UDP-GlcA favored via Arg-mediated recognition | Specialized metabolites | Donor discrimination tied to 6' substituent recognition | Replacement of the glucose-recognizing Thr position by Arg supports UDP-GlcA recognition, showing mechanistic divergence toward glucuronosylation | (lethe2024similaritiesinstructure pages 4-5) |
| Human UGT1A1 | Animal (human) | UDP-GlcA | Bilirubin, drugs, xenobiotics, some phytoestrogens | Bilirubin mono- and diglucuronidation | Animal homologs retain overall UGT architecture but use a different dominant donor and distinct physiological substrates from plant homologs | (lethe2024similaritiesinstructure pages 1-4, lethe2024similaritiesinstructure pages 7-9, lethe2024similaritiesinstructure pages 9-11) |
| Human UGT1A/UGT2B isoforms | Animal (human) | UDP-GlcA | Steroids, estrogens, androgens, phenolic drugs, bisphenol A, morphine, acetaminophen | Isoform-dependent glucuronidation positions on steroids; overlapping but nonidentical activities | Demonstrates large functional spread within animal UGTs: bilirubin specialist (UGT1A1), estrogen-active isoforms (UGT1A1/1A3/1A8/1A9/2B7), androgen-active isoforms (UGT2B15/2B17), xenobiotic-active isoforms | (lethe2024similaritiesinstructure pages 7-9, lethe2024similaritiesinstructure pages 9-11) |
| Family-wide conclusion | Plants, animals, algae and broader taxa | UDP-Glc, UDP-Gal, UDP-Rha, UDP-Xyl, UDP-GlcA all represented in the evidence set | Flavonoids, monolignols, hormones/phytohormones, steroids, triterpenes, xenobiotics | 3-O, 7-O, 3'-O, 4'-O, multisite and glucuronidation patterns all occur | The same GT-B scaffold supports extensive donor, acceptor, and regiospecific divergence; therefore a single specific catalytic GO term would over-annotate this family-level InterPro entry | (gharabli2024thesugardonor pages 3-4, speeckaert2022ugt72amajor pages 2-5, lethe2024similaritiesinstructure pages 7-9, gharabli2024thesugardonor pages 4-6, speeckaert2022ugt72amajor pages 8-9) |


*Table: This table summarizes experimentally supported donor, acceptor, and regiospecific diversity across UDP-glycosyltransferases, including examples where a few residue changes switch specificity. It is useful for showing why broad family-level GO annotation would overgeneralize across this InterPro family.*

### 3.1 Donor Sugar Specificity

Experimental evidence documents divergent donor preferences:

- **UDP-Glc**: The dominant donor in plant UGTs (e.g., UGT71G1, UGT72B1, most plant enzymes) (gharabli2024thesugardonor pages 3-4, lethe2024similaritiesinstructure pages 1-4, speeckaert2022ugt72amajor pages 1-2, lethe2024similaritiesinstructure pages 5-7).
- **UDP-GlcA**: The dominant donor in animal UGTs (human UGT1A1, UGT2B families) (lethe2024similaritiesinstructure pages 1-4, lethe2024similaritiesinstructure pages 7-9, lethe2024similaritiesinstructure pages 9-11).
- **UDP-Gal, UDP-Rha, UDP-Xyl**: Used by specific plant subfamilies; single mutations can switch between these donors (gharabli2024thesugardonor pages 3-4, gharabli2024thesugardonor pages 4-6).
  
For instance, mutagenesis of loop residues LP1 and LP2 converts rhamnosyltransferases to glucosyltransferases and vice versa (gharabli2024thesugardonor pages 4-6). In the *Viola tricolor* enzymes VtCGTa and VtCGTc, a single Thr→Pro substitution at LP1 enabled UDP-Rha activity in a UDP-Glc-preferring enzyme (gharabli2024thesugardonor pages 4-6).

### 3.2 Acceptor Substrate Diversity

Family members glycosylate chemically diverse acceptors:

- **Flavonoids** (quercetin, kaempferol, myricetin): Many plant UGTs, including UGT71G1 and UGT72 family members (lethe2024similaritiesinstructure pages 1-4, speeckaert2022ugt72amajor pages 2-5, lethe2024similaritiesinstructure pages 7-9, speeckaert2022ugt72amajor pages 8-9).
- **Monolignols and derivatives** (coniferyl alcohol, sinapyl alcohol, ferulic acid): Plant UGT72E and UGT72B subfamilies (speeckaert2022ugt72amajor pages 8-9).
- **Triterpenes**: UGT71G1 glycosylates medicagenic acid in *Medicago truncatula* (lethe2024similaritiesinstructure pages 7-9).
- **Steroids and hormones**: Human UGT1A1, 1A3, 2B15, 2B17 glucuronidate estrogens, androgens, and other steroids (lethe2024similaritiesinstructure pages 7-9, lethe2024similaritiesinstructure pages 9-11).
- **Bilirubin**: Human UGT1A1 is the only significant bilirubin glucuronosyltransferase (lethe2024similaritiesinstructure pages 7-9, lethe2024similaritiesinstructure pages 9-11).
- **Xenobiotics**: Morphine, acetaminophen, bisphenol A, chlorophenols, herbicides, and other synthetic compounds (lethe2024similaritiesinstructure pages 7-9, lethe2024similaritiesinstructure pages 9-11, speeckaert2022ugt72amajor pages 8-9).

Even closely related UGTs can differ in acceptor specificity. For example, within the Arabidopsis UGT72 family, UGT72B1 glycosylates monolignols and xenobiotics, while UGT72E2 additionally accepts coumaric acid derivatives (speeckaert2022ugt72amajor pages 8-9).

### 3.3 Regiospecificity

UGTs glycosylate different positions on the same acceptor class:

- Flavonoids: 3-O-glycosides, 7-O-glycosides, 3′-O-glycosides, 4′-O-glycosides, or multisite 3/7/4′-glycosylation (speeckaert2022ugt72amajor pages 8-9).
- Monolignols: Predominantly 4-O-glycosylation (speeckaert2022ugt72amajor pages 8-9).
- Steroids: Position-dependent glucuronidation by different UGT isoforms (lethe2024similaritiesinstructure pages 7-9).

### 3.4 No Evidence for Catalytically Dead Pseudoenzymes

The literature reviewed did not identify catalytically inactive "pseudo-UGT" members that retain the fold but lack glycosyltransferase activity. Mutagenesis of critical catalytic residues (e.g., His→Ala) abolishes activity experimentally, but naturally occurring pseudogenes or decoy proteins were not reported in the reviewed sources.

---

## 4. Taxonomic Scope

| Kingdom / major clade | Representative taxa or groups | Reported UGT abundance / copy number | Dominant donor preference or biochemical tendency | GO-review relevance | Citation |
|---|---|---:|---|---|---|
| Green algae | *Chlamydomonas reinhardtii* | 5 UGTs reported | PSPG-like sequences are divergent from angiosperm consensus; likely non-uniform donor preferences | Earliest-diverging plant-lineage examples already show sequence divergence, arguing against a single family-wide specific GO term | (speeckaert2022ugt72amajor pages 2-5, speeckaert2022ugt72amajor pages 5-8) |
| Liverworts | *Marchantia polymorpha*; functional UGTs from *Marchantia emarginata*, *M. paleacea*, *Plagiochasma appendiculatum* | 41 UGTs in *M. polymorpha* | Flavonoid glycosylation is experimentally described; mainly glucoside formation in cited examples | Shows ancestral plant expansion and early specialization in flavonoid glycosylation rather than one universal substrate/process | (speeckaert2022ugt72amajor pages 2-5, speeckaert2022ugt72amajor pages 5-8) |
| Bryophytes | *Physcomitrella patens* | 30 UGTs | Not detailed here at substrate level | Copy-number expansion beyond algae indicates diversification before vascular plants | (speeckaert2022ugt72amajor pages 2-5) |
| Lycophytes | *Selaginella moellendorffii* | 137 UGTs | Not detailed here at substrate level | Large expansion indicates increasing specialization across land-plant evolution | (speeckaert2022ugt72amajor pages 2-5) |
| Gymnosperms | *Ginkgo biloba*; *Pinus taeda* | 129 (*Ginkgo*), 243 (*Pinus*) | Not detailed here at substrate level | High copy numbers suggest broad neo/subfunctionalization, inconsistent with narrow family-wide GO mapping | (speeckaert2022ugt72amajor pages 2-5) |
| Angiosperms, dicots | *Arabidopsis thaliana*; *Solanum lycopersicum*; *Populus trichocarpa* | 123 (*Arabidopsis*), 162 (*tomato*), 281 (*poplar*) | Plant UGTs most often use UDP-glucose; many glycosylate flavonoids, monolignols, hormones, and xenobiotics | Strong lineage-specific expansion and broad substrate range make specific family-level GO terms unsafe | (gharabli2024thesugardonor pages 3-4, speeckaert2022ugt72amajor pages 2-5, speeckaert2022ugt72amajor pages 1-2, lethe2024similaritiesinstructure pages 5-7, speeckaert2022ugt72amajor pages 8-9) |
| Angiosperms, monocots | *Oryza sativa* | 184 UGTs | Plant UGTs generally prefer UDP-glucose, but donor switching to UDP-Gal, UDP-Rha, UDP-Xyl, or UDP-GlcA occurs in specific enzymes | Even within flowering plants, donor preference is not uniform enough for a specific catalytic GO term at family level | (gharabli2024thesugardonor pages 3-4, speeckaert2022ugt72amajor pages 2-5, speeckaert2022ugt72amajor pages 1-2, gharabli2024thesugardonor pages 4-6) |
| Plants overall | Land plants broadly | UGTs are the largest GT superfamily in plants; ~25% of GT genes in *Arabidopsis* and ~35% in rice belong to UGTs | Usually UDP-glucose donors; acceptors include flavonoids, phenylpropanoids, terpenoids, phytohormones, and xenobiotics | Plant-side evidence alone shows extensive donor/acceptor/regiospecific divergence | (speeckaert2022ugt72amajor pages 1-2) |
| Animals / mammals | Humans and other mammals | Human nomenclature includes UGT families 1 and 2; one review notes four human UGT families encoding ~200 genes, while another distinguishes family numbering 1-2 for humans | Human UGTs predominantly use UDP-glucuronic acid rather than UDP-glucose; major roles in glucuronidation of bilirubin, steroids, drugs, xenobiotics | Major donor shift relative to plants means plant-specific GO terms would leak badly across taxa | (lethe2024similaritiesinstructure pages 1-4, lethe2024similaritiesinstructure pages 7-9, lethe2024similaritiesinstructure pages 5-7, lethe2024similaritiesinstructure pages 9-11) |
| Humans specifically | UGT1A/UGT2B-centered examples | Exact per-gene count varies by source; UGT1A and UGT2B subfamilies emphasized | Bilirubin, steroid, morphine, acetaminophen, BPA, and phytoestrogen glucuronidation; membrane-bound ER-associated enzymes | Animal homologs differ in cellular context, donor preference, and physiological role from plant soluble UGTs | (lethe2024similaritiesinstructure pages 4-5, lethe2024similaritiesinstructure pages 7-9, lethe2024similaritiesinstructure pages 5-7, lethe2024similaritiesinstructure pages 9-11) |
| Bacteria | Broadly distributed bacterial GTs/UGTs | Present across bacteria; no single genome copy number extracted here | Bacterial GTs participate in cell wall, surface glycosylation, and virulence-associated chemistry | Functional roles differ strongly from plant specialized-metabolism UGTs, reinforcing family heterogeneity across taxa | (majeed2024glycosyltransferasesunravelingmolecular pages 1-2, majeed2024glycosyltransferasesunravelingmolecular pages 2-4) |
| Fungi | Broadly distributed fungal homologs; fungal UGT families noted near algal sterol-related enzymes | Present; no single genome copy number extracted here | Some homologs are linked to sterol β-glucosyltransferase or related activities | Fungal-related branches imply additional biochemical diversity beyond plant/animal paradigms | (speeckaert2022ugt72amajor pages 5-8) |
| Archaea | Hyperthermophilic archaeal CAZyme repertoires | GTs present in archaeal genomes; no specific UGT copy number extracted here | GTs are recognized components of archaeal CAZyme complements | Presence outside eukaryotes supports deep evolutionary breadth and cautions against process-specific annotation | (majeed2024glycosyltransferasesunravelingmolecular pages 1-2) |
| Viruses / other eukaryotes | Viruses and amoebae noted in phylogenetic overview | Presence reported qualitatively | Not detailed here | Indicates the broader UGT homolog landscape extends beyond classic plant/animal systems | (lethe2024similaritiesinstructure pages 4-5) |
| InterPro entry scope | PTHR48047 | 16,213 proteins across 1,627 taxa, 133 subfamilies | Family-wide commonality is only broad UDP-sugar-dependent glycosyl transfer, not one substrate/process | Taxonomic breadth plus biochemical divergence supports keeping no specific InterPro2GO mapping at this top-level family | (lethe2024similaritiesinstructure pages 1-4, speeckaert2022ugt72amajor pages 2-5, lethe2024similaritiesinstructure pages 5-7) |


*Table: This table summarizes the phylogenetic breadth of UDP-glycosyltransferases and the large variation in copy number and donor preference across major clades. It is useful for GO review because it shows that PTHR48047 spans deeply divergent taxa and cannot safely support narrow family-level functional annotations.*

The UDP-glycosyltransferase family is **ancient and pan-domain**:

- **Green algae**: *Chlamydomonas reinhardtii* encodes 5 UGTs with divergent PSPG motifs (speeckaert2022ugt72amajor pages 2-5, speeckaert2022ugt72amajor pages 5-8).
- **Liverworts**: *Marchantia polymorpha* has 41 UGTs; functionally characterized liverwort UGTs glycosylate flavonoids (speeckaert2022ugt72amajor pages 2-5, speeckaert2022ugt72amajor pages 5-8).
- **Vascular plants**: Angiosperms encode 123–281 UGTs per genome (*Arabidopsis thaliana*: 123; *Populus trichocarpa*: 281; *Oryza sativa*: 184) (speeckaert2022ugt72amajor pages 2-5, speeckaert2022ugt72amajor pages 1-2).
- **Animals**: Humans have UGT families 1 and 2, with distinct subfamilies for bilirubin, steroid, and xenobiotic metabolism (lethe2024similaritiesinstructure pages 1-4, lethe2024similaritiesinstructure pages 4-5, lethe2024similaritiesinstructure pages 7-9, lethe2024similaritiesinstructure pages 9-11).
- **Bacteria, fungi, archaea**: UGTs participate in cell-wall biosynthesis, surface glycosylation, and other processes (majeed2024glycosyltransferasesunravelingmolecular pages 1-2, majeed2024glycosyltransferasesunravelingmolecular pages 2-4, speeckaert2022ugt72amajor pages 5-8).

**Cross-kingdom divergence in donor preference:** Plant UGTs predominantly use UDP-Glc; animal UGTs predominantly use UDP-GlcA (gharabli2024thesugardonor pages 3-4, lethe2024similaritiesinstructure pages 1-4, lethe2024similaritiesinstructure pages 7-9, lethe2024similaritiesinstructure pages 5-7, lethe2024similaritiesinstructure pages 9-11). This fundamental biochemical difference means any plant-biased GO term (e.g., *flavonoid glucosyltransferase activity*) would mis-annotate animal proteins, and any animal-biased term (e.g., *glucuronosyltransferase activity*) would mis-annotate plant proteins.

**PTHR48047 scope:** Spanning 1,627 taxa and 133 subfamilies, this entry encompasses enormous phylogenetic and functional breadth. No single biological process or molecular function term holds across this scope.

---

## 5. Over-Annotation Verdict and Recommendations

### 5.1 Summary

The PTHR48047 UDP-glycosyltransferase family is unified by:

1. **Conserved GT-B fold** with two Rossmann domains.
2. **Conserved PSPG motif** (in plants) or analogous donor-recognition machinery.
3. **Conserved His-Asp catalytic dyad** mediating inverting SN2-like glycosyl transfer.

However, the family is **functionally heterogeneous**:

1. **Different UDP-sugar donors** across subfamilies and taxa.
2. **Different acceptor substrates** (flavonoids, monolignols, hormones, steroids, xenobiotics, etc.).
3. **Different regiospecificity** and biological processes.
4. **Single amino acid changes** can switch substrate specificity.

### 5.2 InterPro2GO Mapping Verdict

**The absence of GO term mappings for PTHR48047 is CORRECT.**

- **ACCEPT**: Maintain the current state of no InterPro2GO mappings for this family-level entry.
- **Rationale**: Any specific molecular function (e.g., *quercetin 3-O-glucosyltransferase activity*, *UDP-glucuronosyltransferase activity*) or biological process (e.g., *flavonoid biosynthetic process*, *xenobiotic metabolic process*) term would systematically **over-annotate** proteins from subfamilies or taxa where that function is absent.
- **Only appropriate term is too generic**: The sole universally true term, *transferase activity, transferring glycosyl groups* (GO:0016757), adds no information beyond the family name and is not useful for curation.

### 5.3 Recommended Action Pattern

- **For PTHR48047 (top-level family)**: **ACCEPT** the absence of GO mappings. Do not add any molecular function, biological process, or cellular component terms.
  
- **For subfamilies (if InterPro child entries exist)**: GO terms should be mapped at the **subfamily level** (e.g., individual PANTHER subfamilies within PTHR48047) where functional homogeneity can be demonstrated experimentally. For example:
  - A subfamily containing only plant flavonoid 3-O-glucosyltransferases might appropriately carry GO:0080043 (*quercetin 3-O-glucosyltransferase activity*).
  - A subfamily containing only mammalian bilirubin glucuronosyltransferases might carry GO:0015020 (*UDP-glucuronosyltransferase activity*) and GO:0006783 (*heme catabolic process*).

- **Recommendation for InterPro curators**: If PTHR48047 has 133 subfamilies as stated, InterPro should encourage mapping of GO terms to those child entries based on experimentally validated functional data, rather than propagating subfamily-specific annotations to the parent family.

### 5.4 InterPro Entry Type Consideration

PTHR48047 is listed as entry type **family**. Families are generally more amenable to whole-protein function annotations than domain or superfamily entries. However, in this case, the family is so large and functionally diverse that it behaves more like a superfamily in terms of GO annotation risk. The 133 subfamilies within PTHR48047 are the appropriate granularity for functional GO annotation.

---

## 6. Conclusions

The UDP-glycosyltransferase family (PTHR48047) is a textbook example of **structural conservation without functional uniformity**. While all members share the GT-B fold, PSPG-like donor-binding machinery, and inverting catalytic mechanism, they diverge extensively in:

- UDP-sugar donor specificity (UDP-Glc, UDP-GlcA, UDP-Gal, UDP-Rha, UDP-Xyl),
- Acceptor substrate range (flavonoids, monolignols, triterpenes, steroids, hormones, xenobiotics),
- Regiospecificity (3-O, 7-O, 3′-O, 4-O, etc.),
- Biological processes (specialized metabolism, detoxification, hormone regulation, cell-wall biosynthesis),
- Taxonomic context (plants, animals, bacteria, fungi, archaea).

**The current absence of InterPro2GO mappings for PTHR48047 is scientifically sound and should be maintained.** Functional GO annotations should be made at the subfamily level, where experimental evidence supports functional homogeneity. This approach prevents systematic over-annotation and ensures that GO terms accurately reflect the biology of the annotated genes.

---

## References

All citations are to context IDs from the evidence-gathering process:

- **pqac-00000000**: Gharabli & Welner, 2024, *Frontiers in Bioengineering and Biotechnology* (PSPG motif, catalytic mechanism, SN2 inversion)
- **pqac-00000001**: Gharabli & Welner, 2024, pages 3-4 (PSPG positions, donor specificity determinants)
- **pqac-00000002**: Lethe et al., 2024, *International Journal of Molecular Sciences* (GT-B fold, plant vs. human UGT comparison)
- **pqac-00000003**: Lethe et al., 2024, pages 4-5 (catalytic residues, glucuronosyltransferase logic)
- **pqac-00000004**: Speeckaert et al., 2022, *Biology* (UGT evolution, GT-B fold, PSPG architecture)
- **pqac-00000005**: Speeckaert et al., 2022, pages 1-2 (plant UGT abundance, phenylpropanoid pathway)
- **pqac-00000006**: Majeed et al., 2024, *Science Reviews – Biology* (bacterial GTs, structure review)
- **pqac-00000007**: Majeed et al., 2024, pages 2-4 (bacterial and insect GTs)
- **pqac-00000008**: Lethe et al., 2024, pages 7-9 (human UGT substrates, flavonoids, steroids)
- **pqac-00000009**: Lethe et al., 2024, pages 5-7 (acceptor binding, substrate diversity)
- **pqac-00000010**: Speeckaert et al., 2022, pages 5-8 (algal and liverwort UGTs, phylogeny)
- **pqac-00000011**: Gharabli & Welner, 2024, pages 4-6 (N5 loop, LP1/LP2 mutagenesis, donor switching)
- **pqac-00000012**: Lethe et al., 2024, pages 9-11 (UGT diseases, bilirubin, steroid regulation)
- **pqac-00000013**: Speeckaert et al., 2022, pages 8-9 (UGT72 substrate table, monolignol and flavonoid specificity)

Publication dates for the primary sources: Gharabli & Welner (2024), Lethe et al. (2024), Speeckaert et al. (2022), Majeed et al. (2024).

---

**Final Verdict:** The absence of InterPro2GO mappings for PTHR48047 is **scientifically correct** and should be **maintained**. GO annotations should be made at the subfamily level where functional homogeneity can be experimentally validated.

References

1. (gharabli2024thesugardonor pages 3-4): Hani Gharabli and Ditte Hededam Welner. The sugar donor specificity of plant family 1 glycosyltransferases. Frontiers in Bioengineering and Biotechnology, May 2024. URL: https://doi.org/10.3389/fbioe.2024.1396268, doi:10.3389/fbioe.2024.1396268. This article has 22 citations.

2. (lethe2024similaritiesinstructure pages 1-4): Mary Caroline L. Lethe, Vincent Paris, Xiaoqiang Wang, and Clement T. Y. Chan. Similarities in structure and function of udp-glycosyltransferase homologs from human and plants. International Journal of Molecular Sciences, 25:2782, Feb 2024. URL: https://doi.org/10.3390/ijms25052782, doi:10.3390/ijms25052782. This article has 9 citations.

3. (speeckaert2022ugt72amajor pages 2-5): Nathanaël Speeckaert, Mondher El Jaziri, Marie Baucher, and Marc Behr. Ugt72, a major glycosyltransferase family for flavonoid and monolignol homeostasis in plants. Biology, 11:441, Mar 2022. URL: https://doi.org/10.3390/biology11030441, doi:10.3390/biology11030441. This article has 44 citations.

4. (lethe2024similaritiesinstructure pages 4-5): Mary Caroline L. Lethe, Vincent Paris, Xiaoqiang Wang, and Clement T. Y. Chan. Similarities in structure and function of udp-glycosyltransferase homologs from human and plants. International Journal of Molecular Sciences, 25:2782, Feb 2024. URL: https://doi.org/10.3390/ijms25052782, doi:10.3390/ijms25052782. This article has 9 citations.

5. (gharabli2024thesugardonor pages 1-3): Hani Gharabli and Ditte Hededam Welner. The sugar donor specificity of plant family 1 glycosyltransferases. Frontiers in Bioengineering and Biotechnology, May 2024. URL: https://doi.org/10.3389/fbioe.2024.1396268, doi:10.3389/fbioe.2024.1396268. This article has 22 citations.

6. (lethe2024similaritiesinstructure pages 5-7): Mary Caroline L. Lethe, Vincent Paris, Xiaoqiang Wang, and Clement T. Y. Chan. Similarities in structure and function of udp-glycosyltransferase homologs from human and plants. International Journal of Molecular Sciences, 25:2782, Feb 2024. URL: https://doi.org/10.3390/ijms25052782, doi:10.3390/ijms25052782. This article has 9 citations.

7. (gharabli2024thesugardonor pages 4-6): Hani Gharabli and Ditte Hededam Welner. The sugar donor specificity of plant family 1 glycosyltransferases. Frontiers in Bioengineering and Biotechnology, May 2024. URL: https://doi.org/10.3389/fbioe.2024.1396268, doi:10.3389/fbioe.2024.1396268. This article has 22 citations.

8. (speeckaert2022ugt72amajor pages 8-9): Nathanaël Speeckaert, Mondher El Jaziri, Marie Baucher, and Marc Behr. Ugt72, a major glycosyltransferase family for flavonoid and monolignol homeostasis in plants. Biology, 11:441, Mar 2022. URL: https://doi.org/10.3390/biology11030441, doi:10.3390/biology11030441. This article has 44 citations.

9. (lethe2024similaritiesinstructure pages 7-9): Mary Caroline L. Lethe, Vincent Paris, Xiaoqiang Wang, and Clement T. Y. Chan. Similarities in structure and function of udp-glycosyltransferase homologs from human and plants. International Journal of Molecular Sciences, 25:2782, Feb 2024. URL: https://doi.org/10.3390/ijms25052782, doi:10.3390/ijms25052782. This article has 9 citations.

10. (majeed2024glycosyltransferasesunravelingmolecular pages 1-2): Humara Naz Majeed, Muhammad Kashif Zahoor, and Sumaira Shaheen. Glycosyltransferases: unraveling molecular insights and biotechnological implications. Science Reviews. Biology, 3:16-31, Apr 2024. URL: https://doi.org/10.57098/scirevs.biology.3.1.3, doi:10.57098/scirevs.biology.3.1.3. This article has 6 citations.

11. (majeed2024glycosyltransferasesunravelingmolecular pages 2-4): Humara Naz Majeed, Muhammad Kashif Zahoor, and Sumaira Shaheen. Glycosyltransferases: unraveling molecular insights and biotechnological implications. Science Reviews. Biology, 3:16-31, Apr 2024. URL: https://doi.org/10.57098/scirevs.biology.3.1.3, doi:10.57098/scirevs.biology.3.1.3. This article has 6 citations.

12. (lethe2024similaritiesinstructure pages 9-11): Mary Caroline L. Lethe, Vincent Paris, Xiaoqiang Wang, and Clement T. Y. Chan. Similarities in structure and function of udp-glycosyltransferase homologs from human and plants. International Journal of Molecular Sciences, 25:2782, Feb 2024. URL: https://doi.org/10.3390/ijms25052782, doi:10.3390/ijms25052782. This article has 9 citations.

13. (speeckaert2022ugt72amajor pages 1-2): Nathanaël Speeckaert, Mondher El Jaziri, Marie Baucher, and Marc Behr. Ugt72, a major glycosyltransferase family for flavonoid and monolignol homeostasis in plants. Biology, 11:441, Mar 2022. URL: https://doi.org/10.3390/biology11030441, doi:10.3390/biology11030441. This article has 44 citations.

14. (speeckaert2022ugt72amajor pages 5-8): Nathanaël Speeckaert, Mondher El Jaziri, Marie Baucher, and Marc Behr. Ugt72, a major glycosyltransferase family for flavonoid and monolignol homeostasis in plants. Biology, 11:441, Mar 2022. URL: https://doi.org/10.3390/biology11030441, doi:10.3390/biology11030441. This article has 44 citations.

## Artifacts

- [Edison artifact artifact-00](PTHR48047-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR48047-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](PTHR48047-deep-research-falcon_artifacts/artifact-02.md)

## Citations

1. lethe2024similaritiesinstructure pages 4-5
2. gharabli2024thesugardonor pages 3-4
3. gharabli2024thesugardonor pages 1-3
4. gharabli2024thesugardonor pages 4-6
5. majeed2024glycosyltransferasesunravelingmolecular pages 1-2
6. lethe2024similaritiesinstructure pages 7-9
7. lethe2024similaritiesinstructure pages 1-4
8. lethe2024similaritiesinstructure pages 5-7
9. majeed2024glycosyltransferasesunravelingmolecular pages 2-4
10. lethe2024similaritiesinstructure pages 9-11
11. https://doi.org/10.3389/fbioe.2024.1396268,
12. https://doi.org/10.3390/ijms25052782,
13. https://doi.org/10.3390/biology11030441,
14. https://doi.org/10.57098/scirevs.biology.3.1.3,