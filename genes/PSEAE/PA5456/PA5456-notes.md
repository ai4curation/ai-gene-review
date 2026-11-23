# PA5456 (PA5456, Q9HTB4) review notes

No deep-research API was available. Manual research on 2026-11-05: full text of
PMID:23341552 (cached, PMC3560663), a Europe PMC search for "(PA5455 OR PA5456)
AND glycosyltransferase" and for common polysaccharide antigen titles (PubMed MCP
and NCBI E-utilities returned server errors), and the UniProt record (unreviewed,
PE 4).

## Biology

- PA5456 (433 aa) is a predicted GT-B fold, GT4-family glycosyltransferase (Pfam
  PF13692 Glyco_trans_1_4; SUPFAM SSF53756; PANTHER PTHR46656:SF3) in the
  pa5455-pa5459 operon beside the rmd-wbpZ CPA cluster [PMID:23341552 "Gene
  sequence analysis indicated that pa5455 and pa5456 encode putative
  glycosyltransferases."].
- Deletion of PA5456 (in-frame, nonpolar) abolishes CPA; complementation restores it
  [PMID:23341552 "Mutation of either one of the two putative glycosyltransferase
  genes, pa5455 and pa5456, completely abrogated CPA biosynthesis"].
- Co-overexpression of PA5455 and PA5456 shortens CPA chains; the authors suggest a
  chain-length-determining or chain-terminating role [PMID:23341552 "One or both of
  the proteins encoded by these genes is therefore the best candidate for the
  catalyst of the chain length-determining reaction."]. They speculate PA5455 and
  PA5456 may act as a complex, without data.
- The paper's own summary of its evidence [PMID:23341552 "We have presented
  evidence from genetic studies that the genes in the pa5455-pa5459 cluster are
  involved in CPA biosynthesis in P. aeruginosa."]. Methods are RT-PCR, 5'-RACE,
  EMSA with E. coli RNA polymerase, promoter-trap beta-galactosidase assays,
  deletion mutants and arabinose-induced overexpression. No glycosyltransferase
  assay, no purified PA5455/PA5456.
- The D-rhamnan backbone of CPA is made by WbpZ, WbpY and WbpX, which have been
  assayed in vitro (PMID:25845842; PMID:35166992, not cached); no later paper
  found assays PA5455 or PA5456.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002288302 | GO:0016757 glycosyltransferase activity | 2 | 57 (43 taxa) | GO:0016757, IDA, PMID:23341552 (PseudoCAP) | UNVERIFIABLE | Full text read: GT activity is a sequence prediction; only genetics reported. The IDA code is wrong; the claim is plausible from the GT4 domain. | PA5455 (same paper, same problem) | No: the only other seed has the same defect, so the IBD has no experimental seed. Term likely true by domain. |

Defects: PSEUDOCAP WRONG_EVIDENCE_CODE (CONFIRMED) on the GO:0016757 IDA row and
on the GO:0009243 IDA row (should be IMP). The node-level GO_CENTRAL defect is recorded once, on the PA5455 review (genes/PSEAE/PA5455/PA5455-ai-review.yaml, GO:0016757 IBA row); this review cross-references it and does not repeat it.

## Action summary

ACCEPT: GO:0016757 (IBA, IDA), GO:0009243 (IDA). TOO_GENERAL: GO:0009103 (IMP).
