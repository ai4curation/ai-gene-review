# pomt2 notes

## 2026-05-09 review notes

Reviewed GOA, UniProt F1Q8R9, PMID:20466645, PMID:36499139, and PANTHER family cache. The core annotation is the ER protein O-mannosyltransferase role; photoreceptor maintenance is retained as a non-core downstream phenotype/process consequence of O-mannosyl glycan loss.

## Re-review 2026-09-29

Re-reviewed all 12 GOA rows against the two cached primary papers and UniProt F1Q8R9 (the yaml
review blocks had been rewritten in an earlier interrupted pass; this pass verified them,
confirmed zero validation errors, and completed the notes/history records).

- Core activity GO:0004169 (IBA, IEA/EC, IGI): ACCEPT. The zebrafish enzyme was reconstituted
  directly [PMID:20466645 "only when both zPOMT1 and zPOMT2 were expressed in human embryonic
  kidney 293T cells were high levels of protein O-mannosyltransferase activity detected"], and
  UniProt derives EC 2.4.1.109 from that paper. The zebrafish gene appearing in its own IBA
  WITH/FROM is expected (its IGI seeded the PAINT node), not circular.
- Core process GO:0035269 (IBA, IGI): ACCEPT; participation is direct (Pomt2 catalyses the
  initiating mannose transfer) [PMID:20466645 "the IIH6 reactivity was lost in both zPOMT1 and
  zPOMT2 morphants"; PMID:36499139 "pomt2 mutation resulted in a loss of matriglycan"].
- Generic parents GO:0000030 mannosyltransferase activity, GO:0006493 protein O-linked
  glycosylation and GO:0016020 membrane (InterPro/ARBA IEA): MODIFY to the specific child
  terms already carried (GO:0004169, GO:0035269, GO:0005789).
- Localization GO:0005783 (IBA) / GO:0005789 (ISS, IEA SubCell): ACCEPT, supported by the
  SUBCELLULAR LOCATION line and the 11-TM topology, not by the FUNCTION line.
- GO:0045494 photoreceptor cell maintenance (IMP, PMID:36499139, full text cached):
  KEEP_AS_NON_CORE. The protective effect is executed downstream by matriglycan-dependent EYS
  anchoring [PMID:36499139 "Loss of EYS in the connecting cilium region in pomt2 mutant zebrafish
  may ultimately cause photoreceptor degeneration."]; Pomt2 itself does no work in photoreceptor
  maintenance. GOA already uses acts_upstream_of_or_within.
- PMID:20466645 is abstract-only in the cache; all quotes are from the abstract.
- Validation: zero errors; one residual warning (no deep-research citation), left as is because
  primary literature covers every claim.

### Follow-up after PR review (2026-10-09)

- Decided to keep `core_functions[0].molecular_function: GO:0004169` (not `contributes_to_molecular_function`). Distinction from dph2 stated in the core description and the IGI row reason: Pomt2 is itself a GT39-fold catalytic subunit (both subunits of the obligate Pomt1-Pomt2 heteromer carry the glycosyltransferase fold), whereas dph2 is a non-catalytic electron-donor subunit. GOA qualifier on all three zebrafish GO:0004169 rows is `enables`, and QuickGO shows human POMT2 (Q9UKY4) also annotated `enables` GO:0004169 (IBA GO_REF:0000033 and IEA GO_REF:0000003), so curators do not use contributes_to for this subunit.
- Added `in_complex: GO:0031502 dolichyl-phosphate-mannose-protein mannosyltransferase complex` (verified in QuickGO; human POMT1/POMT2 are `part_of` it by IPI on PMID:16698797). Validation: zero errors; a new warning notes GO:0031502 is not in existing_annotations (no NEW row added, per the batch instruction to report rather than add), plus the pre-existing deep-research warning.
