# FH (fumarate hydratase, P07954) — curation notes

## Context

Selected from projects/MITOTOL.md (section 3, "Same activity, unrelated families"), based on
Chen et al. 2026 [PMID:42822426]. That paper is computational and comparative. It is used here
only for evolutionary context, not as evidence for FH function.

## Deep research

`just deep-research-falcon human FH --fallback perplexity-lite` FAILED (2026-10-09).
- Falcon did not return before its timeout.
- The perplexity-lite fallback failed with "Provider 'perplexity' not available. Available:
  falcon, asta, openscientist".
- No deep-research file was created at review time.
- Update: the Falcon job outlived the recipe's 600 s timeout and later wrote
  `FH-deep-research-falcon.md`. It agrees with the review: cytosolic FH removes fumarate released by
  argininosuccinate lyase but does not catalyse a urea-cycle step, and nuclear FH (DNA-PK-phosphorylated
  at Thr236) binds H2A.Z at double-strand breaks, where local fumarate inhibits KDM2B to promote NHEJ.
  No annotation decisions changed.
- Literature research was done instead from the cached publications (GOA references) and PubMed
  searches. Four papers were added: PMID:11865300, PMID:16098467, PMID:22014577 and
  PMID:24280230.

## Core biology (with provenance)

- **Activity.** FH reversibly hydrates fumarate to L-malate. [PMID:30761759 "Fumarate hydratases (FHs, fumarases) catalyze the reversible conversion of fumarate into l-malate."]
  Human FH has been characterised by kinetics and by a 1.8 Å structure [PMID:30761759 "human FH (HsFH) was characterized by using enzyme kinetics"].
- **Homotetramer.** Each active site is built from residues of three subunits, so disease
  variants that break oligomerisation lose activity [PMID:29456767 "We conclude that A308T and H318Y render human fumarase enzymatically inactive via defective oligomerization."].
- **Class II (FumC-type).** The human cDNA is most similar to B. subtilis and E. coli FumC fumarases [PMID:3828494 "This protein, with the exception of an N-terminal methionine, was identified as mitochondrial fumarase."]. These are the iron-independent class II enzymes.
- **Two products from one gene.** Alternative transcription initiation gives products with and
  without the mitochondrial targeting sequence [PMID:27037871 "the FH gene encodes two gene products, one containing and one lacking the mitochondrial targeting sequence"].
  - Mitochondrial matrix / TCA cycle [PMID:27037871 "Fumarate hydratase (FH, fumarase), is a tricarboxylic acid cycle enzyme localized in the mitochondrial matrix."]
  - Cytosolic pool [PMID:20231875 "under normal conditions the FH staining pattern reflects its localization mainly to mitochondria and the cytosol."]
  - Patient mutations affect both isoenzymes [PMID:8200987 "affecting the cytosolic and the mitochondrial fumarase isoenzymes to the same degree"]
- **Cytosolic FH and the urea cycle.** FH consumes the fumarate co-product of argininosuccinate lyase (ASL).
  [PMID:27554470 "Cytosolic FH acts in the urea cycle (19), principally in liver and kidney (20) but not in adipose tissue."]
  When FH is lost, ASL runs in reverse [PMID:24280230 "Argininosuccinate was found to be produced from arginine and fumarate by the reverse activity of the urea cycle enzyme argininosuccinate lyase (ASL), making these cells auxotrophic for arginine."].
  Judgement: FH does a step on the fumarate branch (it removes ASL product), not a step of the
  ornithine-to-arginine cycle itself. Keep the urea cycle annotation as non-core. Mark arginine
  metabolic process as over-annotation, because FH acts on neither arginine nor its precursors.
- **Nuclear DNA damage response / NHEJ.**
  - Human cells: FH enters the nucleus after IR or HU [PMID:20231875 "Surprisingly, after both HU or IR treatments, FH is also localized in the nucleus, showing increasing nuclear levels over time."]. In yeast this function needs enzyme activity and can be complemented by fumarate.
  - Mechanism [PMID:26237645 "ionizing radiation induces DNA-PK-dependent phosphorylation of nuclear fumarase at Thr 236, which leads to an interaction between fumarase and the histone variant H2A.Z at DNA double-strand break (DSB) regions."]
  - Direct binding to H2A.Z [PMID:26237645 "the purified H2A.Z (NKLLG) mutant lost its binding to purified FH in vitro"]
  - FH at DSBs by ChIP [PMID:26237645 "A chromatin immunoprecipitation (ChIP) assay with antibodies against H2A.Z and FH showed that both H2A.Z and FH bound to the DNA adjacent to the I-SceI cutting site"]
  - Outcome [PMID:26237645 "These results indicate that FH-produced fumarate promotes NHEJ-dependent DNA repair by inhibiting KDM2B-mediated demethylation at DSB regions."]
  - Judgement: add NEW GO:2001034 (positive regulation of DSB repair via NHEJ) and GO:0035861
    (site of double-strand break). FH does part of the work, because its catalytic product is the
    signal. It does not join DNA ends, so a regulation term fits better than the NHEJ process term.
