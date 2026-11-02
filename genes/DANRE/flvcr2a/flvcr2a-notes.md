# flvcr2a review notes

- Curated in DANRE batch 04. Flvcr2a should no longer be reviewed as primarily a heme transporter: the current UniProt entry and 2024 paper support MFSD7c as a choline transporter at the BBB [PMID:38302740 "MFSD7c is a choline transporter at the blood-brain barrier"]. I retained ethanolamine/heme transport as non-core inferred capabilities.
- Follow-up: changed generic membrane CC from cross-aspect MODIFY to REMOVE; specific membrane locations remain reviewed separately.

## Re-review 2026-09-28

Rewrote every `review` block against primary literature. Previously the file rested on
49 quotes from the UniProt flat file (the same FUNCTION line pasted under localization
and heme terms) plus deep-research paraphrases; it now cites four cached papers, with
UniProt lines used only where they are the right line (SUBCELLULAR LOCATION for the
ER/mitochondrion rows, CATALYTIC ACTIVITY for the reaction rows).

Newly cached and used: PMID:38778100 (cryo-EM/transport of human FLVCR1/FLVCR2),
PMID:20823265 (the 2010 FLVCR2 heme-import report), PMID:32369449 (Mfsd7c-KO
vasculopathy, abstract-only cache).

Key evidence now anchored in the review:

- The zebrafish protein itself was assayed, not just inferred: [PMID:38302740 "We tested
  the choline import function for several MFSD7c orthologs including the ones from
  zebrafish (DaMfsd7c_a and DaMfsd7c_b isoforms), medaka fish (MeMfsd7c), and frog
  (XeMfsd7c). Consistently, these MFSD7c orthologs also exhibited choline transport
  activity"]. This is the support for the IDA row on GO:0015220 and for the core function.
- Mechanism: [PMID:38302740 "Replacement of sodium with lithium did not affect choline
  import by MFSD7c"], [PMID:38302740 "These results show that the import of choline by
  MFSD7c is electrogenic."], and [PMID:38778100 "Our findings suggest that both FLVCR1
  and FLVCR2 operate as uniporters, facilitating downhill ligand transport independent of
  sodium or pH gradients."].
- In vivo barrier flux for the donor of the GO:0150104 ISS row: [PMID:38302740 "There was
  a significant reduction of radioactive signals in the brain of EcMfsd7c-KO mice compared
  to controls."] with [PMID:32369449 "We identified the mouse ortholog Mfsd7c as a gene
  expressed in the blood-brain barrier."]. The gene product performs the barrier-crossing
  step itself, so the participation test is met; the zebrafish in vivo test has not been
  done, which is flagged with [file:DANRE/flvcr2a/flvcr2a-deep-research-falcon.md "there
  is **no direct in vivo zebrafish mutant phenotype, tissue expression map, or subcellular
  localization imaging** for flvcr2a"].

Action changes:

- GO:0097037 heme export (IBA): KEEP_AS_NON_CORE -> REMOVE. The WITH/FROM is the ancestral
  node plus human FLVCR1 alone, i.e. only the exporting paralog, and the FLVCR2 literature
  states the opposite direction: [PMID:20823265 "a report by Quigley and colleagues ( 37 )
  clearly shows that FLVCR2 does not export heme."]. Added `propagation_review`
  (PROPAGATION_BAD; WRONG_ORTHOLOG_OR_PARALOG, FUNCTIONAL_DIVERGENCE) with both sources
  marked SUPPORTS_SOURCE_BUT_NOT_TARGET. Donor identities were checked rather than assumed:
  MGI:2444881 = mouse Flvcr1, MGI:2384974 = mouse Flvcr2, Q9Y5Y0 = human FLVCR1,
  Q9UPI3 = human FLVCR2, Q91X85 = mouse Flvcr2, Q96SL1/Q6GNV7 = SLC49A4/DIRC2 orthologs.
- GO:0016020 membrane (IBA): REMOVE -> MODIFY to GO:0005886 plasma membrane. The node
  PTN000858822 also contains lysosomal SLC49A4/DIRC2 members, so the generic parent is the
  safe node-level call, but the site of action for this gene is resolved
  [PMID:38778100 "Confocal imaging shows that FLVCR1 and FLVCR2 are localized at the plasma
  membrane"]. A same-aspect MODIFY avoids discarding a true localization.
- GO:0005886 plasma membrane, is_active_in ISS: PENDING -> ACCEPT (the last GOA row added on
  refresh). Distinguished in `reason` from the located_in row: the is_active_in form is the
  more accurate claim, since translocation is measured across the plasma membrane in both
  directions [PMID:38778100 "indicating a bidirectional choline transport activity mediated
  by FLVCR2"].
- Heme rows retained as non-core (GO:0015232, GO:0020037) but re-argued from the actual
  assays: [PMID:20823265 "FLVCR2 binds to hemin-conjugated agarose, and binding is competed
  by free hemin"] against [PMID:38302740 "heme and bilirubin levels in fetal brains were
  comparable between Mfsd7c–/– and WT embryos"] and [PMID:38302740 "However, this
  observation has not been confirmed in the literature"].
- Ethanolamine rows (GO:0034228 ISS, GO:0034229 IEA) kept non-core with the conditionality
  made explicit: [PMID:38302740 "MFSD7c did not increase uptake of ethanolamine"] versus
  [PMID:38302740 "transport of ethanolamine by MFSD7c was increased to a significant level
  when ETNK1 was co-expressed"] and [PMID:38778100 "alanine substitution of the analogous
  Q191FLVCR2 residue abolishes the transport of both ethanolamine and choline in FLVCR2"].
- Unchanged actions but rewritten reasons: GO:0015220 (IDA, IEA) ACCEPT; GO:0015871 ACCEPT;
  GO:0022857 MODIFY to GO:0015220; GO:0055085 MODIFY to GO:0015871; GO:0005886 (IEA, ISS)
  ACCEPT; GO:0005789 and GO:0031966 (IEA and ISS each) KEEP_AS_NON_CORE.

Other changes: `description` rewritten as standalone biology (uniporter mechanism,
localization, BBB choline supply, ethanolamine as secondary substrate, Fowler-syndrome
phenotype) with no curation commentary; `reference_review` added to all four PMIDs
(PMID:20823265 marked DISPUTED - correctly cited but its central import claim is
uncorroborated; PMID:32369449 marked full_text_unavailable and cited only for abstract
statements); `core_functions` reduced to the single choline-uniport entry with primary
quotes; questions and experiments rewritten around the flvcr2a/flvcr2b co-ortholog
redundancy and the untested zebrafish in vivo role. Validation: zero errors, zero warnings.
