# FAE1 / KCS18 (3-ketoacyl-CoA synthase 18) — Arabidopsis thaliana — review notes

UniProt: Q38860 · At4g34520 · EC 2.3.1.199 · Taxon 3702
Relevance: canonical seed VLCFA condensing enzyme; key DOE/BER oilseed domestication
target (erucic/VLCFA content in pennycress and Brassica feedstocks).

## Core function
- **3-ketoacyl-CoA synthase (KCS)**, the condensing enzyme of the ER fatty acid elongase
  (FAE) complex. Catalyzes the first, rate-defining step of each elongation cycle:
  condensation of an acyl-CoA with malonyl-CoA to a 3-ketoacyl-CoA, adding two carbons.
  The KCS is the **chain-length-determining** subunit of the 4-enzyme FAE system.
  [file:ARATH/FAE1/FAE1-deep-research-falcon.md; PMID:11341960; PMID:12135493]
- **Seed-specialized**: active on saturated and monounsaturated C16/C18 acyl-CoAs;
  elongates C18->C20->C22 (and up to C26); produces seed VLCFAs (C20:1, C22:1 etc.).
  No activity on polyunsaturated C18:2/C18:3. [UniProt Q38860 FUNCTION; PMID:12135493]
- **Loss of function**: fae1 seeds drop from ~28% VLCFA (WT) to <1%; vegetative tissues
  largely unaffected — establishing FAE1 as the principal seed condensing enzyme.
  [PMID:7734965; file:ARATH/FAE1/FAE1-deep-research-falcon.md]

## Localization
- **Endoplasmic reticulum / microsome membrane** (integral membrane). Experimentally
  shown (IDA PMID:36798704; microsome PMID:12135493); ER is the site of VLCFA elongation.
- The GOA **chloroplast (ISM, GO_REF:0000122)** annotation contradicts this experimental
  ER localization and is a spurious sequence-model prediction -> REMOVE.

## Annotation review decisions
- GO:0009922 fatty acid elongase activity (EXP/IDA + IEA) -> ACCEPT (core MF)
- GO:0000038 very long-chain fatty acid metabolic process (IMP) -> ACCEPT (core BP)
- GO:0030497 fatty acid elongation (IMP) -> ACCEPT (core BP)
- GO:0006633 fatty acid biosynthetic process (IEA) -> ACCEPT (general but correct)
- GO:0005783 endoplasmic reticulum (IDA + IEA) -> ACCEPT (core location)
- GO:0016020 membrane (IEA) -> ACCEPT (integral ER membrane)
- GO:0016746 / GO:0016747 acyltransferase activity (IEA) -> ACCEPT (correct but general;
  fatty acid elongase activity is the informative term)
- GO:0009507 chloroplast (ISM) -> REMOVE (contradicted by experimental ER localization)

## DOE/BER relevance
FAE1/KCS18 controls seed VLCFA (erucic acid) content — a primary domestication lever for
oilseed feedstocks. fae1 knockouts remove erucic acid to yield food/feed-grade oil; the
enzyme is also a key engineering control point for long-chain monounsaturated oils.
