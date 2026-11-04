# narX (E. coli K-12, UniProt P0AFA2) — review notes

## Deep research status

- 2026-10-23: `just deep-research ECOLI narX --provider perplexity` failed:
  "Provider 'perplexity' not available. Available: falcon, openscientist".
- 2026-10-23: `just deep-research ECOLI narX --provider falcon` failed with an
  authentication error ("Edison API request failed: Failed to authenticate",
  HTTP 403). No `narX-deep-research-*.md` file exists; this review is based on
  the UniProt record and the cached publications listed below.

## Identity and architecture

- 598 aa, NarX/NarQ subfamily (HisKA_3) sensor histidine kinase; PANTHER
  PTHR24421:SF51; PIRSF003167 (STHK_NarX/NarQ); Pfam HisKA_3 (PF07730),
  HATPase_c (PF02518), HAMP (PF00672) [file:ECOLI/narX/narX-uniprot.txt].
- Topology: TM1 15-37, periplasmic sensor 38-151, TM2 152-174, cytoplasmic
  175-598; HAMP 176-228; HK domain 393-587; phospho-His399 (by similarity)
  [file:ECOLI/narX/narX-uniprot.txt].
- Inner (plasma) membrane location experimentally supported:
  [PMID:15919996 "we established the periplasmic or cytoplasmic locations of the C termini for 601 inner membrane proteins"]
  and the UniProt subcellular location "Cell inner membrane {ECO:0000269|PubMed:15919996}".
- Sequence analysis originally identified two hydrophobic segments
  [PMID:2657652 "Presence of two copies of hydrophobic segments in the N-terminal half of the NarX protein suggests the role as a transmembrane receptor sensing nitrate."]

## Molecular function

- Autokinase + phosphotransfer to NarL in vitro with purified proteins
  [PMID:8473280 "Purified NarX was rapidly labeled when incubated with [gamma-32P] ATP but not with [alpha-32P]ATP in a reaction that required Mg2+ but was unaffected by nitrate. Incubation of the labeled NarX with purified NarL resulted in the transient phosphorylation of NarL."]
- Phosphatase toward NarL-P
  [PMID:8473280 "Dephosphorylation of the isolated NarL-phosphate required the addition of both Mg2+ and the NarX protein."]
- Ligand stimulation of autokinase in membranes
  [PMID:9426129 "The low basal autophosphorylation rate was stimulated about sixfold and threefold by nitrate and nitrite respectively."]
- Mechanism of transmitter phosphatase: DxxxQ motif; Gln required for
  phosphatase but not kinase/phosphotransfer
  [PMID:21078995 "Results show that the Gln residue is critical for transmitter phosphatase activity, but is not essential for autokinase or phosphotransfer activities."]
- Periplasmic sensor domain binds nitrate at the dimer interface; piston-type
  displacement on ligand binding
  [PMID:19217390 "Clear electron density was found for a single nitrate ion partially buried within the dimer interface"]
  [PMID:19217390 "nitrate-binding induces conformation changes that result in a piston-type displacement between the N- and C-terminal helices of the periplasmic domain"]
- Dimer: crystal dimer of the sensor domain; fragment monomeric in solution
  [PMID:19217390 "The NarX sensor is found to be dimeric in the ligated state in crystals, despite the lack of observable association of this molecular fragment in solution."]

## Biological role

- NarX and NarQ are redundant nitrate sensors feeding NarL
  [PMID:1508040 "Strains defective in either narQ or narX alone exhibited no nitrate-dependent phenotype whereas mutants defective in both narQ and narX were fully inactive for nitrate-dependent repression or activation."]
- P-box mutants discriminate nitrate vs nitrite
  [PMID:9426129 "Other changes (H45E and R59K) resulted in proteins that responded normally to nitrate but were unable to respond to nitrite."]
- narX expression itself is nitrate induced
  [PMID:2832370 "Expression of phi (narX-lacZ) operon fusions was induced by nitrate and was decreased by narL and fnr mutations."]

## GOA issues found

- GO:0006974 DNA damage response (IEP, EcoliWiki) cites PMID:1197071, a 1975
  Polish clinical paper on serum calcium after thyroid surgery. Almost
  certainly a mis-keyed PMID for PMID:11967071 (Khil & Camerini-Otero 2002,
  mitomycin C transcriptome), which EcoliWiki cites for the same term on
  glgX, glpK, pstA and pstS. Recorded as a source defect (PROBABLE). Even with
  the right paper the claim is a whole-transcriptome expression change, not
  participation; marked over-annotated, consistent with the pstS review.
- GO:0030288 periplasmic space (ISM): NarX is an integral inner-membrane
  protein whose sensor domain faces the periplasm; it is not a resident of the
  periplasmic space. Removed in favour of plasma membrane.
- No GO MF term exists for dephosphorylation of a phospho-aspartyl response
  regulator; GO:0004721 is the most specific available term. Proposed a new
  term.
