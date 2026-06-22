---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-21T20:03:04.425665'
end_time: '2026-06-21T20:17:50.173574'
duration_seconds: 885.75
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR11711
  interpro_name: ADP RIBOSYLATION FACTOR-RELATED
  interpro_short_name: Not specified
  interpro_type: family
  interpro_integrated: IPR024156
  member_databases: Not specified
  n_proteins: '41271'
  n_taxa: '11970'
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
  path: PTHR11711-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR11711-deep-research-falcon_artifacts/artifact-01.md
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
- **Accession:** PTHR11711
- **Name:** ADP RIBOSYLATION FACTOR-RELATED
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** IPR024156
- **Member database signatures:** Not specified
- **Scale:** 41271 proteins across 11970 taxa, 77 subfamilies
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
**PTHR11711 (ADP RIBOSYLATION FACTOR-RELATED)**, structured to support GO annotation review.

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
- **Accession:** PTHR11711
- **Name:** ADP RIBOSYLATION FACTOR-RELATED
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** IPR024156
- **Member database signatures:** Not specified
- **Scale:** 41271 proteins across 11970 taxa, 77 subfamilies
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
**PTHR11711 (ADP RIBOSYLATION FACTOR-RELATED)**, structured to support GO annotation review.

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


# InterPro2GO Annotation Review: PTHR11711 (ADP RIBOSYLATION FACTOR-RELATED)

## Executive Summary

InterPro entry PTHR11711 ("ADP RIBOSYLATION FACTOR-RELATED") is a **family-level** PANTHER signature matching 41,271 proteins across 11,970 taxa with 77 subfamilies. This entry encompasses the entire ARF (ADP-ribosylation factor) superfamily of small GTPases, including classical ARFs, SAR proteins, and the highly diverse ARL (ARF-like) subfamily. The **current absence of InterPro2GO mappings is scientifically appropriate** and should be maintained. This family is too functionally heterogeneous for any whole-protein GO annotation; even seemingly broad terms would systematically over-annotate proteins matching this signature.

---

## 1. Family Definition and Biochemistry

### Core Molecular Architecture

The ARF family proteins share a conserved **small GTPase fold** belonging to the RAS superfamily (sztul2019arfgtpasesand pages 1-2, vargova2021aeukaryotewideperspective pages 1-2). The canonical structure comprises:

- **GTPase domain** with five conserved motifs (G1-G5), including the signature G3 motif **WDXGGQ** where the glutamine (Q) is critical for GTP hydrolysis (quirion2025unfoldingarfand pages 2-4).
- **Switch I and switch II regions** that undergo extensive conformational rearrangement upon GTP loading—more dramatic than in classical RAS GTPases like KRAS (quirion2025unfoldingarfand pages 2-4).
- **Nucleotide-binding pocket** for GDP/GTP cycling regulated by guanine nucleotide exchange factors (GEFs) and GTPase-activating proteins (GAPs) (li2023thearffamily pages 1-3, sztul2019arfgtpasesand pages 1-2).

### Unique Distinguishing Feature: N-terminal Amphipathic Helix

A defining feature separating ARF family proteins from other RAS superfamily members is an **N-terminal amphipathic helix** (typically 16-20 residues) that is post-translationally modified:

- **Myristoylation** (most common): N-terminal glycine receives a C14 fatty acid, enabling membrane insertion upon GTP loading (li2023thearffamily pages 1-3, sztul2019arfgtpasesand pages 1-2, quirion2025unfoldingarfand pages 2-4).
- **Acetylation** (ARL8A/B, ARFRP1): alternative N-terminal modification determining membrane association (li2023thearffamily pages 1-3, vargova2021aeukaryotewideperspective pages 2-3).
- **Palmitoylation** (some members): additional lipid modifications in specific paralogs (quirion2025unfoldingarfand pages 2-4).

In the GDP-bound state, the myristoyl moiety is **buried in a hydrophobic pocket** between the interswitch region and C-terminal helix. Upon GTP binding, a major conformational shift ejects the N-terminal helix, inserting it into lipid bilayers to anchor the GTPase to membranes (li2023thearffamily pages 1-3, quirion2025unfoldingarfand pages 2-4). This membrane-coupled activation mechanism is unique among small GTPases.

### Structural Data

Crystal structures exist for only two family members in both nucleotide states:
- **ARF1**: GDP-bound (PDB 7WQY), GTP-bound (PDB 1HUR) (quirion2025unfoldingarfand pages 2-4)
- **ARF6**: GDP-bound (PDB 1E0S), GTP-bound (PDB 2J5X) (quirion2025unfoldingarfand pages 2-4)

Notably, ARF1-GDP and ARF6-GDP adopt **highly divergent conformations**, particularly in switch regions, yet their GTP-bound states converge, underscoring that despite shared core mechanism, different paralogs exhibit distinct regulatory properties and GEF/GAP specificities (quirion2025unfoldingarfand pages 2-4).

### Biochemical Mechanism

The ARF family operates via **GTPase cycling**:
1. **Inactive state (GDP-bound)**: Cytosolic, N-terminal helix retracted.
2. **Activation**: GEF (e.g., Sec7-domain proteins, AMPK) catalyzes GDP release; GTP binds (10-fold more abundant in cells).
3. **Active state (GTP-bound)**: N-terminal helix exposed, protein membrane-anchored, recruits effectors.
4. **Termination**: GAP (e.g., ArfGAPs with Zn-finger domains, ELMOD proteins) accelerates GTP hydrolysis, releasing the GTPase from membranes (li2023thearffamily pages 1-3, sztul2019arfgtpasesand pages 1-2, jackson2023anevolutionaryperspective pages 5-8).

This differs from the classical RAS "on/off switch" paradigm because **ARF cycling itself mediates trafficking** rather than simply transducing a signal; GAPs and effectors often act concurrently, not sequentially (sztul2019arfgtpasesand pages 1-2).

---

## 2. InterPro2GO Mapping Appropriateness

### Current Status: No GO Terms Mapped

PTHR11711 currently has **zero InterPro2GO mappings**. This is **scientifically appropriate** and should be **maintained**.

### Why Family-Wide GO Annotation Would Be Inappropriate

#### Problem 1: Extreme Functional Divergence Across Subfamilies

The ARF family comprises at least **12 functionally distinct subfamilies** with **opposite cellular roles** (see artifact-00):

