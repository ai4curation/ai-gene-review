# Notes for DANRE slc5a12

## 2026-05-09 review notes

- Core function is apical sodium-coupled monocarboxylate transport [PMID:17255103 "Zebrafish Slc5a12 encodes an electroneutral sodium monocarboxylate transporter"].
- The review narrows generic organic-acid/transmembrane-transporter annotations to monocarboxylate:sodium symporter activity because lactate, pyruvate, nicotinate, propionate, and butyrate transport are directly described [file:DANRE/slc5a12/slc5a12-uniprot.txt "monocarboxylates such as lactate, pyruvate, nicotinate, propionate, butyrate"].
- The location is apical plasma membrane rather than generic membrane [file:DANRE/slc5a12/slc5a12-uniprot.txt "SUBCELLULAR LOCATION: Apical cell membrane"].

## Re-review 2026-09-29

Re-reviewed all 14 GOA rows against UniProt Q7T384 and the cached primary paper (PMID:17255103,
Plata et al. 2007, abstract-only but the abstract reports the full oocyte transport assay).
Replaced the templated one-line reasons and the FUNCTION-line-everywhere supporting_text; removed
one stale yaml row (GO:0022857 IEA GO_REF:0000120, not in GOA).

- Verified every MODIFY replacement term id via QuickGO REST (all current, non-obsolete, labels
  correct, and each a descendant of the term being modified except GO:0015718 which is on the
  substrate rather than transmembrane axis):
  - [0] GO:0005343 organic acid:sodium symporter IBA -> GO:0140161 monocarboxylate:sodium symporter
    (child; +propagation_review TERM_SCOPING_PROBLEM/GRANULARITY_MISMATCH).
  - [2] GO:0006814 sodium ion transport IBA -> GO:0035725 sodium ion transmembrane transport
    (child; +propagation_review).
  - [3] GO:0016020 membrane IEA -> GO:0016324 apical plasma membrane (child).
  - [7] GO:0055085 transmembrane transport IEA -> GO:1905039 carboxylic acid transmembrane transport
    (+ GO:0015718 monocarboxylic acid transport).
  - [13] GO:0022857 transmembrane transporter activity IEA (was PENDING) -> GO:0140161.
- Core: GO:0140161 (IDA), GO:0015355 (IDA) ACCEPT as the direct zebrafish activities
  [PMID:17255103 "Both zSMCTs oocytes increased [Na(+)](i) with addition of monocarboxylates (MC)
  such as lactate, pyruvate, nicotinate, and butyrate."; electroneutral: "we found no significant
  MC-elicited current in either zSMCTn or control oocytes."]; GO:0015718 (IDA) ACCEPT.
- Localization: apical plasma membrane (IEA, ISS) ACCEPT [PMID:17255103 "Within the kidney, zSMCTn
  mRNA is expressed in pronephric tubules"]; plasma membrane IBA ACCEPT. GO:0035725 and GO:1905039
  IEA ACCEPT as accurate coupled-ion / substrate-class transport processes.
- Description rewritten (electroneutral vs electrogenic paralog distinction, substrate range,
  expression); core_functions updated.
- Validation: zero errors, zero warnings.
