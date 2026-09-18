---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T10:45:23.214006'
end_time: '2026-08-31T11:05:30.328549'
duration_seconds: 1207.11
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Bacterial D-ribose uptake and entry
  module_summary: A reusable bacterial route in which an RbsABC complex imports D-ribose,
    RbsD interconverts the beta-pyranose and beta-furanose forms, and RbsK phosphorylates
    ribose to D-ribose 5-phosphate for entry into central carbon and nucleotide metabolism.
    Transcriptional regulation and downstream pentose-phosphate reactions are outside
    the module boundary.
  module_outline: "- Bacterial D-ribose uptake and entry\n  - 1. ATP-dependent D-ribose\
    \ import\n  - RbsABC D-ribose import\n    - RbsABC D-ribose transporter activity\
    \ (molecular player: bacterial RbsABC importer; activity or role: ABC-type D-ribose\
    \ transporter activity)\n  - 2. D-ribose ring-form interconversion\n  - RbsD D-ribose\
    \ pyranase reaction\n    - RbsD D-ribose pyranase activity (molecular player:\
    \ bacterial D-ribose pyranase family; activity or role: D-ribose pyranase activity)\n\
    \  - 3. D-ribose phosphorylation\n  - RbsK ribokinase reaction\n    - RbsK ribokinase\
    \ activity (molecular player: bacterial ribokinase family; activity or role: ribokinase\
    \ activity)"
  module_connections: '- RbsABC D-ribose import feeds into RbsD D-ribose pyranase
    reaction: Imported cytoplasmic D-ribose is the substrate pool for RbsD.

    - RbsD D-ribose pyranase reaction feeds into RbsK ribokinase reaction: RbsD supplies
    beta-D-ribofuranose for RbsK phosphorylation.'
  pathway_query: rbs_locus
  pathway_id: rbs_locus
  pathway_name: rbs_locus
  pathway_source: free-text pathway query
  pathway_context: No local pathway bucket was resolved for this query.
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '0'
  candidate_genes: No local candidate gene table was available or no genes matched
    this pathway/bucket.
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
citation_count: 3
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__bacterial_ribose_uptake_and_entry__rbs-locus-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__bacterial_ribose_uptake_and_entry__rbs-locus-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Bacterial D-ribose uptake and entry in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: rbs_locus
- Resolved ID: rbs_locus
- Resolved name: rbs_locus
- Source: free-text pathway query

No local pathway bucket was resolved for this query.

## Candidate Genes From Local Metadata

Candidate gene count: 0

No local candidate gene table was available or no genes matched this pathway/bucket.

## Generic Module Context

### Working Scope

A reusable bacterial route in which an RbsABC complex imports D-ribose, RbsD interconverts the beta-pyranose and beta-furanose forms, and RbsK phosphorylates ribose to D-ribose 5-phosphate for entry into central carbon and nucleotide metabolism. Transcriptional regulation and downstream pentose-phosphate reactions are outside the module boundary.

### Provisional Biological Outline

- Bacterial D-ribose uptake and entry
  - 1. ATP-dependent D-ribose import
  - RbsABC D-ribose import
    - RbsABC D-ribose transporter activity (molecular player: bacterial RbsABC importer; activity or role: ABC-type D-ribose transporter activity)
  - 2. D-ribose ring-form interconversion
  - RbsD D-ribose pyranase reaction
    - RbsD D-ribose pyranase activity (molecular player: bacterial D-ribose pyranase family; activity or role: D-ribose pyranase activity)
  - 3. D-ribose phosphorylation
  - RbsK ribokinase reaction
    - RbsK ribokinase activity (molecular player: bacterial ribokinase family; activity or role: ribokinase activity)

### Known Relationships Among Steps

- RbsABC D-ribose import feeds into RbsD D-ribose pyranase reaction: Imported cytoplasmic D-ribose is the substrate pool for RbsD.
- RbsD D-ribose pyranase reaction feeds into RbsK ribokinase reaction: RbsD supplies beta-D-ribofuranose for RbsK phosphorylation.

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

# Module/Pathway/Taxon Review: Bacterial D-ribose Uptake and Entry in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Module query:** `rbs_locus` (bacterial D-ribose uptake and entry)
**Candidate genes from local metadata:** 0 (no local candidate table resolved; genes below recovered de novo from UniProt/KEGG for UP000000556)

---

## 1. Executive Summary

