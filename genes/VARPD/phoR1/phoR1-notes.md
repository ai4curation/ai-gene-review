# Curatorial Notes for `phoR1` (`A0A0H2MMT2`, `VPARA_10420`) in *Variovorax paradoxus* TBEA6

## 1. Gene & Protein Identity
- **UniProt Accession:** `A0A0H2MMT2` (`A0A0H2MMT2_VARPD`)
- **Gene Symbol:** `phoR1`
- **Locus Tag / EMBL CDS:** `VPARA_10420` / `KLN58030.1` on contig `JZWI01000005` (`RefSeq:WP_021007059.1`)
- **Protein Length:** 464 aa (50,842 Da); inner-membrane bifunctional sensor histidine kinase / phospho-PhoB1 phosphatase (EC 2.7.13.3).
- **Domain Architecture & Active Sites:**
  - N-terminal transmembrane anchor (`FT TRANSMEM 29..45` / PhoR N-terminal transmembrane domain `Pfam:PF11808` `PhoR`, `InterPro:IPR021766` `PhoR_N`).
  - Cytoplasmic Per-ARNT-Sim (PAS) sensory domain (`Pfam:PF00989` `PAS`, `CDD:cd00130`, `InterPro:IPR000014` / `IPR013767`), which directly interacts with PhoU (`VPARA_10440`) to sense the PstSCAB phosphate-transport state (`PMID:24563032`).
  - Histidine kinase dimerization/phosphoacceptor (DHp, `HisKA`, `Pfam:PF00512`, `CDD:cd00082`, `InterPro:IPR003661`) and catalytic ATP-binding (`HATPase_c`, `Pfam:PF02518`, `InterPro:IPR003594`) domains (`FT DOMAIN 216..436 /note="Histidine kinase"`, `PROSITE:PS50109`), with the invariant autocatalytic phosphohistidine acceptor `His219` (`FT MOD_RES 219 /note="Phosphohistidine; by autocatalysis"` within `215-NVSHEIRTPL-224`).
  - Full-length orthology: `NCBIfam:TIGR02966` (`phoR_proteo`), `InterPro:IPR014310` (`Sig_transdc_His_kinase_PhoR`), `PANTHER:PTHR45453:SF1` (`PHOSPHATE REGULON SENSOR PROTEIN PHOR`).

## 2. Operon Context on Contig `JZWI01000005`
- Encoded immediately adjacent to `phoB1` (`VPARA_10430`, `KLN58031.1`) at the boundary of the `phoR1-phoB1-phoU-pstB-pstA-pstC-pstS-ppx` (`VPARA_10420`–`VPARA_10490`) phosphate regulon gene cluster.

## 3. Literature & Comparative Evidence
- **[PMID:24563032]** (Gardner et al. 2014 *J Bacteriol*): Establishes that PhoR is an integral inner-membrane bifunctional histidine autokinase and phospho-PhoB phosphatase whose cytoplasmic PAS domain physically interacts with PhoU to switch between phosphatase activity (under high external $\text{P}_i$, when PstSCAB is in its high-activity state) and autokinase/phosphotransferase activity (under limiting external $\text{P}_i$).

## 4. Annotation Review Decisions
- `GO:0000155` (`phosphorelay sensor kinase activity`, IEA `GO_REF:0000120`): **ACCEPT** — core MF (`PROSITE:PS50109` `216..436`, `His219` phosphohistidine site).
- `GO:0000160` (`phosphorelay signal transduction system`, IEA `GO_REF:0000002`): **ACCEPT** — core BP.
- `GO:0004673` (`protein histidine kinase activity`, IEA `GO_REF:0000120`): **TOO_GENERAL** — parent of `GO:0000155`.
- `GO:0004721` (`phosphoprotein phosphatase activity`, IEA `GO_REF:0000120`): **ACCEPT** — core second catalytic activity of bifunctional PhoR1 toward phospho-PhoB1 under phosphate-replete conditions (`PMID:24563032`).
- `GO:0005886` (`plasma membrane`, IEA `GO_REF:0000120`): **ACCEPT** — core CC (`FT TRANSMEM 29..45`).
- `GO:0006355` (`regulation of DNA-templated transcription`, IEA `GO_REF:0000002`): **KEEP_AS_NON_CORE** — PhoR1 regulates transcription indirectly upstream of its response regulator partner PhoB1.
- `GO:0007165` (`signal transduction`, IEA `GO_REF:0000120`): **TOO_GENERAL** — entailed by `GO:0000160`.
- `GO:0016020` (`membrane`, IEA `GO_REF:0000002`): **TOO_GENERAL** — entailed by `GO:0005886`.
- `GO:0016036` (`cellular response to phosphate starvation`, IEA `GO_REF:0000118`): **ACCEPT** — core BP.
- `GO:0016301` (`kinase activity`, IEA `GO_REF:0000104`): **TOO_GENERAL** — entailed by `GO:0000155`.
- `GO:0016740` (`transferase activity`, IEA `GO_REF:0000104`): **TOO_GENERAL** — entailed by `GO:0000155`.
- `GO:0016772` (`transferase activity, transferring phosphorus-containing groups`, IEA `GO_REF:0000002`): **TOO_GENERAL** — entailed by `GO:0000155`.
