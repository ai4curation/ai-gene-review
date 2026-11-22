# LRP5L iteration 2 provenance

Analyses run (all code executed in the OpenScientist python executor; outputs below are verbatim).

## 1. BLAT scan with the siamang ORF as query (UCSC BLAT JSON API)
Query sequences: reconstructed LRP5L ORFs from provenance/primate_ORFs.json.
Result: see table_species_distribution_v2.csv and table_blat_phylogeny_scan / scan_pongo.json /
scan_gibbon_macaque.json. The duplicate is recovered in Nomascus leucogenys (nomLeu3 chr7b,
447/455 = 98.24 % identity to the siamang ORF, 3 blocks over 10.2 kb) and is absent from
both T2T orangutan assemblies and from rheMac10, where the only hits are the LRP5 parent
locus at 91-93 % identity over a 20-22 kb intron-containing span.

## 2. Nomascus reconstruction
nomLeu3 chr7b:55,304,800-55,322,000 contains 3,215 N (18.7 %); the window where exon 1 is
expected (r[3700:4400], inside a 1,245-nt N block) is 100 % N, so exon 1 cannot be assessed.
Exons 2-4 rebuilt by glocal alignment: 172 + 217 + 104 = 493 nt, 6 + 4 + 2 substitutions vs
siamang, no net indel; translation of codons 90-252 gives 163 sense codons and the terminal
stop only, i.e. no premature stop.

## 3. Interlocus gene conversion test (4-sequence site patterns)
Sequences: HL human LRP5L, SL siamang LRP5L, HP human LRP5 parent projected onto the LRP5L
frame, SP siamang LRP5 parent projected onto the LRP5L frame.
Jukes-Cantor distances: HL-SL 0.0704, HP-SP 0.0160, HL-HP 0.0973, SL-SP 0.0913,
HL-SP 0.0958, SL-HP 0.0943. The two within-species paralog distances are not smaller than the
two between-species paralog distances, so there is no concerted evolution.
Site patterns: paralog-clustered 37, species-clustered (conversion signature) 1,
other 58, invariant 660. Binomial test 1 vs 37 against 50:50, p = 2.84e-10.

## 4. dN/dS, parent versus duplicate, same 229 codons, human vs siamang
LRP5 parent:    S=164.7 N=522.3 Sd=10.0 Nd=0.0  dS=0.0633 dN=0.0000 omega=0.00  Z=-3.13 p=0.0018
LRP5L duplicate:S=153.7 N=533.3 Sd=19.0 Nd=30.0 dS=0.1351 dN=0.0585 omega=0.433 Z=-2.28 p=0.0224
dS(duplicate)/dS(parent) = 2.13 (Poisson P = 0.0036 for the excess of synonymous changes).
Nonsynonymous: 30 observed in the duplicate, 0 in the parent over the same codons.

## 5. CpG masking sensitivity analysis
Codons containing any position in a CpG dinucleotide in either sequence were dropped.
human-siamang LRP5L:  all sites omega=0.438 (p=0.020) -> CpG-masked omega=0.789 (p=0.643)
human-chimp  LRP5L:   all sites omega=0.653 (p=0.420) -> CpG-masked omega=0.277 (p=0.142)
human-bonobo LRP5L:   all sites omega=0.744 (p=0.556) -> CpG-masked omega=0.340 (p=0.183)
human-siamang LRP5 parent: omega=0.000 in both treatments (Nd=0).
Caveat (PMID 18826599): presence/absence CpG assignment in a two-sequence alignment is itself
biased, most severely for closely related pairs, so the CpG-masked human-chimp and
human-bonobo values are unreliable. The human-siamang pair is the informative one.
