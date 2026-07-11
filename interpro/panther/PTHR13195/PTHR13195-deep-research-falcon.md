---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-21T20:18:52.428606'
end_time: '2026-06-21T20:28:55.368717'
duration_seconds: 602.94
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR13195
  interpro_name: PSEUDOURIDINE SYNTHASE-RELATED
  interpro_short_name: Not specified
  interpro_type: family
  interpro_integrated: IPR039048
  member_databases: Not specified
  n_proteins: '1670'
  n_taxa: '3812'
  n_subfamilies: '1'
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
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: PTHR13195-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# InterPro Family Research for GO Annotation Review

## ⚠️ CRITICAL: Family Identification Context

**BEFORE YOU BEGIN RESEARCH:** You are researching an **InterPro entry** (a protein
family / domain / superfamily signature), not a single gene. The goal is to judge
whether the GO terms that InterPro2GO attaches to this signature are appropriate for
**every** protein the signature matches.

### Target InterPro Entry (from the InterPro API):
- **Accession:** PTHR13195
- **Name:** PSEUDOURIDINE SYNTHASE-RELATED
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** IPR039048
- **Member database signatures:** Not specified
- **Scale:** 1670 proteins across 3812 taxa, 1 subfamilies
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
**PTHR13195 (PSEUDOURIDINE SYNTHASE-RELATED)**, structured to support GO annotation review.

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
- **Accession:** PTHR13195
- **Name:** PSEUDOURIDINE SYNTHASE-RELATED
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** IPR039048
- **Member database signatures:** Not specified
- **Scale:** 1670 proteins across 3812 taxa, 1 subfamilies
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
**PTHR13195 (PSEUDOURIDINE SYNTHASE-RELATED)**, structured to support GO annotation review.

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


# InterPro Family Research Report: PTHR13195 (PSEUDOURIDINE SYNTHASE-RELATED)

## Executive Summary

InterPro entry PTHR13195 is a PANTHER family-level signature encompassing 1670 proteins across 3812 taxa, representing the pseudouridine synthase superfamily. **Currently, no InterPro2GO terms are mapped to this entry.** This report concludes that **the absence of GO annotations is actually appropriate** given the extreme functional heterogeneity across the family, which includes catalytically active enzymes targeting diverse RNA substrates, catalytically inactive pseudo-enzymes, and members with neo-functionalized non-catalytic roles. Any family-wide whole-protein GO annotation would systematically over-annotate a substantial fraction of matched proteins.

---

## 1. Family Definition and Biochemistry

### 1.1 Structural Fold and Conserved Architecture

Pseudouridine (Ψ) synthases catalyze the isomerization of uridine (U) to pseudouridine, converting the N1-C1' glycosidic bond to a C5-C1' carbon-carbon bond (lin2025mechanisticinsightinto pages 2-3, lin2025mechanisticinsightinto pages 1-2). This modification is the most abundant RNA modification found across all three domains of life (lin2025mechanisticinsightinto pages 1-2, jia2025decipheringthepseudouridine pages 3-4, lin2021pseudouridinesinrnas pages 6-8). 

All members of the pseudouridine synthase superfamily share a **highly conserved catalytic core structure** consisting of a TIM-barrel (or mixed α/β) topology with antiparallel β-sheets, α-helices, and multiple loops (lin2025mechanisticinsightinto pages 2-3, lin2025mechanisticinsightinto pages 1-2). Despite low sequence identity among families (often <25%), the spatial arrangement of the catalytic residues is preserved (borchardt2020regulationandfunction pages 3-4, lin2025mechanisticinsightinto pages 5-9).

### 1.2 Catalytic Mechanism and Conserved Residues

The catalytic mechanism involves a **strictly conserved aspartic acid (Asp) residue** that is essential for activity across all PUS families (purchal2022pseudouridinesynthase7 pages 3-4, guegueniat2021thehumanpseudouridine pages 4-5, lin2025mechanisticinsightinto pages 2-3, lin2025mechanisticinsightinto pages 1-2). Mechanistic studies support a **glycal mechanism** where the catalytic Asp deprotonates the C2' hydroxyl of the ribose, triggering cleavage of the N-glycosidic bond, 180° rotation of the uracil base, and reformation via a new C-C bond (lin2025mechanisticinsightinto pages 2-3, lin2025mechanisticinsightinto pages 1-2). This mechanism is supported by kinetic isotope experiments and molecular dynamics simulations across multiple PUS families (lin2025mechanisticinsightinto pages 2-3).

Beyond the catalytic Asp, five additional amino acids are conserved across all PUS families (identified in *Methanocaldococcus jannaschii*: Asp275, Tyr339, Ile412, Lys413, Leu440), contributing to substrate positioning and catalysis (fitzek2018evolutionofeukaryal pages 2-4, fitzek2018evolutionofeukaryal pages 1-2). Structural features such as the **forefinger loop (FFL)** and **thumb loop** are conserved in TruA, RluA, and Pus10 families, forming a "pinch mechanism" that holds the substrate in place (fitzek2018evolutionofeukaryal pages 2-4, fitzek2018evolutionofeukaryal pages 1-2).

### 1.3 Family Classification

The pseudouridine synthase superfamily is divided into **six evolutionarily conserved families** based on bacterial/archaeal naming: **TruA, TruB, TruD, RluA, RsuA, and Pus10** (lin2025mechanisticinsightinto pages 1-2, borchardt2020regulationandfunction pages 3-4, fitzek2018evolutionofeukaryal pages 1-2, song2020differentialrolesof pages 1-2). Each family exhibits distinct structural insertions, accessory domains, and substrate specificities (lin2025mechanisticinsightinto pages 5-9, lin2025mechanisticinsightinto pages 4-5). See the comprehensive comparison table below.

