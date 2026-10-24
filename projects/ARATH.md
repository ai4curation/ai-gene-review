---
title: Arabidopsis thaliana corpus
maturity: SCOPING
tags:
- BIOLOGY_DOMAIN
- FLAGSHIP
species:
- ARATH
genes:
- ABCB19
- ABCG36
- ABI1
- ABI5
- AFB2
- AG
- AGO1
- AHK2
- AHK3
- AHK4
- AHP1
- AOP2
- AP1
- AP2
- AP3
- APO1
- ARF19
- ARF5
- ARF7
- ARR1
- ARR12
- ARR5
- AT1G06680
- AT1G32330
- AT1G74310
- AT2G26150
- AT3G02990
- AT4G17750
- AT4G38370
- AT5G02500
- AT5G03720
- AT5G16820
- AT5G52640
- AUX1
- At1g67980
- BAK1
- BAM1
- BCAT3
- BCAT4
- BES1
- BGLU26
- BIK1
- BIN2
- BKI1
- BRC1
- BRI1
- BSK1
- BSU1
- BUB3.1
- BZR1
- CAL
- CASPL1B1
- CASPL1B2
- CASPL1D1
- CASPL1D2
- CASPL4C1
- CBF1
- CBL10
- CBL4
- CCA1
- CDF1
- CER1
- CERK1
- CHL1
- CIPK24
- CLF
- CLV1
- CLV2
- CLV3
- CO
- COI1
- COP1
- CPC
- CRN
- CRTISO
- CRY1
- CRY2
- CTR1
- CUT1
- CYCD6-1
- CYP71A12
- CYP71A13
- CYP71B15
- CYP79B2
- CYP79B3
- CYP79F1
- CYP79F2
- CYP83A1
- D14
- D6PK
- DCL1
- DGAT1
- DRB1
- DREB2A
- DRS1
- EBF1
- EBF2
- ECR
- EDS1
- EFR
- EGL3
- EIL1
- EIN2
- EIN3
- ELF3
- ELF4
- EPF2
- ERECTA
- ERF094
- ERS1
- ESP
- ETR1
- F4JLB7
- FAD2
- FAE1
- FAMA
- FBL22
- FCA
- FD
- FER
- FIE
- FKF1
- FLC
- FLD
- FLS2
- FMOGS-OX1
- FPA
- FRI
- FRK1
- FT
- FTSH12
- FUL
- FVE
- FY
- GA1
- GA2
- GA20OX1
- GA3
- GA3OX1
- GAI
- GGP1
- GI
- GID1A
- GID1B
- GID1C
- GIP1
- GL1
- GL2
- GL3
- GSTF11
- GSTF6
- GSTU20
- HEN1
- HKT1
- HSP17.6A
- HSP17.7
- HY5
- IAA12
- IAA17
- ICE1
- ICS1
- IIL1
- IMDH1
- JAR1
- JAZ1
- JKD
- KAO1
- KAO2
- KCR1
- LCR1
- LCYB
- LCYE
- LD
- LFY
- LHP1
- LHY
- LUX
- LYK4
- LYK5
- LYM2
- MAM1
- MAM3
- MAPKKK5
- MAX2
- MGP
- MKK4
- MKK5
- MLO2
- MPK3
- MPK6
- MSI1
- MUTE
- MYB122
- MYB34
- MYB51
- MYC2
- MYC3
- NCED3
- NEK3
- NINJA
- NPR1
- NSP1
- OST1
- PAD4
- PAL1
- PAS2
- PBL1
- PBL27
- PDS
- PHYA
- PHYB
- PI
- PID
- PIF1
- PIF3
- PIF4
- PIN1
- PIN2
- PRR5
- PRR7
- PRR9
- PSY
- PYR1
- Q1G3K8
- RBOHD
- RCA
- RDR6
- RGA
- RPM1
- RPS2
- SCR
- SEP1
- SEP2
- SEP3
- SEP4
- SERRATE
- SHR
- SIZ1
- SLAC1
- SLY1
- SMXL6
- SMXL7
- SMXL8
- SnRK2.2
- SnRK2.3
- SOC1
- SOS1
- SOT17
- SOT18
- SPA1
- SPC24
- SPCH
- SSU3
- STM
- SUN1
- SUN2
- SUR1
- SVP
- SWN
- SYP121
- TFL1
- TGG1
- TGG2
- TIR1
- TMM
- TOC1
- TPL
- TRY
- TT8
- TTG1
- UFO
- UGT74C1
- UVR8
- VAL1
- VIN3
- VRN1
- VRN2
- VRN5
- WIP1
- WOX5
- WRI1
- WRKY33
- WRKY70
- WUS
- YDA
- Z-ISO
- ZDS
- ZTL
---

