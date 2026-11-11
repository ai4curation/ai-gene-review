# GPAT2 (donkey): gene-model comparison against mouse Gpat2 (re-review, 2026-10-21)

Reproduce from this folder with:

    uv run --script compare_models_rereview.py mouse-Q14DK4-uniprot.txt models-vs-mouse-rereview.json ../GPAT2-uniprot.txt donkey-A0A8C4KXU5-uniprot.txt donkey-A0A8C4KXM4-uniprot.txt

Inputs were downloaded from the UniProt REST API on 2026-10-21: reviewed mouse Gpat2 Q14DK4 (801 aa, the
protein characterised in PMID:23611983, PMID:22905194, PMID:17689486 and PMID:22285183) and the two other
donkey GPAT2 TrEMBL entries. All three donkey entries carry the PANTHER subfamily PTHR12563:SF15
(GLYCEROL-3-PHOSPHATE ACYLTRANSFERASE 2, MITOCHONDRIAL), the same subfamily as mouse Q14DK4, rat D3ZI76
and human Q6NUI2 (interpro/panther/PTHR12563/PTHR12563-entries.csv). The orthology basis is that shared
subfamily, not the alignment scores below. Full output is in `models-vs-mouse-rereview.json`.

## Result

The three donkey entries are products of one Ensembl gene, ENSEASG00005002382.2 (chromosome 6):

| Entry | Length | Ensembl transcript | Identity to mouse (paired) | Mouse coverage | Mouse H205/D210 | Mouse TM1 (306-332) / TM2 (450-472) |
|---|---|---|---|---|---|---|
| A0A9L0ILJ0 (benchmark) | 718 | ENSEAST00005071166.1 | 78.64% of 707 | 88.26% | H, D at 205, 210 | both aligned |
| A0A8C4KXU5 | 800 | ENSEAST00005003415.2 | 83.75% of 800 | 99.88% | H, D at 205, 210 | both aligned |
| A0A8C4KXM4 | 723 | ENSEAST00005003419.2 | 85.06% of 723 | 90.26% | H, D at 205, 210 | TM1 region (mouse 275-345) missing |

A0A8C4KXU5 is full length: it lacks a partner only for mouse residue 363, and its C-terminal 30 residues
(`AGPMFHLSPTFASRDNQEKLEQFIRQFICG`) match the mouse C-terminus (`TGPQLHLSPTFATRDNQDKLEQFIRQFICS`).

The benchmark A0A9L0ILJ0 matches A0A8C4KXU5 through the acyltransferase domain, the HXXXXD motif
(`HKSLLD`, mouse 205-210) and both predicted transmembrane segments, but has no partner for mouse 650-696
and several shorter segments between 701 and 780, and ends in a different 30-residue tail
(`PHLPAGTIRKSWNSSFGSSFVARTVRWSPS`). It is therefore an alternative-transcript model of the same gene whose
last ~85 residues replace the conserved Gpat2 C-terminal region; whether that exon is real is not known.

## Limitations

Retention of H205 and D210 does not demonstrate enzymatic activity in donkey. The region of mouse Gpat2
that binds MILI/PIWIL2 has not been mapped, so whether the A0A9L0ILJ0 C-terminus affects that interaction
cannot be judged from sequence. Transmembrane positions are UniProt predictions for the mouse protein
(ECO:0000255) supported by the epitope-protection topology of PMID:22285183.
