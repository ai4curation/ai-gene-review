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

## 2026-10-18 — ORGANELLES pilot: mitochondrial sub-compartment

Applied projects/ORGANELLES.md Policy to the four GO:0005739 rows. Question: is the
mitochondrial pool of MMADHC in the matrix (GO:0005759)? Lines of evidence:

1. **MTS, no TM segment.** UniProt TRANSIT 1..38 (ECO:0000255), no TRANSMEM feature;
   [PMID:18385497 "a putative mitochondrial targeting"];
   [PMID:42709793 "Human MMADHC has an N-terminal mitochondrial targeting sequence (MTS)"].
   The MTS-less deltaN38 variant [PMID:42709793 "was localized almost exclusively in the cytosol"].
2. **PMF-dependent import** (presequence pathway across the inner membrane):
   [PMID:42709793 "its short half-life is driven by its continual import into energized mitochondria and degradation by LONP1"];
   accumulates in the cytosol upon depolarization.
3. **Matrix protease turnover.** LONP1 inhibition enriches MMADHC in the mitochondrial fraction:
   [PMID:42709793 "consistent with MMADHC being degraded primarily by LONP1 in the mitochondrial matrix"].
   In mouse HSCs the m-AAA protease Afg3l2 also turns it over:
   [PMID:41411131 "Loss of Afg3l2 leads to Mmadhc accumulation"] (abstract only).
4. **Function on the matrix side.** The mitochondrial branch feeds the AdoCbl pathway
   (MMAB, MMUT); MMUT [file:human/MMUT/MMUT-uniprot.txt "Mitochondrion matrix {ECO:0000269|PubMed:24458}."].

Caveat: no sub-mitochondrial fractionation or protease-protection assay exists for MMADHC
(PMID:23270877 is abstract-only here: IF + subcellular fractionation; PMID:42709793 used
crude mitochondria). Matrix is therefore a curator inference (IC). Four lines agree, so
policy rule 4 applies.

Changes: IBA (GO_REF:0000033; PAINT PTN008546602 seeded only by Q9H3L0's own root
annotation) and IEA (GO_REF:0000044, SL-0173) KEEP_AS_NON_CORE -> MODIFY to GO:0005759;
HTP (PMID:34800366) and IDA (PMID:23270877) stay KEEP_AS_NON_CORE with reasons noting the
assays resolve only the organelle; NEW IC GO:0005759 row; core_functions locations now
cytosol + mitochondrial matrix (the single branch-point core function spans both pools).
Expected validator warning: mixed actions on GO:0005739 (policy-driven: direct vs synthesis rows). (Superseded 2026-10-18: the synthesis rows are no longer MODIFYed, so this warning no longer occurs.)

## 2026-10-18 (ORGANELLES revision)

After the PR #5208 review, the IBA/IEA mitochondrion rows are kept (not MODIFYed to the matrix): their sources correctly assert the organelle and could not resolve further. The mitochondrial matrix stays as the NEW IC row, added alongside the root rows as GO does for DARS2 and MMUT.

## 2026-10-18 (core-function location, after OpenScientist)

Question put to OpenScientist: does the mitochondrial pool perform part of the core
AdoCbl-supply function in the matrix, or is the decisive activity cytosolic? Report:
`MMADHC-hypotheses/mmadhc-mitochondrial-pool-adocbl/openscientist.md`. Verdict "partially
supported": the matrix location is well supported, the matrix-side function is unresolved
[file:human/MMADHC/MMADHC-hypotheses/mmadhc-mitochondrial-pool-adocbl/openscientist.md "No
direct physical interaction between MMADHC and any mitochondrial cobalamin enzyme (MMAB,
MMUT, MMAA) has been demonstrated in any assay."]. Checked its key citations:
[PMID:24722857 "null mutations N-terminal to Met116 cause isolated"] and [PMID:26364851 "the
globular C-terminal domain of human CblD, which is sufficient for its"]. It missed the
mouse Afg3l2 paper, which links mitochondrial Mmadhc accumulation to increased AdoCbl
[PMID:41411131 "Loss of Afg3l2 leads to Mmadhc accumulation, driving excessive"].

Decision: the mitochondrial pool matters for the AdoCbl branch, but where its molecular
step happens is unknown. So the matrix stays on the NEW location row and is removed from
the core function's `locations` (which records where the characterized activity occurs:
the cytosol, with MMACHC). The mitochondrion rows stay KEEP_AS_NON_CORE. The open question
is recorded as a core-function knowledge gap, with a compartment-restricted rescue and
matrix proximity labelling as suggested experiments.
