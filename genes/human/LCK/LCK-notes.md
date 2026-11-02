# LCK (human, P06239) review notes

Context: ADAPTIVE_IMMUNITY project, T cell receptor trunk. Curation rules followed: activity
separated from pathway (LCK = non-membrane-spanning protein tyrosine kinase), generic
`protein binding` IPI rows replaced or removed, knockout/necessity evidence for downstream
processes treated as non-core.

## Deep research

- `just deep-research-falcon human LCK --fallback perplexity-lite` launched in background at the
  start of the session. Falcon wrote `LCK-deep-research-falcon.md` (~16 min run, 50 citations),
  but the just recipe exited non-zero ("All providers failed") because its 600 s wrapper timeout
  fired and the perplexity-lite fallback is not configured in this environment. The falcon report
  is complete and consistent with this review (zinc-dependent CD4/CD8alpha binding via Cys20/Cys23,
  Y394 activating / Y505 CSK-inhibitory, coreceptor-bound vs free LCK pools, Wei et al. 2020 PNAS).
  Annotation decisions rest on the cached publications and the UniProt record.

## Core biology (with provenance)

- Src-family non-receptor PTK; N-terminal myristoylation + palmitoylation anchor it to the inner
  leaflet of the plasma membrane [PMID:22034844 "Dual N-terminal acylation of Lck with myristate
  (N-acylation) and palmitate (S-acylation) is essential for its membrane association and function."]
- Coupled to CD4 and CD8 coreceptor tails; phosphorylates CD3 chains
  [PMID:2470098 "Last, we demonstrate directly that members of the CD3 complex, including the gamma,
  delta, and epsilon chains, as well as a putative zeta subunit, can be phosphorylated at tyrosine
  residues by the CD4/CD8.p56lck complex."]
- Phosphorylates TCR zeta ITAMs, which then recruit ZAP70 tandem SH2 domains
  [PMID:8681956 "The protein tyrosine kinase (PTK) Lck phosphorylates the zeta-chain, which in turn
  associates with another PTK, ZAP70, and stimulates its phosphorylation activity."]
- Phosphorylates and activates ZAP70; SH2 domain binds ZAP70 pY319
  [PMID:10318843 "One essential function of Lck in this process is to phosphorylate ZAP-70 and
  up-regulate its catalytic activity."]; Lck-dependent ZAP70 Y315 phosphorylation [PMID:16339550].
- Other direct substrates: LAT [PMID:16938345 "Further, the in vitro kinase assay using purified
  Lck and LAT shows that Lck directly phosphorylates LAT."], SH-PTP1/PTPN6 [PMID:8114715], magicin
  [PMID:16899217], PKD2 [PMID:19192391], TSAd [PMID:15827961].
- Regulation: CSK phosphorylates inhibitory Y505, CD45 dephosphorylates it; network reconstituted
  on membranes [PMID:24463463 "T-cell receptor (TCR) phosphorylation is controlled by a complex
  network that includes Lck, a Src family kinase (SFK), the tyrosine phosphatase CD45 and the
  Lck-inhibitory kinase Csk."]. CD45 binds Lck [PMID:14625311, PMID:8576115]. Activation-loop Y394
  dephosphorylated by PTPN22 [PMID:16461343] and DUSP22/JKAP [PMID:24714587].
- Raft translocation after TCR/CD4 co-aggregation activates Fyn [PMID:12732664].
- Mouse Lck knockout: thymic atrophy, block at DP stage [PMID:1579166] -- necessity evidence.
- Also signals from Fc gamma RIIIA/CD16 in NK cells via zeta [PMID:8478617], CD28/CTLA-4/PD-1
  tail phosphorylation (Reactome), IL-2R-linked signaling [PMID:7852312].

## Annotation decisions (summary)

- PTK activity rows (GO:0004713, GO:0004715): ACCEPT. Several EXP rows cite papers whose abstracts
  are about other kinases (v-Src 1978, KIT, Shp2, Gab2, vav); function is unambiguously correct so
  deferred to curator.
- GO:0004722 protein serine/threonine phosphatase activity (PMID:8506364): REMOVE. Paper maps
  Ser-42/Ser-59 phosphorylation OF Lck by MAPK/PKA/PKC; LCK has no phosphatase domain.
- 68 `protein binding` IPI rows: REMOVE unless paper supports an informative MF; MODIFY to
  phosphotyrosine residue binding (SH2-pY evidence: 10318843, 8798676, 7507203, 7852312) or protein
  phosphatase binding (CD45: 14625311, 8576115).
- Cytosol (Reactome TAS + IEA): KEEP_AS_NON_CORE; main site of action is cytoplasmic face of PM.
- Downstream processes (adhesion, calcium release, NKT activation, xenobiotic response, platelet
  activation, leukocyte migration, hemopoiesis): non-core or over-annotated.
- SH2 domain binding with HIV Nef (PMID:8794306): REMOVE -- the interaction is Nef proline repeat
  with Lck SH3; Nef has no SH2 domain.
- protein antigen binding (IEA, Ensembl Compara from mouse): REMOVE.
- Cannot verify from abstract: phospholipase activator activity / phospholipase binding (PMID:11606584,
  abstract only names Btk/Syk), protein kinase binding with RASA1 (PMID:8618896), CD27 signaling
  (PMID:38354704) -> UNDECIDED.

## Deep research integration (falcon)

Report: `LCK-deep-research-falcon.md` (Edison/falcon, 2026-09-30). Built mainly on three reviews
(De Sanctis 2024 Cancers PMID:39123358; Fernandez-Aguilar 2023 Biology PMID:37759563; Zhang 2023
Front Cell Dev Biol PMID:36910149) and four primary papers. DOIs were resolved to PMIDs with NCBI
esearch; the four primary papers were cached with `just fetch-pmid` (all full text).

Claim tally (~32 substantive claims): ~19 confirm the review, 5 add something new, 0 conflict,
~8 not relevant to annotation or review-only/unsupported.

### Claims adopted
- Kinase-domain-intrinsic ITAM selectivity (Lck vs Src domain swap) -> description + core_functions[0]
  supported_by [PMID:42638732 "Domain-swapping experiments further revealed that substitution of the
  Src kinase domain with that of Lck was sufficient to confer ITAM phosphorylation and trigger
  downstream TCR signaling responses, whereas exchange of adaptor domains had minimal effect."];
  new suggested question + experiment on the residues responsible.
- Free vs coreceptor-bound LCK pools -> description + CD4 receptor binding core function supported_by
  [PMID:32571924 "Our data show that free Lck has higher mobility, more Y394 phosphorylation, and higher
  kinase activity than the coreceptor-bound Lck."] (mouse OT-I hybridoma). Confirms the existing
  suggested question on free vs bound pools.
- Human partial LCK deficiency (P440S) -> description [PMID:37962568 "These findings demonstrate that
  P440S LCK spares sufficient T cell function to allow the maturation of some conventional T cells but
  not regulatory T cells-leading to intestinal inflammation."]. Necessity evidence only; no new
  process annotation.
- Zinc clasp Cys20/Cys23 with CD4/CD8alpha -> report quoted as descriptive support on the IEA
  CD4 receptor binding row (no action change).
- Report and the four primary papers added to `references` with reference_review.

### Claims not acted on
- CAR-T signaling via FYN without LCK (PMID:36696897): engineered-receptor context; reference added
  (relevance LOW), no annotation change.
- ZDHHC2/ZDHHC21 palmitoylation, Y192 ZAP70-mediated feedback on CD45 binding, PD-1/SHP-2
  dephosphorylation of Y394, LAG-3, CD5/CD2/CD44/CD146/CD160 signaling, ROS/ERK and NF-kB links:
  review-only in the report, no primary paper cited. Y192 feedback raised as a suggested question.
- Nuclear LCK pool (RAD51/BRCA1) in tumor cells: review-only; no nucleus annotation exists in GOA;
  raised as a suggested question, no NEW annotation.
- Therapeutics table (dasatinib, A-770041, etc.) and biomarker material: not relevant to GO.
- The report says nothing about the four UNDECIDED rows (phospholipase activator activity and
  phospholipase binding from PMID:11606584, protein kinase binding/RASA1 from PMID:8618896, CD27
  signaling from PMID:38354704); they remain UNDECIDED.

### Conflicts
- None with the review. All annotation decisions stand.

### Report errors detected
- "~90% kinase-domain sequence identity with Src" attributed to Karpouzou 2026; the paper says
  "60-90% sequence identity in their catalytic sites" across SFKs.
- Presents Lui 2023 as the "first detailed characterization" of human LCK deficiency; that paper itself
  discusses an earlier L341P LCK report. (Also: Lui et al. is J Exp Med 2024 issue, epub Nov 2023.)
- The 2026 Karpouzou paper is listed under "Recent Developments (2023-2024)" - cosmetic.
- No fabricated DOIs found: all seven DOIs resolved to the named papers.
