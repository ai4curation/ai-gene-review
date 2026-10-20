# BBM-070 — MAPK cancer cell fate (Grieco et al. 2013)

Verbatim snapshot of model **070 "MAPK-CANCER-CELL-FATE"** from the Biodivine
Boolean Models (BBM) benchmark collection, which redistributes it from GINsim
(`http://ginsim.org/node/173`) and Cell Collective (module 7984).

- **Publication**: Grieco L, Calzone L, Bernard-Pierrot I, Radvanyi F, Kahn-Perles B,
  Thieffry D. *Integrative modelling of the influence of MAPK network on cancer cell
  fate decision.* PLoS Comput Biol 2013 — [PMID:24250280](https://pubmed.ncbi.nlm.nih.gov/24250280/),
  cached at `publications/PMID_24250280.md` (full text).
- **Fetched from**: `https://raw.githubusercontent.com/sybila/biodivine-boolean-models/main/models/[id-070]__[var-49]__[in-4]__[MAPK-CANCER-CELL-FATE]/` on 2026-09-26.
- **Files**: `model.bnet` (BoolNet format, 53 variables including 4 free inputs,
  104 regulations; md5 `325da49a0ac620ed112c094421f03e57`), `metadata.json` (BBM
  metadata, verbatim).
- **Licence / copyright**: BBM states that copyright of each model belongs to its
  authors/publisher; the source article is open access (PLoS, CC BY). BBM itself:
  Pastva S, Safranek D, et al. *Repository of logically consistent real-world Boolean
  network models*, bioRxiv 2023, doi:10.1101/2023.06.12.544361.
- **Inputs** (free variables, no update function in the source): `v_DNA_damage`,
  `v_EGFR_stimulus`, `v_FGFR3_stimulus`, `v_TGFBR_stimulus`.
- **Outputs** (phenotype read-outs): `v_Apoptosis`, `v_Growth_Arrest`, `v_Proliferation`.

Why this model: it is a curated, published, GINsim-native logical model whose core is
exactly the territory of three curated modules (`modules/erk_cascade.yaml`,
`modules/p38_cascade.yaml`, `modules/jnk_cascade.yaml`) plus the PI3K/AKT branch,
and it carries the feedbacks (ERK ⊣ RAF, RSK ⊣ SOS, ERK → SPRY, DUSP1 ⊣ p38/JNK,
PPP2CA ⊣ MEK, AP1 ⊣ MEK) that decide whether a signalling module oscillates or locks.

`mapping_to_modules.yaml` is the reviewed bridge between this model's variables and
the module element ids; see `models/boolean/README.md` for the format.
