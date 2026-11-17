# KT2440 bacterial microcompartment shell inventory

Script: `bmc_shell_inventory.py` (Python standard library only; queries the UniProt REST API).
Run: `python3 -I bmc_shell_inventory.py > bmc_shell_inventory.tsv` (run 2026-11-04).
Raw output: `bmc_shell_inventory.tsv`.

## Question

UniProt places KT2440 EutB (Q88QF1) and EutC (Q88QF2) in a bacterial microcompartment
by HAMAP rule (MF_00861, MF_00601), and GOA carries GO:0031469 and GO:0031471 IEA rows
for both. A microcompartment is a proteinaceous shell, so it can exist only if the
proteome encodes shell proteins. Does the KT2440 reference proteome encode any?

## Method

Count proteins carrying the two shell-protein signatures in the KT2440 reference
proteome (UP000000556), with E. coli K-12 (UP000000625) as a positive control:
Pfam PF00936 / InterPro IPR000249 (BMC domain: hexamer and trimer shell proteins such as
EutM, EutK, EutL, EutS) and Pfam PF03319 / InterPro IPR004992 (EutN/CcmL pentameric
vertex proteins). Also list the KT2440 genes PP_0538 to PP_0548 around eutBC.

## Results

| Proteome | PF00936 | IPR000249 | PF03319 | IPR004992 |
|---|---|---|---|---|
| P. putida KT2440 (UP000000556) | 0 | 0 | 0 | 0 |
| E. coli K-12 (UP000000625) | 4 | 4 | 1 | 1 |

The E. coli control finds the eut-operon shell proteins: EutL (P76541), EutS (P63746),
EutM (P0ABF4), EutK (P76540) and the vertex protein EutN (P0AEJ8).

KT2440 local locus (PP_0538 to PP_0548): PP_0542 eutC (Q88QF2), PP_0543 eutB (Q88QF1),
PP_0544 ethanolamine transporter (Q88QF0), PP_0545 aldB-I aldehyde dehydrogenase (Q88QE9)
and PP_0546 sigma-54 dependent transcriptional regulator (Q88QE8); the flanking genes
(ppa, mtfA, dedA, a GNAT acetyltransferase, mpl, ubiX) are unrelated to microcompartments.

## Interpretation

KT2440 encodes no BMC-domain or EutN/CcmL-domain protein anywhere in its reference
proteome, while the same queries recover the complete E. coli Eut shell set. With no
shell protein there can be no microcompartment, so EutB/EutC in KT2440 must act as a
free cytoplasmic enzyme. The HAMAP microcompartment location is transferred from
shell-encoding enterobacterial eut operons and does not apply to this organism.

Limitation: the inventory depends on UniProt's InterPro/Pfam match data for the
reference proteome; a highly divergent shell protein missed by both Pfam models
would not be detected. No such protein is present in the local eut locus.
