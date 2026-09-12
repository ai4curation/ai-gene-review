# AmiC2 (Ava_1466 / Q3MD47) — Anabaena variabilis ATCC 29413 (TRIV2) — Gene Review Notes

UniProt: **Q3MD47** (Q3MD47_TRIV2; unreviewed, TrEMBL), 627 aa, MW 68,156. Ordered locus
**Ava_1466**. Taxon NCBITaxon:240292 (*Trichormus/Anabaena variabilis* ATCC 29413 / PCC 7937).
UniProt SubName "Cell wall hydrolase/autolysin", EC 3.5.1.28
[file:TRIV2/AmiC2/AmiC2-uniprot.txt "SubName: Full=Cell wall hydrolase/autolysin"; "EC=3.5.1.28"].

## Orthology basis (this protein is NOT directly characterized)

Q3MD47 is **not itself experimentally characterized**. Its function is transferred by
**orthology (ISS)** from the directly-characterized AmiC2 of *Nostoc/Anabaena* sp. PCC 7120
(alr0093, UniProt A0ACD7S2F2) and *Nostoc punctiforme* (Npun_F1846).

Reciprocal-best-hit (RBH) analysis in `modules/septal_junction/RESULTS.md` assigns the
*A. variabilis* septal-junction module orthologs and, critically, disambiguates the tandem
amidase paralogs: **AmiC2 = Q3MD47, AmiC1 = Q3MD48** (a tandem pair mirroring the 7120
alr0093/alr0092 arrangement). The AmiC2 call is a forward best hit with **E = 0** and
**~96% identity** to the PCC 7120 AmiC2 exemplar (A0ACD7S2F2), and is reciprocal (the reverse
best hit from Q3MD47 returns A0ACD7S2F2). This near-identical, 1:1 reciprocal relationship
across the whole 627-aa protein (including both AMIN and Amidase_3 domains) supports transfer
of the characterized AmiC2 function to Q3MD47.

**Paralog disambiguation:** AmiC1 (Q3MD48) is the adjacent tandem paralog and must not be
conflated with AmiC2 (Q3MD47). In PCC 7120 the two amidases are partly redundant for nanopore
formation and cell–cell communication but not equivalent (e.g. AmiC1 but not AmiC2 is needed
for proper SepJ localization) [PMID:28929086]. This review concerns only AmiC2 (Q3MD47).

## Protein family / domain architecture

From the UniProt/InterPro record for Q3MD47:
- N-terminal **signal peptide** (residues 1–23; SignalP), consistent with export to the
  periplasmic/cell-wall compartment where septal peptidoglycan resides.
- Tandem **AMIN domain(s)** (InterPro IPR021731, Pfam PF11741 — two copies) in the N-terminal
  region: a septal/PG-targeting module that directs the enzyme to the division septum.
- C-terminal **N-acetylmuramoyl-L-alanine amidase catalytic domain, Amidase_3 / MurNAc-LAA**
  (InterPro IPR002508, Pfam PF01520, CDD cd02696, SMART SM00646; DOMAIN 512–621) — a
  **Zn-dependent amidase** (SUPFAM SSF53187, Zn-dependent exopeptidases). PANTHER family
  **PTHR30404** ("N-acetylmuramoyl-L-alanine amidase", subfamily SF0 "AmiC"), eggNOG COG0860.
- InterPro family IPR050695 "N-acetylmuramoyl_amidase_3".

This domain architecture (AMIN targeting + Amidase_3 catalytic, Zn-dependent, secreted) is
identical to that of the characterized 7120/N. punctiforme AmiC2.

## Molecular function — amidase activity (GO:0008745)

The characterized ortholog is a bona fide N-acetylmuramoyl-L-alanine amidase (EC 3.5.1.28)
that hydrolyses the bond between N-acetylmuramoyl residues and L-alanine in peptidoglycan.
The single-gene *amiC2* mutant of *N. punctiforme* "completely changes the morphology and
abrogates cell differentiation and intercellular communication"
[PMID:21244533 "mutation of a single gene, encoding cell wall amidase AmiC2, completely
changes the morphology and abrogates cell differentiation and intercellular communication"].
The GOA IEA amidase-activity assignment (InterPro IPR002508 / EC 3.5.1.28) for Q3MD47 is thus
consistent with both the catalytic domain and the orthologous biochemistry. ACCEPT.

## Biological process — septal PG remodelling / nanopore array / cell–cell communication

In PCC 7120 the AmiC2 ortholog perforates the septal peptidoglycan, creating the nanopore
array [PMID:28929086 "This enzyme perforates the septal peptidoglycan creating an array of
nanopores, which may be the framework for septal junction complexes"]. Inactivation of either
amidase reduces the nanopore array and impairs FRAP tracer exchange, and the double mutant
loses filament morphology and heterocyst differentiation [PMID:28929086 "Inactivation of
either amidase resulted in significant reduction in nanopore count and in the rate of
fluorescent tracer exchange between neighboring cells measured by FRAP analysis. In an amiC1
amiC2 double mutant, filament morphology was affected and heterocyst differentiation was
abolished"].

For Q3MD47 (by orthology, ISS):
- **GO:0009253 peptidoglycan catabolic process** — amidase cleavage of PG is PG catabolism
  (GOA IEA; ACCEPT).
- **GO:0071555 cell wall organization** — the amidase does not merely degrade PG but patterns
  the septal cross-wall into a nanopore array (NEW, ISS).
- **GO:0007267 cell-cell signaling** — the nanopore array is the conduit for septal junctions
  that connect neighbouring cytoplasms, so AmiC2 is required (upstream) for intercellular
  communication (NEW, ISS).

## Cellular localisation

The characterized AmiC2 localises to the division septum / cross-wall. AmiC2-GFP
"localizes in the cell wall with a focus in the cross walls of dividing cells"
[PMID:21244533], and in Anabaena AmiC2 "localizes to the newly formed septum and migrates
during septal invagination to cover the entire septal plane" [PMID:28929086].

- **GO:0030288 outer membrane-bounded periplasmic space** — the GOA IEA (TreeGrafter) call is
  defensible for a secreted amidase of a diderm cyanobacterium acting on periplasmic septal
  PG (ACCEPT), but is less informative than the septal localization.
- **GO:0030428 cell septum** — the more informative, orthology-supported location (NEW, ISS).

## Cited references (cached in publications/)

- **PMID:28929086** — Bornikoel et al. 2017, Front Cell Infect Microbiol — PRIMARY (Anabaena
  PCC 7120 amiC1/amiC2 mutants, nanopores, FRAP, heterocysts). Full text cached. Basis for
  orthology transfer to Q3MD47.
- **PMID:21244533** — Lehner et al. 2011, Mol Microbiol — "The morphogene AmiC2 is pivotal for
  multicellular development in Nostoc punctiforme." Abstract cached. Basis for orthology
  transfer to Q3MD47.
- Orthology/RBH evidence: `modules/septal_junction/RESULTS.md` (AmiC2 Q3MD47 / AmiC1 Q3MD48;
  E=0, ~96% identity, reciprocal best hit vs PCC 7120 A0ACD7S2F2).
