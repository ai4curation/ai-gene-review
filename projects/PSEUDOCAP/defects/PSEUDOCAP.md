# Source-record defects for PSEUDOCAP

282 open defect(s), generated from `source_defects` blocks in this repository's reviews. Do not edit by hand.

## 1. WRONG_EVIDENCE_CODE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I5N4 part_of GO:0098046 type V protein secretion system complex (IMP, PMID:25009238)
- **Field:** Evidence_Code
- **Change:** check ECO:0000315 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA0692/PA0692-ai-review.yaml`

GO:0098046 type V protein secretion system complex for PA0692 (PdtB, Q9I5N4) is annotated IMP to PMID:25009238. The abstract reports a mutant export defect (PdtA transport depends on PdtB), which supports the process GO:0046819 but not complex membership or location. If the full text localizes PdtB (e.g. outer-membrane fractionation), change the evidence to IDA; otherwise use IC from the IMP process row or ISS from TpsB homologs. This row is the sole seed of the PAINT IBD at PTN002160772 (25 leaf IBAs); the IBD conclusion is sound by family, so only the seed evidence needs attention.

> the transport of PdtA is strictly dependent on the production of PdtB
> — PMID:25009238

## 2. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I596 involved_in GO:0051872 sphingosine catabolic process (IDA, PMID:24465209)
- **Field:** GO_ID
- **Change:** GO:0051872 → GO:0046514 (ceramide catabolic process)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA0845/PA0845-ai-review.yaml`

The PseudoCAP IDA row codes cerN (PA0845) to GO:0051872 sphingosine catabolic process from PMID:24465209 (full text read). cerN is the neutral ceramidase that hydrolyses ceramide to sphingosine; it produces sphingosine and sits upstream of the SphR-induced sph genes (sphA/sphBCD) that catabolise sphingosine. cerN does not perform a step of sphingosine catabolism. The reaction it performs is ceramide catabolism. Requested change: re-point to GO:0046514 ceramide catabolic process.

> we generated a clean deletion in the neutral ceramidase encoded by PA0845 and measured enzyme activity from the PA5325-lacZ reporter construct pAL4. Ceramide fails to induce PA5325-lacZ in the absence of the neutral ceramidase
> — PMID:24465209

## 3. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I551 involved_in GO:0001896 autolysis (IMP, PMID:26100878)
- **Change:** GO:0001896 → GO:0043069 (negative regulation of programmed cell death)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA0906/PA0906-ai-review.yaml`

GO:0001896 autolysis (IMP, PMID:26100878) for PA0906 (alpR, Q9I551) records lysis after AlpR depletion or cleavage. AlpR is the repressor of the alp lysis genes, which execute lysis; it is a negative regulator of the process, not a participant. Repoint to GO:0043069 negative regulation of programmed cell death (or to a regulation-of-autolysis term if GO adds one).

> Cleavage of AlpR triggers a cell lysis program through de-repression of the alpA gene
> — PMID:26100878

## 4. WRONG_TERM (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I537 involved_in GO:0055091 phospholipid homeostasis (IDA, PMID:26261323)
- **Change:** GO:0055091 → GO:0008654 (phospholipid biosynthetic process)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA0920/PA0920-ai-review.yaml`

GO:0055091 phospholipid homeostasis for PA0920 (Q9I537) is annotated IDA to PMID:26261323. Its abstract reports the crystal structure and in vitro substrate recognition of the A-PGS catalytic domain and describes no homeostasis assay (full text not read), and the gene performs a biosynthetic step (alanylation of PG). Repoint to GO:0008654 phospholipid biosynthetic process; PMID:19087229 (deletion abolishes A-PG, expression in E. coli confers it) is stronger support for the process. This row is the sole seed of the PAINT IBD at PTN002162750.

> The P. aeruginosa deletion mutant DeltaPA0920 failed to synthesize A-PG.
> — PMID:19087229

## 5. WRONG_EVIDENCE_CODE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I520 located_in GO:0005886 plasma membrane (IDA, PMID:23955007)
- **Field:** Evidence_Code
- **Change:** check ECO:0000314 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA0938/PA0938-ai-review.yaml`

The abstract of PMID:23955007 reports Iap genetics in wzz single and double mutants, sequence alignment of Iap with the first TM segment of Wzz1 and Wzz2, and topology predictions of Iap. It describes no fractionation or imaging of Wzz2, so the plasma-membrane IDA (and the membrane IDA from the same paper) may rest on sequence analysis (ISS/ISM). Only the abstract was read, hence SUSPECTED and CHECK. The location itself is correct.

## 6. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I520 located_in GO:0009276 Gram-negative-bacterium-type cell wall (IDA, PMID:24309320)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0009276
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA0938/PA0938-ai-review.yaml`

Full text of PMID:24309320 read. It is a site-directed mutagenesis study of the Wzy polymerase; Wzz1 and Wzz2 appear as chain-length readouts and as mCherry fusions used for complementation. No experiment localises Wzz2 to the peptidoglycan layer (GO:0009276 Gram-negative-bacterium-type cell wall), and Wzz2 is an integral inner-membrane protein. Please delete the row; the plasma-membrane rows already capture the location.

## 7. WRONG_REFERENCE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I509 enables GO:0016655 oxidoreductase activity, acting on NAD(P)H, quinone or similar compound as acceptor (IDA, PMID:16672604)
- **Field:** Reference
- **Change:** check PMID:16672604 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA0949/PA0949-ai-review.yaml`

GO:0016655 IDA on PA0949 (Q9I509) cites PMID:16672604, which biochemically characterises only E. coli and A. fulgidus WrbA (full text read). P. aeruginosa WrbA appears only as a previously solved crystal structure. Please either re-point the IDA to PMID:25085734, where the purified P. aeruginosa enzyme was assayed (and use GO:0003955), or change the evidence to ISS with E. coli WrbA (P0A8G6).

> The presence of this fold has recently been confirmed in the published crystal structures of the Deinococcus radiodurans and Pseudomonas aeruginosa WrbA homologues
> — PMID:16672604

## 8. WRONG_EVIDENCE_CODE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I4V9 enables GO:0008919 lipopolysaccharide glucosyltransferase I activity (IDA, PMID:21441506)
- **Field:** Evidence_Code
- **Change:** check ECO:0000314 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA1014/PA1014-ai-review.yaml`

The abstract of PMID:21441506 reports a chromosomal mutant whose core lacks the terminal glucose (NMR and MS), complementation, and heterologous expression in other serotypes, and concludes that the results "strongly suggested" a 1,2-glucosyltransferase. No in vitro transfer assay is described, so IMP looks like the right code. Only the abstract was read; the full text could contain a direct assay, hence SUSPECTED and CHECK. The GO term itself is sound.

## 9. WRONG_QUALIFIER (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I4S0 enables GO:0015385 sodium:proton antiporter activity (IMP, PMID:16030218)
- **Field:** Qualifier
- **Change:** enables → contributes_to
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA1054/PA1054-ai-review.yaml`

PA1054 (ShaAB) is the large subunit of the six-subunit Sha/Mrp Na+/H+ antiporter. The IMP evidence (PMID:16030218) is sound: the cluster lacking PA1054 does not restore antiport. But no Mrp antiporter shows activity with MrpA alone, and antiport requires the hetero-oligomeric complex, so the subunit contributes to GO:0015385 rather than enabling it alone.

> In previous studies, none of the Mrp antiporters exhibited antiport activity with MrpA or MrpD alone.
> — PMID:29218041

## 10. WRONG_EVIDENCE_CODE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I4R9 enables GO:0015385 sodium:proton antiporter activity (IMP, PMID:16030218)
- **Field:** Evidence_Code
- **Change:** check ECO:0000315 (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/PSEAE/PA1055/PA1055-ai-review.yaml`

enables GO:0015385 sodium:proton antiporter activity (IMP) on PA1055 cites Kosono et al. 2005 (PMID:16030218). The abstract reports a disruption of PA1054 only, and complementation of E. coli TO114 by the whole PA1054-PA1059 cluster. The full text (supplied by the user, read 2026-11-05) confirms that the only sha mutant constructed is the PA1054 insertion; there is no PA1055 mutant, so IMP does not apply to PA1055. If the antiport was measured in membranes of TO114 carrying the cluster, IDA (as contributes_to) would fit; if only growth complementation, IGI. The full text shows both, with antiport measured in everted membrane vesicles of TO114 carrying the cluster. This row is the sole seed of the PAINT IBD at PTN002160376 (24 leaf IBAs).

> We disrupted PA1054 (a shaA homologue gene) and determined its effect on Na+ tolerance during growth, Na+ efflux, and pathogenicity in mice.
> — PMID:16030218

## 11. WRONG_QUALIFIER (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I4R9 enables GO:0015385 sodium:proton antiporter activity (IMP, PMID:16030218)
- **Field:** Qualifier
- **Change:** enables → contributes_to
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA1055/PA1055-ai-review.yaml`

PA1055 (ShaC) is one of six subunits of the Sha/Mrp Na+/H+ antiporter. Mrp antiport requires the hetero-oligomeric complex of all subunits, so the subunit contributes to GO:0015385 rather than enabling it alone.

> Antiport activity requires hetero-oligomeric complexes of all six or seven hydrophobic Mrp proteins (MrpA-MrpG).
> — PMID:20624916

## 12. WRONG_EVIDENCE_CODE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I4R9 involved_in GO:0035725 sodium ion transmembrane transport (IMP, PMID:16030218)
- **Field:** Evidence_Code
- **Change:** check ECO:0000315 (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/PSEAE/PA1055/PA1055-ai-review.yaml`

involved_in GO:0035725 sodium ion transmembrane transport (IMP) on PA1055 cites Kosono et al. 2005 (PMID:16030218), which reports a mutant of PA1054 only (reduced Na+ efflux) and complementation of E. coli TO114 by the whole PA1054-PA1059 cluster. The full text (read 2026-11-05) confirms there is no PA1055 mutant; the only sha mutant constructed is the PA1054 insertion. Please check the evidence code (IGI or IDA for the cluster-level data). The process itself is appropriate for this subunit.

> Disruption of PA1054 resulted in severe Na+ sensitivity during growth and decreased Na+ efflux activity.
> — PMID:16030218

