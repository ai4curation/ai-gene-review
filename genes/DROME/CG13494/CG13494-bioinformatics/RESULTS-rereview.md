# CG13494 (Q8MZA7) re-review sequence analysis

Script: `analyze_rereview.py` (stdlib Python + HMMER `hmmsearch`); raw output: `results-rereview.json`.
Run date: 2026-10-21.

## Segment composition

- Residues 1-36 (N-terminal, before the Phobius TM helix): Thr 30.6%, Ser 13.9%, Ala 11.1%; a Ser/Thr-rich low-complexity segment.
- Residues 37-61 (Phobius TM helix): Leu 32.0%, Val 20.0%, Ile 20.0%, Cys 12.0%; hydrophobic.
- Residues 62-120 (C-terminal): Gly 35.6%, Cys 28.8%, Asp 16.9%; a Gly/Cys/Asp-rich low-complexity tail (CCG / GGGCC repeats).
- Whole protein: 20 Cys and 25 Gly in 120 residues.

## Family / domain signatures

- InterPro API for Q8MZA7 returned no member-database matches (HTTP 204): no Pfam, PANTHER, PROSITE, SMART or CDD signature.
- The Pfam CYSTM HMM (PF12734; a TM helix followed by a Cys-rich segment) does not match Q8MZA7: full-sequence score -42.3 bits, E-value 1.0. Resemblance to CYSTM is compositional only.
- The UniProt eggNOG cross-reference KOG4726 also covers human keratin-associated proteins (KRTAP3/4/10/12/17) and CRCT1 (UniProt query xref:eggnog-KOG4726, reviewed). That grouping reflects shared Cys-rich low complexity, not demonstrated homology, and is not used to transfer function.

## Taxonomic distribution

- OMA HOG HOG:F0655449: deepest level is "melanogaster group". OMA reports 1:1 orthologs only in D. ficusphila, D. erecta, D. sechellia, D. simulans, D. yakuba and D. suzukii.
- No ortholog outside the melanogaster species group, and no characterised relative in any organism.

## Conclusion

CG13494 encodes a lineage-restricted (melanogaster species group) protein with one predicted TM helix, a Ser/Thr-rich N-terminus and a Gly/Cys-rich C-terminus. It has no recognised family or domain, so no characterised homolog exists from which function could be inferred evolutionarily. Only a membrane location is supported, and that rests on the TM prediction alone.
