---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-15T07:02:06.336805'
end_time: '2026-07-15T07:19:54.987516'
duration_seconds: 1068.65
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Catechol ortho-cleavage branch of the beta-ketoadipate pathway
  module_summary: A reusable bacterial aromatic-catabolism module for the catechol
    ortho-cleavage branch that converts catechol to beta-ketoadipate enol-lactone.
    The branch begins with intradiol cleavage of catechol to cis,cis-muconate by a
    CatA-like catechol 1,2-dioxygenase, followed by CatB-like muconate cycloisomerase
    and CatC-like muconolactone delta-isomerase steps. In Pseudomonas putida KT2440,
    CatA-I/PP_3713 and CatA-II/PP_3166 provide paralogous catechol 1,2-dioxygenase
    exemplars, CatB/PP_3715 supplies the muconate cycloisomerase step, and CatC/PP_3714
    supplies the isomerase step. The module starts at catechol, the output of upstream
    aromatic upper pathways such as BenABCD benzoate degradation, and stops before
    the shared lower beta-ketoadipate reactions that convert the enol-lactone toward
    central metabolism.
  module_outline: "- Catechol ortho-cleavage branch\n  - 1. catechol intradiol ring\
    \ cleavage\n  - CatA catechol 1,2-dioxygenation\n    - Catechol 1,2-dioxygenase\
    \ (molecular player: catechol 1,2-dioxygenase family; activity or role: catechol\
    \ 1,2-dioxygenase activity)\n  - 2. cis,cis-muconate lactonization\n  - CatB muconate\
    \ cycloisomerization\n    - Muconate cycloisomerase (molecular player: muconate\
    \ cycloisomerase family; activity or role: muconate cycloisomerase activity)\n\
    \  - 3. muconolactone isomerization\n  - CatC muconolactone delta-isomerization\n\
    \    - Muconolactone delta-isomerase (molecular player: muconolactone delta-isomerase\
    \ family; activity or role: muconolactone delta-isomerase activity)"
  module_connections: '- CatA catechol 1,2-dioxygenation precedes CatB muconate cycloisomerization:
    The CatA product cis,cis-muconate is the substrate for CatB.

    - CatB muconate cycloisomerization precedes CatC muconolactone delta-isomerization:
    The CatB product muconolactone is the substrate for CatC.'
  pathway_query: ppu00361
  pathway_id: ppu00361
  pathway_name: Chlorocyclohexane and chlorobenzene degradation
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00361 with 3 primary genes; module
    area: aromatic_and_xenobiotic_catabolism.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '3'
  candidate_genes: '- catA-II: PP_3166 | Q88I35 | catechol 1,2-dioxygenase (EC 1.13.11.1)
    (EC 1.13.11.1; primary bucket kegg:ppu00361)

    - catA-I: PP_3713 | Q88GK8 | catechol 1,2-dioxygenase (EC 1.13.11.1) (EC 1.13.11.1;
    primary bucket kegg:ppu00361)

    - catB: PP_3715 | Q88GK6 | Muconate cycloisomerase 1 (EC 5.5.1.1) (EC 5.5.1.1;
    primary bucket kegg:ppu00361)'
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 7
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__catechol_ortho_cleavage__ppu00361-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__catechol_ortho_cleavage__ppu00361-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Catechol ortho-cleavage branch of the beta-ketoadipate pathway in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00361
- Resolved ID: ppu00361
- Resolved name: Chlorocyclohexane and chlorobenzene degradation
- Source: KEGG

Resolved local bucket kegg:ppu00361 with 3 primary genes; module area: aromatic_and_xenobiotic_catabolism.

## Candidate Genes From Local Metadata

Candidate gene count: 3

- catA-II: PP_3166 | Q88I35 | catechol 1,2-dioxygenase (EC 1.13.11.1) (EC 1.13.11.1; primary bucket kegg:ppu00361)
- catA-I: PP_3713 | Q88GK8 | catechol 1,2-dioxygenase (EC 1.13.11.1) (EC 1.13.11.1; primary bucket kegg:ppu00361)
- catB: PP_3715 | Q88GK6 | Muconate cycloisomerase 1 (EC 5.5.1.1) (EC 5.5.1.1; primary bucket kegg:ppu00361)

## Generic Module Context