- **Tumour suppressor (HLRCC).** [PMID:11865300 "that this gene encodes fumarate hydratase, an enzyme of the tricarboxylic acid cycle."]
  Two oncometabolite mechanisms of fumarate:
  - HIF prolyl hydroxylase inhibition [PMID:16098467 "we show that fumarate acts as a competitive inhibitor of HPH."]
  - KEAP1 succination [PMID:22014577 "fumarate modifies cysteine residues within the Kelch-like ECH-associated protein 1 (KEAP1)"]
  These are consequences of FH loss and are not FH activities, so no GO term was proposed.
- **Thermogenesis (mouse adipose knockout).** [PMID:27554470 "In BAT, AFHKO mice show a marked decrease of UCP1 expression, hypertrophic brown adipocytes, and defective thermogenesis."]
  This is an indirect consequence of TCA failure. Positive regulation of cold-induced
  thermogenesis is marked as over-annotation.
- **Evolution (MITOTOL).** [PMID:42822426 "LECA mitochondria also contained multiple pairs of non-homologous enzymes with similar activities, such as class I and"]
  The pair is class I ([4Fe-4S], O2-sensitive) and class II fumarases. Humans retain only class II
  (FH), so the IBA for fumarate hydratase activity has no paralog or family ambiguity in human.

## Annotation decisions summary

- 59 GOA rows reviewed, plus 2 NEW.
- **MODIFY:**
  - catalytic activity → fumarate hydratase activity
  - protein binding with H2A.Z (PMID:26237645) → histone binding (GO:0042393)
- **REMOVE:** 13 generic protein-binding rows from HT Y2H screens and other large-scale screens.
- **MARK_AS_OVER_ANNOTATED:** arginine metabolic process (x2), cold-induced thermogenesis (x2), extracellular exosome.
- **KEEP_AS_NON_CORE:** urea cycle (x2).
- All other rows ACCEPT: MF, TCA, fumarate/malate metabolism, and mitochondrion/matrix/cytosol/nucleus/chromosome locations.

## 2026-10-28: ClinGen follow-up evidence audit

This entry supersedes the earlier decision summary where the decisions differ. The original notes and quotations above are preserved as session history. The current YAML and [evidence audit](FH-source-evidence.md) record the revised decisions; the [source guide](FH-source-guide.md) identifies the evidence and its limits. No new publication quotations were added.

- Exact publication-and-protein IntAct queries support the 13 formerly removed generic-binding rows. Eleven now remain non-core. Binding to PIM1 and LMNB2 is refined to protein kinase binding and lamin binding, respectively, without transferring the partner's activity to FH. The FH–EXOSC5 BioID row is proximity evidence, with independent binary evidence for the same pair from PMID:32296183. The PMID:39468017 correction concerns affiliation only.
- Arginine metabolism and cold-induced thermogenesis remain non-core contextual annotations. The actual mouse donor and human FH rescue constructs in PMID:23643539 support fumarate coupling to ASL chemistry; ASL performs the arginine conversion. PMID:27554470 supports the mouse adipose cold-challenge phenotype. Neither result establishes a universal normal-human flux direction or a dedicated temperature-sensing activity of human FH.
- Cytosolic core wording is limited to reversible fumarate/malate catalysis and the supported metabolic contexts. The artificial FH(N) deletion of residues 1–21 in PMID:26237645 is distinct from the natural P07954-2 deletion of residues 1–43. Nuclear and cytosolic localization pools are not exclusive natural-product assignments.
- The positive NHEJ-regulation proposal remains because FH performs local fumarate-producing catalysis in the reported mechanism. Comparator and GO-CAM checks are qualified in the evidence audit. The experimentally supported chromosome annotation is refined to the site of a double-strand break; the broad electronic chromosome annotation is too general. The earlier authored NEW site-of-break row is retired in place to avoid duplicate active coverage, with its complete source and quotation content retained.
- PMID:29632342 corrects duplicated Figure 2d images and reports additional repetitions. Its operative correction text was read; corrected image pixels and deposited Figshare data were not inspected. This limitation remains explicit and does not invalidate every distinct assay in the original study.
- The exosome annotation is UNDECIDED because the exact FH supplementary entry was not recovered. No contamination claim or requirement for an exosome-specific function is inferred from that gap. Broad lyase activity is too general relative to the established fumarase activity. Mitochondrial IBA is retained with direct target support, without claiming a new reconstruction of its ancestral placement.

The candidate preserves all 59 imported source contexts, both pre-existing authored NEW objects, both natural products and all 78 inherited quotation associations. There are 61 stored annotation rows and 60 active rows: 34 ACCEPT, 17 KEEP_AS_NON_CORE, 5 MODIFY, 2 TOO_GENERAL, 1 UNDECIDED and 1 NEW. Three core functions and 34 references are retained. Two genuine publication caches were added (PMID:23643539 and PMID:29632342); existing cached sources and provider research files were not edited.
