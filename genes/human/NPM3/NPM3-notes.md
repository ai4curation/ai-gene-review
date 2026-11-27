# NPM3 (human, O75607) review notes

## 2026-11-26: review started from literature-scan issue 7141

The trigger paper is PMID:42958702 (DTX3 Suppresses the NPM3-RUVBL1 Axis to Inhibit Homologous
Recombination Repair; Adv Sci 2026). Its full text is cached.

### Deep research

Deep research did not run: falcon returned 403 and the perplexity-lite fallback returned 401
(quota). I searched the literature by hand from the UniProt-cited primaries:

- PMID:11722795: cloning and nuclear localisation of human NPM3.
- PMID:15596447: NPM3 binds B23 and is nucleolar.
- PMID:20073534: NPM3 alone lacks histone chaperone activity.
- PMID:22362753: NPM1/2/3 hetero-oligomers, in which NPM3 is an active histone chaperone in
  complex with NPM1.

### What the trigger paper adds

The paper is about DTX3, but it contains direct NPM3 experiments in HK1 cells, with HeLa used for
DTX3:

- NPM3 knockdown lowers DR-GFP HR activity but not NHEJ, and raises comet tail moments.
- NPM3 binds RUVBL1 directly (GST pull-down) and in cells (co-IP), and the two colocalise in the
  nucleus after IR.
- NPM3 overexpression raises H4K16ac and RUVBL1-TIP60 assembly.
- NPM3 overexpression rescues HR and 53BP1-focus phenotypes in DTX3-overexpressing cells.

Added: NEW GO:1905168, positive regulation of double-strand break repair via homologous
recombination (IMP). The regulation acts through a direct binding partner, and the effect is
pathway-specific (HR but not NHEJ). The DTX3 ubiquitination of NPM3 Lys102 is NPM3 acting as a
substrate, so I did not annotate it on NPM3.

### Annotation decisions

- REMOVE: six bare GO:0005515 rows.
- MARK_AS_OVER_ANNOTATED: cytoplasm (IBA). No study of human NPM3 finds a cytoplasmic pool.
- KEEP_AS_NON_CORE: RNA binding (HDA and IBA).
