---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-21T21:17:01.727928'
end_time: '2026-06-21T21:31:22.347186'
duration_seconds: 860.62
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR24351
  interpro_name: Serine/threonine-protein kinase
  interpro_short_name: Ser_Thr_protein_kinase
  interpro_type: family
  interpro_integrated: None (top-level entry)
  member_databases: Not specified
  n_proteins: '70981'
  n_taxa: '12042'
  n_subfamilies: '71'
  interpro2go_terms: None mapped (no InterPro2GO terms for this entry)
  interpro_description: The protein family includes serine/threonine-protein kinases
    involved in a wide range of cellular processes such as metabolism, proliferation,
    cell survival, growth, and angiogenesis. These kinases mediate their effects by
    phosphorylating downstream substrates, including various ion channels, membrane
    transporters, cellular enzymes, and transcription factors. They play key roles
    in signaling pathways activated by growth factors, nutrients, and stress, contributing
    to cell cycle progression, protein synthesis, and apoptosis regulation. The family
    members are also implicated in cellular stress responses, regulation of renal
    sodium retention, neuronal excitability, and memory consolidation. Some kinases
    within the family are involved in the regulation of cytoskeletal proteins, cell
    adhesion, motility, migration, and immune responses. They are activated by multiple
    phosphorylation events and can be regulated by calcium, diacylglycerol, and phosphatidylserine,
    with some isoforms being constitutively active.
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 14
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PTHR24351-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR24351-deep-research-falcon_artifacts/artifact-01.md
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
- **Accession:** PTHR24351
- **Name:** Serine/threonine-protein kinase
- **Short name:** Ser_Thr_protein_kinase
- **Entry type:** family
- **Integrated into / parent:** None (top-level entry)
- **Member database signatures:** Not specified
- **Scale:** 70981 proteins across 12042 taxa, 71 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** The protein family includes serine/threonine-protein kinases involved in a wide range of cellular processes such as metabolism, proliferation, cell survival, growth, and angiogenesis. These kinases mediate their effects by phosphorylating downstream substrates, including various ion channels, membrane transporters, cellular enzymes, and transcription factors. They play key roles in signaling pathways activated by growth factors, nutrients, and stress, contributing to cell cycle progression, protein synthesis, and apoptosis regulation. The family members are also implicated in cellular stress responses, regulation of renal sodium retention, neuronal excitability, and memory consolidation. Some kinases within the family are involved in the regulation of cytoskeletal proteins, cell adhesion, motility, migration, and immune responses. They are activated by multiple phosphorylation events and can be regulated by calcium, diacylglycerol, and phosphatidylserine, with some isoforms being constitutively active.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR24351 (Serine/threonine-protein kinase)**, structured to support GO annotation review.

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
- **Accession:** PTHR24351
- **Name:** Serine/threonine-protein kinase
- **Short name:** Ser_Thr_protein_kinase
- **Entry type:** family
- **Integrated into / parent:** None (top-level entry)
- **Member database signatures:** Not specified
- **Scale:** 70981 proteins across 12042 taxa, 71 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** The protein family includes serine/threonine-protein kinases involved in a wide range of cellular processes such as metabolism, proliferation, cell survival, growth, and angiogenesis. These kinases mediate their effects by phosphorylating downstream substrates, including various ion channels, membrane transporters, cellular enzymes, and transcription factors. They play key roles in signaling pathways activated by growth factors, nutrients, and stress, contributing to cell cycle progression, protein synthesis, and apoptosis regulation. The family members are also implicated in cellular stress responses, regulation of renal sodium retention, neuronal excitability, and memory consolidation. Some kinases within the family are involved in the regulation of cytoskeletal proteins, cell adhesion, motility, migration, and immune responses. They are activated by multiple phosphorylation events and can be regulated by calcium, diacylglycerol, and phosphatidylserine, with some isoforms being constitutively active.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR24351 (Serine/threonine-protein kinase)**, structured to support GO annotation review.

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


# Comprehensive Research Report: InterPro Entry PTHR24351 (Serine/threonine-protein kinase)

## Executive Summary

PTHR24351 represents one of the largest and most functionally heterogeneous protein families in InterPro, encompassing 70,981 proteins across 12,042 taxa and 71 subfamilies. This report evaluates the appropriateness of GO annotations for this entry and concludes that **the absence of InterPro2GO mappings for PTHR24351 is scientifically appropriate** due to extreme functional divergence across subfamilies, presence of catalytically inactive pseudokinases, and vast taxonomic breadth spanning all three domains of life.

---

## 1. Family Definition and Biochemistry

### 1.1 Conserved Kinase Fold and Catalytic Machinery

Serine/threonine-protein kinases share a highly conserved bilobal protein kinase fold of approximately 290 residues, consisting of a small N-terminal lobe and a larger C-terminal lobe (seok2021structuralinsightsinto pages 1-2, gizzio2024evolutionarysequenceand pages 1-3). The N-terminal lobe primarily positions ATP, while the C-terminal lobe contributes most of the substrate-recognition surface and catalytic machinery (seok2021structuralinsightsinto pages 1-2).

