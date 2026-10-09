# EPF2 (At1g34245, Q8LC53) curation notes

Session 2026-10-06 (stomatal_lineage_development module). Falcon deep research (`just deep-research-falcon ARATH EPF2`) failed with HTTP 402 (provider quota), so no provider deep-research file exists; notes below are from cached primary literature.

## Identity
- UniProt Q8LC53 EPF2_ARATH, 120 aa, signal peptide 1-25, mature MEPF2 chain 69-120, four disulfides; plant cysteine-rich secretory peptide family, EPF subfamily.

## Key findings
- Produced by MMCs and early lineage cells; limits MMC fate non-cell-autonomously [PMID:19435754 "Our results suggest that EPF2 inhibits cells from adopting the MMC fate in a non-cell-autonomous manner, thus limiting the number of MMCs."].
- Loss -> excess small lineage cells; overexpression -> virtually no stomata [PMID:19398336 "In the absence of EPF2, excessive numbers of cells enter the stomatal lineage..."].
- Direct ligand of ERECTA (primary) with TMM as modulator [PMID:22241782 "Our results place the ERECTA family as the primary receptors for EPFs with TMM as a signal modulator and establish EPF2-ERECTA and EPF1-ERL1 as ligand-receptor pairs"]; MEPF2 also binds TMM [PMID:22241782 "MEPF2, unlike MEPF1, exhibited binding to TMM in addition to ERECTA and ERL1"].
- Stomagen competes with EPF2 for ER/TMM; EPF2 elicits MPK3/6 phosphorylation within 10 min [PMID:26083750].
- Required for CO2 repression of stomatal development; CRSP protease cleaves EPF2 [PMID:25043023 "Moreover, EPF2 is essential for CO2 control of stomatal development."].

## Curation decisions
- Core MF: receptor ligand activity (GO:0048018, IBA accepted). IPI "protein kinase binding" rows MODIFIED to receptor ligand activity (TMM has no kinase domain; ERECTA binding is ectodomain-ligand binding).
- Core BP: negative regulation of stomatal complex development (GO:2000122). Guard cell differentiation (IBA and IMP) MODIFIED to GO:2000122 - EPF2 acts at lineage entry and inhibits; IBA propagation_review records TERM_SCOPING_PROBLEM / regulatory sign.
- No GO-CAM models contain EPF2 (gocams/index.tsv checked).
