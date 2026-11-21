# UBA5 (Q9GZZ9) research notes

## Summary
UBA5 (ubiquitin-like modifier-activating enzyme 5) is the E1-activating enzyme of the ufmylation pathway, the first and rate-limiting step in conjugation of the ubiquitin-like modifier UFM1 to substrate proteins. UBA5 is a minimalistic, single-domain (ThiF/MoeB-type adenylation domain) E1 that functions as a homodimer. It activates mature UFM1 by adenylating UFM1's C-terminal glycine with ATP and then forming a high-energy thioester between that glycine and the catalytic cysteine (Cys250), releasing AMP. UFM1 is bound in trans across the two subunits of the UBA5 homodimer, and activated UFM1 is then transferred to the E2-conjugating enzyme UFC1 via UBA5's C-terminal UFC1-binding sequence. UBA5 binds zinc and uses a UFM1-interacting sequence (UIS) that also engages GABARAP/LC3 family proteins, which recruit UBA5 to the ER membrane. Acting at the cytosol and ER, UBA5-initiated ufmylation supports ribosome recycling, the response to ER stress, reticulophagy, the DNA-damage response, innate-immune (RIG-I/interferon) signaling, and erythroid/megakaryocyte differentiation. Biallelic UBA5 loss-of-function variants cause developmental and epileptic encephalopathy (DEE44) and autosomal-recessive spinocerebellar ataxia (SCAR24).

## Core functions (from review)
- **GO:0071566 UFM1 activating enzyme activity** — UBA5 is the E1-activating enzyme of the ufmylation cascade. As a homodimer it adenylates the C-terminal glycine of mature UFM1 with ATP and forms a high-energy thioester between that glycine and its catalytic Cys250 (releasing AMP), then transfers activated UFM1 to the E2 enzyme UFC1.
- **GO:0042803 protein homodimerization activity** — UBA5 homodimerization is an integral part of its catalytic mechanism. The two subunits cooperate in a trans-binding mechanism in which UFM1 contacts distinct sites on both protomers, and dimerization is required for UFM1 activation.

## Provenance
Research and verbatim supporting quotes are recorded inline in `UBA5-ai-review.yaml` (per-annotation `supported_by` and `references` findings). This notes file summarizes the completed review; see the YAML for evidence citations.

## 2026-11-19 ORGANELLES Golgi batch 4 (Golgi apparatus rows)

- Two GO:0005794 rows (UniProt SubCell IEA; UniProt EXP from PMID:26872069), matching -goa.tsv. Both
  located_in.
- PMID:26872069 (full text in cache): endogenous UBA5 co-localizes with GM130 in HEK293A and HeLa cells
  (Fig 2B) beside a mainly cytoplasmic signal [PMID:26872069 "found that endogenous UBA5 co-localized
  with GM130 (Golgi marker)"]. No antibody validation by depletion; no UFMylation step shown at the Golgi.
- Both rows stay KEEP_AS_NON_CORE, reasons record the check: recruited pool of a soluble cytosolic E1
  whose membrane activity is at the ER (consistent with UFL1, UFSP2, DDRGK1, none of which has a Golgi
  row, and with the ORGANELLES 2026-11-17 note). No sub-compartment row (GM130 only). core_functions
  unchanged (cytosol, ER membrane).
