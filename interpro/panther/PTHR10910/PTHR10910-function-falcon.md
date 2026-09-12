---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-24T04:36:24.155006'
end_time: '2026-06-24T04:56:22.200164'
duration_seconds: 1198.05
template_file: templates/treegrafter_family_function.md
template_variables:
  family_id: PTHR10910
  family_name: EUKARYOTE SPECIFIC DSRNA BINDING PROTEIN
  subfamily: PTHR10910:SF62 AT07585P-RELATED
  gene_symbol: ADAR2
  uniprot: C1JAR3
  organism: DOROP
  taxon_label: DOROP
  propagated_term: tRNA-specific adenosine deaminase activity (GO:0008251)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 29
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PTHR10910-function-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR10910-function-falcon_artifacts/artifact-01.md
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

- **PANTHER family:** PTHR10910 — EUKARYOTE SPECIFIC DSRNA BINDING PROTEIN
- **Subfamily of interest:** PTHR10910:SF62 AT07585P-RELATED
- **Representative member:** ADAR2 (C1JAR3), DOROP / DOROP
- **GO term currently propagated at/near this node:** tRNA-specific adenosine deaminase activity (GO:0008251)

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
3. **Subfamily of interest.** Where does PTHR10910:SF62 AT07585P-RELATED sit — does it carry the
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

- **PANTHER family:** PTHR10910 — EUKARYOTE SPECIFIC DSRNA BINDING PROTEIN
- **Subfamily of interest:** PTHR10910:SF62 AT07585P-RELATED
- **Representative member:** ADAR2 (C1JAR3), DOROP / DOROP
- **GO term currently propagated at/near this node:** tRNA-specific adenosine deaminase activity (GO:0008251)

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
3. **Subfamily of interest.** Where does PTHR10910:SF62 AT07585P-RELATED sit — does it carry the
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


# PANTHER Family PTHR10910 — TreeGrafter Granularity Audit

## Family Function Summary

PANTHER family PTHR10910 ("Eukaryote Specific dsRNA Binding Protein") unites proteins that share a zinc-dependent adenosine deaminase domain of the CDA superfamily, characterised by the signature catalytic motifs H-x-E…PC-x-x-C (H394, E396, C451, C516 in human ADAR2 numbering) that coordinate a catalytic zinc ion and activate a water molecule for hydrolytic deamination of adenosine to inosine in RNA substrates (fisher2024structuralperspectiveson pages 5-6, ashley2024adarfamilyproteins pages 7-8). The catalytic mechanism involves base-flipping: a conserved Gly-Glu-Gly loop (E488 in hADAR2) penetrates the RNA minor groove to flip the target adenosine into the active site pocket (fisher2024structuralperspectiveson pages 5-6, ashley2024adarfamilyproteins pages 7-8). Inositol hexakisphosphate (IP6) serves as an obligate structural cofactor for ADARs and ADAT1, buried within the deaminase domain core (fisher2024structuralperspectiveson pages 5-6). However, the family is **not** functionally homogeneous: it contains (i) catalytically active dsRNA-specific adenosine deaminases (ADAR1, ADAR2, invertebrate ADARs) that edit mRNA/dsRNA, (ii) a catalytically active tRNA-specific adenosine deaminase (ADAT1) that edits tRNA position A37, and (iii) multiple catalytically inactive pseudo-enzymes (ADAR3, ADAD1/TENR, ADAD2) that have lost deaminase activity but retained dsRNA-binding capability (mannion2015newinsightsinto pages 1-4, ashley2024adarfamilyproteins pages 7-8). ADARs evolved from an ADAT1-like ancestor through acquisition of dsRNA-binding domains (dsRBDs) fused to the deaminase domain (keegan2004adenosinedeaminasesacting pages 3-4, savva2012theadarprotein pages 1-2).

## Subfamily Divergence Table

The following table enumerates the major functional subgroups within PTHR10910 and their molecular function divergence:

