# PA5190 (Q9HTZ9) — review notes

Tier-3 PseudoCAP review. PA5190 is the last unreviewed member of the `GO:0003955` /
PMID:25085734 shared claim; `PA0949`, `PA1204`, `PA2580` and `PA4975` are merged and all
ACCEPT the term.

## The paper assayed five enzymes, and PA5190 is one of them

PMID:25085734 (Green, La Flamme & Ackerley 2014) tested five *P. aeruginosa* quinone
oxidoreductases:

`[PMID:25085734 "the Pseudomonas aeruginosa orthologs of five quinone oxidoreductases--MdaB, ChrR, WrbA, NfsB, and NQO1--were tested for"]`

and measured the activity directly:

`[PMID:25085734 "each enzyme was shown to reduce quinone substrates with only minimal semiquinone formation"]`

The abstract gives names, not locus tags. The four merged siblings account for four of the
five by their own descriptions: `PA0949` is the WrbA ortholog, `PA1204` the ChrR-type
SsuE/chromate reductase, `PA2580` the MdaB orthologue and `PA4975` the NQO1 counterpart.
That leaves **NfsB**, and PA5190 is a nitroreductase-family protein — Pfam `PF00881`
Nitroreductase, InterPro `IPR000415` Nitroreductase-like, PANTHER `PTHR43673` "NAD(P)H
NITROREDUCTASE YDGI-RELATED" — while NfsB is the classic enterobacterial nitroreductase.

**This correspondence is an inference, not a record-backed fact.** PA5190's UniProt entry
carries no gene name at all (`GN   OrderedLocusNames=PA5190` only), the paper is
abstract-only, and nothing I could check states "PA5190 = NfsB". It is recorded as reasoning
in the review rather than asserted, and the annotation does not depend on it: the activity
claim stands on the shared-claim membership plus the family assignment either way.

## `GO:0003955` accepted, consistent with the siblings

The merged reviews accepted the term on direct in vitro assays of the purified *P.
aeruginosa* enzymes. PA5190 belongs to the same experiment and the same shared claim, and its
nitroreductase family is an NAD(P)H-dependent flavoenzyme family whose members reduce quinones
as well as nitroaromatics, so the term fits the fold.

One evidence-code observation, which the merged `PA0949` review already made and declined to
file: the activity was measured in vitro, so **IDA would be the natural code rather than
IMP**. Since the cache is abstract-only and the same understatement is present across all
five rows of the claim, it is a deliberate uniform practice rather than a slip, and no
`WRONG_EVIDENCE_CODE` defect is raised here either. Flagged for consistency with the
siblings, not as a new finding.

## `GO:0016491` is too general

`GO:0016491 oxidoreductase activity` (IEA, from `IPR000415`) is the root oxidoreductase
term. Checked in OLS: `GO:0003955`'s ancestors run `GO:0003824`, `GO:0016491`,
`GO:0016651 oxidoreductase activity, acting on NAD(P)H` and
`GO:0016655 ... quinone or similar compound as acceptor`. So `GO:0016491` is a genuine
ancestor of the accepted specific term and is imprecise on its own — it names neither the
donor nor the acceptor. `TOO_GENERAL`.

## What is not claimed

The protein is named "probable nitroreductase" and the family reduces nitroaromatics, but
**no nitroreductase activity row is proposed**. Nothing in this paper or on the record
measures a nitroaromatic substrate for PA5190, the `DE` name is a submitter-supplied
`ECO:0000313` import, and the family similarity statement's only evidence is ARBA — an
unvetted prediction under the project rules. Proposing an activity on that basis would be
manufacturing an assertion, which is what the `NEW` bar exists to prevent. It is recorded as
a knowledge gap and an experiment instead.

`PE   3: Inferred from homology`, noted as a limit on the rows rather than cited as support.
