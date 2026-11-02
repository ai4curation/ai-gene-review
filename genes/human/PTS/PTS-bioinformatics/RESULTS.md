# PTS: Human Protein Atlas subcellular evidence

Made by `hpa_subcellular.py` (run with
`uv run --no-project --with pyyaml python -I hpa_subcellular.py ENSG00000150787 > hpa_subcellular.yaml`),
which downloads the HPA entry XML and keeps only the immunofluorescence (ICC/IF)
and protein-array sections. Raw output: `hpa_subcellular.yaml` (retrieved 2026-10-24).

## Result

- HPA summary: Localized to the cytosol. Main location cytosol (GO:0005829); no additional location.
- IF reliability: approved.
- Antibody HPA001481; protein array: supported (Pass with single peak corresponding to interaction only with its own antigen).
- Cell lines: A-431 cytosol; U-251MG cytosol; U2OS cytosol.
- Counterstains in every image: Nucleus, Microtubules, ER. No mitochondrial marker.
- Only one antibody has IF data, so there is no independent second antibody.

## Control: a known mitochondrial protein

The same script run on HSPD1 (ENSG00000144381), output in
`hpa_subcellular_control_HSPD1.yaml`:

- HPA summary: Localized to the mitochondria (reliability enhanced).
- Antibody CAB002775: A-431 mitochondria, with counterstains ER, Microtubules, Nucleus.

So HPA calls a mitochondrial location from the staining pattern when the
image carries only the standard nucleus, microtubule and ER counterstains.

## Interpretation

Given the control, a cytosol-only call with the same counterstain set is a
negative observation for a substantial mitochondrial pool, not just silence. It cannot
exclude a minor pool beneath cytosolic staining. Against it, the only positive line
for mitochondrion is a C-terminal GFP-fusion overexpression screen (LIFEdb).