- **ARF1/3/4/5 (Class I/II)**: Golgi-localized, recruit COPI/AP/GGA vesicle coats for secretory pathway trafficking (li2023thearffamily pages 3-5, vargova2021aeukaryotewideperspective pages 7-8).
- **ARF6 (Class III)**: Plasma membrane/endosome-localized, regulate endocytosis, recycling, actin remodeling (sztul2019arfgtpasesand pages 1-2, quirion2024mappingtheglobal pages 1-3, vargova2021aeukaryotewideperspective pages 7-8).
- **SAR1A/B**: ER exit site-localized, recruit COPII coat for ER-to-Golgi transport (li2023thearffamily pages 3-5, quirion2024mappingtheglobal pages 1-3).
- **ARL1/ARFRP1**: Trans-Golgi network, recruit golgins and tethering factors (vargova2021aeukaryotewideperspective pages 7-8).
- **ARL2**: Cytosol/mitochondria, regulate tubulin heterodimer biogenesis and mitochondrial fusion (sztul2019arfgtpasesand pages 1-2, quirion2024mappingtheglobal pages 3-5).
- **ARL3/6/13B**: Cilia/centrosomes, traffic lipidated cargo to primary cilia (fisher2020arffamilygtpases pages 1-5, vargova2021aeukaryotewideperspective pages 7-8, quirion2024mappingtheglobal pages 3-5).
- **ARL8A/B**: Lysosomes, control lysosome motility (sztul2019arfgtpasesand pages 1-2, vargova2021aeukaryotewideperspective pages 7-8, quirion2024mappingtheglobal pages 3-5).
- **ARL11/14**: Tissue-specific (macrophage/intestine), activate PLD1 in specialized trafficking (quirion2024mappingtheglobal pages 1-3, quirion2024mappingtheglobal pages 3-5).
- **TRIM23**: Multidomain fusion protein with ubiquitin-related functions (jackson2023anevolutionaryperspective pages 5-8, vargova2021aeukaryotewideperspective pages 19-20).

**No single biological process or cellular component GO term is true for all these subfamilies.** Annotating with "vesicle-mediated transport" (GO:0016192) would be wrong for ARL2 (tubulin assembly), ARL3 (ciliary cargo delivery), ARL8 (lysosome positioning). Annotating with "Golgi apparatus" (GO:0005794) would be wrong for ARF6, SAR1, ciliary ARLs, and lysosomal ARL8.

#### Problem 2: Atypical/Pseudo-GTPase Members

Multiple ARF-related proteins exhibit **non-canonical biochemical properties**:

- **ARL5C, ARL9, ARL10, ARL13A** lack the conserved catalytic **glutamine** in the G3 motif (quirion2024mappingtheglobal pages 3-5, quirion2025unfoldingarfand pages 2-4).
- **ARL16** has an atypical G3 sequence **RELGGC** instead of WDXGGQ (quirion2024mappingtheglobal pages 3-5).
- These variants are classified as **pseudoGTPases** or atypical GTPases with impaired or absent GTP hydrolysis activity (quirion2025unfoldingarfand pages 2-4).

Even the seemingly safe molecular function term **"GTP binding" (GO:0005525)** would be questionable for these members, as their nucleotide-binding properties may be altered or lost.

#### Problem 3: Taxon-Specific Functional Modules

Several ARF paralogs are **restricted to specific eukaryotic clades** or **absent from non-ciliated organisms** (see artifact-01):

- **Ciliary paralogs (ARL3, ARL6, ARL13B)** are ancient (present in LECA) but were **lost from fungi** after they lost flagella/cilia (jackson2023anevolutionaryperspective pages 5-8, vargova2021aeukaryotewideperspective pages 7-8). Annotating PTHR11711 with cilium-related GO terms would leak into yeast and other non-ciliated taxa.
- **Jotnarlogs (ARL17, ARL18, SarB)** are ancient but **absent from all opisthokonts** (animals + fungi), yet present in diverse protists (vargova2021aeukaryotewideperspective pages 1-2, jackson2023anevolutionaryperspective pages 5-8, vargova2021aeukaryotewideperspective pages 4-5). GO terms inferred from opisthokont model systems would not apply.
- **Metazoan innovations (ARF4, ARL10, ARL15, ARL19, ARIL20, TRIM23)** emerged post-LECA and are lineage-specific (jackson2023anevolutionaryperspective pages 5-8).

Any cellular component term tied to cilia, lysosomes, or metazoan-specific structures would **inappropriately annotate proteins in taxa lacking those compartments**.

#### Problem 4: This is a FAMILY Entry, Not a Domain

PTHR11711 is classified as **entry type: family**, meaning it matches **whole proteins**, not just a conserved domain. While this might suggest whole-protein function GO terms are appropriate, the **77 reported subfamilies** indicate this is effectively a **superfamily-level grouping** capturing the entire radiation of ARF-related proteins. At this level of breadth, functional homogeneity is lost.

### Recommendation: ACCEPT Current State (No GO Mappings)

**No GO terms should be added** to PTHR11711 at the family level. The appropriate action is:

- **InterPro2GO verdict**: **ACCEPT** (maintain absence of mappings).
- **DO NOT** add "GTP binding," "membrane trafficking," or any other GO term.
- **DO NOT** mark as KEEP_AS_NON_CORE or attempt to salvage with generic terms.

---

## 3. Functional Divergence Across the Family

### Evidence for Subfunctionalization and Neo-Functionalization