| Subgroup | Representative Member(s) (with PMID/citation) | Molecular Function | Substrate/Specialization | Catalytic Residues Intact? | Appropriate GO MF Term | Notes (pseudo-enzyme, neofunctionalization, etc.) |
|---|---|---|---|---|---|---|
| ADAR1 (vertebrate) | Human ADAR1/p110, p150; reviewed structurally and functionally in 2022–2024 sources (fisher2024structuralperspectiveson pages 5-6, ashley2024adarfamilyproteins pages 7-8, keegan2004adenosinedeaminasesacting pages 1-2) | Double-stranded RNA-specific adenosine deaminase; A-to-I editing | Long endogenous/viral dsRNA; extensive editing of repetitive dsRNA and innate immune self/non-self discrimination | Yes; catalytic HxE-PCxxC core and IP6-binding cavity conserved (fisher2024structuralperspectiveson pages 5-6, ashley2024adarfamilyproteins pages 7-8) | GO:0003726 double-stranded RNA-specific adenosine deaminase activity | Catalytically active ADAR clade; ADAR1 has Z-domains plus 3 dsRBDs and major innate-immunity role |
| ADAR2 (vertebrate) | Human ADAR2/ADARB1; site-specific editor of GluR/neuronal transcripts (fisher2024structuralperspectiveson pages 5-6, ashley2024adarfamilyproteins pages 7-8, hajji2022adar2enzymesefficient pages 9-10, keegan2004adenosinedeaminasesacting pages 1-2) | Double-stranded RNA-specific adenosine deaminase; site-selective A-to-I editing | Structured pre-mRNAs, especially nervous-system recoding sites | Yes; H394/E396/C451/C516 in hADAR2 define active site (fisher2024structuralperspectiveson pages 5-6, ashley2024adarfamilyproteins pages 7-8) | GO:0003726 double-stranded RNA-specific adenosine deaminase activity | Canonical metazoan recoding editor; 2 dsRBDs + catalytic deaminase domain |
| dADAR / invertebrate ADAR2 orthologs (SF62) | Drosophila dADAR / C1JAR3, sole fly ADAR and ADAR2 ortholog (hajji2022adar2enzymesefficient pages 9-10, palladino2000dadaradrosophila pages 1-2, palladino2000dadaradrosophila pages 10-11, palladino2000dadaradrosophila pages 2-4) | Double-stranded RNA-specific adenosine deaminase; site-specific mRNA A-to-I editing | Nervous-system pre-mRNAs including ion-channel and synaptic transcripts; robust activity on dsRNA in vitro | Yes; deaminase domain and zinc-binding residues conserved, high similarity to ADAR2 (palladino2000dadaradrosophila pages 1-2, palladino2000dadaradrosophila pages 2-4) | GO:0003726 double-stranded RNA-specific adenosine deaminase activity | This is the subfamily of interest (PTHR10910:SF62); propagated tRNA-deaminase term is a clear misannotation |
| ADAR3 (ADARB2) | Human ADAR3/ADARB2 (mannion2015newinsightsinto pages 1-4, ashley2024adarfamilyproteins pages 7-8, keegan2004adenosinedeaminasesacting pages 1-2) | RNA binding / negative regulation of RNA editing rather than catalysis | Brain-enriched dsRNA-binding protein; competes with ADAR1/2 on substrates | No; catalytic inactivity linked to altered residues including A389, V485, Q549, Q733 (ashley2024adarfamilyproteins pages 7-8) | No deaminase MF safe; at most dsRNA binding-related annotation if independently supported | Pseudo-enzyme-like ADAR paralog; inhibits editing and has regulatory roles |
| ADAD1 (TENR) | Mammalian ADAD1/TENR (mannion2015newinsightsinto pages 1-4, keegan2004adenosinedeaminasesacting pages 1-2) | Likely RNA binding, not demonstrated adenosine deaminase activity | Testis-specific ADAR-related protein | No; inactive deaminase domain (mannion2015newinsightsinto pages 1-4) | No adenosine deaminase GO MF should be propagated | ADAR-related pseudo-enzyme; retained dsRBD architecture but lost catalysis |
| ADAD2 (TENRL) | Mammalian ADAD2/TENRL (mannion2015newinsightsinto pages 1-4) | Likely RNA binding, not demonstrated adenosine deaminase activity | Testis-specific ADAR-related protein | No; inactive deaminase domain (mannion2015newinsightsinto pages 1-4) | No adenosine deaminase GO MF should be propagated | ADAR-related pseudo-enzyme; function diverged from catalytic editors |
| ADAT1 | Human/plant ADAT1; Arabidopsis AtTAD1 is a characterized exemplar (keegan2004adenosinedeaminasesacting pages 3-4, keegan2004adenosinedeaminasesacting pages 5-6) | tRNA-specific adenosine deaminase | tRNA-Ala A37→I37, adjacent to anticodon | Yes; active ADAT1 deaminase domain conserved (keegan2004adenosinedeaminasesacting pages 3-4, keegan2004adenosinedeaminasesacting pages 2-3) | GO:0008251 tRNA-specific adenosine deaminase activity | Distinct catalytic branch from ADARs; lacks dsRBDs; only this branch fits the currently propagated GO term |
| C. elegans ADR-1 | C. elegans ADR-1 (savva2012theadarprotein pages 2-4, keegan2004adenosinedeaminasesacting pages 3-4) | dsRNA binding / editing cofactor, not catalytic editing | dsRNA-associated regulator; may function with ADR-2 | No; lacks active-site glutamate (keegan2004adenosinedeaminasesacting pages 3-4) | No deaminase MF safe; dsRNA binding-related term only if supported | Noncatalytic nematode branch; illustrates loss of catalysis within family |
| C. elegans ADR-2 | C. elegans ADR-2 (savva2012theadarprotein pages 2-4, keegan2004adenosinedeaminasesacting pages 3-4) | Double-stranded RNA-specific adenosine deaminase | Catalytic A-to-I editor in nematodes | Yes; catalytic editor paralog in nematodes (keegan2004adenosinedeaminasesacting pages 3-4) | GO:0003726 double-stranded RNA-specific adenosine deaminase activity | Active nematode ADAR-like branch; contrasts with inactive ADR-1 partner |


