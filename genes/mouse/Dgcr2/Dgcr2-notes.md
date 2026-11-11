# Dgcr2 (mouse, P98154) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: reviewed as the closest experimentally characterised relative of
DROME/CG42404 (same PANTHER family/subfamily PTHR15256:SF6). ProtNLM2 outputs were
not consulted.

### Deep research
`just deep-research-falcon mouse Dgcr2 --fallback perplexity-lite` failed: falcon
returned "Edison API request failed: Failed to authenticate" (403) and the
perplexity-lite fallback also failed (JWT token required). No deep-research file was
produced. Literature was gathered directly from PubMed (esearch DGCR2[tiab]) and the
papers cached in `publications/`.

### Evolutionary grounding
- UniProt: PANTHER PTHR15256 (INTEGRAL MEMBRANE PROTEIN DGCR2/IDD) and PTHR15256:SF6;
  the family has a single subfamily, which also holds human DGCR2 (P98153) and fly
  CG42404. Mouse Dgcr2 (MGI:892866) is the experimental donor for PAINT node
  PTN000391897, which supplies only the IBA `membrane` (is_active_in) annotation.
  PAINT propagated no process or function term, consistent with how little is
  established for the family.
- Domain architecture (UniProt): signal peptide 1-24, extracellular 25-347 with
  LDL-receptor class A (28-68), C-type lectin (113-239) and VWFC (268-331) domains,
  single TM helix 348-366, cytoplasmic 367-548 (415-548 disordered). Single-pass type I
  membrane protein. No carbohydrate-binding residues have been shown; the CTLD
  (IPR034010 DGCR2-like CTLD) is not evidence of lectin activity.

### Literature (mouse unless stated)
- PMID:8630060 (abstract only): Sez-12 cloned from PTZ-treated cortical neurons;
  "SEZ-12 expression is transiently down-regulated in the mouse brain by injection of
  PTZ"; encodes "membrane-bound C-type lectin" from deduced sequence; ubiquitous
  low-abundance expression. Basis of the IDA membrane and IDA
  acts_upstream_of_or_within response to xenobiotic stimulus rows. The xenobiotic row
  rests on an expression change only.
- PMID:28955813 (full text): Dgcr2-KO/EGFP-KI mice: ~20% gait abnormalities,
  reduced rotarod latency, sparse cerebellar Purkinje cells. Organismal phenotype; not
  used as process participation.
- PMID:29305086 (abstract only): in utero electroporation knockdown in mouse cortex
  "impaired radial locomotion and final translocation of projection neurons"; Dgcr2
  identified "as a novel member of the Reelin complex, regulating the phosphorylation of
  Reelin-dependent substrates". Complex members/binding partners not visible in the
  abstract; not converted into annotation.
- PMID:35212007 (full text): Dgcr2 knockdown in upper-layer mPFC pyramidal neurons
  disrupts laminar positioning, dendritic morphology and excitatory activity.
- PMID:37480133 (full text): DGCR2 enriched in postsynaptic densities by subcellular
  fractionation of adult wild-type mouse brain ("we found DGCR2 concentrated in the
  PSDs, but not in the presynaptic membrane fraction"); co-localises with PSD-95 puncta.
  In vivo shRNA (in utero electroporation, mouse hippocampus) reduced CA1 spine
  density; Dgcr2 mutant mice have reduced mEPSC frequency and impaired LTP. The
  NRXN1 binding, PSD-95 binding and cell aggregation assays used FLAG-tagged HUMAN
  DGCR2 in HEK293T cells; cultured neurons were rat. So: PSD localisation and spine
  development requirement are mouse-established; NRXN1 binding via the ECD is
  established for human DGCR2 (same PANTHER subfamily) and transferred by ISO.
- Human association/expression studies (PMID:16783572, PMID:30901624) are
  disease-association only.

### Existing annotation decisions
- membrane (IBA, IDA, IEA): true; MODIFY to plasma membrane (type I TM protein whose
  ECD engages NRXN1 in trans; surface-IP of DGCR2). All three rows treated consistently.
- response to xenobiotic stimulus (IDA, PTZ): expression-change only;
  MARK_AS_OVER_ANNOTATED.
- cognition (ISO from human IMP PMID:23227193): the human source is a single AD case
  whose CNV overlapped both HLA-DRA and DGCR2 (Table footnote b); this does not
  implicate DGCR2 in cognition. MARK_AS_OVER_ANNOTATED with a source defect noted on
  the human donor row.

### New proposals
- postsynaptic density (IDA, PMID:37480133, mouse brain fractionation).
- dendritic spine development (IMP, PMID:37480133, mouse in vivo shRNA + mutant mice);
  DGCR2 is proposed to act as a trans-synaptic adhesion partner of NRXN1, i.e. it
  contributes structure to the process, not merely being required.
- cell adhesion molecule binding (ISO from human DGCR2 data in PMID:37480133).
Not proposed: neuron migration / Reelin signalling (abstract-only evidence; necessity
data); cognition/behaviour (organismal phenotypes); C-type lectin carbohydrate binding
(no data).
