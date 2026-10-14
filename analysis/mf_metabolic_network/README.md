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

   Names come from the Rhea equations, with Rhea's `chebiId_name.tsv` as a fallback.
   The fallback matters for ions that only occur in transport reactions, such as
   "K(+)(out) = K(+)(in)": without it, K⁺ and Na⁺ escaped the filter and linked every
   transporter. That alone removed a third of the human whole-proteome UniProt links.
4. **Gene–gene edge:** an edge joins two genes when their reactions share a non-currency
   metabolite. Edges are split into two kinds:
   - **same-step:** the two genes share a Rhea reaction (complex subunits, isozymes,
     paralogs). They are not a handoff.
   - **handoff:** no shared reaction. A pathway handoff is a *single* intermediate
     passing from one enzyme to the next, so the number of shared chemicals is not a
     confidence measure. Pairs sharing two or more chemicals are mostly same-step: 103 of
     151 in P. putida and 303 of 613 in human.
   - A **non-hub handoff** goes through a chemical that at most 5 enzymes touch.
     Hub intermediates such as pyruvate and acetyl-CoA link many unrelated pathways.
5. **BP alignment:** each gene's BP terms are propagated over is_a/part_of and restricted to
   descendants of *metabolic process*. A term annotated to ≤5% of the organism's enzymes
   counts as "specific". Three tests:
   - **Edge level:** do metabolically linked pairs share a specific BP more often than random pairs?
   - **Term level:** is each BP term's gene set connected (largest-connected-component
     fraction), compared with 200 random gene sets of the same size?
   - **Community level:** Louvain communities, each matched to its best BP term by F1.

Results for this source are in `results/<ORG>/reviews/`. Bulk UniProt/GOA sources are
compared below.

### Viewer (`viewer.html`)

An interactive page for the reviews network, at
`analysis/mf_metabolic_network/viewer.html`. It is not deployed to the GitHub Pages
site, which does not stage `analysis/`. It fetches `results/<ORG>/reviews/graph.json` and embeds no data. Browsers block fetch()
from `file://`, so locally run `python -m http.server` in this folder.

- Pick a BP term to highlight its enzymes and zoom to them. A banner gives the term's
  connectivity against random gene sets of the same size, from `bp_term_coherence.tsv`.
- Pick a Louvain cluster to see its best-matching BP term, or search for a gene.
- Line styles show the edge kind: non-hub handoff (solid), same step (dashed), hub-only
  handoff (faint, hidden unless both ends are highlighted).
- Hover a node for its reactions and BP terms, or a link for the shared chemicals. A
  table view lists the highlighted genes.

`trace_path.py ORG/SOURCE A B` prints the shortest metabolite→enzyme→metabolite route
between two chemicals.

### Reproduce

```bash
mkdir -p analysis/mf_metabolic_network/data && cd analysis/mf_metabolic_network/data
curl -o rhea.tsv "https://www.rhea-db.org/rhea/?query=*&columns=rhea-id,equation,chebi-id&format=tsv"
curl -o go-basic.obo https://current.geneontology.org/ontology/go-basic.obo
cd ../../..
# go-edit.obo, rhea-directions.tsv and the bulk UniProt/GOA files:
uv run --package mf-metabolic-network python analysis/mf_metabolic_network/fetch_bulk.py PSEPK human
uv run --package mf-metabolic-network python analysis/mf_metabolic_network/build_network.py PSEPK            # reviews
uv run --package mf-metabolic-network python analysis/mf_metabolic_network/build_network.py PSEPK --source uniprot-rhea [--reviewed-genes-only]
uv run --package mf-metabolic-network python analysis/mf_metabolic_network/compare_sources.py PSEPK human
```

