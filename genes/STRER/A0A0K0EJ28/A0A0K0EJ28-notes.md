# A0A0K0EJ28 notes

## 2026-11-23

- Started the Strongyloides stercoralis beta-tubulin review after a live
  UniProt query for parasite PTHR11588 members returned `A0A0K0EJ28_STRER` as
  a 442 aa beta-tubulin with the UniProt species code `STRER`,
  WormBaseParasite transcript `TCONS_00005409.p1`, and conserved Tubulin/FtsZ
  GTPase and C-terminal tubulin domains.
- `just deep-research-falcon STRER A0A0K0EJ28 --fallback perplexity-lite`
  could not produce a deep-research file because this checkout only had
  `claude_code` configured as a deep-research provider. I kept manual notes
  rather than creating a provider-named file by hand.
- `just fetch-gene-pmids STRER A0A0K0EJ28` found no PMID references in the
  seeded GOA rows, because all seven rows are electronic mappings to GO_REF
  records.
- `just paint-losses STRER A0A0K0EJ28` reported that A0A0K0EJ28 is in PANTHER
  `PTHR11588` but not as a leaf of the cached PAINT tree, and found no IRD or
  IKR loss on the gene lineage.
- The A0A0K0EJ28 GOA rows are all automated beta-tubulin rows: GTPase
  activity, GTP binding, structural constituent of cytoskeleton, microtubule,
  cytoskeleton, microtubule-based process and microtubule cytoskeleton
  organization. I accepted the core beta-tubulin structural and
  nucleotide-cycle rows, kept microtubule cytoskeleton organization as the
  specific process, and marked the broader cytoskeleton and
  microtubule-based-process rows as too general once microtubule and
  microtubule cytoskeleton organization were asserted.
- A simple global alignment of the three local S. stercoralis beta-tubulins
  found that A0A0K0EJ28 is distinct from the cloned BTUB/Q4KS25 and predicted
  A0A0K0DXA9 isotypes. A0A0K0EJ28 aligns to Q4KS25 over 447 columns with 375
  identities, 67 substitutions and 5 gap columns; it aligns to A0A0K0DXA9 over
  444 columns with 371 identities, 71 substitutions and 2 gap columns. The
  A0A0K0EJ28 sequence retains the canonical susceptible Phe167, Glu198 and
  Phe200 residues in its own numbering.
