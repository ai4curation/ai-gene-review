---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-24T04:50:44.824394'
end_time: '2026-06-24T05:02:40.743812'
duration_seconds: 715.92
template_file: templates/treegrafter_family_function.md
template_variables:
  family_id: PTHR10681
  family_name: THIOREDOXIN PEROXIDASE
  subfamily: PTHR10681:SF121 ALKYL HYDROPEROXIDE REDUCTASE C
  gene_symbol: ahpC
  uniprot: Q88K52
  organism: PSEPK
  taxon_label: PSEPK
  propagated_term: thioredoxin peroxidase activity (GO:0008379)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 25
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PTHR10681-function-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR10681-function-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# PANTHER Family Function Characterization (TreeGrafter granularity audit)

You are characterizing the function of a **protein family** for AI Gene Review.
This is the companion to a set of blinded gene-level function checks: the point
here is to establish, from primary literature and sequence/structure evidence,
**what function is actually conserved across the family** and **where function
diverges between subfamilies** — because automated phylogenetic annotation
(TreeGrafter/PANTHER) propagates a GO term from an ancestral node to every
descendant, and that is only safe when the family is functionally homogeneous.

## Family Under Review

- **PANTHER family:** PTHR10681 — THIOREDOXIN PEROXIDASE
- **Subfamily of interest:** PTHR10681:SF121 ALKYL HYDROPEROXIDE REDUCTASE C
- **Representative member:** ahpC (Q88K52), PSEPK / PSEPK
- **GO term currently propagated at/near this node:** thioredoxin peroxidase activity (GO:0008379)

Note: do **not** assume the propagated term is the family's true conserved
function — that is exactly what you are testing.

## Research Objective

1. **Conserved core function.** What molecular function (and reaction/EC where
   relevant) is shared by *characterized* members across the whole family? Anchor
   this to the diagnostic fold, catalytic/binding residues, and obligate
   cofactors/partners — not to the family name.
2. **Functional divergence across subfamilies.** Enumerate the major
   functional subgroups within the family and how they differ (substrate
   specificity, lost catalysis / pseudo-enzymes, neofunctionalization, structural
   co-option). Is the family **homogeneous** (one MF safe to propagate) or
   **heterogeneous** (propagation will mis-annotate some branches)?
3. **Subfamily of interest.** Where does PTHR10681:SF121 ALKYL HYDROPEROXIDE REDUCTASE C sit — does it carry the
   conserved family function, a more specific specialized activity, or a diverged
   / non-enzymatic role? Name characterized exemplars of that subfamily.
4. **GO granularity verdict.** State the GO MF term appropriate at the **family**
   level versus at the **subfamily** level, and identify any subfamilies for
   which a family-level term would be an over-annotation. This is a lead for
   curators, not a final call.

Where decidable by computation, actually run it (domain/Pfam/InterPro
architecture, catalytic-residue conservation, orthology/paralogy splits) and keep
the result as provenance. Use resources you can access programmatically
(UniProt, InterPro, AlphaFold, sequence computation, public APIs). Prefer PMID
citations to primary literature; treat reviews/databases as orientation. If a
check is web-only or cannot be run, say so — an inconclusive result is acceptable;
never fabricate one.

## Required Output

### Family Function Summary

One paragraph: the conserved core molecular function and the fold/residues that
define it.

### Subfamily Divergence Table

One row per major functional subgroup: subgroup / representative member(s) (PMID)
· molecular function · substrate or specialization · catalytic residues intact?
· GO MF term that fits · notes (pseudo-enzyme, neofunctionalization, etc.).

### Homogeneous vs Heterogeneous Verdict

State plainly whether a single family-level GO MF term is safe to propagate
across this family, and if not, which branches it would mis-annotate.

### Granularity Leads for Curation

Family-level vs subfamily-level GO MF term recommendation, and the subfamilies
(if any) where the currently-propagated term is an over-annotation. Avoid
"protein binding" as a final recommendation.

### Evidence and Gaps

Key citations (PMID preferred), and explicit uncertainties that matter for
deciding the family-vs-subfamily granularity.


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

# PANTHER Family Function Characterization (TreeGrafter granularity audit)

You are characterizing the function of a **protein family** for AI Gene Review.
This is the companion to a set of blinded gene-level function checks: the point
here is to establish, from primary literature and sequence/structure evidence,
**what function is actually conserved across the family** and **where function
diverges between subfamilies** — because automated phylogenetic annotation
(TreeGrafter/PANTHER) propagates a GO term from an ancestral node to every
descendant, and that is only safe when the family is functionally homogeneous.

## Family Under Review

- **PANTHER family:** PTHR10681 — THIOREDOXIN PEROXIDASE
- **Subfamily of interest:** PTHR10681:SF121 ALKYL HYDROPEROXIDE REDUCTASE C
- **Representative member:** ahpC (Q88K52), PSEPK / PSEPK
- **GO term currently propagated at/near this node:** thioredoxin peroxidase activity (GO:0008379)

