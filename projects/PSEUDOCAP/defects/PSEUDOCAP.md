# Source-record defects for PSEUDOCAP

114 open defect(s), generated from `source_defects` blocks in this repository's reviews. Do not edit by hand.

## 1. WRONG_EVIDENCE_CODE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I5N4 part_of GO:0098046 type V protein secretion system complex (IMP, PMID:25009238)
- **Field:** Evidence_Code
- **Change:** check ECO:0000315 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA0692/PA0692-ai-review.yaml`

GO:0098046 type V protein secretion system complex for PA0692 (PdtB, Q9I5N4) is annotated IMP to PMID:25009238. The abstract reports a mutant export defect (PdtA transport depends on PdtB), which supports the process GO:0046819 but not complex membership or location. If the full text localizes PdtB (e.g. outer-membrane fractionation), change the evidence to IDA; otherwise use IC from the IMP process row or ISS from TpsB homologs. This row is the sole seed of the PAINT IBD at PTN002160772 (25 leaf IBAs); the IBD conclusion is sound by family, so only the seed evidence needs attention.

> the transport of PdtA is strictly dependent on the production of PdtB
> — PMID:25009238

## 2. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I551 involved_in GO:0001896 autolysis (IMP, PMID:26100878)
- **Change:** GO:0001896 → GO:0043069 (negative regulation of programmed cell death)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA0906/PA0906-ai-review.yaml`

GO:0001896 autolysis (IMP, PMID:26100878) for PA0906 (alpR, Q9I551) records lysis after AlpR depletion or cleavage. AlpR is the repressor of the alp lysis genes, which execute lysis; it is a negative regulator of the process, not a participant. Repoint to GO:0043069 negative regulation of programmed cell death (or to a regulation-of-autolysis term if GO adds one).

> Cleavage of AlpR triggers a cell lysis program through de-repression of the alpA gene
> — PMID:26100878

## 3. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I537 involved_in GO:0055091 phospholipid homeostasis (IDA, PMID:26261323)
- **Change:** GO:0055091 → GO:0008654 (phospholipid biosynthetic process)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA0920/PA0920-ai-review.yaml`

GO:0055091 phospholipid homeostasis for PA0920 (Q9I537) is annotated IDA to PMID:26261323. That paper reports the crystal structure and in vitro substrate recognition of the A-PGS catalytic domain; it does not assay homeostasis, and the gene performs a biosynthetic step (alanylation of PG). Repoint to GO:0008654 phospholipid biosynthetic process; PMID:19087229 (deletion abolishes A-PG, expression in E. coli confers it) is stronger support for the process. This row is the sole seed of the PAINT IBD at PTN002162750.

> The P. aeruginosa deletion mutant DeltaPA0920 failed to synthesize A-PG.
> — PMID:19087229

## 4. WRONG_QUALIFIER (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I4S0 enables GO:0015385 sodium:proton antiporter activity (IMP, PMID:16030218)
- **Field:** Qualifier
- **Change:** enables → contributes_to
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA1054/PA1054-ai-review.yaml`

PA1054 (ShaAB) is the large subunit of the six-subunit Sha/Mrp Na+/H+ antiporter. The IMP evidence (PMID:16030218) is sound: the cluster lacking PA1054 does not restore antiport. But no Mrp antiporter shows activity with MrpA alone, and antiport requires the hetero-oligomeric complex, so the subunit contributes to GO:0015385 rather than enabling it alone.

> In previous studies, none of the Mrp antiporters exhibited antiport activity with MrpA or MrpD alone.
> — PMID:29218041

