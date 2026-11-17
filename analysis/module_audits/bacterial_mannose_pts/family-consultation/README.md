# Mannose PTS family consultation

Two new family reviews assess PTHR33799 and PTHR32502 without modifying any of
their six fetched metadata, member-entry, or PAINT files. All eight ordered PAINT
assertions retain their original node, term, evidence, polarity, seeds, taxon and
date. The source assertions are preserved even when their scope is questioned.

## Scientific decisions

PTHR33799 contains IIA-bearing proteins: separate IIA chains such as 146-residue
Bacillus LevD and fused IIA/IIB chains such as 323-residue E. coli ManX. They share
the single PANTHER SF1. Broad participation in GO:0009401 remains a family-wide
positive. Specific mannose transport, completeness of the sugar-directed reaction,
and physical association with a transmembrane complex are not universal grants.
No autonomous transmembrane activity is inferred for isolated IIA. An IIB role
requires independent domain evidence, not another use of the same family label.

PTHR32502 is broader than a membrane-transporter family. Its current root covers
IIC/IID proteins and downstream carbohydrate enzymes. The root GO:0009401
assertion is assessed TOO_DEEP because GatZ/KbaZ support downstream aldolase work
rather than coupled uptake/phosphorylation. The positive GO:0008047 assertion at
the narrower GatZ/KbaZ node is SOUND. The root membrane claim and the two
mannose-specific nodes remain UNRESOLVED; their evidence does not establish a
uniform function or identify a particular historical gain/loss/pruning event.
The family-wide term assessments are correspondingly unresolved, retaining
positive exact members without creating an incomplete subfamily list that
implicitly labels every omitted branch negative.

The primary abstract of PMID:2117666 explicitly reports that LevDEFG performs
fructose transport and is not involved in mannose uptake. This is an explicit
source-reported boundary, not an inference from an absent GO annotation, title,
or donor count. Its full experimental negative assay was not independently read;
no gene experimental annotation is removed and no definitive ancestral loss is
invented from that abstract. Both negative-node scope and unknown secondary
activity remain properly bounded.

PMID:11976750 was absent and was fetched normally. Its abstract and linked
curated UniProt ECO:0000269 FUNCTION statements establish positive GatZ/KbaZ
support for aldolase Y activity and stability. They do not establish autonomous
foldase activity or license membrane PTS proteins as enzyme activators. Manual
reference assessments and availability remain in `reference-assessments.yaml`,
because the family schema's Reference class accepts only id/title. The same
schema lacks `record_section`; the relevant UniProt FUNCTION sections and
publication-linked evidence are identified in the consultation instead.

## Verified selector boundaries

| Role/member | PANTHER placement | Independent architecture |
| --- | --- | --- |
| E. coli ManX P69797 | PTHR33799:SF1 | PF03610 IIA + PF03830 IIB, fused |
| E. coli ManY P69801 | PTHR32502:SF4 | IIC, PF03609 |
| E. coli ManZ P69805 | PTHR32502:SF5 | IID, PF03613 |
| IL1403 PtnAB/PtnC/PtnD Q9CEX8/Q9CEX7/Q9CEX6 | SF1 / SF25 / SF27, in the respective families above | Fused IIA/IIB, separate IIC and IID |
| UA159 reference candidates Q8DSC4/Q8DSC3/Q8DSC2 | Same SF1 / SF25 / SF27 pattern | Classification is verified; primary locus/strain assay attribution is a separate consultation |
| Bacillus LevD P26379 | PTHR33799:SF1 | Separate IIA, PF03610; fructose-system control |
| Bacillus LevE P26380 | No PANTHER cross-reference in the official snapshot | Separate IIB, PF03830/IPR004720; no invented family ID |
| Bacillus LevF/P26381 and LevG/P26382 | PTHR32502:SF4 / SF5 | IIC / IID; not licensed as positive mannose exemplars |

The role model may let one fused protein fill both IIA and IIB roles, or let
separate positively identified chains fill those roles. Neither two distinct
genes nor exclusively intramolecular transfer is required. The IIB role cannot
be satisfied by any arbitrary SF1 member. The split L. curvatus architecture
belongs to the primary-source consultation; no active, complete reference quartet
was invented from partial sequence or deleted UniProt records.

Official PANTHER names are preserved verbatim despite their misleading breadth;
readable interpretation is in preferred_name and descriptions. The unchecked
LLM descriptions in cached InterPro metadata are not functional evidence.
The official tree snapshots have 24 and 48 reference leaves, respectively; these
are not exhaustive species inventories and their size is not an evidence score.

## Checks and provenance

`check_preservation.py` verifies all 31 original protected sources, the six family
raw files, the eight PAINT objects, all quoted evidence, current official member
placements and the source/domain boundaries above. Its quote iteration is sorted
for reproducible output. `preservation.json` records the exact inputs, judgments
and verbatim snippets. `scope-ledger.json` exposes the term scope decisions.

The normal family validation phases are run only on the two new reviews: schema,
GO labels/branches, reference snippets, PAINT/PTN/member/residue grounding, and
gene cross-checks. Two matching `just new-history` records were generated and
validated. No family HTML renderer exists in this checkout. No residue rule is
invented merely to remove uncertainty; the residue validator still checks
family/PTN/member grounding. `initial-schema.log` records the initial rejected
gene-only metadata fields before they were moved into this consultation.

`build_reviews.py` is the initial draft builder and refuses to overwrite existing
reviews; final source adjudication was applied to the curated YAML afterward.
For verification, run the checker rather than rebuilding the drafts:

```sh
uv run python analysis/module_audits/bacterial_mannose_pts/family-consultation/check_preservation.py
uv run ruff check analysis/module_audits/bacterial_mannose_pts/family-consultation
```

All external official snapshots are confined to this consultation. Only the
previously absent PMID:11976750 was added through normal publication acquisition;
no pre-existing publication/provider/raw source was rewritten. No gene, module,
project, or other family was edited. No full-corpus validation, commit, or push
was performed.

Final incremental member-index grounding: **46 pass, 0 fail, 0 unresolved**.
The two family schema/term/reference/history checks pass; the scoped gene
cross-check reports zero conflicts. The shared index resolved 6,893 of 7,116
repository-cited accessions; those repository-wide unresolved references are
not unresolved groundings in these two reviews.