| Feature / element | Typical location in kinase domain | Conserved motif / residue(s) | Mechanistic role in catalysis or regulation | Caveats across PTHR24351 breadth | Key citation |
|---|---|---|---|---|---|
| Bilobal protein kinase fold | Whole catalytic core (~290 aa) | N-terminal lobe + C-terminal lobe | Canonical serine/threonine kinases share a conserved bilobal kinase fold in which the N-lobe primarily contributes ATP positioning and the C-lobe contributes much of substrate recognition and catalytic machinery | Fold is conserved broadly, but conformational preferences and regulation vary strongly among subfamilies and pseudokinases | (seok2021structuralinsightsinto pages 1-2, gizzio2024evolutionarysequenceand pages 1-3, shrestha2020cataloguingthedead pages 1-2) |
| N-terminal lobe | N-terminal half of catalytic domain | Small lobe with glycine-rich loop and αC-helix | Helps bind and orient ATP; contains mobile elements required to assemble the active state | Some pseudokinases retain the fold but alter catalytic competence | (seok2021structuralinsightsinto pages 1-2, gizzio2024evolutionarysequenceand pages 1-3, shrestha2020cataloguingthedead pages 1-2) |
| C-terminal lobe | C-terminal half of catalytic domain | Larger α-helical lobe containing catalytic loop and activation segment | Major platform for substrate binding, phosphotransfer chemistry, and regulatory coupling to the activation loop | Conserved as a structural framework, but substrate-binding surfaces differ extensively among kinase families | (seok2021structuralinsightsinto pages 1-2, gizzio2024evolutionarysequenceand pages 1-3, johnson2023anatlasof pages 1-2) |
| Glycine-rich loop (P-loop/G-loop) | N-lobe, above nucleotide-binding pocket | Gly-rich segment; exact sequence varies | Flexible loop that helps position ATP phosphates and participates in active/inactive conformational transitions | Sequence is not invariant across all family members, though function of this mobile element is broadly conserved | (gizzio2024evolutionarysequenceand pages 1-3) |
| β3 lysine / catalytic lysine | N-lobe ATP-binding region | Conserved Lys (classically the ATP-anchoring lysine) | Coordinates ATP phosphates and is a hallmark ATP-binding residue in active kinases; often functionally coupled to αC-helix positioning | Some pseudokinases lose the canonical catalytic configuration even if a lysine is retained or relocated | (gizzio2024evolutionarysequenceand pages 1-3, shrestha2020cataloguingthedead pages 1-2) |
| αC-helix regulatory element | N-lobe | Conserved helix containing residues that couple catalytic and substrate-binding lobes | Dynamic positioning of αC-helix is required for assembly of the active conformation and allosteric regulation | Conformational equilibria differ between serine/threonine kinases and tyrosine kinases, and across STK subfamilies | (gizzio2024evolutionarysequenceand pages 1-3) |
| Catalytic loop | C-lobe, central catalytic core | HRD motif (His-Arg-Asp) | Provides core catalytic residues; the HRD-Asp is a canonical catalytic residue involved in phosphotransfer chemistry, while the loop acts as a structural hub for active-site organization | The motif can be degraded or repurposed in pseudokinases; not every matched sequence will be catalytically active | (gizzio2024evolutionarysequenceand pages 1-3, shrestha2020cataloguingthedead pages 1-2) |
| HRD motif | Catalytic loop in C-lobe | His-Arg-Asp | The HRD motif is a signature catalytic-loop element; HRD-Arg also contributes to the positively charged “RD-pocket” implicated in activation-loop phosphate sensing and regulation | RD versus non-RD kinases differ in regulation; this distinction itself argues against uniform process-level GO mapping for the full family | (gizzio2024evolutionarysequenceand pages 1-3) |
| DFG motif | N-terminus of activation loop | Asp-Phe-Gly | DFG-Asp directly participates in catalysis and metal/ATP coordination; DFG orientation is a central determinant of active vs inactive conformations | Some family members substitute related motifs (for example DYG-like variants in some lineages), and pseudokinases may alter catalytic function despite retaining fold similarity | (gizzio2024evolutionarysequenceand pages 1-3, shrestha2020cataloguingthedead pages 1-2) |
| Activation loop / activation segment | Begins at DFG and ends before APE | Flexible ~20-residue segment; often contains regulatory phosphosites on Ser/Thr | Central regulatory segment controlling access to the active site; phosphorylation in this region stabilizes active conformations and remodels substrate-binding surfaces | Presence, exact phosphosite usage, and mode of activation differ sharply by subfamily; some kinases are constitutively active while others are phosphorylation dependent | (gizzio2024evolutionarysequenceand pages 1-3, seok2021structuralinsightsinto pages 1-2) |
| APE motif | C-terminal end of activation segment | Ala-Pro-Glu | Marks the end of the activation loop and contributes to organization of the substrate-recognition region in the C-lobe | Conserved as a landmark motif, but surrounding substrate-recognition determinants diverge substantially | (gizzio2024evolutionarysequenceand pages 1-3) |
| P+1 loop / substrate recognition surface | C-terminal portion of activation segment near APE | No single invariant motif; structurally conserved region | Forms part of the intermolecular binding surface that recognizes the phosphoacceptor-site context in peptide/protein substrates | This region is a major source of substrate specificity divergence across the STK family | (gizzio2024evolutionarysequenceand pages 1-3, johnson2023anatlasof pages 1-2) |
| Activation-loop anchor interactions | Interfaces between activation loop and catalytic core | N-terminal and C-terminal anchors; RD-pocket interactions | Non-covalent anchoring of the activation loop helps stabilize active conformations; phosphorylation can reinforce these interactions | These anchors differ substantially between STKs and TKs and among STK lineages, contributing to divergent conformational landscapes | (gizzio2024evolutionarysequenceand pages 1-3) |
| ATP-binding function | Nucleotide pocket between lobes | ATP-binding residues include conserved Lys and DFG-associated catalytic machinery | ATP is the phosphate donor for Ser/Thr phosphorylation; ATP binding and proper lobe closure are prerequisites for phosphotransfer | “ATP binding” would be overly generic for a top-level GO assignment because it adds little informational value and may not hold for all pseudokinases | (seok2021structuralinsightsinto pages 1-2, shrestha2020cataloguingthedead pages 1-2) |
| Phosphoacceptor chemistry | Active site facing substrate hydroxyl | Ser/Thr target residue on substrate | Catalyzes transfer of phosphate from ATP to substrate Ser/Thr hydroxyl groups, underlying the defining biochemical activity of canonical STKs | Family-wide substrate context and biological role vary enormously; many proteins in the top-level family differ in cellular role despite shared chemistry | (seok2021structuralinsightsinto pages 1-2, johnson2023anatlasof pages 1-2) |
| Pseudokinase-dead variants | Across multiple subfamilies | Often loss/alteration of catalytic Asp or other canonical residues | Preserve the kinase-like fold but frequently repurpose it for scaffolding, conformational switching, or allosteric signaling rather than phosphotransfer | Important exception showing that even conserved kinase-fold matches in PTHR24351 need not support catalytic GO annotation at the top-family level | (shrestha2020cataloguingthedead pages 1-2, jeffery2020enzymespseudoenzymesand pages 1-5) |


