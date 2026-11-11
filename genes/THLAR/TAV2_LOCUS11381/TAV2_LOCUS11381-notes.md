# TAV2_LOCUS11381: SUR1-like carbon-sulfur lyase

## Identity and inference

UniProtKB A0AAU9RX80, field pennycress (Thlaspi arvense), has native ORF name TAV2_LOCUS11381; the Arabidopsis-like alias is an inferred functional descriptor, not a newly asserted official symbol. TAV2_LOCUS11381 encodes a predicted SUR1-like, pyridoxal-phosphate-dependent carbon-sulfur lyase in field pennycress. It is inferred to generate thiohydroximate intermediates in glucosinolate biosynthesis. The protein retains a class-I aminotransferase-like fold, but its close SUR1 relationship supports specialized lyase chemistry rather than a tyrosine-catabolic assignment. The available 473-residue sequence is flagged as an N-terminal fragment, despite nearly complete coverage of Arabidopsis SUR1; native activity and completeness of the gene model remain unverified.

The existing [phmmer analysis](../../../projects/THLAR_OILSEED/ortholog_mapping/RESULTS.md) was inspected alongside the newly fetched target UniProt record. This is independent sequence evidence, not a GOA annotation used as support. A reciprocal best hit is not by itself a phylogenetic proof of strict one-to-one orthology. No accession matched gocams/index.tsv.

## Primary source assessment

- [PMID:14871316](https://pubmed.ncbi.nlm.nih.gov/14871316/): The accessible Arabidopsis SUR1 abstract combines glucosinolate-deficient mutants, accumulated physiological precursor and recombinant C-S lyase assay with djenkolic acid. It is not a purified assay of the native pennycress model or every physiological substrate.

## Annotation decisions

- GO:0004838 L-tyrosine:2-oxoglutarate transaminase activity: MARK_AS_OVER_ANNOTATED. The target has a SUR1-specific subfamily assignment and nearly full-length reciprocal SUR1 match. Primary Arabidopsis evidence establishes specialized C-S lyase chemistry. PANTHER family-level tyrosine-aminotransferase propagation does not establish that substrate reaction in this specialized, fragment-flagged target; no native negative assay is claimed.
- GO:0005829 cytosol: UNDECIDED. The PANTHER-derived cytosol annotation is plausible for a SUR1-like protein, but the target has an N-terminal fragment flag and no independent localization or intact targeting analysis. The accessible original SUR1 biochemical abstract does not establish this target compartment; retain uncertainty rather than use an electronic location as its own support.
- GO:0006520 amino acid metabolic process: MODIFY. Although the lyase acts on a cysteine-derived conjugate, its specific inferred biological role is formation of the glucosinolate core. The SUR1-specific target mapping and primary source enzyme/genetic data support a lateral process correction to GO:0019761, not a claim that this term descends from amino acid metabolism.
- GO:0006572 L-tyrosine catabolic process: MARK_AS_OVER_ANNOTATED. This electronic claim follows the same broad tyrosine-aminotransferase family placement as GO:0004838. Specific SUR1 homology instead supports C-S lyase participation in glucosinolate formation. A physiological tyrosine-catabolic role is over-propagated; this judgment does not assert that every possible tyrosine side reaction has been experimentally excluded.
- GO:0008483 transaminase activity: MODIFY. The shared PLP-dependent fold does not establish transamination as the physiological chemistry. Target SUR1 subfamily membership and reciprocal alignment support the experimentally characterized homolog lyase. Replace the broad fold-derived activity laterally with GO:0080108; the near-complete target sequence remains flagged as a fragment.
- GO:0030170 pyridoxal phosphate binding: ACCEPT. The target contains a PIRSR-supported PLP-linked lysine, and Arabidopsis SUR1 is a PLP-dependent C-S lyase. This conserved catalytic-site inference remains defensible despite the terminal fragment flag; exact native occupancy is not claimed.

QuickGO is_a/part_of ancestry and exact reaction definitions were checked live on 2026-10-26. GO:0034722 is a descendant of both GO:0016787 and GO:0140096, despite its small-peptide substrates. GO:0010326 is the unelongated methionine reaction; GO:0003862 is the 3-isopropylmalate reaction. Exact elongated-substrate activities are not silently equated to those terms. No NEW biological-process annotation was added; existing process refinements are identified as descendants or lateral corrections in their reasons.

## Research provenance

Applied review, annotation-reviewer and core-function synthesis guidance. Normal fetch-gene seeded original rows; these fields are preserved. Default Falcon deep research and publication caching were launched concurrently. Falcon failed authentication (403) and automatic Perplexity-lite fallback failed with insufficient_quota (401); log /tmp/thlar-TAV2_LOCUS11381-deep.log. No provider report was fabricated. Manual source assessment and existing reproducible sequence analysis were used. Fitness retrieval is not applicable to this plant target. Target-specific publication searches did not establish a native assay for this exact accession; this is a literature-access conclusion, not proof that none exists.
