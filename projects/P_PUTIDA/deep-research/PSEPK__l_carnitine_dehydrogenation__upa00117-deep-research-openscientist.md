---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T14:08:36.031320'
end_time: '2026-07-11T14:16:46.912453'
duration_seconds: 490.88
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: L-carnitine dehydrogenation
  module_summary: A Pseudomonas putida KT2440 UniPathway UPA00117 module for the NAD(+)-dependent
    oxidation of L-carnitine to 3-dehydrocarnitine. The local UniPathway bucket contains
    lcdH/PP_0302/Q88R32, a reviewed UniProtKB L-carnitine dehydrogenase entry with
    EC 1.1.1.108 and Rhea:RHEA:19265. This seed treats UPA00117 as the dehydrogenase
    step in carnitine catabolism rather than the full downstream utilization route
    for the 3-dehydrocarnitine product.
  module_outline: "- L-carnitine dehydrogenation\n  - 1. NAD(+)-dependent L-carnitine\
    \ oxidation\n  - LcdH L-carnitine dehydrogenation\n    - lcdH: L-carnitine dehydrogenase\
    \ (molecular player: PSEPK lcdH; activity or role: carnitine 3-dehydrogenase activity)"
  module_connections: No explicit connections.
  pathway_query: UPA00117
  pathway_id: UPA00117
  pathway_name: UniPathway UPA00117
  pathway_source: UniPathway
  pathway_context: 'Resolved local bucket unipathway:UPA00117 with 1 primary genes;
    module area: unipathway.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '1'
  candidate_genes: '- lcdH: PP_0302 | Q88R32 | L-carnitine dehydrogenase (CDH) (L-CDH)
    (EC 1.1.1.108) (EC 1.1.1.108; primary bucket unipathway:UPA00117)'
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__l_carnitine_dehydrogenation__upa00117-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__l_carnitine_dehydrogenation__upa00117-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

L-carnitine dehydrogenation in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: UPA00117
- Resolved ID: UPA00117
- Resolved name: UniPathway UPA00117
- Source: UniPathway

Resolved local bucket unipathway:UPA00117 with 1 primary genes; module area: unipathway.

## Candidate Genes From Local Metadata

Candidate gene count: 1

- lcdH: PP_0302 | Q88R32 | L-carnitine dehydrogenase (CDH) (L-CDH) (EC 1.1.1.108) (EC 1.1.1.108; primary bucket unipathway:UPA00117)

## Generic Module Context

### Working Scope

A Pseudomonas putida KT2440 UniPathway UPA00117 module for the NAD(+)-dependent oxidation of L-carnitine to 3-dehydrocarnitine. The local UniPathway bucket contains lcdH/PP_0302/Q88R32, a reviewed UniProtKB L-carnitine dehydrogenase entry with EC 1.1.1.108 and Rhea:RHEA:19265. This seed treats UPA00117 as the dehydrogenase step in carnitine catabolism rather than the full downstream utilization route for the 3-dehydrocarnitine product.

### Provisional Biological Outline

- L-carnitine dehydrogenation
  - 1. NAD(+)-dependent L-carnitine oxidation
  - LcdH L-carnitine dehydrogenation
    - lcdH: L-carnitine dehydrogenase (molecular player: PSEPK lcdH; activity or role: carnitine 3-dehydrogenase activity)

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

# Module Review: L-carnitine dehydrogenation (UniPathway UPA00117) in *Pseudomonas putida* KT2440

**Target:** PSEPK / *P. putida* KT2440 (NCBI taxon 160488, proteome UP000000556)
**Bucket:** unipathway:UPA00117 — NAD(+)-dependent oxidation of L-carnitine to 3-dehydrocarnitine
**Candidate gene:** lcdH / PP_0302 / Q88R32 (L-CDH, EC 1.1.1.108)

---

## 1. Executive summary

The scoped UPA00117 step — NAD(+)-dependent oxidation of L-carnitine to 3-dehydrocarnitine (Rhea RHEA:19265, EC 1.1.1.108) — is **COVERED** in *P. putida* KT2440 by the single candidate gene **lcdH/PP_0302 (Q88R32)**. Confidence is **high**, supported by three converging lines of evidence: (i) a specific KEGG orthology assignment K17735 "carnitine 3-dehydrogenase" (not the generic fatty-acid β-oxidation KO); (ii) membership in the L-carnitine dehydrogenase subfamily of the 3-hydroxyacyl-CoA dehydrogenase family; and (iii) location within a dedicated carnitine-catabolism gene cluster (transporter + regulator + downstream cleavage enzymes) that mirrors the experimentally validated *P. aeruginosa* carnitine operon.

The main caveat is that there is **no direct biochemical or genetic characterization of PP_0302 itself** — the UniProt entry is protein-existence level 3 ("Inferred from homology"), with the genome paper as its only reference. However, direct enzymology exists for the carnitine dehydrogenase of *P. putida* strain IFP 206 (same species), giving strong same-species transfer support. No module revision is needed; the single-step bucket is satisfiable and correctly bounded.