| Subfamily | Members | Primary Localization | Core Function | Conserved Features | Functional Divergence |
|---|---|---|---|---|---|
| ARF class I/II | ARF1, ARF3, ARF4, ARF5 | Cytosol ↔ Golgi, trans-Golgi network, endosomes | Recruit vesicle coats (COPI, AP complexes, GGAs), organize vesicle biogenesis, regulate Golgi/endomembrane trafficking, and activate lipid-modifying enzymes such as PLD1 and PI4KB (li2023thearffamily pages 3-5, quirion2024mappingtheglobal pages 1-3, vargova2021aeukaryotewideperspective pages 7-8) | Canonical small ARF GTPase fold; conserved G1-G5 motifs including G3 WDXGGQ; N-terminal amphipathic helix usually myristoylated and membrane exposed upon GTP loading; strong membrane-coupled switch behavior (li2023thearffamily pages 1-3, sztul2019arfgtpasesand pages 1-2, quirion2025unfoldingarfand pages 2-4) | Considerable redundancy among ARF1/3/4/5 in Golgi trafficking, but not complete equivalence; ARF4 has specialized ciliary cargo-targeting roles in some systems; class I/II members are more secretory-pathway-centric than ARF6, so broad trafficking/process GO terms would overgeneralize if applied to all ARF family members (li2023thearffamily pages 3-5, quirion2024mappingtheglobal pages 1-3) |
| ARF class III | ARF6 | Plasma membrane, endosomes, recycling endosomes, cortical actin-rich regions | Endocytosis, recycling, cortical actin remodeling, phosphoinositide and PLD1 signaling, membrane protrusions and motility (sztul2019arfgtpasesand pages 1-2, quirion2024mappingtheglobal pages 1-3, vargova2021aeukaryotewideperspective pages 7-8) | Retains canonical ARF switch machinery and N-terminal membrane-coupled amphipathic helix; GDP-bound structure differs substantially from ARF1 but GTP-bound state is similar, underscoring shared core mechanism with altered regulation/kinetics (quirion2025unfoldingarfand pages 2-4) | Functionally distinct from class I/II ARFs: acts mainly at cell periphery rather than Golgi. Cell motility, endocytosis, phagocytosis, and immune/cancer phenotypes are not generalizable to all ARF-family proteins (quirion2024mappingtheglobal pages 1-3, vargova2021aeukaryotewideperspective pages 7-8) |
| SAR | SAR1A, SAR1B | Endoplasmic reticulum, ER exit sites | COPII recruitment, ER-to-Golgi vesicle budding and cargo export, especially secretory cargo including lipoprotein/chylomicron-related transport (li2023thearffamily pages 3-5, quirion2024mappingtheglobal pages 1-3) | ARF-family GTPase core with membrane-associated N-terminus; shares ancestry with ARF family but represents a specialized secretory-pathway branch; conserved coat-coupled GTPase cycling (li2023thearffamily pages 1-3, jackson2023anevolutionaryperspective pages 5-8, vargova2021aeukaryotewideperspective pages 4-5) | SAR1A and SAR1B have overlapping but non-identical effector/enzyme properties; SAR1B has disease-linked specialization in chylomicron export. COPII-related functions are specific to SAR, not to the broader ARF-related family in PTHR11711 if that family includes ARLs (quirion2024mappingtheglobal pages 1-3) |
| ARL1 | ARL1 | Golgi, especially trans-Golgi network | Recruits golgins, arfaptins, GRIP-domain proteins, and Arf GEFs; supports endosome-to-TGN and Golgi trafficking (sztul2019arfgtpasesand pages 1-2, vargova2021aeukaryotewideperspective pages 7-8) | Canonical ARF-family GTPase architecture and membrane-associated N-terminus; conserved Golgi-associated regulatory logic within ancient eukaryotic ARL clade (li2023thearffamily pages 1-3, jackson2023anevolutionaryperspective pages 5-8) | Functionally linked to ARFRP1 and partly overlaps with Arl5 at the TGN, but is distinct from vesicle-coat recruiting ARFs and from ciliary ARLs; Golgi tether recruitment is not a family-wide property (vargova2021aeukaryotewideperspective pages 7-8) |
| ARL2 | ARL2 | Cytosol, mitochondria, centrosomes, basal bodies, cilia | Tubulin heterodimer biogenesis, microtubule-related processes, mitochondrial fusion, and trafficking of lipidated/prenylated cargo via effectors (sztul2019arfgtpasesand pages 1-2, quirion2024mappingtheglobal pages 1-3, quirion2024mappingtheglobal pages 3-5) | Canonical GTPase domain; part of ancient ARL2/ARL3 sister group; retains switch regions but differs from classical coat-recruiting ARFs in effectors and cell biology (jackson2023anevolutionaryperspective pages 5-8, vargova2021aeukaryotewideperspective pages 19-20) | Strongly diverged from classical vesicle-budding ARFs; mitochondrial and tubulin functions are ARL2-specific and should not drive broad GO transfer to other subfamilies (quirion2024mappingtheglobal pages 3-5) |
| ARL3 | ARL3 | Cilia, centrosomes, Golgi, mitotic structures, immune synapse | Delivery/release of lipid-modified cargo in cilia and related polarized membrane domains; cooperates with ARL13B and RP2 in ciliary trafficking (fisher2020arffamilygtpases pages 1-5, quirion2024mappingtheglobal pages 1-3, quirion2024mappingtheglobal pages 3-5) | Ancient ARF-family member with canonical GTPase fold; functionally coupled to ARL13B as GEF platform and RP2 as GAP; cilia-associated specialization conserved across eukaryotes (fisher2020arffamilygtpases pages 1-5, vargova2021aeukaryotewideperspective pages 7-8) | Highly specialized for ciliary/lipidated cargo trafficking; not interchangeable with ARL2 despite close relationship. Cilium-related GO terms would leak into non-ciliated taxa if mapped broadly to the whole family (fisher2020arffamilygtpases pages 1-5, vargova2021aeukaryotewideperspective pages 7-8) |
| ARL4-ARL6 group | ARL4A, ARL4C, ARL4D, ARL5A, ARL5B, ARL5C, ARL6 | ARL4s: plasma membrane, nucleus, endosomes/actin-associated sites; ARL5s: Golgi/endosome-related compartments; ARL6: cilia/BBSome-associated compartments | ARL4s regulate actin remodeling, migration, membrane traffic and signaling; ARL5A/B participate in endosome-to-Golgi traffic and nutrient signaling; ARL6 functions in ciliary trafficking/BBSome-related processes (sztul2019arfgtpasesand pages 1-2, quirion2024mappingtheglobal pages 1-3, vargova2021aeukaryotewideperspective pages 7-8) | All retain ARF-family ancestry and small-GTPase core, but several are biochemically atypical; ARL5C lacks the canonical catalytic glutamine, and multiple ARLs have unusual or poorly defined nucleotide cycling properties (quirion2024mappingtheglobal pages 3-5, quirion2025unfoldingarfand pages 2-4) | This is a highly heterogeneous set. ARL5C is atypical/non-canonical in the G3 region; ARL6 is a ciliopathy protein; ARL4 paralogs have signaling/cytoskeletal roles. These differences argue strongly against assigning shared whole-protein GO biological process terms across the entire ARF-related family (quirion2024mappingtheglobal pages 3-5, quirion2025unfoldingarfand pages 2-4) |
| ARL8 | ARL8A, ARL8B | Lysosomes, phagolysosomes, vacuolar/lysosomal membranes | Lysosome motility, trafficking, tethering/fusion-related processes (sztul2019arfgtpasesand pages 1-2, vargova2021aeukaryotewideperspective pages 7-8, quirion2024mappingtheglobal pages 3-5) | ARF-family core fold; notable exception in N-terminal chemistry because ARL8 proteins are acetylated rather than myristoylated, illustrating mechanistic diversity in membrane association (li2023thearffamily pages 1-3, vargova2021aeukaryotewideperspective pages 2-3) | Lysosomal specialization is ancient but not universal across ARF-related proteins. Lysosome/vacuole GO terms would be inappropriate for most ARFs/ARLs outside this branch (vargova2021aeukaryotewideperspective pages 7-8) |
| ARL10-ARL16 group | ARL10, ARL11, ARL12, ARL13A, ARL13B, ARL14, ARL15, ARL16 | Diverse and often tissue-restricted: ARL10 mitochondria/nucleus; ARL11 macrophage-associated; ARL14 stomach/intestine-restricted endomembrane compartments; ARL13B cilia; ARL16 broad but poorly defined (quirion2024mappingtheglobal pages 1-3, quirion2024mappingtheglobal pages 3-5) | Mixed functions including ciliary regulation (ARL13B), PLD1 activation and specialized trafficking (ARL11/ARL14), and likely lineage/tissue-specific signaling roles for understudied members (quirion2024mappingtheglobal pages 1-3, quirion2024mappingtheglobal pages 3-5) | Many members are biochemically atypical or insufficiently characterized; several lack the conserved catalytic glutamine or show non-canonical G3 motifs, and ARL13 proteins can carry large accessory C-terminal domains; ARL16 has atypical RELGGC G3 motif (quirion2024mappingtheglobal pages 3-5, vargova2021aeukaryotewideperspective pages 18-19, quirion2025unfoldingarfand pages 2-4) | This group contains the clearest examples of possible pseudoGTPase-like or non-canonical behavior in the family. ARL13B is a ciliary regulator/GEF platform; ARL14 activates PLD1 and participates in ESCPE-1-mediated trafficking; ARL11 is immune-cell enriched. These roles are sharply subfamily- or gene-specific (quirion2024mappingtheglobal pages 1-3, quirion2024mappingtheglobal pages 3-5, quirion2025unfoldingarfand pages 2-4) |
| ARFRP1 | ARFRP1 | Golgi/TGN | Upstream regulator of ARL1 recruitment and Golgi organization; supports trans-Golgi trafficking circuits (vargova2021aeukaryotewideperspective pages 7-8) | ARF-family GTPase core but unusual N-terminus, typically acetylated rather than myristoylated; ancient conserved eukaryotic paralog (li2023thearffamily pages 1-3, vargova2021aeukaryotewideperspective pages 2-3, vargova2021aeukaryotewideperspective pages 7-8) | Mechanistically distinct from coat-recruiting ARFs and from ciliary/lysosomal ARLs. Golgi-organizing role is specific and should not be generalized (vargova2021aeukaryotewideperspective pages 7-8) |
| TRIM23 | TRIM23/ARD1 | Endomembrane/cytosolic compartments; multidomain regulatory protein | Specialized signaling and membrane-trafficking-associated functions as an ARF-family GTPase fused to additional domains rather than a simple small GTPase (li2023thearffamily pages 1-3, jackson2023anevolutionaryperspective pages 5-8, vargova2021aeukaryotewideperspective pages 19-20) | Atypical multidomain architecture distinguishes it from canonical single-domain ARF/ARL/SAR proteins; arose by fusion of an ARF-like GTPase with additional domains, so inference from canonical ARFs is limited (jackson2023anevolutionaryperspective pages 5-8, vargova2021aeukaryotewideperspective pages 19-20) | Strongly neo-functionalized and structurally atypical; should be treated separately from core ARF/ARL proteins for annotation purposes. Any family-wide GO mapping that assumes a simple small-GTPase trafficking role would be unsafe if TRIM23-like proteins are included (jackson2023anevolutionaryperspective pages 5-8, vargova2021aeukaryotewideperspective pages 19-20) |


