# ORC5 (donkey, A0A9L0JAR4) notes

## Sequence and record

- Unreviewed TrEMBL entry, 440 aa, "Origin recognition complex subunit 5"; PANTHER
  PTHR12705:SF0; Orc1-like AAA ATPase domain (8..155), ORC5 lid (204..271), ORC5 C-terminal
  winged-helix region (302..421) [file:EQUAS/ORC5/ORC5-uniprot.txt "Belongs to the ORC5 family."].
- 6 GOA rows, all IEA (InterPro2GO, TreeGrafter, GO_REF:0000120 combined).
- Donkey vs human O43913 (435 aa): 92.87% identity, 100% coverage of human; donkey has a
  5-residue C-terminal extension (436-440); Walker A P-loop GHTASGKT conserved
  [file:EQUAS/ORC5/ORC5-bioinformatics/RESULTS.md "BINDING (): human [37, 38, 39, 40, 41, 42, 43, 44] GHTASGKT -> donkey [37, 38, 39, 40, 41, 42, 43, 44] GHTASGKT."].

## Ortholog biology

- Human ORC5: subunit of the six-subunit ORC that binds replication origins in an
  ATP-dependent manner and is required to assemble the pre-replication complex
  [file:EQUAS/ORC5/ORC5-bioinformatics/human_O43913-uniprot.txt "ORC is required to assemble the pre-replication complex necessary to initiate DNA replication."].
- Human ORC cryo-EM: ORC2-5 forms a stable core; ORC subunits 1-5 have positively charged
  regions near DNA; the ORC5-ORC3 interface acts as a hinge that may facilitate DNA binding
  [PMID:32808929 "revealing a hinge at the ORC5·ORC3 interface that may facilitate ORC binding to DNA"].
- Human GOA (QuickGO 2026-10-14): nuclear ORC (IDA, IPI), DNA replication initiation (IDA),
  DNA replication origin binding (TAS, IBA).

## Decisions

- Core: nuclear origin of replication recognition complex, DNA replication initiation, DNA
  replication origin binding (as a contributing subunit of ORC), nucleus.
- ORC (InterPro): ACCEPT; DNA replication (combined IEA): TOO_GENERAL.

## ProtNLM2 (donkey40 snapshot)

- GO:0006260 DNA replication -> LSP (DNA replication initiation in GOA).
- GO:0005634 nucleus -> CNN (exact term in GOA, correct).
- Non-GO: function text describing ORC component binding origins, ATP-dependent DNA binding,
  pre-RC assembly (not scored; closely mirrors the ARBA function text in the donkey record).
