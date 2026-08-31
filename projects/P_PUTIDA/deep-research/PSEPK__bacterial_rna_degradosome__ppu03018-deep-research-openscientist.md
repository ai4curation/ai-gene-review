---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T16:09:51.465303'
end_time: '2026-08-31T16:18:55.477468'
duration_seconds: 544.01
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Bacterial RNase E RNA degradosome
  module_summary: Reusable bacterial RNase E-centered RNA degradosome module. RNase
    E provides the scaffold and initiating endoribonuclease, RhlB unwinds structured
    RNA, and PNPase phosphorolytically degrades exposed RNA. Enolase is represented
    as a conserved structural participant, not as an RNA-processing enzyme.
  module_outline: "- RNase E-centered bacterial RNA degradosome\n  - 1. degradosome\
    \ core assembly\n  - RNase E scaffold with enolase\n    - RNase E scaffold (molecular\
    \ player: bacterial RNase E family)\n    - Enolase structural component (molecular\
    \ player: enolase family)\n  - 2. endonucleolytic initiation\n  - RNase E cleavage\
    \ of RNA\n    - RNase E catalytic activity (molecular player: bacterial RNase\
    \ E family; activity or role: ribonuclease E activity)\n  - 3. ATP-dependent RNA\
    \ unwinding\n  - RhlB-assisted RNA unwinding\n    - RhlB RNA helicase activity\
    \ (molecular player: DEAD-box RNA helicase RhlB family; activity or role: RNA\
    \ helicase activity)\n  - 4. phosphorolytic exonucleolysis\n  - PNPase phosphorolytic\
    \ RNA degradation\n    - PNPase activity (molecular player: bacterial polynucleotide\
    \ phosphorylase family; activity or role: polyribonucleotide nucleotidyltransferase\
    \ activity)"
  module_connections: '- RNase E scaffold with enolase precedes RNase E cleavage of
    RNA

    - RNase E cleavage of RNA feeds into RhlB-assisted RNA unwinding

    - RhlB-assisted RNA unwinding feeds into PNPase phosphorolytic RNA degradation'
  pathway_query: ppu03018
  pathway_id: ppu03018
  pathway_name: RNA degradation
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu03018 with 15 primary genes; module
    area: other_kegg_pathway.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '17'
  candidate_genes: '- ppkB: PP_0712 | Q88PY6 | ADP/GDP-polyphosphate phosphotransferase
    (EC 2.7.4.-) (Polyphosphate kinase PPK2) (EC 2.7.4.-; primary bucket kegg:ppu03018)

    - rhlB: PP_1295 | Q88NB7 | ATP-dependent RNA helicase RhlB (EC 3.6.4.13) (EC 3.6.4.13;
    primary bucket kegg:ppu03018)

    - groEL: PP_1361 | Q88N55 | Chaperonin GroEL (EC 5.6.1.7) (60 kDa chaperonin)
    (Chaperonin-60) (Cpn60) (EC 5.6.1.7; primary bucket kegg:ppu04156)

    - eno: PP_1612 | Q88MF9 | Enolase (EC 4.2.1.11) (2-phospho-D-glycerate hydro-lyase)
    (2-phosphoglycerate dehydratase) (EC 4.2.1.11; primary bucket kegg:ppu03018)

    - deaD: PP_1868 | Q88LR1 | ATP-dependent RNA helicase DeaD (EC 3.6.4.13) (Cold-shock
    DEAD box protein A) (EC 3.6.4.13; primary bucket kegg:ppu03018)

    - rne: PP_1905 | Q88LM4 | Ribonuclease E (RNase E) (EC 3.1.26.12) (EC 3.1.26.12;
    primary bucket kegg:ppu03018)

    - recQ: PP_4516 | Q88EE9 | DNA helicase RecQ (EC 5.6.2.4) (EC 5.6.2.4; primary
    bucket kegg:ppu03018)

    - pcnB: PP_4697 | Q88DX1 | Poly(A) polymerase I (PAP I) (EC 2.7.7.19) (EC 2.7.7.19;
    primary bucket kegg:ppu03018)

    - pnp: PP_4708 | Q88DW0 | Polyribonucleotide nucleotidyltransferase (EC 2.7.7.8)
    (Polynucleotide phosphorylase) (PNPase) (EC 2.7.7.8; primary bucket kegg:ppu03018)

    - dnaK: PP_4727 | Q88DU2 | Chaperone protein DnaK (HSP70) (Heat shock 70 kDa protein)
    (Heat shock protein 70) (primary bucket kegg:ppu04156)

    - rhlE-I: PP_4766 | Q88DQ7 | DEAD-box ATP-dependent RNA helicase RhpA (EC 3.6.4.13)
    (EC 3.6.4.13; primary bucket kegg:ppu03018)

    - rnr: PP_4880 | Q88DE6 | Ribonuclease R (RNase R) (EC 3.1.13.1) (EC 3.1.13.1;
    primary bucket kegg:ppu03018)

    - hfq: PP_4894 | Q88DD3 | RNA-binding protein Hfq (primary bucket kegg:ppu03018)

    - rhlE: PP_4980 | Q88D48 | ATP-dependent RNA helicase RhlE (EC 3.6.4.13) (EC 3.6.4.13;
    primary bucket kegg:ppu03018)

    - rppH: PP_5146 | Q88CN4 | RNA pyrophosphohydrolase (EC 3.6.1.-) ((Di)nucleoside
    polyphosphate hydrolase) (EC 3.6.1.-; primary bucket kegg:ppu03018)

    - rho: PP_5214 | Q88CG7 | Transcription termination factor Rho (EC 3.6.4.-) (ATP-dependent
    helicase Rho) (EC 3.6.4.-; primary bucket kegg:ppu03018)

    - ppk: PP_5217 | Q88CG4 | Polyphosphate kinase (EC 2.7.4.1) (ATP-polyphosphate
    phosphotransferase) (Polyphosphoric acid kinase) (EC 2.7.4.1; primary bucket kegg:ppu03018)'
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
  path: PSEPK__bacterial_rna_degradosome__ppu03018-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__bacterial_rna_degradosome__ppu03018-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Bacterial RNase E RNA degradosome in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu03018