*Table: This table summarizes the major functional subgroups within PTHR10910, separating catalytically active ADAR/ADAT branches from inactive ADAR-related pseudo-enzymes. It is useful for curating GO granularity because it shows that tRNA-specific adenosine deaminase activity applies to ADAT1, not to the ADAR2-like SF62 branch.*

## Homogeneous vs. Heterogeneous Verdict

> **Verdict: PTHR10910 is functionally HETEROGENEOUS, so no single family-level molecular-function GO term can be safely propagated across all descendants.** The catalytically active branches already split by substrate: ADAR1/ADAR2 and invertebrate ADAR orthologs such as **Drosophila dADAR** catalyze A-to-I editing in **double-stranded RNA / structured pre-mRNA**, whereas **ADAT1** catalyzes A-to-I editing of **tRNA**, specifically the anticodon-adjacent **A37** position (hajji2022adar2enzymesefficient pages 9-10, palladino2000dadaradrosophila pages 1-2, keegan2004adenosinedeaminasesacting pages 3-4). In addition, several branches have lost deaminase activity altogether: **ADAR3 (ADARB2)**, **ADAD1/TENR**, **ADAD2**, and **C. elegans ADR-1** are noncatalytic RNA-binding or regulatory paralogs/pseudo-enzymes, so any deaminase MF propagated to them would be an over-annotation (mannion2015newinsightsinto pages 1-4, ashley2024adarfamilyproteins pages 7-8, keegan2004adenosinedeaminasesacting pages 3-4). Therefore the currently propagated term **GO:0008251 tRNA-specific adenosine deaminase activity** is inappropriate for the ADAR branches and is especially wrong for **PTHR10910:SF62**, whose representative **dADAR/ADAR2-like proteins are definitively dsRNA editors, not tRNA editors** (hajji2022adar2enzymesefficient pages 9-10, palladino2000dadaradrosophila pages 1-2, palladino2000dadaradrosophila pages 2-4).


