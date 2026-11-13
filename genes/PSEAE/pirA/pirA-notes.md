# pirA (PA0931, Q9I527) notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9I527 --alias pirA` (accession fetch). Accession Q9I527
(Swiss-Prot) matches the worklist. No deep-research keys; literature from cached seed/other
papers (PMID:15899402, PMID:28137795, PMID:33350053, all abstract-only) and the UniProt
record.

## Identity

- TonB-dependent outer-membrane receptor, 742 aa + signal peptide 1-28. Plug 57-184,
  beta-barrel 189-742, TonB box motif 725-742. InterPro PirA/FepA/PfeA family (IPR058134);
  PTHR30069:SF8. Crystal structure 5FP2. No N-terminal signalling extension, so a
  receptor-transporter.

## Literature

- Second ferric-enterobactin receptor, redundant with PfeA
  [PMID:15899402 "a double knock-out mutant of ferrienterobactin receptor encoding gene pfeA (PA 2688) and pirA (PA0931) failed to be stimulated by 4 of the tested synthetic catecholate siderophores whose chemical structures resemble enterobactin"];
  [PMID:15899402 "Ferric-enterobactin also failed to stimulate growth of the double pfeA-pirA mutant although, like its synthetic analogues, it stimulated growth of the corresponding single mutants."];
  [PMID:15899402 "Hence, we confirmed that pirA represents a second P. aeruginosa ferric-enterobactin receptor."].
- Imports catecholamine-chelated iron (l-DOPA, norepinephrine preference)
  [PMID:33350053 "Bacterial growth assays under strong iron-restricted conditions and with numerous mutants showed that the TBDTs involved are PiuA and PirA."];
  [PMID:33350053 "whereas PirA specificity appeared to be higher for l-DOPA and norepinephrine"].
- Entry route for siderophore-monobactam conjugates; structure solved
  [PMID:28137795 "The crystal structures of PiuA and PirA from A. baumannii and their orthologues from P. aeruginosa were determined."].

## Annotation decisions

- Cell outer membrane (IBA, IEA): ACCEPT. Siderophore uptake transmembrane transporter
  activity (IBA, IEA, IMP): ACCEPT core. Enterobactin transport (IMP) and enterobactin
  transmembrane transporter activity (IEA, IMP): ACCEPT core. Siderophore-iron import into
  cell (IEA): ACCEPT.
- Siderophore-iron transmembrane transporter activity (IEA, GO:0015343): TOO_GENERAL
  (GO:0015344 is_a descendant). Siderophore transport (IEA x1 + IMP x3, GO:0015891):
  TOO_GENERAL (GO:0044718 is_a descendant). Iron ion transport (IMP, GO:0006826):
  TOO_GENERAL (GO:0033214 is_a descendant).
- Signaling receptor activity (IEA, GO:0038023): REMOVE (InterPro2GO over-mapping; no
  signalling extension, as for PfeA and ChtA).
- Action counts: ACCEPT 10, TOO_GENERAL 6, REMOVE 1. Defects: none (PseudoCAP seed sound;
  signaling row is an InterPro2GO electronic over-mapping removed, not a source defect).
- Note: the GO:0015344 IMP seed rests on pfeA pirA double-mutant data with single-mutant
  controls (PfeA/PirA are redundant for enterobactin); this is a genetic-interaction
  phenotype but, with the controls, still identifies PirA as a ferric-enterobactin receptor.
  GO:0042931 could be refined to GO:0015620 ferric-enterobactin transmembrane transporter
  activity to name the iron-loaded ligand, as noted for PfeA; left as-is (acceptable parent).

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN004738955 | GO:0015344 siderophore uptake transmembrane transporter activity | 4 | 142 (21 taxa) | GO:0015344, IMP, PMID:15899402 | SOUND | pfeA pirA double mutant, not either single mutant, fails to use ferric enterobactin and catecholate analogues; PirA confirmed as a second ferric-enterobactin receptor. Later: catecholamine-iron uptake, crystal structure. | PfeA (Q05098), ChtA (PA4675, Q9HVC0), FvbA (PA4156, Q9HWM5) — PseudoCAP IMP; E. coli CirA (P17315) at the partner process IBD | Yes |

The node-level assessment of PTN004738955 is recorded once in `PA4675-notes.md` (IBD sound,
node term suits the clade, no GO_CENTRAL defect). pirA is consistent with it.