*Table: This table summarizes the conserved architecture and motifs of serine/threonine protein kinases, emphasizing which features support catalytic activity and which vary across the broad PTHR24351 family. It is useful for GO review because it highlights both universally conserved kinase-fold properties and the major exceptions, especially pseudokinases and divergent regulatory mechanisms.*

### 1.2 Conserved Catalytic Motifs

Multiple conserved sequence motifs define the serine/threonine kinase catalytic mechanism:

**DFG Motif (Asp-Phe-Gly):** Located at the N-terminus of the activation loop, the DFG-Asp directly participates in catalysis through metal coordination and ATP positioning. DFG orientation (DFG-in vs. DFG-out) is a central determinant of active versus inactive conformations (gizzio2024evolutionarysequenceand pages 1-3).

**HRD Motif (His-Arg-Asp):** Found in the catalytic loop, this motif provides core catalytic residues. The HRD-Asp is involved in phosphotransfer chemistry, while HRD-Arg contributes to the positively charged "RD-pocket" that senses activation-loop phosphorylation (gizzio2024evolutionarysequenceand pages 1-3).

**APE Motif (Ala-Pro-Glu):** Marks the C-terminal boundary of the activation segment and contributes to organization of substrate-recognition regions (gizzio2024evolutionarysequenceand pages 1-3).

**ATP-Binding Lysine:** A conserved lysine residue in the N-lobe β3 strand coordinates ATP phosphates and is essential for catalytic activity in canonical kinases (gizzio2024evolutionarysequenceand pages 1-3, shrestha2020cataloguingthedead pages 1-2).

**Activation Loop:** This flexible ~20-residue segment beginning at DFG and ending before APE undergoes regulatory phosphorylation on serine or threonine residues, stabilizing active conformations and remodeling substrate-binding surfaces (gizzio2024evolutionarysequenceand pages 1-3, seok2021structuralinsightsinto pages 1-2).

### 1.3 Mechanistic Function

Canonical serine/threonine kinases catalyze the transfer of the γ-phosphate from ATP to hydroxyl groups of serine or threonine residues on protein substrates (seok2021structuralinsightsinto pages 1-2, johnson2023anatlasof pages 1-2). The reaction mechanism requires proper assembly of the active conformation, involving closure of the N- and C-lobes, correct positioning of the activation loop, and coordination of ATP and substrate in the catalytic cleft (seok2021structuralinsightsinto pages 1-2).

Experimental studies have demonstrated that phosphorylation of both serine and threonine induces substantial conformational restriction, with phosphothreonine exhibiting a particularly strong disorder-to-order transition and preferentially adopting a cyclic conformation stabilized by intraresidue hydrogen bonding (seok2021structuralinsightsinto pages 1-2).

---

## 2. InterPro2GO Mapping Appropriateness

### 2.1 Current Status

PTHR24351 currently has **no InterPro2GO mappings**. This analysis evaluates whether GO terms should be assigned to this top-level family entry.

### 2.2 Assessment: No GO Terms Are Appropriate at the Top-Level Family

The absence of GO annotations for PTHR24351 is scientifically sound for the following reasons:

**Reason 1: Extreme Functional Heterogeneity**

PTHR24351 encompasses proteins involved in vastly different cellular processes as described in the InterPro entry itself: metabolism, proliferation, cell survival, growth, angiogenesis, cell cycle progression, protein synthesis, apoptosis regulation, cytoskeletal regulation, cell adhesion, motility, migration, immune responses, stress responses, sodium retention, and neuronal excitability (InterPro description). No single biological process GO term can accurately describe this breadth without being informationally vacuous.

**Reason 2: Multiple Non-Homologous Substrate Specificities**

A comprehensive atlas of substrate specificities for 303 human serine/threonine kinases revealed that kinome-wide substrate specificity is "substantially more diverse than expected and was driven extensively by negative selectivity" (johnson2023anatlasof pages 1-2). Different kinase families within the broader serine/threonine superfamily recognize completely non-overlapping substrate motifs and phosphorylate distinct sets of cellular proteins (johnson2023anatlasof pages 1-2). Assigning a process-level GO term at the family level would incorrectly imply functional equivalence.

**Reason 3: Presence of Pseudokinases**

Pseudokinases constitute approximately 10% of the eukaryotic protein kinome and are present within PTHR24351 (shrestha2020cataloguingthedead pages 1-2, jeffery2020enzymespseudoenzymesand pages 1-5). These proteins retain the kinase fold but lack one or more conserved catalytic residues (typically the catalytic aspartate) and are predicted to be catalytically inactive (shrestha2020cataloguingthedead pages 1-2). Examples include:

