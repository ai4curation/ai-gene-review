# Curation Notes for Escherichia phage Mu repc (P06019)

## Summary of Gene Function
- **Gene symbol**: `repc` (locus tag `Mup01`; UniProt `P06019`, Repressor protein c)
- **Organism**: *Escherichia phage Mu* (`NCBITaxon:2681603`)
- **Function**: Repressor protein c (Repc) is the major lysogenic immunity repressor of temperate transposable bacteriophage Mu. It contains a winged helix-turn-helix (wHTH) N-terminal DNA-binding domain that cooperatively binds nine operator sites distributed across three operator regions (`O1`, `O2`, and `O3`) within the bipartite early control and internal activation sequence (IAS) enhancer region [PMID:9546656, PMID:16154589, file:BPMU/repc/repc-uniprot.txt].
- **Mechanism in Latency-Replication Switch**: By binding `O1` and `O2`, Repc represses transcription from the early lytic promoter (`Pe`), which drives expression of the early transposition operon (`ner`, `A`, `B`, etc.), and competes directly with the MuA transposase (`A`) for binding to the overlapping internal activation sequence (`IAS`) enhancer required for transpososome assembly [PMID:16154589, file:BPMU/repc/repc-uniprot.txt]. At high concentrations, Repc also binds `O3` overlapping its own promoter (`PcM`) to negatively autoregulate its synthesis [PMID:9546656, file:BPMU/repc/repc-uniprot.txt]. Repc homodimers assemble into higher-order oligomers (probable homohexamers) on DNA and undergo ClpXP-mediated degradation when co-expressed with virulent mutant subunits (`Vir`), inducing prophage lytic development [PMID:16154589, file:BPMU/repc/repc-uniprot.txt].

## Literature & Reference Notes
- **PMID:16154589** ("Control of bacteriophage mu lysogenic repression.", Geuskens et al. / Toussaint group review): Reviews the central role of Repc in the Mu lysis-lysogeny decision, maintenance of lysogeny, operator binding competition with MuA transposase, and ClpXP protease-mediated derepression.
- **PMID:9546656** ("DNA loop formation by bacteriophage Mu repressor.", 1998): Demonstrates that Mu repressor c binds three operator sites (`O1`, `O2`, and `O3`) overlapping two divergent promoters (`Pe` and `PcM`) and forms higher-order DNA loop complexes stabilized by DNA supercoiling and IHF.

## Annotation Review Decisions
- `GO:0003677` (`DNA binding`, IEA): `MODIFY` to `GO:0000976` (`transcription cis-regulatory region binding`), as Repc specifically recognizes the `O1`, `O2`, and `O3` operator regions controlling the `Pe` and `PcM` promoters.
- `GO:0017053` (`transcription repressor complex`, IDA, `PMID:16154589`): `ACCEPT` (Repc forms homodimers and higher-order hexameric/looped nucleoprotein repressor complexes on operator DNA).
- `GO:0019042` (`viral latency`, IEA): `MODIFY` to `GO:0019044` (`maintenance of viral latency`), reflecting Repc's specific role in maintaining prophage repression and immunity against superinfection.
- `GO:0030430` (`host cell cytoplasm`, IEA): `ACCEPT` (Repc acts in the bacterial host cytoplasm/nucleoid).
- `GO:0098689` (`latency-replication decision`, IEA): `ACCEPT` (Repc directly competes with MuA and Ner to determine whether phage Mu establishes latency or enters lytic replicative transposition).
- `NEW` `GO:0001217` (`DNA-binding transcription repressor activity`, `enables`) and `GO:0000976` (`transcription cis-regulatory region binding`, `enables`) and `GO:0019044` (`maintenance of viral latency`, `involved_in`): Capture the core molecular function and biological process of Repc.
