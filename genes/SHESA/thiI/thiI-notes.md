# thiI (A0KZA4, SHESA): curation notes

## 2026-11-05: literature search and review

No deep-research provider API keys were available in the session, so this gene has no
`-deep-research-*` file. The literature search was done by hand:

- PubMed `ThiI[Title] AND (tRNA OR thiouridine OR thiamin)`: 12 hits. The ThiI ones were
  cached: PMID:21724998, PMID:21742874, PMID:19509301, PMID:18604845, PMID:16343540,
  PMID:11443125, PMID:10753862, PMID:10722656, PMID:10595545, PMID:9209060. The other two
  concern an unrelated *Aspergillus* thiamine transporter also named thiI.
- Targeted: PMID:15037613 (E. coli substrate specificity), PMID:22773787 (B. subtilis
  thiI/nifZ), PMID:22904325 (M. maripaludis ThiI). All cached entries are abstract-only.

InterPro2GO IPR020536 maps every ThiI to GO:0004810 CCA tRNA nucleotidyltransferase activity.
The UniProt queries `rhea:24176 AND reviewed:true` and `rhea:24176 AND reviewed:true AND
go:0004810` both return 287 entries (2026-11-11), so every reviewed ThiI is affected. Reported
as https://github.com/geneontology/go-annotation/issues/6646 and recorded as a
`source_defects` entry on the GO:0004810 row. The schema's `SourceResourceEnum` has no
INTERPRO value, so that defect uses `resource: OTHER` with `record: InterPro:IPR020536`,
`slot: interpro2go` (as in genes/ECOLI/hemW).

## What is established for Shewanella sp. ANA-3 ThiI

- No experimental literature on this protein; everything is by homology.
- 484 aa with the full E. coli-type architecture: THUMP (63-167), PP-loop AANH domain, and a
  C-terminal rhodanese domain (406-484) carrying the thiazole signature (IPR026340 /
  TIGR04271). UniProt features give the active site at Cys458 and a Cys346-Cys458 disulfide.
  Global alignment to E. coli ThiI maps D189/K321/C344/C456 to D191/K323/C346/C458.
- Shewanella oneidensis ThiI (Q8EGR4) sits in PANTHER clade PTN000769419, together with the
  E. coli, Salmonella, Yersinia, Vibrio and Pseudomonas proteins, all of which carry the
  rhodanese domain and thiazole signature. The thiazole row is therefore accepted on domain
  grounds, unlike for rhodanese-less B. subtilis ThiI.