The `rbs_locus` module — ATP-dependent D-ribose import (RbsABC), ring-form interconversion (RbsD pyranase), and phosphorylation to D-ribose-5-phosphate (RbsK ribokinase) — is **fully satisfiable** in *Pseudomonas putida* KT2440. Although the commission arrived with an empty candidate gene list, proteome- and genome-level evidence shows that KT2440 encodes a canonical, co-localized, LacI-regulated ribose operon spanning **PP_2454–PP_2459** in the gene order *rbsB-rbsA-rbsC-rbsR-rbsK-rbsD*. All three module steps map cleanly onto genes in this cluster: the import step to *rbsBAC* (PP_2454/2455/2456), the pyranase step to *rbsD* (PP_2459, a Swiss-Prot–reviewed entry, RBSD_PSEPK, EC 5.4.99.62), and the phosphorylation step to *rbsK* (PP_2458, EC 2.7.1.15). The presence of an embedded LacI-family repressor (*rbsR*, PP_2457) and an adjacent ribonucleoside hydrolase (*nuh*, PP_2460, EC 3.2.2.3) is exactly the architecture expected for a bona fide ribose-catabolism locus fed by nucleoside breakdown.

Sequence-identity analysis strengthens the two cytoplasmic steps to near-certainty. KT2440 RbsK (PP_2458) and RbsD (PP_2459) are unambiguous 1:1 orthologs of *Escherichia coli* K-12 RbsK and RbsD (53.2% and 53.1% global identity, respectively), so the phosphorylation and interconversion steps should be marked **covered** with high confidence. For the import step, the operon-embedded binding protein RbsB (PP_2454) is the best ribose-binding-protein match among tested solute-binding-protein controls, supporting **covered** status for import as well, though with the caveat that global-identity scoring using a crude scheme cannot fully resolve substrate specificity of periplasmic binding proteins.

The single material curation problem is **paralog ambiguity and likely annotation over-propagation at the import step**. KT2440 carries a *second* sugar ABC cluster (PP_2757–PP_2761) that is independently annotated as a "ribose importer," including the Swiss-Prot–reviewed RBSA_PSEPK (PP_2759). Unlike the true operon, this second cluster is **not** co-located with any ribokinase, pyranase, or LacI repressor, and it carries two solute-binding proteins and two permeases — an atypical architecture. Its binding proteins lean toward AI-2/xylose-like rather than ribose-like in the identity screen. This cluster should be flagged **candidate_uncertain** and its "ribose" label treated as possibly over-propagated. Secondary cleanups: the operon ATP-binding subunit (PP_2455) and permease (PP_2456) still carry a legacy transporter EC (3.6.3.17), and PP_2456 carries a spurious hydrolase GO term (GO:0016787). Importantly, **all KT2440 evidence is homology/rule-based** — no direct experimental demonstration of ribose transport or catabolism in KT2440 was found in the literature searched.

---

## 2. Target-Organism Pathway Definition

### Process included

The module covers the **cytoplasmic entry route for exogenous D-ribose**: (i) periplasmic capture and ATP-driven import of D-ribose by a Type I ABC importer (binding protein + two transmembrane permease subunits + ATPase), (ii) intracellular interconversion of the β-pyranose and β-furanose ring forms of D-ribose by RbsD/FucU-family pyranase, and (iii) phosphorylation of β-D-ribofuranose to D-ribose-5-phosphate by ribokinase. The product, D-ribose-5-phosphate, feeds the non-oxidative pentose-phosphate pathway and nucleotide metabolism.

### Neighboring processes to keep separate

- **Pentose-phosphate pathway proper** (transketolase/transaldolase, ribose-5-phosphate isomerase). D-ribose-5-phosphate is the module's exit metabolite; downstream reactions are *outside* the module boundary.
- **Nucleoside salvage / catabolism.** The adjacent *nuh* ribonucleoside hydrolase (PP_2460, EC 3.2.2.3) generates free ribose from nucleosides. It is a plausible upstream feeder but is a distinct enzymatic step and should not be counted as one of the three core module steps.
- **Transcriptional regulation.** *rbsR* (PP_2457, LacI family) governs operon expression but is explicitly outside the module's molecular-activity scope.
- **Other sugar ABC importers.** KT2440 is a metabolic generalist with many sugar ABC systems; the second cluster (PP_2757–2761) and glucose ABC transporters must not be conflated with the ribose import step.

