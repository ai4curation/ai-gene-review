# Reproducing EIF2AK4 propagation evidence

This package reproduces six PAINT ancestral joins, 29 exact-term ortholog-donor joins and all 144 condition sets of ARBA00028884. It computes source relationships, not curation actions or experimental conclusions.

Use Python 3.9 or later with the standard library. Place the seven external files named in `inputs.json` in an input directory, using the exact recorded versions, then run:

```bash
python reproduce.py --input-dir /path/to/saved-inputs --output-dir /path/to/new-results
```

The output directory must not already exist. Every input is checked against its byte count and SHA256 before parsing. The program performs no network requests. The manifest records official retrieval URLs, but the live services may return newer data; a live version that differs from the recorded snapshot is rejected rather than silently substituted. `source-contexts.json` is bundled and retains the imported assertions without review decisions.

`paint.json`, `donor-joins.json` and `arba.json` are the recorded outputs. The parser rebuilds them from the raw tree, alignment, IBD table, donor annotation responses and rule, without using these outputs as computation inputs. Exact target sequence agreement is checked against UniProt. All target-lineage records are exposed, not only successful term joins. Complete donor-response counts are checked before selecting exact terms. ARBA negative conditions and taxon conditions are evaluated where present; the three matching sets use InterPro/FunFam evidence.

Large upstream tree/alignment/IBD files and article bodies are not bundled. [RESULTS.md](RESULTS.md) explains the evidence boundaries. Source/version hashes and official URLs are in `inputs.json`; source-paper assay and access scopes are in the [gene source guide](../EIF2AK4-source-guide.md).
