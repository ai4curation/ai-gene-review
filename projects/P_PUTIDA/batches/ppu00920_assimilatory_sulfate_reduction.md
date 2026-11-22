---
title: "PSEPK ppu00920 APS-dependent assimilatory sulfate reduction batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [cysD, cysNC, cysH, cysI, fpr-I, PP_0860]
autolink_gene_symbols: false
---

# PSEPK ppu00920: APS-dependent assimilatory sulfate reduction

- Module: `aps_dependent_assimilatory_sulfate_reduction`
- Pathway context: KEGG `ppu00920` (sulfur metabolism)
- Initial curation pull request: [#2254](https://github.com/ai4curation/ai-gene-review/pull/2254)
- Focused genes: 6
- Broad membership-table candidates: 54

## Boundary

This batch covers the direct APS-dependent sulfate-to-sulfide route:

1. `cysD` + `cysNC`: sulfate + ATP to APS, coupled to CysNC GTP turnover
2. `cysH`: APS to sulfite using thioredoxin
3. `cysI` with `fpr-I`: sulfite to sulfide through the Pseudomonad
   ferredoxin/Fpr electron-transfer architecture

Sulfate uptake is upstream. Siroheme synthesis supports CysI but is a separate
cofactor-biosynthesis module. CysK/CysM incorporation of sulfide into cysteine
is downstream.

`PP_0860` is included as an organism-specific ambiguity rather than a core
member. Its unreviewed product name suggests a sulfite-reductase flavoprotein,
but it lacks an exact reaction and has an atypical membrane/PANTHER
architecture. Pseudomonas genetics instead support an FprA-fed CysI system.

The C-terminal APS-kinase-like domain in CysNC is tracked as an open question.
It is not used to add a PAPS intermediate because the exact record assigns only
the CysN ATP-sulfurylase role and KT2440 CysH is an APS reductase.

## Status

- [x] Fetch the focused PSEPK genes from UniProt and GOA.
- [x] Curate all six first-pass gene reviews.
- [x] Create and semantically validate the species-neutral multi-part module.
- [x] Attempt OpenScientist gene-level research; `cysH`, `cysI`, and `PP_0860`
  returned reports, while the corrected `cysD`, `cysNC`, and `fpr-I` requests
  each exhausted the 7,200-second provider timeout without a report.
- [x] Complete fresh generic module OpenScientist research with a requested
  7,200-second research timeout and retain its generated artifacts.
- [x] Complete module + `ppu00920` + PSEPK OpenScientist research.
- [x] Resolve the CysNC APS-kinase-domain and PP_0860 questions after research.
- [x] Integrate useful research findings without treating provider output as authority.
- [x] Validate and render the module, gene reviews, and batch page.
- [x] Merge initial module PR #2254 after automated review and CI.

## Focused Genes

| Gene | Locus | UniProt | Module role | First-pass result |
|---|---|---|---|---|
| `cysD` | PP_1303 | Q88NA9 | ATP sulfurylase catalytic subunit | Exact sulfate adenylyltransferase MF and sulfate-assimilation process accepted |
| `cysNC` | PP_1304 | Q88NA8 | ATP sulfurylase regulatory GTPase | GTPase activity accepted; imported ATP-sulfurylase relation corrected to contributes_to |
| `cysH` | PP_2328 | Q88KG2 | APS reductase | APS-reductase MF accepted; conflicting PAPS-reductase annotation removed |
| `cysI` | PP_2371 | Q88KB9 | sulfite-reductase hemoprotein | Ferredoxin-dependent activity inferred from PTHR32439/Sir orthology and pathway context |
| `fpr-I` | PP_1638 | Q88MD5 | FprA-type electron supply | Exact FNR MF accepted; DSM 3601 sulfate role transferred to KT2440 by orthology |
| `PP_0860` | PP_0860 | Q88PJ0 | questionable CysJ-like candidate | FMN binding retained as non-core; exact redox role undecided and excluded from the module |

## Evidence Notes

The CysD/CysNC mechanism is supported by the homologous Pseudomonas ATP
sulfurylase structure and biochemistry in PMID:16387658. The FprA requirement
and evidence for a non-CysJ Pseudomonas sulfite-reduction system come from
PMID:23794620.

The earlier generic OpenScientist request exhausted its 7,200-second provider
timeout. The wave120 retry completed in 845 seconds with three iterations and
is retained as
[`aps_dependent_assimilatory_sulfate_reduction-deep-research-openscientist.md`](../../../modules/aps_dependent_assimilatory_sulfate_reduction-deep-research-openscientist.md).
It supports the three-step boundary and cross-lineage enzyme variation, but its
organism-mixed mechanistic synthesis and immediate-ferredoxin wording were not
treated as authority. The taxon-aware report and both primary papers remain the
basis for the PSEPK realization and its explicit donor uncertainty.

The gene-level `cysI` report correctly recovered the sulfite-reductase
hemoprotein role but overgeneralized the classical *E. coli* CysJ architecture
and promoted `PP_0860`/`PP_1703` from KEGG context. That inference was not
imported. Q88KB9 maps to broad family PTHR32439, which contains the reviewed
ferredoxin-dependent sulfite reductase Sir P9WJ02. PTHR32439 and PTHR11493 each
span sulfite reductases with different donor architectures, so family placement
does not discriminate the route. Because Q88KB9's own SF9 label is misleading,
the activity proposal uses the exact Sir exemplar, Pseudomonas genetics, and
GO:0050311 function constraint rather than the SF name.

PMID:23794620 used *P. putida* DSM 3601 rather than KT2440. It corroborates the
Pseudomonas FprA-fed physiology, but the `fpr-I` process proposal is therefore
an orthology transfer and the paper is not treated as direct Q88MD5 or Q88KB9
mutant evidence. `PP_0860` remains unresolved.

The separate `PP_0860` report reached the opposite and better-supported
architecture-level conclusion. It identified an N-terminal polytopic
PepSY-associated membrane region fused to a CysJ-like diflavin reductase
module, consistent with the target record's iron-regulated
inner-membrane-protein PANTHER placement rather than a canonical soluble CysJ
subunit. Its proposed ferric-siderophore or membrane-partner acceptor remains
an untested hypothesis, so the report supports exclusion from this module but
does not justify a new substrate-specific molecular function.

The `cysH` report agreed with the exact-record APS-reductase assignment. The
`cysD`, `cysNC`, and `fpr-I` retrieval failures are recorded as provider
timeouts rather than incomplete curation; their reviews rely on exact UniProt
records and the primary biochemical or genetic evidence cited above.

Exact local family grounding uses PTHR43196:SF1 for CysD,
PTHR47878:SF1 for Fpr-I, and specific InterPro families for CysN, CysH, and
CysI where the PSEPK PANTHER labels are misleadingly broad. The reusable module
also includes the classical CysJ/CysI alternative using reviewed E. coli
exemplars P38038 and P17846 with PTHR19384:SF128 and PTHR11493:SF47.

The 54-gene KEGG candidate inventory is retained in
[`ppu00920_assimilatory_sulfate_reduction.tsv`](ppu00920_assimilatory_sulfate_reduction.tsv).

## 2026-09-01 repair checkpoint

The wave120 annotation-reviewer pass rechecked all 27 imported GOA rows across
the six focused genes, together with the four explicit `NEW` proposals. No
row-level action changed: the CysNC qualifier correction, family-grounded CysI
proposal, DSM 3601-to-KT2440 Fpr-I orthology transfer, and conservative
PP_0860 decisions remain supported by the exact records and primary evidence.

The reusable module now grounds the CysD activity with the exact local PAINT
node `PTN001249481`, whose `PTHR43196` IBD record carries `GO:0004781` and is
seeded by E. coli P21156. The terminal variant axis is described as an
electron-supply architecture rather than an experimentally resolved immediate
donor: Pseudomonas physiology supports an Fpr-linked CysI system, while the
immediate carrier and direct donor-specific activity remain explicit knowledge
gaps. The direct APS route, three-step boundary, and exclusion of PP_0860 are
unchanged. Fresh generic OpenScientist research completed in 845 seconds; its
useful boundary synthesis was integrated, while overgeneralized claims were
left in the generated report rather than promoted into curated structure.
