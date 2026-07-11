---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T15:40:45.652061'
end_time: '2026-07-11T15:51:26.575913'
duration_seconds: 640.92
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Cellulose biosynthesis
  module_summary: A Pseudomonas putida KT2440 UniPathway UPA00694 module for bacterial
    cellulose biosynthesis by a BcsA cellulose synthase catalytic subunit, the BcsB
    cyclic-di-GMP-binding regulatory subunit, and a BcsC-like cellulose synthase operon
    C outer-membrane/export protein.
  module_outline: "- Cellulose biosynthesis\n  - 1. Cellulose synthase catalytic subunit\n\
    \  - BcsA cellulose polymerization step\n    - bcsA: cellulose synthase catalytic\
    \ subunit (molecular player: PSEPK bcsA; activity or role: cellulose synthase\
    \ (UDP-forming) activity)\n  - 2. c-di-GMP-responsive cellulose synthase regulatory\
    \ subunit\n  - BcsB cellulose synthase regulatory step\n    - bcsB: c-di-GMP-responsive\
    \ cellulose synthase regulator (molecular player: PSEPK bcsB; activity or role:\
    \ cyclic-di-GMP binding)\n  - 3. Cellulose synthase operon C export/support protein\n\
    \  - PP_2638 cellulose export/support step\n    - PP_2638: cellulose synthase\
    \ operon C protein (molecular player: PSEPK PP_2638)"
  module_connections: No explicit connections.
  pathway_query: UPA00694
  pathway_id: UPA00694
  pathway_name: UniPathway UPA00694
  pathway_source: UniPathway
  pathway_context: 'Resolved local bucket unipathway:UPA00694 with 2 primary genes;
    module area: unipathway.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '2'
  candidate_genes: '- bcsB: PP_2636 | Q88JL3 | Cyclic di-GMP-binding protein (Cellulose
    synthase regulatory subunit) (primary bucket unipathway:UPA00694)

    - PP_2638: PP_2638 | Q88JL1 | Cellulose synthase operon C protein (primary bucket
    unipathway:UPA00694)'
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 3
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 2
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__cellulose_biosynthesis__upa00694-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__cellulose_biosynthesis__upa00694-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Cellulose biosynthesis in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: UPA00694
- Resolved ID: UPA00694
- Resolved name: UniPathway UPA00694
- Source: UniPathway

Resolved local bucket unipathway:UPA00694 with 2 primary genes; module area: unipathway.

## Candidate Genes From Local Metadata

Candidate gene count: 2

- bcsB: PP_2636 | Q88JL3 | Cyclic di-GMP-binding protein (Cellulose synthase regulatory subunit) (primary bucket unipathway:UPA00694)
- PP_2638: PP_2638 | Q88JL1 | Cellulose synthase operon C protein (primary bucket unipathway:UPA00694)

## Generic Module Context

### Working Scope

A Pseudomonas putida KT2440 UniPathway UPA00694 module for bacterial cellulose biosynthesis by a BcsA cellulose synthase catalytic subunit, the BcsB cyclic-di-GMP-binding regulatory subunit, and a BcsC-like cellulose synthase operon C outer-membrane/export protein.

### Provisional Biological Outline

- Cellulose biosynthesis
  - 1. Cellulose synthase catalytic subunit
  - BcsA cellulose polymerization step
    - bcsA: cellulose synthase catalytic subunit (molecular player: PSEPK bcsA; activity or role: cellulose synthase (UDP-forming) activity)
  - 2. c-di-GMP-responsive cellulose synthase regulatory subunit
  - BcsB cellulose synthase regulatory step
    - bcsB: c-di-GMP-responsive cellulose synthase regulator (molecular player: PSEPK bcsB; activity or role: cyclic-di-GMP binding)
  - 3. Cellulose synthase operon C export/support protein
  - PP_2638 cellulose export/support step
    - PP_2638: cellulose synthase operon C protein (molecular player: PSEPK PP_2638)

### Known Relationships Among Steps

No explicit connections.

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

# Module/Pathway/Taxon Review: Cellulose Biosynthesis (UniPathway UPA00694) in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (organism code PSEPK; NCBI taxon 160488; proteome UP000000556)
**Target pathway/bucket:** UniPathway UPA00694 — bacterial cellulose biosynthesis (local bucket `unipathway:UPA00694`)
**Module area:** unipathway
**Assignment:** Species-aware module satisfiability and gene-annotation curation review

---

## 1. Executive Summary

