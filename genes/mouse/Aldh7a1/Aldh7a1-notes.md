# Aldh7a1 (mouse, Q9DBF1) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

No ProtNLM2 output was opened or used.

### Setup and sources
- I ran `just fetch-gene mouse Aldh7a1`, which created the UniProt, GOA (66 rows, collapsed to 57 seeded
  annotations) and stub files.
- Deep research failed. `just deep-research-falcon mouse Aldh7a1 --fallback perplexity-lite` returned
  falcon "Exception: Failed to authenticate", and the perplexity fallback returned
  HTTP 401 insufficient_quota. No deep-research file exists, so this review uses the cached primary
  literature below, the UniProt record and my own sequence analysis.
- I re-fetched PMID:20207735 (Brocker 2010), which now has full text from PMC (it was abstract-only).
  This paper contains mouse experimental data on location.

### Experimental evidence in mouse
- **Lysine catabolism / AASA dehydrogenase (IMP).** In constitutive Aldh7a1-KO mice, the metabolites
  upstream of the ALDH7A1 step (P6C, α-AASA, pipecolic acid) build up in brain and liver
  [PMID:32969477 "three upstream lysine catabolic products (P6C, α-AASA and PIP) accumulated in
  significantly higher concentrations in brain and liver tissues of KO mice"]. A second KO study confirms
  tissue-specific changes in lysine metabolism [PMID:39661514 abstract only, "of tissues from
  Aldh7a1-deficient mice, which reveal tissue-specific differences"]. No purified mouse enzyme assay
  was found, so the mouse MF rests on substrate accumulation in vivo plus orthology to human.
- **Location (mouse tissue).** Fractionation of mouse liver and kidney found the protein in nuclei,
  mitochondria and cytosol but not in microsomes [PMID:20207735 "Subcellular fractionation of liver and
  kidney revealed ALDH7A1 localization in nuclei, mitochondria, and cytosol"]. Immunohistochemistry of
  mouse heart, liver and kidney showed cytosolic and nuclear staining. Mouse has two transcript classes,
  one with and one without the 28-aa mitochondrial presequence (isoform 1 = mALDH7A1_v2, mitochondrial;
  isoform 2 = mALDH7A1_v1, non-mitochondrial).
- **Mitochondrion (HDA).** Two large-scale mitochondrial proteomic surveys of mouse tissues
  (PMID:14651853, PMID:18614015) detected the protein.

### Inferred only (human evidence)
- Broad aldehyde dehydrogenase activity on betaine aldehyde, lipid-peroxidation aldehydes and
  medium-chain aldehydes; homotetramer; osmoprotection. Recombinant human enzyme was used
  (PMID:20207735).
- Membrane (Golgi, plasma membrane) NADH generation that inhibits COPI fission via BARS and supports
  energy homeostasis (PMID:31492851, human HeLa cells). The same mechanism supports FSP1-mediated
  ferroptosis suppression (PMID:40233740, human cells, abstract only in the cache).

### Evolutionary grounding (`Aldh7a1-bioinformatics/RESULTS.md`)
- Mouse is 88.3% identical to human P49419 across the full 539 aa. Catalytic Glu296 and Cys330 are
  conserved.
- PANTHER 19.0 places mouse in PTHR43521:SF1 along with rat, cow, chicken, Xenopus, fly, worm, plant
  ALDH7B4 and bacterial members. Human alone is in SF5. I treat this as a classification artifact.
  PAINT node PTN000192435 contains both proteins, and MGI:108186 is itself a seed for the GO:0004043
  and GO:0019477 IBDs.
- PTN000192435 carries IBDs for mitochondrion, cytosol, nucleus, Golgi membrane, plasma membrane,
  GO:0008802, GO:0004043 and GO:0019477. It has **no** IBD for ferroptosis, energy homeostasis or the
  transport-regulation terms. I read that omission as deliberate.
- **Key finding:** human Ser130 (Ser102 in isoform-2 numbering), the AMPK site that controls membrane
  recruitment in PMID:31492851/PMID:40233740, is **Arg130 in mouse** (and in rat; His in Xenopus). The
  human stress-triggered recruitment switch therefore does not transfer as such to mouse. I kept
  membrane locations as non-core inferences and did not accept the membrane-regulation processes for
  mouse.

### Decisions summary
- Core: GO:0004043 (mouse IMP plus orthology), GO:0019477 (mouse IMP), GO:0004029 (orthology),
  mitochondrion/mitochondrial matrix, cytosol.
- GO:0009063 → MODIFY to GO:0019477. GO:0016491 → MODIFY to GO:0004043/GO:0004029.
- GO:0016655 (quinone oxidoreductase) → REMOVE. This is FSP1's activity. ALDH7A1 only supplies NADH
  (see the human review notes and PMID:40233740).
- Plain transport processes (Golgi to endosome, endosome to lysosome, plasma membrane to endosome) →
  REMOVE. In human, ALDH7A1 inhibits these pathways and does not carry them out.
- Negative-regulation transport terms, energy homeostasis and ferroptosis → MARK_AS_OVER_ANNOTATED for
  mouse. The reasons are: no mouse data, the AMPK site is not conserved, and PAINT did not propagate
  these terms.
- GO:1905750: QuickGO and the GOA label call it obsolete, but OLS returns it as active. My action does
  not depend on which is right.
