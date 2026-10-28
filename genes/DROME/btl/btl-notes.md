# btl review notes

## Session 1 (create review)

- `just fetch-gene DROME btl` resolved Q09147 (FGFR2_DROME; FlyBase FBgn0285896; GeneID 39564), 91 GOA rows.
  The first two attempts timed out against rest.uniprot.org; the third succeeded.
- No deep-research provider available; literature synthesis written by hand in
  `btl-deep-research-manual.md` from the cached publications.
- Key reading: PMID:23029159 (Zpr1, full text). Btl's role in terminal-cell lumen formation is
  inferred only from gain-of-function (λbtl) epistasis with Zpr1; loss-of-function could not be
  tested ["We could not directly test loss of FGFR in lumen development because tracheal cells mutant
  for btl fail to outgrow or undergo branching"]. Kept as non-core.

## Decisions worth flagging

- GO:0035202 tracheal pit formation (IMP, PMID:16818611): abstract-only, paper is about cv-c/EGFR in
  invagination; older work states pit formation is not affected in deletions removing btl
  [PMID:1849109 "the initial formation of the tracheal pits is not affected"]. Marked UNDECIDED,
  not removed, since the curator saw the full text.
- GO:0060438 trachea development (IMP, PMID:19285057): this is the vertebrate airway term
  ("portion of the airway that attaches to the bronchi"); the insect structure is GO:0007424 open
  tracheal system development. MODIFY.
- GO:0045887 positive regulation of synaptic assembly at NMJ (IGI, PMID:21300852): btl/+ alone has no
  NMJ phenotype ["how24BGAL4; btldev1/+ animals do not show any significant effects on the NMJ"]; only
  enhances Smn knockdown. Marked over-annotated.
- Kinase MF rows (protein kinase, PTK, TM RTK) modified to GO:0005007 FGFR activity, which is supported
  by ligand (Bnl) identification, Dof phosphorylation and ligand-receptor colocalization.
- Generic ARBA process rows (ameboidal migration, cell fate specification, tissue morphogenesis etc.)
  set TOO_GENERAL, each entailed by a specific experimental term in this review.
- Protein binding (IPI with Dof) removed per policy; interaction is real (co-IP in S2 cells).

## Comparator / NEW-term check

- No NEW annotations proposed. FGF binding (GO:0017134) is plausible but the evidence is
  colocalization, not a direct binding assay.
