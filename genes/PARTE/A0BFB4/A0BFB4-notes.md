

## Full-gene re-review, 2026-09-20

All14 rows reviewed. Four broad catalytic/nucleotide annotations and membrane/cytosol restored to ACCEPT; cytoplasmic support now explicitly comes from PAINT rather than solubility. The four autophagy rows remain UNDECIDED while root independently checks PTN000681272 and target placement. Neither the LOK-related family name, domain count, huge ciliate kinome nor absence of a target assay is sufficient counterevidence. Falcon was read completely and its target-substrate/location limits incorporated; generic ciliate pathway discussion was removed from the biological description. Source rows are unchanged.


### Actual PAINT topology resolved during the same review

Root obtained the nested tree with POST to the PANTHER treeinfo endpoint. The exact lineage was independently read: PTN002805221 → PTN000681272 → PTN007795585 → PTN008401646 → PTN001218730 → PTN007795752 → PTN002805316 (A0BFB4/GSPATT00028266001). This supersedes the earlier inability to inspect the tree. All four autophagy rows are now ACCEPT as inherited functions. The evidence snapshot and explanation are in A0BFB4-placement-evidence.md/json and root’s projects/TREEGRAFTER/rereview-2026-09-20/a0bfb4-paint-classification-check.json. The remaining focused question reconciles live sequence classification with actual PAINT family assignment; it does not assume that the target lies outside the autophagy clade.


## Recovery PR specificity follow-up (2026-09-22)

Make the molecular work or process role explicit separately for each challenged term; retain evidence-based core versus peripheral judgments rather than treating ontology breadth as non-coreness.


## Final evidence and annotation-action reconciliation (2026-09-23)

Removed limitation/tool-access statements from positive support where applicable and retained the actual lineage or sequence evidence. Historical uncertainties remain in the rationale rather than being treated as proof of function.


## OpenScientist autophagy-architecture follow-up (2026-10-10)

Read the focused report on the PTHR24348 versus PTHR44167 placement issue. The report supports the same conclusion as the earlier topology snapshot that A0BFB4 is genuinely Atg1/ULK-related rather than misplaced into PTHR24348 by a donor-count artifact. Its new target-relevant argument is narrower: A0BFB4 retains the compact kinase domain but lacks the canonical C-terminal Atg1 interaction module, and ciliates lack the Atg13/Atg17/Atg101 initiation complex. Retained the kinase MF rows and broad PAINT localizations, marked the four autophagy BP/CC rows as over-annotated, and removed autophagosome assembly / phagophore assembly site from the core function pending Paramecium-specific localization or knockdown evidence.


## Track C finish (2026-10-20)

Closed the draft out as part of the PROTISTS Track C (ciliates) batch. Automated deep
research is still unavailable in this environment (perplexity is not a registered
provider, falcon fails authentication, the OpenAI key is rejected), so nothing new was
generated; the existing `A0BFB4-deep-research-falcon.md` was re-read instead.

Two changes only, both to clear the one content warning that stood between this file and
`status: COMPLETE` — that no annotation cited the available deep-research file, even
though the 2026-09-20 round records having read it in full:

- `GO:0004674` (IBA) now cites the Falcon report for the point that actually bears on the
  row, that the functional call rests on domain architecture rather than any A0BFB4 assay
  [file:PARTE/A0BFB4/A0BFB4-deep-research-falcon.md "functional interpretation therefore
  depends mainly on domain architecture and kinome context rather than direct experiment"].
- `core_functions` now carries the report's substrate statement
  [file:PARTE/A0BFB4/A0BFB4-deep-research-falcon.md "The specific substrates of A0BFB4 are
  unknown."], which is what keeps the core function stated at kinase level with no substrate.

No annotation action was changed. In particular:

- The four autophagy rows keep the dispositions the earlier rounds reached: three
  `MARK_AS_OVER_ANNOTATED` (`GO:0000045`, `GO:0000407`, `GO:0005776`) and `GO:0010506`
  left `UNDECIDED`. The asymmetry is deliberate and is argued in that row: the three
  specific terms name canonical Atg1-complex machinery the lineage lacks, while
  regulation of autophagy is broad enough that a noncanonical ciliate role stays open.
  Closing it needs Paramecium perturbation data, not another pass over the same evidence.
- The four broad catalytic/nucleotide rows (`GO:0004672`, `GO:0016301`, `GO:0016740`,
  `GO:0000166`) were left `ACCEPT` at first, because the 2026-09-20 and 2026-09-22 rounds set
  them that way on purpose. That is now changed to `TOO_GENERAL` — see the next entry.


## Broad catalytic rows moved to TOO_GENERAL (2026-10-22, PR #5300 review)

Review of PR #5300 pointed out that each of the four rows already conceded the entailment in
its own `reason` — "the specific kinase activity entails the broader
nucleotide-binding/phosphotransfer classes" — and then argued for `ACCEPT` on the ground that
the terms are not false. That is not an argument against `TOO_GENERAL`, whose definition says
in terms that it judges the term rather than the evidence and never means the claim is false.
The same PR applies the opposite convention to TETTS TERT, which marks `GO:0034061` (five
rows, four of them EXP), `GO:0003964`, `GO:0003677` and `GO:0000723` `TOO_GENERAL` on exactly
this reasoning. One batch should not ship two conventions, least of all while flipping this
file to `COMPLETE`.

Ancestry verified against QuickGO (`is_a`/`part_of` closure) rather than assumed, before
changing anything:

| row | descendant accepted in this file | ancestor? |
|---|---|---|
| `GO:0000166` nucleotide binding | `GO:0005524` ATP binding | yes |
| `GO:0004672` protein kinase activity | `GO:0004674` | yes |
| `GO:0016301` kinase activity | `GO:0004674` | yes |
| `GO:0016740` transferase activity | `GO:0004674` | yes |

This does not reverse the earlier rounds' decision. That decision was against
`KEEP_AS_NON_CORE`, i.e. against calling these rows peripheral; `TOO_GENERAL` says something
different and compatible — the rows are central and true, and say nothing the specific term
does not already say.

Also in this round: the Falcon citation on the `GO:0004674` IBA row was an absence statement
("depends mainly on domain architecture ... rather than direct experiment") sitting in
`supported_by` for a row whose reason reads "Strongly supported". The absence point moved into
`reason`, where it belongs, and `supported_by` now carries the report's positive Ser/Thr call
[file:PARTE/A0BFB4/A0BFB4-deep-research-falcon.md "supporting inference that the protein most
likely phosphorylates Ser/Thr residues rather than Tyr residues"].
