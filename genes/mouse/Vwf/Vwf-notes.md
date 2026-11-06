# Vwf (mouse) review notes

## Session 1

- Fetched Q8CIZ8 (Swiss-Prot VWF_MOUSE, MGI:98941, GeneID 22371); 69 GOA rows.
- Literature summarized in `Vwf-deep-research-manual.md` (no deep-research provider).
- Human VWF review (`genes/human/VWF`) used for consistency of ISO/ISS judgments; the
  mouse ISO/ISS rows all descend from human P04275 or rat RGD:621759.

### Key decisions

- Core: collagen binding, GPIb (cell adhesion molecule) binding, integrin binding,
  FVIII carrier, self-association; processes hemostasis, cell-substrate adhesion,
  blood coagulation; locations extracellular region/matrix and Weibel-Palade body.
- Liver/placenta development (PMID:7854452): the paper is the Hgf knockout and the
  With/From allele is Hgf<tm1Cbm> (MGI:1857656). Wrong gene product upstream. The
  cached copy is abstract-only, so per the session rules the rows are UNDECIDED with a
  WRONG_GENE_PRODUCT source defect rather than REMOVE. [PMID:7854452 "Here we report
  that mice lacking SF/HGF fail to complete development and die in utero."]
- External side of plasma membrane (PMID:8562500): CD24/P-selectin paper; abstract does
  not mention VWF. UNDECIDED with a SUSPECTED wrong-gene defect (CHECK).
- Immunoglobulin binding rows: derived from human PMID:3121636, where the partner is
  BiP ("heavy chain binding protein"), an ER chaperone. MODIFY to protein-folding
  chaperone binding; source defect on the human UniProt row.
- Platelet activation: positive rows (ligand role for GPIb signalling) non-core; the NOT
  row (PMID:17380206, laser injury, thrombin-driven) is context-specific; consistency
  exception recorded.
- ECM structural constituent: over-annotation (VWF is an adhesive bridge, not
  load-bearing matrix), consistent with human review.
- PMID:20097747 is a rat study using anti-vWF only as an endothelial marker; not
  informative for Vwf function (LOW relevance).

### Open idea (not asserted)

- VWF is the structural driver of Weibel-Palade body formation [PMID:11274431 "the
  typical rodlike shape of the Weibel--Palade body is missing in vWf -/- endothelial
  cells"]. GO:0033363 secretory granule organization could fit (VWF tubules are the
  organelle's scaffold), but this was left as a suggested question rather than a NEW
  row, pending a comparator check of how GO treats cargo-scaffold proteins.
