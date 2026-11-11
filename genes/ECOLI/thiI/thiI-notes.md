# thiI (P77718, ECOLI): curation notes

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

## What is established for E. coli ThiI

- The reference ThiI: 482 aa, with THUMP (61-165), the PP-loop AANH domain and a C-terminal
  rhodanese domain (404-482); active-site Cys456 and a Cys344-Cys456 disulfide (UniProt
  features).
- s4U8 synthesis: U8 is adenylated by the PP-loop domain (D189, K321 essential;
  PMID:10595545), and IscS-derived persulfide is transferred through Cys456 [PMID:15037613
  "IscS catalyzes sulfur transfer from l-cysteine to ThiI, which utilizes Mg-ATP to activate
  uridine 8 in tRNA and transfers sulfur to give s4U"; PMID:10722656].
- Substrate rules (PMID:15037613): the minimal substrate is a mini-helix of the stacked
  acceptor and T stems with a bulge of at least 4 nt that begins at the target U; a blunt 3'
  end gives under 0.1% activity; nothing outside U8 is sequence-specific. These are recorded
  as findings on the reference. The schema has no structured slot for substrate
  determinants.
- Thiamine: thiI- cells make no ThiS-thiocarboxylate (PMID:9632726). In Salmonella the
  rhodanese domain alone suffices for thiazole (PMID:21724998).
- Over-annotations: detection of UV (s4U is the chromophore), L-cysteine catabolism (IscS's
  step) and sulfur carrier activity (the Cys456 persulfide is a catalytic intermediate).
