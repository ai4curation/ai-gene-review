# AmiC2 (FJSC11DRAFT_3096 / G6FW05) — Fischerella thermalis JSC-11 (FISTH) — Gene Review Notes

UniProt: **G6FW05** (G6FW05_9CYAN; unreviewed, TrEMBL), 616 aa, MW 66,924. ORF name
**FJSC11DRAFT_3096**. Taxon NCBITaxon:741277 (*Fischerella thermalis* JSC-11, a filamentous,
true-branching, heterocyst-forming cyanobacterium of the order Nostocales /
Hapalosiphonaceae — the "Stigonematales" morphotype). UniProt SubName "Cell wall
hydrolase/autolysin" with EC 3.5.1.28
[file:FISTH/AmiC2/AmiC2-uniprot.txt "SubName: Full=Cell wall hydrolase/autolysin"].

## Orthology basis (this protein is NOT directly characterized)

G6FW05 is **not itself experimentally characterized**. Its function is transferred by
**orthology (ISS)** from the directly-characterized AmiC2 of *Nostoc/Anabaena* sp. PCC 7120
(alr0093, UniProt A0ACD7S2F2) and *Nostoc punctiforme* (Npun_F1846).

Reciprocal-best-hit (RBH) analysis in `modules/septal_junction/RESULTS.md` identifies the
*F. thermalis* septal-junction module orthologs and assigns **AmiC2 = G6FW05**. The AmiC2 call
is a forward best hit with **E = 4.3e-250** and **63.8% identity** to the PCC 7120 AmiC2
exemplar (A0ACD7S2F2), and it is reciprocal (the reverse best hit from G6FW05 returns
A0ACD7S2F2). This 1:1 reciprocal relationship across the whole protein (both AMIN and
Amidase_3 domains) supports transfer of the characterized AmiC2 function to G6FW05.

## Tandem AmiC1/AmiC2 pair retained in this deep Stigonematales lineage (comparative note)

Unlike *Cylindrospermum stagnale* (K9X2S2) and *Chlorogloeopsis fritschii*, which each carry
only a **single AmiC** (the AmiC2 ortholog; the AmiC1 exemplar's best hit reverse-maps to
AmiC2), *F. thermalis* **retains the tandem AmiC1/AmiC2 amidase pair**: this AmiC2
(**FJSC11DRAFT_3096 / G6FW05**) plus a distinct AmiC1 ortholog **FJSC11DRAFT_3094 / G6FW03**
[modules/septal_junction/RESULTS.md "*Fischerella thermalis* (Stigonematales) has **both** an
AmiC2 ortholog (G6FW05 / FJSC11DRAFT_3096) and an AmiC1 ortholog (G6FW03 / FJSC11DRAFT_3094)"].
Because the duplication is present in both *Nostoc/Anabaena* and the deep-branching
*Fischerella*, the most parsimonious reading is an **ancestral AmiC1/AmiC2 duplication with
lineage-specific AmiC1 loss** in *Cylindrospermum* and *Chlorogloeopsis*, rather than a
*Nostoc/Anabaena*-specific event. This review concerns AmiC2 (FJSC11DRAFT_3096); the paralog
AmiC1 (FJSC11DRAFT_3094) is a distinct gene.

## Protein family / domain architecture

From the UniProt/InterPro record for G6FW05:
- N-terminal **signal peptide** (residues 1–24; SignalP), consistent with export to the
  periplasmic/cell-wall compartment where septal peptidoglycan resides.
- **AMIN domain(s)** (InterPro IPR021731, Pfam PF11741 — two copies) in the N-terminal
  region: a septal/PG-targeting module that directs the enzyme to the division septum.
- C-terminal **N-acetylmuramoyl-L-alanine amidase catalytic domain, Amidase_3 / MurNAc-LAA**
  (InterPro IPR002508, Pfam PF01520, CDD cd02696, SMART SM00646; DOMAIN 501–610) — a
  **Zn-dependent amidase** (SUPFAM SSF53187, Zn-dependent exopeptidases; Gene3D 3.40.630.40).
  PANTHER family **PTHR30404** ("N-acetylmuramoyl-L-alanine amidase", subfamily SF0 "AmiC").
- InterPro family IPR050695 "N-acetylmuramoyl_amidase_3". EC 3.5.1.28.

This domain architecture (AMIN targeting + Amidase_3 catalytic, Zn-dependent, secreted) is
identical to that of the characterized 7120/*N. punctiforme* AmiC2.

## Molecular function — amidase activity (GO:0008745)

The characterized ortholog is a bona fide N-acetylmuramoyl-L-alanine amidase (EC 3.5.1.28)
that hydrolyses the bond between N-acetylmuramoyl residues and L-alanine in peptidoglycan.
The single-gene *amiC2* mutant of *N. punctiforme*
[PMID:21244533 "mutation of a single gene, encoding cell wall amidase AmiC2, completely
changes the morphology and abrogates cell differentiation and intercellular communication"].
The GOA IEA amidase-activity assignment (InterPro IPR002508 / PANTHER PTN002018865) for
G6FW05 is thus consistent with both the catalytic domain and the orthologous biochemistry.
ACCEPT.

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

For G6FW05 (by orthology, ISS):
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
  orthology transfer to G6FW05.
- **PMID:21244533** — Lehner et al. 2011, Mol Microbiol — "The morphogene AmiC2 is pivotal for
  multicellular development in Nostoc punctiforme." Abstract cached. Basis for orthology
  transfer to G6FW05.
- Orthology/RBH evidence: `modules/septal_junction/RESULTS.md` (AmiC2 = G6FW05; forward
  E=4.3e-250, 63.8% identity, reciprocal best hit vs PCC 7120 A0ACD7S2F2; tandem AmiC1 =
  G6FW03 / FJSC11DRAFT_3094 retained in this Stigonematales genome).
