# ARMH3 (C10orf76) review notes

## Sources
- Affinage: trust gates clear. Checked against:
  - PMID:39580461 (full text): ARL5 effector; activates PI4KB at the TGN.
  - PMID:31829496 (abstract): HDX-MS of the c10orf76-PI4KB complex.
  - PMID:36921576 (abstract): ARMH3 recruits PI4KB for STING trafficking.
  - PMID:31519766 (abstract): GBF1 interaction; Golgi maintenance.
  - PMID:37195633 (full text): CERT uses the ARMH3-PI4KB PI4P pool.
- Partners: GBF1 (Q92538) and PI4KB (Q9UBF8).
- The cytosol IBA (PTN001006532) is seeded only by ARMH3 itself.

## Decisions
- ACCEPT: Golgi membrane and Golgi apparatus; regulation of Golgi organization (IMP).
- KEEP_AS_NON_CORE: cytosol, cytoplasm and perinuclear region (soluble pool).
- MODIFY: PI4KB binding → kinase binding (GO:0019900).
- REMOVE: GBF1 binding (policy).
- NEW:
  - Small GTPase binding (IDA, ARL5).
  - Positive regulation of cGAS/STING signaling pathway (IMP).
- No PI4K activator MF: activation is shown only in cells, with no purified-component assay.
