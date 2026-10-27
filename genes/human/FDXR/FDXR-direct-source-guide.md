# FDXR direct evidence

The [decision table](FDXR-direct-decisions.yaml) preserves each imported source key and its zero-based intake index. The [MitoCoP target table](FDXR-mitocop-records.yaml) retains exact original workbook cells and distinguishes protein groups. The reviewed claims concern reductase activity, mitochondrial location, steroid and ubiquinone synthesis, and broad metabolic context. No new annotation or publication quotation is added.

## Electron supply and ubiquinone synthesis

[PMID:38425362](https://doi.org/10.1038/s41929-023-01087-z), Results **C5 transformation requires a ferredoxin couple**, the COQ6 C1-hydroxylation Results, and Extended Data Figure 3 establish electron transfer through FDXR and FDX2 to COQ6. Reduction/reoxidation, NADPH turnover, competition with cytochrome c, and analytical detection of hydroxylated products support catalytic participation. FDXR supplies electrons; COQ6 performs the hydroxylation chemistry.

The assayed proteins were reconstructed tetrapod ancestors. Short-chain CoQ intermediates made the pathway experimentally tractable. The human gene-level reductase and ubiquinone annotations are retained on conserved enzyme function and curator judgment, with this boundary explicit. They are not described as direct assays of extant human FDXR or any of its seven splice forms. Functional coupling does not itself establish permanent membership of FDXR in a human metabolon.

## Human sequence and steroid pathway evidence

The complete original [PMID:2845396](https://pmc.ncbi.nlm.nih.gov/articles/PMC282132/) was read as all five official scanned pages, 7104–7108. Page 7104 describes mitochondrial electron transfer from NADPH through adrenodoxin reductase and adrenodoxin to P450scc. The original experiments identify human cDNAs, the six-codon alternative splice segment, a single chromosomal locus and RNA expression. Page 7108 explicitly leaves the functional consequences of the splice difference unresolved. The paper does not measure activity for the seven currently recorded products.

[PMID:1863359](https://pubmed.ncbi.nlm.nih.gov/1863359/) is a human regional gene-mapping study. Its verified abstract describes the same steroidogenic electron-transfer chain, but the full publisher text remained inaccessible. The steroid-biosynthesis TAS claim is retained with the matching independently read pathway statement in the 1988 original. FDXR does biochemical work by providing reducing equivalents; it does not itself cleave cholesterol or perform the P450 hydroxylation reactions.

The broad generation-of-precursor-metabolites-and-energy annotation is retained as non-core metabolic context. It is not evidence that FDXR is an ATP-producing enzyme or respiratory-chain structural subunit. Verified GO ancestry does not make the steroid or ubiquinone synthesis terms strict descendants of that broad term, so those annotations alone do not justify a redundancy-based TOO_GENERAL action.

## Mitochondrial location

[PMID:29040572](https://doi.org/10.1093/hmg/ddx377), Results accompanying Figure 2C–D and confocal-immunofluorescence Methods, directly supports endogenous FDXR overlap with MitoTracker in human fibroblasts. The authors also report nuclear and cytoplasmic signal. The annotation records positive mitochondrial presence, not exclusive localization. The paragraph's matrix statement cites earlier work rather than deriving it from confocal resolution.

The [2018 corrigendum, PMID:29554255](https://academic.oup.com/hmg/article/27/12/2224/4938783), corrects the Figure 1 genotype labels for Families 7, 8 and 10. Its actual indexed publisher body was read despite a separate failed HTTP download. No change to Figure 2 localization or retraction is stated. The original normal cache remains unchanged.

[PMID:34800366](https://doi.org/10.1016/j.cmet.2021.11.001), original Tables S1 and S2, names FDXR/P22570. Table S1 sheet B row 343 marks mitochondrial-proteome membership; the study also incorporates prior literature/database knowledge. Table S2 sheet G row 3234 provides the P22570-containing protein group's mitochondrial enrichment across HEK, HeLa, Huh7 and U2OS cells. Additional FDXR-labelled rows are retained separately. These data support the organelle annotation without resolving all natural splice forms or a submitochondrial compartment. Functional classification columns are not treated as direct pathway assays.

## Preservation and access

All imported annotation fields, inherited reference identities/findings and seven splice-product objects remain intact. Whole reference assessments distinguish original text read outside an abstract-only cache from genuinely unavailable text. Provider failures and unavailable family data remain documented in the protected intake; no provider report or phylogenetic evidence has been fabricated. The database evidence lane is documented separately.

## Additional steroidogenesis context

[PMID:38885337](https://doi.org/10.1172/jci.insight.179071), Results and Figure 2, measures steroid output in three patient-derived adrenal-like lines versus one sex-matched control. Cortisone substitutes for cortisol below the quantification limit; GAPDH-transcript normalization addresses differing cell growth. Figure 4 and its Results show lower corticosterone in male mutant mice with largely preserved adrenal organization. These data corroborate steroid-pathway impairment. They do not constitute purified assays of each CYP reaction, establish all effects as direct, or resolve functions of the seven natural splice products. The proposed redox contribution remains distinct from measured steroid output.

## 2026-10-26 feedback: source representation and ontology

The [exact published GO-CAM snapshot](https://github.com/ai4curation/ai-gene-review/blob/8c9a6b52825c93cc0c61d2c27464c5ac5ebb8bcf/gocams/675b862c00001470/675b862c00001470-src.yaml) contains FDXR activity `gomodel:675b862c00001470/675b862c00001526`: enabled by human P22570, ferredoxin-NADP+ reductase activity, mitochondrial location, and `part_of` ubiquinone biosynthesis. Its `RO:0002629` edge targets FDX2 activity `.../675b862c00001519`, whose electron-transfer activity precedes COQ6. The model's activity/process/electron-transfer evidence cites PMID:38425362; mitochondrial location cites PMID:29040572. This is corroborating curation of the same evidence, not a new human experiment. The accepted gene-level ubiquinone role and direct core participation follow the measured electron supply. The imported upstream qualifier remains unchanged and is not treated as a full statement of that participation.

The two PMID:38425362 IDA records carry a **PROBABLE / CHECK** source-defect request for UniProt to assess ancestral-protein evidence coding. Actual Results, **C5 transformation requires a ferredoxin couple**, Methods, **Ancestral sequence reconstruction**, **FDXR–FDX2 kinetics** and **FDXR–FDX2–COQ6 kinetics**, and Extended Data Figure 3 identify the reconstructed proteins and assays. The direct measurements are real; their transfer to extant human P22570 needs explicit source representation. No corrected ISS code is established, no source code is rewritten, and no report has been sent upstream.

The saved official [QuickGO typed ancestor query](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0006744/ancestors?relations=is_a,part_of) lists GO:0044281, GO:0008150, GO:0042180, GO:0044283, GO:0042181, GO:0008152, GO:1901661, GO:1901663, GO:0009058, GO:0006743, GO:0006744 and GO:0009987. Neither GO:0006091 nor GO:0006733 is present. The same captured response for steroid biosynthesis lacks GO:0006091. These are the actual `is_a,part_of` results used for the non-core broad-metabolism decision, not an assumed biochemical ontology path; a future ontology release may differ.
