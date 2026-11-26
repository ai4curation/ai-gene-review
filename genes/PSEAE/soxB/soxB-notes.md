# soxB (PA5416, Q9HTE8) — review notes

Tier-3 PseudoCAP review. Reviewed as one of four subunits of the heterotetrameric sarcosine
oxidase, together with `soxA`, `soxD` and `soxG`, rather than gene by gene.

## The reference is wrong on all four sox genes

GOA carries `GO:0008115 sarcosine oxidase activity` by IMP on all four subunits, each citing
a **different** PMID:

| gene | cited PMID | what that PMID actually is |
|---|---|---|
| soxB | PMID:17951380 | *S. aureus* Newman genome sequence (Baba et al.) |
| soxD | PMID:17951382 | *S. mutans* RelA and global gene control (Nascimento et al.) |
| soxA | PMID:17951384 | a transcript-cleavage-factor commentary (Hochschild) |
| soxG | PMID:17951386 | *S. aureus* QacA multidrug transporter (Hassan et al.) |

None concerns *P. aeruginosa*, sarcosine, or oxidases. All four are *J Bacteriol* papers
e-published on the same day, 2007-10-19 — one issue's block of consecutive PMIDs, which is
why the four ids are evenly spaced two apart.

The intended paper is **PMID:17951379**, immediately below that block, same journal, same
e-publication date: Wargo, Szwergold & Hogan, "Identification of two gene clusters and a
transcriptional regulator required for Pseudomonas aeruginosa glycine betaine catabolism".
Its abstract names the genes directly:

`[PMID:17951379 "Mutant analyses and 13 C NMR studies also confirmed that the soxBDAG genes, predicted to encode a sarcosine oxidase, are required for sarcosine catabolism"]`

Titles and metadata were verified against PubMed; the wrong PMID is live in today's GOA, not
an artefact of a stale worklist. A `WRONG_REFERENCE` defect is recorded on each of the four
reviews with `requested_change: REPOINT` and `cause: IDENTIFIER_TRANSPOSITION`, at
`confidence: CONFIRMED` — the project rule allows a confident claim where a PMID's title is
on an unrelated subject and a near-identical PMID is the obvious intended paper, which is the
case four times over here.

**A side effect worth recording:** these wrong references *concealed a shared claim*. One term
on four subunits of one complex from one paper is exactly the group the PseudoCAP audit is
built to catch, but `build_pseudocap_mf_worklist.py` keys groups on (term, reference), so four
bogus and mutually different PMIDs split the group into four singletons. The group only
becomes visible once the references are corrected.

## What the paper actually shows, and what it does not

The evidence is genetic and spectroscopic, never a protein assay:

- `[PMID:17951379 "The 10 mutants in class II were unable to grow on choline, GB, or DMG"]` —
  transposon insertions in all of `soxABDG` fall in this class.
- `[PMID:17951379 "only sarcosine was detected at 9 h in extracts from soxA"]` — the ¹³C NMR
  experiment was run on a **`soxA` mutant only**. No NMR or growth-intermediate data are
  reported for `soxB`, `soxD` or `soxG` individually.
- `[PMID:17951379 "designated based on their strong homology to the sarcosine oxidase system in Corynebacterium"]` —
  the gene names come from homology, not from activity measured here.
- `[PMID:17951379 "Consistent with the genetic and bioinformatics evidence that soxBDAG genes encode an enzyme that catalyzes the conversion of sarcosine to glycine"]`
- `[PMID:17951379 "our mutagenesis and NMR data verified the role of the predicted sarcosine oxidase"]`

The authors hedge consistently — "predicted", "putative" — and never claim to have assayed
sarcosine oxidase activity in *P. aeruginosa*. So a `GO:0008115` IMP row is the tier-3 pattern
exactly: a molecular function asserted from a growth phenotype. The claim is nonetheless sound
for this organism, because the genetics, the ¹³C flux block and the family assignments agree;
what the phenotype cannot do is say **which subunit** carries the catalytic site.

## Which subunit does the chemistry

`[PMID:17951379 "a heterotetrameric sarcosine oxidase converts sarcosine into glycine"]` — the
enzyme is a four-subunit complex, so the cbb3-oxidase principle applies: the catalytic activity
belongs to the chain carrying the catalytic cofactor, and the others contribute.

From the UniProt records:

| gene | subunit | evidence on the record | PE |
|---|---|---|---|
| soxB | beta | `RecName` sarcosine oxidase subunit beta, `EC=1.5.3.24`, two CATALYTIC ACTIVITY reactions, FAD and FMN cofactors; Pfam `PF01266` (DAO), InterPro `IPR006278` (SoxB), `IPR006076` (FAD-dep_OxRdtase) | 3 |
| soxA | alpha | InterPro `IPR006277` (Sarcosine_oxidase_asu), `IPR041117` (SoxA_A3), GcvT folate-binding domains, FAD/NAD-binding, 2Fe-2S ferredoxin-type | 3 |
| soxD | delta | InterPro `IPR006279` (SoxD) only; no cofactor on the record | 4 |
| soxG | gamma | InterPro `IPR007375`/`IPR006280` (SoxG) only; no cofactor on the record | 4 |

So **soxB is the catalytic subunit**: it is the only one of the four whose record carries a
catalytic reaction, an EC number and a flavin. Its 416-residue length and the DAO
(D-amino-acid-oxidase family) Pfam domain match the beta subunit of the characterised
tetrameric enzymes.

Important caveat on citing this: soxB's `EC`, `RecName`, CATALYTIC ACTIVITY and COFACTOR lines
are all `ECO:0000256|ARBA:...` — ARBA association-rule predictions, which the project rules
classify as unvetted predictions and not valid support, and the `DE`/EC lines are labels in any
case. They are therefore **not** cited in `supported_by`; the family and domain signatures
(`DR Pfam`, `DR InterPro`), which *are* good support for membership, carry the argument
instead, together with the paper.

## Consequence for the qualifier

All four rows are coded `enables`. That is right for `soxB` and an over-reach for the other
three, which contribute to an activity they do not individually catalyse. A `WRONG_QUALIFIER`
defect (`enables` → `contributes_to`, `cause: SCOPE_OVER_REACH`, `confidence: PROBABLE`) is
recorded on `soxA`, `soxD` and `soxG` but **not** on `soxB`, following the pattern the merged
`ccoO1`/`ccoP1` reviews established for the cbb3 oxidase subunits.

## Localisation

`GO:0005737 cytoplasm` (IBA, is_active_in; IEA, located_in) is accepted. Glycine betaine
catabolism runs in the cytoplasm — `[PMID:17951379 "Once in the cytoplasm, choline binds to BetI"]` —
and the characterised tetrameric sarcosine oxidases are soluble. This matters for `soxA`, where
an IBA instead places the protein at the plasma membrane; see that review.
