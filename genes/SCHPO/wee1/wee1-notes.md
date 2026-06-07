# wee1 (S. pombe) — Gene Review Notes

UniProt: P07527 (WEE1_SCHPO), 877 AA, EC 2.7.10.2. ORF SPCC18B5.03. PomBase: SPCC18B5.03.

## Core identity / function

Wee1 is the prototype dose-dependent negative regulator of mitotic entry (G2/M transition) in fission yeast, the founding member of the WEE1 kinase subfamily. It is a dual-specificity (Ser + Tyr) protein kinase whose key substrate is the cyclin-dependent kinase Cdc2 (Cdk1): it phosphorylates Cdc2 on the inhibitory residue Tyr15, holding Cdk1 inactive until cells reach the threshold size for division. The opposing phosphatase Cdc25 removes this phosphate to drive mitosis. Loss of wee1 causes premature mitosis at half the normal cell size ("wee" small-cell phenotype).

- [PMID:3032459 "Fission yeast wee1- mutants initiate mitosis at half the cell size of wild type."]
- [PMID:3032459 "Thus wee1+ functions as a dose-dependent inhibitor of mitosis, the first such element to be specifically identified and cloned."]
- [PMID:3032459 "The carboxy-terminal region of the predicted 112 kd wee1+ protein contains protein kinase consensus sequences, suggesting that negative regulation of mitosis involves protein phosphorylation."]
- [PMID:3032459 "Genetic evidence indicates that wee1+ and cdc25+ compete in a control system regulating the cdc2+ protein kinase, which is required for mitotic initiation."]

### Dual-specificity kinase / direct Cdc2 Tyr15 phosphorylation
- [PMID:1825699 "Here we report that p107wee1 immune complexes phosphorylate p107wee1 equally on serine and tyrosine residues, and also phosphorylate an exogenous substrate, angiotensin II, on tyrosine."] — Featherstone & Russell; tyrosine/serine kinase. Note UniProt FUNCTION cites this (PubMed:1825699): "Protein kinase that acts both on serines and on tyrosines."
- [PMID:1825699 "Thus the wee1+ gene product is representative of a novel class of protein kinase that phosphorylates both serine and tyrosine residues."]
- [PMID:1372994 "Serine and tyrosine kinase activities cofiltered with p37wee1KD, demonstrating that p107wee1 is a dual-specificity kinase."]
- [PMID:1372994 "In vitro, p107wee1 phosphorylated p34cdc2 on Tyr-15 only when p34cdc2 was complexed with cyclin."]
- [PMID:1372994 "These results indicate that p107wee1 functions as a mitotic inhibitor by directly phosphorylating p34cdc2 on Tyr-15 and that the preferred substrate for phosphorylation is the p34cdc2/cyclin complex."]
- Note: GOA also has IDA Ser/Thr kinase activity from PMID:8256510, PMID:7681363, PMID:9034337 (in those papers wee1 is used as substrate or its kinase activity is assayed). PMID:8256510 shows 32P-p107wee1 is a substrate for the pyp1 phosphatase: [PMID:8256510 "32P-labeled p107wee1 is an in vitro substrate for pyp1."]

## Domain / catalytic features (UniProt)
- Protein kinase domain 566-843; ATP binding 572-580, 596; active site (proton acceptor) 693; Mg2+ binding 698, 711 ("Binds 2 magnesium ions per subunit").
- MUTAGEN K596L inactivates enzyme. Belongs to protein kinase superfamily, Ser/Thr family, WEE1 subfamily.
- Large N-terminal disordered region (1-~435); the N-terminal noncatalytic region mediates regulation/localization (Cdr2 interaction, see below).

## Regulation
- Wee1 is itself negatively regulated by phosphorylation, especially by Nim1/Cdr1 in its C-terminus: [PMID:7681363 "The nim1-catalyzed phosphorylation of the wee1 protein occurs in its C-terminal region and leads to a substantial drop in its activity as a cdc2-specific tyrosine kinase."] and [PMID:7681363 "These experiments provide direct biochemical evidence that the wee1 protein is subject to negative regulation by phosphorylation and indicate that the nim1 protein acts as an inhibitory, wee1-specific kinase."] UniProt PTM: "Phosphorylated in the C-terminal by NIM1/CDR1."
- Cdr1 and Cdr2 (SAD kinases) act upstream as inhibitors; Cdr2 nodes recruit Wee1 to the cortex for inhibitory phosphorylation.

