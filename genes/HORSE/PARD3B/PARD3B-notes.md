# PARD3B (horse, A0A9L0RMF2) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

New review (no prior file). ProtNLM2 predictions were not opened or used.

### Setup and provenance

- `just fetch-gene HORSE A0A9L0RMF2 --alias PARD3B` (needed retries after an EBI read timeout);
  stub id confirmed as A0A9L0RMF2; 14 GOA rows (10 IBA, 4 IEA).
- `just deep-research-falcon HORSE PARD3B --fallback perplexity-lite` FAILED: falcon
  "Failed to authenticate"; perplexity fallback returned HTTP 401 insufficient quota. No
  deep-research file exists; the review rests on literature fetched directly from PubMed
  (search for Pard3b / Par3L / PAR3beta, 43 hits) and cached with `just fetch-pmid`.
- Bioinformatics: `PARD3B-bioinformatics/analyze.py` → `RESULTS.md`.

### Identity of the benchmark accession

- A0A9L0RMF2 is an unreviewed Ensembl-derived horse entry (ENSECAP00000063002), 1238 aa,
  PE 3. Horse has 10 unreviewed PARD3B entries (1106-1238 aa) and no reviewed entry, so this is
  one of several transcript models of the gene; it is the longest. It aligns end to end with
  human PARD3B Q8TEW8 (1205 aa, 88.4% identity) and mouse Pard3b Q9CSB4 (83.0%), with one
  31-residue insertion near horse residue 132, N-terminal to PDZ1, absent from both. N-terminal
  Par3/HAL domain and all three PDZ domains are present. It is a full-length product, not a
  fragment; whether the extra segment is a real exon is unresolved.

### Evolutionary placement

- PANTHER PTHR16484:SF4 (PARD3B subfamily), shared with human and mouse PARD3B. PARD3
  (SF10) and Bazooka/PAR-3 (SF17) are other subfamilies.
- All IBA rows derive from family-level node PANTHER:PTN001046835, donors Bazooka
  (FB:FBgn0000163), C. elegans PAR-3 (WB:WBGene00003918), mouse Pard3 (MGI:2135608), rat
  Pard3 (RGD:620374) and human PARD3 (Q8TEW0). None of the donors is a PARD3B. PARD3B has
  no experimental process annotations in any species (QuickGO).
- The PARD3B subfamily has diverged from PARD3 in a way that matters for those transfers:
  PARD3B does not bind aPKC or (most isoforms) PAR6 [PMID:12459187 "PAR3beta is incapable of
  binding to any isotypes of PAR6 or aPKC"; PMID:12234671 "No Par3L isoforms and only a subset
  of Par3 isoforms detectably bind aPKCs"], and the FXR/KR aPKC-binding motif is mutated
  [PMID:33565714 "In the case of vertebrate PARD3B, both the FXR and KR motifs are mutated"].
  The horse protein shares this loss (RESULTS.md: S827→H, KR motif in a gap).
- PARD3B is lateral/junctional rather than apical [PMID:33565714 "PARD3 and PARD3B have
  diverged such that PARD3 remains tightly associated with aPKC apically, while PARD3B
  localises to adherens junctions"].

### What is known about PARD3B function (same subfamily, transferable to horse)

- Tight junctions: [PMID:12459187 "PAR3beta, expressed intrinsically or extrinsically,
  localizes to the tight junctions"]; [PMID:24859006 "In mature glands Par3L staining was
  restricted to the tight junctions of luminal epithelial cells"].
- Cell cortex: [PMID:24859006 "in the developing glands Par3L was detected at the cell cortex
  in the cap cells of terminal end buds"]; [PMID:41274508 "Par3L is distributed evenly on the
  cell cortex"].
- Binds PARD6B (some isoforms; PMID:12234671), INSC [PMID:16458856], 14-3-3 via
  phospho-Ser746 [PMID:15721295]; horse conserves the S746 context identically.
- Binds and restrains LKB1 (STK11) in mouse mammary stem cells [PMID:24859006 "Par3L, but not
  Par3, binds to the tumour suppressor protein Lkb1 and inhibits its kinase activity"]; binding
  maps to the PDZ2-PDZ3 linker, which is 88-93% identical in horse. Inhibition was read out
  indirectly (pAMPK in HEK293T), so I propose kinase binding, not kinase inhibitor activity.
- Mouse KO: stem cell loss in mammary gland (PMID:24859006); tumours and aberrant spindles in
  gut epithelium (PMID:41274508). These are phenotypes; not used as process annotations.

### Decisions summary

- ACCEPT: bicellular tight junction (IEA), cell cortex (IBA), adherens junction (IBA).
- MODIFY: cell junction → bicellular tight junction; apical junction complex → bicellular tight
  junction + adherens junction.
- KEEP_AS_NON_CORE: endomembrane system; protein-containing complex.
- MARK_AS_OVER_ANNOTATED: microtubule cytoskeleton organization, cell adhesion, intracellular
  protein localization, establishment of cell polarity, epithelial apical/basal polarity
  (all family-node IBA from PARD3/Baz/PAR-3 functions that depend on the aPKC/PAR6 complex
  PARD3B does not form).
- REMOVE: apical plasma membrane (IBA from Bazooka; contradicted by PARD3B lateral localization
  and loss of aPKC binding).
- UNDECIDED: phosphatidylinositol binding (Bazooka-only donor; untested for PARD3B).
- NEW: protein kinase binding (LKB1), 14-3-3 protein binding.

### Relative

Closest characterized relative by phylogeny: human PARD3B Q8TEW8 (same subfamily SF4, 88%
identical); mouse Pard3b Q9CSB4 carries the in vivo work. No review exists for either.
