# eryCIII (A4F7P3, SACE_0726) — review notes

Part of the **BGC exemplar curation project** (`projects/BGC.md`). MIBiG BGC0000055
(*Saccharopolyspora erythraea*, erythromycin PKS). GenBank CAM00067.1 → UniProt
**A4F7P3** (ERYC3_SACEN), gene *eryCIII* / SACE_0726.

## Function — the desosaminyl glycosyltransferase

EryCIII is the **TDP-D-desosamine glycosyltransferase** (EC 2.4.1.278) of erythromycin
biosynthesis; it is the catalytic partner of the activator EryCII.

- "EryCIII converts alpha-mycarosyl erythronolide B into erythromycin D using
  TDP-d-desosamine as the glycosyl donor... highly active with a kcat greater than
  100 min-1... selective for the natural nucleotide sugar donor and macrolide
  acceptor." [PMID:15303858 — IDA source]
- "the glycosyltransferase (GT) EryCIII, in concert with its partner EryCII, attaches
  a nucleotide-activated sugar to the macrolide scaffold with high specificity";
  heterotetramer with EryCII (PDB 2YJN). [PMID:22056329]

## Annotation issues

- GO:0008194 UDP-glycosyltransferase activity (IEA) → MODIFY → **GO:0016758
  hexosyltransferase activity**. The donor is **TDP-D-desosamine**, not a UDP-sugar,
  so the UDP-specific term is incorrect; the accurate activity is already IDA-supported.
- GO:0017000 antibiotic biosynthetic process (IEA + IDA) → ACCEPT (correct; erythromycin
  is an antibiotic); add the more specific **GO:1901115 erythromycin biosynthetic
  process** as the core BP (IDA-supported by PMID:15303858).
- GO:0016757 glycosyltransferase activity (IEA) → ACCEPT (true general parent).
- GO:0016758 hexosyltransferase activity (IEA + IDA) → ACCEPT (accurate; IDA).
- GO:0017000 antibiotic biosynthetic process (IDA) → ACCEPT (experimental; erythromycin
  is an antibiotic).

No GO MF term exists for EC 2.4.1.278 specifically → candidate proposed_new_term.

## Predicted-complex evidence (BGC project)

Moriwaki et al. (bioRxiv 2025.10.26.684697) predict the EryCII-EryCIII interaction
(BGC0000055; CAM00066.1/CAM00067.1) at **ipTM 0.92**, matching PDB 2YJN.

## References
- PMID:15303858 — Lee et al. 2004, JACS (EryCIII reconstitution; TDP-D-desosamine
  donor; IDA). VERIFIED.
- PMID:22056329 — Moncrieffe et al. 2012, J Mol Biol (EryCIII·EryCII structure, 2YJN). VERIFIED.
