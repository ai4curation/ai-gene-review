# EPS8L2 (donkey, Equus asinus; UniProt A0A9L0KBR4) - review notes

## Sources used

- Donkey UniProt record (unreviewed, Ensembl-derived): `EPS8L2-uniprot.txt`.
- Donkey GOA (8 IEA rows; 7 TreeGrafter GO_REF:0000118 rows from PANTHER node PTN008992914, 1 UniProt SubCell mapping GO_REF:0000044): `EPS8L2-goa.tsv`.
- Human ortholog EPS8L2 (Q9H6S3) UniProt record, fetched 2026-10-14: `EPS8L2-bioinformatics/human-EPS8L2-Q9H6S3-uniprot.txt`.
- Donkey-human alignment: `EPS8L2-bioinformatics/RESULTS.md`.
- Human QuickGO annotations (queried 2026-10-14) were used as a comparator: human EPS8L2 carries IDA/IGI annotations from PMID:14565974 for actin binding, Rho protein signal transduction, regulation of Rho protein signal transduction, ruffle membrane and positive regulation of ruffle assembly, plus IBA rows for the same terms and plasma membrane. PMID:14565974 is not cached in `publications/`, so it is not quoted here.
- No GOA row for the donkey protein cites a publication, so no publication was fetched.

## Identity and family

- Donkey record: "Belongs to the EPS8 family." [file:EQUAS/EPS8L2/EPS8L2-uniprot.txt "Belongs to the EPS8 family."]
- Domains: PTB, SH3 (459..542) and the EPS8 C-terminal effector region (InterPro EPS8-like IPR039801; PANTHER PTHR12287:SF20 EPS8-like protein 2).
- The donkey protein (681 aa) aligns to human EPS8L2 (715 aa) end to end [file:EQUAS/EPS8L2/EPS8L2-bioinformatics/RESULTS.md "Paired residues: 679; identical: 572; identity over paired: 84.24%"]. Missing human segments are N-terminal (4..27, 38..47).

## Function (human ortholog)

- [file:EQUAS/EPS8L2/EPS8L2-bioinformatics/human-EPS8L2-Q9H6S3-uniprot.txt "Stimulates guanine exchange activity of SOS1. May play a role in membrane ruffling and remodeling of the actin cytoskeleton."]
- Complex/actin: [same file "Part of a complex that contains SOS1, ABI1 and EPS8L2. Associates with F-actin."]
- Hearing: [same file "In the cochlea, is required for stereocilia maintenance in adult hair cells"]; localization [same file "Localizes at the tips of the stereocilia of the inner and outer hair cells."] (by similarity to mouse). Human disease DFNB106 (deafness).

## Review decisions (summary)

- actin binding: ACCEPT (core MF; EPS8 family actin capping/bundling, human IDA).
- cytoplasm: ACCEPT. plasma membrane: KEEP_AS_NON_CORE (the informative location is ruffle membrane). ruffle membrane: ACCEPT.
- vesicle: KEEP_AS_NON_CORE (human support is only exosome proteomics, HDA).
- Rho protein signal transduction / regulation of Rho protein signal transduction / positive regulation of ruffle assembly: ACCEPT (SOS1-ABI1-EPS8L2 Rac-GEF complex; human IDA/IGI).
- NEW: stereocilium tip (GO:0032426) location, supported by the human UniProt location note (by similarity to mouse).

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not opened or used.

### Deep research

`just deep-research-falcon EQUAS EPS8L2 --fallback perplexity-lite` failed: falcon "Failed to authenticate"; perplexity-lite fallback returned HTTP 401 (quota exceeded). No deep-research file was written. The review uses primary literature cached for this session instead.

### Literature cached and read (publications/)

