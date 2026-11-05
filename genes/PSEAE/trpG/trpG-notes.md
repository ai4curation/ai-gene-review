# trpG (PA0649, P20576) notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE P20576 --alias trpG` (accession fetch). Accession
P20576 matches the worklist. No deep-research keys; literature from the UniProt record and
cached publications (PMID:2153661 abstract-only, PMC208517 full text not retrievable;
PMID:23449919 full text cached). UniProt cites PMID:2105306 (not cached) for the trpG/trpE
disruption phenotype.

## Identity

- Glutamine amidotransferase (class I, GATase) small subunit of anthranilate synthase,
  201 aa, EC 4.1.3.27, MEROPS C26. With TrpE it forms the TrpEG heterotetramer; TrpG
  hydrolyses L-glutamine and supplies ammonia for the chorismate->anthranilate step
  [file:PSEAE/trpG/trpG-uniprot.txt "the glutamine-binding beta subunit (TrpG) of anthranilate synthase (AS)"].
- Paralog of PhnB (PA1002), the pyocyanin-pathway TrpG. PAO1 has no standalone pabA; PabB
  (PA1758, unreviewed Q9I2Y1) carries only the chorismate-binding domain, so a GATase
  subunit (TrpG or PhnB) must supply ammonia for folate-precursor ADC synthesis.

## Literature

- Two anthranilate synthases: TrpEG for tryptophan, PhnAB for pyocyanin; both inactivated
  in the chromosome
  [PMID:2153661 "One anthranilate synthase enzyme participates in tryptophan synthesis; its genes are designated trpE and trpG."];
  [PMID:2153661 "They were cloned, sequenced, inactivated in vitro by insertion of an antibiotic resistance gene, and returned to P. aeruginosa, replacing the wild-type gene."].
  Pseudomonas TrpE/TrpG are closer to E. coli PabB/PabA than to E. coli TrpE/TrpG
  [PMID:2153661 "Pseudomonas TrpE and TrpG are more closely related to E. coli PabB and PabA than to E. coli TrpE and TrpG"].
- trpEG mutants are tryptophan auxotrophs; TrpEG expressed at low density, PhnAB at high
  density [PMID:23449919 "trpEG mutants are tryptophan auxotrophs but produce PQS"].

## Annotation decisions

- L-tryptophan biosynthetic process (IBA, IEA, IMP): ACCEPT core.
- Anthranilate synthase activity (IEA, IMP): ACCEPT core; a PSEUDOCAP WRONG_QUALIFIER
  defect (CHECK, PROBABLE) on the IMP row requesting contributes_to (TrpG is one subunit
  of the heterotetramer), mirroring the phnB review.
- Amino acid biosynthetic process (IEA), aromatic amino acid biosynthetic process (IEA):
  TOO_GENERAL (entailed by GO:0000162).
- Tetrahydrofolate biosynthetic process (IBA, PTN000747575), 4-amino-4-deoxychorismate
  synthase activity (IBA, PTN000747575): KEEP_AS_NON_CORE. Seeded by E. coli PabA (P00903,
  experimental). Plausible for TrpG because PAO1 lacks a dedicated pabA and TrpG is PabA-like,
  but untested; left non-core rather than removed.
- Action counts: ACCEPT 5, TOO_GENERAL 2, KEEP_AS_NON_CORE 2. Defects: PSEUDOCAP 1.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000230074 | GO:0000162 L-tryptophan biosynthetic process | 8 | 149 (93 taxa) | GO:0000162, IMP, PMID:2153661 | SOUND | TrpEG inactivated in the chromosome and assigned to tryptophan synthesis; trpEG mutant is a tryptophan auxotroph (PMID:23449919). TrpG supplies the glutaminase half of the first committed step. | E. coli TrpGD P00904 (IDA/EXP GO:0000162), B. subtilis TrpG/PabA P28819 (IMP), yeast TRP3 S000001694, S. pombe trp3 SPBC1539.09c, plant ASB (Q7XUS2, Q764B9, AT1G25220) | Yes; several independent experimental seeds (E. coli, B. subtilis, yeast) |

The GO:0000162 IBD at PTN000230074 is a large (149-leaf, 93-taxon) anthranilate synthase
component II / GATase clade grounded in multiple experimental seeds, so the node term suits
the clade; no GO_CENTRAL defect. Only the PseudoCAP seed's qualifier (enables vs
contributes_to) is questioned. (This node is distinct from the phnB node PTN000230115, where
a separate phenazine/anthranilate-phosphoribosyltransferase propagation problem is recorded.)