# Arabidopsis thaliana corpus

**Bottom line:** the repository holds 282 *Arabidopsis thaliana* gene reviews
covering 8,746 annotation rows, but they were built by many separate projects
and nobody has yet looked at them as one body of work. This project does that.
It summarizes the corpus several ways (by action, by evidence type, by term,
by module, by family, by GO-CAM) and then uses those views to pick follow-up
curation. Excluding `protein binding`, the reviews accept 56% of rows, keep 26%
as non-core, modify 8%, mark 4% over-annotated and remove only 3%, and they add
185 `NEW` rows. `protein binding` alone is 1,954 rows, 22% of the corpus, and
accounts for 83% of all removals. The main gaps are bookkeeping and coverage,
not biology: 22 reviews are fully actioned but still say `INITIALIZED`, 7 have
no status at all, 58 rows in 23 genes are `UNDECIDED`, 71 reviews belong to no
module, only 9 PANTHER family reviews touch an Arabidopsis gene, and the GO-CAM
index has one Arabidopsis model, none of whose genes we have reviewed.

All numbers on this page come from
[`ARATH/scripts/arath_corpus_stats.py`](ARATH/scripts/arath_corpus_stats.py),
which writes [`ARATH/ARATH-corpus-stats.yaml`](ARATH/ARATH-corpus-stats.yaml)
(per-gene rows, module and family membership, term rankings). Re-run it after
any curation round and update the numbers here; the snapshot below is from
2026-10-14.

Use UniProt code ARATH. Folders are named by gene symbol where one exists, and
otherwise by AGI locus (e.g. `AT4G17750` for HSFA1A) or UniProt accession.

## Corpus at a glance

| Measure | Count |
|---|---|
| Gene reviews (`genes/ARATH/`) | 282 |
| Annotation rows reviewed (including `NEW`) | 8,746 |
| Reviews with a deep-research file | 197 |
| Reviews with a bioinformatics folder | 4 |
| Reviews with a ProtNLM prediction review | 2 (AT4G38370, F4JLB7) |
| Modules that mention Arabidopsis or contain a reviewed ARATH gene | 40 |
| ... of which contain at least one reviewed ARATH gene | 29 |
| Reviews that belong to at least one module | 211 |
| PANTHER family reviews citing an ARATH review | 9 (10 genes) |
| Arabidopsis GO-CAMs in `gocams/index.tsv` | 1 |
| Other projects listing ARATH in `species` | 26 |

### Review status

| `status` in the review file | Reviews |
|---|---|
| COMPLETE | 184 |
| DRAFT | 68 |
| INITIALIZED | 22 |
| IN_PROGRESS | 1 |
| (no status field) | 7 |

None of the 8,746 rows is still `PENDING`, so the 22 `INITIALIZED` reviews
have in fact been worked through; their status field was never updated. The 7
reviews with no status are the cytokinin two-component set.

## View 1: actions

