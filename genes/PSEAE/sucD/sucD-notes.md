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

## Reconciliation with the other bacterial SCS reviews (2026-11-18)

The six bacterial succinyl-CoA synthetase reviews (PSEAE, PSEPK and ECOLI sucC and sucD) were compared. PMID:10671455 was re-read in full. Changes to this review:

- core_functions now use contributes_to_molecular_function, as the PSEPK and ECOLI reviews do and as this review's own GO:0004775 IDA reason already said. Both entries now carry in_complex GO:0042709 and location cytosol.
- Cytosol added as a NEW row with evidence IC. GOA has no location row for Q51567 and the alpha family has no cytosol IBD that reaches SucD (its only one is at the SF24 clade PTN001671414). The location is inferred, not measured: HAMAP MF_01988 family membership with no signal or transmembrane feature, the obligate heterotetramer with SucC, and 89% identity to E. coli SucD [PMID:10671455 "showed 89% amino acid sequence identity to the E. coli Scs α subunit"], which has IDA cytosol rows. The recombinant protein was purified from a cleared E. coli lysate (15,000 rpm, 10 min); that is a low-speed supernatant from a heterologous host and is not used as support.
- Length. The description said 288 residues, which is the paper's figure [PMID:10671455 "The sucD gene encodes the Scs α subunit (288 amino acids)"]. The reviewed UniProt record Q51567 is 295 residues and carries CONFLICT features against the original sequence; the description now gives 295.
- Nucleotide wording. No rates were measured, so "at a rate comparable to ATP formation" and "as readily as ATP" were replaced. GTP is formed from GDP alone [PMID:10671455 "either ADP or GDP could act as a substrate at the lowest concentration tested (50 μM)"]; the equimolar result is a 10-minute end-point [PMID:10671455 "At equal concentrations, both GTP and ATP were synthesized in essentially equal amounts."]. GO:0004776 stays ACCEPT and core, a real difference from E. coli that the authors state themselves [PMID:10671455 "the P. aeruginosa Scs has a different specificity for NTP production"].
- GO:0004550 NDP kinase activity stays MARK_AS_OVER_ANNOTATED. Added: the alpha subunit alone gave GTP in the Ndk-modulation assay [PMID:10671455 "the Scs α subunit alone (lane 3) or a combination α and β subunits (lane 7) generated GTP in presence of GDP, CDP, and UDP"]. The nucleotide site of SCS is on the beta subunit, and the authors' Ndk-contamination control addresses only the phosphate-dependent reaction, so a host contaminant in the His-tagged alpha preparation is not excluded for the ATP-dependent transfer.
- GO:0009142 now quotes the four-NTP sentence of the abstract, the same quote as the sucC row.
- Seed assessment above: Q51567 is also a seed of the GO:0004776 IBD at PTN000122012, through the UniProt EXP row from PMID:10671455 (it is in the WITH/FROM of this gene's GO:0004776 IBA). That seed row is sound: GTP formation from GDP by the reconstituted enzyme was shown directly. "No node defect to record" is superseded by the family review, interpro/panther/PTHR11117/PTHR11117-review.yaml, which names leaves that should not inherit the node terms (for example Aquifex aeolicus O67729); that does not concern Q51567.
- Action counts are now ACCEPT 11, MARK_AS_OVER_ANNOTATED 1, KEEP_AS_NON_CORE 1, TOO_GENERAL 1, NEW 1.
- Not done here: the family reviews and modules/tca_cycle.yaml do not yet cite this review; that is outside this change.