*Blockquote: This blockquote gives the curator-facing verdict on GO granularity for PTHR10910. It highlights the key reason propagation is unsafe: the family contains dsRNA editors, tRNA editors, and catalytically inactive paralogs.*

The family is **heterogeneous** across at least three functional axes:

1. **Substrate divergence among active deaminases.** ADAR1 and ADAR2 (and their invertebrate orthologs including Drosophila dADAR) catalyse A-to-I editing of double-stranded RNA within structured pre-mRNAs, affecting codons in ion channels, neurotransmitter receptors, and other nervous system transcripts (hajji2022adar2enzymesefficient pages 9-10, keegan2017adarrnaediting pages 1-2). In contrast, ADAT1 catalyses A-to-I editing specifically at position 37 of tRNA-Ala(AGC) (keegan2004adenosinedeaminasesacting pages 3-4, keegan2004adenosinedeaminasesacting pages 5-6). These are distinct molecular functions with distinct GO terms.

2. **Loss of catalysis (pseudo-enzymes).** ADAR3 (ADARB2) retains all structural domains of ADAR2 but is catalytically inactive due to substitutions at four key residues (A389, V485, Q549, Q733) and instead functions as a competitive inhibitor of ADAR1/ADAR2 editing in the brain (zhang2025adarspleiotropyin pages 4-4, ashley2024adarfamilyproteins pages 7-8). ADAD1 (TENR) and ADAD2 are testis-specific paralogs with inactive deaminase domains and no demonstrated enzymatic activity (mannion2015newinsightsinto pages 1-4). C. elegans ADR-1 lacks the active-site glutamate and is catalytically dead (keegan2004adenosinedeaminasesacting pages 3-4).

3. **Domain architecture variation.** ADAT1 lacks dsRBDs entirely (keegan2004adenosinedeaminasesacting pages 3-4, keegan2004adenosinedeaminasesacting pages 1-2). ADAR1 uniquely possesses Z-DNA/Z-RNA binding domains (Zα, Zβ) and three dsRBDs. ADAR2 and ADAR3 have two dsRBDs each, while ADAR3 additionally carries an arginine-rich R domain for ssRNA binding (zhang2025adarspleiotropyin pages 2-4, huebert2025frommetabolismto pages 22-24).

A single family-level GO MF term **cannot** be safely propagated across all descendants of PTHR10910 without mis-annotating multiple branches.

## Subfamily of Interest: PTHR10910:SF62 (AT07585P-RELATED)

The representative member of this subfamily is **Drosophila melanogaster dADAR** (UniProt: C1JAR3; gene identifier AT07585P). dADAR is the sole ADAR gene in *Drosophila*, structurally and functionally orthologous to vertebrate ADAR2 (ADARB1) (palladino2000dadaradrosophila pages 1-2, palladino2000dadaradrosophila pages 2-4). It contains two dsRNA-binding motifs and a catalytic deaminase domain with all zinc-coordinating and catalytic residues conserved, and shows 67% amino acid identity to human ADAR2 in the catalytic domain (palladino2000dadaradrosophila pages 1-2, palladino2000dadaradrosophila pages 2-4).

