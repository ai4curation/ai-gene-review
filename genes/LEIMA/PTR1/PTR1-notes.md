# PTR1 (Leishmania major, Q01782) - curation notes

**Note:** Automated deep research (Falcon/OpenAI) was unavailable in this environment.
These notes are a manual literature review based on the UniProt record, the cached
publications, and targeted PubMed/web searches. All PMIDs below were verified against
PubMed (esummary titles) before caching.

## Identity

- Pteridine reductase 1, EC 1.5.1.33; synonyms HMTXR (H-region methotrexate resistance
  protein), LmjF.23.0270. 288 aa, short-chain dehydrogenase/reductase (SDR) family,
  homotetramer (UniProt).
- Originally identified as the amplified H-region gene conferring methotrexate (MTX)
  resistance [PMID:1339441 "We have now identified hmtxr as the H region gene conferring MTX resistance using a transfection-based approach."].
  That paper placed it in the aldo-keto reductase grouping; later kinetic/stereochemical
  work placed it firmly in the SDR family [PMID:9521731 "The kinetic mechanism and stereochemical course for the catalyzed reaction confirm PTR1's membership within the short chain dehydrogenase/reductase (SDR) family."].

## Molecular function

- NADPH-dependent reduction of unconjugated pterins (biopterin -> H2B -> H4B) and folates:
  [PMID:7972081 "PTR1 purified from engineered Escherichia coli exhibited a MTX-sensitive, NADPH-dependent biopterin reductase activity."]
  [PMID:7972081 "PTR1 showed good activity with folate and significant activity with dihydrofolate and dihydrobiopterin, but not with quinonoid dihydrobiopterin."]
- Two-step reduction mechanism, structurally resolved:
  [PMID:11373620 "PTR1 catalyzes the NADPH-dependent two-step reduction of oxidized pterins to the active tetrahydro-forms and reduces susceptibility to antifolates by alleviating dihydrofolate reductase (DHFR) inhibition."]
  [PMID:11373620 "The first reduction uses the generic SDR mechanism, whereas the second shares similarities with the mechanism proposed for DHFR."]
- Folate -> DHF -> THF (DHFR-like reaction, same stereochemistry):
  [PMID:9521731 "With folate as a substrate, PTR1 catalyzes two rounds of reduction, yielding 5,6,7, 8-tetrahydrofolate and oxidizing 2 equiv of NADPH."]
  [PMID:9521731 "PTR1 transfers the pro-S hydride of NADPH to carbon 6 on the si face of dihydrofolate, producing the same stereoisomer of THF as does dihydrofolate reductase."]
  -> supports NEW GO:0004146 dihydrofolate reductase activity (GO definition: THF + NADP+ = DHF + NADPH).
  This is not in GOA for Q01782. PTR1 is the catalyst, so no participation concern.
- Tetramer: [PMID:9153248 "Recombinant L. major and Leishmania tarentolae, and native L. major PTR1s, were tetramers of 30-kDa subunits"].
- MTX insensitivity relative to DHFR-TS: [PMID:9153248 "PTR1 exhibited 2000-fold less sensitivity to inhibition by methotrexate than dihydrofolate reductase-thymidylate synthase"].

### Quinonoid dihydropteridine reductase (QDPR) activity - conflicting evidence

- Bello 1994 reported no activity with qH2B (quote above, PMID:7972081; abstract only).
- Ong 2011 (full text) used an HPLC/spectrophotometric assay and found NADPH-dependent
  QDPR activity in both TbPTR1 and LmPTR1:
  [PMID:21239486 "we demonstrate that there is an NADPH-dependent QDPR activity associated with both TbPTR1 and LmPTR1"]
  [PMID:21239486 "Specificity constants (k(cat)/K(m)) for LmPTR1 are similar with dihydrobiopterin (H(2)B) and quinonoid dihydrobiopterin (qH(2)B) as substrates and about 20-fold lower than LmQDPR with qH(2)B."]
- So GO:0004155 6,7-dihydropteridine reductase activity (IDA, PMID:21239486) is supported, but in
  L. major the dedicated LmQDPR is ~20-fold more efficient, so this is a secondary activity
  for LmPTR1 (the dual role is more important in T. brucei, which lacks QDPR). Keep as non-core.
- The UniProt FUNCTION comment still carries the 1994 negative statement; newer data supersede it.

## Biological process

- Pterin salvage: Leishmania are pterin auxotrophs; PTR1 is the primary salvage enzyme:
  [PMID:7972081 "We generated Leishmania lacking PTR1 by homologous gene targeting, and these ptr1- mutants required reduced biopterin (dihydro- or tetrahydrobiopterin) for growth."]
  [PMID:9153248 "studies of ptr1(-) and dhfr-ts- mutants implicated only PTR1 in the ability of L. major to grow on a wide array of pterins."]
  -> GO:0006729 tetrahydrobiopterin biosynthetic process (IEA, UniPathway) is appropriate: the
  enzyme catalyses the formation of H4B from biopterin (salvage rather than de novo GTP route,
  which kinetoplastids lack [PMID:21239486 "These parasites lack the biosynthetic pathway to H4B and are auxotrophic for pterins"]).
- Antifolate resistance: PTR1 amplification confers MTX resistance (bypass of DHFR-TS and/or drug
  sequestration). This is a pharmacological phenotype, not a normal biological process; I did not
  propose "response to methotrexate".
- Downstream phenotypes (metacyclogenesis, oxidative stress sensitivity of ptr1- mutants; glycosome
  and cytokinesis defects in T. brucei RNAi) are consequences of H4B depletion, not processes PTR1
  executes; no process terms proposed for these.
  [PMID:20545846 "Loss of PTR1 was associated with gross morphological changes due to a defect in cytokinesis"]

## Localization

- T. brucei PTR1 (ortholog, ISO donor Tb927.8.2210) fractionates with cytosol:
  [PMID:20545846 "PTR1 was recovered exclusively in the cytosolic fraction along with the cytosolic enzyme marker"]
- L. donovani PTR1-GFP is cytoplasmic:
  [PMID:17275814 "Fluorescence microscopy revealed cytoplasmic localization of GFP tagged protein extending to the flagellum in these stationary phase promastigotes"]
- No evidence for glycosomal localization (no PTS1; despite a database-level glycosome mention in
  LeishmaniaDB, which lacked protein-level evidence). Cytosol ISO accepted.
- L. donovani PTR1 is degraded in stationary phase, proposed proteasome-mediated (PMID:17275814),
  linking lower H4B with metacyclogenesis.

## Annotation decisions summary

| term | evidence | action |
|---|---|---|
| GO:0047040 pteridine reductase activity | IDA, IEA, ISO | ACCEPT (core) |
| GO:0004155 6,7-dihydropteridine reductase activity | IDA | KEEP_AS_NON_CORE |
| GO:0006729 tetrahydrobiopterin biosynthetic process | IEA | ACCEPT |
| GO:0005829 cytosol | ISO | ACCEPT |
| GO:0016491 oxidoreductase activity | IBA, ISM | MODIFY -> GO:0047040, GO:0004146 |
| GO:0004146 dihydrofolate reductase activity | - | NEW |

## Protist-specific checks

- No animal/plant-only terms transferred. No organelle mismatches (cytosol is consistent with
  data). Not part of trypanothione or RNA editing pathways. No host-process terms. SDR family
  is huge; IBA/ISM rows only assert generic oxidoreductase, so no paralog over-annotation, just
  under-specificity.