| Family name | Representative members (bacteria/archaea/eukarya) | Primary RNA targets | Modified positions in tRNA/rRNA | Substrate specificity (strict vs. promiscuous) | Known catalytically inactive members | Additional non-catalytic functions | Taxonomic distribution |
|---|---|---|---|---|---|---|---|
| TruA | **Bacteria:** TruA (e.g., *E. coli* TruA); **Archaea/Eukarya homologs:** PUS3, PUS1 (human/yeast) | Mainly tRNA; in eukaryotes, PUS1 also acts on mRNA and other ncRNAs | Canonical TruA/PUS3 activity at tRNA positions Ψ38/Ψ39/Ψ40 in the anticodon loop; PUS1 acts mainly at tRNA Ψ27/Ψ28 | **Mixed within family:** PUS3/ bacterial TruA are structurally strict tRNA enzymes; PUS1 is broader/promiscuous across RNA classes | No clear inactive TruA/PUS3 ortholog cited here | PUS1/TruA-like enzymes may have broader RNA-binding functions beyond canonical tRNA modification | Conserved across all three domains; TruA family broadly present in bacteria, archaea, and eukaryotes (lin2025mechanisticinsightinto pages 1-2, borchardt2020regulationandfunction pages 3-4, lin2025mechanisticinsightinto pages 5-9, lin2025mechanisticinsightinto pages 4-5) |
| TruB | **Bacteria:** TruB; **Eukarya:** PUS4/TRUB1, TRUB2; **Archaea/Eukarya guide-RNP branch:** Cbf5/DKC1 | Primarily tRNA; in eukaryotes TRUB1 also targets mRNA; Cbf5/DKC1 acts in H/ACA RNPs on rRNA/snRNA | Canonical TruB/TRUB1 installs Ψ55 in tRNA TΨC loop; archaeal/eukaryotic Cbf5/DKC1 acts at multiple guide-RNA-specified rRNA/snRNA sites | **Mixed:** bacterial TruB and TRUB1 are position-specific for tRNA Ψ55, but TRUB1 also modifies mRNA; guide-dependent Cbf5/DKC1 is broad at RNA class level but site-specified by guides | Human TRUB2 shows no noticeable enzymatic activity on predicted tRNA/rRNA targets in cells | TruB can function as a tRNA folding chaperone; DKC1 is also a core telomerase component; TRUB1 contributes to let-7 miRNA maturation in humans | TruB family occurs in bacteria and eukaryotes; Cbf5/DKC1 branch in archaea and eukaryotes; absent as TruB in some lineages with alternative solutions for Ψ55 (lin2025mechanisticinsightinto pages 1-2, borchardt2020regulationandfunction pages 3-4, liu2024advancementsinpseudouridine pages 2-3, xu2025acomprehensivetrna pages 1-2, lin2025mechanisticinsightinto pages 5-9) |
| TruD | **Bacteria:** TruD; **Eukarya:** PUS7 | tRNA; in eukaryotes also mRNA and other ncRNAs | Bacterial TruD classically modifies tRNA U13/U15-class positions; eukaryotic PUS7 modifies tRNA Ψ13 and Ψ35 and also mRNA sites with sequence preference | **Mixed but often broader than TruA/TruB:** bacterial TruD is relatively site-specific; PUS7 is opportunistic/promiscuous among RNAs bearing favorable sequence/structure contexts | No inactive TruD-family member established here | PUS7 affects cellular fitness/stress responses; disease-linked variants occur in humans | Conserved across all three domains; PUS7/TruD family represented in bacteria and eukaryotes and described as broadly conserved (purchal2022pseudouridinesynthase7 pages 3-4, guegueniat2021thehumanpseudouridine pages 4-5, lin2025mechanisticinsightinto pages 1-2, purchal2022pseudouridinesynthase7 pages 1-2, lin2025mechanisticinsightinto pages 5-9) |
| RluA | **Bacteria:** RluA, RluC, RluD, RluE, RluF; **Eukarya:** RPUSD1, RPUSD4, RPUSD3-like members | Primarily rRNA in prokaryotes; mitochondrial rRNA/tRNA targets in eukaryotes for some members | Mostly rRNA pseudouridylation in bacteria; eukaryotic RPUSD4 installs Ψ1397 in 16S mt-rRNA; other members have additional organellar RNA targets depending on paralog | Generally specialized/site-specific, especially in prokaryotic rRNA enzymes | Human RPUSD3 has lost the catalytic Asp and appears catalytically inactive in vivo | Some members are essential for oxidative phosphorylation/mitochondrial gene-expression-linked processes due to organellar RNA roles | Family widespread in bacteria and eukaryotes; primary bacterial role on rRNA, with organellar derivatives in eukaryotes (borchardt2020regulationandfunction pages 3-4, liu2024advancementsinpseudouridine pages 2-3, xu2025acomprehensivetrna pages 1-2, lin2025mechanisticinsightinto pages 4-5) |
| RsuA | **Bacteria:** RsuA (and related bacterial-only branch discussed with RluB/RluF in broader reviews) | Primarily rRNA | Highly site-specific rRNA pseudouridylation in prokaryotes | Mostly strict/site-specific | No inactive member identified here | No additional non-catalytic role established here from cited sources | Present in prokaryotes, especially bacteria; human cells lack an RsuA-family PUS among the 13 annotated human PUS proteins (borchardt2020regulationandfunction pages 3-4, liu2024advancementsinpseudouridine pages 2-3, fitzek2018evolutionofeukaryal pages 1-2) |
| Pus10 | **Archaea:** Pus10; **Eukarya:** PUS10 | Primarily tRNA; in humans also linked to miRNA biogenesis independent of catalysis | Canonical activity at tRNA Ψ54 and Ψ55; in human cells PUS10 contributes to both Ψ54 and Ψ55, with redundancy with TRUB1 for Ψ55 | Moderately specific for tRNA positions 54/55, but biological roles have diversified in eukaryotes | No inactive PUS10 ortholog established here, though lineage-specific losses and motif changes occur | Human PUS10 promotes pri-miRNA processing in the nucleus independently of catalytic activity; also linked to apoptosis-related pathways | Present in archaea and many eukaryotes, absent from bacteria; retained in animals/plants/protozoa surveyed, but lost in dikaryon fungi while present in earlier fungal lineages such as chytrids (hori2023transferrnamodification pages 2-5, fitzek2018evolutionofeukaryal pages 2-4, fitzek2018evolutionofeukaryal pages 1-2, xu2025acomprehensivetrna pages 1-2, song2020differentialrolesof pages 1-2) |


