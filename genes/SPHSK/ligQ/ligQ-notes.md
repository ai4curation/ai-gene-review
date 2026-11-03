# LigQ curation notes

## 2026-11-02 — SLG_04120 identity and native deglutathionylation

G2IKM4 is the retired SYK-6 protein at SLG_04120 (BAK65087.1, AP012222). UniSave version56 uses the submitted name gst; PMID:33244017 explicitly designates this same locus ligQ. The review therefore uses the experimentally established symbol ligQ while preserving the original raw gst record. UniParc is UPI0002276658 and the current deletion reason concerns a nonreference proteome. The deletion does not imply that the gene or function is absent.

PMID:29449375 assays the SYK-6 Nu-class protein on both GS-HPV epimers. Its native essentiality experiments concern the F199 enzyme and are not transferred to SYK-6. Native SYK-6 evidence is supplied by PMID:33244017: LigG and LigQ overlap on betaR-GS-HPV, while LigQ supplies betaS conversion. LigQ's acceptance of both epimers is not lack of preference: the latter paper measures approximately sixfold higher specific activity on betaS under its conditions. Double disruption also blocks MPHPV conversion, consistent with a requirement to recycle available glutathione through the pathway.

The chemistry removes a glutathionyl group from a carbon-sulfur bond using a second GSH and forms HPV plus GSSG. It is distinct from disulfide reduction and from the generic carbon-sulfur elimination reaction described by GO:0016846. The core uses the proposed GS-HPV glutathione-dependent deglutathionylase activity. PANTHER:PTHR44051:SF22 officially reads DISULFIDE-BOND OXIDOREDUCTASE YGHU; this shared family label is not evidence that LigQ's native reaction is YghU's physiological reaction. No new polymer-lignin process annotation is added.

## Source retrieval and review method

Normal `just fetch-gene` was run with the explicit accession. The current deleted-entry endpoint returned an empty flat file, although the command exited successfully and seeded a zero-row review. The adjacent archival transport wrapper then fetched the version-pinned UniSave flat-file block unchanged and supplied it to the repository's normal `fetch_gene_data` function. Live QuickGO returned zero annotation rows. This is an empty annotation set, not an ND assertion; no artificial NEW row is added to fill it. The source snapshot records the current DELETED response, UniParc identity, UniSave version and SHA256. Accession retirement is not gene loss or absence of biochemical evidence.

A real Falcon research request was attempted and failed with HTTP403 authentication. No provider report was fabricated. The cited primary literature and current GO definitions were manually examined instead. Detailed invocation and retrieval logs remain in the audit's ignored log directory. Supporting quotes are checked against the normal publication cache. No native localization experiment is inferred from recombinant purification.
