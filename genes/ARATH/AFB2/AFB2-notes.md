# AFB2 (At3g26810; Q9LW29) curation notes

## 2026-10 review (auxin_nuclear_signaling module)

- Automated deep research (`just deep-research-falcon ARATH AFB2`) failed with HTTP 402 (Payment Required); review written from cached primary literature.
- Identity check: UniProt Q9LW29 AFB2_ARATH, AUXIN SIGNALING F-BOX 2, At3g26810. Correct protein.

### Function
- TIR1/AFB family LRR F-box auxin receptor. AFB1-3 "interact with the Aux/IAA proteins in an auxin-dependent manner" and quadruple mutants are auxin insensitive with mp/bdl-like embryos [PMID:15992545 "Like TIR1, these proteins interact with the Aux/IAA proteins in an auxin-dependent manner"].
- "TIR1 and AFB2 are the dominant auxin receptors in the seedling root" [PMID:20018756].
- Co-receptor: "TIR1 and the Aux/IAA are both necessary and sufficient for auxin binding and act as auxin co-receptors"; AFB2 forms strong Aux/IAA complexes, e.g. "IAA12 interacted specifically with TIR1 and AFB2 at 100 μM IAA" [PMID:22466420].
- Structure (TIR1): InsP6 cofactor; auxin acts as "molecular glue" [PMID:17410169] -> basis for ISS InsP6 binding / auxin binding.
- Localization: "AFB2 through AFB5 are distributed between the nucleus and the cytoplasm" [PMID:32067636]; TIR1 mostly nuclear.
- Redundancy: "functional redundancies between TIR1, AFB2, and AFB3" [PMID:32067636].

### Decisions
- Protein binding (IAA7) IPIs -> MODIFY to GO:1990756 ubiquitin-like ligase-substrate adaptor activity.
- Plant-type vacuole (HDA, vacuole proteomics PMID:17151019) -> MARK_AS_OVER_ANNOTATED.
- InsP6 binding ISS -> KEEP_AS_NON_CORE (structural cofactor).
- Core: auxin receptor activity (GO:0038198) and ligase-substrate adaptor (GO:1990756) in SCF (GO:0019005), auxin-activated signaling (GO:0009734).
