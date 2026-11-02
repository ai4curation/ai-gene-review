# snk (P05049) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: snk was reviewed as the closest experimentally characterised relative of CG43124 (A0A0B4K7P3), which PANTHER 19.0 places in the same subfamily, PTHR24260:SF147. This review treats snk on its own terms; no ProtNLM2 output was consulted.

### Deep research

`just deep-research-falcon DROME snk --fallback perplexity-lite` failed: Falcon (Edison API) returned "Failed to authenticate" (403 Forbidden), and the perplexity-lite fallback also failed. No deep-research file exists. The review is based on the cached primary literature listed below plus the UniProt record.

### What is experimentally established in D. melanogaster

- Snake is a serine protease required maternally for embryonic dorsal-ventral axis specification [PMID:11486795 "The maternal effect gene snake is required for the establishment of the dorsal-ventral axis during the embryonic development of Drosophila."].
- Cascade order and catalysis, from biochemical reconstitution in S2 cells: [PMID:11296245 "Here, we demonstrate biochemically that GD activates Snake, which in turn activates Easter."]; preactivated Snake cleaves a catalytically inactive Easter zymogen, and Gd does not [PMID:11296245 "supporting the conclusion that Snake is the protease that activates Easter"].
- Active-site labelling: [PMID:20638387 "To confirm that the 57 kDa processed form of Snake represented an active form of the protein, we performed activity-labeling with FP-rhodamine."]. Snake activation is cascade-dependent but Pipe-independent [PMID:20638387].
- The first spatially restricted step is Snake cleavage of Easter [PMID:20605458 "we find that the proteolysis of Easter by Snake is the first Pipe-dependent step and therefore the key ventrally restricted event in the protease cascade"]. The Snake prodomain binds the Easter catalytic domain [PMID:20605458 "These results indicate that the Easter catalytic domain and the Snake prodomain are required for this interaction"]. P184L blocks cleavage by Gd (UniProt MUTAGEN, from PMID:20605458).
- Location: perivitelline space [PMID:11296245 "The zymogen forms of Snake and Easter, as well as the Spätzle protein, appear to be freely diffusible in the extracellular perivitelline space surrounding the embryo"]; perivitelline fluid transplantation rescues snake embryos [PMID:1739964].
- Epistasis: activated Easter bypasses snake [PMID:1425342]; in vivo Easter processing requires the upstream proteases [PMID:9477324].

### Inferred, not established

- Innate immune response (IBA, PTN000667087). All donors (psh, MP1, spirit, SPE, grass, modSP, sphinx1/2, scaf) are in PTHR24260 subfamilies other than SF147, and snk is not a donor (see `snk-bioinformatics/RESULTS.md`). No experimental immune role for Snake was found. The immune Toll pathway uses ModSP-Grass-SPE. Marked as over-annotated, not removed, because no study has formally excluded an immune contribution.

### Evolutionary grounding

- PANTHER 19.0: PTHR24260:SF147, a Drosophila-only subfamily of 27 fly proteins (includes CG43124, CG43125, CG43742, CG10764). No other SF147 member has published biochemistry that we found. DIOPT reports no confident ortholog in human or other model organisms (stated in the task brief; not re-checked here).
- Snake's catalytic activity rests on its own biochemistry plus an intact His-Asp-Ser triad (H235/D283/S381). Its substrate (Easter), its activator (Gd) and the processes it takes part in (Toll ligand activation cascade, D/V axis specification) are specific to the snk lineage. Do not transfer them to other SF147 members on subfamily membership alone.

### Actions summary

- ACCEPT: serine-type endopeptidase activity (IDA x2, IEA, ISM x2, TAS); zymogen activation (IMP); Toll receptor ligand protein activation cascade (IDA, IGI x2, IMP); dorsal/ventral axis specification (IGI x2).
- MODIFY: endopeptidase activity -> serine-type endopeptidase activity; extracellular region (IBA, IEA, TAS x2) -> perivitelline space (GO:0098595, the term the comparators gd, ea, ndl and Spn27A carry by IDA); proteolysis (IEA, ISM) and protein processing (IEA) -> zymogen activation.
- MARK_AS_OVER_ANNOTATED: innate immune response (IBA).
