# AhpC regeneration-route checks

Run from the repository root with its installed environment:

```
uv run python modules/bacterial_alkyl_hydroperoxide_reductase-source-analysis/check_module.py
uv run python modules/bacterial_alkyl_hydroperoxide_reductase-source-analysis/check_routes.py
```

`check_module.py` uses the production validator and independently reads PANTHER memberships from the 15 raw UniProt records. It does not construct membership from module declarations or download a release-wide index. Exact gene-product selectors constrain function; the family fields record classification. Broad family-review coverage advisories are reported rather than silently suppressed.

`check_routes.py` exercises the production Boolean compiler over all 32,768 subsets of the 15 exact products. The independent six-route expectation checks complete native pairs/chains, missing components, isolated peroxidases/reductases, mixed-species subsets and coexistence of multiple complete routes. Mtb AhpC is shared between its two alternatives, but neither route requires the other route's donor components.

Presence denotes functional expressed protein under the stated chemical conditions. These tests establish capability coverage, not sufficiency for growth, physiological donor predominance, absolute essentiality or absence of compensatory redox pathways. The qualified Bacillus pairing remains an inference from native operon/physiology and homologous biochemical architecture.

Primary supporting text is stored only through normal publication retrieval. Access failures, provider attempts, row/raw preservation and complete validation logs are kept in the audit cache; no generated provider report or rewritten publication cache is used as evidence.
