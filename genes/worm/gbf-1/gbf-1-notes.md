# gbf-1 review notes

## 2026-10-28 initial review

- `just fetch-gene worm gbf-1` timed out on the UniProt gene-name search three times; the entry was
  fetched by accession instead (`just fetch-gene worm G5EGS5 --alias gbf-1`). UniProt G5EGS5
  (Swiss-Prot GBF1_CAEEL), folder genes/worm/gbf-1, 15 GOA rows.
- Literature: PMID:23840591 full text read [PMID:23840591 "GBF-1 is present on the cis-face of the
  Golgi at so-called transitional ER-Golgi elements"]; PMID:25190516 abstract only; PMID:26115433 full
  text (SGK-1 interactor screen); PMID:35998789 abstract only (miRNA target, not informative).
  Summary with quotes in `gbf-1-deep-research-manual.md`.
- Isoform b (G5EGS5-2) lacks residues 1-1490 and so lacks the Sec7 domain (624-812); it cannot be an
  exchange factor on its own. No functional data on it.
- No in vitro exchange assay exists for the worm protein. The GEF claim rests on the Sec7 domain and
  orthology to GBF1/Gea1/2/garz.

### Decisions
- GEF activity (IBA, IEA): ACCEPT, core.
- Golgi cis cisterna (IBA, IDA): ACCEPT, core location.
- ERGIC (EXP, IEA): ACCEPT, maps the t-ER-Golgi element localization.
- Golgi apparatus (IEA): ACCEPT (root organelle; claim holds on IDA cis-Golgi).
- ER exit site (IDA): KEEP_AS_NON_CORE; only partial overlap with SEC-16, protein sits on the Golgi
  side of the ERES-Golgi unit.
- retrograde Golgi-to-ER transport (IBA): ACCEPT, core process (GEF step for COPI).
- regulation of ARF protein signal transduction (IEA): ACCEPT.
- Golgi organization (IBA), ER organization (IMP), secretion (IMP), endosomal transport (IMP),
  mitochondrion organization (IMP): KEEP_AS_NON_CORE. Real phenotypes, but the authors themselves
  argue ER and secretion effects are indirect; endosomal and mitochondrial roles are less well
  established (mitochondrial paper abstract only).
- No NEW rows (strict NEW bar). A COPI-coat recruitment term would be the natural participation
  term, but there is no worm-specific evidence beyond phenotypes; raised as a question.
