# lhfpl5b notes (Danio rerio, LHFPL tetraspan subfamily member 5b; UniProt B0UYJ1)

## 2026-09-28 — session log (DANRE_DUPLICATION batch 3, random TGD_tree sample)

**Deep research:** not available (Edison/Falcon 402 Payment Required; OpenAI key invalid). Not attempted, per
instructions. Literature searched by hand; see `../lhfpl5a/lhfpl5a-notes.md` for the shared literature and
`../lhfpl5a/lhfpl5a-bioinformatics/RESULTS.md` for the pair analysis.

Accession B0UYJ1 (TrEMBL, 221 aa; UniProt predicts 3 TM helices, the paper's alignment shows 4),
ZFIN:ZDB-GENE-080220-51, Ensembl ENSDARG00000056458, chr8. Mutant allele vo35 (CRISPR 5-bp deletion, S77FfsX48):
[PMID:32009898 "This mutation disrupts the protein in the first extracellular loop and deletes the final three of four transmembrane helices in Lhfpl5b."]

### Expression
- Lateral line only, from 2 dpf: [PMID:32009898 "Conversely, we detect lhfpl5b expression exclusively in neuromasts at this stage, both on the head (Figure 2D) and trunk (data not shown)."]
- Not in 1 dpf ear: [PMID:32009898 "No signal for lhfpl5b was observed at this time point (Figure 2B)."]
- Bgee (expression_compare.py) lists low-to-moderate bulk RNA-seq calls in many adult tissues and early embryo
  stages for lhfpl5b. These are not hair-cell resolved; I did not use them for the fate call. ZFIN curated records are
  neuromast only.

### Function
- [PMID:32009898 "CRISPR-Cas 9 knockout of lhfpl5b alone silences the lateral line organ but has no effect on otic hair cell function."]
- Residual labeling in a few cells persists in double mutants, so lhfpl5a does not compensate:
  [PMID:32009898 "Occasional labeling persists in lhfpl5a/lhfpl5b double mutants, indicating that lhfpl5a is not partially compensating for the loss of lhfpl5b (Supplementary Figures 3A–D)."]
- Cross-rescue (key for fate): [PMID:32009898 "The loss of MET channel activity in lhfpl5bvo35 neuromasts is rescued by expression of the GFP-lhfpl5a vo23Tg transgene (Figures 4I,J; n = 7/7 mutant individuals). This result indicates that Lhfpl5a and Lhfpl5b are functionally interchangeable in this context."]
- Adult viable: [PMID:32009898 "The lhfpl5b mutants are adult viable (data not shown) and represent a possible genetic model for understanding the lateral line in both larval and adult fish."]
- Used as a lateral-line-only mutant: swim bladder (PMID:37272538), pth2 social regulation (PMID:36161311).

### Annotation decisions
- ND root MF → REMOVE (function known: MET accessory subunit, interchangeable with Lhfpl5a).
- GO:0007605 sensory perception of sound (IBA) → MARK_AS_OVER_ANNOTATED: not expressed in the ear; mutants hear.
- GO:0035678 neuromast hair cell morphogenesis (IMP) → MARK_AS_OVER_ANNOTATED: phenotype is fewer hair cells, a
  consequence of lost transduction.
- Tried a NEW IMP row for GO:0050974; the validator rejects NEW for a term already in GOA (IBA), so the
  experimental evidence is attached to the IBA review instead.
