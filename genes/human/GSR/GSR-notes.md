# GSR (Glutathione reductase) — review notes

UniProt: P00390 (GSHR_HUMAN); HGNC:4623; Gene 2936; chromosome 8. EC 1.8.1.7.

## Core biology

GSR is glutathione-disulfide reductase (glutathione reductase, GR/GRase), an
FAD-dependent, NADPH-using homodimeric flavoenzyme of the class-I pyridine
nucleotide-disulfide oxidoreductase family. It reduces oxidized glutathione
(glutathione disulfide, GSSG) back to two molecules of reduced glutathione (GSH)
using NADPH, thereby maintaining the high cellular GSH:GSSG ratio that underpins
antioxidant defense and thiol redox homeostasis.

- Function / catalytic activity:
  [file:human/GSR/GSR-uniprot.txt "Catalyzes the reduction of glutathione disulfide (GSSG) to"]
  ... "reduced glutathione (GSH). Constitutes the major mechanism to maintain"
  ... "a high GSH:GSSG ratio in the cytosol." {ECO:0000269|PubMed:17185460}
- Reaction (Rhea RHEA:11740): 2 glutathione + NADP(+) = glutathione disulfide + NADPH + H(+); EC=1.8.1.7
  [file:human/GSR/GSR-uniprot.txt "Reaction=2 glutathione + NADP(+) = glutathione disulfide + NADPH +"]
- Cofactor FAD, 1 per subunit:
  [file:human/GSR/GSR-uniprot.txt "Note=Binds 1 FAD per subunit."]
- Quaternary structure — homodimer, disulfide-linked:
  [file:human/GSR/GSR-uniprot.txt "SUBUNIT: Homodimer; disulfide-linked."]
- Active site is a redox-active disulfide:
  [file:human/GSR/GSR-uniprot.txt "MISCELLANEOUS: The active site is a redox-active disulfide bond."]
- Domain organization (FAD-binding domain 1, NADPH-binding domain 2, interface domain 4):
  [file:human/GSR/GSR-uniprot.txt "respectively. Domain 4 forms the interface."]
- Family:
  [file:human/GSR/GSR-uniprot.txt "Belongs to the class-I pyridine nucleotide-disulfide"]

## Localization / isoforms

Alternative products (alternative splicing + alternative initiation), 5 named isoforms.
Isoform Mitochondrial (P00390-1, displayed) and Isoform Cytoplasmic (P00390-2, produced by
alternative initiation of the mitochondrial isoform) target the enzyme to mitochondrion
and cytoplasm respectively:
- [file:human/GSR/GSR-uniprot.txt "SUBCELLULAR LOCATION: [Isoform Mitochondrial]: Mitochondrion."]
- [file:human/GSR/GSR-uniprot.txt "SUBCELLULAR LOCATION: [Isoform Cytoplasmic]: Cytoplasm."]
- [file:human/GSR/GSR-uniprot.txt "initiation of isoform Mitochondrial."]
- N-terminal mitochondrial transit peptide (residues 1..43):
  [file:human/GSR/GSR-uniprot.txt "TRANSIT         1..43"]

Reactome places the catalytic activity in both cytosol (R-HSA-71682) and mitochondrial
matrix (R-HSA-3323079). HPA IDA (GO_REF:0000052) supports cytosol localization.
Both localizations are consistent with the dual targeting described in UniProt.

## Disease

Congenital non-spherocytic hemolytic anemia 10 (CNSHA10; MIM:618660), autosomal recessive.
Patients experience hemolytic anemia in response to oxidative stress or ingestion of fava beans (favism).
- [file:human/GSR/GSR-uniprot.txt "experience hemolytic anemia in response to oxidative stress or"]
- Molecular basis: [PMID:17185460 "Owing to a 2246-bp deletion in the patients' DNA, translated GR is
  expected to lack almost the complete dimerization domain, which results in
  unstable and inactive enzyme."] and a G330A substitution (a highly conserved residue in the
  superfamily of NAD(P)H-dependent disulfide reductases) causing impaired thermostability.
  This paper (Kamerbeek et al. 2007, Blood) is the source of the EXP catalytic-activity
  annotation (GO:0004362) and the disease/EC assignment. Cached entry is abstract-only
  (full_text_available: false); the abstract confirms GR catalytic activity assays and the disease link.

## Historical / classic references

- PMID:947404 (Loos et al. 1976, Blood) — familial GR deficiency in human blood cells;
  abstract-only. Basis for the two TAS annotations (GO:0004362 and GO:0009055 electron
  transfer activity). The paper establishes GR deficiency and its clinical manifestation
  (favism, cataracts). Reactome R-HSA-71682 also cites Loos et al. 1976.
- Extensive high-resolution crystal structures with FAD, NADPH and glutathione bound
  (e.g. PDB 3DK9 at 0.95 Å; PMID:18638483 Berkholz et al. 2008), establishing the
  FAD/NADP(P)H/glutathione binding sites listed in the UniProt FT lines.

## Annotation assessment summary

Core molecular functions well supported by structure + biochemistry:
- GO:0004362 glutathione-disulfide reductase (NADPH) activity (EXP PMID:17185460; also TAS/IBA/IEA) — CORE
- GO:0050660 flavin adenine dinucleotide binding (FAD cofactor, 1/subunit; IBA/IEA) — CORE
- GO:0050661 NADP binding (NADPH substrate; IEA InterPro) — CORE (supported by FT NADP(+) binding residues)

Core biological processes:
- GO:0006749 glutathione metabolic process — CORE (regeneration of GSH; note this is
  glutathione RECYCLING, not de-novo glutathione biosynthesis)
- GO:0045454 cell redox homeostasis — CORE

Locations: cytosol (GO:0005829) and mitochondrion (GO:0005739) / mitochondrial matrix
(GO:0005759) are all consistent with the dual (alternative-initiation) targeting.

Over-annotations / non-core (kept, not removed):
- GO:0016491 oxidoreductase activity, GO:0016668 oxidoreductase activity acting on sulfur
  group of donors NAD(P) as acceptor — parent/grouping MF terms subsumed by GO:0004362; MARK_AS_OVER_ANNOTATED.
- GO:0009055 electron transfer activity (TAS PMID:947404) — GR does internal electron
  transfer (NADPH->FAD->disulfide->GSSG) but "electron transfer activity" is the ETC-style
  MF; the specific term GO:0004362 captures the function. MARK_AS_OVER_ANNOTATED (experimental-lineage TAS; not removed).
- GO:0034599 cellular response to oxidative stress — downstream/consequence process; KEEP_AS_NON_CORE.
- GO:0098869 cellular oxidant detoxification — IEA logical inference from GO:0004362; KEEP_AS_NON_CORE.
- GO:0005737 cytoplasm (IEA SubCell) — general parent of cytosol; KEEP_AS_NON_CORE.
- GO:0070062 extracellular exosome (HDA, urinary/prostatic exosome proteomics
  PMID:23533145, PMID:19056867) — high-throughput mass-spec detection in secreted vesicles;
  not a site of GR catalytic function. KEEP_AS_NON_CORE (do not remove HDA).

No annotations were REMOVED (no clearly-wrong IEA present; the two exosome HDA and the
electron-transfer TAS are experimental-lineage and handled with KEEP_AS_NON_CORE /
MARK_AS_OVER_ANNOTATED per policy).
