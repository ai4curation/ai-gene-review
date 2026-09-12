# RPL36AL curation notes

Date: 2026-07-18

## Research provenance

The required automated deep-research run was attempted with Falcon and the
configured Perplexity-lite fallback. Falcon returned HTTP 402 and
Perplexity-lite returned HTTP 401 because its quota was unavailable. Neither
provider produced a usable output, and no provider-labelled file was authored
manually. This review therefore uses the fetched reviewed UniProt record, the
complete GOA set, cached primary publications, manually inspected open article
text, and the current QuickGO term record. The detailed synthesis is in
RPL36AL-deep-research-manual.md.

## Identity and paralog boundary

RPL36AL is an autosomal, expressed retrocopy of the X-linked RPL36A gene. The
gene-discovery study found that RPL36AL is ubiquitously expressed
[PMID:12490704 "RPL36AL is ubiquitously expressed."]. The fetched reviewed
UniProt sequences are each 106 residues long and differ only at residue 38:
RPL36A has lysine and RPL36AL has arginine. The proteins are therefore much
harder to distinguish than the genes, especially in untargeted proteomics.

This review transfers no RPL36A-specific muscle, cancer, localization, or
interaction annotations to RPL36AL. Evidence is treated as RPL36AL-specific only
when the paper explicitly identifies the gene product or uses a recombinant
RPL36AL construct. Family-level human eL42 results that do not state an accession
are used only as context.

## Direct ribosomal and tRNA evidence

The 2012 crosslinking study explicitly identified RPL36AL as the mammalian
large-subunit protein contacting P/E-state tRNA. It mapped the contact to the
CCA-end and RPL36AL Lys53 [PMID:22865768 "the crosslink was formed most
efficiently with C74 and C75 of P/E-tRNA, but could also connect the ultimate A
of this tRNA with Lys53 of protein RPL36AL"].

The 2014 follow-up used purified recombinant human RPL36AL and human 80S
ribosomes. Surface-plasmon-resonance measurements gave nanomolar affinities for
full-length and truncated tRNAs, while poly(A) and poly(U) controls did not bind
[PMID:25191528 "The KD values in the nanomolar range reflect high tRNA-binding
affinities with full length and truncated tRNA species."]. The same paper
recovered RPL36AL-tRNA contacts in assembled ribosomes. This directly supports a
NEW tRNA binding annotation (GO:0000049) in addition to the established
structural constituent of ribosome function.

The paper also explored possible peptidyl-tRNA hydrolase activity and translation
termination geometry. Those observations were not converted into independent GO
annotations because they do not establish a physiological catalytic activity of
free RPL36AL. Similarly, the 2024 conserved-motif paper supports a role for human
eL42 in E-site tRNA release, but its abstract does not identify which of the
single-residue RPL36A/RPL36AL paralogs supplied the FLAG-tagged construct.

## Existing annotation decisions

| GO annotation | Decision | Rationale |
|---|---|---|
| cytoplasmic translation, IBA | ACCEPT | Core process of a cytosolic 60S protein, reinforced by direct human-ribosome evidence. |
| structural constituent of ribosome, IBA | ACCEPT | Core molecular function supported by family, complex, and biochemical evidence. |
| cytosolic large ribosomal subunit, IBA | ACCEPT | Most specific established complex membership. |
| structural constituent of ribosome, IEA | ACCEPT | Correct InterPro mapping and action-consistent with the IBA record. |
| cytoplasm, IEA | ACCEPT | Correct broad functional localization. |
| ribosome, IEA | ACCEPT | Correct broad complex term. |
| translation, IEA | ACCEPT | Correct broad process term. |
| protein binding, IPI | MARK_AS_OVER_ANNOTATED | The KRTAP10-7 screen hit is retained as interaction data, but generic protein binding is not an informative function. |
| nucleus, IDA | UNDECIDED | The candidate-level localization is confined to an inaccessible supplementary table; the accessible narrative does not name RPL36AL. |

The defensible core is a cytosolic 60S-subunit structural role coupled to direct
tRNA binding.

## New annotation

- GO:0000049 tRNA binding, IDA, PMID:25191528, corroborated by PMID:22865768.
  QuickGO was queried directly on 2026-07-18 to verify the current identifier,
  label, molecular-function aspect, definition, and non-obsolete status.

## Open questions

- What proportion of ribosomes contains RPL36AL versus RPL36A across tissues?
- Does the single K38R difference change assembly, modification, tRNA dynamics,
  or translation of particular mRNAs?
- Can endogenous nuclear localization be reproduced with paralog-specific
  reagents, and does it represent normal 60S assembly transit?

