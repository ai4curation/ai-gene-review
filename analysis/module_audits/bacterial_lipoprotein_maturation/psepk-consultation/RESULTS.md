# Reproducible sequence check

This shared three-gene panel is housed under the module consultation because it checks the same provider-transfer question across all three owned targets. The scripts accept explicit input paths and site lists; biological conclusions are kept here and in evidence.md.

Run from repository root:

```sh
uv run python analysis/module_audits/bacterial_lipoprotein_maturation/psepk-consultation/sequence_check.py analysis/module_audits/bacterial_lipoprotein_maturation/psepk-consultation/sequence-panel.yaml analysis/module_audits/bacterial_lipoprotein_maturation/psepk-consultation/sequence-results.yaml
uv run python analysis/module_audits/bacterial_lipoprotein_maturation/psepk-consultation/run_sequence_panel.py analysis/module_audits/bacterial_lipoprotein_maturation/psepk-consultation/sequence-panel.yaml analysis/module_audits/bacterial_lipoprotein_maturation/psepk-consultation/sequence-sensitivity.yaml
```

Dependencies are repository uv.lock/Python and Biopython 1.85. The global BLOSUM62 alignment uses open=-10, extension=-0.5 and the first highest-scoring alignment. All input hashes and alignment strings are recorded. Identity is identical residues divided by aligned non-gap residue pairs, not all columns; thus it need not reproduce a provider percentage using a different denominator or penalties.

The Lgt R139/R216 and all seven specified Lnt target positions match the reference functional residues. LspA D145 maps consistently. The first catalytic Asp correspondence is sensitive to gap scoring: the default introduces a gap at E. coli123, while extension=-1 maps it to target126 across four gap-opening values. Target126 and145 themselves are curated HAMAP catalytic features. This is not evidence of a missing catalytic residue, and no new catalytic geometry is asserted.

Checklist:

- [x] Input paths, source positions and parameters supplied by a config; sequence matches and residue mappings are computed, never hardcoded as outputs.
- [x] The same generic implementation ran on three different proteins.
- [x] Results and input hashes are retained; complete sequence lengths are validated against the raw records.
- [x] Sensitivity analysis retains all five declared parameter combinations, including the ambiguous default result.
- [x] Analysis completed as expected; uncertainty is reported rather than replacing the inconvenient alignment.
- [x] Reproducible output and independent source scopes are recorded in evidence.md.

This analysis corroborates conserved function but cannot establish KT2440 essentiality, enzyme kinetics, preferred donor species, or substrate breadth.
