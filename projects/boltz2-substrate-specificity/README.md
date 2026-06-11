# Boltz-2 substrate-specificity scaffold

Reproducible scaffold for ranking candidate enzyme substrates by Boltz-2 predicted
binding affinity. See [`../BOLTZ2_SUBSTRATE_SPECIFICITY.md`](../BOLTZ2_SUBSTRATE_SPECIFICITY.md)
for the full rationale, scope, and **limitations** (read these before interpreting any output).

> **Honesty note:** Boltz-2 inference requires a GPU and downloads multi-GB weights. These scripts
> only *prepare inputs* and *parse outputs*; they do **not** run the model. They were authored in a
> CPU-only environment, so no predictions have been run here. Run `boltz predict` yourself on a GPU.
>
> Boltz-2 affinity is trained on **inhibitor/binder** data. It scores **binding**, which is a proxy
> for — not proof of — being a catalytic **substrate**. Treat results as hypothesis-generating, and
> always confirm the predicted pose sits in the catalytic pocket. Compare candidates only within one
> enzyme (affinity is relative, not absolute).

## Steps

```bash
# 0. Install Boltz-2 (on a GPU machine)
pip install boltz            # or: uv add boltz

# 1. Generate one input YAML per candidate substrate
python generate_inputs.py \
    --protein-id ENZ \
    --sequence-file enzyme.fasta \
    --panel example_panel.tsv \
    --outdir boltz_inputs

# 2. Run Boltz-2 over the panel (GPU; --use_msa_server auto-builds MSAs)
boltz predict boltz_inputs --use_msa_server --out_dir boltz_out

# 3. Rank candidates by predicted affinity
python rank_affinity.py --results boltz_out --tsv ranked.tsv
```

## Output columns (`ranked.tsv`)

| Column | Meaning |
|---|---|
| `log10_IC50_uM` | Boltz-2 `affinity_pred_value`; **lower = stronger** predicted binding |
| `binder_prob`   | Boltz-2 `affinity_probability_binary`; **higher = more binder-like** (binder vs decoy) |

## Recommended first run: controls

Before questioning any curated annotation, run the pipeline on enzymes with **experimentally known
substrates and known non-substrates** and confirm Boltz-2 recovers the known ordering (the decoy
should rank worst). If it cannot, do not use it to challenge GO annotations. Record outcomes — even
inconclusive ones — honestly; never hardcode expected results.
