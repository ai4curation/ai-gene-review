# ecm31 (Q09672, SPAC5H10.09c) notes

Role: ketopantoate hydroxymethyltransferase PanB (EC 2.1.2.11); module `coenzyme_a_biosynthesis` (pantoate branch, step 1).
Fetch: `just fetch-gene SCHPO ecm31` FAILED (UniProt has no gene name for this entry: "PomBase; SPAC5H10.09c; -."); refetched with `-u Q09672`.

## Evidence
- Family and reaction [UniProt:Q09672 "SIMILARITY: Belongs to the PanB family."]; no S. pombe experiments on activity.
- Mitochondrial in ORFeome screen [PMID:16823372] (PomBase HDA). S. cerevisiae ECM31 deletion requires pantothenate [PMID:19266201 "we show that deletion of ECM31 and PAN6 results in mutants requiring pantothenate"].
- Gene is adjacent to pan6 (SPAC5H10.08c).

## Decisions
- cytoplasm IBA (seeded only by E. coli PanB) -> MODIFY to mitochondrion.
- `monocarboxylic acid biosynthetic process` -> MODIFY to pantothenate biosynthetic process.
- Mg binding IBA non-core.
- Core: GO:0003864 / GO:0015940 / GO:0005739 — matches S. cerevisiae ECM31 review and PomBase GO-CAM 67b1629100001098; YeastPathways places ECM31 in cytosol.