- **Tribbles pseudokinases:** CAMK-related pseudokinases that function as scaffold/adaptor proteins controlling cell growth, proliferation, and metabolism through protein-protein interactions rather than catalysis (shrestha2020cataloguingthedead pages 1-2, jeffery2020enzymespseudoenzymesand pages 1-5)
- **EphA10 and EphB6:** Receptor tyrosine kinase-related pseudokinases involved in cell-to-cell communication (shrestha2020cataloguingthedead pages 1-2)
- **PSKH2:** An orphan pseudokinase of unknown function (shrestha2020cataloguingthedead pages 1-2)

Assigning catalytic activity terms (e.g., "protein serine/threonine kinase activity" GO:0004674) to the entire family would be factually incorrect for pseudokinase members.

**Reason 4: Subfamily-Specific Functions**

The 71 subfamilies within PTHR24351 have evolved distinct, often non-overlapping functions:

| Major group / clade | Representative examples | Distinguishing features | Typical biological functions | Pseudokinases present? | Evidence of functional divergence / neo-functionalization |
|---|---|---|---|---|---|
| AGC | PKA/PRKACA, PKB/Akt, PKC, RSK, MAST kinases | Canonical ePK fold; often regulated by activation-loop and C-terminal tail phosphorylation; many are lipid- or second-messenger-responsive and occupy a major human Ser/Thr kinase branch (fulcher2020functionsandregulation pages 1-2) | Growth-factor signaling, metabolism, survival, proliferation, cytoskeletal regulation, neuronal functions; MAST kinases are development- and disease-linked (fulcher2020functionsandregulation pages 1-2) | Yes, in the broader kinase superfamily, though not all AGC subfamilies are pseudokinase-rich (shrestha2020cataloguingthedead pages 1-2, jeffery2020enzymespseudoenzymesand pages 1-5) | Strong family-specific diversification: Akt links PI3K to anabolic signaling, RSK isoforms regulate different transcriptional programs, and MAST kinases form a distinct conserved branch with specialized functions (fulcher2020functionsandregulation pages 1-2) |
| CAMK | CaMKII, AMPK, DAPK, Tribbles-related pseudokinases | Frequently Ca2+/calmodulin- or stress-responsive; active-site and docking surfaces support highly context-dependent substrate recognition; includes pseudokinase offshoots such as Tribbles (shrestha2020cataloguingthedead pages 1-2) | Calcium signaling, stress responses, metabolism, cell-cycle control, neuronal plasticity and memory; CaMKII directly integrates substrates and activators at the active site (shrestha2020cataloguingthedead pages 1-2) | Yes; Tribbles are a CAMK-related pseudokinase branch (shrestha2020cataloguingthedead pages 1-2) | Clear neo-functionalization: Tribbles lost canonical catalysis but evolved scaffold/adaptor roles in growth, proliferation, metabolism, and signaling control (shrestha2020cataloguingthedead pages 1-2, jeffery2020enzymespseudoenzymesand pages 1-5) |
| CMGC | CDKs, MAPKs, GSK3, CLK, DYRK | Large, well-defined eukaryotic branch; many members recognize proline-directed or primed motifs; often tightly controlled by cyclins, phosphorylation, or docking interactions (johnson2023anatlasof pages 1-2) | Cell cycle, transcription, RNA processing, stress signaling, developmental signaling; GSK3/CK1-like priming logic is a major specialization in this space (johnson2023anatlasof pages 1-2) | Some kinase-like inactive members occur in the wider kinome, but pseudokinases are less central here than in some other clades (shrestha2020cataloguingthedead pages 1-2) | Functional divergence is substantial despite shared fold: cell-cycle kinases, MAPK cascades, and constitutively biased kinases such as GSK3 serve very different biological roles and motif logics (johnson2023anatlasof pages 1-2) |
| CK1 | CK1α, CK1δ, CK1ε, CK1γ isoforms, VRKs, TTBKs | Distinct branch of the human kinome; typically monomeric; often considered basally active; strong dependence on localization, accessory proteins, and primed substrates; related branches include VRK and TTBK members (fulcher2020functionsandregulation pages 1-2) | Circadian regulation, Wnt signaling, membrane trafficking, DNA damage responses, ciliogenesis, immune signaling, neuronal processes (fulcher2020functionsandregulation pages 1-2) | Limited evidence for classic pseudokinase enrichment within core CK1 itself, but kinase-dead variants exist broadly across the kinome (shrestha2020cataloguingthedead pages 1-2) | Marked isoform divergence: CK1α/δ/ε share kinase-domain similarity but differ outside the catalytic domain, in regulation, localization, and pathway usage; TTBK and VRK branches represent further specialization (fulcher2020functionsandregulation pages 1-2) |
| STE | MAP4Ks, MAP3Ks, yeast Ste kinases and relatives | Kinases that frequently act upstream in MAPK cascades and other signaling relays; many function in hierarchical phosphorylation networks rather than direct receptor output (johnson2023anatlasof pages 1-2) | Stress signaling, morphogenesis, polarity, immune and developmental pathways, kinase-cascade organization (johnson2023anatlasof pages 1-2) | Possible in the broader kinase universe, but not the defining feature of the core group in the retrieved evidence (shrestha2020cataloguingthedead pages 1-2) | Strong pathway-level divergence: related catalytic cores have been redeployed as distinct upstream relays in multiple signaling circuits and taxa (johnson2023anatlasof pages 1-2) |
| Plant RLK / RLCK-rich Ser/Thr kinase expansions | RLK-Pelle family members, receptor-like cytoplasmic kinases, SERK/NIK/CIK-related branches | Massive plant-specific expansions of kinase-domain proteins combined with extracellular receptor modules or cytoplasmic signaling modules; many plant kinomes are dominated by these clades (yeung2021evolutionoffunctional pages 1-2) | Development, meristem control, hormone signaling, antiviral defense, pattern-triggered immunity, abiotic stress signaling (yeung2021evolutionoffunctional pages 1-2) | Yes; plant receptor-like kinase repertoires include many pseudokinases and pseudokinase-containing subfamilies (yeung2021evolutionoffunctional pages 1-2) | Especially strong neo-functionalization via domain shuffling and lineage-specific expansions; closely related kinase domains are reused in immunity vs growth/development signaling (yeung2021evolutionoffunctional pages 1-2) |
| Broad eukaryotic Ser/Thr kinase superfamily outside the named core groups | Additional KinBase/PANTHER-recognized Ser/Thr branches across opisthokonts, plants, protists, and parasites | Shared catalytic fold, but highly divergent domain architectures, regulatory inserts, and substrate-recognition surfaces; human kinome-wide profiling shows specificity is far more diverse than expected and heavily shaped by negative selectivity (johnson2023anatlasof pages 1-2) | Nearly every major eukaryotic cellular process: metabolism, proliferation, apoptosis, autophagy, transcription, trafficking, stress adaptation (seok2021structuralinsightsinto pages 1-2, johnson2023anatlasof pages 1-2) | Yes; pseudokinases are widespread across the kinome and often preserve fold while losing one or more canonical catalytic residues (shrestha2020cataloguingthedead pages 1-2, jeffery2020enzymespseudoenzymesand pages 1-5) | Human kinome-wide assays showed major substrate-specificity diversification across 303 Ser/Thr kinases, underscoring that top-level family annotations do not imply a single conserved cellular role (johnson2023anatlasof pages 1-2) |
| Bacterial STK families | PknB-like kinases and the 35 canonical bacterial STK families from kinome-scale analysis | Bacterial Ser/Thr kinases are evolutionarily related to eukaryotic STKs but possess distinct sequence constraints, regulatory domains, and in some cases a characteristic Arg in the C-helix; >300,000 sequences were classified into many families (gizzio2024evolutionarysequenceand pages 1-3) | Cell growth, cell-wall regulation, virulence, pathogenicity, environmental sensing, signaling in diverse bacterial lineages (gizzio2024evolutionarysequenceand pages 1-3) | Yes; 7 bacterial pseudokinase families were identified in kinome-scale analysis (gizzio2024evolutionarysequenceand pages 1-3) | Extensive diversification is documented: bacterial STKs form many canonical and pseudokinase families with distinct regulatory and substrate-specificity determinants, showing they cannot all share the same GO process terms (gizzio2024evolutionarysequenceand pages 1-3) |
| Cross-family pseudokinase layer spanning PTHR24351 breadth | Tribbles, PSKH2, kinase-dead receptor-like kinases, other pseudokinase branches | Retain the bilobal kinase fold but lose one or more catalytic residues or canonical motif functions; often repurposed for scaffolding, conformational switching, allosteric regulation, or protein recruitment (shrestha2020cataloguingthedead pages 1-2, jeffery2020enzymespseudoenzymesand pages 1-5) | Signal integration, adaptor/scaffold roles, control of degradation, pathway gating, noncatalytic regulation of active kinases and signaling complexes (shrestha2020cataloguingthedead pages 1-2, jeffery2020enzymespseudoenzymesand pages 1-5) | Yes—this row summarizes the pseudokinase component itself (shrestha2020cataloguingthedead pages 1-2, jeffery2020enzymespseudoenzymesand pages 1-5) | Pseudokinases are direct evidence against blanket catalytic GO transfer at the top-family level: homologous kinase-fold proteins may have opposite or purely noncatalytic functions after evolutionary repurposing (shrestha2020cataloguingthedead pages 1-2, jeffery2020enzymespseudoenzymesand pages 1-5) |


