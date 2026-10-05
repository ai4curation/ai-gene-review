# CNPY3 (Protein canopy homolog 3 / PRAT4A) — Review notes

UniProt: Q9BT09. Gene synonyms: CTG4A, ERDA5, PRAT4A (Protein Associated with TLR4), TNRC5. HGNC:11968. 278 aa precursor.

## Core biology

CNPY3 is an ER-resident, glycosylated protein with a signal peptide (1-30) and a single
Saposin B-type / MD-2-related lipid-recognition (ML) domain (47-271). It functions as a
Toll-like-receptor-specific co-chaperone for the ER HSP90 paralog HSP90B1 (gp96 / GRP94 / endoplasmin).

- UniProt FUNCTION: "Toll-like receptor (TLR)-specific co-chaperone for HSP90B1. Required for
  proper TLR folding, except that of TLR3, and hence controls TLR exit from the endoplasmic
  reticulum. Consequently, required for both innate and adaptive immune responses." [file:human/CNPY3/CNPY3-uniprot.txt FUNCTION; By similarity, ECO:0000250]
- UniProt SUBUNIT: "Interacts with HSP90B1; this interaction is disrupted in the presence of ATP.
  Interacts with TLR1, TLR2, TLR4 and TLR9. Strongest interaction with TLR4." [file:human/CNPY3/CNPY3-uniprot.txt SUBUNIT]
- UniProt SUBCELLULAR LOCATION: Endoplasmic reticulum. [file:human/CNPY3/CNPY3-uniprot.txt]
- Reactome pathway R-HSA-1679131 "Trafficking and processing of endosomal TLR"; events
  R-HSA-1678923 "TLR folding by chaperones GP96 and CNPY3" and R-HSA-1678944
  "Folded full-length TLR7/8/9 dissociates from the GP96:CNPY3 complex". [file:human/CNPY3/CNPY3-uniprot.txt DR Reactome]

