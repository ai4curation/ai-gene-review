# egl-46 (C. elegans) review notes

## Provenance and method

- Automated deep research was not available for this review: no FutureHouse,
  Perplexity or OpenAI keys exist in this environment, so `just deep-research*`
  was not run. The literature search below was done by hand.
- Queries run (2026-11-16), PubMed E-utilities:
  `("egl-46"[All Fields] OR "EGL-46"[All Fields]) AND elegans` (12 hits, all
  screened); `HSN serotonergic transcription factor collective elegans`;
  `egl-46 HSN`; `egl-46 BAG`; `insm elegans neuron`; `EGL-46 INSM1 elegans`.
  The egl-44 search for the companion review (see `../egl-44/egl-44-notes.md`)
  covered the EGL-44/EGL-46 papers too.
- Full text: PMID:29553368, PMID:29031632 and PMID:32550488 are cached in full.
  PMID:11274062, PMID:12954713, PMID:23946438, PMID:25395666, PMID:30291162,
  PMID:20923979 and PMID:2721931 are abstract-only. The PMC page of
  PMID:25395666 was read through a web-fetch tool that returns a model-written
  summary; findings from it are marked "(full text, via summary)" and are not
  quoted. That tool found no egl-46 content on the PMC page of PMID:2721931
  (a 1989 scanned article), so the WormBase row from that paper could not be
  checked.
- The UniProt fetch by gene symbol hit a UniProt rate limit (HTTP 429), so the
  gene was fetched with `--uniprot-id G5EFY4`.

## Identity and domains

- G5EFY4, 286 aa, Swiss-Prot since 2022. Three C2H2 zinc fingers in the C-terminal
  half (180-200 atypical, 208-230, 248-271); INSM1/2 family (IPR042972; PANTHER
  PTHR15065). UniProt: "Belongs to the INSM1 family." Orthologous to human INSM1
  and INSM2.
- Wu et al. defined the family: [PMID:11274062 "The product of the egl-46 gene,
  two Drosophila proteins, and two proteins in human and mice define a new family
  of zinc finger proteins."]. The "TFIIA-like" label in WormBase (and in some
  abstracts) does not match: TFIIA has no zinc fingers; C2H2 fingers are usually
  called TFIIIA-type.
