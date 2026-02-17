# Oxidative Phosphorylation (OXPHOS) Project

## Overview

Oxidative phosphorylation is the metabolic pathway by which mitochondria generate ATP through
electron transport and chemiosmotic coupling. The electron transport chain (ETC) comprises four
multi-subunit complexes (I-IV) embedded in the mitochondrial inner membrane, plus two mobile
electron carriers (ubiquinone/CoQ10 and cytochrome c). Complex V (ATP synthase) uses the
resulting proton gradient to synthesize ATP.

OXPHOS is responsible for ~90% of cellular ATP production and is unique in requiring
coordinated expression from both nuclear and mitochondrial genomes: 13 subunits are
mtDNA-encoded, while ~80 structural subunits and dozens of assembly factors are nuclear-encoded.

## Model Species

**Primary: Homo sapiens (human)**

## Annotation Review Focus

Key annotation issues in OXPHOS genes:
- Assembly factors should be annotated to assembly processes, NOT electron transport directly
- Dual-function proteins (e.g., SDHA in both TCA cycle and ETC) need both roles annotated
- Tissue-specific isoforms may warrant distinct annotations
- Supercomplex/respirasome assembly is a distinct process from individual complex assembly
- SDH subunit tumor suppressor roles (oncometabolite mechanism) vs. metabolic function
- Avoid generic "protein binding" for assembly factor interactions

## Complex I -- NADH:ubiquinone oxidoreductase

The largest ETC complex (~1 MDa, 44 subunits). 7 mtDNA-encoded + 37 nuclear-encoded.
Transfers electrons from NADH to ubiquinone, pumping 4 H+ per NADH.

### Core catalytic subunits (Priority 1)
| Gene | UniProt | Function | Notes |
|------|---------|----------|-------|
| NDUFS1 | Q16795 | 75 kDa Fe-S protein, electron transfer | N-module |
| NDUFV1 | P49821 | 51 kDa, FMN/NADH binding | N-module, primary electron acceptor |
| NDUFS2 | O75306 | 49 kDa, ubiquinone binding | Q-module |
| NDUFS7 | O75251 | PSST, Fe-S cluster | Q-module |
| NDUFS8 | O00217 | TYKY, 2x [4Fe-4S] | Q-module |
| NDUFV2 | P19404 | 24 kDa, [2Fe-2S] | N-module |
| NDUFS3 | O75489 | 30 kDa | Q-module |

### Key accessory subunits (Priority 2)
| Gene | UniProt | Function | Notes |
|------|---------|----------|-------|
| NDUFS4 | O43181 | 18 kDa, regulatory | Leigh syndrome gene |
| NDUFA9 | Q16795 | 39 kDa | Accessory |
| NDUFA13 | Q9P0J0 | GRIM-19 | Cell death-related |

### Key assembly factors (Priority 2)
| Gene | UniProt | Function | Notes |
|------|---------|----------|-------|
| ACAD9 | Q9H845 | MCIA complex | Assembly factor with acyl-CoA dehydrogenase fold |
| NDUFAF2 | Q8N183 | N-module assembly | Disease gene |
| TMEM126B | Q8IUX1 | MCIA complex | Assembly factor |
| NUBPL | Q8TB37 | Fe-S cluster transfer | Assembly factor |

## Complex II -- Succinate dehydrogenase

Only entirely nuclear-encoded ETC complex. Participates in both TCA cycle and ETC.
Does NOT pump protons. Tumor suppressor role via oncometabolite mechanism.

### All subunits (Priority 1)
| Gene | UniProt | Function | Notes |
|------|---------|----------|-------|
| SDHA | P31040 | Flavoprotein, FAD, succinate binding | Dual TCA/ETC role |
| SDHB | P21912 | Fe-S subunit, electron transfer | Tumor suppressor |
| SDHC | Q99643 | Membrane anchor, ubiquinone binding | Tumor suppressor |
| SDHD | O14521 | Membrane anchor, heme b | Tumor suppressor |

### Assembly factors (Priority 2)
| Gene | UniProt | Function | Notes |
|------|---------|----------|-------|
| SDHAF1 | Q6IAA8 | Fe-S cluster maturation of SDHB | Leukoencephalopathy |
| SDHAF2 | Q9NX18 | FAD insertion into SDHA | Paraganglioma |
| SDHAF3 | Q9NRP4 | Protects SDHB Fe-S from ROS | |
| SDHAF4 | Q5VUM1 | Chaperone for SDHA | |

