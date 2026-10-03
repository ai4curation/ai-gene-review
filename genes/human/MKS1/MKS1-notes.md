# MKS1 curation notes

## 2026-10-03 — initial review (primary cilium life cycle module, stage 3 transition zone)

Human MKS1 = UniProt Q9NXB0. 32 GOA annotations seeded; all reviewed.

### Deep research status

The first `just deep-research-falcon human MKS1 --fallback perplexity-lite` run failed immediately with HTTP 429
(Edison/falcon rate limit) and the perplexity fallback is not available here. It was re-run with `--timeout 2400`
(outcome recorded at the end of this file). The review is based on cached primary literature.

### Biology

- Soluble B9-domain protein. Linear complex MKS1–B9D2–B9D1 [PMID:32726168 "B9D2 interacts directly with MKS1 and B9D1,
  whereas the latter two proteins do not directly interact with each other"; "we concluded that the B9D protein complex
  is composed of the linear interactions of MKS1–B9D2–B9D1"].
- Interdependent TZ localization and barrier function [PMID:32726168 "demonstrate their interdependent localization to
  the TZ"; "formation of the B9D protein complex is crucial for creating a diffusion barrier for ciliary membrane
  proteins"]. KO RPE1 cells: "Both the MKS1-KO and the B9D2-KO cell lines were moderately compromised with respect to
  ciliogenesis efficiency".
- Basal body localization and ciliogenesis [PMID:17185389 "MKS1 localized to basal bodies"; "siRNA-mediated reduction
  of Mks1 and Mks3 expression in a ciliated epithelial cell-line blocked centriole migration to the apical membrane and
  consequent formation of the primary cilium"; "Co-immunoprecipitation experiments show that wild-type meckelin and
  MKS1 interact"].
- Centrosome/cilia number and length [PMID:19515853 "MKS1 and MKS3 functions are required for ciliary structure and
  function, including a role in regulating length and appropriate number through modulating centrosome duplication"].
- Conserved TZ localization in worm [PMID:19208769 "localize to transition zones/basal bodies of sensory cilia"].
- MKS module establishes BB/TZ membrane attachment [PMID:21422230 "MKS/MKSR/NPHP proteins establish basal body/TZ
  membrane attachments before or coinciding with intraflagellar transport-dependent axoneme extension"].
- TMEM107 organizes MKS-1 recruitment in worms [PMID:26595381 "nematode TMEM-107 occupies an intermediate layer of the
  TZ-localized MKS module by organizing recruitment of the ciliopathy proteins MKS-1, TMEM-231 (JBTS20) and JBTS-14
  (TMEM237)"].
- Diseases: Meckel syndrome 1, JBTS28, BBS13.

### Key decisions

- 7 protein binding rows (TMEM67, TMEM107, B9D2 x5 sources): REMOVE per the protein-binding policy; the interactions are
  real and captured by MKS complex (ACCEPT).
- Centrosome/centriole/cytoplasm/cytosol/membrane: KEEP_AS_NON_CORE.
- Branching morphogenesis of an epithelial tube (IEA): KEEP_AS_NON_CORE (secondary to cilia defects).
- TZ, basal body, MKS complex, cilium, cilium assembly, protein localization to TZ: ACCEPT.
- No NEW terms.

## HPA cilium atlas vs module role

- HPA: **Basal body (Supported)**; main locations "Basal body; Nucleoli; Nucleoplasm". The HPA row is in GOA as
  GO:0036064 ciliary basal body IDA GO_REF:0000052 (ACCEPTED).
- Module role: MKS-module transition-zone component (stage 3). Consistent: confocal IF cannot separate the TZ from the
  basal body, and the literature places MKS1 at the TZ. The nucleolar/nucleoplasmic signal has no literature support and
  is not represented in GOA.
- core_functions follow the module role (MKS complex; TZ and basal body; cilium assembly; protein localization to TZ).

## Deep research outcome

The re-run `just deep-research-falcon human MKS1 --timeout 2400` succeeded and produced
`MKS1-deep-research-falcon.md` (2026-10-03). I read it after drafting the review. Its summary agrees with the
cached primary literature used here and changes none of the curation decisions. Annotation-level supporting quotes come
from the cached publications. The first core function also cites one sentence from the deep-research file.
