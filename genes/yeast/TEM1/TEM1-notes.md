# TEM1 (YML064C, UniProt P38987) – curation notes

Working journal for the GO review of *S. cerevisiae* Tem1, the Ras/Rab-like GTPase at the
head of the mitotic exit network (MEN). Sources: `TEM1-uniprot.txt`, `TEM1-goa.tsv`,
`TEM1-deep-research-falcon.md` (Edison/Falcon synthesis, largely built on Zhou et al. 2024
PNAS, PMID:39475649, and Scarfone & Piatti 2015 Small GTPases), and the cached publications
for every `original_reference_id`. Abstract-only caches: PMID:10219244, 11805837, 12048186,
12628189, 21937712. Full text cached: PMID:14734533, 19154724, 21321099, 25658911, 32074005.
The founding paper (Shirayama et al. 1994, PMID:7935462) and Zhou et al. 2024 are not in the
local cache and are therefore not cited in `supported_by`.

## Identity and domain architecture

- 245 aa, single Ras-like small-GTPase domain (UniProt REGION 16-244), three GTP-binding
  motifs (27-34, 75-79, 132-135), disordered C-terminal tail (210-245). InterPro
  IPR017231 "Small_GTPase_Tem1/Spg1", CDD cd04128 Spg1, Pfam PF00071 Ras, PANTHER PTHR47978.
- Orthologue of *S. pombe* Spg1 (SIN GTPase). PAINT nodes used for the IBAs: PTN004662974
  (Ras-superfamily-level node for GTPase activity / GTP binding) and PTN000634389
  (Tem1/Spg1 clade node for SPB localisation and septum-assembly regulation).
- Cloned as a GTP-binding protein required for termination of M phase; UniProt FUNCTION:
  "GTP-binding protein involved in termination of M phase ... Acts upstream of CDC15 kinase".
  573 molecules/cell (PMID:14562106, per UniProt).

## Biochemistry

