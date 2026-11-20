# PA1341 (Q9I403) notes

## Review session 2026-10-28 (PseudoCAP IBA-seed protocol)

Fetched with `just fetch-gene PSEAE PA1341` (no gene symbol; locus tag used as
folder name). Accession Q9I403 matches the worklist (rank 91). Unreviewed
TrEMBL entry (PE 3). No deep-research provider was used. Reviewed alongside
PA1340 (same operon) and for consistency with genes/PSEAE/braF (same
Biolog/growth screen paper) and the Dpp permeases PA4503/PA4504.

### Identity

- HisMQ-subfamily ABC permease; PANTHER PTHR30614:SF42 "GLUTAMATE_ASPARTATE
  IMPORT PERMEASE PROTEIN GLTJ"; TIGR01726 HEQRo_perm_3TM; four predicted TM
  helices; TCDB 3.A.1.3.22.
- Operon PA1342-PA1339 (binding protein, two permeases, ATPase), orthologous to
  P. putida KT2440 AatJQMP (PP1071-PP1068) and E. coli GltIJKL. PA1341 is the
  GltJ-type permease (P. putida AatQ by operon order); PA1340 is GltK-type.

### Literature

- Johnson et al. 2008 (PMID:18833300; full text cached), Biolog PM screen of
  transposon mutants (PA1339-PA1341 mutants are in the PAK background):
  - [PMID:18833300 "PA1339, PA1340 and PA1341 all encode components of a
    predicted ABC amino acid transporter, and are located in a putative three gene
    operon. All three mutants were defective for utilization of L-glutamic acid
    as a carbon source, and expression of two of these genes was induced by
    L-glutamic acid"]
  - Table 2 scores PA1341 only for L-glutamic acid as C source, "C+/-"
    (partial). PA1340 additionally shows L-Gln, D-Glu and N-acetyl-L-Glu
    phenotypes; the authors note the other two mutants had sub-threshold
    reductions on those, "suggesting that this transport system is probably
    specific for all four of these substrates".
- Singh and Rohm 2008 (PMID:18310026; abstract only), P. putida ortholog:
  - [PMID:18310026 "We describe an ATP-binding cassette (ABC) transporter in
    Pseudomonas putida KT2440 that mediates the uptake of glutamate and
    aspartate."]
  - [PMID:18310026 "Uptake of Glu and Asp by either mutant was greatly impaired at
    both low and high amino acid concentrations."]
  - [PMID:18310026 "The purified solute-binding protein AatJ exhibited high
    affinity towards Glu and Asp (K(d)=0.4 and 1.3 muM, respectively), while Gln
    and Asn as well as dicarboxylates (succinate and fumarate) were bound with
    much lower affinity."]

Assessment: the PA1341 phenotype is a partial growth defect (indirect), but it is
consistent across all three operon mutants, matches substrate induction, and the
orthologous P. putida system directly takes up Glu. As the permease, PA1341
does part of the transport work. L-glutamate import is sound.

### Clade checks (cached PAINT IBD/leaf GAF; QuickGO 2026-10-28)

- PTN004745596 (GO:0051938 L-glutamate import; sole seed PA1341): 7 leaves in 5
  taxa: E. coli GltJ (P0AER3), Salmonella GltJ, Yersinia GltJ, Bradyrhizobium
  bll7599, blr3097, blr0037, and PA1341. The only experimental annotation among
  the other leaves is plasma membrane (IDA) for E. coli GltJ. A GltJ clade of
  glutamate/aspartate importer permeases suits the term.
- PTN000770157 (GO:0006865 amino acid transport; 5 seeds: E. coli P0AFT2,
  P0AEQ6 and PAO1 Q9I404, Q9I487, Q9I403): 84 leaf IBAs in 28 taxa. A general
  amino acid transport term is appropriate for the HisMQ-subfamily permease
  clade. (This IBA row is not in the current GOA file for PA1341, presumably
  replaced by the more specific L-glutamate import IBA.)

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN000770157 | GO:0006865 amino acid transport | 5 | 84 (28 taxa) | GO:0051938, IMP, PMID:18833300 (PseudoCAP) | SOUND | General term for a HisMQ-subfamily polar amino acid permease clade; other seeds include experimentally characterised E. coli permeases. |
| PTN004745596 | GO:0051938 L-glutamate import | 1 (sole) | 7 (5 taxa) | GO:0051938, IMP, PMID:18833300 (PseudoCAP) | SOUND | Partial growth defect on L-Glu as C source in a Biolog/plate screen, on its own an indirect phenotype, but consistent across the operon, matched by L-Glu induction, and corroborated by direct Glu/Asp uptake by the orthologous P. putida AatJMQP. The node is a GltJ clade (E. coli/Salmonella/Yersinia GltJ = glutamate/aspartate importers). |

Defects filed: none.

## Decisions summary

- ACCEPT: plasma membrane (IBA, IEA).
- MODIFY: L-glutamate import (IBA, IMP), amino acid transmembrane transport
  (IEA), transmembrane transport (IEA) -> L-glutamate import across plasma
  membrane; amino acid transmembrane transporter activity (IBA) and
  transmembrane transporter activity (IEA) -> ATPase-coupled L-glutamate
  transmembrane transporter activity; membrane -> plasma membrane; ABC
  transporter complex -> substrate-binding subunit-containing ABC transporter
  complex.
