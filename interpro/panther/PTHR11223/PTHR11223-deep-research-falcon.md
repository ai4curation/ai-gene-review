---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-21T20:02:05.022932'
end_time: '2026-06-21T20:14:04.984848'
duration_seconds: 719.96
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR11223
  interpro_name: EXPORTIN 1/5
  interpro_short_name: Not specified
  interpro_type: family
  interpro_integrated: IPR045065
  member_databases: Not specified
  n_proteins: '10061'
  n_taxa: '9089'
  n_subfamilies: '14'
  interpro2go_terms: None mapped (no InterPro2GO terms for this entry)
  interpro_description: Not specified in InterPro
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 23
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: PTHR11223-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR11223-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: PTHR11223-deep-research-falcon_artifacts/artifact-02.md
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
- **Accession:** PTHR11223
- **Name:** EXPORTIN 1/5
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** IPR045065
- **Member database signatures:** Not specified
- **Scale:** 10061 proteins across 9089 taxa, 14 subfamilies
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
**PTHR11223 (EXPORTIN 1/5)**, structured to support GO annotation review.

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
- **Accession:** PTHR11223
- **Name:** EXPORTIN 1/5
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** IPR045065
- **Member database signatures:** Not specified
- **Scale:** 10061 proteins across 9089 taxa, 14 subfamilies
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
**PTHR11223 (EXPORTIN 1/5)**, structured to support GO annotation review.

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


# Comprehensive Research Report: InterPro Entry PTHR11223 (EXPORTIN 1/5)

## Executive Summary

InterPro entry PTHR11223 (EXPORTIN 1/5) is a **family-level** signature matching 10,061 proteins across 9,089 taxa with 14 subfamilies. Currently, **no InterPro2GO terms are mapped** to this entry. Our comprehensive analysis of recent literature (2015-2026) reveals that this family encompasses functionally divergent exportin subfamilies with distinct cargo specificities that cannot be uniformly annotated with cargo-specific GO terms. The current unmapped state is appropriate and defensible.

---

## 1. Family Definition and Biochemistry

### Molecular Architecture and Fold

PTHR11223 members belong to the karyopherin-β superfamily of nuclear transport receptors, characterized by a conserved **HEAT-repeat architecture** (wing2022karyopherinmediatednucleocytoplasmictransport pages 1-6, matsuura2016mechanisticinsightsfrom pages 1-2, yang2023nucleartransportproteins pages 1-2). HEAT repeats (named for Huntingtin, Elongation factor 3, protein phosphatase 2A, and TOR kinase) are structural modules composed of paired antiparallel α-helices that stack to form an elongated, superhelical toroid structure with conformational flexibility suited for cargo recognition and Ran-coupled switching during nuclear transport (matsuura2016mechanisticinsightsfrom pages 1-2, chen2025therapeutictargetingof pages 1-3).

