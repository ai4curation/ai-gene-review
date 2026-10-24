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

## 2026-10-15 journal: response to oxidative stress row resolved (PR #5026 follow-up)

Supersedes the "IEP response to oxidative stress (PMID:9449849) ... -> UNDECIDED" line and the action tally above (now ACCEPT 7, KEEP_AS_NON_CORE 3, REMOVE 1).

- GO:0006979 IEP (PMID:9449849) is REMOVE. The cached full text identifies the Al-induced clone only by >98% identity to the "GST ( Kiyosue et al., 1993 )", in the singular, without saying which Kiyosue clone. Kiyosue et al. 1993 (PMID:8253194) described two cDNAs, ERD11 and ERD13.
- Clone identities (UniProt): ERD11 = GSTF6 (P42760, At1g02930; GSTF6-uniprot.txt `Synonyms=ERD11, GST1, GSTF3`); ERD13 = GSTF10 (P42761, At2g30870; downloaded 2026-10-15 from https://rest.uniprot.org/uniprotkb/P42761.txt, `Synonyms=ERD13`). GSTF11 is At3g03190 (Q96324), legacy alias AtGSTF6.
- Sequence check (GSTF11-bioinformatics/pairwise_identity.py, output in RESULTS.md): global identity GSTF11 vs GSTF6/ERD11 39.6% (over alignment), GSTF11 vs GSTF10/ERD13 42.7%. Neither is compatible with a >98%-identical clone, so the clone is GSTF6 or GSTF10, not GSTF11. (An earlier "~42%" figure in the review reason was not recorded; it is replaced by these reproducible numbers.)
- The oxidative-stress link in the paper is by citation of ozone work, not measured for this clone.
