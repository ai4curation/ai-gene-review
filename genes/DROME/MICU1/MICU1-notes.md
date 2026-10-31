# MICU1 (CG4495) review notes

UniProt A2VEI2 (Calcium uptake protein 1 homolog, mitochondrial); PANTHER PTHR12294:SF1.

## Literature journal

- Gatekeeper [PMID:31042479 "These observations are consistent with MICU1 providing the main gatekeeper function for the uniporter."]
- Lethality independent of MCU [PMID:31042479 "More surprisingly, we find that loss of MCU or EMRE does not suppress MICU1 mutant lethality, suggesting that the lethality results from MCU-independent functions."]
- Knockdown lowers evoked uptake in mushroom body neurons [PMID:27568554 "Upon KCl stimulation, flies with MICU1 silenced in the MBn showed a mitochondrial calcium increase that was 70%±6% of the control"]; memory [PMID:27568554 "The memory decay curve of MICU1-silenced flies revealed an ITM defect"].
- IMS localization in fly muscle [PMID:39680501 "Notably, SLMO-HA and MICU1-sp1-10 were detected only when using Triton, but not 5 μg/ml digitonin, which is insufficient to penetrate the mitochondrial membrane"].

## Curation decisions

- Calcium channel regulator activity ACCEPTED as core MF (bidirectional gating, so not refined to inhibitor).
- Uniporter module conventions as in MCU-notes.md.

## Deep research

`MICU1-deep-research-falcon.md` (falcon) arrived after the review was first committed. It agrees with the review: MICU1 is an EF-hand calcium-sensing regulatory subunit acting on the intermembrane-space side of the inner membrane. Fly data support functional restraint of MCU-EMRE activity (eye assay), but mouse mitoplast patch-clamp data indicate MICUs raise open probability at high calcium rather than plugging the pore at low calcium. This supports keeping the bidirectional calcium channel regulator activity rather than refining it to inhibitor activity. No annotation decision changed.