| Protein name | Structural fold and architecture | Conserved domains/motifs | Key functional residues | RanGTP binding sites | Cargo type and binding mechanism |
|---|---|---|---|---|---|
| Exportin 1 / CRM1 / XPO1 | Karyopherin-β exportin built from ~21 tandem HEAT repeats forming a flexible toroid/superhelix; HEAT repeats 11-12 form the hydrophobic NES-binding groove; conformational switching between closed and open states is coupled to cargo and Ran binding (matsuura2016mechanisticinsightsfrom pages 1-2, chen2025therapeutictargetingof pages 1-3) | CRIME domain at the N-terminus for Ran interaction; acidic loop between HEAT 9A/9B; C-terminal helix/tail; leucine-rich NES-binding groove with five hydrophobic pockets in HEAT 11-12; FG-nucleoporin interaction surfaces distinct from the NES groove (matsuura2016mechanisticinsightsfrom pages 1-2, chen2025therapeutictargetingof pages 1-3) | Lys568 acts as a specificity filter through main-chain H-bonding to NES peptides; Glu571 lies in the groove and alters select NES recognition when mutated; cancer/drug-mechanism literature also highlights groove residues such as Cys528 and functional residues including A541, F572, Q742, and S1055 in cargo export regulation (fung2017nuclearexportreceptor pages 1-8, chen2025therapeutictargetingof pages 1-3) | RanGTP binds the N-terminal CRIME domain and cooperatively stabilizes the open, cargo-binding conformation; RanBP1/RanGAP promote cytoplasmic disassembly of the XPO1-RanGTP-cargo complex (matsuura2016mechanisticinsightsfrom pages 1-2, chen2025therapeutictargetingof pages 1-3) | Primarily exports proteins bearing leucine-rich NESs; also exports some RNA/protein assemblies indirectly via adaptors. Cargo binds the hydrophobic NES groove, RanGTP promotes ternary complex formation in the nucleus, FG-nucleoporin contacts mediate NPC passage, and RanBP1/RanGAP drive cargo release in the cytoplasm (fung2017nuclearexportreceptor pages 1-8, matsuura2016mechanisticinsightsfrom pages 1-2, bruserud2025xpo1exportin1inacute pages 1-2) |
| Exportin 5 / XPO5 | Karyopherin-β exportin with HEAT-repeat ring/closed architecture; structural studies describe a largely HEAT-repeat-based, ring-shaped export receptor specialized for double-stranded RNA hairpins rather than short peptide NESs (wang2020xpo5promotesprimary pages 1-2, kalia2025analysisofexportins pages 1-2) | HEAT-repeat scaffold; RNA end-recognition surfaces that contact 5′ and 3′ ends including the characteristic 2-nt 3′ overhang of pre-miRNA; lacks the CRM1-style leucine-rich NES groove function (wang2020xpo5promotesprimary pages 1-2) | Specific residues are not fully enumerated in the available contexts, but structural work cited in the XPO5 literature shows HEAT-repeat residues forming hydrogen bonds to the 5′ and 3′ ends of pre-miRNA, especially the 2-nt 3′ overhang; selectivity depends strongly on hairpin architecture and overhang features (wang2020xpo5promotesprimary pages 1-2) | Canonical export requires RanGTP-dependent formation of the XPO5-pre-miRNA-RanGTP complex; however, XPO5 also binds some structured pri-miRNAs and other RNAs in a RanGTP-independent manner for noncanonical processing-related functions (wang2020xpo5promotesprimary pages 1-2) | Exports pre-miRNA hairpins and other structured RNAs such as certain tRNAs/minihelix viral RNAs; binding is shape-dependent, recognizing dsRNA stem-loop architecture with proper ends/3′ overhang rather than peptide motifs. In addition to export, XPO5 can bind clustered pri-miRNAs and promote Microprocessor cleavage independently of RanGTP (wu2018theroleof pages 1-2, wang2020xpo5promotesprimary pages 1-2) |
| Exportin 1/5 family-level summary for PTHR11223 | Family belongs to the HEAT-repeat karyopherin-β superfamily: elongated α-helical solenoids with conformational flexibility suited for cargo recognition, Ran-coupled switching, and NPC transit; all members use transient FG-nucleoporin interactions during transport (wing2022karyopherinmediatednucleocytoplasmictransport pages 1-6, matsuura2016mechanisticinsightsfrom pages 1-2, yang2023nucleartransportproteins pages 1-2) | Shared karyopherin-β HEAT-repeat architecture and Ran-responsive transport cycle; diverged cargo-recognition modules underlie specialization of XPO1 for protein NES cargoes and XPO5 for structured RNA cargoes (matsuura2016mechanisticinsightsfrom pages 1-2, yang2023nucleartransportproteins pages 1-2, kalia2025analysisofexportins pages 1-2) | Conserved family principle is not catalysis but binding specificity: residues shaping cargo-binding surfaces and Ran interfaces are the critical functional determinants; family members differ strongly in the exact cargo-contact residues used by XPO1 versus XPO5 (matsuura2016mechanisticinsightsfrom pages 1-2, chen2025therapeutictargetingof pages 1-3) | Exportins generally bind cargo cooperatively with RanGTP in the nucleus; hydrolysis of RanGTP after RanBP1/RanGAP action in the cytoplasm provides directionality and promotes complex disassembly (matsuura2016mechanisticinsightsfrom pages 1-2, yang2023nucleartransportproteins pages 1-2) | Family exports diverse macromolecules from nucleus to cytoplasm. Within PTHR11223, XPO1 mediates broad protein/RNP export via leucine-rich NES recognition, whereas XPO5 specializes in structured RNA export and some ancillary RNA-processing roles; this divergence is central for GO review because no single cargo-specific molecular function fits every family member (wang2020xpo5promotesprimary pages 1-2, chen2025therapeutictargetingof pages 1-3, kalia2025analysisofexportins pages 1-2) |


*Table: This table summarizes the structural architecture, conserved motifs, key residues, RanGTP coupling, and cargo-recognition mechanisms relevant to the Exportin 1/5 family. It is useful for GO review because it makes clear both the shared exportin scaffold and the major functional divergence between XPO1-like and XPO5-like members.*

### Conserved Functional Mechanism

All exportins share a **Ran-dependent export cycle**: in the nucleus, binding of RanGTP promotes an "open" conformation that enables cooperative cargo recognition; the exportin-cargo-RanGTP ternary complex then translocates through nuclear pore complexes (NPCs) via transient interactions with FG-nucleoporins; in the cytoplasm, RanBP1/RanGAP promote GTP hydrolysis and complex disassembly, releasing cargo and regenerating free exportin for another cycle (matsuura2016mechanisticinsightsfrom pages 1-2, chen2025therapeutictargetingof pages 1-3, bruserud2025xpo1exportin1inacute pages 1-2). This RanGTP/GDP gradient provides thermodynamic directionality to nuclear export (matsuura2016mechanisticinsightsfrom pages 1-2).

### Subfamily-Specific Cargo Recognition Modules

While the HEAT-repeat scaffold and Ran-coupled cycle are conserved, **cargo-recognition surfaces diverge sharply** across subfamilies:

