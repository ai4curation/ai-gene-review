# Publisher figure provenance

PMID27118128 Figure 1 was inspected at the public Springer Nature figure endpoint identified by the article landing page. The image is not bundled here. `provenance.json` retains its exact URL, retrieval date and SHA256; a fresh retrieval on 2026-11-06 reproduced the recorded hash.

Visual inspection shows CASDC (BT_0674) on the solid carboxyspermidine-to-spermidine arrow and CASDH (BT_4612) on a dotted arrow. The full article remains subscription-only. This observation resolves locus identity; the cached abstract independently supplies the reported genetic and decarboxylase-activity results. The image is not a computational input to the module capacity checker.

To reproduce the source lookup without adding the image to the repository:

```bash
uv run python genes/BACTN/BT_0674/BT_0674-source-analysis/fetch_figure.py .cache/PMID27118128-figure1.gif
```

The helper verifies the recorded hash and refuses to overwrite a different existing file.
