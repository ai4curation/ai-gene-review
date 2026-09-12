# eryBV (A4F7N6) — review notes

Erythromycin pathway concept (`terms/erythromycin_biosynthesis/`), MIBiG BGC0000055; GenBank
CAM00060.1 → UniProt **A4F7N6**, gene *eryBV*. UniProt entry is a minimally-curated TrEMBL
record (SubName "6-DEB TDP-mycarosyl glycosyltransferase", ECO:0000313|EMBL); all GOA terms are
IEA. This is therefore a homology/cluster-context review.

## Function

EryBV is the **mycarosyltransferase** of the erythromycin pathway and the **paralog of EryCIII**
(both GT-B macrolide glycosyltransferases). It transfers **L-mycarose from TDP-L-mycarose** to
the erythronolide aglycone (erythronolide B / 6-deoxyerythronolide B), forming
3-O-mycarosyl-erythronolide B — the first of the two glycosylation steps (EC 2.4.1.-).

## Annotation review (same donor-specificity error as eryCIII)

- GO:0008194 **UDP-glycosyltransferase activity** (IEA) → **MODIFY** → GO:0016758
  hexosyltransferase. The donor is **TDP-L-mycarose** (a dTDP-sugar), not a UDP-sugar — explicit
  in the UniProt/EMBL name "TDP-mycarosyl glycosyltransferase". (Identical correction to eryCIII.)
- GO:0016757 glycosyltransferase activity (IEA) → ACCEPT (general parent).
- GO:0016758 hexosyltransferase activity (IEA) → ACCEPT (accurate).
- GO:0017000 antibiotic biosynthetic process (IEA) → ACCEPT; add GO:1901115 (erythromycin
  biosynthetic process) in core_functions.

No specific GO MF term exists for the mycarosyltransferase reaction → propose one.

## Note
Unlike its paralog EryCIII (which requires the EryCII activator), the requirement for an
accessory activator by EryBV is not asserted here (not established from the sources at hand).

## References
- UniProt A4F7N6 (TrEMBL); MIBiG BGC0000055. Function inferred from cluster context and the
  TDP-mycarosyl GT name; no experimental GOA evidence is currently attached to this gene.
