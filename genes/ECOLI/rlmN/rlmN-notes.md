# rlmN (P36979, E. coli K-12) notes

Deep research was not available for this gene (falcon returns 403; asta gave
nothing useful in Phase 1 of the RADICAL_SAM project). These notes are built
from cached primary papers, UniProt and PubMed.

## Identity and activity

- RlmN (formerly YfgB, b2517) is the 23S rRNA m2A2503 methyltransferase.
  Deletion removes m2A2503 and plasmid rescue restores it
  [PMID:18025251 "Inactivation of the yfgB gene in E. coli led to the loss of modification at nucleotide A2503 of 23S rRNA"].
- In vitro reconstitution with [4Fe-4S]-reconstituted enzyme, dithionite and
  [methyl-3H]SAM: RlmN makes 2-methyladenosine; SAM is both methyl donor and
  5'-dA radical source [PMID:20184321 "S-Adenosylmethionine (SAM) is both the methyl donor and the source of a 5'-deoxyadenosyl radical"].
  The substrate is protein-free 23S rRNA, not the assembled 50S/70S
  [PMID:20184321 "neither enzyme can act on the assembled 50S subunit or the 70S ribosome, but protein-free 23S rRNA proved to be a good substrate"].
- Dual specificity: RlmN also makes m2A37 in a subset of tRNAs; deletion
  removes m2A from both RNA types [PMID:22891362 "E. coli RlmN is a dual-specificity enzyme that catalyzes methylation of both rRNA and tRNA"].
  Position 38 is a key tRNA determinant [PMID:27902775].
- Crystal structure of RlmN C118A cross-linked to tRNAGlu: contacts the whole
  tRNA and unfolds the anticodon stem-loop [PMID:27081063 "RlmN contacts the entire length of tRNA(Glu)"].

## Mechanism

- Ping-pong via methylated Cys355 [PMID:21415317 "both reactions proceed by a ping-pong mechanism involving intermediate methylation of a conserved cysteine residue"].
  The methyl is assembled from a SAM-derived methylene plus a hydrogen from the
  substrate ("methyl synthase") [PMID:21368151].
- A single [4Fe-4S] cluster (CxxxCxxC, Cys125/129/132); the two other conserved
  Cys (118, 355) bind no iron [PMID:21916495 "each protein contains only the one \"radical SAM\" [4Fe-4S] cluster"].
- Structure with SAM: one SAM on the cluster's unique iron; Cys355 is
  S-methylated next to the SAM methyl [PMID:21527678 "a single molecule of SAM coordinates the [4Fe-4S] cluster"].
- Cross-linked protein-RNA radical intermediate; Cys118 resolves it
  [PMID:24806349].

## Physiology

- Loss of m2A2503 lowers competitive fitness and slightly raises susceptibility
  to tiamulin, hygromycin A and sparsomycin [PMID:18025251].
- dRlmN increases UAG read-through; attributed to loss of m2A2503 in the PTC
  [PMID:22891362].
- RlmN does not significantly influence antibiotic resistance, unlike Cfr
  [PMID:23752511 "RlmN does not significantly influence antibiotic resistance"].

## Curation decisions

- Generic rows follow the RADICAL_SAM treatment rule: GO:0003824 and
  GO:0008173 MODIFY to the two specific MFs; GO:0051536 MODIFY to GO:0051539;
  GO:0051539 ACCEPT; GO:1904047 added as NEW (IDA, Boal 2011 structure).
- Seven GO:0005515 rows (TAP-MS PMID:15690043, Y2H PMID:24561554; partners
  RplO, MalT, SrmB, FtsZ) REMOVE as uninformative. The RplO (uL15) and SrmB
  (50S assembly helicase) partners are at least consistent with RlmN acting
  on 23S rRNA during subunit assembly, but no specific MF follows.
- tRNA binding / rRNA binding kept as non-core (substrate binding, entailed
  by the methyltransferase activities).
- rRNA processing (IEA) MODIFY to rRNA base methylation (same as STAWA/cfr).
- Not added: "response to antibiotic" (cfr has it, but RlmN does not confer
  resistance) and "translational fidelity" (an indirect effect of the
  modification).

## Consistency with other reviews

- STAWA/cfr: uses MARK_AS_OVER_ANNOTATED for GO:0003824 and KEEP_AS_NON_CORE
  for GO:0051539, both now contrary to the project treatment rule; no SAM
  binding row. To fix in Phase 3.
