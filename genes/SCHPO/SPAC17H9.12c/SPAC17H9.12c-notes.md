# SCHPO SPAC17H9.12c Notes

## 2026-10-10

- Seeded `SCHPO/SPAC17H9.12c` from GOA and reviewed all 6 current rows
  against the `PTHR19370` PAINT cache.
- The S. pombe protein `O13809`, ORF `SPAC17H9.12c`, is in
  `PTHR19370:SF184`, the same PANTHER NADH-cytochrome b5 reductase-like
  subfamily as S. pombe `cbr1` and S. cerevisiae `CBR1`.
- GOA currently has one IBA row: broad `GO:0016491 oxidoreductase activity`
  propagated from `PANTHER:PTN001833551`. The ancestral node is biologically
  sound for O13809 and deliberately broad; the more specific PTHR19370 PAINT
  rows for cytochrome-b5 reductase activity, ergosterol biosynthesis, nitrate
  reductase activity, nitrate assimilation, cytokinin metabolism, and electron
  transport are all placed on other PANTHER nodes and do not currently
  propagate to SPAC17H9.12c.
- The InterPro `GO:0016491` row was also accepted. The protein has CBR-like
  and FAD-binding FR-type signatures, but neither GOA nor UniProt imports an
  EC or Rhea reaction for O13809.
- The target-specific broad mitochondrial localization from PMID:16823372 was
  accepted. The UniProt mitochondrial outer-membrane row and PomBase
  CYC2-derived inner-membrane ISO were both left `UNDECIDED` because the cached
  fission-yeast YFP evidence does not resolve the submitochondrial topology.
- The S. cerevisiae `CYC2` ISO to `GO:0031314 extrinsic component of
  mitochondrial inner membrane` was left unresolved. The donor is a real
  inner-membrane intermembrane-space-facing flavoprotein, but O13809 also has an
  unresolved, UniProt-derived outer-membrane call and no direct topology assay.
- The PomBase IC row to `GO:1903607 cytochrome c biosynthetic process` was
  kept as non-core. It records a curator's CYC2-like inference, but PANTHER
  groups O13809 with CBR1-family SF184 members rather than yeast CYC2, the
  `GO:0004128` IC basis is dangling, and no specific PTHR19370 cytochrome-b5
  reductase PAINT node propagates to O13809.
- `just deep-research-falcon SCHPO SPAC17H9.12c --fallback perplexity-lite`
  could not run to completion because no deep-research provider API keys were
  available. Manual web searches for `O13809`, `SPAC17H9.12c`, `C17H9.12c`,
  `Schizosaccharomyces pombe cyc2`, and `Saccharomyces CYC2` found product and
  database records plus the S. cerevisiae Cyc2p papers, but no direct S. pombe
  SPAC17H9.12c biochemical paper that would establish the immediate electron
  donor or acceptor.
