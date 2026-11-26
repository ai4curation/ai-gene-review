# ubiH review notes (E. coli K-12, P25534)

Reviewed for the ubiquinone_biosynthesis module (UbiH 2-octaprenyl-6-methoxyphenol
hydroxylase annoton).

## Provenance

- No deep-research provider was available (no API keys); no
  `-deep-research-<provider>.md` file exists or was fabricated. Built from the
  reviewed UniProt record, cached abstracts and the PTHR43876 PAINT table.

## Which hydroxylation

- UbiH is the C1 hydroxylase: 2-octaprenyl-6-methoxyphenol to
  2-octaprenyl-6-methoxy-1,4-benzoquinol (GO:0008681). [file:ECOLI/ubiH/ubiH-uniprot.txt
  "Is likely an oxygenase that introduces the hydroxyl group at carbon four of
  2-octaprenyl-6-methoxyphenol resulting in the formation of
  2-octaprenyl-6-methoxy-1,4-benzoquinol."] ("carbon four" is the phenol
  numbering of the position that becomes C1 of the quinone.)
- ubiH mutants accumulate phenolic precursors. [PMID:4572721 "The mutants
  accumulate small quantities of 2-octaprenyl-6-methoxyphenol, which was
  isolated and characterized by nuclear magnetic resonance and mass
  spectrometry, and relatively large amounts of 2-octaprenylphenol"]
- Light sensitivity is a consequence of accumulated substrate. [PMID:1339425
  "The photosensitive phenotype appears to be due to the accumulation of the
  substrate for the reaction catalyzed by the visB (ubiH) gene product"]

## Decisions

- Oxidative stress and light response rows (EcoliWiki IMP): MARK_AS_OVER_ANNOTATED.
- Generic oxygenase and flavin terms: MODIFY to GO:0008681 / GO:0071949.
- No purified-enzyme assay exists for UbiH; the activity rests on genetics,
  family signatures and the PAINT node seeded by UbiH.
