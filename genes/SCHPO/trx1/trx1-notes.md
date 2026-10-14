# trx1 (SPAC7D4.07c, UniProt O14463) notes

Naming trap: UniProt lists `trx2` as a synonym of trx1 (O14463, 103 aa, cytosolic). PomBase
trx2 (SPBC12D12.07c) is the distinct mitochondrial thioredoxin (121 aa, N-terminal presequence)
[PMID:12020831 "It has extra N-terminal 17 amino acid residues compared to previously
identified thioredoxin (TRX1)"]. trx3/txl1 is a third (cytosolic, proteasome-associated)
thioredoxin.

## Evidence journal

- Family/active site: classical thioredoxin, CGPC active site Cys30/Cys33 redox-active
  disulfide [UniProt:O14463 "FUNCTION: Participates in various redox reactions through the"].
- Main cytosolic Trx; ∆trx1 sensitive to oxidants, heat and salt; trx1 induced by H2O2 via
  Pap1; trx1 deletion causes cysteine auxotrophy rescued by sulfite, implicating Trx1 as the
  PAPS reductase donor [PMID:18758731 "This suggests that Trxl serves as a primary electron
  donor for 3'-phosphoadenosine-5'-phosphosulfate (PAPS) reductase and thus is an essential
  protein for sulfur assimilation in S. pombe."].
- Electron donor to the peroxiredoxin Tpx1 and other oxidized proteins [PMID:22245228 "the
  Prx Tpx1 is a major substrate for thioredoxin in the fission yeast Schizosaccharomyces
  pombe"].
- Electron donor of ribonucleotide reductase (Cdc22) with Trx3 [PMID:28640807 "Trx1 and Trx3
  are the primary electron donors for RNR in fission yeast."]; also lists Met16 and Mxr1 as
  Trx-recycled enzymes [PMID:28640807 "These two cascades have to recycle enzymes which
  suffer disulfide formation as part of their catalytic functions, such as the essential
  Cdc22 and the non-essential Tpx1, Mxr1 or Met16 (Fig 1A)."].
- Gpx1 prefers thioredoxin as donor [PMID:18162174 "The Gpx1 protein has a peroxidase activity
  but preferred thioredoxin to glutathione as an electron donor when examined in vitro and in
  vivo"].
- IPI partners in PMID:17409354: SPCC576.03c = tpx1 (substrate), SPBC3F6.03 = trr1 (thioredoxin
  reductase, the NADPH-dependent regenerating enzyme; identified via gocams/index.tsv).
- PomBase GO-CAM gomodel:66a3e0bb00001342 activity 66a3e0bb00001398: trx1 enables GO:0009055
  electron transfer activity, occurs in cytosol, part_of GO:0000103, provides input for (RO:0002413)
  met16 PAPS reductase.
- Module: aps_dependent_assimilatory_sulfate_reduction, thioredoxin_electron_donor role
  (function GO:0015035). S. cerevisiae TRX1/TRX2 have no review in this repo yet;
  trx1 trx2 double deletion in S. cerevisiae is a methionine auxotroph (PMID:2026619, per module).
  S. pombe differs: the single trx1 deletion is already a cysteine/sulfur auxotroph.

## Observations
- PMID:12020831 is the trx2 (mitochondrial) cloning paper; its IDA for GO:0034614 on trx1
  may reflect the trx1/trx2 synonym confusion. Abstract-only, so UNDECIDED rather than REMOVE.
- 'protein binding' IPI rows (trr1, tpx1) are informative only as the redox partners; the
  activity is captured by GO:0015035.
