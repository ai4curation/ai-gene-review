# CADM1 (donkey, A0A9L0IJE9) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: A0A9L0IJE9 is the gene-centric canonical product (UP000694387) of the donkey CADM1 gene.
The ProtNLM2 benchmark entry A0A9L0IX39 (genes/EQUAS/CADM1) is a short-tail alternative product
of the same gene. This review does not use any ProtNLM2 output.

Setup: `just fetch-gene EQUAS A0A9L0IJE9 --alias CADM1__A0A9L0IJE9` seeded 28 GOA rows, all IEA
(Ensembl Compara GO_REF:0000107, TreeGrafter GO_REF:0000118, combined GO_REF:0000120).

Deep research: `just deep-research-falcon EQUAS CADM1__A0A9L0IJE9 --fallback perplexity-lite` failed.
Falcon reported "Failed to authenticate", and perplexity returned HTTP 401 insufficient_quota. No
deep-research file exists; the review instead uses cached primary literature (8 papers newly cached
with `just fetch-pmid`, 5 with full text) and the UniProt records of human Q9BY67 and mouse Q8R5M8.

Evolutionary grounding:
- Donkey A0A9L0IJE9, human Q9BY67 and mouse Q8R5M8 are all in PANTHER PTHR45889:SF2 (CELL ADHESION
  MOLECULE 1).
- Alignment (CADM1__A0A9L0IJE9-bioinformatics/RESULTS.md): 98.87% identity to human and 99.12% to mouse.
  The V-type domain, transmembrane helix and the whole 47-residue cytoplasmic tail are identical to
  human, including the EYFI PDZ-binding motif.
- PAINT (via TreeGrafter, PTN002913384) propagated signaling receptor binding, plasma membrane, homophilic
  cell-cell adhesion, cell recognition, susceptibility to NK cytotoxicity, detection of stimulus, neuron
  projection and synapse.
- PAINT did not propagate the mouse-only synaptic process terms (presynapse assembly, maintenance of
  postsynaptic specialization, retrograde trans-synaptic signaling), PDZ binding or heterophilic adhesion.
  Those reach donkey only via the 1:1 Ensembl Compara transfer. I respected the PAINT omission by keeping
  the synapse-assembly, maintenance and retrograde-signaling terms as non-core. I accepted heterophilic
  adhesion, PDZ binding and synaptic membrane adhesion, because they are direct molecular properties of
  conserved regions with independent rodent IDA/IPI support.

Species status: no donkey experiments. Every function is inferred from human and mouse.

Key decisions:
- NEW GO:0098632 cell-cell adhesion mediator activity, the MF behind the accepted adhesion processes.
- GO:0051606 detection of stimulus: MARK_AS_OVER_ANNOTATED. CADM1 is what CRTAM-bearing cells detect
  [PMID:15811952 "natural killer (NK) cells and CD8+ T cells recognize Necl-2 through a receptor known as class I-restricted T-cell-associated molecule (CRTAM)"].
- GO:0097021 lymphocyte migration into lymphoid organs: MARK_AS_OVER_ANNOTATED. The mouse IMP reports
  gut T-cell residency, with CADM1 as the DC ligand [PMID:24687959 "Crtam−/− and Cadm1−/− mice almost completely lacked CD4+CD8+ T cells in the intestinal epithelium under steady-state conditions"].
- GO:0008021 synaptic vesicle: UNDECIDED. The source paper is abstract-only and the location conflicts
  with plasma-membrane topology.
- synapse and neuron projection: MODIFY to the specific descendants this gene already carries.
- identical protein binding: TOO_GENERAL, beside protein homodimerization activity.
