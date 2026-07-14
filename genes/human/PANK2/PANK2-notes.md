# PANK2 (human) — gene review notes

UniProt: Q9BZ23 (PANK2_HUMAN). Gene: PANK2 (syn. C20orf48). Chromosome 20.
NCBI Gene 80025. HGNC:15894.

## Core identity and function

PANK2 is the **mitochondrial isoform of pantothenate kinase**. It catalyzes the
**first and rate-limiting step of coenzyme A (CoA) biosynthesis**: the
ATP-dependent phosphorylation of pantothenate (vitamin B5) to
(R)-4'-phosphopantothenate. This is a feedback-regulated, committed step.

- EC 2.7.1.33; RHEA:16373: `(R)-pantothenate + ATP = (R)-4'-phosphopantothenate + ADP + H(+)`
  [file:human/PANK2/PANK2-uniprot.txt "Reaction=(R)-pantothenate + ATP = (R)-4'-phosphopantothenate + ADP +"].
- "Mitochondrial isoform that catalyzes the phosphorylation of pantothenate to
  generate 4'-phosphopantothenate in the first and rate-determining step of
  coenzyme A (CoA) synthesis"
  [file:human/PANK2/PANK2-uniprot.txt] (FUNCTION [Isoform 1], ECO:0000269 from
  PubMed:15659606, 16272150, 17242360, 17825826).
- Belongs to the **type II pantothenate kinase family**
  [file:human/PANK2/PANK2-uniprot.txt "Belongs to the type II pantothenate kinase family"].
- Pathway: "Cofactor biosynthesis; coenzyme A biosynthesis; CoA from (R)-pantothenate: step 1/5"
  [file:human/PANK2/PANK2-uniprot.txt].

Kinetics (isoform 1): KM = 25.4 uM for pantothenate, KM = 63.6 uM for ATP
[file:human/PANK2/PANK2-uniprot.txt "KM=25.4 uM for pantothenate"].

Enzyme is a **homodimer** [file:human/PANK2/PANK2-uniprot.txt "Homodimer."].

## Localization

- Mitochondrial. Synthesized as a ~62-kDa precursor with an N-terminal
  mitochondrial transit peptide (residues 1-31), proteolytically processed by
  the mitochondrial-processing peptidase (MPP) via a 59-kDa intermediate to the
  mature 48-kDa protein [file:human/PANK2/PANK2-uniprot.txt "processed by the mitochondrial-processing peptidase (MPP)"].
- PanK2 protein "is localized to mitochondria of neurons in human brain,
  distinguishing it from other pantothenate kinases that do not possess
  mitochondrial-targeting sequences" [PMID:15659606 abstract].
- Mature hPanK2 is in the **mitochondrial intermembrane space (IMS)** —
  demonstrated by digitonin permeabilization / protease-protection in SH-SY5Y
  cells; released with the IMS marker SMAC, not the matrix marker cyclophilin D
  [PMID:23152917 "these data supported the conclusion that the mature hPanK2 protein was located in the IMS of mitochondria"].
  The IMS location is proposed to let PanK2 sense cytosol-derived acylcarnitines
  and export phosphopantothenate to cytosolic downstream CoA enzymes.
- hPanK2 also localizes to the **nucleus** (functional NLS residues 82-94; NES
  268-275). It traffics nucleus→mitochondria (not the reverse) and is absent
  from the nucleus during G2 phase [PMID:23152917]. The nuclear pool is dynamic
  and its catalytic role there is unclear; predominant steady-state location is
  mitochondria.
- **Species caveat**: mouse PanK2 is **cytosolic**; the mitochondrial targeting
  signal was acquired only in primates
  [PMID:17825826 "acquisition of a mitochondrial targeting signal was limited to primates. ... Mouse PanK2 localized in the cytosol"].
  So mouse localization data are NOT transferable to human.
- Cytosol IDA (HPA, GO_REF:0000052): the HPA image records cytosol; likely
  reflects the shorter non-mitochondrial isoforms and/or the nucleocytoplasmic
  shuttling pool. Not the core mitochondrial location.

## Regulation

- Strongly **inhibited by acetyl-CoA / acyl-CoA thioesters** (IC50 250-500 nM;
  <1 uM), a classic feedback loop on the committed CoA-biosynthesis step
  [PMID:16272150 "extremely sensitive to feedback inhibition by CoA thioesters (IC50 values between 250 and 500 nM)"; file:human/PANK2/PANK2-uniprot.txt "Strongly inhibited by acetyl-CoA and"].