| Action | All rows | Without `protein binding` | `protein binding` only |
|---|---|---|---|
| ACCEPT | 3,797 | 3,791 | 6 |
| KEEP_AS_NON_CORE | 1,830 | 1,752 | 78 |
| MODIFY | 1,281 | 537 | 744 |
| REMOVE | 1,043 | 180 | 863 |
| MARK_AS_OVER_ANNOTATED | 552 | 303 | 249 |
| NEW | 185 | 185 | 0 |
| UNDECIDED | 58 | 44 | 14 |
| **Total** | **8,746** | **6,792** | **1,954** |

Read the first column with care: most of its removals and modifications are the
project-wide rule that `protein binding` says nothing about function. The middle
column is the better measure of how often the reviews disagreed with GOA about
biology, and there the removal rate is under 3%.

## View 2: evidence type against action

Evidence codes are grouped as experimental (`EXP`, `IDA`, `IPI`, `IMP`, `IGI`,
`IEP` and the high-throughput codes), phylogenetic (`IBA`, `IBD`, `IKR`, `IRD`),
electronic (`IEA`), similarity (`ISS`, `ISO`, `ISA`, `ISM`, `RCA`, `IGC`) and
author/curator (`TAS`, `NAS`, `IC`, `ND`).

| Evidence class | Rows | ACCEPT | NON_CORE | MODIFY | OVER_ANN. | REMOVE | NEW | UNDECIDED |
|---|---|---|---|---|---|---|---|---|
| Experimental | 5,723 | 1,868 | 1,383 | 943 | 424 | 906 | 156 | 43 |
| Electronic | 1,558 | 946 | 275 | 216 | 69 | 45 | 2 | 5 |
| Phylogenetic | 677 | 493 | 93 | 39 | 24 | 24 | 2 | 2 |
| Similarity | 448 | 275 | 27 | 52 | 19 | 67 | 3 | 5 |
| Author/curator | 340 | 215 | 52 | 31 | 16 | 1 | 22 | 3 |

Two things stand out. Experimental rows carry most removals because IPI
`protein binding` is experimental. And phylogenetic rows (almost all IBA) are
the most often accepted class (73%), which fits the repo's position that an IBA carries a PAINT
curator's considered phylogenetic judgment. Similarity rows are removed about
as often as experimental ones (15% against 16%), but for a different reason:
ISM organelle-targeting predictions (next section).

## View 3: recurring term-level corrections

- **`protein binding` (GO:0005515):** 1,954 rows; 863 removed, 744 modified to
  a specific binding or adaptor term, 249 marked over-annotated.
- **Organelle localizations from prediction or proteomics:** 26 of 95
  `chloroplast` (GO:0009507) rows were removed. Of the chloroplast and
  `mitochondrion` (GO:0005739) rows that were removed or marked over-annotated,
  35 are ISM (targeting-peptide prediction) and 17 are HDA (organelle proteomics).
  This pattern is plant-specific and worth checking as a class (see plan).
- **Transcription-factor terms:** `DNA-binding transcription factor activity`
  (GO:0003700; 77 of 244 rows modified), `DNA binding` (52 of 101) and
  `regulation of DNA-templated transcription` (23 of 130) are routinely
  sharpened to activator, repressor or sequence-specific children.
- **Kinase terms:** `protein kinase activity` and `protein serine/threonine
  kinase activity` are modified in 8 rows each, mostly to receptor or MAPK
  kinase children.
- **Most common `NEW` terms:** transcription corepressor activity (6 rows),
  ubiquitin-like ligase-substrate adaptor activity (5), ESC/E(Z) complex (5),
  DNA-binding transcription activator activity (4), cellular response to
  strigolactone (4). Full rankings are in the stats file.

## View 4: modules

Modules are the main way the corpus is organised by pathway. 29 modules contain
at least one reviewed Arabidopsis gene:

