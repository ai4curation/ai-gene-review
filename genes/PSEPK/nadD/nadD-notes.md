# nadD curation notes

## 2026-07-20

- Target identity: PP_4810 / reviewed UniProtKB Q88DL5, NadD-family
  nicotinate-nucleotide adenylyltransferase [UniProtKB:Q88DL5,
  "Belongs to the NadD family."].
- Reaction: NaMN and ATP yield deamido-NAD and diphosphate
  [UniProtKB:Q88DL5, "Catalyzes the reversible adenylation of nicotinate mononucleotide (NaMN) to nicotinic acid adenine dinucleotide (NaAD)."]
  [RHEA:22860, NaMN adenylylation].
- Family grounding: the target has a broad PTHR39321
  nicotinate-nucleotide-adenylyltransferase-related family cross-reference.
  Exact reviewed *Escherichia coli* NadD P0A752 is retained despite its
  PTHR12039:SF0 placement in the pinned member index, and *Bacillus subtilis*
  NadD P54455 provides a directly characterized structural exemplar; no
  ancestral PTN is asserted
  [UniProtKB:Q88DL5, "PANTHER; PTHR39321;
  NICOTINATE-NUCLEOTIDE ADENYLYLTRANSFERASE-RELATED; 1."]
  [PMID:11704676, "The nadD gene in Bacillus subtilis (yqeJ) was identified by sequence homology with other bacterial nadD genes and by biochemical characterization of the gene product."]
  [PMID:11704676, "The NaMN AT crystal structure was determined for both the apo enzyme and product-bound form, to 2.1 and 3.2 A, respectively."].
- Curation: GO:0004515 and NAD+ biosynthesis are core. Generic catalytic,
  nucleotidyltransferase, adenylyltransferase, and nucleotide-biosynthesis terms
  were modified to the specific leaf activity or pathway term.
- OpenScientist independently recovered the reviewed NaMN-to-NaAD reaction and
  NadD-family assignment. Its stronger claims of absolute NMN exclusion,
  essentiality, and detailed mechanism in KT2440 are ortholog-based. The exact
  38.8% identity and target motif mapping are not used as curated evidence
  because no alignment artifact was retained. These claims remain testable
  rather than curated target facts
  [file:PSEPK/nadD/nadD-deep-research-openscientist.md,
  "No enzymatic, structural, or knockout study exists for the P. putida KT2440 NadD specifically"].
