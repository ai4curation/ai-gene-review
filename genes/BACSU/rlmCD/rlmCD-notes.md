# Bacillus subtilis RlmCD (YefA) review notes

## Identity and naming — 2026-10-26

The normal UniProt fetch identifies O31503, RLMCD_BACSU, 459 residues, strain 168, taxon 224308, locus BSU06730, primary gene rlmCD and aliases yefA/yerS. PMID:21824914 explicitly uses B. subtilis 168 (trpC2) and renames YefA as RlmCD. The scaffold was fetched with `just fetch-gene BACSU O31503 --alias rlmCD`. Original GOA assertions and raw UniProt/GOA bytes are retained; no annotation proposal was added.

## Direct primary evidence

PMID:21824914, full text, Methods and Results: “Bacillus subtilis 168 (trpC2) was used here as the reference strain with a wild-type rRNA modification pattern.” Native deletion and MALDI-MS assign both sites: “Analysis of the rRNA from the ΔyefA::Cm strain by MALDI-MS showed that methylation had been lost at both U747 (Figure 2D) and U1939 (Figure 2E and F).” An active yefA plasmid restores both methylations in that native deletion strain. Site numbers throughout this review are the paper's E. coli-equivalent numbers, not a claim that literal sequence coordinates are identical in every bacterium.

The E. coli ΔtrmA/ΔrlmC/ΔrlmD experiment is a separate heterologous test. Partial restoration of the two rRNA methylations (with stronger restoration at U1939) supports intrinsic dual-site recognition; it is not the sole evidence for B. subtilis chemistry. The tRNA HPLC control is also explicit: “Further HPLC analysis showed that YefA is not involved in m5U modification of tRNAs (Supplementary Figure S5).” In B. subtilis the unrelated folate-dependent TrmFO supplies tRNA U54 methylation. The paper reports no major viability effect from yefA deletion under standard laboratory conditions; neither universal essentiality nor a particular antibiotic-resistance phenotype follows from that result.

## All-row decisions and core

All eight seeded rows were reviewed. RNA processing (GO:0006396) and the two rRNA methylation rows (GO:0031167) refine to the already present rRNA base methylation term GO:0070475. RNA methyltransferase activity (GO:0008173) refines to existing GO:0070041, whose current definition specifies SAM-dependent formation of C5-methyluridine in rRNA. The three GO:0070041 rows and GO:0070475 are accepted as the directly demonstrated catalytic function/process. Thus four ACCEPT and four MODIFY decisions preserve all eight original assertions.

The IBA row descends from PTN000115109. The target accession among the descendant evidence is legitimate target-specific experimental support, not circularity; donor count is not used to assess the phylogenetic judgment. ARBA and InterPro mappings are reviewed against the native primary evidence, not quoted as proof of themselves. The core captures both rRNA sites under the existing MF and base-methylation process. No new process, tRNA activity, general antibiotic-response term or localization proposal is manufactured.

## Retrieval and limitations

Actual Falcon and perplexity-lite fallback requests were run concurrently with publication fetching. Falcon failed Edison authentication (403); fallback failed Perplexity quota/authentication (401). No provider research report was produced or fabricated. Normal gene-publication retrieval succeeded. A real `just fetch-fitness BACSU rlmCD` attempt failed because no mapped/local or reachable FEBA source was available; no fitness artifact was produced. Manual research above is based on the inspected primary full text, not provider prose. Logs and baseline/proof are under `.cache/module-audit-logs/rlmcd-*`.

Both strict/schema/source checks and ontology term validation pass without warnings. The unresolved physiological question concerns conditions under which these modifications confer fitness beyond the tested laboratory setting, not whether the two native chemical modifications are demonstrated.
