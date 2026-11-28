# Curation Notes for Escherichia phage Mu ner (P06020)

## Summary of Gene Function
- **Gene symbol**: `ner` (locus tag `Mup02`; UniProt `P06020`, Negative regulator of transcription Ner)
- **Organism**: *Escherichia phage Mu* (`NCBITaxon:2681603`)
- **Function**: Ner is an 8 kDa lambda Cro-like helix-turn-helix transcriptional repressor encoded at the 5' end of the early lytic operon of bacteriophage Mu [PMID:2537762, file:BPMU/ner/ner-uniprot.txt]. It binds a specific operator regionlocated between the divergent `Pe` (early lytic) and `PcM` (c repressor) promoters containing two 12-bp inverted repeat half-sites (`5'-ANPyTAPuGPyTAPuT-3'`) separated by a 6-bp AT-rich spacer [PMID:2537762, file:BPMU/ner/ner-uniprot.txt].
- **Role in Lysis-Lysogeny Decision & Autoregulation**: Ner switches off transcription from the `PcM` promoter, blocking synthesis of the lysogenic repressor Repc and committing the phage to lytic transposition. In addition, Ner negatively regulates the `Pe` promoter to dampen its own expression and keep early operon (`A`, `B`, etc.) transcription independent of rising viral genome copy number during replicative transposition [file:BPMU/ner/ner-uniprot.txt].

## Literature & Reference Notes
- **PMID:2537762** ("Purification and characterization of the Ner repressor of bacteriophage Mu.", Kukolj et al., 1989): Purified the 8 kDa Ner protein to homogeneity and showed by gel retardation and DNase I footprinting that Ner binds specifically as a monomer to a 50-bp operator region containing two 12-bp sites with consensus `5'-ANPyTAPuGPyTAPuT-3'` separated by a 6-bp spacer.

## Annotation Review Decisions
- `GO:0003677` (`DNA binding`, IEA): `MODIFY` to `GO:0000976` (`transcription cis-regulatory region binding`) (or keep `GO:0003677` as `ACCEPT` since `GO:0003677` is in the core functions prompt list, and also add `NEW` `GO:0001217` `DNA-binding transcription repressor activity`, `GO:0098689` `latency-replication decision`, and `GO:0045892` `negative regulation of DNA-templated transcription`). Keeping `GO:0003677` as `ACCEPT` and adding `GO:0001217`, `GO:0098689`, and `GO:0045892` as `NEW` directly matches the cluster specification!
- `GO:0017053` (`transcription repressor complex`, IDA, `PMID:2537762`): `ACCEPT` (annotated by UniProtKB from `PMID:2537762`; two Ner monomers occupy the two 12-bp half-sites of the bipartite `ner` operator to form the repressive nucleoprotein assembly).
- `GO:0030430` (`host cell cytoplasm`, IEA): `ACCEPT`.