- Resolved ID: ppu03018
- Resolved name: RNA degradation
- Source: KEGG

Resolved local bucket kegg:ppu03018 with 15 primary genes; module area: other_kegg_pathway.

## Candidate Genes From Local Metadata

Candidate gene count: 17

- ppkB: PP_0712 | Q88PY6 | ADP/GDP-polyphosphate phosphotransferase (EC 2.7.4.-) (Polyphosphate kinase PPK2) (EC 2.7.4.-; primary bucket kegg:ppu03018)
- rhlB: PP_1295 | Q88NB7 | ATP-dependent RNA helicase RhlB (EC 3.6.4.13) (EC 3.6.4.13; primary bucket kegg:ppu03018)
- groEL: PP_1361 | Q88N55 | Chaperonin GroEL (EC 5.6.1.7) (60 kDa chaperonin) (Chaperonin-60) (Cpn60) (EC 5.6.1.7; primary bucket kegg:ppu04156)
- eno: PP_1612 | Q88MF9 | Enolase (EC 4.2.1.11) (2-phospho-D-glycerate hydro-lyase) (2-phosphoglycerate dehydratase) (EC 4.2.1.11; primary bucket kegg:ppu03018)
- deaD: PP_1868 | Q88LR1 | ATP-dependent RNA helicase DeaD (EC 3.6.4.13) (Cold-shock DEAD box protein A) (EC 3.6.4.13; primary bucket kegg:ppu03018)
- rne: PP_1905 | Q88LM4 | Ribonuclease E (RNase E) (EC 3.1.26.12) (EC 3.1.26.12; primary bucket kegg:ppu03018)
- recQ: PP_4516 | Q88EE9 | DNA helicase RecQ (EC 5.6.2.4) (EC 5.6.2.4; primary bucket kegg:ppu03018)
- pcnB: PP_4697 | Q88DX1 | Poly(A) polymerase I (PAP I) (EC 2.7.7.19) (EC 2.7.7.19; primary bucket kegg:ppu03018)
- pnp: PP_4708 | Q88DW0 | Polyribonucleotide nucleotidyltransferase (EC 2.7.7.8) (Polynucleotide phosphorylase) (PNPase) (EC 2.7.7.8; primary bucket kegg:ppu03018)
- dnaK: PP_4727 | Q88DU2 | Chaperone protein DnaK (HSP70) (Heat shock 70 kDa protein) (Heat shock protein 70) (primary bucket kegg:ppu04156)
- rhlE-I: PP_4766 | Q88DQ7 | DEAD-box ATP-dependent RNA helicase RhpA (EC 3.6.4.13) (EC 3.6.4.13; primary bucket kegg:ppu03018)
- rnr: PP_4880 | Q88DE6 | Ribonuclease R (RNase R) (EC 3.1.13.1) (EC 3.1.13.1; primary bucket kegg:ppu03018)
- hfq: PP_4894 | Q88DD3 | RNA-binding protein Hfq (primary bucket kegg:ppu03018)
- rhlE: PP_4980 | Q88D48 | ATP-dependent RNA helicase RhlE (EC 3.6.4.13) (EC 3.6.4.13; primary bucket kegg:ppu03018)
- rppH: PP_5146 | Q88CN4 | RNA pyrophosphohydrolase (EC 3.6.1.-) ((Di)nucleoside polyphosphate hydrolase) (EC 3.6.1.-; primary bucket kegg:ppu03018)
- rho: PP_5214 | Q88CG7 | Transcription termination factor Rho (EC 3.6.4.-) (ATP-dependent helicase Rho) (EC 3.6.4.-; primary bucket kegg:ppu03018)
- ppk: PP_5217 | Q88CG4 | Polyphosphate kinase (EC 2.7.4.1) (ATP-polyphosphate phosphotransferase) (Polyphosphoric acid kinase) (EC 2.7.4.1; primary bucket kegg:ppu03018)

