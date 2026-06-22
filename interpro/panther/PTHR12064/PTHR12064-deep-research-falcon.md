---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-21T20:18:12.442252'
end_time: '2026-06-21T20:31:57.037139'
duration_seconds: 824.59
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR12064
  interpro_name: METAL TRANSPORTER CNNM
  interpro_short_name: Not specified
  interpro_type: family
  interpro_integrated: IPR045095
  member_databases: Not specified
  n_proteins: '13041'
  n_taxa: '9306'
  n_subfamilies: '30'
  interpro2go_terms: None mapped (no InterPro2GO terms for this entry)
  interpro_description: Not specified in InterPro
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 27
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PTHR12064-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR12064-deep-research-falcon_artifacts/artifact-01.md
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
- **Accession:** PTHR12064
- **Name:** METAL TRANSPORTER CNNM
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** IPR045095
- **Member database signatures:** Not specified
- **Scale:** 13041 proteins across 9306 taxa, 30 subfamilies
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
**PTHR12064 (METAL TRANSPORTER CNNM)**, structured to support GO annotation review.

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
- **Accession:** PTHR12064
- **Name:** METAL TRANSPORTER CNNM
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** IPR045095
- **Member database signatures:** Not specified
- **Scale:** 13041 proteins across 9306 taxa, 30 subfamilies
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
**PTHR12064 (METAL TRANSPORTER CNNM)**, structured to support GO annotation review.

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


# InterPro Entry PTHR12064: METAL TRANSPORTER CNNM – Comprehensive Research Report for GO Annotation Review

## Executive Summary

InterPro entry PTHR12064 represents the METAL TRANSPORTER CNNM family, a broadly conserved protein family of integral membrane proteins with ~90,000 sequences spanning bacteria, archaea, and all eukaryotic kingdoms (chen2021crystalstructureof pages 1-2). The family is defined by a conserved structural core comprising a DUF21 transmembrane domain and a CBS-pair (Bateman) domain. Currently, **no InterPro2GO terms are mapped** to this entry. This report evaluates whether GO terms should be added and, if so, which terms are appropriate for family-wide annotation versus subfamily-specific contexts.

---

## 1. Family Definition and Biochemistry

### Structural Architecture and Fold

The CNNM/CorB family possesses a highly conserved structural framework experimentally resolved in archaeal and bacterial orthologs (chen2021crystalstructureof pages 1-2, chen2021crystalstructureof pages 3-5). The core architecture consists of:

1. **DUF21 Transmembrane Domain**: Three transmembrane helices (TM1-3) that form a homodimeric pore structure in an inward-facing conformation (chen2021crystalstructureof pages 1-2, chen2021crystalstructureof pages 3-5). A juxtamembrane (JM) helix wraps around the transmembrane helices in a belt-like structure (chen2021crystalstructureof pages 3-5).

2. **Acidic Helical Bundle (AHB)**: A four-helix bundle with extensive negative charge (13 of 31 residues acidic in archaeal CorB), likely representing cation-binding sites (chen2021crystalstructureof pages 3-5, chen2021crystalstructureof pages 5-6).

3. **CBS-Pair Domain (Bateman Module)**: Composed of tandem CBS motifs that bind Mg²⁺-ATP and undergo conformational changes upon nucleotide binding (chen2021crystalstructureof pages 1-2, chen2021crystalstructureof pages 3-5, chen2021crystalstructureof pages 5-6). This domain mediates dimerization and likely couples Mg-ATP sensing to transport activity.

4. **Lineage-Specific Domains**: Prokaryotic CorB/C proteins possess a C-terminal CorC domain of unknown function, while eukaryotic CNNMs have an N-terminal extracellular region (cleaved signal peptide) and a C-terminal cyclic nucleotide-binding homology (CNBH) domain that does not actually bind cyclic nucleotides but may regulate CBS-pair function (chen2021crystalstructureof pages 1-2, franken2022structuralandfunctional pages 9-11).

