# A0AAF5DAP5 notes

## 2026-11-23

- Started the Strongyloides stercoralis beta-tubulin review after a live
  UniProt query for parasite PTHR11588 members returned `A0AAF5DAP5_STRER` as
  a 450 aa beta-tubulin with the UniProt species code `STRER`,
  WormBaseParasite transcript `TCONS_00009497.p1`, and conserved Tubulin/FtsZ
  GTPase and C-terminal tubulin domains.
- `just deep-research-falcon STRER A0AAF5DAP5 --fallback perplexity-lite`
  could not produce a deep-research file because this checkout only had
  `claude_code` configured as a deep-research provider. I kept manual notes
  rather than creating a provider-named file by hand.
- `just fetch-gene-pmids STRER A0AAF5DAP5` found no PMID references in the
  seeded GOA rows, because all seven rows are electronic mappings to GO_REF
  records.
- `just paint-losses STRER A0AAF5DAP5` reported that A0AAF5DAP5 is in PANTHER
  `PTHR11588` but not as a leaf of the cached PAINT tree, and found no IRD or
  IKR loss on the gene lineage.
- The A0AAF5DAP5 GOA rows are all automated beta-tubulin rows: GTPase
  activity, GTP binding, structural constituent of cytoskeleton, microtubule,
  cytoskeleton, microtubule-based process and microtubule cytoskeleton
  organization. I accepted the core beta-tubulin structural and
  nucleotide-cycle rows, kept microtubule cytoskeleton organization as the
  specific process, and marked the broader cytoskeleton and
  microtubule-based-process rows as too general once microtubule and
  microtubule cytoskeleton organization were asserted.
- Unlike the cloned Q4KS25 Strongyloides beta-tubulin sequence, A0AAF5DAP5 has
  only a WormBaseParasite identification reference in UniProt. I therefore
  treated its relationship to the benzimidazole-engaged beta-tubulin isotype
  pool and to cloned Strongyloides BTUB/Q4KS25 as unresolved.
- A reproducible global alignment of the four local S. stercoralis
  beta-tubulins found that A0AAF5DAP5 is a distinct WBParaSite model whose
  `LFNII` residues before the conserved `MREIV` start are likely a wrong-start
  extension rather than a biological N-terminal extension. The Q4KS25 versus
  A0AAF5DAP5 alignment spans 453 columns with 420 identities, 24 substitutions
  and 9 gap columns. The literature codon names F167, E198 and F200 correspond
  to Q4KS25 residues F168, E199 and F201 and then to A0AAF5DAP5 residues F173,
  E204 and F206.
