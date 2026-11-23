# crb review notes

## Session 1 (2026-10-28)

- Fetched with `just fetch-gene DROME crb`; UniProt P10040 (CRB_DROME, FlyBase FBgn0259685, GeneID 42896). 112 GOA rows.
- No deep-research provider available; manual synthesis written to `crb-deep-research-manual.md`.
- Key paper PMID:22105348 (Pocha et al. 2011) read in full: Crb complex co-IPs MyoV, Crb stabilizes MyoV
  against proteasomal degradation and is needed for Rh1 transport to the rhabdomere; Crb itself sits on the
  stalk membrane [PMID:22105348 "Crb still localizes to the stalk membrane in MyoV mutant tissue"]. In S2R+ cells
  Crb recruits MyoV-GFP to the plasma membrane without Sdt [PMID:22105348 "upon coexpression with Crb, MyoV-GFP is recruited to the plasma membrane, where it colocalizes with Crb"].

### Curation decisions worth flagging

- `GO:0032391 photoreceptor connecting cilium` (IDA, PMID:32579558, UniProt): Drosophila rhabdomeric photoreceptors
  have no connecting cilium; the paper shows Crb on the stalk membrane. Modified to apical plasma membrane and a
  source defect (WRONG_TERM, UniProt) recorded.
- `GO:0005112 Notch binding` IBA: the PAINT node's donors are Notch ligands (Dl, Ser, Jag, Dll); no Drosophila Crb
  Notch-binding evidence in cached literature. Marked over-annotated.
- `GO:0035002` IGI PMID:21945316 lists crb itself (FBgn0259685) as the WITH partner; probably should be wurst.
  Recorded as a WRONG_WITH_FROM source defect (SUSPECTED, abstract only).
- Overexpression-only rows from PMID:28263180 (apical constriction, apicomedial actomyosin) marked over-annotated.
- No GO term exists for the photoreceptor stalk membrane; rhabdomere rows kept as non-core.
- Core MF chosen as protein-macromolecule adaptor activity (GO:0030674): the short tail links Sdt/Patj, aPKC,
  Moesin/beta-H spectrin and Expanded to the apical membrane. No NEW rows proposed.
