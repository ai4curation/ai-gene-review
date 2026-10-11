# Notes for DANRE fads2

## 2026-05-09 review notes

- Core function is ER membrane fatty-acid/acyl-CoA desaturation for unsaturated fatty-acid biosynthesis [file:DANRE/fads2/fads2-uniprot.txt "Fatty acid desaturase with bifunctional delta-5 and delta-6"].
- Generic lipid metabolic process and oxidoreductase terms were modified to specific unsaturated fatty-acid biosynthesis and acyl-CoA desaturase terms [file:DANRE/fads2/fads2-uniprot.txt "PATHWAY: Lipid metabolism; polyunsaturated fatty acid biosynthesis."].
- Liver development is retained as non-core because it comes from a GWAS candidate morpholino screen and is downstream of the metabolic enzyme role [PMID:23813869 "function of gene candidates during liver development"].
- Core functions now explicitly list both acyl-CoA 6-desaturase activity and acyl-CoA (8-3)-desaturase activity for the bifunctional Fads2 enzyme [file:DANRE/fads2/fads2-uniprot.txt "Fatty acid desaturase with bifunctional delta-5 and delta-6"].

## Re-review 2026-09-29

Starting state: valid with 1 warning (2 PENDING IBA rows); every ACCEPT was supported only by
UniProt FUNCTION plus falcon deep-research paraphrases, with no primary literature cached.

- Cached the two primary papers and rebuilt the evidence base on them:
  Hastings et al. 2001 [PMID:11724940 "it conferred on the yeast the ability to convert
  di-homo-gamma-linoleic \nacid (20:3n-6) and eicosatetraenoic acid (20:4n-3) to arachidonic
  acid (20:4n-6) \nand eicosapentaenoic acid (20:5n-3), respectively, indicating that the
  zebrafish \ngene encodes an enzyme having both Delta5 and Delta6 desaturase activity."] —
  this is the ECO:0000269 source behind the UniProt catalytic activities — and Bláhová et al.
  2022 [PMID:35456508 "...suggest \nthat the zebrafish bifunctional FADS2 enzyme is actually a
  trifunctional \nΔ6/Δ5/Δ8 desaturase."].
- Resolved the 2 PENDING rows, both IBA from the front-end desaturase node PTN002321280:
  GO:0006629 lipid metabolic process -> MODIFY to GO:0006636 (same action as the InterPro IEA
  row for that term), and GO:0016717 -> MODIFY to GO:0016213 + GO:0062076. Term definition of
  GO:0016717 checked via QuickGO: it is the generic two-donor/O2-to-two-waters desaturase
  chemistry, true but position-blind, whereas the regiospecificity was measured directly for
  this protein. Both carry propagation_review (TERM_SCOPING_PROBLEM / GRANULARITY_MISMATCH)
  arguing node depth, not donor count: the node spans plant, nematode, Dictyostelium and
  mycobacterial members, so a specific term could not have been placed there.
- GO:0016020 membrane IBA kept MODIFY to GO:0005789, now with a propagation_review too.
- GO:0016213 and GO:0062076 remain ACCEPT but are now supported by the yeast-expression
  results rather than by UniProt paraphrase; GO:0006636 ACCEPT now cites the in vivo crispant
  data [PMID:35456508 "Our data suggest an impaired pathway of the LC-PUFA biosynthesis ...
  finally resulting in bad-quality eggs."].
- GO:0001889 liver development IMP kept KEEP_AS_NON_CORE with the participation test spelled
  out and the actual screen result quoted [PMID:23813869 "knockdown of cpn1, trib1, fads2,
  slc2a2 or samm50 all resulted in diminished fabp10a expression and a greater proportion of
  smaller livers compared with controls"]. A desaturase does no work in hepatic specification.
- Kept one deep-research quote, the ERp57 co-localization, because it is zebrafish-specific ER
  evidence absent from UniProt; dropped the rest as paraphrase.
- Added reference_review to all 3 PMIDs, rewrote description and both core_function
  descriptions, and filled the empty suggested_questions/experiments (C24 Sprecher step; direct
  test of the delta-8 activity; rescue test for the liver phenotype).

Validation after edits: zero errors, zero warnings.