## 5. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I4R9 enables GO:0015385 sodium:proton antiporter activity (IMP, PMID:16030218)
- **Field:** Evidence_Code
- **Change:** check ECO:0000315 (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/PSEAE/PA1055/PA1055-ai-review.yaml`

enables GO:0015385 sodium:proton antiporter activity (IMP) on PA1055 cites Kosono et al. 2005 (PMID:16030218). The abstract reports a disruption of PA1054 only, and complementation of E. coli TO114 by the whole PA1054-PA1059 cluster. No PA1055 mutant phenotype is reported, so IMP does not apply to PA1055. If the antiport was measured in membranes of TO114 carrying the cluster, IDA (as contributes_to) would fit; if only growth complementation, IGI. Please check the full text. This row is the sole seed of the PAINT IBD at PTN002160376 (24 leaf IBAs).

> We disrupted PA1054 (a shaA homologue gene) and determined its effect on Na+ tolerance during growth, Na+ efflux, and pathogenicity in mice.
> — PMID:16030218

## 6. WRONG_QUALIFIER (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I4R9 enables GO:0015385 sodium:proton antiporter activity (IMP, PMID:16030218)
- **Field:** Qualifier
- **Change:** enables → contributes_to
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA1055/PA1055-ai-review.yaml`

PA1055 (ShaC) is one of six subunits of the Sha/Mrp Na+/H+ antiporter. Mrp antiport requires the hetero-oligomeric complex of all subunits, so the subunit contributes to GO:0015385 rather than enabling it alone.

> Antiport activity requires hetero-oligomeric complexes of all six or seven hydrophobic Mrp proteins (MrpA-MrpG).
> — PMID:20624916

## 7. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I4R9 involved_in GO:0035725 sodium ion transmembrane transport (IMP, PMID:16030218)
- **Field:** Evidence_Code
- **Change:** check ECO:0000315 (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/PSEAE/PA1055/PA1055-ai-review.yaml`

involved_in GO:0035725 sodium ion transmembrane transport (IMP) on PA1055 cites Kosono et al. 2005 (PMID:16030218), which reports a mutant of PA1054 only (reduced Na+ efflux) and complementation of E. coli TO114 by the whole PA1054-PA1059 cluster. No PA1055 mutant phenotype is reported. Please check the evidence code (IGI or IDA for the cluster-level data). The process itself is appropriate for this subunit.

> Disruption of PA1054 resulted in severe Na+ sensitivity during growth and decreased Na+ efflux activity.
> — PMID:16030218

## 8. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I4R8 enables GO:0015385 sodium:proton antiporter activity (IMP, PMID:16030218)
- **Field:** Evidence_Code
- **Change:** check ECO:0000315 (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/PSEAE/PA1056/PA1056-ai-review.yaml`

enables GO:0015385 sodium:proton antiporter activity (IMP) on PA1056 cites Kosono et al. 2005 (PMID:16030218). The abstract reports a disruption of PA1054 only, and complementation of E. coli TO114 by the whole PA1054-PA1059 cluster. No PA1056 mutant phenotype is reported, so IMP does not apply to PA1056. If the antiport was measured in membranes of TO114 carrying the cluster, IDA (as contributes_to) would fit; if only growth complementation, IGI. Please check the full text. This row is one of two seeds of the PAINT IBD at PTN001865541 (16 leaf IBAs).

> We disrupted PA1054 (a shaA homologue gene) and determined its effect on Na+ tolerance during growth, Na+ efflux, and pathogenicity in mice.
> — PMID:16030218

## 9. WRONG_QUALIFIER (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I4R8 enables GO:0015385 sodium:proton antiporter activity (IMP, PMID:16030218)
- **Field:** Qualifier
- **Change:** enables → contributes_to
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA1056/PA1056-ai-review.yaml`

PA1056 (ShaD) is one of six subunits of the Sha/Mrp Na+/H+ antiporter. No Mrp antiporter shows antiport with MrpD alone, so the subunit contributes to GO:0015385 rather than enabling it alone.

> In previous studies, none of the Mrp antiporters exhibited antiport activity with MrpA or MrpD alone.
> — PMID:29218041

## 10. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I4R8 involved_in GO:0035725 sodium ion transmembrane transport (IMP, PMID:16030218)
- **Field:** Evidence_Code
- **Change:** check ECO:0000315 (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/PSEAE/PA1056/PA1056-ai-review.yaml`

involved_in GO:0035725 sodium ion transmembrane transport (IMP) on PA1056 cites Kosono et al. 2005 (PMID:16030218), which reports a mutant of PA1054 only (reduced Na+ efflux) and complementation of E. coli TO114 by the whole PA1054-PA1059 cluster. No PA1056 mutant phenotype is reported. Please check the evidence code (IGI or IDA for the cluster-level data). The process itself is appropriate for this subunit.

> Disruption of PA1054 resulted in severe Na+ sensitivity during growth and decreased Na+ efflux activity.
> — PMID:16030218

## 11. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I4R7 enables GO:0015385 sodium:proton antiporter activity (IMP, PMID:16030218)
- **Field:** Evidence_Code
- **Change:** check ECO:0000315 (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/PSEAE/PA1057/PA1057-ai-review.yaml`

enables GO:0015385 sodium:proton antiporter activity (IMP) on PA1057 cites Kosono et al. 2005 (PMID:16030218). The abstract reports a disruption of PA1054 only, and complementation of E. coli TO114 by the whole PA1054-PA1059 cluster. No PA1057 mutant phenotype is reported, so IMP does not apply to PA1057. If the antiport was measured in membranes of TO114 carrying the cluster, IDA (as contributes_to) would fit; if only growth complementation, IGI. Please check the full text. This row is the sole seed of the PAINT IBD at PTN002160407 (20 leaf IBAs).

> We disrupted PA1054 (a shaA homologue gene) and determined its effect on Na+ tolerance during growth, Na+ efflux, and pathogenicity in mice.
> — PMID:16030218

## 12. WRONG_QUALIFIER (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I4R7 enables GO:0015385 sodium:proton antiporter activity (IMP, PMID:16030218)
- **Field:** Qualifier
- **Change:** enables → contributes_to
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA1057/PA1057-ai-review.yaml`

PA1057 (ShaE) is one of six subunits of the Sha/Mrp Na+/H+ antiporter. Mrp antiport requires the hetero-oligomeric complex, and MrpE acts in complex assembly, so the subunit contributes to GO:0015385 rather than enabling it alone.

> The results extended indications that MrpE is required for normal membrane levels of other Mrp proteins and for complex formation.
> — PMID:20624916

## 13. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I4R7 involved_in GO:0035725 sodium ion transmembrane transport (IMP, PMID:16030218)
- **Field:** Evidence_Code
- **Change:** check ECO:0000315 (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/PSEAE/PA1057/PA1057-ai-review.yaml`

involved_in GO:0035725 sodium ion transmembrane transport (IMP) on PA1057 cites Kosono et al. 2005 (PMID:16030218), which reports a mutant of PA1054 only (reduced Na+ efflux) and complementation of E. coli TO114 by the whole PA1054-PA1059 cluster. No PA1057 mutant phenotype is reported. Please check the evidence code (IGI or IDA for the cluster-level data). The process itself is appropriate for this subunit.

> Disruption of PA1054 resulted in severe Na+ sensitivity during growth and decreased Na+ efflux activity.
> — PMID:16030218

## 14. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I4R6 enables GO:0015385 sodium:proton antiporter activity (IMP, PMID:16030218)
- **Field:** Evidence_Code
- **Change:** check ECO:0000315 (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/PSEAE/PA1058/PA1058-ai-review.yaml`

enables GO:0015385 sodium:proton antiporter activity (IMP) on PA1058 cites Kosono et al. 2005 (PMID:16030218). The abstract reports a disruption of PA1054 only, and complementation of E. coli TO114 by the whole PA1054-PA1059 cluster. No PA1058 mutant phenotype is reported, so IMP does not apply to PA1058. If the antiport was measured in membranes of TO114 carrying the cluster, IDA (as contributes_to) would fit; if only growth complementation, IGI. Please check the full text. This row is the sole seed of the PAINT IBD at PTN002162906 (19 GO_Central leaf IBAs).

> We disrupted PA1054 (a shaA homologue gene) and determined its effect on Na+ tolerance during growth, Na+ efflux, and pathogenicity in mice.
> — PMID:16030218

## 15. WRONG_QUALIFIER (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I4R6 enables GO:0015385 sodium:proton antiporter activity (IMP, PMID:16030218)
- **Field:** Qualifier
- **Change:** enables → contributes_to
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA1058/PA1058-ai-review.yaml`

PA1058 (ShaF) is one of six subunits of the Sha/Mrp Na+/H+ antiporter. Mrp antiport requires the hetero-oligomeric complex of all subunits, so the subunit contributes to GO:0015385 rather than enabling it alone.

> Antiport activity requires hetero-oligomeric complexes of all six or seven hydrophobic Mrp proteins (MrpA-MrpG).
> — PMID:20624916

## 16. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I4R6 involved_in GO:0035725 sodium ion transmembrane transport (IMP, PMID:16030218)
- **Field:** Evidence_Code
- **Change:** check ECO:0000315 (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/PSEAE/PA1058/PA1058-ai-review.yaml`

involved_in GO:0035725 sodium ion transmembrane transport (IMP) on PA1058 cites Kosono et al. 2005 (PMID:16030218), which reports a mutant of PA1054 only (reduced Na+ efflux) and complementation of E. coli TO114 by the whole PA1054-PA1059 cluster. No PA1058 mutant phenotype is reported. Please check the evidence code (IGI or IDA for the cluster-level data). The process itself is appropriate for this subunit.

> Disruption of PA1054 resulted in severe Na+ sensitivity during growth and decreased Na+ efflux activity.
> — PMID:16030218

## 17. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I4R5 enables GO:0015385 sodium:proton antiporter activity (IMP, PMID:16030218)
- **Field:** Evidence_Code
- **Change:** check ECO:0000315 (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/PSEAE/PA1059/PA1059-ai-review.yaml`

enables GO:0015385 sodium:proton antiporter activity (IMP) on PA1059 cites Kosono et al. 2005 (PMID:16030218). The abstract reports a disruption of PA1054 only, and complementation of E. coli TO114 by the whole PA1054-PA1059 cluster. No PA1059 mutant phenotype is reported, so IMP does not apply to PA1059. If the antiport was measured in membranes of TO114 carrying the cluster, IDA (as contributes_to) would fit; if only growth complementation, IGI. Please check the full text. This row is the sole seed of the PAINT IBD at PTN002162936 (19 GO_Central leaf IBAs).

> We disrupted PA1054 (a shaA homologue gene) and determined its effect on Na+ tolerance during growth, Na+ efflux, and pathogenicity in mice.
> — PMID:16030218

## 18. WRONG_QUALIFIER (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I4R5 enables GO:0015385 sodium:proton antiporter activity (IMP, PMID:16030218)
- **Field:** Qualifier
- **Change:** enables → contributes_to
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA1059/PA1059-ai-review.yaml`

PA1059 (ShaG) is one of six subunits of the Sha/Mrp Na+/H+ antiporter. Mrp antiport requires the hetero-oligomeric complex of all subunits, so the subunit contributes to GO:0015385 rather than enabling it alone.

> Antiport activity requires hetero-oligomeric complexes of all six or seven hydrophobic Mrp proteins (MrpA-MrpG).
> — PMID:20624916

## 19. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I4R5 involved_in GO:0035725 sodium ion transmembrane transport (IMP, PMID:16030218)
- **Field:** Evidence_Code
- **Change:** check ECO:0000315 (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/PSEAE/PA1059/PA1059-ai-review.yaml`

involved_in GO:0035725 sodium ion transmembrane transport (IMP) on PA1059 cites Kosono et al. 2005 (PMID:16030218), which reports a mutant of PA1054 only (reduced Na+ efflux) and complementation of E. coli TO114 by the whole PA1054-PA1059 cluster. No PA1059 mutant phenotype is reported. Please check the evidence code (IGI or IDA for the cluster-level data). The process itself is appropriate for this subunit.

> Disruption of PA1054 resulted in severe Na+ sensitivity during growth and decreased Na+ efflux activity.
> — PMID:16030218

## 20. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I404 involved_in GO:0006868 L-glutamine transport (IMP, PMID:18310026)
- **Field:** Evidence_Code
- **Change:** check ECO:0000315 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA1340/PA1340-ai-review.yaml`

GO:0006868 L-glutamine transport for PA1340 (Q9I404) is annotated IMP to PMID:18310026. That paper is about Pseudomonas putida KT2440: it describes the AatJMQP operon PP1071-PP1068 and mutants of the binding protein (aatJ) and ATPase (aatP). No P. aeruginosa gene and no permease was mutated, so IMP does not apply to PA1340. At most this supports an ISS/ISO from the P. putida AatM ortholog, and even there the Gln growth defect concerns the binding protein, which binds Gln only weakly. PA1340's own glutamine phenotype is already captured by the GO:1903803 IMP to PMID:18833300, so the row could be deleted or recoded. This row is the sole seed of the PAINT IBD at PTN000764525.

> The system (AatJMQP, for acidic amino acid transport) is encoded by an operon involving genes PP1071-PP1068.
> — PMID:18310026

## 21. WRONG_REFERENCE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I1J5 enables GO:0016655 oxidoreductase activity, acting on NAD(P)H, quinone or similar compound as acceptor (IDA, PMID:22304305)
- **Change:** PMID:22304305 → PMID:26621870
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA2280/PA2280-ai-review.yaml`

GO:0016655 for PA2280 (Q9I1J5, ArsH) is annotated IDA to PMID:22304305, which reports the purification and kinetics of Synechocystis sp. PCC 6803 ArsH; the abstract gives no indication that the P. aeruginosa protein was assayed. Re-cite the row to PMID:26621870 (Crescente et al. 2016), which assayed recombinant P. aeruginosa ArsH (pa2280) and found NAD(P)H quinone oxidoreductase and azoreductase activity, and consider GO:0003955. This row is the sole seed of the PAINT IBD at PTN008682975.

> Here we have expressed and purified Synechocystis ArsH and conducted an intensive biochemical study.
> — PMID:22304305

## 22. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I0Q6 enables GO:0003955 NAD(P)H dehydrogenase (quinone) activity (IMP, PMID:25085734)
- **Field:** Evidence_Code
- **Change:** ECO:0000315 → ECO:0000314
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA2580/PA2580-ai-review.yaml`

enables GO:0003955 NAD(P)H dehydrogenase (quinone) activity on PA2580 cites Green et al. 2014, whose evidence for the activity is in vitro assays of the purified enzyme. That is IDA; no PA2580 mutant is reported, and the overexpression experiments address H2O2 tolerance, not the activity. The row is a seed of the PTN002922793 IBD.

> In in vitro assays, each enzyme was shown to reduce quinone substrates with only minimal semiquinone formation.
> — PMID:25085734

## 23. WRONG_TERM (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HXU3 involved_in GO:0080164 regulation of nitric oxide metabolic process (IMP, PMID:18043907)
- **Field:** GO_ID
- **Change:** check GO:0080164 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/PA3697/PA3697-ai-review.yaml`

involved_in GO:0080164 regulation of nitric oxide metabolic process (IMP, PMID:18043907) on PA3697. The abstract reports that PA3697 mutants lose nitrate- and nitrite-induced fhp promoter activity; no NO measurement is described. Please check whether the full text measures NO consumption or NO levels in the mutant. If it does not, the row overstates the evidence: the phenotype is reduced fhp expression, and the mechanism (direct promoter binding or an indirect effect) is unknown. This row is the sole seed of the PANTHER IBD at PTN002422332, which spreads the claim to about 175 proteins.

> Both PA0779 and PA3697 were found to be essential for NO3(-) and NO2(-) induced Pfhp activity under aerobic and low-oxygen conditions
> — PMID:18043907

## 24. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HXC2 enables GO:0031459 ABC-type glycine betaine transporter activity (IDA, PMID:17660277)
- **Field:** Evidence_Code
- **Change:** check ECO:0000314 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA3891/PA3891-ai-review.yaml`

GO:0031459 ABC-type glycine betaine transporter activity for PA3891 (Q9HXC2) is annotated IDA to PMID:17660277 (Chen and Beattie 2007). In that paper PA3891 was only recovered as a PAO1 genomic clone that restored growth of a P. syringae DC3000 opuCA-deficient mutant on 0.5 M NaCl with betaine or choline. No transport, binding or ATPase assay was done with PA3891, and glycine betaine specificity was shown for the DC3000 ortholog (Q87WH5). IGI (functional complementation) or ISS with UniProtKB:Q87WH5 would be accurate. This row is the sole seed of the PAINT IBD at PTN001953060 (about 23 leaf IBAs), so coordinate any change with PAINT re-seeding.

> the transformants were plated on MinA media containing 0.5 M NaCl and either glycine betaine or choline (2 mM)
> — PMID:17660277

## 25. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HXC2 part_of GO:0043190 ATP-binding cassette (ABC) transporter complex (IDA, PMID:17660277)
- **Field:** Evidence_Code
- **Change:** check ECO:0000314 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA3891/PA3891-ai-review.yaml`

GO:0043190 ATP-binding cassette (ABC) transporter complex for PA3891 (Q9HXC2) is annotated IDA to PMID:17660277. The paper does not purify, cross-link or co-localise any PA3891 complex. It only shows that a PAO1 genomic clone carrying PA3891 complements a P. syringae opuCA-deficient mutant for osmoprotected growth. The complex membership is a sequence and operon inference (ISS/IC). This row seeds the PAINT plasma membrane IBD at PTN001953445 (about 31 leaf IBAs), so re-coding it affects that node.

## 26. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HVR8 enables GO:0071916 dipeptide transmembrane transporter activity (IDA, PMID:25338022)
- **Field:** Evidence_Code
- **Change:** check ECO:0000314 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA4503/PA4503-ai-review.yaml`

GO:0071916 for PA4503 (DppB, Q9HVR8) is annotated IDA to PMID:25338022. The paper's evidence is a deletion of the whole dppBCDF operon in strain PA14, scored by Biolog respiration on dipeptides and by phaseolotoxin sensitivity. No direct transport, binding or ATPase assay was done with the protein, so IMP is the correct code. The claim itself is sound. This row is the sole seed of the PAINT IBD at PTN000765601 and one of four seeds at PTN002455499. The same applies to the matching PA4504 (DppC) row.

> Numerous dipeptides could not be used as N-source by the mutant lacking the DppBCDF transporter system
> — PMID:25338022

## 27. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HVR7 enables GO:0071916 dipeptide transmembrane transporter activity (IDA, PMID:25338022)
- **Field:** Evidence_Code
- **Change:** check ECO:0000314 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA4504/PA4504-ai-review.yaml`

GO:0071916 for PA4504 (DppC, Q9HVR7) is annotated IDA to PMID:25338022. The paper's evidence is a deletion of the whole dppBCDF operon in strain PA14, scored by Biolog respiration on dipeptides and by phaseolotoxin sensitivity. No direct transport, binding or ATPase assay was done with the protein, so IMP is the correct code. The claim itself is sound. This row is the sole seed of the PAINT IBD at PTN000766696 and one of five seeds at PTN000765620. The same applies to the matching PA4503 (DppB) row.

> Numerous dipeptides could not be used as N-source by the mutant lacking the DppBCDF transporter system
> — PMID:25338022

## 28. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HVR6 enables GO:0071916 dipeptide transmembrane transporter activity (IDA, PMID:25338022)
- **Field:** Evidence_Code
- **Change:** check ECO:0000314 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA4505/PA4505-ai-review.yaml`

GO:0071916 for PA4505 (DppD, Q9HVR6) is annotated IDA to PMID:25338022. The paper's evidence is a deletion of the whole dppBCDF operon in strain PA14, scored by Biolog respiration on dipeptides and by phaseolotoxin sensitivity. No direct transport, binding or ATPase assay was done, so IMP is the correct code. The claim itself is sound. This row is the sole seed of the PAINT IBD at PTN000656114 and one of four seeds at PTN000656054. The same applies to the PA4503 and PA4504 rows.

> Numerous dipeptides could not be used as N-source by the mutant lacking the DppBCDF transporter system
> — PMID:25338022

## 29. WRONG_QUALIFIER (SUSPECTED, NOT_REPORTED)

- **Record:** PMID:20088866
- **Subject:** UniProtKB:Q9HVG7
- **Change:** check involved_in (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA4624/PA4624-ai-review.yaml`

GO:0044010 single-species biofilm formation for PA4624 (CdrB, Q9HVG7) is annotated IMP involved_in to PMID:20088866. The paper made cdrA deletions only; the cdrB evidence is that cdrAB co-overexpression increases biofilm, with cdrB required for secretion of the CdrA adhesin. CdrB therefore acts upstream of biofilm formation by exporting CdrA, rather than taking part in matrix formation. Consider acts_upstream_of_or_within, or removing the row from CdrB and keeping it on CdrA (PA4625).

> This is consistent with the data presented in Fig. 3, suggesting that CdrB is required for CdrA secretion.
> — PMID:20088866

## 30. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HTY2 involved_in GO:0044010 single-species biofilm formation (IMP, PMID:17158671)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0044010
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA5208/PA5208-ai-review.yaml`

involved_in GO:0044010 single-species biofilm formation (IMP) on PA5208 rests on a crystal-violet biofilm reduction in a single mini-Tn5 insertion mutant from a swarming screen (Overhage et al. 2007) that also has a growth defect. This records a mutant phenotype, not participation of this PhoU-like protein in biofilm formation.

> and a PA5208 mutant that had a slight growth defect
> — PMID:17158671

## 31. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HTY2 involved_in GO:0071978 bacterial-type flagellum-dependent swarming motility (IMP, PMID:17158671)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0071978
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA5208/PA5208-ai-review.yaml`

involved_in GO:0071978 (IMP) on PA5208 rests on a single mini-Tn5 insertion mutant from a swarming screen (Overhage et al. 2007) that also has a growth defect. PA5208 is a PhoU-like UPF0111 protein with no flagellar function; the row records an indirect mutant phenotype and is the sole seed of the PTN002194937 swarming IBD (5 leaf IBAs, including non-flagellated Haemophilus and Coxiella).

> and a PA5208 mutant that had a slight growth defect
> — PMID:17158671

## 32. WRONG_GENE_PRODUCT (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HTJ9 involved_in GO:0043448 alkane catabolic process (IMP, PMID:14574114)
- **Field:** DB_Object_ID
- **Change:** check UniProtKB:Q9HTJ9 (alternatives in the explanation)
- **Likely cause:** IDENTIFIER_TRANSPOSITION
- **Recorded in:** `genes/PSEAE/PA5359/PA5359-ai-review.yaml`

PseudoCAP annotates PA5359 (UniProtKB:Q9HTJ9) with GO:0043448 alkane catabolic process, IMP, from PMID:14574114 (Smits, Witholt & van Beilen 2003). Three things suggest the locus tag may be wrong, and we ask PseudoCAP to check against the full text, which is not publicly accessible to us. (1) The paper's abstract characterises AlkB1, AlkB2, RubA1, RubA2 and RubB, which in PAO1 are PA2574, PA1525, PA5351, PA5350 and PA5349; PA5359 is not among them. (2) PA5359 is a 151-residue protein consisting of a signal peptide and two Lipoprotein_15 repeats (Pfam PF03640), with no hydroxylase, rubredoxin or flavoprotein reductase component, and UniProt gives it no function, location or family statement. (3) This is the only annotation in GOA keyed to this reference, while the five genes the paper does describe carry GO:0043448 from UniProt keyword mapping (GO_REF:0000041) rather than from the paper. PA5349 (rubB/alkT, UniProtKB:Q9HTK9) differs from PA5359 by one digit and would fit the evidence. If the row is in fact correct for PA5359, the supporting experiment would be valuable to record, since the row is the sole seed of the PAINT IBD at PTN002217427, from which 764 GOA rows descend.

> Heterologous expression showed that the two alkane hydroxylase homologs of P. aeruginosa PAO1 (AlkB1 and AlkB2) oxidize C(12)-C(16)n-alkanes, while two rubredoxin (RubA1 and RubA2) and a rubredoxin reductase (RubB) homologs can replace their P. putida GPo1 counterparts in n-octane oxidation.
> — PMID:14574114

## 33. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HTI7 enables GO:0005275 amine transmembrane transporter activity (IDA, PMID:19919675)
- **Field:** GO_ID
- **Change:** GO:0005275 → GO:0015418 (ABC-type quaternary ammonium compound transporting activity)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA5377/PA5377-ai-review.yaml`

PA5377 (CbcW permease, Q9HTI7) is annotated GO:0005275 amine transmembrane transporter activity, IDA, PMID:19919675. The substrates shown in that paper (choline, glycine betaine, L-carnitine) are quaternary ammonium compounds, which GO does not class as amines. GO:0015418 ABC-type quaternary ammonium compound transporting activity (with contributes_to for a permease subunit) is the accurate term. This row co-seeds the PAINT IBD at PTN000766131.

## 34. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HTI7 involved_in GO:0031457 glycine betaine catabolic process (IDA, PMID:19919675)
- **Field:** GO_ID
- **Change:** check GO:0031457 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA5377/PA5377-ai-review.yaml`

PA5377 (CbcW, ABC permease) is annotated involved_in GO:0031457 glycine betaine catabolic process (IDA, PMID:19919675). The evidence is that cbc transposon mutants cannot grow on betaine as sole carbon source, which reflects loss of uptake. The permease does not catalyse any catabolic step. Consider removing the row, or keeping only GO:0031460 glycine betaine transport.

## 35. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HTI7 involved_in GO:0042426 choline catabolic process (IDA, PMID:19919675)
- **Field:** GO_ID
- **Change:** check GO:0042426 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA5377/PA5377-ai-review.yaml`

PA5377 (CbcW, ABC permease) is annotated involved_in GO:0042426 choline catabolic process (IDA, PMID:19919675 and PMID:21478341). Both papers show that Cbc is needed for growth on choline as a carbon source, which reflects choline uptake. The permease does not perform any catabolic step. GO:0015871 choline transport already captures its role. Consider removing these rows.

## 36. WRONG_REFERENCE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HTI7 involved_in GO:1902603 carnitine transmembrane transport (IDA, PMID:21478341)
- **Field:** DB:Reference
- **Change:** check PMID:21478341 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA5377/PA5377-ai-review.yaml`

GO:1902603 carnitine transmembrane transport for PA5377 (Q9HTI7) cites PMID:21478341 (Malek et al. 2011), whose abstract deals only with choline uptake by CbcXWV, BetT1 and BetT3. The carnitine evidence for CbcWV is in PMID:19919675 (PA14 cbc mutants fail to grow on carnitine, and PAO1 CbcWV restores CaiX-dependent carnitine uptake) and PMID:29517479. If PMID:21478341 has no carnitine data, please re-key the row. It is the sole seed of the PAINT IBD at PTN000766131.

> These transposon mutants also failed to grow on L-carnitine (Fig. S2), suggesting that carnitine is an additional substrate for this transporter.
> — PMID:19919675

## 37. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HTB2 involved_in GO:0009243 O antigen biosynthetic process (IDA, PMID:23341552)
- **Field:** Evidence_Code
- **Change:** IDA → IMP
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA5458/PA5458-ai-review.yaml`

The PseudoCAP GO:0009243 row for PA5458 (PMID:23341552, Hao et al. 2013) uses IDA, but the paper reports no direct assay of the PA5458 protein or its activity. The evidence is the LPS phenotype of an in-frame deletion mutant, its complementation, and overexpression, analysed by SDS-PAGE and Western blot. Please change the evidence code to IMP. The GO term itself is appropriate.

> Mutation of the putative acetyltransferase-encoding gene pa5458 did not abrogate polysaccharide production
> — PMID:23341552

## 38. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:P18275 enables GO:0043858 arginine:ornithine antiporter activity (IMP, PMID:1311296)
- **Field:** Evidence_Code
- **Change:** check ECO:0000315 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/arcD/arcD-ai-review.yaml`

enables GO:0043858 (IMP) on PA5170 arcD cites Verhoogt et al. 1992, which measures arginine/ornithine exchange in membrane vesicles from E. coli carrying arcD and in proteoliposomes with reconstituted ArcD. That is a direct assay, not a mutant phenotype; IDA fits better. The annotation is correct.

> The ArcD protein was reconstituted in proteoliposomes after detergent solubilization of membrane vesicles.
> — PMID:1311296

## 39. WRONG_REFERENCE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I3N5 involved_in GO:0002049 pyoverdine biosynthetic process (IMP, PMID:16824107)
- **Field:** DB:Reference
- **Change:** PMID:16824107 → PMID:18174132 (Baert et al. 2008, Multiple phenotypic alterations caused by a c-type cytochrome maturation ccmC gene mutation in Pseudomonas aeruginosa)
- **Likely cause:** IDENTIFIER_TRANSPOSITION
- **Recorded in:** `genes/PSEAE/ccmC/ccmC-ai-review.yaml`

PMID:16824107 (Feissner et al. 2006) is an E. coli biochemical study of the CcmABC complex releasing holo-CcmE; it reports no P. aeruginosa mutant phenotypes. The pyoverdine, catalase, rhamnolipid, swarming and twitching phenotypes annotated to PA1477 are those of the P. aeruginosa ccmC mutant in PMID:18174132. All six PseudoCAP IMP rows on PA1477 dated 2019-03-11 cite PMID:16824107 and should be re-keyed.

> Interestingly, other traits were also strongly affected by the ccmC mutation, including the production of pyocyanin, swarming and twitching motility, and rhamnolipid production.
> — PMID:18174132

## 40. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I3N5 enables GO:0004096 catalase activity (IMP, PMID:16824107)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0004096
- **Recorded in:** `genes/PSEAE/ccmC/ccmC-ai-review.yaml`

enables GO:0004096 catalase activity (IMP) on PA1477 ccmC records the mutant phenotype "catalase production was undetectable" (PMID:18174132) as a molecular function of CcmC. CcmC is a heme-handling subunit of the cytochrome c maturation complex, not a catalase. Please delete this row. It is the sole seed of the PAINT IBD at PTN001247822, which propagates catalase activity to about 143 proteins.

## 41. WRONG_REFERENCE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I3N5 enables GO:0004096 catalase activity (IMP, PMID:16824107)
- **Field:** DB:Reference
- **Change:** PMID:16824107 → PMID:18174132
- **Likely cause:** IDENTIFIER_TRANSPOSITION
- **Recorded in:** `genes/PSEAE/ccmC/ccmC-ai-review.yaml`

PMID:16824107 is an E. coli CcmABC biochemistry paper and does not report catalase activity. The phenotype is reported for the P. aeruginosa ccmC mutant in PMID:18174132.

## 42. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I3N5 involved_in GO:0009247 glycolipid biosynthetic process (IMP, PMID:16824107)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0009247
- **Recorded in:** `genes/PSEAE/ccmC/ccmC-ai-review.yaml`

Reduced rhamnolipid production in a ccmC mutant (PMID:18174132) is an indirect phenotype; CcmC does not take part in glycolipid biosynthesis. The row also cites the wrong paper (PMID:16824107, an E. coli study).

## 43. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I3N5 involved_in GO:0043107 type IV pilus-dependent motility (IMP, PMID:16824107)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0043107
- **Recorded in:** `genes/PSEAE/ccmC/ccmC-ai-review.yaml`

Reduced twitching motility in a ccmC mutant (PMID:18174132) is an indirect phenotype of losing cytochrome c maturation. The row also cites the wrong paper (PMID:16824107, an E. coli study).

## 44. WRONG_REFERENCE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I3N5 involved_in GO:0071977 bacterial-type flagellum-dependent swimming motility (IMP, PMID:16824107)
- **Field:** DB:Reference
- **Change:** check PMID:16824107 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/ccmC/ccmC-ai-review.yaml`

PMID:16824107 is an E. coli Ccm biochemistry paper with no motility data. The P. aeruginosa ccmC mutant phenotypes come from PMID:18174132, whose abstract reports swarming and twitching but not swimming. Please check the source of the swimming-motility row; even if confirmed, it is an indirect phenotype.

## 45. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I3N5 involved_in GO:0071978 bacterial-type flagellum-dependent swarming motility (IMP, PMID:16824107)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0071978
- **Recorded in:** `genes/PSEAE/ccmC/ccmC-ai-review.yaml`

Reduced swarming in a ccmC mutant (PMID:18174132) is an indirect phenotype. The row also cites the wrong paper (PMID:16824107, an E. coli study).

## 46. WRONG_REFERENCE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HZR3 involved_in GO:2001226 negative regulation of chloride transport (IDA, PMID:16236828)
- **Field:** DB:Reference
- **Change:** check PMID:16236828 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/cif/cif-ai-review.yaml`

involved_in GO:2001226 negative regulation of chloride transport (IDA) on PA2934 (cif) cites PMID:16236828 (Swiatecka-Urban et al. 2006). That study was done with an unfractionated cell-free filtrate of P. aeruginosa and predates the identification of the factor: its abstract attributes the effect to the filtrate and names no protein. The attribution to PA2934 was made in PMID:17502391 (MacEachran et al. 2007), where purified six-His-tagged Cif was shown to be necessary and sufficient to reduce apical-membrane CFTR and CFTR-mediated chloride secretion, and the mechanism was resolved in PMID:21455491. Please consider re-pointing the reference to PMID:17502391 (optionally keeping PMID:16236828 as a second row with an appropriate code). The annotation itself is correct; only the cited evidence does not identify the gene product.

> report herein that a cell-free filtrate of P. aeruginosa reduced CFTR-mediated
> — PMID:16236828

> sufficient to mediate the reduction in apical membrane expression of CFTR and a
> — PMID:17502391

## 47. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:G3XCU6 involved_in GO:0019344 L-cysteine biosynthetic process (IMP, PMID:9218775)
- **Change:** delete the record asserting GO:0019344
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/cysB/cysB-ai-review.yaml`

GO:0019344 L-cysteine biosynthetic process (IMP, PMID:9218775) for cysB PA1754 (G3XCU6) records that a cysB insertion mutant is a cysteine auxotroph. CysB is a LysR-type transcriptional activator of the cys regulon and catalyses no step of cysteine synthesis, so the phenotype shows necessity, not participation. Please remove the row (CysB's regulatory role is captured by GO:0045893, IDA, PMID:20370820). This row is the sole seed of the PAINT IBD at PTN002824317.

> A CysB-deficient mutant of CHA, constructed by insertional inactivation of cysB, was a cysteine auxotroph
> — PMID:9218775

## 48. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HTG5 enables GO:0047865 dimethylglycine dehydrogenase activity (IDA, PMID:17951379)
- **Field:** Evidence_Code
- **Change:** ECO:0000314 → ECO:0000315 (IMP (inferred from mutant phenotype))
- **Recorded in:** `genes/PSEAE/dgcB/dgcB-ai-review.yaml`

enables GO:0047865 dimethylglycine dehydrogenase activity (IDA) and enables GO:0047866 dimethylglycine oxidase activity (IDA) on PA5399 (dgcB) both cite PMID:17951379, a genetic study whose evidence for dgcAB is the inability of transposon mutants to grow on dimethylglycine and the accumulation of 13C-labelled dimethylglycine in them. No enzyme was assayed; the full text states that characterisation of the biochemical activities of the dgcA and dgcB gene products remains a subject for future research. IMP therefore fits both rows better than IDA. The companion process rows from the same paper are already coded IMP.

> with mutations in the dgcAB (PA5398-PA5399) genes, which exhibit homology to
> — PMID:17951379

## 49. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HTG5 enables GO:0047865 dimethylglycine dehydrogenase activity (IDA, PMID:17951379)
- **Field:** GO_Term
- **Change:** check GO:0047865 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/dgcB/dgcB-ai-review.yaml`

PA5399 (dgcB) carries both GO:0047865 dimethylglycine dehydrogenase activity and GO:0047866 dimethylglycine oxidase activity from the same reference. The two terms describe incompatible reactions: GO:0047865 uses an electron-transfer flavoprotein as acceptor, GO:0047866 uses O2 and releases H2O2. One enzyme system does one or the other, and PMID:17951379 measured neither; it established genetically that dgcA and dgcB are required for the dimethylglycine to sarcosine conversion. In addition, the methyl-removing activity is more plausibly DgcA's: PA5398 is described in that paper as a predicted flavin mononucleotide oxidoreductase similar to a putative N-methylproline demethylase, whereas PA5399 is described as a probable membrane-spanning ferredoxin Fe-S oxidoreductase and carries five predicted transmembrane helices, two 4Fe-4S ferredoxin domains and two CCG domains, the architecture of the electron-transfer subunit in its PANTHER family (PTHR43255: heterodisulfide reductase subunit C, FadF, EtfAB:quinone oxidoreductase). Please consider replacing the two specific activity rows on PA5399 with a generic oxidoreductase or iron-sulfur electron-transfer claim, or qualifying them as contributes_to on the DgcAB system, until the reaction and the acceptor have been measured. These rows are the sole seeds of the PAINT IBD at PTN000229983, which propagates an oxidoreductase annotation to 33 leaves.

> A single enzyme system does one or the other.
> — file:PSEAE/dgcB/dgcB-notes.md

> /note="4Fe-4S ferredoxin-type"
> — file:PSEAE/dgcB/dgcB-uniprot.txt

## 50. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:G3XD14 involved_in GO:0045861 negative regulation of proteolysis (IDA, PMID:11160083)
- **Change:** delete the record asserting GO:0045861
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/dksA/dksA-ai-review.yaml`

GO:0045861 negative regulation of proteolysis (IDA, PMID:11160083) for dksA PA4723 records that multicopy dksA reduced elastase production. That is decreased production of a secreted protease, which the authors attribute to indirect inhibition of rhlI transcription; it is not regulation of proteolysis. Please remove the row.

> In trans, dksA suppressed the elastase production of mutant PR1-E4 and reduced the rhamnolipid production of both PR1-E4 and PAO1.
> — PMID:11160083

## 51. WRONG_REFERENCE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:G3XD14 enables GO:0070063 RNA polymerase binding (IDA, PMID:21255113)
- **Field:** DB:Reference
- **Change:** check PMID:21255113 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/dksA/dksA-ai-review.yaml`

GO:0070063 RNA polymerase binding (IDA) for dksA PA4723 cites PMID:21255113, whose biochemistry is on the paralog DksA2 (PA5536) with E. coli RNAP. Co-purification of PA4723 DksA with RNAP subunits is reported in PMID:15853892. Please check whether the row was meant for PA5536 or should cite PMID:15853892.

> In vitro, purified DksA2 stabilizes the closed promoter complex at, and thus inhibits transcription from, the rrnB P1 promoter
> — PMID:21255113

## 52. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:O33407 involved_in GO:0009247 glycolipid biosynthetic process (IMP, PMID:17631636)
- **Field:** GO_ID
- **Change:** check GO:0009247 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/estA/estA-ai-review.yaml`

PseudoCAP IMP glycolipid biosynthetic process on EstA (O33407, PA5112) from PMID:17631636 records reduced rhamnolipid in an estA deletion mutant. EstA is a surface-exposed outer-membrane carboxylesterase and the step it affects is unknown, so this is a necessity phenotype rather than participation in rhamnolipid biosynthesis. Please check the full text; if no biosynthetic step is attributed to EstA, remove the row or replace it with a regulation-type term. It supports the PAINT lipid biosynthetic process IBD at PTN005219546 (960 leaf IBAs).

## 53. WRONG_TERM (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:O33407 involved_in GO:0071973 bacterial-type flagellum-dependent cell motility (IMP, PMID:17631636)
- **Field:** GO_ID
- **Change:** check GO:0071973 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/estA/estA-ai-review.yaml`

PseudoCAP IMP bacterial-type flagellum-dependent cell motility on EstA (O33407) from PMID:17631636. The estA mutant loses swimming, swarming and twitching alike, so the defect is not specific to the flagellar machinery, and EstA (a surface esterase) is not a flagellar component. The general cell motility term, already annotated by UniProt from the same paper, captures the phenotype.

## 54. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:O33407 involved_in GO:0071978 bacterial-type flagellum-dependent swarming motility (IDA, PMID:20360178)
- **Field:** Evidence_Code
- **Change:** ECO:0000314 → ECO:0000315 (IMP (mutant phenotype, includes overexpression))
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/estA/estA-ai-review.yaml`

PseudoCAP IDA for swarming motility on EstA (O33407) from PMID:20360178 rests on an estA overexpression strain showing enhanced swarming; an overexpression phenotype is coded IMP in GO. The authors also state the effect may be indirect.

## 55. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:G3XD64 enables GO:0005524 ATP binding (IDA, PMID:10629180)
- **Field:** Evidence_Code
- **Change:** check ECO:0000314 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/fleN/fleN-ai-review.yaml`

GO:0005524 ATP binding for FleN (PA1454) is annotated IDA to PMID:10629180 (Dasgupta et al. 2000). The abstract reports only that the ORF codes for a protein "with an ATP-binding motif at its N terminus"; the same authors called FleN "a putative ATP/GTP binding protein" in PMID:11673434 (2001), so no ATP-binding assay appears to underlie the row. Either change the evidence to ISM/ISS for PMID:10629180, or re-key the IDA to PMID:28065505 (Chanchal et al. 2017, FleN-AMP-PNP crystal structure, PDB 5J1J), which provides direct evidence. This row is the sole seed of the PAINT IBD at PTN000344128 (about 149 leaf IBAs), so the correction should be coordinated with PAINT re-seeding.

> that coded for a protein (280 amino acids) with an ATP-binding motif at its N terminus was found
> — PMID:10629180

> Flagellar number in Pseudomonas aeruginosa is controlled by FleN, a putative ATP/GTP binding protein
> — PMID:11673434

## 56. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q03456 involved_in GO:1901668 regulation of superoxide dismutase activity (IMP, PMID:8763923)
- **Change:** check GO:1901668 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/fur/fur-ai-review.yaml`

GO:1901668 regulation of superoxide dismutase activity (IMP, PMID:8763923) for P. aeruginosa Fur (Q03456). The paper shows altered Mn-SOD levels in fur mutants and Fur binding to the iron boxes of the sodA operon, i.e. transcriptional control of sodA expression, not modulation of enzyme activity. Consider removing the row or replacing it with negative regulation of DNA-templated transcription (with a has_input/regulates extension to sodA if wanted).

> Purified wild-type Fur bound more avidly than mutant Fur to a PCR product containing two palindromic 19-bp "iron box" regions controlling expression of an operon containing the sodA gene that encodes Mn-SOD.
> — PMID:8763923

## 57. WRONG_EVIDENCE_CODE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:P14165 involved_in GO:0006099 tricarboxylic acid cycle (IDA, PMID:7626013)
- **Field:** Evidence_Code
- **Change:** check ECO:0000314 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/gltA/gltA-ai-review.yaml`

GO:0006099 tricarboxylic acid cycle for gltA (PA1580, P14165) is annotated IDA to PMID:7626013. The abstract reports purification and characterisation of two citrate synthase isoenzymes and does not assay TCA cycle function; the process follows from the activity. IC (with GO:0036440 from the same paper) would be the accurate code. The row is the sole seed of the PAINT IBD at PTN002450857 (18 leaf IBAs); the IBD conclusion is sound, so only the seed evidence needs attention.

> CSI and CSII were also shown to be distinct kinetically, immunologically and in terms of their regulatory properties.
> — PMID:7626013

## 58. WRONG_REFERENCE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:P29365 enables GO:0004412 homoserine dehydrogenase activity (IDA, PMID:10220164)
- **Field:** DB:Reference
- **Change:** check PMID:10220164 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/hom/hom-ai-review.yaml`

enables GO:0004412 and involved_in GO:0009088 (both IDA) on PA3736 hom cite Patte et al. 1999 (PMID:10220164). That abstract concerns only ThrB and the ThrH homoserine kinase isozyme and never mentions homoserine dehydrogenase; the same PMID was attached to thrB, hom and thrH on the same date. Unless the full text contains an HDH assay, the supporting reference should be PMID:1333566, which reports HDH activity and threonine feedback inhibition of the cloned P. aeruginosa hom product. The annotations themselves are correct.

> In P. aeruginosa, threonine auxotrophy is observed only when both thrB and thrH are simultaneously inactivated.
> — PMID:10220164

> HDH activity was feedback inhibited by threonine
> — PMID:1333566

## 59. WRONG_REFERENCE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:P29365 involved_in GO:0009088 L-threonine biosynthetic process (IDA, PMID:10220164)
- **Field:** DB:Reference
- **Change:** check PMID:10220164 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/hom/hom-ai-review.yaml`

involved_in GO:0009088 (IDA) on PA3736 hom cites PMID:10220164, whose abstract concerns only ThrB and ThrH. This row is the sole seed of the PTN000752178 threonine biosynthesis IBD. The claim is correct, but its support should be PMID:1333566 unless the 1999 full text assays Hom.

> In P. aeruginosa, threonine auxotrophy is observed only when both thrB and thrH are simultaneously inactivated.
> — PMID:10220164

## 60. WRONG_REFERENCE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HU77 involved_in GO:0006548 L-histidine catabolic process (IMP, PMID:4290562)
- **Field:** DB:Reference
- **Change:** check PMID:4290562 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/hutF/hutF-ai-review.yaml`

involved_in GO:0006548 (IMP) on PA5106 hutF cites Lessie and Neidhardt 1967. Its abstract reports a pooled capacity to degrade formiminoglutamate (step IV), which in PAO1 is provided by both HutF/HutG and HutE (PA3175), and describes only urocanase-deficient, auxotrophic and repression mutants. No hutF mutant is described, and the study predates any gene assignment. Please check the full text; if no hutF-specific mutant is reported, re-key the annotation to PMID:16475788 (IDA, direct enzymology placing PA5106 in the hut pathway). The annotation is biologically correct. This row is the sole seed of the PANTHER IBD at PTN000138516.

> Histidine ammonia lyase (histidase), urocanase, and the capacity to degrade formiminoglutamate, which are respectively involved in steps I, II, and IV in the catabolism of histidine
> — PMID:4290562

## 61. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HU85 enables GO:0004397 histidine ammonia-lyase activity (IMP, PMID:4290562)
- **Field:** Evidence_Code
- **Change:** check ECO:0000315 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/hutH/hutH-ai-review.yaml`

enables GO:0004397 (IMP) on PA5098 hutH cites Lessie and Neidhardt 1967. The abstract reports a direct assay and partial purification of P. aeruginosa histidase (MW 210,000; Km 2 mM), not the phenotype of a histidase mutant; its mutants are urocanase-deficient, auxotrophic and catabolite-repression mutants. IDA fits the evidence better than IMP, unless the full text describes a histidase-deficient mutant. The companion IMP for GO:0006548 rests on the same paper. The annotation itself is correct.

> The molecular weight of partially purified histidase was estimated at 210,000 by sucrose gradient centrifugation.
> — PMID:4290562

## 62. WRONG_REFERENCE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HU91 involved_in GO:0006548 L-histidine catabolic process (IMP, PMID:4290562)
- **Field:** DB:Reference
- **Change:** check PMID:4290562 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/hutI/hutI-ai-review.yaml`

involved_in GO:0006548 (IMP) on PA5092 hutI cites Lessie and Neidhardt 1967. Its abstract reports histidase, urocanase and FIGLU-degrading activities (steps I, II and IV) and urocanase-deficient, auxotrophic and catabolite-repression mutants. It does not mention imidazolonepropionase (step III) or a mutant lacking it, and as a pre-cloning study it cannot identify a mutation in PA5092. Please check the full text. If no step III mutant is described, the IMP should be withdrawn, or re-keyed to a paper with a genetically defined hutI mutant. The annotation is biologically correct, so ISS/IBA-level support from the HutI family would be the honest alternative. This row is the sole seed of the PANTHER IBD at PTN000505272.

> Histidine ammonia lyase (histidase), urocanase, and the capacity to degrade formiminoglutamate, which are respectively involved in steps I, II, and IV in the catabolism of histidine
> — PMID:4290562

## 63. WRONG_REFERENCE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HU91 enables GO:0050480 imidazolonepropionase activity (IMP, PMID:4290562)
- **Field:** DB:Reference
- **Change:** check PMID:4290562 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/hutI/hutI-ai-review.yaml`

enables GO:0050480 imidazolonepropionase activity (IMP) on PA5092 hutI cites Lessie and Neidhardt 1967, whose abstract reports only histidase, urocanase and FIGLU-degrading activities (steps I, II, IV). The paper does not mention an imidazolonepropionase assay or a hutI mutant, and it predates any assignment of a mutation to PA5092. Please check the full text. If step III was not assayed in a genetically defined hutI mutant, withdraw the IMP (the function is better supported by ISS/IBA to the HutI family). This row is the sole seed of the PANTHER IBD at PTN000505272 (52 leaf IBAs).

> Histidine ammonia lyase (histidase), urocanase, and the capacity to degrade formiminoglutamate, which are respectively involved in steps I, II, and IV in the catabolism of histidine
> — PMID:4290562

## 64. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HZQ8 involved_in GO:0015628 protein secretion by the type II secretion system (IDA, PMID:9642203)
- **Field:** GO_ID
- **Change:** check GO:0015628 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/lap/lap-ai-review.yaml`

PA2939 (PaAP) is a cargo of the Xcp type II secretion system, not a component of it. GO practice reserves "protein secretion by the type II secretion system" for the secretion machinery; the secreted substrate does not carry out the process. Consider deleting the row, or recording the cargo relationship on the Xcp proteins (has_input) and keeping the extracellular region CC on PaAP.

## 65. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HZQ8 involved_in GO:0043952 protein transport by the Sec complex (IDA, PMID:9642203)
- **Field:** GO_ID
- **Change:** check GO:0043952 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/lap/lap-ai-review.yaml`

PA2939 (PaAP) is a Sec-exported cargo; it is not part of the Sec translocation machinery. The cited paper (PMID:9642203) shows its signal peptide is removed, which is not direct evidence for the Sec complex and is not participation in the transport process. Consider deleting the row.

## 66. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:P14756 involved_in GO:0015628 protein secretion by the type II secretion system (IDA, PMID:9642203)
- **Field:** GO_ID
- **Change:** check GO:0015628 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/lasB/lasB-ai-review.yaml`

PA3724 (LasB) is a cargo of the Xcp type II secretion system, not a component of it. GO practice reserves "protein secretion by the type II secretion system" for the secretion machinery; the secreted substrate does not carry out the process. Consider deleting the row, or recording the cargo relationship on the Xcp proteins (has_input), and keeping the extracellular region CC on LasB. The identical row on PA2939 (PaAP), from the same reference, has the same problem.

## 67. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:P14756 involved_in GO:0043952 protein transport by the Sec complex (IDA, PMID:9642203)
- **Field:** GO_ID
- **Change:** check GO:0043952 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/lasB/lasB-ai-review.yaml`

PA3724 (LasB) is a Sec-exported cargo; it is not part of the Sec translocation machinery, and the cited evidence (removal of its signal peptide) is neither participation in the transport process nor direct evidence that the translocon used is Sec rather than Tat. Consider deleting the row. The identical row on PA2939 (PaAP) from the same reference has the same problem.

## 68. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:P33883 involved_in GO:0007165 signal transduction (IDA, PMID:8493556)
- **Field:** GO_ID
- **Change:** GO:0007165 → GO:0009372 (quorum sensing)
- **Recorded in:** `genes/PSEAE/lasI/lasI-ai-review.yaml`

involved_in GO:0007165 signal transduction (IDA, PMID:8493556) on PA1432 lasI. LasI is the autoinducer synthase: the paper shows lasI is needed to make the diffusible Pseudomonas autoinducer that LasR requires for elastase expression. GO:0007165 covers events at and within the receiving cell, starting with signal reception (LasR), so it does not apply to the synthase. Please re-term to GO:0009372 quorum sensing, whose definition includes producing the signal. The evidence is gene fusions and mutant phenotype, so IMP fits better than IDA. This row is the sole seed of the PANTHER IBD at PTN002217335.

> The lasl gene is involved in the synthesis of a diffusible molecule termed Pseudomonas autoinducer (PAI).
> — PMID:8493556

## 69. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I489 enables GO:0047580 4-hydroxyproline epimerase activity (IMP, PMID:27145750)
- **Change:** GO:0047580 → GO:0050346 (trans-L-3-hydroxyproline dehydratase activity)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/lhpL/lhpL-ai-review.yaml`

PseudoCAP annotates PA1255 (lhpL, UniProtKB:Q9I489) with GO:0047580 4-hydroxyproline epimerase activity, IMP, from PMID:27145750. Two problems. (1) The term's reaction is experimentally absent on this protein: Swiss-Prot records, with ECO:0000269|PubMed:17849014, that it displays neither t4LHyp epimerase nor proline racemase activity, and assigns it the trans-3-hydroxy-L-proline dehydratase (EC 4.2.1.77) and trans-3-hydroxy-L-proline 2-epimerase reactions (ECO:0000269|PubMed:27929065). GO:0050346 is the matching existing term. The organism's genuine 4-hydroxyproline 2-epimerase is PA1268 (UniProtKB:Q9I476), which PseudoCAP annotates with GO:0047580 from the same paper; that row looks correct. (2) The cited evidence is an induction phenotype of an lhpA lhpK double mutant, which cannot assign a molecular function to either single gene, so a process term or an IGC/ISS code would fit it better than IMP on a reaction term. This row is the sole seed of the PAINT IBD at PTN002433936, from which 35 GOA rows now descend.

> Induction of the lhpA promoter by d-Hyp was completely abolished in the lhpA lhpK double mutant devoid of two epimerases, while the induction effect of l-Hyp remained unchanged
> — PMID:27145750

## 70. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I298 involved_in GO:0046247 terpene catabolic process (IMP, PMID:16820476)
- **Change:** GO:0046247 → GO:0016100 (monoterpenoid catabolic process)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/liuC/liuC-ai-review.yaml`

GO:0046247 terpene catabolic process (defined for terpene hydrocarbons) for liuC (PA2013, Q9I298), IMP to PMID:16820476. The substrates of the P. aeruginosa Atu/Liu pathway are acyclic monoterpenoid alcohols and acids (citronellol, geraniol, citronellate), so GO:0016100 monoterpenoid catabolic process is the accurate term. This row is the sole seed of the PAINT IBD at PTN001733227, which should not propagate the terpenoid role to the hydratase clade.

> P. fluorescens, but not P. putida, could grow on acyclic terpenes (citronellol and citronellate)
> — PMID:16820476

## 71. WRONG_REFERENCE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9X6P4 involved_in GO:0009103 lipopolysaccharide biosynthetic process (IDA, PMID:1904818)
- **Field:** DB:Reference
- **Change:** PMID:1904818 → PMID:9440522 (Dotson et al. 1998, Expression cloning of a Pseudomonas gene encoding a hydroxydecanoyl-acyl carrier protein-dependent UDP-GlcNAc acyltransferase)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/lpxA/lpxA-ai-review.yaml`

involved_in GO:0009103 lipopolysaccharide biosynthetic process (IDA) on PA3644 cites Kulshin et al. 1991 (PMID:1904818), a chemical, GC-MS and NMR structural characterisation of lipid A purified from P. aeruginosa strains. That paper assays no enzyme, does not mention lpxA, and predates the cloning of the gene (1998) and the PAO1 genome, so it cannot be direct evidence for this gene product. The intended reference is almost certainly Dotson et al. 1998 (PMID:9440522), which cloned PAO1 lpxA, assayed the enzyme as a 10-carbon-specific UDP-GlcNAc acyltransferase and complemented an E. coli lpxA mutant; it is reference [1] of UniProtKB:Q9X6P4. Please repoint the reference. Note that this row is the only seed of the PANTHER IBD for GO:0009103 at PTN000602377, which propagates to 24 LpxA-family leaves.

> was investigated using chemical analysis, methylation analysis
> — PMID:1904818

> we here report the isolation of the lpxA gene of Pseudomonas aeruginosa
> — PMID:9440522

## 72. WRONG_EVIDENCE_CODE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I544 enables GO:0000287 magnesium ion binding (IMP, PMID:24722909)
- **Field:** Evidence_Code
- **Change:** check ECO:0000315 (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/PSEAE/mgtE/mgtE-ai-review.yaml`

enables GO:0000287 magnesium ion binding (IMP) on PA0913 mgtE cites Coffey et al. 2014 (PMID:24722909). As the abstract presents it, the Mg2+-binding sites were predicted from a homology model based on T. thermophilus MgtE, and their mutation disrupted coupling of transport and cytotoxicity regulation. A loss-of-function phenotype does not show that the residues bind Mg2+. Unless the full text reports a direct binding assay, the annotation is better made as ISS with UniProtKB:Q5SMG8 (Mg2+-bound crystal structures, PMID:17700703). This row is the sole seed of the PAINT IBD at PTN000227060.

> showed that magnesium-binding sites in the connecting helix region of MgtE are vital in coupling these two functions
> — PMID:24722909

## 73. WRONG_EVIDENCE_CODE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HUL2 involved_in GO:0071978 bacterial-type flagellum-dependent swarming motility (IMP, PMID:15629949)
- **Field:** Evidence_Code
- **Change:** check ECO:0000315 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/motB/motB-ai-review.yaml`

involved_in GO:0071978 (IMP) on motB (PA4953) cites Toutain et al. 2005, in which the motAB deletion swarms as well as wild type; a swarming defect is seen only when motCD is also deleted. The support for MotAB in swarming is a genetic interaction (IGI with motCD, PA1460-PA1461), not a motB mutant phenotype. This row is one of the seeds of the PTN001251133 swarming IBD.

> The Δ motAB mutant is able to swarm as well as the WT in agar concentrations up to 0.7%.
> — PMID:15629949

## 74. WRONG_TERM (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HUL2 involved_in GO:0071978 bacterial-type flagellum-dependent swarming motility (IMP, PMID:25349157)
- **Field:** GO_ID
- **Change:** check GO:0071978 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/motB/motB-ai-review.yaml`

involved_in GO:0071978 (IMP) on motB (PA4953) cites Kuchma et al. 2015, whose abstract reports that motAB mutation stimulates swarming and restores swarming at high c-di-GMP. An increased-swarming phenotype does not support a positive involved_in by IMP; the finding is that MotAB is needed for c-di-GMP-mediated repression of swarming. Please check whether the row should be dropped or recast. This row is a seed of the PTN001251133 swarming IBD.

> Mutating the motAB genes restores swarming motility to a strain with artificially elevated levels of c-di-GMP as well as stimulates swarming in the wild-type strain
> — PMID:25349157

## 75. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:G3XD20 involved_in GO:0007165 signal transduction (IDA, PMID:21036998)
- **Change:** GO:0007165 → GO:0009968 (negative regulation of signal transduction)
- **Recorded in:** `genes/PSEAE/mucD/mucD-ai-review.yaml`

GO:0007165 signal transduction IDA for MucD (PA0766, G3XD20) from PMID:21036998. The paper shows that mucD inactivation activates MucP-dependent MucA degradation and AlgU activity, so MucD negatively regulates the RIP signalling cascade rather than taking part in it. The experiments are mutant phenotypes, so the evidence code should be IMP. Suggest GO:0009968 negative regulation of signal transduction, IMP.

> When mucD is inactivated, a high level of algU promoter activity was noted (Fig. 3A ), suggesting that the RIP activities are negatively regulated by MucD.
> — PMID:21036998

## 76. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HT76 enables GO:0004748 ribonucleoside-diphosphate reductase activity, thioredoxin disulfide as acceptor (IDA, PMID:15722359)
- **Field:** GO_Term
- **Change:** check GO:0004748 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/nrdJa/nrdJa-ai-review.yaml`

enables GO:0004748 (ribonucleoside-diphosphate reductase activity, thioredoxin disulfide as acceptor; IDA, PMID:15722359) on PA5497 (nrdJa) fixes the substrate as a ribonucleoside diphosphate. The later biochemical study of the same enzyme with purified subunits (PMID:26225432) found that ribonucleoside triphosphates are preferred by more than 60-fold over CDP, so GO:0008998 ribonucleoside-triphosphate reductase (thioredoxin) activity describes the principal reaction; CDP reduction is measurable but minor. The same applies to the companion annotation on PA5496 (nrdJb) if one exists. Please consider adding GO:0008998 (and keeping GO:0004748 for the minor reaction). Note also that neither paper used thioredoxin: both assays used DTT or TCEP, so the acceptor clause of either term is an inference from class I/II RNR precedent rather than a measurement in P. aeruginosa. This row is the sole seed of the PAINT IBD at PTN000171476, which propagates the diphosphate term to 39 leaves.

> For NrdJa-NrdJb from PA we found that NTP was the favored substrate.
> — PMID:26225432

> The results revealed that CTP is the preferred substrate with a >60-fold higher activity compared to CDP
> — PMID:26225432

## 77. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q51485 involved_in GO:0008643 carbohydrate transport (IDA, PMID:7768797)
- **Field:** Evidence_Code
- **Change:** check ECO:0000314 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/oprB/oprB-ai-review.yaml`

GO:0008643 carbohydrate transport for OprB (PA3186, Q51485) is annotated IDA to PMID:7768797. The paper's evidence is initial sugar uptake by whole cells of an interposon oprB mutant and an OprB overexpressing strain compared with wild type, which is a mutant phenotype (IMP). The claim is sound, and the specific substrates (glucose, mannitol, fructose, glycerol) could be annotated with the substrate-specific transmembrane transport terms. This row is the sole seed of the PAINT IBD at PTN002209977.

> Using interposon mutagenesis, we have generated strains of Pseudomonas aeruginosa which lack or overexpress the substrate-selective OprB porin of this species.
> — PMID:7768797

## 78. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:P09786 involved_in GO:0002047 phenazine biosynthetic process (IMP, PMID:2153661)
- **Change:** check GO:0002047 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/phnB/phnB-ai-review.yaml`

PseudoCAP annotates phnB (PA1002, UniProtKB:P09786) and phnA (P09785) with GO:0002047 phenazine biosynthetic process, IMP, from PMID:2153661, on the basis of reduced pyocyanin in phn mutants. Work since then shows the route is indirect: PhnAB supplies anthranilate for the quinolone signal PQS, and PQS induces the phenazine operons (PMID:23449919), whereas the phenazine core is made from chorismate by PhzE via 2-amino-2-deoxyisochorismate with no anthranilate intermediate (PMID:21454481). UniProt's current FUNCTION line already states this. Our recommendation is to retire the phenazine process term for phnA and phnB in favour of the anthranilate synthase activity they are also annotated with, plus a quinolone-signal biosynthetic process term if one is created; if PseudoCAP prefers to keep a downstream link, a regulatory term such as GO:1900982 positive regulation of phenazine biosynthetic process would describe the observation more accurately. The row is the sole seed of the PAINT IBD at PTN000230115, from which 267 GOA rows now descend onto TrpG proteins of non-phenazine-producing organisms.

> At the time it was believed that PhnAB generated anthranilate for pyocyanin production, but later work determined that anthranilate is instead a precursor for PQS production, which is required to induce genes for pyocyanin biosynthesis
> — PMID:23449919

## 79. WRONG_QUALIFIER (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:P09786 enables GO:0004049 anthranilate synthase activity (IMP, PMID:2153661)
- **Field:** Qualifier
- **Change:** check enables (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/phnB/phnB-ai-review.yaml`

The anthranilate synthase reaction (chorismate + L-glutamine -> anthranilate + pyruvate + L-glutamate) is carried out by the PhnA-PhnB heterotetramer: PhnB is the glutamine amidotransferase subunit that generates ammonia, and PhnA condenses it with chorismate. The complementation evidence is for the gene pair, not for phnB alone, so contributes_to GO:0004049 would describe the subunit's role more accurately than enables. The same applies to the companion row on phnA (P09785), which enables the chorismate-utilizing half.

> Heterotetramer consisting of two non-identical subunits: a
> — file:PSEAE/phnB/phnB-uniprot.txt

## 80. WRONG_REFERENCE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HWG9 enables GO:0004497 monooxygenase activity (IDA, PMID:17012792)
- **Field:** DB:Reference
- **Change:** PMID:17012792 → PMID:17253782 (Parsons et al. 2007, Structural and functional analysis of the pyocyanin biosynthetic protein PhzM from Pseudomonas aeruginosa)
- **Recorded in:** `genes/PSEAE/phzS/phzS-ai-review.yaml`

enables GO:0004497 monooxygenase activity (IDA) on PA4217 phzS cites PMID:17012792 (Gohain et al. 2006), a crystallization and preliminary X-ray communication that reports cloning, purification, crystallization and data collection only and contains no enzyme assay. The activity was shown with purified PhzS in PMID:17253782 (NADH-dependent conversion of PCA to 1-hydroxyphenazine, and pyocyanin formation with PhzM). Please re-key the row to PMID:17253782, or consider the more specific GO:0102169. This row is the sole seed of the PAINT IBD at PTN002492679; the IBD itself remains sound.

> Here, we report the large-scale expression of recombinant PhzS and the first diffraction data collected from native and seleno- l -methionine-labelled protein crystals as an initial step towards understanding the reaction mediated by PhzS and its substrate specificity.
> — PMID:17012792

> This was confirmed by incubating PhzS with PCA and NADH. 1-HP was formed in an NADH dependant manner
> — PMID:17253782

## 81. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:P04739 involved_in GO:0043107 type IV pilus-dependent motility (IDA, PMID:12933890)
- **Field:** Evidence_Code
- **Change:** ECO:0000314 → ECO:0000315 (IMP)
- **Recorded in:** `genes/PSEAE/pilA/pilA-ai-review.yaml`

involved_in GO:0043107 (IDA, PMID:12933890) on PA4525 pilA: the paper examines twitching colony morphology of a pilA mutant of strain PAK, which is a mutant phenotype (IMP), not a direct assay. The term is correct.

## 82. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:P04739 involved_in GO:0043107 type IV pilus-dependent motility (IMP, PMID:9224878)
- **Field:** Evidence_Code
- **Change:** ECO:0000315 → ECO:0000304 (TAS)
- **Recorded in:** `genes/PSEAE/pilA/pilA-ai-review.yaml`

involved_in GO:0043107 (IMP, PMID:9224878) on PA4525 pilA: Alm and Mattick 1997 (Gene 192:89-98) is a review of genes involved in type-4 fimbrial biogenesis and function, not a primary mutant study, so TAS is the appropriate code. The term is correct.

> Thus far over 30 genes have been characterized
> — PMID:9224878

## 83. WRONG_REFERENCE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:P22608 involved_in GO:0043107 type IV pilus-dependent motility (IDA, PMID:1671384)
- **Field:** DB:Reference
- **Change:** check PMID:1671384 (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/PSEAE/pilB/pilB-ai-review.yaml`

involved_in GO:0043107 type IV pilus-dependent motility (IDA) on PA4526 pilB cites Strom et al. 1991 (PMID:1671384), a pilD paper whose abstract mentions pilB only as necessary for pilus biogenesis, citing Nunn, Bergman and Lory 1990 (PMID:1971619), and does not report a motility assay. If the full text has no pilB motility data, the row would be better keyed to a paper that tests pilB twitching (e.g. PMID:18174131 or PMID:25049409) with IMP rather than IDA. Please check.

> The function of the other two accessory proteins, PilB and PilC, appears to be restricted to pilus biogenesis, and strains carrying mutations in their respective genes do not show an export defect.
> — PMID:1671384

## 84. WRONG_EVIDENCE_CODE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:P22608 involved_in GO:0043683 type IV pilus assembly (IDA, PMID:1671384)
- **Field:** Evidence_Code
- **Change:** check ECO:0000314 (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/PSEAE/pilB/pilB-ai-review.yaml`

involved_in GO:0043683 type IV pilus assembly (IDA) on PA4526 pilB cites Strom et al. 1991 (PMID:1671384), a pilD paper whose abstract restates, from Nunn, Bergman and Lory 1990 (PMID:1971619), that pilB is required for assembly of pili. The underlying evidence is a mutant phenotype (no pili), which is IMP, and the primary data are in PMID:1971619. Please check the evidence code and reference.

## 85. WRONG_REFERENCE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:P22610 located_in GO:0005886 plasma membrane (IDA, PMID:9466269)
- **Field:** DB:Reference
- **Change:** check PMID:9466269 (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/PSEAE/pilD/pilD-ai-review.yaml`

located_in GO:0005886 plasma membrane (IDA) on PA4528 pilD cites Kagami et al. 1998 (PMID:9466269), whose abstract is about xcpT temperature-sensitive mutants and xcpR suppressors and mentions PilD/XcpA only as the enzyme processing XcpT-W. If the full text has no PilD localization data, the row would be better keyed to PMID:1898929 (xcpA localised to the cytoplasmic membrane) or PMID:8331069. Please check. The row is a seed of the PAINT plasma membrane IBD at PTN000766410, which has two other seeds.

> These proteins, in addition to the pilin subunit, are cleaved and methylated by the PilD/XcpA prepilin peptidase
> — PMID:9466269

## 86. WRONG_EVIDENCE_CODE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:P22610 involved_in GO:0009297 pilus assembly (IDA, PMID:9668097)
- **Field:** Evidence_Code
- **Change:** check ECO:0000314 (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/PSEAE/pilD/pilD-ai-review.yaml`

involved_in GO:0009297 pilus assembly (IDA) on PA4528 pilD cites Pepe and Lory 1998 (PMID:9668097). The pilus-assembly evidence in the abstract is from PilD Gly95/Lys96 variants expressed in P. aeruginosa, i.e. a mutant phenotype (IMP). The term could also be the more specific GO:0043683 type IV pilus assembly. Please check.

## 87. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:P22610 part_of GO:0015627 type II protein secretion system complex (IDA, PMID:1588814)
- **Field:** GO_ID
- **Change:** check GO:0015627 (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/PSEAE/pilD/pilD-ai-review.yaml`

part_of GO:0015627 type II protein secretion system complex (IDA) on PA4528 pilD cites Bally et al. 1992 (PMID:1588814), whose abstract shows that XcpA/PilD processes the pseudopilins XcpT-W in vivo. That supports a role in type II secretion (processing of secretion apparatus components), not membership of the secretion complex; PilD is the prepilin peptidase shared with the type IV pilus system. Please consider replacing it with involved_in GO:0015628 protein secretion by the type II secretion system (e.g. IMP, PMID:1671384) or deleting it.

## 88. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:G3XD28 located_in GO:0044096 type IV pilus (IMP, PMID:7565110)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0044096
- **Recorded in:** `genes/PSEAE/pilM/pilM-ai-review.yaml`

located_in GO:0044096 type IV pilus (IMP, PMID:7565110) on PA5044 pilM records that pilM mutants lack fimbriae, which is a mutant phenotype and is already captured by the type IV pilus assembly and motility rows from the same paper. PilM is a cytoplasmic protein that associates with the inner membrane via PilN (PMID:19857645) and is not a component of the pilus fibre. Please delete the row. The same pattern applies to the pilN, pilO and pilP rows from PMID:7565110. This row is the sole seed of the PAINT IBD at PTN001286216.

> PilM-P were found to be required for fimbrial biogenesis
> — PMID:7565110

## 89. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:G3XD30 located_in GO:0044096 type IV pilus (IMP, PMID:7565110)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0044096
- **Recorded in:** `genes/PSEAE/pilN/pilN-ai-review.yaml`

located_in GO:0044096 type IV pilus (IMP, PMID:7565110) on PA5043 pilN records that pilM-P mutants lack fimbriae, a mutant phenotype already captured by the type IV pilus assembly and motility rows from the same paper. PilN is a single-pass inner-membrane protein of the PilMNOP alignment subcomplex (PMID:19857645), not a component of the pilus fibre. Please delete the row (the same pattern applies to the pilM, pilO and pilP rows from PMID:7565110). It is the sole seed of the PAINT IBD of GO:0044096 at PTN002220336.

> PilM-P were found to be required for fimbrial biogenesis
> — PMID:7565110

## 90. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:P24559 located_in GO:0044096 type IV pilus (TAS, PMID:20595000)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0044096
- **Recorded in:** `genes/PSEAE/pilT/pilT-ai-review.yaml`

located_in GO:0044096 type IV pilus (TAS, PMID:20595000) on PA0395 pilT: GO:0044096 is the extracellular fibre, while PilT is the cytoplasmic hexameric retraction ATPase (functional YFP-PilT is cytoplasmic and polar, PMID:15659660). PilT's location is already captured by the cytoplasm rows. Please delete the row; the same machine-versus-fibre pattern affects the PseudoCAP type IV pilus rows on pilM, pilN, pilO and pilP.

> Type IV pili are bacterial extracellular filaments
> — PMID:20595000

## 91. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:G3XCX3 enables GO:0016888 DNA endonuclease activity, producing 5'-phosphomonoesters (IDA, PMID:18174131)
- **Field:** GO_ID
- **Change:** GO:0016888 → GO:0016887 (ATP hydrolysis activity)
- **Likely cause:** IDENTIFIER_TRANSPOSITION
- **Recorded in:** `genes/PSEAE/pilU/pilU-ai-review.yaml`

enables GO:0016888 "DNA endonuclease activity, producing 5'-phosphomonoesters" (IDA, PMID:18174131) on PA0396 pilU. Chiang et al. 2008 assayed purified 6xHis-PilB, PilT and PilU and found ATPase activity; there is no nuclease assay and PilU is a PilT-like type IV pilus retraction ATPase. The same paper was used on the same date to annotate PA4526 pilB to GO:0016887 ATP hydrolysis activity, the adjacent GO id. Please change the GO id on the PA0396 row to GO:0016887. The row is the sole seed of a PAINT IBD at PTN000766390 that propagates DNA endonuclease activity to about 13 proteins.

> Assay of purified 6xHis-tagged PilB, PilT and PilU from P. aeruginosa showed that all three proteins have ATPase activities in vitro.
> — PMID:18174131

## 92. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I0Q0 enables GO:0004497 monooxygenase activity (IDA, PMID:20662781)
- **Field:** GO_ID
- **Change:** GO:0004497 → GO:0102164 (2-heptyl-3-hydroxy-4(1H)-quinolone synthase activity)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/pqsH/pqsH-ai-review.yaml`

The PseudoCAP IDA row for PA2587/pqsH from PMID:20662781 (Schertzer et al. 2010) is not wrong, only under-specific. The paper shows purified MBP-PqsH converting HHQ + NADH + O2 to PQS, which is exactly GO:0102164 / RHEA:37871 / EC 1.14.13.182. Requested change: re-point (or add) the IDA to GO:0102164. GO:0102164 is_a GO:0016709 is_a GO:0004497, so the PAINT IBD on PTN008173107 (monooxygenase activity) stays supported by a descendant-term experimental annotation.

> we show that PqsH catalyses the terminal step in PQS production, synthesizing PQS in vitro using the substrates 2-heptyl-4-quinolone (HHQ), NADH and oxygen
> — PMID:20662781

## 93. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I1N6 involved_in GO:0044010 single-species biofilm formation (IDA, PMID:19659934)
- **Field:** Evidence_Code
- **Change:** ECO:0000314 → ECO:0000315 (mutant phenotype evidence used in manual assertion)
- **Recorded in:** `genes/PSEAE/pslC/pslC-ai-review.yaml`

GO:0044010 single-species biofilm formation for PslC (PA2233, Q9I1N6) from PMID:19659934 is coded IDA, but the evidence is an in-frame deletion mutant that loses Psl and surface attachment, which is IMP. This row is the sole seed of the PAINT IBD at PTN002463206, which propagates biofilm formation to unrelated GT-2 glycosyltransferases.

> The same eleven strains that were deficient in attachment likewise did not produce detectable levels of Psl.
> — PMID:19659934

## 94. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:G3XDA6 involved_in GO:1900378 positive regulation of secondary metabolite biosynthetic process (IMP, PMID:16109947)
- **Field:** GO_ID
- **Change:** GO:1900378 → GO:0050709
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/ptrB/ptrB-ai-review.yaml`

involved_in GO:1900378 positive regulation of secondary metabolite biosynthetic process (IMP) on ptrB (PA0612) cites Wu and Jin 2005, which shows that PtrB represses the type III secretion system (deletion restores ExoS secretion and exoT transcription) and reports no secondary-metabolite phenotype. The supported term is negative regulation of protein secretion (GO:0050709; GO has no type III specific regulation term). This row is the sole seed of the PTN002215317 IBD (8 leaf IBAs).

> Therefore, PtrB is a new TTSS repressor that coordinates TTSS repression and pyocin synthesis under the stress of DNA damage.
> — PMID:16109947

## 95. WRONG_EVIDENCE_CODE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HU66 involved_in GO:0052837 thiazole biosynthetic process (IDA, PMID:9209060)
- **Field:** Evidence_Code
- **Change:** check ECO:0000314 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/thiI/thiI-ai-review.yaml`

involved_in GO:0052837 thiazole biosynthetic process (IDA) on PA5118 cites Webb, Claas & Downs 1997 (PMID:9209060), "Characterization of thiI, a new gene involved in thiazole biosynthesis in Salmonella typhimurium". The paper characterises the Salmonella thiI gene by mutant phenotype, mapping and sequencing; it contains no P. aeruginosa experiment, so it is not direct-assay evidence for PA5118. Either recode the row as ISS with the Salmonella ThiI accession in With/From, or delete it. This row is the only seed of the PANTHER IBD at PTN001804941, which propagates thiazole biosynthesis to 25 ThiI family members including Firmicutes and archaea whose ThiI is not needed for thiamine.

> Thiamine pyrophosphate (TPP) is a required cofactor in Salmonella typhimurium
> — PMID:9209060

## 96. WRONG_EVIDENCE_CODE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:P29364 enables GO:0004413 homoserine kinase activity (IDA, PMID:10220164)
- **Field:** Evidence_Code
- **Change:** check ECO:0000314 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/thrB/thrB-ai-review.yaml`

enables GO:0004413 (IDA) on PA5495 thrB cites Patte et al. 1999, whose abstract reports only genetics (thrB thrH double mutant auxotrophy, thrH complementation of E. coli thrB and serB mutants) and no homoserine kinase assay of ThrB. Please check whether the full text contains such an assay. If not, the activity is better supported by ISS/IBA to the type II HSK family (HAMAP MF_00301); the genetics support the process (IGI with thrH). This row is the sole seed of the PANTHER IBD at PTN001464661 and one of two at PTN001464650.

> In P. aeruginosa, threonine auxotrophy is observed only when both thrB and thrH are simultaneously inactivated.
> — PMID:10220164

## 97. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:P29364 involved_in GO:0009088 L-threonine biosynthetic process (IDA, PMID:10220164)
- **Field:** Evidence_Code
- **Change:** check ECO:0000314 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/thrB/thrB-ai-review.yaml`

involved_in GO:0009088 (IDA) on PA5495 thrB cites Patte et al. 1999, whose evidence for thrB is that threonine auxotrophy appears only in thrB thrH double mutants. That is a genetic interaction (IGI with thrH), not a direct assay. The annotation is correct.

> In P. aeruginosa, threonine auxotrophy is observed only when both thrB and thrH are simultaneously inactivated.
> — PMID:10220164

## 98. WRONG_TERM (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HUG6 involved_in GO:0009243 O antigen biosynthetic process (IMP, PMID:15838026)
- **Field:** GO_ID
- **Change:** check GO:0009243 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/waaL/waaL-ai-review.yaml`

waaL (PA4999) is annotated IMP to GO:0009243 O antigen biosynthetic process (PMID:15838026). WaaL ligates the completed, polymerized O antigen onto lipid A-core, a step of LPS assembly after O-chain synthesis; GO:0009103 lipopolysaccharide biosynthetic process is the more accurate process. Consider re-annotating. This row is the sole seed of the PAINT IBD for GO:0000271 at PTN008076295, which remains valid either way.

> The completed chains are covalently attached to lipid A core by the O-antigen ligase, WaaL.
> — PMID:15838026

## 99. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HUG6 involved_in GO:0009297 pilus assembly (IMP, PMID:15838026)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0009297
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/waaL/waaL-ai-review.yaml`

waaL (PA4999) is annotated IMP to GO:0009297 pilus assembly from PMID:15838026. The O-antigen ligase does not participate in pilus assembly; the twitching/pilus defect of the O-antigen-less mutant is an indirect envelope phenotype. Please remove (or capture as a phenotype rather than a GO process).

## 100. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HUG6 enables GO:0016874 ligase activity (IDA, PMID:17697256)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0016874
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/waaL/waaL-ai-review.yaml`

waaL (PA4999) is annotated IDA to GO:0016874 ligase activity citing PMID:17697256. WaaL is EC 2.4.99.26, an ATP-independent, metal-independent inverting glycosyltransferase (PMID:21983211, PMID:30047569); the ATP hydrolysis reported in 2007 was not reproduced. GO:0008754 O-antigen ligase activity (is_a glycosyltransferase activity) is the correct MF and is already annotated. Please delete the ligase activity row.

> E. coli and Pseudomonas aeruginosa WaaL proteins cannot catalyze ATP hydrolysis in vitro
> — PMID:21983211

## 101. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HUG6 involved_in GO:0043107 type IV pilus-dependent motility (IMP, PMID:15838026)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0043107
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/waaL/waaL-ai-review.yaml`

waaL (PA4999) is annotated IMP to GO:0043107 type IV pilus-dependent motility from PMID:15838026. The twitching defect of the O-antigen ligase mutant is an indirect consequence of altered LPS/envelope, not participation of WaaL in motility. Please remove.

## 102. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HUG6 involved_in GO:0044780 bacterial-type flagellum assembly (IMP, PMID:15838026)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0044780
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/waaL/waaL-ai-review.yaml`

waaL (PA4999) is annotated IMP to GO:0044780 bacterial-type flagellum assembly from PMID:15838026. Reduced flagellation of the O-antigen-less mutant is an indirect envelope phenotype; WaaL does not participate in flagellum assembly. Please remove.

## 103. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HUG6 involved_in GO:0071977 bacterial-type flagellum-dependent swimming motility (IMP, PMID:15838026)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0071977
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/waaL/waaL-ai-review.yaml`

waaL (PA4999) is annotated IMP to GO:0071977 bacterial-type flagellum-dependent swimming motility from PMID:15838026. The motility defect of the O-antigen ligase mutant is indirect (envelope/LPS), and waaL deletion in PA14 and PAK did not abolish swimming (PMID:29059582). Please remove.

## 104. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:G3XD01 involved_in GO:0006065 UDP-glucuronate biosynthetic process (EXP, PMID:16102001)
- **Field:** GO_ID
- **Change:** GO:0006065 → GO:0009226 (nucleotide-sugar biosynthetic process)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/wbpD/wbpD-ai-review.yaml`

wbpD (PA3156) is annotated EXP to GO:0006065 UDP-glucuronate biosynthetic process citing PMID:16102001. WbpD is the UDP-GlcNAc3NA 3-N-acetyltransferase (EC 2.3.1.201) of the UDP-ManNAc3NAcA pathway (UDP-GlcNAc -> UDP-GlcNAcA -> UDP-GlcNAc3NA -> UDP-GlcNAc3NAcA -> UDP-ManNAc3NAcA); UDP-glucuronate is not an intermediate. PMID:16102001 also had no substrate to assay. Please re-annotate to GO:0009226 nucleotide-sugar biosynthetic process (citing PMID:19282284 or PMID:19348502, where the reaction was demonstrated) and/or GO:0009243 O antigen biosynthetic process. This row is the sole seed of the PAINT IBD at PTN001292385 (8 leaf IBAs).

> As a substrate for studying the enzymatic activity of WbpD is unavailable at present
> — PMID:16102001

> we confirm that WbpD catalyzes the acetylation of UDP-GlcNAc(3NH(2))A to give UDP-GlcNAc(3NAc)A
> — PMID:19348502

## 105. WRONG_REFERENCE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HTB9 enables GO:0016757 glycosyltransferase activity (IMP, PMID:9680202)
- **Field:** DB:Reference
- **Change:** check PMID:9680202 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/wbpY/wbpY-ai-review.yaml`

GO:0016757 glycosyltransferase activity for wbpY (PA5448) is annotated IMP to PMID:9680202, where the activity was inferred from the A-band-negative mutant phenotype and sequence similarity (the abstract calls the linkage assignments probable/predicted). Direct evidence now exists in PMID:35166992, which shows recombinant WbpY transfers D-Rha from GDP-D-Rha in a1-3 linkage. Please add an IDA row citing PMID:35166992, preferably to GO:0016758 hexosyltransferase activity, and consider retiring the IMP MF row. This row seeds the PAINT IBD at PTN005302544.

> NMR spectroscopic analysis of the WbpY reaction product showed that WbpY transferred one D-Rha residue in α1-3 linkage
> — PMID:35166992

## 106. WRONG_EVIDENCE_CODE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:P35818 involved_in GO:0015628 protein secretion by the type II secretion system (IDA, PMID:9818381)
- **Field:** Evidence_Code
- **Change:** check ECO:0000314 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/xcpQ/xcpQ-ai-review.yaml`

GO:0015628 is annotated IDA to PMID:9818381 (Filloux, Michel and Bally 1998, FEMS Microbiol Rev), which PubMed types as a Review and whose abstract describes it as one. We have only the abstract, so we cannot tell whether the article reports original Xcp data from the authors' laboratory that would justify IDA. Please check; if it presents no new experiment, TAS (or a re-key to a primary paper as IMP or IDA) would be more accurate. The term itself is correct, and this row is a PAINT IBD seed, so any change should be coordinated with PAINT re-seeding.

## 107. WRONG_EVIDENCE_CODE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q00512 involved_in GO:0015628 protein secretion by the type II secretion system (IDA, PMID:9818381)
- **Field:** Evidence_Code
- **Change:** check ECO:0000314 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/xcpR/xcpR-ai-review.yaml`

GO:0015628 is annotated IDA to PMID:9818381 (Filloux, Michel and Bally 1998, FEMS Microbiol Rev), which PubMed types as a Review and whose abstract describes it as one. We have only the abstract, so we cannot tell whether the article reports original Xcp data from the authors' laboratory that would justify IDA. Please check; if it presents no new experiment, TAS (or a re-key to a primary paper as IMP or IDA) would be more accurate. The term itself is correct, and this row is a PAINT IBD seed, so any change should be coordinated with PAINT re-seeding.

## 108. WRONG_EVIDENCE_CODE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q00513 involved_in GO:0015628 protein secretion by the type II secretion system (IDA, PMID:9818381)
- **Field:** Evidence_Code
- **Change:** check ECO:0000314 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/xcpS/xcpS-ai-review.yaml`

GO:0015628 is annotated IDA to PMID:9818381 (Filloux, Michel and Bally 1998, FEMS Microbiol Rev), which PubMed types as a Review and whose abstract describes it as one. We have only the abstract, so we cannot tell whether the article reports original Xcp data from the authors' laboratory that would justify IDA. Please check; if it presents no new experiment, TAS (or a re-key to a primary paper as IMP or IDA) would be more accurate. The term itself is correct, and this row is a PAINT IBD seed, so any change should be coordinated with PAINT re-seeding.

> In this review, we will use the P. aeruginosa Xcp system as a basis
> — PMID:9818381

## 109. WRONG_REFERENCE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q00516 part_of GO:0015627 type II protein secretion system complex (IDA, PMID:8331069)
- **Field:** Reference
- **Change:** check PMID:8331069 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/xcpV/xcpV-ai-review.yaml`

GO:0015627 for XcpV (PA3099, Q00516) is annotated IDA to PMID:8331069 (Nunn and Lory 1993). The abstract reports PilD cleavage, N-methylation and inner-membrane fractionation of XcpT-W, which directly support plasma membrane (already annotated EXP from the same paper) rather than membership of the T2SS complex. Complex membership is directly shown by co-purification of the XcpU-V-W-X tip complex (PMID:19828448, Douzi et al. 2009). The term is correct; please check the full text and, if it does not assay complex membership, re-key the row to PMID:19828448. This row is the sole seed of the PAINT IBD at PTN002446181.

> Analysis of cellular fractions from wild-type and pilD mutant strains of P. aeruginosa showed that the precursor forms of XcpT-W are located predominantly in the bacterial inner membrane
> — PMID:8331069

## 110. WRONG_EVIDENCE_CODE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q00516 involved_in GO:0015628 protein secretion by the type II secretion system (IDA, PMID:9818381)
- **Field:** Evidence_Code
- **Change:** check ECO:0000314 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/xcpV/xcpV-ai-review.yaml`

GO:0015628 is annotated IDA to PMID:9818381 (Filloux, Michel and Bally 1998, FEMS Microbiol Rev), which PubMed types as a Review and whose abstract describes it as one. We have only the abstract, so we cannot tell whether the article reports original Xcp data from the authors' laboratory that would justify IDA. Please check; if it presents no new experiment, TAS (or a re-key to a primary paper as IMP or IDA) would be more accurate. The term itself is correct, and this row is a PAINT IBD seed, so any change should be coordinated with PAINT re-seeding.

> In this review, we will use the P. aeruginosa Xcp system as a basis
> — PMID:9818381

## 111. WRONG_REFERENCE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q00517 part_of GO:0015627 type II protein secretion system complex (IDA, PMID:8331069)
- **Field:** Reference
- **Change:** check PMID:8331069 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/xcpW/xcpW-ai-review.yaml`

GO:0015627 for XcpW (PA3098, Q00517) is annotated IDA to PMID:8331069 (Nunn and Lory 1993). The abstract reports PilD cleavage, N-methylation and inner-membrane fractionation of XcpT-W, which directly support plasma membrane (already annotated EXP from the same paper) rather than membership of the T2SS complex. Complex membership is directly shown by co-purification of the XcpU-V-W-X tip complex (PMID:19828448, Douzi et al. 2009). The term is correct; please check the full text and, if it does not assay complex membership, re-key the row to PMID:19828448. This row seeds the PAINT IBD at PTN002446812; the IBD conclusion is sound.

> Analysis of cellular fractions from wild-type and pilD mutant strains of P. aeruginosa showed that the precursor forms of XcpT-W are located predominantly in the bacterial inner membrane
> — PMID:8331069

## 112. WRONG_EVIDENCE_CODE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q00517 involved_in GO:0015628 protein secretion by the type II secretion system (IDA, PMID:9818381)
- **Field:** Evidence_Code
- **Change:** check ECO:0000314 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/xcpW/xcpW-ai-review.yaml`

GO:0015628 is annotated IDA to PMID:9818381 (Filloux, Michel and Bally 1998, FEMS Microbiol Rev), which PubMed types as a Review and whose abstract describes it as one. We have only the abstract, so we cannot tell whether the article reports original Xcp data from the authors' laboratory that would justify IDA. Please check; if it presents no new experiment, TAS (or a re-key to a primary paper as IMP or IDA) would be more accurate. The term itself is correct, and this row is a PAINT IBD seed, so any change should be coordinated with PAINT re-seeding.

> In this review, we will use the P. aeruginosa Xcp system as a basis
> — PMID:9818381

## 113. WRONG_EVIDENCE_CODE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q00518 involved_in GO:0015628 protein secretion by the type II secretion system (IDA, PMID:9818381)
- **Field:** Evidence_Code
- **Change:** check ECO:0000314 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/xcpX/xcpX-ai-review.yaml`

GO:0015628 is annotated IDA to PMID:9818381 (Filloux, Michel and Bally 1998, FEMS Microbiol Rev), which PubMed types as a Review and whose abstract describes it as one. We have only the abstract, so we cannot tell whether the article reports original Xcp data from the authors' laboratory that would justify IDA. Please check; if it presents no new experiment, TAS (or a re-key to a primary paper as IMP or IDA) would be more accurate. The term itself is correct, and this row is a PAINT IBD seed, so any change should be coordinated with PAINT re-seeding.

> In this review, we will use the P. aeruginosa Xcp system as a basis
> — PMID:9818381

## 114. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HT73 involved_in GO:0010043 response to zinc ion (IMP, PMID:24086521)
- **Change:** GO:0010043 → GO:0071578 (zinc ion import across plasma membrane)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/znuC/znuC-ai-review.yaml`

PseudoCAP annotates znuC (PA5500, UniProtKB:Q9HT73) with GO:0010043 response to zinc ion, IMP, from PMID:24086521. The supporting experiment is a growth defect of the znuC deletion in LB + 0.5 mM EDTA. ZnuC is the ATPase subunit of the ZnuABC zinc importer, so the process it takes part in is zinc import across the plasma membrane (GO:0071578); the zinc-sensing "response" in that paper belongs to Zur (Np20, PA5499), which is annotated separately and correctly. This row is the sole seed of the PAINT IBD at PTN001952271, from which 1455 GOA rows now descend, so the term choice propagates widely. The same re-pointing would apply to the paper's companion rows on znuB (Q9HT72) and PA5498 (Q9HT75).

> Putative znuA, znuB, and znuC genes are required for wild-type level growth in low zinc conditions.
> — PMID:24086521
