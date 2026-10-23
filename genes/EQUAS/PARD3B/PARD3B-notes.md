# PARD3B (donkey, A0A9L0JEY6) notes

## Sources
- Donkey UniProt A0A9L0JEY6 (unreviewed; function, subunit and location text are ARBA predictions, ECO:0000256).
- Human PARD3B Q8TEW8 UniProt record fetched to PARD3B-bioinformatics/Q8TEW8-uniprot.txt. No human/mouse PARD3B review exists in this repository; the primary PARD3B papers (PMID:12234671, PMID:12459187, PMID:16458856) are not in the local publication cache.
- Ortholog experimental GO (QuickGO): PARD3B-bioinformatics/ortholog_experimental_goa.txt.
- Alignment: PARD3B-bioinformatics/RESULTS.md.

## Biology
- PARD3B (PAR3beta/PAR3L) is the vertebrate paralog of the polarity scaffold PARD3 (PAR3 family; PANTHER PTHR16484:SF4). Human UniProt: [file:EQUAS/PARD3B/PARD3B-bioinformatics/Q8TEW8-uniprot.txt "Putative adapter protein involved in asymmetrical cell"] division and cell polarization; "May play a role in the formation of epithelial tight junctions."
- Interacts with PARD6B and INSC (experimental, PMID:12234671, PMID:16458856, per human UniProt).
- Location: endomembrane system, cell junction, tight junction; [Q8TEW8-uniprot.txt "Colocalizes with TJP1 to epithelial tight junctions."].
- Experimental GO for PARD3B orthologs is limited to protein binding, protein-containing complex and cell junction (HPA IDA).
- Family-level (PARD3) functions such as phosphoinositide binding, centrosome positioning and microtubule organization are transferred by TreeGrafter from PAINT node PTN001444301; no PARD3B-specific evidence for them was found.

## Donkey sequence
- 88.3% identity overall; PDZ1-3 and N-terminal domain 94-99% identical [file:EQUAS/PARD3B/PARD3B-bioinformatics/RESULTS.md].

## Decisions
- ACCEPT: bicellular tight junction, establishment of cell polarity, establishment or maintenance of epithelial apical/basal polarity.
- TOO_GENERAL: apical junction complex, cell junction (both entailed by bicellular tight junction).
- KEEP_AS_NON_CORE (family-level transfer, plausible, unverified for PARD3B): adherens junction, cell cortex, apical plasma membrane, intracellular protein localization, microtubule cytoskeleton organization, establishment of centrosome localization, endomembrane system, protein-containing complex.
- MARK_AS_OVER_ANNOTATED: cell adhesion (scaffold organizes junctions but is not itself an adhesion mediator).
- UNDECIDED: phosphatidylinositol binding (PARD3 property; no PARD3B data accessible).

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

### Identity
- A0A9L0JEY6 (Ensembl ENSEASP00005051886.1) is a full-length donkey PARD3B: 1204 aa vs 1205 aa for human canonical Q8TEW8-1, 88.3% identity with 99.8% coverage; PDZ1-3 and the N-terminal Par3/HAL domain are intact [file:EQUAS/PARD3B/PARD3B-bioinformatics/RESULTS.md]. It is not a fragment, isoform or aberrant gene model.
- PANTHER: PTHR16484:SF4 (PARTITIONING DEFECTIVE 3 HOMOLOG B) per the donkey UniProt DR line, the same subfamily as human Q8TEW8 and mouse Q9CSB4 (interpro/panther/PTHR16484/PTHR16484-entries.csv). PARD3 is SF10 and Bazooka/PAR-3 are SF17. There is no family review for PTHR16484 under interpro/panther/ (only metadata and an entries list), so there is no subfamily disagreement to report.

### Deep research
- `just deep-research-falcon EQUAS PARD3B --fallback perplexity-lite` failed on 2026-10-21. Falcon reported "Failed to authenticate" and the perplexity fallback returned HTTP 401 (insufficient quota). No deep-research file was created. The literature below was read directly from cached publications.

