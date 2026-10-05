## 2026-10-01 live-GOA and IBA refresh

- Refreshed ATG7 against current GOA. The live export now has 56 physical rows.
  The review keeps two stale exact rows as `retired: true`: the old
  `GO:0006914 autophagy` keyword IEA and the old `GO:0015031 protein transport`
  keyword IEA.
- Rechecked PTHR10953 PAINT. The current PAINT export has nine live IBD
  assertions for ATG7: broad root calls at `PTN000102039` and `PTN000102040`,
  and seven ATG7-clade calls at `PTN000102341` covering phagophore assembly
  site localization, Atg8/Atg12 activating enzyme activities, autophagosome
  assembly, mitophagy, cellular response to nitrogen starvation, and piecemeal
  microautophagy of the nucleus. All nine remain biologically sound for the
  conserved Atg7 E1-like enzyme.
- Resolved the nine newly seeded live rows. All are exact-partner
  `GO:0005515 protein binding` splits from `PMID:10688190`, `PMID:12965207`,
  `PMID:18719252`, `PMID:22056771`, and `PMID:23142976`; eight rows to the
  yeast E2s Atg3 and Atg10 were modified to `GO:0044390 ubiquitin-like protein
  conjugating enzyme binding`, while the human MAP1LC3B cross-species row was
  removed because it does not support a physiological yeast molecular function.
- Searched for 2025-2026 ATG7 literature and cached `PMID:42141163`, a 2026
  full-text Commun Biol paper showing that the N termini of yeast Atg8 and
  Atg12 tune selective transfer through Atg7. This refines the Atg7 substrate
  discrimination mechanism but does not require a new GO annotation.
- Follow-up on PR 3721 repointed the seven Atg8 `protein binding` MODIFY rows
  from the erroneous `GO:0061664` Pup-ligase identifier to `GO:0032182
  ubiquitin-like protein binding`. A live QuickGO check showed that
  `GO:0097632` was renamed to `extrinsic component of phagophore membrane` on
  2026-08-21 and moved under `GO:7770114 phagophore membrane`, so the row now
  keeps the UniProt IDA instead of weakening it to `GO:0000407`.

The refreshed review has 58 total rows: 56 current GOA rows and 2 retired
historical rows. Final action counts are 31 ACCEPT, 4 REMOVE, 21 MODIFY,
1 KEEP_AS_NON_CORE, and 1 MARK_AS_OVER_ANNOTATED.
