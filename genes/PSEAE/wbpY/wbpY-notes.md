# wbpY (PA5448, Q9HTB9) notes

No deep-research provider was available; literature research done manually (PubMed MCP + cached
publications).

## Identity

- UniProt Q9HTB9 (TrEMBL, unreviewed; PE 4), 375 aa, *P. aeruginosa* PAO1, locus PA5448, in the
  A-band (common polysaccharide antigen, CPA) cluster next to wbpX (PA5449, G3XCU3) and wbpZ.
- GT4 (CAZy) GT-B fold glycosyltransferase: Pfam PF13439 Glyco_transf_4 and PF00534
  Glycos_transf_1; PANTHER PTHR46401 (GLYCOSYLTRANSFERASE WBBK-RELATED) SF2.

## Function

- CPA is a D-rhamnan homopolymer of trisaccharide repeats [D-Rha a1-2 D-Rha a1-3 D-Rha a1-3]n
  [PMID:35166992 "composed of a homopolymer of D-rhamnose (D-Rha) in trisaccharide repeating units"].
- 1998 genetics: wbpX, wbpY and wbpZ mutants lack A-band LPS while B-band is unaffected; WbpY was
  proposed to add alpha1-3 Rha [PMID:9680202 "Chromosomal wbpX, wbpY and wbpZ mutants were
  generated, and Western immunoblot analysis demonstrates that these mutants are unable to
  synthesize A-band LPS, while B-band synthesis is unaffected"]. Abstract only; the assignment of
  activities in that paper was by sequence and phenotype.
- WbpZ (the first D-RhaT) adds D-Rha a1-3 to GlcNAc/GalNAc-PP-lipid [PMID:25845842].
- 2022 biochemistry: recombinant WbpY transfers one D-Rha from GDP-D-Rha in alpha1-3 linkage onto
  the WbpZ product D-Rha a1-3 D-GlcNAc a-PP-lipid (NMR); WbpX adds a1-2 and a1-3 Rha; WbpX+WbpY
  together make D-Rha oligomers non-processively [PMID:35166992 "NMR spectroscopic analysis of the
  WbpY reaction product showed that WbpY transferred one D-Rha residue in α1-3 linkage to synthetic
  D-Rhaα1-3-D-GlcNAcα-O-PO3-PO3-(CH2)11-O-phenyl acceptor"].
- So WbpY is a GDP-D-rhamnose:D-Rha-a1,3-D-GlcNAc-PP-lipid a1,3-D-rhamnosyltransferase. GO has no
  D-rhamnosyltransferase term; rhamnosyltransferase terms sit under GO:0016758 hexosyltransferase
  activity, which is the most specific existing MF.

## GO structure

- GO:0009243 O antigen biosynthetic process is part_of GO:0009103 lipopolysaccharide biosynthetic
  process (OAK, sqlite:obo:go), so the LPS rows are correct but general for WbpY.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN005302544 | GO:0016757 glycosyltransferase activity | 2 (WbpY, WbpX) | 60 (22 taxa) | GO:0016757 glycosyltransferase activity, IMP, PMID:9680202 | INDIRECT-PHENOTYPE (term correct) | As far as the abstract and the IMP code show (full text not read), the 1998 MF assignment rests on mutant LPS phenotype plus sequence similarity, not an activity assay. The term is nevertheless true: WbpY (and WbpX) were shown in vitro to be GDP-D-Rha rhamnosyltransferases (PMID:35166992). Node conclusion sound for a GT4 clade; re-seed with IDA from PMID:35166992. |
| PTN000749272 | GO:0009103 lipopolysaccharide biosynthetic process | 1 (sole seed) | 51 (19 taxa) | GO:0009103 LPS biosynthetic process, IMP, PMID:9680202 | SOUND | Mutants lack A-band (CPA) LPS and WbpY itself catalyses a chain-extension step of the CPA O antigen, so participation in LPS biosynthesis is direct. LPS biosynthesis is a reasonable breadth for a WbbK-related GT4 subclade from O-antigen clusters; members in other species could instead make capsule or exopolysaccharide, which was not checked. |

## Source-defect re-review (2026-11-10)

An independent re-review of this gene's wrong-gene / wrong-reference source defects changed the following; where earlier notes above say otherwise, this section supersedes them.

- GO:0016757 / PMID:9680202: defect withdrawn (evidence depth: ABSTRACT). PMID:9680202 is the correct wbpY paper (A-band rhamnan; wbpY mutant lacks A-band LPS), and an IMP MF from that phenotype uses the right reference. Nothing in the source record is identifiably wrong - the entry was only a curation-improvement note ("direct evidence now exists in 35166992; please add an IDA and consider retiring the IMP"). Per the "disagreement with curator judgement is not a source defect" rule, removed the source_defects block. The MODIFY to GO:0016758 (hexosyltransferase) stands on the direct D-RhaT assays of 35166992.

## 2026-11-17: the encoding above was reversed; read this first

The section headed "Source-defect re-review (2026-11-10)" says it supersedes
earlier notes, and it still does for everything except its last sentence. That
sentence reads:

> The MODIFY to GO:0016758 (hexosyltransferase) stands on the direct D-RhaT
> assays of 35166992.

It no longer does. `wbpY-ai-review.yaml` carries **no `MODIFY` at all**. The three
`GO:0016757` rows (IBA, IEA, IMP) are `ACCEPT`, and the assayed activity is
asserted on its own `NEW` `GO:0016758` IDA row citing PMID:35166992.

The reason is the maintainer ruling of 2026-11-14: a `MODIFY` needs *this row's
own* evidence for the deeper term. None of the three has it. The IBA inherits a
node typed at `GO:0016757`; the IEA rests on `IPR001296`, a generic GT1 fold
signature shared across many sugar specificities, plus an ARBA prediction; and
the 1998 IMP is a mutant LPS phenotype whose rhamnosyltransferase naming is the
authors' own hedged inference. Refining any of them on a *different* paper's
assays is the move the ruling names. The assay belongs on the row that holds it.

The same change was made to `wbpX` in the same PR, so the pair still agrees: the
shared claim, not the gene, is the unit the audit works on.

**One tension left standing rather than resolved here.** The 2026-11-10 section
records removing a source defect on GO:0016757 / PMID:9680202 on the ground that
it was "only a curation-improvement note" rather than an identifiable error in
the source record. The review currently carries a `GO_CENTRAL` defect on the IBA
row asking that `PTN005302544` be re-seeded with the PMID:35166992 assays, which
is arguably the same class of request aimed at a different resource — the node
rather than the PseudoCAP row. Whether that one should stand under the same rule
is a judgement for a curator, and it is flagged rather than decided here.

Not changed by this: the IBA-seed assessment table above, whose verdicts
(INDIRECT-PHENOTYPE for PTN005302544, SOUND for PTN000749272) still hold, and
whose note that the node should be re-seeded with the 2022 IDA is the request in
question.
