# traB (F plasmid, *Escherichia coli* K-12) — curation notes

UniProt: P41067 (TRAB1_ECOLI), 475 aa. Encoded on plasmid F and on plasmid
IncFII ColB2, not on the chromosome. UniProt assigns it to "the TraB family"
and gives one functional statement: "Involved in F pilus assembly."

## Identity and role

TraB is a structural subunit of the outer-membrane core complex of the F-type
type IV secretion system, the VirB10 counterpart of that machine. The
cryo-EM structure of the core complex of an F-family system resolves the
architecture directly: the complex is built from an outer ring of TraK and
TraV together with a central cone made entirely of TraB
[PMID:35046412 "The OMCCF consists of a 13-fold symmetrical outer ring complex (ORC) built from 26 copies of TraK and TraV C-terminal domains, and a 17-fold symmetrical central cone (CC) composed of 17 copies of TraB β-barrels."].
The same work establishes that these three proteins are functionally
load-bearing rather than incidental
[PMID:35046412 "define the importance of TraK, TraV and TraB domains to T4SSF function"].

Note on strain scope: that structure was solved for pED208, an F-family
plasmid, so it establishes the role for the F-type system rather than for
P41067's own polypeptide. P41067 is the F plasmid's TraB.

The F transfer region is the reference conjugation system in which this gene
sits [PMID:7915817 "One of the best-defined conjugation systems is that of the F plasmid, which has been the paradigm for conjugation systems since it was discovered nearly 50 years ago."],
and its genes cover pilus synthesis, mating-pair stabilization, surface
exclusion, DNA nicking and transfer, and regulation
[PMID:7915817 "These are involved in the synthesis of pili, extracellular filaments which establish contact between donor and recipient cells; mating-pair stabilization; prevention of mating between similar donor cells in a process termed surface exclusions; DNA nicking and transfer during conjugation; and the regulation of expression of these functions."].
TraB belongs to the first of those groups.

## The ATP hydrolysis annotation is attributed to the wrong protein

P41067's only GOA row is GO:0016887 ATP hydrolysis activity, IDA, from
PMID:20172994, assigned by CACAO. That paper is not about this protein. Its
abstract states the subject explicitly
[PMID:20172994 "a VirB4 homologue from the pKM101 conjugation"],
and its title names the plasmid as well.

Four independent facts place the paper's protein apart from P41067:

1. **Plasmid.** The paper studies pKM101. P41067 is recorded by UniProt as
   encoded on plasmid F and plasmid IncFII ColB2.
2. **Family.** P41067 belongs to the TraB family. The pKM101 protein is a
   VirB4 homologue; the corresponding UniProt entry Q46698 is annotated
   "Belongs to the TrbE/VirB4 family".
3. **Length.** P41067 is 475 aa. Q46698 is 866 aa, consistent with VirB4-family
   ATPases being the largest component of the machine.
4. **Where F keeps that role.** F's own VirB4-family ATPase is a different
   gene product, TraC (P18004). If F TraB were the VirB4 homologue, F would
   have two.

The collision is purely nomenclatural: Tra symbols are not stable between
conjugative plasmids, and on pKM101 the symbol TraB happens to name the
VirB4 homologue that on F is called TraC.

Worth recording even for the correct protein: the paper's ATP hydrolysis
result is conditional on how the protein was prepared. The membrane-purified
form did not hydrolyse ATP, and only the soluble hexameric form did
[PMID:20172994 "TraB can form hexamers capable of hydrolyzing ATP."].
So the annotation would need care even on Q46698.

Conclusion: REMOVE. This is not a case of second-guessing an assay whose full
text is unavailable. The cached abstract states the plasmid and the family
outright, which is the condition CLAUDE.md sets for making that call, and the
paper's protein has its own accession.

## Open questions

- No subcellular location is annotated for P41067. The core-complex structure
  places TraB β-barrels in the outer membrane while VirB10-family proteins are
  generally anchored in the inner membrane, so a two-membrane assignment is
  likely but was not asserted here from an F-specific experiment.
- UniProt states involvement in F pilus assembly, but GOA carries no process
  annotation at all for this protein. GO:0009297 pilus assembly and
  GO:0044097 look like genuine curation gaps.
