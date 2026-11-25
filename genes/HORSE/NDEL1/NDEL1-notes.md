# NDEL1 (horse, A0A5F5PSW5) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

New review (no prior file existed). ProtNLM2 output was not consulted.

### Data and deep research
- `just fetch-gene HORSE A0A5F5PSW5 --alias NDEL1`: 34 GOA rows (IBA from PAINT plus
  Ensembl Compara/UniProt IEA). No experimental annotation exists for horse NDEL1.
- `just deep-research-falcon HORSE NDEL1 --fallback perplexity-lite` failed (both the
  falcon run and the perplexity-lite fallback exited with an error; no deep-research file
  was written). The review instead uses the literature cached for, and cited by, the
  complete human NDEL1 review (`genes/human/NDEL1/`), all with publications in `publications/`.

### Identity and gene model
- Unreviewed TrEMBL entry, PE 3, 481 aa; VGNC:20610 NDEL1; PANTHER PTHR10921:SF0
  (NUCLEAR DISTRIBUTION PROTEIN NUDE-LIKE 1), the vertebrate NDEL1 subfamily that also holds
  human Q9GZM8, mouse Q9ERR1 and rat Ndel1. Orthology is therefore grounded in subfamily
  membership, not just a best hit.
- Alignment (`NDEL1-bioinformatics/RESULTS.md`): horse 1-338 = human 1-338 with 3
  substitutions (98% identity, no gaps). The human C-terminal heptapeptide 339-345 (with the
  S344 phospho-site) is replaced by a 143-residue extension with no counterpart in human
  NDEL1 or its isoforms; the donkey model (A0A9L0IJ72) shares it. This is most likely an
  alternative or erroneous Ensembl final-exon model, not a conserved region. All mapped
  functional elements (coiled coil and LIS1-binding segment, CDK phospho-sites S215/T219/
  S231/S242/T245, DISC1-binding region, centrosome-targeting region, Cys273) are retained,
  so the accession is treated as the horse NDEL1 product with a doubtful C-terminus.

### Evolutionary grounding of the IBA rows
- PTHR10921 family review (`interpro/panther/PTHR10921/PTHR10921-review.yaml`) flags the
  eukaryote-root node PTN000100519 as TOO_DEEP for kinetochore, centrosome, microtubule
  nucleation and centrosome separation, but the concern is reach into fungi and SF1
  (fly/worm), not vertebrate NDEL1. Horse NDEL1 is in SF0, so these terms are as sound for
  it as for human NDEL1. No disagreement on subfamily placement.
- Kinesin complex (PTN000100519, single rat seed) is assessed WRONG_NODE: Ndel1 is cargo of
  kinesin-1 via DISC1, not a kinesin subunit. Removed here, consistent with human NDEL1 and
  all other family reviews.
- PTN002589147 (regulation of neuron projection development) and PTN000100522 (cell
  migration) both cover vertebrate NDEL1.

### Decisions (consistent with the human NDEL1 review)
- Core: dynein regulation via LIS1/dynein IC binding (cytoskeletal motor regulator
  activity); centrosome; kinetochore; cortical radial migration/nucleokinesis; centrosome
  localization; vesicle transport along microtubule; microtubule binding.
- Non-core: mitotic roles (spindle orientation, chromosome segregation/localization,
  centrosome separation, microtubule nucleation), neurite outgrowth, lysosome localization,
  ruffle assembly (osteoclast), neurofilament cytoskeleton, axon hillock, leading edge,
  tubulin binding, regulation of intracellular protein transport.
- Over-annotated: synaptic vesicle, insulin receptor signaling pathway.
- MODIFY: identical protein binding -> protein homodimerization activity; microtubule
  organizing center -> centrosome (more specific, already carried).
- Relative: human NDEL1 (Q9GZM8, same SF0 subfamily) has a complete review.
- Module: `modules/nucleokinesis.yaml` (LIS1-NDEL1/NDE1 dynein regulatory module).
