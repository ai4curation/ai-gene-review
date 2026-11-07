# Lol whole-panel preservation consultation

This is an independent read-only closure of the frozen Lol audit, not a new gene
review, a capacity rerun, or full-corpus validation. Only this directory was
created. All seven scientific consultation manifests plus the capacity manifest
were verified against current bytes, including their protected/input hashes.

## Reproduce

From the Lol worktree root:

```sh
uv run python analysis/module_audits/bacterial_lol_lipoprotein_trafficking/root-panel-consultation/check_preservation.py
uv run ruff check analysis/module_audits/bacterial_lol_lipoprotein_trafficking/root-panel-consultation/check_preservation.py
```

The checker only reads inputs and prints JSON. `receipt.json` captures its output;
`handoff.json` freezes this directory. Original receipts and input sources are
not rewritten by these commands.

## Preservation accounting

| Baseline | Reviews | Original ordered rows |
|---|---:|---:|
| Original ECOLI/PSEPK | 10 | 123 |
| Additional ACIAD/CAUVC/FLAJ1 seeds | 6 | 16 |
| FLAJ1 Fjoh_2111 ECO-only seed | 1 | 1 |
| Total | 17 | 140 |

The original 140 comprise 134 machine rows and six historical NEW rows. All six
historical proposals retain their source payload, order, NEW action and retirement
state. Eight new proposals were authored in the expansion: three ACIAD molecular
functions; CAUVC CC_3705 carrier, localization process and periplasm claims; and
FLAJ1 Fjoh_1066 localization process and outer-membrane-face claims. All eight are
active. There are 148 final rows and no proposal retirements. Exact proposal
payloads and indices are recorded in `receipt.json` rather than reconstructed
from counts. All 17 reviews are COMPLETE.

The union of baseline-protected files is 67 (53 original, 12 additional seeds,
two Fjoh_2111 raw files). Every hash matches. Eight frozen manifests also match:
ECOLI 29 files, PSEPK 36, ACIAD 31, cross-lineage 19, Fjoh_2111 17, families 21,
module 14 and capacity 11. The capacity receipt additionally closes 276 input
hashes. The verified family receipt preserves 12 ordered PAINT assertions in
three family reviews; this consultation does not independently re-adjudicate
those evolutionary placements.

`required-ignored-provenance.json` names exactly nine additional provenance files.
All nine exist and match their required hashes. They have not been moved,
modified or staged here. Their later exact publication remains a root-owned
requirement; presence on disk is not a claim that they are committed.

## Objective coverage and evidence boundaries

The module has 17 adjudicated references, including three reviews
(PMID30900542, PMID42023066, PMID40536045). The panel spans E. coli K-12,
P. putida KT2440, A. baylyi ADP1, C. crescentus CB15 and F. johnsoniae UW101.
The frozen source closure checks 186 quotations (178 review/module quotations
plus eight boundary excerpts), with no skipped quote or reported error.

The verified capacity receipt records 32 production-compiler scenarios, five
mutations of the actual module, and five evidence-gate sensitivity tests. This
consultation verifies their outputs and all frozen input hashes; it does not
rerun scripts that write into released directories. The controls cover complete
ECOLI/PSEPK/ACIAD panels, missing activities, C/E versus F2 architecture, same-
protein bifunctionality, specificity, compatibility and construct boundaries.

- ECOLI provides experimentally grounded canonical CDE extraction and A/B delivery.
  PSEPK is a matched ortholog-based inference, not relabeled E. coli experiments.
- ACIAD supports native F2D2 extraction and defined single-cycle transfer to LolA;
  terminal LolB function is inferred. The reviewed lolC locus is the paper's LolF;
  identical accession aliases do not create two genes. LolD belongs to verified
  PTHR42798:SF2, not PTHR24220; this is a bounded member descriptor, not a newly
  reviewed whole-family grant.
- FLAJ1 supplies a supported carrier/DUF4292-insertase pair, not a reviewed full
  extractor panel or universal client coverage. LolA2 pigment-context membership
  is not treated as measured loss of carrier activity.
- CB15 bifunctionality remains construct-bounded inference: the study tested an
  altered C-terminal tail in permissive heterologous backgrounds. It does not
  establish an entire native CB15 pathway.
- PTHR24220/30489/35869 family judgments preserve broader ABC knowledge and named
  positive anchors. Shared subfamilies alone do not identify C versus E, select
  cargo, establish insertion, or license all LolA paralogs. Classical LolB uses
  verified TIGR00548; distant Bacteroidota LolB has distinct domain evidence.
- The compiler evaluates the Boolean module, while external evidence predicates
  supply active-unit assembly, partner compatibility, exact curated roles and
  proposed insertion activity. Negative canonical results mean unlicensed
  capacity, not universal biological impossibility. Conditional LolDE release
  and the cpxA24/Δlpp/ΔrcsB LolAB bypass remain positive out-of-model controls.

## Pending integration and limits

The module's curated status is COMPLETE, but no whole-corpus PASS is claimed.
ECO-only source-code dependency `2564a3fb412d7a561ca8fd165128294e2e496016` is not
integrated into this Lol worktree. Its full run 92793 was pending at root's task
handoff. Ordinary Lol validation cannot accept the preserved literal
ECO:0007744 row until that dependency is integrated. The existing Fjoh_2111
receipt records the byte-identical isolated validation overlay and its limits;
this consultation preserves that receipt and does not substitute a GO evidence
code. Root owns dependency integration, ordinary final validation, member-index
closure where needed, exact provenance publication and any full-corpus run.

Ruff and the independent preservation checker pass. No gene, module, family,
project, cache, prior history or prior receipt was edited; no full run, commit,
staging or push was performed.