### Working Scope

A reusable bacterial aromatic-catabolism module for the catechol ortho-cleavage branch that converts catechol to beta-ketoadipate enol-lactone. The branch begins with intradiol cleavage of catechol to cis,cis-muconate by a CatA-like catechol 1,2-dioxygenase, followed by CatB-like muconate cycloisomerase and CatC-like muconolactone delta-isomerase steps. In Pseudomonas putida KT2440, CatA-I/PP_3713 and CatA-II/PP_3166 provide paralogous catechol 1,2-dioxygenase exemplars, CatB/PP_3715 supplies the muconate cycloisomerase step, and CatC/PP_3714 supplies the isomerase step. The module starts at catechol, the output of upstream aromatic upper pathways such as BenABCD benzoate degradation, and stops before the shared lower beta-ketoadipate reactions that convert the enol-lactone toward central metabolism.

### Provisional Biological Outline

- Catechol ortho-cleavage branch
  - 1. catechol intradiol ring cleavage
  - CatA catechol 1,2-dioxygenation
    - Catechol 1,2-dioxygenase (molecular player: catechol 1,2-dioxygenase family; activity or role: catechol 1,2-dioxygenase activity)
  - 2. cis,cis-muconate lactonization
  - CatB muconate cycloisomerization
    - Muconate cycloisomerase (molecular player: muconate cycloisomerase family; activity or role: muconate cycloisomerase activity)
  - 3. muconolactone isomerization
  - CatC muconolactone delta-isomerization
    - Muconolactone delta-isomerase (molecular player: muconolactone delta-isomerase family; activity or role: muconolactone delta-isomerase activity)

### Known Relationships Among Steps

- CatA catechol 1,2-dioxygenation precedes CatB muconate cycloisomerization: The CatA product cis,cis-muconate is the substrate for CatB.
- CatB muconate cycloisomerization precedes CatC muconolactone delta-isomerization: The CatB product muconolactone is the substrate for CatC.

## Assignment

Write a species-aware review of this module/pathway in the target organism. The
goal is not a generic pathway essay; the goal is to support manual module
satisfiability and gene annotation curation.

Treat the candidate gene list as a starting point, not ground truth. Use the
literature and authoritative resources to decide whether each expected pathway
step is present, absent, ambiguous, replaced by a lineage-specific alternative,
or represented by a likely over-propagated annotation.

Prioritize direct evidence from the target species/strain. When using evidence
from related organisms, state the organism and explain whether transfer to the
target taxon is strong, weak, or uncertain. Distinguish *Pseudomonas putida*
KT2440 evidence from broader *Pseudomonas* or generic bacterial evidence.

## Questions To Address

1. **Pathway boundaries**
   - What exact biochemical or cellular process is included?
   - Which neighboring pathways or broad overview maps should be kept separate?
   - Are there alternate names or database-specific definitions for this pathway?

2. **Satisfiability in the target taxon**
   - Which expected steps are encoded by candidate genes?
   - Which steps are missing from the metadata but likely present under a
     different gene name, paralog, or enzyme family?
   - Which steps are probably not expected in this organism?

3. **Candidate gene assessment**
   - For each high-confidence gene, summarize the likely role, evidence type,
     and any curation-relevant caveats.
   - Identify paralog ambiguity, broad EC/GO mappings, and likely annotation
     over-propagation.
   - Note genes that should be promoted to full `fetch-gene` review.

4. **Module implications**
   - What module steps should be marked covered, candidate_uncertain, gap,
     not_expected_in_target_taxon, or module_needs_revision?
   - Are existing generic module boundaries wrong for this organism?
   - Are new module documents or GO term requests likely needed?

5. **Evidence and open questions**
   - Which conclusions are supported by direct experiments?
   - Which are inferred from homology, pathway databases, or neighboring genes?
   - What experiments or expert questions would resolve the important gaps?

## Output Format

Use concise review sections:

1. Executive summary
2. Target-organism pathway definition
3. Expected step model
4. Candidate genes and evidence
5. Gaps, ambiguities, and likely over-annotations
6. Module and GO-curation recommendations
7. Genes to promote to full review
8. Key references

Include citations for major claims, preferably PMIDs or DOIs. Be explicit about
uncertainty, species transfer, and whether evidence is direct for the target
organism.

