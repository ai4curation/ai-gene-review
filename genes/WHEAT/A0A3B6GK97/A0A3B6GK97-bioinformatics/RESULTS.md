# Bioinformatics analysis: A0A3B6GK97 (wheat patatin/PNPLA protein)

**Question.** (1) Which plant patatin-related phospholipase A (pPLA) subfamily does
this protein belong to (to refine the functional inference beyond the domain-level
"lipid metabolic process"), and (2) is its catalytic machinery intact (i.e., is it a
genuine acyl hydrolase, a pseudoenzyme, or a truncated model)?

**TL;DR.**
- By sequence identity and tree placement over the region it retains, A0A3B6GK97 belongs
  to the **pPLAII** subfamily (42–50% identity to pPLAII / rice pPLAs; ~23% to pPLAIII;
  ~16% to pPLAI). It is **not** a pPLAIII (galactolipase/growth) or pPLAI (iPLA2-like) protein.
- **However, the modeled 302-aa sequence lacks the entire N-terminal half of the patatin
  catalytic domain** — both the **oxyanion glycine-rich block (DGGG)** and the **catalytic
  serine nucleophile elbow (G-T-S-T-G)** are absent. It retains the C-terminal portion
  including the catalytic Asp. **As deposited, the protein is therefore predicted to be
  catalytically inactive** (no nucleophilic serine).
- Most parsimonious explanation: an **incomplete/incorrect gene model** (TraesCS3D02G033600
  is ~100–130 aa shorter than full-length orthologs, missing exactly the N-terminal catalytic
  exon region). A genuine degenerate pseudo-enzyme cannot be excluded from sequence alone.

This is a **caveat to the lipase interpretation**: the GO_Central IBA annotations
(glycerophospholipase GO:0004620, monoacylglycerol lipase GO:0047372) are phylogenetic
propagations that assume an intact active site and do **not** verify it; the modeled
sequence cannot support those activities as-is.

---

## Methods

All sequences fetched live from the UniProt REST API; no sequences or results are
hardcoded. Reproduce with `just all` (recipes: `fetch`, `analyze`, `test-control`).

