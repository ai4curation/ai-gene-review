# sctN2 (ssaN, STM1415, P74857) — curation notes

Salmonella enterica serovar Typhimurium LT2. SPI-2 (T3SS-2) injectisome ATPase; SctN-family
paralog of the flagellar FliI, SPI-1 InvC (SctN1, P0A1B9), Yersinia YscN, Shigella Spa47,
EPEC EscN.

## Direct experimental evidence on this protein

- Purified enzyme hydrolyses ATP; the catalytically dead R192G variant (DCCD-box arginine) does not.
  [PMID:24722491 "Purified SsaN-Myc-His6 hydrolyzed ATP in a linear, time-dependent manner with a mean ATPase activity of 0.36"]
  Km(ATP) = 0.81 mM; activity rises non-linearly with protein concentration (cooperative, ring-forming ATPase).
- Required for SPI-2 secretion: [PMID:24722491 "SseB secretion from the ssaN mutant strain was undetectable"];
  translocation of SseJ into HeLa cells is lost in the mutant and restored by complementation, but not by
  R192G, tying the secretion role to catalysis.
- Chaperone-cargo release: [PMID:24722491 "our results indicate that SsaN releases the translocator protein SseB from the T3SS-2 specific chaperone SsaE in an ATP-dependent manner"];
  no release with ATPgammaS or with R192G, although R192G still binds SsaE.
- Binds SPI-2 chaperones [PMID:24722491 "Therefore, we next examined for interactions between SsaN and the T3SS-2 specific chaperones SsaE, SseA, SscA, and SscB"]
  (H9L4A0 SsaE, O84944 SseA, H9L426 SscA, H9L491 SscB), and the multicargo chaperone SrcA via a discrete
  C-terminal module [PMID:25035427 "The C-terminal region of T3SS ATPases mediates binding with multiple contact points along the chaperone."]
- Sorting-platform/C-ring partners: SsaK/SctL2 (P74853, FliH/YscL-like stator) and SsaQ (P74860, FliN/YscQ-like)
  [PMID:24722491 "SsaN interacted with SsaK and SsaQ to form the C ring complex"].
- Localisation: soluble plus peripheral inner-membrane pool under SPI-2-inducing LPM pH 5.8
  [PMID:24722491 "were detected in both the soluble and membrane fractions"]; membrane association is
  independent of SsaK/SsaQ [PMID:24722491 "These results indicated that SsaN could associate with the membrane regardless of the presence of the other ATPase-associated components."].
  No transmembrane segment in the sequence.
- Structure: 2.1 A crystal structure, PDB 4NPH [PMID:25035427 "crystal structure of the Salmonella enterica SPI-2-encoded ATPase, SsaN"];
  hexamer modelled on F1 [PMID:25035427 "SsaN homologues have been shown to exist as hexamers"].
- Virulence: mixed mouse infection CI drops to ~0.05 [PMID:24722491 "The CI value of the wild-type strain versus the ssaN mutant strain was significantly reduced to 0.047"];
  chaperone-docking mutants that retain ATPase activity are also attenuated [PMID:25035427].

## Why the ATP-synthase / proton-transport terms are wrong here

- SctN/FliI ATPases are paralogs of the F1 beta subunit but have no Fo partner and no proton channel;
  the flagellar enzyme is insensitive to F-, V- and P-type inhibitors
  [PMID:8943245 "The activity was not affected by inhibitors of the F-, V- or P-type ATPases"].
- For injectisomes as for flagella, the proton motive force is what drives translocation across the inner
  membrane, through the export gate, not through the ATPase
  [PMID:25701111 "the pmf therefore the primary fuel for secretion via the T3SS"],
  [PMID:25701111 "Collapsing the pmf abolishes protein export via T3SS."]. Dependence of the system on the
  pmf is not proton transport by SsaN.
- IBA rows (GO_REF:0000033, GO:0046933 and GO:0045259) come from PANTHER node PTN008558586. In the cached
  PAINT table (`interpro/panther/PTHR15184/PTHR15184-paint.tsv`) that node carries both IBDs, seeded only by
  F1-beta proteins (E. coli AtpD P0ABB4, human ATP5F1B P06576, yeast ATP2, S. pombe atp2, plant/rat beta).
  `projects/TREEGRAFTER/rotary_atpase/node_placement.tsv` shows PTN008558586 is a DUPLICATION node with two
  children: PTN008558588 (the ATP synthase beta subfamilies, SF51/74/75/76/80/82/83/85) and PTN000390097
  (the bacterial export ATPases, PTHR15184:SF62 SPI-2 T3SS ATPase = this protein, SF9 SPI-1, SF81 flagellar).
  So the IBD sits *on* the duplication node that separated F1-beta from the export ATPases; every seed
  lies in the sister child. The node placement, not the donor list, is the problem: the correct placement is
  PTN008558588 (or an IRD/NOT at PTN000390097).
- InterPro2GO from IPR013380 (T3SS ATPase SctN) currently yields GO:0046961 (rotational proton-transporting
  ATPase) and GO:0006754 (ATP biosynthetic process). These are wrong for an SctN signature: the family
  hydrolyses ATP for export and neither synthesises ATP nor moves protons. GO_REF:0000108 then propagates
  GO:1902600 from GO:0046961 and GO:0015986 from the IBA GO:0046933. Fixing the two sources removes four rows.
- UniProt is already correct for this entry: RecName "SPI-2 type 3 secretion system ATPase", EC 7.4.2.8
  (protein-exporting), not EC 7.1.2.2. No name change needed here (unlike several FliI entries).

## AgBase rows that do not follow from the cited paper

- GO:0030430 host cell cytoplasm (IMP) and GO:0033644 host cell membrane (IMP), both from PMID:24722491.
  The paper localises SsaN to the *bacterial* soluble and membrane fractions (Fig. 5) and shows that the
  *effector* SseJ-2HA reaches the host vacuolar membrane in a SsaN-dependent way (Fig. 2D/E). SsaN itself is
  never shown in a host compartment, and as a cytoplasmic sorting-platform ATPase it is not a translocated
  substrate. These look like the effector's localisation transferred to the machine. Host cell cytoplasm is
  removed; host cell membrane is redirected to GO:0005886 plasma membrane, which is what the fractionation
  actually supports.
- GO:0050714 positive regulation of protein secretion (IMP). SsaN is a core component of the secretion
  machine, not a regulator of it: deleting it abolishes secretion outright. GO:0030254 protein secretion by
  the type III secretion system states the role directly.

## Family/classification bookkeeping

- PANTHER: PTHR15184 (ATP SYNTHASE) subfamily PTHR15184:SF62 "SPI-2 TYPE 3 SECRETION SYSTEM ATPASE".
- InterPro: IPR000194, IPR004100-related N-terminal domain, IPR005714 (FliI/YscN), IPR013380 (SctN),
  IPR040627 (T3SS ATPase C-terminal, the chaperone-docking module of PMID:25035427).
