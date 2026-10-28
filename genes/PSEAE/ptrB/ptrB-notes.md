# ptrB (PA0612, G3XDA6) notes

## Identity

- UniProt G3XDA6, unreviewed, 66 aa; gene ptrB, locus PA0612. Single
  DksA/TraR C4-type zinc finger (Pfam PF01258, 34-65; PROSITE PS51128,
  PS01102; NCBIfam TIGR02419 C4_traR_proteo); PANTHER PTHR38777 (Fels-2
  prophage protein). The two CxxC pairs (CEDC, CSRC) of the C4 motif are
  present in the sequence.
- Lies between prtR (PA0611, pyocin repressor) and PA0613, at the start of the
  R/F pyocin gene cluster; PA0612-PA0613 form an operon repressed by PrtR.

## Literature

- Wu and Jin 2005 (PMID:16109947; strain PAK; full text cached) identified
  ptrB as the PrtR-repressed repressor of the type III secretion system (TTSS)
  [PMID:16109947 "Expression of ptrB is specifically repressed by PrtR, and
  mitomycin C-mediated suppression of the TTSS is also abolished in a ptrB
  mutant strain."; "Therefore, PtrB is a new TTSS repressor that coordinates
  TTSS repression and pyocin synthesis under the stress of DNA damage."].
  Deleting PA0612, not PA0613, restored ExoS production in a prtNR background
  [PMID:16109947 "PA0612, but not PA0613, is required for TTSS repression in
  the prtR mutant background."]. PtrB does not bind ExsA in a two-hybrid
  assay [PMID:16109947 "PtrB has a prokaryotic DskA/TraR C4-type zinc-finger
  motif but does not directly interact with the master regulator, ExsA."].
  Mechanism unknown [PMID:16109947 "Whether PtrB exerts its repressor function
  through interaction with another regulator or through binding to specific
  DNA sequences present in the TTSS operons or their upstream regulator genes
  is not known."].
- Pyocin synthesis is the job of PrtN, not PtrB [PMID:16109947 "PrtN
  activates the expression of pyocin synthesis genes, while PtrB represses the
  TTSS genes."]. The paper never mentions secondary metabolites, and pyocins
  are protein bacteriocins, not secondary metabolites.

## Participation test

PtrB is a negative regulator of type III secretion; the mutant phenotype is
derepression of ExoS secretion and exoT transcription, which by GO convention
supports a negative regulation term (IMP). Nothing in the paper relates PtrB
to any secondary metabolite pathway, positively or negatively. The seeded
term is not a phenotype of PtrB loss at all; it is unsupported.

Clade check: PTN002215317 leaves are E. coli and Salmonella YbiI, a
Salmonella plasmid TraR, Salmonella Fels-2 prophage protein STM2731,
Haemophilus HI_1497, Xanthomonas XCC1304, P. aeruginosa PA4870 and PtrB:
small phage- and plasmid-borne DksA/TraR-type zinc-finger proteins with no
shared secondary-metabolite role. The term cannot be propagated across them.

GO has no "regulation of type III secretion" term; the nearest is
GO:0050709 negative regulation of protein secretion, proposed as NEW (IMP).

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN002215317 | GO:1900378 positive regulation of secondary metabolite biosynthetic process | 1 (sole) | 8 (5 taxa) | GO:1900378, IMP, PMID:16109947 (PseudoCAP) | WRONG | The paper shows PtrB represses type III secretion; it reports no secondary-metabolite phenotype, and pyocin genes are activated by PrtN, not PtrB. The node's phage/plasmid DksA/TraR-like leaves share no such role. Withdraw the IBD. |

## Decisions summary

- REMOVE: positive regulation of secondary metabolite biosynthesis (IBA and
  IMP), with PSEUDOCAP and GO_CENTRAL defects.
- KEEP_AS_NON_CORE: zinc ion binding (IEA, C4 motif).
- NEW: GO:0050709 negative regulation of protein secretion (IMP,
  PMID:16109947).