## Output

# Module/Pathway/Taxon Review: Catechol *ortho*-Cleavage Branch of the β-Ketoadipate Pathway in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (organism code PSEPK; NCBI taxon 160488; proteome UP000000556)
**Pathway bucket queried:** `kegg:ppu00361` (resolved KEGG name: "Chlorocyclohexane and chlorobenzene degradation")
**Module area:** aromatic_and_xenobiotic_catabolism
**Candidate genes supplied:** 3 (catA-II/PP_3166, catA-I/PP_3713, catB/PP_3715)

---

## 1. Executive Summary

The catechol *ortho*-cleavage (intradiol) branch of the β-ketoadipate pathway is **fully satisfiable** in *Pseudomonas putida* KT2440. All three enzymatic steps of the working module — catechol 1,2-dioxygenation, muconate cycloisomerization, and muconolactone δ-isomerization — are encoded and specifically annotated in the KT2440 proteome. Contrary to the supplied 3-gene candidate list, there is **no true pathway gap**: the apparent absence of the third step (muconolactone δ-isomerase) is an artifact of how the candidate list was built from a single KEGG pathway bucket.

The single most important curation action is to **add CatC/PP_3714 (UniProt Q88GK7, EC 5.3.3.4, KO K03464) to the module**. This gene encodes the muconolactone δ-isomerase (step 3) and sits in the canonical *cat* operon immediately adjacent to catA-I and catB, but it was omitted because KEGG assigns PP_3714 to pathway map `ppu00362` (Benzoate degradation) rather than to `ppu00361`, the bucket the candidate list was drawn from. Once CatC is added, every step of the module is covered by a specific, high-quality annotation.

Two secondary recommendations follow. First, the bucket label should be corrected: `ppu00361` resolves to KEGG's "Chlorocyclohexane and chlorobenzene degradation," but the KT2440 genes it captures actually encode the generic **catechol *ortho*-cleavage branch of the β-ketoadipate pathway** (KEGG module M00568). KT2440 has no chlorocatechol (*clcABD*) or *meta*-cleavage (catechol 2,3-dioxygenase, EC 1.13.11.2) enzymes, so the "chlorobenzene degradation" framing is misleading for this organism. Second, curation should record that catechol 1,2-dioxygenase is present as **two genuine paralogs** (catA-I/PP_3713 and catA-II/PP_3166, 76.7% amino-acid identity) in two distinct genomic contexts — the *cat* operon and the benzoate (*ben*) gene cluster, respectively. Evidence for the pathway is **direct at the genomic and transcriptomic level for KT2440** but **homology-only at the enzyme level** for these specific loci; the differential physiological roles of the two CatA paralogs remain the principal open question.

---

## 2. Target-Organism Pathway Definition

**What the module includes.** The catechol *ortho*-cleavage branch is the intradiol route that converts **catechol → *cis,cis*-muconate → (+)-muconolactone → β-ketoadipate enol-lactone** (5-oxo-4,5-dihydro-2-furylacetate). It is the point at which several "upper" aromatic pathways (e.g., benzoate degradation via BenABCD, phenol degradation, anthranilate degradation) funnel into central metabolism. The three enzymatic steps of the working module are:

| Step | Reaction | EC | Enzyme family |
|------|----------|----|--------------|
| 1 | catechol + O₂ → *cis,cis*-muconate + 2 H⁺ | 1.13.11.1 | catechol 1,2-dioxygenase (intradiol dioxygenase) |
| 2 | *cis,cis*-muconate → (+)-muconolactone | 5.5.1.1 | muconate cycloisomerase (enolase superfamily) |
| 3 | (S)-muconolactone → β-ketoadipate enol-lactone | 5.3.3.4 | muconolactone δ-isomerase |

The module **starts at catechol** (the output of upstream upper pathways) and **stops before the shared lower β-ketoadipate reactions** that convert the enol-lactone toward 3-oxoadipate and, ultimately, succinyl-CoA + acetyl-CoA.

**Neighboring pathways that must be kept separate.**

