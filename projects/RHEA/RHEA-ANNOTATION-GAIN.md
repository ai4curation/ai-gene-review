---
title: "RHEA->GO Mapping: UniProt Propagation Gain"
---

# UniProt Propagation Gain from the Curated RHEA->GO Mappings

**Parent project:** [RHEA.md](../RHEA.md) - **Mappings:** [rhea2go.sssom.yaml](rhea2go.sssom.yaml) - **Script:** [rhea_annotation_gain.py](rhea_annotation_gain.py)

If the curated RHEA->GO mappings were added to `rhea2go` and propagated, how many GO
molecular-function annotations would UniProtKB **gain**? For each mapping we count entries that
carry the RHEA reaction but do not already have the mapped GO term
(`gain = N(rhea) - N(rhea AND go)`, via the UniProt `x-total-results` count API). UniProt's `go:`
query is **closure-aware** (term + descendants), so entries already carrying a more specific
child are excluded.

## Headline

| Scope | New GO MF annotations |
|-------|----------------------:|
| **All of UniProtKB** | **25,842** |
| Reviewed (Swiss-Prot) only | 34 |

Across 111 GO-bearing mappings (85 with non-zero gain). The reviewed-only number is
tiny because curated enzymes carrying the reaction almost always already have the term (manual
curation / EC2GO) -- the EC-masking result at the annotation level. **Essentially all the value
is bulk propagation into the unreviewed (TrEMBL) proteome.**

## Top contributors

| RHEA | GO term | UniProt gain | carry reaction | already have |
|------|---------|-------------:|---------------:|-------------:|
| RHEA:48564 | GO:0102682 cytokinin riboside 5'-monophosphate phosphoribohydrolase activity | 8,360 | 12,260 | 3,900 |
| RHEA:85243 | GO:0003960 quinone reductase (NADPH) activity | 4,995 | 7,686 | 2,691 |
| RHEA:36079 | GO:0002950 ceramide phosphoethanolamine synthase activity | 2,831 | 3,020 | 189 |
| RHEA:49072 | GO:0018640 dibenzothiophene monooxygenase activity | 2,450 | 2,520 | 70 |
| RHEA:37667 | GO:0008376 acetylgalactosaminyltransferase activity | 1,047 | 1,133 | 86 |
| RHEA:18113 | GO:0004550 nucleoside diphosphate kinase activity | 645 | 26,755 | 26,110 |
| RHEA:59468 | GO:0036374 glutathione gamma-glutamate hydrolase | 340 | 19,401 | 19,061 |
| RHEA:17377 | GO:0004169 dolichyl-phosphate-mannose-protein mannosyltransferase activity | 287 | 9,487 | 9,200 |
| RHEA:67012 | GO:0004484 mRNA guanylyltransferase activity | 257 | 5,796 | 5,539 |
| RHEA:33751 | GO:0008962 phosphatidylglycerophosphatase activity | 250 | 7,072 | 6,822 |
| RHEA:24670 | GO:0004854 xanthine dehydrogenase activity | 244 | 3,399 | 3,155 |
| RHEA:41792 | GO:0004314 [acyl-carrier-protein] S-malonyltransferase activity | 214 | 26,077 | 25,863 |
| RHEA:53428 | GO:0003908 methylated-DNA-[protein]-cysteine S-methyltransferase activity | 200 | 30,118 | 29,918 |
| RHEA:67008 | GO:0004482 mRNA 5'-cap (guanine-N7-)-methyltransferase activity | 191 | 5,811 | 5,620 |
| RHEA:63644 | GO:0046922 peptide-O-fucosyltransferase activity | 186 | 5,270 | 5,084 |

## Caveats

- Gain **inherits the reliability of each TrEMBL entry's RHEA annotation** (often a UniRule/ARBA
  inference); it is "annotations that would be created", not verified facts.
- broadMatch rows propagate a broader term; a root-level broadMatch should not be propagated as-is.
- The 7 `sssom:NoTermFound` new-term rows contribute 0 here; they enable a separate gain once the
  proposed GO terms are created.

## Reproduce

```bash
uv run python rhea_annotation_gain.py
```
