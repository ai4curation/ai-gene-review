# acrVIA1 evidence audit

## 2026-10-25

Identity: A0A6P3CWF5, bacterial tax1640, PDB 6VRB chain C contains 229 residues and lists no mutations (https://www.rcsb.org/structure/6VRB). The primary paper PMID:32467331 identifies phiLS46 gp2 and calls the protein 232 aa. This discrepancy is recorded rather than silently equating all constructs; it does not invalidate the direct deposited structure-to-accession link. The inhibitor contacts the guide-exposed surface and prevents target engagement/activation, rather than acting as a nuclease itself. Deletion, complementation and natural-host infection give native biological evidence; single-virion escape is a result of this experimental system, not a general rule for all type VI-A infections. The UniProt bacterial taxon is preserved, and the phage origin is described explicitly.

Normal accession-specific fetch-gene produced the source caches and seeded review. Falcon deep research with perplexity-lite fallback failed; see `.cache/module-audit-logs/anti-crispr-deep-LISSE-acrVIA1.log`. This is manual primary-literature research, not a provider-generated research file. Publications were fetched through the normal fetch-pmids workflow and full texts inspected where available. No source cache was hand-edited.

The inhibitor itself performs the interference-blocking step, so the process assignment is based on biochemical participation, not solely deletion/rescue necessity. GO:0098672 is already used for experimentally characterized inhibitors in the same role (AcrIIC1, AcrIIA4, AcrIF2); no redundant parent process is proposed. Conservatively proposed only the essential inhibitor molecular function and, where absent, this specific process. Generic binding and inferred cellular locations are not added as separate NEW rows.


## PR5555 follow-up: canonical sources and evidence scope (2026-10-25)

Moved the CURATION-only 229-versus-232-residue sequence-description discrepancy out of knowledge_gaps into suggested_questions and these notes. PDB 6VRB chain C maps the 229-aa molecular inhibitor to A0A6P3CWF5; the paper describes native gp2 as 232 aa. Comparing genome translation, construct and deposited sequence can resolve this provenance issue without a new wet-lab experiment. The exact native-construct equivalence remains unasserted; both annotation decisions and their caveats are unchanged.
