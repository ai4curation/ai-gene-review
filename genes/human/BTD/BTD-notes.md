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
