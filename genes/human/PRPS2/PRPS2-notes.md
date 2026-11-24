# PRPS2 notes

## Functional summary

PRPS2 encodes human PRSII/ribose-phosphate pyrophosphokinase 2, an EC 2.7.6.1
enzyme that converts ATP plus ribose 5-phosphate into PRPP plus AMP. Direct
support comes from recombinant human PRSII biochemistry: Nosal, Switzer and
Becker purified PRSI and PRSII after overexpression in an E. coli strain lacking
the bacterial PRPP synthetase and found that the isoforms differ in MgATP and
ribose 5-phosphate Km values, pH optima, Mg2+/Pi activation curves and feedback
inhibition [PMID:8387514, "PRSI and PRSII also differed significantly in Km
values for MgATP and ribose 5-phosphate"].

The more recent PRPS2 structural literature confirms the same chemistry and
explains PRPS2 assembly. Lu et al. solved human PRPS2 filaments with ADP, Pi and
Mg2+ and found that PRPS2 hexamers are the polymer unit; R301A/R302A mutations
blocked filament formation and nearly abolished activity [PMID:37248548,
"A point mutation disrupting the inter-hexamer interaction prevents hPRPS2
polymerization and results in significantly reduced catalytic activity."].
Zhang et al. independently solved PRPS2 ligand-bound crystal structures and
showed that PRPS2 sustains purine nucleotide output under conditions where PRPS1
is more sensitive to ADP/GDP feedback inhibition [PMID:40295500, "PRPS2
utilizes four non-conserved key residues to bypass the typical ADP/GDP
allosteric feedback inhibition"].

The 1989 PRPS2 cDNA paper is useful for identity and conservation but is not the
strongest support for detailed function. It cloned a full 954-bp coding region
for 318 residues and noted 99% amino acid identity with rat PRSII
[PMID:2538352, "The five overlapping clones contained 2457 base pairs (bp)
covering a 954-bp complete coding region for 318 amino acid residues."].

## Annotation decisions

- Accept `GO:0004749 ribose phosphate diphosphokinase activity` and
  `GO:0006015 5-phosphoribose 1-diphosphate biosynthetic process`: they are the
  direct activity and one-step process.
- Keep ATP binding, Mg2+ binding, identical protein binding, homodimerization and
  protein hexamerization as non-core: each is part of catalysis or assembly, not
  a separate primary function.
- Accept cytoplasm and cytosol: PRPS2 is a soluble PRPP synthetase and UniProt
  has no organelle-targeting feature.
- Keep `GO:0006164 purine nucleotide biosynthetic process` and
  `GO:0009156 ribonucleoside monophosphate biosynthetic process` as non-core
  downstream context because PRPP is the substrate consumed by those pathways.
- Mark the broad nucleotide, organophosphate, purine-metabolic and
  nucleobase-containing-compound process rows as too general when a direct PRPP
  biosynthesis row is already present.
- Remove the Ensembl-derived pentose-phosphate-shunt row: PRPS2 consumes
  ribose 5-phosphate made by the PPP but is not a PPP enzyme.
- Remove all bare `GO:0005515 protein binding` rows from proteome-scale
  interactome papers under the generic-protein-binding policy. The
  PRPS2-PRPS2 self-interaction is retained separately as `GO:0042802` because
  the human structures show a homohexamer.

## PTHR10210 implications

`just paint-losses human PRPS2` reports an IRD at `PANTHER:PTN000025038` that
blocks `GO:0002189 ribose phosphate diphosphokinase complex` from descending
from `PTN000025022` to PRPS2. The existing PTHR10210 review already calls that
IRD `LOSS_CONTRADICTED`. The human PRPS2 homohexameric structures provide
member-specific support for the same conclusion, so the gene review adds a
conservative `NEW` `GO:0002189` row rather than leaving PRPS2 without a complex
annotation.

I did not add a new RNA methylation or SAM-biosynthesis process annotation from
PMID:40295500. That paper reports a cancer-context PRPS2-MAT2A axis, but the
core PRPS2 activity remains PRPP synthesis and the methylation phenotype is
downstream of nucleotide/SAM flux and MAT2A stabilization.
