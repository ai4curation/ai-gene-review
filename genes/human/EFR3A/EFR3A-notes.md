# EFR3A: evidence notes

## Paired horse benchmark evidence review

The human reference supplies mechanistic evidence for the corresponding selected horse protein; the human conclusion alone is not validation of the horse sequence. The exact horse comparison is in `genes/HORSE/EFR3A/EFR3A-bioinformatics/RESULTS.md`. Research reports are source leads; annotation decisions cite the underlying publication or experimentally supported UniProt passages. Unresolved source-specific results retain UNDECIDED.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Scope: full re-examination of all 13 GOA rows, the NEW MF row, description and core functions. No ProtNLM2 file or prediction-evidence folder was opened.

### Identity
- Q14156 is the reviewed, canonical UniProt entry for human EFR3A (isoform 1, 821 aa). It is not a fragment or an alternative gene model. Alternative products: isoform 2 (VSP_022217, residues 1-36 missing) and isoform 3 (VSP_022218, residues 619-662 missing). Isoform 2 lacks the palmitoylated N-terminal cysteines (sequence MPTRVCCCC..., Cys6-Cys9), which are needed for plasma-membrane anchoring [PMID:23229899 "palmitoylation-deficient mutants (C6S/C7S/C8S/C9S for EFR3A and C5S/C7S/C8S for EFR3B) were localized in the cytosol"]. Added as a suggested question; no isoform-specific GOA rows exist.

### Evolutionary grounding
- PANTHER: PTHR12444 (EFR3 family), subfamily PTHR12444:SF1 (PROTEIN EFR3 HOMOLOG A). Same subfamily contains mouse Efr3a (Q8BG67) and Xenopus efr3a; EFR3B orthologs are in SF4; fly stmA/rbo and worm efr-3 are in SF8 (interpro/panther/PTHR12444/PTHR12444-entries.csv). Yeast Efr3 is in a separate PANTHER family (PTHR47766), so yeast structural data are used for mechanism only, with the mammalian test done on mouse EFR3A (same SF1) [PMID:24360784 "Whereas wild-type EFR3A-GFP localized to the plasma membrane"].
- PAINT node PTN000278197 (EFR3A+EFR3B clade) carries plasma membrane and protein localization to plasma membrane. PAINT did not propagate synaptic vesicle priming or glutamatergic synapse, although mouse Efr3a has SynGO IDA/IMP rows for both from PMID:30867420 (QuickGO, checked 2026-10-20). That omission is consistent with this review removing/over-annotating the Compara transfers.
- Family review interpro/panther/PTHR12444/PTHR12444-review.yaml places EFR3A in SF1 and assesses GO:0072659 as family-wide; no disagreement with subfamily placement or with this review.

### Annotation decisions (re-checked; unchanged)
- Plasma membrane (IDA x2, EXP, IBA, IEA): ACCEPT, core location.
- Cytosol (IDA HPA, IEA SubCell): KEEP_AS_NON_CORE, minor pool.
- Protein localization to plasma membrane (IBA, IMP): ACCEPT; EFR3A itself supplies the membrane anchor of the PI4KA complex [PMID:39705356 "Fundamental to PI4KA activity is its targeted recruitment to the plasma membrane by the lipidated proteins EFR3A and EFR3B."].
- Phosphatidylinositol phosphate biosynthetic process (TAS): MODIFY to GO:0180048 PI4P biosynthetic process (verified in OLS, is a leaf, not obsolete). Participation passes on the scaffold criterion: EFR3A supplies the membrane anchorage for the PI4KA step.
- Synaptic vesicle priming (IEA Compara): REMOVE; source is a disease-model modifier effect, not participation.
- Presynapse (IEA inter-ontology), glutamatergic synapse (IEA Compara): MARK_AS_OVER_ANNOTATED.
- NEW GO:0043495 protein-membrane adaptor activity (verified in OLS; definition "brings together a protein or a protein complex with a membrane ... to establish or maintain the localization"): retained. No GO CC term exists for the PI4KA-EFR3-TTC7-FAM126 complex (OLS search), so no complex membership term is proposed.

### Literature added
- PMID:24860643 (cached full text): rare EFR3A missense variants enriched in ASD [PMID:24860643 "Rare nonsynonymous mutations in EFR3A were more common among cases (16 / 2,196 = 0.73%) than matched controls (12 / 3,389 = 0.35%)"]. Supports the disease sentence of the description only.
- Recent leads not cached (fetch failed for PMID:40136694, Trybus 2025 review): EFR3A/PI4KA axis supports oncogenic KRAS membrane localization in cancer models (deep-research lead; downstream, not annotated).

### Relative to review next
- Mouse Efr3a (Q8BG67), ortholog in the same PANTHER subfamily (PTHR12444:SF1) under PAINT node PTN000278197. It has no review in the repo, and its SynGO IDA/IMP rows for synaptic vesicle priming and glutamatergic synapse (PMID:30867420) are the donor-side source of the human rows judged here.

### Modules
- modules/phosphoinositide_biosynthesis.yaml mentions Efr3 as a non-catalytic scaffold for Stt4/PI4KA (not as an annoton).
