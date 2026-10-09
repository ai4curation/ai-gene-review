# CD79B evidence and annotation review — 2026-10-09

The human P40259 source contains 40 GO assertions, three alternative-product records and 28 references. Original term identifiers, evidence codes, qualifiers, interaction partners and product objects are preserved. The annotation-reviewer and core-function-synthesizer skills were applied with the ClinGen project's standing rule for supported generic protein binding. No NEW annotation is proposed.

This is manual research. A genuine isolated Falcon attempt and its explicit Perplexity-lite fallback failed during network requests and produced no research report. The manually written review and notes are not represented as provider-generated output.

## Core activity and complex context

CD79B supplies the Ig-beta chain of the BCR signaling module with CD79A. The human IgM-BCR structure directly establishes its membership alongside membrane immunoglobulin [PMID:35981043]. Human B-cell experiments demonstrate loss of surface IgM/CD79A after CD79B knockout and recovery with WT CD79B, while a heterodimerization-disrupting G137S variant fails to rescue [PMID:36426942]. Those complete authentic abstracts support the stated composition and assembly role; full structural methods, atomic contacts and complete rescue figures were not independently inspected.

The core therefore uses `contributes_to_molecular_function` for transmembrane signaling receptor activity, in the B-cell receptor complex at the plasma membrane. It does not assert autonomous antigen recognition by CD79B. Original IBA/ISS annotations already use `contributes_to`; the IEA `enables` assertion is preserved and interpreted explicitly at the complex-subunit level. The generic immune-system and signaling terms are refined to the existing BCR signaling pathway term. Broad membrane localization is refined to plasma membrane.

The external-side IBA uses `is_active_in`: the extracellular Ig-alpha/Ig-beta domains contact membrane immunoglobulin and contribute structurally to receptor assembly at that side of the membrane. The separate electronic `located_in` assertion describes the same extracellular region. They do not place the cytoplasmic ITAM outside the cell. The three source products—Long/P40259-1, Short/P40259-2 and P40259-3—are retained without inferring isoform-exclusive activities from sequence notes alone. B-cell differentiation is a downstream physiological consequence of receptor function and is kept NC.

## Exact interaction and mutation context

Four generic binding assertions have exact source-specific IntAct matches:

- PMID:25416956, CD79B–SGTA: pooled, array and validated yeast two-hybrid records support the reported pair.
- PMID:25910212, CD79B–SGTA: an unmodified pooled-interaction record is accompanied by two records marking disruption by a CD79B position137 mutation. They are not three independent positive WT validations. The earlier screen provides separate support for the pair.
- PMID:32296183, CD79B–SGTB: related HuRI pooled, array and validated Y2H records support the target pair, without assigning a chaperone activity to CD79B.
- PMID:35512704, CD79B–BRAF: split-luciferase, pull-down and BRET records explicitly annotate a BRAF position600 mutation as causing or strengthening the interaction. This supports a conditional experimental association, without establishing WT-BRAF binding in B cells or CD79B kinase activity. The precise amino-acid substitution was not independently established from the original supplemental construct data.

All four remain KEEP_AS_NON_CORE under the project rule. The database target records were inspected with their participant features; the original complete supplementary constructs and raw assay data were not reanalysed. Multiple assay records from one study and UniProt's interaction listing are not independent biological replications. The canonical caches marked full-text for the 2015 and 2022 variant screens are partial extractions, and are not treated as complete Methods/Results access.

## Other contextual annotations

The identical-protein-binding assertion is retained NC because the primary abstract explicitly includes recombinant Ig-beta cytoplasmic domains among oligomerizing ITAM-containing proteins [PMID:14967045]. This is not equated with a native CD79B homodimer replacing the physiological CD79A–CD79B heterodimer.

The exosome annotation remains NC. The abstract describes B-cell exosome proteomics, and the source-linked Vesiclepedia record specifically identifies human CD79B protein in experiment80 from that study [PMID:20458337]. The original mass-spectrometry supplement was not independently inspected; the index represents the same evidence, and study-wide western-blot methods do not establish target-specific western validation.

The original Fc-mu-receptor paper's exact CD79B-containing construct was not inspected [PMID:36949194]. Its IgM-BCR component annotation is retained using the independent human IgM-BCR structure, rather than declaring a wrong-gene citation from the title. Ten cached Reactome summaries support pathway localization; their downstream kinase, phosphatase, lipid-hydrolysis or drug-binding events do not assign those activities to CD79B.

All ten PMID identifiers and titles were independently checked against official Europe PMC MED metadata. Existing publication caches were preserved, and missing sources were obtained through the normal fetch commands. PAINT assertions are treated as ancestral-node judgments; donor count and target self-evidence are not grounds for rejection. One short quotation anchors the core composition statement; all other citations use reference identifiers and paraphrased reasoning.

Primary links: [human IgM-BCR structure](https://pubmed.ncbi.nlm.nih.gov/35981043/), [human surface-expression rescue](https://pubmed.ncbi.nlm.nih.gov/36426942/), [mutational interaction screen](https://pubmed.ncbi.nlm.nih.gov/25910212/), [cancer neo-interaction screen](https://pubmed.ncbi.nlm.nih.gov/35512704/), [cytoplasmic-domain oligomerization](https://pubmed.ncbi.nlm.nih.gov/14967045/).