UniPathway **UPA00694 (bacterial cellulose biosynthesis) is satisfiable and effectively complete** in *Pseudomonas putida* KT2440. The genome encodes a single, contiguous *bcs* (bacterial cellulose synthesis) operon spanning **PP_2631–PP_2638** that supplies every catalytic and regulatory function the module requires: the BcsA cellulose synthase catalytic subunit, the BcsB cyclic-di-GMP-binding regulatory subunit, and a BcsC-like outer-membrane export/support protein, together with a supporting cast of accessory glucanases and assembly factors. The system is **single-copy** — there is no paralogous cellulose synthase elsewhere in the genome — so the module carries **no paralog-ambiguity or over-propagation risk** from duplicated synthases.

Two concrete curation actions are nevertheless required, because the candidate metadata handed to this review is both **incomplete** and contains a **downstream mislabel**. First, the candidate list of two genes (bcsB/PP_2636 and PP_2638) **omits the actual catalytic subunit, BcsA (PP_2635 / Q88JL4)** — the enzyme that performs the defining reaction of the pathway (EC 2.4.1.12, cellulose synthase, UDP-forming). BcsA is present in the genome, correctly annotated in UniProt, and sits immediately upstream of the two candidate genes in the same operon; it was simply not assigned to the module's step-1 slot. This gene should be added and the catalytic step marked **covered**. Second, the neighboring locus **PP_2634 (Q88JL5)** carries a generic protein name "Cellulose synthase," but its domain architecture (InterPro IPR017746 *Cellulose_synthase_operon_BcsQ*; Pfam PF06564 *CBP_BcsQ*; TIGR03371 *cellulose_yhjQ*; P-loop NTPase fold) identifies it unambiguously as **BcsQ (YhjQ), a ParA/MinD-like partitioning ATPase**, *not* a second glycosyltransferase. This is a likely **over-propagated annotation** that should be corrected during curation so it is not counted as a redundant synthase.

