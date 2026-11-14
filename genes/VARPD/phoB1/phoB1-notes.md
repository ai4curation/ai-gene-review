# Curatorial Notes for `phoB1` (`A0A0H2M7F4`, `VPARA_10430`) in *Variovorax paradoxus* TBEA6

## 1. Gene & Protein Identity
- **UniProt Accession:** `A0A0H2M7F4` (`A0A0H2M7F4_VARPD`)
- **Gene Symbol:** `phoB1`
- **Locus Tag / EMBL CDS:** `VPARA_10430` / `KLN58031.1` on contig `JZWI01000005` (`RefSeq:WP_021007058.1`)
- **Protein Length:** 230 aa (25,832 Da); two-component response regulator consisting of an N-terminal CheY-like receiver domain (`PROSITE:PS50110` `RESPONSE_REGULATORY` at residues 5–121, `Pfam:PF00072` `Response_reg`, `CDD:cd17618` `REC_OmpR_PhoB`) with the conserved phosphoacceptor `Asp54` (`FT MOD_RES 54 /note="4-aspartylphosphate"` in `50-LILLDWMLPGQSG-62`), and a C-terminal OmpR/PhoB-type winged-helix DNA-binding effector domain (`PROSITE:PS51755` `OMPR_PHOB` at residues 130–226, `Pfam:PF00486` `Trans_reg_C`, `CDD:cd00383`).
- **Specific Family:**
  - `InterPro:IPR011879` (`Sig_transdc_resp-reg_PhoB`), `NCBIfam:TIGR02154` (`PhoB`), `PANTHER:PTHR48111:SF40` (`PHOSPHATE REGULON TRANSCRIPTIONAL REGULATORY PROTEIN PHOB`).

## 2. Operon Context on Contig `JZWI01000005`
- Encoded immediately between `phoR1` (`VPARA_10420`, `KLN58030.1`) and `phoU` (`VPARA_10440`, `KLN58032.1`) within the `phoR1-phoB1-phoU-pstB-pstA-pstC-pstS-ppx` (`VPARA_10420`–`VPARA_10490`) phosphate regulon gene cluster.

## 3. Literature & Comparative Evidence
- **[PMID:24563032]** (Gardner et al. 2014 *J Bacteriol*): Describes how PhoB is a winged-helix response regulator that upon aspartyl phosphorylation by PhoR under phosphate limitation forms a dimer, binds Pho-box DNA sequences upstream of Pho regulon genes (including `pstSCAB-phoU`), and recruits RNA polymerase to activate transcription.

## 4. Annotation Review Decisions
- `GO:0000156` (`phosphorelay response regulator activity`, IEA `GO_REF:0000120`): **ACCEPT** — core MF of the N-terminal receiver domain (`Asp54` phosphorylation site).
- `GO:0000160` (`phosphorelay signal transduction system`, IEA `GO_REF:0000002`): **ACCEPT** — core BP.
- `GO:0000976` (`transcription cis-regulatory region binding`, IEA `GO_REF:0000120`): **ACCEPT** — core MF of the C-terminal winged-helix domain binding Pho-box operators.
- `GO:0003677` (`DNA binding`, IEA `GO_REF:0000120`): **TOO_GENERAL** — entailed by `GO:0000976`.
- `GO:0005737` (`cytoplasm`, IEA `GO_REF:0000044`): **TOO_GENERAL** — entailed by `GO:0005829` (`cytosol`).
- `GO:0005829` (`cytosol`, IEA `GO_REF:0000118`): **ACCEPT** — core CC.
- `GO:0006355` (`regulation of DNA-templated transcription`, IEA `GO_REF:0000120`): **MODIFY** -> `GO:0045893` (`positive regulation of DNA-templated transcription`) — phosphorylated PhoB1 acts as a positive transcriptional activator of the Pho regulon (`PMID:24563032`, `CC FUNCTION` in `file:VARPD/phoB1/phoB1-uniprot.txt`).
- `GO:0006817` (`phosphate ion transport`, IEA `GO_REF:0000002`): **MODIFY** -> `GO:0016036` (`cellular response to phosphate starvation`) — PhoB1 is a cytoplasmic transcription factor that activates phosphate starvation response genes (including `pstSCAB`) rather than a membrane transporter.
- `GO:0032993` (`protein-DNA complex`, IEA `GO_REF:0000118`): **KEEP_AS_NON_CORE** — transient nucleoprotein complex when bound to Pho-box promoters.
- `GO:0001216` (`DNA-binding transcription activator activity`, IC from `file:VARPD/phoB1/phoB1-uniprot.txt`): **NEW**.
- `GO:0045893` (`positive regulation of DNA-templated transcription`, IC from `file:VARPD/phoB1/phoB1-uniprot.txt`): **NEW**.
- `GO:0016036` (`cellular response to phosphate starvation`, IC from `file:VARPD/phoB1/phoB1-uniprot.txt`): **NEW**.
