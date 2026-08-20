# Sequence assessment of the GltX zinc-binding annotation

## Method

`check_zinc_module.sh` extracts the Q88LF6 sequence from the cached PSEPK
UniProt record, downloads the reviewed *Escherichia coli* K-12 GluRS sequence
P04805, and aligns the two proteins with MAFFT. P04805 is the comparison protein
because its reviewed UniProt entry identifies a zinc-binding four-cysteine
cluster.

Run from this directory:

```bash
bash check_zinc_module.sh
```

## Result

The aligned zinc-module region is:

```text
P04805  TAYKCYCSKER...KPRYDGR-----CRHSHEHHADDEPCVVRF
Q88LF6  DAGHAFYCFCTA...GETPRYDGRALLMSAEEVQRRLDAGEPHVIRMKVPSEGICV
```

Q88LF6 retains the upstream Cys pair but has no cysteine at the homologous
position immediately after `DGR`; only one later cysteine remains in this
region. Q88LF6 therefore does not preserve the four-cysteine zinc-binding
cluster present in P04805. This sequence-level loss provides positive evidence
against transferring `GO:0008270` zinc ion binding to Q88LF6.
