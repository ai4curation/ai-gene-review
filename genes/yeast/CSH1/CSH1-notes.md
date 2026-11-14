# CSH1 (P38287, YBR161W) notes

Module: `sphingolipid_de_novo_synthesis`, MIPC synthase (Csg1/Sur1 paralog). Missing from YeastCyc SPHINGOLIPID-SYN-PWY-1 (only SUR1 listed).

## Evidence journal
- Redundancy [PMID:12954640 "Deltacsg1 cells exhibited only a reduction in the synthesis of mannosylated sphingolipids compared with wild-type cells, whereas the Deltacsg1 Deltacsh1 double deletion mutant exhibited a total loss"]
- Distinct specificity [PMID:12954640 "demonstrated that Csh1p has a different substrate specificity from Csg1p"]
- Csg2 dependence [PMID:12954640 "Deletion of the CSG2 gene reduced the Csg1p activity and abolished the Csh1p activity"]
- Vacuole membrane GFP (Huh), heterodimer with Csg2 [UniProt:P38287]
- 2022 N-glycan follow-up: Sur1 and Csh1 N-glycans tune synthesis of
  different MIPC subtypes rather than changing the core IPC-to-MIPC reaction
  [PMID:35713525 "Sur1 N224Q and Csh1 N51Q mutants exhibited a decrease in
  the activity to synthesize specific MIPC subtypes for each enzyme"]
- 2026 ethanol-stress follow-up: `csg1D csh1D` MIPC-deficient cells are
  ethanol-hypersensitive and lose viability, but this is downstream of MIPC
  loss and does not make either IPC mannosyltransferase a direct
  ethanol-response or cell-wall-integrity-pathway component [PMID:42169399
  "Cells lacking the MIPC synthases Csg1 and Csh1 exhibited pronounced ethanol
  hypersensitivity and loss of viability"]

## Decisions
- Core MF GO:0103064, BP GO:0051999, complex GO:0031501, Golgi apparatus (IDA). Vacuole rows KEEP_AS_NON_CORE (conflict flagged).
- M(IP)2C metabolic process rows MARK_AS_OVER_ANNOTATED (Csh1 makes the MIPC precursor; Ipt1 makes M(IP)2C).
- Generic mannosyltransferase IBA MODIFY to GO:0103064; PTHR32385 MIPC-biosynthesis IBA ACCEPT; protein binding (Csg2) REMOVE.