- **The *meta* (extradiol) cleavage route.** Catechol 2,3-dioxygenase (EC 1.13.11.2, metapyrocatechase) cleaves catechol extradiol to 2-hydroxymuconate semialdehyde. This enzyme is structurally distinct from the intradiol dioxygenases [PMID: 10368270] and is **absent from KT2440** (zero EC 1.13.11.2 proteins in the proteome census). The *ortho* module must not be conflated with the *meta* route.
- **The protocatechuate (*pca*) branch.** Protocatechuate 3,4-dioxygenase (EC 1.13.11.3) initiates a parallel intradiol branch that only converges with the catechol branch at the shared lower β-ketoadipate enol-lactone steps. It is a separate module.
- **The downstream shared β-ketoadipate reactions** (enol-lactone hydrolase, β-ketoadipate:succinyl-CoA transferase, thiolase) lie just past the module boundary and should be modeled separately.
- **Broad KEGG overview maps** (ppu01100, ppu01120, ppu01220) aggregate many pathways and should not be used to define module membership.

**Alternate names / database definitions.** This module appears under several labels: "catechol branch of the β-ketoadipate pathway," "catechol *ortho*-cleavage pathway," and — as here — inside broader KEGG xenobiotic-degradation maps. The canonical KEGG module is **M00568 "Catechol *ortho*-cleavage, catechol ⇒ 3-oxoadipate,"** which extends one step further (to 3-oxoadipate) than the working module boundary. The UniProt pathway string for the KT2440 enzymes is *"beta-ketoadipate pathway; 5-oxo-4,5-dihydro-2-furylacetate from catechol."*

---

## 3. Expected Step Model

```
   Upper pathways (benzoate/BenABCD, phenol, anthranilate, IAA ...)
                              │
                              ▼
                          catechol
                              │   O2
        ┌─────────────────────┴──────────────────────┐
   STEP 1: catechol 1,2-dioxygenase (EC 1.13.11.1)   │  INTRADIOL / ortho
        │   CatA-I / PP_3713 (cat operon)             │
        │   CatA-II / PP_3166 (ben cluster)           │
        ▼                                             │
     cis,cis-muconate                                 │
        │                                             │
   STEP 2: muconate cycloisomerase (EC 5.5.1.1)       │
        │   CatB / PP_3715 (cat operon)               │
        ▼                                             │
     (+)-muconolactone                                │
        │                                             │
   STEP 3: muconolactone δ-isomerase (EC 5.3.3.4)     │
        │   CatC / PP_3714 (cat operon)  ◄── MISSING FROM CANDIDATE LIST
        ▼                                             │
   β-ketoadipate enol-lactone  ── MODULE BOUNDARY ────┘
        │
        ▼   (shared lower β-ketoadipate reactions; e.g. PcaD, PP_1380/EC 3.1.1.24)
     3-oxoadipate → central metabolism
```

**Regulation.** The *cat* operon in KT2440 is `PP_3713 (catA-I) – PP_3714 (catC) – PP_3715 (catB) – PP_3716 (catR)`, where CatR is a LysR-family transcriptional regulator. KT2440 **retains catR** (PP_3716), a curation-relevant point because some other *Pseudomonas* (e.g., *P. stutzeri* A1501) lack *catR* [PMID: 20137101].

---

## 4. Candidate Genes and Evidence

### 4.1 CatA-I / PP_3713 (Q88GK8) — catechol 1,2-dioxygenase (Step 1)
- **Role:** Intradiol cleavage of catechol to *cis,cis*-muconate. 311 aa. UniProt reaction: catechol + O₂ = *cis,cis*-muconate + 2 H⁺; annotated as β-ketoadipate pathway step 1/3.
- **Genomic context:** Core member of the canonical *cat* operon (`catA-I–catC–catB–catR`), the strongest possible circumstantial evidence for a bona fide catechol-branch role.
- **Family assignment:** Specific, not generic — Pfam PF00775 (intradiol dioxygenase) + PF04444; InterPro IPR012801 ("Catechol 1,2-dioxygenase"); PROSITE PS00083.
- **Evidence type:** Direct genomic definition of the *cat* branch in KT2440 [PMID: 12534466]; transcriptomic co-induction with *pca* genes during aromatic catabolism [PMID: 17675379]. Enzyme-level (kinetic/structural) evidence for this specific locus is **absent** (UniProt protein-existence level 3, inferred from homology).
- **Caveat:** Paralog ambiguity with CatA-II (see 4.2). The differential in-vivo contribution of catA-I vs catA-II is unresolved.

