# ANKRD13D notes

- ANKRD13D (Q6ZTN6), third ANKRD13 paralog characterized in PMID:22298428 (full text, HeLa). Its UIMs bind Lys63- but not Lys48-linked chains ("Ankrd 13A, 13B, and 13D, but not 13C, pulled down Lys-63–linked, but not Lys-48–linked, Ub chains"). Unlike ANKRD13B, **endogenous** ANKRD13D was detected: it binds EGFR after EGF and is at the plasma membrane, more so after EGF [PMID:22298428 "the amounts of plasma membrane-bound endogenous 13A and 13D were elevated after 5 min of EGF stimulation"].
- **Direction of regulation:** overexpression retains EGFR at the surface, but dominant-negative truncations do the same, and the authors conclude "we propose that Ankrd 13A, 13B, and 13D positively regulate the internalization of ligand-activated EGFR". UniProt agrees ("Positively regulates the internalization"). So GO:0002091 (IMP; ARBA IEA) → MODIFY to GO:0002090, matching the round-3 fix on ANKRD13B (#4092).
- **Late endosome is weak for 13D:** "Ankrd 13D marginally colocalized with CI-M6PR"; the PAINT GO:0005770 node is seeded by 13A and 13B only. KEEP_AS_NON_CORE for the IBA and UniProt SubCell IEA.
- **Perinuclear (IDA + ARBA):** the text places only 13A and 13B in the perinuclear region; 13D has a "cytoplasmic reticular distribution". The figure is not cached, so both rows are UNDECIDED.
- **ENTREP1 (FAM189A2) IPIs ×3** (BioPlex 2.0, BioPlex 3.0, ENTREP Y2H; UniProt NbExp=3). Reproducible and coherent with ITCH/RNF11 links (PMID:31985874, abstract), but GO:0005515 is uninformative → REMOVE, raised as a question.
- Affinage: gates clear, but it cites only PMID:31985874 and attributes the ANKRD13A-RNF11-EGFR transient complex to ANKRD13D. Nothing taken from it.
- No NEW terms.
