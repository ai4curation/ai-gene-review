---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-21T20:17:52.831079'
end_time: '2026-06-21T20:28:48.878035'
duration_seconds: 656.05
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR11814
  interpro_name: SULFATE TRANSPORTER
  interpro_short_name: Not specified
  interpro_type: family
  interpro_integrated: IPR001902
  member_databases: Not specified
  n_proteins: '53835'
  n_taxa: '25803'
  n_subfamilies: '77'
  interpro2go_terms: None mapped (no InterPro2GO terms for this entry)
  interpro_description: Not specified in InterPro
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 21
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PTHR11814-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR11814-deep-research-falcon_artifacts/artifact-01.md
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
- **Accession:** PTHR11814
- **Name:** SULFATE TRANSPORTER
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** IPR001902
- **Member database signatures:** Not specified
- **Scale:** 53835 proteins across 25803 taxa, 77 subfamilies
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
**PTHR11814 (SULFATE TRANSPORTER)**, structured to support GO annotation review.

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
- **Accession:** PTHR11814
- **Name:** SULFATE TRANSPORTER
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** IPR001902
- **Member database signatures:** Not specified
- **Scale:** 53835 proteins across 25803 taxa, 77 subfamilies
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
**PTHR11814 (SULFATE TRANSPORTER)**, structured to support GO annotation review.

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


# Comprehensive Research Report: InterPro Entry PTHR11814 (SULFATE TRANSPORTER)

## Executive Summary

PTHR11814 represents an extremely large and functionally heterogeneous protein family (53,835 proteins across 25,803 taxa, 77 subfamilies) encompassing sulfate transporters and related anion transport proteins across bacteria, plants, and animals. The current absence of InterPro2GO mappings to this entry is **scientifically sound and should be maintained**. Any attempt to apply family-wide GO terms would result in systematic over-annotation due to radical functional divergence spanning substrate specificity (sulfate vs. chloride vs. bicarbonate vs. phosphate vs. iodide), transport mechanism (symport vs. exchange vs. channel vs. motor protein), and subcellular localization (plasma membrane vs. tonoplast vs. lysosomal).

---

## 1. Family Definition and Biochemistry

### Molecular Architecture and Fold

PTHR11814 members share a conserved structural architecture first identified in the prokaryotic uracil transporter UraA and subsequently characterized in multiple SLC26 family members through high-resolution cryo-electron microscopy studies from 2023-2025 (hu2024substratebindingplasticity pages 1-2, tippett2023structuralandfunctional pages 1-2, wang2024mechanismofanion pages 1-2). The canonical architecture comprises:

**Transmembrane Domain (TMD):** 12-14 transmembrane helices organized into two functional subdomains with pseudo-two-fold symmetry (tippett2023structuralandfunctional pages 1-2, hu2024substratebindingplasticity pages 1-2). The **core domain** (helices 1-4, 8-11) forms a compact mobile unit housing the primary substrate-binding site, while the **gate/scaffold domain** (helices 5-7, 12-14) provides a rigid framework that shields one face of the core domain during transport (tippett2023structuralandfunctional pages 1-2, tippett2023structuralandfunctional pages 2-3). This arrangement supports an elevator-type transport mechanism in which the core domain undergoes rigid-body translocation relative to the gate domain to alternately expose the substrate-binding site to opposite sides of the membrane (hu2024substratebindingplasticity pages 1-2, tippett2023structuralandfunctional pages 1-2).

**STAS Domain:** The C-terminal Sulfate Transporter and Anti-Sigma factor antagonist (STAS) domain is cytosolic and mediates homodimerization in mammalian SLC26 proteins, with each protomer's STAS domain interacting with the transmembrane region of the opposite protomer (tippett2023structuralandfunctional pages 1-2, wang2024mechanismofanion pages 1-2, seidler2025theenigmaticslc26a6 pages 1-2). The STAS domain also appears to play regulatory roles in coupling transport activity, though precise mechanisms vary among subfamilies (wang2024mechanismofanion pages 1-2, kuhn2025slc26a11isan pages 1-4).

> Sulfate transporter family members characterized structurally in plants and animals share a conserved membrane architecture built on a UraA-like fold, with transmembrane helices organized into a mobile core domain and a more static gate/scaffold domain that support elevator-type transport. In SLC26 proteins, this transmembrane unit is followed by a cytosolic STAS domain that contributes to dimerization and regulatory coupling to the membrane domain; related sulfate transporters in plants retain the same core transport architecture despite lineage-specific specialization (hu2024substratebindingplasticity pages 1-2, tippett2023structuralandfunctional pages 1-2, wang2024mechanismofanion pages 1-2).
>
> In the plant sulfate transporter structural framework derived from AtSULTR4.1, the proton-coupled transport residue Glu347 is conserved across SULTRs, while key sulfate-binding pocket residues Gln112, Tyr116, Ser392, and Arg/Lys393 are also strongly conserved. Mutational analysis cited in the phylogenetic/structural study reports that alanine substitution at these positions causes near-total loss of sulfate transport activity, supporting their central role in substrate coordination and coupling (surber2025anupdatedsulfate pages 10-13).
>
> Recent cryo-EM work on mammalian SLC26A2 further supports a conserved family logic in which the substrate translocation pathway lies at the interface between core and gate domains, with the core domain carrying the principal anion-binding region and moving relative to the scaffold during transport. Comparable structural principles are described for SLC26A6 and pendrin, reinforcing that shared fold does not imply identical substrate preference or transport stoichiometry (hu2024substratebindingplasticity pages 1-2, tippett2023structuralandfunctional pages 1-2, wang2024mechanismofanion pages 1-2).
>
> Subfamily-specific substitutions in the conserved binding-pocket environment appear to help drive neofunctionalization. In plants, the SULTR3 lineages preserve the overall fold but alter pocket residues: Ala153 is replaced by Ser in SULTR3.3/SULTR3.4, while Ser390 is replaced by Pro in SULTR3.1/SULTR3.5 or by Ala in SULTR3.3. In SULTR3.4, the resulting Ser153-Ser390-Ser392 arrangement is predicted to form a serine triad that better stabilizes phosphate, providing a structural explanation for the experimentally supported shift of SULTR3.4 from sulfate-family ancestry toward phosphate transport (surber2025anupdatedsulfate pages 10-13, surber2025anupdatedsulfate pages 1-4).
>
> The main annotation implication is that conserved architecture and partially conserved substrate-coordinating residues are sufficient to support homology to the sulfate transporter superfamily, but not a single family-wide molecular function. The same fold supports sulfate transporters, chloride/bicarbonate exchangers, chloride channels, and even highly specialized derivatives, so residue-level conservation must be interpreted together with subfamily context before assigning GO terms (li2025structuralbasisfor pages 1-2, wang2024mechanismofanion pages 1-2, kuhn2025slc26a11isan pages 1-4, surber2025anupdatedsulfate pages 10-13).


