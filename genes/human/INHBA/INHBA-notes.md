# INHBA manual review notes

## Scope and research provenance

Reviewed human INHBA (P08476), 104 seeded annotation rows, on 2026-10-25 using the review and annotation-reviewer instructions. UniProt family membership is PANTHER:PTHR11848:SF133, official label **INHIBIN BETA A CHAIN**; the precursor is 426 residues and its annotated mature chain is residues 311–426. The review preserves all seeded annotation fields and adds no NEW rows.

Automated research was unavailable: `/tmp/aigr-activin-INHBA-deep.log` records Perplexity insufficient quota, while `/tmp/aigr-activin-INHBA-falcon.log` records the failed Falcon/fallback run. No provider report was fabricated. These are manual primary-literature notes. Existing caches were read with their `full_text_available` status respected; missing receptor-structure and context sources and donor primary references were fetched through `just fetch-pmid`. Retrying PMID:21828274 did not recover full text. PMID:10320815 has neither substantive abstract nor accessible cached full text.

## Ligand composition controls the direction of action

INHBA is not synonymous with one ligand form. Its homodimer is activin A; its heterodimer with INHA is inhibin A; pairing with INHBB produces activin AB. The mature beta A chain therefore contributes to both activation and antagonism of the same receptor system.

- Human activin A engages type II activin receptor in a crystallographically resolved complex [PMID:12660162, Structures of an ActRIIB:activin A complex reveal a novel binding mode for TGF-beta ligand:receptor interactions, “The activin A dimer is linked by an interchain disulfide bond (Cys80) adjacent to the disordered wrist region.”].
- Inhibin uses the shared beta chain to occupy ActRII while preventing productive type I receptor recruitment [PMID:7890768, Inhibin antagonizes inhibition of liver cell growth by activin by a dominant-negative mechanism, “Inhibin also binds to ActRII through its beta subunit, competes with the binding of activin to ActRII, but fails to form the ActRII.SKR2 complex.”]. Betaglycan promotes the antagonist assembly (PMID:10746731). The protein-sequestering activity is a contribution of INHBA in inhibin A, not a reversal of the observation that follistatin sequesters activin.
- Activin A promotes FSH secretion; inhibin A suppresses it (PMID:2575216, PMID:3267209, PMID:11279126). Both directional annotations are retained. Generic FSH regulation is refined to both directions.

The core synthesis records activin cytokine activity, inhibin-associated receptor sequestration and endocrine FSH regulation. Peripheral developmental, immune, cardiac and erythroid outputs are distinguished from these biochemical roles.

## Receptor and tissue context

Canonical activin A signaling commonly recruits ACVR1B/ALK4 and activates SMAD2/3. Wild-type ACVR1/ALK2 can instead participate in a nonsignaling activin/type II receptor complex that competes with BMP signaling (PMID:26333933). The FOP ACVR1 R206H response is a mutant gain of responsiveness and is not canonical wild-type activation. This also avoids repeating the confusing ligand naming in the UniProt SUBUNIT paragraph.

PMID:34948289 reports ALK1/SMAD1/5/9-dependent osteoblastic responses in Saos2 and NOS1 human osteosarcoma-derived models. These are not a demonstration that all normal human osteoblasts, or all activin targets, use that route. No new bone or alternative-receptor annotation was added from this isolated context.

Growth promotion and growth inhibition both have experimental support. HepG2 and mouse B-cell models show activin-associated growth inhibition or G1 arrest (PMID:11948405, PMID:9884026); adult rat cardiac fibroblasts show increased proliferation, differentiation, collagen expression and MAPK responses (PMID:27477354); ovarian activin genetics support a local growth-promoting pathway (PMID:17609433). These differences are target-cell biology, not contradictions to resolve by deleting one sign.

## Developmental and physiological evidence audit

Human hESC/hiPSC experiments support striatal GABAergic medium spiny neuron differentiation (PMID:25804741). The specific neuronal term refines the broader nervous-system and GABAergic-neuron annotations. Independent primary human stem-cell evidence supports definitive endoderm induction in activin/low-serum culture (PMID:16258519), even though the seeded HEB/E2A paper remains abstract-only. Mouse Inhba-null and Inhbb replacement studies support palate, tooth, hair/whisker and testicular developmental signaling (PMID:10932194); compound mutant studies support eyelid fusion (PMID:14551263). These are conserved developmental roles, not claims that every mouse phenotype is established in humans.