Note: do **not** assume the propagated term is the family's true conserved
function — that is exactly what you are testing.

## Research Objective

1. **Conserved core function.** What molecular function (and reaction/EC where
   relevant) is shared by *characterized* members across the whole family? Anchor
   this to the diagnostic fold, catalytic/binding residues, and obligate
   cofactors/partners — not to the family name.
2. **Functional divergence across subfamilies.** Enumerate the major
   functional subgroups within the family and how they differ (substrate
   specificity, lost catalysis / pseudo-enzymes, neofunctionalization, structural
   co-option). Is the family **homogeneous** (one MF safe to propagate) or
   **heterogeneous** (propagation will mis-annotate some branches)?
3. **Subfamily of interest.** Where does PTHR10681:SF121 ALKYL HYDROPEROXIDE REDUCTASE C sit — does it carry the
   conserved family function, a more specific specialized activity, or a diverged
   / non-enzymatic role? Name characterized exemplars of that subfamily.
4. **GO granularity verdict.** State the GO MF term appropriate at the **family**
   level versus at the **subfamily** level, and identify any subfamilies for
   which a family-level term would be an over-annotation. This is a lead for
   curators, not a final call.

Where decidable by computation, actually run it (domain/Pfam/InterPro
architecture, catalytic-residue conservation, orthology/paralogy splits) and keep
the result as provenance. Use resources you can access programmatically
(UniProt, InterPro, AlphaFold, sequence computation, public APIs). Prefer PMID
citations to primary literature; treat reviews/databases as orientation. If a
check is web-only or cannot be run, say so — an inconclusive result is acceptable;
never fabricate one.

## Required Output

### Family Function Summary

One paragraph: the conserved core molecular function and the fold/residues that
define it.

### Subfamily Divergence Table

One row per major functional subgroup: subgroup / representative member(s) (PMID)
· molecular function · substrate or specialization · catalytic residues intact?
· GO MF term that fits · notes (pseudo-enzyme, neofunctionalization, etc.).

### Homogeneous vs Heterogeneous Verdict

State plainly whether a single family-level GO MF term is safe to propagate
across this family, and if not, which branches it would mis-annotate.

### Granularity Leads for Curation

Family-level vs subfamily-level GO MF term recommendation, and the subfamilies
(if any) where the currently-propagated term is an over-annotation. Avoid
"protein binding" as a final recommendation.

### Evidence and Gaps

Key citations (PMID preferred), and explicit uncertainties that matter for
deciding the family-vs-subfamily granularity.


# PANTHER Family PTHR10681 — THIOREDOXIN PEROXIDASE (Peroxiredoxin) Function Characterization

## Family Function Summary

PANTHER family PTHR10681, annotated as "THIOREDOXIN PEROXIDASE," corresponds to the peroxiredoxin (Prx) superfamily of cysteine-dependent peroxidases. All characterized members share a conserved thioredoxin fold defined by a core of four β-strands and flanking α-helices, with a universally conserved peroxidatic cysteine (C_P) embedded in a PxxxTxxC motif (perkins2015peroxiredoxinsguardiansagainst pages 2-3, vaskova2023glutathionerelatedenzymesand pages 10-11). The C_P thiolate (pKa 5.1–6.3) attacks hydroperoxide substrates — including H₂O₂, alkyl hydroperoxides, and peroxynitrite — becoming oxidized to a sulfenic acid (C_P-SOH) intermediate (perkins2015peroxiredoxinsguardiansagainst pages 2-3, qausain2024unravelingtheperoxidase pages 1-3). This sulfenic acid is then resolved, either by a resolving cysteine (C_R) located on the same or an adjacent subunit (forming a disulfide that is subsequently reduced by an electron donor), or directly by small-molecule thiols such as glutathione (vaskova2023glutathionerelatedenzymesand pages 10-11, xue2024unveilingthesignificance pages 1-3). The conserved core molecular function across the family is **peroxidase activity via cysteine-based peroxide reduction** (EC 1.11.1.15, peroxiredoxin). However, the identity of the obligate electron donor varies dramatically across subfamilies: thioredoxin (Trx) is used by the eukaryotic typical 2-Cys Prx1–4 and atypical 2-Cys Prx5 branches, while bacterial AhpC members preferentially use AhpF (NADH-dependent) or AhpD, and the 1-Cys Prx6 subfamily uses glutathione with glutathione S-transferase π (zhang2019molecularmechanismsof pages 7-9, zhang2019molecularmechanismsof pages 4-5, xue2024unveilingthesignificance pages 1-3, thapa2023theroleof pages 2-4). Therefore, the family name "thioredoxin peroxidase" and the propagated GO term GO:0008379 ("thioredoxin peroxidase activity") are over-specific: they correctly describe only a subset of the family's members.