| Organism type | Representative proteins | Domain architecture | Conserved residues / motifs for Mg2+ or Mg-ATP binding | Key structural features |
|---|---|---|---|---|
| Bacteria | CorB, CorC orthologs from *Salmonella*, *Tepidiphilus*, *Staphylococcus* | Core CNNM/CorB architecture: 3-TM DUF21 transmembrane domain + juxtamembrane helix + acidic helical bundle (AHB) + CBS-pair (Bateman) domain; prokaryotic CorB additionally has a C-terminal CorC domain | TMD Mg2+-site residues equivalent to Ser21, Ser25, Ser71, Gly110, Glu111 in archaeal CorB are strongly conserved across CNNM/CorB proteins; π-helix region contains invariant/near-invariant Glu111, Ile112, Pro114, Lys115; ATP-binding CBS-pair residues include Thr207, Ser234, Arg235, Phe233, Ile311, Thr313, Asp316 in MtCorB numbering (chen2021crystalstructureof pages 3-5, chen2021crystalstructureof pages 5-6) | DUF21 forms an inward-facing dimer with a large negatively charged cavity; TM3 contains a conserved π-helix that contributes to Mg2+ coordination; liposome assays support direct Mg2+ transport; TtCorB transport appears electroneutral rather than strongly electrogenic (chen2021crystalstructureof pages 3-5, chen2021crystalstructureof pages 6-8) |
| Archaea | MtCorB (*Methanoculleus thermophilus*) | 3-TM DUF21 + belt-like juxtamembrane helix + AHB + CBS-pair domain + C-terminal CorC domain; crystallized in apo and Mg2+-ATP-bound states (chen2021crystalstructureof pages 1-2, chen2021crystalstructureof pages 2-3) | Mg2+ in the TMD cavity is coordinated by Ser21, Ser25, Ser71, Glu111, and the main-chain carbonyls of Ser21 and Gly110; Mg2+-ATP binds in the CBS-pair dimer cavity, with adenine packed by Phe233/Ile311 and phosphates stabilized by Arg235/Ser234 plus Mg2+ in octahedral coordination (chen2021crystalstructureof pages 3-5, chen2021crystalstructureof pages 5-6) | Best-resolved structural model for the family: inward-facing DUF21 dimer, conserved π-helix in TM3, highly acidic AHB, and major CBS-pair/AHB rearrangements between apo and Mg2+-ATP-bound states, consistent with Mg-ATP sensing coupled to transport (chen2021crystalstructureof pages 1-2, chen2021crystalstructureof pages 3-5, chen2021crystalstructureof pages 5-6) |
| Eukaryotes (metazoa) | CNNM1-4 (human/vertebrate CNNMs) | Conserved core shared with CorB: DUF21 TMD + AHB + CBS-pair domain; eukaryotic CNNMs diverge by adding an extracellular N-terminal region/signal peptide and a C-terminal CNBH domain instead of the prokaryotic CorC domain (chen2021crystalstructureof pages 1-2, franken2022structuralandfunctional pages 9-11) | Human CNNM models retain the conserved negatively charged cavity, TM3 π-helix, and Mg2+-site equivalents; disease-linked residues map to conserved structural features, e.g. invariant Glu in the cavity/π-helix region and ATP-binding/dimerization residues such as CNNM2 Thr568 (MtCorB Thr313 equivalent) and CNNM4 Arg407 (MtCorB Arg235 equivalent) (chen2021crystalstructureof pages 6-8, franken2022structuralandfunctional pages 8-9) | CNNMs are structural orthologs of CorB/C and likely use the same DUF21/CBS framework for Mg2+ transport or transport regulation; Mg-ATP binding drives conformational changes in the CBS-pair domain; CNNMs also interact with regulators such as PRLs and TRPM7 in vertebrates (bai2021cnnmproteinsselectively pages 2-3, franken2022structuralandfunctional pages 9-11) |
| Eukaryotes (fungi/plants/other eukaryotes) | Yeast MAM3; plant DUF21-CBS proteins; invertebrate CNNM/UEX-like proteins | Phylogeny supports broad eukaryotic conservation of the CorB/CNNM core; fungal and plant homologs retain DUF21-CBS organization, though accessory regions vary relative to vertebrate CNNMs (chen2021crystalstructureof pages 1-2, bosman2024hypomagnesaemiawithvarying pages 1-2, franken2022structuralandfunctional pages 9-11) | Direct residue-level structural data are sparse for these clades, but comparative analyses indicate conservation of key functional domains and residues across eukaryotic homologs, including DUF21 and CBS-pair features linked to Mg2+ handling (chen2021crystalstructureof pages 3-5, takvam2024differentialregulationof pages 1-2) | Broad taxonomic conservation supports that the structural module predates vertebrates; however, clade-specific accessory domains and regulatory interactions make exact transport mechanism/direction less certain outside structurally characterized CorB and vertebrate CNNMs (chen2021crystalstructureof pages 1-2, takvam2024differentialregulationof pages 1-2, franken2022structuralandfunctional pages 9-11) |


*Table: This table summarizes the conserved domain organization and residue-level structural features of CNNM/CorB family proteins across major clades. It is useful for GO review because it distinguishes family-wide conserved architecture from lineage-specific additions and regulatory specializations.*

### Conserved Catalytic and Binding Residues

**Magnesium Coordination Site** (archaeal MtCorB numbering): The transmembrane cavity contains a conserved Mg²⁺-binding site coordinated by hydroxyl groups of Ser21, Ser25, and Ser71; the carboxyl group of Glu111; and main-chain carbonyls of Ser21 and Gly110 (chen2021crystalstructureof pages 1-2, chen2021crystalstructureof pages 3-5). These polar residues line a large, negatively charged cavity (~10 Å diameter) accessible from the intracellular side (chen2021crystalstructureof pages 3-5).

**π-Helix in TM3**: A conserved structural feature where TM3 adopts an i+5 helical configuration creating a bulge. Residues surrounding this turn (Glu111, Ile112, Pro114, Lys115) are highly conserved from archaea to humans (chen2021crystalstructureof pages 3-5). Glu111 is invariant and coordinates the cavity Mg²⁺ ion, while Pro114 acts as a helix-breaker enabling the π-helical geometry (chen2021crystalstructureof pages 3-5).

**Mg-ATP Binding in CBS-Pair**: In the archaeal structure, two Mg²⁺-ATP molecules bind to the central cavity of the CBS-pair dimer. Adenine bases are sandwiched between Phe233 and Ile311 in a hydrophobic pocket. The ribose interacts with Thr207, Asp316, and Thr313, while phosphates are stabilized by Arg235 and Ser234, with the Mg²⁺ ion octahedrally coordinated (chen2021crystalstructureof pages 5-6). Disease mutations in human CNNM2 (Thr568Ile, equivalent to archaeal Thr313) and CNNM4 (Arg407Leu, equivalent to Arg235) map to these conserved ATP-binding residues (chen2021crystalstructureof pages 5-6, chen2021crystalstructureof pages 6-8).

### Mechanistic Function: Direct Magnesium Transport

A longstanding debate in the field concerns whether CNNM/CorB proteins mediate **direct** Mg²⁺ transport or act as **regulators** of other transporters (bai2021cnnmproteinsselectively pages 2-3, franken2022structuralandfunctional pages 9-11). Recent experimental evidence supports **direct transport**:

- **Liposome-Based Assays**: Reconstitution of archaeal MtCorB and bacterial TtCorB into proteoliposomes with mag-fura-2 (a ratiometric Mg²⁺ indicator) demonstrated time-dependent Mg²⁺ accumulation inside liposomes upon addition of extracellular Mg²⁺, providing direct evidence of transport (chen2021crystalstructureof pages 6-8).

- **Transport Is Protein- and Mg²⁺-Dependent**: Varying protein/lipid ratios and Mg²⁺ concentrations confirmed dose-response relationships (chen2021crystalstructureof pages 6-8).

- **Electroneutral Transport**: Unlike the electrogenic bacterial CorA channel (which showed enhanced transport with valinomycin-generated membrane potential), TtCorB transport was unaffected by membrane potential, suggesting electroneutral Mg²⁺ transport, possibly via Mg²⁺/H⁺ or Mg²⁺/Na⁺ exchange (chen2021crystalstructureof pages 6-8, franken2022structuralandfunctional pages 8-9).

