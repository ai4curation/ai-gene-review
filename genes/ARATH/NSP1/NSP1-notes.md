# NSP1 (Q9SDM9, At3g16400) curation notes

## Nomenclature warning
- In Burow et al. 2009 and the Wittstock-lab papers, NSP1 is At3g16400 (this gene).
- Kissen & Bones 2009 call At3g16400 "AtNSP3" and use "AtNSP1" for At5g48180 [PMID:19224919 "Assays with crude bacterial extracts containing AtNSP1 ( At5g48180 ) or AtNSP3 ( At3g16400 ) recombinant proteins also resulted in the production of 2-phenylacetonitrile"].
- In PMID:30395611, "AtNSP3" is At3g16390, a tandem paralog [PMID:30395611 "The expression construct for AtNSP3 (At3g16390)"]. Its iron data therefore do not apply directly to NSP1.
- Kong et al. 2012 (PMID:22954730, cached, abstract-only) uses the Kissen numbering, so its "AtNSP1" is probably At5g48180. It is not used as evidence here.
- Also named JAL28 (jacalin-related lectin 28).

## Function
- The nsp1 T-DNA mutant (SALK_072600) lacks constitutive and herbivore-induced leaf nitrile formation [PMID:18987211 "a line with a T-DNA insertion in the second exon of At3g16400 (SALK_072600) produced no or only trace amounts of simple nitriles of the endogenous glucosinolates in rosette leaf homogenates"].
- Purified NSP1 forms simple nitriles only [PMID:18987211 "AtNSP1 did not promote thiocyanate or epithionitrile formation from any of the tested substrates."].
- In vitro, its activity did not depend on added iron [PMID:18987211 "Thus, simple nitrile formation by AtNSP1 is not dependent on the presence of Fe 2+ or Fe 3+ ion."]. UniProt still lists an Fe(2+) cofactor (by similarity or from other studies), so no iron binding NEW was proposed.
- Organ roles [PMID:27990154 "simple nitrile formation upon tissue disruption depended almost entirely on NSP2 in seeds and mainly on NSP1 in seedlings"].
- Structure: monomer with an N-terminal JAL domain [PMID:30900313 "NSP1 from A. thaliana (AtNSP1) (which is a monomer)"; PMID:30395611 "In addition, AtNSP1 possesses an N-terminal JAL domain"; PMID:28479247 crystal structure].
- Seeds and germination [PMID:31850033 "The time course of total glucosinolate content during ten days of germination depended on functional NSP1."]. The cache is abstract-only, and the phenotype is metabolic, so the seed germination and dormancy rows are UNDECIDED.

## Decisions
- Specifier activity: MODIFY enzyme regulator activity (IBA) to GO:0016846 carbon-sulfur lyase activity, consistent with ESP and TFP. Proposed new term: nitrile-forming thiohydroximate-O-sulfate sulfolyase activity (EC 4.8.1.5).
- Lectin domain: carbohydrate binding (IEA) is KEEP_AS_NON_CORE, because glycan binding is untested [PMID:19224919 "the role of these domains in AtESP and homologous proteins is not yet known"].
- Nucleus (IBA) is MARK_AS_OVER_ANNOTATED. It is seeded only by ESP's WRKY53-dependent nuclear import [PMID:17369373 "ESR is exclusively in the cytoplasm in W53-KO cells"].
- mRNA binding (HDA) is UNDECIDED, because the paper is abstract-only.
- Response to herbivore (IMP) is KEEP_AS_NON_CORE. NSP1 is required for the P. rapae-induced nitrile shift, but no protective effect has been shown.
- No falcon deep-research file was available when this review was written.

## 2026-10-15 journal: UNDECIDED rows resolved (PR #5026 follow-up)

Supersedes the "seed germination and dormancy rows are UNDECIDED" and "mRNA binding (HDA) is UNDECIDED" lines above.

- PMID:31850033 full text is now cached (`full_text_extraction_method: xml`). It contains no germination-rate, radicle-emergence or dormancy assay for nsp1-1; the phenotype is seed glucosinolate content over germination [PMID:31850033 "In contrast to Col-0 and tgg1 tgg2, germinating seeds of nsp1-1 did not contain higher total glucosinolate levels on day 4 relative to days 0 and 10 (Figure 7C)."]. The authors themselves call for more experiments to establish a direct NSP role in turnover. All seed germination rows (IEP, IMP, IEA) and the seed dormancy row are now MARK_AS_OVER_ANNOTATED; the metabolic phenotype is captured by the glucosinolate catabolic process IMP.
- GO:0003729 mRNA binding (HDA, PMID:27729395 poly(A) interactome capture) is MARK_AS_OVER_ANNOTATED, matching the treatment of the same screen for PHYA. No NSP1-specific RNA-binding validation exists. Full-text access on 2026-10-15: `fetch-pmid PMID:27729395 --force` found PMC5134986 but the publisher restricts the XML, and the HTML and PDF fallbacks returned no usable content; the cache remains abstract-only, so NSP1's confidence tier in the screen was not checked.


## Module-member evidence audit — 2026-10-25

Reviewed every original row (18) and core function using review/annotation-reviewer instructions, current cached primary publications and the existing research. Preserved all source annotation fields and all pre-existing proposed rows. Reused the existing genuine Falcon provider report and its artifacts. These plant targets do not require bacterial FEBA retrieval.

Use locus identifiers to separate alternate nomenclature: target At3g16400 can be calledAtNSP3 in earlier Kissen nomenclature, but30395611 explicitly usesAtNSP3 At3g16390 for iron quantification/mutants. Do not transfer that direct assay to this target.18987211 directly tests target nitrile formation;27990154 distinguishes seedNSP2, seedlingNSP1 and rootNSP1+NSP3.31850033 measures glucosinolate content during germination, not a demonstrated direct germination/dormancy mechanism. Retained those over-annotation decisions. mRNA-capture HDA is unresolved rather than rejected because no knownRNA role was expected.

Broad and substrate-specific terms were assessed consistently across evidence codes. No NEW rows were added. Previously proposed rows were evaluated for direct participation rather than filled from pathway adjacency. Experimental cohort calls whose protein-level data were not verified were left UNDECIDED; full-text availability alone was not treated as proof of a target-specific assay. Original sources and provider reports were not hand-edited.

### Final cross-row QA, 2026-10-26

Kept location claims consistent with retained experimental compartments: a supported apoplast assignment refines a general extracellular prediction, while a main cytosolic or vacuolar location does not by itself disprove a secondary predicted pool. Conditional Arabidopsis ESP activity is distinguished from a universal coding knockout. Original annotation fields remain unchanged.


## 2026-10-26 — PR #5550 source-level correction

Revisited review findings 1–3 against the actual publication cache and the primary sources. Removed generic source-unresolved boilerplate where the assay design is adjudicable. Restored relevant verbatim biochemical and localization evidence; did not restore label-only CHAIN features, unrelated introductory statements, or quotations that no longer support the revised claim. Existing source annotation fields were preserved.

PMID:27729395 normal force-fetch still gives abstract only; PMC direct full-text retrieval is challenged. The abstract explicitly allows enzymes as RNA-binding candidates. Target confidence-set membership/enrichment remains unresolved, so UNDECIDED is retained with this specific limitation; no claim that the biological activity is implausible.
