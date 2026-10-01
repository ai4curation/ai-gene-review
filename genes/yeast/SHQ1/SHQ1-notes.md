# SHQ1 notes

## 2026-09-29 IBA re-review

SHQ1 has four IBA annotations, all propagated through `PANTHER:PTN000311574` in
the `PTHR12967` SHQ1 homolog family. The current cached PAINT export for
`PTHR12967` still places `GO:0005654 nucleoplasm`, `GO:0005737 cytoplasm`, and
`GO:0000493 box H/ACA snoRNP assembly` on `PTN000311574`; yeast SHQ1
(`P40486`), human SHQ1 (`Q6PI26`), and the other representative eukaryotic SHQ1
proteins in the local entries table all sit in the single `PTHR12967:SF0`
subfamily. I added explicit `propagation_review` blocks treating the nucleoplasm
and box H/ACA snoRNP assembly IBAs as core transfers and the cytoplasm IBA as a
defensible but secondary localization transfer.

The fourth IBA, `GO:0051082 unfolded protein binding`, is still present in the
local GOA file as a 2017 row from `PTN000311574`, but the current
`PTHR12967-paint.tsv` cache no longer lists the molecular-function assertion.
The existing MODIFY call remains right biologically: the source biology is
Cbf5/dyskerin carrier-chaperone activity, not a generic unfolded-protein-binding
claim. I added `TERM_SCOPING_PROBLEM` / `GRANULARITY_MISMATCH` propagation
metadata and marked the ancestral node source as `SOURCE_STALE_OR_MISSING`
because the exact MF assertion cannot be recovered from the current cached PAINT
table.

The cached experimental papers support the existing action set. Yang et al.
identified `Yil104c/Shq1p` as essential for stable box H/ACA snoRNP accumulation
and pre-rRNA processing, and reported that Shq1p is nuclear and interacts with
Cbf5p and Nhp2p [PMID:12228251]. Godin et al. showed that Shq1p binds the
pseudouridylating enzyme Cbf5p and has stand-alone in vitro chaperone activity,
supporting the MODIFY of unfolded protein binding to `GO:0140597 protein
carrier chaperone` [PMID:19426738]. The oxygen-regulation localization paper
lists YIL104C/SHQ1 among nuclear proteins that relocalize to the cytosol during
hypoxia and return to the nucleus after reoxygenation, so the cytosol/cytoplasm
rows should be retained as non-core/contextual rather than removed
[PMID:22932476].

## Newer-literature search

I searched for 2023-2026 SHQ1/yeast literature. Most newer SHQ1 papers are human
neurodevelopmental-disease or cancer reports that do not change the yeast GO
review. The relevant newer experimental paper is Alidou-D'Anjou et al. 2023,
which expressed human SHQ1 R335C and A426V variants in a conditional yeast
SHQ1-depletion strain and showed weakened Cbf5 interaction, loss of H/ACA
snoRNAs, pre-rRNA processing defects, and reduced ribosome production
[PMID:37818102]. This reinforces the conserved SHQ1-Cbf5 carrier-chaperone
model but does not require a new GO term for the yeast protein.

## 2026-10-01 current-GOA refresh

- Refreshed UniProt/GOA for SHQ1. The live GOA snapshot has 13 rows and no longer
  carries either `GO:0051082 unfolded protein binding` source assertion; both historical
  rows were preserved as retired and still point to the more specific
  `GO:0140597 protein carrier chaperone`.
- Reviewed three live rows backfilled from current GOA: two additional PMID:12228251 IPI
  rows for `GO:0000493 box H/ACA snoRNP assembly` through H/ACA assembly interactors were
  accepted, and the generic `GO:0005515 protein binding` row for the same paper/with-from
  set was removed as an uninformative interaction placeholder.
- Downgraded the pre-existing `GO:0000493` IPI row with `SGD:S000002569` to
  `UNDECIDED`: the cached Yang et al. abstract does not expose the NBP2-linked
  full-text evidence behind that row, so it should be revisited from the full paper
  before making a stronger call.
- Re-read the current `PTHR12967` PAINT cache: `PTN000311574` still carries nucleoplasm,
  cytoplasm, and box H/ACA snoRNP assembly for the SHQ1 homolog family, but not the
  obsolete unfolded-protein-binding assertion. Newer literature searches found no
  yeast SHQ1 paper after the cached 2023 human-SHQ1 complementation study that would
  change the GO calls.
