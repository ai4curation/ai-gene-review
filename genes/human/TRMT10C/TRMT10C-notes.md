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

| gene product | complex | qualifier | evidence |
|---|---|---|---|
| RPPH1 and other ncRNA entries | nuclear (the catalyst) | `enables` | IEA |
| POP1 | nuclear | `contributes_to` | IBA, IDA |
| POP4, POP5, POP7, RPP14, RPP21, RPP25, RPP30, RPP38, RPP40 | nuclear | `contributes_to` | IDA |
| PRORP | **mitochondrial** (the catalyst) | `enables` | IBA, IDA, IEA |

Note the complex column: PRORP (O15091) is `part_of GO:0030678`, the *mitochondrial* complex,
not the nuclear one. So no nuclear **protein** subunit carries `enables` at all - the nuclear
catalyst is an RNA - and PRORP is the only protein in either complex that does, because the
mitochondrial catalyst is a protein.

(POP5, RPP30 and RPP40 additionally carry an `enables` row by IEA or TAS; every IDA row on a
protein subunit other than PRORP is `contributes_to`.)

So GO's convention for an RNase P holoenzyme is `enables` for whatever does the chemistry -
the RPPH1 RNA in the nucleus, PRORP in mitochondria - and `contributes_to` for the other
protein subunits. That is exactly the shape of the proposed row: TRMT10C does not do the
chemistry, and the ten nuclear protein subunits in the same position all carry the term with
this qualifier. Neither mitochondrial accessory subunit carries `GO:0004526` in GOA, so they
are the outliers.

The nuclear subunit genes have no folders in this repository, so this table is the only
in-branch record of the query; re-run the curl above to check it.

### What HSD17B10's review actually says

HSD17B10/MRPP2 is the other non-catalytic subunit of the mitochondrial complex, and its
review is not a stub despite `status: INITIALIZED` — 101 reviewed rows (49 ACCEPT, 36
KEEP_AS_NON_CORE, 16 MARK_AS_OVER_ANNOTATED, none unreviewed), three authored core functions,
and `proposed_new_terms: []`. Its third core function models the moonlighting role as
`GO:0000049` tRNA binding plus `in_complex GO:0030678`, which is a recorded judgment to argue
with rather than an absence. Under the comparator above that review warrants the same
`contributes_to` proposal. TRMT10C also carries `GO:0000049`, so the two reviews differ only
in this one proposed row.
