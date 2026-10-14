# PINK1 notes

Deep research was not run: falcon times out in this environment and perplexity-lite is not installed. These notes are based on the 59 cached publications and the UniProt record.

## Core biology
- Phosphorylates ubiquitin at Ser65 [PMID:24751536 "Using mass spectrometry, we discovered that endogenous PINK1 phosphorylated ubiquitin at serine 65, homologous to the site phosphorylated by PINK1 in Parkin's ubiquitin-like domain."; PMID:24660806 "Remarkably, PINK1 directly phosphorylates Ser65 of ubiquitin in vitro."]
- Phosphorylates Ser65 in the Parkin Ubl domain [PMID:24660806], and polyubiquitin chains [PMID:25474007].
- Stabilized on the outer membrane of depolarized mitochondria, where it recruits Parkin [PMID:22354088 "when mitochondrial import is compromised by depolarization, PINK1 accumulates on the mitochondrial surface where it recruits the PD-linked E3 ubiquitin ligase Parkin from the cytosol"].
- The kinase domain faces the cytoplasm [PMID:18687899]. PARL cleaves PINK1 in healthy mitochondria [PMID:21426348].
- Other substrates: Miro [PMID:22078885], DRP1 S616 [PMID:32484300], TRAP1 [PMID:17579517].

## Curation decisions
- Annotations from PMID:19279012 (PINK1 knockdown increases mitophagy and fragmentation via oxidative stress) were marked as over-annotated, as indirect effects that run opposite to the canonical pathway.
- Positive regulation of cytochrome c release (IMP, PMID:19880420) was changed (MODIFY) to the negative regulation term. The full text shows that PINK1 depletion enhanced cytochrome c release.
- Terms that GOA labels obsolete (GO:1903747/GO:1903749) were changed to GO:0070585 protein localization to mitochondrion (PINK1-dependent recruitment of Parkin).
- All 34 protein binding rows were removed.
