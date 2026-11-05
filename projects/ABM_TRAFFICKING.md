---
title: "Agent-Based Modeling of Intracellular Trafficking"
maturity: IN_PROGRESS
tags: [PIPELINE, BIOLOGY_DOMAIN]
species: [human, mouse, DROME, SCHPO, worm]
genes: [TFRC, CLTC, AP2M1, DNM2, ATP6V1A, EHD1, TSG101, RAB7A, Rab7, CTSD, APOB, LDLR, PCSK9, LIPA, ASGR1, ASGR2, ALB, FCGRT, B2M, SNAP23, SORL1, VPS35, VPS26A, VPS29, Vps35, Vps26, Vps29, RAB9A, AP1B1, AP1G1, apl2, apb-1, dpy-23]
---

# Agent-Based Modeling of Intracellular Trafficking

Can a curated pathway module simulate **where a cohort of cargo particles goes, how competing sorting branches split flux, and where cargo accumulates when a trafficking step is perturbed** — without authoring a separate simulation script?

This project extends the [Executable Models](EXECUTABLE_MODELS.md) architecture ("the module is the model") to **Agent-Based Modeling (`model_type: AGENT_BASED`, `derivation: DERIVED_FROM_MODULE`)** for intracellular vesicle trafficking, receptor-mediated endocytosis, and therapeutic payload delivery ([Deliverome](DELIVEROME.md)).

* **[All executable models](../models/index.html)** — unified index of interactive Boolean and Agent-Based models
* **[Endosomal Trafficking, Sorting & Cytosolic Escape — interactive ABM](../models/endosomal_trafficking_abm.html)** ([module page](../modules/endosomal_trafficking_routing.html))
* **[Hepatocyte ASGR1/ASGR2 GalNAc Uptake & Endosomal Escape — interactive ABM](../models/asgr_galnac_delivery_abm.html)** ([module page](../modules/asgr_galnac_hepatocyte_delivery.html))
* **[Neonatal Fc Receptor (FCGRT/B2M) IgG & Albumin Salvage — interactive ABM](../models/fcrn_salvage_transcytosis_abm.html)** ([module page](../modules/fcrn_igg_albumin_salvage_transcytosis.html))
* **[Retromer (VPS35/VPS26A/VPS29) & SORL1 Endosome-to-TGN Retrieval — interactive ABM](../models/retromer_retrograde_sorting_abm.html)** ([module page](../modules/retromer_endosome_to_tgn_retrieval.html))
* **[LDLR Endocytosis & Cholesterol Clearance — interactive ABM](../models/ldlr_endocytosis_abm.html)** ([module page](../modules/ldl_receptor_mediated_endocytosis.html))

---

## Why trafficking needs agents rather than Boolean states

A [Boolean network](BOOLEAN_MODELS.md) represents each module activity as a binary truth value (`ON` or `OFF`). That abstraction fits catalytic signaling cascades (`erk_cascade`, `jak_stat_signaling`), where an active kinase broadcasts a signal downstream and the biological question is whether the network settles into a fixed point or a limit cycle.

Intracellular trafficking poses a fundamentally different question: **given a finite cohort of discrete cargo particles entering at the plasma membrane, how does the cohort partition across competing intracellular destinations over time?**

