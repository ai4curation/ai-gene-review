# rfc3: functional evidence

Rfc3 is an ATP-binding small subunit shared by replication factor C and alternative RFC complexes. It contributes to ATP-dependent clamp handling on DNA, supports processive DNA replication and repair, and participates in replication and DNA-damage checkpoint signaling through the Rad17-associated machinery. Its principal functions act on nuclear chromatin.

- [PMID:10588638] "From these results, we conclude that rfc3(+) is
required not only for DNA replication but also for replication and damage
checkpoint controls, probably functioning as a checkpoint sensor."

Evidence interpretation: sequence/domain records are used for family placement; AI descriptions and ARBA labels are not independent validation. Family transfer is limited to conserved properties and is identified as inference. Genome-scale localization annotations are retained where consistent with the biology; an abstract does not expose every individual observation. All original annotation rows are preserved.

ProtNLM provenance: pre-release `post-processed-2026_02_28k.xml`, exact entry and all evidence keys preserved in the source XML/JSON. These current Swiss-Prot entries are absent from the public TrEMBL pilot. Known-function overlap does not establish model training membership. See the function sidecar for atom-by-atom paragraph assessments.

Research provenance: the gene-focused Falcon report was generated concurrently with publication caching. The report was inspected for source leads; the biological decisions above rely on the cited primary records and specified family evidence.

The completed Falcon search has retrieval gaps: its inability to locate target-level localization is not used to override PomBase’s HDA records. Curated genomic-screen observations and the directly inspected papers take precedence over an empty literature-search result.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 files and prediction-evidence folders were not opened or used.

**Identity.** O14003 is the reviewed Swiss-Prot canonical product of rfc3 (SPAC27E2.10c), 342 aa, full length: AAA+ module (PF00004) with Walker A ATP-binding site at 63-70 and the RFC C-terminal lid domain (PF08542). Not a fragment, isoform or alternative gene model.

**Evolutionary placement.** PANTHER PTHR11669:SF9 ("REPLICATION FACTOR C SUBUNIT 5"). PANTHER 19.0 classification files place S. cerevisiae RFC3 (P38629), human RFC5 (P40937), mouse Rfc5 (Q9D0F6) and Drosophila RfC3 (Q9VKW3) in the same subfamily, so the direct ortholog is budding-yeast Rfc3 (= human RFC5); symbol numbers do not track orthology across species. The family review interpro/panther/PTHR11669/PTHR11669-review.yaml places rfc3 in SF9 too; no disagreement. IBA nodes: PTN000186209 (clamp loader, RFC complex, repair), PTN000186208 (DNA-templated replication), PTN000912313 (Rad17/Ctf18/Elg1 RFC-like complexes, seeded by SGD:S000005234 = yeast RFC3). PAINT did not propagate clamp unloader activity to the small subunits; I read that as deliberate.

**Evidence.**
- [PMID:10588638 "Pulsed-field gel electrophoresis suggested that rfc3-1 cells had defects in DNA replication."]; checkpoints defective; "Association of Rfc3 and Rad17 in vivo".
- [PMID:16040599 "No additional proteins were identified in these purified preparations, strongly suggesting that Elg1–RFC comprises the Elg1, Rfc2, Rfc3, Rfc4 and Rfc5 proteins only."]. The same paper only *suggests* unloading: "Alternatively, it has been suggested that the Elg1–RFC could function as a PCNA clamp unloader (6)."
- [PMID:16040599 "Instead of PCNA, Rad17–RFC loads the 9-1-1 complex onto DNA."]
- [PMID:10748208 "Processive synthesis occurred in the presence of PCNA, RFC, and Escherichia coli single strand DNA-binding protein (SSB) and required the presence of ATP."]
- [PMID:10704216 RFC required in reconstituted alternative excision repair].

**Changes from previous review.**
- Replaced support that quoted the UniProt record's own `DR GO` lines (circular) with literature and curated UniProt statements.
- DNA binding (IEA): ACCEPT -> KEEP_AS_NON_CORE (true, uninformative versus clamp loading).
- Ctf18-RFC (IBA, NAS): ACCEPT -> KEEP_AS_NON_CORE (phylogenetically sound membership; pombe complex not purified in cited work; peripheral role).
- DNA clamp unloader activity (IC): ACCEPT -> KEEP_AS_NON_CORE; Elg1-driven complex activity, cited paper only hypothesises it; contributes_to would be more accurate (suggested question).
- Checkpoint signaling reasons now explain participation (Rad17-RFC loads the 9-1-1 sensor clamp).
- Rewrote description; split core functions into RFC/PCNA loading and Rad17-RFC checkpoint roles; added reference_review for each PMID.

**Relative to review next.** S. cerevisiae RFC3 (P38629, SGD:S000005234), the SF9 ortholog and PAINT donor; no review in the repo (genes/yeast/RFC3 absent). Human RFC5 (P40937) is also unreviewed.

**Modules.** No module covers eukaryotic RFC or the pombe checkpoint clamp loaders; related: modules/dmel_elg1_rfc_like_complex.yaml, modules/dmel_9_1_1_checkpoint_clamp.yaml (Drosophila), modules/bacterial_chromosomal_dna_replication.yaml (bacterial clamp loader, same PTHR11669 family).
