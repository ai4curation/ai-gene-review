# PBL1 (At3g55450; Q8H186) review notes

## Identity
- PBS1-LIKE 1 / BIK1-like kinase (BLK) / CHANGED CALCIUM ELEVATION 5 (CCE5); RLCK subfamily VII, closest paralog of BIK1.
- N-terminal Gly2 myristoylation site; plasma-membrane targeting required for function
  [PMID:25522736 "Hence, myristoylation and proper targeting of PBL1 to plasma membrane is essential for signaling function of PBL1."]

## Kinase activity (direct evidence)
- cce5 missense alleles abolish autophosphorylation
  [PMID:25522736 "Taken together, these three cce5 mutations led to the loss of PBL1 kinase activity"].
- Direct in vitro substrates: PHT1;4 / PHT1;1 cytosolic loops
  [PMID:34919806 "Indeed, maltose-binding protein (MBP)-fused BIK1 and PBL1, but not their kinase-dead variants, phosphorylated the glutathione S-transferase (GST)-fused cytosolic loop of PHT1;4"];
  vacuolar CAX1/CAX3 S-cluster [PMID:38418878 "the associated cytoplasmic kinases BIK1 and PBL1, which phosphorylate the same S-cluster in CAXs to modulate Ca2+ signals in immunity" — abstract only].

## Receptor coupling
- Associates with FLS2 and is phosphorylated after flg22 [PMID:20413097 "In unstimulated plants, BIK1 and PBL1 interact with FLS2 and are rapidly phosphorylated upon FLS2 activation by its ligand flg22." — abstract only].
- Interacts with PEPR1 [PMID:23431184 "PEPR1 specifically interacts with receptor-like cytoplasmic kinases botrytis-induced kinase 1 (BIK1) and PBS1-like 1 (PBL1) to mediate Pep1-induced defenses"].
- MIK2/SCOOP signalling [PMID:34535661 "the MIK2-BAK1 receptor complex activation by SCOOPs triggers phosphorylation of BIK1 and PBL1 in transducing signaling to downstream events"].

## Calcium signalling and ligand specificity (important for chitin module)
- cce5/pbl1 reduced Ca2+ responses to flg22, elf18, AtPep1, but NOT to chitin
  [PMID:25522736 "Using these lines, a survey of different MAMPs/DAMPs showed reduced calcium responses to flg22, elf18 and AtPep1 but a normal response to chitin octamers (ch8) in cce5 (Figure 2)."]
- PBL1 > BIK1 for flg22 root growth inhibition [PMID:25522736 "PBL1 plays a more important role than BIK1 in the late root growth inhibition response to flg22"].
- PBL1 is not required for flg22-induced resistance to Pseudomonas [PMID:25522736 "BIK1, but not PBL1, has been shown to play an important role in flg22-mediated resistance to subsequent Pseudomonas syringae infection"].

## RBOHD
- Deep research: PBL1 binds RBOHD N-terminus in vitro; RBOHD phosphosite reduction is only in the bik1 pbl1 double mutant; direct site-resolved RBOHD phosphorylation was shown for BIK1, not PBL1 (Kadota 2014, PMID:24630626, abstract-only cached; no PBL1 mention in abstract)
  [file:ARATH/PBL1/PBL1-deep-research-falcon.md "The evidence therefore supports PBL1 participation in an RBOHD-associated, reactive-oxygen signaling pathway, but is weaker for a claim that PBL1 itself phosphorylates RBOHD at S39 or S343."]
- Consequence for modules/chitin_perception.yaml: the "BIK1/PBL1 phosphorylation of RBOHD" annoton is not directly supported for PBL1, and the only chitin-specific PBL1 data (Ranf 2014) show PBL1 is dispensable for the chitin Ca2+ response. PBL1 is better grounded on LRR-RK (FLS2/EFR/PEPR/MIK2) signalling. Not edited (module out of scope).

## Annotation decisions (summary)
- Kinase MF (IBA, IEA) accepted; generic GO:0004672 -> MODIFY to GO:0004674.
- PRR signalling IBA and response to molecule of bacterial origin IMP accepted (core).
- regulation of defense response to bacterium IMP: no bacterial infection assay for PBL1 in PMID:25522736; marked over-annotated.
- protein binding x2: over-annotated (FLS2, PEPR1), consistent with BIK1 review.
- chloroplast ISM: removed (myristoylated PM kinase, no transit peptide evidence).
- cytosol HDA: non-core (peripheral membrane protein; soluble pool plausible).
