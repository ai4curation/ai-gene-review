---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-08T11:25:09.777253'
end_time: '2026-08-08T11:35:52.453442'
duration_seconds: 642.68
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: hydroxyproline_catabolism
  module_summary: No module YAML was resolved; use the pathway and taxon context.
  module_outline: No module YAML outline available.
  module_connections: No module YAML connections available.
  pathway_query: ppu00470
  pathway_id: ppu00470
  pathway_name: D-Amino acid metabolism
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00470 with 11 primary genes; module
    area: amino_acid_metabolism.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '21'
  candidate_genes: '- murI: PP_0736 | Q88PW2 | Glutamate racemase (EC 5.1.1.3) (EC
    5.1.1.3; primary bucket kegg:ppu00470)

    - PP_1255: PP_1255 | Q88NF6 | Cis-4-hydroxy-D-proline oxidase (EC 1.5.1.-) (EC
    1.5.1.-; primary bucket kegg:ppu00470)

    - PP_1256: PP_1256 | Q88NF5 | 2,5-dioxovalerate dehydrogenase (EC 1.2.1.26) (EC
    1.2.1.26; primary bucket kegg:ppu00040)

    - PP_1257: PP_1257 | Q88NF4 | 1-pyrroline-4-hydroxy-2-carboxylate deaminase (EC
    3.5.4.22) (EC 3.5.4.22; primary bucket kegg:ppu00470)

    - proR: PP_1258 | Q88NF3 | 4-hydroxyproline 2-epimerase (4-hydroxyproline epimerase)
    (4Hyp 2-epimerase) (4HypE) (EC 5.1.1.8) (EC 5.1.1.8; primary bucket kegg:ppu00470)

    - murD: PP_1335 | Q88N78 | UDP-N-acetylmuramoylalanine--D-glutamate ligase (EC
    6.3.2.9) (D-glutamic acid-adding enzyme) (UDP-N-acetylmuramoyl-L-alanyl-D-glutamate
    synthetase) (EC 6.3.2.9; primary bucket kegg:ppu00470)

    - ddlB: PP_1339 | Q88N74 | D-alanine--D-alanine ligase B (EC 6.3.2.4) (D-Ala-D-Ala
    ligase B) (D-alanylalanine synthetase B) (EC 6.3.2.4; primary bucket kegg:ppu01502)

    - lysA-I: PP_2077 | Q88L58 | Diaminopimelate decarboxylase (DAP decarboxylase)
    (DAPDC) (EC 4.1.1.20) (EC 4.1.1.20; primary bucket kegg:ppu00300)

    - dauA: PP_2246 | Q88KP4 | Catabolic D-arginine dehydrogenase, FAD-dependent (EC
    1.4.99.-) (EC 1.4.99.-; primary bucket kegg:ppu00470)

    - ansB: PP_2453 | Q88K39 | Glutaminase-asparaginase (EC 3.5.1.38) (L-ASNase/L-GLNase)
    (L-asparagine/L-glutamine amidohydrolase) (EC 3.5.1.38; primary bucket kegg:ppu00470)

    - PP_2585: PP_2585 | Q88JR4 | 2,5-dioxovalerate dehydrogenase (EC 1.2.1.26) (EC
    1.2.1.26; primary bucket kegg:ppu00040)

    - PP_3602: PP_3602 | Q88GW5 | 2,5-dioxovalerate dehydrogenase (EC 1.2.1.26) (EC
    1.2.1.26; primary bucket kegg:ppu00040)

    - alr: PP_3722 | Q88GJ9 | Broad specificity amino-acid racemase (EC 5.1.1.10)
    (Broad spectrum racemase) (EC 5.1.1.10; primary bucket kegg:ppu00470)

    - dapF__Q88GD4: PP_3790 | Q88GD4 | Diaminopimelate epimerase (DAP epimerase) (EC
    5.1.1.7) (PLP-independent amino acid racemase) (EC 5.1.1.7; primary bucket kegg:ppu00300)

    - PP_4311: PP_4311 | Q88EY9 | D-amino acid dehydrogenase 2 small subunit (EC 1.4.99.6)
    (EC 1.4.99.6; primary bucket kegg:ppu00470)

    - ddlA: PP_4346 | Q88EV6 | D-alanine--D-alanine ligase A (EC 6.3.2.4) (D-Ala-D-Ala
    ligase A) (D-alanylalanine synthetase A) (EC 6.3.2.4; primary bucket kegg:ppu01502)

    - dadA1: PP_4434 | Q88EM0 | D-amino acid dehydrogenase 1 (EC 1.4.99.-) (EC 1.4.99.-;
    primary bucket kegg:ppu00470)

    - lysA-II: PP_5227 | Q88CF4 | Diaminopimelate decarboxylase (DAP decarboxylase)
    (DAPDC) (EC 4.1.1.20) (EC 4.1.1.20; primary bucket kegg:ppu00300)

    - dapF__Q88CF3: PP_5228 | Q88CF3 | Diaminopimelate epimerase (DAP epimerase) (EC
    5.1.1.7) (PLP-independent amino acid racemase) (EC 5.1.1.7; primary bucket kegg:ppu00300)

    - dadX: PP_5269 | Q88CB2 | Alanine racemase, catabolic (EC 5.1.1.1) (EC 5.1.1.1;
    primary bucket kegg:ppu01502)

    - dadA2: PP_5270 | Q88CB1 | D-amino acid dehydrogenase 2 (EC 1.4.99.-) (EC 1.4.99.-;
    primary bucket kegg:ppu00470)'
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
  path: PSEPK__hydroxyproline-catabolism__ppu00470-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__hydroxyproline-catabolism__ppu00470-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

