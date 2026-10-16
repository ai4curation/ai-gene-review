# puc1 (SPBC19F5.01c, UniProt P25009) — curation notes

## Identity

- Cyclin puc1, 359 aa, cyclin family (Cyclin_N PF00134, IPR014399 Cyclin_CLN, CDD cd20559
  CYCLIN_ScCLN_like, PANTHER PTHR10177). UniProt FUNCTION line: "Function in exit from the
  mitotic cycle. Contributes to negative regulation of the timing of sexual development in
  fission yeast, and functions at the transition between cycling and non-cycling cells."
- Fission yeast has a single cell-cycle CDK (Cdc2) and the G1/S cyclins Puc1, Cig1 and Cig2
  plus the essential B-type cyclin Cdc13 [PMID:30640914 "Cig1, Cig2 and Puc1 cyclins control
  G1 progression, meanwhile Cdc13 is essential to promote chromosome segregations"].

## Sources available

- Cached, abstract-only: PMID:1828291 (Forsburg & Nurse 1991, Nature), PMID:8006074
  (Forsburg & Nurse 1994, J Cell Sci), PMID:9201720 (Caligiuri et al. 1997, MBoC),
  PMID:16823372 (Matsuyama et al. 2006 ORFeome localization), PMID:8631306 (Fisher & Nurse
  1996).
- Cached, full text: PMID:29084823 (Navarro, Chakravarty & Nurse 2017, Zfs1/Puc1),
  PMID:25891897 (Gutierrez-Escribano & Nurse 2015), PMID:30640914 (Bustamante-Jaramillo et
  al. 2019).
- Deep research (falcon/Edison) `puc1-deep-research-falcon.md`, which is essentially a
  digest of Martin-Castellanos et al. 2000 (MBoC 11:543, the key mechanistic paper). That
  paper is NOT in the local publications cache and is not among the GOA references for puc1,
  so its findings are cited here through the deep-research file
  (`file:SCHPO/puc1/puc1-deep-research-falcon.md`).

## Biology (synthesis)

1. Discovery. puc1+ was cloned by complementation of S. cerevisiae cln1 cln2 cln3 (WHI1/DAF1)
   deficiency [PMID:1828291 "We have isolated a G1-type cyclin gene called puc1+ from S.
   pombe, using a functional assay in S. cerevisiae"]; in S. pombe its overexpression gave a
   cyclin-like role distinct from the mitotic B-type cyclin [PMID:1828291 "Expression of puc1+
   in S. pombe indicates that it has a cyclin-like role in the fission yeast distinct from the
   role of the B-type mitotic cyclin"].
2. 1994 characterisation. Forsburg & Nurse could not detect a mitotic G1/S function of puc1
   on its own, but found that it acts at the cycling/non-cycling transition: expression rises
   in nitrogen starvation, puc1 affects the timing of sexual development, and overexpression
   blocks sexual development and rescues pat1ts lethal meiosis [PMID:8006074 "We fail to
   identify any function of this cyclin at the mitotic G1/S transition in S. pombe, but
   demonstrate that it does function in exit from the mitotic cycle"; "Overexpression of the
   puc1 protein blocks sexual development, and rescues pat1ts cells, which would otherwise
   undergo a lethal meiosis"].
3. Redundant G1/S role (Martin-Castellanos et al. 2000, via deep research). puc1 deletion is
   silent alone but in cig1 cig2 background lengthens G1 and raises the size at S-phase entry;
   the triple mutant is ~15% larger; rum1 deletion abolishes the excess G1. Puc1-Cdc2
   immunocomplexes phosphorylate Rum1 T58/T62 and are resistant to Rum1 inhibition, whereas
   Cdc13-Cdc2 and Cig2-Cdc2 are inhibited [file:SCHPO/puc1/puc1-deep-research-falcon.md "Puc1
   and Cdc2 immunocomplexes phosphorylated Rum1 in vitro at Thr58 and Thr62"; "At 10 nM Rum1,
   Cdc2–Cdc13 activity was inhibited and Cdc2–Cig2 activity was almost completely inhibited,
   whereas Puc1-associated activity was not significantly inhibited"]. Puc1 does not drive S
   phase in the absence of cig1, cig2 and cdc13 [PMID:8631306 "Further deletion of cig1 and
   puc1 had no effect, but deletion of cig2/cyc17 caused a severe delay in re-replication"].
   This is the Cln3-like "gate-opening" role: relief of Rum1 inhibition so that the B-type
   cyclin-Cdc2 complexes can fire.
4. Start machinery. Puc1 associates in vivo with the Ran1/Pat1 kinase and the MBF subunit
   Cdc10; Ran1 controls the Puc1-Cdc10 association [PMID:9201720 "We demonstrate that the
   Puc1 cyclin associates with Ran1 and Cdc10 in vivo and that the Ran1 protein kinase
   functions to control the association between Puc1 and Cdc10"]. This ties the G1 cyclin to
   both the MBF transcription complex and the meiosis-repressing Pat1 kinase.
5. Sexual differentiation. Zfs1 (CCCH tandem zinc finger RBP) binds puc1+ mRNA and lowers
   Puc1 levels; in zfs1Δ Puc1 is elevated and mating drops five-fold, and puc1Δ (but not cig1Δ
   or cig2Δ to the same extent) restores mating; Puc1 has a dose-dependent inhibitory effect on
   mating and delays G1 arrest on nitrogen removal [PMID:29084823 "This experiment showed that
   Puc1 has a dose-dependent inhibitory effect over sexual differentiation, with increasing
   levels of Puc1 reducing mating efficiency to the levels observed in the zfs1Δ mutant";
   "Neither cig1+ nor cig2+ gene deletion suppressed the mating defect of the zfs1Δ mutant as
   efficiently as puc1+ gene deletion, indicating a specific role of Puc1 cyclin in the
   phenotype of the zfs1Δ mutant"]. The proposed mechanism is Puc1-Cdc2 phosphorylation of
   Rum1 (and possibly extended inhibitory phosphorylation of Ste11) [PMID:29084823 "This might
   be due to the ability of the Puc1–Cdc2 complex to phosphorylate and probably inactivate the
   CDK inhibitor Rum1 (Martin-Castellanos et al., 2000). Rum1, in contrast, cannot inactivate
   the Puc1–Cdc2 complex, and therefore, small changes in cyclin levels can result in dramatic
   changes in activity"].
6. Meiosis. No specific meiotic role; cig1 cig2 puc1 triple mutants mate and sporulate
   [PMID:25891897 "the Puc1 cyclin has been shown to have a role during sexual
   differentiation29 but no significant roles have been identified in meiotic cell cycle
   progression"]; puc1 expression is nearly undetectable in meiotic prophase [PMID:30640914 "In
   the case of puc1, expression is almost undetectable during meiotic prophase, where it is
   even less abundant than in vegetative cells"].
7. Localization. Only high-throughput data: the ORFeome YFP screen (PomBase HDA rows: nucleus
   and cytosol) [PMID:16823372 "we determined the localization of 4,431 proteins, corresponding
   to approximately 90% of the fission yeast proteome, by tagging each ORF with the yellow
   fluorescent protein"]. No targeted localization study exists; the deep research explicitly
   flags localization as unresolved.

## Curation decisions (rationale summary)

- GO:0016538 (regulator activity; IBA/IEA/IGI): MODIFY to GO:0061575 activator activity. The
  IBD node PTN000019791 contains only activating cyclins (cyclin D/E/A/B, Cln3, Clb5, cdc13,
  cig1, cig2, puc1); Puc1 confers Rum1-resistant Cdc2 kinase activity (deep research) and
  complements CLN loss in budding yeast (PMID:1828291). Same treatment as the yeast CLN3
  review.
- GO:2000045 IGI (PMID:1828291): MODIFY to GO:1900087 - the complementation of G1-arrested
  cln cells is a positive effect on G1/S; the sign is known. InterPro IEA GO:2000045 accepted
  as a correct family-level mapping.
- GO:0051726 IEA (ARBA): MODIFY to GO:1900087; "regulation of cell cycle" is uninformative.
- GO:0044843 IMP (PMID:8006074): ACCEPT, deferring to the PomBase curator who read the full
  text (the abstract records a negative result for the mitotic G1/S transition but the paper
  documents the puc1 contribution to staying in the cycle vs. exiting; Martin-Castellanos
  2000 later established the G1/S role). ARBA IEA GO:0044843 accepted as generic-but-correct.
- GO:1900087 EXP (PMID:9201720): ACCEPT.
- GO:0110045 IGI with zfs1 (PMID:29084823): ACCEPT as a core, Puc1-specific function.
- GO:0023052 signaling NAS (keyword mapping): MARK_AS_OVER_ANNOTATED - a cyclin is not a
  signaling component; the informative process terms already exist.
- Nucleus HDA/IBA: ACCEPT. Cytosol HDA and cytoplasm IBA: KEEP_AS_NON_CORE (documented pool,
  but the substrates Rum1, Cdc10/MBF, Ste11 are nuclear).
- No NEW terms proposed. Candidate "regulation of conjugation with cellular fusion"
  (GO:0031137) was considered but PomBase already expresses the same biology with GO:0110045
  and other pombe differentiation regulators use that term; adding a sibling would be
  redundant.

## Open items

- Martin-Castellanos et al. 2000 (the key mechanistic paper) does not appear among the GOA
  references for puc1; its Rum1-phosphorylation and cell-size data would support IDA/IGI
  annotations (e.g. GO:0000082 with cig1/cig2, and a Cdc2 has-input Rum1 relationship in a
  GO-CAM). Raised in suggested_questions.
- Direct localization of endogenous Puc1 through the cycle and during nitrogen starvation is
  unknown.