However, the **directionality** (influx versus efflux) and coupling mechanism remain context-dependent and disputed:

- **Prokaryotic Evidence**: In bacteria, CorB/C were originally identified in Mg²⁺ efflux screens; loss-of-function mutants accumulate Mg²⁺ (franken2022structuralandfunctional pages 6-8, franken2022structuralandfunctional pages 8-9).

- **Vertebrate CNNMs – Mixed Evidence**:
  - **CNNM2 and CNNM4** exhibit robust Mg²⁺ extrusion/efflux when overexpressed in cells, consistent with their basolateral epithelial localization in kidney and intestine where Mg²⁺ is extruded to blood (krose2024magnesiumbiology pages 1-2, franken2022structuralandfunctional pages 9-11).
  - **CNNM-TRPM7 Complexes**: CNNMs also selectively bind the TRPM7 Mg²⁺ channel and **stimulate divalent cation influx** (bai2021cnnmproteinsselectively pages 1-2). Knockout of CNNM3/CNNM4 in HEK293 cells reduces TRPM7-mediated Mg²⁺ entry, and overexpression of CNNMs with TRPM7 markedly increases uptake of Mg²⁺, Zn²⁺, and Ca²⁺ (bai2021cnnmproteinsselectively pages 2-3, bai2021cnnmproteinsselectively pages 1-2).
  - **Conclusion**: CNNMs possess both TRPM7-dependent influx-promoting activity and TRPM7-independent Mg²⁺ efflux capacity, indicating they can regulate Mg²⁺ homeostasis bidirectionally depending on cellular context and interacting partners (bai2021cnnmproteinsselectively pages 1-2).

---

## 2. InterPro2GO Mapping Appropriateness

**Current Status**: No GO terms are mapped to PTHR12064.

### Recommended Family-Wide GO Terms

Given the experimental evidence, the following GO terms are **appropriate for family-wide annotation** because they reflect conserved biochemical activities present across prokaryotic and eukaryotic members:

1. **GO:0015095 – Magnesium ion transmembrane transporter activity** (Molecular Function)
   - **Justification**: Liposome assays demonstrate direct Mg²⁺ transport by CorB proteins (chen2021crystalstructureof pages 6-8), and extensive cellular studies support Mg²⁺ transport roles for CNNMs (krose2024magnesiumbiology pages 1-2, franken2022structuralandfunctional pages 9-11).
   - **Caveat**: The exact mechanism (uniport, antiport, symport) and directionality vary by subfamily and context. This term is sufficiently broad to encompass the family's conserved capacity without overspecifying mechanism.

2. **GO:0000287 – Magnesium ion binding** (Molecular Function)
   - **Justification**: Structural data confirm conserved Mg²⁺-binding sites in the transmembrane cavity (coordinated by Ser, Glu residues) and Mg-ATP binding in the CBS-pair domain (chen2021crystalstructureof pages 1-2, chen2021crystalstructureof pages 3-5, chen2021crystalstructureof pages 5-6).

3. **GO:0016020 – Membrane** (Cellular Component)
   - **Justification**: All family members are integral membrane proteins with conserved transmembrane architecture (chen2021crystalstructureof pages 1-2, franken2022structuralandfunctional pages 9-11).

4. **GO:0005524 – ATP binding** (Molecular Function)
   - **Justification**: The CBS-pair domain binds Mg-ATP with high affinity across the family (chen2021crystalstructureof pages 5-6, franken2022structuralandfunctional pages 9-11), and this binding drives conformational changes coupling transport activity to cellular energy status.

### GO Terms That Are INAPPROPRIATE for Family-Wide Annotation

The following terms would **over-annotate** because they are not true for *every* protein matching PTHR12064:

1. **Tissue/Compartment-Specific Terms** (e.g., GO:0005887 – integral component of plasma membrane basolateral region; kidney-specific GO terms)
   - **Reason**: Only subfamily-specific. CNNM2 is basolateral in kidney DCT (krose2024magnesiumbiology pages 1-2, bosman2024hypomagnesaemiawithvarying pages 1-2), CNNM4 is basolateral in intestine/colon (krose2024magnesiumbiology pages 2-3, krose2024magnesiumbiology pages 1-2), but prokaryotic CorB proteins lack tissue compartmentalization, and CNNM localization varies by isoform and species (takvam2024differentialregulationof pages 1-2, franken2022structuralandfunctional pages 9-11).

2. **Process Terms Specific to Nervous System or Development** (e.g., seizure control, intellectual development, brain morphogenesis)
   - **Reason**: These phenotypes are associated with *specific* CNNM2 mutations in vertebrates (bosman2024hypomagnesaemiawithvarying pages 1-2, zhang2021cnnm2relateddisordersphenotype pages 1-2) but are not general properties of the family. Prokaryotic and plant members lack nervous systems, and even vertebrate CNNM4 mutations cause Jalili syndrome (amelogenesis and retinal defects) without hypomagnesemia or neurological phenotype (franken2022structuralandfunctional pages 9-11).

3. **Directional Transport Terms** (e.g., "magnesium ion export" or "import")
   - **Reason**: Direction is **context-dependent** and varies among family members. Bacterial CorB/C mediate efflux (franken2022structuralandfunctional pages 6-8, franken2022structuralandfunctional pages 8-9), vertebrate CNNM2/CNNM4 show efflux in epithelial cells (krose2024magnesiumbiology pages 1-2, franken2022structuralandfunctional pages 9-11), but CNNMs also promote TRPM7-mediated influx in other contexts (bai2021cnnmproteinsselectively pages 1-2). A directionally neutral term like "magnesium ion transmembrane transporter activity" is more accurate family-wide.

4. **Generic Terms That Add Little Information** (e.g., "metal ion binding," "membrane")
   - **Status**: While technically correct, GO:0046872 (metal ion binding) is less informative than the more specific GO:0000287 (magnesium ion binding). The family's specificity for Mg²⁺ justifies the more precise term (chen2021crystalstructureof pages 1-2, krose2024magnesiumbiology pages 1-2).

