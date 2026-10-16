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
