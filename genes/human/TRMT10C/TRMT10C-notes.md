# TRMT10C notes

Literature review was done manually from cached PubMed records; the falcon deep-research report (TRMT10C-deep-research-falcon.md) completed afterwards and was skimmed for consistency with the review decisions; no conflicts were found.

- MRPP1-MRPP2 subcomplex is the m1G9/m1A9 methyltransferase [PMID:23042678 "a subcomplex of human mitochondrial RNase P, the endonuclease removing tRNA 5' extensions, is the methyltransferase responsible for m(1)G9 and m(1)A9 formation"].
- Mitochondrial RNase P is a protein-only enzyme from three proteins [PMID:18984158 "human mitochondrial RNase P is a protein enzyme that does not require a trans-acting RNA component for catalysis"].
- MRPP1/2 acts as a tRNA maturation platform for ELAC2 and TRNT1 [PMID:29040705].
- Disease (COXPD30): variants destabilise MRPP1 and impair processing without abolishing methylation [PMID:27132592 "these variants affect MRPP1 protein stability and mt-tRNA processing without affecting m(1)R9 methyltransferase activity"].
- Nucleus/nucleoplasm IBA come from a PANTHER node above the TRMT10A/TRMT10C split (donor TRMT10A, Q8TBZ6); removed.

## Comparator check behind the proposed `contributes_to GO:0004526`

CLAUDE.md requires a comparator check before a `NEW`, naming two or three gene products
standing in the *same role*. The role here is "non-catalytic protein subunit of an RNase P
holoenzyme", and the nuclear holoenzyme supplies ten of them: its catalytic moiety is the
RPPH1 RNA, not any protein, so GO must say something about the proteins' relation to the
activity. Query run 2026-10-12 against QuickGO:

```
curl -H 'Accept: application/json' \
  'https://www.ebi.ac.uk/QuickGO/services/annotation/search?goId=GO:0004526&taxonId=9606&limit=100&goUsage=exact'
```

40 human annotations. Grouped by symbol and qualifier:

| gene product | complex it is recorded in | qualifier | evidence | rows |
|---|---|---|---|---|
| POP1 | `GO:0005655` | `contributes_to` | IBA 1, IDA 2 | 3 |
| POP4 | `GO:0005655`, `GO:0030677` | `contributes_to` | IDA | 1 |
| POP7, RPP21, RPP25 | `GO:0005655` | `contributes_to` | IDA | 1 each, 3 |
| RPP14 | `GO:0005655`, `GO:0030677` | `contributes_to` | IDA | 1 |
| RPP38 | `GO:0005655` | `contributes_to` | IBA 1, IDA 1 | 2 |
| POP5 | `GO:0005655`, `GO:0030677` | `contributes_to` | IDA | 1 |
| **POP5** | `GO:0005655`, `GO:0030677` | **`enables`** | **IEA** | **1** |
| RPP30 | `GO:0005655` | `contributes_to` | IDA | 1 |
| **RPP30** | `GO:0005655` | **`enables`** | **TAS** | **1** |
| RPP40 | `GO:0005655`, `GO:0030677` | `contributes_to` | IBA 1, IDA 1 | 2 |
| **RPP40** | `GO:0005655`, `GO:0030677` | **`enables`** | **TAS** | **1** |
| PRORP | `GO:0030678` | `enables` | IBA 1, IDA 1, IEA 5 | 7 |
| RPPH1, the nuclear catalyst, under 4 RNAcentral ids (`URS000013F331`, `URS000061A549`, `URS000071B825`, `URS0002A685AF`) | `GO:0030677` | `enables` | IEA | 4 |
| 10 further RNAcentral ncRNA ids not named as RPPH1: 3 `HSALNT*`, 2 `LHRI_LNC*`, 3 `lnc-*` (CCNB1IP1, PDGFC), 2 unnamed (`ncRNA`, `non-coding RNA`) | `GO:0030677` | `enables` | IEA | 10 |
| `ComplexPortal:CPX-6155` mribonucleasep_human, the whole complex | n/a, is the complex | `enables` | IDA | 1 |
| `ComplexPortal:CPX-2877` rnasep_human, the whole complex | n/a, is the complex | `enables` | IPI | 1 |

`GO:0005655` is nucleolar ribonuclease P complex, `GO:0030677` ribonuclease P complex and
`GO:0030678` mitochondrial ribonuclease P complex. Their ancestry is read from `runoak
relationships` on 2026-10-12 rather than from memory, and it is not the flat parent/child shape
an earlier draft of this paragraph asserted: `GO:0030677` is the direct `is_a` parent of
`GO:0030678`, but reaches `GO:0005655` only through `GO:0030681` multimeric ribonuclease P
complex, so it sits two levels above the nucleolar term and one above the mitochondrial one.
The asymmetry does not change the reading below, since `GO:0030677` is still the term both
specific complexes descend from, but "generic parent" was wrong for the nucleolar side.

The column records the term each gene product is actually annotated to rather than a
nuclear/mitochondrial reading of it, which is a third query and is logged below. It does not
apply to the two ComplexPortal rows, which are the assembled complexes themselves rather than
parts of one; those two cells read `n/a, is the complex` and come from no query. Two things the
column shows that "nuclear" would have hidden: every one of the ten protein subunits is in the
nucleolar term, while **none** of the fourteen ncRNA ids is - they carry `GO:0030677` and
nothing below it, RPPH1's four included. So the ncRNA `enables` rows are not recorded as
nucleolar-complex members at all, which is consistent with reading them as a Rfam-style
electronic propagation rather than as curated subunit annotations.