---

## 3. Functional Divergence Across the Family

The CNNM/CorB family exhibits **substantial functional divergence** among subfamilies, driven by gene duplication, subfunctionalization, and neo-functionalization events.

### Vertebrate CNNM1-4 Isoforms

| CNNM isoform | Tissue expression / localization in vertebrates | Transport function / mechanistic status | Associated disease or phenotype links | Key references showing functional differences |
|---|---|---|---|---|
| CNNM1 | Present in vertebrates and detected as a TRPM7-complex component in rodent brain; in teleost kidney literature, CNNM1 family members are discussed as distinct from CNNM2/3/4 and may be recruited in lineage-specific renal regulation (kollewe2021themolecularappearance pages 1-5, takvam2024differentialregulationof pages 1-2) | Family-level function is inferred as Mg2+-homeostasis related, but isoform-specific direct transport evidence is weaker than for CNNM2/4; likely participates in CNNM/TRPM7 regulatory complexes in some tissues rather than being securely assignable as a universal standalone Mg2+ exporter/importer (bai2021cnnmproteinsselectively pages 1-2, kollewe2021themolecularappearance pages 1-5, franken2022structuralandfunctional pages 9-11) | No single defining Mendelian vertebrate syndrome was identified in the retrieved sources; functional specialization remains less resolved than for CNNM2 and CNNM4 (franken2022structuralandfunctional pages 9-11) | Bai et al. 2021 for CNNM family interaction with TRPM7; Kollewe et al. 2021 for native TRPM7/CNNM1-4 complexes; Takvam et al. 2024 for vertebrate paralog diversification (bai2021cnnmproteinsselectively pages 1-2, kollewe2021themolecularappearance pages 1-5, takvam2024differentialregulationof pages 1-2) |
| CNNM2 | Prominently expressed in kidney distal convoluted tubule and brain; basolateral role in renal Mg2+ handling is emphasized in renal physiology reviews and clinical studies (bosman2024hypomagnesaemiawithvarying pages 1-2, krose2024magnesiumbiology pages 1-2, gimenezmascarell2018novelaspectsof pages 1-2, franken2022structuralandfunctional pages 9-11) | Best-supported vertebrate CNNM for systemic Mg2+ homeostasis. Reported as a basolateral Mg2+ extrusion/efflux factor in epithelia and as a direct or putative transporter in several systems, but the field remains debated; also may regulate or cooperate with TRPM7-dependent divalent cation influx in some cellular contexts (bai2021cnnmproteinsselectively pages 2-3, bai2021cnnmproteinsselectively pages 1-2, franken2022structuralandfunctional pages 9-11) | Heterozygous and recessive variants cause hypomagnesemia, often with seizures and intellectual disability/developmental delay; knockout causes severe developmental phenotypes and lethality in mice (bosman2024hypomagnesaemiawithvarying pages 1-2, zhang2021cnnm2relateddisordersphenotype pages 1-2, franken2022structuralandfunctional pages 9-11) | Bosman et al. 2024; Zhang et al. 2021; Kröse and de Baaij 2024; Franken et al. 2022 (bosman2024hypomagnesaemiawithvarying pages 1-2, zhang2021cnnm2relateddisordersphenotype pages 1-2, krose2024magnesiumbiology pages 1-2, franken2022structuralandfunctional pages 9-11) |
| CNNM3 | Broadly expressed; endogenous CNNM3 detected with TRPM7 in HEK293 and in native TRPM7 complexes; in salmonids, cnnm3 paralogs are salinity-responsive in kidney, supporting regulatory divergence within vertebrates (bai2021cnnmproteinsselectively pages 2-3, kollewe2021themolecularappearance pages 1-5, takvam2024differentialregulationof pages 1-2) | Frequently discussed as a Mg2+-homeostasis protein with disputed directionality. Strong evidence supports participation in CNNM/TRPM7 complexes that stimulate divalent cation entry; separate TRPM7-independent Mg2+ efflux activity has also been proposed for CNNM family members, including CNNM3-related contexts (bai2021cnnmproteinsselectively pages 1-2, bai2021cnnmproteinsselectively pages 2-3) | Associated with oncogenic PRL-CNNM biology rather than a classic inherited Mg-wasting syndrome in the cited sources; kidney/osmoregulatory recruitment in fish suggests subfunctionalization among vertebrate paralogs (bai2021cnnmproteinsselectively pages 2-3, takvam2024differentialregulationof pages 1-2, franken2022structuralandfunctional pages 9-11) | Bai et al. 2021; Takvam et al. 2024; Franken et al. 2022 (bai2021cnnmproteinsselectively pages 1-2, takvam2024differentialregulationof pages 1-2, franken2022structuralandfunctional pages 9-11) |
| CNNM4 | Expressed in intestine/colon basolateral membrane for transepithelial Mg2+ absorption; also implicated in vertebrate tissues including retina/tooth-related disease contexts and detected in TRPM7 complexes (krose2024magnesiumbiology pages 2-3, krose2024magnesiumbiology pages 1-2, bai2021cnnmproteinsselectively pages 2-3, kollewe2021themolecularappearance pages 1-5, franken2022structuralandfunctional pages 9-11) | Along with CNNM2, has some of the strongest evidence for epithelial Mg2+ efflux/extrusion activity; in colon, proposed basolateral Na+-dependent Mg2+ extrusion role. Also participates in CNNM-TRPM7 complexes that can promote divalent cation influx, illustrating context-dependent behavior (krose2024magnesiumbiology pages 2-3, bai2021cnnmproteinsselectively pages 1-2, franken2022structuralandfunctional pages 9-11) | Jalili syndrome due to CNNM4 variants; mouse loss causes intestinal Mg2+ malabsorption/hypomagnesemia and infertility, but human Jalili syndrome is dominated by amelogenesis and cone-rod dystrophy rather than a uniform systemic Mg phenotype (bai2021cnnmproteinsselectively pages 2-3, franken2022structuralandfunctional pages 9-11) | Kröse and de Baaij 2024; Bai et al. 2021; Franken et al. 2022 (krose2024magnesiumbiology pages 2-3, bai2021cnnmproteinsselectively pages 1-2, franken2022structuralandfunctional pages 9-11) |


