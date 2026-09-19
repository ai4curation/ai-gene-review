# ARHGAP23 retains the RhoGAP arginine finger — and that is not evidence of activity

Every number below is produced by `analyze_arhgap23.py`; nothing is transcribed. Re-run with `uv run python analyze_arhgap23.py`, and `--self-test` to check the guards.

## 1. The subject, and the provenance of the claim under test

| | |
|---|---|
| accession | Q9P227 (RHG23_HUMAN, 1491 aa) |
| Rho-GAP domain | 905–1097 |
| annotated arginine finger | 942 (residue **R**) |
| evidence on that Site feature | `ECO:0000255` |
| evidence on the FUNCTION comment | `ECO:0000250` |

UniProt's FUNCTION text is: *"GTPase activator for the Rho-type GTPases by converting them to an inactive GDP-bound state"*

Both of those evidence codes are non-experimental — the arginine finger is placed by a PROSITE profile rule and the function is asserted by similarity — so the question this analysis can settle is whether the *sequence* supports the inference, not whether the protein has been shown to work.

## 2. The arginine finger, tested reciprocally

A comparator's own annotated arginine finger is projected onto ARHGAP23 by aligning the two Rho-GAP **domains**, and is scored `retained` only if the aligned residue is an arginine *and* it lands on one of ARHGAP23's own annotated Site features. The projection is then run backwards: ARHGAP23's annotated site must map onto the comparator's annotated finger. Only a test that passes both ways is reported as reciprocal.

| comparator | its finger | → ARHGAP23 | residue | on an ARHGAP23 Site? | reverse lands on comparator finger? | reciprocal |
|---|---|---|---|---|---|---|
| RHG01_HUMAN (Q07960, resolved in 1TX4) | 282R | 942 | **R** | yes | yes | **yes** |
| RHG21_HUMAN (Q5T5U3, closest paralog / IBA donor) | 1184R | 942 | **R** | yes | yes | **yes** |

## 3. What a positive result is worth: the controls

The same test, same code path, on an active RhoGAP and on two proteins that are known to be GAP-dead and that fail in opposite ways.

Each control's status is **verified, not asserted**: the run aborts if the credential below cannot be found in the repo's own GOA table or in the fetched UniProt record.

| subject | verified credential | evidence | residue at its own annotated finger | test verdict |
|---|---|---|---|---|
| RHG21_HUMAN (Q5T5U3) | an active RhoGAP with a direct experimental GTPase-activator annotation | `enables GO:0005096` IDA PMID:15793564 | 1184**R** | retained |
| OCRL_HUMAN (Q01968) | UniProt states, on experimental evidence, that its Rho-GAP domain is inactive | `ECO:0000269` | 757**Q** | NOT retained |
| RHGBB_HUMAN (Q3KRB8) | experimentally GAP-dead: curated NOT annotations for GTPase activator activity | `NOT|enables GO:0005096` IDA PMID:27957544; `NOT|enables GO:0005096` IDA PMID:25721503 | 87**R** | retained |

The OCRL_HUMAN statement in full: *"The ASH (ASPM-SPD2-Hydin) and RhoGAP (Rho GTPase activating) domains form a single folding module. The ASH domain has an immunoglobulin-like fold, the Rho-GAP domain lacks the catalytic arginine and is catalytically inactive. The ASH-RhoGAP module regulates the majority of the protein-protein interactions currently described. The ASH domain mediates association with membrane-targeting Rab GTPases. The Rho-GAP domain interacts with the endocytic adapter APPL1, which is then displaced by PHETA1 and PHETA2 as endosomes mature"*

What UniProt's own GO cross-reference says about GO:0005096 for each of these, which is worth recording because it is not always consistent with the entry's prose: RHG23_HUMAN `TAS:Reactome`; RHG21_HUMAN `TAS:Reactome`; OCRL_HUMAN `IDA:FlyBase`; RHGBB_HUMAN `TAS:Reactome`. The GAP-dead controls both still carry the positive term in the GO record — which is the same class of defect this review is examining, seen from the other side.

So of 2 known GAP-dead controls, the residue test calls 1 of them `retained`. The test can fire — it fires on the control that lost the residue — but a protein can keep the arginine and still have no measurable GAP activity.

