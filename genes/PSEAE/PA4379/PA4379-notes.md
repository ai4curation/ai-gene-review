# PA4379 (warA, Q9HW23) notes

## Literature

No deep-research provider was available. PubMed E-utilities returned HTTP 500
on 2026-11-05; the cached publications were searched for WarA/PA4379, and only
PMID:28263305 was found.

- WarA was identified as a SadC partner by bacterial two-hybrid screening, and
  forms a complex with WarB [PMID:28263305 "WarA was shown to specifically
  interact with the cytoplasmic part of SadC and form a complex with WarB"].
- It binds c-di-GMP by DRaCALA, specifically [PMID:28263305 "WarA was capable of
  binding to c-di-GMP (Fig. 4b) in the low micromolar range"].
- It is a SAM-dependent methyltransferase with LPS as substrate, stimulated by
  c-di-GMP [PMID:28263305 "LPS was shown to be a substrate for WarA"].
- It affects CPA O-antigen modal distribution and immune evasion in zebrafish.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN008676703 | GO:0008168 methyltransferase activity | 4 | 385 (112 taxa) | GO:0008168, IDA, PMID:28263305 (PseudoCAP) | SOUND | Full text read. Purified WarA, SAM donor, LPS acceptor, activity increases with LPS and with c-di-GMP. Generic MTase is the right level because the product is not characterised. | E. coli RlmA P36999 (23S rRNA m1G745 MTase), M. tuberculosis Rv2952 P9WIN3 (PDIM methyltransferase), human TMT1A Q9H8H3 (thiol/N6-adenosine MTase) | Yes. The other seeds are biochemically characterised MTases; the generic term suits a node whose members methylate very different substrates. No defect. |

PA4178 (EftM) seeds a different methyltransferase node (PTN000010968), also
SOUND; see `genes/PSEAE/PA4178`.

## Decisions

- GO:0005515 protein binding EXP: REMOVE (protein-binding policy).
- Methyltransferase (IDA, IBA) and c-di-GMP binding: ACCEPT.
