# alt1 (SPBC582.08, UniProt Q10334) notes

Putative alanine aminotransferase (EC 2.6.1.2). No S. pombe experimental data in GOA or UniProt; everything is by similarity to S. cerevisiae Alt1 (P52893).

- [UniProt:Q10334 "Reaction=L-alanine + 2-oxoglutarate = pyruvate + L-glutamate;"]; [UniProt:Q10334 "FUNCTION: Alanine aminotransferase involved in both alanine"] (ECO:0000250 P52893).
- Location: [UniProt:Q10334 "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}. Mitochondrion"] — cytoplasm is a curator inference, mitochondrion by similarity.
- Sequence observation: alt1 is 490 aa [UniProt:Q10334 "SEQUENCE   490 AA;"] and begins [UniProt:Q10334 "MSDLDGFCQN AFSDLNSLNQ QVFKANYAVR GALAILADEI"] — acidic (D3, D5, D14), only K24/R30 basic in the first 30 residues, no annotated transit peptide. S. cerevisiae Alt1 is 592 aa with [file:yeast/ALT1/ALT1-uniprot.txt "TRANSIT         1..64"]. So alt1 lacks the N-terminal extension that targets budding-yeast Alt1 to mitochondria; it resembles cytosolic ALTs in length. (Simple visual inspection; no targeting predictor run.)
- S. cerevisiae: [PMID:19396236 "under respiratory conditions, Alt1p constitutes the sole pathway for alanine biosynthesis and catabolism"]; paralog Alt2 inert [PMID:23049841 "only Alt1 displays alanine aminotransferase activity; in contrast ALT2 encodes a catalytically inert protein"]. S. pombe has a single ALT (PTHR11751:SF29).

## GO-CAM / module disagreement
- PomBase GO-CAM gomodel:67c10cc400000148 places both alt1 activities (alanine biosynthesis, alanine catabolism) in the **mitochondrial matrix** (IC). Module text also says "S. pombe alt1 enables GO:0004021 in the mitochondrial matrix". Given the missing transit peptide, I marked the mitochondrion/matrix rows UNDECIDED and accepted cytoplasm (UniProt curator inference) as best-available; core function gives no location.
- S. cerevisiae ALT1 review core location = mitochondrial matrix; differs here deliberately.
- GOA also has L-glutamate biosynthetic process IC (glutamate GO-CAM) -> non-core.
