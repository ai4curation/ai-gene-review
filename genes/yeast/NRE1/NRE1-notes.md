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

## Gene-specific notes: NRE1 (P40579, YIR035C)

The set-level notes above are shared across the four RHEA:25968 genes. What is
specific to this one:

- **It was an orphan until 2023.** SGD characterized Nre1p as a protein of
  unconfirmed function; the MicroPublication paper is the first demonstration of
  any in vitro activity for it
  [PMID:37602278 "Thus, Nre1p is a benzil reductase in vitro and likely paralog of Irc24p."].
- **It has the structures; IRC24 does not.** Two crystal structures exist
  (PDB 3KZV at 2.00 A, 6UHX at 2.75 A, both unpublished elsewhere), while IRC24
  has only an AlphaFold model. The OpenScientist run exploited exactly this
  asymmetry, superposing the IRC24 model onto 6UHX.
- **The paralog pocket is shared, not diverged.** That run measured 1.36 A CA
  RMSD and found the substrate pocket 15/18 residues identical with the
  Ser-Tyr-Lys triad conserved, so the pocket is *more* conserved than the
  protein overall (52% identity). The single non-conservative near-pocket change
  is Nre1 Asp138 / Irc24 Gly145, in the second shell at 4.8 A. Consequence for
  curation: annotations should transfer symmetrically between the two genes, and
  this review's GO:0004090 call matches IRC24's for that reason.
- **Cofactor preference.** Km 0.39 mM for benzil with NADPH versus 0.96 mM with
  NADH (UniProt), i.e. the same ~2-fold NADPH preference reported for Irc24,
  which is why the NADPH-specific GO:0004090 is preferred over a cofactor-
  agnostic parent.
- **Localization is independently supported.** Two separate high-throughput
  datasets place Nre1 in the cytoplasm (PMID:11914276, PMID:14562095), and the
  2023 paper restates it
  [PMID:37602278 "High-throughput protein expression data confirm that Nre1p is cytoplasmic"].
  That quote now supports the keyword-mapped IEA row as well; an earlier draft
  used the paper's *B. cereus* GFP sentence there, which was a cross-organism
  citation and was corrected after PR review.