dADAR has been experimentally demonstrated to possess **robust dsRNA-specific adenosine deaminase activity**: recombinant dADAR expressed in *Pichia pastoris* efficiently converts adenosine to inosine in synthetic dsRNA substrates (palladino2000dadaradrosophila pages 1-2, palladino2000dadaradrosophila pages 10-11). In vivo, dADAR site-specifically edits hundreds of pre-mRNA transcripts encoding ion channel subunits, neurotransmitter receptors, and synaptic proteins in the nervous system (hajji2022adar2enzymesefficient pages 9-10, keegan2017adarrnaediting pages 1-2, savva2012theadarprotein pages 2-4). Comparison with the tRNA-specific deaminase dADAT1 showed only 17% overall identity and 28% identity in the catalytic domain, confirming that dADAR is functionally distinct from tRNA deaminases (palladino2000dadaradrosophila pages 2-4).

**The currently propagated GO term GO:0008251 (tRNA-specific adenosine deaminase activity) is incorrect for this subfamily.** dADAR/ADAR2 orthologs have no demonstrated activity on tRNA; their substrate is structured pre-mRNA/dsRNA. The appropriate GO term for SF62 is **GO:0003726 (double-stranded RNA-specific adenosine deaminase activity)**.

## Granularity Leads for Curation

**Family-level recommendation:** No single molecular function GO term is safe to propagate across the entire PTHR10910 family. The broadest accurate ancestor-level annotation that applies to catalytically active members would be **adenosine deaminase activity, acting on RNA (a parent of both GO:0003726 and GO:0008251)**, but even this would over-annotate the catalytically inactive ADAR3, ADAD1, ADAD2, and C. elegans ADR-1 branches. If a term must be placed at the family root, it should be restricted to the structural/binding feature shared by all members—however, "protein binding" or "RNA binding" is too uninformative.

**Subfamily-level recommendations:**

| Subfamily clade | Recommended GO MF term |
|---|---|
| ADAR1 orthologs | GO:0003726 double-stranded RNA-specific adenosine deaminase activity |
| ADAR2 orthologs (including SF62 / dADAR) | GO:0003726 double-stranded RNA-specific adenosine deaminase activity |
| ADAR3 (ADARB2) orthologs | No deaminase term; dsRNA binding if independently supported |
| ADAD1 / ADAD2 | No deaminase term |
| ADAT1 orthologs | GO:0008251 tRNA-specific adenosine deaminase activity |
| C. elegans ADR-1 | No deaminase term |
| C. elegans ADR-2 | GO:0003726 double-stranded RNA-specific adenosine deaminase activity |

**Subfamilies for which the currently propagated term (GO:0008251) is an over-annotation:**
- **PTHR10910:SF62 (AT07585P-RELATED / dADAR / ADAR2 orthologs)** — these are dsRNA editors, not tRNA editors; this is the clearest mis-annotation.
- **All ADAR1 and ADAR2 vertebrate subfamilies** — dsRNA editors, not tRNA editors.
- **ADAR3, ADAD1, ADAD2** — catalytically inactive; any deaminase term is incorrect.
- **C. elegans ADR-1** — catalytically inactive.

**The only subfamily for which GO:0008251 is correct is the ADAT1 clade**, which edits adenosine at position 37 in tRNA-Ala.

## Evidence and Gaps

