# Ank2 (M9MRX4, isoform U) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Scope: a new review of M9MRX4, the UniProt gene-centric canonical product of FlyBase
FBgn0261788. The folder is named `Ank2__M9MRX4` because `genes/DROME/Ank2/` holds the
review of a different accession (Q3KN55, the 697-aa Ank2-PE). No ProtNLM2 files or
prediction-evidence folders were opened.

### Deep research

`just deep-research-falcon DROME Ank2__M9MRX4 --fallback perplexity-lite` failed.
Falcon (Edison) returned "Failed to authenticate", and perplexity-lite returned HTTP 401
(insufficient quota). No deep-research file exists. The review is built from primary
literature cached in `publications/`. Full text was recovered for PMID:18439405,
25800091, 23610557, 31475145, 24395637, 25139856, 27911898, 37194019 and 29602811. Only
abstracts are available for PMID:18439406, 16920632, 22939627, 23390136, 12056839 and
19317464.

### What M9MRX4 is

From `Ank2__M9MRX4-bioinformatics/analysis-output.txt`:
- 13,559 aa. Its first 11,629 aa are identical to X2JCM1 (isoform AA, 11,634 aa). That
  matches the 11,640-aa Ank2-XL of Stephan et al. 2015
  [PMID:25800091 "Ank2-XL encodes one of the largest neuronal proteins in Drosophila with an open reading frame of 11,640 aa"].
- It also ends with the last 1,662 aa of Ank2-L (Q7KU92). The Ank2-L microtubule-binding
  segment 1682-2089 (PMID:18439405) sits at the same coordinates in M9MRX4.
- So M9MRX4 contains both giant-isoform C-terminal regions that have been shown
  experimentally to bind microtubules. We did not establish whether this exact splice
  form is expressed.

### Evolutionary grounding (the key caveat)

- PANTHER 19 splits the ankyrins. PTN002380879, the bilaterian ankyrin PAINT node,
  is in PTHR24133 and contains human ANK1/ANK2/ANK3 and fly **Ank** (FBgn0011747). Fly
  **Ank2** is in PTHR24123:SF141, in an ecdysozoan node with worm unc-44 and mask-1,
  sister to human ASB4/ASB10/ANKRD55.
- Our local `interpro/panther/PTHR24123/PTHR24123-paint.tsv` lists PTN002380879 under
  PTHR24123, which reflects an older release. The campaign brief's statement that "SF141
  holds PTN002380879" comes from that stale file. In PANTHER 19, Ank2 is not a descendant
  of the node.
- QuickGO confirms this: all six PTN002380879 IBA rows in fly go to Ank (Q0KIE7), and
  none go to any Ank2 accession. M9MRX4 has no IBA rows.
- Jegla et al. 2016 built a maximum-likelihood ankyrin phylogeny on the ANK repeats plus
  the ZU5-ZU5-UPA cassette. It treats Ank2 as a true bilaterian ankyrin with giant
  isoforms [PMID:27911898 "Drosophila Ank2 and mouse AnkG share 64.4% amino acid identity across the Ank-UPA core"].
  The PANTHER split is therefore probably an artefact, but this is not settled.
- Decision: no PAINT terms from ANK1/2/3 are transferred. Every NEW term rests on fly
  Ank2 experiments. The placement problem is raised as a suggested question.

### Annotation decisions (summary)

- ACCEPT: microtubule cytoskeleton organization (x2), NMJ development (x2), cytoskeleton,
  plasma membrane (HDA), NMJ, presynaptic periactive zone, presynaptic membrane (x2),
  terminal bouton.
- MODIFY: cytoplasm to cytoskeleton; membrane to plasma membrane and presynaptic membrane.
- KEEP_AS_NON_CORE: sensory perception of sound, short-term memory, positive regulation
  of synaptic assembly at NMJ (abstract-only sources, so we defer to the curators).
- UNDECIDED: axon extension (PMID:16920632 says "Ankyrin (Ank)", and we cannot tell
  whether Ank or Ank2 was assayed).
- REMOVE: signal transduction (death-domain InterPro2GO over-propagation).
- REMOVE, with a FlyBase source defect: neuron cellular homeostasis (IGI) and negative
  regulation of neuromuscular synaptic transmission (IMP), both from PMID:22153373. In
  that paper ank2 is the degeneration background, and egr/wgn/Dcp-1/Debcl/Dark are the
  genes that carry the findings. QuickGO shows the same rows on egr, wgn, Debcl and Dark
  with WITH = FBgn0261788, while the Ank2 IGI row names Ank2 as its own interactor. Loss
  of ank2 *reduces* EPSPs [PMID:22153373 "Next, we confirmed that the loss of ank2 results in impaired average EPSP amplitudes"].
- NEW (fly experimental):
  - microtubule binding (IDA, PMID:25800091 and PMID:18439405)
  - cell adhesion molecule binding (IPI, Nrg180 co-IP, PMID:23610557)
  - cytoskeletal adaptor activity
  - axon
  - maintenance of synapse structure
  - regulation of axon diameter

### Experimentally established in Drosophila, versus inferred

- Established, with direct fly data:
  - microtubule binding by the XL and L C-terminal segments, from in vitro pelleting
  - Nrg180 binding, by co-IP and S2 pull-down that depends on FIGQY
  - co-IP with Futsch
  - localization to axons and the presynaptic membrane, cytoskeleton and boutons
  - NMJ stability and microtubule organization, from mutants
  - axon caliber, from XL mutants and domain rescue
  - the proximal-axon diffusion barrier
- Inferred, not shown in the fly:
  - direct spectrin binding through ZU5-ZU5-UPA (the only fly evidence is genetic,
    "downstream of spectrin")
  - any function of the death domain
  - whether the isoform U splice form itself exists
