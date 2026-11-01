# CG32086 (Q8IQG0, CG32086-RA) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

No ProtNLM2 output was consulted. This folder is the canonical CG32086-RA product (Q8IQG0) of FlyBase gene
FBgn0052086. The sibling folder `genes/DROME/CG32086/` is keyed to the M9NF85 isoform. The two differ only by
a 16-residue internal segment (Q8IQG0 234-250), so the family-placement analysis written there applies here
and is cited (`file:DROME/CG32086/CG32086-bioinformatics/RESULTS-rereview.md`).

Files: fetched with `just fetch-gene DROME Q8IQG0 --alias CG32086__Q8IQG0`. UniProt calls the gene `CG6100`
(a FlyBase synonym); the review uses the FlyBase symbol CG32086.

### Deep research
Not re-run for this folder. A falcon report for the same gene exists at
`genes/DROME/CG32086/CG32086-deep-research-falcon.md` (run 2026-09-10 on the M9NF85 accession). It found no
CG32086-specific primary literature. A Europe PMC search on 2026-10-21 for "CG32086" and "CG6100"
confirmed this: the only hits mention the locus incidentally, e.g. a glue-gene copy-number study,
PMID:38308233.
IntAct lists 15 interactions for Q8IQG0, all high-throughput (Giot et al. 2003 yeast two-hybrid, PMID:14605208;
Lowe et al. 2014 co-IP/pull-down, PMID:25294943). GOA has no IPI rows from them, and they are not used.

### Evolutionary placement
- PANTHER 19.0: Q8IQG0 is in PTHR12086:SF12 (EFHB), with human/mouse/bovine EFHB and fly paralogs FBgn0053489
  and FBgn0053490. Fly Efhc1.1/Efhc1.2 are in SF11 (see sibling RESULTS-rereview.md).
- PAINT nodes behind the five IBA rows (interpro/panther/PTHR12086/PTHR12086-paint.tsv):
  - PTN000250051 GO:0005879 axonemal microtubule. Deep node with 9 seeds across EFHC1, EFHC2 and EFHB.
  - PTN000949412 (taxon 6072, Eumetazoa). GO:0030317 seeded by mouse Efhb (MGI:3045296) alone;
    GO:0070884 seeded by human EFHB alone.
  - PTN004335498 (taxon 2759). GO:0061891 and GO:2001256 seeded by human EFHB alone.
  - Not propagated to CG32086: PTN000250050 terms (centrosome, alpha-tubulin binding, cell-cycle terms,
    cilium-dependent cell motility). These are seeded by EFHC1, and for motility also by mouse Efhc1
    and a trypanosome protein. That node is on the EFHC side, which is consistent with the subfamily split.
- Mouse Efhb motility seed: QuickGO shows mouse Efhb (Q8CDU5) with GO:0030317 IDA from PMID:37295417,
  PMID:37865089 and PMID:37989994, all sperm doublet-microtubule cryo-EM localization papers. In
  PMID:37989994 CFAP21 is modelled as an A-tubule MIP that "may play the role of stabilizing A-tubule wall".
  None of the cached text reports an Efhb motility assay.
- Human EFHB SOCE/Ca-sensor seed: PMID:30481768, a single cell-line study (abstract only). In it, EFHB binds
  STIM1 after store depletion and dissociates in a Ca2+-dependent way.
- PMID:38538594: FAP21 and its human homolog EFHB are outer doublet MIPs, bound near the A-tubule seam
  through GFG repeats, and MIP modules are restricted to ciliated species.

### New analysis (CG32086__Q8IQG0-bioinformatics/RESULTS.md)
- Aligning Q8IQG0 to human EFHB at the canonical loop (human 610 DVDNDGFINYLE) gives fly L340, V342, E344,
  C346, a 4-residue insertion, N352 and D355. So the ligand positions 1 and 3 are lost, 12 is E→D, and the
  loop is interrupted. The canonical Ca-binding loop is not conserved.
- GFG tripeptide scan: there is no contiguous GFG even in human EFHB, so the scan is inconclusive about GFG
  repeats. Nothing is concluded from it.

### Decisions
- GO:0005879 axonemal microtubule (IBA): ACCEPT, core, as an inference (deep, well-seeded node; fly in the
  EFHB subfamily; spermatid expression).
- GO:0030317 flagellated sperm motility (IBA): KEEP_AS_NON_CORE. Plausible structural contribution of a
  sperm axoneme MIP, but the only seed is localization-based, and there are no fly data.
- GO:0061891 calcium ion sensor activity (IBA): REMOVE, because the fly protein has lost the
  coordinating residues of the single canonical loop.
- GO:0070884 calcineurin-NFAT and GO:2001256 SOCE regulation (IBA): MARK_AS_OVER_ANNOTATED. Each rests
  on a single human cell-line study whose mechanism is Ca-dependent, and the predicted location is
  axonemal.
- No NEW terms. Nothing experimental exists for the fly protein. For transfer, the only well-grounded
  statement is the inferred axonemal location, and no CG32086 function is experimentally established in
  Drosophila.
