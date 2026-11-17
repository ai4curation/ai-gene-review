# sucC (PA1588, P53593) notes

## Literature

No deep-research provider was available. PubMed E-utilities returned HTTP 500
on 2026-11-05. The review rests on the full text of PMID:10671455 (cached) and
the reviewed UniProt entry (HAMAP MF_00558).

- SucC and SucD were purified separately; the mixture is active [PMID:10671455
  "an Scs enzymatic reaction was performed with succinate, CoA, and a mixture
  of purified Scs α and β subunits"].
- Dual ADP/GDP specificity [PMID:10671455 "Scs synthesizes essentially an
  equimolar amount of ATP and GTP"]; can also make UTP and CTP at higher NDP
  concentrations.
- NDK-like phosphate transfer from ATP to GDP without succinyl-CoA [PMID:10671455
  "the Scs complex transferred the terminal phosphate from [γ- 32 P]ATP to GDP
  to form GTP"].
- The phosphorylated protein is the 30-kDa alpha subunit [PMID:10671455
  "stimulated the phosphorylation of the 30-kDa Scs α subunit"].

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000212531 | GO:0042709 succinate-CoA ligase complex | 6 | 208 (130 taxa) | GO:0042709, IDA, PMID:10671455 (PseudoCAP) | SOUND | Full text read: activity only from the mixture of purified SucC and SucD. The heteromer was not isolated, but it is reconstituted functionally. | E. coli SucC P0A836, human SUCLG2 Q96I99, mouse MGI:1306775/MGI:1306824, rat RGD:1305008 | Yes. The other seeds are characterised SCS beta subunits; the term suits the whole SCS-beta clade. |
| PTN000212531 | GO:0004775 succinate-CoA ligase (ADP-forming) activity | 5 | 164 (126 taxa) | GO:0004775, IDA, PMID:10671455 (PseudoCAP) | SOUND | Full text read: forward and reverse SCS reactions with ATP/ADP on reconstituted enzyme. | E. coli SucC P0A836, human SUCLA2 Q9P2R7, Arabidopsis Q84LB6, rat RGD:1309397 | Yes. The node term is right for the clade, and the GTP-specific SUCLG2 branch is excluded by a NOT at PTN000929335 (checked in leaf.gaf). |

No PSEUDOCAP defect on the seed rows and no GO_CENTRAL defect.

## Other decisions

- GO:0046777 protein autophosphorylation (PseudoCAP IDA): REMOVE. The labelled
  protein is SucD, and the label is the catalytic phosphohistidine. A PSEUDOCAP
  WRONG_TERM defect is recorded (PROBABLE). Not a seed.
- GO:0004550 NDP kinase activity: MARK_AS_OVER_ANNOTATED. The activity is real
  in vitro but of unknown relevance, and a dedicated Ndk exists.
- GO:0009142 NTP biosynthesis: KEEP_AS_NON_CORE.
- GO:0003824 and GO:0046872: TOO_GENERAL.
