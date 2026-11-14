# spuE (PA0301, Q9I6J0) review notes

Periplasmic solute-binding protein of the PotD/PotF family (PIRNR019574;
Pfam SBP_bac_8; InterPro IPR001188), 365 aa with a 24-residue signal peptide.
Paralog of SpuD (57% identical) in the spuDEFGH ABC transporter locus.

## Literature (no deep-research provider available; own reading)

- Lu et al. 2002 (full text cached, PMC135167): spuE mutant greatly reduced in
  spermidine uptake [PMID:12081945 "Second, spermidine uptake is inducible in
  spermidine-grown cells and is greatly reduced in either spuD or spuE mutant
  (Fig."]. PseudoCAP IMP source for polyamine transport.
- Wu et al. 2012 (abstract only; UniProt curated text from this paper): SpuE
  binds spermidine exclusively [PMID:22300763 "we found that SpuD is a
  putrescine-preferential binding protein, while SpuE binds to spermidine
  exclusively."]; a Trp271Phe substitution gives SpuE substantial putrescine
  affinity [PMID:22300763 "substitution of Trp271 by Phe enabled SpuE to gain
  substantial binding affinity for putrescine"]. UniProt: "Binds spermidine
  with high affinity (KD=14.3 nM). Does not bind putrescine, cadaverine or
  spermine." PseudoCAP IDA source for spermidine binding. UniProt also records
  reduced T3SS induction in the spuE mutant (not annotated in GOA; not added).

## PseudoCAP IBA-seed assessment

Other seeds' experimental support queried live in QuickGO on 2026-11-05.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001249912 | GO:0015846 polyamine transport | 4 | 78 (57 taxa) | GO:0015846, IMP, PMID:12081945 (PseudoCAP) | SOUND | Full text shows spuE mutant greatly reduced in spermidine uptake; node term suits the PotD/PotF clade. | SpuD Q9I6J1 (same paper), E. coli PotD P0AFK9, PotF P31133 | Yes |
| PTN008624361 | GO:0019809 spermidine binding | 2 | 35 (10 taxa) | GO:0019809, IDA, PMID:22300763 (PseudoCAP) | SOUND | Abstract states SpuE binds spermidine exclusively; spermidine-bound crystal structure; UniProt KD 14.3 nM. | E. coli PotD P0AFK9 (IDA PMID:1939142, PMID:8366082; IPI) | Yes; PotD has IDA |

No PSEUDOCAP defect on spuE.

### Node-level problem at PTN008624361 (recorded here for the batch)

PTN008624361 also carries GO:0019810 putrescine binding (seeds SpuD, PotF,
PotD) and GO:0015847 putrescine transport (seeds PotF, PotD). Both propagate to
SpuE, which does not bind putrescine (abstract and UniProt curated text from
PMID:22300763). The IBDs are sound for the seeds, but the node terms do not suit
the SpuE branch. Two GO_CENTRAL MISSING_NEGATION defects are recorded on the
spuE IBA rows: GO:0019810 (CONFIRMED, the abstract states it outright) and
GO:0015847 (PROBABLE; SpuE is part of a transporter that may move putrescine
via SpuD, so the full text could qualify the call). spuD notes cross-reference
these; no separate defect is recorded there.
