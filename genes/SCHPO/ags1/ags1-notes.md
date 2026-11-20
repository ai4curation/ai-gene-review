# ags1 (mok1, SPCC1281.01; UniProt Q9USK8) notes

## Identity and architecture

- 2410-aa multidomain protein. Predicted N-terminal signal peptide, an extracellular GH13
  (alpha-amylase-like) region with three TM segments, a central TM, an intracellular
  GT5 glycogen/starch-synthase-like domain, and a C-terminal 12-TM domain
  [PMID:10087262 "The fifth domain is the COOH-terminal 400 amino acid residues that predict 12 membrane spanning domains"].
- The founding paper framed the two catalytic regions as "an intracellular domain for alpha-glucan
  synthesis and an extracellular domain speculated to cross-link or remodel alpha-glucan"
  [PMID:9689051].
- Paralogs mok11, mok12, mok13, mok14 [PMID:10087262]; mok12/13/14 are sporulation-specific and
  make spore-envelope alpha-glucans [PMID:16420355 "three mok1+ paralogues -mok12+, mok13+ and mok14+- are required for sporulation to succeed"].
- UniProt Q9USK8 has no TRANSMEM features; the topology is from the primary papers.

## Activity: shown vs inferred

- No in vitro alpha-1,3-glucan synthase assay with purified Ags1 has been reported. The activity
  rests on in vivo [14C]glucose incorporation: overexpression raises wall alpha-glucan 3.4-fold, ts
  mutants lower it by 69% [PMID:10087262 "These results strongly suggested that Mok1 is an α-glucan synthase."];
  depletion lowers it by 53% [PMID:22891259].
- GT5 (synthase) domain: overexpressed Ags1 accumulates (1,4)-alpha-glucan; E1526A in the GT5 domain
  abolishes this and poorly complements ags1-1 [PMID:17472966 "the production of (1,4)-alpha-glucan by the synthase domain of Ags1p is important"].
  This is the only residue-level evidence and it concerns the alpha-1,4 primer, not alpha-1,3 elongation.
- Mature wall alpha-glucan = two ~120-residue (1->3) chains with (1->4) residues at the reducing end,
  coupled; an ags1 mutant makes single chains only [PMID:15470229 "consisted of a single chain only"].
  The coupling step is attributed to the GH13 domain by hypothesis.
- GH13 domain: essential (ags1-664 = Y256F/R408H in GH13) [PMID:40668835], lacks hydrolase catalytic
  residues, transglycosylase role "suggested" [PMID:40668835 "the Ags1 GH13 domain is suggested to act as a transglycosylase"].
  PMID:42786154 Discussion states Ags1 "integrates α-glucan synthase and remodeling activities" citing
  the model, not new data. So GH13 activity is inferred, not demonstrated.

## Localization and timing

- Plasma membrane of growing tips in interphase (old end, then both after NETO), medial ring at
  mitosis before the primary septum, leading edge of the septum, then invaginated membrane flanking
  the septum [PMID:22891259; PMID:10087262].
- Colocalizes with Bgs1 from the earliest medial dots; Bgs1 co-IPs with Ags1 [PMID:22891259 "physiological Bgs1 and Ags1 coimmunoprecipitate"].
- Medial recruitment needs a stable contractile ring; SIN needed only for ring form. Depends on actin
  patches and exocyst [PMID:22891259].
- Present at mating, spore formation and germination sites [PMID:22891259].

## Function

- Essential; depletion causes lysis at septum at cell separation and at pole sides; secondary septum
  absent and primary septum weak/twisted [PMID:22891259 "Ags1 synthesizes an α-glucan of the primary septum"].
- Regulation: Rho2 -> Pck2 -> Mok1 [PMID:11102532 "the Rho2p GTPase activates Pck2p, and this kinase in turn controls Mok1p"];
  pck2 mutants delocalize Mok1 [PMID:10087262].
- Aah1/Aah3 (GPI-anchored GH13) act with Ags1 non-redundantly [PMID:40668835].

## GO-CAM

- gomodel:6918f23700003787 (PomBase): ags1 enables GO:0047657, part_of GO:0031671, occurs_in
  GO:0000935 division septum. MF and BP agree with this review. The occurs_in location is the septum
  (a wall structure); this review prefers plasma membrane at the cell division site for an integral
  membrane enzyme (as for bgs1), so division septum is kept as non-core.

## Open curation notes (not knowledge gaps)

- Secondary cell septum biogenesis (GO:1990344) is supported by PMID:22891259 Fig. 7 but PomBase
  annotated only primary septum biogenesis from the same paper; raised as a question, not added.
