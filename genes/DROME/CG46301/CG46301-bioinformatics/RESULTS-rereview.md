# CG46301 re-review: gene products and NOL4-family placement (2026-10-20)

Script: `compare_isoforms_rereview.py` (Biopython local alignment, BLOSUM62, gap -11/-1).
Raw output: `RESULTS-rereview-output.txt`. Inputs: UniProt FASTA files in this folder,
downloaded 2026-10-20.

## Gene products

UniProt holds four unreviewed entries for FlyBase FBgn0283651 (CG46301), and no reviewed
(Swiss-Prot) entry:

| Accession | Length | Maps onto A0A1W5PXH3 | Contains HTH_NOL4 (789-886) |
|---|---|---|---|
| A0A1W5PXH3 | 1237 | 1-1237 (itself) | yes |
| A0A1W5Q009 | 636 | 615-1237 (100% identity over 623 aa) | yes (UniProt FT DOMAIN 188..285) |
| A0A1W5PVN5 | 667 | 1-614 (100% identity over 614 aa) | no |
| A0A1W5PW03 | 623 | 1-614 (100% identity over 614 aa) | no |

A0A1W5PXH3 is the longest product and joins the N-terminal region (1-614) of the
CG17341-named products to the C-terminal region (615-1237) of the CG16879-named products,
consistent with the merged gene model carrying both former CG numbers as synonyms. It is
the accession PANTHER 19.0 lists for FBgn0283651 (PTHR12449:SF22). It is therefore the
most complete product, not a fragment; the shorter entries are alternative products of the
same gene.

## Relationship to vertebrate NOL4 and NOL4L

| Comparison | Aligned region | Identity |
|---|---|---|
| A0A1W5PXH3 789-886 vs human NOL4 (O94818) | -> 406-500 | 80.0% over 95 |
| A0A1W5PXH3 789-886 vs human NOL4L (Q96MY1) | -> 185-279 | 82.1% over 95 |
| A0A1W5PXH3 full vs human NOL4 (O94818) | 73-924 -> 3-538 | 44.2% over 523 aligned |
| A0A1W5PXH3 full vs human NOL4L (Q96MY1) | 696-895 -> 98-289 | 51.3% over 191 |

The helical domain is equally similar to NOL4 and NOL4L, so it does not discriminate
between them. PANTHER places the fly protein in its own subfamily (SF22), separate from
vertebrate NOL4 (SF17: human O94818, mouse P60954) and NOL4L (SF19: human Q96MY1, mouse
Q6DIB4); no other fruit-fly or nematode PTHR12449 member is listed in the PANTHER 19.0
classification files. This is consistent with a single invertebrate gene that is
co-orthologous to both vertebrate paralogs, but this analysis builds no tree, so that
remains an inference.

These numbers come from pairwise alignment only. They do not test any molecular activity.
