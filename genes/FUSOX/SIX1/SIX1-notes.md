# SIX1 (Avr3), Fusarium oxysporum f. sp. lycopersici (Q709D8): curation notes

## Sources used
- UniProt Q709D8 (TrEMBL, unreviewed): 284 aa, SignalP 1-21, PDB 7T69 (22-284), 4 disulfides. GO rows in UniProt all come from PHI-base.
- Deep research: `SIX1-deep-research-falcon.md`. Used for orientation; claims checked against cached papers.
- Cached papers: PMID:15387816 (abstract only), 15672814 (abstract only), 25740416 (abstract only, no PMC), 18464895, 23596453, 26177154, 19851506, 38411527 (full text). PMID:29786161 abstract only.
- New PMIDs verified with PubMed MCP (metadata/citation lookup): 15387816, 29786161, 19851506, 38411527.

## Biology
- Found in xylem sap: [PMID:15387816 "The central part of Six1 corresponds to the 12 kDa protein found in xylem sap of infected plants."]
- I-3 avirulence: [PMID:15387816 "Conversely, deletion of the SIX1 gene in a wild-type strain results in breaking of I-3-mediated resistance."]
- Virulence plus avirulence: [PMID:15672814 "deletion leads to a further increase in virulence on the I-3 line as well as reduced virulence on susceptible lines"]
- Recognition can be separated from virulence: [PMID:29786161 "These findings separate the recognition of SIX1 from its role as an effector and suggest direct recognition by I-3."]
- I-3 is an SRLK: [PMID:25740416 "one was found to confer Avr3-dependent resistance to Fol race 3, confirming it to be I-3."]
- Avr1 suppresses I-3; Avr3 needed for full virulence: [PMID:18464895 "Since Avr3 is required for full virulence of Fol, evasion of I-3 recognition through loss of the AVR3 gene would entail a serious fitness penalty."]
- Expressed only in planta, depends on Sge1: [PMID:19851506 "SIX1 is only expressed during in planta growth and encodes Avr3, as it is required for I-3 mediated resistance"]
- Structure, FOLD family: [PMID:38411527 "represent the founding members of a new structural class of fungal effectors we have designated the FOLD effectors."]
- No known molecular activity or host target.

## Annotation decisions
- GO:0140404 perturbation of host innate immune response (EXP x4): ACCEPT for 15672814, 18464895 and 25740416. The neutral parent fits: recognition activates I-3 immunity, but HR has not been shown (so not GO:0080185) and Six1 has no shown suppressive activity. REMOVE for 26177154: the full text has no SIX1 experiment (I-7 paper; Avr3 appears only in a strain description and the discussion).
- GO:0043657 host cell (EXP, PMID:23596453): REMOVE. Full text checked: SIX1 appears only as a pAVR3:GFP reporter in which [PMID:23596453 "the coding sequence for Avr3 has been replaced by GFP"]. The host-cell location in that paper is for Avr2.
- GO:0020002 host cell plasma membrane (IDA, PMID:25740416): UNDECIDED. Abstract-only, no PMC copy. Possibly I-3 localisation was mis-attributed, but I could not verify this.
- NEW GO:0140593 host apoplast (IDA, PMID:15387816). Its definition includes the xylem vessel lumen. Comparator: AVR9 (FULFL) uses the same term.
- No NEW process terms. There is no generic pathogen-side "virulence" term, and the virulence mechanism is unknown.

## Project curation question 1
All effector process rows use the symbiont-side term GO:0140404 and are experimental (PHI-base), not IEA. However, 2 of 6 PHI-base rows cite papers that do not test SIX1 (PMID:23596453, 26177154). They appear to have been attached by co-mention.
