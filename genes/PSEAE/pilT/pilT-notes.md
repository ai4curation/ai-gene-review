# pilT (PA0395, P24559) notes

## Identity

- UniProt P24559 (PILT_PSEAE), reviewed, 344 aa; type IV pilus retraction
  ATPase. GspE/secretion NTPase superfamily (Pfam PF00437 T2SSE; InterPro
  IPR006321 PilT/PilU); PANTHER PTHR30486:SF6. Structures 3JVU/3JVV.

## Literature

- Purified PilT is an ATPase; Walker A/B mutants abolish twitching; Asp Box
  and His Box residues needed for ATPase activity [PMID:18174131 "Assay of
  purified 6xHis-tagged PilB, PilT and PilU from P. aeruginosa showed that all
  three proteins have ATPase activities in vitro."; "mutation of these
  residues caused loss of PilT ATPase activity in vitro"]. PilT powers
  retraction [PMID:18174131 "PilB and PilT are bipolar proteins belonging to
  the secretion NTPase superfamily, and power pilus extension and retraction,
  respectively"]. This is the PilB/PilT/PilU ATPase paper also used in
  genes/PSEAE/pilB and genes/PSEAE/pilU.
- Hexameric retraction motor, crystal structures with and without AMP-PCP
  [PMID:20595000 "Retraction is accomplished by the motor protein PilT.";
  "revealing an interlocking hexamer"]. Glu204 (Walker B) assigned to
  catalysis [PMID:20595000 "The roles of two invariant carboxylates, Asp Box
  motif Glu163 and Walker B motif Glu204, have been assigned to Mg(2+) binding
  and catalysis, respectively."].
- Cytoplasmic, bipolar localisation of functional YFP fusions
  [PMID:15659660 "PilB and PilT fusions localized to both poles, while PilU
  fusions localized only to the piliated pole."].
- UniProt disruption phenotype: "Mutants retain surface pili but have lost
  twitching motility".

## GO term check

- GO:0044096 type IV pilus is the extracellular fibre. PilT is a soluble
  cytoplasmic hexamer that docks on the base of the machine; it is not part of
  the fibre. The PseudoCAP TAS located_in type IV pilus from the structure
  paper conflates the machine with the fibre (same pattern as the
  pilM/N/O/P IMP rows). Not an IBD seed.
- GO:0043108 pilus retraction: no type IV-specific child exists, so this is
  as precise as GO allows.

## PANTHER node PTN002020799

- IBDs: GO:0016887 ATP hydrolysis activity (seed UniProtKB:P24559, PseudoCAP
  IDA PMID:18174131) and GO:0005829 cytosol (seed E. coli YggR, P52052),
  both 2024-08-27.
- Leaves (8, 8 taxa): P. aeruginosa PilT, Xanthomonas PilT (Q7CLR1),
  Shewanella PilT (Q8EBZ4), Vibrio VC_0462 (Q9KUQ3), E. coli YggR (P52052),
  Salmonella YggR (Q8ZM48), Yersinia YPO0940, Coxiella DotB (Q83B70). All
  PilT-like secretion NTPases with Walker A/B, Asp Box and His Box motifs;
  ATP hydrolysis is a safe, appropriately general term across this clade
  (DotB of the Dot/Icm T4SS is also an ATPase).

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN002020799 | GO:0016887 ATP hydrolysis activity | 1 (sole) | 8 (8 taxa) | GO:0016887 ATP hydrolysis activity, IDA, PMID:18174131 (PseudoCAP) | SOUND | In vitro ATPase assay of purified P. aeruginosa PilT, stated in the abstract, with catalytic-residue mutants that abolish activity. The secretion-NTPase catalytic motifs are conserved across the node (PilT, YggR, DotB), so ATP hydrolysis is a suitably broad node term. |

## Decisions summary

- ACCEPT: ATP binding (IEA); cytoplasm (EXP, IEA); cytosol (IBA); ATP
  hydrolysis (IBA, IDA); motility (TAS); pilus retraction (TAS).
- REMOVE: located_in type IV pilus (TAS, PseudoCAP), with PSEUDOCAP defect.
