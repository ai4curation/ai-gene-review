# GLDC source guide

The normal source union contains 24 paths: 20 existing sources reused byte-for-byte and four publication records acquired through the normal repository fetcher without force on 2026-11-06. All four additions are abstract-only; PMID:1634607 has a PMC identifier, but the fetcher could not obtain its full text. These records add provenance, without expanding the functional claims.

| Source | Scope |
| --- | --- |
| `interpro/panther/PTHR11773/PTHR11773-entries.csv` | Existing immutable source |
| `interpro/panther/PTHR11773/PTHR11773-metadata.yaml` | Existing immutable source |
| `interpro/panther/PTHR11773/PTHR11773-paint.tsv` | Existing immutable source |
| `publications/PMID_11286506.md` | Acquired by normal fetcher; abstract only |
| `publications/PMID_11592811.md` | Acquired by normal fetcher; abstract only |
| `publications/PMID_14702039.md` | Existing immutable source |
| `publications/PMID_15164053.md` | Existing immutable source |
| `publications/PMID_15489334.md` | Existing immutable source |
| `publications/PMID_1634607.md` | Acquired by normal fetcher; abstract only |
| `publications/PMID_18088087.md` | Existing immutable source |
| `publications/PMID_1993704.md` | Existing immutable source |
| `publications/PMID_1996985.md` | Existing immutable source |
| `publications/PMID_21269460.md` | Existing immutable source |
| `publications/PMID_2268343.md` | Existing immutable source |
| `publications/PMID_24275569.md` | Existing immutable source |
| `publications/PMID_24467211.md` | Existing immutable source |
| `publications/PMID_28244183.md` | Existing immutable source |
| `publications/PMID_28737873.md` | Acquired by normal fetcher; abstract only |
| `publications/PMID_3426593.md` | Existing immutable source |
| `publications/PMID_34800366.md` | Existing immutable source |
| `publications/PMID_7440562.md` | Existing immutable source |
| `publications/PMID_7440563.md` | Existing immutable source |
| `reactome/R-HSA-5693967.md` | Existing immutable source |
| `reactome/R-HSA-6783984.md` | Existing immutable source |

The raw GOA context list and seed order are preserved independently of review decisions. The inherited five gene objects, 25 historical annotations and 29 historical quotation associations remain reconstructable from pinned Git objects and the context archive. No prior source text is rewritten, no historical assertion is silently promoted to new evidence, and no PDB/PAINT/HPA original is presented as a generated research-provider file.

The functional bibliography is assessed in the review. Additional clinical, sequence-resource and phosphoproteome records fetched from UniProt provenance are retained as sources without implying new GLDC processes. PMID:15791207 is omitted from this union because the accessible bacterial abstract adds no necessary evidence.

Native execution used the repository fetch command after preserving the existing review. The resulting 25 annotation objects exactly matched the private forecast, including qualifiers and WITH/FROM. The original UniProt and GOA files remain byte-identical. Six IEA rows have date 20260706 in the retained GOA versus 20260727 in the separately preserved current projection; the no-force fetch did not refresh the GOA file. The six row identities and dates are recorded in `GLDC-source-evidence.json`.

Default validation, strict GOA matching, computed status, new EDIT history validation, tracked HTML rendering and changed-path whitespace checks passed. The original five objects and prior histories remain recoverable; the new history record is `history/genes/human/GLDC/2026-11-06T213550Z-codex-747f3b.yaml`. These are affected-file checks, not a claim that the full repository test suite ran.