The mechanism was established in mouse Cnpy3/PRAT4A, not directly in human CNPY3. Mouse Cnpy3 and
gp96/Hsp90b1 form a TLR-folding module required for maturation and trafficking of multiple TLRs,
whereas TLR3 is independent. Purified mouse Cnpy3 bound gp96 directly and nucleotide disrupted the
interaction [PMID:20865800 "gp96 directly interacts with CNPY3, and the complex dissociates in the
presence of adenosine triphosphate (ATP)."]. Cnpy3 and gp96 cooperatively bind TLR9, and Cnpy3 promotes
substrate loading [PMID:20865800 "TLR9 forms a multimolecular complex with gp96 and CNPY3, and the
binding of TLR9 to either molecule requires the presence of the other."; "We suggest that CNPY3
interacts with the ATP-sensitive conformation of gp96 to promote substrate loading."]. Human UniProt
transfers this conserved function by similarity; human-specific mechanistic validation remains a gap.

## Disease

Biallelic loss-of-function variants in CNPY3 cause Developmental and epileptic encephalopathy 60
(DEE60, MIM:617929), autosomal recessive, with seizure onset in the first months of life.
A missense variant Gly125Arg is reported. [PMID:29394991 "Biallelic Variants in CNPY3, Encoding an
Endoplasmic Reticulum Chaperone, Cause Early-Onset Epileptic Encephalopathy"; file:human/CNPY3/CNPY3-uniprot.txt
DISEASE + RN 13]

## Feature / domain evidence (UniProt)

- Saposin B-type domain 47-271; this is the ML/saposin-like fold, but the cached evidence does not map
  direct TLR or gp96 engagement to this domain.
- Three disulfide bonds (49-206, 52-194, 104-166) stabilize the domain [ECO:0000250].
- N-glycosylation at Asn-153 [PMID:19159218].
- Belongs to the canopy family (CNPY1-4). PANTHER PTHR15382:SF2 "PROTEIN CANOPY HOMOLOG 3".

## Existing GO annotations (GOA) — assessment summary

1. GO:0005102 signaling receptor binding (IBA, GO_REF:0000033) — CNPY3 does physically engage TLR
   ectodomains in the ER as a folding chaperone client interaction. "signaling receptor binding" is a
   defensible MF for the TLR interaction but does not capture the chaperone activity. Keep as non-core;
   the chaperone MF terms are more informative.
2. GO:0005783 endoplasmic reticulum (IEA, GO_REF:0000044, from UniProt SubCell) — correct, ACCEPT.
3. GO:0005515 protein binding has four exact PMID signatures from high-throughput interactomes
   (PMID:28514442, 32296183, 32814053, 33961781), spanning thirteen physical GOA rows. KEEP_AS_NON_CORE:
   IPI asserts observed physical interactions and no evidence contradicts them, so the rows are retained.
   Bare protein binding is uninformative and the heterogeneous partner sets do not support a single
   evidence-matched replacement, which makes them non-core rather than invalid. The cached abstract-only
   PMID:32814053 cannot adjudicate individual interactions, so no misattribution claim is made.
4. GO:0005102 signaling receptor binding (IEA, GO_REF:0000107, ortholog transfer from mouse Q9DAU1) —
   redundant with the IBA; keep as non-core.
5. GO:0005788 endoplasmic reticulum lumen (TAS, Reactome) x2 — correct subcellular location, more
   specific than GO:0005783. ACCEPT.

## Chaperone-term decision

- GO:0051082 is formally obsolete and is not retained or proposed for CNPY3. Live QuickGO is authoritative:
  its API currently returns the name `obsolete unfolded protein binding`, `isObsolete=true`, and the
  replacement considerations GO:0044183 and GO:0140309. The repository's local `ontologies/go.tsv`
  snapshot is stale (dated 2026-03-21) and must not be used to reverse that live status. PMID:20865800
  shows a substrate-loading co-chaperone that requires gp96 for efficient TLR binding; it does not
  demonstrate autonomous passive binding to an unfolded protein.
- GO:0044183 protein folding chaperone is not asserted as a CNPY3 MF. CNPY3 is required for the gp96
  folding system, but it lacks intrinsic ATPase activity and is described as a co-chaperone
  [PMID:20865800 "CNPY3 has neither intrinsic ATPase activity nor the ability to significantly modulate
  the ATPase activity of gp96"]. The folding contribution is represented as the BP GO:0034975.
- GO:0140309 unfolded protein holdase activity does not fit: it requires binding an unfolded protein
  and escorting it to an acceptor or location while preventing aggregation. No such carrier/antiaggregation
  activity is shown for CNPY3. Likewise, there is no evidence for an independent in-situ holdase/NTR.
- GO:0051879 Hsp90 protein binding is the evidence-matched MF for the direct, ATP-sensitive gp96
  interaction. CNPY3's substrate-loading co-chaperone role is stated in free text because GO has no
  active general co-chaperone MF term.

## New annotations retained

- MF: GO:0051879 Hsp90 protein binding (direct mouse biochemical evidence; conserved human function
  by orthology).
- BP: GO:0034975 protein folding in endoplasmic reticulum (TLR folding in ER).
- BP: GO:0072657 protein localization to membrane. Mouse Cnpy3 silencing traps TLR9 precursors in the
  ER [PMID:20865800 "we found that TLR9 precursors were trapped in the ER of cells with silenced
  expression of either gp96 or CNPY3 (Fig. 5b)."]. This supports CNPY3-dependent TLR ER exit and
  membrane delivery; the human annotation is transferred by orthology.
- BP: GO:0045087 innate immune response (UniProtKB-KW Immunity/Innate immunity).
- BP: GO:0034123 positive regulation of toll-like receptor signaling pathway is retained as a downstream,
  non-core NEW process context. It reflects loss of TLR responses after disruption of the maturation
  module, not direct signaling catalysis by CNPY3.

## PAINT and signature audit (2026-08-28)

- PANTHER places the GO:0005102 IBD at `PANTHER:PTN008355430` in the correct family `PTHR15382`
  (CTG4A-related). Human CNPY3 is in `PTHR15382:SF2`; seeds are mouse Cnpy3
  (`MGI:MGI:1919279`) and mouse Cnpy4 (`MGI:MGI:1913705`). The transfer is retained as
  `NO_FAILURE_NON_CORE`; mouse Cnpy3 supplies direct TLR-complex evidence.
- The 18 physical GOA rows collapse to 9 exact qualifier-aware signatures: 6 `enables` and 3
  `located_in`. Each is represented exactly once. Five additional author-proposed annotations are
  retained as NEW.
- Final actions across all 14 review entries: 3 ACCEPT, 6 KEEP_AS_NON_CORE, 5 NEW, 0 MODIFY,
  0 REMOVE, 0 MARK_AS_OVER_ANNOTATED, and 0 UNDECIDED.