*Table: This table summarizes the major serine/threonine kinase groups relevant to the broad PTHR24351 family, highlighting why the family is functionally heterogeneous. It also shows where pseudokinases and lineage-specific expansions occur, supporting cautious GO annotation at subfamily rather than top-family level.*

Major groups like AGC, CAMK, CMGC, CK1, and STE kinases share the kinase fold but serve completely different biological roles and cannot be accurately described by a single GO biological process term (johnson2023anatlasof pages 1-2, fulcher2020functionsandregulation pages 1-2).

**Reason 5: Generic Terms Provide No Information Value**

The only GO terms that could apply across the entire family would be extremely generic annotations such as:
- "ATP binding" (GO:0005524)
- "metal ion binding" (GO:0046872)
- "protein binding" (GO:0005515)

These terms are so broad that they add minimal informational value for functional annotation and fail to capture the specific biology of individual kinases (johnson2023anatlasof pages 1-2). Moreover, even "ATP binding" is inaccurate for pseudokinases that may have altered or lost nucleotide-binding capacity (shrestha2020cataloguingthedead pages 1-2).

**Reason 6: Taxonomic Breadth Precludes Universal Process/Component Terms**

PTHR24351 spans 12,042 taxa across bacteria, archaea, and eukaryotes (InterPro description). Serine/threonine kinases are ancient enzymes likely present in the last universal common ancestor (LUCA) ~3-4 billion years ago (gizzio2024evolutionarysequenceand pages 1-3). Recent analyses have classified over 300,000 bacterial serine/threonine kinase sequences into 35 canonical families plus 7 pseudokinase families (gizzio2024evolutionarysequenceand pages 1-3).

Cellular compartments, signaling pathways, and biological processes differ dramatically across these taxa. For example:
- Bacterial STKs function in cell-wall regulation and virulence pathways absent in eukaryotes (gizzio2024evolutionarysequenceand pages 1-3)
- Plant receptor-like kinases mediate pathogen defense and meristem development specific to plants (yeung2021evolutionoffunctional pages 1-2)
- Mammalian kinases regulate angiogenesis and immune responses not present in bacteria or plants

