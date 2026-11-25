# ytcI (C0SPB0, YTCI_BACSU) curation notes

## 2026-11-02 session

### Sources and limits

- Deep research: no provider available ("Provider 'perplexity' not available. Available:
  openscientist, claude_code"; asta also unavailable). No `-deep-research-<provider>.md` written.
- UniProt: "Uncharacterized acyl--CoA ligase YtcI", EC 6.2.1.-, PE 3 (inferred from homology).
  No experimental comments; the only references are genome sequencing papers.
- PubMed: `ytcI[tiab] AND subtilis` returned no hits; no paper characterises YtcI.
- Domains/families: Pfam PF00501 AMP-binding + PF13193 AMP-binding_C, PROSITE PS00455
  AMP_BINDING, CDD cd05972 MACS_like, PANTHER PTHR43605:SF10, NCBIfam NF047394 "acyl-CoA
  synthetase MbcS".

### Key homology finding

- S. aureus MbcS (SAUSA300_2542, A0A0H2XHR6) is in PTHR43605:SF10 and NF047394 too, and is 58%
  identical to YtcI (ytcI-bioinformatics/RESULTS.md). YtcI is the only PTHR43605 / NF047394 member
  in B. subtilis 168.
- MbcS: [PMID:36806679 "purified MbcS is an ATP-dependent acyl-CoA synthetase that selectively
  catalyzes the activation of 2-methylbutyrate and isobutyrate"]; [PMID:36806679 "MbcS functions
  to convert extracellular 2-methylbutyric and isobutyric acids to their respective acyl-CoAs that
  are used by 3-ketoacyl-ACP synthase III (FabH) to initiate BCFA biosynthesis"].
- The MbcS paper notes that B. subtilis also incorporates such acids: [PMID:36806679 "it is known
  that extracellular short-chain acids, like 2-methylbutyrate (aC5), are incorporated into BCFA in
  Bacillus subtilis and S. aureus"]. This makes YtcI a candidate for that activation step in
  B. subtilis, untested.
- Other SF10 relatives: M. sedula Msed_0406 (4-hydroxybutyrate-CoA ligase, broad C2-C5) and
  P. putida PP_2213 (uncharacterised). Both characterised relatives use short-chain (<C6) acids.

### Annotation decisions (summary)

- GO:0004321 fatty-acyl-CoA synthase (IBA): REMOVE, synthase/synthetase confusion from the
  PTHR43605 root IBD PTN001944787 (sole seed RGD Acsm4, PMID:12709059 reporting ligase activity).
  GO_CENTRAL source defect as in PP_2213.
- GO:0006633 fatty acid biosynthetic process (IBA): UNDECIDED. The IBD's mammalian seeds point to
  oxidation [PMID:11470804 "acyl-CoAs produced by MACS1 and Sa protein are utilized mainly for
  oxidation."], so the node's basis does not support the term; but an independent line (MbcS
  orthology) makes a primer-supplying role in branched-chain fatty acid synthesis plausible for
  YtcI. Needs experiment. (PP_2213: MARK_AS_OVER_ANNOTATED, where no such line exists.)
- GO:0006637 acyl-CoA metabolic process (IBA): ACCEPT.
- GO:0015645 fatty acid ligase activity (IBA): ACCEPT; as precise as family evidence allows.
- GO:0031956 medium-chain fatty acid-CoA ligase (ARBA IEA): MARK_AS_OVER_ANNOTATED; ARBA
  prediction, and the characterised relatives (MbcS, Msed_0406) act on short-chain acids.
- No NEW annotations: short-chain/branched-chain activity is a homology hypothesis only.
