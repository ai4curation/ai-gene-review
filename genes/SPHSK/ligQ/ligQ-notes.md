# LigQ curation notes

## 2026-11-02 — SLG_04120 identity and native deglutathionylation

G2IKM4 is the retired SYK-6 protein at SLG_04120 (BAK65087.1, AP012222). UniSave version56 uses the submitted name gst; PMID:33244017 explicitly designates this same locus ligQ. The review therefore uses the experimentally established symbol ligQ while preserving the original raw gst record. UniParc is UPI0002276658 and the current deletion reason concerns a nonreference proteome. The deletion does not imply that the gene or function is absent.

PMID:29449375 assays the SYK-6 Nu-class protein on both GS-HPV epimers. Its native essentiality experiments concern the F199 enzyme and are not transferred to SYK-6. Native SYK-6 evidence is supplied by PMID:33244017: LigG and LigQ overlap on betaR-GS-HPV, while LigQ supplies betaS conversion. LigQ's acceptance of both epimers is not lack of preference: the latter paper measures approximately sixfold higher specific activity on betaS under its conditions. Double disruption also blocks MPHPV conversion, consistent with a requirement to recycle available glutathione through the pathway.

The chemistry removes a glutathionyl group from a carbon-sulfur bond using a second GSH and forms HPV plus GSSG. It is distinct from disulfide reduction and from the generic carbon-sulfur elimination reaction described by GO:0016846. The core uses the proposed GS-HPV glutathione-dependent deglutathionylase activity. PANTHER:PTHR44051:SF22 officially reads DISULFIDE-BOND OXIDOREDUCTASE YGHU; this shared family label is not evidence that LigQ's native reaction is YghU's physiological reaction. No new polymer-lignin process annotation is added.

## Source retrieval and review method

Normal `just fetch-gene` was run with the explicit accession. The current deleted-entry endpoint returned an empty flat file, although the command exited successfully and seeded a zero-row review. The adjacent archival transport wrapper then fetched the version-pinned UniSave flat-file block unchanged and supplied it to the repository's normal `fetch_gene_data` function. Live QuickGO returned zero annotation rows. This is an empty annotation set, not an ND assertion; no artificial NEW row is added to fill it. The source snapshot records the current DELETED response, UniParc identity, UniSave version and SHA256. Accession retirement is not gene loss or absence of biochemical evidence.

A real Falcon research request was attempted and failed with HTTP403 authentication. No provider report was fabricated. The cited primary literature and current GO definitions were manually examined instead. Detailed invocation and retrieval logs remain in the audit's ignored log directory. Supporting quotes are checked against the normal publication cache. No native localization experiment is inferred from recombinant purification.

## 2026-11-03 UTC — current UniParc cross-reference follow-up (PR #5930)

Queried the official [UniParc entry](https://rest.uniprot.org/uniparc/UPI0002276658.json), [complete database cross-references](https://rest.uniprot.org/uniparc/UPI0002276658/databases?size=500), and [current UniProtKB accession](https://rest.uniprot.org/uniprotkb/G2IKM4.json). The cross-reference endpoint returned 12 records, matching its `x-total-results` header, with no next page. Its only UniProtKB cross-reference is G2IKM4, marked `active: false`; the direct accession response independently remains DELETED. **No live UniProtKB replacement was returned for this exact sequence.** A deletion reason of redundant sequence does not itself identify a replacement accession.

The pinned archival protein is 299 residues and matches the current UniParc sequence exactly. All cross-references that supply an organism give taxon 627192 (SYK-6); none supplies a different taxon. Active RefSeq/EMBL links include RefSeq WP_014074739.1, EMBL BAK65087.1. These preserve sequence provenance but do not constitute active UniProtKB records, new functional evidence, or a reason to move the review to another strain. This exact-sequence lookup does not test all homologs or sequence variants.

Unmodified JSON responses and per-request URLs, UTC retrieval times, response headers and SHA256 hashes are retained under `genes/SPHSK/ligN/ligN-source-analysis/uniparc-2026-11-03`; `ligQ-record-evidence.yaml` records the gene-specific result. Reproduce with `query_uniparc_cross_references.py` in the shared LigN source-analysis directory and a new output directory. The reviewed archival accession, original UniProt flat file and GOA file remain unchanged.

## 2026-11-03 — shared proposed-term definition

PR5930 follow-up reconciles the shared proposed activity with the canonical definition, GO parent and chemistry-specific justification in `analysis/module_audits/bacterial_beta_aryl_ether_dimer_cleavage/canonical-proposed-terms.yaml`. Gene-specific evidence and stereoselectivity are retained. The broad parent is not substituted for the precise proposed activity; BaeAB subunits continue to contribute to the assembled complex rather than receiving standalone full activity.
