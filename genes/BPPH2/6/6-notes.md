# phi29 gene 6 (protein p6, P03685) review notes

## Provenance / method

- Deep research was NOT available in this container (no provider API keys), so no
  `6-deep-research-*.md` file exists. Research was done directly from cached
  publications, the UniProt record, the PubMed MCP and WebFetch.
- All cached primary papers except PMID:15247336 are abstract-only.
- PMID:12426390 (CACAO source for 4 rows): PMC137212 full text was not returned by
  the PubMed MCP (empty full_text) and Europe PMC returned HTTP 500; a WebFetch of
  the PMC HTML page (pmc.ncbi.nlm.nih.gov/articles/PMC137212/) returned a
  model-generated per-figure summary (not cached, so not quotable). It reported:
  Fig. 1 in vitro transcription (p6 enhances p4 repression of A2c and activation of
  A3; p4 C-terminal deletion p4(CΔ14+2) fails to repress A2c with p6); Fig. 2/3
  DNase I footprinting (p4 increases p6 affinity >16-fold and sets the p6 complex
  boundary); Fig. 4/5 RNAP footprint and band shift (stable p4–p6–DNA complex
  displaces RNAP from A2c); Fig. 6 p4 site mutants; and explicitly "no sus6 or amber
  mutant experiments". All mutants in the paper are mutants of p4 or of DNA sites,
  not of p6.
- GONUTS wiki (gowiki.tamu.edu PMID:12426390 and PMID:820555 pages) returned
  "This site is temporarily offline while we perform upgrades" on 2026-10-29, so the
  student evidence could not be checked.
- PMID:820555 (1976) full text: Wiley returned HTTP 403.

## Biology

- Very abundant early, non-sequence-specific dsDNA-binding protein; DNA wraps as a
  right-handed superhelix around a multimeric p6 core via the minor groove
  [PMID:2111580 "support a model in which a DNA right-handed superhelix tightly wraps around a
  multimeric p6 core. The interaction occurs through the DNA minor groove."].
- N-terminal amphipathic helix binds DNA [PMID:7925279 "an alpha-helical structure located in the
  N-terminal region of protein p6 is involved in DNA binding through the minor
  groove."].
- Dimer is the active form in vivo; dimerization mutants fail to complement sus6 for
  DNA replication [PMID:12383516 "they do not support phage DNA replication in a
  trans-complementation assay with phi29sus6 mutant-infected B. subtilis cells"].
- Binds most of the viral genome in vivo, highest at the ends (origins); specificity
  via low negative supercoiling [PMID:15118076 "protein p6 binds to most, if
  not all, the viral genome in vivo, although with higher affinity for both DNA
  ends, which contain the replication origins"].
- Activates initiation of protein-primed replication [PMID:2111580 "required for the protein-primed initiation of replication"].
- p17 optimizes p6 binding at DNA ends [PMID:12480935].
- Transcription: represses C2 by impairing closed complex stability
  [PMID:11384991 "affecting specifically the stability of the closed complex"]; with p4
  represses A2b/A2c and activates late A3 [PMID:15362097 "together with protein p4, it represses transcription from promoters A2b
  and A2c and activates late transcription from promoter A3"].
- p4 C-terminus contacts p6 to assemble repression complex [PMID:12426390 "stable assembly of this
  complex requires interaction between protein p6 and the C-terminus of protein
  p4"].

## CACAO rows

| Term | Ev | PMID | Action | Why |
|---|---|---|---|---|
| GO:0001217 DNA-binding transcription repressor activity | IMP | 12426390 | MODIFY -> GO:0030527 | p6 is a non-sequence-specific architectural protein, not a sequence-specific TF; paper's mutants are p4 mutants (evidence code doubtful) |
| GO:0017053 transcription repressor complex | IDA | 12426390 | KEEP_AS_NON_CORE | footprinting/band-shift show p4–p6–DNA complex that excludes RNAP from A2c |
| GO:0017053 transcription repressor complex | IMP | 12426390 | KEEP_AS_NON_CORE | same claim; IMP rests on p4 mutants |
| GO:0006351 DNA-templated transcription | IMP | 12426390 | MODIFY -> neg/pos regulation of viral transcription | p6 regulates, it is not transcription machinery (granularity) |
| GO:0039693 viral DNA genome replication (acts upstream, positive) | IMP | 820555 | ACCEPT | DNA-negative phenotype of gene-6 mutants; abstract doesn't name gene 6, consistent with later sus6 work |

Failure taxonomy: new-ish pattern "partner-mutant IMP" — IMP code applied to p6 when
the mutated protein was its partner p4; plus "regulator annotated to the regulated
process" (DNA-templated transcription) and "architectural protein typed as a
sequence-specific DNA-binding TF".