- **XPO1/CRM1**: HEAT repeats 11-12 form a hydrophobic NES-binding groove containing five pockets (P0-P4) that recognize leucine-rich nuclear export signals (NESs) in protein cargoes. Conserved residue **Lys568** (human numbering) acts as a specificity filter through backbone hydrogen bonding, discriminating functional NESs from non-NES peptides (fung2017nuclearexportreceptor pages 1-8, chen2025therapeutictargetingof pages 1-3). Crystal structures reveal that NES peptides can bind in multiple orientations (plus/minus) and conformations (extended, helical, loop-like), explaining the sequence degeneracy of NES consensus patterns (fung2017nuclearexportreceptor pages 1-8).

- **XPO5**: Recognizes structured RNA stem-loops (e.g., pre-miRNA hairpins) through shape-dependent binding to dsRNA features and the characteristic 2-nucleotide 3' overhang, rather than peptide motifs. HEAT-repeat residues form hydrogen bonds to RNA ends (wang2020xpo5promotesprimary pages 1-2). Interestingly, XPO5 can bind some RNAs in a **RanGTP-independent** manner for non-export functions such as promoting pri-miRNA processing by the Microprocessor (wang2020xpo5promotesprimary pages 1-2).

- **XPOT/Exportin-t**: Dedicated tRNA exporter that specifically recognizes the processed **CCA-tail** of mature tRNAs, distinguishing processed from unprocessed tRNA precursors (hardenberg2026xpotdeficiencycauses pages 1-5, li2024exportin5bindingprecedes pages 1-2).

---

## 2. InterPro2GO Mapping Appropriateness

**Current status**: No GO terms are mapped to PTHR11223.

> Family-level GO that is safest for PTHR11223 (EXPORTIN 1/5) is limited to broad exportin/karyopherin biology that is plausibly universal across the matched proteins: **Ran GTPase binding**, **nuclear export receptor activity / Ran-dependent nuclear export receptor activity**, and related very high-level nucleocytoplasmic transport terms, because all exportins share the HEAT-repeat karyopherin-β scaffold and Ran-coupled export cycle even though their cargo classes differ sharply (matsuura2016mechanisticinsightsfrom pages 1-2, yang2023nucleartransportproteins pages 1-2, wing2022karyopherinmediatednucleocytoplasmictransport pages 1-6).
>
> Terms that should **NOT** be applied at the family level are cargo-specific or lineage-specific functions, including **protein export / NES-dependent protein export** (true for XPO1 but not XPO5-like members), **pre-miRNA export from nucleus** or **miRNA biogenesis** (true for XPO5, not XPO1-like members), and **tRNA export from nucleus** (canonical for XPOT and secondarily adopted by Drosophila XPO5, but not universal for the family). Likewise, cargo-level process terms such as ribosomal export, actin export, or importin-α export belong to other exportin subfamilies and demonstrate why this family is functionally heterogeneous (wang2020xpo5promotesprimary pages 1-2, kalia2025analysisofexportins pages 1-2, li2024exportin5bindingprecedes pages 1-2, dhungel2026adeeplearningatlas pages 1-4).
>
> Recommended GO action pattern for genes matching this family: **ACCEPT** only highly general exportin-level molecular functions if InterPro intends to annotate a broad family; **MODIFY-to-specific** by moving protein-export terms to XPO1-specific children and RNA-hairpin/pre-miRNA export terms to XPO5-specific children; **REMOVE / avoid adding** any cargo-specific biological process or component terms at the parent family level, because they would systematically over-annotate divergent subfamilies (chen2025therapeutictargetingof pages 1-3, li2024exportin5bindingprecedes pages 1-2, dhungel2026adeeplearningatlas pages 1-4).
>
> Taxonomic caveats are substantial: exportins are broadly conserved across eukaryotes, but individual members are gained, lost, or repurposed by lineage. Drosophila lacks XPOT and uses XPO5 for major tRNA-related export roles, whereas plants lack some other exportins such as XPO6; therefore even apparently reasonable process terms can leak across clades if attached at an overly broad family node. The current state of **no InterPro2GO mappings** for this parent family is therefore defensible and likely preferable to broad cargo-specific mappings (hardenberg2026xpotdeficiencycauses pages 1-5, li2024exportin5bindingprecedes pages 1-2, wing2022karyopherinmediatednucleocytoplasmictransport pages 1-6, jin2022identificationofthe pages 1-2).
>
> Overall verdict: **KEEP parent family minimally annotated or unmapped; annotate at child/subfamily level instead.** For PTHR11223 specifically, the evidence supports a **MODIFY-to-specific / KEEP_UNMAPPED_AT_PARENT** strategy rather than adding XPO1- or XPO5-specific GO terms to all matches (wang2020xpo5promotesprimary pages 1-2, dhungel2026adeeplearningatlas pages 1-4, wing2022karyopherinmediatednucleocytoplasmictransport pages 1-6).


*Blockquote: This blockquote summarizes which GO terms are safe or unsafe for the broad EXPORTIN 1/5 family. It is useful for deciding whether annotation should remain absent at the parent level or be moved to more specific child entries.*

### Why Cargo-Specific Terms Would Over-Annotate

