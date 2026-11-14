# phnB (PA1002, P09786) notes

## 2026-10-28 review (PseudoCAP IBA-seed worklist, rank 96)

No deep-research provider keys were available; literature gathered by PubMed
search and from the cached publications. The completed reviews of phzM and phzS
in this repository were read for phenazine-pathway context.

### Identity

- UniProt P09786 (Swiss-Prot, PE 1), 200 aa, "Anthranilate synthase component 2,
  pyocyanine specific", EC 4.1.3.27, gene phnB (synonym trpG), locus PA1002
  [file:PSEAE/phnB/phnB-uniprot.txt].
- A single class I (triad) glutamine amidotransferase domain, residues 2-195
  (PROSITE PS51273, Pfam PF00117 GATase, CDD cd01743
  GATase1_Anthranilate_Synthase, NCBIfam TIGR00566 trpG_papA), with the
  catalytic Cys/His/Glu triad curated at 83, 169 and 171 and glutamine-binding
  residues at 56-58, 87 and 133-134 [file:PSEAE/phnB/phnB-uniprot.txt]. There is
  no phosphoribosyltransferase region: the protein is a standalone TrpG, not a
  TrpGD fusion. This matters for one of the IBAs reviewed below.
- PhnB works with the large subunit PhnA: "Heterotetramer consisting of two
  non-identical subunits: a beta subunit (PhnB) and a large alpha subunit
  (PhnA)" [file:PSEAE/phnB/phnB-uniprot.txt]. PAO1 has a second anthranilate
  synthase, TrpE/TrpG (P20580/P20576), for tryptophan biosynthesis.

### What PMID:2153661 (the seed reference) shows

