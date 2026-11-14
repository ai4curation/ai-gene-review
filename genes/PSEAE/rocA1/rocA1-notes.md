# rocA1 (PA3948, Q9HX68) review notes

## Literature

- RocA1 was found in a transposon screen for loci controlling cupB/cupC fimbrial gene expression; it is the response regulator of the RocS1-RocR-RocA1 system [PMID:15659157 "RocS1 is a sensor kinase, RocA1 is a DNA binding response regulator that activates cup genes, and RocR is an antagonist of RocA1 activity"].
- RocS1 interacts with the receiver domain of RocA1 and activates it through a phosphorelay [PMID:15659157 "the sensor kinase activates its cognate response regulator through a phosphorelay pathway"].
- Domain architecture (UniProt Q9HX68): N-terminal receiver (PF00072), C-terminal LuxR-type HTH (GerE, PF00196); PANTHER PTHR43214 (NarL/FixJ family response regulators).
- RocR, the EAL-domain antagonist, is reviewed in `genes/PSEAE/rocR/`.

Search: PubMed metadata for the GOA-cited PMID (abstract only; no PMC copy). NCBI E-utilities and Europe PMC search were unavailable (HTTP 500/503) during this session, so no further literature on direct RocA1-promoter binding was retrieved.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN008449896 | GO:0006355 regulation of DNA-templated transcription | 9 | 167 (26 taxa) | GO:0045893, IMP, PMID:15659157 | SOUND | The abstract states RocA1 is a DNA-binding response regulator that activates cup genes, identified as a locus controlling cupB/cupC transcription. Positive regulation of transcription is the right term for the gene and is subsumed by the node term. | E. coli NarL (P0AF28), NarP (P31802), UhpA (P0AGA6), RcsB (P0DMC7), BglJ (P39404); B. subtilis DegU (P13800); P. aeruginosa NarL (Q9HXD3); eraR (Q9I2C7) | Yes |

Node-level verdict for PTN008449896 (recorded here once; eraR cross-references this table): the node is a NarL/FixJ (LuxR-type HTH) response-regulator clade. Its GO:0006355 IBD rests on nine seeds, seven of them classical, experimentally characterised transcription factors (NarL, NarP, UhpA, RcsB, BglJ, DegU, P. aeruginosa NarL); the GO:0003700 and GO:0000976 IBDs on the same node rest on NarL, RcsB, BglJ and PA NarL only, not on PseudoCAP. The generic node term suits a clade of DNA-binding response regulators. The IBD stands without either PseudoCAP seed (rocA1, eraR). No GO_CENTRAL defect.

Seed confidence: the abstract states the decisive facts (DNA-binding regulator that activates cup genes); full text not read.