hydroxyproline_catabolism in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00470
- Resolved ID: ppu00470
- Resolved name: D-Amino acid metabolism
- Source: KEGG

Resolved local bucket kegg:ppu00470 with 11 primary genes; module area: amino_acid_metabolism.

## Candidate Genes From Local Metadata

Candidate gene count: 21

- murI: PP_0736 | Q88PW2 | Glutamate racemase (EC 5.1.1.3) (EC 5.1.1.3; primary bucket kegg:ppu00470)
- PP_1255: PP_1255 | Q88NF6 | Cis-4-hydroxy-D-proline oxidase (EC 1.5.1.-) (EC 1.5.1.-; primary bucket kegg:ppu00470)
- PP_1256: PP_1256 | Q88NF5 | 2,5-dioxovalerate dehydrogenase (EC 1.2.1.26) (EC 1.2.1.26; primary bucket kegg:ppu00040)
- PP_1257: PP_1257 | Q88NF4 | 1-pyrroline-4-hydroxy-2-carboxylate deaminase (EC 3.5.4.22) (EC 3.5.4.22; primary bucket kegg:ppu00470)
- proR: PP_1258 | Q88NF3 | 4-hydroxyproline 2-epimerase (4-hydroxyproline epimerase) (4Hyp 2-epimerase) (4HypE) (EC 5.1.1.8) (EC 5.1.1.8; primary bucket kegg:ppu00470)
- murD: PP_1335 | Q88N78 | UDP-N-acetylmuramoylalanine--D-glutamate ligase (EC 6.3.2.9) (D-glutamic acid-adding enzyme) (UDP-N-acetylmuramoyl-L-alanyl-D-glutamate synthetase) (EC 6.3.2.9; primary bucket kegg:ppu00470)
- ddlB: PP_1339 | Q88N74 | D-alanine--D-alanine ligase B (EC 6.3.2.4) (D-Ala-D-Ala ligase B) (D-alanylalanine synthetase B) (EC 6.3.2.4; primary bucket kegg:ppu01502)
- lysA-I: PP_2077 | Q88L58 | Diaminopimelate decarboxylase (DAP decarboxylase) (DAPDC) (EC 4.1.1.20) (EC 4.1.1.20; primary bucket kegg:ppu00300)
- dauA: PP_2246 | Q88KP4 | Catabolic D-arginine dehydrogenase, FAD-dependent (EC 1.4.99.-) (EC 1.4.99.-; primary bucket kegg:ppu00470)
- ansB: PP_2453 | Q88K39 | Glutaminase-asparaginase (EC 3.5.1.38) (L-ASNase/L-GLNase) (L-asparagine/L-glutamine amidohydrolase) (EC 3.5.1.38; primary bucket kegg:ppu00470)
- PP_2585: PP_2585 | Q88JR4 | 2,5-dioxovalerate dehydrogenase (EC 1.2.1.26) (EC 1.2.1.26; primary bucket kegg:ppu00040)
- PP_3602: PP_3602 | Q88GW5 | 2,5-dioxovalerate dehydrogenase (EC 1.2.1.26) (EC 1.2.1.26; primary bucket kegg:ppu00040)
- alr: PP_3722 | Q88GJ9 | Broad specificity amino-acid racemase (EC 5.1.1.10) (Broad spectrum racemase) (EC 5.1.1.10; primary bucket kegg:ppu00470)
- dapF__Q88GD4: PP_3790 | Q88GD4 | Diaminopimelate epimerase (DAP epimerase) (EC 5.1.1.7) (PLP-independent amino acid racemase) (EC 5.1.1.7; primary bucket kegg:ppu00300)
- PP_4311: PP_4311 | Q88EY9 | D-amino acid dehydrogenase 2 small subunit (EC 1.4.99.6) (EC 1.4.99.6; primary bucket kegg:ppu00470)
- ddlA: PP_4346 | Q88EV6 | D-alanine--D-alanine ligase A (EC 6.3.2.4) (D-Ala-D-Ala ligase A) (D-alanylalanine synthetase A) (EC 6.3.2.4; primary bucket kegg:ppu01502)
- dadA1: PP_4434 | Q88EM0 | D-amino acid dehydrogenase 1 (EC 1.4.99.-) (EC 1.4.99.-; primary bucket kegg:ppu00470)
- lysA-II: PP_5227 | Q88CF4 | Diaminopimelate decarboxylase (DAP decarboxylase) (DAPDC) (EC 4.1.1.20) (EC 4.1.1.20; primary bucket kegg:ppu00300)
- dapF__Q88CF3: PP_5228 | Q88CF3 | Diaminopimelate epimerase (DAP epimerase) (EC 5.1.1.7) (PLP-independent amino acid racemase) (EC 5.1.1.7; primary bucket kegg:ppu00300)
- dadX: PP_5269 | Q88CB2 | Alanine racemase, catabolic (EC 5.1.1.1) (EC 5.1.1.1; primary bucket kegg:ppu01502)
- dadA2: PP_5270 | Q88CB1 | D-amino acid dehydrogenase 2 (EC 1.4.99.-) (EC 1.4.99.-; primary bucket kegg:ppu00470)

