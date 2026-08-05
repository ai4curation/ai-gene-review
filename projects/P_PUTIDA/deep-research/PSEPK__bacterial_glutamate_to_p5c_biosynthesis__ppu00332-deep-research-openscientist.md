---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-16T10:47:21.576021'
end_time: '2026-07-16T11:03:07.792176'
duration_seconds: 946.22
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Bacterial glutamate-to-P5C branch of proline biosynthesis
  module_summary: Species-neutral bacterial module for the two-enzyme conversion of
    L-glutamate to L-glutamate 5-semialdehyde, which cyclizes to 1-pyrroline-5-carboxylate
    (P5C), during proline biosynthesis. ProB phosphorylates L-glutamate to L-glutamyl
    5-phosphate, and ProA reduces that acyl phosphate intermediate to L-glutamate
    5-semialdehyde using NADPH. This module deliberately stops before the terminal
    P5C reductase step that makes L-proline.
  module_outline: "- Bacterial glutamate-to-P5C branch of proline biosynthesis\n \
    \ - 1. glutamate phosphorylation\n  - ProB glutamate 5-kinase\n    - proB: glutamate\
    \ 5-kinase (molecular player: bacterial glutamate 5-kinase family; activity or\
    \ role: glutamate 5-kinase activity)\n  - 2. gamma-glutamyl phosphate reduction\
    \ to P5C precursor\n  - ProA gamma-glutamyl phosphate reductase\n    - proA: gamma-glutamyl\
    \ phosphate reductase (molecular player: bacterial gamma-glutamyl phosphate reductase\
    \ family; activity or role: glutamate-5-semialdehyde dehydrogenase activity)"
  module_connections: '- ProB glutamate 5-kinase feeds into ProA gamma-glutamyl phosphate
    reductase: ProB produces L-glutamyl 5-phosphate, the substrate reduced by ProA
    to L-glutamate 5-semialdehyde/P5C.'
  pathway_query: ppu00332
  pathway_id: ppu00332
  pathway_name: Carbapenem biosynthesis
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00332 with 2 primary genes; module
    area: other_kegg_pathway.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '2'
  candidate_genes: '- proB: PP_0691 | Q88Q07 | Glutamate 5-kinase (EC 2.7.2.11) (Gamma-glutamyl
    kinase) (GK) (EC 2.7.2.11; primary bucket kegg:ppu00332)

    - proA: PP_4811 | Q88DL4 | Gamma-glutamyl phosphate reductase (GPR) (EC 1.2.1.41)
    (Glutamate-5-semialdehyde dehydrogenase) (Glutamyl-gamma-semialdehyde dehydrogenase)
    (GSA dehydrogenase) (EC 1.2.1.41; primary bucket kegg:ppu00332)'
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
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
  path: PSEPK__bacterial_glutamate_to_p5c_biosynthesis__ppu00332-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__bacterial_glutamate_to_p5c_biosynthesis__ppu00332-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Bacterial glutamate-to-P5C branch of proline biosynthesis in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00332
- Resolved ID: ppu00332
- Resolved name: Carbapenem biosynthesis
- Source: KEGG

Resolved local bucket kegg:ppu00332 with 2 primary genes; module area: other_kegg_pathway.

## Candidate Genes From Local Metadata

Candidate gene count: 2

- proB: PP_0691 | Q88Q07 | Glutamate 5-kinase (EC 2.7.2.11) (Gamma-glutamyl kinase) (GK) (EC 2.7.2.11; primary bucket kegg:ppu00332)
- proA: PP_4811 | Q88DL4 | Gamma-glutamyl phosphate reductase (GPR) (EC 1.2.1.41) (Glutamate-5-semialdehyde dehydrogenase) (Glutamyl-gamma-semialdehyde dehydrogenase) (GSA dehydrogenase) (EC 1.2.1.41; primary bucket kegg:ppu00332)

## Generic Module Context

### Working Scope

