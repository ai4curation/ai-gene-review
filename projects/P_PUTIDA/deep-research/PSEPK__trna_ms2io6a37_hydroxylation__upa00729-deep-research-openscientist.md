---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T13:27:22.298660'
end_time: '2026-07-11T13:47:13.066474'
duration_seconds: 1190.77
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: tRNA ms2io6A37 hydroxylation
  module_summary: A Pseudomonas putida KT2440 UniPathway UPA00729 module for the terminal
    oxygen-dependent hydroxylation step that converts ms2i6A37-modified tRNA to ms2io6A37-modified
    tRNA. The module is centered on miaE (PP_2188, UniProtKB:Q88KV1). The upstream
    MiaA and MiaB reactions that generate the ms2i6A37 substrate are pathway context,
    not members of this single-gene UniPathway bucket.
  module_outline: "- tRNA ms2io6A37 hydroxylation\n  - 1. MiaE-dependent hydroxylation\
    \ of ms2i6A37-tRNA\n  - MiaE tRNA ms2io6A37 hydroxylation\n    - miaE: tRNA ms2i6A37\
    \ hydroxylase (molecular player: PSEPK miaE; activity or role: tRNA 2-(methylsulfanyl)-N(6)-isopentenyladenosine(37)\
    \ hydroxylase activity)"
  module_connections: No explicit connections.
  pathway_query: UPA00729
  pathway_id: UPA00729
  pathway_name: UniPathway UPA00729
  pathway_source: UniPathway
  pathway_context: 'Resolved local bucket unipathway:UPA00729 with 1 primary genes;
    module area: unipathway.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '1'
  candidate_genes: '- miaE: PP_2188 | Q88KV1 | tRNA 2-(methylsulfanyl)-N(6)-isopentenyladenosine(37)
    hydroxylase (EC 1.14.99.69) (2-methylthio-N6-isopentenyladenosine(37)-tRNA monooxygenase)
    (tRNA-(ms[2]io[6]A37)-hydroxylase) (EC 1.14.99.69; primary bucket unipathway:UPA00729)'
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
citation_count: 4
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__trna_ms2io6a37_hydroxylation__upa00729-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__trna_ms2io6a37_hydroxylation__upa00729-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

tRNA ms2io6A37 hydroxylation in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: UPA00729
- Resolved ID: UPA00729
- Resolved name: UniPathway UPA00729
- Source: UniPathway

Resolved local bucket unipathway:UPA00729 with 1 primary genes; module area: unipathway.

## Candidate Genes From Local Metadata

Candidate gene count: 1

- miaE: PP_2188 | Q88KV1 | tRNA 2-(methylsulfanyl)-N(6)-isopentenyladenosine(37) hydroxylase (EC 1.14.99.69) (2-methylthio-N6-isopentenyladenosine(37)-tRNA monooxygenase) (tRNA-(ms[2]io[6]A37)-hydroxylase) (EC 1.14.99.69; primary bucket unipathway:UPA00729)

## Generic Module Context

### Working Scope

A Pseudomonas putida KT2440 UniPathway UPA00729 module for the terminal oxygen-dependent hydroxylation step that converts ms2i6A37-modified tRNA to ms2io6A37-modified tRNA. The module is centered on miaE (PP_2188, UniProtKB:Q88KV1). The upstream MiaA and MiaB reactions that generate the ms2i6A37 substrate are pathway context, not members of this single-gene UniPathway bucket.

### Provisional Biological Outline

- tRNA ms2io6A37 hydroxylation
  - 1. MiaE-dependent hydroxylation of ms2i6A37-tRNA
  - MiaE tRNA ms2io6A37 hydroxylation
    - miaE: tRNA ms2i6A37 hydroxylase (molecular player: PSEPK miaE; activity or role: tRNA 2-(methylsulfanyl)-N(6)-isopentenyladenosine(37) hydroxylase activity)

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

# Module/Pathway/Taxon Review: tRNA ms2io6A37 Hydroxylation (UPA00729) in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (organism code PSEPK; NCBI taxon 160488; proteome UP000000556)
**Target bucket:** UniPathway UPA00729 — terminal O2-dependent hydroxylation of ms2i6A37-tRNA → ms2io6A37-tRNA
**Candidate gene(s):** miaE (PP_2188 | UniProtKB Q88KV1)

---

## 1. Executive Summary

