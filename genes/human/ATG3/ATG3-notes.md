# ATG3 (human, Q9NT62) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: human ATG3 is the experimentally characterised reference relative for the
HORSE/ATG3 (A0A3Q2L0A4) ProtNLM2 benchmark gene. No ProtNLM2 output was consulted.

### Deep research
- `just deep-research-falcon human ATG3 --fallback perplexity-lite` failed: Edison API
  returned 403 "Failed to authenticate"; the perplexity-lite fallback timed out (600 s).
  A second direct perplexity-lite attempt also timed out. No deep-research file exists;
  the review rests on the cached publications and the UniProt record.

### Evolutionary grounding
- PANTHER: Q9NT62, mouse Q9CPX6 and yeast P40344 are all in PTHR12866:SF2
  (UBIQUITIN-LIKE-CONJUGATING ENZYME ATG3) per `interpro/panther/PTHR12866/PTHR12866-entries.csv`;
  ATG10 is in a different subfamily (SF5), so IPR007135 (Atg3/Atg10) alone does not give
  Atg8 specificity.
- IBA rows derive from PAINT nodes PTN000305307 and PTN000305308; human ATG3 is itself a
  donor for the conjugating-activity, cytosol and autophagosome-assembly IBAs.

### What is experimentally established in human
- E2 activity for Atg8 family (GATE-16, GABARAP, MAP-LC3), Cys264 thioester
  [PMID:11825910 "hApg3p is an E2-like enzyme essential for three human Apg8p homologues"].
- E1/E3 binding sites overlap; ATG3 cycles between ATG7 and E3 [PMID:24186333]; ATG12-binding
  segment needed for E3 interaction and LC3 lipidation [PMID:24191030]; ATG7-interacting region
  [PMID:26043688].
- N-terminal curvature-sensing helix plus conserved region couple membrane geometry to
  catalysis; human ATG3 rescues Atg3-/- MEFs [PMID:33446636]; anionic/curved membrane binding
  [PMID:29142222]; noncanonical LIR needed for ATG3~LC3 thioester and lipidation [PMID:37252361].

### Inferred only (mouse, by similarity)
- ATG12-ATG3 autoconjugation at Lys243; mitochondrial homeostasis phenotype [PMID:20723759,
  mouse cells]; PDCD6IP/endolysosomal role; OFD1/ciliogenesis. Kept Atg12 transferase as
  non-core; marked mitochondrial-fragmentation and cilium-regulation transfers as
  over-annotations (indirect phenotypes, necessity not participation).

### Key decisions
- GO:0019776 Atg8-family ligase activity (E3 term) -> MODIFY to GO:0141046 conjugating enzyme.
- GO:0016567 protein ubiquitination and GO:0006612 protein targeting to membrane -> MODIFY to
  GO:0061739 protein lipidation involved in autophagosome assembly.
- GO:0034274 Atg12-Atg5-Atg16 complex (IDA x3) -> MARK_AS_OVER_ANNOTATED: transient E2-E3
  client, not a subunit; not removed because these are curator IDA calls.
- Bare protein binding rows removed per policy, except ATG7 rows refined to GO:0044388.
- Plasma membrane (HPA IF) marked over-annotated.
