# dpm-1 (U4PF58) notes

## 2026-10-20 full re-review

### Identity of the benchmark accession

- U4PF58 is the 51-aa product of WormBase gene model **Y66H1A.2b** (UniProt GN line cites
  `WormBase:Y66H1A.2b`). The canonical full-length dpm-1 product is **Q9TYJ7** (Y66H1A.2a, 239 aa).
- Reproducible alignment (`dpm-1-bioinformatics/RESULTS.md`, now built only from UniProt downloads,
  no prediction files): U4PF58 = Q9TYJ7 residues 189-239, 51/51 identical.
- The UniProt glycosyltransferase 2-like domain of Q9TYJ7 (residues 8-176) is entirely absent
  (0/169 mapped). The DXD-type motif (Q9TYJ7 position 96; human DPM1 position 118) is absent.
- So U4PF58 is an alternative gene model / C-terminal fragment-like isoform, not a catalytically
  competent enzyme. Whether Y66H1A.2b is translated is untested; PeptideAtlas PE 1 is a gene-level
  peptide flag and its peptides may all derive from the shared C-terminal region, so it does not
  establish that the short product exists.

### Evolutionary placement

- UniProt places U4PF58 (and thus the dpm-1 locus) in PANTHER PTHR43398:SF1 (DPM1). Human DPM1
  (O60762), S. cerevisiae DPM1 (P14020) and S. pombe dpm1 (O14466) are all in PTHR43398:SF1
  (`interpro/panther/PTHR43398/PTHR43398-entries.csv`).
- PAINT: GO:0004582 placed at PTN002459128 with seeds including human O60762, mouse Dpm1, yeast
  SGD:S000006387; GO:0005789 (ER membrane) at PTN000092441 (taxon 2759); GO:0006488 (dolichol-linked
  oligosaccharide biosynthesis) at PTN000092440. Worm full-length DPM-1 is inside these clades.
- Full-length worm DPM-1 vs human DPM1: 64.7% identity over 238 aligned columns. Worm DPM-1, like
  human/S. pombe DPM1, lacks the C-terminal TM anchor of the S. cerevisiae single-subunit enzyme
  (family review / InterPro description), so the closest characterised relative by architecture and
  phylogeny is human DPM1 (animal three-subunit type).
- The fragment region (worm 189-239) maps to human DPM1 211-260 with 33 identical residues.

### Literature

- [PMID:10835346 "mammalian DPM synthase contains catalytic DPM1 and regulatory DPM2 subunits"].
  The abstract states DPM3 associates with DPM1 "via its C-terminal domain" - this refers to DPM3's
  C-terminal domain, not a mapped DPM1 region, so it cannot be used to argue that the DPM1 C-terminal
  tail (the U4PF58 region) is a DPM3-binding module.
- Falcon deep research (`dpm-1-deep-research-falcon.md`) treats U4PF58 as if it were full-length
  DPM1 and does not notice the truncation; it found no worm-specific experimental work. Its general
  DPM1 biochemistry applies to Q9TYJ7, not to U4PF58.

### Decisions

- GO:0004582 IEA (InterPro2GO): REMOVE for this product (no catalytic domain). The activity should be
  carried by Q9TYJ7.
- No core functions: none can be assigned to the isolated 51-aa product.
- PANTHER family review (`interpro/panther/PTHR43398/PTHR43398-review.yaml`): no disagreement about
  subfamily placement (SF1). Its only listed representative member for SF1 is the fragment U4PF58;
  a full-length member (Q9TYJ7 or O60762) would be a better representative. Not edited here (outside
  this gene folder).
- Previous review/notes cited a ProtNLM source file; those references and the script dependency on
  it were removed so the review is independent of predictions.