*Blockquote: This blockquote summarizes the shared structural framework and key substrate-binding residues across sulfate transporter family members, while highlighting how subtle pocket substitutions can produce major functional divergence. It is useful for judging whether family-level GO annotation is justified or should be restricted to narrower subfamilies.*

### Conserved Catalytic and Binding Residues

Analysis of the plant sulfate transporter AtSULTR4.1 structure and alignment across SULTR and SLC26 families identified key conserved substrate-coordinating residues (surber2025anupdatedsulfate pages 10-13, surber2025anupdatedsulfate pages 4-7):

- **Glu347** (AtSULTR4.1 numbering): Essential for proton sensing and coupled transport; conserved across all SULTRs and many SLC26 members (surber2025anupdatedsulfate pages 10-13)
- **Substrate-binding pocket residues:** Gln112, Tyr116, Ser392, and Arg/Lys393 are strongly conserved and critical for sulfate coordination. Mutagenesis to alanine at these positions causes near-total loss of sulfate transport activity in experimental validation (surber2025anupdatedsulfate pages 10-13)
- **Subfamily-specific substitutions:** Ala153→Ser in SULTR3.3/3.4 and Ser390→Pro in SULTR3.1/3.5 or Ser390→Ala in SULTR3.3 represent binding-pocket modifications that correlate with altered substrate preference and likely drive neo-functionalization (surber2025anupdatedsulfate pages 10-13, surber2025anupdatedsulfate pages 7-10)

Mammalian SLC26 structures reveal comparable substrate-binding architectures despite sequence divergence. SLC26A2 structures with sulfate, oxalate, and chloride demonstrate plasticity in the binding pocket that accommodates diverse anionic substrates (hu2024substratebindingplasticity pages 1-2). SLC26A6 and pendrin (SLC26A4) cryo-EM studies identified dual anion-binding sites within the core domain, with residue composition determining substrate selectivity and coupling stoichiometry (tippett2023structuralandfunctional pages 1-2, wang2024mechanismofanion pages 1-2, tippett2023structuralandfunctional pages 2-3).

### Mechanistic Diversity

Despite shared structural scaffolding, PTHR11814 members exhibit profound mechanistic heterogeneity:

**Prokaryotic and plant sulfate transporters** predominantly function as **sulfate-proton symporters** for cellular sulfate uptake. Plant SULTRs mediate H⁺-coupled sulfate import with high (SULTR1) or low (SULTR2) affinity, supporting root absorption and vascular distribution (surber2025anupdatedsulfate pages 1-4, surber2025anupdatedsulfate pages 7-10). Bacterial sulfate permeases (SulP/SULP family) similarly couple sulfate uptake to electrochemical gradients (snoozy2025xdh1inactivationcauses pages 1-2).

**Mammalian SLC26 proteins** primarily function as **anion exchangers** rather than symporters, with diverse coupling modes:
- SLC26A1 and SLC26A2 mediate electroneutral or electrogenic sulfate/bicarbonate/oxalate/chloride exchange (pfau2023slc26a1isa pages 1-2, hu2024substratebindingplasticity pages 1-2, lee2024chloridemultipleanionexchanger pages 1-2)
- SLC26A3, SLC26A4, and SLC26A6 are Cl⁻/HCO₃⁻ exchangers critical for pH and ion homeostasis (lee2024chloridemultipleanionexchanger pages 1-2, wang2024mechanismofanion pages 1-2, tippett2023structuralandfunctional pages 1-2)
- SLC26A11 exhibits **dual functionality** as both a proton:sulfate exchanger and a gated chloride channel, representing an unusual hybrid transport-channel mode (kuhn2025slc26a11isan pages 1-4)

**Channel-like transporters:** SLC26A7 and SLC26A9 mediate fast, uncoupled chloride transport with channel-like properties, contrasting sharply with coupled exchangers (li2025structuralbasisfor pages 1-2, lee2024chloridemultipleanionexchanger pages 1-2, tippett2023structuralandfunctional pages 1-2).

**Motor protein:** SLC26A5 (prestin) has undergone complete neo-functionalization to serve as an electromechanical motor protein in cochlear outer hair cells rather than functioning as an ion transporter, representing the most extreme functional divergence within the family (lee2024chloridemultipleanionexchanger pages 1-2, tippett2023structuralandfunctional pages 1-2).

---

## 2. InterPro2GO Mapping Appropriateness

**Current status:** PTHR11814 has **zero InterPro2GO mappings**.

**Verdict:** This absence is **appropriate and scientifically justified** given the extreme functional heterogeneity documented above.

### Terms That Would Systematically Over-Annotate

The following commonly expected GO terms would be **false for major subsets** of PTHR11814 proteins:

#### Molecular Function Terms:
- **"Sulfate transmembrane transporter activity" (GO:0008271 or similar):** FALSE for chloride channels (SLC26A7, SLC26A9), Cl⁻/HCO₃⁻ exchangers without sulfate transport (SLC26A3, SLC26A4), phosphate transporter SULTR3.4, and prestin (li2025structuralbasisfor pages 1-2, wang2024mechanismofanion pages 1-2, lee2024chloridemultipleanionexchanger pages 1-2, surber2025anupdatedsulfate pages 1-4, surber2025anupdatedsulfate pages 10-13)
  
- **"Chloride transmembrane transporter activity":** FALSE for plant SULTRs specialized for sulfate, phosphate transporter SULTR3.4, and prestin (surber2025anupdatedsulfate pages 1-4, surber2025anupdatedsulfate pages 10-13)

- **"Anion transmembrane transporter activity" (GO:0008509):** Even this broad term is problematic because prestin functions as a motor protein rather than a transporter (lee2024chloridemultipleanionexchanger pages 1-2)

- **"Anion:anion antiporter activity":** FALSE for proton-coupled symporters (plant SULTRs, bacterial SulP, SLC26A11 sulfate transport mode), uncoupled channels (SLC26A9, SLC26A7), and prestin (kuhn2025slc26a11isan pages 1-4, surber2025anupdatedsulfate pages 1-4, surber2025anupdatedsulfate pages 7-10)

#### Cellular Component Terms:
- **"Plasma membrane":** FALSE for tonoplast-localized SULTR4 (vacuolar sulfate efflux in plants) and lysosomal SLC26A11 (surber2025anupdatedsulfate pages 4-7, kuhn2025slc26a11isan pages 1-4, surber2025anupdatedsulfate pages 7-10)

