# DNAJC15 (MCJ) research notes

## Identity
- UniProt Q9Y5T4, HGNC:20325, 150 aa. Small single-pass mitochondrial inner-membrane DnaJ/HSP40
  subfamily C protein. AltNames: Methylation-controlled J protein (MCJ); Cell growth-inhibiting
  gene 22 protein (GIG22). Synonym DNAJD1.
- Topology: N-terminal segment in intermembrane space (1-35), single TM helix (36-58), C-terminal
  J domain (96-150) facing the mitochondrial matrix. [file:human/DNAJC15/DNAJC15-uniprot.txt]

## Dual function: TIM23 import co-chaperone AND complex I repressor
### (1) J co-chaperone of TIM23 import motor (PRESEQUENCE translocase)
- PMID:23263864 (Schusdziarra 2013): "MCJ functions as J co-chaperone of the human TIM23 pre-protein
  translocase". "It is anchored in the mitochondrial inner membrane with the C-terminal J domain
  facing the matrix space." "MCJ forms a stable subcomplex with a component of the mitochondrial
  import motor, MAGMAS" (=PAM16). "the recombinant soluble MCJ domain stimulates the ATPase activity
  of the human mtHsp70 chaperone, mortalin" (=HSPA9). "This stimulation is counteracted by MAGMAS."
  "pre-protein import into mitochondria is impaired in the absence of MCJ." "MCJ is able to take over
  the function of Tim14" (=DNAJC19/yeast Pam18). [PMID:23263864]
- UniProt FUNCTION: "Acts as an import component of the TIM23 translocase complex. Stimulates the
  ATPase activity of HSPA9." SUBUNIT: "Directly interacts with PAM16/MAGMAS; this interaction
  counteracts DNAJC15-dependent stimulation of HSPA9 ATPase activity." [file:human/DNAJC15/DNAJC15-uniprot.txt]

### (2) Negative regulator of respiratory chain complex I
- PMID:23530063 (Hatle 2013): "MCJ/DnaJC15 ... localizes at the mitochondrial inner membrane, where
  it interacts preferentially with complex I of the electron transfer chain. We show that MCJ impairs
  the formation of supercomplexes and functions as a negative regulator of the respiratory chain. The
  loss of MCJ leads to increased complex I activity, mitochondrial membrane potential, and ATP
  production." MCJ deficiency prevents pathological lipid accumulation in liver. [PMID:23530063]
- UniProt FUNCTION: "Negative regulator of the mitochondrial respiratory chain. Prevents
  mitochondrial hyperpolarization state and restricts mitochondrial generation of ATP." "Associates
  with complex I ... this interaction may interfere with the formation of supercomplexes."
  [file:human/DNAJC15/DNAJC15-uniprot.txt]

## Disease / cancer
- Methylation-silenced in ovarian cancer; loss correlates with cisplatin chemoresistance
  (PMID:11358853). Highest expression in heart, then liver, kidney. [file:human/DNAJC15/DNAJC15-uniprot.txt]

## GOA decisions
- GO:0001671 ATPase activator activity (IBA): SUPPORTED experimentally (stimulates HSPA9/mortalin
  ATPase). Core MF. ACCEPT.
- GO:0001405 PAM complex / GO:0005744 TIM23 translocase / GO:0030150 protein import into matrix /
  GO:0006886 intracellular protein transport: SUPPORTED (TIM23 import co-chaperone). ACCEPT.
- GO:0005743 mitochondrial inner membrane / GO:0005739 mitochondrion: SUPPORTED. ACCEPT (mito generic
  is non-core relative to inner membrane).
- complex I repressor / negative regulation of respiratory chain: these Ensembl-IEA BP terms
  (GO:0006120, GO:1902957, GO:0031333, GO:0065003, GO:0009267, GO:0019216) are NOT in the seeded
  ai-review list (they're in the UniProt DR block but the GOA tsv only lists a subset). Only review
  what's in the seeded file + goa.tsv.
- IPI protein binding: WITH Q9Y3D7 = PAM16/MAGMAS (PMID:23263864, PMID:33961781) - functionally
  central (counteracts ATPase stimulation). KEEP_AS_NON_CORE (real, but bare term uninformative).
  PMID:25416956 WITH Q8IUQ4, Q8IZU0 (Y2H) - less characterized, KEEP_AS_NON_CORE.
- PMID:10339406 NAS (ComplexPortal) and PMID:34800366 HTP (FlyBase mito) - localization support.

## Core functions
1. ATPase activator activity (GO:0001671) - J co-chaperone stimulating HSPA9/mortalin in TIM23 motor.
2. Negative regulation of mitochondrial respiratory chain via complex I binding. The GOA-seeded list
   does NOT include a respiratory-chain MF/BP term, but it IS a documented core function; capture in
   core_functions with the negative-regulation BP term (GO:1902957 negative regulation of
   mitochondrial electron transport, NADH to ubiquinone), supported by PMID:23530063.
