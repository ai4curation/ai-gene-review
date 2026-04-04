# BioReason-Pro RL Review: BRCA2 (human)

Source: BRCA2-deep-research-bioreason-rl.md

- **Correctness**: 4/5
- **Completeness**: 2/5

## Analysis

BioReason-Pro RL correctly identifies BRCA2 as a nuclear DNA repair assembly factor involved in homologous recombination. The core inference -- BRC repeats recruit RAD51 for strand exchange -- is the central biological truth about BRCA2. However, the analysis is notably shallow given the protein's complexity.

### What it got right

- Correctly identifies BRCA2 as a mediator of homologous recombination.
- Accurately describes the BRC repeat array as a docking platform for RAD51 recombinase.
- Correctly assigns nuclear localization (GO:0005634).
- Properly identifies GO:0006310 (DNA recombination) as the core biological process.
- Correctly describes BRCA2 as a non-enzymatic assembly factor (protein binding, not catalytic).
- The mechanistic hypothesis about RAD51 stabilization on ssDNA is accurate.

### What it got wrong or missed

- **Limited domain coverage**: BioReason only identifies two InterPro entries (IPR015525 and IPR002093). The curated review describes multiple functional domains: BRC repeats, DNA-binding domain with OB folds and tower domain, and C-terminal recombinase-binding region (CTRB). This likely reflects InterPro annotation depth rather than a BioReason limitation.
- **Missing ssDNA binding**: The curated review identifies GO:0003697 (single-stranded DNA binding) as a core molecular function -- BRCA2 directly binds ssDNA through its OB folds. BioReason only assigns protein binding.
- **Replication fork protection completely missed**: The curated review identifies a second core function: protection of stalled/reversed replication forks from MRE11-mediated nucleolytic degradation. This is genetically separable from HR and is a distinct biological role. BioReason does not mention it.
- **Missing key partner biology**: The curated review names PALB2, BRCA1-BARD1, DSS1, and RPA as key interaction partners. BioReason only generically references "recombinases and mediator complexes."
- **No disease context**: No mention of breast/ovarian cancer susceptibility, Fanconi anemia (FANCD1), HRD/PARP inhibitor sensitivity, or clinical significance.
- **Histone acetyltransferase activity in GO terms**: Notably, the BioReason GO term list includes histone acetyltransferase activity (GO:0004402) and related terms. This appears to be an InterPro2GO propagation artifact -- BRCA2 is not known to have intrinsic HAT activity. BioReason does not flag this as questionable.

### Failure modes

- **Shallow domain annotation leads to shallow functional inference**: With only two broad InterPro entries, the functional analysis cannot go beyond "BRC repeats bind RAD51." The OB fold/tower domain/CTRB regions are invisible.
- **Single-function bias**: BioReason infers one biological role. For BRCA2, the dual role in HR and replication fork protection is biologically important and clinically relevant.
- **Uncritical GO term propagation**: The GO terms section includes many terms (e.g., HAT activity) that likely come from InterPro2GO or similar automated pipelines. BioReason does not evaluate whether these are plausible.
