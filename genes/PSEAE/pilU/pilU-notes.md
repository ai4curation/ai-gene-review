# pilU (PA0396, UniProt G3XCX3) review notes

No deep-research provider was available; the notes below are from my own
reading of the cached publications, PubMed and the UniProt entry.

## Identity

- Fetched accession G3XCX3 (PILU_PSEAE), PA0396, 382 aa, matches the
  PseudoCAP worklist entry (rank 39).
- PilT/PilU family (InterPro IPR006321, NCBIfam TIGR01420 pilT_fam), PANTHER
  PTHR30486:SF12 "TYPE IV PILUS ATPASE PILU"; Walker A ATP site 133-138 by
  similarity [file:PSEAE/pilU/pilU-uniprot.txt]. No nuclease domain.

## Function

- pilU lies directly downstream of pilT; mutants lose twitching, are
  hyperfimbriate but stay phage-sensitive [PMID:7854122 "The other three
  transposon mutations were found to have occurred within a new gene located
  directly downstream of pilT."; "Like pilT mutants, the pilU mutants were
  hyperfimbriate"].
- Purified PilU is an ATPase [PMID:18174131 "Assay of purified 6xHis-tagged
  PilB, PilT and PilU from P. aeruginosa showed that all three proteins have
  ATPase activities in vitro."].
- Unipolar localization at the piliated pole [PMID:15659660 "PilB and PilT
  fusions localized to both poles, while PilU fusions localized only to the
  piliated pole."].
- PilT-dependent retraction ATPase [PMID:31525185 "Finally, we show that
  Pseudomonas aeruginosa PilU also functions as a PilT-dependent retraction
  ATPase"].
- PilU matters for retraction under load [PMID:30804544 "its partner ATPase
  PilU may improve retraction only in high-friction environments"].
- Crystal structure: hexameric motor [PMID:41055394 "PilU is a hexameric
  motor ATPase with unique features."]; pilU mutants have high cAMP and some
  PilA/PilY1 alleles restore twitching without PilU.
- Species variation: P. stutzeri pilU is dispensable for twitching
  [PMID:11466271 "Insertional inactivation did not affect piliation, twitching
  motility, or PO4 infection but reduced transformation to about 10%."];
  D. nodosus pilU is required [PMID:18310333 "We showed that mutation of
  either the pilT or pilU gene eliminated the ability to carry out twitching
  motility."].

## Reference check: PMID:18174131 and the DNA endonuclease row

- PubMed-verified: Chiang et al. 2008, Microbiology 154:114-126, "Functional
  role of conserved residues in the characteristic secretion NTPase motifs of
  the Pseudomonas aeruginosa type IV pilus motor proteins PilB, PilT and
  PilU". The PMID is correct for PilU; it is NOT a mis-keyed reference
  (PMID:18174132 is the ccmC paper in the same issue, pp. 127-138, with no
  PilU content). So reference_review correctness is VERIFIED, not
  WRONG_IDENTIFIER.
- The error is in the GO term. The abstract reports ATPase activity only.
  PseudoCAP annotated PilB (PA4526) from the same paper, same date
  (2019-03-11), to GO:0016887 ATP hydrolysis activity; PilU got GO:0016888
  "DNA endonuclease activity, producing 5'-phosphomonoesters", the next GO
  id. This is an off-by-one term keying error. Recorded as WRONG_TERM
  (cause IDENTIFIER_TRANSPOSITION, REPOINT to GO:0016887, CONFIRMED) for
  PseudoCAP, and as a WRONG_TERM defect for GO_Central on the PTN000766390 IBD.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN000766390 | GO:0016888 DNA endonuclease activity, producing 5'-phosphomonoesters | 1 (sole seed) | 13 (9 taxa) | GO:0016888, IDA, PMID:18174131 (PseudoCAP) | WRONG | The paper (correct PMID) assays ATPase activity of purified PilU; no nuclease assay, no nuclease domain. GO:0016888 is a mis-keyed id for the adjacent GO:0016887 ATP hydrolysis activity, which PseudoCAP gave PilB from the same paper. The IBD and its ~13 leaf IBAs (including the one back onto PilU) should be withdrawn or repointed to ATP hydrolysis activity. |
| PTN000766390 | GO:0043107 type IV pilus-dependent motility | 1 (sole seed) | 13 (9 taxa) | GO:0043107, IMP, PMID:7854122 (PseudoCAP) | SOUND | pilU transposon mutants lose twitching while keeping (excess) pili; PilU is itself a retraction motor, so it does part of the work of twitching. Suitable for a small PilU clade, with the caveat that some orthologs (P. stutzeri; Neisseria) are not needed for twitching. |

## Decisions summary

- ACCEPT: ATP binding (IEA), cytoplasm (EXP, IEA), type IV pilus-dependent
  motility (IBA, IMP).
- MODIFY: DNA endonuclease activity IDA -> ATP hydrolysis activity
  (GO:0016887); PseudoCAP WRONG_TERM defect.
- REMOVE: DNA endonuclease activity IBA (propagated keying error); GO_Central
  WRONG_TERM defect on PTN000766390.
- No GO process term exists for type IV pilus retraction; raised as a
  suggested question.
