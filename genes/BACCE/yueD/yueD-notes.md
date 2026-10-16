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

## Structural + kinetic analysis (OpenScientist, AlphaFold)

The one run of the five that delivered the measurement I asked for, and it
qualified my own quinone speculation.

**What it measured.** AlphaFold model AF-Q8RJB2-F1 **v6** (the v4 URL in my
seed context 404s), global pLDDT 96.8. SDR catalytic tetrad
Asn86/Ser140/Tyr154/Lys158 at pLDDT 98.0-98.9, Rossmann motif TGTSQGLG at
residues 7-14. The substrate pocket is 33 residues, mean pLDDT 97.1, and
**enclosed** (only 7% of 400 probe rays escape). Candidate sterics from PubChem
3D: benzil is 10.0 A across and twisted (plane-RMSD 0.39), 1,4-naphthoquinone
is 5.3 A and perfectly flat (0.00), methylglyoxal 3.7 A. So the pocket does
discriminate sterically, and in the direction the reported affinities predict:
bulky twisted benzil binds worst.

**Where it corrected me.** I had read the low naphthoquinone Km as hinting at
quinone detoxification. Four arguments against making that the function:

1. **Affinity is not efficiency.** By kcat/Km the best substrate is
   1-phenyl-1,2-propanedione (3.93 min-1 uM-1), about 15x better than
   1,4-naphthoquinone (0.268) and 47x better than benzil (0.084). The best
   substrate is another synthetic diketone.
2. **Family context points elsewhere.** Foldseek's nearest named neighbours are
   B. subtilis YueD, yeast Irc24, then sepiapterin reductases and SDR
   ketoreductases. No quinone reductase appears at all.
3. **The real bacterial quinone does not fit.** Menaquinone is a large
   lipophilic isoprenoid; this pocket is small and soluble.
4. **The mechanism may be the opposite of detoxification.** In human SPR,
   quinone handling is NADPH-dependent redox cycling at the cofactor site,
   distinct from sepiapterin reduction and separable from it by the D257H
   substrate-site mutation
   [PMID:23640889 "These data indicate that SPR-mediated reduction of sepiapterin and redox cycling occur by distinct mechanisms."].
   That generates ROS rather than clearing an electrophile.

Both points are now knowledge_gaps on the core function rather than claims.

**Quality signal.** The run self-corrected mid-analysis: iteration 2 misread
UniProt's "in decreasing order" phrasing as a preference ranking; iteration 3
fetched the actual Km/kcat table and reversed its own judgment, flagging the
change explicitly. Its honest limitations are also stated: the model is apo, so
pocket metrics are geometric rather than energetic, and no docking or MD was run.

**Corroborations.** It independently endorses GO:0004090 as the best-supported
general core MF, and independently flags GO:0004757 (sepiapterin reductase) and
GO:0006729 (BH4 biosynthesis) as TreeGrafter-only inferences with no BH4 pathway
known in B. cereus - the same calls this review makes.