- **"Integral component of plasma membrane":** Same issue as above, plus additional localization diversity to ER, chloroplast, basolateral vs. apical domains in polarized epithelia (lee2024chloridemultipleanionexchanger pages 1-2, surber2025anupdatedsulfate pages 1-4)

#### Biological Process Terms:
- **"Sulfate transport" or "sulfate assimilation":** FALSE for non-sulfate-transporting members (chloride channels, bicarbonate exchangers, phosphate transporter, prestin) (li2025structuralbasisfor pages 1-2, wang2024mechanismofanion pages 1-2, surber2025anupdatedsulfate pages 10-13)

- **"Chloride transport":** FALSE for sulfate-specialized SULTRs and phosphate transporter SULTR3.4 (surber2025anupdatedsulfate pages 1-4, surber2025anupdatedsulfate pages 10-13)

- **Any metabolic process term** (e.g., "cellular ion homeostasis," "pH regulation," "sulfur compound metabolic process") would be subfamily-specific and inappropriate for family-wide assignment

### Subfamily-Specific Functions Requiring Restricted Annotation

Documented cases where GO terms apply to **subsets only**:

1. **Phosphate transport (SULTR3.4 only):** Rice OsSULTR3.4, barley HvSULTR3.4, and Arabidopsis AtSULTR3.4 function as phosphate distribution transporters validated in oocytes and knockout studies, representing neo-functionalization from ancestral sulfate transport (surber2025anupdatedsulfate pages 1-4, surber2025anupdatedsulfate pages 10-13). A GO term for phosphate transport would be correct for this subfamily but **over-annotating for the remaining 53,834+ family members**.

2. **Electromotility/motor function (prestin only):** SLC26A5 specialization for cochlear mechanics rather than ion transport (lee2024chloridemultipleanionexchanger pages 1-2, tippett2023structuralandfunctional pages 1-2).

3. **Lysosomal sulfate export (SLC26A11 only):** Recent 2025 work identifies SLC26A11 as the elusive lysosomal sulfate exporter, a highly specific compartment and function not shared by other family members (kuhn2025slc26a11isan pages 1-4).

4. **Lignification-associated function (perennial-specific SULTR3.2 subgroup):** Poplar PtaSULTR3.2a is strongly coexpressed with lignin biosynthesis genes and belongs to a eudicot perennial-specific branch, suggesting specialized roles in woody tissue development absent from herbaceous plants and all animal members (surber2025anupdatedsulfate pages 1-4, surber2025anupdatedsulfate pages 10-13, surber2025anupdatedsulfate pages 7-10).

### More Appropriate Alternative Approaches

Rather than applying broad GO terms to PTHR11814, annotation should be:
- **Restricted to child entries** representing functionally coherent subgroups (e.g., separate PANTHER subfamilies for SLC26A1-like sulfate exchangers, SLC26A9-like chloride channels, plant SULTR1 uptake transporters, plant SULTR3.4 phosphate transporters)
- **Marked with evidence codes indicating computational inference** (IEA) only when subfamily context has been validated
- **Flagged as "functionally heterogeneous family - requires subfamily-level curation"** to prevent automated propagation of over-broad terms

---

## 3. Functional Divergence Across the Family

PTHR11814 exhibits extraordinary functional diversification with multiple documented cases of neo-functionalization, lineage-specific specialization, and mechanistic divergence.