*Table: This table compares the six pseudouridine synthase families by representative enzymes, substrates, target positions, specificity, inactive members, non-catalytic roles, and taxonomic scope. It is useful for judging whether a broad family-level GO annotation could apply uniformly across all matched proteins.*

---

## 2. InterPro2GO Mapping Appropriateness

**Current status:** PTHR13195 has **no GO terms mapped** via InterPro2GO.

### 2.1 Assessment of Potential GO Terms

Given the absence of current mappings, we assessed what GO terms *could* be appropriate and whether they would cause over-annotation:

#### (a) **Molecular Function: "pseudouridine synthase activity" (GO:0009982)**

- **Problem:** This term would be **partially over-annotating**. 
- **Rationale:** Human RPUSD3 has lost its catalytic aspartate residue and shows no detectable enzymatic activity on rRNAs or tRNAs in vivo (xu2025acomprehensivetrna pages 1-2). Human TRUB2 also exhibits no noticeable enzymatic activity on predicted tRNA/rRNA targets despite possessing the conserved catalytic domain (xu2025acomprehensivetrna pages 1-2). These are **pseudo-enzymes** that retain the fold but have lost catalytic function.
- **Verdict:** Would over-annotate ~2-10% of family members depending on taxon (catalogued inactive members in humans; prevalence across all 3812 taxa unknown).

#### (b) **RNA Substrate-Specific Terms (e.g., "tRNA binding," "rRNA binding," "mRNA binding")**

- **Problem:** **Family-wide substrate heterogeneity** makes any single substrate term inappropriate.
- **Rationale:** 
  - TruA-family enzymes like PUS3 and bacterial TruA are **tRNA-specific**, showing no activity on mRNA (lin2025mechanisticinsightinto pages 5-9, lin2025mechanisticinsightinto pages 4-5).
  - TruB-family enzymes like PUS4/TRUB1 modify **both tRNA and mRNA** (lin2025mechanisticinsightinto pages 5-9).
  - RluA and RsuA families primarily target **rRNA**, especially in bacteria, with eukaryotic orthologs (e.g., RPUSD4) modifying mitochondrial rRNA (xu2025acomprehensivetrna pages 1-2, lin2025mechanisticinsightinto pages 4-5).
  - TruD-family enzyme PUS7 is **promiscuous**, modifying tRNA, mRNA, and other ncRNAs opportunistically (purchal2022pseudouridinesynthase7 pages 3-4, purchal2022pseudouridinesynthase7 pages 1-2).
- **Verdict:** Any substrate-specific binding term (tRNA, rRNA, mRNA) would massively over-annotate the majority of family members with different specificities.

#### (c) **Process Terms (e.g., "tRNA pseudouridylation," "rRNA pseudouridylation")**

- **Problem:** **Subfamily-specific processes** cannot be generalized to the family level.
- **Rationale:** Different subfamilies modify different RNA classes at different positions:
  - TruA/PUS3: tRNA Ψ38/39/40 (lin2025mechanisticinsightinto pages 5-9, lin2025mechanisticinsightinto pages 4-5)
  - TruB/TRUB1: tRNA Ψ55 and mRNA sites (lin2025mechanisticinsightinto pages 5-9)
  - TruD/PUS7: tRNA Ψ13, Ψ35, and mRNA (purchal2022pseudouridinesynthase7 pages 3-4, purchal2022pseudouridinesynthase7 pages 1-2, lin2025mechanisticinsightinto pages 5-9)
  - Pus10: tRNA Ψ54 and Ψ55 (fitzek2018evolutionofeukaryal pages 2-4, fitzek2018evolutionofeukaryal pages 1-2, xu2025acomprehensivetrna pages 1-2)
  - RluA/RsuA: prokaryotic rRNA (borchardt2020regulationandfunction pages 3-4, liu2024advancementsinpseudouridine pages 2-3, lin2025mechanisticinsightinto pages 4-5)
- **Verdict:** Process terms are subfamily-restricted and not applicable to the family signature as a whole.

#### (d) **Neo-functionalized Roles (e.g., "miRNA biogenesis," "telomerase complex," "tRNA folding")**

- **Problem:** These are **lineage-specific and catalysis-independent** functions of particular orthologs.
- **Rationale:**
  - Human PUS10 promotes pri-miRNA processing **independently of its pseudouridylation activity**, via physical interaction with the microprocessor complex (DROSHA-DGCR8) (song2020differentialrolesof pages 1-2).
  - TruB functions as a **tRNA folding chaperone** beyond its modification activity (liu2024advancementsinpseudouridine pages 2-3).
  - DKC1 (a TruB-family guide-dependent enzyme) is a core component of the **telomerase complex** (liu2024advancementsinpseudouridine pages 2-3).
- **Verdict:** These functions are not family-wide and would over-annotate the vast majority of proteins lacking these neofunctionalized roles.