| Module | Reviewed ARATH genes | Members |
|---|---|---|
| [Aliphatic glucosinolate biosynthesis and myrosinase activation (glucosinolate-myrosinase defense system)](../modules/aliphatic_glucosinolate_myrosinase_defense.html) | 23 | AOP2, BCAT3, BCAT4, CYP79F1, CYP79F2, CYP83A1, ESP, FMOGS-OX1, GGP1, GSTF11, GSTU20, IIL1, IMDH1, MAM1, MAM3, NSP1, SOT17, SOT18, SSU3, SUR1, TGG1, TGG2, UGT74C1 |
| [FRIGIDA-dependent FLC activation and vernalization-induced Polycomb silencing of FLC](../modules/vernalization_flc_silencing.html) | 15 | CLF, FIE, FLC, FRI, FT, LHP1, MSI1, SOC1, SVP, SWN, VAL1, VIN3, VRN1, VRN2, VRN5 |
| [Plant chitin perception by LysM receptor complexes](../modules/chitin_perception.html) | 12 | BIK1, CERK1, LYK4, LYK5, MAPKKK5, MKK4, MKK5, MPK3, MPK6, PBL1, PBL27, RBOHD |
| [Photoperiodic (long-day) flowering via the CONSTANS-FLOWERING LOCUS T pathway (Arabidopsis)](../modules/photoperiodic_flowering_co_ft.html) | 12 | CDF1, CO, COP1, CRY2, FD, FKF1, FT, GI, PHYA, SOC1, SPA1, ZTL |
| [Stomatal lineage progression and spacing (EPF-ERECTA-YODA-MAPK and SPCH/MUTE/FAMA-SCRM)](../modules/stomatal_lineage_development.html) | 12 | EPF2, ERECTA, FAMA, ICE1, MKK4, MKK5, MPK3, MPK6, MUTE, SPCH, TMM, YDA |
| [Arabidopsis core circadian oscillator (CCA1/LHY - PRR - evening complex - ZTL)](../modules/plant_circadian_clock_oscillator.html) | 11 | CCA1, ELF3, ELF4, GI, LHY, LUX, PRR5, PRR7, PRR9, TOC1, ZTL |
| [Camalexin biosynthesis (tryptophan-derived indole phytoalexin)](../modules/camalexin_biosynthesis.html) | 10 | CYP71A12, CYP71A13, CYP71B15, CYP79B2, CYP79B3, GGP1, GSTF6, MPK3, MPK6, WRKY33 |
| [Specification of floral meristem identity at the Arabidopsis shoot apex](../modules/floral_meristem_identity.html) | 10 | AP1, AP2, CAL, FD, FT, FUL, LFY, SOC1, TFL1, UFO |
| [Autonomous flowering pathway repressing FLOWERING LOCUS C (Arabidopsis)](../modules/autonomous_flowering_pathway.html) | 9 | FCA, FLC, FLD, FPA, FT, FVE, FY, LD, SOC1 |
| [ABCE model of floral organ identity (MADS floral quartets)](../modules/floral_organ_identity_abce.html) | 9 | AG, AP1, AP2, AP3, PI, SEP1, SEP2, SEP3, SEP4 |
| [Phytochrome control of photomorphogenesis (phyA/phyB - PIF - COP1/SPA - HY5)](../modules/phytochrome_photomorphogenesis.html) | 9 | COP1, CRY1, HY5, PHYA, PHYB, PIF1, PIF3, PIF4, SPA1 |
| [Nuclear auxin signaling (TIR1/AFB-Aux/IAA-TOPLESS-ARF module)](../modules/auxin_nuclear_signaling.html) | 8 | AFB2, ARF19, ARF5, ARF7, IAA12, IAA17, TIR1, TPL |
| [Brassinosteroid signal perception and relay to BZR1/BES1 transcription factors](../modules/brassinosteroid_signaling.html) | 8 | BAK1, BES1, BIN2, BKI1, BRI1, BSK1, BSU1, BZR1 |
| [Ethylene signaling (ETR/ERS receptor-CTR1-EIN2-EBF-EIN3/EIL1 module)](../modules/ethylene_signaling.html) | 8 | CTR1, EBF1, EBF2, EIL1, EIN2, EIN3, ERS1, ETR1 |
| [Gibberellin perception and DELLA derepression (GID1-DELLA-SCF(SLY1) module)](../modules/gibberellin_della_signaling.html) | 8 | GAI, GID1A, GID1B, GID1C, PIF3, PIF4, RGA, SLY1 |
| [Carotenoid biosynthesis I — carotene backbone (GGPP -> phytoene -> lycopene -> cyclic carotenes)](../modules/carotene_backbone_biosynthesis.html) | 7 | CRTISO, LCYB, LCYE, PDS, PSY, Z-ISO, ZDS |
| [Cytokinin two-component (His-Asp phosphorelay) signaling in Arabidopsis](../modules/cytokinin_two_component_signaling.html) | 7 | AHK2, AHK3, AHK4, AHP1, ARR1, ARR12, ARR5 |
| [Bioactive gibberellin (GA4/GA1) biosynthesis from geranylgeranyl diphosphate](../modules/gibberellin_biosynthesis.html) | 7 | GA1, GA2, GA20OX1, GA3, GA3OX1, KAO1, KAO2 |
| [Jasmonate perception and JAZ derepression (JAR1-COI1-JAZ-NINJA/TPL-MYC module)](../modules/jasmonate_coi1_jaz_signaling.html) | 7 | COI1, JAR1, JAZ1, MYC2, MYC3, NINJA, TPL |
| [CLAVATA-WUSCHEL negative feedback loop in shoot apical meristem stem-cell homeostasis](../modules/shoot_meristem_clv_wus_feedback.html) | 7 | BAM1, CLV1, CLV2, CLV3, CRN, STM, WUS |
| [Leaf trichome initiation and patterning by the MYB-bHLH-WD40 activator complex and R3 MYB lateral inhibitors](../modules/trichome_initiation_mbw.html) | 7 | CPC, EGL3, GL1, GL2, GL3, TRY, TTG1 |
| [Polar (cell-to-cell) auxin transport](../modules/auxin_polar_transport.html) | 6 | ABCB19, AUX1, D6PK, PID, PIN1, PIN2 |
| [Root ground-tissue radial patterning by the SHORT-ROOT-SCARECROW-BIRD module](../modules/root_radial_patterning_shr_scr.html) | 6 | CYCD6-1, JKD, MGP, SCR, SHR, WOX5 |
| [Strigolactone perception and D14-MAX2-SMXL signalling in shoot-branching control](../modules/strigolactone_signaling_shoot_branching.html) | 6 | BRC1, D14, MAX2, SMXL6, SMXL7, SMXL8 |
| [Microsomal fatty-acid elongation cycle (ELOVL or KCS -> KAR -> HACD -> ECR)](../modules/fatty_acid_elongation_cycle.html) | 5 | CUT1, ECR, FAE1, KCR1, PAS2 |
| [LINC complex (SUN-KASH nuclear envelope bridge) module](../modules/linc_complex.html) | 3 | SUN1, SUN2, WIP1 |
| [Plant NLR resistosome activation and signalling](../modules/plant_nlr_resistosome_signaling.html) | 2 | EDS1, PAD4 |
| [Plant lignin (monolignol) biosynthesis module](../modules/lignin_monolignol_biosynthesis.html) | 1 | PAL1 |
| [Plant seed triacylglycerol (oil) biosynthesis module](../modules/seed_triacylglycerol_biosynthesis.html) | 1 | DGAT1 |

