---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T13:27:45.360219'
end_time: '2026-09-01T13:55:26.899117'
duration_seconds: 1661.54
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Bacterial type VI secretion apparatus
  module_summary: A contractile bacterial secretion nanomachine assembled from an
    envelope-spanning membrane complex, a cytoplasmic baseplate, an Hcp tube surrounded
    by a TssBC sheath, a VgrG puncturing tip, and the ClpV ATPase that recycles contracted
    sheath. Cargo effectors, cognate immunity proteins, cargo-specific adapters, and
    global transcriptional regulation are outside this conserved structural boundary.
  module_outline: "- Bacterial type VI secretion apparatus\n  - 1. Envelope-spanning\
    \ membrane complex\n  - TssJLM membrane complex\n    - TssJ outer-membrane lipoprotein\
    \ (molecular player: TssJ family; activity or role: structural molecule activity)\n\
    \    - TssL inner-membrane component (molecular player: TssL family; activity\
    \ or role: structural molecule activity)\n    - TssM trans-envelope component\
    \ (molecular player: TssM family; activity or role: structural molecule activity)\n\
    \  - 2. Baseplate assembly\n  - TssEFGK baseplate\n    - TssE baseplate subunit\
    \ (molecular player: TssE family; activity or role: structural molecule activity)\n\
    \    - TssF baseplate subunit (molecular player: TssF family; activity or role:\
    \ structural molecule activity)\n    - TssG baseplate subunit (molecular player:\
    \ TssG family; activity or role: structural molecule activity)\n    - TssK baseplate\
    \ connector (molecular player: TssK family; activity or role: structural molecule\
    \ activity)\n  - 3. Contractile tube and sheath assembly\n  - Hcp tube and TssBC\
    \ sheath\n    - TssA assembly coordinator (molecular player: TssA family; activity\
    \ or role: structural molecule activity)\n    - Hcp inner-tube subunit (molecular\
    \ player: Hcp/TssD family; activity or role: structural molecule activity)\n \
    \   - TssB sheath subunit (molecular player: TssB family; activity or role: structural\
    \ molecule activity)\n    - TssC sheath subunit (molecular player: TssC family;\
    \ activity or role: structural molecule activity)\n  - 4. Puncturing tip\n  -\
    \ VgrG puncturing tip\n    - VgrG tip component (molecular player: VgrG family;\
    \ activity or role: structural molecule activity)\n  - 5. Contracted-sheath recycling\n\
    \  - ClpV-dependent sheath recycling\n    - ClpV sheath-disassembly ATPase (molecular\
    \ player: ClpV family; activity or role: ATP hydrolysis activity)"
  module_connections: '- TssJLM membrane complex feeds into TssEFGK baseplate

    - TssEFGK baseplate feeds into Hcp tube and TssBC sheath

    - Hcp tube and TssBC sheath feeds into VgrG puncturing tip

    - Hcp tube and TssBC sheath feeds into ClpV-dependent sheath recycling'
  pathway_query: ppu03070
  pathway_id: ppu03070
  pathway_name: Bacterial secretion system
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu03070 with 42 primary genes; module
    area: transport_motility_signaling.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: NCBITaxon:160488
  proteome_id: UP000000556
  candidate_gene_count: '61'
  candidate_genes: '- yidC: PP_0006 | P0A140 | Membrane protein insertase YidC (Foldase
    YidC) (Membrane integrase YidC) (Membrane protein YidC) (primary bucket kegg:ppu03060)

    - secE: PP_0441 | Q88QP7 | Protein translocase subunit SecE (primary bucket kegg:ppu03060)

    - secY: PP_0474 | Q88QL5 | Protein translocase subunit SecY (primary bucket kegg:ppu03060)

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

    - xcpX: PP_1042 | Q88P11 | Type II secretion system protein K (primary bucket
    kegg:ppu03070)

    - xcpP: PP_1045 | Q88P08 | Type II secretion pathway protein XcpP (primary bucket
    kegg:ppu03070)

    - xcpQ: PP_1046 | Q88P07 | Type II secretion pathway protein XcpQ (primary bucket
    kegg:ppu03070)

    - gspE: PP_1047 | Q88P06 | General secretion pathway protein E (primary bucket
    kegg:ppu03070)

    - gspF: PP_1048 | Q88P05 | General secretion pathway protein F (primary bucket
    kegg:ppu03070)

    - gspG: PP_1049 | Q88P04 | Type II secretion system core protein G (primary bucket
    kegg:ppu03070)

    - xcpU: PP_1050 | Q88P03 | Type II secretion pathway protein XcpU (primary bucket
    kegg:ppu03070)

    - ... 45 additional candidate genes omitted from prompt.'
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
citation_count: 15
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__bacterial_type_vi_secretion_apparatus__ppu03070-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__bacterial_type_vi_secretion_apparatus__ppu03070-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Bacterial type VI secretion apparatus in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: NCBITaxon:160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu03070
- Resolved ID: ppu03070
- Resolved name: Bacterial secretion system
- Source: KEGG

Resolved local bucket kegg:ppu03070 with 42 primary genes; module area: transport_motility_signaling.

## Candidate Genes From Local Metadata

Candidate gene count: 61

