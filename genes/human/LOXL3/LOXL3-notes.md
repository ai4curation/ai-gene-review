# LOXL3 evidence notes

## Research provenance and blocker

The seeded GOA, reviewed UniProt entry P58215, and all PMID sources listed in the
review were inspected locally. Additional direct or boundary-setting sources were
resolved and cached for PMID:11334717, PMID:11386757, PMID:21244857,
PMID:25663169, PMID:26218558, PMID:26307084, PMID:26954549, PMID:26957899,
PMID:28112368, PMID:29229995, and PMID:33456446.

A policy-compliant deep-research attempt was made with the repository's unified
tool using provider `perplexity`. It resolved LOXL3/P58215 but failed with HTTP
401 (`insufficient_quota`). No provider-named deep-research file was created, and
no deep-research assertions were used.

## Direct human catalytic evidence

The strongest direct human biochemical source in the seeded set is PMID:17018530.
Its cached abstract states:

> The recombinant LOXL3-sv1 protein showed a beta-aminopropionitrile-inhibitable amine oxidase activity toward elastin and collagen with substrate specificity.

The same abstract concludes:

> These findings strongly indicate that LOXL3 encodes two variants, LOXL3 and LOXL3-sv1, both of which function as amine oxidases with distinct tissue and substrate specificities from one another.

PMID:28112368 directly extends the biochemical evidence to sv2:

> The recombinant LOXL3-sv2 protein showed a β-aminopropionitrile-inhibitable amine oxidase activity toward collagen type I.

These are recombinant activity assays. They support protein-lysine oxidase activity
and candidate collagen/elastin substrates, but they do not by themselves prove the
same substrate hierarchy in vivo. PMID:11284725 is important for human secretion
but does not report a catalytic assay:

> Recombinant LOXL3, expressed in HT-1080 cells, was secreted into the culture medium but was not detected by immunofluorescence staining in nuclei.

## Isoform and transcript boundaries

Current UniProt P58215 names three isoforms: P58215-1 (canonical), P58215-2
(LOXL3-sv1), and P58215-3. The literature discusses four LOXL3 transcript/protein
forms, but they must not be conflated with four curated UniProt isoforms:

1. Canonical full-length LOXL3 is a 753-residue precursor.
2. LOXL3-sv1 (P58215-2) is a 392-residue form lacking sequences corresponding
   to exons 1, 2, 3, and 5 and SRCR domains 1-3 (PMID:17018530).
3. LOXL3-sv2 is a 608-residue exon-4/exon-5 deletion that lacks SRCR domain 2
   (PMID:28112368). Human melanoma work calls the corresponding form
   LOXL3ΔE4E5/LOXL3Δ and says it “probably corresponds” to sv2 (PMID:29229995).
4. PMID:11386757 reports ESTs predicting a distinct exon-5/exon-8-deleted form.
   It was not experimentally shown to yield protein or activity and is not a
   fourth named UniProt isoform.

Exact source boundaries:

> LOXL3-sv1 was predicted to encode a polypeptide of 392 amino acids that contains the C-terminal domains required for amine oxidase activity but lacks the N-terminal SRCR domains 1, 2, and 3. [PMID:17018530]

> The deletion of exons 4 and 5 do not change the open-reading frame of LOXL3 but results in deletion of the SRCR domain 2. [PMID:28112368]

> A BLASTN search of the human EST database indicated the presence of ESTs, corresponding to alternative splice variants of LOXL3, that lacked exon 5 and exon 8. [PMID:11386757]

> Both LOXL3 isoforms were found similarly expressed in most melanoma cells tested (Fig. 1f). LOXL3Δ isoform probably corresponds to the recently identified splice variant LOXL3-sv2 [27]. [PMID:29229995]

No P58215-4 identifier was inferred.

## Precursor, secretion, and processing

The reviewed UniProt entry annotates a predicted signal peptide at residues 1-25
and a chain beginning at residue 26. PMID:11284725 directly supports secretion of
recombinant human LOXL3. However, the reviewed sources do not demonstrate a
LOXL3-specific extracellular propeptide-removal step analogous to mature LOX,
nor do they establish BMP1 cleavage of human LOXL3. Indeed, the older predicted
exon-5/exon-8 transcript lacks a potential BMP-1 cleavage site:

