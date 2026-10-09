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
2. **MF → reaction:** GO column of the Rhea reaction TSV. This is the same content as
   rhea2go, which is generated from the `xref: RHEA:` lines on GO terms. Those xrefs carry
   no mapping predicate, so they are not guaranteed to be exact. Two filters reduce that:
   - GO terms with an incomplete-EC xref (e.g. `EC:1.1.1.-`) are grouping classes, and
     their Rhea xrefs are ignored. Four terms are affected: GO:0016616, GO:0016712,
     GO:0004713 and GO:0008241.
   - A general MF (e.g. *oxidoreductase activity*) is not expanded to its descendants.
   When one GO term maps to more than 5 Rhea reactions (a class reaction plus substrate
   examples, e.g. *acyl-CoA hydrolase activity*), only the generic class reactions are kept.
   Otherwise a broad hydrolase gets linked to every acyl-CoA in the cell.
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

`trace_path.py ORG/SOURCE A B` prints the shortest metabolite→enzyme→metabolite route between
two chemicals.

### Reproduce

```bash
mkdir -p analysis/mf_metabolic_network/data && cd analysis/mf_metabolic_network/data
curl -o rhea.tsv "https://www.rhea-db.org/rhea/?query=*&columns=rhea-id,equation,chebi-id,go&format=tsv"
curl -o go-basic.obo https://current.geneontology.org/ontology/go-basic.obo
cd ../../.. && uv run python analysis/mf_metabolic_network/build_network.py PSEPK
# bulk UniProt/GOA sources (see below)
uv run python analysis/mf_metabolic_network/fetch_bulk.py PSEPK human
uv run python analysis/mf_metabolic_network/build_network.py PSEPK --source uniprot-rhea [--reviewed-genes-only]
uv run python analysis/mf_metabolic_network/compare_sources.py PSEPK human
```

The downloads (`data/`) are git-ignored. Results were regenerated on 2026-10-09.

## Results

| Metric | PSEPK | human | yeast | SCHPO | worm | ARATH |
|---|---:|---:|---:|---:|---:|---:|
| Reviews | 944 | 2183 | 224 | 149 | 212 | 138 |
| Enzymes with Rhea-mapped reviewed MF | 591 | 794 | 75 | 40 | 50 | 31 |
| Distinct Rhea reactions | 577 | 1184 | 53 | 43 | 35 | 28 |
| Gene–gene metabolite edges | 1973 | 3630 | 27 | 1 | 0 | 1 |
| Giant component (genes) | 433 | 559 | 6 | 2 | 1 | 2 |
| Isolated enzymes | 107 | 211 | 60 | 38 | 50 | 29 |
| Linked pairs sharing a specific metabolic BP | 0.36 | 0.521 | 0.1 | 0.0 | 0.0 | 0.0 |
| …pairs sharing ≥2 intermediates | 0.701 | 0.729 | 0.333 | 0.0 | 0.0 | 0.0 |
| …random enzyme pairs | 0.041 | 0.066 | 0.034 | 0.053 | 0.033 | 0.02 |
| BP terms tested (≥3 enzymes) | 388 | 735 | 39 | 26 | 18 | 37 |
| BP terms more connected than random (p<0.05) | 302 | 570 | 3 | 0 | 0 | 15 |
| Louvain communities | 20 | 15 | 1 | 1 | 0 | 1 |
| Communities matching a BP term (F1≥0.5) | 10 | 10 | 0 | 1 | 0 | 1 |

Only *P. putida* KT2440 (near whole-metabolism coverage) and human have enough reviewed
enzymes to form a network. In the other organisms the reviewed genes are mostly
non-enzymes, so the numbers are not interpretable.

### The network does assemble

