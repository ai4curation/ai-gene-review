# CG45100 (A0A0B4LGP2): evidence and ProtNLM claim review

CG45100 encodes a predicted 38-residue peptide from an upstream open reading frame associated with the Hdac3 5-prime untranslated region. Its strongly hydrophobic central segment is compatible with membrane insertion, but peptide production, membrane topology, and biological activity are not established.

Exact input: [A0A0B4LGP2](https://www.uniprot.org/uniprotkb/A0A0B4LGP2/entry), 38 residues. The accession was fetched explicitly with the gene-directory alias; no canonical-sequence substitution is made.

Raw emitted predictions: [CG45100-predictions-source.json](CG45100-predictions-source.json). Source features: [CG45100-uniprot.txt](CG45100-uniprot.txt), with an exact extraction in [CG45100-sequence-evidence.json](CG45100-sequence-evidence.json).

## Sequence and domain evidence

These are sequence/domain observations or explicitly named feature predictions, not measurements of biological function. ARBA assertions and ProtNLM-derived UniProt names are not counted as validation.

```text
FT   TRANSMEM        12..30
FT                   /note="Helical"
FT                   /evidence="ECO:0000256|SAM:Phobius"
```

## ProtNLM claims

The snapshot emits names and location/keyword statements, with no GO or EC prediction for this target. Each actual statement is assessed below; no GO term has been substituted for it. Categories follow the function-prediction rubric, with nonspecific “uncharacterized” names marked UNC because they contain no testable function. CNN records an independently supported existing annotation; it does not assert a particular training-set composition.

| Kind | Verbatim emitted statement | Assessment | Evidence and limitation |
|---|---|---|---|
| Name | Uncharacterized protein | UNC | Uncharacterized protein is an appropriately nonspecific name but supplies no testable molecular-function hypothesis. This is a predicted 38-residue upstream-ORF product and must not be conflated with HDAC3. |
| Location | Membrane (SL-0162) | UNC | Residues 12-30 form a hydrophobic segment and are called a transmembrane helix by Phobius. Membrane association is a reasonable sequence hypothesis; expression and membrane insertion of this tiny upstream-ORF product remain unverified. |

## Literature evidence

No target-specific primary finding is used to establish a molecular activity here. The current assessment is bounded by exact-record architecture and the explicitly identified curated inferences.

## Annotation decisions

- GO:0003674 molecular_function (ND): **ACCEPT**. The exact 38-residue upstream-ORF product lacks a characterized molecular function; neither its genomic proximity to Hdac3 nor its hydrophobic segment establishes deacetylase activity.
- GO:0005575 cellular_component (ND): **ACCEPT**. Phobius predicts a transmembrane helix at residues 12-30 but this sequence prediction does not establish that the upstream-ORF peptide is produced and localized in vivo.
- GO:0008150 biological_process (ND): **ACCEPT**. No functional process is established for the exact upstream-ORF peptide. Hdac3 gene function cannot be transferred to a separate 38-residue translation product.

## Research assessment

Falcon timed out after 600 seconds; the configured perplexity-lite fallback returned HTTP 401 with insufficient_quota. Manual exact-identifier searches checked NCBI Gene 19835016 and FlyBase clone reports FBcl0277028 and FBcl0167378. They establish the CG45100/Hdac3-uORF identity and transcript/cDNA support, without establishing translation, membrane insertion, or physiological function of the 38-residue peptide. No provider report is fabricated.

Sources: [NCBI Gene 19835016](https://www.ncbi.nlm.nih.gov/gene/19835016), [FlyBase SD27965](https://flybase.org/reports/FBcl0277028.html), [FlyBase LD42026](https://flybase.org/reports/FBcl0167378.html).

The annotation and prediction assessments are complete. UNC/UNDECIDED record delimited scientific or evidence uncertainty. Empty core-function lists indicate that no sufficiently resolved molecular activity can be asserted, rather than an unfinished review.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

This re-review did not open any ProtNLM2 prediction file or prediction-evidence folder and does not use their output as evidence.

**Identity.** A0A0B4LGP2 is the complete 38-residue product of the CG45100 upstream ORF (FlyBase FBgn0266539; RefSeq NP_001287174.1). It is not a fragment, isoform or alternative gene model of Hdac3. It is a separate FlyBase gene and a separate UniProt entry for an alternative-ORF peptide that the repo convention gives its own folder. No canonical product needs substituting. The Hdac3 link is positional only (names Hdac3-5'utr and Dmel_Hdac3_uORF). [file:DROME/CG45100/CG45100-uniprot.txt; file:DROME/CG45100/CG45100-deep-research-falcon.md "No exact-target publication was found under A0A0B4LGP2, AHN57173.1, FBgn0266539, CG45100, Dmel_CG45100, Dmel_Hdac3_uORF, or Hdac3-5′utr."]

**Evolutionary evidence.** The UniProt record lists no PANTHER, Pfam or InterPro entry, so there is no PAINT node and no IBA. A new reproducible blastp search (CG45100-bioinformatics/blast_conservation_rereview.sh, results in RESULTS-rereview.md) found the peptide conserved across Drosophilidae: D. mauritiana 97%, rhopaloa 100%/35, kikkawai and suzukii 97%/35, Scaptodrosophila lebanonensis 91%/32, and D. rubida 76%/33 (44 aa). It found no homolog outside the family (the next hit has E = 0.058 and is a compositional TM match) and no HDAC hit. Every homolog is uncharacterized, so no function can be transferred. The conserved amino-acid sequence, including the TM segment, fits a translated peptide under selection, but that remains an inference.

**Annotation decisions (unchanged actions; support improved).** All three ND root rows stay ACCEPT. Before, each ND row cited only the Phobius feature. That shows the sequence prediction, not that the literature was searched. Each row now cites the negative literature search from the deep-research report, plus the conservation analysis or the Phobius feature where relevant. I did not add a NEW membrane CC term: Phobius alone, on an ORF whose translation is untested, does not meet the bar. The description now covers the Drosophilidae-restricted conservation and the cis/trans hypotheses. Core functions stay empty.

**Relative.** No characterized relative exists. There is no PANTHER family or PAINT node, and the only homologs are uncharacterized Drosophilidae ORFs. Hdac3 is the host gene on the same transcript, not a relative, and the repo has no DROME Hdac3 review. No PANTHER family review or module applies. (The repo modules that mention HDAC3 are about vertebrate nuclear-receptor signaling and concern the deacetylase, not this peptide.)
