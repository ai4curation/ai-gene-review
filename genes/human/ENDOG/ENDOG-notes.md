# ENDOG notes

## 2026-09-30

ENDOG is a nuclear-encoded, mitochondrial DNA/RNA endonuclease with a mitochondrial
transit peptide and catalytic Mg-dependent nuclease fold. The human protein is in the
same PANTHER `PTHR13966:SF5` subfamily as mouse Endog, yeast NUC1, and worm cps-6,
which supports the broad DNA/RNA nonspecific endonuclease PAINT transfers.

The best direct human and mammalian process evidence splits into three branches:

- **Modified nuclear DNA cleavage and recombination.** Robertson et al. purified EndoG
  as the activity in mouse liver extracts that preferentially cleaves
  5-hydroxymethylcytosine-modified DNA, showed recombinant EndoG cleavage, and showed
  that 5hmC stimulates conservative recombination in an EndoG-dependent manner
  [PMID:25355512 Endonuclease G preferentially cleaves 5-hydroxymethylcytosine-modified
  DNA creating a substrate for recombination., "recombinant EndoG preferentially
  recognizes and cleaves a core sequence"; "promote conservative recombination in an
  EndoG-dependent manner"].
- **Mitochondrial DNA turnover.** Wiehe et al. used human-cell knockdown, knockout,
  re-expression, and nuclease-mutant assays to show that ENDOG stimulates mitochondrial
  DNA depletion and compensatory mitochondrial DNA replication in a nuclease-dependent
  manner, especially under oxidative stress [PMID:29719607 Endonuclease G promotes
  mitochondrial genome cleavage and replication., "EndoG stimulates both mtDNA
  replication"].
- **Starvation autophagy.** Wang et al. showed that starvation-released, GSK3beta-
  phosphorylated ENDOG binds YWHAG/14-3-3gamma, freeing TSC2 and VPS34 from YWHAG to
  suppress mTORC1 and initiate autophagy; they also support an endonuclease-dependent
  DNA damage-response branch of the same autophagy phenotype [PMID:33473107
  Endonuclease G promotes autophagy by suppressing mTOR signaling and activating the DNA
  damage response., "mTOR pathway suppression and autophagy initiation"; "enhances its
  interaction with 14-3-3"].

The inherited apoptotic DNA-fragmentation row is plausible and should stay specific:
ENDOG can itself cleave DNA after mitochondrial release, so `GO:0006309 apoptotic DNA
fragmentation` is preferable to any broad `GO:0006915 apoptotic process` row. It is not
the central CAD/DFF40 nuclease, though, and the more recent human papers point toward
mtDNA maintenance, 5hmC-biased cleavage/recombination, and starvation autophagy as the
core ENDOG axes.

The rat-derived stimulus rows for mechanical stimulus, calcium, glucose, hypoxia,
estradiol, oxidative stress, and hydrogen-peroxide cell death look over-propagated into
human. They describe conditions or cell-death outcomes in which rat Endog was mobilized
rather than a molecular step performed by human ENDOG. The DNAJA4 and ITLN2 protein
binding rows from high-throughput interactome/chaperone studies were removed as generic
edges with no ENDOG-specific functional interpretation.