## Complex III -- Cytochrome bc1

Homodimer (III2), 11 subunits per monomer. Transfers electrons from ubiquinol to
cytochrome c via Q-cycle, pumping 4 H+ per QH2.

### Core catalytic subunits (Priority 1)
| Gene | UniProt | Function | Notes |
|------|---------|----------|-------|
| CYC1 | P08574 | Cytochrome c1, heme c1 | **Already reviewed** |
| UQCRFS1 | P47985 | Rieske Fe-S protein | Core catalytic |
| UQCRC1 | P31930 | Core protein 1 | Structural |
| UQCRC2 | P22695 | Core protein 2 | Structural |

### Key assembly factors (Priority 2)
| Gene | UniProt | Function | Notes |
|------|---------|----------|-------|
| BCS1L | Q9Y276 | Rieske protein insertion | GRACILE syndrome |
| LYRM7 | Q5T7U8 | Rieske protein chaperone | |
| TTC19 | Q6DKK2 | UQCRFS1 fragment turnover | Neurodegeneration |

## Complex IV -- Cytochrome c oxidase

Terminal oxidase. 14 subunits. Transfers electrons from cytochrome c to O2, pumping 4 H+.

### Core subunits (Priority 1)
| Gene | UniProt | Function | Notes |
|------|---------|----------|-------|
| COX5B | P10606 | Nuclear-encoded structural | **Already reviewed** |
| COX4I1 | P13073 | Regulatory, ATP inhibition | Ubiquitous isoform |
| COX4I2 | Q96KJ9 | Regulatory | Hypoxia/lung isoform |
| COX6A1 | P12074 | Liver isoform | Tissue-specific |
| COX6B1 | P14854 | Stabilizes dimer | |
| NDUFA4 | O00483 | Confirmed CIV subunit | Reclassified from CI |

### Key assembly factors (Priority 1-2)
| Gene | UniProt | Function | Notes |
|------|---------|----------|-------|
| SURF1 | Q15526 | COX1 module assembly | Most common COX Leigh syndrome |
| SCO2 | O43819 | Copper chaperone for CuA | Cardioencephalomyopathy |
| SCO1 | O75880 | Copper chaperone for CuA | Hepatopathy |
| COX10 | Q12887 | Heme a biosynthesis | |
| COX15 | Q7KZN9 | Heme a synthase | |
| LRPPRC | P42704 | Stabilizes MT-CO1/CO3 mRNAs | **Already reviewed** |

## Complex V -- ATP synthase

Rotary motor enzyme. Uses proton gradient to synthesize ATP (~4 H+/ATP).
F1 (catalytic) + Fo (proton channel) + central/peripheral stalks.

### Core subunits (Priority 1)
| Gene | UniProt | Function | Notes |
|------|---------|----------|-------|
| ATP5F1A | P25705 | F1 alpha, regulatory | |
| ATP5F1B | P06576 | F1 beta, catalytic | ATP synthesis |
| ATP5F1C | P36542 | Gamma, central stalk rotor | |
| ATP5PO | P48047 | OSCP, stator/F1 connection | |
| ATP5MC1 | P05496 | c-ring subunit | **Already reviewed** |
| ATP5MC2 | Q06055 | c-ring isoform 2 | **Already reviewed** |
| ATP5MC3 | P48201 | c-ring isoform 3 | **Already reviewed** |
| ATP5IF1 | Q9UII2 | IF1, inhibitory factor | Prevents ATP hydrolysis |

### Key assembly factors (Priority 2)
| Gene | UniProt | Function | Notes |
|------|---------|----------|-------|
| TMEM70 | Q9BUB7 | c-ring/Fo assembly | **Already reviewed**, most common nuclear CV deficiency |
| ATPAF1 | Q5TC12 | alpha/beta hexamer assembly | |
| ATPAF2 | Q8N5M1 | alpha/beta hexamer assembly | |

## Mobile Electron Carriers and Accessory Proteins

### Cytochrome c (Priority 1)
| Gene | UniProt | Function | Notes |
|------|---------|----------|-------|
| CYCS | P99999 | Electron carrier III->IV | Also apoptosis role |
| HCCS | P53701 | Heme attachment to CYCS | |

