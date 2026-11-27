# ANKRD13D notes

- ANKRD13D (Q6ZTN6), third ANKRD13 paralog characterized in PMID:22298428 (full text, HeLa). Its UIMs bind Lys63- but not Lys48-linked chains ("Ankrd 13A, 13B, and 13D, but not 13C, pulled down Lys-63–linked, but not Lys-48–linked, Ub chains"). Unlike ANKRD13B, **endogenous** ANKRD13D was detected: it binds EGFR after EGF and is at the plasma membrane, more so after EGF [PMID:22298428 "the amounts of plasma membrane-bound endogenous 13A and 13D were elevated after 5 min of EGF stimulation"].
- **Direction of regulation:** overexpression retains EGFR at the surface, but dominant-negative truncations do the same, and the authors conclude "we propose that Ankrd 13A, 13B, and 13D positively regulate the internalization of ligand-activated EGFR". UniProt agrees ("Positively regulates the internalization"). So GO:0002091 (IMP; ARBA IEA) → MODIFY to GO:0002090, matching the round-3 fix on ANKRD13B (#4092).
- **Late endosome is weak for 13D:** "Ankrd 13D marginally colocalized with CI-M6PR"; the PAINT GO:0005770 node is seeded by 13A and 13B only. KEEP_AS_NON_CORE for the IBA and UniProt SubCell IEA.
- **Perinuclear (IDA + ARBA):** the text places only 13A and 13B in the perinuclear region; 13D has a "cytoplasmic reticular distribution". The figure is not cached, so both rows are UNDECIDED.
- **ENTREP1 (FAM189A2) IPIs ×3** (BioPlex 2.0, BioPlex 3.0, ENTREP Y2H; UniProt NbExp=3). Reproducible and coherent with ITCH/RNF11 links (PMID:31985874, abstract), but GO:0005515 is uninformative → REMOVE, raised as a question.
- Affinage: gates clear, but it cites only PMID:31985874 and attributes the ANKRD13A-RNF11-EGFR transient complex to ANKRD13D. Nothing taken from it.
- No NEW terms.

## Round 2 (reviewer, PR #4100)

- Late endosome IEA (GO_REF:0000044) comes from UniProt SubCell, which records late endosome as experimental (ECO:0000269, PMID:22298428), not from PAINT. Reason rewritten to cite that line; still KEEP_AS_NON_CORE because the paper calls the colocalization marginal.
- Late endosome IBA: the source entities are now SUPPORTS_TRANSFER, with the "13D not a seed; minor pool" caveat in the node comment. The previous SUPPORTS_SOURCE_BUT_NOT_TARGET contradicted NO_FAILURE_NON_CORE.
- Duplicate reference entries (UniProt, affinage) removed. The stub already seeds them; the builder now de-duplicates, and qcheck now flags duplicate reference ids.
- NEW GO:0070530 K63-linked polyubiquitin modification-dependent protein binding (IDA, PMID:22298428). This is not redundant with GO:0140036; the two are siblings under modification-dependent protein binding.
- GO:0002091 reason now says why GO:0002092 (positive) is not proposed: it is the authors' interpretation, and no loss-of-function experiment has tested it.
