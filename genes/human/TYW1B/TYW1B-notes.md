# TYW1B (Q6NUM6) curation notes

Session 2026-10-18, RADICAL_SAM project, reviewed together with TYW1 (see
genes/human/TYW1/TYW1-notes.md for the shared enzymology).

## Evidence status

- No experimental study of TYW1B function exists. A PubMed search for "TYW1B OR RSAFD2"
  (2026-10-18) returns 7 papers, all genomic or association hits (somatic variant lists,
  methylation EWAS, sheep selective sweeps, a translocation breakpoint), with no biochemistry.
- UniProt function, catalytic activity and cofactor are all ECO:0000250 from yeast Tyw1
  (Q08960). There is no TYW1B-specific experimental support.
- The asta deep-research file is retrieval-only. Its one relevant hit, PMID:30698754
  (human tRNA modification enzymes), does not discuss TYW1 or TYW1B in the cached text.
- The only experimental GOA row is a HuRI Y2H interaction with TAS2R19 (PMID:32296183),
  which gives no functional information.

## Sequence analysis (file:human/TYW1B/TYW1B-bioinformatics/RESULTS.md)

- TYW1B is 95.7% identical to TYW1 over aligned positions. This fits a recent segmental
  duplication on 7q11 (gene location from the brief; not verified by me in a cached source).
- Canonical TYW1B lacks TYW1 residues 46-91, which hold the flavodoxin phosphate-binding
  loop (TYW1 SQTGT 85-89, a UniProt FMN feature). The UniProt TYW1B FMN feature at 43-47
  (EMQGF) is a ProRule projection that does not line up with this loop.
- Canonical TYW1B lacks two of the three auxiliary-cluster cysteines (TYW1 C381 and C394,
  matching P. abyssi Cys45/Cys58). In their place is a segment (VDAPRERSLLQTHILWN) that
  resembles the TYW1 isoform-2 alternative exon. The radical-SAM CX3CX2C triad is kept.
- In the archaeal enzyme the auxiliary cluster binds pyruvate and is proposed to cleave it
  oxidatively [PMID:23043105; PMID:36326713]. Losing two of its ligands would be expected
  to impair or abolish 4-demethylwyosine synthase activity. This is an inference.
- The human TYW1 knockout abolishes OHyW in hESCs [PMID:38706838]. If that knockout was
  specific to TYW1, any TYW1B present cannot make up for it in those cells.

## Decisions

- GO:0102521 tRNA-4-demethylwyosine synthase activity (IEA from EC): UNDECIDED. The
  activity is inferred only by transfer from yeast, and the sequence lacks auxiliary-cluster
  ligands.
- GO:0031591 wybutosine biosynthetic process (IBA): UNDECIDED. TYW1B sits inside the PTN
  clade, but there is target-specific sequence divergence at the catalytic motifs.
- GO:0003824 catalytic activity: KEEP_AS_NON_CORE. The project rule says to MODIFY to the
  specific reaction MF "the gene carries or is shown to have", with KEEP_AS_NON_CORE when no
  reaction is known. The reaction MF is itself undecided here, so KEEP_AS_NON_CORE avoids
  asserting it, and the radical-SAM fold makes a generic catalytic claim defensible.
- GO:0051539: KEEP_AS_NON_CORE (the project rule allows this where catalysis is not
  established; the radical-SAM triad is kept, so the cluster is plausible).
- GO:0051536: MODIFY to GO:0051539 (project rule).
- GO:0010181 FMN binding: UNDECIDED (the phosphate-binding loop is missing; other FMN
  contacts remain).
- GO:0008033 tRNA processing: UNDECIDED, consistent with GO:0031591.
- GO:0005515 protein binding (TAS2R19, HuRI): REMOVE (uninformative). TAS2R19 is a
  bitter-taste GPCR, which gives no functional lead.

## Knowledge gap (genuine biology)

- Is TYW1B translated as a stable protein, and does it have any 4-demethylwyosine synthase
  activity? Would wet-lab work close this? Yes: recombinant enzyme assays, and yW/OHyW
  measurement in TYW1-null cells complemented with TYW1B.
