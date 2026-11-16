# RPTOR (Raptor) review notes

UniProt: **Q8N122** → **RPTOR** (regulatory associated protein of MTOR complex 1;
aka Raptor, KOG1). PANTHER: PTHR12848. Taxon: 9606.

## Core function (standalone summary)

RPTOR is the non-catalytic **substrate-presenting subunit of mTOR complex 1
(mTORC1)** (with MTOR and MLST8). It is a molecular adaptor with two roles:
1. **Recruitment adaptor** — binds the **Rag GTPases** to dock mTORC1 at the
   lysosomal membrane, where it is activated by nutrients.
2. **Substrate-specific adaptor (enzyme-substrate adaptor)** — binds
   **TOS-motif**-containing substrates (EIF4EBP1/4E-BP1, RPS6KB1/S6K1; also the
   inhibitor AKT1S1/PRAS40) and directs them to the active site of the MTOR
   kinase, conferring substrate specificity on the complex.

## Key evidence (provenance)

- UniProt Q8N122 CC:FUNCTION: "Within the mTORC1 complex, RPTOR acts both as a
  molecular adapter, which (1) mediates recruitment of mTORC1 to [the lysosome via
  Rag GTPases] ... and a (2) substrate-specific adapter, which promotes substrate
  specificity by binding to TOS motif-containing proteins and direct them towards
  the active site of the MTOR [kinase]." CC:SUBUNIT: "Interacts with (via TOS
  motifs) EIF4EBP1 and RPS6KB1; interaction is independent of its association with
  MTOR."
- [PMID:12150926 abstract]: "Raptor, a binding partner of target of rapamycin
  (TOR), mediates TOR action." Raptor binding to mTOR is required for
  mTOR-catalysed 4E-BP1 phosphorylation.
- [PMID:12747827 abstract]: "TOS motif-mediated raptor binding regulates 4E-BP1
  multisite phosphorylation" — TOS motifs in S6K1 (N-term) and 4E-BP1 (C-term)
  mediate raptor binding/substrate presentation.
- [PMID:24403073 abstract, full text]: "Raptor in mTOR complex 1 is believed to
  recruit 4E-BP1, facilitating phosphorylation of 4E-BP1 by the kinase mTOR."
- [PMID:37541260 abstract]: O-GlcNAcylation of Raptor (Thr700) "facilitates the
  interactions between Raptor and Rag GTPases and promotes the translocation of
  mTOR to the lysosomal surface."
- [PMID:26588989 abstract]: "NLK phosphorylates Raptor on S863 to disrupt its
  interaction with the Rag GTPase, which is important for mTORC1 lysosomal
  recruitment."

## Annotation landscape (GOA, 170 rows)

- **61 × GO:0005515 protein binding (IPI)** — triage by partner: MTOR (P42345,
  mouse Q9JLN9) → GO:0019901 protein kinase binding; TOS-motif substrates
  (RPS6KB1 P23443, EIF4EBP1 Q13541, AKT1S1 Q96B36) → GO:0140767 enzyme-substrate
  adaptor activity; others (MLST8 Q9BVC4, BRAF P15056, singletons) → REMOVE.
- Adaptor MFs: GO:0140767 enzyme-substrate adaptor activity (IDA), GO:0030674
  protein-macromolecule adaptor activity (IDA/IBA), GO:0031267 small GTPase
  (Rag) binding, GO:0019901 protein kinase binding, contributes_to GO:0004674.
- Core processes: TORC1 signaling (GO:0038202), part_of TORC1 complex
  (GO:0031931), cellular response to nutrient levels / amino acids / leucine /
  glucose / starvation, (negative) regulation of autophagy. Core locations:
  lysosomal membrane, cytosol, lysosome.
- Downstream/pleiotropic (KEEP_AS_NON_CORE): cell growth/size, glycolysis, lipid
  biosynthesis, Pol III transcription, G1/S, hypoxia/osmotic stress.
- Over-annotations (ISS/IEA, distal): social behavior, osteoclast/odontoblast
  differentiation, xenobiotic response.
