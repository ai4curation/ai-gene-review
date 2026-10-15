# foxd3-a (Xenopus laevis, Q9DEN4) — curation notes

Project context: `projects/NEURAL_CREST_ORIGINS.md`, Tier 1 (candidate vertebrate-specific
neural crest specifier). Homeolog: `foxd3-b` (Q9DEN3), no review in this repo.

## Identity

- FoxD3-A, aka XFD-6 / xFKH6 / FKH-6; 371 aa; forkhead (winged-helix) domain residues ~92-192.
  Intronless gene; Xenopus orthologue of zebrafish fkd6, chick CWH-3, mammalian HFH-2/genesis
  [PMID:11335115 "Xenopus FoxD3 (XFD-6) is an intron-less gene initially expressed within the Spemann organizer and later in premigratory neural crest cells"].
- Historical Xenopus papers (2001-2007) do not distinguish L/S homeologs; GOA attaches the
  experimental annotations to Q9DEN4 (foxd3-a) only. Deep research flags this explicitly
  [file:XENLA/foxd3-a/foxd3-a-deep-research-falcon.md "The historical experiments generally studied “Xenopus FoxD3/XFD-6” and did not resolve modern *X. laevis* homeologs"].
  Per project rule, noted, not "fixed" by assertion.

## Lines of evidence (project framework)

### 1. Expression
- Maternal + zygotic; organizer at gastrula, then presumptive neural crest from late gastrula,
  overlapping Zic-r1 and similar to Slug [PMID:11493569 "Expression of FoxD3 in the presumptive neural crest region starts at the late gastrula stage in a manner similar to that of Slug, and overlaps with that of Zic-r1"].
- Premigratory NC; switched off as NC migrates/differentiates (UniProt tissue specificity).
- Also expressed in pluripotent blastula animal-pole cells and lost as competence is lost
  [PMID:25931449 "Oct60, Sox3, FoxD3, and Myc expression was high in blastula-stage explants but reduced by late gastrula stages, correlating with loss of potential"].
  [PMID:30144418 "Many neural crest potency factors are first expressed in naïve blastula cells, including Snail1, Myc, Foxd3, Ets1, Ap2, and Vent2"].

### 2. Molecular activity
- Sequence-specific DNA-binding transcriptional repressor; repression needs the winged-helix
  domain [PMID:11335115 "By injections of VP16 and engrailed fusions we can demonstrate that FoxD3 acts as a negative transcriptional regulator; this repressive function strictly requires the presence of the winged helix domain"].
- Repression requires a C-terminal eh1/GEH motif that binds Groucho/TLE (Grg4 = tle4, O42478)
  [PMID:17138566 "the results indicate that FoxD3 recruitment of Groucho corepressors is essential for the transcriptional repression of target genes and induction of mesoderm in Xenopus"].
  No activation domain found [PMID:17138566 "No domains of FoxD3 were identified that were capable of activating reporter transcription"].
  eh1/GEH is ancestral to the FoxD subclass [PMID:17138566 "every vertebrate and invertebrate member of the FoxD subclass (27 proteins) contains a C-terminal sequence with high similarity to the eh1/GEH Groucho interaction motif"].
- Nuclear [PMID:17138566 "Therefore, exogenous FoxD3 is localized to the nucleus of cells competent to form mesoderm in response to FoxD3."].
- Pioneer→repressor bimodality is shown in zebrafish NC (not Xenopus)
  [PMID:30513303 "foxd3 acts globally as a pioneer factor to prime the onset of genes regulating NC specification and migration"],
  [PMID:30513303 "foxd3 then gradually switches from an activator to its well-described role as a transcriptional repressor"].
  No GO MF term for "pioneer"; not asserted here.

### 3. Direct targets / enhancers
- Negative autoregulation [PMID:11335115 "FoxD3 also inhibits its own expression, thereby acting in a negative autoregulatory loop"].
- No Xenopus ChIP/direct NC target defined. Organizer Nodal regulation is indirect (proposed
  derepression of an unknown inhibitor) [file:XENLA/foxd3-a/foxd3-a-deep-research-falcon.md "The relevant endogenous inhibitor and any direct FoxD3-bound regulatory element were **not identified** in these experiments."].
- Network position: downstream of border specifiers (Zic) and upstream of / parallel to Slug
  [PMID:11493569 "Slug induction by Zic factors requires FoxD3-related signaling"].
  Downstream of SoxE in explants [PMID:30144418 "Co-expression of either Sox9 or Sox10 could rescue the induction of the neural crest marker FoxD3"].

