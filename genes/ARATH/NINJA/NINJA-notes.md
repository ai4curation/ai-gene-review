# NINJA (At4g28910; UniProt Q9SV55, UniProt gene name AFPH2) curation notes

## 2026-10-06 — initial review (jasmonate_coi1_jaz_signaling module)

- UniProt gene name is AFPH2 (synonym NINJA). Folder and gene_symbol use the standard Arabidopsis/TAIR symbol NINJA. Fetched by accession: `just fetch-gene ARATH Q9SV55 --alias NINJA`; UniProt record checked (NINJA_ARATH, At4g28910).
- `just deep-research-falcon ARATH NINJA` failed (HTTP 429); review based on cached publications.

### Key evidence (Pauwels et al. 2010, PMID:20360743, full text)
- Adaptor linking JAZ to TPL/TPRs [PMID:20360743 "Here we show that the Arabidopsis JAZ proteins recruit the Groucho/Tup1-type co-repressor TOPLESS (TPL) and TPL-related proteins (TPRs) through a previously uncharacterized adaptor protein, designated Novel Interactor of JAZ (NINJA)."].
- EAR motif needed and sufficient for repression [PMID:20360743 "Second, a NINJA fragment containing the EAR motif, but lacking a JAZ interaction domain, was sufficient for repression."].
- Binds TIFY motif of most JAZs (not JAZ7/JAZ8) and group-II TIFY proteins PPD1/PPD2/TIFY8.
- Nuclear [PMID:20360743 "Analysis of seedlings producing a C-terminal GFP fusion with NINJA revealed a clear nuclear localization for NINJA"].
- OE reduces, KD enhances JA responses.
- Leaf flatness with PPD2 via CYCD3;2 [PMID:29991485]; root stem cell niche via PAT1H1 [PMID:26956135, abstract only].

### Decisions
- 41 protein-binding IPI rows resolved by supporting_entities: JAZ, PPD/TIFY8, TPL/TPR2/TPR3 partners -> MODIFY to GO:0001222 transcription corepressor binding; PAT1H1 and GID1A partners -> REMOVE (uninformative, not a rejection of the interaction).
- NEW: GO:0003714 transcription corepressor activity (IDA, PMID:20360743) as the core MF. GO has no "corepressor adaptor" MF; raised as a suggested question.
- signal transduction (IEA) marked over-annotated (uninformative parent).
