# Curatorial Notes for `act` (`B9U6P4`, `VPARA_05450`) in *Variovorax paradoxus* TBEA6

## 1. Gene & Protein Identity
- **UniProt Accession:** `B9U6P4` (`B9U6P4_VARPD`)
- **Gene Symbol:** `act`
- **Locus Tag / EMBL CDS:** `VPARA_05450` / `KLN58430.1` on contig `JZWI01000003` (`MetaCyc:MONOMER-18547`, `RefSeq:WP_047783181.1`)
- **Protein Length:** 398 aa (43,322 Da); family III acyl-CoA transferase (`Pfam:PF02515` `CoA_transf_3`, `InterPro:IPR003673` `CoA-Trfase_fam_III`, `InterPro:IPR050483`, `SUPFAM:SSF89796`, `PANTHER:PTHR48207:SF3`).

## 2. Operon & Direct Experimental Evidence in *Variovorax paradoxus* TBEA6
- Encoded on contig `JZWI01000003` (`KLN58430.1`) immediately adjacent to `acd` (`VPARA_05440`, `KLN58429.1`, `UniProtKB:B9U6P5`, 3-sulfinopropionyl-CoA desulfinase, characterized in `PMID:24317404` and curated in Tranche 1) and in the same gene cluster as `mdo` (`VPARA_05600`, `KLN58445.1`, `UniProtKB:B9U5L8`) and `fox` (`VPARA_05580`, `KLN58443.1`, `UniProtKB:A0A0H2M811`).
- **[PMID:19001372]** (Bruland, Wübbeler & Steinbüchel 2009 *J Biol Chem*):
  - Directly characterized `act` (`VPARA_05450`) in *Variovorax paradoxus* TBEA6 via `Tn5::mob` transposon mutagenesis:
    > "Insertion of Tn5::mob in a gene putatively coding for a family III acyl-CoA-transferase resulted in the accumulation of 3-sulfinopropionate during cultivation on 3,3-thiodipropionic acid, indicating that this compound is further metabolized to 3-sulfinopropionyl-CoA and subsequently to propionyl-CoA."
- **[PMID:24317404]** (Schürmann et al. 2014 *J Bacteriol*): Confirms that the 3-sulfinopropionyl-CoA (3SP-CoA) generated from 3-sulfinopropionate (3SP) is desulfinated to propionyl-CoA and sulfite by the adjacent Acd (`VPARA_05440`, `B9U6P5`).

## 3. Annotation Review Decisions & Source Defect
- `GO:0003824` (`catalytic activity`, IEA `GO_REF:0000002`, `enables`, `InterPro:IPR003673`): **TOO_GENERAL** — entailed by `GO:0008410` (`CoA-transferase activity`).
- `GO:0008410` (`CoA-transferase activity`, IEA `GO_REF:0000120`, `enables`, `ARBA:ARBA00085262`, `PANTHER:PTN008734856`): **ACCEPT** — core molecular function (`Pfam:PF02515` `CoA_transf_3`, `InterPro:IPR003673`), with a `proposed_new_terms` entry for `succinyl-CoA:3-sulfinopropionate CoA-transferase activity`.
- `GO:0033877` (`succinyl-CoA:(R)-benzylsuccinate CoA-transferase activity`, IEA `GO_REF:0000003`, `enables`, `EC:2.8.3.15`): **REMOVE** — automated WGS/EMBL EC 2.8.3.15 mis-assignment (`DE EC=2.8.3.15 {ECO:0000313|EMBL:KLN58430.1}`). Succinyl-CoA:(R)-benzylsuccinate CoA-transferase (BbsEF, EC 2.8.3.15) is a two-subunit enzyme of anaerobic toluene catabolism, whereas *V. paradoxus* TBEA6 Act (`B9U6P4`, `VPARA_05450`) is a single-polypeptide family III CoA-transferase directly shown by `Tn5::mob` mutagenesis (`PMID:19001372`) to convert 3-sulfinopropionate to 3-sulfinopropionyl-CoA during aerobic 3,3'-thiodipropionic acid catabolism. Record a `source_defects` (`WRONG_TERM` on `UNIPROT`) on `file:VARPD/act/act-uniprot.txt`.
- `GO:0044273` (`sulfur compound catabolic process`, IMP from `PMID:19001372`, `involved_in`): **NEW** — directly demonstrated by `Tn5::mob` insertion in `act` causing accumulation of 3-sulfinopropionate during growth on 3,3'-thiodipropionic acid (`PMID:19001372`).
- `GO:0005829` (`cytosol`, IC from `file:VARPD/act/act-uniprot.txt`, `located_in`): **NEW** — soluble 398-aa cytoplasmic enzyme acting immediately upstream of cytosolic Acd (`VPARA_05440`).
