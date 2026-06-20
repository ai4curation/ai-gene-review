---
title: "PANTHER IBA family review — reviewed S. pombe genes"
---

# PANTHER IBA family review — reviewed S. pombe genes

Family-level review of the **Inferred from Biological Ancestor** (IBA;
ECO:0000318, `GO_REF:0000033`) annotations on the 40 S. pombe genes curated in
the two pombe batches. IBAs are produced by GO Consortium **PAINT** curators
propagating experimental annotations across **PANTHER** family trees, so the
right place to judge them is the family/subfamily, not the individual gene.

## Method (reproducible)

`extract_iba_propagation.py` reconstructs every IBA propagation from cached repo
data only (nothing hardcoded):

* the GOA `with/from` field gives the ancestral PANTHER node (`PTN…`) and the
  **seed genes** (experimentally annotated relatives that justified the IBA);
* each gene's PANTHER family + subfamily is read from its `*-uniprot.txt`;
* each UniProt seed is mapped to its subfamily via the cached
  `interpro/panther/<FAM>/<FAM>-entries.csv` member table;
* a propagation is flagged `CROSS_SUBFAMILY` when **no** seed shares our gene's
  subfamily (i.e. the function came only from sibling subfamilies),
  `LOCALIZATION` for cellular-component terms (which transfer worst across
  trees), `GENE_NO_SUBFAMILY` / `NO_UNIPROT_SEEDS` where mapping is incomplete.

Output: `iba_propagation.tsv` (one row per IBA, with our curation action joined).

```
IBA annotations analyzed: 151
  with UniProt seeds mappable to subfamilies: 83
  CROSS_SUBFAMILY (seeds only from other subfamilies): 33
```

## The big caveat: `CROSS_SUBFAMILY` is triage, not a verdict

PANTHER subfamilies are very fine-grained, and true orthologs in different
species routinely land in different SFs. So the flag has a **high false-positive
rate** for broadly conserved functions. Among the 33 cross-subfamily hits, most
are unambiguously correct and were (correctly) ACCEPTed:

| Gene | IBA term | Why the flag is a false positive |
|------|----------|----------------------------------|
| cdc2 | cyclin-dependent protein kinase holoenzyme | Cdc2 *is* the founding CDK; seeds are CDKs in sibling SFs |
| plo1 | protein Ser/Thr kinase activity | Polo kinase; activity conserved family-wide |
| rad3 | protein Ser/Thr kinase activity; DNA damage checkpoint | Rad3/ATR; conserved PIKK function |
| ste11 | dbTF activity; RNA Pol II cis-reg DNA binding | Ste11 HMG TF; genuinely a transcription factor |
| slp1 | anaphase-promoting complex binding | Slp1/Cdc20; correct |
| cdc18 | DNA replication origin binding/initiation | Cdc18/Cdc6; correct |
| cnp1 | kinetochore assembly | Cnp1/CENP-A; correct |
| cut7 | spindle microtubule | Kinesin-5; correct |

So the family lens **confirms our per-gene calls were sound** rather than
overturning them — and it did **not** surface additional genuine errors among
the ACCEPTed IBAs.

## Confirmed over-propagations (the genuine errors)

The flag's true positives line up exactly with the three IBAs we removed/flagged
by hand, now substantiated at the family level:

### 1. pom1 — `cytoskeleton` (GO:0005856) → REMOVE ✓
- Family **PTHR24058** (dual-specificity kinases); pom1 = **SF132** (DYRK-family kinase Pom1).
- Node `PTN008603465`; the only mappable UniProt seed is human **DYRK3 (SF35)**.
- "Cytoskeleton" is a DYRK3-subfamily property, not a Pom1/SF132 function — Pom1
  is a cortical/plasma-membrane kinase. Cross-subfamily transfer of a
  localization term. **Over-propagation confirmed.**

### 2. rqh1 — `cytoplasm` (GO:0005737) → REMOVE ✓
- Family **PTHR13710** (RecQ helicases); rqh1 = **SF153** (RecQ-like helicase BLM).
- Seeds only from **SF105 / SF152** (other RecQ subfamilies).
- Rqh1 is experimentally nuclear; a sibling-subfamily cytoplasm localization
  transferred onto it. **Over-propagation confirmed.**

### 3. mid1 — `septin ring organization` (GO:0031106) → REMOVE (nuanced)
- mid1 has no PANTHER subfamily tag in UniProt (`GENE_NO_SUBFAMILY`), so the SF
  test could not fire. The `with/from` node is `PTN001853010`, seeded by
  *Drosophila* anillin (`FB:FBgn0261385`), *C. elegans* anillin
  (`WB:WBGene00013038`), and **mid1 itself** (`PomBase:SPCC4B3.15` is mid1's own
  ORFName — *not* mid2, contrary to a first draft of this note).
- "Septin ring organization" is a genuine **ancestral anillin** function (the
  metazoan seeds really do organize septins), so at the family level the
  propagation is not spurious. The issue is pombe-specific **sub-functionalization**:
  the two pombe anillins split the job — **mid2** organizes the septin ring,
  while **mid1** positions the actomyosin ring — so the ancestral term does not
  describe mid1's retained role.
- The mid1 leaf in `with/from` traces to mid1's own experimental septin-ring
  annotation, i.e. the IMP from PMID:15385632 — whose **full text** (cached) we
  checked and found contains 0 mid1 / 6 mid2 mentions. That IMP REMOVE is solid;
  the IBA REMOVE is the weaker, sub-functionalization-based call (KEEP_AS_NON_CORE
  would also be defensible for the IBA alone).

## A discrimination the family lens adds: "MAPK cascade"

Two genes carry an IBA to `MAPK cascade` (GO:0000165) and we gave **opposite**
actions — the family review shows both are correct:

- **wis1 → ACCEPT.** Wis1 is the MAP2K (Pbs2 ortholog) of the Sty1 SAPK
  cascade; "MAPK cascade" is its actual biology.
- **cdc7 → MARK_AS_OVER_ANNOTATED.** Cdc7 is the SIN initiating kinase; the SIN
  is a GTPase-regulated kinase relay, *not* a MAPK cascade. The term is
  over-propagated from STE-family relatives.

## Bottom line

- 151 IBAs reviewed at the family level. Two clean over-propagations (**pom1**
  cytoskeleton, **rqh1** cytoplasm — localization terms crossing subfamilies) and
  one **sub-functionalization** case (**mid1** septin ring, where the ancestral
  anillin function partitioned to mid2 in pombe). All three were already caught
  in per-gene curation; the family lens substantiates the localization cases and
  reframes mid1 as sub-functionalization rather than a clean mis-attribution.
- No additional IBA errors were found among the ACCEPTed annotations; the
  remaining cross-subfamily flags are conserved functions (false positives of a
  deliberately sensitive flag).
- The recurring true-positive pattern is **localization terms** and
  **paralog-specific functions** crossing subfamily boundaries — the two things
  to scrutinize hardest in any IBA.

## Files
- `extract_iba_propagation.py` — reproducible extractor/flagger.
- `iba_propagation.tsv` — per-IBA table (node, seeds, subfamilies, our action, flags).
