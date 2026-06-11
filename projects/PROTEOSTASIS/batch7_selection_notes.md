# Proteostasis Review Batch 7 — Gene Selection

Date: 2026-06-11
Branch: `claude/gallant-hypatia-3rlpyb`

## Context

Batches 1–6 are complete (`pr-1217`, `2026-06-03`, `2026-06-06`,
`2026-06-07`, `2026-06-07b`, `2026-06-07c`). Batch 6 covered the Translation
branch's co-translational quality-control machinery (RQC, UFMylation, NMD,
N-terminal acetylation). Batch 7 moves squarely into the **ER proteostasis
branch**, selecting 50 unreviewed PN candidates (`ok_for_propagation_to_go`
scope, no prior `*-ai-review.yaml`).

## Theme: ER protein biogenesis, folding, and ER-associated degradation (ERAD)

This batch walks the full ER-proteostasis lifecycle of a secretory/membrane
protein, from co-translational targeting and insertion, through glycoprotein
folding quality control, to ERAD-mediated disposal of terminally misfolded
clients. It complements the `er_proteostasis` mapping set and the batch-5
cytosolic/ER chaperone work, and feeds the `ER_PHAGY` and
`UNFOLDED_PROTEIN_BINDING` related projects.

### Selected genes (50)

#### ER membrane protein insertion — EMC insertase (10)
1. `EMC1` — EMC large lumenal/scaffold subunit
2. `EMC2` — EMC cytosolic TPR subunit
3. `EMC3` — EMC core insertase subunit (Oxa1 superfamily)
4. `EMC4` — EMC membrane subunit
5. `MMGT1` (EMC5) — EMC membrane subunit
6. `EMC6` — EMC membrane subunit
7. `EMC7` — EMC lumenal/membrane subunit
8. `EMC8` — EMC cytosolic subunit
9. `EMC9` — EMC cytosolic subunit (EMC8 paralog)
10. `EMC10` — EMC lumenal subunit

#### Tail-anchored protein insertion — GET/TRC pathway (3)
11. `GET1` (WRB) — ER membrane GET insertase receptor
12. `GET3` (ASNA1/TRC40) — cytosolic TA-targeting ATPase
13. `GET4` (TRC35) — pre-targeting complex / GET3 loading

#### SRP-dependent co-translational targeting (5)
14. `SRP9` — Alu domain (elongation arrest)
15. `SRP19` — S domain assembly
16. `SRP68` — S domain
17. `SRP72` — S domain
18. `SRPRB` — SRP receptor beta subunit

#### Translocon-associated & signal-peptide processing (8)
19. `SEC62` — post-translational translocation / SEC62-SEC63
20. `SEC63` — translocon-associated, BiP recruitment (J-domain)
21. `SEC11A` — signal peptidase catalytic subunit
22. `SEC11C` — signal peptidase catalytic subunit
23. `SPCS1` — signal peptidase complex subunit
24. `SPCS2` — signal peptidase complex subunit
25. `SPCS3` — signal peptidase complex subunit
26. `SERP1` (RAMP4) — translocon-associated stress protein

#### Glycoprotein folding QC — ERAD mannosidases & lectins (8)
27. `EDEM1` — ERAD mannosidase-like (misfold recognition)
28. `EDEM2` — ERAD mannosidase-like (initiates mannose trimming)
29. `EDEM3` — ERAD mannosidase-like (α1,2-mannosidase)
30. `MAN1B1` — ER α-mannosidase I (ERAD timer)
31. `LMAN1` (ERGIC-53) — ER-Golgi cargo lectin (MCFD2 partner)
32. `LMAN2` (VIP36) — ER-Golgi cargo lectin
33. `LMAN1L` — LMAN1 paralog (testis)
34. `LMAN2L` (VIPL) — VIP36-like lectin

