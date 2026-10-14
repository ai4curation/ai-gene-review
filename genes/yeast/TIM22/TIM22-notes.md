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

QuickGO marks `GO:0030943` obsolete in current GO and notes that it was obsoleted in
favor of more specific molecular functions. For TIM22, the receptor replacement
`GO:0140436` would be the wrong role: Kovermann et al.'s signal-recognition evidence
is real, but Tim22 responds to internal targeting sequences as the signal-gated
insertion channel, and `GO:0032977` already covers binding a transmembrane-domain
protein and mediating its integration into the inner membrane.

## 2026-09-29 literature check

Recent searches for `TIM22`, `YDL217C`, and the yeast TIM22 carrier translocase in
2025-2026 found Badrie, Hell, and Mokranjac 2025 (`PMID:39753782`; DOI
`10.1038/s44319-024-00349-6`), already cited in the UniProt flatfile for Tim22
disulfide-bond assembly. That Dbi1 oxidoreductase/chaperone work refines how the
C42-C141 disulfide is introduced and how Tim22 assembly is assisted, but it does not
change the core GO review: Tim22 remains the channel-forming TIM22-complex subunit
whose conserved activity is inner-membrane insertion of hydrophobic multi-pass
precursor proteins.

## 2026-10-01 current GOA refresh

- Re-fetched GOA, UniProt, cached PMIDs, and the current `PTHR14110` PAINT table.
  Current PAINT still places `GO:0042721` TIM22 mitochondrial import inner membrane
  insertion complex, `GO:0045039` protein insertion into mitochondrial inner
  membrane, and `GO:0032977` membrane insertase activity on `PTN000364156`.
- Resolved the new exact ComplexPortal `GO:0042721` IPI row from PMID:10648604
  as `ACCEPT`; the paper directly identifies Tim22p as an integral membrane
  subunit of the 300-kDa TIM22 complex.
- Retired three exact assertions no longer present in current GOA: the old
  `GO:0030943` IBA row, the broad UniProt keyword `GO:0015031` protein transport
  row, and the old direct `GO:0030943` row from PMID:11864609. The signal-recognition
  evidence remains relevant but is now captured by the proposed `GO:0032977`
  membrane insertase activity annotation.
- Searched 2025-2026 TIM22/Saccharomyces literature; newer hits were either broad
  mitochondrial import/proteostasis work or not direct yeast TIM22 functional papers,
  so they did not change the IBA or core-function calls.