- yidC: PP_0006 | P0A140 | Membrane protein insertase YidC (Foldase YidC) (Membrane integrase YidC) (Membrane protein YidC) (primary bucket kegg:ppu03060)
- secE: PP_0441 | Q88QP7 | Protein translocase subunit SecE (primary bucket kegg:ppu03060)
- secY: PP_0474 | Q88QL5 | Protein translocase subunit SecY (primary bucket kegg:ppu03060)
- yajC: PP_0834 | Q88PL6 | Sec translocon accessory complex subunit YajC (primary bucket kegg:ppu03060)
- secD: PP_0835 | Q88PL5 | Protein translocase subunit SecD (primary bucket kegg:ppu03060)
- secF: PP_0836 | Q88PL4 | Protein-export membrane protein SecF (primary bucket kegg:ppu03060)
- tatC-I: PP_1039 | Q88P14 | Sec-independent protein translocase protein TatC (primary bucket kegg:ppu03060)
- tatB-I: PP_1040 | Q88P13 | Sec-independent protein translocase TatB (primary bucket kegg:ppu03060)
- tatA-I: PP_1041 | Q88P12 | Sec-independent protein translocase protein TatA (primary bucket kegg:ppu03060)
- xcpX: PP_1042 | Q88P11 | Type II secretion system protein K (primary bucket kegg:ppu03070)
- xcpP: PP_1045 | Q88P08 | Type II secretion pathway protein XcpP (primary bucket kegg:ppu03070)
- xcpQ: PP_1046 | Q88P07 | Type II secretion pathway protein XcpQ (primary bucket kegg:ppu03070)
- gspE: PP_1047 | Q88P06 | General secretion pathway protein E (primary bucket kegg:ppu03070)
- gspF: PP_1048 | Q88P05 | General secretion pathway protein F (primary bucket kegg:ppu03070)
- gspG: PP_1049 | Q88P04 | Type II secretion system core protein G (primary bucket kegg:ppu03070)
- xcpU: PP_1050 | Q88P03 | Type II secretion pathway protein XcpU (primary bucket kegg:ppu03070)
- ... 45 additional candidate genes omitted from prompt.

## Generic Module Context

### Working Scope

A contractile bacterial secretion nanomachine assembled from an envelope-spanning membrane complex, a cytoplasmic baseplate, an Hcp tube surrounded by a TssBC sheath, a VgrG puncturing tip, and the ClpV ATPase that recycles contracted sheath. Cargo effectors, cognate immunity proteins, cargo-specific adapters, and global transcriptional regulation are outside this conserved structural boundary.

### Provisional Biological Outline

- Bacterial type VI secretion apparatus
  - 1. Envelope-spanning membrane complex
  - TssJLM membrane complex
    - TssJ outer-membrane lipoprotein (molecular player: TssJ family; activity or role: structural molecule activity)
    - TssL inner-membrane component (molecular player: TssL family; activity or role: structural molecule activity)
    - TssM trans-envelope component (molecular player: TssM family; activity or role: structural molecule activity)
  - 2. Baseplate assembly
  - TssEFGK baseplate
    - TssE baseplate subunit (molecular player: TssE family; activity or role: structural molecule activity)
    - TssF baseplate subunit (molecular player: TssF family; activity or role: structural molecule activity)
    - TssG baseplate subunit (molecular player: TssG family; activity or role: structural molecule activity)
    - TssK baseplate connector (molecular player: TssK family; activity or role: structural molecule activity)
  - 3. Contractile tube and sheath assembly
  - Hcp tube and TssBC sheath
    - TssA assembly coordinator (molecular player: TssA family; activity or role: structural molecule activity)
    - Hcp inner-tube subunit (molecular player: Hcp/TssD family; activity or role: structural molecule activity)
    - TssB sheath subunit (molecular player: TssB family; activity or role: structural molecule activity)
    - TssC sheath subunit (molecular player: TssC family; activity or role: structural molecule activity)
  - 4. Puncturing tip
  - VgrG puncturing tip
    - VgrG tip component (molecular player: VgrG family; activity or role: structural molecule activity)
  - 5. Contracted-sheath recycling
  - ClpV-dependent sheath recycling
    - ClpV sheath-disassembly ATPase (molecular player: ClpV family; activity or role: ATP hydrolysis activity)

### Known Relationships Among Steps

- TssJLM membrane complex feeds into TssEFGK baseplate
- TssEFGK baseplate feeds into Hcp tube and TssBC sheath
- Hcp tube and TssBC sheath feeds into VgrG puncturing tip
- Hcp tube and TssBC sheath feeds into ClpV-dependent sheath recycling

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

# Type VI Secretion Apparatus in *Pseudomonas putida* KT2440 — Module/Pathway/Taxon Review Brief

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBITaxon:160488; proteome UP000000556)
**Target bucket:** KEGG ppu03070 — "Bacterial secretion system" (broad multi-system map; module area transport_motility_signaling)
**Module under review:** Bacterial type VI secretion apparatus (contractile injection nanomachine)
**Scope of curation task:** Manual module satisfiability and gene-annotation review — not a generic pathway essay.

---

## 1. Executive Summary

