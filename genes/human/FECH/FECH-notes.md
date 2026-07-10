# FECH (Ferrochelatase, mitochondrial) — review notes

UniProt: P22830 (HEMH_HUMAN). HGNC:3647. EC 4.98.1.1 (formerly 4.99.1.1).
Chromosome 18q21.3. 423 aa precursor; 54-aa mitochondrial transit peptide;
mature chain 55-423.

## Core biology (grounded in UniProt P22830 + cached PMIDs)

- **Function.** Catalyses the eighth and final (terminal, committed) step of heme
  biosynthesis: insertion of ferrous iron (Fe2+) into protoporphyrin IX to form
  protoheme (heme b). UniProt FUNCTION: "Catalyzes the ferrous insertion into
  protoporphyrin IX and participates in the terminal step in the heme biosynthetic
  pathway." Catalytic activity RHEA:22584; EC=4.98.1.1
  [PMID:8276824 "catalyzes the terminal step in the heme"; "the insertion of ferrous iron into protoporphyrin IX"].
- **Cofactor.** Binds one [2Fe-2S] cluster (ChEBI:190135). Ligated by C196, C403,
  C406, C411 (four cysteine ligands per PDB 1HRK/2HRC). Cluster required for
  activity/stability; may act as an NO sensor
  [PMID:8973195 "in ligating the [2Fe-2S] cluster"].
- **Structure/subunit.** Homodimer on the matrix side of the inner mitochondrial
  membrane; peripheral membrane protein. Crystal structures 1HRK, 2HRC, etc.
  [PMID:17261801 "homodimeric, inner mitochondrial membrane-associated enzyme"; "possesses an essential [2Fe-2S] cluster"].
- **Localization.** Mitochondrion inner membrane; peripheral membrane protein; matrix
  side (UniProt SUBCELLULAR LOCATION, by similarity to rat P22315). GOA carries
  GO:0005743 (mito inner membrane) and GO:0005739 (mitochondrion).

## Interactions / metabolon

- Forms the mitochondrial heme biosynthesis metabolon. Dimeric FECH bridges ABCB7
  and ABCB10 homodimers (complex required for heme biosynthesis / cellular iron
  homeostasis) [PMID:30765471 "A dimeric ferrochelatase physically bridged ABCB7 and ABCB10"; "characterized a complex formed of"; "complex required for heme biosynthesis"].
- Interacts with PGRMC1 (and PGRMC2); PGRMC1 binding decreases FECH activity in vitro
  in a dose-dependent manner (proposed heme chaperone/sensor, regulator of product
  release) [PMID:27599036 "In the presence of PGRMC1 in vitro measured FECH activity decreased in a dose dependent manner"].
- Frataxin (FXN) delivers iron to FECH for the terminal step (iron donor at the
  matrix-side site of the homodimer) [PMID:15123683 "iron binding partner for Hs ferrochelatase that is capable of both delivering"; "a potential binding site for an iron donor protein on the matrix side"].
- Forms oligomeric complex with mitoferrin-1 (SLC25A37/MFRN1) and ABCB10 to channel
  iron to heme synthesis [PMID:36836934 "FECH forms an oligomeric complex with mitoferrin-1 (MFRN1), a mitochondrial iron transporter, and ATP-binding cassette sub-family B member 10 (ABCB10)"].

## Disease

- Erythropoietic protoporphyria (EPP1, MIM:177000). Many EPP1 loss-of-function
  variants (UniProt VARIANT block). Photosensitivity from protoporphyrin IX
  accumulation. F417S has <2% normal activity [PMID:8276824 "The F417S mutant has less than 2% of the"; PMID:1376018 "which catalyzes the last step in the heme"; "elevated protoporphyrin levels"].

## GOA notes

- GOA MF label for GO:0004325 is "protoporphyrin ferrochelatase activity" (current GO
  label). Kept as-is in existing_annotations. core_functions uses same current label.
- Ensembl-projected "response to X" BP terms (xenobiotic, metal ion, lead, insecticide,
  ethanol, arsenic, methylmercury, platinum, dexamethasone) are ortholog projections
  from rat (ENSRNOP.../A0A8I6GEM4) via GO_REF:0000107. Not core; over-annotations for
  the molecular function of FECH — reflect rat toxicology stress-response experiments.
- GO:0043190 (ABC transporter complex) part_of comes from the ABCB7/ABCB10 metabolon
  paper (PMID:30765471). FECH is not itself an ABC transporter; it bridges two ABC
  transporter homodimers. Keep as non-core (documents metabolon membership).
- GO:0006091 (generation of precursor metabolites and energy) TAS is a broad/legacy
  ProtInc term — over-annotation; heme biosynthesis is the specific process.
- GO:0009416 (response to light stimulus) TAS from PMID:1376018 reflects EPP
  photosensitivity phenotype, not a molecular response-to-light function of the enzyme.
</content>