## Generic Module Context

### Working Scope

Reusable bacterial RNase E-centered RNA degradosome module. RNase E provides the scaffold and initiating endoribonuclease, RhlB unwinds structured RNA, and PNPase phosphorolytically degrades exposed RNA. Enolase is represented as a conserved structural participant, not as an RNA-processing enzyme.

### Provisional Biological Outline

- RNase E-centered bacterial RNA degradosome
  - 1. degradosome core assembly
  - RNase E scaffold with enolase
    - RNase E scaffold (molecular player: bacterial RNase E family)
    - Enolase structural component (molecular player: enolase family)
  - 2. endonucleolytic initiation
  - RNase E cleavage of RNA
    - RNase E catalytic activity (molecular player: bacterial RNase E family; activity or role: ribonuclease E activity)
  - 3. ATP-dependent RNA unwinding
  - RhlB-assisted RNA unwinding
    - RhlB RNA helicase activity (molecular player: DEAD-box RNA helicase RhlB family; activity or role: RNA helicase activity)
  - 4. phosphorolytic exonucleolysis
  - PNPase phosphorolytic RNA degradation
    - PNPase activity (molecular player: bacterial polynucleotide phosphorylase family; activity or role: polyribonucleotide nucleotidyltransferase activity)

### Known Relationships Among Steps

- RNase E scaffold with enolase precedes RNase E cleavage of RNA
- RNase E cleavage of RNA feeds into RhlB-assisted RNA unwinding
- RhlB-assisted RNA unwinding feeds into PNPase phosphorolytic RNA degradation

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

# Species-Aware Review: Bacterial RNase E RNA Degradosome in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Target bucket:** KEGG `ppu03018` "RNA degradation" (15 primary genes; 17 candidate genes)
**Commissioned module:** Reusable bacterial RNase E-centered RNA degradosome
**Date:** 2026-08-31 · **Iterations:** 1–2 of 3

---

## 1. Executive summary

The RNase E-centered RNA degradosome **is present and satisfiable** in *P. putida* KT2440, but the organism-specific composition **diverges from the *Escherichia coli* textbook model**, and the KEGG `ppu03018` bucket is **substantially broader than the commissioned module**.

