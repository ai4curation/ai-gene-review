# soxG (PA5419, Q9HTE5) — review notes

Tier-3 PseudoCAP review, done as part of the four-subunit sarcosine oxidase group
(`soxA`, `soxB`, `soxD`, `soxG`). The group evidence, the wrong-reference finding and the
argument about which subunit is catalytic are in `soxB-notes.md`; this file records what is
specific to the gamma subunit.

## Wrong reference

The `GO:0008115` IMP row cites **PMID:17951386**, which PubMed shows to be "Transmembrane
helix 12 of the Staphylococcus aureus multidrug transporter QacA lines the bivalent cationic
drug binding pocket" (Hassan, Skurray & Brown, *J Bacteriol* 2007, DOI 10.1128/JB.01492-07) —
a *S. aureus* efflux-transporter mutagenesis study. The intended paper is **PMID:17951379**.
All four sox subunits carry the same transposition from the same *J Bacteriol* issue block.
Recorded as a `WRONG_REFERENCE` defect at `CONFIRMED`; the full table is in `soxB-notes.md`.

## What SoxG is

211 residues. The record carries:

- `DE   SubName: Full=Sarcosine oxidase gamma subunit {ECO:0000313|EMBL:AAG08804.1}` — a
  submitter-supplied name (`ECO:0000313`), an unvetted import under the project rules, so not
  cited as support.
- `[file:PSEAE/soxG/soxG-uniprot.txt "DR   InterPro; IPR007375; SoxG."]` and
  `[file:PSEAE/soxG/soxG-uniprot.txt "DR   Pfam; PF04268; SoxG; 1."]` — a subunit-specific
  family signature, which is good support for membership. The record also lists
  `IPR006280 SoxG_het`, a signature for the gamma subunit of the *heterotetrameric* enzyme
  specifically, and `IPR027266 TrmE/GcvT-like`.
- `PE   4: Predicted;` — recorded as a limit on what the rows can carry, never cited to
  support an ACCEPT.

No cofactor and no catalytic activity appear on the record.

## Why `contributes_to`, not `enables`

Same reasoning as for `soxD`: the flavin and the D-amino-acid-oxidase-family domain are on
SoxB, so SoxB is the catalytic chain and SoxG contributes to the holoenzyme's activity rather
than enabling it. The `enables` qualifier is an operon-level phenotype transferred to each
subunit, and the correction requested is `enables` → `contributes_to`, as the merged
`ccoO1`/`ccoP1` reviews requested for the non-catalytic cbb3 chains.

As with `soxD`, this is not the `ccoQ1` over-annotation case. The paper describes a
heterotetramer, the operon names four genes, the `soxABDG` transposon mutants share the class
II phenotype, and `IPR006280` is a signature specific to the gamma subunit *of the
heterotetrameric enzyme* — a protein with a dedicated subunit family in the characterised
systems is a structural subunit, not a passenger.

One thing worth noting in the gamma subunit's favour: `IPR027266 TrmE/GcvT-like` is the same
broad fold group that appears on the alpha subunit's folate-binding (GcvT) region. That is
consistent with gamma sitting near the folate-handling half of the complex, but it is a fold
similarity on a 211-residue chain with no cofactor, so this review does not turn it into a
claim. It is left as a question.

## No tetrahydrofolate row

Unlike `soxA`, `soxB` and `soxD`, `soxG` has **no** `GO:0046653 tetrahydrofolate metabolic
process` row in GOA — its only two rows are the `GO:0008115` IEA and IMP. That looks like an
InterPro2GO coverage difference (`IPR006280`/`IPR007375` carry no folate mapping where
`IPR006277`/`IPR006278`/`IPR006279` do) rather than a biological distinction, since the gamma
subunit is part of the same folate-dependent holoenzyme.

This review does **not** propose the missing row as `NEW`. The reason is the project's own bar
for `NEW`: a process term needs the product to do some of the work, and nothing here
establishes that SoxG handles folate — the fold hint above is not evidence, and "the other
three subunits have this term and mine does not" is precisely the comparator reasoning the
rules warn is usually a convention rather than a gap. The asymmetry is recorded here instead,
as a curation observation, which is where a mapping-coverage gap belongs.
