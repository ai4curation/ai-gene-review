# SPG21 (maspardin) review notes

## Why this gene was selected

SPG21 is a case where the protein's *fold* asserts more than the evidence supports. Maspardin carries
an alpha/beta hydrolase (ABHD) domain, is a member of the AB hydrolase superfamily in UniProt, and sits
in Pfam PF00561 (Abhydrolase_1) - yet in twenty-five years no catalytic activity has been reported for
it, and a 2026 J Cell Biol paper still opens by calling it a protein of unknown function:
[PMID:41400694 "It is caused by mutations in the SPG21 gene, which encodes maspardin, a cytosolic
protein of unknown function that associates with the late endosomal/lysosomal membrane."] and
[PMID:41400694 "the function of the 308 amino acid protein encoded by human SPG21 (or spg21 in mice),
called maspardin, has not yet been identified."]. GOA's molecular-function content is a single
`GO:0005515 protein binding` from ten interactome screens, plus a `GO:0042609 CD4 receptor binding`
pair from 2001.

## The catalytic-residue question, checked rather than assumed

The nucleophile elbow is intact. In Q9NZD8 the sequence at residues 107-111 is G-A-S-L-G, the canonical
G-x-S-x-G motif, with Ser109 at the nucleophile position; UniProt annotates the AB hydrolase-1 domain at
residues 87-159. So this is not a case of a degenerate fold.

The rest of the triad is not. Four independent sequence analyses, spanning the original disease paper to
a 2025 structural-prediction analysis, all report that the acid and histidine partners of the triad are
absent:

- [PMID:14564668 "Although our alignment studies indicate that maspardin is clearly related to members of
  this superfamily and possesses a nucleophilic elbow and parallel β strands, it does not possess the
  catalytic triad, which suggests that it is unlikely to possess enzymatic function"]
- [PMID:20661613 "though it contains a G-X-S-X-G motif (single letter amino acid code) found in serine
  lipases, it lacks the full catalytic triad common to most"]
- [PMID:19184135 "it lacks the catalytic triad common to most α/β hydrolases, suggesting that it lacks
  enzymatic activity and might instead function as a peptide-binding module mediating protein–protein
  interactions"]
- [PMID:40833810 "However, SPG21 lacks a catalytic triad typical of most α/β hydrolases (Supplemental
  Figure S1), suggesting that it does not have enzymatic activity"]

The original CD4 paper had already framed the domain as non-catalytic and repurposed:
[PMID:11113139 "Furthermore, we demonstrate that interaction with CD4 is mediated by the noncatalytic
alpha/beta hydrolase fold domain of ACP33."]

**What is still missing, and why I have not written "pseudoenzyme" as a finding.** No assay has ever been
run. Every statement above is a sequence or structure inference, and the authors of the mouse-knockout
paper say so explicitly: [PMID:20661613 "though the presumed catalytic triad of maspardin has some
differences from other proteins in the esterase/lipase superfamily, it will be important to confirm that
it lacks enzymatic activity"]. An invertebrate comparative study hedges the same way:
[PMID:22729480 "Maspardin presents similarity to the α/β-hydrolase superfamily, but might lack enzymatic
activity and rather be involved in protein-protein interactions."]. The convergence of four independent
analyses is strong, and it is reinforced by the fact that the retained Ser109 sits inside the recurrent
pathogenic missense allele p.Ala108Pro, whose effect is protein misfolding and degradation rather than loss
of a catalysis - but converging predictions are not a negative experiment. This goes in
`suggested_questions` and `knowledge_gaps`, not into `core_functions` as an asserted pseudoenzyme call.

## What maspardin does do: RAB7A effector

Two 2025-2026 papers, from independent laboratories, converge on the same molecular description.

Bonifacino group: [PMID:40833810 "Herein, we report that the SPG21 protein localizes to endolysosomes
through interaction with the GTP-bound form of RAB7A."] and [PMID:40833810 "We conclude that SPG21 acts
as a RAB7A effector that promotes noncanonical mTORC1-catalyzed phosphorylation of TFEB, thereby
suppressing its nuclear localization and transcriptional activity."], with the specificity result
[PMID:40833810 "Biochemical studies reveal that SPG21 depletion does not affect phosphorylation of
canonical mTORC1 substrates such as ULK1, S6K1, 4E-BP1, but reduces phosphorylation of the noncanonical
mTORC1 substrate TFEB."].

Boonen group: [PMID:41400694 "In the present study, we found that maspardin binds to RAB7 in control
cells"] and [PMID:41400694 "These findings identify maspardin as a newly discovered RAB7 effector and
shed light on several consequences of its deficiency."], with the mechanism running through RAB7
positioning: [PMID:41400694 "This redistribution decreases the interaction between RAB7 and its
GTPase-activating protein (GAP), TBC1D5."] and [PMID:41400694 "Consequently, RAB7 remains primarily
GTP-bound, recruiting more FYCO1 to lysosomes and promoting the anterograde movement of these organelles
along microtubules."].

So the honest molecular function is **small GTPase binding** (GO:0031267; GO merged "Rab GTPase binding"
into it) - specifically binding GTP-loaded RAB7A - and the honest statement of what remains dark is the
*effector output*: nobody knows what maspardin does to RAB7A once bound, or how binding keeps RAB7A on
retromer/TBC1D5-positive late endosomes rather than on lysosomes.

## The CD4 annotation

`GO:0042609 CD4 receptor binding` is a real result: a two-hybrid screen with the CD4 cytoplasmic tail
recovered ACP33, and the interaction was mapped to CD4's C-terminal hydrophobic residues
[PMID:11113139 "we propose that ACP33 modulates the stimulatory activity of CD4"]. It is not overturned,
and I have not removed it. But it is not the conserved core function: maspardin is ubiquitously expressed,
is conserved to insects and beyond (CD4 is vertebrate-specific), the disease is neurological rather than
immunological, and the IBA row is seeded solely by this human gene's own IPI (WITH/FROM
`PANTHER:PTN002698091|UniProtKB:Q9NZD8`), so the phylogenetic assertion projects a vertebrate-specific
partner across a family that predates it. Marked non-core with that reasoning stated.

## Curation position taken

- `GO:0005515` protein binding (10 IPI rows from interactome screens) → **MARK_AS_OVER_ANNOTATED**.
  This is where maspardin's whole molecular function currently lives in GOA, and it says nothing.
- `GO:0042609` CD4 receptor binding (IBA + IPI) → **KEEP_AS_NON_CORE**. Real, unreplicated in 25 years,
  taxon-restricted partner, not the conserved function.
- `GO:0005829` cytosol (IBA, IEA, 2x IDA) → **ACCEPT**. Maspardin genuinely partitions between cytosol
  and the endolysosomal membrane.
- `GO:0010008` endosome membrane (IEA) → **ACCEPT** as the informative location.
- `GO:0016020` membrane (IEA) → **MODIFY** to endosome membrane; correct but uninformative.
- `GO:0030140` trans-Golgi network transport vesicle and `GO:0005794` Golgi apparatus →
  **KEEP_AS_NON_CORE**. From the 2001 work; the compartment that the current mechanism runs through is
  the late endosome/lysosome.
- `GO:0007166` cell surface receptor signaling pathway (ARBA IEA) → **MARK_AS_OVER_ANNOTATED**; a machine
  generalisation of the CD4 story.
- `GO:0050851` antigen receptor-mediated signaling pathway (IC) → **KEEP_AS_NON_CORE**.
- New: RAB7A binding as `GO:0031267 small GTPase binding`, late endosome, and the TFEB/mTORC1 and
  lysosome-motility processes.

## Open question for experts

Has anyone ever assayed maspardin for hydrolase activity? The pseudoenzyme call has been repeated for
twenty-two years on sequence grounds alone, and the retained, mutation-hit nucleophile elbow is exactly
the configuration in which a fold-retaining protein sometimes turns out to retain residual activity.
