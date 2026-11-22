# FAS1 (YKL182W, P07149) notes

- Beta subunit of the cytosolic type I fungal FAS (alpha6beta6, 2.6 MDa) [UniProt:P07149 "SUBUNIT: [Alpha(6)beta(6)] hexamers of two multifunctional subunits"]; [PMID:19679086 "The fungal type I fatty acid synthase (FAS) is a 2.6 MDa multienzyme complex, catalyzing all necessary steps for the synthesis of long acyl chains"].
- Beta-chain domains: AT, MPT (malonyl/palmitoyl transferase), DH, ER [PMID:18725634 "the 230-kDa β-chain harbors an acetyl transferase and a malonyl/palmitoyl transferase domain (AT/MPT), as well as a dehydratase and an ER domain"]; [PMID:374077 "malonyl, palmitoyl and acetyl transferase, enoyl reductase and dehydratase were shown to be exclusive functions of the beta chains of the complex"].
- Malonyl and palmitoyl transfer by one enzyme (MPT) [PMID:1100391 "From this it is concluded that both transfer reactions are catalyzed by the same enzyme"].
- Overall reaction EC 2.3.1.86 (acyl-CoA product, NADPH for both reductions) [UniProt:P07149 "Reaction=acetyl-CoA + n malonyl-CoA + 2n NADPH + 4n H(+) = a long-"]. Hence:
  - GO:0004318 enoyl-ACP reductase (NADH) from EC 1.3.1.9 mapping is wrong cofactor; GO:0141148 (NADPH) correct.
  - GO:0016297 fatty acyl-ACP hydrolase (EC 3.1.2.14) wrong: yeast FAS releases acyl-CoA via MPT, not free acid.
  - GO:0008410 CoA-transferase (RCA) wrong: MPT transfers acyl group to CoA, not CoA group.
  - GO:0004312 (EC 2.3.1.85, free FA product) less accurate than GO:0004321.
- fas1 mutants require fatty acids and die on starvation [PMID:4127627].
- Cytosolic [PMID:6025308]; mitochondrial HDA likely contamination by an extremely abundant cytosolic complex (91800 molecules/cell; UniProt).
- Lipid droplet IDA (PMID:17803462) - abstract does not report it; full text not available.
