# sucD (PA1589, Q51567) notes

No deep-research provider was available. Literature: PMID:10671455 (full text cached and read).
Reviewed in the same tier-2 round as sucC (PA1588), whose actions on the shared PMID:10671455 rows
this review matches.

## Biology

- sucCD operon, SucD = alpha subunit, 89% identical to E. coli SucD [PMID:10671455 "The sucD gene
  encodes the Scs α subunit (288 amino acids) and showed 89% amino acid sequence identity to the E. coli
  Scs α subunit."].
- SCS reaction with purified subunits [PMID:10671455 "In this reaction the Scs enzyme converted
  succinate, CoA, and [γ- 32 P]ATP to succinyl-CoA, ADP, and P i ."].
- Dual ATP/GTP formation [PMID:10671455 "In the presence of inorganic orthophosphate, succinyl-CoA, and
  an equimolar amount of ADP and GDP, Scs synthesizes essentially an equimolar amount of ATP and GTP."].
- NDP-kinase-like transphosphorylation [PMID:10671455 "As shown in Fig. 4 A and B, the Scs complex
  transferred the terminal phosphate from [γ- 32 P]ATP to GDP to form GTP"].

### Annotation decisions

- GO:0004775 (IBA, IEA, IDA), GO:0004776 (IBA, IEA, EXP), GO:0006099 (IBA, IEA), GO:0009361 (IBA),
  GO:0042709 (IEA, IDA): ACCEPT.
- GO:0004550 NDP kinase (IDA): MARK_AS_OVER_ANNOTATED (as sucC).
- GO:0009142 NTP biosynthesis (IDA): KEEP_AS_NON_CORE (as sucC).
- GO:0003824 (IEA): TOO_GENERAL.
- GO:0042709 is kept beside GO:0009361 (its is_a descendant) because the enzyme is equally
  GDP-forming; TOO_GENERAL would imply the ADP-forming complex is the whole story.
- Action counts: ACCEPT 11, MARK_AS_OVER_ANNOTATED 1, KEEP_AS_NON_CORE 1, TOO_GENERAL 1.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000122012 | GO:0004775 succinate-CoA ligase (ADP-forming) activity | 6 | 185 (127 taxa) | GO:0004775, IDA, PMID:10671455 (PseudoCAP) | SOUND | Full text: purified SucC+SucD run the SCS reaction in both directions and make ATP from succinyl-CoA, Pi and ADP. | E. coli SucD P0AGE9, human SUCLG1 P53597, rat Suclg1 (RGD:619821), tomato SCS-alpha1/alpha2 Q8GTQ9/Q6DQL1 | Yes; five other characterised alpha subunits, and the term suits an alpha-subunit clade shared by ADP- and GDP-forming enzymes |

sucD does not share a PTN node with sucC: sucC's seed node is PTN000212531 (beta-subunit family).
No node defect to record. No PSEUDOCAP or GO_CENTRAL defect on sucD.
