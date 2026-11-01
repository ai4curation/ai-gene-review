# ATG4C (horse, A0A3Q2H6C4) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

New folder created with `just fetch-gene HORSE A0A3Q2H6C4 --alias ATG4C`; stub id confirmed as A0A3Q2H6C4
(TrEMBL, PE 3, Ensembl ENSECAP00000029390.2, VGNC:15624). ProtNLM2 output was not opened or used.

### Deep research
`just deep-research-falcon HORSE ATG4C --fallback perplexity-lite` failed: falcon and the perplexity-lite fallback
both exited with errors and no deep-research file was written. The review therefore rests on the cached
publications PMID:21177865, PMID:29458288 and PMID:33773106 (all abstract-only in the cache), the curated
Swiss-Prot record of human ATG4C (Q96DT6), and my own sequence analysis.

### Identity: aberrant gene model
- The horse product is 666 aa; human ATG4C (Q96DT6) and donkey ATG4C (A0A9L0IIU3) are 458 aa.
- Residues 1-400 are 90-100% identical to human per 50-residue window; identity collapses after ~403, and horse
  404-666 has no significant similarity to the human tail 404-458 (local score 27.5)
  [file:HORSE/ATG4C/ATG4C-bioinformatics/RESULTS.md].
- The catalytic triad C111/D345/H347 is conserved and the Pfam Peptidase C54 domain (77-398) is intact.
- The C-terminal extension is Pro-rich (SPPR repeats) and Gly-rich, disordered by MobiDB-lite. With a full-length,
  colinear donkey ortholog in the same genus, this is most likely an Ensembl last-exon model error. The canonical
  horse ATG4C product is not in UniProt as a separate entry (this is the only horse entry), so there is no separate
  canonical accession to review.

### Evolutionary placement
UniProt places A0A3Q2H6C4 in PANTHER PTHR22624:SF38 (CYSTEINE PROTEASE ATG4C), the same subfamily as human Q96DT6
and mouse Q811C2 (interpro/panther/PTHR22624/PTHR22624-entries.csv). There is no family review under
interpro/panther/PTHR22624/ (only entries and metadata), so no placement disagreement to report. The IBA rows come
from PAINT node PTN002503342 (the whole ATG4 family, including yeast Atg4). Horse is a PAINT reference proteome here,
so the rows are true IBAs, unlike the donkey TreeGrafter rows.

### Human ATG4C biology (the subfamily's characterised member)
- Weak priming: "whereas Atg4C and Atg4D had minimal activities as did the catalytic mutant of Atg4B (C74S)"
  [PMID:21177865].
- Delipidation comparable across paralogs: "all 4 ATG4 proteases can be activated to similar enzymatic activities
  on lipid-attached substrates" [PMID:29458288].
- Mitophagy: the human Swiss-Prot entry says ATG4C is "weakly or not involved in phagophore growth during
  mitophagy" (PMID:33773106).

### Decisions
- Accept MF cysteine-type endopeptidase activity and protein-PE deconjugating activity, BP autophagosome assembly and
  protein processing, CC cytoplasm. The catalytic domain these rest on is intact in this model.
- Refine the general terms (cysteine-type peptidase activity, proteolysis, autophagy) to the specific terms the gene
  already carries.
- Mitophagy and piecemeal microautophagy of the nucleus: marked over-annotated (consistent with the donkey review).
  Aggrephagy: non-core.

### Relative
Human ATG4C (Q96DT6), same PANTHER subfamily SF38, carries the experimental evidence. There is no review of human
ATG4C in the repo (genes/human/ has ATG4D only), so it is the relative to review next.
Modules: modules/metazoan_autophagosome_biogenesis.yaml (ATG4 priming step, family-level grounding);
modules/dmel_autophagosome_biogenesis.yaml (fly analogue).