---

## Subfamily Divergence Table

The following table enumerates the major functional subgroups within PTHR10681, their catalytic features, electron donor usage, substrate specialization, and the GO MF term most appropriate for each.

| Subgroup/Subfamily | Representative Members (PMID/citation) | Molecular Function | Substrate/Specialization | Catalytic Residues Intact? | Electron Donor | GO MF Term That Fits | Notes |
|---|---|---|---|---|---|---|---|
| Prx1/AhpC (typical 2-Cys) | Mammalian PRDX1-4; yeast TSA; bacterial AhpC (perkins2015peroxiredoxinsguardiansagainst pages 2-3, vaskova2023glutathionerelatedenzymesand pages 10-11, thapa2023theroleof pages 1-2) | Cys-based peroxidase / peroxiredoxin | H2O2, alkyl hydroperoxides, often peroxynitrite | Yes: CP + CR; intersubunit disulfide typical of 2-Cys Prx | Usually thioredoxin in eukaryotic/yeast members; AhpF or AhpD in many bacterial AhpC branches | GO:0008379 for clearly Trx-dependent members; GO:0051920 for AhpF/AhpD-dependent branches | Shared thioredoxin fold and PxxxTxxC catalytic motif; family label “thioredoxin peroxidase” is too narrow for AhpC-like bacterial branches (perkins2015peroxiredoxinsguardiansagainst pages 2-3, wan2021distincth2o2scavengingsystem pages 10-12) |
| Prx5 (atypical 2-Cys) | Mammalian PRDX5 / PrxV (vaskova2023glutathionerelatedenzymesand pages 10-11, thapa2023theroleof pages 1-2, thapa2023theroleof pages 2-4) | Cys-based peroxidase / peroxiredoxin | H2O2, alkyl hydroperoxides, peroxynitrite | Yes: CP + CR; intrasubunit disulfide | Thioredoxin | GO:0008379 | Atypical 2-Cys architecture; retains peroxidase core but differs from Prx1/AhpC in CR placement and redox cycle topology (vaskova2023glutathionerelatedenzymesand pages 10-11, thapa2023theroleof pages 2-4) |
| Prx6 (1-Cys) | Mammalian PRDX6 (xue2024unveilingthesignificance pages 1-3, thapa2023theroleof pages 2-4, jia2023antioxidantandprooxidant pages 9-11) | Peroxiredoxin/peroxidase plus phospholipase A2 and LPCAT activities | H2O2, short-chain hydroperoxides, phospholipid hydroperoxides; membrane lipid repair | CP only; no canonical resolving CR | Glutathione with GST-pi, not thioredoxin | GO:0051920 for peroxiredoxin activity plus a separate phospholipase A2 MF term; not GO:0008379 | Clear bifunctional/neofunctionalized branch; strongest evidence that a single thioredoxin-dependent MF is unsafe at family level (xue2024unveilingthesignificance pages 1-3, thapa2023theroleof pages 2-4, lagal2024lossofperoxiredoxin pages 5-6) |
| Tpx | Bacterial thiol peroxidase Tpx (subfamily noted in Prx classifications) (perkins2015peroxiredoxinsguardiansagainst pages 2-3, vaskova2023glutathionerelatedenzymesand pages 10-11) | Cys-based peroxidase / peroxiredoxin | H2O2 and alkyl hydroperoxides | Yes: CP + CR; atypical 2-Cys-type arrangement | Thioredoxin | GO:0008379 | Conserved peroxiredoxin chemistry, but less direct recent primary characterization in retrieved set than AhpC/Prx6; classification evidence supports Trx-dependent branch assignment (perkins2015peroxiredoxinsguardiansagainst pages 2-3, vaskova2023glutathionerelatedenzymesand pages 10-11) |
| PrxQ/BCP | Bacterial/plant PrxQ / bacterioferritin comigratory protein (perkins2015peroxiredoxinsguardiansagainst pages 2-3, vaskova2023glutathionerelatedenzymesand pages 10-11) | Cys-based peroxidase / peroxiredoxin | H2O2 and organic hydroperoxides | Usually CP + CR, but CR position/mechanism variable | Thioredoxin or other reductants depending on branch | GO:0051920 | Functionally closer to generic peroxiredoxin activity than specifically thioredoxin peroxidase activity because reductant usage varies (perkins2015peroxiredoxinsguardiansagainst pages 2-3) |
| AhpE | Mycobacterial AhpE (classified Prx subfamily) (perkins2015peroxiredoxinsguardiansagainst pages 2-3, vaskova2023glutathionerelatedenzymesand pages 10-11) | Cys-based peroxidase / peroxiredoxin | Fatty-acid hydroperoxides and related organic peroxides | CP present; 1-Cys-like branch lacking canonical Prx1-style CR pairing | Thioredoxin-related or mycothiol-linked systems reported for actinobacteria; exact donor can vary by system | GO:0051920 | Bacterial-restricted subfamily; substrate specialization and non-canonical reductant context argue against GO:0008379 as a universal branch label (perkins2015peroxiredoxinsguardiansagainst pages 2-3, vaskova2023glutathionerelatedenzymesand pages 10-11) |
| PTHR10681:SF121 AhpC specifically | Bacterial AhpC exemplars including Escherichia coli, Salmonella Typhimurium, Burkholderia thailandensis; representative bacterial AhpC branch including Pseudomonas AhpC-like proteins (zhang2019molecularmechanismsof pages 7-9, zhang2019molecularmechanismsof pages 4-5, groot2022thiolreductasesin pages 16-17, wan2021distincth2o2scavengingsystem pages 10-12) | Alkyl hydroperoxide reductase / peroxiredoxin peroxidase | H2O2, alkyl hydroperoxides, often peroxynitrite | Yes: CP + C-terminal CR residues; intersubunit typical 2-Cys mechanism | Primarily AhpF (NADH-linked) or AhpD in many bacteria; thioredoxin can be secondary in some species | GO:0051920, not GO:0008379 | This is the clearest over-annotation risk for the current propagated term: characterized AhpC proteins often are not primarily thioredoxin-dependent, even though they remain bona fide peroxiredoxins (zhang2019molecularmechanismsof pages 7-9, zhang2019molecularmechanismsof pages 4-5, wan2021distincth2o2scavengingsystem pages 10-12, groot2022thiolreductasesin pages 30-31) |