The downloads (`data/`) are git-ignored. Results were regenerated on 2026-10-14 from the gene reviews on `main` at that
date (2,937 human, 952 P. putida), with
go-edit.obo pinned to go-ontology commit 3df35ba (`GO_EDIT_COMMIT`; saved as
`data/go-edit-3df35ba.obo`, so a copy from another commit is never reused).
The folder is a uv workspace member (`pyproject.toml` declares networkx and pyyaml).
Results are deterministic. Term-level p-values follow `--seed` (default 42). Every set
that feeds an ordering (edge insertion, and so the Louvain partition; hub-chemical
ranking) is iterated in sorted order, so the output does not depend on Python's
per-process hash seed. When BP terms tie on F1 for a community, the most specific is
reported (a tied term that is an ancestor of another tied term is dropped), then the
lowest GO id among siblings. The permutation p-value floor is 1/201 ≈ 0.005 with the
default `--n-random 200`. Reviews that use obsolete GO terms are reported as a warning
and counted in `summary.json` (`obsolete_terms_ignored`: 80 human gene–term pairs). An
obsolete term has no parents, so it contributes nothing to the BP sets.

## Results

| Metric | PSEPK | human | yeast | SCHPO | worm | ARATH |
|---|---:|---:|---:|---:|---:|---:|
| Reviews | 952 | 2937 | 406 | 192 | 347 | 265 |
| Enzymes with Rhea-mapped reviewed MF | 578 | 895 | 222 | 71 | 93 | 70 |
| Distinct Rhea reactions | 463 | 732 | 184 | 63 | 33 | 43 |
| Gene–gene metabolite edges | 1738 | 3135 | 426 | 43 | 47 | 27 |
| Giant component (genes) | 411 | 528 | 134 | 11 | 9 | 8 |
| Isolated enzymes | 120 | 336 | 75 | 44 | 76 | 41 |
| Linked pairs sharing a specific metabolic BP | 0.39 | 0.543 | 0.536 | 0.118 | 0.093 | 0.222 |
| …same-step pairs (shared reaction) | 0.958 | 0.93 | 0.854 | 0.2 | 0.051 | 0.333 |
| …handoff pairs (no shared reaction) | 0.344 | 0.495 | 0.491 | 0.103 | 0.5 | 0.167 |
| …handoffs via a non-hub chemical | 0.653 | 0.712 | 0.779 | 0.077 | 0.5 | 0.167 |
| …random enzyme pairs | 0.044 | 0.071 | 0.05 | 0.019 | 0.03 | 0.018 |
| "Specific" BP cutoff (≤5% of enzymes) | 28 | 44 | 11 | 3 | 4 | 3 |
| BP terms tested (≥3 enzymes, up to the size limit below) | 384 | 742 | 214 | 63 | 55 | 67 |
| …upper size limit (enzymes) | 112 | 176 | 44 | 12 | 16 | 12 |
| BP terms more connected than random (p<0.05) | 301 | 563 | 144 | 39 | 33 | 36 |
| …significant after Benjamini–Hochberg (FDR 0.05) | 292 | 544 | 138 | 39 | 33 | 29 |
| BP terms whose label names a currency chemical | 12 | 38 | 0 | 0 | 0 | 0 |
| Louvain communities | 22 | 19 | 14 | 3 | 1 | 3 |
| Communities matching a BP term (F1≥0.5) | 14 | 10 | 11 | 3 | 1 | 2 |

*P. putida* KT2440 (near whole-metabolism coverage) and human are analysed in detail
below. Yeast now has enough reviewed enzymes (222) for a network of its own. It shows
the same pattern: linked pairs share a specific BP 10.7× more often than random, non-hub
handoffs 78% of the time, and 11 of its 14 communities match a BP term. Fission yeast,
worm and Arabidopsis have under 100 mapped enzymes each and small networks (≤ 47
edges), so their figures rest on few links.

In these small organisms the edge-level fractions are also biased, in a known direction.
The "specific" cutoff (≤5% of mapped enzymes: 4 in worm, 3 in fission yeast and
Arabidopsis) falls below the size of an ordinary paralog family. A same-step clique
whose genes all share one correct BP term then scores as disagreement. Worm's same-step
figure (0.051, against 0.5 for handoffs) comes almost entirely from one clique:
daf-11, odr-1 and seven *gcy* guanylate cyclases. They all carry *cGMP biosynthetic
process*, but that term covers 9 enzymes, so none of the 36 pairs counts as sharing a
specific BP. The term- and community-level tests rate the same genes as ideal:
*cGMP biosynthetic process* is fully connected (p = 0.005), and worm's one community
is exactly these 9 genes and is labelled *cGMP biosynthetic process* (F1 = 1.0). In
*P. putida* (cutoff 28) and human (44), paralog families sit well below the cutoff.

