# GRB2 curation notes

UniProt: P62993 (GRB2_HUMAN), 217 aa, HGNC:4566. Family: GRB2/Sem-5/DRK.
Architecture: N-terminal SH3 – central SH2 – C-terminal SH3 (SH3-SH2-SH3).

## Core biology (synthesis)

GRB2 is a small, non-catalytic cytoplasmic signaling adaptor. It contains no
enzymatic activity; its function is entirely interaction-based. The central SH2
domain recognizes phosphotyrosine motifs (preference ~pY-x-N-x) on activated
receptor tyrosine kinases and phosphorylated scaffolds; the two SH3 domains bind
proline-rich motifs (PxxP / RxxK) on downstream effectors, chiefly the Ras GEF
SOS1/SOS2.

Canonical pathway: ligand activates an RTK -> RTK autophosphorylates -> GRB2 SH2
docks on receptor pTyr (directly, or indirectly via phosphorylated SHC1) -> GRB2
SH3 domains recruit SOS -> SOS placed at the plasma membrane loads GTP onto Ras
-> RAF-MEK-ERK (MAPK) cascade.

Key primary evidence:
- GRB2 links RTKs to Ras signaling; SH2 binds tyrosine-phosphorylated EGFR/PDGFR
  [PMID:1322798 "GRB2 associates with tyrosine-phosphorylated epidermal growth factor receptors (EGFRs) and platelet-derived growth factor receptors (PDGFRs) via its SH2 domain"].
- GRB2 couples RTKs to a Ras guanine-nucleotide-exchange factor
  [PMID:8386805 "Cellular Grb2 appears to form a complex with a guanine-nucleotide-exchange factor for Ras, which binds to the ligand-activated EGF receptor, allowing the tyrosine kinase to modulate Ras activity."].
- Sos1 is a Ras GEF that binds GRB2 (UniProt RN[13], PMID:8493579).
- GRB2 (Ash/Grb-2) required for EGF/PDGF mitogenesis and actin/ruffle
  reorganization [PMID:8253073 "The antibody abolished both S phase entry and the reorganization of actin assembly to ruffle formation upon stimulation with epidermal growth factor (EGF) and platelet-derived growth factor (PDGF)."; "Ash plays a critical role in the signaling of both pathways downstream from growth factor receptors to Ras and Rac"].

Adaptor/scaffold role beyond SOS-Ras:
- GRB2 nucleates LAT microclusters in TCR signaling; its SH3-ligand binding is
  required for cluster formation, controlling PLCg1 activation and cytokine output
  [PMID:25870599 "GRB2 regulates signaling downstream of adaptors and receptors by both recruiting effector proteins and regulating the formation of signaling complexes."; "GRB2, and its ability to bind to SH3 domain ligands, is required for establishing LAT microclusters"].
- Binds proline-rich motifs of partners via its SH3 domains, e.g. GAREM
  [PMID:19509291 "the proline-rich motifs of GAREM are recognized by the N- and C-terminal SH3 domains of Grb2"].
- Binds tyrosine-phosphorylated IRS1 (insulin/Ras coupling)
  [PMID:8388384 "fusion protein of ASH was able to bind the fusion protein of tyrosine-phosphorylated IRS-1 fragments, suggesting that ASH is able to bind tyrosine-phosphorylated IRS-1 directly"].
- Binds activated EphB1 (ephrin receptor)
  [PMID:12925710 "activated EphB1 recruits the adaptor proteins Grb2 and p52Shc"].
- Homodimerizes (identical protein binding); dimeric GRB2 restrains basal FGFR2
  signaling [PMID:22536782 "Grb2 exists in a monomer-dimer equilibrium"; PMID:22726438 "Dimeric Grb2 binds to the C termini of two FGFR2 molecules."].

Receptor endocytosis / signal termination:
- GRB2 is specifically required for clathrin-mediated EGFR endocytosis
  [PMID:14985334 "CALM is the second protein besides Grb2 that appears to play a specific role in EGFR endocytosis"]; it recruits CBL to activated EGFR (deep-research falcon, jiang2003 = internalization via CCPs).

Localization: predominantly cytosolic under basal conditions, translocating to
the cytoplasmic face of the plasma membrane on RTK activation; also detected at
endosomes during receptor trafficking, and nuclear GRB2 has been reported (miRNA
regulation, DNA-damage foci) [PMID:37328606 title "Regulation of microRNA expression by the adaptor protein GRB2."; PMID:21179510 nuclear/cytoplasmic HD-PTP colocalization].

Immune / other pleiotropic roles (non-core, downstream):
- NKG2D-DAP10 NK cytotoxicity requires a DAP10-bound Grb2-Vav1 intermediate
  [PMID:16582911 "binding of an intermediate consisting of the DAP10 binding partner Grb2 and the effector molecule Vav1 (Grb2-Vav1) to DAP10 was sufficient to initiate tyrosine-phosphorylation events"].
- Node in a p21/ROS senescence signaling loop
  [PMID:20160708 "GADD45-MAPK14(p38MAPK)-GRB2-TGFBR2-TGFbeta"] -- treated as
  peripheral/indirect (GRB2 does not itself carry out ROS metabolism or the DNA
  damage response).

## Curation decisions

- 564 x GO:0005515 protein binding (all IPI): REMOVE per CLAUDE.md policy. Generic
  protein binding is uninformative about GRB2's molecular function; removal does
  not dispute that the reported interactions occur. GRB2's actual adaptor function
  is captured by the specific MF terms (GO:0001784, GO:0005068, GO:0005091,
  GO:0030674, GO:0005154, GO:0043560, GO:0046875, GO:0019901, etc.).
- 307 x GO:0005829 cytosol (TAS Reactome + IDA/IEA): ACCEPT. Cytosol is a correct
  and well-supported basal location for this soluble adaptor; the large number of
  Reactome TAS rows is redundant provenance for the same, correct assertion.
- GO:0008180 COP9 signalosome: the IBA and IEA rows assert family-wide membership
  of the CSN (a GPS1/COPS1-8 complex) for an SH2/SH3 adaptor, which is
  biologically implausible; REMOVE those as over-propagation. The IDA (PMID:22561606)
  cites the Tespa1 paper whose abstract concerns the TCR signalosome, not the COP9
  signalosome; full text not available -> UNDECIDED (defer to curator, flag term).
- GO:0003723 RNA binding (HDA, interactome capture): KEEP_AS_NON_CORE -- real
  high-throughput identification, some corroboration from nuclear miRNA-regulation
  work, but not a core adaptor function.
- Specific RTK/partner binding (EGFR, TRKA, ephrin, IRS, kinase, phosphatase):
  ACCEPT the canonical/informative ones; KEEP_AS_NON_CORE the narrower partners.
- Pleiotropic BP (T/B/NK immune activation, myelination, Schwann cell dev,
  actin organization, Rac signaling, DNA damage/ROS/senescence, IGF pathway):
  KEEP_AS_NON_CORE.

No NEW annotations proposed: core molecular functions (phosphotyrosine binding,
RTK/GEF adaptor activity, protein-macromolecule adaptor activity) and their
processes (Ras signal transduction, MAPK cascade regulation, EGFR pathway,
receptor internalization) are all already present in the existing set.

## Provenance for existing_annotations references
Deep research: genes/human/GRB2/GRB2-deep-research-falcon.md (Wang 2024
Biomolecules review; Malagrino 2024; Nocka 2023 eLife BTK; Qiu 2024 PNAS).
