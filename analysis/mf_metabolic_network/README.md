# MF-derived metabolic network vs. reviewed BP

**Question.** Can we assemble an organism-wide biochemical network using only the
*reviewed* molecular-function annotations in `genes/<ORG>/`, connecting enzymes through
shared chemicals? And does the topology of that network agree with the reviewed
biological-process annotations?

## Method (`build_network.py`)

1. **Reviewed terms per gene:** `core_functions[].molecular_function` /
   `contributes_to_molecular_function` / `directly_involved_in`, plus existing annotations
   with action `ACCEPT`, `KEEP_AS_NON_CORE` or `NEW`, plus MODIFY replacement terms. NOT
   annotations are skipped.
2. **MF → reaction:** only the `skos:exactMatch` Rhea xrefs in GO's editors' file
   (`go-edit.obo`), e.g. `xref: RHEA:11560 {source="skos:exactMatch"}`.
   - The released files (`go-basic.obo`, rhea2go, the GO column of the Rhea TSV) drop the
     predicate, so their narrowMatch and broadMatch xrefs look exact. Of the 7,738
     GO–Rhea pairs in the Rhea TSV, 3,262 are narrowMatch, 3 broadMatch, 7 unqualified and
     11 absent from go-edit; 4,455 are exactMatch.
   - The exact set is strictly one-to-one: 4,482 live GO terms, one Rhea reaction each.
     Directional Rhea ids are mapped to the master reaction.
   - A general MF (e.g. *oxidoreductase activity*) is not expanded to its descendants.
3. **Reaction → chemicals:** the ChEBI participants. Some participants are removed so that
   edges reflect pathway intermediates rather than shared cofactors:
   - currency metabolites: H2O, ATP/ADP, NAD(P)(H), CoA, SAM/SAH, glutamate/2-oxoglutarate, …
   - electron-carrier pools: quinones, cytochromes, ferredoxins
   - macromolecular residues: `-[protein]`, `[histone]`, tRNA, DNA/RNA
4. **Gene–gene edge:** an edge joins two genes when their reactions share a non-currency
   metabolite.
5. **BP alignment:** each gene's BP terms are propagated over is_a/part_of and restricted to
   descendants of *metabolic process*. A term annotated to ≤5% of the organism's enzymes
   counts as "specific". Three tests:
   - **Edge level:** do metabolically linked pairs share a specific BP more often than random pairs?
   - **Term level:** is each BP term's gene set connected (largest-connected-component
     fraction), compared with 200 random gene sets of the same size?
   - **Community level:** Louvain communities, each matched to its best BP term by F1.

Results for this source are in `results/<ORG>/reviews/`. Bulk UniProt/GOA sources are
compared below.

`trace_path.py ORG/SOURCE A B` prints the shortest metabolite→enzyme→metabolite route
between two chemicals.

### Reproduce

```bash
mkdir -p analysis/mf_metabolic_network/data && cd analysis/mf_metabolic_network/data
curl -o rhea.tsv "https://www.rhea-db.org/rhea/?query=*&columns=rhea-id,equation,chebi-id&format=tsv"
curl -o go-basic.obo https://current.geneontology.org/ontology/go-basic.obo
cd ../../..
# go-edit.obo, rhea-directions.tsv and the bulk UniProt/GOA files:
uv run python analysis/mf_metabolic_network/fetch_bulk.py PSEPK human
uv run python analysis/mf_metabolic_network/build_network.py PSEPK            # reviews
uv run python analysis/mf_metabolic_network/build_network.py PSEPK --source uniprot-rhea [--reviewed-genes-only]
uv run python analysis/mf_metabolic_network/compare_sources.py PSEPK human
```

The downloads (`data/`) are git-ignored. Results were regenerated on 2026-10-09, with
go-edit.obo from go-ontology master (commit 3df35ba).

## Results

| Metric | PSEPK | human | yeast | SCHPO | worm | ARATH |
|---|---:|---:|---:|---:|---:|---:|
| Reviews | 944 | 2183 | 224 | 149 | 212 | 138 |
| Enzymes with Rhea-mapped reviewed MF | 570 | 789 | 70 | 38 | 52 | 30 |
| Distinct Rhea reactions | 455 | 700 | 35 | 23 | 17 | 18 |
| Gene–gene metabolite edges | 1719 | 2858 | 26 | 1 | 0 | 1 |
| Giant component (genes) | 403 | 509 | 6 | 2 | 1 | 2 |
| Isolated enzymes | 113 | 248 | 57 | 36 | 52 | 28 |
| Linked pairs sharing a specific metabolic BP | 0.383 | 0.544 | 0.0 | 0.0 | 0.0 | 0.0 |
| …pairs sharing ≥2 intermediates | 0.77 | 0.788 | 0.0 | 0.0 | 0.0 | 0.0 |
| …random enzyme pairs | 0.045 | 0.064 | 0.04 | 0.057 | 0.033 | 0.02 |
| BP terms tested (≥3 enzymes) | 373 | 711 | 36 | 24 | 18 | 37 |
| BP terms more connected than random (p<0.05) | 285 | 530 | 0 | 0 | 0 | 15 |
| Louvain communities | 23 | 19 | 1 | 1 | 0 | 1 |
| Communities matching a BP term (F1≥0.5) | 15 | 12 | 0 | 1 | 0 | 1 |

