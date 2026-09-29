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
- Generic `protein binding` annotations were migrated from
  MARK_AS_OVER_ANNOTATED to REMOVE under the current GO:0005515 policy: the
  reported interactions are true, but the rows do not by themselves establish an
  evidence-backed, specific molecular function for Zds1.
- Coimmunoprecipitation with Cdc55 and Tpd3 demonstrates association with
  PP2A-Cdc55, not `part_of` membership in the heterotrimeric PP2A holoenzyme;
  no new GO:0000159 annotation is proposed.

## Core synthesis

Zds1 is a non-catalytic PP2A-Cdc55 adaptor/regulator. Its principal conserved
role is to establish the cytoplasmic and cortical pool of PP2A-Cdc55 and limit
nuclear Cdc55, thereby coordinating mitotic entry and exit. Cell-polarity,
cell-wall, mRNA-export, and chromatin-silencing phenotypes are retained where
experimentally supported but are secondary to this core mechanism; the broad
mRNA-transport parent is marked over-annotated because the more specific
nuclear-export term is already supported.

## 2026-09-29 IBA re-review

Re-checked the three ZDS1 IBA rows against `projects/IBA_REVIEW.md` and the
current `interpro/panther/PTHR28089/PTHR28089-paint.tsv` cache. The
`GO:0005737` cytoplasm, `GO:0010971` positive regulation of G2/M transition of
mitotic cell cycle, and `GO:0030010` establishment of cell polarity rows all
trace to `PANTHER:PTN001999034`, the fungal ancestral node for the Zds1/Zds2
family, and all are supported by direct budding-yeast ZDS1/ZDS2 seeds in PAINT.
The target's own experimental evidence is legitimate support for the ancestral
IBD placement rather than a circular source, so all three transfers were marked
`SUPPORTS_TRANSFER`; the polarity row remains `KEEP_AS_NON_CORE` because that
process is secondary to the core PP2A-Cdc55 adaptor/localization activity.

This pass also migrated the six `GO:0005515` protein binding rows from the old
`MARK_AS_OVER_ANNOTATED` convention to `REMOVE`. Those interactions still
support the mRNA-export and PP2A-Cdc55 regulatory annotations, but generic
protein binding does not add an informative standalone molecular function.

Searches for newer ZDS1/Zds1, Cdc55, PP2A and Rho1 literature did not find a
newer peer-reviewed paper that supersedes the cached 2011 Cdc55-localization
work, the 2015 Rho1-output paper summarized in the Falcon report, or the 2023
yeast interactome map already referenced in the review.
