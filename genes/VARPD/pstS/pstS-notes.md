# Curatorial Notes for `pstS` (`A0A0H2M7F6`, `VPARA_10480`) in *Variovorax paradoxus* TBEA6

## 1. Gene & Protein Identity
- **UniProt Accession:** `A0A0H2M7F6` (`A0A0H2M7F6_VARPD`)
- **Gene Symbol:** `pstS`
- **Locus Tag / EMBL CDS:** `VPARA_10480` / `KLN58036.1` on contig `JZWI01000005` (`RefSeq:WP_047783563.1`)
- **Protein Length:** 345 aa (36,423 Da); N-terminal SignalP cleavable secretory signal peptide at residues 1–24 (`MKTTFKFAAAGLVAAAFAHVPAFA`), mature periplasmic chain at residues 25–345 (`PRO_5002596677`), Type-II periplasmic binding protein (PBP) domain at residues 26–304 (`Pfam:PF12849` `PBP_like_2`).
- **Family & Domain Architecture:**
  - `InterPro:IPR005673` (`ABC_phos-bd_PstS`), `InterPro:IPR024370` (`PBP_domain`), `InterPro:IPR050962` (`PstS-like`)
  - `CDD:cd13565` (`PBP2_PstS`), `NCBIfam:TIGR00975` (`3a0107s03`), `NCBIfam:NF008171` (`pstS`), `PIRSF:PIRSF002756` (`PstS`)
  - `PANTHER:PTHR42996:SF1` (`PHOSPHATE-BINDING PROTEIN PSTS`)

## 2. Operon & Genomic Context on Contig `JZWI01000005`
- `pstS` (`VPARA_10480`, `KLN58036.1`) lies immediately adjacent to the high-affinity phosphate transport and PhoBR two-component regulatory gene cluster on contig `JZWI01000005`:
  - `VPARA_10420` (`KLN58030.1`, `phoR1`, `A0A0H2MMT2`): Phosphate regulon sensor histidine kinase PhoR1 (464 aa)
  - `VPARA_10430` (`KLN58031.1`, `phoB1`, `A0A0H2M7F4`): Phosphate regulon response regulator PhoB1 (230 aa)
  - `VPARA_10440` (`KLN58032.1`, `phoU`, `A0A0H2MBK2`): Phosphate-specific transport system accessory regulatory protein PhoU (233 aa)
  - `VPARA_10450` (`KLN58033.1`, `pstB`, `A0A0D0L7E0`): Phosphate import ATP-binding protein PstB (259 aa)
  - `VPARA_10460` (`KLN58034.1`, `pstA`, `A0A0H2M6I3`): Phosphate transport system permease protein PstA (294 aa)
  - `VPARA_10470` (`KLN58035.1`, `pstC`, `A0A0H2MMT5`): Phosphate transport system permease protein PstC (359 aa)
  - `VPARA_10480` (`KLN58036.1`, `pstS`, `A0A0H2M7F6`): Periplasmic phosphate-binding protein PstS (345 aa)
  - `VPARA_10490` (`KLN58037.1`, `ppx`, `A0A0H2MBK5`): Exopolyphosphatase Ppx (506 aa, curated in Tranche 3)

## 3. Literature & Comparative Evidence
- **[PMID:2215649]** (Luecke & Quiocho 1990 *Nature*): 1.7 Å crystal structure of *E. coli* periplasmic phosphate-binding protein PstS showing how the hinged two-domain cleft coordinates tetrahedral orthophosphate via 12 hydrogen bonds and an aspartate carboxylate that confers strict selectivity against sulfate.
- **[PMID:6321434]** (Surin et al. 1984 *J Bacteriol*) and **[PMID:3881386]** (Surin et al. 1985 *J Bacteriol*): Sequence and organization of `phoS` (`pstS`) and the `pstS-pstC-pstA-pstB-phoU` operon in *E. coli*, establishing export of PstS to the periplasm via a cleavable N-terminal signal sequence.
- **[PMID:24563032]** (Gardner et al. 2014 *J Bacteriol*): Synthesizes the mechanism of the PstSCAB-PhoU-PhoRB complex in high-affinity $\text{P}_i$ uptake and $\text{P}_i$-sufficiency signaling.

## 4. Annotation Review Decisions
- `GO:0042301` (`phosphate ion binding`, IEA `GO_REF:0000002`): **ACCEPT** — core molecular function of periplasmic PstS (with `contributes_to_molecular_function: GO:0015415` `ATPase-coupled phosphate ion transmembrane transporter activity` on `core_functions`).
- `GO:0035435` (`phosphate ion transmembrane transport`, IEA `GO_REF:0000002`): **ACCEPT** — core biological process; PstS captures orthophosphate in the periplasm and delivers it to the PstCA permease channel.
- `GO:0043190` (`ATP-binding cassette (ABC) transporter complex`, IEA `GO_REF:0000002`): **MODIFY** -> `GO:0055052` (`ATP-binding cassette (ABC) transporter complex, substrate-binding subunit-containing`) — refines the generic ABC transporter complex term to the specific child complex that includes the periplasmic substrate-binding subunit (matching `ECOLI/pstS`, `ECOLI/pstC`, `ECOLI/pstA`, `ECOLI/pstB`).
- `GO:0030288` (`outer membrane-bounded periplasmic space`, IC from `file:VARPD/pstS/pstS-uniprot.txt`): **NEW** — *V. paradoxus* is a diderm Betaproteobacterium and VPARA_10480 carries a canonical 24-aa SignalP signal peptide (`FT SIGNAL 1..24`) for export of mature PstS (`25..345`) to the outer membrane-bounded periplasmic space.
- `GO:0055052` (`ATP-binding cassette (ABC) transporter complex, substrate-binding subunit-containing`, IC from `file:VARPD/pstS/pstS-uniprot.txt`): **NEW** — asserted alongside the modified `GO:0043190` row.