- **Activated by palmitoylcarnitine** (long-chain acylcarnitine), which
  competitively antagonizes acetyl-CoA inhibition; proposed to couple CoA
  synthesis to mitochondrial fatty-acid (beta-oxidation) demand
  [PMID:17242360 "Palmitoylcarnitine was discovered to be a potent activator of PanK2 that functions to competitively antagonize acetyl-CoA inhibition"].

## Disease: NBIA1 / PKAN

- Autosomal-recessive **Neurodegeneration with Brain Iron Accumulation type 1
  (NBIA1)** = Pantothenate Kinase-Associated Neurodegeneration (PKAN), formerly
  Hallervorden-Spatz syndrome. Iron accumulation in basal ganglia; dystonia,
  dysarthria, rigidity, pigmentary retinopathy; "eye of the tiger" MRI sign
  [file:human/PANK2/PANK2-uniprot.txt DISEASE block].
- Many missense variants characterized biochemically. The most common,
  **G521R**, is catalytically dead and misfolds; but "nine of the mutant proteins
  associated with disease possessed catalytic activities that were
  indistinguishable from wild type", implying catalytic loss is not the sole
  disease mechanism [PMID:16272150 abstract].
- Global metabolic profiling of PKAN patient plasma/fibroblasts (14 patients)
  found elevated lactate, elevated pantothenate in premature-stop patients, and
  defects in bile-acid conjugation and lipid metabolism — all downstream CoA-
  dependent pathways [PMID:22221393 abstract/full text].

## Notes on specific existing annotations

- **MF GO:0004594 pantothenate kinase activity** — core; supported by EXP/IMP
  from PMID:17825826, 15659606, 16272150, 17242360 (biochemical assays of the
  human enzyme and disease mutants) plus IBA/IEA/TAS. ACCEPT the experimental
  ones as core.
- **GO:0005524 ATP binding (IEA)** — correct; ATP is a cosubstrate. ACCEPT
  (supporting MF, kept as non-core relative to the catalytic activity, but
  standard for a kinase; keep).
- **BP GO:0015937 coenzyme A biosynthetic process** and **GO:0015939 pantothenate
  metabolic process** — core; PANK2 catalyzes step 1/5 of CoA biosynthesis from
  pantothenate. ACCEPT.
- **Localization**: mitochondrion (GO:0005739) and mitochondrial intermembrane
  space (GO:0005758) are core/experimentally supported (PMID:15659606, 23152917,
  Reactome, HTP mito proteome PMID:34800366). Nucleus (GO:0005634) is
  experimentally observed (PMID:23152917) but a dynamic, shuttling minor pool —
  keep as non-core. Cytosol/cytoplasm (GO:0005829/GO:0005737) reflect
  non-mitochondrial isoforms / shuttling; keep as non-core (IDA/EXP) or REMOVE
  the redundant IEA electronic ones.
- **GO:0001525 angiogenesis (IMP, PMID:30221726)** — PANK2 silencing reduces
  HUVEC angiogenesis, but this is a **downstream physiological consequence** of
  reduced CoA availability, not a distinct molecular role. Keep as non-core.
- **GO:0019217 regulation of fatty acid metabolic process** and **GO:0090207
  regulation of triglyceride metabolic process** (IMP, acts_upstream_of,
  PMID:22221393) — these come from metabolic-profiling observations in PKAN
  patients; they are **secondary metabolic consequences** of CoA deficiency
  (CoA is required for lipid metabolism). Over-annotation of a phenotypic
  readout as a regulatory function. MARK_AS_OVER_ANNOTATED (do not REMOVE — IMP).
- **GO:0005515 protein binding (IPI)** x3 (PMID:15161933 14-3-3/YWHAZ;
  PMID:35271311 OpenCell; PMID:32814053 interactome, isoform Q9BZ23-2) — bare
  "protein binding", uninformative. Per policy do NOT remove IPI; mark
  over-annotated. The 14-3-3 (YWHAZ) interaction is consistent with the
  phospho-Ser sites (Ser168/169/189) in the disordered N-terminal region.

## Provenance conventions
UniProt CC lines are wrapped with a `CC       ` prefix; quotes above never span
two wrapped lines. All PMID quotes are verbatim substrings of the cached
`publications/PMID_*.md` files.
</content>
</invoke>
