# nbs (Drosophila NBN/nibrin) review notes

## Literature journal
- Nuclear import of MR: [PMID:16648644 "Rad50 accumulates in the nuclei of wild-type cells but not in those of nbs cells, indicating that Nbs mediates transport of the Mre11/Rad50 complex in the nucleus"]; [PMID:33556205 "Here, we show that Nbs interacts with Mre11 and transports the Mre11-Rad50 complex from the cytoplasm to the nucleus."]
- Telomeres: [PMID:16648644 "This suggests that Nbs and the Mre11/Rad50 complex play partially independent roles in telomere protection and that Nbs functions in both ATR- and ATM-controlled telomere protection pathways."]; HOAP interaction [PMID:33556205 "we reveal that Nbs interacts with the N-terminal region of HOAP"].
- DNA damage responses: [PMID:16710445 "We demonstrate that Drosophila nbs is required for atm- and atr-dependent DNA damage responses including DNA repair."]; apoptosis [PMID:16710445 "Apoptosis in nbs mutant discs is strongly suppressed by mutations in p53 (K, Q, and W) and mnk (L, R, and X)."]
- HR and checkpoint: [PMID:19395318 "We found that either reducing levels of NBS or removing the N-terminal forkhead-associated (FHA) domain caused a defect in gap repair by HR."]; [PMID:19395318 "Reducing the level of NBS also resulted in a profound defect in the DNA damage-dependent cell cycle checkpoint."]

## Curation decisions
- Core: adaptor/regulatory subunit of MRN (MF approximated by GO:0030674) in G2 checkpoint signaling and SDSA/HR repair; telomere protection.
- PML body (IEA, from human NBN location) removed: Drosophila has no PML ortholog.
- Damaged DNA binding (IBA) marked over-annotated; apoptosis kept as non-core.
- Review follow-up: the MRN telomere role is curated as GO:0016233 telomere capping across mre11, rad50 and nbs (IMP GO:0000723 rows MODIFY to capping; core_functions use capping), since the fly evidence is telomere fusion and loss of HOAP/HP1 at chromosome ends in a telomerase-free organism [PMID:15296753 "This suggests that the MRN complex protects Drosophila telomeres by facilitating recruitment of HOAP and HP1 at chromosome ends."].

## Falcon deep research (added after the initial review)
- The report (`nbs-deep-research-falcon.md`) agrees with the curated picture: Nbs is a nuclear, non-catalytic MRN adaptor [file:DROME/nbs/nbs-deep-research-falcon.md "Nbs is a **nuclear DNA-damage-response and chromatin-associated adaptor**, not an enzyme or transporter."], and nuclease activity belongs to the complex [file:DROME/nbs/nbs-deep-research-falcon.md "nuclease activity should not be assigned to Nbs itself"].
- Telomeres: it supports end protection without Nbs being a stable telomeric cap [file:DROME/nbs/nbs-deep-research-falcon.md "A model in which Nbs enables a chromatin environment permissive for capping is consequently better established than a model requiring Nbs to be a stable physical cap at every chromosome end."]. It also notes that Gao et al. 2009 did not detect an MRN-HOAP co-IP, whereas PMID:33556205 reports the Nbs-HOAP interaction; the core function keeps the HOAP interaction (from the primary paper), and this tension is worth expert attention. The telomere capping (GO:0016233) refinement is consistent with the report.
- Newer findings (HP1a stabilisation, Bosso 2019; ATM-Nbs-dependent HOAP hyperphosphorylation, On et al. 2023; neuroblast and hemocyte RNAi phenotypes, 2023-2024) are not in GOA and are pathway-level or indirect; no annotation decision was changed.