Terms such as **"protein export from nucleus"** (true for XPO1-like members), **"pre-miRNA export from nucleus"** or **"miRNA biogenesis"** (true for XPO5-like members), and **"tRNA export from nucleus"** (canonical for XPOT, secondarily adopted in Drosophila XPO5) are **subfamily-specific** and would systematically over-annotate proteins from divergent subfamilies if applied at the parent family level (wang2020xpo5promotesprimary pages 1-2, kalia2025analysisofexportins pages 1-2, li2024exportin5bindingprecedes pages 1-2, dhungel2026adeeplearningatlas pages 1-4).

### Safe Family-Level Terms

Only highly general terms are appropriate:
- **Ran GTPase binding** (GO:0008536) — universally required for the export cycle (matsuura2016mechanisticinsightsfrom pages 1-2, yang2023nucleartransportproteins pages 1-2).
- **Ran-dependent nuclear export receptor activity** or **nuclear export signal receptor activity** (generic, not cargo-class-specific) (matsuura2016mechanisticinsightsfrom pages 1-2, wing2022karyopherinmediatednucleocytoplasmictransport pages 1-6).

Even these should be applied cautiously, as the family encompasses biportins (XPO4, XPO7) with bidirectional transport behavior that complicates simple "export" annotations (kalia2025analysisofexportins pages 1-2, dhungel2026adeeplearningatlas pages 1-4).

---

## 3. Functional Divergence Across the Family

| Exportin family member | Major cargo types | Cargo recognition mechanism | Key distinguishing features | Distribution across species |
|---|---|---|---|---|
| XPO1 / CRM1 | Hundreds of NES-bearing proteins; some RNP/RNA cargos via adaptors; major protein export receptor | Recognizes leucine-rich nuclear export signals (NESs) in a hydrophobic groove formed mainly by HEAT repeats 11-12; cargo binding is cooperative with RanGTP; interacts with FG-nucleoporins during NPC transit (fung2017nuclearexportreceptor pages 1-8, matsuura2016mechanisticinsightsfrom pages 1-2, chen2025therapeutictargetingof pages 1-3, dhungel2026adeeplearningatlas pages 1-4) | Broadest known protein export specificity; dominant mediator of protein nuclear export in mammalian cells; structurally flexible NES recognition including plus/minus orientations and multiple NES conformations (fung2017nuclearexportreceptor pages 1-8, chen2025therapeutictargetingof pages 1-3, dhungel2026adeeplearningatlas pages 1-4) | Deeply conserved across eukaryotes; represented from yeast to animals and plants as part of the conserved karyopherin/exportin system (wing2022karyopherinmediatednucleocytoplasmictransport pages 1-6, matsuura2016mechanisticinsightsfrom pages 1-2, yang2023nucleartransportproteins pages 1-2) |
| XPO5 / Exportin-5 | Pre-miRNA hairpins; other structured RNAs including minihelix RNAs and, in some taxa, tRNA-related substrates | Shape/structure-based recognition of dsRNA stem-loops with short 3' overhangs; canonical export is RanGTP-dependent, but some pri-miRNA and structured RNA binding can be RanGTP-independent (wang2020xpo5promotesprimary pages 1-2, li2024exportin5bindingprecedes pages 1-2) | RNA-specialized exportin; also promotes pri-miRNA processing in addition to export; in Drosophila, expands into strong tRNA-related roles because canonical Exportin-t is absent (wang2020xpo5promotesprimary pages 1-2, li2024exportin5bindingprecedes pages 1-2) | Broad eukaryotic distribution, but functional scope varies by lineage; especially notable neo-functional expansion in Drosophila (wing2022karyopherinmediatednucleocytoplasmictransport pages 1-6, li2024exportin5bindingprecedes pages 1-2) |
| XPOT / Exportin-t | Mature tRNAs | Recognizes mature tRNA features, including the processed CCA-tail; RanGTP-dependent export receptor for tRNA nuclear export (hardenberg2026xpotdeficiencycauses pages 1-5, li2024exportin5bindingprecedes pages 1-2, dhungel2026adeeplearningatlas pages 1-4) | Canonical dedicated tRNA exporter in many animals and other eukaryotes; functionally distinct from XPO5 despite some overlap in certain organisms (hardenberg2026xpotdeficiencycauses pages 1-5, li2024exportin5bindingprecedes pages 1-2, dhungel2026adeeplearningatlas pages 1-4) | Present in many eukaryotes including vertebrates, but absent from Drosophila, where XPO5 appears to compensate; not universally required in simpler organisms (hardenberg2026xpotdeficiencycauses pages 1-5, li2024exportin5bindingprecedes pages 1-2) |
| XPO2 / CSE1L | Importin-α (recycling/export of import adaptor) | Specialized recognition of importin-α export complexes in the Ran system rather than broad RNA or NES-cargo export (kalia2025analysisofexportins pages 1-2, dhungel2026adeeplearningatlas pages 1-4) | Functionally narrow and mechanistically distinct from XPO1 and XPO5; primarily maintains import cycle homeostasis by recycling importin-α (kalia2025analysisofexportins pages 1-2, dhungel2026adeeplearningatlas pages 1-4) | Present across eukaryotes as a conserved exportin family member, though not the universal dominant protein export receptor (wing2022karyopherinmediatednucleocytoplasmictransport pages 1-6, dhungel2026adeeplearningatlas pages 1-4) |
| XPO4 | eIF5A, Smad3; can also mediate import of Sox2/SRY in some contexts | Cargo-specific recognition with bidirectional transport behavior depending on cargo/context (kalia2025analysisofexportins pages 1-2, dhungel2026adeeplearningatlas pages 1-4) | Biportin-like behavior (export and import); demonstrates that some exportins are not purely exporters, complicating family-level GO assignments (kalia2025analysisofexportins pages 1-2, dhungel2026adeeplearningatlas pages 1-4) | Present in many metazoans; absent in some lineages such as Drosophila according to comparative karyopherin surveys (wing2022karyopherinmediatednucleocytoplasmictransport pages 1-6, dhungel2026adeeplearningatlas pages 1-4) |
| XPO6 | Profilin-actin complexes | Specialized cargo recognition for actin-family related complexes rather than NES peptides or structured RNAs (kalia2025analysisofexportins pages 1-2, dhungel2026adeeplearningatlas pages 1-4) | Narrow cargo spectrum; distinct from XPO1 and XPO5 in both substrate class and cellular role (kalia2025analysisofexportins pages 1-2, dhungel2026adeeplearningatlas pages 1-4) | Present in mammals and many eukaryotes, but absent from plants and some other lineages in comparative surveys (wing2022karyopherinmediatednucleocytoplasmictransport pages 1-6, dhungel2026adeeplearningatlas pages 1-4) |
| XPO7 | Broad but context-dependent protein cargo set | Less canonical and more context-dependent cargo selectivity than XPO1; can function in bidirectional transport behavior in some analyses (kalia2025analysisofexportins pages 1-2, dhungel2026adeeplearningatlas pages 1-4) | Functionally heterogeneous and not reducible to a single simple cargo rule; another example that exportin family members are not annotation-equivalent (kalia2025analysisofexportins pages 1-2, dhungel2026adeeplearningatlas pages 1-4) | Conserved in many metazoans; family surveys note paralogy/relatedness with RANBP17 and lineage-specific variation (wing2022karyopherinmediatednucleocytoplasmictransport pages 1-6, dhungel2026adeeplearningatlas pages 1-4) |
| Family-level implication for PTHR11223 | Mixed: NES-bearing proteins for XPO1-like members, structured RNAs for XPO5-like members, and lineage-specific tRNA roles in some taxa | Shared Ran-dependent karyopherin-β export cycle, but cargo-recognition modules are highly divergent across members (matsuura2016mechanisticinsightsfrom pages 1-2, yang2023nucleartransportproteins pages 1-2, dhungel2026adeeplearningatlas pages 1-4) | Strong functional heterogeneity means cargo-specific GO terms such as "protein export" or "pre-miRNA export" are not safe at broad family level unless restricted to the correct child/subfamily (wang2020xpo5promotesprimary pages 1-2, kalia2025analysisofexportins pages 1-2, li2024exportin5bindingprecedes pages 1-2, dhungel2026adeeplearningatlas pages 1-4) | Exportins are broadly eukaryotic, but individual members are gained/lost and can undergo lineage-specific specialization, so taxon-aware annotation review is essential (wing2022karyopherinmediatednucleocytoplasmictransport pages 1-6, hardenberg2026xpotdeficiencycauses pages 1-5, li2024exportin5bindingprecedes pages 1-2, dhungel2026adeeplearningatlas pages 1-4) |