11 further modules mention Arabidopsis but contain no gene we have reviewed.
Most are cross-kingdom metabolic modules where Arabidopsis is one of several
representative organisms:

- [Plant cellulose biosynthesis module](../modules/cellulose_biosynthesis.html)
- [Endoplasmic reticulum unfolded protein response](../modules/er_unfolded_protein_response.html)
- [Eukaryotic (THI4/THI5-type) de novo thiamine diphosphate biosynthesis](../modules/eukaryotic_thiamine_biosynthesis.html)
- [Folate one-carbon carrier-state interconversion](../modules/folate_one_carbon_interconversion.html)
- [L-methionine biosynthesis (from homoserine)](../modules/methionine_biosynthesis.html)
- [Oxygenic photosynthesis module](../modules/photosynthesis.html)
- [Pyrenoid-based CO2-concentrating mechanism](../modules/pyrenoid_ccm.html)
- [Siroheme biosynthesis from uroporphyrinogen III](../modules/siroheme_biosynthesis.html)
- [De novo tetrahydrofolate and folylpolyglutamate biosynthesis](../modules/tetrahydrofolate_biosynthesis.html)
- [Glycerolipid / triacylglycerol biosynthesis (glycerol-3-phosphate and DHAP routes)](../modules/triacylglycerol_biosynthesis.html)
- [Plant xylan (glucuronoxylan) biosynthesis module](../modules/xylan_biosynthesis.html)

