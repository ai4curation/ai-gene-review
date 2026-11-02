# CFAP69 (A5D8W1) curation notes

## Deep research status

- `just deep-research human CFAP69 --provider falcon` failed with an Edison client
  `Exception: Failed to authenticate`.
- `just deep-research human CFAP69 --provider perplexity` failed: `Provider 'perplexity'
  not available. Available: falcon, asta, openscientist`.
- No `*-deep-research-*.md` file exists. Literature was gathered manually: PubMed title
  search `CFAP69[Title]` (4 records) plus a search for CFAP69 with central apparatus /
  C1b / SPEF2 terms, and the cached publications. Abstract-only caches are flagged below.

## Identity

- 941 aa; armadillo-like (ARM) repeat fold, CFA69 family; PANTHER PTHR14716
  [file:human/CFAP69/CFAP69-uniprot.txt "PANTHER; PTHR14716; CILIA- AND FLAGELLA-ASSOCIATED PROTEIN 69; 1."].
- No transmembrane or catalytic domain annotated.

## Sperm flagellum (human, mouse)

- Human biallelic loss-of-function variants cause MMAF (SPGF24); CFAP69 localizes to the
  sperm midpiece [PMID:29606301 "In sperm from control individuals, we observed CFAP69 concentrated in the midpiece of the sperm flagellum"].
- Midpiece-restricted staining led the authors to suggest it is not a core axonemal
  protein [PMID:29606301 "This localization suggests that CFAP69 is unlikely to belong to the core axoneme"].
- Patient sperm lose SPEF2 staining; SPEF2 had been proposed as a partner
  [PMID:29606301 "Although mass spectrometry analysis recently suggested that SPEF2 might interact with CFAP69"].
- Cfap69 knockout males are infertile with immotile, MMAF sperm and disorganized
  flagellar components; spermatogenesis otherwise progresses
  [PMID:29606301 "no sperm were observed to be motile in Cfap69 mutant samples"];
  [PMID:29606301 "The abnormal organization of all sperm flagellum components indicates a failure of sperm flagellum development during spermiogenesis in Cfap69 knockout mice"].
- Independent human/mouse confirmation (abstract only):
  [PMID:30415212 "male Cfap69-knockout mice manifested with MMAF phenotypes"].
- Further human variant (abstract only): [PMID:37392306 "We identified a novel frameshift variant in CFAP69"].

## Central apparatus C1b projection (Tetrahymena)

- In Tetrahymena, Cfap69 co-purifies with Spef2A, Cfap246 and Adgb and its knockout
  loses the C1b projection and alters ciliary motion
  [PMID:34083607 "Mass spectrometry of the Adgb-3HA and Cfap69-3HA immunoprecipitates detected Spef2A, Cfap69, Cfap246, and Adgb in both samples"];
  [PMID:34083607 "Note a lack of a large C1b projection in CFAP69-KO and SPEF2A-coDel mutants"].
- This conflicts in part with the mammalian midpiece-restricted staining. The localization
  of mammalian CFAP69 within the axoneme has not been determined structurally; this is kept
  as an open question and no central-apparatus annotation is proposed.

## Olfactory sensory neuron cilia (mouse)

- CFAP69 is enriched in OSN cilia; OSN-specific loss speeds transduction kinetics and
  impairs a buried-food test with background odor
  [PMID:28495971 "OSNs lacking CFAP69, remarkably, displayed faster kinetics in both the on and off phases of electrophysiological responses"]
  (abstract only).
- Olfactory cilia lacking CFAP69 look morphologically normal [PMID:29606301 "the olfactory cilia lacking CFAP69 in mouse appeared morphologically normal"].
- Human olfaction in CFAP69 patients has not been tested.

## Annotation decisions (summary)

- Accept sperm midpiece, sperm axoneme assembly (acts upstream of/within), flagellated
  sperm motility.
- Non-core: olfactory behavior, response to odorant, non-motile cilium (mouse OSN).
- Positive regulation of flagellated sperm motility: MODIFY to flagellated sperm motility;
  knockout sperm lack functional flagella, which is not evidence of a regulatory role.
- Positive regulation of fertilization: over-annotation of a downstream infertility phenotype.
- Cilium / motile cilium: TOO_GENERAL given sperm midpiece and non-motile cilium.
- Cytoplasm IDA: the specific observation could not be located in the full text; UNDECIDED.