*Table: This table compares major exportin family members by cargo class, recognition mode, and phylogenetic distribution. It is useful for GO review because it makes clear that exportins share a transport scaffold but differ sharply in substrate specificity and lineage-dependent biology.*

### Major Subfamilies and Their Cargo Classes

The PTHR11223 family exhibits profound **functional heterogeneity**:

- **XPO1/CRM1 subfamily**: Dominant mediator of protein nuclear export in metazoans, recognizing hundreds of leucine-rich NES-bearing cargoes including tumor suppressors, transcription factors, and cell-cycle regulators. XPO1 also exports some RNP/RNA cargoes indirectly via adaptor proteins (chen2025therapeutictargetingof pages 1-3, bruserud2025xpo1exportin1inacute pages 1-2, dhungel2026adeeplearningatlas pages 1-4).

- **XPO5 subfamily**: RNA-specialized exportin primarily exporting pre-miRNA hairpins and other structured RNAs. In Drosophila, XPO5 has undergone **neo-functionalization** to assume major tRNA-related export roles normally mediated by XPOT in other lineages (wang2020xpo5promotesprimary pages 1-2, li2024exportin5bindingprecedes pages 1-2). Recent findings show XPO5 also promotes pri-miRNA processing independently of its canonical RanGTP-dependent export function, revealing non-export roles (wang2020xpo5promotesprimary pages 1-2).

- **XPOT/Exportin-t subfamily**: Canonical dedicated tRNA exporter recognizing mature tRNA CCA-tails. **Absent from Drosophila**, where XPO5 compensates (hardenberg2026xpotdeficiencycauses pages 1-5, li2024exportin5bindingprecedes pages 1-2).