| Subfamily/member | Organism group | Primary substrate(s) | Transport mechanism | Subcellular localization | Representative examples with citations |
|---|---|---|---|---|---|
| SLC26A1 (Sat1) | Mammals/vertebrates | Sulfate, bicarbonate, oxalate, glyoxylate | pH-sensitive anion exchanger; major determinant of systemic sulfate homeostasis | Basolateral membrane of renal proximal tubule; also liver/intestine | Human SLC26A1 validated as sulfate transporter in genetics + functional assays; knockout/LOF causes hyposulfatemia and renal sulfate wasting (pfau2023slc26a1isa pages 1-2, lee2024chloridemultipleanionexchanger pages 1-2) |
| SLC26A2 (DTDST) | Mammals/vertebrates | Sulfate, oxalate, chloride | Electroneutral anion exchanger; bidirectional depending on gradients | Plasma membrane; prominent in chondrocytes, enterocytes, dental tissues | Human SLC26A2 cryo-EM structures with sulfate/oxalate/chloride; critical for skeletal and tooth development (hu2024substratebindingplasticity pages 1-2, yoshida2024slc26a2mediatedsulfatemetabolism pages 1-3, lee2024chloridemultipleanionexchanger pages 1-2) |
| SLC26A3 (DRA/CLD) | Mammals/vertebrates | Chloride, bicarbonate, oxalate | Cl-/HCO3- exchanger | Apical membrane of enterocytes, sperm, epididymis | Member of Cl-/HCO3- exchanger clan rather than sulfate-specialized subgroup (lee2024chloridemultipleanionexchanger pages 1-2) |
| SLC26A4 (Pendrin) | Mammals/vertebrates | Chloride, bicarbonate, iodide, thiocyanate; sometimes reported oxalate | Coupled anion exchanger with two anion-binding sites | Kidney, lung, cochlea, thyroid epithelia | Pendrin structures with Cl-, I-, HCO3- show exchanger function and STAS-TM interactions; major functional divergence from sulfate transporters (wang2024mechanismofanion pages 1-2, lee2024chloridemultipleanionexchanger pages 1-2) |
| SLC26A5 (Prestin) | Mammals/vertebrates | Historically linked to chloride/formate/oxalate/sulfate, but specialized function is electromotility | Motor protein in outer hair cells, not a canonical transporter | Cochlear outer hair cells | Clear neo-functionalization away from transport into motor function; strongest reason broad transporter GO terms would over-annotate the family (tippett2023structuralandfunctional pages 1-2, lee2024chloridemultipleanionexchanger pages 1-2) |
| SLC26A6 (PAT1/CFEX) | Mammals/vertebrates | Chloride, bicarbonate, oxalate, formate, sulfate, nitrate | Coupled exchanger; 1:1 electroneutral Cl-/HCO3- exchange and electrogenic Cl-/oxalate exchange | Intestine, kidney, pancreas, heart | Human SLC26A6 cryo-EM + proteoliposome studies define exchanger mechanism and broad substrate range (tippett2023structuralandfunctional pages 1-2, tippett2023structuralandfunctional pages 2-3, seidler2025theenigmaticslc26a6 pages 1-2, lee2024chloridemultipleanionexchanger pages 1-2) |
| SLC26A7 | Mammals/vertebrates | Chloride, iodide, nitrate; little/no bicarbonate permeability in some studies | Channel-like or exchanger-like depending context; halide-preferring SLC26 member | Kidney, stomach, cochlea, retinal pigment epithelium | Cryo-EM identified non-canonical halide recognition site; belongs to Cl- channel clan, not sulfate-specialized subgroup (li2025structuralbasisfor pages 1-2) |
| SLC26A8 (TAT1) | Mammals/vertebrates | Chloride, sulfate | Poorly characterized anion transporter | Male germ cells, sperm | Testis-enriched divergent SLC26 member; supports family heterogeneity (lee2024chloridemultipleanionexchanger pages 1-2) |
| SLC26A9 | Mammals/vertebrates | Chloride (main), some bicarbonate-related activity reported | Fast uncoupled chloride transporter/channel-like uniport | Airway and gastric epithelia | Canonical example of channel-like SLC26 behavior; contrasts with coupled sulfate symporters and exchangers (tippett2023structuralandfunctional pages 1-2, kuhn2025slc26a11isan pages 1-4, lee2024chloridemultipleanionexchanger pages 1-2) |
| SLC26A10 | Mammals/vertebrates | None established | Pseudogene/non-functional in human ORFeome | Not applicable | Human SLC26A10 is noted as a pseudogene, reinforcing that even generic transporter MF terms would fail universally at broad family scope (lee2024chloridemultipleanionexchanger pages 1-2) |
| SLC26A11 (KBAT/SUT1) | Mammals/vertebrates | Sulfate, chloride, bicarbonate, oxalate | Dual-function protein: proton:sulfate/chloride exchanger plus uncoupled channel-like chloride conductance | Lysosomal membrane; also reported in kidney/brain | Recent work identifies SLC26A11 as elusive lysosomal sulfate exporter with gated chloride-conducting state (kuhn2025slc26a11isan pages 1-4, lee2024chloridemultipleanionexchanger pages 1-2) |
| SULTR1 | Land plants | Sulfate | High-affinity sulfate-proton cotransport | Plasma membrane, especially roots | Root uptake transporters for sulfate acquisition; conserved plant uptake module (surber2025anupdatedsulfate pages 1-4, surber2025anupdatedsulfate pages 7-10) |
| SULTR2 | Land plants | Sulfate | Low-affinity sulfate transport, important for root-to-shoot movement | Plasma membrane, root vascular tissues | Vascular sulfate distribution rather than uptake; distinct from SULTR1 but still sulfate-centered (surber2025anupdatedsulfate pages 1-4, surber2025anupdatedsulfate pages 7-10) |
| SULTR3.1 / 3.2 branch | Land plants, especially angiosperms; perennial-specific subgroup in eudicots | Often sulfate-related; some members difficult to validate directly in vitro | Diverse/poorly resolved; some cooperate with other SULTRs rather than acting alone | Plasma membrane, ER, chloroplast, vascular tissues depending member | Expanded branch with lineage-specific duplications; perennial-specific subgroup linked to lignifying tissues in poplar (surber2025anupdatedsulfate pages 1-4, surber2025anupdatedsulfate pages 10-13, surber2025anupdatedsulfate pages 7-10) |
| SULTR3.3 | Land plants | Sulfate-related/uncertain; likely specialized transport role | Divergent SULTR3-type transport; often not robustly reconstituted as simple sulfate uptake | Broad tissue distribution in some species | Conserved SULTR3 subfamily with altered binding-pocket residues relative to canonical sulfate transporters (surber2025anupdatedsulfate pages 10-13, surber2025anupdatedsulfate pages 7-10) |
| SULTR3.4 (SPDT) | Land plants | Phosphate rather than sulfate in validated cases | Influx transporter for phosphate; neofunctionalized from sulfate transporter family | Vascular/plasma membrane-associated distribution tissues | Rice, barley, Arabidopsis SULTR3.4 function as phosphate distribution transporters, not sulfate transporters; strongest plant case of neo-functionalization (surber2025anupdatedsulfate pages 1-4, surber2025anupdatedsulfate pages 10-13) |
| SULTR3.5 | Land plants | Sulfate-related; can cooperate with SULTR2.1 | Accessory/cooperative role in sulfate transport; some individual assays negative | Vasculature and other tissues depending species | Arabidopsis SULTR3.5 improves sulfate transport with SULTR2.1 rather than behaving as simple standalone sulfate importer (surber2025anupdatedsulfate pages 1-4, surber2025anupdatedsulfate pages 7-10) |
| SULTR4 | Land plants | Sulfate | Tonoplast sulfate efflux; proton-coupled sulfate transport with conserved Glu347, Gln112, Tyr116, Ser392, Arg/Lys393 pocket residues | Tonoplast/vacuolar membrane | AtSULTR4.1 structural template underpins conserved plant sulfate-binding pocket; vacuolar exporter rather than plasma-membrane importer (surber2025anupdatedsulfate pages 4-7, surber2025anupdatedsulfate pages 10-13, surber2025anupdatedsulfate pages 7-10) |
| SulP / SULP sulfate permeases | Bacteria and some microbial eukaryotes/nematodes | Sulfate and related small anions; some homologs more broadly anion-exchanging | Typically secondary active sulfate permeases/symporters or exchangers depending lineage | Usually plasma membrane or equivalent cell membrane | Widespread bacterial sulfate permeases and C. elegans SULP-4 homologous to human SLC26 proteins illustrate deep evolutionary breadth and non-uniform physiology across the family (snoozy2025xdh1inactivationcauses pages 1-2, tippett2023structuralandfunctional pages 1-2) |
| Family-level conserved architecture across many members | Cross-kingdom overview | Small inorganic anions, but exact specificity highly variable | Core/gate elevator-type architecture with STAS-associated regulation in many members | Membrane-embedded; localization varies from plasma membrane to tonoplast to lysosome | Shared UraA-like fold and STAS domain coexist with radical functional divergence, explaining why PTHR11814 is unsafe for narrow GO mapping at family level (hu2024substratebindingplasticity pages 1-2, tippett2023structuralandfunctional pages 1-2, wang2024mechanismofanion pages 1-2, kuhn2025slc26a11isan pages 1-4) |


*Table: This table summarizes the major functional branches represented within the PTHR11814 sulfate transporter family across animals, plants, and microbes. It highlights why family-wide GO annotation is risky by showing strong divergence in substrate specificity, mechanism, and localization, including phosphate-transporting SULTR3.4 and prestin’s motor-protein specialization.*

### Neo-Functionalization Events

