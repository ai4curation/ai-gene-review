# PA4596 (Q9HVJ0) start-site check

Script: `start_site_check.py` (standard library only; run with `python3 start_site_check.py`).
Run on 2026-11-05. It fetches the PAO1 region upstream of PA4596 from NCBI
(NC_002516.2), translates the annotated frame upstream of the annotated start
codon, and summarises the lengths of UniRef50_Q9HVJ0 members from UniProt.

## Raw output

```
Annotated ORF translation (172 aa): MVNHPRATMGELAELAGVSRATLNRHCGTREGLKRRLESHARSTLERLTH...
Upstream in-frame codons: 100; last in-frame stop at codon index 6 (i.e. 93 sense codons before the annotated start)
Open upstream extension translation: ARRRPSPRARSGWAWHCSRPWCCRSRPDAKQGVGRSSLLQLIQISLKRTKKTSKMTLAPRSAQLPDSPHRDSLDPAPTPSSQDQRLLKALATA
  candidate start GTG giving +61 aa N-terminal extension
  candidate start TTG giving +53 aa N-terminal extension
  candidate start ATG giving +39 aa N-terminal extension
UniRef50_Q9HVJ0 members retrieved: 73; median length 186; members >= 180 aa: 70; members <= 175 aa: 3
Most common lengths: [(185, 20), (188, 11), (186, 10), (183, 10), (187, 7), (184, 3), (172, 2), (198, 2)]
```

## Interpretation

- The annotated 172-aa protein begins MVNHPRATMGELAELAGVSRATLNRHCG. In TetR-family
  regulators the HTH domain (Pfam PF00440, InterPro IPR001647) starts with helix 1
  ahead of the GVS..TLY.HF motif. Q9HVJ0 has no PF00440 or IPR001647 match in its
  UniProt record, only the Homeodomain-like superfamily and the TetR C-terminal
  domain signatures, consistent with a missing helix 1.
- The reading frame stays open for 93 codons upstream of the annotated start. The
  residues directly upstream (SQDQRLLKALATA) look like TetR helix 1. There are
  in-frame ATG (+39 aa), TTG (+53 aa) and GTG (+61 aa) codons upstream.
- 70 of 73 UniRef50_Q9HVJ0 members are 180 aa or longer (median 186 aa); Q9HVJ0
  is one of 3 at 175 aa or shorter.
- Conclusion: the annotated start codon probably truncates the N-terminus of the
  HTH domain (status SUSPECTED; no transcript or N-terminal proteomic data were
  checked). The exact true start cannot be determined from this analysis. This
  does not affect the GO review, since the purified protein bound the
  mexCD-oprJ promoter (PMID:25143244), but the recombinant construct used in that
  paper was not checked.