*Table: This table summarizes the principal ARF-family subgroups, their localizations, conserved biochemical features, and major functional specializations. It is useful for judging whether whole-family GO annotation would be too broad for the heterogeneous ARF-related PTHR11711 family.*

Key patterns of functional divergence documented in recent literature (2019-2025):

#### Vesicle Coat Recruitment (ARF1/3/4/5 vs SAR1)

- **ARF1-related proteins** recruit **COPI, AP complexes, GGAs** at the Golgi and endosomes for retrograde and endosome-Golgi traffic (li2023thearffamily pages 3-5, quirion2024mappingtheglobal pages 1-3, vargova2021aeukaryotewideperspective pages 7-8).
- **SAR1** recruits **COPII** at ER exit sites for ER-to-Golgi anterograde transport (li2023thearffamily pages 3-5, quirion2024mappingtheglobal pages 1-3).
- These are **mutually exclusive pathways** with different coat complexes, different subcellular locations, and opposite directionality. They cannot be described by the same process GO term.

#### Plasma Membrane vs Golgi Specialization (ARF6 vs ARF1)

- **ARF6** acts at the **plasma membrane and recycling endosomes**, regulating endocytosis, phagocytosis, cell motility, and actin dynamics via activation of phospholipase D1 (PLD1) and phosphatidylinositol kinases (sztul2019arfgtpasesand pages 1-2, quirion2024mappingtheglobal pages 1-3, vargova2021aeukaryotewideperspective pages 7-8, quirion2024mappingtheglobal pages 3-5).
- **ARF1** acts at the **Golgi**, recruiting coat proteins for secretory pathway organization (li2023thearffamily pages 3-5, vargova2021aeukaryotewideperspective pages 7-8).
- These paralogs occupy **opposite cellular territories** and should not share cellular component annotations.

#### Ciliary vs Non-Ciliary Paralogs

- **ARL3, ARL6, ARL13B** are **ciliary specialists** involved in trafficking lipid-modified (myristoylated/prenylated) cargo proteins into and within primary cilia (fisher2020arffamilygtpases pages 1-5, vargova2021aeukaryotewideperspective pages 7-8, quirion2024mappingtheglobal pages 3-5).
- **ARL13B acts as a GEF** for ARL3, representing a **GTPase-on-GTPase regulatory module** unique to cilia (quirion2024mappingtheglobal pages 3-5).
- These paralogs are **repeatedly lost** in non-ciliated lineages (e.g., fungi post-flagellar loss) (jackson2023anevolutionaryperspective pages 5-8), demonstrating that ciliary functions are **not family-wide traits**.

#### Tubulin Assembly vs Membrane Traffic (ARL2)

- **ARL2** interacts with **tubulin-binding cochaperone TBCD** and β-tubulin to regulate **cytosolic α/β-tubulin heterodimer assembly**, not membrane trafficking (sztul2019arfgtpasesand pages 1-2, quirion2024mappingtheglobal pages 3-5).
- ARL2 also localizes to **mitochondria** where it promotes **mitochondrial fusion** (quirion2024mappingtheglobal pages 3-5).
- This is a **complete functional departure** from vesicle-based trafficking; annotating ARL2-containing proteins with trafficking terms would be wrong.

#### Lysosome vs Golgi Localization (ARL8 vs ARL1)

- **ARL8A/B** localize to **lysosomes/phagolysosomes** and regulate lysosome motility via kinesin recruitment (sztul2019arfgtpasesand pages 1-2, vargova2021aeukaryotewideperspective pages 7-8, quirion2024mappingtheglobal pages 3-5).
- **ARL1** localizes to the **Golgi/TGN** and recruits golgins (vargova2021aeukaryotewideperspective pages 7-8).
- These are **opposite organelles** in the endomembrane system; cellular component GO terms cannot be shared.

### Biochemically Atypical Members (Candidate Pseudo-Enzymes)

Several ARF-related proteins lack canonical GTPase motifs or exhibit non-standard biochemistry:

- **ARL5C, ARL9, ARL10, ARL13A**: Missing the conserved catalytic **glutamine** in the G3 motif, suggesting **impaired or absent GTP hydrolysis** (quirion2024mappingtheglobal pages 3-5, quirion2025unfoldingarfand pages 2-4).
- **ARL16**: Non-canonical G3 motif **RELGGC**; biochemical properties unknown (quirion2024mappingtheglobal pages 3-5).
- **TRIM23**: Multidomain protein containing an ARF-family GTPase domain fused to ubiquitin-related domains (tripartite motif), representing **neo-functionalization** via domain fusion (jackson2023anevolutionaryperspective pages 5-8, vargova2021aeukaryotewideperspective pages 18-19, vargova2021aeukaryotewideperspective pages 19-20).

