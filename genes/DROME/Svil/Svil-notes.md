# Svil (DROME) review notes

## Session 1

- `just fetch-gene DROME Svil` failed repeatedly (UniProt stream search timed out on
  the gene-name query). Fetched by accession instead:
  `just fetch-gene DROME M9MRN1 --alias Svil`. The record is M9MRN1, gene Svil,
  FlyBase FBgn0266696, GeneID 38306, so it is the requested entry.
- GOA for M9MRN1 contains only two ND rows (GO:0005575, GO:0008150; FlyBase, 2006).
  Gene-level FlyBase annotations on other Svil accessions (X2JAM4, Q0E8J1, Q7KV92,
  Q9W016; QuickGO, checked this session) are also only ND plus IEA/IBA actin-binding
  terms carried by domain-bearing isoforms. FlyBase has no experimental GO for Svil.
- Bioinformatics (Svil-bioinformatics/RESULTS.md): M9MRN1 lacks the gelsolin and
  headpiece regions; residues 1-1292 are shared with isoform AE, the remainder is
  isoform-specific and ends in a predicted TM helix. So actin binding should not be
  added NEW to this accession.
- PMID:22530061 read in full. BG02427 gene assignment is ambiguous (CG42669 = Svil vs
  CG42699), phenotype not confirmed by excision. Not sufficient for a process term.
  Note: the paper also says "the line that trapped cpo, BG02427, is homozygous
  lethal", which contradicts its own Table 2 (cpo is BG02810) and the behaviour data
  for BG02427; probably a typo.
- PMID:36067835 abstract only: Supervillin co-purifies with Mib2 and affects border
  cell migration. Phenotype-level; does not meet the NEW bar on its own.
- Decision: keep both ND rows (ACCEPT). No NEW annotations. Raise the TM/tail-anchor
  question and the Mib2/border-cell question as suggested questions/experiments.

## 2026-10-28 review fixes

Added Svil-bioinformatics/pyproject.toml declaring biopython for compare_isoforms.py (stdlib urllib used, no requests). Status set from update-status.
