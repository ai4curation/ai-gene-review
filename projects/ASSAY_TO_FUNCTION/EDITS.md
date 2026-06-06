# Gene annotation edits from the ASSAY_TO_FUNCTION analysis

YAML edits made to gene review files as a direct result of this project's
readout/over-annotation analysis, plus the candidates that were re-reviewed and
**deliberately left unchanged** (with the reason), so the curation record is
transparent.

## Annotations downgraded ACCEPT → KEEP_AS_NON_CORE

All are genuine, evidence-supported processes that are **downstream of the
gene's core molecular function** (a secreted signaling ligand or an enzyme),
surfaced by the flagger's `indirect_ligand` / hub-readout signal and confirmed
by re-review against each file.

| gene | gene description (short) | term (GO) | refs | rationale |
|---|---|---|---|---|
| **PDGFB** (human) | Platelet-derived growth factor B chain; secreted PDGF ligand subunit that activates PDGF receptors to drive paracrine growth-factor signaling. | positive regulation of glomerular mesangial cell proliferation (GO:0072126) | PMID:16014047, PMID:11788434 | Tissue-specific proliferation downstream of PDGF-B/PDGFR signaling; not a core function of the ligand. |
| **HMGB1** (human) | Non-histone chromatin protein (two HMG-box DNA-binding domains); nuclear DNA bending/architecture + extracellular DAMP signaling. | positive regulation of cytosolic calcium ion concentration (GO:0007204) | PMID:22370717 | Calcium rise is downstream of extracellular HMGB1-CXCL12 acting via the CXCR4 receptor; not an HMGB1 core function. |
| **Sirt2** (mouse) | NAD-dependent protein deacetylase / defatty-acylase; deacetylates histones, α-tubulin, and many substrates. | positive regulation of cell division (GO:0051781) | PMID:24334550 | Division control is downstream of Sirt2's core deacetylase activity (mitotic substrate deacetylation), not a core function itself. |
| **VEGFA** (human) | Master regulator of angiogenesis; secreted growth factor activating VEGFR signaling. | negative regulation of apoptotic process (GO:0043066) | PMID:11461089, PMID:10066377 | Generic anti-apoptosis reflects downstream PI3K-Akt survival signaling; VEGFA's core/defining output (endothelial proliferation / angiogenesis) is retained as core. |

4 genes, 6 annotation records (PDGFB ×2, VEGFA ×2, HMGB1 ×1, Sirt2 ×1). All
files re-validated with `linkml-validate` (no issues).

**PDGFB note (discussion outcome):** a reversal was considered on the grounds
that mesangial cells are a "signature" PDGFB role (PDGFB-null mice lack them).
That argument was rejected as **non-mechanistic** — knockout *necessity* for
mesangial-cell development is not evidence that the secreted ligand *directly
regulates proliferation* (the receptor does the signaling). The annotation
stays `KEEP_AS_NON_CORE`.

## Deferred to expert curator (ACCEPT → UNDECIDED)

| gene | term (GO) | refs | why deferred |
|---|---|---|---|
| **IL21** (human) | positive regulation of T cell proliferation (GO:0042102, ×2) | PMID:17673207, PMID:15207081 | Borderline core vs non-core: the effect is real and directly evidenced, but IL21 is a weak, context-dependent T-cell mitogen relative to its signature B-cell/Tfh axis. Set `UNDECIDED` and removed from `core_functions` pending expert review — see **issue [#1418](https://github.com/ai4curation/ai-gene-review/issues/1418)**. The B-cell/Tfh/GC/Ig signature processes remain core; NK cytotoxicity (GO:0045954, IBA/IEA) is raised in the issue for the same review. |

## Re-reviewed but deliberately NOT changed (flag was a false positive)

Documented so the analysis is honest about precision and to prevent re-flagging.

| gene | candidate term | why kept as-is |
|---|---|---|
| **VEGFA** | positive regulation of endothelial cell proliferation (GO:0001938) | This *is* VEGFA's defining function (massive IDA support); the flag fires only because VEGFA has growth-factor-activity MF. |
| **SIRT1** | transcription corepressor activity (GO:0003714) | Well-supported MF across many IDA/IMP studies; deacetylase is the core MF but corepressor activity is a legitimate, directly evidenced role. |
| **Calm2 / HRC** | calcium(-dependent) binding (GO:0048306 / GO:0005509) | Direct binding MF established by binding/IPI assays — not licensed by, nor reducible to, a calcium-imaging readout. |
| **CTNNB1 / NOTCH1** | transcription coactivator activity (GO:0003713) | β-catenin and NICD are bona fide transcriptional coactivators (machinery); reporter-supported MF is appropriate. |

## Method note

These edits are the curation output of the pipeline in
[`../ASSAY_TO_FUNCTION.md`](../ASSAY_TO_FUNCTION.md): mine source papers for
assay/readout usage → rubric → flagger (`flagged_candidates.tsv`) → per-gene
re-review against the actual file evidence. The key discipline: a flag is a
*candidate*; an edit is made only after confirming the process is downstream of
a different, more proximal core function — and is declined when the "downstream"
process is itself the gene's defining role (VEGFA EC proliferation, IL21 immune
outputs).
