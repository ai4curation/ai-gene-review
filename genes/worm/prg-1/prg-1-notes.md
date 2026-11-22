# prg-1 curation notes

## 2026-09-20 IBA re-review

Restored reported slicer/hydrolase activity as non-core; distinguished catalytic capacity from dispensability in major silencing assays. Withdrew nuclear and piRNA-processing exclusions pending role-specific adjudication, and updated outdated suggested experiments.

Evidence inspected: [PMID:22700655](https://pubmed.ncbi.nlm.nih.gov/22700655/), [PMID:34428467](https://pubmed.ncbi.nlm.nih.gov/34428467/), [PMID:22738724](https://pubmed.ncbi.nlm.nih.gov/22738724/), [PMID:18571452](https://pubmed.ncbi.nlm.nih.gov/18571452/).

Remaining questions:

- Nucleus localization and precursor-processing participation (OpenScientist queued).

The project audit records all changed row indices and decisions in `projects/IBA_REVIEW/rereview-2026-09-20/localization.yaml`.

## Focused OpenScientist incorporation, 2026-09-20

The actual nuclear-localization/piRNA-processing report was read with five primary full texts (PMID:26919432,34469728,38244197,41529195,41414669). Its two verdicts each overstate the evidence. Positive P-granule localization and an electronic cytoplasm comment are not exclusion evidence for every nuclear pool, and do not justify a NOT annotation. Nuclear localization remains UNDECIDED. PMID:41529195 supports loading-dependent perinuclear localization, without nuclear-pool quantitation.

For processing, PMID:26919432 explicitly states: "the exonuclease PARN-1 mediates 3′ trimming of piRNA precursors prior to, or independently, from PRG-1 loading". It also suggests PRG-1 or other factors might limit PARN-1, leaving a scaffold mechanism plausible but unproved. The provider's normal precursor→PRG-1→PARN-1 diagram therefore is not established by association of untrimmed RNAs in parn-1 mutants. PMID:34469728 documents protective trimming/methylation, and PMID:38244197 documents PRG-1-bound abnormal piRNA/anti-piRNA duplexes in trimming-defective mutants; neither resolves normal temporal order. GO:0034587 stays UNDECIDED with this direct mechanistic uncertainty. This does not reject noncatalytic participation as a principle, nor claim that the inherited PIWI function was lost. PMID:41414669 independently links PRG-1 RG motifs to downstream WAGO-siRNA production without impairing piRNA loading/biogenesis. The previously verified target-slicer activity remains non-core and is not erased by the report's maturation-specific 'noncatalytic' wording.
