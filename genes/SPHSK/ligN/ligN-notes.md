# LigN curation notes

## 2026-11-02 — identity, stereochemistry and native contribution

C0SUK1 is the retired SYK-6 LigN entry, retained here as an archival identifier rather than an active UniProtKB record. UniSave version74 preserves the gene name ligN, locus SLG_35900, original cloned sequence BAH56685.1 (AB491222), genome product BAK68265.1 and taxon627192. UniParc is UPI00019B2644. Its deletion reason is redundant sequence; a deletion is not proof of functional loss. The source record's historical Sphingomonadaceae taxonomy is not silently updated.

PMID:19542348 directly isolates and expresses the SYK-6 gene and uses chiral HPLC and native disruptions. Its full text says, "LigL and LigN have the same stereospecificity". Both enzymes accept alphaS/betaR and alphaS/betaS GGE in NAD+-containing assays, retaining the beta configuration in MPHPV. The paired substrate/product wording in the abstract must not be read as assigning one beta epimer to LigL and the other to LigN. The authors conclude, "both ligL and ligN contribute to the degradation" of the alphaS pair. Their overlap is an experimentally supported native redundancy, not a sequence-only inference.

The archived sequence carries PANTHER:PTHR43391:SF26, whose official name is BLL7251 PROTEIN, and the NAD(P)-binding SDR/PF00106 classifications. These establish family membership; the unexpected PANTHER name does not replace the direct LigN assays or name a different protein. No PAINT node is inferred. The core uses the proposed substrate-defined arylglycerol-beta-aryl ether Calpha-dehydrogenase (NAD+) activity, with GO:0016616 as its broad parent. There is no new polymer-breakdown process assertion.

## Source retrieval and review method

Normal `just fetch-gene` was run with the explicit accession. The current deleted-entry endpoint returned an empty flat file, although the command exited successfully and seeded a zero-row review. The adjacent archival transport wrapper then fetched the version-pinned UniSave flat-file block unchanged and supplied it to the repository's normal `fetch_gene_data` function. Live QuickGO returned zero annotation rows. This is an empty annotation set, not an ND assertion; no artificial NEW row is added to fill it. The source snapshot records the current DELETED response, UniParc identity, UniSave version and SHA256. Accession retirement is not gene loss or absence of biochemical evidence.

A real Falcon research request was attempted and failed with HTTP403 authentication. No provider report was fabricated. The cited primary literature and current GO definitions were manually examined instead. Detailed invocation and retrieval logs remain in the audit's ignored log directory. Supporting quotes are checked against the normal publication cache. No native localization experiment is inferred from recombinant purification.

## 2026-11-03 UTC — current UniParc cross-reference follow-up (PR #5930)

Queried the official [UniParc entry](https://rest.uniprot.org/uniparc/UPI00019B2644.json), [complete database cross-references](https://rest.uniprot.org/uniparc/UPI00019B2644/databases?size=500), and [current UniProtKB accession](https://rest.uniprot.org/uniprotkb/C0SUK1.json). The cross-reference endpoint returned 13 records, matching its `x-total-results` header, with no next page. Its only UniProtKB cross-reference is C0SUK1, marked `active: false`; the direct accession response independently remains DELETED. **No live UniProtKB replacement was returned for this exact sequence.** A deletion reason of redundant sequence does not itself identify a replacement accession.

The pinned archival protein is 311 residues and matches the current UniParc sequence exactly. All cross-references that supply an organism give taxon 627192 (SYK-6); none supplies a different taxon. Active RefSeq/EMBL links include RefSeq WP_014077904.1, EMBL BAK68265.1, EMBL BAH56685.1. These preserve sequence provenance but do not constitute active UniProtKB records, new functional evidence, or a reason to move the review to another strain. This exact-sequence lookup does not test all homologs or sequence variants.

Unmodified JSON responses and per-request URLs, UTC retrieval times, response headers and SHA256 hashes are retained under `genes/SPHSK/ligN/ligN-source-analysis/uniparc-2026-11-03`; `ligN-record-evidence.yaml` records the gene-specific result. Reproduce with `query_uniparc_cross_references.py` in the shared LigN source-analysis directory and a new output directory. The reviewed archival accession, original UniProt flat file and GOA file remain unchanged.

## 2026-11-03 — shared proposed-term definition

PR5930 follow-up reconciles the shared proposed activity with the canonical definition, GO parent and chemistry-specific justification in `analysis/module_audits/bacterial_beta_aryl_ether_dimer_cleavage/canonical-proposed-terms.yaml`. Gene-specific evidence and stereoselectivity are retained. The broad parent is not substituted for the precise proposed activity; BaeAB subunits continue to contribute to the assembled complex rather than receiving standalone full activity.