## Localization
- UniProt SUBCELLULAR LOCATION: Nucleus {PubMed:10759889}. GOA: nucleus IDA (PMID:19474789), nucleoplasm TAS Reactome.
- [PMID:19474789] — Wee1 is part of medial cortical nodes with Cdr1, Cdr2, Mid1. Annotated medial cortical node (GO:0071341) IDA, mitotic spindle pole body (GO:0044732) IDA, nucleus IDA. Full text of related paper (PMID:29514920): "Wee1 primarily localizes in the nucleus and the spindle pole body (SPB), where it can interact with Cdk1" and "By live-cell total internal reflection fluorescence (TIRF) microscopy, we discovered that endogenous Wee1 localizes to Cdr2 nodes in transient bursts."
- mitotic spindle pole body also HDA from PMID:16823372 (genome-wide YFP screen): [PMID:16823372 "we determined the localization of 4,431 proteins, corresponding to approximately 90% of the fission yeast proteome, by tagging each ORF with the yellow fluorescent protein."]
- Cytoplasm (GO:0005737) is IBA only; the predominant experimental localization is nuclear / SPB / medial nodes.

## Cell-size control / nodes (Cdr2 medial cortical node complex)
- [PMID:29514920 "In fission yeast, the protein kinase Cdr2 forms cortical nodes that include the Cdk1 inhibitor Wee1 along with the Wee1-inhibitory kinase Cdr1."]
- [PMID:29514920 "Recruitment of Wee1 to nodes required Cdr2 kinase activity and the noncatalytic N terminus of Wee1."]
- [PMID:29514920 "increasing Cdr2 activity during cell growth promotes Wee1 localization to nodes, where inhibitory phosphorylation of Wee1 by Cdr1 and Cdr2 kinases promotes mitotic entry."]
- Cdr2 node complex part_of (GO:0110115) annotated EXP (PMID:29514920) and NAS (PMID:34958661).
- [PMID:34958661 "The protein kinase Cdr2 contributes to this size control system by forming multiprotein nodes that inhibit Wee1 at the medial cell cortex."]
- G2 cell size control checkpoint signaling (GO:0031569): IMP PMID:872890 (the classic Nurse & Thuriaux cdc/wee size-control paper), EXP PMID:29514920, NAS PMID:34958661.
- NOT mitotic G1 cell size control checkpoint signaling (GO:0031568): negated IMP PMID:872890 — wee1 controls G2 size, not a G1 size checkpoint (S. pombe controls size predominantly at G2/M; the G1 size requirement is normally cryptic). Keep as accurate negation.

## DNA damage / replication / cytokinesis checkpoints (Wee1 as effector)
- DNA damage checkpoint (GO:0044773, IGI PMID:12186947 with chk1 SPBC29A10.15): [PMID:12186947 "We show here that in G1-arrested orp1-4 cells, Wee1 phosphorylates and inactivates Cdc2."] Also Chk1 phosphorylates Wee1 in G2 DNA damage response: [PMID:9034337 "wee1 is required for cell cycle arrest induced by up-regulation of an essential component of this checkpoint, chk1"] and [PMID:9034337 "p56chk1 can phosphorylate p107wee1 directly in vitro."] (PMID:9034337 in GOA supports Ser/Thr kinase activity IDA.)
- Cytokinesis checkpoint (GO:0044878, IMP PMID:10704373): [PMID:10704373 "The G(2)/M transition defect of cps1-191 mutants is suppressed by a mutation in the wee1 gene"] and [PMID:10704373 "We conclude that an F-actin and Wee1p dependent checkpoint blocks G(2)/M transition until previous cytokinesis is completed."]

