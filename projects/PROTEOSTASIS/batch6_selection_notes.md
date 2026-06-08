# Proteostasis Review Batch 6 — Gene Selection

Date: 2026-06-07
Branch: `claude/proteostasis-50-genes-xFOZK`

## Context

Batches 1–5 are complete (`pr-1217`, `2026-06-03`, `2026-06-06`, `2026-06-07`,
`2026-06-07b`). Batch 5 covered the cytosolic/ER chaperone & co-chaperone
folding machinery. Batch 6 moves to the **Translation branch**, selecting 50
unreviewed PN candidates (`ok_for_propagation_to_go` scope, no prior
`*-ai-review.yaml`).

## Theme: co-translational quality control & translation surveillance

This is the most proteostasis-central slice of the Translation branch — the
machinery that monitors translation, rescues stalled/collided ribosomes,
degrades aberrant nascent chains, surveils faulty mRNAs, and co-translationally
modifies emerging nascent chains. It complements the related
`RIBOSOME_QUALITY_CONTROL` and `INTEGRATED_STRESS_RESPONSE` projects.

### Deferred mega/pleiotropic genes

`HUWE1` (giant ~4374-aa E3 with hundreds of substrates) and `OGT`
(O-GlcNAc transferase, pervasively pleiotropic) were considered but deferred to
dedicated reviews rather than diluting this batch.

## Selected genes (50)

### Ribosome-associated quality control (RQC) & ribosome rescue — 26
1. `LTN1` (Listerin) — RQC E3 ubiquitin ligase that ubiquitinates 60S-stalled nascent chains
2. `NEMF` — RQC complex; CAT-tailing of stalled nascent chains, recruits LTN1
3. `TCF25` — RQC complex subunit (RQC2-associated)
4. `RACK1` — 40S ribosomal scaffold; collision sensing / ribosome QC hub
5. `ZNF598` — E3 that ubiquitinates 40S (eS10/uS10) on ribosome collision (initiates RQC)
6. `PELO` (Dom34) — ribosome rescue / no-go & non-stop decay (with HBS1L)
7. `HBS1L` — GTPase partner of PELO in ribosome rescue
8. `GTPBP1` — translational GTPase, ribosome-associated mRNA surveillance
9. `GTPBP2` — translational GTPase, ribosome rescue (with PELO)
10. `MKRN1` — RING E3, poly(A)/polylysine-stall ribosome QC
11. `MKRN2` — makorin RING E3 paralog
12. `RNF14` — RING E3 in ribosome-collision/RQC signaling
13. `RNF25` — RING E3 in ribosome-associated quality control
14. `GIGYF1` — 4EHP/EIF4E2 partner; translational repression on ribosome stalling
15. `GIGYF2` — 4EHP/EIF4E2 partner; co-translational repression
16. `EIF4E2` (4EHP) — cap-binding translational repressor in RQC/surveillance
17. `EIF3J` — loosely associated eIF3 subunit; ribosome recycling/QC
18. `EIF5A` — hypusine-containing elongation/termination factor; polyproline & stall resolution
19. `DRG2` — developmentally regulated GTP-binding protein, translation-associated
20. `NPLOC4` (NPL4) — p97/VCP cofactor; extracts ubiquitinated RQC substrates
21. `UFD1` (UFD1L) — p97/VCP cofactor (with NPLOC4) for substrate unfolding/extraction
22. `OTUD3` — deubiquitinase, ribosome-associated QC
23. `USP21` — deubiquitinase, ribosome/RQC-associated
24. `TRIP4` (ASC-1) — ASC-1 complex; ribosome-collision quality control
25. `MAP3K20` (ZAKα) — ribotoxic stress response kinase; senses ribosome collisions
26. `GCN1` — ribosome-collision sensor that activates GCN2/integrated stress response

### UFMylation pathway (ER-ribosome co-translational QC) — 7
27. `UFM1` — ubiquitin-fold modifier 1
28. `UFC1` — UFM1-conjugating enzyme (E2)
29. `UFL1` — UFM1 E3 ligase (ribosome/ER UFMylation)
30. `UFSP1` — UFM1-specific protease
31. `UFSP2` — UFM1-specific protease
32. `UBA5` — UFM1-activating enzyme (E1)
33. `DDRGK1` (UFBP1) — UFL1 cofactor / UFM1 substrate adaptor at the ER

### Nonsense-mediated mRNA decay (translation-coupled surveillance) — 4
34. `UPF1` — central NMD RNA helicase/ATPase
35. `UPF2` — NMD core factor (UPF1–UPF3 bridge)
36. `UPF3A` — NMD core factor (EJC-associated)
37. `UPF3B` — NMD core factor (EJC-associated)

### Nascent-chain N-terminal acetylation & husbandry — 8
38. `HYPK` — NatA-associated chaperone / huntingtin-interacting nascent-chain factor
39. `NAA10` — NatA catalytic N-terminal acetyltransferase (Ogden syndrome)
40. `NAA15` — NatA auxiliary subunit
41. `NAA25` — NatB auxiliary subunit
42. `NAA30` — NatC catalytic subunit
43. `NAA35` — NatC auxiliary subunit
44. `NAA38` — NatC/NatB-associated subunit (LSML)
45. `NAA40` — NatD, N-terminal acetyltransferase for histones H2A/H4

### Ribosome recycling, reinitiation & elongation control — 5
46. `DENR` — density-regulated; ribosome recycling / reinitiation (with MCTS1)
47. `MCTS1` — MCTS1–DENR reinitiation complex
48. `EIF2D` — non-canonical initiation/recycling factor (Ligatin)
49. `GTPBP6` — ribosome recycling-associated GTPase
50. `EEF2K` — eEF2 kinase; elongation control coupling stress to translation

## Method

Same as batch 5: `fetch-gene --no-fetch-titles` scaffolding (with timeout
retries), per-annotation review against GO guidelines with verbatim
`supported_by`, populated `description`/`core_functions`/questions/experiments,
`uv run ai-gene-review validate`, then PN-mapping feedback.

## Curation watch-points

- **Avoid `protein binding` (GO:0005515)** as core; for E3s use
  `ubiquitin protein ligase activity`, for the rescue GTPases use translational
  GTPase / ribosome-binding terms, for Nat subunits use
  `N-terminal (peptidyl-)amino-acid acetyltransferase activity`.
- **Catalytic vs auxiliary subunits:** NatA/B/C auxiliary subunits (NAA15, NAA25,
  NAA35, NAA38) and HYPK are non-catalytic — do not assign acetyltransferase
  catalytic activity; use complex/adaptor/auxiliary terms.
- **RQC vs generic translation:** keep broad `translation` (GO:0006412) terms
  non-core where the gene's specific role is collided-ribosome surveillance /
  rescue / RQC (cf. the EDF1 precedent).
- **UFMylation enzyme roles:** assign the correct E1/E2/E3/protease step; UFM1 is
  the modifier, not an enzyme.
- **Moonlighting:** RACK1, EIF5A, NAA10 have well-documented non-RQC moonlighting
  roles — capture the core translation/QC function, mark over-annotations.