## Generic Module Context

### Working Scope

No module YAML was resolved; use the pathway and taxon context.

### Provisional Biological Outline

No module YAML outline available.

### Known Relationships Among Steps

No module YAML connections available.

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

# Module/Pathway Review: Hydroxyproline Catabolism in *Pseudomonas putida* KT2440

**Taxon:** *Pseudomonas putida* KT2440 (PSEPK, NCBI taxon 160488, proteome UP000000556)
**Nominal bucket:** KEGG `ppu00470` "D-Amino acid metabolism" (21 candidate genes)
**Review target:** `hydroxyproline_catabolism`

---

## 1. Executive summary

The free **trans-4-hydroxy-L-proline (Hyp) catabolic pathway is present and essentially fully covered** in *P. putida* KT2440. It is encoded by a **contiguous four-gene operon, PP_1255–PP_1258**, that converts trans-4-hydroxy-L-proline to 2-oxoglutarate (α-ketoglutarate) in four steps. This is one of the few bacterial lineages where the pathway is biochemically established **directly in the target species** (Watanabe et al. 2012, PMID 22833679), so module satisfiability rests on strong, direct evidence rather than homology transfer.

The critical curation issue is **not gap-filling but scope**: the assignment inherits the KEGG `ppu00470` "D-amino acid metabolism" bucket, which lumps ~15 unrelated peptidoglycan-, lysine/DAP-, and D-amino-acid-dehydrogenase genes into the candidate list. Only **4 genes (PP_1255, PP_1256, PP_1257, PP_1258)** — plus **paralog disambiguation of the terminal dehydrogenase** — belong to hydroxyproline catabolism. The remaining candidates should be marked `not_expected_in_target_taxon` **for this module** (they are correct genes in *other* modules). Two isomer/derivative pathways that databases frequently conflate — **hydroxyproline *betaine*** catabolism and **3-hydroxyproline** catabolism — must be kept separate.

