# GSTF11 pairwise identity to the Kiyosue et al. 1993 GSTs (ERD11, ERD13)

## Question

Richards et al. 1998 (PMID:9449849) identified an aluminium-induced "GST" cDNA only by
">98% identity" to the GST sequence of Kiyosue et al. 1993 (PMID:8253194). Kiyosue et al.
described two dehydration-inducible phi GST cDNAs, ERD11 and ERD13. Can that clone be
GSTF11 (At3g03190)?

UniProt maps the two Kiyosue clones as follows:

- ERD11 = GSTF6 (P42760, At1g02930): `GSTF6-uniprot.txt` lists `Synonyms=ERD11, GST1, GSTF3`.
- ERD13 = GSTF10 (P42761, At2g30870): `P42761-GSTF10-ERD13-uniprot.txt` (downloaded
  2026-10-15 from https://rest.uniprot.org/uniprotkb/P42761.txt, entry version 185) lists
  `Synonyms=ERD13`.

## Method

`pairwise_identity.py` reads the three UniProt flat files and runs a Needleman-Wunsch
global alignment (Biopython 1.85 `PairwiseAligner`, BLOSUM62, gap open -10, gap extend
-0.5, end gaps free; EMBOSS needle defaults). Run with:

```
uv run python pairwise_identity.py > output.txt   # biopython is a root project dependency; run from this folder
```

## Output (verbatim, `output.txt`, run 2026-10-15)

```
GSTF11	Q96324	length=214	GN=GSTF11
GSTF6_ERD11	P42760	length=208	GN=GSTF6
GSTF10_ERD13	P42761	length=215	GN=GSTF10

pair	identical	aln_length	identity_over_alignment	identity_over_shorter
GSTF11 vs GSTF6_ERD11	86	217	39.6%	41.3%
GSTF11 vs GSTF10_ERD13	93	218	42.7%	43.5%
GSTF6_ERD11 vs GSTF10_ERD13	81	218	37.2%	38.9%
```

## Interpretation

GSTF11 is about 40% identical to ERD11/GSTF6 (39.6% over the alignment) and about 43%
identical to ERD13/GSTF10 (42.7% over the alignment). Neither is compatible with a
cDNA that is >98% identical to a Kiyosue clone. Richards et al. 1998 cite the Kiyosue
"GST" in the singular without saying whether it is ERD11 or ERD13, but either way the
Al-induced clone corresponds to GSTF6 or GSTF10, not to GSTF11.

Caveat: Richards et al. compared a 5' single-pass read at the nucleotide level, whereas
this analysis compares full-length proteins. A nucleotide region >98% identical to
GSTF6 or GSTF10 would encode protein nearly identical to that gene, so the conclusion
is unaffected.
