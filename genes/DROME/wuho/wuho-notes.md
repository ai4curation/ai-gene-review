# wuho (Q9W415; CG15897) review notes

## Identity
- WD40-repeat protein of the TRM82/WDR4 family; non-catalytic partner of Mettl1 in the tRNA
  m7G46 methyltransferase. [file:DROME/wuho/wuho-uniprot.txt "Required for the Mettl1-dependent formation of N(7)-"]

## Literature
- Wu et al. 2006: [PMID:16762337 "wh null mutants display male sterile and female semi-sterile phenotypes"];
  [PMID:16762337 "Yeast homologue with 5 WD40 repeats, Trm82, is the non-catalytic subunit of a tRNA methylase."];
  [PMID:16762337 "In wh mutant males, spermatogenesis is arrested at the elongating stage of the developing spermatids"];
  oogenesis defect: [PMID:16762337 "the cystocytes fail to arrest their cell division at the fourth mitotic cycle"].
  Immunostaining placed Wh in germ-cell nuclei (abstract mentions a bipartite NLS and hub-cell expression).
- Rastegari et al. 2020: Wh works with the TRIM-NHL protein Mei-P26 in ovarian germline homeostasis:
  [PMID:31941704 "Wh and Mei-p26 are epistatically linked"]; [PMID:31941704 "In GSC progeny, Wh and Mei-p26 silence nanos translation"].
  Reported cytoplasmic Wh in ovarian cells (UniProt).
- Kaneko et al. 2024: Mettl1-Wh heterodimer methylates tRNA; [PMID:39317727 "Drosophila Mettl1 required Wh for tRNA methylation"];
  [PMID:39317727 "Mettl1 associates with Wh in vivo and in vitro"]; the m7G-bearing 3' tRNA fragments were also lost in
  Wh mutant testes. Mei-P26, Nanos and Bgcn were not co-purified with Mettl1, suggesting separate Wh complexes.

## Decisions
- Core: non-catalytic subunit of tRNA (m7G46) methyltransferase complex; involved in tRNA
  (guanine-N7)-methylation. No single specific MF term exists for this activator role; used
  core function without MF, with complex + process.
- Spermatogenesis/oogenesis IMP: kept as non-core (phenotypes; spermatogenesis defect phenocopies Mettl1-KO).
- Protein binding IPI rows: removed as uninformative (interaction itself is real; captured by complex).
- Localizations (nucleus, germ-cell nuclei, cytoplasm, cytosol): accepted/kept per curator IDA/EXP.
