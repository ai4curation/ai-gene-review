# petC (Q88N93, PP_1319) — curation notes

Cytochrome *c*1 output subunit of the respiratory cytochrome bc1 complex of
*Pseudomonas putida* KT2440. See `genes/PSEPK/petA/petA-notes.md` for the operon-level
identity argument and the evidence caveats shared by all three subunits.

## This is the weakest-evidenced of the three entries

`petC-uniprot.txt` is **PE 4: Predicted** — the only one of the three at that level —
with a `SubName` rather than a `RecName`, no FUNCTION line, and no SUBUNIT line. What
it does give is concrete and directly usable:

- Cytochrome c1 family assignment: `IPR002326 Cyt_c1`, PRINTS `PR00603 CYTOCHROMEC1`,
  PANTHER `PTHR10266` CYTOCHROME C1, Pfam `PF02167 Cytochrom_C1`.
- One covalently attached heme: "Name=heme c; Xref=ChEBI:CHEBI:61717;" and
  "Note=Binds 1 heme c group covalently per subunit.", with covalent BINDING residues
  mapped at positions 50, 53 and 54.
- Topology: SIGNAL 1..19 (cleaved), CHAIN 20..259, and a single TRANSMEM helix at
  232..250 — i.e. a periplasmic cytochrome c domain (DOMAIN 37..222) on a C-terminal
  membrane anchor.
- Subcellular location: the unqualified "Membrane" only.

Everything asserted in the review beyond that list is sourced below, and the two
proposed annotations carry `ISS` against the co-operonic petA record rather than an
experimental code, precisely because this entry is predicted.

## Complex membership comes from petA's record, not petC's

petC has no SUBUNIT line of its own. The membership claim rests on the petA record
naming the c1 cytochrome as one of the three main subunits ("The main subunits of
complex b-c1 are: cytochrome b, cytochrome c1 and the Rieske protein.") and on the
operon architecture [PMID:15948965 "Bacterial cytochrome bc1-complex encoded by the
petABC operon consists of three subunits, the Rieske iron-sulphur protein, the b-type
cytochrome, and the c1-type cytochrome."]. PP_1317/1318/1319 are that triple.

## Comparator check before proposing GO:0045275 and GO:0022904

Neither term is in petC's GOA, while the co-operonic petB carries both by IEA. Per
CLAUDE.md, absence in a gene where sibling participants have the term is a reason to
check the convention, not an automatic gap. The check supports adding them here:

- `GO:0045275 respiratory chain complex III` is annotated to *individual* complex III
  subunits, not only to whole complexes — human CYC1 (the cytochrome c1 orthologue)
  by IPI, UQCRFS1 by IDA and IC, UQCRB by IPI (`genes/human/*/[gene]-goa.tsv`).
- For the process term, human CYC1 carries `GO:0006122` mitochondrial electron
  transport, ubiquinol to cytochrome c — the mitochondrion-specific descendant of
  `GO:0022904` — and UQCRFS1 carries `GO:0022904` itself by IMP. For a bacterium,
  `GO:0022904` is the correct granularity.

The participation test is also satisfied rather than assumed: PetC is not a substrate
or a mere requirement of the chain, it performs the output step. Its heme *c* accepts
the electron from the Rieske center and reduces periplasmic cytochrome *c*, which then
feeds the terminal oxidases.

## Downstream acceptors are inferred, not identified

The bc1 complex reduces cytochrome *c*, which supplies the cytochrome *c* oxidases of
a branched chain [PMID:16958757 "Pseudomonas putida KT2440 contains a branched aerobic
respiratory chain with several terminal oxidases."]. Which specific periplasmic
cytochrome *c* proteins accept electrons from P. putida PetC has not been established
— recorded as a `suggested_question` rather than asserted anywhere in the review.

## Cytochrome c1 is the least structurally conserved subunit

Worth flagging against over-confident homology transfer to this subunit specifically.
The Paracoccus structure found that, in contrast to cytochrome *b* and the Rieske
protein, "cytochrome c(1) shows structural differences to the mitochondrial and even
between the two Rhodobacteraceae complexes" [PMID:21996020 "Interestingly, cytochrome
c(1) shows structural differences to the mitochondrial and even between the two
Rhodobacteraceae complexes."], with low structural constraint on the surface facing
the Rieske domain. The same work showed that truncating an organism-specific acidic
N-terminal extension of cytochrome c1 changes the oligomerization state of the whole
enzyme — hence the `suggested_question` about whether P. putida PetC carries such an
extension. The conserved claims (heme c attachment, electron relay from Rieske to
cytochrome c, membership in the complex) are safe; fine structural detail should not
be transferred.

## Location: why GO:0005886 rather than GO:0016020

As for petB: petC's own record says only "Membrane", and the refinement to
`GO:0005886 plasma membrane` is an inference from complex membership with petA, whose
record specifies "Cell membrane" (UniProtKB-SubCell:SL-0039). In a Gram-negative
bacterium a complex III subunit sits in the cytoplasmic (inner) membrane.
`modules/bacterial_cytochrome_bc1_complex.yaml` already asserts `GO:0005886` for petC,
so the earlier `GO:0016020` in `core_functions.locations` contradicted the module and
has been brought into line with it. `MODIFY` rather than `REMOVE` because petC has no
`GO:0005886` row of its own, so removing the generic term would leave no location at
all. The inference basis is stated explicitly in the review reason, which matters more
here than for petB given the PE 4 status.
