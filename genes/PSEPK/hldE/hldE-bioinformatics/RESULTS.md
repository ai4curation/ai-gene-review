# Results: no HldD epimerase in P. putida KT2440

## Checklist
- [x] Script has no hardcoded accessions, hit counts or biological conclusions.
- [x] A positive-control organism runs the identical queries, so an empty target result is interpretable.
- [x] All six queries completed; the script exits non-zero if any fails, so a partial run cannot read as a negative.
- [x] Raw output retained as `hldd_absence.tsv`.
- [x] Limits of the inference stated below.

## Question

The ADP-heptose route produces ADP-D-glycero-beta-D-manno-heptose. Only a C-6
epimerase (HldD/RfaD, EC 5.1.3.20) converts that to the L,D stereoisomer named by
GO:0097171. Whether KT2440 reaches the L,D endpoint therefore depends on whether it
encodes such an epimerase, which decides the GO:0097171 rows on Q88D93 (hldE) and
Q88RS0 (gmhB).

## Result

Run 2026-11-02 against the UniProt REST API.

| organism | role | gene name hldD/rfaD | EC 5.1.3.20 | name text |
|---|---|---|---|---|
| *P. putida* KT2440 (160488) | target | 0 | 0 | 1 |
| *P. aeruginosa* PAO1 (208964) | positive control | 1 | 1 | 1 |

The positive control returns Q9HYQ8 `hldD rfaD PA3337`
"ADP-L-glycero-D-manno-heptose-6-epimerase (EC 5.1.3.20)" on all three queries, so
the queries work.

For KT2440 the gene-name and EC queries return nothing. The single name-text hit is
Q88HZ6 `PP_3206`, "NAD-dependent epimerase/dehydratase domain-containing protein" —
a generic domain-level name with no heptose or 6-epimerase assignment, matched only
because the query is a substring search over protein names. It is not an annotated
HldD.

## Interpretation

KT2440 has no annotated ADP-heptose 6-epimerase, so on present evidence its pathway
terminates at ADP-D-glycero-beta-D-manno-heptose and does not reach the L,D
stereoisomer.

Two independent lines agree with this, and neither depends on these queries:

- PANTHER's committed member inventory for the HldD family: KT2440's only member of
  `PTHR43103` is the uronate dehydrogenase Q88NN6, placed in the 4-epimerase
  subfamily `SF5`. The 161-member heptose 6-epimerase subfamily `SF3`, which
  contains both PSEAE hldD (Q9HYQ8) and *E. coli* hldD (P67910), has no KT2440
  member at all. KT2440 is itself present in that inventory, so the absence is not
  a sampling artefact. See `interpro/panther/PTHR43103/PTHR43103-entries.csv`.
- The project deep-research page for this pathway reaches the same conclusion from
  KEGG, UniProt/UniRef, RefSeq and genome-level similarity search, calling the step
  "a genome-confirmed GAP in KT2440". See
  `projects/P_PUTIDA/deep-research/PSEPK__adp-heptose-biosynthesis__ppu00541-deep-research-openscientist.md`.

## Limits

This is an annotation-absence argument, not a biochemical one. It shows that no
protein in KT2440 is *annotated* as an ADP-heptose 6-epimerase; it cannot exclude an
unannotated or non-orthologous enzyme performing the same C-6 epimerization, and no
assay on KT2440 heptose stereochemistry was examined. Q88HZ6 in particular is an
uncharacterized NAD-dependent epimerase/dehydratase whose substrate is unknown, so
it is not positively excluded as a candidate — only shown not to be an annotated
HldD, and not placed in the HldD subfamily by PANTHER. The queries hit a live
service, so counts can change as UniProt is updated; re-run with `just` to refresh.
