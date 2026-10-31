# SMIM5 (Q71RC9) review notes

## 2026-10-03 Tier 2 microprotein review

### Identity
- UniProt Q71RC9 SMIM5_HUMAN, 77 aa, PE1; alias C17orf109. One predicted helical TM segment
  (32-52) followed immediately by a cysteine cluster (CSCCCTHCCC, residues 53-62) and a short
  basic/proline-rich C terminus. Membrane / single-pass is curator inference (ECO:0000305).
- Family: Pfam PF15831 SMIM5_18_22, InterPro IPR031671 (SMIM5/18/22), PANTHER PTHR37344.
  SMIM22 (CASIMO1) is the only family member with a published function (SQLE-associated ER
  microprotein; see genes/human/SMIM22). Function should not be transferred from SMIM22 to SMIM5.
- Expression: HPA "Tissue enhanced (kidney)" (UniProt DR line). HPA JSON (fetched 2026-10-03):
  kidney nTPM 32.7, immune-cell enriched in plasmacytoid DC; antibody IF main location "Vesicles",
  additional "Golgi apparatus". Not in GOA and not used for annotation.

### Literature search
- PubMed `SMIM5[tiab] OR C17orf109[tiab]` -> 5 hits, all expression/genetic lists:
  PMID:42270003 (higher SMIM5 mRNA in diabetic-retinopathy blood), PMID:30275705 (hub gene in oral
  squamous cell carcinoma co-expression network), PMID:24318988 (differentially expressed in ccRCC),
  PMID:39364777 (chicken GWAS candidate), PMID:33584805 (cattle selection signature). None tests
  protein function, so none is cached or cited.

### GOA rows
- 7 x protein binding (IPI) from HuRI [PMID:32296183]: SGTA (O43765), ARFIP1 (P53367), EHHADH
  (Q08426), PRRT2 (Q7Z6L0), RBFA (Q8N0V3), ZFYVE21 (Q9BQ24), SH3GLB1 (Q9Y371).
  - SGTA (NbExp=9 in UniProt) is a cytosolic quality-control factor that engages exposed hydrophobic
    TMDs of mislocalized membrane proteins [PMID:23129660 "SGTA does not simply
    mask the exposed hydrophobic transmembrane domain of a mislocalized protein"]. An SGTA hit
    for a single-pass TM peptide is expected client recognition.
  - The others are a mixed set (mitochondrial RBFA, peroxisomal EHHADH, BAR-domain ARFIP1/SH3GLB1,
    membrane PRRT2, FYVE ZFYVE21) with no shared pathway; no follow-up exists.
  -> REMOVE all seven; no informative MF.
- membrane IEA -> ACCEPT.

### Conclusion
No function known. No core function, no NEW terms.
