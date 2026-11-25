# BTD (Biotinidase, P43251) — review notes

## Core biology (verified)
BTD is **biotinidase** (EC 3.5.1.12), the enzyme that recycles biotin. It hydrolyses
**biocytin** (biotinyl-lysine) and short biotinyl-peptides released by proteolysis of the
holo-carboxylases, liberating free biotin for reuse; it also cleaves dietary protein-bound
biotin, making dietary biotin bioavailable.

- Catalytic reaction (UniProt): `biocytin + H2O = biotin + L-lysine` (Rhea:RHEA:77171) and
  `biotin amide + H2O = biotin + NH4(+)` (Rhea:RHEA:13081), EC 3.5.1.12.
  [file:P43251 UniProt CATALYTIC ACTIVITY]
- UniProt FUNCTION: "Catalytic release of biotin from biocytin, the product of
  biotin-dependent carboxylases degradation." [ECO:0000305|PubMed:9099842, PubMed:9654207]
- Belongs to the carbon-nitrogen hydrolase superfamily, BTD/VNN family. CN hydrolase domain
  (52-331); catalytic triad ACT_SITE 92 (proton acceptor), 192 (proton donor), 225 (nucleophile).
- SUBCELLULAR LOCATION (UniProt): "Secreted, extracellular space." Serum/plasma glycoprotein
  (N-glycosylated at N99, N130, N183, N329, N382, N469). Detected in colostrum and prostatic
  exosomes by proteomics.
