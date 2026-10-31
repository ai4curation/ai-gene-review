# Term-by-term ontology review for PR #5616

Verified 2026-10-30T01:41:26.802620+00:00 against the normal QuickGO response and [GO source commit 939abfae5a06](https://raw.githubusercontent.com/geneontology/go-ontology/939abfae5a06a9dbb20d931465707e5e61a7c537/src/ontology/go-edit.obo). The queried IDs, request URL and input checksum are in `go-snapshot-provenance.json`. `go-obsolescence.obo` contains complete unedited source stanzas. QuickGO omits some OBO migration tags; the pinned OBO supplies `replaced_by` and `consider` below.

The original snapshot omitted these terms. The refresh script updates only their stale label, ontology-metadata and BP-enum cache entries, preserving unrelated rows. Fetched GOA IDs and labels remain unchanged.

| Term | QuickGO obsolete | GO migration metadata |
|---|---|---|
| GO:0006419: obsolete alanyl-tRNA aminoacylation | true | replaced_by: GO:0006418 |
| GO:0006420: obsolete arginyl-tRNA aminoacylation | true | replaced_by: GO:0006418 |
| GO:0006421: obsolete asparaginyl-tRNA aminoacylation | true | replaced_by: GO:0006418 |
| GO:0006422: obsolete aspartyl-tRNA aminoacylation | true | replaced_by: GO:0006418 |
| GO:0006423: obsolete cysteinyl-tRNA aminoacylation | true | replaced_by: GO:0006418 |
| GO:0006424: obsolete glutamyl-tRNA aminoacylation | true | replaced_by: GO:0006418 |
| GO:0006425: obsolete glutaminyl-tRNA aminoacylation | true | replaced_by: GO:0006418 |
| GO:0006426: obsolete glycyl-tRNA aminoacylation | true | replaced_by: GO:0006418 |
| GO:0006427: obsolete histidyl-tRNA aminoacylation | true | replaced_by: GO:0006418 |
| GO:0006428: obsolete isoleucyl-tRNA aminoacylation | true | replaced_by: GO:0006418 |
| GO:0006429: obsolete leucyl-tRNA aminoacylation | true | replaced_by: GO:0006418 |
| GO:0006430: obsolete lysyl-tRNA aminoacylation | true | replaced_by: GO:0006418 |
| GO:0006431: obsolete methionyl-tRNA aminoacylation | true | replaced_by: GO:0006418 |
| GO:0006432: obsolete phenylalanyl-tRNA aminoacylation | true | replaced_by: GO:0006418 |
| GO:0006433: obsolete prolyl-tRNA aminoacylation | true | replaced_by: GO:0006418 |
| GO:0006434: obsolete seryl-tRNA aminoacylation | true | replaced_by: GO:0006418 |
| GO:0006435: obsolete threonyl-tRNA aminoacylation | true | replaced_by: GO:0006418 |
| GO:0006436: obsolete tryptophanyl-tRNA aminoacylation | true | replaced_by: GO:0006418 |
| GO:0006437: obsolete tyrosyl-tRNA aminoacylation | true | replaced_by: GO:0006418 |
| GO:0006438: obsolete valyl-tRNA aminoacylation | true | replaced_by: GO:0006418 |
| GO:0070680: obsolete asparaginyl-tRNAAsn biosynthesis via transamidation | true | replaced_by: GO:0070981 |
| GO:0070681: obsolete glutaminyl-tRNAGln biosynthesis via transamidation | true | consider: GO:0043039; consider: GO:0050567 |

## Curated interpretation

The twenty substrate-specific charging BPs explicitly map to GO:0006418. All 45 affected direct-charging rows follow that process mapping; substrate specificity remains in the biologically supported molecular functions. Two existing GO:0006424 rows on PSEPK/glnS and PSEAE/glnS have a separate historical wrong-substrate issue: their existing reasons already explain glutamine rather than glutamate charging. Their retained MF is GO:0004819, not GO:0004818; the obsolete source label does not justify transferring the wrong chemistry. PSEPK/glyS also has a historical arginyl-tRNA process row; its existing reason explicitly corrects the substrate to glycine. These preserved exceptions show why term migration does not substitute for gene-specific biochemical review.

GO:0070681 has no automatic replacement. Its consider entries are advice. GatCAB acts on an already esterified tRNA, so all 11 GatCAB rows retain GO:0019988 after mechanistic review. Native versus supplied-substrate Gln/Asn distinctions and molecular-function contributions remain explicit.

GO:0070680 maps to GO:0070981 in the pinned source but occurs in none of this panel's existing rows. Its discussion does not manufacture a new annotation or apply that mapping to GatCAB.

## All affected existing rows

Row numbers are one-based positions in existing_annotations; repeated terms retain distinct evidence rows.

| Review | Row | Original term | Retained action/replacement |
|---|---|---|
| genes/ECOLI/asnS/asnS-ai-review.yaml | 13 | GO:0006421 | MODIFY → GO:0006418 |
| genes/ECOLI/asnS/asnS-ai-review.yaml | 14 | GO:0006421 | MODIFY → GO:0006418 |
| genes/ECOLI/asnS/asnS-ai-review.yaml | 15 | GO:0006421 | MODIFY → GO:0006418 |
| genes/ECOLI/asnS/asnS-ai-review.yaml | 16 | GO:0006421 | MODIFY → GO:0006418 |
| genes/ECOLI/asnS/asnS-ai-review.yaml | 17 | GO:0006421 | MODIFY → GO:0006418 |
| genes/PSEPK/alaS/alaS-ai-review.yaml | 9 | GO:0006419 | MODIFY → GO:0006418 |
| genes/PSEPK/argS/argS-ai-review.yaml | 7 | GO:0006420 | MODIFY → GO:0006418 |
| genes/PSEPK/aspS/aspS-ai-review.yaml | 8 | GO:0006422 | MODIFY → GO:0006418 |
| genes/PSEPK/cysS/cysS-ai-review.yaml | 8 | GO:0006423 | MODIFY → GO:0006418 |
| genes/PSEPK/gatA/gatA-ai-review.yaml | 7 | GO:0070681 | MODIFY → GO:0019988 |
| genes/PSEPK/gatB/gatB-ai-review.yaml | 8 | GO:0070681 | MODIFY → GO:0019988 |
| genes/PSEPK/gatC/gatC-ai-review.yaml | 3 | GO:0070681 | MODIFY → GO:0019988 |
| genes/PSEPK/glnS/glnS-ai-review.yaml | 9 | GO:0006424 | MODIFY → GO:0006418 |
| genes/PSEPK/glnS/glnS-ai-review.yaml | 10 | GO:0006425 | MODIFY → GO:0006418 |
| genes/PSEPK/gltX/gltX-ai-review.yaml | 9 | GO:0006424 | MODIFY → GO:0006418 |
| genes/PSEPK/glyQ/glyQ-ai-review.yaml | 6 | GO:0006426 | MODIFY → GO:0006418 |
| genes/PSEPK/glyS/glyS-ai-review.yaml | 7 | GO:0006420 | MODIFY → GO:0006418 |
| genes/PSEPK/glyS/glyS-ai-review.yaml | 8 | GO:0006426 | MODIFY → GO:0006418 |
| genes/PSEPK/hisS/hisS-ai-review.yaml | 4 | GO:0006427 | MODIFY → GO:0006418 |
| genes/PSEPK/ileS/ileS-ai-review.yaml | 10 | GO:0006428 | MODIFY → GO:0006418 |
| genes/PSEPK/leuS/leuS-ai-review.yaml | 9 | GO:0006429 | MODIFY → GO:0006418 |
| genes/PSEPK/lysS/lysS-ai-review.yaml | 11 | GO:0006430 | MODIFY → GO:0006418 |
| genes/PSEPK/metG/metG-ai-review.yaml | 9 | GO:0006431 | MODIFY → GO:0006418 |
| genes/PSEPK/pheS/pheS-ai-review.yaml | 8 | GO:0006432 | MODIFY → GO:0006418 |
| genes/PSEPK/pheT/pheT-ai-review.yaml | 7 | GO:0006432 | MODIFY → GO:0006418 |
| genes/PSEPK/proS/proS-ai-review.yaml | 9 | GO:0006433 | MODIFY → GO:0006418 |
| genes/PSEPK/serS/serS-ai-review.yaml | 7 | GO:0006434 | MODIFY → GO:0006418 |
| genes/PSEPK/thrS/thrS-ai-review.yaml | 8 | GO:0006435 | MODIFY → GO:0006418 |
| genes/PSEPK/trpS/trpS-ai-review.yaml | 8 | GO:0006436 | MODIFY → GO:0006418 |
| genes/PSEPK/tyrS/tyrS-ai-review.yaml | 9 | GO:0006437 | MODIFY → GO:0006418 |
| genes/PSEPK/valS/valS-ai-review.yaml | 9 | GO:0006438 | MODIFY → GO:0006418 |
| genes/THEVB/gltX/gltX-ai-review.yaml | 9 | GO:0006424 | MODIFY → GO:0006418 |
| genes/BACSU/asnS/asnS-ai-review.yaml | 8 | GO:0006421 | MODIFY → GO:0006418 |
| genes/BACSU/asnS/asnS-ai-review.yaml | 9 | GO:0006421 | MODIFY → GO:0006418 |
| genes/BACSU/aspS/aspS-ai-review.yaml | 9 | GO:0006422 | MODIFY → GO:0006418 |
| genes/BACSU/aspS/aspS-ai-review.yaml | 10 | GO:0006422 | MODIFY → GO:0006418 |
| genes/BACSU/gatA/gatA-ai-review.yaml | 8 | GO:0070681 | MODIFY → GO:0019988 |
| genes/BACSU/gatB/gatB-ai-review.yaml | 9 | GO:0070681 | MODIFY → GO:0019988 |
| genes/BACSU/gatB/gatB-ai-review.yaml | 10 | GO:0070681 | MODIFY → GO:0019988 |
| genes/BACSU/gatC/gatC-ai-review.yaml | 3 | GO:0070681 | MODIFY → GO:0019988 |
| genes/BACSU/gltX/gltX-ai-review.yaml | 10 | GO:0006424 | MODIFY → GO:0006418 |
| genes/BACSU/gltX/gltX-ai-review.yaml | 11 | GO:0006424 | MODIFY → GO:0006418 |
| genes/BORBU/lysS/lysS-ai-review.yaml | 9 | GO:0006430 | MODIFY → GO:0006418 |
| genes/PSEAE/aspS/aspS-ai-review.yaml | 9 | GO:0006422 | MODIFY → GO:0006418 |
| genes/PSEAE/aspS/aspS-ai-review.yaml | 10 | GO:0006422 | MODIFY → GO:0006418 |
| genes/PSEAE/gatA/gatA-ai-review.yaml | 7 | GO:0070681 | MODIFY → GO:0019988 |
| genes/PSEAE/gatB/gatB-ai-review.yaml | 9 | GO:0070681 | MODIFY → GO:0019988 |
| genes/PSEAE/gatB/gatB-ai-review.yaml | 10 | GO:0070681 | MODIFY → GO:0019988 |
| genes/PSEAE/gatC/gatC-ai-review.yaml | 3 | GO:0070681 | MODIFY → GO:0019988 |
| genes/PSEAE/glnS/glnS-ai-review.yaml | 10 | GO:0006424 | MODIFY → GO:0006418 |
| genes/PSEAE/glnS/glnS-ai-review.yaml | 11 | GO:0006425 | MODIFY → GO:0006418 |
| genes/PSEAE/glnS/glnS-ai-review.yaml | 12 | GO:0006425 | MODIFY → GO:0006418 |
| genes/PSEAE/gltX/gltX-ai-review.yaml | 10 | GO:0006424 | MODIFY → GO:0006418 |
| genes/PSEAE/gltX/gltX-ai-review.yaml | 11 | GO:0006424 | MODIFY → GO:0006418 |
| genes/THET8/glyQS/glyQS-ai-review.yaml | 11 | GO:0006426 | MODIFY → GO:0006418 |
| genes/THET8/glyQS/glyQS-ai-review.yaml | 12 | GO:0006426 | MODIFY → GO:0006418 |

## Repository-wide dependent migrations

Pruning the stale BP enum exposed four out-of-panel core processes. AARS1 and Populus ALARS now use GO:0006418 while retaining alanine specificity in GO:0004813; their obsolete-term reviews and authored replacement suggestions are reconciled. Populus GATC now uses GO:0019988 while retaining its supported organellar Gln-forming complex contribution. The generic GO enum is pruned alongside the BP enum.

The METTP GatC review required biological correction as well as migration. A0B5K3 is Methanothrix thermoacetophila PT; its old manual report had applied Methanothermobacter thermautotrophicus findings. The corrected review uses target HAMAP family/complex evidence and explicitly comparative archaeal pathway evidence. It retains eight original annotation payloads and archives two unsupported inherited NEW proposals. The core records a GatCAB Asn-forming contribution with GO:0019988, while target Gln-forming capacity and a separate regulatory role remain undecided. These four dependencies are not added to the 42-member bacterial module panel.

## Upstream issue provenance

The GO:0070681 source stanza's reference to issue15375 is supported by the issue discussion, despite its broader title. The [2026-09-02 closure summary](https://github.com/geneontology/go-ontology/issues/15375#issuecomment-5505778750) explicitly discusses GO:0070681, its consider-only migration, and the related pathway-variant work in issue31932. The source stanza is preserved exactly; the issue title alone is not evidence of a wrong reference.
