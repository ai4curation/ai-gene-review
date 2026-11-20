# Manual CEK2 literature sweep

Falcon deep research was unavailable for this gene, so this file records the
manual replacement search and the cached papers used in the review.

## Direct pheromone-response and mating evidence

- **Chen et al. 2002, PMID:12075459** described CEK2 as a Candida MAPK with
  MAPK-like kinase activity: the abstract reports that the `CEK2` gene
  complemented a budding-yeast `fus3/kss1` mutant and that Cek2 phosphorylated
  MBP in vitro.
- **Chen et al. 2002, PMID:12453219** established the Cek1/Cek2 split in mating
  by showing that Cek2 supplies residual mating activity in `cek1` mutants and
  that a `cek1 cek2` double mutant was completely defective in mating.
- **Rastghalam et al. 2019, PMID:30787119** refined that model: Cek1 is the
  major pheromone-response MAPK, Cek2 has a weaker positive mating role, and
  loss of Cek2 increases pheromone-arrest halos, consistent with a role in
  adaptation to pheromone-mediated arrest.
- **Herrera-Lasheras et al. 2021, PMID:33793759** imaged pathway components and
  showed that Cek2-GFP is cytoplasmic before stimulation and nuclear after
  pheromone treatment; the same study showed that Cek2 and Cek2-GFP are
  phosphorylated after pheromone stimulation in a Ste11-dependent manner.
- **Xie et al. 2023, PMID:37045865** showed that the pheromone MAPK pathway also
  supports white-cell mating under glucose-depleted conditions and that
  elevating CEK2 is especially effective in that setting.

## Cell-wall evidence needing full-text follow-up

**Correia et al. 2016, PMID:26682470** is directly about Cek2 and cell-wall
biogenesis, but only the PubMed abstract is cached locally. The abstract says
CEK2 deletion makes cells sensitive to cell-wall-interfering drugs and that
Cek2 can be phosphorylated by Cek1-activating stimuli when overexpressed. This
is a strong prompt for full-text review but not enough, by itself, to add a new
`fungal-type cell wall biogenesis` row.

## PAINT interpretation

PTHR24055 is the eukaryotic MAPK family. The PAINT file propagates broad
MAPK-family activity and compartment terms from `PANTHER:PTN000622075`; those
transfers are biologically compatible with Candida Cek2 and include Cek2 itself
as target-specific descendant support. The more exact `GO:0071507 pheromone
response MAPK cascade` row is on `PANTHER:PTN001172087`, the fungal
Fus3/Spk1-like pheromone MAPK node, and should be retained for Cek2. The
Fus3-derived EnsemblFungi transfers for invasive growth, Ty1 silencing,
identical protein binding, mating-projection-tip localization, and Fus2 nuclear
export should not be transferred to Cek2.