Species-neutral bacterial module for the two-enzyme conversion of L-glutamate to L-glutamate 5-semialdehyde, which cyclizes to 1-pyrroline-5-carboxylate (P5C), during proline biosynthesis. ProB phosphorylates L-glutamate to L-glutamyl 5-phosphate, and ProA reduces that acyl phosphate intermediate to L-glutamate 5-semialdehyde using NADPH. This module deliberately stops before the terminal P5C reductase step that makes L-proline.

### Provisional Biological Outline

- Bacterial glutamate-to-P5C branch of proline biosynthesis
  - 1. glutamate phosphorylation
  - ProB glutamate 5-kinase
    - proB: glutamate 5-kinase (molecular player: bacterial glutamate 5-kinase family; activity or role: glutamate 5-kinase activity)
  - 2. gamma-glutamyl phosphate reduction to P5C precursor
  - ProA gamma-glutamyl phosphate reductase
    - proA: gamma-glutamyl phosphate reductase (molecular player: bacterial gamma-glutamyl phosphate reductase family; activity or role: glutamate-5-semialdehyde dehydrogenase activity)

### Known Relationships Among Steps

- ProB glutamate 5-kinase feeds into ProA gamma-glutamyl phosphate reductase: ProB produces L-glutamyl 5-phosphate, the substrate reduced by ProA to L-glutamate 5-semialdehyde/P5C.

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

# Module Review: Bacterial glutamate→P5C branch of proline biosynthesis in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK, NCBI taxon 160488, proteome UP000000556)
**Resolved bucket:** `kegg:ppu00332` ("Carbapenem biosynthesis") — see §5, this label is a precursor-overlap artifact.
**Candidate genes:** proB (PP_0691 / Q88Q07), proA (PP_4811 / Q88DL4)

---

## 1. Executive summary

- **The module is SATISFIED.** Both expected steps of the glutamate→L-glutamate-5-semialdehyde/P5C branch are encoded in KT2440 by high-confidence, reviewed (Swiss-Prot) genes: **proB (PP_0691)** = glutamate 5-kinase (EC 2.7.2.11) and **proA (PP_4811)** = γ-glutamyl phosphate reductase (EC 1.2.1.41). Both are single-copy for their KEGG ortholog and map to UniPathway UPA00098 (L-proline biosynthesis), steps 1 and 2.
- **The resolved pathway name is misleading.** KEGG `ppu00332` "Carbapenem biosynthesis" contains **only** proB and proA; the carbapenem-committed enzymes (carA K21284, carB K21283, carC K21298) are **entirely absent** from KT2440. proB/proA appear in that map solely because pyrroline-5-carboxylate (P5C) is a shared precursor. The correct biological home is **proline biosynthesis** (KEGG map00330 / module M00015; UniPathway UPA00098). → Flag the bucket `module_needs_revision`.
- **The module boundary is correct for this organism.** KEGG module M00015 (`((K00931 K00147),K12657) K00286`) shows the bacterial two-gene branch (proB+proA) is the *sole* Glu→P5C route in KT2440 (no eukaryotic bifunctional P5CS, K12657, is present). The terminal P5C reductase **proC (PP_5095)** is present but is intentionally outside module scope.
- **Evidence type:** Direct KT2440 gene/genome evidence (UniProt Swiss-Prot rule-based annotation, KEGG genome). Enzyme mechanism/regulation is transferred from well-studied *E. coli* orthologs (strong transfer; conserved family, HAMAP rules). No direct KT2440 enzymology was found.

---

## 2. Target-organism pathway definition

**Process included (module scope):** the two committed cytoplasmic reactions converting L-glutamate to L-glutamate-5-semialdehyde (GSA), which non-enzymatically cyclizes to Δ¹-pyrroline-5-carboxylate (P5C):

1. **L-glutamate + ATP → L-glutamyl-5-phosphate + ADP** (glutamate 5-kinase, ProB, EC 2.7.2.11; Rhea:14877)
2. **L-glutamyl-5-phosphate + NADPH + H⁺ → L-glutamate-5-semialdehyde + Pi + NADP⁺** (γ-glutamyl phosphate reductase, ProA, EC 1.2.1.41; Rhea:19541)