**Key citations:**
- Keegan et al., *Genome Biology* 2004; 5:209 (PMID: 14759252) — foundational ADAR family review establishing evolutionary relationship from ADAT1 to ADARs and domain architecture (keegan2004adenosinedeaminasesacting pages 6-7, keegan2004adenosinedeaminasesacting pages 5-6, keegan2004adenosinedeaminasesacting pages 3-4, keegan2004adenosinedeaminasesacting pages 1-2).
- Palladino et al., *RNA* 2000; 6:1004–1018 (PMID: 10917599) — cloning and characterisation of Drosophila dADAR, demonstrating dsRNA-specific activity (palladino2000dadaradrosophila pages 1-2, palladino2000dadaradrosophila pages 10-11, palladino2000dadaradrosophila pages 2-4).
- Fisher & Beal, *Mol. Ther. Nucleic Acids* 2024; 35:102284 — structural perspectives on ADAR catalytic mechanism including IP6 requirement and base-flipping (fisher2024structuralperspectiveson pages 5-6).
- Ashley et al., *Curr. Issues Mol. Biol.* 2024; 46:3919–3945 — structural review of ADAR family proteins including ADAR3 inactivating mutations (ashley2024adarfamilyproteins pages 7-8, ashley2024adarfamilyproteins pages 4-7).
- Mannion et al., *Biomolecules* 2015; 5:2338–2362 — characterisation of ADAR3, ADAD1, ADAD2 as catalytically inactive family members (mannion2015newinsightsinto pages 1-4).
- Hajji et al., *RNA* 2022; 28:1281–1297 — comprehensive review of ADAR2 function and Drosophila editing sites (hajji2022adar2enzymesefficient pages 9-10).
- Savva et al., *Genome Biology* 2012; 13:252 — ADAR protein family review (savva2012theadarprotein pages 1-2, savva2012theadarprotein pages 2-4).
- Keegan et al., *RNA* 2017; 23:1317–1328 — Drosophila ADAR editing sites and mechanisms (keegan2017adarrnaediting pages 3-5, keegan2017adarrnaediting pages 1-2).
- Zhang et al., *Nucleic Acids Res.* 2025 — ADAR3 as catalytically inactive competitive inhibitor (zhang2025adarspleiotropyin pages 4-4, zhang2025adarspleiotropyin pages 2-4).
- Dolce et al., *Nature Commun.* 2022 — cryo-EM structure of eukaryotic ADAT2/3-tRNA complex (relevant for distinguishing ADAT2/3 from ADAT1 and ADARs).

**Explicit uncertainties:**
1. **PANTHER tree composition.** The exact set of proteins grouped under PTHR10910 could not be verified programmatically (PANTHER web API was not accessible). The analysis assumes the family encompasses the ADAT1-ADAR clade based on the family name, representative member, and phylogenetic trees in the literature. If ADAT2/ADAT3 are also included in this family, the heterogeneity is even greater.
2. **ADAD1/ADAD2 function.** The biological roles of the testis-specific ADAD proteins remain poorly characterised; they are inferred to be pseudo-enzymes based on catalytic residue divergence, but their RNA-binding targets and regulatory roles are largely unknown.
3. **C. elegans ADR-1/ADR-2 classification.** The nematode ADAR genes are divergent and difficult to assign to specific vertebrate ADAR1/ADAR2 orthologs (keegan2004adenosinedeaminasesacting pages 3-4); their placement in PTHR10910 subfamilies needs verification.
4. **Subfamily SF62 membership.** Whether SF62 includes only invertebrate ADAR2 orthologs or also vertebrate ADAR2 proteins could not be confirmed from the PANTHER database directly. The functional conclusion (dsRNA editing, not tRNA editing) applies regardless.


References

1. (fisher2024structuralperspectiveson pages 5-6): Andrew J. Fisher and Peter A. Beal. Structural perspectives on adenosine to inosine rna editing by adars. Molecular Therapy - Nucleic Acids, 35:102284, Sep 2024. URL: https://doi.org/10.1016/j.omtn.2024.102284, doi:10.1016/j.omtn.2024.102284. This article has 22 citations.

2. (ashley2024adarfamilyproteins pages 7-8): Carolyn N. Ashley, Emmanuel Broni, and Whelton A. Miller. Adar family proteins: a structural review. Current Issues in Molecular Biology, 46:3919-3945, Apr 2024. URL: https://doi.org/10.3390/cimb46050243, doi:10.3390/cimb46050243. This article has 29 citations.

3. (mannion2015newinsightsinto pages 1-4): Niamh Mannion, Fabiana Arieti, Angela Gallo, Liam Keegan, and Mary O'Connell. New insights into the biological role of mammalian adars; the rna editing proteins. Biomolecules, 5:2338-2362, Sep 2015. URL: https://doi.org/10.3390/biom5042338, doi:10.3390/biom5042338. This article has 94 citations.

