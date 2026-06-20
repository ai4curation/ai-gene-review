---
title: "RHEA->GO Mapping: Annotation Gain from Propagation"
---

# Annotation Gain from the Curated RHEA->GO Mappings

**Parent project:** [RHEA.md](../RHEA.md) - **Mappings:** [rhea2go.sssom.yaml](rhea2go.sssom.yaml) - **Script:** [rhea_annotation_gain.py](rhea_annotation_gain.py)

If the curated RHEA->GO mappings were added to `rhea2go` and propagated, how many GO
molecular-function annotations would be **gained**? For each mapping we count UniProtKB entries
that carry the RHEA reaction but do **not** already have the mapped GO term
(`gain = N(rhea) - N(rhea AND go)`, via the UniProt `x-total-results` count API). UniProt's
`go:` query is **closure-aware** (term + descendants), so entries already carrying a more
specific child are excluded -- this is a closure-filtered estimate.

## Headline

| Scope | New GO MF annotations gained |
|-------|------------------------------|
| **All of UniProtKB** | **9,325** |
| **Reviewed (Swiss-Prot) only** | **23** |

Across 71 GO-bearing mappings (45 with non-zero gain).

## The split is the finding

Almost all the gain is in **TrEMBL (unreviewed)**: only **23** reviewed annotations would be
added, versus **9,325** across all of UniProtKB. This is the [EC-masking](RHEA-EC-SPECIFICITY.md)
result at the annotation level -- reviewed enzymes carrying the reaction almost always **already
have** the GO term (from manual curation or EC2GO), so RHEA is redundant there; the unreviewed
proteome is where the reaction is annotated but the activity term is missing. The mapping is
therefore mainly a **bulk TrEMBL gap-filler**, with a small, high-confidence reviewed-curation
tail.

## Top contributors (all-UniProtKB gain)

| RHEA | GO term | gain (all) | N(rhea) | already have | gain (reviewed) |
|------|---------|-----------:|--------:|-------------:|----------------:|
| RHEA:36079 | GO:0002950 ceramide phosphoethanolamine synthase activity | 2,831 | 3,020 | 189 | 6 |
| RHEA:49072 | GO:0018640 dibenzothiophene monooxygenase activity | 2,450 | 2,520 | 70 | 5 |
| RHEA:37667 | GO:0008376 acetylgalactosaminyltransferase activity | 1,047 | 1,133 | 86 | 0 |
| RHEA:17377 | GO:0004169 dolichyl-phosphate-mannose-protein mannosyltransferase activity | 287 | 9,487 | 9,200 | 0 |
| RHEA:67012 | GO:0004484 mRNA guanylyltransferase activity | 257 | 5,796 | 5,539 | 0 |
| RHEA:33751 | GO:0008962 phosphatidylglycerophosphatase activity | 250 | 7,072 | 6,822 | 0 |
| RHEA:24670 | GO:0004854 xanthine dehydrogenase activity | 244 | 3,399 | 3,155 | 0 |
| RHEA:41792 | GO:0004314 [acyl-carrier-protein] S-malonyltransferase activity | 214 | 26,077 | 25,863 | 0 |
| RHEA:67008 | GO:0004482 mRNA 5'-cap (guanine-N7-)-methyltransferase activity | 191 | 5,811 | 5,620 | 0 |
| RHEA:23956 | GO:0004653 polypeptide N-acetylgalactosaminyltransferase activity | 181 | 9,641 | 9,460 | 0 |
| RHEA:48940 | GO:0016805 dipeptidase activity | 144 | 8,702 | 8,558 | 0 |
| RHEA:18021 | GO:0047288 beta-D-galactosyl-(1->3)-N-acetyl-beta-D-galactosaminide alpha-2,3- sialyltransferase activity | 132 | 3,228 | 3,096 | 0 |
| RHEA:16573 | GO:0004648 O-phospho-L-serine:2-oxoglutarate transaminase activity | 125 | 16,156 | 16,031 | 0 |
| RHEA:26422 | GO:0004062 aryl sulfotransferase activity | 120 | 120 | 0 | 5 |
| RHEA:13493 | GO:0004455 ketol-acid reductoisomerase activity | 118 | 16,976 | 16,858 | 0 |

The top 3 reactions (CPE synthase, dibenzothiophene monooxygenase, the B3GALNT2 broadMatch)
account for most of the total.

## Caveats

- **Gain inherits the reliability of each entry's RHEA annotation.** Many TrEMBL RHEA
  annotations are themselves UniRule/ARBA inferences, so a propagated GO term is only as good
  as that upstream call. The reviewed-only number is the trustworthy floor.
- **broadMatch rows propagate a broader term** (e.g. PHYKPL->`lyase activity`, B3GALNT2->
  `acetylgalactosaminyltransferase activity`); their gain is real but lower-value than a
  specific exactMatch term, and a root-level broadMatch should not be propagated as-is.
- **The 7 `sssom:NoTermFound` new-term rows contribute 0 here** (no GO object); they would
  enable a separate gain once the proposed GO terms are created.

## Reproduce

```bash
uv run python rhea_annotation_gain.py            # all mappings
uv run python rhea_annotation_gain.py --reviewed-only
```
