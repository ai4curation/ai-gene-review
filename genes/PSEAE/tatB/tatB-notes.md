# tatB (PA5069, Q9HUB4) — review notes

Tier-3 PseudoCAP review. `tatB` is the last unreviewed member of the `GO:0008320` /
PMID:16621825 shared claim; `tatA` and `tatC` are already merged.

## What the protein is

Single-pass inner-membrane subunit of the twin-arginine translocation system, assigned to
the TatB family by HAMAP MF_00237.

- `[file:PSEAE/tatB/tatB-uniprot.txt "Together with\nTatC, TatB is part of a receptor directly interacting with Tat signal\npeptides."]`
- `[file:PSEAE/tatB/tatB-uniprot.txt "TatB may form an oligomeric binding site that transiently\naccommodates folded Tat precursor proteins before their translocation."]`
- `[file:PSEAE/tatB/tatB-uniprot.txt "The Tat system comprises two distinct complexes: a TatABC"]`
- `[file:PSEAE/tatB/tatB-uniprot.txt "Cell inner membrane"]`, `Single-pass membrane protein`,
  and one TM segment (`FT   TRANSMEM        1..21`).
- `PE   3: Inferred from homology` — no direct experimental evidence on the PAO1 protein
  itself. Noted because it bears on how much the IMP rows can carry, not used as support
  for any ACCEPT.

The PANTHER family on the record is `PTHR33162`, whose official name is
`SEC-INDEPENDENT PROTEIN TRANSLOCASE PROTEIN TATA, CHLOROPLASTIC`. That is the usual case
of a family name dominated by one member and is not evidence of a misassignment — the TatB
family assignment comes from HAMAP, and the IBA node's donors include the canonical E. coli
TatB.

## IBA node donors — checked, not assumed

The `GO:0009977`, `GO:0043953` and `GO:0065002` IBA rows all come from
`PANTHER:PTN002109144`. The `WITH/FROM` accessions were resolved against the UniProt REST
API rather than read from memory:

| accession | entry | organism |
|---|---|---|
| P69425 | TATB_ECOLI, Sec-independent protein translocase protein TatB | *E. coli* K12 |
| O48950 | TATB_MAIZE, TatB chloroplastic | *Zea mays* |
| Q9XFJ8 | TATA_MAIZE, TatA chloroplastic | *Zea mays* |

Plus `AGI_LocusCode:AT5G52440`. A node seeded by the canonical E. coli TatB together with
the plant thylakoid Tat machinery is a sound placement for a bacterial TatB; the short
donor list is not weakness (per the IBA guidance). `tatB` does not appear in its own
`WITH/FROM`, consistent with having no experimental annotation of its own for these terms.

## The reference

PMID:16621825 (Voulhoux, Filloux & Schalk 2006) is the PseudoCAP source for both IMP rows.
The cached entry is **abstract-only** (`full_text_available: false`) and the abstract names
no individual tat gene — it speaks of "a tat mutant" throughout.

- `[PMID:16621825 "However, in the tat mutant, no Pvd was produced."]`
- `[PMID:16621825 "FpvA is correctly located in the outer membrane of a tat mutant and is fully functional for all steps of the iron uptake process"]`

So the evidence is a pathway-level export phenotype. It cannot distinguish which subunit
contributes what, and it is the same paper PseudoCAP used for `tatA` and `tatC` — a
deliberate practice across the operon, not a slip, so no source defect is recorded. Per the
project rule against overruling curators from incomplete evidence, the membership and
transporter claims are accepted on the family assignment and the E. coli record, with the
indirectness stated in the row rather than held against it.

## The tatA/tatC divergence, and where tatB falls

PR #6499 recorded an unresolved divergence on this shared claim: `GO:0008320` is
`MODIFY`→`GO:0009977` on `tatA` but `TOO_GENERAL` on `tatC`. Fetching `tatB` shows the
asymmetry is in GOA, and now resolves 2:1:

| gene | `GO:0009977` in GOA | `GO:0008320` in GOA | verdict on `GO:0008320` |
|---|---|---|---|
| tatA | **absent** | IBA, IEA, IMP | `MODIFY` → `GO:0009977` |
| tatB | IBA | IEA, IMP | `TOO_GENERAL` (this review) |
| tatC | IBA | IEA, IMP | `TOO_GENERAL` |

`tatB` and `tatC` have identical row shapes, so `tatB` takes `tatC`'s encoding: accept
`GO:0009977` where GOA asserts it, and mark the ancestor `GO:0008320` rows `TOO_GENERAL`.
`tatA` differs only in that PAINT gave its node (`PTN002452729`, the TatA/TatE node) the
general term, so its reviewer had to propose the specific term rather than accept it.

Whether `tatA`'s `MODIFY` clears the 2026-11-14 bar — which requires that row's own
evidence for the deeper term, and whose IMP reason cites an export phenotype — is a
question about a merged review and is **not** touched here. It remains open for a human, as
recorded on the project page. What this review adds is that the majority shape is
`TOO_GENERAL`, and that the difference is a GOA/PAINT artifact rather than a disagreement
about the biology: all three reviews agree the protein is a PMF-driven Tat translocon
subunit, and `tatA` carries `GO:0009977` as its core-function MF too.

## Terms checked in OLS

Relations relied on in the review, verified rather than asserted from memory:

- `GO:0009977` is_a `GO:0008320` (so the IEA/IMP rows on the parent are `TOO_GENERAL`)
- `GO:0005886` is_a `GO:0016020` (so the `membrane` row is `TOO_GENERAL`)
- `GO:0015031` **is** among `GO:0043953`'s ancestors (so the `protein transport` row is
  `TOO_GENERAL`)
- `GO:0065002` is **not** among `GO:0043953`'s ancestors — they are siblings, so both are
  kept and neither is redundant. This matches the reasoning in the merged `tatC` review.
