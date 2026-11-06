# Manual gene evidence notes

## 2026-11-05 comparative module audit

Reviewed the complete gene rather than only a module placement: all seeded GO
rows, original reference fields, exact raw UniProt record and relevant primary
literature were checked. The 2016 polyamine synthesis review (PMID:27268252)
and 2018 function review (PMID:30254075) were read as background; neither
substitutes for a target-specific assay. The broad family names encompass
substrate-divergent proteins and do not determine native substrate preference.

The normal command `just deep-research BACFG HMPREF1080_01141 --provider falcon` failed
with HTTP 403 authentication. No Falcon-branded text was authored. The raw
UniProt/GOA files were retained without refresh or edits. Manual curation uses
these notes and the genuine primary sources; no source cache was hand-edited.

QuickGO searches for carboxyaminopropylagmatine and the specific carboxypolyamine
decarboxylases found no corresponding specific activity term. GO:0102143 is
active and its definition explicitly covers both PUT/DAP reactions; obsolete
GO:0102144 is not used. NTRs describe missing activities rather than guessing IDs.
Exact PANTHER labels were checked against panther.obo and the record's DR lines.

The NCBI WP_005801052.1 amino-acid sequence exactly matches all 397 residues of the I9VY56 UniProt sequence.

The downloaded NCBI FASTA and SHA-256 comparison are retained under
HMPREF1080_01141-source-analysis. The paper identifies this exact accession
[PMID:37437886, "accession numbers WP_005801052.1 and EDO61991.1."], and the
UniProt record independently cross-references the resulting 8DEB structure.
The reference strain is CL05T12C13; a nonredundant WP accession does not prove
that this strain itself was genetically assayed. The experiment used a synthetic,
codon-optimized gene expressed and purified from E. coli.

PUT/DAP activities are direct enzyme measurements. BfCASDH has reported apparent
PUT kcat/Km 96 ± 7 and DAP 17 ± 3 M−1 s−1; the 5.6-fold comparison does not
compare agmatine. NADPH is preferred over NADH; ASA was subsaturating for
apparent kinetic values. Cooperativity and dimer assembly were measured.
A weak NADPH-dependent saccharopine reaction (0.039 s−1) was reported for BfCASDH,
but does not establish a physiological saccharopine role, and the ProtNLM
protein name is not independent support. No NEW saccharopine claim is made.

Decision: NEW IDA GO:0102143 for the exact assayed protein; retain this measured
activity in the core, with no native substrate preference over agmatine and
no inferred target-strain process annotation. This is the first authored row
for the zero-row seed, not an inherited NEW assertion.