### The network does assemble

- In PSEPK, 411 of 578 enzymes fall into one connected component. When every step of a
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
  - P. putida: 14 of 22 communities match a BP term (F1 ≥ 0.5). Examples are the TCA
    cycle, benzoate catabolism, chorismate biosynthesis, fatty-acid biosynthesis, the
    pentose-phosphate shunt (0.74), the methylerythritol phosphate pathway (0.77) and
    L-leucine catabolism (0.89).
  - Human: 10 of 19 match. Examples are protein N-linked glycosylation (0.79), glucose
    6-phosphate metabolism (0.72), nucleotide salvage (0.60), bile-acid biosynthesis and
    saturated fatty-acid elongation (0.93; tied with the unsaturated sibling term, as each
    covers 7 of the cluster's 8 genes: ELOVL1–7 and HSD17B12).

### It agrees with BP, strongly but not completely

- Metabolically linked enzymes share a specific metabolic BP **8–9× more often than random
  pairs**: 39% vs 4.4% in PSEPK (8.9×) and 54% vs 7.1% in human (7.6×).
- Split by edge kind (BP-annotated pairs only):
  - Same-step pairs agree almost always (96% and 93%), as expected for genes doing the
    same reaction.
  - Handoffs: 34% (P. putida) and 50% (human) share a specific BP.
  - Handoffs through a non-hub intermediate: 65% and 71%, i.e. 15× and 10× random.
    These are the edges that behave like real pathway steps.
- 78% (PSEPK) and 76% (human) of tested metabolic BP terms have gene sets that are
  significantly more connected than random (p < 0.05). After Benjamini–Hochberg
  correction the counts are 292/384 and 544/742.
- Terms are tested only between 3 enzymes and 4× the "specific" cutoff (112 enzymes in
  P. putida, 176 in human). That excludes the broadest grab-bag terms.

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
4. **Filter-induced false negatives.** This one is a property of the method, not of
   the annotations.
   - A BP term whose label names a currency chemical may be unable to assemble, because
     that chemical is removed: glutamate, glutamine, 2-oxoglutarate, ATP, NADH,
     glutathione and so on. Read such a term against its own random baseline. Human
     *L-glutamine metabolic process*, *L-glutamate biosynthetic process*, *ATP
     biosynthetic process* and *superoxide metabolic process* all sit at it (p = 1).
   - Such terms are flagged in `bp_term_coherence.tsv` (`label_matches_currency_name`,
     a string match on the label): 12 in P. putida and 38 in human. Free ions
     (phosphate, diphosphate, sulfate, sulfite, chloride) are left out of the match,
     because in a label they are almost always part of a compound name ("isopentenyl
     diphosphate", "chondroitin sulfate").
   - Many flagged terms still assemble (8/12 and 23/38 at p < 0.05), mostly nucleotide
     terms (UMP, GMP, CTP) linked through their sugar-phosphate intermediates. Leaving
     all flagged terms out changes the headline little: 293/372 and 540/704 (79% and
     77%).
5. **Gaps.** Unreviewed genes break chains, and so do reviewed MFs with no exact Rhea
   mapping. 336 human and 120 PSEPK enzymes are isolated nodes. These are candidates for
   missing MF specificity, or for GO terms that need an exact Rhea xref (see
   `projects/RHEA`).

### Limits

- **No direction or atom mapping.** Rhea master reactions are undirected, and edges ignore
  which atoms are carried. Shortest paths therefore cut through hubs and side activities:
  - human mevalonate→cholesterol runs via acetyl-CoA, glucosamine 6-phosphate and GBA1;
  - PSEPK lysine→glutarate runs via alanine racemase's lysine side activity, arginine
    and succinyl-CoA.

  A true pathway reconstruction needs Rhea directional IDs (`rhea-directions.tsv`) plus
  atom mappings or a carbon-tracing constraint.
- **Hand-chosen settings.** The currency list and the non-hub cutoff (≤5 enzymes) are
  heuristic. The cutoff is crude: the TCA cycle's own intermediates (succinate,
  fumarate, malate) each touch more than 5 enzymes. So in the viewer the cycle hangs
  together mainly through "hub" links.
- **Exact-only costs coverage.** Dropping narrowMatch xrefs removes reactions as well as
  noise. When the switch was made (2,183 human reviews), human reviewed enzymes mapped to
  700 distinct reactions, against 1,184 when narrow xrefs were (wrongly) treated as
  exact. The same change raised agreement with BP. A
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
| Enzymes with reactions | 578 | 495 | 603 | 17 | 917 | 1355 | 29 | 22 |
| Distinct Rhea reactions | 463 | 484 | 514 | 20 | 843 | 891 | 33 | 26 |
| Edges | 1738 | 1386 | 2161 | 2 | 3516 | 7432 | 6 | 3 |
| Giant component | 411 | 361 | 447 | 2 | 565 | 872 | 5 | 2 |
| Isolated enzymes | 120 | 89 | 114 | 13 | 246 | 398 | 22 | 16 |
| Enzymes with no metabolic BP | 54 | 52 | 109 | 10 | 202 | 471 | 19 | 15 |
| Linked pairs sharing specific BP | 0.39 | 0.42 | 0.376 | 1.0 | 0.422 | 0.397 | 1.0 | 1.0 |
| Same-step edges (shared reaction) | 119 | 99 | 163 | 0 | 257 | 479 | 0 | 0 |
| …sharing specific BP | 0.958 | 0.96 | 0.914 | – | 0.969 | 0.885 | – | – |
| Handoff edges (no shared reaction) | 1467 | 1077 | 1517 | 1 | 2129 | 3611 | 2 | 1 |
| …sharing specific BP | 0.344 | 0.37 | 0.318 | 1.0 | 0.357 | 0.332 | 1.0 | 1.0 |
| Handoffs via a non-hub chemical (≤5 enzymes) | 505 | 424 | 426 | 1 | 532 | 487 | 2 | 1 |
| …sharing specific BP | 0.653 | 0.646 | 0.627 | 1.0 | 0.712 | 0.743 | 1.0 | 1.0 |
| …random pairs | 0.044 | 0.052 | 0.053 | 0.141 | 0.056 | 0.065 | 0.067 | 0.141 |
| BP terms tested | 384 | 359 | 367 | 8 | 485 | 523 | 11 | 8 |
| BP terms connected > random | 301 | 277 | 289 | 0 | 376 | 399 | 3 | 0 |
| Communities | 22 | 19 | 22 | 1 | 24 | 23 | 2 | 1 |
| Communities ≈ a BP term (F1≥0.5) | 14 | 11 | 12 | 1 | 11 | 8 | 2 | 1 |
| Enrichment over random | 8.9× | 8.1× | 7.1× | 7.1× | 7.5× | 6.1× | 14.9× | 7.1× |

#### human

| Metric | reviews | uniprot-rhea-reviewedset | goa-all-reviewedset | goa-exp-reviewedset | uniprot-rhea | goa-all | goa-noiea | goa-exp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Enzymes with reactions | 895 | 952 | 947 | 726 | 4140 | 3758 | 3270 | 2457 |
| Distinct Rhea reactions | 732 | 2420 | 787 | 640 | 6151 | 1593 | 1507 | 1365 |
| Edges | 3135 | 5790 | 3817 | 2549 | 74826 | 45813 | 37418 | 22130 |
| Giant component | 528 | 659 | 555 | 469 | 2403 | 1960 | 1835 | 1495 |
| Isolated enzymes | 336 | 277 | 364 | 226 | 1718 | 1749 | 1379 | 915 |
| Enzymes with no metabolic BP | 130 | 157 | 154 | 179 | 1258 | 993 | 860 | 827 |
| Linked pairs sharing specific BP | 0.543 | 0.468 | 0.504 | 0.477 | 0.439 | 0.469 | 0.468 | 0.457 |
| Same-step edges (shared reaction) | 327 | 295 | 433 | 168 | 5327 | 6840 | 4913 | 2070 |
| …sharing specific BP | 0.93 | 0.898 | 0.855 | 0.869 | 0.827 | 0.754 | 0.755 | 0.743 |
| Handoff edges (no shared reaction) | 2633 | 4920 | 3101 | 1579 | 48922 | 30423 | 23427 | 9857 |
| …sharing specific BP | 0.495 | 0.442 | 0.455 | 0.436 | 0.397 | 0.405 | 0.408 | 0.397 |
| Handoffs via a non-hub chemical (≤5 enzymes) | 527 | 1016 | 545 | 331 | 1688 | 589 | 584 | 422 |
| …sharing specific BP | 0.712 | 0.703 | 0.714 | 0.61 | 0.745 | 0.727 | 0.697 | 0.675 |
| …random pairs | 0.071 | 0.072 | 0.068 | 0.068 | 0.076 | 0.071 | 0.076 | 0.077 |
| BP terms tested | 742 | 848 | 812 | 581 | 1415 | 1375 | 1262 | 939 |
| BP terms connected > random | 563 | 649 | 605 | 380 | 1078 | 1053 | 933 | 659 |
| Communities | 19 | 12 | 15 | 19 | 13 | 19 | 20 | 19 |
| Communities ≈ a BP term (F1≥0.5) | 10 | 6 | 5 | 8 | 2 | 9 | 7 | 5 |
| Enrichment over random | 7.6× | 6.5× | 7.4× | 7.0× | 5.8× | 6.6× | 6.2× | 5.9× |

### Findings

- **Yes, a network assembles from plain UniProt annotations.** It is bigger and less
  coherent than the one from reviewed annotations:
  - Human: whole Swiss-Prot gives a 2,403-gene giant component from the Rhea column
    (1,960 from GOA). Linked pairs share a specific BP 5.8–6.6× more often than random.
  - On the same genes, reviewed annotations agree best, though in human only narrowly:
    8.9× (P. putida) and 7.6× (human), against 7.1× and 7.4× for GOA with all evidence.
  - Reviewed annotations also give the most BP-matching communities: 14/22 (P. putida)
    and 10/19 (human), against 12/22 and 5/15 for GOA on the same genes.
  - **For non-hub handoffs, the sources converge.** On the same genes, 65%/71% of these
    share a BP with reviewed annotations, against 63%/71% for GOA and 65%/70% for the
    UniProt Rhea column (P. putida/human). Whole-proteome GOA is higher (74%/73%), but
    electronic MF and BP from the same rule agree by construction.
  - So the reviews' advantage sits in same-step pairs, which reviews get more right
    (93% vs 86% in human), and in hub-mediated links.
- **The UniProt Rhea column has the widest reaction coverage but the weakest BP
  agreement in human.** It needs no GO→Rhea step.
  - On the same 952 human enzymes it lists 2,420 reactions, against 732 from the
    reviews. Many of these are substrate-specific variants. Its BP agreement there is
    6.5×, and its handoffs share a BP 44% of the time (50% for the reviews). Its
    non-hub handoffs (70%) match the reviews (71%).
  - In P. putida it is close to the reviews (8.1× vs 8.9× on the same genes).
  - Its coverage is mostly Swiss-Prot: 441 of 745 reviewed P. putida entries carry Rhea
    IDs, against 476 of 4,784 unreviewed ones. Most of the benzoate pathway (benA, benC,
    benD) is unreviewed TrEMBL with no CATALYTIC ACTIVITY line. As a result, the
    benzoate→succinyl-CoA route that the reviews reconstruct is broken in
    `uniprot-rhea`.
- **GOA MF with exact Rhea xrefs is a reasonable bulk source.** P. putida `goa-all` has
  1,355 enzymes, against 578 from the reviews. It reconstructs the benzoate→succinyl-CoA
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
  `-reviewedset` and `goa-exp` columns are the fairer comparisons. The `reviews` source
  has its own version of this. A curator fills `molecular_function` and
  `directly_involved_in` in one pass over the same papers, and many MF→BP pairs are
  linked in GO itself. Part of the reviews' advantage is therefore single-author
  consistency rather than independent agreement.

## Outputs (`results/<ORG>/<source>/`)

`summary.json`, `edges.tsv`, `gene_reactions.tsv`, `bp_term_coherence.tsv` (per-term
connectivity, p-value, isolated genes), `communities.tsv`, `discordant_edges.tsv` (linked
pairs with no shared metabolic BP), `graph.json` (for visualisation). Whole-proteome
`edges.tsv`/`graph.json` are git-ignored (large, regenerable).