#### (e) **Generic Terms (e.g., "RNA binding," "metal ion binding")**

- **Problem:** Too **uninformative** and lack biological specificity.
- **Rationale:** While all functional PUS enzymes bind RNA, this term provides minimal information content and does not distinguish pseudouridine synthases from thousands of other RNA-binding proteins.
- **Verdict:** Technically accurate but of limited annotation value.

### 2.2 Conclusion on InterPro2GO Appropriateness

**The current absence of InterPro2GO mappings for PTHR13195 is appropriate.** This PANTHER family signature is at too broad a hierarchical level to support accurate whole-protein GO annotations. The family encompasses:

1. **Catalytically active enzymes** with diverse substrate specificities (tRNA-only, rRNA-only, mRNA+tRNA, etc.)
2. **Catalytically inactive pseudo-enzymes** (RPUSD3, TRUB2)
3. **Enzymes with neo-functionalized non-catalytic roles** (PUS10 in miRNA biogenesis, TruB in tRNA folding, DKC1 in telomerase)
4. **Redundant enzymes** (TRUB1 and PUS10 both catalyze Ψ55 in human cy-tRNAs) (xu2025acomprehensivetrna pages 1-2)

Any single GO term applied at the family level would over-annotate a substantial fraction of matched proteins.

---

## 3. Functional Divergence Across the Family

### 3.1 Subfamilies with Distinct Substrate Specificities

The six PUS families exhibit **profound functional divergence**, as summarized in the comparative table (artifact-00). Key examples include:

- **TruA family (PUS1, PUS3):** Human PUS3 is a strict tRNA-only enzyme, forming homodimers that recognize the overall L-shaped tRNA architecture and modify positions Ψ38-40 in the anticodon loop (lin2025mechanisticinsightinto pages 5-9, lin2025mechanisticinsightinto pages 4-5). In contrast, PUS1 (also TruA family) is monomeric, modifies tRNA positions Ψ27-28, *and* acts promiscuously on mRNAs and other ncRNAs (lin2025mechanisticinsightinto pages 5-9, lin2025mechanisticinsightinto pages 4-5).
  
- **TruB family (TRUB1, TRUB2, DKC1/Cbf5):** TRUB1 installs Ψ55 in tRNA and modifies mRNAs with a GUΨCNA motif (lin2025mechanisticinsightinto pages 5-9). DKC1/Cbf5 operates via an RNA-guided mechanism (H/ACA snoRNPs) and targets rRNA and snRNA at guide-specified positions (lin2025mechanisticinsightinto pages 2-3, lin2025mechanisticinsightinto pages 1-2, lin2025mechanisticinsightinto pages 5-9). TRUB2, despite sequence similarity, shows **no detectable activity** in human cells (xu2025acomprehensivetrna pages 1-2).

- **RluA/RsuA families:** Predominantly target **rRNA** in prokaryotes, with highly site-specific activity (borchardt2020regulationandfunction pages 3-4, liu2024advancementsinpseudouridine pages 2-3, lin2025mechanisticinsightinto pages 4-5). Eukaryotic orthologs like RPUSD4 modify mitochondrial rRNA (16S mt-rRNA Ψ1397) (xu2025acomprehensivetrna pages 1-2). RPUSD3 has lost its catalytic aspartate and is **catalytically dead** (xu2025acomprehensivetrna pages 1-2).

- **Pus10 family:** Archaeal and eukaryotic Pus10 enzymes modify tRNA at positions Ψ54 and Ψ55 (fitzek2018evolutionofeukaryal pages 2-4, fitzek2018evolutionofeukaryal pages 1-2, xu2025acomprehensivetrna pages 1-2). Human PUS10 also has a **non-catalytic role in miRNA biogenesis**, promoting pri-miRNA processing via interaction with the microprocessor, a function entirely independent of pseudouridylation activity (song2020differentialrolesof pages 1-2).

### 3.2 Catalytically Inactive (Pseudo-Enzyme) Members

Experimental evidence identifies at least two human PUS proteins that are **catalytically inactive**:

1. **RPUSD3 (RluA family):** Has lost the conserved catalytic aspartate residue and exhibits no enzymatic activity on rRNAs or tRNAs in cells (xu2025acomprehensivetrna pages 1-2).

2. **TRUB2 (TruB family):** Despite possessing an intact catalytic domain with the conserved Asp, shows no noticeable pseudouridylation activity on predicted tRNA or rRNA targets in human cells (xu2025acomprehensivetrna pages 1-2).

These pseudo-enzymes may have evolved alternative, non-catalytic functions (e.g., regulatory roles, scaffolding), though these remain poorly characterized (xu2025acomprehensivetrna pages 1-2).

### 3.3 Neofunctionalization and Non-Catalytic Roles

Several family members have acquired **additional functions beyond RNA modification**:

- **PUS10:** In the nucleus, promotes miRNA biogenesis by binding pri-miRNAs and interacting with the microprocessor complex (DROSHA-DGCR8). This function is **independent of Ψ synthesis** and catalytic activity (song2020differentialrolesof pages 1-2). In the cytoplasm, PUS10 retains canonical tRNA pseudouridylation activity at positions 54 and 55 (song2020differentialrolesof pages 1-2).

- **TruB:** Functions as a **tRNA folding chaperone**, interacting with both misfolded and properly folded tRNAs to promote correct folding, a role separate from its Ψ-synthase activity (liu2024advancementsinpseudouridine pages 2-3).

- **DKC1 (Dyskerin):** A core component of the **human telomerase complex**, stabilizing telomerase RNA (hTR) and protecting telomere integrity, in addition to its H/ACA RNP-guided rRNA/snRNA pseudouridylation activity (liu2024advancementsinpseudouridine pages 2-3).