- **Core scaffold + endonuclease is solid.** RNase E (`rne`, PP_1905) is present, essential, and — as in all *Pseudomonadota* — nucleates the degradosome through its C-terminal domain (CTD). Direct *Pseudomonas* evidence (from *P. aeruginosa*) shows the CTD binds the core partners **PNPase and RhlB** through short linear motifs (SLiMs) (PMID 40096066).
- **PNPase and a DEAD-box helicase are present** (`pnp` PP_4708; `rhlB` PP_1295 plus paralogs). Which helicase is the *bona fide* degradosome partner in *P. putida* is **ambiguous** — Pseudomonads can use **RhlE** rather than RhlB, and can recruit the hydrolytic exoribonuclease **RNase R** in place of/alongside PNPase (PMID 15705581).
- **Enolase membership is homology-inferred and uncertain** in this lineage; its glycolytic role is certain, its degradosome role in KT2440 is not demonstrated (contrast E. coli, PMID 23927922).
- **The bucket over-reaches.** `recQ` (DNA repair), `rho` (transcription termination), `ppk`/`ppkB` (polyphosphate), and `groEL`/`dnaK` (chaperones) are neighboring-process or over-propagated members that should be kept out of the degradosome-core module.
- **Direct KT2440 experimental evidence exists** for RNase E, PNPase, RNase R (deletion phenotypes; PMID 33089610) and for Hfq (Crc-Hfq catabolite repression; PMID 24803210) — the latter clarifies that Hfq's characterized role here is translational regulation, not degradosome scaffolding.

**Bottom line:** Mark the four degradosome-core steps **covered** (with a `candidate_uncertain` flag on the enolase step and on helicase/exonuclease paralog identity). Recommend `module_needs_revision` on the fixed RhlB/PNPase wiring, `not_expected_in_target_taxon`/wrong-process for `recQ`, and separation of the 5′-trigger, 3′-decay, chaperone and polyphosphate members into neighboring modules.

---

## 2. Target-organism pathway definition

**What the module includes (biochemical scope):** the multi-protein machine that carries out bulk mRNA turnover and processing in Gram-negative bacteria — endonucleolytic initiation by RNase E, ATP-dependent unwinding of structured RNA by a DEAD-box helicase, and 3′→5′ exonucleolytic degradation by PNPase — physically organized on the intrinsically disordered RNase E CTD scaffold, which in Pseudomonads also tethers the complex to the inner membrane (PMID 40096066).

**Neighboring processes to keep separate (do NOT fold into the degradosome-core module):**
- **5′-end deprotection / decay initiation** — RppH (`rppH`, PP_5146): removes 5′-pyrophosphate to license RNase E cleavage; upstream trigger, not a core subunit (PMID 18202662).
- **3′-end-dependent decay & tailing** — RNase R (`rnr`, PP_4880) and poly(A) polymerase I (`pcnB`, PP_4697).
- **Transcription termination** — Rho (`rho`, PP_5214).
- **DNA metabolism** — RecQ (`recQ`, PP_4516): a DNA helicase; not RNA degradation.
- **Protein folding / stress** — GroEL (`groEL`, PP_1361), DnaK (`dnaK`, PP_4727): chaperones (primary bucket `ppu04156`); DnaK is at most a stress-induced minor degradosome associate in E. coli (PMID 16139413).
- **Polyphosphate metabolism** — PPK/PPK2 (`ppk` PP_5217, `ppkB` PP_0712): KEGG map03018 "others" box; peripheral.
- **Glycolysis** — Enolase (`eno`, PP_1612): primary role in `ppu00010`.

**Alternate names / database definitions:** KEGG map03018 "RNA degradation" ≈ the "RNA degradosome" concept, but the KEGG map is deliberately inclusive (degradosome + exosome + accessory/others boxes). GO terms of interest: degradosome (GO:0030679 "cytoplasmic side"/complex terms), ribonuclease E activity (GO:0008995), 3′→5′ exoribonuclease/polyribonucleotide nucleotidyltransferase (GO:0004654), ATP-dependent RNA helicase (GO:0004004), RNA pyrophosphohydrolase (GO:0034353-adjacent Nudix activity).

---

## 3. Expected step model (module) → status in KT2440

