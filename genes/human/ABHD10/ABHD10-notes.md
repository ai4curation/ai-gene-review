# Curatorial Notes for Human ABHD10 (UniProtKB:Q9NUJ1)

## Summary of Gene Product & Architecture

- **Protein**: Palmitoyl-protein thioesterase ABHD10, mitochondrial (`UniProtKB:Q9NUJ1`, sequence version 1; 306 aa precursor; HGNC `ABHD10`, `HGNC:25656`, chromosome 3q13.2 adjacent to `TAGLN3`).
- **Targeting & Maturation**: Precursor residues `1..52` form a cleavable N-terminal mitochondrial matrix-targeting transit peptide (`FT TRANSIT 1..52`), yielding the soluble ~28-kDa mature chain `53..306` (`PRO_0000280733`) with zero transmembrane segments (`PMID:25944712`, `PMID:31740833`, `PMID:41285782`). Deletion of the N-terminal transit peptide abolishes mitochondrial import in HEK293T cells and causes cytoplasmic aggregation (`PMID:41285782`).
- **Fold & Catalytic Triad**: Member of the alpha/beta-hydrolase superfamily (`PF00561`, `IPR052382`, `PANTHER:PTHR16138:SF7`). Carries a canonical charge-relay catalytic triad in `Q9NUJ1-1`: nucleophilic **Ser152** (within the `GSSLG` nucleophilic elbow), acidic **Asp249**, and general base **His279** (`PMID:22294686`, `PMID:31740833`). Active-site substitution `S152A` completely abolishes peptide and protein S-depalmitoylase activity in vitro and in live HEK293T cells (`PMID:31740833`), and Ser152 is covalently modified by fluorophosphonate probes (`FP-TAMRA`, `mitoFP`), aza-beta-lactam `ABL303` (`IC50 ~ 30 nM`), and rocaglate-derived beta-lactones (`PMID:22400490`, `PMID:24447064`, `PMID:31740833`).
- **Alternative Splice Isoforms**:
  - `Q9NUJ1-1` (canonical, 306 aa): Full-length mitochondrial precursor with intact transit peptide and catalytic triad.
  - `Q9NUJ1-2` (missing `1..157`): Lacks both the mitochondrial transit peptide and nucleophilic Ser152; catalytically inactive.
  - `Q9NUJ1-3` (divergent `193..205`, missing `206..306`): Lacks acidic Asp249 and general base His279; catalytically incomplete.

## Core Endogenous Function vs. Secondary Xenobiotic Activity

1. **Core Function — Mitochondrial Matrix Protein S-Depalmitoylase (`GO:0008474`, `EC 3.1.2.22`)**:
   - Cao et al. (`PMID:31740833`) used spatially restricted mitochondrial fluorophosphonate probes (`mitoFP`) and mitochondrial S-depalmitoylation probes (`mitoDPP-2`, `DPP-5`) to identify ABHD10 — rather than mitochondrial pools of LYPLA1/APT1 — as the resident mitochondrial S-depalmitoylase that maintains mitochondrial H2O2 buffering capacity.
   - ABHD10 specifically S-depalmitoylates **peroxiredoxin-5 (`PRDX5`)** at its nucleophilic peroxidatic active-site cysteine (**Cys100**), regenerating the free thiol required to reduce H2O2 (`PMID:31740833`). Knockdown of `ABHD10` in HEK293T or HeLa cells increases PRDX5 S-palmitoylation, elevates mitochondrial H2O2 upon oxidative stress, and sensitizes cells to H2O2- and paraquat-induced death in a PRDX5-dependent manner (`PMID:31740833`).
   - In alcoholic hepatitis and hepatotoxic injury (`PMID:37400491`), TGFbeta1/EGF-induced ELK-3 binds the `ABHD10` promoter to repress transcription, increasing inhibitory S-palmitoylation of PRDX5 Cys100 and hepatocyte oxidative stress.
   - In mammalian testis (`PMID:41285782`), ABHD10 is strongly enriched in germ-cell mitochondrial matrix and S-depalmitoylates mitochondrial sheath factors (`SPATA19`, `GK2`) and respiratory/pyruvate dehydrogenase subunits (`PDHX`, `NDUFV1`, `SDHB`).

