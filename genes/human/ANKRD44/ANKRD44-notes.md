# ANKRD44 notes

- PP6-ARS-B: one of three PP6 ankyrin-repeat subunits (ANKRD28, ANKRD44, ANKRD52). It co-purifies with PP6 through PPP6R1 in human cells [PMID:18186651, abstract]. Depleting it, as with ANKRD28 but not ANKRD52, disrupts PP6 in mitosis [PMID:21187329, full text].
- GOA has protein-binding rows only (11), with no complex or regulator term, although paralog ANKRD28 carries GO:0008287 (IDA) and GO:0019888 (IMP). Added NEW GO:0008287 (IDA, PMID:18186651) and NEW GO:0019888 (IMP, PMID:21187329). This passes the comparator check against the paralog, and ANKRD44 is a subunit doing the work (participation).
- Protein-binding rows:
  - PPP6R1 ×5 → REMOVE (complex co-membership).
  - USP6/Tre2 → MODIFY to GO:0019899 enzyme binding, supported by pulldown, co-IP and colocalization in PMID:16555005. That abstract names the partner "LOC91256", while ANKRD44's GeneID is 91526 (likely a digit transposition); GOA and IntAct map the interaction to ANKRD44.
  - WWP2 ×2, HSPB1, RNF11, WFS1 → REMOVE (Y2H screens).
- Affinage attributes the IkBe knockdown in PMID:18186651 to ANKRD44, but that experiment tested ANKRD28 and PP6R1, so the record is marked LOW_QUALITY.
- Trastuzumab-resistance phenotype [PMID:31297336]: one cell line; no GO term drawn.

## Round 2 (reviewer, PR #4131)

- "interchangeable" is replaced by "alternative". PMID:18186651 says the three ankyrin subunits "segregate into separate branches ... suggesting individual biological functions", and PMID:21187329 shows ANKRD52 lacks the mitotic role. The wrong word came from the affinage record.
- Paralog provenance corrected: ANKRD28's GO:0008287 (IDA) and GO:0019888 (IMP) come from PMID:35512830, not PMID:18186651.
- GO:0008287 now also cites the reciprocal FLAG-PPP6C mitotic purification in PMID:21187329.
- The GO:0019888 reason states the evidence is phenotype-level. The four AP-MS sources of the PPP6R1 association are now relevance MEDIUM.
- PMID:16555005 correctness is left unset because of the LOC91256 identifier caveat. The miR-133a paper (PMID:34350837) is now listed (LOW; no GO term).
