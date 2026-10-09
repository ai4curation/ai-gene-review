# Gcat (CG10361, Q9VTN9) notes

## 2026-10-09 review session

- Deep research (falcon, with perplexity-lite fallback) timed out / failed; no deep-research file.
  Review is based on the UniProt record and GOA rows.
- No Drosophila-specific publication is attached to any Gcat GOA row; all annotations are
  IBA/ISS/IEA from the bovine GCAT ortholog (Q0P5L8) and InterPro IPR011282.
- UniProt: "2-amino-3-ketobutyrate coenzyme A ligase, mitochondrial", EC 2.3.1.29,
  "Reaction=glycine + acetyl-CoA = (2S)-2-amino-3-oxobutanoate + CoA" with
  "PhysiologicalDirection=right-to-left", i.e. glycine-forming
  [file:DROME/Gcat/Gcat-uniprot.txt "PhysiologicalDirection=right-to-left"].
- PANTHER PTHR13693:SF102 (mitochondrial GCAT subfamily); PLP cofactor.
- Pathway partner: Tdh (CG5955) makes 2-amino-3-oxobutanoate from threonine
  [PMID:31313987 "CG5955 is a fly homolog of threonine 3-dehydrogenase that converts threonine and NAD+ into L-2-amino-acetoacetate, NADH, and H+"].

## Decisions
- All annotations accepted except generic `transferase activity` (MODIFY -> GO:0008890).
- Core function: glycine C-acetyltransferase activity in mitochondrion, L-threonine catabolism and
  glycine biosynthesis.
