# GSTF11 (Q96324, At3g03190) review notes

## Session 2026-09-30

### Identity and biochemistry
- Phi-class GST (PANTHER PTHR43900:SF64). UniProt function and EC are by similarity to GSTF9 (O80852).
- No direct enzymology: recombinant protein insoluble [PMID:19174456 "Only GSTF11 and GSTF12 were undetectable in the soluble fraction."]; also [PMID:35145536 "The enzymatic activity of GSTF11 was undetectable because of the protein could not be isolated and purified in vitro due to the rare abundance."].
- Indirect in vivo support: overexpression in Brassica napus raises leaf GST activity [PMID:34961200 "A higher GSTF11 mRNA content in transgenic plants was accompanied by an increase in the activity of the GST enzyme by an average of 30%"].

### Glucosinolates
- MYB28-regulated [PMID:17420480 "Transcriptome analyses of myb28 and Myb28 -overexpressing cell cultures indicated that both of them are regulated by Myb28"].
- CRISPR gstf11: some aliphatic GSLs reduced, indolic unaffected [PMID:35145536 "no significant changes in the abundance of indolic GSLs were noted in gstf11 (Figures 4A,B) and gstu20 (Figures 5A,B) mutants"]; weaker than gstu20; authors note the gstf11 lesions are late in the gene (possible partial function).
- Mikkelsen et al. 2010 glucoraphanin engineering in tobacco (PMID:20457641, abstract-only) is cited by Zhang et al. as showing GSTF11 is not essential for heterologous production; not verified from the abstract.
- Decision: no NEW GO:0019761, same reasoning as GSTU20 (see GSTU20-notes.md): necessity evidence only, no activity on the native intermediate, non-null double mutant, possible non-enzymatic conjugation. Comparators: GSTF9/GSTF10 lack glucosinolate terms; GSTU13 has IMP indole glucosinolate catabolic process (acts_upstream_of_or_within).

### Stress
- B. napus 35S:AtGSTF11 lines: reduced powdery mildew growth [PMID:34961200 "In most of transgenic plants, mycelium growth was inhibited"]; transgene cold-responsive. Heterologous and correlative; no NEW defense/cold terms proposed.
- IEP response to oxidative stress (PMID:9449849): Al-induced GST clone identified only by identity to a Kiyosue et al. 1993 GST; locus not named and oxidative-stress link is by citation -> UNDECIDED.

### Action tally
- ACCEPT 7, KEEP_AS_NON_CORE 3, UNDECIDED 1, NEW 0 (11 rows).
