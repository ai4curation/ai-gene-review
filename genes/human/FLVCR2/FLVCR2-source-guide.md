# FLVCR2 source guide

The genuine repository fetch produced30 annotations and two natural products. Eight exact-main normal sources were hydrated before fetch and preserved; three qualified missing publications were fetched normally. Shared PMID:15369674 reuses the independently accepted FLVCR1 actual merge. [Evidence synthesis](FLVCR2-source-evidence.md) and [notes](FLVCR2-notes.md) provide the biological scope and chronological record.

## Identity and accepted scope

Human FLVCR2 is UniProt Q9UPI3 / HGNC:20105. The official identity set includes C14orf58, CCT, FLJ20371, MFSD7C and SLC49A2. Preserve the official products Q9UPI3-1 (526 residues) and Q9UPI3-2 (321 residues). The latter has VSP_043048 replacing native residues 1–18 and VSP_043049 deleting 19–223. Existing exact FASTA reconstruction establishes identity only; it does not assign the full-length transport functions, heme-binding fragment results or a membrane location to the short product.

The review preserves 30 original contexts: 16 ACCEPT, 10 KEEP_AS_NON_CORE, 3 TOO_GENERAL and 1 REMOVE. The genuine seed contains30 rows, with a bijection to all30 accepted original contexts and no collapse. No NEW annotation or publication quotation is proposed. The review has18 references: seven GO references, eight publications and three authored evidence/notes files. Computed status is recorded after validation in the notes.

Two core proposals are retained: GO:0015220 choline transmembrane transporter activity with GO:0015871 choline transport, and GO:0034228 ethanolamine transmembrane transporter activity with GO:0034229 ethanolamine transport. Both use GO:0005886 plasma membrane. Human cell/yeast transport and human structural evidence are kept separate from mouse BBB physiology and from separately scoped purified mouse assays. The source-evidence draft records the assay and direction limits.

## Original extension and deterministic projection

Raw1, `UniProtKB:Q9UPI3!447598895`, is the PMID:38302740 IDA choline-transporter context. It contains the only nonempty original extension: `occurs_in GO:0005886`. The retained official predicate mapping is BFO:0000066. Serialize the singleton through `ExistingAnnotation.extensions` as:

```yaml
extensions:
- predicate: BFO:0000066
  term:
    id: GO:0005886
    label: plasma membrane
```

The original expression has one disjunct containing one conjunct, so this singleton preserves its meaning without flattening an OR expression. The other 29 original contexts have no extension. The genuine seeded match is stored row6 (zero-based), joined by term, evidence, original reference and supporting entities to the original QuickGO ID. The original extension was restored to that row without changing its machine fields or review action. The private TSV annotation-extension column did not represent this structured expression and must not substitute for the original QuickGO object. Future multi-group expressions would require separate treatment.

The compact table below identifies all30 original source contexts and review actions. The committed GOA and review retain imported identifiers, evidence, supporting entities and qualifiers; the original extension is restored as described above. Complete raw-source and projection records are retained as private audit provenance, not public evidence links.

Raw indices are zero-based. `NC` means KEEP_AS_NON_CORE; `TG` means TOO_GENERAL.

