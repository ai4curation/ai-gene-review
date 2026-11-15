# Curation Notes for Drosophila melanogaster Arfrp1 (UniProtKB:Q9W389, FB:FBgn0030088)

## 1. Gene Identity, Sequence Conservation, and Fly Pathway Context
- **Symbol / Accession**: `Arfrp1` (`UniProtKB:Q9W389`, `FB:FBgn0030088`, `CG7039`), 200 aa, single 1:1 *Drosophila melanogaster* ortholog of human `ARFRP1` (`Q13795`) and budding yeast `ARL3` (`Q02804`) in `PANTHER:PTHR45909:SF1` (`PTN000196303`).
- **Conserved Functional Motifs**:
  - N-terminal NatC/SYS1-binding amphipathic helix `1-MYTLMHGFYKYMTQ-14` preserving `Met1-Tyr2`.
  - P-loop Walker A `24-GLDNAGKT-31` (`Lys30`, `Thr31`), Switch II catalytic `75-DLGGQ-79` (`Gln79`), and G4 `134-NKQD-137`.
- **Conserved Fly Partner Machinery**:
  - *Drosophila* encodes all components of the ARFRP1 targeting and effector axis: the NatC catalytic subunit `Naa30A` (`CG11412`, `PMID:37891180`), the Golgi receptor `Sys1` (`CG7578`), downstream trans-Golgi `Arl1` (`Arf72A`, `FBgn0035866`, which recruits `Sec71` and GRIP-domain golgins to the trans-Golgi, `PMID:19001129`, `PMID:22291037`), and GRIP golgins.

## 2. Literature Search & ND Annotation Verification (`GO:0005575`, `GO:0008150`)
- FlyBase has no hand-written curated gene summary for `FBgn0030088` (`mod-description-deep-research` returned `no_curated: 1`).
- Literature searches of PubMed and cached FlyBase/UniProt references for `"CG7039"`, `"FBgn0030088"`, and `"Drosophila" AND ("Arfrp1" OR "ARP1")` on 2026-11-15 identified `PMID:22291037` (Christis & Munro 2012, which replaced the N-terminal amphipathic helix of `CG7039` with a His10 tag for in vitro liposome pull-down assays alongside `Arf79F`, `Arf102F`, and `Arf72A`/`Arl1` without detecting differential `CG7039` effectors or assaying endogenous in vivo localization), `PMID:19001129` (Sinka et al. 2008 on *Drosophila* golgins and `Arl1`), and `PMID:37891180` (2023 study of *Drosophila* NatC `CG11412` noting human `ARFRP1`/yeast `Arl3` in background prose), with zero published in vivo experimental assays of *Drosophila* `Arfrp1` (`CG7039`) subcellular localization or biological process in *D. melanogaster*.
- Search log (2026-11-15): PubMed and FlyBase literature queries for CG7039, FBgn0030088, and Drosophila Arfrp1 or ARP1 retrieved PMID:22291037 (Christis and Munro 2012, which expressed His10-tagged truncated CG7039 on liposomes in vitro without detecting candidate effectors and did not assay endogenous subcellular localization or in vivo biological process in Drosophila), PMID:19001129 (Sinka et al. 2008 on Drosophila golgins and Arl1), and PMID:37891180 (2023 study of Drosophila NatC CG11412 mentioning human ARFRP1 and yeast Arl3 only as background examples), confirming that no published study in Drosophila melanogaster establishes an in vivo cellular component or biological process for Arfrp1.
- Accordingly, per `projects/NO_DATA.md`, both FlyBase `ND` (`GO_REF:0000015`) rows—`GO:0005575` (`cellular_component`) and `GO:0008150` (`biological_process`)—are **accepted (`ACCEPT`)** with `nd_case: INFERABLE`, because no direct *D. melanogaster* experimental literature identifies a cellular component or biological process for `CG7039`, while `IBA`/`IEA` orthology rows do not make an `ND` stale.

## 3. Automated TrEMBL Annotation Defects in `Arfrp1-uniprot.txt`
- Two automated TrEMBL rules in `file:DROME/Arfrp1/Arfrp1-uniprot.txt` produce false statements recorded in `references[].reference_review.source_defects`:
  1. `ARBA:ARBA00037377` (`CC -!- FUNCTION`): asserts `"Required for the lipidation of chylomicrons in the intestine and required for VLDL lipidation in the liver."`—mammalian organ/lipoprotein phenotypes (chylomicrons, VLDL, vertebrate liver) absent in insects, which lack a vertebrate liver and transport dietary lipids via lipophorin in hemolymph rather than chylomicrons/VLDLs.
  2. `PROSITE-ProRule:PRU00753` (`CC -!- SIMILARITY`): asserts `"Belongs to the small GTPase superfamily. Rab family."`—misclassifying an Arf-family GTPase (`IPR006689`/`PS51417`/`PTHR45909:SF1`) as a Rab-family GTPase.

## 4. Key Annotation Decisions
- **`GO:0003924`, `GO:0005525`, `GO:0005794`, `GO:0006886`, `GO:0034067`, `GO:0043001`**: `ACCEPT`.
- **`GO:0005575` (`ND`), `GO:0008150` (`ND`)**: `ACCEPT` with `nd_case: INFERABLE`.
- **`GO:0016020` (`membrane`, `IEA` `ARBA00028763`)**: `MODIFY` to `GO:0000139` (`Golgi membrane`).
- **`GO:0016192` (`vesicle-mediated transport`, `IEA` `ARBA00028249`)**: `MODIFY` to `GO:0043001` (`Golgi to plasma membrane protein transport`).
- **`GO:0051649` (`establishment of localization in cell`, `IEA` `ARBA00028679`)**: `MODIFY` to `GO:0006886` (`intracellular protein transport`).