- Intrinsic GTPase: [PMID:12048186 "We describe the nucleotide binding properties of Tem1
  and characterize its intrinsic GTPase activity."] and the two-component GAP:
  [PMID:12048186 "The combination of Bfa1 and Bub2 acts as a two-component
  GTPase-activating protein for Tem1."]. Bfa1 alone inhibits both hydrolysis and exchange;
  Bfa1 is proposed to act as adaptor connecting Bub2 and Tem1.
- Quantitative parameters (deep research, from Zhou et al. 2024): MANT-GDP Kd 1.2 uM,
  spontaneous exchange 0.005 /s, intrinsic hydrolysis 0.011 /min; GAP-stimulated hydrolysis
  ~0.07 /s (~400-fold); Bub2-Bfa1 binds Tem1-GTPgS at <0.4 nM; Cdc15 binds Tem1-GTPgS at
  3.9 nM vs Tem1-GDP at 16 nM (only ~4-fold selectivity). [file:yeast/TEM1/TEM1-deep-research-falcon.md
  "Cdc15 is the immediate downstream kinase effector."]
- Q79L (switch II glutamine) is GAP-refractory: [PMID:25658911 "Tem1-Q79L was completely
  refractory to stimulation of GTP hydrolysis by the GAP Bub2/Bfa1 in vitro, suggesting that
  in vivo it is preferentially in its active GTP-bound form."]
- Lte1 as GEF is not established: [file:yeast/TEM1/TEM1-deep-research-falcon.md "Direct
  stimulation of Tem1 nucleotide exchange has not been established biochemically."] Given the
  fast spontaneous exchange, a GEF may not be needed at all. Do not annotate Lte1 as a Tem1 GEF
  on the strength of the older genetics.

## Localisation

- SPB, asymmetric, daughter-bound pole: [PMID:19154724 "Bfa1, Bub2 and Tem1 form a complex
  (henceforth the Tem1 complex) that localizes to spindle pole bodies (SPBs) in an asymmetric
  manner."]; [PMID:19154724 "Localization of Tem1 at SPBs depends on the Bub2-Bfa1 complex but
  the converse is not true"].
- Residence is dynamic (FRAP t1/2 ~6 s WT, ~16 s Q79L); recruitment via Bub2-Bfa1, or via Cdc15
  when Bfa1 is absent [file:yeast/TEM1/TEM1-deep-research-falcon.md "Tem1 cannot stably
  associate with SPBs by itself: recruitment occurs predominantly through Bub2–Bfa1 and, when
  that complex is absent, through Cdc15."]
- SPB localisation is required for function: [PMID:21321099 "Finally, we demonstrate for the
  first time that localization of Tem1 to the SPBs is a requirement for mitotic exit."]; the
  Cnm67-Tem1 fusion (constitutive SPB loading) keeps tem1-null cells alive.
- Anaphase accumulation on the dSPB initiates signalling: [PMID:32074005 "Movement of half of
  the nucleus into the bud during anaphase causes the active form of the MEN GTPase Tem1 to
  accumulate at the dSPB."]

## Pathway position and outputs

- MEN order: Tem1 -> Cdc15 -> Dbf2-Mob1 -> Cdc14. [PMID:12628189 "In S. cerevisiae cells
  undergoing anaphase, a ras-related GTPase, Tem1, is located on the spindle pole body that
  enters the daughter cell and activates a signal transduction pathway, MEN, to allow mitotic
  exit."]
- Tem1 recruits Cdc15 to SPBs: [PMID:32074005 "The GTPase Tem1 recruits the protein kinase
  Cdc15 to SPBs."]; [PMID:21937712 "We further show that both Tem1 and Cdc5 are required to
  recruit the MEN kinase Cdc15 to spindle pole bodies, which is both necessary and sufficient
  to induce MEN signaling."] Cdc15 is a coincidence detector of Tem1 (spatial) and Cdc5
  (temporal) inputs; MEN restriction to anaphase can occur Tem1-independently in unperturbed
  cycles [PMID:21937712 "restricting MEN activity to anaphase can occur in a Tem1
  GTPase-independent manner"].
- Cdc14 release from the nucleolar RENT complex: [PMID:10219244 "In late anaphase, Cdc14
  dissociates from RENT, disperses throughout the cell in a Tem1-dependent manner, and
  ultimately triggers mitotic exit."]; net1-1 bypasses tem1-null lethality.
- Reset after exit: Amn1 [PMID:12628189 "the Amn1 protein that binds directly to Tem1 and
  prevents its association with its target kinase Cdc15"].
- Revised model (Zhou 2024 via deep research): Tem1 is not a classic binary switch whose
  GTP:GDP ratio rises at anaphase; the nucleotide cycle sets SPB recruitment/turnover, and
  spindle position controls MEN activation by setting the local *concentration* of Tem1.
  SPB-tethering or 120-mer nanoparticle clustering rescues nucleotide-binding-dead T34A/T34N.
  Model estimates (<10 % Tem1-GTP with active GAP) are not direct measurements – flagged in
  suggested_experiments.

## Spindle position checkpoint (SPOC) and spindle orientation

- Constitutively active Tem1 mutants are SPOC-defective and symmetric: [PMID:25658911 "These
  mutants are SPOC-defective and invariably lead to symmetrical localization of Bub2/Bfa1/Tem1
  at spindle poles, indicating that GTP hydrolysis is essential for asymmetry."]; removal of
  Tem1 from SPBs is needed for the SPOC [PMID:21321099 "We also find that removal of Tem1 from
  the SPBs is critical for the SPOC to impede cell cycle progression."]
- Kar9 asymmetry / spindle orientation: [PMID:25658911 "Thus, asymmetry of the Bub2/Bfa1/Tem1
  complex is crucial to control Kar9 distribution and spindle positioning during mitosis."]
  but [PMID:25658911 "Although Tem1 inactivation causes similar phenotypes for what concerns
  Kar9 localization and spindle orientation, it does not affect spindle positioning at the bud
  neck"]. This role is exerted via MEN kinase activity on Kar9 – indirect for Tem1.

## Curation decisions (summary)

| Term | Evidence | Action | Note |
|---|---|---|---|
| GO:0003924 GTPase activity | IBA, IDA x2, IEA | ACCEPT | measured intrinsic + GAP-stimulated hydrolysis |
| GO:0005525 GTP binding | IBA, IEA | ACCEPT | canonical P-loop GTPase |
| GO:0005816 spindle pole body | IBA, IDA, IEA | ACCEPT | site of action |
| GO:0005515 protein binding (Cdc15, PMID:12628189) | IPI | MODIFY -> GO:0003925 G protein activity | effector engagement is the defining function |
| GO:0005515 protein binding (Cdc15/Bfa1 HT screen; Amn1; Bub2; Bfa1) | IPI x5 | REMOVE | uninformative; GAP/inhibitor relationships belong on the partner |
| GO:0023056 positive regulation of signaling | IDA | MODIFY -> GO:0007264 small GTPase-mediated signal transduction | Tem1 *is* the relaying GTPase, not an external regulator; term too general |
| GO:0031536 positive regulation of exit from mitosis | IMP | ACCEPT | core |
| GO:0031578 mitotic spindle orientation checkpoint signaling | IMP | ACCEPT | Tem1's GAP-stimulated hydrolysis executes the checkpoint output |
| GO:0035556 intracellular signal transduction | IEA | ACCEPT | broad parent |
| GO:0040001 establishment of mitotic spindle localization | IMP | KEEP_AS_NON_CORE | indirect via MEN/Kar9; abstract-only, defer to curator |
| GO:0090068 positive regulation of cell cycle process | IEA | ACCEPT | broad parent |
| GO:0140281 positive regulation of mitotic division septum assembly | IBA | KEEP_AS_NON_CORE | Spg1/SIN-derived; true for MEN output but several steps downstream |
| GO:1902542 regulation of protein localization to mitotic SPB | IMP | ACCEPT | Cdc15 recruitment = mechanism |
| GO:1904750 negative regulation of protein localization to nucleolus | IMP | ACCEPT | Cdc14 release; regulation term admits indirect action |

- Comparator checks: GO:0140281 sits under GO:0032467 positive regulation of cytokinesis;
  budding-yeast genes DBF20, MNN10, BNI4, SHS1 are annotated to GO:0000917 division septum
  assembly, so the term is in use for *S. cerevisiae*. GO:0003925 and GO:0007264 verified in
  QuickGO (not obsolete, unrestricted usage).
- No NEW terms proposed. The MEN-initiating function is fully covered by the accepted/modified
  rows; a `positive regulation of cytokinesis` annotation would duplicate the IBA already kept.
- GO-CAM index: no production GO-CAM contains TEM1 (checked `gocams/index.tsv`).
- Module `metaphase_anaphase_transition_and_mitotic_exit.yaml` types Tem1 as GO:0003924 with
  process GO:0007096; the core_functions here are consistent (GO:0003924; GO:0031536 is the
  positive child of GO:0007096).

## Open questions

- How does Tem1 binding convert Cdc15 into its SPB-competent active form, given only ~4-fold
  nucleotide selectivity of Cdc15 for Tem1-GTP?
- Is Lte1 a GEF at all? Biochemistry says probably not.
- Direct measurement of endogenous Tem1 nucleotide state across the cell cycle is still lacking.

## 2026-09-29 IBA alignment

- Rechecked the four TEM1 IBA rows against the current `PTHR47978` PAINT snapshot.
  `PTN004662974` still carries `GO:0003924` GTPase activity and `GO:0005525` GTP
  binding on the conserved Tem1/Spg1 and related small-GTPase branch.
  `PTN000634389` still carries `GO:0005816` spindle pole body and `GO:0140281`
  positive regulation of mitotic division septum assembly on the Tem1/Spg1 clade.
- Added PTN-level `propagation_review` blocks to those IBA rows. The
  small-GTPase activity and spindle-pole-body localization are core for budding-yeast
  Tem1; the septum-assembly process remains a defensible but non-core MEN/SIN output
  that is several kinase steps downstream of Tem1 in S. cerevisiae.
- Searched 2025-2026 PubMed and the broader web for yeast TEM1, YML064C, Tem1, Cdc15,
  and mitotic exit network literature. The search turned up Zhou et al. 2024 PNAS as
  the newest mechanistic Tem1 study already synthesized in the existing deep-research
  report; no newer peer-reviewed S. cerevisiae TEM1 paper changes the GO decisions.
