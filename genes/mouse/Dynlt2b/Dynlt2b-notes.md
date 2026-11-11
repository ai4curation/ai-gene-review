# Dynlt2b (mouse, Q9CQ66) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

No ProtNLM2 files or prediction-evidence folders were consulted.

### Deep research

`just deep-research-falcon mouse Dynlt2b --fallback perplexity-lite` failed: Falcon
(Edison API) returned 403 Forbidden on authentication, and the perplexity-lite fallback
timed out after 600 s. No deep-research file exists; the review is built from the cached
full-text publications listed below.

### Evolutionary grounding

- Mouse Dynlt2b and human DYNLT2B (Q8WW35) are both in PANTHER subfamily PTHR21255:SF7
  (DYNEIN LIGHT CHAIN TCTEX-TYPE PROTEIN 2B), per `interpro/panther/PTHR21255/PTHR21255-entries.csv`
  and the UniProt PANTHER cross-reference. Human-to-mouse transfer of dynein-2 functions is
  therefore within-subfamily.
- The IBA rows come from PTN000478852, a Tctex light-chain node spanning dynein-1 (DYNLT1/3)
  and dynein-2 members; terms there (cytoplasm, cytoplasmic dynein complex, microtubule-based
  movement, dynein intermediate chain binding) are family-level.
- Chlamydomonas Tctex2b is described in PMID:26044572 as a reciprocal best BLAST match of
  TCTEX1D2 ("49% identical at 80% BLAST coverage"); its PANTHER placement was not verified,
  so nothing is transferred from it.

### Mouse experimental evidence (PMID:39827215, full text)

- 3xFLAG knock-in: TCTEX1D2 "localized along the flagella from round spermatids to elongated
  spermatids" and "was also localized in the manchette"; also in motile cilia of ventricle,
  trachea, oviduct [PMID:39827215 "TCTEX1D2 was also expressed in cilia of these tissues"].
- Testis co-IP: "TCTEX1D2 interacted not only with WDR60 and DYNLT1, but also with WDR34";
  and "TCTEX1D2 interacted with WDR63 and WDR78" (inner-arm ICs).
- Sperm fractionation: "These results showed that TCTEX1D2 is an axoneme component in mice."
- Knockout: male infertility; axoneme disorganized from step-4 spermatids; "cytoplasmic dynein 2
  complexes were disrupted in Tctex1d2−/− mice elongated spermatids"; somatic motile cilia normal.
- Not measured in mouse: retrograde IFT itself; ciliary base / MTOC / spindle pole localization.

### Decisions

- Retrograde IFT (GO:0035721) accepted as core but flagged as inferred from human (KO
  fibroblasts, PMID:26044572, PMID:29742051).
- Regulation-of-retrograde-IFT rows → MODIFY to GO:0035721 (participation not regulation), as in
  the human review. microtubule-based movement IBA → MODIFY to GO:0035721.
- cilium assembly IEA → MODIFY to sperm flagellum assembly (GO:0120316; parent motile cilium
  assembly). Comparator check (QuickGO, mouse, GO:0120316): Ift81, Bbs4, Dnali1 (inner-arm light
  chain) carry it by IMP, so IFT/axonemal-dynein components in this role are annotated to it.
- NEW: sperm flagellum (IDA), manchette (IDA, non-core), dynein light chain binding (IPI, DYNLT1
  co-IP; heterodimer structure for human ortholog PMID:38454149).
- Not added: inner dynein arm / axonemal dynein complex. Co-IP with WDR63/WDR78 is suggestive
  but does not establish stoichiometric membership; raised as a suggested question.
- Not added: male fertility / spermatogenesis process terms (organismal phenotypes).
- Dynein axonemal particle rows UNDECIDED (no experiment in any species), matching human.
