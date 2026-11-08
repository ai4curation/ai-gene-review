# Curatorial Notes for `pstB` (`A0A0D0L7E0`, `VPARA_10450`) in *Variovorax paradoxus* TBEA6

## 1. Gene & Protein Identity
- **UniProt Accession:** `A0A0D0L7E0` (`A0A0D0L7E0_VARPD`)
- **Gene Symbol:** `pstB`
- **Locus Tag / EMBL CDS:** `VPARA_10450` / `KLN58033.1` on contig `JZWI01000005` (`RefSeq:WP_021007056.1`)
- **Protein Length:** 259 aa (29,009 Da); ABC transporter nucleotide-binding domain at residues 13–254 (`PROSITE:PS50893` `ABC_TRANSPORTER_2`, `Pfam:PF00005` `ABC_tran`, `CDD:cd03260` `ABC_PstB_phosphate_transporter`).
- **Specific Family & Active-Site Conservation:**
  - `InterPro:IPR005670` (`PstB-like`), `NCBIfam:TIGR00972` (`3a0107s01c2`), `PANTHER:PTHR43423:SF3` (`PHOSPHATE IMPORT ATP-BINDING PROTEIN PSTB`).
  - Conserves the Walker A P-loop ATP-binding motif at residues 45–52 (`45-GPSGCGKS-52`, `FT BINDING 45..52 /ligand="ATP"`) containing `Gly50` and `Lys51` (corresponding to *E. coli* PstB `Gly48` and `Lys49`, whose mutation abolishes Pst phosphate transport and causes constitutive alkaline phosphatase derepression in `PMID:2646285`), the ABC signature motif `146-LSGGQQQRLCIAR-158` (`PROSITE:PS00211`), the Walker B catalytic glutamate `Glu172` (in `167-VLLLDEPCSALD-178`), and the H-loop switch histidine `His204`.

## 2. Operon Context on Contig `JZWI01000005`
- Encoded immediately between `phoU` (`VPARA_10440`, `KLN58032.1`) and `pstA` (`VPARA_10460`, `KLN58034.1`) within the `phoR1-phoB1-phoU-pstB-pstA-pstC-pstS-ppx` (`VPARA_10420`–`VPARA_10490`) phosphate regulon gene cluster.

## 3. Literature & Comparative Evidence
- **[PMID:2646285]** (Cox, Webb & Rosenberg 1989 *J Bacteriol*): Site-directed mutagenesis of *E. coli* `pstB` (`Gly48Ile`, `Lys49Gln`) abolishes Pst phosphate transport and derepresses the Pho regulon.
- **[PMID:24563032]** (Gardner et al. 2014 *J Bacteriol*): Demonstrates by bacterial two-hybrid and affinity co-elution that PstB directly interacts with PhoU at the cytoplasmic face of the inner membrane to transduce the PstSCAB conformational state to PhoR.
- **[PMID:3881386]** (Surin et al. 1985 *J Bacteriol*): Sequence and organization of `pstB` in the `phoS-pstC-pstA-pstB-phoU` operon.

## 4. Annotation Review Decisions
- Following `ECOLI/pstB` (`P0AAH0`):
  - `GO:0000166` (`nucleotide binding`, IEA `GO_REF:0000104`): **TOO_GENERAL** — entailed by `GO:0005524` (`ATP binding`).
  - `GO:0005315` (`phosphate transmembrane transporter activity`, IEA `GO_REF:0000002`, `enables`): **MARK_AS_OVER_ANNOTATED** — PstB is the cytoplasmic nucleotide-binding ATPase subunit of the PstSCAB holocomplex rather than the transmembrane pore; its contribution to `GO:0015415` (`ATPase-coupled phosphate ion transmembrane transporter activity`) is captured in `core_functions.contributes_to_molecular_function`.
  - `GO:0005524` (`ATP binding`, IEA `GO_REF:0000120`): **KEEP_AS_NON_CORE** — prerequisite cosubstrate binding for the core `GO:0016887` (`ATP hydrolysis activity`), matching `ECOLI/pstB`.
  - `GO:0005886` (`plasma membrane`, IEA `GO_REF:0000044`): **ACCEPT** — peripheral inner-membrane ATPase subunit.
  - `GO:0016020` (`membrane`, IEA `GO_REF:0000002`): **TOO_GENERAL** — entailed by `GO:0005886`.
  - `GO:0016887` (`ATP hydrolysis activity`, IEA `GO_REF:0000002`): **ACCEPT** — core molecular function of the PstB motor subunit.
  - `GO:0035435` (`phosphate ion transmembrane transport`, IEA `GO_REF:0000002`): **ACCEPT** — core biological process energized by PstB.
  - `GO:0055052` (`ATP-binding cassette (ABC) transporter complex, substrate-binding subunit-containing`, IC from `file:VARPD/pstB/pstB-uniprot.txt`): **NEW** — matching `ECOLI/pstB`.
