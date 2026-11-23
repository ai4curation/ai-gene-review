# Curation Notes: Bacteriophage T4 gene 2 (gp2; UniProt P15076)

## Identity and Nomenclature
- **Gene symbol**: `2` (historical synonym: `64`)
- **Protein**: Terminal DNA protecting protein gp2 (also referred to as gp64; 274 aa, ~31.6 kDa)
- **UniProt**: `P15076` (`VG02_BPT4`)
- **Taxon**: `NCBITaxon:10665` (*Tequatrovirus T4*)

## Biological Function Summary
1. **Protection of injected viral linear dsDNA ends against host RecBCD (exonuclease V)**:
   - T4 packages ~171 kb linear, circularly permuted, terminally redundant dsDNA into its capsid. Upon tail sheath contraction and DNA ejection into the *Escherichia coli* cytoplasm, the free blunt dsDNA ends are vulnerable to degradation by the host RecBCD (exonuclease V) complex.
   - Gene 2 encodes gp2, an internal virion protein (~31.6 kDa) packaged with the head that binds noncovalently to the genomic dsDNA termini (specifically situated at the portal/head-tail junction primed for entry) and caps the ends during and immediately after DNA injection, preventing RecBCD-mediated exonucleolytic degradation (Silverstein & Goldberg 1976, PubMed 796649; Oliver & Goldberg 1977, PubMed 326966; Lipinska et al. 1989, PubMed 2651415).
   - Gene 2 amber mutants produce morphologically normal DNA-filled particles that adsorb and inject DNA into *E. coli*, but the injected DNA is rapidly degraded to acid-soluble fragments and fails to initiate replication or late transcription in *recBCD+* hosts; infectivity is restored to wild-type levels in *recB* or *recD* mutant hosts lacking exonuclease V activity (Silverstein & Goldberg 1976, PubMed 796649; Goldberg 1983; Wang et al. 2000, PubMed 10633097).
2. **Role in head-to-tail joining and head completion**:
   - Historically, mutations in genes `2` and `64` were isolated as head completion defects affecting head-to-tail attachment and sensitivity to exonuclease V. Sequencing of the gene 50-65-4 region demonstrated that `2` and `64` map to the same open reading frame encoding the ~30-31.6 kDa gp2 protein (Lipinska et al. 1989, PubMed 2651415; Leiman et al. 2010).
   - gp2 is positioned at the portal/connector interface where it stabilizes the terminal DNA within the neck/portal channel and participates in head completion prior to tail attachment.

## Review of Existing GOA Annotations
- `GO:0099016` (`symbiont-mediated evasion of DNA end degradation by host`, IEA `GO_REF:0000043`): **ACCEPT**. This term accurately and specifically captures the primary biological role of gp2 in protecting injected linear phage dsDNA ends from host RecBCD exonuclease degradation.
- `GO:0052031` (`symbiont-mediated perturbation of host defense response`, IEA `GO_REF:0000043`): **MODIFY** -> `GO:0099016` (`symbiont-mediated evasion of DNA end degradation by host`). While true in a broad sense, `GO:0052031` is overly general because gp2 acts specifically by capping linear viral DNA termini to evade host RecBCD exonuclease (`GO:0099016`), which is already present on the record.
- `GO:0052170` (`symbiont-mediated suppression of host innate immune response`, IEA `GO_REF:0000043`): **MODIFY** -> `GO:0099016` (`symbiont-mediated evasion of DNA end degradation by host`). Derived from the broad UniProt keyword `Inhibition of host innate immune response by virus`; gp2 does not inhibit a host innate immune signaling pathway or enzymatic complex directly, but instead physically caps viral DNA ends to evade host RecBCD end degradation (`GO:0099016`).
- **New annotations (`NEW`)**:
  - `GO:0003677` (`DNA binding`): gp2 functions by binding linear dsDNA ends to shield them from RecBCD exonuclease.
  - `GO:0019028` (`viral capsid`): gp2 is packaged inside the phage head/capsid at the portal junction and accompanies the viral genome into the host cell.
