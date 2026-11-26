# ispB review notes (E. coli K-12, P0AD57)

Reviewed for the ubiquinone_biosynthesis module (optional polyprenyl tail
synthesis part, IspB-type homomeric octaprenyl diphosphate synthase).

## Provenance

- No deep-research provider was available (no API keys); no
  `-deep-research-<provider>.md` file exists or was fabricated. Built from the
  reviewed UniProt record, cached abstracts and the PTHR12001 PAINT table.

## Function

- IspB makes all-trans-octaprenyl diphosphate. [PMID:11825609 "Octaprenyl
  pyrophosphate synthase (OPPs) catalyzes the sequential condensation of five
  molecules of isopentenyl pyrophosphate with farnesyl pyrophosphate to
  generate all-trans C40-octaprenyl pyrophosphate, which constitutes the side
  chain of ubiquinone."]
- Chain length depends on residues and the dimer. [PMID:11108713 "this dimer
  formation is important for the determination of the isoprenoid chain
  length."]

## Decisions

- Prenyltransferase activity (IBA, IDA, IEA): MODIFY to GO:0106350.
- Heterologous Dlp1/Dps1 protein-binding rows removed; identical protein
  binding MODIFY to homodimerization, which is kept as non-core.
- Isoprenoid and polyprenol biosynthetic process accepted (pathway-level, true).
