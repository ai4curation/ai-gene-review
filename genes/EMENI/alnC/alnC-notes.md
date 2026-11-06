# alnC review notes

## 2026-11-01

- Seeded `EMENI/alnC` with 3 current GOA rows for C8VJR5/ANIA_11198.  The
  rows are a UniProtSubCell membrane mapping, the PTHR19370 family-root
  `GO:0016491 oxidoreductase activity` IBA, and the matching InterPro/ARBA
  broad oxidoreductase IEA.
- Cached PMID:30339758 after targeted searches for `alnC`, `AN11198`, and
  `NADH-cytochrome b5 reductase-like protein alnC`.  The direct full-text
  paper activates the silent A. nidulans `aln` cluster, names the cluster
  members, and shows by deletant LC/MS that alnA, alnB, alnC, alnD, alnF,
  alnH, and alnI are all required for (+)-asperlin production.
- `just deep-research-falcon EMENI alnC --fallback perplexity-lite` failed
  because neither the `falcon` provider nor the Perplexity fallback is
  available without `agentapi` on this shell's `PATH`; no provider-authored
  deep-research file was created.
- The search did not turn up a newer paper assigning AlnC's exact
  electron acceptor or reaction within the asperlin pathway.  CAoGDX mirrors
  UniProt's PMID:30339758-backed `alnC` name, but that is database context, not
  a new primary assay.
- AlnC is larger than canonical CBR1/MCR1 proteins, is predicted to have two
  transmembrane regions, and has a cytochrome-b5-like domain in addition to the
  FAD-binding and FNR nucleotide-binding signatures.  It is reasonable to keep
  both GO:0016491 rows as broad oxidoreductase assertions, but not to refine
  them to a cytochrome-b5 reductase term or a Dph3 reductase term.
- The family-root PAINT assertion at `PANTHER:PTN001833551` correctly supports
  only broad oxidoreductase chemistry across the whole family.  A specific
  fungal CBR1/MCR1 IBD would not cover AlnC unless future work shows that
  AlnC carries the same electron acceptor specificity.

## 2026-11-02

- Rechecked PR #5873 feedback against cached PMID:30339758 and the curated
  Swiss-Prot comments.  The paper supports adding a new
  `GO:0030639 polyketide biosynthetic process` proposal because AlnC is named
  among the (+)-asperlin biosynthetic genes and its deletion fully eliminates
  (+)-asperlin production after cluster induction; unlike a substrate case,
  AlnC is a predicted redox enzyme in the aln cluster.
- Refined the author-synthesized core molecular function from
  `GO:0016491 oxidoreductase activity` to the still-conservative
  `GO:0016651 oxidoreductase activity, acting on NAD(P)H`.  The
  cytochrome-b5-like/FAD/FNR domain architecture and UniProt's flavoprotein
  pyridine nucleotide cytochrome reductase family assignment support a
  pyridine-nucleotide donor, but the direct acceptor and aln-cluster substrate
  remain unknown, so `GO:0004128` and `GO:0016653` would still overstate the
  evidence.
