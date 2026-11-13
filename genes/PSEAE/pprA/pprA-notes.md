# pprA / PA4293 (Q9HWA7) review notes

## Summary of the literature

PprA is a 922-residue sensor histidine kinase of *P. aeruginosa*. UniProt (reviewed,
PPRA_PSEAE) places several PAS/PAC modules in the N-terminal half (DOMAIN 506-684
and others) and a HisKA/HATPase kinase core at the C-terminus. There is no signal
peptide and no transmembrane segment.

Primary data, Wang et al. 2003 [PMID:12499175], **full text read** (PMC149007):

- A spontaneous aminoglycoside-resistant PAK mutant (PAK1-3) with reduced membrane
  permeability was complemented by a genomic clone carrying PA4293, named *pprA*
  [PMID:12499175 "pUCP19B was found to contain a 3,280-bp DNA insert encoding a
  2,768-bp putative histidine kinase homolog, identical to PA4293 of the Pseudomonas
  genome sequence"].
- PprA has no signal sequence or TM segment and is predicted cytoplasmic, with
  N-terminal PAS and PAC motifs [PMID:12499175 "the PprA protein lacks a signal
  sequence or transmembrane segments; thus, it is likely a cytoplasmic protein"].
- **In vitro kinase assay with purified His-tagged proteins**: "PprA alone underwent
  active autophosphorylation, while PprB did not" and "in the presence of PprA, PprB is
  highly phosphorylated; thus, PprA functions as a specific kinase for PprB"
  [PMID:12499175].
- The *pprA* insertion mutant itself showed no change in antibiotic resistance
  (the effect was seen on overexpression), so the permeability phenotype is not a
  loss-of-function phenotype of *pprA*.

UniProt adds later work (PubMed:21091863, 23209420, 31492668 — not cached here) in which
PprA/PprB control a biofilm regulon (Flp type IVb pilin, BapA adhesin, CupE fimbriae) and
describes PprA as a heme sensor histidine kinase.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN009166588 | GO:0000155 phosphorelay sensor kinase activity | 4 | 268 (41 taxa) | GO:0000155, IDA, PMID:12499175 (PseudoCAP) | SOUND | Full text read: purified PprA autophosphorylates with [γ-32P]ATP and transfers phosphate to purified PprB. This is exactly the activity the term denotes, measured directly on this protein. | *S. pombe* Mak3 (O74539, EXP GO:0000155), *E. coli* AtoS (Q06067, IDA GO:0000155), *M. tuberculosis* PdtaS (P9WGL5, IDA GO:0000155) — all verified by live QuickGO query 2026-11-05 | Yes, comfortably: three of the four seeds have independent direct kinase evidence. No GO_CENTRAL defect. |

PprA is **not** a seed of the second IBD on the same node (GO:0007165 signal transduction);
FleS and CbrA in this batch are (see their notes). The node is PTHR43065 "sensor histidine
kinase", an appropriate home for a generic kinase/signalling term.

### Node-level note for PTN009166588 (recorded once, here)

The three *P. aeruginosa* genes in this batch that sit under PTN009166588 — pprA, fleS, cbrA —
receive the same pair of IBAs (GO:0000155, GO:0007165). Both IBDs are soundly seeded (see the
seed lists above and in `fleS-notes.md`), the node term suits a histidine-kinase clade, and
**no GO_CENTRAL defect is filed for this node**. The existing reviews of the other PAO1 sensor
kinases, `genes/PSEAE/parS` and `genes/PSEAE/PA5484` (KinB), reached the same conclusion for the
GO:0000155 IBA, and the TOO_GENERAL treatment of GO:0007165, GO:0016772, GO:0004673 and
GO:0016301/GO:0016740 is kept consistent with them.

## Annotation decisions

- GO:0000155 (IDA, IBA, IEA): ACCEPT. Direct biochemistry, agreeing IBA from a well-seeded node.
- GO:0000160 (IEA GO_REF:0000108, from the MF): ACCEPT — PprA/PprB are a cognate pair.
- GO:0004673, GO:0016772, GO:0007165 (IEA), GO:0007165 (IBA): TOO_GENERAL, each entailed by an
  accepted more specific term (GO:0000155 or GO:0000160).

No source defects: the single PseudoCAP row on this gene is a correct IDA.
