# SHY1 notes

## 2026-09-29 IBA re-review

SHY1 has two IBA rows from `GO_REF:0000033`, both traced by GOA to
`PANTHER:PTN000603741` in the SURF1/Shy1 family. I fetched the current
`PTHR23427` metadata, entries table, and PAINT node export; the cached PAINT
slice still places both `GO:0033617 mitochondrial respiratory chain complex IV
assembly` and `GO:0005739 mitochondrion` on `PTN000603741`, and
S. cerevisiae Shy1 is in `PTHR23427:SF2 SURFEIT LOCUS PROTEIN 1`.

The complex IV assembly IBA is a sound core transfer. S. cerevisiae Shy1 has
direct experimental support as a complex IV assembly factor that interacts with
Mss51, Cox14, Coa1, and complex IV subcomplexes [PMID:17882259; PMID:17882260],
and the current review already captures this as SHY1's central process. The
mitochondrion IBA is also sound, with direct inner-mitochondrial-membrane
evidence from the original yeast characterization [PMID:9162072]. The 2024
S. pombe Shy1/SURF1 homolog study provides newer ortholog corroboration for
mitochondrial localization and complex IV assembly, but it also reports that
S. pombe shy1 deletion does not critically disrupt respiratory-chain assembly
[PMID:39289458 "Unlike its homologs, deletion of shy1 does not critically
disrupt respiratory chain assembly, indicating the presence of the compensatory
mechanism(s) within S. pombe that ensure mitochondrial functionality."]. I
therefore treated it as corroborating ortholog context rather than direct
S. cerevisiae evidence.

I reclassified both `GO:0005515 protein binding` IPI rows from
`MARK_AS_OVER_ANNOTATED` to `REMOVE` under the current generic-protein-binding
policy. Both current IntAct rows are Shy1-Coa1 edges; that contact is real, but
the informative curation is Shy1's role in complex IV assembly, not a standalone
protein-binding MF. I changed the obsolete `GO:0051082 unfolded protein binding`
IMP row to `MODIFY` with a `GO:0140777 protein-containing complex stabilizing
activity` replacement; PMID:11389896 supports a Shy1-containing assembly complex
and a complex IV assembly/stability role, not general binding to unfolded
substrates.

## Newer-literature search

I searched 2023-2026 SHY1/Shy1/SURF1 yeast literature. I did not find a newer
direct S. cerevisiae SHY1 paper. The relevant recent paper is Luo et al. 2024 on
the S. pombe SURF1 homolog Shy1 [PMID:39289458], which is useful for IBA
ortholog context because PomBase:SPBC1215.01 appears in the GOA
`WITH/FROM` field for the mitochondrial IBA.
