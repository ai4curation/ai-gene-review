# LigP curation notes

## 2026-11-02 — archival identity and betaR etherase branch

E1CJ68 is the retired SYK-6 LigP entry. UniSave version63 preserves ligP, SLG_32600, the original clone BAJ11989.1 (AB571799), genome product BAK67935.1 and taxon627192. UniParc is UPI0001DD3D33; the current deletion reason is redundant sequence. The historical source remains immutable. The archived record has InterPro GST-domain classifications, including IPR053605 Lignin-Degrading_GST-like, but no PANTHER assignment; no family identifier is guessed.

The accessible abstract of primary PMID:22146726 explicitly establishes recombinant LigP enantioselectivity for betaR-MPHPV and its native overlap with LigE. Full-text details not present in the cache are not invented. Full PMID:24509858 independently assays LigP with defined guaiacyl-veratryl substrates and demonstrates inversion from a betaR substrate to a betaS glutathione adduct. Those chemical substrates are named as the paper's models; they are not silently relabeled GGE. Together the sources support the native betaR beta-etherase branch.

Current QuickGO defines GO:0004364 with a halide leaving group. LigP releases a phenolic aryloxy-derived leaving group instead. The protein's GST fold is not sufficient to assign that chemically mismatched term. Its core therefore uses the proposed glutathione-dependent beta-aryl etherase activity. This does not manufacture a GOA row or assert that LigP depolymerizes intact lignin.

## Source retrieval and review method

Normal `just fetch-gene` was run with the explicit accession. The current deleted-entry endpoint returned an empty flat file, although the command exited successfully and seeded a zero-row review. The adjacent archival transport wrapper then fetched the version-pinned UniSave flat-file block unchanged and supplied it to the repository's normal `fetch_gene_data` function. Live QuickGO returned zero annotation rows. This is an empty annotation set, not an ND assertion; no artificial NEW row is added to fill it. The source snapshot records the current DELETED response, UniParc identity, UniSave version and SHA256. Accession retirement is not gene loss or absence of biochemical evidence.

A real Falcon research request was attempted and failed with HTTP403 authentication. No provider report was fabricated. The cited primary literature and current GO definitions were manually examined instead. Detailed invocation and retrieval logs remain in the audit's ignored log directory. Supporting quotes are checked against the normal publication cache. No native localization experiment is inferred from recombinant purification.
