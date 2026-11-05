# O2 review notes

## Session 2026-10-28

- Task named B4FHZ3 (TrEMBL). `just fetch-gene MAIZE O2` resolved the Swiss-Prot
  entry P12959 instead, with GOA keyed to P12959 (7 rows). Confirmed same gene:
  NCBI Gene 542375 (the GeneID on B4FHZ3) lists P12959 and B4FHZ3 as products of
  the same locus (o2, GRMZM2G015534/Zm00001d018971). Reviewed P12959.
  B4FHZ3 keeps its own 10 GOA rows; the three EnsemblPlants rows unique to it
  (GO:0043565, GO:0045893, GO:0010581) are covered here by MODIFY targets and one
  NEW row.
- Key paper PMID:22937104 (full text read): ZmTaxilin binds O2 and retains it
  outside the nucleus; YFP-O2 activates the 22-kD zein z1C promoter 3-4 fold in
  onion cells [PMID:22937104 "YFP-O2 is able to induce transcription of the z1C
  promoter by 3–4 fold relative to the negative controls"].
- Other papers abstract only: PMID:1392590 (binding site + yeast activation),
  PMID:2001677 (b-32 and own promoter), PMID:1899843 (o2-676 R->K loses
  binding), PMID:8453304 (OHP1), PMID:9207153 (PBF), PMID:1332794 (NLS),
  PMID:25691733 (ChIP-seq), PMID:27621432 (starch genes).

## Decisions

- GO:0003700 (IBA, IEA) -> MODIFY to GO:0001216 DNA-binding transcription
  activator activity (is_a GO:0003700, checked with OAK). Activation is shown
  in yeast, maize and onion cells.
- GO:0006355 (IBA, IEA) -> MODIFY to GO:0045893 (is_a GO:0006355, OAK).
- GO:0000976 (IBA) -> MODIFY to GO:0000987 cis-regulatory region
  sequence-specific DNA binding (is_a GO:0000976, OAK); footprinted site,
  consensus motifs, single-residue loss of specificity.
- GO:0005634 nucleus (IBA, IEA) -> ACCEPT; NLS mapping and nuclear GUS fusions
  [PMID:1332794].
- NEW GO:0010581 regulation of starch biosynthetic process: O2 itself does the
  work (direct promoter transactivation of PPDK1/2 and SSIII), not just
  necessity evidence. Comparator: EnsemblPlants already projects this term to
  B4FHZ3, and PBF is the co-regulator. Kept non-core relative to zein control.
- Did not add a zein/storage-protein process term: no GO term for seed storage
  protein gene expression exists, and expression/phenotype alone is not
  enough for a NEW process term beyond GO:0045893.
- No protein-binding terms added for PBF/OHP1/Taxilin.
