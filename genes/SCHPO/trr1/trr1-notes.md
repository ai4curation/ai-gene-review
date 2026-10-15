# trr1 (SPBC3F6.03, synonym caf4, UniProt Q92375) – notes

Low-Mr (class-II) thioredoxin reductase. Module: thioredoxin reductase in `glutathione_thioredoxin_redox_systems`. S. cerevisiae orthologs TRR1 (cytosolic, review genes/yeast/TRR1) and TRR2 (mitochondrial).

Naming trap: synonym caf4 collides with unrelated S. cerevisiae CAF4 (CCR4-associated factor).

## Evidence
- Only TrxR gene: [PMID:15135546 "The unique putative gene for thioredoxin reductase (TrxR) was isolated from the chromosomal DNA of the fission yeast Schizosaccharomyces pombe."]
- Activity by dosage: [PMID:15135546 "The S. pombe cells harboring the cloned TrxR gene contain increased TrxR activity, and shows higher survivals on solid media with mercuric chloride or aluminum chloride."]
- Pap1-mediated induction by menadione/HgCl2 [PMID:15135546].
- IDA + IPI (with Tpx1) from PMID:17409354, abstract-only; abstract does not mention Trr1. Deferred to curator for IDA; IPI "protein binding" removed per policy.
- Cytosol/nucleus ORFeome HDA [PMID:16823372]. Mitochondrion ISS from S. cerevisiae TRR2 left UNDECIDED: plausible (single TrxR, mitochondrial Trx2 exists) but no S. pombe data.

## Decisions
- removal of superoxide radicals (InterPro2GO IPR005982) REMOVE, as in yeast TRR1.
- Core MF GO:0004791, BP GO:0045454, cytosol — matches yeast TRR1.
- No PomBase GO-CAM association for trr1 in the module (only YeastPathways THIOREDOX-PWY for TRR1/TRR2).