- Essar et al. cloned, sequenced and insertionally inactivated both gene pairs
  and returned them to the chromosome [PMID:2153661 "The other anthranilate
  synthase enzyme, encoded by phnA and phnB, participates in the synthesis of
  pyocyanin, the characteristic phenazine pigment of the organism"].
- The functional evidence for anthranilate synthase activity is heterologous
  complementation [PMID:2153661 "The cloned phnA phnB gene pair complements trpE
  and trpE(G) mutants of Escherichia coli"], and the pigment evidence is a
  partial phenotype [PMID:2153661 "phnA mutants retain a low level of pyocyanin
  production"] that becomes complete only in combination
  [PMID:2153661 "Introduction of an inactivated trpE gene into a phnA mutant
  abolished residual pyocyanin production, suggesting that the trpE trpG gene
  products are capable of providing some anthranilate for pyocyanin synthesis"].
  Swiss-Prot records the phnB-side phenotype as
  "Single disruption in strain PA04290 results in decreased pyocyanine synthesis
  (PubMed:2153661)" [file:PSEAE/phnB/phnB-uniprot.txt].
- So the paper supports the molecular function (anthranilate synthase) well, and
  supports a pigment phenotype; it does not show that PhnAB performs any step of
  phenazine biosynthesis.

### Anthranilate is a PQS precursor, not a phenazine precursor

This is the crux of the "debated" point in the worklist, and the literature has
settled it:

- Palmer et al. state it directly [PMID:23449919 "At the time it was believed
  that PhnAB generated anthranilate for pyocyanin production, but later work
  determined that anthranilate is instead a precursor for PQS production, which
  is required to induce genes for pyocyanin biosynthesis"], and
  [PMID:23449919 "Based on its organization in an operon and
  quinolone-dependent regulation, PhnAB has probably evolved to generate
  anthranilate for quinolone biosynthesis"].
- PhnAB is the dominant source of that anthranilate under the conditions where
  PQS is made [PMID:23449919 "No detectable PQS was produced by Δ phnAB ,
  indicating that PhnAB is the anthranilate synthase responsible for PQS
  production in the presence of phenylalanine and tyrosine"], restored by feeding
  anthranilate [PMID:23449919 "Consistent with Farrow and Pesci’s observations,
  Δ phnAB PQS production is restored upon growth with anthranilate"], with
  tryptophan catabolism as the alternative route
  [PMID:17337571 "This compound can be derived from the conversion of chorismate
  to anthranilate by an anthranilate synthase or through the degradation of
  tryptophan via the anthranilate branch of the kynurenine pathway"].
- The phenazine core itself is built from chorismate without passing through
  anthranilate: PhzE is an ADIC synthase, not an anthranilate synthase
  [PMID:21454481 "PhzE utilizes chorismate and glutamine to synthesize
  2-amino-2-desoxyisochorismate (ADIC) in the first step of phenazine
  biosynthesis"], and the distinction has been checked against a close homologue
  [PMID:18646313 "PhzE has the sequence signature of an anthranilate synthase,
  but recent evidence indicates that it catalyzes the production of
  2-amino-2-deoxyisochorismate [corrected] (ADIC), an intermediate in the
  two-step anthranilate synthase reaction, not anthranilate"].
- UniProt's current FUNCTION line says the same thing, with experimental evidence
  codes: PhnAB makes "anthranilate, a precursor for Pseudomonas quinolone signal
  (2-heptyl-3-hydroxy-4-quinolone; PQS) production which is required to induce
  the genes for the biosynthesis of the virulence factor pyocyanine"
  [file:PSEAE/phnB/phnB-uniprot.txt].

So phnB's link to phenazines runs through a diffusible signal and transcriptional
induction, which is the textbook shape of an indirect phenotype.

### Tryptophan biosynthesis

PhnAB and TrpEG are interchangeable in principle but differentially regulated:
trpE deletion revertants with a non-feedback-inhibited anthranilate synthase
arise from PhnAB [PMID:2153661 "The anthranilate synthase of these revertants is
not feedback inhibited by tryptophan, suggesting that it arises from PhnAB"], and
"Double phnA-phnB deletions are tryptophan prototrophs"
[file:PSEAE/phnB/phnB-uniprot.txt]. Palmer et al. explain the asymmetry by
expression timing [PMID:23449919 "At low cell densities PhnAB expression is low
and TrpEG is the primary anthranilate synthase enzyme present"]. So the
tryptophan-pathway IBA is defensible but not this gene's physiological job.

### PAINT nodes (phnB-bioinformatics/RESULTS.md)

- PTN000230115 (PTHR43418:SF2, Gammaproteobacteria, 7 leaves/7 organisms) carries
  two IBDs: GO:0002047 phenazine biosynthetic process, sole-seeded by this gene,
  and GO:0004048 anthranilate phosphoribosyltransferase activity, sole-seeded by
  E. coli P00904. The leaves are trpG of H. influenzae, V. cholerae, Y. pestis
  and Shewanella, the TrpGD fusions of E. coli and Salmonella, and phnB. GOA has
  267 rows for each term with this node in with/from (7 GO_Central, 260
  TreeGrafter).
- PTN000230074 (family LUCA node, 149 leaves) carries the GO:0000162 and
  GO:0004049 IBDs, with 8 and 2 seeds respectively.

Two distinct problems follow. Phenazine biosynthesis is asserted for the TrpG
proteins of organisms that make no phenazines (E. coli, Salmonella, Haemophilus,
Yersinia, Vibrio, Shewanella). And anthranilate phosphoribosyltransferase
activity, which in the seed P00904 comes from the fused TrpD region of a
531-residue bifunctional protein, is asserted for 200-residue standalone GATase
subunits that have no such domain.

### Annotation decisions

- GO:0004049 anthranilate synthase activity (IMP, IEA): ACCEPT, core; the
  reaction belongs to the PhnA-PhnB heterotetramer, so contributes_to would be
  the better qualifier.
- GO:0002047 phenazine biosynthetic process (IMP, IBA): MARK_AS_OVER_ANNOTATED.
  Defects to PSEUDOCAP (the seed row) and GO_CENTRAL (the node IBD).
- GO:0004048 anthranilate phosphoribosyltransferase activity (IBA): REMOVE, with
  a GO_CENTRAL defect: a fusion-protein artefact.
- GO:0000162 L-tryptophan biosynthetic process (IBA): KEEP_AS_NON_CORE.
- Proposed a process term for PQS (2-heptyl-3-hydroxy-4(1H)-quinolone)
  biosynthesis, which GO lacks although it has the synthase activity term
  GO:0102164.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN000230115 | GO:0002047 phenazine biosynthetic process | 1 (sole) | 7 GO_Central (267 GOA rows incl. TreeGrafter) | GO:0002047, IMP, PMID:2153661 | INDIRECT-PHENOTYPE | The seed is the reduced pyocyanin of a phn mutant (and only partially reduced: phnA mutants retain low-level production, abolished only when trpE is also inactivated). PhnAB is an anthranilate synthase, and anthranilate is the precursor of PQS, not of the phenazine core, which PhzE builds from chorismate via ADIC; PQS then induces the phz genes. So the pigment phenotype is a signalling effect, two steps removed from phenazine biosynthesis. The node is also the wrong place for the term even if it were right for phnB: its other six leaves are the TrpG and TrpGD proteins of E. coli, Salmonella, Haemophilus, Yersinia, Vibrio and Shewanella, none of which make phenazines, and the term has reached 267 GOA rows. |

Separate finding at the same node, not PseudoCAP-seeded: the GO:0004048
anthranilate phosphoribosyltransferase IBD (sole seed E. coli P00904, the
531-residue bifunctional TrpGD) is propagated to standalone 200-residue GATase
subunits such as phnB that lack the TrpD region entirely. Verdict for that IBD:
WRONG (fusion-protein artefact); reviewed on the phnB IBA row with a GO_CENTRAL
defect.