*Table: This table summarizes how CNNM1-4 differ in vertebrate tissue distribution, mechanistic interpretation, and phenotype associations. It is useful for GO review because it shows that family-wide functional assignments beyond broad Mg2+-homeostasis are not uniformly supported across all isoforms.*

**Key Observations**:

- **CNNM2**: Predominantly expressed in kidney distal convoluted tubule (DCT) and brain. Heterozygous and recessive loss-of-function variants cause renal Mg²⁺ wasting with hypomagnesemia, and in many cases seizures and intellectual disability (HSMR syndrome) (bosman2024hypomagnesaemiawithvarying pages 1-2, zhang2021cnnm2relateddisordersphenotype pages 1-2). Knockout mice are embryonic lethal or develop exencephaly and severe hypomagnesemia (franken2022structuralandfunctional pages 9-11). Variants cluster in the DUF21 domain for neurological phenotypes, while CBS2 domain variants correlate with more severe hypomagnesemia (zhang2021cnnm2relateddisordersphenotype pages 1-2).

- **CNNM4**: Expressed in intestine (colon basolateral membrane) and is required for intestinal Mg²⁺ absorption. Knockout mice develop hypomagnesemia due to intestinal malabsorption and male infertility (franken2022structuralandfunctional pages 9-11). Intriguingly, human CNNM4 mutations cause **Jalili syndrome** (amelogenesis imperfecta and cone-rod dystrophy) *without* consistent systemic hypomagnesemia, indicating tissue-specific functional requirements not reflected by systemic Mg²⁺ levels (bai2021cnnmproteinsselectively pages 2-3, franken2022structuralandfunctional pages 9-11).

- **CNNM3**: Broadly expressed and forms complexes with TRPM7 in multiple cell types (bai2021cnnmproteinsselectively pages 1-2, kollewe2021themolecularappearance pages 1-5). Its function is less well-defined than CNNM2/4, but it is implicated in oncogenesis via interactions with PRL phosphatases (bai2021cnnmproteinsselectively pages 2-3, franken2022structuralandfunctional pages 9-11). In teleost fish, cnnm3 paralogs show salinity-responsive regulation in kidney, supporting subfunctionalization after whole-genome duplication (takvam2024differentialregulationof pages 1-2).

- **CNNM1**: Detected in TRPM7 complexes in brain (kollewe2021themolecularappearance pages 1-5), but specific transport activity and disease associations are less clear. In salmonids, cnnm1 paralogs are differentially regulated, suggesting lineage-specific innovations (takvam2024differentialregulationof pages 1-2).

**Evolutionary Perspective**: Salmonid-specific whole genome duplication (Ss4R ~50-80 million years ago) generated multiple CNNM paralogs that exhibit **selective retention** (25-75% retention of duplicates) and **differential regulation** in response to environmental salinity (takvam2024differentialregulationof pages 1-2). This indicates neo- and/or subfunctionalization: for example, slc41a1-1, cnnm4a1, cnnm4a2, and trpm7-2 are upregulated during parr-smolt transformation preparing for seawater migration, while cnnm3-1 and cnnm3-2 are only upregulated after seawater exposure (takvam2024differentialregulationof pages 1-2). Such isoform-specific responses argue against a single, uniform function assignable to all CNNM proteins.

### Catalytically Dead or Pseudo-Transporter Members?

**No evidence** for catalytically inactive "pseudo-enzyme" paralogs retaining the fold without activity was found in the retrieved literature. Disease-causing mutations (e.g., CNNM2 Glu357Lys, a charge reversal of the invariant Mg²⁺-coordinating glutamate) likely abolish transport but also cause pathology, not a tolerated inactive form (chen2021crystalstructureof pages 6-8). All functional CNNM/CorB members retain the conserved Mg²⁺-binding site and CBS-pair architecture.

---

## 4. Taxonomic Scope

### Distribution Across All Kingdoms

CNNM/CorB proteins are among the most evolutionarily ancient and broadly distributed transporter families, with **close to 90,000 sequences** known spanning all domains of life (chen2021crystalstructureof pages 1-2).

- **Bacteria**: CorB/C found in *Salmonella*, *Staphylococcus*, *Bacillus*, *Tepidiphilus*, and many others. Bacterial CorB proteins mediate Mg²⁺ efflux and are often upregulated under high Mg²⁺ stress (chen2021crystalstructureof pages 1-2, franken2022structuralandfunctional pages 6-8, franken2022structuralandfunctional pages 8-9).

- **Archaea**: Archaeal orthologs (e.g., *Methanoculleus thermophilus*, *Thermococcus kodakarensis*) retain the conserved DUF21-CBS architecture. The archaeal MtCorB crystal structure is the best-resolved example of the family fold (chen2021crystalstructureof pages 1-2, chen2021crystalstructureof pages 3-5).

- **Eukaryotes**:
  - **Fungi**: Yeast *Saccharomyces cerevisiae* expresses MAM3, a CNNM ortholog localized to mitochondria or other compartments (franken2022structuralandfunctional pages 1-2, franken2022structuralandfunctional pages 9-11).
  - **Plants**: *Arabidopsis thaliana* has multiple DUF21-CBS proteins (CBSDUF1, CBSDUFCH2) (chen2021crystalstructureof pages 1-2, franken2022structuralandfunctional pages 1-2). Phylogenetic data show plant CNNM homologs, though specific functional studies are limited.
  - **Metazoa**: Present in invertebrates (e.g., *Drosophila melanogaster* UEX, *Caenorhabditis elegans* cnnm-1) and all vertebrates (fish, amphibians, reptiles, birds, mammals) (franken2022structuralandfunctional pages 1-2, chen2021crystalstructureof pages 1-2).

### Conservation of Function Across Taxa

