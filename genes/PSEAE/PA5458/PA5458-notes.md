# PA5458 notes

## Identity

- UniProt Q9HTB2 (unreviewed, PE 4), 380 aa, locus PA5458, no gene name.
- Pfam PF01757 Acyl_transf_3 (residues 7-341); InterPro IPR002656; PANTHER
  PTHR23028:SF53. Nine Phobius TM helices (7-26 ... 291-312), so a polytopic
  integral membrane protein, in a Gram-negative bacterium the cytoplasmic
  (inner) membrane.
- No deep-research provider available; literature research done manually
  (PubMed, cached full text of PMID:23341552).

## Literature

Only one paper studies PA5458: Hao et al. 2013 mBio, PMID:23341552 (full text cached).

- PA5458 is in the pa5455-pa5459 cluster adjacent to the CPA (common polysaccharide
  antigen, D-rhamnan O antigen) locus pa5447-pa5454; the 5-gene cluster is an operon
  and is required for CPA biosynthesis [PMID:23341552 "Here we demonstrate that an
  adjacent five-gene cluster pa5455-pa5459 is also involved"].
- Domain: [PMID:23341552 "The pa5458 gene encodes a protein with a conserved
  acetyltransferase domain."]
- In-frame deletion: CPA still made but altered. [PMID:23341552 "Mutation of the
  putative acetyltransferase-encoding gene pa5458 did not abrogate polysaccharide
  production"]; [PMID:23341552 "When the run time of SDS-PAGE was increased, it was
  clear that the bands produced by the mutant were shifted relative to the positions
  of bands produced by the wild type, and the bands also appeared to be more diffuse"];
  weaker MAb N1F10 binding to the mutant polymer [PMID:23341552 "Therefore, the fainter
  bands on the Western blot indicate weaker binding of MAb N1F10 to the mutant
  polymer."]. Complementation partly restored it.
- Overexpression: [PMID:23341552 "Overexpression of the putative acetyltransferase
  resulted in a modest reduction in the amount of CPA produced and a subtle shift in
  the chain length distribution"].
- Authors' interpretation: [PMID:23341552 "its function is clearly not required for
  assembly and processing of the polysaccharide, although the mutant produces CPA with
  a different structure, which is consistent with previous reports of the presence of
  acetylation substitutions in the sugars of CPA"].
- No chemical analysis of acetylation, no enzyme assay, no localisation experiment.
  Acetyltransferase activity is a domain-based prediction.

Assessment: PA5458 is very probably the membrane-bound O-acyltransferase that
decorates CPA (probably O-acetylation), i.e. a modification step of O-antigen
biosynthesis. The mutant phenotype (altered polymer structure, not merely amount)
fits the gene acting on the polymer itself, so involvement in O antigen
biosynthesis is acceptable at the gene level. The IDA evidence code on the
PseudoCAP O-antigen row is wrong: the evidence is mutant (IMP) and overexpression
analysis, not a direct assay.

## Family context

Acyltransferase-3 (AT3, PF01757) proteins are polytopic inner-membrane
acyltransferases that O-acylate cell-surface glycans, with different substrates in
different lineages: S. aureus OatA O-acetylates peptidoglycan muramic acid
[PMID:15661003 "the muramic acid of the oatA mutant lacked this modification"], and
Salmonella OafA acetylates O antigen. Both sit in the same PAINT node as PA5458
(see bioinformatics).

## PAINT node composition

See `PA5458-bioinformatics/RESULTS.md`.

- PTN000546841 (GO:0009103 LPS biosynthetic process; 31 leaves): 15 leaves are in
  organisms with no LPS (M. tuberculosis x5, S. coelicolor x4, S. aureus x2 incl. OatA,
  L. monocytogenes OatA, S. pneumoniae spr1868, B. subtilis YrhL, B. cereus).
- PTN000546715 (GO:0000271 polysaccharide biosynthetic process; 113 leaves): 109
  eukaryotic, 97 nematode. Nematode AT3 proteins have no known polysaccharide role.

Comparator check: S. aureus OatA (Q2FV54) and L. monocytogenes OatA (Q8Y7I6), whose
function is peptidoglycan O-acetylation, carry only IBA GO:0009103 for process in
QuickGO (queried 2026-10-28): the propagated term is wrong for them.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN000546841 | GO:0009103 lipopolysaccharide biosynthetic process | 1 | 31 | GO:0009103 IMP PMID:23341552 (plus GO:0009243 IDA, same paper) | WRONG | The seed is sound for PA5458 itself (the deletion alters CPA structure), but one Gram-negative O-antigen seed cannot justify LPS biosynthesis at a node that also contains Gram-positive peptidoglycan O-acetyltransferases (OatA of S. aureus and L. monocytogenes) and mycobacterial/streptomycete members: 15 of 31 leaves are in organisms that make no LPS. The node term should be withdrawn or moved to a Gram-negative O-antigen subclade (with OafA). |
| PTN000546715 | GO:0000271 polysaccharide biosynthetic process | 1 | 113 | GO:0009103 IMP PMID:23341552 (plus GO:0009243 IDA) | WRONG | Generalising one bacterial O-antigen modification phenotype to a deep node whose leaves are 109/113 eukaryotic (97 nematode, 9 oomycete) AT3 proteins of unknown function. The seed shows modification of an already made polymer, not synthesis; no evidence for polysaccharide synthesis in the propagated clade. |

Seed rows themselves: GO:0009103 IMP is acceptable but under-specific (the gene
already carries GO:0009243); GO:0009243 is the right term but its IDA code should be
IMP.
