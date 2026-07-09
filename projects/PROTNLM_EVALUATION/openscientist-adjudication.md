---
title: ProtNLM2 — OpenScientist adjudication of borderline and disputed predictions
---
# OpenScientist adjudication of borderline and disputed ProtNLM2 predictions

[← back to ProtNLM2 Evaluation](../PROTNLM_EVALUATION.md)

## Bottom line

Every ProtNLM2 prediction the ARGO-ProtNLM-50 review had scored **`UNC`** (genuinely
on the fence — "cannot validate or refute from the evidence at hand") was re-tested as an
**independent, blinded gene-function hypothesis** by an OpenScientist agent (structure +
comparative genomics; the suspected answer was withheld from the prompt). 15 `UNC` terms
across 11 genes; 10 genes adjudicated (14 terms), 1 gene failed upstream.

The result splits cleanly by prediction *type*:

- **Localization calls held up — 3/3 correct**, and one (ARTAN) caught a **mis-localized
  *curated* annotation**. But they systematically *undersell* a specific protein identity
  (Exportin-5, ESRP1 flattened to a generic "cytoplasm"/"nucleus").
- **Specific function / family-process refinements over-reached — 9/14 → `NPI`** (wrong
  subfamily, over-specific substrate, or untransferable ortholog-derived developmental roles).
- **2/14 were genuinely undecidable from sequence** and were kept as `UNC` leads.

This mirrors and sharpens the main evaluation's finding that ProtNLM2 "captures broad
functional categories but lacks resolution": where it names a *compartment* it is usually
right; where it names a *specific mechanism or process* it tends to over-generalize from
family/ortholog associations.

A **second round** then tested the opposite population — the 10 genes whose predictions the
review had **disputed** (`NPI`/`PLI`, "the prediction is wrong") — as the same blinded
hypotheses, to check our own rejections. **9 of 10 were independently confirmed as
misassignments; 1 (GADMO/tbc1d14) was partially overturned** (see the dispute-confirmation
section). Together the two rounds show the adjudicator moves in both directions: it upholds
well-reasoned rejections and catches an over-harsh one.

## Round 1 — borderline (UNC) verdicts

| Gene | UNC prediction(s) | Verdict | New assessment | Why |
|------|-------------------|---------|----------------|-----|
| ARTAN/A0A2U1PS28 | chloroplast (GO:0009507) | **Supported** | `UNC → COR` | ~78% id to Arabidopsis *chloroplastic* paralog Q9FNM5 vs ~47% to the mitochondrial one, + chloroplast transit-peptide signature. **The GOA/HAMAP mitochondrial annotation is the error.** |
| DROVI/B4MAQ2 | cytoplasm (GO:0005737) | **Supported (incomplete)** | `UNC → COR` | It is **Exportin-5**; cytoplasm is valid (obligatory cytoplasmic phase) but undersells a Ran-GTP nucleocytoplasmic shuttle. |
| CALMI/A0A4W3GVU1 | nucleus (GO:0005634) | **Supported** | `UNC → COR` | It is **ESRP1** (paralog ESRP2 ruled out); human ortholog is IDA-nuclear. |
| STRCO/Q9L243 | deoxyribonucleotide catabolism (GO:0009264) | **Over-annotated** | `UNC → NPI` | A generic HAD phosphohydrolase (PF18143 RNA-repair family), not a dNMP-specific 5′-nucleotidase; the process term has no pathway support. |
| AQUCT/A0A2G9RZF1 | single fertilization (GO:0007338) | **Refuted** | `UNC → NPI` | A 156-aa **CUB-domain-only** protein with no serine-protease domain or catalytic triad; real ovochymases are large multidomain S1 proteases. Family over-annotation. |
| ORYSI/B8BAB0 | pollen maturation (GO:0010152) | **Refuted** | `UNC → NPI` | Belongs to the **PG1β-like cell-wall/pectin BURP clade**, not the anther-specific RAFTIN clade that supplies the reproductive precedent. Wrong-subfamily over-generalization. |
| WHEAT/A0A3B6RKV1 | photomorphogenesis, GA signaling, red light, seed germination (GO:0010099/0010476/0010114/0010030) | **Split** | `UNC → NPI ×4` | A catalytically competent JMJ22 co-ortholog (correcting the "KDM5/JARID" mislabel — it is a **JMJD6-type histone *arginine* demethylase**), but the four terms are Arabidopsis IMP redundant-pair phenotypes not transferable to wheat by orthology alone. |
| PHATC/B7FXQ8 | salt stress, H₂O₂ (GO:0009651, GO:0042542) | **Over-annotated** | `UNC → NPI ×2` | A bona fide small-HSP/ACD chaperone whose only defensible family process is `response to heat`; salt is weakly plausible only by cross-kingdom analogy and H₂O₂ is partly *contradicted* by sHSP precedent. |
| ORYSJ/Q6YYC5 | K63-linked ubiquitination (GO:0070534) | **Undecidable** | kept `UNC` (lead) | A real RGLG-family RING E3 ligase, but chain-linkage specificity is E2-determined and not decidable from sequence/orthology — needs an in-vitro chain-linkage assay. |
| SOYBN/C6T1A2 | neg. reg. ABA signaling (GO:0009788) | **Undecidable** | kept `UNC` (lead) | A real Q-type (QALGGH) C2H2 zinc-finger TF (MF scaffold solid), but the specific ABA-negative-regulation role is overexpression-only and should not be a direct annotation. |
| ABRPR/A0A8B8L1Z3 | endoplasmic reticulum (GO:0005783) | **—** | unchanged | Run failed 4× with a transient upstream error (`Request ID: …`); gene-specific, not attempted further. |

