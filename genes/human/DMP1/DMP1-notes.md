# DMP1 review notes (2026-10-10)

Deep research: the first `just deep-research-falcon human DMP1` call timed out (600 s); a falcon report
(`DMP1-deep-research-falcon.md`, 2026-10-10) was nonetheless written later and agrees with the manual work below:
it concludes DMP1 is a "regulator of bone and tooth matrix mineralization" that restrains osteocytic FGF23 by an
incompletely understood mechanism. Literature work was done manually via PubMed and the cached `publications/`.

## Function
- Acidic SIBLING-family matrix phosphoprotein of dentin/bone; cloning paper describes "a matrix-associated
  acidic phosphoprotein, with a potentially high calcium ion binding capacity" [PMID:8509401].
- Recombinant DMP1 binds calcium and nucleates apatite: "recombinant DMP1 (rDMP1) possesses calcium-binding
  ability under physiological conditions" and "DMP1 could be considered as a nucleator for apatite deposition
  in vitro" [PMID:12952204].
- Phosphorylation/cleavage state matters: "in its native form, DMP1 inhibits mineralization, but when cleaved
  or dephosphorylated, it initiates mineralization" [PMID:14769788].
- Phosphorylated by FAM20C: "Fam20C phosphorylated OPN, MEPE, and DMP1 in a time-dependent manner" [PMID:22582013].
- Proposed nuclear role (single group): "In the nucleus, DMP1 acts as a transcriptional component for
  activation of osteoblast-specific genes like osteocalcin" [PMID:12615915] - kept non-core.

## Disease (ARHR1)
- "absence of DMP1 results in defective osteocyte maturation and increased FGF23 expression" [PMID:17033621].
- "suggesting that DMP1 may regulate FGF23 expression" [PMID:17033625].
- The FGF23-suppressing role is real at the physiological level but the molecular mechanism is unknown, so it
  is a suggested question rather than a core function / GO process assertion.

## Curation decisions
- Ossification rows -> MODIFY to bone mineralization (GO:0030282).
- ECM organization (IBA/IEA) -> MARK_AS_OVER_ANNOTATED; DMP1 regulates mineral, not matrix assembly.
- Core function: calcium ion binding (GO:0005509) in bone/dentin mineralization, extracellular matrix.
- Alignment with dismech `Autosomal_Recessive_Hypophosphatemic_Rickets_1`: molecular node now carries calcium
  ion binding DECREASED; downstream nodes use bone mineralization / dentin mineralization DECREASED.
