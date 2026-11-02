# GPC3 (human, P51654) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: human GPC3 is the experimentally characterised ortholog (same PANTHER
subfamily PTHR10822:SF4, GLYPICAN-3) of HORSE/GPC3 (A0A3Q2L6D3), and a seed of the
PAINT nodes PTN002585559 (plasma membrane) and PTN000850517 (positive regulation of
canonical Wnt signaling). No ProtNLM2 files were opened.

### Deep research
`just deep-research-falcon human GPC3 --fallback perplexity-lite` failed: Edison
API returned 403 on auth (`Failed to authenticate`), and the perplexity-lite fallback
also failed. No deep-research file was written. The review is built from cached
publications (full text for PMID:14610063, PMID:39822733, PMID:25653284; abstracts
for the rest) and the UniProt record.

### Evidence summary, by species
Established experimentally for the HUMAN protein:
- Cell-surface, GPI-anchored, convertase-processed alpha/beta heterodimer
  [PMID:14610063 "It generates two core protein subunits, designated as α and β, which remain in association with one another through disulfide bonding, and with the cell surface via the GPI-tail of the β subunit."]
- Binds Wnts and stimulates canonical Wnt signalling in HCC cells
  [PMID:16024626 "Co-immunoprecipitation experiments showed that GPC3 is able to form complexes with Wnts"]
- Binds Frizzled via HS chains; Wnt-Fz-GPC3 complex is co-endocytosed
  [PMID:24496449 "GPC3 and Frizzled interact directly through the glycosaminoglycan chains of GPC3"]
- In CHO cells represses canonical and non-canonical Wnt reporters; binds Wnt5A
  [PMID:14610063 "Together, these results indicate that GPC3 overexpression suppresses noncanonical Wnt signaling in CHO-K1 cells"]
- Binds DPP4/CD26 and inhibits its peptidase activity (single abstract-only study)
  [PMID:17549790 "led to the inhibition of CD26 peptidase activity"]
- Binds AFP directly [PMID:39822733 "We further validated the direct interaction of GPC3 and alpha-fetoprotein (AFP) in cell-free immunoprecipitation"]
- Shed/serum GPC3 in HCC [PMID:12851874]

Established in MOUSE (ortholog, same PANTHER subfamily) and transferred by ISS:
- Hedgehog binding, competition with Patched, Hh endocytosis/degradation, negative
  regulation of Hh signalling [PMID:18477453 "GPC3 competes with Patched for Hedgehog binding"]
  (convertase processing requirement: PMID:25653284, which UniProt attaches to the human entry).
- Renal branching/proliferation and coronary development phenotypes of Gpc3-null mice
  (UniProt By similarity; primary papers not cached).

Zebrafish: morphant gastrulation movements (epiboly, convergent extension), rescued only
by processable GPC3 [PMID:14610063].

### PAINT
PTHR10822 PAINT file: GPC3 lineage gets PTN002585559 (PM), PTN000850517 (pos. reg.
canonical Wnt; seeds dally + human GPC3), and deep node PTN002247069 (cell surface,
extracellular region, cell migration, regulation of protein localization to membrane).
No hedgehog-regulation IBD is placed on the GPC3 lineage; I treat hedgehog antagonism
as ortholog-based (ISS), not phylogenetically inferred. The negative/cell-type specific
Wnt effects were not propagated, consistent with stimulation being the conserved trait.

### Decisions worth flagging
- GO:0060422 peptidyl-dipeptidase inhibitor activity is mis-specified for DPP4 (an
  N-terminal dipeptidyl-peptidase, GO:0008239); MODIFY to GO:0030414 peptidase
  inhibitor activity. Suggested question raised about a missing GO term.
- Developmental knockout/morphant phenotypes (coronary vasculature, gastrulation
  cell migration, anatomical structure morphogenesis) marked over-annotated; kidney
  growth-factor modulation rows kept as non-core.
- protein binding: DPP4 row -> protease binding; SMYLE-complex row and AFP row removed
  (uninformative; PMID:29162697 abstract does not mention GPC3).
- NEW: frizzled binding (IDA, human), Wnt-protein binding (IDA, human), hedgehog family
  protein binding (ISS, mouse-based).
