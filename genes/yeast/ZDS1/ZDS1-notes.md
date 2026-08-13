# ZDS1 review notes

## Identity and research provenance

- Canonical target: ZDS1/YMR273C, UniProt P50111. `HST1` is a legacy synonym of
  ZDS1 and caused the earlier directory collision with canonical sirtuin HST1
  (YOL068C/P53685).
- The existing Falcon report is correctly grounded on P50111/ZDS1, although its
  recorded request metadata still contains the former `gene_id: HST1` value.
- `just deep-research-openscientist yeast ZDS1` was attempted twice on
  2026-08-12. Both jobs resolved P50111/ZDS1 correctly but failed while polling
  the provider (first `ConnectTimeout`, then DNS `ConnectError`). No provider
  artifact was written or fabricated.

## Curation corrections

- PMID:10662670 directly studies ZDS1 deletion and reports redistribution of
  silencing among rDNA, a silent mating-type cassette, and telomeres. The
  experimental heterochromatin annotation is therefore retained as non-core;
  the initialized review's claim that the paper concerned a different protein
  was incorrect.
- PMID:18762578 directly reports that ectopic Zds1 down-regulates PP2A-Cdc55 and
  suggests that Zds1/Zds2 act as separase-regulated PP2A-Cdc55 inhibitors.
  Later spatial-localization work refines this mechanism but does not justify
  removing the experimental molecular-function annotations.
- Generic `protein binding` annotations are marked over-annotated because they
  are true interaction observations but do not describe Zds1's adaptor/regulator
  function.

## Core synthesis

Zds1 is a non-catalytic PP2A-Cdc55 adaptor/regulator. Its principal conserved
role is to establish the cytoplasmic and cortical pool of PP2A-Cdc55 and limit
nuclear Cdc55, thereby coordinating mitotic entry and exit. Cell-polarity,
cell-wall, mRNA-export, and chromatin-silencing phenotypes are retained where
experimentally supported but are secondary to this core mechanism.
