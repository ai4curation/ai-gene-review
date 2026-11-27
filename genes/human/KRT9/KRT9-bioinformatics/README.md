# KRT9 (P35527) bioinformatics: architecture, variant catalogue, conservation, structural context

Reproducible analysis supporting the KRT9 gene review and the epidermolytic palmoplantar
keratoderma 1 (EPPK1) mechanism entry. Findings are in [RESULTS.md](RESULTS.md).

## Rerun

```bash
cd genes/human/KRT9/KRT9-bioinformatics
uv run run_all.py            # reuses the committed data/ snapshot; downloads coordinate files into cache/
uv run run_all.py --refresh  # refetches every input first (results then describe the new snapshot)
```

`just all` / `just refresh` do the same. Each script declares its own pinned dependencies inline
(PEP 723), so `uv run` builds an isolated environment and nothing is installed into the repository
environment; there is deliberately no `pyproject.toml` here (it would join the root uv workspace).

Network hosts used: rest.uniprot.org, eutils.ncbi.nlm.nih.gov, gnomad.broadinstitute.org,
www.ebi.ac.uk (InterPro, PDBe), alphafold.ebi.ac.uk, pantherdb.org, search/data/files.rcsb.org.

## Layout

| path | content |
|---|---|
| `00_fetch.py` | downloads all inputs; writes `data/` and `data/manifest.json` (URL, time, release) |
| `01_architecture.py` | domains, composition, glycine loops, heptad register, boundary motifs, stutter |
| `02_variants.py` | UniProt + ClinVar + gnomAD variants merged on the canonical sequence, reference-residue check |
| `03_statistics.py` | per-domain distribution, Fisher/binomial tests, constraint and pLoF summary |
| `04_conservation.py` | FAMSA alignments (type I keratins, all keratins, orthologs), conservation, cross-keratin disease variants |
| `05_structure.py` | experimental-structure check, AlphaFold pLDDT, template search and interchain contact analysis |
| `06_report_tables.py` | formats result files as Markdown tables (`results/06_tables.md`); no analysis |
| `common.py` | shared helpers |
| `data/` | small fetched inputs (committed) |
| `results/` | every script output (committed) |
| `cache/` | AlphaFold and PDB mmCIF files, fetched at run time (git-ignored, about 40 MB) |

Options: `00_fetch.py --accession/--gene`, `01_architecture.py --keratin-gene KRT14 --tag control_KRT14`
(any reviewed human keratin as a control input), `--boundary-window`, `--break-penalty`; see each
script's docstring.

`RESULTS.md` is written by hand from the result files for the snapshot recorded in
`data/manifest.json`; after `--refresh`, compare it against the regenerated `results/06_tables.md`.