71 reviews belong to no module: ABCG36, ABI1, ABI5, AGO1, APO1, AT1G06680, AT1G32330, AT1G74310, AT2G26150, AT3G02990, AT4G17750, AT4G38370, AT5G02500, AT5G03720, AT5G16820, AT5G52640, At1g67980, BGLU26, BUB3.1, CASPL1B1, CASPL1B2, CASPL1D1, CASPL1D2, CASPL4C1, CBF1, CER1, CHL1, CIPK24, DCL1, DRB1, DREB2A, DRS1, EFR, ERF094, F4JLB7, FAD2, FBL22, FER, FLS2, FRK1, FTSH12, GIP1, HEN1, HKT1, HSP17.6A, HSP17.7, ICS1, LCR1, LYM2, MLO2, MYB122, MYB34, MYB51, NCED3, NEK3, NPR1, OST1, PYR1, Q1G3K8, RCA, RDR6, RPM1, RPS2, SIZ1, SOS1, SPC24, SYP121, TT8, UVR8, WRI1, WRKY70.

Several of these fall into obvious groups that have no module yet: ABA
perception and signaling (PYR1, ABI1, OST1, ABI5, NCED3), small-RNA biogenesis
and silencing (DCL1, DRB1, HEN1, AGO1, RDR6), pattern-triggered immunity
(FLS2, EFR, FRK1, FER), salicylic acid and systemic resistance (ICS1, NPR1,
WRKY70, RPM1, RPS2), salt tolerance (SOS1, CIPK24, HKT1), indolic glucosinolate
regulation (MYB34, MYB51, MYB122) and the heat-stress set from
[ARATH_HEAT_STRESS](ARATH_HEAT_STRESS.md).

## View 5: families

| Family | PANTHER name | Coherence call | ARATH reviews |
|---|---|---|---|
| [`PANTHER:PTHR10782`](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR10782/PTHR10782-review.yaml) | ZINC FINGER MIZ DOMAIN-CONTAINING PROTEIN | MOSTLY_COHERENT | SIZ1 |
| [`PANTHER:PTHR11654`](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR11654/PTHR11654-review.yaml) | OLIGOPEPTIDE TRANSPORTER-RELATED | HETEROGENEOUS | CHL1 |
| [`PANTHER:PTHR11706`](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR11706/PTHR11706-review.yaml) | SOLUTE CARRIER PROTEIN FAMILY 11 MEMBER | HETEROGENEOUS | EIN2 |
| [`PANTHER:PTHR12911`](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR12911/PTHR12911-review.yaml) | SAD1/UNC-84-LIKE PROTEIN-RELATED | MOSTLY_COHERENT | SUN1, SUN2 |
| [`PANTHER:PTHR14773`](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR14773/PTHR14773-review.yaml) | WD REPEAT-CONTAINING PROTEIN 76 | MOSTLY_COHERENT | DRS1 |
| [`PANTHER:PTHR43655`](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR43655/PTHR43655-review.yaml) | ATP-DEPENDENT PROTEASE | HETEROGENEOUS | FTSH12 |
| [`PANTHER:PTHR44329`](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR44329/PTHR44329-review.yaml) | SERINE/THREONINE-PROTEIN KINASE TNNI3K-RELATED | HETEROGENEOUS | CTR1 |
| [`PANTHER:PTHR47821`](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR47821/PTHR47821-review.yaml) | PHOSPHOGLYCERATE MUTASE FAMILY PROTEIN | UNKNOWN | AT4G38370 |
| [`PANTHER:PTHR48004`](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR48004/PTHR48004-review.yaml) | OS01G0149700 PROTEIN | UNKNOWN | F4JLB7 |

