# Hspa5 (rat BiP/GRP78, UniProt P06761) notes

## Re-review 2026-10-10

GOA changes since the original review:
- New rows (12, all resolved): GO:0005524 ATP binding IEA (InterPro); cytoplasm ISO (human
  P11021) and ISS (mouse P20029); ER lumen ISO located_in and ISS (P11021); cell surface ISO;
  melanosome ISO and ISS; GO:0044183 protein folding chaperone IEA (ARBA00029119) and IPI
  (PMID:11884402, with thyroglobulin RGD:3848); GO:0009725 response to hormone IDA
  (PMID:11884402); GO:0045732 positive regulation of protein catabolic process ISO (mouse).
- Retired rows (6, reviews kept, retirement sentence added): GO:0000166, GO:0005524 and
  GO:0016787 IEA; GO:0005515 IPI PMID:18757373 (DMP1) and PMID:12514190 (TMEM132A);
  GO:0051082 IPI PMID:11884402. QuickGO confirms GO:0051082 is obsolete ("should be replaced
  by an activity term such as protein folding chaperone (GO:0044183) or unfolded protein
  holdase activity (GO:0140309)"). GOA replaced it with GO:0044183 IPI from the same paper,
  which is what the earlier review recommended. As in St13, the HSP70 chaperone activity has
  a GO term (GO:0044183), so no proposed_new_terms entry is needed.

Action changes:
- GO:0005515 protein binding (5 IPI rows), MARK_AS_OVER_ANNOTATED is no longer allowed:
  - PMID:7916014 (thyroglobulin) -> MODIFY to GO:0044183, because the binding is ATP-sensitive
    client binding [PMID:7916014 "several endoplasmic reticulum (ER) proteins, including BiP,
    ERp72, grp94, and protein disulfide isomerase, bind to a denatured thyroglobulin (Tg)
    affinity column and can be specifically eluted by ATP"]. This matches the curators'
    GO:0044183 IPI for the same interaction from PMID:11884402.
  - PMID:17981125 (Sigmar1), PMID:9714535 (ERp29), PMID:18757373 (DMP1, retired) and
    PMID:12514190 (TMEM132A, retired) -> REMOVE. None of the abstracts supports a specific BiP
    MF; removal does not mean the interactions are false.
- GO:0006983 ER overload response ISO: ACCEPT -> MARK_AS_OVER_ANNOTATED, with a
  propagation_review. The mouse source is Bip mRNA induction [PMID:11854325 "mRNAs for the ER
  chaperone Bip and the ER stress-associated apoptosis factor Chop were induced in the
  pancreas"], and the term is defined by NF-kappaB activation.
- GO:0042149 cellular response to glucose starvation ISO: ACCEPT -> KEEP_AS_NON_CORE. It is
  an expression response (human source PMID:10085239), not BiP's own molecular role.
- GO:0031625 ubiquitin protein ligase binding ISO: ACCEPT -> KEEP_AS_NON_CORE. The human
  source is an IPI from a Ro/SS-A (Ro52/TRIM21) study (PMID:8666824), not SYVN1/HRD1 as the
  old text claimed; UniProt has "Interacts with TMEM132A and TRIM21".
- New GO:0045732 ISO -> MARK_AS_OVER_ANNOTATED. The mouse source IDA (PMID:18923430, full
  text) shows substrate handover from P58 [PMID:18923430 "BiP-induced dissociation of P58 from
  its substrate depends on the presence of ATP"] and reports no BiP degradation assay; BiP's
  degradation role is participation in ERAD (GO:0036503).
- New GO:0009725 response to hormone IDA -> UNDECIDED. The abstract only says that ERp29 was
  induced by TSH [PMID:11884402 "ERp29 was induced upon treatment of FRTL-5 rat thyrocytes
  with the thyroid-stimulating hormone"], and the full text is not cached.
- Added verbatim supported_by to about 70 ACCEPT/KEEP rows that had none: current UniProt CC
  lines, deep-research quotes, the IEP papers, and donor-side papers for ISO rows (mouse
  conditional knockout PMID:19816510; Cripto/TGF-beta PMID:17991893; ERdj5 PMID:12411443;
  Mtj1 PMID:12065409).
- core_functions: replaced three non-verbatim, paraphrased quotes (flagged
  full_text_unavailable) with verbatim UniProt and paper quotes; added supported_by to the
  ATP hydrolysis entry; removed project-rule wording and stated why GO:0044183 rather than
  GO:0140309 fits. Description: typo fix only.

Open questions:
- GO:0009725 (IDA, PMID:11884402): does the full text show a TSH-induced change in BiP? If it
  does, IEP is the more usual code.
- GO:0071353 cellular response to interleukin-4 (ISO from MGI IDA PMID:9798653) rests on a
  cDNA-subtraction expression screen; kept non-core, but it is an expression observation.