| Raw | Original QuickGO ID | GO term | Evidence / original reference | Accepted action |
| --- | --- | --- | --- | --- |
| 0 | `UniProtKB:Q9UPI3!447598894` | GO:0015220 choline transmembrane transporter activity | IEA / GO_REF:0000120 | ACCEPT |
| 1 | `UniProtKB:Q9UPI3!447598895` | GO:0015220 choline transmembrane transporter activity | IDA / PMID:38302740 | ACCEPT |
| 2 | `UniProtKB:Q9UPI3!447598896` | GO:0015220 choline transmembrane transporter activity | IDA / PMID:38778100 | ACCEPT |
| 3 | `UniProtKB:Q9UPI3!447598897` | GO:0015220 choline transmembrane transporter activity | IDA / PMID:40972734 | ACCEPT |
| 4 | `UniProtKB:Q9UPI3!447598898` | GO:0015232 heme transmembrane transporter activity | IBA / GO_REF:0000033 | NC |
| 5 | `UniProtKB:Q9UPI3!447598899` | GO:0015232 heme transmembrane transporter activity | IDA / PMID:20823265 | NC |
| 6 | `UniProtKB:Q9UPI3!447598900` | GO:0020037 heme binding | IBA / GO_REF:0000033 | NC |
| 7 | `UniProtKB:Q9UPI3!447598901` | GO:0020037 heme binding | IDA / PMID:20823265 | NC |
| 8 | `UniProtKB:Q9UPI3!447598902` | GO:0020037 heme binding | IDA / PMID:32973183 | NC |
| 9 | `UniProtKB:Q9UPI3!447598903` | GO:0022857 transmembrane transporter activity | IEA / GO_REF:0000002 | TG |
| 10 | `UniProtKB:Q9UPI3!447598904` | GO:0033265 choline binding | IEA / GO_REF:0000107 | NC |
| 11 | `UniProtKB:Q9UPI3!447598905` | GO:0034228 ethanolamine transmembrane transporter activity | IDA / PMID:38778100 | ACCEPT |
| 12 | `UniProtKB:Q9UPI3!447598906` | GO:0015871 choline transport | IEA / GO_REF:0000107 | ACCEPT |
| 13 | `UniProtKB:Q9UPI3!447598907` | GO:0015871 choline transport | IDA / PMID:38302740 | ACCEPT |
| 14 | `UniProtKB:Q9UPI3!447598908` | GO:0015871 choline transport | IDA / PMID:38778100 | ACCEPT |
| 15 | `UniProtKB:Q9UPI3!447598909` | GO:0015871 choline transport | IDA / PMID:40972734 | ACCEPT |
| 16 | `UniProtKB:Q9UPI3!447598910` | GO:0034229 ethanolamine transport | IEA / GO_REF:0000108 | ACCEPT |
| 17 | `UniProtKB:Q9UPI3!447598911` | GO:0055085 transmembrane transport | IEA / GO_REF:0000002 | TG |
| 18 | `UniProtKB:Q9UPI3!447598912` | GO:0097037 heme export | IBA / GO_REF:0000033 | REMOVE |
| 19 | `UniProtKB:Q9UPI3!447598913` | GO:0150104 transport across blood-brain barrier | ISS / GO_REF:0000024 | ACCEPT |
| 20 | `UniProtKB:Q9UPI3!447598914` | GO:0150104 transport across blood-brain barrier | IEA / GO_REF:0000107 | ACCEPT |
| 21 | `UniProtKB:Q9UPI3!447598915` | GO:0005886 plasma membrane | IDA / PMID:38302740 | ACCEPT |
| 22 | `UniProtKB:Q9UPI3!447598916` | GO:0005886 plasma membrane | IDA / PMID:38778100 | ACCEPT |
| 23 | `UniProtKB:Q9UPI3!447598917` | GO:0016020 membrane | IBA / GO_REF:0000033 | TG |
| 24 | `UniProtKB:Q9UPI3!447598918` | GO:0005789 endoplasmic reticulum membrane | IEA / GO_REF:0000044 | NC |
| 25 | `UniProtKB:Q9UPI3!447598919` | GO:0005789 endoplasmic reticulum membrane | IDA / PMID:32973183 | NC |
| 26 | `UniProtKB:Q9UPI3!447598920` | GO:0005886 plasma membrane | IEA / GO_REF:0000120 | ACCEPT |
| 27 | `UniProtKB:Q9UPI3!447598921` | GO:0005886 plasma membrane | EXP / PMID:14729055 | ACCEPT |
| 28 | `UniProtKB:Q9UPI3!447598922` | GO:0031966 mitochondrial membrane | IEA / GO_REF:0000044 | NC |
| 29 | `UniProtKB:Q9UPI3!447598923` | GO:0031966 mitochondrial membrane | IDA / PMID:32973183 | NC |

## Source access and immutable normal dependencies

All11 normal dependencies are present: eight publications and three PTHR10924 files. Eight reuse exact main2251f5c29ecb4479005a4e21f55d1c6e81dc7080 bytes; PMID:14729055, PMID:32973183 and PMID:38693257 were genuinely fetched after ownership qualification. All normal caches are immutable after acquisition, including the shared PMID:15369674 source.