**Deliberately excluded:** the terminal reduction **P5C + NADPH → L-proline** (P5C reductase, ProC, EC 1.5.1.2), encoded by PP_5095 in KT2440.

**Neighboring pathways/maps to keep SEPARATE:**
- **Proline catabolism (utilization):** bifunctional **PutA (PP_4947, K13821)** oxidizes proline → P5C → glutamate — the *reverse/degradative* direction; not part of biosynthesis.
- **Ornithine→proline bypass:** ornithine cyclodeaminase **ocd (PP_3533, K01750)** makes proline from ornithine *without* traversing Glu→P5C.
- **Arginine biosynthesis:** N-acetylglutamate kinase **argB (PP_5289, K00930)** and N-acetyl-γ-glutamyl-phosphate reductase **argC (PP_0432, PP_3633, K00145)** are the same-superfamily paralogs of proB/proA (see §5).
- **Broad overview maps** (ppu01100 Metabolic pathways, ppu01110 Biosynthesis of secondary metabolites, ppu01230 Biosynthesis of amino acids) contain proB/proA but should not define the module.
- **Carbapenem biosynthesis (ppu00332):** not a real pathway in KT2440 (§5).

**Alternate names / database definitions:** ProB = glutamate 5-kinase = γ-glutamyl kinase (GK); ProA = γ-glutamyl phosphate reductase (GPR) = glutamate-5-semialdehyde dehydrogenase (GSA dehydrogenase). UniPathway UPA00098 "L-proline biosynthesis"; KEGG module M00015 "Proline biosynthesis, glutamate => proline"; MetaCyc PROSYN-PWY.

