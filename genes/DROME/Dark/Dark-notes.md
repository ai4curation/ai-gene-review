# Dark notes

Dark is the Drosophila Apaf-1/CED-4 family scaffold upstream of the
initiator caspase Dronc. Its core function is not a catalytic protease
activity but assembly of a nucleotide-bound adaptor platform that recruits
Dronc through CARD/CARD and CARD/WD1 contacts, enabling Dronc
autoprocessing and downstream DrICE cleavage [PMID:21220123,
"Dark-Dronc complex cleaves DrICE"; PMID:25644603, "nearby Dark protomer
are indispensable for Dronc activation"; PMID:38381783, "the
auto-inhibited Dark monomer recruits Dronc zymogen"].

The three broad `GO:0006915 apoptotic process` rows were therefore
tightened to `GO:2001235 positive regulation of apoptotic signaling
pathway`. That term follows the same boundary used in the Dronc review:
Dark is part of the upstream activation platform that makes Dronc active,
but it does not itself execute the effector-caspase proteolysis.

Generic Dronc `GO:0005515 protein binding` rows were recast as
`GO:0050700 CARD domain binding` where the cited paper or later structural
evidence supported the interaction. Dark's WD40 repeats also contact the
Dronc CARD, so "CARD domain binding" is still informative from the Dark
side: the recognized domain is Dronc-CARD.

The review keeps several non-core developmental and cell-remodeling
contexts. Dark/Dronc is reused directly in spermatid individualization
[PMID:14737191, "inhibition of ARK"; PMID:16362035, "proper removal of
bulk cytoplasm during spermatogenesis"] and in sensory-organ precursor
patterning through caspase cleavage of Shaggy/GSK-3beta [PMID:16222340,
"is cleaved by the Dark-dependent caspase"]. These are not apoptotic
execution but they are direct uses of the same initiator module.

Salivary-gland histolysis is a careful boundary. Dark is required for the
histolytic death of larval salivary glands, but Akdemir et al. separate
that requirement from induction of the autophagic program itself
[PMID:16540507, "dark was essential for histolysis"]. The `GO:0048102
autophagic cell death` row was changed to `GO:0035070 salivary gland
histolysis` to avoid making Dark a component of autophagy.

The PMID:24746817 immune and metabolic rows were marked as over-annotations.
The cached abstract places humoral immunity, SAM-cycle, melanization,
starvation, and triglyceride phenotypes downstream of apoptosis-deficient
mutants with necrosis-driven systemic inflammation and FOXO/Gnmt energy
responses, not within the direct Dark apoptosome function [PMID:24746817,
"apoptosis-deficient mutants spontaneously develop a necrosis-driven systemic
immune response in Drosophila"; "Gnmt was cell-autonomously upregulated by
dFoxO in the fat body"].

Rows backed only by abstract-level cached evidence were otherwise kept
cautious. The PMID:16485033 RNAi screen abstract supports Dark/Dronc as
rate-limiting in several in vivo apoptosis paradigms but not the exact
salivary-gland and retinal-cell rows; PMID:16980964 does not expose
Dark-specific evidence for dendrite engulfment.
