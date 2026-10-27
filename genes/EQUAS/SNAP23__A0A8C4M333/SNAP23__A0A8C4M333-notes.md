# SNAP23 (donkey, A0A8C4M333) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: A0A8C4M333 is the UniProt gene-centric canonical product (211 aa, Ensembl
ENSEAST00005020803) of donkey SNAP23 gene ENSEASG00005013173. It is the full-length relative of
benchmark entry A0A8C4M285 (`genes/EQUAS/SNAP23/`, an alternative-terminal-exon 97-aa product).
No ProtNLM2 output was consulted.

Deep research: `just deep-research-falcon EQUAS SNAP23__A0A8C4M333 --fallback perplexity-lite`
failed (Edison API returned 403 Forbidden at login; the perplexity-lite fallback timed out at
600 s). No deep-research file was produced. The review relies on cached publications that I read
directly.

Evolutionary grounding (`SNAP23__A0A8C4M333-bioinformatics/RESULTS.md`):
- PANTHER PTHR19305:SF4 (SNAP23 subfamily), shared with human O00161 and mouse O09044. Human SNAP25
  is in SF5.
- The gapless global alignment gives 89.6% identity to human SNAP23, 91.9% to mouse Snap23 and 64.1%
  to human SNAP25. Gln-48 and the palmitoylated linker cysteines C79/80/83/85/87 are conserved;
  human C112 is Ser in donkey.
- PAINT nodes from the human IBA rows (QuickGO): PTN000447753 (fusogenic activity, exocytosis,
  SNARE complex), PTN000447754 (synaptic vesicle priming and fusion), PTN000447752 (plasma
  membrane). The SNAP25-specific syntaxin-1 binding and neuronal SNARE complex terms sit at a
  SNAP25-lineage node, PTN002712515, and were not propagated to SNAP23. I treat that omission as
  deliberate.

Literature (all on human or mouse proteins; nothing on donkey SNAP23):
- [PMID:8663154 "binds tightly to multiple syntaxins and synaptobrevins/VAMPs in vitro"]; "Unlike SNAP-25, SNAP-23 was expressed in all tissues examined."
- [PMID:12556468 "SNAP-23N can assemble spontaneously with the coiled-coil domains from SNAP-23C, syntaxin-4, and VAMP-3 to form a heterotetrameric complex."]
- [PMID:30811271 "a plasma membrane—localized Qbc-SNARE"], cooperating with STX11 in TLR4 delivery in macrophages.
- [PMID:24910990 "We show that syntaxin 11 binds to SNAP23 in NK cells"]
- [PMID:12859899 "whereas SNAP-23 did not support a standing pool of primed vesicles"]
- [PMID:17728451 "SNAP-23 supported asynchronous release only"]
- [PMID:20118925 "SNAP-23 was enriched in dendritic spines and colocalized with constituents of the postsynaptic density, whereas SNAP-25 was restricted to axons"]

Decisions:
- ACCEPT: helical-bundle zippering fusogenic activity, plasma membrane, exocytosis, vesicle fusion
  and SNARE complex. All are transferred from the same subfamily, with experimental support in
  human or mouse.
- MARK_AS_OVER_ANNOTATED: synaptic vesicle priming and synaptic vesicle fusion to the presynaptic
  active zone membrane. Both come from node PTN000447754, which is ancestral to SNAP23 and SNAP25.
  SNAP23-lineage rescue data show divergence: no primed pool, and asynchronous release only.
  The presynapse row is logically derived from the priming row and is marked the same way.
- No NEW terms. SNAP23 also acts in endosome-to-plasma membrane protein transport (human IDA) and
  in postsynaptic NMDA receptor delivery. These are specific uses of the same exocytic fusion
  activity, so I did not propose them for donkey from ortholog data alone.