### Alternate names / database definitions

The locus is variously described as the *rbs* operon, ribose ABC transporter (TC 3.A.1.2.1), and ribose catabolic operon. RbsD is annotated as **D-ribose pyranase** (EC 5.4.99.62; older references use "RbsD/FucU family" or "mutarotase-like"). RbsK is **ribokinase** (EC 2.7.1.15, PfkB/ribokinase subfamily). Legacy transporter ECs (3.6.3.17, now reclassified toward EC 7.5.2.x for ABC sugar transport) still appear on some subunits.

---

## 3. Expected Step Model

```
   D-ribose (periplasm)
        │
        │  STEP 1: ATP-dependent D-ribose import
        ▼
  ┌──────────────────────────────────────────────┐
  │  RbsABC importer                              │
  │   RbsB  PP_2454  periplasmic binding protein  │
  │   RbsA  PP_2455  ABC ATPase                    │
  │   RbsC  PP_2456  permease (AraH/RbsC)          │
  └──────────────────────────────────────────────┘
        │
        ▼  D-ribose (cytoplasm, β-pyranose ⇌ β-furanose)
        │  STEP 2: ring-form interconversion
        ▼
  ┌──────────────────────────────────────────────┐
  │  RbsD  PP_2459  D-ribose pyranase              │
  │        EC 5.4.99.62 (Swiss-Prot RBSD_PSEPK)    │
  └──────────────────────────────────────────────┘
        │
        ▼  β-D-ribofuranose
        │  STEP 3: phosphorylation
        ▼
  ┌──────────────────────────────────────────────┐
  │  RbsK  PP_2458  ribokinase                     │
  │        EC 2.7.1.15                             │
  └──────────────────────────────────────────────┘
        │
        ▼
   D-ribose-5-phosphate  →  (PPP / nucleotide metabolism; outside module)

  Regulation (outside module):  RbsR  PP_2457  LacI-family repressor
  Feeder (outside module):      Nuh   PP_2460  ribonucleoside hydrolase (EC 3.2.2.3)
```

| Module step | Expected activity | KT2440 gene(s) | Satisfiability |
|---|---|---|---|
| 1. ATP-dependent import | ABC-type D-ribose transporter | *rbsB* PP_2454, *rbsA* PP_2455, *rbsC* PP_2456 | **Covered** (binding-protein specificity a minor caveat) |
| 2. Ring interconversion | D-ribose pyranase (EC 5.4.99.62) | *rbsD* PP_2459 | **Covered** (high confidence) |
| 3. Phosphorylation | Ribokinase (EC 2.7.1.15) | *rbsK* PP_2458 | **Covered** (high confidence) |

---

## 4. Candidate Genes and Evidence

### The canonical operon: PP_2454–PP_2459 (Finding F001)

*Pseudomonas putida* KT2440 encodes a complete, contiguous, and correctly ordered ribose operon within proteome UP000000556. The gene order *rbsB-rbsA-rbsC-rbsR-rbsK-rbsD* recapitulates the classical enterobacterial *rbs* architecture with an embedded LacI-family regulator:

| Locus | Gene | Product / family | EC | Module role |
|---|---|---|---|---|
| PP_2454 | *rbsB* | periplasmic ribose-binding protein (SBP family 2) | — | Import (SBP) |
| PP_2455 | *rbsA* | ABC ATP-binding subunit | (legacy 3.6.3.17) | Import (ATPase) |
| PP_2456 | *rbsC* | permease (AraH/RbsC subfamily) | (legacy 3.6.3.17) | Import (permease) |
| PP_2457 | *rbsR* | LacI-family transcriptional repressor | — | Regulation (outside module) |
| PP_2458 | *rbsK* | ribokinase (PfkB/ribokinase subfamily) | 2.7.1.15 | Phosphorylation |
| PP_2459 | *rbsD* | D-ribose pyranase (RbsD/FucU family) | 5.4.99.62 | Ring interconversion |
| PP_2460 | *nuh* | ribonucleoside hydrolase | 3.2.2.3 | Feeder (outside module) |

PP_2459 (*rbsD*) is a **Swiss-Prot–reviewed** entry (RBSD_PSEPK), the strongest annotation-confidence tier available short of direct experiment. The co-location of *rbsR* and the adjacent *nuh* hydrolase is diagnostic of a genuine ribose-catabolism operon fed by nucleoside breakdown, not a chance clustering of homologs.

