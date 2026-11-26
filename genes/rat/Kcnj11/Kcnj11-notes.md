# Kcnj11 (rat) review notes

- 2026-10-28: Review created. fetch-gene resolved P70673 (Swiss-Prot, RGD:69247,
  GeneID 83535) as expected. 88 GOA rows. No deep-research provider; manual synthesis in
  Kcnj11-deep-research-manual.md.
- Core: pore-forming subunit of KATP (Kir6.2/SUR octamer); ATP-inhibited inward rectifier
  K+ channel activity (GO:0015272; despite the "ATP-activated" label, the definition is
  pore block by ATP). Kir6.2 alone carries the pore, ATP site and PIP2 site
  [PMID:38509107], so `enables` rather than `contributes_to`.
- Upstream issues found:
  - GO:0019829 ATPase-coupled cation transporter (IGI, PMID:28842488) is wrong: the
    paper studies channel gating; Kir6.2 is not a pump. Recorded as WRONG_TERM source
    defect, MODIFY to GO:0015272.
  - GO:0031072 heat shock protein binding (IPI, PMID:20427569): full text shows
    chaperones do not co-IP with Kir6.2 in COS cells lacking SUR1; association via SUR1.
    Recorded source defect (CHECK).
  - GO:0006813 IMP (PMID:16048905): pharmacology (glibenclamide/pinacidil) in pericytes
    co-expressing Kir6.1; no Kir6.2-specific perturbation in the abstract. CHECK the
    evidence code.
  - GO:0042734/GO:0098978 (PMID:17883401): abstract is about Kir6.1/SUR1 at CA3
    presynaptic terminals; full text not available, so UNDECIDED, not REMOVE.
- Many MGI-derived ISO phenotype rows (lifespan, apoptosis, development, AMPK cascade,
  resveratrol) are downstream consequences of loss of the channel: MARK_AS_OVER_ANNOTATED.
- IEP mRNA-level response terms: MARK_AS_OVER_ANNOTATED.
