# PPP3CA notes

## Session 2026-10-03: completion of DRAFT review (ADAPTIVE_IMMUNITY project, part 5 calcineurin)

Starting state: DRAFT review with all 125 rows actioned but no core_functions. The
earlier session's summaries cited PMIDs with no verbatim quotes, and every review
reused the same few boilerplate sentences.

### GOA refresh
`just fetch-gene human PPP3CA` added 6 rows, all reviewed:
- protein binding IPI PMID:11114196 (MYOZ2/calsarcin-1): REMOVE (anchoring partner)
- protein binding IPI PMID:19896943 (PPP3R1): REMOVE (paper WITHDRAWN)
- protein binding IPI PMID:25416956 (C16orf74): REMOVE (HuRI Y2H hit)
- protein binding IPI PMID:26248042 (RCAN3): REMOVE (inhibitor docking)
- protein binding IPI PMID:30611118 (Q68ED7, mouse CRTC1): REMOVE (substrate)
- protein dimerization activity IPI PMID:11005320 (with Q08209 itself): UNDECIDED

The remote GOA file differs from the local `PPP3CA-goa.tsv`, but the local file was not
overwritten (no `--force`). The review matches the local file exactly. The local file has
one duplicated IDA calmodulin binding row from PMID:18384083, which appears once in the review.

### Changes to existing actions (re-check against CLAUDE.md)
- Every row now has a specific summary/reason. Experimental and core rows have verbatim
  `supported_by` quotes from cached papers.
- Removed a meaningless supported_by quote ("model: Edison Scientific Literature") from the IBA
  GO:0033192 row.
- Protein binding (25 rows, all REMOVE): the reasons now give the actual partner class.
  Partners are CnB/PPP3R1 (captured by calcineurin complex), substrates (NFATC2, DNM1L, CRTC1/2),
  inhibitors (RCAN1, RCAN3), docking/anchoring partners (calsarcins, C16orf74, SPATA33, TARP
  gamma-8, NHE1), screen hits (GRB2) or rows from a withdrawn paper (USP14, PPP3R1;
  PMID:19896943). GO:0030346 protein phosphatase 2B binding was not used as a MODIFY target,
  because it is self-referential on a calcineurin subunit (same as PPP3CB).
- GO:0070886 positive regulation of calcineurin-NFAT signaling cascade (NAS x2): ACCEPT ->
  MARK_AS_OVER_ANNOTATED. PPP3CA is the cascade's catalytic step (involved_in GO:0033173),
  not an outside regulator.
- GO:1905949 negative regulation of Ca2+ import across plasma membrane (NAS, PMID:17640527):
  MARK_AS_OVER_ANNOTATED -> KEEP_AS_NON_CORE. The paper reports that "anchored CaN dominantly
  suppresses PKA enhancement of the channel". The positive-direction row stays over-annotated.
- GO:0051592 response to calcium ion: ACCEPT -> KEEP_AS_NON_CORE (broad stimulus term).
- GO:0016311 dephosphorylation (TAS): ACCEPT -> MODIFY to GO:0006470 protein dephosphorylation.
- GO:0019899 enzyme binding IDA, PMID:11005320: KEEP_AS_NON_CORE -> UNDECIDED.
- GO:0046983 protein dimerization IPI, PMID:11005320: REMOVE -> UNDECIDED.
  PMID:11005320 is abstract-only, and the abstract describes only an SSCP polymorphism screen.
  CLAUDE.md does not allow removing an experimental row whose full text we have not read.
  The calmodulin binding and calcineurin-mediated signaling rows from the same paper stay
  ACCEPT, because those functions are well established.
- GO:0005509 calcium ion binding (NAS, PMID:8392375): stays MARK_AS_OVER_ANNOTATED, matching
  PPP3CB. The cloning paper does not address Ca2+ binding, CnA's metals are Fe3+/Zn2+, and
  the Ca2+ EF-hands are on CnB and calmodulin. I first set this row to REMOVE, then
  reverted it for consistency with the PPP3CB review.
- NEW bar: no NEW rows. GO:0050852 TCR signaling was considered. PPP3CA does perform a step
  (NFAT dephosphorylation), but that step is captured by GO:0033173. Whether to link
  GO:0033173 to TCR signaling is a modelling question, raised in suggested_questions.

