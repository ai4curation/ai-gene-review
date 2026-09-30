# UNC93B1 (Q9H1C4, human) — curation notes

Unc-93 homolog B1; ER-resident multi-pass (12-TM) membrane chaperone/trafficking factor for
nucleotide-sensing Toll-like receptors.

## Deep research
Falcon deep research did not complete during this session; no `-deep-research-falcon.md` was
produced. Review is based on the cached UniProt record, cached PMIDs, Reactome, OLS/QuickGO, and
the cached GO-CAM (65a1f4f800002740).

## Core biology
- ER-resident polytopic membrane protein; its function is to deliver nucleotide-sensing TLRs
  (TLR7, TLR9; also TLR3, TLR8) from the ER to endolysosomes
  [PMID:18305481 "function of the polytopic membrane protein UNC93B1 is to deliver the nucleotide-sensing receptors TLR7 and TLR9 from the ER to endolysosomes"].
- Physically interacts with TLR3/7/8/9 in the ER via their transmembrane regions
  [PMID:18305481 "essential for\nsignalling of TLR3, TLR7 and TLR9 in both humans and mice, physically interacts\nwith these TLRs in the endoplasmic reticulum (ER)"; PMID:33432245 "Both TLRs interact with the UNC93B1\namino-terminal six-helix bundle through their transmembrane and luminal\njuxtamembrane regions"].
- Cryo-EM structures of human/mouse TLR3-UNC93B1 and human TLR7-UNC93B1 complexes; UNC93B1
  resembles MFS transporters and is indispensable for TLR ER-to-endosome trafficking
  [PMID:33432245 "indispensable for the\ntrafficking of TLRs from the endoplasmic reticulum to the endosome"].
- UNC93B1 also physically associates with human TLR8 and is critical for TLR8 signalling
  [PMID:22164301 "UNC93B1 physically associated with human TLR8,\nsimilar to TLRs 3, 7, and 9, and played a critical role in TLR8-mediated\nsignaling"].
- Crucially, UNC93B1 is DISPENSABLE for ligand recognition and signal initiation by the TLRs
  themselves — it acts upstream as a trafficking chaperone, not as a signal transducer
  [PMID:18305481 "UNC93B1 is dispensable for ligand recognition and signal initiation by TLRs"].
- The mouse 3d mutation (H412R, Unc93b1) abolishes TLR3/7/9 signalling and antigen cross-presentation
  [PMID:16415873 "no signaling\noccurs via the intracellular Toll-like receptors 3, 7 and 9"].
- Human UNC-93B (UNC93B1) deficiency causes isolated herpes simplex encephalitis via impaired
  type I/III IFN responses [PMID:16973841 "autosomal recessive deficiency in the intracellular protein\nUNC-93B, resulting in impaired cellular interferon-alpha/beta and -lambda\nantiviral responses"].
- UNC93B1-deficient human cells are unresponsive to TLR3, TLR7, TLR8 and TLR9 and patients show
  defective B-cell tolerance checkpoints [PMID:19006693 "UNC-93B-deficient cells are unresponsive to TLR3, TLR7,\nTLR8, and TLR9"].
- Also required for TLR5 (a cell-surface TLR) plasma membrane localization and signalling
  [PMID:24778236 "TLR5, a cell surface receptor for bacterial protein flagellin, also\nrequires UNC93B1 for plasma membrane localization and signaling"].

## Participation-test analysis for TLR signaling-pathway process terms (project focus)
UNC93B1 is a trafficking chaperone. Applying the CLAUDE.md participation test: the "work" of a TLR
signaling pathway (ligand binding, receptor dimerization, TIR/adaptor recruitment, kinase
activation) is performed by the TLR and downstream components, NOT by UNC93B1. UNC93B1 is
*required* for the pathway (knockout abolishes signalling), but this is necessity, not
participation — and the same paper that establishes necessity states UNC93B1 is dispensable for
signal initiation [PMID:18305481]. UNC93B1 acts upstream as the chaperone that positions the
receptor.

However, GO curators have consistently annotated both human (Q9H1C4) and mouse (Q8VCW4) UNC93B1
to GO:0034138/0034154/0034162 (TLR3/7/9 signaling pathway) with experimental (IMP) and
phylogenetic (IBA, PANTHER:PTN002928790) evidence, and the mouse rows use
`acts_upstream_of_or_within`. Per the "do not overrule curators from incomplete evidence" rule,
these experimental annotations are not removed. Instead they are marked KEEP_AS_NON_CORE: the core
molecular function is Toll-like receptor binding / protein carrier (trafficking) activity and the
core process is intracellular protein transport; the TLR signaling-pathway terms record the
downstream process UNC93B1 enables as an upstream chaperone, which is non-core.

Comparator: CNPY3 (Q9BT09), another TLR chaperone, carries signaling receptor binding (GO:0005102)
but is not annotated to the TLR signaling-pathway process terms in QuickGO — consistent with the
view that a chaperone's core representation is receptor binding + trafficking rather than pathway
participation. UNC93B1's pathway annotations are a curator convention grounded in strong knockout
data, retained here as non-core.

## GO:0005515 generic protein binding rows
- PMID:22164301 (TLR8, Q9NR97) and PMID:33961781 (TLR8, Q9NR97): partner is a TLR → MODIFY to
  GO:0035325 Toll-like receptor binding (informative, supported).
- PMID:32296183 (HuRI binary interactome, ~24 partners: BEST2, CCDC107, CD79A, CLDN7, CREB3L1,
  CSE1L... EBP, ERGIC3, FATE1, FFAR3, GPR101, GPR37L1, GPRC5D, HHLA2, KLRC1, LDLRAD1, LEUTX, LIME1,
  MFF, REEP1, SLC35C2, SSMEM1, SYNDIG1, TM4SF18, TMEM237): high-throughput Y2H binary interactome,
  mostly membrane proteins with no functional follow-up → REMOVE as uninformative generic binding
  (removal does not assert the interactions are false).
- PMID:30833792 (CSE1L P55060, KPNB1 Q14974): interferon-stimulated-gene AP-MS network; nuclear
  transport proteins, no established functional UNC93B1 role → REMOVE as uninformative.
- PMID:33845483 (SARS-CoV-2 ORF7b P0DTD8, Xeno): virus-host proteomics screen → REMOVE as
  uninformative.

## Locations
ER and ER membrane (core, IDA), Golgi membrane (transits), endosome and lysosome (relocalizes with
CpG stimulation), early phagosome / phagocytic vesicle (ortholog/subcell mapping, non-core). All
ACCEPT; consistent with the ER-to-endolysosome trafficking route.