**Genomic organization (species-specific):** In KT2440 the three pro genes are **unlinked** — proB PP_0691 at ~0.80 Mb (+ strand), proA PP_4811 at ~5.47 Mb (− strand), proC PP_5095 at ~5.82 Mb (+ strand) — i.e., proB and proA are ~4.67 Mb apart on opposite strands. This differs from the co-transcribed **proBA operon** of *E. coli*/*Serratia* (PMID 1851803). The ProB→ProA metabolic relationship holds, but operon-/synteny-based co-regulation or joint annotation transfer must **not** be assumed for this taxon; each gene stands on its own evidence.

---

## 3. Expected step model

| # | Step | Enzyme (family) | KO | EC | KT2440 gene | Status |
|---|------|-----------------|----|----|-------------|--------|
| 1 | Glutamate phosphorylation | Glutamate 5-kinase / ProB (amino-acid-kinase AAK family + PUA domain) | K00931 | 2.7.2.11 | **PP_0691** (Q88Q07) | **covered** |
| 2 | γ-Glutamyl phosphate reduction → GSA/P5C | γ-Glutamyl phosphate reductase / ProA (aldehyde-dehydrogenase family) | K00147 | 1.2.1.41 | **PP_4811** (Q88DL4) | **covered** |
| (3) | P5C → L-proline (terminal, out of scope) | P5C reductase / ProC | K00286 | 1.5.1.2 | PP_5095 | present (excluded from module) |

No expected in-scope step is missing. No lineage-specific replacement of steps 1–2 exists (no bifunctional P5CS K12657).

---

## 4. Candidate genes and evidence

### proB — PP_0691 (UniProt Q88Q07, PROB_PSEPK) — HIGH confidence
- **Role:** Glutamate 5-kinase (EC 2.7.2.11), committed first step; catalyzes L-glutamate + ATP → L-glutamyl-5-phosphate (Rhea:14877). 372 aa.
- **Evidence:** Reviewed Swiss-Prot; annotation via HAMAP rule MF_00456 (PE=3, inferred from homology). Single gene for K00931 in KT2440; UniPathway UPA00098:UER00359. RefSeq WP_003247458.1; BioCyc PPUT160488 monomer.
- **Domain architecture:** AAK catalytic domain (Pfam PF00696) + C-terminal PUA regulatory domain (Pfam PF01472). In *E. coli* the AAK domain performs catalysis and proline feedback inhibition; the PUA domain modulates Mg²⁺ requirement and proline-triggered oligomerization (PMID 17321544, 16337196). **Strong transfer** to KT2440 (conserved domain set).
- **Curation caveat:** activity is inferred (rule-based), not measured in KT2440. The AAK fold is shared with arginine-pathway argB (NAGK); however KO and domain context resolve them cleanly. Proline feedback inhibition is expected but unverified in KT2440 (relevant if the module is used for flux/metabolic-engineering reasoning).

### proA — PP_4811 (UniProt Q88DL4, PROA_PSEPK) — HIGH confidence
- **Role:** γ-Glutamyl phosphate reductase (EC 1.2.1.41); NADPH-dependent reduction of L-glutamyl-5-phosphate → L-glutamate-5-semialdehyde (Rhea:19541). 423 aa.
- **Evidence:** Reviewed Swiss-Prot; HAMAP rule MF_00412 (PE=3). Single gene for K00147; UniPathway UPA00098:UER00360. RefSeq WP_004576854.1.
- **Domain architecture:** aldehyde-dehydrogenase domain (Pfam PF00171); GPR-specific InterPro IPR000965/IPR012134.
- **Curation caveat:** shares the aldehyde-DH fold with arginine-pathway argC; KO/InterPro resolve them. Activity inferred, not directly measured in KT2440.

**GO annotations (both, IEA/UniRule):** proB GO:0004349 (glutamate 5-kinase activity); proA GO:0004350 (glutamate-5-semialdehyde dehydrogenase activity); both GO:0055129 (L-proline biosynthetic process). proB also carries GO:0003723 (RNA binding, from the PUA domain via InterPro) — a **broad/likely-spurious** transfer for a biosynthetic kinase; treat with caution.

---

## 5. Gaps, ambiguities, and likely over-annotations

1. **Bucket mislabel (highest priority).** `kegg:ppu00332` "Carbapenem biosynthesis" is **not a real pathway in KT2440**: it contains only proB/proA, and all carbapenem-committed genes (carA/carB/carC) are absent. This is a KEGG map artifact driven by the shared P5C precursor. → **module_needs_revision**; re-anchor the module under proline biosynthesis (map00330 / M00015 / UPA00098). Carbapenem-specific steps → **not_expected_in_target_taxon**.
2. **Paralog ambiguity (low actual risk).** proB↔argB (PP_5289; AAK family) and proA↔argC (PP_0432, PP_3633; aldehyde-DH family) are homologous, but are cleanly resolved by **distinct EC numbers and KOs**: argB = acetylglutamate kinase EC 2.7.2.8 (K00930) vs proB EC 2.7.2.11 (K00931); argC = N-acetyl-γ-glutamyl-phosphate reductase EC 1.2.1.38 (K00145) vs proA EC 1.2.1.41 (K00147). Since they differ at the 4th EC digit and carry different KOs (plus proB's diagnostic PUA domain), EC/KO-based curation will not cross-assign them — over-propagation risk is genuinely low. (Nuance: KT2440 has two argC-family copies, PP_0432 and PP_3633 [latter "putative"], a duplication within the *arginine* branch, irrelevant to this module.)
3. **Broad GO term.** proB's GO:0003723 (RNA binding) is a PUA-domain InterPro side-effect, not a demonstrated function; potentially over-propagated.
4. **Direction/utilization confusion.** PP_4947 (PutA) and PP_3533 (ocd) are proline *catabolism* and an *ornithine bypass*; they must not be counted toward this biosynthetic module.
5. **No direct enzymology.** All KT2440 evidence is rule/homology-based (PE=3); no target-strain kinetic or knockout data was located. This is the main evidence gap, though transfer confidence is high given deep conservation.

---

## 6. Module and GO-curation recommendations

| Item | Recommendation |
|------|----------------|
| Step 1 (ProB glutamate 5-kinase) | **covered** — PP_0691 |
| Step 2 (ProA γ-glutamyl phosphate reductase) | **covered** — PP_4811 |
| Terminal P5C reductase (proC) | out of module scope; present as PP_5095 (note for completeness) |
| Carbapenem-committed steps | **not_expected_in_target_taxon** (carA/carB/carC absent) |
| Bucket `kegg:ppu00332` | **module_needs_revision** — relabel/re-anchor to proline biosynthesis (map00330 / M00015 / UPA00098); "Carbapenem biosynthesis" is a shared-precursor artifact |
| Module boundaries | **correct** as written (Glu→GSA/P5C, stopping before ProC); matches the bacterial `(K00931 K00147)` arm of M00015 |
| New GO term requests | none needed; existing GO:0004349, GO:0004350, GO:0055129 are adequate. Consider deprecating/flagging proB GO:0003723 (RNA binding) as likely over-propagated |

No new module document is required beyond correcting the pathway anchor. If the curation system tracks the terminal step, a sibling module (P5C→proline, ProC/PP_5095) could be added, but it is out of the present module's scope.

---

## 7. Genes to promote to full `fetch-gene` review

- **PP_0691 (proB)** — promote. Rationale: it is the committed, feedback-regulated control point; confirm domain architecture (AAK+PUA), single-copy status, and that GO:0003723 is not carried forward. Low ambiguity but high pathway importance.
- **PP_4811 (proA)** — promote. Rationale: confirm EC 1.2.1.41 assignment vs. argC paralogy; single-copy status.
- **Context genes (review only if module is extended):** PP_5095 (proC, terminal step), PP_5289 (argB paralog), PP_0432/PP_3633 (argC paralogs), PP_4947 (PutA, catabolism), PP_3533 (ocd). These are *not* part of this module but are relevant to keep boundaries clean.

---

## 8. Key references

- Marco-Marín C, et al. *Crystal structure of E. coli glutamate 5-kinase: a novel two-domain (AAK+PUA) architecture; feedback-inhibited by proline/ornithine.* J Mol Biol. 2007. **PMID 17321544**.
- Pérez-Arellano I, Rubio V, Cervera J. *Mapping active-site residues in glutamate-5-kinase: glutamate and proline bind at overlapping sites.* FEBS J. 2006. **PMID 17069808**.
- Pérez-Arellano I, Rubio V, Cervera J. *Dissection of E. coli glutamate 5-kinase: functional impact of PUA-domain deletion.* FEBS Lett. 2005. **PMID 16337196**.
- Omori K, et al. *Serratia marcescens proBA operon: proB (GK) and proA (GPR) organization and proline feedback control.* J Bacteriol. 1991 / Mol Gen Genet 1992. **PMID 1851803**, **PMID 1316937**.
- Fujita T, et al. *Allosteric regulation of γ-glutamyl kinase by proline (tomato tomPRO1).* Plant Physiol. 2003. **PMID 12566437**.
- Database resources (direct KT2440 evidence): UniProt **Q88Q07** (PROB_PSEPK), **Q88DL4** (PROA_PSEPK); KEGG pathway **ppu00332**, module **M00015**; UniPathway **UPA00098** (UER00359/UER00360/UER00361); KEGG orthology K00931/K00147/K00286/K00930/K00145/K13821/K01750.

---

### Uncertainty & species-transfer notes
- **Direct (KT2440):** gene presence, single-copy KO mapping, EC/pathway assignment, absence of carbapenem genes, presence of proC/PutA/ocd/argB/argC — all from KT2440 genome/UniProt records.
- **Transferred (strong):** enzyme mechanism, domain function, proline feedback inhibition — from *E. coli* and other bacteria; family is deeply conserved and covered by HAMAP rules, so transfer to KT2440 is strong though not experimentally confirmed in-strain.
- **Open questions:** Is ProB feedback inhibition operative/measurable in KT2440 (relevant for proline/osmolyte engineering)? Any in-strain knockout/kinetic data? These would elevate evidence from homology-based to direct.


## Artifacts

- [OpenScientist final report](PSEPK__bacterial_glutamate_to_p5c_biosynthesis__ppu00332-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__bacterial_glutamate_to_p5c_biosynthesis__ppu00332-deep-research-openscientist_artifacts/final_report.pdf)