- In PSEPK, 433 of 591 enzymes fall into one connected component. When every step of a
  pathway has been reviewed, the textbook route comes out of MF annotations alone:

  ```
  benzoate -> [benC] -> 1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate -> [benD] -> catechol
    -> [catA] -> cis,cis-muconate -> [catB] -> (S)-muconolactone -> [catC] -> enol-lactone
    -> [pcaD] -> 3-oxoadipate -> [pcaJ] -> succinyl-CoA
  ```

  benA/benC (dioxygenase subunits) and pcaI/pcaJ (transferase subunits) are
  interchangeable on this path.
- Louvain communities correspond to recognisable pathways:
  - P. putida: benzoate catabolism (F1 0.57), chorismate biosynthesis (0.69), isoprenoid
    metabolism (0.70), glyoxylate metabolism (0.71), fatty-acid biosynthesis (0.62),
    L-leucine catabolism (0.89).
  - Human: N-linked glycosylation (0.79), ceramide metabolism (0.68), steroid metabolism
    (0.63), polyamine metabolism (0.83).

### It agrees with BP, strongly but not completely

- Metabolically linked enzymes share a specific metabolic BP **8–9× more often than random
  pairs**: 36% vs 4% in PSEPK and 52% vs 6.6% in human. For pairs sharing at least two
  intermediates the figure rises to 70–73%.
- 78% (PSEPK) and 78% (human) of metabolic BP terms have gene sets that are significantly
  more connected than random.

### Where they disagree, and why

1. **Network artefacts.** These are the commonest cause:
   - Generic Rhea participants ("a fatty acid", "an acyl-CoA", "a carboxylate").
   - Non-exact GO→Rhea xrefs. Before the grouping-term filter, the GO:0016616 →
     RHEA:25968 (benzil reductase) xref linked nine unrelated PSEPK dehydrogenases through
     benzil/(S)-benzoin. With the filter, no PSEPK gene in the reviews network has a benzil
     reaction.
   - Generic NTPase reactions (human ABCE1–ALPL).
2. **Genuine cross-pathway links.** These are correct, but no shared BP is expected:
   - pcaIJ–sucCD through succinyl-CoA (β-ketoadipate feeding the TCA cycle).
   - soxABD–thiO through sarcosine/glycine.
   - AADAC–ASMT through melatonin/N-acetylserotonin.
3. **BP terms that are not one pathway.** Some fragmented terms are grab-bags or not
   chemical routes at all:
   - grab-bag metabolic terms: *non-proteinogenic amino acid biosynthesis*, *vitamin
     biosynthetic process*;
   - pathways connected only through currency metabolites or polymers: OXPHOS / *ATP
     biosynthetic process* on NDUF* subunits, RNA modification enzymes under *RNA
     biosynthetic process*.

   Low connectivity here does **not** mean the BP is wrong.
4. **Gaps.** Unreviewed genes, and reviewed MFs with no Rhea mapping, break chains. 211
   human and 107 PSEPK enzymes are isolated nodes. These are candidates for missing MF
   specificity, or for terms that need a rhea2go mapping (see `projects/RHEA`).

### Limits

- **No direction or atom mapping.** Rhea master reactions are undirected, and edges ignore
  which atoms are carried. Shortest paths therefore cut through hubs and side activities:
  human mevalonate→cholesterol runs via "a fatty acid", and PSEPK lysine→glutarate runs
  via alanine racemase. A true pathway reconstruction needs Rhea directional IDs
  (`rhea-directions.tsv`) plus atom mappings or a carbon-tracing constraint.
- **Hand-chosen settings.** The currency list, the grouping-term filter and the
  >5-reaction trimming threshold are heuristic. Results shift by a few points when they change, but the roughly 8–9× enrichment holds.

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
| `reviews` | reviewed MF → rhea2go | reviewed BP |
| `uniprot-rhea` | UniProt Rhea column (no GO in between) | GOA, all evidence |
| `goa-all` / `goa-noiea` / `goa-exp` | GOA MF → rhea2go | GOA BP, same evidence filter |

Add `--reviewed-genes-only` to restrict a bulk source to the genes that have a review.
That gives a like-for-like comparison with `reviews`.

#### PSEPK