Rows sum to 40, which is the hit count, so nothing was truncated at `limit=100`.

The three bold rows are the exceptions, and they are in the table rather than only in the
prose below for the same reason the ComplexPortal rows are: a reader who checks the table
and stops there would otherwise come away with the absolute claim this file spent a round
retracting. The two ComplexPortal rows are assembled complexes rather than proteins, which
is why they carry `enables` and why the claims below are scoped to proteins; `CPX-6155` is
the only `enables` row with a direct-assay code other than PRORP's.

Note the complex column: PRORP (O15091) is `part_of GO:0030678`, the *mitochondrial* complex,
not the nuclear one. The nuclear catalyst is an RNA, so the `enables` rows there sit on ncRNA entries
rather than on any protein subunit - four of them RPPH1 itself and ten further RNAcentral
ids that are not named as RPPH1 - but not absolutely: POP5, RPP30 and RPP40 each also carry an
`enables` row, POP5 by IEA and the other two by TAS. What holds without exception is the
evidence-code version. **Every IDA row on a nuclear protein subunit is `contributes_to`**, and
PRORP is the only protein in either complex carrying `enables` by direct assay, because the
mitochondrial catalyst is a protein. The experimental curation lines up behind `contributes_to`
for the subunits; only the electronic and author-statement rows do not, which is the propagation
class this repository treats as arguable.

So GO's convention for an RNase P holoenzyme is `enables` for whatever does the chemistry -
the RPPH1 RNA in the nucleus, PRORP in mitochondria - and `contributes_to` for the other
protein subunits. That is exactly the shape of the proposed row: TRMT10C does not do the
chemistry, and the ten nuclear protein subunits in the same position all carry the term with
this qualifier. Neither mitochondrial accessory subunit carries `GO:0004526` in GOA, so they
are the outliers.

The complex assignment above is a separate query from the qualifier table, and it is the one
this correction turned on, so it is logged rather than asserted:

```
curl -H 'Accept: application/json' \
  'https://www.ebi.ac.uk/QuickGO/services/annotation/search?geneProductId=UniProtKB:O15091&goId=GO:0030678&limit=20&goUsage=exact'
```

4 annotations, all `PRORP | GO:0030678 | part_of`, by IBA, IDA, IPI and TAS. So PRORP is a part
of the *mitochondrial* ribonuclease P complex, which is what makes it the counterpart rather
than a member of the nuclear comparator set.

The complex column for the 25 protein and ncRNA gene products in the table - the ten nuclear
subunits, PRORP and the fourteen RNAcentral ids, which is every entity in it but the two
ComplexPortal complexes - comes from a third query, run 2026-10-12, because the
qualifier query above returns gene product, qualifier and evidence and says nothing about
complex membership - so filling that column from it would be an inference rather than a
record:

```
curl -H 'Accept: application/json' \
  'https://www.ebi.ac.uk/QuickGO/services/annotation/search?goId=GO:0005655&taxonId=9606&limit=100&goUsage=exact'
```

run for `GO:0005655`, `GO:0030677` and `GO:0030678`, plus a per-id
`geneProductId=RNAcentral:URS..._9606` query for each of the fourteen ncRNA ids. Results:
all ten protein subunits are in `GO:0005655`, four of them also in `GO:0030677`; PRORP is in
`GO:0030678` only; and all fourteen ncRNA ids are in `GO:0030677` only, each by `part_of` IEA.

The ancestry among the three complex terms is from the ontology rather than from QuickGO:

```
uv run runoak -i sqlite:obo:go relationships GO:0005655 GO:0030678 GO:0030681
```

`GO:0005655 is_a GO:0030681 is_a GO:0030677` and `GO:0030678 is_a GO:0030677`, which is where the
two-levels-versus-one asymmetry above comes from.

The nuclear subunit genes have no folders in this repository, so these tables are the only
in-branch record of the three queries logged above - `goId=GO:0004526`, 
`geneProductId=UniProtKB:O15091&goId=GO:0030678`, and the complex-term family - plus the
per-id ncRNA queries; re-run the curls above to check them.

### What HSD17B10's review actually says

HSD17B10/MRPP2 is the other non-catalytic subunit of the mitochondrial complex, and its
review is not a stub despite `status: INITIALIZED` — 101 reviewed rows (49 ACCEPT, 36
KEEP_AS_NON_CORE, 16 MARK_AS_OVER_ANNOTATED, none unreviewed), three authored core functions,
and `proposed_new_terms: []`. Its third core function models the moonlighting role as
`GO:0000049` tRNA binding plus `in_complex GO:0030678`, which is a recorded judgment to argue
with rather than an absence. Under the comparator above that review warrants the same
`contributes_to` proposal. TRMT10C also carries `GO:0000049`, so the two reviews differ only
in this one proposed row.

## The organelle-level localization rows

The eight `GO:0005739` mitochondrion rows are `ACCEPT`, and that is a decision rather than an
oversight. TRMT10C (MRPP1) is a mitochondrial matrix protein and `GO:0005759` is accepted here on
three rows, so a reader applying the "correct but general terms are MODIFY" rule mechanically, or
re-running an ancestor-based scan, will stop on these. They are not reached by that rule: none of
the eight reasons says the term is less specific than the evidence supports — they give the proteome
and localization evidence and the gene's function. Nothing else in this file refines a
mitochondrial-location ancestor, so the file does not treat one argument two ways. Whether GOA's
organelle-level rows should be refined wherever a compartment row exists is a real question, and it
is a slice-wide one rather than anything specific to this gene.
