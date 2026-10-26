# A0A2I0M3K7 (Columba livia TRUB2 gene model) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not opened or used. Evidence used: UniProt record, PANTHER/PAINT files under
`interpro/panther/PTHR13195/`, cached abstracts PMID:27974379 and PMID:33023933, human TRUB2
(O95900) UniProt features and GOA (QuickGO), and a new alignment analysis.

### Identity: truncated gene model
- 142 aa, unreviewed TrEMBL, from unassembled WGS contig AKCR02000043 (PE 3).
- Aligns to human TRUB2 (331 aa) residues 178-307 at 72.7% identity; pigeon Met1 = human Met178
  [file:COLLI/A0A2I0M3K7/A0A2I0M3K7-bioinformatics/RESULTS.md "Pigeon Met1 corresponds to human TRUB2 Met178"].
- Missing human residues 1-177, which include the catalytic nucleophile D98 (UniProt O95900
  ACT_SITE 98; maps to E. coli TruB D48) and the predicted transit peptide (1-10)
  [file:COLLI/A0A2I0M3K7/A0A2I0M3K7-bioinformatics/RESULTS.md "so A0A2I0M3K7 lacks the catalytic aspartate"].
- No full-length pigeon TRUB2 entry exists in UniProt (gene:TRUB2 AND organism_id:8932 returns
  only this accession), so there is no same-gene canonical product to review.

### Evolutionary grounding
- PTHR13195:SF0 (PSEUDOURIDYLATE SYNTHASE TRUB2, MITOCHONDRIAL) and IPR039048 Trub2: same
  subfamily as human TRUB2.
- PAINT node PTN000324318 (Bilateria), seeded by human TRUB2 only, asserts GO:0009982, GO:1990481,
  GO:0070131, GO:0005759. It does NOT assert GO:0160148 / GO:0070902 although human TRUB2 has
  IMP for both (PMID:33023933). Treated as a deliberate decision.

### Changes vs previous review
- GO:0009982: MODIFY -> GO:0160148 replaced by ACCEPT (tRNA Psi55 not projected by PAINT).
- GO:0001522: MODIFY target changed GO:0070902 -> GO:1990481 mRNA pseudouridine synthesis.
- GO:0009451: KEEP_AS_NON_CORE -> MODIFY to GO:1990481 (correct-but-general rule).
- GO:0006396: kept MARK_AS_OVER_ANNOTATED, but reason corrected: in current GO, RNA modification
  is not under RNA processing (OLS ancestors checked), so the old "RNA modification is the parent"
  rationale was wrong.
- GO:0003723: KEEP_AS_NON_CORE retained.
- NEW GO:0005759 mitochondrial matrix (PAINT IBD + human RNA-granule localization).
- GO:0070131 positive regulation of mitochondrial translation (also on the PAINT node) not added:
  knockdown effect on translation is downstream of the modification, not participation.
- Core function changed to pseudouridine synthase activity / mRNA pseudouridine synthesis /
  mitochondrial matrix; description rewritten to state the truncation.
- Deep research report retained as reference but marked DISPUTED/not used; its finding quote was not
  verbatim and was corrected.

### Relative
- Human TRUB2 (O95900), same PANTHER subfamily SF0 and the PAINT seed. No review exists in
  `genes/` (no TRUB2 folder in any species) -> needs review.
- PANTHER family review `interpro/panther/PTHR13195/PTHR13195-review.yaml`: places this entry in
  SF0, agrees; it also leaves tRNA Psi synthase activity UNRESOLVED, consistent with this review.
- No modules mention TRUB2 or PTHR13195.
