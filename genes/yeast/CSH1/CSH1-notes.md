# CSH1 (P38287, YBR161W) notes

Module: `sphingolipid_de_novo_synthesis`, MIPC synthase (Csg1/Sur1 paralog). Missing from YeastCyc SPHINGOLIPID-SYN-PWY-1 (only SUR1 listed).

## Evidence journal
- Redundancy [PMID:12954640 "Deltacsg1 cells exhibited only a reduction in the synthesis of mannosylated sphingolipids compared with wild-type cells, whereas the Deltacsg1 Deltacsh1 double deletion mutant exhibited a total loss"]
- Distinct specificity [PMID:12954640 "demonstrated that Csh1p has a different substrate specificity from Csg1p"]
- Csg2 dependence [PMID:12954640 "Deletion of the CSG2 gene reduced the Csg1p activity and abolished the Csh1p activity"]
- Vacuole membrane GFP (Huh), heterodimer with Csg2 [UniProt:P38287]

## Decisions
- Core MF GO:0103064, BP GO:0051999, complex GO:0031501, Golgi apparatus (IDA). Vacuole rows KEEP_AS_NON_CORE (conflict flagged).
- M(IP)2C metabolic process rows KEEP_AS_NON_CORE (Csh1 makes the MIPC precursor; Ipt1 makes M(IP)2C).
- Generic mannosyltransferase IBA MODIFY to GO:0103064; protein binding (Csg2) REMOVE.