| Metric | reviews | uniprot-rhea-reviewedset | goa-all-reviewedset | goa-exp-reviewedset | uniprot-rhea | goa-all | goa-noiea | goa-exp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Enzymes with reactions | 591 | 488 | 614 | 19 | 917 | 1403 | 31 | 24 |
| Distinct Rhea reactions | 577 | 477 | 650 | 31 | 843 | 1207 | 59 | 48 |
| Edges | 1973 | 1368 | 2457 | 5 | 3545 | 9215 | 12 | 6 |
| Giant component | 433 | 354 | 465 | 4 | 569 | 965 | 6 | 4 |
| Isolated enzymes | 107 | 86 | 99 | 11 | 228 | 348 | 18 | 14 |
| Enzymes with no metabolic BP | 58 | 52 | 113 | 10 | 202 | 496 | 19 | 15 |
| Linked pairs sharing specific BP | 0.36 | 0.417 | 0.348 | 0.333 | 0.423 | 0.373 | 0.5 | 0.333 |
| …sharing ≥2 intermediates | 0.701 | 0.675 | 0.694 | 0.0 | 0.694 | 0.74 | 0.0 | 0.0 |
| …random pairs | 0.041 | 0.049 | 0.055 | 0.054 | 0.056 | 0.069 | 0.064 | 0.054 |
| BP terms tested | 388 | 344 | 360 | 14 | 485 | 528 | 11 | 14 |
| BP terms connected > random | 302 | 263 | 269 | 0 | 376 | 413 | 0 | 0 |
| Communities | 20 | 18 | 17 | 2 | 21 | 24 | 2 | 2 |
| Communities ≈ a BP term (F1≥0.5) | 10 | 11 | 7 | 1 | 8 | 8 | 2 | 1 |
| Enrichment over random | 8.8× | 8.5× | 6.3× | 6.2× | 7.6× | 5.4× | 7.8× | 6.2× |

#### human

| Metric | reviews | uniprot-rhea-reviewedset | goa-all-reviewedset | goa-exp-reviewedset | uniprot-rhea | goa-all | goa-noiea | goa-exp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Enzymes with reactions | 794 | 819 | 827 | 671 | 4140 | 3898 | 3420 | 2586 |
| Distinct Rhea reactions | 1184 | 2302 | 1301 | 1019 | 6151 | 2523 | 2360 | 2159 |
| Edges | 3630 | 5223 | 4376 | 2887 | 109281 | 75663 | 60580 | 34323 |
| Giant component | 559 | 624 | 583 | 498 | 2623 | 2219 | 2085 | 1705 |
| Isolated enzymes | 211 | 176 | 218 | 138 | 1481 | 1608 | 1262 | 823 |
| Enzymes with no metabolic BP | 71 | 100 | 88 | 149 | 1258 | 1030 | 910 | 887 |
| Linked pairs sharing specific BP | 0.521 | 0.458 | 0.496 | 0.46 | 0.436 | 0.417 | 0.429 | 0.449 |
| …sharing ≥2 intermediates | 0.729 | 0.56 | 0.668 | 0.643 | 0.583 | 0.608 | 0.626 | 0.627 |
| …random pairs | 0.066 | 0.07 | 0.068 | 0.075 | 0.076 | 0.074 | 0.077 | 0.079 |
| BP terms tested | 735 | 826 | 818 | 577 | 1415 | 1415 | 1309 | 983 |
| BP terms connected > random | 570 | 629 | 620 | 419 | 1044 | 1055 | 955 | 692 |
| Communities | 15 | 12 | 12 | 15 | 12 | 12 | 12 | 15 |
| Communities ≈ a BP term (F1≥0.5) | 10 | 8 | 7 | 5 | 2 | 3 | 2 | 1 |
| Enrichment over random | 7.9× | 6.5× | 7.3× | 6.1× | 5.7× | 5.6× | 5.6× | 5.7× |

### Findings

