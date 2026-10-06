# nudF (Aspergillus nidulans, Q00664) review notes

## 2026-09-27 initial review (claude-code)

Context: comparative member of `modules/nucleokinesis.yaml` (LIS1 unit). Human ortholog PAFAH1B1 reviewed under `genes/human/PAFAH1B1/`.

Key evidence
- Cloned as a nuclear-migration (nud) gene; ~42% identical to human LIS1 [PMID:7612965 "we cloned a gene, nudF, which is required for nuclear migration during vegetative growth as well as development"].
- Dynein pathway: dynein heavy-chain (nudA/snfC) alleles bypass nudF6 [PMID:9236777 "our data suggests that NUDF affects nuclear migration by acting on the dynein motor system"].
- NudE is a multicopy suppressor of nudF7 and binds NudF via its coiled coil [PMID:10931877 "NUDF protein interacts with the Aspergillus NUDE coiled-coil in a yeast two-hybrid system"].
- Plus-end comets; recruited by ClipA and NudE [PMID:12686603; PMID:16467375 "we suggest that CLIPA and NUDE both recruit NUDF to the microtubule plus end"].
- SPB localization independent of MTs/dynein; needed for dynein SPB targeting [PMID:15930134 "the spindle pole localization of dynein is positively regulated by NUDF"]; complex with NudC and BnfA at SPBs [PMID:18390647].
- Early endosome/peroxisome transport initiation [PMID:22711696 "In the absence of Lis1, endosomes and peroxisomes accumulate at hyphal tips, and retrograde movements are quite rare"].
- Mechanism: relieves dynein phi autoinhibition; required for HookA-mediated activation [PMID:31562232 "promotes the switch of dynein from the autoinhibited state to an open state to facilitate dynein activation"].
- Functions as a dimer via N-terminal coiled coil [PMID:11134054].
- NOTE: PMID:11509576 (Hoffmann et al. 2001, NudF/NudE direct binding to dynein subunits and tubulins) is RETRACTED (PMID:14712821); not used.

Decisions
- Core MF: GO:0140659 cytoskeletal motor regulator activity (NEW, matches module/human) + GO:0070840 dynein complex binding (IEA accepted).
- Core BP: nuclear migration (IMP accepted; GO:0030473 used in core), NEW GO:0072382 for EE transport initiation.
- Spindle orientation (IEA) and MT sliding (IEA) kept non-core: family-level inference, not assayed in A. nidulans.
- Conidiation / sexual sporulation IMP kept non-core (downstream of nuclear distribution).
- Protein binding (NudE) removed as uninformative.
- Microtubule binding IDA (abstract-only paper, localization data) kept non-core, deferring to curator.

Deep research: no falcon report present at time of review.

## 2026-09-27 falcon deep research incorporated (claude-code)

- Read nudF-deep-research-falcon.md. Its core model (noncatalytic LIS1-family dynein regulator acting at transport initiation; plus-end comets and SPBs; NudE/NudC/BnfA partners) agrees with the review; no action changed.
- New primary paper found via the report and verified at PubMed: PMID:34428469 (Qiu et al. 2021 Curr Biol, AAA3 nucleotide state). Cached; supports NudF bypass by the wB-AAA3 dynein mutation ["Importantly, the wB-AAA3 mutation suppressed the colony growth defect of the ΔnudF mutant"]. Added to the NEW GO:0140659 row and core function 1.
- Added PMID:22711696 quote that Lis1 is absent from moving cargo to the GO:0072382 row; deep-research quote added to core function 1.
- Not used: 2024 mammalian/yeast structural and force papers (Singh 2024, Kusakci 2024) - cross-species context only.

## 2026-10-01 re-review (GOA refresh)

- No new (PENDING) or vanished GOA rows after the refresh. Existing judgments re-audited against current guidelines (IBA reasoning, NEW participation/comparator tests, protein-binding handling, verbatim supporting text); no changes needed.
