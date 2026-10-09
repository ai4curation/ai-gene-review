# SNURF (Q9Y675) review notes

## 2026-10-08 — MICROPROTEINS Tier 2 review (claude-code)

### Identity
- HGNC SNURF (HGNC:11171), UniProt Q9Y675 (Swiss-Prot, PE1), 71 aa, highly basic
  (~17% Arg), conserved nuclear localization motif (KRRR). Encoded by the upstream ORF of
  the bicistronic SNURF-SNRPN transcript in the Prader-Willi imprinting centre (15q11-q13);
  the downstream ORF encodes SmN (SNRPN). Separate UniProt entry and HGNC symbol, so it has
  its own folder (CLAUDE.md alt-ORF convention).
- **Symbol collision:** "SNURF" was also the original name of RNF4 (small nuclear RING
  finger protein, 194 aa) [PMID:9710597 "194 amino acid residues and comprising a consensus
  C3HC4 zinc finger (RING) structure"]. Most PubMed hits for "SNURF" are RNF4 papers
  (PMID:10617653, 10934038, 11319220, 15707587 ...). None of them concern Q9Y675.

### Evidence for the SNRPN-uORF protein
- Only primary paper: Gray et al. 1999 [PMID:10318933 "SNURF encodes a highly basic 71-aa
  protein that is nuclear-localized (as is SmN)"]; GFP fusion [PMID:10318933 "C-terminally
  tagged SNURF–GFP is indeed targeted to the nucleus when ectopically expressed"]; protein
  detected in normal but not PWS cells. Function unknown [PMID:10318933 "Additional studies
  are needed to determine whether SNURF functions as a ubiquitin-like or RNA-binding protein
  or has other biochemical functions."]. Wobble-position-biased substitution pattern argues
  for coding selection.
- HPA immunofluorescence: nuclear speckles, reliability "Supported" (proteinatlas.org JSON for
  ENSG00000273173, queried 2026-10-08).
- PubMed search (2026-10-08) for "SNRPN upstream reading frame" found no later study of the
  protein's function; later papers address the locus/imprinting centre or RNF4.

### ATPase binding (IEA, Ensembl Compara from mouse Q9WU12)
- Mouse source is MGI IPI to Snurf, WITH Rad54l2/ARIP4 (Q99NG0), PMID:12058073 (Rouleau 2002,
  ARIP4 paper; cache is abstract-only). QuickGO shows MGI also gave ARIP4 "protein binding"
  IPI WITH Q9WU12 from the same paper.
- Full text read through PMC (WebFetch, PMC117628): the paper defines "small nuclear RING
  finger protein (SNURF)" and uses a "SNURF residues 20–177" VP16 fusion as an AR-binding
  control in two-hybrid. Residues 20-177 cannot exist in a 71-aa protein, so the SNURF in the
  paper is RNF4. The MGI rows are a symbol-collision mapping error (should be Rnf4, O88846,
  if an ARIP4 interaction was shown at all). Removed here; upstream fix is at MGI.

### Decisions
- nucleus (IEA, NAS): ACCEPT. nuclear speck (IDA HPA, IBA): ACCEPT.
- ATPase binding: REMOVE (wrong gene product at source).
- No MF or BP proposed: nothing known.