The Type VI secretion (T6SS) apparatus module is **strongly satisfiable** in *Pseudomonas putida* KT2440, supported by **direct, species-specific experimental evidence**. The strain encodes **three complete or near-complete T6SS gene clusters** (designated K1, K2, K3) plus several orphan *hcp*/*vgrG*/PAAR islands that supply tube and spike machinery in trans. The **K1 cluster** (locus tags PP_3088–PP_3106, containing the sole genome-wide *clpV1* = PP_3095) is a **complete, standalone, experimentally validated antibacterial apparatus** encoding every one of the 13 canonical core subunits; it secretes Rhs-type effectors and kills competitor bacteria in the rhizosphere (Bernal et al. 2017, [PMID: 28045455](https://pubmed.ncbi.nlm.nih.gov/28045455/); Nie et al. 2022, [PMID: 35178858](https://pubmed.ncbi.nlm.nih.gov/35178858/)).

Two curation caveats dominate this review. **First**, the KEGG bucket ppu03070 is a *broad, multi-system* "Bacterial secretion system" map mixing at least six export machineries (Sec/SRP, Tat, Type II/Xcp, Type I, Type V two-partner secretion, and Type VI). Its KEGG Orthology (KO) layer annotates only **6 of the 13 T6SS core families**; the entire sheath (TssB/TssC), the entire baseplate (TssE/F/G/K), and the TssA cap are **not KO-annotated** in this bucket. Module satisfiability therefore **cannot** be judged from KEGG KO calls and must be reconstructed from InterPro/Pfam domain evidence, UniProt, and primary literature. **Second**, this domain-level reconstruction exposes a concrete, curation-actionable **annotation error**: **PP_3099 is mislabeled as "uricase / urate oxidase (EC 1.7.3.3), gene *puuD*" when it is in fact the K1 sheath large subunit TssC1.** Correcting this single call converts the K1 cluster from apparently "missing TssC" to a complete 13/13 apparatus.

The residual genuine gaps are narrow and specific: **ClpV/TssH is single-copy** (ClpV1 = PP_3095, physically inside K1), so the sheath-recycling step for the K2 and K3 clusters must be trans-supplied or is cryptic; and the **K3 cluster lacks a detectable TssC** large sheath subunit (locus-tag gap at PP_4075). These are the only steps that should be flagged `candidate_uncertain`/`gap` for the K2/K3 sub-apparatuses. All other core steps are `covered` on domain evidence. Type III secretion is confirmed **absent** from KT2440 and should be marked `not_expected_in_target_taxon` where it appears in generic secretion overview maps.

---

## 2. Target-Organism Pathway Definition

### 2.1 What the T6SS module is (and is not)

The T6SS is a **contractile bacterial secretion nanomachine** evolutionarily and structurally homologous to the tail of contractile bacteriophages (Brunet et al. 2015, [PMID: 26460929](https://pubmed.ncbi.nlm.nih.gov/26460929/)). It comprises, mechanistically:

1. an **envelope-spanning membrane complex** (TssJLM) that docks the apparatus and provides the channel for the inner tube;
2. a **cytoplasmic baseplate** (TssEFGK plus VgrG) that serves as the tail-assembly platform and evolutionary adaptor;
3. a **contractile tail** — an **Hcp inner tube** wrapped by a **TssBC sheath**, coordinated by the **TssA cap**;
4. a **VgrG (+PAAR) puncturing tip**; and
5. the **ClpV (TssH) AAA+ ATPase** that recycles the contracted sheath.

Cargo effectors, cognate immunity proteins, effector-specific adaptors (Tap/DUF4123), and global transcriptional regulation lie **outside** the conserved structural boundary of this module and should be curated separately — though they are richly represented in KT2440 (10 effector–immunity pairs; Bernal 2017).

### 2.2 Pathway boundaries — what to keep separate

The KEGG bucket **ppu03070** is *not* a T6SS map; it is the pan-secretion overview for *P. putida* and must be decomposed. Programmatic KO classification of all 61 bucket genes shows it embeds at least six distinct systems:

| Sub-system in ppu03070 | Representative KO / genes | Curation action |
|---|---|---|
| Sec translocon / SRP | secA/Y/E/G/D/F, yajC, yidC, ffh, ftsY, secB (K03070–K03217) | Separate module (protein export) |
| Tat pathway | tatABC (K03116–K03118) | Separate module |
| Type II secretion (Xcp/Gsp) | gspC–L (K02452–K02461) | Separate module |
| Type I secretion | hlyB/hlyD (K11003/K11004), tolC (K12340) | Separate module |
| Type V two-partner secretion | shlA/B (K11016/K11017) | Separate module |
| **Type VI secretion** | **K11891/K11892/K11903/K11904/K11906/K11907** | **This module** |

Critically, the **truncated candidate list surfaced in the commissioning brief** (yidC, sec\*, tat\*, xcp\*/gsp\*) is dominated by Sec/Tat/T2SS genes and **does not represent the T6SS at all**; the actual T6SS genes are among the 45 candidates omitted from the prompt. Any reviewer working only from the visible candidate names would mis-scope the module. **Type III secretion is absent** from KT2440 (no *hrc*/*sct* secretion apparatus; apparent *sctC*/*sctS* hits resolve to sulfur-compound ABC transporters), so it should not be expected in this organism.

### 2.3 Alternate names / database definitions

Core subunits carry multiple synonymous names that fragment free-text annotation: TssB≡VipA≡EvpA; TssC≡VipB≡EvpB; TssH≡ClpV; TssD≡Hcp; TssI≡VgrG; TssM≡IcmF≡ImpL≡VasK; TssL≡DotU≡VasF; TssJ≡VasD/Lip. KEGG KO IDs used in ppu03070: K11891 (TssM), K11892 (TssL), K11906 (TssJ/VasD), K11903 (Hcp), K11904 (VgrG), K11907 (ClpV). There is no dedicated stand-alone "T6SS" KEGG map. KT2440's clusters additionally use a **system-specific numeral** ("1") convention: **ClpV1 / TssB1 / TssC1** all belong to the K1 locus — a useful internal consistency check.

---

## 3. Expected Step Model and Satisfiability

The following table maps each canonical step to KT2440 evidence, per cluster, and gives the recommended module curation status.

| Module step | Core player | KT2440 genes (K1 / K2 / K3) | KO in ppu03070? | Curation call |
|---|---|---|---|---|
| **1. Membrane complex** | TssJ (lipoprotein) | PP_3094 / PP_2618 / PP_4079 | ✔ K11906 | **covered** |
| | TssL (DotU) | PP_3092 / PP_2616 / PP_4081 (+orphan PP_3385) | ✔ K11892 | **covered** |
| | TssM (IcmF) | PP_3090+PP_3091 / PP_2627 / PP_4071 | ✔ K11891 | **covered** (K1 TssM split across 2 ORFs) |
| **2. Baseplate** | TssE (Gp25-like) | PP_3098 / PP_2622 / PP_4076 | ✖ | **covered** (UniProt/Pfam), KEGG gap |
| | TssF | PP_3097 / PP_2621 / PP_4077 | ✖ | **covered**, KEGG gap |
| | TssG | PP_3096 / PP_2620 / PP_4078 | ✖ | **covered**, KEGG gap |
| | TssK | PP_3093 / PP_2617 / PP_4080 | ✖ | **covered**, KEGG gap |
| **3. Tube + sheath** | TssA (cap) | PP_3088 / PP_2626 / PP_4072 | ✖ | **covered** (ImpA N-term), KEGG gap |
| | Hcp (tube) | PP_3089 / PP_2615 / PP_4082 (+orphans PP_4886, PP_5238, PP_0655) | ✔ K11903 | **covered** |
| | TssB (sheath small) | **PP_3100 (IPR008312=TssB1)** / PP_2624 / PP_4074 | ✖ | **covered** all three (K1 only via InterPro) |
| | TssC (sheath large, VipB) | **PP_3099 (mis-annot. "uricase"→TssC1)** / PP_2623 / **absent (PP_4075 gap)** | ✖ | **covered** K1 & K2; **gap** K3 |
| **4. Puncturing tip** | VgrG | PP_3106 / PP_2614 / PP_4049 (+orphan vgrG-II PP_3386) | ✔ K11904 | **covered** |
| | (PAAR sharpener) | — / PP_2610 / PP_4045 | ✖ | accessory; covered where present |
| **5. Sheath recycling** | ClpV (TssH) | **PP_3095 (K1 only; sole genome-wide ClpV)** | ✔ K11907 (single) | **covered K1**; **candidate_uncertain K2/K3** |

*Genome-wide there is exactly one T6SS ClpV (PP_3095); PP_0625/PP_4008/PP_3316 are housekeeping ClpB/ClpA-type chaperones, not T6SS. Type III secretion is absent in KT2440.*

**Verified per-cluster completeness (Pfam-based audit):**

| Cluster | Core subunits present | ClpV | Verdict |
|---|---|---|---|
| **K1** (PP_3088–3106, *clpV1*) | **13/13** (incl. TssB1 PP_3100, TssC1 PP_3099) | ✔ PP_3095 | **complete standalone apparatus** (= functional K1-T6SS) |
| **K2** (PP_2610–2628, *vgrG-I*) | 12/13 (full TssBC sheath, baseplate, membrane) | ✖ | complete except ClpV → recycling trans-shared |
| **K3** (PP_4045–4049 + PP_4071–4085, *vgrG-III*) | 11/13 (**no TssC, no ClpV**) | ✖ | cryptic/trans-dependent |

TssC (Pfam PF05943/PF18945) occurs in exactly two proteins genome-wide (PP_2623 K2, PP_3099 K1); the sole T6SS ClpV is PP_3095. TssJ/TssL confirmed by curated name; all other subunits confirmed one-per-cluster by discriminating Pfam.

---

## 4. Candidate Genes and Evidence

### 4.1 Finding F001 — Three T6SS clusters plus orphan islands (direct, target-strain evidence)

*P. putida* KT2440 was genome-analyzed by Bernal et al. (2017), who identified three T6SS gene clusters (K1-, K2-, K3-T6SS) and 10 effector–immunity pairs. The K1 system is a **potent antibacterial device** secreting the Rhs effector Tke2, active against a broad range of bacteria in the rhizosphere. This is **direct experimental evidence in the target strain** and is the strongest possible support for module presence.

> "Here we analyze the genome of the biocontrol agent *Pseudomonas putida* KT2440 and identify three T6SS gene clusters (K1-, K2- and K3-T6SS). Besides, 10 T6SS effector-immunity pairs were found" — [PMID: 28045455](https://pubmed.ncbi.nlm.nih.gov/28045455/)

> "*Pseudomonas putida* KT2440 possesses a functional T6SS (K1-T6SS) and exhibits antibacterial activity towards a broad range of bacteria" — Nie et al. 2022, [PMID: 35178858](https://pubmed.ncbi.nlm.nih.gov/35178858/)

Subsequent work confirms functional, engineerable T6SSs in this exact strain: KT2440 has been engineered to heterologously deliver antibacterial and antifungal effectors via its T6SS ([PMID: 40176102](https://pubmed.ncbi.nlm.nih.gov/40176102/)); the three systems shape rhizosphere and biofilm community structure ([PMID: 41036489](https://pubmed.ncbi.nlm.nih.gov/41036489/); [PMID: 38096690](https://pubmed.ncbi.nlm.nih.gov/38096690/)); the systems are transcriptionally distinct and independently regulated ([PMID: 36748579](https://pubmed.ncbi.nlm.nih.gov/36748579/)); and a cryo-EM structure of the KT2440 Tap3–Tke5 adaptor–effector complex has been solved ([PMID: 41526723](https://pubmed.ncbi.nlm.nih.gov/41526723/)). The module is unambiguously real and active in the target organism.

### 4.2 Finding F002 — KEGG KO layer covers only 6 of 13 core families

Programmatic KEGG REST mapping of all 61 ppu03070 genes to KO IDs shows the T6SS panel is KO-annotated for only six families: **TssM/IcmF** (K11891; PP_2627, PP_3090, PP_3091, PP_4071), **TssL/DotU** (K11892; PP_2616, PP_3092, PP_3385, PP_4081), **TssJ** lipoprotein (K11906; PP_2618, PP_3094, PP_4079), **Hcp** (K11903; PP_2615, PP_3089, PP_4082, PP_4886, PP_5238), **VgrG** (K11904; PP_2614, PP_3106, PP_3386, PP_4049), and **ClpV** (K11907; single copy PP_3095). There is **no KO annotation in this bucket** for the sheath (TssB, TssC), the baseplate (TssE/F/G/K), or the TssA cap. Since the canonical apparatus comprises 13 core subunits (Brunet 2015, [PMID: 26460929](https://pubmed.ncbi.nlm.nih.gov/26460929/)), the KO layer leaves **7 of 13 steps invisible**. KEGG gene descriptions here are largely "conserved protein of unknown function," signalling shallow annotation depth. **Curation consequence:** do not judge module satisfiability from KEGG KO coverage — it will produce false gaps.

> "The 13 T6SS subunits assemble a cytoplasmic contractile structure anchored to the cell envelope by a membrane-spanning complex." — [PMID: 26460929](https://pubmed.ncbi.nlm.nih.gov/26460929/)

### 4.3 Findings F004/F005 — Full per-cluster reconstruction from UniProt; ClpV single-copy

Reconstruction of the three clusters from UniProt proteome UP000000556 resolves **every canonical core subunit**, most unannotated in KEGG (Section 3 table). Key facts for curation:

- **TssM/IcmF** in K1 is **split across two ORFs** (PP_3090 + PP_3091) — a real biological/annotation feature to preserve, not merge blindly.
- **ClpV/TssH is single-copy genome-wide**: a proteome-wide search for ClpV/ClpB AAA+ ATPases returns exactly **one** T6SS ClpV, **ClpV1 = PP_3095**, embedded in K1. The only other Clp ATPases are housekeeping chaperones (ClpB = PP_0625, ClpA = PP_4008, PP_3316), **not** T6SS-associated. The K2 (PP_2610–2628) and K3 (PP_4071–4085) windows contain **no** *clpV*.
- **Sheath annotation is asymmetric on free-text names**: K2 has clearly named TssB (PP_2624, 167 aa) and TssC (PP_2623, 496 aa); K1's sheath was initially represented only by PP_3100 ("Type VI secretion protein," 191 aa) with the operon apparently interrupted by an unrelated "uricase" gene; K3 has TssB (PP_4074) but its expected large-subunit locus (PP_4075) is unannotated.

**High-confidence, direct target-organism support** exists for the Hcp tube (secretion is the classic functional readout, demonstrated for K1), the VgrG tip (engineered VgrG-dependent delivery shown in KT2440), ClpV1, and the three TssJLM membrane complexes. Baseplate TssE/F/G/K, sheath TssB/TssC, and TssA are **same-organism UniProt/Pfam** calls in canonical operon order — transfer is **strong** because these are same-genome ORFs, not cross-species inference.

### 4.4 Finding F006 — InterPro rescues subunits that free-text names miss

InterPro/Pfam annotation resolves what free-text names hide. **PP_3100** (191 aa), named merely "Type VI secretion protein," carries **IPR008312 = T6SS sheath protein TssB1** — it *is* the K1 small sheath subunit, and the shared "1" (ClpV1/TssB1) confirms a coherent K1 locus. Baseplate and membrane families are cleanly resolved in all clusters by InterPro (TssK IPR010263, TssF IPR010272, TssG IPR010732, ClpV1 IPR017729). **Curation consequence:** InterPro/Pfam is the authoritative layer for this module in KT2440; name-based searches systematically under-count.

### 4.5 Finding F007 — PP_3099 "uricase" is actually TssC1 (a real annotation error)

This is the single most curation-actionable finding. **PP_3099** (500 aa) is annotated in UniProt as *"Uricase/urate oxidase (EC 1.7.3.3), gene name puuD"*, yet domain analysis shows it carries **IPR010269 (TssC-like), IPR044031 (TssC1 N-terminal), IPR044032 (TssC1 C-terminal), and Pfam PF05943 + PF18945 (EvpB/VipB tail-sheath domains)** — identical to the bona fide TssC PP_2623 (K2; same Pfams) — and carries **no uricase Pfam (PF01014)**. Its **genomic position is exactly the expected TssC slot**, between TssE (PP_3098) and TssB1 (PP_3100), inside the K1/ClpV1 operon. A genome-wide scan for the sheath-large domain (PF05943/PF18945) returns **exactly two** proteins: PP_2623 (K2) and PP_3099 (K1). The complementary TssB scan (IPR008312/PF05591) returns **exactly three** (PP_2624 K2, PP_3100 K1, PP_4074 K3) — one per cluster.

**Correcting PP_3099 → TssC1 completes the K1 cluster as a 13/13 standalone apparatus**, consistent with its experimentally validated antibacterial function. A curation trap to note: **IPR010269 ("TssC-like") is a broad superfamily also hit by TssF** (PP_2621, PP_4077); discriminate TssC from TssF using PF05943 (TssC) vs PF05947 (TssF).

### 4.6 Finding F008 — Verified per-cluster completeness matrix

Systematic Pfam-based enumeration binned to clusters confirms **one copy per cluster** for TssA (PF06812), TssB (PF05591), TssE (PF04965), TssF (PF05947), TssG (PF06996), TssK (PF05936), TssM (PF06761), Hcp (PF05638; plus orphans PP_4886/PP_5238/PP_0655), and VgrG (PF05954; plus orphan vgrG-II PP_3386). TssJ and TssL are confirmed by curated names. **TssC (PF05943) returns exactly two proteins genome-wide** — PP_3099 (K1) and PP_2623 (K2) — so **K3 has no TssC**. **Net: K1 = 13/13, K2 = 12/13 (no ClpV), K3 = 11/13 (no TssC, no ClpV).**

---

## 5. Mechanistic Model / Interpretation

### 5.1 Assembly logic (supported by structural literature)

```
   OUTER MEMBRANE ┌── TssJ (OM lipoprotein) ─────────────┐
                  │                                      │  MEMBRANE COMPLEX
   INNER MEMBRANE ├── TssL (DotU) ── TssM (IcmF) ────────┘  (TssJLM)
                  │        │  recruits baseplate via TssG/TssK contacts
   CYTOPLASM      ▼        ▼
             TssE·TssF·TssG·TssK + VgrG ── BASEPLATE (assembly platform)
                          │  TssA caps and coordinates polymerization
                          ▼
             Hcp inner tube  ⇄  TssB/TssC sheath (extended)
                          │  sheath contracts → propels VgrG(+PAAR) tip + effectors
                          ▼
             ClpV (TssH) AAA+ ATPase recycles contracted sheath → next firing
```

This assembly order — membrane complex → baseplate → tail tube/sheath → contraction → ClpV recycling — is established by structural and biochemical work in enteroaggregative *E. coli* (EAEC): baseplate biogenesis and structure ([PMID: 30323254](https://pubmed.ncbi.nlm.nih.gov/30323254/)), TssEFGK–VgrG recruitment to TssJLM ([PMID: 26460929](https://pubmed.ncbi.nlm.nih.gov/26460929/)), TssL–baseplate–membrane contacts ([PMID: 27600409](https://pubmed.ncbi.nlm.nih.gov/27600409/)), the TssM–TssG interface ([PMID: 27600411](https://pubmed.ncbi.nlm.nih.gov/27600411/)), VgrG–Hcp adaptor function ([PMID: 30031895](https://pubmed.ncbi.nlm.nih.gov/30031895/)), TssB sheath structure/function ([PMID: 29223729](https://pubmed.ncbi.nlm.nih.gov/29223729/)), and the TssA cap ([PMID: 28817192](https://pubmed.ncbi.nlm.nih.gov/28817192/)). Transfer of this framework from EAEC to KT2440 is **strong** at the level of subunit identity and assembly order (universally conserved architecture), but fine details (e.g., the domesticated MltE transglycosylase required for membrane-complex assembly through peptidoglycan, [PMID: 27920034](https://pubmed.ncbi.nlm.nih.gov/27920034/)) are **inferred, not directly demonstrated in KT2440.**

### 5.2 The three-cluster division of labor in KT2440

The most parsimonious interpretation is that **K1 is a fully autonomous apparatus** (13/13, with its own ClpV1 and validated antibacterial output), whereas **K2 and K3 are structurally near-complete tails that depend on trans-acting or shared components** for two steps:

- **Sheath recycling (ClpV):** With only one ClpV in the genome (ClpV1/PP_3095, physically in K1), the K2 and K3 sheaths must either (a) be recycled by ClpV1 acting in trans, (b) fire only once without recycling, or (c) be recycled by an as-yet-unrecognized enzyme. ClpV recognizes a cognate TssC N-terminal helix, so cross-recycling is not guaranteed. This step is genuinely **candidate_uncertain** for K2/K3.
- **TssC in K3:** The K3 locus has TssB (PP_4074) but no detectable TssC (PF05943) — the slot PP_4075 is not present as a separate VipB-domain ORF. K3 may therefore be **degenerate/pseudogenized**, or its large sheath subunit may be supplied in trans by TssC1 or TssC2. This is the one genuine core **gap**.

The three systems are transcriptionally distinct and independently regulated ([PMID: 36748579](https://pubmed.ncbi.nlm.nih.gov/36748579/)), consistent with functional specialization rather than pure redundancy.

### 5.3 Why the KEGG bucket misleads

The confusion at every level of this review traces to two annotation-layer facts: (1) ppu03070 is a **pan-secretion overview** intermixing six systems, and (2) its KO layer covers fewer than half the T6SS core families and leaves the sheath/baseplate/cap as "unknown function." The correct KT2440 T6SS annotation is only visible at the **InterPro/Pfam** layer — which additionally corrects a false EC-numbered enzyme call (PP_3099 "uricase"). This is a textbook example of why module satisfiability must be judged on domain evidence and primary literature, not on pathway-database bucket membership.

---

## 6. Gaps, Ambiguities, and Likely Over-Annotations

| Item | Type | Locus | Recommendation |
|---|---|---|---|
| PP_3099 "Uricase (EC 1.7.3.3), *puuD*" | **Annotation error** | K1 | Re-annotate as **TssC1** (sheath large subunit); remove EC 1.7.3.3; promote to `fetch-gene` |
| ClpV single-copy | Real functional gap for K2/K3 | PP_3095 (K1 only) | Mark K2/K3 recycling step `candidate_uncertain`; test trans-recycling |
| K3 TssC absent | Real core gap | slot PP_4075 | Mark K3 sheath-large step `gap`; check for pseudogene / trans-sharing |
| PP_3100 "Type VI secretion protein" | Under-annotation | K1 | Promote to **TssB1** (InterPro IPR008312) |
| IPR010269 "TssC-like" hitting TssF | **Over-broad domain** | PP_2621, PP_4077 | Do not assign TssC from IPR010269 alone; require PF05943/PF18945 |
| K11892 TssL/DotU multi-mapping | Paralog ambiguity | PP_2616, PP_3092, PP_3385, PP_4081 | Resolve per-cluster; PP_3385 is an orphan tssL near orphan vgrG PP_3386 |
| Hcp/VgrG multi-copy | Expected biology, not error | orphans PP_4886/PP_5238/PP_0655, PP_3386 | Curate as trans-acting tube/spike modules or effectors, not duplicates |
| TssM split ORF in K1 | Structural feature | PP_3090+PP_3091 | Preserve as two ORFs; do not force-merge |
| Type III secretion | Absent | — | Mark `not_expected_in_target_taxon` in generic maps |
| Sec/Tat/SRP/T1SS/T2SS/T5SS in ppu03070 | Boundary over-inclusion | many | Do not pull into the T6SS module; KEGG-map artifact |

**Likely over-propagation risk:** the broad "TssC-like" superfamily (IPR010269) and the generic KO "unknown function" labels are the two places most likely to generate false or missing T6SS annotations for related *Pseudomonas* proteomes. Any automated pipeline that trusts EC 1.7.3.3 on PP_3099 will silently break the K1 module. **Cluster-naming caveat:** the K1/K2/K3 labels here are mapped to genomic loci by inference (the ClpV1-containing locus PP_3088–3106 → "K1"); the exact K2 vs K3 correspondence should be confirmed against Bernal et al. before hard-coding into module documents.

---

## 7. Module and GO-Curation Recommendations

- **Mark covered:** membrane complex (TssJLM), baseplate (TssEFGK), Hcp tube, sheath (TssBC), VgrG tip, and ClpV recycling are ALL covered for the **K1 cluster** (a complete standalone apparatus once PP_3099 is corrected to TssC1). K2 is covered for all steps except ClpV; at the genome level every core family is present.
- **Mark candidate_uncertain / gap:** ClpV-dependent recycling for K2/K3 (single genome-wide ClpV1); TssC for K3 (no PF05943/PF18945 protein at slot PP_4075).
- **Correct an annotation error:** PP_3099 must be re-typed from uricase (EC 1.7.3.3) to TssC1 — the key data-quality action.
- **Not a gap / not_expected:** none of the core steps should be marked "not expected"; the full core is present. Type III secretion, a *neighboring* system, *is* `not_expected_in_target_taxon`.
- **module_needs_revision (generic boundary):** the generic module treats the apparatus as single-copy. For KT2440 the module should be **instantiated three times (K1/K2/K3)** or carry an explicit "paralogous multi-copy" flag, and the single-ClpV topology (one ATPase potentially serving multiple clusters) should be representable. The architectural boundary itself (membrane complex → baseplate → tail → tip → recycling) is **correct** and does not need revision.
- **Annotation-source note:** because KEGG ppu03070 KO-annotates only 6/13 core families, satisfiability must be evaluated against **UniProt/InterPro/Pfam**, not KEGG KO alone. Recommend adding InterPro signatures (TssA/ImpA, TssE/Gp25-like, TssF/TssG, TssK, VipA/VipB sheath) to the module's evidence sources.
- **GO usage:** structural subunits map to *T6SS complex* (GO:0033104) and *protein secretion by the T6SS* (GO:0033103); ClpV to ATP hydrolysis activity (GO:0016887). No new GO term appears strictly required, but a GO/annotation request to capture per-cluster sheath (TssB/TssC) and TssA in KEGG would close the KO gap.

---

## 8. Genes to Promote to Full `fetch-gene` Review

1. **PP_3099 — top priority: correct "uricase (EC 1.7.3.3)" → TssC1** (sheath large subunit; PF05943/PF18945). A clear erroneous annotation that also completes the K1 sheath.
2. **PP_3095 (ClpV1)** — sole genome-wide recycling ATPase; test whether it services K2/K3 in trans (defines their functionality).
3. **PP_4075 slot / K3 TssC** — confirm true loss (pseudogene, frameshift, or genuine absence) before finalizing the K3 `gap`.
4. **PP_3100 (TssB1, currently "Type VI secretion protein")** — rename to TssB (IPR008312).
5. **PP_3090 + PP_3091 (K1 TssM/IcmF)** — resolve whether this is a split/fused TssM annotation, not an assembly artifact.
6. **PP_3385 / PP_3386 (orphan tssL / vgrG-II)** — clarify whether these form a fourth partial system or are trans-acting accessories.
7. **Orphan Hcp (PP_4886, PP_5238, PP_0655)** — determine whether tube components of a cluster or standalone effector/immunity modules.

---

## 9. Limitations and Knowledge Gaps

- **Cluster-to-window binning** relied on locus-tag adjacency; a few accessory genes at cluster edges may be mis-binned. This does not affect the core-subunit calls, which are domain-anchored.
- **ClpV trans-recycling for K2/K3 is a hypothesis**, not demonstrated. Whether ClpV1 recognizes K2/K3 TssC N-termini is untested in KT2440.
- **K3 TssC absence** is a negative result from domain scanning; a highly divergent or frameshifted TssC could evade PF05943 detection. This warrants direct sequence inspection of the PP_4074–PP_4076 interval.
- **Mechanistic transfer from EAEC** (assembly order, MltE peptidoglycan domestication, VgrG–Hcp adaptor mechanism) is homology-based; target-strain evidence is strongest for K1 *function* (Bernal 2017) but not for step-by-step *assembly* in KT2440.
- This review deliberately **excluded** effectors, immunity proteins, adaptors, and regulation from the module boundary; KT2440's rich effector repertoire (10 E–I pairs; Tke2, Tke5, Tap3) is documented but out of module scope.

---

## 10. Proposed Follow-up Experiments / Actions

1. **Re-annotate PP_3099 → TssC1** in the local metadata and submit an error report to UniProt/KEGG (removes spurious EC 1.7.3.3).
2. **Sequence-inspect the K3 PP_4074–PP_4076 interval** for a cryptic/frameshifted TssC before finalizing the K3 `gap` call.
3. **Test ClpV1 trans-function:** a Δ*clpV1* mutant assayed for K2- and K3-dependent secretion would resolve whether recycling is shared or K1-exclusive.
4. **Confirm the K1 TssM split** (PP_3090/PP_3091) by RNA-seq operon structure or targeted sequencing.
5. **Run an InterPro/Pfam sweep as the primary annotation layer** for all *Pseudomonas* T6SS curation, using PF05943 (TssC) vs PF05947 (TssF) to avoid the IPR010269 superfamily trap.
6. **Expert question for T6SS specialists:** Do the three KT2440 systems share the single ClpV1, and is K3 a functional or degenerate apparatus?

---

## 11. Key References

| PMID | Relevance & evidence type |
|---|---|
| [28045455](https://pubmed.ncbi.nlm.nih.gov/28045455/) | **Primary target-strain evidence:** three T6SS clusters (K1/K2/K3) and 10 effector–immunity pairs in KT2440; K1 antibacterial function (Tke2). *Direct.* |
| [35178858](https://pubmed.ncbi.nlm.nih.gov/35178858/) | Confirms K1-T6SS is a functional antibacterial apparatus in KT2440; c-di-GMP/Wsp regulation. *Direct.* |
| [36748579](https://pubmed.ncbi.nlm.nih.gov/36748579/) | Transcriptional organization/regulation of the three *P. putida* T6SSs. *Direct.* |
| [40176102](https://pubmed.ncbi.nlm.nih.gov/40176102/) | Engineering KT2440 T6SS for VgrG/PAAR-dependent effector delivery. *Direct.* |
| [41036489](https://pubmed.ncbi.nlm.nih.gov/41036489/); [38096690](https://pubmed.ncbi.nlm.nih.gov/38096690/) | KT2440 T6SS shapes rhizosphere/biofilm community structure. *Direct.* |
| [41526723](https://pubmed.ncbi.nlm.nih.gov/41526723/) | Cryo-EM of KT2440 Tap3–Tke5 adaptor–effector complex (effector biology; outside structural module). *Direct.* |
| [26460929](https://pubmed.ncbi.nlm.nih.gov/26460929/) | Canonical 13-subunit core; TssEFGK–VgrG baseplate recruitment to TssJLM — the reference model for satisfiability. *Generic; strong transfer.* |
| [30323254](https://pubmed.ncbi.nlm.nih.gov/30323254/) | Cryo-EM baseplate structure and biogenesis pathway (EAEC). *Generic; structural reference.* |
| [27600409](https://pubmed.ncbi.nlm.nih.gov/27600409/) | TssL–baseplate–membrane complex interactions. *Generic.* |
| [27600411](https://pubmed.ncbi.nlm.nih.gov/27600411/) | TssM cytoplasmic domain–TssG baseplate interface. *Generic.* |
| [30031895](https://pubmed.ncbi.nlm.nih.gov/30031895/) | VgrG serves as adaptor to nucleate Hcp tube assembly. *Generic.* |
| [29223729](https://pubmed.ncbi.nlm.nih.gov/29223729/) | TssB sheath subunit structure/function. *Generic.* |
| [28817192](https://pubmed.ncbi.nlm.nih.gov/28817192/) | TssA cap coordinates tube/sheath polymerization. *Generic.* |
| [27920034](https://pubmed.ncbi.nlm.nih.gov/27920034/) | MltE transglycosylase domestication for membrane-complex assembly (mechanistic detail, EAEC). *Generic; inferred for KT2440.* |

---

### Evidence-strength summary

- **Direct experimental (KT2440):** presence of three clusters; K1 functional antibacterial activity; Hcp/effector secretion; regulation by c-di-GMP/Wsp; engineered effector delivery; Tap3–Tke5 structure.
- **Same-organism sequence/UniProt annotation (strong):** completeness of all 13 core subunits in K1; near-completeness of K2/K3.
- **Cross-species homology (conserved core, strong transfer):** subunit roles/architecture and assembly order from EAEC/*E. coli* structural work.
- **Open questions:** ClpV provisioning for K2/K3; firing status of K2/K3; true absence vs. cryptic K3 TssC; whether orphan *hcp*/*vgrG* are standalone effectors.

*Report prepared for manual module satisfiability and gene-annotation curation. Bottom line: module presence in KT2440 is direct and experimentally validated (K1); per-step completeness is domain-evidence-based (InterPro/Pfam); the mislabeling of PP_3099 as uricase and the single-copy ClpV / K3-TssC questions are the concrete curation actions.*


## Artifacts

- [OpenScientist final report](PSEPK__bacterial_type_vi_secretion_apparatus__ppu03070-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__bacterial_type_vi_secretion_apparatus__ppu03070-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:28045455
2. PMID:35178858
3. PMID:26460929
4. PMID:40176102
5. PMID:41036489
6. PMID:38096690
7. PMID:36748579
8. PMID:41526723
9. PMID:30323254
10. PMID:27600409
11. PMID:27600411
12. PMID:30031895
13. PMID:29223729
14. PMID:28817192
15. PMID:27920034