# LigN curation notes

## 2026-11-02 — identity, stereochemistry and native contribution

C0SUK1 is the retired SYK-6 LigN entry, retained here as an archival identifier rather than an active UniProtKB record. UniSave version74 preserves the gene name ligN, locus SLG_35900, original cloned sequence BAH56685.1 (AB491222), genome product BAK68265.1 and taxon627192. UniParc is UPI00019B2644. Its deletion reason is redundant sequence; a deletion is not proof of functional loss. The source record's historical Sphingomonadaceae taxonomy is not silently updated.

PMID:19542348 directly isolates and expresses the SYK-6 gene and uses chiral HPLC and native disruptions. Its full text says, "LigL and LigN have the same stereospecificity". Both enzymes accept alphaS/betaR and alphaS/betaS GGE in NAD+-containing assays, retaining the beta configuration in MPHPV. The paired substrate/product wording in the abstract must not be read as assigning one beta epimer to LigL and the other to LigN. The authors conclude, "both ligL and ligN contribute to the degradation" of the alphaS pair. Their overlap is an experimentally supported native redundancy, not a sequence-only inference.

The archived sequence carries PANTHER:PTHR43391:SF26, whose official name is BLL7251 PROTEIN, and the NAD(P)-binding SDR/PF00106 classifications. These establish family membership; the unexpected PANTHER name does not replace the direct LigN assays or name a different protein. No PAINT node is inferred. The core uses the proposed substrate-defined arylglycerol-beta-aryl ether Calpha-dehydrogenase (NAD+) activity, with GO:0016616 as its broad parent. There is no new polymer-breakdown process assertion.

## Source retrieval and review method

Normal `just fetch-gene` was run with the explicit accession. The current deleted-entry endpoint returned an empty flat file, although the command exited successfully and seeded a zero-row review. The adjacent archival transport wrapper then fetched the version-pinned UniSave flat-file block unchanged and supplied it to the repository's normal `fetch_gene_data` function. Live QuickGO returned zero annotation rows. This is an empty annotation set, not an ND assertion; no artificial NEW row is added to fill it. The source snapshot records the current DELETED response, UniParc identity, UniSave version and SHA256. Accession retirement is not gene loss or absence of biochemical evidence.

A real Falcon research request was attempted and failed with HTTP403 authentication. No provider report was fabricated. The cited primary literature and current GO definitions were manually examined instead. Detailed invocation and retrieval logs remain in the audit's ignored log directory. Supporting quotes are checked against the normal publication cache. No native localization experiment is inferred from recombinant purification.
