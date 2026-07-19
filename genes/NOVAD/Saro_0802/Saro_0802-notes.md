# NOV1 (Saro_0802, Q2GA76_NOVAD) — review notes

## Identity and function

Saro_0802 = **NOV1**, a **resveratrol-cleaving dioxygenase / stilbene cleavage oxygenase (SCO)** of
*Novosphingobium aromaticivorans* (DSM 12444). It is a bacterial member of the same enzyme class as
Neurospora CAO-1 and the *Sphingomonas* lignostilbene α,β-dioxygenases (LSDs); the CCO/RPE65 superfamily
(PANTHER PTHR10543). EC 1.13.11.-; non-heme Fe(II).

- **Reaction:** cleaves the central (interphenyl) Cα–Cβ double bond of stilbenes → two aromatic
  aldehydes. Structurally characterized with resveratrol (substrate) and vanillin (product).
  [PMID:27911781 "Stilbene cleavage oxygenases (SCOs) cleave the central double"]
- **Fold/cofactor:** [PMID:27911781 "an iron cofactor coordinated by four histidines"]; seven-bladed
  β-propeller. Dioxygen binds side-on to the iron.
- **Mechanism (why the 4′-OH matters):** the reaction proceeds by a ferric-superoxide reacting with
  substrate [PMID:27911781 "activated by deprotonation of a phenol group at position 4 of the substrate"].
  So the 4′-OH is **catalytically essential** (the deprotonation/activation site), not merely a binding
  determinant. Correspondingly [PMID:27911781 "NOV1 cleaves a wide range of other stilbene-like compounds with a 4'-OH group"].
- **Biotech:** NOV1 has been engineered to convert lignin-derived **isoeugenol to vanillin**
  (PMID:35687874) — a lignin-valorization application.

## The annotation problem: carotenoid over-annotation, via TreeGrafter (IEA)

All three GOA annotations for NOV1 are **IEA**:
- GO:0010436 carotenoid dioxygenase activity — GO_REF:0000118 (**TreeGrafter**)
- GO:0016121 carotene catabolic process — GO_REF:0000118 (TreeGrafter)
- GO:0016702 oxidoreductase (dioxygenase) — GO_REF:0000002 (InterPro2GO)

This is the **same substrate-class over-annotation as cao-1** (carotenoid terms on a stilbene cleaver),
but propagated by **TreeGrafter** (automated phylogenetic grafting onto the PANTHER tree) rather than
manual PAINT/IBA — so the fungal IBA case and this bacterial IEA case are two propagation mechanisms
making the identical error, because the CCO family mixes carotenoid- and stilbene-cleaving members. NOV1
is a stilbene cleavage oxygenase, not a carotenoid enzyme.

## Review decisions

| GO term | Evidence | Decision | Rationale |
|---|---|---|---|
| GO:0010436 carotenoid dioxygenase activity | IEA (TreeGrafter) | **REMOVE** | NOV1 cleaves stilbenes (resveratrol, isoeugenol), not carotenoids; TreeGrafter over-propagation. Correct specific term is GO:7770086 resveratrol dioxygenase activity. |
| GO:0016121 carotene catabolic process | IEA (TreeGrafter) | **MODIFY → GO:0046272 stilbene catabolic process** | Wrong substrate class; NOV1 acts in stilbene/lignin-derived compound catabolism. |
| GO:0016702 oxidoreductase (2 O atoms) | IEA (InterPro2GO) | **ACCEPT** | Correct general dioxygenase MF. |

Core function: resveratrol/stilbene cleavage dioxygenase (best specific term GO:7770086; parent
GO:0016702), non-heme four-His Fe(II), in stilbene catabolic process. Flag the TreeGrafter rule
(GO_REF:0000118) that assigns carotenoid activity to the SCO clade for correction (cf. the TreeGrafter
and IBA_REVIEW projects).

## Cross-family point (vs cao-1)

NOV1 shows the 4′-OH requirement is **mechanistic** (phenol deprotonation activates catalysis) and is
comparatively **permissive** (cleaves a wide range of 4′-OH stilbenes). CAO-1 is more restrictive,
requiring additional free hydroxyls for its two-ring binding anchors (see
`genes/NEUCR/cao-1/cao-1-bioinformatics/RESULTS.md`). Shared catalytic logic (4′-OH activation),
different binding-pocket stringency.