- BAG allele rp4 is C185Y in the first zinc finger [PMID:32550488 "which would be
  predicted to affect DNA binding."].

## Partner and mechanism

- EGL-46 binds EGL-44 directly, through its C-terminal zinc-finger region, with the
  N-terminal TEA-domain region of EGL-44 (UniProt SUBUNIT; PMID:23946438).
- With EGL-44 it represses touch-receptor genes in FLP and represses zag-1
  [PMID:30291162 "The FLP neurons fail to activate TRN genes, however, because a
  complex of two transcriptional repressors (EGL-44/EGL-46) prevents their
  expression."]. (Full text of PMID:30291162, via summary, from the egl-44 review:
  the EMSA shows binding of EGL-44 and of the EGL-44/EGL-46 complex; whether
  EGL-46 alone binds DNA was not reported.)
- egl-46 is expressed in the touch cells, which lack EGL-44; in FLP its expression
  needs egl-44, in HSN it does not [PMID:11274062 "expression of egl-46 is
  dependent on egl-44 in the FLP cells but not in the HSN cells."].

## Neuron types and roles

- FLP versus touch fate: [PMID:11274062 "In egl-44 and egl-46 mutants, two other
  neurons, the FLP cells, express touch receptor-like features."];
  [PMID:8187641 "Mutations in seven genes either reduce (lin-14) or increase
  (lin-4, egl-44, egl-46, sem-4, ced-3 and ced-4) the number of touch
  receptor-like cells."].
- HSN serotonergic identity: EGL-46 is one of the HSN transcription factor
  collective [PMID:29553368 "Activation of the HSN transcriptome is directly
  orchestrated by a collective of six TFs."]; [PMID:29553368 "At least four genes
  matched this criteria: the POU domain TF unc-86, the Spalt-type Zn finger TF
  sem-4, the bHLH domain TF hlh-3 and the Insm-type Zn finger TF egl-46"];
  [PMID:29553368 "bas-1prom13 contains bHLH- and INSM-binding sites and
  INMS-binding site mutation, but not bHLH mutation, leads to expression defects
  which suggest a direct role for EGL-46 in robust bas-1 expression (Figure
  5F)."]; [PMID:29553368 "Loss-of-function (RNAi) experiments after HSN
  differentiation show that AST-1, UNC-86, SEM-4, EGL-46 and EGL-18 are required
  to maintain proper tph-1::yfp and cat-1::MDM2::gfp (unstable GFP) reporter
  expression."]; mouse Insm1 substitutes for egl-46 [PMID:29553368 "mouse Pet1,
  Ascl1, Insm1, Gata2 and Sall2 could respectively substitute ast-1, hlh-3,
  egl-46, egl-18 and sem-4"]. Here EGL-46 acts as an activator, and EGL-44 is
  not required in HSN for egl-46 expression.
- HSN migration and axon outgrowth: stated by WormBase and annotated by WormBase
  from PMID:11274062 (IMP), not visible in the abstract.
- Q lineage: [PMID:23946438 "The TEAD TF EGL-44, in a physical association with
  the zinc-finger TF EGL-46, instructs cell cycle exit after the terminal
  division."]; UniProt MUTAGEN: cas36 gives "production of an extra neuron from
  the Q lineage".
- HOB (male): [PMID:12954713 "male vulva location behavior and expression of
  lov-1 and pkd-2 in the ciliated sensory neuron HOB require the activities of
  transcription factor EGL-46 and to some extent also EGL-44."]; DAF-19M acts
  downstream [PMID:20923979 "In the male-specific HOB neuron, DAF-19(M) acts
  downstream of the zinc finger TF EGL-46, indicating that a TF cascade controls
  the PKD gene battery in this cell-type specific context."].
- BAG (O2/CO2 sensing): [PMID:25395666 "We report here the identification of
  EGL-46, a zinc-finger transcription factor, which regulates BAG gas-sensing fate
  in partially parallel pathways to ETS-5 and EGL-13."]. (Full text, via summary:)
  reduced gcy-9, gcy-31 and flp-19 reporter expression; reduced CO2 avoidance
  responses and a mild defect in responding to a small O2 downshift; no DNA-binding
  or cell-autonomy test.
- PVD: [PMID:29031632 "Here, we show that another MEC-3 target, the conserved
  TFIIA-like zinc finger transcription factor EGL-46, adopts the alternative role
  of specifying commissural dendrites."]; [PMID:29031632 "These results are
  consistent with a cell autonomous role for EGL-46 in PVD lateral branching and
  the conclusion that this function depends on egl-44."].

## Annotation decisions (summary)

- Core MF: Pol II DNA-binding transcription repressor activity (IBA from the INSM
  family, matching the EGL-44/EGL-46 repressor), with EGL-44 binding; the HSN
  data show it also activates serotonergic genes, so the general Pol II TF row is
  accepted too.
- `positive regulation of exit from mitosis` modified to `negative regulation of
  neuroblast proliferation`, as for egl-44. `neuroblast division` (WormBase IMP
  from PMID:2721931) is UNDECIDED: the 1989 paper could not be read and the later
  data show an extra division in mutants, which a positive division term does not
  describe.
- `detection of oxygen` and `detection of carbon dioxide` are marked
  over-annotated: EGL-46 specifies BAG identity upstream of the guanylyl cyclases
  that do the sensing.
- `axon guidance` is UNDECIDED: WormBase's own text speaks of HSN axon
  outgrowth, a different process, and the paper behind the row is abstract-only.

## WormBase and UniProt text check

- WormBase: correct on FLP fate with egl-44, nuclear expression in TRNs, ventral
  cord, FLP and HSN, egl-44 dependence in FLP but not HSN, male mating and HSN
  serotonin. Wrong or misleading: "required for ... terminal divisions of the Q
  neuroblasts" (mutants make an extra division, PMID:23946438); "TFIIA-like
  zinc-finger" family label (INSM family). Not traced: coordinated locomotion and
  touch-cell morphology and process formation. Missing: BAG, PVD and HOB/DAF-19
  roles, the HSN TF collective, and the EGL-44 complex and ZAG-1 loop.
- UniProt FUNCTION: correct and cited throughout; omits the HSN serotonergic
  role (PMID:29553368).
