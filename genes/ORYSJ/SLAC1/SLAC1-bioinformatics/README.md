# Rice SLAC1 construct identity check

Purpose: determine whether the primer sequences in Min et al. 2019
([PMID:31134357](https://pubmed.ncbi.nlm.nih.gov/31134357/), Supplementary Table S1)
are consistent with Q7XTX7, despite the inconsistent `Os04g18530` identifier in
the article body. An older study, PMID:22915747, gives `Os04g0674700`,
`LOC_Os04g57850.1` and cDNA `AK106615`; those identifiers must not be silently
assumed to identify the current SLAC1 model.

Run `just analyze` in this directory. Python 3.12+ and Biopython 1.85 are managed
by `uv` using the local project and lock file. `just fetch` refreshes the two
external inputs; routine reproduction should use the preserved input files.
The two UniProt flat files are the repository's fetched, unedited records for
SLAC1 Q7XTX7 and the independently assayed kinase SAPK10 Q75H77.

Inputs retrieved 2026-10-25:

- `data/PMID31134357-TableS1.xlsx`: unchanged member
  `12284_2019_297_MOESM8_ESM.xlsx` from the [Europe PMC supplementary archive](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6536566/supplementaryFiles).
- `data/AK106615.embl`: unchanged [ENA record](https://www.ebi.ac.uk/ena/browser/api/embl/AK106615), including the translated CDS BAG97777.1, used as a comparison to the older paper's stated accession.
- `../SLAC1-uniprot.txt`: Q7XTX7, 578 aa.
- `../../SAPK10/SAPK10-uniprot.txt`: Q75H77, 362 aa, an independent positive control using that gene's primers from the same supplement.

`primer_matches.py` extracts primer sequences from the spreadsheet, translates
both strands in all three frames with the standard genetic code, and reports
the longest contiguous exact peptide match for every primer/protein pair.
Cloning tails are retained in the input; only the matched internal peptide is
reported. Minimum report length: five amino acids. Coordinates are one-based,
inclusive. No protein identity or biological conclusion is encoded in the
matching script. See `RESULTS.md` for interpretation and limitations.
