# treA (PA2416, Q9I165) review notes

## The one experimental row is an *E. coli* paper

PseudoCAP annotates `GO:0015927` trehalase activity to PA2416 by **IMP** from PMID:2820965. That
paper is titled "Trehalase of *Escherichia coli*. Mapping and cloning of its structural gene and
identification of the enzyme as a periplasmic protein induced under high osmolarity growth
conditions", and its abstract is *E. coli* genetics throughout: a `treA::Tn10` insertion mapped
"at 26 min on the E. coli linkage map", strains MC4100, PPA69 and UE5, P1 transduction.

Two things make this a confident call rather than a guess about unread text:

- The experiment that an IMP code asserts — loss of function in a mutant — was done in *E. coli*
  strains, named in the abstract. Nothing in the unread full text can turn that into a
  *P. aeruginosa* mutant.
- The paper is from **1987**. PA2416 as a locus did not exist until the PAO1 genome was published
  in 2000, so the paper cannot be reporting a mutant of it.

The *claim* is not in doubt — see below — so the row is kept rather than removed, and the defect
filed is `WRONG_EVIDENCE_CODE`: an annotation transferred from a characterised ortholog is ISS,
not IMP. The reference itself is marked `VERIFIED` rather than `MISCITED`, since the paper is
correctly identified and does support the trehalase claim; what is wrong is the code attached to
it, and that is recorded as the defect. This follows the merged `pvdL` precedent in this project, where an IMP citing a
*P. syringae* paper was kept and faulted the same way.

## The claim itself is solidly supported, just not by that paper

Q9I165 is a **reviewed** (Swiss-Prot) entry built on **HAMAP-Rule MF_01060**, a curated UniRule
system, and the supporting features are reaction-specific rather than fold-level:

- `DR NCBIfam; NF009774; treA; 1.` and `NF009775; treA` — curated family models named for the gene.
- `DR PROSITE; PS00927; TREHALASE_1; 1.` and `PS00928; TREHALASE_2; 1.` — two trehalase patterns.
- `DR InterPro; IPR023720; Trehalase_periplasmic.` — the periplasmic-trehalase entry specifically.
- Two active sites (320, 503) and seven substrate-binding sites placed by the rule.
- `FT SIGNAL 1..30` and `DE Flags: Precursor`, consistent with the periplasmic location the rule
  assigns.

So the enzyme identification rests on curated family systems, which this project treats as good
support for membership and hence for function. What is missing is any measurement on the
*P. aeruginosa* protein.

## The osmotic-response row

`GO:0071474` cellular hyperosmotic response is mapped from `IPR023720`. The row stays
`MARK_AS_OVER_ANNOTATED`, but the reasoning below replaces an earlier version of this section that
was wrong, and the way it was wrong is worth keeping.

**What I argued first, and why it does not hold.** I wrote that the mapping "inverts what the
curated rule actually says": the rule's FUNCTION line gives a **nutritional** function
([file:PSEAE/treA/treA-uniprot.txt "Provides the cells with the ability to utilize trehalose at
high osmolarity by splitting it into glucose molecules that can subsequently be taken up by the
phosphotransferase-mediated uptake system."]), the *E. coli* observation behind the mapping is
osmotic *induction* ([PMID:2820965 "Trehalase activity in MC4100 was not induced by growth in the
presence of trehalose but increased by about 10-fold when 0.6 M sucrose was added to minimal growth
medium."]), and being induced by a condition is not participating in the response to it. The
general principle is sound. It is not what is happening here.

A *treA* null has a phenotype that appears **only** under osmotic stress:
[PMID:1825082 "treA mutants with a defective periplasmic trehalase accumulated trehalose
extracellularly under osmotic stress."] The authors read the wild type as running a cycle —
[PMID:1825082 "Thus, stressed E. coli cells regulate the cytoplasmic level of trehalose by a futile
cycle involving overproduction, excretion, and degradation to glucose, which is
reutilized."] So the stressed cell overproduces trehalose, excretes some, and TreA degrades the
excreted pool to glucose that is taken back up. Periplasmic degradation is a **limb of an
osmotic-stress mechanism**, not merely a reaction switched on by one, and my claim that "nothing
identifies a step of osmotic adaptation that this protein carries out" was false.

**Why it is still over-annotation.** Two reasons, neither of which is the one I gave.

First, the compartmental split is real and the enzyme is on the catabolic side of it:
[PMID:8391102 "Externally supplied trehalose does not serve as a stress protectant, but it can
be utilized as the sole source of carbon and energy."] The protectant is cytoplasmic trehalose;
TreA acts on what has left the cell. Osmolarity also selects *which* catabolic route runs —
[PMID:8391102 "In the absence of osmotic stress, trehalose induces the formation of an enzyme IITre
(TreB) of the group translocation system, a catabolic trehalose-6-phosphate phosphatase (TreE), and
an amylotrehalase (TreC) which converts trehalose to free glucose and a glucose polymer."] — so the
enzyme's own job is catabolism under both conditions, and what changes with osmolarity is which
enzyme does it.

Second, and this is the mapping-level point: the osmotic content of the story lives in the
**circuitry around** the enzyme — an osmotically regulated promoter, OtsAB-type trehalose
synthesis, trehalose excretion — and none of that is what a trehalase signature detects.
`IPR023720` matches 472 proteins (InterPro API, checked 2026-11-26), every one of which inherits a
regulatory finding from *E. coli* K-12.

For *P. aeruginosa* the architecture is at least plausible rather than excluded, which is a point
against my first version too: PAO1 does accumulate trehalose under osmotic stress
([PMID:8434912 "osmotically stressed cultures were found to accumulate glutamate, trehalose, and
N-acetylglutaminylglutamine amide, an unusual dipeptide previously reported only in osmotically
stressed Rhizobium meliloti and Pseudomonas fluorescens."]), so the substrate pool the cycle needs
exists here. What does not exist is any measurement of osmotic induction of this gene or of a
*treA* phenotype in this organism. That is why the row is over-annotated rather than removed, and
why the mapping review records this as `broadMatch` rather than a removal.

## Granularity

OLS confirms `GO:0004555` alpha,alpha-trehalase activity sits under `GO:0015927` trehalase
activity, which also covers trehalose-6-phosphate hydrolases (EC 3.2.1.93) and is therefore a
grouping term rather than a reaction. Both `GO:0015927` rows are `TOO_GENERAL`: the specific term
is already carried on this gene by IBA and by the HAMAP-derived IEA, and neither general row's own
evidence reaches past the group — the IEA row's only entity is an ARBA association rule, and the
IMP row's evidence is the *E. coli* experiment discussed above.

Likewise `GO:0005991` trehalose metabolic process is the parent of the accepted `GO:0005993`
trehalose catabolic process, and `GO:0005975` carbohydrate metabolic process is further up again.

## The IBA

`PTN004635776` is seeded by trehalases from across the eukaryotes — human TREH (O43280), *Drosophila*
Treh, *S. cerevisiae* NTH1 and ATH1, *S. pombe*, *Candida*, *Arabidopsis*. The donor list being
eukaryotic is not a weakness: GH37 trehalases span bacteria and eukaryotes, the node is where the
family's shared activity sits, and PA2416 carries both trehalase PROSITE patterns and the curated
periplasmic-trehalase assignment, so it is inside the clade that inherited the function. Accepted.