The biological importance of the pathway in this organism is modest and condition-dependent. Direct experimental work in KT2440 ([PMID: 21507178](https://pubmed.ncbi.nlm.nih.gov/21507178/)) shows the *bcs* cluster does mediate cellulose biosynthesis, but plays only a **minor role in biofilm formation and stability** under the conditions tested; the novel Pea and Peb exopolysaccharide systems dominate KT2440 biofilm architecture. This does not affect module satisfiability — the genes are present and functional — but it is relevant curation context: cellulose is a facultative, accessory EPS in this strain rather than its principal matrix polymer.

---

## 2. Target-Organism Pathway Definition

**What UPA00694 includes.** Bacterial cellulose biosynthesis is the c-di-GMP-activated polymerization of **UDP-glucose into β-1,4-linked glucan (cellulose)** at the inner membrane, followed by transenvelope guidance and secretion of the nascent chain to the cell surface. The defining catalytic reaction is **UDP-glucose + [(1→4)-β-D-glucosyl]ₙ → UDP + [(1→4)-β-D-glucosyl]ₙ₊₁** (EC 2.4.1.12), carried out by a processive membrane-integral glycosyltransferase of family GT2. The minimal functional core in the well-studied *Bcs* systems is the **BcsA–BcsB** complex, in which BcsA is the catalytic subunit and BcsB is a periplasmic/membrane-anchored partner; polymerization is switched on by direct binding of the second messenger **cyclic di-GMP** to a C-terminal PilZ domain of BcsA and to the BcsB regulatory subunit. Chain export across the outer membrane requires a **BcsC-like** protein bearing periplasmic TPR repeats and a β-barrel.

**What to keep separate.** For curation, this module should be bounded to *synthesis, assembly and export of cellulose*. It should **not** be merged with:
- **Alginate biosynthesis** (the *alg* cluster) — a distinct EPS pathway in KT2440.
- **Pea / Peb exopolysaccharide biosynthesis** — the dominant KT2440 biofilm EPS systems, mechanistically unrelated to cellulose.
- **Nucleotide-sugar supply** (UDP-glucose generation via *galU*/*pgm*) — an upstream precursor pathway that feeds many polysaccharides, not part of UPA00694 proper.
- **General c-di-GMP signaling** (diguanylate cyclases / phosphodiesterases genome-wide) — these set the c-di-GMP pool but are a signaling network, not the cellulose module; only the c-di-GMP *effector* elements within the *bcs* system belong here.

**Alternate names / database definitions.** The pathway appears under several conventions: *UniPathway UPA00694*; the *bcs* (bacterial cellulose synthesis) operon nomenclature; the older *acs* (Acetobacter cellulose synthase) nomenclature; "cellulose synthase (UDP-forming)" (EC 2.4.1.12); and GO terms for cellulose biosynthetic process / cellulose synthase (UDP-forming) activity. Gene names in KT2440 follow the *bcsA/B/C/…* convention.

---

## 3. Expected Step Model

The generic module posits three steps. The table below maps each to KT2440 evidence.

| Module step | Expected player / activity | KT2440 gene | UniProt | Status |
|---|---|---|---|---|
| **1. Catalytic subunit** | BcsA cellulose synthase (UDP-forming), EC 2.4.1.12 | **PP_2635** | Q88JL4 | **Covered** — present, but *missing from candidate list* |
| **2. c-di-GMP regulatory subunit** | BcsB, cyclic-di-GMP binding | **PP_2636** (bcsB) | Q88JL3 | **Covered** — in candidate list |
| **3. Operon-C export/support** | BcsC-like outer-membrane/export | **PP_2638** | Q88JL1 | **Covered** — in candidate list |

Beyond the three-step generic outline, the full KT2440 *bcs* operon supplies the canonical accessory functions expected of a structurally complete cellulose machine:

```
  PP_2631   PP_2632     PP_2633  PP_2634   PP_2635   PP_2636   PP_2637     PP_2638
  BcsF/YhjT endoglucanase BcsR   BcsQ      BcsA      BcsB      GH8/BcsZ    BcsC
  (61 aa)   (537 aa)     (72 aa) (ATPase)  (CATALYTIC)(c-di-GMP)(cellulase) (TPR export)
   |          |            |       |          |          |         |           |
   accessory  glucan       assembly partition CATALYSIS  REGULATION glucan     EXPORT
   membrane   hydrolysis   factor   ATPase    (EC 2.4.1.12)(PilZ)   hydrolysis  (outer mem)
                                              c-di-GMP-ACTIVATED CORE
```

Compared with the canonical *bcsABCD* reference operon of dedicated cellulose producers, KT2440 has clear **A, B, C** and multiple accessory factors; the classic **BcsD** crystalline-packing subunit is not prominent, consistent with KT2440 producing a non-crystalline/accessory cellulose rather than the thick crystalline pellicle of dedicated producers such as *Gluconacetobacter*.

---

## 4. Candidate Genes and Evidence

### F001 — BcsA catalytic subunit (PP_2635 / Q88JL4) is present but was omitted from the candidate list

The single most important finding of this review is that the **catalytic engine of the pathway was not in the candidate metadata.** UniProt Q88JL4 (PP_2635, 869 aa) is annotated as the "**Catalytic subunit of cellulose synthase. It polymerizes uridine 5′-diphosphate glucose to cellulose**," carries **EC 2.4.1.12** (cellulose synthase, UDP-forming), belongs to the **glycosyltransferase-2 (GT2) family**, and has the diagnostic **GT2-like + PilZ (c-di-GMP-binding) domain architecture** of an inner-membrane processive synthase. UniProt places it explicitly in PATHWAY "bacterial cellulose biosynthesis." Crucially, PP_2635 sits **immediately upstream of both candidate genes** — bcsB (PP_2636) and the bcsC-like protein (PP_2638) — in one contiguous operon. The module's step-1 slot named an expected molecular player ("PSEPK bcsA") but had no gene assigned. This is therefore not a genuine gap in the organism but a **metadata omission**: the catalytic step is covered by PP_2635 and should be recorded as such. Without this gene the module would appear to have a regulatory subunit and an exporter but no enzyme — biologically nonsensical.

**Curation action:** add PP_2635 (BcsA) to `unipathway:UPA00694`, mark step 1 **covered**, and promote to full `fetch-gene` review as the module's keystone gene.

### F002 — KT2440 encodes a complete *bcs* cellulose operon (PP_2631–PP_2638)

Reading the locus in order establishes a coherent, structurally complete cellulose machine. The UniProt-annotated members are: **PP_2631** (Q88JL8, BcsF/YhjT, 61 aa, small accessory membrane protein); **PP_2632** (Q88JL7, endoglucanase, 537 aa); **PP_2633** (Q88JL6, BcsR, 72 aa, assembly factor); **PP_2634** (Q88JL5, generic "cellulose synthase," 235 aa, sparse annotation — see F004); **PP_2635** (Q88JL4, BcsA catalytic subunit, EC 2.4.1.12); **PP_2636** (Q88JL3, BcsB c-di-GMP-binding regulatory subunit, AcsB/BcsB family); **PP_2637** (Q88JL2, glycoside hydrolase family 8 / cellulase D, EC 3.2.1.-, notable for having a **solved 3D structure**); and **PP_2638** (Q88JL1, BcsC operon-C protein, TPR repeats, "required for maximal cellulose synthesis"). The flanking genes PP_2639 (*dapA*) and PP_2640 (GNAT acetyltransferase) are functionally unrelated and mark the operon boundaries.

This composition maps cleanly onto the canonical *bcs* reference. In *Gluconacetobacter xylinus*, the operon is defined as "**comprising *bcsA*, *bcsB*, *bcsC*, and *bcsD***" ([PMID: 29674724](https://pubmed.ncbi.nlm.nih.gov/29674724/)), and "**cyclic diguanylate (c-di-GMP) is the key activator of BcsA–BcsB subunit of Bcs**." Both statements transfer well to KT2440 at the level of the conserved A/B/C core: PP_2635/PP_2636 form the c-di-GMP-regulated catalytic–regulatory heart, and PP_2638 provides the C export function. The species transfer for *mechanism* is strong (deeply conserved Bcs biochemistry), while transfer of *phenotype* (crystalline pellicle formation) is weak, since KT2440 is not a dedicated cellulose producer.

### bcsB (PP_2636 / Q88JL3) — candidate gene, high confidence

The c-di-GMP-responsive regulatory subunit. Annotated in UniProt as a **cyclic di-GMP-binding protein / cellulose synthase regulatory subunit** of the AcsB/BcsB family. It is the effector that couples the intracellular c-di-GMP pool to activation of the BcsA catalytic subunit. Evidence type: **homology + domain architecture + operon context**; direct KT2440 biochemistry is absent but the assignment is secure. **Status: covered.** Curation caveat: none major; role is well defined. Single-copy (F005).

### PP_2638 (Q88JL1) — candidate gene, high confidence

The **BcsC-like operon-C protein**, bearing periplasmic **TPR repeats** and annotated "**required for maximal cellulose synthesis**." This is the transenvelope export/support component that guides the nascent glucan across the periplasm and outer membrane. Evidence type: **homology + domain architecture + operon context**. **Status: covered.** Curation caveat: "operon C protein" is a family-level assignment; the precise outer-membrane β-barrel topology in KT2440 is inferred, not experimentally solved.

### F004 — PP_2634 (Q88JL5) is BcsQ (YhjQ), not a synthase

PP_2634 is labeled with the generic protein name "Cellulose synthase," but this is a **mis-annotation / over-propagation.** Its InterPro/Pfam/TIGRFAM cross-references are decisive: **InterPro IPR017746 "Cellulose_synthase_operon_BcsQ"; Pfam PF06564 "CBP_BcsQ"; NCBIfam TIGR03371 "cellulose_yhjQ"; Gene3D 3.40.50.300 / SUPFAM SSF52540 "P-loop containing NTP hydrolases."** These signatures define a **ParA/MinD-like partitioning ATPase (BcsQ/YhjQ)**, which localizes the cellulose machinery to the cell pole/membrane — an assembly/positioning factor, not a glycosyltransferase. Consistent with this, the entry carries **no FUNCTION text, no EC number, and no GT domain**. The 235-aa length is typical of a small P-loop ATPase and far too short for a processive synthase (BcsA is 869 aa). **Status: covered as BcsQ (accessory), but flagged for name correction.**

### F005 — The system is single-copy; no paralog ambiguity

A proteome-wide UniProt scan (taxon 160488) shows that the EC 2.4.1.12 / "cellulose synthase" name maps **only to the four operon loci** (PP_2634 BcsQ, PP_2635 BcsA, PP_2636 BcsB, PP_2638 BcsC). BcsB-family and BcsC operon-C names each return **exactly one** hit (PP_2636 and PP_2638 respectively). Among 14 c-di-GMP/PilZ-domain proteins genome-wide, **only PP_2635 (BcsA) is a cellulose synthase**; the remainder are diguanylate cyclases/phosphodiesterases, the flagellar brake YcgR (PP_4397), and other PilZ proteins unrelated to cellulose. This means the module is unambiguous: there is **no second synthase to disambiguate**, and no risk that a distant homolog is being wrongly counted as fulfilling the catalytic step.

---

## 5. Gaps, Ambiguities, and Likely Over-Annotations

**Metadata gap (not a biological gap).** The candidate list contained only 2 of the ≥3 core genes; the catalytic subunit BcsA (PP_2635) was missing. This is the highest-priority correction. The biological pathway is *not* incomplete — only the module's gene mapping was.

**Likely over-annotation — PP_2634.** The generic "Cellulose synthase" protein name on PP_2634 is misleading. It is BcsQ, a positioning ATPase. If a curator or automated pipeline treats this name literally, it could be double-counted as a second synthase or wrongly assigned to the catalytic step. Recommend renaming to **BcsQ / cellulose biosynthesis protein BcsQ** and removing any implied glycosyltransferase/EC 2.4.1.12 mapping.

**Broad EC/GO mapping caution.** PP_2632 (endoglucanase) and PP_2637 (GH8 cellulase, EC 3.2.1.-) are cellulose-*degrading/processing* hydrolases embedded in the operon. They are legitimately part of the cellulose machine (chain editing, crystallinity control, glucan trimming), but they carry hydrolase EC numbers, not biosynthetic ones. They should be recorded as **accessory / editing** functions, not as fulfilling the biosynthetic catalytic step, to avoid confusing the module's satisfiability logic.

**BcsD absence.** The classic BcsD crystalline-packing subunit of dedicated producers is not clearly present. For KT2440 this is expected (it makes accessory, likely amorphous cellulose), so BcsD should be marked **not_expected_in_target_taxon** rather than a gap.

**Phenotype vs. genotype divergence.** Direct KT2440 evidence (F003) shows the *bcs* cluster plays only a **minor biofilm role**. This is a functional caveat, not a satisfiability gap — the genes are present and the pathway is encoded; the polymer is simply a minor, condition-dependent EPS in this strain relative to Pea/Peb.

---

## 6. Module and GO-Curation Recommendations

| Module step | Recommended status | Rationale |
|---|---|---|
| Step 1 — BcsA catalytic subunit | **covered** — add PP_2635 | Present in genome, EC 2.4.1.12, GT2+PilZ; only missing from metadata |
| Step 2 — BcsB c-di-GMP regulator | **covered** — PP_2636 | In candidate list; secure homology assignment |
| Step 3 — BcsC-like export | **covered** — PP_2638 | In candidate list; TPR export protein |
| Accessory — BcsQ positioning ATPase | **covered (accessory)** — PP_2634, *rename* | Mis-labeled "cellulose synthase"; is BcsQ |
| Accessory — glucanases/editing | **covered (accessory)** — PP_2632, PP_2637 | Hydrolase EC; not biosynthetic step |
| Assembly factors — BcsR, BcsF | **covered (accessory)** — PP_2633, PP_2631 | Small operon accessory proteins |
| BcsD crystalline packing | **not_expected_in_target_taxon** | Absent; KT2440 not a dedicated producer |

**Overall module verdict: SATISFIABLE / COMPLETE** for UPA00694 in KT2440, contingent on the two curation edits (add PP_2635; rename PP_2634).

**Module-boundary assessment.** The generic three-step boundary (catalytic / regulatory / export) is **broadly correct** but too narrow to represent the real KT2440 machine. Consider expanding the module model to include the accessory tier (BcsQ positioning, BcsR/BcsF assembly, glucanase editing) as optional/accessory steps so the operon's full membership is represented without inflating the core satisfiability requirement.

**GO-curation notes.** BcsA (PP_2635) is a clean candidate for confidently inferred GO annotations: *cellulose synthase (UDP-forming) activity* (GO:0016760), *cellulose biosynthetic process* (GO:0030244), *plasma membrane* localization, and *cyclic-di-GMP binding* (GO:0035438) via its PilZ domain. PP_2634 should **lose** any cellulose-synthase-activity GO term and instead receive *ATP binding* / *cell division site positioning*-type terms appropriate to a ParA/MinD ATPase. No new GO term requests appear necessary — existing terms cover all functions.

---

## 7. Genes to Promote to Full `fetch-gene` Review

1. **PP_2635 (BcsA, Q88JL4) — HIGH PRIORITY.** The catalytic subunit and keystone of the module; currently missing from the candidate list. Full review needed to formally add it and confirm the EC/GO mapping and operon assignment.
2. **PP_2634 (BcsQ, Q88JL5) — HIGH PRIORITY.** To correct the over-propagated "Cellulose synthase" protein name to BcsQ and adjust its functional annotation to a P-loop positioning ATPase.
3. **PP_2638 (BcsC-like, Q88JL1) — MEDIUM.** Confirm the outer-membrane export topology and the "operon C" family assignment; verify it is the sole export component.
4. **PP_2637 (GH8 cellulase, Q88JL2) — LOW/OPTIONAL.** Has a solved 3D structure; a useful accessory-function reference but not core to satisfiability.

---

## 8. Evidence Base and Key References

| PMID | Title | How it supports this review |
|---|---|---|
| [21507178](https://pubmed.ncbi.nlm.nih.gov/21507178/) | *Influence of putative exopolysaccharide genes on Pseudomonas putida KT2440 biofilm stability* | **Direct KT2440 evidence.** States the *bcs* cluster codes for proteins mediating cellulose biosynthesis but "**played minor roles in P. putida KT2440 biofilm formation and stability under the conditions tested**," while Pea/Peb dominate. Establishes the pathway is real but accessory in this strain (F003). |
| [29674724](https://pubmed.ncbi.nlm.nih.gov/29674724/) | *Complete genome analysis of Gluconacetobacter xylinus CGMCC 2955 for elucidating bacterial cellulose biosynthesis and metabolic regulation* | Defines the canonical operon "**comprising bcsA, bcsB, bcsC, and bcsD**" and that "**c-di-GMP is the key activator of BcsA-BcsB subunit of Bcs**." Provides the reference frame against which the KT2440 operon (F002) is mapped; mechanistic transfer is strong, phenotypic transfer weak. |

**UniProt / InterPro authoritative resources used:** Q88JL4 (PP_2635 BcsA, EC 2.4.1.12); Q88JL3 (PP_2636 BcsB); Q88JL1 (PP_2638 BcsC); Q88JL5 (PP_2634) with InterPro **IPR017746**, Pfam **PF06564**, TIGRFAM **TIGR03371**, SUPFAM SSF52540 (BcsQ / P-loop NTPase); plus proteome-wide UniProt scan of taxon 160488 (F005).

**Evidence-type summary:**
- *Direct experimental (target organism):* Minor biofilm role of *bcs* in KT2440 (PMID 21507178).
- *Homology + domain architecture + operon synteny (strong inference):* All gene-role assignments (BcsA catalysis, BcsB regulation, BcsC export, BcsQ positioning). No direct KT2440 enzymology on cellulose synthesis itself.
- *Database/reference transfer (moderate):* Operon composition and c-di-GMP mechanism from *Gluconacetobacter* (PMID 29674724).

---

## 9. Limitations and Knowledge Gaps

- **No direct KT2440 enzymology** confirms BcsA (PP_2635) catalyzes cellulose synthesis in vitro; the EC 2.4.1.12 assignment rests on homology and domain architecture, though these are strong.
- **BcsC export topology** in KT2440 is inferred from TPR/operon context, not solved experimentally.
- **Regulatory wiring** — which diguanylate cyclases feed c-di-GMP to BcsA/BcsB in KT2440 — is unresolved; among 14 genome-wide PilZ/c-di-GMP proteins, the upstream signaling partners are not mapped to the cellulose module.
- **Physiological conditions** under which KT2440 cellulose is actually produced are unclear; the one direct study found only a minor biofilm contribution, so the pathway's in vivo relevance may be niche/stress-specific.
- **BcsD status** is inferred absent; a targeted search could confirm it is genuinely not encoded.

## 10. Proposed Follow-up Actions

1. **Curate metadata:** add PP_2635 (BcsA) to `unipathway:UPA00694` step 1 (covered); rename/reannotate PP_2634 as **BcsQ** and strip its cellulose-synthase name/EC.
2. **Promote PP_2635 and PP_2634** to full `fetch-gene` review (Section 7).
3. **Expand the module model** to include the accessory tier (BcsQ, BcsR, BcsF, glucanases) as optional steps and mark **BcsD not_expected_in_target_taxon**.
4. **Experimental resolution (if pursued):** cellulose-specific staining (Calcofluor/Congo Red) and a ΔbcsA (PP_2635) knockout to confirm the polymer product; RNA-seq under biofilm/desiccation stress to identify inducing conditions; map the c-di-GMP cyclase(s) that activate the operon.

---

*Prepared for manual module satisfiability and gene-annotation curation. Verdict: UPA00694 is satisfiable/complete in P. putida KT2440 pending two edits — add BcsA (PP_2635); reannotate BcsQ (PP_2634).*


## Artifacts

- [OpenScientist final report](PSEPK__cellulose_biosynthesis__upa00694-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__cellulose_biosynthesis__upa00694-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:21507178
2. PMID:29674724