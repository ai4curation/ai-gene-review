# tbx5b (E3W6T6) notes

## Setup and provenance

- Gene fetched earlier with `just fetch-gene` on E3W6T6 (TrEMBL). That accession holds the 31 GOA rows,
  experimental and IBA. The genes were not re-fetched.
- **Deep research failed.** Edison returned 402 Payment Required and the OpenAI key is invalid. It was not
  retried. The literature below was researched by hand from the cached publications and from Europe PMC
  searches.

## Identity and origin

- 422 aa. T-box domain at residues 57-237 (PROSITE). UniProt caution: "Lacks conserved residue(s) required
  for the propagation of feature annotation". ZFIN ZDB-GENE-060601-2.
- TGD paralog of tbx5a:
  [PMID:19925885 "This duplicate gene is present in all teleost genomes whose sequence is available, suggesting it resulted from the teleost-specific genome duplication event that took place during fish evolution."]
  [PMID:23441045 "Using morpholino depletion studies, we find that tbx5b is required in the heart for embryonic survival, and influences the timing and morphogenesis of pectoral fin development."]
  The 23441045 abstract also states a phylogenetic TGD origin; that sentence contains a "~" character, so it
  is not quoted here.
- 49.2% identical to tbx5a overall (compare_pair.py) and 83% in the T-box
  [PMID:39079985 "The T-box domain of Tbx5b shares only 83% sequence identity with its Tbx5a counterpart"].
  [PMID:30532148 "There are high levels of conservation at the amino acid level in the Tbox domain between the two paralogues but there are low levels of conservation throughout the rest of the protein [10]."]

## Expression

- [PMID:19925885 "We show that tbx5b has lost the characteristic forelimb/pectoral fin expression of Tbx5 genes but has retained the eye and heart expression, partially overlapping with that of its paralogue, now referred to as tbx5a."]
- The fin result is disputed:
  [PMID:24759614 "Although we had not previously observed tbx5b expression in developing pectoral fins [16], others have recently described it in the pectoral fin bud mesenchyme of 36 hpf embryos [17]."]
- Later onset and ventricle restriction:
  [PMID:30532148 "While tbx5a is detectable through in situ hybridization as early as 14 hpf in the LPM, tbx5b is not detectable until 17 hpf [9]."]
  [PMID:30532148 "Expression in the heart is similar for both paralogues until 36 hpf, when tbx5b expression is restricted to the ventricle, whereas tbx5a expression remains in both chambers of the heart [9]."]
  [PMID:29382818 "tbx5a expression levels during heart development are higher than those of tbx5b"]

## Alleles

- A CRISPR allele: 4-bp insertion in intron 1, which causes a splicing defect, a frameshift and a PTC. It may
  be subject to NMD and so could trigger transcriptional adaptation; this was not tested.
  [PMID:30532148 "This mutation would result in a splicing error such that the first intron is not spliced from the protein, leading to a frameshift starting at amino acid 53 and a premature stop codon after 16 incorrect amino acids (Fig 1C)."]
  [PMID:30532148 "Tbx5b-/- mutants fully phenocopy the reported Tbx5b morphants[10,13]."]
- Morpholinos: translation-blocking and splice-blocking, both used in PMID:24759614, and two morpholinos in
  PMID:23441045 (ZFIN MRPHLNO-130123-3 and 130702-2).

## Function

- Heart: [PMID:30532148 "The heart fails to loop and a fluid filled edema forms surrounding the heart (Fig 1E and 1F)."]
  [PMID:30532148 "By 6 days, both mutants and morphant embryos die, possibly as a result of the severe heart defects."]
  The two copies are not redundant:
  [PMID:23441045 "Because tbx5a hypomorphic mutations are embryonic lethal, tbx5a and tbx5b functions in the heart must not be completely redundant."]
  [PMID:23441045 "simultaneous depletion of both tbx5 paralogs did not lead to more severe phenotypes, and injection of wild-type mRNA from one tbx5 paralog was not sufficient to cross-rescue phenotypes of the paralogous gene."]
- Jogging (morpholino-only): [PMID:24759614 "Similarly, tbx5b morphants displayed left as well as right and middle jogging of their linear heart tubes"]
- Fin: [PMID:24759614 "Taken together, we show that pectoral fin development has a different requirement for each of the tbx5 paralogues: tbx5a function is required for the earliest steps of initiation of fin outgrowth, whereas tbx5b functions later to ensure properly timed and sustained fin outgrowth."]
  [PMID:34756968 "We show here that loss of Tbx5b function affects initial ML directed movements so that fin field cells fail to migrate laterally but continue to converge along the AP axis."]
- Beyond the lateral plate mesoderm: [PMID:30532148 "Specifically, knockdown of tbx5b results in changes in somite size, in the differentiation of vasculature progenitors and in later patterning of trunk blood vessels."]
  This is morpholino/RNA-seq only and was not proposed as NEW.
- Swim bladder: [PMID:30532148 "Additionally, unlike their wildtype siblings, the swim bladder of Tbx5b-deficient embryos does not inflate."]
  This concerns inflation, not formation, so the NOT swim bladder development annotation from PMID:30352852
  stands.

## Annotation decisions (summary)

- ACCEPT:
  - MF (IBA/IEA). There is no direct assay of Tbx5b, but there is a conserved T-box, rescue by its own mRNA,
    and a mutant phenocopy.
  - nucleus, chromatin, regulation of transcription.
  - heart looping, heart morphogenesis, heart development.
  - pectoral fin development (copy-specific late role).
  - NOT swim bladder development.
- KEEP_AS_NON_CORE:
  - heart jogging (morpholino-only, but no contradicting mutant; tbx5a jogging rows are UNDECIDED).
  - optic nerve and retina (double morphants), cytoplasm, cell fate and pattern specification.
- MARK_AS_OVER_ANNOTATED: cardiac left ventricle formation (IBA, with a propagation_review), epithelium
  development (ARBA).
- No NEW terms. The vasculature and somite effects are morpholino-only, and possibly indirect.
