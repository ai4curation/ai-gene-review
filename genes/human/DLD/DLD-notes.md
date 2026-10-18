# DLD (P09622) review notes

Human dihydrolipoyl dehydrogenase (DLD), the **E3** component. Shared, pleiotropic subunit.

## Verified core biology
- DLD is a FAD-dependent, NAD+-linked flavoenzyme (EC 1.8.1.4) that reoxidizes the
  dihydrolipoyl group on the lipoyl-bearing E2/H components, transferring electrons to
  NAD+ via its FAD. GO:0004148 dihydrolipoyl dehydrogenase (NADH) activity. Functions as a
  homodimer, one FAD per subunit; active site is a redox-active disulfide (Cys80-Cys85).
  [UniProt P09622 CATALYTIC ACTIVITY / COFACTOR / MISCELLANEOUS blocks]
- Shared E3 of FOUR complexes:
  - pyruvate dehydrogenase complex (PDH) — GO:0045254
  - 2-oxoglutarate (alpha-ketoglutarate) dehydrogenase complex (OGDH) — GO:0045252
  - branched-chain alpha-ketoacid dehydrogenase complex (BCKDH) — GO:0160157
  - glycine cleavage system as the L protein (GCSL / GcvL)
  - Also the 2-oxoadipate dehydrogenase complex (OADH, DHTKD1-E1) — GO:0160167
    [PMID:37701333 "including pyruvate dehydrogenase (PDH), alpha-ketoglutarate dehydrogenase
    (KGDH), branched-chain alpha-keto acid dehydrogenase (BCKDH), and 2-oxoadipate
    dehydrogenase (OADH)"; PMID:29191460 hE1a recruits hE2o and hE3 of OGDHc]
- Localization: mitochondrial matrix (main). Small nuclear fraction (~1-1.6%) as part of
  the nuclear α-KGDH complex that supplies succinyl-CoA to KAT2A for histone H3 succinylation
  [PMID:29211711].

## Moonlighting / secondary
- Cryptic serine protease activity when the homodimer is destabilized (S456-E431 dyad at
  interface); induced by disruption of the native dimer, which also inhibits the primary
  dehydrogenase activity [PMID:17404228]. Treat as non-core.
- Reported cilium/flagellum/acrosome localization by similarity (Q811C4, rodent), sperm
  capacitation/acrosome reaction — non-core, By similarity/IEA only.

## Disease
- DLD deficiency (DLDD, MIM 246900): combined deficiency of PDH + OGDH + BCKDH (and OADH).
  MSUD variant + lactic acidosis + alpha-ketoglutaric aciduria. [UniProt DISEASE; dismech
  Maple_Syrup_Urine_Disease.yaml "deficiency in the shared E3 subunit (DLD) produces..."]

## Annotation strategy
- Core MF: GO:0004148 (many EXP/IDA/IMP/IBA/TAS lines — ACCEPT).
- FAD binding GO:0050660 — ACCEPT (cofactor, direct).
- Complex membership (PDH GO:0045254, OGDH GO:0045252, BCKDH GO:0160157, OADH GO:0160167):
  all genuine, ACCEPT (or KEEP for OADH as it is a shared but less-central role).
- Processes: pyruvate decarboxylation to acetyl-CoA GO:0006086, 2-oxoglutarate
  decarboxylation to succinyl-CoA GO:0120551, branched-chain keto acid decarboxylation
  GO:0120552, TCA GO:0006099, 2-oxoglutarate metabolic GO:0006103, BCAA catabolic GO:0009083,
  L-lysine catabolic GO:0019477 — all genuine given shared E3 role. ACCEPT the specific ones;
  broad/parent ones KEEP_AS_NON_CORE.
- protein binding IPIs (GO:0005515) x9 from IntAct/interactome screens (PDHX O00330 is the
  physiological E3-binding-protein partner; HTT, ITGB1BP1, PRDX6, YWHAE, others are
  screen hits) — originally MARK_AS_OVER_ANNOTATED; re-actioned to REMOVE under the
  generic-protein-binding policy (2026-09): the PDHX contact is an assembly interaction
  captured by the PDH complex CC terms, the rest are screen hits, and none supports a more
  specific DLD MF. Removal does not mean the interactions are false.
- Localization: mitochondrion / mitochondrial matrix — ACCEPT. Nucleus/nucleoplasm — genuine
  minor pool (KEEP_AS_NON_CORE). Cilium/motile cilium/flagellum/acrosome/acrosomal
  vesicle/acrosomal matrix — By-similarity/IEA electronic; MARK_AS_OVER_ANNOTATED for human.
- oxidoreductase activity GO:0016491 (too general) — MODIFY -> GO:0004148.
  GO:0016668 (acting on sulfur group of donors, NAD(P) acceptor) — parent of GO:0004148,
  keep as accurate-but-general -> KEEP_AS_NON_CORE.

DR: falcon deep-research file did not land within the 8-minute poll window; grounded in
UniProt, cached publications, and dismech.

## Deep research (falcon) follow-up, 2026-09
The falcon file (`DLD-deep-research-falcon.md`) landed after the review was written. What it
adds, and what was done with each item:
- **Glycine cleavage system L protein.** The review described this role in prose but had no
  process annotation, and GOA has none for human or mouse DLD. Added NEW GO:0019464
  glycine decarboxylation via glycine cleavage system, because DLD catalyses the final step.
  Support: Reactome R-HSA-5694018 ["The last step in the glycine cleavage system is the
  reoxidation of the reduced lipoate (dihydrolipoyl group) attached to the H protein
  (GCSH:DHLL) catalysed by the L protein (mitochondrial dihydrolipoyl dehydrogenase, DLD)"].
  Comparator: yeast LPD1 and E. coli lpdA carry GO:0019464 in QuickGO. Added to
  core_functions.
- **Diaphorase / ROS moonlighting** (NADH oxidation with O2, Fe3+, NO or ubiquinone as
  acceptor; enhanced by dimer-interface disease variants). The deep research attributes this
  to Babady 2007 (PMID:17404228) and Vaubel 2011. The cached PMID:17404228 is abstract-only
  and its abstract does not mention diaphorase activity, so no annotation was made. Non-core
  in any case.
- **Cuproptosis.** The deep research reports DLD among the genes whose knockout blunts
  copper-induced death (Tsvetkov 2022). The cached abstract of that paper (PMID:35298263) does
  not name DLD. Even with full text this is necessity evidence: copper binds the *lipoylated*
  E2s (DLAT and others), and DLD is not lipoylated. No annotation.
- **KGDHc, BCKDHc, OADH, PDHc membership, and the E3BP tether.** Already covered by
  experimental rows (PMID:16442803, 29191460, 3593587, 15712224); nothing new.
- Disease-variant tables (G194C founder allele, dimer-interface variants) are consistent with
  the review's disease text. No GO consequence.