**SULTR3.4 → Phosphate Transport:** The most extensively characterized case of substrate-switching neo-functionalization. Rice, barley, and Arabidopsis SULTR3.4 proteins (also termed SPDT, Sulfate transporter-like Phosphorus Distribution Transporter) function as influx transporters for phosphate rather than sulfate, validated through functional complementation in oocytes and loss-of-function mutant phenotypes showing impaired phosphorus distribution to developing organs (surber2025anupdatedsulfate pages 1-4, surber2025anupdatedsulfate pages 10-13). Structural modeling suggests that SULTR3.4's unique Ser153-Ser390-Ser392 triad creates a binding pocket optimized for phosphate's -3 charge versus sulfate's -2 charge (surber2025anupdatedsulfate pages 10-13).

**Prestin (SLC26A5) → Electromechanical Motor:** Complete loss of canonical ion transport function with gain of voltage-dependent conformational changes that drive mechanical amplification in cochlear outer hair cells. This represents the most radical departure from ancestral sulfate transport within the family (lee2024chloridemultipleanionexchanger pages 1-2, tippett2023structuralandfunctional pages 1-2).

**SLC26A11 → Dual Transport-Channel Function:** Recent 2025 studies demonstrate that SLC26A11 is an atypical solute carrier with two distinct functional modes: proton:sulfate symport (canonical transporter behavior) and an uncoupled, channel-like chloride conductance gated by the transport cycle (kuhn2025slc26a11isan pages 1-4). This dual functionality appears unique within the family and supports both lysosomal sulfate export and potentially chloride homeostasis.

### Lineage-Specific Specialization

**Perennial-specific SULTR3.2 subgroup:** Phylogenetic analysis revealed a eudicot-specific SULTR3.1 subgroup retained only in perennial species (poplar, oak, birch, papaya, peach, coffee) but absent from annuals like Arabidopsis (surber2025anupdatedsulfate pages 1-4, surber2025anupdatedsulfate pages 10-13, surber2025anupdatedsulfate pages 7-10). Poplar PtaSULTR3.2a shows strong coexpression with lignin biosynthesis genes, one-carbon metabolism genes, and transcriptional regulators of secondary cell wall formation, suggesting specialized roles in woody tissue development distinct from herbaceous plant SULTRs (surber2025anupdatedsulfate pages 1-4, surber2025anupdatedsulfate pages 10-13).

**Mammalian tissue-specific diversification:** SLC26 paralogs show restricted expression patterns correlating with specialized physiological roles:
- SLC26A4 (pendrin): thyroid, kidney, inner ear, lung epithelia for iodide/bicarbonate/chloride exchange (wang2024mechanismofanion pages 1-2, lee2024chloridemultipleanionexchanger pages 1-2)
- SLC26A5 (prestin): exclusively cochlear outer hair cells for electromotility (lee2024chloridemultipleanionexchanger pages 1-2)
- SLC26A8: testis-enriched with poorly characterized function in male germ cells (lee2024chloridemultipleanionexchanger pages 1-2)
- SLC26A11: lysosomal localization across tissues with highest expression in brain (kuhn2025slc26a11isan pages 1-4)

### Transport Mechanisms: Coupled vs. Uncoupled vs. Channel-like

**Coupled exchangers (electroneutral or electrogenic):** Most characterized SLC26 members mediate obligate anion exchange with varied stoichiometry. SLC26A6 exhibits 1:1 electroneutral Cl⁻/HCO₃⁻ exchange but electrogenic Cl⁻/oxalate²⁻ exchange, as determined through proteoliposome reconstitution and patch-clamp studies (tippett2023structuralandfunctional pages 1-2, tippett2023structuralandfunctional pages 2-3, seidler2025theenigmaticslc26a6 pages 1-2). Pendrin structures with different anions revealed two binding sites per protomer, both involved in coupled exchange (wang2024mechanismofanion pages 1-2).

**Uncoupled/channel-like transporters:** SLC26A9 and SLC26A7 mediate fast passive chloride fluxes resembling channel behavior rather than coupled exchange, with large ohmic currents lacking time-dependence and reversal potentials matching the chloride equilibrium potential (tippett2023structuralandfunctional pages 1-2, li2025structuralbasisfor pages 1-2, lee2024chloridemultipleanionexchanger pages 1-2).

**Proton-coupled symporters:** Plant SULTRs and prokaryotic sulfate permeases couple sulfate uptake to proton gradients rather than anion exchange, representing a fundamentally different energetic mechanism (surber2025anupdatedsulfate pages 1-4, surber2025anupdatedsulfate pages 7-10). SLC26A11's sulfate transport mode also involves proton:sulfate symport distinct from most mammalian SLC26 exchangers (kuhn2025slc26a11isan pages 1-4).

### Catalytically Attenuated Members

Several SULTR3 subfamily members show reduced or absent sulfate transport activity in heterologous expression systems:

- Arabidopsis AtSULTR3.1, AtSULTR3.2, and AtSULTR3.3 did not mediate sulfate uptake when expressed in yeast, contrasting with robust activity from SULTR1, SULTR2, and SULTR4 members (surber2025anupdatedsulfate pages 1-4, surber2025anupdatedsulfate pages 7-10)
- AtSULTR3.5 alone does not support sulfate uptake in yeast or isolated chloroplasts but enhances activity when co-expressed with AtSULTR2.1, suggesting an accessory/regulatory role rather than standalone transport (surber2025anupdatedsulfate pages 1-4)
- Rice OsSULTR3.3 knockout mutants display low phytic acid phenotypes despite inability to demonstrate sulfate, phosphate, or inositol transport in yeast or Xenopus oocytes, indicating indirect or non-transport functions (surber2025anupdatedsulfate pages 1-4)

These examples demonstrate that not all family members function as canonical transporters, further supporting the inappropriateness of applying transporter-specific GO terms family-wide.

---

## 4. Taxonomic Scope

PTHR11814 spans **all domains of life** with representation across bacteria, plants, and animals, totaling 53,835 proteins across 25,803 taxa according to the InterPro API metadata.

### Prokaryotes (Bacteria)

Bacterial sulfate permeases (SulP/SULP family) are widespread sulfate uptake systems coupling sulfate influx to membrane potential or ion gradients (snoozy2025xdh1inactivationcauses pages 1-2, tippett2023structuralandfunctional pages 1-2). C. elegans SULP-4, homologous to human SLC26 proteins, functions as an anion exchanger in the excretory cell to regulate sulfate and potentially other small anion levels (snoozy2025xdh1inactivationcauses pages 1-2).

### Plants (Viridiplantae)