> The putative resulting protein retained the region encoding the structural and functional elements of the amine oxidase but the second and fourth SRCR domains were truncated and the potential BMP-1 cleavage site was not present. [PMID:11386757]

Accordingly, “secreted full-length/catalytic LOXL3” is evidence-bounded; “mature
proteolytically processed LOXL3” is not established by these sources.

## Ortholog boundaries: collagen, fibronectin, and development

Mouse loss-of-function supports collagen-matrix and developmental roles, not a
direct human assay. PMID:26307084 states:

> In our study, a significant decrease in collagen-links from the lack of LOXL3 caused cleft palate and spinal deformity, while no obvious difference was observed in the elastin cross-links in the palate and spine.

Fibronectin oxidation and myotendinous-junction integrin activation come from
non-human model work (PMID:26954549), even though UniProt transfers the function
to the human entry by similarity:

> We find that LoxL3 complexes with and directly oxidizes Fibronectin (FN), an ECM scaffold protein and integrin ligand enriched at the MTJ.

Zebrafish has two mammalian-LOXL3-related paralogs, and the cited phenotype is
specifically loxl3b rather than human LOXL3 (PMID:21244857):

> We now demonstrate that loxl3b is abundantly expressed within the head mesenchyme of the zebrafish and is critically important for maturation of neural crest derived cartilage elements.

Thus fibronectin binding/oxidation, somite/MTJ positioning, and zebrafish
craniofacial cartilage phenotypes are informative ortholog evidence, not direct
human molecular evidence.

## Extracellular versus nuclear roles and the STAT3 claim

Human secretion is directly observed in PMID:11284725, whereas that experiment
did not detect recombinant LOXL3 in nuclei. In contrast, PMID:28065600 reports a
nuclear STAT3 mechanism:

> LOX-like 3 (Loxl3) associates with Stat3 in the nucleus to deacetylate and deacetyliminate Stat3 on multiple acetyl-lysine sites.

It further reports an unusual domain assignment:

> Surprisingly, Loxl3 N-terminal scavenger receptor cysteine-rich (SRCR) repeats, rather than the C-terminal oxidase catalytic domain, represent the major deacetylase/deacetyliminase activity.

The PMID/title/abstract are internally consistent, and the cached record carries
no retraction flag. Nevertheless, only an abstract is cached, and no independent
direct replication was located in the reviewed source set. The dual STAT3
deacetylation/deacetylimination chemistry should therefore be retained as a
single-study intracellular claim, clearly separated from the established
C-terminal extracellular lysyl-oxidase chemistry. It should not be generalized
to all isoforms: sv1 lacks SRCR domains 1-3, and sv2 lacks SRCR domain 2.

## Intracellular partners, complexes, and disease context

PMID:16096638 supports a context-specific LOXL3-Snail interaction in epithelial
models:

> Here we show that lysyl-oxidase-like 2 and 3 (LOXL2 and LOXL3), two members of the lysyl-oxidase gene family, interact and cooperate with Snail to downregulate E-cadherin expression.

PMID:29229995 supports human melanoma-cell dependencies and associations with
genome-integrity proteins:

> Consistent with these findings, LOXL3 binds to proteins involved in the maintenance of genome integrity, in particular BRCA2 and MSH2, whose levels dramatically decrease upon LOXL3 depletion.

These interaction data do not establish BRCA2, MSH2, SMC1A, NUMA1, Snail, or
ADAMTSL2 as LOXL3 catalytic substrates, and they do not define a constitutive,
stoichiometric stable LOXL3 complex. Melanoma survival, EMT, and DNA-damage
phenotypes are disease/cell-context roles rather than universal core functions.

Human Stickler syndrome and early-onset high-myopia reports connect LOXL3 to
connective-tissue disease, but do not independently identify a molecular
substrate. PMID:26957899 explicitly cautions:

> LOXL3 is a potential candidate gene for high myopia, but this possibility should be confirmed in additional studies.

No cached source in this review is marked retracted or replaced. The surprising
STAT3 chemistry remains verification-limited for the reasons above; the generic
elastic-fibre reviews PMID:16893474 and PMID:23962539 do not specifically establish
LOXL3 localization in elastic fibres from their cached abstracts.
