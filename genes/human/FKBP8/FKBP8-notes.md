# FKBP8 (FKBP38) research notes

UniProt: Q14318. EC 5.2.1.8. Single FKBP-type PPIase domain (120-204), three TPR repeats
(221-339), C-terminal transmembrane helix (390-410) -> tail-anchored, single-pass mitochondrial
outer-membrane protein, cytoplasmic side. 3 isoforms.

## Core biology (well-established)
- Constitutively INACTIVE PPIase that becomes active only when bound to calmodulin + Ca2+
  [uniprot "Constitutively inactive PPiase, which becomes active when bound to calmodulin and
  calcium"]. Ca2+ is a cofactor; calmodulin binding (EXP PMID:20707607, PMID:24145868; partner
  P0DP23 = calmodulin).
- Chaperone for BCL2: targets BCL2 to mitochondria, modulates its phosphorylation; BCL2/FKBP8/CaM/Ca2+
  complex interferes with BCL2 target binding; active form regulates apoptosis [uniprot "Seems to
  act as a chaperone for BCL2, targets it to the mitochondria and modulates its phosphorylation
  state... The active form of FKBP8 may therefore play a role in the regulation of apoptosis"].
  Disordered/flexible loop of BCL2 mediates the interaction [PMID:15733859 "The flexible loop of
  Bcl-2 is required for molecular interaction with... FKBP38"] -> GO:0097718 disordered domain
  specific binding (partner P10415=BCL2), GO:0001933 neg reg protein phosphorylation, GO:0032991
  complex.
- Mitophagy receptor/adapter: regulates mitophagy (IDA PMID:28381481, PMID:31908024); interacts
  with BNIP3 (Q9GZQ8) and autophagy machinery (LC3/GABARAP family: O95166/Q9H0R8/P60520/Q9BXW4/Q9H492);
  promotes protein localization to mitochondrion (GO:0070585, partner BNIP3). Ubiquitinated by PRKN
  during mitophagy -> degradation; deubiquitinated by USP30 [uniprot PTM].
- Anti-viral: inhibits influenza A virus infection [PMID:28169297]; partners include IAV PB1
  (P03431, Q5EP37) and HCV NS5A (O39474, microbial-infection subunit).
- mTOR / Hedgehog regulation: documented in literature (FKBP38 inhibits mTOR; required for
  Smoothened/Hedgehog signaling). Smoothened signaling pathway IEA:Ensembl (GO:0007224) present
  in UniProt DR but NOT in GOA terms list. Signal transduction (IEA), intracellular signal
  transduction (TAS PMID:10197430).
- Interacts with ZFYVE27 (protrudin, Q5T4F4); may negatively regulate its phosphorylation.
- Interacts with HSP90AA1/AB1 (P07900/P08238).

## Subcellular location
Mitochondrion outer membrane (single-pass, cytoplasmic side; EXP PMID:12510191, 16176796, 18385096;
IDA, HTP). ER membrane (IEA from mouse O35465). cytosol/endomembrane/membrane (IBA). membrane HDA.

## Action plan
- PPIase activity GO:0003755 (IEA only): ACCEPT but note Ca2+/CaM-dependent (constitutively inactive
  alone). Core conditional MF.
- protein folding chaperone GO:0044183 (IBA/IEA/IMP 29916806): ACCEPT — BCL2 chaperone + dynein-assembly
  chaperone relay (ZMYND10 paper) support genuine chaperone function. Core.
- protein folding GO:0006457 (IBA/IMP 29916806): KEEP_AS_NON_CORE (process).
- calmodulin binding GO:0005516 (EXP/IPI): ACCEPT core MF (activates PPIase; partner CaM).
- neg reg apoptosis GO:0043066 (IBA): KEEP_AS_NON_CORE / accept-ish (BCL2 chaperone role). Keep non-core.
- regulation of mitophagy GO:1901524 (IDA x2): ACCEPT — mitophagy receptor/adapter. Core process.
- protein localization to mitochondrion GO:0070585 (IPI BNIP3): ACCEPT (mitochondrial targeting role).
- disordered domain specific binding GO:0097718 (IPI BCL2): ACCEPT (BCL2 flexible-loop binding).
- neg reg protein phosphorylation GO:0001933 (IMP 15733859): KEEP_AS_NON_CORE (BCL2 phospho modulation).
- protein-containing complex GO:0032991 (IMP): KEEP_AS_NON_CORE.
- mitochondrion / mito membrane / mito envelope (EXP/IDA/IBA/IEA): ACCEPT primary; ER membrane IEA
  KEEP_AS_NON_CORE (mouse transfer, plausible secondary). membrane(IBA/HDA) KEEP_AS_NON_CORE.
- signal transduction / intracellular signal transduction GO:0007165/GO:0035556: KEEP_AS_NON_CORE
  (mTOR/Hedgehog/anti-viral signaling roles, generic terms).
- identical protein binding GO:0042802 (self): KEEP_AS_NON_CORE (homomultimer).
- protein binding IPI block: KEEP_AS_NON_CORE generally; MODIFY HSP90 partners to Hsp90 protein
  binding; MARK_AS_OVER_ANNOTATED the huge membrane-protein screen PMID:32296183 (~25 TM partners).
