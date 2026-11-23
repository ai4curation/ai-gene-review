# IRF9 (horse, A0A9L0SN53) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

No earlier review existed; folder created with `just fetch-gene HORSE A0A9L0SN53 --alias IRF9`
(stub id confirmed as A0A9L0SN53). ProtNLM2 output was not consulted.

### Deep research
`just deep-research-falcon HORSE IRF9 --fallback perplexity-lite` failed (falcon and the
perplexity-lite fallback both exited with an error after timeouts). No deep-research file was
produced. Literature was gathered directly from PubMed and cached with `just fetch-pmid`.

### Identity / gene model
- PANTHER PTHR11949:SF26 (INTERFERON REGULATORY FACTOR 9), the same subfamily as human IRF9
  (Q00978) and mouse Irf9 (Q61179) per `interpro/panther/PTHR11949/PTHR11949-entries.csv`.
  Transfer of IRF9-specific function from human/mouse is therefore within-subfamily.
- Five horse UniProt models from one Ensembl gene (ENSECAG00000024429). A0A9L0SN53 is the
  Ensembl canonical transcript and the UniProt gene-centric canonical. F6Z2B0 (445 aa) carries
  the RefSeq XP_005603301.2 xref.
- A0A9L0SN53 (529 aa) = F6Z2B0 + an 84-aa Pro-rich insertion inside the IAD, after human
  residue 330; absent from human, mouse, donkey and the RefSeq-backed horse model
  [file:HORSE/IRF9/IRF9-bioinformatics/RESULTS.md]. Likely an alternative-exon or
  retained-intron model. DBD intact. Pfam splits the IRF-3/IAD domain into two hits.
- Horse-wide (all models) 17-aa insertion after human 216 and 33-aa C-terminal extension.

### Literature (human/mouse IRF9, same PANTHER subfamily)
- ISGF3 gamma (IRF9) is the DNA recognition subunit of ISGF3 [PMID:1630447 "ISGF3 gamma serves as the DNA recognition subunit"].
- Irf9-null mice: type I and II IFN responses impaired, no ISRE binding [PMID:9078371].
- IRF9 IAD binds the STAT2 coiled-coil domain; interface required for ISGF3 function [PMID:29317535].
- Human IRF9 loss-of-function: no ISGF3 formation, impaired antiviral control, severe influenza [PMID:30143481].
- PMID:31217193 (TLR3 deficiency) was returned by a search and cached but is not about IRF9; not cited.

### Decisions
- Core: ISRE (RNA pol II cis-regulatory) DNA binding; Pol II-specific DNA-binding TF activity;
  ISGF3 complex; positive regulation of Pol II transcription; type I IFN signaling.
- General terms (DNA binding, cis-regulatory region binding, ds sequence-specific DNA binding,
  DNA-binding TF activity, regulation of transcription) MODIFY to the specific terms above.
- immune system process (IBA) MODIFY to type I interferon-mediated signaling pathway
  (a descendant), supported by mouse knockout and human LoF evidence.
- DNA-templated transcription: MARK_AS_OVER_ANNOTATED (IRF9 regulates, does not perform, transcription).
- Caveat: ISGF3/IAD-dependent functions are less certain for this particular model because of the
  IAD insertion; recorded in suggested questions/experiments.

### Relative
Human IRF9 (Q00978), same PANTHER subfamily SF26 and a donor at the PAINT nodes; no review in repo
(`genes/human/IRF9` absent). Mouse Irf9 also unreviewed. Donkey IRF9 (genes/EQUAS/IRF9) is the
campaign partner, not used as the relative.