### Core functions
Consistent with PPP3CB: MF GO:0033192 calmodulin-dependent protein phosphatase activity
(is_a GO:0004723 calcium-dependent protein Ser/Thr phosphatase activity; checked in OLS),
in_complex GO:0005955 calcineurin complex, location GO:0005829 cytosol.
1. Catalytic activity -> protein dephosphorylation and calcineurin-mediated signaling
   (substrates: NFAT, Elk-1, DARPP-32, DNM1L, SSH1L, KLHL3) [PMID:19154138 "CaN alpha
   dephosphorylates the transcription factor Elk-1 with 7- and 2-fold higher catalytic
   efficiencies than the beta and gamma isoforms, respectively"].
2. NFAT dephosphorylation in GO:0033173 (substrates NFATC1, NFATC2), with T cell, cardiac,
   muscle, bone and neuronal contexts [PMID:8631904 "We also demonstrate a direct interaction
   between calcineurin and NFAT1 that is consistent with a direct enzyme-substrate relation
   between these two proteins"].
3. Calmodulin binding as the activating input [PMID:18384083 "Upon binding of Ca2+ and
   calmodulin (Ca2+/CaM) to CaMBD, the autoinhibitory domains dissociate from the catalytic
   groove, thus activating the enzyme."].

## Deep research integration (falcon)

The report (`PPP3CA-deep-research-falcon.md`) relies mainly on 2023-2025 reviews (Lim 2023,
Nolze 2023, Fonodi 2024) and on calcineurin-inhibitor clinical material (voclosporin, trial
registries). It contains few primary findings about PPP3CA itself.

Adopted (traced to primary papers, cached, quoted):
- c-Myc as a direct calcineurin substrate (Thr58/Ser62), from Masaki 2023, PMID:37573463
  [cached; "Calcineurin directly dephosphorylates Thr58 and Ser62 in c-Myc, which inhibit
  binding to the ubiquitin ligase Fbxw7."]. Used in the description only; the abstract does
  not say which CnA isoform was tested.
- PPP3CA isoform lengths and genotype-phenotype, from Castiglioni 2024, PMID:39707491
  [cached]. The isoform lengths 521/511/469/289/454 aa match UniProt (isoform 4 = 521 - 232
  aa deletion 87..318). Autoinhibitory-domain variants are gain-of-function and cause ACCIID
  ["with a gain-of-function mechanism"]. Used in the description.
- Confirming (no change needed): Ca2+/CaM activation through displacement of the AID, PxIxIT and
  LxVP docking, and NFAT dephosphorylation as the canonical pathway. These were already supported
  by PMID:18384083, PMID:23468591 and PMID:27974827.

Rejected / not used:
- Clinical CNI efficacy data (voclosporin, lupus nephritis meta-analysis, NCT trials) is drug
  pharmacology and does not inform PPP3CA gene function.
- The VSMC targets (NCX1, RyR, AMPA/NMDA receptors, TFEB, FOXO, MEF2) are cited only to a
  review (Nolze 2023), are not specific to the alpha isoform, and were not traced. TFEB
  dephosphorylation by PPP3CA is in UniProt (PMID:33691586) but was not added to the review.
- Neutrophil CN-NFAT chemokine data (Vymazal 2024) used pharmacological inhibitors, so it is
  not attributable to PPP3CA specifically.

Report errors:
- It gives the catalytic cofactors as "Zn2+ and Fe2+". UniProt and the crystal structures give
  Fe3+ and Zn2+ (binuclear Fe/Zn site, PMID:8524402).
- It cites a 2026 meta-analysis and a 2025 review for "current" data. These are not errors,
  but they are irrelevant to function.

No annotation action changed because of the report.

- Coordinator follow-up: the two GO:0070886 positive regulation of calcineurin-NFAT signaling cascade (NAS) rows were changed from MARK_AS_OVER_ANNOTATED to MODIFY -> GO:0033173, matching the PPP3CB review.

- Coordinator follow-up: the GO:1905665 positive regulation of calcium ion import (NAS, PMID:17640527) row was changed from MARK_AS_OVER_ANNOTATED to REMOVE, since the cited study contradicts the direction; this matches PPP3R1.
