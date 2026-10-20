# BPQBE rep (RNA-directed RNA polymerase subunit beta / P14647) Notes

## Overview
- **Gene symbol**: `rep`
- **UniProt ID**: `P14647` (`RDRP_BPQBE`)
- **Organism**: Qubevirus durum / Escherichia virus Qbeta (`NCBITaxon:39803`)
- **Protein**: RNA-directed RNA polymerase subunit beta (RNA replicase beta chain), 589 amino acids, EC 2.7.7.48.

## Biological Function, Structure & Subunit Interactions
- **Catalytic RdRp subunit of Qbeta replicase**: `rep` encodes the 589-aa catalytic beta-subunit (`GO:0003968`) of the Qbeta replicase holoenzyme, which replicates the positive-sense viral ssRNA genome via a complementary negative-strand RNA intermediate (`GO:0039694`) ([PMID:20798060]; [PMID:22245970]; [file:BPQBE/rep/rep-uniprot.txt]).
- **Complex with host EF-Tu, EF-Ts, and ribosomal protein S1**: Crystal structures of the core Qbeta replicase ([PMID:20798060]; [PMID:22245970]) show that the right-handed beta-subunit (comprising finger, palm, and thumb domains) forms a tight 1:1:1 catalytic core complex with the host *Escherichia coli* translation elongation factor binary complex EF-Tu:EF-Ts (`tufA`/`tufB` and `tsf`), which acts as a structural co-factor maintaining the catalytic crevasse and forming the single-stranded template RNA exit channel. Host 30S ribosomal protein S1 associates with the core complex to bind viral RNA cooperatively (`GO:0003723`) and initiate (+)-strand replication ([file:BPQBE/rep/rep-uniprot.txt]).
- **Metal cofactor**: Binds two catalytic Mg2+ ions (`GO:0000287`) in the palm active site ([PMID:20798060]; [file:BPQBE/rep/rep-uniprot.txt]).

## Curation Decisions
- **ACCEPT**:
  - `GO:0003968` (`RNA-directed RNA polymerase activity`, IEA from GO_REF:0000120): Core enzymatic activity of the Qbeta replicase beta-subunit.
  - `GO:0003723` (`RNA binding`, IEA from GO_REF:0000043): Binds the viral RNA template and nascent RNA strand during de novo initiation and elongation.
  - `GO:0039694` (`viral RNA genome replication`, IEA from GO_REF:0000002): Core biological process catalyzed by the Qbeta replicase complex.
- **KEEP_AS_NON_CORE**:
  - `GO:0000166` (`nucleotide binding`, IEA from GO_REF:0000043): True substrate-binding property (binds ribonucleoside 5'-triphosphates), kept as non-core alongside `GO:0003968`.
  - `GO:0001172` (`RNA-templated transcription`, IEA from GO_REF:0000108): Kept as non-core alongside `GO:0039694`.
- **MODIFY**:
  - `GO:0016740` (`transferase activity`, IEA from GO_REF:0000043) -> `GO:0003968` (`RNA-directed RNA polymerase activity`).
  - `GO:0016779` (`nucleotidyltransferase activity`, IEA from GO_REF:0000043) -> `GO:0003968` (`RNA-directed RNA polymerase activity`).
  - `GO:0034062` (`5'-3' RNA polymerase activity`, EXP from PMID:22245970 and IEA from GO_REF:0000116) -> `GO:0003968` (`RNA-directed RNA polymerase activity`).
  - `GO:0019079` (`viral genome replication`, IEA from GO_REF:0000002) -> `GO:0039694` (`viral RNA genome replication`).
  - `GO:0046872` (`metal ion binding`, IEA from GO_REF:0000043) -> `GO:0000287` (`magnesium ion binding`), supported by binding of 2 Mg2+ ions per subunit at the polymerase catalytic site.
- **REMOVE**:
  - `GO:0005515` (`protein binding`, IPI from PMID:20798060 with `UniProtKB:P0A6P1` and `UniProtKB:P0CE47`): While physical assembly of the beta-subunit with host EF-Ts (`P0A6P1`) and EF-Tu (`P0CE47`) is genuine and structurally resolved in [PMID:20798060], bare `GO:0005515` (`protein binding`) is uninformative and removed per GO curation policy.
