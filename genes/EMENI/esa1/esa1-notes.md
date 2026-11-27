# EMENI esa1 notes

## 2026-10-11

- Fetched `EMENI/esa1` as UniProt `C8VBH4`. The Swiss-Prot entry places EsaA in
  `PTHR10615:SF218 HISTONE ACETYLTRANSFERASE ESA1`, carries the MYST-type HAT
  domain plus the C2HC MYST-type zinc finger, and infers nuclear/chromosomal
  NuA4 membership from fungal ESA1 orthologs.
- Cached the only PMID currently returned for the GOA rows, Soukup et al. 2012
  [PMID:22882998, "Overexpression of the Aspergillus nidulans histone 4
  acetyltransferase EsaA increases activation of secondary metabolite
  production."]. The full text directly establishes that `AN10956.4`, renamed
  `esaA`, is a fungal ESA1 homolog that can complement budding-yeast `ESA1`;
  that overexpression of A. nidulans `esaA` increases histone H4K5/H4K8/H4K12
  acetylation; and that increased H4 acetylation correlates with increased
  activation of sterigmatocystin, penicillin, terrequinone, and orsellinic-acid
  secondary-metabolite clusters.
- Reviewed `interpro/panther/PTHR10615/PTHR10615-paint.tsv`. The important IBA
  sources are the broad eukaryotic MYST node `PANTHER:PTN004172926` for
  chromatin/nucleus/chromatin binding/transcription-coregulator/Pol II
  regulation, and the Fungi-level ESA1 node `PANTHER:PTN000834946` for
  `GO:0010485 histone H4 acetyltransferase activity`. The `C8VBH4` self-seed on
  `PTN000834946` is correct PAINT grounding rather than circular evidence.
- `just deep-research-falcon EMENI esa1 --fallback perplexity-lite` failed
  before producing a deep-research file because the local deep-research tooling
  could not import `agentapi` and no fallback provider key was available.
- Searched the web for newer `AN10956`/`esaA`/`H4K12` papers in A. nidulans. I
  found reviews and later secondary-metabolism papers that cite the 2012 EsaA
  study as precedent, but no newer direct primary study testing A. nidulans
  EsaA molecular function.
- Changed the broad `GO:0003682 chromatin binding` and `GO:0003712
  transcription coregulator activity` rows from `ACCEPT` to
  `KEEP_AS_NON_CORE`; they remain biologically valid, but the review already
  treats them as generic/non-core descriptors rather than core EsaA activities.
