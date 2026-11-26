# Fezf2 (Mus musculus, Q9ESP5) — curation notes

## 2026-11-26 — initial review (claude-code, Fable 5.2)

Trigger: Kroon, Sanalidou, …, Flames & Rico (2026) *Nature Neuroscience*,
"The identity gene *Fezf2* is repurposed postnatally to specify inhibitory input in an
activity-dependent manner" — DOI:10.1038/s41593-026-02515-6. **No PMID yet** (published online
2026-11-26; not indexed in PubMed at review time). The full text was extracted from the uploaded
PDF and cached as `publications/DOI_10.1038_s41593-026-02515-6.md` so that `supporting_text`
quotes validate; cite it by DOI.

### Gene gestalt

- C2H2 zinc-finger TF (Fez family), forebrain-restricted. Nuclear, sequence-specific RNAPII
  DNA-binding factor, **bifunctional** (activator GO:0001228 + repressor GO:0001227; both IDA,
  Lodato 2014 PMID:24997765). Represses Hes5 with Fezf1 (Shimizu 2010 PMID:20431123).
- **Embryonic core = selector gene** for layer-5 extratelencephalic (subcerebral / corticospinal)
  projection neurons: neuron fate determination (GO:0048664) and commitment to specific neuron type
  (GO:0021902), controlling their neurotransmitter identity and long-range connectivity
  [PMID:24997765; Chen 2005 PMID:16284245]. Rich downstream developmental annotations (forebrain/
  telencephalon/dentate-gyrus development, axon guidance/fasciculation, dendrite development,
  locomotor behaviour) — all kept `KEEP_AS_NON_CORE` as consequences of the identity program.
- Lodato 2011 (PMID:21338885) already showed that L5 projection-neuron identity set by Fezf2
  **non-cell-autonomously** shapes the laminar distribution of cortical interneurons and GABAergic
  inhibition — an embryonic precursor to the postnatal theme of the new paper.

### New finding (this paper) and how it is modelled

- **Postnatal, activity-dependent repurposing:** *Fezf2* expression is regulated by neuronal
  activity specifically in L5 ET cells (not IT / L2-3). It behaves as a **late-response gene** —
  its 2.7 kb promoter carries AP-1 (Fos/Jun) and EGR1 sites, c-Fos occupies the promoter, and Fos
  activates it [DOI:10.1038/s41593-026-02515-6, "c-Fos occupies the Fezf2 promoter and that Fezf2
  expression can be directly regulated by the IEG Fos"]. NB: this is regulation *of* Fezf2 by
  others — it is **not** a function of the FEZF2 protein, so it is not annotated on Fezf2 (it is
  captured in the description and the module/GO-CAM upstream of Fezf2).
- **New function annotated:** FEZF2 sets the **number of PV+ perisomatic inhibitory synapses** onto
  L5 ET cells. shFezf2 → mIPSC frequency −45%, Syt2+ (PV) bouton density −18%, with shRNA-resistant
  rescue; late knockdown also reduces boutons (maintenance). Added as **NEW**
  `GO:1905704 positive regulation of inhibitory synapse assembly`, qualifier
  `acts_upstream_of_or_within`, evidence IMP, cited by DOI.
  - *Why acts_upstream_of_or_within, not involved_in:* FEZF2 is a nuclear TF. It does not build the
    synapse; CDH22 and the PV interneuron do. Per the project participation test, the TF "does the
    transcriptional work", so it acts upstream. The physical synaptic participant is CDH22 (see
    `genes/mouse/Cdh22`).
- **Mechanism / effector:** FEZF2 transcriptionally controls the cell-surface cadherin **Cdh22**.
  Activity ↑ → Fos → Fezf2 (+16% at 6 h) → Cdh22 (+85%, 6–24 h); Fezf2 OE → Cdh22 +22%; shFezf2
  abolishes activity-induced Cdh22. Captured in `core_functions[2]` and in the dedicated module
  `FEZF2_CDH22_PV_INHIBITION`. Cntn6 is also activity/Fezf2-linked but its knockdown does **not**
  change inhibitory input (so no inhibitory-synapse annotation for Cntn6).
- **Open mechanism (knowledge gap):** direct vs indirect FEZF2→Cdh22 regulation is unresolved
  (the authors state "Further research is needed to determine whether FEZF2 regulates Cdh22
  expression by directly binding its promoter"). Recorded as a BIOLOGY knowledge_gap +
  suggested_experiment (FEZF2 ChIP/CUT&RUN at Cdh22).

### Source defects flagged (ortholog-transfer onto the mouse entry)

Four GOA rows on mouse Fezf2 (Q9ESP5) rest on **Drosophila Earmuff/dFezf (erm, UniProtKB:Q9VQ56)**
studies and look mis-filed from the fly ortholog:
- GO:0000976 & GO:0043565 (IDA, PMID:28245922, Janssens 2017 — fly neuroblast Hdac1/Erm). DNA-binding
  is **true** for mouse Fezf2 (independently supported by Lodato 2014 ChIP-seq), so the terms are
  kept `ACCEPT`; the **reference** is flagged `WRONG_REFERENCE` / `CHECK`.
- GO:0043697 cell dedifferentiation & GO:0050767 regulation of neurogenesis (IGI, PMID:20152183,
  Weng 2010, With/From Q9VQ56). These are the fly Earmuff phenotypes; `MARK_AS_OVER_ANNOTATED` +
  `WRONG_GENE_PRODUCT` / `CHECK` (corrected_value Q9VQ56), cause `ORTHOLOG_TRANSFER_AS_EXPERIMENTAL`.
  Confidence kept `PROBABLE` (not CONFIRMED) and requested_change `CHECK` — per the maintainer
  ruling, a wrong-gene assertion needs the whole paper read or the record itself to be obvious; the
  With/From naming the fly gene is strong record-level evidence but I did not read both full texts.

### Not done / follow-ups

- The DOI paper will get a PMID once indexed; re-point the DOI reference and re-quote if the cached
  text is replaced by a `just fetch-gene`/deep-research artifact.
- Human FEZF2 and zebrafish fezf2 (`genes/DANRE/fezf2`) are separate entries; a cross-species pass
  on the activator/repressor and the new inhibitory-wiring role would be worthwhile.
- Source defects here are exported by `just export-source-defects` for an upstream report to UniProt.
