# sctN (YscN, P40290) — Yersinia enterocolitica Ysc injectisome ATPase — curation notes

## Identity

- UniProt P40290, gene `sctN` (synonym `yscN`), first gene of the virB locus on the pYV virulence plasmid
  [PMID:8132449 "It is the first gene of the virB locus"].
- UniProt RecName is "Type 3 secretion system ATPase", EC 7.4.2.8 (protein-exporting ATPase) — **not** an
  ATP-synthase EC. This contrasts with several flagellar FliI entries, which UniProt still calls
  "Flagellum-specific ATP synthase" with EC 7.1.2.2. So for this gene the protein name/EC is already correct and
  the synthase-flavoured GO rows come purely from PANTHER/InterPro pipelines.
- **Do not confuse with YsaN**, the ATPase of the chromosomal Ysa–Ysp T3SS of the same organism. YsaN
  biochemistry (Mg2+ dependence, YsaL inhibition) is a different protein and is not evidence for P40290
  (flagged in `sctN-deep-research-falcon.md`, "Critical ambiguity resolved: SctN/YscN is not YsaN").

## Family placement (relevant to the ATP-synthase GO rows)

- PANTHER PTHR15184 "ATP SYNTHASE"; P40290 is in subfamily **PTHR15184:SF9** (SPI-1 type 3 secretion system
  ATPase), i.e. the T3SS/FliI export-ATPase branch, not the F1-beta branch (SF51/SF74/SF75/SF76/SF80/SF82/
  SF83/SF85).
- `interpro/panther/PTHR15184/PTHR15184-paint.tsv`: the GO:0046933 IBD sits at **PTN008558586**, seeded by
  PomBase SPAC222.12c, SGD S000003882, UniProtKB:P06576 (human ATP5F1B), UniProtKB:P0ABB4 (E. coli AtpD) —
  all genuine F1-beta subunits.
- `projects/TREEGRAFTER/rotary_atpase/node_placement.tsv`: **PTN001807733** (the WITH/FROM on this gene's
  GO:0046933 row) is a TreeGrafter graft node in clade **PTN000390097**, the eubacterial sister clade of the
  F1-beta clade PTN008558588 under the same IBD node. PTN000390097 contains exactly the export-ATPase
  subfamilies SF9 / SF62 / SF81. So the graft sits under an IBD node whose function arose in (and is
  experimentally grounded only in) the F1-beta sister clade — a paralog over-propagation across a duplication
  node, not an inheritance the target shares.

## Experimental evidence on this protein