- Reported side activity: **biotinyl-transferase / biotinylation** activity (UniProt variant
  annotations at D444H "52% decrease in biotinyl-transferase activity" and R518C "loss of
  biotinyl-transferase activity"). Consistent with a transferase side reaction.

## Disease
Biotinidase deficiency (MIM:253260; MONDO:0009665) — autosomal recessive; a treatable,
newborn-screened **late-onset (juvenile) multiple carboxylase deficiency**. Loss of biotinidase
prevents recycling of biotin from biocytin/biotinyl-peptides → free-biotin depletion → secondary
functional deficiency of the four biotin-dependent carboxylases (PC, PCC, MCC, ACC). Profound
(<10% residual) vs partial (10-30%). Lifelong oral biotin is highly effective if started early.
[dismech kb: Biotinidase_Deficiency.yaml; Reactome R-HSA-3076905; UniProt DISEASE]

## Reactome context
R-HSA-3076905 "Extracellular BTD hydrolyses BCTN" and R-HSA-4167509 "Mitochondrial BTD
hydrolyses BCTN": Reactome asserts BTD is "both secreted from various cells and localised in
the mitochondria (Wolf & Jensen 2005)." The mitochondrial-matrix localization (GO:0005759) is a
Reactome TAS claim; the dominant/canonical localization is secreted/extracellular (serum). The
mitochondrial claim is less well established than secretion; keep as non-core.

## GOA annotation set (20 lines) and dispositions
1. GO:0005576 extracellular region, IBA (GO_REF:0000033), is_active_in → ACCEPT (core location; secreted enzyme)
2. GO:0006768 biotin metabolic process, IBA → ACCEPT (core BP; biotin recycling/salvage)
3. GO:0047708 biotinidase activity, IBA → ACCEPT (core MF)
4. GO:0005576 extracellular region, IEA (SubCell SL-0112) → ACCEPT (redundant, correct)
5. GO:0016811 hydrolase acting on C-N (not peptide) linear amides, IEA (InterPro/ARBA) → ACCEPT as broader parent MF of biotinidase activity (biotin-amide C-N bond); correct but general
6. GO:0047708 biotinidase activity, IEA (RHEA:13081/EC:3.5.1.12) → ACCEPT (core MF, direct EC mapping)
7. GO:0005515 protein binding, IPI PMID:28514442 (MYO1D O94832, BioPlex) → MARK_AS_OVER_ANNOTATED (bare protein binding; uninformative; HT AP-MS)
8. GO:0005515 protein binding, IPI PMID:33961781 (MYO1D O94832, BioPlex) → MARK_AS_OVER_ANNOTATED (same)
9. GO:0006768 biotin metabolic process, TAS Reactome:R-HSA-196780 → ACCEPT (core BP)
10-13. GO:0047708 biotinidase activity, TAS x4 Reactome → ACCEPT (core MF; keep one as core, others redundant but correct)
14. GO:0005576 extracellular region, TAS Reactome:R-HSA-3325540 → ACCEPT (correct location)
15. GO:0005759 mitochondrial matrix, TAS Reactome:R-HSA-4225086 → KEEP_AS_NON_CORE (secondary/debated localization)
16. GO:0070062 extracellular exosome, HDA PMID:23533145 → KEEP_AS_NON_CORE (proteomic detection in prostatic exosomes; consistent with secreted, non-core)
17. GO:0005576 extracellular region, HDA PMID:16502470 → ACCEPT (colostrum proteomics; secreted, supports extracellular)
18. GO:0005759 mitochondrial matrix, TAS Reactome:R-HSA-4167509 → KEEP_AS_NON_CORE (same as #15)
19. GO:0005576 extracellular region, TAS Reactome:R-HSA-3076905 → ACCEPT (correct location)
20. GO:0007417 central nervous system development, TAS PMID:7550325 → MARK_AS_OVER_ANNOTATED (disease/phenotype-derived; CNS symptoms of deficiency, not a direct developmental role of the enzyme; ProtInc legacy TAS). Abstract is about a mutation causing deficiency, not a CNS developmental function.

## Supporting-text verification notes
- PMID:16502470 (colostrum) and PMID:23533145 (prostatic exosomes) are HT proteomics; BTD is
  not named in cached abstract, but these are HDA (mass-spec detection) annotations by UniProt —
  do NOT remove per policy; use verbatim abstract quotes about the fluid/exosome source.
- PMID:28514442 / PMID:33961781 (BioPlex): bare protein-binding IPIs from IntAct (MYO1D). Use
  verbatim methodology quotes. MARK_AS_OVER_ANNOTATED, not REMOVE (per policy on bare PB IPIs).
- PMID:7550325 abstract does not describe a CNS developmental function; it describes a
  deficiency-causing mutation. CNS involvement is a downstream disease phenotype.

## core_functions
- MF: GO:0047708 biotinidase activity
- BP (directly_involved_in): GO:0006768 biotin metabolic process (biotin recycling/salvage)
- location: GO:0005576 extracellular region (secreted)


## 2026-10-03 — source reassessment and review follow-up

This section supersedes the earlier dispositions and unchecked claims above. The historical notes are preserved verbatim. All 20 source assertions and four alternative products are unchanged. Fourteen annotations are ACCEPT and six are UNDECIDED; there is one extracellular biotinidase core and no NEW annotation.

BTD performs the biotin salvage reaction itself. The human serum cloning study identifies the enzyme through peptide sequence, liver cDNA and antibody recognition [PMID:7509806 "catalyzes the hydrolysis of biocytin"](https://pubmed.ncbi.nlm.nih.gov/7509806/). The historical sequence has 543 residues, whereas the current UniProt displayed product has 523. Historical D444H numbering must not be transferred silently onto its Asp424 position. The source records remain unchanged. RHEA:13081 describes biotin-amide hydrolysis; biocytin hydrolysis is RHEA:77171. The human R538C study also supports an enzyme/secretion defect and now supplements the biotinidase-activity reviews [PMID:9099842](https://pubmed.ncbi.nlm.nih.gov/9099842/). No new histone-transferase function is inferred. PMID:9654207 has an erratum whose substantive content was unavailable; no quantitative variant-effect conclusion depends on it.

The matrix assignments remain uncertain. PMID:15059618 distinguishes nonspecific human organelle immunofluorescence from rat liver fractionation: the rat mitochondrial anti-BTD-reactive protein lacked the measured activities, and its identity was unresolved [PMID:15059618 "The function and validation of the mitochondrial species remains to
be determined."](https://pubmed.ncbi.nlm.nih.gov/15059618/). Sequence analysis provides inconsistent mitochondrial targeting predictions [PMID:16150625](https://pubmed.ncbi.nlm.nih.gov/16150625/). These abstracts do not verify an active human matrix pool; they also do not establish its absence. The complete primary localization experiments and images were not accessible. Reactome's matrix assignments are therefore preserved as unresolved database assertions, while the enzyme activity is independently supported.

The CNS-development row is a legacy TAS, so its UNDECIDED action does not rely on the rule protecting experimental annotations. The abstract establishes biotin-recycling deficiency and preventable neurological injury [PMID:7550325 "permanent neurological
damage can be prevented."](https://pubmed.ncbi.nlm.nih.gov/7550325/). Rescue establishes metabolic necessity rather than identifying a developmental step executed by BTD. That is insufficient to accept the developmental term. Because the full paper and exact annotation rationale remain unavailable, the general source-access rule favors UNDECIDED; absence of a developmental mechanism from an abstract does not establish that the complete paper is MISCITED. The same evidence supports the description's statement about early supplementation and newborn screening without treating therapy as a molecular function.

The two MYO1D interaction assertions remain UNDECIDED because their specific BioPlex records were not inspected [PMID:28514442](https://pubmed.ncbi.nlm.nih.gov/28514442/) and [PMID:33961781](https://pubmed.ncbi.nlm.nih.gov/33961781/). The latter cache contains Introduction/Discussion but not the relevant Results/Methods, despite its full-text flag. The [ClinGen project's curation instruction](../../../projects/CLINGEN_MENDELIAN.md#curation-instructions) explicitly overrides the skill's generic-binding informational-exclusion default: supported correct binding is retained as KEEP_AS_NON_CORE when no evidence-backed finer term is available, while unresolved evidence remains UNDECIDED. This is a project-specific user instruction, not a claim that repository-wide policy changed.

The exosome row also remains UNDECIDED. The full cached article describes a human EPS-urine vesicle preparation and mass spectrometry, but its BTD-specific supplementary record was not inspected [PMID:23533145](https://pubmed.ncbi.nlm.nih.gov/23533145/). Biological plausibility for a secreted enzyme is not record verification. The broad extracellular colostrum annotation is retained on independent human serum evidence, with its target-table limit disclosed [PMID:16502470](https://pubmed.ncbi.nlm.nih.gov/16502470/).

All cited normal publication and Reactome caches are present. The five added publications are abstract-only; the four added Reactome caches contain normal reaction summaries. Sources were not edited. The three IBA node/term/donor joins were checked against cached PAINT data; the separate vanin pantetheinase node is not evidence against the biotinidase placement. No full phylogenetic-tree reconstruction is claimed. The normal deep-research attempt failed dependency resolution, and the installed-provider fallback failed network access; no generated report resulted. The assessment therefore uses the cited primary records with the access limits above. No provider file was written by hand.

The first reassessment passed normal validation and was applied with a standard EDIT history. This follow-up clarifies policy precedence and source uncertainty, adds a clinical-context sentence and the existing R538C enzyme reference, and replaces unpublished working-file pointers with durable literature citations. Prior history records and the historical notes above remain unchanged.

## 2026-10-03 — Review follow-up applied

The independently reviewed follow-up was applied. The 20 source assertions, four products, core function, 14 ACCEPT and six UNDECIDED decisions, and existing YAML quotations are unchanged. The revised explanations distinguish the standing project policy for supported binding from unresolved source access and explain why the abstract alone does not settle the legacy developmental assertion. Existing UniProt and biochemical references now explicitly support the relevant statements. The original notes prefix and all prior history records were preserved.
