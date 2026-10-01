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

`trace_path.py ORG A B` prints the shortest metabolite→enzyme→metabolite route between
two chemicals.

### Reproduce

```bash
mkdir -p analysis/mf_metabolic_network/data && cd analysis/mf_metabolic_network/data
curl -o rhea.tsv "https://www.rhea-db.org/rhea/?query=*&columns=rhea-id,equation,chebi-id,go&format=tsv"
curl -o go-basic.obo https://current.geneontology.org/ontology/go-basic.obo
cd ../../.. && uv run python analysis/mf_metabolic_network/build_network.py PSEPK
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

## Outputs (`results/<ORG>/`)

`summary.json`, `edges.tsv`, `gene_reactions.tsv`, `bp_term_coherence.tsv` (per-term
connectivity, p-value, isolated genes), `communities.tsv`, `discordant_edges.tsv` (linked
pairs with no shared metabolic BP), `graph.json` (for visualisation).