*Table: This table summarizes the major functional subgroups within PTHR10681 and highlights where reductant usage, catalytic architecture, and additional activities diverge. It is useful for deciding whether GO:0008379 is safe at family level or should be restricted to specific thioredoxin-dependent branches.*

---

## Homogeneous vs. Heterogeneous Verdict

**PTHR10681 is functionally HETEROGENEOUS.** A single family-level GO MF term of "thioredoxin peroxidase activity" (GO:0008379) is **not safe** to propagate across this family. The key axes of heterogeneity are:

1. **Electron donor divergence.** The defining qualifier in GO:0008379 is the assertion that thioredoxin serves as the electron donor. This is experimentally validated for the eukaryotic typical 2-Cys branch (Prx1–4) and Prx5, but is incorrect for multiple other subfamilies. Bacterial AhpC proteins (including the subfamily of interest, SF121) primarily use AhpF or AhpD as their physiological reductant, with thioredoxin serving only as a secondary or alternative donor in some species (zhang2019molecularmechanismsof pages 7-9, zhang2019molecularmechanismsof pages 4-5, wan2021distincth2o2scavengingsystem pages 10-12). The 1-Cys Prx6 subfamily uses glutathione/GST-π rather than thioredoxin (xue2024unveilingthesignificance pages 1-3, thapa2023theroleof pages 2-4).

2. **Neofunctionalization.** PRDX6 has acquired phospholipase A2 (aiPLA2) and lysophosphatidylcholine acyltransferase (LPCAT) enzymatic activities in addition to its peroxidase function (xue2024unveilingthesignificance pages 1-3, jia2023antioxidantandprooxidant pages 3-4, lagal2024lossofperoxiredoxin pages 5-6). These additional activities are structurally independent of the peroxidatic site and are absent from all other subfamilies.

3. **Moonlighting functions.** Several 2-Cys Prx members gain molecular chaperone activity upon hyperoxidation-induced oligomerization, representing a redox-state-dependent functional switch beyond peroxidase catalysis (groot2022thiolreductasesin pages 16-17).

4. **Substrate breadth.** While all subfamilies reduce peroxides, substrate preferences differ: Prx6 specializes in phospholipid hydroperoxides; AhpC is optimized for small alkyl hydroperoxides and H₂O₂; AhpE shows preference for fatty acid hydroperoxides (perkins2015peroxiredoxinsguardiansagainst pages 2-3, zhang2019molecularmechanismsof pages 4-5, xue2024unveilingthesignificance pages 1-3).

Propagating GO:0008379 at the family root would **mis-annotate** at least four branches: AhpC (SF121), Prx6, PrxQ/BCP, and AhpE.

---

## Subfamily of Interest: PTHR10681:SF121 — ALKYL HYDROPEROXIDE REDUCTASE C (AhpC)

SF121 (AhpC) sits within the Prx1/AhpC clade and retains the full typical 2-Cys peroxiredoxin catalytic architecture: a conserved N-terminal peroxidatic cysteine (e.g., Cys57 in *B. thailandensis*) and C-terminal resolving cysteines (e.g., Cys171 and Cys173), forming intersubunit disulfide bonds during the catalytic cycle (zhang2019molecularmechanismsof pages 7-9, zhang2019molecularmechanismsof pages 5-7). AhpC catalyzes the reduction of H₂O₂, tert-butyl hydroperoxide, cumene hydroperoxide, and peroxynitrite (zhang2019molecularmechanismsof pages 4-5, zhang2019molecularmechanismsof pages 1-2).

