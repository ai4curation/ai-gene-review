# Q7NUH2 (CV_2726) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 prediction files were not opened or used.

Identity: Q7NUH2 is the complete 147-aa product of CV_2726 (TrEMBL, PE 4). The HTH marR-type domain
covers residues 1-147. It is not a fragment, isoform or alternative gene model. No other UniProt entry
exists for this locus.

Evolutionary placement:
- PANTHER PTHR33164:SF43, "HTH-TYPE TRANSCRIPTIONAL REPRESSOR YETL". B. subtilis YetL (O31541) itself
  is now in PTHR42756:SF1, so the subfamily name is a historical label. [file:genes/CHRVO/Q7NUH2/Q7NUH2-bioinformatics/RESULTS.md]
- Reviewed SF43 members: Rv2887/MT2955 (M. tuberculosis) and Mb2911; TcaR (S. aureus); YwhA (B. subtilis);
  O33817 (Thauera); and Rv2011c/MT2066/Mb2034c. CV_2726 shares 20-29% global identity with the ones
  tested. Rv2887 (P9WME9) is the closest at 28.8%. E. coli MarR (SF87) is at 24.3%, so SF43 does not
  give a specific ortholog. Rv2887 is the best-characterized SF43 member: it represses htm (Rv0560c)
  and is released from DNA by salicylate or PAS (per UniProt P9WME9, citing PMID:26303802, 27432954, 28743871).
- PAINT: PTN002109389 (PTHR33164) carries IBD GO:0006355 (8 seeds) and GO:0006950 (seeds O34777 and P27245).
  CV_2726 receives both, by GO_REF:0000120 and TreeGrafter respectively.
- C. violaceum OhrR (CV_0210) is in SF5. The earlier draft's use of OhrR as a model was paralog analogy
  and has been dropped.
- Genome neighbours (KEGG): acyl-CoA hydrolase/dehydrogenase, TetR, metZ, hypothetical CV_2727, alcohol
  dehydrogenase CV_2728, marC. Not informative about the regulon.

Changes from the previous draft:
- GO:0003677: ACCEPT -> MODIFY to GO:0043565 (correct but general term).
- GO:0006950: UNDECIDED -> KEEP_AS_NON_CORE (defers to the PAINT node; no evidence of divergence).
- GO:0003700 and GO:0006355: ACCEPT. GO:0006351: MARK_AS_OVER_ANNOTATED (unchanged).
- Description rewritten. The OhrR/virulence speculation and the "stress adaptation" claim are removed.

Relative to review next: Rv2887 (P9WME9, M. tuberculosis H37Rv), the closest experimentally characterized
member of the same PANTHER subfamily. No review of it exists in the repo: genes/MYCTU has no Rv2887 folder, and no review cites P9WME9. No module under modules/ covers this gene.
Even so, the low identity means its regulon and ligand should not be transferred to CV_2726.