### Orthology evidence for the cytoplasmic steps (Finding F003)

Needleman–Wunsch global percent-identity comparisons against *E. coli* K-12 references place the two cytoplasmic enzymes as clear 1:1 orthologs:

| KT2440 protein | *E. coli* reference | % identity | Interpretation |
|---|---|---|---|
| RbsK (PP_2458) | EcRbsK (P0A9J6) | **53.2%** | Unambiguous ribokinase ortholog |
| RbsD (PP_2459) | EcRbsD (P04982) | **53.1%** | Unambiguous pyranase ortholog |

These identities are well within the range expected for functional orthologs across the Gammaproteobacteria and, combined with the reviewed Swiss-Prot status of RbsD, make **steps 2 and 3 covered with high confidence**.

For the **import step**, the operon binding protein RbsB (PP_2454) was screened against three solute-binding-protein controls to test substrate assignment:

| Binding protein | vs RbsB | vs XylF (xylose) | vs LsrB (AI-2) | Best match |
|---|---|---|---|---|
| PP_2454 (operon *rbsB*) | **48.0%** | 46.2% | 45.8% | **RbsB (ribose)** |
| PP_2758 (paralog cluster) | 45.4% | 37.6% | — | RbsB, weaker |
| PP_2757 (paralog cluster) | 43.6% | — | 46.1% | LsrB (AI-2-like) |

The operon RbsB scores highest on the ribose reference, consistent with correct assignment of the import step to the PP_2454–2456 subunits. Both candidate ATPases are near-equal to *E. coli* RbsA (PP_2455 53.0% vs PP_2759 51.5%) and both permease sets match RbsC (~51%), so ATPase/permease identity alone cannot discriminate the two clusters — the discriminating signal comes from operon context and binding-protein specificity, not the transmembrane machinery.

**Caveat on method:** scoring used a crude scheme (match +1 / mismatch −1 / gap −1, no BLOSUM substitution matrix), so the binding-protein differences are *supportive but not decisive*. Periplasmic sugar-binding proteins are notoriously cross-reactive, and global identity is a weak proxy for ligand specificity.

---

## 5. Gaps, Ambiguities, and Likely Over-Annotations

### Paralog ambiguity: the second ABC cluster PP_2757–PP_2761 (Finding F002)

The principal curation hazard is a **second sugar ABC cluster** at PP_2757–PP_2761 that is independently annotated as a ribose importer:

| Locus | Annotation | Note |
|---|---|---|
| PP_2757 | SBP-family binding protein | Leans AI-2-like in identity screen |
| PP_2758 | SBP-family binding protein | RbsB-like but weak |
| PP_2759 | *rbsA*, "Ribose importer TC 3.A.1.2.1 family", EC 7.5.2.7 | **Swiss-Prot reviewed (RBSA_PSEPK)** |
| PP_2760 | AraH/RbsC permease | — |
| PP_2761 | AraH/RbsC permease | — |

This cluster's architecture is **atypical for a dedicated ribose importer**: it contains *two* solute-binding proteins and *two* permeases, and — critically — it is **not co-located with any ribokinase, pyranase, or LacI repressor**. A functional ribose-uptake system normally sits next to (or is regulated together with) the catabolic enzymes that consume its product. The isolation of this cluster from any ribose-catabolic gene, combined with binding proteins that score AI-2/xylose-like, strongly suggests its "ribose" label is **over-propagated** — likely a rule-based transfer of a generic "ribose importer TC family" annotation onto a transporter of different or broader specificity. Notably, the fact that PP_2759 is Swiss-Prot–reviewed does **not** guarantee the substrate assignment is experimentally grounded for KT2440; reviewed status can still reflect rule-based curation.

**Recommendation:** mark this cluster's contribution to the ribose import step as **candidate_uncertain**, and do not let it double-count as a second "covered" import route.

### Legacy EC and spurious GO on the true operon

- **PP_2455 (*rbsA*)** is unreviewed and still carries legacy transporter **EC 3.6.3.17**; **PP_2456 (*rbsC*)** carries the same legacy EC. Under current classification, ABC sugar transport maps to the EC 7.5.2.x series (the reviewed paralog PP_2759 already uses EC 7.5.2.7). These should be reconciled.
- **PP_2456 (*rbsC*)** carries a **spurious hydrolase GO term (GO:0016787)** inconsistent with a membrane permease. This is a clear annotation error to remove.