| # | Module step | Expected player | KT2440 candidate | Status |
|---|-------------|-----------------|------------------|--------|
| 1 | Degradosome core assembly (scaffold + enolase) | RNase E family + enolase | `rne` PP_1905 (scaffold); `eno` PP_1612 (enolase) | **covered** (scaffold); **candidate_uncertain** (enolase membership) |
| 2 | Endonucleolytic initiation | RNase E catalytic | `rne` PP_1905 | **covered** |
| 3 | ATP-dependent RNA unwinding | DEAD-box RhlB | `rhlB` PP_1295 (+ `rhlE` PP_4980, `rhlE-I`/RhpA PP_4766, `deaD` PP_1868) | **covered but candidate_uncertain** (paralog identity) |
| 4 | Phosphorolytic exonucleolysis | PNPase | `pnp` PP_4708 (± hydrolytic `rnr` PP_4880) | **covered** (PNPase present); **module_needs_revision** (RNase R may substitute) |

---

## 4. Candidate genes and evidence

### High-confidence degradosome-core genes

**`rne` — Ribonuclease E, PP_1905 (Q88LM4).** *Role:* endoribonuclease + degradosome scaffold (CTD). *Evidence:* strong. Directly studied in KT2440 (RNase E deletion/variant among a panel of RNase mutants, PMID 33089610); Pseudomonas CTD scaffold function mapped in the close relative *P. aeruginosa* (PMID 40096066). *Caveat:* the Pseudomonas CTD is sequence-divergent from E. coli, so which SLiMs recruit which partners must be read from Pseudomonas data, not E. coli homology. **Promote to full review.**

**`pnp` — PNPase (polyribonucleotide nucleotidyltransferase), PP_4708 (Q88DW0).** *Role:* 3′→5′ phosphorolytic exoribonuclease; classic degradosome core partner and Pseudomonas CTD binder (PMID 40096066). *Evidence:* strong; KT2440 pnp deletion characterized (PMID 33089610). *Caveat:* PNPase has well-documented degradosome-**independent** functions (e.g., cold/oxidative stress in related genera; PMID 23082859), so presence ≠ obligate degradosome participation. **Promote to full review.**

**`rhlB` — ATP-dependent RNA helicase RhlB, PP_1295 (Q88NB7).** *Role:* unwinds structured RNA to feed PNPase; Pseudomonas CTD binder (PMID 40096066). *Evidence:* moderate (homology + P. aeruginosa interaction data). *Caveat:* **paralog ambiguity** — see below. **Promote to full review.**

**`eno` — Enolase, PP_1612 (Q88MF9).** *Role:* glycolytic 2-phosphoglycerate dehydratase; in E. coli also a degradosome structural component (PMID 23927922, 16139413). *Evidence for degradosome role in Pseudomonas:* weak/absent — the P. aeruginosa CTD map named PNPase and RhlB (not enolase) as core partners (PMID 40096066). *Caveat:* likely over-propagated as a "degradosome" annotation in this lineage; glycolytic annotation is solid. **candidate_uncertain.**

### Accessory / neighboring RNA-metabolism genes (present, but not degradosome-core)

**`rnr` — RNase R, PP_4880 (Q88DE6).** Hydrolytic 3′→5′ exoribonuclease for structured RNA. *Species-relevant twist:* in *P. syringae* Lz4W, RNase R (not PNPase) co-purifies with RNase E and RhlE — a "degradosome of novel structure" (PMID 15705581). KT2440 rnr deletion characterized (PMID 33089610). **Relevant to step 4; promote to full review** to resolve whether it is a KT2440 degradosome partner.

**`rppH` — RNA pyrophosphohydrolase, PP_5146 (Q88CN4).** 5′-triphosphate→monophosphate deprotection that licenses RNase E cleavage (PMID 18202662; H. pylori ortholog PMID 27974459). *Status:* upstream **decay-initiation** step, adjacent to but outside the degradosome core. Homology-only in KT2440.

**`pcnB` — Poly(A) polymerase I, PP_4697 (Q88DX1).** Adds 3′ poly(A) tails that mark RNA for exonucleolytic decay. Accessory to 3′-decay; homology-based.

**`hfq` — RNA-binding protein Hfq, PP_4894 (Q88DD3).** In KT2440, characterized role is **Crc-Hfq catabolite repression** (binds AAnAAnAA CA motifs, inhibits translation; regulates CrcZ/CrcY sRNAs) — PMID 24803210, 27777366, 37348756. Its degradosome/decay role is not the primary demonstrated function here. **candidate_uncertain** for this module.

