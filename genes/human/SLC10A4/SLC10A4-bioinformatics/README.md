# SLC10 pocket-conservation analysis

Asks one falsifiable question: do the human SLC10 paralogues retain the residues
that NTCP/SLC10A1 actually uses to bind sodium and the HBV preS1 myristoyl
anchor? Sites are defined from ligand contacts in NTCP cryo-EM structures, not
from memory, and each paralogue is compared through its AlphaFold DB model.

See `RESULTS.md` for findings, limits and the method control that decided how
residue correspondence is computed. The analysis covers the whole family, so
`genes/human/SLC10A7/SLC10A7-bioinformatics/RESULTS.md` reports the SLC10A7
slice of the same run rather than duplicating the pipeline.

```bash
uv run python fetch_structures.py      # RCSB + AlphaFold DB
uv run python pocket_conservation.py   # -> pocket_conservation.json
```
