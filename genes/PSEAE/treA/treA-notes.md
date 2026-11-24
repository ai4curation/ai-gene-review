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
not IMP. This follows the merged `pvdL` precedent in this project, where an IMP citing a
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

`GO:0071474` cellular hyperosmotic response is mapped from `IPR023720`, and it inverts what the
curated rule actually says. The rule's own FUNCTION line is
[file:PSEAE/treA/treA-uniprot.txt "Provides the cells with the ability to utilize trehalose at
high osmolarity by splitting it into glucose molecules that can subsequently be taken up by the
phosphotransferase-mediated uptake system."] — a **nutritional** function exercised under
high-osmolarity conditions, not a contribution to osmotic adaptation. The *E. coli* observation
behind the mapping is that trehalase activity "was not induced by growth in the presence of
trehalose but increased by about 10-fold when 0.6 M sucrose was added" — i.e. the gene is
*regulated by* osmolarity. Being induced by a condition is not participating in the response to
it, and the entity doing the osmotic work in these cells is cytoplasmic trehalose, not the
periplasmic enzyme that destroys the periplasmic pool. Marked over-annotated.

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
