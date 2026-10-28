# xcpR (PA3103, Q00512) review notes

## Review session 2026-10-28 (PseudoCAP IBA-seed protocol)

Fetched with `just fetch-gene PSEAE xcpR`; accession Q00512 matches the worklist entry (rank 72,
PA3103, reviewed Swiss-Prot entry GSPE_PSEAE). No deep-research provider key was available, so
these notes are manual, from the cached publications, the UniProt record and the cached PAINT
table `interpro/panther/PTHR30258/PTHR30258-paint.tsv`.

### What XcpR is

- XcpR is the GspE-family secretion ATPase of the Xcp type II secretion system (T2SS), the
  cytoplasmic motor of the machine. UniProt: "Belongs to the GSP E family"; NCBIfam TIGR02533
  (type_II_gspE), Pfam PF00437 T2SSE, PANTHER PTHR30258.
- It was identified with the other xcp genes and recognised as a PilB homologue with a canonical
  nucleotide-binding site [PMID:1588814 "two other proteins, XcpR and XcpS, show similarity to
  the PilB and PilC proteins required for fimbriae assembly"]. UniProt records a Walker A motif
  (`FT:BINDING 263..270`) and four further ATP/metal-binding residues.
- Serine substitution of the conserved Walker A glycine abolishes exoprotein secretion, and
  overexpression of the mutant protein is dominant-negative, causing periplasmic accumulation of
  normally secreted enzymes [PMID:8102361 "Bacteria expressing mutant XcpR or PilB were unable to
  secrete exotoxin A or assemble pili, respectively."]. UniProt `CC:DISRUPTION PHENOTYPE`:
  "Mutants show complete loss of extracellular exotoxin A secretion."
- XcpR dimerises through an 85-residue N-terminal region and that dimerisation is required for
  secretion [PMID:9426126 "the data presented in this paper suggest that the XcpR protein
  dimerizes via its N-terminus"].
- It has no hydrophobic anchor of its own and reaches the cytoplasmic (inner) membrane only via
  XcpY/GspL [PMID:9882649 "In a wild-type P. aeruginosa strain, XcpR was found associated with the
  cytoplasmic membrane. This association depends on the presence of the XcpY protein"].
- Co-purification with His-tagged XcpZ isolated an XcpRSYZ inner-membrane platform subcomplex
  [PMID:16168578 "This subcomplex was also found to interact with XcpR and XcpS to form a XcpRSYZ
  complex which was isolated under native conditions."].
- UniProt assigns EC 7.4.2.8 with `ECO:0000305|PubMed:8102361`, i.e. the catalytic activity is a
  curator inference from the Walker-site genetics, not a measured ATPase rate for XcpR itself. A
  Zn(2+) cofactor is asserted only by similarity (`ECO:0000250|UniProtKB:P37093`).

### PseudoCAP row details

- `GO:0015627` IDA PMID:16168578 (Robert, Filloux & Michel 2005): the abstract itself reports the
  native XcpRSYZ subcomplex, so the complex-membership claim is directly supported even though
  only the abstract is cached. Sole seed of the PTN002016240 IBD for this term.
- `GO:0015628` IDA PMID:9818381: Filloux, Michel & Bally 1998 is a **review** (`publication_type:
  REVIEW` in the cached file; PubMed publication type Review). The same reference is mis-keyed as
  IDA on the xcpQ and xcpX rows for the same term, so this is a systematic PseudoCAP pattern over
  the xcp cluster rather than a single slip. The term is correct for XcpR - Walker-site mutants
  lose exoprotein secretion entirely - and the right primary reference is PMID:8102361 (IMP).
  Recorded as a `WRONG_EVIDENCE_CODE` source defect on both the xcpR and xcpQ reviews.

### PAINT node context

`interpro/panther/PTHR30258/PTHR30258-paint.tsv`:

- PTN001250205 (no taxon restriction): GO:0005886 IBD seeded by P0AFA5 and Q00512; GO:0016887 ATP
  hydrolysis IBD seeded by P22608. This is the broad GspE/PilB-type ATPase node, and both terms
  (inner-membrane localisation, ATP hydrolysis) are generic enough to suit it.
- PTN002016240 (taxon:1236, Gammaproteobacteria): GO:0015627 and GO:0015628 IBDs, both sole-seeded
  by Q00512. The T2SS-specific terms are confined to a Gammaproteobacterial subnode rather than
  being pushed to the family root, which is the right shape - the family also contains type IV
  pilus assembly ATPases (PilB) and other T4P-superfamily motors, for which T2SS terms would be
  wrong.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN002016240 | GO:0015628 protein secretion by the type II secretion system | 1 (sole seed) | 7 (6 taxa) | GO:0015628, IDA, PMID:9818381 | SOUND (term); evidence code WRONG | XcpR is the T2SS secretion ATPase: Walker A mutants lose exoprotein secretion and are dominant-negative (PMID:8102361), and dimerisation-defective variants cannot secrete (PMID:9426126). But PMID:9818381 is a review, so IDA cannot stand; the row should be re-keyed to PMID:8102361 as IMP (or downgraded to TAS). The IBD conclusion is unaffected, and the Gammaproteobacterial restriction of the node keeps the term off the PilB-type members. |
| PTN002016240 | GO:0015627 type II protein secretion system complex | 1 (sole seed) | 7 (6 taxa) | GO:0015627, IDA, PMID:16168578 | SOUND | The seed paper isolated the native XcpRSYZ inner-membrane platform subcomplex, which is direct evidence of membership; XcpR's membrane recruitment by XcpY (PMID:9882649) is consistent. The node term fits a Gammaproteobacterial GspE clade. |

## Open questions

- No ATPase rate has been measured for XcpR itself; EC 7.4.2.8 and the GO:0008564
  protein-exporting ATPase activity row both descend from the Walker-site genetics
  (`ECO:0000305|PubMed:8102361`). A direct hydrolysis assay on purified XcpR, ideally in the
  XcpRSYZ context, would settle it.
- The Zn(2+) cofactor is asserted only by similarity to P37093, so no metal-binding GO row is
  proposed here.
- GO:0008564 is a transmembrane transporter activity. XcpR is the cytoplasmic motor, not the
  conduit, so `contributes_to` would describe the row better than `enables`.