**Recommended module verdict:** all four expected steps `covered`; terminal step additionally flagged `candidate_uncertain` for paralog choice; module boundary `module_needs_revision` (bucket is too broad).

---

## 2. Target-organism pathway definition

**Process included (and only this):** intracellular oxidative catabolism of **free trans-4-hydroxy-L-proline** to the TCA-cycle intermediate **2-oxoglutarate**, allowing Hyp to serve as a carbon/nitrogen source. Trans-4-hydroxy-L-proline is abundant as a collagen breakdown product, and most bacteria cannot use it; *Pseudomonas* is a notable exception (PMID 22833679).

**Bacterial route (distinct from the mammalian D-amino-acid-oxidase route):**

1. Epimerization of trans-4-hydroxy-L-proline to cis-4-hydroxy-D-proline.
2. Oxidation of cis-4-hydroxy-D-proline to Δ¹-pyrroline-4-hydroxy-2-carboxylate (Pyr4H2C).
3. Deamination/ring-opening of Pyr4H2C to α-ketoglutarate semialdehyde (2,5-dioxopentanoate / 2,5-dioxovalerate).
4. Oxidation of α-ketoglutarate semialdehyde to 2-oxoglutarate.

**Neighboring pathways / overview maps to keep SEPARATE:**

- **KEGG `ppu00470` "D-Amino acid metabolism"** (the nominal bucket) — an overview map that also contains peptidoglycan D-Ala/D-Glu metabolism, DAP/lysine biosynthesis, and D-amino-acid dehydrogenases. It is **not** a hydroxyproline module.
- **L-proline degradation** (PutA/proline dehydrogenase → glutamate) — different substrate stereochemistry and enzymes.
- **Hydroxyproline *betaine* (betonicine) / proline betaine (stachydrine) catabolism** — a *betainized* parallel pathway using HpbD-type epimerase/racemase (PMID 24520058). Same chemistry class, different substrates and genes; a classic source of annotation cross-contamination.
- **3-hydroxyproline catabolism** (cis-3- / trans-3-Hyp), which runs through an enolase-superfamily dehydratase to Δ¹-pyrroline-2-carboxylate (PMID 25608448) — a different isomer route.
- KEGG maps `ppu00040` (pentose/glucuronate) and `ppu00300` (lysine) — where several miscataloged candidates actually belong.