The family-wide version of the same number, read from `genes/human/ARHGAP11B/ARHGAP11B-bioinformatics/results.json`: of 66 human reviewed proteins carrying the PROSITE RhoGAP profile, 60 have an arginine at their own annotated finger position and 6 do not, and only 1 of the flagged entries carries an experimentally supported UniProt statement of inactivity. ARHGAP23 is not among the flagged entries.

## 4. The rest of the catalytic surface

One residue is a thin basis for a molecular-function call, so the whole GAP:GTPase interface was computed from PDB 1TX4 (p50RhoGAP:RhoA:GDP:AlF4, a transition-state mimic): every RHG01_HUMAN residue within 4.5 Å of RhoA or of the ALF, GDP, MG ligands. Chain roles are proved rather than assumed (chain A is 99.5% identical to Q07960, chain B is 99.4% identical to RhoA), and the contact set recovers RHG01_HUMAN's own annotated arginine finger (282), as it must.

That gives 25 contact positions, 25 of them inside the Rho-GAP domain. Those are projected onto each subject, accepted only when the projection is in register (the control's finger lands on the subject's own annotated finger):

| subject | role | interface positions | identical | conservative | different | unaligned | identical or conservative |
|---|---|---|---|---|---|---|---|
| RHG23_HUMAN | subject | 25 | 11 | 2 | 12 | 0 | **52.0%** |
| RHG21_HUMAN | positive control — an active, experimentally characterised RhoGAP | 25 | 11 | 2 | 12 | 0 | **52.0%** |
| OCRL_HUMAN | GAP-dead, arginine lost | 25 | 4 | 5 | 15 | 1 | **36.0%** |
| RHGBB_HUMAN | GAP-dead, arginine retained | 25 | 12 | 4 | 8 | 1 | **64.0%** |

**This metric does not order the subjects by activity.** Ranked by percent identical-or-conservative the order is RHGBB_HUMAN (64.0%) > RHG23_HUMAN (52.0%) > RHG21_HUMAN (52.0%) > OCRL_HUMAN (36.0%). Among the three subjects whose catalytic status is known, the experimentally GAP-dead protein that kept its arginine scores **above** the experimentally active one, so the number is tracking relatedness to the structural comparator rather than catalysis. It is reported here as context and is not used as an argument in either direction.

The comparison that does carry information is ARHGAP23 against the positive control. At the 25 interface positions mapped in both, ARHGAP23 and RHG21_HUMAN carry the **same residue at 22** — the exceptions being RHG01_HUMAN 309: RHG23_HUMAN Q vs RHG21_HUMAN R, RHG01_HUMAN 394: RHG23_HUMAN L vs RHG21_HUMAN I, RHG01_HUMAN 410: RHG23_HUMAN D vs RHG21_HUMAN H.

ARHGAP23's non-conservative differences at interface positions (RHG01_HUMAN → ARHGAP23): E278→T938, R283→V943, S284→P944, A285→G945, T287→N947, Q288→A948, N309→Q972, N399→T1063, A406→D1070, A407→N1071, L410→D1074, I413→T1077.

## 5. What this does and does not license

ARHGAP23 **retains** the RhoGAP catalytic arginine: position 942 is an arginine, it is ARHGAP23's own annotated arginine-finger Site, and it is reciprocally in register with RHG01_HUMAN 282, whose role is resolved in a transition-state structure. The same result holds against the closest paralog RHG21_HUMAN. The surrounding catalytic surface is 52.0% identical or conservatively substituted, a number that section 4 shows does not discriminate active from dead in this control set.

The honest reading is asymmetric, and section 3 is the reason. A *lost* arginine would have been a substantive argument against the GAP-activity annotation. A *retained* one is only the absence of that argument: one of the two known GAP-dead controls here passes the same test, and the family-wide census says the same thing at scale. Nothing in this analysis is evidence that ARHGAP23 hydrolyses anything, and no GTPase substrate can be assigned from it — RhoA, RAC1 and CDC42 contacts are not distinguished by this calculation, which uses a single RhoA complex.

What would settle it: an in-vitro GAP assay on the isolated ARHGAP23 Rho-GAP domain against RhoA, RAC1 and CDC42, with the arginine-finger mutant as the negative control.
