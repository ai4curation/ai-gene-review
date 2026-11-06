# GlxA evidence and identity audit

## Identity and constructs

P0DYA0 is the reviewed645-residue GlxA/SLI_3188 record from Streptomyces lividans1326/66, taxon1200984 (STRL6). The current record was integrated into Swiss-Prot on2026-11-04 and has no fetched GOA rows. The older GenBankEOY47901.1 model has627 residues and is flagged ALT_INIT in UniProt. It must not be equated by length to the assayed model.

The current645-residue sequence exactly matches translation of the extended1326 genomic intervalCM001889.1:3309615..3311552. Its N-terminal sequence matches the actual FigureS2 construct diagram in [PMID:38557137](https://pmc.ncbi.nlm.nih.gov/articles/PMC11022532/). TableS1 primers3188-F/R and full-length GlxA-BlaM-F match the same genomic locus. The reproducible identity script/report is under STRLI/cslA source-analysis and checks both proteins. The2024 activity assay uses PelB-GlxA(12–645), with an engineered Met-Gly linker, coexpressed with tagged1326 CslA in E. coli. Full-length and N-terminal GlxA-BlaM fusions support the topology. Neither E. coli expression nor an identical TK24 CslA sequence changes the GlxA source strain.

## Biochemistry and native biology

[PMID:26205496](https://pubmed.ncbi.nlm.nih.gov/26205496/) establishes a membrane-associated mononuclear copper-radical oxidase, with a Tyr289–Cys121 cross-link and Cu coordination. The native glxA deletion loses hyphal-tip glycan deposition and changes aerial development/pellet morphology. Those perturbations do not themselves identify a chemical substrate or justify annotation to every affected developmental process.

The primary2015 manuscript's activity section reports low-efficiency oxidation with glycolaldehyde (Km115mM,kcat0.14s−1) and much weaker activity with glucose, galactose and glycerol. No detectable activity was reported with glyoxal, glucuronic acid, lactose or cellobiose in those assays. It is inappropriate to call GlxA a canonical galactose oxidase or glyoxal oxidase. The actual physiological donor and oxidation product remain unknown. The partial EC1.2.3.- label is insufficient to decide an aldehyde-specific reaction. The review therefore uses oxidoreductase activity at the supported general level and retains the precise model-substrate assay limits in prose.

[PMID:26740586](https://pmc.ncbi.nlm.nih.gov/articles/PMC4736821/) directly demonstrates glycolaldehyde-dependent peroxide production through the GlxA/DtpA coupled assay and analyzes GlxA maturation. [PMID:28093470](https://pubmed.ncbi.nlm.nih.gov/28093470/) connects Trp288 to Cu loading, redox-cofactor maturation and restoration of native morphology. These support an evolved redox role while leaving its native substrate unresolved; they do not make glycolaldehyde metabolism the core physiological specialization.

[PMID:38557137](https://pmc.ncbi.nlm.nih.gov/articles/PMC11022532/) establishes a physical GlxA–CslA complex that produces cellulose in vitro. GlxA truncations affect complex formation/activity. Thus GlxA contributes to the demonstrated synthase activity; it is not merely a substrate consumed by another protein, and it does not itself supply the glycosyltransferase active site. The qualifier is `contributes_to`, not `enables`. The authors explicitly leave native glycan composition and a possible direct c-di-GMP-binding site unresolved. No c-di-GMP binding or native cellulose-specific BP is asserted.

## NEW assertions and comparator checks

All four rows are distinctly NEW because the original record has zero rows: plasma membrane, oxidoreductase activity, copper-ion binding, and contribution to cellulose synthase (UDP-forming) activity. Each has independent primary experimental support. Term ancestry was checked: membrane is not duplicated beside plasma membrane; the binding, redox and contributed synthase claims are not ancestor/descendant duplicates. Copper binding records an experimentally resolved cofactor interaction, not copper transport/homeostasis.

Same-role live QuickGO checks of E. coliBcsB P37652 and RhodobacterBcsB Q3J126 found no contributed cellulose-synthase MF row. This absence is not evidence that curators missed GlxA. The proposal is supported independently by direct GlxA complex reconstitution and truncation assays, and its qualifier distinguishes the catalytic carrier CslA from the partner. No target GO-CAM was found. No bare protein-binding annotation was added.

## Sources, access and reproducibility

Normal fetching seeded the zero-row review and frozen raw files before edits; the baseline is `.cache/module-audit-logs/cellulose-20261105/streptomyces-baseline.json`. Default Falcon research failedHTTP403; its log is preserved, with no manually fabricated provider output.

The2024 and2016 papers are normally cached in full. The2015/2017 normal caches are abstract-only, but official accepted manuscripts were retrieved from the University of Essex repository and retained with hashes. PDF font encodings corrupt ordinary pdftotext output, which was rejected; the source PDFs remain unmodified. Selected source pages were separately rendered and OCRed with clearly named derived files. The source2015 structural page8 and assay page10 were visually inspected, as were the2024 supplementary construct figure and a2017 structural page. OCR is an aid and is not used for verbatim supporting quotations. Exact quotes in the review come from normally cached publications or curated UniProt experimental statements.

The primary2024 Sarcina study [PMID:38750617](https://pubmed.ncbi.nlm.nih.gov/38750617/) demonstrates mixed-linkage glucan synthases and is a specificity counterexample, not a cellulose exemplar. The clostridial study [PMID:33264329](https://pmc.ncbi.nlm.nih.gov/articles/PMC7710045/) directly characterizes CcsZ hydrolase but predicts CcsA synthase activity; it does not establish another directly assayed cellulose polymerase.
