# CEP290 curation notes

## 2026-10-03 — initial review (primary cilium life cycle module, stage 3 transition zone)

Human CEP290 (NPHP6, BBS14) = UniProt O15078. 99 GOA annotations seeded; all reviewed.

### Deep research status

First falcon run (600 s timeout, perplexity fallback unavailable) did not complete; a `--timeout 2400` re-run was
killed (exit 137) and relaunched (outcome at the end of this file). The review is based on cached primary literature.

### Biology

- Transition-zone Y-links: [PMID:20819941 "CEP290 is located in the flagellar transition zone in close association
  with the prominent microtubule-membrane links there"; "CEP290 is required to form microtubule-membrane linkers that
  tether the flagellar membrane to the transition zone microtubules, and is essential for controlling flagellar protein
  composition"] (Chlamydomonas).
- Membrane and microtubule binding domains [PMID:24051377 "CEP290 directly binds to cellular membranes through an
  N-terminal domain that includes a highly conserved amphipathic helix motif and to microtubules through a domain
  located within its myosin-tail homology domain"].
- TZ modules and position: [PMID:28401750 "revealed the existence of three main TZ modules, MKS, NPHP and CEP290";
  "CEP290’s signal had a width close to that of the axoneme, and occupied a proximal position close to the BB and
  transition fiber markers centrin and CEP164 respectively"; satellites deliver TZ proteins: "These results suggest that,
  like CEP290, other TZ components also rely on centriolar satellites for their delivery to the TZ"].
- CP110 restrains CEP290; CEP290 needed for ciliogenesis and Rab8a recruitment [PMID:18694559 "Ablation of CEP290
  prevents ciliogenesis without affecting centrosome function or cell-cycle progression"; "Depletion of CEP290
  diminishes the localization of Rab8a to centrosomes and prevents its entry into the cilium"].
- Ciliary vesicle maturation [PMID:24421332 "Talpid3 is required for centriolar satellite dispersal, which precedes the
  formation of mature ciliary vesicles, a process requiring Cep290"].
- BBSome binding, TZ/satellite/connecting-cilium co-localization [PMID:23943788 "co-localizes with CEP290 to the
  transition zone (TZ) of primary cilia and centriolar satellites in ciliated cells, as well as to the connecting cilium
  in photoreceptor cells"].
- Nuclear pool / ATF4 [PMID:16682973 "CEP290 (also known as NPHP6) interacts with and modulates the activity of ATF4";
  "NPHP6 is found at centrosomes and in the nucleus of renal epithelial cells in a cell cycle-dependent manner and in
  connecting cilia of photoreceptors"].
- Co-purifies with Tctn1 complex [PMID:21725307 "including Mks1, Tmem216, Tmem67, Cep290, B9d1, Tctn2 and Cc2d2a"].

### Key decisions

- 30 protein binding rows: REMOVE (policy), with partner-specific notes (CP110, NPHP5, BBS4, CEP131, CCDC66 are
  biologically meaningful).
- Extracellular region + specific granule lumen (Reactome neutrophil degranulation): REMOVE — granule proteomics
  contaminant, no signal peptide.
- MKS complex (ISS): KEEP_AS_NON_CORE — co-purifies with Tctn1 complex but is a separate TZ module.
- Developmental terms (kidney, eye, hindbrain, otic vesicle, pronephros, photoreceptor development): KEEP_AS_NON_CORE.
- Positive regulation of transcription (IDA, ATF4): KEEP_AS_NON_CORE (cannot verify; not overruled).
- NOT microtubule minus-end binding: ACCEPT as stated.
- Cilium assembly IDA (PMID:26386044, a KIAA0586 paper that only references the Cep290 phenotype): ACCEPT on the
  strength of other evidence.
- Centrosome, centriole, centriolar satellite, TZ, connecting cilium, TZ assembly (GO:1905349), non-motile cilium
  assembly: ACCEPT. GO:1905349 is the replacement for obsoleted GO:0097711 (projects/CILIARY_BASAL_BODY_DOCKING_OBSOLETION.md
  lists CEP290 as Tier 1); the human IBA already uses GO:1905349, so no NEW row needed.

## HPA cilium atlas vs module role

- HPA: **Primary cilium (Approved); Basal body (Uncertain); Centrosome (Approved)**; main locations "Basal body;
  Centrosome; Mid piece". No GO_REF:0000052 row for CEP290 in GOA.
- Module role: transition-zone scaffold (stage 3, "MKS module plus CEP290"). Consistent with HPA and literature.
- Where I go beyond the module: CEP290 also acts before TZ assembly, at centriolar satellites and the mother centriole,
  in ciliary vesicle maturation and RAB8A recruitment (stage 2 boundary). core_functions therefore list two units:
  (1) TZ Y-link scaffold / TZ assembly (module role), (2) satellite/centriole scaffold for ciliary vesicle maturation and
  RAB8A recruitment. CEP290 should not be treated as an MKS-complex subunit.
