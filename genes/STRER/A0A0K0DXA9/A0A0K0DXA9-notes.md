# A0A0K0DXA9 notes

## 2026-11-23

- Started the Strongyloides stercoralis beta-tubulin review after a live
  UniProt query for parasite PTHR11588 members returned `A0A0K0DXA9_STRER` as
  a 444 aa beta-tubulin with the UniProt species code `STRER`, WormBaseParasite
  transcript `TCONS_00006325.p1`, and conserved Tubulin/FtsZ GTPase and
  C-terminal tubulin domains.
- `just deep-research-falcon STRER A0A0K0DXA9 --fallback perplexity-lite`
  could not produce a deep-research file because this checkout only had
  `claude_code` configured as a deep-research provider. I kept manual notes
  rather than creating a provider-named file by hand.
- `just fetch-gene-pmids STRER A0A0K0DXA9` found no PMID references in the
  seeded GOA rows, because all seven rows are electronic mappings to GO_REF
  records.
- `just paint-losses STRER A0A0K0DXA9` reported that A0A0K0DXA9 is in PANTHER
  `PTHR11588` but not as a leaf of the cached PAINT tree, and found no IRD or
  IKR loss on the gene lineage.
- The A0A0K0DXA9 GOA rows are all automated beta-tubulin rows: GTPase
  activity, GTP binding, structural constituent of cytoskeleton, microtubule,
  cytoskeleton, microtubule-based process and microtubule cytoskeleton
  organization. I accepted the core beta-tubulin structural and
  nucleotide-cycle rows, kept microtubule cytoskeleton organization as the
  specific process, and marked the broader cytoskeleton and
  microtubule-based-process rows as too general once microtubule and
  microtubule cytoskeleton organization were asserted.
- Unlike the cloned Q4KS25 Strongyloides beta-tubulin sequence, A0A0K0DXA9 has
  only a WormBaseParasite identification reference in UniProt. I therefore
  treated its relationship to the benzimidazole-engaged beta-tubulin isotype
  pool and to cloned Strongyloides BTUB/Q4KS25 as unresolved.
- After AI review, I compared the A0A0K0DXA9 and Q4KS25 UniProt sequences
  directly. A0A0K0DXA9 is 444 aa and Q4KS25 is 447 aa; over residues 1-420
  they align one-to-one with 17 substitutions at positions 32, 37, 39, 41, 42,
  43, 65, 79, 219, 222, 224, 329, 332, 348, 358, 360 and 378. After their
  shared `AEYQQYQEA` at positions 421-429, their acidic C-terminal tails
  diverge completely (`GIEDGTGEEYEADAE` in A0A0K0DXA9 versus
  `TADDYDDAEYEGEVAEEE` in Q4KS25), supporting treatment as two distinct
  S. stercoralis beta-tubulin isotypes. The candidate benzimidazole-binding
  pocket from residues 121-210 is identical, including Ser167/Phe168,
  Asp198/Glu199 and Thr200/Phe201; the literature's F167, E198 and F200
  positions therefore sit one residue later in both A0A0K0DXA9 and Q4KS25.