### 4.2 CatA-II / PP_3166 (Q88I35) — catechol 1,2-dioxygenase (Step 1, paralog)
- **Role:** Second catechol 1,2-dioxygenase. 304 aa; same UniProt reaction and family assignment (IPR012801) as CatA-I.
- **Genomic context:** Embedded in the **benzoate (*ben*) gene cluster**: `PP_3163 (benC) – PP_3164 (benD) – PP_3165 (benK) – PP_3166 (catA-II) – PP_3167 (benE-II)`. This location suggests catA-II may be dedicated to catechol produced during benzoate degradation.
- **Paralog relationship:** Global Needleman–Wunsch alignment against CatA-I gives 240/313 identical columns = **76.7% identity** — homologous but genuinely distinct, i.e., a real duplication rather than a redundant database record.
- **Evidence type:** Homology-only at the enzyme level (protein-existence level 3). No kinetic data for this locus.
- **Caveat:** This is the reason the candidate bucket lists *two* catA genes; both are valid but only one (catA-I) is operonically linked to catB/catC.

### 4.3 CatB / PP_3715 (Q88GK6) — muconate cycloisomerase (Step 2)
- **Role:** Lactonization of *cis,cis*-muconate to (+)-muconolactone. 373 aa; EC 5.5.1.1; KO K01856.
- **Family:** Enolase-superfamily muconate cycloisomerase domains (Pfam PF02746 + PF13378; InterPro IPR013370). Single copy in the proteome.
- **Genomic context:** *cat* operon.
- **Evidence type:** Genomic/transcriptomic (direct for KT2440); enzyme-level homology-only.

### 4.4 CatC / PP_3714 (Q88GK7) — muconolactone δ-isomerase (Step 3) — **NOT in candidate list**
- **Role:** Isomerization of (S)-muconolactone to β-ketoadipate enol-lactone. 96 aa; EC 5.3.3.4; KO K03464. UniProt reaction: (S)-muconolactone = (4,5-dihydro-5-oxofuran-2-yl)-acetate; annotated as β-ketoadipate pathway step 3/3.
- **Family:** Specific muconolactone δ-isomerase family (Pfam PF02426; InterPro IPR003464). Single copy in the proteome.
- **Genomic context:** *cat* operon, between catA-I and catB.
- **Why it was missing:** KEGG assigns PP_3714 to pathway maps **ppu00362** (Benzoate degradation), ppu01100, ppu01120, ppu01220 — but **not** to ppu00361. The candidate list was built from ppu00361 membership, which is exactly `{PP_3166, PP_3713, PP_3715}`. This is a KEGG-map partitioning artifact, not a biological gap.
- **Recommendation:** **Promote to full review and add to the module as the covered Step 3.**

---

## 5. Gaps, Ambiguities, and Likely Over-Annotations

**5.1 The "gap" is a metadata artifact, not biology.** The proteome-wide census confirms exactly one enzyme for each of steps 2 and 3 and two for step 1:

| InterPro / EC | Function | Copies in KT2440 |
|---------------|----------|------------------|
| IPR012801 / EC 1.13.11.1 | catechol 1,2-dioxygenase (Step 1) | **2** (catA-I, catA-II) |
| IPR013370 / EC 5.5.1.1 | muconate cycloisomerase (Step 2) | **1** (catB) |
| IPR003464 / EC 5.3.3.4 | muconolactone δ-isomerase (Step 3) | **1** (catC) |
| — / EC 1.13.11.2 | catechol 2,3-dioxygenase (*meta*) | **0** |
| *clcA*-named | chlorocatechol 1,2-dioxygenase | **0** |

Every expected step of the working module is covered once CatC is included.

**5.2 Bucket-label mismatch (likely over-broad database framing).** `ppu00361` resolves to "Chlorocyclohexane and chlorobenzene degradation," but KT2440 possesses **no chlorocatechol or *meta*-cleavage machinery**. The three genes captured by this bucket are the generic catechol *ortho*-cleavage enzymes, cross-listed into the chlorobenzene map because chlorocatechol pathways are evolutionary offshoots of the *cat* pathway. For KT2440 curation, the module should be labeled as the **catechol *ortho*-cleavage branch of the β-ketoadipate pathway (M00568)**, not chlorobenzene degradation.

