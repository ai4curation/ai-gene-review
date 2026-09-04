# PEX11B curation notes

## 2026-09-04 — finishing pass (PAINT no-IBA project)

Performed the finishing quality pass over `PEX11B-ai-review.yaml` (drafted with all
actions assigned) and completed the companion family review for PANTHER:PTHR12652.

What was checked / changed:

- Re-verified every one of the 40 `existing_annotations` entries against the GOA
  table and the cached publications. All actions were found justified; no action
  changes were needed. All `supported_by` quotes pass the verbatim-substring
  validator against the cached publications.
- Added the deep-research file (`file:human/PEX11B/PEX11B-deep-research-falcon.md`)
  to the top-level `references` list — it was already cited in `supported_by` of the
  peroxisomal-membrane IBA entry but missing from `references`.
- Set `status: COMPLETE` (update-status confirmed no PENDING actions and zero
  validation warnings).

Action distribution: 23 ACCEPT, 12 MARK_AS_OVER_ANNOTATED (all generic
GO:0005515 protein binding IPIs — the real interactions with PEX19, FIS1, PEX11G
and self are captured by GO:0042802/GO:0042803/GO:0032991 and process terms),
3 KEEP_AS_NON_CORE (the three Reactome cytosol TAS entries, which reflect the
transient cytosolic state of PEX11B during PEX19-dependent PMP import), and
2 REMOVE (GO:0005739 mitochondrion, an Ensembl Compara IEA transfer with no
experimental support in human — PEX11B is an integral peroxisomal membrane
protein; and GO:0007165 signal transduction, an over-broad ISS transfer —
PEX11B is a membrane-remodeling effector, not a signal transducer, and is
constitutively expressed [PMID:9792670 "Levels of PEX11beta mRNA were similar in all tissues examined and were unaffected by peroxisome-proliferating agents"]).

Notable curation findings:

- **The "human no-IBA" flag for this gene is stale.** The current GOA slice
  contains two IBA rows (dated 2025-09-03) from PAINT node PTN000291586:
  GO:0005778 peroxisomal membrane and GO:0016559 peroxisome fission. These match
  the two IBD rows in `interpro/panther/PTHR12652/PTHR12652-paint.tsv` and are
  both reviewed as ACCEPT — the propagation is sound, and PEX11B's own
  experimental evidence (it appears in its own WITH/FROM, as expected) grounds
  the node placement [PMID:9792670 "Overexpression of the human PEX11beta gene alone was sufficient to induce peroxisome proliferation"].
- **Human PEX11G is not in PTHR12652.** Per `interpro/panther/panther-members.tsv`,
  PEX11G (Q96HA9) is classified in PTHR20990, so PTHR12652's human members are
  PEX11A (O75192, SF22) and PEX11B (O96011, SF7) only. Statements that the
  "PEX11 family" tree contains all three human paralogs should not be assumed at
  the PANTHER family level.
- Core function is well settled: constitutive peroxisome membrane elongation and
  fission, via N-terminal-domain-dependent homo-oligomerization and coordination
  with FIS1/DLP1 [PMID:17408615 "ternary complexes comprising Fis1, Pex11pbeta, and DLP1 were detected by chemical cross-linking"].
