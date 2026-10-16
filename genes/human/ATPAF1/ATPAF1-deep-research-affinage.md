---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ATPAF1
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q5TC12
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 9
citation_count: 9
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ATPAF1 (human)

## Current model (mechanistic narrative)

ATPAF1 (Atp11p) is a mitochondrial matrix molecular chaperone that mediates a late step in assembly of the F1 catalytic sector of the mitochondrial ATP synthase [PMID:1532796, PMID:12206899]. It binds selectively and physically to unassembled F1-ATPase beta-subunits, engaging residues Gly-114–Leu-318 of the beta-subunit nucleotide-binding domain — the same surface that contacts alpha-subunits in the mature enzyme — such that incoming alpha-subunits displace ATPAF1 to drive formation of the alpha3beta3 hexamer; in its absence alpha and beta subunits accumulate as inactive aggregates [PMID:1532796, PMID:10681564]. The chaperone activity operates through a defined hydrophobic surface that shields aggregation-prone subunits, and ATPAF1 can hold a generic unfolding substrate (insulin B chain) as well as its natural beta-subunit client in vitro [PMID:11522798, PMID:12829692]. The functional core of the protein maps to residues Phe-120–Asn-174, with the N-terminal targeting sequence and disordered N-terminus dispensable for activity [PMID:8617760, PMID:12829692]. This chaperone function is structurally and functionally conserved from yeast through Drosophila to human, as human ATPAF1 complements the yeast mutant [PMID:10386611, PMID:11410595].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0044183 protein folding chaperone, GO:0098772 molecular function regulator activity
- **localization:** GO:0005739 mitochondrion
- **pathway (Reactome):** R-HSA-1852241 Organelle biogenesis and maintenance
- **partners:** ATP5F1B
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1992 | High | ATP11 (Atp11p) encodes a 37 kDa mitochondrial protein in S. cerevisiae; loss-of-function mutations cause alpha and beta subunits of F1-ATPase to accumulate as inactive aggregates, indicating a required role in a late step of F1 assembly. In vitro import assays and immunochemical evidence confirmed mitochondrial localization. Affinity-purified biotinylated Atp11p co-purified with alpha and beta subunits of F1-ATPase, indicating physical association. | PMID:1532796 | The Journal of biological chemistry |
| 1995 | Medium | Recombinant mature Atp11p produced in bacteria retains biological activity as confirmed by yeast complementation assays, establishing that the N-terminal targeting sequence is dispensable for function and that the mature protein alone is sufficient for F1-ATPase assembly activity. | PMID:7771799 | Archives of biochemistry and biophysics |
| 1996 | High | The active domain of Atp11p was mapped to residues Phe-120 through Asn-174 by limited proteolysis and deletion mutagenesis. The N-terminal 39 residues constitute the mitochondrial targeting domain. Nonsense mutations throughout the mature protein sequence cause loss of function, indicating that overall protein structure (not a localized catalytic active site) is required for activity. Flanking domains (Glu-40–Ser-109 and Arg-183–Asn-318) are important for protein stability inside mitochondria. | PMID:8617760 | The Journal of biological chemistry |
| 2000 | High | Atp11p binds selectively to the beta-subunit of F1-ATPase. Biotinylated Atp11p pulled down the F1 beta-subunit from yeast mitochondrial extracts. Yeast two-hybrid analysis mapped the Atp11p-binding region to residues Gly-114–Leu-318 of the beta-subunit nucleotide-binding domain — a region that contacts alpha-subunits in the assembled enzyme, suggesting alpha-subunits may exchange for Atp11p during F1 assembly. | PMID:10681564 | The Journal of biological chemistry |
| 1999 | Medium | A Drosophila homolog of Atp11p (from D. yakuba gene 2A5) complements the respiratory-deficient phenotype of yeast atp11::HIS3 deletion mutants and interacts with the S. cerevisiae F1 beta-subunit in the yeast two-hybrid assay, establishing functional conservation of Atp11p chaperone activity in higher eukaryotes. | PMID:10386611 | FEBS letters |
| 2001 | High | Atp11p acts as a molecular chaperone by preventing unassembled F1-ATPase beta-subunits from aggregating in the mitochondrial matrix. Its chaperone activity is mediated by hydrophobic interactions: a hydrophobic surface identified by bis-ANS fluorescence probe binding accommodates up to three bis-ANS molecules cooperatively, and binding of even a single bis-ANS molecule virtually eliminates chaperone activity. Atp11p also protects the insulin B chain from aggregating in vitro (surrogate chaperone substrate). | PMID:11522798 | The Journal of biological chemistry |
| 2001 | High | Human ATP11 (ATPAF1) and ATP12 proteins functionally complement their yeast counterparts, establishing that human Atp11p is a conserved assembly factor (chaperone) for the F1-ATPase in human mitochondria. The human ATP11 gene spans 24 kb in 9 exons and maps to chromosomal locus 1p32.3-p33. | PMID:11410595 | The Journal of biological chemistry |
| 2002 | High | Atp11p and Atp12p are molecular chaperones specifically required for assembly of the alpha and beta subunits of the mitochondrial F1-ATPase oligomer (alpha3beta3gamma-delta-epsilon); without them, alpha and beta subunits form inactive aggregates. This chaperone function is conserved between yeast and human mitochondria. | PMID:12206899 | Biochimica et biophysica acta |
| 2003 | High | A truncated recombinant Atp11p lacking 67 N-terminal residues (Atp11pTRNC) retains full molecular chaperone activity in vitro against both reduced insulin (surrogate substrate) and the natural substrate F1 beta-subunit. Preliminary 15N-1H HSQC NMR spectra show the truncated protein is well-ordered, indicating the disordered N-terminal region is dispensable for chaperone function. | PMID:12829692 | The Journal of biological chemistry |

## Citations

- PMID:10386611
- PMID:10681564
- PMID:11410595
- PMID:11522798
- PMID:12206899
- PMID:12829692
- PMID:1532796
- PMID:7771799
- PMID:8617760