These atypical members likely function via **non-canonical mechanisms** distinct from classical GTP-dependent switch behavior, further undermining the applicability of standard GTPase GO terms at the family level (quirion2025unfoldingarfand pages 2-4).

### Tissue-Specific Expression and Specialization

Recent high-throughput interactome studies reveal **extreme tissue restriction** for some ARF-related proteins:

- **ARL14**: Expression restricted to **stomach and intestines**, where it activates PLD1 and participates in ESCPE-1-mediated endosomal trafficking (quirion2024mappingtheglobal pages 1-3, quirion2024mappingtheglobal pages 3-5).
- **ARL11**: Enriched in **macrophages**, activates PLD1 to promote phagocytosis (quirion2024mappingtheglobal pages 1-3).

These tissue-specific paralogs should not drive annotation of PTHR11711-matching proteins in **other tissues or organisms lacking those cell types**.

---

## 4. Taxonomic Scope

### LECA Complexity and Pan-Eukaryotic Distribution

Comprehensive phylogenetic analyses reconstructed the **last eukaryotic common ancestor (LECA)** as possessing **15-16 ARF family paralogs** (vargova2021aeukaryotewideperspective pages 1-2, jackson2023anevolutionaryperspective pages 5-8, vargova2021aeukaryotewideperspective pages 4-5):

| ARF paralog | LECA presence | Distribution across major eukaryotic clades | Pan-eukaryotic vs restricted | Notes on lineage-specific losses/gains |
|---|---|---|---|---|
| Arf1 | Yes | Broadly distributed across Opisthokonta (metazoans + fungi), plants, Amoebozoa, SAR, and Excavata/metamonads (vargova2021aeukaryotewideperspective pages 4-5, vargova2021aeukaryotewideperspective pages 7-8) | Pan-eukaryotic core paralog | Ancestral secretory-pathway paralog; expanded repeatedly in lineage-specific duplications, including metazoan Arf1/Arf4 classes and yeast Arf1/Arf2 duplication (jackson2023anevolutionaryperspective pages 5-8, vargova2021aeukaryotewideperspective pages 7-8) |
| Arf6 | Yes | Widely distributed across major eukaryotic groups, with ancestral presence newly supported by broad phylogenetic sampling (vargova2021aeukaryotewideperspective pages 1-2, vargova2021aeukaryotewideperspective pages 4-5) | Nearly pan-eukaryotic | Some highly diverged sequences complicate recognition; associated mainly with plasma membrane/endosomal functions rather than Golgi roles (vargova2021aeukaryotewideperspective pages 7-8) |
| Arl1 | Yes | Broadly distributed in opisthokonts, plants, SAR, Amoebozoa, and other major eukaryotic lineages (vargova2021aeukaryotewideperspective pages 4-5, vargova2021aeukaryotewideperspective pages 7-8) | Pan-eukaryotic core paralog | Conserved Golgi/TGN-associated paralog; functionally linked to Arfrp1. Retained in many lineages even when other ARLs are lost (vargova2021aeukaryotewideperspective pages 7-8) |
| Arl2 | Yes | Broadly distributed across major eukaryotic clades (vargova2021aeukaryotewideperspective pages 4-5, vargova2021aeukaryotewideperspective pages 7-8) | Pan-eukaryotic core paralog | Ancient paralog associated with tubulin/mitochondrial functions; sister to Arl3 in phylogenies (vargova2021aeukaryotewideperspective pages 19-20) |
| Arl3 | Yes | Broad but patchy owing to loss in non-ciliated/non-flagellated lineages; present across many ciliated eukaryotes in opisthokonts, plants/protists, SAR, Excavata (jackson2023anevolutionaryperspective pages 5-8, vargova2021aeukaryotewideperspective pages 7-8) | Broadly distributed but cilium-linked | Ciliary ARL; lost in fungal lineages after loss of flagella/cilia. Not expected in secondarily non-ciliated taxa (jackson2023anevolutionaryperspective pages 5-8, vargova2021aeukaryotewideperspective pages 7-8) |
| Arl5 | Yes | Broadly distributed across major clades, though absent from some derived fungal lineages (jackson2023anevolutionaryperspective pages 5-8, vargova2021aeukaryotewideperspective pages 7-8) | Broad but not universal in extant taxa | Lost in stem Ascomycota on the yeast lineage; TGN/endosome-related paralog (jackson2023anevolutionaryperspective pages 5-8, vargova2021aeukaryotewideperspective pages 7-8) |
| Arl6 | Yes | Broadly distributed in many eukaryotes but absent in non-ciliated/non-flagellated taxa; present in animals and many protists (vargova2021aeukaryotewideperspective pages 1-2, jackson2023anevolutionaryperspective pages 5-8, vargova2021aeukaryotewideperspective pages 7-8) | Broadly distributed but cilium-linked | Another ciliary paralog; lost from fungi with loss of flagella. Ancient, not metazoan-specific (vargova2021aeukaryotewideperspective pages 1-2, jackson2023anevolutionaryperspective pages 5-8) |
| Arl8 | Yes | Broadly distributed across major clades, including metazoans and plants; absent in some reduced lineages such as budding yeast (jackson2023anevolutionaryperspective pages 5-8, vargova2021aeukaryotewideperspective pages 7-8) | Broad but not universal in extant taxa | Ancient lysosome/vacuole-associated paralog; lost late in Saccharomyces lineage (jackson2023anevolutionaryperspective pages 5-8) |
| Arl13 | Yes | Broadly distributed across ciliated eukaryotes in multiple supergroups; absent from non-ciliated lineages and lineages that lost flagella/cilia (vargova2021aeukaryotewideperspective pages 1-2, jackson2023anevolutionaryperspective pages 5-8, vargova2021aeukaryotewideperspective pages 7-8) | Broadly distributed but cilium-linked | Ciliary paralog with strong evidence for ancestral origin; lost from fungi with loss of flagella. Domain architecture diversified substantially in some lineages (vargova2021aeukaryotewideperspective pages 1-2, vargova2021aeukaryotewideperspective pages 18-19) |
| Arl16 | Yes | Broadly distributed across major eukaryotic groups outside some opisthokont sublineages (vargova2021aeukaryotewideperspective pages 1-2, vargova2021aeukaryotewideperspective pages 4-5) | Broad but not universal in extant taxa | Lost early on the lineage leading to Holozoa + fungi after opisthokont divergence in some scenarios; MAD rooting places Arl16 as an early-branching clade (vargova2021aeukaryotewideperspective pages 4-5, vargova2021aeukaryotewideperspective pages 19-20) |
| Arfrp1 | Yes | Broadly distributed across major eukaryotic clades (vargova2021aeukaryotewideperspective pages 4-5, vargova2021aeukaryotewideperspective pages 7-8) | Pan-eukaryotic core paralog | Ancient Golgi-associated paralog functionally tied to Arl1 recruitment; retained in many lineages despite broad losses elsewhere (vargova2021aeukaryotewideperspective pages 7-8) |
| Sar1 | Yes | Broadly distributed across all major sampled eukaryotic clades (vargova2021aeukaryotewideperspective pages 4-5, vargova2021aeukaryotewideperspective pages 7-8) | Pan-eukaryotic core paralog | Core ER/COPII paralog; duplicated in vertebrates into SAR1A and SAR1B, and present in reduced systems such as Giardia (quirion2024mappingtheglobal pages 1-3, vargova2021aeukaryotewideperspective pages 7-8) |
| Arl17 | Yes | Present in diverse non-opisthokont eukaryotes; absent from virtually all metazoans and fungi/opisthokonts (vargova2021aeukaryotewideperspective pages 1-2, jackson2023anevolutionaryperspective pages 5-8) | Restricted; jotnarlog | Ancient eukaryotic paralog secondarily lost from opisthokonts; qualifies as a jotnarlog. Also exhibits unusual domain architectures in some taxa (jackson2023anevolutionaryperspective pages 5-8, vargova2021aeukaryotewideperspective pages 18-19) |
| Arl18 | Yes | Present in diverse non-opisthokont lineages but lost early before Amoebozoa divergence and absent from opisthokonts (jackson2023anevolutionaryperspective pages 5-8, vargova2021aeukaryotewideperspective pages 4-5) | Restricted; jotnarlog | Ancient but absent from opisthokonts; another jotnarlog. Sister relationship with Arl8 is supported in backbone phylogeny (vargova2021aeukaryotewideperspective pages 19-20) |
| SarB | Yes | Present in multiple non-opisthokont lineages; absent from metazoans and fungi/opisthokonts (vargova2021aeukaryotewideperspective pages 1-2, jackson2023anevolutionaryperspective pages 5-8, vargova2021aeukaryotewideperspective pages 4-5) | Restricted; jotnarlog | Ancient Sar-like paralog distinct from Sar1; lost from opisthokonts and thus another jotnarlog. Supports unexpectedly high LECA complexity (vargova2021aeukaryotewideperspective pages 4-5, vargova2021aeukaryotewideperspective pages 19-20) |
| Arf4 (metazoan/holozoan innovation from ancestral Arf1) | No | Mainly holozoans/metazoans; not inferred for LECA (jackson2023anevolutionaryperspective pages 5-8) | Restricted to holozoan/metazoan lineage | Emerged on the holozoan stem from ancestral Arf1 duplication; part of lineage-specific expansion rather than ancient pan-eukaryotic complement (jackson2023anevolutionaryperspective pages 5-8) |
| Arl15 | No | Holozoan/metazoan lineage (jackson2023anevolutionaryperspective pages 5-8) | Restricted | Emerged on holozoan stem; origin obscured by sequence divergence (jackson2023anevolutionaryperspective pages 5-8) |
| Arl19 | No | Early holozoans/metazoans; later lost in mammals/humans (jackson2023anevolutionaryperspective pages 5-8) | Restricted | Holozoan innovation, later duplicated to Arl4 in metazoans; subsequently lost on some vertebrate/mammalian branches (jackson2023anevolutionaryperspective pages 5-8) |
| Arl20 | No | Some holozoan protist/animal-adjacent lineages; absent from vertebrates (jackson2023anevolutionaryperspective pages 5-8) | Restricted | Emerged later in holozoan evolution and was lost before vertebrate emergence (jackson2023anevolutionaryperspective pages 5-8) |
| Arl10 | No | Metazoans/vertebrates (jackson2023anevolutionaryperspective pages 5-8) | Restricted | Newer metazoan paralog added after LECA; not appropriate for deep ancestral functional generalization (jackson2023anevolutionaryperspective pages 5-8) |
| TRIM23 | No | Metazoans (jackson2023anevolutionaryperspective pages 5-8, vargova2021aeukaryotewideperspective pages 18-19) | Restricted | Multidomain ARF-family derivative that likely arose in early metazoan evolution by domain fusion; should not be used to infer ancestral family-wide functions (jackson2023anevolutionaryperspective pages 5-8, vargova2021aeukaryotewideperspective pages 18-19) |


