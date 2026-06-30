# RHEA substrate-specificity & reaction-chaining check — fatty acid β-oxidation module

## Question

Does the module tooling check that the **products of one reaction match the
substrates of the next**, and is **substrate (chain-length) specificity**
captured? (See the parent module `../fatty_acid_beta_oxidation.yaml`.)

## What the standard tooling does / does not do

- `linkml-validate`, `module_validator`, and `module_qc` perform **no**
  reaction-chaining or mass-balance check. `connections` (`PRECEDES`,
  `PROVIDES_INPUT_FOR`) assert ordering only; the chemistry on either side of an
  edge is never compared.
- Substrate/product fields on a module annoton are free-text `preferred_term`
  unless grounded to an ontology id. Only `{id,label}` term pairs are
  label-checked (and only for prefixes in `conf/oak_config.yaml`, which **does**
  include `CHEBI` and `RHEA`).

## Approach (this folder)

GO molecular-function terms are already mapped to RHEA. `rhea_chaining_check.py`
uses the **local OAK** adapters (`sqlite:obo:go`, `sqlite:obo:rhea`) — no web
service — to:

1. resolve each step's GO MF → RHEA reaction(s) (`GO.sssom_mappings`);
2. read each RHEA reaction's balanced equation (`RHEA.label`) — this is where the
   chain-length specificity lives;
3. for every `PRECEDES` edge, test whether a CoA-bearing species of the upstream
   reaction also appears in the downstream reaction.

Reproduce:

```bash
uv run python modules/fatty_acid_beta_oxidation/rhea_chaining_check.py \
    modules/fatty_acid_beta_oxidation.yaml
```

## Substrate specificity is fully recovered from RHEA

The GO→RHEA mapping yields chain-length-resolved, balanced equations, e.g.:

| Step | GO MF | representative RHEA | equation (substrate specificity) |
|------|-------|--------------------|----------------------------------|
| ① VLCAD | GO:0017099 | RHEA:19181 | *a very-long-chain 2,3-saturated fatty acyl-CoA + ETF(ox) → a very-long-chain (2E)-enoyl-CoA + ETF(red)* |
| ① MCAD | GO:0070991 | RHEA:14477 | *a medium-chain 2,3-saturated fatty acyl-CoA → a medium-chain (2E)-enoyl-CoA* |
| ① SCAD | GO:0016937 | RHEA:47196 | *a short-chain 2,3-saturated fatty acyl-CoA → a short-chain (2E)-enoyl-CoA* |
| ② hydratase | GO:0004300 | RHEA:20724 | *a 4-saturated-(3S)-3-hydroxyacyl-CoA = a (3E)-enoyl-CoA + H2O* |
| ③ 3-OH-acyl-CoA DH | GO:0003857 | RHEA:22432 | *a (3S)-3-hydroxyacyl-CoA + NAD⁺ → a 3-oxoacyl-CoA + NADH* |
| ③ long-chain variant | GO:0016509 | RHEA:52656 | *a long-chain (3S)-3-hydroxy fatty acyl-CoA + NAD⁺ → a long-chain 3-oxo fatty acyl-CoA + NADH* |
| ④ thiolase | GO:0003988 | RHEA:21564 | *an acyl-CoA + acetyl-CoA = a 3-oxoacyl-CoA + CoA* |
| ④ acetoacetyl thiolase | GO:0003985 | RHEA:21036 | *2 acetyl-CoA = acetoacetyl-CoA + CoA* |

The VLCAD/MCAD/SCAD molecular-function terms map to **chain-length-distinct**
RHEA reactions, so the chain-length specificity is machine-readable, not prose.

## Chaining result

| Edge | Verdict | Shared intermediate |
|------|---------|---------------------|
| ① acad → ② hydratase | **NO SHARED CoA INTERMEDIATE** | — |
| ② hydratase → ③ 3-OH-acyl-CoA DH | OK | (3S)-3-hydroxyacyl-CoA |
| ③ 3-OH-acyl-CoA DH → ④ thiolase | OK | 3-oxoacyl-CoA |

## The ①→② break is a real GO→RHEA mapping issue, not a module error

Step ① produces **(2E)-enoyl-CoA**. The canonical second-step enzyme is the
2-enoyl-CoA hydratase / crotonase reaction **RHEA:16105**
(*a (3S)-3-hydroxyacyl-CoA = a (2E)-enoyl-CoA + H2O*), which would chain
perfectly. But in the local ontology **GO:0004300 (enoyl-CoA hydratase
activity) maps only to RHEA:20724**, the *(3E)*-enoyl-CoA variant — so the GO MF
the curators (correctly) assigned to HADHA/ECHS1 does **not** resolve to the
reaction that consumes the (2E)-enoyl-CoA made in step ①. This is the
machine-checkable form of the "sequential reactions not easy to connect with
Rhea" caveat: the gap is in the **GO:0004300 → RHEA** mapping (it points at the
(3E) auxiliary reaction rather than, or in addition to, the (2E) canonical
RHEA:16105), and is a candidate to raise with the GO/RHEA mapping maintainers.

## Caveats

- One GO MF maps to several RHEA variants (master + directional + per-chain
  instances); the script picks the lowest-id generic reaction as representative
  and reports all candidates.
- RHEA master equations are written in one canonical direction, so a carbon
  carrier may sit on either side; the check is direction-agnostic over CoA
  species.
- Matching is on normalized participant **names**, because the local
  `sqlite:obo:rhea` exposes the equation label and `enabled by` proteins but not
  decomposed ChEBI participant ids. ChEBI-id-level chaining (with class
  subsumption, e.g. *medium-chain acyl-CoA* ⊑ *acyl-CoA*) would be exact and is
  the natural next step if RHEA participant data is loaded.
