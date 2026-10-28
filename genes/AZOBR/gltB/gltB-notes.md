# gltB — manual evidence review

2026-10-27

## Target and family

Q05755 is the 1515-residue GltB alpha subunit. UniProt associates the principal genomic source PMID:8428988 with Sp7 and a separate regional sequence source with strain RG. CDD cd02808 (GltS_FMN), InterPro IPR017932 (GATase_2_dom), IPR002932 (Glu_synthdom) and PROSITE PS51278 support the catalytic domain architecture. The exact PANTHER subfamily PTHR11938:SF133 has the official ontology label GLUTAMATE SYNTHASE (NADH). That label is a family name, not evidence that this NADPH-characterized protein prefers NADH. No guessed alternative family is asserted.

Accept the original NADPH GOGAT, ammonia-assimilation cycle and glutamate-biosynthesis rows. Refine donor-generic GOGAT and broad redox terms to NADPH GOGAT as a complex contribution. The direct glutaminase subreaction appears in the core synthesis with target amidotransferase-domain and mechanistic support; no redundant NEW row is added. The physiological direction forms two glutamate molecules even though database reactions may be written in the reverse direction.

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


## 2026-10-28 — PR #5696 review follow-up

The glutamine-hydrolysis and ammonia-channel mechanism remains in the biological description and core-function prose. The machine-readable core now records contribution to GO:0004355 glutamate synthase (NADPH) activity, with the native small chain required for NADPH input, rather than a separate GO:0004359 glutaminase activity. This policy is applied to all four reviewed large chains; the inherited PSEPK standalone proposal is archived, and no new rows are added to fill coverage warnings. Direct E. coli partial-activity evidence (PMID:770440) remains valid and retained.
