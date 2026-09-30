# LAT (human, O43561) review notes

## Provenance / process

- 2026-09-30: `just deep-research-falcon human LAT --fallback perplexity-lite` exited with code 1 and
  produced no deep-research file (in this environment falcon runs were timing out at 600 s and the
  perplexity-lite fallback reported "Provider 'perplexity' not available"). The review was done
  without a deep-research file, from the UniProt record, the GOA-cited publications
  (`just fetch-gene-pmids`) and additional primary papers fetched with `just fetch-pmid`
  (PMIDs found by PubMed esearch: 10843385, 10567557, 10204488, 27242165; plus mouse source papers
  22561606, 23793062, 16002666 traced via QuickGO for ISS/IEA/IBA rows).
- Most GOA-cited LAT papers are cached abstract-only; quotes are from abstracts.

## Biology summary

- Palmitoylated (C26/C29) single-pass type III transmembrane adaptor, no catalytic domain
  [PMID:9729044 "palmitoylation at C26 and C29 is essential for efficient partitioning into GEMs"].
- Phosphorylated by ZAP70/SYK (also reported LCK, ITK) on Y132, Y171, Y191, Y226
  [PMID:9489702 "phosphorylated by ZAP-70/Syk protein tyrosine kinases leading to recruitment of multiple signaling molecules"].
- Docking map: Y132 -> PLCG1; Y171/Y191/Y226 -> GRB2; Y171/Y191 -> GADS
  [PMID:10811803]; Y171/Y226 -> VAV1 [PMID:12186560].
- Forms TCR signalosome / microclusters; phospho-LAT + GRB2-SOS1 phase separate into liquid-like
  condensates [PMID:27056844 "pLAT microclusters are liquid-like, phase-separated structures"].
- Also scaffold in FcepsilonRI mast cell signaling [PMID:10843385] and platelet GPVI signaling
  [PMID:10567557].
- Mouse KO: block at DN stage [PMID:10204488]; human LOF: combined immunodeficiency + autoimmunity
  (IMD52) [PMID:27242165]. TRAF6 K63-ubiquitinates LAT K88 [PMID:23514740].

## Curation decisions (key points)

- Core MF: GO:0030159 signaling receptor complex adaptor activity (IBA + IDA), with parent
  GO:0035591 accepted. NEW GO:0140693 molecular condensate scaffold activity (IDA, PMID:27056844);
  comparator: condensate partners SOS1 and NCK1 carry GO:0140693 by IDA.
- 17 `protein binding` IPI rows: MODIFY -> GO:0030159 when the paper maps LAT phosphotyrosine
  docking of an SH2 effector (PLCG1, GRB2, PIK3R1, VAV1); REMOVE for kinase/phosphatase-substrate
  pairs (ZAP70, LCK, PTPN1), high-throughput screens (EGFR MaMTH, EGFR proteomics, SGTA HuRI), a
  LAT-peptide control (SLAM paper) and the NTAL/LAB paper.
- COP9 signalosome (IEA+ISS from mouse Lat, UniProt IDA PMID:22561606): the source Tespa1 paper
  describes the *TCR signalosome*; MODIFY -> GO:0036398. Likely a signalosome term-selection error
  at source; raised as a suggested question.
- Cell-cell junction (IEA from mouse, PMID:23793062 Rltpr/CD28 at immunological synapse): MODIFY ->
  immunological synapse.
- Integrin-mediated signaling pathway (IDA PMID:15100278): paper shows TCR inside-out activation of
  beta1 integrins -> MODIFY to GO:0033625 positive regulation of integrin activation.
- Inflammatory response IBA: seeded by mouse LatY136F phenotype -> MARK_AS_OVER_ANNOTATED
  (necessity/phenotype, not participation).
- Positive regulation of protein kinase activity (IEP, RAG repression microarray paper) ->
  MARK_AS_OVER_ANNOTATED.
- NEW process terms: Fc-epsilon receptor signaling pathway (PMID:10843385) and
  collagen-activated signaling pathway (PMID:10567557); LAT does work in these pathways as the
  scaffold (same role as in TCR signaling), passing the participation test.
