# RPA49 (Q01080, YNL248C) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: reviewed as the closest experimentally characterised relative of SCHPO/rpa49 (O14086).
No ProtNLM2 output was consulted.

### Deep research
`just deep-research-falcon yeast RPA49 --fallback perplexity-lite` failed: falcon returned
"Failed to authenticate" and the perplexity fallback returned HTTP 401 (insufficient quota).
No deep-research file exists; the review was built from cached publications and the UniProt record.

### Evolutionary grounding
- PANTHER PTHR14440 (DNA-DIRECTED RNA POLYMERASE I SUBUNIT RPA49) has no subfamily split in the
  local entries file; Q01080, S. pombe O14086 and human POLR1E (Q9GZS1) are all members.
- PAINT node PTN000374345: SGD:S000005192 (this gene) is a donor for the RNA polymerase I complex
  and Pol I elongation IBA rows. The Pol I preinitiation complex assembly IBA has only mouse Polr1e
  as donor, but yeast has independent support (Rrn3 recruitment defect, tWH promoter DNA binding).
- S. pombe rpa51+ complements S. cerevisiae rpa49 deletion
  [PMID:12893961 "is able to complement S. cerevisiae rpa49Delta mutation, indicating that RPA51 is a functionally-conserved subunit of Pol I between the budding yeast and the fission yeast"].

### Experimentally established in S. cerevisiae (usable as transfer reference)
- Pol I subunit; forms a heterodimer with A34.5 [PMID:18160037 "The Pol I-specific subunits A49 and A34.5 form a heterodimer near the enzyme funnel that acts as a built-in elongation factor"].
- DNA binding by C-terminal tWH [PMID:20797630 "The C-terminal region of A49 forms a \"tandem winged helix\" (tWH) domain that binds DNA with a preference for the upstream promoter nontemplate strand"]; mutagenesis K356A/S358A, K359A abolishes binding (UniProt FT, ECO:0000269 PMID:20797630).
- tWH on upstream DNA in transcribing Pol I (PMID:27867008, full text).
- Rrn3 recruitment and release [PMID:18086878 "These data suggest a dual role of the Rpa49-Rpa34 dimer during the recruitment of Rrn3 and its subsequent dissociation from the elongating polymerase."].
- Processivity, nucleosome passage [PMID:32060094].
- rRNA synthesis reduced ~5-fold in rpa49-delta; synthetic lethal with hmo1-delta, bypassed by Pol II-driven rRNA (PMID:12374750).
- Pol I clustering on rDNA and nucleolar integrity (PMID:21263028).

### Decisions
- GO:0003899 enables (PMID:24153184): kept, but recorded a WRONG_QUALIFIER source defect (should be contributes_to; A49 is non-catalytic).
- nucleus -> MODIFY to nucleolus; DNA-templated transcription -> MODIFY to transcription by RNA polymerase I.
- termination of Pol I transcription (PMID:18160037, abstract-only): UNDECIDED; abstract attributes cleavage/3' trimming to A12.2.
- regulation of cell size (HMP, genome-wide size screen): MARK_AS_OVER_ANNOTATED, indirect phenotype of reduced ribosome biogenesis.
- No NEW annotations proposed.
