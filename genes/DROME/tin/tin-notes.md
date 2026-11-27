# tin (tinman) — curation notes

UniProt P22711 (TIN_DROME), FlyBase FBgn0004110. NK-2 class homeodomain transcription factor
(NK-4 / msh-2), the Drosophila ortholog of vertebrate Nkx2-5 (PANTHER PTHR24340:SF41).

## Provenance note

Automated deep research failed for this gene (falcon provider returned HTTP 402; OpenAI provider
returned HTTP 401). No `*-deep-research-<provider>.md` file was created. These notes are a manual
literature synthesis from cached publications (`publications/PMID_*.md`), PubMed abstracts fetched
into the cache, the UniProt record, and targeted web searches.

## Expression and upstream regulation

- First identified as msh-2: expressed in all trunk mesoderm, then restricted to dorsal mesoderm and
  finally to heart precursors [PMID:1982429 "During germband elongation all the mesodermal cells in the
  segmented part of the embryo express msh-2, but soon afterwards msh-2 becomes restricted to the dorsal
  mesoderm, which includes the primordia for the visceral musculature and the heart"].
- Three successive enhancers; the early one is a direct Twist target [PMID:9362473 "We provide evidence
  that the early-active enhancer element is a direct target of twist"].
- Dorsal restriction/maintenance requires Dpp (Smad) plus Tinman autoregulation at the same enhancer
  [PMID:9694800 "Screens for binding factors yielded Tinman itself and the Smad4 homolog Medea. We show
  that the binding and synergistic activities of Smad and Tinman proteins are critical for mesodermal
  tinman induction"].
- Wg and Dpp intersect with tin-expressing mesoderm to position the heart [PMID:12175486 "tin confers
  mesoderm-specificity to the wg/dpp response"].
- In head mesoderm, tin expression is controlled by Notch [PMID:21901108 "Tinman expression in head
  mesoderm is regulated by Notch signaling"].

## Loss-of-function phenotypes

- Heart and visceral mesoderm absent; some somatic muscles defective [PMID:7915669 "Embryos that are
  mutant for the tinman gene lack the appearance of visceral mesoderm and of heart primordia"].
- tin is required for bap activation and hence visceral mesoderm; also heart and specific body wall
  muscle founders [PMID:8101173 "In tin mutant embryos, bap expression is not activated in the dorsal
  mesoderm"; "tin is required for the formation of the heart from dorsal mesoderm and for the
  specification of founder cells for particular body wall muscles"].
- Later, cardioblast-intrinsic Tin is needed for working-myocardium vs ostial identity (represses Doc)
  and for adult heart remodeling [PMID:16987868 "This function of tin involves the repression of
  Dorsocross (Doc) T-box genes"].
- Required for all cardiogenic mesoderm including lymph gland and pericardial nephrocytes
  [PMID:15286786 "are required for the development of all cardiogenic mesoderm, including the lymph
  gland"].
- Gonadal mesoderm: tin acts in parallel with zfh-1 in dorsolateral mesoderm specification; germ-cell
  migration defects are secondary (PMID:9435287; web review of Moore et al. 1998 / Broihier et al. 1998).
- Corpora cardiaca neuroendocrine cells arise from tin+ head mesoderm and are absent in tin mutants
  [PMID:21901108 "The absence of CC precursors in twist and tinman mutants also strongly support this
  view"].
- Adult heart function: tin haploinsufficiency interacts with Cdc42; Tin regulates miR-1 [PMID:21690310].

## Direct targets / molecular mechanism

- Binds TCAAGTG-type NK-2 sites. Direct targets include tinman itself (PMID:9694800), bagpipe
  (PMID:15750188), D-mef2 cardiac enhancer [PMID:9034334 "D-mef2 expression in the developing
  Drosophila heart requires a novel upstream enhancer containing two Tinman binding sites"], pannier
  [PMID:11336505 "pannier is a direct transcriptional target of Tinman in the heart-forming region"],
  Hand (PMID:15975941), even-skipped mesodermal enhancer (PMID:12482712), Toll dorsal vessel
  enhancer (PMID:15870289), eya and stat92E (ChIP-chip, PMID:19217429).
- Cooperates with Pnr/GATA (physical interaction in cultured cells, PMID:11336505), Doc (T-box),
  dTCF and pMad as a "TF collective" on heart enhancers (PMID:22304916).

## Master regulator caveat

tin is necessary but not sufficient for heart induction. Ectopic tin alone does not make heart
outside Wg/Dpp intersections (PMID:12175486); synergy with Pannier is needed to induce ectopic
cardial cells [PMID:10572044 "co-expression of Pannier and the homeodomain protein Tinman
synergistically activate cardiac gene expression and induce cardial cells"]. Similarly, ectopic tin
alone does not expand corpora cardiaca precursors (PMID:21901108). It is best described as a
mesoderm-intrinsic competence/selector factor that combines with signal effectors.

## Curation decisions (summary)

- Core: RNA Pol II sequence-specific DNA-binding TF activity (activator) in nucleus; dorsal-mesoderm
  subdivision; cardioblast/cardiac muscle specification and differentiation; visceral mesoderm
  specification via bap.
- Indirect/non-autonomous phenotypes (salivary gland positioning, gut L/R looping, germ cell
  migration, ventral cord FMRFa neuron) marked as over-annotations: tin acts in mesoderm upstream of
  tissues that these processes depend on.
- ARBA IEA "nervous system development" removed (likely transferred from neural NK-2 paralogs such as
  Nkx2-1/Nkx2-2; no evidence tin acts in neural development).
- IEA "digestive tract development" modified to visceral muscle development (GO:0007522).
