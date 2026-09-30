---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T13:38:01.315909'
end_time: '2026-09-01T13:50:36.165299'
duration_seconds: 754.85
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Bacterial SRP-dependent cotranslational membrane targeting
  module_summary: A reusable bacterial module for cotranslational targeting of hydrophobic
    nascent membrane proteins to the cytoplasmic membrane. An Ffh/4.5S-RNA signal
    recognition particle binds the ribosome-nascent-chain complex, the SRP receptor
    FtsY captures that complex at the membrane, and reciprocal GTPase activation promotes
    handoff to the SecYEG insertion machinery and dissociation of Ffh and FtsY. The
    boundary ends at this handoff; SecYEG-mediated translocation and insertion are
    downstream modules.
  module_outline: "- Bacterial SRP-dependent cotranslational membrane targeting\n\
    \  - 1. nascent signal-sequence recognition by bacterial SRP\n  - Ffh/4.5S-RNA\
    \ nascent-chain recognition\n    - Ffh nascent signal-sequence binding (molecular\
    \ player: Ffh/SRP54 family; activity or role: signal sequence binding)\n    -\
    \ Ffh binding to bacterial SRP RNA (molecular player: Ffh/SRP54 family; activity\
    \ or role: 7S RNA binding)\n  - 2. membrane receptor engagement\n  - FtsY engagement\
    \ of the SRP-ribosome complex\n    - FtsY SRP receptor (molecular player: bacterial\
    \ FtsY SRP receptor family; activity or role: signal recognition particle binding)\n\
    \  - 3. GTP-coupled handoff and targeting-factor recycling\n  - Ffh/FtsY GTPase\
    \ handoff cycle\n    - Ffh GTPase (molecular player: Ffh/SRP54 family; activity\
    \ or role: GTPase activity)\n    - FtsY receptor GTPase (molecular player: bacterial\
    \ FtsY SRP receptor family; activity or role: GTPase activity)"
  module_connections: '- Ffh/4.5S-RNA nascent-chain recognition precedes FtsY engagement
    of the SRP-ribosome complex: Signal recognition by SRP precedes capture of the
    SRP-RNC complex by membrane-associated FtsY.

    - FtsY engagement of the SRP-ribosome complex precedes Ffh/FtsY GTPase handoff
    cycle: Receptor engagement precedes reciprocal GTPase activation, SecYEG handoff,
    and targeting-factor dissociation.'
  pathway_query: ppu03060
  pathway_id: ppu03060
  pathway_name: Protein export
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu03060 with 19 primary genes; module
    area: other_kegg_pathway.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '19'
  candidate_genes: '- yidC: PP_0006 | P0A140 | Membrane protein insertase YidC (Foldase
    YidC) (Membrane integrase YidC) (Membrane protein YidC) (primary bucket kegg:ppu03060)

    - secE: PP_0441 | Q88QP7 | Protein translocase subunit SecE (primary bucket kegg:ppu03060)

    - secY: PP_0474 | Q88QL5 | Protein translocase subunit SecY (primary bucket kegg:ppu03060)

    - lspA: PP_0604 | Q88Q91 | Lipoprotein signal peptidase (EC 3.4.23.36) (Prolipoprotein
    signal peptidase) (Signal peptidase II) (SPase II) (EC 3.4.23.36; primary bucket
    kegg:ppu03060)

    - yajC: PP_0834 | Q88PL6 | Sec translocon accessory complex subunit YajC (primary
    bucket kegg:ppu03060)

    - secD: PP_0835 | Q88PL5 | Protein translocase subunit SecD (primary bucket kegg:ppu03060)

    - secF: PP_0836 | Q88PL4 | Protein-export membrane protein SecF (primary bucket
    kegg:ppu03060)

    - tatC-I: PP_1039 | Q88P14 | Sec-independent protein translocase protein TatC
    (primary bucket kegg:ppu03060)

    - tatB-I: PP_1040 | Q88P13 | Sec-independent protein translocase TatB (primary
    bucket kegg:ppu03060)

    - tatA-I: PP_1041 | Q88P12 | Sec-independent protein translocase protein TatA
    (primary bucket kegg:ppu03060)

    - secA: PP_1345 | Q88N69 | Protein translocase subunit SecA (EC 7.4.2.8) (EC 7.4.2.8;
    primary bucket kegg:ppu03060)

    - lepB: PP_1432 | Q88MY6 | Signal peptidase I (EC 3.4.21.89) (EC 3.4.21.89; primary
    bucket kegg:ppu03060)

    - ffh: PP_1461 | Q88MV7 | Signal recognition particle protein (EC 3.6.5.4) (Fifty-four
    homolog) (EC 3.6.5.4; primary bucket kegg:ppu03060)

    - tatA-II: PP_5016 | Q88D13 | Sec-independent protein translocase protein TatA
    (primary bucket kegg:ppu03060)

    - tatB: PP_5017 | Q88D12 | Sec-independent protein translocase protein TatB (primary
    bucket kegg:ppu03060)

    - tatC-II: PP_5018 | Q88D11 | Sec-independent protein translocase protein TatC
    (primary bucket kegg:ppu03060)

    - secB: PP_5053 | Q88CX7 | Protein-export protein SecB (primary bucket kegg:ppu03060)

    - ftsY: PP_5111 | Q88CR9 | Signal recognition particle receptor FtsY (SRP receptor)
    (EC 3.6.5.4) (EC 3.6.5.4; primary bucket kegg:ppu03060)

    - secG: PP_5706 | A0A140FWQ9 | Protein-export membrane protein SecG (primary bucket
    kegg:ppu03060)'
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
  path: PSEPK__bacterial_srp_cotranslational_targeting__ppu03060-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__bacterial_srp_cotranslational_targeting__ppu03060-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Bacterial SRP-dependent cotranslational membrane targeting in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu03060