- **ATPase, cooperative, YscL-regulated.** Purified HisYscN is an ATPase; activity is inhibited by HisYscL
  [PMID:16672607 "A biochemical analysis of YscN reveals it to be a highly cooperative ATPase whose activity is
  inhibited by the addition of YscL."]. The paper frames the system as
  ["The bacterial energy source for secretion is ATP, which is consumed by an ATPase that couples ATP hydrolysis
  to the unfolding of secreted proteins and the dissociation of their chaperones just prior to secretion"].
  Inhibition is non-competitive/allosteric.
- **Required for Yop secretion; Walker-A dependent.** A pYV mutant lacking box A is secretion-defective and
  complementable [PMID:8132449 "This mutant, impaired in Yop secretion, can be complemented in trans by a cloned
  yscN gene."]; the Walker-box point mutant is likewise non-functional
  [PMID:20453832 "Secretion could be complemented in trans by a wild-type yscN allele, but not by an yscN allele
  encoding YscN K175E altered in the Walker box"].
- **Substrate/secretion-signal recognition.** YopR (encoded by yscH, UniProtKB:Q01249) hybrids capture YscN in
  vivo and purified HisYscN binds YopR-GST but not signal-deleted YopR
  [PMID:17050689 "we observed His YscN binding to YopR-GST, its in vivo substrate"]. This is the IPI row's
  experiment: it is substrate-signal recognition by the export ATPase, not generic protein binding.
- **Cytosolic sorting platform.** EGFP-YscN localizes to injectisome foci; its assembly requires YscC, YscJ,
  YscK, YscL and YscQ, and YscN is in turn needed for C-ring formation — structurally, not catalytically, since
  YscN K175E still supports C-ring formation [PMID:20453832]. YscN is also part of stable *cytosolic* K/Q/L/N
  complexes [PMID:28653671], and is fully cytosolic when YscQ_C is absent [PMID:25591178].
- **Hexamer.** [PMID:20453832 "At the cytosolic side of the injectisome, an ATPase of the AAA + family (YscN)
  forms a hexameric ring that is activated by oligomerization"]. Blaylock et al. could not observe hexamers with
  refolded recombinant protein.
- **Localization.** Cytoplasm (UniProt SUBCELLULAR LOCATION from PMID:16672607); peripheral, at the cytoplasmic
  face of the injectisome basal body.

## Energetics — why the proton terms are wrong for this protein

- Yersinia type III secretion needs the PMF, but the dependency is a property of the machine, not of YscN:
  [PMID:15213145 "Motility as well as type III-dependent secretion of Yop proteins was inhibited by CCCP."]
- In the homologous flagellar system the proton flux is carried by the membrane export gate, not by the soluble
  ATPase [PMID:21934659 "the export gate complex by itself is a proton-protein antiporter";
  PMID:29946050 "FlhA has an ion channel activity, and the FlhA-FliJ interaction enables effective utilization
  of PMF for protein export"].
- The homologous FliI ATPase is insensitive to F-, V- and P-type ATPase inhibitors
  [PMID:8943245 "The activity was not affected by inhibitors of the F-, V- or P-type ATPases"], i.e. it is not
  an F-type enzyme despite the fold.
- The rotary-like architecture is real (SctO/YscO is the gamma-stalk analogue
  [PMID:25591178 "a protein with homology to the central stalk of the FoF1-ATPase that stimulates ATPase
  activity (SctO; YscO)"]; FliJ binds the centre of the FliI hexamer
  [PMID:21278755 "FliJ promotes the formation of FliI hexamer rings by binding to the center of the ring"]),
  but there is no Fo-like proton channel partner and no ATP synthesis. Structural rotary homology is not
  proton-transporting ATPase activity.

## Mechanism (ortholog support)

Chaperone release and substrate unfolding are shown for the Salmonella SPI-1 ortholog InvC
[PMID:16208377 "InvC induces chaperone release from and unfolding of the cognate secreted protein in an
ATP-dependent manner"]; the same role is assumed for SctN/YscN [PMID:25591178, PMID:28653671]. Note the
flagellar-system caveat that export can proceed without ATPase activity under some conditions — for Yersinia,
however, YscN catalytic activity is required for secretion (K175E is secretion-null).

## Annotation decisions (summary)

| Term | Evid | Source | Action |
|---|---|---|---|
| GO:0046933 ATP synthase activity, rotational | IEA | GO_REF:0000118, PTN001807733 | REMOVE |
| GO:0015986 PMF-driven ATP synthesis | IEA | GO_REF:0000108 from GO:0046933 | REMOVE |
| GO:0046961 proton-transporting ATPase, rotational | IEA | GO_REF:0000002, IPR013380 | REMOVE |
| GO:1902600 proton transmembrane transport | IEA | GO_REF:0000002, IPR004100 | REMOVE |
| GO:0006754 ATP biosynthetic process | IEA | GO_REF:0000002, IPR013380 | REMOVE |
| GO:0046034 ATP metabolic process | IEA | GO_REF:0000002, IPR004100 | MARK_AS_OVER_ANNOTATED |
| GO:0008564 protein-exporting ATPase activity | IEA | GO_REF:0000003, EC:7.4.2.8 | ACCEPT (core MF) |
| GO:0016887 ATP hydrolysis activity | IEA | GO_REF:0000002 | ACCEPT |
| GO:0005524 ATP binding | IEA | GO_REF:0000002 | ACCEPT |
| GO:0030254 protein secretion by T3SS | IEA | GO_REF:0000002 | ACCEPT |
| GO:0030257 T3SS complex | IEA | GO_REF:0000002 | ACCEPT |
| GO:0005737 cytoplasm (EXP + IEA) | EXP/IEA | PMID:16672607 / GO_REF:0000120 | ACCEPT |
| GO:0005515 protein binding | IPI | PMID:17050689, Q01249 | MODIFY → GO:0008564 |

IPR013380 (T3SS ATPase SctN) is the InterPro entry that carries both GO:0046961 and GO:0006754 — a
T3SS-specific signature mapped to rotary-ATP-synthase terms. That mapping is wrong at source and affects every
SctN protein, so it is raised as a suggested question.
