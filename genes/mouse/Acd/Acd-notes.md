# Acd (Q5EE38) Curation Notes — Mouse Shelterin Subunit TPP1

## 1. Gene & Protein Overview

- **Organism & Identifiers**: *Mus musculus* `Acd` (`MGI:87873`, `UniProtKB:Q5EE38`, sequence version 1, **416 aa**; `PANTHER:PTHR14487` / `PANTHER:PTHR14487:SF3` `ADRENOCORTICAL DYSPLASIA PROTEIN HOMOLOG`), commonly referred to in mouse telomere biology as **Tpp1** or **Acd**.
- **Conserved Domain & Residue Architecture**:
  - Unlike human `ACD`, which produces both a 458-aa somatic `TPP1-S` (`Q96AP0`) and a spermatid-enriched 544-aa `TPP1-L` isoform (`PMID:31216472`), mouse `Q5EE38` initiates directly at the conserved NOB (N-terminal of OB) start (`MSDSGLLALQPWIRELIL...`, 416 aa) and lacks the primate-type 86-aa basic upstream extension.
  - **NOB motif**: `P11-W12-I13` (`LLALQPWIRELIL`, positions 11–13 in `Q5EE38` SV 1, identical 1-based coordinates to human `Q96AP0`).
  - **TEL patch acidic loop**: `D78-W79-E80-E81-K82-E83` (`DWEEKE` at positions 78–83 in `Q5EE38` SV 1, shifted by −2 relative to `D80–E85` in human `Q96AP0`), plus `R92` and `L95`.
  - **POT1a/POT1b-interacting domain**: `aa 156–245` (`FT REGION 156..245`). Rodents underwent duplication of *Pot1* into *Pot1a* (repressing ATR DNA damage signaling at telomeres) and *Pot1b* (preventing excessive 5' C-strand resection / regulating 3' overhang length), and mouse Acd/TPP1 is required to tether **both** POT1a and POT1b to telomeres (`PMID:17053789`, `PMID:17632522`, `PMID:22101936`).
  - **TIN2-interacting C-terminus** & **STN1 (CST) interaction** (`PMID:19648609`).

## 2. Genetics of the *acd* Hypomorphic Mutant vs. Conditional Nulls

1. **Spontaneous *acd* splice-donor hypomorph (`PMID:15537664`, `PMID:18185984`, `PMID:19660449`, `PMID:22038471`)**:
   - Positional cloning by Keegan et al. 2005 (`PMID:15537664`) identified an intronic splice-donor mutation in *Acd* as the cause of autosomal recessive *adrenocortical dysplasia* (*acd*), characterized by adrenocortical hypoplasia, urogenital ridge malformations, caudal regression/vertebral segmentation defects, and preaxial/postaxial limb anomalies.
   - Else et al. 2008 (`PMID:18185984`) showed that *acd/acd* MEFs exhibit telomere deprotection, DNA damage foci (TIFs), and end-to-end chromosome/chromatid fusions (`GO:0016233` `telomere capping`, `GO:0031848` `protection from non-homologous end joining at telomere`).
   - Crucially, Vlangos et al. 2009 (`PMID:19660449`) proved that the skeletal, caudal-axis, and limb malformations in *acd* embryos are caused by **p53-dependent apoptosis** downstream of telomere dysfunction and are rescued on a *Trp53*⁻/⁻ background (whereas *TAp63* loss does not rescue them, `PMID:22038471`). Thus, the MGI `IMP` annotations to `GO:0001501` (`skeletal system development`), `GO:0001655` (`urogenital system development`), `GO:0030326` (`embryonic limb morphogenesis`), and `GO:0035282` (`segmentation`) with qualifier `acts_upstream_of_or_within` represent pleiotropic downstream consequences of telomere uncapping in rapidly proliferating progenitors rather than direct morphogenetic roles (`KEEP_AS_NON_CORE`).

