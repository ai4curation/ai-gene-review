# CGRRF1 (Q99675) review notes

## Identity
- Gene: CGRRF1 (cell growth regulator with RING finger domain protein 1); synonyms CGR19, RNF197; HGNC:15528; UniProt Q99675; 332 aa.
- Domain architecture: N-terminal hydrophobic/transmembrane region (sequence MAAVFLVTLY...GLVLGWFGWDV, ~residues 1-50, multiple hydrophobic stretches consistent with membrane anchoring) and a C-terminal cytosolic RING-type zinc finger (FT ZN_FING 274..309, RING-type; PROSITE PS50089; CDD cd16787 mRING-HC-C3HC5_CGRF1). NMR structure of the RING domain solved (PDB 2EA5, residues 264-318) [file:human/CGRRF1/CGRRF1-uniprot.txt "PDB; 2EA5; NMR; -; A=264-318"].

## Origin / discovery
- Originally isolated as "CGR19", a p53-induced cell growth regulatory gene, in differential RT-PCR of rat embryo fibroblasts with a temperature-sensitive p53 allele. Predicted protein contains a RING-finger domain. CGR19 (and CGR11) "are able to inhibit the growth of several cell lines" [PMID:8968090 "Both CGR11 and CGR19 are able to inhibit the growth of several cell lines."]. This is the basis for the cell-growth/proliferation annotations. Note: assay is overexpression-based growth inhibition; no mechanism established.

## ER membrane E3 ligase / ERAD context
- CGRRF1 was one of 37 human RING-finger + transmembrane proteins computationally selected as candidate ERAD E3 ligases [PMID:27485036 "we searched human protein databases (RefSeq and Ensembl)... (1) having a RING-finger motif (C3H2C3 or C3HC4) and (2) having transmembrane domain(s). We found a total of 37 putative RING-type E3 genes"].
- Its expression is significantly up-regulated by ER stress (thapsigargin, tunicamycin) and induced by ATF6 (N-terminal domain) [PMID:27485036 "The expression of four genes RNFT1, RNF185, CGRRF1 and RNF19B was significantly elevated by both Tg and Tm"; "ATF6 (N-terminal domain) significantly upregulated CGRRF1 and RNF19B expression"]. Peak induction late (~48 h), suggesting indirect UPR pathway.
- Subcellular localization: V5-CGRRF1 partially colocalized with PDI (ER chaperone) in COS-1 cells, indicating ER localization [PMID:27485036 "RNFT1, RNF185, CGRRF1 and RNF19B partially colocalised with endogenous PDI, an ER-resident chaperone, indicating their localisation to the ER"]. UniProt SUBCELLULAR LOCATION lists Nucleus (ECO:0000269|PubMed:22361696) and Endoplasmic reticulum (ECO:0000269|PubMed:27485036).

## IMPORTANT caveat on E3 activity (negative result)
- In the same study, in vitro autoubiquitination assays (E1=UBE1, E2=UbcH5c/UBE2D3, ubiquitin) showed CGRRF1 did NOT exhibit autoubiquitination/E3 activity, unlike RNFT1/RNF185/RNF19B [PMID:27485036 "the smears of WT-CGRRF1 remained at basal levels compared with those in its mutants, indicating that CGRRF1 does not have E3 activity, at least in an in vitro system using the UbcH5c E2 enzyme"].
- CGRRF1 also did NOT confer ER stress resistance [PMID:27485036 "Consistent with the lack of E3 activity, WT-CGRRF1 had no resistance to ER stress."].
- Interpretation: CGRRF1 has all the structural hallmarks of an ER-membrane RING E3 ligase (RING domain + TM anchor + ER localization + UPR induction), and is strongly predicted to be one, but direct biochemical demonstration of ubiquitin ligase activity is lacking; the one published in vitro test (with a single E2, UbcH5c) was negative. The "ubiquitin protein ligase activity" inference therefore rests on RING-domain homology/structure, not on a positive functional assay. No specific physiological substrate has been demonstrated. Accordingly, MF E3 ligase activity is best treated as supported-by-homology but not core-experimentally-proven; I do not ACCEPT it as a curated experimental function here because it is not present in the existing GOA annotation set and the only direct test was negative.

## Protein interactions
- The only MF annotation in GOA is GO:0005515 protein binding (IPI), derived entirely from the HuRI high-throughput binary interactome (Y2H) screen [PMID:32296183 "a human 'all-by-all' reference interactome map... HuRI"]. UniProt INTERACTION lists ~30 partners, predominantly other multi-pass / single-pass membrane or ER/Golgi proteins (e.g., BET1, CYB5B, MARCHF5, RHBDD1, ZFPL1, YIPF6, JAGN1, SCAMP4). These are systematic Y2H hits, not validated functional partners, and are consistent with membrane-protein co-localization rather than a defined molecular function. Bare "protein binding" is uninformative.

## Tissue expression
- Ubiquitously expressed; high in testis and cerebellum [PMID:27485036 "Ubiquitously expressed with high expression in testis and the cerebellum"]. HPA: low tissue specificity.

## Summary of curation decisions
- MF GO:0005515 protein binding (IPI, HuRI) -> MARK_AS_OVER_ANNOTATED (uninformative, HT only).
- CC GO:0005783 endoplasmic reticulum (IDA, PMID:27485036) -> ACCEPT (could be refined to GO:0005789 ER membrane given TM anchor, but IDA supports the parent ER directly).
- CC GO:0005783 endoplasmic reticulum (IEA, GO_REF:0000044, from UniProt SubCell) -> KEEP_AS_NON_CORE (redundant IEA of the experimentally supported ER term).
- CC GO:0005634 nucleus (IEA, from PubMed:22361696 antibody localization) -> KEEP_AS_NON_CORE (a TM-anchored ER membrane protein in the nucleus is biologically questionable; antibody-based, possibly the nucleoplasm signal; keep but non-core).
- CC GO:0005654 nucleoplasm (IDA, HPA) -> KEEP_AS_NON_CORE (HPA immunofluorescence; not consistent with primary ER-membrane function but retained as observed).
- BP GO:0030308 negative regulation of cell growth (IBA) -> KEEP_AS_NON_CORE (phylogenetic transfer rooted in the original p53/overexpression growth-inhibition phenotype; not the molecular core function).
- BP GO:0008285 negative regulation of cell population proliferation (TAS, PMID:8968090) -> KEEP_AS_NON_CORE (original overexpression phenotype; descriptive, not mechanistic core).

## Proposed (not in GOA, supported by structure/homology, not added as accepted annotations)
- MF GO:0061630 ubiquitin protein ligase activity and BP GO:0036503 ERAD pathway are strongly suggested by the RING+TM+ER+UPR profile but lack positive functional evidence (the one in vitro test was negative). Raised in suggested_experiments rather than asserted.