Sulfate transporters (SULTRs) are ubiquitous across land plants from bryophytes (mosses like Physcomitrium patens) through vascular plants (lycophytes like Selaginella moellendorffii) to angiosperms (surber2025anupdatedsulfate pages 1-4, surber2025anupdatedsulfate pages 7-10). Recent phylogenetic reconstruction across 20 angiosperm species plus early-divergent lineages supports **seven evolutionarily conserved SULTR subfamilies** predating angiosperm radiation (surber2025anupdatedsulfate pages 1-4, surber2025anupdatedsulfate pages 10-13, surber2025anupdatedsulfate pages 7-10):

- **Ancient Clade I (AC-I):** SULTR4 (tonoplast localized, 1-2 copies per genome)
- **Ancient Clade II (AC-II):**
  - **AC-IIA:** SULTR1 (high-affinity root uptake), SULTR2 (low-affinity vascular distribution)
  - **AC-IIB:** SULTR3.1, SULTR3.5, SULTR3.3, SULTR3.4 (diverse localization and functions including neo-functionalized phosphate transport in SULTR3.4)

The SULTR3 group is the largest and most diverse, with 5 genes in Arabidopsis expanding to many more in other angiosperms through lineage-specific duplications (surber2025anupdatedsulfate pages 1-4, surber2025anupdatedsulfate pages 10-13, surber2025anupdatedsulfate pages 7-10).

### Animals (Metazoa)

The **SLC26 family** comprises **11 genes in humans** (SLC26A1-A11, with SLC26A10 being a pseudogene) encoding functionally diverse anion transporters, exchangers, channels, and the prestin motor protein (lee2024chloridemultipleanionexchanger pages 1-2). SLC26 proteins are conserved across vertebrates with tissue-specific expression patterns supporting specialized physiological roles in kidney, intestine, cochlea, thyroid, lung, and other organs (wang2024mechanismofanion pages 1-2, lee2024chloridemultipleanionexchanger pages 1-2, pfau2023slc26a1isa pages 1-2).

### Cross-Kingdom Functional and Mechanistic Differences

**Transport Mechanism:**
- Prokaryotes and plants: predominantly **H⁺-coupled sulfate symport** for cellular uptake (surber2025anupdatedsulfate pages 1-4, surber2025anupdatedsulfate pages 7-10, snoozy2025xdh1inactivationcauses pages 1-2)
- Mammals: predominantly **anion exchange** (Cl⁻/HCO₃⁻, Cl⁻/oxalate, sulfate/bicarbonate) rather than symport (wang2024mechanismofanion pages 1-2, lee2024chloridemultipleanionexchanger pages 1-2, tippett2023structuralandfunctional pages 1-2, pfau2023slc26a1isa pages 1-2)

**Subcellular Localization:**
- Prokaryotes: plasma membrane or equivalent cell membrane sulfate importers
- Plants: plasma membrane (SULTR1, SULTR2, SULTR3), tonoplast/vacuolar (SULTR4), chloroplast (some SULTR3), ER (some SULTR3) (surber2025anupdatedsulfate pages 4-7, surber2025anupdatedsulfate pages 1-4, surber2025anupdatedsulfate pages 7-10)
- Mammals: plasma membrane with apical vs. basolateral polarity in epithelia, lysosomal membrane (SLC26A11) (lee2024chloridemultipleanionexchanger pages 1-2, kuhn2025slc26a11isan pages 1-4, pfau2023slc26a1isa pages 1-2)

**Substrate Preference:**
- Bacterial/plant SULTRs: primarily sulfate-specialized (with exceptions like SULTR3.4)
- Mammalian SLC26: broad substrate diversity including sulfate (SLC26A1, A2), chloride/bicarbonate (A3, A4, A6, A7, A9), iodide (A4, A7), oxalate (A1, A2, A6), formate (A6), with prestin non-transporting (li2025structuralbasisfor pages 1-2, wang2024mechanismofanion pages 1-2, lee2024chloridemultipleanionexchanger pages 1-2, tippett2023structuralandfunctional pages 1-2, pfau2023slc26a1isa pages 1-2)

**Physiological Context:**
- Plants: sulfate assimilation for biosynthesis, stress responses, lignification in perennials (surber2025anupdatedsulfate pages 1-4, surber2025anupdatedsulfate pages 10-13, surber2025anupdatedsulfate pages 7-10)
- Mammals: pH homeostasis, salt/fluid balance, thyroid hormone synthesis (iodide), kidney stone prevention (oxalate), hearing (prestin), lysosomal catabolite clearance (wang2024mechanismofanion pages 1-2, lee2024chloridemultipleanionexchanger pages 1-2, kuhn2025slc26a11isan pages 1-4, pfau2023slc26a1isa pages 1-2)

These profound differences mean that **no process-level or component-level GO term applies universally** across the family's taxonomic scope.

---

## 5. Over-Annotation Verdict and Recommendations

### Summary Verdict: Current InterPro2GO State is SOUND

PTHR11814's current status of **zero mapped GO terms is scientifically appropriate** and should be maintained. This family exhibits functional heterogeneity so extreme that it defies family-level functional annotation. The 77 subfamilies spanning 53,835 proteins across 25,803 taxa represent:

1. **Radical substrate divergence:** Sulfate vs. chloride vs. bicarbonate vs. phosphate vs. iodide vs. oxalate vs. formate vs. no transported substrate (prestin)
2. **Mechanistic diversity:** Proton symport vs. electroneutral exchange vs. electrogenic exchange vs. uncoupled channel-like transport vs. motor protein function
3. **Compartmental heterogeneity:** Plasma membrane (apical or basolateral) vs. tonoplast vs. lysosomal vs. ER vs. chloroplast
4. **Neo-functionalization events:** Complete substrate-switching (sulfate→phosphate in SULTR3.4), loss of transport with gain of electromotility (prestin), acquisition of dual transport-channel modes (SLC26A11)

### Recommended GO Annotation Action Pattern

**For PTHR11814 itself (family level):**
- **ACCEPT** current absence of InterPro2GO mappings
- **Flag entry** as "functionally heterogeneous family - subfamily-level annotation required"
- **Reject/REMOVE** any proposed family-wide molecular function, biological process, or cellular component terms

**If specific GO terms were proposed for PTHR11814, the appropriate response would be:**
- "Sulfate transmembrane transporter activity": **MARK_AS_OVER_ANNOTATED** / **REMOVE** (false for chloride channels, bicarbonate exchangers, phosphate transporter SULTR3.4, prestin)
- "Chloride transmembrane transporter activity": **MARK_AS_OVER_ANNOTATED** / **REMOVE** (false for plant sulfate-specialized SULTRs, phosphate transporter, prestin)
- "Anion transmembrane transporter activity": **MARK_AS_OVER_ANNOTATED** / **REMOVE** (false for prestin motor protein)
- "Plasma membrane": **MARK_AS_OVER_ANNOTATED** / **REMOVE** (false for tonoplast SULTR4, lysosomal SLC26A11)
- Any biological process term: **MARK_AS_OVER_ANNOTATED** / **REMOVE** (all are subfamily-specific)

