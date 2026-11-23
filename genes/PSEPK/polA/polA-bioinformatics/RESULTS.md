# PolA (Q88RK6, PP_0123) active-site conservation versus E. coli DNA polymerase I (P00582)

Method: `residue_conservation.py` (Biopython global alignment, BLOSUM62, gap open -10,
extend -0.5) of the P. putida KT2440 PolA sequence against E. coli Pol I, both read from
the cached UniProt flat files. Region boundaries are the E. coli UniProt DOMAIN/REGION
features (5'-3' exonuclease 1-323, 3'-5' exonuclease 324-517, polymerase 521-928).
Polymerase active-site residues R668, Y766, R841, N845, Q849 and D882 are the Klenow
residues named in PMID:2201688; D705 and E883 (palm carboxylates) and the 3'-5'
exonuclease metal-ligand residues D355, E357, D424, D501 and Y497 are the classic Klenow
fragment active-site residues from the structural literature (not quoted from a cached
abstract). The script checks that E. coli carries each expected residue at the stated
position before mapping it. Raw output: `polA_vs_ecoli.txt`.

Command:

    python residue_conservation.py ../polA-uniprot.txt ../../../ECOLI/polA/polA-uniprot.txt \
      --site D355 --site E357 --site D424 --site D501 --site Y497 \
      --site R668 --site Y766 --site R841 --site N845 --site Q849 \
      --site D705 --site D882 --site E883 \
      --region 5-3_exonuclease:1-323 --region 3-5_exonuclease:324-517 --region polymerase:521-928

## Results

- Overall: 585 identical residues over the 928-residue E. coli sequence (63.0%); 911 reference positions aligned.
- All 13 checked E. coli residues are present at the stated E. coli positions and all align to identical residues in Q88RK6.
- 3'-5' exonuclease site: E. coli D355, E357, D424, D501, Y497 align to Q88RK6 D339, E341, D408, D487, Y483.
- Polymerase site: E. coli R668, D705, Y766, R841, N845, Q849, D882, E883 align to Q88RK6 R655, D692, Y753, R828, N832, Q836, D869, E870.
- Domain identity: 5'-3' exonuclease 59.8% (306/323 aligned), 3'-5' exonuclease 62.4%, polymerase 66.4%.

## Interpretation

P. putida PolA retains the full three-domain Pol I architecture with intact polymerase and
3'-5' proofreading active-site residues, unlike type-A polymerases in which the
proofreading domain is degenerate. The 5'-3' exonuclease domain is well conserved at the
domain level; individual 5' nuclease carboxylates were not mapped here.