2. **Conditional *Acd* knockdown/knockout in MEFs and stem cells (`PMID:17632522`, `PMID:22101936`, `PMID:24316971`)**:
   - Depletion or deletion of *Acd* in MEFs (`PMID:17632522`, `PMID:22101936`, `PMID:24316971`) abolishes POT1a and POT1b localization to telomeres, unleashing ATR-dependent telomere DNA damage signaling, excess 3' G-overhang generation, and non-homologous end joining fusions.
   - In hematopoietic stem cells (`PMID:24316971`), acute *Acd* deletion causes rapid cell-cycle arrest and stem-cell depletion that is NOT rescued by *Trp53* deletion.

## 3. Key Annotation Decisions (Harmonized with `human/ACD` and `PANTHER:PTHR14487`)

- **`ACCEPT` (core)**: `GO:0070187` (`shelterin complex`), `GO:0016233` (`telomere capping`), `GO:0031848` (`protection from non-homologous end joining at telomere`), `GO:0007004` (`telomere maintenance via telomerase`), `GO:0032211` (`negative regulation of telomere maintenance via telomerase`), `GO:0070198` (`protein localization to chromosome, telomeric region`), `GO:0070200` (`establishment of protein localization to telomere`), `GO:0032202` (`telomere assembly`), `GO:0070182` (`DNA polymerase binding`).
- **`MODIFY` (refinement)**:
  - `GO:0005515` (`protein binding` IPI with Pot1a/Pot1b `PMID:17053789` and Stn1 `PMID:19648609`) → `GO:0060090` (`molecular adaptor activity`).
  - `GO:0000781` (`chromosome, telomeric region`) → `GO:0140445` (`chromosome, telomeric repeat region`).
  - `GO:0000783` (`nuclear telomere cap complex`) → `GO:0070187` (`shelterin complex`).
  - `GO:0000723` (`telomere maintenance`) → `GO:0016233` (`telomere capping`) and `GO:0007004` (`telomere maintenance via telomerase`).
  - `GO:0006886` (`intracellular protein transport`, `ISO`/`IEA` from `PMID:15181449`) → `GO:0070200` (`establishment of protein localization to telomere`).
  - `GO:0032206` (`positive regulation of telomere maintenance`, `NAS`) → `GO:0032212` (`positive regulation of telomere maintenance via telomerase`).
- **`KEEP_AS_NON_CORE`**: `GO:0005634` (`nucleus`), `GO:0005654` (`nucleoplasm`), `GO:0016604` (`nuclear body`), `GO:0044877` (`protein-containing complex binding`), and `acts_upstream_of_or_within` developmental phenotypes (`GO:0001501`, `GO:0001655`, `GO:0030326`, `GO:0035282`).
- **`REMOVE` (refuted / mis-propagated)**:
  - `GO:0005697` (`telomerase holoenzyme complex`, `IEA` `IPR019437`): shelterin subunit, not a telomerase holoenzyme subunit (`PMID:35201900`).
  - `GO:0042162` (`telomeric repeat DNA binding`, `IBA`/`IDA`/`IEA`/`ISO`): `PMID:23685356` pulled down whole shelterin from nuclear extract on ds-`TTAGGG` DNA; purified TPP1/Acd does not contact DNA (`PMID:31216472`, `PMID:35201900`), whereas POT1a/POT1b bind ssDNA (`PMID:17053789`, `PMID:17632522`).
  - `GO:0010521` (`telomerase inhibitor activity`, `ISO`/`IEA` from human `PMID:25172512`): unsupported in source paper and opposite to Acd/TPP1's direct telomerase-stimulating activity.
  - `GO:0070203` (`regulation of establishment of protein localization to telomere`, `ISO`/`IEA` from human `PMID:25172512`): propagated from an erroneous BHF-UCL `IDA` on `PMID:25172512` (which assayed TPP1's own localization upon deubiquitinase perturbation, whereas Acd directly mediates `GO:0070200` for POT1a/b and TERT).