4. (keegan2004adenosinedeaminasesacting pages 3-4): Liam P Keegan, Anne Leroy, Duncan Sproul, and Mary A O'Connell. Adenosine deaminases acting on rna (adars): rna-editing enzymes. Genome Biology, 5:209-209, Feb 2004. URL: https://doi.org/10.1186/gb-2004-5-2-209, doi:10.1186/gb-2004-5-2-209. This article has 208 citations and is from a highest quality peer-reviewed journal.

5. (savva2012theadarprotein pages 1-2): Yiannis A Savva, Leila E Rieder, and Robert A Reenan. The adar protein family. Genome Biology, 13:252-252, Dec 2012. URL: https://doi.org/10.1186/gb-2012-13-12-252, doi:10.1186/gb-2012-13-12-252. This article has 435 citations and is from a highest quality peer-reviewed journal.

6. (keegan2004adenosinedeaminasesacting pages 1-2): Liam P Keegan, Anne Leroy, Duncan Sproul, and Mary A O'Connell. Adenosine deaminases acting on rna (adars): rna-editing enzymes. Genome Biology, 5:209-209, Feb 2004. URL: https://doi.org/10.1186/gb-2004-5-2-209, doi:10.1186/gb-2004-5-2-209. This article has 208 citations and is from a highest quality peer-reviewed journal.

7. (hajji2022adar2enzymesefficient pages 9-10): Khadija Hajji, Jiří Sedmík, Anna Cherian, Damiano Amoruso, Liam P. Keegan, and Mary A. O'Connell. Adar2 enzymes: efficient site-specific rna editors with gene therapy aspirations. RNA, 28:1281-1297, Jul 2022. URL: https://doi.org/10.1261/rna.079266.122, doi:10.1261/rna.079266.122. This article has 29 citations and is from a domain leading peer-reviewed journal.

8. (palladino2000dadaradrosophila pages 1-2): MICHAEL J. PALLADINO, LIAM P. KEEGAN, MARY A. O'CONNELL, and ROBERT A. REENAN. Dadar, a drosophila double-stranded rna-specific adenosine deaminase is highly developmentally regulated and is itself a target for rna editing. RNA, 6 7:1004-18, Jul 2000. URL: https://doi.org/10.1017/s1355838200000248, doi:10.1017/s1355838200000248. This article has 243 citations and is from a domain leading peer-reviewed journal.

9. (palladino2000dadaradrosophila pages 10-11): MICHAEL J. PALLADINO, LIAM P. KEEGAN, MARY A. O'CONNELL, and ROBERT A. REENAN. Dadar, a drosophila double-stranded rna-specific adenosine deaminase is highly developmentally regulated and is itself a target for rna editing. RNA, 6 7:1004-18, Jul 2000. URL: https://doi.org/10.1017/s1355838200000248, doi:10.1017/s1355838200000248. This article has 243 citations and is from a domain leading peer-reviewed journal.

10. (palladino2000dadaradrosophila pages 2-4): MICHAEL J. PALLADINO, LIAM P. KEEGAN, MARY A. O'CONNELL, and ROBERT A. REENAN. Dadar, a drosophila double-stranded rna-specific adenosine deaminase is highly developmentally regulated and is itself a target for rna editing. RNA, 6 7:1004-18, Jul 2000. URL: https://doi.org/10.1017/s1355838200000248, doi:10.1017/s1355838200000248. This article has 243 citations and is from a domain leading peer-reviewed journal.