**For child entries (PANTHER subfamilies or more specific InterPro signatures):**
- **MODIFY-to-specific:** Restrict GO terms to functionally coherent subgroups validated by experimental evidence
  - Example: A child signature capturing only SLC26A1/A2-like sulfate exchangers could appropriately carry "sulfate transmembrane transporter activity" and "basolateral plasma membrane"
  - Example: A signature specific to plant SULTR3.4 orthologs could carry "phosphate transmembrane transporter activity" rather than sulfate transport
  - Example: A prestin-specific signature should carry motor-related terms, not transporter terms

**Recommendation for InterPro hierarchy:**
- **Demote** any whole-protein functional annotations from PTHR11814 to more specific child entries representing mechanistically and biochemically validated subgroups
- **Move** subfamily-specific terms (e.g., prestin electromotility, SULTR3.4 phosphate transport, SLC26A11 lysosomal sulfate export) to appropriately narrow child signatures
- **Consider creating** new child signatures if functional subgroups are not adequately captured (e.g., separate signatures for plant high-affinity sulfate uptake transporters, mammalian chloride/bicarbonate exchangers, perennial-specific lignification-associated SULTRs)

### Experimental vs. Inference-Based Evidence

The recommendations above are grounded in:

**Experimental structural evidence:** High-resolution cryo-EM structures of SLC26A2, SLC26A6, SLC26A7, SLC26A9, SLC26A11, pendrin, prestin from 2023-2025 defining substrate-binding sites, conformational states, and transport architecture (li2025structuralbasisfor pages 1-2, wang2024mechanismofanion pages 1-2, kuhn2025slc26a11isan pages 1-4, hu2024substratebindingplasticity pages 1-2, tippett2023structuralandfunctional pages 1-2)

**Experimental functional validation:** Proteoliposome reconstitution and transport assays (SLC26A6, SLC26A11, AtSULTR4.1), patch-clamp electrophysiology (SLC26A9, SLC26A7, pendrin), heterologous expression in yeast/oocytes with substrate uptake measurements (plant SULTRs, SLC26 members), and genetic knockout/loss-of-function studies in mice, plants, C. elegans, and human patients (wang2024mechanismofanion pages 1-2, kuhn2025slc26a11isan pages 1-4, surber2025anupdatedsulfate pages 1-4, tippett2023structuralandfunctional pages 1-2, pfau2023slc26a1isa pages 1-2, surber2025anupdatedsulfate pages 10-13, surber2025anupdatedsulfate pages 7-10, yoshida2024slc26a2mediatedsulfatemetabolism pages 1-3, snoozy2025xdh1inactivationcauses pages 1-2)

**Phylogenetic and structural modeling:** Maximum likelihood phylogenetic reconstructions across 262 plant SULTR sequences from 22 species plus bacterial and mammalian homologs, AlphaFold3 structural modeling of plant SULTRs with substrate docking, and sequence alignments identifying conserved vs. subfamily-specific residues in binding pockets (surber2025anupdatedsulfate pages 4-7, surber2025anupdatedsulfate pages 1-4, surber2025anupdatedsulfate pages 10-13, surber2025anupdatedsulfate pages 7-10)

**Clinical genetics:** Human loss-of-function mutations in SLC26A1 causing hyposulfatemia and sulfate wasting, SLC26A2 mutations causing chondrodysplasias and dental abnormalities, SLC26A4 mutations causing Pendred syndrome with hearing loss, and SLC26A6 mutations associated with kidney stones (pfau2023slc26a1isa pages 1-2, yoshida2024slc26a2mediatedsulfatemetabolism pages 1-3, wang2024mechanismofanion pages 1-2, seidler2025theenigmaticslc26a6 pages 1-2)

This body of experimental work from 2023-2025 conclusively demonstrates that PTHR11814 is far too functionally diverse to support family-level GO annotation. The absence of InterPro2GO mappings should be maintained to prevent systematic over-annotation of the >50,000 proteins matching this signature.

---

## References

All major claims are supported by citations to primary literature and recent structural/functional studies as indicated by context IDs (li2025structuralbasisfor pages 1-2, seidler2025theenigmaticslc26a6 pages 1-2) throughout this report.

References

1. (hu2024substratebindingplasticity pages 1-2): Wenxin Hu, Alex Song, and Hongjin Zheng. Substrate binding plasticity revealed by cryo-em structures of slc26a2. ArXiv, May 2024. URL: https://doi.org/10.2210/pdb8tny/pdb, doi:10.2210/pdb8tny/pdb. This article has 9 citations.

2. (tippett2023structuralandfunctional pages 1-2): David N. Tippett, Colum Breen, Stephen J. Butler, Marta Sawicka, and Raimund Dutzler. Structural and functional properties of the transporter slc26a6 reveal mechanism of coupled anion exchange. May 2023. URL: https://doi.org/10.7554/elife.87178.2, doi:10.7554/elife.87178.2. This article has 22 citations.

3. (wang2024mechanismofanion pages 1-2): Lie Wang, Anthony Hoang, Eva Gil-Iturbe, Arthur Laganowsky, Matthias Quick, and Ming Zhou. Mechanism of anion exchange and small-molecule inhibition of pendrin. Nature Communications, Jan 2024. URL: https://doi.org/10.1038/s41467-023-44612-1, doi:10.1038/s41467-023-44612-1. This article has 26 citations and is from a highest quality peer-reviewed journal.

4. (tippett2023structuralandfunctional pages 2-3): David N. Tippett, Colum Breen, Stephen J. Butler, Marta Sawicka, and Raimund Dutzler. Structural and functional properties of the transporter slc26a6 reveal mechanism of coupled anion exchange. May 2023. URL: https://doi.org/10.7554/elife.87178.2, doi:10.7554/elife.87178.2. This article has 22 citations.

5. (seidler2025theenigmaticslc26a6 pages 1-2): Ursula E. Seidler. The enigmatic slc26a6 multifunctional anion transporter: recent advances in structure-function relationship, pathophysiological significance and novel pharmacological inhibitors. Frontiers in Pharmacology, Jan 2025. URL: https://doi.org/10.3389/fphar.2024.1536864, doi:10.3389/fphar.2024.1536864. This article has 2 citations.

