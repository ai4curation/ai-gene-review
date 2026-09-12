# MMADHC (Cobalamin trafficking protein CblD) — review notes

UniProt: Q9H3L0 (MMAD_HUMAN). Gene MMADHC (a.k.a. C2orf25, cblD). 296 aa, MW ~32.9 kDa.
Predicted N-terminal mitochondrial transit peptide (1..38, ECO:0000255); mature chain 39..296.
Structure solved for C-terminal domain (residues 108-296; PDB 5CUZ/5CV0/6X8Z) — a nitro-FMN
reductase-like fold [PMID:26364851, not cached: "molecular mimicry ... new subfamily of nitro-FMN reductases"].

## Core biology (verified from cached publications + UniProt)

MMADHC is the cblD-complementation-group protein and acts as a **branch-point / adaptor in
intracellular cobalamin (vitamin B12) trafficking**, functioning **downstream of MMACHC (cblC)**
in the cytosol. It is NOT an enzyme (the "-DHC" refers to the disease methylmalonic aciduria and
homocystinuria, not a dehydrogenase).

- Branch point routing MeCbl vs AdoCbl:
  [PMID:22156578 "supporting the role of cblD protein as a branch point in intracellular cobalamin trafficking"];
  "a single protein exists with two different functional domains that interact with either cytosolic or mitochondrial targets";
  sequence after Met116 sufficient for MeCbl (cytosolic MTR branch), sequence between Met62 and Met116 required for AdoCbl (mitochondrial MMUT branch).
- Downstream of MMACHC/CblC; controls partitioning between cytoplasmic (MeCbl/MTR) and mitochondrial (AdoCbl) routes:
  [PMID:23415655 "functions downstream of CblC in the cofactor assimilation pathway"; "an adapter function for CblD"].
- Directs B12 delivery to cytoplasm vs mitochondria — branch point:
  [PMID:23270877 "MMADHC acts as a branch point for vitamin B(12) delivery to the cytoplasm and mitochondria"];
  "MMADHC is both mitochondrial and cytoplasmic".
- Domain / mutation mapping to three cblD phenotypes:
  [PMID:24722857 "specific regions of MMADHC are involved in differential regulation of AdoCbl and MeCbl synthesis"].
  Null N-terminal to Met116 → isolated MMA (cblD-MMA, AdoCbl deficiency, MACD MIM:620953);
  null across C-terminus (p.Y140-R250) → combined MMA/HC (MAHCD MIM:277410);
  missense in conserved C-terminal region (p.D246-L259) → isolated HC (cblD-HC/HMAD MIM:620952, MeCbl deficiency).

## Molecular interactions

- Physical heterodimer with MMACHC/CblC (SPR + bacterial two-hybrid):
  [PMID:21071249 "MMADHC was confirmed as a binding partner for MMACHC both in vitro (SPR) and in vivo (bacterial two-hybrid system)"].
- Multiprotein cytosolic complex with MMACHC, MTR (methionine synthase), MTRR (MSR):
  [PMID:27771510 "processing of Cbl in cytoplasm occurs in a multiprotein complex composed of at least MS, MSR, MMACHC and MMADHC"];
  novel interactions "MS with MMADHC".
- Interprotein Co-S coordination: CblD donates a Cys-261 thiolate ligand to cob(II)alamin bound to CblC:
  [PMID:32871076 "CblD provides a sulfur ligand to cob(II)alamin bound to CblC"; "Cys-261 on CblD as the sulfur donor"].
  (UniProt FUNCTION: "Promotes oxidation of cob(II)alamin bound to MMACHC", PMID:26364851.)

## Localization

- Cytosol (IDA): [PMID:23270877]. Also mitochondrion (IDA + HTP mito proteome PMID:34800366; UniProt SUBCELLULAR LOCATION Cytoplasm + Mitochondrion).
  The cytosol is where the branch-point adaptor activity occurs (in complex with MMACHC/MTR/MTRR).

## GOA molecular function

GOA carries **GO:0140104 molecular carrier activity** (IBA + multiple IDA/EXP/TAS from Reactome & primary
papers) as the F-aspect term — this is the "carries/hands-off cobalamin" adaptor activity, NOT an enzyme
activity. There is no catalytic/EC term in GOA and none should be invented. Retain molecular carrier activity
as the MF for core_functions.

The IPI "protein binding" (GO:0005515) annotations (PMID:32296183 HuRI high-throughput Y2H hits: CINP,
CREB5, POU4F2, TBC1D7; PMID:27771510 MTR/MTRR/MMACHC; PMID:23415655 MMACHC) are uninformative bare
protein-binding — mark as over-annotated per curation policy (do NOT REMOVE experimental IPIs), noting the
biologically meaningful partners (MMACHC, MTR, MTRR) are captured by the molecular carrier activity + BP terms.

## Reference for file: quote
Add file:human/MMADHC/MMADHC-uniprot.txt to references for the UniProt FUNCTION/SUBCELLULAR quote support.
