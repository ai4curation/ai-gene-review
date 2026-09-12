# PYGL (Glycogen phosphorylase, liver form) — review notes

UniProt: P06737 (PYGL_HUMAN), 847 aa, HGNC:9725, chromosome 14. EC 2.4.1.1.

## Core biology (from UniProt P06737 + literature)

- PYGL is the **liver isoform of glycogen phosphorylase**, the rate-limiting enzyme
  of glycogenolysis. Homodimer; uses a **pyridoxal-5'-phosphate (PLP)** cofactor
  covalently bound at Lys681 (`FT MOD_RES 681 N6-(pyridoxal phosphate)lysine`).
- Reaction (RHEA:41732, EC 2.4.1.1): `[(1->4)-alpha-D-glucosyl](n) + phosphate =
  [(1->4)-alpha-D-glucosyl](n-1) + alpha-D-glucose 1-phosphate`. Phosphorolyses
  alpha-1,4 glycosidic bonds at glycogen non-reducing ends, releasing
  glucose-1-phosphate; stops ~4 residues short of alpha-1,6 branch points (then AGL
  debranches). [PMID:22225877 "catalyzes phosphorolytic cleavage of glycogen to produce glucose-1-phosphate"]
- Allosterically **activated by AMP** (BINDING 43-45, 76, 310) and **inhibited by ATP,
  ADP and glucose-6-phosphate** (UniProt ACTIVITY REGULATION). Covalent activation:
  phosphorylase kinase (PHK) phosphorylates Ser15, converting inactive **b** form to
  active **a** form; PP1 dephosphorylation inactivates it. [PMID:10949035; PMID:22225877]
- PMID:22225877 (Zhang 2012, full text): acetylation at K470/K796 negatively regulates
  GP by recruiting PP1 via PPP1R3B/G_L; measured catalytic activity of purified human
  GP; establishes EC 2.4.1.1 catalytic activity and PPP1R3B interaction. This is the
  experimental basis for the EXP/IDA `glycogen phosphorylase activity` and
  `1,4-alpha-oligoglucan phosphorylase activity` annotations.
- Subcellular location: **Cytoplasm, cytosol** (UniProt; ECO:0000305|PubMed:22225877).

## Disease

- **Glycogen storage disease type VI (GSD6 / Hers disease; MIM:232700)**: liver GP
  deficiency → mild-to-moderate fasting hypoglycemia, mild ketosis, growth retardation,
  prominent hepatomegaly; heart and skeletal muscle spared. Predominantly missense
  mutations affecting enzyme activity. [PMID:9529348; PMID:17705025]

## Annotation review reasoning

- Core MF: **GO:0008184 glycogen phosphorylase activity** (IBA/IDA/IMP/EXP all
  converge). GO:0004645 (1,4-alpha-oligoglucan phosphorylase activity) is the
  parent/EC-mapped term; ACCEPT (EXP-backed by PMID:22225877; IEA is EC/InterPro).
- Core BP: **GO:0005980 glycogen catabolic process** (IBA) — the precise process;
  GO:0005977 glycogen metabolic process and GO:0005975 carbohydrate metabolic process
  are correct-but-general parents (KEEP_AS_NON_CORE / accept as broad IEA).
- Core CC: **GO:0005829 cytosol** (IBA + IEA + Reactome TAS).
- Cofactor: **GO:0030170 pyridoxal phosphate binding** (IEA/InterPro) — ACCEPT; PLP is
  the essential covalent cofactor (Lys681).
- Ligand-binding IDA terms (D-glucose, AMP, ATP, purine nucleobase, vitamin, bile acid
  binding) come from crystallography of allosteric/inhibitor sites (PMID:10980448,
  PMID:12204691, PMID:10949035; all abstract-only in cache). These are structurally
  real but represent binding at allosteric/drug-discovery sites rather than the core
  catalytic function; AMP binding is the physiological allosteric activator (core-ish),
  while `vitamin binding`, `bile acid binding`, `purine nucleobase binding` are generic/
  drug-screen-derived → MARK_AS_OVER_ANNOTATED. Defer to curator on full text (can't
  REMOVE experimental annotations without reading full text).
- `protein binding` (GO:0005515) IPIs (PMID:25416956, 25910212, 32296183, 33961781):
  large-scale interactome maps; with/from = PYGB (P11216), PYGM (P11217) — glycogen
  phosphorylase isoform homo/hetero association. Per policy: bare protein binding →
  MARK_AS_OVER_ANNOTATED (uninformative), not REMOVE.
- `identical protein binding` (GO:0042802, IPI, PMID:10980448, with/from P06737):
  homodimer — biologically real (UniProt SUBUNIT: Homodimer). ACCEPT.
- Extracellular / secretory granule / ficolin granule / exosome localizations
  (GO:0005576, GO:0034774, GO:1904813, GO:0070062): from Reactome neutrophil
  degranulation module (TAS) and a prostate-exosome proteomics screen (HDA,
  PMID:23533145). PYGL is a cytosolic enzyme; these are bystander/secretome-catalog
  localizations, not sites of function → MARK_AS_OVER_ANNOTATED.
- `glucose homeostasis` (GO:0042593, IMP, PMID:17705025): GSD6 phenotype (fasting
  hypoglycemia) supports an organismal glucose-homeostasis role; KEEP_AS_NON_CORE
  (systemic/physiological, downstream of the core enzymatic function).
</content>
</invoke>
