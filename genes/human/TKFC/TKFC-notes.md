# TKFC (Triokinase/FMN cyclase, Q3LXA3) — review notes

Deep research: `just deep-research human TKFC --provider falcon` was attempted twice; both
runs exited non-zero and produced no `-deep-research-falcon.md`. Review is therefore grounded
in the UniProt record (`TKFC-uniprot.txt`), the seeded GOA, and cached `publications/PMID_*.md`.
Did NOT fabricate a `-deep-research-*.md` file.

## Core biology (verified)

TKFC is a cytosolic, homodimeric **bifunctional** enzyme (UniProt Q3LXA3; DAK family). Two domains:
DhaK (aa 9-336) and DhaL (aa 372-571). Individually DhaK is inactive and DhaL shows cyclase but not
kinase activity [file:TKFC-uniprot.txt DOMAIN; PMID:24569995].

Activity 1 — **ATP-dependent dihydroxyacetone / triokinase (DHA kinase)** (EC 2.7.1.29 and 2.7.1.28):
- dihydroxyacetone + ATP = dihydroxyacetone phosphate + ADP + H+ (RHEA:15773, EC 2.7.1.29)
- D-glyceraldehyde + ATP = D-glyceraldehyde 3-phosphate + ADP + H+ (RHEA:13941, EC 2.7.1.28)
- Phosphorylates the D-glyceraldehyde produced by ALDOB in fructolysis, returning fructose carbon
  to glycolysis; also phosphorylates DHA. [PMID:32004446, PMID:4688871]

Activity 2 — **FAD-AMP lyase (cyclizing) / FMN cyclase** (EC 4.6.1.15):
- FAD = riboflavin cyclic-4',5'-phosphate + AMP + H+ (RHEA:13729). Only known enzymatic source of
  riboflavin 4',5'-cyclic phosphate (cyclic FMN). Requires Mn2+ or Co2+. [PMID:16289032, PMID:4688871]
- Each activity inhibited by the substrate(s) of the other (single/overlapping active center). [PMID:16289032]

Activity 3 (regulatory, moonlighting) — **negative regulation of MDA5 (IFIH1) antiviral signaling**:
- DAK is a specific MDA5-interacting protein; overexpression inhibits MDA5- (not RIG-I-) mediated
  IFN-beta induction; knockdown activates it. Interacts via IFIH1 CARD domains; interaction inhibited
  by viral infection. [PMID:17600090]

Disease: **TKFC deficiency (TKFCD, MIM:618805)** — autosomal recessive; cataracts + developmental
delay ± cerebellar hypoplasia, liver dysfunction, microcytic anemia, fatal cardiomyopathy with lactic
acidosis after febrile illness. Bi-allelic variants in FMN lyase domain (G445S, R543I). [PMID:32004446]

## Annotation decisions (summary)

- Catalytic MF terms glycerone kinase (GO:0004371), triokinase (GO:0050354), FAD-AMP lyase
  (GO:0034012): ACCEPT — directly demonstrated (IDA) and phylogenetically supported (IBA).
- ATP binding (GO:0005524): ACCEPT — required for kinase; matches ATP-binding residues in UniProt.
- Glycerol catabolic/metabolic (GO:0019563 IBA, GO:0006071 IEA): the human enzyme's physiological
  triose substrates are DHA and glyceraldehyde in fructose metabolism, not glycerol. These are
  DAK-family phylogenetic/InterPro over-generalizations (some bacterial DAK orthologs act in glycerol
  catabolism). MODIFY IBA glycerol catabolic -> fructose catabolic; MARK_AS_OVER_ANNOTATED the IEA
  glycerol metabolic.
- Fructose catabolic (GO:0006001 IEA, Ensembl): MODIFY to the more specific GO:0061624 (which the
  UniProt DR line and Ensembl actually assert).
- Cytosol (GO:0005829 IBA + 4 Reactome TAS): ACCEPT — bona fide cytosolic localization.
- protein binding (GO:0005515 IPI x2, IFIH1/Q9BYX4 and SDCBP/O00560): MARK_AS_OVER_ANNOTATED
  (uninformative bare term; IFIH1 interaction better captured by GO:0039534).
- neg reg MDA-5 signaling (GO:0039534 IDA, PMID:17600090): ACCEPT.
- regulation of innate immune response (GO:0045088 IDA, PMID:16289032): general parent of the MDA5
  role but attributed here to the FAD-AMP-lyase paper; KEEP_AS_NON_CORE.
- carbohydrate metabolic process (GO:0005975 IDA x2), carbohydrate phosphorylation (GO:0046835 IDA):
  correct but general; KEEP_AS_NON_CORE.
- extracellular exosome (GO:0070062 HDA x2), nucleus (GO:0005634 HDA): mass-spec bulk-proteomics
  localizations for a cytosolic enzyme; MARK_AS_OVER_ANNOTATED.