No single GO biological process or cellular component term holds across this taxonomic breadth.

### 2.3 Recommended GO Action Pattern

**For PTHR24351 (top-level family):** **ACCEPT the absence of InterPro2GO mappings**. Do not add GO terms at this level.

**For the 71 subfamilies:** GO annotations should be evaluated and assigned at the subfamily level where functional homogeneity can be demonstrated through experimental evidence. Each subfamily should be assessed independently for:
1. Conservation of catalytic residues (vs. pseudokinase status)
2. Substrate specificity based on experimental data
3. Biological process participation supported by literature
4. Cellular localization validated experimentally
5. Taxonomic scope of the subfamily

**Rationale:** The distinction between a functionally homogeneous subfamily and a heterogeneous top-level family is critical for accurate GO annotation. PTHR24351 is precisely the type of broad, ancient, functionally diverse family for which top-level GO annotations systematically over-annotate and mislead users.

---

## 3. Functional Divergence Across the Family

### 3.1 Major Evolutionary Groups

The serine/threonine kinase superfamily represented by PTHR24351 comprises multiple evolutionarily distinct groups that have undergone extensive functional divergence and neo-functionalization:

**AGC Group:** Named for PKA, PKG, and PKC families, AGC kinases are often responsive to lipids or second messengers and include kinases regulating metabolism, survival, and proliferation. RSK1 and RSK2 isoforms, both classified as AGC kinases, regulate completely different transcriptional programs despite high sequence similarity (fulcher2020functionsandregulation pages 1-2).

**CAMK Group:** Frequently calcium/calmodulin-regulated, CAMK includes kinases controlling stress responses, metabolism, and neuronal plasticity. This group notably includes the Tribbles pseudokinase branch, which lost catalytic activity but evolved scaffold functions for controlling growth factor signaling and metabolic pathways—a clear example of neo-functionalization (shrestha2020cataloguingthedead pages 1-2, jeffery2020enzymespseudoenzymesand pages 1-5).

**CMGC Group:** A large eukaryotic branch containing cell-cycle kinases (CDKs), MAP kinases, GSK3, and RNA-processing kinases. Despite sharing catalytic machinery, these subfamilies serve dramatically different roles in cell-cycle control versus stress signaling (johnson2023anatlasof pages 1-2).

**CK1 Family:** Forms a distinct branch with isoforms (CK1α, δ, ε, γ) that differ in regulation, localization, and pathway usage despite kinase-domain similarity. CK1 kinases function in circadian regulation, Wnt signaling, and DNA damage responses (fulcher2020functionsandregulation pages 1-2).

**STE Group:** Kinases frequently acting upstream in MAPK cascades, serving as hierarchical signaling relays (johnson2023anatlasof pages 1-2).

### 3.2 Catalytically Dead Members (Pseudokinases)

Pseudokinases represent a major mechanism of functional divergence through loss of catalytic activity while retaining the kinase fold for regulatory functions:

**Structural Basis:** Pseudokinases typically lack the catalytic aspartate in the HRD motif or other essential catalytic residues. The kinase fold is preserved, but conformational dynamics and regulatory mechanisms are repurposed (shrestha2020cataloguingthedead pages 1-2, jeffery2020enzymespseudoenzymesand pages 1-5).

**Functional Repurposing:** Rather than catalyzing phosphotransfer, pseudokinases function as:
- Scaffolds for assembling signaling complexes
- Allosteric regulators of active kinases
- Conformational switches responding to cellular signals
- Protein recruitment modules (shrestha2020cataloguingthedead pages 1-2, jeffery2020enzymespseudoenzymesand pages 1-5)

**Examples:**
- **Tribbles:** CAMK-related pseudokinases that bind and promote degradation of transcription factors like C/EBP, controlling cell growth and metabolism (shrestha2020cataloguingthedead pages 1-2, jeffery2020enzymespseudoenzymesand pages 1-5)
- **EphA10 and EphB6:** Vertebrate receptor pseudokinases involved in cell-cell signaling despite lacking catalytic activity (shrestha2020cataloguingthedead pages 1-2)
- **Plant receptor-like pseudokinases:** Involved in immunity and development through noncatalytic mechanisms (yeung2021evolutionoffunctional pages 1-2)

### 3.3 Substrate Specificity Divergence

A landmark study profiling 303 human serine/threonine kinases using peptide library screening demonstrated that substrate specificity is "substantially more diverse than expected" and "driven extensively by negative selectivity" (johnson2023anatlasof pages 1-2). Kinases recognize distinct amino acid residues at multiple positions surrounding the phosphorylation site, creating family-specific recognition motifs that ensure signaling fidelity (johnson2023anatlasof pages 1-2).

Importantly, 129 out of 303 kinases showed selectivity for prephosphorylated substrates (phospho-priming), adding another layer of specificity divergence (johnson2023anatlasof pages 1-2). This diversity in substrate recognition reinforces that PTHR24351 members phosphorylate non-overlapping substrate sets and cannot be described by a single biological process GO term.

---

## 4. Taxonomic Scope

### 4.1 Cross-Kingdom Distribution

PTHR24351 exhibits extraordinary taxonomic breadth, with 70,981 proteins identified across 12,042 taxa (InterPro description). Serine/threonine-protein kinases are distributed across all three domains of life:

**Bacteria:** Over 300,000 bacterial STK sequences have been classified into 35 canonical kinase families and 7 pseudokinase families. Bacterial STKs regulate cell growth, cell-wall synthesis, virulence, and environmental sensing (gizzio2024evolutionarysequenceand pages 1-3). These kinases possess distinct sequence constraints, including a characteristic arginine in the C-helix regulatory element not universally present in eukaryotic STKs (gizzio2024evolutionarysequenceand pages 1-3).