**Conserved**: The **core Mg²⁺ transport/homeostasis function** is retained across all kingdoms, as evidenced by:
- Complementation experiments where bacterial CorB can partially rescue yeast Mrs2-deficient phenotypes in some contexts (franken2022structuralandfunctional pages 1-2, franken2022structuralandfunctional pages 4-6).
- Homology in the Mg²⁺-binding cavity, π-helix, and CBS-pair Mg-ATP sensing (chen2021crystalstructureof pages 1-2, chen2021crystalstructureof pages 3-5).

**Variable**: The **directionality** (influx vs. efflux), **coupling mechanism** (uniport, Na⁺ or H⁺ antiport), and **regulatory context** differ by lineage and isoform:
- Prokaryotic CorB/C: primarily efflux (franken2022structuralandfunctional pages 6-8, franken2022structuralandfunctional pages 8-9).
- Vertebrate CNNMs: bidirectional depending on cellular context and interaction with TRPM7 or PRL phosphatases (bai2021cnnmproteinsselectively pages 1-2, franken2022structuralandfunctional pages 9-11).

**Pathway/Compartment Terms**: GO process or component terms describing specific tissues (kidney, intestine), developmental processes (brain morphogenesis), or disease phenotypes (seizures) are **not** conserved across taxa. Prokaryotes and plants lack these compartments, and even among vertebrates, CNNM isoforms have non-overlapping tissue distributions and phenotypes (krose2024magnesiumbiology pages 1-2, bosman2024hypomagnesaemiawithvarying pages 1-2, takvam2024differentialregulationof pages 1-2, franken2022structuralandfunctional pages 9-11).

---

## 5. Over-Annotation Verdict and Recommended GO Action

### Summary: InterPro2GO Mapping for PTHR12064

**Current Status**: No GO terms mapped.

**Verdict**: **Partially ACCEPT with recommendations for specific, conserved GO terms only.**

The CNNM/CorB family is **functionally homogeneous** at the level of core biochemistry (Mg²⁺ binding, Mg-ATP sensing, membrane transport) but **functionally divergent** at the level of tissue localization, directionality, regulatory mechanisms, and associated phenotypes. Therefore:

1. **ACCEPT** the following **family-wide GO terms** as appropriate for *every* protein matching PTHR12064:
   - **GO:0015095** (magnesium ion transmembrane transporter activity) – Molecular Function
   - **GO:0000287** (magnesium ion binding) – Molecular Function
   - **GO:0005524** (ATP binding) – Molecular Function
   - **GO:0016020** (membrane) – Cellular Component

2. **REJECT** or **DEMOTE to KEEP_AS_NON_CORE** the following types of terms because they are subfamily-specific or context-dependent:
   - Directional transport terms (import/export) – direction varies by isoform and context.
   - Tissue/compartment-specific terms (kidney, intestine, basolateral membrane) – only apply to specific vertebrate isoforms, not prokaryotic or plant members.
   - Process terms related to nervous system, development, or disease (seizures, intellectual disability, amelogenesis) – phenotypes of specific CNNM2/CNNM4 mutations, not general family properties.
   - Overly generic terms (metal ion binding) when a more specific term (magnesium ion binding) is justified.

3. **Recommendation for Subfamily Annotation**: If InterPro or GO consortia wish to annotate subfamily-specific functions, these should be assigned to **child InterPro entries** or **specific PANTHER subfamilies** (e.g., CNNM2-specific, CNNM4-specific) rather than to the family-level entry PTHR12064. For example:
   - A CNNM2-specific child entry could include GO terms for kidney DCT localization and renal Mg²⁺ reabsorption.
   - A CNNM4-specific child entry could include intestinal Mg²⁺ absorption.

### Recommended GO Action Pattern

- **For PTHR12064 (family level)**: **MODIFY-to-specific** – Add the four conserved GO terms listed above (Mg²⁺ transporter activity, Mg²⁺ binding, ATP binding, membrane). Do not add tissue, disease, or directional terms.

- **For hypothetical subfamily entries** (if created): **ACCEPT** isoform-specific GO terms (e.g., kidney localization for CNNM2 subfamily, intestinal localization for CNNM4 subfamily), but ensure these are clearly demarcated as not applying family-wide.

### Note to InterPro Curators

The entry type is **family**, which is more appropriate for whole-protein function terms than a domain or homologous_superfamily entry. However, given the 13,041 proteins across 9,306 taxa and 30 subfamilies, this family exhibits considerable functional heterogeneity. The core conserved function (Mg²⁺ transport/homeostasis via a DUF21-CBS architecture) justifies family-level GO terms for the fundamental biochemical activity, but tissue-specific and phenotype-specific terms should be reserved for subfamilies. The lack of current InterPro2GO terms suggests previous curators recognized this complexity; the present analysis supports adding **conserved biochemical terms only** to avoid over-annotation.

---

## References (Cited Sources)

All major claims in this report are supported by primary literature and authoritative reviews published 2018-2024:

- **Structural studies**: Chen et al. 2021 (archaeal CorB crystal structure, liposome transport assays) – (chen2021crystalstructureof pages 1-2, chen2021crystalstructureof pages 3-5, chen2021crystalstructureof pages 5-6, chen2021crystalstructureof pages 6-8)
- **Evolutionary and comparative analyses**: Franken et al. 2022 (structural and functional comparison of Mg transporters throughout evolution) – (franken2022structuralandfunctional pages 1-2, franken2022structuralandfunctional pages 4-6, franken2022structuralandfunctional pages 6-8, franken2022structuralandfunctional pages 8-9, franken2022structuralandfunctional pages 9-11)
- **Functional and interaction studies**: Bai et al. 2021 (CNNM-TRPM7 complexes) – (bai2021cnnmproteinsselectively pages 2-3, bai2021cnnmproteinsselectively pages 1-2)
- **Clinical and phenotypic analyses**: Bosman et al. 2024, Zhang et al. 2021 (CNNM2-related disorders) – (bosman2024hypomagnesaemiawithvarying pages 1-2, zhang2021cnnm2relateddisordersphenotype pages 1-2)
- **Recent reviews**: Kröse & de Baaij 2024 (magnesium biology and renal/intestinal homeostasis) – (krose2024magnesiumbiology pages 2-3, krose2024magnesiumbiology pages 1-2)
- **Evolutionary diversification**: Takvam et al. 2024 (salmonid Mg transporter paralogs and salinity adaptation) – (takvam2024differentialregulationof pages 1-2)
- **Proteomics and native complexes**: Kollewe et al. 2021 (native TRPM7-CNNM1-4 complexes in brain) – (kollewe2021themolecularappearance pages 1-5)
- **Additional structural and mechanistic context**: Giménez-Mascarell et al. 2018 (renal Mg homeostasis) – (gimenezmascarell2018novelaspectsof pages 1-2)

