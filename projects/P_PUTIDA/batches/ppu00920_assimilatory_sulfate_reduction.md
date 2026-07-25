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
- [ ] Complete OpenScientist gene-level research.
- [ ] Complete generic module OpenScientist research.
- [x] Complete module + `ppu00920` + PSEPK OpenScientist research.
- [x] Resolve the CysNC APS-kinase-domain and PP_0860 questions after research.
- [ ] Integrate useful research findings without treating provider output as authority.
- [ ] Validate and render the module, gene reviews, and batch page.
- [ ] Open and shepherd one PR for this module.

## Focused Genes

| Gene | Locus | UniProt | Module role | First-pass result |
|---|---|---|---|---|
| `cysD` | PP_1303 | Q88NA9 | ATP sulfurylase catalytic subunit | Exact sulfate adenylyltransferase MF and sulfate-assimilation process accepted |
| `cysNC` | PP_1304 | Q88NA8 | ATP sulfurylase regulatory GTPase | GTPase activity accepted; contributes to sulfate adenylyltransferase |
| `cysH` | PP_2328 | Q88KG2 | APS reductase | APS-reductase MF accepted; conflicting PAPS-reductase annotation removed |
| `cysI` | PP_2371 | Q88KB9 | sulfite-reductase hemoprotein | Ferredoxin-dependent sulfite reduction synthesized as the current model |
| `fpr-I` | PP_1638 | Q88MD5 | FprA-type electron supply | Exact FNR MF accepted and sulfate-assimilation role added to the synthesis |
| `PP_0860` | PP_0860 | Q88PJ0 | questionable CysJ-like candidate | FMN binding retained; exact redox role undecided and excluded from the module |

## Evidence Notes

The CysD/CysNC mechanism is supported by the homologous Pseudomonas ATP
sulfurylase structure and biochemistry in PMID:16387658. The FprA requirement
and evidence for a non-CysJ Pseudomonas sulfite-reduction system come from
PMID:23794620.

Exact local family grounding uses PTHR43196:SF1 for CysD,
PTHR47878:SF1 for Fpr-I, and specific InterPro families for CysN, CysH, and
CysI where the PSEPK PANTHER labels are misleadingly broad. The reusable module
also includes the classical CysJ/CysI alternative using reviewed E. coli
exemplars P38038 and P17846 with PTHR19384:SF128 and PTHR11493:SF47.

The 54-gene KEGG candidate inventory is retained in
[`ppu00920_assimilatory_sulfate_reduction.tsv`](ppu00920_assimilatory_sulfate_reduction.tsv).
