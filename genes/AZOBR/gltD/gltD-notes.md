# gltD — manual evidence review

2026-10-27

## Target and family

Q05756 is the 482-residue GltD beta subunit. Its UniProt record combines Sp7 genomic-sequence provenance (PMID:8428988) with Sp6 partial-protein sequencing (reference [4] in the immutable UniProt record; the underlying article was not recovered); the latter is not used to claim all experiments used Sp7. A later sequence revision is part of the raw record and is retained. NCBIfam TIGR01318, InterPro IPR006006 (GltD-like), IPR023753 (FAD/NAD-binding_dom) and IPR009051 (Helical_ferredxn) independently ground the electron-transfer architecture. Exact PANTHER PTHR42783:SF3 is named GLUTAMATE SYNTHASE [NADPH] SMALL CHAIN-RELATED in the committed ontology.

Accept NADPH GOGAT as a component contribution, [4Fe-4S] binding and glutamate biosynthesis. Refine generic iron–sulfur binding to the [4Fe-4S] term already present. Refine oxidoreductase activity to both the direct NAD(P)H-donor activity and the already-present complex GOGAT activity. GO:0016651 is a donor-class term, not an assertion of equal measured NADH turnover. The direct NADPH/FAD relay and the complete complex reaction are separate levels of function. No NEW process or complex annotation is manufactured; supported complex membership is represented in the core.

## Evidence scope and acquisition

The repository keys these records to AZOBR, NCBITaxon:192 (Azospirillum brasilense), a species-level record rather than a strain-specific taxon. Do not change the inherited accession/taxon or silently equate Sp6, Sp7, RG and a recombinant expression host. No raw UniProt or GOA file was edited.

The actual provider, publication and fitness acquisition attempts are recorded under `.cache/module-audit-logs/ammonia-acquisition/AZOBR-<gene>-*.log`: provider returned 1, publication fetching returned 0, fitness returned 1. No provider output or fitness measurement is invented. This notes document is the manual research record; it is not labeled as provider-generated deep research.

Normal PMID fetching recovered abstract-only records. Full PMC routes for PMID:2887545/PMC213731 and PMID:4019412/PMC219181 did not recover article text; URL retries returned a reCAPTCHA page and were rejected as evidence. The PMID:8428988 JBC PDF and PMID:10785395 Wiley full-text routes returned HTTP403. The author repository for PMID:31473159 states that no files are associated with the record; it repeats the abstract, not a full manuscript. These failed or abstract-only URL caches are not evidence references. Positive findings below are restricted to explicit accessible statements and curated target domain/function data. No experimental annotation is removed on an inaccessible-full-text argument.

## Shared mechanism and source limits

- [PMID:8428988](https://pubmed.ncbi.nlm.nih.gov/8428988/), “Two open reading frames of 4548 and 1446 base pairs (bp) were identified within the fragment as the structural genes for the alpha and beta subunits (gltB and gltD, respectively) of A. brasilense GltS.” This establishes gene/subunit identity; its sequence-based cofactor assignments were tentative.
- [PMID:10785395](https://pubmed.ncbi.nlm.nih.gov/10785395/), “one FMN (at Site 2, the 2-oxoglutarate/L-glutamate site in the alpha subunit)” and “one FAD (at Site 1, the pyridine nucleotide site within the beta subunit)”. Recombinant enzyme expressed in E. coli BL21(DE3) matched native A. brasilense enzyme in the properties listed in the abstract. Alpha carries one [3Fe-4S] center. The paper explicitly left the two [4Fe-4S] locations unresolved; it is not evidence for their subunit localization.
- [PMID:31473159](https://pubmed.ncbi.nlm.nih.gov/31473159/), “allows unequivocal location of the FAD cofactor and of two electron transfer [4Fe-4S]+1,+2 clusters within βGltS.” This later structural result resolves the earlier uncertainty. The abstract names A. brasilense, not a particular strain. Target UniProt records link to PDB6S6S/6S6T/6S6U/6S6X.
- [PMID:18421771](https://pubmed.ncbi.nlm.nih.gov/18421771/) is a mechanistic review: an Ntn-amidotransferase and FMN synthase center are coupled through an ammonia tunnel, while the other module supplies FAD-dependent NAD(P)H oxidation. It discusses several GOGAT implementations; donor-specific conclusions here use primary A. brasilense biochemistry.
- [PMID:4019412](https://pubmed.ncbi.nlm.nih.gov/4019412/), “Growth conditions for Azospirillum brasilense Sp6 were devised for maximal expression of glutamate synthase.” Its native kinetic parameters are Sp6 data, not automatically P10583/Q05755/Q05756 Sp7 measurements. Older stoichiometry is not substituted for later structural allocation.
- [PMID:2887545](https://pubmed.ncbi.nlm.nih.gov/2887545/) reports native isotope-tracer and GS/GOGAT inhibitor evidence for ammonium assimilation under nitrogen excess and limitation. Its accessible abstract does not identify the strain. Enzyme-activity or tracer changes are physiological support; they do not make these enzymes transcriptional regulators or establish a new subcellular location.

The primary source allocation corrects historical raw UniProt prose that suggests 2-oxoglutarate binds the small subunit, lists FAD under GltB, or assigns only one [4Fe-4S] center to GltD. The immutable downloaded records are retained; the review reasons and scientific synthesis state the supported allocation. A future upstream UniProt correction is suggested, not claimed to have been submitted.

## Annotation policy and validation

All original machine annotation fields, ordering and 19 total rows across the three genes are preserved. Only review metadata is changed. Ordinary relationship strings are inert. Whole-complex NADPH GOGAT annotations are accepted as subunit contributions; core functions use `contributes_to_molecular_function` to make that role explicit. Direct GltB glutaminase and GltD NADPH oxidation are distinguished in the core synthesis without manufacturing redundant NEW rows. Correct broad terms are refined using supported descendants. No new process term is proposed, no experimental claim is removed, and no inherited precomposed involved-in term requires decomposition. No source GOA file is used as biological support.

Focused validation includes schema/terms/best practices, literal supporting quotes, record-section derivation, notes PMID checks, HTML render and helper-created history validation. Exact paths and immutable-row/raw-hash proof are in `.cache/module-audit-logs/ammonia-azobr-review/`.