### No direct experimental evidence in KT2440

Literature searches returned **no direct experimental demonstration** of ribose transport, ribokinase activity, or *rbs* operon function in KT2440 specifically. The strongest same-strain evidence is the reviewed Swiss-Prot entry for RbsD and genome/proteome annotation; everything else is homology- and context-based inference. A carbon-source expression study in KT2440 (PMID: 20807680) profiled glucose, glycerol, citrate and fatty-acid growth but did not test ribose, so it neither confirms nor refutes operon function. Cross-species transfer from *E. coli* (import/kinase/pyranase biochemistry) is **strong for the cytoplasmic enzymes** and **moderate for the import step**.

---

## 6. Module and GO-Curation Recommendations

| Module step | Recommended status | Rationale |
|---|---|---|
| 1. ATP-dependent D-ribose import (RbsABC) | **Covered** via PP_2454–2456; flag paralog PP_2757–2761 as **candidate_uncertain** | Operon RbsB is best ribose-SBP match; second cluster likely over-annotated |
| 2. RbsD ring interconversion | **Covered** (high confidence) | Swiss-Prot reviewed RBSD_PSEPK; 53.1% ortholog of EcRbsD |
| 3. RbsK phosphorylation | **Covered** (high confidence) | 53.2% ortholog of EcRbsK; EC 2.7.1.15 |

**Module-level verdict:** the generic module boundaries are **appropriate for KT2440** — no `module_needs_revision` flag required for scope. The three-step model transfers cleanly.

**Specific curation actions:**
1. Attach the module's import step to the **operon** subunits PP_2454/2455/2456, *not* to the isolated PP_2757–2761 cluster.
2. Flag PP_2757–2761 (esp. reviewed PP_2759/RBSA_PSEPK) for re-examination of substrate specificity; treat "ribose" as **provisional/over-propagated** pending experimental support.
3. Reconcile legacy **EC 3.6.3.17 → EC 7.5.2.x** on PP_2455 and PP_2456.
4. Remove the spurious **GO:0016787 (hydrolase)** from PP_2456 (a permease).
5. Keep *rbsR* (PP_2457) and *nuh* (PP_2460) documented as **adjacent-but-outside-module** (regulation and feeder, respectively).
6. No new module document or new GO term request appears necessary; existing GO terms for ABC ribose transport, ribokinase, and D-ribose pyranase suffice.

---

## 7. Genes to Promote to Full Review

| Gene | Locus | Why promote |
|---|---|---|
| *rbsD* | PP_2459 | Anchor of step 2; reviewed entry — confirm EC 5.4.99.62 and that it is the intended module gene |
| *rbsK* | PP_2458 | Anchor of step 3; confirm ribokinase EC 2.7.1.15 |
| *rbsB* | PP_2454 | Import specificity determinant; verify ribose-binding assignment vs paralogs |
| *rbsA* / *rbsC* | PP_2455 / PP_2456 | Fix legacy EC (PP_2455/2456) and spurious hydrolase GO (PP_2456) |
| paralog cluster | PP_2757–PP_2761 (esp. PP_2759 RBSA_PSEPK) | Resolve over-annotation; determine true substrate; decide whether it contributes any ribose import capacity |

Highest priority for `fetch-gene` promotion: **PP_2759 (RBSA_PSEPK)** and **PP_2454 (rbsB)**, because they jointly determine whether KT2440 has one or two ribose import routes and whether the reviewed paralog annotation is trustworthy.

---

## 8. Evidence Base and Key References

The module conclusions rest primarily on **genome/proteome annotation and cross-species homology**, not direct KT2440 phenotyping. The supporting literature:

