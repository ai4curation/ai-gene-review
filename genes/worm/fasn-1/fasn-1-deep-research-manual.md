# fasn-1 (F32H2.5; UniProt P91871) -- manual literature synthesis

No deep-research API was available for this review. This summary was compiled by hand
from PubMed searches (`fasn-1[Title/Abstract] OR F32H2.5[Title/Abstract]` AND elegans,
28 hits) and the cached publications in `publications/`. Each claim carries its source.

## Identity and family

- F32H2.5 is the single predicted fatty acid synthase gene of *C. elegans*; a shorter
  homolog, F32H2.6, encodes only an N-terminal portion
  [PMID:15340492 "There is one predicted FAS gene, F32H2.5, and its shorter homolog, F32H2.6, in the C. elegans genome. The latter can only encode the N-terminal portion of the protein."].
- FASN-1 is orthologous to human FASN
  [PMID:21178429 "fasn-1 encodes a putative fatty acid synthase, orthologous to human FASN."];
  emb-14 was renamed fasn-1 after its g43ts lesion was mapped to this gene
  [PMID:32550489 "At that time, it was suggested that the emb-14 gene be renamed fasn-1."].
- Domain architecture (UniProt P91871, InterPro/Pfam/SMART): KS (PF00109/PF02801),
  MAT (PF00698, SMART PKS_AT), DH (PROSITE PS52019), pseudo-KR (PF21149), ER
  (SMART PKS_ER), KR (PF08659), ACP (PF00550, PROSITE PS50075 with
  pantetheine-phosphoserine Ser2248) and thioesterase (PF00975). This is the
  canonical animal type I FAS order.
- Own alignment to human FASN: all annotated catalytic residues (KS Cys/His/His, MAT
  Ser, DH His/Asp, ACP Ser, TE Ser/His) are conserved
  [file:worm/fasn-1/fasn-1-bioinformatics/RESULTS.md].

## Biochemical function

- No purified-enzyme assay of *C. elegans* FASN-1 was found. Evidence for activity is
  (i) orthology and full catalytic-residue conservation, and (ii) in vivo fatty-acid
  profiling: transgenic rescue/overexpression raised palmitate and stearate
  [PMID:21178429 "the rescued siblings did show significantly increased levels of C16:0 (palmitic acid), the main product of FASN-1, and its elongated form C18:0"].
- RNAi of fasn-1 reduces triglyceride production
  [PMID:21524356 "knockdown of the proteins encoded by these genes using RNA interference produced severe defects in triglyceride production, molting, and reproduction"].
- FASN-1 output also feeds mmBCFA/sphingolipid precursors per the anchor-cell study,
  which describes "11-methyldodecanoic acid, which is a core precursor for C. elegans
  sphingolipids" as a key output of POD-2 and FASN-1 [PMID:39007804]. Kniazeva et al.
  however found RNAi of fasn-1 did not change FA composition selectively
  [PMID:15340492 "This suggests that disruption of FAS does not selectively alter FA biosynthesis and that neither FAS protein is specific for mmBCFA."].

## Localization

- Endogenously tagged FASN-1::mNG is cytoplasmic in the anchor cell
  [PMID:39007804 "POD-2 and FASN-1 are in the AC cytoplasm"].

## Phenotypes (necessity, not activity)

- Loss of function is lethal or causes growth arrest
  [PMID:15340492 "the RNAi-mediated disruption of F32H2.5 and F32H2.6 resulted in multiple defects and a lethal growth arrest (unpublished data)"].
- Temperature-sensitive alleles g43ts (A1425T / reported elsewhere as A1424T) and g14ts
  (G1830R) cause embryonic lethality and permeable eggshells [PMID:32550489]; loss of
  ptr-6 suppresses this [PMID:42400361].
- Partial loss-of-function fr8 (M241I) derepresses the antimicrobial peptide reporter
  nlp-29 in the epidermis, acting upstream of WNK-1/GCK-3 [PMID:21178429].
- Molting and cuticle defects on RNAi [PMID:21524356]; anchor-cell invasion defects on
  AC-specific RNAi [PMID:39007804]; sensitivity to biguanide-induced reductive stress
  [PMID:41394642, preprint].
- These are downstream consequences of fatty-acid supply; none identifies an activity of
  FASN-1 beyond fatty acid synthesis.

## Regulation

- Transcriptional target of SBP-1/SREBP (anchor cell, [PMID:39007804]), PHA-4 under
  nucleolar stress [PMID:29567958], CEP-1/p53 [PMID:16582625] and repressed by MAFR-1
  [PMID:25497095].
