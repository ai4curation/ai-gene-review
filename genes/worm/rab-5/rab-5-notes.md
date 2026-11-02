# rab-5 review notes

## Session 1 (creation)

- fetch-gene resolved P91857 (TrEMBL, unreviewed); 35 GOA rows. Manual literature synthesis in
  `rab-5-deep-research-manual.md` (no deep-research provider available).
- Full text read: PMID:10588660, 15895077, 20462958, 22451698, 22545101, 26783301, 23840591.
  Abstract only: PMID:16394106, 16497226, 20434987, 20921409, 22342749, 23100538, 25858456.
- Core: Rab5 molecular switch (G protein activity / GTPase activity) on early endosome membranes,
  activated by RME-6 at coated pits and by RABX-5 on endosomes, inactivated by TBC-2; drives
  receptor-mediated endocytosis (yolk uptake) and early endosome function; also phagosome
  maturation of apoptotic corpses [PMID:22451698 "RAB-5 acts upstream of RAB-7 by tethering early endosomes and nascent phagosomes"].
- GO:0032794 GTPase activating protein binding (IPI, partner RME-6): RME-6 has a RasGAP-like
  domain but the interaction is GDP-RAB-5 binding to its Vps9 GEF domain; the term misrepresents
  the interaction. Marked over-annotated. GO has no "guanyl-nucleotide exchange factor binding" term.
- SynGO DCV exocytosis rows (PMID:23100538, abstract only): abstract places RAB-5 at DCV sorting
  at the Golgi-endosomal interface, not at the release step [PMID:23100538 "locally exclude each other at an essential stage during DCV sorting"].
  Modified to dense core granule biogenesis; synapse CC rows left UNDECIDED (full text unseen).
- Protein secretion (EGL-17): partial RNAi effect, authors suggest an indirect endocytic route;
  marked over-annotated.
- No NEW terms proposed. Early-to-late endosome transport / Rab conversion is a candidate, but
  the worm evidence shows RAB-5 being converted (substrate of the switch) and its activity
  maintained, so it is left as a question rather than an annotation.
