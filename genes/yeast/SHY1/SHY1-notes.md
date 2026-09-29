# SHY1 notes

## 2026-09-29 IBA re-review

SHY1 has two IBA rows from `GO_REF:0000033`, both traced by GOA to
`PANTHER:PTN000603741` in the SURF1/Shy1 family. The repository has
`PTHR23427` in `interpro/panther/panther.obo`, with S. cerevisiae Shy1 in
`PTHR23427:SF2 SURFEIT LOCUS PROTEIN 1`, but no cached PTHR23427 PAINT TSV or
PTN record. I added structured `propagation_review` blocks to both rows and
recorded the PTN as `SOURCE_STALE_OR_MISSING` because the exact ancestral
assertion cannot be recovered from a local PAINT export.

The complex IV assembly IBA is a sound core transfer. S. cerevisiae Shy1 has
direct experimental support as a complex IV assembly factor that interacts with
Mss51, Cox14, Coa1, and complex IV subcomplexes [PMID:17882259; PMID:17882260],
and the current review already captures this as SHY1's central process. The
mitochondrion IBA is also sound, with direct inner-mitochondrial-membrane
evidence from the original yeast characterization [PMID:9162072]. The 2024
S. pombe Shy1/SURF1 homolog study provides newer ortholog corroboration for
mitochondrial localization and complex IV assembly, but it does not change the
S. cerevisiae action calls [PMID:39289458].

I reclassified both `GO:0005515 protein binding` IPI rows from
`MARK_AS_OVER_ANNOTATED` to `REMOVE` under the current generic-protein-binding
policy. The Cox14/Mss51 and Coa1 contacts are real, but the informative
curation is Shy1's role in complex IV assembly, not a standalone protein-binding
MF. I also changed the obsolete `GO:0051082 unfolded protein binding` IMP row to
`REMOVE`; PMID:11389896 supports a Shy1-containing assembly complex and a
complex IV assembly/stability role, not direct general binding to unfolded
substrates.

## Newer-literature search

I searched 2023-2026 SHY1/Shy1/SURF1 yeast literature. I did not find a newer
direct S. cerevisiae SHY1 paper. The relevant recent paper is Luo et al. 2024 on
the S. pombe SURF1 homolog Shy1 [PMID:39289458], which is useful for IBA
ortholog context because PomBase:SPBC1215.01 appears in the GOA
`WITH/FROM` field for the mitochondrial IBA.
