# Curation Notes for `ssuA2` (`VPARA_09270`, `A0A0H2M784`) in *Variovorax paradoxus* TBEA6

## 1. Gene & Protein Overview
- **UniProtKB Accession:** `A0A0H2M784` (`A0A0H2M784_VARPD`, unreviewed, 319 aa, 33,241 Da)
- **Gene Symbol / Locus Tag:** `ssuA2` / `VPARA_09270` (`EMBL:KLN57916.1` on genomic contig `JZWI01000005`, `RefSeq:WP_021006431.1`)
- **Organism:** *Variovorax paradoxus* strain TBEA6 (`NCBITaxon:34073`)
- **Genomic Context:** Encoded on contig `JZWI01000005` within the aliphatic sulfonate uptake and desulfonation gene cluster spanning `ssuB2` (`VPARA_09230`, `KLN57912.1`), `ssuC5` (`VPARA_09240`, `KLN57913.1`), `ssuD` (`VPARA_09250`, `KLN57914.1`), `ssuA2` (`VPARA_09270`, `KLN57916.1`), and `ssuE` (`VPARA_09290`, `KLN57918.1`).
- **Domain Architecture & Targeting:**
  - N-terminal Twin-arginine translocation (Tat) signal peptide (`PROSITE:PS51318`, residues `1..29`, `1-MTSISVPRRRLLQGAAAAAIALPSFAALA-29`) containing the canonical twin-arginine motif `Arg8-Arg9-Arg10` (`8-RRRLLQ-13`), directing export of the folded precursor across the inner membrane into the periplasm.
  - Mature periplasmic substrate-binding domain (residues `30..319`): `NCBIfam:TIGR01728` (`ssuA`, aliphatic sulfonates-binding protein), `InterPro:IPR010067` (`Aliphatic_sulfonates-bd_SsuA`), `PANTHER:PTHR30024:SF42` (`ALIPHATIC SULFONATES-BINDING PROTEIN-RELATED`), and periplasmic binding protein-like II superfamily (`InterPro:IPR028082`, `SUPFAM:SSF53850`).

## 2. Literature & Comparative Evidence
- **[PMID:10781534](https://pubmed.ncbi.nlm.nih.gov/10781534/) (Eichhorn, van der Ploeg & Leisinger 2000, *J Bacteriol* 182:2687-2695):** Deletion and complementation analysis of the *Escherichia coli* `tauABCD` and `ssuEADCB` gene clusters established that SsuABC forms a dedicated ABC-type uptake system for aliphatic sulfonates that is functionally distinct from and non-exchangeable with TauABC (`"the individual components of the two transport systems were not functionally exchangeable"`).
- **[PMID:10781557](https://pubmed.ncbi.nlm.nih.gov/10781557/) (Kahnert et al. 2000, *J Bacteriol* 182:2869-2878):** Characterized the `ssuEADCBF` operon in *Pseudomonas putida* S-313, identifying `ssuA`, `ssuB`, and `ssuC` as the periplasmic binding, ATP-binding, and membrane permease subunits of the ABC-type sulfonate importer supplying the SsuED monooxygenase system (`"The first group consists of ssuA , ssuB , and ssuC , which are the genes for a putative ATP-binding cassette (ABC)-type transport system."`).

## 3. Review of Existing GOA Annotations (4 IEA rows)
1. **`GO:0016020` (`membrane`, `located_in`, IEA `GO_REF:0000002` from `InterPro:IPR010067`)** -> **`REMOVE`**:
   - Incorrect InterPro2GO propagation (`WRONG_TERM` / `SCOPE_OVER_REACH`) from `InterPro:IPR010067` (`ABC_SsuA_sub-bd`); mature SsuA2 (`residues 30..319`) is a soluble periplasmic solute-binding protein lacking transmembrane helices, localizing to `GO:0030288` (`outer membrane-bounded periplasmic space`).
2. **`GO:0042597` (`periplasmic space`, `located_in`, IEA `GO_REF:0000044` from `UniProtKB-SubCell:SL-0200`)** -> **`MODIFY` to `GO:0030288` (`outer membrane-bounded periplasmic space`)**:
   - Refined to `GO:0030288` (`outer membrane-bounded periplasmic space`) for this diderm Gram-negative betaproteobacterial periplasmic binding protein following cleavage of the N-terminal Tat signal peptide (`residues 1..29`, `PROSITE:PS51318`).
3. **`GO:0042626` (`ATPase-coupled transmembrane transporter activity`, `enables`, IEA `GO_REF:0000002` from `InterPro:IPR010067`)** -> **`MARK_AS_OVER_ANNOTATED`**:
   - `GO:0042626` describes the ATP-driven transmembrane transport activity of the intact SsuABC complex (`GO:0055052`) rather than the soluble periplasmic substrate-binding subunit SsuA2 alone. Its complex-level contribution is recorded via `contributes_to_molecular_function` (`GO:0042959`) in `core_functions`.
4. **`GO:0055085` (`transmembrane transport`, `involved_in`, IEA `GO_REF:0000108` from `GO:0042626`)** -> **`MODIFY` to `GO:0042918` (`alkanesulfonate transmembrane transport`)**:
   - Refined to `GO:0042918` (`alkanesulfonate transmembrane transport`) based on `NCBIfam:TIGR01728`, `PANTHER:PTHR30024:SF42`, and syntenic clustering in the `ssuB2-ssuC5-ssuD-...-ssuA2-...-ssuE` locus (`UniProtKB:A0A0H2MBB8`, `UniProtKB:A0A0H2M6G6`, `UniProtKB:A0A0H2MCI3`, `UniProtKB:A0A0H2M6H0`).

## 4. Proposed New Annotations
- **`GO:0055052` (`ATP-binding cassette (ABC) transporter complex, substrate-binding subunit-containing`, `part_of`, IC from `file:VARPD/ssuA2/ssuA2-uniprot.txt` and `PMID:10781557`)** -> **`NEW`**:
   - SsuA2 (`VPARA_09270`, `EMBL:KLN57916.1`) is encoded in the same contig `JZWI01000005` cluster as the ATPase subunit `ssuB2` (`VPARA_09230`, `UniProtKB:A0A0H2MBB8`, `KLN57912.1`) and the permease subunit `ssuC5` (`VPARA_09240`, `UniProtKB:A0A0H2M6G6`, `KLN57913.1`), assembling into the substrate-binding-subunit-containing ABC importer complex (`GO:0055052`).