- **Query:** A0A3B6GK97 (wheat, TraesCS3D02G033600), 302 aa.
- **Reference set (13):** characterized plant pPLAs spanning all three subfamilies plus a
  structural anchor — Arabidopsis pPLAI (F4HX15), pPLAIIα–ε (O48723, O23181, O23179, O23180,
  Q9FIY1), pPLAIIIα–δ (O80959, Q9SV43, Q8H133, Q93ZQ3 — the last annotated "probable
  **inactive**", used as a pseudoenzyme control), rice PLP1/PLP2 (Q84QY3, Q6ZJD3), and potato
  patatin (P15478; the Ser-Asp dyad family of PMID:12779324). Provenance and the UniProt
  queries used are in `data/reference_accessions.tsv`.
- **Tools:** Python 3.11; pyfamsa 0.7.0 (FAMSA MSA, UPGMA guide tree); BioPython 1.87
  (identity distance matrix, neighbour-joining tree). Catalytic motifs detected two ways:
  (a) MSA-independent regex scan of raw sequences for the nucleophile `G-x-S-x-G` and
  oxyanion `DGGG`; (b) MSA column conservation among the core active single-domain enzymes
  (pPLAI and the inactive PLP9 excluded from the catalytic-consensus set only; they are still
  in the placement analysis).
- **Outputs:** `results/alignment.fasta`, `pairwise_identity_to_query.tsv`, `nj_tree.newick`,
  `motif_scan.tsv`, `catalytic_site.tsv`, `catalytic_columns_all_seqs.tsv`, `summary.json`.

## Results

### 1. Subfamily placement → pPLAII

`results/pairwise_identity_to_query.tsv` (%identity to query, over ~98% query coverage):

| Reference | Subfamily | %id |
|---|---|---|
| At pPLAIIα PLP2 (O48723) | pPLAII | **50.5** |
| Rice PLP1 (Q84QY3) | pPLA (rice) | 50.0 |
| Rice PLP2 (Q6ZJD3) | pPLA (rice) | 46.8 |
| At pPLAIIβ PLP3 (O23181) | pPLAII | 46.0 |
| At pPLAIIδ PLP5 (O23180) | pPLAII | 45.6 |
| At pPLAIIε PLP4 (Q9FIY1) | pPLAII | 43.5 |
| At pPLAIIγ PLP1 (O23179) | pPLAII | 42.6 |
| Potato patatin (P15478) | storage | 36.9 |
| At pPLAIIIδ PLP9 (Q93ZQ3) | pPLAIII (inactive) | 23.9 |
| At pPLAIIIα/β/γ | pPLAIII | 22.4–23.7 |
| At pPLAI PLA1 (F4HX15) | pPLAI | 15.8 |

The whole pPLAII subfamily (+ rice pPLAs) ranks at 42–50%, with a clear gap to pPLAIII
(~23%) and pPLAI (16%). The NJ tree (`nj_tree.newick`) places the query within the
pPLAII/rice/patatin clade, separate from pPLAIII and the long-branch pPLAI. Nearest
neighbours by patristic distance: rice PLP2, At pPLAIIα, At pPLAIIγ, At pPLAIIδ.
**Conclusion: pPLAII-type** (the "classic" lipid acyl hydrolase clade — defense/wounding/
stress-associated in Arabidopsis), *over the portion of the domain the model retains*.

### 2. Catalytic machinery is missing from the modeled sequence

MSA-independent motif scan (`results/motif_scan.tsv`):

| Sequence | len | G-x-S-x-G (catalytic Ser) | DGGG (oxyanion) |
|---|---|---|---|
| **QUERY A0A3B6GK97** | **302** | **0 — NONE** | **0 — NONE** |
| At pPLAIIα PLP2 | 407 | 1 — pos 66 (GTSTG) | pos 25 |
| At pPLAIIβ/γ/δ/ε | 401–428 | 1 — GTSTG | present |
| Rice PLP1 / PLP2 | 405–432 | 1 — GTSTG | present |
| Potato patatin P15478 | 386 | 1 — pos 77 (GTSTG) | pos 35 |
| At pPLAIIIδ PLP9 (inactive ctrl) | 384 | 0 — NONE | present |

Every active reference carries the canonical `G-T-S-T-G` nucleophile elbow; the query has
**no `G-x-S-x-G` anywhere** in 302 aa and **no `DGGG` oxyanion block**. The MSA
(`results/catalytic_columns_all_seqs.tsv`, and the alignment around cols 540–600) shows the
query **fully gapped** through the N-terminal catalytic core — its modeled N-terminus begins
*downstream* of where the catalytic Ser sits. The query **does** retain the catalytic-Asp
region (Asp121, in `NLIDSG`), matching the active references.

Interpretation: the model has the C-terminal ~⅔ of the patatin domain (incl. catalytic Asp)
but is missing the N-terminal ~⅓ bearing the oxyanion and the catalytic serine. Without the
nucleophilic Ser, acyl-ester hydrolysis is mechanistically impossible — **predicted inactive
as modeled.**

### 3. Control (pipeline is input-driven, not hardcoded)

Re-running with potato patatin relabelled as the query (`just test-control`,
`results_control/`) correctly recovers intact motifs (GTSTG pos 77, DGGG pos 35) and a
pPLAII/patatin placement — confirming the query's "motifs absent" result is a property of the
A0A3B6GK97 sequence, not an artifact.

## Interpretation & caveats

- **Subfamily = pPLAII** is well supported (large identity gap to other subfamilies; consistent
  tree placement). pPLAII proteins are soluble lipid acyl hydrolases (sn-1/sn-2 acyl ester
  hydrolysis of glycerolipids), associated in Arabidopsis with defense, wounding, phosphate
  starvation and abiotic stress — *not* membrane trafficking. This (plus the single-domain
  architecture) makes a trafficking role very unlikely for this protein.
- **The deposited protein lacks the catalytic serine** and oxyanion block → predicted
  catalytically inactive *as modeled*.
- **Two non-exclusive explanations**, which sequence alone cannot distinguish:
  1. **Incomplete/incorrect gene model** (most parsimonious): 302 aa vs ~400–432 aa for
     orthologs; the missing segment is a clean N-terminal block consistent with a missing
     5′ exon — a common error in automated hexaploid-wheat annotation. **Resolving this
     requires checking the genomic locus, the 3B/3A/3D homoeologs, and alternative gene
     models / RNA-seq — not done here.**
  2. A genuine **degenerate pseudo-patatin** that has lost the nucleophile.
- **Consequence for GO:** the IBA lipase MF annotations were propagated phylogenetically and
  assume an intact active site; they are **not verifiable on the modeled sequence**. The MF
  inference (lipase / carboxylic ester hydrolase) should carry this caveat, and the gene model
  itself is a candidate for revisiting.

## Reproducibility checklist

- [x] Scripts use **no hardcoded inputs or outputs** — all sequences fetched live from UniProt
      by accession; all numbers computed from the data at runtime. Conclusions are only in this
      RESULTS.md, not in code.
- [x] Pipeline **tested on another input** — (a) it runs over 13 references simultaneously and
      correctly recovers GTSTG/DGGG in all active enzymes while flagging absence in the
      annotated-inactive PLP9; (b) an explicit control (`test-control`) with active patatin as
      the query recovers intact motifs + correct placement.
- [x] Analyses **completed as expected**; full pipeline re-runs cleanly from scratch
      (`just all`).
- [x] **Direct script outputs** are in `results/` and `results_control/`.
- [x] Summary includes **detailed provenance and justification**, and is explicit about
      uncertainty (truncated model vs true pseudoenzyme is **not resolved**).
- [?] **Not resolved:** whether the missing N-terminus is an annotation artifact or biological
      — would need genomic/homoeolog/transcript evidence.

## Provenance

- Reference accessions + UniProt query rationale: `data/reference_accessions.tsv`.
- pPLA subfamily framework: Scherer et al. 2010 (PMID:20961799); review PMID:39645102.
- Patatin Ser-Asp catalytic dyad / GTSTG nucleophile: PMID:12779324.
- Tools: UniProt REST (rest.uniprot.org), pyfamsa 0.7.0, BioPython 1.87.