- Resolved ID: ppu03060
- Resolved name: Protein export
- Source: KEGG

Resolved local bucket kegg:ppu03060 with 19 primary genes; module area: other_kegg_pathway.

## Candidate Genes From Local Metadata

Candidate gene count: 19

- yidC: PP_0006 | P0A140 | Membrane protein insertase YidC (Foldase YidC) (Membrane integrase YidC) (Membrane protein YidC) (primary bucket kegg:ppu03060)
- secE: PP_0441 | Q88QP7 | Protein translocase subunit SecE (primary bucket kegg:ppu03060)
- secY: PP_0474 | Q88QL5 | Protein translocase subunit SecY (primary bucket kegg:ppu03060)
- lspA: PP_0604 | Q88Q91 | Lipoprotein signal peptidase (EC 3.4.23.36) (Prolipoprotein signal peptidase) (Signal peptidase II) (SPase II) (EC 3.4.23.36; primary bucket kegg:ppu03060)
- yajC: PP_0834 | Q88PL6 | Sec translocon accessory complex subunit YajC (primary bucket kegg:ppu03060)
- secD: PP_0835 | Q88PL5 | Protein translocase subunit SecD (primary bucket kegg:ppu03060)
- secF: PP_0836 | Q88PL4 | Protein-export membrane protein SecF (primary bucket kegg:ppu03060)
- tatC-I: PP_1039 | Q88P14 | Sec-independent protein translocase protein TatC (primary bucket kegg:ppu03060)
- tatB-I: PP_1040 | Q88P13 | Sec-independent protein translocase TatB (primary bucket kegg:ppu03060)
- tatA-I: PP_1041 | Q88P12 | Sec-independent protein translocase protein TatA (primary bucket kegg:ppu03060)
- secA: PP_1345 | Q88N69 | Protein translocase subunit SecA (EC 7.4.2.8) (EC 7.4.2.8; primary bucket kegg:ppu03060)
- lepB: PP_1432 | Q88MY6 | Signal peptidase I (EC 3.4.21.89) (EC 3.4.21.89; primary bucket kegg:ppu03060)
- ffh: PP_1461 | Q88MV7 | Signal recognition particle protein (EC 3.6.5.4) (Fifty-four homolog) (EC 3.6.5.4; primary bucket kegg:ppu03060)
- tatA-II: PP_5016 | Q88D13 | Sec-independent protein translocase protein TatA (primary bucket kegg:ppu03060)
- tatB: PP_5017 | Q88D12 | Sec-independent protein translocase protein TatB (primary bucket kegg:ppu03060)
- tatC-II: PP_5018 | Q88D11 | Sec-independent protein translocase protein TatC (primary bucket kegg:ppu03060)
- secB: PP_5053 | Q88CX7 | Protein-export protein SecB (primary bucket kegg:ppu03060)
- ftsY: PP_5111 | Q88CR9 | Signal recognition particle receptor FtsY (SRP receptor) (EC 3.6.5.4) (EC 3.6.5.4; primary bucket kegg:ppu03060)
- secG: PP_5706 | A0A140FWQ9 | Protein-export membrane protein SecG (primary bucket kegg:ppu03060)

