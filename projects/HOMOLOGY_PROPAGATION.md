---
title: "Propagation by Homology"
maturity: IN_PROGRESS
tags: [PIPELINE, EVALUATION]
collections: [HOMOLOGY_PROPAGATION]
autolink_gene_symbols: false
---
# Propagation by Homology

An index to the projects that review GO annotations **transferred to a gene from
other gene products**: orthology transfers (ISO), curator similarity transfers
(ISS/ISA), phylogenetic inference (IBA/PAINT), and the electronic pipelines that
do the same thing automatically (Ensembl Compara, TreeGrafter, InterPro2GO).

**[Browse all propagated annotations](../app/propagation/index.html)** — one row per
transferred GOA annotation, read as *donor(s) → intermediate → target*, with what
the donor carries today, what else the target already carries, and the gene
review's verdict. Filter by method, donor or target species, donor support,
review action, or failure mode; the URL records the selection.
[Browser guide](../docs/propagation_browser.md) ·
[Current statistics](HOMOLOGY_PROPAGATION/propagation-stats.md)

## The three parts of every transfer

Every propagated annotation has the same shape, whatever the method:

| Part | ISO / ISS / ISA | IBA (PAINT) | Ensembl Compara (IEA) |
|---|---|---|---|
| **Donor** | Gene product(s) in `WITH/FROM`, carrying an experimental annotation | Seed genes with experimental annotations, listed in `WITH/FROM` | Ortholog with an experimental annotation |
| **Intermediate** | The orthology or similarity call (Alliance, HCOP, curator) | The PANTHER ancestral node (`PTN…`) where a curator placed the function | The Compara ortholog relation (≥40% identity) |
| **Target** | The annotated gene | Every descendant of the node | The annotated gene |

A review therefore asks three separate questions, and a failure can sit in any one
of them:

1. **Is the donor annotation sound?** Does the donor still carry the term, with
   experimental support, from a paper about that gene?
2. **Is the relation the right one?** One-to-one ortholog, a paralog, one of an
   expanded family, or a node that the target should not descend from.
3. **Is this term safe to move?** Conserved activity versus tissue, lineage,
   compartment, or regulatory context that does not transfer.

The shared vocabulary for recording the answer is the
[ISO/IBA failure taxonomy](ISO.md#failure-taxonomy) (`review.propagation_review`).

## Projects

| Project | Method | Question |
|---|---|---|
| [ISO review](ISO.md) | ISO (GO_REF:0000119, 0000096, 0000121) | Which orthology transfers are sound, which are stale or transfers-of-transfers, and what ISO adds on top of IBA. |
| [IBA annotation quality](IBA_REVIEW.md) | IBA (GO_REF:0000033) | Whether the PAINT node placement fits the target: paralog subfamilies, lost sub-activities, lineage mismatches. |
| [PAINT no-IBA genes](PAINT.md) | IBA gaps | Human genes with no IBA — missing PAINT coverage or genuinely lineage-specific function. |
| [TreeGrafter](TREEGRAFTER.md) | IEA (GO_REF:0000118) | Automatic placement onto PANTHER trees and inheritance of PAINT annotations. |
| [Ortholog conjecture](ORTHOLOG_CONJECTURE.md) | Orthologs vs paralogs | Whether orthologs retain function more than paralogs in the reviewed corpus. |
| [InterPro2GO](INTERPRO.md) | IEA (GO_REF:0000002) | Family- and domain-signature transfers and where they over-reach. |
| [NCBIFam / CDD](NCBIFam.md) | Family HMMs | What NCBI family models add or mis-assign. |

## Methods covered by the browser

Method definitions follow the GO_REF descriptions in
[go-site `gorefs.yaml`](https://github.com/geneontology/go-site/blob/master/metadata/gorefs.yaml).

| Evidence · reference | Method | Donor → target |
|---|---|---|
| ISO · GO_REF:0000119 | Alliance automated transfer | human experimental → mouse ortholog |
| ISO · GO_REF:0000096 | Alliance automated transfer | mouse ↔ rat orthologs |
| ISO · GO_REF:0000121 | RGD transfer (HCOP/Alliance orthologs) | other mammals → rat |
| ISO · GO_REF:0000008 | MGI curated orthology | human or rat → mouse |
| ISS/ISA/ISO · GO_REF:0000024 | Curator judgment of similarity | any → any (mostly UniProt) |
| ISA · GO_REF:0000113 | TFClass DNA-binding-domain classification | human DbTF family |
| IBA · GO_REF:0000033 | PAINT | seed genes → PANTHER node → descendants |
| IEA · GO_REF:0000107 | Ensembl Compara | experimental → orthologs (≥40% identity) |
| IEA · GO_REF:0000118 | TreeGrafter | PAINT node → grafted sequence |
| IEA · GO_REF:0000120 | Combined IEA, rows with a Compara or PANTHER component | as above |

The browser also includes ISO/ISS/ISA rows that cite a paper instead of a GO_REF.
ISM (sequence-model predictors such as AtSubP) is not homology transfer and is not
included.

## Rebuilding

```bash
just refresh-propagation-sources   # network: donor identities (UniProt), donor GO (QuickGO), GO closure
just deploy-propagation-browser    # offline: app/propagation/
just propagation-stats             # offline: HOMOLOGY_PROPAGATION/propagation-stats.md
```

The donor cache lives in `HOMOLOGY_PROPAGATION/data/` and is committed, so the
browser and statistics rebuild offline and reproducibly; refresh it when GOA
files are re-fetched.
