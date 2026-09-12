---
title: "PSEPK D-amino-acid cell-wall precursor supply"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK D-amino-acid cell-wall precursor supply

This batch extracts a coherent cell-wall precursor-supply module from the broad
KEGG ppu00470 D-amino-acid metabolism map. The reusable boundary contains
three required parts: D-glutamate production, cytoplasmic D-alanine production,
and D-Ala-D-Ala ligation. Incorporation by MurD and MurF belongs to the existing
peptidoglycan precursor module; D-amino-acid catabolism and hydroxyproline
catabolism are separate pathways.

The complete 21-gene KEGG membership snapshot is retained in
ppu00470_d_amino_acid_cell_wall_precursor_supply.tsv. Six genes were selected
because they establish the expected steps or adjudicate the central PSEPK
uncertainty. The third Ddl paralog, ddl/PP_5673, is added from UniPathway and
UniProt even though it is absent from the KEGG membership list.

## Workflow

- [x] Define and schema-check a reusable three-part module.
- [x] Fetch the five selected gene records missing from current main.
- [ ] Full-allowance OpenScientist jobs are active for murI, alr, dadX, ddlA,
  and ddl; ddlB already has a completed OpenScientist report. These jobs are
  allowed to finish after draft PR publication and will not be stopped.
- [ ] Generic module OpenScientist research is active with the full allowance.
- [ ] Module + ppu00470 + PSEPK OpenScientist research is active with the full allowance.
- [x] Curate all six selected gene reviews and notes from current UniProt and
  independently checked primary literature.
- [x] Validate and render gene, module, batch, and project artifacts.
- [x] Publish one draft pull request.

## Selected Genes

| Done | Gene | Locus | UniProt | Module assessment |
|---|---|---|---|---|
| [x] | murI | PP_0736 | Q88PW2 | Covered D-glutamate-production step |
| [x] | alr | PP_3722 | Q88GJ9 | Excluded from cytoplasmic D-alanine supply; periplasmic BSR |
| [x] | dadX | PP_5269 | Q88CB2 | Leading cytoplasmic D-alanine candidate, physiological assignment unresolved |
| [x] | ddlA | PP_4346 | Q88EV6 | Covered DdlA-like ligase variant |
| [x] | ddlB | PP_1339 | Q88N74 | Covered DdlB-like ligase variant; prior review retained |
| [x] | ddl | PP_5673 | A0A140FWM5 | Covered DdlB-like ligase variant; relative deployment among three paralogs unresolved |

## Boundary Decisions

- murI directly covers D-glutamate production through the specific,
  cell-wall-associated glutamate racemase assignment.
- Q88GJ9 alr is not forced into the module. It is an experimentally
  periplasmic broad-spectrum racemase whose strongest substrates and
  physiological role are lysine/arginine catabolism. An alr deletion did not
  alter stationary-phase peptidoglycan composition under the tested
  conditions.
- Cytoplasmic Q88CB2 dadX is alanine-specific, reversible, and kinetically
  more efficient on alanine than Q88GJ9. However, the target paper calls its
  role catabolic and does not directly test cell-wall D-alanine supply.
  Therefore the PSEPK D-alanine-production step is candidate_uncertain, not
  covered.
- ddlA, ddlB, and ddl all have specific D-alanine-D-alanine ligase
  assignments. PANTHER separates DdlA into SF25 and DdlB into SF23; PP_5673 is
  also assigned to SF23 by UniProt. The reusable module models two family
  variants, not three invented biochemical roles.
- murD and murF consume the products of this module but are not supply steps.
  D-amino-acid dehydrogenases, hydroxyproline enzymes, DapF/LysA, and AnsB are
  KEGG-map neighbors outside this boundary.

## Hole-Filling Result

| Required step | PSEPK status | Evidence boundary |
|---|---|---|
| D-glutamate production | covered | MurI/Q88PW2 |
| Cytoplasmic D-alanine production | candidate_uncertain | DadX/Q88CB2 is the leading candidate; no direct cell-wall phenotype or flux evidence |
| D-Ala-D-Ala ligation | covered_with_variants | DdlA/Q88EV6, DdlB/Q88N74, and Ddl/A0A140FWM5 |

The unresolved D-alanine assignment is a real curation/biology hole. It should
be closed with targeted genetics and metabolite-rescue evidence, not by
transferring a canonical alr assumption onto the periplasmic BSR.
