# RHOJ G3V4H1 re-review: product identity and G-domain completeness

Script: `compare_sequences_rereview.py` (PEP 723, stdlib only). Run with
`uv run --script compare_sequences_rereview.py`; the raw output is saved in
`RESULTS-rereview.txt`. Sequences are fetched live from the UniProt REST API
(G3V4H1, Q9H4E5) and transcript models from the Ensembl REST API (GRCh38).
This analysis is independent of any ML function prediction and uses no
prediction output as input.

## Product identity

- G3V4H1 is 153 aa; the reviewed canonical RHOJ product Q9H4E5 is 214 aa.
- G3V4H1 is identical to Q9H4E5 over residues 1-103 only. The G3V4H1 divergent tail (104-153) is WDLPPPHPGMRMAANLCGQAPAKKEGTTRKELPLHGGLPHHPLSPPNTAH.
- G3V4H1 is the translation of Ensembl transcript ENST00000557447 (RHOJ-204), biotype nonsense_mediated_decay, not the Ensembl canonical transcript. The canonical product is encoded by ENST00000316754 (RHOJ-201), biotype protein_coding.
- The two coding sequences are identical to nt 305 (codon 102). RHOJ-204 uses a shorter version of canonical exon 3 (ends at 63281036 instead of 63281135), skips canonical exon 4 (63283121-63283216) and splices into two sub-segments of the canonical last exon (63291026-63291511 and 63292928-63293219).
- The tail probe WDLPPPHP is not found in any reading frame of the canonical CDS, and the downstream RHOJ-204 coding sequence does not resume the canonical CDS: the tail is encoded by sequence that is non-coding in the canonical transcript. The RHOJ-204 tail exon begins at 63291026, immediately 3' of the canonical stop codon (canonical translation ends at 63291024), and the RHOJ-204 stop lies at 63291184, so the 50-residue tail is read from the canonical 3' UTR.
- G3V4H1 is therefore not either of the two UniProt-described isoforms of Q9H4E5 (isoform 2, Q9H4E5-2, lacks residues 113-134 but keeps the canonical C-terminus). It is an alternative gene model from an NMD-targeted transcript.

## G-domain motifs

| Motif | Q9H4E5 | G3V4H1 |
|---|---|---|
| G1 P-loop GxxxxGK(S/T) | 28 GDGAVGKT | 28 GDGAVGKT |
| G2 switch I PTVFD | 52 PTVFD | 52 PTVFD |
| G3 switch II DTAGQ | 75 DTAGQ | 75 DTAGQ |
| G4 (T/N)(K/Q)xD guanine-base motif | 133 TQID | absent |
| G5 (C/S)SA(L/K) guanine-base motif | 175 CSAL | absent |
| C-terminal CAAX box | 211 CSII | absent |

## Interpretation

G3V4H1 retains the phosphate/Mg2+-binding elements (P-loop, switch I, switch II) but lacks the G4 and G5 motifs that contact the guanine base, the C-terminal half of the Ras-like fold (beyond codon 103), the polybasic region and the CAAX prenylation site. The result is not a complete small-GTPase domain, and it comes from a transcript annotated for nonsense-mediated decay. These are sequence and transcript-model observations; they do not show whether any G3V4H1 polypeptide accumulates in cells, or what it does if it does.