*Table: This table summarizes which ARF-family paralogs were already present in LECA and how they are distributed across major eukaryotic clades. It is useful for GO review because it shows that some paralogs are broadly conserved, whereas others are clade-restricted or cilium-dependent and therefore unsuitable for family-wide process/component annotation.*

#### Pan-Eukaryotic Core Paralogs

The following are broadly conserved across animals, fungi, plants, and diverse protists:

- **Arf1, Arl1, Arl2, Arfrp1, Sar1** (vargova2021aeukaryotewideperspective pages 4-5, vargova2021aeukaryotewideperspective pages 7-8).

These represent the **ancestral secretory/trafficking machinery** and might be candidates for conserved GO annotation—*except* that even within this set, **functional divergence is extreme** (Arf1 vs Sar1 recruit different coats; Arl2 does tubulin assembly, not trafficking).

#### Cilium-Linked Paralogs (Lost in Non-Ciliated Taxa)

- **Arl3, Arl6, Arl13**: Ancient (LECA-derived) but **repeatedly lost** in lineages that lost cilia/flagella, including:
  - **Fungi** (lost after flagellar loss on the fungal stem) (jackson2023anevolutionaryperspective pages 5-8, vargova2021aeukaryotewideperspective pages 7-8).
  - **Other secondarily non-ciliated eukaryotes**.

**Implication**: Cilium-related GO terms (e.g., "cilium assembly," "ciliary basal body") would **inappropriately annotate** PTHR11711-matching proteins in **budding yeast, fission yeast, and other non-ciliated fungi**.

#### Jotnarlogs (Ancient but Opisthokont-Absent)

Three ARF paralogs are **ancient (LECA-derived)** but **secondarily lost from all opisthokonts** (animals + fungi):

- **Arl17, Arl18, SarB** (vargova2021aeukaryotewideperspective pages 1-2, jackson2023anevolutionaryperspective pages 5-8, vargova2021aeukaryotewideperspective pages 4-5).

These "jotnarlogs" are present in diverse protists (SAR clade, Excavata, plants) but **invisible in standard model organisms** (human, mouse, yeast, fly, worm). Functions inferred from mammalian studies **cannot apply** to these paralogs, and vice versa.

#### Metazoan-Specific Innovations

Multiple ARF paralogs arose **post-LECA** in the holozoan/metazoan lineage:

- **Arf4, Arl10, Arl15, Arl19, Arl20, TRIM23** (jackson2023anevolutionaryperspective pages 5-8).

These are **absent from non-metazoans** (fungi, plants, most protists). GO terms describing metazoan-specific processes (e.g., immune synapse assembly, cancer cell invasion) linked to these paralogs would **leak into plant/fungal proteins** if applied at the family level.

