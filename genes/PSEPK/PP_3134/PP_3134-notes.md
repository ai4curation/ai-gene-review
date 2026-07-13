# PP_3134 notes

2026-07-09 PDT / 2026-07-10 UTC: First-pass cell-envelope bucket curation.
The fetched GOA table has only broad transferase activity. UniProt is more
informative: it records O-acyltransferase activity, lipid A biosynthetic
process, and hexapeptide/LpxA-like acyltransferase-family domains
[file:PSEPK/PP_3134/PP_3134-uniprot.txt "DR   GO; GO:0008374;
F:O-acyltransferase activity; IEA:TreeGrafter."; file:PSEPK/PP_3134/PP_3134-uniprot.txt
"DR   GO; GO:0009245; P:lipid A biosynthetic process; IEA:UniProtKB-KW.";
file:PSEPK/PP_3134/PP_3134-uniprot.txt "DR   InterPro; IPR051159;
Hexapeptide_acetyltransf."; file:PSEPK/PP_3134/PP_3134-uniprot.txt "DR
InterPro; IPR011004; Trimer_LpxA-like_sf."].

Decision: modify the broad transferase GOA row toward O-acyltransferase
activity and add conservative NEW O-acyltransferase/lipid-A-process rows from
UniProt metadata. Do not assign a substrate-specific lipid A acyltransferase
term until the PP_3134 substrate is resolved.
