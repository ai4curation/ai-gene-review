# AZOVI algX: comparative alginate acetylation review

## Target identity

Accession O52194 is a reviewed Azotobacter vinelandii species-level record (taxon 354) whose original genomic sequence is from ATCC 9046 and is linked to PMID:10352233. It is not silently relabeled as a DJ genome assay. The four normal fetch-gene operations seed 11 rows in total; all original annotation fields are preserved.

## Primary evidence and limits

- [PMID:10352233](https://pubmed.ncbi.nlm.nih.gov/10352233/): Original ATCC 9046 native sequencing identifies the algX/L/V/I/F region; the nonpolar algF mutant demonstrates loss of alginate acetylation. It does not provide purified enzyme assays for AlgI, AlgV or AlgX.
- [PMID:40821665](https://pubmed.ncbi.nlm.nih.gov/40821665/): Azotobacter-focused review supports nomenclature and system context, but several acetylation/localization citations concern Pseudomonas. Its direct acetyl-CoA transport wording and depiction of all four proteins as enzymes are not accepted as target-specific mechanistic proof.
- [PMID:35401471](https://pubmed.ncbi.nlm.nih.gov/35401471/): Review of native regulation and pathway architecture; the four-component acetylation model partly rests on Pseudomonas literature. Used for comparative context, not as direct native enzymology.
- [PMID:35756034](https://pubmed.ncbi.nlm.nih.gov/35756034/): Publisher correction page inspected: Figure 1A changes the precursor enzyme labels to GDP-mannose pyrophosphorylase AlgA and GDP-mannose dehydrogenase AlgD. It does not alter these acetylation-component identities. Local cache is bibliographic/abstract only.
- [PMID:40171682](https://pubmed.ncbi.nlm.nih.gov/40171682/): Mechanistic review explicitly identifies the complete AlgI/AlgJ/AlgF/AlgX transfer pathway as an incompletely demonstrated model. It supports caution about donor identity and the AlgJ-to-AlgX handoff; it is not an Azotobacter target assay.
- [PMID:25165982](https://pubmed.ncbi.nlm.nih.gov/25165982/): Comparative Pseudomonas AlgJ/AlgX structure and assays distinguish a putative intermediate acetylation role from AlgX polymer binding and direct polymer acetylation with a surrogate donor. No native Azotobacter assay or residue numbering is inferred.
- [PMID:23779107](https://pubmed.ncbi.nlm.nih.gov/23779107/): Pseudomonas aeruginosa AlgX structure and mutagenesis support the SGNH/CBM architecture and role in acetylation. Target-specific family/domain membership supports qualified transfer, not native structural measurements.

The strongest native acetylation experiment is the nonpolar algF mutant AJ34: “As expected, AJ34 produced unacetylated alginate” (PMID:10352233). It establishes the target system and AlgF contribution, not purified activity for every component. Pseudomonas protein assays inform homolog-based roles but are not Azotobacter assays. No direct acetyl-CoA transport, exact donor preference, complete relay order or target residue coordinates are asserted. The review uses subunit contribution for roles whose intrinsic target activity is unresolved; AlgF is not assigned an acetyltransferase enzyme activity.

## GO decisions and research provenance

GO:0051979 is not an is_a/part_of descendant of GO:0042121 in live QuickGO (checked 2026-10-25). For AlgI/V/F the process change is an explicitly lateral correction from broad polymer production to polymer modification; AlgF already has the precise experimentally supported term. AlgX retains biosynthesis because its homolog-supported role also includes nascent polymer protection/export. No new process row is manufactured to populate a pathway. The GO-CAM index has no match for O52196, O52197, P70799 or O52194.

Applied review, annotation-reviewer and core-function synthesis guidance. Default Falcon plus automatic Perplexity-lite fallback were attempted concurrently with publication caching; both research providers failed (log /tmp/azovi-algX-deep.log). The wrapper did not expose a detailed provider cause, so none is invented. No provider report was fabricated. Fitness retrieval was attempted and failed without a reachable FEBA source (/tmp/azovi-algX-fitness.log); this is missing data, not a negative fitness phenotype. Manual primary research and source-specific assessments provide the review.

## Family grounding

IPR034655 — Alginate biosynthesis protein AlgX, N-terminal; IPR031798 — Alginate biosynthesis protein AlgX, C-terminal carbohydrate-binding module; IPR031811 — AlgX/AlgJ, SGNH hydrolase-like domain. No target PANTHER cross-reference is present. Names verified through official InterPro API/PANTHER ontology and actual target UniProt membership. No PTN or subfamily id is guessed.


## Intrinsic activity versus complex contribution follow-up

Reassessed the molecular-function relation: homology-based evidence does not make an inferred enzyme activity a `contributes_to` activity. O52194 has the specific AlgX family and SGNH/CBM architecture, together with curated “Probably has acetyltransferase activity in vivo (By similarity).” Pa AlgX Q51372 directly catalyzes polymer O-acetylation in PMID:25165982 using a surrogate donor. Together these support intrinsic GO:0016413 with explicit ISS inference; no target divergence evidence was identified. Added one NEW MF row, retaining both original rows, and changed the core to molecular_function. No native donor, kinetics or residue mapping is asserted. Live QuickGO confirms GO:0016413 means transfer of an acetyl group to an oxygen atom and is a descendant of GO:0016407; neither overlaps the two seeded BP/CC terms. Comparator queries for Q51372/Q88ND0/O52194 returned no existing GO:0016413 rows, so annotation frequency is not used as evidence. The inference instead rests on the experimental chemistry and target family architecture. There is no cached target GO-CAM. No NEW process annotation was added. This supersedes the earlier note that unresolved target activity was represented as subunit contribution.

## Deep research availability, 2026-11-02

No provider deep-research report exists for this gene. During the alginate O-acetylation module audit, `just deep-research-falcon PSEAE algI` was retried and failed with "403 Failed to authenticate"; earlier Falcon and Perplexity attempts for the KT2440 homologs also failed (see genes/PSEPK/algI/algI-notes.md). No deep-research file was written by hand. The review instead rests on cached primary publications, the UniProt record and the existing annotation reviews.
