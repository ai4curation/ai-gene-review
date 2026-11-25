# MFN1 notes

## 2026-11-22

- `just fetch-gene human MFN1` resolved the reviewed UniProtKB/Swiss-Prot protein Q8IWA4 in
  `PTHR10465:SF2` but QuickGO returned no current GOA annotations; the fetched
  `MFN1-goa.tsv` has only its header.
- UniProtKB still records MFN1 GO cross-references for GTPase activity, mitochondrial outer
  membrane, mitochondrion, membrane, GTP metabolic process, mitochondrial fusion,
  mitochondrion localization, and GTP binding, and the PTHR10465 PAINT slice lists MFN1
  (`UniProtKB:Q8IWA4`) as an IBD seed at `PTN002573358`.
- Deep research with the configured falcon provider and the requested perplexity-lite fallback
  failed because neither provider is available in this checkout. I used the UniProt bibliography,
  the existing MFN2 review, the PTHR10465 PAINT cache, and cached PMIDs 12759376, 27920125 and
  28114303 for the manual review.
- MFN1 and MFN2 share the core outer-membrane fusion mechanism. The MFN1 review does not assert
  MFN2-specific ER-mitochondria tethering, Miro/TRAK transport, or PINK1/Parkin mitophagy roles.
- A forced `just fetch-gene human MFN1 --force` on 2026-11-22 repaired the initial
  header-only GOA fetch by retrieving 47 QuickGO rows. The review now adjudicates the real
  MFN1 rows, accepts the existing IDA GTPase and mitochondrial outer-membrane annotations,
  refines `GO:0008053` mitochondrial fusion to `GO:1990626` mitochondrial outer membrane
  fusion, and retains `GO:0051646` mitochondrion localization as a broader non-core network
  organization outcome.
- The family review covers the reviewed human and worm mitofusin/Fzo representatives in
  `PTHR10465:SF1`, `PTHR10465:SF2`, and `PTHR10465:SF3`; `PTHR10465:SF4` is the
  PANTHER `DYNAMIN N-TERMINAL DOMAIN-CONTAINING PROTEIN` subfamily from
  `interpro/panther/panther.obo`, not represented by the reviewed members in this slice.