### CoQ10 Biosynthesis (Priority 2-3)
| Gene | UniProt | Function | Notes |
|------|---------|----------|-------|
| COQ2 | Q96H96 | Ring-tail conjugation | Primary CoQ deficiency |
| COQ7 | Q99807 | Hydroxylase | |
| COQ8A | Q8NI60 | Regulatory kinase | Cerebellar ataxia |
| COQ8B | Q96D53 | Regulatory kinase | Nephropathy |

### ETF system (Priority 3)
| Gene | UniProt | Function | Notes |
|------|---------|----------|-------|
| ETFDH | Q16134 | ETF:ubiquinone oxidoreductase | Multiple acyl-CoA dehydrogenase deficiency |

### Supercomplex (Priority 3)
| Gene | UniProt | Function | Notes |
|------|---------|----------|-------|
| COX7A2L | O14548 | Respirasome assembly (SCAF1) | Controversial |

## Disease Context

- **Leigh syndrome**: >100 genes; NDUFS4, SURF1, MT-ATP6 most common
- **LHON**: MT-ND4, MT-ND1, MT-ND6 (Complex I, mtDNA)
- **MELAS/MERRF**: tRNA mutations affecting multiple complexes
- **Paraganglioma/pheochromocytoma**: SDHA/B/C/D, SDHAF2 (tumor suppressors)
- **CoQ10 deficiency**: COQ2-9, PDSS1/2
- **GRACILE syndrome**: BCS1L (Complex III)
- **Barth syndrome**: TAZ (cardiolipin, indirect)

## Priority Gene List for Review

Focus on nuclear-encoded genes with rich GO annotation to review.
mtDNA-encoded genes have limited GO annotations and are lower priority.

**Tier 1 (High Priority)** -- Core catalytic, disease-relevant, annotation-rich:
1. SDHA -- dual TCA/ETC function, tumor suppressor
2. SDHB -- tumor suppressor, Fe-S subunit
3. CYCS -- dual ETC/apoptosis function
4. NDUFS1 -- largest CI subunit, Fe-S chain
5. NDUFV1 -- NADH binding, primary electron entry
6. UQCRFS1 -- Rieske protein, catalytic
7. ATP5F1B -- catalytic beta subunit
8. SURF1 -- most common COX assembly defect
9. ATP5IF1 -- regulatory inhibitor

**Tier 2 (Medium Priority)** -- Important structural/assembly:
10. NDUFS2 -- ubiquinone binding
11. NDUFS4 -- Leigh syndrome, regulatory
12. SDHC -- membrane anchor, tumor suppressor
13. SDHD -- membrane anchor, tumor suppressor
14. UQCRC1 -- Complex III core protein
15. COX4I1 -- regulatory subunit
16. NDUFA4 -- reclassified CI->CIV
17. BCS1L -- GRACILE syndrome
18. SCO2 -- copper delivery
19. ACAD9 -- dual function (CI assembly + FAD)
20. ATP5F1A -- F1 alpha subunit

**Tier 3 (Lower Priority)** -- Specialized/accessory:
21. SDHAF2 -- paraganglioma
22. COQ8A -- cerebellar ataxia
23. ETFDH -- FAO electron entry to ETC
24. COX7A2L -- supercomplex assembly (controversial)
25. HCCS -- heme maturation

---
# STATUS

- [x] CYC1 -- already reviewed
- [x] COX5B -- already reviewed
- [x] ATP5MC1 -- already reviewed
- [x] ATP5MC2 -- already reviewed
- [x] ATP5MC3 -- already reviewed
- [x] TMEM70 -- already reviewed
- [x] LRPPRC -- already reviewed
- [x] SDHA -- reviewed 2026-02-11 (56 annotations, core_functions with contributes_to)
- [x] SDHB -- reviewed 2026-02-11 (49 annotations, tumor suppressor role documented)
- [x] CYCS -- reviewed 2026-02-11 (53 annotations, dual ETC/apoptosis core_functions)
- [x] NDUFS1 -- reviewed 2026-02-11 (57 annotations, Fe-S electron relay, contributes_to CI activity)
- [x] NDUFV1 -- reviewed 2026-02-11 (44 annotations + 2 NEW, FMN catalytic subunit, NADH dehydrogenase activity)
- [x] UQCRFS1 -- reviewed 2026-02-11 (31 annotations + 1 NEW, Rieske Fe-S electron transfer, contributes_to CIII activity)
- [x] ATP5F1B -- reviewed 2026-02-11 (89 annotations, catalytic beta subunit, ecto-ATP synthase as non-core)
- [x] SURF1 -- reviewed 2026-02-11 (19 annotations + 1 NEW, CIV assembly factor, root MF)
- [x] ATP5IF1 -- reviewed 2026-02-11 (49 annotations + 1 NEW, ATPase inhibitor activity, pH-dependent)
- [ ] NDUFS2
- [ ] NDUFS4
- [ ] SDHC
- [ ] SDHD
- [ ] UQCRC1
- [ ] COX4I1
- [ ] NDUFA4
- [ ] BCS1L
- [ ] SCO2
- [ ] ACAD9
- [ ] ATP5F1A
- [ ] SDHAF2
- [ ] COQ8A
- [ ] ETFDH
- [ ] COX7A2L
- [ ] HCCS

