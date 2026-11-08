# Curatorial Notes for `copA2` (`A0A0H2M2H3`, `VPARA_21930`) in *Variovorax paradoxus* TBEA6

## 1. Gene & Protein Identity
- **UniProt Accession:** `A0A0H2M2H3` (`A0A0H2M2H3_VARPD`)
- **Gene Symbol:** `copA2`
- **Locus Tag / EMBL CDS:** `VPARA_21930` / `KLN56614.1` on contig `JZWI01000010` (`RefSeq:WP_047784522.1`)
- **Protein Length:** 747 aa (76,733 Da); $\text{P}_{1\text{B}-1}$-type $\text{Cu}^+$-translocating efflux ATPase (EC 7.2.2.8, transferred from EC 3.6.3.54).
- **Domain Architecture & Conserved Motifs:**
  - N-terminal cytoplasmic heavy-metal-associated (HMA) domain at residues 13–80 (`PROSITE:PS50846` `HMA_2`, `PROSITE:PS01047` `HMA_1`, `Pfam:PF00403` `HMA`, `CDD:cd00371`, `InterPro:IPR006121`) carrying the canonical $\text{Cu}^+$-binding CXXC motif `24-MTCASCV-30`.
  - Eight RuleBase-annotated transmembrane alpha-helices (`98..116`, `128..147`, `159..181`, `193..212`, `349..371`, `377..410`, `700..719`, `725..742`), with TM6 (`377..410`) housing the intramembrane metal-translocation motif `379-CPCALGLATP-388` (`Cys379-Pro380-Cys381`) and TM7/TM8 housing the $\text{P}_{1\text{B}-1}$ invariant $\text{Cu}^+$-coordinating `Tyr707-Asn708` (`706-AYNV-709`) and `Met735` (`732-SSVSVMAN-739`) residues.
  - Cytoplasmic actuator (A) domain (`Pfam:PF00122` `E1-E2_ATPase`, `InterPro:IPR008250`, containing the `269-TGES-272` phosphatase loop) and HAD-like catalytic phosphorylation (P) / nucleotide-binding (N) domain (`Pfam:PF00702` `Hydrolase`, `PROSITE:PS00154` `ATPASE_E1_E2`, `InterPro:IPR023299`) with the invariant acyl-phosphate acceptor `Asp423` (within `423-DKTGTLT-429`) and $\text{Mg}^{2+}$-binding `615-GDGVNDAPALA-625` hinge.
  - Specific family models: `NCBIfam:TIGR01511` (`ATPase-IB1_Cu`), `PANTHER:PTHR43520:SF8` (`P-TYPE CU(+) TRANSPORTER`), `FunFam:2.70.150.10:FF:000020` / `3.30.70.100:FF:000005` (`Copper-exporting P-type ATPase A`).

## 2. Note on WGS SubName vs. Physiological Directionality
- The WGS EMBL submission (`KLN56614.1`) assigned `SubName: Full=Putative copper-importing P-type ATPase A` (`EC=3.6.3.54`, transferred to `EC 7.2.2.8`) via Prokka homology to an older *Bacillus*/*Enterococcus* CopA entry. In Gram-negative Proteobacteria, $\text{P}_{1\text{B}-1}$-type CopA ATPases (`NCBIfam:TIGR01511`, `FunFam` `Copper-exporting P-type ATPase A`, `ARBA:ARBA00089529`) export monovalent $\text{Cu}^+$ from the cytoplasm across the inner membrane into the periplasm (`GO:0060003` `copper ion export`, `GO:0055070` `copper ion homeostasis`) to prevent cytoplasmic copper toxicity.

## 3. Annotation Review Decisions
- Matching our curation of `cadA2` (`A0A0H2LVW9`, `VPARA_44980`):
  - `GO:0000166` (`nucleotide binding`, IEA `GO_REF:0000002`): **TOO_GENERAL** — entailed by `GO:0005524` (`ATP binding`).
  - `GO:0005507` (`copper ion binding`, IEA `GO_REF:0000118`): **ACCEPT** — N-terminal HMA domain (`24-MTCASCV-30`) and intramembrane `379-CPC-381` translocation site.
  - `GO:0005524` (`ATP binding`, IEA `GO_REF:0000120`): **ACCEPT** — cytoplasmic N and P domains (`InterPro:IPR023299`, `PROSITE:PS00154` `423-DKTGTLT-429`).
  - `GO:0005886` (`plasma membrane`, IEA `GO_REF:0000120`): **ACCEPT** — 8-pass inner-membrane P-type ATPase.
  - `GO:0006812` (`monoatomic cation transport`, IEA `GO_REF:0000002`): **TOO_GENERAL** — entailed by `GO:0060003` (`copper ion export`).
  - `GO:0015662` (`P-type ion transporter activity`, IEA `GO_REF:0000117`): **TOO_GENERAL** — entailed by `GO:0140581` (`P-type monovalent copper transporter activity`).
  - `GO:0016020` (`membrane`, IEA `GO_REF:0000120`): **TOO_GENERAL** — entailed by `GO:0005886`.
  - `GO:0016887` (`ATP hydrolysis activity`, IEA `GO_REF:0000002`): **TOO_GENERAL** — entailed by `GO:0140581`.
  - `GO:0019829` (`ATPase-coupled monoatomic cation transmembrane transporter activity`, IEA `GO_REF:0000002`): **TOO_GENERAL** — entailed by `GO:0140581`.
  - `GO:0043682` (`P-type divalent copper transporter activity`, IEA `GO_REF:0000118`): **MODIFY** -> `GO:0140581` (`P-type monovalent copper transporter activity`) — $\text{P}_{1\text{B}-1}$ CopA ATPases (`NCBIfam:TIGR01511`, `PANTHER:PTHR43520:SF8`, EC 7.2.2.8) translocate monovalent $\text{Cu}^+$ from the reducing bacterial cytoplasm, not divalent $\text{Cu}^{2+}$.
  - `GO:0046872` (`metal ion binding`, IEA `GO_REF:0000002`): **TOO_GENERAL** — entailed by `GO:0005507` (`copper ion binding`).
  - `GO:0046915` (`transition metal ion transmembrane transporter activity`, IEA `GO_REF:0000117`): **TOO_GENERAL** — entailed by `GO:0140581`.
  - `GO:0055070` (`copper ion homeostasis`, IEA `GO_REF:0000118`): **ACCEPT** — core BP.
  - `GO:0060003` (`copper ion export`, IEA `GO_REF:0000117`): **ACCEPT** — core BP.
  - `GO:0140581` (`P-type monovalent copper transporter activity`, IEA `GO_REF:0000003`): **ACCEPT** — core MF.
