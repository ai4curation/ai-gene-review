# MYB51 (HIG1, At1g18570, UniProt O49782) — review notes

## Identity

- R2R3-MYB transcription factor, 352 aa; two HTH myb-type repeats (10-62, 63-117; UniProt
  PROSITE-ProRule PRU00625), C-terminal disordered/low-complexity region. PANTHER
  PTHR10641:SF1309 (TRANSCRIPTION FACTOR MYB51). Subgroup 12 R2R3-MYB with MYB34/ATR1 and
  MYB122/HIG2 (indolic glucosinolate, IG, regulators) and MYB28/29/76 (aliphatic GSL regulators).
- UniProt FUNCTION: "Transcription factor positively regulating indolic glucosinolate
  biosynthetic pathway genes" (PubMed:17461791, 23580754, 23943862). Nucleus (ECO:0000269
  PubMed:17461791). Can form complexes with MYC2, MYC3 or MYC4.

## Core biology (with provenance)

- Activation tagging identified HIG1/MYB51 as an activator of IG biosynthesis
  [PMID:17461791 "HIG1/MYB51 was shown to activate promoters of indolic glucosinolate
  biosynthetic genes leading to increased accumulation of indolic glucosinolates."];
  loss of function lowers GSLs [PMID:17461791 "The corresponding loss-of-function mutant
  hig1-1 contained low levels of glucosinolates."]. Overexpression specifically raises IGs
  without auxin effects (unlike MYB34/MYB122) [PMID:17461791 "overexpression of HIG1/MYB51
  resulted in the specific accumulation of indolic glucosinolates without affecting auxin
  metabolism and plant morphology."]. Touch/wounding induce MYB51; overexpression reduces
  S. exigua herbivory (same paper). Abstract-only cache.
- Division of labour among the three IG MYBs [PMID:24431192 "MYB51 regulating biosynthesis in
  shoots, and MYB122 having an accessory role"; "MYB51 is the central regulator of IG synthesis
  upon SA and ET signaling"; triple mutant "devoid of IGs"]. Abstract-only cache.
- Partners: bHLH05 (and bHLH04, bHLH06/MYC2) interact with MYB51; bHLH04/05/06 required for
  MYB51 to drive IG production [PMID:25049362 "we identified basic helix-loop-helix
  transcription factor05 (bHLH05) as an interacting partner of MYB51"; "The MYBs could induce
  the transcription of all tested promoters of GSL biosynthetic pathway in trans, indicating a
  direct role of MYB51 in the binding and activation of GSL biosynthesis genes."].
  MYC2/3/4 interact directly with GS-related MYBs [PMID:23943862].
- Downstream of ethylene in MAMP (flg22) responses; required for flg22-induced callose via
  4-methoxy-I3G [PMID:19095898 "two transcription factor mutants myb51-1 and myb51-2, were
  impaired in the Flg22-induced callose response"; "MYB51 up-regulates IGS biosynthesis in
  response to Flg22"; "MYB51 functions downstream of Et signaling"]. MYB51 also drives
  ASA1 (Trp biosynthesis) induction in this setting. Note CYP81F2 induction is MYB51-independent.
- Camalexin: myb51-containing double/triple mutants have low camalexin; acts upstream of IAOx;
  MYBs do not trans-activate CYP71B15/PAD3 promoter [PMID:26379682]. But Frerigmann 2016
  [PMID:26802248 "gene induction and accumulation of ICAs and camalexin upon pathogen infection
  was not compromised in myb34/51/122 plants"] — so camalexin role is context-dependent;
  not proposed as a GO annotation.
- Defense: myb34/51/122 triple susceptible to Plectosphaerella cucumerina, similar to pen2
  [PMID:26802248]. Single-gene contribution not resolved, so no NEW defense-to-fungus term.
- Rhizobacterium Pf.SS101-induced resistance against Pst requires MYB51 [PMID:23073694]; that
  response is SA-dependent (abstract), which conflicts with the GO:0009682 definition ("does not
  depend upon salicylic acid signaling").
- Trichomes produce GSLs; MYB51 promoter induced in trichomes on wounding [PMID:23115560].
- Sulfur deficiency: SLIM1 represses ProMYB51 in vitro; MYB51 transcript rises on prolonged -S
  [PMID:25426131]. MYB51/MYB34 regulate PGDH1/PSAT1 (phosphoserine pathway) [PMID:24368794].

## Project context: Tang et al. 2023 (PMID:37741284, abstract-only cache; full text read from PDF)

- scRNA-seq of C. higginsianum-infected leaves. At infection sites "only MYB51 and MYB122
  exhibited induction" among the three GSL MYBs; "MYB122 was only induced in the epidermis while
  MYB51 was only induced in the vasculature cells" (full text, not in cache). MYB51 also used as
  an immunity marker (with FRK1, PR1). This is EXPRESSION only; the paper functionally tested
  MYB122, not MYB51. No annotations proposed from it.

## Annotation decisions (summary)

- MF: GO:0003700 ISS ACCEPT; GO:0000976 IPI x2 (Y1H network screens) ACCEPT; NEW GO:0001228
  (activator) from trans-activation evidence.
- CC: nucleus x2 ACCEPT.
- BP: regulation of DNA-templated transcription ACCEPT; indole glucosinolate biosynthetic
  process -> MODIFY to GO:0010439 regulation of glucosinolate biosynthetic process (TF does not
  catalyse; no positive/indole-specific regulation term exists in GO). Defense/callose/response
  terms KEEP_AS_NON_CORE (indirect, via IG supply); ISR MARK_AS_OVER_ANNOTATED (definition
  excludes SA-dependent responses, and Pf.SS101 ISR is SA-dependent).

## Deep research status

- `just deep-research-falcon ARATH MYB51 --fallback perplexity-lite` was run (2026-10-02):
  falcon timed out after 600 s and the perplexity-lite fallback failed ("Provider 'perplexity'
  not available. Available: falcon, asta, openscientist"). No deep-research file exists; the
  review is based on the cached primary literature listed above (PubMed-verified PMIDs),
  UniProt O49782, and the Tang et al. 2023 full text supplied by the user.

## Update: late falcon deep research (2026-10-02)

The falcon job reported as timed out above kept running server-side and later wrote
`MYB51-deep-research-falcon.md`. The review was completed before it arrived and does not
rely on it; it is kept as a provenance record and a source of leads for future re-review.