**5.3 Paralog ambiguity (curation-relevant, not an over-annotation).** Both catA-I and catA-II are legitimately annotated as EC 1.13.11.1. This is **not** annotation over-propagation — the 76.7% identity and distinct genomic contexts confirm two real genes. However, curators should flag that only catA-I is operonically part of the *cat* cluster; catA-II is a *ben*-cluster paralog whose primary physiological substrate flux may differ.

**5.4 No evidence of broad/generic EC or GO over-mapping.** All four loci carry *specific* family assignments (dedicated Pfam/InterPro families for each enzyme class), so there is no sign that a broad EC (e.g., a generic "dioxygenase" or "isomerase") has been over-propagated onto unrelated proteins.

**5.5 Enzyme-level evidence gap.** For all four loci, biochemical characterization (in vitro kinetics, substrate range, structure) is **absent for KT2440 specifically**; UniProt lists them at protein-existence level 3. Supporting biochemistry exists only in related organisms (see §8).

---

## 6. Module and GO-Curation Recommendations

| Module step | Recommended status | Basis |
|-------------|-------------------|-------|
| Step 1 — catechol 1,2-dioxygenase | **covered** (two paralogs) | catA-I/PP_3713 + catA-II/PP_3166; specific IPR012801; direct genomic evidence [PMID: 12534466] |
| Step 2 — muconate cycloisomerase | **covered** | catB/PP_3715; specific IPR013370 |
| Step 3 — muconolactone δ-isomerase | **covered** (after fix) | catC/PP_3714; specific IPR003464 — **add to module** |

**Actionable curation fixes:**