| Biological phenomenon | Boolean network (`BOOLEAN`) | Agent-Based Trafficking (`AGENT_BASED`) |
|---|---|---|
| **Cargo conservation** | No conservation: every downstream branch can turn `ON` simultaneously | Strict particle conservation: $\sum_i n_i(t) = N_{\text{agents}}$ at every step $t$ |
| **Competing branch flux** (`early_endosome` $\to$ recycling vs. late endosome vs. cytosolic escape) | All reachable branches evaluate to `1` unless mutually exclusive logic is hard-coded | Competing outflow transitions split the compartment's particle pool proportionally to their active transition rates |
| **Knockout of a dominant sink** (e.g., `Rab7` loss in [PMID:41814093](https://pubmed.ncbi.nlm.nih.gov/41814093/)) | Sets the `escrt_rab7_late_endosome` bit to `0`; cannot quantify how much trapped cargo is diverted to escape vs. recycling | Relieves competing-pathway attenuation and diverts trapped early-endosomal cargo into `cytosolic_cargo_escape` ($10\% \to 47\%$) and `ehd1_recycling_branch` ($47\% \to 53\%$) |
| **Downstream enzymatic block** (e.g., `LIPA` loss in Wolman disease or `CTSD` loss in CLN10) | Sets the terminal hydrolysis bit to `0`; upstream nodes remain `1` indistinguishably from wild type | Cargo physically accumulates in the immediately upstream endolysosomal compartment (`escrt_rab7_late_endosome` or `ldlr_endocytosis`) |

---

## How a module compiles into an Agent-Based Model

In `src/ai_gene_review/module_abm.py`, `module_to_abm()` compiles a `ModuleReview` YAML document directly into an `ABMModel` with no external rule files:

1. **Compartments (`ABMStage`)**: Every leaf activity (`AtomicActivity`) or complex (`ProteinComplex`) that participates in at least one resolved module connection (with containers expanded to their constituent leaves via `PART_OF`) becomes a discrete stage.
   - **Entry stages**: Stages with outgoing cargo flow (`PROVIDES_INPUT_FOR` / `CAUSES` / `HAS_INPUT`) and no incoming cargo flow (e.g., `tfrc_cargo_binding` or `apob_ligand`; falling back to the first flow stage if all flow stages have incoming flow) split the initial cohort of $N = 100$ cargo particles at $t = 0$.
   - **Pure regulators (`is_flow_stage = False`)**: Stages that only emit or receive regulatory edges (`POSITIVELY_REGULATES` / `NEGATIVELY_REGULATES`) and have no incoming or outgoing flow edges (e.g., `pcsk9_degradation` in `ldl_receptor_mediated_endocytosis`) are flagged with `is_flow_stage = False` and `default_active = False`. They act as regulatory switches rather than cargo-holding compartments.
2. **Flow transitions (`ABMTransition`)**: Every `PROVIDES_INPUT_FOR`, `CAUSES`, or `HAS_INPUT` connection between stages becomes a directed particle transition with a uniform uncalibrated default base rate:
   - **Uniform base transition rate**: $r_{\text{base}} = 0.45\text{ step}^{-1}$ (`DEFAULT_BASE_RATE = 0.45`). Branch partitioning arises from the module topology and regulatory edges rather than stage-name heuristics.
3. **Regulatory coupling (`NEGATIVELY_REGULATES` and `POSITIVELY_REGULATES`)**:
   - **Competing-pathway attenuation**: When a flow stage $A$ `NEGATIVELY_REGULATES` a sibling flow stage $B$ (e.g., `escrt_rab7_late_endosome` $\dashv$ `cytosolic_cargo_escape`), active sequestration down pathway $A$ multiplies transitions into $B$ by `COMPETING_INHIBITOR_FACTOR = 0.25`. Knocking out $A$ (`active: false`) relieves that attenuation, allowing trapped upstream particles to divert into $B$.
   - **Pure regulator gating**: When a pure regulator $R$ `NEGATIVELY_REGULATES` a transport stage $T$ (e.g., `pcsk9_degradation` $\dashv$ `ldlr_endocytosis`), locking $R$ `ON` (`active: true`) gates off $T$ and sets transitions into $T$ to zero, trapping cargo upstream.
   - **Positive modulation**: When a flow stage $M$ `POSITIVELY_REGULATES` a target stage $T$, transitions into $T$ are boosted by `POSITIVE_REGULATOR_BOOST = 1.35` when $M$ is active and gated to $0$ when $M$ is inactive (unless overridden by an explicit `activation_logic` expression).
4. **Conservation-preserving discrete stepping (`simulate_abm`)**:
   - At each step $t \in [1, 24]$, if a compartment has total active outflow rate $R = \sum_k r_k > 0.85$ (`DEFAULT_MAX_LEAVE_FRACTION`), outgoing rates are scaled proportionally so at most $\lceil 0.85 \cdot n_u(t) \rceil$ particles leave in a single step.
   - Integer particle movements are assigned via the **largest-remainder method**, guaranteeing exact particle conservation ($\sum_i n_i(t) = N_{\text{agents}}$) at every time step in both Python (`module_abm.py`) and browser JavaScript (`executable_abm.html.j2`).

---

## Curated Agent-Based Trafficking Models

### 1. Endosomal Trafficking, Sorting & Cytosolic Escape (`endosomal_trafficking_routing`)

* **Module**: [`modules/endosomal_trafficking_routing.yaml`](../modules/endosomal_trafficking_routing.html)
* **Interactive ABM**: [`pages/models/endosomal_trafficking_abm.html`](../models/endosomal_trafficking_abm.html)
* **Biology & Qualitative Parameterization**: Models the 7-stage canonical endolysosomal sorting network shared by physiological transferrin-iron (`TFRC`) uptake and therapeutic lipid nanoparticle (LNP) / macromolecular cargo delivery:
  1. `tfrc_cargo_binding` (`TFRC`, `PANTHER:PTHR10404:SF26`, [PMID:10192390](https://pubmed.ncbi.nlm.nih.gov/10192390/))
  2. `clathrin_ap2_internalization` (`CLTC` `PANTHER:PTHR10292:SF7`, `AP2M1` `PANTHER:PTHR10529`, [PMID:31104773](https://pubmed.ncbi.nlm.nih.gov/31104773/), [PMID:14985334](https://pubmed.ncbi.nlm.nih.gov/14985334/))
  3. `early_endosome_acidification` (`ATP6V1A` `PANTHER:PTHR43607:SF9`, luminal acidification to pH ~6.0, [PMID:33065002](https://pubmed.ncbi.nlm.nih.gov/33065002/))
  4. `ehd1_recycling_branch` (`EHD1` `PANTHER:PTHR11216:SF127`, endocytic recycling compartment export to plasma membrane, [PMID:15020713](https://pubmed.ncbi.nlm.nih.gov/15020713/))
  5. `escrt_rab7_late_endosome` (`TSG101` `PANTHER:PTHR23306:SF17`, `RAB7A`/`Rab7` `PANTHER:PTHR47981:SF13`, ESCRT-I MVB sorting and Rab7 late endosome maturation, [PMID:12900395](https://pubmed.ncbi.nlm.nih.gov/12900395/), [PMID:20028791](https://pubmed.ncbi.nlm.nih.gov/20028791/))
  6. `cytosolic_cargo_escape` (`RAB7A`/`Rab7` negative regulation of pre-lysosomal membrane translocation, [PMID:41814093](https://pubmed.ncbi.nlm.nih.gov/41814093/))
  7. `ctsd_lysosomal_degradation` (`CTSD` `PANTHER:PTHR47966:SF42`, terminal lysosomal proteolysis, [PMID:8393577](https://pubmed.ncbi.nlm.nih.gov/8393577/))

| Scenario ID | Perturbation (`settings`) | Final Cohort Distribution ($N = 100, T = 24$) | Biological Interpretation |
|---|---|---|---|
| `wt_steady_trafficking` | *(none)* | **47%** `ehd1_recycling_branch`, **43%** `ctsd_lysosomal_degradation`, **10%** `cytosolic_cargo_escape` | Baseline endosomal partitioning under uniform default rates: most internalized cargo is recycled or degraded in lysosomes while ~10% escapes to the cytosol (consistent with the qualitative pattern of low (~8%) baseline hepatic LNP cytosolic escape in [PMID:41814093](https://pubmed.ncbi.nlm.nih.gov/41814093/)). |
| `rab7a_loss_lnp_escape` | `escrt_rab7_late_endosome: false` | **53%** `ehd1_recycling_branch`, **47%** `cytosolic_cargo_escape`, **0%** `ctsd_lysosomal_degradation` | **Rab7 loss-of-function ([PMID:41814093](https://pubmed.ncbi.nlm.nih.gov/41814093/))**: Blocking late-endosome/lysosome maturation prevents lysosomal degradation and lifts competitive sequestration, increasing productive cytosolic cargo escape from 10% to 47% in the uncalibrated model. |
| `clathrin_endocytosis_block` | `clathrin_ap2_internalization: false` | **100%** `tfrc_cargo_binding` | Clathrin/AP-2 Pitstop-2 or `AP2M1` Y286A block traps 100% of receptor-bound cargo at the cell surface. |
| `vatpase_acidification_block` | `early_endosome_acidification: false` | **100%** `clathrin_ap2_internalization` | Bafilomycin A1 / V-ATPase block prevents luminal acidification and ligand uncoupling, arresting cargo in nascent endocytic vesicles. |
| `ehd1_recycling_block` | `ehd1_recycling_branch: false` | **80%** `ctsd_lysosomal_degradation`, **20%** `cytosolic_cargo_escape` | `EHD1` recycling block diverts the entire sorting pool into late endosomes/lysosomes and pre-lysosomal escape. |
| `ctsd_proteolysis_block` | `ctsd_lysosomal_degradation: false` | **47%** `ehd1_recycling_branch`, **43%** `escrt_rab7_late_endosome`, **10%** `cytosolic_cargo_escape` | Cathepsin D (`CTSD`) deficiency traps undegraded cargo inside `escrt_rab7_late_endosome` (ceroid/lipofuscin storage phenotype in CLN10). |

### 2. Hepatocyte ASGR1/ASGR2 GalNAc-Conjugate Uptake & Endosomal Escape (`asgr_galnac_hepatocyte_delivery`)

* **Module**: [`modules/asgr_galnac_hepatocyte_delivery.yaml`](../modules/asgr_galnac_hepatocyte_delivery.html)
* **Interactive ABM**: [`pages/models/asgr_galnac_delivery_abm.html`](../models/asgr_galnac_delivery_abm.html)
* **Biology & Qualitative Parameterization**: Models hepatocyte-targeted trivalent GalNAc-siRNA/ASO capture by the sinusoidal C-type lectin receptor complex `ASGR1`/`ASGR2` (`PANTHER:PTHR22803`, [PMID:12171918](https://pubmed.ncbi.nlm.nih.gov/12171918/), [PMID:29069408](https://pubmed.ncbi.nlm.nih.gov/29069408/)), clathrin/AP-2/dynamin-2 internalization (`AP2M1`, `CLTC`, `DNM2`, [PMID:24970086](https://pubmed.ncbi.nlm.nih.gov/24970086/)), V-ATPase early endosomal acidification and $\text{Ca}^{2+}$-dependent GalNAc uncoupling (`ATP6V1A`), rapid `EHD1` receptor recycling (`ehd1_receptor_recycling`, **47%**), `TSG101`/`RAB7A` late-endosomal maturation (`escrt_rab7_late_endosome`) and `CTSD` lysosomal sequestration/degradation (`ctsd_lysosomal_degradation`, **43%**), and rate-limiting cytosolic oligonucleotide escape (`cytosolic_galnac_escape`, **10%** in wild-type, rising to **47%** upon `RAB7A` loss). Note that the **10%** baseline escape (`47/43/10`) and `10% -> 47%` shift upon `RAB7A` loss result from uniform uncalibrated ABM rates (`DEFAULT_BASE_RATE = 0.45`, `COMPETING_INHIBITOR_FACTOR = 0.25`) and represent a qualitative cross-modality extrapolation from hepatic LNP delivery ([PMID:41814093](https://pubmed.ncbi.nlm.nih.gov/41814093/)), whereas only a minuscule portion of endocytosed clinical GalNAc-siRNA/ASO conjugates escapes into the cytosol in vivo ([PMID:29069408](https://pubmed.ncbi.nlm.nih.gov/29069408/)).

### 3. Neonatal Fc Receptor (FCGRT/B2M) pH-Dependent IgG & Albumin Salvage (`fcrn_igg_albumin_salvage_transcytosis`)

* **Module**: [`modules/fcrn_igg_albumin_salvage_transcytosis.yaml`](../modules/fcrn_igg_albumin_salvage_transcytosis.html)
* **Interactive ABM**: [`pages/models/fcrn_salvage_transcytosis_abm.html`](../models/fcrn_salvage_transcytosis_abm.html)
* **Biology & Qualitative Parameterization**: Models how endothelial and barrier epithelial cells maintain the ~21-day circulatory half-life of human IgG and serum albumin (`ALB`, `PANTHER:PTHR11385:SF15`, [PMID:36979511](https://pubmed.ncbi.nlm.nih.gov/36979511/)). Following pinocytic and clathrin/AP-2/DNM2 uptake (`clathrin_dnm2_endocytic_uptake`) and V-ATPase acidification to pH ~6.0 (`early_endosome_acidification`), protonated histidine residues on IgG and albumin bind the endosomal `FCGRT`/`B2M` (FcRn) heterodimer (`fcrn_ph_dependent_salvage`, [PMID:28330995](https://pubmed.ncbi.nlm.nih.gov/28330995/), [PMID:24469444](https://pubmed.ncbi.nlm.nih.gov/24469444/)). Active FcRn capture negatively regulates `rab7_late_endosome_routing`, rescuing **80%** of internalized cohort via `EHD1`/`SNAP23` exocytic recycling (`ehd1_snap23_salvage_exocytosis`, [PMID:30811271](https://pubmed.ncbi.nlm.nih.gov/30811271/)) vs. **20%** lysosomal catabolism (`ctsd_lysosomal_catabolism`). Inactivating `fcrn_ph_dependent_salvage` (modeling `FCGRT`/`B2M` deficiency or therapeutic anti-FcRn blockers such as efgartigimod) diverts **100%** of internalized IgG/albumin to lysosomal catabolism.

### 4. Retromer (VPS35/VPS26A/VPS29) & SORL1 Endosome-to-TGN Retrograde Retrieval (`retromer_endosome_to_tgn_retrieval`)

* **Module**: [`modules/retromer_endosome_to_tgn_retrieval.yaml`](../modules/retromer_endosome_to_tgn_retrieval.html)
* **Interactive ABM**: [`pages/models/retromer_retrograde_sorting_abm.html`](../models/retromer_retrograde_sorting_abm.html)
* **Biology & Qualitative Parameterization**: Models retrograde endosome-to-Golgi retrieval of the Alzheimer-associated sorting receptor `SORL1` (SorLA/LR11, `PANTHER:PTHR12106:SF27`, [PMID:16174740](https://pubmed.ncbi.nlm.nih.gov/16174740/)) by the heterotrimeric retromer cargo-selective complex (`VPS35` `PANTHER:PTHR11099:SF0`, `VPS26A` `PANTHER:PTHR12233:SF4`/`SF1`, `VPS29` `PANTHER:PTHR11124:SF12`, [PMID:15078902](https://pubmed.ncbi.nlm.nih.gov/15078902/), [PMID:18193037](https://pubmed.ncbi.nlm.nih.gov/18193037/), [PMID:18193032](https://pubmed.ncbi.nlm.nih.gov/18193032/), [PMID:32286230](https://pubmed.ncbi.nlm.nih.gov/32286230/)) across early and maturing endosomes and TGN docking via `RAB9A` and `AP-1` (`AP1B1` `PANTHER:PTHR11134:SF31`/`SF3`, `AP1G1` `PANTHER:PTHR22780:SF26`, [PMID:8164745](https://pubmed.ncbi.nlm.nih.gov/8164745/), [PMID:34793709](https://pubmed.ncbi.nlm.nih.gov/34793709/), [PMID:23415225](https://pubmed.ncbi.nlm.nih.gov/23415225/)). In wild-type sorting (`wt_retromer_tgn_retrieval`), active retromer recruitment (`retromer_csc_cargo_selection`) opposes `RAB7A` degradative progression and delivers **80%** of internalized receptors to the TGN (`rab9a_ap1_tgn_delivery`) vs. **20%** lysosomal proteolysis (`ctsd_lysosomal_proteolysis`). Retromer loss (`retromer_vps35_loss_degradation`) diverts **100%** of cargo to lysosomal degradation, whereas `RAB7A` block (`rab7_reduction_suppresses_degradation`) restores **100%** TGN retrieval ([PMID:32286230](https://pubmed.ncbi.nlm.nih.gov/32286230/)).

### 5. LDL Receptor-Mediated Endocytosis (`ldl_receptor_mediated_endocytosis`)

* **Module**: [`modules/ldl_receptor_mediated_endocytosis.yaml`](../modules/ldl_receptor_mediated_endocytosis.html)
* **Interactive ABM**: [`pages/models/ldlr_endocytosis_abm.html`](../models/ldlr_endocytosis_abm.html) (alongside the existing [Boolean model](../models/ldlr_endocytosis_boolean.html))
* **Dual-model demonstration**: The exact same 4-stage module (`apob_ligand`, `ldlr_endocytosis`, `lipa_ce_hydrolysis`, `pcsk9_degradation`) compiles into both a Boolean network and an Agent-Based cohort simulator:
  - `normal_ldl_clearance`: Maximal PCSK9-independent clearance (`pcsk9_degradation` defaults to `false`), delivering **100%** of the `apob_ligand` cohort to `lipa_ce_hydrolysis`.
  - `pcsk9_gain_of_function` (`pcsk9_degradation: true`): Pure-regulator inhibition of `ldlr_endocytosis` traps **100%** of LDL particles in the extracellular `apob_ligand` pool.
  - `ldlr_loss_fh` (`ldlr_endocytosis: false`): Familial hypercholesterolemia receptor loss traps **100%** of LDL particles in `apob_ligand`.
  - `lipa_loss_wolman` (`lipa_ce_hydrolysis: false`): Wolman disease / CESD acid lipase loss internalizes LDL normally (`apob_ligand = 0%`) but traps **100%** of unhydrolyzed cholesteryl esters in the endolysosomal `ldlr_endocytosis` compartment.

---

## Scenario Validation in CI (`validate_executable_models`)

Every scenario declared on a module-derived `AGENT_BASED` model is executed and verified automatically by `just validate-modules` (`src/ai_gene_review/validation/module_validator.py`):

* `expected_active`: flow stages that must be enabled (`element_active = True`) and visited by cargo (`peak_counts > 0`) during the simulation, or pure regulators that evaluate to `element_active = True`.
* `expected_inactive`: flow stages that must either be disabled (`element_active = False`) or never reached by cargo (`peak_counts == 0`), or pure regulators that evaluate to `element_active = False`.
* `expected_outcome_order`: stages listed in strictly descending order of final particle count at $T = 24$ ($n_{\text{final}}(s_1) > n_{\text{final}}(s_2) > \dots$), allowing quantitative branching predictions (such as `ehd1_recycling_branch > ctsd_lysosomal_degradation > cytosolic_cargo_escape` in wild-type vs. `ehd1_recycling_branch > cytosolic_cargo_escape > ctsd_lysosomal_degradation` in `Rab7` loss) to be regression-tested against module topology edits.
