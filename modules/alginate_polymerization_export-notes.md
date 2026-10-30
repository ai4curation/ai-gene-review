# Alginate polymerization and export: literature and taxon audit

## 2026-10-25

Scope: bacterial Alg8/Alg44-dependent mannuronan polymerization, periplasmic handling, optional compositional epimerization, escaped-polymer degradation and outer-membrane export. AlgX contributes to polymer handling independently of its acetyltransferase chemistry, which remains in the adjacent acetylation module. Polymer precursor production, transcriptional regulation and extracellular Azotobacter AlgE1–7 epimerases are adjacent biology.

Literature searches used “alginate polymerization export Alg8 Alg44 AlgK AlgE review 2024 2025” and “AlgL periplasm homeostasis alginate 2022 review secretion AlgX AlgK”, followed by targeted PubMed and primary-paper searches. Most recent generic alginate reviews concern materials/extraction rather than this mechanism and were not used to establish protein roles. Relevant comparative reviews include PMID:24034361 (2013 bacterial production), PMID:37884397 (2023 Pseudomonas exopolysaccharides), and PMID:40821665 (2025 Azotobacter). Their older mechanistic conclusions must be checked against subsequent primary data.

PMID:36494359 establishes a KT2440 AlgKX structure and direct polymer binding, with P. aeruginosa native interface-mutant secretion/attachment measurements. The prior module knowledge gap excluded AlgX from the export machinery; that exclusion must be revisited against the direct evidence for a polymer-handling function distinct from catalytic acetyl transfer. AlgG similarly has separable catalytic and structural roles; marking the whole protein optional conflates dispensable epimerization with possible conduit support.

PMID:34990713 defines P. aeruginosa AlgL as a periplasmic homeostasis enzyme, with genetic-background-dependent viability effects and AlgU/T-associated compensation. AlgL is not an obligatory polymerase subunit. Native Azotobacter nonpolar algL phenotypes (PMID:12664154) require separate interpretation.

A new primary study (PMID:42766672; DOI:10.1371/journal.pbio.3003985, September 2026) identifies isolated P. aeruginosa AlgK and AlgX as MucD substrates and finds assembled AlgKX comparatively protected. This is external proteolytic regulation, not evidence that AlgK/AlgX perform proteolysis. Keep MucD outside the polymerization/export core.

The representative panel is being verified across KT2440, P. aeruginosa and A. vinelandii. Azotobacter accession/strain assignments must follow original source records: the outer-membrane protein called AlgJ historically (Q44497, now canonical algE) is neither the AlgV acetylation relay nor an extracellular AlgE1–7 epimerase. No universal species/strain presence is implied.

Independent QA: IPR053440 matches the KT2440 and Pa AlgK proteins but not P94202 in the current InterPro member endpoint; the Azotobacter protein remains a verified AlgK homolog with broader IPR050767 Sel1/AlgK classification. The common selector therefore retains its three representatives but omits a falsely shared exact family ID. AlgL clearance is explicitly Pa-direct versus homolog-inferred for the other systems; native Azotobacter data establish lyase chemistry and molecular-mass control. PMID:9358065 is cited as mutant genetics without claiming an unverified complementation experiment.

Required AlgG protection is scoped to the native P. aeruginosa node context and its directly characterized representative. Azotobacter structural necessity remains an explicit biological gap. PMID:16855245 (PMC1540039) disrupts extracellular-epimerase export eexDEF while retaining algG; near-pure mannuronan in those mutants is not a test of algG-null export and does not demonstrate whole-protein dispensability.

## 2026-10-26 executable scope of AlgG protection

The broad template now makes the AlgG protection part optional while visibly retaining its experimentally established requirement in P. aeruginosa. The compiler does not interpret context.taxa as a conditional requirement; leaving the part globally required would incorrectly transfer Pa evidence across the template. No Azotobacter dispensability is inferred. A species-specific required implementation would need an explicit instantiation; this audit does not modify module logic.


## PR #5552 follow-up, 2026-10-26

Verified live GO definitions for AlgG GO:0016857 and AlgE GO:0015159; both broad activities fit the demonstrated/inferred mechanisms. Unified gene representations with explicit direct-versus-ISS boundaries and no NEW process rows. Added RHEA:45572 to the AlgG function evidence, matching the existing notes claim. Retained the omitted Alg8 family ID after inspecting actual SF12 assignments: UniProt P0C0H0 HasA (hyaluronan chemistry), P04340/P26024 NodC, and the three Alg8 representatives all carry PTHR22913:SF12. This is diversity within SF12, not only its parent. Official UniProt REST source: https://rest.uniprot.org/uniprotkb/search?query=xref%3Apanther-PTHR22913%20AND%20reviewed%3Atrue&format=json&size=500 ; audited response retained locally in .cache/module-audit-logs/pr5552-panther-query1.json. The module names these counterexamples and retains the specific functional constraint. No AlgX dependency content was edited.

## 2026-10-26 — catalytic evidence and scoped polymer recognition

The Alg8 GO:0047643 function now cites the actual radiolabeled GDP-mannuronate incorporation assay in FRD1 envelope fractions (PMID:16391057) and active-site mutagenesis in P. aeruginosa (PMID:18524915). The fraction assay is not purified Alg8 kinetics, and two substitutions also affected stability. The existing interaction quote is retained at the assembly-evidence level. The polymer-production edge to AlgG now has a catalytic anchor without claiming a reconstituted protein-to-protein handoff.

Specific binding evidence was checked against the member reviews: PMID:36494359 directly assays KT2440 AlgK and AlgX separately, and PMID:25165982 assays Pa AlgX. GO:0030247 is reviewed for those proteins, but not for Pa/Azotobacter AlgK or a separate Azotobacter AlgX binding role. The shared three-taxon scaffold/handling annotons therefore retain their existing function scope, with explicit source-specific binding evidence rather than a new universal MF assertion. AlgX acetyl-transfer chemistry remains in the neighboring acetylation module. The module graph, required/optional roles and all representative identities are unchanged.

The two PSEPK ISS comparator omissions are documented in the gene review provenance without changing machine payload fields. PSEPK algG now cites PMID:8144447 directly in review support while retaining its historical original-reference field. The existing Alg8 additional-reference bookkeeping is internally consistent because its actual supporting citations and top-level references are present; no cosmetic edit is required. The GO:0085029 cross-species actions retain their previously reviewed source-specific matrix/physiology distinctions; no contrary evidence was found in this bounded follow-up.
