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

## 5. The published specificity screen, and the mutant it calls an arginine finger

PMID:32203420 (Müller et al. 2020, *Nature Cell Biology*) ran a cellular FRET biosensor screen across the human RhoGEF/RhoGAP family. Its main text is paywalled and absent from PMC, but the publisher's Source Data and Supplementary Tables are open, and they are parsed directly here. ARHGAP23's row in the Fig. 1b source data:

| GTPase | norm ΔR/R0 AVG | p-value | authors' significance flag | >20% of main activity |
|---|---|---|---|---|
| RhoA | -0.364 | 2.93e-05 | 1 | 1 |
| Rac1 | -0.372 | 2.92e-06 | 1 | 1 |
| Cdc42 | +0.197 | *(none)* | 0 | 0 |

A negative value is a drop in biosensor activity, ie GAP activity toward that GTPase. The screen therefore scores ARHGAP23 as active on RhoA **and** Rac1 to essentially equal degrees and inactive on Cdc42.

Supplementary Table 2 records the same conclusion as explicit calls — RhoA `+`, Rac1 `+`, Cdc42 `-` — and, in the columns that matter for what is *not* known, summarises the prior literature per GTPase:

| literature column | RhoA | Rac1 | Cdc42 |
|---|---|---|---|
| integrated | `+` | *(empty)* | *(empty)* |
| in vitro | *(empty)* | *(empty)* | *(empty)* |
| in vivo | `+` | *(empty)* | *(empty)* |
| reference | `+` | *(empty)* | *(empty)* |

This parse finds the **"integrated" row populated**, the **"in vitro" row empty**, the **"in vivo" row populated**, the **"reference" row populated**. The contrast is the point: an empty in-vitro row means nothing if every row is empty. This is the machine-checkable form of the review's statement that no purified-protein GAP assay exists for ARHGAP23, and it is checked here rather than asserted because it is otherwise the one load-bearing claim in the review that nothing re-runs. Every group in the table above is required to be present, so an absent column aborts the run instead of rendering as an empty one.

The same paper's Supplementary Table 4 records the ARHGAP23 localization experiment as "Focal adhesion localization found by TIRF imaging (GAP-deficient arginine finger mutant), pericentric. Weak actin score in Cytochalasin D assay." — ie the imaged construct was a **R986K** arginine-finger mutant. Supplementary Table 1 gives the screened cDNA as NP_001186346.1, 1491 aa, clone MB134.

That construct is the same length as Q9P227 (1491 aa), so the residue numbers are directly comparable — and they do not agree:

- Position 986 of the canonical sequence is **R**, so the mutant names a real arginine (consistent with the mutant string).
- It is **not** the residue UniProt annotates as the arginine finger, which is 942.
- It aligns to RHG01_HUMAN 323R, which is NOT that protein's annotated arginine finger (282).
- In 1TX4, RHG01_HUMAN 323 is part of the GAP:GTPase interface, and does not contact the nucleotide/AlF4/Mg transition-state ligands — which is the defining property of an arginine finger, and which the annotated finger (282) does.

So the only published "GAP-deficient arginine finger mutant" of ARHGAP23 targets a conserved interface arginine that is not the catalytic finger. That mutant was used for TIRF localization imaging, not to validate the activity screen: the supplementary sentence naming the catalytic controls reads *"mutation of critical arginine residues (‘arginine fingers’) abrogated the activity of the RhoGAPs ARHGAP11A, ARHGAP40, ARHGAP4, FAM13A, and SYDE2 (Extended Data Fig. 2h)."*, and ARHGAP23 is not among them.

**No experiment has yet tested whether ARHGAP23's actual arginine finger (942) is required for its measured RhoA/Rac1 activity.** This is a discrepancy in the literature, not a correction of it: one of the two assignments is wrong and only an experiment can say which.

## 6. What this does and does not license

ARHGAP23 **retains** the RhoGAP catalytic arginine: position 942 is an arginine, it is ARHGAP23's own annotated arginine-finger Site, and it is reciprocally in register with RHG01_HUMAN 282, whose role is resolved in a transition-state structure. The same result holds against the closest paralog RHG21_HUMAN. The surrounding catalytic surface is 52.0% identical or conservatively substituted, a number that section 4 shows does not discriminate active from dead in this control set.

The honest reading is asymmetric, and section 3 is the reason. A *lost* arginine would have been a substantive argument against the GAP-activity annotation. A *retained* one is only the absence of that argument: one of the two known GAP-dead controls here passes the same test, and the family-wide census says the same thing at scale. Nothing in this analysis is by itself evidence that ARHGAP23 hydrolyses anything, and no GTPase substrate can be assigned from it — RhoA, Rac1 and Cdc42 contacts are not distinguished by this calculation, which uses a single RhoA complex. The substrate evidence is the cellular screen in section 5, not the structure.

Put the two together and the position is: the catalytic machinery is intact and indistinguishable from that of an experimentally active close paralog, and a cellular assay reports GAP activity on RhoA and Rac1 — but no purified-protein assay exists, and the one published mutant that would have tied the activity to the catalytic residue mutates a different arginine.

What would settle it: an in-vitro GAP assay on the isolated ARHGAP23 Rho-GAP domain against RhoA, Rac1 and Cdc42, with R942 mutated as the negative control — and, separately, a side-by-side test of R942 against the published 986 position to establish which one the activity depends on.
