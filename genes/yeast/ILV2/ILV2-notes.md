# ILV2 notes (YMR108W, P07342)

Evidence journal for the review; module context: branched-chain amino acid biosynthesis.

- Ilv2 is the catalytic subunit of mitochondrial acetohydroxyacid synthase (AHAS, EC 2.2.1.6) [UniProt:P07342].
- AHAS catalyses the first common step of BCAA synthesis [PMID:16390333 "Isoleucine, leucine and valine are synthesized via a common pathway in which the first reaction is catalysed by AHAS (acetohydroxyacid synthase; EC 2.2.1.6)."]
- Two reactions: 2 pyruvate -> 2-acetolactate (Val/Leu) and pyruvate + 2-oxobutanoate -> 2-aceto-2-hydroxybutanoate (Ile) [UniProt:P07342, RHEA:25249, RHEA:27654].
- Recombinant Ilv2 is active alone; Ilv6 stimulates it [PMID:10213630 "Reconstitution studies showed that the ilv6 protein stimulates the catalytic activity of the ilv2 protein by up to 7-fold"].
- Cofactors ThDP, Mg2+, FAD [PMID:15709745 "In addition to thiamin diphosphate, AHAS requires FAD for activity."]; crystal structures with sulfonylurea herbicides [PMID:15709745].
- Location: mitochondrion (multiple proteomics HDA; UniProt).

## Curation observations
- PMID:2406721 (cited by SGD for IDA and IMP BCAA biosynthesis) is a protein N-myristoylation/NMT1 study; the abstract does not mention ILV2. Accepted on independent evidence; flagged as a possible reference mis-mapping (full text not cached).
- No GO:1901705 L-isoleucine biosynthetic process on ILV2, although ILV5/ILV3/BAT1/BAT2 and the ComplexPortal AHAS complex carry it (QuickGO, 2026-10). Proposed as NEW (IC): Ilv2 catalyses step 1 of the Ile branch.
- YeastPathways appears to assign the AHAS reaction to the complex rather than to ILV2 (no RCA rows on ILV2).