## Meiotic role (GO:0110031 negative regulation of G2/MI transition of meiotic cell cycle)
- This is a GENUINE meiotic role (unlike the autophagy "mug"-keyword over-annotations described in projects/SPKW-SCHPO.md). Wee1 (with Mik1) inhibits CDK to prevent premature meiotic divisions when the replication checkpoint is active.
- [PMID:25492408 "Meanwhile, activation of Cds1 inhibits CDK activity by activating Mik1 and Wee1 tyrosine kinases (Murakami & Nurse 1999), thus preventing entry into meiotic nuclear divisions."]
- [PMID:25492408 "These results indicate that inactivation of Mik1/Wee1 triggers nuclear divisions, consistent with the results obtained from the Cdc25 overproduction experiments."]
- [PMID:25492408 "These results indicate that inactivation of Mik1/Wee1 overcomes the DNA replication checkpoint."]
- GOA: GO:0110031 IMP PMID:25492408 and IBA. ACCEPT — direct meiotic effector role via Tyr15 phosphorylation of Cdc2.

## Kinetochore-microtubule attachment (GO:1902425 positive regulation of attachment of mitotic spindle microtubules to kinetochore)
- [PMID:38166399 "Wee1 catalyses an inhibitory tyrosine phosphorylation of Cdc2/Cdk1, a cyclin-dependent kinase essential for G2/M transition."]
- [PMID:38166399 "the wee1 mutant cannot maintain stable kinetochore-microtubule attachment, and relies on the delay imposed by the spindle checkpoint for establishing biorientation of kinetochores."]
- [PMID:38166399 "This study revealed a role of Wee1 in ensuring accurate segregation of chromosomes during mitosis"]
- This is a newly described, distinct mitotic role (EXP, 2024). Genetic analysis showed the requirement is NOT due to early mitotic onset, so it is mechanistically separable from the canonical Tyr15/size-control function. Accept but treat as non-core (a secondary mitotic function).

## MF / catalytic IEA annotations
- protein kinase activity (GO:0004672) IEA InterPro — accurate parent, KEEP_AS_NON_CORE/ACCEPT as grouping.
- protein tyrosine kinase activity (GO:0004713) IEA RHEA + IDA/IBA — core (Tyr15 of Cdc2).
- non-membrane spanning protein tyrosine kinase activity (GO:0004715) IEA EC 2.7.10.2 — EC mapping; Wee1 is not membrane-associated, accurate but generic; keep.
- protein serine/threonine kinase activity (GO:0004674) IDA (PMID:9034337, 7681363, 8256510, 1372994) — Wee1 has Ser/Thr activity (dual specificity; autophosphorylates Ser). ACCEPT.
- ATP binding (GO:0005524) IEA — standard kinase cofactor, ACCEPT. (UniProt: ATP binding 572-580, 596; K596L inactivates.)
- metal ion binding (GO:0046872) in DR but not in GOA tsv stub — Mg2+ binding (2 ions/subunit). Not in the review stub, so not added.

## Summary of action plan
- MF tyrosine kinase / Ser/Thr kinase / ATP binding: core or accept.
- BP negative regulation of G2/M transition (GO:0010972): CORE.
- BP G2 cell size control checkpoint (GO:0031569): ACCEPT (core regulatory readout).
- BP meiotic G2/MI (GO:0110031): ACCEPT (genuine, non-core relative to mitotic role).
- Checkpoints (DNA damage GO:0044773, cytokinesis GO:0044878): ACCEPT non-core (Wee1 is the shared effector that enforces G2 delay).
- Kinetochore-MT attachment (GO:1902425): ACCEPT non-core.
- Cdr2 node complex (GO:0110115) / medial cortical node (GO:0071341) / SPB (GO:0044732) / nucleus: ACCEPT (nucleus + nodes/SPB are the real sites). cytoplasm IBA (GO:0005737): KEEP_AS_NON_CORE (generic; predominant localization is nuclear/SPB/nodes).
- NOT G1 cell size checkpoint (GO:0031568): ACCEPT the negation.
- nucleoplasm TAS Reactome: ACCEPT (subdivision of nucleus).