- **XPO2/CSE1L subfamily**: Specialized for recycling importin-α, not general cargo export (kalia2025analysisofexportins pages 1-2, dhungel2026adeeplearningatlas pages 1-4).

- **XPO4, XPO6, XPO7 subfamilies**: Narrow or context-dependent cargo specificities (e.g., XPO4 exports eIF5A and Smad3 but can also import Sox2/SRY; XPO6 exports profilin-actin; XPO7 has broad but context-dependent roles). XPO4 and XPO7 exhibit **biportin behavior** (kalia2025analysisofexportins pages 1-2, dhungel2026adeeplearningatlas pages 1-4).

### No Catalytically Dead Members Identified

Unlike enzyme families, exportins are **binding proteins**, not catalytic. Their function depends on binding specificity for cargo and Ran, not enzymatic activity. Therefore, there are no "pseudo-exportin" or catalytically inactive members within this family — functional diversification occurs through divergence in cargo-binding surfaces, not loss of catalytic residues (matsuura2016mechanisticinsightsfrom pages 1-2, chen2025therapeutictargetingof pages 1-3).

---

## 4. Taxonomic Scope

### Broad Eukaryotic Conservation with Lineage-Specific Variation

Exportins are conserved across **all eukaryotic lineages**, including animals, fungi, plants, and even early-diverging trypanosomes, reflecting their ancient origin in the last eukaryotic common ancestor (wing2022karyopherinmediatednucleocytoplasmictransport pages 1-6, yang2023nucleartransportproteins pages 1-2). The **number of exportin genes varies by organism**: S. cerevisiae has ~14 karyopherins, whereas humans have ~20 (wing2022karyopherinmediatednucleocytoplasmictransport pages 1-6).

### Lineage-Specific Gains, Losses, and Repurposing

- **Drosophila** lacks XPOT, XPO4, RANBP6, and RANBP17 homologs but has expanded XPO5 functionality to compensate for XPOT absence in tRNA export. Drosophila also has multiple TNPO3 and IPO4 paralogs (wing2022karyopherinmediatednucleocytoplasmictransport pages 1-6, li2024exportin5bindingprecedes pages 1-2).

- **Plants** lack XPO6 but possess multiple IMP, TNPO3, and IPO5 homologs; land plants evolved a novel PLANTKAP distantly related to IPO8 (wing2022karyopherinmediatednucleocytoplasmictransport pages 1-6, jin2022identificationofthe pages 1-2).

- **Trypanosomes**, despite early eukaryotic divergence, retain significant karyopherin homology but lack TNPO3, XPO6, and IPO13 (wing2022karyopherinmediatednucleocytoplasmictransport pages 1-6).

### Implications for GO Annotation

This lineage-specific variation means that **cargo-specific GO terms can "leak" across clades** where the pathway or cargo class differs. For example, annotating "pre-miRNA export" at the family level would incorrectly propagate to yeast and plant orthologs where miRNA biogenesis pathways may be absent or divergent. Similarly, "tRNA export" terms applied broadly would be misleading in Drosophila, where the canonical XPOT route is absent (hardenberg2026xpotdeficiencycauses pages 1-5, li2024exportin5bindingprecedes pages 1-2, wing2022karyopherinmediatednucleocytoplasmictransport pages 1-6, jin2022identificationofthe pages 1-2).

---

## 5. Over-Annotation Verdict and Recommendations

### Summary Assessment

InterPro entry PTHR11223 is a **functionally heterogeneous family** encompassing exportins with sharply divergent cargo specificities. Applying cargo-specific GO terms (e.g., "protein export," "pre-miRNA export," "tRNA export") at the parent family level would result in **systematic over-annotation** of subfamily members that do not perform those functions (wang2020xpo5promotesprimary pages 1-2, chen2025therapeutictargetingof pages 1-3, kalia2025analysisofexportins pages 1-2, li2024exportin5bindingprecedes pages 1-2, dhungel2026adeeplearningatlas pages 1-4).

### Recommended GO Action Pattern

**KEEP_UNMAPPED_AT_PARENT / MODIFY-to-specific**

- **Current state (no mappings)**: The absence of InterPro2GO terms for PTHR11223 is **defensible and appropriate** given the functional divergence within the family (wing2022karyopherinmediatednucleocytoplasmictransport pages 1-6).

- **If annotation is desired**: Apply only **highly general terms** such as:
  - Ran GTPase binding (GO:0008536)
  - Ran-dependent nuclear export receptor activity (generic, not cargo-class-specific)
  - Nucleocytoplasmic transport (very high-level process term)

- **Do NOT apply** at the parent family level:
  - Protein export from nucleus (XPO1-specific)
  - Pre-miRNA export / miRNA biogenesis (XPO5-specific)
  - tRNA export from nucleus (XPOT/XPO5 context-specific)
  - Any cargo-class-specific biological process or cellular component terms

