# daf-15 review notes

- Fetched UniProt id confirmed: G5EEV7 (WormBase WBGene00000911, GeneID 177770). 5 GOA rows.
- Deep research API unavailable; literature compiled manually in daf-15-deep-research-manual.md.

## Evidence notes

- DAF-15 = Raptor ortholog [PMID:15253933 "The daf-15 (raptor) and let-363 (CeTOR) mutants shift metabolism to accumulate fat, and raptor mutations extend adult life span."]
- TORC1 membership in worm [PMID:18804378 "C. elegans possesses homologues of TOR complex 1 (TORC1) components, including TOR kinase (let-363 [21]), Raptor (daf-15; [15]) and LST8"]
- Functional TORC1 activation through DAF-15 fusion [PMID:23705068 "We fused a 22-amino acid fragment of the C-terminal end of rap-1 to the C-terminal end of daf-15 and named it daf-15::rap-1(22)."; "This indicates that hyperactivation of TORC1 was sufficient to support L1 growth in mmBCFA-depleted animals."]
- Lifespan IGI: let-363+daf-15 RNAi from L4 extends lifespan, pha-4 dependent [PMID:18804378 "Reduction of let-363 and daf-15 together led to a statistically-significant increase in lifespan in 3/4 experiments"].
- Dauer IMP: daf-15(m81) dauer-like larvae [PMID:3350212, abstract only].

## Decisions

- TOR signaling IEA -> MODIFY to TORC1 signaling (GO:0038202): Raptor is TORC1-specific.
- TORC1 complex (IEA, ISS) -> ACCEPT (core location/complex).
- Lifespan, dauer -> KEEP_AS_NON_CORE (organismal outputs of TORC1 signaling).
- NEW MF protein-macromolecule adaptor activity (GO:0030674), ISS to human RPTOR, consistent with
  the DROME/raptor review; no worm biochemistry exists, flagged as a question.
- No NEW process terms (growth/fat/germline phenotypes are downstream of TORC1 signaling and fail the NEW bar).