11. (keegan2004adenosinedeaminasesacting pages 5-6): Liam P Keegan, Anne Leroy, Duncan Sproul, and Mary A O'Connell. Adenosine deaminases acting on rna (adars): rna-editing enzymes. Genome Biology, 5:209-209, Feb 2004. URL: https://doi.org/10.1186/gb-2004-5-2-209, doi:10.1186/gb-2004-5-2-209. This article has 208 citations and is from a highest quality peer-reviewed journal.

12. (keegan2004adenosinedeaminasesacting pages 2-3): Liam P Keegan, Anne Leroy, Duncan Sproul, and Mary A O'Connell. Adenosine deaminases acting on rna (adars): rna-editing enzymes. Genome Biology, 5:209-209, Feb 2004. URL: https://doi.org/10.1186/gb-2004-5-2-209, doi:10.1186/gb-2004-5-2-209. This article has 208 citations and is from a highest quality peer-reviewed journal.

13. (savva2012theadarprotein pages 2-4): Yiannis A Savva, Leila E Rieder, and Robert A Reenan. The adar protein family. Genome Biology, 13:252-252, Dec 2012. URL: https://doi.org/10.1186/gb-2012-13-12-252, doi:10.1186/gb-2012-13-12-252. This article has 435 citations and is from a highest quality peer-reviewed journal.

14. (keegan2017adarrnaediting pages 1-2): Liam Keegan, Anzer Khan, Dragana Vukic, and Mary O'Connell. Adar rna editing below the backbone. RNA, 23:1317-1328, May 2017. URL: https://doi.org/10.1261/rna.060921.117, doi:10.1261/rna.060921.117. This article has 28 citations and is from a domain leading peer-reviewed journal.

15. (zhang2025adarspleiotropyin pages 4-4): Yifan Zhang, Jack Bryant, Laura Herron, and Prashant Mali. Adars: pleiotropy in function, versatility in application. Nucleic Acids Research, Jul 2025. URL: https://doi.org/10.1093/nar/gkaf672, doi:10.1093/nar/gkaf672. This article has 6 citations and is from a highest quality peer-reviewed journal.

16. (zhang2025adarspleiotropyin pages 2-4): Yifan Zhang, Jack Bryant, Laura Herron, and Prashant Mali. Adars: pleiotropy in function, versatility in application. Nucleic Acids Research, Jul 2025. URL: https://doi.org/10.1093/nar/gkaf672, doi:10.1093/nar/gkaf672. This article has 6 citations and is from a highest quality peer-reviewed journal.

17. (huebert2025frommetabolismto pages 22-24): David Huebert and Mani Larijani. From metabolism to mutation: the multifaceted roles of deaminases in biological systems. Unknown journal, Oct 2025. URL: https://doi.org/10.20944/preprints202510.0048.v1, doi:10.20944/preprints202510.0048.v1.

18. (keegan2004adenosinedeaminasesacting pages 6-7): Liam P Keegan, Anne Leroy, Duncan Sproul, and Mary A O'Connell. Adenosine deaminases acting on rna (adars): rna-editing enzymes. Genome Biology, 5:209-209, Feb 2004. URL: https://doi.org/10.1186/gb-2004-5-2-209, doi:10.1186/gb-2004-5-2-209. This article has 208 citations and is from a highest quality peer-reviewed journal.

19. (ashley2024adarfamilyproteins pages 4-7): Carolyn N. Ashley, Emmanuel Broni, and Whelton A. Miller. Adar family proteins: a structural review. Current Issues in Molecular Biology, 46:3919-3945, Apr 2024. URL: https://doi.org/10.3390/cimb46050243, doi:10.3390/cimb46050243. This article has 29 citations.

20. (keegan2017adarrnaediting pages 3-5): Liam Keegan, Anzer Khan, Dragana Vukic, and Mary O'Connell. Adar rna editing below the backbone. RNA, 23:1317-1328, May 2017. URL: https://doi.org/10.1261/rna.060921.117, doi:10.1261/rna.060921.117. This article has 28 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PTHR10910-function-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR10910-function-falcon_artifacts/artifact-01.md)