# NOTES

## 2026-02-11

Completed first 3 Tier 1 reviews (SDHA, SDHB, CYCS). Key findings:
- SDHA: catalytic flavoprotein with contributes_to SDH quinone activity. First gene to use
  new contributes_to_molecular_function schema field for complex subunit pattern.
- SDHB: iron-sulfur relay subunit, tumor suppressor via oncometabolite mechanism documented.
- CYCS: dual-function gene with 2 core_functions entries (ETC electron carrier + apoptosis).
  Added NEW GO:0043293 (apoptosome). Corrected GO:0097194->GO:0097193 (intrinsic signaling,
  not execution phase).

Fetched and prepared remaining Tier 1 genes (NDUFS1, NDUFV1, UQCRFS1, ATP5F1B, SURF1, ATP5IF1).
Deep research completed for all 6. NDUFS1 and NDUFV1 annotation reviews completed.

NDUFS1 (57 ann): 75 kDa Fe-S subunit, largest CI subunit. N-module, electron relay via 3 Fe-S
clusters. enables GO:0009055 (electron transfer), contributes_to GO:0008137 (CI activity).
Caspase cleavage role (PMID:15186778) documented as non-core. MDM2 interaction (PMID:30879903).

NDUFV1 (44 ann + 2 NEW): 51 kDa FMN catalytic subunit, primary NADH acceptor. N-module tip.
NEW GO:0003954 (NADH dehydrogenase activity, enables) -- subunit-specific MF analogous to SDHA
pattern. NEW GO:0009055 (electron transfer activity). contributes_to GO:0008137 (CI activity).
Cdk1 phosphorylation for G2/M cell cycle (PMID:24746669) documented.

Completed remaining 4 Tier 1 reviews (UQCRFS1, ATP5F1B, SURF1, ATP5IF1). All Tier 1 done.

UQCRFS1 (31 ann + 1 NEW): Rieske iron-sulfur protein, Complex III catalytic subunit. [2Fe-2S]
electron transfer from QH2 to cytochrome c1. NEW GO:0009055 (electron transfer activity).
contributes_to GO:0008121 (quinol-cytochrome-c reductase activity). Assembly pathway via
LYRM7/HSC20/HSPA9/BCS1L documented. Complex III assembly (GO:0034551) kept as non-core.

ATP5F1B (89 ann): F1 catalytic beta subunit, largest review in project. contributes_to
GO:0046933 (proton-transporting ATP synthase, rotational). Extensive ecto-ATP synthase
annotations (angiogenesis, MHC class I binding, cell surface) all KEEP_AS_NON_CORE.
Multiple protein binding annotations over-annotated.

SURF1 (19 ann + 1 NEW): Complex IV assembly factor, most common COX-related Leigh syndrome.
NEW GO:0062011 (CIV pre-assembly complex). Assembly factor pattern: root MF (GO:0003674)
since molecular function not fully characterized. Removed incorrect cytochrome-c oxidase
activity and proton transport annotations.

ATP5IF1 (49 ann + 1 NEW): IF1 inhibitory factor, prevents futile ATP hydrolysis. Core MF
GO:0042030 (ATPase inhibitor activity). NEW GO:0005759 (mitochondrial matrix). pH-dependent
dimerization mechanism. 8 MODIFY actions improving term specificity. Heme biosynthesis role
(PMID:23135403) documented as non-core.

## 2026-02-10

Project created. OXPHOS gene annotation review covering all five respiratory chain complexes
plus mobile electron carriers and assembly factors. 7 genes already reviewed from prior
projects (ATP5MC1/2/3, CYC1, COX5B, TMEM70, LRPPRC). 25 new genes prioritized across
three tiers. Complex II (SDH) genes are particularly interesting due to dual TCA/ETC
function and tumor suppressor roles.
