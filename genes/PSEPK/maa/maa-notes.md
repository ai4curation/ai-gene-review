# maa notes

2026-07-09 PDT / 2026-07-10 UTC: First-pass cell-envelope bucket curation.
`maa` entered the cell-envelope bucket because UniProt carries a lipid-A
biosynthesis keyword/cross-reference, but the stronger gene-level evidence is
for maltose O-acetyltransferase: UniProt names maltose acetyltransferase,
records EC 2.3.1.79, has GO:0008925, and annotates a Mac
maltose/galactoside-acetyltransferase domain [file:PSEPK/maa/maa-uniprot.txt
"DE   SubName: Full=Maltose acetyltransferase {ECO:0000313|EMBL:AAN70728.1};";
file:PSEPK/maa/maa-uniprot.txt "DE            EC=2.3.1.79
{ECO:0000313|EMBL:AAN70728.1};"; file:PSEPK/maa/maa-uniprot.txt "DR   GO;
GO:0008925; F:maltose O-acetyltransferase activity; IEA:UniProtKB-EC.";
file:PSEPK/maa/maa-uniprot.txt "FT                   /note=\"Maltose/galactoside
acetyltransferase\""].

Decision: accept maltose O-acetyltransferase activity and cytosol, keep generic
O-acetyltransferase as non-core, mark broad parent transferase/acetyltransferase
terms as over-annotated, and treat lipid-A context as a likely family-level
spillover pending direct evidence.
