# COX19 curation notes

## 2026-10-01 current-GOA and IBA re-review

Reviewed *Saccharomyces cerevisiae* **COX19/YLL009C-A** after a current GOA/UniProt
refresh. Cox19 is a twin-CX9C protein that partitions between the cytosol and the
mitochondrial intermembrane space, where it binds the IMS-facing domain of Cox11
and supports Cox11 copper coordination during cytochrome c oxidase assembly.

The current GOA has **17** rows. The refresh did not seed any new rows or reveal
any stale rows; it backfilled exact PANTHER, UniProt-SubCell and GO:0044183
supporting entities on the six live IBA/IEA rows.

### IBA / PAINT review

All three IBA rows point to a single node in `PTHR21107-paint.tsv`:

- `PANTHER:PTN001465117 -> GO:0044183 protein folding chaperone`, seeded by
  yeast and human COX19.
- `PANTHER:PTN001465117 -> GO:0033617 mitochondrial respiratory chain complex IV
  assembly`, seeded by yeast and human COX19.
- `PANTHER:PTN001465117 -> GO:0005758 mitochondrial intermembrane space`, seeded
  by yeast and human COX19.

The PAINT placement is sound. COX19 itself in the `WITH/FROM` is target evidence
that the PAINT curator used to place the ancestral IBD, not circular support, and
both yeast and human seeds lie in the same narrow `PTHR21107:SF2` COX19
subfamily.

### Literature checked

Cached publications were sufficient for the existing rows:

- PMID:25926683: direct Cox19-Cox11 interaction work that establishes Cox19 as a
  Cox11 chaperone and shows the interaction occurs dynamically in the IMS.
- PMID:12171940: original COX19 characterization showing Cox19 acts after
  subunit synthesis in cytochrome oxidase assembly and is both cytosolic and
  mitochondrial.
- PMID:17237235: in vitro Cu(I) binding by recombinant Cox19, a true biochemical
  property that is not enough to make Cox19 a copper metallochaperone.
- PMID:22984289: Bax-release IMS proteomics supporting IMS localization.

A 2024-2026 PubMed search found human COX19 papers and broader redox/copper
pathway studies but no newer yeast COX19 primary paper that changes these calls.

### Retained curation caveats

The SGD `GO:0030001 metal ion transport` row remains `MARK_AS_OVER_ANNOTATED`.
It was inferred from Cox19 resemblance to Cox17 in the original paper; later
mechanistic evidence instead supports Cox19 as a Cox11 chaperone, not as a
demonstrated metal transporter.
