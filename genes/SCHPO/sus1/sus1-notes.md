# sus1 evidence notes

Sus1 is a conserved small subunit of the SAGA transcription coactivator and the TREX-2 mRNA export complex. It connects transcription-associated chromatin regulation with nuclear mRNA export. Within the SAGA deubiquitination module it supports complex assembly and histone H2B deubiquitination by the catalytic subunit; it is not itself a histone deubiquitinase.

## Identity and prediction provenance

PomBase primary symbol sus1, locus SPBC6B1.12c, current UniProt Q7LL15. The supplied pre-release post-processed-2026_02_28k.xml is the source of the reviewed claims; its placeholder sequence, taxonomy and dates are not biological metadata. The current UniProt sequence is not established as the model input. Current API availability and published-list inclusion are separate properties; all biological judgments here concern the preserved original claims.

## Primary evidence inspected

- [PMID:19056896 The S. pombe SAGA complex controls the switch from proliferation to sexual differentiation through the opposing roles of its subunits Gcn5 and Spt8.] "Purification of the S. pombe SAGA complex showed that its subunit composition is identical to that of Saccharomyces cerevisiae."
- [PMID:14718168 Sus1, a functional component of the SAGA histone acetylase complex and the nuclear pore-associated mRNA export machinery.] "Biochemical analyses show that Sus1 interacts with SAGA, a large intranuclear histone acetylase complex involved in transcription initiation, and with the Sac3-Thp1 complex, which functions in mRNA export with specific nuclear pore proteins at the nuclear basket."
- [PMID:16855026 The mRNA export factor Sus1 is involved in Spt/Ada/Gcn5 acetyltransferase-mediated H2B deubiquitinylation through its interaction with Ubp8 and Sgf11.] "We demonstrate that Sus1 is involved in the SAGA-dependent histone H2B deubiquitinylation and maintenance of normal H3 methylation levels."

## Evidence limits and adjudication

- GO:0000932 (UNDECIDED): The reviewed primary evidence establishes nuclear SAGA and nuclear-pore export functions, but does not resolve a functional cytoplasmic or P-body pool of fission yeast Sus1. The automatic localization mapping is plausible but needs the underlying localization experiment or a specific justified transfer.

Primary reports are interpreted at the species, assay and subunit level. Abstract-only experimental annotations are not rejected because a title foregrounds another subunit. PAINT asserts inheritance from a curated ancestral node; donor count and target self-inclusion are not objections. ARBA overlap is recorded only as provenance, never as biological validation. CNN and LSP reflect established biological knowledge, without asserting training-data membership.

## Falcon report appraisal and additional primary evidence

The returned Falcon report was inspected. Its noncatalytic SAGA model agrees with the primary evidence, and its separation of conserved export inference from direct target assays is appropriate. The review already anchors export and deubiquitination to the original budding-yeast studies rather than the dissertations cited in parts of the report.

[PMID:31748520 Chaperone-mediated ordered assembly of the SAGA and NuA4 transcription co-activator complexes in yeast.] The full text explicitly reports: "Mass spectrometry analyses confirmed that, in S. pombe sgf73Δ mutants, the DUB subunits Ubp8, Sgf11 and Sus1 are absent from SAGA purifications". This supports target DUB-module membership; Sus1 itself is not the catalytic deubiquitinase. The authors also caution that the small Sgf11 and Sus1 proteins are less reliably quantified by mass spectrometry. This report strengthens the existing SAGA judgment without changing the export evidence category.
