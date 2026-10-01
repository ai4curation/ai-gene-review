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
2. **MF → reaction:** GO column of the Rhea reaction TSV (= rhea2go). Exact mappings only.
   A general MF (e.g. *oxidoreductase activity*) is not expanded to its descendants.
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

The downloads (`data/`) are git-ignored. Results were generated on 2026-10-01.

## Results

| Metric | PSEPK | human | yeast | SCHPO | worm | ARATH |
|---|---:|---:|---:|---:|---:|---:|
| Reviews | 942 | 2184 | 224 | 149 | 212 | 137 |
| Enzymes with Rhea-mapped reviewed MF | 593 | 805 | 76 | 42 | 51 | 31 |
| Distinct Rhea reactions | 578 | 1187 | 55 | 45 | 36 | 29 |
| Gene–gene metabolite edges | 1981 | 3693 | 27 | 1 | 0 | 1 |
| Giant component (genes) | 436 | 565 | 6 | 2 | 1 | 2 |
| Isolated enzymes | 106 | 220 | 61 | 40 | 51 | 29 |
| Linked pairs sharing a specific metabolic BP | 0.356 | 0.524 | 0.1 | 0.0 | 0.0 | 0.0 |
| …pairs sharing ≥2 intermediates | 0.67 | 0.725 | 0.333 | 0.0 | 0.0 | 0.0 |
| …random enzyme pairs | 0.041 | 0.065 | 0.031 | 0.051 | 0.034 | 0.02 |
| BP terms tested (≥3 enzymes) | 389 | 739 | 39 | 26 | 18 | 37 |
| BP terms more connected than random (p<0.05) | 306 | 567 | 3 | 0 | 0 | 15 |
| Louvain communities | 20 | 14 | 1 | 1 | 0 | 1 |
| Communities matching a BP term (F1≥0.5) | 10 | 6 | 0 | 1 | 0 | 1 |

Only *P. putida* KT2440 (near whole-metabolism coverage) and human have enough reviewed
enzymes to form a network. In the other organisms the reviewed genes are mostly
non-enzymes, so the numbers are not interpretable.

### The network does assemble

- In PSEPK, 436 of 593 enzymes fall into one connected component. When every step of a
  pathway has been reviewed, the textbook route comes out of MF annotations alone:

  ```
  benzoate -> [benA] -> 1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate -> [benD] -> catechol
    -> [catA] -> cis,cis-muconate -> [catB] -> (S)-muconolactone -> [catC] -> enol-lactone
    -> [pcaD] -> 3-oxoadipate -> [pcaI] -> succinyl-CoA
  ```
- Louvain communities correspond to recognisable pathways: β-ketoadipate/benzoate (F1 0.57),
  chorismate biosynthesis (0.67), ubiquinone (0.82), fatty-acid synthesis (0.57),
  gluconate (1.0), and in human N-glycosylation (0.79), fatty-acid elongation (0.90) and
  β-oxidation (0.67).

### It agrees with BP, strongly but not completely

- Metabolically linked enzymes share a specific metabolic BP **8–9× more often than random
  pairs**: 36% vs 4% in PSEPK and 52% vs 6.5% in human. For pairs sharing at least two
  intermediates the figure rises to 67–73%.
- 79% (PSEPK) and 77% (human) of metabolic BP terms have gene sets that are significantly
  more connected than random.

### Where they disagree, and why

1. **Network artefacts.** These are the commonest cause:
   - Generic Rhea participants ("a fatty acid", "an acyl-CoA", "a carboxylate").
   - Promiscuous or side reactions listed under a GO term. For example, *carbonyl reductase
     (NADPH) activity* maps to the benzil/benzoin reactions, which links five unrelated
     PSEPK dehydrogenases.
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
4. **Gaps.** Unreviewed genes, and reviewed MFs with no Rhea mapping, break chains. 220
   human and 106 PSEPK enzymes are isolated nodes. These are candidates for missing MF
   specificity, or for terms that need a rhea2go mapping (see `projects/RHEA`).

### Limits

- **No direction or atom mapping.** Rhea master reactions are undirected, and edges ignore
  which atoms are carried. Shortest paths therefore cut through hubs and side activities:
  human mevalonate→cholesterol runs via "a fatty acid", and PSEPK lysine→glutarate runs
  via alanine racemase. A true pathway reconstruction needs Rhea directional IDs
  (`rhea-directions.tsv`) plus atom mappings or a carbon-tracing constraint.
- **Hand-chosen settings.** The currency list and the >5-reaction trimming threshold are
  heuristic. Results shift by a few points when they change, but the 8–9× enrichment holds.

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
| Enzymes with reactions | 595 | 488 | 615 | 19 | 917 | 1416 | 31 | 24 |
| Distinct Rhea reactions | 578 | 477 | 652 | 31 | 843 | 1210 | 59 | 48 |
| Edges | 2008 | 1368 | 2726 | 5 | 3545 | 10401 | 12 | 6 |
| Giant component | 438 | 354 | 469 | 4 | 569 | 982 | 6 | 4 |
| Isolated enzymes | 106 | 86 | 96 | 11 | 228 | 348 | 18 | 14 |
| Enzymes with no metabolic BP | 61 | 52 | 114 | 10 | 202 | 506 | 19 | 15 |
| Linked pairs sharing specific BP | 0.359 | 0.417 | 0.332 | 0.333 | 0.423 | 0.362 | 0.5 | 0.333 |
| …sharing ≥2 intermediates | 0.678 | 0.675 | 0.489 | 0.0 | 0.694 | 0.59 | 0.0 | 0.0 |
| …random pairs | 0.041 | 0.049 | 0.055 | 0.054 | 0.056 | 0.068 | 0.064 | 0.054 |
| BP terms tested | 388 | 344 | 360 | 14 | 485 | 528 | 11 | 14 |
| BP terms connected > random | 302 | 263 | 271 | 0 | 377 | 405 | 0 | 0 |
| Communities | 21 | 18 | 17 | 2 | 21 | 19 | 2 | 2 |
| Communities ≈ a BP term (F1≥0.5) | 10 | 11 | 4 | 1 | 8 | 2 | 2 | 1 |
| Enrichment over random | 8.8× | 8.5× | 6.0× | 6.2× | 7.6× | 5.3× | 7.8× | 6.2× |

