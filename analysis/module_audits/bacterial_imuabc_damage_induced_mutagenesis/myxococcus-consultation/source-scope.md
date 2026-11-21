# Myxococcus ImuA evidence scope

## 2021: native DK1622 genetics and recombinant protein interactions

[Sheng et al., PMID:34190612](https://doi.org/10.1128/AEM.00919-21)
was read through the publisher/PMC full-text web views. The existing repository
cache is abstract-only and was not overwritten. The publisher Figure 1 image
was downloaded and visually inspected. Figure 1 supplies the primary identity
bridge documented in RESULTS.md. The supplement's text was readable through
the web PDF extractor, including Table S1's ImuB identifier. Its Figure S5
alignment pixels could not be retrieved: the screenshot interface returned
only a placeholder, while direct downloads were blocked. No amino-acid
alignment was fabricated from that unavailable figure.

The study establishes ImuA interaction with ImuB and RecA1 and inhibition of
RecA1 DNA binding and recombinase activity. Its native imuA deletion reduces
induced mutagenesis but does not phenocopy complete loss of ImuB/DnaE2; absolute
ImuA indispensability is not asserted. The reported long-DNA mobility-shift
assay did not detect ImuA DNA binding. It does not establish that binding is
absent with every substrate or assay. The ImuA protein itself supplies a physical
regulatory/accessory role, so the process judgment is not based only on necessity.

## 2024: biochemical capacity and its limits

[Lichimo et al., PMID:38591662](https://doi.org/10.1002/pro.4981)
has full text in the unchanged publication cache. Its actual supplemental PDF
was acquired through Europe PMC's PMC11002988 supplementaryFiles ZIP endpoint
and read locally. The supplement supplies assay summaries and structural models,
but no complete synthetic-construct sequence/accession. RESULTS.md explicitly
records this residual construct-identity inference.

Purified wild-type M. xanthus ImuA binds single- and double-stranded DNA and
hydrolyzes ATP; DNA enhances ATP turnover. Fluorescence-polarization binding
measurements supply positive support beyond the earlier negative mobility-shift
result. Nucleotide-dependent binding changes support a relationship between
binding and nucleotide state. ATP hydrolysis is a measured activity; ATP-driven
mutasome assembly/disassembly is a proposed interpretation. A complete
ImuA–ImuB–DnaE2 lesion-bypass cycle was not reconstituted here. ImuA is predominantly
monomeric in solution despite a self-interaction signal, so this review does not
infer a stable physiological ImuA homopolymer.

GO:0016887 ATP hydrolysis activity is supported. GO:0008094 now requires an
ATP-dependent activity modifying DNA: DNA-stimulated ATP turnover alone does not
establish that claim. ATPase and binding are separate activities in GO; one is
not used to delete the other. GO:0042276 error-prone translesion synthesis names
the supported accessory process, with a branch correction from the broad DNA
repair row. No separate process NEW is manufactured. No ATPase activity is
transferred to the divergent mycobacterial ImuA′ proteins.

## Research and propagation limits

A genuine Falcon research request failed with HTTP 403 authentication/access
failure. No provider-branded research was written manually. `just paint-losses`
reported that Q1D5A2 is not a leaf in the cached PTHR45900 tree: PAINT loss status
is unassessed, not a demonstrated absence of losses. The three seeded rows are
InterPro IEA, with their original payloads retained.
