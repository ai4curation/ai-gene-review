# gmhB notes

## 2026-10-02 ADP-heptose module review

GmhB is the HAD-family phosphatase step between the two HldE reactions in E. coli ADP-heptose synthesis. Kneidinger et al. showed that purified E. coli GmhB converts the beta heptose 1,7-bisphosphate intermediate to beta heptose 1-phosphate and that deleting gmhB produces an altered LPS core [PMID:11751812].

The exact `GO:0034200` activity is well supported by several later biochemical and structural studies. Wang et al. showed that E. coli GmhB has a narrow substrate range, high catalytic efficiency for beta-HBP, and selective C-7 phosphate removal by NMR [PMID:20050615]. The same work found that E. coli GmhB prefers the beta anomer over the alpha anomer by about 100:1 while retaining measurable alpha-HBP phosphatase activity, explaining why McCallum et al. could use E. coli GmhB as an alpha-HBP phosphatase substitute in a Campylobacter GDP-heptose reconstitution [PMID:31449400]. Nguyen et al. solved Mg/substrate-bound and apo E. coli GmhB structures and established the structural Zn-binding loop as a substrate-recognition feature rather than the catalytic metal site [PMID:20050614]. The abstract-only structural paper cited in GOA/UniProt also supports Mg and Zn binding [PMID:20050699].

Review decisions:

- Accept all exact `GO:0034200` rows and both specific pathway rows.
- Mark the broad IBA `GO:0009103 lipopolysaccharide biosynthetic process` row as over-annotated because the more precise `GO:0009244 lipopolysaccharide core region biosynthetic process` row already exists.
- Keep Mg/Zn binding and cytosol/cytoplasm as real but non-core.
- Mark generic carbohydrate metabolism and phosphatase activity as over-annotated.

## 2026-10-25 — complete annotation and evidence audit

Applied the review and annotation-reviewer instructions to every seeded row. Source fields were preserved and a JSON comparison checked that only annotation review blocks changed. Correct broad terms were refined with MODIFY, not treated as false or excessive claims. No new process annotations were added.

Research provenance: the actual `just deep-research-falcon ECOLI hldE --fallback perplexity-lite` run was launched concurrently with publication caching. Falcon/Edison returned HTTP 403 authentication failure; the Perplexity fallback returned HTTP 401 insufficient_quota. This session-wide provider outage applies to this four-gene audit; these notes are manual primary-source research, not a provider-generated report. Existing and additional publication caches were fetched with supported commands; no publication cache was hand-edited.

`just fetch-fitness ECOLI gmhB` was attempted and failed because no local FEBA data or reachable data source was available; no fitness artifact was written. PSEAE additionally lacks an organism mapping in the fetcher. No fitness phenotype is inferred from that failure.

All 19 existing rows reviewed. The beta-heptose 1,7-bisphosphate 7-phosphatase activity and LPS-core/ADP-L,D-heptose synthesis are retained. General phosphatase, carbohydrate metabolism, LPS biosynthesis and cytoplasm terms are refined to supported specific descendants; cytosol, Mg binding and Zn binding are accepted as core location/cofactor features. This supersedes the older notes recommending MARK_AS_OVER_ANNOTATED for valid broad terms.

PMID11751812 full text directly reconstructs E. coli GmhB chemistry and shows the gmhB deletion's altered LPS core. PMID20050615 full text uses biochemical kinetics and NMR: C7 phosphate is removed while the C1 phosphate remains. Exact quote: “E. coli GmhB prefers the β-anomer over the α-anomer by a factor of 100 : 1”. The preference concerns catalytic efficiency and is not absolute exclusivity.

PMID20050614 full text establishes distinct Mg-catalytic and Zn-structural/substrate-recognition sites. The Zn loop is not conserved in every family member, so the target result should not be generalized indiscriminately. Exact quote: “Ala replacement of any one of the four Zn2+ ligands of E. coli GmhB is detrimental.” PMID20050699 is abstract-only in the cache; its detailed metal annotations are corroborated by PMID20050614 and the curated record. The apparent P63288 accession typo in PMID20050614 is not evidence of a different experimental protein.

PMID31449400 is a critical title-versus-full-text example. The article is by **Huddleston and Raushel**, not McCallum as incorrectly stated in the older note. It explicitly says: “GmhB from E. coli was used as a substitute for Cj1152 in large-scale reactions. The gene for GmhB (Uniprot ID: P63228) was amplified from the genomic DNA of E. coli K12”. Thus E. coli GmhB really was assayed; the Campylobacter title is no reason to remove the experimental row. Here the enzyme serves a preparative GDP-alpha-heptose pathway through its weaker alpha-HBP activity, not a demonstrated native E. coli GDP-heptose pathway. The exact beta activity is independently established.

PMID16990279 is an abstract-only E. coli HAD-family screen; its focus on other substrates/proteins does not contradict GmhB evidence. Cytosolic localization retains the existing curator assignment from PMID18304323, with the cohort-versus-target quote limitation recorded.