**Helicase paralogs `deaD` PP_1868, `rhlE` PP_4980, `rhlE-I`/RhpA PP_4766.** Additional DEAD-box helicases (EC 3.6.4.13). Create genuine ambiguity about which helicase serves the degradosome (RhlB vs RhlE, the latter favored in Pseudomonas per PMID 15705581).

### Likely over-propagated / wrong-process bucket members

- **`recQ` — DNA helicase RecQ, PP_4516 (EC 5.6.2.4).** DNA repair/recombination. **Not an RNA-degradation enzyme; over-propagation into ppu03018.** → `not_expected_in_target_taxon` for the degradosome module (wrong process).
- **`rho` — Rho, PP_5214.** Transcription termination factor. Adjacent (transcription), not degradosome.
- **`ppk` PP_5217, `ppkB` PP_0712.** Polyphosphate kinases (KEGG "others" box). Peripheral.
- **`groEL` PP_1361, `dnaK` PP_4727.** Chaperones (primary bucket `ppu04156`). DnaK is only a stress-induced minor degradosome associate in E. coli, not a structural subunit (PMID 16139413).

---

## 5. Gaps, ambiguities, and likely over-annotations

1. **Helicase identity gap (step 3).** RhlB is annotated, but Pseudomonas degradosomes can use **RhlE** (PMID 15705581). With four DEAD-box paralogs (`rhlB`, `rhlE`, `rhpA`, `deaD`), the actual KT2440 degradosome helicase is unresolved. → `candidate_uncertain`.
2. **Exonuclease substitution (step 4).** PNPase is present, but **RNase R** may substitute or co-participate in Pseudomonas (PMID 15705581). The generic module's rigid "PNPase" wiring may under-represent KT2440. → `module_needs_revision`.
3. **Enolase membership (step 1).** No KT2440 evidence that enolase is a structural degradosome subunit; homology transfer from E. coli is weak across *Pseudomonadota*. → `candidate_uncertain`; guard against auto-propagating a degradosome GO term to PP_1612.
4. **Bucket over-inclusion.** `recQ` (DNA), `rho` (transcription), `ppk`/`ppkB` (polyphosphate), `groEL`/`dnaK` (chaperones) inflate the module. Keep separate.
5. **Divergent physiology.** KT2440 RNase deletion phenotypes "diverged significantly" from E. coli (PMID 33089610) — a general caution that E. coli functional annotations transfer imperfectly.
6. **RNase E regulators not captured by the bucket.** RraA-type regulators bind the RNase E regulatory domain and modulate its activity; an RraA-like protein exists in *P. putida* F1 (structurally characterized alongside HMG/CHA aldolases, PMID 24359411). These regulatory inputs are relevant to degradosome biology but are absent from the ppu03018 candidate list — a note for curators rather than a module step. (Not present as a KT2440 candidate gene; homology-level relevance only.)

---

## 6. Module and GO-curation recommendations

| Module step / gene | Recommended mark | Rationale |
|---|---|---|
| Step 2 endonucleolytic initiation (`rne`) | **covered** | Present, essential, direct KT2440 + Pseudomonas scaffold data |
| Step 1 scaffold (`rne` CTD) | **covered** | Pseudomonas CTD scaffold demonstrated (P. aeruginosa) |
| Step 1 enolase (`eno`) | **candidate_uncertain** | Degradosome role homology-inferred only; weak transfer |
| Step 3 unwinding (`rhlB`/`rhlE`/…) | **candidate_uncertain** | Paralog identity unresolved; RhlE plausible partner |
| Step 4 phosphorolysis (`pnp`) | **covered** | Present, KT2440-studied, Pseudomonas CTD binder |
| Step 4 wiring (PNPase-only) | **module_needs_revision** | RNase R substitution documented in Pseudomonas |
| `recQ` in this bucket | **not_expected_in_target_taxon** (wrong process) | DNA helicase; over-propagation |
| `rho`, `ppk`, `ppkB`, `groEL`, `dnaK` | keep in neighboring modules | Transcription / polyphosphate / chaperone processes |
| `rppH`, `pcnB`, `rnr`, `hfq` | accessory (candidate_uncertain for core) | 5′-trigger / 3′-tailing / hydrolytic exo / regulator |