### Scale and Diversity: 11,970 Taxa, 77 Subfamilies

The InterPro entry reports **41,271 proteins across 11,970 taxa** with **77 subfamilies**. This immense scale reflects:

1. Broad eukaryotic sampling across all major supergroups.
2. Lineage-specific duplications (e.g., vertebrate whole-genome duplications generating Arf1-5, Sar1A/B, Arl8A/B paralogs) (jackson2023anevolutionaryperspective pages 5-8).
3. Taxon-specific expansions (e.g., expanded ARF complements in some protist lineages).

**Implication**: Process and component GO terms that apply in one taxon (e.g., "Golgi apparatus" in animals) may **not exist or function equivalently** in other taxa represented in PTHR11711 (e.g., plant Golgi, protist contractile vacuoles, archaeal homologs if any).

---

## 5. Over-Annotation Verdict and GO Action Recommendations

### Summary Verdict: Current Absence of GO Mappings is Scientifically Sound

**PTHR11711 should NOT receive family-wide InterPro2GO mappings.** The absence of GO terms is appropriate given:

1. **Extreme functional heterogeneity**: 12+ subfamilies with opposite localizations (ER, Golgi, endosomes, plasma membrane, lysosomes, mitochondria, cilia) and incompatible biological roles.
2. **Presence of atypical/pseudo-GTPase members**: Several paralogs lack canonical catalytic residues or exhibit non-standard nucleotide cycling.
3. **Taxon-restricted functions**: Ciliary paralogs absent from non-ciliated organisms; jotnarlogs absent from opisthokonts; metazoan innovations absent from plants/fungi.
4. **Family-level entry masking subfunctionalization**: 77 subfamilies indicate this is effectively a superfamily; annotation should occur at finer granularity.

### Recommended GO Action Pattern: **ACCEPT**

- **Action**: **ACCEPT** the current state (no InterPro2GO mappings for PTHR11711).
- **Do NOT add** any GO terms, including:
  - **Molecular function**: "GTP binding" (GO:0005525) would be wrong for pseudo-GTPases.
  - **Biological process**: "vesicle-mediated transport," "small GTPase mediated signal transduction," etc., would over-annotate non-trafficking paralogs (ARL2, ciliary ARLs).
  - **Cellular component**: "Golgi," "membrane," "cilium," "lysosome" are all subfamily-specific.
- **Do NOT mark as KEEP_AS_NON_CORE** or attempt to salvage with ultra-generic terms; the problem is structural, not just specificity.

### Alternative Recommendation for InterPro Curation

Consider whether **PTHR11711 should be subdivided** into separate InterPro entries for major functional clades:

- **PTHR11711:SF001** → ARF1-type (Golgi coat recruitment)
- **PTHR11711:SF002** → ARF6-type (plasma membrane/endocytosis)
- **PTHR11711:SF003** → SAR-type (ER/COPII)
- **PTHR11711:SF004** → Ciliary ARLs (ARL3/6/13B)
- **PTHR11711:SF005** → Lysosomal ARLs (ARL8)
- **PTHR11711:SF006** → Tubulin-regulatory ARLs (ARL2)
- ...and so on.

This would enable **subfamily-specific GO annotation** without inappropriate family-wide over-annotation. However, **if such subdivision is not feasible**, the current approach (no family-level GO terms) is the only scientifically defensible option.

### Key Experimental vs Inferred Evidence

- **Structural evidence**: Crystal structures for ARF1 and ARF6 (experimental) define the GTPase fold and membrane-insertion mechanism (quirion2025unfoldingarfand pages 2-4).
- **Functional evidence**: Coat recruitment, lipid enzyme activation, ciliary trafficking roles supported by decades of biochemical, cell biological, and genetic studies in model organisms (li2023thearffamily pages 1-3, sztul2019arfgtpasesand pages 1-2, li2023thearffamily pages 3-5, fisher2020arffamilygtpases pages 1-5, quirion2024mappingtheglobal pages 1-3, vargova2021aeukaryotewideperspective pages 7-8, quirion2024mappingtheglobal pages 3-5).
- **Evolutionary inference**: LECA complexity and paralog distribution inferred from phylogenetic analyses of >2,000 curated sequences across 114 eukaryotic species (vargova2021aeukaryotewideperspective pages 1-2, jackson2023anevolutionaryperspective pages 5-8, vargova2021aeukaryotewideperspective pages 4-5).
- **Atypical member properties**: Pseudo-GTPase classification based on sequence motif analysis and emerging biophysical data (quirion2024mappingtheglobal pages 3-5, quirion2025unfoldingarfand pages 2-4).

---

## Conclusion

InterPro entry **PTHR11711** represents the **entire ARF-related protein superfamily**, encompassing functionally divergent subfamilies with incompatible cellular roles, taxon-restricted distributions, and atypical biochemical properties. The **current absence of InterPro2GO mappings is scientifically appropriate** and reflects sound judgment. Assigning any specific GO biological process or cellular component term at the family level would **systematically over-annotate** proteins across the 41,271 members in 11,970 taxa. The recommended action is to **ACCEPT** the current state and **maintain zero GO mappings** for PTHR11711. Subfamily-specific annotation would be preferable but requires finer-grained InterPro entries.

References

1. (sztul2019arfgtpasesand pages 1-2): Elizabeth Sztul, Pei-Wen Chen, James E. Casanova, Jacqueline Cherfils, Joel B. Dacks, David G. Lambright, Fang-Jen S. Lee, Paul A. Randazzo, Lorraine C. Santy, Annette Schürmann, Ilka Wilhelmi, Marielle E. Yohe, and Richard A. Kahn. Arf gtpases and their gefs and gaps: concepts and challenges. Molecular Biology of the Cell, 30:1249-1271, May 2019. URL: https://doi.org/10.1091/mbc.e18-12-0820, doi:10.1091/mbc.e18-12-0820. This article has 290 citations and is from a domain leading peer-reviewed journal.

2. (vargova2021aeukaryotewideperspective pages 1-2): Romana Vargová, Jeremy G. Wideman, Romain Derelle, Vladimír Klimeš, Richard A. Kahn, Joel B. Dacks, and Marek Eliáš. A eukaryote-wide perspective on the diversity and evolution of the arf gtpase protein family. Genome Biology and Evolution, Nov 2021. URL: https://doi.org/10.1093/gbe/evab157, doi:10.1093/gbe/evab157. This article has 47 citations and is from a domain leading peer-reviewed journal.

3. (quirion2025unfoldingarfand pages 2-4): Laura Quirion, Regina Strakhova, Matthew J. Smith, and Jean-François Côté. Unfolding arf and arl gtpases: from biophysics to systems-level insights. Frontiers in Molecular Biosciences, Dec 2025. URL: https://doi.org/10.3389/fmolb.2025.1712544, doi:10.3389/fmolb.2025.1712544. This article has 0 citations.