- **[PMID: 10941799](https://pubmed.ncbi.nlm.nih.gov/10941799/)** — *Ribose utilization in Lactobacillus sakei: analysis of the regulation of the rbs operon and putative involvement of a new transporter.* Establishes the canonical *rbsD/rbsK/rbsR* gene set and demonstrates by mutagenesis that *rbsK* (ribokinase) disruption impairs growth on ribose and *rbsR* is the repressor. It also documents lineage-specific variation — *L. sakei* lacks *rbsABC* and instead uses an RbsU/GltA-like transporter — a direct reminder that **import machinery is the most variable part of the module** and that a "ribose operon" need not carry an ABC importer. This supports treating KT2440's import step (and its paralog ambiguity) with more caution than the conserved cytoplasmic enzymes. *Transfer to KT2440: weak/indirect for transporter identity; conceptually important for expecting import-step variability.*

- **[PMID: 20807680](https://pubmed.ncbi.nlm.nih.gov/20807680/)** — *Monitoring differences in gene expression levels and PHA production in Pseudomonas putida KT2440 grown on different carbon sources.* Same-strain study confirming KT2440's metabolic versatility and that ABC transporter genes are among the carbon-source-responsive loci. It did **not** test ribose, so it provides context (KT2440 regulates sugar ABC transporters by carbon source) but **no direct confirmation** of *rbs* operon function. *Transfer: direct organism, but not the pathway.*

- **[PMID: 17827293](https://pubmed.ncbi.nlm.nih.gov/17827293/)** — *Modulation of glucose transport causes preferential utilization of aromatic compounds in Pseudomonas putida CSV86.* Illustrates that periplasmic sugar-binding proteins in *P. putida* can be specific (a 43-kDa glucose-binding protein) and closely resemble KT2440 sugar ABC transporters. Reinforces that **binding-protein specificity is the key discriminator among paralogous sugar ABC systems** — the exact question raised by the PP_2757–2761 cluster. *Transfer: closely related strain; supportive of the specificity-focused curation approach.*

---

## 9. Limitations and Knowledge Gaps

1. **No direct KT2440 experiments.** No growth-on-ribose, transport-assay, or enzyme-activity data specific to KT2440 were found. All step assignments are homology/annotation-based (RbsD reviewed status being the strongest single anchor).
2. **Crude identity scoring.** The Needleman–Wunsch comparisons used a simple ±1 scheme without a substitution matrix, so binding-protein specificity calls (RbsB vs XylF vs LsrB) are indicative, not definitive.
3. **Binding-protein cross-reactivity.** Periplasmic SBPs for pentoses/AI-2 are structurally similar; global identity cannot conclusively assign ligand specificity for PP_2454, PP_2757, or PP_2758.
4. **Paralog function unknown.** Whether PP_2757–2761 imports ribose, another pentose, AI-2, or a broader set of sugars is unresolved; its reviewed EC/annotation may be over-propagated.
5. **Regulatory/feeder linkage untested.** The functional coupling of *rbsR* regulation and *nuh*-derived ribose to the operon is inferred from gene context, not measured.

---

## 10. Proposed Follow-up Experiments and Actions

**Bioinformatic (immediate, low cost):**
- Re-run binding-protein comparisons with BLAST/HMMER against curated SBP families (Pfam PF13407/Peripla_BP_4, ribose vs AI-2 vs xylose) to firm up specificity calls for PP_2454, PP_2757, PP_2758.
- Structural modeling (AlphaFold) of PP_2454, PP_2757, PP_2758 binding pockets and docking of D-ribose vs autoinducer-2 to discriminate the paralog cluster's ligand.
- Synteny/operon-context analysis across sequenced *P. putida* strains to test whether PP_2757–2761 is consistently ribose-labeled or variably annotated.

**Experimental (definitive):**
- Growth assays of KT2440 wild-type and single-cluster knockouts (Δ*rbsBAC* [PP_2454–2456] vs Δ[PP_2757–2761]) on D-ribose as sole carbon source to determine which cluster is required for ribose uptake.
- RT-qPCR / RNA-seq of the *rbs* operon under ribose induction to confirm RbsR-dependent regulation and operon expression.
- Enzyme assays: recombinant RbsK (PP_2458) ribokinase and RbsD (PP_2459) pyranase activity to convert reviewed annotation into direct evidence for KT2440.

**Curation (now):**
- Apply the six curation actions in Section 6 (attach import to operon, flag paralog, fix EC/GO, document adjacent genes).
- Promote PP_2759 and PP_2454 to full `fetch-gene` review.

---

*Prepared from a 3-iteration autonomous review. Confidence: steps 2 and 3 (RbsD pyranase, RbsK ribokinase) — high; step 1 (RbsABC import) — moderate-to-high for the operon, uncertain for the paralog cluster. All evidence is homology/annotation-based; direct KT2440 phenotyping is the key outstanding gap.*


## Artifacts

- [OpenScientist final report](PSEPK__bacterial_ribose_uptake_and_entry__rbs-locus-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__bacterial_ribose_uptake_and_entry__rbs-locus-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:20807680
2. PMID:10941799
3. PMID:17827293