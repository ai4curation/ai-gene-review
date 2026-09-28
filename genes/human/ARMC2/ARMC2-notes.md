# ARMC2 literature and curation notes — 2026-09-28

Root reviewed all five seeded assertions, both original normal cached abstracts, and UniProt identity/function/disease/product sections. The Seed11 import preserves the two products and all source fields. Automated falcon research with perplexity-lite fallback failed without creating a provider file. Additional normal PMID fetches 34982025 and 42272638 failed DNS once; Source43 recovered both normal caches, which were independently checked and imported byte-identically. No authored normal cache or provider report is being substituted.

## Human and mouse sperm evidence

[Coutton et al., PMID:30686508](https://pmc.ncbi.nlm.nih.gov/articles/PMC6372258/) reports five unrelated affected men and a mouse mutant with abnormal sperm flagella. Targeted main-text and Figure 1–3 captions establish a particularly useful limitation: detailed ultrastructure and marker analysis used one affected man, with fewer than ten interpretable transverse sections. Central-pair loss and absent human SPAG6 staining support an assembly/stability role. Mouse SPEF2 staining was absent. Other tested components remained detectable. The study lacked a suitable ARMC2 antibody for direct localization. These observations support the existing sperm-assembly annotations; they do not establish stable central-pair membership or a specific catalytic activity.

Read scope: complete cached abstract, PMC main-text sections on cohort, variants, expression, human ultrastructure, mouse disruption and immunofluorescence, and Figure 1–3 captions. Supplementary Methods, image pixels and supplement tables were not inspected. Cache remains abstract-only.

## Cargo mechanism in algae

[Lechtreck et al., PMID:34982025](https://pmc.ncbi.nlm.nih.gov/articles/PMC8789290/) identifies Chlamydomonas ARMC2/PF27 as an adaptor for radial-spoke transport. Tagged ARMC2 and RSP3 travel together; loss of ARMC2 prevents normal spoke transport, and after delivery the adaptor returns toward the cell body. The authors expressly leave conservation of this mechanism in other organisms open. Human central-pair defects do not prove ARMC2 is a permanent central-pair component. Read scope: official PubMed abstract and indexed original Results on ARMC2/RSP3 transport, Figure 3 caption and Table 1, tip unloading, and relevant Discussion; no full Methods or movie/image inspection.

## Broader mouse ciliary phenotype

[Giordani et al., PMID:42272638](https://www.frontiersin.org/journals/cell-and-developmental-biology/articles/10.3389/fcell.2026.1695239/full) extends the mouse phenotype to tracheal and oviductal cilia. Tracheal cilia are shorter and more often structurally abnormal; bead transport is impaired away from the ciliary border despite increased beat frequency. Oviductal cilia are shorter with reduced flow but largely preserved ultrastructure. The study also describes reduced female fecundity and uncommon laterality/hydrocephalus phenotypes. These are mouse observations, not confirmation of a human multisystem ciliopathy. Existing broad cilium organization is consistent with this evidence. Reduced RSPH1 staining and a structural interaction prediction do not demonstrate an ARMC2–RSPH1 interaction; the Discussion explicitly calls for experimental confirmation. No mammalian IFT cargo-binding activity follows automatically.

Read scope: abstract, Introduction, targeted mouse and videomicroscopy Methods, tracheal and oviductal Results/captions, fertility and laterality Results, RSPH1 Results/Figure 9 caption, and relevant Discussion. Not all Methods, figures or supplements inspected. Publisher image alt text does not consistently match adjacent captions; assessment uses original prose/captions without claiming image verification.

## PYCARD interaction

[Dowling et al., PMID:24407287](https://pubmed.ncbi.nlm.nih.gov/24407287/) is correctly identified. The available abstract and PubMed Figure 1–5 captions concern PML/ASC and inflammasomes. The specific ARMC2–PYCARD experiment or supporting table has not been recovered. This is insufficient to contradict the curator or declare a wrong-gene citation. Leave the existing IPI assertion UNDECIDED and do not assign inflammasome function.

## Annotation synthesis

The review records four ACCEPT decisions for the three sperm axoneme assembly rows and the cilium organization IBA, with one UNDECIDED interaction. PAINT source self-inclusion is valid experimental grounding, not circularity; neither IBA is challenged on donor count. No NEW rows. One core describes the established assembly role, using existing GO:0007288 and explicitly leaving the human molecular activity unresolved. Omit a guessed MF or location. Local gocams/index.tsv has no ARMC2/Q8NEN0 match. Independent all-five annotation and core consultation passed, with mammalian-versus-algal limits retained. Both requested normal references are now present; their XML full-text availability flags are preserved.

## Initial review scope

All five seeded assertions and both products are preserved. The review proposes four ACCEPT and one UNDECIDED, with no new annotation. The broad cilium organization evidence is kept distinct from proof of a human multisystem disease, and the human molecular activity and precise localization are not guessed. The normal source files and automatically generated provider-report namespace remain unchanged.

## Normal reference recovery and completion

The exact Source43 artifact supplied PMID:34982025 and PMID:42272638 with full_text_available=true and XML-extracted body content. The complete recovered abstracts and frontmatter, algal conservation passage, and mammalian interaction-prediction/experimental-confirmation passages were checked against the original reading above. Retrieval availability does not imply every Method, supplement or image was reviewed. The original two abstracts, GOA and UniProt files remain unchanged. The final review preserves all five original assertions and both products, with one core function and an explicit molecular-function knowledge gap.
