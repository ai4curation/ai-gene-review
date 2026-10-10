# SPH1 notes

## 2026-10-10 Initial review (PTHR21601 family pass with SPA2 and S. pombe spa2)

Identity: Q06160, YLR313C, "Spa2 homolog". Same PANTHER subfamily as SPA2 (PTHR21601:SF0).
It has one Pfam GIT_SHD (Spa2 homology domain) and the Spa2-box localization domain.

### Localization
- [PMID:9214378 "These experiments demonstrate that Sph1p also localizes to sites of polarized
  growth: at the site where the bud will form, the bud tip, and the mother–daughter bud neck."]
- [PMID:9443897 "Sph1p concentrates as a cortical patch at the presumptive bud site in unbudded
  cells, at the tip of small, medium and large buds, and at the bud neck prior to cytokinesis."]
- Shmoo tip: [PMID:9443897 "In pheromone-treated cells, Sph1p localizes to the tip of the
  mating projection."]
- The two papers disagree on whether Sph1 localization needs Spa2:
  [PMID:9443897 "Proper localization of Sph1p to sites of active growth during budding and mating
  requires Spa2p."] vs. PMID:9214378, where Sph1-GFP localized in spa2 deletion cells (full text).
  Recorded as a suggested question.
- Hub1 conjugate; Sph1 localization is disrupted in hub1 deletion cells [PMID:11923536 "In the
  hub1Delta mutant, the subcellular localization of both Hbt1 and Sph1 was disrupted"].
- The "cytoskeleton" location (UniProt SubCell, no evidence tag) has no Sph1 data behind it, so
  it is marked over-annotated.

### Phenotypes
- Bipolar budding: [PMID:9214378 "Together these results demonstrate that SPH1 is required for
  bipolar budding after the positioning of the first bud and, together with shmoo formation and
  mating experiments, show that SPH1 and SPA2 have overlapping functions."]
- Shmoo formation is reduced (about halfway between wild type and spa2); there is no detectable
  quantitative mating defect (PMID:9214378 full text). SPA2-GFP rescues sph1, but SPH1-GFP does
  not rescue spa2.
- Pseudohyphal growth (single mutant) and haploid invasive growth (sph1 spa2 double mutant)
  [PMID:9443897].
- No NEW GO:0000753 (conjugation morphogenesis) was added. SGD annotated bipolar budding from
  this paper but not shmoo morphogenesis, and the mating defect is mild, so this is a curator
  choice we do not override.

### MAPK
- [PMID:9443897 "Sph1p interacts in the two-hybrid system with three mitogen-activated protein
  (MAP) kinase kinases (MAPKKs): Mkk1p and Mkk2p ... and Ste7p"]. Ste11 interacts weakly, and
  the interactions are Ste5-independent. The only role proposed is speculative tethering.
- The GO:0005078 IBA was accepted: Sph1 has the SHD1 module and target-specific binding to
  several kinases of the module. Its core function is recorded with an explicit
  two-hybrid-only caveat.

### PAINT
- PTN001091461 (Saccharomycetales): incipient bud site, bud tip, bud neck, bipolar budding,
  pseudohyphal growth and invasive growth all fit Sph1, which is a seed for each.
- PTN004550576 (Eukaryota root): mating projection tip is correct for Sph1; MAPK scaffold is
  plausible for Sph1; GO:0120105 contractile ring intermediate layer (PomBase-only seed) is
  wrong for Sph1 and was removed. GOA still cites PTN001091459 for that row.

## Addendum: falcon deep research (arrived after the review was written)

`SPH1-deep-research-falcon.md` landed after the annotation review was finished and was cross-checked
against it. It agrees with the review: Sph1 is a polarized-growth regulatory protein of the polarisome
that contributes to Slt2/Mpk1 activation (reduced dually phosphorylated Slt2 in sph1 ptc1 cells) and
to bud and mating-projection morphogenesis, without being required for Slt2 or Mkk1 localization. It
is cited on the GO:0005078 IBA row. No annotation decision changes.
