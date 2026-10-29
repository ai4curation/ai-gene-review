# raga-1 review notes

## 2026-10-28 initial review

- Fetched with `just fetch-gene worm raga-1`; UniProt Q22743 (TrEMBL, unreviewed); 17 GOA rows.
- See `raga-1-deep-research-manual.md` for the literature summary (no provider deep research was run).

### Decisions

- MF (GTPase activity, GTP binding): family-level, no worm biochemistry. Accepted on
  orthology (IBA; Pfam Gtr1_RagA) and because the T18N/Q63L nucleotide-state mutants
  behave as expected [PMID:20523893 "we made corresponding DN (T18N in C. elegans raga-1) and GF (Q63L) mutations in worm raga-1"].
- CC lysosome (IBA): root organelle term; accepted. Sub-compartment (lysosomal membrane,
  cytosolic face) has only one line of support (orthology), so no NEW sub-compartment row.
- CC nucleus (IBA): kept as non-core; no worm data, seeded by yeast Gtr1/Gtr2 and human
  Rag nuclear pools. Peripheral to the TORC1 function.
- Gtr1-Gtr2 GTPase complex (IBA): accepted; RAGC-1 is the single RagC/D orthologue.
- positive regulation of TORC1 signaling (IBA): accepted as core; worm biochemistry
  supports it (phospho-RSKS-1 falls on RAGA-1 depletion [PMID:37721956], rises with
  endogenous Q63L [PMID:40385374]).
- positive regulation of TOR signaling (IGI with let-363): MODIFY to TORC1 signaling.
- determination of adult lifespan (6 rows), positive regulation of multicellular organism
  growth, negative regulation of autophagy, cellular response to starvation: all
  KEEP_AS_NON_CORE, downstream organismal consequences of TORC1 activity.
- PMID:22560223 cached abstract-only. The PMC full text read through the PubMed tool
  confirms adult-only Rag RNAi extended lifespan; gene names are stripped in that text,
  so it was not quoted.
- No NEW rows. Organismal phenotypes (L1 arrest bypass in elo-5, swimming decline)
  are necessity/sufficiency evidence for TORC1 output and do not meet the NEW-process bar.