1. **Add CatC/PP_3714 (Q88GK7, K03464, EC 5.3.3.4) to the module** as the Step-3 gene. This is the single most important fix.
2. **Relabel the bucket** from "Chlorocyclohexane and chlorobenzene degradation" to "catechol *ortho*-cleavage branch of the β-ketoadipate pathway (KEGG M00568)" for this organism, and record that KT2440 lacks chlorocatechol/*meta* enzymes.
3. **Record the two-paralog structure of Step 1** with genomic context (catA-I in *cat* operon; catA-II in *ben* cluster) so downstream logic does not treat them as redundant.
4. **Note the module boundary explicitly:** the working module stops at the β-ketoadipate enol-lactone; the downstream 3-oxoadipate enol-lactonase (K01055/EC 3.1.1.24) is present as PP_1380 in the *pca* cluster, confirming the handoff exists just past the boundary but is a separate module.
5. **No new GO term request appears necessary** — GO terms and enzyme families exist for all three steps and map specifically. The gap was purely a pathway-membership partition, not a missing ontology term.

**Module boundaries assessment:** The *generic* module boundaries (catechol → enol-lactone, three steps CatA/CatB/CatC) are **correct** for KT2440. It is the *candidate-list construction* (single-bucket ppu00361 filter) that was wrong, not the module design.

---

## 7. Genes to Promote to Full Review

| Gene | Locus | Priority | Reason |
|------|-------|----------|--------|
| **catC** | PP_3714 (Q88GK7) | **High** | Missing Step-3 gene; add to module immediately |
| catA-I | PP_3713 (Q88GK8) | Medium | Resolve paralog role vs catA-II; confirm operon function |
| catA-II | PP_3166 (Q88I35) | Medium | Confirm *ben*-cluster catechol-flux role; paralog disambiguation |
| catB | PP_3715 (Q88GK6) | Low | Well-placed in operon; low ambiguity |

The **catA-I vs catA-II differential role** is the principal open scientific question and the strongest reason to promote both catA loci to full `fetch-gene` review.

---

## 8. Evidence Base and Key References

**Direct, KT2440-specific evidence (genomic / transcriptomic):**

- *Genomic analysis of the aromatic catabolic pathways from Pseudomonas putida KT2440.* [PMID: 12534466](https://pubmed.ncbi.nlm.nih.gov/12534466/) — Establishes that the catechol (*cat*) and protocatechuate (*pca*) branches of the β-ketoadipate pathway are genomically defined in KT2440. Verbatim: *"predicted the existence of at least four main pathways for the catabolism of central aromatic intermediates, that is, the protocatechuate (pca genes) and catechol (cat genes) branches of the beta-ketoadipate pathway."* This is the foundational, direct evidence for module presence.
- *Transcriptome analysis of Pseudomonas putida KT2440 harboring the pCAR1 plasmid.* [PMID: 17675379](https://pubmed.ncbi.nlm.nih.gov/17675379/) — Confirms the chromosomal *cat* and *pca* genes function in the catechol branch and are co-induced during aromatic (carbazole/benzoate) catabolism. Verbatim: *"the chromosomal cat and pca genes involved in the catechol branch of the beta-ketoadipate pathway."*

**Mechanistic / boundary evidence (related organisms, transfer noted):**

- *Crystal structure of catechol 2,3-dioxygenase (metapyrocatechase) from Pseudomonas putida mt-2.* [PMID: 10368270](https://pubmed.ncbi.nlm.nih.gov/10368270/) — Documents the intradiol-vs-extradiol distinction. Verbatim: *"Catechol dioxygenases catalyze the ring cleavage of catechol and its derivatives in either an intradiol or extradiol manner."* Justifies keeping the *ortho* (intradiol) module separate from the *meta* route. Transfer to KT2440: the *meta* enzyme is from a related strain (mt-2) and is **absent** from KT2440's genome.
- *Genome-wide investigation of the β-ketoadipate pathway in Pseudomonas stutzeri A1501.* [PMID: 20137101](https://pubmed.ncbi.nlm.nih.gov/20137101/) — Shows *catR* can be absent in some *Pseudomonas*. Verbatim: *"the absence of the catR and pcaK genes encoding a LysR family regulator."* KT2440 by contrast **retains** *catR* (PP_3716) — a curation-relevant regulatory difference. Transfer: weak (different species), used only as a contrast.

**Enzyme-level biochemistry (related organisms only — homology transfer, not direct for KT2440 loci):**

- *Anthranilate degradation by a cold-adapted Pseudomonas sp. PAMC 25931.* [PMID: 23720227](https://pubmed.ncbi.nlm.nih.gov/23720227/) — Functional recombinant CatA (catechol 1,2-dioxygenase) from a *catBCA* cluster, anthranilate-induced. Supports the biochemical plausibility of the KT2440 CatA annotation, but is from a different *Pseudomonas* sp.; transfer to KT2440 is moderate (same enzyme family, different strain).
- *Purification and characterization of catechol 1,2-dioxygenase from a phenol-degrading Pseudomonas putida.* [PMID: 37702837](https://pubmed.ncbi.nlm.nih.gov/37702837/) — C12O activity in *P. putida* (local isolate), ~69 kDa. Species-level support, not the KT2440 locus.
- *Co-metabolism of phenolic compounds by Pseudomonas putida.* [PMID: 22279923](https://pubmed.ncbi.nlm.nih.gov/22279923/) — Demonstrates *ortho*-cleavage phenol degradation with *cis,cis*-muconate and 3-oxoadipate intermediates in *P. putida*. Supports operation of the *ortho* branch at the species level.

**Evidence tiering summary:**

| Claim | Evidence tier | Directness for KT2440 |
|-------|---------------|----------------------|
| *cat* branch present & genomically defined | Direct genomic | **High** (KT2440) [PMID: 12534466] |
| *cat* genes co-induced during aromatic catabolism | Direct transcriptomic | **High** (KT2440) [PMID: 17675379] |
| CatA/CatB/CatC specific enzyme identities | Homology (InterPro/UniProt level 3) | Inferred |
| CatA enzyme kinetics/substrate range | Biochemistry in related *Pseudomonas* | Weak–moderate transfer [PMID: 23720227, 37702837] |
| No *meta*/chlorocatechol enzymes | Proteome census | **High** (KT2440) |

---

## 9. Mechanistic Model and Interpretation

The narrative that emerges across the five iterations is a **metadata-provenance story layered on solid biology**. Biologically, KT2440 carries a textbook catechol *ortho*-cleavage branch: a *cat* operon (`catA-I–catC–catB–catR`) plus a second, benzoate-cluster-embedded catechol 1,2-dioxygenase (catA-II). This gene arrangement — two dioxygenase paralogs feeding one downstream cycloisomerase/isomerase pair — likely reflects **substrate-source specialization**: catA-II may handle catechol generated locally from benzoate (its *ben*-cluster neighbors are benzoate-pathway genes), while catA-I serves the general catechol pool routed through the *cat* operon under CatR control. This hypothesis is consistent with the genomic architecture but has **not** been tested biochemically for these specific loci, and is the key open question.

