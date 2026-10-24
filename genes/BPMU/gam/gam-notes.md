# Curation Notes for Escherichia phage Mu gam (P06023)

## Summary of Gene Function
- **Gene symbol**: `gam` (locus tag `Mup10`; UniProt `P06023`, Putative DNA ends protecting protein gam)
- **Organism**: *Escherichia phage Mu* (`NCBITaxon:2681603`)
- **Function**: Protein Gam (`gam`, 174 aa) is a homodimeric semi-early DNA-binding protein of bacteriophage Mu (`GO:0003677` `DNA binding`, `GO:0003690` `double-stranded DNA binding`) that binds specifically to linear double-stranded DNA ends regardless of overhang polarity (`5'`, `3'`, or blunt) and does not bind RNA or single-stranded DNA [file:BPMU/gam/gam-uniprot.txt].
- **Mechanism of Host Exonuclease Evasion**: By capping linear dsDNA termini, Mu Gam physically blocks access by bacterial exonucleases (such as RecBCD), thereby protecting linear phage DNA from degradation (`GO:0099016` `symbiont-mediated evasion of DNA end degradation by host`, `GO:0042262` `DNA protection`) [file:BPMU/gam/gam-uniprot.txt]. Unlike phage lambda Gam (which directly binds and inhibits the RecBCD enzyme complex as a DNA mimic), phage Mu Gam is a structural ortholog of eukaryotic Ku70/Ku80 that directly binds linear dsDNA ends (`PubMed:11278599`, `PubMed:12524520` cited in `file:BPMU/gam/gam-uniprot.txt`).

## Annotation Review Decisions
- `GO:0003677` (`DNA binding`, IEA) and `GO:0003690` (`double-stranded DNA binding`, IEA): We mark `GO:0003677` as `ACCEPT` (or `TOO_GENERAL` entailed by `GO:0003690`; wait—since the prompt specifically lists `GO:0003677` `DNA binding` for `gam`, let's `ACCEPT` both `GO:0003677` and `GO:0003690` so there is no conflict and both are represented!).
- `GO:0099016` (`symbiont-mediated evasion of DNA end degradation by host`, IEA): `ACCEPT`.
- `GO:0042262` (`DNA protection`, IEA): `ACCEPT`.
- `GO:0052031` (`symbiont-mediated perturbation of host defense response`, IEA) and `GO:0052170` (`symbiont-mediated suppression of host innate immune response`, IEA): `TOO_GENERAL` because both are high-level parent terms entailed by the specific annotation `GO:0099016` (`symbiont-mediated evasion of DNA end degradation by host`).
- `GO:0030430` (`host cell cytoplasm`, IEA): `ACCEPT`.