Two of these (PTHR47821, PTHR48004) cover the ProtNLM benchmark proteins;
the rest arose from single-gene reviews. None of the large plant
transcription-factor or receptor-kinase families that dominate the corpus
(MADS-box, ARF, AUX/IAA, type-B ARR, DELLA, LRR-RLK) has a family review yet.

## View 6: GO-CAMs

`gocams/index.tsv` has one Arabidopsis model,
`67e5e74400000148` "Arabidopsis MRG domain proteins bridge two histone
modifications", with ASHH2, ASHH3, MRG2 and SCL27. None of these four has a
review here. We have not yet checked whether this reflects the number of
production Arabidopsis GO-CAMs or only what has been cached.

## Related projects

Focused Arabidopsis projects:
[ARATH_HEAT_STRESS](ARATH_HEAT_STRESS.md),
[ARATH_SINGLE_CELL_FUNGAL](ARATH_SINGLE_CELL_FUNGAL.md),
[CASPL_FAMILY](CASPL_FAMILY.md),
[PLANT_FUNGAL_INTERACTIONS](PLANT_FUNGAL_INTERACTIONS.md),
[PHOTOSYNTHESIS](PHOTOSYNTHESIS.md),
[PLANT_BIOENERGY](PLANT_BIOENERGY.md).
Another 20 cross-cutting projects (obsoletions, evaluations, evidence-code
studies) list ARATH among their species; the stats file names them all.

---
# STATUS

Last updated: 2026-10-19

## Phase 1: summarize the corpus

- [x] Reproducible corpus statistics script and YAML snapshot
- [x] Action, evidence-class, term, module, family and GO-CAM views (this page)
- [ ] Per-gene table (status, rows, actions, module) rendered as a sub-page
- [ ] Narrative synthesis by biological area (hormone signaling, flowering,
      development, immunity, specialised metabolism, abiotic stress)
- [ ] Compare against TAIR/GOA: what share of all Arabidopsis GOA rows and of
      experimentally annotated Arabidopsis genes the corpus covers

## Phase 2: consistency review of the standard annotations

- [ ] Set `status` on the 22 fully actioned `INITIALIZED` reviews after a spot
      check: AP3, AT4G17750, AT5G16820, AT5G52640, BIK1, CIPK24, CLV3, DREB2A, EFR, FER, FKF1, GAI, HKT1, LHY, MUTE, PI, PIF3, PIF4, RCA, SPCH, TOC1, UVR8
- [ ] Add `status` to the 7 reviews that lack it: AHK2, AHK3, AHK4, AHP1, ARR1, ARR12, ARR5
- [ ] Audit the 68 `DRAFT` reviews and promote the finished ones
- [ ] Resolve the 58 `UNDECIDED` rows: ABI1 (12), AT5G52640 (2), BUB3.1 (1), CASPL1D1 (5), CHL1 (1), DRB1 (3), DRS1 (3), F4JLB7 (4), FBL22 (3), FLS2 (1), FRK1 (1), FTSH12 (3), GSTF11 (1), GSTF6 (2), HEN1 (2), MKK4 (1), NPR1 (1), NSP1 (5), PAS2 (2), RCA (1), SUN2 (1), SUR1 (1), WIP1 (2)
- [ ] Check ISM/HDA chloroplast and mitochondrion calls as a class, so the same
      kind of evidence gets the same action across genes
- [ ] Check that sibling genes in the same module received consistent actions
      for shared terms (e.g. the three GID1s, the SEPALLATAs, the AHKs)
