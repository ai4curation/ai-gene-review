# tusA (E. coli K-12) curation notes

## Sources checked

- UniProtKB record (genes/ECOLI/tusA/tusA-uniprot.txt) and GOA table.
- Cached publications: PMID:16387657, PMID:10830496, PMID:23281480 (abstract-only);
  PMID:20404999, PMID:38916309, PMID:24561554 (full text).
- No provider deep-research file was generated for this gene.

## Findings

- Core role: IscS-to-TusD sulfur carrier in the mnm5s2U relay
  [PMID:16387657 "IscS transfers the persulfide sulfur to TusA."]; TusA also
  stimulates IscS [PMID:16387657 "The desulfurase activity of IscS is stimulated
  by TusA binding."]. The IscS-TusA complex has been crystallized
  [PMID:20404999 "we have determined the crystal structure of the IscS-TusA and
  the IscS-IscU complexes"].
- Moco: TusA affects but is not required for molybdenum cofactor synthesis
  [PMID:23281480 "showing that TusA is not essential for molybdenum cofactor
  biosynthesis"]; kept as non-core.
- Fe-S: the tusA Fe-S phenotype is attributed to reduced fur translation
  [PMID:38916309 "We show that the absence of TusA reduces the translation of
  fur, thereby leading to pleiotropic cellular effects"]; marked over-annotated
  as an indirect effect.
- Bare protein-binding IPI rows (all with IscS) are removed per the
  protein-binding policy; the interaction is kept as GO:1990329.