Publication dates: 2018–2024, with priority given to 2023-2024 sources where available.

References

1. (chen2021crystalstructureof pages 1-2): Yu Seby Chen, Guennadi Kozlov, Brandon E. Moeller, Ahmed Rohaim, Rayan Fakih, Benoît Roux, John E. Burke, and Kalle Gehring. Crystal structure of an archaeal corb magnesium transporter. Nature Communications, Jun 2021. URL: https://doi.org/10.1038/s41467-021-24282-7, doi:10.1038/s41467-021-24282-7. This article has 52 citations and is from a highest quality peer-reviewed journal.

2. (chen2021crystalstructureof pages 3-5): Yu Seby Chen, Guennadi Kozlov, Brandon E. Moeller, Ahmed Rohaim, Rayan Fakih, Benoît Roux, John E. Burke, and Kalle Gehring. Crystal structure of an archaeal corb magnesium transporter. Nature Communications, Jun 2021. URL: https://doi.org/10.1038/s41467-021-24282-7, doi:10.1038/s41467-021-24282-7. This article has 52 citations and is from a highest quality peer-reviewed journal.

3. (chen2021crystalstructureof pages 5-6): Yu Seby Chen, Guennadi Kozlov, Brandon E. Moeller, Ahmed Rohaim, Rayan Fakih, Benoît Roux, John E. Burke, and Kalle Gehring. Crystal structure of an archaeal corb magnesium transporter. Nature Communications, Jun 2021. URL: https://doi.org/10.1038/s41467-021-24282-7, doi:10.1038/s41467-021-24282-7. This article has 52 citations and is from a highest quality peer-reviewed journal.

4. (franken2022structuralandfunctional pages 9-11): G. A. C. Franken, M. A. Huynen, L. A. Martínez-Cruz, R. J. M. Bindels, and J. H. F. de Baaij. Structural and functional comparison of magnesium transporters throughout evolution. Cellular and Molecular Life Sciences: CMLS, Jul 2022. URL: https://doi.org/10.1007/s00018-022-04442-8, doi:10.1007/s00018-022-04442-8. This article has 85 citations.

5. (chen2021crystalstructureof pages 6-8): Yu Seby Chen, Guennadi Kozlov, Brandon E. Moeller, Ahmed Rohaim, Rayan Fakih, Benoît Roux, John E. Burke, and Kalle Gehring. Crystal structure of an archaeal corb magnesium transporter. Nature Communications, Jun 2021. URL: https://doi.org/10.1038/s41467-021-24282-7, doi:10.1038/s41467-021-24282-7. This article has 52 citations and is from a highest quality peer-reviewed journal.

6. (chen2021crystalstructureof pages 2-3): Yu Seby Chen, Guennadi Kozlov, Brandon E. Moeller, Ahmed Rohaim, Rayan Fakih, Benoît Roux, John E. Burke, and Kalle Gehring. Crystal structure of an archaeal corb magnesium transporter. Nature Communications, Jun 2021. URL: https://doi.org/10.1038/s41467-021-24282-7, doi:10.1038/s41467-021-24282-7. This article has 52 citations and is from a highest quality peer-reviewed journal.

7. (franken2022structuralandfunctional pages 8-9): G. A. C. Franken, M. A. Huynen, L. A. Martínez-Cruz, R. J. M. Bindels, and J. H. F. de Baaij. Structural and functional comparison of magnesium transporters throughout evolution. Cellular and Molecular Life Sciences: CMLS, Jul 2022. URL: https://doi.org/10.1007/s00018-022-04442-8, doi:10.1007/s00018-022-04442-8. This article has 85 citations.

8. (bai2021cnnmproteinsselectively pages 2-3): Zhiyong Bai, Jianlin Feng, Gijs A. C. Franken, Namariq Al’Saadi, Na Cai, Albert S. Yu, Liping Lou, Yuko Komiya, Joost G. J. Hoenderop, Jeroen H. F. de Baaij, Lixia Yue, and Loren W. Runnels. Cnnm proteins selectively bind to the trpm7 channel to stimulate divalent cation entry into cells. Dec 2021. URL: https://doi.org/10.1371/journal.pbio.3001496, doi:10.1371/journal.pbio.3001496. This article has 59 citations and is from a highest quality peer-reviewed journal.

9. (bosman2024hypomagnesaemiawithvarying pages 1-2): Willem Bosman, Gijs A. C. Franken, Javier de las Heras, Leire Madariaga, Tahsin Stefan Barakat, Rianne Oostenbrink, Marjon van Slegtenhorst, Ana Perdomo-Ramírez, Félix Claverie-Martín, Albertien M. van Eerde, Rosa Vargas-Poussou, Laurence Derain Dubourg, Irene González-Recio, Luis Alfonso Martínez-Cruz, Jeroen H. F. de Baaij, and Joost G. J. Hoenderop. Hypomagnesaemia with varying degrees of extrarenal symptoms as a consequence of heterozygous cnnm2 variants. Scientific Reports, Mar 2024. URL: https://doi.org/10.1038/s41598-024-57061-7, doi:10.1038/s41598-024-57061-7. This article has 2 citations and is from a peer-reviewed journal.

10. (takvam2024differentialregulationof pages 1-2): Marius Takvam, Elsa Denker, Naouel Gharbi, Valentina Tronci, Jelena Kolarevic, and Tom Ole Nilsen. Differential regulation of magnesium transporters slc41, cnnm and trpm6-7 in the kidney of salmonids may represent evolutionary adaptations to high salinity environments. BMC Genomics, Nov 2024. URL: https://doi.org/10.1186/s12864-024-11055-x, doi:10.1186/s12864-024-11055-x. This article has 0 citations and is from a peer-reviewed journal.

