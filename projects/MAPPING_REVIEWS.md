---
title: "Mapping Reviews"
maturity: IN_PROGRESS
tags: [PIPELINE]
collections: [MAPPINGS]
autolink_gene_symbols: false
---
# Mapping Reviews

**Bottom line:** a large share of electronic GO annotations comes from mappings
between another vocabulary and GO: an InterPro or Pfam entry, a Rhea reaction, a
TCDB transporter class, a CAZy family, an ARO resistance term or a UniProt
keyword is mapped to a GO term, and every protein carrying the source term
inherits the GO term. One wrong mapping therefore produces many wrong
annotations. This page indexes the projects that review such mappings one source
at a time.

## What the projects share

Most of these projects record their verdicts as SSSOM mapping sets, one row per
source-term-to-GO mapping with a predicate (`exactMatch`, `broadMatch`,
`narrowMatch`) and the evidence behind the judgement:

| Source | Mapping set |
|---|---|
| InterPro | [interpro2go.sssom.yaml](INTERPRO/interpro2go.sssom.yaml) |
| NCBIfam | [ncbifam2go.sssom.yaml](NCBIFam/ncbifam2go.sssom.yaml) |
| Rhea | [rhea2go.sssom.yaml](RHEA/rhea2go.sssom.yaml) |
| TCDB | [tc2go.sssom.yaml](TCDB/tc2go.sssom.yaml) |
| CAZy | [cazy2go.sssom.yaml](GLYCOBIOLOGY/cazy2go.sssom.yaml) |
| ARO | [aro2go.sssom.yaml](ANTIMICROBIAL_RESISTANCE/aro2go.sssom.yaml) |
| RGD Pathway Ontology | [pw_go_curated.sssom.yaml](RGD_PATHWAY_ONTOLOGY/data/pw_go_curated.sssom.yaml) |

The Pfam, UniProt keyword (SPKW, KW-1110) and UniPathway projects review their
mappings in project tables and gene reviews rather than in an SSSOM file.

A mapping that is right for some members of a family and wrong for others can be
replaced by a curated annotation rule that adds the missing condition; see the
curated rules in `rules/curated/`.

## Joining this collection

A project joins by adding `MAPPINGS` to its `collections:` frontmatter list; the
table below is generated from that.