## Generic Module Context

### Working Scope

A reusable bacterial module for cotranslational targeting of hydrophobic nascent membrane proteins to the cytoplasmic membrane. An Ffh/4.5S-RNA signal recognition particle binds the ribosome-nascent-chain complex, the SRP receptor FtsY captures that complex at the membrane, and reciprocal GTPase activation promotes handoff to the SecYEG insertion machinery and dissociation of Ffh and FtsY. The boundary ends at this handoff; SecYEG-mediated translocation and insertion are downstream modules.

### Provisional Biological Outline

- Bacterial SRP-dependent cotranslational membrane targeting
  - 1. nascent signal-sequence recognition by bacterial SRP
  - Ffh/4.5S-RNA nascent-chain recognition
    - Ffh nascent signal-sequence binding (molecular player: Ffh/SRP54 family; activity or role: signal sequence binding)
    - Ffh binding to bacterial SRP RNA (molecular player: Ffh/SRP54 family; activity or role: 7S RNA binding)
  - 2. membrane receptor engagement
  - FtsY engagement of the SRP-ribosome complex
    - FtsY SRP receptor (molecular player: bacterial FtsY SRP receptor family; activity or role: signal recognition particle binding)
  - 3. GTP-coupled handoff and targeting-factor recycling
  - Ffh/FtsY GTPase handoff cycle
    - Ffh GTPase (molecular player: Ffh/SRP54 family; activity or role: GTPase activity)
    - FtsY receptor GTPase (molecular player: bacterial FtsY SRP receptor family; activity or role: GTPase activity)

### Known Relationships Among Steps

- Ffh/4.5S-RNA nascent-chain recognition precedes FtsY engagement of the SRP-ribosome complex: Signal recognition by SRP precedes capture of the SRP-RNC complex by membrane-associated FtsY.
- FtsY engagement of the SRP-ribosome complex precedes Ffh/FtsY GTPase handoff cycle: Receptor engagement precedes reciprocal GTPase activation, SecYEG handoff, and targeting-factor dissociation.

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

# Species-Aware Module Review: Bacterial SRP-Dependent Cotranslational Membrane Targeting in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Local bucket reviewed:** KEGG `ppu03060` "Protein export" (19 primary genes)
**Module scope:** SRP-dependent cotranslational targeting of nascent membrane proteins — from signal-sequence recognition by the Ffh/SRP-RNA particle, through FtsY capture at the membrane, to the reciprocal GTPase-driven handoff to SecYEG. **Boundary ends at handoff**; SecYEG translocation/insertion, signal-peptide cleavage, and Tat export are downstream/parallel modules.

---

## 1. Executive summary

- The SRP-targeting module is **fully satisfiable** in *P. putida* KT2440. All three required components are present in the genome:
  - **Ffh** — `ffh` / **PP_1461** (UniProt Q88MV7)
  - **SRP RNA** — `ffs` / **PP_mr50** (RefSeq **PP_RS22200**; NCBI GeneID 26969983) — a **non-coding RNA**, confirmed directly in the genome
  - **FtsY** — `ftsY` / **PP_5111** (UniProt Q88CR9)
