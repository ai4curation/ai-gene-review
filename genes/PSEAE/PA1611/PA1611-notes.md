# PA1611 review notes

## Literature search (2026-11-05)

No deep-research provider was available. The PubMed MCP and Europe PMC search
endpoints returned errors during this session (API_ERROR / HTTP 503), so the
search was limited to the local `publications/` cache (grep for "PA1611") and to
fetching PMIDs already known from UniProt and GOA. Papers found: PMID:16182517,
PMID:32939285, PMID:27792789, PMID:19543378 (mention only).

## Findings

- PA1611 is a hybrid sensor that signals through HptB to PA3346 (HsbR)
  [PMID:16182517 "We herein demonstrate that the hybrid sensor PA1611 carries out
  specific signal transduction, through HptB (PA3345), to the response regulator
  PA3346 in Pseudomonas aeruginosa PAO1"].
- The phosphotransfer was a direct biochemical assay: [PMID:32939285 "between the
  cytosolic part of PA1611 (a.a. 202–652) and HptB has been confirmed with"
  [gamma-32P]ATP in Lin et al. 2006 and Hsu et al. 2008].
- Structure of the REC domain (507-651): canonical receiver fold, Asp565 is the
  phosphoacceptor, Mg2+/Ca2+ bound (PDB 7C1J, 7CFW) [PMID:32939285].
- PA1611 is one of three hybrid kinases (with ErcS' and SagS) that feed HptB
  [PMID:27792789 "Several upstream sensors have been proposed for the HptB pathway,
  including PA1611"].

## Domain architecture (UniProt Q9I3B1, InterPro/Pfam, checked 2026-11-05)

TM 12-34 and 167-186 (Phobius) around a periplasmic sCache_4 domain (PF09984);
HAMP 191-243; HisKA (PF00512) with His275; HATPase_c (PF02518); REC (PF00072)
516-632 with Asp565. PA1611 has no Hpt domain (no HPt / IPR008207 match), so it
relies on the separate Hpt protein HptB.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | other seeds | IBD stands without this seed? | verdict | rationale |
|---|---|---|---|---|---|---|---|---|
| PTN001976860 | GO:0000155 phosphorelay sensor kinase activity | 3 | 330 (86 taxa) | GO:0000155, IDA, PMID:16182517 (PseudoCAP) | SenX3 P9WGK5 (IDA PMID:11101667, UniProt); PA3271 Q9HYX0 (IDA PMID:22168309, PseudoCAP) | Yes (SenX3 alone suffices) | SOUND | The paper assayed autophosphorylation and phosphotransfer of the PA1611 cytoplasmic region with [gamma-32P]ATP (as the same lab restates in PMID:32939285), which is direct evidence for histidine kinase activity in a phosphorelay. The node term suits a clade of hybrid sensor kinases. |

Other node terms at PTN001976860 (not seeded by PA1611): GO:0009927
histidine phosphotransfer kinase activity, seeded by RcsD (P39838, has an HPt
domain) and SLN1 (S000001409, no HPt domain). It propagates to Hpt-less hybrid
kinases such as PA1611 and PA3271. I removed the PA1611 IBA and filed one
GO_CENTRAL defect (PROBABLE) asking that the IBD be removed or restricted to the
HPt-containing subclade. PA3271 (Q9HYX0) shares this node and receives the same
IBA; its review should cross-reference this defect rather than file a second one.
