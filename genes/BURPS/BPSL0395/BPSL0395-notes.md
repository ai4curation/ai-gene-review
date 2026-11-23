# BPSL0395 review notes

## 2026-10-25: ADP-heptose module audit

RCSB 5X9Q entity 1 contains 173 residues, including the complete 161-residue Q63XZ4 sequence at zero-based offset 12. Its source taxon is 272560 (K96243), and SIFTS covers 100% of Q63XZ4. The UniProt RefSeq cross-reference WP_004189202.1 matches the protein identifier in PMID33733972. PMID28177319 names the earlier YP_107021.1 record.

Mapping was checked against https://data.rcsb.org/rest/v1/core/polymer_entity/5X9Q/1 and the fetched UniProt sequence by exact substring comparison after removing sequence-line whitespace. N-terminal construct residues were excluded by locating the full native sequence; no inference of native activity was made from a PANTHER label.

The split HldA/HldC system is distinguished from fused HldE. PANTHER labels containing “BIFUNCTIONAL PROTEIN HLDE” cannot establish that both activities are present in a monofunctional representative. GO definitions were retrieved from QuickGO on 2026-10-25: GO:0016773 requires an alcohol acceptor, whereas GO:0016779 transfers a nucleotidyl group; HldC acts on the sugar phosphate.

Default Falcon research and perplexity-lite fallback were attempted concurrently with publication caching. Falcon returned HTTP403 and the fallback failed authentication/quota; no provider report was authored manually. Manual source review underlies these decisions. FEBA fetch was attempted but no local or reachable source was available for this organism.

PMID:28177319 identifies the cloned protein and the AMP-transfer reaction. PMID:33733972 explicitly uses beta-glucose-1-phosphate because the native heptose substrate was difficult to obtain. This assay limitation is retained; inhibitor results are not claimed to establish native substrate specificity or growth inhibition. PMID:28986923 provides the later structure but its cached text is abstract-only, so its unseen experiments are not asserted. No separate kinase activity is supported by the HldC architecture.
