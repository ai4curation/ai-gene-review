# Curatorial Notes for `zur` (`A0A0H2LYR2`, `VPARA_33720`) in *Variovorax paradoxus* TBEA6

## 1. Gene & Protein Identity
- **UniProt Accession:** `A0A0H2LYR2` (`A0A0H2LYR2_VARPD`)
- **Gene Symbol:** `zur`
- **Locus Tag / EMBL CDS:** `VPARA_33720` / `KLN55348.1` on contig `JZWI01000017` (`RefSeq:WP_021008287.1`)
- **Protein Length:** 149 aa (16,287 Da); homodimeric Fur-family zinc uptake transcriptional repressor Zur (`PANTHER:PTHR33202` `ZINC UPTAKE REGULATION PROTEIN`, `Pfam:PF01475` `FUR`, `CDD:cd07153` `Fur_like`, `InterPro:IPR002481` `FUR`).
- **Domain Architecture & Metal-Binding Sites:**
  - N-terminal winged-helix DNA-binding domain (`Gene3D:1.10.10.10`, `InterPro:IPR036388` / `IPR036390`, `SUPFAM:SSF46785`).
  - C-terminal dimerization and metal-binding domain (`InterPro:IPR043135` `Fur_C`) housing two metal-coordination sites per subunit:
    1. Structural $\text{Zn}^{2+}$ site coordinated by four conserved cysteines at `Cys96`, `Cys99` (`96-CGSC-99`), `Cys133`, and `Cys136` (`133-CAAC-136`; `FT BINDING 96, 99, 133, 136 /ligand="Zn(2+)"`, `PIRSR:PIRSR602481-1`).
    2. Regulatory metal-sensing site including `His90` (within the histidine-rich `87-HHHHYFH-93` motif) and `His125` (`124-SHEVT-128`).

## 2. Note on Automated RuleBase / PIRSR Fur-Superfamily Conflation
- Because `VPARA_33720` belongs to the Fur superfamily (`InterPro:IPR002481`), automated UniProt rules `RuleBase:RU364037` and `PIRSR:PIRSR602481-2` assigned the generic family name `RecName: Full=Ferric uptake regulation protein` (`Synonyms=fur`) and `Name=Mn(2+)` / `Name=Fe(2+)` cofactor binding at `His90` and `His125`.
- However, the WGS genome annotation (`EMBL:KLN55348.1`) specifically identifies `VPARA_33720` as `zur` (zinc uptake regulator), `PANTHER:PTHR33202:SF14` (`PTHR33202`) classifies it under `ZINC UPTAKE REGULATION PROTEIN`, and *V. paradoxus* TBEA6 encodes its dedicated ferric uptake regulator `fur1` at `VPARA_18200` (`A0A0H2M8T9`, curated in Tranche 4). Record a `source_defects` (`WRONG_STATEMENT`) on `file:VARPD/zur/zur-uniprot.txt`!

## 3. Annotation Review Decisions
- Matching our curation of `fur1` (`A0A0H2M8T9`, `VPARA_18200`):
  - `GO:0000976` (`transcription cis-regulatory region binding`, IEA `GO_REF:0000118`): **ACCEPT** — core MF.
  - `GO:0003677` (`DNA binding`, IEA `GO_REF:0000104`): **TOO_GENERAL** — entailed by `GO:0000976`.
  - `GO:0003700` (`DNA-binding transcription factor activity`, IEA `GO_REF:0000120`): **MODIFY** -> `GO:0001217` (`DNA-binding transcription repressor activity`).
  - `GO:0005737` (`cytoplasm`, IEA `GO_REF:0000044`): **TOO_GENERAL** — entailed by `NEW` `GO:0005829` (`cytosol`).
  - `GO:0006355` (`regulation of DNA-templated transcription`, IEA `GO_REF:0000002`): **TOO_GENERAL** — entailed by `GO:0045892` (`negative regulation of DNA-templated transcription`).
  - `GO:0008270` (`zinc ion binding`, IEA `GO_REF:0000118`): **ACCEPT** — core MF (`Cys96/Cys99/Cys133/Cys136` structural $\text{Zn}^{2+}$ site plus regulatory $\text{Zn}^{2+}$-sensing site).
  - `GO:0045892` (`negative regulation of DNA-templated transcription`, IEA `GO_REF:0000118`): **ACCEPT** — core BP.
  - `GO:1900376` (`regulation of secondary metabolite biosynthetic process`, IEA `GO_REF:0000118`): **MARK_AS_OVER_ANNOTATED** — propagated by TreeGrafter (`PANTHER:PTN009142137`) from Fur-family siderophore regulators; while Fur1 (`VPARA_18200`) represses siderophore biosynthesis, Zur (`VPARA_33720`) regulates cellular zinc uptake and homeostasis.
  - `GO:0001217` (`DNA-binding transcription repressor activity`, IC from `file:VARPD/zur/zur-uniprot.txt`): **NEW**.
  - `GO:0006882` (`cellular zinc ion homeostasis`, IC from `file:VARPD/zur/zur-uniprot.txt`): **NEW**.
  - `GO:0005829` (`cytosol`, IC from `file:VARPD/zur/zur-uniprot.txt`): **NEW**.