- **Only 2 of the 19** candidate genes in the KEGG `ppu03060` bucket actually belong to this module (`ffh`, `ftsY`). The KEGG "Protein export" bucket is **broader than the module**; the other 17 genes are downstream Sec translocation, YidC insertion, signal peptidases, or the parallel (Sec-independent) Tat pathway.
- The single most important **curation action** is to recognize that a required module component (`ffs` SRP RNA) is a non-coding RNA that is **structurally invisible to a proteome-derived candidate list**. It must be tracked outside UP000000556. It is present (PP_mr50), so the RNA-binding step is **covered**, not a gap.
- **Ffh and FtsY are strictly single-copy** — no paralog ambiguity, no lineage-specific replacement, no over-propagation risk for these two.
- **Evidence caveat:** There is **no direct KT2440 experimental study** of the SRP pathway. All target-organism annotations are computational homology transfer (HAMAP/UniRule, IEA). Transfer from *E. coli*/*B. subtilis* is nonetheless **strong** because SRP/FtsY/SRP-RNA are essential, universally conserved (LUCA-level), and single-copy.

---

## 2. Target-organism pathway definition

**What is included (module scope):** cotranslational recognition of a hydrophobic signal-anchor sequence emerging from the ribosome by bacterial SRP (Ffh + SRP RNA); GTP-dependent capture of the ribosome-nascent-chain (RNC)·SRP complex by the membrane receptor FtsY; reciprocal Ffh↔FtsY GTPase activation; handoff of the RNC to the Sec translocase; and dissociation/recycling of Ffh and FtsY. This corresponds to **GO:0006614 / GO:0006613 "SRP-dependent cotranslational protein targeting to membrane"** (the term already annotated on both Ffh and FtsY in UniProt).

**Neighboring processes that must be kept separate (same KEGG bucket, different module):**
- **SecYEG protein-conducting channel** (SecY/SecE/SecG) and the **SecA** motor ATPase, **SecB** chaperone, **SecDF–YajC** ancillary complex — this is the *downstream* Sec translocation/insertion machinery. The module boundary explicitly ends at the SRP→SecYEG handoff.
- **YidC** membrane insertase — downstream/parallel insertion (SecYEG-dependent and SecYEG-independent insertion), not part of targeting.
- **LepB** (signal peptidase I) and **LspA** (signal peptidase II) — post-translocation signal-peptide cleavage/maturation.
- **Twin-arginine translocation (Tat)** — a completely separate, *Sec-independent* pathway that exports folded proteins; not SRP-related.

**Alternate names / database definitions:** KEGG map03060 "Protein export"; the SRP RNA appears as **ffs** (gene), **4.5S RNA** (*E. coli* nomenclature), **small cytoplasmic/SRP RNA**, and **Rfam RF00169** ("Bacteria_small_SRP"). Ffh = "Fifty-four homolog" / SRP54 family; FtsY = SRP receptor (SR / SRα homolog).

---

## 3. Expected step model and satisfiability

| Module step | Required player | KT2440 locus | Status | Evidence |
|---|---|---|---|---|
| 1a. Nascent signal-sequence binding | Ffh (SRP54 family) | `ffh` / PP_1461 (Q88MV7) | **covered** | Homology (HAMAP MF_00306, IEA); single-copy |
| 1b. SRP RNA scaffold binding (7S/4.5S RNA binding) | SRP RNA + Ffh | `ffs` / PP_mr50 (PP_RS22200) + PP_1461 | **covered** (non-protein component) | Direct genome evidence (NCBI GeneID 26969983); Rfam RF00169 |
| 2. Membrane receptor engagement | FtsY (SR family) | `ftsY` / PP_5111 (Q88CR9) | **covered** | Homology (HAMAP MF_00920, IEA); single-copy |
| 3. Reciprocal GTPase handoff + recycling | Ffh + FtsY GTPase domains | PP_1461 + PP_5111 | **covered** | SRP54-type GTP-binding domain (PROSITE PS00300) on both |

**No module step is a gap or "not expected."** The module is complete. The only nuance is that step 1b depends on a non-coding RNA that a proteome-only candidate list cannot represent.

---

## 4. Candidate genes and evidence (module-relevant genes)

**Ffh — `ffh` / PP_1461 / Q88MV7 (458 aa).**
- Role: binds the hydrophobic signal sequence of the RNC and the SRP RNA; forms SRP; delivers cargo to FtsY; GTPase.
- Evidence: ProteinExistence level 3 (inferred from homology); HAMAP-Rule MF_00306; GO GTPase activity, 7S RNA binding, SRP complex, SRP-dependent cotranslational targeting (all IEA). SRP54-type GTP-binding domain (PS00300).
- Caveats: EC 3.6.5.4 is the generic SRP-GTPase EC and is fine here. No direct KT2440 data, but transfer is strong (essential, universally conserved, single-copy).

**FtsY — `ftsY` / PP_5111 / Q88CR9 (494 aa).**
- Role: membrane-associated SRP receptor; captures RNC·SRP; reciprocal GTPase; hands RNC to Sec translocase; dissociates.
- Evidence: ProteinExistence level 3; HAMAP-Rule MF_00920; GO GTPase activity, signal recognition particle binding, plasma membrane, SRP-dependent targeting (all IEA). SRP54-type GTP-binding domain (PS00300).
- Caveats: Same generic EC 3.6.5.4; appropriate. Note FtsY in *E. coli* lacks the eukaryotic SRα "A-domain" architecture; the KT2440 protein is the standard bacterial one-domain-linker + NG-domain form — no transfer concern.

**SRP RNA — `ffs` / PP_mr50 / PP_RS22200 (GeneID 26969983, ~97 nt).**
- Role: RNA scaffold of SRP; accelerates and catalyzes Ffh–FtsY complex assembly and GTPase activation.
- Evidence: **Direct genome annotation** in KT2440 (NCBI Gene); Rfam RF00169. Not in the proteome candidate list because it is non-coding.
- Caveat: Must be curated as a non-protein module component.

*(The remaining 15 candidate genes — SecY/E/G, SecA/B, SecDF/YajC, YidC, LepB, LspA, and both Tat operons — are annotated correctly but belong to downstream/parallel modules and are out of scope for this module's satisfiability.)*

---

## 5. Gaps, ambiguities, and likely over-annotations

- **No true gaps** in the SRP-targeting module for KT2440.
- **Apparent gap that is actually a metadata artifact:** the SRP RNA (`ffs`) is missing from the candidate list only because the list is proteome-derived. Resolved — the locus exists (PP_mr50).
- **Bucket-level over-inclusion (the main curation issue):** KEGG `ppu03060` conflates ≥5 distinct processes (SRP targeting, Sec translocation, YidC insertion, signal-peptide cleavage, Tat export). Scoring all 19 genes as "module coverage" would badly over-count. Only `ffh` + `ftsY` (+`ffs`) count toward *this* module.
- **Paralog notes (informational, out of module scope):** KT2440 carries a **duplicated Tat system** (tatABC-I at PP_1039–1041 and tatABC-II at PP_5016–5018) — a genuine *Pseudomonas* feature, but irrelevant to SRP. Ffh and FtsY themselves have **no paralogs**.
- **No over-propagated SRP annotations detected:** the `ffh`/`ftsY` calls are specific, rule-based, and unambiguous.

---

## 6. Module and GO-curation recommendations

**Per-step disposition:**
- Step 1a (Ffh signal binding): **covered** → PP_1461.
- Step 1b (SRP-RNA binding): **covered** → non-protein locus `ffs`/PP_mr50; add an explicit note that this module requires a non-coding-RNA component tracked outside UP000000556.
- Step 2 (FtsY engagement): **covered** → PP_5111.
- Step 3 (reciprocal GTPase handoff/recycling): **covered** → PP_1461 + PP_5111 (GTPase domains).

**Module-level:**
- Mark the SRP-targeting module **covered/satisfied** for KT2440.
- **Do not** treat KEGG `ppu03060` as coextensive with this module. Recommend either (a) splitting the bucket in local metadata into SRP-targeting / Sec-translocation / YidC / signal-peptidase / Tat sub-modules, or (b) tagging the 17 non-SRP genes as "adjacent, downstream/parallel" so they are not scored as SRP-module coverage.
- **GO curation:** GO:0006614/GO:0006613 is already correctly applied to Ffh and FtsY. Consider adding an SRP-RNA-linked annotation for `ffs` if the local model supports ncRNA participants. No new GO term request appears necessary.
- **New module documents:** not required for SRP itself; a small note documenting the non-protein `ffs` dependency would prevent this false-gap from recurring in other proteome-only reviews.

---

## 7. Genes to promote to full `fetch-gene` review

- **`ffh` / PP_1461** and **`ftsY` / PP_5111** — promote both to full review to formally attach the module-satisfiability call and record that evidence is homology-based (level 3). Low risk, high value for closing the module.
- **`ffs` / PP_mr50 (PP_RS22200)** — flag as a **non-protein locus** requiring a curation path that can register a ncRNA participant; this is the one item most likely to be mishandled by protein-centric tooling.
- The 17 non-SRP genes do **not** need promotion under this module (they belong to their own modules).

---

## 8. Evidence and open questions

**Supported by direct target-organism evidence:** presence of all three loci (`ffh` PP_1461, `ffs` PP_mr50, `ftsY` PP_5111) in the KT2440 genome/proteome; single-copy status of `ffh`/`ftsY`.

**Inferred (homology / rules / neighboring organisms):** the biochemical mechanism (signal recognition → FtsY capture → reciprocal GTPase activation → SecYEG handoff → dissociation) is established in *E. coli*, *B. subtilis*, and *T. aquaticus* (PMIDs 15383838, 15680975, 19174514, 30146170, 35065991) and transferred to KT2440. Essentiality is inferred from other bacteria (e.g., SRP disruption impairs growth in *Lactococcus lactis*, PMID 39378800; `ffs` is essential in *E. coli*, PMID 18805981).

**Open questions / experiments to resolve gaps:**
1. Direct confirmation that `ffh`, `ftsY`, and `ffs` are essential in KT2440 (targeted CRISPRi or a genome-wide essentiality/Tn-seq dataset). No KT2440-specific SRP essentiality study currently exists.
2. Whether *P. putida* SRP substrate range or regulation (e.g., (p)ppGpp inhibition of SRP assembly, shown in *B. subtilis*/*E. coli*, PMID 35217658) behaves as in model organisms — relevant to stress physiology but outside module satisfiability.

