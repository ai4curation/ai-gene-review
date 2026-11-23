# hldA review notes

## 2026-10-25: ADP-heptose module audit

RCSB 4E84 entity 1 contains 352 residues, including the complete 316-residue B4EB35 sequence at zero-based offset 36. Its source taxon is 216591 (J2315), and the SIFTS reference covers 100% of B4EB35. PMID23256532 uses K56-2 for its genetic complementation assays, so that phenotype is not described as a J2315 assay.

Mapping was checked against https://data.rcsb.org/rest/v1/core/polymer_entity/4E84/1 and the fetched UniProt sequence by exact substring comparison after removing sequence-line whitespace. N-terminal construct residues were excluded by locating the full native sequence; no inference of native activity was made from a PANTHER label.

The split HldA/HldC system is distinguished from fused HldE. PANTHER labels containing “BIFUNCTIONAL PROTEIN HLDE” cannot establish that both activities are present in a monofunctional representative. GO definitions were retrieved from QuickGO on 2026-10-25: GO:0016773 requires an alcohol acceptor, whereas GO:0016779 transfers a nucleotidyl group; HldC acts on the sugar phosphate.

Default Falcon research and perplexity-lite fallback were attempted concurrently with publication caching. Falcon returned HTTP403 and the fallback failed authentication/quota; no provider report was authored manually. Manual source review underlies these decisions. FEBA fetch was attempted but no local or reachable source was available for this organism.

PMID:23256532 directly supports kinase chemistry and the homodimeric structure. Its full text states: “HldA and HldC are homologous to the N- and the C-terminal domains of HldE, respectively.” The cytosol annotation was UNDECIDED in this round because neither structural nor complementation evidence directly localizes the native protein; it is now ACCEPT (see the 2026-11-02 entry). Two electronic nucleotidyltransferase claims are contradicted by the single kinase architecture.

## 2026-11-02 — cytosol resolved to ACCEPT

GO:0005829 moves from `UNDECIDED` to `ACCEPT`, decided by the new `PTHR46969` family
review rather than by any new experiment on J2315 HldA.

The descent step is now stated explicitly in the review, because it is load-bearing.
The GOA row is a `GO_REF:0000118` TreeGrafter assignment whose with/from is the graft
node `PTN002931072`, not the PAINT node; the cytosol IBD for this family sits at
`PTN000062036`. TreeGrafter transfers terms from PAINT-annotated ancestors, so the row
asserts that `PTN002931072` lies at or below `PTN000062036`. That ancestry follows
from the mechanism and is **not** checkable in the committed PAINT slice, which
records IBD rows but no tree topology — the one unverified link in the argument.

Granting it, the claim inherits experimental grounding, because `PTN000062036` is
seeded by E. coli HldE itself, whose cytosol rows are IDA against the K-12
biochemical-fractionation proteome [PMID:15911532] and the cytosolic abundance
proteome [PMID:18304323]. Neither paper names HldE in the text available here, so
they establish the experiments behind those IDA rows rather than target-specific
peptide evidence; the per-protein assignment is the curator's. The row previously
carried no `supported_by` at all and now cites both papers and the PAINT row.

Independently of the propagation, HldA was purified and crystallized as a soluble
enzyme and acts on cytoplasmic sugar phosphates, and no competing compartment is
proposed for any member of the family. That native J2315 HldA was never localized
directly limits the strength of the evidence, not the correctness of the compartment.
