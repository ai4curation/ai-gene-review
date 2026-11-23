# mup-4 (Q21281) review notes

Deep research was skipped: falcon times out in this environment and perplexity-lite is unavailable.
This review relies on cached publications. PMID:25692704 is abstract-only in the cache.

- Single-pass transmembrane receptor with EGF-like repeats, a vWFA domain, two SEA modules and a
  filaggrin-like cytoplasmic domain. It is located at apical hemidesmosomes [PMID:11470827 "MUP-4 colocalizes with epithelial hemidesmosomes overlying body wall muscles"].
- Mutants detach the apical epidermis from the cuticle [PMID:11470827 "In contrast, all mup-4 mutants (n = 14) showed a lesion between the apical hypodermal membrane and the cuticle."].
- MUP-4 sequesters STA-2 and releases it when the epidermis is damaged [PMID:37759445 "MUP-4 exerts immune surveillance function through binding and sequestering STA-2 under normal conditions and releasing STA-2 to induce AMPs upon apical structural damage"].
- BLI-1 as the MUP-4 ligand is presumptive [PMID:37759445 "However, the direct binding between BLI-1 and MUP-4 requires biochemical methods for further validation."].

Decisions:
- Fibrillin-derived IBAs (ECM structural constituent, extracellular matrix): marked as over-annotated.
  MUP-4 is a transmembrane receptor, not a secreted matrix protein.
- Protein binding (IPI with STA-2): MODIFY to GO:0097677 STAT family protein binding.
- NEW terms: GO:0007160 cell-matrix adhesion (comparator: MUA-3 has it by IMP from PMID:11470828),
  GO:0098631 cell adhesion mediator activity, and GO:0140311 protein sequestering activity.
