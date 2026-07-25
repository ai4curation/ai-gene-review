# ELAVL2 review notes

## Research provenance

The required Falcon deep-research attempt failed with HTTP 402, and the
configured Perplexity-lite fallback failed with HTTP 401. No provider-named
output was retained. The review instead uses reviewed UniProtKB Q12926, current
GOA, the local Reactome event, cached primary publications, and targeted manual
PubMed/PMC research. The evidence synthesis is in
`ELAVL2-deep-research-manual.md`.

## Core biology

ELAVL2 (HuB/Hel-N1) is a neural ELAV-family RNA-binding protein with three RRMs.
Human biochemical studies show that Hel-N1 binds mRNA 3'-UTRs and selects A/U-
rich RNA sequences [PMID:8158249 "can bind to the 3' untranslated region (3'
UTR) of Id mRNA, a transcript that"] [PMID:7972035 "combinatorial libraries
yielded (A+U)-rich consensus sequences for both Hel-N1"]. A family study that
explicitly includes Hel-N1 independently records AU-rich 3'-UTR recognition
[PMID:10710437 "include HuC, HuD, Hel-N1 and HuR. These proteins bind to AU-rich
elements in the"].

Human-neuron perturbation studies reveal two major downstream RNA-processing
roles. ELAVL2 reduction changes alternatively spliced transcripts
[PMID:27260404 "spliced genes resulting from haploinsufficient levels of
ELAVL2."]. A separate study shows that [PMID:37862432 "Depleting ELAVL2 in WT
neurons led to global shortening of 3'UTR"], establishing a role in distal
poly(A)-site choice and 3'-UTR lengthening. Long 3'-UTRs increase endogenous
dsRNA and tonic antiviral signaling in that experimental system, but these
immune phenotypes are treated as downstream context rather than ELAVL2's primary
molecular function.

## Annotation decisions

| GOA annotation | Decision | Rationale |
|---|---|---|
| GO:0035925 mRNA 3'-UTR AU-rich region binding, IBA | ACCEPT | Direct Hel-N1 A/U-rich 3'-UTR selection corroborates the phylogenetic inference. |
| GO:0140517 protein-RNA adaptor activity, IBA | ACCEPT | Well-curated IBA is consistent with ELAVL2's RNA binding and RNP associations. |
| GO:0003676 nucleic acid binding, IEA | MODIFY | Too broad; replace with GO:0035925. |
| GO:0003723 RNA binding, IEA | ACCEPT | Correct domain-supported parent activity. |
| GO:0003730 mRNA 3'-UTR binding, IEA | ACCEPT | Direct human Hel-N1 evidence establishes this activity. |
| GO:1990904 ribonucleoprotein complex, IEA | ACCEPT | Consistent with RNA binding and experimentally recorded IGF2BP1 association. |
| GO:0005515 protein binding, DYRK1A IPI | MARK_AS_OVER_ANNOTATED | The interaction may be genuine, but generic protein binding is not a useful function and no consequence is established. |
| GO:0005654 nucleoplasm, Reactome TAS | KEEP_AS_NON_CORE | Plausible for RNA processing, but the cached viral Reactome event does not expose ELAVL2-specific evidence. |
| GO:0003723 RNA binding, PMID:22658674 HDA | ACCEPT | Direct UV-crosslinking/mRNA-interactome capture. |
| GO:0003723 RNA binding, PMID:22681889 HDA | ACCEPT | Independent direct mRNA-bound-proteome capture. |
| GO:0005515 protein binding, IGF2BP1 IPI | MARK_AS_OVER_ANNOTATED | Interaction retained; the generic GO term is uninformative. |
| GO:0003730 mRNA 3'-UTR binding, PMID:8158249 TAS | ACCEPT | Direct Hel-N1 binding to the Id 3'-UTR. |
| GO:0006355 regulation of DNA-templated transcription, PMID:8158249 TAS | MODIFY | The paper assays binding to an mRNA encoding a transcriptional repressor, not transcription; replace with GO:0010608. |
| GO:0000381 regulation of alternative mRNA splicing, via spliceosome | NEW (IMP) | Human neuronal ELAVL2 knockdown changes alternative splicing. |
| GO:0110104 mRNA alternative polyadenylation | NEW (IMP) | Human neuronal ELAVL2 knockdown globally shortens 3'-UTRs. |

## Evidence boundaries

- The PMID:8158249 transcription row is not removed as a citation error; its
  biological essence is corrected from transcriptional to post-transcriptional
  regulation.
- PMID:17289661 is abstract-only locally and does not name ELAVL2 in the abstract.
  UniProt and GOA both map it to IGF2BP1 interaction, so the interaction is
  retained while the generic protein-binding function is marked over-annotated.
- PMID:36950384 is full text, but the ELAVL2-DYRK1A pair is exposed through the
  GOA/IntAct record rather than explained mechanistically in the paper body.
- The Reactome event focuses on dengue NS5 and spliceosomal components CD2BP2 and
  DDX23. It does not justify treating nucleoplasm as a defining ELAVL2 location.
- The two recorded UniProt isoforms differ in the RRM2-RRM3 hinge, but the cited
  functional assays do not support an isoform-specific GO assertion.

## Open questions

- Which direct ELAVL2 RNA targets account for its alternative-splicing and
  alternative-polyadenylation phenotypes in human neurons?
- Does ELAVL2 act alone at proximal poly(A) sites, or cooperatively with ELAVL3,
  ELAVL4, cleavage/polyadenylation factors, or other RNP proteins?
- What do DYRK1A phosphorylation and IGF2BP1 association do to ELAVL2 target
  selection, localization, or regulatory output?
- Do isoforms Q12926-1 and Q12926-2 differ in nuclear-cytoplasmic shuttling or in
  alternative-splicing versus 3'-UTR-lengthening activity?
