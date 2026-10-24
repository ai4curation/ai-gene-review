# Notes: benzil reductase (EC 1.1.1.320 / RHEA:25968) gene set

Reviewed as a set with the other UniProt entries carrying RHEA:25968: yeast IRC24 and NRE1, B. cereus yueD (Q8RJB2), B. subtilis yueD (O32099). Gerbil SPR (Q8R536) also carries RHEA:25968, but it is a sepiapterin reductase that was incidentally tested on benzil, so it is out of scope.

## Why this set was reviewed

GO:0102306 "benzil reductase [(S)-benzoin-forming] activity" was obsoleted
(geneontology/go-ontology#30498, "not a physiologically relevant substrate"), and
RHEA:25968 was then attached as a `skos:narrowMatch` to the EC 1.1.1.- grouping
class GO:0016616. Consequences visible in GOA:

- The experimental benzil annotations (SGD IDA PMID:37602278; UniProt EXP
  PMID:11796169, PMID:11745140) now sit on GO:0016616, which only says "CH-OH
  donor, NAD(P) acceptor".
- New IEA rows (GO_REF:0000120, 2026-07-27, with/from RHEA:25968) are generated
  to the same grouping class.

## Biology

- B. cereus YueD: found by expression screen; NADPH-dependent stereospecific benzil ->
  (S)-benzoin; broad aromatic carbonyl specificity (diketones, 1,4-naphthoquinone,
  p-nitrobenzaldehyde); GFP shows cytoplasm [PMID:11796169 "Recombinant B. cereus benzil reductase produced optically pure"].
- Yeast Irc24 (YIR036C) and its tandem paralog Nre1 (YIR035C, 52% identical) both reduce benzil and
  prefer NADPH 2:1 over NADH [PMID:37602278 "Both enzymes were active with both coenzymes but showed a two-fold preference for NADPH"].
- All substrates are xenobiotic; no physiological substrate is known for any member.
- Sister reaction RHEA:31891 (1-phenyl-1,2-propanedione, also EC 1.1.1.320) is
  already narrowMatch to GO:0004090 carbonyl reductase (NADPH) activity, which yields the
  GO_REF:0000116 IEA to GO:0004090 on IRC24 and on B. cereus YueD.

## Decisions

- GO:0016616 rows -> MODIFY to GO:0004090. (S)-benzoin is a secondary alcohol, and
  benzil -> benzoin is ketone -> secondary alcohol with NADPH: exactly the
  GO:0004090/EC 1.1.1.184 reaction. EC 1.1.1.184's synonym list includes "xenobiotic ketone reductase".
- GO:0050664 (NAD(P)H, O2 acceptor) on IRC24 (SGD IDA 2013) and its IBA onto NRE1
  -> MODIFY to GO:0004090; the acceptor is benzil, not O2.
- Bacillus sepiapterin reductase / BH4 biosynthesis (PTHR44085 IBA/IEA): BH4
  process REMOVE (pathway absent in Bacillus); SPR activity over-annotated or
  undecided (never tested).
- No new GO term is needed: a benzil-specific term would reverse #30498, and
  GO:0004090 already covers the reaction class.

## Proposed GO-side change

Move `xref: RHEA:25968 {source="skos:narrowMatch"}` from GO:0016616 to GO:0004090.
More generally, flag any RHEA xref on an EC-incomplete (x.x.x.-) grouping term:
currently 9 reactions on GO:0016616, GO:0008241 and GO:0016712.

## Gene-specific notes: B. subtilis yueD (O32099, BSU31840)

The set-level notes above are shared across the four RHEA:25968 genes. What is
specific to this one:

- **Nothing about this protein has been measured.** It is the only member of the
  set with no experimental data of any kind. Every annotation it carries is an
  inference, and UniProt says so explicitly, basing both its FUNCTION and its
  SUBCELLULAR LOCATION lines on ECO:0000250|UniProtKB:Q8RJB2, the B. cereus
  ortholog. For that reason this review asserts **no core function**: recording
  one would convert an inference into a claim about an unassayed protein.
- **Why the B. cereus quotes are legitimate here.** The supporting quotes on the
  cytoplasm and GO:0016616 rows come from the B. cereus characterization. That
  is appropriate because homology to Q8RJB2 *is* the stated basis of the
  annotation, and the reasons now say so explicitly. This differs from the
  yeast files, where B. cereus quotes were supporting yeast-specific rows and
  were corrected after PR review.
- **The asymmetry between GO:0004090 and GO:0004757.** This review refines
  GO:0016616 to GO:0004090 on 41% identity, yet leaves the sepiapterin reductase
  IBA UNDECIDED on the same identity. That is deliberate, and the reason now
  states it: GO:0004090 names a chemistry every characterized family member
  performs, whereas GO:0004757 asserts a specific pterin substrate that no
  Bacillus family member has ever been tested on. Homology at this distance
  carries a reaction class but not a substrate.
- **BH4 is the clean REMOVE.** Tetrahydrobiopterin biosynthesis is an animal
  pathway and B. subtilis is not known to run it, so the PTHR44085 IBA to
  GO:0006729 is a pathway-context failure independent of how the enzyme behaves.
  B. subtilis does have a PTPS-family protein, but it serves queuosine rather
  than BH4, which is the kind of near-miss that makes this propagation
  plausible-looking.
- **41% identity to a characterized ortholog is the whole evidence base.**
  [PMID:11745140 "Bacillus subtilis yueD protein (41% identity)"].
