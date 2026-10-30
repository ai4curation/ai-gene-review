# PP_0024 (Q88RV5), P. putida KT2440: notes

Dashboard gene: NZ_CP009974.1_1821 (https://gene-annotate-dashboard.kbase.us/review/NZ_CP009974.1_1821). It is 100% identical over all 565 aa to PP_0024.
Dashboard call (tier A): "Lipid A phosphoethanolamine transferase EptA catalyzing addition of phosphoethanolamine to lipid A." GO terms: GO:0043838 and GO:0009103.

## Conclusion

PP_0024 is a catalytically intact inner-membrane phosphoethanolamine (PEA) transferase of the EptA subfamily (PANTHER PTHR30443:SF0). It has five N-terminal TM helices and a periplasmic sulfatase-fold domain. The Neisseria LptA nucleophile T280 and Zn ligands E240, D452, H453 and H465 align to PP_0024 T296, E258, D468, H469 and H481. Its acceptor is unknown. It is **not** the KT2440 EptA orthologue.

- **Two EptA-subfamily paralogs in KT2440.** UniProt PANTHER SF0 lists PP_0024 and PP_4592. PP_2579 (CptA) is SF2.
- **PP_4592 is the EptA orthologue.** It is 61.4% identical to P. aeruginosa EptA PA1972 (characterized lipid A 4'-PEA transferase, PMID:25846400) and 67% to P. syringae EptA.
- **PP_0024 is equidistant.** It is 47.4% identical to PA1972, 44.2% to PA3310, 45% to E. coli EptA, 41% to MCR-1 and 39% to Neisseria LptA, but only 28-34% to EptB, EptC/CptA and OpgE. Global alignments: BERIL run `20261030T213838Z-pp0024-pea-paralogs`.
- **Paralogs at this distance can have other acceptors.** In P. aeruginosa, the EptA-like paralog PA3310 (PA14_21210) gives only trace lipid A modification and "lipid A is probably not the primary target" (PMID:25846400).
- **Fitness (KT2440, BERDL `kescience.fitnessbrowser`, run `20261030T214120Z-pp0024-fitness`).**
  - PP_0024 has no phenotype (|fit| < 0.33) in all 300 experiments, including four polymyxin B (1 µg/ml) and one 2 µg/ml experiment.
  - PP_4592 is the only gene in the set with a specific phenotype, in polymyxin B: fit −1.04 (t −7.0), with the other replicates at −0.59 to −0.73.
  - The polymyxin-protective lipid A PEA transferase activity in KT2440 therefore tracks PP_4592.
  - The KT2440 compendium has no zinc or aluminium experiments.
- **Neighbourhood.** PP_0024 lies in a metal-resistance region (PP_0014–PP_0049). Nearby are a CzcD-family exporter (PP_0026), a heavy-metal TCS (PP_0029/PP_0030), CadA (PP_0041) and Czc efflux genes (PP_0043–PP_0045). This hints at a metal-stress role. It does not tell us the acceptor.
- **Regulation.** The P. putida ColRS (zinc) regulon includes the PEA transferase PP2579/CptA, not PP_0024 (PMID:24946800, PMID:19445690).
- **P. putida lipid A.** Analyses of KT2442 (PMID:26579930, PMID:32673427) report hexa- and penta-acyl species, with "less modification" than in P. aeruginosa. Neither abstract mentions PEA. The 2020 LC-MS/MS study reports "several lipid A species ... not previously described", and its full text (not available here) was not checked for PEA.

## Dashboard verdict

**Overreach** (the dashboard's verdict 2).
- The family and the reaction type (PEA transfer from phosphatidylethanolamine) are right.
- The gene name EptA and the lipid A substrate are not supported.
  - The cited homologs (46.1% P. aeruginosa, 45.1% P. syringae) are outparalogs. Their KT2440 orthologue is PP_4592.
  - The aluminium and polymyxin phenotypes are from 39–45% homologs in other genera, so they are not specific to this paralog.
- Suggested annotation: "Putative phosphoethanolamine transferase, EptA-like paralog (not the EptA orthologue PP_4592); acceptor unknown."
- GO:0043838 = UNC. Lipid A is not refuted, so this is not PLI.
- GO:0009103 = UNC.
- The companion review adds GO:0016780 (ISS).

## GOA actions

| Term | Action |
|---|---|
| GO:0005886 plasma membrane | ACCEPT |
| GO:0016020 membrane | ACCEPT |
| GO:0009244 LPS core region biosynthesis | MARK_AS_OVER_ANNOTATED |
| GO:0016772 | TOO_GENERAL → GO:0016780 |
| GO:0016776 phosphate-as-acceptor | MODIFY → GO:0016780 (wrong EC class; GO:0043838 sits under GO:0016780) |
| GO:0016780 | NEW (ISS) |

## Caveats

- No experiment on PP_0024 exists.
- Lipid A remains a plausible acceptor: some bacteria carry two lipid A PEA transferases. The absence of a fitness phenotype could reflect redundancy with PP_4592.
- The deep-research report places the nucleophile at Thr259 (GETARS). Alignment to Neisseria LptA places it at Thr296 (SCGTATA). The report is wrong on this point.
- `just fetch-fitness` failed: the FEBA site and bulk download were unreachable. Fitness was read from BERDL instead.
  - The MCP query endpoint needs a curl User-Agent.
  - Paging an unordered multi-gene join over offsets gave duplicated and missing rows. The final run uses one ordered query per gene.