Only *P. putida* KT2440 (near whole-metabolism coverage) and human have enough reviewed
enzymes to form a network. In the other organisms the reviewed genes are mostly
non-enzymes, so the numbers are not interpretable.

### The network does assemble

- In PSEPK, 403 of 570 enzymes fall into one connected component. When every step of a
  pathway has been reviewed, the textbook route comes out of MF annotations alone:

  ```
  benzoate -> [benC] -> 1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate -> [benD] -> catechol
    -> [catA] -> cis,cis-muconate -> [catB] -> (S)-muconolactone -> [catC] -> enol-lactone
    -> [pcaD] -> 3-oxoadipate -> [pcaJ] -> succinyl-CoA
  ```

  benA/benC (dioxygenase subunits) and pcaI/pcaJ (transferase subunits) are
  interchangeable on this path.
- Glucose to pyruvate comes out as the Entner–Doudoroff route (glk, zwf, pgl, edd, eda).
  That is the route *P. putida* actually uses, since it lacks phosphofructokinase.
- Louvain communities correspond to recognisable pathways:
  - P. putida: 15 of 23 communities match a BP term (F1 ≥ 0.5). Examples are the TCA
    cycle, benzoate catabolism, chorismate biosynthesis, fatty-acid biosynthesis,
    isopentenyl diphosphate biosynthesis (0.77) and L-leucine catabolism (0.89).
  - Human: 12 of 19 match. Examples are glucose 6-phosphate metabolism (0.72), purine
    salvage, bile-acid biosynthesis, saturated fatty-acid elongation (0.93) and
    polyamine metabolism (0.80).

### It agrees with BP, strongly but not completely

- Metabolically linked enzymes share a specific metabolic BP **8.5× more often than random
  pairs**: 38% vs 4.5% in PSEPK and 54% vs 6.4% in human. For pairs sharing at least two
  intermediates the figure rises to 77–79%.
- 76% (PSEPK) and 75% (human) of metabolic BP terms have gene sets that are significantly
  more connected than random.

### Where they disagree, and why

