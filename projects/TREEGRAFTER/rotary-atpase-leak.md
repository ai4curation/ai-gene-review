# ATP-synthase terms leaking onto flagellar and T3SS export ATPases

**Part of [TreeGrafter Inference Evaluation](../TREEGRAFTER.md).** Opened 2026-09-27.

## Bottom line

- **Almost every FliI / SctN protein in UniProt is annotated as an ATP synthase.**
  These are the ATPases that power flagellar and injectisome (type III) protein
  export. They are paralogs of the F1-ATP synthase β subunit, and they hydrolyse ATP
  rather than make it. Of the 11,205 UniProtKB entries in their family (InterPro
  IPR005714), 97% carry `GO:0046933` *proton-transporting ATP synthase activity,
  rotational mechanism* and 97% carry `GO:0015986` *proton motive force-driven ATP
  synthesis*. Among the 29 reviewed Swiss-Prot entries, all 29 carry `GO:0015986`
  and 20 carry `GO:0046933` ([counts](rotary_atpase/fliI_sctN_go_counts.tsv)).
- **One misplaced PAINT node explains the synthase terms.** Both IBDs (for
  `GO:0046933` and `GO:0045259` *proton-transporting ATP synthase complex*) sit on
  `PANTHER:PTN008558586` in PTHR15184. In the live PANTHER tree that node is a
  **duplication**. Its two children are the F1-β clade `PTN008558588`, which holds
  every seed, and the FliI/SctN export-ATPase clade `PTN000390097` (SF9 SPI-1, SF62
  SPI-2, SF81 flagellar) ([placement](rotary_atpase/node_placement.tsv)).
  - PAINT IBA passes `GO:0046933` to 28 proteins with the FliI/SctN signature
    IPR005714 in the reference genomes, plus a *Chlamydia* FliI (O84722) that lacks
    the signature ([targets](rotary_atpase/ptn008558586_iba_targets.tsv)). They
    include *Salmonella* FliI, InvC and SsaN and *E. coli* FliI.
  - TreeGrafter then passes `GO:0046933` to every grafted FliI/SctN. All five graft
    nodes seen in our reviews descend from `PTN000390097`.
  - The IBD was placed one node too deep. TreeGrafter faithfully reproduces the
    error rather than causing it.
- **Two more pipelines add errors of their own:**
  - InterPro2GO maps the **SctN-specific** entry IPR013380 to `GO:0046961` *proton-
    transporting ATPase activity, rotational mechanism* and to `GO:0006754` *ATP
    biosynthetic process*.
  - It maps the shared F1/V1/A1 N-terminal domain IPR004100 to `GO:1902600` *proton
    transmembrane transport* and `GO:0046034` *ATP metabolic process*.
  - GO's logical inference (`GO_REF:0000108`) then turns each wrong molecular
    function into a wrong process: `GO:0046933` → `GO:0015986` and `GO:0046961` →
    `GO:1902600`.
- **Nine full reviews reject every such row:** 35 rows, 31 REMOVE and 4
  MARK_AS_OVER_ANNOTATED, with none accepted
  ([per-row table](rotary_atpase/review_actions.tsv)).

## How this was found

It came out of a first-principles completeness test. A process every organism
needs gives an independent truth set: "does this proteome encode a complete F-type
ATP synthase?". The test asks how well plain GO annotation recovers it
([`completeness_*.py`](rotary_atpase/), [results](rotary_atpase/completeness_results.txt)).

- **Proteomes:** 15,525 bacterial reference proteomes with BUSCO completeness ≥ 95%.
  Of these, 14,959 encode all eight F-type subunit families.
- **Accuracy:** "has a `GO:0046933` protein" scores precision 0.967 and recall 0.976
  against that truth.
- **False negatives:** new TrEMBL entries that have InterPro cross-references but no
  GO annotations yet.