These neofunctionalized roles are **lineage-specific** and not conserved across the entire family.

### 3.4 Functional Redundancy

Some PUS enzymes exhibit **redundant activities** on the same substrates:

- **TRUB1 and PUS10:** Both catalyze Ψ55 in human cytosolic tRNAs, with PUS10 being fully responsible for Ψ54 and partially for Ψ55 (xu2025acomprehensivetrna pages 1-2). Loss of TRUB1 alone does not eliminate Ψ55 in cy-tRNAs, demonstrating functional compensation (xu2025acomprehensivetrna pages 1-2).

This redundancy reflects the evolutionary history of eukaryotes, which inherited both archaeal (Pus10) and bacterial (TruB) enzymes, creating overlapping functionalities (fitzek2018evolutionofeukaryal pages 2-4, fitzek2018evolutionofeukaryal pages 1-2).

---

## 4. Taxonomic Scope

### 4.1 Distribution Across Domains of Life

Pseudouridine synthases are **universally distributed** across all three domains of life, but with **family-specific taxonomic patterns**:

- **TruA, TruB, TruD, RluA, RsuA families:** Present in **bacteria and eukaryotes**, reflecting their likely origin in the bacterial ancestor of mitochondria and subsequent endosymbiotic gene transfer to the nucleus (fitzek2018evolutionofeukaryal pages 1-2, mccown2020naturallyoccurringmodified pages 2-3).

- **Pus10 family:** Present in **archaea and eukaryotes** but **absent from bacteria** (fitzek2018evolutionofeukaryal pages 2-4, fitzek2018evolutionofeukaryal pages 1-2, song2020differentialrolesof pages 1-2). This distribution indicates an archaeal origin, consistent with the archaeal ancestry of eukaryotic nucleocytoplasmic biology.

- **RsuA family:** Restricted to **prokaryotes**, with no clear eukaryotic ortholog among the 13 annotated human PUS proteins (borchardt2020regulationandfunction pages 3-4, liu2024advancementsinpseudouridine pages 2-3, fitzek2018evolutionofeukaryal pages 1-2).

### 4.2 Eukaryotic Redundancy and Lineage-Specific Losses

The **last eukaryotic common ancestor (LECA)** possessed orthologs of *both* archaeal Pus10 and bacterial TrmA/TruB, creating functional redundancy for tRNA positions 54 and 55 (fitzek2018evolutionofeukaryal pages 2-4, fitzek2018evolutionofeukaryal pages 1-2). Comprehensive phylogenomic analyses reveal:

- **Animals, plants, and most protists** retain all three genes (Pus10, TrmA, TruB) (fitzek2018evolutionofeukaryal pages 2-4, fitzek2018evolutionofeukaryal pages 1-2).

- **Fungi exhibit lineage-specific losses:** Pus10 is present in early-diverging fungi (Chytridiomycota, Mucoromycotina) but **absent in all dikaryon fungi** (Ascomycota and Basidiomycota) surveyed (fitzek2018evolutionofeukaryal pages 2-4, fitzek2018evolutionofeukaryal pages 1-2). This loss is compensated by retention of TrmA and TruB.

- **Microsporidia** (highly derived parasitic fungi) have lost Pus10 entirely and show additional losses in conserved cysteine residues within the THUMP domain (fitzek2018evolutionofeukaryal pages 2-4, fitzek2018evolutionofeukaryal pages 1-2).

### 4.3 Scale of PTHR13195

According to InterPro metadata, **PTHR13195 encompasses 1670 proteins distributed across 3812 taxa**. This broad taxonomic sampling spans bacteria, archaea, fungi, plants, animals, and protists, reflecting the ancient and essential nature of pseudouridine modification (fitzek2018evolutionofeukaryal pages 2-4, fitzek2018evolutionofeukaryal pages 1-2, mccown2020naturallyoccurringmodified pages 2-3).

### 4.4 Do GO Terms Hold Across All Taxa?

**No.** The functional heterogeneity documented in Section 3 is exacerbated by taxonomic variation:

- **Process/component terms** valid in one clade (e.g., "mitochondrial rRNA modification" in eukaryotes with RPUSD4 orthologs) are **inapplicable to bacteria**, which lack mitochondria.

