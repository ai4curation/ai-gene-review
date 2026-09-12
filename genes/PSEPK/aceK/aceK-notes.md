# aceK (Pseudomonas putida KT2440, PP_4565) - Curation Notes

UniProt: Q88EA1 (ACEK_PSEPK), 571 aa, OrderedLocusName PP_4565.
EC=2.7.11.5 (kinase) and EC=3.1.3.- (phosphatase). PE: 3 (Inferred from homology).
Annotated via HAMAP-Rule MF_00747 (AceK family). There are no experimental
characterizations of the *P. putida* protein itself; functional knowledge derives from
the AceK family (best characterized in *E. coli*) and from the HAMAP rule.

## FUNCTION

AceK is a bifunctional isocitrate dehydrogenase kinase/phosphatase. It both
phosphorylates (inactivating) and dephosphorylates (reactivating) isocitrate
dehydrogenase (IDH) on a specific serine residue, controlling the partitioning of
isocitrate between the TCA cycle and the glyoxylate bypass.

- [UniProt "Bifunctional enzyme which can phosphorylate or dephosphorylate isocitrate dehydrogenase (IDH) on a specific serine residue."]
- [UniProt "This is a regulatory mechanism which enables bacteria to bypass the Krebs cycle via the glyoxylate shunt in response to the source of carbon."]
- [UniProt "When bacteria are grown on glucose, IDH is fully active and unphosphorylated, but when grown on acetate or ethanol, the activity of IDH declines drastically concomitant with its phosphorylation."]

When IDH is phosphorylated and thereby inactivated, isocitrate accumulates and is
diverted into the glyoxylate bypass (isocitrate lyase / malate synthase), allowing net
carbon assimilation from C2 substrates such as acetate and fatty acids. When the carbon
source returns to glucose, AceK dephosphorylates and reactivates IDH.

## CATALYTIC ACTIVITY

Kinase reaction (EC 2.7.11.5):
- [UniProt "Reaction=L-seryl-[isocitrate dehydrogenase] + ATP = O-phospho-L-seryl-[isocitrate dehydrogenase] + ADP + H(+)"]
- Rhea:RHEA:43540; EC=2.7.11.5.

Phosphatase reaction (EC 3.1.3.-): reverse dephosphorylation of phospho-IDH.
The phosphatase activity is also ATP-dependent (a hallmark of AceK; the same active
site and ATP catalyze both opposing reactions in the family).

The specific MF term for the phosphatase activity is GO:0101014
([isocitrate dehydrogenase (NADP+)] phosphatase activity), which is more precise than
the GOA-provided generic terms GO:0004721 (phosphoprotein phosphatase activity) and
GO:0016791 (phosphatase activity).

## STRUCTURE / SITES

- ACT_SITE at residue 374 (HAMAP-Rule MF_00747).
- ATP binding: residues 318..324 and 339 (ligand ATP, ChEBI:CHEBI:30616).
- [UniProt "Belongs to the AceK family."]
- Domains: AceK_kinase (Pfam PF06315), AceK_regulatory (Pfam PF20423);
  InterPro IPR010452 (Isocitrate_DH_AceK).

## SUBCELLULAR LOCATION

- [UniProt "Cytoplasm"] (ECO:0000255|HAMAP-Rule:MF_00747).

## BIOLOGICAL PROCESS

The HAMAP rule annotates the protein to the glyoxylate cycle (GO:0006097) and
tricarboxylic acid cycle (GO:0006099). AceK is the regulatory switch that partitions
flux between these two pathways. Mechanistically AceK does not itself carry out TCA-cycle
or glyoxylate-cycle catalysis; it regulates the entry point (IDH vs isocitrate lyase),
so it is appropriately described as a regulator of these pathways during growth on
acetate/fatty acids.

## ANNOTATION ASSESSMENT NOTES

- GO:0008772 [isocitrate dehydrogenase (NADP+)] kinase activity - ACCEPT (core MF;
  matches EC 2.7.11.5 and the Rhea reaction).
- GO:0004721 phosphoprotein phosphatase activity / GO:0016791 phosphatase activity -
  generic; MODIFY to GO:0101014 ([isocitrate dehydrogenase (NADP+)] phosphatase
  activity), the precise term for the reactivating dephosphorylation (EC 3.1.3.-).
- GO:0005524 ATP binding - real (ATP-binding residues annotated) but broad relative to
  the kinase MF; MARK_AS_OVER_ANNOTATED.
- GO:0004674 protein serine/threonine kinase activity (a UniProt keyword-derived term,
  present in the UniProt DR block; not in GOA file) - generic parent of the specific
  IDH kinase term.
- GO:0016208 AMP binding - TreeGrafter (PANTHER) prediction. AceK kinase/phosphatase
  switching is allosterically regulated by metabolites including AMP/ADP/AMP in the
  family, but a discrete "AMP binding" MF is weakly supported for the P. putida
  ortholog; KEEP_AS_NON_CORE / over-annotated rather than core.
- GO:0016788 hydrolase activity, acting on ester bonds - broad parent of the phosphatase
  activity; redundant once the specific phosphatase term is used; MARK_AS_OVER_ANNOTATED.
- GO:0006006 glucose metabolic process - InterPro2GO; AceK acts during growth on
  acetate/ethanol (IDH is dephosphorylated/active on glucose, i.e. AceK is largely OFF
  on glucose); this term is misleading and over-broad; MARK_AS_OVER_ANNOTATED.
- GO:0006097 glyoxylate cycle, GO:0006099 tricarboxylic acid cycle - ACCEPT as
  pathway-context BP (regulatory role partitioning flux between the two).
- GO:0005737 cytoplasm - ACCEPT (consistent with UniProt SUBCELLULAR LOCATION).

## CAVEATS

- All annotations are IEA/electronic; there are no P. putida-specific experimental
  studies of AceK in the cached corpus. Confidence rests on strong family-level
  conservation (HAMAP MF_00747, conserved active site Ser374 region and ATP-binding
  residues).
