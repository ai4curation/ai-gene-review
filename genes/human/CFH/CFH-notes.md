# CFH research notes

## 2026-10-10 — ClinGen Mendelian review

The authenticated primary catalog lists CFH unchecked. HGNC:4883 and reviewed UniProt P08603 identify the intended gene. All 67 normal source assertions, two alternative-product records and 44 original reference identifier/title pairs are preserved. This review adds no annotation. The current decisions are 19 ACCEPT, 13 KEEP_AS_NON_CORE, 2 MARK_AS_OVER_ANNOTATED, 28 MODIFY, 5 UNDECIDED.

The source packet and exact lookup scope are recorded in [CFH-source-evidence.json](CFH-source-evidence.json). That file contains literal interaction identities, methods, taxa, roles, features and figure locators, plus current official term definitions and Reactome event records. It deliberately distinguishes a curated source join from a new experiment.

### Molecular synthesis and product scope

Human factor H recognizes C3b, supports factor-I-mediated C3b processing and accelerates alternative-pathway convertase decay. Factor I supplies the protease catalytic site; factor H performs noncatalytic cofactor work. The transient C3b–miniFH–FI structure uses engineered miniFH and FI-S525A, while separate biochemical assays establish cleavage. Full-length FH contains 20 CCP domains; FHL-1 shares the N-terminal seven and has a distinct short tail, without CCP19–20. The human FH/FHL-1 decay study is available as a genuine normal abstract, with its access limit retained. [PMID:28671664; PMID:21317894; PMID:8898949]

Host-polyanion recognition is a second molecular capability. Heparin experiments are informative biochemical models for heparan-sulfate recognition; they do not identify a particular proteoglycan core-protein interface. Full-length and truncated-product domain assignments remain distinct. [PMID:22471560; PMID:16612335]

### Source-specific adjudications

- C3 source products were checked literally: PRO_0000005908 is the beta chain within C3b, whereas PRO_0000005915 is C3d. A beta-chain identifier was not re-described as intact C3b or a free-chain assay.
- CRP and PTX3 support specific pentraxin-binding refinements. Native versus modified CRP, calcium, salt, concentration, immobilization and fragment context explain differences between studies; no unconditional native-CRP negative was inferred. Bovine fibromodulin and the plasma affinity/MS PTX3 record remain scoped generic associations.
- The APOE competition record is not evidence for factor-H self-binding. The distinct salt-dependent oligomerization papers retain their positive self-association assertions. [PMID:26468283; PMID:19505476; PMID:19850925]
- The acute autoimmune-encephalomyelitis experiment measures reduced inflammation and myelin loss following human-FH treatment in mice. Protection from demyelination was not equated with formation of myelin. [PMID:19299737]
- Recent work separates human MS expression/localization observations from mouse neuronal constructs and protection experiments. This supplies current intracellular-protection context, not neurogenesis or new-myelin evidence. [PMID:42686909]
- Five source-specific questions remain undecided: the exact M49 assay linkage after the streptococcal-binding correction; unresolved electronic neurogenesis and cell-development chains; and exact target records in two vesicle proteomes. Positive reports and original qualifiers remain intact.

### Authority and evidence handling

Supported generic protein associations are retained as non-core under the standing explicit [ClinGen project instruction](https://github.com/ai4curation/ai-gene-review/blob/8a69f3d2b551d632a37bfeb6217a7d667db8d51b/projects/CLINGEN_MENDELIAN.md#curation-instructions). More informative binding terms are used where partner class and assay support suffice. No source annotation is deleted or silently rewritten. PAINT ancestral-node history is not inferred from donor count or target self-reference.

Normal fetch completed before manual review. Existing main publication, Reactome and family caches were selected byte-for-byte; fresh normal variants remain separate. Genuine context-complete Falcon research timed out, and the explicit fallback returned a quota error. No synthetic provider report was written. Two missing supplemental PMIDs were fetched through the normal CLI. Optional full-text availability flags are omitted where cache availability and actual external access differ; reference assessments state both.

Short supporting quotations occur only in the review YAML and are audited across the newly authored packet, including repeats. The authoring ceiling is 25 words per source; it is not described as a repository validator rule. No primary quotations are added to these notes. Raw downloaded documents and machine records remain separately identified archival evidence.

### Independent review and remaining limits

The mechanism/product peer independently verified performed cofactor work, exact C3 processed-product identities and FH/FHL-1 boundaries. The pentraxin peer independently checked ligand forms and exact source records. Whole-gene and publication review remain separate gates; this research packet does not itself mark the campaign gene complete.

The read ledger distinguishes selected full primary sections, actual figures/legends, abstract-only access and unresolved supplements. HTTP-success challenge pages were excluded. An early incorrect PMC resource request and an initial self-pair join overcount were explicitly corrected in research receipts before candidate authoring; neither altered any cached source or biological source object.