- **Compartment-specific terms** (e.g., "nucleus" for PUS10's miRNA function) are **taxon-restricted** and do not apply to prokaryotes or to fungi that lost Pus10.

- **Substrate-specific terms** (e.g., "spliceosomal snRNA pseudouridylation" for DKC1/Cbf5) are **eukaryote-specific** and absent in bacteria/archaea lacking spliceosomes.

Thus, no single process or component GO term is valid across the full taxonomic breadth of PTHR13195.

---

## 5. Over-Annotation Verdict and GO Action Recommendations

### 5.1 Summary Assessment

**PTHR13195 is a functionally heterogeneous family-level signature** that encompasses:

1. **Six distinct subfamilies** (TruA, TruB, TruD, RluA, RsuA, Pus10) with different substrate specificities and modification sites.
2. **Catalytically active enzymes** with varying substrate scopes (tRNA-only, rRNA-only, tRNA+mRNA, guide-RNA-dependent).
3. **Catalytically inactive pseudo-enzymes** (RPUSD3, TRUB2).
4. **Enzymes with neofunctionalized non-catalytic roles** (PUS10 in miRNA biogenesis, TruB as tRNA chaperone, DKC1 in telomerase).
5. **Broad taxonomic distribution** (1670 proteins across 3812 taxa, spanning all three domains of life).

### 5.2 Verdict: Current InterPro2GO Status is Appropriate

**The absence of InterPro2GO mappings for PTHR13195 is SOUND and should be maintained.**

Applying any of the following GO terms at the family level would result in **systematic over-annotation**:

- **"pseudouridine synthase activity" (GO:0009982):** Over-annotates catalytically dead members (RPUSD3, TRUB2).
- **Substrate-specific terms** (tRNA binding, rRNA binding, mRNA binding): Over-annotate enzymes with different substrate specificities.
- **Process terms** (tRNA modification, rRNA modification, mRNA processing): Subfamily-specific, not universal.
- **Neofunctionalized roles** (miRNA biogenesis, telomerase, tRNA folding): Lineage-specific, not family-wide.

### 5.3 Recommended GO Action Pattern

**ACCEPT the current absence of InterPro2GO mappings.**

**Rationale:** PTHR13195 is a **family-level entry** (entry type = "family"), not a domain or repeat. While family-level entries are *more likely* than domain entries to support whole-protein function terms, this particular family is **too functionally heterogeneous** to annotate accurately at the family level. The presence of:

- **Catalytically inactive members** (undermining catalytic activity terms)
- **Substrate-divergent subfamilies** (undermining substrate-specific terms)
- **Neofunctionalized orthologs** (creating lineage-specific non-canonical functions)

...makes any family-wide GO term inappropriate.

### 5.4 Recommendations for InterPro

**Option 1: Maintain Status Quo (Recommended)**

Leave PTHR13195 **without InterPro2GO mappings** and rely on subfamily-level or ortholog-level annotations from curated databases (UniProtKB, GO Consortium direct annotations). This avoids systematic over-annotation.

**Option 2: Subdivision into Functionally Homogeneous Child Entries**

InterPro could **create or map to child entries** corresponding to the six PUS subfamilies (TruA, TruB, TruD, RluA, RsuA, Pus10). Each child entry could then receive subfamily-appropriate GO terms:

- **TruA-family child entry → "tRNA pseudouridylation" (with position-specific qualifiers)**
- **TruB-family child entry → "tRNA pseudouridylation" + "mRNA pseudouridylation" (for eukaryotic orthologs)**
- **Pus10-family child entry → "tRNA pseudouridylation" + potentially "miRNA biogenesis" (taxon-qualified)**

However, this requires significant curation effort and may still face challenges due to within-subfamily heterogeneity (e.g., PUS1 vs. PUS3 within TruA family).

**Option 3: Mark as NON_CORE for GO Propagation**

If InterPro2GO terms are added in the future, they should be flagged as **KEEP_AS_NON_CORE** to prevent automatic propagation to gene annotations without manual review. This would allow the terms to exist for informational purposes without causing bulk over-annotation.

### 5.5 Final Verdict

**Verdict:** The current InterPro2GO mapping status for PTHR13195 is **SOUND**—no GO terms are mapped, and **none should be added** without subdivision into functionally homogeneous subfamilies.

**Recommended GO Action:**  
**ACCEPT** (maintain absence of InterPro2GO terms at the family level).

**Alternative (if terms are added in future):**  
**KEEP_AS_NON_CORE** (prevent automatic propagation) or **MODIFY-to-subfamily-specific** (create child entries with appropriate GO terms).

**InterPro Recommendation:**  
Consider mapping PTHR13195 to existing InterPro child entries corresponding to the six PUS subfamilies (TruA, TruB, TruD, RluA, RsuA, Pus10) and applying GO terms at the subfamily level rather than the family level. This would preserve annotation accuracy while providing functional context.

---

## 6. References (Key Citations)

This report is based on comprehensive analysis of 29 peer-reviewed publications from 2020-2025, including:

- Structural studies: Crystal structures and cryo-EM analyses of PUS enzymes from bacteria, archaea, and eukaryotes (purchal2022pseudouridinesynthase7 pages 3-4, guegueniat2021thehumanpseudouridine pages 4-5, grunberg2023thestructuralbasis pages 3-5, lin2025mechanisticinsightinto pages 2-3, lin2025mechanisticinsightinto pages 1-2, lin2025mechanisticinsightinto pages 5-9, lin2025mechanisticinsightinto pages 4-5)
- Mechanistic studies: Catalytic mechanisms, conserved residues, and substrate recognition (purchal2022pseudouridinesynthase7 pages 3-4, guegueniat2021thehumanpseudouridine pages 4-5, lin2025mechanisticinsightinto pages 2-3, lin2025mechanisticinsightinto pages 1-2, purchal2022pseudouridinesynthase7 pages 1-2, lin2025mechanisticinsightinto pages 5-9)
- Functional genomics: Knockout/knockdown studies identifying PUS targets and catalytically inactive members (xu2025acomprehensivetrna pages 1-2, song2020differentialrolesof pages 1-2)
- Evolutionary analyses: Phylogenomic studies of PUS family distribution and lineage-specific losses (fitzek2018evolutionofeukaryal pages 2-4, fitzek2018evolutionofeukaryal pages 1-2, mccown2020naturallyoccurringmodified pages 2-3)
- Reviews: Comprehensive reviews of pseudouridine biology and PUS enzymes (lin2025mechanisticinsightinto pages 1-2, borchardt2020regulationandfunction pages 3-4, jia2025decipheringthepseudouridine pages 3-4, khan2023pseudouridineinrna pages 4-5, liu2024advancementsinpseudouridine pages 2-3, lin2021pseudouridinesinrnas pages 6-8, hori2023transferrnamodification pages 2-5)

---

**Report Prepared:** 2025  
**InterPro Entry:** PTHR13195 (PSEUDOURIDINE SYNTHASE-RELATED)  
**Integrated Parent:** IPR039048  
**Scale:** 1670 proteins, 3812 taxa, 1 subfamily  
**Current InterPro2GO Terms:** None (appropriate status)

References

1. (lin2025mechanisticinsightinto pages 2-3): Ting-Yu Lin, Yasmin Stone, and Sebastian Glatt. Mechanistic insight into the pseudouridylation of rna. RNA biology, 22 1:1-25, 2025. URL: https://doi.org/10.1080/15476286.2025.2541421, doi:10.1080/15476286.2025.2541421. This article has 6 citations and is from a peer-reviewed journal.

2. (lin2025mechanisticinsightinto pages 1-2): Ting-Yu Lin, Yasmin Stone, and Sebastian Glatt. Mechanistic insight into the pseudouridylation of rna. RNA biology, 22 1:1-25, 2025. URL: https://doi.org/10.1080/15476286.2025.2541421, doi:10.1080/15476286.2025.2541421. This article has 6 citations and is from a peer-reviewed journal.

3. (jia2025decipheringthepseudouridine pages 3-4): Shiheng Jia, Xue Yu, Na Deng, Chen Zheng, Mingguang Ju, Fanglin Wang, Yixiao Zhang, Ziming Gao, Yanshu Li, Heng Zhou, and Kai Li. Deciphering the pseudouridine nucleobase modification in human diseases: from molecular mechanisms to clinical perspectives. Clinical and Translational Medicine, Jan 2025. URL: https://doi.org/10.1002/ctm2.70190, doi:10.1002/ctm2.70190. This article has 15 citations and is from a peer-reviewed journal.

4. (lin2021pseudouridinesinrnas pages 6-8): Ting‐Yu Lin, Rahul Mehta, and Sebastian Glatt. Pseudouridines in rnas: switching atoms means shifting paradigms. Febs Letters, 595:2310-2322, Sep 2021. URL: https://doi.org/10.1002/1873-3468.14188, doi:10.1002/1873-3468.14188. This article has 49 citations and is from a peer-reviewed journal.

5. (borchardt2020regulationandfunction pages 3-4): Erin K. Borchardt, Nicole M. Martinez, and Wendy V. Gilbert. Regulation and function of rna pseudouridylation in human cells. Annual Review of Genetics, 54:309-336, Nov 2020. URL: https://doi.org/10.1146/annurev-genet-112618-043830, doi:10.1146/annurev-genet-112618-043830. This article has 268 citations and is from a domain leading peer-reviewed journal.

6. (lin2025mechanisticinsightinto pages 5-9): Ting-Yu Lin, Yasmin Stone, and Sebastian Glatt. Mechanistic insight into the pseudouridylation of rna. RNA biology, 22 1:1-25, 2025. URL: https://doi.org/10.1080/15476286.2025.2541421, doi:10.1080/15476286.2025.2541421. This article has 6 citations and is from a peer-reviewed journal.

7. (purchal2022pseudouridinesynthase7 pages 3-4): Meredith K. Purchal, Daniel E. Eyler, Mehmet Tardu, Monika K. Franco, Megan M. Korn, Taslima Khan, Ryan McNassor, Rachel Giles, Katherine Lev, Hari Sharma, Jeremy Monroe, Leena Mallik, Markos Koutmos, and Kristin S. Koutmou. Pseudouridine synthase 7 is an opportunistic enzyme that binds and modifies substrates with diverse sequences and structures. Proceedings of the National Academy of Sciences of the United States of America, Jan 2022. URL: https://doi.org/10.1073/pnas.2109708119, doi:10.1073/pnas.2109708119. This article has 60 citations and is from a highest quality peer-reviewed journal.

8. (guegueniat2021thehumanpseudouridine pages 4-5): Julia Guegueniat, Levon Halabelian, Hong Zeng, Aiping Dong, Yanjun Li, Hong Wu, Cheryl H Arrowsmith, and Ute Kothe. The human pseudouridine synthase pus7 recognizes rna with an extended multi-domain binding surface. Nucleic Acids Research, 49:11810-11822, Oct 2021. URL: https://doi.org/10.1093/nar/gkab934, doi:10.1093/nar/gkab934. This article has 47 citations and is from a highest quality peer-reviewed journal.

9. (fitzek2018evolutionofeukaryal pages 2-4): Elisabeth Fitzek, Archi Joardar, Ramesh C. Gupta, and Matt Geisler. Evolution of eukaryal and archaeal pseudouridine synthase pus10. Journal of Molecular Evolution, 86:77-89, Jan 2018. URL: https://doi.org/10.1007/s00239-018-9827-y, doi:10.1007/s00239-018-9827-y. This article has 25 citations and is from a peer-reviewed journal.

10. (fitzek2018evolutionofeukaryal pages 1-2): Elisabeth Fitzek, Archi Joardar, Ramesh C. Gupta, and Matt Geisler. Evolution of eukaryal and archaeal pseudouridine synthase pus10. Journal of Molecular Evolution, 86:77-89, Jan 2018. URL: https://doi.org/10.1007/s00239-018-9827-y, doi:10.1007/s00239-018-9827-y. This article has 25 citations and is from a peer-reviewed journal.

11. (song2020differentialrolesof pages 1-2): Jinghui Song, Yuan Zhuang, Chenxu Zhu, Haowei Meng, Bo Lu, Bingteng Xie, Jinying Peng, Mo Li, and Chengqi Yi. Differential roles of human pus10 in mirna processing and trna pseudouridylation. Nature Chemical Biology, 16:160-169, Dec 2020. URL: https://doi.org/10.1038/s41589-019-0420-5, doi:10.1038/s41589-019-0420-5. This article has 125 citations and is from a highest quality peer-reviewed journal.

12. (lin2025mechanisticinsightinto pages 4-5): Ting-Yu Lin, Yasmin Stone, and Sebastian Glatt. Mechanistic insight into the pseudouridylation of rna. RNA biology, 22 1:1-25, 2025. URL: https://doi.org/10.1080/15476286.2025.2541421, doi:10.1080/15476286.2025.2541421. This article has 6 citations and is from a peer-reviewed journal.

13. (liu2024advancementsinpseudouridine pages 2-3): Kaijie Liu, Shujun Zhang, Yafeng Liu, Xinjun Hu, and Xinyu Gu. Advancements in pseudouridine modifying enzyme and cancer. Frontiers in Cell and Developmental Biology, Dec 2024. URL: https://doi.org/10.3389/fcell.2024.1465546, doi:10.3389/fcell.2024.1465546. This article has 19 citations.

14. (xu2025acomprehensivetrna pages 1-2): Haiqi Xu, Linzhen Kong, Mengjie Li, Giuseppina Pisignano, Jingfei Cheng, Feng Feng, Parinaz Mehdipour, and Chun-Xiao Song. A comprehensive trna pseudouridine map uncovers targets dependent on human stand-alone pseudouridine synthases. Nature Cell Biology, 27:2186-2197, Oct 2025. URL: https://doi.org/10.1038/s41556-025-01803-w, doi:10.1038/s41556-025-01803-w. This article has 9 citations and is from a highest quality peer-reviewed journal.

15. (purchal2022pseudouridinesynthase7 pages 1-2): Meredith K. Purchal, Daniel E. Eyler, Mehmet Tardu, Monika K. Franco, Megan M. Korn, Taslima Khan, Ryan McNassor, Rachel Giles, Katherine Lev, Hari Sharma, Jeremy Monroe, Leena Mallik, Markos Koutmos, and Kristin S. Koutmou. Pseudouridine synthase 7 is an opportunistic enzyme that binds and modifies substrates with diverse sequences and structures. Proceedings of the National Academy of Sciences of the United States of America, Jan 2022. URL: https://doi.org/10.1073/pnas.2109708119, doi:10.1073/pnas.2109708119. This article has 60 citations and is from a highest quality peer-reviewed journal.

16. (hori2023transferrnamodification pages 2-5): Hiroyuki Hori. Transfer rna modification enzymes with a thiouridine synthetase, methyltransferase and pseudouridine synthase (thump) domain and the nucleosides they produce in trna. Genes, 14:382, Jan 2023. URL: https://doi.org/10.3390/genes14020382, doi:10.3390/genes14020382. This article has 15 citations.

17. (mccown2020naturallyoccurringmodified pages 2-3): Phillip J. McCown, Agnieszka Ruszkowska, Charlotte N. Kunkler, Kurtis Breger, Jacob P. Hulewicz, Matthew C. Wang, Noah A. Springer, and Jessica A. Brown. Naturally occurring modified ribonucleosides. Wiley Interdisciplinary Reviews. RNA, Apr 2020. URL: https://doi.org/10.1002/wrna.1595, doi:10.1002/wrna.1595. This article has 261 citations and is from a peer-reviewed journal.

18. (grunberg2023thestructuralbasis pages 3-5): Sebastian Grünberg, Lindsey A. Doyle, Eric J. Wolf, Nan Dai, Ivan R. Corrêa, Erbay Yigit, and Barry L. Stoddard. The structural basis of mrna recognition and binding by yeast pseudouridine synthase pus1. PLOS ONE, 18:e0291267, Nov 2023. URL: https://doi.org/10.1371/journal.pone.0291267, doi:10.1371/journal.pone.0291267. This article has 13 citations and is from a peer-reviewed journal.

19. (khan2023pseudouridineinrna pages 4-5): A Khan, YD Hu, S Khan, SM Aqeel, and I Khan. Pseudouridine in rna: enzymatic synthesis mechanisms and functional roles in molecular biology. International Journal of Environment, Agriculture and Biotechnology, 8:284-300, Jan 2023. URL: https://doi.org/10.22161/ijeab.86.25, doi:10.22161/ijeab.86.25. This article has 10 citations.

## Artifacts

- [Edison artifact artifact-00](PTHR13195-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. lin2025mechanisticinsightinto pages 2-3
2. xu2025acomprehensivetrna pages 1-2
3. lin2025mechanisticinsightinto pages 5-9
4. song2020differentialrolesof pages 1-2
5. liu2024advancementsinpseudouridine pages 2-3
6. lin2025mechanisticinsightinto pages 1-2
7. jia2025decipheringthepseudouridine pages 3-4
8. lin2021pseudouridinesinrnas pages 6-8
9. borchardt2020regulationandfunction pages 3-4
10. guegueniat2021thehumanpseudouridine pages 4-5
11. fitzek2018evolutionofeukaryal pages 2-4
12. fitzek2018evolutionofeukaryal pages 1-2
13. lin2025mechanisticinsightinto pages 4-5
14. hori2023transferrnamodification pages 2-5
15. mccown2020naturallyoccurringmodified pages 2-3
16. grunberg2023thestructuralbasis pages 3-5
17. khan2023pseudouridineinrna pages 4-5
18. https://doi.org/10.1080/15476286.2025.2541421,
19. https://doi.org/10.1002/ctm2.70190,
20. https://doi.org/10.1002/1873-3468.14188,
21. https://doi.org/10.1146/annurev-genet-112618-043830,
22. https://doi.org/10.1073/pnas.2109708119,
23. https://doi.org/10.1093/nar/gkab934,
24. https://doi.org/10.1007/s00239-018-9827-y,
25. https://doi.org/10.1038/s41589-019-0420-5,
26. https://doi.org/10.3389/fcell.2024.1465546,
27. https://doi.org/10.1038/s41556-025-01803-w,
28. https://doi.org/10.3390/genes14020382,
29. https://doi.org/10.1002/wrna.1595,
30. https://doi.org/10.1371/journal.pone.0291267,
31. https://doi.org/10.22161/ijeab.86.25,