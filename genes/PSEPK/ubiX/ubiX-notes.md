# ubiX (PP_0548, Q88QE6) - Pseudomonas putida KT2440 - curation notes

## 2026-11-11 audit (ubiquinone_biosynthesis module)

No Perplexity/Falcon/OpenAI deep research available (no provider keys); the OpenScientist
report was read. Evidence: unreviewed UniProt entry with HAMAP MF_01984 text, and E. coli UbiX
literature. No KT2440 experiment.

- Activity: [PMID:26083743 "UbiX acts as a flavin prenyltransferase, linking a dimethylallyl
  moiety to the flavin N5 and C6 atoms."]; [PMID:26083743 "In contrast to other
  prenyltransferases, UbiX is metal-independent and requires dimethylallyl-monophosphate as
  substrate."]
- Not a decarboxylase: [PMID:26083743 "Despite structural and biochemical characterization of
  UbiX as a flavin mononucleotide (FMN)-binding protein, no decarboxylase activity has been
  detected."] -> TreeGrafter GO:0016831 REMOVE. Current PTHR43374 paint.tsv has no
  carboxy-lyase IBD (only GO:0106141 and GO:0006744 at PTN000764671), so the TreeGrafter
  row appears stale.
- Pathway role: [PMID:17889824 "LLI produces very low levels of Q, grows slowly on succinate
  as the sole carbon source, accumulates 4-hydroxy-3-octaprenyl-benzoate"]. Added NEW
  GO:0006744 (ISS) on the cofactor-supply participation argument; comparator E. coli UbiX
  P0AG03 is the PAINT seed for GO:0006744 at PTN000764671. Missing in GOA only because
  KT2440 has no IBA rows.
- UniProt catalytic activity evidence includes ARBA alongside HAMAP; quoted only the
  HAMAP-backed FUNCTION text.

Module agreement: `flavin_prenyltransferase_activity` (GO:0106141), modeled as cofactor
supply for UbiD. Consistent.
