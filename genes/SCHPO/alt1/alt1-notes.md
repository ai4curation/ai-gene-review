# alt1 (SPBC582.08, UniProt Q10334) notes

Putative alanine aminotransferase (EC 2.6.1.2). No S. pombe experimental data in GOA or UniProt; everything is by similarity to S. cerevisiae Alt1 (P52893).

- [UniProt:Q10334 "Reaction=L-alanine + 2-oxoglutarate = pyruvate + L-glutamate;"]; [UniProt:Q10334 "FUNCTION: Alanine aminotransferase involved in both alanine"] (ECO:0000250 P52893).
- Location: [UniProt:Q10334 "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}. Mitochondrion"] — cytoplasm is a curator inference, mitochondrion by similarity.
- Sequence observation: alt1 is 490 aa [UniProt:Q10334 "SEQUENCE   490 AA;"] and begins [UniProt:Q10334 "MSDLDGFCQN AFSDLNSLNQ QVFKANYAVR GALAILADEI"] — acidic (D3, D5, D14), only K24/R30 basic in the first 30 residues, no annotated transit peptide. S. cerevisiae Alt1 is 592 aa with [file:yeast/ALT1/ALT1-uniprot.txt "TRANSIT         1..64"]. So alt1 lacks the N-terminal extension that targets budding-yeast Alt1 to mitochondria; it resembles cytosolic ALTs in length. (Simple visual inspection; no targeting predictor run.)
- S. cerevisiae: [PMID:19396236 "under respiratory conditions, Alt1p constitutes the sole pathway for alanine biosynthesis and catabolism"]; paralog Alt2 inert [PMID:23049841 "only Alt1 displays alanine aminotransferase activity; in contrast ALT2 encodes a catalytically inert protein"]. S. pombe has a single ALT (PTHR11751:SF29).

## GO-CAM / module disagreement
- PomBase GO-CAM gomodel:67c10cc400000148 places both alt1 activities (alanine biosynthesis, alanine catabolism) in the **mitochondrial matrix** (IC). Module text also says "S. pombe alt1 enables GO:0004021 in the mitochondrial matrix". Given the missing transit peptide, I marked the mitochondrion/matrix rows UNDECIDED and accepted cytoplasm (UniProt curator inference) as best-available; core function gives no location.
- S. cerevisiae ALT1 review core location = mitochondrial matrix; differs here deliberately.
- GOA also has L-glutamate biosynthetic process IC (glutamate GO-CAM) -> non-core.


## 2026-10-26 comparative annotation audit

Reviewed all 12 existing rows and the core-function synthesis for SCHPO/alt1; no rows were added or dropped. Original GO terms, evidence codes, source identifiers and all other machine fields are preserved. Actions: {'ACCEPT': 8, 'MODIFY': 3, 'KEEP_AS_NON_CORE': 1}.

The UniProt/PomBase localization assignments are retained as curated orthology-based inference. The previous review treated a shorter N-terminus and missing transit-peptide annotation as evidence against mitochondrial import; neither establishes targeting loss. The characterized S. cerevisiae Alt1 donor and conserved family support the inference, while native S. pombe import/localization experiments remain an open question. The matrix row is ACCEPT with explicit inference provenance, and both broader mitochondrion rows MODIFY to that supported matrix term. The broad cytoplasmic assignment is retained without claiming exclusive cytosolic residence or using sequence length as localization evidence. No native localization assay is claimed.

The core is conserved reversible PLP-dependent alanine transamination; alanine synthesis and catabolism are inferred from the characterized donor. PMID:19396236 provides condition-specific native donor physiology, and PMID:23049841 distinguishes active Alt1 from inactive Alt2 rather than showing that all ALT-family proteins are uncertain. General transaminase activity refines to the supported MF; integral PLP binding is core. Future endogenous tagging, mitochondrial import and mutant flux assays would independently test the assignments.

### Research access and provenance

An actual per-gene Falcon attempt with Perplexity-lite fallback ran in parallel with normal publication caching. Falcon returned HTTP 403 authentication failure; Perplexity returned HTTP 401 insufficient quota. No provider report was fabricated. Manual evidence review is recorded here; research and publication logs are `.cache/module-audit-logs/aspartate-SCHPO-alt1-research.log` and `aspartate-SCHPO-alt1-publications.log`. Normal publication fetching succeeded. Cached abstracts are used only for explicit reported findings; unverified target-specific experiments are not confidently rejected.

The annotation-reviewer workflow and current bare-protein-binding policy were applied. No GOA file is used as evidence. Existing sound source quotations were preserved, new quotations were checked against cached source text, and UniProt record sections were backfilled by the helper. Gene summaries are standalone biology. Histories use the helper with explicit Codex actor/tool; focused strict/term/source validation and HTML rendering are logged under `.cache/module-audit-logs/aspartate-SCHPO-alt1-*`. Final results and machine-payload proof are in the panel validation/payload manifests.


## Root-organelle policy correction (2026-10-25)

Reassessed all 2 mitochondrion (GO:0005739) rows against their original source scope and independent localization evidence. Changed MODIFY to ACCEPT: CLAUDE.md and projects/ORGANELLES.md explicitly retain a supported root organelle rather than replacing it with a subcompartment. The row-specific reasons distinguish direct localization/proteomics from similarity or phylogenetic inference and preserve source-resolution limits. Existing matrix rows, core locations and other annotations are unchanged; no NEW row was added. This supersedes the earlier matrix-replacement decisions, not their historical records. No inferred granularity failure is retained for a biologically sound IBA.


## PR #5568 follow-up, 2026-10-26

Repaired authored citation spacing and fused numeric prose while preserving original annotation payloads, every action, raw UniProt/GOA records and all existing supporting quotations. Source-cited passages in notes were protected from rewriting.
