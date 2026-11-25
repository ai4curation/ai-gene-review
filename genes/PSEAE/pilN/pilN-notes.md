# pilN (PA5043, G3XD30) notes

## Identity

- UniProt G3XD30 (PILN_PSEAE), reviewed, 198 aa, gene pilN, locus PA5043.
  Single TM segment 19-39 (ECO:0000255), short cytoplasmic N-terminal tail,
  periplasmic coiled-coil + ferredoxin-like domain. Pfam PF05137 PilN,
  PANTHER PTHR40278:SF2 (type IV pilus inner membrane component PilN).
- Second gene of the pilMNOPQ operon [PMID:7565110 "This region contains four
  genes: pilM-P"].

## Literature

- Mutants lack functional fimbriae: transposon screen for loss of twitching;
  complementation; phage sensitivity; EM [PMID:7565110 "PilM-P were found to be
  required for fimbrial biogenesis by complementation studies using twitching
  motility and sensitivity to fimbrial-specific phage as indicators of the
  presence of functional fimbriae."; "This was confirmed by electron
  microscopy."]. PilN predicted inner-membrane [PMID:7565110 "PilN and PilO have
  long internal hydrophobic domains which may serve to localize them to the
  cytoplasmic membrane"] and resembles the T2SS GspL protein XpsL.
- Inner membrane location, PilMNOP complex [PMID:19857645 "all four proteins,
  including the nominally cytoplasmic PilM, colocalized to the inner
  membrane"]; interdependent stability [PMID:19857645 "loss of one component
  has a negative impact on the levels of other members of the putative
  complex"]. UniProt: "Cell inner membrane {ECO:0000269|PubMed:19857645}";
  "Deletion mutants lack surface pili."
- Periplasmic PilN/PilO heterodimer [PMID:19857646 "the periplasmic domains of
  PilN and PilO interact to form a heterodimer"].
- PilN cytoplasmic tail binds PilM; PilNOP links to PilQ via PilP
  [PMID:23457250 "the N-terminal cytoplasmic tail of PilN binds to the
  actin-like protein PilM"]; conserved N-terminal residues needed for
  twitching, phage sensitivity and surface PilA [PMID:23457250 "Constructs
  expressing the PilN_N5A variant or deletion constructs lacking residues 2 to
  9 or 4 to 18 did not restore twitching motility, phage sensitivity, or
  surface PilA in a pilN mutant"].
- PilN binding monomerises PilM and alters its ATP site [PMID:27022027 "upon
  PilN binding, there is a large domain closure in PilM that alters its ATP
  binding site"].
- PilN/PilO homo- and heterodimers in vivo; some locked configurations abolish
  twitching [PMID:27474743 "certain covalent homo- or heterodimers eliminated
  twitching motility, suggesting that specific PilNO configurations are
  essential for T4P function"].

## GO term check

- GO:0044096 type IV pilus is the surface fibre ("A short filamentous structure
  on the surface of a bacterial cell distinguished from other pili by
  post-translational N-methylation of the pilin monomers"). PilN is a bitopic
  inner-membrane protein of the alignment subcomplex, not a fibre subunit.
  Same situation as pilM (genes/PSEAE/pilM): the PseudoCAP
  located_in type IV pilus IMP rows for pilM, pilN, pilO, pilP all come from
  the PMID:7565110 mutant screen.

## PANTHER node PTN002220336

- PAINT IBD.gaf (cached .cache/paint): IBDs at PTN002220336 for GO:0043107
  and GO:0043683 (2017-02-28), and GO:0044096 type IV pilus and GO:0005886
  plasma membrane (2026-06-17), all WITH UniProtKB:G3XD30 only.
- Leaves (paint_uniprot GAF): G3XD30 (P. aeruginosa), Q4W563 (Neisseria
  meningitidis NMB1809 PilN), Q74BL0 (Geobacter GSU2031 PilN), Q74C93
  (Geobacter GSU1781, named "PulN" but PilN family, PTHR40278:SF2), Q8EK24
  (Shewanella), Q8P5V4 (Xanthomonas), Q9KNU7 (Vibrio VC_2633). 7 leaves, 6
  taxa, all PilN subfamily members per UniProt PANTHER xref. Node scope is
  appropriate.
- The GO:0044096 and GO:0005886 IBAs are not yet in the GOA file for pilN
  (fetched 2026-10-28; QuickGO shows only GO:0043107 and GO:0043683 IBAs from
  this node), so there is no IBA type IV pilus row to review. The GO_CENTRAL
  defect for the type IV pilus IBD is recorded on the PseudoCAP seed row.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN002220336 | GO:0044096 type IV pilus | 1 (sole) | 7 (6 taxa) | GO:0044096 type IV pilus, located_in, IMP, PMID:7565110 (PseudoCAP) | INDIRECT-PHENOTYPE | "Mutant has no pili" recorded as a location. PilN is a bitopic inner-membrane alignment-subcomplex protein, not part of the surface fibre GO:0044096 defines. The IBD (added 2026-06-17) has no other support. |
| PTN002220336 | GO:0043107 type IV pilus-dependent motility | 1 (sole) | 7 (6 taxa) | GO:0043107, IMP, PMID:7565110 and PMID:19857645 (PseudoCAP) | SOUND | PilN is a structural component of the pilus machine; mutants and N-terminal point mutants abolish twitching. Node confined to PilN orthologues. |
| PTN002220336 | GO:0043683 type IV pilus assembly | 1 (sole) | 7 (6 taxa) | GO:0043683, IMP, PMID:7565110 and PMID:19857645 (PseudoCAP) | SOUND | Deletion mutants lack surface pili; PilN anchors the PilMNOP alignment subcomplex that is required for assembly. Conserved across the PilN clade. |

## Decisions summary

- ACCEPT: plasma membrane (EXP, IEA); motility (IBA, IMP x2); assembly (IBA,
  IMP x2).
- REMOVE: located_in type IV pilus (IMP, PseudoCAP), with PSEUDOCAP and
  GO_CENTRAL defects.
