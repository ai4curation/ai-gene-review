# lag-2 (C. elegans) curation notes

UniProt P45442 "Protein lag-2". PANTHER (verbatim from UniProt): PTHR22669 (DELTA/SERRATE/LAG-2 DOMAIN
PROTEIN), PTHR22669:SF8 (PROTEIN LAG-2). IBA rows: PANTHER:PTN000505678 for Notch binding (GO:0005112),
cell projection membrane (GO:0031253) and cell fate specification (GO:0001708). Donors are lag-2 itself
(WB:WBGene00002246) plus WB:WBGene00001103 for Notch binding.

## Ligand function

- Delta-like membrane protein expressed in the DTC [PMID:7607081 "lag-2 encodes a putative membrane protein
  with sequence similarity to Drosophila Delta, a proposed ligand for the Notch receptor"].
- Required for both LIN-12 and GLP-1 signaling [PMID:1769331].
- ECD binds LIN-12 EGF repeats 1-6 (Y2H) [PMID:18700817].
- The N-terminal region and DSL domain are required; the EGF repeats are dispensable; the intracellular
  region down-regulates activity [PMID:9307971].
- APX-1 substitutes for LAG-2; truncated secreted ECDs activate LIN-12/GLP-1 ectopically [PMID:8575327].

## Variant biology

- Lacks a DOS motif. The DOS motif is proposed to be supplied in trans by OSM-11-family co-ligands
  [PMID:18700817 "DSL ligands such as LAG-2 lack a DOS motif; C. elegans DSL ligands, such as LAG-2, and
  DOS-motif proteins, such as OSM-11, may both be required to activate LIN-12 Notch receptor signaling in
  vivo."]
- Germline stem-cell niche: LAG-2 on DTC processes [PMID:16672375].
- AC/VU decision: feedback restricts lag-2 transcription to the presumptive AC (HLH-2 directly activates
  lag-2) [PMID:14701877].

## Flags

- GO:0032809 neuronal cell body membrane (IDA, PMID:16672375 and PMID:8575327): the cells assayed (DTC and
  gonadal cells) are not neurons, so I MODIFY this to plasma membrane.

## Deep research status

The first falcon run (`just deep-research-falcon worm lag-2 --fallback perplexity-lite`) timed out at 600 s. The
perplexity fallback is unavailable in this environment. A rerun with `--timeout 2400` succeeded:
`lag-2-deep-research-falcon.md`. It is consistent with the review and is cited in core_functions. Note that
falcon reports C. elegans LIN-12/GLP-1 are tuned to lower force thresholds for activation than Drosophila
Notch (Langridge et al. 2021 bioRxiv; not in the publications cache, so not used as evidence here).

Falcon also reports two points not verified against cached primary papers. (1) A soluble LAG-2 ectodomain
did not rescue lag-2 null lethality, whereas GPI tethering partly did (Post et al. 2025). This appears to be in
tension with PMID:8575327, where truncated secreted DSL forms substituted for lag-2. (2) The adhesion GPCR LAT-1
binds LAG-2 in cis on the DTC and enhances GLP-1 activation.