### 4. Gain of function
- Sufficiency (Sasai): [PMID:11493569 "When overexpressed in the embryo and in ectodermal explants, FoxD3 induces expression of neural crest markers."]
- Conflicting high-dose result (Pohl): [PMID:11335115 "Ectopic overexpression of FoxD3 leads to an enlargement of the neural plate concomitant with a failure in neural crest formation"]
  — consistent with a dose-sensitive repressor/maintenance factor (excess FoxD3 blocks NC
  progression, and overexpressing cells "do neither differentiate nor migrate").
- Chick: vertebrate FoxD3 (incl. Xenopus) induces ectopic NC; amphioxus FoxD does not
  [PMID:24252777 "whereas vertebrate FoxD3 genes induced the differentiation of ectopic NCCs when overexpressed in chick neural tube, neither amphioxus FoxD nor any other vertebrate FoxD paralogs exhibited this activity"].

### 5. Loss of function
- Dominant-negative FoxD3delN blocks NC without suppressing Sox2; rescued by Slug
  [PMID:11493569 "Attenuation of FoxD3-related signaling by a dominant-negative FoxD3 construct (FoxD3delN) inhibits neural crest differentiation in vivo without suppressing the CNS marker Sox2"].
  Caveat: dominant-negative, "FoxD3 (or its closely related factor)".
- Organizer: MO knockdown blocks axis and Nodal expression [PMID:17092955 "FoxD3 is required for Nodal expression in the Spemann organizer and this function is essential for dorsal mesoderm formation"].
- Mouse: required for epiblast/ES maintenance [PMID:12381664 "These results establish Foxd3 as a factor required for the maintenance of progenitor cells in the mammalian embryo."]
  and NC progenitor maintenance [PMID:18367558 "Foxd3 is required for maintenance of the multipotent mammalian neural crest"];
  restricts mesenchymal fates [PMID:21228004 "Foxd3 mediates a fate restriction choice for multipotent NC progenitors with loss of Foxd3 biasing NC toward a mesenchymal fate"].

### 6. Conservation / outgroups
- Amphioxus FoxD is not expressed at the neural plate border; its regulatory region drives
  mesoderm, not NC [PMID:18562679 "the regulatory region of AmphiFoxD, homologous to the vertebrate neural crest specifier FoxD3 , drives tissue-specific reporter expression in chick mesoderm, but not neural crest"].
- Protein-level innovation: N-terminal 39-aa motif [PMID:24252777 "replacement of the N-terminus of amphioxus FoxD with a 39-amino-acid segment from zebrafish FoxD3 conferred neural crest-inducing activity on amphioxus FoxD or zebrafish FoxD1"].
- Repressor activity + DNA specificity are ancestral [PMID:24252777 "Amphioxus and vertebrate (Xenopus) FoxD proteins both exhibited transcriptional repressor activity in Gal4 transactivation assays and bound to similar DNA sequences in vitro"].
  So: ancestral MF (forkhead repressor, Groucho recruitment), vertebrate-specific
  deployment (cis) + NC-inducing competence (N-terminal motif, trans).

## Network-layer placement

FoxD3 is a **neural crest specifier** (layer 3), not a border specifier: it is activated
at the border by Zic/Wnt inputs and is required for Slug induction by Zic, and it is not
expressed at the amphioxus border. It also has a **competence/multipotency** face (blastula
expression, mouse epiblast and NC progenitor maintenance), which places it at the junction
between NC specification and the retained blastula potency programme. GO process choice:
`GO:0014034 neural crest cell fate commitment` (existing IMP) is the right level for Xenopus
(covers specification + determination; Sasai describes "determination"). Mouse maintenance
data argue for `GO:0019827 stem cell population maintenance`-type annotation in mouse, but
Xenopus has no direct LOF evidence for that; raised as a question, not a NEW annotation.

The Spemann organizer / mesoderm role (Steiner 2006, Yaklichkin 2007) is real but is a
separate, earlier deployment; kept as non-core.

## Decisions summary
- MF: accept IBA/IEA DNA-binding TF; NEW GO:0001227 repressor activity (Pol II) supported by
  Yaklichkin/Pohl; protein binding (tle4) → MODIFY to GO:0001222 transcription corepressor binding.
- BP: neg reg transcription → GO:0000122 for Yaklichkin row; NC fate commitment ACCEPT (core);
  mesoderm formation KEEP_AS_NON_CORE; neurogenesis ±regulation MARK_AS_OVER_ANNOTATED
  (indirect, opposite-sign phenotypes; not where FoxD3 does work).
