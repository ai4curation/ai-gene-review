# EIN2 re-review notes

## 2026-09-11 — source-aware re-review

Read all 63 annotation entries (62 source rows plus the pre-existing NEW adaptor
proposal), all 32 original publication caches, the UniProt record and the existing
Falcon synthesis. The publication fetch completed 32/32; it did not upgrade
abstract-only records. A Falcon refresh with perplexity-lite fallback was started
concurrently; its result is recorded below when available. Several files marked
full-text contain only selected sections, so the presence of that flag was not
used as evidence of seeing all experiments.

Substantive corrections:

- ABA positive regulation is retained as a non-core, tissue-dependent function.
  The abstract explicitly states: “In contrast, the ethylene response pathway
  positively regulates some aspects of ABA action that involve root growth in the
  absence of ethylene.” [PMID:10899978, *Regulation of abscisic acid signaling by
  the ethylene response pathway in Arabidopsis.*] Opposite effects during
  germination do not invalidate the positive root-growth annotation.
- Auxin transport and negative defense regulation change from REMOVE to
  UNDECIDED. The PubMed record for [PMID:9032965](https://pubmed.ncbi.nlm.nih.gov/9032965/)
  verifies the pir2/ein2 identity but does not settle the transport assay. The
  [publisher preview for PMID:16732289](https://www.nature.com/articles/ng1806)
  supplies only the abstract and captions. Ethylene-independent mlo resistance
  does not refute all EIN2 defense-regulatory effects. No wrong-gene claim is made.
- Root hair differentiation is retained as a non-core developmental process:
  the acquired specialized feature is hair positioning, supported by “combinatorial
  action of the auxin influx carrier AUX1, ETHYLENE-INSENSITIVE2 (EIN2) , and GNOM
  genes” [PMID:17084699, *Vectorial information for Arabidopsis planar polarity is
  mediated by combined AUX1, EIN2, and GNOM activity.*]. QuickGO defines
  GO:0048765 as acquisition of specialized root-hair cell features.
- Cell division is retained as non-core rather than replaced by histogenesis:
  “blocking ethylene signalling using a variety of ethylene insensitive mutants
  such as ein2 enhances the cell division defect of pxy.” [PMID:23166504,
  *Plant vascular cell division is maintained by an interaction between PXY and
  ethylene signalling.*] A tissue-limited experiment still supports its process.
- The two IBA metal-homeostasis removals change to UNDECIDED. The local
  `interpro/panther/PTHR11706/PTHR11706-paint.tsv` verifies the iron and manganese
  homeostasis IBDs at PTN000194431. It does not provide an alignment/tree-based
  demonstration of loss in the EIN2 clade. Removed unsupported source labels and
  confident divergence metadata; recorded the traced node as unresolved.
- A newly verified and automatically cached primary study is directly relevant:
  “The results obtained clearly support the participation of ET and NO, through
  EIN2, in the regulation of the Fe acquisition genes FRO2 and IRT1.”
  [PMID:33573082, *Comparative Study of Several Fe Deficiency Responses in the
  Arabidopsis thaliana Ethylene Insensitive Mutants ein2-1 and ein2-5.*]
  DOI 10.3390/plants10020262 was resolved through Europe PMC. The mutants retain
  iron-deficiency gene induction but show altered hormone responses. This supports
  regulatory participation, not direct transport, and means an ethylene role
  cannot be used to categorically exclude iron-homeostasis biology. The same
  source's Introduction explicitly reports that heterologous EIN2 metal transport
  has not been detected; the IEA transport removals are retained as unsupported
  family-domain transfers, not claims of experimentally proven loss in all contexts.
- Existing mRNA/P-body MODIFY decisions now cite exact targeted evidence from
  PMID:26496607, which states that ethylene induces EIN2 to associate with 3' UTRs
  and target EBF1/2 mRNA to P-bodies. Interactome abstracts are not represented as
  demonstrating 3'-UTR specificity. Nuclear localization in the translation-paper
  rows is corroborated explicitly with PMID:22936567. The inaccessible cytoplasm
  experiment in PMID:25843012 remains UNDECIDED.
- Fungus-to-oomycete MODIFY is retained for PMID:17513501 because the source
  explicitly calls Pythium irregulare an oomycete. The partial cached text does
  not independently verify the EIN2 mutant panel, which is retained from GOA.

QuickGO API definitions checked on this date: GO:0002229, GO:0035591,
GO:0003730, GO:0000932, GO:0048765. No GOA-sourced fields were changed.
The adaptor synthesis is supported by CTR1/EIN2 interactions (PMID:23132950),
EIN2 association with RNA and P-body factors (PMID:26496607), and EIN2/ENAP1
interaction (PMID:27694846), matching the definition's coordination of signaling
partners. Nuclear chromatin and translational functions remain the core outputs.

Removed fabricated summaries presented as quotations of the Falcon report,
replaced ellipsis fragments with contiguous primary-source quotations, and added
findings only for source statements actually inspected. IEA decisions can use
mapping rationale; there is no requirement to fabricate a literature snippet for
a GO_REF. Unavailable or context-incomplete evidence remains visible in UNDECIDED
rows and source-specific reasons. Primary-source support is intentionally preferred
to quoting the secondary research report merely to satisfy a warning.

During this session a concurrent automated refresh temporarily downgraded
PMID:30630869 from partial full text to abstract-only. The coordinating reviewer
restored the prior generated cache from version control, preserving its inspected
Discussion passage and the corresponding EIN2 support. No publication text was
manually composed.

Validation: `just validate ARATH EIN2` passed after the source restoration, with
three intentionally retained warnings: fungus annotations differ because one
reference is about an oomycete and another cannot be verified; cytoplasm actions
differ because some sources establish P-bodies, another broad cytoplasm, and one
is inaccessible; no secondary research-report quotation is forced into an
annotation. `just validate-history` passed for this session's generated record.

Research refresh completed successfully with Falcon/Edison Scientific Literature
in 516.68 seconds (provider metadata); fallback was not needed. The generated
report and its artifact are preserved without manual edits. Its mechanistic
summary agrees with the primary-source core functions used here. It also points
to a 2024 preprint questioning aspects of obligatory EIN2 cleavage and candidate
HAF2/chromatin extensions. Those are research leads rather than independently
verified new evidence in this pass; no contradictory annotation removal or new
molecular activity was inferred from them. The unresolved protease/processing
question remains explicit in the review.
