# BioReason-Pro RL Review: HTT (human)

Source: HTT-bioreason-rl-predictions.md

- **Correctness**: 4/5
- **Completeness**: 3/5

## Functional Summary Review

The BioReason functional summary states:

> A large cytoplasmic scaffold that organizes intracellular transport by assembling multivalent protein complexes through tandem helical repeats and a C-terminal bridge module. Its architecture supports high-capacity binding and conformational switching that couples vesicle carriers to cytoskeletal systems, thereby coordinating intracellular protein trafficking pathways in human cells.

The central functional claims are supported by the current, completed curated review. HTT
is a large non-enzymatic HEAT/ARM-repeat scaffold, and motor-coupled vesicle transport
along microtubules is one of its core functions. One limited architecture error prevents
5/5 correctness: the bridge domain is central and is followed by the C-HEAT domain; it is
not a C-terminal bridge module in the full-length protein. The 2,000-residue truncation
likely made the bridge appear terminal to the model. The earlier comparison used a stale
TODO description and therefore understated how well the paragraph captures transport,
even though 4/5 remains appropriate for the domain-placement error.

The summary remains incomplete. The current review also identifies selective
macroautophagy as a core scaffold function, including assembly of ULK1, p62/SQSTM1, LC3,
and ubiquitinated cargo. It further identifies the HTT-HAP1-PCM1 ciliogenesis axis and a
role in mitotic spindle orientation in neural progenitors. These are separate core roles,
not merely peripheral autophagy annotations. Coverage of one major transport function but
omission of these other core functions supports 3/5 completeness. More specific motor and
cargo interactions (dynein/dynactin, kinesin-1, BDNF vesicles, and endolysosomes) are also
absent.

**Input caveat:** the BioReason export contains exactly 2,000 residues, whereas cached
UniProt HTT is 3,142 residues. The omitted C-terminal 1,142 residues include much of the
C-terminal HEAT-repeat architecture. This case should be stratified as a truncated-input
case in aggregate performance analysis; the scores above still evaluate only the
Functional Summary that was produced.

Comparison with interpro2go:

The curated review does not list GO_REF:0000002 among its reference IDs, suggesting no interpro2go annotations were present. BioReason's reasoning from the Huntingtin family and HEAT repeat domains is structurally sound but produces only generic functional predictions that could apply to many HEAT-repeat proteins. There is no interpro2go baseline to compare against, but BioReason's output is essentially domain-family-level inference.

## Notes on thinking trace

The trace correctly identifies HEAT repeats, armadillo folds, and the bridge domain. The mechanistic hypothesis about dynein-dynactin and kinesin interactions is plausible but speculative. The trace appropriately notes the absence of enzymatic domains.
