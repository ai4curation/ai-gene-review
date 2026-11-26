# ARHGEF4 (Asef) notes

## Biology
- Binds the APC armadillo repeats; APC enhances its GEF activity and lamellipodia formation [PMID:10947987]. That paper originally called it Rac-specific.
- A Cdc42-specific GEF in vitro (little activity on Rac1-3, RhoA, TC10) [PMID:17214551].
- SH3-mediated autoinhibition is relieved by APC binding to the CAB motif, activating CDC42 [PMID:17704816].
- **PMID:17599059 is the Asef2 (SPATA13) paper**, yet GOA attributes three ARHGEF4 IMP rows to it (GEF activity, lamellipodium, filopodium).
  - Abstract-only, so we cannot see whether Asef was also tested.
  - The rows keep the same action as their sibling rows for each term, with the caveat in their summaries; a suggested question is recorded.
- PAINT PTHR47544:
  - The ARHGEF4 GEF IBD (PTN009210929) is seeded by ARHGEF4 itself.
  - The lamellipodium/filopodium IBDs sit on the SPATA13 node PTN002911504, not on ARHGEF4.
- Not annotated (from the affinage record; no cached paper): adenoma reduction in Asef-/-; Apc(Min) mice; angiogenesis; HGF/EGF-induced Rac1 activation.

## GOA calls
- **ACCEPT:** GEF activity (all rows; substrate CDC42); APC armadillo binding (protein domain specific binding).
- **Non-core:** lamellipodium/filopodium assembly, ruffle membrane, cytosol/cytoplasm, general signalling.
- **REMOVE:** generic protein binding with DNAJA3 and HSF2BP.
- Review round (PR #4170):
  - CC rows now quote the UniProt SubCell line (isoform 3: cytoplasm, ruffle membrane).
  - GO:0051056 rows → MODIFY to GO:0032489 regulation of Cdc42 protein signal transduction.
  - Filopodium assembly IEA → MARK_AS_OVER_ANNOTATED (filopodia data are Asef2's, and the PAINT IBD is on the SPATA13 node). The IMP row is left non-core, deferring to the curator; validation warns about the inconsistency.
  - Cdc42-vs-Rac1 substrate question recorded as an MF_DARK knowledge gap. Rac1 evidence:
    - EGF-induced Rac1 activation with Tyr94 phosphorylation [PMID:18653540].
    - HGF-Asef-IQGAP1 Rac activation [PMID:25492863].
    - Endothelial barrier [PMID:25518936].
    - Hepatic stellate cells [PMID:30871422].
