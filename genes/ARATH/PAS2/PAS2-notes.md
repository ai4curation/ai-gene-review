# PAS2 (PASTICCINO2/PEPINO; At5g10480; Q8VZB2) review notes

## Identity and function
- ER 3-hydroxyacyl-CoA dehydratase of the VLCFA elongase, PHS1/HACD ortholog [PMID:18799749 "the plant 3-hydroxy-acyl-CoA dehydratase PASTICCINO2 is an essential and limiting enzyme in VLCFA synthesis"].
- Reciprocal complementation with yeast PHS1; pas2-1 accumulates 3-hydroxyacyl-CoAs [PMID:18799749 "the defective elongation cycle resulted in the accumulation of 3-hydroxy-acyl-CoA intermediates"].
- ER localization; BiFC with CER10/ECR [PMID:18799749 "PAS2 was specifically associated in the endoplasmic reticulum with the enoyl-CoA reductase CER10"].
- Null alleles embryo lethal; pas2-1 has reduced VLCFAs in TAG, wax, sphingolipids.
- Historical PTP-like classification: mutated PTP site, no phosphatase activity [PMID:16698944 "The recombinant PAS2 had no phosphatase activity"]; dehydratase catalytic residues are not in the PTP motif [PMID:18799749].
- CDKA;1 "antiphosphatase" model and cytosolic/nuclear localization come from overexpressed 35S-PAS2:GFP [PMID:16698944]; later PHS1 complementation shows developmental defects are due to defective dehydratase [PMID:18799749 "PHS1 complementation indicates that pas2 developmental defects are most likely caused by a defective dehydratase activity"].
- Deep research (file:ARATH/PAS2/PAS2-deep-research-falcon.md) also mentions a Golgi pool (Zhu et al. 2020) linked to cellulose synthase complexes - not in GOA, not reviewed further (paper not cached).

## Decisions
- REMOVE: protein tyrosine phosphatase activity (ISS; contradicted), protein binding (IPI), mitochondrion (ISM).
- UNDECIDED: nucleus (IDA and IEA) - single overexpression GFP study vs integral ER membrane protein; needs native-promoter validation.
- MARK_AS_OVER_ANNOTATED: cytosol (IDA), negative regulation of developmental growth (IMP, overexpression phenotype).
- KEEP_AS_NON_CORE: cell differentiation (IMP), regulation of cell division (IMP).
- ACCEPT: dehydratase activities, elongase complex (IPI), ER/ER membrane, cytoplasm (general), FA elongation, VLCFA biosynthesis, sphingolipid biosynthesis (IBA), FA biosynthesis (IEA).

## 2026-10-15 journal: nucleus rows resolved (PR #5026 follow-up)

Supersedes the "UNDECIDED: nucleus (IDA and IEA)" line above.

- GO:0005634 nucleus IDA (PMID:16698944) and the matching IEA (UniProt subcellular location derived from the same study) are both MARK_AS_OVER_ANNOTATED. The cached full text shows the nuclear signal came from a 35S-driven C-terminal GFP fusion in lines selected for high GFP [PMID:16698944 "High GFP-producing plants were retained for further analysis"], with perinuclear accumulation in dividing cells consistent with nuclear envelope/ER. PAS2 is a multi-pass ER-membrane 3-hydroxyacyl-CoA dehydratase; ER membrane is the supported location. Not removed, because nuclear GFP signal was genuinely recorded.