The UniPathway UPA00729 bucket for *P. putida* KT2440 contains a single enzyme member, **MiaE (PP_2188, Q88KV1)**, the tRNA (ms2io6A37) hydroxylase. On the narrow question of whether that terminal hydroxylation *enzyme* is present and functional in KT2440, the evidence is **unusually strong**: Q88KV1 is a reviewed Swiss-Prot entry with protein-level existence evidence (PE1), four experimental X-ray structures (PDB 2ITB, 6ZMA, 6ZMB, 6ZMC), an assigned EC number (1.14.99.69), a dedicated Pfam family (PF06175/MiaE) and InterPro entry (IPR010386), and a dedicated primary paper — Carpentier et al. 2020 ([PMID: 32785618](https://pubmed.ncbi.nlm.nih.gov/32785618/)) — that reports the in vivo activity, biochemistry, spectroscopy, and crystal structure of MiaE *from P. putida* and explicitly concludes that PP_2188 encodes a functional MiaE. **This step should be marked COVERED with high confidence and no paralog ambiguity.**

However, a species-aware review of the *pathway that supplies MiaE's canonical substrate* uncovers an important curation caveat. The canonical ms2io6A37 route requires an upstream methylthiotransferase, **MiaB (EC 2.8.4.3, K06168)**, to convert i6A37 into the 2-methylthio substrate ms2i6A37 that MiaE then hydroxylates. Three orthogonal lines of evidence — UniProt/InterPro proteome inspection, KEGG orthology, and direct sequence-homology comparison — indicate that **KT2440 has no MiaB**. Its only radical-SAM methylthiotransferase, PP_1197 (Q88NL0), is unambiguously **RimO** (uS12-Asp88 methylthiotransferase, EC 2.8.4.4), not MiaB. A positive/negative control against *P. aeruginosa* PAO1 (which is MiaB-positive and carries two IPR005839 proteins) confirms the KT2440 single-methylthiotransferase count is real, not an annotation gap.

The consequence for module curation is subtle but important. The **enzyme step is covered**, but the **native physiological product in KT2440 is candidate_uncertain**. MiaA (PP_4895, EC 2.5.1.75) is present and produces i6A37, and MiaE is documented to hydroxylate i6A directly in vitro; so in a MiaB-minus background the physiological product is most plausibly **io6A37, not ms2io6A37**. Critically, the Carpentier 2020 demonstration of ms2io6A production was performed in a *heterologous E. coli TOP10 host that supplies ms2i6A* — not in native *P. putida* tRNA — so no published dataset directly establishes that KT2440 makes ms2io6A in vivo. The module's generic "ms2io6A37" product label may therefore be wrong for this organism and should be flagged **module_needs_revision** pending direct LC-MS nucleoside analysis of KT2440 tRNA.

---

## 2. Target-Organism Pathway Definition

### What UPA00729 includes

UPA00729 covers **exactly one biochemical reaction**: the O2-dependent, allylic hydroxylation of the isopentenyl side chain of a 2-methylthio-N6-isopentenyladenosine at position 37 of tRNA, producing the *cis*-4-hydroxyisopentenyl derivative:

```
ms2i6A37-tRNA  +  O2  +  [reductant]  --MiaE-->  ms2io6A37-tRNA  +  H2O
                                       (EC 1.14.99.69)
```

This is the **terminal tail-end modification** in the biosynthesis of the hypermodified wobble-adjacent nucleoside ms2io6A37, found on tRNAs reading codons starting with U (tRNA^Ser, tRNA^Trp, tRNA^Tyr, tRNA^Phe, tRNA^Cys, etc.). Position 37 (3′-adjacent to the anticodon) modifications stabilize codon–anticodon pairing and maintain reading-frame fidelity.

### Neighboring processes to keep separate

- **UPA00729 is a single-gene bucket.** The upstream reactions belong to the same overall biosynthetic *pathway context* but are **not members of this UniPathway bucket**:
  - **MiaA** (Δ2-isopentenylpyrophosphate:tRNA isopentenyltransferase, EC 2.5.1.75) — makes i6A37 from A37. Present in KT2440 as **PP_4895 (Q88DD2)**.
  - **MiaB** (tRNA i6A37 methylthiotransferase, EC 2.8.4.3, K06168) — converts i6A37 → ms2i6A37. **Apparently absent in KT2440** (see §5).
- **RimO** (ribosomal protein uS12 methylthiotransferase, EC 2.8.4.4) is a *paralogous radical-SAM methylthiotransferase acting on protein, not tRNA*. It must be kept strictly separate — it is the source of a real paralog-confusion risk in this proteome (see §5).
- Broad overview maps such as "tRNA modification" (KEGG map / GO:0006400) or "sulfur relay" should not be conflated with this single terminal hydroxylation step.

### Alternate names and database definitions

| Resource | Identifier | Label |
|---|---|---|
| UniPathway | UPA00729 | terminal ms2i6A37 → ms2io6A37 hydroxylation |
| EC | 1.14.99.69 | tRNA (ms2io6A37) hydroxylase / 2-methylthio-N6-isopentenyladenosine(37)-tRNA monooxygenase |
| KEGG ortholog | K06169 | MiaE |
| Pfam | PF06175 | MiaE |
| InterPro | IPR010386 | tRNA-Hydrxlase_MiaE |
| GO (molecular function) | GO:0045301 | tRNA ms2i6A37 hydroxylase activity |
| GO (parent function) | GO:0004497 | monooxygenase activity |
| GO (process) | GO:0006400 | tRNA modification |

Enzyme synonyms in the literature: "MiaE," "tRNA-(ms2io6A37)-hydroxylase," "2-methylthio-N6-isopentenyladenosine(37)-tRNA monooxygenase," "tRNA-modifying monooxygenase."

---

## 3. Expected Step Model

The full ms2io6A37 biosynthetic route and its status in KT2440:

```
                 A37-tRNA
                    |
                    |  MiaA  (EC 2.5.1.75, PP_4895/Q88DD2)      [PRESENT]
                    v
                 i6A37-tRNA
                    |
                    |  MiaB  (EC 2.8.4.3, K06168)               [ABSENT in KT2440]
                    v
                 ms2i6A37-tRNA   <-- canonical UPA00729 substrate
                    |
                    |  MiaE  (EC 1.14.99.69, PP_2188/Q88KV1)    [PRESENT, COVERED]
                    v
                 ms2io6A37-tRNA   <-- generic module product label
```

Because MiaB is missing but MiaA and MiaE are present, the **most parsimonious native route in KT2440 bypasses the 2-methylthio branch**:

```
                 A37 --MiaA--> i6A37 --MiaE--> io6A37   (predicted native product)
```

This is mechanistically supported: MiaE is substrate-promiscuous and hydroxylates i6A (yielding io6A), Cl2i6A, and ms2i6A in vitro ([PMID: 23906247](https://pubmed.ncbi.nlm.nih.gov/23906247/)).

**UPA00729 step status for KT2440:**

| Step | Enzyme / gene | Status |
|---|---|---|
| Terminal hydroxylation (bucket member) | MiaE / PP_2188 | **covered** (direct target-species evidence) |
| Upstream methylthiolation (context, not in bucket) | MiaB / — | **gap / not_present** (lineage-specific loss) |
| Native product identity | — | **candidate_uncertain** (likely io6A, not ms2io6A) |

---

## 4. Candidate Genes and Evidence

### 4.1 MiaE — PP_2188 (Q88KV1) — HIGH CONFIDENCE, COVERED

**Role:** tRNA (ms2io6A37 / io6A37) hydroxylase; nonheme carboxylate-bridged diiron monooxygenase catalyzing the terminal O2-dependent allylic hydroxylation.

**Evidence type — direct, target-organism, experimental (the strongest possible tier):**

- **Reviewed Swiss-Prot, PE1 (protein-level evidence):** Q88KV1 (MIAE_PSEPK), 205 aa, EC 1.14.99.69, Pfam PF06175, InterPro IPR010386. KEGG ppu:PP_2188 = K06169.
- **Four experimental crystal structures:** 2ITB, 6ZMA, 6ZMB, 6ZMC. The enzyme is a diiron four-helix-bundle protein forming a homodimer/monomer with a diiron domain.
- **Dedicated primary paper on the target species:** Carpentier et al. 2020 ([PMID: 32785618](https://pubmed.ncbi.nlm.nih.gov/32785618/)) report *"the in vivo activity, biochemical, spectroscopic characterization and X-ray crystal structure of MiaE from Pseudomonas putida"* and state the investigation *"demonstrates that the putative pp-2188 gene encodes a MiaE enzyme."* This is finding **F001**.
- **Mechanistic family assignment:** MiaE contains a *"nonheme dinuclear iron cluster, similar to that found in the hydroxylase component of methane monooxygenase"* (Mathevon et al. 2007, *S. typhimurium*, [PMID: 17679698](https://pubmed.ncbi.nlm.nih.gov/17679698/)) — finding **F003**.
- **GO annotations for Q88KV1:** GO:0045301 (tRNA ms2i6A37 hydroxylase activity), GO:0004497 (monooxygenase), GO:0046872 (metal ion binding), GO:0006400 (tRNA modification).

**Genomic context (F005):** PP_2188 (2,494,792–2,495,409, + strand) is a **standalone transcriptional unit**, flanked by PP_2187 (universal stress protein) and PP_2189 (unknown), both on the complementary strand. There is **no mia operon** — MiaE is not co-transcribed with MiaA or any methylthiotransferase, consistent with its being an independently acquired, lineage-restricted accessory modification enzyme.

**Curation-relevant caveat (F006):** The Carpentier 2020 in vivo activity was assayed in a **heterologous E. coli TOP10 host**, chosen precisely *because "E. coli contains the unhydroxylated ms2i6A37 in its tRNAs"* — i.e., E. coli supplies the ms2i6A substrate that KT2440 itself may not make. The empty-vector control showed *"ms2i6A37 … with no evidence for the presence of ms2io6A37,"* while *"tRNAs isolated from the complemented strain showed the presence of ms2io6A37."* **No native P. putida tRNA nucleoside analysis is reported in that paper.** The enzyme's catalytic competence is proven; the identity of its native in vivo product in KT2440 is not.

### 4.2 Contextual (non-bucket) genes assessed

| Gene | Locus / UniProt | Role | Status in KT2440 | Evidence |
|---|---|---|---|---|
| **MiaA** | PP_4895 / Q88DD2 | i6A37 synthase (EC 2.5.1.75) | Present | UniProt + KEGG EC link (F002/F004) |
| **MiaB** | — | ms2i6A37 synthase (EC 2.8.4.3, K06168) | **Absent** | 3 orthogonal lines (F002/F004/F007) |
| **RimO** | PP_1197 / Q88NL0 | uS12-Asp88 methylthiotransferase (EC 2.8.4.4) | Present (paralog, NOT MiaB) | Homology (F004) |

---

## 5. Gaps, Ambiguities, and Likely Over-Annotations

### 5.1 The MiaB substrate gap (primary finding)

Three independent, orthogonal analyses converge on the conclusion that **KT2440 lacks a canonical MiaB**:

1. **UniProt/InterPro proteome inspection (F002, F007):** The KT2440 proteome (5,529 proteins) contains **exactly one** IPR005839 (radical-SAM MiaB/RimO fold) protein and **exactly one** MiaE (PF06175). Searches by `gene:miaB`, `ec:2.8.4.3`, `protein_name:methylthiotransferase`, and InterPro IPR005839/IPR013848 return **only RimO** (Q88NL0) — no MiaB.
2. **KEGG orthology (F002):** Ortholog **K06168 (MiaB) has no member in ppu**, whereas it is present in *E. coli* (b0661), *P. aeruginosa* (PA3980), *P. fluorescens* (PFL_5432), and *P. syringae* (PSPTO_4804).
3. **Direct sequence homology (F004):** 3-mer Jaccard similarity of the sole KT2440 methylthiotransferase PP_1197 (443 aa) is **0.299 to E. coli RimO** (P0AEI4, 441 aa) but only **0.069 to E. coli MiaB** (P0AEI1, 474 aa) — unambiguously identifying PP_1197 as the RimO ortholog (uS12 Asp88, EC 2.8.4.4), not MiaB.

**Positive control (F007):** *P. aeruginosa* PAO1 (MiaB-positive; PA3980) carries **two** IPR005839 proteins (RimO + MiaB), whereas KT2440 carries only one. This clean positive/negative control demonstrates the KT2440 methylthiotransferase deficit is a genuine biological loss, not a proteome-annotation artifact.

### 5.2 Native product ambiguity

Because MiaB is absent but MiaA and MiaE are present, the native KT2440 product is most likely **io6A37**, not ms2io6A37. This is supported by MiaE's documented in vitro substrate promiscuity: *"regardless of the substrate (i6A, Cl2i6A, and ms2i6A) used in peroxide-shunt assays, hydroxylation of the terminal isopentenyl-C4-position was observed"* ([PMID: 23906247](https://pubmed.ncbi.nlm.nih.gov/23906247/)), and the corresponding products io6A, Cl2io6A, and ms2io6A were all synthesized/defined. This is findings **F002/F004**. The generic module product label "ms2io6A37" is therefore likely **wrong for this organism**.

### 5.3 Paralog / over-annotation risks

- **RimO ↔ MiaB confusion:** PP_1197 is the single greatest annotation-propagation risk in this locus. Both are radical-SAM/IPR005839 methylthiotransferases; naive homology transfer could mislabel it "MiaB." The homology data (F004) firmly assign it to RimO. Curators should ensure PP_1197 is annotated EC 2.8.4.4 (uS12 protein modification), **not** EC 2.8.4.3 (tRNA).
- **Broad EC/GO mappings on MiaE:** Q88KV1 carries the generic GO:0004497 (monooxygenase); the specific, defensible term is GO:0045301 (tRNA ms2i6A37 hydroxylase activity). If native product is io6A, a curator may wish to note that GO:0045301's substrate name (ms2i6A) does not match the likely native substrate (i6A) in this organism — a possible GO term/definition mismatch.
- **Lineage restriction (F003):** MiaE (K06169) is **absent in E. coli**, present in *P. putida*, *P. aeruginosa*, *P. fluorescens*, and *Salmonella*. Kaminska et al. 2008 note ms2i6A is hydroxylated to ms2io6A *"in a few bacteria, such as Salmonella typhimurium"* ([PMID: 17910062](https://pubmed.ncbi.nlm.nih.gov/17910062/)). Any module that assumes MiaE is broadly distributed across bacteria would be mis-scoped.

---

## 6. Module and GO-Curation Recommendations

| Module element | Recommended mark | Rationale |
|---|---|---|
| MiaE terminal hydroxylation (PP_2188) — enzyme presence | **covered** | Direct target-species experimental + structural evidence (F001, F005) |
| Native module product = ms2io6A37 | **candidate_uncertain / module_needs_revision** | MiaB absent → native product most likely io6A, not ms2io6A (F002, F004, F006) |
| Upstream MiaB substrate step | **gap / not_expected_in_target_taxon** | Three orthogonal lines confirm MiaB absence; this is a lineage-specific loss (F002, F004, F007) |
| Upstream MiaA step | present (context only) | PP_4895; not a UPA00729 bucket member |

**Concrete recommendations:**

1. **Mark the UPA00729 enzyme step COVERED.** PP_2188 satisfies the bucket with the highest evidence tier. No paralog ambiguity for MiaE itself.
2. **Flag the module product for revision.** The generic "ms2io6A37" product should carry an organism-specific note: in a MiaB-minus KT2440 background the physiological product is predicted to be **io6A37**. Consider a species-specific module variant or a `candidate_uncertain` annotation on the product node.
3. **Do NOT create a MiaB gap-fill request against PP_1197.** PP_1197 is RimO; annotating it as MiaB would be an error. If module satisfiability logic expects MiaB upstream, mark that step `not_expected_in_target_taxon` rather than forcing a candidate.
4. **Potential GO curation note:** GO:0045301 (tRNA ms2i6A37 hydroxylase activity) is correct for the enzyme's canonical/defined activity but its substrate name may not match the native KT2440 substrate. A broader or additional term capturing i6A→io6A hydroxylation may be warranted if experimental confirmation of io6A is obtained. No new GO term request is urgent absent that data.
5. **Keep RimO and the tRNA hydroxylation module strictly separate** in the module graph to prevent cross-propagation.

---

## 7. Genes to Promote to Full Review

| Gene | Promote? | Reason |
|---|---|---|
| **miaE / PP_2188 (Q88KV1)** | **Yes — confirm/close** | Already the bucket's sole member with PE1 + structures; a full `fetch-gene` review will formally close it as COVERED and attach the substrate-supply caveat. |
| **PP_1197 (Q88NL0, RimO)** | **Yes — disambiguation** | Full review needed to lock its annotation as RimO (EC 2.8.4.4) and pre-empt any MiaB mis-propagation in the module graph. |
| **PP_4895 (Q88DD2, MiaA)** | Optional | Context gene; confirms i6A37 production. Low priority — not a bucket member. |

---

## 8. Limitations and Knowledge Gaps

- **No native KT2440 tRNA nucleoside data.** The single most important gap: every ms2io6A demonstration for Pp-MiaE was performed in *heterologous E. coli* (F006). Whether KT2440 tRNA carries io6A, ms2io6A, both, or neither is **experimentally unresolved**.
- **MiaB absence is inferred from bioinformatics**, albeit by three orthogonal methods with a clean positive control. A cryptic, highly diverged methylthiotransferase cannot be formally excluded, though InterPro/KEGG/homology all agree it is unlikely.
- **Homology metric is coarse.** The RimO-vs-MiaB assignment used a 3-mer Jaccard heuristic (0.299 vs 0.069); this is decisive directionally but is not a substitute for a full phylogenetic/HMM analysis.
- **Substrate promiscuity is in vitro.** MiaE's ability to hydroxylate i6A directly ([PMID: 23906247](https://pubmed.ncbi.nlm.nih.gov/23906247/)) was shown with nucleoside surrogates in peroxide-shunt assays, not on native tRNA in KT2440.

---

## 9. Proposed Follow-up Experiments / Actions

1. **LC-MS/MS nucleoside analysis of KT2440 total tRNA** (highest priority). Directly determine whether io6A37 and/or ms2io6A37 is present. This single experiment resolves the product-identity ambiguity and the module_needs_revision flag.
2. **ΔPP_2188 knockout + LC-MS.** Confirm that the observed hydroxylated species (io6A or ms2io6A) disappears upon miaE deletion, tying the modification to PP_2188 in vivo.
3. **Bioinformatic confirmation of MiaB absence** via HMMER/pHMM search of the KT2440 proteome and re-annotation of PP_1197 as RimO with a curator note.
4. **Cross-species check within the KT2440 lineage.** Confirm whether other sequenced *P. putida* strains share the MiaB-minus/MiaE-plus configuration, to establish whether this is strain- or species-level.
5. **Expert question for module curators:** Should UPA00729's product node be organism-parameterized (io6A vs ms2io6A) rather than fixed, given MiaE's substrate promiscuity and variable upstream MiaB presence across taxa?

---

## 10. Key References

| PMID | Title (abbrev.) | Support for this review |
|---|---|---|
| [32785618](https://pubmed.ncbi.nlm.nih.gov/32785618/) | *Structural, biochemical and functional analyses of tRNA-monooxygenase MiaE from Pseudomonas putida* | **Primary target-organism evidence** that PP_2188 encodes functional MiaE (F001); also reveals the in vivo assay used heterologous *E. coli* (F006). |
| [17679698](https://pubmed.ncbi.nlm.nih.gov/17679698/) | *tRNA-modifying MiaE from Salmonella typhimurium is a nonheme diiron monooxygenase* | Defines the enzyme family/mechanism (nonheme diiron, MMO-like) underlying EC 1.14.99.69 (F003). |
| [23906247](https://pubmed.ncbi.nlm.nih.gov/23906247/) | *Peroxide-shunt substrate-specificity for the S. typhimurium MiaE* | MiaE hydroxylates i6A, Cl2i6A, and ms2i6A → io6A, Cl2io6A, ms2io6A; basis for predicting io6A as native KT2440 product (F002, F004). |
| [17910062](https://pubmed.ncbi.nlm.nih.gov/17910062/) | *Structural bioinformatics of ms2io6A37 biosynthesis enzymes* | Establishes taxonomic restriction of the ms2io6A step to "a few bacteria such as Salmonella typhimurium" (F003). |

---

### Bottom line for curators

Mark the **UPA00729 MiaE hydroxylation step COVERED** (PP_2188, direct + structural evidence). Flag the **module product for revision** because the upstream MiaB methylthiotransferase is absent in KT2440 (three orthogonal lines + positive control), making the native product most plausibly **io6A37 rather than ms2io6A37** — a conclusion resolvable only by direct LC-MS of KT2440 tRNA. Do not mis-annotate PP_1197 as MiaB; it is RimO.


## Artifacts

- [OpenScientist final report](PSEPK__trna_ms2io6a37_hydroxylation__upa00729-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__trna_ms2io6a37_hydroxylation__upa00729-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:32785618
2. PMID:23906247
3. PMID:17679698
4. PMID:17910062