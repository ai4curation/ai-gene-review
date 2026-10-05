# CNE1 notes

## 2026-10-01 current GOA and IBA re-review

Forced a current GOA/UniProt refresh for the IBA campaign. Live QuickGO now has
14 rows for budding-yeast CNE1. The refreshed review keeps the four older rows
that no longer exactly match live GOA as explicit `retired: true` entries:

- `GO:0030246 carbohydrate binding` / `IEA` / `GO_REF:0000043`
- `GO:0051082 unfolded protein binding` / `IEA` / `GO_REF:0000002`
- `GO:0051082 unfolded protein binding` / `IDA` / `PMID:16002399`
- `GO:0051082 unfolded protein binding` / `IMP` / `PMID:15173200`

The current PAINT slice `interpro/panther/PTHR11073/PTHR11073-paint.tsv`
places all four CNE1 IBA rows on `PANTHER:PTN000117401`, the root
calreticulin/calnexin node. The yeast target appearing in the protein-folding,
ERAD quality-control, and ER-membrane descendant evidence is normal PAINT
semantics rather than circular support. Three of the four placements were
retained:

- `GO:0006457 protein folding`: accepted. Xu et al. directly showed that Cne1p
  suppresses citrate synthase thermal denaturation and enhances refolding
  [PMID:15173200, "Cne1p effectively suppressed the thermal denaturation of CS
  and enhanced the refolding of thermally or chemically denatured CS in a
  concentration-dependent manner"].
- `GO:0036503 ERAD quality control pathway`: accepted. Azakami et al. showed
  Cne1p binding to unstable glycosylated lysozyme clients and CNE1-dependent
  retention/elimination [PMID:25229868, "These results suggest that in yeasts,
  Cne1p interacts with misfolded lysozyme proteins possibly causing their
  retention in the ER and subsequent elimination via ER-associated
  degradation"].
- `GO:0005789 endoplasmic reticulum membrane`: accepted. Parlati et al. placed
  Cne1p in the ER by fractionation and confocal immunofluorescence
  [PMID:7814381, "Localization of the Cne1p protein by differential and
  analytical subcellular fractionation as well as by confocal
  immunofluorescence microscopy showed that it was exclusively located in the
  endoplasmic reticulum (ER)"].

The one bad IBA transfer remains `GO:0005509 calcium ion binding`. PTHR11073
still asserts calcium binding at `PANTHER:PTN000117401` from metazoan and
fission-yeast calreticulin/calnexin seeds, but direct budding-yeast Cne1p
characterization reported that "Ca2+ binding activity has not been detected for
Cne1p" [PMID:7814381]. The matching InterPro2GO calcium-binding row is still in
GOA and is removed for the same target-specific divergence.

The UniProt keyword `carbohydrate binding` row has disappeared from GOA, but the
underlying lectin biology is solid and is retained as a core
`GO:0070492 oligosaccharide binding` function plus the proposed
`monoglucosylated oligosaccharide binding` term. PMID:15173200 showed that G1M9
competes with recombinant Cne1p chaperone activity, and the FEBS Letters
follow-up directly tested P-domain and lectin-site mutants; its abstract reports
that "The binding of monoglucosylated oligosaccharide (G1M9) with Cne1p was
clearly demonstrated using lectin site mutants" [PMID:15251457].

The two generic `GO:0005515 protein binding` IPI rows to EPS1 and MPD1 remain
`REMOVE`: SGD's physical interactions are not disputed, but the cached abstract
only exposes the Mpd1p/Cne1p functional interaction [PMID:16002399, "Mpd1p
alone does not have chaperone activity but that it interacts with and inhibits
the chaperone activity of Cne1p"], and neither row should retain a generic
protein-binding molecular-function annotation.

I searched PubMed and the open web for exact CNE1/Cne1p/YAL058W hits from
2024-2026. The search surfaced no newer direct CNE1 paper that changes this
curation; recent broad *S. cerevisiae* engineering papers were not CNE1-specific.
