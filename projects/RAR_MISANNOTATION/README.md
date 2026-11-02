# RAR misannotation re-examination: data and scripts

Supporting material for [RAR_MISANNOTATION](../RAR_MISANNOTATION.md).

| File | What it is |
|---|---|
| `scripts/parse_supplement.py` | Downloads the authors' supplement (`https://zhanggroup.org/RAR/SI.pdf`) to the git-ignored `.cache/rar/` and rebuilds Supplementary Tables S3–S6 from word positions. |
| `scripts/check_current_goa.py` | Looks up every protein–term pair in current GOA (QuickGO API) and UniProt. |
| `data/rar_supplement_cases.yaml` | The 93 flagged term rows (43 for 2019-06-03, 50 for 2018-11-06) with all 440 protein–term pairs. |
| `data/rar_current_status.yaml` | Per pair: organism, UniProt status, whether GOA still has the annotation, and with what evidence. |

Run from the repository root:

```bash
uv run python projects/RAR_MISANNOTATION/scripts/parse_supplement.py
uv run python projects/RAR_MISANNOTATION/scripts/check_current_goa.py
```

## How the tables are reconstructed

The supplement is a PDF with tall, vertically centred cells, so plain text
extraction does not say which example protein belongs to which row. The parser
uses poppler `pdftotext -bbox` word positions and:

1. finds each row by its GO id and its fixed number of per-taxon counts;
2. cuts the example-protein column into one run per row by dynamic
   programming, so that each run is centred on its row's GO id and every
   protein (by UniProt lineage) comes from a taxon whose annotation rate is at
   most 0.2 of that row's top rate. The per-taxon protein totals needed for
   rates are back-calculated from rate ratios the paper prints (see the
   comments in the script).

The result matches the paper's Table 1 exactly (2019: 109 kingdom + 81 phylum
annotations on 100 + 81 proteins; 2018: 170 + 80 on 153 + 80). Accessions that
UniProt has since deleted have no lineage and only the layout places them.

The supplement's footnote gives the kingdom count order as Animals, Archaea,
Bacteria, Fungi, Plants; the column header and the data say Archaea, Animals,
Bacteria, Fungi, Plants, and the latter is used.

GOA status is a snapshot: rerunning `check_current_goa.py` later will change it.
The authors' "full dataset" download (`full.zip`) returns 404, so per-pair
evidence codes from 2018–19 are not available; only each row's most frequent
code is.