4. (li2023thearffamily pages 1-3): Fu‐Long Li and Kun‐Liang Guan. The arf family gtpases: regulation of vesicle biogenesis and beyond. BioEssays, Mar 2023. URL: https://doi.org/10.1002/bies.202200214, doi:10.1002/bies.202200214. This article has 18 citations and is from a peer-reviewed journal.

5. (vargova2021aeukaryotewideperspective pages 2-3): Romana Vargová, Jeremy G. Wideman, Romain Derelle, Vladimír Klimeš, Richard A. Kahn, Joel B. Dacks, and Marek Eliáš. A eukaryote-wide perspective on the diversity and evolution of the arf gtpase protein family. Genome Biology and Evolution, Nov 2021. URL: https://doi.org/10.1093/gbe/evab157, doi:10.1093/gbe/evab157. This article has 47 citations and is from a domain leading peer-reviewed journal.

6. (jackson2023anevolutionaryperspective pages 5-8): Catherine L. Jackson, Julie Ménétrey, Mandeep Sivia, Joel B. Dacks, and Marek Eliáš. An evolutionary perspective on arf family gtpases. Current Opinion in Cell Biology, 85:102268, Dec 2023. URL: https://doi.org/10.1016/j.ceb.2023.102268, doi:10.1016/j.ceb.2023.102268. This article has 16 citations and is from a peer-reviewed journal.

7. (li2023thearffamily pages 3-5): Fu‐Long Li and Kun‐Liang Guan. The arf family gtpases: regulation of vesicle biogenesis and beyond. BioEssays, Mar 2023. URL: https://doi.org/10.1002/bies.202200214, doi:10.1002/bies.202200214. This article has 18 citations and is from a peer-reviewed journal.

8. (vargova2021aeukaryotewideperspective pages 7-8): Romana Vargová, Jeremy G. Wideman, Romain Derelle, Vladimír Klimeš, Richard A. Kahn, Joel B. Dacks, and Marek Eliáš. A eukaryote-wide perspective on the diversity and evolution of the arf gtpase protein family. Genome Biology and Evolution, Nov 2021. URL: https://doi.org/10.1093/gbe/evab157, doi:10.1093/gbe/evab157. This article has 47 citations and is from a domain leading peer-reviewed journal.

9. (quirion2024mappingtheglobal pages 1-3): Laura Quirion, Amélie Robert, Jonathan Boulais, Shiying Huang, Gabriela Bernal Astrain, Regina Strakhova, Chang Hwa Jo, Yacine Kherdjemil, Denis Faubert, Marie-Pier Thibault, Marie Kmita, Jeremy M. Baskin, Anne-Claude Gingras, Matthew J. Smith, and Jean-François Côté. Mapping the global interactome of the arf family reveals spatial organization in cellular signaling pathways. Journal of Cell Science, Apr 2024. URL: https://doi.org/10.1242/jcs.262140, doi:10.1242/jcs.262140. This article has 16 citations and is from a domain leading peer-reviewed journal.

10. (quirion2024mappingtheglobal pages 3-5): Laura Quirion, Amélie Robert, Jonathan Boulais, Shiying Huang, Gabriela Bernal Astrain, Regina Strakhova, Chang Hwa Jo, Yacine Kherdjemil, Denis Faubert, Marie-Pier Thibault, Marie Kmita, Jeremy M. Baskin, Anne-Claude Gingras, Matthew J. Smith, and Jean-François Côté. Mapping the global interactome of the arf family reveals spatial organization in cellular signaling pathways. Journal of Cell Science, Apr 2024. URL: https://doi.org/10.1242/jcs.262140, doi:10.1242/jcs.262140. This article has 16 citations and is from a domain leading peer-reviewed journal.

11. (fisher2020arffamilygtpases pages 1-5): Skylar Fisher, Damian Kuna, Tamara Caspary, Richard A. Kahn, and Elizabeth Sztul. Arf family gtpases with links to cilia. American Journal of Physiology-Cell Physiology, 319:C404-C418, Aug 2020. URL: https://doi.org/10.1152/ajpcell.00188.2020, doi:10.1152/ajpcell.00188.2020. This article has 44 citations.

12. (vargova2021aeukaryotewideperspective pages 19-20): Romana Vargová, Jeremy G. Wideman, Romain Derelle, Vladimír Klimeš, Richard A. Kahn, Joel B. Dacks, and Marek Eliáš. A eukaryote-wide perspective on the diversity and evolution of the arf gtpase protein family. Genome Biology and Evolution, Nov 2021. URL: https://doi.org/10.1093/gbe/evab157, doi:10.1093/gbe/evab157. This article has 47 citations and is from a domain leading peer-reviewed journal.

13. (vargova2021aeukaryotewideperspective pages 4-5): Romana Vargová, Jeremy G. Wideman, Romain Derelle, Vladimír Klimeš, Richard A. Kahn, Joel B. Dacks, and Marek Eliáš. A eukaryote-wide perspective on the diversity and evolution of the arf gtpase protein family. Genome Biology and Evolution, Nov 2021. URL: https://doi.org/10.1093/gbe/evab157, doi:10.1093/gbe/evab157. This article has 47 citations and is from a domain leading peer-reviewed journal.

14. (vargova2021aeukaryotewideperspective pages 18-19): Romana Vargová, Jeremy G. Wideman, Romain Derelle, Vladimír Klimeš, Richard A. Kahn, Joel B. Dacks, and Marek Eliáš. A eukaryote-wide perspective on the diversity and evolution of the arf gtpase protein family. Genome Biology and Evolution, Nov 2021. URL: https://doi.org/10.1093/gbe/evab157, doi:10.1093/gbe/evab157. This article has 47 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PTHR11711-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR11711-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. quirion2025unfoldingarfand pages 2-4
2. sztul2019arfgtpasesand pages 1-2
3. vargova2021aeukaryotewideperspective pages 7-8
4. quirion2024mappingtheglobal pages 3-5
5. jackson2023anevolutionaryperspective pages 5-8
6. quirion2024mappingtheglobal pages 1-3
7. vargova2021aeukaryotewideperspective pages 19-20
8. vargova2021aeukaryotewideperspective pages 1-2
9. li2023thearffamily pages 1-3
10. vargova2021aeukaryotewideperspective pages 2-3
11. li2023thearffamily pages 3-5
12. fisher2020arffamilygtpases pages 1-5
13. vargova2021aeukaryotewideperspective pages 4-5
14. vargova2021aeukaryotewideperspective pages 18-19
15. https://doi.org/10.1091/mbc.e18-12-0820,
16. https://doi.org/10.1093/gbe/evab157,
17. https://doi.org/10.3389/fmolb.2025.1712544,
18. https://doi.org/10.1002/bies.202200214,
19. https://doi.org/10.1016/j.ceb.2023.102268,
20. https://doi.org/10.1242/jcs.262140,
21. https://doi.org/10.1152/ajpcell.00188.2020,