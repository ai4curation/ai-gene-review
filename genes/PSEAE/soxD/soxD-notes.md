# soxD (PA5417, Q9HTE7) — review notes

Tier-3 PseudoCAP review, done as part of the four-subunit sarcosine oxidase group
(`soxA`, `soxB`, `soxD`, `soxG`). The group-level evidence, the wrong-reference finding and
the argument about which subunit is catalytic are set out in `soxB-notes.md`; this file records
what is specific to the delta subunit.

## Wrong reference

The `GO:0008115` IMP row cites **PMID:17951382**, which PubMed shows to be
"Role of RelA of Streptococcus mutans in global control of gene expression" (Nascimento et
al., *J Bacteriol* 2008, DOI 10.1128/JB.01395-07) — a *S. mutans* stringent-response study with
no bearing on *P. aeruginosa* sarcosine catabolism. The intended paper is **PMID:17951379**.
All four sox subunits carry this same transposition, each citing a different unrelated paper
from the same *J Bacteriol* issue block. Recorded as a `WRONG_REFERENCE` defect at
`CONFIRMED`; see `soxB-notes.md` for the full table and reasoning.

## What SoxD is

106 residues. The UniProt record carries:

- `DE   SubName: Full=Sarcosine oxidase delta subunit {ECO:0000313|EMBL:AAG08802.1}` — a
  submitter-supplied name (`ECO:0000313`), which the project rules class as an unvetted
  import and therefore not valid support. Not cited.
- `[file:PSEAE/soxD/soxD-uniprot.txt "DR   InterPro; IPR006279; SoxD."]` and
  `[file:PSEAE/soxD/soxD-uniprot.txt "DR   Pfam; PF04267; SoxD; 1."]` — a subunit-specific
  family signature, which *is* good support for membership.
- `PE   4: Predicted;` — the weakest existence level. Recorded because it bears on how much
  the rows can carry, never cited to support an ACCEPT.

No cofactor, no catalytic activity and no domain other than SoxD itself appear on the record.

## Why `contributes_to`, not `enables`, and not over-annotation

Size and the absence of a cofactor rule SoxD out as the catalytic chain — that is SoxB, the
only subunit with a flavin and a D-amino-acid-oxidase-family domain. So `enables
GO:0008115` over-reaches, and the row should read `contributes_to`, exactly as the merged
`ccoO1` and `ccoP1` reviews requested for the non-catalytic cbb3 oxidase chains.

But SoxD is **not** the CcoQ case, where the review used `MARK_AS_OVER_ANNOTATED`. Three
things distinguish it:

1. The characterised enzyme is a four-subunit complex, not a three-subunit core with an
   accessory chain: `[PMID:17951379 "a heterotetrameric sarcosine oxidase converts sarcosine into glycine"]`.
2. The operon is `soxBDAG` — delta is one of the four genes the paper names, and its
   transposon mutants share the class II phenotype:
   `[PMID:17951379 "The 10 mutants in class II were unable to grow on choline, GB, or DMG"]`.
3. `IPR006279` is a dedicated, conserved SoxD family signature. A protein with its own
   subunit family across the sarcosine oxidase systems is a recognised structural subunit,
   not an ORF that happens to sit in the operon.

So the activity claim is kept at complex level with the qualifier corrected, and the delta
subunit is given `contributes_to_molecular_function` in `core_functions`.

The qualifier defect is recorded **once**, on the IMP row against PseudoCAP, rather than on
both rows, so that the upstream report carries a single request per gene. The IEA row's
`reason` notes that the same relation applies to it.

## What is genuinely unknown

What the delta subunit does is not known for any member of the family as far as this review
established: it has no cofactor and no catalytic motif, and the paper tests it only as part of
the operon. Whether it is an assembly factor, a structural brace, or contributes residues to
the active site of the complex is open, and is recorded as a BIOLOGY knowledge gap with a
matching suggested experiment rather than guessed at.
