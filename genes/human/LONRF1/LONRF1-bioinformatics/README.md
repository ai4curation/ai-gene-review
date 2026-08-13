# LONRF1 RING and Lon-domain comparative analysis

## Objective

Test whether reviewed human LONRF1 (Q17RB8), its reviewed mouse ortholog, and reviewed human LONRF paralogs retain InterPro-defined RING-type zinc-finger regions and a Lon protease N-terminal domain. The analysis asks whether sequence/domain evidence is compatible with GO:0061630 (ubiquitin protein ligase activity) and GO:0046872 (metal ion binding). It does **not** infer peptidase activity from a Lon N-terminal domain.

## Inputs and controls

`inputs/proteins.tsv` is the parameterized accession manifest. Records are fetched from the official reviewed UniProtKB REST API and InterPro API. P78317/RNF4 is a characterized RING E3 positive control; P36776/LONP1 is an active Lon protease architecture control. These controls test the scripts on proteins outside the LONRF family and help separate RING from Lon-protease evidence.

## Reproduction

Requirements: `uv`, `just`, network access, and Python 3.12.

```bash
uv sync --locked
just all
```

The downloader rejects unreviewed UniProt entries and accession mismatches. Raw API responses are preserved in `outputs/raw/`. Direct, computed outputs are written to `outputs/direct/`. Change the manifest or command-line paths to reuse the scripts; no accession or output path is embedded in analysis code.

## Methods and limits

- InterPro accessions IPR001841, IPR018957, and IPR017907 identify RING-type regions/sites; IPR003111 identifies the Lon protease N-terminal domain. IPR003593/IPR003959 and IPR004815/IPR008268/IPR008269 are tracked to distinguish ATPase/protease machinery from the isolated N-terminal domain.
- Cys/His residues and their spacings are read directly from each InterPro region. This is descriptive, not a de novo E3 classifier.
- Like regions are globally aligned with Biopython 1.85 and pairwise identity is calculated over residue-residue aligned columns. Identity supports homology/conservation but does not establish biochemical activity.
- GO:0046872 is broad. RING zinc coordination is compatible with metal-ion binding, but a direct metal-binding annotation may still require the evidence policy used by the curation project.
- A Lon N-terminal/substrate-binding domain alone is not the ATPase or protease catalytic machinery of LONP1. No peptidase conclusion is made.

## Provenance

- UniProt Consortium, UniProtKB REST API: `https://rest.uniprot.org/`
- InterPro, InterPro API: `https://www.ebi.ac.uk/interpro/api/`
- Cock et al. (2009), Biopython, *Bioinformatics* 25:1422–1423.
