# Cyp2d10 review notes

## Evidence summary
- [UniProtKB:P12939] UniProt describes Cyp2d10 as a heme-thiolate monooxygenase that oxidizes steroids, fatty acids, and xenobiotics.
- [PMID:2107330] The fetched GOA file uses this publication for monooxygenase activity.

## Curation decisions
- Core function: cytochrome P450 2D10 monooxygenase (monooxygenase activity, GO:0004497).
- Specific catalytic activities and direct metabolic processes were accepted.
- Broad parent, localization, binding, and stimulus-response annotations were modified, kept non-core, or marked over-annotated according to support.

## Re-review 2026-10-04

- GOA refresh (commit a3cf70b6d): no new rows and no retired rows; only WITH/FROM
  (`supporting_entities`) and qualifier backfill on the 12 existing rows. 0 PENDING.
- All 12 rows re-audited against current policy (IBA node-placement rule, protein-binding
  policy, positive support for ACCEPT/KEEP). No protein-binding rows.
- GO:0016705 (IEA, GO_REF:0000002) remains MODIFY, but the replacement was changed from
  GO:0004497 monooxygenase activity to GO:0016712 (oxidoreductase ... reduced flavin or
  flavoprotein as one donor, and incorporation of one atom of oxygen). QuickGO is_a ancestry
  of GO:0016712 includes both GO:0016705 and GO:0004497, so it is the true refinement;
  GO:0004497 is a sibling branch of GO:0016705, not a child. UniProt catalytic activity is
  RHEA:17149 / EC 1.14.14.1 with NADPH--hemoprotein reductase as donor.
- core_functions molecular_function changed GO:0004497 -> GO:0016712 for the same reason;
  added location GO:0005789 endoplasmic reticulum membrane (UniProt: "Endoplasmic reticulum
  membrane; Peripheral membrane protein").
- GO:0004497 TAS (PMID:2107330) kept ACCEPT; added positive support: the abstract (gene
  sequencing paper, abstract-only) notes the conserved ninth-exon region "is associated with
  the noncovalently bound heme iron at the enzyme's active site" [PMID:2107330], plus the
  UniProt FUNCTION line.
- GO:0019369 arachidonate metabolic process (IBA) kept MARK_AS_OVER_ANNOTATED: the argument
  is node placement (single Cyp2d4 seed, RGD:620640, at PTN000670525), which is the allowed
  way to challenge an IBA.
- Open question: no direct enzymology on rat CYP2D10 substrate specificity is available;
  the xenobiotic MF/BP rest on CYP2D-family inference.
