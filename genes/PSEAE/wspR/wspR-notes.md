# wspR (PA3702, Q9HXT9) review notes

## Summary of the literature

WspR is a 347-aa response regulator with an N-terminal receiver domain (UniProt
20-137, phospho-acceptor D70) and a C-terminal GGEEF diguanylate cyclase domain
(201-339). It is the output of the Wsp chemosensory system. No hydrophobic
segment long enough for a TM helix (Kyte-Doolittle, 19-residue window, threshold
1.6; scan run in this session) and no UniProt TRANSMEM feature: it is soluble.

- Hickman et al. 2005 (PMID:16186483; full text cached). Purified WspR makes
  c-di-GMP and phosphorylation stimulates it [PMID:16186483 "We determined that
  purified WspR catalyzed the formation of c-diGMP in vitro and phosphorylation
  stimulated this activity."]. A wspF mutant (constitutively active Wsp pathway)
  has more c-di-GMP and more biofilm, WspR-dependently.
- De et al. 2008 (PMID:18366254; abstract cached). Crystal structure of WspR bound
  to c-di-GMP at the inhibitory site; active dimer, tetramer and product-inhibited
  dimer [PMID:18366254 "By switching from an active to a product-inhibited dimer via
  a tetrameric assembly, WspR utilizes a novel mechanism for modulation of its
  activity through oligomerization."]. Basis of the IntAct IPI GO:0042802 row.
- Kulasakara et al. 2006 (PMID:16477007). Full text read on the PMC web page
  (PMC1413825) in this session; the cached copy is abstract-only. DGC activity was
  measured as c-di-GMP extracted from cells overexpressing each protein: "To detect
  DGC activity, cultures overexpressing genes that encode DGC-containing proteins
  were extracted and analyzed for c-di-GMP content". Table 1 row: "PA3702 GGEEF
  +(445)" (pmol c-di-GMP per mg wet cell weight), the highest value in the table.
  Footnote: "Given the limits of sensitivity of the HPLC assay (12 pmol/mg cell wet
  weight), we cannot conclude that any particular DGC or PDE domain does not have
  the corresponding enzymatic activity in vivo".
- D'Argenio et al. 2002 (PMID:12426335; full text cached and read). Genetics only:
  wspR insertions suppress the wrinkled, autoaggregative colonies of a wspF mutant
  and restore motility [PMID:12426335 "Mutation of wspR completely suppressed colony
  wrinkledness and restored swarming and swimming motility"]. No c-di-GMP or
  enzyme assay; the GGDEF nucleotide-cyclase link is discussed only as a hypothesis
  [PMID:12426335 "The mechanism by which regulatory proteins with a GGDEF domain
  exert their effect is not yet clear, but there is growing evidence that the
  domain encodes a nucleotide cyclase"].

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002895344 | GO:0052621 diguanylate cyclase activity | 19 | 205 (28 taxa) | GO:0052621, IDA, PMID:16477007 (PseudoCAP) | SOUND | Cells overexpressing WspR accumulated 445 pmol/mg c-di-GMP (full text read); purified WspR is active (PMID:16186483). | E. coli DosC, DgcC, DgcJ, DgcM, DgcN, DgcP, DgcQ, DgcZ; B. subtilis DgcK, DgcP; Shewanella DgcS; P. aeruginosa dgcP, PA1107, PA2870, PA3177, PA3343, PA4332, PA4843 | Yes. Many seeds have direct activity evidence; the node term is the defining activity of GGDEF DGCs. No GO_CENTRAL defect. |
| PTN002895344 | GO:0052621 diguanylate cyclase activity | 19 | 205 (28 taxa) | GO:0052621, IMP, PMID:12426335 (PseudoCAP) | INDIRECT-PHENOTYPE | Suppressor genetics of colony morphology; no c-di-GMP measured (full text read). The term is right for WspR, but this paper does not show it. | as above | Yes (this row adds nothing to the node; WspR's own IDA row and the other seeds carry it). |

Batch consistency (PA3177, dgcP, wspR, PA4332, PA4843 all seed PTN002895344):
all seed rows except this IMP are SOUND, so no node-level GO_CENTRAL defect is
needed for PTN002895344.

## Non-seed IBA nodes (PTN002895351)

The PM, cell-adhesion and motility IBAs come from PTN002895351, whose IBDs are
seeded by E. coli proteins only (PM: DgcN, DgcQ, DgcJ, P76236, P76147, P75801;
GO:0043709: DgcZ alone; GO:1902201: DgcJ, P76236, DgcQ, DgcN). None of my genes
seeds it, but its PM term reaches four soluble P. aeruginosa DGCs in this batch
(WspR, DgcP, PA3177, PA4843). The node-level GO_CENTRAL defects for PTN002895351
(PM; GO:0043709) are recorded once, here on wspR, and cross-referenced from the
PA3177, dgcP, PA4332 and PA4843 notes.

## Annotation decisions

- GO:0052621 (IBA, IDA, IEA, IMP): ACCEPT. The IMP row carries a PSEUDOCAP defect
  (paper does not show the activity).
- GO:0005886 IBA and IEA: MARK_AS_OVER_ANNOTATED (soluble response regulator).
- GO:0043709 IBA: MARK_AS_OVER_ANNOTATED (a DGC regulates attachment, it does not
  perform cell adhesion).
- GO:1902201 IBA: ACCEPT (wspR loss restores motility of the wspF mutant).
- GO:0000160 IEA: KEEP_AS_NON_CORE (receiver domain of the Wsp phosphorelay).
- GO:0042802 IPI: KEEP_AS_NON_CORE (regulatory oligomerization).

## Verbatim excerpts from full texts not in the cache

PMID:16477007 (PMC1413825, read on the PMC web page):

- To detect DGC activity, cultures overexpressing genes that encode DGC-containing proteins were extracted and analyzed for c-di-GMP content
- PA3702 GGEEF +(445)
- DGC activity is measured as pmol of c-diGMP produced per mg wet cell weight.
- Given the limits of sensitivity of the HPLC assay (12 pmol/mg cell wet weight), we cannot conclude that any particular DGC or PDE domain does not have the corresponding enzymatic activity in vivo

## Hydrophobicity scan

Kyte-Doolittle, 19-residue window, mean above 1.6: no window found in WspR (347 aa).
The same scan finds the six TM helices of PA4332 (SadC), which UniProt also annotates.

## Defects recorded (2026-11-05)

- PSEUDOCAP, GO:0052621 IMP (PMID:12426335): WRONG_REFERENCE, repoint to
  PMID:16186483; CONFIRMED (full text read).
- GO_CENTRAL, PTN002895351 GO:0005886 (node-level, recorded once here for the
  batch): PROBABLE. Seeds are six E. coli inner-membrane DGCs, all IDA from
  PMID:15919996 (QuickGO, 2026-11-05); the node also covers soluble WspR,
  PA3177, DgcP and PA4843 (no TRANSMEM in UniProt, no hydrophobic window).
- GO_CENTRAL, PTN002895351 GO:0043709 (node-level, recorded once here):
  WRONG_QUALIFIER, PROBABLE. The sole seed, E. coli DgcZ (P31129), carries the
  term in QuickGO only as IMP with qualifier acts_upstream_of_or_within
  (EcoCyc, PMID:19460094); the IBD asserts involved_in. PA3177 deletion has no
  effect on attachment (PMID:30082282).