| Normal publication | Consulted access and limitation |
| --- | --- |
| PMID_14729055.md | Authentic metadata/abstract; exact old localization assay remains UNVERIFIED. |
| PMID_15369674.md | Retained original publisher PDF; selected target/paralog heme-washout result and caption support raw18 with the identity link from PMID:20823265. |
| PMID_20823265.md | Original Methods/Results; distinguish human protein, CHO and oocyte hosts, human knockdown and lysate binding. |
| PMID_32973183.md | Original main body and selected supplementary Figure 10/caption; human NTD and THP-1 observations remain distinct from mouse constructs/tissues. |
| PMID_38302740.md | Selected original Results/Methods; human cell/yeast transport and separate mouse BBB experiments. |
| PMID_38693257.md | Selected original Results/Methods/Discussion read after genuine normal fetch recovered full text; mouse purified/HEK293-construct experiments remain distinct from human iHBEC and brain staining. No pixels or supplemental-source-data replay. |
| PMID_38778100.md | Selected original Results/Methods; human FLVCR2 choline structure/transport and ethanolamine uptake; no FLVCR1 structure/washout transfer. |
| PMID_40972734.md | Authentic metadata/abstract; exact FLVCR2 assay remains UNVERIFIED despite independent term support. |

Retain `interpro/panther/PTHR10924/PTHR10924-entries.csv`, `PTHR10924-metadata.yaml` and `PTHR10924-paint.tsv`. The accepted replay maps four incoming IBAs to original IBDs and matches all eight normal slice rows. Neither a target-derived seed nor a short donor list is a reason to reject an IBA. The export removal rests on the target-specific comparative primary evidence; the other heme IBAs remain non-core.

## Source-byte and access record

| Normal path | Bytes | SHA256 | Full text in normal cache |
| --- | --- | --- | --- |
| `interpro/panther/PTHR10924/PTHR10924-entries.csv` | 3489 | `8b94e935c03f439529c18ca060799a4bdc0eb489f8c80424cf04fdc12d0fe342` | not applicable |
| `interpro/panther/PTHR10924/PTHR10924-metadata.yaml` | 954 | `6dd9f6ec7363c0ab878aa4050b9183f0d977bb85651701653053701d36a6130c` | not applicable |
| `interpro/panther/PTHR10924/PTHR10924-paint.tsv` | 934 | `16d069553243a627ce7e4a1522ee3e7a90afe20da6bf12da30f9ccb222b92f78` | not applicable |
| `publications/PMID_14729055.md` | 2802 | `42ebcbb9c8be48d8bc8ebd210ab971dd85c034a8d1df9c43973d842e19d49c78` | False |
| `publications/PMID_15369674.md` | 2139 | `f6c97b07acd5fb97c9ed1c2b8a93943fbef585c687e4100273bc2f3761fbe165` | False |
| `publications/PMID_20823265.md` | 29620 | `e99d103b8eb0be3da587cb65c1b68c2f764091f28995544f6668ad8b604bf685` | True |
| `publications/PMID_32973183.md` | 223929 | `ad3605f4f51e70fa29d1bd40d7d98e90436a1d8ea674347d4895c79aa7125c7d` | True |
| `publications/PMID_38302740.md` | 184318 | `4064686d1bb03143b5948d4767708fb54a416b31adb843a1b16c6a841c533a47` | True |
| `publications/PMID_38693257.md` | 190239 | `2d03eeef1e1b664bc681e000cfddc40088bf1aa43cd28a24a0c65084e3446b7d` | True |
| `publications/PMID_38778100.md` | 145945 | `99b5a14b48d2e4226d214b2f8de5ff01b0250ee4d918b67b170aa299a70f1e30` | True |
| `publications/PMID_40972734.md` | 3454 | `aed5099079cd893498447e206987f18c3842e357acb4a330d5c38ce982643238` | False |

External selected-primary access and normal-cache availability are distinct. The evidence synthesis records source-specific assay and access limits; no provider-generated research report or new publication quotations were manufactured. Known provider authentication/quota failures were not retried. The [published campaign instructions](https://github.com/ai4curation/ai-gene-review/blob/2251f5c29ecb4479005a4e21f55d1c6e81dc7080/projects/CLINGEN_MENDELIAN.md#curation-instructions) require reference-only support, taking precedence over conflicting local skill requests for quotations. Default validators are unchanged.
