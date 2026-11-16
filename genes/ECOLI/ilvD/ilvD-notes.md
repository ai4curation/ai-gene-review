# ilvD (P05791, E. coli K-12) review notes

No provider deep research was run for this gene. These notes are my own,
from the cached publications, the UniProt record (`ilvD-uniprot.txt`) and the
existing reviews of the same step (`genes/PSEPK/ilvD`, `genes/yeast/ILV3`,
`genes/SCHPO/ilv3`).

## Function

- Dihydroxy-acid dehydratase (DHAD), EC 4.2.1.9, IlvD/Edd family (PANTHER
  PTHR43661; Edd P0ADF6 and the D-xylonate dehydratases YjhG P39358 / YagF
  P77596 are E. coli paralogs in the same family, verified in
  `interpro/panther/PTHR43661/PTHR43661-entries.csv`).
- Dehydrates (2R)-2,3-dihydroxyisovalerate to 2-oxoisovalerate (valine and,
  via 2-oxoisovalerate, leucine) and (2R,3R)-2,3-dihydroxy-3-methylpentanoate
  to (S)-3-methyl-2-oxopentanoate (isoleucine) [UniProt CC:FUNCTION,
  ECO:0000269 PMID:13727223, PMID:8325851].
- Purified enzyme: homodimer of 66 kDa subunits [PMID:8325851].
- Oxygen sensitivity: "Dihydroxy-acid dehydratase from E. coli is inactivated
  by O2 in vitro and in vivo as a result of oxidative degradation of the
  [4Fe-4S]cluster" [PMID:8325851]; superoxide dismutase protects DHAD activity
  in vivo [PMID:7771772]. DHAD is a classic intracellular superoxide target.

## Cluster type (unresolved)

- E. coli-specific spectroscopy (UV-visible, EPR, MCD, resonance Raman):
  "the native enzyme contains a [4Fe-4S]2+,+ cluster, in contrast to spinach
  dihydroxy-acid dehydratase which contains a [2Fe-2S]2+,+ cluster"
  [PMID:8325851].
- UniProt now assigns a [2Fe-2S] cluster by HAMAP rule MF_00012, with a
  CAUTION: "Was originally thought to contain a [4Fe-4S] cluster ... However,
  a more recent study in M.tuberculosis has shown that this enzyme contains a
  [2Fe-2S] cluster, which is unstable and subject to degradation."
- I could not read the M. tuberculosis or plant structural papers here, and no
  newer E. coli-specific cluster study is cached. Decision: accept the generic
  iron-sulfur cluster binding IDA; keep the E. coli 4Fe-4S IDA as non-core
  (direct data on this protein, not overruled from ortholog evidence); leave
  the rule-propagated 2Fe-2S row UNDECIDED: it rests on ortholog data and
  conflicts with the only E. coli-specific data, but the curated UniProt
  caution may be right. A suggested question, experiment and knowledge gap
  record the conflict.

## Other decisions

- Magnesium binding (HAMAP) kept as non-core, as in KT2440 IlvD.
- catalytic activity and hydro-lyase activity modified to dihydroxy-acid
  dehydratase activity (correct but general parents). The hydro-lyase IBA node
  PTN000470254 spans IlvD, Edd and the xylonate dehydratases, so PAINT's
  family-level placement is right; the refinement is only for this member.
- BCAA biosynthetic process accepted (shared trunk; product 2-oxoisovalerate
  also feeds leucine), as for IlvC and in the yeast/pombe reviews.
- Cytosol (IBA, IDA proteomics) accepted.