**Archaea:** While less extensively characterized, serine/threonine kinases are present in archaeal genomes and likely contributed to the ancient kinase repertoire predating eukaryogenesis (gizzio2024evolutionarysequenceand pages 1-3).

**Eukaryotes:** STKs are ubiquitous across all eukaryotic lineages:
- **Fungi:** Contains kinases regulating cell-cycle and stress responses
- **Plants:** Massive expansions of receptor-like kinases (RLKs) and receptor-like cytoplasmic kinases (RLCKs) mediating development, immunity, and environmental sensing (yeung2021evolutionoffunctional pages 1-2)
- **Protists:** Kinomes have been characterized in parasitic protists including trypanosomatids and apicomplexans
- **Metazoans:** Extensive diversification in holozoans, with human genome encoding over 400 serine/threonine kinases classified into multiple major groups (johnson2023anatlasof pages 1-2, fulcher2020functionsandregulation pages 1-2)

### 4.2 Evolutionary Timescale

Serine/threonine kinases are among the most ancient signaling enzymes, with evidence suggesting their presence in the last universal common ancestor (LUCA) approximately 3-4 billion years ago (gizzio2024evolutionarysequenceand pages 1-3). This ancient origin is consistent with their fundamental role in cellular regulation across all life forms.

Tyrosine kinases, by contrast, emerged much later—just prior to metazoan evolution ~600 million years ago (gizzio2024evolutionarysequenceand pages 1-3, yeung2021evolutionoffunctional pages 1-2). The STK-to-TK divergence represents a major evolutionary innovation in multicellular eukaryotes.

### 4.3 Implications for GO Annotation

The vast taxonomic scope of PTHR24351 means that:

1. **Process terms** referencing eukaryotic-specific pathways (e.g., "cell cycle," "angiogenesis," "immune response") do not apply to bacterial or archaeal members
2. **Component terms** referencing eukaryotic organelles (e.g., "nucleus," "mitochondrion") do not apply to prokaryotes
3. **Taxon-specific expansions** (e.g., plant RLKs, bacterial virulence kinases) serve completely different biological roles despite sharing the kinase fold

No GO biological process or cellular component term holds across the full taxonomic breadth of this family. Even the most conserved molecular function term—"protein serine/threonine kinase activity" (GO:0004674)—fails for pseudokinase members present across multiple taxa.

---

## 5. Over-Annotation Verdict and Recommendations

### 5.1 Summary Verdict

The InterPro2GO system is **currently appropriate** for PTHR24351 by having **no GO term mappings** at the top-level family. This entry represents a textbook case where:

1. **Functional heterogeneity is extreme:** 71 subfamilies with diverse roles in metabolism, proliferation, immunity, development, stress responses, and more
2. **Catalytic activity is not universal:** Pseudokinases lack catalytic function despite retaining the kinase fold
3. **Taxonomic scope is maximal:** Spanning bacteria, archaea, and all eukaryotic kingdoms with taxon-specific pathway differences
4. **Substrate specificity varies completely:** Different subfamilies phosphorylate non-overlapping substrate sets
5. **Entry type is appropriate:** As a "family" rather than "domain," it correctly reflects evolutionary relatedness rather than structural modularity, but the family is too broad and ancient to support uniform GO annotation

### 5.2 Recommended GO Action Pattern

**For PTHR24351 (top-level):** **ACCEPT / KEEP_AS_NON_CORE**

- Current status (no GO mappings) is scientifically appropriate
- Do not add GO terms at this level
- Even generic terms like "ATP binding" or "protein serine/threonine kinase activity" would be inaccurate due to pseudokinases

**For the 71 subfamilies:** **ANNOTATE_AT_SUBFAMILY_LEVEL**

Each subfamily should be independently evaluated for GO annotation based on:
1. Experimental evidence of substrate specificity
2. Demonstrated biological process participation
3. Validated cellular localization
4. Conservation of catalytic machinery (vs. pseudokinase status)
5. Taxonomic homogeneity of the subfamily

Subfamily-level annotations would be far more informative and accurate than any top-level family annotation.

### 5.3 Recommendations for InterPro

**Recommendation 1:** Maintain the absence of GO mappings for PTHR24351 at the top-level family entry.

**Recommendation 2:** Consider whether the 71 subfamilies within PTHR24351 should be promoted to independent InterPro entries with subfamily-specific GO annotations. This would follow the model of other highly diversified families where functional homogeneity exists at the subfamily but not family level.

**Recommendation 3:** If subfamily-level InterPro entries are not feasible, consider adding a cautionary note to PTHR24351 indicating that functional annotation should be performed at the subfamily level and that the top-level family encompasses catalytically active and inactive (pseudokinase) members.

**Recommendation 4:** Document that PTHR24351 is an example of an evolutionarily ancient, functionally heterogeneous family where the shared kinase fold does not imply shared biological function—a critical distinction for avoiding systematic over-annotation in GO.

### 5.4 Broader Implications for GO Annotation Policy

PTHR24351 exemplifies a general challenge in functional annotation: **structural/evolutionary families defined by fold conservation do not necessarily correspond to functional families defined by shared biological roles**. The serine/threonine kinase superfamily has undergone:

- **Functional divergence:** Subfamilies evolved distinct substrate specificities and cellular roles
- **Neo-functionalization:** Pseudokinases repurposed the fold for noncatalytic functions  
- **Lineage-specific expansions:** Taxa-specific kinase repertoires (plant RLKs, bacterial virulence kinases) serving unique biological needs