The critical functional distinction is in the electron donor. Characterized AhpC enzymes overwhelmingly use **AhpF** (a FAD-containing NADH-dependent reductase with a thioredoxin-like domain that mediates electron transfer to AhpC) as their primary reductant (groot2022thiolreductasesin pages 16-17, wan2021distincth2o2scavengingsystem pages 10-12, groot2022thiolreductasesin pages 30-31). In organisms lacking AhpF (e.g., mycobacteria, *Burkholderia*), **AhpD** serves as the alternative reductase, with higher catalytic efficiency than thioredoxin C (kcat/Km of 4.29 × 10⁵ vs. 0.79 × 10⁵ M⁻¹s⁻¹ for cumene hydroperoxide) (zhang2019molecularmechanismsof pages 4-5). Although thioredoxin can serve as a secondary electron donor for some AhpC proteins, it is not the physiologically preferred pathway (zhang2019molecularmechanismsof pages 7-9, wan2021distincth2o2scavengingsystem pages 10-12).

**Characterized exemplars** include: *Salmonella typhimurium* AhpC (the founding member of the Prx1 subfamily) (perkins2015peroxiredoxinsguardiansagainst pages 2-3), *E. coli* AhpC, *Burkholderia thailandensis* AhpC (PMID: 31354673) (zhang2019molecularmechanismsof pages 7-9, zhang2019molecularmechanismsof pages 1-2), and *Yersinia pseudotuberculosis* AhpC (wan2021distincth2o2scavengingsystem pages 10-12). The representative member Q88K52 is from *Pseudomonas putida* KT2440.

**Verdict for SF121:** AhpC carries the conserved family peroxidase function but with a specialized electron donor pathway (AhpF/AhpD rather than thioredoxin). Annotating it as "thioredoxin peroxidase activity" (GO:0008379) is an **over-annotation** that misstates the enzyme's primary reducing system.

---

## GO Granularity Verdict and Curation Leads

| Level | Recommended GO MF Term | Term ID | Applies To | Rationale |
|---|---|---|---|---|
| Family level (PTHR10681) | peroxiredoxin activity | GO:0051920 | All subfamilies | Conserved CP-based peroxide reduction is the shared family function across Prx1/AhpC, Prx5, Prx6, Tpx, PrxQ/BCP, and AhpE; the electron donor is not conserved across the whole family (perkins2015peroxiredoxinsguardiansagainst pages 2-3, vaskova2023glutathionerelatedenzymesand pages 10-11) |
| Subfamily: Prx1-4 (eukaryotic typical 2-Cys) | thioredoxin peroxidase activity | GO:0008379 | Prx1-4, TSA | Typical 2-Cys eukaryotic/yeast members are experimentally established thioredoxin-dependent peroxidases with intersubunit disulfide cycling (vaskova2023glutathionerelatedenzymesand pages 10-11, thapa2023theroleof pages 1-2, thapa2023theroleof pages 2-4) |
| Subfamily: AhpC (SF121, bacterial) | peroxiredoxin activity (or alkyl hydroperoxide reductase activity) | GO:0051920 | Bacterial AhpC | Characterized AhpC enzymes are bona fide peroxiredoxins but commonly use AhpF or AhpD as primary reductants rather than thioredoxin; GO:0008379 is therefore over-specific for this branch (zhang2019molecularmechanismsof pages 7-9, zhang2019molecularmechanismsof pages 4-5, groot2022thiolreductasesin pages 16-17, wan2021distincth2o2scavengingsystem pages 10-12) |
| Subfamily: Prx5 (atypical 2-Cys) | thioredoxin peroxidase activity | GO:0008379 | PrxV/Prx5 | Prx5/PrxV is thioredoxin-dependent but differs mechanistically from typical 2-Cys enzymes by using an intramolecular disulfide (vaskova2023glutathionerelatedenzymesand pages 10-11, thapa2023theroleof pages 1-2, thapa2023theroleof pages 2-4) |
| Subfamily: Prx6 (1-Cys) | peroxiredoxin activity + phospholipase A2 activity | GO:0051920 + GO:0047714 | PRDX6 | PRDX6 is GSH/GST-dependent rather than thioredoxin-dependent and is multifunctional, also carrying phospholipase A2 and LPCAT-related activities; GO:0008379 would miss this divergence and misstate the reductant (xue2024unveilingthesignificance pages 1-3, thapa2023theroleof pages 2-4, jia2023antioxidantandprooxidant pages 3-4, jia2023antioxidantandprooxidant pages 9-11) |
| Subfamily: Tpx | thioredoxin peroxidase activity | GO:0008379 | Bacterial Tpx | Tpx is a thioredoxin-dependent bacterial peroxiredoxin branch and fits a thioredoxin-specific MF term better than generic AhpC-like branches (perkins2015peroxiredoxinsguardiansagainst pages 2-3, vaskova2023glutathionerelatedenzymesand pages 10-11) |
| Subfamily: PrxQ/BCP | peroxiredoxin activity | GO:0051920 | Plant/bacterial PrxQ | PrxQ/BCP retains the conserved peroxiredoxin catalytic core, but reductant usage is variable enough that a thioredoxin-specific term is not uniformly safe (perkins2015peroxiredoxinsguardiansagainst pages 2-3) |
| Subfamily: AhpE | peroxiredoxin activity | GO:0051920 | Mycobacterial AhpE | AhpE is a bacterial-restricted, non-canonical branch with 1-Cys-like features and non-standard reductant context; a generic peroxiredoxin term is safer than GO:0008379 (perkins2015peroxiredoxinsguardiansagainst pages 2-3, vaskova2023glutathionerelatedenzymesand pages 10-11) |
| Currently propagated term | thioredoxin peroxidase activity | GO:0008379 | Mis-annotates AhpC (SF121), Prx6, PrxQ, AhpE | Over-specific because it asserts thioredoxin as electron donor, which is incorrect or insufficiently supported for multiple peroxiredoxin branches in PTHR10681 (zhang2019molecularmechanismsof pages 7-9, xue2024unveilingthesignificance pages 1-3, perkins2015peroxiredoxinsguardiansagainst pages 2-3, vaskova2023glutathionerelatedenzymesand pages 10-11) |