- **Recommended strategy**: Move cargo-specific annotations to **child entries** or **subfamily-level signatures** (e.g., create or use specific InterPro entries for XPO1-like vs. XPO5-like vs. XPOT-like subfamilies) rather than annotating the broad parent family (dhungel2026adeeplearningatlas pages 1-4, wing2022karyopherinmediatednucleocytoplasmictransport pages 1-6).

### Experimental vs. Inferred Evidence

The structural and biochemical mechanisms described here are based on **extensive experimental evidence** including:
- X-ray crystal structures of exportin-cargo-RanGTP complexes (fung2017nuclearexportreceptor pages 1-8, matsuura2016mechanisticinsightsfrom pages 1-2)
- Biochemical binding assays and mutagenesis studies identifying key residues (fung2017nuclearexportreceptor pages 1-8, chen2025therapeutictargetingof pages 1-3)
- CLIP-seq and functional studies mapping cargo repertoires (wang2020xpo5promotesprimary pages 1-2, li2024exportin5bindingprecedes pages 1-2, dhungel2026adeeplearningatlas pages 1-4)
- Genetic knockout/knockdown studies in multiple organisms (wang2020xpo5promotesprimary pages 1-2, hardenberg2026xpotdeficiencycauses pages 1-5)

Functional divergence is inferred from **phylogenetic analysis, comparative genomics, and lineage-specific experimental studies** showing distinct cargo classes and neo-functionalization events (e.g., Drosophila XPO5 compensating for XPOT absence) (li2024exportin5bindingprecedes pages 1-2, wing2022karyopherinmediatednucleocytoplasmictransport pages 1-6, jin2022identificationofthe pages 1-2).

---

## Conclusion

PTHR11223 (EXPORTIN 1/5) is a structurally conserved but functionally divergent protein family. The shared karyopherin-β HEAT-repeat scaffold and Ran-coupled export mechanism support only very general GO annotations. The profound cargo-specificity divergence (proteins for XPO1, structured RNAs for XPO5, tRNAs for XPOT, specialized cargoes for others) means that **subfamily-level annotation is essential** to avoid systematic over-annotation. The current absence of InterPro2GO mappings is appropriate and should be maintained unless/until subfamily-specific child entries are created for annotation.

**Final Recommendation**: **KEEP parent family unmapped; annotate at subfamily/child level instead.**

References

1. (wing2022karyopherinmediatednucleocytoplasmictransport pages 1-6): Casey E. Wing, Ho Yee Joyce Fung, and Yuh Min Chook. Karyopherin-mediated nucleocytoplasmic transport. Nature Reviews Molecular Cell Biology, 23:307-328, Jan 2022. URL: https://doi.org/10.1038/s41580-021-00446-7, doi:10.1038/s41580-021-00446-7. This article has 316 citations and is from a domain leading peer-reviewed journal.

2. (matsuura2016mechanisticinsightsfrom pages 1-2): Yoshiyuki Matsuura. Mechanistic insights from structural analyses of ran-gtpase-driven nuclear export of proteins and rnas. Journal of molecular biology, 428 10 Pt A:2025-39, May 2016. URL: https://doi.org/10.1016/j.jmb.2015.09.025, doi:10.1016/j.jmb.2015.09.025. This article has 79 citations and is from a domain leading peer-reviewed journal.

3. (yang2023nucleartransportproteins pages 1-2): Yang Yang, Lu Guo, Lin Chen, Bo Gong, Da Jia, and Qingxiang Sun. Nuclear transport proteins: structure, function and disease relevance. Signal Transduction and Targeted Therapy, Nov 2023. URL: https://doi.org/10.1038/s41392-023-01649-4, doi:10.1038/s41392-023-01649-4. This article has 190 citations and is from a peer-reviewed journal.

4. (chen2025therapeutictargetingof pages 1-3): Yi Fan Chen and Drew J. Adams. Therapeutic targeting of exportin-1 beyond nuclear export. Trends in Pharmacological Sciences, 46:20-31, Jan 2025. URL: https://doi.org/10.1016/j.tips.2024.11.002, doi:10.1016/j.tips.2024.11.002. This article has 13 citations and is from a highest quality peer-reviewed journal.

5. (fung2017nuclearexportreceptor pages 1-8): Ho Yee Joyce Fung, Szu-Chin Fu, and Yuh Min Chook. Nuclear export receptor crm1 recognizes diverse conformations in nuclear export signals. eLife, Mar 2017. URL: https://doi.org/10.7554/elife.23961, doi:10.7554/elife.23961. This article has 120 citations and is from a domain leading peer-reviewed journal.

6. (bruserud2025xpo1exportin1inacute pages 1-2): Øystein Bruserud, Frode Selheim, Maria Hernandez-Valladares, and Håkon Reikvam. Xpo1/exportin-1 in acute myelogenous leukemia; biology and therapeutic targeting. Biomolecules, 15:175, Jan 2025. URL: https://doi.org/10.3390/biom15020175, doi:10.3390/biom15020175. This article has 2 citations.

