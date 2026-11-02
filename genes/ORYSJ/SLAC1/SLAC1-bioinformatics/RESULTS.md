# Results: published SLAC1 primers support Q7XTX7

The full-length `topo-SLAC1-F` primer matches Q7XTX7 residues 1–6 (`MAAKPS`),
and `SLAC1-R` matches residues 570–578 (`DKEEEEKTE`) on the reverse strand.
Additional independent fragment primers match the expected N-terminal regions:
residues 191–196, 46–50, 25–29, 36–41, 51–55 and 70–75. Thus the paired termini
and multiple internal fragment boundaries consistently support Q7XTX7 as the
protein intended by the Min et al. 2019 SLAC1 constructs. The supplement also
names its SLAC1 promoter primer `pOs04g48530-F`, agreeing with
`LOC_Os04g48530` rather than the inconsistent identifier in the article body.

As an independent positive control, SAPK10 primers match Q75H77 residues 1–6
and 355–362. None of the published primers produces a peptide match of five or
more residues to BAG97777.1, the translated CDS of AK106615. This comparison
shows why that older accession cannot be substituted for Q7XTX7. It does **not**
establish which protein was experimentally assayed in the older 2012 paper;
that requires its constructs or sequence figures. That paper is not used to
assign Q7XTX7-specific functional evidence in this review.

This is a targeted construct-consistency check, not a genome-wide uniqueness
search or full-length sequence validation. Short peptide matches in isolation
are weak; the paired terminal positions and concordant internal primers are
what support the inference. Synonymous codons, intervening sequence variants,
and the remainder of each cloned insert are not verified by this analysis.

Results are in `results/primer-protein-matches.tsv`; source URLs, retrieval date,
parameters and reproduction commands are in `README.md`. Biological evidence
comes from PMID:31134357; these results resolve the relationship of its stated
constructs to the selected UniProt exemplar.

- [x] Scripts take input/output paths as arguments and contain no hardcoded gene conclusions.
- [x] Tested on another protein: SAPK10/Q75H77 gives the expected paired terminal matches.
- [x] Compared an unrelated accession: AK106615/BAG97777.1 gives no reportable matches.
- [x] Analysis completed and direct results are retained in this directory.
- [x] Input provenance, exact dependency version, method and limits are documented.
