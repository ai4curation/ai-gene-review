# PDB: Deposited Structures as Functional-Insight Evidence

## Goal

Many genes in this review pipeline have experimentally solved 3D structures deposited in
the [Protein Data Bank](https://www.rcsb.org/). A structure is not just a picture: when it
captures a **bound ligand, cofactor, catalytic metal, or partner macromolecule**, it is
direct, experimental evidence for molecular function, binding, and complex membership — the
very things GO annotation review hinges on.

This project (1) inventories what is deposited across the whole pipeline, and (2) prioritizes
the structures most likely to *change or strengthen* a gene's functional annotation, so that
structure-informed review effort goes where it pays off.

## What "functional insight" means here

A deposited structure is most valuable for review when **what is bound in it** tells us
something the current annotations do not. The prioritization therefore combines two axes:

1. **Structure richness** — what the structure actually contains:
   - bound **cofactor / catalytic metal** (FAD, NAD(P), PQQ, F430, Fe–S clusters, heme, Zn, …)
     → strongest single clue to catalytic mechanism / molecular function
   - bound **substrate / product / inhibitor ligand** → active-site and specificity evidence
   - **complex** (≥2 protein entities, or bound nucleic acid) → interaction & CC evidence
   - high **sequence coverage** (full-length vs a short peptide fragment in a partner's structure)

2. **Annotation sparsity** — a structure adds the most where we currently know the least.
   Genes whose GO annotations are **electronic-only (IEA/IBA)** with *no experimental
   molecular-function term* are upweighted: here a ligand-bound structure (plus literature)
   can ground a specific, experiment-grade MF annotation that today rests only on inference.

The two are multiplied: `richness × sparsity`. An apo structure of an already
well-annotated protein scores low; a cofactor-bound, full-length structure of an IEA-only
enzyme scores high.

## What is deposited (pipeline-wide inventory)

Computed offline from the cached UniProt records (`*-uniprot.txt`, `DR PDB` cross-references):

| Metric | Count |
|--------|------:|
| Genes with ≥1 deposited PDB structure | **949** / 2529 |
| Total deposited PDB entries | **13,415** |
| **Eukaryotic** genes with a structure | 815 |
| Genes with a structure but **no experimental GO at all** | 73 |
| Genes with a structure but **no experimental molecular-function GO** | 115 |
| Genes where a review **disputed a catalytic MF** (REMOVE/over-annotated) | 130 |

Top organisms by genes-with-structure: human (588), yeast (65), ARATH (53), BPT4 (32),
mouse (30), ECOLI (23), PSEPK (19), SCHPO (17), worm (17), rat (15).

### Three prioritization cuts

`enrich_rcsb.py` enriches the union of three candidate cuts (281 genes; each tagged in the
`candidate_reason` column), so the priority list is no longer prokaryote-dominated:

| Cut | Definition | Genes | What structure adds |
|-----|------------|------:|---------------------|
| `dark_mf` | no experimental molecular-function GO | 115 | grounds a first experiment-grade MF |
| `euk` | eukaryotic **and** ≤2 experimental MF terms | 103 | sharpens an IEA term / pins complex membership |
| `contested` | review marked a **catalytic** MF `REMOVE`/over-annotated | 130 | adjudicates the disputed activity (pseudo-enzyme / over-general / wrong-specific) |

Full inventory: `PDB/data/pdb_inventory.tsv` (per entry) and
`pdb_gene_summary.tsv` (per gene).

## Prioritized candidates (first pass)

The 115 genes with a structure but no experimental MF GO were enriched with RCSB metadata
(bound ligands, entity counts, titles). Of the 105 that resolved:

- **42** have a structure with a bound **cofactor / catalytic metal**
- **69** have a structure with a meaningful (non-buffer) **ligand**
- **40** are captured in a **complex**; 6 with bound **nucleic acid**
- 23 are apo with no partner (lower structural-insight yield)

These are **IEA-only** enzymes/proteins whose function is structurally (and often
biochemically) characterized but whose GO annotations have not been promoted beyond
electronic inference — the sweet spot for structure-grounded review.

| # | Gene | Organism | UniProt | n PDB | cofactor | ligand | complex | cofactors/ligands |
|---|------|----------|---------|------:|:--------:|:------:|:-------:|-------------------|
| 1 | rpsD | PSEAE | O52759 | 6 | ✓ | ✓ | ✓ | GDP,ZN |
| 2 | psaC | CHLRE | Q00914 | 17 | ✓ | ✓ | ✓ | FES,SF4 |
| 3 | secA | BACSU | P28366 | 18 | ✓ | ✓ | ✓ | ADP |
| 4 | (DsrAB) | DESVH | P07598 | 12 | ✓ | ✓ | ✓ | FE2,HEC,SF4,ZN |
| 5 | mcrA | METAC | Q8THH1 | 4 | ✓ | ✓ | ✓ | COB,F430,FE,SAM,SF4 |
| 6 | wac | BPT4 | P10104 | 117 | ✓ | ✓ | ✓ | ZN |
| 7 | rbcL | 9POAL | P0C512 | 3 | ✓ | ✓ | ✓ | NDP (RuBisCO) |
| 8 | algK | PSEPK | Q88NC7 | 1 | ✓ | ✓ | ✓ | NI |
| 9 | mxaI | METEA | P14775 | 3 | ✓ | ✓ | ✓ | PQQ |
| 10 | fae | METEA | Q9FA38 | 11 |  | ✓ | ✓ | H4MPT,DCP,CA,MG |
| 12 | cbh1 | HYPJE | P62694 | 48 | ✓ | ✓ |  | (cellobiohydrolase) |
| 13 | pqqB | PSEPK | Q88QV5 | 8 | ✓ | ✓ |  | CU,MN,ZN |
| 16 | merA | PSEAI | P00392 | 6 | ✓ | ✓ |  | FAD,NADP |
| 17 | mtdA | METEA | P55818 | 5 | ✓ | ✓ |  | NADP |
| 18 | pcaF | PSEPK | Q88N39 | 4 | ✓ | ✓ |  | COA |
| 23 | mdh | METEA | Q84FY8 | 2 | ✓ | ✓ |  | NAD |
| 25 | xoxF1 | METEA | C5B120 | 2 | ✓ | ✓ |  | PQQ |

Full ranked list: `PDB/data/pdb_gene_enriched.tsv` (now includes the
RCSB per-entry **structure-paper PMIDs** and an `is_eukaryote` flag).

## Eukaryotic candidates (so they aren't drowned out)

Broadening beyond the strict "no experimental MF" cut to `euk` + `contested` surfaces a
much richer eukaryotic slice (815 eukaryotic genes have a structure). Top eukaryotic
candidates by score, with the cut(s) that flagged them:

| # | Gene | Org | UniProt | reason | nPDB | cof | lig | cplx | cofactors/ligands | paper |
|---|------|-----|---------|--------|-----:|:--:|:--:|:--:|---|---|
| 1 | psaC | CHLRE | Q00914 | dark_mf,euk | 17 | ✓ | ✓ | ✓ | FES,SF4 (Photosystem I) | PMID:36979472 |
| 2 | rbcL | 9POAL | P0C512 | dark_mf,euk | 3 | ✓ | ✓ | ✓ | NDP (RuBisCO) | PMID:22609438 |
| 3 | PNO1 | yeast | Q99216 | euk | 28 | ✓ | ✓ | ✓ | GTP,ZN (ribosome assembly) | PMID:33326748 |
| 4 | RPS3 | human | P23396 | contested | 133 | ✓ | ✓ | ✓ | ZN (ribosomal / endonuclease?) | PMID:29875412 |
| 5 | NAA15 | human | Q9BXJ9 | contested | 10 | ✓ | ✓ | ✓ | AcCoA (NatA auxiliary) | PMID:40639378 |
| 6 | HEN1 | ARATH | Q9C5Q8 | contested,euk | 1 | ✓ | ✓ | ✓ | SAH (RNA methyltransferase) | PMID:19812675 |
| 7 | TERT | human | O14746 | contested | 17 | ✓ | ✓ | ✓ | (telomerase RT) | PMID:27903649 |
| 8 | cbh1 | HYPJE | P62694 | contested,dark_mf,euk | 48 | ✓ | ✓ |  | cellobiohydrolase Cel7A | PMID:26307003 |
| 9 | XYL1 | PICST | P31867 | contested,dark_mf,euk | 2 | ✓ | ✓ |  | NADP (xylose reductase) | PMID:30487522 |
| 10 | UPF1 | human | Q92900 | contested | 11 | ✓ | ✓ | ✓ | ATP,Zn (NMD helicase) | PMID:38709891 |
| 11 | BRCA2 | human | P51587 | contested | 14 | ✓ | ✓ | ✓ | ATP (HR mediator) | PMID:40441151 |
| 12 | DOT1 | yeast | Q04089 | contested | 5 | ✓ | ✓ | ✓ | SAM/SAH (H3K79 MTase) | PMID:33479126 |
| 13 | SIRT2 | human | Q8IXJ6 | contested | 60 | ✓ | ✓ | ✓ | NAD,Zn (deacetylase) | PMID:28286128 |

The verified flagships (IDH3B, ATAD1, XYL1, psaC, COX6B1, SPR, COI1) are written up in
`PDB/STRUCTURE_PAPERS.md`. For human genes the structure typically sharpens an
existing IEA term or pins **complex membership** rather than revealing function from scratch.

## Contested catalytic functions (structure adjudicates)

130 genes with a structure have a review that marked a **catalytic** molecular function as
`REMOVE` or over-annotated. A deposited structure is decisive here — it shows whether the
cofactor/active-site pocket is actually present. **Two distinct cases (don't conflate them):**

- **Over-general parent** marked over-annotated (e.g. DOT1/SIRT2 "transferase activity",
  XYL1/pobA "oxidoreductase activity"): the bound cofactor *confirms* catalysis and the
  structure points to the **specific** child term that should replace the generic one.
- **Genuinely-wrong specific** activity marked `REMOVE` (e.g. ARATH **HEN1** "peptidyl-prolyl
  isomerase" — but bound **SAH** argues for its real RNA-methyltransferase activity; human
  **CASP3** tagged "aspartic-type endopeptidase" when it is a cysteine protease; **BRCA2**
  "histone acetyltransferase"): the structure/cofactor adjudicates against the wrong call.

| Gene | Org | disputed catalytic MF | action | cofactor present? | paper |
|------|-----|-----------------------|--------|:-----------------:|-------|
| HEN1 | ARATH | peptidyl-prolyl cis-trans isomerase | REMOVE | **SAH** (→ methyltransferase) | PMID:19812675 |
| CASP3 | human | aspartic-type endopeptidase | REMOVE | (cysteine protease) | — |
| mcrA | METAC | transferase activity (generic) | REMOVE | F430,SAM,Fe-S | PMID:39772843 |
| HAP1 | human | deoxyribonuclease (pyrimidine dimer) | REMOVE | Mn (AP endonuclease) | PMID:25251148 |
| BRCA2 | human | histone acetyltransferase | REMOVE | ATP | PMID:40441151 |
| DOT1 | yeast | methyltransferase activity (generic) | over-annotated | SAM/SAH | PMID:33479126 |
| SIRT2 | human | transferase activity (generic) | over-annotated | NAD,Zn | PMID:28286128 |
| pcaF | PSEPK | acyltransferase activity (generic) | over-annotated | CoA | PMID:32647822 |
| XYL1 | PICST | oxidoreductase activity (generic) | REMOVE | NADP | PMID:30487522 |

Full list with all disputed terms per gene: `pdb_gene_enriched.tsv` (`candidate_reason`
contains `contested`; `contested_cat_mf` lists the term/label/action). **As always, the
disputed-term mapping and the structure PMID must both be verified before use.**

## Grounding in the structure papers

A bound ligand is the clue; the **primary structure paper** carries the functional
interpretation. `PDB/STRUCTURE_PAPERS.md` records verified, PubMed-sourced
notes for the shortlist above (and the prokaryotic flagships mcrA, merA, pcaF), with the
GO-annotation implication for each.

**Caveat surfaced by doing this:** the `structure_papers` PMIDs are the RCSB *per-entry*
primary citation — the paper that deposited *that* coordinate set, which is often a downstream
ligand/inhibitor or methods study rather than the definitive structure/function paper. Verified
drift cases: SPR's PMIDs are inhibitor-screening papers; cbh1's are glycosylation/propranolol
NMR; merA's is the N-terminal NmerA-domain NMR. Others (XYL1, psaC, IDH3B, ATAD1, pcaF, COX6B1)
*are* the definitive paper. **Each PMID must be verified against the gene before it is cited in
a review** (the "verify, don't trust" rule), exactly as `STRUCTURE_PAPERS.md` does.

Patterns worth noting: a cluster of **methylotrophy / PQQ-dependent dehydrogenases**
(METEA `mxaI`, `xoxF1`, `mdh`, `mtdA`, `fae`, PSEPK `pedH`, `pqqB`) and **redox cofactor
enzymes** (`merA` FAD/NADP, `psaC`/`mcrA`/`pqqE` Fe–S, DsrAB heme/siroheme) — these have
diagnostic cofactors visible in their structures, making them low-effort, high-yield review
targets.

## Reproduce

```bash
# 1. offline inventory from cached UniProt + GOA (no network)
python3 projects/PDB/inventory_pdb.py
# 2. RCSB enrichment of the prioritized candidate genes (network)
python3 projects/PDB/enrich_rcsb.py
# 3. structure-paper -> GOA citation gap (offline); writes CURATION_GAP.md
python3 projects/PDB/curation_gap.py
# 4. ranked GAP_OPPORTUNITY review worklist (offline); writes GAP_WORKLIST.md
python3 projects/PDB/gap_worklist.py
# 5. H1 frontier test set: GAP_NO_EXP_CURATION genes (offline); writes data/h1_testset.tsv
python3 projects/PDB/h1_testset.py
```

See `PDB/RESULTS.md` for method detail, caveats, and the full output schema.

## Does structural evidence fill annotation gaps? (`PDB/H1_LEDGER.md`)

`H1_LEDGER.md` tests whether structures fill GO gaps that traditional publications would
not. It records the GAP_OPPORTUNITY→GAP_NO_EXP_CURATION methodology correction, the
three-evidence-layer model of a structure paper (coordinates → low-information binding
terms; the paper's integrative hypothesis → informative function; sequence/EC → catalytic
identity), and the Layer-2 scoring pass. Bottom line: structures reliably supply *first
experimental-grade* evidence for under-curated proteins, but genuinely *new informative*
function is rare — throttled by subunit mismatch and GO expressivity.

## Caveats

- The "no experimental MF GO" flag is computed from the cached `*-goa.tsv`. It flags genes
  whose GO is electronic-only **in our snapshot**; some are well-characterized in the
  literature. That is the point — the structure + literature can justify promoting the
  annotation, not that the function is unknown.
- A bound ligand is a *clue*, not proof: crystallization additives are filtered out, but a
  flagged ligand still needs reviewer judgment (substrate vs adventitious binder).
- UniProt `DR PDB` residue ranges drive the coverage metric; a gene present only as a short
  peptide in a partner's structure scores low coverage, correctly.

## Are structure papers overlooked by curation? (`PDB/CURATION_GAP.md`)

`PDB/curation_gap.py` measures, for every deposited structure with a linked primary
publication, whether that PMID is cited in the gene's GOA `REFERENCE` column. Across
**737** structure-paper × gene pairs (247 genes), only **14%** are cited by GOA; **64%**
are `GAP_OPPORTUNITY` (the paper predates the gene's last *experimental* annotation yet is
never referenced), and **174/247** genes cite zero of their structure papers. "Not cited"
means the structural study is absent from the evidence trail, not that the function is
unannotated — but it quantifies how under-used the structural literature is as a GO evidence
source. The lag boundary uses the latest *experimental* annotation year, since overall GOA
dates are inflated by IEA/IBA pipeline refreshes.

The reusable GOA-citation helper lives in core
(`ai_gene_review.validation.goa_validator.referenced_pmids`); the analysis is
project-specific.

## Prioritized worklist (`PDB/GAP_WORKLIST.md`)

`PDB/gap_worklist.py` ranks the `GAP_OPPORTUNITY` papers by gene priority
(dark-MF / eukaryote / contested) plus the cofactor / ligand / complex richness of the
uncited structures, collapsed to one row per gene (the review unit). Top targets:
`yeast PNO1`, `human RPS3`, `human BIRC5`, `human GCH1`, `human SIRT2`, `human MAPK1`,
`ARATH CRY2`. Per-paper detail in `PDB/data/gap_worklist.tsv`.

## Next steps

- [x] First eukaryotic batch reviewed with structure evidence: `PICST XYL1`, `human IDH3B`,
      `human COX6B1`, `CHLRE psaC`, `ARATH COI1`, `human ATAD1`.
- [ ] Work down `GAP_WORKLIST.md` from the top, citing the verified structure paper + PDB
      entry + bound cofactor as evidence; remaining shortlist includes **prokaryotic**
      `PSEPK pcaF`, `METAC mcrA`, `PSEAI merA`.
- [ ] Extend enrichment beyond the no-exp-MF set to genes with **contested** function
      (cross-reference `CONTESTED_FUNCTION.md`) where a structure could adjudicate.
- [ ] For complexes (≥2 protein entities), map partners to UniProt to support CC / complex
      membership annotations.
- [ ] Replace each peripheral RCSB auto-citation with the definitive structure/function paper
      (see the caveat above) as genes go to review.
- [ ] Consider adding a PDB-evidence field to the review schema (per `ALPHAFOLD.md` action items).
