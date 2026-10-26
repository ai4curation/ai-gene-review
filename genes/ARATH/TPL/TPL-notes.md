# TOPLESS / TPL (At1g15750; Q94AI7) curation notes

## 2026-10 review (auxin_nuclear_signaling module; TPL also used by jasmonate module)

- Deep research (falcon) failed (HTTP 402); review based on cached literature.
- Identity: UniProt Q94AI7 TPL_ARATH (WSIP1). Correct.

### Function
- tpl-1 transforms the shoot pole into a root pole; TPL resembles transcriptional corepressors [PMID:16763149].
- TPL binds IAA12/BDL domain I and is required for BDL repression; "TPL is a transcriptional co-repressor" [PMID:18258861].
- NINJA connects TPL to JAZ repressors; TPL negative regulator of JA responses; TPL general co-repressor via adaptors [PMID:20360743].
- TPL interactome: "TPL/TPR corepressors predominantly interact directly with specific transcription factors"; RD (EAR) sequences essential for recruitment [PMID:22065421].
- TPD binds EAR motifs; tetramer [PMID:26601214]; tetramerization and repressor binding interdependent [PMID:28698367].
- CRA helix 8 binds MED21/MED10; required for repression [PMID:34075876].
- HDA19 in repressor complex with TPL/MIF2/KNU [PMID:29298836].

### Decisions
- ~100 protein-binding IPIs: DNA-binding TF partners -> GO:0140297; Aux/IAAs -> GO:0001222; adaptors (NINJA/AFPs/JAZ/KIX9/miP1a/TWA1) -> GO:0001221; HDA19 -> GO:0042826; MED21/MED10 -> GO:0036033; uncharacterized/chromatin proteins without functional link -> REMOVE.
- Cytoplasm ISM -> MARK_AS_OVER_ANNOTATED.
- Core: GO:0003714 transcription corepressor activity in nucleus.


## 2026-10-26 native auxin-system evidence audit

All seeded annotation payloads were preserved, including term IDs, evidence types, original sources, supporting entities and flags. The review evaluates biological claims independently of inert relationship fields. No new annotation row was added. Available genuine prior research reports were used for discovery; primary text and curated record statements were preferred for evidence. The actual Falcon and perplexity-lite fallback attempts failed (authorization/quota errors), as recorded in `.cache/module-audit-logs/auxin-fetch/`; no provider report was fabricated. Normal publication fetching and normal ReferenceFetcher URL recovery supplied the sources below. Canonical PMID records were not hand-edited to insert recovered text.

The annotation-reviewer workflow was applied to every row. Bare protein-binding rows are refined only where the interaction and functional partner class support a more informative term; removal of an otherwise uninformative binding row does not dispute the measured interaction. True general transcription terms are refined rather than rejected. Nuclear evidence does not establish absence from cytoplasm.
TPL is a transcriptional corepressor, not an enzyme inferred from the catalytic activities of its partners. The 2012 interactome full text was recovered through the normal URL pipeline: `url:https://pmc.ncbi.nlm.nih.gov/articles/PMC3252085/`, canonical PMID:22065421. The paper combines yeast two-hybrid library screens and TF arrays with selected validations. Each existing pair retains its actual partner identity and evidence payload, while its functional interpretation is bounded: a screen interaction does not establish the exact repression motif, native target genes or obligatory complex for every hit. The full text explicitly identifies presumed chromatin regulators “SDG19, EMF1, VRN5, FVE”, permitting the corresponding binding-class refinements without assigning their chemistry to TPL. Uncharacterized partners remain uninformative bare-binding removals.

PMID:34075876 separates Mediator contacts, synthetic Arabidopsis-auxin circuitry in yeast, and plant assays. Binding of MED21/MED10B is informative, but a universal endogenous requirement is not inferred. Its finding that multimer formation had minimal influence on repression under those assay conditions does not make self-association false or irrelevant: structural/interactome self-binding and homodimerization rows are retained as core assembly properties, with no universal tetramer requirement. The N-terminal TOPLESS and C-terminal WD40 interaction surfaces are not collapsed into one universal repression-motif binding site. PMID:38750356 provides the specific temperature-sensitive JAM–TWA1–TPL/TPR context for TWA1 binding.

Nuclear annotations remain ACCEPT. The AtSubP-only cytoplasm prediction is UNDECIDED: the inspected sources do not settle a cytoplasmic pool, and strong nuclear evidence is not counterevidence. This uncertainty concerns a prediction rather than a supposedly inaccessible publication. Broad transcription regulation is refined to the demonstrated negative direction. Auxin and jasmonate participation remains supported by active corepressor work, not merely necessity.

Validation and source-closure results are recorded in `.cache/module-audit-logs/auxin-arf-tpl-final-report.md`; the committed helper history identifies this curation session.
