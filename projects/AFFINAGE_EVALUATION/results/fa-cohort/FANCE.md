# FANCE (FANCE) — AIGR vs Affinage

**Affinage record:** run 2026-06-09 · 10 discoveries · self-eval pairwise "win", faith 100% · gates passed.

## Agreement (brief)

The Affinage narrative and the curated AIGR review agree on FANCE's core biology and there
are no factual conflicts in the narrative layer:

- FANCE is a nuclear subunit of the eight-membered FA core complex (GO:0043240 Fanconi
  anaemia nuclear complex) that acts as a **molecular bridge/adaptor** coupling the core
  complex to its downstream substrate FANCD2 by directly binding both FANCC and FANCD2.
- FANCE is required for nuclear accumulation of FANCC and for FANCD2 monoubiquitination /
  foci; the FANCC-binding and FANCD2-binding surfaces are separable, and the extreme
  C-terminus (Phe-522) is the critical FANCD2-interaction determinant.
- FANCE is phosphorylated by CHK1 (Chk1) at Thr346/Ser374 — a modification dispensable for
  FANCD2 monoubiquitination but required for full crosslink resistance (a separable,
  monoubiquitination-independent function).
- Core BP = interstrand cross-link repair (GO:0036297); FANCE is non-catalytic (FANCL is
  the RING ligase).

Both the CHK1 phosphorylation event and the direct FANCD2-binding/bridging role that the
task flagged were **already captured** in the AIGR review (PMID:17296736 for CHK1;
PMID:12093742 + PMID:12649160 for bridging), so no correction was needed there — only
additional verbatim support was added.

## Disagreements

| Topic | Affinage says | AIGR review says | Verdict (who is right + why) |
|---|---|---|---|
| FANCE molecular activity | `mechanism_profile` lists **GO:0140096 catalytic activity, acting on a protein** alongside molecular adaptor activity | FANCE is **non-catalytic**; core MF = GO:0060090 molecular adaptor activity only; the ligase activity belongs to FANCL (RING subunit) | **AIGR.** The catalytic-activity term is a coarse `mechanism_profile` over-reach. FANCE has no enzymatic activity; it recruits the substrate for FANCL-catalyzed monoubiquitination. AIGR correctly excludes it. |
| GO grounding granularity | Collapses to broad parents (GO:0060090; GO:0005634 nucleus; Reactome R-HSA-73894 DNA Repair) | Re-grounds to specific, GOA-backed terms: nucleoplasm (GO:0005654), FA nuclear complex (GO:0043240), ICL repair (GO:0036297) | **AIGR.** The mechanism profile is intentionally coarse; AIGR's specific terms are correct and more informative. Not a factual conflict. |
| Meiotic anti-crossover role | Highlights FANCC-FANCE-FANCF as conserved **anti-crossover** subcomplex suppressing meiotic crossovers (PMID:36652992) | Not annotated for human FANCE | **AIGR (conservative).** PMID:36652992 evidences this in *Arabidopsis* meiosis; direct human FANCE experimental evidence is lacking, so no human GO annotation is warranted. Noted as a plausible conserved role, not imported. |
| FANCEΔ4 dominant-negative isoform | Reports splice isoform FANCEΔ4 (lacks exon 4) that cannot support FANCD2/FANCI monoubiquitination and may act dominant-negatively (PMID:26277624) | Not annotated | **Neither wrong.** Interesting isoform biology but a loss-of-function/regulatory isoform, not a distinct GO function for the canonical protein. Correctly excluded from annotations; candidate for the notes/isoform tracking layer only. |
| Chr 6p21-22 mapping | Discovery entry PMID:10205272 (linkage mapping to 6p21-22) | Not cited | **Neither.** Genetic-mapping locus fact, not a molecular/biological function; nothing to annotate. |

## Papers incorporated into the review

| PMID | Supports | How used |
|---|---|---|
| PMID:12239156 | FANCE is nuclear FA-complex component; restores FANCC nuclear accumulation + FANCD2 monoubiquitination | Added to `references` (HIGH/VERIFIED) + verbatim `supported_by` on `core_functions` |
| PMID:16127171 | FANCE mediates FANCC-FANCD2 ternary complex; FANCC-only-binding mutants abolish FANCD2 monoubiquitination | Added to `references` (HIGH/VERIFIED) + verbatim `supported_by` on the GO:0060090 molecular adaptor activity annotation |
| PMID:16513431 | FANCE "acts as a molecular bridge" between FA core complex and FANCD2; separable FANCC/FANCD2 binding regions | Added to `references` (HIGH/VERIFIED) + verbatim `supported_by` on the GO:0060090 molecular adaptor activity annotation |
| PMID:24451376 | C-terminal Phe-522 recruits FANCD2 and drives FANCD2-FANCI monoubiquitination; interaction-deficient mutant = cisplatin/MMC sensitive | Added to `references` (HIGH/VERIFIED) + verbatim `supported_by` on `core_functions` |

No NEW GO annotations were added — the adaptor MF and the FA-complex/ICL-repair terms were
already present and correctly grounded; the incorporated papers strengthen (not extend)
existing decisions. Validation remains `✓ Valid`.

## Net assessment

The AIGR review is more accurate and better grounded than the Affinage record wherever they
differ. Affinage's PMID-dense narrative is scientifically sound and its citation set is
high quality, but its `mechanism_profile` GO layer is coarse and, in one case (catalytic
activity, acting on a protein), wrong for this non-catalytic adaptor — a term AIGR rightly
excludes. Affinage's chief value here was surfacing four well-evidenced primary papers
(PMID:12239156, 16127171, 16513431, 24451376) that were absent from the review; these were
verified against their cached text and folded in conservatively as additional support for
the existing molecular-adaptor and bridging annotations. Affinage's meiotic anti-crossover
(Arabidopsis) and FANCEΔ4 isoform findings are real but do not meet the bar for human GO
annotation and were correctly left out.