## Round 2 — dispute confirmation (NPI / PLI)

The 10 genes whose predictions the review had **disputed** were re-tested the same way
(neutral hypothesis: "is this prediction supported or a misassignment?"). This checks whether
our own rejections hold up — and, as ARTAN showed in round 1, an independent agent can overturn
a call.

| Gene | Disputed prediction (our call) | OpenScientist finding | Outcome |
|------|-------------------------------|-----------------------|---------|
| ARATH/F4JLB7 (RIC7) | kinase activity + phosphorylation (`PLI`) | no kinase catalytic domain (LRR-RLP; no VAIK/HRD/DFG) | confirmed |
| MYTGA/A0A8B6GS20 | PI3P phosphatase (`NPI`) | catalytically dead pseudophosphatase (MTMR9-like) | confirmed |
| ASPOR/Q2U1U6 | O-glycosyl hydrolase (`NPI`) | polysaccharide lyase, not GH (and too small for either) | confirmed |
| WHEAT/F6LAX4 | 6 animal/mitotic terms (`NPI×6`) | PP2A A scaffold; terms taxon-inappropriate or B56-subunit (not A) | confirmed |
| CAEEL/mcm-4 (A0A061AL94) | transcription initiation (`NPI`) | 74-aa MCM4 replicative-helicase fragment | confirmed |
| XENTR/A0A8J0SCI2 | DNA-binding TF activator (`NPI`) | naked C2H2 array, no effector domain → direction not sequence-determinable | confirmed |
| DANRE/dnajc6 (A0A8M9QG43) | dephosphorylation (`NPI`) | PTEN-fold pseudophosphatase, no intact catalytic site | confirmed |
| DROPS/A0A6I8W8A2 | ligase activity (`NPI`) | 169-aa RCC1 β-propeller, no HECT/RING (HERC3 name-transfer) | confirmed |
| XENNA/D3VIU4 | ligand-gated ion channel (`NPI`) | periplasmic SBP; iGluR fold homology but no TM pore | confirmed |
| **GADMO/tbc1d14 (A0A8C5FPT8)** | **autophagosome (`NPI`)** | **defensible — human ortholog has a curated IDA** | **overturned → `CNN`** |

**9 confirmed, 1 overturned.** The overturn is the informative case: our review flatly rejected
autophagosome for tbc1d14, but human TBC1D14 (Q9P2M4) carries a **direct experimental IDA
autophagosome annotation** (Longatti et al. 2012, PMID:22613832) plus a phylogenetic IBA
(verified independently via QuickGO). The prediction is correct-by-orthology, so it was
reassessed `NPI → CNN` — with the caveat, on which both analyses agree, that autophagosome is a
*secondary, condition-dependent* localization (the recycling endosome is primary and the role is
regulatory). The other nine confirmations recapitulate the main evaluation's failure modes:
paralog/pseudoenzyme over-annotation, cross-kingdom / taxon-inappropriate transfer, over-specific
directional child terms, and RefSeq-name-transfer artifacts.

## Curation leads beyond the predictions

Three findings warrant fixes to the genes' own reviews, independent of the ProtNLM assessment:

- **ARTAN/A0A2U1PS28** — the existing GOA/UniRule **mitochondrial** localization (GO:0005743,
  GO:0005759 via HAMAP-Rule MF_03137) is very likely wrong; the protein is a chloroplastic
  cpLEPA/EF4. Candidate for correction in `A0A2U1PS28-ai-review.yaml`.
- **WHEAT/A0A3B6RKV1** — the review text repeatedly labels the enzyme "KDM5/JARID1"
  (H3K4 *lysine* demethylase); it is actually a **JMJD6-type histone *arginine* demethylase**
  (F-box + Cupin_8/JmjC), which changes the H3K4-directionality reasoning.
- **ARATH/F4JLB7** — a gene-symbol collision: F4JLB7 is labelled "RIC7" but appears to be an
  LRR receptor-like protein, whereas the characterized CRIB-motif RIC7 (ROP2 effector) is the
  adjacent locus At4g28556 (Q1G3K8). Worth disentangling in the gene review.

## Method & provenance

Each hypothesis was run with `just gene-hypothesis-research openscientist <ORG> <GENE>`
(3 iterations, 7200 s job timeout), framed neutrally as `computational_prediction`, with the
suspected answer withheld. No local `*-bioinformatics/RESULTS.md` was fed to the agent (there
was none for these genes). Full reports and provenance artifacts live under each gene's
`genes/<ORG>/<GENE>/<GENE>-hypotheses/<slug>/openscientist.md`. Verdicts are wired into the
per-gene `*-protnlm-predictions-review.yaml` files with verbatim `supporting_text` quotes.

Caveat: all verdicts rest on **computational** evidence (sequence, structure, orthology,
comparative genomics) without new wet-lab data; the two `COR` localization upgrades and the
ARTAN curation lead are strong but should be curator-confirmed.
