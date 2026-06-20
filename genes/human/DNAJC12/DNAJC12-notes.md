# DNAJC12 (JDP1) research notes

## Identity
- UniProt Q9UKB3 (DJC12_HUMAN), 198 aa. HGNC:28908. Synonym JDP1. "J domain-only" protein:
  N-terminal J domain (14-79, HPD motif) + C-terminal disordered region; no other folded domain.
- Cytoplasmic (isoform a). NMR structure of J domain (PDB 2CTQ).

## Core function: cytosolic HSP70 co-chaperone for aromatic amino acid hydroxylases
- Co-chaperone that participates in proper folding of biopterin (BH4)-dependent aromatic amino acid
  hydroxylases: PAH, TH (tyrosine 3-monooxygenase), TPH1, TPH2.
  [file:human/DNAJC12/DNAJC12-uniprot.txt "Probable co-chaperone that participates in the proper folding
  of biopterin-dependent aromatic amino acid hydroxylases, which include phenylalanine-4-hydroxylase
  (PAH), tyrosine 3-monooxygenase (TH) and peripheral and neuronal tryptophan hydroxylases (TPH1 and
  TPH2)."]
  [PMID:28132689 "DNAJC12 encodes a co-chaperone of the HSP70 family which interacts with PAH, tyrosine
  hydroxylase, and tryptophan hydroxylase."]
- Binds Hsc70 (HSPA8) in unstressed cells; J domain stimulates HSP70 ATPase.
  [PMID:24122553 "The most frequently identified partner of DNAJC12 in unstressed cells was Hsc70, a
  cognate Hsp70 chaperone, whereas in stressed cells, the ER chaperone BiP was frequently associated with
  DNAJC12." ; "These results clarify the role of DNAJC12 in the regulation of Hsp70 function."]
- J-domain HPD motif stimulates HSP70 ATPase. [PMID:28132689 "the J-domain ... promotes functional
  interactions with chaperones of the HSP70 family by stimulating their ATPase activity ... HPD motif ...
  crucial for binding to HSP70 proteins and for ATPase stimulation."]
- PAH enzyme activity reduced in presence of DNAJC12 mutations [PMID:28132689 "PAH enzyme activity was
  reduced in the presence of DNAJC12 mutations."]

## Localization
- Cytoplasm (IDA PMID:24122553; diffusely distributed in cytoplasm). Up-regulated by ER stress.

## Disease
- Biallelic loss-of-function -> hyperphenylalaninemia, non-BH4-deficient (HPANBH4), with dystonia,
  intellectual disability, dopamine/serotonin deficiency (parkinsonism spectrum). Treatable with BH4 and
  neurotransmitter precursors. [PMID:28132689]

## GOA WITH-partner key
- P17752 = TPH1 (tryptophan hydroxylase 1) - a hydroxylase client. P11142 = HSPA8/Hsc70.

## Review logic
CORE MFs:
- The bare protein binding rows: PMID:24122553 WITH HSPA8 (Hsc70) -> MODIFY to Hsp70 protein binding
  (GO:0030544). PMID:28514442 / PMID:33961781 WITH TPH1 -> these capture client (hydroxylase) binding; the
  TPH1 interaction reflects the hydroxylase-chaperoning function. Could MODIFY to a client-binding MF but
  no specific "aromatic amino acid hydroxylase binding" term; keep as KEEP_AS_NON_CORE or note client.
- No explicit ATPase activator activity / Hsp70 binding term in GOA, so propose Hsp70 protein binding as
  core MF (supported by Hsc70 interaction + J-domain ATPase stimulation).
CC:
- cytoplasm (IBA/IEA/IDA): ACCEPT, CORE compartment.