*Table: This table summarizes suggested molecular function GO terms for family- versus subfamily-level curation of PTHR10681. It highlights where the currently propagated thioredoxin-specific term is likely to over-annotate branches with different reductants or additional activities.*

### Summary of Recommendations

- **Family-level term (PTHR10681 root):** GO:0051920 "peroxiredoxin activity" — this captures the universally conserved cysteine-dependent peroxide reduction without asserting a specific electron donor.

- **Currently propagated term (GO:0008379, "thioredoxin peroxidase activity"):** Should be **restricted** to the eukaryotic typical 2-Cys (Prx1–4), atypical 2-Cys (Prx5), and bacterial Tpx subfamilies where thioredoxin dependency is experimentally established.

- **SF121 (AhpC):** Should receive GO:0051920 "peroxiredoxin activity" rather than GO:0008379. An additional specific term such as "alkyl hydroperoxide reductase activity" would be more precise if available in the ontology.

- **Prx6 branch:** Requires GO:0051920 plus a phospholipase A2 activity term (e.g., GO:0047714 or related) to capture its bifunctional nature. GO:0008379 is incorrect because Prx6 is GSH-dependent, not Trx-dependent (xue2024unveilingthesignificance pages 1-3, thapa2023theroleof pages 2-4).

- **PrxQ/BCP and AhpE branches:** GO:0051920 is safer than GO:0008379 given variable reductant usage (perkins2015peroxiredoxinsguardiansagainst pages 2-3).

---

## Evidence and Gaps

### Key Citations

1. Perkins et al. (2015) *Trends in Biochemical Sciences* 40:435–45. PMID: 26067716. Foundational review defining six Prx subfamilies, catalytic mechanism, and structural classification (perkins2015peroxiredoxinsguardiansagainst pages 2-3).
2. Zhang et al. (2019) *Frontiers in Microbiology* 10:1483. PMID: 31354673. Characterization of *B. thailandensis* AhpC demonstrating AhpD as primary electron donor over TrxC (zhang2019molecularmechanismsof pages 7-9, zhang2019molecularmechanismsof pages 4-5, zhang2019molecularmechanismsof pages 5-7).
3. Wan et al. (2021) *Frontiers in Microbiology* 12:626874. AhpC in *Y. pseudotuberculosis*, demonstrating AhpF-dependent reduction and structural features of AhpC (wan2021distincth2o2scavengingsystem pages 10-12).
4. Vašková et al. (2023) *Molecules* 28:1447. Review categorizing Prx subfamilies and their electron donor systems (vaskova2023glutathionerelatedenzymesand pages 10-11).
5. Thapa et al. (2023) *Biology* 12:666. Mammalian Prx classification with emphasis on electron donor differences between Prx1–4 (Trx), Prx5 (Trx, intramolecular), and Prx6 (GSH) (thapa2023theroleof pages 1-2, thapa2023theroleof pages 2-4).
6. Xue et al. (2024) *Antioxidants* 13:449. Detailed characterization of PRDX6 multifunctional activities: peroxidase, aiPLA2, and LPCAT (xue2024unveilingthesignificance pages 1-3).
7. Lagal et al. (2024) *Biochemical Journal* 481:1997–2015. Functional evidence for PRDX6 iPLA2 activity and its specificity for phosphatidylcholine substrates (lagal2024lossofperoxiredoxin pages 5-6).
8. De Groot et al. (2022) *Antioxidants* 11:561. AhpC in Deinococcus, describing AhpF-AhpC electron transfer and molecular chaperone activity of AhpC (groot2022thiolreductasesin pages 16-17, groot2022thiolreductasesin pages 30-31).
9. Qausain & Basheeruddin (2024) *Cureus* 16:e66117. Comprehensive review of Prx catalytic mechanisms across subfamilies (qausain2024unravelingtheperoxidase pages 1-3).

