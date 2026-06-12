# ARO ↔ GO mappings & the UniProt→ARO→GO pipeline

Part of the [Antimicrobial Resistance project](../ANTIMICROBIAL_RESISTANCE.md).

## Files

| File | What it is |
|------|------------|
| `aro2go.sssom.yaml` | Curated **ARO → GO** mapping set in [SSSOM](https://mapping-commons.github.io/sssom/) format (source of truth). CURIE+label tuples throughout; validates with `linkml-validate`. |
| `aro2go.terms.yaml` | **Generated** nested term-tuple form of the mapping, validated by `linkml-term-validator` (do not edit by hand). |
| `sssom_to_terms.py` | Converter: reshapes the flat SSSOM rows into the nested `{id,label}` form the term-validator checks. |
| `uniprot2aro2go.py` | Pipeline that chains **UniProt → ARO → GO** by applying the SSSOM mapping. |
| `examples/rgi_example_mphA.txt` | Tiny example of CARD RGI tab-delimited output, used to demonstrate the sequence-based route. |
| `examples/rgi_example_betalactamases.txt` | RGI example (CTX-M-15/KPC-2/NDM-1) demonstrating exact-or-narrower propagation from the beta-lactamase family node. |

## Validation: `just validate-mappings`

Two layers, both run by the recipe (and by `tests/test_aro2go_mapping.py`):

1. **Structural** — `linkml-validate` against the SSSOM LinkML schema (required slots, shape).
2. **Ontology terms** — `linkml-term-validator` checks every **ARO** and **GO** CURIE in the mapping
   both *resolves* (ARO via `sqlite:obo:aro`, GO via `sqlite:obo:go`) and that the supplied **label
   matches the ontology label** — the "curie+label tuple" guarantee. This uses the sidecar schema
   `src/ai_gene_review/schema/aro_go_mapping.yaml`, whose `subject`/`object` are `{id,label}` tuples
   with `bindings` to dynamic enums (`AROTermEnum` reachable from `ARO:1000001`; `GOTermEnum` from the
   three GO roots). Prefix→adapter resolution is configured in `conf/oak_config.yaml`.

A label typo or a wrong id fails the build, e.g.:
`Label mismatch for 'GO:0050073': expected 'macrolide 2'-kinase activity', got '...'`.

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

## Propagation: exact or narrower (the high-value logic)

A GO term mapped at an ARO term applies to a gene whose ARO assignment is **that term or any
narrower (is_a descendant) ARO term** — i.e. propagate down the ARO hierarchy, never up. This is
why **family-level ARO nodes are the high-value mapping targets**: one mapping covers an entire
subtree. For example the single `beta-lactamase` (`ARO:3000001`) → `GO:0008800` mapping reaches
its **5,317** descendant ARO gene terms (CTX-M, KPC, NDM, …), none of which need their own row.

The pipeline implements this by walking each gene's ARO **is_a ancestors** (via OAK
`sqlite:obo:aro`) and firing any mapping whose subject is an ancestor-or-self. The output
`aro_relation` column records `exact` (mapping is on the gene's own ARO term) vs `narrower` (the
gene's ARO term is narrower than the mapped family/mechanism node). Use `--no-propagate` for
exact-only. Demonstration:

```text
$ uv run python uniprot2aro2go.py --sssom aro2go.sssom.yaml --rgi-output examples/rgi_example_betalactamases.txt
gene_aro_id   gene_aro_label   mapped_aro_id   mapped_aro_label   aro_relation   go_id        go_label
ARO:3001878   CTX-M-15         ARO:3000001     beta-lactamase     narrower       GO:0008800   beta-lactamase activity
ARO:3002312   KPC-2            ARO:3000001     beta-lactamase     narrower       GO:0008800   beta-lactamase activity
ARO:3000589   NDM-1           ARO:3000001     beta-lactamase     narrower       GO:0008800   beta-lactamase activity
```

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

A TSV of **candidate** GO annotations with full provenance — `uniprot_acc`,
`gene_aro_id`/`gene_aro_label` (the gene's ARO assignment), `mapped_aro_id`/`mapped_aro_label`
(the ARO term the mapping is on), `aro_relation` (`exact` or `narrower`),
`predicate_id`/`predicate_label`, `go_id`/`go_label`, `mapping_justification`, and `route`
(`DR_CARD` or `RGI`).

These are **leads for a curator, not final annotations**: the `enables`/`relatedMatch` predicates
indicate the relationship type, and a family-level mapping is only a prior for its members. As a
sanity check, the pipeline reproduces exactly the GO terms curators assigned by hand:

- **MphB** (`DR CARD` route) → `GO:0050073` macrolide 2'-kinase activity + `GO:0046677` response to antibiotic
- **MphA** (RGI route) → `GO:0050073` macrolide 2'-kinase activity

## Coverage (18 mappings)

- **Mechanism → `GO:0046677` response to antibiotic** (`skos:relatedMatch`): antibiotic inactivation,
  efflux, target alteration, target protection, target replacement, reduced permeability.
- **AMR gene family → GO MF** (`RO:0002327` enables, unless noted): MPH (`GO:0050073`),
  beta-lactamase (`GO:0008800`), CAT (`GO:0008811`), APH/AAC/ANT (`GO:0034071`/`0034069`/`0034068`),
  Erm (`GO:0052910`), dfr (`GO:0004146`), sul (`GO:0004156`), FosA (`GO:0004364`, `relatedMatch`).
- **Determinant → GO MF** (`enables`): mphA, mphB (`GO:0050073`).

### Deliberately NOT mapped (verification record)

Checked and intentionally left out because GO has no correct specific MF term (mapping to the nearest
term would assert a paralog or the wrong chemistry):

| ARO family | Why not mapped |
|---|---|
| rifampin ADP-ribosyltransferase (Arr, `ARO:3000390`) | `GO:0003950` is **poly**-ADP-ribosyltransferase; Arr is mono-ADP-ribosyltransferase. No mono term fits. |
| glycopeptide VanA ligase (`ARO:3000010`) | `GO:0008716` is D-Ala-**D-Ala** ligase; VanA makes D-Ala-**D-Lac**. No D-Ala-D-Lac GO MF term. |
| Cfr 23S rRNA methyltransferase (`ARO:3000202`) | `GO:0070040` is the **C2** (RlmN housekeeping) activity; Cfr methylates **C8**. No C8 term. |
| macrolide esterase (Ere, `ARO:3000320`) | No macrolide/erythromycin esterase GO MF term exists. |
| rifampin monooxygenase (`ARO:3000445`) | No rifampin/rifamycin monooxygenase GO MF term exists. |
| tetracycline efflux | No single ARO efflux-family node; GO efflux-transporter terms are non-specific. |

## Validation & tests

- `just validate-mappings` — structural (`linkml-validate`) **and** ontology-term
  (`linkml-term-validator`, checks every ARO/GO id resolves + label matches).
- `tests/test_aro2go_mapping.py` — SSSOM structure, terms-file sync, and (integration) term-validator.
- Pipeline parser: doctest — `uv run python -m doctest projects/mappings/uniprot2aro2go.py`.
