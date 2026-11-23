# INSIG2 (Q9Y5U4) review notes

## Deep research status

- 2026-10-18: Falcon deep research was tried once for INSIG1 in this session and failed at login
  ("Exception: Failed to authenticate"; key not authorised). It was not retried for INSIG2.
  No deep-research file exists. These notes are built from cached primary literature, UniProt and GOA.

## Identity and family

- INSIG2 is the paralog of INSIG1 (PANTHER PTHR15301:SF10), a six-TM ER membrane protein with a
  shorter N-terminus [PMID:12242332 "Insig-2 differs from insig-1 primarily in the NH 2 -terminal sequence, which is much shorter in insig-2."].
- More conserved than INSIG1 across vertebrates [PMID:12242332 "Insig-2 is more highly conserved than insig-1 among various vertebrate species"].
- ER location by immunofluorescence [PMID:12242332 "Immunofluorescence studies of cells overexpressing epitope-tagged versions of both proteins show an ER distribution with no apparent change in the presence of sterols"].

## Core function 1: sterol-dependent ER retention of SCAP-SREBP

- INSIG2 binds SCAP in a sterol-regulated way and blocks SREBP export
  [PMID:12242332 "insig-2 binds to the SCAP/SREBP-2 complex only in the presence of sterols"].
- Restores sterol block of SCAP budding in a vesicle-formation assay
  [PMID:12242332 "Coexpression of insig-1 or -2 did not affect budding in the absence of sterols (lanes 4 and 6), but it permitted sterols to specifically block SCAP budding"].
- Absolute sterol requirement, and constitutive (SREBP-independent) expression; this is the key
  difference from INSIG1 [PMID:12242332 "the insig-2 mRNA was expressed constitutively and was not affected by induction of either SREBP"].
- Liver-specific Insig-2a transcript is repressed by insulin, allowing SREBP-1c processing
  [PMID:12624180 "Insig-2a is the predominant transcript in livers of fed animals, and it is selectively down-regulated by insulin."].
- Insigs lower cholesterol needed for SCAP conformational change [PMID:12963821].

## Core function 2: oxysterol binding (best-characterised for INSIG2)

- [PMID:17428920 "These studies define Insigs as oxysterol-binding proteins"]; TM3/TM4 needed for oxysterol and Scap binding.
- Cryo-EM human SCAP-INSIG2-25HC [PMID:33446483 "A 25HC molecule is sandwiched between the S4 to S6 segments in Scap and TMs 3 and 4 in Insig-2 in the luminal leaflet of the membrane."].
- MvINS-based model [PMID:26160948 "suggest that the central cavity of Insig-2 accommodates 25-hydroxycholesterol, whereas TM3 and TM4 engage in Scap binding"].
- PCK1 phosphorylation of INSIG2 Ser151 reduces sterol binding (single lab, HCC) [PMID:32322062].

## Core function 3: HMGCR ERAD adaptor (TRC8/RNF145 rather than gp78)

- Both Insigs mediate sterol-induced HMGCR binding [PMID:22143767 "This degradation results from sterol-induced binding of reductase to the Insig-1 or Insig-2 proteins of ER membranes."].
- INSIG2 does not detectably bind gp78 but binds Trc8 [PMID:22143767 "Trc8-dependent ubiquitination is mediated by both Insig-1 and Insig-2"].
- Asp to Ala in INSIG2 gives the same dual defect as INSIG1 D205A [PMID:16606821 "Alanine substitution of the corresponding aspartic acid in Insig-2 produced the same dual defects."].
- RNF145 binds Insig-1 and -2 [PMID:29374057].
- GO:1990756 ubiquitin-like ligase-substrate adaptor activity proposed as NEW (no GOA row for this on INSIG2).

## Annotation decisions (summary; kept identical to INSIG1 for shared PAINT terms)

- 39 protein-binding rows: SCAP rows (PMID:12242332, PMID:17428920) MODIFY -> GO:0140311; HuRI/Rolland
  Y2H rows (incl. RNF5) REMOVE as uninformative.
- ER -> MODIFY to ER membrane; cholesterol biosynthetic/metabolic process -> MODIFY to GO:0045541.
- cellular response to insulin stimulus IBA and response to insulin IEA: MARK_AS_OVER_ANNOTATED (expression
  regulation of the gene, not a protein function; insulin represses Insig-2a).
- response to lipid IEA: MODIFY -> GO:0036315 cellular response to sterol (INSIG2 is a sterol sensor).
- response to fatty acid IEA: MARK_AS_OVER_ANNOTATED (no human evidence that INSIG2 protein acts in a fatty-acid response).
- regulation of transcription by RNA pol II NAS: MARK_AS_OVER_ANNOTATED, as for INSIG1.
- Gene-specific difference vs INSIG1: INSIG2 is not an SREBP target (no feedback induction), has an absolute
  sterol requirement and weaker SCAP affinity; and its ERAD partner is TRC8/RNF145 rather than gp78.
  None of these changes the shared-term verdicts.
