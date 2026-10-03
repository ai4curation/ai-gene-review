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


## 2026-10-03 source-specific reassessment (TMP proposal)

This section supersedes the earlier dispositions and access claims above; the original notes are preserved verbatim. The whole 20-row source projection and all four alternative products are retained. Proposed decisions are 14 ACCEPT and 6 UNDECIDED, with one extracellular biotinidase/biotin-metabolism core. No NEW assertion is proposed: the established chemistry and metabolic participation already have coverage, and incomplete localization or histone-function evidence is not a reason to manufacture an additional function.

The two BioPlex interaction rows are unresolved because the publication-specific BTD–MYO1D records were not inspected. Generic protein-binding wording and absent biological interpretation do not justify the prior over-annotation flags. The prostatic-exosome article has genuine Methods/Results in its cache, but its target-specific supplementary table was not inspected. Colostrum's broad extracellular assertion is retained on independent serum enzyme support, with its uninspected target table disclosed.

The matrix and CNS-development claims remain unresolved; neither is treated as disproven. Human organelle immunofluorescence, rat fractionation and secretion predictions must not be conflated into a demonstrated active human mitochondrial pool. The core enzyme activity remains valid independently of those compartment claims. The prior categorical CNS-role denial and reference MISCITED judgment are withdrawn because mutation-associated neurological injury does not settle developmental participation and the full source is unavailable.

The 2026 UniProt displayed product is isoform4 (523 residues), while the historical cloned sequence is the longer product (543 residues). The products' identities and sequence notes remain unchanged; old D444H numbering should not be silently transferred to the displayed product's Asp424 position. The source's RHEA:13081 is biotin-amide hydrolysis; biocytin hydrolysis is separately RHEA:77171.

### Access and provenance

The initial fixed-main audit matches all 11 local gene/source files at a23171822631d413dd046408b064f512f69fc406. Four cited Reactome reaction caches were absent both locally and at that main; the standard hosted fetch was requested for those records plus five relevant publications. No source was written by hand or overwritten. This baseline is not a future publication clearance.

The normal repository deep-research wrapper attempted falcon with perplexity-lite fallback in isolated TMP output and failed dependency resolution. The documented installed-client fallback then failed DNS. No provider research file was produced. The assessment is saved in provider-attempt-assessment.json; credential-bearing rich tracebacks were not stored or exposed. This reassessment instead uses actual cached records, bounded official primary access and two targeted independent consultations.

Source access before arrival of the normal batch: complete canonical abstracts for 16502470 and 7550325, complete cached main article for 23533145; binding source limits are recorded by the annotation consultant (28514442 general methods with target table unread, 33961781 Abstract/Introduction/Discussion only). Official publisher 7550325 access returned a subscription preview, not the complete paper. The official 7509806 abstract identifies the human serum enzyme; official 15059618/16150625 abstracts and limited indexed 16150625 sections establish the localization caveats. No figure image or localization supplement was inspected. All four official Reactome reaction summaries were inspected and distinguished from their primary supporting evidence. The local GO ontology definitions for the molecular function, metabolic process, matrix and CNS-development term were checked. No local GO-CAM index match for P43251/BTD was found; that is not a claim of global absence.

The annotation consultation checked exact PAINT node/term/donor tuples for all three IBAs and the human PTHR10609:SF14 member, without claiming a full phylogenetic tree/MSA reconstruction. PTHR10609's vanin family members have a distinct pantetheinase IBD; family breadth is not a reason to reject biotinidase inheritance. The source fields and snapshot differences are preserved.

Useful short evidence anchors are retained, repeated long reaction excerpts are shortened, and misleading mitochondrial and target-nonspecific binding excerpts are removed. The candidate quote ledger will record exact substrings and per-source budgets after the normal sources are imported. No fresh science or validation completion is claimed at this provisional stage.


### Completed normal-source recovery and final proposal

The five publication and four Reactome caches were subsequently fetched by the unchanged normal fetchers, authenticated from the hosted artifact, and exclusively imported by ROOT after a fresh absence check (import actual 1050db; receipt `tmp/BTD-reference-artifact-transport/import-receipt.json`). All nine complete cache bodies were read: the five publications are genuinely abstract-only, while the four Reactome records contain their complete normal reaction summaries. No cached body or metadata was edited.

PMID:7509806 identifies purified human serum biotinidase using protein sequence, liver cDNA and antibody recognition, providing an independent primary anchor for enzyme activity and extracellular localization. PMID:9099842 concerns an R538C-associated enzyme defect and does not establish a histone-transferase function. PMID:9654207 concerns partial deficiency; official PubMed lists an erratum (Hum Genet 1998;102(6):712) whose substantive content could not be recovered. Its reference assessment remains UNVERIFIED, and no quantitative allele-effect claim depends on it. The original notes' transferase variant percentages are not independently validated or carried into the final description/core.

The complete PMID:15059618 abstract distinguishes human nonspecific organelle immunofluorescence from rat fractionation. Its 48-kDa mitochondrial anti-BTD-reactive species lacked hydrolase/transferase activity and had unresolved identity. PMID:16150625 supports secretion predictions while leaving mitochondrial/nuclear targeting uncertain. These are reasons for explicit uncertainty about the human matrix claim, not proof of absence. Reactome's mitochondrial summaries are faithfully identified as database assertions; the unnegated broad molecular-function rows remain valid from independent human enzymology.

All 20 decisions are now written: 14 ACCEPT and six UNDECIDED (the two source-specific MYO1D interaction records, two matrix locations, exosome association and CNS development). The original source projection and four alternative products are unchanged. No additional annotation or MF core is proposed. The extracellular biotinidase core states the direct catalytic salvage step; no intrinsic histone biotinylation, mitochondrial catalysis, therapeutic mechanism or direct neural-development function is inferred.

Two independent consultations informed the proposal: `tmp/BTD-annotation-consultation/consultation.json` for rows 0–7 and exact PAINT/GOA joins, and `localization-core-consultation-bicra.json` for matrix/CNS/core distinctions. These are bounded consultations rather than whole-gene peer approval. The quote ledger records 16 exact instances versus 24 previously, with all per-source unique quoted totals at or below 25 words; the new primary core anchor is five words. The old notes remain verbatim as historical context, superseded by this source-specific reassessment.

Final normal update-status and full validation passed with zero curation warnings and computed COMPLETE. This records completion of all 20 review decisions, including the six explicit UNDECIDED outcomes; it does not imply that those biological uncertainties are resolved. The candidate remains TMP-only pending independent whole-gene review and application authorization.

## 2026-10-03 — application

ROOT independently reviewed and authorized this exact candidate. The reviewed YAML and notes were applied after preserving all three authored preimages. The prior notes remain as chronology. All 20 source assertions and four products are preserved. Fourteen decisions are ACCEPT and six UNDECIDED; the explicit evidence gaps remain. Nine normally fetched reference caches were previously imported by ROOT without overwrites. Normal canonical validation, rendering and a new standard EDIT history record are recorded in the adjacent application receipt. Existing source caches and histories were preserved.
