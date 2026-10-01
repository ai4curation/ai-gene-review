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
