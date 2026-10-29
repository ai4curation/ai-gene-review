# AZOVI algF: comparative alginate acetylation review

## Target identity

Accession P70799 is a reviewed Azotobacter vinelandii species-level record (taxon 354) whose original genomic sequence is from ATCC 9046 and is linked to PMID:10352233. It is not silently relabeled as a DJ genome assay. The four normal fetch-gene operations seed 11 rows in total; all original annotation fields are preserved.

## Primary evidence and limits

- [PMID:10352233](https://pubmed.ncbi.nlm.nih.gov/10352233/): Original ATCC 9046 native sequencing identifies the algX/L/V/I/F region; the nonpolar algF mutant demonstrates loss of alginate acetylation. It does not provide purified enzyme assays for AlgI, AlgV or AlgX.
- [PMID:40821665](https://pubmed.ncbi.nlm.nih.gov/40821665/): Azotobacter-focused review supports nomenclature and system context, but several acetylation/localization citations concern Pseudomonas. Its direct acetyl-CoA transport wording and depiction of all four proteins as enzymes are not accepted as target-specific mechanistic proof.
- [PMID:35401471](https://pubmed.ncbi.nlm.nih.gov/35401471/): Review of native regulation and pathway architecture; the four-component acetylation model partly rests on Pseudomonas literature. Used for comparative context, not as direct native enzymology.
- [PMID:35756034](https://pubmed.ncbi.nlm.nih.gov/35756034/): Publisher correction page inspected: Figure 1A changes the precursor enzyme labels to GDP-mannose pyrophosphorylase AlgA and GDP-mannose dehydrogenase AlgD. It does not alter these acetylation-component identities. Local cache is bibliographic/abstract only.
- [PMID:40171682](https://pubmed.ncbi.nlm.nih.gov/40171682/): Mechanistic review explicitly identifies the complete AlgI/AlgJ/AlgF/AlgX transfer pathway as an incompletely demonstrated model. It supports caution about donor identity and the AlgJ-to-AlgX handoff; it is not an Azotobacter target assay.
- [PMID:12003941](https://pubmed.ncbi.nlm.nih.gov/12003941/): Primary Pseudomonas aeruginosa FRD1 deletion/complementation and localization work. Used as homolog evidence only; no Pseudomonas helix count, signal processing or membrane fractionation result is relabeled as an Azotobacter experiment.
- [PMID:37797696](https://pubmed.ncbi.nlm.nih.gov/37797696/): Direct Pseudomonas interaction and negative acetylesterase assays support the AlgF-family noncatalytic adaptor model. Exact native Azotobacter partners and interaction affinities remain untested.

The strongest native acetylation experiment is the nonpolar algF mutant AJ34: “As expected, AJ34 produced unacetylated alginate” (PMID:10352233). It establishes the target system and AlgF contribution, not purified activity for every component. Pseudomonas protein assays inform homolog-based roles but are not Azotobacter assays. No direct acetyl-CoA transport, exact donor preference, complete relay order or target residue coordinates are asserted. The review uses subunit contribution for roles whose intrinsic target activity is unresolved; AlgF is not assigned an acetyltransferase enzyme activity.

## GO decisions and research provenance

GO:0051979 is not an is_a/part_of descendant of GO:0042121 in live QuickGO (checked 2026-10-25). For AlgI/V/F the process change is an explicitly lateral correction from broad polymer production to polymer modification; AlgF already has the precise experimentally supported term. AlgX retains biosynthesis because its homolog-supported role also includes nascent polymer protection/export. No new process row is manufactured to populate a pathway. The GO-CAM index has no match for O52196, O52197, P70799 or O52194.

Applied review, annotation-reviewer and core-function synthesis guidance. Default Falcon plus automatic Perplexity-lite fallback were attempted concurrently with publication caching; both research providers failed (log /tmp/azovi-algF-deep.log). The wrapper did not expose a detailed provider cause, so none is invented. No provider report was fabricated. Fitness retrieval was attempted and failed without a reachable FEBA source (/tmp/azovi-algF-fitness.log); this is missing data, not a negative fitness phenotype. Manual primary research and source-specific assessments provide the review.

## Family grounding

IPR035422 — Alginate O-acetyl transferase AlgF (family name does not prove intrinsic catalytic activity). No target PANTHER cross-reference is present. Names verified through official InterPro API/PANTHER ontology and actual target UniProt membership. No PTN or subfamily id is guessed.

## Independent final QA, 2026-10-25

Removed contributes_to acetyltransferase activity from the core. Native algF genetics establish participation in acetylation; homolog interaction data support a noncatalytic organizational model. Neither demonstrates an enzymatic activity distributed across a complex that requires AlgF for catalysis. Retained the directly supported process/location core and all original annotation rows; no intrinsic adaptor activity is substituted because simultaneous bridging also remains hypothetical. Removed an AlgV-specific membrane-side sentence copied into the AlgF localization rationale.

## PR 5546 follow-up, 2026-10-25

Clarified the lateral GO:0042121 to GO:0051979 decision against the Pseudomonas comparator. PMID:31900562 explicitly reports a PDO300 algF production defect and effects on polymerization/secretion-complex stability; native ATCC 9046 AJ34 instead directly establishes production of unacetylated alginate (PMID:10352233). Those additional PDO300 phenotypes are not transferred as an established native Azotobacter biosynthetic role. No action changed. The 31900562 cache contains abstract/repository metadata despite full_text_html labeling, so the new assessment explicitly limits source access to the abstract.