The "missing Step 3" flagged by the candidate metadata is not a biological gap but a **KEGG map-partitioning artifact**: PP_3714 (catC) is filed under Benzoate degradation (ppu00362), not the chlorobenzene bucket (ppu00361) from which candidates were drawn. Recognizing this resolves the apparent gap and prevents an incorrect "module unsatisfiable" call. Similarly, the bucket's "chlorobenzene degradation" name is an over-broad cross-listing: KT2440's enzymes are the ancestral, non-chlorinated *cat* enzymes, and the organism has none of the chlorocatechol or *meta*-cleavage machinery the bucket name implies.

**Bottom line for curation:** mark all three steps **covered**, add CatC/PP_3714, relabel the bucket, record the two-paralog structure, and promote the two catA loci for follow-up to resolve their differential roles.

---

## 10. Limitations and Knowledge Gaps

1. **No direct enzyme-level evidence for the specific KT2440 loci.** All four proteins are UniProt protein-existence level 3 (inferred from homology). No in vitro kinetics, substrate-range, or structural data exist for PP_3166/PP_3713/PP_3714/PP_3715 themselves.
2. **Paralog roles unresolved.** The relative in-vivo contribution of catA-I (cat operon) vs catA-II (ben cluster) has not been dissected (e.g., by single/double knockouts or expression profiling under distinct aromatic substrates).
3. **Regulatory detail incomplete.** CatR (PP_3716) is present, but its precise operon control and any cross-talk with *ben*-cluster regulation in KT2440 were not experimentally examined here.
4. **Analysis is annotation-driven.** Conclusions rest on UniProt/KEGG/InterPro annotations and published genomic/transcriptomic studies, not on new wet-lab data generated in this review.

---

## 11. Proposed Follow-up Experiments / Actions

**Curation actions (immediate, no experiments needed):**
- Add CatC/PP_3714 to the module as Step 3 (covered).
- Relabel the `ppu00361` bucket for KT2440 to "catechol *ortho*-cleavage branch of the β-ketoadipate pathway (M00568)"; annotate the absence of chlorocatechol/*meta* enzymes.
- Record catA-I/catA-II as two genuine paralogs with genomic context.
- Promote catA-I, catA-II (high value) and catC (for module addition) to full `fetch-gene` review.

**Wet-lab experiments to close the enzyme-level gap:**
- **Paralog knockouts:** ΔcatA-I, ΔcatA-II, and the double mutant, with growth assays on catechol vs benzoate vs phenol, to resolve differential physiological roles.
- **Recombinant expression + kinetics** of PP_3713, PP_3166, PP_3714, PP_3715 to obtain locus-specific k_cat/K_m and substrate ranges (would elevate protein-existence to level 1).
- **Transcriptional reporter / RT-qPCR** of the *cat* operon vs catA-II under CatR induction to test the substrate-source-specialization hypothesis.

**Expert questions:**
- Is catA-II expression benzoate-specific and CatR-independent in KT2440?
- Does the *cat* operon's CatR regulon overlap with *ben*-cluster regulation?

---

### Consensus

The catechol *ortho*-cleavage branch of the β-ketoadipate pathway is **fully satisfiable** in *P. putida* KT2440. All three steps are encoded by specific, high-quality annotations — catechol 1,2-dioxygenase (two paralogs: catA-I/PP_3713, catA-II/PP_3166), muconate cycloisomerase (catB/PP_3715), and muconolactone δ-isomerase (catC/PP_3714). The only real curation defect is the omission of CatC/PP_3714 from the candidate list — a KEGG map-partition artifact — plus the misleading "chlorobenzene degradation" bucket label. No true pathway gap exists.


## Artifacts

- [OpenScientist final report](PSEPK__catechol_ortho_cleavage__ppu00361-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__catechol_ortho_cleavage__ppu00361-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:10368270
2. PMID:20137101
3. PMID:12534466
4. PMID:17675379
5. PMID:23720227
6. PMID:37702837
7. PMID:22279923