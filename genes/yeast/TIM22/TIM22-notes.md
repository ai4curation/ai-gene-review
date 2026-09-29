# TIM22 notes

## 2026-09-29 IBA re-review

GOA carries four PTHR14110 IBA rows for TIM22. Current PAINT keeps the conserved
TIM22 complex (`GO:0042721`) and inner-membrane protein insertion (`GO:0045039`)
assertions at `PANTHER:PTN000364156`, but no longer has either of the two older
molecular-function rows from the GOA snapshot (`GO:0030943` mitochondrion targeting
sequence binding and `GO:0008320` transmembrane protein transporter activity). The
current molecular function on that node is `GO:0032977` membrane insertase activity,
added on 2026-07-29, which is a better direct activity term for the Tim22
carrier-pathway insertase.

`GO:0030943` is obsolete in current GO and should be remapped rather than accepted
as-is. For TIM22, the receptor replacement `GO:0140436` would be the wrong role:
Tim22 responds to internal targeting sequences as the signal-gated insertion channel,
whereas the current PAINT update captures the insertase activity itself.

## 2026-09-29 literature check

Recent searches for `TIM22`, `YDL217C`, and the yeast TIM22 carrier translocase in
2025-2026 found Badrie, Hell, and Mokranjac 2025 (`PMID:39753782`; DOI
`10.1038/s44319-024-00349-6`), already cited in the UniProt flatfile for Tim22
disulfide-bond assembly. That Dbi1 oxidoreductase/chaperone work refines how the
C42-C141 disulfide is introduced and how Tim22 assembly is assisted, but it does not
change the core GO review: Tim22 remains the channel-forming TIM22-complex subunit
whose conserved activity is inner-membrane insertion of hydrophobic multi-pass
precursor proteins.
