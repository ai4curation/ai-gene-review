# LONRF3 RING and Lon-domain comparative analysis

## Objective

Use reviewed official sequence/domain records to test whether human LONRF3 Q496Y0 retains two intact RING-type zinc-binding regions and to distinguish its Lon N-terminal domain from the catalytic architecture of an active Lon peptidase. This sequence analysis can support or qualify domain-based GO inferences but cannot establish E3 activity by itself.

## Inputs and controls

`inputs/proteins.tsv` is the parameterized accession manifest. Records are fetched from the official reviewed UniProtKB REST API and InterPro API. Reviewed mouse Lonrf3 is the ortholog comparison, and reviewed human LONRF1/LONRF2 are paralogs. P78317/RNF4 is a characterized RING E3 positive control; P36776/LONP1 is an active Lon protease architecture control.

## Reproduction

Requirements: `uv`, `just`, network access, and Python 3.12.

```bash
uv sync --locked
just all
```

The downloader rejects unreviewed UniProt entries and accession mismatches. Raw API responses are preserved in `outputs/raw/`; computed outputs are written to `outputs/direct/`. Inputs and paths are parameters rather than embedded results.

## Methods and limits

- InterPro IPR001841, IPR018957, and IPR017907 identify RING-type regions/sites; IPR003111 identifies the Lon protease N-terminal domain.
- IPR003593/IPR003959 and IPR004815/IPR008268/IPR008269 are tracked explicitly to distinguish ATPase/protease machinery from an isolated N-terminal substrate-binding domain.
- Cys/His residues and spacings are calculated from each InterPro-defined RING region. This is descriptive, not an independent activity classifier.
- Like regions are globally aligned with Biopython 1.85. Conservation does not independently establish E3 activity, zinc occupancy, substrate specificity, or peptidase activity.

## Provenance

- UniProt Consortium, UniProtKB REST API: `https://rest.uniprot.org/`
- InterPro, InterPro API: `https://www.ebi.ac.uk/interpro/api/`
- Cock et al. (2009), Biopython, *Bioinformatics* 25:1422–1423.
