# PP_5105 (Q88CS5, ThiS) notes

Session 2026-11-12. Deep-research providers were not available in this session, so there is
no `PP_5105-deep-research-*.md` file. Sources were the cached UniProt record, cached
publications, the PSEPK thiamine pathway report
(`projects/P_PUTIDA/deep-research/PSEPK__thiamine_diphosphate_biosynthesis__ppu00730-deep-research-openscientist.md`),
QuickGO and the ortholog analysis in `PP_5105-bioinformatics/`.

## Identity
- TrEMBL Q88CS5, 92 aa, PE 4, no gene name; the stub gene_symbol is the accession. The name
  "Sulfur carrier protein ThiS" is a submitter annotation (ECO:0000313), so it is not evidence.
- Family evidence: InterPro IPR010035 Thi_S, IPR003749 ThiS/MoaD-like, NCBIfam TIGR01683 thiS,
  Pfam PF02597, CDD cd00565 Ubl_ThiS, PANTHER PTHR34472:SF1 [file:PSEPK/PP_5105/PP_5105-uniprot.txt "InterPro; IPR010035; Thi_S."].
- Ends in Gly-Gly [file:PSEPK/PP_5105/PP_5105-bioinformatics/RESULTS.md "Q88CS5 is 92 aa and ends in the C-terminal Gly-Gly that ThiS-family carriers thiocarboxylate"].
- Locus neighbourhood: thiG is PP_5104 (AAN70669.1) and this gene is PP_5105 (AAN70670.1), with consecutive locus tags and protein ids
  in AE015451. Strand and operon structure were not checked; adjacency only.

## Gene model
- 301 Pseudomonas ThiS entries (66 aa) start at the position of Q88CS5 Met27, and 38 entries (71 aa) at Met22.
  Only one other entry has the 1-21 extension. Recorded as a SUSPECTED WRONG_START_SITE.

## Ortholog biochemistry (E. coli, abstracts only)
- ThiS thiocarboxylate is the immediate S donor [PMID:9632726 "Identification of ThiS thiocarboxylate as the immediate sulfur donor in the thiazole formation."].
- ThiF adenylates ThiS, and ThiF-ThiS acyldisulfide is an intermediate [PMID:11438688], [PMID:16388576].
- Reconstituted thiazole synthase requires ThiS-COSH [PMID:17403671 "was the use of ThiS in the thiocarboxylate form."].

## KT2440 open issue
- No thiF gene. The pathway report names MoeB/PP_0735 as the only plausible E1-like substitute; this is unconfirmed.
  The PTHR34472 IBD GO:1902503 adenylyltransferase complex (ThiF-ThiS) therefore cannot be assumed for KT2440.

## Decisions
- No GOA rows. NEW: GO:0097163 sulfur carrier activity and GO:0052837 thiazole biosynthetic process, matching the PAINT IBDs at
  PTN002157649 and E. coli IDA (O32583, QuickGO 2026-11-12). The adenylyltransferase complex was not proposed.
