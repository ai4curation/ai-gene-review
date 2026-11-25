# CG34171 / SPH244 review notes

## Finding and exact target

**ProtNLM's GO:0004252 serine-type endopeptidase prediction is contradicted for X2JEK1.** The selected 176-residue product lacks the C-terminal part of the S1 domain carrying the catalytic serine. This is distinct from the longer CG34171 protein's serine-equivalent **F222 substitution**. Both are incompatible with the canonical S1 catalytic mechanism; they are not the same residue-level defect.

[FlyBase FBgn0085200](https://flybase.org/reports/FBgn0085200) maps CG34171-PC / FBpp0310560 / NP_001286041 / AHN54555 to X2JEK1 (176 residues), and CG34171-PB / FBpp0293603 / NP_001097175 / ABV53692 to A8DZ15 (292 residues). The record explicitly lists two unique polypeptides and notes “Alternative translation stop created by use of multiphasic reading frames within coding region.” The current short isoform is therefore a documented native gene model, not a sequence truncation introduced by this review. This does not prove the predicted polypeptide is stably expressed, nor identify the sequence actually supplied to the historical ProtNLM run.

The original cohort record and prediction response are preserved as `CG34171-uniprot-source.json` and `CG34171-predictions-source.json`, extracted without alteration from the frozen fly-benchmark JSONL files. Raw FlyBase HTML and a BeautifulSoup text extraction are retained. The exact target UniProt record and all reference records were retrieved on 2026-09-08.

## Catalytic evidence

The [reproducible sequence analysis](CG34171-bioinformatics/RESULTS.md) uses MAFFT v7.526 with localpair and globalpair iterative modes, plus Biopython 1.85 for residue mapping. Reference active-site positions are parsed from UniProt, not recalled from memory. Independent active bovine trypsin P00760 and the first S1 domain of toad OVCH2 Q66TN7 agree on the H/D/S alignment. Q66TN7's second S1 domain serves as a contrasting sequence control: its histidine-equivalent position is asparagine.

Both CG34171 isoforms preserve H72/D124. The long isoform has F222 in the aligned serine position, while X2JEK1 has no aligned sequence there. Full-sequence comparison establishes an identical 167-residue prefix; the short form then has a distinct 9-residue tail. Including this entire tail in the alignment does not supply the missing catalytic region. This is stronger evidence than the SPH244 name, a generic PROSITE caution, or a family-level peptidase annotation.

The intrinsic-activity prediction is **NPI, confidence score 0**. The optional `error_type` is omitted: the closest schema enum, `PSEUDOENZYME_OVERANNOTATION`, describes fold-retaining pseudoenzymes, while retention of a complete fold has not been demonstrated for this short product. The locus is a useful pseudoenzyme-related case, but its selected isoform specifically illustrates failure to check domain completeness. `WRONG_INPUT_SEQUENCE` is not justified because the predictor's actual input is not known.

## Primary literature and annotation provenance

The target GOA already contains a **NOT GO:0004252 IKR** annotation to [Cao and Jiang, 2018, PMID:30367934](https://pubmed.ncbi.nlm.nih.gov/30367934/), DOI [10.1016/j.ibmb.2018.10.006](https://doi.org/10.1016/j.ibmb.2018.10.006). The cached [full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC6358214/) explains SP/SPH classification “based on the presence or absence of the His-Asp-Ser catalytic triad.” This is a sequence-based inference, not a negative enzyme assay. The main review **ACCEPTs the negation**, preserving `negated: true` and its original evidence code/reference.

Table S1 is described as containing the exact SPH sequences and properties, but its XLSX download returned a browser challenge and the manuscript's supplementary files were unavailable through the attempted EuropePMC route. Its SPH244 row and historical sequence were **not inspected**. The gene-specific IKR assertion is visible in the current GOA and FlyBase records; the particular contemporary molecular defect is independently established by the local alignment. The paper's general discussion of SPH cofactors does not establish that CG34171-PC has such a role.

The other seeded annotation, **IEA GO:0006508 proteolysis** from InterPro IPR001254, is **UNDECIDED**. Loss of intrinsic activity invalidates a direct enzyme inference but does not rule out noncatalytic participation in proteolysis. The short product's target-specific participation is not established. QuickGO definitions for both terms were retrieved and frozen as JSON; the molecular-function term expressly requires a serine nucleophile, whereas the biological-process term describes peptide-bond hydrolysis.

FlyBase also displays a gene-level IBA innate-immune-response assertion. This is a phylogenetic assertion, not mere donor-count evidence, but it was not seeded on the exact target accession. Its ancestral placement and relevance to the shortened PC protein were not independently examined. No new immune-process or protease-inhibitor annotation is proposed, and `core_functions` is left empty because the short product's positive molecular function is unresolved.

## Prediction donor and ancillary fields

The original GO prediction records model score **0.99**, phmmer donor **Q66TN7** and phmmer score **65.4**. [Q66TN7](https://www.uniprot.org/uniprotkb/Q66TN7/entry) is a 980-residue toad ovochymase/oviductin with two S1 domains, one bearing the complete catalytic-site annotation. No alignment coordinates accompany the model metadata, so the particular matched domain cannot be inferred. The reviewed donor's function also includes curator-assessed homology transfer; its database status is not direct experimental proof of the target's activity.

The response's “Peptidase S1 domain-containing protein” name is a defensible domain description rather than an enzymatic claim. Its “Secreted” location is consistent with the target's N-terminal hydrophobic signal and SignalP call at residues 1–16; this remains a sequence-based localization inference, not target-specific extracellular detection. These ancillary observations are separate from the GO activity assessment.

## Provider research assessment

[The Falcon/Edison report](CG34171-deep-research-falcon.md) completed in 348.65 seconds on 2026-09-08, with a retained markdown artifact. It usefully warns against confusing SPH244 with the independently studied cSPH242 and does not invent a target-specific enzyme assay. However, it relies heavily on the supplied **ARBA-derived CLIP-subfamily description** and does not resolve the exact isoforms or the existing Cao/Jiang IKR evidence. That CLIP claim is not adopted: the target has no annotated clip domain, and its sequence before the S1-domain start lacks the cysteine pattern expected of an N-terminal clip domain. S1-family membership is supported; a conventional CLIP architecture is not established.

The report leaves catalysis uncertain because it did not inspect the active-site residues. The independent sequence analysis supplies the missing discriminator and supports NPI for the intrinsic activity. Its general immune-cofactor discussion cannot supply the missing positive molecular function of X2JEK1. No report prose is used as biological validation; the preserved report records the provider's synthesis and its limitations.

## Validation

All two seeded GOA rows are reviewed, including the explicit NOT flag. Main validation passes with two advisories: no defined positive core function and no annotation-support citation to the provider report. Both are deliberate: the positive function is unresolved, and the provider contributes no independent decisive evidence. Schema status is DRAFT under the repository's warning convention. The ProtNLM sidecar validates with zero errors and warnings, one title and two supporting quotes verified. No GO term or source label was rewritten. No new biological-process or molecular-function claim is introduced merely to fill a field.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

No ProtNLM2 output was opened or used for this re-review. The sources were the GOA rows, the UniProt X2JEK1 and A8DZ15 records, the frozen FlyBase report, PMID:30367934 (full text cached), the PTHR24256 PAINT table and family review, the cached PANTHER 19.0 fly classification, and the existing local catalytic-site analysis (`CG34171-bioinformatics/RESULTS.md`, unchanged).

**Identity (benchmark accession is an alternative product, not the canonical one).** X2JEK1 is CG34171-PC, 176 aa. It is the product of an alternative translation stop (FlyBase: "Alternative translation stop created by use of multiphasic reading frames within coding region."). It shares residues 1-167 with the 292-aa CG34171-PB product A8DZ15 and then has a distinct 9-residue tail. Its S1 domain call is 38..161, compared with 38..265 in A8DZ15. This means X2JEK1 holds only the N-terminal half of the trypsin fold: H72 and D124 are present, but the C-terminal barrel with the catalytic-serine region is absent. A8DZ15 has a complete domain with F222 at the serine position. Both entries are unreviewed TrEMBL records. A8DZ15 is the gene's representative product: it carries the KEGG, eggNOG and PaxDb cross-references and the gene-level IBA row.

**Annotation decisions.**
- NOT GO:0004252 (IKR, PMID:30367934): ACCEPT. The decision rests on the triad-based SP/SPH classification, the FlyBase "S1A non-peptidase homologs" gene group, the local alignment, and the PAINT NOT-IKR nodes in PTHR24256.
- GO:0006508 proteolysis (IEA, InterPro IPR001254): changed from UNDECIDED to MARK_AS_OVER_ANNOTATED. The InterPro2GO mapping assumes catalysis, and that assumption fails for this product. FlyBase also records NOT peptidase activity by key residues for the gene. PAINT propagated proteolysis only from catalytic node PTN001207268, while the gene's IBA is innate immune response from PTN000667087. We read the missing IBA proteolysis row as a deliberate decision. The row was not removed, because a noncatalytic cofactor role in a cascade has not been ruled out.
- No NEW terms were added. The gene-level IBA innate immune response (PTN000667087) sits on A8DZ15, not X2JEK1. Whether the half-domain PC product takes part in immunity is unknown, so it is not transferred. `core_functions` is left empty because there is no supported positive molecular function.

**Evolutionary placement and family review.** PANTHER assignments disagree:
- X2JEK1 (UniProt/InterPro): PTHR24256 (TRYPTASE-RELATED), with no subfamily.
- A8DZ15 (UniProt cross-reference): PTHR24276:SF96 (POLYSERASE-RELATED / PEPTIDASE S1 DOMAIN-CONTAINING PROTEIN).
- A8DZ15 (cached PANTHER 19.0 fly classification): PTHR24260:SF136 (GH08193P-RELATED).

The FlyBase IBA comes from PTN000667087, a PTHR24256 node, which means PAINT treats the locus as part of PTHR24256. The PTHR24256 family review (`interpro/panther/PTHR24256/PTHR24256-review.yaml`) lists X2JEK1 under "Benchmark members without resolved subfamily placement" and scopes GO:0004252 as UNRESOLVED. That fits this review's gene-specific NOT. DIOPT lists no ortholog with a score above 1/14, so no characterised ortholog exists to transfer function from.

**Relative to review next.** The canonical same-gene product A8DZ15 (CG34171-PB) has no review in the repository (`genes/DROME/CG34171` is keyed to X2JEK1). Its folder would be `genes/DROME/CG34171__A8DZ15`.

**Modules.** No module under `modules/` refers to CG34171, PTHR24256 or PTHR24276.