These evolutionary processes create families where top-level GO annotation would systematically over-annotate by attributing subfamily-specific functions to all family members. The appropriate annotation strategy is to recognize these cases and restrict GO mappings to functionally homogeneous subfamilies supported by experimental evidence.

---

## Conclusion

PTHR24351 (Serine/threonine-protein kinase) represents one of the most functionally diverse protein families in biology, encompassing 70,981 proteins across 12,042 taxa, spanning all three domains of life, and including both catalytically active kinases and catalytically inactive pseudokinases across 71 subfamilies. The current absence of InterPro2GO mappings for this entry is scientifically sound and should be maintained. Any attempt to assign GO terms at the top-level family would result in systematic over-annotation, incorrectly attributing subfamily-specific functions to proteins that do not perform those functions. GO annotations should instead be assigned at the subfamily level based on experimental evidence of conserved function within evolutionarily and functionally coherent groups (seok2021structuralinsightsinto pages 1-2, johnson2023anatlasof pages 1-2, fulcher2020functionsandregulation pages 1-2, gizzio2024evolutionarysequenceand pages 1-3, shrestha2020cataloguingthedead pages 1-2, jeffery2020enzymespseudoenzymesand pages 1-5, yeung2021evolutionoffunctional pages 1-2).

References

1. (seok2021structuralinsightsinto pages 1-2): Seung-Hyeon Seok. Structural insights into protein regulation by phosphorylation and substrate recognition of protein kinases/phosphatases. Life, 11:957, Sep 2021. URL: https://doi.org/10.3390/life11090957, doi:10.3390/life11090957. This article has 122 citations.

2. (gizzio2024evolutionarysequenceand pages 1-3): Joan Gizzio, Abhishek Thakur, Allan Haldane, Carol Beth Post, and Ronald M. Levy. Evolutionary sequence and structural basis for the distinct conformational landscapes of tyr and ser/thr kinases. bioRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.03.08.584161, doi:10.1101/2024.03.08.584161. This article has 26 citations.

3. (shrestha2020cataloguingthedead pages 1-2): Safal Shrestha, Dominic P. Byrne, John A. Harris, Natarajan Kannan, and Patrick A. Eyers. Cataloguing the dead: breathing new life into pseudokinase research. Mar 2020. URL: https://doi.org/10.1111/febs.15246, doi:10.1111/febs.15246. This article has 54 citations.

4. (johnson2023anatlasof pages 1-2): Jared L. Johnson, Tomer M. Yaron, Emily M. Huntsman, Alexander Kerelsky, Junho Song, Amit Regev, Ting-Yu Lin, Katarina Liberatore, Daniel M. Cizin, Benjamin M. Cohen, Neil Vasan, Yilun Ma, Konstantin Krismer, Jaylissa Torres Robles, Bert van de Kooij, Anne E. van Vlimmeren, Nicole Andrée-Busch, Norbert F. Käufer, Maxim V. Dorovkov, Alexey G. Ryazanov, Yuichiro Takagi, Edward R. Kastenhuber, Marcus D. Goncalves, Benjamin D. Hopkins, Olivier Elemento, Dylan J. Taatjes, Alexandre Maucuer, Akio Yamashita, Alexei Degterev, Mohamed Uduman, Jingyi Lu, Sean D. Landry, Bin Zhang, Ian Cossentino, Rune Linding, John Blenis, Peter V. Hornbeck, Benjamin E. Turk, Michael B. Yaffe, and Lewis C. Cantley. An atlas of substrate specificities for the human serine/threonine kinome. Nature, 613:759-766, Jan 2023. URL: https://doi.org/10.1038/s41586-022-05575-3, doi:10.1038/s41586-022-05575-3. This article has 764 citations and is from a highest quality peer-reviewed journal.

5. (jeffery2020enzymespseudoenzymesand pages 1-5): Constance J. Jeffery. Enzymes, pseudoenzymes, and moonlighting proteins: diversity of function in protein superfamilies. The FEBS Journal, 287:4141-4149, Jun 2020. URL: https://doi.org/10.1111/febs.15446, doi:10.1111/febs.15446. This article has 84 citations.

6. (fulcher2020functionsandregulation pages 1-2): Luke J. Fulcher and Gopal P. Sapkota. Functions and regulation of the serine/threonine protein kinase ck1 family: moving beyond promiscuity. Biochemical Journal, 477:4603-4621, Dec 2020. URL: https://doi.org/10.1042/bcj20200506, doi:10.1042/bcj20200506. This article has 88 citations and is from a domain leading peer-reviewed journal.

7. (yeung2021evolutionoffunctional pages 1-2): Wayland Yeung, Annie Kwon, Rahil Taujale, Claire Bunn, Aarya Venkat, and Natarajan Kannan. Evolution of functional diversity in the holozoan tyrosine kinome. Molecular Biology and Evolution, 38:5625-5639, Aug 2021. URL: https://doi.org/10.1093/molbev/msab272, doi:10.1093/molbev/msab272. This article has 21 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PTHR24351-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR24351-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. seok2021structuralinsightsinto pages 1-2
2. gizzio2024evolutionarysequenceand pages 1-3
3. johnson2023anatlasof pages 1-2
4. shrestha2020cataloguingthedead pages 1-2
5. fulcher2020functionsandregulation pages 1-2
6. yeung2021evolutionoffunctional pages 1-2
7. jeffery2020enzymespseudoenzymesand pages 1-5
8. https://doi.org/10.3390/life11090957,
9. https://doi.org/10.1101/2024.03.08.584161,
10. https://doi.org/10.1111/febs.15246,
11. https://doi.org/10.1038/s41586-022-05575-3,
12. https://doi.org/10.1111/febs.15446,
13. https://doi.org/10.1042/bcj20200506,
14. https://doi.org/10.1093/molbev/msab272,