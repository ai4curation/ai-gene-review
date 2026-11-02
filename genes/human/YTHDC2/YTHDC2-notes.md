# YTHDC2 (human, Q9H6S0) review notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: reviewed as the closest experimentally characterised relative of fly CG8915
(Q9VX63). No ProtNLM2 output was opened or used. This is a review of human YTHDC2 in its
own right.

### Provenance / process

- `just fetch-gene human YTHDC2` created the folder (41 GOA rows).
- Deep research FAILED: falcon raised `Exception: Failed to authenticate`; the
  perplexity-lite fallback returned HTTP 401 `insufficient_quota`. No deep-research file
  exists. The review relies on cached primary literature read directly.
- Extra papers cached with `just fetch-pmid`: PMID:29970596, PMID:29087293,
  PMID:29360036, PMID:35058317, PMID:35305312, PMID:31799605.
- PMID:29033321 (Wojtas 2017) and PMID:28809393 (Hsu 2017) and PMID:35305312 (Li 2022) are
  abstract-only in the cache.

### Evolutionary grounding

- PANTHER: PTHR18934:SF213 "3'-5' RNA HELICASE YTHDC2" (UniProt DR line). The cached member
  inventory (`interpro/panther/PTHR18934/PTHR18934-entries.csv`) places human Q9H6S0, mouse
  B2RR83 (Ythdc2), Pongo Q5R746, Arabidopsis F4INY4 (HVT1) and fly Q9W1I2 (bgcn) in SF213.
  Mouse Ythdc2 is therefore a same-subfamily 1:1 ortholog and a valid donor for ISS/IEA
  transfers to human.
- PAINT (`PTHR18934-paint.tsv`): the only IBDs affecting human YTHDC2 sit on the deep node
  PTN008360424 (GO:0003723 RNA binding; GO:0004386 helicase activity). PAINT did NOT place
  3'-5' RNA helicase activity, m6A reader activity or any germline process at a
  YTHDC2-subfamily node; treat that as deliberate. There is an IRD (NOT GO:0004386 helicase
  activity) at PTN000433935 (taxon:7227, Drosophila), from PTN008360424: helicase activity is
  considered lost on a Drosophila branch (consistent with Bgcn being catalytically dead;
  PMID:29360036 notes Drosophilidae Bgcn "is descended from a Ythdc2 gene duplication").
- Implication for transfer to CG8915: CG8915 lacks the ankyrin (ARD) insertion and the YTH
  domain, so XRN1 recruitment (ANK-mediated, PMID:29970596, PMID:29033321) and m6A binding
  (YTH, PMID:26318451) cannot be inherited by it; only the DEAH helicase core/RNA binding
  is a plausible shared property, and whether CG8915 lies inside or outside the IRD node
  must be checked on the tree.

### What is experimentally established in HUMAN YTHDC2

1. RNA-stimulated ATPase and 3'->5' RNA helicase. Wojtas 2017 (abstract): "YTHDC2 is an
   RNA-induced ATPase with a 3'→5' RNA helicase activity" [PMID:29033321]. Saito 2022
   confirms the protein used was human: "the equivalent mutation in human YTHDC2 has been
   shown to abolish ATP hydrolysis and helicase activity in vitro (Wojtas et al. 2017)"
   [PMID:35058317]. Mouse protein also unwinds 3'-tailed duplexes [PMID:29360036].
   Morohashi 2011 measured RNA-dependent ATPase on a fragment (aa 761-1430) that lacks the
   Walker A/DEAH box (aa 216-223, 316-319) [PMID:21559518]; that particular result is
   mechanistically odd, but the activity itself is established by PMID:29033321.
2. YTH domain binds m6A RNA in vitro. ITC with the human YTH domain [PMID:26318451];
   "The YTH domain of YTHDC2 preferentially binds m6A-containing RNAs via a conserved
   hydrophobic pocket" [PMID:29970596]; W1360A abolishes preference [PMID:35058317 citing
   Xu 2015, Wojtas 2017]. Affinity is modest (Kd 8.9 uM m6A vs 61.6 uM unmodified).
3. RNA binding in cells: YTH and R3H domains both contribute to binding cellular RNAs; CRAC
   shows crosslinking to 18S rRNA near the mRNA entry/exit; co-sediments with 40S and 80S
   [PMID:29970596]. Captured in two mRNA interactome screens (HDA, PMID:22658674,
   PMID:22681889).
4. ANK repeats mediate RNA-independent interaction with XRN1 [PMID:29970596,
   PMID:29033321].
5. Localization: mostly cytoplasmic, perinuclear enrichment, "not excluded from nuclei"
   (HeLa/HEK293) [PMID:29970596]; ER co-localisation in Huh-7 [PMID:21559518]. Reactome
   places it in nucleoplasm via co-IP with ZFC3H1/PAXT (Contreras 2023, via Reactome).
6. HCV: siRNA depletion lowers HCV replicon replication; binds NS5B and CyPB
   [PMID:21559518]. Single study, non-core.

### What is established only in MOUSE (inferred for human by orthology, same subfamily)

- Required for male and female fertility; germ cells enter meiosis but keep a mixed
  mitotic/meiotic identity, attempt aberrant metaphase and die [PMID:29087293,
  PMID:29360036, PMID:28809393, PMID:29033321].
- Partner MEIOC (coiled-coil-dependent, RNA-independent) [PMID:26742488].
- m6A-pocket point mutants are FERTILE; CLIP sites are U-rich/UG-rich and do not coincide
  with m6A [PMID:35058317, PMID:35305312]. So the physiological function is
  m6A-independent; m6A binding is a real in vitro activity but not the core mechanism.
- Helicase-dead E332Q blocks meiotic prophase I progression (dominant) [PMID:35058317,
  PMID:35305312]; XRN1 enhances the weak helicase activity [PMID:35305312].
- Effects on translation are contested (Hsu 2017 enhanced TE; Saito 2022 no substantial
  effect on target translation).

### Decisions (summary)

- Core MF: 3'-5' RNA helicase activity (GO:0034458); RNA binding (GO:0003723).
- Generic helicase/RNA helicase/ATP-dependent-on-RNA rows -> MODIFY to GO:0034458.
- m6A reader rows -> KEEP_AS_NON_CORE (real in vitro, dispensable in vivo).
- Germline switching (GO:0051729) ACCEPT as core process (mouse IMP-based transfer within
  SF213). Oocyte development KEEP_AS_NON_CORE. Spermatid development
  MARK_AS_OVER_ANNOTATED: mutant cells arrest before spermatids exist, so the defect is
  upstream.
- Response to TNF / IL-1: expression-induction readouts only -> MARK_AS_OVER_ANNOTATED.
- Protein binding IPIs -> REMOVE per policy (interactions with XRN1, MEIOC are real and are
  described in core_functions text).
- NEW: GO:0043024 ribosomal small subunit binding (human CRAC + 40S co-sedimentation,
  PMID:29970596), non-core.