**Alternate names/IDs:** "L-hydroxyproline metabolism," "4-hydroxyproline degradation," "Hyp catabolism"; genes are named *lhp*/*hyp* in other organisms (e.g., *hypRE/hypO/hypD/hypH* in *Sinorhizobium meliloti*; *lhpABCD* in *Pseudomonas aeruginosa*). MetaCyc: "trans-4-hydroxy-L-proline degradation I."

---

## 3. Expected step model

| Step | Reaction | EC | Enzyme (family) | KT2440 gene | Status |
|------|----------|----|-----------------|-------------|--------|
| 1 | trans-4-hydroxy-L-Pro → cis-4-hydroxy-D-Pro | 5.1.1.8 | 4-Hyp 2-epimerase (HypE; ProR superfamily) | **PP_1258 / proR** | covered |
| 2 | cis-4-hydroxy-D-Pro → Δ¹-pyrroline-4-hydroxy-2-carboxylate (Pyr4H2C) | 1.5.-.- (annot. 1.5.1.-) | D-hydroxyproline dehydrogenase (FAD) | **PP_1255** | covered |
| 3 | Pyr4H2C → α-ketoglutarate semialdehyde (+ NH₃) | 3.5.4.22 | Pyr4H2C deaminase (DHDPS/NAL family) | **PP_1257** | covered |
| 4 | α-ketoglutarate semialdehyde → 2-oxoglutarate | 1.2.1.26 | KG-semialdehyde (2,5-dioxovalerate) dehydrogenase | **PP_1256** (operonic) | covered / candidate_uncertain (paralogs PP_2585, PP_3602) |

Upstream **transport** of Hyp into the cell is expected but is not part of this enzymatic module and is not represented among the candidate genes (see §5).

---

## 4. Candidate genes and evidence

### 4.1 High-confidence in-pathway genes (the operon PP_1255–PP_1258)

- **PP_1258 / proR (Q88NF3) — 4-hydroxyproline 2-epimerase, EC 5.1.1.8 (Step 1).**
  Family-level evidence is strong: HypE of the PLP-independent proline-racemase (ProR) superfamily catalyzes the first step of bacterial trans-4-hydroxy-L-proline metabolism (PMID 25786142). Independent confirmation of the identical first step (trans-4-L-Hyp → cis-4-D-Hyp) comes from *S. meliloti* hypRE (PMID 26833407). **Caveat:** ProR-superfamily members can be bifunctional proline racemase / Hyp epimerase, and a single active-site residue (Trp vs Phe) discriminates Hyp from Pro (PMID 30773259). Operon context and the 4HypE annotation strongly favor the epimerase function, but the specificity residue is worth verifying at gene-review level.

- **PP_1255 (Q88NF6) — cis-4-hydroxy-D-proline oxidase / D-hydroxyproline dehydrogenase (Step 2).**
  **Direct target-species evidence.** Watanabe et al. purified and characterized the *P. putida* enzyme; notably it is a **homomeric, FAD-only** enzyme — i.e., a single gene suffices in KT2440 — in contrast to the heterododecameric (α4β4γ4) *P. aeruginosa* enzyme (PMID 22833679). Curation note: the local EC annotation `1.5.1.-` implies NAD(P) as acceptor, but the enzyme is a **dehydrogenase using artificial/quinone-type electron acceptors** (flavoprotein), so EC should be treated as `1.5.-.-` / `1.5.99.-`-like rather than strictly NAD(P)-linked.

- **PP_1257 (Q88NF4) — Δ¹-pyrroline-4-hydroxy-2-carboxylate (Pyr4H2C) deaminase, EC 3.5.4.22 (Step 3).**
  **Direct target-species evidence** (PMID 22833679). It is a unique member of the dihydrodipicolinate synthase / N-acetylneuraminate lyase (DHDPS/NAL) (α/β)₈ family, competitively inhibited by pyruvate. The orthologous HypD of *S. meliloti* has a solved structure confirming the NAL-subfamily fold and mechanism (PMID 26833407).

- **PP_1256 (Q88NF5) — 2,5-dioxovalerate (α-KG-semialdehyde) dehydrogenase, EC 1.2.1.26 (Step 4).**
  Best in-pathway candidate on **synteny** (immediately adjacent to PP_1255/57/58). Note it carries a *different* primary bucket in metadata (`ppu00040`), reflecting that EC 1.2.1.26 is shared with sugar-acid catabolism — an example of how the terminal step is genuinely paralog-ambiguous.

### 4.2 Terminal-step paralogs (candidate_uncertain)

- **PP_2585 (Q88JR4)** and **PP_3602 (Q88GW5)** — both annotated EC 1.2.1.26, primary bucket `ppu00040`. These are broad-specificity aldehyde dehydrogenases likely serving **other** α-ketoglutarate-semialdehyde-producing routes (e.g., oxidative sugar-acid / non-phosphorylative pentose pathways, where α-ketoglutaric semialdehyde dehydrogenase activity is documented in *P. putida*; PMID 19270113). They should not be counted as the hydroxyproline module gene unless expression/knockout data show otherwise.

### 4.3 Candidates that are over-propagated into this module (belong elsewhere)

All of the following are legitimately annotated but belong to **other** modules; they enter the candidate list only through the broad `ppu00470` bucket:

- **Peptidoglycan / cell-wall D-amino-acid:** murI (PP_0736, Glu racemase), murD (PP_1335), ddlA (PP_4346), ddlB (PP_1339).
- **Lysine / diaminopimelate:** lysA-I (PP_2077), lysA-II (PP_5227), dapF (PP_3790), dapF (PP_5228).
- **Alanine / broad racemases:** dadX (PP_5269, Ala racemase), alr (PP_3722, broad-spectrum racemase; characterized as a promiscuous racemase in *Pseudomonas*, PMID 30008699).
- **D-amino-acid / D-arginine dehydrogenases:** dadA1 (PP_4434), dadA2 (PP_5270), PP_4311 (DadA small subunit), dauA (PP_2246, catabolic D-Arg dehydrogenase).
- **Amidohydrolase:** ansB (PP_2453, glutaminase-asparaginase).

None of these participates in Hyp → 2-oxoglutarate conversion.

---

## 5. Gaps, ambiguities, and likely over-annotations

- **No true enzymatic gap.** All four catalytic steps map to KT2440 genes with direct or strong family evidence. Steps 2 and 3 have direct *P. putida* biochemistry; step 1 has strong family + related-organism evidence; step 4 is present but paralog-ambiguous.
- **Terminal-step paralog ambiguity (main open issue).** Three EC 1.2.1.26 genes (PP_1256, PP_2585, PP_3602); synteny favors PP_1256, but functional assignment of which paralog carries flux for Hyp catabolism is unresolved. → `candidate_uncertain`.
- **EC/annotation precision for PP_1255.** `EC 1.5.1.-` overstates NAD(P)-dependence; the enzyme is a flavin dehydrogenase with artificial acceptors. Curators should relax/correct the acceptor.
- **Transport not represented.** A Hyp uptake system (analogous to *S. meliloti* HypMNPQ ABC transporter, PMID 26833407) is biologically expected but is absent from the candidate list; whether KT2440 uses a dedicated transporter or a general amino-acid permease is an open question (weak transfer from *S. meliloti*).
- **Bucket over-breadth = over-annotation.** ~15 of 21 candidates are unrelated. This is precisely the annotation-propagation problem highlighted for this enzyme class: "at least half of the extant protein annotations are incorrect, and the errors propagate…" (PMID 24520058).
- **Isomer/derivative confounders.** Keep hydroxyproline *betaine* (HpbD; PMID 24520058) and 3-hydroxyproline (enolase-superfamily dehydratase; PMID 25608448) pathways out of this module.
- **Regulation** (activator/repressor of the PP_1255–1258 operon) is not addressed by the candidate set and remains an open question for KT2440.

---

## 6. Module and GO-curation recommendations

**Step-level status:**

| Step | Verdict | Gene(s) |
|------|---------|---------|
| 1 Epimerase | `covered` | PP_1258 |
| 2 D-Hyp dehydrogenase | `covered` | PP_1255 |
| 3 Pyr4H2C deaminase | `covered` | PP_1257 |
| 4 KG-semialdehyde dehydrogenase | `covered` + `candidate_uncertain` | PP_1256 (assign); PP_2585, PP_3602 (exclude/other-module) |
| (Transport, optional) | `gap` / not-in-module | — (no candidate) |

**Module boundary:** `module_needs_revision`. Create/curate a **dedicated `hydroxyproline_catabolism` module** scoped to PP_1255–PP_1258 rather than inheriting KEGG `ppu00470`. Explicitly mark the ~15 peptidoglycan/lysine/D-amino-acid genes as `not_expected_in_target_taxon` **for this module** (they remain valid in their own modules).

**GO/EC curation:**
- PP_1255: prefer GO "D-hydroxyproline dehydrogenase / oxidoreductase acting on CH-NH group of donors, flavin acceptor"; avoid NAD(P)-specific EC `1.5.1.-`.
- PP_1257: EC 3.5.4.22 with DHDPS/NAL-family GO; consistent and can stand.
- PP_1258: EC 5.1.1.8 (4-Hyp 2-epimerase); flag possible bifunctional proline-racemase activity.
- Consider a **GO term request** if no specific term exists for "Δ¹-pyrroline-4-hydroxy-2-carboxylate deaminase" activity or the assembled "L-hydroxyproline catabolic process."

**No new module needed** for the core chemistry beyond scoping; separate modules for **hydroxyproline betaine** and **3-hydroxyproline** catabolism should exist independently.

---

## 7. Genes to promote to full `fetch-gene` review

1. **PP_1256** — confirm it (not PP_2585/PP_3602) is the operonic KG-semialdehyde dehydrogenase; resolve the EC 1.2.1.26 paralog assignment. *(highest priority)*
2. **PP_1258 / proR** — verify epimerase vs bifunctional racemase specificity residue (Trp/Phe active-site position).
3. **PP_1255** — correct EC/acceptor annotation (flavin dehydrogenase, not NAD(P)-linked); confirm single-subunit sufficiency.
4. **PP_2585 and PP_3602** — assign to their true pathways (likely sugar-acid / pentose oxidative catabolism) and remove from this module.

The core operon (PP_1255, PP_1257) already has direct *P. putida* biochemistry and needs only annotation tidy-up, not re-investigation.

---

## 8. Key references

- **PMID 22833679** — Watanabe et al. (2012) *J Biol Chem.* Identification/characterization of D-hydroxyproline dehydrogenase and Δ¹-pyrroline-4-hydroxy-2-carboxylate deaminase; **direct *P. putida*/*P. aeruginosa* evidence** for the four-step Hyp→α-KG pathway and gene clustering. *(Primary, direct target-species.)*
- **PMID 25786142** — Watanabe et al. (2015). HypE (ProR superfamily) catalyzes the first step (4-Hyp 2-epimerization) of bacterial trans-4-L-Hyp metabolism.
- **PMID 30773259** — Watanabe et al. (2019). Structure of bifunctional proline racemase/Hyp epimerase; Trp/Phe residue governs Hyp vs Pro specificity. *(Specificity caveat for PP_1258.)*
- **PMID 26833407** — Chen et al. (2016) *Sinorhizobium meliloti* L-Hyp/D-proline catabolism: hypRE/hypO/hypD/hypH step assignments, HypD structure, HypMNPQ transporter. *(Related-organism corroboration; moderate transfer.)*
- **PMID 24520058** — Kumar et al. (2014). Proline betaine / hydroxyproline betaine catabolic pathway (HpbD); explicit warning on annotation over-propagation. *(Boundary separation + over-annotation caution.)*
- **PMID 25608448** — Zhang et al. (2015). cis-3-hydroxy-L-proline dehydratase (enolase superfamily). *(3-Hyp isomer route to keep separate.)*
- **PMID 30008699** — Radkov & Moe (2018). Broad-spectrum racemase (Alr) in *Pseudomonas*. *(Reassigns candidate PP_3722/alr out of this module.)*
- **PMID 19270113** — Meijnen et al. (2009). α-Ketoglutaric semialdehyde dehydrogenase in *P. putida* oxidative sugar catabolism. *(Context for KGSADH paralog function.)*

---

*Evidence grading:* Steps 2–3 rest on **direct *P. putida* KT2440-genus biochemistry**; step 1 on **strong family + related-organism** evidence; step 4 presence is certain but **specific-gene assignment is inferential (synteny)**. Transport and regulation are **inferred/unknown** for KT2440. The dominant curation action is scoping the module away from the broad `ppu00470` bucket, not filling enzymatic gaps.


## Artifacts

- [OpenScientist final report](PSEPK__hydroxyproline-catabolism__ppu00470-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__hydroxyproline-catabolism__ppu00470-deep-research-openscientist_artifacts/final_report.pdf)