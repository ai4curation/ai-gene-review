# spuD (PA0300, Q9I6J1) review notes

Periplasmic solute-binding protein of the PotD/PotF family (PIRNR019574;
Pfam SBP_bac_8; InterPro IPR001188), 367 aa with a 24-residue signal peptide.
Part of the spuDEFGH ABC transporter locus (spermidine and putrescine
utilization) together with its paralog SpuE (57% identical).

## Literature (no deep-research provider available; own reading)

- Lu et al. 2002 (full text cached, PMC135167): spuD and spuE mutants are both
  defective in spermidine uptake [PMID:12081945 "Second, spermidine uptake is
  inducible in spermidine-grown cells and is greatly reduced in either spuD or
  spuE mutant (Fig."]; the authors concluded that spermidine rather than
  putrescine is the preferred ligand [PMID:12081945 "Contrary to such sequence
  similarities, SpuD and SpuE prefer spermidine rather than putrescine as the
  transport ligand as determined empirically in this report."]. This is the
  PseudoCAP IMP source for polyamine transport.
- Wu et al. 2012 (abstract only; UniProt curated text from this paper): ITC and
  crystal structures show SpuD is putrescine-preferential [PMID:22300763 "we
  found that SpuD is a putrescine-preferential binding protein, while SpuE binds
  to spermidine exclusively."]. UniProt: "Binds putrescine with high affinity
  (KD=3 nM), spermidine with relatively low affinity (KD=6.8 uM)." This is the
  PseudoCAP IDA source for putrescine binding.
- The two papers differ on SpuD's preferred ligand (uptake competition versus
  direct binding). Direct binding favours putrescine; the uptake data show SpuD
  also contributes to spermidine uptake. Both putrescine transport and
  spermidine transport are therefore supported, and the general polyamine
  transport rows are modified to both.

## PseudoCAP IBA-seed assessment

Other seeds' experimental support queried live in QuickGO on 2026-11-05.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001249912 | GO:0015846 polyamine transport | 4 | 78 (57 taxa) | GO:0015846, IMP, PMID:12081945 (PseudoCAP) | SOUND | Full text shows spuD mutant greatly reduced in spermidine uptake. Term is general but correct; node term suits a PotD/PotF clade. | SpuE Q9I6J0 (same paper), E. coli PotD P0AFK9 and PotF P31133 (experimental binding/transport) | Yes |
| PTN008624361 | GO:0019810 putrescine binding | 3 | 35 (10 taxa) | GO:0019810, IDA, PMID:22300763 (PseudoCAP) | SOUND | Abstract states SpuD is putrescine-preferential; UniProt curated KD 3 nM from the paper. | E. coli PotF P31133 (IDA PMID:8416922, IPI), PotD P0AFK9 (IDA PMID:1939142, PMID:8366082) | Yes |

No PSEUDOCAP defect on spuD. The PTN008624361 putrescine-binding IBD is sound
for SpuD, PotF and PotD, but the node term does not suit the whole clade: it
propagates to SpuE, which does not bind putrescine. That node-level
GO_CENTRAL MISSING_NEGATION defect is recorded once, on the spuE GO:0019810 IBA
row (genes/PSEAE/spuE), where the direct evidence sits.

SpuD's own spermidine-binding IBA (from PTN008624361, seeded by SpuE and PotD)
is correct but low affinity (KD 6.8 uM), so it is kept as non-core. Open
question, not a defect: E. coli PotF (P31133) also receives the spermidine
binding IBA, although its curated function records only putrescine binding; I
have not read the PotF papers, so I raise this as a question only.