### Literature (newly cached)
- PMID:12459187 (Kohjima 2002, abstract): [PMID:12459187 "Unexpectedly, in contrast to other PAR3s found in various species, PAR3beta is incapable of binding to any isotypes of PAR6 or aPKC."]; [PMID:12459187 "PAR3beta, expressed intrinsically or extrinsically, localizes to the tight junctions, indicating that the localization does not require the ternary complex formation."]
- PMID:12234671 (Gao 2002, abstract): [PMID:12234671 "No Par3L isoforms and only a subset of Par3 isoforms detectably bind aPKCs."]; "Par3L isoforms also show differential binding to Par6"; N-terminal Par3L disrupts TJ formation when overexpressed in MDCK cells. This is the source of the UniProt "Interacts with PARD6B" line, which the other two studies contradict.
- PMID:16458856 (Izaki 2006, abstract): INSC binds Par3 and Par3beta.
- PMID:24859006 (Huo & Macara 2014, full text): [PMID:24859006 "Unexpectedly, Par3L, but not Par3, binds to the tumour suppressor protein Lkb1 and inhibits its kinase activity."] Binding maps to a Par3L-specific PDZ2-PDZ3 linker, and a swap mutant loses LKB1 binding and fails to rescue. Wild-type Par3L lowers phospho-AMPK in HEK293T cells. The authors state that a role of Par3L in cell polarity had not been addressed.

### Evolutionary grounding
- QuickGO, 2026-10-21: Current GO_Central IBA rows for human PARD3B (Q8TEW8), human PARD3 (Q8TEW0) and mouse Pard3b (Q9CSB4) come from PANTHER node PTN001046835 and do not include GO:0051660 (establishment of centrosome localization). The ten IBA terms are GO:0035091, GO:0000226, GO:0007155, GO:0008104, GO:0030010, GO:0045197, GO:0005912, GO:0005938, GO:0016324 and GO:0043296; their donors are Bazooka (FBgn0000163), C. elegans par-3, mouse/rat Pard3 and human PARD3. The only current IBA carriers of GO:0051660 are CEP83 orthologs (PTN000570990). The donkey TreeGrafter row for GO:0051660 (node PTN001444301) therefore has no current PAINT counterpart.
- New analysis [file:EQUAS/PARD3B/PARD3B-bioinformatics/RESULTS-rereview.md]: the human PARD3B 469-497 linker between PDZ2 and PDZ3 is 26/29 identical in donkey and 25/29 in mouse, but only 15/29 in human PARD3. The LKB1-binding determinant is therefore an SF4 feature that the donkey protein retains.

### Decision changes vs previous review
- GO:0030010 establishment of cell polarity: ACCEPT -> KEEP_AS_NON_CORE. PARD3B lacks aPKC/PAR6 binding and no polarity function has been shown.
- GO:0045197 epithelial apical/basal polarity: ACCEPT -> MARK_AS_OVER_ANNOTATED. The donors act through PAR6-aPKC, which PARD3B cannot bind.
- GO:0000226 microtubule cytoskeleton organization: KEEP_AS_NON_CORE -> MARK_AS_OVER_ANNOTATED, for the same paralog-divergence reason.
- GO:0008104 intracellular protein localization: KEEP_AS_NON_CORE -> MARK_AS_OVER_ANNOTATED. The previous support (PARD6B binding) is contradicted.
- GO:0051660 establishment of centrosome localization: KEEP_AS_NON_CORE -> REMOVE. It is absent from current PAINT for the whole family branch.
- NEW GO:0004860 protein kinase inhibitor activity (ISS from mouse PMID:24859006; SF4 membership plus conserved linker) is now the core MF.
- Unchanged: bicellular tight junction ACCEPT (now cited to PMID:12459187 and PMID:12234671); cell junction and apical junction complex TOO_GENERAL; adherens junction, cell cortex, apical plasma membrane, endomembrane system and protein-containing complex KEEP_AS_NON_CORE; cell adhesion MARK_AS_OVER_ANNOTATED; phosphatidylinositol binding UNDECIDED.
- Description rewritten. It no longer states PARD6B binding as established, and it adds the LKB1 function.

### Relative
- The next relative is human PARD3B (Q8TEW8), the same SF4 subfamily ortholog with the reviewed Swiss-Prot entry and the human interaction and localization data. Mouse Pard3b (Q9CSB4) carries the LKB1 functional data. Neither has a review in the repo.

### Modules
- No module in modules/ contains PARD3B. modules/dmel_epithelial_polarity_complexes.yaml covers the Drosophila Bazooka/PAR complex (PAR3 family, SF17), which is related only at family level.

## 2026-10-23 — PR #5309 review follow-up

Dropped the two remaining `ortholog_experimental_goa.txt` quotes (GO:0030054 cell junction and
GO:0032991 protein-containing complex). A GO annotation listing is not evidence for an annotation; both
rows keep their primary support (PMID:12459187, PMID:16458856). The listing reference is downgraded to
relevance LOW and noted as provenance only.
