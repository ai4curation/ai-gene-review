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

## Update: deep research arrived
- The first falcon run finished after the wrapper timed out and wrote `Gcat-deep-research-falcon.md`.
- It confirms there is no enzyme assay of fly Gcat; identity rests on orthology
  [Gcat-deep-research-falcon.md "The publication establishes an orthology-based annotation, **not** an enzyme assay of Q9VTN9."].
- A 2026 fly study (Yoshinari et al., per the deep research) reports Gcat expression mainly in fat body,
  induced by starvation, and fat-body Tdh knockdown reduces threonine-derived label in glycine and serine
  [Gcat-deep-research-falcon.md "fat-body **Tdh knockdown** reduced incorporation of threonine-derived isotope into **glycine and serine**"].
  This supports the pathway context; no change to review decisions.