11. (franken2022structuralandfunctional pages 6-8): G. A. C. Franken, M. A. Huynen, L. A. Martínez-Cruz, R. J. M. Bindels, and J. H. F. de Baaij. Structural and functional comparison of magnesium transporters throughout evolution. Cellular and Molecular Life Sciences: CMLS, Jul 2022. URL: https://doi.org/10.1007/s00018-022-04442-8, doi:10.1007/s00018-022-04442-8. This article has 85 citations.

12. (krose2024magnesiumbiology pages 1-2): Jana L Kröse and Jeroen H F de Baaij. Magnesium biology. Nephrology Dialysis Transplantation, 39:1965-1975, Jun 2024. URL: https://doi.org/10.1093/ndt/gfae134, doi:10.1093/ndt/gfae134. This article has 67 citations and is from a domain leading peer-reviewed journal.

13. (bai2021cnnmproteinsselectively pages 1-2): Zhiyong Bai, Jianlin Feng, Gijs A. C. Franken, Namariq Al’Saadi, Na Cai, Albert S. Yu, Liping Lou, Yuko Komiya, Joost G. J. Hoenderop, Jeroen H. F. de Baaij, Lixia Yue, and Loren W. Runnels. Cnnm proteins selectively bind to the trpm7 channel to stimulate divalent cation entry into cells. Dec 2021. URL: https://doi.org/10.1371/journal.pbio.3001496, doi:10.1371/journal.pbio.3001496. This article has 59 citations and is from a highest quality peer-reviewed journal.

14. (krose2024magnesiumbiology pages 2-3): Jana L Kröse and Jeroen H F de Baaij. Magnesium biology. Nephrology Dialysis Transplantation, 39:1965-1975, Jun 2024. URL: https://doi.org/10.1093/ndt/gfae134, doi:10.1093/ndt/gfae134. This article has 67 citations and is from a domain leading peer-reviewed journal.

15. (zhang2021cnnm2relateddisordersphenotype pages 1-2): Han Zhang, Ye Wu, and Yuwu Jiang. Cnnm2-related disorders: phenotype and its severity were associated with the mode of inheritance. Frontiers in Pediatrics, Sep 2021. URL: https://doi.org/10.3389/fped.2021.699568, doi:10.3389/fped.2021.699568. This article has 9 citations.

16. (kollewe2021themolecularappearance pages 1-5): Astrid Kollewe, Vladimir Chubanov, Fong Tsuen Tseung, Alexander Haupt, Catrin Swantje Müller, Wolfgang Bildl, Uwe Schulte, Annette Nicke, Bernd Fakler, and Thomas Gudermann. The molecular appearance of native trpm7 channel complexes identified by high-resolution proteomics. eLife, Jul 2021. URL: https://doi.org/10.1101/2021.07.09.451738, doi:10.1101/2021.07.09.451738. This article has 63 citations and is from a domain leading peer-reviewed journal.

17. (gimenezmascarell2018novelaspectsof pages 1-2): Paula Giménez-Mascarell, Carlotta Else Schirrmacher, Luis Alfonso Martínez-Cruz, and Dominik Müller. Novel aspects of renal magnesium homeostasis. Frontiers in Pediatrics, Apr 2018. URL: https://doi.org/10.3389/fped.2018.00077, doi:10.3389/fped.2018.00077. This article has 57 citations.

18. (franken2022structuralandfunctional pages 1-2): G. A. C. Franken, M. A. Huynen, L. A. Martínez-Cruz, R. J. M. Bindels, and J. H. F. de Baaij. Structural and functional comparison of magnesium transporters throughout evolution. Cellular and Molecular Life Sciences: CMLS, Jul 2022. URL: https://doi.org/10.1007/s00018-022-04442-8, doi:10.1007/s00018-022-04442-8. This article has 85 citations.

19. (franken2022structuralandfunctional pages 4-6): G. A. C. Franken, M. A. Huynen, L. A. Martínez-Cruz, R. J. M. Bindels, and J. H. F. de Baaij. Structural and functional comparison of magnesium transporters throughout evolution. Cellular and Molecular Life Sciences: CMLS, Jul 2022. URL: https://doi.org/10.1007/s00018-022-04442-8, doi:10.1007/s00018-022-04442-8. This article has 85 citations.

## Artifacts

- [Edison artifact artifact-00](PTHR12064-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR12064-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. chen2021crystalstructureof pages 1-2
2. chen2021crystalstructureof pages 3-5
3. chen2021crystalstructureof pages 5-6
4. chen2021crystalstructureof pages 6-8
5. bai2021cnnmproteinsselectively pages 1-2
6. franken2022structuralandfunctional pages 9-11
7. takvam2024differentialregulationof pages 1-2
8. kollewe2021themolecularappearance pages 1-5
9. gimenezmascarell2018novelaspectsof pages 1-2
10. chen2021crystalstructureof pages 2-3
11. franken2022structuralandfunctional pages 8-9
12. bai2021cnnmproteinsselectively pages 2-3
13. bosman2024hypomagnesaemiawithvarying pages 1-2
14. franken2022structuralandfunctional pages 6-8
15. krose2024magnesiumbiology pages 1-2
16. krose2024magnesiumbiology pages 2-3
17. franken2022structuralandfunctional pages 1-2
18. franken2022structuralandfunctional pages 4-6
19. https://doi.org/10.1038/s41467-021-24282-7,
20. https://doi.org/10.1007/s00018-022-04442-8,
21. https://doi.org/10.1371/journal.pbio.3001496,
22. https://doi.org/10.1038/s41598-024-57061-7,
23. https://doi.org/10.1186/s12864-024-11055-x,
24. https://doi.org/10.1093/ndt/gfae134,
25. https://doi.org/10.3389/fped.2021.699568,
26. https://doi.org/10.1101/2021.07.09.451738,
27. https://doi.org/10.3389/fped.2018.00077,