# TGFBR3 (human, Q03167) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: reviewed as the experimentally characterised reference for the donkey
(EQUAS) TGFBR3 ortholog A0A8C4M6Z6. ProtNLM2 output was not consulted.

### Deep research
`just deep-research-falcon human TGFBR3 --fallback perplexity-lite` failed: falcon
returned "Failed to authenticate" and the perplexity fallback returned HTTP 401
(insufficient quota). No deep-research file exists; the review is based on the cached
publications listed in the review YAML, the UniProt record, PANTHER/PAINT data and
Reactome entries.

### Evolutionary grounding
- PANTHER PTHR14002 (endoglin/TGF-beta receptor type III), subfamily PTHR14002:SF7
  (TGFBR3); endoglin is a separate subfamily, so endoglin-specific functions were not
  transferred.
- PAINT node PTN002678643 (taxon Euteleostomi) IBDs: GO:0005024, GO:0005114,
  GO:0005539, GO:0050431, GO:0001837, GO:0007179, GO:0017015
  (`interpro/panther/PTHR14002/PTHR14002-paint.tsv`). Plasma membrane IBD comes from
  the deeper PTN008553354 node. PAINT did not propagate BMP binding, coreceptor
  activity, inhibin terms or any developmental terms; I read that as deliberate.

### Experimentally established in human
- Type III TGF-beta receptor / ligand presentation and TGFBR2 binding
  [PMID:11323414 "The type III receptor with the cytoplasmic domain deleted is able to bind TGF-beta, to bind the type II receptor, and to enhance TGF-beta binding to the type II receptor"].
- Inhibin coreceptor with ActRII [PMID:10746731 "betaglycan, can function as an inhibin co-receptor with ActRII"].
- BMP binding and BMP signaling [PMID:18184661 "TbetaRIII directly and specifically binds to multiple members of the BMP subfamily, including BMP-2, BMP-4, BMP-7, and GDF-5"]; ALK3/ALK6 [PMID:19726563].
- GIPC1 PDZ binding [PMID:11546783 "GIPC binds a Class I PDZ binding motif in the cytoplasmic domain of the type III receptor"].
- beta-arrestin 2 recruitment after TGFBR2 phosphorylation and endocytosis [PMID:12958365];
  Cdc42 activation and inhibition of migration [PMID:19416857]; NF-kappaB inhibition
  [PMID:19325136]; integrin a5b1 trafficking and FN adhesion [PMID:22562249].

### Inferred from mouse (not human)
- Embryonic lethality with heart/liver defects [PMID:12773577]; coronary vessel
  formation failure [PMID:17704211]; epicardial EMT/invasion via GIPC and
  Par6/Smurf1/RhoA [PMID:21871877, PMID:22033038, PMID:22237159]; inhibin A (not B)
  coreceptor in gonadotropes [PMID:30364975].
- Fine-grained cardiac/hematopoietic/palate ISS terms from mouse knockouts were marked
  as over-annotations (downstream phenotypes, not participation).

### Key decisions
- GO:0005024 rows -> MODIFY to GO:0070123 (GO:0005024 definition implies kinase
  catalysis; betaglycan lacks a kinase domain).
- GAG/heparin binding -> MARK_AS_OVER_ANNOTATED (covalent GAG substitution is not
  GAG binding).
- Protein binding IPIs converted to informative terms (inhibin complex binding, TGF-beta
  binding, PDZ domain binding, arrestin family protein binding); FGFR4 screen hit removed.
- Cytosol (Reactome) removed: signal peptide + type I TM protein.
- Immune response IMP (SNP association) removed.
- NEW: GO:0032926 negative regulation of activin receptor signaling pathway (inhibin
  coreceptor; TGFBR3 itself forms the antagonistic complex).
- NOT JNK/ERK ISS rows and SMAD binding IMP left UNDECIDED (source evidence not
  accessible).
