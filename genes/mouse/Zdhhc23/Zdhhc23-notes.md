# Zdhhc23 (mouse, Q5Y5T3) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

No ProtNLM2 output was consulted.

### Deep research
`just deep-research-falcon mouse Zdhhc23 --fallback perplexity-lite` failed: falcon returned
`403 Forbidden` at Edison auth, and the perplexity-lite fallback timed out (600 s). No
deep-research file exists; the review is built from cached full-text literature and UniProt.

### Evolutionary grounding
- PANTHER PTHR22883:SF475 (PALMITOYLTRANSFERASE ZDHHC23) contains mouse Q5Y5T3, human Q8IYP9,
  rat Q76IC6 and zebrafish zdhhc23a/b (interpro/panther/PTHR22883/PTHR22883-entries.csv), so
  human-to-mouse transfers are within the 1:1 ortholog clade.
- The GO:0072659 IBA comes from the ZDHHC23-specific node PTN008583751 (donors human ZDHHC23 and
  mouse Zdhhc23). Other IBAs (MF, Golgi, ER, protein targeting to membrane) come from the deep
  DHHC node PTN000525256.
- DHHC motif at residues 276-279; C279 is the S-palmitoyl cysteine intermediate
  (UniProt ACT_SITE, PROSITE-ProRule PRU00067).

### Mouse experimental evidence (what is established in this species)
- Zdhhc23-/- (Zdhhc23tm1(KOMP)Vlcg) aortic VSMCs: ~60% reduction in endogenous BK alpha-subunit
  S-acylation by acyl-RAC; ~40% reduction in sustained outward (BK) current; no change in
  alpha-subunit surface expression [PMID:31213527 "Acyl-RAC performed on VSMCs from Zdhhc23−/− mice displayed a significant (∼60%) reduction in BK channel α-subunit S-acylation (Fig. 5A)."]
  [PMID:31213527 "Genetic deletion of Zdhhc23 or pharmacological inhibition of S-acylation reduced BK channel currents without affecting cell surface expression of BK channel α-subunits."]
- Endogenous protein is perinuclear in VSMCs; the authors only say this is consistent with Golgi
  and ER localization reported elsewhere [PMID:31213527].
- Knockdown in mouse astrocyte line MA-C lowers GFAP palmitoylation [PMID:38050183 "ZDHHC23 expression knockdown significantly downregulated GFAP palmitoyl modification levels."]. Single study.

### Evidence from orthologs / other cells
- PMID:22399288: siRNA screen in HEK293 (human) cells identified zDHHC22/23 as the BK S0-S1 loop
  acyltransferases; overexpressed zDHHC23 localizes to Golgi (GM130) and TGN. MGI attached the IMP
  rows to the mouse gene; I defer to the curator.
- Rat NIDD (Q76IC6) binds nNOS (UniProt by similarity); not tested in mouse, not annotated.

### Decisions
- MF GO:0019706: ACCEPT all rows; GO:0016409 MODIFY to GO:0019706.
- GO:0018345 protein palmitoylation: ACCEPT (enzyme performs the step; mouse KO evidence).
- GO:0072659 protein localization to plasma membrane: KEEP_AS_NON_CORE for all rows. In the only
  native mouse tissue tested (beta1-containing VSMCs) deletion did not change surface expression;
  the trafficking effect is beta1-context dependent. This differs from the human review, which
  ACCEPTs it as core; the mouse native-tissue data are the reason.
- GO:0006612 KEEP_AS_NON_CORE; Golgi apparatus MODIFY -> Golgi membrane; ER IBA
  MARK_AS_OVER_ANNOTATED (ER donors are paralogs outside SF475), consistent with human review.
- No NEW annotations: BK current reduction and pain phenotypes are downstream of the substrate,
  not processes Zdhhc23 performs.
