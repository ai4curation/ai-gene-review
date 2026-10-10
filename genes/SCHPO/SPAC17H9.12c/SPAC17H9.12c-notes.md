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
- The target-specific mitochondrial localization from PMID:16823372 and the
  UniProt mitochondrial outer-membrane row were accepted.
- The S. cerevisiae `CYC2` ISO to `GO:0031314 extrinsic component of
  mitochondrial inner membrane` was removed. The donor is a real inner-membrane
  intermembrane-space-facing flavoprotein, but this topology conflicts with the
  target-supported UniProt mitochondrial outer-membrane row.
- The PomBase IC row to `GO:1903607 cytochrome c biosynthetic process` was
  accepted as a CYC2-like inference from the characterized budding-yeast
  protein. This row should not be expanded into `GO:0004128` cytochrome-b5
  reductase activity: that term is only the historical GO annotation used as
  the IC basis, and no specific PTHR19370 cytochrome-b5 reductase PAINT node
  propagates to O13809.
- `just deep-research-falcon SCHPO SPAC17H9.12c --fallback perplexity-lite`
  could not run to completion because no deep-research provider API keys were
  available. Manual web searches for `O13809`, `SPAC17H9.12c`, `C17H9.12c`,
  `Schizosaccharomyces pombe cyc2`, and `Saccharomyces CYC2` found product and
  database records plus the S. cerevisiae Cyc2p papers, but no direct S. pombe
  SPAC17H9.12c biochemical paper that would establish the immediate electron
  donor or acceptor.
