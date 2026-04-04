# Benchmark Data

Place Mordret et al. benchmark or supplement tables here.

## Raw inputs

Store untouched downloads in `raw/`.

## Normalized inputs

The evaluation code expects a tab-delimited file with these columns:

- `protein_id`
- `is_defense`
- `family`
- `is_novel`

Optional columns such as `split`, `contig`, or `genome_id` can be retained, but the evaluator only requires the four fields above.

## Normalization workflow

Example:

```bash
just normalize-benchmark \
  input=benchmark/raw/mordret_supplement.tsv \
  output=benchmark/normalized/mordret_benchmark.tsv \
  protein_id_column=protein_id \
  label_column=is_defense \
  family_column=family \
  novel_column=is_novel
```

If the final *Science* supplement uses different column names, pass those names explicitly.
