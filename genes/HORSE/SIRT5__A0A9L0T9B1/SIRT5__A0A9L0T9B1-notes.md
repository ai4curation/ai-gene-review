# SIRT5 (horse, A0A9L0T9B1) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Scope: A0A9L0T9B1 is the full-length 310-aa horse SIRT5 product (Ensembl transcript
ENSECAT00000146678, gene ENSECAG00000026898). It is the same gene as the ProtNLM2
benchmark entry F6S899 (genes/HORSE/SIRT5/), which is a 282-aa model that lacks two
zinc-ligand cysteines and NAD+-contacting segments. No ProtNLM2 files were opened.

Deep research: `just deep-research-falcon HORSE A0A9L0T9B1 --alias SIRT5__A0A9L0T9B1
--fallback perplexity-lite` failed (falcon: "Failed to authenticate"; perplexity: HTTP 401
insufficient quota). No deep-research file was produced. The review relies on the cached
human/mouse SIRT5 literature already used by genes/human/SIRT5 and on sequence analysis.

Horse-specific literature: a web search found no experimental study of SIRT5 in horse.
Every function in this review is therefore an ortholog inference; nothing is
experimentally established in this species.

Evolutionary grounding:
- PANTHER PTHR11085:SF10 (same subfamily as human Q9NXA8 and mouse Q8K2C6).
- PAINT: horse inherits IBDs from SIRT5-subfamily node PTN000119399 (mitochondrion,
  cytosol, GO:0036054/36055/61697; seeds human and mouse SIRT5) and eumetazoan node
  PTN000872307 (mitochondrial matrix; seed human SIRT5)
  [interpro/panther/PTHR11085/PTHR11085-paint.tsv]. Nucleus (PTN008492176) and histone
  deacetylase activity (PTN008718612) come from deep sirtuin nodes with no SIRT5 seeds.
- PAINT did not propagate the SIRT5 process terms (protein desuccinylation etc.) that
  human SIRT5 carries by IDA; treated as a deliberate omission, so no NEW process
  annotations were added and core_functions list MF + location only.
- Sequence: 273/310 identical to human SIRT5 (88.1%); His158, Tyr102, Arg105, the four
  zinc Cys (166/169/207/212) and NAD+ motifs all conserved
  [file:HORSE/SIRT5/SIRT5-bioinformatics/RESULTS-rereview.md "A0A9L0T9B1: 310 residues; 273/310 paired residues identical (88.1%)"].
  The canonical Ensembl product A0A9L0T6A9 diverges at the C-terminus (Trp at human
  Cys293 position).

Decisions (17 GOA rows):
- ACCEPT: GO:0036054, GO:0036055, GO:0061697 (IBA + IEA), mitochondrial matrix (IBA),
  cytosol (IBA + IEA).
- MODIFY: mitochondrion (IBA, IEA) -> mitochondrial matrix; histone deacetylase activity,
  NAD-dependent (IBA, deep node) -> the three acidic deacylase activities
  [PMID:22076378 "With all three peptide sequences, the catalytic efficiencies for demalonylation and desuccinylation were much (29 to >1000 fold) higher than that for deacetylation"].
- KEEP_AS_NON_CORE: nucleus (IBA, IEA), zinc ion binding, NAD-dependent protein lysine
  deacetylase activity, NAD+ binding.
- REMOVE: chromatin remodeling (IEA inferred from the deep-node HDAC IBA)
  [PMID:23806337 "SIRT5 deficiency does not significantly impact global Lys acetylation"].