#### ER oxidative folding & prolyl hydroxylation (8)
35. `P3H1` — prolyl 3-hydroxylase 1 (collagen; ER complex with CRTAP/PPIB)
36. `P3H2` — prolyl 3-hydroxylase 2
37. `P4HA1` — prolyl 4-hydroxylase alpha-1 (collagen)
38. `P4HA2` — prolyl 4-hydroxylase alpha-2
39. `P4HA3` — prolyl 4-hydroxylase alpha-3
40. `TXNDC11` — ER thioredoxin-domain protein
41. `TXNDC12` — ER thioredoxin-domain protein (ERp18/ERp19)
42. `TXNDC16` — ER thioredoxin-domain protein (ERp90)

#### ERAD ubiquitin machinery & membrane cofactors (8)
43. `RNF5` (RMA1) — ER membrane RING E3 ligase
44. `RNF185` — ER membrane RING E3 ligase (MARCH6-like branch)
45. `RNF170` — ER membrane RING E3 ligase (IP3R ERAD)
46. `FAF2` (UBXD8) — p97/VCP UBX cofactor, ERAD/lipid droplet
47. `UBAC2` — ERAD membrane component (RHBDD1/UBAC2)
48. `ERLIN1` — ER lipid-raft SPFH/prohibitin, IP3R ERAD
49. `ERLIN2` — ER lipid-raft SPFH/prohibitin, IP3R ERAD
50. `SERP2` — SERP1 paralog, translocon-associated stress protein

## Method

Same as batches 5–6: `fetch-gene` scaffolding (uniprot + goa + seeded
`-ai-review.yaml` + cached publications), per-annotation review against GO
guidelines with verbatim `supported_by`, populated
`description`/`core_functions`/`suggested_questions`/`suggested_experiments`,
reference `reference_review` adjudication, then `uv run ai-gene-review validate`.

## Curation watch-points

- **Avoid bare `protein binding` (GO:0005515)** as core. EMC/SPC/SRP/GET
  subunits should use complex `part_of` terms plus the complex's molecular
  function where the subunit contributes (e.g. EMC membrane insertase activity
  `GO:0032977`, signal peptidase `GO:0008233`/`GO:0004252`).
- **Catalytic vs structural subunits.** Of the signal peptidase complex only
  SEC11A/SEC11C are catalytic (serine endopeptidase); SPCS1/2/3 are accessory —
  do not assign peptidase catalytic activity to the SPCS subunits. Of the SRP,
  only the RNA-binding/receptor roles apply per subunit. EMC catalytic insertase
  activity is centered on EMC3 (Oxa1/YidC-like) with EMC6; cytosolic subunits
  (EMC2/8/9) are scaffolds.
- **Mannosidase activity vs lectin recognition.** EDEM1/2/3 and MAN1B1 act as
  mannose-trimming / misfold-recognition factors (EDEM1 may be lectin-like
  rather than catalytic; EDEM2 has demonstrated mannosidase activity). LMAN1/2
  and paralogs are cargo **lectins**, not hydrolases — use carbohydrate/mannose
  binding + ER-Golgi transport, not glycosidase activity.
- **Prolyl hydroxylases.** P3H1/P3H2 are 3-hydroxylases; P4HA1/2/3 are the
  catalytic alpha subunits of the α2β2 prolyl 4-hydroxylase (β = P4HB/PDI).
  Capture 2-oxoglutarate/Fe(II)-dependent dioxygenase MF and collagen biogenesis
  BP; keep generic "protein binding" non-core.
- **ERAD E3 specificity.** RNF5/RNF185/RNF170 are membrane RING E3s; use
  `ubiquitin protein ligase activity` + ERAD pathway, not bare ubiquitination.
  RNF170 and ERLIN1/ERLIN2 share the IP3R ERAD complex — capture that without
  over-broadening.
- **Paralog caution (PN domain-based inclusions).** `LMAN1L`, `LMAN2L`,
  `DCAF`-style testis/low-evidence paralogs, `EMC9` (EMC8 paralog), `SERP2`,
  and `SEC11A` vs `SEC11C` tissue paralogs may rest largely on family
  membership/IBA — distinguish defensible core function from family propagation,
  and use `KEEP_AS_NON_CORE`/`UNDECIDED` where direct evidence is thin.