- PMID:14565974 (Offenhäuser 2004, full text): human EPS8L1-3 characterization. [PMID:14565974 "only eps8L1 and eps8L2 activate the Rac-GEF activity of Sos-1, and bind to actin in vivo"]; direct F-actin cosedimentation of the EPS8L2 C-terminus [PMID:14565974 "eps8, eps8L1, and L2, but not eps8L3 could directly associate to F-actin"]; ruffle localization and rescue of ruffling in Eps8-/- MEFs [PMID:14565974 "Ectopic expression of eps8, eps8L1, or eps8L2, but not of eps8L3, restored ruffling formation"].
- PMID:23918390 (Furness 2013, mouse, full text): [PMID:23918390 "localized at the tips of stereocilia of both cochlear and vestibular hair cells"]; knockout gives late-onset progressive hearing loss.
- PMID:26282398, PMID:41514136: human DFNB106 genetics (context only).
- PMID:34346063 (BAIAP2L2, abstract only): EPS8L2 is a binding partner of the stereocilia "row 2 complex" (BAIAP2L2, TWF2, CAPZB2); context only, not cited in the review.
- PMID:19190083: source of the human vesicle row (exosome-like vesicle proteomics).

### Identity

A0A9L0KBR4 (681 aa, Ensembl ENSEASP00005062258) is the donkey EPS8L2 gene product, PANTHER PTHR12287:SF20 (EPS8L2 subfamily; same subfamily as human Q9H6S3 and mouse Q99K30 per `interpro/panther/PTHR12287/PTHR12287-entries.csv`). It is not a fragment: it aligns end to end to human (84.24% identity, 99.7% of donkey covered); the only notable differences are short gaps in the human N-terminal low-complexity region before the PTB domain (human 4..27, 38..47), consistent with species divergence or a slightly different start in the gene model. PTB, SH3 and the C-terminal F-actin-binding effector region are all present. The task header said "PANTHER from UniProt: (none listed)", but the donkey UniProt record does list PTHR12287:SF20.

### Evolutionary basis of the IEA rows

All seven TreeGrafter rows cite PTN008992914 (the graft node; QuickGO shows it used only for EQUAS EPS8L2 rows). Human/mouse IBA rows for the same terms come from family nodes PTN000958212 (actin binding, Rho signal transduction, regulation of Rho signal transduction, plasma membrane) and PTN000264860 (ruffle membrane, positive regulation of ruffle assembly). The donkey TreeGrafter set also contains vesicle (GO:0031982), which is not among the human or mouse IBA rows; the only experimental basis in human is exosome proteomics.

### Decisions (changed vs the previous review)

- actin binding: ACCEPT -> MODIFY to actin filament binding (GO:0051015), since the evidence is direct F-actin cosedimentation (MGI already uses GO:0051015 for mouse from the same paper).
- cytoplasm: ACCEPT -> KEEP_AS_NON_CORE (true, but functional locations are ruffle membrane and stereocilium tip).
- plasma membrane: KEEP_AS_NON_CORE -> MODIFY to ruffle membrane (correct-but-general rule; ruffle membrane is part_of plasma membrane, verified via OLS ancestors).
- vesicle: KEEP_AS_NON_CORE -> MARK_AS_OVER_ANNOTATED (proteomics-only, not in the PAINT IBA set).
- Rho protein signal transduction, regulation of Rho protein signal transduction, ruffle membrane, positive regulation of ruffle assembly: ACCEPT (unchanged), now quoting PMID:14565974 directly.
- NEW stereocilium tip (GO:0032426): retained, now referenced to the mouse primary paper (PMID:23918390, same SF20 subfamily) with ISS.
- Not added: stereocilium maintenance (GO:0120045), sensory perception of sound (GO:0007605) - knockout phenotypes, and the CLAUDE.md rule against turning necessity into participation applies. Not added: contributes_to GEF activity (GO:0005085) - human IDA exists but PAINT did not propagate it; raised as a suggested question instead.
- Core functions split into (1) Rac-GEF/ruffle module and (2) stereocilium-tip actin binding.

### Relative and family

- Closest characterized relative: human EPS8L2 (Q9H6S3), same PANTHER subfamily SF20; no review exists in the repo (genes/human/EPS8L2 absent). Mouse Eps8l2 (Q99K30, SF20) is also characterized (stereocilia).
- No PANTHER family review under interpro/panther/PTHR12287 beyond metadata/entries files; no subfamily-placement disagreement.
- No module under modules/ covers EPS8L2, the EPS8-ABI1-SOS1 complex or stereocilia.