#### human

| Metric | reviews | uniprot-rhea-reviewedset | goa-all-reviewedset | goa-exp-reviewedset | uniprot-rhea | goa-all | goa-noiea | goa-exp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Enzymes with reactions | 804 | 819 | 837 | 679 | 4140 | 3993 | 3502 | 2647 |
| Distinct Rhea reactions | 1187 | 2302 | 1304 | 1021 | 6151 | 2528 | 2365 | 2164 |
| Edges | 3654 | 5223 | 4603 | 2887 | 109281 | 79038 | 62053 | 34786 |
| Giant component | 564 | 624 | 589 | 498 | 2623 | 2232 | 2095 | 1711 |
| Isolated enzymes | 220 | 176 | 226 | 146 | 1481 | 1690 | 1334 | 878 |
| Enzymes with no metabolic BP | 74 | 100 | 93 | 153 | 1258 | 1059 | 930 | 908 |
| Linked pairs sharing specific BP | 0.52 | 0.458 | 0.478 | 0.46 | 0.436 | 0.415 | 0.435 | 0.45 |
| …sharing ≥2 intermediates | 0.722 | 0.56 | 0.598 | 0.643 | 0.583 | 0.594 | 0.634 | 0.632 |
| …random pairs | 0.061 | 0.07 | 0.069 | 0.065 | 0.076 | 0.071 | 0.075 | 0.078 |
| BP terms tested | 737 | 826 | 819 | 578 | 1415 | 1426 | 1316 | 983 |
| BP terms connected > random | 568 | 629 | 615 | 420 | 1046 | 1064 | 953 | 693 |
| Communities | 14 | 12 | 13 | 15 | 12 | 12 | 11 | 15 |
| Communities ≈ a BP term (F1≥0.5) | 6 | 8 | 7 | 5 | 2 | 5 | 3 | 2 |
| Enrichment over random | 8.5× | 6.5× | 6.9× | 7.1× | 5.7× | 5.8× | 5.8× | 5.8× |


### Findings

- **Yes, a network assembles from plain UniProt annotations.** It is bigger and noisier
  than the one from reviewed annotations:
  - Human: whole Swiss-Prot gives a 2,623-gene giant component from the Rhea column
    (2,232 from GOA). Linked pairs share a specific BP 5.7–5.8× more often than random.
  - On the same genes, reviewed annotations give the sharpest agreement: 8.8× (P. putida)
    and 8.5× (human), against 6.0–6.9× for GOA. Strong edges (≥2 shared intermediates)
    share a BP 72% of the time with reviewed annotations, against 56–64% with GOA.
- **The UniProt Rhea column beats GO→rhea2go as a bulk source.**
  - It skips the GO-term breadth problem: a broad oxidoreductase term no longer pulls in
    benzil reductase.
  - In P. putida it scores close to the reviews on the same genes (8.5× enrichment,
    11 BP-matching communities).
  - It is more reaction-specific. Human UniProt lists 2,302 reactions for the 819
    reviewed enzymes, against 1,187 from the reviews.
  - Its coverage is mostly Swiss-Prot: 441 of 745 reviewed P. putida entries carry Rhea
    IDs, against 476 of 4,784 unreviewed ones. Most of the benzoate pathway (benA, benC,
    benD) is unreviewed TrEMBL with no CATALYTIC ACTIVITY line. As a result, the
    benzoate→succinyl-CoA route that the reviews reconstruct is broken in `uniprot-rhea`.
- **GO MF→rhea2go over IEA annotations adds coverage and nonsense together.** P. putida
  `goa-all` has 1,416 enzymes, but only 2 of its 19 communities match a BP term.
  - Its benzoate→succinyl-CoA path runs benzoate → [benC] → diol → [benD] → *(S)-benzoin* →
    [paaH] → "a 3-oxoacyl-CoA" → [yqeF] → succinyl-CoA.
  - That happens because benD's IEA MF is a broad oxidoreductase class that maps to the
    benzil reaction. Its IEA BP is *fatty acid biosynthetic process*; the review says
    *benzoate catabolic process*.
- **Bacteria have almost no experimental GO.** Of 25,276 P. putida GOA rows, all but 195
  are IEA (GO_REF pipelines). `goa-exp` and `goa-noiea` keep only 24–31 enzymes, so for
  bacteria the choice is between curated reviews and electronic annotation. Human
  experimental-only still gives 2,647 enzymes with 5.8× enrichment.
- **Circularity caveat.** IEA MF and IEA BP often come from the same rule (UniRule/ARBA,
  EC2GO, InterPro2GO), so their agreement is partly built in. The `-reviewedset` and
  `goa-exp` columns are the fairer comparisons.

## Outputs (`results/<ORG>/<source>/`)

`summary.json`, `edges.tsv`, `gene_reactions.tsv`, `bp_term_coherence.tsv` (per-term
connectivity, p-value, isolated genes), `communities.tsv`, `discordant_edges.tsv` (linked
pairs with no shared metabolic BP), `graph.json` (for visualisation).