---

## Key references

- Shan & Walter, reciprocal SRP–SR GTPase activation, *FEBS Lett* 2005 (PMID 15680975); Shan, Stroud & Walter, *Science* 2004 (PMID 15383838).
- Zhang, Schaffitzel, Ban & Shan, conformational switches driving targeting, *PNAS* 2009 (PMID 19174514).
- Kempf et al., *E. coli* FtsY homodimer & GTPase activation, 2018 (PMID 30146170).
- Mayer et al., cotranslational FtsY membrane targeting & translocon docking, 2022 (PMID 35065991).
- Czech et al., (p)ppGpp inhibits SRP targeting via Ffh/FtsY, *PNAS* 2022 (PMID 35217658).
- Peterson & Phillips, essential `ffs`/4.5S RNA in *E. coli*, 2008 (PMID 18805981).
- Sauerbrei et al., SRP composed of Ffh + 4.5S RNA, Lon controls Ffh levels, 2020 (PMID 32366590).
- Harris & Goldman, FtsY/Ffh/SecY present by LUCA (deep conservation), 2021 (PMID 33684113).
- Wang et al., SRP-pathway disruption phenotypes in *L. lactis*, 2025 (PMID 39378800).
- Resources: UniProt Q88MV7 (Ffh), Q88CR9 (FtsY); HAMAP MF_00306, MF_00920; PROSITE PS00300; NCBI Gene 26969983 (`ffs`, PP_mr50/PP_RS22200); Rfam RF00169.


## Artifacts

- [OpenScientist final report](PSEPK__bacterial_srp_cotranslational_targeting__ppu03060-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__bacterial_srp_cotranslational_targeting__ppu03060-deep-research-openscientist_artifacts/final_report.pdf)