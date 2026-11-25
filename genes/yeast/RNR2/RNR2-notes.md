# RNR2 (P09938) notes

Module: `dntp_de_novo_synthesis`, role = radical-bearing small (R2/beta) subunit.

## Evidence journal
- Active small subunit is the Rnr2/Rnr4 heterodimer; Rnr2 homodimer inactive [PMID:10716984 "The specific activity of the Rnr2p complexed with Rnr4p is 2,250 nmol deoxycytidine 5'-diphosphate formed per min per mg, whereas the homodimer of Rnr2p shows no activity."]
- Rnr2 binds iron; Zn in the Fe2 site of the as-crystallised protein [PMID:11526233 "A single metal ion, assigned as Zn(II), occupies the Fe2 position in the Y2 active site."; "Treatment of the crystals with Fe(II) results in difference electron density consistent with formation of a diiron center."]
- Nuclear storage, cytoplasmic in S phase/damage [PMID:12732713 "Under genotoxic stress, Rnr2 and Rnr4 become redistributed to the cytoplasm in a checkpoint-dependent manner."; PMID:18851834 "In response to S phase or DNA damage, Rnr2-Rnr4 enters the cytoplasm to bind Rnr1, forming an active complex."]

## Annotation decisions
- Protein binding IPI: MODIFY to protein heterodimerization activity (GO:0046982) for Rnr4 small-scale data; REMOVE for Rnr1 (captured by complex) and high-throughput rows.
- Zinc ion binding IDA: MARK_AS_OVER_ANNOTATED (crystallographic metal substitution in the iron site).
- Molecular adaptor activity (EXP, PMID:11526233): MARK_AS_OVER_ANNOTATED; the paper attributes the helper role to Y4 (Rnr4), not Rnr2.
- Oxidoreductase activity IEA: MODIFY to GO:0004748.
- GO:0106387 GMP biosynthesis RCA: REMOVE.
