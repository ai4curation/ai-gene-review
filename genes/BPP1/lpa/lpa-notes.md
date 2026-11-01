# lpa (Q06260) — Curation Notes

## Summary
- **Gene symbol**: `lpa` (also known as gene `10` / `gp10`)
- **UniProtKB**: `Q06260` (`LPA_BPP1`, 150 aa, 18.1 kDa)
- **Organism**: Escherichia phage P1 (`NCBITaxon:2886926`)
- **Function**: Late promoter-activating protein Lpa (gp10), a sequence-specific DNA-binding transcription activator required for transcription from P1 late promoters during the lytic cycle. Recognizes a conserved 9-bp inverted repeat (`5'-TTAAACTAA-3'` / consensus `5'-TTNNCAAAN-3'`) centered around position -22 of P1 late promoters and recruits host RNA polymerase sigma-70 holoenzyme (with host stringent starvation protein SspA) to activate expression of morphogenetic, DNA packaging (`pacAB`), and lysis operons.

## Literature Evidence
- **Lehnherr, Guidolin & Arber 1991 (`PMID:1917870`)**:
  - Cloned and sequenced P1 gene `10` (`lpa`, `X55810`), showing that it encodes an 18.13-kDa protein whose expression is controlled by a C1-repressible early promoter (`Op72`). Using an in vivo trans-activation assay with a late promoter `Ps` driving a `gene S::lacZ` fusion, proved that gp10 (Lpa) is the sole phage-encoded factor required for P1 late promoter activation.
  - Quote: `"An in vivo trans activation assay system, consisting of gene 10 under the transcriptional control of an inducible promoter and a gene S/lacZ fusion transcribed from Ps, was used to show that gene 10 is the only phage-encoded function required for late promoter activation."`
- **Łobocka et al. 2004 (`PMID:15489417`)**:
  - Reviewed the mechanism of late transcription activation by Lpa (`gp10`) across 11 experimentally verified P1 late promoters. Late promoters lack canonical sigma-70 -35 hexamers and instead harbor a conserved 9-bp inverted repeat centered near position -22 that binds Lpa; Lpa and host `E. coli` SspA act together to enable RNA polymerase sigma-70 holoenzyme binding and transcription initiation.
  - Quote: `"Instead, they have a conserved 9-bp inverted repeat (previously termed late operator) that is centered about position −22 of the transcription start site and interacts with Lpa"`
  - Quote: `"Results of in vivo footprinting experiments confirm that RNA polymerase binds to late promoter sequences in the presence, but not in the absence, of Lpa"`

## Annotation Review Decisions
- `GO:0003677` (`DNA binding`, IEA: `GO_REF:0000120`): **MODIFY** to `GO:0001216` (`DNA-binding transcription activator activity`) and `GO:0000976` (`transcription cis-regulatory region binding`). Lpa is experimentally established as a sequence-specific DNA-binding transcription activator that binds the -22 inverted repeat of P1 late promoters to recruit RNA polymerase (`PMID:1917870`, `PMID:15489417`).