1. **Network artefacts.**
   - Generic Rhea participants ("a fatty acid", "an acyl-CoA", "a carboxylate"). For
     example, CLYBL is linked to BAAT, ACAA1/2, HADHB and SCP2 through "an acyl-CoA".
   - Generic NTPase reactions (human ABCE1–ALPL through "a ribonucleoside
     5'-triphosphate").
2. **Genuine cross-pathway links.** These are correct, but no shared BP is expected:
   - pcaIJ–sucCD through succinyl-CoA (β-ketoadipate feeding the TCA cycle).
   - PP_1451–soxABD through glycine.
3. **BP terms that are not one pathway.** Some fragmented terms are grab-bags or not
   chemical routes at all:
   - grab-bag metabolic terms: *vitamin biosynthetic process*, *non-proteinogenic amino
     acid metabolic process*;
   - pathways connected only through currency metabolites or polymers: *electron
     transport chain* on nuo/NDUF subunits, RNA modification enzymes under *RNA
     biosynthetic process*.

   Low connectivity here does **not** mean the BP is wrong.
4. **Gaps.** Unreviewed genes break chains, and so do reviewed MFs with no exact Rhea
   mapping. 248 human and 113 PSEPK enzymes are isolated nodes. These are candidates for
   missing MF specificity, or for GO terms that need an exact Rhea xref (see
   `projects/RHEA`).

### Limits

- **No direction or atom mapping.** Rhea master reactions are undirected, and edges ignore
  which atoms are carried. Shortest paths therefore cut through hubs and side activities:
  - human mevalonate→cholesterol runs via acetyl-CoA, glucosamine 6-phosphate and GBA1;
  - PSEPK lysine→glutarate runs via diaminopimelate and succinate.

  A true pathway reconstruction needs Rhea directional IDs (`rhea-directions.tsv`) plus
  atom mappings or a carbon-tracing constraint.
- **Hand-chosen settings.** The currency list is heuristic.
- **Exact-only costs coverage.** Dropping narrowMatch xrefs removes reactions as well as
  noise. Human reviewed enzymes map to 700 distinct reactions, against 1,184 when narrow
  xrefs were (wrongly) treated as exact. The same change raised agreement with BP. A
  reviewed MF whose only Rhea xref is a narrowMatch is an isolated node here.

## Would plain UniProt/GOA annotations work?

`fetch_bulk.py` gets a whole proteome with **one request per source** instead of
fetching gene by gene:

- **UniProt REST `stream` endpoint** (`uniprotkb/stream?query=organism_id:N&fields=accession,gene_primary,rhea,ec,go_f,go_p&format=tsv`).
  This returns the Rhea IDs from each entry's CATALYTIC ACTIVITY lines, plus GO MF and BP,
  for every entry. The GO columns carry no evidence codes.
- **GOA GAF files**, which do carry evidence codes:
  - `goa/proteomes/109.P_putida_KT2440.goa` for P. putida;
  - `goa/HUMAN/goa_human.gaf.gz` for human.
- The QuickGO `downloadSearch` endpoint, filtered by `taxonId` and `aspect`, also works
  as a bulk alternative.
- `rhea-directions.tsv` maps directional Rhea IDs (UniProt often cites the LR/RL forms)
  to the master reaction.

Human uses Swiss-Prot entries only (20,431). P. putida uses the whole proteome (5,529).

`build_network.py --source` choices:

| source | reactions from | BP from |
|---|---|---|
| `reviews` | reviewed MF → exact GO–Rhea xrefs | reviewed BP |
| `uniprot-rhea` | UniProt Rhea column (no GO in between) | GOA, all evidence |
| `goa-all` / `goa-noiea` / `goa-exp` | GOA MF → exact GO–Rhea xrefs | GOA BP, same evidence filter |

Add `--reviewed-genes-only` to restrict a bulk source to the genes that have a review.
That gives a like-for-like comparison with `reviews`.


#### PSEPK

| Metric | reviews | uniprot-rhea-reviewedset | goa-all-reviewedset | goa-exp-reviewedset | uniprot-rhea | goa-all | goa-noiea | goa-exp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Enzymes with reactions | 570 | 488 | 595 | 17 | 917 | 1355 | 29 | 22 |
| Distinct Rhea reactions | 455 | 477 | 505 | 20 | 843 | 891 | 33 | 26 |
| Edges | 1719 | 1368 | 2146 | 2 | 3545 | 7546 | 6 | 3 |
| Giant component | 403 | 354 | 440 | 2 | 569 | 889 | 5 | 2 |
| Isolated enzymes | 113 | 86 | 107 | 13 | 228 | 368 | 22 | 16 |
| Enzymes with no metabolic BP | 55 | 52 | 109 | 10 | 202 | 471 | 19 | 15 |
| Linked pairs sharing specific BP | 0.383 | 0.417 | 0.365 | 1.0 | 0.423 | 0.397 | 1.0 | 1.0 |
| …sharing ≥2 intermediates | 0.77 | 0.675 | 0.712 | 0.0 | 0.694 | 0.751 | 0.0 | 0.0 |
| …random pairs | 0.045 | 0.049 | 0.053 | 0.141 | 0.056 | 0.065 | 0.067 | 0.141 |
| BP terms tested | 373 | 344 | 352 | 8 | 485 | 523 | 11 | 8 |
| BP terms connected > random | 285 | 258 | 269 | 0 | 376 | 398 | 4 | 0 |
| Communities | 23 | 18 | 23 | 1 | 21 | 22 | 2 | 1 |
| Communities ≈ a BP term (F1≥0.5) | 15 | 11 | 11 | 1 | 8 | 7 | 2 | 1 |
| Enrichment over random | 8.5× | 8.5× | 6.9× | 7.1× | 7.6× | 6.1× | 14.9× | 7.1× |

#### human

| Metric | reviews | uniprot-rhea-reviewedset | goa-all-reviewedset | goa-exp-reviewedset | uniprot-rhea | goa-all | goa-noiea | goa-exp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Enzymes with reactions | 789 | 819 | 822 | 645 | 4140 | 3758 | 3270 | 2457 |
| Distinct Rhea reactions | 700 | 2302 | 754 | 613 | 6151 | 1593 | 1507 | 1365 |
| Edges | 2858 | 5223 | 3419 | 2316 | 109281 | 48550 | 40034 | 23397 |
| Giant component | 509 | 624 | 530 | 445 | 2623 | 2020 | 1893 | 1534 |
| Isolated enzymes | 248 | 176 | 258 | 160 | 1481 | 1665 | 1298 | 853 |
| Enzymes with no metabolic BP | 88 | 100 | 105 | 147 | 1258 | 993 | 860 | 827 |
| Linked pairs sharing specific BP | 0.544 | 0.458 | 0.521 | 0.479 | 0.436 | 0.468 | 0.467 | 0.456 |
| …sharing ≥2 intermediates | 0.788 | 0.56 | 0.735 | 0.709 | 0.583 | 0.7 | 0.71 | 0.645 |
| …random pairs | 0.064 | 0.07 | 0.066 | 0.071 | 0.076 | 0.071 | 0.076 | 0.077 |
| BP terms tested | 711 | 826 | 788 | 558 | 1415 | 1375 | 1262 | 939 |
| BP terms connected > random | 530 | 636 | 585 | 371 | 1047 | 1050 | 938 | 652 |
| Communities | 19 | 12 | 16 | 17 | 12 | 22 | 18 | 20 |
| Communities ≈ a BP term (F1≥0.5) | 12 | 8 | 9 | 8 | 2 | 9 | 7 | 3 |
| Enrichment over random | 8.5× | 6.5× | 7.9× | 6.7× | 5.7× | 6.6× | 6.1× | 5.9× |

### Findings

- **Yes, a network assembles from plain UniProt annotations.** It is bigger and less
  coherent than the one from reviewed annotations:
  - Human: whole Swiss-Prot gives a 2,623-gene giant component from the Rhea column
    (2,020 from GOA). Linked pairs share a specific BP 5.7–6.6× more often than random.
  - On the same genes, reviewed annotations agree best: 8.5× in both organisms, against
    6.9× (P. putida) and 7.9× (human) for GOA with all evidence. With reviewed
    annotations, 77–79% of strong edges (≥2 shared intermediates) share a BP, against
    71–74% for GOA.
  - Reviewed annotations also give the most BP-matching communities: 15/23 (P. putida)
    and 12/19 (human), against 11/23 and 9/16 for GOA on the same genes.
- **The UniProt Rhea column has the widest reaction coverage but the weakest BP
  agreement in human.** It needs no GO→Rhea step.
  - On the same 819 human enzymes it lists 2,302 reactions, against 700 from the
    reviews. Many of these are substrate-specific variants. Its BP agreement there is
    6.5×, and only 56% of strong edges share a BP.
  - In P. putida it matches the reviews (8.5× on the same genes).
  - Its coverage is mostly Swiss-Prot: 441 of 745 reviewed P. putida entries carry Rhea
    IDs, against 476 of 4,784 unreviewed ones. Most of the benzoate pathway (benA, benC,
    benD) is unreviewed TrEMBL with no CATALYTIC ACTIVITY line. As a result, the
    benzoate→succinyl-CoA route that the reviews reconstruct is broken in
    `uniprot-rhea`.
- **GOA MF with exact Rhea xrefs is a reasonable bulk source.** P. putida `goa-all` has
  1,355 enzymes, against 570 from the reviews. It reconstructs the benzoate→succinyl-CoA
  route through benD's ec2go term (GO:0047116 ≡ RHEA:11560). Its BP agreement (6.1×)
  is lower than the reviews'.
- **Narrow xrefs read as exact were the main source of spurious links.** For example,
  GO:0016616 *oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as
  acceptor* carries `xref: RHEA:25968 {source="skos:narrowMatch"}` (benzil reductase).
  - With the predicate dropped, every gene annotated to GO:0016616 became a benzil
    reductase. TreeGrafter annotates P. putida benD to that term (GO_REF:0000118,
    PANTHER:PTN002460465), and nine unrelated dehydrogenases were linked through
    benzil/(S)-benzoin.
  - Using exactMatch only removes this class of error without any term-specific filter.
- **Bacteria have almost no experimental GO.** Of 25,276 P. putida GOA rows, all but 195
  are IEA (GO_REF pipelines). `goa-exp` and `goa-noiea` keep only 22–29 enzymes, so for
  bacteria the choice is between curated reviews and electronic annotation. Their
  enrichment figures rest on 3–6 edges and are not meaningful. Human experimental-only
  still gives 2,457 enzymes with 5.9× enrichment.
- **Circularity caveat.** IEA MF and IEA BP often come from the same rule (UniRule/ARBA,
  EC2GO, InterPro2GO, TreeGrafter), so their agreement is partly built in. The
  `-reviewedset` and `goa-exp` columns are the fairer comparisons.

## Outputs (`results/<ORG>/<source>/`)

`summary.json`, `edges.tsv`, `gene_reactions.tsv`, `bp_term_coherence.tsv` (per-term
connectivity, p-value, isolated genes), `communities.tsv`, `discordant_edges.tsv` (linked
pairs with no shared metabolic BP), `graph.json` (for visualisation). Whole-proteome
`edges.tsv`/`graph.json` are git-ignored (large, regenerable).