- [ ] Add deep research for the 85 reviews that have none
- [ ] File the draft reports in [upstream-reports.md](ARATH/upstream-reports.md)
      (GO-CAM HAM1/SCL27; TAIR SUR1, F4JLB7/RIC7, GSTF6) and record the tickets
- [x] Bring OST1 in line with SnRK2.2/SnRK2.3: all three now MODIFY protein
      kinase activity (GO:0004672) and kinase activity (GO:0016301) to GO:0004674
- [ ] Re-run the corpus statistics after the 2026-10-19 additions

## Phase 3: modules

- [ ] Draft modules for the unmodularized groups: ABA signaling, small-RNA
      biogenesis, pattern-triggered immunity, salicylic acid / NPR1, SOS salt
      tolerance, indolic glucosinolate regulation, heat-stress response
- [ ] Decide whether the 11 modules with no reviewed Arabidopsis gene need
      Arabidopsis reviews (cellulose, xylan and photosynthesis first)
- [ ] Move the 29 populated modules from `DRAFT` toward review

## Phase 4: families

- [ ] Family reviews for the large plant families in the corpus (MADS-box,
      ARF, AUX/IAA, type-B ARR, DELLA/GRAS, LRR-RLK), checking IBA propagation
      within each. Family ids to be looked up in `interpro/panther/`, not assumed.

## Phase 5: GO-CAMs

- [ ] Find the production Arabidopsis GO-CAMs and cache those that touch
      reviewed genes
- [ ] Review the cached MRG-domain model and decide whether its four genes
      need reviews

---
# NOTES

## 2026-10-14

Project created. Wrote the stats script and took the first snapshot. Counted
rows include `NEW` rows, since those live in `existing_annotations`. Module
membership is found by matching module UniProt accessions to review ids, plus
explicit `genes/ARATH/<GENE>/` paths; family membership by `genes/ARATH/` paths
in PANTHER family reviews.

## 2026-10-19

Followed up the handoff from the previous session.

- New reviews: CBL4 (SOS3), CBL10 (SCaBP8), SLAC1, SnRK2.2 (SRK2D), SnRK2.3
  (SRK2I) and SERRATE (SE). No deep-research provider worked in this session
  (Edison authentication failed and the OpenAI key was rejected), so each review
  rests on hand-written notes in its `-notes.md`. None has a deep-research file.
  All validate; all are `DRAFT`.
- Paralogs were aligned on shared terms. CBL4 and CBL10 both use GO:0043539 for
  CIPK24 activation. SnRK2.2 and SnRK2.3 both MODIFY GO:0004672 to GO:0004674
  and GO:0010029 to GO:0010187.
- GAI, RGA and GID1A: GOA was re-fetched, and their IBA rows (7, 7 and 4) were
  reviewed against the PTHR31636 and PTHR23024 family reviews. GID1A lost two
  ARBA rows; GO:0009939 was re-proposed as NEW because a core function cites it.
- AGO1: the RNA endonuclease activity IDA row is now MODIFY to GO:0090624.
- GID1A notes: the source status in the GID1B cross-reference now refers to
  PTN009058710, not AADAC.
- Draft upstream reports are in [upstream-reports.md](ARATH/upstream-reports.md).
  None has been filed.

## 2026-10-24

- OST1: the four general kinase MF rows now MODIFY to GO:0004674, matching SnRK2.2 and SnRK2.3.
- OpenScientist checked the two single-study potassium channel inhibitor (GO:0019870) calls.
  Neither finding has been independently replicated. For CBL10/AKT1 the in-planta data are
  overexpression-only, so AKT1 inhibition was dropped from CBL10's core functions. For
  SLAC1/KAT1, slac1 loss-of-function shows reduced rather than increased inward K+ current
  (PMID:23126621). Both keep their MODIFY to GO:0019870 with caveats. Reports are in each gene's
  `-hypotheses/` folder.

