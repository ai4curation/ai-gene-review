# EcR review notes

## Session (2026-10-28)

- `just fetch-gene DROME EcR` resolved P34021 (135 GOA rows). Several publication caches were written
  as 0-byte files while the shared disk was full; re-fetched with `fetch-pmid --force`
  (22912598, 20209436, 20215472, 21423150, 21981918, 22569554, 22628309, 23160410).
- No deep-research API keys; literature synthesis is in `EcR-deep-research-manual.md`.
- Key paper PMID:22912598 read in full: CRC (ATF4) binds the 17-residue AF1 of EcR-B2 directly
  (E9K abolishes binding; CRC-R361E restores binding to E9K) and EcR-B2 drives ETH transcription in Inka cells
  [PMID:22912598 "Thus, ETH expression was strongly stimulated by ecdysone and required EcR expression in the Inka cells."].

## Decisions worth expert attention

- Located in dendrite (IMP, PMID:16210248) REMOVED: a phenotype cannot establish location, EcR is nuclear;
  the dendrite-pruning role is kept through neuron remodelling terms.
- Negative regulation of inflammatory response (IBA, LXR donors) MARK_AS_OVER_ANNOTATED: vertebrate LXR function,
  no insect data.
- Sperm individualization (PMID:9550716) UNDECIDED: abstract does not mention EcR.
- Cardioblast differentiation (PMID:16284119) UNDECIDED: abstract is about reprogramming differentiated larval
  cardiomyocytes at metamorphosis.
- Regulation of hemocyte proliferation (PMID:20688956) UNDECIDED: only an AML1-ETO suppressor phenotype in the abstract.
- Alien binding annotated as DNA-binding transcription factor binding MODIFIED to transcription corepressor binding.
- Cell-level processes executed by other machinery (cell adhesion, chitin cuticle biosynthesis, response to cocaine)
  marked over-annotated; engulfment and autophagy moved to positive-regulation terms.
- Many developmental IMP terms kept as non-core: EcR acts as a transcription factor gating these programs.
- No NEW annotations proposed (mutant-phenotype evidence alone does not meet the NEW bar).

## Ontology checks (OLS)

- GO:0004879 nuclear receptor activity is_a GO:0098531 ligand-modulated TF activity is_a GO:0003700; it is not under GO:0000981,
  so the GO:0000981 IDA row was accepted, not modified.
- GO:0035076 ecdysone receptor signaling pathway is_a ... GO:0030522; GO:0035075 response to ecdysone is not an ancestor.
- GO:0008230 ecdysone receptor holocomplex is under GO:0090575.
- GO:0035100 ecdysone binding is under GO:0005496 steroid binding and GO:0036094 small molecule binding.
