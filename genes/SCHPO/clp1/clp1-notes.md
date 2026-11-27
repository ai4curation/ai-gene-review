# clp1 (flp1; SPAC1782.09c; UniProt Q9P7H1) — curation notes

Session: 2026-09-26. Fission yeast Cdc14-family phosphatase. Inputs: `clp1-uniprot.txt`,
`clp1-goa.tsv` (75 rows), `clp1-deep-research-falcon.md` (Edison), cached publications.
Comparator: `genes/yeast/CDC14/CDC14-ai-review.yaml` (complete S. cerevisiae review).

## Full-text availability

Abstract-only caches (curators read the full text; I did not): PMID:11448769, 15128870,
15265986, 15525536, 16085489, 16823372, 16950131, 18418059, 33176152, 37128864. Europe PMC
has no OA full text for any of these. Full text cached for the other 15 papers.

## Holistic picture

- Founding paper: Clp1 is the S. pombe Cdc14 homolog, "not required for mitotic exit but rather
  functions together with the SIN in coordinating cytokinesis with the nuclear-division cycle"
  [PMID:11448769 "We have identified the S. pombe Cdc14p homolog, Clp1p, and show that it is not
  required for mitotic exit but rather functions together with the SIN in coordinating cytokinesis
  with the nuclear-division cycle."]. It leaves the nucleolus at mitotic entry (earlier than Cdc14)
  and goes to the spindle and division site; the SIN keeps it out of the nucleolus until cytokinesis
  is done [PMID:11448769 "the SIN is required for keeping Clp1p out of the nucleolus until
  completion of cytokinesis"]. clp1Δ enters mitosis early; overexpression delays G2/M
  [PMID:11448769 "cells deleted for clp1 enter mitosis precociously and cells overexpressing Clp1p
  delay mitotic entry"].
- Substrate specificity: Ser/Thr-Pro (Cdk1) sites. "belongs to a conserved family of
  serine-threonine-phosphatases" [PMID:15128870]; "proline-directed Cdc14-like phosphatase Clp1"
  [PMID:21965289]. Substrate-trap proteomics: >70 C286S-enriched candidates, Cdk1 sites in 44/73
  [PMID:23297348 "we and others detected Cdk1 phosphorylation sites in over half (44/73) of these
  potential substrates"]. No phosphotyrosine substrate is known (deep research agrees). Clp1 affects
  Cdc2 Tyr15 only indirectly, via Cdc25.
- Mitotic exit / G2-M: Cdc25 is an in vitro substrate and Flp1 is needed for its rapid degradation
  at the end of mitosis [PMID:15128870 "Cdc25p is a substrate of Flp1p in vitro"; PMID:18418059
  "Flp1p is required for the rapid degradation of Cdc25p"]. Cdk1 phosphorylates and inhibits Clp1
  before anaphase; Clp1 autodephosphorylates as Cdk1 falls [PMID:16950131 "Clp1/Flp1
  autocatalytically reverses these phosphorylation events to stimulate its own activity"]. Pxl1 is
  dephosphorylated by Clp1 and Dis2 at mitotic exit [PMID:34133210].
- Spindle: dephosphorylates Klp9 and Ase1 at anaphase B onset so they bind at the midzone; clp1off
  halves elongation velocity [PMID:19686686 "mutants clp1off and ase1S>D-klp9S>D cells showed
  significantly decreased spindle velocities (0.35 ± 0.05 n=9 and 0.48 ± 0.08 n=12 μm/min"]. Also
  Dis1 [PMID:34080538 "Upon clp1 deletion, Dis1-EGFP was only detected at spindle poles"]. Clp1
  concentrates at the midzone in anaphase B [PMID:19686686 "clp1p appeared to concentrate at the
  spindle midzone during anaphase B"]. Meadows 2017: Klp9 C-terminus dephosphorylation by Clp1 is
  needed for Klp9-CPC interaction at the midzone; no change in pole-separation rate but more
  anaphase B spindle collapse in clp1Δ/C286S [PMID:28178520].
- Kinetochores: Clp1 at kinetochores in prometaphase; clp1Δ cosegregates sisters when
  mono-orientation-prone; works with Aurora/Ark1 [PMID:15525536]. Nsk1 substrate: dephosphorylation
  needed for kinetochore-SPB junction localization [PMID:21965289; PMID:22065639 "purified MBP-Clp1
  but not catalytically inactive MBP-Clp1-C286S dephosphorylated Nsk1"]. Mde4 (monopolin) substrate
  [PMID:19523829 "Clp1 can dephosphorylate Mde4 in vitro"].
- IMPORTANT opposite sign: Choi & McCollum 2012 — clp1Δ *reduces* lagging chromosomes in mde4Δ and
  swi6Δ; Clp1-NLS increases them: "Clp1 antagonizes correction of merotelic attachments"
  [PMID:22264609], mechanism = Klp9-dependent metaphase spindle length / tension.
- Cytokinesis: Mid1 tethers Clp1 at the contractile ring (Mid1 aa 331-534 binds Clp1 catalytic
  domain; 0/102 mid1Δ rings have Clp1); Clp1 dephosphorylates Cdc15 [PMID:18378776]. Cdc12 formin
  Cdk1 sites dephosphorylated by Clp1, allowing maximal Cdc12 at the ring [PMID:29343550]. FPALM:
  Clp1 at 136 nm, intermediate stratum [PMID:28914606]. Cdc11 (SIN scaffold) Cdk1 sites are
  Clp1 substrates [PMID:23297348].
- Cytokinesis checkpoint: Clp1-dependent G2 delay and ring maintenance under mild cytokinetic
  perturbation; ectopic SIN activation bypasses the need for Clp1 [PMID:15265986]. Sid2 (SIN)
  phosphorylates Clp1 RxxS sites → 14-3-3 Rad24 binding → cytoplasmic retention [PMID:16085489;
  PMID:18951025 "Mutation of the Sid2 phosphorylation sites on Clp1 disrupts the Clp1-Rad24
  interaction and causes Clp1 to return prematurely to the nucleolus during cytokinesis"]. clp1-6A
  keeps the checkpoint but fails to complete cytokinesis under ring stress.
- Nuclear import via Sal3 (importin-β3); C-terminal basic NLS [PMID:23297348 "Thus, Sal3 is
  required for Clp1 nuclear import."].
- Stress: HU/H2O2 (not heat/osmotic) trigger interphase nucleoplasmic release via Cds1/Chk1, Pmk1
  and Cdk1 phosphorylation [PMID:22918952]. Deep research adds Cañete 2023 (Sci Rep; not in GOA):
  released Clp1 dephosphorylates Pcr1 and limits the oxidative-stress transcriptional response.
- Stress sequestration sites: heat-shock nucleolar rings (NuRs) [PMID:33176152] and stationary
  phase nucleolar inclusions [PMID:37128864] — GO:0140602 rows, abstract-only.

## GO-CAM context

`gocams/index.tsv` has clp1 in three production models: SIN model 66187e4700002284 (Clp1 phosphatase
→ positive regulation of contractile ring assembly at the ring; phospho-Clp1 → cytokinesis checkpoint
at the mitotic SPB), ring-assembly model 67f85f2b00002096 (same MF/BP/CC), and G2/M model
69729a3800001390 (negative regulation of G2/M at the mitotic SPB). Core functions were aligned with
these. Module `modules/metaphase_anaphase_transition_and_mitotic_exit.yaml` uses Clp1 as the
fission-yeast exit-phosphatase variant (annoton `clp1_spom`, GO:0004722).

## Decisions of note

- GO:0004725 protein tyrosine phosphatase activity (IEA, EC 3.1.3.48): MODIFY → GO:0008138
  protein tyrosine/serine/threonine phosphatase activity, mirroring the CDC14 review. No
  phosphotyrosine substrate; all substrates are Cdk1 pS/pT-P sites.
- GO:0005515 protein binding IPIs: Ark1 → MODIFY GO:0019901 protein kinase binding; Rad24 (two rows)
  → MODIFY GO:0071889 14-3-3 protein binding (evidence-backed, mechanistic); Mid1 → REMOVE (scaffold
  relationship already captured by the CR localization row); Mde4 → REMOVE (enzyme–substrate;
  belongs as has_input on the phosphatase activity).
- GO:0140429 IGI PMID:22264609 → MODIFY to GO:0051988 regulation of attachment of spindle
  microtubules to kinetochore. GO:0140429 has secondary ids GO:0098783 (repair of merotelic
  attachment defect) and GO:1990598 (repair of mono-orientation defect), merged 2020; the IGI row
  was presumably made to the former, but the paper shows Clp1 antagonizes merotelic correction, so
  the merged positive-regulation label misstates the direction. No negative-regulation term exists.
  The IMP row from PMID:15525536 (mono-orientation repair) is ACCEPTed. This creates a deliberate
  "inconsistent actions for the same term" validator warning.
- GO:0072479 response to SAC signaling (IMP, PMID:15525536): UNDECIDED — abstract-only; abstract
  supports biorientation, not a SAC-response process.
- GO:0006974 DNA damage response and GO:0033554 cellular response to stress: KEEP_AS_NON_CORE
  (real, kinase-dependent relocalization; downstream role undefined in the cited paper).
- GO:0140602 nucleolar peripheral inclusion body (two IDA rows): KEEP_AS_NON_CORE — sequestration
  under heat stress / stationary phase, not a site of activity.
- GO:1902846 EXP PMID:28178520: ACCEPT with caveat that this paper found no rate change, only more
  spindle collapse; rate effect is in PMID:19686686 and PMID:34080538.
- No NEW annotations proposed; the Pcr1/oxidative-stress function (Cañete 2023) is not in GOA and
  the paper is not cached, so it is noted here and in the GO:0033554 row only.

## Validation

`just validate SCHPO clp1`: valid, 1 warning (deliberate GO:0140429 inconsistency). Rendered with
`just render SCHPO clp1`.
