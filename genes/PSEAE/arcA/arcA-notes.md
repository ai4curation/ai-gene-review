# arcA (PA5171, P13981) notes

## Identity

- UniProt P13981 (ARCA_PSEAE), 418 aa, Swiss-Prot reviewed. Arginine deiminase
  (ADI, EC 3.5.3.6), arginine deiminase family (HAMAP MF_00242, NCBIfam TIGR01078,
  Pfam PF02274, InterPro IPR003876, PANTHER PTHR47271:SF3). Active site Cys406.
  Five PDB structures of the PAO1 enzyme (1RXX, 2A9G, 2AAF, 2ABR, 2ACI).
- First enzyme-encoding gene of the anaerobically induced arcDABC operon (PA5170
  arcD, PA5171 arcA, PA5172 arcB, PA5173 arcC).

## Biology (literature)

- Genetics: mutants unable to grow anaerobically on arginine fell into arcA, arcB,
  arcC (each lacking one ADI-pathway enzyme) and arcD classes, closely linked at
  17 min [PMID:6438064 "The mutations arcA (arginine deiminase), arcB (catabolic ornithine carbamoyltransferase), arcC (carbamate kinase), and arcD were highly cotransducible and mapped in the 17-min chromosome region."].
  The same paper notes that some arc mutations lowered all three enzymes, i.e.
  regulatory rather than structural mutations
  [PMID:6438064 "Some mutations in the arc cluster led to low, noninducible levels of all three arginine deiminase pathway enzymes"].
- Structural gene identification: arcA was sequenced, and the purified ADI
  subunit size and N-terminal sequence matched the ORF
  [PMID:2537202 "The N-terminal amino acid sequence of arginine deiminase was in agreement with the corresponding nucleotide sequence."];
  the purified enzyme was characterised kinetically
  [PMID:2537202 "The apparent Km for L-arginine was 0.04 mM in the presence of Mg2+ and 0.47 mM without Mg2+."].
- Structure and mechanism: P. aeruginosa ADI crystal structure, pentein fold
  shared with DDAH and amidinotransferases
  [PMID:14701825 "We have determined the crystal structure of ADI from Pseudomonas aeruginosa by the multi-wavelength anomalous diffraction method at 2.45 A resolution."];
  Cys406 nucleophile, substrate complex and thiouronium intermediate structures
  [PMID:16091358 "The function of Cys406 in nucleophilic catalysis has been demonstrated by transient kinetic studies."].
- Pathway: ADI pathway (ADI, catabolic OTC ArcB, carbamate kinase ArcC; ArcD
  arginine:ornithine antiporter) generates ATP from arginine under anoxia
  [PMID:2158926 "The arginine deiminase (ADI) pathway in Pseudomonas aeruginosa serves to generate ATP."].

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN005338738 | GO:0016990 arginine deiminase activity | 1 (sole seed) | 23 (18 taxa) | GO:0016990 arginine deiminase activity, IMP, PMID:6438064 (PseudoCAP) | SOUND | Classic enzyme-deficient mutant evidence: arcA mutants were defined by loss of ADI activity, separate from the regulatory class that lost all three enzymes, and the locus was later shown to be the ADI structural gene (PMID:2537202: purified ADI N-terminus matches the arcA ORF). A mutant phenotype can support an MF when the mutant is shown to lack that specific activity and the mutation is in the structural gene; both hold here. Stronger direct evidence (purified enzyme kinetics, crystal structures, Cys406 mechanism) exists for this very protein, so the IBD is very well anchored; IDA from PMID:2537202 would be a better seed. |

Node breadth: PTN005338738 spans the whole PTHR47271 family (SF2 + SF3): bacterial,
archaeal and protist (Giardia, Trichomonas, Chlamydomonas) ADIs. Most leaves are
~400-420 aa canonical ADIs, which fits the term. A few leaves are much shorter and
are not annotated as ADIs: B. subtilis YkgA (O34497, 286 aa, UniProt "Belongs to the
DDAH family", "Uncharacterized protein"), Methanosarcina Q8TSK4 (335 aa), Sulfolobus
Q97TX4 (341 aa) and Korarchaeum B1L3J0 ("N-dimethylarginine dimethylaminohydrolase").
B. subtilis 168 degrades arginine via arginase, not the ADI pathway. These leaves may
be over-propagations within the pentein superfamily; this was flagged to GO_CENTRAL
as a CHECK (SUSPECTED) on the IBA row. Not verified by sequence analysis here.

## Decisions summary

- ACCEPT: arginine deiminase activity (IBA, IEA, IMP), L-arginine catabolic process
  (IEA), cytoplasm (IEA).
- PSEUDOCAP: no defect; IMP is acceptable (enzyme-deficient structural-gene mutant).
- GO_CENTRAL: CHECK (SUSPECTED) for DDAH-like short leaves under PTN005338738.
