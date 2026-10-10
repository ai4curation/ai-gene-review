# thi4 (SPAC23H4.10c, UniProt P40386) notes

Fetch: `just fetch-gene SCHPO thi4` fetched the correct accession (THI6_SCHPO, P40386, 518 aa).

## Naming trap
- S. pombe **thi4** is the orthologue of S. cerevisiae **THI6** (bifunctional TMP synthase / HET kinase),
  NOT of S. cerevisiae THI4 (the thiazole synthase; that role is S. pombe thi2/nmt2, P40998).
  UniProt entry name is THI6_SCHPO [UniProt:P40386].

## Evidence
- Domain architecture: N-terminal TMP synthase (TenI/ThiE) + C-terminal Thz kinase (ThiM)
  [file:SCHPO/thi4/thi4-uniprot.txt "In the N-terminal section; belongs to the thiamine-"]
  [file:SCHPO/thi4/thi4-uniprot.txt "In the C-terminal section; belongs to the Thz kinase"].
- Function asserted by similarity (ECO:0000250) in UniProt: condenses THZ-P and HMP-PP to TMP.
- Genetics: [PMID:7961415 "thi4 mutants of Schizosaccharomyces pombe exhibit defective thiamine
  biosynthesis"]; the gene was cloned by complementation; the abstract describes the enzymatic role as
  believed, not demonstrated ("believed to be involved in the phosphorylation of ... and/or in the coupling").
- Regulation: [PMID:7961415 "The appearance of thi4 mRNA is strongly repressed by thiamine"], controlled by thi1
  and the tnr1/tnr2/tnr3 negative regulators.
- Location: cytoplasm/cytosol in the ORFeome screen (PMID:16823372, HDA).
- No direct S. pombe enzyme assay is cached; MF evidence is ISO from S. cerevisiae THI6
  (PMID:7982968 in genes/yeast/THI6), IBA and IEA.

## GO-CAM
- PomBase gomodel:66c7d41500000963: thi4 enables GO:0004789 (IBA) and GO:0004417 (ISO from SGD THI6), both in
  cytosol, part_of GO:0009228. Consistent with this review.

## Decisions
- Core MF GO:0004789 (TMP synthase) and GO:0004417 (HET kinase), BP GO:0009228, location cytosol. Consistent with
  genes/yeast/THI6 core functions.
- Mg2+ and ATP binding: KEEP_AS_NON_CORE (cofactor/substrate binding, as for THI6).
- GO:0009229 (UniPathway) ACCEPT as in THI6 review.
