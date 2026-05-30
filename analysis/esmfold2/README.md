# ESMFold2 (Biohub) complex caller

ESMFold2 counterpart to the BioLM Boltz2 callers used elsewhere under `analysis/`.
Background and the decision to evaluate ESMFold2 are in
[`projects/PROTEIN_COMPLEX_FUNCTIONS.md`](../../projects/PROTEIN_COMPLEX_FUNCTIONS.md)
(2026-05-29 NOTES entry).

ESMFold2 is the structure/interaction model in Biohub's protein "world model"
(formerly EvolutionaryScale / Forge). It predicts multi-chain complexes, reports
`pLDDT`/`pTM`/`ipTM`, is MIT-licensed with open weights, and is offered as a
hosted endpoint at `https://biohub.ai` (model `esmfold2-fast-2026-05`). Its
headline claim is interface accuracy (FoldBench DockQ pass-rate vs Chai-1,
Boltz-1, AlphaFold 3), which is the regime our attribution pilots care about.

## Why this lives next to the Boltz2 runs

`run_esmfold2.py` writes its outputs with the **same filenames** the Boltz2
analyzers already glob for:

| File | Read by |
|------|---------|
| `esmfold2_model_0.cif` | `analyze_output.py` (`*_model_0.cif` / `*.cif`) |
| `confidence_esmfold2.json` | `analyze_output.py` (`confidence_*.json`) |
| `esmfold2_response.json` | raw response, provenance only |

So the head-to-head re-run reuses the existing per-complex analyzers and FASTA
inputs unchanged — only the structure-prediction backend changes.

## Setup

```bash
cd analysis/esmfold2
uv sync          # installs the pinned Biohub/esm GitHub SDK + biopython
export BIOHUB_API_TOKEN=...   # token from biohub.ai (or ESM_API_TOKEN)
```

Verify the installed SDK surface before spending a token:

```bash
python3 run_esmfold2.py --check-sdk
```

## Head-to-head re-runs (the three archived Boltz2 inputs)

Each block predicts with ESMFold2 then runs the same analyzer that produced the
Boltz2 `RESULTS_*` notes, so the confidence/interface readouts are directly
comparable.

```bash
cd analysis/esmfold2

# Complex III: CYC1:UQCRFS1 active electron-transfer interface
python3 run_esmfold2.py \
  --fasta ../complex_iii_boltz/inputs/cyc1_uqcrfs1_ims_domains.fasta \
  --output-dir cyc1_uqcrfs1_domains_out
python3 ../complex_iii_boltz/analyze_output.py cyc1_uqcrfs1_domains_out \
  --markdown-out RESULTS_CYC1_UQCRFS1_ESMFOLD2.md

# Proteasome: PSMB5 (catalytic) vs PSMA1 (structural) control
python3 run_esmfold2.py \
  --fasta ../proteasome_boltz/inputs/psmb5_psma1_attribution_domains.fasta \
  --output-dir psmb5_psma1_out
python3 ../proteasome_boltz/analyze_output.py psmb5_psma1_out \
  --markdown-out RESULTS_PSMB5_PSMA1_ESMFOLD2.md

# Complex IV: COX2 Model C copper-maturation module (apo first; see ligand note)
python3 run_esmfold2.py \
  --fasta ../complex_iv_boltz/inputs/cox2_sco1_sco2_model_c_domains.fasta \
  --output-dir cox2_model_c_out
python3 ../complex_iv_boltz/analyze_model_c_output.py cox2_model_c_out \
  --markdown-out RESULTS_MODEL_C_ESMFOLD2.md
```

All three FASTA paths above are exact files in the sibling `inputs/`
directories. The Complex IV `model_c_domains` input is the apo (metal-free)
domain set; a `..._cu_pocket` YAML variant exists for the metal-aware follow-up
once `LigandInput` parameterization is verified.

## Open items (must verify before relying on results)

These are the same caveats recorded in the project note:

1. **SDK surface.** The constructor, input-builder classes, `FoldingConfig`,
   and `fold_all_atom` call come from the Biohub/esm GitHub README. The PyPI
   wheel currently lags that complex API, so `pyproject.toml` pins the GitHub
   SDK commit used here. `extract_*` read fields defensively; `--check-sdk`
   prints what resolved.
   Adjust the isolated `build_structure_input` / `run_prediction` /
   `extract_confidence` helpers if the installed version differs.
2. **PAE / pair-chain iPAE.** Not confirmed in the hosted API surface; the
   Complex III analyzer reports pair-chain ipTM, which ESMFold2 does expose, but
   iPAE may be local-weights-only.
3. **Metals / cofactors.** Cu (COX2 CuA), heme (CYC1), and Fe-S (UQCRFS1) are
   run apo here. `LigandInput` exists in the SDK but parameterization of
   non-standard metals is unverified; treat metal-aware runs as a follow-up.
4. **Quota.** Biohub states free availability to researchers; exact rate/credit
   limits are unconfirmed.

## Curation guardrail

No ESMFold2 output is GO evidence on its own. As with the Boltz2 pilots it is
hypothesis-generating triage: flag plausible interfaces and select cases for
manual, literature-driven review.
