# Stat1 review notes

Falcon deep research was unavailable for this corrected batch after the provider
timeout observed during the batch run; no `Stat1-deep-research-falcon.md` file
was produced. Review decisions used the cached UniProt record and publications.

Core function judgment: STAT1 is a cytokine-activated DNA-binding transcription
factor, especially in type I and type II interferon signaling. UniProt describes
STAT1 as a signal transducer and transcription activator that forms ISGF3 or GAF
complexes, enters the nucleus, binds ISRE or GAS elements, and activates
interferon-stimulated genes [UniProt:P42225 "binds to the IFN stimulated
response element"; UniProt:P42225 "binds to the IFN gamma activated sequence"].
Experimental mouse/cell evidence supports interferon-dependent activation and
transcriptional output [PMID:11972023 "Stat1 becomes phosphorylated on Y701,
dimerizes, and accumulates in the nucleus"].

Curation stance: RNA polymerase II-specific DNA-binding transcription factor
activity and regulation of DNA-templated transcription are core. JAK-STAT and
interferon pathway terms directly describe the activation context and are
retained, but immune defense, proliferation, development, apoptosis, and other
cellular response terms are kept as non-core downstream outcomes. Generic
`protein binding` and broad response/process terms are over-annotated when they
do not add mechanistic specificity.
