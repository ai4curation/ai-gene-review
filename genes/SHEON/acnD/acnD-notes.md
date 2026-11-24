# acnD (Q8EJW3, SO_0343) - Shewanella oneidensis MR-1

## 2026-10-23 - Initial review

### Setup / provenance
- Files fetched with `just fetch-gene SHEON acnD`.
- Provider deep research could not be run in this session because provider API
  credentials were unavailable. No `-deep-research-*.md` file was created. The review
  rests on the cached full-text papers PMID:14702315 (PMC305763) and PMID:29145506
  (PMC5690661), plus the reviewed UniProt entry. PMID:29145506 is not cited in GOA
  for AcnD but was already cached (from the prpF review).
- Comparators: genes/SHEON/prpF (partner isomerase), genes/PSEPK/acnA-II (KT2440 AcnD).

### Evidence from the S. oneidensis protein
- AcnD + PrpF, but neither alone, complement an S. enterica prpD mutant on propionate
  [PMID:14702315 "These results indicate that both acnD and prpF are required to complement a prpD strain of S. enterica ."].
- Substrates: citrate, cis-aconitate, 2-MC; not 2-MIC or isocitrate (dehydration half only)
  [PMID:14702315 "AcnD used citrate, cis -aconitate, and 2-MC as substrates but not 2-MIC or isocitrate, indicating that, like PrpD ( 17 ), AcnD only catalyzes the first half of the aconitase-like reaction."].
- 2-MC activity ~2.5x citrate [PMID:14702315 "The specific activity of AcnD for 2-MC was approximately 2.5-fold higher than that for citrate."].
- Fe/S-dependent [PMID:14702315 "AcnD activity was only observed after anoxic reactivation with iron, sulfide, and reductant."];
  conserves the three cluster-ligating Cys of mitochondrial aconitase
  [PMID:14702315 "including the three cysteine residues that coordinate the 4Fe/4S cluster of mAcn"].
- Cannot replace aconitase in the TCA cycle
  [PMID:14702315 "Hence, it was concluded that the acnD and prpF genes cannot compensate for the lack of aconitase activity required for a functional TCA cycle of S. enterica , at least not to the level required for growth on pyruvate."].

### Product identity (disputed)
- 2004: 13C-NMR peak of the AcnD product matched the PrpD product (2-methyl-cis-aconitate)
  [PMID:14702315 "The peaks observed with the H 6 PrpD-catalyzed reaction matched exactly the shifts of those seen with the AcnD reaction."].
- 2017: HPLC shows different products; aconitases do not use the AcnD product; PrpF
  converts it to 2-methyl-cis-aconitate
  [PMID:29145506 "The different retention times and chromatographic behavior indicated to us that the dehydration product of SePrpD and SoAcnD were different compounds"]
  [PMID:29145506 "Neither SeAcnA nor SeAcnB used the SoAcnD reaction product as substrate"]
  [PMID:29145506 "it is likely that 4-methylaconitate is the product of the AcnD enzyme"].
- UniProt/Rhea record the product as 2-methyl-trans-aconitate (EC 4.2.1.117, RHEA:26522),
  which neither paper determines structurally.

### GO term choice for the MF
- GO:0047547 2-methylcitrate dehydratase activity (checked in OLS) is defined as
  "(2S,3S)-2-methylcitrate = cis-2-methylaconitate + H2O" (EC 4.2.1.79, RHEA:17725), the
  PrpD reaction, so it does not fit AcnD. The citrate/isocitrate sub-reaction terms
  (GO:0052632, GO:0052633) are obsolete. Used GO:0016836 hydro-lyase activity (existing
  IDA) as the honest parent, with a proposed new term "AcnD-type 2-methylcitrate
  dehydratase activity" (same name as the PSEPK acnA-II proposal).

### Decisions
- GO:0003994 aconitate hydratase (EXP, IBA, IEA): MODIFY -> GO:0016836 (isocitrate not a
  substrate; contradicted by the cited full text). Source defect recorded against UniProt
  (EXP row and EC 4.2.1.3 citrate = D-threo-isocitrate catalytic-activity line).
- GO:0016836 hydro-lyase (IDA): ACCEPT, core MF.
- GO:0019543 propionate catabolic process (IDA, IEA): ACCEPT.
- GO:0051539 4Fe-4S binding (IBA): KEEP_AS_NON_CORE (cofactor).
- GO:0005829 cytosol (IBA): ACCEPT (soluble enzyme; no experimental localization).
- GO:0006099 TCA cycle (IBA): REMOVE (target-specific divergence; fails acnA acnB complementation).
- GO:0030350 IRE binding (IBA): REMOVE (IRP-branch function over-propagated from family root).
- No NEW annotations.
