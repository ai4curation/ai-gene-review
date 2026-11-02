# osm-11 (C. elegans) curation notes

UniProt O45346 "Notch ligand osm-11". PANTHER (verbatim from UniProt): PTHR35015 (PROTEIN CBR-OSM-7-RELATED),
PTHR35015:SF1 (NOTCH LIGAND OSM-11). IBA rows are from PANTHER:PTN002169806 (the only donor is osm-11 itself,
WB:WBGene00003891): Notch binding (GO:0005112), extracellular region (GO:0005576), and positive regulation of
Notch signaling pathway (GO:0045747).

## Co-ligand function

- Secreted, diffusible, binds LIN-12 ECD [PMID:18700817 "OSM-11 is a secreted, diffusible protein that, like
  previously described C. elegans Delta, Serrate, and LAG-2 (DSL) ligands, can interact with the lineage
  defective-12 (LIN-12) Notch receptor extracellular domain."]
- Bipartite ligand model: C. elegans DSL ligands lack a DOS motif, so a DSL ligand plus a DOS protein may both be
  required [PMID:18700817 "DSL ligands such as LAG-2 lack a DOS motif; C. elegans DSL ligands, such as LAG-2, and
  DOS-motif proteins, such as OSM-11, may both be required to activate LIN-12 Notch receptor signaling in vivo."]
- Mammalian DLK1 substitutes for OSM-11 [PMID:18700817].
- Acts with LAG-2 on LIN-12 and GLP-1 in adult neurons (octanol avoidance, quiescence); secreted from seam
  cells into the pseudocoelom [PMID:21549604].

## Other

- Osmotic resistance and high glycerol in osm-11 mutants [PMID:16980399]. The Notch dependence of this
  phenotype is unclear. Osmosensitive gene expression is altered and is not enriched for Notch targets
  [PMID:20126308].

## Variant notes (for the module)

- This is a nematode-specific pathway variant: the DOS motif is split off from the DSL ligand into separate
  secreted co-ligands (OSM-11, OSM-7, DOS-1/2/3). Vertebrate DLK1/DLK2 and DNER-type DOS proteins are
  functional analogs, since DLK1 rescues osm-11.

## Deep research status

The first falcon run (`just deep-research-falcon worm osm-11 --fallback perplexity-lite`) timed out at 600 s. The
perplexity fallback is unavailable in this environment. A rerun with `--timeout 2400` succeeded:
`osm-11-deep-research-falcon.md`. It is consistent with the review and is cited in core_functions. Note that
falcon reports C. elegans LIN-12/GLP-1 are tuned to lower force thresholds for activation than Drosophila
Notch (Langridge et al. 2021 bioRxiv; not in the publications cache, so not used as evidence here).
