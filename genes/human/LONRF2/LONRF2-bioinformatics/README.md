# LONRF2 RING and Lon-domain comparative analysis

## Objective

Use reviewed, official sequence/domain records to distinguish RING E3 architecture from Lon peptidase architecture in human LONRF2 Q1L5Z9. This analysis is secondary to direct experimental literature showing that LONRF2 ubiquitylates damaged or misfolded proteins. Its useful role is narrower: test whether the sequence retains a RING-type zinc-binding region and whether the misleading protein name is accompanied by the ATPase/protease machinery of an active Lon protease.

## Inputs and controls

`inputs/proteins.tsv` is the parameterized accession manifest. Records are fetched from the official reviewed UniProtKB REST API and InterPro API. Reviewed human LONRF1 and LONRF3 are paralog comparisons. P78317/RNF4 is a characterized RING E3 positive control; P36776/LONP1 is an active Lon protease architecture control. A current UniProt query found no reviewed non-human LONRF2 entry, so no unreviewed ortholog was substituted.

## Reproduction

Requirements: `uv`, `just`, network access, and Python 3.12.

```bash
uv sync --locked
just all
```

The downloader rejects unreviewed UniProt entries and accession mismatches. Raw API responses are preserved in `outputs/raw/`; computed outputs are written to `outputs/direct/`. Inputs and paths are command-line parameters rather than embedded results.

## Methods and limits

- InterPro IPR001841, IPR018957, and IPR017907 identify RING-type regions/sites; IPR003111 identifies the Lon protease N-terminal domain.
- IPR003593/IPR003959 and IPR004815/IPR008268/IPR008269 are tracked explicitly to distinguish ATPase/protease machinery from an isolated N-terminal substrate-binding domain.
- Cys/His residues and their spacings are calculated from each InterPro-defined RING region. This is descriptive, not a de novo activity classifier.
- Like regions are globally aligned with Biopython 1.85. Sequence conservation does not independently establish E3 activity, zinc occupancy, substrate specificity, or peptidase activity.

## Provenance

- UniProt Consortium, UniProtKB REST API: `https://rest.uniprot.org/`
- InterPro, InterPro API: `https://www.ebi.ac.uk/interpro/api/`
- Cock et al. (2009), Biopython, *Bioinformatics* 25:1422–1423.
