# SAMD8 focused report and reaction-donor assessment

2026-09-21. This follows the full 22-row review in `receptor-and-lipid-claims.yaml`; it is a bounded reaction/report update, not a new source import. The 20 source annotations and two pre-existing authored proposals remain intact.

## Reaction identities and actual ancestry

GO:0047493 uses CDP-choline and produces CMP; the SMS1/SMS2 reaction uses phosphatidylcholine and produces DAG. Live GO:0002950 likewise uses CDP-ethanolamine and produces CMP. Human SMSr instead transfers phosphoethanolamine from PE to ceramide and produces DAG. PMID:19506037, Fig. 2/S1, directly contrasts PE with PC and CDP-ethanolamine; its human expression/knockdown and heterologous yeast experiments establish CPE formation. The modern human structure paper PMID:38388831 independently describes PE hydrolysis followed by phosphoethanolamine transfer to ceramide. Its accessible abstract establishes that mechanism; the full wild-type residual-SMS controls remain inaccessible.

Consequently the broad GO:0016780 core was already correct. No GO:0002950 source assertion occurs in the frozen SAMD8 review. The report's recommendation to upgrade that term is not imported. The existing GO:0047493 IBA is generalized to GO:0016780 because the source reaction mapping has the wrong donor/byproduct, without claiming a universally negative CDP-choline assay. The existing CPE ontology proposal now names the PE donor explicitly.

`SAMD8-reaction-donor-check.json` stores the live definitions, relevant IBD records, exact 19-node lineage and raw full-tree SHA256. Target Q96LT4/SAMD8 is leaf PTN002501711 in PTHR21290:SF25. It descends from PTN000480004 and PTN000480005, through the SMSr branch PTN000480086. PTN000480007 is not on its path; the older notes' two-node shorthand was not an exact target lineage. Current IBD GO:0002950 occurs at PTN000480005, although that newer row is absent from the frozen source review. The actual positive ancestral placements are meaningful; no pairwise similarity or donor-count objection is used. Correcting donor chemistry concerns the term attached to the node, not tree misplacement.

## Critical reuse of the complete provider output

Read `SAMD8-hypotheses/lipid-reaction-spectrum-pathways-and-compartments/openscientist.md`, its CSV decision table, full HTML and extracted PDF. The HTML/PDF repeat the report rather than provide independent experiments. They include sequence-identity percentages but no executable alignment or deposited sequences, so those numbers are not used as verified topology.

The report usefully identifies CPE transfer, ER retention, PLC/PAP chemistry and conditional ceramide-homeostasis phenotypes. Its recommendations need these corrections:

- GO:0002950 is not the measured PE-donor reaction. GO:0047493 is not synonymous with PC-dependent sphingomyelin synthase.
- The wild-type Golgi pool is directly documented in PMID:28120887; the report calls it mutant-only. Keep the prior non-core Golgi annotation.
- The report did not establish absence of a secondary plasma-membrane pool. Its ER-versus-PM argument adds no decisive target exclusion evidence.
- The report's approximately 300-fold CPE/SM comparison is not a general turnover comparison between purified SMSr and SMS1; cellular abundance and assay-specific rates must be distinguished.
- The report explicitly did not retrieve PMID:34332077 or PMID:38388831. Newly read 34332077 supplies human recombinant CPE/PE-PLC positive and NBD-SM negative assays, but cannot substitute for the missing 2024 wild-type controls. Residual SMS and its process scope remain UNDECIDED with a primary-full-text follow-up, not a duplicate provider request.
- Forward consumption of ceramide does not by itself exclude reverse chemistry or pathway-regulatory work. The report's broad no-in-vivo-ceramide-effect claim must now be limited by the conditional 2025 mouse results.
- Keep the pre-existing broad PLC proposal, avoiding redundant new BP or MF rows. Two direct 2021 human studies disagree over broader substrate specificity; no universal pan-PLC or PE-only conclusion is adopted.

## Newly accessed primary evidence and its limits

PMID:40998032 (full Methods, Results, figure captions and Discussion) was not covered by the report. Figure 1 uses human GTEx and liver/adipose transcriptomic data: SMSr/SPT expression associates, but the authors explicitly state that causal direction cannot be determined from observational human RNA-seq. Figures 2–5 use mice and liver microsomes: adenoviral overexpression increases PE-PLC/SPT activity; high-fat/cholesterol-diet knockout reduces SPTLC2 protein, SPT activity and circulating sphingolipids; PE intervention lowers SPTLC2 abundance, and PE added to microsomes lowers SPT activity. Figure 5E co-IP associates tagged SMSr with SPTLC2 in mouse liver. This is evidence of a complex association, not purified binary binding.

The study supplies a plausible PE-sensitive regulatory contribution and strengthens existing GO:2000303. It does not demonstrate that human SMSr catalyzes ceramide formation, nor settle the GO scope of biosynthetic participation versus regulation. Existing GO:0046513 rows remain UNDECIDED for that specific distinction. Human association supports ortholog context but is not labeled a human causal assay. The authors discuss multiple possible mechanisms (ORMDL, Nogo-B, membrane properties, protein stability); none is presented here as established. Chow-fed knockout negative results and developmental compensation qualify the condition dependence. Their claim that low/undetectable CPE excludes all in-vivo CPE function is stronger than the observations and does not cancel demonstrated human CPE catalytic capacity.

PMID:34332077 (full Methods/Results/Discussion) explicitly uses human cDNA for recombinant Sf9 SMSr. Its CPE/PE-PLC activity and negative NBD-SM assay are target-relevant. Its negative PC/PA results conflict with PMID:33621517's broader activities under different preparations; its fluorescent-PI comparison has spontaneous substrate hydrolysis, so that null result is not a clean universal exclusion. Both studies support the broad PLC class, and direct human full-length PAP/PI-PLC results in 33621517 remain cited with their construct/assay limits.

No duplicate OpenScientist request was submitted. Remaining questions are primary-full-text/curator follow-ups, including residual SMS controls, biosynthetic term scope, and antibody-resolved HPA cytosol localization.
