# ARO ↔ GO mappings & the UniProt→ARO→GO pipeline

Part of the [Antimicrobial Resistance project](../ANTIMICROBIAL_RESISTANCE.md).

## Files

| File | What it is |
|------|------------|
| `aro2go.sssom.yaml` | Curated **ARO → GO** mapping set in [SSSOM](https://mapping-commons.github.io/sssom/) format. CURIE+label tuples throughout; validates with `linkml-validate`. |
| `uniprot2aro2go.py` | Pipeline that chains **UniProt → ARO → GO** by applying the SSSOM mapping. |
| `examples/rgi_example_mphA.txt` | Tiny example of CARD RGI tab-delimited output, used to demonstrate the sequence-based route. |

## Why a pipeline?

CARD/ARO has **no native ARO→GO mapping** (verified against `aro.owl`). We supply the
ARO→GO bridge as curated SSSOM, then need a **UniProt→ARO** step to apply it to real
protein entries. There are two routes:

1. **`DR CARD` cross-reference (deterministic, sparse).** UniProt flat-files sometimes carry
   a CARD cross-reference, e.g.
   `DR   CARD; ARO:3000318; mphB; ARO:0001004; antibiotic inactivation.`
   This single line gives **both** the determinant ARO id *and* the resistance-mechanism ARO
   id for free. But UniProt only populates it for a minority of entries — in this repo,
   **1 of 2334** cached UniProt records (MphB). MphA (Q47396) has none.

2. **Sequence-based assignment with RGI (scalable).** CARD's
   [Resistance Gene Identifier](https://github.com/arpcard/rgi) assigns ARO ids to protein
   sequences. This is the route for entries lacking a `DR CARD` line. We do **not** run RGI
   in this script (it needs RGI + the local CARD database installed); instead we parse its
   output if you run it. Related: [`argNorm`](https://github.com/BigDataBiology/argNorm)
   normalises the output of RGI/AMRFinderPlus/ABRicate/etc. to ARO accessions.

## Usage

Run via the just recipe (validates the SSSOM first, then runs the chain on the AMR genes):

```bash
just aro2go-pipeline
```

Or directly:

```bash
# Route 1 — DR CARD line(s) from cached UniProt record(s):
uv run python projects/mappings/uniprot2aro2go.py \
    --sssom projects/mappings/aro2go.sssom.yaml \
    genes/ECO8N/A0A0H3EUF3_ECO8N/A0A0H3EUF3_ECO8N-uniprot.txt

# Sweep every cached UniProt record (recursive glob; quote it):
uv run python projects/mappings/uniprot2aro2go.py \
    --sssom projects/mappings/aro2go.sssom.yaml \
    'genes/**/*-uniprot.txt' -o /tmp/aro2go_all.tsv

# Route 2 — parse RGI output (for entries without a DR CARD line, e.g. MphA):
uv run python projects/mappings/uniprot2aro2go.py \
    --sssom projects/mappings/aro2go.sssom.yaml \
    --rgi-output projects/mappings/examples/rgi_example_mphA.txt
```

To generate real RGI output for the sequence-based route:

```bash
rgi load --card_json card.json            # one-time, from https://card.mcmaster.ca/download
rgi main --input_sequence protein.faa --input_type protein --output_file rgi_out
# then pass rgi_out.txt to --rgi-output
```

## Output

A TSV of **candidate** GO annotations with full provenance — `uniprot_acc`, `aro_id`,
`aro_label`, `predicate_id`/`predicate_label`, `go_id`/`go_label`, `mapping_justification`,
and `route` (`DR_CARD` or `RGI`).

These are **leads for a curator, not final annotations**: the mapping is curated only for the
MPH family so far, and `enables`/`relatedMatch` predicates indicate the relationship type. As a
sanity check, the pipeline reproduces exactly the GO terms curators assigned by hand:

- **MphB** (`DR CARD` route) → `GO:0050073` macrolide 2'-kinase activity + `GO:0046677` response to antibiotic
- **MphA** (RGI route) → `GO:0050073` macrolide 2'-kinase activity

## Validation & tests

- SSSOM file: `just validate-mappings` (runs `linkml-validate -C "mapping set"`).
- Pipeline parser: doctest — `uv run python -m doctest projects/mappings/uniprot2aro2go.py`.