**Module-boundary recommendations:**
- The generic RNase E module is broadly correct but should (a) allow **RhlE** as an alternative helicase player, (b) allow **RNase R** as an alternative/added exonuclease player for Pseudomonads, and (c) demote enolase to an optional, lineage-variable structural participant.
- Consider a **separate "5′-end-dependent decay initiation" module** (RppH) and a **"3′-end decay/polyadenylation" module** (PcnB + RNase R + PNPase), which the KEGG bucket currently conflates with the degradosome.

**GO-curation notes:** avoid propagating degradosome-complex GO terms onto `eno` (PP_1612), the chaperones, `recQ`, `rho`, and the polyphosphate kinases without direct evidence. A GO term / annotation request may be warranted to capture the Pseudomonas-specific **RNase R-containing degradosome** variant if curation needs to represent it.

---

## 7. Genes to promote to full `fetch-gene` review

1. **`rne` PP_1905** — core scaffold + catalytic; confirm CTD SLiMs and partner set in KT2440.
2. **`pnp` PP_4708** — core exonuclease; confirm degradosome vs independent roles.
3. **`rhlB` PP_1295** *and* **`rhlE` PP_4980** (and `rhpA` PP_4766) — resolve which helicase is the degradosome partner.
4. **`rnr` PP_4880** — test for RNase E association (Pseudomonas-specific degradosome variant).
5. **`eno` PP_1612** — verify/deny degradosome membership before annotation propagation.
6. (Secondary) **`hfq` PP_4894** — clarify degradosome vs Crc-Hfq regulatory scope.

---

## 8. Key references

- **PMID 40096066** (2025) Geslain et al. *Critical functions and key interactions mediated by the RNase E scaffolding domain in Pseudomonas aeruginosa.* — Pseudomonas RNase E CTD scaffold; SLiMs binding PNPase and RhlB; membrane attachment; virulence/cold roles. *(Close relative; strong transfer to P. putida.)*
- **PMID 33089610** (2021) Apura et al. *Ribonucleases control distinct traits of Pseudomonas putida lifestyle.* — **Direct KT2440**: PNPase, RNase R, RNase E, RNase III, RNase G deletions; roles diverge from E. coli.
- **PMID 15705581** (2005) Purusharth et al. *Exoribonuclease R interacts with endoribonuclease E and an RNA helicase in Pseudomonas syringae Lz4W.* — Pseudomonas degradosome with RNase R + RhlE (novel structure). *(Same genus; moderate transfer.)*
- **PMID 24803210** (2015) Moreno et al. *The Crc and Hfq proteins of Pseudomonas putida cooperate in catabolite repression…* — **Direct KT2440** Hfq function.
- **PMID 27777366** (2016) Hernández-Arranz et al. — KT2440 Hfq/Crc and CrcZ sRNA processing/stability.
- **PMID 37348756** (2023) Lu et al. — Crc-Hfq as a portable translational-control module.
- **PMID 18202662** (2008) Deana et al. *The bacterial enzyme RppH triggers mRNA degradation by 5′ pyrophosphate removal.* — RppH as the 5′-deprotection trigger upstream of RNase E. *(E. coli; mechanism generalizes.)*
- **PMID 27974459** (2017) Bischler et al. — RppH ortholog function in another Gram-negative (H. pylori).
- **PMID 23927922** (2013) Domínguez-Malfavón et al. — E. coli degradosome assembly; RNase E-enolase and RNase E-PNPase interactions; CTD scaffold.
- **PMID 16139413** (2006) Regonesi et al. — E. coli degradosome proteomics; DnaK a stress-induced minor associate, not structural.
- **PMID 23082859** (2012) Henry et al. — PNPase degradosome-independent functions (Yersinia).

---

### Evidence provenance summary
- **Direct KT2440 experiment:** RNase E, PNPase, RNase R, RNase III/G (deletion phenotypes); Hfq (Crc-Hfq).
- **Same-genus (Pseudomonas):** CTD scaffold/PNPase/RhlB (P. aeruginosa); RNase R + RhlE degradosome (P. syringae).
- **Homology / generic bacterial:** RhlB partner identity, enolase membership, RppH, PcnB, and all "others"-box genes.


## Artifacts

- [OpenScientist final report](PSEPK__bacterial_rna_degradosome__ppu03018-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__bacterial_rna_degradosome__ppu03018-deep-research-openscientist_artifacts/final_report.pdf)