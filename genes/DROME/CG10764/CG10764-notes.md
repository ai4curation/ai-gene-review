# CG10764 (SP77, A1ZAT2) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: reviewed as the closest experimentally studied relative of DROME/CG43742 (same PANTHER 19.0
subfamily PTHR24260:SF147, tandem PD+PLD branch). No ProtNLM2 output was consulted.

Deep research: `just deep-research-falcon DROME CG10764 --fallback perplexity-lite` failed
(Edison API "Failed to authenticate"; perplexity fallback HTTP 403). The review uses the cached literature
below plus a local motif scan.

### Sequence and family
- 523 aa, SignalP signal peptide 1-18, two PS50240 Peptidase S1 domains (38-265, 274-517).
- Domain 1: complete triad H78/D121/S214, S1-pocket D208 (trypsin-like P1 predicted)
  [file:DROME/CG10764/CG10764-bioinformatics/RESULTS.md].
- Domain 2: no His or Ser motif; protease-like domain [same file]; agrees with
  [PMID:30367934 "SP77, SP222, SP248, and SP251 contain a PD and a PLD"].
- PANTHER: UniProt DR and the GOA IBA rows use PTHR24256 (PTN000667087, Ecdysozoa node; IBD for
  GO:0005576 and GO:0045087). The PANTHER 19.0 fruit-fly HMM file (.cache/panther/PTHR19.0_fruit_fly)
  assigns A1ZAT2 to PTHR24260:SF147 "EG:BACR7A4.3 PROTEIN-RELATED". The PAINT seeds of PTN000667087 lie in
  other PTHR24260 subfamilies (see genes/DROME/CG43742/CG43742-bioinformatics/RESULTS.md), so the innate-immune
  IBA alone would be a weak transfer. GO:0004252 in this family is asserted at the root PTN001207268 with
  IKR losses at specific nodes; CG10764 has no NOT annotation.

### Experimental evidence (this species)
- JAK/STAT target in haemocyte-like cells; tested in hopTum blood-cell over-proliferation model
  [PMID:20168330, abstract only; forced re-fetch gave no full text]. FlyBase IGI with hop:
  negative regulation of hemocyte proliferation. Direction not verifiable from abstract.
- RNAi (two independent lines) in lamellocytes (msn-GAL4) or plasmatocytes (eater-GAL4) reduces
  encapsulation of L. clavipes eggs [PMID:33644706 "results in a significant reduction in the proportion of
  wasp eggs that are successfully encapsulated"]. RNAi only; no null allele, rescue or catalytic-dead test.
- No biochemistry: protease activity, activation and substrates are unmeasured.

### What is established vs inferred (for transfer to relatives)
- Experimentally established in D. melanogaster: required in haemocytes for normal encapsulation (RNAi);
  genetic modifier of hopTum; JAK/STAT-responsive expression.
- Inferred from sequence only: serine endopeptidase activity (domain 1), trypsin-like specificity,
  secretion.
- Not established: the step of the immune response, whether catalysis is required.

### Decisions
- GO:0004252 (IEA, 2x ISM) ACCEPT; peptidase/serine-type peptidase/hydrolase MODIFY -> GO:0004252.
- GO:0005576 (IBA, IEA) ACCEPT; GO:0006508 (IEA, ISM) ACCEPT.
- GO:0035207 IGI KEEP_AS_NON_CORE (curator saw full text; regulatory tumour-model phenotype).
- GO:0045087 IBA ACCEPT, supported independently by the haemocyte RNAi encapsulation phenotype.
- No NEW process terms (e.g. encapsulation of foreign target): RNAi necessity evidence only, and
  FlyBase has not annotated the 2021 microPublication.