- **False positives:** mostly V/A-type ATPases and FliI/SctN. The FliI/SctN false
  positives are genuine annotation errors, and they are the subject of this page.
- **Genuine absences:** the complex is missing from phytoplasmas, and V/A-type
  ATPases replace it in many Clostridia, Spirochaetia and Bacteroidota.

## Why the terms are wrong

The reviews give the evidence with verbatim quotes. In brief:

- **FliI/SctN are hydrolases.** They are soluble, peripheral ATPases that dock
  export chaperone–substrate complexes, release the chaperones, and unfold and hand
  on the substrates. Their EC is 7.4.2.8, protein-secreting ATPase.
- **FliI's ATPase is not an F-type activity.** It is insensitive to inhibitors of
  F-, V- and P-type ATPases (PMID:8943245).
- **Protons move through the export gate, not the ATPase.** The export apparatus
  does use the proton motive force, but the flux runs through the membrane export
  gate, a proton–protein antiporter whose *Salmonella* `FlhA` subunit acts as the ion channel (PMID:21934659,
  PMID:29946050). CCCP sensitivity of Ysc secretion reflects this (PMID:15213145),
  not proton transport by SctN.
- **The resemblance to F1 is real but does not make them synthases.** FliJ/SctO is
  γ-stalk-like, and the FliI₆–FliJ ring resembles F1 (PMID:21278755, PMID:17202259).
  But the ring still hydrolyses ATP and has no Fo sector to couple to.

## Reviews

| Review | Protein | Rows that carry the error | Source nodes / signatures |
|---|---|---|---|
| CAUVC/fliI | *Caulobacter* FliI P0CAT8 | TreeGrafter, InterPro2GO, logical inference | PTN000390110; IPR004100 |
| HELPJ/fliI | *H. pylori* J99 FliI Q9ZJJ3 | TreeGrafter, logical inference | PTN002689426 |
| PSEPK/fliI | *P. putida* FliI Q88ET7 (pre-existing) | TreeGrafter, logical inference | PTN002309653 |
| ECOLI/fliI | *E. coli* FliI P52612 | PAINT IBA ×2, logical inference | PTN008558586 |
| SALTY/fliI | *Salmonella* FliI P26465 | PAINT IBA ×2, logical inference | PTN008558586 |
| SALTY/sctN1 | *Salmonella* InvC P0A1B9 | PAINT IBA ×2, InterPro2GO, logical inference | PTN008558586; IPR004100 |
| SALTY/sctN2 | *Salmonella* SsaN P74857 | PAINT IBA ×2, InterPro2GO, logical inference ×2 | PTN008558586; IPR013380 |
| YEREN/sctN | *Yersinia* YscN P40290 | TreeGrafter, InterPro2GO, logical inference | PTN001807733; IPR013380, IPR004100 |
| SHIFL/sctN | *Shigella* Spa47 P0A1C1 | TreeGrafter, InterPro2GO, logical inference | PTN001807734; IPR004100 |

**Actions by pipeline:**

| Pipeline | REMOVE | MARK_AS_OVER_ANNOTATED |
|---|---:|---:|
| GO logical inference (`GO_REF:0000108`) | 10 | 0 |
| InterPro2GO (`GO_REF:0000002`) | 8 | 4 |
| PAINT IBA (`GO_REF:0000033`) | 8 | 0 |
| TreeGrafter (`GO_REF:0000118`) | 5 | 0 |

- **The four over-annotations** are all `GO:0046034` *ATP metabolic process*. It is
  literally true of an ATPase but adds nothing beyond `GO:0016887`.
- **What replaces the wrong terms.** The correct molecular function, `GO:0008564`
  *protein-exporting ATPase activity*, is kept where it was already in GOA and
  added (NEW) where it was missing.

**Other errors the reviews found along the way:**

