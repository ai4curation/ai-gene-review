# Q9RSY6 (DR_1983, bS1/RpsA) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 prediction files were not opened or used.

### Identity
- Q9RSY6 is the full-length, sole bS1 product of DR_1983 (629 aa, TrEMBL, PE 3).
  Not an isoform, fragment or alternative gene model: it carries five complete
  PROSITE S1 domains (122-539), a disordered polar N-terminal extension (1-100)
  and a disordered Gly-rich C-terminal tail (540-589). E. coli bS1 is 557 aa
  with six domains (D1-D6); the Deinococcus protein has the extra N-terminal
  extension.
- PANTHER: PTHR10724:SF7 ("SMALL RIBOSOMAL SUBUNIT PROTEIN BS1C"). E. coli RpsA
  P0AG67 is in the same subfamily (interpro/panther/PTHR10724/PTHR10724-entries.csv),
  so transfer of the bS1 core functions is within-subfamily.
- PAINT (interpro/panther/PTHR10724/PTHR10724-paint.tsv): PTN000076677 carries
  mRNA binding, structural constituent of ribosome, translation; PTN000076734
  (taxon:2) carries cytosolic small ribosomal subunit; PTN000076722 cytosol is
  restricted to Proteobacteria (taxon:1224) and so not propagated to Deinococcus.
  E. coli RpsA experimental terms NOT propagated by PAINT (treated as deliberate):
  ribosomal small subunit assembly (GO:0000028), single-stranded RNA binding,
  negative regulation of translation terms (GO:2000766, autoregulation, which
  [PMID:38474204 "which are highly conserved in several families of γ-proteobacteria"]),
  no translational initiation term on E. coli either.

### D. radiodurans-specific evidence
- [PMID:35856907 "all four proteins exhibited higher binding affinity to the 8-oxoG-containing oligoribonucleotide than the control oligoribonucleotide"]
  but Kd for RpsA ~1.7 uM, much weaker than PNPase/RhlB.
- [PMID:35856907 "deletion of these proteins could not be achieved, likely due to their critical roles for cell viability in D. radiodurans"]
- [PMID:35856907 "RpsA (the ribosomal protein S1) was also found to interact with PNPase in D. radiodurans in an RNA-independent fashion"]
- Not used for a NEW annotation: oxidized-RNA preference is modest, and
  "RNA binding" would be an ancestor of the accepted mRNA binding.

### Decisions
- mRNA binding (IBA, IEA): ACCEPT. Structural constituent of ribosome, translation,
  cytosolic small ribosomal subunit (IBA): ACCEPT.
- nucleic acid binding (IEA, InterPro2GO): changed MARK_AS_OVER_ANNOTATED -> MODIFY
  to mRNA binding (correct but general).
- cytoplasm (IEA, ARBA): changed KEEP_AS_NON_CORE -> MODIFY to cytosolic small
  ribosomal subunit (correct but general).
- Replaced all supporting quotes that cited ARBA keywords or DE protein names
  with literature (PMID:38474204, PMID:35856907, PMID:9451450) and family
  signatures (PANTHER SF7, IPR050437, PRINTS, Pfam).
- No NEW terms. Translational initiation is mechanistically apt but neither PAINT
  nor GOA for E. coli RpsA carries it; raised as a suggested question.

### Relative
- E. coli rpsA (P0AG67), same PANTHER subfamily SF7, PAINT donor. No review in repo
  (no genes/ECOLI/rpsA). Webster et al. 2024 (PMID:39607923) could not be cached.
- Modules: none contain bS1 as a part; modules/bacterial_translation_initiation.yaml
  is the closest related module (IF1/IF2/IF3 only).
