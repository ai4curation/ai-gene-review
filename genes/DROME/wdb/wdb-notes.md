# wdb (widerborst, Drosophila melanogaster) curation notes

Accession: A0A6F7R657 (TrEMBL, FBgn0027492). `just fetch-gene DROME wdb` resolved to Q9VB23 (21 GOA rows);
the expected accession A0A6F7R657 also has GOA rows (12) and was used, as instructed.

Deep research: falcon run queued at time of review (see later commits).

## Literature journal

- PP2A-B56 (Wdb/Wrd) in oocyte meiosis: cohesion, end-on attachments, metaphase I arrest; centromeric recruitment
  [PMID:34297127 "PP2A-B56, which has a B subunit encoded by two partially redundant paralogs, wdb and wrd, is also required for maintenance of sister chromatid cohesion, establishment of end-on microtubule attachments, and metaphase I arrest in oocytes"]
  [PMID:34297127 "WDB recruitment to the centromeres depends on BUBR1, MEI-S332 and kinetochore protein SPC105R"].
- B55 and B56 antagonize Aurora B spindle assembly (a regulatory, opposing role)
  [PMID:34297127 "We found that both forms of PP2A, B55 and B56, antagonize the Aurora B spindle assembly function, suggesting that a balance between Aurora B and PP2A activity maintains the oocyte spindle during meiosis I"].
- Hippo [PMID:36205125 "PP2A(Wdb) acts genetically upstream of the antagonistic activities of the Hpo regulators Sav and Rassf"].
- Insulin/TOR and autophagy [PMID:22330894 "wdb genetically interacts with the PtdIns3K/PTEN/Akt signaling cascade"].

## Decisions

- Signal transduction (InterPro2GO) marked over-annotated.
- Maintenance of sister chromatid cohesion -> maintenance of meiotic sister chromatid cohesion; meiotic spindle assembly -> regulation of spindle assembly (PP2A opposes Aurora B rather than building the spindle). Same treatment applied to tws/mts/Pp2A-29B rows from PMID:34297127.
