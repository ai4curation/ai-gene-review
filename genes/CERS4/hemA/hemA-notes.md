# hemA (Cereibacter sphaeroides 2.4.1) review notes

UniProtKB: Q04512 (HEM1_CERS4), locus RHOS4_15770 / RSP_2984, 407 aa. EC 2.3.1.37.
Folder genes/CERS4/hemA (UniProt mnemonic CERS4, gene name hemA).

## Deep research

No `-deep-research-*.md` exists; deep research was not available in this session (the
perplexity provider attempt for the sibling RHOCB/hemA failed: template missing, no keys). Review
built from the UniProt record and cached abstracts.

## Core biology

- ALAS isozyme 1 of R. sphaeroides; HemT is the second isozyme (53% identical).
  [PMID:8468290 "ALA synthase catalyzes the condensation of glycine and succinyl coenzyme A, the first and rate-limiting step in tetrapyrrole biosynthesis."]
- hemT is silent in wild-type 2.4.1; expressed when hemA is inactivated.
  [PMID:8468290 "Transcription of hemT was not detected in wild-type cells under the physiological growth conditions tested."]
- Single mutants grow without ALA; double mutant HemAT1 is an ALA auxotroph.
  [PMID:8468291 "whereas a mutant, HemAT1, in which hemA and hemT had both been inactivated required exogenous ALA for growth"]
- ALA feeds hemes, bacteriochlorophylls and corrinoids.
  [PMID:8468291 "leading to the biosynthesis of hemes, bacteriochlorophylls, and corrinoids"]
- Purified HemA: active, Km glycine 1.9 mM, succinyl-CoA 17 uM, PLP-dependent (aldimine).
  [PMID:10491185 "The Km values for HemA are 1.9 mM for glycine and 17 microM for succinyl-CoA"]
- HemA is more hemin-sensitive than HemT.
  [PMID:30232811 "HemT enzymes are far less sensitive to feedback inhibition by hemin than HemA enzymes"]
- UniProt cofactor, subunit and binding-site features are by similarity to R. capsulatus P18079.

## Decisions

- ALAS activity, PLP binding, tetrapyrrole biosynthetic process: ACCEPT.
- transferase activity: TOO_GENERAL.
- NEW heme biosynthetic process (IC), matching the R. capsulatus ortholog's TreeGrafter row.
