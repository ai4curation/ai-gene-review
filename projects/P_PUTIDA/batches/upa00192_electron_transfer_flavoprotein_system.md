---
title: "PSEPK electron-transfer flavoprotein system"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [etfA, etfB, PP_4203, PP_0312, PP_0313]
autolink_gene_symbols: false
---

# PSEPK electron-transfer flavoprotein system

- Module: `electron_transfer_flavoprotein_system`
- Focused genes: two ETF alpha/beta pairs and one ETF:quinone oxidoreductase
- Satisfiability: core relay complete at PP_4201-PP_4203
- Module research: not run for this batch
- Gene-level OpenScientist research: complete for PP_4203; not run for the other
  four genes

## Boundary

This module covers the conserved ETF electron relay, not every upstream
flavin-dependent dehydrogenase that can donate electrons to it. The PP_4201-
PP_4203 locus encodes an ETF alpha/beta heterodimer and ETF:quinone
oxidoreductase, satisfying both stages of the relay. PP_0312-PP_0313 encode a
second ETF-family alpha/beta pair. Their family identity is clear, and genomic
context points to methylated-glycine oxidation as the likely donor pathway (see
below), but that pairing has not been assayed.

## Functional Parts

| Part | PSEPK realization | Assessment |
|---|---|---|
| Soluble ETF electron acceptor | EtfA Q88F97 and EtfB Q88F96 | Covered |
| ETF reoxidation and quinone reduction | PP_4203 Q88F95 | Covered |
| Alternative ETF heterodimer | PP_0312 Q88R22 and PP_0313 Q88R21 | Present; methylated-glycine oxidation the likely donor pathway, not yet assayed |

## Gene Curation

| Gene | Locus | UniProt | Review | OpenScientist |
|---|---|---|---|---|
| `etfA` | PP_4201 | Q88F97 | Curated and validated | Not run |
| `etfB` | PP_4202 | Q88F96 | Curated and validated | Not run |
| `PP_4203` | PP_4203 | Q88F95 | Curated and validated | Complete |
| `PP_0312` | PP_0312 | Q88R22 | Curated and validated | Not run |
| `PP_0313` | PP_0313 | Q88R21 | Curated and validated | Not run |

## Curation Findings

The reusable module represents bacterial and mitochondrial ETF systems without
making mitochondrial localization part of the universal definition. Its root
node is typed with the process term GO:0022900 electron transport chain; the
complex term GO:0045251 sits on the PROTEIN_COMPLEX node for the heterodimer,
where a cellular-component grounding belongs, and all four ETF-subunit reviews
now carry it as `in_complex`, as the human ETFA and ETFB reviews do. Compartment
is modelled rather than asserted in prose: each of the two parts carries a
`variant_sets` entry on a taxon axis, giving cytoplasm (GO:0005737) /
mitochondrial matrix (GO:0005759) for the soluble heterodimer and plasma
membrane (GO:0005886) / mitochondrial inner membrane (GO:0005743) for the
oxidoreductase step.

Both subunits carry `enables GO:0009055`, and the gene reviews record the
subunit-level dependency as `contributes_to_molecular_function`. Note that this
is a deliberate divergence from the completed human ETFA and ETFB reviews,
which place GO:0009055 directly in `molecular_function`: the single FAD of the
heterodimer sits at the subunit interface, so neither polypeptide carries the
activity alone. The human reviews are cited for the ACCEPT call and for the
GO:0045251 grounding, not as precedent for the `contributes_to` modelling.

For the second KT2440 ETF pair, the adjacent genes dgcA (PP_0310) and dgcB
(PP_0311) are dimethylglycine dehydrogenase subunits at EC 1.5.8.-, hence
ETF-dependent by definition, and KEGG groups all four genes in ppu00260. The
likely donor pathway is therefore methylated-glycine oxidation, which is recorded
as such and also strengthens the rejection of the family-default
GO:0033539 fatty-acid beta-oxidation term on PP_0312. The pairing has not been
assayed.

PP_4203 gains GO:0050660 (FAD binding — asserted by the UniProt record's own
RuleBase but absent from GOA) and its generic GO:0005737 cytoplasm term is
modified to GO:0005886 plasma membrane, since ETF-QO reduces a membrane quinone
and the characterized orthologs are monotopic integral membrane proteins. The
localization is inferred rather than measured, and is carried as a knowledge gap
on that annotation.

## Evidence

- [PP_4203 OpenScientist gene report](../../../genes/PSEPK/PP_4203/PP_4203-deep-research-openscientist.md)
  — the only deep research run for this batch. Two of its nine cited PMIDs were
  not used: PMID:42239388 is a 2026 bioRxiv preprint, and PMID:18625020 is
  *P. aeruginosa* rather than *P. putida*. See
  `genes/PSEPK/PP_4203/PP_4203-notes.md`.
- `modules/electron_transfer_flavoprotein_system.yaml`
- Per-gene curation notes: `genes/PSEPK/{etfA,etfB,PP_4203,PP_0312,PP_0313}/*-notes.md`
- `projects/P_PUTIDA/data/psepk_gene_list.tsv`,
  `projects/P_PUTIDA/data/psepk_pathway_buckets.tsv` — locus and KEGG-bucket
  evidence for the dgcAB donor inference.
