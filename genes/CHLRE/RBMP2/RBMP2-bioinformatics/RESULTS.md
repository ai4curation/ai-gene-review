# RBMP2 (A0A2K3DG19) sequence checks

Script: `analyze_sequence.py` (standard library only; `python3 analyze_sequence.py`).
Raw output: `analysis_output.txt`. Input: `../RBMP2-uniprot.txt` (1690 aa).

## 1. Rhodanese domain has no cysteine

- The whole 1690-residue protein has a single cysteine, Cys498, which lies in the
  Pro/Ala-rich low-complexity N-terminal half, far outside the rhodanese domain.
- The PROSITE PS50206 rhodanese domain (775-920) contains no cysteine at all.
- Active rhodanese domains (thiosulfate sulfurtransferases, CDC25 phosphatases) depend on
  a catalytic cysteine at the start of the active-site loop. A crude `[C/D]xxGxx` scan
  finds one candidate loop in the domain, `D870-SYGVE`, i.e. an aspartate where the
  cysteine would sit. This agrees with Wu et al. 2026 (PMID:42427617), whose alignment
  marks a "non-catalytic aspartic acid residue in RBMP2" at the catalytic-cysteine
  position and calls the domain "non-catalytic".
- Conclusion: the domain cannot perform the persulfide (sulfurtransferase) or
  phosphocysteine (CDC25-type phosphatase) chemistry. Do not annotate
  thiosulfate-cyanide sulfurtransferase activity, sulfurtransferase activity or
  phosphatase activity.

## 2. Six Rubisco-binding motifs in the C-terminal half

Matches to the Meyer et al. 2020 consensus `[D/N]W[R/K]XX[L/I/V/A]` (PMID:33177094):
1126 NWRDVI, 1265 DWRQAA, 1345 NWRDQV, 1592 DWRREL, 1638 NWRQQV, and 1685 DWRARV at the
exact C-terminus (C-terminal residue Val, as Meyer et al. note). Six motifs, matching the
count given by Adler et al. 2022 (PMID:35961043) and Wu et al. 2026 (PMID:42427617).

## 3. Hydrophobic segments (Kyte-Doolittle, 19-aa window, mean >= 1.6)

- 684-714 (max 2.47): strong candidate transmembrane helix, N-terminal to the rhodanese
  domain.
- 961-981 (max 1.82): weaker candidate, C-terminal to the rhodanese domain.
- 191-209 and 403-422 are Ala/Pro-rich low-complexity stretches that only just pass the
  threshold and are unlikely to be real membrane spans.

This crude screen agrees with the DeepTMHMM result reported by Wu et al. 2026
("predicted transmembrane helices (TM) on both sides of the RHO domain"). It is not a
topology prediction; the side of the membrane on which the rhodanese domain sits is not
established here.

## Not done

No transit-peptide prediction (TargetP/PredAlgo not available offline). The N-terminus is
Ala-rich and Ser-rich, as is typical of Chlamydomonas chloroplast transit peptides, but
this is not asserted as a result.