- **UniProt naming.** The flagellar FliI entries (P26465, P52612, P0CAT8, Q9ZJJ3)
  are named "Flagellum-specific ATP synthase" with **EC 7.1.2.2**, the
  H⁺-transporting synthase EC, and keep a 1991 "proton translocase" hypothesis in
  their FUNCTION text (PMID:1646201). The injectisome SctN entries already use
  EC 7.4.2.8.
- **SsaN host-cell locations.** Two AgBase IMP rows place SsaN in *host cell
  cytoplasm* and *host cell membrane*. The paper fractionates bacterial cells, and
  the effector, not the ATPase, is what reaches the host (see
  SALTY/sctN2).

## Where this sits among the TreeGrafter failure modes

- **Unlike most of the failure modes**, this is not a problem with the term attached
  to the graft node, nor a mis-graft. The TreeGrafter placements are correct: every
  graft node is inside the FliI/SctN clade.
- **The error comes in from PAINT.** The ancestral IBD sits on the duplication node,
  so it covers both paralog clades. This is a fifth pattern: **inherited PAINT
  over-placement**. Fixing the IBD fixes the TreeGrafter output with no change to
  TreeGrafter.
- **Earlier reviews did not catch it.** The PTHR15184 family review
  (`interpro/panther/PTHR15184/PTHR15184-review.yaml`) had rated the `PTN008558586`
  assertions SOUND, having checked the node against its F1-β descendants only. It
  now records both as **TOO_DEEP**, lists SF9, SF62 and SF81 as diverged
  subfamilies, and scopes `GO:0046933` to the F1-β subfamilies and `GO:0008564` to
  the export-ATPase subfamilies (updated 2026-09-27).
- **In the headline figures since 2026-10-01.** All five TreeGrafter rows (`fliI`
  in CAUVC, HELPJ and PSEPK; `sctN` in SHIFL and YEREN) are in the main page's
  tables refreshed at `943b98815`, all `REMOVE`. In its four-mode classification
  they are filed as mode 1 by the operational rule there (correct subfamily,
  wrong term from a node above it); this page identifies that node term as an
  inherited PAINT IBD.

## Suggested upstream fixes

1. **PANTHER/PAINT:** move the `GO:0046933` and `GO:0045259` IBDs from
   `PTN008558586` to `PTN008558588`, or add an IRD/NOT at `PTN000390097`. This one
   change fixes both the IBA rows and every TreeGrafter row.
2. **InterPro2GO:**
   - Drop `GO:0046961` and `GO:0006754` from IPR013380. That entry is SctN-specific,
     so the mapping is wrong for every member.
   - Suppress IPR004100 → `GO:1902600` / `GO:0046034` when IPR005714 also matches.
   - Drop the stale IPR005714 → `GO:0009058` *biosynthetic process* mapping.
   - All five are recorded in the [InterPro mapping review](../INTERPRO.md)
     ([mapping set](../INTERPRO/interpro2go.sssom.yaml)).
3. **UniProt:** rename the flagellar FliI entries to a flagellar export ATPase, use
   EC 7.4.2.8, and drop the "proton translocase" clause.

## Reproduce

```bash
uv run --with requests projects/TREEGRAFTER/rotary_atpase/leak_scan.py          # UniProt counts + PTN008558586 IBA targets
uv run --with requests projects/TREEGRAFTER/rotary_atpase/node_placement.py     # PANTHER tree placement of IBD and graft nodes
uv run --with pyyaml   projects/TREEGRAFTER/rotary_atpase/review_actions.py     # per-row reviewer actions from the gene reviews
uv run --with requests projects/TREEGRAFTER/rotary_atpase/completeness_fetch.py # bacterial F-type completeness (large; to ./cache)
python3 projects/TREEGRAFTER/rotary_atpase/completeness_analyze.py > projects/TREEGRAFTER/rotary_atpase/completeness_results.txt
```

The UniProt, QuickGO and PANTHER queries run against live services, so the counts
will drift between releases. The committed TSVs were generated on 2026-09-27.