- **Yes, a network assembles from plain UniProt annotations.** It is bigger and noisier
  than the one from reviewed annotations:
  - Human: whole Swiss-Prot gives a 2,623-gene giant component from the Rhea column
    (2,219 from GOA). Linked pairs share a specific BP 5.6–5.7× more often than random.
  - On the same genes, reviewed annotations give the sharpest agreement: 8.8× (P. putida)
    and 7.9× (human), against 6.3× and 7.3× for GOA (all evidence). Strong edges
    (≥2 shared intermediates) share a BP 70–73% of the time with reviewed annotations.
    In human, GOA on the same genes reaches 67%.
- **The UniProt Rhea column is the more specific bulk source.** It comes from each entry's
  CATALYTIC ACTIVITY lines, so no GO→Rhea xref is involved.
  - In P. putida it scores close to the reviews on the same genes (8.5× enrichment,
    11 BP-matching communities).
  - It is more reaction-specific. Human UniProt lists 2,302 reactions for the 819
    reviewed enzymes, against 1,184 from the reviews.
  - Its coverage is mostly Swiss-Prot: 441 of 745 reviewed P. putida entries carry Rhea
    IDs, against 476 of 4,784 unreviewed ones. Most of the benzoate pathway (benA, benC,
    benD) is unreviewed TrEMBL with no CATALYTIC ACTIVITY line. As a result, the
    benzoate→succinyl-CoA route that the reviews reconstruct is broken in `uniprot-rhea`.
- **GO MF→Rhea over IEA annotations gains coverage.** P. putida `goa-all` has 1,403
  enzymes, against 591 from the reviews, and the benzoate→succinyl-CoA route
  reconstructs correctly through benD's ec2go term (GO:0047116 → RHEA:11560). The cost is
  weaker BP agreement: 5.4× enrichment, with 8 of 24 communities matching a BP term.
- **Non-exact GO→Rhea xrefs are a real hazard.** The rhea2go file states every row as a
  plain mapping, but xrefs on grouping terms are at best broad. Before the grouping-term
  filter was added, one such xref drove the P. putida benD example:
  - GO:0016616 *oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP
    as acceptor* has `xref: EC:1.1.1.-` and `xref: RHEA:25968` (benzil reductase) in GO.
  - TreeGrafter (GO_REF:0000118, PANTHER:PTN002460465) annotates benD to GO:0016616.
  - Read as exact, that xref made benD a benzil reductase. The benzoate route then
    detoured through (S)-benzoin.
  - benD's IEA BP, *fatty acid elongation* (GO:0030497), comes from the same TreeGrafter
    node. The review says *benzoate catabolic process*.
  - The incomplete-EC filter catches only 4 terms. Many-to-one xrefs, where one GO term
    has dozens of substrate-example Rhea reactions (e.g. *carbonyl reductase (NADPH)
    activity*), are handled by the >5-reaction trimming instead. An SSSOM GO–Rhea mapping
    with explicit exact/broad/narrow predicates would replace both heuristics.
- **Bacteria have almost no experimental GO.** Of 25,276 P. putida GOA rows, all but 195
  are IEA (GO_REF pipelines). `goa-exp` and `goa-noiea` keep only 24–31 enzymes, so for
  bacteria the choice is between curated reviews and electronic annotation. Human
  experimental-only still gives 2,586 enzymes with 5.7× enrichment.
- **Circularity caveat.** IEA MF and IEA BP often come from the same rule (UniRule/ARBA,
  EC2GO, InterPro2GO, TreeGrafter), so their agreement is partly built in. The
  `-reviewedset` and `goa-exp` columns are the fairer comparisons.

## Outputs (`results/<ORG>/<source>/`)

`summary.json`, `edges.tsv`, `gene_reactions.tsv`, `bp_term_coherence.tsv` (per-term
connectivity, p-value, isolated genes), `communities.tsv`, `discordant_edges.tsv` (linked
pairs with no shared metabolic BP), `graph.json` (for visualisation).
