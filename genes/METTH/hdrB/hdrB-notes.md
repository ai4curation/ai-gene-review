# hdrB (MTH_1879, O27907) - Methanothermobacter thermautotrophicus Delta H - review notes

## Literature search (2026-11-07)

Deep-research providers were unavailable; no `-deep-research-*.md` file exists. Searches as
for METTH/hdrA (WebSearch: Setzke 1994, Hamann 2007 CCG domain, Kaster 2011, Wagner 2017).
No study of the Delta H HdrB protein was found; biochemistry is on M. marburgensis
(strain Marburg) HdrB, Q50755, which is 94.7% identical to O27907
(file:METTH/hdrA/hdrA-bioinformatics/RESULTS.md).

Cached and read: PMID:17929940 (full text), PMID:28818947 (abstract), PMID:21262829
(full text), PMID:8119281 (abstract).

## Record facts (UniProt O27907, PE 3)

- 302 aa, two Pfam CCG domains (PF02754, 2 copies), NCBIfam TIGR03288 CoB_CoM_SS_B,
  InterPro IPR017678. No COFACTOR or FT BINDING lines in the record.
- PANTHER PTHR42947:SF1 (family PTHR42947 "COB--COM HETERODISULFIDE REDUCTASE SUBUNIT B 1").
- EC 1.8.98.5 by similarity to Q50755; Rhea RHEA:55748.

## Biology

- HdrB carries the active-site cluster [PMID:17929940 "Here we present experimental
  evidence that the C-terminal CCG domain of HdrB binds this unusual [4Fe-4S] cluster."];
  ligands C153, C193, C194, C234 in M. marburgensis HdrB, all conserved at the same
  positions in O27907 (RESULTS.md).
- The 2017 structure shows two noncubane clusters at the CCG motifs, with the disulfide
  clamped between them [PMID:28818947 "HdrB contains two noncubane [4Fe-4S] clusters
  composed of fused [3Fe-4S]-[2Fe-2S] units sharing 1 iron (Fe) and 1 sulfur (S), which
  were coordinated at the CCG motifs."]. The 2007 suggestion that the N-terminal CCG domain
  binds a Zn site is not consistent with both CCG motifs coordinating clusters; recorded as
  a DISPUTED finding. Whether the holoenzyme also has a Zn site cannot be judged from the
  2017 abstract.
- HdrB alone does not reduce the heterodisulfide physiologically; electrons come from H2 via
  Mvh, HdrA (bifurcation) and HdrC [PMID:21262829].

## Is there a GO term for HdrB's half-reaction?

No. OLS search (2026-11-07) for heterodisulfide/disulfide reductase terms: GO:0051912 is
defined as "coenzyme B + coenzyme M + methanophenazine = ... + dihydromethanophenazine"
(EC 1.8.98.1, RHEA:18085), which is the membrane HdrDE reaction of Methanosarcinales.
GO:0045331 (H2:heterodisulfide) is obsolete. The other disulfide reductase terms are NAD(P)H-,
glutathione- or protein-specific. The HdrB half-reaction (CoM-S-S-CoB + 2 e- + 2 H+ ->
CoM-SH + CoB-SH, electrons from HdrC) is an intra-complex step with no free donor, so no
separate term is proposed; the complex activity is the proposed "H2:CoB-CoM
heterodisulfide,ferredoxin reductase activity" (shared with METJA/hdrA).

## Decisions

- GO:0051912 IEA (IPR017678): MODIFY to the proposed term, as contributes_to (pattern 20;
  pattern 16 does not apply in the sense of a wrong subunit, since HdrB is the catalytic
  subunit for the disulfide, but the defined reaction needs the whole complex).
- GO:0015948 methanogenesis IEA: MODIFY to GO:0019386 methanogenesis, from carbon dioxide.
- NEW: GO:0051539 4Fe-4S cluster binding (ISS), GO:0044678 complex (ISS).
