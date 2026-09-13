# NCU04302: ProtNLM2 function review

Source method: ProtNLM2. Source version: live API snapshot 2026-09-09T03:00:51.831347+00:00. Accession: Q1K772. Raw source: [NCU04302-protnlm-source.json](NCU04302-protnlm-source.json).

## Exact emitted paragraph

> Accepts the ubiquitin from the E1 complex and catalyzes its covalent attachment to other proteins

## Atomic claims

| Exact claim span | Assessment | Rationale |
|---|---|---|
| Accepts the ubiquitin from the E1 complex | PLI (0) | The Ubc9 subfamily accepts activated SUMO. The literal ubiquitin substrate specifies the wrong E2 subfamily. |
| catalyzes its covalent attachment to other proteins | PLI (0) | “its” refers to ubiquitin in the emitted sentence. Ubc9 catalyzes SUMO attachment, so the stated substrate-specific reaction is incorrect. |

The conserved E2 reaction pattern is plausible only after changing the modifier to SUMO; that correction is not silently substituted for the original claim. The generic transferase GO prediction is separately LSP.

## Evidence and provenance

Modifier-specific sequence assignments are “DR   CDD; cd23798; UBCc_UBE2I; 1.” and “DR   FunFam; 3.10.110.10:FF:000035; SUMO-conjugating enzyme ubc9; 1.” Full-length comparisons give 75.0% identity to fission-yeast Ubc9 and 62.42% to human Ubc9, compared with 42.0% to the recorded ubiquitin-E2 donor; [reproducible results](NCU04302-bioinformatics/RESULTS.md) preserve all alignments and controls. PMID:12597774 directly characterizes SUMO transfer in the fission-yeast reference. The current GOA PAINT assertion at PANTHER:PTN000629675 places the target in the SUMO E2 lineage; PROSITE identifies a UBC core at residues 3–156 and an active-site cysteine at 92. [PMID:9435231](https://pubmed.ncbi.nlm.nih.gov/9435231/) establishes recombinant yeast and mammalian Ubc9 thioesters with SUMO. This is a conserved-family inference for the target, not an NCU04302 biochemical assay. The recorded phmmer donor is Arabidopsis UBC2 (P42745), and its current reviewed function text is identical to the emitted paragraph; that record attributes ubiquitin conjugation to PMID:16339806. This exact textual agreement does not establish the internal mechanism of prediction. The preserved donor record confirms that this is a different E2 specificity, not simply a synonym for SUMO.

Error type: PARALOG_OVERANNOTATION. Donor record: [NCU04302-donor-P42745.json](NCU04302-donor-P42745.json).

## Complete paragraph evidence object

```json
{
  "commentType": "FUNCTION",
  "texts": [
    {
      "evidences": [
        {
          "evidenceCode": "ECO:0008006",
          "id": "ProtNLM2",
          "properties": [
            {
              "key": "model_score",
              "value": "0.19"
            },
            {
              "key": "phmmer_accession",
              "value": "P42745"
            },
            {
              "key": "phmmer_score",
              "value": "127.9"
            }
          ],
          "source": "Google"
        }
      ],
      "value": "Accepts the ubiquitin from the E1 complex and catalyzes its covalent attachment to other proteins"
    }
  ]
}
```