## 13. WRONG_EVIDENCE_CODE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I4R8 enables GO:0015385 sodium:proton antiporter activity (IMP, PMID:16030218)
- **Field:** Evidence_Code
- **Change:** check ECO:0000315 (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/PSEAE/PA1056/PA1056-ai-review.yaml`

enables GO:0015385 sodium:proton antiporter activity (IMP) on PA1056 cites Kosono et al. 2005 (PMID:16030218). The abstract reports a disruption of PA1054 only, and complementation of E. coli TO114 by the whole PA1054-PA1059 cluster. The full text (supplied by the user, read 2026-11-05) confirms that the only sha mutant constructed is the PA1054 insertion; there is no PA1056 mutant, so IMP does not apply to PA1056. If the antiport was measured in membranes of TO114 carrying the cluster, IDA (as contributes_to) would fit; if only growth complementation, IGI. The full text shows both, with antiport measured in everted membrane vesicles of TO114 carrying the cluster. This row is one of two seeds of the PAINT IBD at PTN001865541 (16 leaf IBAs).

> We disrupted PA1054 (a shaA homologue gene) and determined its effect on Na+ tolerance during growth, Na+ efflux, and pathogenicity in mice.
> — PMID:16030218

## 14. WRONG_QUALIFIER (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I4R8 enables GO:0015385 sodium:proton antiporter activity (IMP, PMID:16030218)
- **Field:** Qualifier
- **Change:** enables → contributes_to
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA1056/PA1056-ai-review.yaml`

PA1056 (ShaD) is one of six subunits of the Sha/Mrp Na+/H+ antiporter. No Mrp antiporter shows antiport with MrpD alone, so the subunit contributes to GO:0015385 rather than enabling it alone.

> In previous studies, none of the Mrp antiporters exhibited antiport activity with MrpA or MrpD alone.
> — PMID:29218041

## 15. WRONG_EVIDENCE_CODE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I4R8 involved_in GO:0035725 sodium ion transmembrane transport (IMP, PMID:16030218)
- **Field:** Evidence_Code
- **Change:** check ECO:0000315 (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/PSEAE/PA1056/PA1056-ai-review.yaml`

involved_in GO:0035725 sodium ion transmembrane transport (IMP) on PA1056 cites Kosono et al. 2005 (PMID:16030218), which reports a mutant of PA1054 only (reduced Na+ efflux) and complementation of E. coli TO114 by the whole PA1054-PA1059 cluster. The full text (read 2026-11-05) confirms there is no PA1056 mutant; the only sha mutant constructed is the PA1054 insertion. Please check the evidence code (IGI or IDA for the cluster-level data). The process itself is appropriate for this subunit.

> Disruption of PA1054 resulted in severe Na+ sensitivity during growth and decreased Na+ efflux activity.
> — PMID:16030218

## 16. WRONG_EVIDENCE_CODE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I4R7 enables GO:0015385 sodium:proton antiporter activity (IMP, PMID:16030218)
- **Field:** Evidence_Code
- **Change:** check ECO:0000315 (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/PSEAE/PA1057/PA1057-ai-review.yaml`

enables GO:0015385 sodium:proton antiporter activity (IMP) on PA1057 cites Kosono et al. 2005 (PMID:16030218). The abstract reports a disruption of PA1054 only, and complementation of E. coli TO114 by the whole PA1054-PA1059 cluster. The full text (supplied by the user, read 2026-11-05) confirms that the only sha mutant constructed is the PA1054 insertion; there is no PA1057 mutant, so IMP does not apply to PA1057. If the antiport was measured in membranes of TO114 carrying the cluster, IDA (as contributes_to) would fit; if only growth complementation, IGI. The full text shows both, with antiport measured in everted membrane vesicles of TO114 carrying the cluster. This row is the sole seed of the PAINT IBD at PTN002160407 (20 leaf IBAs).

> We disrupted PA1054 (a shaA homologue gene) and determined its effect on Na+ tolerance during growth, Na+ efflux, and pathogenicity in mice.
> — PMID:16030218

## 17. WRONG_QUALIFIER (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I4R7 enables GO:0015385 sodium:proton antiporter activity (IMP, PMID:16030218)
- **Field:** Qualifier
- **Change:** enables → contributes_to
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA1057/PA1057-ai-review.yaml`

PA1057 (ShaE) is one of six subunits of the Sha/Mrp Na+/H+ antiporter. Mrp antiport requires the hetero-oligomeric complex, and MrpE acts in complex assembly, so the subunit contributes to GO:0015385 rather than enabling it alone.

> The results extended indications that MrpE is required for normal membrane levels of other Mrp proteins and for complex formation.
> — PMID:20624916

## 18. WRONG_EVIDENCE_CODE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I4R7 involved_in GO:0035725 sodium ion transmembrane transport (IMP, PMID:16030218)
- **Field:** Evidence_Code
- **Change:** check ECO:0000315 (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/PSEAE/PA1057/PA1057-ai-review.yaml`

involved_in GO:0035725 sodium ion transmembrane transport (IMP) on PA1057 cites Kosono et al. 2005 (PMID:16030218), which reports a mutant of PA1054 only (reduced Na+ efflux) and complementation of E. coli TO114 by the whole PA1054-PA1059 cluster. The full text (read 2026-11-05) confirms there is no PA1057 mutant; the only sha mutant constructed is the PA1054 insertion. Please check the evidence code (IGI or IDA for the cluster-level data). The process itself is appropriate for this subunit.

> Disruption of PA1054 resulted in severe Na+ sensitivity during growth and decreased Na+ efflux activity.
> — PMID:16030218

## 19. WRONG_EVIDENCE_CODE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I4R6 enables GO:0015385 sodium:proton antiporter activity (IMP, PMID:16030218)
- **Field:** Evidence_Code
- **Change:** check ECO:0000315 (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/PSEAE/PA1058/PA1058-ai-review.yaml`

enables GO:0015385 sodium:proton antiporter activity (IMP) on PA1058 cites Kosono et al. 2005 (PMID:16030218). The abstract reports a disruption of PA1054 only, and complementation of E. coli TO114 by the whole PA1054-PA1059 cluster. The full text (supplied by the user, read 2026-11-05) confirms that the only sha mutant constructed is the PA1054 insertion; there is no PA1058 mutant, so IMP does not apply to PA1058. If the antiport was measured in membranes of TO114 carrying the cluster, IDA (as contributes_to) would fit; if only growth complementation, IGI. The full text shows both, with antiport measured in everted membrane vesicles of TO114 carrying the cluster. This row is the sole seed of the PAINT IBD at PTN002162906 (19 GO_Central leaf IBAs).

> We disrupted PA1054 (a shaA homologue gene) and determined its effect on Na+ tolerance during growth, Na+ efflux, and pathogenicity in mice.
> — PMID:16030218

## 20. WRONG_QUALIFIER (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I4R6 enables GO:0015385 sodium:proton antiporter activity (IMP, PMID:16030218)
- **Field:** Qualifier
- **Change:** enables → contributes_to
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA1058/PA1058-ai-review.yaml`

PA1058 (ShaF) is one of six subunits of the Sha/Mrp Na+/H+ antiporter. Mrp antiport requires the hetero-oligomeric complex of all subunits, so the subunit contributes to GO:0015385 rather than enabling it alone.

> Antiport activity requires hetero-oligomeric complexes of all six or seven hydrophobic Mrp proteins (MrpA-MrpG).
> — PMID:20624916

## 21. WRONG_EVIDENCE_CODE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I4R6 involved_in GO:0035725 sodium ion transmembrane transport (IMP, PMID:16030218)
- **Field:** Evidence_Code
- **Change:** check ECO:0000315 (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/PSEAE/PA1058/PA1058-ai-review.yaml`

involved_in GO:0035725 sodium ion transmembrane transport (IMP) on PA1058 cites Kosono et al. 2005 (PMID:16030218), which reports a mutant of PA1054 only (reduced Na+ efflux) and complementation of E. coli TO114 by the whole PA1054-PA1059 cluster. The full text (read 2026-11-05) confirms there is no PA1058 mutant; the only sha mutant constructed is the PA1054 insertion. Please check the evidence code (IGI or IDA for the cluster-level data). The process itself is appropriate for this subunit.

> Disruption of PA1054 resulted in severe Na+ sensitivity during growth and decreased Na+ efflux activity.
> — PMID:16030218

## 22. WRONG_EVIDENCE_CODE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I4R5 enables GO:0015385 sodium:proton antiporter activity (IMP, PMID:16030218)
- **Field:** Evidence_Code
- **Change:** check ECO:0000315 (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/PSEAE/PA1059/PA1059-ai-review.yaml`

enables GO:0015385 sodium:proton antiporter activity (IMP) on PA1059 cites Kosono et al. 2005 (PMID:16030218). The abstract reports a disruption of PA1054 only, and complementation of E. coli TO114 by the whole PA1054-PA1059 cluster. The full text (supplied by the user, read 2026-11-05) confirms that the only sha mutant constructed is the PA1054 insertion; there is no PA1059 mutant, so IMP does not apply to PA1059. If the antiport was measured in membranes of TO114 carrying the cluster, IDA (as contributes_to) would fit; if only growth complementation, IGI. The full text shows both, with antiport measured in everted membrane vesicles of TO114 carrying the cluster. This row is the sole seed of the PAINT IBD at PTN002162936 (19 GO_Central leaf IBAs).

> We disrupted PA1054 (a shaA homologue gene) and determined its effect on Na+ tolerance during growth, Na+ efflux, and pathogenicity in mice.
> — PMID:16030218

## 23. WRONG_QUALIFIER (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I4R5 enables GO:0015385 sodium:proton antiporter activity (IMP, PMID:16030218)
- **Field:** Qualifier
- **Change:** enables → contributes_to
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA1059/PA1059-ai-review.yaml`

PA1059 (ShaG) is one of six subunits of the Sha/Mrp Na+/H+ antiporter. Mrp antiport requires the hetero-oligomeric complex of all subunits, so the subunit contributes to GO:0015385 rather than enabling it alone.

> Antiport activity requires hetero-oligomeric complexes of all six or seven hydrophobic Mrp proteins (MrpA-MrpG).
> — PMID:20624916

## 24. WRONG_EVIDENCE_CODE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I4R5 involved_in GO:0035725 sodium ion transmembrane transport (IMP, PMID:16030218)
- **Field:** Evidence_Code
- **Change:** check ECO:0000315 (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/PSEAE/PA1059/PA1059-ai-review.yaml`

involved_in GO:0035725 sodium ion transmembrane transport (IMP) on PA1059 cites Kosono et al. 2005 (PMID:16030218), which reports a mutant of PA1054 only (reduced Na+ efflux) and complementation of E. coli TO114 by the whole PA1054-PA1059 cluster. The full text (read 2026-11-05) confirms there is no PA1059 mutant; the only sha mutant constructed is the PA1054 insertion. Please check the evidence code (IGI or IDA for the cluster-level data). The process itself is appropriate for this subunit.

> Disruption of PA1054 resulted in severe Na+ sensitivity during growth and decreased Na+ efflux activity.
> — PMID:16030218

## 25. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I4D4 enables GO:0003955 NAD(P)H dehydrogenase (quinone) activity (IMP, PMID:25085734)
- **Field:** Evidence_Code
- **Change:** IMP → IDA
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA1204/PA1204-ai-review.yaml`

PseudoCAP row for PA1204 (Q9I4D4), GO:0003955 NAD(P)H dehydrogenase (quinone) activity, IMP, PMID:25085734 (Green et al. 2014). The abstract states that each of the five quinone oxidoreductase orthologs reduced quinone substrates in in vitro assays; the only genetic experiments reported are overexpression growth tests under H2O2, which bear on oxidative-stress defence, not on the enzyme activity. The term is correct, but the evidence is a direct assay (IDA). Abstract-only reading; the full text could describe a mutant assay, which the abstract does not mention.

> In in vitro assays, each enzyme was shown to reduce quinone substrates with only minimal semiquinone formation.
> — PMID:25085734

## 26. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I4D4 enables GO:0016655 oxidoreductase activity, acting on NAD(P)H, quinone or similar compound as acceptor (IDA, PMID:24915188)
- **Field:** Evidence_Code
- **Change:** IDA → TAS
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA1204/PA1204-ai-review.yaml`

PseudoCAP row for PA1204 (Q9I4D4), GO:0016655, IDA, PMID:24915188 (Ryan et al. 2014). The cached full text assays three azoreductases (paAzoR1-3); PA1204 appears in the phylogeny, the structural overlay and the sentence quoted below, which attributes its quinone reductase activity to reference 75. That is a traceable author statement, not a direct assay. Requested change: evidence code TAS, or repoint the row to the primary paper (probably PMID:25085734, already annotated). PROBABLE because the experimental tables were read in extracted form only.

> Recent data have shown that PA0949, PA1204, PA2580 and PA4975, have NAD(P)H quinone oxidoreductase activities [75].
> — PMID:24915188

## 27. WRONG_EVIDENCE_CODE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I404 involved_in GO:0006868 L-glutamine transport (IMP, PMID:18310026)
- **Field:** Evidence_Code
- **Change:** check ECO:0000315 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA1340/PA1340-ai-review.yaml`

GO:0006868 L-glutamine transport for PA1340 (Q9I404) is annotated IMP to PMID:18310026. That paper is about Pseudomonas putida KT2440: it describes the AatJMQP operon PP1071-PP1068 and mutants of the binding protein (aatJ) and ATPase (aatP). The abstract describes no P. aeruginosa mutant and no permease mutant, so IMP is unlikely to apply to PA1340 (full text not read). At most this supports an ISS/ISO from the P. putida AatM ortholog, and even there the Gln growth defect concerns the binding protein, which binds Gln only weakly. PA1340's own glutamine phenotype is already captured by the GO:1903803 IMP to PMID:18833300, so the row could be deleted or recoded. This row is the sole seed of the PAINT IBD at PTN000764525.

> The system (AatJMQP, for acidic amino acid transport) is encoded by an operon involving genes PP1071-PP1068.
> — PMID:18310026

## 28. OTHER (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I1Y2 involved_in GO:1900191 negative regulation of single-species biofilm formation (IMP, PMID:16186483)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:1900191
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA2133/PA2133-ai-review.yaml`

The PseudoCAP IMP of GO:1900191 to PA2133 from PMID:16186483 (Hickman et al. 2005) rests only on plasmid expression of PA2133, used as a tool to deplete c-di-GMP and test the Wsp model. The paper states that a PA2133 mutant resembles wild type in attachment assays. An overexpression-as-tool phenotype is not evidence for the gene's own role in biofilm regulation. Please delete the row. PA2133 seeds PTN009140332 with this row, but the IBD also rests on bifA (Q9HW35, deletion plus complementation, PMID:17586641), E. coli PdeF and arr, so no change to the IBD is requested.

> A PA2133 mutant resembled the wild type in attachment assays.
> — PMID:16186483

## 29. WRONG_REFERENCE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I1J5 enables GO:0016655 oxidoreductase activity, acting on NAD(P)H, quinone or similar compound as acceptor (IDA, PMID:22304305)
- **Change:** PMID:22304305 → PMID:26621870
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA2280/PA2280-ai-review.yaml`

GO:0016655 for PA2280 (Q9I1J5, ArsH) is annotated IDA to PMID:22304305, which reports the purification and kinetics of Synechocystis sp. PCC 6803 ArsH; the abstract gives no indication that the P. aeruginosa protein was assayed. Re-cite the row to PMID:26621870 (Crescente et al. 2016), which assayed recombinant P. aeruginosa ArsH (pa2280) and found NAD(P)H quinone oxidoreductase and azoreductase activity, and consider GO:0003955. This row is the sole seed of the PAINT IBD at PTN008682975.

> Here we have expressed and purified Synechocystis ArsH and conducted an intensive biochemical study.
> — PMID:22304305

## 30. WRONG_EVIDENCE_CODE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I0Q6 enables GO:0003955 NAD(P)H dehydrogenase (quinone) activity (IMP, PMID:25085734)
- **Field:** Evidence_Code
- **Change:** ECO:0000315 → ECO:0000314
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA2580/PA2580-ai-review.yaml`

enables GO:0003955 NAD(P)H dehydrogenase (quinone) activity on PA2580 cites Green et al. 2014, whose evidence for the activity is in vitro assays of the purified enzyme. That is IDA. The abstract reports no PA2580 mutant (full text not read), and the overexpression experiments address H2O2 tolerance, not the activity. The row is a seed of the PTN002922793 IBD.

> In in vitro assays, each enzyme was shown to reduce quinone substrates with only minimal semiquinone formation.
> — PMID:25085734

## 31. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HZG1 involved_in GO:0009252 peptidoglycan biosynthetic process (IDA, PMID:25495032)
- **Field:** GO_ID
- **Change:** GO:0009252 → GO:0000270
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA3047/PA3047-ai-review.yaml`

involved_in GO:0009252 peptidoglycan biosynthetic process on PA3047 (PBP4) cites Lee et al. 2015 (PMID:25495032). Full text read. The experiments are in vitro hydrolysis of synthetic stem-pentapeptide and 4,3-cross-linked muropeptides by purified PBP4, plus muropeptide profiling after cefoxitin induction; no biosynthetic step is measured. The supported process is GO:0000270 peptidoglycan metabolic process (or a hydrolytic/remodelling child). PROBABLE rather than CONFIRMED because GO practice sometimes places PBP DD-carboxypeptidases under biosynthesis as sacculus maturation, a convention a curator might defend. The PTN000768632 GO:0000270 IBD does not depend on this row: it stands on E. coli DacB and PAINT already generalised the seed to the parent term.

> PBP4 is a bifunctional enzyme having both dd-carboxypeptidase and endopeptidase activities.
> — PMID:25495032

## 32. WRONG_TERM (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HXU3 involved_in GO:0080164 regulation of nitric oxide metabolic process (IMP, PMID:18043907)
- **Field:** GO_ID
- **Change:** check GO:0080164 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/PA3697/PA3697-ai-review.yaml`

involved_in GO:0080164 regulation of nitric oxide metabolic process (IMP, PMID:18043907) on PA3697. The abstract reports that PA3697 mutants lose nitrate- and nitrite-induced fhp promoter activity; no NO measurement is described. Please check whether the full text measures NO consumption or NO levels in the mutant. If it does not, the row overstates the evidence: the phenotype is reduced fhp expression, and the mechanism (direct promoter binding or an indirect effect) is unknown. This row is the sole seed of the PANTHER IBD at PTN002422332, which spreads the claim to about 175 proteins.

> Both PA0779 and PA3697 were found to be essential for NO3(-) and NO2(-) induced Pfhp activity under aerobic and low-oxygen conditions
> — PMID:18043907

## 33. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HXC2 enables GO:0031459 ABC-type glycine betaine transporter activity (IDA, PMID:17660277)
- **Field:** Evidence_Code
- **Change:** check ECO:0000314 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA3891/PA3891-ai-review.yaml`

GO:0031459 ABC-type glycine betaine transporter activity for PA3891 (Q9HXC2) is annotated IDA to PMID:17660277 (Chen and Beattie 2007). In that paper PA3891 was only recovered as a PAO1 genomic clone that restored growth of a P. syringae DC3000 opuCA-deficient mutant on 0.5 M NaCl with betaine or choline. No transport, binding or ATPase assay was done with PA3891, and glycine betaine specificity was shown for the DC3000 ortholog (Q87WH5). IGI (functional complementation) or ISS with UniProtKB:Q87WH5 would be accurate. This row is the sole seed of the PAINT IBD at PTN001953060 (about 23 leaf IBAs), so coordinate any change with PAINT re-seeding.

> the transformants were plated on MinA media containing 0.5 M NaCl and either glycine betaine or choline (2 mM)
> — PMID:17660277

## 34. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HXC2 part_of GO:0043190 ATP-binding cassette (ABC) transporter complex (IDA, PMID:17660277)
- **Field:** Evidence_Code
- **Change:** check ECO:0000314 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA3891/PA3891-ai-review.yaml`

GO:0043190 ATP-binding cassette (ABC) transporter complex for PA3891 (Q9HXC2) is annotated IDA to PMID:17660277. The paper does not purify, cross-link or co-localise any PA3891 complex. It only shows that a PAO1 genomic clone carrying PA3891 complements a P. syringae opuCA-deficient mutant for osmoprotected growth. The complex membership is a sequence and operon inference (ISS/IC). This row seeds the PAINT plasma membrane IBD at PTN001953445 (about 31 leaf IBAs), so re-coding it affects that node.

## 35. WRONG_GENE_PRODUCT (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HX83 enables GO:0005275 amine transmembrane transporter activity (IDA, PMID:21478341)
- **Field:** DB_Object_ID
- **Change:** UniProtKB:Q9HX83 → UniProtKB:Q9HTR3 (PA5291, BetT3)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA3933/PA3933-ai-review.yaml`

PA3933 is annotated enables GO:0005275 (IDA, PMID:21478341). The paper studies BetT1, BetT3 and CbcXWV, naming BetT2 as PA14_12990 and BetT3 as PA14_69850. PA14_12990 is identical to PAO1 PA3933 and PA14_69850 is identical to PAO1 PA5291. The paper has no transport data for BetT2; the choline uptake data are for BetT3 (PA5291). Please move the row to PA5291 (better as GO:0015220 choline transmembrane transporter activity).

## 36. WRONG_GENE_PRODUCT (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HX83 enables GO:0033265 choline binding (IDA, PMID:21478341)
- **Field:** DB_Object_ID
- **Change:** UniProtKB:Q9HX83 → UniProtKB:Q9HTR3 (PA5291, BetT3)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA3933/PA3933-ai-review.yaml`

PA3933 is annotated enables GO:0033265 choline binding (IDA, PMID:21478341). The paper's BetT3 is PA14_69850, identical to PAO1 PA5291; BetT2 (PA3933) is only measured by qRT-PCR. The row belongs to PA5291; note also that the paper measures uptake, not binding.

## 37. WRONG_GENE_PRODUCT (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HX83 involved_in GO:0042426 choline catabolic process (IDA, PMID:21478341)
- **Field:** DB_Object_ID
- **Change:** UniProtKB:Q9HX83 → UniProtKB:Q9HTR3 (PA5291, BetT3)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA3933/PA3933-ai-review.yaml`

PA3933 is annotated involved_in GO:0042426 (IDA, PMID:21478341). The growth data are for BetT3 (PA14_69850 = PAO1 PA5291), not BetT2 (PA14_12990 = PAO1 PA3933). On PA5291 the term should itself be GO:0015871 choline transport, since the transporter performs no catabolic step.

## 38. WRONG_GENE_PRODUCT (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HX83 involved_in GO:0071475 cellular hyperosmotic salinity response (IDA, PMID:21478341)
- **Field:** DB_Object_ID
- **Change:** UniProtKB:Q9HX83 → UniProtKB:Q9HTR3 (PA5291, BetT3)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA3933/PA3933-ai-review.yaml`

PA3933 is annotated involved_in GO:0071475 (IDA, PMID:21478341). The paper's hyperosmolar growth data concern BetT3, which is PA14_69850 = PAO1 PA5291. BetT2 (PA3933) was not tested. Please move the row to PA5291.

## 39. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HWU0 enables GO:0042286 glutamate-1-semialdehyde 2,1-aminomutase activity (EXP, PMID:29684343)
- **Field:** GO_ID
- **Change:** check GO:0042286 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/PA4088/PA4088-ai-review.yaml`

The PseudoCAP EXP GO:0042286 glutamate-1-semialdehyde 2,1-aminomutase activity on PA4088 (Q9HWU0) cites PMID:29684343, a crystal-structure paper. Its abstract calls pa4088 uncharacterized, assigns it to the GSAM family from the structure and reports PLP and PMP complexes; it describes no activity assay. PAO1 has a canonical HemL (PA3977, P48247), and PA4088 is about 27% identical to HemL enzymes, versus 66% between HemL orthologs (sequence analysis in PA4088-bioinformatics). What the structure supports is GO:0030170 pyridoxal phosphate binding. Only the abstract was read; if the full text reports a GSAM assay of the purified protein the row stands. The row seeds PTN000241365 and PTN000241400.

> The resulting high-resolution structure confirms it to be a member of the GSAM family
> — PMID:29684343

> Continuous electron density indicates the presence of a PLP cofactor with a Schiff base linkage between the PLP cofactor and the ε-amino group of Lys286
> — PMID:29684343

> | E. coli HemL vs PA4088 | 26.9 |
> — file:PSEAE/PA4088/PA4088-bioinformatics/RESULTS.md

## 40. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HWG8 located_in GO:0009276 Gram-negative-bacterium-type cell wall (IDA, PMID:21192796)
- **Field:** GO_ID
- **Change:** GO:0009276 → GO:0005886 (plasma membrane)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA4218/PA4218-ai-review.yaml`

GO:0009276 Gram-negative-bacterium-type cell wall (the peptidoglycan layer) is annotated by IDA to PA4218 (AmpP) from PMID:21192796. The paper's PhoA/LacZ fusion data (full text read) show a 10-helix inner-membrane protein. Please repoint to GO:0005886 plasma membrane. The AmpG (PA4393) row from PMID:20713660 has the same error.

> AmpP fusions at amino acids 80, 170, 248, 308, 400 as well as full length were LacZ-positive and PhoA-negative, and fusions at amino acids 38, 120, 195, 278, and 360 were LacZ-negative and PhoA-positive, consistent with 10 TM domains (Figures 4A and 4B).
> — PMID:21192796

## 41. WRONG_EVIDENCE_CODE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HWG8 enables GO:0022857 transmembrane transporter activity (IDA, PMID:21192796)
- **Field:** Evidence_Code
- **Change:** check IDA (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA4218/PA4218-ai-review.yaml`

GO:0022857 transmembrane transporter activity is annotated by IDA to PA4218 (AmpP) from PMID:21192796. The full text reports PhoA/LacZ topology fusions and beta-lactamase and ampC-promoter induction in mutants, and concludes only that the topology is consistent with transport; there is no transport assay. Topology is not direct evidence of transporter activity. Please downgrade the evidence (for example to ISS against an experimentally characterised family member) or remove the row. The term itself is plausible; the PTN008542531 IBD does not depend on this row.

> AmpP fusions at amino acids 80, 170, 248, 308, 400 as well as full length were LacZ-positive and PhoA-negative, and fusions at amino acids 38, 120, 195, 278, and 360 were LacZ-negative and PhoA-positive, consistent with 10 TM domains (Figures 4A and 4B).
> — PMID:21192796

## 42. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HWG8 involved_in GO:0033252 regulation of beta-lactamase activity (IDA, PMID:21192796)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0033252
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA4218/PA4218-ai-review.yaml`

GO:0033252 regulation of beta-lactamase activity is annotated by IDA to PA4218 (AmpP) from PMID:21192796. The full text shows that ampP mutants lose benzylpenicillin induction of the ampC promoter; the lower beta-lactamase activity in lysates follows from lower ampC expression. AmpP does not act on the enzyme. Please delete the row.

> Benzyl-penicillin dependent induction of PampC-lacZ was lost in PAOampG or PAOampP (Figure 6).
> — PMID:21192796

## 43. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HW69 involved_in GO:0044010 single-species biofilm formation (IMP, PMID:17586642)
- **Change:** GO:0044010 → GO:1900192 (positive regulation of single-species biofilm formation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA4332/PA4332-ai-review.yaml`

GO:0044010 IMP on PA4332/SadC (Q9HW69) from PMID:17586642. SadC is a diguanylate cyclase; the paper shows that its c-di-GMP promotes biofilm formation by controlling EPS production and flagellar reversals. The regulatory term GO:1900192 describes this better.

> Deletion of the sadC gene results in a strain that is defective in biofilm formation and a hyperswarmer, while multicopy expression of this gene promotes sessility.
> — PMID:17586642

## 44. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HW69 involved_in GO:0071978 bacterial-type flagellum-dependent swarming motility (IMP, PMID:17586642)
- **Change:** GO:0071978 → GO:1902201 (negative regulation of bacterial-type flagellum-dependent cell motility)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA4332/PA4332-ai-review.yaml`

GO:0071978 swarming motility IMP on PA4332/SadC (Q9HW69) from PMID:17586642. The abstract states that the deletion is a hyperswarmer, so SadC negatively regulates swarming. Please annotate a negative regulation term (GO:1902201, or a new negative regulation of swarming motility term if created).

> Deletion of the sadC gene results in a strain that is defective in biofilm formation and a hyperswarmer, while multicopy expression of this gene promotes sessility.
> — PMID:17586642

## 45. WRONG_REFERENCE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HW69 involved_in GO:1900192 positive regulation of single-species biofilm formation (IDA, PMID:26991003)
- **Field:** DB:Reference
- **Change:** check PMID:26991003 (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/PSEAE/PA4332/PA4332-ai-review.yaml`

GO:1900192 IDA on PA4332/SadC (Q9HW69) cites PMID:26991003 (Chen et al. 2016), whose title and abstract concern arsenate resistance by GAPDH and the efflux permease ArsJ; the full text does not mention SadC, PA4332, c-di-GMP or biofilms. Please identify the intended reference. If none, the claim is supported as IMP by PMID:17586642.

> Here, we describe a new pathway of arsenate resistance involving biosynthesis and extrusion of an unusual pentavalent organoarsenical.
> — PMID:26991003

## 46. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HW06 involved_in GO:0006281 DNA repair (IDA, PMID:12445642)
- **Field:** Evidence_Code
- **Change:** check ECO:0000314 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA4400/PA4400-ai-review.yaml`

PA4400 (mutT, Q9HW06) involved_in GO:0006281 DNA repair is coded IDA from PMID:12445642 (Oliver et al. 2002). The abstract states that the evidence is complementation of the high mutation frequency of an E. coli mutT strain by the cloned P. aeruginosa gene, which is heterologous genetic complementation (IGI), not a direct assay. Only the abstract was read, hence PROBABLE and CHECK. The term is correct, and the row seeds the PAINT IBD at PTN000755027, which also stands on E. coli MutT.

## 47. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HVR8 enables GO:0071916 dipeptide transmembrane transporter activity (IDA, PMID:25338022)
- **Field:** Evidence_Code
- **Change:** check ECO:0000314 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA4503/PA4503-ai-review.yaml`

GO:0071916 for PA4503 (DppB, Q9HVR8) is annotated IDA to PMID:25338022. The paper's evidence is a deletion of the whole dppBCDF operon in strain PA14, scored by Biolog respiration on dipeptides and by phaseolotoxin sensitivity. No direct transport, binding or ATPase assay was done with the protein, so IMP is the correct code. The claim itself is sound. This row is the sole seed of the PAINT IBD at PTN000765601 and one of four seeds at PTN002455499. The same applies to the matching PA4504 (DppC) row.

> Numerous dipeptides could not be used as N-source by the mutant lacking the DppBCDF transporter system
> — PMID:25338022

## 48. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HVR7 enables GO:0071916 dipeptide transmembrane transporter activity (IDA, PMID:25338022)
- **Field:** Evidence_Code
- **Change:** check ECO:0000314 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA4504/PA4504-ai-review.yaml`

GO:0071916 for PA4504 (DppC, Q9HVR7) is annotated IDA to PMID:25338022. The paper's evidence is a deletion of the whole dppBCDF operon in strain PA14, scored by Biolog respiration on dipeptides and by phaseolotoxin sensitivity. No direct transport, binding or ATPase assay was done with the protein, so IMP is the correct code. The claim itself is sound. This row is the sole seed of the PAINT IBD at PTN000766696 and one of five seeds at PTN000765620. The same applies to the matching PA4503 (DppB) row.

> Numerous dipeptides could not be used as N-source by the mutant lacking the DppBCDF transporter system
> — PMID:25338022

## 49. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HVR6 enables GO:0071916 dipeptide transmembrane transporter activity (IDA, PMID:25338022)
- **Field:** Evidence_Code
- **Change:** check ECO:0000314 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA4505/PA4505-ai-review.yaml`

GO:0071916 for PA4505 (DppD, Q9HVR6) is annotated IDA to PMID:25338022. The paper's evidence is a deletion of the whole dppBCDF operon in strain PA14, scored by Biolog respiration on dipeptides and by phaseolotoxin sensitivity. No direct transport, binding or ATPase assay was done, so IMP is the correct code. The claim itself is sound. This row is the sole seed of the PAINT IBD at PTN000656114 and one of four seeds at PTN000656054. The same applies to the PA4503 and PA4504 rows.

> Numerous dipeptides could not be used as N-source by the mutant lacking the DppBCDF transporter system
> — PMID:25338022

## 50. WRONG_EVIDENCE_CODE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HVR5 enables GO:0071916 dipeptide transmembrane transporter activity (IDA, PMID:25338022)
- **Field:** Evidence
- **Change:** IDA → IMP
- **Recorded in:** `genes/PSEAE/PA4506/PA4506-ai-review.yaml`

The PseudoCAP GO:0071916 row on PA4506 cites PMID:25338022 as IDA. The full text shows the evidence is a deletion of the whole dppBCDF operon in strain PA14, scored by Biolog respiration and growth on dipeptides; no transport or ATPase assay of DppF was done. That is mutant-phenotype evidence (IMP), transferred from PA14_58490 to the PAO1 ortholog PA4506. The term itself is right.

> In order to investigate the substrate profile of the ABC transporter DppBCDF, a deletion mutant of the dppBCDF operon was constructed
> — PMID:25338022

> Numerous dipeptides could not be used as N-source by the mutant lacking the DppBCDF transporter system
> — PMID:25338022

## 51. WRONG_QUALIFIER (SUSPECTED, NOT_REPORTED)

- **Record:** PMID:20088866
- **Subject:** UniProtKB:Q9HVG7
- **Change:** check involved_in (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA4624/PA4624-ai-review.yaml`

GO:0044010 single-species biofilm formation for PA4624 (CdrB, Q9HVG7) is annotated IMP involved_in to PMID:20088866. The paper made cdrA deletions only; the cdrB evidence is that cdrAB co-overexpression increases biofilm, with cdrB required for secretion of the CdrA adhesin. CdrB therefore acts upstream of biofilm formation by exporting CdrA, rather than taking part in matrix formation. Consider acts_upstream_of_or_within, or removing the row from CdrB and keeping it on CdrA (PA4625).

> This is consistent with the data presented in Fig. 3, suggesting that CdrB is required for CdrA secretion.
> — PMID:20088866

## 52. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HUW7 involved_in GO:1902065 response to L-glutamate (IMP, PMID:25331436)
- **Change:** check GO:1902065 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA4843/PA4843-ai-review.yaml`

GO:1902065 response to L-glutamate IMP on PA4843/GcbA (Q9HUW7) from PMID:25331436. The abstract states that GcbA, through early BdlA processing, is required for biofilm dispersal in response to many substances (carbohydrates, heavy metals, nitric oxide), so the phenotype reflects a general dispersal defect rather than a role in the glutamate response. Please consider removing the row, or annotating a biofilm dispersal term if one is created (abstract only; full text not read).

> plays an essential role in allowing biofilm cells to disperse in response to increasing concentrations of a variety of substances, including carbohydrates, heavy metals, and nitric oxide
> — PMID:25331436

## 53. WRONG_TERM (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HUR7 involved_in GO:0034756 regulation of iron ion transport (IMP, PMID:18086184)
- **Field:** GO_ID
- **Change:** check GO:0034756 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA4896/PA4896-ai-review.yaml`

PseudoCAP IMP GO:0034756 regulation of iron ion transport on PA4896 from PMID:18086184 (Llamas et al. 2008). The abstract shows only that PA4896 overexpression induces a TonB-dependent transducer and putative (metal) transport genes; it names no iron substrate for PA4896. Please check whether the full text shows an iron-transport phenotype; if not, a regulation of transport term without iron, or no BP row, would be more accurate. This row does not seed an IBD.

> although all these sigma factors seem to control putative (metal) transport systems
> — PMID:18086184

## 54. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HUJ0 enables GO:0003955 NAD(P)H dehydrogenase (quinone) activity (IMP, PMID:25085734)
- **Field:** Evidence_Code
- **Change:** IMP → IDA
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA4975/PA4975-ai-review.yaml`

PseudoCAP row for PA4975 (Q9HUJ0), GO:0003955 NAD(P)H dehydrogenase (quinone) activity, IMP, PMID:25085734 (Green et al. 2014). The abstract states that each of the five quinone oxidoreductase orthologs reduced quinone substrates in in vitro assays; the only genetic experiments it reports are overexpression growth tests under H2O2, and only the WrbA and MdaB orthologs gave a phenotype. The term is correct, but the evidence is a direct assay (IDA). Abstract-only reading; the full text could describe a mutant assay that the abstract does not mention. Same defect as recorded for PA1204 from this paper.

> In in vitro assays, each enzyme was shown to reduce quinone substrates with only minimal semiquinone formation.
> — PMID:25085734

## 55. WRONG_REFERENCE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HU50 involved_in GO:0007165 signal transduction (IDA, PMID:24928312)
- **Field:** DB:Reference
- **Change:** delete the record asserting PMID:24928312
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA5134/PA5134-ai-review.yaml`

PMID:24928312 (Carroll et al. 2014) characterises the lone S41 CTP of Staphylococcus aureus, as its title and abstract state outright; it has no P. aeruginosa data and reports no signal transduction role. The IDA row on PA5134 has no support and should be deleted.

## 56. WRONG_REFERENCE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HU50 involved_in GO:0042546 cell wall biogenesis (IDA, PMID:24928312)
- **Field:** DB:Reference
- **Change:** delete the record asserting PMID:24928312
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA5134/PA5134-ai-review.yaml`

PMID:24928312 characterises the S. aureus CtpA, as the abstract states outright; it shows cell-wall localisation of that protein, not cell wall biogenesis, and has no P. aeruginosa data. The IDA row on PA5134 should be deleted.

## 57. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HTY2 involved_in GO:0044010 single-species biofilm formation (IMP, PMID:17158671)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0044010
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA5208/PA5208-ai-review.yaml`

involved_in GO:0044010 single-species biofilm formation (IMP) on PA5208 rests on a crystal-violet biofilm reduction in a single mini-Tn5 insertion mutant from a swarming screen (Overhage et al. 2007) that also has a growth defect. This records a mutant phenotype, not participation of this PhoU-like protein in biofilm formation.

> and a PA5208 mutant that had a slight growth defect
> — PMID:17158671

## 58. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HTY2 involved_in GO:0071978 bacterial-type flagellum-dependent swarming motility (IMP, PMID:17158671)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0071978
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA5208/PA5208-ai-review.yaml`

involved_in GO:0071978 (IMP) on PA5208 rests on a single mini-Tn5 insertion mutant from a swarming screen (Overhage et al. 2007) that also has a growth defect. PA5208 is a PhoU-like UPF0111 protein with no flagellar or motor domain and whose own function is predicted rather than known; the row records an indirect mutant phenotype and is the sole seed of the PTN002194937 swarming IBD (5 leaf IBAs, two of them in Haemophilus influenzae and Coxiella burnetii, which encode no core flagellar genes).

> and a PA5208 mutant that had a slight growth defect
> — PMID:17158671

## 59. WRONG_GENE_PRODUCT (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HTR3 enables GO:0015653 glycine betaine:proton symporter activity (IDA, PMID:18156257)
- **Field:** DB_Object_ID
- **Change:** check UniProtKB:Q9HTR3 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA5291/PA5291-ai-review.yaml`

PA5291 is annotated enables GO:0015653 glycine betaine:proton symporter activity (IDA, PMID:18156257). Malek et al. 2011 (PMID:21478341), from the same group, state that this paper showed BetT2 transports glycine betaine and BetT3 transports choline, and name BetT2 and BetT3 as PA14_12990 and PA14_69850. These are identical to PAO1 PA3933 and PA5291. The glycine betaine transport data therefore most likely belong to PA3933. Please check against the full text and move the row to PA3933 if confirmed.

## 60. WRONG_GENE_PRODUCT (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HTR3 involved_in GO:0031460 glycine betaine transport (IDA, PMID:18156257)
- **Field:** DB_Object_ID
- **Change:** check UniProtKB:Q9HTR3 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA5291/PA5291-ai-review.yaml`

PA5291 is annotated involved_in GO:0031460 glycine betaine transport (IDA, PMID:18156257). As for the GO:0015653 row from the same paper, the glycine betaine transporter characterised there is BetT2, which is PA3933 (identical to PA14_12990), not BetT3 (PA5291, identical to PA14_69850). Please check and move the row to PA3933 if confirmed.

## 61. WRONG_GENE_PRODUCT (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HTJ9 involved_in GO:0043448 alkane catabolic process (IMP, PMID:14574114)
- **Field:** DB_Object_ID
- **Change:** check UniProtKB:Q9HTJ9 (alternatives in the explanation)
- **Likely cause:** IDENTIFIER_TRANSPOSITION
- **Recorded in:** `genes/PSEAE/PA5359/PA5359-ai-review.yaml`

PseudoCAP annotates PA5359 (UniProtKB:Q9HTJ9) with GO:0043448 alkane catabolic process, IMP, from PMID:14574114 (Smits, Witholt & van Beilen 2003). Three things suggest the locus tag may be wrong, and we ask PseudoCAP to check against the full text, which is not publicly accessible to us. (1) The paper's abstract characterises AlkB1, AlkB2, RubA1, RubA2 and RubB, which in PAO1 are PA2574, PA1525, PA5351, PA5350 and PA5349; PA5359 is not among them. (2) PA5359 is a 151-residue protein consisting of a signal peptide and two Lipoprotein_15 repeats (Pfam PF03640), with no hydroxylase, rubredoxin or flavoprotein reductase component, and UniProt gives it no function, location or family statement. (3) This is the only annotation in GOA keyed to this reference, while the five genes the paper does describe carry GO:0043448 from UniProt keyword mapping (GO_REF:0000041) rather than from the paper. PA5349 (rubB/alkT, UniProtKB:Q9HTK9) differs from PA5359 by one digit and would fit the evidence. If the row is in fact correct for PA5359, the supporting experiment would be valuable to record, since the row is the sole seed of the PAINT IBD at PTN002217427, from which 764 GOA rows descend.

> Heterologous expression showed that the two alkane hydroxylase homologs of P. aeruginosa PAO1 (AlkB1 and AlkB2) oxidize C(12)-C(16)n-alkanes, while two rubredoxin (RubA1 and RubA2) and a rubredoxin reductase (RubB) homologs can replace their P. putida GPo1 counterparts in n-octane oxidation.
> — PMID:14574114

## 62. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HTI8 enables GO:0005275 amine transmembrane transporter activity (IDA, PMID:19919675)
- **Field:** GO_ID
- **Change:** GO:0005275 → GO:0015418 (ABC-type quaternary ammonium compound transporting activity)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA5376/PA5376-ai-review.yaml`

PA5376 (CbcV ATPase, Q9HTI8) is annotated GO:0005275 amine transmembrane transporter activity, IDA, PMID:19919675 (full text read). The substrates shown in that paper (choline, glycine betaine, L-carnitine) are quaternary ammonium compounds, which GO does not class as amines. GO:0015418 ABC-type quaternary ammonium compound transporting activity (contributes_to for an ATPase subunit) is the accurate term. This row co-seeds the PAINT IBD at PTN002466744.

## 63. WRONG_TERM (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HTI8 enables GO:0015419 ABC-type sulfate transporter activity (IDA, PMID:23763788)
- **Field:** GO_ID
- **Change:** check GO:0015419 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA5376/PA5376-ai-review.yaml`

PA5376 (CbcV, ATPase of the Cbc choline/betaine/carnitine ABC importer) is annotated GO:0015419 ABC-type sulfate transporter activity, IDA, PMID:23763788. The abstract describes P. syringae QAC bioreporters and plant choline and does not mention sulfate or PA5376. If the paper shows uptake of a sulfur-containing QAC (for example choline-O-sulfate), the row should be GO:0015418 ABC-type quaternary ammonium compound transporting activity, not a sulfate transporter. Only the abstract was read, hence SUSPECTED.

## 64. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HTI8 involved_in GO:0031457 glycine betaine catabolic process (IDA, PMID:19919675)
- **Field:** GO_ID
- **Change:** check GO:0031457 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA5376/PA5376-ai-review.yaml`

PA5376 (CbcV, ABC ATPase) is annotated involved_in GO:0031457 glycine betaine catabolic process (IDA, PMID:19919675). The evidence is that cbc transposon mutants cannot grow on betaine as sole carbon source, which reflects loss of uptake. The transporter does not catalyse any catabolic step. Consider removing the row, keeping GO:0031460 glycine betaine transport.

## 65. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HTI8 involved_in GO:0042426 choline catabolic process (IDA, PMID:19919675)
- **Field:** GO_ID
- **Change:** check GO:0042426 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA5376/PA5376-ai-review.yaml`

PA5376 (CbcV, ABC ATPase) is annotated involved_in GO:0042426 choline catabolic process (IDA, PMID:19919675 and PMID:21478341). Both papers show that Cbc is needed for growth on choline as a carbon source, which reflects choline uptake. The transporter performs no catabolic step. GO:0015871 choline transport already captures its role. Consider removing these rows.

## 66. WRONG_REFERENCE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HTI8 involved_in GO:1902603 carnitine transmembrane transport (IDA, PMID:21478341)
- **Field:** DB:Reference
- **Change:** check PMID:21478341 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA5376/PA5376-ai-review.yaml`

GO:1902603 carnitine transmembrane transport for PA5376 (Q9HTI8) cites PMID:21478341 (Malek et al. 2011), whose abstract deals only with choline uptake by CbcXWV, BetT1 and BetT3. The carnitine evidence for Cbc is in PMID:19919675 (PA14 cbc mutants, including PA5376::tn, fail to grow on carnitine) and PMID:29517479. If PMID:21478341 has no carnitine data, please re-key the row. Only the abstract was read.

## 67. WRONG_EVIDENCE_CODE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HTB5 involved_in GO:0009243 O antigen biosynthetic process (IDA, PMID:23341552)
- **Field:** Evidence_Code
- **Change:** ECO:0000314 → ECO:0000315 (IMP)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA5455/PA5455-ai-review.yaml`

The PseudoCAP row PA5455 GO:0009243 IDA PMID:23341552 rests on in-frame deletion and complementation (loss and restoration of CPA on LPS gels and immunoblots). No direct assay of the protein is reported in the full text. Re-code as IMP. PseudoCAP already holds a parallel IMP row on GO:0009103.

> We have presented evidence from genetic studies that the genes in the pa5455-pa5459 cluster are involved in CPA biosynthesis in P. aeruginosa.
> — PMID:23341552

## 68. WRONG_EVIDENCE_CODE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HTB5 enables GO:0016757 glycosyltransferase activity (IDA, PMID:23341552)
- **Field:** Evidence_Code
- **Change:** check ECO:0000314 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA5455/PA5455-ai-review.yaml`

The PseudoCAP row PA5455 GO:0016757 IDA PMID:23341552 has no direct assay behind it. The full text states that pa5455 and pa5456 were identified as putative glycosyltransferases by gene sequence analysis, and the only experiments on them are deletion, complementation and overexpression with LPS gel and immunoblot readouts. Either re-code with a sequence-based code (ISM/ISS) or drop the row; IMP would also not fit, since loss of CPA does not show which activity the protein has. This row is one of only two seeds of the PAINT IBD on PTN002288302.

> Gene sequence analysis indicated that pa5455 and pa5456 encode putative glycosyltransferases.
> — PMID:23341552

## 69. WRONG_EVIDENCE_CODE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HTB4 involved_in GO:0009243 O antigen biosynthetic process (IDA, PMID:23341552)
- **Field:** Evidence_Code
- **Change:** ECO:0000314 → ECO:0000315 (IMP)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA5456/PA5456-ai-review.yaml`

The PseudoCAP row PA5456 GO:0009243 IDA PMID:23341552 rests on in-frame deletion and complementation (loss and restoration of CPA on LPS gels and immunoblots). No direct assay of the protein is reported in the full text. Re-code as IMP. PseudoCAP already holds a parallel IMP row on GO:0009103.

> We have presented evidence from genetic studies that the genes in the pa5455-pa5459 cluster are involved in CPA biosynthesis in P. aeruginosa.
> — PMID:23341552

## 70. WRONG_EVIDENCE_CODE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HTB4 enables GO:0016757 glycosyltransferase activity (IDA, PMID:23341552)
- **Field:** Evidence_Code
- **Change:** check ECO:0000314 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA5456/PA5456-ai-review.yaml`

The PseudoCAP row PA5456 GO:0016757 IDA PMID:23341552 has no direct assay behind it. The full text states that pa5455 and pa5456 were identified as putative glycosyltransferases by gene sequence analysis, and the only experiments on them are deletion, complementation and overexpression with LPS gel and immunoblot readouts. Either re-code with a sequence-based code (ISM/ISS) or drop the row; IMP would also not fit, since loss of CPA does not show which activity the protein has. This row is one of only two seeds of the PAINT IBD on PTN002288302.

> Gene sequence analysis indicated that pa5455 and pa5456 encode putative glycosyltransferases.
> — PMID:23341552

## 71. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HTB2 involved_in GO:0009243 O antigen biosynthetic process (IDA, PMID:23341552)
- **Field:** Evidence_Code
- **Change:** IDA → IMP
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA5458/PA5458-ai-review.yaml`

The PseudoCAP GO:0009243 row for PA5458 (PMID:23341552, Hao et al. 2013) uses IDA, but the paper reports no direct assay of the PA5458 protein or its activity. The evidence is the LPS phenotype of an in-frame deletion mutant, its complementation, and overexpression, analysed by SDS-PAGE and Western blot. Please change the evidence code to IMP. The GO term itself is appropriate.

> Mutation of the putative acetyltransferase-encoding gene pa5458 did not abrogate polysaccharide production
> — PMID:23341552

## 72. WRONG_QUALIFIER (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HT75 enables GO:0000006 high-affinity zinc transmembrane transporter activity (ISS, PMID:9680209)
- **Field:** Qualifier
- **Change:** enables GO:0000006 → contributes_to GO:0015633 (ABC-type zinc transporter activity)
- **Recorded in:** `genes/PSEAE/PA5498/PA5498-ai-review.yaml`

A periplasmic solute-binding protein does not by itself enable transmembrane transport; it contributes to the activity of the ZnuABC complex. Not an IBD seed.

> The Znu permease comprises the solute-binding protein (SBP) ZnuA, and an ABC transporter, which consists of ZnuB
> — PMID:26290475

## 73. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HT75 involved_in GO:0010043 response to zinc ion (IMP, PMID:24086521)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0010043
- **Recorded in:** `genes/PSEAE/PA5498/PA5498-ai-review.yaml`

Full text read: the znuA evidence is a growth defect of the deletion mutant under zinc depletion, an indirect phenotype of lost zinc uptake already captured by zinc ion transport. Not an IBD seed.

> the inability to express the putative znuA, znuB, or znuC genes resulted in decreased growth at 18 hours
> — PMID:24086521

## 74. WRONG_TERM (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HT69 involved_in GO:1903810 L-histidine import across plasma membrane (IMP, PMID:18833300)
- **Field:** GO_ID
- **Change:** check GO:1903810 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA5504/PA5504-ai-review.yaml`

The PseudoCAP IMP GO:1903810 L-histidine import across plasma membrane row on PA5504 rests on a reduced (C+/-) growth of a Mini-Tn5 mutant on L-histidine in Johnson et al. 2008 (PMID:18833300), with no uptake assay and no induction by histidine. PA5504 is a MetI-family permease (NCBIfam metI) next to MetN2. Please consider either a less specific term (GO:0003333 amino acid transmembrane transport) or keeping the row with a note; SUSPECTED because a growth phenotype on a substrate is an accepted, if indirect, basis for transport annotation.

> A PA5504 knockout affected growth on L-histidine as a carbon source (Table 2), however its expression was not induced by this compound.
> — PMID:18833300

## 75. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HTB8 involved_in GO:0015920 lipopolysaccharide transport (IMP, PMID:9244257)
- **Field:** GO_ID
- **Change:** GO:0015920 → GO:0015774 (polysaccharide transport)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/Q9HTB8/Q9HTB8-ai-review.yaml`

involved_in GO:0015920 lipopolysaccharide transport (IMP, PMID:9244257) on Wzm (PA5451, Q9HTB8). The paper shows that wzm mutants accumulate A-band polysaccharide in the cytoplasm because the polymer cannot cross the inner membrane. What Wzm-Wzt exports is the undecaprenyl-pyrophosphate-linked polysaccharide, which becomes LPS only after WaaL ligation in the periplasm, so polysaccharide transport (GO:0015774) states the substrate correctly. This row is the sole seed of the PAINT IBD at PTN002019107.

> The inability of the polymer to cross the inner membrane resulted in the accumulation of cytoplasmic A-band polysaccharide.
> — PMID:9244257

## 76. WRONG_QUALIFIER (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HTH6 enables GO:0015226 carnitine transmembrane transporter activity (IDA, PMID:19919675)
- **Field:** Qualifier
- **Change:** enables → contributes_to
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/Q9HTH6/Q9HTH6-ai-review.yaml`

CaiX is the periplasmic substrate-binding protein of an ABC importer and cannot translocate carnitine without the CbcW permease and CbcV ATPase; contributes_to is the GO relation for a subunit carrying part of a complex activity.

## 77. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HY69 enables GO:0004467 long-chain fatty acid-CoA ligase activity (IDA, PMID:16797016)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0004467
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/PSEAE/alg44/alg44-ai-review.yaml`

The PseudoCAP IDA annotation assigns long-chain fatty acid-CoA ligase activity to Alg44 (Q9HY69) using PMID:16797016. The complete original article, reproduced as Chapter III of Uwe Remminghorst's 2007 thesis (printed pp.58-69; PDF pp.71-82; https://mro.massey.ac.nz/bitstreams/55746141-71a5-48b8-b1b2-8abf9db2eb49/download), reports alginate production, topology, morphology and protein identification, not ATP/CoA-dependent fatty-acid activation. Delete this unsupported activity row; a replacement assay/gene is not established. The unexpected PseudoCAP threonine-deaminase row on AlgL is a separate suspected defect, not proof of a shared mapping cause.

- **Evidence reference:** PMID:16797016

> These studies suggest that Alg44 may act as a co-polymerase in concert with Alg8, the major GT
> — PMID:18524915

## 78. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:P23747 involved_in GO:0042121 alginic acid biosynthetic process (IMP, PMID:1738315)
- **Field:** GO_ID
- **Change:** GO:0042121 → GO:0032885 (regulation of polysaccharide biosynthetic process)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/algB/algB-ai-review.yaml`

PA5483/algB is annotated to alginic acid biosynthetic process (IMP, PMID:1738315), but the title and abstract state that AlgB is an NtrC-subclass regulator controlling algD expression. A regulator should be annotated to regulation of the process. No alginate-specific regulation term exists, so GO:0032885 is the nearest; a positive regulation of alginic acid biosynthetic process term would be better.

> regulates the expression of the alginate biosynthetic gene, algD, thereby resulting in increased expression of alginate in mucoid P. aeruginosa
> — PMID:1738315

## 79. WRONG_REFERENCE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:P23747 involved_in GO:0045862 positive regulation of proteolysis (IMP, PMID:23024348)
- **Field:** REFERENCE
- **Change:** check PMID:23024348 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/algB/algB-ai-review.yaml`

PMID:23024348 (full text read) has no proteolysis data, and its elastase data show repression by phosphorylated AlgB (opposite sign). The promote-proteolysis claim matches PMID:19168621 (AlgW-mediated MucA degradation needs algB in a kinB mutant), which was cited for an unrelated biofilm row on the same gene. Either the references were swapped or the row should be dropped; the curators should check.

> Our results also indicate that AlgW-mediated MucA degradation required algB and rpoN in the kinB mutant.
> — PMID:19168621

## 80. WRONG_REFERENCE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:P23747 involved_in GO:1900232 negative regulation of single-species biofilm formation on inanimate substrate (IMP, PMID:19168621)
- **Field:** REFERENCE
- **Change:** check PMID:19168621 (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/PSEAE/algB/algB-ai-review.yaml`

The full text of PMID:19168621 has no biofilm experiments or mentions. The row needs the correct reference or deletion. Supplementary data were not checked, hence PROBABLE.

> Our results also indicate that AlgW-mediated MucA degradation required algB and rpoN in the kinB mutant.
> — PMID:19168621

## 81. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:P23747 involved_in GO:1900378 positive regulation of secondary metabolite biosynthetic process (IMP, PMID:23024348)
- **Field:** GO_ID
- **Change:** GO:1900378 → GO:1900377 (negative regulation of secondary metabolite biosynthetic process)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/algB/algB-ai-review.yaml`

Full text of PMID:23024348 read: algB deletion in PA14 kinB restores wild-type pyocyanin, and phosphorylated AlgB is required to repress acute-virulence traits. The PseudoCAP row has the opposite sign (likely carried over from the KinB annotations).

> Similarly, algB deletion in PA14Δ kinB also restores wild-type levels of pyocyanin and elastase
> — PMID:23024348

> These data suggest that in the absence of KinB, AlgB must be phosphorylated in order to repress virulence.
> — PMID:23024348

## 82. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:P23747 involved_in GO:2000147 positive regulation of cell motility (IMP, PMID:23024348)
- **Field:** GO_ID
- **Change:** GO:2000147 → GO:2000146 (negative regulation of cell motility)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/algB/algB-ai-review.yaml`

Full text of PMID:23024348 read: complementing algB in the algB kinB double mutant restores the reduced motility of the kinB strain, so AlgB represses motility. The row has the opposite sign.

> Episomal complementation of the algB deletion in the PA14Δ algB Δ kinB strain restores the reduced pyocyanin, elastase, and motility phenotypes of the PA14Δ kinB strain
> — PMID:23024348

## 83. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q06749 enables GO:0004794 threonine deaminase activity (IDA, PMID:8370530)
- **Field:** GO_ID
- **Change:** GO:0004794 → GO:0045135
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/PSEAE/algL/algL-ai-review.yaml`

The PseudoCAP IDA row for AlgL (Q06749) from PMID:8370530 uses GO:0004794 threonine deaminase activity, but the paper's abstract describes only an alginate lyase assay on purified AlgL. The activity measured corresponds to GO:0045135 poly(beta-D-mannuronate) lyase activity. Please repoint the row; the full text was not available to confirm that no separate deaminase assay was performed.

> The purified protein was shown to have alginate lyase activity.
> — PMID:8370530

## 84. WRONG_EVIDENCE_CODE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:G3XCZ2 involved_in GO:0000160 phosphorelay signal transduction system (IDA, PMID:8790418)
- **Field:** Evidence_Code
- **Change:** check ECO:0000314 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/algZ/algZ-ai-review.yaml`

The PseudoCAP row codes GO:0000160 to AlgZ/FimS as IDA from PMID:8790418. The abstract reports that fimS was found by sequence next to algR and that a fimS mutant cannot twitch, and it classifies FimS and AlgR as a new subclass of two-component systems. It describes no direct assay of phosphorelay. IMP (mutant phenotype) or ISS (sequence) would fit. SUSPECTED, because the full text (a page scan) could not be read and could contain a biochemical experiment. The term itself is not in question.

> FimS and AlgR are representative of a new subclass of two-component transmitter-receiver regulatory systems.
> — PMID:8790418

## 85. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:G3XCW9 located_in GO:0009276 Gram-negative-bacterium-type cell wall (IMP, PMID:9835532)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0009276
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/ampD/ampD-ai-review.yaml`

The PseudoCAP IMP row placing PA4522/ampD in GO:0009276 Gram-negative-bacterium-type cell wall (PMID:9835532) rests on cloning and complementation of E. coli ampD mutants for beta-lactamase expression, which does not localize the protein. AmpD is the cytoplasmic recycling amidase (PMID:23510438; E. coli orthologue P13016 is cytoplasmic). Delete the row. The row is the source of the ampD seed of the PTN002019137 IBD. PROBABLE because the 1998 full text could not be read.

> The ampD product transcomplemented Escherichia coli ampD mutants to wild-type beta-lactamase expression.
> — PMID:9835532

## 86. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:G3XCW9 involved_in GO:0033252 regulation of beta-lactamase activity (IMP, PMID:9835532)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0033252
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/ampD/ampD-ai-review.yaml`

The PseudoCAP IMP row annotates PA4522/ampD to GO:0033252 regulation of beta-lactamase activity (PMID:9835532). The paper reports that ampD restores wild-type beta-lactamase expression in E. coli ampD mutants; AmpD controls ampC transcription indirectly by degrading the AmpR-activating anhydromuropeptide and does not modulate beta-lactamase catalytic activity. Delete the row. PROBABLE because the 1998 full text could not be read.

> The ampD product transcomplemented Escherichia coli ampD mutants to wild-type beta-lactamase expression.
> — PMID:9835532

## 87. WRONG_EVIDENCE_CODE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HT86 located_in GO:0009276 Gram-negative-bacterium-type cell wall (IDA, PMID:23510438)
- **Field:** Evidence_Code
- **Change:** check ECO:0000314 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/ampDh2/ampDh2-ai-review.yaml`

The PseudoCAP row PA5485/ampDh2 located_in GO:0009276 is coded IDA from PMID:23510438, but the paper (full text read) contains no localization experiment. It cites earlier work for the signal peptide and outer-membrane anchor and infers a periplasmic role from substrate preference. The location is correct, so keep the term but re-code the row (TAS or IC), or cite a paper that localized the protein.

> If AmpDh2 and AmpDh3 were to be periplasmic enzymes, as proposed in this report
> — PMID:23510438

## 88. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HT86 involved_in GO:0033252 regulation of beta-lactamase activity (IDA, PMID:23510438)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0033252
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/ampDh2/ampDh2-ai-review.yaml`

The PseudoCAP IDA row annotates PA5485/ampDh2 to GO:0033252 regulation of beta-lactamase activity from PMID:23510438. The paper (full text read) measures amidase kinetics only; its link to AmpC is an interpretation of earlier genetic data, in which the paralogue's marginal turnover of anhydromuropeptides lowers the AmpR inducer and so ampC expression. It neither assays nor modulates beta-lactamase activity. Delete the row.

> Nonetheless, the marginal activity in turnover of metabolite 1 with AmpDh2 and AmpDh3 explains the stepwise effect observed in augmenting derepression of AmpC β-lactamase by eliminations of these enzymes one-by-one.
> — PMID:23510438

## 89. WRONG_EVIDENCE_CODE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I5D1 located_in GO:0009276 Gram-negative-bacterium-type cell wall (IDA, PMID:23510438)
- **Field:** Evidence_Code
- **Change:** check ECO:0000314 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/ampDh3/ampDh3-ai-review.yaml`

The PseudoCAP row PA0807/ampDh3 located_in GO:0009276 is coded IDA from PMID:23510438, but the paper (full text read) contains no localization experiment and itself states that the cellular location of AmpDh3 is unknown; a periplasmic role is proposed from substrate preference. AmpDh3 lacks a predicted signal peptide, and PMID:36577706 found no export. Re-code the row (IC at most) or delete it until AmpDh3 has been localized.

> the cellular location of AmpDh3 is currently unknown
> — PMID:23510438

## 90. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I5D1 involved_in GO:0033252 regulation of beta-lactamase activity (IDA, PMID:23510438)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0033252
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/ampDh3/ampDh3-ai-review.yaml`

The PseudoCAP IDA row annotates PA0807/ampDh3 to GO:0033252 regulation of beta-lactamase activity from PMID:23510438. The paper (full text read) measures amidase kinetics only; its link to AmpC is an interpretation of earlier genetic data, in which the paralogue's marginal turnover of anhydromuropeptides lowers the AmpR inducer and so ampC expression. It neither assays nor modulates beta-lactamase activity. Delete the row.

> Nonetheless, the marginal activity in turnover of metabolite 1 with AmpDh2 and AmpDh3 explains the stepwise effect observed in augmenting derepression of AmpC β-lactamase by eliminations of these enzymes one-by-one.
> — PMID:23510438

## 91. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:G3XCT7 located_in GO:0009276 Gram-negative-bacterium-type cell wall (IMP, PMID:20713660)
- **Field:** GO_ID
- **Change:** GO:0009276 → GO:0005886 (plasma membrane)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/ampG/ampG-ai-review.yaml`

GO:0009276 Gram-negative-bacterium-type cell wall (defined as the peptidoglycan layer) is annotated to the AmpG permease PA4393 from PMID:20713660. AmpG is an integral inner-membrane protein: PhoA/LacZ fusion topology in PMID:21192796 (full text read) shows 14 transmembrane helices. Please repoint to GO:0005886 plasma membrane. The same error occurs on the AmpP (PA4218) row from PMID:21192796.

> suggesting that AmpG has only 14 TM helices (Figures 4C and 4D).
> — PMID:21192796

## 92. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:G3XCT7 involved_in GO:0033252 regulation of beta-lactamase activity (IMP, PMID:20713660)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0033252
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/ampG/ampG-ai-review.yaml`

GO:0033252 regulation of beta-lactamase activity is annotated to the AmpG permease PA4393 from PMID:20713660 (abstract only). The abstract states AmpG transports the muropeptides that signal ampC induction, and PMID:21192796 (full text) shows the ampC promoter is not induced in the ampG mutant. The mutant lacks beta-lactamase because ampC is not expressed; AmpG does not act on the enzyme. Please delete the row.

> transports 1,6-GlcNAc-anhydro-MurNAc and the 1,6-GlcNAc-anhydro-MurNAc peptide
> — PMID:20713660

> Benzyl-penicillin dependent induction of PampC-lacZ was lost in PAOampG or PAOampP (Figure 6).
> — PMID:21192796

## 93. WRONG_EVIDENCE_CODE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:P24734 involved_in GO:0006355 regulation of DNA-templated transcription (IDA, PMID:22479525)
- **Field:** Evidence_Code
- **Change:** check ECO:0000314 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/ampR/ampR-ai-review.yaml`

involved_in GO:0006355 on ampR (PA4109) is coded IDA citing Balasubramanian et al. 2012 (PMID:22479525). Full text read. The experiments are a microarray and qPCR comparison of PAO1 with the ampR deletion mutant; AmpR binding sites are only predicted bioinformatically and the authors state that direct targets remain to be identified. The term is right; the evidence is a mutant phenotype (IMP). This row is one of six seeds of the PTN000794521 IBD, which stands on the others (see the trpI notes for the node record).

> Studies aimed at identifying the direct targets of AmpR are needed to identify genes that are directly regulated by AmpR
> — PMID:22479525

## 94. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:P18275 enables GO:0043858 arginine:ornithine antiporter activity (IMP, PMID:1311296)
- **Field:** Evidence_Code
- **Change:** check ECO:0000315 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/arcD/arcD-ai-review.yaml`

enables GO:0043858 (IMP) on PA5170 arcD cites Verhoogt et al. 1992, which measures arginine/ornithine exchange in membrane vesicles from E. coli carrying arcD and in proteoliposomes with reconstituted ArcD. The abstract positively describes direct assays, not a mutant phenotype, so IDA likely fits better; the full text was not available to rule out a mutant experiment. The annotation is correct.

> The ArcD protein was reconstituted in proteoliposomes after detergent solubilization of membrane vesicles.
> — PMID:1311296

## 95. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:P22567 enables GO:0004358 L-glutamate N-acetyltransferase activity, acting on acetyl-L-ornithine as donor (IMP, PMID:22447897)
- **Field:** GO_ID
- **Change:** GO:0004358 → GO:0004042 (L-glutamate N-acetyltransferase activity, acting on acetyl-CoA as donor)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/argA/argA-ai-review.yaml`

Full text of PMID:22447897 read: the assay mixture contains L-glutamate and acetyl-CoA, and the paper describes NAGS producing N-acetyl-L-glutamate from glutamate and acetyl-CoA. GO:0004358 is the acetyl-L-ornithine-donor (ArgJ) reaction. The two terms share the synonyms N-acetylglutamate synthase activity and L-glutamate N-acetyltransferase activity, which is the likely cause. The work is biochemical, so IDA would also be the better evidence code.

> producing N -acetyl- l -glutamate (NAG) from glutamate and acetyl coenzyme A (acetyl-CoA) and being feedback inhibited by arginine
> — PMID:22447897

> 30 mM l -glutamate (sodium salt), 4 mM acetyl-CoA, and, when used, the indicated concentrations of arginine hydrochloride
> — PMID:22447897

## 96. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I025 enables GO:0004114 3',5'-cyclic-nucleotide phosphodiesterase activity (IDA, PMID:16121184)
- **Change:** GO:0004114 → GO:0071111 (cyclic-guanylate-specific phosphodiesterase activity)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/arr/arr-ai-review.yaml`

The cited abstract (PMID:16121184) names c-di-GMP as the substrate whose hydrolysis is reduced in arr mutant membranes. GO:0004114 3',5'-cyclic-nucleotide phosphodiesterase activity covers cyclic nucleoside monophosphates and does not subsume GO:0071111 (GO:0071111 is_a GO:0008081). Please repoint the row to GO:0071111.

> membranes from arr mutants had diminished c-di-GMP phosphodiesterase activity
> — PMID:16121184

## 97. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:P51691 enables GO:0008081 phosphoric diester hydrolase activity (IDA, PMID:19554727)
- **Field:** GO_ID
- **Change:** GO:0008081 → GO:0016791 (phosphatase activity)
- **Recorded in:** `genes/PSEAE/atsA/atsA-ai-review.yaml`

The PseudoCAP IDA on PA0183 atsA to PMID:19554727 uses GO:0008081 phosphoric diester hydrolase activity. The title and abstract of that paper report hydrolysis of phosphate monoesters (kcat 0.023 s-1, KM 29 microM) and do not mention diesters. GO:0016791 phosphatase activity (hydrolysis of a phosphoric monoester) fits the reported result. Only the abstract was read; if the full text also reports diester hydrolysis the original term could stand for that part. Either way this is a promiscuous activity of the arylsulfatase. This row does not seed a PAINT IBD on the worklist.

> Besides hydrolyzing sulfate monoesters, this enzyme catalyzes the hydrolysis of phosphate monoesters with multiple turnovers
> — PMID:19554727

## 98. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HZW2 involved_in GO:0046247 terpene catabolic process (IDA, PMID:20487029)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0046247
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/atuR/atuR-ai-review.yaml`

PseudoCAP IDA row for PA2885/atuR, GO:0046247 terpene catabolic process, from PMID:20487029 (Forster-Fromme and Jendrossek 2010). The abstract identifies AtuR as a TetR-family repressor of the atu cluster by sequence similarity, constitutive Atu protein expression in the mutant and EMSA binding to the atuA operator. A repressor of catabolic genes is not a participant in the catabolic process, and the only direct assay (EMSA) shows DNA binding. Requested change: delete the row; the regulatory role is already annotated as GO:0045827 and GO:0045892. Abstract-only reading.

> AtuR was identified as a repressor of the atu gene cluster expression by (1) amino acid similarity to TetR repressor family members, (2) constitutive expression of Atu proteins in the atuR insertion mutant and (3) specific binding of purified AtuR homodimers to the atuR-atuA intergenic region in electrophoretic mobility shift assay (EMSA)
> — PMID:20487029

## 99. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HTI9 involved_in GO:0042426 choline catabolic process (IDA, PMID:21478341)
- **Field:** GO_ID
- **Change:** check GO:0042426 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/betT1/betT1-ai-review.yaml`

PA5375 (BetT1, BCCT choline transporter) is annotated involved_in GO:0042426 choline catabolic process (IDA, PMID:21478341). The paper shows choline uptake by BetT1 and a lag on choline in the deletion mutant; the transporter performs no catabolic step. GO:0015871 choline transport describes its role. Consider replacing the row.

## 100. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:P21175 involved_in GO:0042941 D-alanine transmembrane transport (IMP, PMID:18833300)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0042941
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/braC/braC-ai-review.yaml`

GO:0042941 D-alanine transmembrane transport is annotated by IMP to the LIV-I binding protein BraC (PA1074) from PMID:18833300, based on a partial Biolog/plate growth defect on D-alanine of a Tn5 insertion in the first gene of the braCDEFG operon. PMID:31627455 found no D-alanine binding by purified BraC in ITC, while the five LIVAT ligands bind with nanomolar affinity. BraC therefore does not deliver D-alanine; please delete the row.

> ITC experiments revealed binding with nanomolar affinities for the five ligands identified in the study by Hoshino et al. [58] (Figure 6A), whereas no binding was detected for l-Met and d-Ala.
> — PMID:31627455

## 101. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HTI7 enables GO:0005275 amine transmembrane transporter activity (IDA, PMID:19919675)
- **Field:** GO_ID
- **Change:** GO:0005275 → GO:0015418 (ABC-type quaternary ammonium compound transporting activity)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/cbcW/cbcW-ai-review.yaml`

PA5377 (CbcW permease, Q9HTI7) is annotated GO:0005275 amine transmembrane transporter activity, IDA, PMID:19919675. The substrates shown in that paper (choline, glycine betaine, L-carnitine) are quaternary ammonium compounds, which GO does not class as amines. GO:0015418 ABC-type quaternary ammonium compound transporting activity (with contributes_to for a permease subunit) is the accurate term. This row co-seeds the PAINT IBD at PTN000766131.

## 102. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HTI7 involved_in GO:0031457 glycine betaine catabolic process (IDA, PMID:19919675)
- **Field:** GO_ID
- **Change:** check GO:0031457 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/cbcW/cbcW-ai-review.yaml`

PA5377 (CbcW, ABC permease) is annotated involved_in GO:0031457 glycine betaine catabolic process (IDA, PMID:19919675). The evidence is that cbc transposon mutants cannot grow on betaine as sole carbon source, which reflects loss of uptake. The permease does not catalyse any catabolic step. Consider removing the row, or keeping only GO:0031460 glycine betaine transport.

## 103. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HTI7 involved_in GO:0042426 choline catabolic process (IDA, PMID:19919675)
- **Field:** GO_ID
- **Change:** check GO:0042426 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/cbcW/cbcW-ai-review.yaml`

PA5377 (CbcW, ABC permease) is annotated involved_in GO:0042426 choline catabolic process (IDA, PMID:19919675 and PMID:21478341). Both papers show that Cbc is needed for growth on choline as a carbon source, which reflects choline uptake. The permease does not perform any catabolic step. GO:0015871 choline transport already captures its role. Consider removing these rows.

## 104. WRONG_REFERENCE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HTI7 involved_in GO:1902603 carnitine transmembrane transport (IDA, PMID:21478341)
- **Field:** DB:Reference
- **Change:** check PMID:21478341 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/cbcW/cbcW-ai-review.yaml`

GO:1902603 carnitine transmembrane transport for PA5377 (Q9HTI7) cites PMID:21478341 (Malek et al. 2011), whose abstract deals only with choline uptake by CbcXWV, BetT1 and BetT3. The carnitine evidence for CbcWV is in PMID:19919675 (PA14 cbc mutants fail to grow on carnitine, and PAO1 CbcWV restores CaiX-dependent carnitine uptake) and PMID:29517479. If PMID:21478341 has no carnitine data, please re-key the row. It is the sole seed of the PAINT IBD at PTN000766131.

> These transposon mutants also failed to grow on L-carnitine (Fig. S2), suggesting that carnitine is an additional substrate for this transporter.
> — PMID:19919675

## 105. WRONG_EVIDENCE_CODE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HV74 involved_in GO:0000160 phosphorelay signal transduction system (IDA, PMID:11401699)
- **Field:** Evidence_Code
- **Change:** check ECO:0000314 (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/PSEAE/cbrA/cbrA-ai-review.yaml`

involved_in GO:0000160 phosphorelay signal transduction system (IDA) on PA4725 (CbrA) cites Nishijyo et al. 2001 (PMID:11401699). The abstract reports sequence analysis, cbrA/cbrB mutant growth phenotypes, complementation and primer extension, and no phosphorylation assay; IMP or IGI would fit those data. The term itself is appropriate. Only the abstract was available, so a direct assay in the full text cannot be excluded. The row seeds the PAINT IBD GO:0007165 at PTN009166588, which stands on other seeds.

> cbrA and cbrB mutants of strain PAO were found to be unable to use several amino acids (such as arginine, histidine and proline), polyamines and agmatine as sole carbon and nitrogen sources
> — PMID:11401699

## 106. WRONG_REFERENCE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I3N5 involved_in GO:0002049 pyoverdine biosynthetic process (IMP, PMID:16824107)
- **Field:** DB:Reference
- **Change:** PMID:16824107 → PMID:18174132 (Baert et al. 2008, Multiple phenotypic alterations caused by a c-type cytochrome maturation ccmC gene mutation in Pseudomonas aeruginosa)
- **Likely cause:** IDENTIFIER_TRANSPOSITION
- **Recorded in:** `genes/PSEAE/ccmC/ccmC-ai-review.yaml`

The abstract of PMID:16824107 (Feissner et al. 2006, Kranz lab) describes a biochemical study of the CcmA2B1C1 complex releasing holo-CcmE. It does not name the organism (MEDLINE indexes it under Escherichia coli, not Pseudomonas) and describes no mutant phenotypes; the full text was not available here. The pyoverdine, catalase, rhamnolipid, swarming and twitching phenotypes annotated to PA1477 are those of the P. aeruginosa ccmC mutant in the abstract of PMID:18174132. All six PseudoCAP IMP rows on PA1477 dated 2019-03-11 cite PMID:16824107 and should be re-keyed.

> Interestingly, other traits were also strongly affected by the ccmC mutation, including the production of pyocyanin, swarming and twitching motility, and rhamnolipid production.
> — PMID:18174132

## 107. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I3N5 enables GO:0004096 catalase activity (IMP, PMID:16824107)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0004096
- **Recorded in:** `genes/PSEAE/ccmC/ccmC-ai-review.yaml`

enables GO:0004096 catalase activity (IMP) on PA1477 ccmC records the mutant phenotype "catalase production was undetectable" (PMID:18174132) as a molecular function of CcmC. CcmC is a heme-handling subunit of the cytochrome c maturation complex, not a catalase. Please delete this row. It is the sole seed of the PAINT IBD at PTN001247822, which propagates catalase activity to about 143 proteins.

## 108. WRONG_REFERENCE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I3N5 enables GO:0004096 catalase activity (IMP, PMID:16824107)
- **Field:** DB:Reference
- **Change:** PMID:16824107 → PMID:18174132
- **Likely cause:** IDENTIFIER_TRANSPOSITION
- **Recorded in:** `genes/PSEAE/ccmC/ccmC-ai-review.yaml`

The abstract of PMID:16824107 describes CcmABC biochemistry (MEDLINE indexes it under E. coli) and reports no catalase activity; the full text was not available here. The phenotype is reported for the P. aeruginosa ccmC mutant in PMID:18174132.

## 109. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I3N5 involved_in GO:0009247 glycolipid biosynthetic process (IMP, PMID:16824107)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0009247
- **Recorded in:** `genes/PSEAE/ccmC/ccmC-ai-review.yaml`

Reduced rhamnolipid production in a ccmC mutant (PMID:18174132) is an indirect phenotype; CcmC does not take part in glycolipid biosynthesis. The row also appears to cite the wrong paper (PMID:16824107; see the WRONG_REFERENCE defects).

## 110. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I3N5 involved_in GO:0043107 type IV pilus-dependent motility (IMP, PMID:16824107)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0043107
- **Recorded in:** `genes/PSEAE/ccmC/ccmC-ai-review.yaml`

Reduced twitching motility in a ccmC mutant (PMID:18174132) is an indirect phenotype of losing cytochrome c maturation. The row also appears to cite the wrong paper (PMID:16824107; see the WRONG_REFERENCE defects).

## 111. WRONG_REFERENCE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I3N5 involved_in GO:0071977 bacterial-type flagellum-dependent swimming motility (IMP, PMID:16824107)
- **Field:** DB:Reference
- **Change:** check PMID:16824107 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/ccmC/ccmC-ai-review.yaml`

The abstract of PMID:16824107 describes Ccm biochemistry (indexed under E. coli) and no motility data; the full text was not available here. Unlike the other phenotype rows, swimming is in neither abstract, so this call rests on what the abstracts do not say. The P. aeruginosa ccmC mutant phenotypes come from PMID:18174132, whose abstract reports swarming and twitching but not swimming. Please check the source of the swimming-motility row; even if confirmed, it is an indirect phenotype.

## 112. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I3N5 involved_in GO:0071978 bacterial-type flagellum-dependent swarming motility (IMP, PMID:16824107)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0071978
- **Recorded in:** `genes/PSEAE/ccmC/ccmC-ai-review.yaml`

Reduced swarming in a ccmC mutant (PMID:18174132) is an indirect phenotype. The row also appears to cite the wrong paper (PMID:16824107; see the WRONG_REFERENCE defects).

## 113. WRONG_REFERENCE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I3N2 involved_in GO:0002049 pyoverdine biosynthetic process (IMP, PMID:16824107)
- **Field:** DB:Reference
- **Change:** PMID:16824107 → PMID:18174132 (Baert et al. 2008, Multiple phenotypic alterations caused by a c-type cytochrome maturation ccmC gene mutation in Pseudomonas aeruginosa)
- **Likely cause:** IDENTIFIER_TRANSPOSITION
- **Recorded in:** `genes/PSEAE/ccmF/ccmF-ai-review.yaml`

The abstract of PMID:16824107 (Feissner et al. 2006) describes the CcmA2B1C1 complex that releases holo-CcmE; it does not mention CcmF or any mutant phenotype, and its full text could not be read here. All five PseudoCAP IMP rows on PA1480 dated 2019-03-11 (pyoverdine, catalase, twitching, swimming, swarming) cite it, as do the matching rows on ccmC (PA1477). The P. aeruginosa ccmF insertion mutant and its pleiotropic phenotypes are described in PMID:18174132. Please re-key all five rows.

> Non-polar insertions were generated in the Pseudomonas aeruginosa ccmA, ccmC, ccmE, ccmF and ccmH genes, and their impacts on different phenotypes were compared.
> — PMID:18174132

> The ccmC mutant, and to a lesser extent the ccmF mutant, showed a range of other phenotypic changes.
> — PMID:18174132

## 114. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I3N2 enables GO:0004096 catalase activity (IMP, PMID:16824107)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0004096
- **Recorded in:** `genes/PSEAE/ccmF/ccmF-ai-review.yaml`

enables GO:0004096 catalase activity (IMP) on PA1480 ccmF records a mutant phenotype (reduced catalase activity in a cytochrome c maturation mutant) as a molecular function. CcmF is the membrane subunit of the CcmFH heme lyase, not a catalase; the reasoning does not depend on which paper reported the phenotype. Please delete this row. It seeds the PAINT IBD of GO:0016491 at PTN009171456, which happens to be correct for CcmF on other grounds (E. coli CcmF quinol:heme oxidoreductase), so no IBA is lost.

> The ccmC mutant was also found to accumulate porphyrins, and catalase production was undetectable, consistent with the increased sensitivity to hydrogen peroxide.
> — PMID:18174132

> Required for the biogenesis of c-type cytochromes. Possible subunit of a heme lyase (By similarity).
> — file:PSEAE/ccmF/ccmF-uniprot.txt

## 115. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I3N2 involved_in GO:0043107 type IV pilus-dependent motility (IMP, PMID:16824107)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0043107
- **Recorded in:** `genes/PSEAE/ccmF/ccmF-ai-review.yaml`

Reduced twitching motility in a ccm mutant (PMID:18174132) is an indirect phenotype of losing c-type cytochromes. The row also cites the wrong paper (see the WRONG_REFERENCE defect on the pyoverdine row).

## 116. WRONG_REFERENCE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I3N2 involved_in GO:0071977 bacterial-type flagellum-dependent swimming motility (IMP, PMID:16824107)
- **Field:** DB:Reference
- **Change:** check PMID:16824107 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/ccmF/ccmF-ai-review.yaml`

Swimming motility is in neither the cited abstract (Ccm biochemistry, no motility data) nor the abstract of PMID:18174132, so this call rests on what the abstracts do not say. Please check the source of the swimming row; even if confirmed, it is an indirect phenotype.

## 117. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I3N2 involved_in GO:0071978 bacterial-type flagellum-dependent swarming motility (IMP, PMID:16824107)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0071978
- **Recorded in:** `genes/PSEAE/ccmF/ccmF-ai-review.yaml`

Reduced swarming in a ccm mutant (PMID:18174132) is an indirect phenotype. The row also cites the wrong paper (see the WRONG_REFERENCE defect on the pyoverdine row).

## 118. WRONG_QUALIFIER (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I3G4 enables GO:0004129 cytochrome-c oxidase activity (IMP, PMID:14763990)
- **Field:** Qualifier
- **Change:** enables → contributes_to
- **Likely cause:** SCOPE_OVER_REACH
- **Recorded in:** `genes/PSEAE/ccoO1/ccoO1-ai-review.yaml`

GO:0004129 cytochrome-c oxidase activity on ccoO1 (Q9I3G4) is coded enables, IMP, PMID:14763990. The abstract describes the loss of whole cbb3 isoforms, and PseudoCAP entered the identical row on 20190311 for all eight subunits of both cbb3 operons, so one operon-level phenotype was transferred to each subunit. CcoO is the monoheme cytochrome c that passes electrons to the catalytic heme b3-CuB centre on CcoN; it contributes to the complex's activity. The same correction was requested from the ccoP1 and ccoP2 reviews for the CcoP chains, and the ccoN1/ccoN2 rows are left as enables because subunit I does carry the catalytic centre. Full text not read, so a ccoO-specific experiment cannot be excluded.

> only loss of cbb3-1 influenced growth
> — PMID:14763990

## 119. WRONG_QUALIFIER (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I3G1 enables GO:0004129 cytochrome-c oxidase activity (IMP, PMID:14763990)
- **Field:** Qualifier
- **Change:** enables → contributes_to
- **Likely cause:** SCOPE_OVER_REACH
- **Recorded in:** `genes/PSEAE/ccoO2/ccoO2-ai-review.yaml`

GO:0004129 cytochrome-c oxidase activity on ccoO2 (Q9I3G1) is coded enables, IMP, PMID:14763990. The abstract describes the loss of whole cbb3 isoforms, and PseudoCAP entered the identical row on 20190311 for all eight subunits of both cbb3 operons, so one operon-level phenotype was transferred to each subunit. CcoO is the monoheme cytochrome c that passes electrons to the catalytic heme b3-CuB centre on CcoN; it contributes to the complex's activity. The same correction was requested from the ccoP1 and ccoP2 reviews for the CcoP chains, and the ccoN1/ccoN2 rows are left as enables because subunit I does carry the catalytic centre. Full text not read, so a ccoO-specific experiment cannot be excluded.

> only loss of cbb3-1 influenced growth
> — PMID:14763990

## 120. WRONG_QUALIFIER (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I3G5 enables GO:0004129 cytochrome-c oxidase activity (IMP, PMID:14763990)
- **Field:** Qualifier
- **Change:** enables → contributes_to
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/ccoP1/ccoP1-ai-review.yaml`

GO:0004129 cytochrome-c oxidase activity on ccoP1 (Q9I3G5) is coded enables, IMP, PMID:14763990. The abstract describes the loss of whole cbb3 isoforms, and PseudoCAP entered the identical row on 20190311 for all eight subunits of both cbb3 operons (ccoN1/O1/Q1/P1 and ccoN2/O2/Q2/P2), so the row transfers an operon-level phenotype to each subunit. CcoP is the diheme cytochrome c that passes electrons to the catalytic heme b3-CuB centre on CcoN; it contributes to the complex's activity. The row seeds the PAINT IBD at PTN002435498. Full text not read, so a ccoP-specific experiment cannot be excluded.

> only loss of cbb3-1 influenced growth
> — PMID:14763990

## 121. WRONG_QUALIFIER (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I3G2 enables GO:0004129 cytochrome-c oxidase activity (IMP, PMID:14763990)
- **Field:** Qualifier
- **Change:** enables → contributes_to
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/ccoP2/ccoP2-ai-review.yaml`

GO:0004129 cytochrome-c oxidase activity on ccoP2 (Q9I3G2) is coded enables, IMP, PMID:14763990. The abstract describes the loss of whole cbb3 isoforms, and PseudoCAP entered the identical row on 20190311 for all eight subunits of both cbb3 operons (ccoN1/O1/Q1/P1 and ccoN2/O2/Q2/P2), so the row transfers an operon-level phenotype to each subunit. CcoP is the diheme cytochrome c that passes electrons to the catalytic heme b3-CuB centre on CcoN; it contributes to the complex's activity. The row seeds the PAINT IBD at PTN002435498. Full text not read, so a ccoP-specific experiment cannot be excluded.

> only loss of cbb3-1 influenced growth
> — PMID:14763990

## 122. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q51434 involved_in GO:0071978 bacterial-type flagellum-dependent swarming motility (IMP, PMID:7860605)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0071978
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/cheZ/cheZ-ai-review.yaml`

The PseudoCAP IMP row annotates PA1457/cheZ to flagellum-dependent swarming motility from Masduki et al. 1995. The abstract describes chemotaxis mutants selected on swarm plates that were fully motile but failed to spread because of a signalling defect, and the cheZ single mutant was phenotyped by swimming reversals. That is chemotaxis, already annotated from the same paper (GO:0006935), not surface swarming. PROBABLE because only the abstract could be read. This row does not seed a PAINT IBD.

> These mutants were fully motile but incapable of swarming, suggesting that they had a defect in the intracellular signalling pathway.
> — PMID:7860605

## 123. WRONG_REFERENCE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HZR3 involved_in GO:2001226 negative regulation of chloride transport (IDA, PMID:16236828)
- **Field:** DB:Reference
- **Change:** check PMID:16236828 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/cif/cif-ai-review.yaml`

involved_in GO:2001226 negative regulation of chloride transport (IDA) on PA2934 (cif) cites PMID:16236828 (Swiatecka-Urban et al. 2006). That study is described in its abstract as using an unfractionated cell-free filtrate of P. aeruginosa, and it predates the identification of the factor: the abstract attributes the effect to the filtrate and names no protein. The full text was not available here (no PMC copy, rechecked 2026-10-29), so this rests on the abstract. The attribution to PA2934 was made in PMID:17502391 (MacEachran et al. 2007), where purified six-His-tagged Cif was shown to be necessary and sufficient to reduce apical-membrane CFTR and CFTR-mediated chloride secretion, and the mechanism was resolved in PMID:21455491. Please consider re-pointing the reference to PMID:17502391 (optionally keeping PMID:16236828 as a second row with an appropriate code). The annotation itself is correct; the question is only whether the cited evidence identifies the gene product.

> report herein that a cell-free filtrate of P. aeruginosa reduced CFTR-mediated
> — PMID:16236828

> sufficient to mediate the reduction in apical membrane expression of CFTR and a
> — PMID:17502391

## 124. WRONG_QUALIFIER (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I1Y5 involved_in GO:0007155 cell adhesion (IMP, PMID:11381121)
- **Field:** Qualifier
- **Change:** involved_in → acts_upstream_of_or_within
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/cupA3/cupA3-ai-review.yaml`

GO:0007155 cell adhesion is annotated involved_in, by IMP, to the CupA usher CupA3 (PA2130) from PMID:11381121 (full text read). The paper shows reduced attachment of a cupA3 mutant; CupA3 is the outer-membrane usher that assembles the fimbria, and the adhesion is made by the fimbrial subunits. Please change the qualifier to acts_upstream_of_or_within (as EcoCyc does for E. coli HtrE), or repoint the row to GO:0009297 pilus assembly. This row seeds the PTN001252526 IBD.

> This strain, carrying a disrupted cupA3 gene, showed an adhesion-deficient phenotype, with only 10% of the bacteria adhering relative to the parental PAK-NP
> — PMID:11381121

## 125. WRONG_QUALIFIER (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I1Y5 involved_in GO:0007155 cell adhesion (IMP, PMID:15090530)
- **Field:** Qualifier
- **Change:** check involved_in (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/cupA3/cupA3-ai-review.yaml`

GO:0007155 cell adhesion is annotated involved_in, by IMP, to CupA3 (PA2130) from PMID:15090530, an MvaT regulation paper. The abstract only restates that the cupA cluster is needed for biofilm formation; I could not read the full text to see whether a cupA3 mutant is assayed. If it is, the usher still acts upstream of adhesion (see the PMID:11381121 row); please check, and use acts_upstream_of_or_within.

> The cupA gene cluster, but not the cupB or cupC cluster, is required for biofilm formation on abiotic surfaces.
> — PMID:15090530

## 126. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:G3XCU6 involved_in GO:0019344 L-cysteine biosynthetic process (IMP, PMID:9218775)
- **Change:** delete the record asserting GO:0019344
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/cysB/cysB-ai-review.yaml`

GO:0019344 L-cysteine biosynthetic process (IMP, PMID:9218775) for cysB PA1754 (G3XCU6) appears to record that a cysB insertion mutant is a cysteine auxotroph, the phenotype its abstract reports (the full text was not read). CysB is a LysR-type transcriptional activator of the cys regulon and catalyses no step of cysteine synthesis, so the phenotype shows necessity, not participation. Please remove the row (CysB's regulatory role is captured by GO:0045893, IDA, PMID:20370820). This row is the sole seed of the PAINT IBD at PTN002824317.

> A CysB-deficient mutant of CHA, constructed by insertional inactivation of cysB, was a cysteine auxotroph
> — PMID:9218775

## 127. WRONG_REFERENCE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HU99 enables GO:0008718 D-amino-acid dehydrogenase activity (IDA, PMID:17021207)
- **Field:** Reference
- **Change:** delete the record asserting PMID:17021207
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/dadA2/dadA2-ai-review.yaml`

GO:0008718 IDA on dadA2 (PA5084, Q9HU99) cites PMID:17021207, a study of the AauR-AauS two-component system and acidic amino acid uptake in Pseudomonas putida KT2440 (full text read; the title names P. putida). The paper does not mention DadA, PA5084 or any D-amino acid dehydrogenase assay. No paper assaying the PA5084 product was found (PubMed search for PA5084/dadA2). Please delete the row or re-cite it to a paper that assayed PA5084; otherwise the activity is only a homology inference. The row is one of three seeds of the PAINT IBD at PTN008552203, which stands on the other two (E. coli DadA, P. aeruginosa DadA1), so no change to the IBD content is needed.

> Here, we show that the two-component system encoded by PP1067-PP1066 ( aauS-aauR ) is required for efficient growth of P. putida KT2440 on acidic amino acids (Glu and Asp) and their amides (Gln and Asn).
> — PMID:17021207

## 128. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HTG5 enables GO:0047865 dimethylglycine dehydrogenase activity (IDA, PMID:17951379)
- **Field:** Evidence_Code
- **Change:** ECO:0000314 → ECO:0000315 (IMP (inferred from mutant phenotype))
- **Recorded in:** `genes/PSEAE/dgcB/dgcB-ai-review.yaml`

enables GO:0047865 dimethylglycine dehydrogenase activity (IDA) and enables GO:0047866 dimethylglycine oxidase activity (IDA) on PA5399 (dgcB) both cite PMID:17951379, a genetic study whose evidence for dgcAB is the inability of transposon mutants to grow on dimethylglycine and the accumulation of 13C-labelled dimethylglycine in them. No enzyme was assayed; the full text states that characterisation of the biochemical activities of the dgcA and dgcB gene products remains a subject for future research. IMP therefore fits both rows better than IDA. The companion process rows from the same paper are already coded IMP.

> with mutations in the dgcAB (PA5398-PA5399) genes, which exhibit homology to
> — PMID:17951379

## 129. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HTG5 enables GO:0047865 dimethylglycine dehydrogenase activity (IDA, PMID:17951379)
- **Field:** GO_Term
- **Change:** check GO:0047865 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/dgcB/dgcB-ai-review.yaml`

PA5399 (dgcB) carries both GO:0047865 dimethylglycine dehydrogenase activity and GO:0047866 dimethylglycine oxidase activity from the same reference. The two terms describe incompatible reactions: GO:0047865 uses an electron-transfer flavoprotein as acceptor, GO:0047866 uses O2 and releases H2O2. One enzyme system does one or the other, and PMID:17951379 measured neither; it established genetically that dgcA and dgcB are required for the dimethylglycine to sarcosine conversion. In addition, the methyl-removing activity is more plausibly DgcA's: PA5398 is described in that paper as a predicted flavin mononucleotide oxidoreductase similar to a putative N-methylproline demethylase, whereas PA5399 is described as a probable membrane-spanning ferredoxin Fe-S oxidoreductase and carries five predicted transmembrane helices, two 4Fe-4S ferredoxin domains and two CCG domains, the architecture of the electron-transfer subunit in its PANTHER family (PTHR43255: heterodisulfide reductase subunit C, FadF, EtfAB:quinone oxidoreductase). Please consider replacing the two specific activity rows on PA5399 with a generic oxidoreductase or iron-sulfur electron-transfer claim, or qualifying them as contributes_to on the DgcAB system, until the reaction and the acceptor have been measured. These rows are the sole seeds of the PAINT IBD at PTN000229983, which propagates an oxidoreductase annotation to 33 leaves.

> A single enzyme system does one or the other.
> — file:PSEAE/dgcB/dgcB-notes.md

> /note="4Fe-4S ferredoxin-type"
> — file:PSEAE/dgcB/dgcB-uniprot.txt

## 130. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:G3XD14 involved_in GO:0045861 negative regulation of proteolysis (IDA, PMID:11160083)
- **Change:** delete the record asserting GO:0045861
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/dksA/dksA-ai-review.yaml`

GO:0045861 negative regulation of proteolysis (IDA, PMID:11160083) for dksA PA4723 records that multicopy dksA reduced elastase production. That is decreased production of a secreted protease, which the authors attribute to indirect inhibition of rhlI transcription; it is not regulation of proteolysis. Please remove the row.

> In trans, dksA suppressed the elastase production of mutant PR1-E4 and reduced the rhamnolipid production of both PR1-E4 and PAO1.
> — PMID:11160083

## 131. WRONG_REFERENCE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:G3XD14 enables GO:0070063 RNA polymerase binding (IDA, PMID:21255113)
- **Field:** DB:Reference
- **Change:** check PMID:21255113 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/dksA/dksA-ai-review.yaml`

GO:0070063 RNA polymerase binding (IDA) for dksA PA4723 cites PMID:21255113, whose biochemistry is on the paralog DksA2 (PA5536) with E. coli RNAP. Co-purification of PA4723 DksA with RNAP subunits is reported in PMID:15853892. Please check whether the row was meant for PA5536 or should cite PMID:15853892.

> In vitro, purified DksA2 stabilizes the closed promoter complex at, and thus inhibits transcription from, the rrnB P1 promoter
> — PMID:21255113

## 132. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:O33407 involved_in GO:0009247 glycolipid biosynthetic process (IMP, PMID:17631636)
- **Field:** GO_ID
- **Change:** check GO:0009247 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/estA/estA-ai-review.yaml`

PseudoCAP IMP glycolipid biosynthetic process on EstA (O33407, PA5112) from PMID:17631636 records reduced rhamnolipid in an estA deletion mutant. EstA is a surface-exposed outer-membrane carboxylesterase and the step it affects is unknown, so the evidence supports necessity, not participation; rhamnolipid output may be several steps downstream of whatever EstA does. This is an over-annotation: the phenotype shows that EstA stands in some causal relationship to rhamnolipid production, which could be regulation, but not that it is involved_in the biosynthetic process. Please consider removing the row, or replacing it with a regulation term if the full text supports one. It is the sole seed of the PAINT lipid biosynthetic process IBD at PTN005219546 (960 leaf IBAs).

## 133. WRONG_TERM (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:O33407 involved_in GO:0071973 bacterial-type flagellum-dependent cell motility (IMP, PMID:17631636)
- **Field:** GO_ID
- **Change:** check GO:0071973 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/estA/estA-ai-review.yaml`

PseudoCAP IMP bacterial-type flagellum-dependent cell motility on EstA (O33407) from PMID:17631636. The estA mutant loses swimming, swarming and twitching alike, so the defect is not specific to the flagellar machinery, and EstA (a surface esterase) is not a flagellar component. The phenotype is most plausibly pleiotropic, so even the general cell motility term (annotated by UniProt from the same paper) overstates participation; please check whether the row should be removed.

## 134. WRONG_EVIDENCE_CODE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:O33407 involved_in GO:0071978 bacterial-type flagellum-dependent swarming motility (IDA, PMID:20360178)
- **Field:** Evidence_Code
- **Change:** ECO:0000314 → ECO:0000315 (IMP (mutant phenotype, includes overexpression))
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/estA/estA-ai-review.yaml`

PseudoCAP IDA for swarming motility on EstA (O33407) from PMID:20360178 rests on an estA overexpression strain showing enhanced swarming; an overexpression phenotype is coded IMP in GO. The authors also state the effect may be indirect.

## 135. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:P26993 involved_in GO:0050709 negative regulation of protein secretion (IMP, PMID:1655713)
- **Field:** GO_ID
- **Change:** check GO:0050709 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/exsA/exsA-ai-review.yaml`

The IMP row codes ExsA to GO:0050709 negative regulation of protein secretion from PMID:1655713. ExsA is a transcriptional activator of the T3SS operons, so its molecular action is regulation of transcription (already annotated), not regulation of secretion, and the secretion defect of an exsA mutant is indirect, through loss of apparatus transcription. The sign is also inverted: the cited abstract states ExsA is required for (activates) exoenzyme S production. Suggested change: remove this term; the activation of T3SS gene transcription is captured by GO:2000144 / GO:0001216. PROBABLE: the 1655713 full text was not read.

> The ExsA gene product appeared to be required for induction of exoenzyme S synthesis above a low basal level.
> — PMID:1655713

## 136. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HVN0 enables GO:0016888 DNA endonuclease activity, producing 5'-phosphomonoesters (IDA, PMID:18174131)
- **Field:** GO_ID
- **Change:** check GO:0016888 (alternatives in the explanation)
- **Likely cause:** IDENTIFIER_TRANSPOSITION
- **Recorded in:** `genes/PSEAE/fimT/fimT-ai-review.yaml`

enables GO:0016888 "DNA endonuclease activity, producing 5'-phosphomonoesters" (IDA, PMID:18174131, 2019-03-11) on PA4549 fimT (Q9HVN0). A live QuickGO query shows the four PseudoCAP rows from this paper, all dated 2019-03-11: PA4526 pilB and PA0395 pilT to GO:0016887 ATP hydrolysis activity, and PA0396 pilU and PA4549 fimT to GO:0016888, the next GO id. GO:0016888 is the same keying slip already reported for the pilU row. FimT is a GspH-family minor pilin with no nuclease domain, so GO:0016888 is wrong for it. GO:0016887 is not the correction here either, because FimT is not an ATPase; see the companion WRONG_GENE_PRODUCT defect, which asks for the row to be deleted.

> Assay of purified 6xHis-tagged PilB, PilT and PilU from P. aeruginosa showed that all three proteins have ATPase activities in vitro.
> — PMID:18174131

## 137. WRONG_GENE_PRODUCT (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HVN0 enables GO:0016888 DNA endonuclease activity, producing 5'-phosphomonoesters (IDA, PMID:18174131)
- **Field:** DB_Object_ID
- **Change:** delete the record asserting UniProtKB:Q9HVN0
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/PSEAE/fimT/fimT-ai-review.yaml`

The PA4549 fimT row enables GO:0016888 (IDA, PMID:18174131) appears to be a duplicate of the PA0396 pilU row (same paper, same wrong GO id, same date) attached to the wrong gene product. Chiang et al. 2008 purified and mutated the type IV pilus NTPases PilB, PilT and PilU (stated in the abstract); FimT is a minor pilin, not an NTPase, and is not mentioned in the abstract. Since pilU already has its own row (separately reported for repointing to GO:0016887), please delete the fimT row rather than repoint it. We could read only the abstract; if the full text does report an experiment on FimT, please re-key the row to the term that experiment supports.

> In Pseudomonas aeruginosa, PilB and PilT are bipolar proteins belonging to the secretion NTPase superfamily, and power pilus extension and retraction, respectively, while the unipolar PilT paralogue PilU supports pilus retraction in an unknown manner.
> — PMID:18174131

## 138. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

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

## 139. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:G3XCV0 involved_in GO:0006351 DNA-templated transcription (IDA, PMID:9287015)
- **Field:** GO_ID
- **Change:** GO:0006351 → GO:0045893 (positive regulation of DNA-templated transcription)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/fleQ/fleQ-ai-review.yaml`

The PseudoCAP IDA row for PA1097/fleQ from PMID:9287015 uses the transcription process term for an activator. The abstract states that promoter fusions show fleSR regulated by RpoN and FleQ, which is positive regulation of transcription. Abstract only, so PROBABLE.

> Promoter fusion experiments showed that the fleSR operon was regulated by RpoN and FleQ.
> — PMID:9287015

## 140. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:G3XCV0 involved_in GO:2000155 positive regulation of cilium-dependent cell motility (IMP, PMID:12218010)
- **Field:** GO_ID
- **Change:** GO:2000155 → GO:1902210 (positive regulation of bacterial-type flagellum assembly)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/fleQ/fleQ-ai-review.yaml`

GO:2000155 positive regulation of cilium-dependent cell motility is only_in_taxon Eukaryota (live QuickGO query), so it cannot apply to P. aeruginosa. The full text of PMID:12218010 (read) is about FleQ binding and activating flagellar promoters.

> Direct interaction of FleQ with flhA , fliE , fliL , and fleSR promoters was demonstrated by gel shift assay, along with experiments to conclusively determine the specificity of its binding.
> — PMID:12218010

## 141. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I4N4 involved_in GO:0000160 phosphorelay signal transduction system (IDA, PMID:7591148)
- **Field:** Evidence_Code
- **Change:** check ECO:0000314 (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/PSEAE/fleS/fleS-ai-review.yaml`

involved_in GO:0000160 phosphorelay signal transduction system (IDA) on PA1098 (FleS) cites Ritchings et al. 1995 (PMID:7591148). The abstract describes FleS from sequence homology only ("shows strong homology to histidine kinases") and lists as evidence a fleR insertion mutant, its complementation, and Western blot and electron microscopy of that fleR mutant. No direct assay on FleS (for example, autophosphorylation or phosphotransfer to FleR) is listed. The term suits FleS; please check the evidence code (ISS, or IGI/IMP if a fleS mutant is reported in the full text). The row seeds the PAINT IBD GO:0007165 at PTN009166588, which stands on other seeds.

> FleS has a predicted molecular mass of 43.87 kDa and shows strong homology to histidine kinases which in other two-component systems have been shown to be sensor proteins
> — PMID:7591148

## 142. WRONG_EVIDENCE_CODE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:P72151 involved_in GO:0071973 bacterial-type flagellum-dependent cell motility (IDA, PMID:9423837)
- **Field:** Evidence_Code
- **Change:** ECO:0000314 → ECO:0000315
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/fliC/fliC-ai-review.yaml`

Full text of PMID:9423837 read. The only motility data are that fliC disruption mutants of strain PAK (and PAK/NP) were identified as nonmotile; no direct assay of flagellin in motility is reported, so the evidence is IMP. The mutants were made in PAK, which carries the a-type flagellin, not in PAO1 (b-type, P72151); PAO1 appears only in adherence assays. The GO term is correct for flagellin; consider also noting the strain, or using ISS from the PAK flagellin.

> Fla − mutants of PAK and PAK/NP were isolated by gene replacement.
> — PMID:9423837

## 143. WRONG_REFERENCE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HV49 enables GO:0004156 dihydropteroate synthase activity (IDA, PMID:1657875)
- **Field:** DB:Reference
- **Change:** delete the record asserting PMID:1657875
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/PSEAE/folP/folP-ai-review.yaml`

The PseudoCAP IDA GO:0004156 on PA4750 folP (Q9HV49) cites PMID:1657875, whose abstract states that HPPK and DHPS were purified from Escherichia coli MC4100. No P. aeruginosa enzyme was studied, so the row is direct evidence for E. coli FolP, not for PA4750. Please delete the row (the IBA and the IEA carry the claim) or supply a P. aeruginosa reference. The row is one of six seeds of PTN000468650; the IBD stands on the other five.

> were purified to homogeneity from crude extracts of Escherichia coli MC4100
> — PMID:1657875

## 144. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q03456 involved_in GO:1901668 regulation of superoxide dismutase activity (IMP, PMID:8763923)
- **Change:** check GO:1901668 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/fur/fur-ai-review.yaml`

GO:1901668 regulation of superoxide dismutase activity (IMP, PMID:8763923) for P. aeruginosa Fur (Q03456). The paper shows altered Mn-SOD levels in fur mutants and Fur binding to the iron boxes of the sodA operon, i.e. transcriptional control of sodA expression, not modulation of enzyme activity. Consider removing the row or replacing it with negative regulation of DNA-templated transcription (with a has_input/regulates extension to sodA if wanted).

> Purified wild-type Fur bound more avidly than mutant Fur to a PCR product containing two palindromic 19-bp "iron box" regions controlling expression of an operon containing the sodA gene that encodes Mn-SOD.
> — PMID:8763923

## 145. WRONG_EVIDENCE_CODE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HTF3 enables GO:0016491 oxidoreductase activity (IDA, PMID:17951379)
- **Field:** Evidence_Code
- **Change:** check IDA (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/gbcB/gbcB-ai-review.yaml`

PseudoCAP row for gbcB (PA5411, Q9HTF3), GO:0016491 oxidoreductase activity, IDA, PMID:17951379 (Wargo et al. 2008). The abstract reports transposon mutants that cannot grow on glycine betaine and 13C-choline NMR showing gbcAB are needed for GB to DMG conversion, which is mutant evidence (IMP). The term is right. Only the abstract was read; please check whether the full text contains a direct enzyme assay before changing the code.

> Subsequent nuclear magnetic resonance (NMR) experiments with 1,2-(13)C-labeled choline indicated that these genes are necessary for conversion of GB to DMG.
> — PMID:17951379

## 146. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HTI4 involved_in GO:0010518 positive regulation of phospholipase activity (IMP, PMID:19103776)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0010518
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/gbdR/gbdR-ai-review.yaml`

GO:0010518 positive regulation of phospholipase activity is annotated to the AraC-family activator GbdR (PA5380) from PMID:19103776. The full text shows that GbdR binds the plcH promoter and activates its transcription; the loss of PlcH activity in the mutant follows from lost induction. GbdR does not modulate the enzyme. Please delete the row; the transcriptional role is already captured by GO:0045893.

> In electrophoretic mobility shift assays, a GbdR-maltose binding protein fusion bound specifically to both the plcH and pchP promoters.
> — PMID:19103776

## 147. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HTI4 involved_in GO:0010922 positive regulation of phosphatase activity (IMP, PMID:19103776)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0010922
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/gbdR/gbdR-ai-review.yaml`

GO:0010922 positive regulation of phosphatase activity is annotated to GbdR (PA5380) from PMID:19103776. The full text shows GbdR binding the pchP promoter and activating pchP transcription; it does not act on PchP. Please delete the row.

> In electrophoretic mobility shift assays, a GbdR-maltose binding protein fusion bound specifically to both the plcH and pchP promoters.
> — PMID:19103776

## 148. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HTI4 involved_in GO:0031457 glycine betaine catabolic process (IMP, PMID:17951379)
- **Field:** GO_ID
- **Change:** GO:0031457 → GO:0009896 (positive regulation of catabolic process)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/gbdR/gbdR-ai-review.yaml`

GO:0031457 glycine betaine catabolic process is annotated by IMP to the AraC-family regulator GbdR (PA5380) from PMID:17951379, whose abstract identifies gbdR as a predicted regulator required for induction of the catabolic genes gbcAB and dgcAB. PMID:24097953 (full text) shows GbdR directly activates transcription of those genes. GbdR performs no step of GB catabolism; please repoint to GO:0009896, which PseudoCAP already asserts from the same paper.

> Our screen also identified a predicted AraC
> — PMID:17951379

> as it directly regulates transcription of the genes involved in all steps of conversion from GB to pyruvate
> — PMID:24097953

## 149. WRONG_TERM (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HT24 involved_in GO:0032885 regulation of polysaccharide biosynthetic process (IMP, PMID:14982774)
- **Field:** GO_ID
- **Change:** check GO:0032885 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/glmR/glmR-ai-review.yaml`

The PseudoCAP IMP for regulation of polysaccharide biosynthetic process on GlmR (PA5550) from PMID:14982774 appears to rest on the authors' suggestion that glmS repression may affect peptidoglycan and LPS precursor pools. Please check whether the full text measures polysaccharide (LPS or peptidoglycan) synthesis in the mutant; if not, the row is an indirect inference and should be removed.

> We showed that GlmR represses the transcription of the adjacent glmS homologue (PA5549) in P. aeruginosa, possibly affecting the pool of precursors for peptidoglycan and LPS synthesis.
> — PMID:14982774

## 150. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HT24 involved_in GO:0045724 positive regulation of cilium assembly (IMP, PMID:14982774)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0045724
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/glmR/glmR-ai-review.yaml`

GO:0045724 positive regulation of cilium assembly is annotated to the P. aeruginosa DeoR-family repressor GlmR (PA5550) from PMID:14982774. GO defines the cilium as a specialized eukaryotic organelle, so the term is wrong for a bacterium regardless of the paper's content. The underlying observation, loss of motility of the pleiotropic glmR mutant, is an indirect phenotype. Please delete the row.

> The drug supersusceptibility of 19A was accompanied by loss of motility, reduced resistance to osmotic and heat shock stress, and impaired growth at low temperatures.
> — PMID:14982774

## 151. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HT24 involved_in GO:2000147 positive regulation of cell motility (IMP, PMID:14982774)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:2000147
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/glmR/glmR-ai-review.yaml`

The PseudoCAP IMP for positive regulation of cell motility on GlmR (PA5550) from PMID:14982774 records loss of motility of a transposon mutant that is also filamentous, stress-sensitive and antibiotic hypersusceptible. The abstract names glmS as the only GlmR target. Loss of motility is therefore an indirect consequence of an envelope defect, not a regulatory role. PROBABLE because the full text was not read.

> The drug supersusceptibility of 19A was accompanied by loss of motility, reduced resistance to osmotic and heat shock stress, and impaired growth at low temperatures.
> — PMID:14982774

## 152. WRONG_EVIDENCE_CODE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:P14165 involved_in GO:0006099 tricarboxylic acid cycle (IDA, PMID:7626013)
- **Field:** Evidence_Code
- **Change:** check ECO:0000314 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/gltA/gltA-ai-review.yaml`

GO:0006099 tricarboxylic acid cycle for gltA (PA1580, P14165) is annotated IDA to PMID:7626013. The abstract reports purification and characterisation of two citrate synthase isoenzymes and does not assay TCA cycle function; the process follows from the activity. IC (with GO:0036440 from the same paper) would be the accurate code. The row is the sole seed of the PAINT IBD at PTN002450857 (18 leaf IBAs); the IBD conclusion is sound, so only the seed evidence needs attention.

> CSI and CSII were also shown to be distinct kinetically, immunologically and in terms of their regulatory properties.
> — PMID:7626013

## 153. WRONG_REFERENCE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:P29365 enables GO:0004412 homoserine dehydrogenase activity (IDA, PMID:10220164)
- **Field:** DB:Reference
- **Change:** check PMID:10220164 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/hom/hom-ai-review.yaml`

enables GO:0004412 and involved_in GO:0009088 (both IDA) on PA3736 hom cite Patte et al. 1999 (PMID:10220164). That abstract concerns only ThrB and the ThrH homoserine kinase isozyme and never mentions homoserine dehydrogenase; the same PMID was attached to thrB, hom and thrH on the same date. Unless the full text contains an HDH assay, the supporting reference should be PMID:1333566, which reports HDH activity and threonine feedback inhibition of the cloned P. aeruginosa hom product. The annotations themselves are correct.

> In P. aeruginosa, threonine auxotrophy is observed only when both thrB and thrH are simultaneously inactivated.
> — PMID:10220164

> HDH activity was feedback inhibited by threonine
> — PMID:1333566

## 154. WRONG_REFERENCE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:P29365 involved_in GO:0009088 L-threonine biosynthetic process (IDA, PMID:10220164)
- **Field:** DB:Reference
- **Change:** check PMID:10220164 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/hom/hom-ai-review.yaml`

involved_in GO:0009088 (IDA) on PA3736 hom cites PMID:10220164, whose abstract concerns only ThrB and ThrH. This row is the sole seed of the PTN000752178 threonine biosynthesis IBD. The claim is correct, but its support should be PMID:1333566 unless the 1999 full text assays Hom.

> In P. aeruginosa, threonine auxotrophy is observed only when both thrB and thrH are simultaneously inactivated.
> — PMID:10220164

## 155. WRONG_REFERENCE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HU77 involved_in GO:0006548 L-histidine catabolic process (IMP, PMID:4290562)
- **Field:** DB:Reference
- **Change:** check PMID:4290562 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/hutF/hutF-ai-review.yaml`

The full text of Lessie and Neidhardt 1967 (J Bacteriol 93, 1800-1810; supplied by the user, read 2026-11-05) measures step IV only as formiminoglutamate degradation by crude extracts, an activity that in PAO1 comes from both HutF/HutG and HutE (PA3175), and its mutants are a urocanase-deficient strain, a histidine auxotroph and regulatory mutants; there is no hutF mutant. The IMP for GO:0006548 on PA5106 therefore has no support in this paper. Please re-key it to PMID:16475788 (direct enzymology placing PA5106 in the hut pathway, IDA). The annotation is biologically correct. This row is the sole seed of the PANTHER IBD at PTN000138516.

> Histidine ammonia lyase (histidase), urocanase, and the capacity to degrade formiminoglutamate, which are respectively involved in steps I, II, and IV in the catabolism of histidine
> — PMID:4290562

## 156. WRONG_EVIDENCE_CODE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HU85 enables GO:0004397 histidine ammonia-lyase activity (IMP, PMID:4290562)
- **Field:** Evidence_Code
- **Change:** check ECO:0000315 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/hutH/hutH-ai-review.yaml`

The full text of Lessie and Neidhardt 1967 (J Bacteriol 93, 1800-1810; supplied by the user, read 2026-11-05) assays histidase directly in crude extracts, partly purifies it about 10-fold, and characterises it (molecular weight about 210,000 by sucrose gradient; Km for histidine 1.8 to 2 mM; inhibition by pyrophosphate). It describes no histidase- deficient structural mutant; its mutants are a urocanase-deficient strain, a histidine auxotroph and regulatory mutants with altered repression. The evidence for GO:0004397 on PA5098 is therefore a direct assay, so IDA rather than IMP. The companion IMP for GO:0006548 rests on the same paper. The annotation itself is correct.

> The molecular weight of partially purified histidase was estimated at 210,000 by sucrose gradient centrifugation.
> — PMID:4290562

## 157. WRONG_REFERENCE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HU91 involved_in GO:0006548 L-histidine catabolic process (IMP, PMID:4290562)
- **Field:** DB:Reference
- **Change:** check PMID:4290562 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/hutI/hutI-ai-review.yaml`

The full text of Lessie and Neidhardt 1967 (J Bacteriol 93, 1800-1810; supplied by the user, read 2026-11-05) assays histidase (step I), urocanase (step II) and formiminoglutamate degradation (step IV) in crude extracts and partly purifies histidase. It never assays imidazolonepropionase (step III), and its mutants are a urocanase-deficient strain, a histidine auxotroph and regulatory mutants with altered repression; there is no hutI mutant, and the study predates any gene assignment. The IMP for GO:0006548 on PA5092 therefore has no support in this paper. Please withdraw it or re-key it to a paper with a genetically defined hutI mutant. The annotation is biologically correct, so ISS or IBA support from the HutI family would be the honest alternative. This row is the sole seed of the PANTHER IBD at PTN000505272.

> Histidine ammonia lyase (histidase), urocanase, and the capacity to degrade formiminoglutamate, which are respectively involved in steps I, II, and IV in the catabolism of histidine
> — PMID:4290562

## 158. WRONG_REFERENCE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HU91 enables GO:0050480 imidazolonepropionase activity (IMP, PMID:4290562)
- **Field:** DB:Reference
- **Change:** check PMID:4290562 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/hutI/hutI-ai-review.yaml`

The full text of Lessie and Neidhardt 1967 (J Bacteriol 93, 1800-1810; supplied by the user, read 2026-11-05) assays steps I, II and IV of histidine degradation but never imidazolonepropionase (step III), and describes no hutI mutant. The IMP for GO:0050480 on PA5092 therefore has no support in this paper; please withdraw it or re-key it. The function is better supported by ISS or IBA to the HutI family. This row is the sole seed of the PANTHER IBD at PTN000505272 (52 leaf IBAs).

> Histidine ammonia lyase (histidase), urocanase, and the capacity to degrade formiminoglutamate, which are respectively involved in steps I, II, and IV in the catabolism of histidine
> — PMID:4290562

## 159. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HZQ8 involved_in GO:0015628 protein secretion by the type II secretion system (IDA, PMID:9642203)
- **Field:** GO_ID
- **Change:** check GO:0015628 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/lap/lap-ai-review.yaml`

PA2939 (PaAP) is a cargo of the Xcp type II secretion system, not a component of it. GO practice reserves "protein secretion by the type II secretion system" for the secretion machinery; the secreted substrate does not carry out the process. Consider deleting the row, or recording the cargo relationship on the Xcp proteins (has_input) and keeping the extracellular region CC on PaAP.

## 160. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HZQ8 involved_in GO:0043952 protein transport by the Sec complex (IDA, PMID:9642203)
- **Field:** GO_ID
- **Change:** check GO:0043952 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/lap/lap-ai-review.yaml`

PA2939 (PaAP) is a Sec-exported cargo; it is not part of the Sec translocation machinery. The evidence visible to us (UniProt's N-terminal sequence from residue 25, credited to PMID:9642203) shows its signal peptide is removed, which is not participation in the transport process and does not by itself identify the Sec complex; the full text was not read. Consider deleting the row.

## 161. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:P14756 involved_in GO:0015628 protein secretion by the type II secretion system (IDA, PMID:9642203)
- **Field:** GO_ID
- **Change:** check GO:0015628 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/lasB/lasB-ai-review.yaml`

PA3724 (LasB) is a cargo of the Xcp type II secretion system, not a component of it. GO practice reserves "protein secretion by the type II secretion system" for the secretion machinery; the secreted substrate does not carry out the process. Consider deleting the row, or recording the cargo relationship on the Xcp proteins (has_input), and keeping the extracellular region CC on LasB. The identical row on PA2939 (PaAP), from the same reference, has the same problem.

## 162. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:P14756 involved_in GO:0043952 protein transport by the Sec complex (IDA, PMID:9642203)
- **Field:** GO_ID
- **Change:** check GO:0043952 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/lasB/lasB-ai-review.yaml`

PA3724 (LasB) is a Sec-exported cargo; it is not part of the Sec translocation machinery, and the evidence the abstract reports (removal of its signal peptide) is neither participation in the transport process nor by itself evidence that the translocon used is Sec rather than Tat; the full text was not read. Consider deleting the row. The identical row on PA2939 (PaAP) from the same reference has the same problem.

## 163. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:P33883 involved_in GO:0007165 signal transduction (IDA, PMID:8493556)
- **Field:** GO_ID
- **Change:** GO:0007165 → GO:0009372 (quorum sensing)
- **Recorded in:** `genes/PSEAE/lasI/lasI-ai-review.yaml`

involved_in GO:0007165 signal transduction (IDA, PMID:8493556) on PA1432 lasI. LasI is the autoinducer synthase: the paper shows lasI is needed to make the diffusible Pseudomonas autoinducer that LasR requires for elastase expression. GO:0007165 covers events at and within the receiving cell, starting with signal reception (LasR), so it does not apply to the synthase. Please re-term to GO:0009372 quorum sensing, whose definition includes producing the signal. The abstract describes gene-fusion and mutant evidence, so IMP may fit better than IDA, but we have read only the abstract and do not assert that. This row is the sole seed of the PANTHER IBD at PTN002217335.

> The lasl gene is involved in the synthesis of a diffusible molecule termed Pseudomonas autoinducer (PAI).
> — PMID:8493556

## 164. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I489 enables GO:0047580 4-hydroxyproline epimerase activity (IMP, PMID:27145750)
- **Change:** GO:0047580 → GO:0050346 (trans-L-3-hydroxyproline dehydratase activity)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/lhpL/lhpL-ai-review.yaml`

PseudoCAP annotates PA1255 (lhpL, UniProtKB:Q9I489) with GO:0047580 4-hydroxyproline epimerase activity, IMP, from PMID:27145750. Two problems. (1) The term's reaction is experimentally absent on this protein: Swiss-Prot records, with ECO:0000269|PubMed:17849014, that it displays neither t4LHyp epimerase nor proline racemase activity, and assigns it the trans-3-hydroxy-L-proline dehydratase (EC 4.2.1.77) and trans-3-hydroxy-L-proline 2-epimerase reactions (ECO:0000269|PubMed:27929065). GO:0050346 is the matching existing term. The organism's genuine 4-hydroxyproline 2-epimerase is PA1268 (UniProtKB:Q9I476), which PseudoCAP annotates with GO:0047580 from the same paper; that row looks correct. Point (1) is confirmed from the full text of PMID:17849014 (Table 1 lists Q9I489 as the Ser-Cys variant; Figure 1 shows no epimerase or racemase activity). (2) The evidence the abstract of PMID:27145750 reports is an induction phenotype of an lhpA lhpK double mutant, which cannot assign a molecular function to either single gene; we have not read the full text, so point (2) is a suggestion to check, not a finding. This row is the sole seed of the PAINT IBD at PTN002433936, from which 35 GOA rows now descend.

> Induction of the lhpA promoter by d-Hyp was completely abolished in the lhpA lhpK double mutant devoid of two epimerases, while the induction effect of l-Hyp remained unchanged
> — PMID:27145750

> P. aeruginosa (SC) and B. cenocepacia (CT) recombinant proteins whose sequences lack one of the two Cys catalytic residues do not display any PRAC or HyPRE activities.
> — PMID:17849014

## 165. WRONG_QUALIFIER (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I297 enables GO:0004485 methylcrotonoyl-CoA carboxylase activity (IDA, PMID:18469096)
- **Field:** Qualifier
- **Change:** enables → contributes_to
- **Likely cause:** SCOPE_OVER_REACH
- **Recorded in:** `genes/PSEAE/liuB/liuB-ai-review.yaml`

GO:0004485 methylcrotonoyl-CoA carboxylase activity on liuB (Q9I297) is coded enables, IDA, PMID:18469096. The activity belongs to the two-subunit enzyme, not to either chain: the full text of PMID:18469096, which is the IDA behind these rows, measured it on an enzyme reconstituted by mixing purified alpha and beta subunits and renaturing them, so no single subunit was shown active. The structure paper PMID:22158123 says why, for this organism's own enzyme: the alpha subunit carries the biotin carboxylase and BCCP domains and the beta subunit supplies the carboxyltransferase activity, with roughly 80 A between the two active sites, so the carboxyl group has to be handed between chains. Both rows on both subunits should read contributes_to. CONFIRMED rather than PROBABLE because the reconstitution is stated in the full text rather than inferred from an abstract.

> The α and β subunits (2 mg each) were mixed and renatured by dialysis
> — PMID:18469096

> BC catalyzes the MgATP-dependent carboxylation of biotin, and then a carboxyltransferase (CT) activity, supplied by the β subunit, catalyzes the transfer of the carboxyl group to the acceptor
> — PMID:22158123

## 166. WRONG_QUALIFIER (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I297 enables GO:0004485 methylcrotonoyl-CoA carboxylase activity (IMP, PMID:16517656)
- **Field:** Qualifier
- **Change:** enables → contributes_to
- **Likely cause:** SCOPE_OVER_REACH
- **Recorded in:** `genes/PSEAE/liuB/liuB-ai-review.yaml`

GO:0004485 methylcrotonoyl-CoA carboxylase activity on liuB (Q9I297) is coded enables, IMP, PMID:16517656. The activity belongs to the two-subunit enzyme, not to either chain: the full text of PMID:18469096, which is the IDA behind these rows, measured it on an enzyme reconstituted by mixing purified alpha and beta subunits and renaturing them, so no single subunit was shown active. The structure paper PMID:22158123 says why, for this organism's own enzyme: the alpha subunit carries the biotin carboxylase and BCCP domains and the beta subunit supplies the carboxyltransferase activity, with roughly 80 A between the two active sites, so the carboxyl group has to be handed between chains. Both rows on both subunits should read contributes_to. CONFIRMED rather than PROBABLE because the reconstitution is stated in the full text rather than inferred from an abstract.

> The α and β subunits (2 mg each) were mixed and renatured by dialysis
> — PMID:18469096

> BC catalyzes the MgATP-dependent carboxylation of biotin, and then a carboxyltransferase (CT) activity, supplied by the β subunit, catalyzes the transfer of the carboxyl group to the acceptor
> — PMID:22158123

## 167. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I298 involved_in GO:0046247 terpene catabolic process (IMP, PMID:16820476)
- **Change:** GO:0046247 → GO:0016100 (monoterpenoid catabolic process)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/liuC/liuC-ai-review.yaml`

GO:0046247 terpene catabolic process (defined for terpene hydrocarbons) for liuC (PA2013, Q9I298), IMP to PMID:16820476. The substrates of the P. aeruginosa Atu/Liu pathway are acyclic monoterpenoid alcohols and acids (citronellol, geraniol, citronellate), so GO:0016100 monoterpenoid catabolic process is the accurate term. This row is the sole seed of the PAINT IBD at PTN001733227, which should not propagate the terpenoid role to the hydratase clade.

> P. fluorescens, but not P. putida, could grow on acyclic terpenes (citronellol and citronellate)
> — PMID:16820476

## 168. WRONG_QUALIFIER (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I299 enables GO:0004485 methylcrotonoyl-CoA carboxylase activity (IDA, PMID:18469096)
- **Field:** Qualifier
- **Change:** enables → contributes_to
- **Likely cause:** SCOPE_OVER_REACH
- **Recorded in:** `genes/PSEAE/liuD/liuD-ai-review.yaml`

GO:0004485 methylcrotonoyl-CoA carboxylase activity on liuD (Q9I299) is coded enables, IDA, PMID:18469096. The activity belongs to the two-subunit enzyme: the IDA behind these rows measured it on an enzyme reconstituted by mixing purified alpha and beta subunits, so no single chain was shown active, and the structure of this organism's enzyme places the biotin carboxylase site on the alpha subunit roughly 80 A from the carboxyltransferase site supplied by beta. LiuD performs only the first half-reaction, which it already has as GO:0004075 biotin carboxylase activity. The same correction is requested for the liuB rows. CONFIRMED on the strength of the full text rather than an abstract.

> The α and β subunits (2 mg each) were mixed and renatured by dialysis
> — PMID:18469096

> BC catalyzes the MgATP-dependent carboxylation of biotin, and then a carboxyltransferase (CT) activity, supplied by the β subunit, catalyzes the transfer of the carboxyl group to the acceptor
> — PMID:22158123

## 169. WRONG_QUALIFIER (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I299 enables GO:0004485 methylcrotonoyl-CoA carboxylase activity (IMP, PMID:16517656)
- **Field:** Qualifier
- **Change:** enables → contributes_to
- **Likely cause:** SCOPE_OVER_REACH
- **Recorded in:** `genes/PSEAE/liuD/liuD-ai-review.yaml`

GO:0004485 methylcrotonoyl-CoA carboxylase activity on liuD (Q9I299) is coded enables, IMP, PMID:16517656. The activity belongs to the two-subunit enzyme: the IDA behind these rows measured it on an enzyme reconstituted by mixing purified alpha and beta subunits, so no single chain was shown active, and the structure of this organism's enzyme places the biotin carboxylase site on the alpha subunit roughly 80 A from the carboxyltransferase site supplied by beta. LiuD performs only the first half-reaction, which it already has as GO:0004075 biotin carboxylase activity. The same correction is requested for the liuB rows. CONFIRMED on the strength of the full text rather than an abstract.

> The α and β subunits (2 mg each) were mixed and renatured by dialysis
> — PMID:18469096

> BC catalyzes the MgATP-dependent carboxylation of biotin, and then a carboxyltransferase (CT) activity, supplied by the β subunit, catalyzes the transfer of the carboxyl group to the acceptor
> — PMID:22158123

## 170. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I2A0 enables GO:0004419 hydroxymethylglutaryl-CoA lyase activity (IMP, PMID:16517656)
- **Field:** Evidence_Code
- **Change:** check ECO:0000315 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/liuE/liuE-ai-review.yaml`

The GO:0004419 row on PA2011 is coded IMP from PMID:16517656, but that paper's abstract describes the assignment as a "probable hydroxy-acyl-CoA lyase (probably HMG-CoA lyase)" inferred from sequence, with cluster mutagenesis and growth phenotypes as the experimental content - not an enzyme assay. The activity was later measured on purified protein (PMID:19459965, kinetics; PMID:19597963, both activities), and UniProt already carries EXP rows from those papers. Requested change - re-point this row to PMID:19459965/PMID:19597963, or recode it as an inference, so that the IMP coding of a molecular function on a sequence-based prediction does not stand as a PAINT seed. Filed as PROBABLE because the abstract positively states the "probable" basis while the full text was not read.

> The liuE gene encodes a probable hydroxy-acyl-CoA lyase (probably HMG-CoA lyase), an enzyme with bifunctional activity that is essential for both AMTC and leucine degradation.
> — PMID:16517656

## 171. WRONG_REFERENCE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9X6P4 involved_in GO:0009103 lipopolysaccharide biosynthetic process (IDA, PMID:1904818)
- **Field:** DB:Reference
- **Change:** PMID:1904818 → PMID:9440522 (Dotson et al. 1998, Expression cloning of a Pseudomonas gene encoding a hydroxydecanoyl-acyl carrier protein-dependent UDP-GlcNAc acyltransferase)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/lpxA/lpxA-ai-review.yaml`

involved_in GO:0009103 lipopolysaccharide biosynthetic process (IDA) on PA3644 cites Kulshin et al. 1991 (PMID:1904818), a chemical, GC-MS and NMR structural characterisation of lipid A purified from P. aeruginosa strains. Its abstract names only chemical, GC-MS, mass spectrometric and NMR methods on purified lipopolysaccharide, and mentions no enzyme assay and no lpxA; the paper also predates the cloning of the gene (1998). We have read only the abstract, so an enzyme measurement in the full text cannot be excluded, but the paper is unlikely to be direct evidence for this gene product. The intended reference is probably Dotson et al. 1998 (PMID:9440522), which cloned PAO1 lpxA, assayed the enzyme as a 10-carbon-specific UDP-GlcNAc acyltransferase and complemented an E. coli lpxA mutant; it is reference [1] of UniProtKB:Q9X6P4. Please repoint the reference. Note that this row is the only seed of the PANTHER IBD for GO:0009103 at PTN000602377, which propagates to 24 LpxA-family leaves.

> was investigated using chemical analysis, methylation analysis
> — PMID:1904818

> we here report the isolation of the lpxA gene of Pseudomonas aeruginosa
> — PMID:9440522

## 172. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:P52477 involved_in GO:0046677 response to antibiotic (IDA, PMID:8540696)
- **Field:** Evidence_Code
- **Change:** IDA → IMP
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/mexA/mexA-ai-review.yaml`

PseudoCAP row for PA0425/mexA (P52477), GO:0046677 response to antibiotic, IDA, PMID:8540696 (Li, Nikaido and Poole 1995). The abstract reports drug accumulation and susceptibility in mexA and oprM null mutants and in a MexAB-OprM-overproducing mutant: mutant phenotypes, so IMP. The term is correct. Abstract-only reading; the full text could contain a direct assay the abstract does not mention.

> Thus, the steady-state accumulation levels of tetracycline and norfloxacin were increased in mexA and oprM null mutants.
> — PMID:8540696

## 173. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I0Z0 involved_in GO:0045861 negative regulation of proteolysis (IMP, PMID:21075931)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0045861
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/mexT/mexT-ai-review.yaml`

GO:0045861 negative regulation of proteolysis is annotated by IMP to the LysR regulator MexT (PA2492, Q9I0Z0) from PMID:21075931 (Jin et al. 2011). The full text shows only that mexT and mexS mutants of PAO1 produce more elastase; the mechanism is not via MexS and is not identified. A regulator that lowers protease production does not regulate proteolysis. Please delete the row.

> the mexS and mexT mutants of PAO1 shared the same phenotype of increased elastase and pyocyanin production compared to that in wild-type PAO1
> — PMID:21075931

## 174. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:G3XCU9 involved_in GO:0032410 negative regulation of transporter activity (IMP, PMID:15105120)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0032410
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/mexZ/mexZ-ai-review.yaml`

PseudoCAP IMP row for PA2020/mexZ, GO:0032410 negative regulation of transporter activity, from PMID:15105120 (Vogne et al. 2004). The abstract describes mexZ as the repressor gene of the mexXY operon, with MexY overproduced in mexZ mutants and MICs reduced by mexZ complementation. That is regulation of transporter gene expression, not of transporter activity. Requested change: delete the row; the transcriptional role is already annotated (GO:0045892), and the transport consequence fits GO:1905700. Abstract-only reading; the full text could in principle report a post-translational effect.

> Alterations in mexZ, the repressor gene of operon mexXY, were found in all of the AG-resistant CF isolates
> — PMID:15105120

## 175. WRONG_EVIDENCE_CODE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I544 enables GO:0000287 magnesium ion binding (IMP, PMID:24722909)
- **Field:** Evidence_Code
- **Change:** check ECO:0000315 (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/PSEAE/mgtE/mgtE-ai-review.yaml`

enables GO:0000287 magnesium ion binding (IMP) on PA0913 mgtE cites Coffey et al. 2014 (PMID:24722909). As the abstract presents it, the Mg2+-binding sites were predicted from a homology model based on T. thermophilus MgtE, and their mutation disrupted coupling of transport and cytotoxicity regulation. A loss-of-function phenotype does not show that the residues bind Mg2+. Unless the full text reports a direct binding assay, the annotation is better made as ISS with UniProtKB:Q5SMG8 (Mg2+-bound crystal structures, PMID:17700703). This row is the sole seed of the PAINT IBD at PTN000227060.

> showed that magnesium-binding sites in the connecting helix region of MgtE are vital in coupling these two functions
> — PMID:24722909

## 176. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I5M1 involved_in GO:0015920 lipopolysaccharide transport (IDA, PMID:19589832)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0015920
- **Recorded in:** `genes/PSEAE/migA/migA-ai-review.yaml`

involved_in GO:0015920 lipopolysaccharide transport (IDA, PMID:19589832) is not what the paper studied: its abstract describes swimming and swarming motility, attachment to glass and flagellin glycosylation in mutants with truncated core oligosaccharide, and nothing on LPS export. The glycosyltransferase builds the core in the cytoplasm before LPS export. Please delete the row. PROBABLE because only the abstract was read.

> P. aeruginosa wild-type strain PAO1 and three isogenic mutants with defects in the rmlC, migA and wapR genes and producing truncated core oligosaccharide were investigated in terms of motility, attachment to glass and flagella expression.
> — PMID:19589832

> LPS truncations probably alter flagella-mediated motility in P. aeruginosa by modulating cell-surface attachment but not flagella synthesis
> — PMID:19589832

## 177. WRONG_EVIDENCE_CODE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HUL1 involved_in GO:0071978 bacterial-type flagellum-dependent swarming motility (IMP, PMID:15629949)
- **Field:** Evidence_Code
- **Change:** check ECO:0000315 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/motA/motA-ai-review.yaml`

involved_in GO:0071978 (IMP) on motA (PA4954) cites Toutain et al. 2005, in which the motAB deletion swarms as well as wild type; a swarming defect is seen only when motCD (PA1460-PA1461) is also deleted. The support for MotAB in swarming is a genetic interaction (IGI with motCD), not a motA mutant phenotype. This row is one of the two seeds of the PTN001252377 swarming IBD (with motC, PA1460).

> The Δ motAB mutant is able to swarm as well as the WT in agar concentrations up to 0.7%.
> — PMID:15629949

## 178. WRONG_TERM (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HUL1 involved_in GO:0071978 bacterial-type flagellum-dependent swarming motility (IMP, PMID:25349157)
- **Field:** GO_ID
- **Change:** check GO:0071978 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/motA/motA-ai-review.yaml`

involved_in GO:0071978 (IMP) on motA (PA4954) cites Kuchma et al. 2015, whose abstract reports that motAB mutation stimulates swarming and restores swarming at high c-di-GMP, and that MotA overexpression represses swarming. An increased-swarming phenotype does not support a positive involved_in by IMP; the finding is that MotAB is needed for c-di-GMP-mediated repression of swarming. Please check whether the row should be dropped or recast. This row is a seed of the PTN001252377 swarming IBD; the same issue was recorded for motB (PA4953).

> Mutating the motAB genes restores swarming motility to a strain with artificially elevated levels of c-di-GMP as well as stimulates swarming in the wild-type strain, while overexpression of MotA from a plasmid represses swarming motility.
> — PMID:25349157

## 179. WRONG_EVIDENCE_CODE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HUL2 involved_in GO:0071978 bacterial-type flagellum-dependent swarming motility (IMP, PMID:15629949)
- **Field:** Evidence_Code
- **Change:** check ECO:0000315 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/motB/motB-ai-review.yaml`

involved_in GO:0071978 (IMP) on motB (PA4953) cites Toutain et al. 2005, in which the motAB deletion swarms as well as wild type; a swarming defect is seen only when motCD is also deleted. The support for MotAB in swarming is a genetic interaction (IGI with motCD, PA1460-PA1461), not a motB mutant phenotype. This row is one of the seeds of the PTN001251133 swarming IBD.

> The Δ motAB mutant is able to swarm as well as the WT in agar concentrations up to 0.7%.
> — PMID:15629949

## 180. WRONG_TERM (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HUL2 involved_in GO:0071978 bacterial-type flagellum-dependent swarming motility (IMP, PMID:25349157)
- **Field:** GO_ID
- **Change:** check GO:0071978 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/motB/motB-ai-review.yaml`

involved_in GO:0071978 (IMP) on motB (PA4953) cites Kuchma et al. 2015, whose abstract reports that motAB mutation stimulates swarming and restores swarming at high c-di-GMP. An increased-swarming phenotype does not support a positive involved_in by IMP; the finding is that MotAB is needed for c-di-GMP-mediated repression of swarming. Please check whether the row should be dropped or recast. This row is a seed of the PTN001251133 swarming IBD.

> Mutating the motAB genes restores swarming motility to a strain with artificially elevated levels of c-di-GMP as well as stimulates swarming in the wild-type strain
> — PMID:25349157

## 181. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:G3XD20 involved_in GO:0007165 signal transduction (IDA, PMID:21036998)
- **Change:** GO:0007165 → GO:0009968 (negative regulation of signal transduction)
- **Recorded in:** `genes/PSEAE/mucD/mucD-ai-review.yaml`

GO:0007165 signal transduction IDA for MucD (PA0766, G3XD20) from PMID:21036998. The paper shows that mucD inactivation activates MucP-dependent MucA degradation and AlgU activity, so MucD negatively regulates the RIP signalling cascade rather than taking part in it. The experiments are mutant phenotypes, so the evidence code should be IMP. Suggest GO:0009968 negative regulation of signal transduction, IMP.

> When mucD is inactivated, a high level of algU promoter activity was noted (Fig. 3A ), suggesting that the RIP activities are negatively regulated by MucD.
> — PMID:21036998

## 182. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HXS0 involved_in GO:0032410 negative regulation of transporter activity (IMP, PMID:15387820)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0032410
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/nalC/nalC-ai-review.yaml`

PseudoCAP IMP row for PA3721/nalC, GO:0032410 negative regulation of transporter activity, from PMID:15387820 (Cao et al. 2004). GO:0032410 is a process that reduces the activity of a transporter. The abstract states that NalC acts only by repressing PA3720-PA3719, whose product PA3719 raises MexAB-OprM expression. That is regulation of gene expression, not of transporter activity. Requested change: delete the row; the transcriptional role is already annotated (GO:0045892). Abstract-only reading; the full text could in principle report a post-translational effect, which would be unprecedented for a TetR repressor.

> Thus, the nalC (PA3721) mutation serves only to enhance PA3720-PA3719 expression
> — PMID:15387820

## 183. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HY46 involved_in GO:0032410 negative regulation of transporter activity (IMP, PMID:17028276)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0032410
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/nalD/nalD-ai-review.yaml`

PseudoCAP IMP row for PA3574/nalD, GO:0032410 negative regulation of transporter activity, from PMID:17028276 (Morita et al. 2006). GO:0032410 is a process that reduces the activity of a transporter. The abstract states that NalD binds an operator overlapping a mexAB-oprM promoter and that expression from that promoter rises in a nalD mutant. That is regulation of gene expression, not of transporter activity. Requested change: delete the row; the transcriptional role is already annotated (GO:0045892). Abstract-only reading; the full text could in principle report a post-translational effect, which would be unprecedented for a TetR repressor.

> increased expression from this promoter was seen in a nalD mutant, consistent with NalD directly controlling mexAB-oprM expression from a second promoter
> — PMID:17028276

## 184. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q59636 involved_in GO:0042121 alginic acid biosynthetic process (IDA, PMID:8809750)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0042121
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/ndk/ndk-ai-review.yaml`

PseudoCAP row for PA3807/ndk (Q59636), GO:0042121 alginic acid biosynthetic process, IDA, PMID:8809750 (Sundin et al. 1996). The abstract's alginate evidence is that ndk hyperexpression restored alginate to about 60% of wild type in an algR2 regulatory mutant, which the authors attribute to GTP supply for GDP-mannose. Ndk catalyses no step of alginate synthesis, and a rescue phenotype is not an IDA. Please delete the row (at most an IGI acts_upstream_of_or_within). PROBABLE because only the abstract was read.

> Hyperexpression of ndk from pGWS95 in the P. aeruginosa algR2 mutant also restored alginate production to levels that were approximately 60% of wild type.
> — PMID:8809750

## 185. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:P32265 involved_in GO:0032410 negative regulation of transporter activity (IMP, PMID:20373734)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0032410
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/nfxB/nfxB-ai-review.yaml`

PseudoCAP IMP row for PA4600/nfxB, GO:0032410 negative regulation of transporter activity, from PMID:20373734 (Stickland et al. 2010). GO:0032410 is a process that reduces the activity of a transporter. The abstract attributes the nfxB mutant phenotypes to inappropriate overexpression of the MexCD-OprJ pump. That is regulation of gene expression, not of transporter activity. Requested change: delete the row; the transcriptional role is already annotated (GO:0045892). Abstract-only reading; the full text could in principle report a post-translational effect, which would be unprecedented for a TetR repressor.

> suggesting that inappropriate overexpression of a functional MexCD-OprJ efflux pump causes pleiotropic changes
> — PMID:20373734

## 186. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:P32265 involved_in GO:0032410 negative regulation of transporter activity (IMP, PMID:8878035)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0032410
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/nfxB/nfxB-ai-review.yaml`

PseudoCAP IMP row for PA4600/nfxB, GO:0032410 negative regulation of transporter activity, from PMID:8878035 (Poole et al. 1996). GO:0032410 is a process that reduces the activity of a transporter. The abstract shows that NfxB represses a mexC-lacZ fusion and that nfxB mutants overproduce OprJ. That is regulation of gene expression, not of transporter activity. Requested change: delete the row; the transcriptional role is already annotated (GO:0045892). Abstract-only reading; the full text could in principle report a post-translational effect, which would be unprecedented for a TetR repressor.

> the cloned nfxB gene repressed synthesis of a mexC-lacZ fusion in Escherichia coli
> — PMID:8878035

## 187. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HT74 involved_in GO:1900376 regulation of secondary metabolite biosynthetic process (IMP, PMID:12426334)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:1900376
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/np20/np20-ai-review.yaml`

PseudoCAP IMP row for PA5499/np20 (Q9HT74), GO:1900376 regulation of secondary metabolite biosynthetic process, from PMID:12426334 (Gallagher et al. 2002). The full text reports an np20 transposon mutant from a pyocyanin-deficiency screen with reduced transcription of several quorum-sensing-controlled genes; it does not test whether Np20 acts on phenazine or other secondary-metabolite genes. Np20 was later shown to be Zur, a zinc-responsive repressor of the znuABC zinc uptake genes (PMID:24086521). The row records an indirect, pleiotropic phenotype. Requested change: delete the row. This row also seeds the PTN002112386 GO:1900376 IBD. PROBABLE because the indirectness is an inference from the absence of a mechanism and from the protein's known function.

> Third, mutations in the putative regulators np20 and PA3946 reduced transcription of a number of quorum sensing-controlled genes, showing that these functions participate in the quorum-sensing regulatory network.
> — PMID:12426334

## 188. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HT76 enables GO:0004748 ribonucleoside-diphosphate reductase activity, thioredoxin disulfide as acceptor (IDA, PMID:15722359)
- **Field:** GO_Term
- **Change:** check GO:0004748 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/nrdJa/nrdJa-ai-review.yaml`

enables GO:0004748 (ribonucleoside-diphosphate reductase activity, thioredoxin disulfide as acceptor; IDA, PMID:15722359) on PA5497 (nrdJa) fixes the substrate as a ribonucleoside diphosphate. The later biochemical study of the same enzyme with purified subunits (PMID:26225432) found that ribonucleoside triphosphates are preferred by more than 60-fold over CDP, so GO:0008998 ribonucleoside-triphosphate reductase (thioredoxin) activity describes the principal reaction; CDP reduction is measurable but minor. The same applies to the companion annotation on PA5496 (nrdJb) if one exists. Please consider adding GO:0008998 (and keeping GO:0004748 for the minor reaction). Note also that the purified-enzyme assays used DTT or TCEP, not thioredoxin (we read only the abstract of PMID:15722359, so its reductant is unchecked), so the acceptor clause of either term looks like an inference from class I/II RNR precedent rather than a measurement in P. aeruginosa. This row is the sole seed of the PAINT IBD at PTN000171476, which propagates the diphosphate term to 39 leaves.

> For NrdJa-NrdJb from PA we found that NTP was the favored substrate.
> — PMID:26225432

> The results revealed that CTP is the preferred substrate with a >60-fold higher activity compared to CDP
> — PMID:26225432

## 189. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I6Y9 involved_in GO:0006163 purine nucleotide metabolic process (IMP, PMID:15995202)
- **Field:** GO_ID
- **Change:** GO:0006163 → GO:0006152 (purine nucleoside catabolic process)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/nuh/nuh-ai-review.yaml`

PseudoCAP IMP row for PA0143/nuh, GO:0006163 purine nucleotide metabolic process, from the Nuh(-) adenosine growth phenotype in PMID:15995202. Nuh is a nucleoside hydrolase acting on adenosine, a purine nucleoSIDE, cleaving it to adenine and ribose; it does not metabolize nucleoTIDES. The correct process is GO:0006152 purine nucleoside catabolic process, which the gene already carries by IBA. Abstract read; full text (PMC1169536) not retrievable, but the error is in the term choice versus the stated substrate, not in the biology.

> lasR mutants did not grow on adenosine as the sole carbon source because a key degradative enzyme, nucleoside hydrolase (Nuh), is positively controlled by LasR
> — PMID:15995202

## 190. WRONG_REFERENCE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HVS0 enables GO:0015288 porin activity (IDA, PMID:25338022)
- **Field:** Reference
- **Change:** PMID:25338022 → PMID:22272184
- **Recorded in:** `genes/PSEAE/opdP/opdP-ai-review.yaml`

Full text read: Pletzer et al. 2014 study the DppBCDF dipeptide ABC transporter and DppA1-A5 in PA14 and mention OpdP only as co-transcribed with dppA4, citing earlier work for its transport role. No OpdP assay is reported, so the IDA has no support in this paper. Eren et al. 2012 (PMID:22272184) provide direct OccD3 single-channel and arginine-uptake data and are a suitable IDA reference. The IBD on PTN002160747 is not affected: it stands on OprD.

> co-transcribed in an operon with PA14_58410 encoding the porin OpdP
> — PMID:25338022

> The porin OpdP was previously shown to be involved in the transport of dipeptides as well as of single amino acids in PAO1 [24].
> — PMID:25338022

> The efficient arginine uptake mediated by OccD3 is noteworthy since this protein was shown, like OccD1, to mediate arginine uptake in P. aeruginosa in vivo
> — PMID:22272184

## 191. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I189 involved_in GO:0002049 pyoverdine biosynthetic process (IMP, PMID:12686626)
- **Field:** GO_ID
- **Change:** GO:0002049 → GO:0015891 (siderophore transport)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/opmQ/opmQ-ai-review.yaml`

opmQ is a component of the PvdRT-OpmQ efflux pump, which exports pyoverdine from the periplasm to the medium. The IMP row from PMID:12686626 (Lamont and Martin 2003) records lower pyoverdine yield in a mutant as involvement in pyoverdine biosynthesis. A transporter mutant makes less extracellular pyoverdine because export and recycling fail, which also lowers synthesis indirectly (Imperi et al. 2009, PMID:19906986). The pump does none of the chemistry of synthesis. Requested change: re-point to GO:0015891 siderophore transport (or delete). PROBABLE because the 2003 paper was read as an abstract only.

> our preliminary results suggest that the lower PVD levels in their culture supernatants are a result of reduced PVD synthesis rather than of impaired secretion of de novo synthesized PVD
> — PMID:19906986

> Bacteria lacking this efflux pump accumulated PVD, or a fluorescent precursor, in the periplasm, due to their inability to efficiently secrete into the media newly synthesized PVD.
> — PMID:21035449

## 192. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I189 enables GO:0015562 efflux transmembrane transporter activity (IDA, PMID:19906986)
- **Field:** Evidence_Code
- **Change:** IDA → IMP
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/opmQ/opmQ-ai-review.yaml`

The IDA row for opmQ (GO:0015562 efflux transmembrane transporter activity) cites PMID:19906986 (Imperi et al. 2009). Full text read: every result for PvdR, PvdT and OpmQ is a mutant phenotype (PVD levels in supernatants, periplasmic fractions and confocal images of transposon or deletion mutants, with complementation). The paper does not assay the purified protein or the assembled complex. The same paper already supports the parallel IMP row, so the IDA row should be recoded as IMP or deleted. PROBABLE rather than CONFIRMED because the supplementary material was not read.

> Conversely, PA2389 , PA2390 , and opmQ mutants accumulated five- to sixfold higher amounts of PVD than wild-type PAO1, suggesting an involvement of these genes in PVD export.
> — PMID:19906986

## 193. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I189 part_of GO:1990281 efflux pump complex (IDA, PMID:19906986)
- **Field:** Evidence_Code
- **Change:** IDA → IMP
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/opmQ/opmQ-ai-review.yaml`

The IDA row for opmQ (GO:1990281 efflux pump complex) cites PMID:19906986 (Imperi et al. 2009). Full text read: every result for PvdR, PvdT and OpmQ is a mutant phenotype (PVD levels in supernatants, periplasmic fractions and confocal images of transposon or deletion mutants, with complementation). The paper does not assay the purified protein or the assembled complex. The same paper already supports the parallel IMP row, so the IDA row should be recoded as IMP or deleted. PROBABLE rather than CONFIRMED because the supplementary material was not read.

> Conversely, PA2389 , PA2390 , and opmQ mutants accumulated five- to sixfold higher amounts of PVD than wild-type PAO1, suggesting an involvement of these genes in PVD export.
> — PMID:19906986

## 194. WRONG_EVIDENCE_CODE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q51485 involved_in GO:0008643 carbohydrate transport (IDA, PMID:7768797)
- **Field:** Evidence_Code
- **Change:** ECO:0000314 → ECO:0000315
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/oprB/oprB-ai-review.yaml`

GO:0008643 carbohydrate transport for OprB (PA3186, Q51485) is annotated IDA to PMID:7768797. The full text (read 2026-11-05) measures initial sugar uptake by whole cells of an interposon oprB mutant, complemented and OprB overexpressing strains, and wild type, with arginine uptake as a control; it contains no assay with purified OprB. A mutant and overexpression phenotype is IMP in GO, so please change the evidence code to IMP. The claim is sound, and the specific substrates (glucose, mannitol, fructose, glycerol) could be annotated with the substrate-specific transmembrane transport terms. This row is the sole seed of the PAINT IBD at PTN002209977.

> Using interposon mutagenesis, we have generated strains of Pseudomonas aeruginosa which lack or overexpress the substrate-selective OprB porin of this species.
> — PMID:7768797

## 195. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:P32722 enables GO:0015288 porin activity (IMP, PMID:2120174)
- **Field:** Evidence
- **Change:** check IMP GO:0015288 PMID:2120174 (oprD) (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/oprD/oprD-ai-review.yaml`

The cited abstract reports transductants that lost four outer membrane proteins (C, D2, E1, E2) together and concludes that at least one of them is a porin, so the mutant phenotype cannot be attributed to this protein alone. The same paper supports identical PseudoCAP IMP rows on oprD and oprE. The porin activity itself is correct, supported by PMID:2118530 and PMID:22272184; the IMP row should be re-referenced or dropped. Full text not read, hence PROBABLE.

> decreased amounts of outer membrane proteins C, D2, E1, and E2 lowered the
> — PMID:2120174

> The results suggested that at least one of the four proteins was
> — PMID:2120174

## 196. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:G3XDA5 enables GO:0015288 porin activity (IMP, PMID:2120174)
- **Field:** Evidence
- **Change:** check IMP GO:0015288 PMID:2120174 (oprE) (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/oprE/oprE-ai-review.yaml`

The cited abstract reports transductants that lost four outer membrane proteins (C, D2, E1, E2) together and concludes that at least one of them is a porin, so the mutant phenotype cannot be attributed to this protein alone. The same paper supports identical PseudoCAP IMP rows on oprD and oprE. The porin activity itself is correct, supported by PMID:33481046; the IMP row should be re-referenced or dropped. Full text not read, hence PROBABLE.

> decreased amounts of outer membrane proteins C, D2, E1, and E2 lowered the
> — PMID:2120174

> The results suggested that at least one of the four proteins was
> — PMID:2120174

## 197. WRONG_EVIDENCE_CODE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I2U3 enables GO:0000156 phosphorelay response regulator activity (IMP, PMID:20547815)
- **Field:** Evidence_Code
- **Change:** check ECO:0000315 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/parR/parR-ai-review.yaml`

The GO:0000156 row on PA1799 is coded IMP from PMID:20547815, but the evidence in the cited abstract is a mutant phenotype of the ParR-ParS system (loss of peptide-induced arnBCADTEF expression and of adaptive polymyxin resistance), not an assay of ParR as a phosphoryl-group acceptor. Since this row seeds the PAINT IBD on PTN000724188, the coding matters beyond this gene. Requested change - confirm whether the full text contains a phosphotransfer or phospho-ParR experiment; if not, consider recoding as an inference from the receiver-domain architecture while keeping the term. Filed as SUSPECTED because the full text of PMID:20547815 was not available and could report such an experiment.

> This system was required for activation of the arnBCADTEF LPS modification operon in the presence of subinhibitory concentrations of polymyxin, colistin, or the bovine peptide indolicidin, leading to increased resistance to various polycationic antibiotics, including aminoglycosides.
> — PMID:20547815

## 198. WRONG_EVIDENCE_CODE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I2U4 enables GO:0000155 phosphorelay sensor kinase activity (IMP, PMID:20547815)
- **Field:** Evidence_Code
- **Change:** check ECO:0000315 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/parS/parS-ai-review.yaml`

The GO:0000155 row on PA1798 is coded IMP from PMID:20547815, but the evidence in the cited abstract is a mutant phenotype of the ParR-ParS system (loss of peptide-induced arnBCADTEF expression and of adaptive polymyxin resistance), not an assay of ParS kinase or phosphotransfer activity. The row is one of three seeds of the PAINT IBD on PTN001293174 (the other two, EnvZ and PA5484, are IDA, so the node is unaffected). Requested change - confirm whether the full text contains an autophosphorylation or phosphotransfer experiment; if not, consider recoding as an inference from the HisKA/HATPase architecture while keeping the term. SUSPECTED because the full text was not read.

> Here we describe the identification and characterization of a novel P. aeruginosa two-component regulator affecting polymyxin-adaptive resistance, ParR-ParS (PA1799-PA1798).
> — PMID:20547815

## 199. WRONG_EVIDENCE_CODE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q04804 involved_in GO:0000160 phosphorelay signal transduction system (IDA, PMID:8808923)
- **Field:** Evidence_Code
- **Change:** check ECO:0000314 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/pfeS/pfeS-ai-review.yaml`

PseudoCAP IDA row for PA2687/pfeS, GO:0000160 phosphorelay signal transduction system, from PMID:8808923 (Dean, Neshat and Poole 1996). The abstract reports direct assays only on PfeR (bandshift with the pfeA promoter) and genetic data on pfeR and pfeA; it states that PfeS is required but describes no PfeS assay. If the PfeS evidence in the paper is genetic, the code should be IMP (or the row should cite the paper that made the pfeS mutant). SUSPECTED: the full text (scanned PDF only) was not read and may contain a PfeS experiment.

> PfeR (Regulator) and PfeS (Sensor), members of the superfamily of so-called two-component regulatory protein pairs, are required for the enterobactin-inducible production of the ferric enterobactin receptor (PfeA) in Pseudomonas aeruginosa.
> — PMID:8808923

> PfeR overexpressed in P. aeruginosa bound, in bandshift assays, the promoter region of pfeA
> — PMID:8808923

## 200. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:P09786 involved_in GO:0002047 phenazine biosynthetic process (IMP, PMID:2153661)
- **Change:** check GO:0002047 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/phnB/phnB-ai-review.yaml`

PseudoCAP annotates phnB (PA1002, UniProtKB:P09786) and phnA (P09785) with GO:0002047 phenazine biosynthetic process, IMP, from PMID:2153661, on the basis of reduced pyocyanin in phn mutants. Work since then shows the route is indirect: PhnAB supplies anthranilate for the quinolone signal PQS, and PQS induces the phenazine operons (PMID:23449919), whereas the phenazine core is made from chorismate by PhzE via 2-amino-2-deoxyisochorismate with no anthranilate intermediate (PMID:21454481). UniProt's current FUNCTION line already states this. Our recommendation is to retire the phenazine process term for phnA and phnB in favour of the anthranilate synthase activity they are also annotated with, plus a quinolone-signal biosynthetic process term if one is created; if PseudoCAP prefers to keep a downstream link, a regulatory term such as GO:1900982 positive regulation of phenazine biosynthetic process would describe the observation more accurately. The row is the sole seed of the PAINT IBD at PTN000230115, from which 267 GOA rows now descend onto TrpG proteins of non-phenazine-producing organisms.

> At the time it was believed that PhnAB generated anthranilate for pyocyanin production, but later work determined that anthranilate is instead a precursor for PQS production, which is required to induce genes for pyocyanin biosynthesis
> — PMID:23449919

## 201. WRONG_QUALIFIER (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:P09786 enables GO:0004049 anthranilate synthase activity (IMP, PMID:2153661)
- **Field:** Qualifier
- **Change:** check enables (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/phnB/phnB-ai-review.yaml`

The anthranilate synthase reaction (chorismate + L-glutamine -> anthranilate + pyruvate + L-glutamate) is carried out by the PhnA-PhnB heterotetramer: PhnB is the glutamine amidotransferase subunit that generates ammonia, and PhnA condenses it with chorismate. The complementation evidence is for the gene pair, not for phnB alone, so contributes_to GO:0004049 would describe the subunit's role more accurately than enables. The same applies to the companion row on phnA (P09785), which enables the chorismate-utilizing half.

> Heterotetramer consisting of two non-identical subunits: a
> — file:PSEAE/phnB/phnB-uniprot.txt

## 202. WRONG_REFERENCE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HWG9 enables GO:0004497 monooxygenase activity (IDA, PMID:17012792)
- **Field:** DB:Reference
- **Change:** PMID:17012792 → PMID:17253782 (Parsons et al. 2007, Structural and functional analysis of the pyocyanin biosynthetic protein PhzM from Pseudomonas aeruginosa)
- **Recorded in:** `genes/PSEAE/phzS/phzS-ai-review.yaml`

enables GO:0004497 monooxygenase activity (IDA) on PA4217 phzS cites PMID:17012792 (Gohain et al. 2006), a crystallization and preliminary X-ray communication that reports cloning, purification, crystallization and data collection only and contains no enzyme assay. The activity was shown with purified PhzS in PMID:17253782 (NADH-dependent conversion of PCA to 1-hydroxyphenazine, and pyocyanin formation with PhzM). Please re-key the row to PMID:17253782, or consider the more specific GO:0102169. This row is the sole seed of the PAINT IBD at PTN002492679; the IBD itself remains sound.

> Here, we report the large-scale expression of recombinant PhzS and the first diffraction data collected from native and seleno- l -methionine-labelled protein crystals as an initial step towards understanding the reaction mediated by PhzS and its substrate specificity.
> — PMID:17012792

> This was confirmed by incubating PhzS with PCA and NADH. 1-HP was formed in an NADH dependant manner
> — PMID:17253782

## 203. WRONG_EVIDENCE_CODE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:P04739 involved_in GO:0043107 type IV pilus-dependent motility (IDA, PMID:12933890)
- **Field:** Evidence_Code
- **Change:** ECO:0000314 → ECO:0000315 (IMP)
- **Recorded in:** `genes/PSEAE/pilA/pilA-ai-review.yaml`

involved_in GO:0043107 (IDA, PMID:12933890) on PA4525 pilA: the paper examines twitching colony morphology of a pilA mutant of strain PAK, which is a mutant phenotype (IMP), not a direct assay. Checked in the cached full text, where colony morphology of the mutants is the only twitching assay. The term is correct.

> we examined their twitching motility qualitatively by examination of colony morphology
> — PMID:12933890

## 204. WRONG_REFERENCE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:P22608 involved_in GO:0043107 type IV pilus-dependent motility (IDA, PMID:1671384)
- **Field:** DB:Reference
- **Change:** check PMID:1671384 (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/PSEAE/pilB/pilB-ai-review.yaml`

involved_in GO:0043107 type IV pilus-dependent motility (IDA) on PA4526 pilB cites Strom et al. 1991 (PMID:1671384), a pilD paper whose abstract mentions pilB only as necessary for pilus biogenesis, citing Nunn, Bergman and Lory 1990 (PMID:1971619), and does not report a motility assay. If the full text has no pilB motility data, the row would be better keyed to a paper that tests pilB twitching (e.g. PMID:18174131 or PMID:25049409) with IMP rather than IDA. Please check.

> The function of the other two accessory proteins, PilB and PilC, appears to be restricted to pilus biogenesis, and strains carrying mutations in their respective genes do not show an export defect.
> — PMID:1671384

## 205. WRONG_EVIDENCE_CODE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:P22608 involved_in GO:0043683 type IV pilus assembly (IDA, PMID:1671384)
- **Field:** Evidence_Code
- **Change:** check ECO:0000314 (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/PSEAE/pilB/pilB-ai-review.yaml`

involved_in GO:0043683 type IV pilus assembly (IDA) on PA4526 pilB cites Strom et al. 1991 (PMID:1671384), a pilD paper whose abstract restates, from Nunn, Bergman and Lory 1990 (PMID:1971619), that pilB is required for assembly of pili. The underlying evidence is a mutant phenotype (no pili), which is IMP, and the primary data are in PMID:1971619. Please check the evidence code and reference.

## 206. WRONG_REFERENCE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:P22610 located_in GO:0005886 plasma membrane (IDA, PMID:9466269)
- **Field:** DB:Reference
- **Change:** check PMID:9466269 (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/PSEAE/pilD/pilD-ai-review.yaml`

located_in GO:0005886 plasma membrane (IDA) on PA4528 pilD cites Kagami et al. 1998 (PMID:9466269), whose abstract is about xcpT temperature-sensitive mutants and xcpR suppressors and mentions PilD/XcpA only as the enzyme processing XcpT-W. If the full text has no PilD localization data, the row would be better keyed to PMID:1898929 (xcpA localised to the cytoplasmic membrane) or PMID:8331069. Please check. The row is a seed of the PAINT plasma membrane IBD at PTN000766410, which has two other seeds.

> These proteins, in addition to the pilin subunit, are cleaved and methylated by the PilD/XcpA prepilin peptidase
> — PMID:9466269

## 207. WRONG_EVIDENCE_CODE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:P22610 involved_in GO:0009297 pilus assembly (IDA, PMID:9668097)
- **Field:** Evidence_Code
- **Change:** check ECO:0000314 (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/PSEAE/pilD/pilD-ai-review.yaml`

involved_in GO:0009297 pilus assembly (IDA) on PA4528 pilD cites Pepe and Lory 1998 (PMID:9668097). The pilus-assembly evidence in the abstract is from PilD Gly95/Lys96 variants expressed in P. aeruginosa, i.e. a mutant phenotype (IMP). The term could also be the more specific GO:0043683 type IV pilus assembly. Please check.

## 208. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:P22610 part_of GO:0015627 type II protein secretion system complex (IDA, PMID:1588814)
- **Field:** GO_ID
- **Change:** check GO:0015627 (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/PSEAE/pilD/pilD-ai-review.yaml`

part_of GO:0015627 type II protein secretion system complex (IDA) on PA4528 pilD cites Bally et al. 1992 (PMID:1588814), whose abstract shows that XcpA/PilD processes the pseudopilins XcpT-W in vivo. That supports a role in type II secretion (processing of secretion apparatus components), not membership of the secretion complex (the full text was not available to check for complex data); PilD is the prepilin peptidase shared with the type IV pilus system. Please consider replacing it with involved_in GO:0015628 protein secretion by the type II secretion system (e.g. IMP, PMID:1671384) or deleting it.

## 209. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:G3XD28 located_in GO:0044096 type IV pilus (IMP, PMID:7565110)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0044096
- **Recorded in:** `genes/PSEAE/pilM/pilM-ai-review.yaml`

located_in GO:0044096 type IV pilus (IMP, PMID:7565110) on PA5044 pilM records that pilM mutants lack fimbriae, which is a mutant phenotype and is already captured by the type IV pilus assembly and motility rows from the same paper. PilM is a cytoplasmic protein that associates with the inner membrane via PilN (PMID:19857645) and is not a component of the pilus fibre. Please delete the row. The same pattern applies to the pilN, pilO and pilP rows from PMID:7565110. This row is the sole seed of the PAINT IBD at PTN001286216.

> PilM-P were found to be required for fimbrial biogenesis
> — PMID:7565110

## 210. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:G3XD30 located_in GO:0044096 type IV pilus (IMP, PMID:7565110)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0044096
- **Recorded in:** `genes/PSEAE/pilN/pilN-ai-review.yaml`

located_in GO:0044096 type IV pilus (IMP, PMID:7565110) on PA5043 pilN records that pilM-P mutants lack fimbriae, a mutant phenotype already captured by the type IV pilus assembly and motility rows from the same paper. PilN is a single-pass inner-membrane protein of the PilMNOP alignment subcomplex (PMID:19857645), not a component of the pilus fibre. Please delete the row (the same pattern applies to the pilM, pilO and pilP rows from PMID:7565110). It is the sole seed of the PAINT IBD of GO:0044096 at PTN002220336.

> PilM-P were found to be required for fimbrial biogenesis
> — PMID:7565110

## 211. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:P24559 located_in GO:0044096 type IV pilus (TAS, PMID:20595000)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0044096
- **Recorded in:** `genes/PSEAE/pilT/pilT-ai-review.yaml`

located_in GO:0044096 type IV pilus (TAS, PMID:20595000) on PA0395 pilT: GO:0044096 is the extracellular fibre, while PilT is the cytoplasmic hexameric retraction ATPase (functional YFP-PilT is cytoplasmic and polar, PMID:15659660). PilT's location is already captured by the cytoplasm rows. Please delete the row; the same machine-versus-fibre pattern affects the PseudoCAP type IV pilus rows on pilM, pilN, pilO and pilP.

> Type IV pili are bacterial extracellular filaments
> — PMID:20595000

## 212. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:G3XCX3 enables GO:0016888 DNA endonuclease activity, producing 5'-phosphomonoesters (IDA, PMID:18174131)
- **Field:** GO_ID
- **Change:** GO:0016888 → GO:0016887 (ATP hydrolysis activity)
- **Likely cause:** IDENTIFIER_TRANSPOSITION
- **Recorded in:** `genes/PSEAE/pilU/pilU-ai-review.yaml`

enables GO:0016888 "DNA endonuclease activity, producing 5'-phosphomonoesters" (IDA, PMID:18174131) on PA0396 pilU. Chiang et al. 2008 assayed purified 6xHis-PilB, PilT and PilU and found ATPase activity (stated in the abstract; no nuclease assay is mentioned) and PilU is a PilT-like type IV pilus retraction ATPase. The same paper was used on the same date (2019-03-11) to annotate PA4526 pilB and PA0395 pilT to GO:0016887 ATP hydrolysis activity, the adjacent GO id. Please change the GO id on the PA0396 row to GO:0016887. The row is the sole seed of a PAINT IBD at PTN000766390 that propagates DNA endonuclease activity to about 13 proteins.

> Assay of purified 6xHis-tagged PilB, PilT and PilU from P. aeruginosa showed that all three proteins have ATPase activities in vitro.
> — PMID:18174131

## 213. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:P06200 involved_in GO:0015628 protein secretion by the type II secretion system (IDA, PMID:11726509)
- **Field:** GO_ID
- **Change:** check GO:0015628 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/plcH/plcH-ai-review.yaml`

PA0844 (PlcH) is cargo of the Xcp type II secretion system, not a component of it. GO practice reserves "protein secretion by the type II secretion system" for the secretion machinery; the secreted substrate does not carry out the process. Consider deleting the row, or recording the cargo relationship on the Xcp proteins (has_input) and keeping an extracellular region component annotation on PlcH. The identical pattern was reported for PA3724 (LasB) and PA2939 (PaAP).

> two substrates for the Pseudomonas aeruginosa secreton, both phospholipases, use the twin-arginine translocation (Tat) system
> — PMID:11726509

## 214. WRONG_REFERENCE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:P06200 involved_in GO:0044179 hemolysis in another organism (IMP, PMID:23667230)
- **Field:** DB:Reference
- **Change:** check PMID:23667230 (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/PSEAE/plcH/plcH-ai-review.yaml`

involved_in GO:0044179 hemolysis in another organism (IMP) on PA0844 cites Jackson et al. 2013 (PMID:23667230). The cached full text of that paper reports no haemolysis experiment; its plcHR mutant phenotypes are epithelial-cell colonization, biofilm formation in surfactant, Anr regulon activation and mouse pneumonia virulence. Please check which reference was intended (for example the purified-enzyme haemolysis data in PMID:12410824, already annotated as IDA, or an earlier plcH mutant haemolysis study). Figures were not available in the extracted text, so a haemolysis panel cannot be entirely excluded. The term itself is correct for PlcH.

> A ΔplcHR mutant, known to be defective in virulence in animal models, was less able to colonize epithelial cell monolayers and was defective in biofilm formation on plastic when grown in lung surfactant
> — PMID:23667230

## 215. WRONG_REFERENCE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HYC2 enables GO:0004630 D-type glycerophospholipase activity (IMP, PMID:24832454)
- **Field:** DB:Reference
- **Change:** PMID:24832454 → PMID:23552891 (Diverse type VI secretion phospholipases are functionally plastic antibacterial effectors (Russell et al. 2013; PldA = Tle5PA, purified-enzyme assay))
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/pldA/pldA-ai-review.yaml`

The PseudoCAP IMP row for PA3487/pldA on GO:0004630 cites PMID:24832454, whose abstract states that the work characterises PldB, the paralogous phospholipase D effector encoded at PA5089. The same row with the same PMID is also present on PA5089, where it belongs. The annotated activity is correct for PldA, but its own evidence is elsewhere: PMID:23552891 shows purified PldA (Tle5PA) releasing choline from phosphatidylcholine with a requirement for His855, and PMID:11136451 reports calcium-regulated PLD activity for cloned pldA. Requested change: re-point the reference to PMID:23552891 (or PMID:11136451), and consider raising the evidence code from IMP accordingly. Filed as PROBABLE because only the abstract of PMID:24832454 is available; the full text might also contain PldA experiments.

> Here we describe the characterization of a P. aeruginosa H3-T6SS-dependent phospholipase D effector, PldB, and its three tightly linked cognate immunity proteins.
> — PMID:24832454

> vgrG5 (PA5090, blue) is encoded directly upstream of pldB (PA5089, cyan)
> — PMID:31417515

## 216. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I3Y3 located_in GO:0098567 periplasmic side of plasma membrane (IDA, PMID:14679249)
- **Change:** delete the record asserting GO:0098567
- **Recorded in:** `genes/PSEAE/pmpM/pmpM-ai-review.yaml`

PMID:14679249 (full text read) reports no localization, fractionation or topology experiment for PmpM; its only membrane-related assay is H+/drug antiport in everted membrane vesicles from E. coli expressing pmpM, which supports plasma membrane (already annotated by PseudoCAP from the same paper) but not the periplasmic side. PmpM is a 12-transmembrane-helix MATE transporter. Please delete the GO:0098567 row; the GO:0005886 row from the same paper is correct.

## 217. WRONG_EVIDENCE_CODE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HV31 involved_in GO:0000160 phosphorelay signal transduction system (IDA, PMID:14507375)
- **Field:** Evidence_Code
- **Change:** check ECO:0000314 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/pmrB/pmrB-ai-review.yaml`

PseudoCAP IDA row for PA4777/pmrB, GO:0000160 phosphorelay signal transduction system, from PMID:14507375 (McPhee, Lewenza and Hancock 2003). The abstract reports interposon mutants in pmrB and pmrA, lacZ reporter expression and peptide induction, which is mutant (IMP) evidence; it describes no biochemical assay of PmrB. SUSPECTED: the full text was not read and may contain a direct assay.

> Inactivation of the pmrB sensor kinase and pmrA response regulator greatly decreased the expression of the operon encoding pmrA-pmrB
> — PMID:14507375

## 218. WRONG_EVIDENCE_CODE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I758 enables GO:0004674 protein serine/threonine kinase activity (IDA, PMID:9852028)
- **Field:** Evidence_Code
- **Change:** check ECO:0000314 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/ppkA/ppkA-ai-review.yaml`

The GO:0004674 row on PA0074 (ppkA) is coded IDA from PMID:9852028. The abstract describes overexpression toxicity in E. coli and P. aeruginosa that a catalytic-site substitution abolishes, and concludes only that the kinase domain is "functional". That is a mutant phenotype (IMP-type), not a direct kinase assay. The term is right: direct in vitro evidence exists in Mougous et al. 2007 (PMID:17558395) and Hsu et al. 2009 (PMID:19400797). Requested change: check whether the full text contains a kinase assay; if not, recode as IMP or cite the later papers. The row is one of 17 seeds of PTN001981567, which stands without it. SUSPECTED because the full text was not available.

> However, a single amino acid change at the catalytic site of the kinase domain eliminated the toxic effect of PpkA on bacterial cells, suggesting that the kinase domain of PpkA is functional within bacterial cells.
> — PMID:9852028

## 219. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9ZN70 involved_in GO:0009247 glycolipid biosynthetic process (IMP, PMID:24275100)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0009247
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/ppx/ppx-ai-review.yaml`

The PseudoCAP row PA5241/ppx GO:0009247 glycolipid biosynthetic process IMP PMID:24275100 is based on altered rhamnolipid levels in a ppx null mutant. Ppx is an exopolyphosphatase and performs no step of rhamnolipid synthesis; the effect is a downstream consequence of polyP metabolism. Suggested change: delete the row (an annotation to regulation of the process would also need evidence of a specific regulatory role). PROBABLE: abstract only read.

> Results obtained from the ppx null mutant demonstrated that Ppx is involved in the production of virulence factors associated with both acute infection (e.g. motility-promoting factors, blue/green pigment production, C6-C12 quorum-sensing homoserine lactones) and chronic infection (e.g. rhamnolipids, biofilm formation).
> — PMID:24275100

## 220. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9ZN70 involved_in GO:0009372 quorum sensing (IMP, PMID:24275100)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0009372
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/ppx/ppx-ai-review.yaml`

The PseudoCAP row PA5241/ppx GO:0009372 quorum sensing IMP PMID:24275100 is based on altered C6-C12 AHL levels in a ppx null mutant. Ppx is an exopolyphosphatase, not an AHL synthase, receptor or regulator; the effect is indirect. Suggested change: delete the row. PROBABLE: abstract only read.

> Results obtained from the ppx null mutant demonstrated that Ppx is involved in the production of virulence factors associated with both acute infection (e.g. motility-promoting factors, blue/green pigment production, C6-C12 quorum-sensing homoserine lactones) and chronic infection (e.g. rhamnolipids, biofilm formation).
> — PMID:24275100

## 221. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I0Q0 enables GO:0004497 monooxygenase activity (IDA, PMID:20662781)
- **Field:** GO_ID
- **Change:** GO:0004497 → GO:0102164 (2-heptyl-3-hydroxy-4(1H)-quinolone synthase activity)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/pqsH/pqsH-ai-review.yaml`

The PseudoCAP IDA row for PA2587/pqsH from PMID:20662781 (Schertzer et al. 2010) is not wrong, only under-specific. The paper shows purified MBP-PqsH converting HHQ + NADH + O2 to PQS, which is exactly GO:0102164 / RHEA:37871 / EC 1.14.13.182. Requested change: re-point (or add) the IDA to GO:0102164. GO:0102164 is_a GO:0016709 is_a GO:0004497, so the PAINT IBD on PTN008173107 (monooxygenase activity) stays supported by a descendant-term experimental annotation.

> we show that PqsH catalyses the terminal step in PQS production, synthesizing PQS in vitro using the substrates 2-heptyl-4-quinolone (HHQ), NADH and oxygen
> — PMID:20662781

## 222. WRONG_REFERENCE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I5E3 involved_in GO:0006099 tricarboxylic acid cycle (IDA, PMID:7626013)
- **Field:** DB:Reference
- **Change:** check PMID:7626013 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/prpC/prpC-ai-review.yaml`

PseudoCAP IDA rows GO:0006099 and GO:0036440 for PA0795/prpC (Q9I5E3) cite Mitchell et al. 1995 (PMID:7626013), which purified two native citrate synthases (hexameric CSI, dimeric CSII) and, per its abstract, did not identify their genes; the same rows were given to gltA (P14165). CSII matches PrpC (homodimer of ~41 kDa), so the attribution is probably right, but it is an inference. Please check the full text; if no gene identity is given, add or repoint to Dolan et al. 2022 (PMID:36377867), which assays purified recombinant PrpC. For GO:0006099, note that PrpC's TCA-cycle role is a backup to GltA. SUSPECTED because only the abstract was read.

> It is suggested that the CS isoenzymes are products of different structural genes.
> — PMID:7626013

## 223. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I1N6 involved_in GO:0044010 single-species biofilm formation (IDA, PMID:19659934)
- **Field:** Evidence_Code
- **Change:** ECO:0000314 → ECO:0000315 (mutant phenotype evidence used in manual assertion)
- **Recorded in:** `genes/PSEAE/pslC/pslC-ai-review.yaml`

GO:0044010 single-species biofilm formation for PslC (PA2233, Q9I1N6) from PMID:19659934 is coded IDA, but the evidence is an in-frame deletion mutant that loses Psl and surface attachment, which is IMP. This row is the sole seed of the PAINT IBD at PTN002463206, which propagates biofilm formation to unrelated GT-2 glycosyltransferases.

> The same eleven strains that were deficient in attachment likewise did not produce detectable levels of Psl.
> — PMID:19659934

## 224. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:G3XDA6 involved_in GO:1900378 positive regulation of secondary metabolite biosynthetic process (IMP, PMID:16109947)
- **Field:** GO_ID
- **Change:** GO:1900378 → GO:0050709
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/ptrB/ptrB-ai-review.yaml`

involved_in GO:1900378 positive regulation of secondary metabolite biosynthetic process (IMP) on ptrB (PA0612) cites Wu and Jin 2005, which shows that PtrB represses the type III secretion system (deletion restores ExoS secretion and exoT transcription) and reports no secondary-metabolite phenotype. The supported term is negative regulation of protein secretion (GO:0050709; GO has no type III specific regulation term). This row is the sole seed of the PTN002215317 IBD (8 leaf IBAs).

> Therefore, PtrB is a new TTSS repressor that coordinates TTSS repression and pyocin synthesis under the stress of DNA damage.
> — PMID:16109947

## 225. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:P72131 enables GO:0003950 NAD+ poly-ADP-ribosyltransferase activity (IMP, PMID:8843437)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0003950
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/ptxR/ptxR-ai-review.yaml`

PseudoCAP IMP row for PA2258/ptxR, GO:0003950 NAD+ poly-ADP-ribosyltransferase activity, from PMID:8843437 (Hamood et al. 1996). The abstract states that PtxR is a LysR-family transcriptional activator and that ptxR mutants show reduced exotoxin A activity, with ptxR increasing toxA and regA transcription. The ADP-ribosyltransferase activity measured is that of exotoxin A (ToxA, PA1148), not of PtxR. Requested change: delete the row; the regulatory role is already annotated as GO:0045893 (IDA, PMID:22844393).

> The deduced amino acid sequence of PtxR is homologous to that of several members of the LysR family of transcriptional activators.
> — PMID:8843437

> both mutants showed a significant reduction in the level of exotoxin A activity
> — PMID:8843437

## 226. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I182 involved_in GO:0002049 pyoverdine biosynthetic process (IMP, PMID:12700264)
- **Field:** Evidence_Code
- **Change:** IMP → IDA
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/pvdD/pvdD-ai-review.yaml`

PseudoCAP rows for PvdD (PA2399, Q9I182) GO:0002049 and GO:0003824, IMP, PMID:12700264 (Ackerley, Caradoc-Davies and Lamont 2003). The abstract describes overexpression of the first PvdD module in E. coli, purification, ATP-PPi exchange assays with L-threonine and other amino acids, and structural modelling; it mentions no pvdD mutant. A purified-protein assay is IDA. Abstract-only reading (the PMC copy returned no body text), so a mutant experiment in the full text cannot be excluded.

> The first module of pvdD was overexpressed in Escherichia coli, and the protein product was purified.
> — PMID:12700264

## 227. WRONG_REFERENCE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I182 involved_in GO:0002049 pyoverdine biosynthetic process (IMP, PMID:9770291)
- **Field:** DB:Reference
- **Change:** check PMID:9770291 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/pvdD/pvdD-ai-review.yaml`

PseudoCAP rows for PvdD (Q9I182) GO:0002049 and GO:0003824, IMP, PMID:9770291 (Stintzi et al. 1998). The abstract reports reduced pyoverdine in lasR/lasI mutants and measures pvdD expression in them; it describes pvdD as already known to be involved in peptide synthesis and reports no pvdD mutant. Please check whether the full text has a pvdD mutant phenotype; if not, the IMP rows should cite a paper with one, such as PMID:15271355. SUSPECTED because the call rests on what the abstract does not say.

> lasR mutants were not altered with respect to expression of the pvdD gene involved in the synthesis of the peptide portion of pyoverdine
> — PMID:9770291

## 228. WRONG_EVIDENCE_CODE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I181 involved_in GO:0002049 pyoverdine biosynthetic process (IMP, PMID:19854904)
- **Field:** Evidence_Code
- **Change:** check IMP (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/pvdJ/pvdJ-ai-review.yaml`

PseudoCAP rows for PvdJ (PA2400, Q9I181) GO:0002049 pyoverdine biosynthetic process and GO:0003824 catalytic activity, IMP, PMID:19854904 (Taguchi et al. 2010, J Bacteriol). The paper, read in full, constructs Delta pvdJ, Delta pvdL and Delta fpvA mutants of Pseudomonas syringae pv. tabaci 6605 only; no P. aeruginosa mutant is made. A mutant phenotype in another species cannot be IMP for the PAO1 gene. Please either re-reference the rows to P. aeruginosa evidence (for example PMID:15271355) or recode as ISS with the P. syringae protein in WITH/FROM, noting that the P. syringae PvdJ is described as an L-Thr-L-Ser component, so module-level equivalence to PAO1 PvdJ is not established.

> The constructs were digested with StuI, AfaI, or AgeI to delete 483, 196, or 975 internal bp for generation of the Δ fpvA , Δ pvdJ , or Δ pvdL mutant, respectively.
> — PMID:19854904

## 229. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I194 located_in GO:0005737 cytoplasm (IDA, PMID:22498339)
- **Field:** GO_ID
- **Change:** GO:0005737 → GO:0042597 (periplasmic space)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/pvdQ/pvdQ-ai-review.yaml`

The PseudoCAP IDA row places PA2385/PvdQ in the cytoplasm from PMID:22498339 (Guillon et al. 2012), whose abstract states outright that PvdQ is uniformly distributed in the periplasm; the cytoplasmic protein in that study is PvdA. Re-point the row to periplasmic space. This row does not seed a PAINT IBD.

> Epifluorescence and TIRF imaging on cells expressing labelled PvdQ showed that this enzyme was uniformly distributed in the periplasm
> — PMID:22498339

## 230. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I191 involved_in GO:0002049 pyoverdine biosynthetic process (IMP, PMID:12686626)
- **Field:** GO_ID
- **Change:** GO:0002049 → GO:0015891 (siderophore transport)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/pvdR/pvdR-ai-review.yaml`

pvdR is a component of the PvdRT-OpmQ efflux pump, which exports pyoverdine from the periplasm to the medium. The IMP row from PMID:12686626 (Lamont and Martin 2003) records lower pyoverdine yield in a mutant as involvement in pyoverdine biosynthesis. A transporter mutant makes less extracellular pyoverdine because export and recycling fail, which also lowers synthesis indirectly (Imperi et al. 2009, PMID:19906986). The pump does none of the chemistry of synthesis. Requested change: re-point to GO:0015891 siderophore transport (or delete). PROBABLE because the 2003 paper was read as an abstract only.

> our preliminary results suggest that the lower PVD levels in their culture supernatants are a result of reduced PVD synthesis rather than of impaired secretion of de novo synthesized PVD
> — PMID:19906986

> Bacteria lacking this efflux pump accumulated PVD, or a fluorescent precursor, in the periplasm, due to their inability to efficiently secrete into the media newly synthesized PVD.
> — PMID:21035449

## 231. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I191 enables GO:0015562 efflux transmembrane transporter activity (IDA, PMID:19906986)
- **Field:** Evidence_Code
- **Change:** IDA → IMP
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/pvdR/pvdR-ai-review.yaml`

The IDA row for pvdR (GO:0015562 efflux transmembrane transporter activity) cites PMID:19906986 (Imperi et al. 2009). Full text read: every result for PvdR, PvdT and OpmQ is a mutant phenotype (PVD levels in supernatants, periplasmic fractions and confocal images of transposon or deletion mutants, with complementation). The paper does not assay the purified protein or the assembled complex. The same paper already supports the parallel IMP row, so the IDA row should be recoded as IMP or deleted. PROBABLE rather than CONFIRMED because the supplementary material was not read.

> Conversely, PA2389 , PA2390 , and opmQ mutants accumulated five- to sixfold higher amounts of PVD than wild-type PAO1, suggesting an involvement of these genes in PVD export.
> — PMID:19906986

## 232. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I191 part_of GO:1990281 efflux pump complex (IDA, PMID:19906986)
- **Field:** Evidence_Code
- **Change:** IDA → IMP
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/pvdR/pvdR-ai-review.yaml`

The IDA row for pvdR (GO:1990281 efflux pump complex) cites PMID:19906986 (Imperi et al. 2009). Full text read: every result for PvdR, PvdT and OpmQ is a mutant phenotype (PVD levels in supernatants, periplasmic fractions and confocal images of transposon or deletion mutants, with complementation). The paper does not assay the purified protein or the assembled complex. The same paper already supports the parallel IMP row, so the IDA row should be recoded as IMP or deleted. PROBABLE rather than CONFIRMED because the supplementary material was not read.

> Conversely, PA2389 , PA2390 , and opmQ mutants accumulated five- to sixfold higher amounts of PVD than wild-type PAO1, suggesting an involvement of these genes in PVD export.
> — PMID:19906986

## 233. WRONG_REFERENCE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:G3XCV1 involved_in GO:1900378 positive regulation of secondary metabolite biosynthetic process (IMP, PMID:15073293)
- **Field:** DB:Reference
- **Change:** check PMID:15073293 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/pvdS/pvdS-ai-review.yaml`

PseudoCAP IMP GO:1900378 on PA2426/pvdS cites Juhas et al. 2004, a study of the VqsR (PA2591) regulator. The abstract reports reduced siderophore transcripts in a vqsR mutant and does not mention a pvdS mutant. If pvdS appears only as a VqsR-dependent transcript, the row describes VqsR, not PvdS, regulating biosynthesis. Please check; the claim is well supported for PvdS by PMID:7651323 and PMID:8636031.

> the vqsR mutant harboured less mRNA transcript for the production of siderophores
> — PMID:15073293

## 234. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I190 involved_in GO:0002049 pyoverdine biosynthetic process (IMP, PMID:12686626)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0002049
- **Recorded in:** `genes/PSEAE/pvdT/pvdT-ai-review.yaml`

The PseudoCAP IMP GO:0002049 pyoverdine biosynthetic process on PA2390 pvdT (PMID:12686626) rests on a mutant screen scored by pyoverdine production. PvdT is the inner membrane ABC component of the PvdRT-OpmQ exporter; pvdT mutants accumulate pyoverdine in the periplasm (PMID:19906986, full text; PMID:21035449), so the lower extracellular level is an export defect. Please delete the row or replace it with siderophore transmembrane transport (GO:0044718). Only the abstract of PMID:12686626 was read. This row does not seed a worklist IBD.

> nearly all intracellular PVD was associated with the periplasmic fraction of pvdR , pvdT , and opmQ mutants
> — PMID:19906986

> Bacteria lacking this efflux pump accumulated PVD, or a fluorescent precursor, in the periplasm, due to their inability to efficiently secrete into the media newly synthesized PVD
> — PMID:21035449

## 235. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HU21 involved_in GO:0009244 lipopolysaccharide core region biosynthetic process (IDA, PMID:11065359)
- **Field:** Evidence_Code
- **Change:** check ECO:0000314 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/rmlC/rmlC-ai-review.yaml`

GO:0009244 for rmlC (Q9HU21, PA5164) is coded IDA to PMID:11065359. The abstract describes non-polar chromosomal rmlC mutants whose LPS was analysed by SDS-PAGE, immunoblotting and structural analysis of the mutant core: the attribution to rmlC rests on the mutant phenotype, so IMP is the appropriate code. The term itself is correct. PROBABLE because the full text could include a direct biochemical experiment not described in the abstract.

> Non-polar chromosomal rmlC mutants were generated in P. aeruginosa strains PAO1 (serotype O5) and PAK (serotype O6) and LPS extracted from the mutants was analysed by SDS-PAGE and Western immunoblotting.
> — PMID:11065359

## 236. WRONG_EVIDENCE_CODE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:P45684 involved_in GO:0006355 regulation of DNA-templated transcription (IDA, PMID:10383954)
- **Field:** Evidence_Code
- **Change:** IDA → IMP
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/rpoS/rpoS-ai-review.yaml`

PseudoCAP row for PA3622/rpoS (P45684), GO:0006355 regulation of DNA-templated transcription, IDA, PMID:10383954 (Suh et al. 1999). The full text was read: it reports stress sensitivity, catalase, exoproduct, twitching and alginate phenotypes of rpoS mutants and contains no transcription assay (no lacZ fusion, primer extension, RT-PCR or in vitro transcription). The evidence is a mutant phenotype, so IMP, not IDA. A direct transcription reference for RpoS is PMID:20735777 (psl). The row seeds PTN000779307, whose IBD stands on other seeds.

> In addition, the PAO1 rpoS mutant was hypersensitive to heat shock at 50°C, increased osmolarity, and prolonged exposure to high concentrations of H 2 O 2 .
> — PMID:10383954

## 237. WRONG_EVIDENCE_CODE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I2W5 enables GO:0016987 sigma factor activity (IDA, PMID:10438740)
- **Field:** Evidence_Code
- **Change:** check ECO:0000314 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/sigX/sigX-ai-review.yaml`

The PseudoCAP row for PA1776/sigX, GO:0016987 sigma factor activity from PMID:10438740 (Brinkman et al. 1999), is coded IDA. The abstract describes only genetic evidence: a sigX disruption, Northern analysis and primer extension comparing sigX-mutant and wild-type RNA. It describes no purified-protein assay, which would fit IMP. The full text could not be read, so the code may still reflect an experiment the abstract omits. The term itself is correct and the PTN002455017 IBD is unaffected either way.

> Comparison of sigX-disrupted and wild-type cell transcripts by primer extension indicated that monocistronic transcription of oprF occurs from two overlapping promoters
> — PMID:10438740

## 238. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I2W5 involved_in GO:0030307 positive regulation of cell growth (IMP, PMID:10438740)
- **Field:** GO_ID
- **Change:** check GO:0030307 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/sigX/sigX-ai-review.yaml`

PseudoCAP IMP GO:0030307 positive regulation of cell growth on PA1776/sigX from PMID:10438740. The abstract states the phenotype as a markedly reduced logarithmic-phase growth rate in rich medium, a population growth-rate defect of a regulator mutant, not the increase in cell size that GO:0016049 cell growth denotes. Consider deleting the row or replacing it with a term for the direct regulatory role. This row does not seed an IBD.

> which included a markedly reduced logarithmic-phase growth rate in rich medium
> — PMID:10438740

## 239. OTHER (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HV35 enables GO:0004014 adenosylmethionine decarboxylase activity (IMP, PMID:22155771)
- **Field:** Reference
- **Change:** check PMID:22155771 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/speH/speH-ai-review.yaml`

The PseudoCAP IMP adenosylmethionine decarboxylase activity row for PA4773 cites Johnson et al. 2012 (PMID:22155771). The abstract describes PA4773 only as a DNA-induced speD homolog and reports the mutant phenotypes (antibiotic and oxidative-stress susceptibility, no surface spermidine) for a PA4774 (speE2) mutant. No PA4773 mutant and no decarboxylase assay are described in the abstract. The full text (not available to this review) may contain a PA4773 mutant, so this is a request to check that the IMP rests on a PA4773 experiment; otherwise the evidence code should be ISS/IEA. The term itself is correct for SpeH (HAMAP MF_00464).

> annotated as homologs of the spermidine synthesis genes speD (PA4773) and speE
> — PMID:22155771

> Mutation of PA4774
> — PMID:22155771

## 240. WRONG_REFERENCE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I6J4 involved_in GO:0046203 spermidine catabolic process (IMP, PMID:21622750)
- **Field:** DB:Reference
- **Change:** PMID:21622750 → PMID:12081945
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/spuA/spuA-ai-review.yaml`

The PseudoCAP IMP row for PA0297/spuA (spermidine catabolic process) cites Yao et al. 2011. Its abstract does not mention spuA, and in the full text (read online from PMC3147493, not cached) spuA/pauD1 appears only as a restatement of the laboratory's earlier result; the new mutants in that paper are pauA genes. The spuA mutant phenotype was reported by Lu et al. 2002 (PMID:12081945). The term is correct, so the PAINT IBD on PTN000230196 is unaffected. PROBABLE rather than CONFIRMED because the supplementary material was not checked.

> Although spuA and spuB mutants showed an apparent defect in spermidine utilization, the biochemical functions of the gene products have yet to be elucidated.
> — PMID:12081945

## 241. WRONG_REFERENCE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I6J5 involved_in GO:0009447 putrescine catabolic process (IMP, PMID:12081945)
- **Field:** REFERENCE
- **Change:** PMID:12081945 → PMID:21622750
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/spuI/spuI-ai-review.yaml`

The PseudoCAP IMP GO:0009447 row on PA0296/spuI cites Lu et al. 2002 (PMID:12081945), whose full text says spuI mutations show no growth defect on agmatine and polyamines. Putrescine catabolism by spuI (pauA1) is shown by Yao et al. 2011 (PMID:21622750) with pauA1A4 and pauA1A2A4 mutants. Re-point the reference; the GO term is correct.

> While mutations on spuI did not show any growth defect on agmatine and polyamines
> — PMID:12081945

## 242. WRONG_REFERENCE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I6J5 involved_in GO:0046203 spermidine catabolic process (IMP, PMID:12081945)
- **Field:** REFERENCE
- **Change:** delete the record asserting PMID:12081945
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/spuI/spuI-ai-review.yaml`

The PseudoCAP IMP GO:0046203 spermidine catabolic process row on PA0296/spuI cites PMID:12081945, whose full text states that spuI mutations cause no growth defect on agmatine and polyamines; the spermidine defect it reports is for spuA and spuB. Yao et al. 2011 (PMID:21622750) assign spermidine utilization to pauA2 (PA0298/spuB). Delete the row (it may have been meant for spuB, which already carries GO:0046203).

> Although spuA and spuB mutants showed an apparent defect in spermidine utilization
> — PMID:12081945

## 243. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:P53593 involved_in GO:0046777 protein autophosphorylation (IDA, PMID:10671455)
- **Change:** delete the record asserting GO:0046777
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/sucC/sucC-ai-review.yaml`

GO:0046777 protein autophosphorylation for sucC (P53593, SCS beta) is coded IDA to PMID:10671455. In that paper the phosphorylated protein is the 30-kDa alpha subunit (SucD), and the label is the catalytic phosphohistidine intermediate of succinyl-CoA synthetase, not a regulatory autophosphorylation. Delete it from SucC; for SucD it would also be better captured by the ligase activity. PROBABLE (full text read) because how a curator should treat the phosphoenzyme intermediate is a matter of interpretation. Not an IBD seed.

> A 5 μM concentration of GDP in the reaction mixture stimulated the phosphorylation of the 30-kDa Scs α subunit, whereas 50 μM GDP in the reaction mixture showed a significant decrease.
> — PMID:10671455

## 244. WRONG_EVIDENCE_CODE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HU66 involved_in GO:0052837 thiazole biosynthetic process (IDA, PMID:9209060)
- **Field:** Evidence_Code
- **Change:** check ECO:0000314 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/thiI/thiI-ai-review.yaml`

involved_in GO:0052837 thiazole biosynthetic process (IDA) on PA5118 cites Webb, Claas & Downs 1997 (PMID:9209060), "Characterization of thiI, a new gene involved in thiazole biosynthesis in Salmonella typhimurium". The abstract states outright that the paper characterises the Salmonella thiI gene (mapping it on the S. typhimurium chromosome and sequencing it) and describes no P. aeruginosa work; the 1997 paper also predates the PAO1 genome, so it is not direct-assay evidence for PA5118. Either recode the row as ISS with the Salmonella ThiI accession in With/From, or delete it. This row is the only seed of the PANTHER IBD at PTN001804941, which propagates thiazole biosynthesis to 25 ThiI family members including Firmicutes and archaea whose ThiI is not needed for thiamine.

> Thiamine pyrophosphate (TPP) is a required cofactor in Salmonella typhimurium
> — PMID:9209060

> thiI is a 1,449-bp open reading frame located at minute 9.65 on the S. typhimurium chromosome
> — PMID:9209060

## 245. WRONG_EVIDENCE_CODE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:P29364 enables GO:0004413 homoserine kinase activity (IDA, PMID:10220164)
- **Field:** Evidence_Code
- **Change:** check ECO:0000314 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/thrB/thrB-ai-review.yaml`

enables GO:0004413 (IDA) on PA5495 thrB cites Patte et al. 1999, whose abstract reports only genetics (thrB thrH double mutant auxotrophy, thrH complementation of E. coli thrB and serB mutants) and no homoserine kinase assay of ThrB. Please check whether the full text contains such an assay. If not, the activity is better supported by ISS/IBA to the type II HSK family (HAMAP MF_00301); the genetics support the process (IGI with thrH). This row is the sole seed of the PANTHER IBD at PTN001464661 and one of two at PTN001464650.

> In P. aeruginosa, threonine auxotrophy is observed only when both thrB and thrH are simultaneously inactivated.
> — PMID:10220164

## 246. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:P29364 involved_in GO:0009088 L-threonine biosynthetic process (IDA, PMID:10220164)
- **Field:** Evidence_Code
- **Change:** check ECO:0000314 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/thrB/thrB-ai-review.yaml`

involved_in GO:0009088 (IDA) on PA5495 thrB cites Patte et al. 1999, whose abstract reports, as the evidence for thrB, that threonine auxotrophy appears only in thrB thrH double mutants. That is a genetic interaction (IGI with thrH), not a direct assay; the full text (not available here) could add an enzyme assay. The annotation is correct.

> In P. aeruginosa, threonine auxotrophy is observed only when both thrB and thrH are simultaneously inactivated.
> — PMID:10220164

## 247. WRONG_QUALIFIER (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:P20576 enables GO:0004049 anthranilate synthase activity (IMP, PMID:2153661)
- **Field:** Qualifier
- **Change:** check enables (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/trpG/trpG-ai-review.yaml`

The anthranilate synthase reaction (chorismate + L-glutamine to anthranilate + pyruvate + L-glutamate) is carried out by the TrpE-TrpG heterotetramer: TrpG is the glutamine amidotransferase subunit that supplies ammonia and TrpE condenses it with chorismate. The genetic evidence is for the TrpEG pair, so contributes_to GO:0004049 describes the subunit role more accurately than enables. Same request as for the paralogous phnB row (P09786).

> Heterotetramer consisting of two non-identical subunits: a
> — file:PSEAE/trpG/trpG-uniprot.txt

## 248. WRONG_GENE_PRODUCT (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I739
- **Subject:** UniProtKB:Q9I739
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0097351 on Q9I739 (tse6)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/tse6/tse6-ai-review.yaml`

GO:0097351 toxin sequestering activity is annotated by IMP from PMID:24589350 to both halves of the tse6-tsi6 effector-immunity pair. The term describes binding a toxin to neutralise it, so it fits the immunity protein Tsi6 and inverts the role of the effector Tse6, which is the toxin being neutralised. The full text states the direction explicitly: the Tse6 Toxin_61 domain is a potent cytoplasmic toxin whose activity is specifically neutralized by Tsi6, and co-expression of Tsi6 but not of the non-cognate Tsi2 rescued viability. Suggested change: delete the row on Q9I739 and keep it on Q9I740. CONFIRMED from the full text, not an abstract.

> These results demonstrate that the Toxin_61 domain of Tse6 is a potent cytoplasmic toxin whose activity can be specifically neutralized by Tsi6.
> — PMID:24589350

> the observed toxicity was specific to Tse6-CT as co-expression of Tsi6, but not the non-cognate cytoplasmic immunity protein Tsi2, provided full rescue of E. coli viability
> — PMID:24589350

## 249. WRONG_REFERENCE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I737 involved_in GO:0033103 protein secretion by the type VI secretion system (IMP, PMID:21325275)
- **Field:** DB:Reference
- **Change:** PMID:21325275 → PMID:30455305
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/vgrG1b/vgrG1b-ai-review.yaml`

involved_in GO:0033103 (IMP) and part_of GO:0033104 (IMP) on vgrG1b (PA0095) both cite Hachani et al. 2011, whose result for this gene is negative: VgrG1b is not required for Hcp1 or VgrG1a/VgrG1c secretion, and its own release is unaffected by deletion of clpV1, clpV2, clpV3 or all three. The paper's conclusion is that VgrG1b neither needs nor supports the H1-T6SS for secretion, so it cannot be the IMP support for a positive T6SS secretion or complex row. The claims are supported by later work: Pissaridou et al. 2018 (PMID:30455305) show VgrG1b forms a spike topped by the PAAR protein Tse7 whose delivery depends on the H1-T6SS cluster, and Hachani et al. 2014 (PMID:24794869) show vgrG1b alone restores activity to a triple vgrG1abc mutant. Please repoint both rows to those references. These rows are two of the three seeds of the PTN002088178 IBDs; the node itself stands on the VgrG1a and VgrG1c seeds.

> Overall, these results indicate that although vgrG1b is co-expressed with H1-T6SS genes, VgrG1b neither impacts secretion of components of the H1-T6SS nor requires H1-T6SS components for its own secretion.
> — PMID:21325275

> Thus, VgrG1b secretion is independent of the three known T6SS clusters.
> — PMID:21325275

## 250. WRONG_EVIDENCE_CODE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HUF5 involved_in GO:0009244 lipopolysaccharide core region biosynthetic process (IDA, PMID:9171387)
- **Field:** Evidence_Code
- **Change:** check ECO:0000314 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/waaC/waaC-ai-review.yaml`

The abstract of PMID:9171387 reports cloning by complementation of a Salmonella waaC mutant (restored smooth LPS), sequence identity, maxicell expression and failed chromosomal knockouts; it describes no direct assay of WaaC. IGI (complementation) or IMP looks like the right code. Only the abstract was read, so the full text could contain an assay, hence SUSPECTED and CHECK. The GO term is sound.

## 251. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HUF5 enables GO:0071968 lipid A-core heptosyltransferase activity (ISS, PMID:9171387)
- **Field:** GO_ID
- **Change:** GO:0071968 → GO:0008920 (lipopolysaccharide heptosyltransferase activity)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/waaC/waaC-ai-review.yaml`

GO:0071968 lipid A-core heptosyltransferase activity is defined as galactosyl-glucosyl3-heptosyl3-KDO2-lipid A-bisphosphate + ADP-heptose = lipid A-core + ADP. The with/from protein, Salmonella WaaC (P26469), is heptosyltransferase I (EC 2.4.99.23), which transfers the first heptose to Kdo2-lipid A. GO has no term for that reaction, so the correct term is the parent GO:0008920. The same row was made for waaF (PA5012), whose correct term is GO:0008713.

## 252. WRONG_EVIDENCE_CODE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:G3XD35 involved_in GO:0009244 lipopolysaccharide core region biosynthetic process (IDA, PMID:9171387)
- **Field:** Evidence_Code
- **Change:** check ECO:0000314 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/waaF/waaF-ai-review.yaml`

The abstract of PMID:9171387 reports cloning of waaF by complementation of a Salmonella waaF mutant, sequence identity, maxicell expression and failed chromosomal knockouts; no direct assay of WaaF is described. IGI (or IMP) looks like the right code. Only the abstract was read, hence SUSPECTED and CHECK. Same issue on the waaC (PA5011) row from this paper.

## 253. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:G3XD35 enables GO:0071968 lipid A-core heptosyltransferase activity (ISS, PMID:9171387)
- **Field:** GO_ID
- **Change:** GO:0071968 → GO:0008713 (ADP-heptose-lipopolysaccharide heptosyltransferase activity)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/waaF/waaF-ai-review.yaml`

GO:0071968 lipid A-core heptosyltransferase activity is defined with a galactosyl-glucosyl3-heptosyl3-KDO2-lipid A-bisphosphate acceptor. The with/from protein, Salmonella WaaF (P37421), is heptosyltransferase II (EC 2.4.99.24), whose reaction (heptosyl-Kdo2-lipid A acceptor) is GO:0008713. The same wrong term was used on waaC (PA5011).

## 254. WRONG_TERM (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HUG6 involved_in GO:0009243 O antigen biosynthetic process (IMP, PMID:15838026)
- **Field:** GO_ID
- **Change:** check GO:0009243 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/waaL/waaL-ai-review.yaml`

waaL (PA4999) is annotated IMP to GO:0009243 O antigen biosynthetic process (PMID:15838026). WaaL ligates the completed, polymerized O antigen onto lipid A-core, a step of LPS assembly after O-chain synthesis; GO:0009103 lipopolysaccharide biosynthetic process is the more accurate process. Consider re-annotating. This row is the sole seed of the PAINT IBD for GO:0000271 at PTN008076295, which remains valid either way.

> The completed chains are covalently attached to lipid A core by the O-antigen ligase, WaaL.
> — PMID:15838026

## 255. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HUG6 involved_in GO:0009297 pilus assembly (IMP, PMID:15838026)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0009297
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/waaL/waaL-ai-review.yaml`

waaL (PA4999) is annotated IMP to GO:0009297 pilus assembly from PMID:15838026. The O-antigen ligase does not participate in pilus assembly; the twitching/pilus defect of the O-antigen-less mutant is an indirect envelope phenotype. Please remove (or capture as a phenotype rather than a GO process). Audit 2026-10-29 - full text read at PMC1082828; its only data on pili, flagella and motility are mutant phenotypes (TEM counts, twitching and swimming assays), which the authors attribute to a disturbed outer membrane and reduced surface wettability.

## 256. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HUG6 enables GO:0016874 ligase activity (IDA, PMID:17697256)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0016874
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/waaL/waaL-ai-review.yaml`

waaL (PA4999) is annotated IDA to GO:0016874 ligase activity citing PMID:17697256. WaaL is EC 2.4.99.26, an ATP-independent, metal-independent inverting glycosyltransferase (PMID:21983211, PMID:30047569); the ATP hydrolysis reported in 2007 was not reproduced (the 2012 abstract states that P. aeruginosa WaaL cannot hydrolyse ATP in vitro). Neither full text was read, so this rests on a published conflict resolved in favour of the later work (as UniProt and the EC classification also do), hence PROBABLE. GO:0008754 O-antigen ligase activity (is_a glycosyltransferase activity) is the correct MF and is already annotated. Please delete the ligase activity row.

> E. coli and Pseudomonas aeruginosa WaaL proteins cannot catalyze ATP hydrolysis in vitro
> — PMID:21983211

## 257. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HUG6 involved_in GO:0043107 type IV pilus-dependent motility (IMP, PMID:15838026)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0043107
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/waaL/waaL-ai-review.yaml`

waaL (PA4999) is annotated IMP to GO:0043107 type IV pilus-dependent motility from PMID:15838026. The twitching defect of the O-antigen ligase mutant is an indirect consequence of altered LPS/envelope, not participation of WaaL in motility. Please remove. Audit 2026-10-29 - full text read at PMC1082828; its only data on pili, flagella and motility are mutant phenotypes (TEM counts, twitching and swimming assays), which the authors attribute to a disturbed outer membrane and reduced surface wettability.

## 258. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HUG6 involved_in GO:0044780 bacterial-type flagellum assembly (IMP, PMID:15838026)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0044780
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/waaL/waaL-ai-review.yaml`

waaL (PA4999) is annotated IMP to GO:0044780 bacterial-type flagellum assembly from PMID:15838026. Reduced flagellation of the O-antigen-less mutant is an indirect envelope phenotype; WaaL does not participate in flagellum assembly. Please remove. Audit 2026-10-29 - full text read at PMC1082828; its only data on pili, flagella and motility are mutant phenotypes (TEM counts, twitching and swimming assays), which the authors attribute to a disturbed outer membrane and reduced surface wettability.

## 259. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HUG6 involved_in GO:0071977 bacterial-type flagellum-dependent swimming motility (IMP, PMID:15838026)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0071977
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/waaL/waaL-ai-review.yaml`

waaL (PA4999) is annotated IMP to GO:0071977 bacterial-type flagellum-dependent swimming motility from PMID:15838026. The motility defect of the O-antigen ligase mutant is indirect (envelope/LPS), and waaL deletion in PA14 and PAK did not abolish swimming (PMID:29059582). Please remove. Audit 2026-10-29 - full text read at PMC1082828; its only data on pili, flagella and motility are mutant phenotypes (TEM counts, twitching and swimming assays), which the authors attribute to a disturbed outer membrane and reduced surface wettability.

## 260. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HUG5 involved_in GO:0009243 O antigen biosynthetic process (IMP, PMID:18178733)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0009243
- **Recorded in:** `genes/PSEAE/wapR/wapR-ai-review.yaml`

involved_in GO:0009243 O antigen biosynthetic process (IMP) on PA5000 wapR records the absence of O antigen from mutant LPS. The same abstract shows the cause is a truncated core lacking the alpha-1,3-L-Rha attachment site, so WapR acts in core biosynthesis (already annotated), not O antigen synthesis. PROBABLE because the full text, which might show an effect on O-antigen polymer synthesis itself, was not read.

> The capped core of the wapR mutant was found to be truncated and lacked alpha-1,3-L-Rha.
> — PMID:18178733

> one form is capped with O antigen through an alpha-1,3-linked L-rhamnose (L-Rha), while the other is uncapped and contains an alpha-1,6-linked L-Rha
> — PMID:18178733

## 261. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HUG5 involved_in GO:0015920 lipopolysaccharide transport (IDA, PMID:19589832)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0015920
- **Recorded in:** `genes/PSEAE/wapR/wapR-ai-review.yaml`

involved_in GO:0015920 lipopolysaccharide transport (IDA, PMID:19589832) is not what the paper studied: its abstract describes swimming and swarming motility, attachment to glass and flagellin glycosylation in mutants with truncated core oligosaccharide, and nothing on LPS export. The glycosyltransferase builds the core in the cytoplasm before LPS export. Please delete the row. PROBABLE because only the abstract was read.

> P. aeruginosa wild-type strain PAO1 and three isogenic mutants with defects in the rmlC, migA and wapR genes and producing truncated core oligosaccharide were investigated in terms of motility, attachment to glass and flagella expression.
> — PMID:19589832

> LPS truncations probably alter flagella-mediated motility in P. aeruginosa by modulating cell-surface attachment but not flagella synthesis
> — PMID:19589832

## 262. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:G3XD94 enables GO:0003954 NADH dehydrogenase activity (EXP, PMID:18621892)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0003954
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/wbpA/wbpA-ai-review.yaml`

GO:0003954 NADH dehydrogenase activity is annotated by EXP to WbpA (PA3159, G3XD94) from PMID:18621892 (Westman et al. 2008). The full text assays the B. pertussis WbpO(1629) and WbpO(3150) dehydrogenases, which produce NADH from NAD+; WbpA appears only in knockout and complementation experiments. GO:0003954 describes NADH oxidation, the reverse of what these UDP-sugar 6-dehydrogenases do. WbpA's activity is already captured by GO:0047004 from PMID:15226302. Please delete the row. This row seeds PTN000890018; the node term (oxidoreductase activity) still stands on E. coli WecC and on the GO:0047004 seed.

> Capillary electrophoresis was used to characterize the enzymatic activities of purified WbpO(1629) and WbpO(3150)
> — PMID:18621892

## 263. WRONG_TERM (CONFIRMED, NOT_REPORTED)

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

## 264. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HZ76 involved_in GO:0006065 UDP-glucuronate biosynthetic process (EXP, PMID:19282284)
- **Field:** GO_ID
- **Change:** GO:0006065 → GO:0009226 (nucleotide-sugar biosynthetic process)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/wbpE/wbpE-ai-review.yaml`

wbpE (PA3155) is annotated EXP to GO:0006065 UDP-glucuronate biosynthetic process citing PMID:19282284. The abstract states that the WbpE product is UDP-GlcNAc3NA, formed from UDP-3-keto-GlcNAcA; UDP-glucuronate is not an intermediate of the UDP-ManNAc3NAcA pathway. Please re-annotate to GO:0009226 nucleotide-sugar biosynthetic process. The same error was recorded on wbpD (PA3156). This row is not an IBD seed.

> we identified ions that corresponded to the predicted products of WbpB (UDP-3-keto-d-GlcNAcA) and WbpE (UDP-d-GlcNAc3NA) in the coupled enzyme-substrate reaction
> — PMID:19282284

## 265. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:G3XD61 enables GO:0008761 UDP-N-acetylglucosamine 2-epimerase activity (IMP, PMID:10930727)
- **Change:** check GO:0008761 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/wbpI/wbpI-ai-review.yaml`

This IMP row seeds the GO:0008761 IBD at PANTHER:PTN001056041. The cited paper (PMID:10930727) shows that wbpI knockouts lack B-band LPS and itself proposes a di-N-acetylated substrate; the purified enzyme does not use UDP-GlcNAc (PMID:17346239). Please replace GO:0008761: either delete the MF row (the paper is a phenotype study) or use GO:0016857 until a term for EC 5.1.3.23 exists.

> These results imply that the P. aeruginosa UDP-D-GlcNAc precursor may be di-N-acetylated prior to further modification, preventing the E. coli enzymes from recognizing it as a substrate.
> — PMID:10930727

> Neither enzyme utilized UDP-alpha-D-GlcNAc, UDP-alpha-D-GlcNAcA (UDP-2-acetamido-2,3-dideoxy-alpha-D-glucuronic acid) or UDP-alpha-D-GlcNAc3NAc (UDP-2,3-diacetamido-2,3-dideoxy-alpha-D-glucose) as substrates.
> — PMID:17346239

## 266. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:G3XD61 enables GO:0050378 UDP-glucuronate 4-epimerase activity (EXP, PMID:17346239)
- **Change:** check GO:0050378 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/wbpI/wbpI-ai-review.yaml`

GO:0050378 UDP-glucuronate 4-epimerase activity (UDP-glucuronate = UDP-galacturonate) does not describe the activity in PMID:17346239, whose abstract shows a 2-epimerization of UDP-2,3-diacetamido-2,3-dideoxy-alpha-D-glucuronate to the mannuronate (EC 5.1.3.23). Use GO:0016857 until a term for EC 5.1.3.23 exists.

> Data collected from one- and two-dimensional NMR experiments showed that His6-WbpI catalysed the 2-epimerization of UDP-alpha-D-GlcNAc3NAcA, converting it into UDP-alpha-D-ManNAc3NAcA.
> — PMID:17346239

## 267. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:G3XD50 enables GO:0016757 glycosyltransferase activity (IMP, PMID:9680202)
- **Field:** GO_ID
- **Change:** GO:0016757 → GO:0016780 (phosphotransferase activity, for other substituted phosphate groups)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/wbpL/wbpL-ai-review.yaml`

The PseudoCAP IMP row codes WbpL to GO:0016757 glycosyltransferase activity. The abstract of PMID:9680202 shows WbpL is a WecA homologue that adds Fuc2NAc (or GlcNAc or GalNAc) to undecaprenyl phosphate. WecA-family enzymes transfer a sugar-1-phosphate from a UDP-sugar (EC 2.7.8.33 class), which GO places under GO:0016780, not under glycosyl transfer. The term choice probably follows the Pfam family name. PROBABLE, because only the abstract was read. This row is not an IBD seed.

> Cross-complementation experiments using WbpL and its homologue, Escherichia coli WecA, demonstrates that WbpL is bifunctional
> — PMID:9680202

## 268. WRONG_EVIDENCE_CODE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HTB7 involved_in GO:0009243 O antigen biosynthetic process (IDA, PMID:19659934)
- **Field:** Evidence_Code
- **Change:** ECO:0000314 → ECO:0000315 (mutant phenotype evidence used in manual assertion (IMP))
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/wbpW/wbpW-ai-review.yaml`

wbpW (PA5452) involved_in GO:0009243 O antigen biosynthetic process is coded IDA from PMID:19659934 (Byrd et al. 2009, full text read). The A-band data in that paper are immunoblots of in-frame wbpW, pslB and pslB wbpW deletion mutants; there is no direct assay of WbpW in O-antigen synthesis. The evidence code should be IMP. The term itself is correct.

## 269. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HTB7 involved_in GO:0009298 GDP-mannose biosynthetic process (IDA, PMID:9781879)
- **Field:** Evidence_Code
- **Change:** check ECO:0000314 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/wbpW/wbpW-ai-review.yaml`

wbpW (PA5452) involved_in GO:0009298 GDP-mannose biosynthetic process is coded IDA from PMID:9781879 (Rocchetta et al. 1998). The abstract states that the activity was confirmed by complementing E. coli PMI and GMP mutants with wbpW and restoring K30 capsule, and describes no assay of WbpW protein. Heterologous complementation is IGI (or IMP), not IDA. Only the abstract was read, hence PROBABLE and CHECK. The term is correct, and the row is a seed of the PAINT IBD at PTN000283179, which also stands on E. coli ManC.

## 270. WRONG_REFERENCE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HTB9 enables GO:0016757 glycosyltransferase activity (IMP, PMID:9680202)
- **Field:** DB:Reference
- **Change:** check PMID:9680202 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/wbpY/wbpY-ai-review.yaml`

GO:0016757 glycosyltransferase activity for wbpY (PA5448) is annotated IMP to PMID:9680202. The IMP code and the abstract both point to inference from the A-band-negative mutant phenotype and sequence similarity (the abstract calls the transferase assignments probable/predicted); the full text was not read. Direct evidence now exists in PMID:35166992, which shows recombinant WbpY transfers D-Rha from GDP-D-Rha in a1-3 linkage. Please add an IDA row citing PMID:35166992, preferably to GO:0016758 hexosyltransferase activity, and consider retiring the IMP MF row. This row seeds the PAINT IBD at PTN005302544.

> NMR spectroscopic analysis of the WbpY reaction product showed that WbpY transferred one D-Rha residue in α1-3 linkage
> — PMID:35166992

## 271. WRONG_REFERENCE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9HXT9 enables GO:0052621 diguanylate cyclase activity (IMP, PMID:12426335)
- **Field:** DB:Reference
- **Change:** PMID:12426335 → PMID:16186483
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/wspR/wspR-ai-review.yaml`

GO:0052621 IMP on wspR (Q9HXT9) cites D'Argenio et al. 2002 (PMID:12426335). Full text read: wspR insertions suppress the wrinkled colony phenotype of a wspF mutant, but no c-di-GMP or enzyme activity is measured, and the GGDEF domain is discussed only as a probable nucleotide cyclase from other work. Please repoint to Hickman et al. 2005 (PMID:16186483), where purified WspR makes c-di-GMP in vitro (IDA), or delete the row, since an IDA from PMID:16477007 already exists.

> The mechanism by which regulatory proteins with a GGDEF domain exert their effect is not yet clear, but there is growing evidence that the domain encodes a nucleotide cyclase
> — PMID:12426335

## 272. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:G3XD19 located_in GO:0009276 Gram-negative-bacterium-type cell wall (IDA, PMID:9922263)
- **Change:** delete the record asserting GO:0009276
- **Recorded in:** `genes/PSEAE/wzx/wzx-ai-review.yaml`

GO:0009276 Gram-negative-bacterium-type cell wall for wzx (G3XD19, PA3153) is coded IDA to PMID:9922263. The abstract reports LPS phenotypes of wzx insertion mutants and predicts Wzx to be a multi-pass membrane protein; it describes no localisation of Wzx. Topology mapping with PhoA-LacZ and GFP fusions (PMID:20824106) places Wzx in the inner membrane, which GO does not treat as part of the cell wall. Please delete; plasma membrane is already annotated. PROBABLE because the full text of PMID:9922263 was not read.

> Protein orientation in the inner membrane was confirmed via C-terminal fusion to green fluorescent protein.
> — PMID:20824106

## 273. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:G3XD19 located_in GO:0098567 periplasmic side of plasma membrane (IDA, PMID:20824106)
- **Change:** delete the record asserting GO:0098567
- **Recorded in:** `genes/PSEAE/wzx/wzx-ai-review.yaml`

GO:0098567 periplasmic side of plasma membrane for wzx (G3XD19, PA3153) is coded IDA to PMID:20824106. That paper (full text read) maps Wzx as an integral inner-membrane protein with 12 transmembrane segments and loops on both the cytoplasmic and periplasmic sides; it is not a peripheral protein of the periplasmic face. The periplasmic loops do not make the protein a component of the periplasmic side. Please delete the row; GO:0005886 plasma membrane, already annotated, is the correct location. The row also seeds PTN001250140 through its parent, but the IBD stands on the other seeds.

> requiring the integral inner membrane proteins Wzx (O-antigen [O-Ag] flippase), Wzy (O-Ag polymerase), and WaaL (O-Ag ligase)
> — PMID:20824106

## 274. WRONG_EVIDENCE_CODE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:P35818 involved_in GO:0015628 protein secretion by the type II secretion system (IDA, PMID:9818381)
- **Field:** Evidence_Code
- **Change:** ECO:0000314 → ECO:0000304 (TAS (traceable author statement))
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/xcpQ/xcpQ-ai-review.yaml`

GO:0015628 is annotated IDA to PMID:9818381 (Filloux, Michel and Bally 1998, FEMS Microbiol Rev 22:177-198). We read the full text; it is a review, and it reports no original experiment showing that this protein acts in type II secretion. Its only new observations are unpublished or in-preparation notes on Xcp protein structure and interactions (XcpT multimerization, XcpR homomultimers and membrane association, XcpP-XcpQ interaction); the secretion roles it describes are attributed to cited primary papers. The term is correct, so the evidence code should be TAS, or the row re-keyed to a primary paper with IMP. This row is a PAINT IBD seed, so the change should be coordinated with PAINT re-seeding.

## 275. WRONG_EVIDENCE_CODE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q00512 involved_in GO:0015628 protein secretion by the type II secretion system (IDA, PMID:9818381)
- **Field:** Evidence_Code
- **Change:** ECO:0000314 → ECO:0000304 (TAS (traceable author statement))
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/xcpR/xcpR-ai-review.yaml`

GO:0015628 is annotated IDA to PMID:9818381 (Filloux, Michel and Bally 1998, FEMS Microbiol Rev 22:177-198). We read the full text; it is a review, and it reports no original experiment showing that this protein acts in type II secretion. Its only new observations are unpublished or in-preparation notes on Xcp protein structure and interactions (XcpT multimerization, XcpR homomultimers and membrane association, XcpP-XcpQ interaction); the secretion roles it describes are attributed to cited primary papers. The term is correct, so the evidence code should be TAS, or the row re-keyed to a primary paper with IMP. This row is a PAINT IBD seed, so the change should be coordinated with PAINT re-seeding.

## 276. WRONG_EVIDENCE_CODE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q00513 involved_in GO:0015628 protein secretion by the type II secretion system (IDA, PMID:9818381)
- **Field:** Evidence_Code
- **Change:** ECO:0000314 → ECO:0000304 (TAS (traceable author statement))
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/xcpS/xcpS-ai-review.yaml`

GO:0015628 is annotated IDA to PMID:9818381 (Filloux, Michel and Bally 1998, FEMS Microbiol Rev 22:177-198). We read the full text; it is a review, and it reports no original experiment showing that this protein acts in type II secretion. Its only new observations are unpublished or in-preparation notes on Xcp protein structure and interactions (XcpT multimerization, XcpR homomultimers and membrane association, XcpP-XcpQ interaction); the secretion roles it describes are attributed to cited primary papers. The term is correct, so the evidence code should be TAS, or the row re-keyed to a primary paper with IMP. This row is a PAINT IBD seed, so the change should be coordinated with PAINT re-seeding.

> In this review, we will use the P. aeruginosa Xcp system as a basis
> — PMID:9818381

## 277. WRONG_REFERENCE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q00516 part_of GO:0015627 type II protein secretion system complex (IDA, PMID:8331069)
- **Field:** Reference
- **Change:** check PMID:8331069 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/xcpV/xcpV-ai-review.yaml`

GO:0015627 for XcpV (PA3099, Q00516) is annotated IDA to PMID:8331069 (Nunn and Lory 1993). The abstract reports PilD cleavage, N-methylation and inner-membrane fractionation of XcpT-W, which directly support plasma membrane (already annotated EXP from the same paper) rather than membership of the T2SS complex. Complex membership is directly shown by co-purification of the XcpU-V-W-X tip complex (PMID:19828448, Douzi et al. 2009). The term is correct; please check the full text and, if it does not assay complex membership, re-key the row to PMID:19828448. This row is the sole seed of the PAINT IBD at PTN002446181.

> Analysis of cellular fractions from wild-type and pilD mutant strains of P. aeruginosa showed that the precursor forms of XcpT-W are located predominantly in the bacterial inner membrane
> — PMID:8331069

## 278. WRONG_EVIDENCE_CODE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q00516 involved_in GO:0015628 protein secretion by the type II secretion system (IDA, PMID:9818381)
- **Field:** Evidence_Code
- **Change:** ECO:0000314 → ECO:0000304 (TAS (traceable author statement))
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/xcpV/xcpV-ai-review.yaml`

GO:0015628 is annotated IDA to PMID:9818381 (Filloux, Michel and Bally 1998, FEMS Microbiol Rev 22:177-198). We read the full text; it is a review, and it reports no original experiment showing that this protein acts in type II secretion. Its only new observations are unpublished or in-preparation notes on Xcp protein structure and interactions (XcpT multimerization, XcpR homomultimers and membrane association, XcpP-XcpQ interaction); the secretion roles it describes are attributed to cited primary papers. The term is correct, so the evidence code should be TAS, or the row re-keyed to a primary paper with IMP. This row is a PAINT IBD seed, so the change should be coordinated with PAINT re-seeding.

> In this review, we will use the P. aeruginosa Xcp system as a basis
> — PMID:9818381

## 279. WRONG_REFERENCE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q00517 part_of GO:0015627 type II protein secretion system complex (IDA, PMID:8331069)
- **Field:** Reference
- **Change:** check PMID:8331069 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/xcpW/xcpW-ai-review.yaml`

GO:0015627 for XcpW (PA3098, Q00517) is annotated IDA to PMID:8331069 (Nunn and Lory 1993). The abstract reports PilD cleavage, N-methylation and inner-membrane fractionation of XcpT-W, which directly support plasma membrane (already annotated EXP from the same paper) rather than membership of the T2SS complex. Complex membership is directly shown by co-purification of the XcpU-V-W-X tip complex (PMID:19828448, Douzi et al. 2009). The term is correct; please check the full text and, if it does not assay complex membership, re-key the row to PMID:19828448. This row seeds the PAINT IBD at PTN002446812; the IBD conclusion is sound.

> Analysis of cellular fractions from wild-type and pilD mutant strains of P. aeruginosa showed that the precursor forms of XcpT-W are located predominantly in the bacterial inner membrane
> — PMID:8331069

## 280. WRONG_EVIDENCE_CODE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q00517 involved_in GO:0015628 protein secretion by the type II secretion system (IDA, PMID:9818381)
- **Field:** Evidence_Code
- **Change:** ECO:0000314 → ECO:0000304 (TAS (traceable author statement))
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/xcpW/xcpW-ai-review.yaml`

GO:0015628 is annotated IDA to PMID:9818381 (Filloux, Michel and Bally 1998, FEMS Microbiol Rev 22:177-198). We read the full text; it is a review, and it reports no original experiment showing that this protein acts in type II secretion. Its only new observations are unpublished or in-preparation notes on Xcp protein structure and interactions (XcpT multimerization, XcpR homomultimers and membrane association, XcpP-XcpQ interaction); the secretion roles it describes are attributed to cited primary papers. The term is correct, so the evidence code should be TAS, or the row re-keyed to a primary paper with IMP. This row is a PAINT IBD seed, so the change should be coordinated with PAINT re-seeding.

> In this review, we will use the P. aeruginosa Xcp system as a basis
> — PMID:9818381

## 281. WRONG_EVIDENCE_CODE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q00518 involved_in GO:0015628 protein secretion by the type II secretion system (IDA, PMID:9818381)
- **Field:** Evidence_Code
- **Change:** ECO:0000314 → ECO:0000304 (TAS (traceable author statement))
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/xcpX/xcpX-ai-review.yaml`

GO:0015628 is annotated IDA to PMID:9818381 (Filloux, Michel and Bally 1998, FEMS Microbiol Rev 22:177-198). We read the full text; it is a review, and it reports no original experiment showing that this protein acts in type II secretion. Its only new observations are unpublished or in-preparation notes on Xcp protein structure and interactions (XcpT multimerization, XcpR homomultimers and membrane association, XcpP-XcpQ interaction); the secretion roles it describes are attributed to cited primary papers. The term is correct, so the evidence code should be TAS, or the row re-keyed to a primary paper with IMP. This row is a PAINT IBD seed, so the change should be coordinated with PAINT re-seeding.

> In this review, we will use the P. aeruginosa Xcp system as a basis
> — PMID:9818381

## 282. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HT73 involved_in GO:0010043 response to zinc ion (IMP, PMID:24086521)
- **Change:** GO:0010043 → GO:0071578 (zinc ion import across plasma membrane)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/znuC/znuC-ai-review.yaml`

PseudoCAP annotates znuC (PA5500, UniProtKB:Q9HT73) with GO:0010043 response to zinc ion, IMP, from PMID:24086521. The supporting experiment is a growth defect of the znuC deletion in LB + 0.5 mM EDTA. ZnuC is the ATPase subunit of the ZnuABC zinc importer, so the process it takes part in is zinc import across the plasma membrane (GO:0071578); the zinc-sensing "response" in that paper belongs to Zur (Np20, PA5499), which is annotated separately and correctly. This row is the sole seed of the PAINT IBD at PTN001952271, from which 1455 GOA rows now descend, so the term choice propagates widely. The same re-pointing would apply to the paper's companion rows on znuB (Q9HT72) and PA5498 (Q9HT75).

> Putative znuA, znuB, and znuC genes are required for wild-type level growth in low zinc conditions.
> — PMID:24086521