### Explicit Uncertainties

- **PANTHER tree topology vs. sequence-based Prx classification.** This analysis maps the six recognized Prx evolutionary subfamilies onto PTHR10681, but the PANTHER tree topology and the specific assignment of nodes to SF121 vs. other subfamilies could not be computationally verified (PANTHER's internal tree is not programmatically accessible for this audit). The subfamily boundaries may not perfectly align with the Prx1/Prx5/Prx6/Tpx/PrxQ/AhpE classification.

- **AhpC electron donor plasticity.** Some AhpC proteins can accept electrons from thioredoxin as a secondary pathway (zhang2019molecularmechanismsof pages 7-9, wan2021distincth2o2scavengingsystem pages 10-12). Whether any AhpC proteins in the SF121 subtree use thioredoxin as their *primary* physiological reductant is species-dependent and not universally characterized. This introduces ambiguity in whether GO:0008379 is always wrong for SF121, or merely usually wrong.

- **PrxQ/BCP and AhpE characterization depth.** These subfamilies have fewer characterized members with defined electron donors in the retrieved literature, making GO term assignment less certain.

- **Chaperone and signaling functions.** Several Prx members (particularly Prx1, Prx2, and AhpC) exhibit redox-regulated chaperone or signaling functions upon hyperoxidation or oligomeric switching (groot2022thiolreductasesin pages 16-17). Whether these moonlighting functions warrant separate GO annotations at specific nodes is a curation judgment beyond the scope of this molecular function audit.

- **Q88K52 (*P. putida* AhpC) specifically.** The representative member Q88K52 from *Pseudomonas putida* KT2440 was not individually characterized in the retrieved literature. Its functional assignment is inferred from characterized homologs in closely related Pseudomonad and Gammaproteobacterial species.


References

1. (perkins2015peroxiredoxinsguardiansagainst pages 2-3): Arden Perkins, Kimberly J. Nelson, Derek Parsonage, Leslie B. Poole, and P. Andrew Karplus. Peroxiredoxins: guardians against oxidative stress and modulators of peroxide signaling. Trends in biochemical sciences, 40 8:435-45, Aug 2015. URL: https://doi.org/10.1016/j.tibs.2015.05.001, doi:10.1016/j.tibs.2015.05.001. This article has 780 citations and is from a domain leading peer-reviewed journal.

2. (vaskova2023glutathionerelatedenzymesand pages 10-11): Janka Vašková, Ladislav Kočan, Ladislav Vaško, and Pál Perjési. Glutathione-related enzymes and proteins: a review. Molecules, 28:1447, Feb 2023. URL: https://doi.org/10.3390/molecules28031447, doi:10.3390/molecules28031447. This article has 425 citations.

3. (qausain2024unravelingtheperoxidase pages 1-3): Sana Qausain and Mohd Basheeruddin. Unraveling the peroxidase activity in peroxiredoxins: a comprehensive review of mechanisms, functions, and biological significance. Cureus, Aug 2024. URL: https://doi.org/10.7759/cureus.66117, doi:10.7759/cureus.66117. This article has 17 citations.

4. (xue2024unveilingthesignificance pages 1-3): Min Xue, Xiaojie Huang, Tong Zhu, Lijun Zhang, Hao Yang, Yuxian Shen, and Lijie Feng. Unveiling the significance of peroxiredoxin 6 in central nervous system disorders. Antioxidants, 13:449, Apr 2024. URL: https://doi.org/10.3390/antiox13040449, doi:10.3390/antiox13040449. This article has 25 citations.

5. (zhang2019molecularmechanismsof pages 7-9): Bing Zhang, Huawei Gu, Yantao Yang, Haonan Bai, Chao Zhao, Meiru Si, Tao Su, and Xihui Shen. Molecular mechanisms of ahpc in resistance to oxidative stress in burkholderia thailandensis. Frontiers in Microbiology, Jul 2019. URL: https://doi.org/10.3389/fmicb.2019.01483, doi:10.3389/fmicb.2019.01483. This article has 52 citations and is from a peer-reviewed journal.

6. (zhang2019molecularmechanismsof pages 4-5): Bing Zhang, Huawei Gu, Yantao Yang, Haonan Bai, Chao Zhao, Meiru Si, Tao Su, and Xihui Shen. Molecular mechanisms of ahpc in resistance to oxidative stress in burkholderia thailandensis. Frontiers in Microbiology, Jul 2019. URL: https://doi.org/10.3389/fmicb.2019.01483, doi:10.3389/fmicb.2019.01483. This article has 52 citations and is from a peer-reviewed journal.

7. (thapa2023theroleof pages 2-4): Pratik Thapa, Hong Jiang, Na Ding, Yanning Hao, Aziza Alshahrani, and Qiou Wei. The role of peroxiredoxins in cancer development. Biology, 12:666, Apr 2023. URL: https://doi.org/10.3390/biology12050666, doi:10.3390/biology12050666. This article has 26 citations.

8. (thapa2023theroleof pages 1-2): Pratik Thapa, Hong Jiang, Na Ding, Yanning Hao, Aziza Alshahrani, and Qiou Wei. The role of peroxiredoxins in cancer development. Biology, 12:666, Apr 2023. URL: https://doi.org/10.3390/biology12050666, doi:10.3390/biology12050666. This article has 26 citations.

9. (wan2021distincth2o2scavengingsystem pages 10-12): Fen Wan, Xue Feng, Jianhua Yin, and Haichun Gao. Distinct h2o2-scavenging system in yersinia pseudotuberculosis: katg and ahpc act together to scavenge endogenous hydrogen peroxide. Frontiers in Microbiology, May 2021. URL: https://doi.org/10.3389/fmicb.2021.626874, doi:10.3389/fmicb.2021.626874. This article has 24 citations and is from a peer-reviewed journal.

10. (jia2023antioxidantandprooxidant pages 9-11): Wenhui Jia, Chunling Dong, and Bo Li. Anti-oxidant and pro-oxidant effects of peroxiredoxin 6: a potential target in respiratory diseases. Cells, 12:181, Jan 2023. URL: https://doi.org/10.3390/cells12010181, doi:10.3390/cells12010181. This article has 28 citations.

11. (lagal2024lossofperoxiredoxin pages 5-6): Daniel J. Lagal, Ángel Ortiz-Alcántara, José R. Pedrajas, Brian McDonagh, J. Antonio Bárcena, Raquel Requejo-Aguilar, and C. Alicia Padilla. Loss of peroxiredoxin 6 alters lipid composition and distribution resulting in increased sensitivity to ferroptosis. Biochemical Journal, 481:1997-2015, Dec 2024. URL: https://doi.org/10.1042/bcj20240445, doi:10.1042/bcj20240445. This article has 14 citations and is from a domain leading peer-reviewed journal.

12. (groot2022thiolreductasesin pages 16-17): Arjan de Groot, Laurence Blanchard, Nicolas Rouhier, and Pascal Rey. Thiol reductases in deinococcus bacteria and roles in stress tolerance. Mar 2022. URL: https://doi.org/10.3390/antiox11030561, doi:10.3390/antiox11030561. This article has 9 citations.

13. (groot2022thiolreductasesin pages 30-31): Arjan de Groot, Laurence Blanchard, Nicolas Rouhier, and Pascal Rey. Thiol reductases in deinococcus bacteria and roles in stress tolerance. Mar 2022. URL: https://doi.org/10.3390/antiox11030561, doi:10.3390/antiox11030561. This article has 9 citations.

14. (jia2023antioxidantandprooxidant pages 3-4): Wenhui Jia, Chunling Dong, and Bo Li. Anti-oxidant and pro-oxidant effects of peroxiredoxin 6: a potential target in respiratory diseases. Cells, 12:181, Jan 2023. URL: https://doi.org/10.3390/cells12010181, doi:10.3390/cells12010181. This article has 28 citations.

15. (zhang2019molecularmechanismsof pages 5-7): Bing Zhang, Huawei Gu, Yantao Yang, Haonan Bai, Chao Zhao, Meiru Si, Tao Su, and Xihui Shen. Molecular mechanisms of ahpc in resistance to oxidative stress in burkholderia thailandensis. Frontiers in Microbiology, Jul 2019. URL: https://doi.org/10.3389/fmicb.2019.01483, doi:10.3389/fmicb.2019.01483. This article has 52 citations and is from a peer-reviewed journal.

16. (zhang2019molecularmechanismsof pages 1-2): Bing Zhang, Huawei Gu, Yantao Yang, Haonan Bai, Chao Zhao, Meiru Si, Tao Su, and Xihui Shen. Molecular mechanisms of ahpc in resistance to oxidative stress in burkholderia thailandensis. Frontiers in Microbiology, Jul 2019. URL: https://doi.org/10.3389/fmicb.2019.01483, doi:10.3389/fmicb.2019.01483. This article has 52 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PTHR10681-function-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR10681-function-falcon_artifacts/artifact-01.md)