7. (wang2020xpo5promotesprimary pages 1-2): Jingjing Wang, Jerome E. Lee, Kent Riemondy, Yang Yu, Steven M. Marquez, Eric C. Lai, and Rui Yi. Xpo5 promotes primary mirna processing independently of rangtp. Nature Communications, Apr 2020. URL: https://doi.org/10.1038/s41467-020-15598-x, doi:10.1038/s41467-020-15598-x. This article has 55 citations and is from a highest quality peer-reviewed journal.

8. (kalia2025analysisofexportins pages 1-2): Punita Kalia, Rohini Ravindran Nair, and Suresh Singh Yadav. Analysis of exportins expression unveils their prognostic significance in colon adenocarcinoma: insights from public databases. Discover Oncology, Jan 2025. URL: https://doi.org/10.1007/s12672-025-01748-4, doi:10.1007/s12672-025-01748-4. This article has 1 citations.

9. (wu2018theroleof pages 1-2): Ke Wu, Juan He, Wenchen Pu, and Yong Peng. The role of exportin-5 in microrna biogenesis and cancer. Genomics, Proteomics & Bioinformatics, 16:120-126, Apr 2018. URL: https://doi.org/10.1016/j.gpb.2017.09.004, doi:10.1016/j.gpb.2017.09.004. This article has 208 citations and is from a peer-reviewed journal.

10. (hardenberg2026xpotdeficiencycauses pages 1-5): S. von Hardenberg, I. Niehaus, A. Wiemers, T. Rothoeft, K. Huang, C. Petree, V. Schäffer, C. Phillipe, A-L. Bruel, K. Warnatz, M. Zamani, R. Ahmadi, A. Sedaghat, S. Bahram, S. Sedighzadeh, S. Ebrahimi, S. Khalilian, S. Landwehr-Kenzel, N. Schwerk, A. Elsayed, J. Rösler, S-J. Lin, S. Sabu, N. Strenzke, G. Sogkas, B. Vona, G. K. Varshney, N. Di Donato, and B. Auber. <i>xpot</i> deficiency causes a human disorder through impaired trna nuclear export. Unknown journal, Feb 2026. URL: https://doi.org/10.64898/2026.01.28.26344748, doi:10.64898/2026.01.28.26344748.

11. (li2024exportin5bindingprecedes pages 1-2): Ze Li, Junko Iida, Masami Shiimori, and Katsutomo Okamura. Exportin-5 binding precedes 5′- and 3′-end processing of trna precursors in drosophila. Sep 2024. URL: https://doi.org/10.1016/j.jbc.2024.107632, doi:10.1016/j.jbc.2024.107632. This article has 1 citations and is from a domain leading peer-reviewed journal.

12. (dhungel2026adeeplearningatlas pages 1-4): Sajina Dhungel, Sihara de Zoysa, DeAnna Burns, Linden McGregor, RP Rajesh, Ridila Alam, Diya Arain, Vivaan Bhaskar, Jayden Jeong, Aarush Kikani, Eashan Kolli, Zain Mardini, Aanya Parasramka, Eden Potterton, Saachi Thomas, and Chintan K. Kikani. A deep-learning atlas of xpo1-mediated nuclear export at proteome scale. bioRxiv, Mar 2026. URL: https://doi.org/10.64898/2026.03.25.713363, doi:10.64898/2026.03.25.713363. This article has 0 citations.

13. (jin2022identificationofthe pages 1-2): Lu Jin, Guobin Zhang, Guichuan Yang, and Jiaqiang Dong. Identification of the karyopherin superfamily in maize and its functional cues in plant development. International Journal of Molecular Sciences, 23:14103, Nov 2022. URL: https://doi.org/10.3390/ijms232214103, doi:10.3390/ijms232214103. This article has 6 citations.

## Artifacts

- [Edison artifact artifact-00](PTHR11223-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR11223-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](PTHR11223-deep-research-falcon_artifacts/artifact-02.md)

## Citations

1. matsuura2016mechanisticinsightsfrom pages 1-2
2. fung2017nuclearexportreceptor pages 1-8
3. wing2022karyopherinmediatednucleocytoplasmictransport pages 1-6
4. yang2023nucleartransportproteins pages 1-2
5. chen2025therapeutictargetingof pages 1-3
6. kalia2025analysisofexportins pages 1-2
7. wu2018theroleof pages 1-2
8. hardenberg2026xpotdeficiencycauses pages 1-5
9. dhungel2026adeeplearningatlas pages 1-4
10. jin2022identificationofthe pages 1-2
11. https://doi.org/10.1038/s41580-021-00446-7,
12. https://doi.org/10.1016/j.jmb.2015.09.025,
13. https://doi.org/10.1038/s41392-023-01649-4,
14. https://doi.org/10.1016/j.tips.2024.11.002,
15. https://doi.org/10.7554/elife.23961,
16. https://doi.org/10.3390/biom15020175,
17. https://doi.org/10.1038/s41467-020-15598-x,
18. https://doi.org/10.1007/s12672-025-01748-4,
19. https://doi.org/10.1016/j.gpb.2017.09.004,
20. https://doi.org/10.64898/2026.01.28.26344748,
21. https://doi.org/10.1016/j.jbc.2024.107632,
22. https://doi.org/10.64898/2026.03.25.713363,
23. https://doi.org/10.3390/ijms232214103,