6. (kuhn2025slc26a11isan pages 1-4): Benedikt T Kuhn, Peter Kovermann, Bassam G Haddad, Tim Rasmussen, Tamsanga Hove, Stefanie Bungert-Pluemke, Bettina Boettcher, Jan-Philipp Machtens, Christoph Fahlke, and Eric R. Geertsma. Slc26a11 is an atypical solute carrier with dual transport-channel function mediating lysosomal sulfate transport. BioRxiv, Aug 2025. URL: https://doi.org/10.1101/2025.08.17.670773, doi:10.1101/2025.08.17.670773. This article has 1 citations.

7. (surber2025anupdatedsulfate pages 10-13): Samantha M. Surber, Chen Hsieh, Lan Na, Scott A. Harding, and Chung-Jui Tsai. An updated sulfate transporter phylogeny uncovers a perennial-specific subgroup associated with lignification. bioRxiv, Jul 2025. URL: https://doi.org/10.1101/2025.04.23.650276, doi:10.1101/2025.04.23.650276. This article has 4 citations.

8. (surber2025anupdatedsulfate pages 1-4): Samantha M. Surber, Chen Hsieh, Lan Na, Scott A. Harding, and Chung-Jui Tsai. An updated sulfate transporter phylogeny uncovers a perennial-specific subgroup associated with lignification. bioRxiv, Jul 2025. URL: https://doi.org/10.1101/2025.04.23.650276, doi:10.1101/2025.04.23.650276. This article has 4 citations.

9. (li2025structuralbasisfor pages 1-2): Xiaorong Li, Xiaoxu Yang, Xiaoli Lu, Bingqian Lin, Yuanyuan Zhang, Bangdong Huang, Yutong Zhou, Jing Huang, Kun Wu, Qiang Zhou, and Ximin Chi. Structural basis for substrate recognition mechanism of human slc26a7. Nature Communications, Aug 2025. URL: https://doi.org/10.1038/s41467-025-62792-w, doi:10.1038/s41467-025-62792-w. This article has 6 citations and is from a highest quality peer-reviewed journal.

10. (surber2025anupdatedsulfate pages 4-7): Samantha M. Surber, Chen Hsieh, Lan Na, Scott A. Harding, and Chung-Jui Tsai. An updated sulfate transporter phylogeny uncovers a perennial-specific subgroup associated with lignification. bioRxiv, Jul 2025. URL: https://doi.org/10.1101/2025.04.23.650276, doi:10.1101/2025.04.23.650276. This article has 4 citations.

11. (surber2025anupdatedsulfate pages 7-10): Samantha M. Surber, Chen Hsieh, Lan Na, Scott A. Harding, and Chung-Jui Tsai. An updated sulfate transporter phylogeny uncovers a perennial-specific subgroup associated with lignification. bioRxiv, Jul 2025. URL: https://doi.org/10.1101/2025.04.23.650276, doi:10.1101/2025.04.23.650276. This article has 4 citations.

12. (snoozy2025xdh1inactivationcauses pages 1-2): Jennifer Snoozy, Sushila Bhattacharya, Brandon E. Johnson, Robin R. Fettig, Ashley Van Asma, Chloe Brede, Sophia Miller, Martina Ralle, and Kurt Warnhoff. Xdh-1 inactivation causes xanthine stone formation in caenorhabditis elegans which is inhibited by sulp-4-mediated anion exchange in the excretory cell. Sep 2025. URL: https://doi.org/10.1371/journal.pbio.3003410, doi:10.1371/journal.pbio.3003410. This article has 2 citations and is from a highest quality peer-reviewed journal.

13. (pfau2023slc26a1isa pages 1-2): Anja Pfau, Karen I. López-Cayuqueo, Nora Scherer, Matthias Wuttke, Annekatrin Wernstedt, Daniela González Fassrainer, Desiree E.C. Smith, Jiddeke M. van de Kamp, Katharina Ziegeler, Kai-Uwe Eckardt, Friedrich C. Luft, Peter S. Aronson, Anna Köttgen, Thomas J. Jentsch, and Felix Knauf. Slc26a1 is a major determinant of sulfate homeostasis in humans. The Journal of Clinical Investigation, Feb 2023. URL: https://doi.org/10.1172/jci161849, doi:10.1172/jci161849. This article has 22 citations.

14. (lee2024chloridemultipleanionexchanger pages 1-2): Dongun Lee and Jeong Hee Hong. Chloride/multiple anion exchanger slc26a family: systemic roles of slc26a4 in various organs. International Journal of Molecular Sciences, 25:4190, Apr 2024. URL: https://doi.org/10.3390/ijms25084190, doi:10.3390/ijms25084190. This article has 10 citations.

15. (yoshida2024slc26a2mediatedsulfatemetabolism pages 1-3): Yuka Yoshida, Toshihiro Inubushi, Mika Yokoyama, Priyanka Nag, Jun-ichi Sasaki, Ayaka Oka, Tomoya Murotani, Renshiro Kani, Yuki Shiraishi, Hiroshi Kurosaka, Yoshifumi Takahata, Riko Nishimura, Satoshi Imazato, Petros Papagerakis, and Takashi Yamashiro. <i>slc26a2</i>-mediated sulfate metabolism is important in tooth development. Disease Models &amp; Mechanisms, Dec 2024. URL: https://doi.org/10.1242/dmm.052107, doi:10.1242/dmm.052107. This article has 3 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PTHR11814-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR11814-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. surber2025anupdatedsulfate pages 10-13
2. hu2024substratebindingplasticity pages 1-2
3. lee2024chloridemultipleanionexchanger pages 1-2
4. li2025structuralbasisfor pages 1-2
5. wang2024mechanismofanion pages 1-2
6. surber2025anupdatedsulfate pages 1-4
7. tippett2023structuralandfunctional pages 1-2
8. tippett2023structuralandfunctional pages 2-3
9. surber2025anupdatedsulfate pages 4-7
10. surber2025anupdatedsulfate pages 7-10
11. https://doi.org/10.2210/pdb8tny/pdb,
12. https://doi.org/10.7554/elife.87178.2,
13. https://doi.org/10.1038/s41467-023-44612-1,
14. https://doi.org/10.3389/fphar.2024.1536864,
15. https://doi.org/10.1101/2025.08.17.670773,
16. https://doi.org/10.1101/2025.04.23.650276,
17. https://doi.org/10.1038/s41467-025-62792-w,
18. https://doi.org/10.1371/journal.pbio.3003410,
19. https://doi.org/10.1172/jci161849,
20. https://doi.org/10.3390/ijms25084190,
21. https://doi.org/10.1242/dmm.052107,