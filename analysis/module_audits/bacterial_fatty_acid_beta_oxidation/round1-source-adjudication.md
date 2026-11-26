# PR6136: substrate specificity and electron-transfer inference

Chain length and electron acceptor are separate dimensions. ECOLI/SALTY FadE now retain long- and medium-chain acceptor-unspecified activities in structured replacements and cores. PA0506 retains long- and medium-chain capability (C16/C18/C8, weaker C6); PA0508 retains butyryl-CoA/C4 and medium-chain capability (C6/C8). No term asserts turnover of every member of a chain class. The enterobacterial conclusions remain genetic/extract/gene-exchange inferences, distinct from PAO1 purified-protein kinetics. The PA0508 review now quotes the C4 row of Table1 directly; its C4 result takes precedence over the paper's informal medium-chain-only sentence.

## Bound cofactor versus reaction acceptor

QuickGO GO0052890 refers to reduction of a flavin and maps to EC1.3.8.-. It does not name ETF explicitly. Nevertheless, an enzyme's prosthetic FAD is not sufficient evidence for that net-acceptor classification: [IUBMB EC1.3.8.7](https://iubmb.qmul.ac.uk/enzyme/EC1/3/8/7.html) separately specifies ETF in the reaction and states “Contains FAD as prosthetic group.” [EC1.3.5.1](https://enzyme.expasy.org/EC/1.3.5.1) describes an FAD-containing complex whose reaction acceptor is quinone. Thus a reductive half-reaction does not identify the terminal acceptor.

[PMID40057486](https://pubmed.ncbi.nlm.nih.gov/40057486/) uses ferrocenium in the PAO1 kinetic assay and explicitly leaves the physiological ETF relay unproven. Its proposed membrane/compartment model is not a demonstration that ETF coupling is impossible. GO0052890 remains MODIFY as correction/generalization of an unestablished acceptor dimension, not as an is_a refinement, while donor specificity is retained. The previous rationale equating bound FAD with this term's biological essence has been removed. An ontology clarification of net acceptor versus prosthetic cofactor would be useful; no claim of an upstream issue submission is made.

## Bacillus supports a different inference

[PMID17189250](https://pubmed.ncbi.nlm.nih.gov/17189250/) links yusJ and etfAB disruptions to convergent YsiA-regulon derepression interpreted as acyl-CoA accumulation, as well as native palmitate-use defects. Together with enzyme/ETF identities and family evidence, this supports inferred ETF-linked FadE activity. Both original GO0003995 rows are now ACCEPT, and the module distinguishes this realization from the unresolved relays. A direct purified-protein transfer assay is still desirable; it is not a universal requirement for accepting inferred function. The broader mixed-family/ancestral-node scope remains unresolved because its functional branches have not been delimited.

The BACSU review now quotes the palmitate-utilization result and accurately distinguishes the immutable abstract-only cache from the independently inspected author-uploaded full text. The direct author-copy provenance remains in the existing gene source analysis. Human ACADM is not an equivalent unresolved-partner case: its known MCAD–ETF interaction does not identify the partner for every bacterial FadE. No human record was changed.

## Other review corrections

The module explains the hydratase convention: BACSU FadB's supported 2-enoyl reaction uses GO0018812, while ECOLI FadB also has curated (3E)-enoyl hydration (RHEA20724), requiring GO0004300 to cover its repertoire. SALTY FadA/FadB and PSEPK FadE descriptions now summarize biology; their earlier evidence-assessment prose is retained in notes.

The annotation-reviewer consultation independently supported the chain-preserving correction, the cofactor/acceptor distinction, and the Bacillus-specific inference. Original annotation payloads and source files are checked separately from these scientific judgments. Full validation of the revised science passed on 2026-11-06 at frozen science commit `f063b332b1c5aa1ff7b1ac043f43586bd51819a4`; see `round1-full-validation.json`. Renewed external review, CI and actual merge remain pending.

## Validation provenance

The PTHR42803 evidence checker retains its original 47-file handoff baseline, verified against released science commit `79f177e6497c4cb7c31d4478509c4e9910c868db`. Current immutable sources remain checked against that baseline; subsequent curated review, notes and rendering updates are covered by the round1 preservation proof and renewed validation. The checker lint defects are corrected without changing its family, tree, PAINT, quotation or membership assertions. Original per-panel consultation reports are historical snapshots; the scientific adjudications above supersede their earlier Bacillus acceptor assessment.
