# NCU01540 (Q7RWZ3) re-review sequence comparison

Script: `compare_sequences_rereview.py` (run with `uv run --script`); raw output in
`results-rereview.json`. Sequences fetched live from UniProt REST on 2026-10-21.

## Family placement

PANTHER places Q7RWZ3 in PTHR10283:SF92 (LOW-AFFINITY PHOSPHATE TRANSPORTER PHO91),
together with S. cerevisiae PHO91 (P27514) and S. pombe plt1 (O59712). S. cerevisiae
PHO87 (P25360) and PHO90 (P39535) sit in a different subfamily, PTHR10283:SF110
(INORGANIC PHOSPHATE TRANSPORTER PHO87-RELATED). A UniProt query
(xref:panther-PTHR10283 AND organism_id:367110) returned only Q7RWZ3, so NCU01540 is the
only PTHR10283 member in the N. crassa reference proteome; Neurospora has no SF110
Pho87/Pho90 paralog.

## Global pairwise identity (BLOSUM62, gap open -10, extend -0.5)

| Comparison | Subfamily of partner | Identity over aligned pairs |
|---|---|---|
| NCU01540 vs PHO91 (P27514) | SF92 | 48.6% (386/794) |
| NCU01540 vs plt1 (O59712) | SF92 | 50.2% (405/806) |
| NCU01540 vs PHO87 (P25360) | SF110 | 40.3% (318/790) |
| NCU01540 vs PHO90 (P39535) | SF110 | 40.8% (322/790) |

The identities agree with the PANTHER subfamily assignment: NCU01540 is closer to the
SF92 members than to the SF110 Pho87/Pho90 pair. These figures corroborate, and do not
replace, the HMM-based subfamily placement.

## SPX inositol-pyrophosphate-binding lysine

Pho91 K237 lies in the SPX inositol-pyrophosphate-binding patch; the pho91-K237A allele
mimics the InsPP-free state (PMID:41324358). In the global alignment, Pho91 K237
(window QTGFSKICKKF) aligns to NCU01540 K241 (window RTGFSKVLKKF). The lysine and its
flanking TGFSK motif are conserved, which fits the hypothesis that the NCU01540 SPX
domain is regulated by inositol pyrophosphates. Binding has not been tested.

## Limits

These are pairwise alignments, not a phylogeny. Transport direction, coupling ion and
resident membrane cannot be inferred from sequence.
