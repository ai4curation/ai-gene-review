# POLD2 (horse, F7DA84) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: ProtNLM2 benchmark cohort DONKEY40 / DONKEY40_HORSE_PARTNER; F7DA84 is the horse partner of donkey A0A9L0IND0 (genes/EQUAS/POLD2). No ProtNLM2 output was consulted.

Folder created with `just fetch-gene HORSE F7DA84 --alias POLD2`; stub id is F7DA84.

Deep research: `just deep-research-falcon HORSE POLD2 --fallback perplexity-lite` failed (Edison API 403 "Failed to authenticate"; the perplexity-lite fallback timed out after 600 s). The review relies on cached human POLD2 literature and the human review (genes/human/POLD2).

### Identity
- F7DA84 is unreviewed TrEMBL, 469 aa, PE 3, VGNC:21652 POLD2. Global alignment to human P49005 (469 aa): 95.1% identity, 100% coverage both ways, no gaps (file:HORSE/POLD2/POLD2-bioinformatics/RESULTS.md). Full-length canonical product; not a fragment or isoform. Patient-variant residue Asp293 conserved.
- PANTHER PTHR10416 (DNA POLYMERASE DELTA SUBUNIT 2), subfamily SF0 — the family has a single subfamily, shared with human POLD2, so there is no subfamily-placement issue. The horse IBA rows derive from PTN000045935 (GO:0006271) and PTN000045936 (GO:0043625, eukaryote-wide).

### Evolutionary grounding
- PAINT data (interpro/panther/PTHR10416/PTHR10416-paint.tsv) places at PTN000045935: GO:0016035 zeta DNA polymerase complex (IBD, seeds SGD Pol31 + human P49005; dated 2026-07-27), GO:0042276 error-prone translesion synthesis (IBD, same seeds, 2026-07-27), GO:0008047 enzyme activator activity (IBD, human only, 2026-08-28), GO:0006271 (PomBase Cdc1). Horse descends from that node (it already carries GO:0006271 IBA from it). The three newer IBDs post-date the horse GOA rows and are not deliberate omissions; I propose zeta complex and error-prone TLS as NEW (supported by human Pol zeta4 purification, PMID:24449906, PMID:22465957). I did not propose the enzyme activator activity term: the precise contribution (stimulating REV3L/POLD1 catalysis as a structural subunit) is better expressed as contributes_to DNA-directed DNA polymerase activity in core_functions.

### Annotation decisions
- DNA binding (IEA InterPro): MARK_AS_OVER_ANNOTATED. The PolD2/PolD3-NTD structure shows a negatively charged surface without DNA-binding features [PMID:24449906 "shows a primarily negatively charged molecular surface without obvious features for DNA binding"]. Consistent with human and donkey reviews.
- nucleus (IEA SubCell): MODIFY -> nucleoplasm (Pol delta acts in nucleoplasm; human core function location).
- DNA metabolic process (ARBA): TOO_GENERAL (entailed by GO:0006271).
- DNA replication (IEA InterPro): MODIFY -> GO:0006271.
- DNA strand elongation involved in DNA replication (IBA): ACCEPT.
- delta DNA polymerase complex (IBA + ARBA IEA): ACCEPT both rows.

### Relative
Human POLD2 (P49005), ortholog in same PANTHER subfamily PTHR10416:SF0 and PAINT seed of PTN000045935/36; complete review at genes/human/POLD2/POLD2-ai-review.yaml.

Module: modules/dmel_dna_polymerase_complexes.yaml (Pol delta / Pol zeta shared PolD2-PolD3).
