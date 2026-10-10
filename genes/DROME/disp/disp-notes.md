# disp (Dispatched, Q9VNJ5) curation notes

Deep research: `disp-deep-research-falcon.md` (falcon; the wrapper reported a 600 s timeout but the run completed later). Folded in as an EDIT; its conclusions agree with the review and it is cited in the core function.

## Literature journal

- disp is a segment-polarity gene required in Hh-sending cells; Disp releases cholesterol-anchored Hh
  [PMID:10619433 "In the absence of Disp, cholesterol-modified but not cholesterol-free Hh is retained in these cells, indicating that Disp functions to release cholesterol-anchored Hh."]
- Disp shares a sterol-sensing domain with Patched
  [PMID:10619433 "Disp and Ptc share structural homology in the form of a sterol-sensing domain"]
- Genetic screen: disp acts upstream of ptc and only in secreting cells; contrasted with cmn (rasp)
  [PMID:11748147 "unlike disp, which is required for the release of the cholesterol-modified form of Hh"]
- Mouse DispA rescues fly disp; biochemical release assay; RND-transporter residues required
  [PMID:12372301 "This activity is disrupted by alteration of residues functionally conserved in Patched and in a related family of bacterial transmembrane transporters"]
- Disp-YFP localizes to basal cytonemes in the wing disc
  [PMID:24121526 "Dispatched (Disp), which is required for Hh release34, and Dlp, which is required for both Hh release28 and reception35, localised to basal protrusions"]
- Germ cell migration: trans-heterozygous interactions of hmgcr with hh pathway mutants
  [PMID:16256738 "there are substantial germ cell migration defects in trans combinations between hmgcr and mutations in different components of the hh pathway"]

## Curation decisions

- GO:0007225 patched ligand maturation is defined as posttranslational modification of Hh (signal
  sequence cleavage, autoprocessing, sterol attachment). Disp releases already-modified Hh, so the four
  rows were MODIFY -> GO:0009306 protein secretion. GO has GO:0061355 Wnt protein secretion but no
  Hh-specific secretion term; raised as a suggested question.
- GO:0007224 smoothened signaling pathway (IBA) kept as non-core: Disp acts in the sending cell.
- No molecular function term has fly-specific experimental support; core function records BP + location only.
