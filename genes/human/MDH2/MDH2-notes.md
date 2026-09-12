# MDH2 (human) — gene review notes

UniProt: P40926 (MDHM_HUMAN). HGNC:6971. Gene on chromosome 7. 338 aa precursor
(N-terminal 1–24 mitochondrial transit peptide; mature chain 25–338).

## Core biology (authoritative: UniProt P40926)

MDH2 is the **mitochondrial (NAD-dependent) malate dehydrogenase**. It catalyzes
the reversible oxidation of L-malate to oxaloacetate with reduction of NAD+ to NADH.

- EC 1.1.1.37 [file:human/MDH2/MDH2-uniprot.txt "EC=1.1.1.37"].
- Catalytic reaction: [file:human/MDH2/MDH2-uniprot.txt "Reaction=(S)-malate + NAD(+) = oxaloacetate + NADH + H(+)"]
  (Rhea:21432; ECO:0000269|PubMed:27989324).
- FUNCTION (UniProt): [file:human/MDH2/MDH2-uniprot.txt "Mitochondrial malate dehydrogenase that catalyzes the"]
  ... "reversible conversion of malate to oxaloacetate using NAD(+) as a cofactor (PubMed:27989324)".
- Central role in TCA cycle: [file:human/MDH2/MDH2-uniprot.txt "Plays a central role in the tricarboxylic"]
  ("acid (TCA) cycle contributing to cellular respiration and energy production via the
  mitochondrial electron transport chain (PubMed:35366151)").
- Malate-aspartate shuttle: [file:human/MDH2/MDH2-uniprot.txt "Also participates in the malate-aspartate NADH"]
  ("shuttle, facilitating transfer of reducing equivalents between cytosol and mitochondria to
  maintain redox balance (NAD(+)/NADH homeostasis)...").
- Subunit: **Homodimer** [file:human/MDH2/MDH2-uniprot.txt "SUBUNIT: Homodimer. Interacts with GATD3"].
- Subcellular location: **Mitochondrion matrix** [file:human/MDH2/MDH2-uniprot.txt "SUBCELLULAR LOCATION: Mitochondrion matrix"].
- Family: LDH/MDH superfamily, MDH type 1 family [file:human/MDH2/MDH2-uniprot.txt "Belongs to the LDH/MDH superfamily. MDH type 1 family"].
- Structural genomics X-ray structures (2DFD, 4WLE etc.) of residues 20-338 in complex with
  NAD and substrate; classic NAD(P)-binding Rossmann fold + LDH/MDH C-terminal domain.

## Disease

Bi-allelic loss-of-function mutations cause **developmental and epileptic
encephalopathy 51 (DEE51; MIM:617339)**, autosomal recessive
[file:human/MDH2/MDH2-uniprot.txt "Developmental and epileptic encephalopathy 51 (DEE51)"].
Also a pheochromocytoma/paraganglioma susceptibility gene (Orphanet 29072).

Primary paper PMID:27989324 (Ait-El-Mkadem 2017, Am J Hum Genet, FULL TEXT available):
- MDH2 "is essential for the conversion of malate to oxaloacetate as part of the proper
  functioning of the Krebs cycle" [PMID:27989324].
- Patient fibroblasts: "an apparently complete loss of MDH2 levels and MDH2 enzymatic
  activity close to null" [PMID:27989324]; malate + fumarate accumulate; lentiviral WT
  MDH2 cDNA "restored MDH2 levels and mitochondrial MDH activity".
- "MDH2 plays an essential role in the malate-aspartate NADH shuttle, which is the main
  pathway whereby reducing equivalents from cytosolic NADH are transferred to mitochondria"
  [PMID:27989324].
- Variants Gly37Arg (NAD pocket), Pro133Leu, Pro207Leu characterized; DEE51 variants show
  "severe defects in aerobic respiration, when assayed in a heterologous system"
  [file:human/MDH2/MDH2-uniprot.txt] (yeast mdh1Δ complementation). This is the basis of the
  GO:0009060 aerobic respiration IDA and GO:0030060 IDA (PMID:27989324).

## Malate-aspartate shuttle functional evidence

PMID:37647199 (Broeks 2023, Cell Rep, abstract-only in cache): generated MAS-deficient HEK293
cell lines "genetically disrupted each MAS component"; MDH2-deficient cells were among the panel
("MDH2-deficient cells are less affected" than MDH1-deficient). Supports MDH2 involvement in
malate-aspartate shuttle (GO:0043490 IMP) and, indirectly, TCA cycle (GO:0006099 IMP). MDH2 is a
core MAS enzyme (mitochondrial arm). Note: MDH2-deficient cells "less affected" than MDH1 —
consistent with MDH2 being the mitochondrial MAS enzyme; still a bona fide MAS component.

## Moonlighting RNA binding (well-supported, non-core)

PMID:38609156 (Noble/Hentze 2024, RNA, FULL TEXT): MDH2 binds RNA in cells (PNK + 2C assays,
eCLIP). "MDH2 preferentially binds cytosolic over mitochondrial RNAs"; 524 binding regions across
361 RNAs; prefers tRNAs (e.g. Arg TCT, Lys TTT), also mRNAs/lincRNAs/rRNAs. "mitochondrial
targeting is dispensable for MDH2-RNA interactions"; RNA binding uses the NAD+-binding Rossmann
fold and increases when NAD+ is depleted (FK866). Physiological role "as yet unidentified".
This is a genuine moonlighting activity (GO:0003723 RNA binding IDA/HDA) but NOT the core
metabolic function → KEEP_AS_NON_CORE.
Large-scale RNA-interactome captures also annotate GO:0003723 (PMID:22658674, PMID:22681889, HDA).

## PTM / regulation (context, from UniProt)

- Acetylation enhances activity [file:human/MDH2/MDH2-uniprot.txt "Enzyme activity is enhanced by acetylation"]
  (PubMed:20167786); deacetylation by SIRT3 decreases activity.
- Palmitoylation at Cys-138 by ZDHHC18 increases activity / modulates mitochondrial respiration
  (PubMed:35366151).
- Numerous acetyl/succinyl/malonyl-lysine, phospho-Ser sites (large-scale proteomics).

## Localization annotations — assessment

- Mitochondrion / mitochondrial matrix: strongly supported (UniProt SUBCELLULAR LOCATION, IDA
  PMID:38609156, HTP PMID:34800366 mito proteome, multiple Reactome TAS, IBA). Core CC =
  mitochondrial matrix (GO:0005759).
- cytoplasm (GO:0005737, IBA): the mature enzyme is matrix; however MDH2 is synthesized as a
  cytosolic preprotein and the RNA-binding pool is cytosolic (PMID:38609156). IBA to broad
  "cytoplasm" is defensible as non-core but not the primary location → KEEP_AS_NON_CORE.
- nucleus (GO:0005634, HDA PMID:21630459, sperm nucleus proteomics): likely contamination /
  over-annotation of a proteomics dataset; not the enzyme's site of action →
  MARK_AS_OVER_ANNOTATED.
- extracellular exosome (GO:0070062, HDA x3): abundant mitochondrial matrix enzyme recurrently
  detected in exosome/secretome proteomics; not a functional secreted localization →
  MARK_AS_OVER_ANNOTATED.
- membrane (GO:0016020, IEA GO_REF:0000107 from Ensembl/P08249): MDH2 is a soluble matrix enzyme,
  not a membrane protein; the transferred term is a generic mis-transfer → REMOVE (clearly-wrong IEA).

## Molecular-function annotations — assessment

- GO:0030060 L-malate dehydrogenase (NAD+) activity — CORE MF. Supported IDA (PMID:16740313,
  PMID:27989324), IMP (PMID:6576816), EXP (Reactome via PMID:16740313), IBA. ACCEPT.
- GO:0016615 malate dehydrogenase activity (IEA) — parent of the specific NAD+ term; less precise
  → MODIFY to GO:0030060.
- GO:0003824 catalytic activity; GO:0016491 oxidoreductase activity; GO:0016616 oxidoreductase
  acting on CH-OH ... NAD(P) — all IEA root/broad ancestors of GO:0030060; over-general →
  MARK_AS_OVER_ANNOTATED.
- GO:0046554 L-malate dehydrogenase (NADP+) activity (IEA, Ensembl from P08249) — MDH2 is
  NAD-dependent (EC 1.1.1.37), not NADP. NADP+ activity is not a documented MDH2 function; this is
  an incorrect ortholog transfer → REMOVE (clearly-wrong IEA).
- GO:0042802 identical protein binding (IEA, Ensembl) — MDH2 is a homodimer
  [file:human/MDH2/MDH2-uniprot.txt "SUBUNIT: Homodimer"], so self-association is real; keep as
  non-core (not the informative MF). KEEP_AS_NON_CORE.
- GO:0003723 RNA binding — real moonlighting activity (see above). KEEP_AS_NON_CORE.

## Biological-process annotations — assessment

- GO:0006099 tricarboxylic acid cycle — CORE BP (IBA, IEA, TAS Reactome, IMP). ACCEPT the
  experimental/TAS; the IEA duplicates are redundant but not wrong.
- GO:0043490 malate-aspartate shuttle — CORE BP (TAS Reactome, IMP PMID:37647199). ACCEPT.
- GO:0006108 malate metabolic process — true but a general parent of the specific processes; keep
  as non-core. KEEP_AS_NON_CORE.
- GO:0009060 aerobic respiration (IDA PMID:27989324) — MDH2 loss impairs respiration; the DEE51
  variants show "severe defects in aerobic respiration" in a heterologous assay. Legitimate but
  downstream/broad relative to the TCA-cycle role. KEEP_AS_NON_CORE.

## Core functions (summary)

1. MF GO:0030060 L-malate dehydrogenase (NAD+) activity — in mitochondrial matrix (GO:0005759).
2. BP GO:0006099 tricarboxylic acid cycle.
3. BP GO:0043490 malate-aspartate shuttle.
</content>
</invoke>
