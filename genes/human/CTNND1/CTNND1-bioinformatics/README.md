# Historical p120 construct sequence mapping

This analysis compares the translation of the paper-cited mouse accession Z17804
with all 32 official human CTNND1 products. It checks sequence compatibility and
maps the paper's residue numbers. It does not establish assay-clone identity,
equal product function, binding affinity or GDP-inhibition activity.

Run `just analyze` and `just check-other-gene` from this directory. Python 3.12
and Biopython 1.85 are recorded in the dependency files. Inputs are archived under
`data/`; `data/provenance.json` records their origins. The independent CTNNB1 input
checks that the program is not keyed to p120 sequences. Outputs contain all ranked
alignments and selected residue mappings. `RESULTS.md` interprets these outputs.

The program uses global BLOSUM62 alignment with gap-open -10 and gap-extension
-0.5. Identity is matches divided by paired residues; query coverage is reported
separately. It examines the first two optimal alignments, explicitly flags ties,
and does not claim to enumerate all equally scoring alternatives. The library's
display labels the first/input-query sequence `target`; the JSON metadata uses
the user-facing query/target convention. No similarity cutoff implies function.

Primary sequence endpoints are [ENA Z17804](https://www.ebi.ac.uk/ena/browser/api/embl/Z17804)
and [UniProt O60716 products](https://rest.uniprot.org/uniprotkb/stream?query=accession%3AO60716&format=fasta&includeIsoform=true).
The control sequences are UniProt P35222 and Q02248. The assay context comes from
[PMID:17194753](https://pubmed.ncbi.nlm.nih.gov/17194753/), with the earlier mutant
positions from [PMID:10980705](https://pubmed.ncbi.nlm.nih.gov/10980705/).