2. **Secondary Xenobiotic Esterase Activity in Human Liver (`GO:0102390`, `EC 3.1.1.93`)**:
   - Iwamura et al. (`PMID:22294686`) purified mature 28-kDa ABHD10 from post-mortem human liver homogenate supernatant and showed that recombinant human ABHD10 hydrolyzes the carboxylic ester linkage of **mycophenolic acid acyl-glucuronide (`AcMPAG`)** (`Km = 100.7 uM`, `Vmax = 47.6 nmol/min/mg`), attenuating net `AcMPAG` accumulation during UGT2B7-mediated MPA glucuronidation.
   - Ito et al. (`PMID:25217485`) similarly demonstrated that human ABHD10 hydrolyzes **probenecid acyl-glucuronide (`PRAG`)** in human liver homogenates and suppresses net `PRAG` formation.
   - Crucially, Iwamura et al. (`PMID:22294686`) proved that ABHD10 **cannot** hydrolyze the phenolic O-glycoside **MPAG** (`"recombinant human ABHD10 could catalyze the deglucuronidation of AcMPAG, but could not catalyze the deglucuronidation of MPAG, a phenolic glucuronide of MPA"`). Acyl-glucuronides (`1-O-acyl-beta-D-glucuronides`) are **carboxylic esters**, not O-glycosyl compounds (`EC 3.1.1.93` is a carboxylic-ester hydrolase under `GO:0052689`, not a glycosidase under `GO:0004553`).

## Key Curation Decisions & Source Defects

- **`GO:0004553` (`hydrolase activity, hydrolyzing O-glycosyl compounds`) -> `REMOVE` (with `source_defects`)**:
  - Three rows (`IBA` from `PTN004490000`, `IDA` from `PMID:22294686` assigned by `BHF-UCL`, and `TAS` from `Reactome:R-HSA-5694563` assigned by `Reactome`) misclassify acyl-glucuronide carboxylic-ester cleavage as O-glycosyl bond hydrolysis (`LABEL_WITHOUT_DEFINITION` caused by "deglucuronidation" terminology, compounded in `Reactome:R-HSA-5694563` by the reaction display name `"ABHD10 hydrolyses MPAG"` when its own summary text says `"ABHD10 deglucuronidates AMPAG"`).
- **`GO:0002084` (`obsolete protein depalmitoylation`) -> `MODIFY` to `GO:0008474`**:
  - Obsoleted by GOC because protein depalmitoylation represents the molecular function `GO:0008474` (`palmitoyl-(protein) hydrolase activity`), matching GOC's `consider` target and comparator APTs (`LYPLA1`, `LYPLA2`, `PPT1`).
- **`GO:0005829` (`cytosol`, `IDA` `PMID:22294686`) -> `REMOVE`**:
  - `PMID:22294686` fractionated frozen post-mortem human liver into a 105,000 x g supernatant ("human liver cytosol") and microsomes, recovering the N-terminally processed 28-kDa mature mitochondrial form in both fractions due to mitochondrial rupture during tissue freezing/homogenization. Intact-cell fractionation, MitoCoP (`PMID:34800366`), N-terminomics (`PMID:25944712`), and immunogold EM (`PMID:41285782`) show ABHD10 is exclusively mitochondrial matrix-localized.
- **`GO:0005739` (`mitochondrion`) & `GO:0005759` (`mitochondrial matrix`) -> `ACCEPT`**:
  - Per the Root Organelle Policy, all `GO:0005739` rows (`IDA`, `HTP`, `IBA`, `IEA`) are retained as `ACCEPT` alongside `GO:0005759` (`mitochondrial matrix`).
- **`GO:0045454` (`cell redox homeostasis`) -> `NEW` (`IMP`, `PMID:31740833`)**:
  - Supplies the missing non-obsolete biological process for ABHD10's core function: direct enzymatic regeneration of active-site Cys100 on PRDX5 to buffer mitochondrial H2O2 (`PMID:31740833`, `PMID:37400491`).
- **Affinage Deep Research Evaluation (`ABHD10-deep-research-affinage.md`)**:
  - Passed trust gates (`faith_pct: 100.0`, `self_evaluation_pairwise: win`, 8 valid numeric PMIDs). Accurately synthesized both PRDX5/testis S-depalmitoylase biology and hepatic AcMPAG/PRAG esterase activity, and surfaced `PMID:37400491`, `PMID:41285782`, and `PMID:42206676`. Its `goslim_generic` mechanism profile (`GO:0140096`, `GO:0016787`, `R-HSA-1430728`) is far too coarse to import, and `PMID:42206676` (abstract-only cochlear aging study with internal title/abstract sign tension and an unverified extra-mitochondrial KCMF1 co-IP) is treated cautiously and not used for GO assertions.
