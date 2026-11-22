# cpi-2 notes

## 2026-11-22

- Fetched `worm/cpi-2`, UniProt `G5ECM9` (`CPI2_CAEEL`), as the
  C. elegans same-subfamily comparator for the Brugia malayi CPI-2 cystatin
  lane. BRUMA CPI-2 and worm CPI-2 both sit in PANTHER `PTHR46186:SF2`, but
  Murray et al. separated their inhibitory profiles: Brugia CPI-2 inhibits
  both papain-like cathepsins and AEP/legumain, while recombinant Ce-CPI-2
  blocks cathepsins and lacks AEP inhibition [PMID:15664654, "C. elegans
  proteins, Ce-CPI-1 (K08B4.6) and Ce-CPI-2 (R01B10.1), both of which block
  cathepsins and neither of which possess the ability to block AEP"].
- `just mod-description-deep-research worm cpi-2` reported `no_curated: 1`, so
  there was no hand-written WormBase description to add. `just deep-research
  worm cpi-2 --provider perplexity` failed because Perplexity is not configured
  in this environment; the review therefore uses the seeded GOA publications,
  UniProt and the local PANTHER IBD rows directly.
- `PMID_12704112.md` is full text and supports the recombinant Ce-CPI-2
  cathepsin B/L/S inhibition call. It also argues against copying the filarial
  immunomodulation role onto C. elegans CPI-2: the authors found that the
  free-living nematode cystatins did not suppress antigen-driven lymphocyte
  proliferation like the filarial cystatins and instead produced a more
  Th1-like cytokine response.
- `PMID_16857685.md` is abstract-only locally. Its abstract still names the
  direct gonad and yolk-granule localization experiment and the
  `cpi-2a(ok1256)` yolk-protein/oogenesis phenotype, and UniProt's curated
  `SUBCELLULAR LOCATION` and `FUNCTION` comments record the corresponding
  extracellular, cytoplasmic, yolk-granule and yolk uptake/processing claims
  with experimental ECOs to the same paper.
- `just paint-losses worm cpi-2` reported no IRD or IKR loss on the CPI-2
  PANTHER lineage. The IBA rows for `GO:0004869`, `GO:0005576` and
  `GO:0005737` are current and include C. elegans cpi-2 among the direct
  descendant evidence at `PTN005285938`; the `GO:0031982` vesicle IBA at the
  same node is sourced only from rat cystatin C rows and does not match the
  C. elegans-specific yolk-granule compartment.
