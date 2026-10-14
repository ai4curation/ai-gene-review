# MTLN (mitoregulin; MOXI / MPM / LEMP / SMIM37) review notes

UniProt Q8NCU8 (MTLN_HUMAN), 56 aa, encoded by LINC00116 (mouse 1500011K16Rik).
Single predicted TM helix (res 10-27); UniProt topology (by similarity to mouse Q8BT35):
N-terminus matrix, C-terminal basic tail in the intermembrane space. Initiator Met removed
(top-down MS of human mitochondrial membrane proteins, PMID:23305238 per UniProt).
Family: InterPro IPR038778, PANTHER PTHR37154, Pfam PF22002 -- vertebrate-restricted.

## Session 2026-09-30 (claude-code)

### Discovery (2018-2020): four groups, four names

- Stein et al. 2018 (Boudreau lab; "mitoregulin"): [PMID:29949756 "Mtln localizes to the inner
  mitochondrial membrane, where it binds cardiolipin and influences protein complex assembly."]
  - Cardiolipin: [PMID:29949756 "cardiolipin-coated beads pulled down Mtln from wild-type mouse
    cardiac tissue lysates to a similar or greater degree compared to subunit c, an ATP synthase
    subunit with high affinity for cardiolipin (Figure 2F)"] and [PMID:29949756 "A lipid-strip
    binding assay further supported that Mtln preferentially engages cardiolipin relative to other
    common cell membrane lipids (Figure 2G)."] -- assay on mouse heart lysate (mouse Mtln).
  - Supercomplexes (mouse KO): [PMID:29949756 "decreases in respiratory supercomplexes were evident
    in Mtln-KO hearts (Figure 5C) and skeletal muscles (Figure S7B)"]; [PMID:29949756 "Mtln-KO
    skeletal muscle samples also showed reduced CI activities within both I+III2 supercomplexes and
    respirasomes (I+III2+IV) (Figure S7C)."]
  - BN-PAGE: [PMID:29949756 "Mtln co-migrates with several notable complexes, including the CI
    assembly module ... complex V, and various supercomplexes"]
  - Human cell data: HeLa Dox-On overexpression increases membrane potential, respiration, Ca2+
    retention; overexpression did not change SC levels ([PMID:29949756 "Although Mtln
    overexpression did not cause overt changes in levels of OXPHOS machinery or respiratory
    supercomplexes"]). So the supercomplex evidence is loss-of-function in mouse; the human IDA
    for respirasome assembly probably reflects the curator's reading of the whole paper.
  - Authors frame FAO defect as downstream: [PMID:29949756 "Despite our observation that Mtln loss
    leads to deficiency in FAO, we believe that this occurs downstream of defects in respiratory
    chain activity"]
- Makarewich et al. 2018 (Olson lab; "MOXI"), mouse: [PMID:29949755 "MOXI localizes to the inner
  mitochondrial membrane where it associates with the mitochondrial trifunctional protein"]; MTP
  levels unaffected: [PMID:29949755 "indicating that MOXI is not required for MTP complex formation
  or stability"]. KO mitochondria oxidise fatty acids less, TG overexpression more.
- Chugunova et al. 2019 (Sergiev/Dontsova), mouse cell lines: complex I activity reduced in KO but
  [PMID:30796188 "Unlike the integral components and assembly factors of NADH:ubiquinone
  oxidoreductase, Mtln does not alter its enzymatic activity directly."] Partner is CYB5R3:
  [PMID:30796188 "Interaction of Mtln with NADH-dependent cytochrome b5 reductase stimulates complex
  I functioning most likely by providing a favorable lipid composition of the membrane."]
- Lin et al. 2019 ("MPM"), mouse C2C12/KO: myogenic differentiation phenotype, attributed to
  respiration: [PMID:31296841 "MPM may promote myogenic differentiation by enhancing mitochondrial
  respiratory activity."] -- source of the mouse IMP for striated muscle cell differentiation and
  cellular respiration that were ISS-transferred to human.
- Wang et al. 2020 ("LEMP"), mouse + zebrafish myogenesis: [PMID:32393776 "LEMP is localized at both
  the plasma membrane and mitochondria, and associated with multiple mitochondrial proteins"].
- Friesen et al. 2020 (human hPSC-adipocytes + mouse KO): [PMID:32243843 "MTLN directly interacts
  with the β subunit of the mitochondrial trifunctional protein"]; co-IP of HADHB and ATP5B
  [PMID:32243843 "We verified the co-immunoprecipitation of exogenously expressed mitochondrial
  trifunctional enzyme, subunit beta (HADHB) and the endogenous ATP synthase beta subunit (ATP5B)"].
  Source of all human IPI/IMP/IDA rows other than respirasome assembly.
  Mechanism is regulatory: [PMID:32243843 "Our data suggest MTLN augments the rate of β-oxidation of
  long-chain fatty acids, possibly through direct interaction with HADHB."]

### Later work (2023-2026)

- Localisation dispute. Zhang et al. 2023 (human cells; split-GFP topology, protease protection):
  [PMID:37664623 "Here, by applying multiple orthogonal methods, we concluded that MTLN is primarily
  localized to the mitochondrial outer membrane and has a cytosolic tail."] Interactors CPT1B,
  CYB5B, CYB5R3, ACSL1, VDAC3; KO accumulates VLCFA/DHA. The Boudreau lab continues to model
  Mtln in the IMM/cristae (PMID:41555203, PMID:39811642). Not resolved; IMM annotations kept, OMM
  raised as a question rather than a NEW annotation.
- Self-association: [PMID:39811642 "Our combined results provide strong support that Mtln
  self-associates and likely forms a hexameric pore-like structure."] (~66 kDa complex, synthetic
  protein; human and mouse).
- Membrane role: [PMID:41555203 "Our work supports a model in which Mtln binds cardiolipin and
  stabilizes mitochondrial membranes to broadly influence diverse mitochondrial functions, including
  lipid metabolism, while also protecting against stress."] Synthetic human Mtln alters
  IMM-like lipid monolayers; KO cristae defects, CL damage/MLCL increase.
- Averina 2023 (mouse KO): obesity on HFD, elevated serum TG (PMID:36174793, abstract only);
  muscle CL decrease/MLCL increase, MtCK octamer dissociation (PMID:37108753).
- Li 2023 Kidney Int (PMID:36804379): MOXI nuclear translocation in fibrotic kidney -- abstract
  only, single report, not used for GO.

### Synthesis

The most direct molecular observation is lipid (cardiolipin) binding and membrane modulation, plus
physical association with several IMM/OMM enzyme complexes (MTP, ATP synthase, CYB5R3, CPT1B).
There is no catalytic activity. Respiratory supercomplex (respirasome) assembly/stability and
enhanced FAO are the best-supported processes; both plausibly follow from a membrane-organising,
CL-binding role. Downstream phenotypes (TG accumulation, obesity on HFD, myogenic
differentiation defects, exercise capacity) are consequences of reduced oxidative capacity.

Decisions:
- protein binding IPIs (HADHB, ATP5F1B): REMOVE (uninformative; interactions real but no specific MF
  can be inferred -- MTLN not required for MTP formation/stability).
- fatty acid beta-oxidation IMP: MODIFY -> positive regulation of fatty acid beta-oxidation
  (MTLN does not catalyse a step; enhances rate).
- triglyceride homeostasis IMP, striated muscle cell differentiation, lipid metabolic process,
  cellular respiration: KEEP_AS_NON_CORE (indirect/broad).
- respirasome assembly, IMM, mitochondrion, positive regulation of FAO: ACCEPT.
- NEW: cardiolipin binding (GO:1901612), ISS from mouse data in PMID:29949756, supported for the
  human peptide by PMID:41555203 (synthetic human Mtln in lipid monolayers).
- Considered but not proposed: GO:0010918 positive regulation of mitochondrial membrane potential
  (appears as IBA in UniProt DR lines but not in this GOA download; phenotype-level readout of
  overexpression); GO:0005741 mitochondrial outer membrane (contested); identical protein binding
  (self-association) -- uninformative.
