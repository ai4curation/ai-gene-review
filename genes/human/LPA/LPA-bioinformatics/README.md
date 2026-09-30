# LPA protease-domain sequence analysis

This workflow asks whether the human apo(a) reference protein (UniProt P08519) is sequence-compatible with a catalytically competent trypsin-like serine protease. It compares the UniProt-defined peptidase S1 domain with human plasminogen (P00747), human prothrombin/thrombin (P00734; active-protease control), and human hepatocyte growth factor (P14210; protease-like negative control).

The pipeline downloads current, reviewed records directly from the official UniProt REST API and domain matches from the official InterPro API. It then extracts the annotated peptidase S1 domains, aligns each target to PLG using BLOSUM62, maps PLG's UniProt-annotated charge-relay residues, and compares the residues at each UniProt domain boundary to PLG's annotated activation cleavage junction. Raw API responses and their SHA-256 checksums are retained.

Run with:

```bash
uv sync --locked
just all
just check
```

All accessions, inputs, and output paths are command-line parameters in the scripts. To analyze another protein, add its reviewed UniProt accession to the `accessions` list and to the `--targets` list in `justfile`. The scripts contain no gene-specific expected residues or conclusions.

Interpretive limits:

- Conservation or disruption of sequence features can establish compatibility with a catalytic mechanism, not experimental activity or inactivity.
- UniProt P08519 is one reference apo(a) sequence. LPA alleles vary extensively in kringle IV type-2 copy number, so total length and kringle count should not be generalized to every human allele.
- Pairwise alignment to PLG is appropriate for positional comparison of this close paralog, but it is not a structure calculation and does not test substrate binding, zymogen activation, or reaction kinetics.
- API records can change. `raw/manifest.json` records exact URLs, response metadata where supplied, and content checksums for the committed run.

Outputs are documented in [RESULTS.md](RESULTS.md). Direct machine-generated results are in `outputs/`; source records are in `raw/`.
