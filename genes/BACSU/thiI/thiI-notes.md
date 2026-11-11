# thiI (O34595, BACSU): curation notes

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

## What is established for B. subtilis ThiI

- 401 aa. THUMP (60-165) and the PP-loop AANH domain, but **no rhodanese domain and no
  thiazole signature** (no IPR001763 or IPR026340/TIGR04271 in the entry). Global alignment
  to E. coli ThiI puts D189 and K321 at the same positions and C344 at C345, with no
  equivalent of Cys456.
- Gene inactivation: thiI and the adjacent desulfurase nifZ are required for s4U **but not
  thiamine** [PMID:22773787 "Gene inactivation experiments in B. subtilis indicate the
  requirement of ThiI and NifZ for the biosynthesis of 4-thiouridine, but not thiamine"].
  ThiI with NifZ makes s4U in vitro. B. subtilis has no canonical IscS.
- The same pattern holds in an archaeon: M. maripaludis ThiI is needed for s4U but not
  thiamine (PMID:22904325).
- Consequences: the thiazole row (IBA, PAINT PTN001804941) and the thiamine diphosphate row
  (UniRule UR000075655) are removed. Source defects record the PAINT node, the UniRule rule,
  and the UniProt FUNCTION text and CATALYTIC ACTIVITY (RHEA:43340) that HAMAP MF_00021
  propagates to this entry.
