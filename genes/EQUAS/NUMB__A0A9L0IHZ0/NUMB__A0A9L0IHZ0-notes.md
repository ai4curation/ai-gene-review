# NUMB (donkey, A0A9L0IHZ0) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Target: A0A9L0IHZ0, the UniProt gene-centric canonical product (652 aa) of donkey NUMB
(Ensembl ENSEASG00005004756, proteome UP000694387). Folder name `NUMB__A0A9L0IHZ0` because
`genes/EQUAS/NUMB` already holds the review of the 506-aa isoform product A0A9L0IQ95. No ProtNLM2
output was opened or used.

### Deep research
`just deep-research EQUAS NUMB__A0A9L0IHZ0 --provider falcon` failed (`Exception: Failed to
authenticate` from the Edison client). Review continued from cached literature
(publications/) and UniProt records for human P49757 and mouse Q9QZS3.

### Evolutionary grounding
- PANTHER: donkey A0A9L0IHZ0 is in PTHR47368:SF5 (PROTEIN NUMB HOMOLOG) with human P49757 and mouse
  Q9QZS3; NUMBL orthologs are SF4 and Drosophila numb is SF2 (file:EQUAS/NUMB__A0A9L0IHZ0/NUMB__A0A9L0IHZ0-bioinformatics/RESULTS.md).
- Global alignment: 96.92% identity to human canonical NUMB over 650 residues, end-to-end (isoform-1-like
  exon content), 94.17% to mouse. Human Thr-102 (AAK1 site) conserved at donkey 102; C-terminal DPF/NPF
  motifs at equivalent positions.
- PAINT: human P49757 carries IBA for cytoplasm, cytoplasmic vesicle, basolateral plasma membrane
  (UniProt DR GO lines, GO_Central). Donkey receives these via TreeGrafter (PTN001342999). Endocytic
  terms (clathrin-coated pit, endosome, regulation of endocytosis) were NOT propagated at the PAINT node;
  treated as a deliberate decision, so the endocytosis NEW below is an ortholog (ISS) transfer, not an
  inherited family-level claim.
- All Ensembl Compara (GO_REF:0000107) rows come from 1:1 orthologs in the same subfamily.

### Experimental evidence (none in donkey; all mouse/human)
- Human NUMB: endocytic protein at clathrin-coated pits, regulated by AAK1 phosphorylation at Thr-102;
  T102A disrupts transferrin and LDL uptake [PMID:18657069 "Numb is an endocytic protein that is proposed
  to influence clathrin-coated pit assembly"].
- Human HeLa: Numb depletion raises surface integrin alpha5; Numb at clathrin-coated structures near
  leading edge; removal inhibits migration [PMID:19581412 "Removal of Numb also inhibited migration,
  although to a lesser extent than removing Dab2"].
- Mouse radial glia: Numb on adherens-junction-associated vesicles, binds cadherins, needed for basolateral
  cadherin insertion [PMID:17589506 "Numb accumulates in the apical end-feet, where it localizes to adherens
  junction-associated vesicles and interacts with cadherins"].
- Mouse neurogenesis: Numb/Numbl redundantly maintain neural progenitors [PMID:12410312].
- Mouse postnatal SVZ: Numb/Numbl deletion damages lateral ventricle wall and reduces neuroblast
  survival [PMID:17174898 "identified roles for Numb/Numblike in regulating ependymal wall integrity and SVZ
  neuroblast survival"]. The full text reports apoptosis/survival defects, not division defects, so the
  "neuroblast division in subventricular zone" row is judged over-annotated; "lateral ventricle development"
  is a tissue-level outcome of a conditional double knockout (downstream phenotype).
- Mouse Purkinje cells: Numb needed for mGlu1 internalization and recycling at parallel fibre synapses
  [PMID:26621723].
- Mouse: Numb at clathrin-coated pits co-localizing with Stonin1 [PMID:26437238 "Numb, a specific adaptor
  for β1-integrin endocytosis at disassembling FAs"].

### Decisions summary
Core: endocytic adaptor regulating clathrin-dependent endocytosis (NEW GO:2000369, ISS from human), at
plasma membrane / clathrin-coated pit / clathrin-coated vesicle / early endosome; cadherin binding in
basolateral cadherin delivery. Non-core: neurogenesis, catenin binding, cell migration, synaptic
receptor internalization, apical localization. Over-annotated: lateral ventricle development, neuroblast
division in SVZ. Consistent with the sibling review of the isoform product (genes/EQUAS/NUMB).