The source for positive ovulation regulation, PMID:17609433, establishes subfertility and increased functional corpora lutea but does not resolve the positive ovulation-specific mechanism in its abstract. Both rows are UNDECIDED. Progesterone secretion and perinuclear localization also remain unresolved because the relevant assay details are inaccessible (PMID:10932194 and PMID:8133077). No source was called a wrong gene merely because its abstract emphasized another component.

Human erythroid progenitor experiments establish increased globin transcripts and hemoglobin (PMID:1310063); primary hematopoietic cultures support erythroid commitment (PMID:15451575). Hemoglobin biosynthesis was refined to **positive regulation of hemoglobin biosynthetic process**, because INHBA supplies the signal rather than catalyzing heme or globin synthesis. This is a MODIFY of an existing claim, not a new process assertion.

The NOT wound-response row remains UNDECIDED. PMID:10320815 has no substantive accessible text; its title cannot establish or refute a negated annotation. The B9 apoptosis abstract demonstrates death after activin addition (PMID:8267637) but does not resolve the much more specific “absence of ligand” dependence-receptor pathway. That row is likewise UNDECIDED.

## Tracing imported rat and mouse assertions

QuickGO donor queries were used only to locate primary references, never as functional evidence. Rat donor P18331 and mouse donor Q04998 are explicit in the seeded supporting entities. No corresponding rat/mouse INHBA review exists in this checkout to update.

- Autophagy: PMID:27769861 shows suppression of OGD-induced autophagy by activin in PC12 cells. Refine to negative regulation of autophagy; retain functional OGD-response participation.
- Collagen, ERK, cardiac fibroblast development and angiotensin response: PMID:27477354 combines ligand treatment, follistatin, pathway inhibitors and target-cell readouts; keep these context-specific effects as non-core.
- Hypoxia: PMID:30765322 shows activin induction and ligand effects in cardiomyocytes. ACVR2B-Fc blocks multiple ligands, so its whole phenotype is not assigned specifically to activin A.
- Polymerase III: PMID:23567549 assays SMAD3-dependent protein-coding follistatin transcription, including promoter/reporter experiments. Refine the inherited claim to RNA polymerase II transcription. PMID:12702211 by itself only measures steady-state receptor mRNA and explicitly allows changes in mRNA stability; independent PMID:11948405 supplies transcription-specific support.
- FSH and cholesterol responses: PMID:19464342 measures altered subunit expression and ligand secretion after FSH or 25-hydroxycholesterol. This does not establish that INHBA protein performs a step in the responding-cell mechanism; the transferred process claims are marked over-annotated. The endocrine feedback effects on FSH secretion remain supported.
- Aldosterone: PMID:29713904 reports retinal Inhba transcript downregulation and explicitly requests functional follow-up. Marking this inherited participation claim over-annotated does not dispute the expression measurement.

## Interaction and reference limitations

Bare protein-binding entries for subunit assembly and follistatin/FSTL3 interactions are removed as uninformative, without rejecting the physical interactions. The ACVR2A interaction is refined to type II activin receptor binding. The AKT1 screen row remains UNDECIDED because the main text of PMID:35512704 does not resolve the INHBA-specific constructs, variant state or supplementary interaction record. A high-throughput interaction does not itself establish intracellular physiological INHBA signaling.

PMID:16198295 resolves activin–follistatin binding, but peptide hormone binding requires the *bound partner* to have hormone activity. The abstract does not independently establish that classification for follistatin, so the specific annotation remains UNDECIDED rather than reversing ligand and antagonist roles.

Interferon-gamma inhibition is supported independently by human Th17 assays [PMID:32409602, “IFN-γ and IL-17 protein levels were significantly decreased, while IL-10 was up-regulated in human Th17 cells differentiated in the presence of activin-A”]. The associated [correction](https://pmc.ncbi.nlm.nih.gov/articles/PMC7382228/) (PMID:32661143) adds an author affiliation; it does not revise these results. The correction was inspected online because its cached record lacks full text. Macrophage differentiation inhibition and the protein-metabolic regulatory claim remain unresolved from their available abstracts.

## Completion

Action counts: KEEP_AS_NON_CORE 32, MODIFY 17, ACCEPT 38, REMOVE 4, UNDECIDED 10, MARK_AS_OVER_ANNOTATED 3. No PENDING or NEW rows remain. Evidence quotations were checked against cached source text. Final ontology ancestry checks retained hematopoietic progenitor differentiation as non-core rather than falsely calling erythrocyte differentiation its descendant, and verified all generic-development replacements. Gene and history validation passed without warnings.