## 2. Target-organism pathway definition

- **Included (scoped UPA00117):** the *single* enzymatic reaction L-carnitine + NAD(+) → 3-dehydrocarnitine + NADH + H(+). This is a carnitine-*catabolic* (degradative) dehydrogenase step, not carnitine biosynthesis and not the CoA-dependent CaiB/CaiD carnitine racemase/dehydratase (anaerobic *Enterobacteriaceae*) route.
- **Kept separate (neighboring pathways / broad maps):**
  - Downstream carnitine catabolism: 3-dehydrocarnitine → glycine betaine → dimethylglycine → sarcosine → glycine (a distinct, larger pathway; genomically present in KT2440 but outside this bucket).
  - Glycine betaine biosynthesis/osmoprotection (choline → GB) — shares the GB metabolite node but is a different process.
  - Fatty-acid β-oxidation (EC 1.1.1.35, 3-hydroxyacyl-CoA dehydrogenase / FadB) — same protein *superfamily*, different substrate; a classic over-propagation trap.
  - Anaerobic carnitine metabolism (CaiTABCDE, crotonobetaine/γ-butyrobetaine) — not this pathway.
- **Alternate names / DB definitions:** L-carnitine dehydrogenase = carnitine 3-dehydrogenase = carnitine:NAD+ oxidoreductase; EC 1.1.1.108; Rhea RHEA:19265; KO K17735; UniProt PATHWAY "Amine and polyamine metabolism; carnitine metabolism"; gene symbol *lcdH* (also *cdh* in some *Pseudomonas* literature).

## 3. Expected step model

UPA00117 as seeded is a **one-step module**:

| Step | Reaction | Expected enzyme | Status in KT2440 |
|------|----------|-----------------|------------------|
| S1. L-carnitine dehydrogenation | L-carnitine + NAD⁺ → 3-dehydrocarnitine + NADH + H⁺ | Carnitine 3-dehydrogenase (EC 1.1.1.108, K17735) | **Covered** by PP_0302 |

There are no additional expected internal steps within this bucket ("No explicit connections"). The provisional outline is accurate: the module is the dehydrogenase step only, not the full utilization route.

## 4. Candidate genes and evidence

**lcdH / PP_0302 / Q88R32 — L-carnitine dehydrogenase (EC 1.1.1.108)**

- **Likely role:** genuine carnitine 3-dehydrogenase catalyzing step S1. High confidence.
- **Evidence type & strength:**
  - *Sequence/annotation:* 321 aa, 34.6 kDa/subunit, annotated homodimer (~69 kDa). Matches the biochemically characterized *P. putida* IFP 206 enzyme (homodimer, ~62 kDa, NAD⁺- and L-carnitine-specific, EC 1.1.1.108; Goulas 1988, PMID 3058208) — **strong same-species transfer**.
  - *Ortholog specificity:* KO **K17735** (carnitine 3-dehydrogenase) is substrate-specific, distinguishing PP_0302 from generic 3-hydroxyacyl-CoA dehydrogenases (fadB/K01825). Family: 3-hydroxyacyl-CoA dehydrogenase family, **L-carnitine dehydrogenase subfamily** (Pfam PF02737 NAD-binding + PF00725 C-terminal; COG1250; PANTHER PTHR48075:SF5).
  - *Genomic context (strong):* PP_0302 lies in a carnitine-catabolism cluster — PP_0301 betainyl-CoA thiolase, PP_0303 dehydrocarnitine cleavage enzyme, PP_0304 carnitine ABC-transporter periplasmic component, PP_0305 regulator CdhR, PP_0298 AraC-family regulator. This synteny parallels the transposon-validated *P. aeruginosa* carnitine operon (PA5388–PA5384 + PA1999–PA2000; Wargo & Hogan 2009, PMID 19406895).
- **Curation-relevant caveats:**
  - UniProt protein existence **level 3 (inferred from homology)**; no direct KT2440 assay or knockout — function is *predicted*, not *demonstrated*, for this specific ORF.
  - EC 1.1.1.108 and the Pfam domains belong to a broad NAD-dependent dehydrogenase superfamily; the confident call depends on the specific KO + subfamily + operon context, not on Pfam alone.
  - Rhea/EC mapping is exact and appropriate; no over-broad GO expected here (GO:0008859 carnitine 3-dehydrogenase activity is specific and correct).

## 5. Gaps, ambiguities, and likely over-annotations

