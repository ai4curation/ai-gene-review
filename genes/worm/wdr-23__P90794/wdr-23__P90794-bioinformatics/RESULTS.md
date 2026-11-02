# wdr-23 (P90794): DxR-box motif mapping

Script: `dxr_motifs.py` (stdlib only; `uv run --script dxr_motifs.py` from this folder).
Output: `results.json`. Input is only `../wdr-23__P90794-uniprot.txt` (canonical isoform a, 571 aa).

## Result

Four (W/Y)DxR motifs occur in WDR-23A:

| Motif | Start | Arg | UniProt WD repeat |
|-------|-------|-----|-------------------|
| WDKR | 339 | R342 | WD 3 |
| WDLR | 386 | R389 | WD 4 |
| WDYR | 409 | R412 | between WD 4 and WD 5 |
| WDER | 513 | R516 | WD 6 |

R342 and R389, the two arginines that Staab et al. 2013 (PMID:23555279) mutated to His to make the
DDB-1-binding-deficient WDR-23(DxR) allele, are both arginines of WDxR motifs in this sequence.
The paper places them in "WD repeats four and five"; in UniProt's repeat numbering they lie in WD 3 and WD 4.
The difference is in repeat numbering only, not in residue identity.

## Limits

This is a sequence observation. It confirms that the residues tested experimentally sit in canonical
DDB1-binding motifs; it is not by itself evidence of DDB-1 binding.
