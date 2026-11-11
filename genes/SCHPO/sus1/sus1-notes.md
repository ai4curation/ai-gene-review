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

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not opened or used. Every GOA row, the description and the core functions were checked again against primary literature and evolutionary placement.

### Identity
Q7LL15 is the reviewed, canonical, full-length UniProt entry for sus1/SPBC6B1.12c (108 aa). It is not a fragment, isoform or alternative gene model. Global alignment with S. cerevisiae SUS1 (Q6WNK7, 96 aa; 26% identity) and human ENY2 (Q9NPA8, 101 aa; 32% identity) covers the whole length. The extra length is a C-terminal extension of about 10 residues that neither ortholog has [file:SCHPO/sus1/sus1-bioinformatics/RESULTS-rereview.md].

### Evolutionary grounding
PANTHER PTHR12514 (ENY2). UniProt assigns no subfamily to Q7LL15, Q6WNK7 or Q9NPA8, so no subfamily boundary separates the target from the characterised orthologs. All IBA rows descend from PTN000282153, whose descendant evidence includes fission yeast, budding yeast, fly, Arabidopsis and human members. The budding-yeast Sus1 interface mutants map to conserved S. pombe residues: sus1-11 G37/W38 to G40/W41 (CGW motif, also in human ENY2); sus1-10 E18/S19/G20 to E21/T22/G23; sus1-12 V73/D75 to I76/D78 [PMID:19269973 "In vivo, all three sus1 mutants were impaired in targeting TREX-2 (i.e. Sac3) to the nuclear pore complexes and exhibited nuclear mRNA export defects."]. The family review interpro/panther/PTHR12514/PTHR12514-review.yaml uses Q7LL15 as its reference protein in a single coherent subfamily, and its placement agrees with this one.

### Additional primary evidence used
- Fission yeast: [PMID:20838651 "Under our experimental conditions Ubp8 co-purified with four SAGA subunits—Sus1, Tra1, Sgf73, and Sgf29"]. [PMID:26443059 "deletion of other subunit of the UBP module, including Sus1, Sgf11 or the catalytic subunit Ubp8, did not affect silencing of ura4+"]: Sus1 does not share Sgf73's role in assembling the RITS heterochromatin complex.
- Budding-yeast structure: [PMID:20434206 "In the \"assembly lobe,\" a long Sgf11 N-terminal helix is clamped onto the Ubp8 ZnF-UBP domain by Sus1."]. Sus1 is a scaffold, not a catalyst.
- Budding-yeast elongation: [PMID:18923079 "Here, we show that Sus1 is required during transcription elongation and is associated with the elongating form of RNA Polymerase II (RNAP II) phosphorylated on Ser5 and Ser2 of the C-terminal domain (CTD)."] (newly cached).
- Budding-yeast cytoplasmic pool: [PMID:20230609 "Sus1 accumulates in discrete cytoplasmic granules, which partially co-localise with P-bodies and stress granules under specific conditions."] and "From this, we conclude that Sus1 can enter the P-bodies when overexpressed." (newly cached, full text).
- Falcon report: fission yeast TREX-2 membership has not been shown directly. In a 2016 Korean thesis, the Sus1 bait in the two-hybrid screen autoactivated the reporter, so it does not establish any TREX-2 interaction. The thesis was not used as support.

### Changes from the previous review
- GO:0000932 P-body and GO:0005737 cytoplasm: UNDECIDED changed to KEEP_AS_NON_CORE. The budding-yeast cytoplasmic and P-body pool is real but conditional (overexpression or stationary phase), minor and probably transient, and it has not been tested in fission yeast.
- GO:0006368 transcription elongation by RNA polymerase II: ACCEPT changed to KEEP_AS_NON_CORE. Support is ortholog-only (PMID:18923079), the role is accessory, and PAINT does not assert it.
- GO:0005634 nucleus: ACCEPT changed to MODIFY, with GO:0005654 nucleoplasm and GO:0005643 nuclear pore as replacements; both are already annotated.
- GO:0006406 mRNA export from nucleus: ACCEPT changed to MODIFY, with GO:0016973 poly(A)+ mRNA export from nucleus (already IBA) as the replacement.
- GO:0045893 positive regulation of DNA-templated transcription: ACCEPT changed to MODIFY, with GO:0045944 (already ISO) as the replacement.
- All other rows stay ACCEPT, each with a row-specific rationale replacing the shared boilerplate. GO:0006357 (EXP, PMID:21642955) is kept on deference to the curator: the abstract does not mention sus1, and the full text could not be retrieved.
- Core functions now use DUBm complex as the SAGA-side complex and nucleoplasm instead of nucleus as the location. The description now states which roles are shown in fission yeast (SAGA, DUB module) and which are inferred from orthologs (TREX-2, export).
- No NEW terms. Histone deubiquitination is catalysed by Ubp8, and the obsolete GO:0016578 has no replacement here; Sus1's scaffold contribution is already covered by GO:0045815 and GO:0071819.

### Relative to review next
The closest experimentally characterised relative is S. cerevisiae SUS1 (Q6WNK7, SGD:S000028510). It is in the same PAINT clade (PTN000282153) and is the main donor for the ISO and IBA rows. No review exists in genes/yeast/. Human ENY2 (Q9NPA8) is also unreviewed.