- **No gap within the bucket:** S1 is covered; the module is satisfiable.
- **Paralog ambiguity — RESOLVED:** a KEGG ortholog check confirms PP_0302 is the **sole** carnitine-3-dehydrogenase (K17735) gene in KT2440; the generic 3-hydroxyacyl-CoA dehydrogenase KO K00022 has 0 KT2440 genes, and the fatty-acid β-oxidation *fadB* KO K01825 maps to a **separate** locus (PP_2136, not PP_0302). Thus there is no competing carnitine-dehydrogenase paralog, and the superfamily's β-oxidation activity is carried by a distinct gene. The step assignment to PP_0302 is unambiguous at the ortholog level.
- **Over-annotation risk elsewhere, not here:** the reverse risk (a true fadB being called lcdH) is the more common error in this family; PP_0302's cluster context argues against it being a mis-annotation.
- **Scope creep risk:** the downstream carnitine→glycine betaine→glycine genes (PP_0301, PP_0303, transporter PP_0304, regulator PP_0305) are present but must **not** be folded into UPA00117; they belong to separate downstream modules. Keeping the bucket single-step is correct.
- **Physiology unverified:** whether KT2440 actually grows on L-carnitine as C/N source is not directly documented here (demonstrated for *P. aeruginosa*, and the complete cluster in KT2440 makes it likely). This is an open question, not a module defect.

## 6. Module and GO-curation recommendations

- **Step S1 (L-carnitine dehydrogenation): mark `covered`** via lcdH/PP_0302. Evidence code ≈ inferred by sequence/orthology + genomic context (ISS/IBA-type), *not* experimental for this ORF.
- **Module boundaries:** correct as scoped; **no `module_needs_revision`**. Do not expand UPA00117 to include downstream GB-forming steps.
- **GO annotation:** GO:0008859 (carnitine 3-dehydrogenase activity) and GO:0009437 (carnitine metabolic process) for PP_0302 are appropriate and specific; no new GO term request needed.
- **No `gap`, `candidate_uncertain`, or `not_expected_in_target_taxon`** flags required for the single scoped step. If a broader carnitine-utilization module is later created, PP_0301/PP_0303/PP_0304/PP_0305 would populate its downstream/transport/regulatory steps.

## 7. Genes to promote to full review

- **PP_0302 / lcdH (Q88R32):** promote to full `fetch-gene` review to (a) record that it is confirmed as the **sole K17735 copy** in KT2440 (fadB/β-oxidation is the separate PP_2136), (b) attach the same-species biochemical reference (IFP 206) and the *P. aeruginosa* operon precedent, and (c) upgrade the evidence narrative from bare homology to homology + unique-ortholog + synteny. This is the only gene in the bucket and warrants a curated record.
- *(Context only, not in this bucket)* PP_0301, PP_0303, PP_0304, PP_0305 merit review when the downstream carnitine-catabolism / GB module is curated.

## 8. Key references

- Goulas P. (1988) *Purification and properties of carnitine dehydrogenase from Pseudomonas putida.* PMID **3058208**. — Direct same-species biochemistry: EC 1.1.1.108, L-carnitine→3-dehydrocarnitine, NAD⁺-specific, homodimer.
- Wargo MJ, Hogan DA. (2009) *Identification of genes required for Pseudomonas aeruginosa carnitine catabolism.* PMID **19406895**. — Genetic definition of a *Pseudomonas* carnitine operon (carnitine→3-dhc→glycine betaine), supporting the KT2440 cluster interpretation.
- Nelson KE et al. (2002) Complete genome sequence of *P. putida* KT2440. PMID **12534463**. — Source annotation of PP_0302/lcdH.
- UniProtKB **Q88R32** (LCDH_PSEPK); KEGG **ppu:PP_0302** / KO **K17735**; Rhea **RHEA:19265**; UniPathway **UPA00117**.

---

### Uncertainty ledger
- **Direct for KT2440:** genome annotation, gene-cluster synteny, KO/Rhea/EC mapping.
- **Same-species transfer (strong):** biochemistry from *P. putida* IFP 206.
- **Related-species transfer (moderate–strong):** operon logic and carnitine-catabolism physiology from *P. aeruginosa*.
- **Inferred/unverified:** actual enzymatic assay of PP_0302, KT2440 growth on carnitine. (Note: targeted PubMed searches returned no KT2440-specific carnitine growth, knockout, or transcriptomic study — the assignment therefore rests on homology + unique-ortholog + operon synteny, with same-species biochemistry from *P. putida* IFP 206 and genetic validation from *P. aeruginosa* as the strongest transferable support.)
- **Resolved:** absence of confounding paralogs (PP_0302 is the sole K17735 gene; fadB is the separate PP_2136).

### Curation decision (one line)
UPA00117 step **S1 = `covered`** by lcdH/PP_0302; module boundaries correct (single-step); no new module or GO-term request needed; promote PP_0302 to full `fetch-gene` review. Sole residual gap = no direct KT2440 enzyme assay/knockout.


## Artifacts

- [OpenScientist final report](PSEPK__l_carnitine_dehydrogenation__upa00117-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__l_carnitine_dehydrogenation__upa00117-deep-research-openscientist_artifacts/final_report.pdf)